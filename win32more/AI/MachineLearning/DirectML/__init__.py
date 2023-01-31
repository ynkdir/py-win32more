from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.AI.MachineLearning.DirectML
import win32more.Foundation
import win32more.Graphics.Direct3D12
import win32more.System.Com
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
DML_TARGET_VERSION: UInt32 = 16384
DML_TENSOR_DIMENSION_COUNT_MAX: UInt32 = 5
DML_TENSOR_DIMENSION_COUNT_MAX1: UInt32 = 8
DML_TEMPORARY_BUFFER_ALIGNMENT: UInt32 = 256
DML_PERSISTENT_BUFFER_ALIGNMENT: UInt32 = 256
DML_MINIMUM_BUFFER_TENSOR_ALIGNMENT: UInt32 = 16
@winfunctype('DirectML.dll')
def DMLCreateDevice(d3d12Device: win32more.Graphics.Direct3D12.ID3D12Device_head, flags: win32more.AI.MachineLearning.DirectML.DML_CREATE_DEVICE_FLAGS, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('DirectML.dll')
def DMLCreateDevice1(d3d12Device: win32more.Graphics.Direct3D12.ID3D12Device_head, flags: win32more.AI.MachineLearning.DirectML.DML_CREATE_DEVICE_FLAGS, minimumFeatureLevel: win32more.AI.MachineLearning.DirectML.DML_FEATURE_LEVEL, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class DML_ACTIVATION_CELU_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Alpha: Single
class DML_ACTIVATION_ELU_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Alpha: Single
class DML_ACTIVATION_HARDMAX_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ACTIVATION_HARD_SIGMOID_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Alpha: Single
    Beta: Single
class DML_ACTIVATION_IDENTITY_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ACTIVATION_LEAKY_RELU_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Alpha: Single
class DML_ACTIVATION_LINEAR_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Alpha: Single
    Beta: Single
class DML_ACTIVATION_LOG_SOFTMAX_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ACTIVATION_PARAMETERIZED_RELU_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    SlopeTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ACTIVATION_PARAMETRIC_SOFTPLUS_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Alpha: Single
    Beta: Single
class DML_ACTIVATION_RELU_GRAD_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    InputGradientTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputGradientTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ACTIVATION_RELU_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ACTIVATION_SCALED_ELU_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Alpha: Single
    Gamma: Single
class DML_ACTIVATION_SCALED_TANH_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Alpha: Single
    Beta: Single
class DML_ACTIVATION_SHRINK_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Bias: Single
    Threshold: Single
class DML_ACTIVATION_SIGMOID_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ACTIVATION_SOFTMAX_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ACTIVATION_SOFTPLUS_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Steepness: Single
class DML_ACTIVATION_SOFTSIGN_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ACTIVATION_TANH_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ACTIVATION_THRESHOLDED_RELU_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Alpha: Single
class DML_ADAM_OPTIMIZER_OPERATOR_DESC(Structure):
    InputParametersTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    InputFirstMomentTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    InputSecondMomentTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    GradientTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    TrainingStepTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputParametersTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputFirstMomentTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputSecondMomentTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    LearningRate: Single
    Beta1: Single
    Beta2: Single
    Epsilon: Single
class DML_ARGMAX_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    AxisCount: UInt32
    Axes: POINTER(UInt32)
    AxisDirection: win32more.AI.MachineLearning.DirectML.DML_AXIS_DIRECTION
class DML_ARGMIN_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    AxisCount: UInt32
    Axes: POINTER(UInt32)
    AxisDirection: win32more.AI.MachineLearning.DirectML.DML_AXIS_DIRECTION
class DML_AVERAGE_POOLING_GRAD_OPERATOR_DESC(Structure):
    InputGradientTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputGradientTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    DimensionCount: UInt32
    Strides: POINTER(UInt32)
    WindowSize: POINTER(UInt32)
    StartPadding: POINTER(UInt32)
    EndPadding: POINTER(UInt32)
    IncludePadding: win32more.Foundation.BOOL
class DML_AVERAGE_POOLING_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    DimensionCount: UInt32
    Strides: POINTER(UInt32)
    WindowSize: POINTER(UInt32)
    StartPadding: POINTER(UInt32)
    EndPadding: POINTER(UInt32)
    IncludePadding: win32more.Foundation.BOOL
DML_AXIS_DIRECTION = Int32
DML_AXIS_DIRECTION_INCREASING: DML_AXIS_DIRECTION = 0
DML_AXIS_DIRECTION_DECREASING: DML_AXIS_DIRECTION = 1
class DML_BATCH_NORMALIZATION_GRAD_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    InputGradientTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    MeanTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    VarianceTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputGradientTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputScaleGradientTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputBiasGradientTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Epsilon: Single
class DML_BATCH_NORMALIZATION_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    MeanTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    VarianceTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BiasTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Spatial: win32more.Foundation.BOOL
    Epsilon: Single
    FusedActivation: POINTER(win32more.AI.MachineLearning.DirectML.DML_OPERATOR_DESC_head)
class DML_BINDING_DESC(Structure):
    Type: win32more.AI.MachineLearning.DirectML.DML_BINDING_TYPE
    Desc: c_void_p
class DML_BINDING_PROPERTIES(Structure):
    RequiredDescriptorCount: UInt32
    TemporaryResourceSize: UInt64
    PersistentResourceSize: UInt64
class DML_BINDING_TABLE_DESC(Structure):
    Dispatchable: win32more.AI.MachineLearning.DirectML.IDMLDispatchable_head
    CPUDescriptorHandle: win32more.Graphics.Direct3D12.D3D12_CPU_DESCRIPTOR_HANDLE
    GPUDescriptorHandle: win32more.Graphics.Direct3D12.D3D12_GPU_DESCRIPTOR_HANDLE
    SizeInDescriptors: UInt32
DML_BINDING_TYPE = Int32
DML_BINDING_TYPE_NONE: DML_BINDING_TYPE = 0
DML_BINDING_TYPE_BUFFER: DML_BINDING_TYPE = 1
DML_BINDING_TYPE_BUFFER_ARRAY: DML_BINDING_TYPE = 2
class DML_BUFFER_ARRAY_BINDING(Structure):
    BindingCount: UInt32
    Bindings: POINTER(win32more.AI.MachineLearning.DirectML.DML_BUFFER_BINDING_head)
class DML_BUFFER_BINDING(Structure):
    Buffer: win32more.Graphics.Direct3D12.ID3D12Resource_head
    Offset: UInt64
    SizeInBytes: UInt64
class DML_BUFFER_TENSOR_DESC(Structure):
    DataType: win32more.AI.MachineLearning.DirectML.DML_TENSOR_DATA_TYPE
    Flags: win32more.AI.MachineLearning.DirectML.DML_TENSOR_FLAGS
    DimensionCount: UInt32
    Sizes: POINTER(UInt32)
    Strides: POINTER(UInt32)
    TotalTensorSizeInBytes: UInt64
    GuaranteedBaseOffsetAlignment: UInt32
class DML_CAST_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
DML_CONVOLUTION_DIRECTION = Int32
DML_CONVOLUTION_DIRECTION_FORWARD: DML_CONVOLUTION_DIRECTION = 0
DML_CONVOLUTION_DIRECTION_BACKWARD: DML_CONVOLUTION_DIRECTION = 1
class DML_CONVOLUTION_INTEGER_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    InputZeroPointTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    FilterTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    FilterZeroPointTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    DimensionCount: UInt32
    Strides: POINTER(UInt32)
    Dilations: POINTER(UInt32)
    StartPadding: POINTER(UInt32)
    EndPadding: POINTER(UInt32)
    GroupCount: UInt32
DML_CONVOLUTION_MODE = Int32
DML_CONVOLUTION_MODE_CONVOLUTION: DML_CONVOLUTION_MODE = 0
DML_CONVOLUTION_MODE_CROSS_CORRELATION: DML_CONVOLUTION_MODE = 1
class DML_CONVOLUTION_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    FilterTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BiasTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Mode: win32more.AI.MachineLearning.DirectML.DML_CONVOLUTION_MODE
    Direction: win32more.AI.MachineLearning.DirectML.DML_CONVOLUTION_DIRECTION
    DimensionCount: UInt32
    Strides: POINTER(UInt32)
    Dilations: POINTER(UInt32)
    StartPadding: POINTER(UInt32)
    EndPadding: POINTER(UInt32)
    OutputPadding: POINTER(UInt32)
    GroupCount: UInt32
    FusedActivation: POINTER(win32more.AI.MachineLearning.DirectML.DML_OPERATOR_DESC_head)
DML_CREATE_DEVICE_FLAGS = UInt32
DML_CREATE_DEVICE_FLAG_NONE: DML_CREATE_DEVICE_FLAGS = 0
DML_CREATE_DEVICE_FLAG_DEBUG: DML_CREATE_DEVICE_FLAGS = 1
class DML_CUMULATIVE_PRODUCT_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Axis: UInt32
    AxisDirection: win32more.AI.MachineLearning.DirectML.DML_AXIS_DIRECTION
    HasExclusiveProduct: win32more.Foundation.BOOL
class DML_CUMULATIVE_SUMMATION_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Axis: UInt32
    AxisDirection: win32more.AI.MachineLearning.DirectML.DML_AXIS_DIRECTION
    HasExclusiveSum: win32more.Foundation.BOOL
DML_DEPTH_SPACE_ORDER = Int32
DML_DEPTH_SPACE_ORDER_DEPTH_COLUMN_ROW: DML_DEPTH_SPACE_ORDER = 0
DML_DEPTH_SPACE_ORDER_COLUMN_ROW_DEPTH: DML_DEPTH_SPACE_ORDER = 1
class DML_DEPTH_TO_SPACE1_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BlockSize: UInt32
    Order: win32more.AI.MachineLearning.DirectML.DML_DEPTH_SPACE_ORDER
class DML_DEPTH_TO_SPACE_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BlockSize: UInt32
class DML_DIAGONAL_MATRIX_OPERATOR_DESC(Structure):
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Offset: Int32
    Value: Single
class DML_DYNAMIC_QUANTIZE_LINEAR_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputScaleTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputZeroPointTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_ABS_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleBias: POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)
class DML_ELEMENT_WISE_ACOSH_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleBias: POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)
class DML_ELEMENT_WISE_ACOS_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleBias: POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)
class DML_ELEMENT_WISE_ADD1_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    FusedActivation: POINTER(win32more.AI.MachineLearning.DirectML.DML_OPERATOR_DESC_head)
class DML_ELEMENT_WISE_ADD_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_ASINH_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleBias: POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)
class DML_ELEMENT_WISE_ASIN_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleBias: POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)
class DML_ELEMENT_WISE_ATANH_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleBias: POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)
class DML_ELEMENT_WISE_ATAN_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleBias: POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)
class DML_ELEMENT_WISE_ATAN_YX_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_BIT_AND_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_BIT_COUNT_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_BIT_NOT_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_BIT_OR_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_BIT_SHIFT_LEFT_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_BIT_SHIFT_RIGHT_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_BIT_XOR_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_CEIL_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleBias: POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)
class DML_ELEMENT_WISE_CLIP_GRAD_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    InputGradientTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputGradientTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Min: Single
    Max: Single
class DML_ELEMENT_WISE_CLIP_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleBias: POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)
    Min: Single
    Max: Single
class DML_ELEMENT_WISE_CONSTANT_POW_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleBias: POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)
    Exponent: Single
class DML_ELEMENT_WISE_COSH_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleBias: POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)
class DML_ELEMENT_WISE_COS_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleBias: POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)
class DML_ELEMENT_WISE_DEQUANTIZE_LINEAR_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ZeroPointTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_DIFFERENCE_SQUARE_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_DIVIDE_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_ERF_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleBias: POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)
class DML_ELEMENT_WISE_EXP_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleBias: POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)
class DML_ELEMENT_WISE_FLOOR_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleBias: POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)
class DML_ELEMENT_WISE_IDENTITY_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleBias: POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)
class DML_ELEMENT_WISE_IF_OPERATOR_DESC(Structure):
    ConditionTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_IS_INFINITY_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    InfinityMode: win32more.AI.MachineLearning.DirectML.DML_IS_INFINITY_MODE
