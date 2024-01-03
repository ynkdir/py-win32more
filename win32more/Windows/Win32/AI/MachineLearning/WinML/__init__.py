from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.AI.MachineLearning.WinML
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Direct3D12
import win32more.Windows.Win32.System.Com
WINML_TENSOR_DIMENSION_COUNT_MAX: UInt32 = 4
@winfunctype('winml.dll')
def WinMLCreateRuntime(runtime: POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.IWinMLRuntime)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('windows.ai.machinelearning.dll')
def MLCreateOperatorRegistry(registry: POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.IMLOperatorRegistry)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMLOperatorAttributes(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4b1b1759-ec40-466c-aab4-beb5347fd24c}')
    @commethod(3)
    def GetAttributeElementCount(self, name: win32more.Windows.Win32.Foundation.PSTR, type: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorAttributeType, elementCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAttribute(self, name: win32more.Windows.Win32.Foundation.PSTR, type: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorAttributeType, elementCount: UInt32, elementByteSize: UIntPtr, value: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStringAttributeElementLength(self, name: win32more.Windows.Win32.Foundation.PSTR, elementIndex: UInt32, attributeElementByteSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStringAttributeElement(self, name: win32more.Windows.Win32.Foundation.PSTR, elementIndex: UInt32, attributeElementByteSize: UInt32, attributeElement: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMLOperatorKernel(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{11c4b4a0-b467-4eaa-a1a6-b961d8d0ed79}')
    @commethod(3)
    def Compute(self, context: win32more.Windows.Win32.AI.MachineLearning.WinML.IMLOperatorKernelContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMLOperatorKernelContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{82536a28-f022-4769-9d3f-8b278f84c0c3}')
    @commethod(3)
    def GetInputTensor(self, inputIndex: UInt32, tensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.IMLOperatorTensor)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOutputTensor(self, outputIndex: UInt32, dimensionCount: UInt32, dimensionSizes: POINTER(UInt32), tensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.IMLOperatorTensor)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetOutputTensor(self, outputIndex: UInt32, tensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.IMLOperatorTensor)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AllocateTemporaryData(self, size: UIntPtr, data: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetExecutionInterface(self, executionObject: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> Void: ...
class IMLOperatorKernelCreationContext(ComPtr):
    extends: win32more.Windows.Win32.AI.MachineLearning.WinML.IMLOperatorAttributes
    _iid_ = Guid('{5459b53d-a0fc-4665-addd-70171ef7e631}')
    @commethod(7)
    def GetInputCount(self) -> UInt32: ...
    @commethod(8)
    def GetOutputCount(self) -> UInt32: ...
    @commethod(9)
    def IsInputValid(self, inputIndex: UInt32) -> Boolean: ...
    @commethod(10)
    def IsOutputValid(self, outputIndex: UInt32) -> Boolean: ...
    @commethod(11)
    def GetInputEdgeDescription(self, inputIndex: UInt32, edgeDescription: POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeDescription)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetOutputEdgeDescription(self, outputIndex: UInt32, edgeDescription: POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeDescription)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def HasTensorShapeDescription(self) -> Boolean: ...
    @commethod(14)
    def GetTensorShapeDescription(self, shapeDescription: POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.IMLOperatorTensorShapeDescription)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetExecutionInterface(self, executionObject: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> Void: ...
class IMLOperatorKernelFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ef15ad6f-0dc9-4908-ab35-a575a30dfbf8}')
    @commethod(3)
    def CreateKernel(self, context: win32more.Windows.Win32.AI.MachineLearning.WinML.IMLOperatorKernelCreationContext, kernel: POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.IMLOperatorKernel)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMLOperatorRegistry(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2af9dd2d-b516-4672-9ab5-530c208493ad}')
    @commethod(3)
    def RegisterOperatorSetSchema(self, operatorSetId: POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorSetId), baselineVersion: Int32, schema: POINTER(POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorSchemaDescription)), schemaCount: UInt32, typeInferrer: win32more.Windows.Win32.AI.MachineLearning.WinML.IMLOperatorTypeInferrer, shapeInferrer: win32more.Windows.Win32.AI.MachineLearning.WinML.IMLOperatorShapeInferrer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RegisterOperatorKernel(self, operatorKernel: POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorKernelDescription), operatorKernelFactory: win32more.Windows.Win32.AI.MachineLearning.WinML.IMLOperatorKernelFactory, shapeInferrer: win32more.Windows.Win32.AI.MachineLearning.WinML.IMLOperatorShapeInferrer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMLOperatorShapeInferenceContext(ComPtr):
    extends: win32more.Windows.Win32.AI.MachineLearning.WinML.IMLOperatorAttributes
    _iid_ = Guid('{105b6b29-5408-4a68-9959-09b5955a3492}')
    @commethod(7)
    def GetInputCount(self) -> UInt32: ...
    @commethod(8)
    def GetOutputCount(self) -> UInt32: ...
    @commethod(9)
    def IsInputValid(self, inputIndex: UInt32) -> Boolean: ...
    @commethod(10)
    def IsOutputValid(self, outputIndex: UInt32) -> Boolean: ...
    @commethod(11)
    def GetInputEdgeDescription(self, inputIndex: UInt32, edgeDescription: POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeDescription)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetInputTensorDimensionCount(self, inputIndex: UInt32, dimensionCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetInputTensorShape(self, inputIndex: UInt32, dimensionCount: UInt32, dimensions: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetOutputTensorShape(self, outputIndex: UInt32, dimensionCount: UInt32, dimensions: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMLOperatorShapeInferrer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{540be5be-a6c9-40ee-83f6-d2b8b40a7798}')
    @commethod(3)
    def InferOutputShapes(self, context: win32more.Windows.Win32.AI.MachineLearning.WinML.IMLOperatorShapeInferenceContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMLOperatorTensor(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7fe41f41-f430-440e-aece-54416dc8b9db}')
    @commethod(3)
    def GetDimensionCount(self) -> UInt32: ...
    @commethod(4)
    def GetShape(self, dimensionCount: UInt32, dimensions: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTensorDataType(self) -> win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorTensorDataType: ...
    @commethod(6)
    def IsCpuData(self) -> Boolean: ...
    @commethod(7)
    def IsDataInterface(self) -> Boolean: ...
    @commethod(8)
    def GetData(self) -> VoidPtr: ...
    @commethod(9)
    def GetDataInterface(self, dataInterface: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> Void: ...
class IMLOperatorTensorShapeDescription(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f20e8cbe-3b28-4248-be95-f96fbc6e4643}')
    @commethod(3)
    def GetInputTensorDimensionCount(self, inputIndex: UInt32, dimensionCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInputTensorShape(self, inputIndex: UInt32, dimensionCount: UInt32, dimensions: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def HasOutputShapeDescription(self) -> Boolean: ...
    @commethod(6)
    def GetOutputTensorDimensionCount(self, outputIndex: UInt32, dimensionCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetOutputTensorShape(self, outputIndex: UInt32, dimensionCount: UInt32, dimensions: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMLOperatorTypeInferenceContext(ComPtr):
    extends: win32more.Windows.Win32.AI.MachineLearning.WinML.IMLOperatorAttributes
    _iid_ = Guid('{ec893bb1-f938-427b-8488-c8dcf775f138}')
    @commethod(7)
    def GetInputCount(self) -> UInt32: ...
    @commethod(8)
    def GetOutputCount(self) -> UInt32: ...
    @commethod(9)
    def IsInputValid(self, inputIndex: UInt32) -> Boolean: ...
    @commethod(10)
    def IsOutputValid(self, outputIndex: UInt32) -> Boolean: ...
    @commethod(11)
    def GetInputEdgeDescription(self, inputIndex: UInt32, edgeDescription: POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeDescription)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetOutputEdgeDescription(self, outputIndex: UInt32, edgeDescription: POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeDescription)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMLOperatorTypeInferrer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{781aeb48-9bcb-4797-bf77-8bf455217beb}')
    @commethod(3)
    def InferOutputTypes(self, context: win32more.Windows.Win32.AI.MachineLearning.WinML.IMLOperatorTypeInferenceContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWinMLEvaluationContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{95848f9e-583d-4054-af12-916387cd8426}')
    @commethod(3)
    def BindValue(self, pDescriptor: POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_BINDING_DESC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetValueByName(self, Name: win32more.Windows.Win32.Foundation.PWSTR, pDescriptor: POINTER(POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_BINDING_DESC))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Clear(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWinMLModel(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e2eeb6a9-f31f-4055-a521-e30b5b33664a}')
    @commethod(3)
    def GetDescription(self, ppDescription: POINTER(POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_MODEL_DESC))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumerateMetadata(self, Index: UInt32, pKey: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pValue: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumerateModelInputs(self, Index: UInt32, ppInputDescriptor: POINTER(POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_VARIABLE_DESC))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumerateModelOutputs(self, Index: UInt32, ppOutputDescriptor: POINTER(POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_VARIABLE_DESC))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWinMLRuntime(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a0425329-40ae-48d9-bce3-829ef7b8a41a}')
    @commethod(3)
    def LoadModel(self, Path: win32more.Windows.Win32.Foundation.PWSTR, ppModel: POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.IWinMLModel)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateEvaluationContext(self, device: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Device, ppContext: POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.IWinMLEvaluationContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EvaluateModel(self, pContext: win32more.Windows.Win32.AI.MachineLearning.WinML.IWinMLEvaluationContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWinMLRuntimeFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a807b84d-4ae5-4bc0-a76a-941aa246bd41}')
    @commethod(3)
    def CreateRuntime(self, RuntimeType: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_RUNTIME_TYPE, ppRuntime: POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.IWinMLRuntime)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class MLOperatorAttribute(EasyCastStructure):
    name: win32more.Windows.Win32.Foundation.PSTR
    type: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorAttributeType
    required: Byte
class MLOperatorAttributeNameValue(EasyCastStructure):
    name: win32more.Windows.Win32.Foundation.PSTR
    type: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorAttributeType
    valueCount: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        reserved: VoidPtr
        ints: POINTER(Int64)
        strings: POINTER(POINTER(SByte))
        floats: POINTER(Single)
MLOperatorAttributeType = UInt32
MLOperatorAttributeType_Undefined: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorAttributeType = 0
MLOperatorAttributeType_Float: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorAttributeType = 2
MLOperatorAttributeType_Int: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorAttributeType = 3
MLOperatorAttributeType_String: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorAttributeType = 4
MLOperatorAttributeType_FloatArray: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorAttributeType = 7
MLOperatorAttributeType_IntArray: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorAttributeType = 8
MLOperatorAttributeType_StringArray: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorAttributeType = 9
class MLOperatorEdgeDescription(EasyCastStructure):
    edgeType: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeType
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        reserved: UInt64
        tensorDataType: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorTensorDataType
MLOperatorEdgeType = UInt32
MLOperatorEdgeType_Undefined: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeType = 0
MLOperatorEdgeType_Tensor: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeType = 1
class MLOperatorEdgeTypeConstraint(EasyCastStructure):
    typeLabel: win32more.Windows.Win32.Foundation.PSTR
    allowedTypes: POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeDescription)
    allowedTypeCount: UInt32
MLOperatorExecutionType = UInt32
MLOperatorExecutionType_Undefined: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorExecutionType = 0
MLOperatorExecutionType_Cpu: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorExecutionType = 1
MLOperatorExecutionType_D3D12: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorExecutionType = 2
class MLOperatorKernelDescription(EasyCastStructure):
    domain: win32more.Windows.Win32.Foundation.PSTR
    name: win32more.Windows.Win32.Foundation.PSTR
    minimumOperatorSetVersion: Int32
    executionType: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorExecutionType
    typeConstraints: POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeTypeConstraint)
    typeConstraintCount: UInt32
    defaultAttributes: POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorAttributeNameValue)
    defaultAttributeCount: UInt32
    options: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorKernelOptions
    executionOptions: UInt32
MLOperatorKernelOptions = UInt32
MLOperatorKernelOptions_None: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorKernelOptions = 0
MLOperatorKernelOptions_AllowDynamicInputShapes: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorKernelOptions = 1
MLOperatorParameterOptions = UInt32
MLOperatorParameterOptions_Single: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorParameterOptions = 0
MLOperatorParameterOptions_Optional: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorParameterOptions = 1
MLOperatorParameterOptions_Variadic: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorParameterOptions = 2
class MLOperatorSchemaDescription(EasyCastStructure):
    name: win32more.Windows.Win32.Foundation.PSTR
    operatorSetVersionAtLastChange: Int32
    inputs: POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorSchemaEdgeDescription)
    inputCount: UInt32
    outputs: POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorSchemaEdgeDescription)
    outputCount: UInt32
    typeConstraints: POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeTypeConstraint)
    typeConstraintCount: UInt32
    attributes: POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorAttribute)
    attributeCount: UInt32
    defaultAttributes: POINTER(win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorAttributeNameValue)
    defaultAttributeCount: UInt32
class MLOperatorSchemaEdgeDescription(EasyCastStructure):
    options: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorParameterOptions
    typeFormat: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorSchemaEdgeTypeFormat
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        reserved: VoidPtr
        typeLabel: win32more.Windows.Win32.Foundation.PSTR
        edgeDescription: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeDescription
MLOperatorSchemaEdgeTypeFormat = Int32
MLOperatorSchemaEdgeTypeFormat_EdgeDescription: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorSchemaEdgeTypeFormat = 0
MLOperatorSchemaEdgeTypeFormat_Label: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorSchemaEdgeTypeFormat = 1
class MLOperatorSetId(EasyCastStructure):
    domain: win32more.Windows.Win32.Foundation.PSTR
    version: Int32
MLOperatorTensorDataType = UInt32
MLOperatorTensorDataType_Undefined: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorTensorDataType = 0
MLOperatorTensorDataType_Float: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorTensorDataType = 1
MLOperatorTensorDataType_UInt8: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorTensorDataType = 2
MLOperatorTensorDataType_Int8: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorTensorDataType = 3
MLOperatorTensorDataType_UInt16: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorTensorDataType = 4
MLOperatorTensorDataType_Int16: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorTensorDataType = 5
MLOperatorTensorDataType_Int32: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorTensorDataType = 6
MLOperatorTensorDataType_Int64: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorTensorDataType = 7
MLOperatorTensorDataType_String: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorTensorDataType = 8
MLOperatorTensorDataType_Bool: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorTensorDataType = 9
MLOperatorTensorDataType_Float16: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorTensorDataType = 10
MLOperatorTensorDataType_Double: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorTensorDataType = 11
MLOperatorTensorDataType_UInt32: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorTensorDataType = 12
MLOperatorTensorDataType_UInt64: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorTensorDataType = 13
MLOperatorTensorDataType_Complex64: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorTensorDataType = 14
MLOperatorTensorDataType_Complex128: win32more.Windows.Win32.AI.MachineLearning.WinML.MLOperatorTensorDataType = 15
class WINML_BINDING_DESC(EasyCastStructure):
    Name: win32more.Windows.Win32.Foundation.PWSTR
    BindType: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_BINDING_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Tensor: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_BINDING_DESC
        Sequence: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_SEQUENCE_BINDING_DESC
        Map: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_MAP_BINDING_DESC
        Image: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_IMAGE_BINDING_DESC
        Resource: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_RESOURCE_BINDING_DESC
WINML_BINDING_TYPE = Int32
WINML_BINDING_UNDEFINED: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_BINDING_TYPE = 0
WINML_BINDING_TENSOR: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_BINDING_TYPE = 1
WINML_BINDING_SEQUENCE: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_BINDING_TYPE = 2
WINML_BINDING_MAP: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_BINDING_TYPE = 3
WINML_BINDING_IMAGE: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_BINDING_TYPE = 4
WINML_BINDING_RESOURCE: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_BINDING_TYPE = 5
WINML_FEATURE_TYPE = Int32
WINML_FEATURE_UNDEFINED: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_FEATURE_TYPE = 0
WINML_FEATURE_TENSOR: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_FEATURE_TYPE = 1
WINML_FEATURE_SEQUENCE: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_FEATURE_TYPE = 2
WINML_FEATURE_MAP: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_FEATURE_TYPE = 3
WINML_FEATURE_IMAGE: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_FEATURE_TYPE = 4
class WINML_IMAGE_BINDING_DESC(EasyCastStructure):
    ElementType: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
    NumDimensions: UInt32
    pShape: POINTER(Int64)
    DataSize: UInt32
    pData: VoidPtr
class WINML_IMAGE_VARIABLE_DESC(EasyCastStructure):
    ElementType: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
    NumDimensions: UInt32
    pShape: POINTER(Int64)
class WINML_MAP_BINDING_DESC(EasyCastStructure):
    ElementCount: UInt32
    KeyType: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
    Anonymous1: _Anonymous1_e__Union
    Fields: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
    Anonymous2: _Anonymous2_e__Union
    class _Anonymous1_e__Union(EasyCastUnion):
        pStringKeys: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
        pIntKeys: POINTER(Int64)
    class _Anonymous2_e__Union(EasyCastUnion):
        pStringFields: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
        pIntFields: POINTER(Int64)
        pFloatFields: POINTER(Single)
        pDoubleFields: POINTER(Double)
class WINML_MAP_VARIABLE_DESC(EasyCastStructure):
    KeyType: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
    Fields: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
class WINML_MODEL_DESC(EasyCastStructure):
    Author: win32more.Windows.Win32.Foundation.PWSTR
    Name: win32more.Windows.Win32.Foundation.PWSTR
    Domain: win32more.Windows.Win32.Foundation.PWSTR
    Description: win32more.Windows.Win32.Foundation.PWSTR
    Version: UIntPtr
class WINML_RESOURCE_BINDING_DESC(EasyCastStructure):
    ElementType: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
    NumDimensions: UInt32
    pShape: POINTER(Int64)
    pResource: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource
WINML_RUNTIME_TYPE = Int32
WINML_RUNTIME_CNTK: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_RUNTIME_TYPE = 0
class WINML_SEQUENCE_BINDING_DESC(EasyCastStructure):
    ElementCount: UInt32
    ElementType: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        pStrings: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
        pInts: POINTER(Int64)
        pFloats: POINTER(Single)
        pDoubles: POINTER(Double)
class WINML_SEQUENCE_VARIABLE_DESC(EasyCastStructure):
    ElementType: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
class WINML_TENSOR_BINDING_DESC(EasyCastStructure):
    DataType: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
    NumDimensions: UInt32
    pShape: POINTER(Int64)
    DataSize: UInt32
    pData: VoidPtr
WINML_TENSOR_DATA_TYPE = Int32
WINML_TENSOR_UNDEFINED: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE = 0
WINML_TENSOR_FLOAT: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE = 1
WINML_TENSOR_UINT8: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE = 2
WINML_TENSOR_INT8: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE = 3
WINML_TENSOR_UINT16: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE = 4
WINML_TENSOR_INT16: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE = 5
WINML_TENSOR_INT32: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE = 6
WINML_TENSOR_INT64: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE = 7
WINML_TENSOR_STRING: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE = 8
WINML_TENSOR_BOOLEAN: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE = 9
WINML_TENSOR_FLOAT16: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE = 10
WINML_TENSOR_DOUBLE: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE = 11
WINML_TENSOR_UINT32: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE = 12
WINML_TENSOR_UINT64: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE = 13
WINML_TENSOR_COMPLEX64: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE = 14
WINML_TENSOR_COMPLEX128: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE = 15
class WINML_TENSOR_VARIABLE_DESC(EasyCastStructure):
    ElementType: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
    NumDimensions: UInt32
    pShape: POINTER(Int64)
class WINML_VARIABLE_DESC(EasyCastStructure):
    Name: win32more.Windows.Win32.Foundation.PWSTR
    Description: win32more.Windows.Win32.Foundation.PWSTR
    FeatureType: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_FEATURE_TYPE
    Required: win32more.Windows.Win32.Foundation.BOOL
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Tensor: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_VARIABLE_DESC
        Sequence: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_SEQUENCE_VARIABLE_DESC
        Map: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_MAP_VARIABLE_DESC
        Image: win32more.Windows.Win32.AI.MachineLearning.WinML.WINML_IMAGE_VARIABLE_DESC


make_ready(__name__)
