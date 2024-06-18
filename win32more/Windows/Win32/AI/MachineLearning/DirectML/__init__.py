from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.AI.MachineLearning.DirectML
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Direct3D12
import win32more.Windows.Win32.System.Com
DML_TARGET_VERSION: UInt32 = 20480
DML_TENSOR_DIMENSION_COUNT_MAX: UInt32 = 5
DML_TENSOR_DIMENSION_COUNT_MAX1: UInt32 = 8
DML_TEMPORARY_BUFFER_ALIGNMENT: UInt32 = 256
DML_PERSISTENT_BUFFER_ALIGNMENT: UInt32 = 256
DML_MINIMUM_BUFFER_TENSOR_ALIGNMENT: UInt32 = 16
@winfunctype('DirectML.dll')
def DMLCreateDevice(d3d12Device: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Device, flags: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_CREATE_DEVICE_FLAGS, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('DirectML.dll')
def DMLCreateDevice1(d3d12Device: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Device, flags: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_CREATE_DEVICE_FLAGS, minimumFeatureLevel: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_FEATURE_LEVEL, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class DML_ACTIVATION_CELU_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Alpha: Single
class DML_ACTIVATION_ELU_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Alpha: Single
class DML_ACTIVATION_HARDMAX_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ACTIVATION_HARD_SIGMOID_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Alpha: Single
    Beta: Single
class DML_ACTIVATION_IDENTITY_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ACTIVATION_LEAKY_RELU_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Alpha: Single
class DML_ACTIVATION_LINEAR_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Alpha: Single
    Beta: Single
class DML_ACTIVATION_LOG_SOFTMAX_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ACTIVATION_PARAMETERIZED_RELU_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    SlopeTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ACTIVATION_PARAMETRIC_SOFTPLUS_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Alpha: Single
    Beta: Single
class DML_ACTIVATION_RELU_GRAD_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    InputGradientTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputGradientTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ACTIVATION_RELU_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ACTIVATION_SCALED_ELU_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Alpha: Single
    Gamma: Single
class DML_ACTIVATION_SCALED_TANH_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Alpha: Single
    Beta: Single
class DML_ACTIVATION_SHRINK_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Bias: Single
    Threshold: Single
class DML_ACTIVATION_SIGMOID_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ACTIVATION_SOFTMAX_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ACTIVATION_SOFTPLUS_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Steepness: Single
class DML_ACTIVATION_SOFTSIGN_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ACTIVATION_TANH_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ACTIVATION_THRESHOLDED_RELU_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Alpha: Single
class DML_ADAM_OPTIMIZER_OPERATOR_DESC(Structure):
    InputParametersTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    InputFirstMomentTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    InputSecondMomentTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    GradientTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    TrainingStepTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputParametersTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputFirstMomentTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputSecondMomentTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    LearningRate: Single
    Beta1: Single
    Beta2: Single
    Epsilon: Single
class DML_ARGMAX_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    AxisCount: UInt32
    Axes: POINTER(UInt32)
    AxisDirection: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_AXIS_DIRECTION
class DML_ARGMIN_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    AxisCount: UInt32
    Axes: POINTER(UInt32)
    AxisDirection: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_AXIS_DIRECTION
class DML_AVERAGE_POOLING_GRAD_OPERATOR_DESC(Structure):
    InputGradientTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputGradientTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    DimensionCount: UInt32
    Strides: POINTER(UInt32)
    WindowSize: POINTER(UInt32)
    StartPadding: POINTER(UInt32)
    EndPadding: POINTER(UInt32)
    IncludePadding: win32more.Windows.Win32.Foundation.BOOL
class DML_AVERAGE_POOLING_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    DimensionCount: UInt32
    Strides: POINTER(UInt32)
    WindowSize: POINTER(UInt32)
    StartPadding: POINTER(UInt32)
    EndPadding: POINTER(UInt32)
    IncludePadding: win32more.Windows.Win32.Foundation.BOOL
DML_AXIS_DIRECTION = Int32
DML_AXIS_DIRECTION_INCREASING: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_AXIS_DIRECTION = 0
DML_AXIS_DIRECTION_DECREASING: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_AXIS_DIRECTION = 1
class DML_BATCH_NORMALIZATION_GRAD_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    InputGradientTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    MeanTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    VarianceTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputGradientTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputScaleGradientTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputBiasGradientTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Epsilon: Single
class DML_BATCH_NORMALIZATION_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    MeanTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    VarianceTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BiasTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Spatial: win32more.Windows.Win32.Foundation.BOOL
    Epsilon: Single
    FusedActivation: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_DESC)
class DML_BINDING_DESC(Structure):
    Type: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_BINDING_TYPE
    Desc: VoidPtr
class DML_BINDING_PROPERTIES(Structure):
    RequiredDescriptorCount: UInt32
    TemporaryResourceSize: UInt64
    PersistentResourceSize: UInt64
class DML_BINDING_TABLE_DESC(Structure):
    Dispatchable: win32more.Windows.Win32.AI.MachineLearning.DirectML.IDMLDispatchable
    CPUDescriptorHandle: win32more.Windows.Win32.Graphics.Direct3D12.D3D12_CPU_DESCRIPTOR_HANDLE
    GPUDescriptorHandle: win32more.Windows.Win32.Graphics.Direct3D12.D3D12_GPU_DESCRIPTOR_HANDLE
    SizeInDescriptors: UInt32
DML_BINDING_TYPE = Int32
DML_BINDING_TYPE_NONE: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_BINDING_TYPE = 0
DML_BINDING_TYPE_BUFFER: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_BINDING_TYPE = 1
DML_BINDING_TYPE_BUFFER_ARRAY: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_BINDING_TYPE = 2
class DML_BUFFER_ARRAY_BINDING(Structure):
    BindingCount: UInt32
    Bindings: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_BUFFER_BINDING)
class DML_BUFFER_BINDING(Structure):
    Buffer: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12Resource
    Offset: UInt64
    SizeInBytes: UInt64
class DML_BUFFER_TENSOR_DESC(Structure):
    DataType: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DATA_TYPE
    Flags: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_FLAGS
    DimensionCount: UInt32
    Sizes: POINTER(UInt32)
    Strides: POINTER(UInt32)
    TotalTensorSizeInBytes: UInt64
    GuaranteedBaseOffsetAlignment: UInt32
