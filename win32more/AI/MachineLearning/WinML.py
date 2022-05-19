from win32more import *
import win32more.AI.MachineLearning.WinML
import win32more.Foundation
import win32more.Graphics.Direct3D12
import win32more.System.Com

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
WINML_TENSOR_DIMENSION_COUNT_MAX = 4
WINML_TENSOR_DATA_TYPE = Int32
WINML_TENSOR_UNDEFINED = 0
WINML_TENSOR_FLOAT = 1
WINML_TENSOR_UINT8 = 2
WINML_TENSOR_INT8 = 3
WINML_TENSOR_UINT16 = 4
WINML_TENSOR_INT16 = 5
WINML_TENSOR_INT32 = 6
WINML_TENSOR_INT64 = 7
WINML_TENSOR_STRING = 8
WINML_TENSOR_BOOLEAN = 9
WINML_TENSOR_FLOAT16 = 10
WINML_TENSOR_DOUBLE = 11
WINML_TENSOR_UINT32 = 12
WINML_TENSOR_UINT64 = 13
WINML_TENSOR_COMPLEX64 = 14
WINML_TENSOR_COMPLEX128 = 15
WINML_FEATURE_TYPE = Int32
WINML_FEATURE_UNDEFINED = 0
WINML_FEATURE_TENSOR = 1
WINML_FEATURE_SEQUENCE = 2
WINML_FEATURE_MAP = 3
WINML_FEATURE_IMAGE = 4
WINML_BINDING_TYPE = Int32
WINML_BINDING_UNDEFINED = 0
WINML_BINDING_TENSOR = 1
WINML_BINDING_SEQUENCE = 2
WINML_BINDING_MAP = 3
WINML_BINDING_IMAGE = 4
WINML_BINDING_RESOURCE = 5
def _define_WINML_TENSOR_BINDING_DESC_head():
    class WINML_TENSOR_BINDING_DESC(Structure):
        pass
    return WINML_TENSOR_BINDING_DESC
def _define_WINML_TENSOR_BINDING_DESC():
    WINML_TENSOR_BINDING_DESC = win32more.AI.MachineLearning.WinML.WINML_TENSOR_BINDING_DESC_head
    WINML_TENSOR_BINDING_DESC._fields_ = [
        ("DataType", win32more.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE),
        ("NumDimensions", UInt32),
        ("pShape", POINTER(Int64)),
        ("DataSize", UInt32),
        ("pData", c_void_p),
    ]
    return WINML_TENSOR_BINDING_DESC
def _define_WINML_SEQUENCE_BINDING_DESC_head():
    class WINML_SEQUENCE_BINDING_DESC(Structure):
        pass
    return WINML_SEQUENCE_BINDING_DESC
def _define_WINML_SEQUENCE_BINDING_DESC():
    WINML_SEQUENCE_BINDING_DESC = win32more.AI.MachineLearning.WinML.WINML_SEQUENCE_BINDING_DESC_head
    class WINML_SEQUENCE_BINDING_DESC__Anonymous_e__Union(Union):
        pass
    WINML_SEQUENCE_BINDING_DESC__Anonymous_e__Union._fields_ = [
        ("pStrings", POINTER(win32more.Foundation.PWSTR)),
        ("pInts", POINTER(Int64)),
        ("pFloats", POINTER(Single)),
        ("pDoubles", POINTER(Double)),
    ]
    WINML_SEQUENCE_BINDING_DESC._anonymous_ = [
        'Anonymous',
    ]
    WINML_SEQUENCE_BINDING_DESC._fields_ = [
        ("ElementCount", UInt32),
        ("ElementType", win32more.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE),
        ("Anonymous", WINML_SEQUENCE_BINDING_DESC__Anonymous_e__Union),
    ]
    return WINML_SEQUENCE_BINDING_DESC
def _define_WINML_MAP_BINDING_DESC_head():
    class WINML_MAP_BINDING_DESC(Structure):
        pass
    return WINML_MAP_BINDING_DESC
def _define_WINML_MAP_BINDING_DESC():
    WINML_MAP_BINDING_DESC = win32more.AI.MachineLearning.WinML.WINML_MAP_BINDING_DESC_head
    class WINML_MAP_BINDING_DESC__Anonymous2_e__Union(Union):
        pass
    WINML_MAP_BINDING_DESC__Anonymous2_e__Union._fields_ = [
        ("pStringFields", POINTER(win32more.Foundation.PWSTR)),
        ("pIntFields", POINTER(Int64)),
        ("pFloatFields", POINTER(Single)),
        ("pDoubleFields", POINTER(Double)),
    ]
    class WINML_MAP_BINDING_DESC__Anonymous1_e__Union(Union):
        pass
    WINML_MAP_BINDING_DESC__Anonymous1_e__Union._fields_ = [
        ("pStringKeys", POINTER(win32more.Foundation.PWSTR)),
        ("pIntKeys", POINTER(Int64)),
    ]
    WINML_MAP_BINDING_DESC._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    WINML_MAP_BINDING_DESC._fields_ = [
        ("ElementCount", UInt32),
        ("KeyType", win32more.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE),
        ("Anonymous1", WINML_MAP_BINDING_DESC__Anonymous1_e__Union),
        ("Fields", win32more.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE),
        ("Anonymous2", WINML_MAP_BINDING_DESC__Anonymous2_e__Union),
    ]
    return WINML_MAP_BINDING_DESC
def _define_WINML_IMAGE_BINDING_DESC_head():
    class WINML_IMAGE_BINDING_DESC(Structure):
        pass
    return WINML_IMAGE_BINDING_DESC
def _define_WINML_IMAGE_BINDING_DESC():
    WINML_IMAGE_BINDING_DESC = win32more.AI.MachineLearning.WinML.WINML_IMAGE_BINDING_DESC_head
    WINML_IMAGE_BINDING_DESC._fields_ = [
        ("ElementType", win32more.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE),
        ("NumDimensions", UInt32),
        ("pShape", POINTER(Int64)),
        ("DataSize", UInt32),
        ("pData", c_void_p),
    ]
    return WINML_IMAGE_BINDING_DESC
def _define_WINML_RESOURCE_BINDING_DESC_head():
    class WINML_RESOURCE_BINDING_DESC(Structure):
        pass
    return WINML_RESOURCE_BINDING_DESC
