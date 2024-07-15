from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.AI.MachineLearning
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Graphics
import win32more.Windows.Graphics.DirectX.Direct3D11
import win32more.Windows.Graphics.Imaging
import win32more.Windows.Media
import win32more.Windows.Storage
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class IImageFeatureDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.IImageFeatureDescriptor'
    _iid_ = Guid('{365585a5-171a-4a2a-985f-265159d3895a}')
    @winrt_commethod(6)
    def get_BitmapPixelFormat(self) -> win32more.Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_commethod(7)
    def get_BitmapAlphaMode(self) -> win32more.Windows.Graphics.Imaging.BitmapAlphaMode: ...
    @winrt_commethod(8)
    def get_Width(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_Height(self) -> UInt32: ...
    BitmapAlphaMode = property(get_BitmapAlphaMode, None)
    BitmapPixelFormat = property(get_BitmapPixelFormat, None)
    Height = property(get_Height, None)
    Width = property(get_Width, None)
class IImageFeatureDescriptor2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.IImageFeatureDescriptor2'
    _iid_ = Guid('{2b27cca7-d533-5862-bb98-1611b155b0e1}')
    @winrt_commethod(6)
    def get_PixelRange(self) -> win32more.Windows.AI.MachineLearning.LearningModelPixelRange: ...
    PixelRange = property(get_PixelRange, None)
class IImageFeatureValue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.IImageFeatureValue'
    _iid_ = Guid('{f0414fd9-c9aa-4405-b7fb-94f87c8a3037}')
    @winrt_commethod(6)
    def get_VideoFrame(self) -> win32more.Windows.Media.VideoFrame: ...
    VideoFrame = property(get_VideoFrame, None)
class IImageFeatureValueStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.IImageFeatureValueStatics'
    _iid_ = Guid('{1bc317fd-23cb-4610-b085-c8e1c87ebaa0}')
    @winrt_commethod(6)
    def CreateFromVideoFrame(self, image: win32more.Windows.Media.VideoFrame) -> win32more.Windows.AI.MachineLearning.ImageFeatureValue: ...
class ILearningModel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    def get_Metadata(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_commethod(12)
    def get_InputFeatures(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.AI.MachineLearning.ILearningModelFeatureDescriptor]: ...
    @winrt_commethod(13)
    def get_OutputFeatures(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.AI.MachineLearning.ILearningModelFeatureDescriptor]: ...
    Author = property(get_Author, None)
    Description = property(get_Description, None)
    Domain = property(get_Domain, None)
    InputFeatures = property(get_InputFeatures, None)
    Metadata = property(get_Metadata, None)
    Name = property(get_Name, None)
    OutputFeatures = property(get_OutputFeatures, None)
    Version = property(get_Version, None)
class ILearningModelBinding(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelBinding'
    _iid_ = Guid('{ea312f20-168f-4f8c-94fe-2e7ac31b4aa8}')
    @winrt_commethod(6)
    def Bind(self, name: WinRT_String, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(7)
    def BindWithProperties(self, name: WinRT_String, value: win32more.Windows.Win32.System.WinRT.IInspectable, props: win32more.Windows.Foundation.Collections.IPropertySet) -> Void: ...
    @winrt_commethod(8)
    def Clear(self) -> Void: ...
class ILearningModelBindingFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelBindingFactory'
    _iid_ = Guid('{c95f7a7a-e788-475e-8917-23aa381faf0b}')
    @winrt_commethod(6)
    def CreateFromSession(self, session: win32more.Windows.AI.MachineLearning.LearningModelSession) -> win32more.Windows.AI.MachineLearning.LearningModelBinding: ...
class ILearningModelDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelDevice'
    _iid_ = Guid('{f5c2c8fe-3f56-4a8c-ac5f-fdb92d8b8252}')
    @winrt_commethod(6)
    def get_AdapterId(self) -> win32more.Windows.Graphics.DisplayAdapterId: ...
    @winrt_commethod(7)
    def get_Direct3D11Device(self) -> win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice: ...
    AdapterId = property(get_AdapterId, None)
    Direct3D11Device = property(get_Direct3D11Device, None)
class ILearningModelDeviceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelDeviceFactory'
    _iid_ = Guid('{9cffd74d-b1e5-4f20-80ad-0a56690db06b}')
    @winrt_commethod(6)
    def Create(self, deviceKind: win32more.Windows.AI.MachineLearning.LearningModelDeviceKind) -> win32more.Windows.AI.MachineLearning.LearningModelDevice: ...
class ILearningModelDeviceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelDeviceStatics'
    _iid_ = Guid('{49f32107-a8bf-42bb-92c7-10b12dc5d21f}')
    @winrt_commethod(6)
    def CreateFromDirect3D11Device(self, device: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice) -> win32more.Windows.AI.MachineLearning.LearningModelDevice: ...
class ILearningModelEvaluationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelEvaluationResult'
    _iid_ = Guid('{b2f9bfcd-960e-49c0-8593-eb190ae3eee2}')
    @winrt_commethod(6)
    def get_CorrelationId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ErrorStatus(self) -> Int32: ...
    @winrt_commethod(8)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Outputs(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    CorrelationId = property(get_CorrelationId, None)
    ErrorStatus = property(get_ErrorStatus, None)
    Outputs = property(get_Outputs, None)
    Succeeded = property(get_Succeeded, None)
class ILearningModelFeatureDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelFeatureDescriptor'
    _iid_ = Guid('{bc08cf7c-6ed0-4004-97ba-b9a2eecd2b4f}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Kind(self) -> win32more.Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_commethod(9)
    def get_IsRequired(self) -> Boolean: ...
    Description = property(get_Description, None)
    IsRequired = property(get_IsRequired, None)
    Kind = property(get_Kind, None)
    Name = property(get_Name, None)
class ILearningModelFeatureValue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelFeatureValue'
    _iid_ = Guid('{f51005db-4085-4dfe-9fed-95eb0c0cf75c}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    Kind = property(get_Kind, None)
class ILearningModelOperatorProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelOperatorProvider'
    _iid_ = Guid('{2a222e5d-afb1-47ed-bfad-b5b3a459ec04}')
class ILearningModelSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelSession'
    _iid_ = Guid('{8e58f8f6-b787-4c11-90f0-7129aeca74a9}')
    @winrt_commethod(6)
    def get_Model(self) -> win32more.Windows.AI.MachineLearning.LearningModel: ...
    @winrt_commethod(7)
    def get_Device(self) -> win32more.Windows.AI.MachineLearning.LearningModelDevice: ...
    @winrt_commethod(8)
    def get_EvaluationProperties(self) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_commethod(9)
    def EvaluateAsync(self, bindings: win32more.Windows.AI.MachineLearning.LearningModelBinding, correlationId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.AI.MachineLearning.LearningModelEvaluationResult]: ...
    @winrt_commethod(10)
    def EvaluateFeaturesAsync(self, features: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], correlationId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.AI.MachineLearning.LearningModelEvaluationResult]: ...
    @winrt_commethod(11)
    def Evaluate(self, bindings: win32more.Windows.AI.MachineLearning.LearningModelBinding, correlationId: WinRT_String) -> win32more.Windows.AI.MachineLearning.LearningModelEvaluationResult: ...
    @winrt_commethod(12)
    def EvaluateFeatures(self, features: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], correlationId: WinRT_String) -> win32more.Windows.AI.MachineLearning.LearningModelEvaluationResult: ...
    Device = property(get_Device, None)
    EvaluationProperties = property(get_EvaluationProperties, None)
    Model = property(get_Model, None)
class ILearningModelSessionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelSessionFactory'
    _iid_ = Guid('{0f6b881d-1c9b-47b6-bfe0-f1cf62a67579}')
    @winrt_commethod(6)
    def CreateFromModel(self, model: win32more.Windows.AI.MachineLearning.LearningModel) -> win32more.Windows.AI.MachineLearning.LearningModelSession: ...
    @winrt_commethod(7)
    def CreateFromModelOnDevice(self, model: win32more.Windows.AI.MachineLearning.LearningModel, deviceToRunOn: win32more.Windows.AI.MachineLearning.LearningModelDevice) -> win32more.Windows.AI.MachineLearning.LearningModelSession: ...
class ILearningModelSessionFactory2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelSessionFactory2'
    _iid_ = Guid('{4e5c88bf-0a1f-5fec-ade0-2fd91e4ef29b}')
    @winrt_commethod(6)
    def CreateFromModelOnDeviceWithSessionOptions(self, model: win32more.Windows.AI.MachineLearning.LearningModel, deviceToRunOn: win32more.Windows.AI.MachineLearning.LearningModelDevice, learningModelSessionOptions: win32more.Windows.AI.MachineLearning.LearningModelSessionOptions) -> win32more.Windows.AI.MachineLearning.LearningModelSession: ...
class ILearningModelSessionOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelSessionOptions'
    _iid_ = Guid('{b8f63fa1-134d-5133-8cff-3a5c3c263beb}')
    @winrt_commethod(6)
    def get_BatchSizeOverride(self) -> UInt32: ...
    @winrt_commethod(7)
    def put_BatchSizeOverride(self, value: UInt32) -> Void: ...
    BatchSizeOverride = property(get_BatchSizeOverride, put_BatchSizeOverride)
class ILearningModelSessionOptions2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelSessionOptions2'
    _iid_ = Guid('{6fcd1dc4-175f-5bd2-8de5-2f2006a25adf}')
    @winrt_commethod(6)
    def get_CloseModelOnSessionCreation(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_CloseModelOnSessionCreation(self, value: Boolean) -> Void: ...
    CloseModelOnSessionCreation = property(get_CloseModelOnSessionCreation, put_CloseModelOnSessionCreation)
class ILearningModelSessionOptions3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelSessionOptions3'
    _iid_ = Guid('{58e15cee-d8c2-56fc-92e8-76d751081086}')
    @winrt_commethod(6)
    def OverrideNamedDimension(self, name: WinRT_String, dimension: UInt32) -> Void: ...
class ILearningModelStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ILearningModelStatics'
    _iid_ = Guid('{e3b977e8-6952-4e47-8ef4-1f7f07897c6d}')
    @winrt_commethod(6)
    def LoadFromStorageFileAsync(self, modelFile: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.AI.MachineLearning.LearningModel]: ...
    @winrt_commethod(7)
    def LoadFromStreamAsync(self, modelStream: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.AI.MachineLearning.LearningModel]: ...
    @winrt_commethod(8)
    def LoadFromFilePath(self, filePath: WinRT_String) -> win32more.Windows.AI.MachineLearning.LearningModel: ...
    @winrt_commethod(9)
    def LoadFromStream(self, modelStream: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.AI.MachineLearning.LearningModel: ...
    @winrt_commethod(10)
    def LoadFromStorageFileWithOperatorProviderAsync(self, modelFile: win32more.Windows.Storage.IStorageFile, operatorProvider: win32more.Windows.AI.MachineLearning.ILearningModelOperatorProvider) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.AI.MachineLearning.LearningModel]: ...
    @winrt_commethod(11)
    def LoadFromStreamWithOperatorProviderAsync(self, modelStream: win32more.Windows.Storage.Streams.IRandomAccessStreamReference, operatorProvider: win32more.Windows.AI.MachineLearning.ILearningModelOperatorProvider) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.AI.MachineLearning.LearningModel]: ...
    @winrt_commethod(12)
    def LoadFromFilePathWithOperatorProvider(self, filePath: WinRT_String, operatorProvider: win32more.Windows.AI.MachineLearning.ILearningModelOperatorProvider) -> win32more.Windows.AI.MachineLearning.LearningModel: ...
    @winrt_commethod(13)
    def LoadFromStreamWithOperatorProvider(self, modelStream: win32more.Windows.Storage.Streams.IRandomAccessStreamReference, operatorProvider: win32more.Windows.AI.MachineLearning.ILearningModelOperatorProvider) -> win32more.Windows.AI.MachineLearning.LearningModel: ...
class IMapFeatureDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.IMapFeatureDescriptor'
    _iid_ = Guid('{530424bd-a257-436d-9e60-c2981f7cc5c4}')
    @winrt_commethod(6)
    def get_KeyKind(self) -> win32more.Windows.AI.MachineLearning.TensorKind: ...
    @winrt_commethod(7)
    def get_ValueDescriptor(self) -> win32more.Windows.AI.MachineLearning.ILearningModelFeatureDescriptor: ...
    KeyKind = property(get_KeyKind, None)
    ValueDescriptor = property(get_ValueDescriptor, None)
class ISequenceFeatureDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ISequenceFeatureDescriptor'
    _iid_ = Guid('{84f6945a-562b-4d62-a851-739aced96668}')
    @winrt_commethod(6)
    def get_ElementDescriptor(self) -> win32more.Windows.AI.MachineLearning.ILearningModelFeatureDescriptor: ...
    ElementDescriptor = property(get_ElementDescriptor, None)
class ITensor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensor'
    _iid_ = Guid('{05489593-a305-4a25-ad09-440119b4b7f6}')
    @winrt_commethod(6)
    def get_TensorKind(self) -> win32more.Windows.AI.MachineLearning.TensorKind: ...
    @winrt_commethod(7)
    def get_Shape(self) -> win32more.Windows.Foundation.Collections.IVectorView[Int64]: ...
    Shape = property(get_Shape, None)
    TensorKind = property(get_TensorKind, None)
class ITensorBoolean(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorBoolean'
    _iid_ = Guid('{50f311ed-29e9-4a5c-a44d-8fc512584eed}')
    @winrt_commethod(6)
    def GetAsVectorView(self) -> win32more.Windows.Foundation.Collections.IVectorView[Boolean]: ...
class ITensorBooleanStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorBooleanStatics'
    _iid_ = Guid('{2796862c-2357-49a7-b476-d0aa3dfe6866}')
    @winrt_commethod(6)
    def Create(self) -> win32more.Windows.AI.MachineLearning.TensorBoolean: ...
    @winrt_commethod(7)
    def Create2(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorBoolean: ...
    @winrt_commethod(8)
    def CreateFromArray(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: PassArray[Boolean]) -> win32more.Windows.AI.MachineLearning.TensorBoolean: ...
    @winrt_commethod(9)
    def CreateFromIterable(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: win32more.Windows.Foundation.Collections.IIterable[Boolean]) -> win32more.Windows.AI.MachineLearning.TensorBoolean: ...
class ITensorBooleanStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorBooleanStatics2'
    _iid_ = Guid('{a3a4a501-6a2d-52d7-b04b-c435baee0115}')
    @winrt_commethod(6)
    def CreateFromShapeArrayAndDataArray(self, shape: PassArray[Int64], data: PassArray[Boolean]) -> win32more.Windows.AI.MachineLearning.TensorBoolean: ...
    @winrt_commethod(7)
    def CreateFromBuffer(self, shape: PassArray[Int64], buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.AI.MachineLearning.TensorBoolean: ...
class ITensorDouble(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorDouble'
    _iid_ = Guid('{91e41252-7a8f-4f0e-a28f-9637ffc8a3d0}')
    @winrt_commethod(6)
    def GetAsVectorView(self) -> win32more.Windows.Foundation.Collections.IVectorView[Double]: ...
class ITensorDoubleStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorDoubleStatics'
    _iid_ = Guid('{a86693c5-9538-44e7-a3ca-5df374a5a70c}')
    @winrt_commethod(6)
    def Create(self) -> win32more.Windows.AI.MachineLearning.TensorDouble: ...
    @winrt_commethod(7)
    def Create2(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorDouble: ...
    @winrt_commethod(8)
    def CreateFromArray(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: PassArray[Double]) -> win32more.Windows.AI.MachineLearning.TensorDouble: ...
    @winrt_commethod(9)
    def CreateFromIterable(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: win32more.Windows.Foundation.Collections.IIterable[Double]) -> win32more.Windows.AI.MachineLearning.TensorDouble: ...
class ITensorDoubleStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorDoubleStatics2'
    _iid_ = Guid('{93a570de-5e9a-5094-85c8-592c655e68ac}')
    @winrt_commethod(6)
    def CreateFromShapeArrayAndDataArray(self, shape: PassArray[Int64], data: PassArray[Double]) -> win32more.Windows.AI.MachineLearning.TensorDouble: ...
    @winrt_commethod(7)
    def CreateFromBuffer(self, shape: PassArray[Int64], buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.AI.MachineLearning.TensorDouble: ...
class ITensorFeatureDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorFeatureDescriptor'
    _iid_ = Guid('{74455c80-946a-4310-a19c-ee0af028fce4}')
    @winrt_commethod(6)
    def get_TensorKind(self) -> win32more.Windows.AI.MachineLearning.TensorKind: ...
    @winrt_commethod(7)
    def get_Shape(self) -> win32more.Windows.Foundation.Collections.IVectorView[Int64]: ...
    Shape = property(get_Shape, None)
    TensorKind = property(get_TensorKind, None)
class ITensorFloat(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorFloat'
    _iid_ = Guid('{f2282d82-aa02-42c8-a0c8-df1efc9676e1}')
    @winrt_commethod(6)
    def GetAsVectorView(self) -> win32more.Windows.Foundation.Collections.IVectorView[Single]: ...
class ITensorFloat16Bit(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorFloat16Bit'
    _iid_ = Guid('{0ab994fc-5b89-4c3c-b5e4-5282a5316c0a}')
    @winrt_commethod(6)
    def GetAsVectorView(self) -> win32more.Windows.Foundation.Collections.IVectorView[Single]: ...
class ITensorFloat16BitStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorFloat16BitStatics'
    _iid_ = Guid('{a52db6f5-318a-44d4-820b-0cdc7054a84a}')
    @winrt_commethod(6)
    def Create(self) -> win32more.Windows.AI.MachineLearning.TensorFloat16Bit: ...
    @winrt_commethod(7)
    def Create2(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorFloat16Bit: ...
    @winrt_commethod(8)
    def CreateFromArray(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: PassArray[Single]) -> win32more.Windows.AI.MachineLearning.TensorFloat16Bit: ...
    @winrt_commethod(9)
    def CreateFromIterable(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: win32more.Windows.Foundation.Collections.IIterable[Single]) -> win32more.Windows.AI.MachineLearning.TensorFloat16Bit: ...
class ITensorFloat16BitStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorFloat16BitStatics2'
    _iid_ = Guid('{68545726-2dc7-51bf-b470-0b344cc2a1bc}')
    @winrt_commethod(6)
    def CreateFromShapeArrayAndDataArray(self, shape: PassArray[Int64], data: PassArray[Single]) -> win32more.Windows.AI.MachineLearning.TensorFloat16Bit: ...
    @winrt_commethod(7)
    def CreateFromBuffer(self, shape: PassArray[Int64], buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.AI.MachineLearning.TensorFloat16Bit: ...
class ITensorFloatStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorFloatStatics'
    _iid_ = Guid('{dbcd395b-3ba3-452f-b10d-3c135e573fa9}')
    @winrt_commethod(6)
    def Create(self) -> win32more.Windows.AI.MachineLearning.TensorFloat: ...
    @winrt_commethod(7)
    def Create2(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorFloat: ...
    @winrt_commethod(8)
    def CreateFromArray(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: PassArray[Single]) -> win32more.Windows.AI.MachineLearning.TensorFloat: ...
    @winrt_commethod(9)
    def CreateFromIterable(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: win32more.Windows.Foundation.Collections.IIterable[Single]) -> win32more.Windows.AI.MachineLearning.TensorFloat: ...
class ITensorFloatStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorFloatStatics2'
    _iid_ = Guid('{24610bc1-5e44-5713-b281-8f4ad4d555e8}')
    @winrt_commethod(6)
    def CreateFromShapeArrayAndDataArray(self, shape: PassArray[Int64], data: PassArray[Single]) -> win32more.Windows.AI.MachineLearning.TensorFloat: ...
    @winrt_commethod(7)
    def CreateFromBuffer(self, shape: PassArray[Int64], buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.AI.MachineLearning.TensorFloat: ...
class ITensorInt16Bit(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorInt16Bit'
    _iid_ = Guid('{98a32d39-e6d6-44af-8afa-baebc44dc020}')
    @winrt_commethod(6)
    def GetAsVectorView(self) -> win32more.Windows.Foundation.Collections.IVectorView[Int16]: ...
class ITensorInt16BitStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorInt16BitStatics'
    _iid_ = Guid('{98646293-266e-4b1a-821f-e60d70898b91}')
    @winrt_commethod(6)
    def Create(self) -> win32more.Windows.AI.MachineLearning.TensorInt16Bit: ...
    @winrt_commethod(7)
    def Create2(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorInt16Bit: ...
    @winrt_commethod(8)
    def CreateFromArray(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: PassArray[Int16]) -> win32more.Windows.AI.MachineLearning.TensorInt16Bit: ...
    @winrt_commethod(9)
    def CreateFromIterable(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: win32more.Windows.Foundation.Collections.IIterable[Int16]) -> win32more.Windows.AI.MachineLearning.TensorInt16Bit: ...
class ITensorInt16BitStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorInt16BitStatics2'
    _iid_ = Guid('{0cd70cf4-696c-5e5f-95d8-5ebf9670148b}')
    @winrt_commethod(6)
    def CreateFromShapeArrayAndDataArray(self, shape: PassArray[Int64], data: PassArray[Int16]) -> win32more.Windows.AI.MachineLearning.TensorInt16Bit: ...
    @winrt_commethod(7)
    def CreateFromBuffer(self, shape: PassArray[Int64], buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.AI.MachineLearning.TensorInt16Bit: ...
class ITensorInt32Bit(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorInt32Bit'
    _iid_ = Guid('{2c0c28d3-207c-4486-a7d2-884522c5e589}')
    @winrt_commethod(6)
    def GetAsVectorView(self) -> win32more.Windows.Foundation.Collections.IVectorView[Int32]: ...
class ITensorInt32BitStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorInt32BitStatics'
    _iid_ = Guid('{6539864b-52fa-4e35-907c-834cac417b50}')
    @winrt_commethod(6)
    def Create(self) -> win32more.Windows.AI.MachineLearning.TensorInt32Bit: ...
    @winrt_commethod(7)
    def Create2(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorInt32Bit: ...
    @winrt_commethod(8)
    def CreateFromArray(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: PassArray[Int32]) -> win32more.Windows.AI.MachineLearning.TensorInt32Bit: ...
    @winrt_commethod(9)
    def CreateFromIterable(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: win32more.Windows.Foundation.Collections.IIterable[Int32]) -> win32more.Windows.AI.MachineLearning.TensorInt32Bit: ...
class ITensorInt32BitStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorInt32BitStatics2'
    _iid_ = Guid('{7c4b079a-e956-5ce0-a3bd-157d9d79b5ec}')
    @winrt_commethod(6)
    def CreateFromShapeArrayAndDataArray(self, shape: PassArray[Int64], data: PassArray[Int32]) -> win32more.Windows.AI.MachineLearning.TensorInt32Bit: ...
    @winrt_commethod(7)
    def CreateFromBuffer(self, shape: PassArray[Int64], buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.AI.MachineLearning.TensorInt32Bit: ...
class ITensorInt64Bit(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorInt64Bit'
    _iid_ = Guid('{499665ba-1fa2-45ad-af25-a0bd9bda4c87}')
    @winrt_commethod(6)
    def GetAsVectorView(self) -> win32more.Windows.Foundation.Collections.IVectorView[Int64]: ...
class ITensorInt64BitStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorInt64BitStatics'
    _iid_ = Guid('{9648ad9d-1198-4d74-9517-783ab62b9cc2}')
    @winrt_commethod(6)
    def Create(self) -> win32more.Windows.AI.MachineLearning.TensorInt64Bit: ...
    @winrt_commethod(7)
    def Create2(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorInt64Bit: ...
    @winrt_commethod(8)
    def CreateFromArray(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: PassArray[Int64]) -> win32more.Windows.AI.MachineLearning.TensorInt64Bit: ...
    @winrt_commethod(9)
    def CreateFromIterable(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorInt64Bit: ...
class ITensorInt64BitStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorInt64BitStatics2'
    _iid_ = Guid('{6d3d9dcb-ff40-5ec2-89fe-084e2b6bc6db}')
    @winrt_commethod(6)
    def CreateFromShapeArrayAndDataArray(self, shape: PassArray[Int64], data: PassArray[Int64]) -> win32more.Windows.AI.MachineLearning.TensorInt64Bit: ...
    @winrt_commethod(7)
    def CreateFromBuffer(self, shape: PassArray[Int64], buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.AI.MachineLearning.TensorInt64Bit: ...
class ITensorInt8Bit(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorInt8Bit'
    _iid_ = Guid('{cddd97c5-ffd8-4fef-aefb-30e1a485b2ee}')
    @winrt_commethod(6)
    def GetAsVectorView(self) -> win32more.Windows.Foundation.Collections.IVectorView[Byte]: ...
class ITensorInt8BitStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorInt8BitStatics'
    _iid_ = Guid('{b1a12284-095c-4c76-a661-ac4cee1f3e8b}')
    @winrt_commethod(6)
    def Create(self) -> win32more.Windows.AI.MachineLearning.TensorInt8Bit: ...
    @winrt_commethod(7)
    def Create2(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorInt8Bit: ...
    @winrt_commethod(8)
    def CreateFromArray(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: PassArray[Byte]) -> win32more.Windows.AI.MachineLearning.TensorInt8Bit: ...
    @winrt_commethod(9)
    def CreateFromIterable(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: win32more.Windows.Foundation.Collections.IIterable[Byte]) -> win32more.Windows.AI.MachineLearning.TensorInt8Bit: ...
class ITensorInt8BitStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorInt8BitStatics2'
    _iid_ = Guid('{c0d59637-c468-56fb-9535-c052bdb93dc0}')
    @winrt_commethod(6)
    def CreateFromShapeArrayAndDataArray(self, shape: PassArray[Int64], data: PassArray[Byte]) -> win32more.Windows.AI.MachineLearning.TensorInt8Bit: ...
    @winrt_commethod(7)
    def CreateFromBuffer(self, shape: PassArray[Int64], buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.AI.MachineLearning.TensorInt8Bit: ...
class ITensorString(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorString'
    _iid_ = Guid('{582335c8-bdb1-4610-bc75-35e9cbf009b7}')
    @winrt_commethod(6)
    def GetAsVectorView(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
class ITensorStringStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorStringStatics'
    _iid_ = Guid('{83623324-cf26-4f17-a2d4-20ef8d097d53}')
    @winrt_commethod(6)
    def Create(self) -> win32more.Windows.AI.MachineLearning.TensorString: ...
    @winrt_commethod(7)
    def Create2(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorString: ...
    @winrt_commethod(8)
    def CreateFromArray(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: PassArray[WinRT_String]) -> win32more.Windows.AI.MachineLearning.TensorString: ...
    @winrt_commethod(9)
    def CreateFromIterable(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.AI.MachineLearning.TensorString: ...
class ITensorStringStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorStringStatics2'
    _iid_ = Guid('{9e355ed0-c8e2-5254-9137-0193a3668fd8}')
    @winrt_commethod(6)
    def CreateFromShapeArrayAndDataArray(self, shape: PassArray[Int64], data: PassArray[WinRT_String]) -> win32more.Windows.AI.MachineLearning.TensorString: ...
class ITensorUInt16Bit(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorUInt16Bit'
    _iid_ = Guid('{68140f4b-23c0-42f3-81f6-a891c011bc3f}')
    @winrt_commethod(6)
    def GetAsVectorView(self) -> win32more.Windows.Foundation.Collections.IVectorView[UInt16]: ...
class ITensorUInt16BitStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorUInt16BitStatics'
    _iid_ = Guid('{5df745dd-028a-481a-a27c-c7e6435e52dd}')
    @winrt_commethod(6)
    def Create(self) -> win32more.Windows.AI.MachineLearning.TensorUInt16Bit: ...
    @winrt_commethod(7)
    def Create2(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorUInt16Bit: ...
    @winrt_commethod(8)
    def CreateFromArray(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: PassArray[UInt16]) -> win32more.Windows.AI.MachineLearning.TensorUInt16Bit: ...
    @winrt_commethod(9)
    def CreateFromIterable(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: win32more.Windows.Foundation.Collections.IIterable[UInt16]) -> win32more.Windows.AI.MachineLearning.TensorUInt16Bit: ...
class ITensorUInt16BitStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorUInt16BitStatics2'
    _iid_ = Guid('{8af40c64-d69f-5315-9348-490877bbd642}')
    @winrt_commethod(6)
    def CreateFromShapeArrayAndDataArray(self, shape: PassArray[Int64], data: PassArray[UInt16]) -> win32more.Windows.AI.MachineLearning.TensorUInt16Bit: ...
    @winrt_commethod(7)
    def CreateFromBuffer(self, shape: PassArray[Int64], buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.AI.MachineLearning.TensorUInt16Bit: ...
class ITensorUInt32Bit(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorUInt32Bit'
    _iid_ = Guid('{d8c9c2ff-7511-45a3-bfac-c38f370d2237}')
    @winrt_commethod(6)
    def GetAsVectorView(self) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
class ITensorUInt32BitStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorUInt32BitStatics'
    _iid_ = Guid('{417c3837-e773-4378-8e7f-0cc33dbea697}')
    @winrt_commethod(6)
    def Create(self) -> win32more.Windows.AI.MachineLearning.TensorUInt32Bit: ...
    @winrt_commethod(7)
    def Create2(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorUInt32Bit: ...
    @winrt_commethod(8)
    def CreateFromArray(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: PassArray[UInt32]) -> win32more.Windows.AI.MachineLearning.TensorUInt32Bit: ...
    @winrt_commethod(9)
    def CreateFromIterable(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: win32more.Windows.Foundation.Collections.IIterable[UInt32]) -> win32more.Windows.AI.MachineLearning.TensorUInt32Bit: ...
class ITensorUInt32BitStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorUInt32BitStatics2'
    _iid_ = Guid('{ef1a1f1c-314e-569d-b496-5c8447d20cd2}')
    @winrt_commethod(6)
    def CreateFromShapeArrayAndDataArray(self, shape: PassArray[Int64], data: PassArray[UInt32]) -> win32more.Windows.AI.MachineLearning.TensorUInt32Bit: ...
    @winrt_commethod(7)
    def CreateFromBuffer(self, shape: PassArray[Int64], buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.AI.MachineLearning.TensorUInt32Bit: ...
class ITensorUInt64Bit(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorUInt64Bit'
    _iid_ = Guid('{2e70ffad-04bf-4825-839a-82baef8c7886}')
    @winrt_commethod(6)
    def GetAsVectorView(self) -> win32more.Windows.Foundation.Collections.IVectorView[UInt64]: ...
class ITensorUInt64BitStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorUInt64BitStatics'
    _iid_ = Guid('{7a7e20eb-242f-47cb-a9c6-f602ecfbfee4}')
    @winrt_commethod(6)
    def Create(self) -> win32more.Windows.AI.MachineLearning.TensorUInt64Bit: ...
    @winrt_commethod(7)
    def Create2(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorUInt64Bit: ...
    @winrt_commethod(8)
    def CreateFromArray(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: PassArray[UInt64]) -> win32more.Windows.AI.MachineLearning.TensorUInt64Bit: ...
    @winrt_commethod(9)
    def CreateFromIterable(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: win32more.Windows.Foundation.Collections.IIterable[UInt64]) -> win32more.Windows.AI.MachineLearning.TensorUInt64Bit: ...
class ITensorUInt64BitStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorUInt64BitStatics2'
    _iid_ = Guid('{085a687d-67e1-5b1e-b232-4fabe9ca20b3}')
    @winrt_commethod(6)
    def CreateFromShapeArrayAndDataArray(self, shape: PassArray[Int64], data: PassArray[UInt64]) -> win32more.Windows.AI.MachineLearning.TensorUInt64Bit: ...
    @winrt_commethod(7)
    def CreateFromBuffer(self, shape: PassArray[Int64], buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.AI.MachineLearning.TensorUInt64Bit: ...
class ITensorUInt8Bit(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorUInt8Bit'
    _iid_ = Guid('{58e1ae27-622b-48e3-be22-d867aed1daac}')
    @winrt_commethod(6)
    def GetAsVectorView(self) -> win32more.Windows.Foundation.Collections.IVectorView[Byte]: ...
class ITensorUInt8BitStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorUInt8BitStatics'
    _iid_ = Guid('{05f67583-bc24-4220-8a41-2dcd8c5ed33c}')
    @winrt_commethod(6)
    def Create(self) -> win32more.Windows.AI.MachineLearning.TensorUInt8Bit: ...
    @winrt_commethod(7)
    def Create2(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorUInt8Bit: ...
    @winrt_commethod(8)
    def CreateFromArray(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: PassArray[Byte]) -> win32more.Windows.AI.MachineLearning.TensorUInt8Bit: ...
    @winrt_commethod(9)
    def CreateFromIterable(self, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: win32more.Windows.Foundation.Collections.IIterable[Byte]) -> win32more.Windows.AI.MachineLearning.TensorUInt8Bit: ...
class ITensorUInt8BitStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.ITensorUInt8BitStatics2'
    _iid_ = Guid('{2ba042d6-373e-5a3a-a2fc-a6c41bd52789}')
    @winrt_commethod(6)
    def CreateFromShapeArrayAndDataArray(self, shape: PassArray[Int64], data: PassArray[Byte]) -> win32more.Windows.AI.MachineLearning.TensorUInt8Bit: ...
    @winrt_commethod(7)
    def CreateFromBuffer(self, shape: PassArray[Int64], buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.AI.MachineLearning.TensorUInt8Bit: ...
class ImageFeatureDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.AI.MachineLearning.IImageFeatureDescriptor
    _classid_ = 'Windows.AI.MachineLearning.ImageFeatureDescriptor'
    @winrt_mixinmethod
    def get_BitmapPixelFormat(self: win32more.Windows.AI.MachineLearning.IImageFeatureDescriptor) -> win32more.Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_mixinmethod
    def get_BitmapAlphaMode(self: win32more.Windows.AI.MachineLearning.IImageFeatureDescriptor) -> win32more.Windows.Graphics.Imaging.BitmapAlphaMode: ...
    @winrt_mixinmethod
    def get_Width(self: win32more.Windows.AI.MachineLearning.IImageFeatureDescriptor) -> UInt32: ...
    @winrt_mixinmethod
    def get_Height(self: win32more.Windows.AI.MachineLearning.IImageFeatureDescriptor) -> UInt32: ...
    @winrt_mixinmethod
    def get_PixelRange(self: win32more.Windows.AI.MachineLearning.IImageFeatureDescriptor2) -> win32more.Windows.AI.MachineLearning.LearningModelPixelRange: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> win32more.Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def get_IsRequired(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> Boolean: ...
    BitmapAlphaMode = property(get_BitmapAlphaMode, None)
    BitmapPixelFormat = property(get_BitmapPixelFormat, None)
    Description = property(get_Description, None)
    Height = property(get_Height, None)
    IsRequired = property(get_IsRequired, None)
    Kind = property(get_Kind, None)
    Name = property(get_Name, None)
    PixelRange = property(get_PixelRange, None)
    Width = property(get_Width, None)
class ImageFeatureValue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.AI.MachineLearning.IImageFeatureValue
    _classid_ = 'Windows.AI.MachineLearning.ImageFeatureValue'
    @winrt_mixinmethod
    def get_VideoFrame(self: win32more.Windows.AI.MachineLearning.IImageFeatureValue) -> win32more.Windows.Media.VideoFrame: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureValue) -> win32more.Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_classmethod
    def CreateFromVideoFrame(cls: win32more.Windows.AI.MachineLearning.IImageFeatureValueStatics, image: win32more.Windows.Media.VideoFrame) -> win32more.Windows.AI.MachineLearning.ImageFeatureValue: ...
    Kind = property(get_Kind, None)
    VideoFrame = property(get_VideoFrame, None)
class LearningModel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.MachineLearning.ILearningModel
    _classid_ = 'Windows.AI.MachineLearning.LearningModel'
    @winrt_mixinmethod
    def get_Author(self: win32more.Windows.AI.MachineLearning.ILearningModel) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.AI.MachineLearning.ILearningModel) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Domain(self: win32more.Windows.AI.MachineLearning.ILearningModel) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.AI.MachineLearning.ILearningModel) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Version(self: win32more.Windows.AI.MachineLearning.ILearningModel) -> Int64: ...
    @winrt_mixinmethod
    def get_Metadata(self: win32more.Windows.AI.MachineLearning.ILearningModel) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_InputFeatures(self: win32more.Windows.AI.MachineLearning.ILearningModel) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.AI.MachineLearning.ILearningModelFeatureDescriptor]: ...
    @winrt_mixinmethod
    def get_OutputFeatures(self: win32more.Windows.AI.MachineLearning.ILearningModel) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.AI.MachineLearning.ILearningModelFeatureDescriptor]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def LoadFromStorageFileAsync(cls: win32more.Windows.AI.MachineLearning.ILearningModelStatics, modelFile: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.AI.MachineLearning.LearningModel]: ...
    @winrt_classmethod
    def LoadFromStreamAsync(cls: win32more.Windows.AI.MachineLearning.ILearningModelStatics, modelStream: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.AI.MachineLearning.LearningModel]: ...
    @winrt_classmethod
    def LoadFromFilePath(cls: win32more.Windows.AI.MachineLearning.ILearningModelStatics, filePath: WinRT_String) -> win32more.Windows.AI.MachineLearning.LearningModel: ...
    @winrt_classmethod
    def LoadFromStream(cls: win32more.Windows.AI.MachineLearning.ILearningModelStatics, modelStream: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.AI.MachineLearning.LearningModel: ...
    @winrt_classmethod
    def LoadFromStorageFileWithOperatorProviderAsync(cls: win32more.Windows.AI.MachineLearning.ILearningModelStatics, modelFile: win32more.Windows.Storage.IStorageFile, operatorProvider: win32more.Windows.AI.MachineLearning.ILearningModelOperatorProvider) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.AI.MachineLearning.LearningModel]: ...
    @winrt_classmethod
    def LoadFromStreamWithOperatorProviderAsync(cls: win32more.Windows.AI.MachineLearning.ILearningModelStatics, modelStream: win32more.Windows.Storage.Streams.IRandomAccessStreamReference, operatorProvider: win32more.Windows.AI.MachineLearning.ILearningModelOperatorProvider) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.AI.MachineLearning.LearningModel]: ...
    @winrt_classmethod
    def LoadFromFilePathWithOperatorProvider(cls: win32more.Windows.AI.MachineLearning.ILearningModelStatics, filePath: WinRT_String, operatorProvider: win32more.Windows.AI.MachineLearning.ILearningModelOperatorProvider) -> win32more.Windows.AI.MachineLearning.LearningModel: ...
    @winrt_classmethod
    def LoadFromStreamWithOperatorProvider(cls: win32more.Windows.AI.MachineLearning.ILearningModelStatics, modelStream: win32more.Windows.Storage.Streams.IRandomAccessStreamReference, operatorProvider: win32more.Windows.AI.MachineLearning.ILearningModelOperatorProvider) -> win32more.Windows.AI.MachineLearning.LearningModel: ...
    Author = property(get_Author, None)
    Description = property(get_Description, None)
    Domain = property(get_Domain, None)
    InputFeatures = property(get_InputFeatures, None)
    Metadata = property(get_Metadata, None)
    Name = property(get_Name, None)
    OutputFeatures = property(get_OutputFeatures, None)
    Version = property(get_Version, None)
class LearningModelBinding(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[MappingProtocol[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]]
    default_interface: win32more.Windows.AI.MachineLearning.ILearningModelBinding
    _classid_ = 'Windows.AI.MachineLearning.LearningModelBinding'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.AI.MachineLearning.LearningModelBinding.CreateFromSession(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateFromSession(cls: win32more.Windows.AI.MachineLearning.ILearningModelBindingFactory, session: win32more.Windows.AI.MachineLearning.LearningModelSession) -> win32more.Windows.AI.MachineLearning.LearningModelBinding: ...
    @winrt_mixinmethod
    def Bind(self: win32more.Windows.AI.MachineLearning.ILearningModelBinding, name: WinRT_String, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def BindWithProperties(self: win32more.Windows.AI.MachineLearning.ILearningModelBinding, name: WinRT_String, value: win32more.Windows.Win32.System.WinRT.IInspectable, props: win32more.Windows.Foundation.Collections.IPropertySet) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.AI.MachineLearning.ILearningModelBinding) -> Void: ...
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
class LearningModelDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.AI.MachineLearning.ILearningModelDevice
    _classid_ = 'Windows.AI.MachineLearning.LearningModelDevice'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.AI.MachineLearning.LearningModelDevice.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.AI.MachineLearning.ILearningModelDeviceFactory, deviceKind: win32more.Windows.AI.MachineLearning.LearningModelDeviceKind) -> win32more.Windows.AI.MachineLearning.LearningModelDevice: ...
    @winrt_mixinmethod
    def get_AdapterId(self: win32more.Windows.AI.MachineLearning.ILearningModelDevice) -> win32more.Windows.Graphics.DisplayAdapterId: ...
    @winrt_mixinmethod
    def get_Direct3D11Device(self: win32more.Windows.AI.MachineLearning.ILearningModelDevice) -> win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice: ...
    @winrt_classmethod
    def CreateFromDirect3D11Device(cls: win32more.Windows.AI.MachineLearning.ILearningModelDeviceStatics, device: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice) -> win32more.Windows.AI.MachineLearning.LearningModelDevice: ...
    AdapterId = property(get_AdapterId, None)
    Direct3D11Device = property(get_Direct3D11Device, None)
class LearningModelDeviceKind(Enum, Int32):
    Default = 0
    Cpu = 1
    DirectX = 2
    DirectXHighPerformance = 3
    DirectXMinPower = 4
class LearningModelEvaluationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.AI.MachineLearning.ILearningModelEvaluationResult
    _classid_ = 'Windows.AI.MachineLearning.LearningModelEvaluationResult'
    @winrt_mixinmethod
    def get_CorrelationId(self: win32more.Windows.AI.MachineLearning.ILearningModelEvaluationResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ErrorStatus(self: win32more.Windows.AI.MachineLearning.ILearningModelEvaluationResult) -> Int32: ...
    @winrt_mixinmethod
    def get_Succeeded(self: win32more.Windows.AI.MachineLearning.ILearningModelEvaluationResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_Outputs(self: win32more.Windows.AI.MachineLearning.ILearningModelEvaluationResult) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    CorrelationId = property(get_CorrelationId, None)
    ErrorStatus = property(get_ErrorStatus, None)
    Outputs = property(get_Outputs, None)
    Succeeded = property(get_Succeeded, None)
class LearningModelFeatureKind(Enum, Int32):
    Tensor = 0
    Sequence = 1
    Map = 2
    Image = 3
class LearningModelPixelRange(Enum, Int32):
    ZeroTo255 = 0
    ZeroToOne = 1
    MinusOneToOne = 2
class LearningModelSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.MachineLearning.ILearningModelSession
    _classid_ = 'Windows.AI.MachineLearning.LearningModelSession'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.AI.MachineLearning.LearningModelSession.CreateFromModel(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.AI.MachineLearning.LearningModelSession.CreateFromModelOnDevice(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.AI.MachineLearning.LearningModelSession.CreateFromModelOnDeviceWithSessionOptions(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateFromModel(cls: win32more.Windows.AI.MachineLearning.ILearningModelSessionFactory, model: win32more.Windows.AI.MachineLearning.LearningModel) -> win32more.Windows.AI.MachineLearning.LearningModelSession: ...
    @winrt_factorymethod
    def CreateFromModelOnDevice(cls: win32more.Windows.AI.MachineLearning.ILearningModelSessionFactory, model: win32more.Windows.AI.MachineLearning.LearningModel, deviceToRunOn: win32more.Windows.AI.MachineLearning.LearningModelDevice) -> win32more.Windows.AI.MachineLearning.LearningModelSession: ...
    @winrt_factorymethod
    def CreateFromModelOnDeviceWithSessionOptions(cls: win32more.Windows.AI.MachineLearning.ILearningModelSessionFactory2, model: win32more.Windows.AI.MachineLearning.LearningModel, deviceToRunOn: win32more.Windows.AI.MachineLearning.LearningModelDevice, learningModelSessionOptions: win32more.Windows.AI.MachineLearning.LearningModelSessionOptions) -> win32more.Windows.AI.MachineLearning.LearningModelSession: ...
    @winrt_mixinmethod
    def get_Model(self: win32more.Windows.AI.MachineLearning.ILearningModelSession) -> win32more.Windows.AI.MachineLearning.LearningModel: ...
    @winrt_mixinmethod
    def get_Device(self: win32more.Windows.AI.MachineLearning.ILearningModelSession) -> win32more.Windows.AI.MachineLearning.LearningModelDevice: ...
    @winrt_mixinmethod
    def get_EvaluationProperties(self: win32more.Windows.AI.MachineLearning.ILearningModelSession) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_mixinmethod
    def EvaluateAsync(self: win32more.Windows.AI.MachineLearning.ILearningModelSession, bindings: win32more.Windows.AI.MachineLearning.LearningModelBinding, correlationId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.AI.MachineLearning.LearningModelEvaluationResult]: ...
    @winrt_mixinmethod
    def EvaluateFeaturesAsync(self: win32more.Windows.AI.MachineLearning.ILearningModelSession, features: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], correlationId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.AI.MachineLearning.LearningModelEvaluationResult]: ...
    @winrt_mixinmethod
    def Evaluate(self: win32more.Windows.AI.MachineLearning.ILearningModelSession, bindings: win32more.Windows.AI.MachineLearning.LearningModelBinding, correlationId: WinRT_String) -> win32more.Windows.AI.MachineLearning.LearningModelEvaluationResult: ...
    @winrt_mixinmethod
    def EvaluateFeatures(self: win32more.Windows.AI.MachineLearning.ILearningModelSession, features: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], correlationId: WinRT_String) -> win32more.Windows.AI.MachineLearning.LearningModelEvaluationResult: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Device = property(get_Device, None)
    EvaluationProperties = property(get_EvaluationProperties, None)
    Model = property(get_Model, None)
class LearningModelSessionOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.AI.MachineLearning.ILearningModelSessionOptions
    _classid_ = 'Windows.AI.MachineLearning.LearningModelSessionOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.AI.MachineLearning.LearningModelSessionOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.AI.MachineLearning.LearningModelSessionOptions: ...
    @winrt_mixinmethod
    def get_BatchSizeOverride(self: win32more.Windows.AI.MachineLearning.ILearningModelSessionOptions) -> UInt32: ...
    @winrt_mixinmethod
    def put_BatchSizeOverride(self: win32more.Windows.AI.MachineLearning.ILearningModelSessionOptions, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_CloseModelOnSessionCreation(self: win32more.Windows.AI.MachineLearning.ILearningModelSessionOptions2) -> Boolean: ...
    @winrt_mixinmethod
    def put_CloseModelOnSessionCreation(self: win32more.Windows.AI.MachineLearning.ILearningModelSessionOptions2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def OverrideNamedDimension(self: win32more.Windows.AI.MachineLearning.ILearningModelSessionOptions3, name: WinRT_String, dimension: UInt32) -> Void: ...
    BatchSizeOverride = property(get_BatchSizeOverride, put_BatchSizeOverride)
    CloseModelOnSessionCreation = property(get_CloseModelOnSessionCreation, put_CloseModelOnSessionCreation)
MachineLearningContract: UInt32 = 327680
class MapFeatureDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.AI.MachineLearning.IMapFeatureDescriptor
    _classid_ = 'Windows.AI.MachineLearning.MapFeatureDescriptor'
    @winrt_mixinmethod
    def get_KeyKind(self: win32more.Windows.AI.MachineLearning.IMapFeatureDescriptor) -> win32more.Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_ValueDescriptor(self: win32more.Windows.AI.MachineLearning.IMapFeatureDescriptor) -> win32more.Windows.AI.MachineLearning.ILearningModelFeatureDescriptor: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> win32more.Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def get_IsRequired(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> Boolean: ...
    Description = property(get_Description, None)
    IsRequired = property(get_IsRequired, None)
    KeyKind = property(get_KeyKind, None)
    Kind = property(get_Kind, None)
    Name = property(get_Name, None)
    ValueDescriptor = property(get_ValueDescriptor, None)
class SequenceFeatureDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.AI.MachineLearning.ISequenceFeatureDescriptor
    _classid_ = 'Windows.AI.MachineLearning.SequenceFeatureDescriptor'
    @winrt_mixinmethod
    def get_ElementDescriptor(self: win32more.Windows.AI.MachineLearning.ISequenceFeatureDescriptor) -> win32more.Windows.AI.MachineLearning.ILearningModelFeatureDescriptor: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> win32more.Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def get_IsRequired(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> Boolean: ...
    Description = property(get_Description, None)
    ElementDescriptor = property(get_ElementDescriptor, None)
    IsRequired = property(get_IsRequired, None)
    Kind = property(get_Kind, None)
    Name = property(get_Name, None)
class TensorBoolean(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.MachineLearning.ITensorBoolean
    _classid_ = 'Windows.AI.MachineLearning.TensorBoolean'
    @winrt_mixinmethod
    def GetAsVectorView(self: win32more.Windows.AI.MachineLearning.ITensorBoolean) -> win32more.Windows.Foundation.Collections.IVectorView[Boolean]: ...
    @winrt_mixinmethod
    def get_TensorKind(self: win32more.Windows.AI.MachineLearning.ITensor) -> win32more.Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: win32more.Windows.AI.MachineLearning.ITensor) -> win32more.Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureValue) -> win32more.Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def CreateReference(self: win32more.Windows.Foundation.IMemoryBuffer) -> win32more.Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFromShapeArrayAndDataArray(cls: win32more.Windows.AI.MachineLearning.ITensorBooleanStatics2, shape: PassArray[Int64], data: PassArray[Boolean]) -> win32more.Windows.AI.MachineLearning.TensorBoolean: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: win32more.Windows.AI.MachineLearning.ITensorBooleanStatics2, shape: PassArray[Int64], buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.AI.MachineLearning.TensorBoolean: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.AI.MachineLearning.ITensorBooleanStatics) -> win32more.Windows.AI.MachineLearning.TensorBoolean: ...
    @winrt_classmethod
    def Create2(cls: win32more.Windows.AI.MachineLearning.ITensorBooleanStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorBoolean: ...
    @winrt_classmethod
    def CreateFromArray(cls: win32more.Windows.AI.MachineLearning.ITensorBooleanStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: PassArray[Boolean]) -> win32more.Windows.AI.MachineLearning.TensorBoolean: ...
    @winrt_classmethod
    def CreateFromIterable(cls: win32more.Windows.AI.MachineLearning.ITensorBooleanStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: win32more.Windows.Foundation.Collections.IIterable[Boolean]) -> win32more.Windows.AI.MachineLearning.TensorBoolean: ...
    Kind = property(get_Kind, None)
    Shape = property(get_Shape, None)
    TensorKind = property(get_TensorKind, None)
class TensorDouble(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.MachineLearning.ITensorDouble
    _classid_ = 'Windows.AI.MachineLearning.TensorDouble'
    @winrt_mixinmethod
    def GetAsVectorView(self: win32more.Windows.AI.MachineLearning.ITensorDouble) -> win32more.Windows.Foundation.Collections.IVectorView[Double]: ...
    @winrt_mixinmethod
    def get_TensorKind(self: win32more.Windows.AI.MachineLearning.ITensor) -> win32more.Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: win32more.Windows.AI.MachineLearning.ITensor) -> win32more.Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureValue) -> win32more.Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def CreateReference(self: win32more.Windows.Foundation.IMemoryBuffer) -> win32more.Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFromShapeArrayAndDataArray(cls: win32more.Windows.AI.MachineLearning.ITensorDoubleStatics2, shape: PassArray[Int64], data: PassArray[Double]) -> win32more.Windows.AI.MachineLearning.TensorDouble: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: win32more.Windows.AI.MachineLearning.ITensorDoubleStatics2, shape: PassArray[Int64], buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.AI.MachineLearning.TensorDouble: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.AI.MachineLearning.ITensorDoubleStatics) -> win32more.Windows.AI.MachineLearning.TensorDouble: ...
    @winrt_classmethod
    def Create2(cls: win32more.Windows.AI.MachineLearning.ITensorDoubleStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorDouble: ...
    @winrt_classmethod
    def CreateFromArray(cls: win32more.Windows.AI.MachineLearning.ITensorDoubleStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: PassArray[Double]) -> win32more.Windows.AI.MachineLearning.TensorDouble: ...
    @winrt_classmethod
    def CreateFromIterable(cls: win32more.Windows.AI.MachineLearning.ITensorDoubleStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: win32more.Windows.Foundation.Collections.IIterable[Double]) -> win32more.Windows.AI.MachineLearning.TensorDouble: ...
    Kind = property(get_Kind, None)
    Shape = property(get_Shape, None)
    TensorKind = property(get_TensorKind, None)
class TensorFeatureDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.AI.MachineLearning.ITensorFeatureDescriptor
    _classid_ = 'Windows.AI.MachineLearning.TensorFeatureDescriptor'
    @winrt_mixinmethod
    def get_TensorKind(self: win32more.Windows.AI.MachineLearning.ITensorFeatureDescriptor) -> win32more.Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: win32more.Windows.AI.MachineLearning.ITensorFeatureDescriptor) -> win32more.Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> win32more.Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def get_IsRequired(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureDescriptor) -> Boolean: ...
    Description = property(get_Description, None)
    IsRequired = property(get_IsRequired, None)
    Kind = property(get_Kind, None)
    Name = property(get_Name, None)
    Shape = property(get_Shape, None)
    TensorKind = property(get_TensorKind, None)
class TensorFloat(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.MachineLearning.ITensorFloat
    _classid_ = 'Windows.AI.MachineLearning.TensorFloat'
    @winrt_mixinmethod
    def GetAsVectorView(self: win32more.Windows.AI.MachineLearning.ITensorFloat) -> win32more.Windows.Foundation.Collections.IVectorView[Single]: ...
    @winrt_mixinmethod
    def get_TensorKind(self: win32more.Windows.AI.MachineLearning.ITensor) -> win32more.Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: win32more.Windows.AI.MachineLearning.ITensor) -> win32more.Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureValue) -> win32more.Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def CreateReference(self: win32more.Windows.Foundation.IMemoryBuffer) -> win32more.Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFromShapeArrayAndDataArray(cls: win32more.Windows.AI.MachineLearning.ITensorFloatStatics2, shape: PassArray[Int64], data: PassArray[Single]) -> win32more.Windows.AI.MachineLearning.TensorFloat: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: win32more.Windows.AI.MachineLearning.ITensorFloatStatics2, shape: PassArray[Int64], buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.AI.MachineLearning.TensorFloat: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.AI.MachineLearning.ITensorFloatStatics) -> win32more.Windows.AI.MachineLearning.TensorFloat: ...
    @winrt_classmethod
    def Create2(cls: win32more.Windows.AI.MachineLearning.ITensorFloatStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorFloat: ...
    @winrt_classmethod
    def CreateFromArray(cls: win32more.Windows.AI.MachineLearning.ITensorFloatStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: PassArray[Single]) -> win32more.Windows.AI.MachineLearning.TensorFloat: ...
    @winrt_classmethod
    def CreateFromIterable(cls: win32more.Windows.AI.MachineLearning.ITensorFloatStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: win32more.Windows.Foundation.Collections.IIterable[Single]) -> win32more.Windows.AI.MachineLearning.TensorFloat: ...
    Kind = property(get_Kind, None)
    Shape = property(get_Shape, None)
    TensorKind = property(get_TensorKind, None)
class TensorFloat16Bit(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.MachineLearning.ITensorFloat16Bit
    _classid_ = 'Windows.AI.MachineLearning.TensorFloat16Bit'
    @winrt_mixinmethod
    def GetAsVectorView(self: win32more.Windows.AI.MachineLearning.ITensorFloat16Bit) -> win32more.Windows.Foundation.Collections.IVectorView[Single]: ...
    @winrt_mixinmethod
    def get_TensorKind(self: win32more.Windows.AI.MachineLearning.ITensor) -> win32more.Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: win32more.Windows.AI.MachineLearning.ITensor) -> win32more.Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureValue) -> win32more.Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def CreateReference(self: win32more.Windows.Foundation.IMemoryBuffer) -> win32more.Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFromShapeArrayAndDataArray(cls: win32more.Windows.AI.MachineLearning.ITensorFloat16BitStatics2, shape: PassArray[Int64], data: PassArray[Single]) -> win32more.Windows.AI.MachineLearning.TensorFloat16Bit: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: win32more.Windows.AI.MachineLearning.ITensorFloat16BitStatics2, shape: PassArray[Int64], buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.AI.MachineLearning.TensorFloat16Bit: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.AI.MachineLearning.ITensorFloat16BitStatics) -> win32more.Windows.AI.MachineLearning.TensorFloat16Bit: ...
    @winrt_classmethod
    def Create2(cls: win32more.Windows.AI.MachineLearning.ITensorFloat16BitStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorFloat16Bit: ...
    @winrt_classmethod
    def CreateFromArray(cls: win32more.Windows.AI.MachineLearning.ITensorFloat16BitStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: PassArray[Single]) -> win32more.Windows.AI.MachineLearning.TensorFloat16Bit: ...
    @winrt_classmethod
    def CreateFromIterable(cls: win32more.Windows.AI.MachineLearning.ITensorFloat16BitStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: win32more.Windows.Foundation.Collections.IIterable[Single]) -> win32more.Windows.AI.MachineLearning.TensorFloat16Bit: ...
    Kind = property(get_Kind, None)
    Shape = property(get_Shape, None)
    TensorKind = property(get_TensorKind, None)
class TensorInt16Bit(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.MachineLearning.ITensorInt16Bit
    _classid_ = 'Windows.AI.MachineLearning.TensorInt16Bit'
    @winrt_mixinmethod
    def GetAsVectorView(self: win32more.Windows.AI.MachineLearning.ITensorInt16Bit) -> win32more.Windows.Foundation.Collections.IVectorView[Int16]: ...
    @winrt_mixinmethod
    def get_TensorKind(self: win32more.Windows.AI.MachineLearning.ITensor) -> win32more.Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: win32more.Windows.AI.MachineLearning.ITensor) -> win32more.Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureValue) -> win32more.Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def CreateReference(self: win32more.Windows.Foundation.IMemoryBuffer) -> win32more.Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFromShapeArrayAndDataArray(cls: win32more.Windows.AI.MachineLearning.ITensorInt16BitStatics2, shape: PassArray[Int64], data: PassArray[Int16]) -> win32more.Windows.AI.MachineLearning.TensorInt16Bit: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: win32more.Windows.AI.MachineLearning.ITensorInt16BitStatics2, shape: PassArray[Int64], buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.AI.MachineLearning.TensorInt16Bit: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.AI.MachineLearning.ITensorInt16BitStatics) -> win32more.Windows.AI.MachineLearning.TensorInt16Bit: ...
    @winrt_classmethod
    def Create2(cls: win32more.Windows.AI.MachineLearning.ITensorInt16BitStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorInt16Bit: ...
    @winrt_classmethod
    def CreateFromArray(cls: win32more.Windows.AI.MachineLearning.ITensorInt16BitStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: PassArray[Int16]) -> win32more.Windows.AI.MachineLearning.TensorInt16Bit: ...
    @winrt_classmethod
    def CreateFromIterable(cls: win32more.Windows.AI.MachineLearning.ITensorInt16BitStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: win32more.Windows.Foundation.Collections.IIterable[Int16]) -> win32more.Windows.AI.MachineLearning.TensorInt16Bit: ...
    Kind = property(get_Kind, None)
    Shape = property(get_Shape, None)
    TensorKind = property(get_TensorKind, None)
class TensorInt32Bit(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.MachineLearning.ITensorInt32Bit
    _classid_ = 'Windows.AI.MachineLearning.TensorInt32Bit'
    @winrt_mixinmethod
    def GetAsVectorView(self: win32more.Windows.AI.MachineLearning.ITensorInt32Bit) -> win32more.Windows.Foundation.Collections.IVectorView[Int32]: ...
    @winrt_mixinmethod
    def get_TensorKind(self: win32more.Windows.AI.MachineLearning.ITensor) -> win32more.Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: win32more.Windows.AI.MachineLearning.ITensor) -> win32more.Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureValue) -> win32more.Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def CreateReference(self: win32more.Windows.Foundation.IMemoryBuffer) -> win32more.Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFromShapeArrayAndDataArray(cls: win32more.Windows.AI.MachineLearning.ITensorInt32BitStatics2, shape: PassArray[Int64], data: PassArray[Int32]) -> win32more.Windows.AI.MachineLearning.TensorInt32Bit: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: win32more.Windows.AI.MachineLearning.ITensorInt32BitStatics2, shape: PassArray[Int64], buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.AI.MachineLearning.TensorInt32Bit: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.AI.MachineLearning.ITensorInt32BitStatics) -> win32more.Windows.AI.MachineLearning.TensorInt32Bit: ...
    @winrt_classmethod
    def Create2(cls: win32more.Windows.AI.MachineLearning.ITensorInt32BitStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorInt32Bit: ...
    @winrt_classmethod
    def CreateFromArray(cls: win32more.Windows.AI.MachineLearning.ITensorInt32BitStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: PassArray[Int32]) -> win32more.Windows.AI.MachineLearning.TensorInt32Bit: ...
    @winrt_classmethod
    def CreateFromIterable(cls: win32more.Windows.AI.MachineLearning.ITensorInt32BitStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: win32more.Windows.Foundation.Collections.IIterable[Int32]) -> win32more.Windows.AI.MachineLearning.TensorInt32Bit: ...
    Kind = property(get_Kind, None)
    Shape = property(get_Shape, None)
    TensorKind = property(get_TensorKind, None)
class TensorInt64Bit(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.MachineLearning.ITensorInt64Bit
    _classid_ = 'Windows.AI.MachineLearning.TensorInt64Bit'
    @winrt_mixinmethod
    def GetAsVectorView(self: win32more.Windows.AI.MachineLearning.ITensorInt64Bit) -> win32more.Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_TensorKind(self: win32more.Windows.AI.MachineLearning.ITensor) -> win32more.Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: win32more.Windows.AI.MachineLearning.ITensor) -> win32more.Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureValue) -> win32more.Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def CreateReference(self: win32more.Windows.Foundation.IMemoryBuffer) -> win32more.Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFromShapeArrayAndDataArray(cls: win32more.Windows.AI.MachineLearning.ITensorInt64BitStatics2, shape: PassArray[Int64], data: PassArray[Int64]) -> win32more.Windows.AI.MachineLearning.TensorInt64Bit: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: win32more.Windows.AI.MachineLearning.ITensorInt64BitStatics2, shape: PassArray[Int64], buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.AI.MachineLearning.TensorInt64Bit: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.AI.MachineLearning.ITensorInt64BitStatics) -> win32more.Windows.AI.MachineLearning.TensorInt64Bit: ...
    @winrt_classmethod
    def Create2(cls: win32more.Windows.AI.MachineLearning.ITensorInt64BitStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorInt64Bit: ...
    @winrt_classmethod
    def CreateFromArray(cls: win32more.Windows.AI.MachineLearning.ITensorInt64BitStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: PassArray[Int64]) -> win32more.Windows.AI.MachineLearning.TensorInt64Bit: ...
    @winrt_classmethod
    def CreateFromIterable(cls: win32more.Windows.AI.MachineLearning.ITensorInt64BitStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorInt64Bit: ...
    Kind = property(get_Kind, None)
    Shape = property(get_Shape, None)
    TensorKind = property(get_TensorKind, None)
class TensorInt8Bit(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.MachineLearning.ITensorInt8Bit
    _classid_ = 'Windows.AI.MachineLearning.TensorInt8Bit'
    @winrt_mixinmethod
    def GetAsVectorView(self: win32more.Windows.AI.MachineLearning.ITensorInt8Bit) -> win32more.Windows.Foundation.Collections.IVectorView[Byte]: ...
    @winrt_mixinmethod
    def get_TensorKind(self: win32more.Windows.AI.MachineLearning.ITensor) -> win32more.Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: win32more.Windows.AI.MachineLearning.ITensor) -> win32more.Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureValue) -> win32more.Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def CreateReference(self: win32more.Windows.Foundation.IMemoryBuffer) -> win32more.Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFromShapeArrayAndDataArray(cls: win32more.Windows.AI.MachineLearning.ITensorInt8BitStatics2, shape: PassArray[Int64], data: PassArray[Byte]) -> win32more.Windows.AI.MachineLearning.TensorInt8Bit: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: win32more.Windows.AI.MachineLearning.ITensorInt8BitStatics2, shape: PassArray[Int64], buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.AI.MachineLearning.TensorInt8Bit: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.AI.MachineLearning.ITensorInt8BitStatics) -> win32more.Windows.AI.MachineLearning.TensorInt8Bit: ...
    @winrt_classmethod
    def Create2(cls: win32more.Windows.AI.MachineLearning.ITensorInt8BitStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorInt8Bit: ...
    @winrt_classmethod
    def CreateFromArray(cls: win32more.Windows.AI.MachineLearning.ITensorInt8BitStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: PassArray[Byte]) -> win32more.Windows.AI.MachineLearning.TensorInt8Bit: ...
    @winrt_classmethod
    def CreateFromIterable(cls: win32more.Windows.AI.MachineLearning.ITensorInt8BitStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: win32more.Windows.Foundation.Collections.IIterable[Byte]) -> win32more.Windows.AI.MachineLearning.TensorInt8Bit: ...
    Kind = property(get_Kind, None)
    Shape = property(get_Shape, None)
    TensorKind = property(get_TensorKind, None)
class TensorKind(Enum, Int32):
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
class TensorString(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.MachineLearning.ITensorString
    _classid_ = 'Windows.AI.MachineLearning.TensorString'
    @winrt_mixinmethod
    def GetAsVectorView(self: win32more.Windows.AI.MachineLearning.ITensorString) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_TensorKind(self: win32more.Windows.AI.MachineLearning.ITensor) -> win32more.Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: win32more.Windows.AI.MachineLearning.ITensor) -> win32more.Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureValue) -> win32more.Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def CreateReference(self: win32more.Windows.Foundation.IMemoryBuffer) -> win32more.Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFromShapeArrayAndDataArray(cls: win32more.Windows.AI.MachineLearning.ITensorStringStatics2, shape: PassArray[Int64], data: PassArray[WinRT_String]) -> win32more.Windows.AI.MachineLearning.TensorString: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.AI.MachineLearning.ITensorStringStatics) -> win32more.Windows.AI.MachineLearning.TensorString: ...
    @winrt_classmethod
    def Create2(cls: win32more.Windows.AI.MachineLearning.ITensorStringStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorString: ...
    @winrt_classmethod
    def CreateFromArray(cls: win32more.Windows.AI.MachineLearning.ITensorStringStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: PassArray[WinRT_String]) -> win32more.Windows.AI.MachineLearning.TensorString: ...
    @winrt_classmethod
    def CreateFromIterable(cls: win32more.Windows.AI.MachineLearning.ITensorStringStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.AI.MachineLearning.TensorString: ...
    Kind = property(get_Kind, None)
    Shape = property(get_Shape, None)
    TensorKind = property(get_TensorKind, None)
class TensorUInt16Bit(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.MachineLearning.ITensorUInt16Bit
    _classid_ = 'Windows.AI.MachineLearning.TensorUInt16Bit'
    @winrt_mixinmethod
    def GetAsVectorView(self: win32more.Windows.AI.MachineLearning.ITensorUInt16Bit) -> win32more.Windows.Foundation.Collections.IVectorView[UInt16]: ...
    @winrt_mixinmethod
    def get_TensorKind(self: win32more.Windows.AI.MachineLearning.ITensor) -> win32more.Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: win32more.Windows.AI.MachineLearning.ITensor) -> win32more.Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureValue) -> win32more.Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def CreateReference(self: win32more.Windows.Foundation.IMemoryBuffer) -> win32more.Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFromShapeArrayAndDataArray(cls: win32more.Windows.AI.MachineLearning.ITensorUInt16BitStatics2, shape: PassArray[Int64], data: PassArray[UInt16]) -> win32more.Windows.AI.MachineLearning.TensorUInt16Bit: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: win32more.Windows.AI.MachineLearning.ITensorUInt16BitStatics2, shape: PassArray[Int64], buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.AI.MachineLearning.TensorUInt16Bit: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.AI.MachineLearning.ITensorUInt16BitStatics) -> win32more.Windows.AI.MachineLearning.TensorUInt16Bit: ...
    @winrt_classmethod
    def Create2(cls: win32more.Windows.AI.MachineLearning.ITensorUInt16BitStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorUInt16Bit: ...
    @winrt_classmethod
    def CreateFromArray(cls: win32more.Windows.AI.MachineLearning.ITensorUInt16BitStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: PassArray[UInt16]) -> win32more.Windows.AI.MachineLearning.TensorUInt16Bit: ...
    @winrt_classmethod
    def CreateFromIterable(cls: win32more.Windows.AI.MachineLearning.ITensorUInt16BitStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: win32more.Windows.Foundation.Collections.IIterable[UInt16]) -> win32more.Windows.AI.MachineLearning.TensorUInt16Bit: ...
    Kind = property(get_Kind, None)
    Shape = property(get_Shape, None)
    TensorKind = property(get_TensorKind, None)
class TensorUInt32Bit(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.MachineLearning.ITensorUInt32Bit
    _classid_ = 'Windows.AI.MachineLearning.TensorUInt32Bit'
    @winrt_mixinmethod
    def GetAsVectorView(self: win32more.Windows.AI.MachineLearning.ITensorUInt32Bit) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_mixinmethod
    def get_TensorKind(self: win32more.Windows.AI.MachineLearning.ITensor) -> win32more.Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: win32more.Windows.AI.MachineLearning.ITensor) -> win32more.Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureValue) -> win32more.Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def CreateReference(self: win32more.Windows.Foundation.IMemoryBuffer) -> win32more.Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFromShapeArrayAndDataArray(cls: win32more.Windows.AI.MachineLearning.ITensorUInt32BitStatics2, shape: PassArray[Int64], data: PassArray[UInt32]) -> win32more.Windows.AI.MachineLearning.TensorUInt32Bit: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: win32more.Windows.AI.MachineLearning.ITensorUInt32BitStatics2, shape: PassArray[Int64], buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.AI.MachineLearning.TensorUInt32Bit: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.AI.MachineLearning.ITensorUInt32BitStatics) -> win32more.Windows.AI.MachineLearning.TensorUInt32Bit: ...
    @winrt_classmethod
    def Create2(cls: win32more.Windows.AI.MachineLearning.ITensorUInt32BitStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorUInt32Bit: ...
    @winrt_classmethod
    def CreateFromArray(cls: win32more.Windows.AI.MachineLearning.ITensorUInt32BitStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: PassArray[UInt32]) -> win32more.Windows.AI.MachineLearning.TensorUInt32Bit: ...
    @winrt_classmethod
    def CreateFromIterable(cls: win32more.Windows.AI.MachineLearning.ITensorUInt32BitStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: win32more.Windows.Foundation.Collections.IIterable[UInt32]) -> win32more.Windows.AI.MachineLearning.TensorUInt32Bit: ...
    Kind = property(get_Kind, None)
    Shape = property(get_Shape, None)
    TensorKind = property(get_TensorKind, None)
class TensorUInt64Bit(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.MachineLearning.ITensorUInt64Bit
    _classid_ = 'Windows.AI.MachineLearning.TensorUInt64Bit'
    @winrt_mixinmethod
    def GetAsVectorView(self: win32more.Windows.AI.MachineLearning.ITensorUInt64Bit) -> win32more.Windows.Foundation.Collections.IVectorView[UInt64]: ...
    @winrt_mixinmethod
    def get_TensorKind(self: win32more.Windows.AI.MachineLearning.ITensor) -> win32more.Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: win32more.Windows.AI.MachineLearning.ITensor) -> win32more.Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureValue) -> win32more.Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def CreateReference(self: win32more.Windows.Foundation.IMemoryBuffer) -> win32more.Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFromShapeArrayAndDataArray(cls: win32more.Windows.AI.MachineLearning.ITensorUInt64BitStatics2, shape: PassArray[Int64], data: PassArray[UInt64]) -> win32more.Windows.AI.MachineLearning.TensorUInt64Bit: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: win32more.Windows.AI.MachineLearning.ITensorUInt64BitStatics2, shape: PassArray[Int64], buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.AI.MachineLearning.TensorUInt64Bit: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.AI.MachineLearning.ITensorUInt64BitStatics) -> win32more.Windows.AI.MachineLearning.TensorUInt64Bit: ...
    @winrt_classmethod
    def Create2(cls: win32more.Windows.AI.MachineLearning.ITensorUInt64BitStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorUInt64Bit: ...
    @winrt_classmethod
    def CreateFromArray(cls: win32more.Windows.AI.MachineLearning.ITensorUInt64BitStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: PassArray[UInt64]) -> win32more.Windows.AI.MachineLearning.TensorUInt64Bit: ...
    @winrt_classmethod
    def CreateFromIterable(cls: win32more.Windows.AI.MachineLearning.ITensorUInt64BitStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: win32more.Windows.Foundation.Collections.IIterable[UInt64]) -> win32more.Windows.AI.MachineLearning.TensorUInt64Bit: ...
    Kind = property(get_Kind, None)
    Shape = property(get_Shape, None)
    TensorKind = property(get_TensorKind, None)
class TensorUInt8Bit(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.MachineLearning.ITensorUInt8Bit
    _classid_ = 'Windows.AI.MachineLearning.TensorUInt8Bit'
    @winrt_mixinmethod
    def GetAsVectorView(self: win32more.Windows.AI.MachineLearning.ITensorUInt8Bit) -> win32more.Windows.Foundation.Collections.IVectorView[Byte]: ...
    @winrt_mixinmethod
    def get_TensorKind(self: win32more.Windows.AI.MachineLearning.ITensor) -> win32more.Windows.AI.MachineLearning.TensorKind: ...
    @winrt_mixinmethod
    def get_Shape(self: win32more.Windows.AI.MachineLearning.ITensor) -> win32more.Windows.Foundation.Collections.IVectorView[Int64]: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.AI.MachineLearning.ILearningModelFeatureValue) -> win32more.Windows.AI.MachineLearning.LearningModelFeatureKind: ...
    @winrt_mixinmethod
    def CreateReference(self: win32more.Windows.Foundation.IMemoryBuffer) -> win32more.Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFromShapeArrayAndDataArray(cls: win32more.Windows.AI.MachineLearning.ITensorUInt8BitStatics2, shape: PassArray[Int64], data: PassArray[Byte]) -> win32more.Windows.AI.MachineLearning.TensorUInt8Bit: ...
    @winrt_classmethod
    def CreateFromBuffer(cls: win32more.Windows.AI.MachineLearning.ITensorUInt8BitStatics2, shape: PassArray[Int64], buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.AI.MachineLearning.TensorUInt8Bit: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.AI.MachineLearning.ITensorUInt8BitStatics) -> win32more.Windows.AI.MachineLearning.TensorUInt8Bit: ...
    @winrt_classmethod
    def Create2(cls: win32more.Windows.AI.MachineLearning.ITensorUInt8BitStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64]) -> win32more.Windows.AI.MachineLearning.TensorUInt8Bit: ...
    @winrt_classmethod
    def CreateFromArray(cls: win32more.Windows.AI.MachineLearning.ITensorUInt8BitStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: PassArray[Byte]) -> win32more.Windows.AI.MachineLearning.TensorUInt8Bit: ...
    @winrt_classmethod
    def CreateFromIterable(cls: win32more.Windows.AI.MachineLearning.ITensorUInt8BitStatics, shape: win32more.Windows.Foundation.Collections.IIterable[Int64], data: win32more.Windows.Foundation.Collections.IIterable[Byte]) -> win32more.Windows.AI.MachineLearning.TensorUInt8Bit: ...
    Kind = property(get_Kind, None)
    Shape = property(get_Shape, None)
    TensorKind = property(get_TensorKind, None)


make_ready(__name__)