class DML_CAST_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
DML_CONVOLUTION_DIRECTION = Int32
DML_CONVOLUTION_DIRECTION_FORWARD: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_CONVOLUTION_DIRECTION = 0
DML_CONVOLUTION_DIRECTION_BACKWARD: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_CONVOLUTION_DIRECTION = 1
class DML_CONVOLUTION_INTEGER_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    InputZeroPointTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    FilterTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    FilterZeroPointTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    DimensionCount: UInt32
    Strides: POINTER(UInt32)
    Dilations: POINTER(UInt32)
    StartPadding: POINTER(UInt32)
    EndPadding: POINTER(UInt32)
    GroupCount: UInt32
DML_CONVOLUTION_MODE = Int32
DML_CONVOLUTION_MODE_CONVOLUTION: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_CONVOLUTION_MODE = 0
DML_CONVOLUTION_MODE_CROSS_CORRELATION: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_CONVOLUTION_MODE = 1
class DML_CONVOLUTION_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    FilterTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BiasTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Mode: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_CONVOLUTION_MODE
    Direction: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_CONVOLUTION_DIRECTION
    DimensionCount: UInt32
    Strides: POINTER(UInt32)
    Dilations: POINTER(UInt32)
    StartPadding: POINTER(UInt32)
    EndPadding: POINTER(UInt32)
    OutputPadding: POINTER(UInt32)
    GroupCount: UInt32
    FusedActivation: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_DESC)
DML_CREATE_DEVICE_FLAGS = Int32
DML_CREATE_DEVICE_FLAG_NONE: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_CREATE_DEVICE_FLAGS = 0
DML_CREATE_DEVICE_FLAG_DEBUG: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_CREATE_DEVICE_FLAGS = 1
class DML_CUMULATIVE_PRODUCT_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Axis: UInt32
    AxisDirection: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_AXIS_DIRECTION
    HasExclusiveProduct: win32more.Windows.Win32.Foundation.BOOL
class DML_CUMULATIVE_SUMMATION_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Axis: UInt32
    AxisDirection: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_AXIS_DIRECTION
    HasExclusiveSum: win32more.Windows.Win32.Foundation.BOOL
DML_DEPTH_SPACE_ORDER = Int32
DML_DEPTH_SPACE_ORDER_DEPTH_COLUMN_ROW: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_DEPTH_SPACE_ORDER = 0
DML_DEPTH_SPACE_ORDER_COLUMN_ROW_DEPTH: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_DEPTH_SPACE_ORDER = 1
class DML_DEPTH_TO_SPACE1_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BlockSize: UInt32
    Order: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_DEPTH_SPACE_ORDER
class DML_DEPTH_TO_SPACE_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BlockSize: UInt32
class DML_DIAGONAL_MATRIX_OPERATOR_DESC(Structure):
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Offset: Int32
    Value: Single
class DML_DYNAMIC_QUANTIZE_LINEAR_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputScaleTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputZeroPointTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_ABS_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleBias: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALE_BIAS)
class DML_ELEMENT_WISE_ACOSH_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleBias: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALE_BIAS)
class DML_ELEMENT_WISE_ACOS_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleBias: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALE_BIAS)
class DML_ELEMENT_WISE_ADD1_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    FusedActivation: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_DESC)
class DML_ELEMENT_WISE_ADD_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_ASINH_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleBias: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALE_BIAS)
class DML_ELEMENT_WISE_ASIN_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleBias: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALE_BIAS)
class DML_ELEMENT_WISE_ATANH_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleBias: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALE_BIAS)
class DML_ELEMENT_WISE_ATAN_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleBias: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALE_BIAS)
class DML_ELEMENT_WISE_ATAN_YX_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_BIT_AND_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_BIT_COUNT_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_BIT_NOT_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_BIT_OR_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_BIT_SHIFT_LEFT_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_BIT_SHIFT_RIGHT_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_BIT_XOR_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_CEIL_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleBias: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALE_BIAS)
class DML_ELEMENT_WISE_CLIP_GRAD_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    InputGradientTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputGradientTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Min: Single
    Max: Single
class DML_ELEMENT_WISE_CLIP_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleBias: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALE_BIAS)
    Min: Single
    Max: Single
class DML_ELEMENT_WISE_CONSTANT_POW_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleBias: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALE_BIAS)
    Exponent: Single
class DML_ELEMENT_WISE_COSH_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleBias: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALE_BIAS)
class DML_ELEMENT_WISE_COS_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleBias: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALE_BIAS)
class DML_ELEMENT_WISE_DEQUANTIZE_LINEAR_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ZeroPointTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_DIFFERENCE_SQUARE_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_DIVIDE_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_ERF_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleBias: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALE_BIAS)
class DML_ELEMENT_WISE_EXP_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleBias: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALE_BIAS)
class DML_ELEMENT_WISE_FLOOR_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleBias: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALE_BIAS)
class DML_ELEMENT_WISE_IDENTITY_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleBias: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALE_BIAS)
class DML_ELEMENT_WISE_IF_OPERATOR_DESC(Structure):
    ConditionTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_IS_INFINITY_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    InfinityMode: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_IS_INFINITY_MODE
class DML_ELEMENT_WISE_IS_NAN_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_LOGICAL_AND_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_LOGICAL_EQUALS_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_LOGICAL_GREATER_THAN_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_LOGICAL_GREATER_THAN_OR_EQUAL_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_LOGICAL_LESS_THAN_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_LOGICAL_LESS_THAN_OR_EQUAL_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_LOGICAL_NOT_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_LOGICAL_OR_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_LOGICAL_XOR_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_LOG_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleBias: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALE_BIAS)
class DML_ELEMENT_WISE_MAX_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_MEAN_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_MIN_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_MODULUS_FLOOR_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_MODULUS_TRUNCATE_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_MULTIPLY_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_POW_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ExponentTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleBias: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALE_BIAS)
class DML_ELEMENT_WISE_QUANTIZED_LINEAR_ADD_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    AScaleTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    AZeroPointTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BScaleTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BZeroPointTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputScaleTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputZeroPointTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_QUANTIZE_LINEAR_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ZeroPointTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_RECIP_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleBias: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALE_BIAS)
class DML_ELEMENT_WISE_ROUND_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    RoundingMode: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_ROUNDING_MODE
class DML_ELEMENT_WISE_SIGN_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_SINH_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleBias: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALE_BIAS)
class DML_ELEMENT_WISE_SIN_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleBias: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALE_BIAS)
class DML_ELEMENT_WISE_SQRT_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleBias: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALE_BIAS)
class DML_ELEMENT_WISE_SUBTRACT_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ELEMENT_WISE_TANH_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleBias: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALE_BIAS)
class DML_ELEMENT_WISE_TAN_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleBias: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALE_BIAS)
class DML_ELEMENT_WISE_THRESHOLD_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleBias: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALE_BIAS)
    Min: Single
