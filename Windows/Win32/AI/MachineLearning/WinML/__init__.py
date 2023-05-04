from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.AI.MachineLearning.WinML
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Direct3D12
import Windows.Win32.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
WINML_TENSOR_DIMENSION_COUNT_MAX: UInt32 = 4
@winfunctype('winml.dll')
def WinMLCreateRuntime(runtime: POINTER(Windows.Win32.AI.MachineLearning.WinML.IWinMLRuntime_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('windows.ai.machinelearning.dll')
def MLCreateOperatorRegistry(registry: POINTER(Windows.Win32.AI.MachineLearning.WinML.IMLOperatorRegistry_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMLOperatorAttributes(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4b1b1759-ec40-466c-aab4-beb5347fd24c}')
    @commethod(3)
    def GetAttributeElementCount(self, name: Windows.Win32.Foundation.PSTR, type: Windows.Win32.AI.MachineLearning.WinML.MLOperatorAttributeType, elementCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAttribute(self, name: Windows.Win32.Foundation.PSTR, type: Windows.Win32.AI.MachineLearning.WinML.MLOperatorAttributeType, elementCount: UInt32, elementByteSize: UIntPtr, value: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStringAttributeElementLength(self, name: Windows.Win32.Foundation.PSTR, elementIndex: UInt32, attributeElementByteSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStringAttributeElement(self, name: Windows.Win32.Foundation.PSTR, elementIndex: UInt32, attributeElementByteSize: UInt32, attributeElement: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IMLOperatorKernel(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{11c4b4a0-b467-4eaa-a1a6-b961d8d0ed79}')
    @commethod(3)
    def Compute(self, context: Windows.Win32.AI.MachineLearning.WinML.IMLOperatorKernelContext_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMLOperatorKernelContext(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{82536a28-f022-4769-9d3f-8b278f84c0c3}')
    @commethod(3)
    def GetInputTensor(self, inputIndex: UInt32, tensor: POINTER(Windows.Win32.AI.MachineLearning.WinML.IMLOperatorTensor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOutputTensor(self, outputIndex: UInt32, dimensionCount: UInt32, dimensionSizes: POINTER(UInt32), tensor: POINTER(Windows.Win32.AI.MachineLearning.WinML.IMLOperatorTensor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetOutputTensor(self, outputIndex: UInt32, tensor: POINTER(Windows.Win32.AI.MachineLearning.WinML.IMLOperatorTensor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AllocateTemporaryData(self, size: UIntPtr, data: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetExecutionInterface(self, executionObject: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Void: ...
class IMLOperatorKernelCreationContext(ComPtr):
    extends: Windows.Win32.AI.MachineLearning.WinML.IMLOperatorAttributes
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
    def GetInputEdgeDescription(self, inputIndex: UInt32, edgeDescription: POINTER(Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeDescription_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetOutputEdgeDescription(self, outputIndex: UInt32, edgeDescription: POINTER(Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeDescription_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def HasTensorShapeDescription(self) -> Boolean: ...
    @commethod(14)
    def GetTensorShapeDescription(self, shapeDescription: POINTER(Windows.Win32.AI.MachineLearning.WinML.IMLOperatorTensorShapeDescription_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetExecutionInterface(self, executionObject: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Void: ...
class IMLOperatorKernelFactory(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ef15ad6f-0dc9-4908-ab35-a575a30dfbf8}')
    @commethod(3)
    def CreateKernel(self, context: Windows.Win32.AI.MachineLearning.WinML.IMLOperatorKernelCreationContext_head, kernel: POINTER(Windows.Win32.AI.MachineLearning.WinML.IMLOperatorKernel_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMLOperatorRegistry(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2af9dd2d-b516-4672-9ab5-530c208493ad}')
    @commethod(3)
    def RegisterOperatorSetSchema(self, operatorSetId: POINTER(Windows.Win32.AI.MachineLearning.WinML.MLOperatorSetId_head), baselineVersion: Int32, schema: POINTER(POINTER(Windows.Win32.AI.MachineLearning.WinML.MLOperatorSchemaDescription_head)), schemaCount: UInt32, typeInferrer: Windows.Win32.AI.MachineLearning.WinML.IMLOperatorTypeInferrer_head, shapeInferrer: Windows.Win32.AI.MachineLearning.WinML.IMLOperatorShapeInferrer_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RegisterOperatorKernel(self, operatorKernel: POINTER(Windows.Win32.AI.MachineLearning.WinML.MLOperatorKernelDescription_head), operatorKernelFactory: Windows.Win32.AI.MachineLearning.WinML.IMLOperatorKernelFactory_head, shapeInferrer: Windows.Win32.AI.MachineLearning.WinML.IMLOperatorShapeInferrer_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMLOperatorShapeInferenceContext(ComPtr):
    extends: Windows.Win32.AI.MachineLearning.WinML.IMLOperatorAttributes
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
    def GetInputEdgeDescription(self, inputIndex: UInt32, edgeDescription: POINTER(Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeDescription_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetInputTensorDimensionCount(self, inputIndex: UInt32, dimensionCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetInputTensorShape(self, inputIndex: UInt32, dimensionCount: UInt32, dimensions: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetOutputTensorShape(self, outputIndex: UInt32, dimensionCount: UInt32, dimensions: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMLOperatorShapeInferrer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{540be5be-a6c9-40ee-83f6-d2b8b40a7798}')
    @commethod(3)
    def InferOutputShapes(self, context: Windows.Win32.AI.MachineLearning.WinML.IMLOperatorShapeInferenceContext_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMLOperatorTensor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7fe41f41-f430-440e-aece-54416dc8b9db}')
    @commethod(3)
    def GetDimensionCount(self) -> UInt32: ...
    @commethod(4)
    def GetShape(self, dimensionCount: UInt32, dimensions: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTensorDataType(self) -> Windows.Win32.AI.MachineLearning.WinML.MLOperatorTensorDataType: ...
    @commethod(6)
    def IsCpuData(self) -> Boolean: ...
    @commethod(7)
    def IsDataInterface(self) -> Boolean: ...
    @commethod(8)
    def GetData(self) -> c_void_p: ...
    @commethod(9)
    def GetDataInterface(self, dataInterface: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Void: ...
class IMLOperatorTensorShapeDescription(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f20e8cbe-3b28-4248-be95-f96fbc6e4643}')
    @commethod(3)
    def GetInputTensorDimensionCount(self, inputIndex: UInt32, dimensionCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInputTensorShape(self, inputIndex: UInt32, dimensionCount: UInt32, dimensions: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def HasOutputShapeDescription(self) -> Boolean: ...
    @commethod(6)
    def GetOutputTensorDimensionCount(self, outputIndex: UInt32, dimensionCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetOutputTensorShape(self, outputIndex: UInt32, dimensionCount: UInt32, dimensions: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMLOperatorTypeInferenceContext(ComPtr):
    extends: Windows.Win32.AI.MachineLearning.WinML.IMLOperatorAttributes
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
    def GetInputEdgeDescription(self, inputIndex: UInt32, edgeDescription: POINTER(Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeDescription_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetOutputEdgeDescription(self, outputIndex: UInt32, edgeDescription: POINTER(Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeDescription_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMLOperatorTypeInferrer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{781aeb48-9bcb-4797-bf77-8bf455217beb}')
    @commethod(3)
    def InferOutputTypes(self, context: Windows.Win32.AI.MachineLearning.WinML.IMLOperatorTypeInferenceContext_head) -> Windows.Win32.Foundation.HRESULT: ...
class IWinMLEvaluationContext(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{95848f9e-583d-4054-af12-916387cd8426}')
    @commethod(3)
    def BindValue(self, pDescriptor: POINTER(Windows.Win32.AI.MachineLearning.WinML.WINML_BINDING_DESC_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetValueByName(self, Name: Windows.Win32.Foundation.PWSTR, pDescriptor: POINTER(POINTER(Windows.Win32.AI.MachineLearning.WinML.WINML_BINDING_DESC_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Clear(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWinMLModel(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e2eeb6a9-f31f-4055-a521-e30b5b33664a}')
    @commethod(3)
    def GetDescription(self, ppDescription: POINTER(POINTER(Windows.Win32.AI.MachineLearning.WinML.WINML_MODEL_DESC_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumerateMetadata(self, Index: UInt32, pKey: POINTER(Windows.Win32.Foundation.PWSTR), pValue: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumerateModelInputs(self, Index: UInt32, ppInputDescriptor: POINTER(POINTER(Windows.Win32.AI.MachineLearning.WinML.WINML_VARIABLE_DESC_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumerateModelOutputs(self, Index: UInt32, ppOutputDescriptor: POINTER(POINTER(Windows.Win32.AI.MachineLearning.WinML.WINML_VARIABLE_DESC_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IWinMLRuntime(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a0425329-40ae-48d9-bce3-829ef7b8a41a}')
    @commethod(3)
    def LoadModel(self, Path: Windows.Win32.Foundation.PWSTR, ppModel: POINTER(Windows.Win32.AI.MachineLearning.WinML.IWinMLModel_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateEvaluationContext(self, device: Windows.Win32.Graphics.Direct3D12.ID3D12Device_head, ppContext: POINTER(Windows.Win32.AI.MachineLearning.WinML.IWinMLEvaluationContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EvaluateModel(self, pContext: Windows.Win32.AI.MachineLearning.WinML.IWinMLEvaluationContext_head) -> Windows.Win32.Foundation.HRESULT: ...
class IWinMLRuntimeFactory(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a807b84d-4ae5-4bc0-a76a-941aa246bd41}')
    @commethod(3)
    def CreateRuntime(self, RuntimeType: Windows.Win32.AI.MachineLearning.WinML.WINML_RUNTIME_TYPE, ppRuntime: POINTER(Windows.Win32.AI.MachineLearning.WinML.IWinMLRuntime_head)) -> Windows.Win32.Foundation.HRESULT: ...
class MLOperatorAttribute(EasyCastStructure):
    name: Windows.Win32.Foundation.PSTR
    type: Windows.Win32.AI.MachineLearning.WinML.MLOperatorAttributeType
    required: Byte
class MLOperatorAttributeNameValue(EasyCastStructure):
    name: Windows.Win32.Foundation.PSTR
    type: Windows.Win32.AI.MachineLearning.WinML.MLOperatorAttributeType
    valueCount: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        reserved: c_void_p
        ints: POINTER(Int64)
        strings: POINTER(POINTER(SByte))
        floats: POINTER(Single)
MLOperatorAttributeType = UInt32
MLOperatorAttributeType_Undefined: MLOperatorAttributeType = 0
MLOperatorAttributeType_Float: MLOperatorAttributeType = 2
MLOperatorAttributeType_Int: MLOperatorAttributeType = 3
MLOperatorAttributeType_String: MLOperatorAttributeType = 4
MLOperatorAttributeType_FloatArray: MLOperatorAttributeType = 7
MLOperatorAttributeType_IntArray: MLOperatorAttributeType = 8
MLOperatorAttributeType_StringArray: MLOperatorAttributeType = 9
class MLOperatorEdgeDescription(EasyCastStructure):
    edgeType: Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeType
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        reserved: UInt64
        tensorDataType: Windows.Win32.AI.MachineLearning.WinML.MLOperatorTensorDataType
MLOperatorEdgeType = UInt32
MLOperatorEdgeType_Undefined: MLOperatorEdgeType = 0
MLOperatorEdgeType_Tensor: MLOperatorEdgeType = 1
class MLOperatorEdgeTypeConstraint(EasyCastStructure):
    typeLabel: Windows.Win32.Foundation.PSTR
    allowedTypes: POINTER(Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeDescription_head)
    allowedTypeCount: UInt32
MLOperatorExecutionType = UInt32
MLOperatorExecutionType_Undefined: MLOperatorExecutionType = 0
MLOperatorExecutionType_Cpu: MLOperatorExecutionType = 1
MLOperatorExecutionType_D3D12: MLOperatorExecutionType = 2
class MLOperatorKernelDescription(EasyCastStructure):
    domain: Windows.Win32.Foundation.PSTR
    name: Windows.Win32.Foundation.PSTR
    minimumOperatorSetVersion: Int32
    executionType: Windows.Win32.AI.MachineLearning.WinML.MLOperatorExecutionType
    typeConstraints: POINTER(Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeTypeConstraint_head)
    typeConstraintCount: UInt32
    defaultAttributes: POINTER(Windows.Win32.AI.MachineLearning.WinML.MLOperatorAttributeNameValue_head)
    defaultAttributeCount: UInt32
    options: Windows.Win32.AI.MachineLearning.WinML.MLOperatorKernelOptions
    executionOptions: UInt32
MLOperatorKernelOptions = UInt32
MLOperatorKernelOptions_None: MLOperatorKernelOptions = 0
MLOperatorKernelOptions_AllowDynamicInputShapes: MLOperatorKernelOptions = 1
MLOperatorParameterOptions = UInt32
MLOperatorParameterOptions_Single: MLOperatorParameterOptions = 0
MLOperatorParameterOptions_Optional: MLOperatorParameterOptions = 1
MLOperatorParameterOptions_Variadic: MLOperatorParameterOptions = 2
class MLOperatorSchemaDescription(EasyCastStructure):
    name: Windows.Win32.Foundation.PSTR
    operatorSetVersionAtLastChange: Int32
    inputs: POINTER(Windows.Win32.AI.MachineLearning.WinML.MLOperatorSchemaEdgeDescription_head)
    inputCount: UInt32
    outputs: POINTER(Windows.Win32.AI.MachineLearning.WinML.MLOperatorSchemaEdgeDescription_head)
    outputCount: UInt32
    typeConstraints: POINTER(Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeTypeConstraint_head)
    typeConstraintCount: UInt32
    attributes: POINTER(Windows.Win32.AI.MachineLearning.WinML.MLOperatorAttribute_head)
    attributeCount: UInt32
    defaultAttributes: POINTER(Windows.Win32.AI.MachineLearning.WinML.MLOperatorAttributeNameValue_head)
    defaultAttributeCount: UInt32
class MLOperatorSchemaEdgeDescription(EasyCastStructure):
    options: Windows.Win32.AI.MachineLearning.WinML.MLOperatorParameterOptions
    typeFormat: Windows.Win32.AI.MachineLearning.WinML.MLOperatorSchemaEdgeTypeFormat
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        reserved: c_void_p
        typeLabel: Windows.Win32.Foundation.PSTR
        edgeDescription: Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeDescription
MLOperatorSchemaEdgeTypeFormat = Int32
MLOperatorSchemaEdgeTypeFormat_EdgeDescription: MLOperatorSchemaEdgeTypeFormat = 0
MLOperatorSchemaEdgeTypeFormat_Label: MLOperatorSchemaEdgeTypeFormat = 1
class MLOperatorSetId(EasyCastStructure):
    domain: Windows.Win32.Foundation.PSTR
    version: Int32
MLOperatorTensorDataType = UInt32
MLOperatorTensorDataType_Undefined: MLOperatorTensorDataType = 0
MLOperatorTensorDataType_Float: MLOperatorTensorDataType = 1
MLOperatorTensorDataType_UInt8: MLOperatorTensorDataType = 2
MLOperatorTensorDataType_Int8: MLOperatorTensorDataType = 3
MLOperatorTensorDataType_UInt16: MLOperatorTensorDataType = 4
MLOperatorTensorDataType_Int16: MLOperatorTensorDataType = 5
MLOperatorTensorDataType_Int32: MLOperatorTensorDataType = 6
MLOperatorTensorDataType_Int64: MLOperatorTensorDataType = 7
MLOperatorTensorDataType_String: MLOperatorTensorDataType = 8
MLOperatorTensorDataType_Bool: MLOperatorTensorDataType = 9
MLOperatorTensorDataType_Float16: MLOperatorTensorDataType = 10
MLOperatorTensorDataType_Double: MLOperatorTensorDataType = 11
MLOperatorTensorDataType_UInt32: MLOperatorTensorDataType = 12
MLOperatorTensorDataType_UInt64: MLOperatorTensorDataType = 13
MLOperatorTensorDataType_Complex64: MLOperatorTensorDataType = 14
MLOperatorTensorDataType_Complex128: MLOperatorTensorDataType = 15
class WINML_BINDING_DESC(EasyCastStructure):
    Name: Windows.Win32.Foundation.PWSTR
    BindType: Windows.Win32.AI.MachineLearning.WinML.WINML_BINDING_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Tensor: Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_BINDING_DESC
        Sequence: Windows.Win32.AI.MachineLearning.WinML.WINML_SEQUENCE_BINDING_DESC
        Map: Windows.Win32.AI.MachineLearning.WinML.WINML_MAP_BINDING_DESC
        Image: Windows.Win32.AI.MachineLearning.WinML.WINML_IMAGE_BINDING_DESC
        Resource: Windows.Win32.AI.MachineLearning.WinML.WINML_RESOURCE_BINDING_DESC
WINML_BINDING_TYPE = Int32
WINML_BINDING_UNDEFINED: WINML_BINDING_TYPE = 0
WINML_BINDING_TENSOR: WINML_BINDING_TYPE = 1
WINML_BINDING_SEQUENCE: WINML_BINDING_TYPE = 2
WINML_BINDING_MAP: WINML_BINDING_TYPE = 3
WINML_BINDING_IMAGE: WINML_BINDING_TYPE = 4
WINML_BINDING_RESOURCE: WINML_BINDING_TYPE = 5
WINML_FEATURE_TYPE = Int32
WINML_FEATURE_UNDEFINED: WINML_FEATURE_TYPE = 0
WINML_FEATURE_TENSOR: WINML_FEATURE_TYPE = 1
WINML_FEATURE_SEQUENCE: WINML_FEATURE_TYPE = 2
WINML_FEATURE_MAP: WINML_FEATURE_TYPE = 3
WINML_FEATURE_IMAGE: WINML_FEATURE_TYPE = 4
class WINML_IMAGE_BINDING_DESC(EasyCastStructure):
    ElementType: Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
    NumDimensions: UInt32
    pShape: POINTER(Int64)
    DataSize: UInt32
    pData: c_void_p
class WINML_IMAGE_VARIABLE_DESC(EasyCastStructure):
    ElementType: Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
    NumDimensions: UInt32
    pShape: POINTER(Int64)
class WINML_MAP_BINDING_DESC(EasyCastStructure):
    ElementCount: UInt32
    KeyType: Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
    Anonymous1: _Anonymous1_e__Union
    Fields: Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
    Anonymous2: _Anonymous2_e__Union
    class _Anonymous1_e__Union(EasyCastUnion):
        pStringKeys: POINTER(Windows.Win32.Foundation.PWSTR)
        pIntKeys: POINTER(Int64)
    class _Anonymous2_e__Union(EasyCastUnion):
        pStringFields: POINTER(Windows.Win32.Foundation.PWSTR)
        pIntFields: POINTER(Int64)
        pFloatFields: POINTER(Single)
        pDoubleFields: POINTER(Double)
class WINML_MAP_VARIABLE_DESC(EasyCastStructure):
    KeyType: Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
    Fields: Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
class WINML_MODEL_DESC(EasyCastStructure):
    Author: Windows.Win32.Foundation.PWSTR
    Name: Windows.Win32.Foundation.PWSTR
    Domain: Windows.Win32.Foundation.PWSTR
    Description: Windows.Win32.Foundation.PWSTR
    Version: UIntPtr
class WINML_RESOURCE_BINDING_DESC(EasyCastStructure):
    ElementType: Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
    NumDimensions: UInt32
    pShape: POINTER(Int64)
    pResource: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head
WINML_RUNTIME_TYPE = Int32
WINML_RUNTIME_CNTK: WINML_RUNTIME_TYPE = 0
class WINML_SEQUENCE_BINDING_DESC(EasyCastStructure):
    ElementCount: UInt32
    ElementType: Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        pStrings: POINTER(Windows.Win32.Foundation.PWSTR)
        pInts: POINTER(Int64)
        pFloats: POINTER(Single)
        pDoubles: POINTER(Double)
class WINML_SEQUENCE_VARIABLE_DESC(EasyCastStructure):
    ElementType: Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
class WINML_TENSOR_BINDING_DESC(EasyCastStructure):
    DataType: Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
    NumDimensions: UInt32
    pShape: POINTER(Int64)
    DataSize: UInt32
    pData: c_void_p
WINML_TENSOR_DATA_TYPE = Int32
WINML_TENSOR_UNDEFINED: WINML_TENSOR_DATA_TYPE = 0
WINML_TENSOR_FLOAT: WINML_TENSOR_DATA_TYPE = 1
WINML_TENSOR_UINT8: WINML_TENSOR_DATA_TYPE = 2
WINML_TENSOR_INT8: WINML_TENSOR_DATA_TYPE = 3
WINML_TENSOR_UINT16: WINML_TENSOR_DATA_TYPE = 4
WINML_TENSOR_INT16: WINML_TENSOR_DATA_TYPE = 5
WINML_TENSOR_INT32: WINML_TENSOR_DATA_TYPE = 6
WINML_TENSOR_INT64: WINML_TENSOR_DATA_TYPE = 7
WINML_TENSOR_STRING: WINML_TENSOR_DATA_TYPE = 8
WINML_TENSOR_BOOLEAN: WINML_TENSOR_DATA_TYPE = 9
WINML_TENSOR_FLOAT16: WINML_TENSOR_DATA_TYPE = 10
WINML_TENSOR_DOUBLE: WINML_TENSOR_DATA_TYPE = 11
WINML_TENSOR_UINT32: WINML_TENSOR_DATA_TYPE = 12
WINML_TENSOR_UINT64: WINML_TENSOR_DATA_TYPE = 13
WINML_TENSOR_COMPLEX64: WINML_TENSOR_DATA_TYPE = 14
WINML_TENSOR_COMPLEX128: WINML_TENSOR_DATA_TYPE = 15
class WINML_TENSOR_VARIABLE_DESC(EasyCastStructure):
    ElementType: Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
    NumDimensions: UInt32
    pShape: POINTER(Int64)
class WINML_VARIABLE_DESC(EasyCastStructure):
    Name: Windows.Win32.Foundation.PWSTR
    Description: Windows.Win32.Foundation.PWSTR
    FeatureType: Windows.Win32.AI.MachineLearning.WinML.WINML_FEATURE_TYPE
    Required: Windows.Win32.Foundation.BOOL
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Tensor: Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_VARIABLE_DESC
        Sequence: Windows.Win32.AI.MachineLearning.WinML.WINML_SEQUENCE_VARIABLE_DESC
        Map: Windows.Win32.AI.MachineLearning.WinML.WINML_MAP_VARIABLE_DESC
        Image: Windows.Win32.AI.MachineLearning.WinML.WINML_IMAGE_VARIABLE_DESC
make_head(_module, 'IMLOperatorAttributes')
make_head(_module, 'IMLOperatorKernel')
make_head(_module, 'IMLOperatorKernelContext')
make_head(_module, 'IMLOperatorKernelCreationContext')
make_head(_module, 'IMLOperatorKernelFactory')
make_head(_module, 'IMLOperatorRegistry')
make_head(_module, 'IMLOperatorShapeInferenceContext')
make_head(_module, 'IMLOperatorShapeInferrer')
make_head(_module, 'IMLOperatorTensor')
make_head(_module, 'IMLOperatorTensorShapeDescription')
make_head(_module, 'IMLOperatorTypeInferenceContext')
make_head(_module, 'IMLOperatorTypeInferrer')
make_head(_module, 'IWinMLEvaluationContext')
make_head(_module, 'IWinMLModel')
make_head(_module, 'IWinMLRuntime')
make_head(_module, 'IWinMLRuntimeFactory')
make_head(_module, 'MLOperatorAttribute')
make_head(_module, 'MLOperatorAttributeNameValue')
make_head(_module, 'MLOperatorEdgeDescription')
make_head(_module, 'MLOperatorEdgeTypeConstraint')
make_head(_module, 'MLOperatorKernelDescription')
make_head(_module, 'MLOperatorSchemaDescription')
make_head(_module, 'MLOperatorSchemaEdgeDescription')
make_head(_module, 'MLOperatorSetId')
make_head(_module, 'WINML_BINDING_DESC')
make_head(_module, 'WINML_IMAGE_BINDING_DESC')
make_head(_module, 'WINML_IMAGE_VARIABLE_DESC')
make_head(_module, 'WINML_MAP_BINDING_DESC')
make_head(_module, 'WINML_MAP_VARIABLE_DESC')
make_head(_module, 'WINML_MODEL_DESC')
make_head(_module, 'WINML_RESOURCE_BINDING_DESC')
make_head(_module, 'WINML_SEQUENCE_BINDING_DESC')
make_head(_module, 'WINML_SEQUENCE_VARIABLE_DESC')
make_head(_module, 'WINML_TENSOR_BINDING_DESC')
make_head(_module, 'WINML_TENSOR_VARIABLE_DESC')
make_head(_module, 'WINML_VARIABLE_DESC')
