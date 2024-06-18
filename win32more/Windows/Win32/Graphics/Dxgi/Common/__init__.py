from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Dxgi.Common
_FACDXGI: UInt32 = 2170
DXGI_CPU_ACCESS_NONE: UInt32 = 0
DXGI_CPU_ACCESS_DYNAMIC: UInt32 = 1
DXGI_CPU_ACCESS_READ_WRITE: UInt32 = 2
DXGI_CPU_ACCESS_SCRATCH: UInt32 = 3
DXGI_CPU_ACCESS_FIELD: UInt32 = 15
DXGI_FORMAT_DEFINED: UInt32 = 1
DXGI_STANDARD_MULTISAMPLE_QUALITY_PATTERN: UInt32 = 4294967295
DXGI_CENTER_MULTISAMPLE_QUALITY_PATTERN: UInt32 = 4294967294
DXGI_ALPHA_MODE = Int32
DXGI_ALPHA_MODE_UNSPECIFIED: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_ALPHA_MODE = 0
DXGI_ALPHA_MODE_PREMULTIPLIED: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_ALPHA_MODE = 1
DXGI_ALPHA_MODE_STRAIGHT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_ALPHA_MODE = 2
DXGI_ALPHA_MODE_IGNORE: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_ALPHA_MODE = 3
DXGI_COLOR_SPACE_TYPE = Int32
DXGI_COLOR_SPACE_RGB_FULL_G22_NONE_P709: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE = 0
DXGI_COLOR_SPACE_RGB_FULL_G10_NONE_P709: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE = 1
DXGI_COLOR_SPACE_RGB_STUDIO_G22_NONE_P709: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE = 2
DXGI_COLOR_SPACE_RGB_STUDIO_G22_NONE_P2020: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE = 3
DXGI_COLOR_SPACE_RESERVED: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE = 4
DXGI_COLOR_SPACE_YCBCR_FULL_G22_NONE_P709_X601: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE = 5
DXGI_COLOR_SPACE_YCBCR_STUDIO_G22_LEFT_P601: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE = 6
DXGI_COLOR_SPACE_YCBCR_FULL_G22_LEFT_P601: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE = 7
DXGI_COLOR_SPACE_YCBCR_STUDIO_G22_LEFT_P709: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE = 8
DXGI_COLOR_SPACE_YCBCR_FULL_G22_LEFT_P709: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE = 9
DXGI_COLOR_SPACE_YCBCR_STUDIO_G22_LEFT_P2020: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE = 10
DXGI_COLOR_SPACE_YCBCR_FULL_G22_LEFT_P2020: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE = 11
DXGI_COLOR_SPACE_RGB_FULL_G2084_NONE_P2020: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE = 12
DXGI_COLOR_SPACE_YCBCR_STUDIO_G2084_LEFT_P2020: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE = 13
DXGI_COLOR_SPACE_RGB_STUDIO_G2084_NONE_P2020: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE = 14
DXGI_COLOR_SPACE_YCBCR_STUDIO_G22_TOPLEFT_P2020: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE = 15
DXGI_COLOR_SPACE_YCBCR_STUDIO_G2084_TOPLEFT_P2020: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE = 16
DXGI_COLOR_SPACE_RGB_FULL_G22_NONE_P2020: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE = 17
DXGI_COLOR_SPACE_YCBCR_STUDIO_GHLG_TOPLEFT_P2020: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE = 18
DXGI_COLOR_SPACE_YCBCR_FULL_GHLG_TOPLEFT_P2020: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE = 19
DXGI_COLOR_SPACE_RGB_STUDIO_G24_NONE_P709: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE = 20
DXGI_COLOR_SPACE_RGB_STUDIO_G24_NONE_P2020: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE = 21
DXGI_COLOR_SPACE_YCBCR_STUDIO_G24_LEFT_P709: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE = 22
DXGI_COLOR_SPACE_YCBCR_STUDIO_G24_LEFT_P2020: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE = 23
DXGI_COLOR_SPACE_YCBCR_STUDIO_G24_TOPLEFT_P2020: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE = 24
DXGI_COLOR_SPACE_CUSTOM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE = -1
DXGI_FORMAT = Int32
DXGI_FORMAT_UNKNOWN: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 0
DXGI_FORMAT_R32G32B32A32_TYPELESS: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 1
DXGI_FORMAT_R32G32B32A32_FLOAT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 2
DXGI_FORMAT_R32G32B32A32_UINT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 3
DXGI_FORMAT_R32G32B32A32_SINT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 4
DXGI_FORMAT_R32G32B32_TYPELESS: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 5
DXGI_FORMAT_R32G32B32_FLOAT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 6
DXGI_FORMAT_R32G32B32_UINT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 7
DXGI_FORMAT_R32G32B32_SINT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 8
DXGI_FORMAT_R16G16B16A16_TYPELESS: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 9
DXGI_FORMAT_R16G16B16A16_FLOAT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 10
DXGI_FORMAT_R16G16B16A16_UNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 11
DXGI_FORMAT_R16G16B16A16_UINT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 12
DXGI_FORMAT_R16G16B16A16_SNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 13
DXGI_FORMAT_R16G16B16A16_SINT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 14
DXGI_FORMAT_R32G32_TYPELESS: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 15
DXGI_FORMAT_R32G32_FLOAT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 16
DXGI_FORMAT_R32G32_UINT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 17
DXGI_FORMAT_R32G32_SINT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 18
DXGI_FORMAT_R32G8X24_TYPELESS: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 19
DXGI_FORMAT_D32_FLOAT_S8X24_UINT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 20
DXGI_FORMAT_R32_FLOAT_X8X24_TYPELESS: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 21
DXGI_FORMAT_X32_TYPELESS_G8X24_UINT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 22
DXGI_FORMAT_R10G10B10A2_TYPELESS: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 23
DXGI_FORMAT_R10G10B10A2_UNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 24
DXGI_FORMAT_R10G10B10A2_UINT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 25
DXGI_FORMAT_R11G11B10_FLOAT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 26
DXGI_FORMAT_R8G8B8A8_TYPELESS: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 27
DXGI_FORMAT_R8G8B8A8_UNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 28
DXGI_FORMAT_R8G8B8A8_UNORM_SRGB: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 29
DXGI_FORMAT_R8G8B8A8_UINT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 30
DXGI_FORMAT_R8G8B8A8_SNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 31
DXGI_FORMAT_R8G8B8A8_SINT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 32
DXGI_FORMAT_R16G16_TYPELESS: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 33
DXGI_FORMAT_R16G16_FLOAT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 34
DXGI_FORMAT_R16G16_UNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 35
DXGI_FORMAT_R16G16_UINT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 36
DXGI_FORMAT_R16G16_SNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 37
DXGI_FORMAT_R16G16_SINT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 38
DXGI_FORMAT_R32_TYPELESS: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 39
DXGI_FORMAT_D32_FLOAT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 40
DXGI_FORMAT_R32_FLOAT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 41
DXGI_FORMAT_R32_UINT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 42
DXGI_FORMAT_R32_SINT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 43
DXGI_FORMAT_R24G8_TYPELESS: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 44
DXGI_FORMAT_D24_UNORM_S8_UINT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 45
DXGI_FORMAT_R24_UNORM_X8_TYPELESS: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 46
DXGI_FORMAT_X24_TYPELESS_G8_UINT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 47
DXGI_FORMAT_R8G8_TYPELESS: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 48
DXGI_FORMAT_R8G8_UNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 49
DXGI_FORMAT_R8G8_UINT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 50
DXGI_FORMAT_R8G8_SNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 51
DXGI_FORMAT_R8G8_SINT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 52
DXGI_FORMAT_R16_TYPELESS: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 53
DXGI_FORMAT_R16_FLOAT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 54
DXGI_FORMAT_D16_UNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 55
DXGI_FORMAT_R16_UNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 56
DXGI_FORMAT_R16_UINT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 57
DXGI_FORMAT_R16_SNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 58
DXGI_FORMAT_R16_SINT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 59
DXGI_FORMAT_R8_TYPELESS: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 60
DXGI_FORMAT_R8_UNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 61
DXGI_FORMAT_R8_UINT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 62
DXGI_FORMAT_R8_SNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 63
DXGI_FORMAT_R8_SINT: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 64
DXGI_FORMAT_A8_UNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 65
DXGI_FORMAT_R1_UNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 66
DXGI_FORMAT_R9G9B9E5_SHAREDEXP: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 67
DXGI_FORMAT_R8G8_B8G8_UNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 68
DXGI_FORMAT_G8R8_G8B8_UNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 69
DXGI_FORMAT_BC1_TYPELESS: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 70
DXGI_FORMAT_BC1_UNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 71
DXGI_FORMAT_BC1_UNORM_SRGB: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 72
DXGI_FORMAT_BC2_TYPELESS: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 73
DXGI_FORMAT_BC2_UNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 74
DXGI_FORMAT_BC2_UNORM_SRGB: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 75
DXGI_FORMAT_BC3_TYPELESS: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 76
DXGI_FORMAT_BC3_UNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 77
DXGI_FORMAT_BC3_UNORM_SRGB: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 78
DXGI_FORMAT_BC4_TYPELESS: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 79
DXGI_FORMAT_BC4_UNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 80
DXGI_FORMAT_BC4_SNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 81
DXGI_FORMAT_BC5_TYPELESS: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 82
DXGI_FORMAT_BC5_UNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 83
DXGI_FORMAT_BC5_SNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 84
DXGI_FORMAT_B5G6R5_UNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 85
DXGI_FORMAT_B5G5R5A1_UNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 86
DXGI_FORMAT_B8G8R8A8_UNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 87
DXGI_FORMAT_B8G8R8X8_UNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 88
DXGI_FORMAT_R10G10B10_XR_BIAS_A2_UNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 89
DXGI_FORMAT_B8G8R8A8_TYPELESS: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 90
DXGI_FORMAT_B8G8R8A8_UNORM_SRGB: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 91
DXGI_FORMAT_B8G8R8X8_TYPELESS: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 92
DXGI_FORMAT_B8G8R8X8_UNORM_SRGB: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 93
DXGI_FORMAT_BC6H_TYPELESS: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 94
DXGI_FORMAT_BC6H_UF16: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 95
DXGI_FORMAT_BC6H_SF16: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 96
DXGI_FORMAT_BC7_TYPELESS: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 97
DXGI_FORMAT_BC7_UNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 98
DXGI_FORMAT_BC7_UNORM_SRGB: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 99
DXGI_FORMAT_AYUV: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 100
DXGI_FORMAT_Y410: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 101
DXGI_FORMAT_Y416: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 102
DXGI_FORMAT_NV12: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 103
DXGI_FORMAT_P010: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 104
DXGI_FORMAT_P016: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 105
DXGI_FORMAT_420_OPAQUE: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 106
DXGI_FORMAT_YUY2: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 107
DXGI_FORMAT_Y210: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 108
DXGI_FORMAT_Y216: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 109
DXGI_FORMAT_NV11: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 110
DXGI_FORMAT_AI44: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 111
DXGI_FORMAT_IA44: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 112
DXGI_FORMAT_P8: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 113
DXGI_FORMAT_A8P8: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 114
DXGI_FORMAT_B4G4R4A4_UNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 115
DXGI_FORMAT_P208: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 130
DXGI_FORMAT_V208: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 131
DXGI_FORMAT_V408: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 132
DXGI_FORMAT_SAMPLER_FEEDBACK_MIN_MIP_OPAQUE: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 189
DXGI_FORMAT_SAMPLER_FEEDBACK_MIP_REGION_USED_OPAQUE: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 190
DXGI_FORMAT_A4B4G4R4_UNORM: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT = 191
class DXGI_GAMMA_CONTROL(Structure):
    Scale: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_RGB
    Offset: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_RGB
    GammaCurve: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_RGB * 1025