def _define_WINML_RESOURCE_BINDING_DESC():
    WINML_RESOURCE_BINDING_DESC = win32more.AI.MachineLearning.WinML.WINML_RESOURCE_BINDING_DESC_head
    WINML_RESOURCE_BINDING_DESC._fields_ = [
        ("ElementType", win32more.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE),
        ("NumDimensions", UInt32),
        ("pShape", POINTER(Int64)),
        ("pResource", win32more.Graphics.Direct3D12.ID3D12Resource_head),
    ]
    return WINML_RESOURCE_BINDING_DESC
def _define_WINML_BINDING_DESC_head():
    class WINML_BINDING_DESC(Structure):
        pass
    return WINML_BINDING_DESC
def _define_WINML_BINDING_DESC():
    WINML_BINDING_DESC = win32more.AI.MachineLearning.WinML.WINML_BINDING_DESC_head
    class WINML_BINDING_DESC__Anonymous_e__Union(Union):
        pass
    WINML_BINDING_DESC__Anonymous_e__Union._fields_ = [
        ("Tensor", win32more.AI.MachineLearning.WinML.WINML_TENSOR_BINDING_DESC),
        ("Sequence", win32more.AI.MachineLearning.WinML.WINML_SEQUENCE_BINDING_DESC),
        ("Map", win32more.AI.MachineLearning.WinML.WINML_MAP_BINDING_DESC),
        ("Image", win32more.AI.MachineLearning.WinML.WINML_IMAGE_BINDING_DESC),
        ("Resource", win32more.AI.MachineLearning.WinML.WINML_RESOURCE_BINDING_DESC),
    ]
    WINML_BINDING_DESC._anonymous_ = [
        'Anonymous',
    ]
    WINML_BINDING_DESC._fields_ = [
        ("Name", win32more.Foundation.PWSTR),
        ("BindType", win32more.AI.MachineLearning.WinML.WINML_BINDING_TYPE),
        ("Anonymous", WINML_BINDING_DESC__Anonymous_e__Union),
    ]
    return WINML_BINDING_DESC
def _define_WINML_TENSOR_VARIABLE_DESC_head():
    class WINML_TENSOR_VARIABLE_DESC(Structure):
        pass
    return WINML_TENSOR_VARIABLE_DESC
def _define_WINML_TENSOR_VARIABLE_DESC():
    WINML_TENSOR_VARIABLE_DESC = win32more.AI.MachineLearning.WinML.WINML_TENSOR_VARIABLE_DESC_head
    WINML_TENSOR_VARIABLE_DESC._fields_ = [
        ("ElementType", win32more.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE),
        ("NumDimensions", UInt32),
        ("pShape", POINTER(Int64)),
    ]
    return WINML_TENSOR_VARIABLE_DESC
def _define_WINML_SEQUENCE_VARIABLE_DESC_head():
    class WINML_SEQUENCE_VARIABLE_DESC(Structure):
        pass
    return WINML_SEQUENCE_VARIABLE_DESC
def _define_WINML_SEQUENCE_VARIABLE_DESC():
    WINML_SEQUENCE_VARIABLE_DESC = win32more.AI.MachineLearning.WinML.WINML_SEQUENCE_VARIABLE_DESC_head
    WINML_SEQUENCE_VARIABLE_DESC._fields_ = [
        ("ElementType", win32more.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE),
    ]
    return WINML_SEQUENCE_VARIABLE_DESC
def _define_WINML_MAP_VARIABLE_DESC_head():
    class WINML_MAP_VARIABLE_DESC(Structure):
        pass
    return WINML_MAP_VARIABLE_DESC
def _define_WINML_MAP_VARIABLE_DESC():
    WINML_MAP_VARIABLE_DESC = win32more.AI.MachineLearning.WinML.WINML_MAP_VARIABLE_DESC_head
    WINML_MAP_VARIABLE_DESC._fields_ = [
        ("KeyType", win32more.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE),
        ("Fields", win32more.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE),
    ]
    return WINML_MAP_VARIABLE_DESC
def _define_WINML_IMAGE_VARIABLE_DESC_head():
    class WINML_IMAGE_VARIABLE_DESC(Structure):
        pass
    return WINML_IMAGE_VARIABLE_DESC
def _define_WINML_IMAGE_VARIABLE_DESC():
    WINML_IMAGE_VARIABLE_DESC = win32more.AI.MachineLearning.WinML.WINML_IMAGE_VARIABLE_DESC_head
    WINML_IMAGE_VARIABLE_DESC._fields_ = [
        ("ElementType", win32more.AI.MachineLearning.WinML.WINML_TENSOR_DATA_TYPE),
        ("NumDimensions", UInt32),
        ("pShape", POINTER(Int64)),
    ]
    return WINML_IMAGE_VARIABLE_DESC
def _define_WINML_VARIABLE_DESC_head():
    class WINML_VARIABLE_DESC(Structure):
        pass
    return WINML_VARIABLE_DESC
def _define_WINML_VARIABLE_DESC():
    WINML_VARIABLE_DESC = win32more.AI.MachineLearning.WinML.WINML_VARIABLE_DESC_head
    class WINML_VARIABLE_DESC__Anonymous_e__Union(Union):
        pass
    WINML_VARIABLE_DESC__Anonymous_e__Union._fields_ = [
        ("Tensor", win32more.AI.MachineLearning.WinML.WINML_TENSOR_VARIABLE_DESC),
        ("Sequence", win32more.AI.MachineLearning.WinML.WINML_SEQUENCE_VARIABLE_DESC),
        ("Map", win32more.AI.MachineLearning.WinML.WINML_MAP_VARIABLE_DESC),
        ("Image", win32more.AI.MachineLearning.WinML.WINML_IMAGE_VARIABLE_DESC),
    ]
    WINML_VARIABLE_DESC._anonymous_ = [
        'Anonymous',
    ]
    WINML_VARIABLE_DESC._fields_ = [
        ("Name", win32more.Foundation.PWSTR),
        ("Description", win32more.Foundation.PWSTR),
        ("FeatureType", win32more.AI.MachineLearning.WinML.WINML_FEATURE_TYPE),
        ("Required", win32more.Foundation.BOOL),
        ("Anonymous", WINML_VARIABLE_DESC__Anonymous_e__Union),
    ]
    return WINML_VARIABLE_DESC