DML_EXECUTION_FLAGS = Int32
DML_EXECUTION_FLAG_NONE: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_EXECUTION_FLAGS = 0
DML_EXECUTION_FLAG_ALLOW_HALF_PRECISION_COMPUTATION: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_EXECUTION_FLAGS = 1
DML_EXECUTION_FLAG_DISABLE_META_COMMANDS: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_EXECUTION_FLAGS = 2
DML_EXECUTION_FLAG_DESCRIPTORS_VOLATILE: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_EXECUTION_FLAGS = 4
DML_FEATURE = Int32
DML_FEATURE_TENSOR_DATA_TYPE_SUPPORT: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_FEATURE = 0
DML_FEATURE_FEATURE_LEVELS: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_FEATURE = 1
class DML_FEATURE_DATA_FEATURE_LEVELS(Structure):
    MaxSupportedFeatureLevel: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_FEATURE_LEVEL
class DML_FEATURE_DATA_TENSOR_DATA_TYPE_SUPPORT(Structure):
    IsSupported: win32more.Windows.Win32.Foundation.BOOL
DML_FEATURE_LEVEL = Int32
DML_FEATURE_LEVEL_1_0: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_FEATURE_LEVEL = 4096
DML_FEATURE_LEVEL_2_0: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_FEATURE_LEVEL = 8192
DML_FEATURE_LEVEL_2_1: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_FEATURE_LEVEL = 8448
DML_FEATURE_LEVEL_3_0: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_FEATURE_LEVEL = 12288
DML_FEATURE_LEVEL_3_1: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_FEATURE_LEVEL = 12544
DML_FEATURE_LEVEL_4_0: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_FEATURE_LEVEL = 16384
DML_FEATURE_LEVEL_4_1: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_FEATURE_LEVEL = 16640
DML_FEATURE_LEVEL_5_0: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_FEATURE_LEVEL = 20480
class DML_FEATURE_QUERY_FEATURE_LEVELS(Structure):
    RequestedFeatureLevelCount: UInt32
    RequestedFeatureLevels: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_FEATURE_LEVEL)
class DML_FEATURE_QUERY_TENSOR_DATA_TYPE_SUPPORT(Structure):
    DataType: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DATA_TYPE
class DML_FILL_VALUE_CONSTANT_OPERATOR_DESC(Structure):
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ValueDataType: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DATA_TYPE
    Value: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALAR_UNION
class DML_FILL_VALUE_SEQUENCE_OPERATOR_DESC(Structure):
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ValueDataType: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DATA_TYPE
    ValueStart: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALAR_UNION
    ValueDelta: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SCALAR_UNION
class DML_GATHER_ELEMENTS_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    IndicesTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Axis: UInt32
class DML_GATHER_ND1_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    IndicesTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    InputDimensionCount: UInt32
    IndicesDimensionCount: UInt32
    BatchDimensionCount: UInt32
class DML_GATHER_ND_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    IndicesTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    InputDimensionCount: UInt32
    IndicesDimensionCount: UInt32
class DML_GATHER_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    IndicesTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Axis: UInt32
    IndexDimensions: UInt32
class DML_GEMM_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    CTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    TransA: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_MATRIX_TRANSFORM
    TransB: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_MATRIX_TRANSFORM
    Alpha: Single
    Beta: Single
    FusedActivation: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_DESC)
class DML_GRAPH_DESC(Structure):
    InputCount: UInt32
    OutputCount: UInt32
    NodeCount: UInt32
    Nodes: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_GRAPH_NODE_DESC)
    InputEdgeCount: UInt32
    InputEdges: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_GRAPH_EDGE_DESC)
    OutputEdgeCount: UInt32
    OutputEdges: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_GRAPH_EDGE_DESC)
    IntermediateEdgeCount: UInt32
    IntermediateEdges: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_GRAPH_EDGE_DESC)
class DML_GRAPH_EDGE_DESC(Structure):
    Type: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_GRAPH_EDGE_TYPE
    Desc: VoidPtr
DML_GRAPH_EDGE_TYPE = Int32
DML_GRAPH_EDGE_TYPE_INVALID: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_GRAPH_EDGE_TYPE = 0
DML_GRAPH_EDGE_TYPE_INPUT: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_GRAPH_EDGE_TYPE = 1
DML_GRAPH_EDGE_TYPE_OUTPUT: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_GRAPH_EDGE_TYPE = 2
DML_GRAPH_EDGE_TYPE_INTERMEDIATE: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_GRAPH_EDGE_TYPE = 3
class DML_GRAPH_NODE_DESC(Structure):
    Type: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_GRAPH_NODE_TYPE
    Desc: VoidPtr
DML_GRAPH_NODE_TYPE = Int32
DML_GRAPH_NODE_TYPE_INVALID: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_GRAPH_NODE_TYPE = 0
DML_GRAPH_NODE_TYPE_OPERATOR: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_GRAPH_NODE_TYPE = 1
class DML_GRU_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    WeightTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    RecurrenceTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BiasTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    HiddenInitTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    SequenceLengthsTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputSequenceTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputSingleTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ActivationDescCount: UInt32
    ActivationDescs: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_DESC)
    Direction: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_RECURRENT_NETWORK_DIRECTION
    LinearBeforeReset: win32more.Windows.Win32.Foundation.BOOL
class DML_INPUT_GRAPH_EDGE_DESC(Structure):
    GraphInputIndex: UInt32
    ToNodeIndex: UInt32
    ToNodeInputIndex: UInt32
    Name: win32more.Windows.Win32.Foundation.PSTR
class DML_INTERMEDIATE_GRAPH_EDGE_DESC(Structure):
    FromNodeIndex: UInt32
    FromNodeOutputIndex: UInt32
    ToNodeIndex: UInt32
    ToNodeInputIndex: UInt32
    Name: win32more.Windows.Win32.Foundation.PSTR