class DXGI_GAMMA_CONTROL_CAPABILITIES(Structure):
    ScaleAndOffsetSupported: win32more.Windows.Win32.Foundation.BOOL
    MaxConvertedValue: Single
    MinConvertedValue: Single
    NumGammaControlPoints: UInt32
    ControlPointPositions: Single * 1025
class DXGI_JPEG_AC_HUFFMAN_TABLE(Structure):
    CodeCounts: Byte * 16
    CodeValues: Byte * 162
class DXGI_JPEG_DC_HUFFMAN_TABLE(Structure):
    CodeCounts: Byte * 12
    CodeValues: Byte * 12
class DXGI_JPEG_QUANTIZATION_TABLE(Structure):
    Elements: Byte * 64
class DXGI_MODE_DESC(Structure):
    Width: UInt32
    Height: UInt32
    RefreshRate: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_RATIONAL
    Format: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT
    ScanlineOrdering: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_SCANLINE_ORDER
    Scaling: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_SCALING
DXGI_MODE_ROTATION = Int32
DXGI_MODE_ROTATION_UNSPECIFIED: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_ROTATION = 0
DXGI_MODE_ROTATION_IDENTITY: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_ROTATION = 1
DXGI_MODE_ROTATION_ROTATE90: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_ROTATION = 2
DXGI_MODE_ROTATION_ROTATE180: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_ROTATION = 3
DXGI_MODE_ROTATION_ROTATE270: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_ROTATION = 4
DXGI_MODE_SCALING = Int32
DXGI_MODE_SCALING_UNSPECIFIED: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_SCALING = 0
DXGI_MODE_SCALING_CENTERED: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_SCALING = 1
DXGI_MODE_SCALING_STRETCHED: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_SCALING = 2
DXGI_MODE_SCANLINE_ORDER = Int32
DXGI_MODE_SCANLINE_ORDER_UNSPECIFIED: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_SCANLINE_ORDER = 0
DXGI_MODE_SCANLINE_ORDER_PROGRESSIVE: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_SCANLINE_ORDER = 1
DXGI_MODE_SCANLINE_ORDER_UPPER_FIELD_FIRST: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_SCANLINE_ORDER = 2
DXGI_MODE_SCANLINE_ORDER_LOWER_FIELD_FIRST: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_SCANLINE_ORDER = 3
class DXGI_RATIONAL(Structure):
    Numerator: UInt32
    Denominator: UInt32
class DXGI_RGB(Structure):
    Red: Single
    Green: Single
    Blue: Single
class DXGI_SAMPLE_DESC(Structure):
    Count: UInt32
    Quality: UInt32


make_ready(__name__)