def _define_WINML_MODEL_DESC_head():
    class WINML_MODEL_DESC(Structure):
        pass
    return WINML_MODEL_DESC
def _define_WINML_MODEL_DESC():
    WINML_MODEL_DESC = win32more.AI.MachineLearning.WinML.WINML_MODEL_DESC_head
    WINML_MODEL_DESC._fields_ = [
        ("Author", win32more.Foundation.PWSTR),
        ("Name", win32more.Foundation.PWSTR),
        ("Domain", win32more.Foundation.PWSTR),
        ("Description", win32more.Foundation.PWSTR),
        ("Version", UIntPtr),
    ]
    return WINML_MODEL_DESC
def _define_IWinMLModel_head():
    class IWinMLModel(win32more.System.Com.IUnknown_head):
        Guid = Guid('e2eeb6a9-f31f-4055-a521-e30b5b33664a')
    return IWinMLModel
def _define_IWinMLModel():
    IWinMLModel = win32more.AI.MachineLearning.WinML.IWinMLModel_head
    IWinMLModel.GetDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.AI.MachineLearning.WinML.WINML_MODEL_DESC_head)), use_last_error=False)(3, 'GetDescription', ((1, 'ppDescription'),)))
    IWinMLModel.EnumerateMetadata = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(4, 'EnumerateMetadata', ((1, 'Index'),(1, 'pKey'),(1, 'pValue'),)))
    IWinMLModel.EnumerateModelInputs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.AI.MachineLearning.WinML.WINML_VARIABLE_DESC_head)), use_last_error=False)(5, 'EnumerateModelInputs', ((1, 'Index'),(1, 'ppInputDescriptor'),)))
    IWinMLModel.EnumerateModelOutputs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.AI.MachineLearning.WinML.WINML_VARIABLE_DESC_head)), use_last_error=False)(6, 'EnumerateModelOutputs', ((1, 'Index'),(1, 'ppOutputDescriptor'),)))
    return IWinMLModel
def _define_IWinMLEvaluationContext_head():
    class IWinMLEvaluationContext(win32more.System.Com.IUnknown_head):
        Guid = Guid('95848f9e-583d-4054-af12-916387cd8426')
    return IWinMLEvaluationContext
def _define_IWinMLEvaluationContext():
    IWinMLEvaluationContext = win32more.AI.MachineLearning.WinML.IWinMLEvaluationContext_head
    IWinMLEvaluationContext.BindValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.AI.MachineLearning.WinML.WINML_BINDING_DESC_head), use_last_error=False)(3, 'BindValue', ((1, 'pDescriptor'),)))
    IWinMLEvaluationContext.GetValueByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.AI.MachineLearning.WinML.WINML_BINDING_DESC_head)), use_last_error=False)(4, 'GetValueByName', ((1, 'Name'),(1, 'pDescriptor'),)))
    IWinMLEvaluationContext.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Clear', ()))
    return IWinMLEvaluationContext
def _define_IWinMLRuntime_head():
    class IWinMLRuntime(win32more.System.Com.IUnknown_head):
        Guid = Guid('a0425329-40ae-48d9-bce3-829ef7b8a41a')
    return IWinMLRuntime
def _define_IWinMLRuntime():
    IWinMLRuntime = win32more.AI.MachineLearning.WinML.IWinMLRuntime_head
    IWinMLRuntime.LoadModel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.AI.MachineLearning.WinML.IWinMLModel_head), use_last_error=False)(3, 'LoadModel', ((1, 'Path'),(1, 'ppModel'),)))
    IWinMLRuntime.CreateEvaluationContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D12.ID3D12Device_head,POINTER(win32more.AI.MachineLearning.WinML.IWinMLEvaluationContext_head), use_last_error=False)(4, 'CreateEvaluationContext', ((1, 'device'),(1, 'ppContext'),)))
    IWinMLRuntime.EvaluateModel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.AI.MachineLearning.WinML.IWinMLEvaluationContext_head, use_last_error=False)(5, 'EvaluateModel', ((1, 'pContext'),)))
    return IWinMLRuntime
WINML_RUNTIME_TYPE = Int32
WINML_RUNTIME_CNTK = 0
def _define_IWinMLRuntimeFactory_head():
    class IWinMLRuntimeFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('a807b84d-4ae5-4bc0-a76a-941aa246bd41')
    return IWinMLRuntimeFactory
def _define_IWinMLRuntimeFactory():
    IWinMLRuntimeFactory = win32more.AI.MachineLearning.WinML.IWinMLRuntimeFactory_head
    IWinMLRuntimeFactory.CreateRuntime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.AI.MachineLearning.WinML.WINML_RUNTIME_TYPE,POINTER(win32more.AI.MachineLearning.WinML.IWinMLRuntime_head), use_last_error=False)(3, 'CreateRuntime', ((1, 'RuntimeType'),(1, 'ppRuntime'),)))
    return IWinMLRuntimeFactory
MLOperatorAttributeType = UInt32
MLOperatorAttributeType_Undefined = 0
MLOperatorAttributeType_Float = 2
MLOperatorAttributeType_Int = 3
MLOperatorAttributeType_String = 4
MLOperatorAttributeType_FloatArray = 7
MLOperatorAttributeType_IntArray = 8
MLOperatorAttributeType_StringArray = 9
MLOperatorTensorDataType = UInt32
MLOperatorTensorDataType_Undefined = 0
MLOperatorTensorDataType_Float = 1
MLOperatorTensorDataType_UInt8 = 2
MLOperatorTensorDataType_Int8 = 3
MLOperatorTensorDataType_UInt16 = 4
MLOperatorTensorDataType_Int16 = 5
MLOperatorTensorDataType_Int32 = 6
MLOperatorTensorDataType_Int64 = 7
MLOperatorTensorDataType_String = 8
MLOperatorTensorDataType_Bool = 9
MLOperatorTensorDataType_Float16 = 10
MLOperatorTensorDataType_Double = 11
MLOperatorTensorDataType_UInt32 = 12
MLOperatorTensorDataType_UInt64 = 13
MLOperatorTensorDataType_Complex64 = 14
MLOperatorTensorDataType_Complex128 = 15
MLOperatorEdgeType = UInt32
MLOperatorEdgeType_Undefined = 0
MLOperatorEdgeType_Tensor = 1
def _define_MLOperatorEdgeDescription_head():
    class MLOperatorEdgeDescription(Structure):
        pass
    return MLOperatorEdgeDescription