DML_INTERPOLATION_MODE = Int32
DML_INTERPOLATION_MODE_NEAREST_NEIGHBOR: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_INTERPOLATION_MODE = 0
DML_INTERPOLATION_MODE_LINEAR: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_INTERPOLATION_MODE = 1
DML_IS_INFINITY_MODE = Int32
DML_IS_INFINITY_MODE_EITHER: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_IS_INFINITY_MODE = 0
DML_IS_INFINITY_MODE_POSITIVE: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_IS_INFINITY_MODE = 1
DML_IS_INFINITY_MODE_NEGATIVE: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_IS_INFINITY_MODE = 2
class DML_JOIN_OPERATOR_DESC(Structure):
    InputCount: UInt32
    InputTensors: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Axis: UInt32
class DML_LOCAL_RESPONSE_NORMALIZATION_GRAD_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    InputGradientTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputGradientTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    CrossChannel: win32more.Windows.Win32.Foundation.BOOL
    LocalSize: UInt32
    Alpha: Single
    Beta: Single
    Bias: Single
class DML_LOCAL_RESPONSE_NORMALIZATION_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    CrossChannel: win32more.Windows.Win32.Foundation.BOOL
    LocalSize: UInt32
    Alpha: Single
    Beta: Single
    Bias: Single
class DML_LP_NORMALIZATION_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Axis: UInt32
    Epsilon: Single
    P: UInt32
class DML_LP_POOLING_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    DimensionCount: UInt32
    Strides: POINTER(UInt32)
    WindowSize: POINTER(UInt32)
    StartPadding: POINTER(UInt32)
    EndPadding: POINTER(UInt32)
    P: UInt32
class DML_LSTM_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    WeightTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    RecurrenceTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BiasTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    HiddenInitTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    CellMemInitTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    SequenceLengthsTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    PeepholeTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputSequenceTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputSingleTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputCellSingleTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ActivationDescCount: UInt32
    ActivationDescs: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_DESC)
    Direction: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_RECURRENT_NETWORK_DIRECTION
    ClipThreshold: Single
    UseClipThreshold: win32more.Windows.Win32.Foundation.BOOL
    CoupleInputForget: win32more.Windows.Win32.Foundation.BOOL
class DML_MATRIX_MULTIPLY_INTEGER_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    AZeroPointTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BZeroPointTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
DML_MATRIX_TRANSFORM = Int32
DML_MATRIX_TRANSFORM_NONE: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_MATRIX_TRANSFORM = 0
DML_MATRIX_TRANSFORM_TRANSPOSE: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_MATRIX_TRANSFORM = 1
class DML_MAX_POOLING1_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputIndicesTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    DimensionCount: UInt32
    Strides: POINTER(UInt32)
    WindowSize: POINTER(UInt32)
    StartPadding: POINTER(UInt32)
    EndPadding: POINTER(UInt32)
class DML_MAX_POOLING2_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputIndicesTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    DimensionCount: UInt32
    Strides: POINTER(UInt32)
    WindowSize: POINTER(UInt32)
    StartPadding: POINTER(UInt32)
    EndPadding: POINTER(UInt32)
    Dilations: POINTER(UInt32)
class DML_MAX_POOLING_GRAD_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    InputGradientTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputGradientTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    DimensionCount: UInt32
    Strides: POINTER(UInt32)
    WindowSize: POINTER(UInt32)
    StartPadding: POINTER(UInt32)
    EndPadding: POINTER(UInt32)
    Dilations: POINTER(UInt32)
class DML_MAX_POOLING_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    DimensionCount: UInt32
    Strides: POINTER(UInt32)
    WindowSize: POINTER(UInt32)
    StartPadding: POINTER(UInt32)
    EndPadding: POINTER(UInt32)
class DML_MAX_UNPOOLING_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    IndicesTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_MEAN_VARIANCE_NORMALIZATION1_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BiasTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    AxisCount: UInt32
    Axes: POINTER(UInt32)
    NormalizeVariance: win32more.Windows.Win32.Foundation.BOOL
    Epsilon: Single
    FusedActivation: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_DESC)
class DML_MEAN_VARIANCE_NORMALIZATION_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BiasTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    CrossChannel: win32more.Windows.Win32.Foundation.BOOL
    NormalizeVariance: win32more.Windows.Win32.Foundation.BOOL
    Epsilon: Single
    FusedActivation: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_DESC)
class DML_NONZERO_COORDINATES_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputCountTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputCoordinatesTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_ONE_HOT_OPERATOR_DESC(Structure):
    IndicesTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ValuesTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Axis: UInt32
class DML_OPERATOR_DESC(Structure):
    Type: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE
    Desc: VoidPtr
class DML_OPERATOR_GRAPH_NODE_DESC(Structure):
    Operator: win32more.Windows.Win32.AI.MachineLearning.DirectML.IDMLOperator
    Name: win32more.Windows.Win32.Foundation.PSTR