class DML_ELEMENT_WISE_IS_NAN_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_LOGICAL_AND_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_LOGICAL_EQUALS_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_LOGICAL_GREATER_THAN_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_LOGICAL_GREATER_THAN_OR_EQUAL_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_LOGICAL_LESS_THAN_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_LOGICAL_LESS_THAN_OR_EQUAL_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_LOGICAL_NOT_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_LOGICAL_OR_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_LOGICAL_XOR_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_LOG_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleBias: POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)
class DML_ELEMENT_WISE_MAX_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_MEAN_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_MIN_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_MODULUS_FLOOR_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_MODULUS_TRUNCATE_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_MULTIPLY_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_POW_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ExponentTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleBias: POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)
class DML_ELEMENT_WISE_QUANTIZED_LINEAR_ADD_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    AScaleTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    AZeroPointTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BScaleTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BZeroPointTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputScaleTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputZeroPointTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_QUANTIZE_LINEAR_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ZeroPointTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_RECIP_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleBias: POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)
class DML_ELEMENT_WISE_ROUND_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    RoundingMode: win32more.AI.MachineLearning.DirectML.DML_ROUNDING_MODE
class DML_ELEMENT_WISE_SIGN_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_SINH_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleBias: POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)
class DML_ELEMENT_WISE_SIN_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleBias: POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)
class DML_ELEMENT_WISE_SQRT_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleBias: POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)
class DML_ELEMENT_WISE_SUBTRACT_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ELEMENT_WISE_TANH_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleBias: POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)
class DML_ELEMENT_WISE_TAN_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleBias: POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)
class DML_ELEMENT_WISE_THRESHOLD_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleBias: POINTER(win32more.AI.MachineLearning.DirectML.DML_SCALE_BIAS_head)
    Min: Single
DML_EXECUTION_FLAGS = UInt32
DML_EXECUTION_FLAG_NONE: DML_EXECUTION_FLAGS = 0
DML_EXECUTION_FLAG_ALLOW_HALF_PRECISION_COMPUTATION: DML_EXECUTION_FLAGS = 1
DML_EXECUTION_FLAG_DISABLE_META_COMMANDS: DML_EXECUTION_FLAGS = 2
DML_EXECUTION_FLAG_DESCRIPTORS_VOLATILE: DML_EXECUTION_FLAGS = 4
DML_FEATURE = Int32
DML_FEATURE_TENSOR_DATA_TYPE_SUPPORT: DML_FEATURE = 0
DML_FEATURE_FEATURE_LEVELS: DML_FEATURE = 1
class DML_FEATURE_DATA_FEATURE_LEVELS(Structure):
    MaxSupportedFeatureLevel: win32more.AI.MachineLearning.DirectML.DML_FEATURE_LEVEL
class DML_FEATURE_DATA_TENSOR_DATA_TYPE_SUPPORT(Structure):
    IsSupported: win32more.Foundation.BOOL
DML_FEATURE_LEVEL = Int32
DML_FEATURE_LEVEL_1_0: DML_FEATURE_LEVEL = 4096
DML_FEATURE_LEVEL_2_0: DML_FEATURE_LEVEL = 8192
DML_FEATURE_LEVEL_2_1: DML_FEATURE_LEVEL = 8448
DML_FEATURE_LEVEL_3_0: DML_FEATURE_LEVEL = 12288
DML_FEATURE_LEVEL_3_1: DML_FEATURE_LEVEL = 12544
DML_FEATURE_LEVEL_4_0: DML_FEATURE_LEVEL = 16384
class DML_FEATURE_QUERY_FEATURE_LEVELS(Structure):
    RequestedFeatureLevelCount: UInt32
    RequestedFeatureLevels: POINTER(win32more.AI.MachineLearning.DirectML.DML_FEATURE_LEVEL)
class DML_FEATURE_QUERY_TENSOR_DATA_TYPE_SUPPORT(Structure):
    DataType: win32more.AI.MachineLearning.DirectML.DML_TENSOR_DATA_TYPE
class DML_FILL_VALUE_CONSTANT_OPERATOR_DESC(Structure):
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ValueDataType: win32more.AI.MachineLearning.DirectML.DML_TENSOR_DATA_TYPE
    Value: win32more.AI.MachineLearning.DirectML.DML_SCALAR_UNION
class DML_FILL_VALUE_SEQUENCE_OPERATOR_DESC(Structure):
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ValueDataType: win32more.AI.MachineLearning.DirectML.DML_TENSOR_DATA_TYPE
    ValueStart: win32more.AI.MachineLearning.DirectML.DML_SCALAR_UNION
    ValueDelta: win32more.AI.MachineLearning.DirectML.DML_SCALAR_UNION
class DML_GATHER_ELEMENTS_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    IndicesTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Axis: UInt32
class DML_GATHER_ND1_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    IndicesTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    InputDimensionCount: UInt32
    IndicesDimensionCount: UInt32
    BatchDimensionCount: UInt32
class DML_GATHER_ND_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    IndicesTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    InputDimensionCount: UInt32
    IndicesDimensionCount: UInt32
class DML_GATHER_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    IndicesTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Axis: UInt32
    IndexDimensions: UInt32
class DML_GEMM_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    CTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    TransA: win32more.AI.MachineLearning.DirectML.DML_MATRIX_TRANSFORM
    TransB: win32more.AI.MachineLearning.DirectML.DML_MATRIX_TRANSFORM
    Alpha: Single
    Beta: Single
    FusedActivation: POINTER(win32more.AI.MachineLearning.DirectML.DML_OPERATOR_DESC_head)
class DML_GRAPH_DESC(Structure):
    InputCount: UInt32
    OutputCount: UInt32
    NodeCount: UInt32
    Nodes: POINTER(win32more.AI.MachineLearning.DirectML.DML_GRAPH_NODE_DESC_head)
    InputEdgeCount: UInt32
    InputEdges: POINTER(win32more.AI.MachineLearning.DirectML.DML_GRAPH_EDGE_DESC_head)
    OutputEdgeCount: UInt32
    OutputEdges: POINTER(win32more.AI.MachineLearning.DirectML.DML_GRAPH_EDGE_DESC_head)
    IntermediateEdgeCount: UInt32
    IntermediateEdges: POINTER(win32more.AI.MachineLearning.DirectML.DML_GRAPH_EDGE_DESC_head)
class DML_GRAPH_EDGE_DESC(Structure):
    Type: win32more.AI.MachineLearning.DirectML.DML_GRAPH_EDGE_TYPE
    Desc: c_void_p
DML_GRAPH_EDGE_TYPE = Int32
DML_GRAPH_EDGE_TYPE_INVALID: DML_GRAPH_EDGE_TYPE = 0
DML_GRAPH_EDGE_TYPE_INPUT: DML_GRAPH_EDGE_TYPE = 1
DML_GRAPH_EDGE_TYPE_OUTPUT: DML_GRAPH_EDGE_TYPE = 2
DML_GRAPH_EDGE_TYPE_INTERMEDIATE: DML_GRAPH_EDGE_TYPE = 3
class DML_GRAPH_NODE_DESC(Structure):
    Type: win32more.AI.MachineLearning.DirectML.DML_GRAPH_NODE_TYPE
    Desc: c_void_p
DML_GRAPH_NODE_TYPE = Int32
DML_GRAPH_NODE_TYPE_INVALID: DML_GRAPH_NODE_TYPE = 0
DML_GRAPH_NODE_TYPE_OPERATOR: DML_GRAPH_NODE_TYPE = 1
class DML_GRU_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    WeightTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    RecurrenceTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BiasTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    HiddenInitTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    SequenceLengthsTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputSequenceTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputSingleTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ActivationDescCount: UInt32
    ActivationDescs: POINTER(win32more.AI.MachineLearning.DirectML.DML_OPERATOR_DESC_head)
    Direction: win32more.AI.MachineLearning.DirectML.DML_RECURRENT_NETWORK_DIRECTION
    LinearBeforeReset: win32more.Foundation.BOOL
class DML_INPUT_GRAPH_EDGE_DESC(Structure):
    GraphInputIndex: UInt32
    ToNodeIndex: UInt32
    ToNodeInputIndex: UInt32
    Name: win32more.Foundation.PSTR
class DML_INTERMEDIATE_GRAPH_EDGE_DESC(Structure):
    FromNodeIndex: UInt32
    FromNodeOutputIndex: UInt32
    ToNodeIndex: UInt32
    ToNodeInputIndex: UInt32
    Name: win32more.Foundation.PSTR
DML_INTERPOLATION_MODE = Int32
DML_INTERPOLATION_MODE_NEAREST_NEIGHBOR: DML_INTERPOLATION_MODE = 0
DML_INTERPOLATION_MODE_LINEAR: DML_INTERPOLATION_MODE = 1
DML_IS_INFINITY_MODE = Int32
DML_IS_INFINITY_MODE_EITHER: DML_IS_INFINITY_MODE = 0
DML_IS_INFINITY_MODE_POSITIVE: DML_IS_INFINITY_MODE = 1
DML_IS_INFINITY_MODE_NEGATIVE: DML_IS_INFINITY_MODE = 2
class DML_JOIN_OPERATOR_DESC(Structure):
    InputCount: UInt32
    InputTensors: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Axis: UInt32
class DML_LOCAL_RESPONSE_NORMALIZATION_GRAD_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    InputGradientTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputGradientTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    CrossChannel: win32more.Foundation.BOOL
    LocalSize: UInt32
    Alpha: Single
    Beta: Single
    Bias: Single
class DML_LOCAL_RESPONSE_NORMALIZATION_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    CrossChannel: win32more.Foundation.BOOL
    LocalSize: UInt32
    Alpha: Single
    Beta: Single
    Bias: Single
class DML_LP_NORMALIZATION_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Axis: UInt32
    Epsilon: Single
    P: UInt32
class DML_LP_POOLING_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    DimensionCount: UInt32
    Strides: POINTER(UInt32)
    WindowSize: POINTER(UInt32)
    StartPadding: POINTER(UInt32)
    EndPadding: POINTER(UInt32)
    P: UInt32
class DML_LSTM_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    WeightTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    RecurrenceTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BiasTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    HiddenInitTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    CellMemInitTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    SequenceLengthsTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    PeepholeTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputSequenceTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputSingleTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputCellSingleTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ActivationDescCount: UInt32
    ActivationDescs: POINTER(win32more.AI.MachineLearning.DirectML.DML_OPERATOR_DESC_head)
    Direction: win32more.AI.MachineLearning.DirectML.DML_RECURRENT_NETWORK_DIRECTION
    ClipThreshold: Single
    UseClipThreshold: win32more.Foundation.BOOL
    CoupleInputForget: win32more.Foundation.BOOL
class DML_MATRIX_MULTIPLY_INTEGER_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    AZeroPointTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BZeroPointTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
DML_MATRIX_TRANSFORM = Int32
DML_MATRIX_TRANSFORM_NONE: DML_MATRIX_TRANSFORM = 0
DML_MATRIX_TRANSFORM_TRANSPOSE: DML_MATRIX_TRANSFORM = 1
class DML_MAX_POOLING1_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputIndicesTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    DimensionCount: UInt32
    Strides: POINTER(UInt32)
    WindowSize: POINTER(UInt32)
    StartPadding: POINTER(UInt32)
    EndPadding: POINTER(UInt32)
class DML_MAX_POOLING2_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputIndicesTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    DimensionCount: UInt32
    Strides: POINTER(UInt32)
    WindowSize: POINTER(UInt32)
    StartPadding: POINTER(UInt32)
    EndPadding: POINTER(UInt32)
    Dilations: POINTER(UInt32)
class DML_MAX_POOLING_GRAD_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    InputGradientTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputGradientTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    DimensionCount: UInt32
    Strides: POINTER(UInt32)
    WindowSize: POINTER(UInt32)
    StartPadding: POINTER(UInt32)
    EndPadding: POINTER(UInt32)
    Dilations: POINTER(UInt32)
class DML_MAX_POOLING_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    DimensionCount: UInt32
    Strides: POINTER(UInt32)
    WindowSize: POINTER(UInt32)
    StartPadding: POINTER(UInt32)
    EndPadding: POINTER(UInt32)
class DML_MAX_UNPOOLING_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    IndicesTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_MEAN_VARIANCE_NORMALIZATION1_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BiasTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    AxisCount: UInt32
    Axes: POINTER(UInt32)
    NormalizeVariance: win32more.Foundation.BOOL
    Epsilon: Single
    FusedActivation: POINTER(win32more.AI.MachineLearning.DirectML.DML_OPERATOR_DESC_head)
class DML_MEAN_VARIANCE_NORMALIZATION_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BiasTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    CrossChannel: win32more.Foundation.BOOL
    NormalizeVariance: win32more.Foundation.BOOL
    Epsilon: Single
    FusedActivation: POINTER(win32more.AI.MachineLearning.DirectML.DML_OPERATOR_DESC_head)
class DML_NONZERO_COORDINATES_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputCountTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputCoordinatesTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_ONE_HOT_OPERATOR_DESC(Structure):
    IndicesTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ValuesTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Axis: UInt32
class DML_OPERATOR_DESC(Structure):
    Type: win32more.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE
    Desc: c_void_p
class DML_OPERATOR_GRAPH_NODE_DESC(Structure):
    Operator: win32more.AI.MachineLearning.DirectML.IDMLOperator_head
    Name: win32more.Foundation.PSTR