def _define_MLOperatorEdgeDescription():
    MLOperatorEdgeDescription = win32more.AI.MachineLearning.WinML.MLOperatorEdgeDescription_head
    class MLOperatorEdgeDescription__Anonymous_e__Union(Union):
        pass
    MLOperatorEdgeDescription__Anonymous_e__Union._fields_ = [
        ("reserved", UInt64),
        ("tensorDataType", win32more.AI.MachineLearning.WinML.MLOperatorTensorDataType),
    ]
    MLOperatorEdgeDescription._anonymous_ = [
        'Anonymous',
    ]
    MLOperatorEdgeDescription._fields_ = [
        ("edgeType", win32more.AI.MachineLearning.WinML.MLOperatorEdgeType),
        ("Anonymous", MLOperatorEdgeDescription__Anonymous_e__Union),
    ]
    return MLOperatorEdgeDescription
def _define_IMLOperatorAttributes_head():
    class IMLOperatorAttributes(win32more.System.Com.IUnknown_head):
        Guid = Guid('4b1b1759-ec40-466c-aab4-beb5347fd24c')
    return IMLOperatorAttributes
def _define_IMLOperatorAttributes():
    IMLOperatorAttributes = win32more.AI.MachineLearning.WinML.IMLOperatorAttributes_head
    IMLOperatorAttributes.GetAttributeElementCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,win32more.AI.MachineLearning.WinML.MLOperatorAttributeType,POINTER(UInt32), use_last_error=False)(3, 'GetAttributeElementCount', ((1, 'name'),(1, 'type'),(1, 'elementCount'),)))
    IMLOperatorAttributes.GetAttribute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,win32more.AI.MachineLearning.WinML.MLOperatorAttributeType,UInt32,UIntPtr,c_void_p, use_last_error=False)(4, 'GetAttribute', ((1, 'name'),(1, 'type'),(1, 'elementCount'),(1, 'elementByteSize'),(1, 'value'),)))
    IMLOperatorAttributes.GetStringAttributeElementLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,UInt32,POINTER(UInt32), use_last_error=False)(5, 'GetStringAttributeElementLength', ((1, 'name'),(1, 'elementIndex'),(1, 'attributeElementByteSize'),)))
    IMLOperatorAttributes.GetStringAttributeElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,UInt32,UInt32,POINTER(Byte), use_last_error=False)(6, 'GetStringAttributeElement', ((1, 'name'),(1, 'elementIndex'),(1, 'attributeElementByteSize'),(1, 'attributeElement'),)))
    return IMLOperatorAttributes
def _define_IMLOperatorTensorShapeDescription_head():
    class IMLOperatorTensorShapeDescription(win32more.System.Com.IUnknown_head):
        Guid = Guid('f20e8cbe-3b28-4248-be95-f96fbc6e4643')
    return IMLOperatorTensorShapeDescription
def _define_IMLOperatorTensorShapeDescription():
    IMLOperatorTensorShapeDescription = win32more.AI.MachineLearning.WinML.IMLOperatorTensorShapeDescription_head
    IMLOperatorTensorShapeDescription.GetInputTensorDimensionCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(3, 'GetInputTensorDimensionCount', ((1, 'inputIndex'),(1, 'dimensionCount'),)))
    IMLOperatorTensorShapeDescription.GetInputTensorShape = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(UInt32), use_last_error=False)(4, 'GetInputTensorShape', ((1, 'inputIndex'),(1, 'dimensionCount'),(1, 'dimensions'),)))
    IMLOperatorTensorShapeDescription.HasOutputShapeDescription = COMMETHOD(WINFUNCTYPE(Boolean, use_last_error=False)(5, 'HasOutputShapeDescription', ()))
    IMLOperatorTensorShapeDescription.GetOutputTensorDimensionCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(6, 'GetOutputTensorDimensionCount', ((1, 'outputIndex'),(1, 'dimensionCount'),)))
    IMLOperatorTensorShapeDescription.GetOutputTensorShape = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(UInt32), use_last_error=False)(7, 'GetOutputTensorShape', ((1, 'outputIndex'),(1, 'dimensionCount'),(1, 'dimensions'),)))
    return IMLOperatorTensorShapeDescription
def _define_IMLOperatorKernelCreationContext_head():
    class IMLOperatorKernelCreationContext(win32more.AI.MachineLearning.WinML.IMLOperatorAttributes_head):
        Guid = Guid('5459b53d-a0fc-4665-addd-70171ef7e631')
    return IMLOperatorKernelCreationContext
def _define_IMLOperatorKernelCreationContext():
    IMLOperatorKernelCreationContext = win32more.AI.MachineLearning.WinML.IMLOperatorKernelCreationContext_head
    IMLOperatorKernelCreationContext.GetInputCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(7, 'GetInputCount', ()))
    IMLOperatorKernelCreationContext.GetOutputCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(8, 'GetOutputCount', ()))
    IMLOperatorKernelCreationContext.IsInputValid = COMMETHOD(WINFUNCTYPE(Boolean,UInt32, use_last_error=False)(9, 'IsInputValid', ((1, 'inputIndex'),)))
    IMLOperatorKernelCreationContext.IsOutputValid = COMMETHOD(WINFUNCTYPE(Boolean,UInt32, use_last_error=False)(10, 'IsOutputValid', ((1, 'outputIndex'),)))
    IMLOperatorKernelCreationContext.GetInputEdgeDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.AI.MachineLearning.WinML.MLOperatorEdgeDescription_head), use_last_error=False)(11, 'GetInputEdgeDescription', ((1, 'inputIndex'),(1, 'edgeDescription'),)))
    IMLOperatorKernelCreationContext.GetOutputEdgeDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.AI.MachineLearning.WinML.MLOperatorEdgeDescription_head), use_last_error=False)(12, 'GetOutputEdgeDescription', ((1, 'outputIndex'),(1, 'edgeDescription'),)))
    IMLOperatorKernelCreationContext.HasTensorShapeDescription = COMMETHOD(WINFUNCTYPE(Boolean, use_last_error=False)(13, 'HasTensorShapeDescription', ()))
    IMLOperatorKernelCreationContext.GetTensorShapeDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.AI.MachineLearning.WinML.IMLOperatorTensorShapeDescription_head), use_last_error=False)(14, 'GetTensorShapeDescription', ((1, 'shapeDescription'),)))
    IMLOperatorKernelCreationContext.GetExecutionInterface = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(15, 'GetExecutionInterface', ((1, 'executionObject'),)))
    return IMLOperatorKernelCreationContext