DML_OPERATOR_TYPE = Int32
DML_OPERATOR_INVALID: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 0
DML_OPERATOR_ELEMENT_WISE_IDENTITY: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 1
DML_OPERATOR_ELEMENT_WISE_ABS: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 2
DML_OPERATOR_ELEMENT_WISE_ACOS: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 3
DML_OPERATOR_ELEMENT_WISE_ADD: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 4
DML_OPERATOR_ELEMENT_WISE_ASIN: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 5
DML_OPERATOR_ELEMENT_WISE_ATAN: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 6
DML_OPERATOR_ELEMENT_WISE_CEIL: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 7
DML_OPERATOR_ELEMENT_WISE_CLIP: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 8
DML_OPERATOR_ELEMENT_WISE_COS: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 9
DML_OPERATOR_ELEMENT_WISE_DIVIDE: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 10
DML_OPERATOR_ELEMENT_WISE_EXP: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 11
DML_OPERATOR_ELEMENT_WISE_FLOOR: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 12
DML_OPERATOR_ELEMENT_WISE_LOG: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 13
DML_OPERATOR_ELEMENT_WISE_LOGICAL_AND: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 14
DML_OPERATOR_ELEMENT_WISE_LOGICAL_EQUALS: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 15
DML_OPERATOR_ELEMENT_WISE_LOGICAL_GREATER_THAN: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 16
DML_OPERATOR_ELEMENT_WISE_LOGICAL_LESS_THAN: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 17
DML_OPERATOR_ELEMENT_WISE_LOGICAL_NOT: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 18
DML_OPERATOR_ELEMENT_WISE_LOGICAL_OR: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 19
DML_OPERATOR_ELEMENT_WISE_LOGICAL_XOR: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 20
DML_OPERATOR_ELEMENT_WISE_MAX: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 21
DML_OPERATOR_ELEMENT_WISE_MEAN: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 22
DML_OPERATOR_ELEMENT_WISE_MIN: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 23
DML_OPERATOR_ELEMENT_WISE_MULTIPLY: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 24
DML_OPERATOR_ELEMENT_WISE_POW: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 25
DML_OPERATOR_ELEMENT_WISE_CONSTANT_POW: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 26
DML_OPERATOR_ELEMENT_WISE_RECIP: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 27
DML_OPERATOR_ELEMENT_WISE_SIN: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 28
DML_OPERATOR_ELEMENT_WISE_SQRT: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 29
DML_OPERATOR_ELEMENT_WISE_SUBTRACT: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 30
DML_OPERATOR_ELEMENT_WISE_TAN: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 31
DML_OPERATOR_ELEMENT_WISE_THRESHOLD: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 32
DML_OPERATOR_ELEMENT_WISE_QUANTIZE_LINEAR: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 33
DML_OPERATOR_ELEMENT_WISE_DEQUANTIZE_LINEAR: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 34
DML_OPERATOR_ACTIVATION_ELU: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 35
DML_OPERATOR_ACTIVATION_HARDMAX: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 36
DML_OPERATOR_ACTIVATION_HARD_SIGMOID: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 37
DML_OPERATOR_ACTIVATION_IDENTITY: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 38
DML_OPERATOR_ACTIVATION_LEAKY_RELU: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 39
DML_OPERATOR_ACTIVATION_LINEAR: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 40
DML_OPERATOR_ACTIVATION_LOG_SOFTMAX: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 41
DML_OPERATOR_ACTIVATION_PARAMETERIZED_RELU: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 42
DML_OPERATOR_ACTIVATION_PARAMETRIC_SOFTPLUS: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 43
DML_OPERATOR_ACTIVATION_RELU: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 44
DML_OPERATOR_ACTIVATION_SCALED_ELU: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 45
DML_OPERATOR_ACTIVATION_SCALED_TANH: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 46
DML_OPERATOR_ACTIVATION_SIGMOID: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 47
DML_OPERATOR_ACTIVATION_SOFTMAX: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 48
DML_OPERATOR_ACTIVATION_SOFTPLUS: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 49
DML_OPERATOR_ACTIVATION_SOFTSIGN: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 50
DML_OPERATOR_ACTIVATION_TANH: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 51
DML_OPERATOR_ACTIVATION_THRESHOLDED_RELU: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 52
DML_OPERATOR_CONVOLUTION: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 53
DML_OPERATOR_GEMM: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 54
DML_OPERATOR_REDUCE: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 55
DML_OPERATOR_AVERAGE_POOLING: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 56
DML_OPERATOR_LP_POOLING: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 57
DML_OPERATOR_MAX_POOLING: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 58
DML_OPERATOR_ROI_POOLING: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 59
DML_OPERATOR_SLICE: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 60
DML_OPERATOR_CAST: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 61
DML_OPERATOR_SPLIT: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 62
DML_OPERATOR_JOIN: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 63
DML_OPERATOR_PADDING: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 64
DML_OPERATOR_VALUE_SCALE_2D: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 65
DML_OPERATOR_UPSAMPLE_2D: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 66
DML_OPERATOR_GATHER: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 67
DML_OPERATOR_SPACE_TO_DEPTH: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 68
DML_OPERATOR_DEPTH_TO_SPACE: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 69
DML_OPERATOR_TILE: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 70
DML_OPERATOR_TOP_K: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 71
DML_OPERATOR_BATCH_NORMALIZATION: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 72
DML_OPERATOR_MEAN_VARIANCE_NORMALIZATION: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 73
DML_OPERATOR_LOCAL_RESPONSE_NORMALIZATION: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 74
DML_OPERATOR_LP_NORMALIZATION: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 75
DML_OPERATOR_RNN: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 76
DML_OPERATOR_LSTM: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 77
DML_OPERATOR_GRU: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 78
DML_OPERATOR_ELEMENT_WISE_SIGN: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 79
DML_OPERATOR_ELEMENT_WISE_IS_NAN: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 80
DML_OPERATOR_ELEMENT_WISE_ERF: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 81
DML_OPERATOR_ELEMENT_WISE_SINH: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 82
DML_OPERATOR_ELEMENT_WISE_COSH: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 83
DML_OPERATOR_ELEMENT_WISE_TANH: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 84
DML_OPERATOR_ELEMENT_WISE_ASINH: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 85
DML_OPERATOR_ELEMENT_WISE_ACOSH: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 86
DML_OPERATOR_ELEMENT_WISE_ATANH: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 87
DML_OPERATOR_ELEMENT_WISE_IF: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 88
DML_OPERATOR_ELEMENT_WISE_ADD1: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 89
DML_OPERATOR_ACTIVATION_SHRINK: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 90
DML_OPERATOR_MAX_POOLING1: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 91
DML_OPERATOR_MAX_UNPOOLING: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 92
DML_OPERATOR_DIAGONAL_MATRIX: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 93
DML_OPERATOR_SCATTER_ELEMENTS: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 94
DML_OPERATOR_SCATTER: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 94
DML_OPERATOR_ONE_HOT: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 95
DML_OPERATOR_RESAMPLE: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 96
DML_OPERATOR_ELEMENT_WISE_BIT_SHIFT_LEFT: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 97
DML_OPERATOR_ELEMENT_WISE_BIT_SHIFT_RIGHT: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 98
DML_OPERATOR_ELEMENT_WISE_ROUND: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 99
DML_OPERATOR_ELEMENT_WISE_IS_INFINITY: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 100
DML_OPERATOR_ELEMENT_WISE_MODULUS_TRUNCATE: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 101
DML_OPERATOR_ELEMENT_WISE_MODULUS_FLOOR: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 102
DML_OPERATOR_FILL_VALUE_CONSTANT: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 103
DML_OPERATOR_FILL_VALUE_SEQUENCE: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 104
DML_OPERATOR_CUMULATIVE_SUMMATION: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 105
DML_OPERATOR_REVERSE_SUBSEQUENCES: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 106
DML_OPERATOR_GATHER_ELEMENTS: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 107
DML_OPERATOR_GATHER_ND: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 108
DML_OPERATOR_SCATTER_ND: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 109
DML_OPERATOR_MAX_POOLING2: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 110
DML_OPERATOR_SLICE1: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 111
DML_OPERATOR_TOP_K1: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 112
DML_OPERATOR_DEPTH_TO_SPACE1: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 113
DML_OPERATOR_SPACE_TO_DEPTH1: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 114
DML_OPERATOR_MEAN_VARIANCE_NORMALIZATION1: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 115
DML_OPERATOR_RESAMPLE1: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 116
DML_OPERATOR_MATRIX_MULTIPLY_INTEGER: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 117
DML_OPERATOR_QUANTIZED_LINEAR_MATRIX_MULTIPLY: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 118
DML_OPERATOR_CONVOLUTION_INTEGER: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 119
DML_OPERATOR_QUANTIZED_LINEAR_CONVOLUTION: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 120
DML_OPERATOR_ELEMENT_WISE_BIT_AND: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 121
DML_OPERATOR_ELEMENT_WISE_BIT_OR: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 122
DML_OPERATOR_ELEMENT_WISE_BIT_XOR: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 123
DML_OPERATOR_ELEMENT_WISE_BIT_NOT: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 124
DML_OPERATOR_ELEMENT_WISE_BIT_COUNT: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 125
DML_OPERATOR_ELEMENT_WISE_LOGICAL_GREATER_THAN_OR_EQUAL: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 126
DML_OPERATOR_ELEMENT_WISE_LOGICAL_LESS_THAN_OR_EQUAL: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 127
DML_OPERATOR_ACTIVATION_CELU: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 128
DML_OPERATOR_ACTIVATION_RELU_GRAD: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 129
DML_OPERATOR_AVERAGE_POOLING_GRAD: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 130
DML_OPERATOR_MAX_POOLING_GRAD: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 131
DML_OPERATOR_RANDOM_GENERATOR: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 132
DML_OPERATOR_NONZERO_COORDINATES: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 133
DML_OPERATOR_RESAMPLE_GRAD: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 134
DML_OPERATOR_SLICE_GRAD: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 135
DML_OPERATOR_ADAM_OPTIMIZER: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 136
DML_OPERATOR_ARGMIN: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 137
DML_OPERATOR_ARGMAX: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 138
DML_OPERATOR_ROI_ALIGN: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 139
DML_OPERATOR_GATHER_ND1: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 140
DML_OPERATOR_ELEMENT_WISE_ATAN_YX: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 141
DML_OPERATOR_ELEMENT_WISE_CLIP_GRAD: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 142
DML_OPERATOR_ELEMENT_WISE_DIFFERENCE_SQUARE: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 143
DML_OPERATOR_LOCAL_RESPONSE_NORMALIZATION_GRAD: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 144
DML_OPERATOR_CUMULATIVE_PRODUCT: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 145
DML_OPERATOR_BATCH_NORMALIZATION_GRAD: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 146
DML_OPERATOR_ELEMENT_WISE_QUANTIZED_LINEAR_ADD: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 147
DML_OPERATOR_DYNAMIC_QUANTIZE_LINEAR: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 148
DML_OPERATOR_ROI_ALIGN1: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_TYPE = 149
class DML_OUTPUT_GRAPH_EDGE_DESC(Structure):
    FromNodeIndex: UInt32
    FromNodeOutputIndex: UInt32
    GraphOutputIndex: UInt32
    Name: win32more.Windows.Win32.Foundation.PSTR