DML_OPERATOR_TYPE = Int32
DML_OPERATOR_INVALID: DML_OPERATOR_TYPE = 0
DML_OPERATOR_ELEMENT_WISE_IDENTITY: DML_OPERATOR_TYPE = 1
DML_OPERATOR_ELEMENT_WISE_ABS: DML_OPERATOR_TYPE = 2
DML_OPERATOR_ELEMENT_WISE_ACOS: DML_OPERATOR_TYPE = 3
DML_OPERATOR_ELEMENT_WISE_ADD: DML_OPERATOR_TYPE = 4
DML_OPERATOR_ELEMENT_WISE_ASIN: DML_OPERATOR_TYPE = 5
DML_OPERATOR_ELEMENT_WISE_ATAN: DML_OPERATOR_TYPE = 6
DML_OPERATOR_ELEMENT_WISE_CEIL: DML_OPERATOR_TYPE = 7
DML_OPERATOR_ELEMENT_WISE_CLIP: DML_OPERATOR_TYPE = 8
DML_OPERATOR_ELEMENT_WISE_COS: DML_OPERATOR_TYPE = 9
DML_OPERATOR_ELEMENT_WISE_DIVIDE: DML_OPERATOR_TYPE = 10
DML_OPERATOR_ELEMENT_WISE_EXP: DML_OPERATOR_TYPE = 11
DML_OPERATOR_ELEMENT_WISE_FLOOR: DML_OPERATOR_TYPE = 12
DML_OPERATOR_ELEMENT_WISE_LOG: DML_OPERATOR_TYPE = 13
DML_OPERATOR_ELEMENT_WISE_LOGICAL_AND: DML_OPERATOR_TYPE = 14
DML_OPERATOR_ELEMENT_WISE_LOGICAL_EQUALS: DML_OPERATOR_TYPE = 15
DML_OPERATOR_ELEMENT_WISE_LOGICAL_GREATER_THAN: DML_OPERATOR_TYPE = 16
DML_OPERATOR_ELEMENT_WISE_LOGICAL_LESS_THAN: DML_OPERATOR_TYPE = 17
DML_OPERATOR_ELEMENT_WISE_LOGICAL_NOT: DML_OPERATOR_TYPE = 18
DML_OPERATOR_ELEMENT_WISE_LOGICAL_OR: DML_OPERATOR_TYPE = 19
DML_OPERATOR_ELEMENT_WISE_LOGICAL_XOR: DML_OPERATOR_TYPE = 20
DML_OPERATOR_ELEMENT_WISE_MAX: DML_OPERATOR_TYPE = 21
DML_OPERATOR_ELEMENT_WISE_MEAN: DML_OPERATOR_TYPE = 22
DML_OPERATOR_ELEMENT_WISE_MIN: DML_OPERATOR_TYPE = 23
DML_OPERATOR_ELEMENT_WISE_MULTIPLY: DML_OPERATOR_TYPE = 24
DML_OPERATOR_ELEMENT_WISE_POW: DML_OPERATOR_TYPE = 25
DML_OPERATOR_ELEMENT_WISE_CONSTANT_POW: DML_OPERATOR_TYPE = 26
DML_OPERATOR_ELEMENT_WISE_RECIP: DML_OPERATOR_TYPE = 27
DML_OPERATOR_ELEMENT_WISE_SIN: DML_OPERATOR_TYPE = 28
DML_OPERATOR_ELEMENT_WISE_SQRT: DML_OPERATOR_TYPE = 29
DML_OPERATOR_ELEMENT_WISE_SUBTRACT: DML_OPERATOR_TYPE = 30
DML_OPERATOR_ELEMENT_WISE_TAN: DML_OPERATOR_TYPE = 31
DML_OPERATOR_ELEMENT_WISE_THRESHOLD: DML_OPERATOR_TYPE = 32
DML_OPERATOR_ELEMENT_WISE_QUANTIZE_LINEAR: DML_OPERATOR_TYPE = 33
DML_OPERATOR_ELEMENT_WISE_DEQUANTIZE_LINEAR: DML_OPERATOR_TYPE = 34
DML_OPERATOR_ACTIVATION_ELU: DML_OPERATOR_TYPE = 35
DML_OPERATOR_ACTIVATION_HARDMAX: DML_OPERATOR_TYPE = 36
DML_OPERATOR_ACTIVATION_HARD_SIGMOID: DML_OPERATOR_TYPE = 37
DML_OPERATOR_ACTIVATION_IDENTITY: DML_OPERATOR_TYPE = 38
DML_OPERATOR_ACTIVATION_LEAKY_RELU: DML_OPERATOR_TYPE = 39
DML_OPERATOR_ACTIVATION_LINEAR: DML_OPERATOR_TYPE = 40
DML_OPERATOR_ACTIVATION_LOG_SOFTMAX: DML_OPERATOR_TYPE = 41
DML_OPERATOR_ACTIVATION_PARAMETERIZED_RELU: DML_OPERATOR_TYPE = 42
DML_OPERATOR_ACTIVATION_PARAMETRIC_SOFTPLUS: DML_OPERATOR_TYPE = 43
DML_OPERATOR_ACTIVATION_RELU: DML_OPERATOR_TYPE = 44
DML_OPERATOR_ACTIVATION_SCALED_ELU: DML_OPERATOR_TYPE = 45
DML_OPERATOR_ACTIVATION_SCALED_TANH: DML_OPERATOR_TYPE = 46
DML_OPERATOR_ACTIVATION_SIGMOID: DML_OPERATOR_TYPE = 47
DML_OPERATOR_ACTIVATION_SOFTMAX: DML_OPERATOR_TYPE = 48
DML_OPERATOR_ACTIVATION_SOFTPLUS: DML_OPERATOR_TYPE = 49
DML_OPERATOR_ACTIVATION_SOFTSIGN: DML_OPERATOR_TYPE = 50
DML_OPERATOR_ACTIVATION_TANH: DML_OPERATOR_TYPE = 51
DML_OPERATOR_ACTIVATION_THRESHOLDED_RELU: DML_OPERATOR_TYPE = 52
DML_OPERATOR_CONVOLUTION: DML_OPERATOR_TYPE = 53
DML_OPERATOR_GEMM: DML_OPERATOR_TYPE = 54
DML_OPERATOR_REDUCE: DML_OPERATOR_TYPE = 55
DML_OPERATOR_AVERAGE_POOLING: DML_OPERATOR_TYPE = 56
DML_OPERATOR_LP_POOLING: DML_OPERATOR_TYPE = 57
DML_OPERATOR_MAX_POOLING: DML_OPERATOR_TYPE = 58
DML_OPERATOR_ROI_POOLING: DML_OPERATOR_TYPE = 59
DML_OPERATOR_SLICE: DML_OPERATOR_TYPE = 60
DML_OPERATOR_CAST: DML_OPERATOR_TYPE = 61
DML_OPERATOR_SPLIT: DML_OPERATOR_TYPE = 62
DML_OPERATOR_JOIN: DML_OPERATOR_TYPE = 63
DML_OPERATOR_PADDING: DML_OPERATOR_TYPE = 64
DML_OPERATOR_VALUE_SCALE_2D: DML_OPERATOR_TYPE = 65
DML_OPERATOR_UPSAMPLE_2D: DML_OPERATOR_TYPE = 66
DML_OPERATOR_GATHER: DML_OPERATOR_TYPE = 67
DML_OPERATOR_SPACE_TO_DEPTH: DML_OPERATOR_TYPE = 68
DML_OPERATOR_DEPTH_TO_SPACE: DML_OPERATOR_TYPE = 69
DML_OPERATOR_TILE: DML_OPERATOR_TYPE = 70
DML_OPERATOR_TOP_K: DML_OPERATOR_TYPE = 71
DML_OPERATOR_BATCH_NORMALIZATION: DML_OPERATOR_TYPE = 72
DML_OPERATOR_MEAN_VARIANCE_NORMALIZATION: DML_OPERATOR_TYPE = 73
DML_OPERATOR_LOCAL_RESPONSE_NORMALIZATION: DML_OPERATOR_TYPE = 74
DML_OPERATOR_LP_NORMALIZATION: DML_OPERATOR_TYPE = 75
DML_OPERATOR_RNN: DML_OPERATOR_TYPE = 76
DML_OPERATOR_LSTM: DML_OPERATOR_TYPE = 77
DML_OPERATOR_GRU: DML_OPERATOR_TYPE = 78
DML_OPERATOR_ELEMENT_WISE_SIGN: DML_OPERATOR_TYPE = 79
DML_OPERATOR_ELEMENT_WISE_IS_NAN: DML_OPERATOR_TYPE = 80
DML_OPERATOR_ELEMENT_WISE_ERF: DML_OPERATOR_TYPE = 81
DML_OPERATOR_ELEMENT_WISE_SINH: DML_OPERATOR_TYPE = 82
DML_OPERATOR_ELEMENT_WISE_COSH: DML_OPERATOR_TYPE = 83
DML_OPERATOR_ELEMENT_WISE_TANH: DML_OPERATOR_TYPE = 84
DML_OPERATOR_ELEMENT_WISE_ASINH: DML_OPERATOR_TYPE = 85
DML_OPERATOR_ELEMENT_WISE_ACOSH: DML_OPERATOR_TYPE = 86
DML_OPERATOR_ELEMENT_WISE_ATANH: DML_OPERATOR_TYPE = 87
DML_OPERATOR_ELEMENT_WISE_IF: DML_OPERATOR_TYPE = 88
DML_OPERATOR_ELEMENT_WISE_ADD1: DML_OPERATOR_TYPE = 89
DML_OPERATOR_ACTIVATION_SHRINK: DML_OPERATOR_TYPE = 90
DML_OPERATOR_MAX_POOLING1: DML_OPERATOR_TYPE = 91
DML_OPERATOR_MAX_UNPOOLING: DML_OPERATOR_TYPE = 92
DML_OPERATOR_DIAGONAL_MATRIX: DML_OPERATOR_TYPE = 93
DML_OPERATOR_SCATTER_ELEMENTS: DML_OPERATOR_TYPE = 94
DML_OPERATOR_SCATTER: DML_OPERATOR_TYPE = 94
DML_OPERATOR_ONE_HOT: DML_OPERATOR_TYPE = 95
DML_OPERATOR_RESAMPLE: DML_OPERATOR_TYPE = 96
DML_OPERATOR_ELEMENT_WISE_BIT_SHIFT_LEFT: DML_OPERATOR_TYPE = 97
DML_OPERATOR_ELEMENT_WISE_BIT_SHIFT_RIGHT: DML_OPERATOR_TYPE = 98
DML_OPERATOR_ELEMENT_WISE_ROUND: DML_OPERATOR_TYPE = 99
DML_OPERATOR_ELEMENT_WISE_IS_INFINITY: DML_OPERATOR_TYPE = 100
DML_OPERATOR_ELEMENT_WISE_MODULUS_TRUNCATE: DML_OPERATOR_TYPE = 101
DML_OPERATOR_ELEMENT_WISE_MODULUS_FLOOR: DML_OPERATOR_TYPE = 102
DML_OPERATOR_FILL_VALUE_CONSTANT: DML_OPERATOR_TYPE = 103
DML_OPERATOR_FILL_VALUE_SEQUENCE: DML_OPERATOR_TYPE = 104
DML_OPERATOR_CUMULATIVE_SUMMATION: DML_OPERATOR_TYPE = 105
DML_OPERATOR_REVERSE_SUBSEQUENCES: DML_OPERATOR_TYPE = 106
DML_OPERATOR_GATHER_ELEMENTS: DML_OPERATOR_TYPE = 107
DML_OPERATOR_GATHER_ND: DML_OPERATOR_TYPE = 108
DML_OPERATOR_SCATTER_ND: DML_OPERATOR_TYPE = 109
DML_OPERATOR_MAX_POOLING2: DML_OPERATOR_TYPE = 110
DML_OPERATOR_SLICE1: DML_OPERATOR_TYPE = 111
DML_OPERATOR_TOP_K1: DML_OPERATOR_TYPE = 112
DML_OPERATOR_DEPTH_TO_SPACE1: DML_OPERATOR_TYPE = 113
DML_OPERATOR_SPACE_TO_DEPTH1: DML_OPERATOR_TYPE = 114
DML_OPERATOR_MEAN_VARIANCE_NORMALIZATION1: DML_OPERATOR_TYPE = 115
DML_OPERATOR_RESAMPLE1: DML_OPERATOR_TYPE = 116
DML_OPERATOR_MATRIX_MULTIPLY_INTEGER: DML_OPERATOR_TYPE = 117
DML_OPERATOR_QUANTIZED_LINEAR_MATRIX_MULTIPLY: DML_OPERATOR_TYPE = 118
DML_OPERATOR_CONVOLUTION_INTEGER: DML_OPERATOR_TYPE = 119
DML_OPERATOR_QUANTIZED_LINEAR_CONVOLUTION: DML_OPERATOR_TYPE = 120
DML_OPERATOR_ELEMENT_WISE_BIT_AND: DML_OPERATOR_TYPE = 121
DML_OPERATOR_ELEMENT_WISE_BIT_OR: DML_OPERATOR_TYPE = 122
DML_OPERATOR_ELEMENT_WISE_BIT_XOR: DML_OPERATOR_TYPE = 123
DML_OPERATOR_ELEMENT_WISE_BIT_NOT: DML_OPERATOR_TYPE = 124
DML_OPERATOR_ELEMENT_WISE_BIT_COUNT: DML_OPERATOR_TYPE = 125
DML_OPERATOR_ELEMENT_WISE_LOGICAL_GREATER_THAN_OR_EQUAL: DML_OPERATOR_TYPE = 126
DML_OPERATOR_ELEMENT_WISE_LOGICAL_LESS_THAN_OR_EQUAL: DML_OPERATOR_TYPE = 127
DML_OPERATOR_ACTIVATION_CELU: DML_OPERATOR_TYPE = 128
DML_OPERATOR_ACTIVATION_RELU_GRAD: DML_OPERATOR_TYPE = 129
DML_OPERATOR_AVERAGE_POOLING_GRAD: DML_OPERATOR_TYPE = 130
DML_OPERATOR_MAX_POOLING_GRAD: DML_OPERATOR_TYPE = 131
DML_OPERATOR_RANDOM_GENERATOR: DML_OPERATOR_TYPE = 132
DML_OPERATOR_NONZERO_COORDINATES: DML_OPERATOR_TYPE = 133
DML_OPERATOR_RESAMPLE_GRAD: DML_OPERATOR_TYPE = 134
DML_OPERATOR_SLICE_GRAD: DML_OPERATOR_TYPE = 135
DML_OPERATOR_ADAM_OPTIMIZER: DML_OPERATOR_TYPE = 136
DML_OPERATOR_ARGMIN: DML_OPERATOR_TYPE = 137
DML_OPERATOR_ARGMAX: DML_OPERATOR_TYPE = 138
DML_OPERATOR_ROI_ALIGN: DML_OPERATOR_TYPE = 139
DML_OPERATOR_GATHER_ND1: DML_OPERATOR_TYPE = 140
DML_OPERATOR_ELEMENT_WISE_ATAN_YX: DML_OPERATOR_TYPE = 141
DML_OPERATOR_ELEMENT_WISE_CLIP_GRAD: DML_OPERATOR_TYPE = 142
DML_OPERATOR_ELEMENT_WISE_DIFFERENCE_SQUARE: DML_OPERATOR_TYPE = 143
DML_OPERATOR_LOCAL_RESPONSE_NORMALIZATION_GRAD: DML_OPERATOR_TYPE = 144
DML_OPERATOR_CUMULATIVE_PRODUCT: DML_OPERATOR_TYPE = 145
DML_OPERATOR_BATCH_NORMALIZATION_GRAD: DML_OPERATOR_TYPE = 146
DML_OPERATOR_ELEMENT_WISE_QUANTIZED_LINEAR_ADD: DML_OPERATOR_TYPE = 147
DML_OPERATOR_DYNAMIC_QUANTIZE_LINEAR: DML_OPERATOR_TYPE = 148
DML_OPERATOR_ROI_ALIGN1: DML_OPERATOR_TYPE = 149
class DML_OUTPUT_GRAPH_EDGE_DESC(Structure):
    FromNodeIndex: UInt32
    FromNodeOutputIndex: UInt32
    GraphOutputIndex: UInt32
    Name: win32more.Foundation.PSTR