def _define_IMLOperatorTensor_head():
    class IMLOperatorTensor(win32more.System.Com.IUnknown_head):
        Guid = Guid('7fe41f41-f430-440e-aece-54416dc8b9db')
    return IMLOperatorTensor
def _define_IMLOperatorTensor():
    IMLOperatorTensor = win32more.AI.MachineLearning.WinML.IMLOperatorTensor_head
    IMLOperatorTensor.GetDimensionCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(3, 'GetDimensionCount', ()))
    IMLOperatorTensor.GetShape = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(4, 'GetShape', ((1, 'dimensionCount'),(1, 'dimensions'),)))
    IMLOperatorTensor.GetTensorDataType = COMMETHOD(WINFUNCTYPE(win32more.AI.MachineLearning.WinML.MLOperatorTensorDataType, use_last_error=False)(5, 'GetTensorDataType', ()))
    IMLOperatorTensor.IsCpuData = COMMETHOD(WINFUNCTYPE(Boolean, use_last_error=False)(6, 'IsCpuData', ()))
    IMLOperatorTensor.IsDataInterface = COMMETHOD(WINFUNCTYPE(Boolean, use_last_error=False)(7, 'IsDataInterface', ()))
    IMLOperatorTensor.GetData = COMMETHOD(WINFUNCTYPE(c_void_p, use_last_error=False)(8, 'GetData', ()))
    IMLOperatorTensor.GetDataInterface = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'GetDataInterface', ((1, 'dataInterface'),)))
    return IMLOperatorTensor
def _define_IMLOperatorKernelContext_head():
    class IMLOperatorKernelContext(win32more.System.Com.IUnknown_head):
        Guid = Guid('82536a28-f022-4769-9d3f-8b278f84c0c3')
    return IMLOperatorKernelContext
def _define_IMLOperatorKernelContext():
    IMLOperatorKernelContext = win32more.AI.MachineLearning.WinML.IMLOperatorKernelContext_head
    IMLOperatorKernelContext.GetInputTensor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.AI.MachineLearning.WinML.IMLOperatorTensor_head), use_last_error=False)(3, 'GetInputTensor', ((1, 'inputIndex'),(1, 'tensor'),)))
    IMLOperatorKernelContext.GetOutputTensor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(UInt32),POINTER(win32more.AI.MachineLearning.WinML.IMLOperatorTensor_head), use_last_error=False)(4, 'GetOutputTensor', ((1, 'outputIndex'),(1, 'dimensionCount'),(1, 'dimensionSizes'),(1, 'tensor'),)))
    IMLOperatorKernelContext.GetOutputTensor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.AI.MachineLearning.WinML.IMLOperatorTensor_head), use_last_error=False)(5, 'GetOutputTensor', ((1, 'outputIndex'),(1, 'tensor'),)))
    IMLOperatorKernelContext.AllocateTemporaryData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(6, 'AllocateTemporaryData', ((1, 'size'),(1, 'data'),)))
    IMLOperatorKernelContext.GetExecutionInterface = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'GetExecutionInterface', ((1, 'executionObject'),)))
    return IMLOperatorKernelContext
def _define_IMLOperatorKernel_head():
    class IMLOperatorKernel(win32more.System.Com.IUnknown_head):
        Guid = Guid('11c4b4a0-b467-4eaa-a1a6-b961d8d0ed79')
    return IMLOperatorKernel
def _define_IMLOperatorKernel():
    IMLOperatorKernel = win32more.AI.MachineLearning.WinML.IMLOperatorKernel_head
    IMLOperatorKernel.Compute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.AI.MachineLearning.WinML.IMLOperatorKernelContext_head, use_last_error=False)(3, 'Compute', ((1, 'context'),)))
    return IMLOperatorKernel
MLOperatorParameterOptions = UInt32
MLOperatorParameterOptions_Single = 0
MLOperatorParameterOptions_Optional = 1
MLOperatorParameterOptions_Variadic = 2
MLOperatorSchemaEdgeTypeFormat = Int32
MLOperatorSchemaEdgeTypeFormat_EdgeDescription = 0
MLOperatorSchemaEdgeTypeFormat_Label = 1
def _define_MLOperatorSchemaEdgeDescription_head():
    class MLOperatorSchemaEdgeDescription(Structure):
        pass
    return MLOperatorSchemaEdgeDescription
def _define_MLOperatorSchemaEdgeDescription():
    MLOperatorSchemaEdgeDescription = win32more.AI.MachineLearning.WinML.MLOperatorSchemaEdgeDescription_head
    class MLOperatorSchemaEdgeDescription__Anonymous_e__Union(Union):
        pass
    MLOperatorSchemaEdgeDescription__Anonymous_e__Union._fields_ = [
        ("reserved", c_void_p),
        ("typeLabel", win32more.Foundation.PSTR),
        ("edgeDescription", win32more.AI.MachineLearning.WinML.MLOperatorEdgeDescription),
    ]
    MLOperatorSchemaEdgeDescription._anonymous_ = [
        'Anonymous',
    ]
    MLOperatorSchemaEdgeDescription._fields_ = [
        ("options", win32more.AI.MachineLearning.WinML.MLOperatorParameterOptions),
        ("typeFormat", win32more.AI.MachineLearning.WinML.MLOperatorSchemaEdgeTypeFormat),
        ("Anonymous", MLOperatorSchemaEdgeDescription__Anonymous_e__Union),
    ]
    return MLOperatorSchemaEdgeDescription
def _define_MLOperatorEdgeTypeConstraint_head():
    class MLOperatorEdgeTypeConstraint(Structure):
        pass
    return MLOperatorEdgeTypeConstraint
def _define_MLOperatorEdgeTypeConstraint():
    MLOperatorEdgeTypeConstraint = win32more.AI.MachineLearning.WinML.MLOperatorEdgeTypeConstraint_head
    MLOperatorEdgeTypeConstraint._fields_ = [
        ("typeLabel", win32more.Foundation.PSTR),
        ("allowedTypes", POINTER(win32more.AI.MachineLearning.WinML.MLOperatorEdgeDescription_head)),
        ("allowedTypeCount", UInt32),
    ]
    return MLOperatorEdgeTypeConstraint