DML_PADDING_MODE = Int32
DML_PADDING_MODE_CONSTANT: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_PADDING_MODE = 0
DML_PADDING_MODE_EDGE: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_PADDING_MODE = 1
DML_PADDING_MODE_REFLECTION: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_PADDING_MODE = 2
DML_PADDING_MODE_SYMMETRIC: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_PADDING_MODE = 3
class DML_PADDING_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    PaddingMode: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_PADDING_MODE
    PaddingValue: Single
    DimensionCount: UInt32
    StartPadding: POINTER(UInt32)
    EndPadding: POINTER(UInt32)
class DML_QUANTIZED_LINEAR_CONVOLUTION_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    InputScaleTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    InputZeroPointTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    FilterTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    FilterScaleTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    FilterZeroPointTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BiasTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputScaleTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputZeroPointTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    DimensionCount: UInt32
    Strides: POINTER(UInt32)
    Dilations: POINTER(UInt32)
    StartPadding: POINTER(UInt32)
    EndPadding: POINTER(UInt32)
    GroupCount: UInt32
class DML_QUANTIZED_LINEAR_MATRIX_MULTIPLY_OPERATOR_DESC(Structure):
    ATensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    AScaleTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    AZeroPointTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BScaleTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BZeroPointTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputScaleTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputZeroPointTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
class DML_RANDOM_GENERATOR_OPERATOR_DESC(Structure):
    InputStateTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputStateTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Type: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_RANDOM_GENERATOR_TYPE
DML_RANDOM_GENERATOR_TYPE = Int32
DML_RANDOM_GENERATOR_TYPE_PHILOX_4X32_10: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_RANDOM_GENERATOR_TYPE = 0
DML_RECURRENT_NETWORK_DIRECTION = Int32
DML_RECURRENT_NETWORK_DIRECTION_FORWARD: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_RECURRENT_NETWORK_DIRECTION = 0
DML_RECURRENT_NETWORK_DIRECTION_BACKWARD: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_RECURRENT_NETWORK_DIRECTION = 1
DML_RECURRENT_NETWORK_DIRECTION_BIDIRECTIONAL: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_RECURRENT_NETWORK_DIRECTION = 2
DML_REDUCE_FUNCTION = Int32
DML_REDUCE_FUNCTION_ARGMAX: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_REDUCE_FUNCTION = 0
DML_REDUCE_FUNCTION_ARGMIN: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_REDUCE_FUNCTION = 1
DML_REDUCE_FUNCTION_AVERAGE: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_REDUCE_FUNCTION = 2
DML_REDUCE_FUNCTION_L1: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_REDUCE_FUNCTION = 3
DML_REDUCE_FUNCTION_L2: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_REDUCE_FUNCTION = 4
DML_REDUCE_FUNCTION_LOG_SUM: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_REDUCE_FUNCTION = 5
DML_REDUCE_FUNCTION_LOG_SUM_EXP: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_REDUCE_FUNCTION = 6
DML_REDUCE_FUNCTION_MAX: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_REDUCE_FUNCTION = 7
DML_REDUCE_FUNCTION_MIN: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_REDUCE_FUNCTION = 8
DML_REDUCE_FUNCTION_MULTIPLY: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_REDUCE_FUNCTION = 9
DML_REDUCE_FUNCTION_SUM: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_REDUCE_FUNCTION = 10
DML_REDUCE_FUNCTION_SUM_SQUARE: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_REDUCE_FUNCTION = 11
class DML_REDUCE_OPERATOR_DESC(Structure):
    Function: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_REDUCE_FUNCTION
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    AxisCount: UInt32
    Axes: POINTER(UInt32)