DML_PADDING_MODE = Int32
DML_PADDING_MODE_CONSTANT: DML_PADDING_MODE = 0
DML_PADDING_MODE_EDGE: DML_PADDING_MODE = 1
DML_PADDING_MODE_REFLECTION: DML_PADDING_MODE = 2
DML_PADDING_MODE_SYMMETRIC: DML_PADDING_MODE = 3
class DML_PADDING_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    PaddingMode: win32more.AI.MachineLearning.DirectML.DML_PADDING_MODE
    PaddingValue: Single
    DimensionCount: UInt32
    StartPadding: POINTER(UInt32)
    EndPadding: POINTER(UInt32)
class DML_QUANTIZED_LINEAR_CONVOLUTION_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    InputScaleTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    InputZeroPointTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    FilterTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    FilterScaleTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    FilterZeroPointTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BiasTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputScaleTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputZeroPointTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    DimensionCount: UInt32
    Strides: POINTER(UInt32)
    Dilations: POINTER(UInt32)
    StartPadding: POINTER(UInt32)
    EndPadding: POINTER(UInt32)
    GroupCount: UInt32
class DML_QUANTIZED_LINEAR_MATRIX_MULTIPLY_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    AScaleTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    AZeroPointTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BScaleTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BZeroPointTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputScaleTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputZeroPointTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
class DML_RANDOM_GENERATOR_OPERATOR_DESC(Structure):
    InputStateTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputStateTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Type: win32more.AI.MachineLearning.DirectML.DML_RANDOM_GENERATOR_TYPE
DML_RANDOM_GENERATOR_TYPE = Int32
DML_RANDOM_GENERATOR_TYPE_PHILOX_4X32_10: DML_RANDOM_GENERATOR_TYPE = 0
DML_RECURRENT_NETWORK_DIRECTION = Int32
DML_RECURRENT_NETWORK_DIRECTION_FORWARD: DML_RECURRENT_NETWORK_DIRECTION = 0
DML_RECURRENT_NETWORK_DIRECTION_BACKWARD: DML_RECURRENT_NETWORK_DIRECTION = 1
DML_RECURRENT_NETWORK_DIRECTION_BIDIRECTIONAL: DML_RECURRENT_NETWORK_DIRECTION = 2
DML_REDUCE_FUNCTION = Int32
DML_REDUCE_FUNCTION_ARGMAX: DML_REDUCE_FUNCTION = 0
DML_REDUCE_FUNCTION_ARGMIN: DML_REDUCE_FUNCTION = 1
DML_REDUCE_FUNCTION_AVERAGE: DML_REDUCE_FUNCTION = 2
DML_REDUCE_FUNCTION_L1: DML_REDUCE_FUNCTION = 3
DML_REDUCE_FUNCTION_L2: DML_REDUCE_FUNCTION = 4
DML_REDUCE_FUNCTION_LOG_SUM: DML_REDUCE_FUNCTION = 5
DML_REDUCE_FUNCTION_LOG_SUM_EXP: DML_REDUCE_FUNCTION = 6
DML_REDUCE_FUNCTION_MAX: DML_REDUCE_FUNCTION = 7
DML_REDUCE_FUNCTION_MIN: DML_REDUCE_FUNCTION = 8
DML_REDUCE_FUNCTION_MULTIPLY: DML_REDUCE_FUNCTION = 9
DML_REDUCE_FUNCTION_SUM: DML_REDUCE_FUNCTION = 10
DML_REDUCE_FUNCTION_SUM_SQUARE: DML_REDUCE_FUNCTION = 11
class DML_REDUCE_OPERATOR_DESC(Structure):
    Function: win32more.AI.MachineLearning.DirectML.DML_REDUCE_FUNCTION
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    AxisCount: UInt32
    Axes: POINTER(UInt32)
class DML_RESAMPLE1_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    InterpolationMode: win32more.AI.MachineLearning.DirectML.DML_INTERPOLATION_MODE
    DimensionCount: UInt32
    Scales: POINTER(Single)
    InputPixelOffsets: POINTER(Single)
    OutputPixelOffsets: POINTER(Single)
class DML_RESAMPLE_GRAD_OPERATOR_DESC(Structure):
    InputGradientTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputGradientTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    InterpolationMode: win32more.AI.MachineLearning.DirectML.DML_INTERPOLATION_MODE
    DimensionCount: UInt32
    Scales: POINTER(Single)
    InputPixelOffsets: POINTER(Single)
    OutputPixelOffsets: POINTER(Single)
class DML_RESAMPLE_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    InterpolationMode: win32more.AI.MachineLearning.DirectML.DML_INTERPOLATION_MODE
    ScaleCount: UInt32
    Scales: POINTER(Single)
class DML_REVERSE_SUBSEQUENCES_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    SequenceLengthsTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Axis: UInt32
class DML_RNN_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    WeightTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    RecurrenceTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BiasTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    HiddenInitTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    SequenceLengthsTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputSequenceTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputSingleTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ActivationDescCount: UInt32
    ActivationDescs: POINTER(win32more.AI.MachineLearning.DirectML.DML_OPERATOR_DESC_head)
    Direction: win32more.AI.MachineLearning.DirectML.DML_RECURRENT_NETWORK_DIRECTION
class DML_ROI_ALIGN1_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ROITensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BatchIndicesTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ReductionFunction: win32more.AI.MachineLearning.DirectML.DML_REDUCE_FUNCTION
    InterpolationMode: win32more.AI.MachineLearning.DirectML.DML_INTERPOLATION_MODE
    SpatialScaleX: Single
    SpatialScaleY: Single
    InputPixelOffset: Single
    OutputPixelOffset: Single
    OutOfBoundsInputValue: Single
    MinimumSamplesPerOutput: UInt32
    MaximumSamplesPerOutput: UInt32
    AlignRegionsToCorners: win32more.Foundation.BOOL
class DML_ROI_ALIGN_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ROITensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BatchIndicesTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ReductionFunction: win32more.AI.MachineLearning.DirectML.DML_REDUCE_FUNCTION
    InterpolationMode: win32more.AI.MachineLearning.DirectML.DML_INTERPOLATION_MODE
    SpatialScaleX: Single
    SpatialScaleY: Single
    OutOfBoundsInputValue: Single
    MinimumSamplesPerOutput: UInt32
    MaximumSamplesPerOutput: UInt32
class DML_ROI_POOLING_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ROITensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    SpatialScale: Single
    PooledSize: win32more.AI.MachineLearning.DirectML.DML_SIZE_2D
DML_ROUNDING_MODE = Int32
DML_ROUNDING_MODE_HALVES_TO_NEAREST_EVEN: DML_ROUNDING_MODE = 0
DML_ROUNDING_MODE_TOWARD_ZERO: DML_ROUNDING_MODE = 1
DML_ROUNDING_MODE_TOWARD_INFINITY: DML_ROUNDING_MODE = 2
class DML_SCALAR_UNION(Union):
    Bytes: Byte * 8
    Int8: SByte
    UInt8: Byte
    Int16: Int16
    UInt16: UInt16
    Int32: Int32
    UInt32: UInt32
    Int64: Int64
    UInt64: UInt64
    Float32: Single
    Float64: Double
class DML_SCALE_BIAS(Structure):
    Scale: Single
    Bias: Single
class DML_SCATTER_ND_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    IndicesTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    UpdatesTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    InputDimensionCount: UInt32
    IndicesDimensionCount: UInt32
class DML_SCATTER_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    IndicesTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    UpdatesTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Axis: UInt32
class DML_SIZE_2D(Structure):
    Width: UInt32
    Height: UInt32
class DML_SLICE1_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    DimensionCount: UInt32
    InputWindowOffsets: POINTER(UInt32)
    InputWindowSizes: POINTER(UInt32)
    InputWindowStrides: POINTER(Int32)
class DML_SLICE_GRAD_OPERATOR_DESC(Structure):
    InputGradientTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputGradientTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    DimensionCount: UInt32
    InputWindowOffsets: POINTER(UInt32)
    InputWindowSizes: POINTER(UInt32)
    InputWindowStrides: POINTER(Int32)
class DML_SLICE_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    DimensionCount: UInt32
    Offsets: POINTER(UInt32)
    Sizes: POINTER(UInt32)
    Strides: POINTER(UInt32)
class DML_SPACE_TO_DEPTH1_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BlockSize: UInt32
    Order: win32more.AI.MachineLearning.DirectML.DML_DEPTH_SPACE_ORDER
class DML_SPACE_TO_DEPTH_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    BlockSize: UInt32
class DML_SPLIT_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputCount: UInt32
    OutputTensors: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Axis: UInt32