def _define_IMLOperatorShapeInferenceContext_head():
    class IMLOperatorShapeInferenceContext(win32more.AI.MachineLearning.WinML.IMLOperatorAttributes_head):
        Guid = Guid('105b6b29-5408-4a68-9959-09b5955a3492')
    return IMLOperatorShapeInferenceContext
def _define_IMLOperatorShapeInferenceContext():
    IMLOperatorShapeInferenceContext = win32more.AI.MachineLearning.WinML.IMLOperatorShapeInferenceContext_head
    IMLOperatorShapeInferenceContext.GetInputCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(7, 'GetInputCount', ()))
    IMLOperatorShapeInferenceContext.GetOutputCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(8, 'GetOutputCount', ()))
    IMLOperatorShapeInferenceContext.IsInputValid = COMMETHOD(WINFUNCTYPE(Boolean,UInt32, use_last_error=False)(9, 'IsInputValid', ((1, 'inputIndex'),)))
    IMLOperatorShapeInferenceContext.IsOutputValid = COMMETHOD(WINFUNCTYPE(Boolean,UInt32, use_last_error=False)(10, 'IsOutputValid', ((1, 'outputIndex'),)))
    IMLOperatorShapeInferenceContext.GetInputEdgeDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.AI.MachineLearning.WinML.MLOperatorEdgeDescription_head), use_last_error=False)(11, 'GetInputEdgeDescription', ((1, 'inputIndex'),(1, 'edgeDescription'),)))
    IMLOperatorShapeInferenceContext.GetInputTensorDimensionCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(12, 'GetInputTensorDimensionCount', ((1, 'inputIndex'),(1, 'dimensionCount'),)))
    IMLOperatorShapeInferenceContext.GetInputTensorShape = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(UInt32), use_last_error=False)(13, 'GetInputTensorShape', ((1, 'inputIndex'),(1, 'dimensionCount'),(1, 'dimensions'),)))
    IMLOperatorShapeInferenceContext.SetOutputTensorShape = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(UInt32), use_last_error=False)(14, 'SetOutputTensorShape', ((1, 'outputIndex'),(1, 'dimensionCount'),(1, 'dimensions'),)))
    return IMLOperatorShapeInferenceContext
def _define_IMLOperatorTypeInferenceContext_head():
    class IMLOperatorTypeInferenceContext(win32more.AI.MachineLearning.WinML.IMLOperatorAttributes_head):
        Guid = Guid('ec893bb1-f938-427b-8488-c8dcf775f138')
    return IMLOperatorTypeInferenceContext
def _define_IMLOperatorTypeInferenceContext():
    IMLOperatorTypeInferenceContext = win32more.AI.MachineLearning.WinML.IMLOperatorTypeInferenceContext_head
    IMLOperatorTypeInferenceContext.GetInputCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(7, 'GetInputCount', ()))
    IMLOperatorTypeInferenceContext.GetOutputCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(8, 'GetOutputCount', ()))
    IMLOperatorTypeInferenceContext.IsInputValid = COMMETHOD(WINFUNCTYPE(Boolean,UInt32, use_last_error=False)(9, 'IsInputValid', ((1, 'inputIndex'),)))
    IMLOperatorTypeInferenceContext.IsOutputValid = COMMETHOD(WINFUNCTYPE(Boolean,UInt32, use_last_error=False)(10, 'IsOutputValid', ((1, 'outputIndex'),)))
    IMLOperatorTypeInferenceContext.GetInputEdgeDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.AI.MachineLearning.WinML.MLOperatorEdgeDescription_head), use_last_error=False)(11, 'GetInputEdgeDescription', ((1, 'inputIndex'),(1, 'edgeDescription'),)))
    IMLOperatorTypeInferenceContext.SetOutputEdgeDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.AI.MachineLearning.WinML.MLOperatorEdgeDescription_head), use_last_error=False)(12, 'SetOutputEdgeDescription', ((1, 'outputIndex'),(1, 'edgeDescription'),)))
    return IMLOperatorTypeInferenceContext
def _define_IMLOperatorTypeInferrer_head():
    class IMLOperatorTypeInferrer(win32more.System.Com.IUnknown_head):
        Guid = Guid('781aeb48-9bcb-4797-bf77-8bf455217beb')
    return IMLOperatorTypeInferrer
def _define_IMLOperatorTypeInferrer():
    IMLOperatorTypeInferrer = win32more.AI.MachineLearning.WinML.IMLOperatorTypeInferrer_head
    IMLOperatorTypeInferrer.InferOutputTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.AI.MachineLearning.WinML.IMLOperatorTypeInferenceContext_head, use_last_error=False)(3, 'InferOutputTypes', ((1, 'context'),)))
    return IMLOperatorTypeInferrer
def _define_IMLOperatorShapeInferrer_head():
    class IMLOperatorShapeInferrer(win32more.System.Com.IUnknown_head):
        Guid = Guid('540be5be-a6c9-40ee-83f6-d2b8b40a7798')
    return IMLOperatorShapeInferrer
def _define_IMLOperatorShapeInferrer():
    IMLOperatorShapeInferrer = win32more.AI.MachineLearning.WinML.IMLOperatorShapeInferrer_head
    IMLOperatorShapeInferrer.InferOutputShapes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.AI.MachineLearning.WinML.IMLOperatorShapeInferenceContext_head, use_last_error=False)(3, 'InferOutputShapes', ((1, 'context'),)))
    return IMLOperatorShapeInferrer
def _define_MLOperatorAttribute_head():
    class MLOperatorAttribute(Structure):
        pass
    return MLOperatorAttribute
def _define_MLOperatorAttribute():
    MLOperatorAttribute = win32more.AI.MachineLearning.WinML.MLOperatorAttribute_head
    MLOperatorAttribute._fields_ = [
        ("name", win32more.Foundation.PSTR),
        ("type", win32more.AI.MachineLearning.WinML.MLOperatorAttributeType),
        ("required", Boolean),
    ]
    return MLOperatorAttribute
def _define_MLOperatorAttributeNameValue_head():
    class MLOperatorAttributeNameValue(Structure):
        pass
    return MLOperatorAttributeNameValue