class DML_RESAMPLE1_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    InterpolationMode: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_INTERPOLATION_MODE
    DimensionCount: UInt32
    Scales: POINTER(Single)
    InputPixelOffsets: POINTER(Single)
    OutputPixelOffsets: POINTER(Single)
class DML_RESAMPLE_GRAD_OPERATOR_DESC(Structure):
    InputGradientTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputGradientTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    InterpolationMode: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_INTERPOLATION_MODE
    DimensionCount: UInt32
    Scales: POINTER(Single)
    InputPixelOffsets: POINTER(Single)
    OutputPixelOffsets: POINTER(Single)
class DML_RESAMPLE_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    InterpolationMode: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_INTERPOLATION_MODE
    ScaleCount: UInt32
    Scales: POINTER(Single)
class DML_REVERSE_SUBSEQUENCES_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    SequenceLengthsTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Axis: UInt32
class DML_RNN_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    WeightTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    RecurrenceTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BiasTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    HiddenInitTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    SequenceLengthsTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputSequenceTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputSingleTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ActivationDescCount: UInt32
    ActivationDescs: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_DESC)
    Direction: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_RECURRENT_NETWORK_DIRECTION
class DML_ROI_ALIGN1_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ROITensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BatchIndicesTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ReductionFunction: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_REDUCE_FUNCTION
    InterpolationMode: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_INTERPOLATION_MODE
    SpatialScaleX: Single
    SpatialScaleY: Single
    InputPixelOffset: Single
    OutputPixelOffset: Single
    OutOfBoundsInputValue: Single
    MinimumSamplesPerOutput: UInt32
    MaximumSamplesPerOutput: UInt32
    AlignRegionsToCorners: win32more.Windows.Win32.Foundation.BOOL
class DML_ROI_ALIGN_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ROITensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BatchIndicesTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ReductionFunction: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_REDUCE_FUNCTION
    InterpolationMode: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_INTERPOLATION_MODE
    SpatialScaleX: Single
    SpatialScaleY: Single
    OutOfBoundsInputValue: Single
    MinimumSamplesPerOutput: UInt32
    MaximumSamplesPerOutput: UInt32
class DML_ROI_POOLING_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ROITensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    SpatialScale: Single
    PooledSize: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SIZE_2D
DML_ROUNDING_MODE = Int32
DML_ROUNDING_MODE_HALVES_TO_NEAREST_EVEN: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_ROUNDING_MODE = 0
DML_ROUNDING_MODE_TOWARD_ZERO: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_ROUNDING_MODE = 1
DML_ROUNDING_MODE_TOWARD_INFINITY: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_ROUNDING_MODE = 2
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
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    IndicesTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    UpdatesTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    InputDimensionCount: UInt32
    IndicesDimensionCount: UInt32
class DML_SCATTER_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    IndicesTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    UpdatesTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Axis: UInt32
class DML_SIZE_2D(Structure):
    Width: UInt32
    Height: UInt32
class DML_SLICE1_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    DimensionCount: UInt32
    InputWindowOffsets: POINTER(UInt32)
    InputWindowSizes: POINTER(UInt32)
    InputWindowStrides: POINTER(Int32)
class DML_SLICE_GRAD_OPERATOR_DESC(Structure):
    InputGradientTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputGradientTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    DimensionCount: UInt32
    InputWindowOffsets: POINTER(UInt32)
    InputWindowSizes: POINTER(UInt32)
    InputWindowStrides: POINTER(Int32)
class DML_SLICE_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    DimensionCount: UInt32
    Offsets: POINTER(UInt32)
    Sizes: POINTER(UInt32)
    Strides: POINTER(UInt32)
class DML_SPACE_TO_DEPTH1_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BlockSize: UInt32
    Order: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_DEPTH_SPACE_ORDER
class DML_SPACE_TO_DEPTH_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    BlockSize: UInt32
class DML_SPLIT_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputCount: UInt32
    OutputTensors: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Axis: UInt32
DML_TENSOR_DATA_TYPE = Int32
DML_TENSOR_DATA_TYPE_UNKNOWN: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DATA_TYPE = 0
DML_TENSOR_DATA_TYPE_FLOAT32: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DATA_TYPE = 1
DML_TENSOR_DATA_TYPE_FLOAT16: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DATA_TYPE = 2
DML_TENSOR_DATA_TYPE_UINT32: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DATA_TYPE = 3
DML_TENSOR_DATA_TYPE_UINT16: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DATA_TYPE = 4
DML_TENSOR_DATA_TYPE_UINT8: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DATA_TYPE = 5
DML_TENSOR_DATA_TYPE_INT32: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DATA_TYPE = 6
DML_TENSOR_DATA_TYPE_INT16: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DATA_TYPE = 7
DML_TENSOR_DATA_TYPE_INT8: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DATA_TYPE = 8
DML_TENSOR_DATA_TYPE_FLOAT64: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DATA_TYPE = 9
DML_TENSOR_DATA_TYPE_UINT64: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DATA_TYPE = 10
DML_TENSOR_DATA_TYPE_INT64: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DATA_TYPE = 11
class DML_TENSOR_DESC(Structure):
    Type: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_TYPE
    Desc: VoidPtr
DML_TENSOR_FLAGS = Int32
DML_TENSOR_FLAG_NONE: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_FLAGS = 0
DML_TENSOR_FLAG_OWNED_BY_DML: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_FLAGS = 1
DML_TENSOR_TYPE = Int32
DML_TENSOR_TYPE_INVALID: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_TYPE = 0
DML_TENSOR_TYPE_BUFFER: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_TYPE = 1
class DML_TILE_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    RepeatsCount: UInt32
    Repeats: POINTER(UInt32)
