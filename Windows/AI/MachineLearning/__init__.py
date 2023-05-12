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
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.AI.MachineLearning
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Graphics
import Windows.Graphics.DirectX.Direct3D11
import Windows.Graphics.Imaging
import Windows.Media
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
class IImageFeatureDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.IImageFeatureDescriptor'
    _iid_ = Guid('{365585a5-171a-4a2a-985f-265159d3895a}')
    @winrt_commethod(6)
    def get_BitmapPixelFormat(self) -> Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_commethod(7)
    def get_BitmapAlphaMode(self) -> Windows.Graphics.Imaging.BitmapAlphaMode: ...
    @winrt_commethod(8)
    def get_Width(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_Height(self) -> UInt32: ...
    BitmapPixelFormat = property(get_BitmapPixelFormat, None)
    BitmapAlphaMode = property(get_BitmapAlphaMode, None)
    Width = property(get_Width, None)
    Height = property(get_Height, None)
class IImageFeatureDescriptor2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.IImageFeatureDescriptor2'
    _iid_ = Guid('{2b27cca7-d533-5862-bb98-1611b155b0e1}')
    @winrt_commethod(6)
    def get_PixelRange(self) -> Windows.AI.MachineLearning.LearningModelPixelRange: ...
    PixelRange = property(get_PixelRange, None)
class IImageFeatureValue(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.IImageFeatureValue'
    _iid_ = Guid('{f0414fd9-c9aa-4405-b7fb-94f87c8a3037}')
    @winrt_commethod(6)
    def get_VideoFrame(self) -> Windows.Media.VideoFrame: ...
    VideoFrame = property(get_VideoFrame, None)
class IImageFeatureValueStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.IImageFeatureValueStatics'
    _iid_ = Guid('{1bc317fd-23cb-4610-b085-c8e1c87ebaa0}')
    @winrt_commethod(6)
    def CreateFromVideoFrame(self, image: Windows.Media.VideoFrame) -> Windows.AI.MachineLearning.ImageFeatureValue: ...
class ILearningModel(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModel'
    _iid_ = Guid('{5b8e4920-489f-4e86-9128-265a327b78fa}')
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
    def get_InputFeatures(self) -> Windows.Foundation.Collections.IVectorView[Windows.AI.MachineLearning.ILearningModelFeatureDescriptor]: ...
    @winrt_commethod(13)
    def get_OutputFeatures(self) -> Windows.Foundation.Collections.IVectorView[Windows.AI.MachineLearning.ILearningModelFeatureDescriptor]: ...
    Author = property(get_Author, None)
    Name = property(get_Name, None)
    Domain = property(get_Domain, None)
    Description = property(get_Description, None)
    Version = property(get_Version, None)
    Metadata = property(get_Metadata, None)
    InputFeatures = property(get_InputFeatures, None)
    OutputFeatures = property(get_OutputFeatures, None)
class ILearningModelBinding(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelBinding'
    _iid_ = Guid('{ea312f20-168f-4f8c-94fe-2e7ac31b4aa8}')
    @winrt_commethod(6)
    def Bind(self, name: WinRT_String, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(7)
    def BindWithProperties(self, name: WinRT_String, value: Windows.Win32.System.WinRT.IInspectable_head, props: Windows.Foundation.Collections.IPropertySet) -> Void: ...
    @winrt_commethod(8)
    def Clear(self) -> Void: ...
class ILearningModelBindingFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelBindingFactory'
    _iid_ = Guid('{c95f7a7a-e788-475e-8917-23aa381faf0b}')
    @winrt_commethod(6)
    def CreateFromSession(self, session: Windows.AI.MachineLearning.LearningModelSession) -> Windows.AI.MachineLearning.LearningModelBinding: ...
class ILearningModelDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelDevice'
    _iid_ = Guid('{f5c2c8fe-3f56-4a8c-ac5f-fdb92d8b8252}')
    @winrt_commethod(6)
    def get_AdapterId(self) -> Windows.Graphics.DisplayAdapterId: ...
    @winrt_commethod(7)
    def get_Direct3D11Device(self) -> Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice: ...
    AdapterId = property(get_AdapterId, None)
    Direct3D11Device = property(get_Direct3D11Device, None)
class ILearningModelDeviceFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelDeviceFactory'
    _iid_ = Guid('{9cffd74d-b1e5-4f20-80ad-0a56690db06b}')
    @winrt_commethod(6)
    def Create(self, deviceKind: Windows.AI.MachineLearning.LearningModelDeviceKind) -> Windows.AI.MachineLearning.LearningModelDevice: ...
class ILearningModelDeviceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelDeviceStatics'
    _iid_ = Guid('{49f32107-a8bf-42bb-92c7-10b12dc5d21f}')
    @winrt_commethod(6)
    def CreateFromDirect3D11Device(self, device: Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice) -> Windows.AI.MachineLearning.LearningModelDevice: ...
class ILearningModelEvaluationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelEvaluationResult'
    _iid_ = Guid('{b2f9bfcd-960e-49c0-8593-eb190ae3eee2}')
    @winrt_commethod(6)
    def get_CorrelationId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ErrorStatus(self) -> Int32: ...
    @winrt_commethod(8)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Outputs(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    CorrelationId = property(get_CorrelationId, None)
    ErrorStatus = property(get_ErrorStatus, None)
    Succeeded = property(get_Succeeded, None)
    Outputs = property(get_Outputs, None)
class ILearningModelFeatureDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelFeatureDescriptor'
    _iid_ = Guid('{bc08cf7c-6ed0-4004-97ba-b9a2eecd2b4f}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Kind(self) -> Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_commethod(9)
    def get_IsRequired(self) -> Boolean: ...
    Name = property(get_Name, None)
    Description = property(get_Description, None)
    Kind = property(get_Kind, None)
    IsRequired = property(get_IsRequired, None)
class ILearningModelFeatureValue(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelFeatureValue'
    _iid_ = Guid('{f51005db-4085-4dfe-9fed-95eb0c0cf75c}')
    @winrt_commethod(6)
    def get_Kind(self) -> Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    Kind = property(get_Kind, None)
class ILearningModelOperatorProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelOperatorProvider'
    _iid_ = Guid('{2a222e5d-afb1-47ed-bfad-b5b3a459ec04}')
class ILearningModelSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelSession'
    _iid_ = Guid('{8e58f8f6-b787-4c11-90f0-7129aeca74a9}')
    @winrt_commethod(6)
    def get_Model(self) -> Windows.AI.MachineLearning.LearningModel: ...
    @winrt_commethod(7)
    def get_Device(self) -> Windows.AI.MachineLearning.LearningModelDevice: ...
    @winrt_commethod(8)
    def get_EvaluationProperties(self) -> Windows.Foundation.Collections.IPropertySet: ...
    @winrt_commethod(9)
    def EvaluateAsync(self, bindings: Windows.AI.MachineLearning.LearningModelBinding, correlationId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.AI.MachineLearning.LearningModelEvaluationResult]: ...
    @winrt_commethod(10)
    def EvaluateFeaturesAsync(self, features: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], correlationId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.AI.MachineLearning.LearningModelEvaluationResult]: ...
    @winrt_commethod(11)
    def Evaluate(self, bindings: Windows.AI.MachineLearning.LearningModelBinding, correlationId: WinRT_String) -> Windows.AI.MachineLearning.LearningModelEvaluationResult: ...
    @winrt_commethod(12)
    def EvaluateFeatures(self, features: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], correlationId: WinRT_String) -> Windows.AI.MachineLearning.LearningModelEvaluationResult: ...
    Model = property(get_Model, None)
    Device = property(get_Device, None)
    EvaluationProperties = property(get_EvaluationProperties, None)
class ILearningModelSessionFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelSessionFactory'
    _iid_ = Guid('{0f6b881d-1c9b-47b6-bfe0-f1cf62a67579}')
    @winrt_commethod(6)
    def CreateFromModel(self, model: Windows.AI.MachineLearning.LearningModel) -> Windows.AI.MachineLearning.LearningModelSession: ...
    @winrt_commethod(7)
    def CreateFromModelOnDevice(self, model: Windows.AI.MachineLearning.LearningModel, deviceToRunOn: Windows.AI.MachineLearning.LearningModelDevice) -> Windows.AI.MachineLearning.LearningModelSession: ...
class ILearningModelSessionFactory2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelSessionFactory2'
    _iid_ = Guid('{4e5c88bf-0a1f-5fec-ade0-2fd91e4ef29b}')
    @winrt_commethod(6)
    def CreateFromModelOnDeviceWithSessionOptions(self, model: Windows.AI.MachineLearning.LearningModel, deviceToRunOn: Windows.AI.MachineLearning.LearningModelDevice, learningModelSessionOptions: Windows.AI.MachineLearning.LearningModelSessionOptions) -> Windows.AI.MachineLearning.LearningModelSession: ...
class ILearningModelSessionOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelSessionOptions'
    _iid_ = Guid('{b8f63fa1-134d-5133-8cff-3a5c3c263beb}')
    @winrt_commethod(6)
    def get_BatchSizeOverride(self) -> UInt32: ...
    @winrt_commethod(7)
    def put_BatchSizeOverride(self, value: UInt32) -> Void: ...
    BatchSizeOverride = property(get_BatchSizeOverride, put_BatchSizeOverride)
class ILearningModelSessionOptions2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelSessionOptions2'
    _iid_ = Guid('{6fcd1dc4-175f-5bd2-8de5-2f2006a25adf}')
    @winrt_commethod(6)
    def get_CloseModelOnSessionCreation(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_CloseModelOnSessionCreation(self, value: Boolean) -> Void: ...
    CloseModelOnSessionCreation = property(get_CloseModelOnSessionCreation, put_CloseModelOnSessionCreation)
class ILearningModelSessionOptions3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelSessionOptions3'
    _iid_ = Guid('{58e15cee-d8c2-56fc-92e8-76d751081086}')
    @winrt_commethod(6)
    def OverrideNamedDimension(self, name: WinRT_String, dimension: UInt32) -> Void: ...
class ILearningModelStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelStatics'
    _iid_ = Guid('{e3b977e8-6952-4e47-8ef4-1f7f07897c6d}')
    @winrt_commethod(6)
    def LoadFromStorageFileAsync(self, modelFile: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Windows.AI.MachineLearning.LearningModel]: ...
    @winrt_commethod(7)
    def LoadFromStreamAsync(self, modelStream: Windows.Storage.Streams.IRandomAccessStreamReference) -> Windows.Foundation.IAsyncOperation[Windows.AI.MachineLearning.LearningModel]: ...
    @winrt_commethod(8)
    def LoadFromFilePath(self, filePath: WinRT_String) -> Windows.AI.MachineLearning.LearningModel: ...
    @winrt_commethod(9)
    def LoadFromStream(self, modelStream: Windows.Storage.Streams.IRandomAccessStreamReference) -> Windows.AI.MachineLearning.LearningModel: ...
    @winrt_commethod(10)
    def LoadFromStorageFileWithOperatorProviderAsync(self, modelFile: Windows.Storage.IStorageFile, operatorProvider: Windows.AI.MachineLearning.ILearningModelOperatorProvider) -> Windows.Foundation.IAsyncOperation[Windows.AI.MachineLearning.LearningModel]: ...
    @winrt_commethod(11)
    def LoadFromStreamWithOperatorProviderAsync(self, modelStream: Windows.Storage.Streams.IRandomAccessStreamReference, operatorProvider: Windows.AI.MachineLearning.ILearningModelOperatorProvider) -> Windows.Foundation.IAsyncOperation[Windows.AI.MachineLearning.LearningModel]: ...
    @winrt_commethod(12)
    def LoadFromFilePathWithOperatorProvider(self, filePath: WinRT_String, operatorProvider: Windows.AI.MachineLearning.ILearningModelOperatorProvider) -> Windows.AI.MachineLearning.LearningModel: ...
    @winrt_commethod(13)
    def LoadFromStreamWithOperatorProvider(self, modelStream: Windows.Storage.Streams.IRandomAccessStreamReference, operatorProvider: Windows.AI.MachineLearning.ILearningModelOperatorProvider) -> Windows.AI.MachineLearning.LearningModel: ...
class IMapFeatureDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.IMapFeatureDescriptor'
    _iid_ = Guid('{530424bd-a257-436d-9e60-c2981f7cc5c4}')
    @winrt_commethod(6)
    def get_KeyKind(self) -> Windows.AI.MachineLearning.TensorKind: ...
    @winrt_commethod(7)
    def get_ValueDescriptor(self) -> Windows.AI.MachineLearning.ILearningModelFeatureDescriptor: ...
    KeyKind = property(get_KeyKind, None)
    ValueDescriptor = property(get_ValueDescriptor, None)
class ISequenceFeatureDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ISequenceFeatureDescriptor'
    _iid_ = Guid('{84f6945a-562b-4d62-a851-739aced96668}')
    @winrt_commethod(6)
    def get_ElementDescriptor(self) -> Windows.AI.MachineLearning.ILearningModelFeatureDescriptor: ...
    ElementDescriptor = property(get_ElementDescriptor, None)
class ITensor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensor'
    _iid_ = Guid('{05489593-a305-4a25-ad09-440119b4b7f6}')
    @winrt_commethod(6)
    def get_TensorKind(self) -> Windows.AI.MachineLearning.TensorKind: ...
    @winrt_commethod(7)
    def get_Shape(self) -> Windows.Foundation.Collections.IVectorView[Int64]: ...
    TensorKind = property(get_TensorKind, None)
    Shape = property(get_Shape, None)
class ITensorBoolean(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorBoolean'
    _iid_ = Guid('{50f311ed-29e9-4a5c-a44d-8fc512584eed}')
    @winrt_commethod(6)
    def GetAsVectorView(self) -> Windows.Foundation.Collections.IVectorView[Boolean]: ...
class ITensorBooleanStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorBooleanStatics'
    _iid_ = Guid('{2796862c-2357-49a7-b476-d0aa3dfe6866}')
    @winrt_commethod(6)
    def Create(self) -> Windows.AI.MachineLearning.TensorBoolean: ...
    @winrt_commethod(7)
    def Create2(self, shape: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorBoolean: ...
    @winrt_commethod(8)
    def CreateFromArray(self, shape: Windows.Foundation.Collections.IIterable[Int64], data: POINTER(Boolean)) -> Windows.AI.MachineLearning.TensorBoolean: ...
    @winrt_commethod(9)
    def CreateFromIterable(self, shape: Windows.Foundation.Collections.IIterable[Int64], data: Windows.Foundation.Collections.IIterable[Boolean]) -> Windows.AI.MachineLearning.TensorBoolean: ...
class ITensorBooleanStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorBooleanStatics2'
    _iid_ = Guid('{a3a4a501-6a2d-52d7-b04b-c435baee0115}')
    @winrt_commethod(6)
    def CreateFromShapeArrayAndDataArray(self, shape: POINTER(Int64), data: POINTER(Boolean)) -> Windows.AI.MachineLearning.TensorBoolean: ...
    @winrt_commethod(7)
    def CreateFromBuffer(self, shape: POINTER(Int64), buffer: Windows.Storage.Streams.IBuffer) -> Windows.AI.MachineLearning.TensorBoolean: ...
class ITensorDouble(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorDouble'
    _iid_ = Guid('{91e41252-7a8f-4f0e-a28f-9637ffc8a3d0}')
    @winrt_commethod(6)
    def GetAsVectorView(self) -> Windows.Foundation.Collections.IVectorView[Double]: ...
class ITensorDoubleStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorDoubleStatics'
    _iid_ = Guid('{a86693c5-9538-44e7-a3ca-5df374a5a70c}')
    @winrt_commethod(6)
    def Create(self) -> Windows.AI.MachineLearning.TensorDouble: ...
    @winrt_commethod(7)
    def Create2(self, shape: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorDouble: ...
    @winrt_commethod(8)
    def CreateFromArray(self, shape: Windows.Foundation.Collections.IIterable[Int64], data: POINTER(Double)) -> Windows.AI.MachineLearning.TensorDouble: ...
    @winrt_commethod(9)
    def CreateFromIterable(self, shape: Windows.Foundation.Collections.IIterable[Int64], data: Windows.Foundation.Collections.IIterable[Double]) -> Windows.AI.MachineLearning.TensorDouble: ...
class ITensorDoubleStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorDoubleStatics2'
    _iid_ = Guid('{93a570de-5e9a-5094-85c8-592c655e68ac}')
    @winrt_commethod(6)
    def CreateFromShapeArrayAndDataArray(self, shape: POINTER(Int64), data: POINTER(Double)) -> Windows.AI.MachineLearning.TensorDouble: ...
    @winrt_commethod(7)
    def CreateFromBuffer(self, shape: POINTER(Int64), buffer: Windows.Storage.Streams.IBuffer) -> Windows.AI.MachineLearning.TensorDouble: ...
class ITensorFeatureDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorFeatureDescriptor'
    _iid_ = Guid('{74455c80-946a-4310-a19c-ee0af028fce4}')
    @winrt_commethod(6)
    def get_TensorKind(self) -> Windows.AI.MachineLearning.TensorKind: ...
    @winrt_commethod(7)
    def get_Shape(self) -> Windows.Foundation.Collections.IVectorView[Int64]: ...
    TensorKind = property(get_TensorKind, None)
    Shape = property(get_Shape, None)
class ITensorFloat(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorFloat'
    _iid_ = Guid('{f2282d82-aa02-42c8-a0c8-df1efc9676e1}')
    @winrt_commethod(6)
    def GetAsVectorView(self) -> Windows.Foundation.Collections.IVectorView[Single]: ...
class ITensorFloat16Bit(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorFloat16Bit'
    _iid_ = Guid('{0ab994fc-5b89-4c3c-b5e4-5282a5316c0a}')
    @winrt_commethod(6)
    def GetAsVectorView(self) -> Windows.Foundation.Collections.IVectorView[Single]: ...
class ITensorFloat16BitStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorFloat16BitStatics'
    _iid_ = Guid('{a52db6f5-318a-44d4-820b-0cdc7054a84a}')
    @winrt_commethod(6)
    def Create(self) -> Windows.AI.MachineLearning.TensorFloat16Bit: ...
    @winrt_commethod(7)
    def Create2(self, shape: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorFloat16Bit: ...
    @winrt_commethod(8)
    def CreateFromArray(self, shape: Windows.Foundation.Collections.IIterable[Int64], data: POINTER(Single)) -> Windows.AI.MachineLearning.TensorFloat16Bit: ...
    @winrt_commethod(9)
    def CreateFromIterable(self, shape: Windows.Foundation.Collections.IIterable[Int64], data: Windows.Foundation.Collections.IIterable[Single]) -> Windows.AI.MachineLearning.TensorFloat16Bit: ...
class ITensorFloat16BitStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorFloat16BitStatics2'
    _iid_ = Guid('{68545726-2dc7-51bf-b470-0b344cc2a1bc}')
    @winrt_commethod(6)
    def CreateFromShapeArrayAndDataArray(self, shape: POINTER(Int64), data: POINTER(Single)) -> Windows.AI.MachineLearning.TensorFloat16Bit: ...
    @winrt_commethod(7)
    def CreateFromBuffer(self, shape: POINTER(Int64), buffer: Windows.Storage.Streams.IBuffer) -> Windows.AI.MachineLearning.TensorFloat16Bit: ...
class ITensorFloatStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorFloatStatics'
    _iid_ = Guid('{dbcd395b-3ba3-452f-b10d-3c135e573fa9}')
    @winrt_commethod(6)
    def Create(self) -> Windows.AI.MachineLearning.TensorFloat: ...
    @winrt_commethod(7)
    def Create2(self, shape: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorFloat: ...
    @winrt_commethod(8)
    def CreateFromArray(self, shape: Windows.Foundation.Collections.IIterable[Int64], data: POINTER(Single)) -> Windows.AI.MachineLearning.TensorFloat: ...
    @winrt_commethod(9)
    def CreateFromIterable(self, shape: Windows.Foundation.Collections.IIterable[Int64], data: Windows.Foundation.Collections.IIterable[Single]) -> Windows.AI.MachineLearning.TensorFloat: ...
class ITensorFloatStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorFloatStatics2'
    _iid_ = Guid('{24610bc1-5e44-5713-b281-8f4ad4d555e8}')
    @winrt_commethod(6)
    def CreateFromShapeArrayAndDataArray(self, shape: POINTER(Int64), data: POINTER(Single)) -> Windows.AI.MachineLearning.TensorFloat: ...
    @winrt_commethod(7)
    def CreateFromBuffer(self, shape: POINTER(Int64), buffer: Windows.Storage.Streams.IBuffer) -> Windows.AI.MachineLearning.TensorFloat: ...
class ITensorInt16Bit(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorInt16Bit'
    _iid_ = Guid('{98a32d39-e6d6-44af-8afa-baebc44dc020}')
    @winrt_commethod(6)
    def GetAsVectorView(self) -> Windows.Foundation.Collections.IVectorView[Int16]: ...
class ITensorInt16BitStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorInt16BitStatics'
    _iid_ = Guid('{98646293-266e-4b1a-821f-e60d70898b91}')
    @winrt_commethod(6)
    def Create(self) -> Windows.AI.MachineLearning.TensorInt16Bit: ...
    @winrt_commethod(7)
    def Create2(self, shape: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorInt16Bit: ...
    @winrt_commethod(8)
    def CreateFromArray(self, shape: Windows.Foundation.Collections.IIterable[Int64], data: POINTER(Int16)) -> Windows.AI.MachineLearning.TensorInt16Bit: ...
    @winrt_commethod(9)
    def CreateFromIterable(self, shape: Windows.Foundation.Collections.IIterable[Int64], data: Windows.Foundation.Collections.IIterable[Int16]) -> Windows.AI.MachineLearning.TensorInt16Bit: ...
class ITensorInt16BitStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorInt16BitStatics2'
    _iid_ = Guid('{0cd70cf4-696c-5e5f-95d8-5ebf9670148b}')
    @winrt_commethod(6)
    def CreateFromShapeArrayAndDataArray(self, shape: POINTER(Int64), data: POINTER(Int16)) -> Windows.AI.MachineLearning.TensorInt16Bit: ...
    @winrt_commethod(7)
    def CreateFromBuffer(self, shape: POINTER(Int64), buffer: Windows.Storage.Streams.IBuffer) -> Windows.AI.MachineLearning.TensorInt16Bit: ...
class ITensorInt32Bit(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorInt32Bit'
    _iid_ = Guid('{2c0c28d3-207c-4486-a7d2-884522c5e589}')
    @winrt_commethod(6)
    def GetAsVectorView(self) -> Windows.Foundation.Collections.IVectorView[Int32]: ...
class ITensorInt32BitStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorInt32BitStatics'
    _iid_ = Guid('{6539864b-52fa-4e35-907c-834cac417b50}')
    @winrt_commethod(6)
    def Create(self) -> Windows.AI.MachineLearning.TensorInt32Bit: ...
    @winrt_commethod(7)
    def Create2(self, shape: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorInt32Bit: ...
    @winrt_commethod(8)
    def CreateFromArray(self, shape: Windows.Foundation.Collections.IIterable[Int64], data: POINTER(Int32)) -> Windows.AI.MachineLearning.TensorInt32Bit: ...
    @winrt_commethod(9)
    def CreateFromIterable(self, shape: Windows.Foundation.Collections.IIterable[Int64], data: Windows.Foundation.Collections.IIterable[Int32]) -> Windows.AI.MachineLearning.TensorInt32Bit: ...
class ITensorInt32BitStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorInt32BitStatics2'
    _iid_ = Guid('{7c4b079a-e956-5ce0-a3bd-157d9d79b5ec}')
    @winrt_commethod(6)
    def CreateFromShapeArrayAndDataArray(self, shape: POINTER(Int64), data: POINTER(Int32)) -> Windows.AI.MachineLearning.TensorInt32Bit: ...
    @winrt_commethod(7)
    def CreateFromBuffer(self, shape: POINTER(Int64), buffer: Windows.Storage.Streams.IBuffer) -> Windows.AI.MachineLearning.TensorInt32Bit: ...
class ITensorInt64Bit(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorInt64Bit'
    _iid_ = Guid('{499665ba-1fa2-45ad-af25-a0bd9bda4c87}')
    @winrt_commethod(6)
    def GetAsVectorView(self) -> Windows.Foundation.Collections.IVectorView[Int64]: ...
class ITensorInt64BitStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorInt64BitStatics'
    _iid_ = Guid('{9648ad9d-1198-4d74-9517-783ab62b9cc2}')
    @winrt_commethod(6)
    def Create(self) -> Windows.AI.MachineLearning.TensorInt64Bit: ...
    @winrt_commethod(7)
    def Create2(self, shape: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorInt64Bit: ...
    @winrt_commethod(8)
    def CreateFromArray(self, shape: Windows.Foundation.Collections.IIterable[Int64], data: POINTER(Int64)) -> Windows.AI.MachineLearning.TensorInt64Bit: ...
    @winrt_commethod(9)
    def CreateFromIterable(self, shape: Windows.Foundation.Collections.IIterable[Int64], data: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorInt64Bit: ...
class ITensorInt64BitStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorInt64BitStatics2'
    _iid_ = Guid('{6d3d9dcb-ff40-5ec2-89fe-084e2b6bc6db}')
    @winrt_commethod(6)
    def CreateFromShapeArrayAndDataArray(self, shape: POINTER(Int64), data: POINTER(Int64)) -> Windows.AI.MachineLearning.TensorInt64Bit: ...
    @winrt_commethod(7)
    def CreateFromBuffer(self, shape: POINTER(Int64), buffer: Windows.Storage.Streams.IBuffer) -> Windows.AI.MachineLearning.TensorInt64Bit: ...
class ITensorInt8Bit(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorInt8Bit'
    _iid_ = Guid('{cddd97c5-ffd8-4fef-aefb-30e1a485b2ee}')
    @winrt_commethod(6)
    def GetAsVectorView(self) -> Windows.Foundation.Collections.IVectorView[Byte]: ...
class ITensorInt8BitStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorInt8BitStatics'
    _iid_ = Guid('{b1a12284-095c-4c76-a661-ac4cee1f3e8b}')
    @winrt_commethod(6)
    def Create(self) -> Windows.AI.MachineLearning.TensorInt8Bit: ...
    @winrt_commethod(7)
    def Create2(self, shape: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorInt8Bit: ...
    @winrt_commethod(8)
    def CreateFromArray(self, shape: Windows.Foundation.Collections.IIterable[Int64], data: c_char_p_no) -> Windows.AI.MachineLearning.TensorInt8Bit: ...
    @winrt_commethod(9)
    def CreateFromIterable(self, shape: Windows.Foundation.Collections.IIterable[Int64], data: Windows.Foundation.Collections.IIterable[Byte]) -> Windows.AI.MachineLearning.TensorInt8Bit: ...
class ITensorInt8BitStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorInt8BitStatics2'
    _iid_ = Guid('{c0d59637-c468-56fb-9535-c052bdb93dc0}')
    @winrt_commethod(6)
    def CreateFromShapeArrayAndDataArray(self, shape: POINTER(Int64), data: c_char_p_no) -> Windows.AI.MachineLearning.TensorInt8Bit: ...
    @winrt_commethod(7)
    def CreateFromBuffer(self, shape: POINTER(Int64), buffer: Windows.Storage.Streams.IBuffer) -> Windows.AI.MachineLearning.TensorInt8Bit: ...
class ITensorString(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorString'
    _iid_ = Guid('{582335c8-bdb1-4610-bc75-35e9cbf009b7}')
    @winrt_commethod(6)
    def GetAsVectorView(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
class ITensorStringStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorStringStatics'
    _iid_ = Guid('{83623324-cf26-4f17-a2d4-20ef8d097d53}')
    @winrt_commethod(6)
    def Create(self) -> Windows.AI.MachineLearning.TensorString: ...
    @winrt_commethod(7)
    def Create2(self, shape: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorString: ...
    @winrt_commethod(8)
    def CreateFromArray(self, shape: Windows.Foundation.Collections.IIterable[Int64], data: POINTER(WinRT_String)) -> Windows.AI.MachineLearning.TensorString: ...
    @winrt_commethod(9)
    def CreateFromIterable(self, shape: Windows.Foundation.Collections.IIterable[Int64], data: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.AI.MachineLearning.TensorString: ...
class ITensorStringStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorStringStatics2'
    _iid_ = Guid('{9e355ed0-c8e2-5254-9137-0193a3668fd8}')
    @winrt_commethod(6)
    def CreateFromShapeArrayAndDataArray(self, shape: POINTER(Int64), data: POINTER(WinRT_String)) -> Windows.AI.MachineLearning.TensorString: ...
class ITensorUInt16Bit(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorUInt16Bit'
    _iid_ = Guid('{68140f4b-23c0-42f3-81f6-a891c011bc3f}')
    @winrt_commethod(6)
    def GetAsVectorView(self) -> Windows.Foundation.Collections.IVectorView[UInt16]: ...
class ITensorUInt16BitStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorUInt16BitStatics'
    _iid_ = Guid('{5df745dd-028a-481a-a27c-c7e6435e52dd}')
    @winrt_commethod(6)
    def Create(self) -> Windows.AI.MachineLearning.TensorUInt16Bit: ...
    @winrt_commethod(7)
    def Create2(self, shape: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorUInt16Bit: ...
    @winrt_commethod(8)
    def CreateFromArray(self, shape: Windows.Foundation.Collections.IIterable[Int64], data: POINTER(UInt16)) -> Windows.AI.MachineLearning.TensorUInt16Bit: ...
    @winrt_commethod(9)
    def CreateFromIterable(self, shape: Windows.Foundation.Collections.IIterable[Int64], data: Windows.Foundation.Collections.IIterable[UInt16]) -> Windows.AI.MachineLearning.TensorUInt16Bit: ...
class ITensorUInt16BitStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorUInt16BitStatics2'
    _iid_ = Guid('{8af40c64-d69f-5315-9348-490877bbd642}')
    @winrt_commethod(6)
    def CreateFromShapeArrayAndDataArray(self, shape: POINTER(Int64), data: POINTER(UInt16)) -> Windows.AI.MachineLearning.TensorUInt16Bit: ...
    @winrt_commethod(7)
    def CreateFromBuffer(self, shape: POINTER(Int64), buffer: Windows.Storage.Streams.IBuffer) -> Windows.AI.MachineLearning.TensorUInt16Bit: ...
class ITensorUInt32Bit(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorUInt32Bit'
    _iid_ = Guid('{d8c9c2ff-7511-45a3-bfac-c38f370d2237}')
    @winrt_commethod(6)
    def GetAsVectorView(self) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
class ITensorUInt32BitStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorUInt32BitStatics'
    _iid_ = Guid('{417c3837-e773-4378-8e7f-0cc33dbea697}')
    @winrt_commethod(6)
    def Create(self) -> Windows.AI.MachineLearning.TensorUInt32Bit: ...
    @winrt_commethod(7)
    def Create2(self, shape: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorUInt32Bit: ...
    @winrt_commethod(8)
    def CreateFromArray(self, shape: Windows.Foundation.Collections.IIterable[Int64], data: POINTER(UInt32)) -> Windows.AI.MachineLearning.TensorUInt32Bit: ...
    @winrt_commethod(9)
    def CreateFromIterable(self, shape: Windows.Foundation.Collections.IIterable[Int64], data: Windows.Foundation.Collections.IIterable[UInt32]) -> Windows.AI.MachineLearning.TensorUInt32Bit: ...
class ITensorUInt32BitStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorUInt32BitStatics2'
    _iid_ = Guid('{ef1a1f1c-314e-569d-b496-5c8447d20cd2}')
    @winrt_commethod(6)
    def CreateFromShapeArrayAndDataArray(self, shape: POINTER(Int64), data: POINTER(UInt32)) -> Windows.AI.MachineLearning.TensorUInt32Bit: ...
    @winrt_commethod(7)
    def CreateFromBuffer(self, shape: POINTER(Int64), buffer: Windows.Storage.Streams.IBuffer) -> Windows.AI.MachineLearning.TensorUInt32Bit: ...
class ITensorUInt64Bit(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorUInt64Bit'
    _iid_ = Guid('{2e70ffad-04bf-4825-839a-82baef8c7886}')
    @winrt_commethod(6)
    def GetAsVectorView(self) -> Windows.Foundation.Collections.IVectorView[UInt64]: ...
class ITensorUInt64BitStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorUInt64BitStatics'
    _iid_ = Guid('{7a7e20eb-242f-47cb-a9c6-f602ecfbfee4}')
    @winrt_commethod(6)
    def Create(self) -> Windows.AI.MachineLearning.TensorUInt64Bit: ...
    @winrt_commethod(7)
    def Create2(self, shape: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorUInt64Bit: ...
    @winrt_commethod(8)
    def CreateFromArray(self, shape: Windows.Foundation.Collections.IIterable[Int64], data: POINTER(UInt64)) -> Windows.AI.MachineLearning.TensorUInt64Bit: ...
    @winrt_commethod(9)
    def CreateFromIterable(self, shape: Windows.Foundation.Collections.IIterable[Int64], data: Windows.Foundation.Collections.IIterable[UInt64]) -> Windows.AI.MachineLearning.TensorUInt64Bit: ...
class ITensorUInt64BitStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorUInt64BitStatics2'
    _iid_ = Guid('{085a687d-67e1-5b1e-b232-4fabe9ca20b3}')
    @winrt_commethod(6)
    def CreateFromShapeArrayAndDataArray(self, shape: POINTER(Int64), data: POINTER(UInt64)) -> Windows.AI.MachineLearning.TensorUInt64Bit: ...
    @winrt_commethod(7)
    def CreateFromBuffer(self, shape: POINTER(Int64), buffer: Windows.Storage.Streams.IBuffer) -> Windows.AI.MachineLearning.TensorUInt64Bit: ...
class ITensorUInt8Bit(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorUInt8Bit'
    _iid_ = Guid('{58e1ae27-622b-48e3-be22-d867aed1daac}')
    @winrt_commethod(6)
    def GetAsVectorView(self) -> Windows.Foundation.Collections.IVectorView[Byte]: ...
class ITensorUInt8BitStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorUInt8BitStatics'
    _iid_ = Guid('{05f67583-bc24-4220-8a41-2dcd8c5ed33c}')
    @winrt_commethod(6)
    def Create(self) -> Windows.AI.MachineLearning.TensorUInt8Bit: ...
    @winrt_commethod(7)
    def Create2(self, shape: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorUInt8Bit: ...
    @winrt_commethod(8)
    def CreateFromArray(self, shape: Windows.Foundation.Collections.IIterable[Int64], data: c_char_p_no) -> Windows.AI.MachineLearning.TensorUInt8Bit: ...
    @winrt_commethod(9)
    def CreateFromIterable(self, shape: Windows.Foundation.Collections.IIterable[Int64], data: Windows.Foundation.Collections.IIterable[Byte]) -> Windows.AI.MachineLearning.TensorUInt8Bit: ...
class ITensorUInt8BitStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorUInt8BitStatics2'
    _iid_ = Guid('{2ba042d6-373e-5a3a-a2fc-a6c41bd52789}')
    @winrt_commethod(6)
    def CreateFromShapeArrayAndDataArray(self, shape: POINTER(Int64), data: c_char_p_no) -> Windows.AI.MachineLearning.TensorUInt8Bit: ...
    @winrt_commethod(7)
    def CreateFromBuffer(self, shape: POINTER(Int64), buffer: Windows.Storage.Streams.IBuffer) -> Windows.AI.MachineLearning.TensorUInt8Bit: ...
class ImageFeatureDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.AI.MachineLearning.IImageFeatureDescriptor
    _classid_ = 'Windows.AI.MachineLearning.ImageFeatureDescriptor'
    @winrt_mixinmethod
    def get_BitmapPixelFormat(self: Windows.AI.MachineLearning.IImageFeatureDescriptor) -> Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_mixinmethod
    def get_BitmapAlphaMode(self: Windows.AI.MachineLearning.IImageFeatureDescriptor) -> Windows.Graphics.Imaging.BitmapAlphaMode: ...
    @winrt_mixinmethod
    def get_Width(self: Windows.AI.MachineLearning.IImageFeatureDescriptor) -> UInt32: ...
    @winrt_mixinmethod
    def get_Height(self: Windows.AI.MachineLearning.IImageFeatureDescriptor) -> UInt32: ...
    @winrt_mixinmethod
    def get_PixelRange(self: Windows.AI.MachineLearning.IImageFeatureDescriptor2) -> Windows.AI.MachineLearning.LearningModelPixelRange: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def get_IsRequired(self: Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> Boolean: ...
    BitmapPixelFormat = property(get_BitmapPixelFormat, None)
    BitmapAlphaMode = property(get_BitmapAlphaMode, None)
    Width = property(get_Width, None)
    Height = property(get_Height, None)
    PixelRange = property(get_PixelRange, None)
    Name = property(get_Name, None)
    Description = property(get_Description, None)
    Kind = property(get_Kind, None)
    IsRequired = property(get_IsRequired, None)
class ImageFeatureValue(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.AI.MachineLearning.IImageFeatureValue
    _classid_ = 'Windows.AI.MachineLearning.ImageFeatureValue'
    @winrt_mixinmethod
    def get_VideoFrame(self: Windows.AI.MachineLearning.IImageFeatureValue) -> Windows.Media.VideoFrame: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.AI.MachineLearning.ILearningModelFeatureValue) -> Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_classmethod
    def CreateFromVideoFrame(cls: Windows.AI.MachineLearning.IImageFeatureValueStatics, image: Windows.Media.VideoFrame) -> Windows.AI.MachineLearning.ImageFeatureValue: ...
    VideoFrame = property(get_VideoFrame, None)
    Kind = property(get_Kind, None)
class LearningModel(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.AI.MachineLearning.ILearningModel
    _classid_ = 'Windows.AI.MachineLearning.LearningModel'
    @winrt_mixinmethod
    def get_Author(self: Windows.AI.MachineLearning.ILearningModel) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.AI.MachineLearning.ILearningModel) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Domain(self: Windows.AI.MachineLearning.ILearningModel) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.AI.MachineLearning.ILearningModel) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Version(self: Windows.AI.MachineLearning.ILearningModel) -> Int64: ...
    @winrt_mixinmethod
    def get_Metadata(self: Windows.AI.MachineLearning.ILearningModel) -> Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_InputFeatures(self: Windows.AI.MachineLearning.ILearningModel) -> Windows.Foundation.Collections.IVectorView[Windows.AI.MachineLearning.ILearningModelFeatureDescriptor]: ...
    @winrt_mixinmethod
    def get_OutputFeatures(self: Windows.AI.MachineLearning.ILearningModel) -> Windows.Foundation.Collections.IVectorView[Windows.AI.MachineLearning.ILearningModelFeatureDescriptor]: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def LoadFromStorageFileAsync(cls: Windows.AI.MachineLearning.ILearningModelStatics, modelFile: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Windows.AI.MachineLearning.LearningModel]: ...
    @winrt_classmethod
    def LoadFromStreamAsync(cls: Windows.AI.MachineLearning.ILearningModelStatics, modelStream: Windows.Storage.Streams.IRandomAccessStreamReference) -> Windows.Foundation.IAsyncOperation[Windows.AI.MachineLearning.LearningModel]: ...
    @winrt_classmethod
    def LoadFromFilePath(cls: Windows.AI.MachineLearning.ILearningModelStatics, filePath: WinRT_String) -> Windows.AI.MachineLearning.LearningModel: ...
    @winrt_classmethod
    def LoadFromStream(cls: Windows.AI.MachineLearning.ILearningModelStatics, modelStream: Windows.Storage.Streams.IRandomAccessStreamReference) -> Windows.AI.MachineLearning.LearningModel: ...
    @winrt_classmethod
    def LoadFromStorageFileWithOperatorProviderAsync(cls: Windows.AI.MachineLearning.ILearningModelStatics, modelFile: Windows.Storage.IStorageFile, operatorProvider: Windows.AI.MachineLearning.ILearningModelOperatorProvider) -> Windows.Foundation.IAsyncOperation[Windows.AI.MachineLearning.LearningModel]: ...
    @winrt_classmethod
    def LoadFromStreamWithOperatorProviderAsync(cls: Windows.AI.MachineLearning.ILearningModelStatics, modelStream: Windows.Storage.Streams.IRandomAccessStreamReference, operatorProvider: Windows.AI.MachineLearning.ILearningModelOperatorProvider) -> Windows.Foundation.IAsyncOperation[Windows.AI.MachineLearning.LearningModel]: ...
    @winrt_classmethod
    def LoadFromFilePathWithOperatorProvider(cls: Windows.AI.MachineLearning.ILearningModelStatics, filePath: WinRT_String, operatorProvider: Windows.AI.MachineLearning.ILearningModelOperatorProvider) -> Windows.AI.MachineLearning.LearningModel: ...
    @winrt_classmethod
    def LoadFromStreamWithOperatorProvider(cls: Windows.AI.MachineLearning.ILearningModelStatics, modelStream: Windows.Storage.Streams.IRandomAccessStreamReference, operatorProvider: Windows.AI.MachineLearning.ILearningModelOperatorProvider) -> Windows.AI.MachineLearning.LearningModel: ...
    Author = property(get_Author, None)
    Name = property(get_Name, None)
    Domain = property(get_Domain, None)
    Description = property(get_Description, None)
    Version = property(get_Version, None)
    Metadata = property(get_Metadata, None)
    InputFeatures = property(get_InputFeatures, None)
    OutputFeatures = property(get_OutputFeatures, None)
class LearningModelBinding(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.AI.MachineLearning.ILearningModelBinding
    _classid_ = 'Windows.AI.MachineLearning.LearningModelBinding'
    @winrt_factorymethod
    def CreateFromSession(cls: Windows.AI.MachineLearning.ILearningModelBindingFactory, session: Windows.AI.MachineLearning.LearningModelSession) -> Windows.AI.MachineLearning.LearningModelBinding: ...
    @winrt_mixinmethod
    def Bind(self: Windows.AI.MachineLearning.ILearningModelBinding, name: WinRT_String, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def BindWithProperties(self: Windows.AI.MachineLearning.ILearningModelBinding, name: WinRT_String, value: Windows.Win32.System.WinRT.IInspectable_head, props: Windows.Foundation.Collections.IPropertySet) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.AI.MachineLearning.ILearningModelBinding) -> Void: ...
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
class LearningModelDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.AI.MachineLearning.ILearningModelDevice
    _classid_ = 'Windows.AI.MachineLearning.LearningModelDevice'
    @winrt_factorymethod
    def Create(cls: Windows.AI.MachineLearning.ILearningModelDeviceFactory, deviceKind: Windows.AI.MachineLearning.LearningModelDeviceKind) -> Windows.AI.MachineLearning.LearningModelDevice: ...
    @winrt_mixinmethod
    def get_AdapterId(self: Windows.AI.MachineLearning.ILearningModelDevice) -> Windows.Graphics.DisplayAdapterId: ...
    @winrt_mixinmethod
    def get_Direct3D11Device(self: Windows.AI.MachineLearning.ILearningModelDevice) -> Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice: ...
    @winrt_classmethod
    def CreateFromDirect3D11Device(cls: Windows.AI.MachineLearning.ILearningModelDeviceStatics, device: Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice) -> Windows.AI.MachineLearning.LearningModelDevice: ...
    AdapterId = property(get_AdapterId, None)
    Direct3D11Device = property(get_Direct3D11Device, None)
LearningModelDeviceKind = Int32
LearningModelDeviceKind_Default: LearningModelDeviceKind = 0
LearningModelDeviceKind_Cpu: LearningModelDeviceKind = 1
LearningModelDeviceKind_DirectX: LearningModelDeviceKind = 2
LearningModelDeviceKind_DirectXHighPerformance: LearningModelDeviceKind = 3
LearningModelDeviceKind_DirectXMinPower: LearningModelDeviceKind = 4
class LearningModelEvaluationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.AI.MachineLearning.ILearningModelEvaluationResult
    _classid_ = 'Windows.AI.MachineLearning.LearningModelEvaluationResult'
    @winrt_mixinmethod
    def get_CorrelationId(self: Windows.AI.MachineLearning.ILearningModelEvaluationResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ErrorStatus(self: Windows.AI.MachineLearning.ILearningModelEvaluationResult) -> Int32: ...
    @winrt_mixinmethod
    def get_Succeeded(self: Windows.AI.MachineLearning.ILearningModelEvaluationResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_Outputs(self: Windows.AI.MachineLearning.ILearningModelEvaluationResult) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    CorrelationId = property(get_CorrelationId, None)
    ErrorStatus = property(get_ErrorStatus, None)
    Succeeded = property(get_Succeeded, None)
    Outputs = property(get_Outputs, None)
LearningModelFeatureKind = Int32
LearningModelFeatureKind_Tensor: LearningModelFeatureKind = 0
LearningModelFeatureKind_Sequence: LearningModelFeatureKind = 1
LearningModelFeatureKind_Map: LearningModelFeatureKind = 2
LearningModelFeatureKind_Image: LearningModelFeatureKind = 3
LearningModelPixelRange = Int32
LearningModelPixelRange_ZeroTo255: LearningModelPixelRange = 0
LearningModelPixelRange_ZeroToOne: LearningModelPixelRange = 1
LearningModelPixelRange_MinusOneToOne: LearningModelPixelRange = 2
class LearningModelSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.AI.MachineLearning.ILearningModelSession
    _classid_ = 'Windows.AI.MachineLearning.LearningModelSession'
    @winrt_factorymethod
    def CreateFromModelOnDeviceWithSessionOptions(cls: Windows.AI.MachineLearning.ILearningModelSessionFactory2, model: Windows.AI.MachineLearning.LearningModel, deviceToRunOn: Windows.AI.MachineLearning.LearningModelDevice, learningModelSessionOptions: Windows.AI.MachineLearning.LearningModelSessionOptions) -> Windows.AI.MachineLearning.LearningModelSession: ...
    @winrt_factorymethod
    def CreateFromModel(cls: Windows.AI.MachineLearning.ILearningModelSessionFactory, model: Windows.AI.MachineLearning.LearningModel) -> Windows.AI.MachineLearning.LearningModelSession: ...
    @winrt_factorymethod
    def CreateFromModelOnDevice(cls: Windows.AI.MachineLearning.ILearningModelSessionFactory, model: Windows.AI.MachineLearning.LearningModel, deviceToRunOn: Windows.AI.MachineLearning.LearningModelDevice) -> Windows.AI.MachineLearning.LearningModelSession: ...
    @winrt_mixinmethod
    def get_Model(self: Windows.AI.MachineLearning.ILearningModelSession) -> Windows.AI.MachineLearning.LearningModel: ...
    @winrt_mixinmethod
    def get_Device(self: Windows.AI.MachineLearning.ILearningModelSession) -> Windows.AI.MachineLearning.LearningModelDevice: ...
    @winrt_mixinmethod
    def get_EvaluationProperties(self: Windows.AI.MachineLearning.ILearningModelSession) -> Windows.Foundation.Collections.IPropertySet: ...
    @winrt_mixinmethod
    def EvaluateAsync(self: Windows.AI.MachineLearning.ILearningModelSession, bindings: Windows.AI.MachineLearning.LearningModelBinding, correlationId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.AI.MachineLearning.LearningModelEvaluationResult]: ...
    @winrt_mixinmethod
    def EvaluateFeaturesAsync(self: Windows.AI.MachineLearning.ILearningModelSession, features: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], correlationId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.AI.MachineLearning.LearningModelEvaluationResult]: ...
    @winrt_mixinmethod
    def Evaluate(self: Windows.AI.MachineLearning.ILearningModelSession, bindings: Windows.AI.MachineLearning.LearningModelBinding, correlationId: WinRT_String) -> Windows.AI.MachineLearning.LearningModelEvaluationResult: ...
    @winrt_mixinmethod
    def EvaluateFeatures(self: Windows.AI.MachineLearning.ILearningModelSession, features: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], correlationId: WinRT_String) -> Windows.AI.MachineLearning.LearningModelEvaluationResult: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Model = property(get_Model, None)
    Device = property(get_Device, None)
    EvaluationProperties = property(get_EvaluationProperties, None)
class LearningModelSessionOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.AI.MachineLearning.ILearningModelSessionOptions
    _classid_ = 'Windows.AI.MachineLearning.LearningModelSessionOptions'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.AI.MachineLearning.LearningModelSessionOptions: ...
    @winrt_mixinmethod
    def get_BatchSizeOverride(self: Windows.AI.MachineLearning.ILearningModelSessionOptions) -> UInt32: ...
    @winrt_mixinmethod
    def put_BatchSizeOverride(self: Windows.AI.MachineLearning.ILearningModelSessionOptions, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_CloseModelOnSessionCreation(self: Windows.AI.MachineLearning.ILearningModelSessionOptions2) -> Boolean: ...
    @winrt_mixinmethod
    def put_CloseModelOnSessionCreation(self: Windows.AI.MachineLearning.ILearningModelSessionOptions2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def OverrideNamedDimension(self: Windows.AI.MachineLearning.ILearningModelSessionOptions3, name: WinRT_String, dimension: UInt32) -> Void: ...
    BatchSizeOverride = property(get_BatchSizeOverride, put_BatchSizeOverride)
    CloseModelOnSessionCreation = property(get_CloseModelOnSessionCreation, put_CloseModelOnSessionCreation)
MachineLearningContract: UInt32 = 327680
class MapFeatureDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.AI.MachineLearning.IMapFeatureDescriptor
    _classid_ = 'Windows.AI.MachineLearning.MapFeatureDescriptor'
    @winrt_mixinmethod
    def get_KeyKind(self: Windows.AI.MachineLearning.IMapFeatureDescriptor) -> Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_ValueDescriptor(self: Windows.AI.MachineLearning.IMapFeatureDescriptor) -> Windows.AI.MachineLearning.ILearningModelFeatureDescriptor: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def get_IsRequired(self: Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> Boolean: ...
    KeyKind = property(get_KeyKind, None)
    ValueDescriptor = property(get_ValueDescriptor, None)
    Name = property(get_Name, None)
    Description = property(get_Description, None)
    Kind = property(get_Kind, None)
    IsRequired = property(get_IsRequired, None)
class SequenceFeatureDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.AI.MachineLearning.ISequenceFeatureDescriptor
    _classid_ = 'Windows.AI.MachineLearning.SequenceFeatureDescriptor'
    @winrt_mixinmethod
    def get_ElementDescriptor(self: Windows.AI.MachineLearning.ISequenceFeatureDescriptor) -> Windows.AI.MachineLearning.ILearningModelFeatureDescriptor: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def get_IsRequired(self: Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> Boolean: ...
    ElementDescriptor = property(get_ElementDescriptor, None)
    Name = property(get_Name, None)
    Description = property(get_Description, None)
    Kind = property(get_Kind, None)
    IsRequired = property(get_IsRequired, None)
class TensorBoolean(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.AI.MachineLearning.ITensorBoolean
    _classid_ = 'Windows.AI.MachineLearning.TensorBoolean'
    @winrt_mixinmethod
    def GetAsVectorView(self: Windows.AI.MachineLearning.ITensorBoolean) -> Windows.Foundation.Collections.IVectorView[Boolean]: ...
    @winrt_mixinmethod
    def get_TensorKind(self: Windows.AI.MachineLearning.ITensor) -> Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: Windows.AI.MachineLearning.ITensor) -> Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.AI.MachineLearning.ILearningModelFeatureValue) -> Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def CreateReference(self: Windows.Foundation.IMemoryBuffer) -> Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFromShapeArrayAndDataArray(cls: Windows.AI.MachineLearning.ITensorBooleanStatics2, shape: POINTER(Int64), data: POINTER(Boolean)) -> Windows.AI.MachineLearning.TensorBoolean: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: Windows.AI.MachineLearning.ITensorBooleanStatics2, shape: POINTER(Int64), buffer: Windows.Storage.Streams.IBuffer) -> Windows.AI.MachineLearning.TensorBoolean: ...
    @winrt_classmethod
    def Create(cls: Windows.AI.MachineLearning.ITensorBooleanStatics) -> Windows.AI.MachineLearning.TensorBoolean: ...
    @winrt_classmethod
    def Create2(cls: Windows.AI.MachineLearning.ITensorBooleanStatics, shape: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorBoolean: ...
    @winrt_classmethod
    def CreateFromArray(cls: Windows.AI.MachineLearning.ITensorBooleanStatics, shape: Windows.Foundation.Collections.IIterable[Int64], data: POINTER(Boolean)) -> Windows.AI.MachineLearning.TensorBoolean: ...
    @winrt_classmethod
    def CreateFromIterable(cls: Windows.AI.MachineLearning.ITensorBooleanStatics, shape: Windows.Foundation.Collections.IIterable[Int64], data: Windows.Foundation.Collections.IIterable[Boolean]) -> Windows.AI.MachineLearning.TensorBoolean: ...
    TensorKind = property(get_TensorKind, None)
    Shape = property(get_Shape, None)
    Kind = property(get_Kind, None)
class TensorDouble(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.AI.MachineLearning.ITensorDouble
    _classid_ = 'Windows.AI.MachineLearning.TensorDouble'
    @winrt_mixinmethod
    def GetAsVectorView(self: Windows.AI.MachineLearning.ITensorDouble) -> Windows.Foundation.Collections.IVectorView[Double]: ...
    @winrt_mixinmethod
    def get_TensorKind(self: Windows.AI.MachineLearning.ITensor) -> Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: Windows.AI.MachineLearning.ITensor) -> Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.AI.MachineLearning.ILearningModelFeatureValue) -> Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def CreateReference(self: Windows.Foundation.IMemoryBuffer) -> Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFromShapeArrayAndDataArray(cls: Windows.AI.MachineLearning.ITensorDoubleStatics2, shape: POINTER(Int64), data: POINTER(Double)) -> Windows.AI.MachineLearning.TensorDouble: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: Windows.AI.MachineLearning.ITensorDoubleStatics2, shape: POINTER(Int64), buffer: Windows.Storage.Streams.IBuffer) -> Windows.AI.MachineLearning.TensorDouble: ...
    @winrt_classmethod
    def Create(cls: Windows.AI.MachineLearning.ITensorDoubleStatics) -> Windows.AI.MachineLearning.TensorDouble: ...
    @winrt_classmethod
    def Create2(cls: Windows.AI.MachineLearning.ITensorDoubleStatics, shape: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorDouble: ...
    @winrt_classmethod
    def CreateFromArray(cls: Windows.AI.MachineLearning.ITensorDoubleStatics, shape: Windows.Foundation.Collections.IIterable[Int64], data: POINTER(Double)) -> Windows.AI.MachineLearning.TensorDouble: ...
    @winrt_classmethod
    def CreateFromIterable(cls: Windows.AI.MachineLearning.ITensorDoubleStatics, shape: Windows.Foundation.Collections.IIterable[Int64], data: Windows.Foundation.Collections.IIterable[Double]) -> Windows.AI.MachineLearning.TensorDouble: ...
    TensorKind = property(get_TensorKind, None)
    Shape = property(get_Shape, None)
    Kind = property(get_Kind, None)
class TensorFeatureDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.AI.MachineLearning.ITensorFeatureDescriptor
    _classid_ = 'Windows.AI.MachineLearning.TensorFeatureDescriptor'
    @winrt_mixinmethod
    def get_TensorKind(self: Windows.AI.MachineLearning.ITensorFeatureDescriptor) -> Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: Windows.AI.MachineLearning.ITensorFeatureDescriptor) -> Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def get_IsRequired(self: Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> Boolean: ...
    TensorKind = property(get_TensorKind, None)
    Shape = property(get_Shape, None)
    Name = property(get_Name, None)
    Description = property(get_Description, None)
    Kind = property(get_Kind, None)
    IsRequired = property(get_IsRequired, None)
class TensorFloat(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.AI.MachineLearning.ITensorFloat
    _classid_ = 'Windows.AI.MachineLearning.TensorFloat'
    @winrt_mixinmethod
    def GetAsVectorView(self: Windows.AI.MachineLearning.ITensorFloat) -> Windows.Foundation.Collections.IVectorView[Single]: ...
    @winrt_mixinmethod
    def get_TensorKind(self: Windows.AI.MachineLearning.ITensor) -> Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: Windows.AI.MachineLearning.ITensor) -> Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.AI.MachineLearning.ILearningModelFeatureValue) -> Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def CreateReference(self: Windows.Foundation.IMemoryBuffer) -> Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFromShapeArrayAndDataArray(cls: Windows.AI.MachineLearning.ITensorFloatStatics2, shape: POINTER(Int64), data: POINTER(Single)) -> Windows.AI.MachineLearning.TensorFloat: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: Windows.AI.MachineLearning.ITensorFloatStatics2, shape: POINTER(Int64), buffer: Windows.Storage.Streams.IBuffer) -> Windows.AI.MachineLearning.TensorFloat: ...
    @winrt_classmethod
    def Create(cls: Windows.AI.MachineLearning.ITensorFloatStatics) -> Windows.AI.MachineLearning.TensorFloat: ...
    @winrt_classmethod
    def Create2(cls: Windows.AI.MachineLearning.ITensorFloatStatics, shape: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorFloat: ...
    @winrt_classmethod
    def CreateFromArray(cls: Windows.AI.MachineLearning.ITensorFloatStatics, shape: Windows.Foundation.Collections.IIterable[Int64], data: POINTER(Single)) -> Windows.AI.MachineLearning.TensorFloat: ...
    @winrt_classmethod
    def CreateFromIterable(cls: Windows.AI.MachineLearning.ITensorFloatStatics, shape: Windows.Foundation.Collections.IIterable[Int64], data: Windows.Foundation.Collections.IIterable[Single]) -> Windows.AI.MachineLearning.TensorFloat: ...
    TensorKind = property(get_TensorKind, None)
    Shape = property(get_Shape, None)
    Kind = property(get_Kind, None)
class TensorFloat16Bit(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.AI.MachineLearning.ITensorFloat16Bit
    _classid_ = 'Windows.AI.MachineLearning.TensorFloat16Bit'
    @winrt_mixinmethod
    def GetAsVectorView(self: Windows.AI.MachineLearning.ITensorFloat16Bit) -> Windows.Foundation.Collections.IVectorView[Single]: ...
    @winrt_mixinmethod
    def get_TensorKind(self: Windows.AI.MachineLearning.ITensor) -> Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: Windows.AI.MachineLearning.ITensor) -> Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.AI.MachineLearning.ILearningModelFeatureValue) -> Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def CreateReference(self: Windows.Foundation.IMemoryBuffer) -> Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFromShapeArrayAndDataArray(cls: Windows.AI.MachineLearning.ITensorFloat16BitStatics2, shape: POINTER(Int64), data: POINTER(Single)) -> Windows.AI.MachineLearning.TensorFloat16Bit: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: Windows.AI.MachineLearning.ITensorFloat16BitStatics2, shape: POINTER(Int64), buffer: Windows.Storage.Streams.IBuffer) -> Windows.AI.MachineLearning.TensorFloat16Bit: ...
    @winrt_classmethod
    def Create(cls: Windows.AI.MachineLearning.ITensorFloat16BitStatics) -> Windows.AI.MachineLearning.TensorFloat16Bit: ...
    @winrt_classmethod
    def Create2(cls: Windows.AI.MachineLearning.ITensorFloat16BitStatics, shape: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorFloat16Bit: ...
    @winrt_classmethod
    def CreateFromArray(cls: Windows.AI.MachineLearning.ITensorFloat16BitStatics, shape: Windows.Foundation.Collections.IIterable[Int64], data: POINTER(Single)) -> Windows.AI.MachineLearning.TensorFloat16Bit: ...
    @winrt_classmethod
    def CreateFromIterable(cls: Windows.AI.MachineLearning.ITensorFloat16BitStatics, shape: Windows.Foundation.Collections.IIterable[Int64], data: Windows.Foundation.Collections.IIterable[Single]) -> Windows.AI.MachineLearning.TensorFloat16Bit: ...
    TensorKind = property(get_TensorKind, None)
    Shape = property(get_Shape, None)
    Kind = property(get_Kind, None)
class TensorInt16Bit(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.AI.MachineLearning.ITensorInt16Bit
    _classid_ = 'Windows.AI.MachineLearning.TensorInt16Bit'
    @winrt_mixinmethod
    def GetAsVectorView(self: Windows.AI.MachineLearning.ITensorInt16Bit) -> Windows.Foundation.Collections.IVectorView[Int16]: ...
    @winrt_mixinmethod
    def get_TensorKind(self: Windows.AI.MachineLearning.ITensor) -> Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: Windows.AI.MachineLearning.ITensor) -> Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.AI.MachineLearning.ILearningModelFeatureValue) -> Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def CreateReference(self: Windows.Foundation.IMemoryBuffer) -> Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFromShapeArrayAndDataArray(cls: Windows.AI.MachineLearning.ITensorInt16BitStatics2, shape: POINTER(Int64), data: POINTER(Int16)) -> Windows.AI.MachineLearning.TensorInt16Bit: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: Windows.AI.MachineLearning.ITensorInt16BitStatics2, shape: POINTER(Int64), buffer: Windows.Storage.Streams.IBuffer) -> Windows.AI.MachineLearning.TensorInt16Bit: ...
    @winrt_classmethod
    def Create(cls: Windows.AI.MachineLearning.ITensorInt16BitStatics) -> Windows.AI.MachineLearning.TensorInt16Bit: ...
    @winrt_classmethod
    def Create2(cls: Windows.AI.MachineLearning.ITensorInt16BitStatics, shape: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorInt16Bit: ...
    @winrt_classmethod
    def CreateFromArray(cls: Windows.AI.MachineLearning.ITensorInt16BitStatics, shape: Windows.Foundation.Collections.IIterable[Int64], data: POINTER(Int16)) -> Windows.AI.MachineLearning.TensorInt16Bit: ...
    @winrt_classmethod
    def CreateFromIterable(cls: Windows.AI.MachineLearning.ITensorInt16BitStatics, shape: Windows.Foundation.Collections.IIterable[Int64], data: Windows.Foundation.Collections.IIterable[Int16]) -> Windows.AI.MachineLearning.TensorInt16Bit: ...
    TensorKind = property(get_TensorKind, None)
    Shape = property(get_Shape, None)
    Kind = property(get_Kind, None)
class TensorInt32Bit(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.AI.MachineLearning.ITensorInt32Bit
    _classid_ = 'Windows.AI.MachineLearning.TensorInt32Bit'
    @winrt_mixinmethod
    def GetAsVectorView(self: Windows.AI.MachineLearning.ITensorInt32Bit) -> Windows.Foundation.Collections.IVectorView[Int32]: ...
    @winrt_mixinmethod
    def get_TensorKind(self: Windows.AI.MachineLearning.ITensor) -> Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: Windows.AI.MachineLearning.ITensor) -> Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.AI.MachineLearning.ILearningModelFeatureValue) -> Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def CreateReference(self: Windows.Foundation.IMemoryBuffer) -> Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFromShapeArrayAndDataArray(cls: Windows.AI.MachineLearning.ITensorInt32BitStatics2, shape: POINTER(Int64), data: POINTER(Int32)) -> Windows.AI.MachineLearning.TensorInt32Bit: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: Windows.AI.MachineLearning.ITensorInt32BitStatics2, shape: POINTER(Int64), buffer: Windows.Storage.Streams.IBuffer) -> Windows.AI.MachineLearning.TensorInt32Bit: ...
    @winrt_classmethod
    def Create(cls: Windows.AI.MachineLearning.ITensorInt32BitStatics) -> Windows.AI.MachineLearning.TensorInt32Bit: ...
    @winrt_classmethod
    def Create2(cls: Windows.AI.MachineLearning.ITensorInt32BitStatics, shape: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorInt32Bit: ...
    @winrt_classmethod
    def CreateFromArray(cls: Windows.AI.MachineLearning.ITensorInt32BitStatics, shape: Windows.Foundation.Collections.IIterable[Int64], data: POINTER(Int32)) -> Windows.AI.MachineLearning.TensorInt32Bit: ...
    @winrt_classmethod
    def CreateFromIterable(cls: Windows.AI.MachineLearning.ITensorInt32BitStatics, shape: Windows.Foundation.Collections.IIterable[Int64], data: Windows.Foundation.Collections.IIterable[Int32]) -> Windows.AI.MachineLearning.TensorInt32Bit: ...
    TensorKind = property(get_TensorKind, None)
    Shape = property(get_Shape, None)
    Kind = property(get_Kind, None)
class TensorInt64Bit(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.AI.MachineLearning.ITensorInt64Bit
    _classid_ = 'Windows.AI.MachineLearning.TensorInt64Bit'
    @winrt_mixinmethod
    def GetAsVectorView(self: Windows.AI.MachineLearning.ITensorInt64Bit) -> Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_TensorKind(self: Windows.AI.MachineLearning.ITensor) -> Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: Windows.AI.MachineLearning.ITensor) -> Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.AI.MachineLearning.ILearningModelFeatureValue) -> Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def CreateReference(self: Windows.Foundation.IMemoryBuffer) -> Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFromShapeArrayAndDataArray(cls: Windows.AI.MachineLearning.ITensorInt64BitStatics2, shape: POINTER(Int64), data: POINTER(Int64)) -> Windows.AI.MachineLearning.TensorInt64Bit: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: Windows.AI.MachineLearning.ITensorInt64BitStatics2, shape: POINTER(Int64), buffer: Windows.Storage.Streams.IBuffer) -> Windows.AI.MachineLearning.TensorInt64Bit: ...
    @winrt_classmethod
    def Create(cls: Windows.AI.MachineLearning.ITensorInt64BitStatics) -> Windows.AI.MachineLearning.TensorInt64Bit: ...
    @winrt_classmethod
    def Create2(cls: Windows.AI.MachineLearning.ITensorInt64BitStatics, shape: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorInt64Bit: ...
    @winrt_classmethod
    def CreateFromArray(cls: Windows.AI.MachineLearning.ITensorInt64BitStatics, shape: Windows.Foundation.Collections.IIterable[Int64], data: POINTER(Int64)) -> Windows.AI.MachineLearning.TensorInt64Bit: ...
    @winrt_classmethod
    def CreateFromIterable(cls: Windows.AI.MachineLearning.ITensorInt64BitStatics, shape: Windows.Foundation.Collections.IIterable[Int64], data: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorInt64Bit: ...
    TensorKind = property(get_TensorKind, None)
    Shape = property(get_Shape, None)
    Kind = property(get_Kind, None)
class TensorInt8Bit(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.AI.MachineLearning.ITensorInt8Bit
    _classid_ = 'Windows.AI.MachineLearning.TensorInt8Bit'
    @winrt_mixinmethod
    def GetAsVectorView(self: Windows.AI.MachineLearning.ITensorInt8Bit) -> Windows.Foundation.Collections.IVectorView[Byte]: ...
    @winrt_mixinmethod
    def get_TensorKind(self: Windows.AI.MachineLearning.ITensor) -> Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: Windows.AI.MachineLearning.ITensor) -> Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.AI.MachineLearning.ILearningModelFeatureValue) -> Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def CreateReference(self: Windows.Foundation.IMemoryBuffer) -> Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFromShapeArrayAndDataArray(cls: Windows.AI.MachineLearning.ITensorInt8BitStatics2, shape: POINTER(Int64), data: c_char_p_no) -> Windows.AI.MachineLearning.TensorInt8Bit: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: Windows.AI.MachineLearning.ITensorInt8BitStatics2, shape: POINTER(Int64), buffer: Windows.Storage.Streams.IBuffer) -> Windows.AI.MachineLearning.TensorInt8Bit: ...
    @winrt_classmethod
    def Create(cls: Windows.AI.MachineLearning.ITensorInt8BitStatics) -> Windows.AI.MachineLearning.TensorInt8Bit: ...
    @winrt_classmethod
    def Create2(cls: Windows.AI.MachineLearning.ITensorInt8BitStatics, shape: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorInt8Bit: ...
    @winrt_classmethod
    def CreateFromArray(cls: Windows.AI.MachineLearning.ITensorInt8BitStatics, shape: Windows.Foundation.Collections.IIterable[Int64], data: c_char_p_no) -> Windows.AI.MachineLearning.TensorInt8Bit: ...
    @winrt_classmethod
    def CreateFromIterable(cls: Windows.AI.MachineLearning.ITensorInt8BitStatics, shape: Windows.Foundation.Collections.IIterable[Int64], data: Windows.Foundation.Collections.IIterable[Byte]) -> Windows.AI.MachineLearning.TensorInt8Bit: ...
    TensorKind = property(get_TensorKind, None)
    Shape = property(get_Shape, None)
    Kind = property(get_Kind, None)
TensorKind = Int32
TensorKind_Undefined: TensorKind = 0
TensorKind_Float: TensorKind = 1
TensorKind_UInt8: TensorKind = 2
TensorKind_Int8: TensorKind = 3
TensorKind_UInt16: TensorKind = 4
TensorKind_Int16: TensorKind = 5
TensorKind_Int32: TensorKind = 6
TensorKind_Int64: TensorKind = 7
TensorKind_String: TensorKind = 8
TensorKind_Boolean: TensorKind = 9
TensorKind_Float16: TensorKind = 10
TensorKind_Double: TensorKind = 11
TensorKind_UInt32: TensorKind = 12
TensorKind_UInt64: TensorKind = 13
TensorKind_Complex64: TensorKind = 14
TensorKind_Complex128: TensorKind = 15
class TensorString(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.AI.MachineLearning.ITensorString
    _classid_ = 'Windows.AI.MachineLearning.TensorString'
    @winrt_mixinmethod
    def GetAsVectorView(self: Windows.AI.MachineLearning.ITensorString) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_TensorKind(self: Windows.AI.MachineLearning.ITensor) -> Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: Windows.AI.MachineLearning.ITensor) -> Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.AI.MachineLearning.ILearningModelFeatureValue) -> Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def CreateReference(self: Windows.Foundation.IMemoryBuffer) -> Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFromShapeArrayAndDataArray(cls: Windows.AI.MachineLearning.ITensorStringStatics2, shape: POINTER(Int64), data: POINTER(WinRT_String)) -> Windows.AI.MachineLearning.TensorString: ...
    @winrt_classmethod
    def Create(cls: Windows.AI.MachineLearning.ITensorStringStatics) -> Windows.AI.MachineLearning.TensorString: ...
    @winrt_classmethod
    def Create2(cls: Windows.AI.MachineLearning.ITensorStringStatics, shape: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorString: ...
    @winrt_classmethod
    def CreateFromArray(cls: Windows.AI.MachineLearning.ITensorStringStatics, shape: Windows.Foundation.Collections.IIterable[Int64], data: POINTER(WinRT_String)) -> Windows.AI.MachineLearning.TensorString: ...
    @winrt_classmethod
    def CreateFromIterable(cls: Windows.AI.MachineLearning.ITensorStringStatics, shape: Windows.Foundation.Collections.IIterable[Int64], data: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.AI.MachineLearning.TensorString: ...
    TensorKind = property(get_TensorKind, None)
    Shape = property(get_Shape, None)
    Kind = property(get_Kind, None)
class TensorUInt16Bit(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.AI.MachineLearning.ITensorUInt16Bit
    _classid_ = 'Windows.AI.MachineLearning.TensorUInt16Bit'
    @winrt_mixinmethod
    def GetAsVectorView(self: Windows.AI.MachineLearning.ITensorUInt16Bit) -> Windows.Foundation.Collections.IVectorView[UInt16]: ...
    @winrt_mixinmethod
    def get_TensorKind(self: Windows.AI.MachineLearning.ITensor) -> Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: Windows.AI.MachineLearning.ITensor) -> Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.AI.MachineLearning.ILearningModelFeatureValue) -> Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def CreateReference(self: Windows.Foundation.IMemoryBuffer) -> Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFromShapeArrayAndDataArray(cls: Windows.AI.MachineLearning.ITensorUInt16BitStatics2, shape: POINTER(Int64), data: POINTER(UInt16)) -> Windows.AI.MachineLearning.TensorUInt16Bit: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: Windows.AI.MachineLearning.ITensorUInt16BitStatics2, shape: POINTER(Int64), buffer: Windows.Storage.Streams.IBuffer) -> Windows.AI.MachineLearning.TensorUInt16Bit: ...
    @winrt_classmethod
    def Create(cls: Windows.AI.MachineLearning.ITensorUInt16BitStatics) -> Windows.AI.MachineLearning.TensorUInt16Bit: ...
    @winrt_classmethod
    def Create2(cls: Windows.AI.MachineLearning.ITensorUInt16BitStatics, shape: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorUInt16Bit: ...
    @winrt_classmethod
    def CreateFromArray(cls: Windows.AI.MachineLearning.ITensorUInt16BitStatics, shape: Windows.Foundation.Collections.IIterable[Int64], data: POINTER(UInt16)) -> Windows.AI.MachineLearning.TensorUInt16Bit: ...
    @winrt_classmethod
    def CreateFromIterable(cls: Windows.AI.MachineLearning.ITensorUInt16BitStatics, shape: Windows.Foundation.Collections.IIterable[Int64], data: Windows.Foundation.Collections.IIterable[UInt16]) -> Windows.AI.MachineLearning.TensorUInt16Bit: ...
    TensorKind = property(get_TensorKind, None)
    Shape = property(get_Shape, None)
    Kind = property(get_Kind, None)
class TensorUInt32Bit(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.AI.MachineLearning.ITensorUInt32Bit
    _classid_ = 'Windows.AI.MachineLearning.TensorUInt32Bit'
    @winrt_mixinmethod
    def GetAsVectorView(self: Windows.AI.MachineLearning.ITensorUInt32Bit) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_mixinmethod
    def get_TensorKind(self: Windows.AI.MachineLearning.ITensor) -> Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: Windows.AI.MachineLearning.ITensor) -> Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.AI.MachineLearning.ILearningModelFeatureValue) -> Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def CreateReference(self: Windows.Foundation.IMemoryBuffer) -> Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFromShapeArrayAndDataArray(cls: Windows.AI.MachineLearning.ITensorUInt32BitStatics2, shape: POINTER(Int64), data: POINTER(UInt32)) -> Windows.AI.MachineLearning.TensorUInt32Bit: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: Windows.AI.MachineLearning.ITensorUInt32BitStatics2, shape: POINTER(Int64), buffer: Windows.Storage.Streams.IBuffer) -> Windows.AI.MachineLearning.TensorUInt32Bit: ...
    @winrt_classmethod
    def Create(cls: Windows.AI.MachineLearning.ITensorUInt32BitStatics) -> Windows.AI.MachineLearning.TensorUInt32Bit: ...
    @winrt_classmethod
    def Create2(cls: Windows.AI.MachineLearning.ITensorUInt32BitStatics, shape: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorUInt32Bit: ...
    @winrt_classmethod
    def CreateFromArray(cls: Windows.AI.MachineLearning.ITensorUInt32BitStatics, shape: Windows.Foundation.Collections.IIterable[Int64], data: POINTER(UInt32)) -> Windows.AI.MachineLearning.TensorUInt32Bit: ...
    @winrt_classmethod
    def CreateFromIterable(cls: Windows.AI.MachineLearning.ITensorUInt32BitStatics, shape: Windows.Foundation.Collections.IIterable[Int64], data: Windows.Foundation.Collections.IIterable[UInt32]) -> Windows.AI.MachineLearning.TensorUInt32Bit: ...
    TensorKind = property(get_TensorKind, None)
    Shape = property(get_Shape, None)
    Kind = property(get_Kind, None)
class TensorUInt64Bit(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.AI.MachineLearning.ITensorUInt64Bit
    _classid_ = 'Windows.AI.MachineLearning.TensorUInt64Bit'
    @winrt_mixinmethod
    def GetAsVectorView(self: Windows.AI.MachineLearning.ITensorUInt64Bit) -> Windows.Foundation.Collections.IVectorView[UInt64]: ...
    @winrt_mixinmethod
    def get_TensorKind(self: Windows.AI.MachineLearning.ITensor) -> Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: Windows.AI.MachineLearning.ITensor) -> Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.AI.MachineLearning.ILearningModelFeatureValue) -> Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def CreateReference(self: Windows.Foundation.IMemoryBuffer) -> Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFromShapeArrayAndDataArray(cls: Windows.AI.MachineLearning.ITensorUInt64BitStatics2, shape: POINTER(Int64), data: POINTER(UInt64)) -> Windows.AI.MachineLearning.TensorUInt64Bit: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: Windows.AI.MachineLearning.ITensorUInt64BitStatics2, shape: POINTER(Int64), buffer: Windows.Storage.Streams.IBuffer) -> Windows.AI.MachineLearning.TensorUInt64Bit: ...
    @winrt_classmethod
    def Create(cls: Windows.AI.MachineLearning.ITensorUInt64BitStatics) -> Windows.AI.MachineLearning.TensorUInt64Bit: ...
    @winrt_classmethod
    def Create2(cls: Windows.AI.MachineLearning.ITensorUInt64BitStatics, shape: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorUInt64Bit: ...
    @winrt_classmethod
    def CreateFromArray(cls: Windows.AI.MachineLearning.ITensorUInt64BitStatics, shape: Windows.Foundation.Collections.IIterable[Int64], data: POINTER(UInt64)) -> Windows.AI.MachineLearning.TensorUInt64Bit: ...
    @winrt_classmethod
    def CreateFromIterable(cls: Windows.AI.MachineLearning.ITensorUInt64BitStatics, shape: Windows.Foundation.Collections.IIterable[Int64], data: Windows.Foundation.Collections.IIterable[UInt64]) -> Windows.AI.MachineLearning.TensorUInt64Bit: ...
    TensorKind = property(get_TensorKind, None)
    Shape = property(get_Shape, None)
    Kind = property(get_Kind, None)
class TensorUInt8Bit(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.AI.MachineLearning.ITensorUInt8Bit
    _classid_ = 'Windows.AI.MachineLearning.TensorUInt8Bit'
    @winrt_mixinmethod
    def GetAsVectorView(self: Windows.AI.MachineLearning.ITensorUInt8Bit) -> Windows.Foundation.Collections.IVectorView[Byte]: ...
    @winrt_mixinmethod
    def get_TensorKind(self: Windows.AI.MachineLearning.ITensor) -> Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: Windows.AI.MachineLearning.ITensor) -> Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.AI.MachineLearning.ILearningModelFeatureValue) -> Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def CreateReference(self: Windows.Foundation.IMemoryBuffer) -> Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFromShapeArrayAndDataArray(cls: Windows.AI.MachineLearning.ITensorUInt8BitStatics2, shape: POINTER(Int64), data: c_char_p_no) -> Windows.AI.MachineLearning.TensorUInt8Bit: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: Windows.AI.MachineLearning.ITensorUInt8BitStatics2, shape: POINTER(Int64), buffer: Windows.Storage.Streams.IBuffer) -> Windows.AI.MachineLearning.TensorUInt8Bit: ...
    @winrt_classmethod
    def Create(cls: Windows.AI.MachineLearning.ITensorUInt8BitStatics) -> Windows.AI.MachineLearning.TensorUInt8Bit: ...
    @winrt_classmethod
    def Create2(cls: Windows.AI.MachineLearning.ITensorUInt8BitStatics, shape: Windows.Foundation.Collections.IIterable[Int64]) -> Windows.AI.MachineLearning.TensorUInt8Bit: ...
    @winrt_classmethod
    def CreateFromArray(cls: Windows.AI.MachineLearning.ITensorUInt8BitStatics, shape: Windows.Foundation.Collections.IIterable[Int64], data: c_char_p_no) -> Windows.AI.MachineLearning.TensorUInt8Bit: ...
    @winrt_classmethod
    def CreateFromIterable(cls: Windows.AI.MachineLearning.ITensorUInt8BitStatics, shape: Windows.Foundation.Collections.IIterable[Int64], data: Windows.Foundation.Collections.IIterable[Byte]) -> Windows.AI.MachineLearning.TensorUInt8Bit: ...
    TensorKind = property(get_TensorKind, None)
    Shape = property(get_Shape, None)
    Kind = property(get_Kind, None)
make_head(_module, 'IImageFeatureDescriptor')
make_head(_module, 'IImageFeatureDescriptor2')
make_head(_module, 'IImageFeatureValue')
make_head(_module, 'IImageFeatureValueStatics')
make_head(_module, 'ILearningModel')
make_head(_module, 'ILearningModelBinding')
make_head(_module, 'ILearningModelBindingFactory')
make_head(_module, 'ILearningModelDevice')
make_head(_module, 'ILearningModelDeviceFactory')
make_head(_module, 'ILearningModelDeviceStatics')
make_head(_module, 'ILearningModelEvaluationResult')
make_head(_module, 'ILearningModelFeatureDescriptor')
make_head(_module, 'ILearningModelFeatureValue')
make_head(_module, 'ILearningModelOperatorProvider')
make_head(_module, 'ILearningModelSession')
make_head(_module, 'ILearningModelSessionFactory')
make_head(_module, 'ILearningModelSessionFactory2')
make_head(_module, 'ILearningModelSessionOptions')
make_head(_module, 'ILearningModelSessionOptions2')
make_head(_module, 'ILearningModelSessionOptions3')
make_head(_module, 'ILearningModelStatics')
make_head(_module, 'IMapFeatureDescriptor')
make_head(_module, 'ISequenceFeatureDescriptor')
make_head(_module, 'ITensor')
make_head(_module, 'ITensorBoolean')
make_head(_module, 'ITensorBooleanStatics')
make_head(_module, 'ITensorBooleanStatics2')
make_head(_module, 'ITensorDouble')
make_head(_module, 'ITensorDoubleStatics')
make_head(_module, 'ITensorDoubleStatics2')
make_head(_module, 'ITensorFeatureDescriptor')
make_head(_module, 'ITensorFloat')
make_head(_module, 'ITensorFloat16Bit')
make_head(_module, 'ITensorFloat16BitStatics')
make_head(_module, 'ITensorFloat16BitStatics2')
make_head(_module, 'ITensorFloatStatics')
make_head(_module, 'ITensorFloatStatics2')
make_head(_module, 'ITensorInt16Bit')
make_head(_module, 'ITensorInt16BitStatics')
make_head(_module, 'ITensorInt16BitStatics2')
make_head(_module, 'ITensorInt32Bit')
make_head(_module, 'ITensorInt32BitStatics')
make_head(_module, 'ITensorInt32BitStatics2')
make_head(_module, 'ITensorInt64Bit')
make_head(_module, 'ITensorInt64BitStatics')
make_head(_module, 'ITensorInt64BitStatics2')
make_head(_module, 'ITensorInt8Bit')
make_head(_module, 'ITensorInt8BitStatics')
make_head(_module, 'ITensorInt8BitStatics2')
make_head(_module, 'ITensorString')
make_head(_module, 'ITensorStringStatics')
make_head(_module, 'ITensorStringStatics2')
make_head(_module, 'ITensorUInt16Bit')
make_head(_module, 'ITensorUInt16BitStatics')
make_head(_module, 'ITensorUInt16BitStatics2')
make_head(_module, 'ITensorUInt32Bit')
make_head(_module, 'ITensorUInt32BitStatics')
make_head(_module, 'ITensorUInt32BitStatics2')
make_head(_module, 'ITensorUInt64Bit')
make_head(_module, 'ITensorUInt64BitStatics')
make_head(_module, 'ITensorUInt64BitStatics2')
make_head(_module, 'ITensorUInt8Bit')
make_head(_module, 'ITensorUInt8BitStatics')
make_head(_module, 'ITensorUInt8BitStatics2')
make_head(_module, 'ImageFeatureDescriptor')
make_head(_module, 'ImageFeatureValue')
make_head(_module, 'LearningModel')
make_head(_module, 'LearningModelBinding')
make_head(_module, 'LearningModelDevice')
make_head(_module, 'LearningModelEvaluationResult')
make_head(_module, 'LearningModelSession')
make_head(_module, 'LearningModelSessionOptions')
make_head(_module, 'MapFeatureDescriptor')
make_head(_module, 'SequenceFeatureDescriptor')
make_head(_module, 'TensorBoolean')
make_head(_module, 'TensorDouble')
make_head(_module, 'TensorFeatureDescriptor')
make_head(_module, 'TensorFloat')
make_head(_module, 'TensorFloat16Bit')
make_head(_module, 'TensorInt16Bit')
make_head(_module, 'TensorInt32Bit')
make_head(_module, 'TensorInt64Bit')
make_head(_module, 'TensorInt8Bit')
make_head(_module, 'TensorString')
make_head(_module, 'TensorUInt16Bit')
make_head(_module, 'TensorUInt32Bit')
make_head(_module, 'TensorUInt64Bit')
make_head(_module, 'TensorUInt8Bit')