def _define_MLOperatorAttributeNameValue():
    MLOperatorAttributeNameValue = win32more.AI.MachineLearning.WinML.MLOperatorAttributeNameValue_head
    class MLOperatorAttributeNameValue__Anonymous_e__Union(Union):
        pass
    MLOperatorAttributeNameValue__Anonymous_e__Union._fields_ = [
        ("reserved", c_void_p),
        ("ints", POINTER(Int64)),
        ("strings", POINTER(POINTER(SByte))),
        ("floats", POINTER(Single)),
    ]
    MLOperatorAttributeNameValue._anonymous_ = [
        'Anonymous',
    ]
    MLOperatorAttributeNameValue._fields_ = [
        ("name", win32more.Foundation.PSTR),
        ("type", win32more.AI.MachineLearning.WinML.MLOperatorAttributeType),
        ("valueCount", UInt32),
        ("Anonymous", MLOperatorAttributeNameValue__Anonymous_e__Union),
    ]
    return MLOperatorAttributeNameValue
def _define_MLOperatorSchemaDescription_head():
    class MLOperatorSchemaDescription(Structure):
        pass
    return MLOperatorSchemaDescription
def _define_MLOperatorSchemaDescription():
    MLOperatorSchemaDescription = win32more.AI.MachineLearning.WinML.MLOperatorSchemaDescription_head
    MLOperatorSchemaDescription._fields_ = [
        ("name", win32more.Foundation.PSTR),
        ("operatorSetVersionAtLastChange", Int32),
        ("inputs", POINTER(win32more.AI.MachineLearning.WinML.MLOperatorSchemaEdgeDescription_head)),
        ("inputCount", UInt32),
        ("outputs", POINTER(win32more.AI.MachineLearning.WinML.MLOperatorSchemaEdgeDescription_head)),
        ("outputCount", UInt32),
        ("typeConstraints", POINTER(win32more.AI.MachineLearning.WinML.MLOperatorEdgeTypeConstraint_head)),
        ("typeConstraintCount", UInt32),
        ("attributes", POINTER(win32more.AI.MachineLearning.WinML.MLOperatorAttribute_head)),
        ("attributeCount", UInt32),
        ("defaultAttributes", POINTER(win32more.AI.MachineLearning.WinML.MLOperatorAttributeNameValue_head)),
        ("defaultAttributeCount", UInt32),
    ]
    return MLOperatorSchemaDescription
def _define_MLOperatorSetId_head():
    class MLOperatorSetId(Structure):
        pass
    return MLOperatorSetId
def _define_MLOperatorSetId():
    MLOperatorSetId = win32more.AI.MachineLearning.WinML.MLOperatorSetId_head
    MLOperatorSetId._fields_ = [
        ("domain", win32more.Foundation.PSTR),
        ("version", Int32),
    ]
    return MLOperatorSetId
MLOperatorKernelOptions = UInt32
MLOperatorKernelOptions_None = 0
MLOperatorKernelOptions_AllowDynamicInputShapes = 1
MLOperatorExecutionType = UInt32
MLOperatorExecutionType_Undefined = 0
MLOperatorExecutionType_Cpu = 1
MLOperatorExecutionType_D3D12 = 2
def _define_MLOperatorKernelDescription_head():
    class MLOperatorKernelDescription(Structure):
        pass
    return MLOperatorKernelDescription
def _define_MLOperatorKernelDescription():
    MLOperatorKernelDescription = win32more.AI.MachineLearning.WinML.MLOperatorKernelDescription_head
    MLOperatorKernelDescription._fields_ = [
        ("domain", win32more.Foundation.PSTR),
        ("name", win32more.Foundation.PSTR),
        ("minimumOperatorSetVersion", Int32),
        ("executionType", win32more.AI.MachineLearning.WinML.MLOperatorExecutionType),
        ("typeConstraints", POINTER(win32more.AI.MachineLearning.WinML.MLOperatorEdgeTypeConstraint_head)),
        ("typeConstraintCount", UInt32),
        ("defaultAttributes", POINTER(win32more.AI.MachineLearning.WinML.MLOperatorAttributeNameValue_head)),
        ("defaultAttributeCount", UInt32),
        ("options", win32more.AI.MachineLearning.WinML.MLOperatorKernelOptions),
        ("executionOptions", UInt32),
    ]
    return MLOperatorKernelDescription
def _define_IMLOperatorKernelFactory_head():
    class IMLOperatorKernelFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('ef15ad6f-0dc9-4908-ab35-a575a30dfbf8')
    return IMLOperatorKernelFactory
def _define_IMLOperatorKernelFactory():
    IMLOperatorKernelFactory = win32more.AI.MachineLearning.WinML.IMLOperatorKernelFactory_head
    IMLOperatorKernelFactory.CreateKernel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.AI.MachineLearning.WinML.IMLOperatorKernelCreationContext_head,POINTER(win32more.AI.MachineLearning.WinML.IMLOperatorKernel_head), use_last_error=False)(3, 'CreateKernel', ((1, 'context'),(1, 'kernel'),)))
    return IMLOperatorKernelFactory
def _define_IMLOperatorRegistry_head():
    class IMLOperatorRegistry(win32more.System.Com.IUnknown_head):
        Guid = Guid('2af9dd2d-b516-4672-9ab5-530c208493ad')
    return IMLOperatorRegistry
def _define_IMLOperatorRegistry():
    IMLOperatorRegistry = win32more.AI.MachineLearning.WinML.IMLOperatorRegistry_head
    IMLOperatorRegistry.RegisterOperatorSetSchema = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.AI.MachineLearning.WinML.MLOperatorSetId_head),Int32,POINTER(POINTER(win32more.AI.MachineLearning.WinML.MLOperatorSchemaDescription_head)),UInt32,win32more.AI.MachineLearning.WinML.IMLOperatorTypeInferrer_head,win32more.AI.MachineLearning.WinML.IMLOperatorShapeInferrer_head, use_last_error=False)(3, 'RegisterOperatorSetSchema', ((1, 'operatorSetId'),(1, 'baselineVersion'),(1, 'schema'),(1, 'schemaCount'),(1, 'typeInferrer'),(1, 'shapeInferrer'),)))
    IMLOperatorRegistry.RegisterOperatorKernel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.AI.MachineLearning.WinML.MLOperatorKernelDescription_head),win32more.AI.MachineLearning.WinML.IMLOperatorKernelFactory_head,win32more.AI.MachineLearning.WinML.IMLOperatorShapeInferrer_head, use_last_error=False)(4, 'RegisterOperatorKernel', ((1, 'operatorKernel'),(1, 'operatorKernelFactory'),(1, 'shapeInferrer'),)))
    return IMLOperatorRegistry