class DML_TOP_K1_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputValueTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputIndexTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Axis: UInt32
    K: UInt32
    AxisDirection: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_AXIS_DIRECTION
class DML_TOP_K_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputValueTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputIndexTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Axis: UInt32
    K: UInt32
class DML_UPSAMPLE_2D_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    ScaleSize: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_SIZE_2D
    InterpolationMode: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_INTERPOLATION_MODE
class DML_VALUE_SCALE_2D_OPERATOR_DESC(Structure):
    InputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    OutputTensor: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_TENSOR_DESC)
    Scale: Single
    ChannelCount: UInt32
    Bias: POINTER(Single)
class IDMLBindingTable(ComPtr):
    extends: win32more.Windows.Win32.AI.MachineLearning.DirectML.IDMLDeviceChild
    _iid_ = Guid('{29c687dc-de74-4e3b-ab00-1168f2fc3cfc}')
    @commethod(8)
    def BindInputs(self, bindingCount: UInt32, bindings: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_BINDING_DESC)) -> Void: ...
    @commethod(9)
    def BindOutputs(self, bindingCount: UInt32, bindings: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_BINDING_DESC)) -> Void: ...
    @commethod(10)
    def BindTemporaryResource(self, binding: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_BINDING_DESC)) -> Void: ...
    @commethod(11)
    def BindPersistentResource(self, binding: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_BINDING_DESC)) -> Void: ...
    @commethod(12)
    def Reset(self, desc: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_BINDING_TABLE_DESC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDMLCommandRecorder(ComPtr):
    extends: win32more.Windows.Win32.AI.MachineLearning.DirectML.IDMLDeviceChild
    _iid_ = Guid('{e6857a76-2e3e-4fdd-bff4-5d2ba10fb453}')
    @commethod(8)
    def RecordDispatch(self, commandList: win32more.Windows.Win32.Graphics.Direct3D12.ID3D12CommandList, dispatchable: win32more.Windows.Win32.AI.MachineLearning.DirectML.IDMLDispatchable, bindings: win32more.Windows.Win32.AI.MachineLearning.DirectML.IDMLBindingTable) -> Void: ...
class IDMLCompiledOperator(ComPtr):
    extends: win32more.Windows.Win32.AI.MachineLearning.DirectML.IDMLDispatchable
    _iid_ = Guid('{6b15e56a-bf5c-4902-92d8-da3a650afea4}')
class IDMLDebugDevice(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7d6f3ac9-394a-4ac3-92a7-390cc57a8217}')
    @commethod(3)
    def SetMuteDebugOutput(self, mute: win32more.Windows.Win32.Foundation.BOOL) -> Void: ...
class IDMLDevice(ComPtr):
    extends: win32more.Windows.Win32.AI.MachineLearning.DirectML.IDMLObject
    _iid_ = Guid('{6dbd6437-96fd-423f-a98c-ae5e7c2a573f}')
    @commethod(7)
    def CheckFeatureSupport(self, feature: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_FEATURE, featureQueryDataSize: UInt32, featureQueryData: VoidPtr, featureSupportDataSize: UInt32, featureSupportData: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateOperator(self, desc: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_OPERATOR_DESC), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CompileOperator(self, op: win32more.Windows.Win32.AI.MachineLearning.DirectML.IDMLOperator, flags: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_EXECUTION_FLAGS, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CreateOperatorInitializer(self, operatorCount: UInt32, operators: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.IDMLCompiledOperator), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CreateCommandRecorder(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CreateBindingTable(self, desc: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_BINDING_TABLE_DESC), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Evict(self, count: UInt32, ppObjects: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.IDMLPageable)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def MakeResident(self, count: UInt32, ppObjects: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.IDMLPageable)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetDeviceRemovedReason(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetParentDevice(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDMLDevice1(ComPtr):
    extends: win32more.Windows.Win32.AI.MachineLearning.DirectML.IDMLDevice
    _iid_ = Guid('{a0884f9a-d2be-4355-aa5d-5901281ad1d2}')
    @commethod(17)
    def CompileGraph(self, desc: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_GRAPH_DESC), flags: win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_EXECUTION_FLAGS, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDMLDeviceChild(ComPtr):
    extends: win32more.Windows.Win32.AI.MachineLearning.DirectML.IDMLObject
    _iid_ = Guid('{27e83142-8165-49e3-974e-2fd66e4cb69d}')
    @commethod(7)
    def GetDevice(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDMLDispatchable(ComPtr):
    extends: win32more.Windows.Win32.AI.MachineLearning.DirectML.IDMLPageable
    _iid_ = Guid('{dcb821a8-1039-441e-9f1c-b1759c2f3cec}')
    @commethod(8)
    def GetBindingProperties(self) -> win32more.Windows.Win32.AI.MachineLearning.DirectML.DML_BINDING_PROPERTIES: ...
class IDMLObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c8263aac-9e0c-4a2d-9b8e-007521a3317c}')
    @commethod(3)
    def GetPrivateData(self, guid: POINTER(Guid), dataSize: POINTER(UInt32), data: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPrivateData(self, guid: POINTER(Guid), dataSize: UInt32, data: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetPrivateDataInterface(self, guid: POINTER(Guid), data: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetName(self, name: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDMLOperator(ComPtr):
    extends: win32more.Windows.Win32.AI.MachineLearning.DirectML.IDMLDeviceChild
    _iid_ = Guid('{26caae7a-3081-4633-9581-226fbe57695d}')
class IDMLOperatorInitializer(ComPtr):
    extends: win32more.Windows.Win32.AI.MachineLearning.DirectML.IDMLDispatchable
    _iid_ = Guid('{427c1113-435c-469c-8676-4d5dd072f813}')
    @commethod(9)
    def Reset(self, operatorCount: UInt32, operators: POINTER(win32more.Windows.Win32.AI.MachineLearning.DirectML.IDMLCompiledOperator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDMLPageable(ComPtr):
    extends: win32more.Windows.Win32.AI.MachineLearning.DirectML.IDMLDeviceChild
    _iid_ = Guid('{b1ab0825-4542-4a4b-8617-6dde6e8f6201}')


make_ready(__name__)