DML_TENSOR_DATA_TYPE = Int32
DML_TENSOR_DATA_TYPE_UNKNOWN: DML_TENSOR_DATA_TYPE = 0
DML_TENSOR_DATA_TYPE_FLOAT32: DML_TENSOR_DATA_TYPE = 1
DML_TENSOR_DATA_TYPE_FLOAT16: DML_TENSOR_DATA_TYPE = 2
DML_TENSOR_DATA_TYPE_UINT32: DML_TENSOR_DATA_TYPE = 3
DML_TENSOR_DATA_TYPE_UINT16: DML_TENSOR_DATA_TYPE = 4
DML_TENSOR_DATA_TYPE_UINT8: DML_TENSOR_DATA_TYPE = 5
DML_TENSOR_DATA_TYPE_INT32: DML_TENSOR_DATA_TYPE = 6
DML_TENSOR_DATA_TYPE_INT16: DML_TENSOR_DATA_TYPE = 7
DML_TENSOR_DATA_TYPE_INT8: DML_TENSOR_DATA_TYPE = 8
DML_TENSOR_DATA_TYPE_FLOAT64: DML_TENSOR_DATA_TYPE = 9
DML_TENSOR_DATA_TYPE_UINT64: DML_TENSOR_DATA_TYPE = 10
DML_TENSOR_DATA_TYPE_INT64: DML_TENSOR_DATA_TYPE = 11
class DML_TENSOR_DESC(Structure):
    Type: win32more.AI.MachineLearning.DirectML.DML_TENSOR_TYPE
    Desc: c_void_p
DML_TENSOR_FLAGS = UInt32
DML_TENSOR_FLAG_NONE: DML_TENSOR_FLAGS = 0
DML_TENSOR_FLAG_OWNED_BY_DML: DML_TENSOR_FLAGS = 1
DML_TENSOR_TYPE = Int32
DML_TENSOR_TYPE_INVALID: DML_TENSOR_TYPE = 0
DML_TENSOR_TYPE_BUFFER: DML_TENSOR_TYPE = 1
class DML_TILE_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    RepeatsCount: UInt32
    Repeats: POINTER(UInt32)
class DML_TOP_K1_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputValueTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputIndexTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Axis: UInt32
    K: UInt32
    AxisDirection: win32more.AI.MachineLearning.DirectML.DML_AXIS_DIRECTION
class DML_TOP_K_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputValueTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputIndexTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Axis: UInt32
    K: UInt32
class DML_UPSAMPLE_2D_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    ScaleSize: win32more.AI.MachineLearning.DirectML.DML_SIZE_2D
    InterpolationMode: win32more.AI.MachineLearning.DirectML.DML_INTERPOLATION_MODE
class DML_VALUE_SCALE_2D_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    OutputTensor: POINTER(win32more.AI.MachineLearning.DirectML.DML_TENSOR_DESC_head)
    Scale: Single
    ChannelCount: UInt32
    Bias: POINTER(Single)
class IDMLBindingTable(c_void_p):
    extends: win32more.AI.MachineLearning.DirectML.IDMLDeviceChild
    Guid = Guid('29c687dc-de74-4e3b-ab-00-11-68-f2-fc-3c-fc')
    @commethod(8)
    def BindInputs(bindingCount: UInt32, bindings: POINTER(win32more.AI.MachineLearning.DirectML.DML_BINDING_DESC_head)) -> Void: ...
    @commethod(9)
    def BindOutputs(bindingCount: UInt32, bindings: POINTER(win32more.AI.MachineLearning.DirectML.DML_BINDING_DESC_head)) -> Void: ...
    @commethod(10)
    def BindTemporaryResource(binding: POINTER(win32more.AI.MachineLearning.DirectML.DML_BINDING_DESC_head)) -> Void: ...
    @commethod(11)
    def BindPersistentResource(binding: POINTER(win32more.AI.MachineLearning.DirectML.DML_BINDING_DESC_head)) -> Void: ...
    @commethod(12)
    def Reset(desc: POINTER(win32more.AI.MachineLearning.DirectML.DML_BINDING_TABLE_DESC_head)) -> win32more.Foundation.HRESULT: ...
class IDMLCommandRecorder(c_void_p):
    extends: win32more.AI.MachineLearning.DirectML.IDMLDeviceChild
    Guid = Guid('e6857a76-2e3e-4fdd-bf-f4-5d-2b-a1-0f-b4-53')
    @commethod(8)
    def RecordDispatch(commandList: win32more.Graphics.Direct3D12.ID3D12CommandList_head, dispatchable: win32more.AI.MachineLearning.DirectML.IDMLDispatchable_head, bindings: win32more.AI.MachineLearning.DirectML.IDMLBindingTable_head) -> Void: ...
class IDMLCompiledOperator(c_void_p):
    extends: win32more.AI.MachineLearning.DirectML.IDMLDispatchable
    Guid = Guid('6b15e56a-bf5c-4902-92-d8-da-3a-65-0a-fe-a4')