def _define_WinMLCreateRuntime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.AI.MachineLearning.WinML.IWinMLRuntime_head), use_last_error=False)(("WinMLCreateRuntime", windll["winml"]), ((1, 'runtime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MLCreateOperatorRegistry():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.AI.MachineLearning.WinML.IMLOperatorRegistry_head), use_last_error=False)(("MLCreateOperatorRegistry", windll["windows.ai.machinelearning"]), ((1, 'registry'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "WINML_TENSOR_DIMENSION_COUNT_MAX",
    "WINML_TENSOR_DATA_TYPE",
    "WINML_TENSOR_UNDEFINED",
    "WINML_TENSOR_FLOAT",
    "WINML_TENSOR_UINT8",
    "WINML_TENSOR_INT8",
    "WINML_TENSOR_UINT16",
    "WINML_TENSOR_INT16",
    "WINML_TENSOR_INT32",
    "WINML_TENSOR_INT64",
    "WINML_TENSOR_STRING",
    "WINML_TENSOR_BOOLEAN",
    "WINML_TENSOR_FLOAT16",
    "WINML_TENSOR_DOUBLE",
    "WINML_TENSOR_UINT32",
    "WINML_TENSOR_UINT64",
    "WINML_TENSOR_COMPLEX64",
    "WINML_TENSOR_COMPLEX128",
    "WINML_FEATURE_TYPE",
    "WINML_FEATURE_UNDEFINED",
    "WINML_FEATURE_TENSOR",
    "WINML_FEATURE_SEQUENCE",
    "WINML_FEATURE_MAP",
    "WINML_FEATURE_IMAGE",
    "WINML_BINDING_TYPE",
    "WINML_BINDING_UNDEFINED",
    "WINML_BINDING_TENSOR",
    "WINML_BINDING_SEQUENCE",
    "WINML_BINDING_MAP",
    "WINML_BINDING_IMAGE",
    "WINML_BINDING_RESOURCE",
    "WINML_TENSOR_BINDING_DESC",
    "WINML_SEQUENCE_BINDING_DESC",
    "WINML_MAP_BINDING_DESC",
    "WINML_IMAGE_BINDING_DESC",
    "WINML_RESOURCE_BINDING_DESC",
    "WINML_BINDING_DESC",
    "WINML_TENSOR_VARIABLE_DESC",
    "WINML_SEQUENCE_VARIABLE_DESC",
    "WINML_MAP_VARIABLE_DESC",
    "WINML_IMAGE_VARIABLE_DESC",
    "WINML_VARIABLE_DESC",
    "WINML_MODEL_DESC",
    "IWinMLModel",
    "IWinMLEvaluationContext",
    "IWinMLRuntime",
    "WINML_RUNTIME_TYPE",
    "WINML_RUNTIME_CNTK",
    "IWinMLRuntimeFactory",
    "MLOperatorAttributeType",
    "MLOperatorAttributeType_Undefined",
    "MLOperatorAttributeType_Float",
    "MLOperatorAttributeType_Int",
    "MLOperatorAttributeType_String",
    "MLOperatorAttributeType_FloatArray",
    "MLOperatorAttributeType_IntArray",
    "MLOperatorAttributeType_StringArray",
    "MLOperatorTensorDataType",
    "MLOperatorTensorDataType_Undefined",
    "MLOperatorTensorDataType_Float",
    "MLOperatorTensorDataType_UInt8",
    "MLOperatorTensorDataType_Int8",
    "MLOperatorTensorDataType_UInt16",
    "MLOperatorTensorDataType_Int16",
    "MLOperatorTensorDataType_Int32",
    "MLOperatorTensorDataType_Int64",
    "MLOperatorTensorDataType_String",
    "MLOperatorTensorDataType_Bool",
    "MLOperatorTensorDataType_Float16",
    "MLOperatorTensorDataType_Double",
    "MLOperatorTensorDataType_UInt32",
    "MLOperatorTensorDataType_UInt64",
    "MLOperatorTensorDataType_Complex64",
    "MLOperatorTensorDataType_Complex128",
    "MLOperatorEdgeType",
    "MLOperatorEdgeType_Undefined",
    "MLOperatorEdgeType_Tensor",
    "MLOperatorEdgeDescription",
    "IMLOperatorAttributes",
    "IMLOperatorTensorShapeDescription",
    "IMLOperatorKernelCreationContext",
    "IMLOperatorTensor",
    "IMLOperatorKernelContext",
    "IMLOperatorKernel",
    "MLOperatorParameterOptions",
    "MLOperatorParameterOptions_Single",
    "MLOperatorParameterOptions_Optional",
    "MLOperatorParameterOptions_Variadic",
    "MLOperatorSchemaEdgeTypeFormat",
    "MLOperatorSchemaEdgeTypeFormat_EdgeDescription",
    "MLOperatorSchemaEdgeTypeFormat_Label",
    "MLOperatorSchemaEdgeDescription",
    "MLOperatorEdgeTypeConstraint",
    "IMLOperatorShapeInferenceContext",
    "IMLOperatorTypeInferenceContext",
    "IMLOperatorTypeInferrer",
    "IMLOperatorShapeInferrer",
    "MLOperatorAttribute",
    "MLOperatorAttributeNameValue",
    "MLOperatorSchemaDescription",
    "MLOperatorSetId",
    "MLOperatorKernelOptions",
    "MLOperatorKernelOptions_None",
    "MLOperatorKernelOptions_AllowDynamicInputShapes",
    "MLOperatorExecutionType",
    "MLOperatorExecutionType_Undefined",
    "MLOperatorExecutionType_Cpu",
    "MLOperatorExecutionType_D3D12",
    "MLOperatorKernelDescription",
    "IMLOperatorKernelFactory",
    "IMLOperatorRegistry",
    "WinMLCreateRuntime",
    "MLCreateOperatorRegistry",
]
