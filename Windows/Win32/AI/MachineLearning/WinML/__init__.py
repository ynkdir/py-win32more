from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
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
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
WINML_TENSOR_DIMENSION_COUNT_MAX: UInt32 = 4
@winfunctype('winml.dll')
def WinMLCreateRuntime(runtime: POINTER(Windows.Win32.AI.MachineLearning.WinML.IWinMLRuntime_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('windows.ai.machinelearning.dll')
def MLCreateOperatorRegistry(registry: POINTER(Windows.Win32.AI.MachineLearning.WinML.IMLOperatorRegistry_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMLOperatorAttributes(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4b1b1759-ec40-466c-aa-b4-be-b5-34-7f-d2-4c')
    @commethod(3)
    def GetAttributeElementCount(name: Windows.Win32.Foundation.PSTR, type: Windows.Win32.AI.MachineLearning.WinML.MLOperatorAttributeType, elementCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAttribute(name: Windows.Win32.Foundation.PSTR, type: Windows.Win32.AI.MachineLearning.WinML.MLOperatorAttributeType, elementCount: UInt32, elementByteSize: UIntPtr, value: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStringAttributeElementLength(name: Windows.Win32.Foundation.PSTR, elementIndex: UInt32, attributeElementByteSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStringAttributeElement(name: Windows.Win32.Foundation.PSTR, elementIndex: UInt32, attributeElementByteSize: UInt32, attributeElement: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IMLOperatorKernel(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('11c4b4a0-b467-4eaa-a1-a6-b9-61-d8-d0-ed-79')
    @commethod(3)
    def Compute(context: Windows.Win32.AI.MachineLearning.WinML.IMLOperatorKernelContext_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMLOperatorKernelContext(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('82536a28-f022-4769-9d-3f-8b-27-8f-84-c0-c3')
    @commethod(3)
    def GetInputTensor(inputIndex: UInt32, tensor: POINTER(Windows.Win32.AI.MachineLearning.WinML.IMLOperatorTensor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOutputTensor(outputIndex: UInt32, dimensionCount: UInt32, dimensionSizes: POINTER(UInt32), tensor: POINTER(Windows.Win32.AI.MachineLearning.WinML.IMLOperatorTensor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetOutputTensor(outputIndex: UInt32, tensor: POINTER(Windows.Win32.AI.MachineLearning.WinML.IMLOperatorTensor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AllocateTemporaryData(size: UIntPtr, data: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetExecutionInterface(executionObject: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Void: ...
class IMLOperatorKernelCreationContext(c_void_p):
    extends: Windows.Win32.AI.MachineLearning.WinML.IMLOperatorAttributes
    Guid = Guid('5459b53d-a0fc-4665-ad-dd-70-17-1e-f7-e6-31')
    @commethod(7)
    def GetInputCount() -> UInt32: ...
    @commethod(8)
    def GetOutputCount() -> UInt32: ...
    @commethod(9)
    def IsInputValid(inputIndex: UInt32) -> Boolean: ...
    @commethod(10)
    def IsOutputValid(outputIndex: UInt32) -> Boolean: ...
    @commethod(11)
    def GetInputEdgeDescription(inputIndex: UInt32, edgeDescription: POINTER(Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeDescription_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetOutputEdgeDescription(outputIndex: UInt32, edgeDescription: POINTER(Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeDescription_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def HasTensorShapeDescription() -> Boolean: ...
    @commethod(14)
    def GetTensorShapeDescription(shapeDescription: POINTER(Windows.Win32.AI.MachineLearning.WinML.IMLOperatorTensorShapeDescription_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetExecutionInterface(executionObject: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Void: ...
class IMLOperatorKernelFactory(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ef15ad6f-0dc9-4908-ab-35-a5-75-a3-0d-fb-f8')
    @commethod(3)
    def CreateKernel(context: Windows.Win32.AI.MachineLearning.WinML.IMLOperatorKernelCreationContext_head, kernel: POINTER(Windows.Win32.AI.MachineLearning.WinML.IMLOperatorKernel_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMLOperatorRegistry(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2af9dd2d-b516-4672-9a-b5-53-0c-20-84-93-ad')
    @commethod(3)
    def RegisterOperatorSetSchema(operatorSetId: POINTER(Windows.Win32.AI.MachineLearning.WinML.MLOperatorSetId_head), baselineVersion: Int32, schema: POINTER(POINTER(Windows.Win32.AI.MachineLearning.WinML.MLOperatorSchemaDescription_head)), schemaCount: UInt32, typeInferrer: Windows.Win32.AI.MachineLearning.WinML.IMLOperatorTypeInferrer_head, shapeInferrer: Windows.Win32.AI.MachineLearning.WinML.IMLOperatorShapeInferrer_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RegisterOperatorKernel(operatorKernel: POINTER(Windows.Win32.AI.MachineLearning.WinML.MLOperatorKernelDescription_head), operatorKernelFactory: Windows.Win32.AI.MachineLearning.WinML.IMLOperatorKernelFactory_head, shapeInferrer: Windows.Win32.AI.MachineLearning.WinML.IMLOperatorShapeInferrer_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMLOperatorShapeInferenceContext(c_void_p):
    extends: Windows.Win32.AI.MachineLearning.WinML.IMLOperatorAttributes
    Guid = Guid('105b6b29-5408-4a68-99-59-09-b5-95-5a-34-92')
    @commethod(7)
    def GetInputCount() -> UInt32: ...
    @commethod(8)
    def GetOutputCount() -> UInt32: ...
    @commethod(9)
    def IsInputValid(inputIndex: UInt32) -> Boolean: ...
    @commethod(10)
    def IsOutputValid(outputIndex: UInt32) -> Boolean: ...
    @commethod(11)
    def GetInputEdgeDescription(inputIndex: UInt32, edgeDescription: POINTER(Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeDescription_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetInputTensorDimensionCount(inputIndex: UInt32, dimensionCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetInputTensorShape(inputIndex: UInt32, dimensionCount: UInt32, dimensions: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetOutputTensorShape(outputIndex: UInt32, dimensionCount: UInt32, dimensions: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMLOperatorShapeInferrer(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('540be5be-a6c9-40ee-83-f6-d2-b8-b4-0a-77-98')
    @commethod(3)
    def InferOutputShapes(context: Windows.Win32.AI.MachineLearning.WinML.IMLOperatorShapeInferenceContext_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMLOperatorTensor(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7fe41f41-f430-440e-ae-ce-54-41-6d-c8-b9-db')
    @commethod(3)
    def GetDimensionCount() -> UInt32: ...
    @commethod(4)
    def GetShape(dimensionCount: UInt32, dimensions: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTensorDataType() -> Windows.Win32.AI.MachineLearning.WinML.MLOperatorTensorDataType: ...
    @commethod(6)
    def IsCpuData() -> Boolean: ...
    @commethod(7)
    def IsDataInterface() -> Boolean: ...
    @commethod(8)
    def GetData() -> c_void_p: ...
    @commethod(9)
    def GetDataInterface(dataInterface: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Void: ...
class IMLOperatorTensorShapeDescription(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f20e8cbe-3b28-4248-be-95-f9-6f-bc-6e-46-43')
    @commethod(3)
    def GetInputTensorDimensionCount(inputIndex: UInt32, dimensionCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInputTensorShape(inputIndex: UInt32, dimensionCount: UInt32, dimensions: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def HasOutputShapeDescription() -> Boolean: ...
    @commethod(6)
    def GetOutputTensorDimensionCount(outputIndex: UInt32, dimensionCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetOutputTensorShape(outputIndex: UInt32, dimensionCount: UInt32, dimensions: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMLOperatorTypeInferenceContext(c_void_p):
    extends: Windows.Win32.AI.MachineLearning.WinML.IMLOperatorAttributes
    Guid = Guid('ec893bb1-f938-427b-84-88-c8-dc-f7-75-f1-38')
    @commethod(7)
    def GetInputCount() -> UInt32: ...
    @commethod(8)
    def GetOutputCount() -> UInt32: ...
    @commethod(9)
    def IsInputValid(inputIndex: UInt32) -> Boolean: ...
    @commethod(10)
    def IsOutputValid(outputIndex: UInt32) -> Boolean: ...
    @commethod(11)
    def GetInputEdgeDescription(inputIndex: UInt32, edgeDescription: POINTER(Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeDescription_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetOutputEdgeDescription(outputIndex: UInt32, edgeDescription: POINTER(Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeDescription_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMLOperatorTypeInferrer(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('781aeb48-9bcb-4797-bf-77-8b-f4-55-21-7b-eb')
    @commethod(3)
    def InferOutputTypes(context: Windows.Win32.AI.MachineLearning.WinML.IMLOperatorTypeInferenceContext_head) -> Windows.Win32.Foundation.HRESULT: ...
class IWinMLEvaluationContext(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('95848f9e-583d-4054-af-12-91-63-87-cd-84-26')
    @commethod(3)
    def BindValue(pDescriptor: POINTER(Windows.Win32.AI.MachineLearning.WinML.WINML_BINDING_DESC_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetValueByName(Name: Windows.Win32.Foundation.PWSTR, pDescriptor: POINTER(POINTER(Windows.Win32.AI.MachineLearning.WinML.WINML_BINDING_DESC_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Clear() -> Windows.Win32.Foundation.HRESULT: ...
class IWinMLModel(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e2eeb6a9-f31f-4055-a5-21-e3-0b-5b-33-66-4a')
    @commethod(3)
    def GetDescription(ppDescription: POINTER(POINTER(Windows.Win32.AI.MachineLearning.WinML.WINML_MODEL_DESC_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumerateMetadata(Index: UInt32, pKey: POINTER(Windows.Win32.Foundation.PWSTR), pValue: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumerateModelInputs(Index: UInt32, ppInputDescriptor: POINTER(POINTER(Windows.Win32.AI.MachineLearning.WinML.WINML_VARIABLE_DESC_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumerateModelOutputs(Index: UInt32, ppOutputDescriptor: POINTER(POINTER(Windows.Win32.AI.MachineLearning.WinML.WINML_VARIABLE_DESC_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IWinMLRuntime(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a0425329-40ae-48d9-bc-e3-82-9e-f7-b8-a4-1a')
    @commethod(3)
    def LoadModel(Path: Windows.Win32.Foundation.PWSTR, ppModel: POINTER(Windows.Win32.AI.MachineLearning.WinML.IWinMLModel_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateEvaluationContext(device: Windows.Win32.Graphics.Direct3D12.ID3D12Device_head, ppContext: POINTER(Windows.Win32.AI.MachineLearning.WinML.IWinMLEvaluationContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EvaluateModel(pContext: Windows.Win32.AI.MachineLearning.WinML.IWinMLEvaluationContext_head) -> Windows.Win32.Foundation.HRESULT: ...
class IWinMLRuntimeFactory(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a807b84d-4ae5-4bc0-a7-6a-94-1a-a2-46-bd-41')
    @commethod(3)
    def CreateRuntime(RuntimeType: Windows.Win32.AI.MachineLearning.WinML.WINML_RUNTIME_TYPE, ppRuntime: POINTER(Windows.Win32.AI.MachineLearning.WinML.IWinMLRuntime_head)) -> Windows.Win32.Foundation.HRESULT: ...
class MLOperatorAttribute(Structure):
    name: Windows.Win32.Foundation.PSTR
    type: Windows.Win32.AI.MachineLearning.WinML.MLOperatorAttributeType
    required: Byte
class MLOperatorAttributeNameValue(Structure):
    name: Windows.Win32.Foundation.PSTR
    type: Windows.Win32.AI.MachineLearning.WinML.MLOperatorAttributeType
    valueCount: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
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
class MLOperatorEdgeDescription(Structure):
    edgeType: Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeType
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        reserved: UInt64
        tensorDataType: Windows.Win32.AI.MachineLearning.WinML.MLOperatorTensorDataType
MLOperatorEdgeType = UInt32
MLOperatorEdgeType_Undefined: MLOperatorEdgeType = 0
MLOperatorEdgeType_Tensor: MLOperatorEdgeType = 1
class MLOperatorEdgeTypeConstraint(Structure):
    typeLabel: Windows.Win32.Foundation.PSTR
    allowedTypes: POINTER(Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeDescription_head)
    allowedTypeCount: UInt32
MLOperatorExecutionType = UInt32
MLOperatorExecutionType_Undefined: MLOperatorExecutionType = 0
MLOperatorExecutionType_Cpu: MLOperatorExecutionType = 1
MLOperatorExecutionType_D3D12: MLOperatorExecutionType = 2
class MLOperatorKernelDescription(Structure):
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
class MLOperatorSchemaDescription(Structure):
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
class MLOperatorSchemaEdgeDescription(Structure):
    options: Windows.Win32.AI.MachineLearning.WinML.MLOperatorParameterOptions
    typeFormat: Windows.Win32.AI.MachineLearning.WinML.MLOperatorSchemaEdgeTypeFormat
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        reserved: c_void_p
        typeLabel: Windows.Win32.Foundation.PSTR
        edgeDescription: Windows.Win32.AI.MachineLearning.WinML.MLOperatorEdgeDescription
MLOperatorSchemaEdgeTypeFormat = Int32
MLOperatorSchemaEdgeTypeFormat_EdgeDescription: MLOperatorSchemaEdgeTypeFormat = 0
MLOperatorSchemaEdgeTypeFormat_Label: MLOperatorSchemaEdgeTypeFormat = 1
class MLOperatorSetId(Structure):
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
class WINML_BINDING_DESC(Structure):
    Name: Windows.Win32.Foundation.PWSTR
    BindType: Windows.Win32.AI.MachineLearning.WinML.WINML_BINDING_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
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
class WINML_IMAGE_BINDING_DESC(Structure):
    ElementType: Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
    NumDimensions: UInt32
    pShape: POINTER(Int64)
    DataSize: UInt32
    pData: c_void_p
class WINML_IMAGE_VARIABLE_DESC(Structure):
    ElementType: Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
    NumDimensions: UInt32
    pShape: POINTER(Int64)
class WINML_MAP_BINDING_DESC(Structure):
    ElementCount: UInt32
    KeyType: Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
    Anonymous1: _Anonymous1_e__Union
    Fields: Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
    Anonymous2: _Anonymous2_e__Union
    class _Anonymous1_e__Union(Union):
        pStringKeys: POINTER(Windows.Win32.Foundation.PWSTR)
        pIntKeys: POINTER(Int64)
    class _Anonymous2_e__Union(Union):
        pStringFields: POINTER(Windows.Win32.Foundation.PWSTR)
        pIntFields: POINTER(Int64)
        pFloatFields: POINTER(Single)
        pDoubleFields: POINTER(Double)
class WINML_MAP_VARIABLE_DESC(Structure):
    KeyType: Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
    Fields: Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
class WINML_MODEL_DESC(Structure):
    Author: Windows.Win32.Foundation.PWSTR
    Name: Windows.Win32.Foundation.PWSTR
    Domain: Windows.Win32.Foundation.PWSTR
    Description: Windows.Win32.Foundation.PWSTR
    Version: UIntPtr
class WINML_RESOURCE_BINDING_DESC(Structure):
    ElementType: Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
    NumDimensions: UInt32
    pShape: POINTER(Int64)
    pResource: Windows.Win32.Graphics.Direct3D12.ID3D12Resource_head
WINML_RUNTIME_TYPE = Int32
WINML_RUNTIME_CNTK: WINML_RUNTIME_TYPE = 0
class WINML_SEQUENCE_BINDING_DESC(Structure):
    ElementCount: UInt32
    ElementType: Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        pStrings: POINTER(Windows.Win32.Foundation.PWSTR)
        pInts: POINTER(Int64)
        pFloats: POINTER(Single)
        pDoubles: POINTER(Double)
class WINML_SEQUENCE_VARIABLE_DESC(Structure):
    ElementType: Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
class WINML_TENSOR_BINDING_DESC(Structure):
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
class WINML_TENSOR_VARIABLE_DESC(Structure):
    ElementType: Windows.Win32.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE
    NumDimensions: UInt32
    pShape: POINTER(Int64)
class WINML_VARIABLE_DESC(Structure):
    Name: Windows.Win32.Foundation.PWSTR
    Description: Windows.Win32.Foundation.PWSTR
    FeatureType: Windows.Win32.AI.MachineLearning.WinML.WINML_FEATURE_TYPE
    Required: Windows.Win32.Foundation.BOOL
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
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
__all__ = [
    "IMLOperatorAttributes",
    "IMLOperatorKernel",
    "IMLOperatorKernelContext",
    "IMLOperatorKernelCreationContext",
    "IMLOperatorKernelFactory",
    "IMLOperatorRegistry",
    "IMLOperatorShapeInferenceContext",
    "IMLOperatorShapeInferrer",
    "IMLOperatorTensor",
    "IMLOperatorTensorShapeDescription",
    "IMLOperatorTypeInferenceContext",
    "IMLOperatorTypeInferrer",
    "IWinMLEvaluationContext",
    "IWinMLModel",
    "IWinMLRuntime",
    "IWinMLRuntimeFactory",
    "MLCreateOperatorRegistry",
    "MLOperatorAttribute",
    "MLOperatorAttributeNameValue",
    "MLOperatorAttributeType",
    "MLOperatorAttributeType_Float",
    "MLOperatorAttributeType_FloatArray",
    "MLOperatorAttributeType_Int",
    "MLOperatorAttributeType_IntArray",
    "MLOperatorAttributeType_String",
    "MLOperatorAttributeType_StringArray",
    "MLOperatorAttributeType_Undefined",
    "MLOperatorEdgeDescription",
    "MLOperatorEdgeType",
    "MLOperatorEdgeTypeConstraint",
    "MLOperatorEdgeType_Tensor",
    "MLOperatorEdgeType_Undefined",
    "MLOperatorExecutionType",
    "MLOperatorExecutionType_Cpu",
    "MLOperatorExecutionType_D3D12",
    "MLOperatorExecutionType_Undefined",
    "MLOperatorKernelDescription",
    "MLOperatorKernelOptions",
    "MLOperatorKernelOptions_AllowDynamicInputShapes",
    "MLOperatorKernelOptions_None",
    "MLOperatorParameterOptions",
    "MLOperatorParameterOptions_Optional",
    "MLOperatorParameterOptions_Single",
    "MLOperatorParameterOptions_Variadic",
    "MLOperatorSchemaDescription",
    "MLOperatorSchemaEdgeDescription",
    "MLOperatorSchemaEdgeTypeFormat",
    "MLOperatorSchemaEdgeTypeFormat_EdgeDescription",
    "MLOperatorSchemaEdgeTypeFormat_Label",
    "MLOperatorSetId",
    "MLOperatorTensorDataType",
    "MLOperatorTensorDataType_Bool",
    "MLOperatorTensorDataType_Complex128",
    "MLOperatorTensorDataType_Complex64",
    "MLOperatorTensorDataType_Double",
    "MLOperatorTensorDataType_Float",
    "MLOperatorTensorDataType_Float16",
    "MLOperatorTensorDataType_Int16",
    "MLOperatorTensorDataType_Int32",
    "MLOperatorTensorDataType_Int64",
    "MLOperatorTensorDataType_Int8",
    "MLOperatorTensorDataType_String",
    "MLOperatorTensorDataType_UInt16",
    "MLOperatorTensorDataType_UInt32",
    "MLOperatorTensorDataType_UInt64",
    "MLOperatorTensorDataType_UInt8",
    "MLOperatorTensorDataType_Undefined",
    "WINML_BINDING_DESC",
    "WINML_BINDING_IMAGE",
    "WINML_BINDING_MAP",
    "WINML_BINDING_RESOURCE",
    "WINML_BINDING_SEQUENCE",
    "WINML_BINDING_TENSOR",
    "WINML_BINDING_TYPE",
    "WINML_BINDING_UNDEFINED",
    "WINML_FEATURE_IMAGE",
    "WINML_FEATURE_MAP",
    "WINML_FEATURE_SEQUENCE",
    "WINML_FEATURE_TENSOR",
    "WINML_FEATURE_TYPE",
    "WINML_FEATURE_UNDEFINED",
    "WINML_IMAGE_BINDING_DESC",
    "WINML_IMAGE_VARIABLE_DESC",
    "WINML_MAP_BINDING_DESC",
    "WINML_MAP_VARIABLE_DESC",
    "WINML_MODEL_DESC",
    "WINML_RESOURCE_BINDING_DESC",
    "WINML_RUNTIME_CNTK",
    "WINML_RUNTIME_TYPE",
    "WINML_SEQUENCE_BINDING_DESC",
    "WINML_SEQUENCE_VARIABLE_DESC",
    "WINML_TENSOR_BINDING_DESC",
    "WINML_TENSOR_BOOLEAN",
    "WINML_TENSOR_COMPLEX128",
    "WINML_TENSOR_COMPLEX64",
    "WINML_TENSOR_DATA_TYPE",
    "WINML_TENSOR_DIMENSION_COUNT_MAX",
    "WINML_TENSOR_DOUBLE",
    "WINML_TENSOR_FLOAT",
    "WINML_TENSOR_FLOAT16",
    "WINML_TENSOR_INT16",
    "WINML_TENSOR_INT32",
    "WINML_TENSOR_INT64",
    "WINML_TENSOR_INT8",
    "WINML_TENSOR_STRING",
    "WINML_TENSOR_UINT16",
    "WINML_TENSOR_UINT32",
    "WINML_TENSOR_UINT64",
    "WINML_TENSOR_UINT8",
    "WINML_TENSOR_UNDEFINED",
    "WINML_TENSOR_VARIABLE_DESC",
    "WINML_VARIABLE_DESC",
    "WinMLCreateRuntime",
]
_arch_optional = [
]