class IDMLDebugDevice(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('7d6f3ac9-394a-4ac3-92-a7-39-0c-c5-7a-82-17')
    @commethod(3)
    def SetMuteDebugOutput(mute: win32more.Foundation.BOOL) -> Void: ...
class IDMLDevice(c_void_p):
    extends: win32more.AI.MachineLearning.DirectML.IDMLObject
    Guid = Guid('6dbd6437-96fd-423f-a9-8c-ae-5e-7c-2a-57-3f')
    @commethod(7)
    def CheckFeatureSupport(feature: win32more.AI.MachineLearning.DirectML.DML_FEATURE, featureQueryDataSize: UInt32, featureQueryData: c_void_p, featureSupportDataSize: UInt32, featureSupportData: c_void_p) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def CreateOperator(desc: POINTER(win32more.AI.MachineLearning.DirectML.DML_OPERATOR_DESC_head), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def CompileOperator(op: win32more.AI.MachineLearning.DirectML.IDMLOperator_head, flags: win32more.AI.MachineLearning.DirectML.DML_EXECUTION_FLAGS, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def CreateOperatorInitializer(operatorCount: UInt32, operators: POINTER(win32more.AI.MachineLearning.DirectML.IDMLCompiledOperator_head), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def CreateCommandRecorder(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def CreateBindingTable(desc: POINTER(win32more.AI.MachineLearning.DirectML.DML_BINDING_TABLE_DESC_head), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Evict(count: UInt32, ppObjects: POINTER(win32more.AI.MachineLearning.DirectML.IDMLPageable_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def MakeResident(count: UInt32, ppObjects: POINTER(win32more.AI.MachineLearning.DirectML.IDMLPageable_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetDeviceRemovedReason() -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetParentDevice(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IDMLDevice1(c_void_p):
    extends: win32more.AI.MachineLearning.DirectML.IDMLDevice
    Guid = Guid('a0884f9a-d2be-4355-aa-5d-59-01-28-1a-d1-d2')
    @commethod(17)
    def CompileGraph(desc: POINTER(win32more.AI.MachineLearning.DirectML.DML_GRAPH_DESC_head), flags: win32more.AI.MachineLearning.DirectML.DML_EXECUTION_FLAGS, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IDMLDeviceChild(c_void_p):
    extends: win32more.AI.MachineLearning.DirectML.IDMLObject
    Guid = Guid('27e83142-8165-49e3-97-4e-2f-d6-6e-4c-b6-9d')
    @commethod(7)
    def GetDevice(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IDMLDispatchable(c_void_p):
    extends: win32more.AI.MachineLearning.DirectML.IDMLPageable
    Guid = Guid('dcb821a8-1039-441e-9f-1c-b1-75-9c-2f-3c-ec')
    @commethod(8)
    def GetBindingProperties() -> win32more.AI.MachineLearning.DirectML.DML_BINDING_PROPERTIES: ...
class IDMLObject(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c8263aac-9e0c-4a2d-9b-8e-00-75-21-a3-31-7c')
    @commethod(3)
    def GetPrivateData(guid: POINTER(Guid), dataSize: POINTER(UInt32), data: c_void_p) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetPrivateData(guid: POINTER(Guid), dataSize: UInt32, data: c_void_p) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetPrivateDataInterface(guid: POINTER(Guid), data: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetName(name: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class IDMLOperator(c_void_p):
    extends: win32more.AI.MachineLearning.DirectML.IDMLDeviceChild
    Guid = Guid('26caae7a-3081-4633-95-81-22-6f-be-57-69-5d')
class IDMLOperatorInitializer(c_void_p):
    extends: win32more.AI.MachineLearning.DirectML.IDMLDispatchable
    Guid = Guid('427c1113-435c-469c-86-76-4d-5d-d0-72-f8-13')
    @commethod(9)
    def Reset(operatorCount: UInt32, operators: POINTER(win32more.AI.MachineLearning.DirectML.IDMLCompiledOperator_head)) -> win32more.Foundation.HRESULT: ...
class IDMLPageable(c_void_p):
    extends: win32more.AI.MachineLearning.DirectML.IDMLDeviceChild
    Guid = Guid('b1ab0825-4542-4a4b-86-17-6d-de-6e-8f-62-01')
make_head(_module, 'DML_ACTIVATION_CELU_OPERATOR_DESC')
make_head(_module, 'DML_ACTIVATION_ELU_OPERATOR_DESC')
make_head(_module, 'DML_ACTIVATION_HARDMAX_OPERATOR_DESC')
make_head(_module, 'DML_ACTIVATION_HARD_SIGMOID_OPERATOR_DESC')
make_head(_module, 'DML_ACTIVATION_IDENTITY_OPERATOR_DESC')
make_head(_module, 'DML_ACTIVATION_LEAKY_RELU_OPERATOR_DESC')
make_head(_module, 'DML_ACTIVATION_LINEAR_OPERATOR_DESC')
make_head(_module, 'DML_ACTIVATION_LOG_SOFTMAX_OPERATOR_DESC')
make_head(_module, 'DML_ACTIVATION_PARAMETERIZED_RELU_OPERATOR_DESC')
make_head(_module, 'DML_ACTIVATION_PARAMETRIC_SOFTPLUS_OPERATOR_DESC')
make_head(_module, 'DML_ACTIVATION_RELU_GRAD_OPERATOR_DESC')
make_head(_module, 'DML_ACTIVATION_RELU_OPERATOR_DESC')
make_head(_module, 'DML_ACTIVATION_SCALED_ELU_OPERATOR_DESC')
make_head(_module, 'DML_ACTIVATION_SCALED_TANH_OPERATOR_DESC')
make_head(_module, 'DML_ACTIVATION_SHRINK_OPERATOR_DESC')
make_head(_module, 'DML_ACTIVATION_SIGMOID_OPERATOR_DESC')
make_head(_module, 'DML_ACTIVATION_SOFTMAX_OPERATOR_DESC')
make_head(_module, 'DML_ACTIVATION_SOFTPLUS_OPERATOR_DESC')
make_head(_module, 'DML_ACTIVATION_SOFTSIGN_OPERATOR_DESC')
make_head(_module, 'DML_ACTIVATION_TANH_OPERATOR_DESC')
make_head(_module, 'DML_ACTIVATION_THRESHOLDED_RELU_OPERATOR_DESC')
make_head(_module, 'DML_ADAM_OPTIMIZER_OPERATOR_DESC')
make_head(_module, 'DML_ARGMAX_OPERATOR_DESC')
make_head(_module, 'DML_ARGMIN_OPERATOR_DESC')
make_head(_module, 'DML_AVERAGE_POOLING_GRAD_OPERATOR_DESC')
make_head(_module, 'DML_AVERAGE_POOLING_OPERATOR_DESC')
make_head(_module, 'DML_BATCH_NORMALIZATION_GRAD_OPERATOR_DESC')
make_head(_module, 'DML_BATCH_NORMALIZATION_OPERATOR_DESC')
make_head(_module, 'DML_BINDING_DESC')
make_head(_module, 'DML_BINDING_PROPERTIES')
make_head(_module, 'DML_BINDING_TABLE_DESC')
make_head(_module, 'DML_BUFFER_ARRAY_BINDING')
make_head(_module, 'DML_BUFFER_BINDING')
make_head(_module, 'DML_BUFFER_TENSOR_DESC')
make_head(_module, 'DML_CAST_OPERATOR_DESC')
make_head(_module, 'DML_CONVOLUTION_INTEGER_OPERATOR_DESC')
make_head(_module, 'DML_CONVOLUTION_OPERATOR_DESC')
make_head(_module, 'DML_CUMULATIVE_PRODUCT_OPERATOR_DESC')
make_head(_module, 'DML_CUMULATIVE_SUMMATION_OPERATOR_DESC')
make_head(_module, 'DML_DEPTH_TO_SPACE1_OPERATOR_DESC')
make_head(_module, 'DML_DEPTH_TO_SPACE_OPERATOR_DESC')
make_head(_module, 'DML_DIAGONAL_MATRIX_OPERATOR_DESC')
make_head(_module, 'DML_DYNAMIC_QUANTIZE_LINEAR_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_ABS_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_ACOSH_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_ACOS_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_ADD1_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_ADD_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_ASINH_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_ASIN_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_ATANH_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_ATAN_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_ATAN_YX_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_BIT_AND_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_BIT_COUNT_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_BIT_NOT_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_BIT_OR_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_BIT_SHIFT_LEFT_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_BIT_SHIFT_RIGHT_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_BIT_XOR_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_CEIL_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_CLIP_GRAD_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_CLIP_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_CONSTANT_POW_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_COSH_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_COS_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_DEQUANTIZE_LINEAR_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_DIFFERENCE_SQUARE_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_DIVIDE_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_ERF_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_EXP_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_FLOOR_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_IDENTITY_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_IF_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_IS_INFINITY_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_IS_NAN_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_LOGICAL_AND_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_LOGICAL_EQUALS_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_LOGICAL_GREATER_THAN_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_LOGICAL_GREATER_THAN_OR_EQUAL_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_LOGICAL_LESS_THAN_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_LOGICAL_LESS_THAN_OR_EQUAL_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_LOGICAL_NOT_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_LOGICAL_OR_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_LOGICAL_XOR_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_LOG_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_MAX_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_MEAN_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_MIN_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_MODULUS_FLOOR_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_MODULUS_TRUNCATE_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_MULTIPLY_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_POW_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_QUANTIZED_LINEAR_ADD_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_QUANTIZE_LINEAR_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_RECIP_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_ROUND_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_SIGN_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_SINH_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_SIN_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_SQRT_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_SUBTRACT_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_TANH_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_TAN_OPERATOR_DESC')
make_head(_module, 'DML_ELEMENT_WISE_THRESHOLD_OPERATOR_DESC')
make_head(_module, 'DML_FEATURE_DATA_FEATURE_LEVELS')
make_head(_module, 'DML_FEATURE_DATA_TENSOR_DATA_TYPE_SUPPORT')
make_head(_module, 'DML_FEATURE_QUERY_FEATURE_LEVELS')
make_head(_module, 'DML_FEATURE_QUERY_TENSOR_DATA_TYPE_SUPPORT')
make_head(_module, 'DML_FILL_VALUE_CONSTANT_OPERATOR_DESC')
make_head(_module, 'DML_FILL_VALUE_SEQUENCE_OPERATOR_DESC')
make_head(_module, 'DML_GATHER_ELEMENTS_OPERATOR_DESC')
make_head(_module, 'DML_GATHER_ND1_OPERATOR_DESC')
make_head(_module, 'DML_GATHER_ND_OPERATOR_DESC')
make_head(_module, 'DML_GATHER_OPERATOR_DESC')
make_head(_module, 'DML_GEMM_OPERATOR_DESC')
make_head(_module, 'DML_GRAPH_DESC')
make_head(_module, 'DML_GRAPH_EDGE_DESC')
make_head(_module, 'DML_GRAPH_NODE_DESC')
make_head(_module, 'DML_GRU_OPERATOR_DESC')
make_head(_module, 'DML_INPUT_GRAPH_EDGE_DESC')
make_head(_module, 'DML_INTERMEDIATE_GRAPH_EDGE_DESC')
make_head(_module, 'DML_JOIN_OPERATOR_DESC')
make_head(_module, 'DML_LOCAL_RESPONSE_NORMALIZATION_GRAD_OPERATOR_DESC')
make_head(_module, 'DML_LOCAL_RESPONSE_NORMALIZATION_OPERATOR_DESC')
make_head(_module, 'DML_LP_NORMALIZATION_OPERATOR_DESC')
make_head(_module, 'DML_LP_POOLING_OPERATOR_DESC')
make_head(_module, 'DML_LSTM_OPERATOR_DESC')
make_head(_module, 'DML_MATRIX_MULTIPLY_INTEGER_OPERATOR_DESC')
make_head(_module, 'DML_MAX_POOLING1_OPERATOR_DESC')
make_head(_module, 'DML_MAX_POOLING2_OPERATOR_DESC')
make_head(_module, 'DML_MAX_POOLING_GRAD_OPERATOR_DESC')
make_head(_module, 'DML_MAX_POOLING_OPERATOR_DESC')
make_head(_module, 'DML_MAX_UNPOOLING_OPERATOR_DESC')
make_head(_module, 'DML_MEAN_VARIANCE_NORMALIZATION1_OPERATOR_DESC')
make_head(_module, 'DML_MEAN_VARIANCE_NORMALIZATION_OPERATOR_DESC')
make_head(_module, 'DML_NONZERO_COORDINATES_OPERATOR_DESC')
make_head(_module, 'DML_ONE_HOT_OPERATOR_DESC')
make_head(_module, 'DML_OPERATOR_DESC')
make_head(_module, 'DML_OPERATOR_GRAPH_NODE_DESC')
make_head(_module, 'DML_OUTPUT_GRAPH_EDGE_DESC')
make_head(_module, 'DML_PADDING_OPERATOR_DESC')
make_head(_module, 'DML_QUANTIZED_LINEAR_CONVOLUTION_OPERATOR_DESC')
make_head(_module, 'DML_QUANTIZED_LINEAR_MATRIX_MULTIPLY_OPERATOR_DESC')
make_head(_module, 'DML_RANDOM_GENERATOR_OPERATOR_DESC')
make_head(_module, 'DML_REDUCE_OPERATOR_DESC')
make_head(_module, 'DML_RESAMPLE1_OPERATOR_DESC')
make_head(_module, 'DML_RESAMPLE_GRAD_OPERATOR_DESC')
make_head(_module, 'DML_RESAMPLE_OPERATOR_DESC')
make_head(_module, 'DML_REVERSE_SUBSEQUENCES_OPERATOR_DESC')
make_head(_module, 'DML_RNN_OPERATOR_DESC')
make_head(_module, 'DML_ROI_ALIGN1_OPERATOR_DESC')
make_head(_module, 'DML_ROI_ALIGN_OPERATOR_DESC')
make_head(_module, 'DML_ROI_POOLING_OPERATOR_DESC')
make_head(_module, 'DML_SCALAR_UNION')
make_head(_module, 'DML_SCALE_BIAS')
make_head(_module, 'DML_SCATTER_ND_OPERATOR_DESC')
make_head(_module, 'DML_SCATTER_OPERATOR_DESC')
make_head(_module, 'DML_SIZE_2D')
make_head(_module, 'DML_SLICE1_OPERATOR_DESC')
make_head(_module, 'DML_SLICE_GRAD_OPERATOR_DESC')
make_head(_module, 'DML_SLICE_OPERATOR_DESC')
make_head(_module, 'DML_SPACE_TO_DEPTH1_OPERATOR_DESC')
make_head(_module, 'DML_SPACE_TO_DEPTH_OPERATOR_DESC')
make_head(_module, 'DML_SPLIT_OPERATOR_DESC')
make_head(_module, 'DML_TENSOR_DESC')
make_head(_module, 'DML_TILE_OPERATOR_DESC')
make_head(_module, 'DML_TOP_K1_OPERATOR_DESC')
make_head(_module, 'DML_TOP_K_OPERATOR_DESC')
make_head(_module, 'DML_UPSAMPLE_2D_OPERATOR_DESC')
make_head(_module, 'DML_VALUE_SCALE_2D_OPERATOR_DESC')
make_head(_module, 'IDMLBindingTable')
make_head(_module, 'IDMLCommandRecorder')
make_head(_module, 'IDMLCompiledOperator')
make_head(_module, 'IDMLDebugDevice')
make_head(_module, 'IDMLDevice')
make_head(_module, 'IDMLDevice1')
make_head(_module, 'IDMLDeviceChild')
make_head(_module, 'IDMLDispatchable')
make_head(_module, 'IDMLObject')
make_head(_module, 'IDMLOperator')
make_head(_module, 'IDMLOperatorInitializer')
make_head(_module, 'IDMLPageable')
__all__ = [
    "DMLCreateDevice",
    "DMLCreateDevice1",
    "DML_ACTIVATION_CELU_OPERATOR_DESC",
    "DML_ACTIVATION_ELU_OPERATOR_DESC",
    "DML_ACTIVATION_HARDMAX_OPERATOR_DESC",
    "DML_ACTIVATION_HARD_SIGMOID_OPERATOR_DESC",
    "DML_ACTIVATION_IDENTITY_OPERATOR_DESC",
    "DML_ACTIVATION_LEAKY_RELU_OPERATOR_DESC",
    "DML_ACTIVATION_LINEAR_OPERATOR_DESC",
    "DML_ACTIVATION_LOG_SOFTMAX_OPERATOR_DESC",
    "DML_ACTIVATION_PARAMETERIZED_RELU_OPERATOR_DESC",
    "DML_ACTIVATION_PARAMETRIC_SOFTPLUS_OPERATOR_DESC",
    "DML_ACTIVATION_RELU_GRAD_OPERATOR_DESC",
    "DML_ACTIVATION_RELU_OPERATOR_DESC",
    "DML_ACTIVATION_SCALED_ELU_OPERATOR_DESC",
    "DML_ACTIVATION_SCALED_TANH_OPERATOR_DESC",
    "DML_ACTIVATION_SHRINK_OPERATOR_DESC",
    "DML_ACTIVATION_SIGMOID_OPERATOR_DESC",
    "DML_ACTIVATION_SOFTMAX_OPERATOR_DESC",
    "DML_ACTIVATION_SOFTPLUS_OPERATOR_DESC",
    "DML_ACTIVATION_SOFTSIGN_OPERATOR_DESC",
    "DML_ACTIVATION_TANH_OPERATOR_DESC",
    "DML_ACTIVATION_THRESHOLDED_RELU_OPERATOR_DESC",
    "DML_ADAM_OPTIMIZER_OPERATOR_DESC",
    "DML_ARGMAX_OPERATOR_DESC",
    "DML_ARGMIN_OPERATOR_DESC",
    "DML_AVERAGE_POOLING_GRAD_OPERATOR_DESC",
    "DML_AVERAGE_POOLING_OPERATOR_DESC",
    "DML_AXIS_DIRECTION",
    "DML_AXIS_DIRECTION_DECREASING",
    "DML_AXIS_DIRECTION_INCREASING",
    "DML_BATCH_NORMALIZATION_GRAD_OPERATOR_DESC",
    "DML_BATCH_NORMALIZATION_OPERATOR_DESC",
    "DML_BINDING_DESC",
    "DML_BINDING_PROPERTIES",
    "DML_BINDING_TABLE_DESC",
    "DML_BINDING_TYPE",
    "DML_BINDING_TYPE_BUFFER",
    "DML_BINDING_TYPE_BUFFER_ARRAY",
    "DML_BINDING_TYPE_NONE",
    "DML_BUFFER_ARRAY_BINDING",
    "DML_BUFFER_BINDING",
    "DML_BUFFER_TENSOR_DESC",
    "DML_CAST_OPERATOR_DESC",
    "DML_CONVOLUTION_DIRECTION",
    "DML_CONVOLUTION_DIRECTION_BACKWARD",
    "DML_CONVOLUTION_DIRECTION_FORWARD",
    "DML_CONVOLUTION_INTEGER_OPERATOR_DESC",
    "DML_CONVOLUTION_MODE",
    "DML_CONVOLUTION_MODE_CONVOLUTION",
    "DML_CONVOLUTION_MODE_CROSS_CORRELATION",
    "DML_CONVOLUTION_OPERATOR_DESC",
    "DML_CREATE_DEVICE_FLAGS",
    "DML_CREATE_DEVICE_FLAG_DEBUG",
    "DML_CREATE_DEVICE_FLAG_NONE",
    "DML_CUMULATIVE_PRODUCT_OPERATOR_DESC",
    "DML_CUMULATIVE_SUMMATION_OPERATOR_DESC",
    "DML_DEPTH_SPACE_ORDER",
    "DML_DEPTH_SPACE_ORDER_COLUMN_ROW_DEPTH",
    "DML_DEPTH_SPACE_ORDER_DEPTH_COLUMN_ROW",
    "DML_DEPTH_TO_SPACE1_OPERATOR_DESC",
    "DML_DEPTH_TO_SPACE_OPERATOR_DESC",
    "DML_DIAGONAL_MATRIX_OPERATOR_DESC",
    "DML_DYNAMIC_QUANTIZE_LINEAR_OPERATOR_DESC",
    "DML_ELEMENT_WISE_ABS_OPERATOR_DESC",
    "DML_ELEMENT_WISE_ACOSH_OPERATOR_DESC",
    "DML_ELEMENT_WISE_ACOS_OPERATOR_DESC",
    "DML_ELEMENT_WISE_ADD1_OPERATOR_DESC",
    "DML_ELEMENT_WISE_ADD_OPERATOR_DESC",
    "DML_ELEMENT_WISE_ASINH_OPERATOR_DESC",
    "DML_ELEMENT_WISE_ASIN_OPERATOR_DESC",
    "DML_ELEMENT_WISE_ATANH_OPERATOR_DESC",
    "DML_ELEMENT_WISE_ATAN_OPERATOR_DESC",
    "DML_ELEMENT_WISE_ATAN_YX_OPERATOR_DESC",
    "DML_ELEMENT_WISE_BIT_AND_OPERATOR_DESC",
    "DML_ELEMENT_WISE_BIT_COUNT_OPERATOR_DESC",
    "DML_ELEMENT_WISE_BIT_NOT_OPERATOR_DESC",
    "DML_ELEMENT_WISE_BIT_OR_OPERATOR_DESC",
    "DML_ELEMENT_WISE_BIT_SHIFT_LEFT_OPERATOR_DESC",
    "DML_ELEMENT_WISE_BIT_SHIFT_RIGHT_OPERATOR_DESC",
    "DML_ELEMENT_WISE_BIT_XOR_OPERATOR_DESC",
    "DML_ELEMENT_WISE_CEIL_OPERATOR_DESC",
    "DML_ELEMENT_WISE_CLIP_GRAD_OPERATOR_DESC",
    "DML_ELEMENT_WISE_CLIP_OPERATOR_DESC",
    "DML_ELEMENT_WISE_CONSTANT_POW_OPERATOR_DESC",
    "DML_ELEMENT_WISE_COSH_OPERATOR_DESC",
    "DML_ELEMENT_WISE_COS_OPERATOR_DESC",
    "DML_ELEMENT_WISE_DEQUANTIZE_LINEAR_OPERATOR_DESC",
    "DML_ELEMENT_WISE_DIFFERENCE_SQUARE_OPERATOR_DESC",
    "DML_ELEMENT_WISE_DIVIDE_OPERATOR_DESC",
    "DML_ELEMENT_WISE_ERF_OPERATOR_DESC",
    "DML_ELEMENT_WISE_EXP_OPERATOR_DESC",
    "DML_ELEMENT_WISE_FLOOR_OPERATOR_DESC",
    "DML_ELEMENT_WISE_IDENTITY_OPERATOR_DESC",
    "DML_ELEMENT_WISE_IF_OPERATOR_DESC",
    "DML_ELEMENT_WISE_IS_INFINITY_OPERATOR_DESC",
    "DML_ELEMENT_WISE_IS_NAN_OPERATOR_DESC",
    "DML_ELEMENT_WISE_LOGICAL_AND_OPERATOR_DESC",
    "DML_ELEMENT_WISE_LOGICAL_EQUALS_OPERATOR_DESC",
    "DML_ELEMENT_WISE_LOGICAL_GREATER_THAN_OPERATOR_DESC",
    "DML_ELEMENT_WISE_LOGICAL_GREATER_THAN_OR_EQUAL_OPERATOR_DESC",
    "DML_ELEMENT_WISE_LOGICAL_LESS_THAN_OPERATOR_DESC",
    "DML_ELEMENT_WISE_LOGICAL_LESS_THAN_OR_EQUAL_OPERATOR_DESC",
    "DML_ELEMENT_WISE_LOGICAL_NOT_OPERATOR_DESC",
    "DML_ELEMENT_WISE_LOGICAL_OR_OPERATOR_DESC",
    "DML_ELEMENT_WISE_LOGICAL_XOR_OPERATOR_DESC",
    "DML_ELEMENT_WISE_LOG_OPERATOR_DESC",
    "DML_ELEMENT_WISE_MAX_OPERATOR_DESC",
    "DML_ELEMENT_WISE_MEAN_OPERATOR_DESC",
    "DML_ELEMENT_WISE_MIN_OPERATOR_DESC",
    "DML_ELEMENT_WISE_MODULUS_FLOOR_OPERATOR_DESC",
    "DML_ELEMENT_WISE_MODULUS_TRUNCATE_OPERATOR_DESC",
    "DML_ELEMENT_WISE_MULTIPLY_OPERATOR_DESC",
    "DML_ELEMENT_WISE_POW_OPERATOR_DESC",
    "DML_ELEMENT_WISE_QUANTIZED_LINEAR_ADD_OPERATOR_DESC",
    "DML_ELEMENT_WISE_QUANTIZE_LINEAR_OPERATOR_DESC",
    "DML_ELEMENT_WISE_RECIP_OPERATOR_DESC",
    "DML_ELEMENT_WISE_ROUND_OPERATOR_DESC",
    "DML_ELEMENT_WISE_SIGN_OPERATOR_DESC",
    "DML_ELEMENT_WISE_SINH_OPERATOR_DESC",
    "DML_ELEMENT_WISE_SIN_OPERATOR_DESC",
    "DML_ELEMENT_WISE_SQRT_OPERATOR_DESC",
    "DML_ELEMENT_WISE_SUBTRACT_OPERATOR_DESC",
    "DML_ELEMENT_WISE_TANH_OPERATOR_DESC",
    "DML_ELEMENT_WISE_TAN_OPERATOR_DESC",
    "DML_ELEMENT_WISE_THRESHOLD_OPERATOR_DESC",
    "DML_EXECUTION_FLAGS",
    "DML_EXECUTION_FLAG_ALLOW_HALF_PRECISION_COMPUTATION",
    "DML_EXECUTION_FLAG_DESCRIPTORS_VOLATILE",
    "DML_EXECUTION_FLAG_DISABLE_META_COMMANDS",
    "DML_EXECUTION_FLAG_NONE",
    "DML_FEATURE",
    "DML_FEATURE_DATA_FEATURE_LEVELS",
    "DML_FEATURE_DATA_TENSOR_DATA_TYPE_SUPPORT",
    "DML_FEATURE_FEATURE_LEVELS",
    "DML_FEATURE_LEVEL",
    "DML_FEATURE_LEVEL_1_0",
    "DML_FEATURE_LEVEL_2_0",
    "DML_FEATURE_LEVEL_2_1",
    "DML_FEATURE_LEVEL_3_0",
    "DML_FEATURE_LEVEL_3_1",
    "DML_FEATURE_LEVEL_4_0",
    "DML_FEATURE_QUERY_FEATURE_LEVELS",
    "DML_FEATURE_QUERY_TENSOR_DATA_TYPE_SUPPORT",
    "DML_FEATURE_TENSOR_DATA_TYPE_SUPPORT",
    "DML_FILL_VALUE_CONSTANT_OPERATOR_DESC",
    "DML_FILL_VALUE_SEQUENCE_OPERATOR_DESC",
    "DML_GATHER_ELEMENTS_OPERATOR_DESC",
    "DML_GATHER_ND1_OPERATOR_DESC",
    "DML_GATHER_ND_OPERATOR_DESC",
    "DML_GATHER_OPERATOR_DESC",
    "DML_GEMM_OPERATOR_DESC",
    "DML_GRAPH_DESC",
    "DML_GRAPH_EDGE_DESC",
    "DML_GRAPH_EDGE_TYPE",
    "DML_GRAPH_EDGE_TYPE_INPUT",
    "DML_GRAPH_EDGE_TYPE_INTERMEDIATE",
    "DML_GRAPH_EDGE_TYPE_INVALID",
    "DML_GRAPH_EDGE_TYPE_OUTPUT",
    "DML_GRAPH_NODE_DESC",
    "DML_GRAPH_NODE_TYPE",
    "DML_GRAPH_NODE_TYPE_INVALID",
    "DML_GRAPH_NODE_TYPE_OPERATOR",
    "DML_GRU_OPERATOR_DESC",
    "DML_INPUT_GRAPH_EDGE_DESC",
    "DML_INTERMEDIATE_GRAPH_EDGE_DESC",
    "DML_INTERPOLATION_MODE",
    "DML_INTERPOLATION_MODE_LINEAR",
    "DML_INTERPOLATION_MODE_NEAREST_NEIGHBOR",
    "DML_IS_INFINITY_MODE",
    "DML_IS_INFINITY_MODE_EITHER",
    "DML_IS_INFINITY_MODE_NEGATIVE",
    "DML_IS_INFINITY_MODE_POSITIVE",
    "DML_JOIN_OPERATOR_DESC",
    "DML_LOCAL_RESPONSE_NORMALIZATION_GRAD_OPERATOR_DESC",
    "DML_LOCAL_RESPONSE_NORMALIZATION_OPERATOR_DESC",
    "DML_LP_NORMALIZATION_OPERATOR_DESC",
    "DML_LP_POOLING_OPERATOR_DESC",
    "DML_LSTM_OPERATOR_DESC",
    "DML_MATRIX_MULTIPLY_INTEGER_OPERATOR_DESC",
    "DML_MATRIX_TRANSFORM",
    "DML_MATRIX_TRANSFORM_NONE",
    "DML_MATRIX_TRANSFORM_TRANSPOSE",
    "DML_MAX_POOLING1_OPERATOR_DESC",
    "DML_MAX_POOLING2_OPERATOR_DESC",
    "DML_MAX_POOLING_GRAD_OPERATOR_DESC",
    "DML_MAX_POOLING_OPERATOR_DESC",
    "DML_MAX_UNPOOLING_OPERATOR_DESC",
    "DML_MEAN_VARIANCE_NORMALIZATION1_OPERATOR_DESC",
    "DML_MEAN_VARIANCE_NORMALIZATION_OPERATOR_DESC",
    "DML_MINIMUM_BUFFER_TENSOR_ALIGNMENT",
    "DML_NONZERO_COORDINATES_OPERATOR_DESC",
    "DML_ONE_HOT_OPERATOR_DESC",
    "DML_OPERATOR_ACTIVATION_CELU",
    "DML_OPERATOR_ACTIVATION_ELU",
    "DML_OPERATOR_ACTIVATION_HARDMAX",
    "DML_OPERATOR_ACTIVATION_HARD_SIGMOID",
    "DML_OPERATOR_ACTIVATION_IDENTITY",
    "DML_OPERATOR_ACTIVATION_LEAKY_RELU",
    "DML_OPERATOR_ACTIVATION_LINEAR",
    "DML_OPERATOR_ACTIVATION_LOG_SOFTMAX",
    "DML_OPERATOR_ACTIVATION_PARAMETERIZED_RELU",
    "DML_OPERATOR_ACTIVATION_PARAMETRIC_SOFTPLUS",
    "DML_OPERATOR_ACTIVATION_RELU",
    "DML_OPERATOR_ACTIVATION_RELU_GRAD",
    "DML_OPERATOR_ACTIVATION_SCALED_ELU",
    "DML_OPERATOR_ACTIVATION_SCALED_TANH",
    "DML_OPERATOR_ACTIVATION_SHRINK",
    "DML_OPERATOR_ACTIVATION_SIGMOID",
    "DML_OPERATOR_ACTIVATION_SOFTMAX",
    "DML_OPERATOR_ACTIVATION_SOFTPLUS",
    "DML_OPERATOR_ACTIVATION_SOFTSIGN",
    "DML_OPERATOR_ACTIVATION_TANH",
    "DML_OPERATOR_ACTIVATION_THRESHOLDED_RELU",
    "DML_OPERATOR_ADAM_OPTIMIZER",
    "DML_OPERATOR_ARGMAX",
    "DML_OPERATOR_ARGMIN",
    "DML_OPERATOR_AVERAGE_POOLING",
    "DML_OPERATOR_AVERAGE_POOLING_GRAD",
    "DML_OPERATOR_BATCH_NORMALIZATION",
    "DML_OPERATOR_BATCH_NORMALIZATION_GRAD",
    "DML_OPERATOR_CAST",
    "DML_OPERATOR_CONVOLUTION",
    "DML_OPERATOR_CONVOLUTION_INTEGER",
    "DML_OPERATOR_CUMULATIVE_PRODUCT",
    "DML_OPERATOR_CUMULATIVE_SUMMATION",
    "DML_OPERATOR_DEPTH_TO_SPACE",
    "DML_OPERATOR_DEPTH_TO_SPACE1",
    "DML_OPERATOR_DESC",
    "DML_OPERATOR_DIAGONAL_MATRIX",
    "DML_OPERATOR_DYNAMIC_QUANTIZE_LINEAR",
    "DML_OPERATOR_ELEMENT_WISE_ABS",
    "DML_OPERATOR_ELEMENT_WISE_ACOS",
    "DML_OPERATOR_ELEMENT_WISE_ACOSH",
    "DML_OPERATOR_ELEMENT_WISE_ADD",
    "DML_OPERATOR_ELEMENT_WISE_ADD1",
    "DML_OPERATOR_ELEMENT_WISE_ASIN",
    "DML_OPERATOR_ELEMENT_WISE_ASINH",
    "DML_OPERATOR_ELEMENT_WISE_ATAN",
    "DML_OPERATOR_ELEMENT_WISE_ATANH",
    "DML_OPERATOR_ELEMENT_WISE_ATAN_YX",
    "DML_OPERATOR_ELEMENT_WISE_BIT_AND",
    "DML_OPERATOR_ELEMENT_WISE_BIT_COUNT",
    "DML_OPERATOR_ELEMENT_WISE_BIT_NOT",
    "DML_OPERATOR_ELEMENT_WISE_BIT_OR",
    "DML_OPERATOR_ELEMENT_WISE_BIT_SHIFT_LEFT",
    "DML_OPERATOR_ELEMENT_WISE_BIT_SHIFT_RIGHT",
    "DML_OPERATOR_ELEMENT_WISE_BIT_XOR",
    "DML_OPERATOR_ELEMENT_WISE_CEIL",
    "DML_OPERATOR_ELEMENT_WISE_CLIP",
    "DML_OPERATOR_ELEMENT_WISE_CLIP_GRAD",
    "DML_OPERATOR_ELEMENT_WISE_CONSTANT_POW",
    "DML_OPERATOR_ELEMENT_WISE_COS",
    "DML_OPERATOR_ELEMENT_WISE_COSH",
    "DML_OPERATOR_ELEMENT_WISE_DEQUANTIZE_LINEAR",
    "DML_OPERATOR_ELEMENT_WISE_DIFFERENCE_SQUARE",
    "DML_OPERATOR_ELEMENT_WISE_DIVIDE",
    "DML_OPERATOR_ELEMENT_WISE_ERF",
    "DML_OPERATOR_ELEMENT_WISE_EXP",
    "DML_OPERATOR_ELEMENT_WISE_FLOOR",
    "DML_OPERATOR_ELEMENT_WISE_IDENTITY",
    "DML_OPERATOR_ELEMENT_WISE_IF",
    "DML_OPERATOR_ELEMENT_WISE_IS_INFINITY",
    "DML_OPERATOR_ELEMENT_WISE_IS_NAN",
    "DML_OPERATOR_ELEMENT_WISE_LOG",
    "DML_OPERATOR_ELEMENT_WISE_LOGICAL_AND",
    "DML_OPERATOR_ELEMENT_WISE_LOGICAL_EQUALS",
    "DML_OPERATOR_ELEMENT_WISE_LOGICAL_GREATER_THAN",
    "DML_OPERATOR_ELEMENT_WISE_LOGICAL_GREATER_THAN_OR_EQUAL",
    "DML_OPERATOR_ELEMENT_WISE_LOGICAL_LESS_THAN",
    "DML_OPERATOR_ELEMENT_WISE_LOGICAL_LESS_THAN_OR_EQUAL",
    "DML_OPERATOR_ELEMENT_WISE_LOGICAL_NOT",
    "DML_OPERATOR_ELEMENT_WISE_LOGICAL_OR",
    "DML_OPERATOR_ELEMENT_WISE_LOGICAL_XOR",
    "DML_OPERATOR_ELEMENT_WISE_MAX",
    "DML_OPERATOR_ELEMENT_WISE_MEAN",
    "DML_OPERATOR_ELEMENT_WISE_MIN",
    "DML_OPERATOR_ELEMENT_WISE_MODULUS_FLOOR",
    "DML_OPERATOR_ELEMENT_WISE_MODULUS_TRUNCATE",
    "DML_OPERATOR_ELEMENT_WISE_MULTIPLY",
    "DML_OPERATOR_ELEMENT_WISE_POW",
    "DML_OPERATOR_ELEMENT_WISE_QUANTIZED_LINEAR_ADD",
    "DML_OPERATOR_ELEMENT_WISE_QUANTIZE_LINEAR",
    "DML_OPERATOR_ELEMENT_WISE_RECIP",
    "DML_OPERATOR_ELEMENT_WISE_ROUND",
    "DML_OPERATOR_ELEMENT_WISE_SIGN",
    "DML_OPERATOR_ELEMENT_WISE_SIN",
    "DML_OPERATOR_ELEMENT_WISE_SINH",
    "DML_OPERATOR_ELEMENT_WISE_SQRT",
    "DML_OPERATOR_ELEMENT_WISE_SUBTRACT",
    "DML_OPERATOR_ELEMENT_WISE_TAN",
    "DML_OPERATOR_ELEMENT_WISE_TANH",
    "DML_OPERATOR_ELEMENT_WISE_THRESHOLD",
    "DML_OPERATOR_FILL_VALUE_CONSTANT",
    "DML_OPERATOR_FILL_VALUE_SEQUENCE",
    "DML_OPERATOR_GATHER",
    "DML_OPERATOR_GATHER_ELEMENTS",
    "DML_OPERATOR_GATHER_ND",
    "DML_OPERATOR_GATHER_ND1",
    "DML_OPERATOR_GEMM",
    "DML_OPERATOR_GRAPH_NODE_DESC",
    "DML_OPERATOR_GRU",
    "DML_OPERATOR_INVALID",
    "DML_OPERATOR_JOIN",
    "DML_OPERATOR_LOCAL_RESPONSE_NORMALIZATION",
    "DML_OPERATOR_LOCAL_RESPONSE_NORMALIZATION_GRAD",
    "DML_OPERATOR_LP_NORMALIZATION",
    "DML_OPERATOR_LP_POOLING",
    "DML_OPERATOR_LSTM",
    "DML_OPERATOR_MATRIX_MULTIPLY_INTEGER",
    "DML_OPERATOR_MAX_POOLING",
    "DML_OPERATOR_MAX_POOLING1",
    "DML_OPERATOR_MAX_POOLING2",
    "DML_OPERATOR_MAX_POOLING_GRAD",
    "DML_OPERATOR_MAX_UNPOOLING",
    "DML_OPERATOR_MEAN_VARIANCE_NORMALIZATION",
    "DML_OPERATOR_MEAN_VARIANCE_NORMALIZATION1",
    "DML_OPERATOR_NONZERO_COORDINATES",
    "DML_OPERATOR_ONE_HOT",
    "DML_OPERATOR_PADDING",
    "DML_OPERATOR_QUANTIZED_LINEAR_CONVOLUTION",
    "DML_OPERATOR_QUANTIZED_LINEAR_MATRIX_MULTIPLY",
    "DML_OPERATOR_RANDOM_GENERATOR",
    "DML_OPERATOR_REDUCE",
    "DML_OPERATOR_RESAMPLE",
    "DML_OPERATOR_RESAMPLE1",
    "DML_OPERATOR_RESAMPLE_GRAD",
    "DML_OPERATOR_REVERSE_SUBSEQUENCES",
    "DML_OPERATOR_RNN",
    "DML_OPERATOR_ROI_ALIGN",
    "DML_OPERATOR_ROI_ALIGN1",
    "DML_OPERATOR_ROI_POOLING",
    "DML_OPERATOR_SCATTER",
    "DML_OPERATOR_SCATTER_ELEMENTS",
    "DML_OPERATOR_SCATTER_ND",
    "DML_OPERATOR_SLICE",
    "DML_OPERATOR_SLICE1",
    "DML_OPERATOR_SLICE_GRAD",
    "DML_OPERATOR_SPACE_TO_DEPTH",
    "DML_OPERATOR_SPACE_TO_DEPTH1",
    "DML_OPERATOR_SPLIT",
    "DML_OPERATOR_TILE",
    "DML_OPERATOR_TOP_K",
    "DML_OPERATOR_TOP_K1",
    "DML_OPERATOR_TYPE",
    "DML_OPERATOR_UPSAMPLE_2D",
    "DML_OPERATOR_VALUE_SCALE_2D",
    "DML_OUTPUT_GRAPH_EDGE_DESC",
    "DML_PADDING_MODE",
    "DML_PADDING_MODE_CONSTANT",
    "DML_PADDING_MODE_EDGE",
    "DML_PADDING_MODE_REFLECTION",
    "DML_PADDING_MODE_SYMMETRIC",
    "DML_PADDING_OPERATOR_DESC",
    "DML_PERSISTENT_BUFFER_ALIGNMENT",
    "DML_QUANTIZED_LINEAR_CONVOLUTION_OPERATOR_DESC",
    "DML_QUANTIZED_LINEAR_MATRIX_MULTIPLY_OPERATOR_DESC",
    "DML_RANDOM_GENERATOR_OPERATOR_DESC",
    "DML_RANDOM_GENERATOR_TYPE",
    "DML_RANDOM_GENERATOR_TYPE_PHILOX_4X32_10",
    "DML_RECURRENT_NETWORK_DIRECTION",
    "DML_RECURRENT_NETWORK_DIRECTION_BACKWARD",
    "DML_RECURRENT_NETWORK_DIRECTION_BIDIRECTIONAL",
    "DML_RECURRENT_NETWORK_DIRECTION_FORWARD",
    "DML_REDUCE_FUNCTION",
    "DML_REDUCE_FUNCTION_ARGMAX",
    "DML_REDUCE_FUNCTION_ARGMIN",
    "DML_REDUCE_FUNCTION_AVERAGE",
    "DML_REDUCE_FUNCTION_L1",
    "DML_REDUCE_FUNCTION_L2",
    "DML_REDUCE_FUNCTION_LOG_SUM",
    "DML_REDUCE_FUNCTION_LOG_SUM_EXP",
    "DML_REDUCE_FUNCTION_MAX",
    "DML_REDUCE_FUNCTION_MIN",
    "DML_REDUCE_FUNCTION_MULTIPLY",
    "DML_REDUCE_FUNCTION_SUM",
    "DML_REDUCE_FUNCTION_SUM_SQUARE",
    "DML_REDUCE_OPERATOR_DESC",
    "DML_RESAMPLE1_OPERATOR_DESC",
    "DML_RESAMPLE_GRAD_OPERATOR_DESC",
    "DML_RESAMPLE_OPERATOR_DESC",
    "DML_REVERSE_SUBSEQUENCES_OPERATOR_DESC",
    "DML_RNN_OPERATOR_DESC",
    "DML_ROI_ALIGN1_OPERATOR_DESC",
    "DML_ROI_ALIGN_OPERATOR_DESC",
    "DML_ROI_POOLING_OPERATOR_DESC",
    "DML_ROUNDING_MODE",
    "DML_ROUNDING_MODE_HALVES_TO_NEAREST_EVEN",
    "DML_ROUNDING_MODE_TOWARD_INFINITY",
    "DML_ROUNDING_MODE_TOWARD_ZERO",
    "DML_SCALAR_UNION",
    "DML_SCALE_BIAS",
    "DML_SCATTER_ND_OPERATOR_DESC",
    "DML_SCATTER_OPERATOR_DESC",
    "DML_SIZE_2D",
    "DML_SLICE1_OPERATOR_DESC",
    "DML_SLICE_GRAD_OPERATOR_DESC",
    "DML_SLICE_OPERATOR_DESC",
    "DML_SPACE_TO_DEPTH1_OPERATOR_DESC",
    "DML_SPACE_TO_DEPTH_OPERATOR_DESC",
    "DML_SPLIT_OPERATOR_DESC",
    "DML_TARGET_VERSION",
    "DML_TEMPORARY_BUFFER_ALIGNMENT",
    "DML_TENSOR_DATA_TYPE",
    "DML_TENSOR_DATA_TYPE_FLOAT16",
    "DML_TENSOR_DATA_TYPE_FLOAT32",
    "DML_TENSOR_DATA_TYPE_FLOAT64",
    "DML_TENSOR_DATA_TYPE_INT16",
    "DML_TENSOR_DATA_TYPE_INT32",
    "DML_TENSOR_DATA_TYPE_INT64",
    "DML_TENSOR_DATA_TYPE_INT8",
    "DML_TENSOR_DATA_TYPE_UINT16",
    "DML_TENSOR_DATA_TYPE_UINT32",
    "DML_TENSOR_DATA_TYPE_UINT64",
    "DML_TENSOR_DATA_TYPE_UINT8",
    "DML_TENSOR_DATA_TYPE_UNKNOWN",
    "DML_TENSOR_DESC",
    "DML_TENSOR_DIMENSION_COUNT_MAX",
    "DML_TENSOR_DIMENSION_COUNT_MAX1",
    "DML_TENSOR_FLAGS",
    "DML_TENSOR_FLAG_NONE",
    "DML_TENSOR_FLAG_OWNED_BY_DML",
    "DML_TENSOR_TYPE",
    "DML_TENSOR_TYPE_BUFFER",
    "DML_TENSOR_TYPE_INVALID",
    "DML_TILE_OPERATOR_DESC",
    "DML_TOP_K1_OPERATOR_DESC",
    "DML_TOP_K_OPERATOR_DESC",
    "DML_UPSAMPLE_2D_OPERATOR_DESC",
    "DML_VALUE_SCALE_2D_OPERATOR_DESC",
    "IDMLBindingTable",
    "IDMLCommandRecorder",
    "IDMLCompiledOperator",
    "IDMLDebugDevice",
    "IDMLDevice",
    "IDMLDevice1",
    "IDMLDeviceChild",
    "IDMLDispatchable",
    "IDMLObject",
    "IDMLOperator",
    "IDMLOperatorInitializer",
    "IDMLPageable",
]
_arch_optional = [
]
