from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Media.Streaming
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
class CapturedMetadataExposureCompensation(Structure):
    Flags: UInt64
    Value: Int32
class CapturedMetadataISOGains(Structure):
    AnalogGain: Single
    DigitalGain: Single
class CapturedMetadataWhiteBalanceGains(Structure):
    R: Single
    G: Single
    B: Single
class FaceCharacterization(Structure):
    BlinkScoreLeft: UInt32
    BlinkScoreRight: UInt32
    FacialExpression: UInt32
    FacialExpressionScore: UInt32
class FaceCharacterizationBlobHeader(Structure):
    Size: UInt32
    Count: UInt32
class FaceRectInfo(Structure):
    Region: win32more.Foundation.RECT
    confidenceLevel: Int32
class FaceRectInfoBlobHeader(Structure):
    Size: UInt32
    Count: UInt32
class HistogramBlobHeader(Structure):
    Size: UInt32
    Histograms: UInt32
class HistogramDataHeader(Structure):
    Size: UInt32
    ChannelMask: UInt32
    Linear: UInt32
class HistogramGrid(Structure):
    Width: UInt32
    Height: UInt32
    Region: win32more.Foundation.RECT
class HistogramHeader(Structure):
    Size: UInt32
    Bins: UInt32
    FourCC: UInt32
    ChannelMasks: UInt32
    Grid: win32more.Media.Streaming.HistogramGrid
class MetadataTimeStamps(Structure):
    Flags: UInt32
    Device: Int64
    Presentation: Int64
MF_MEDIASOURCE_STATUS_INFO = Int32
MF_MEDIASOURCE_STATUS_INFO_FULLYSUPPORTED: MF_MEDIASOURCE_STATUS_INFO = 0
MF_MEDIASOURCE_STATUS_INFO_UNKNOWN: MF_MEDIASOURCE_STATUS_INFO = 1
MF_TRANSFER_VIDEO_FRAME_FLAGS = Int32
MF_TRANSFER_VIDEO_FRAME_DEFAULT: MF_TRANSFER_VIDEO_FRAME_FLAGS = 0
MF_TRANSFER_VIDEO_FRAME_STRETCH: MF_TRANSFER_VIDEO_FRAME_FLAGS = 1
MF_TRANSFER_VIDEO_FRAME_IGNORE_PAR: MF_TRANSFER_VIDEO_FRAME_FLAGS = 2
make_head(_module, 'CapturedMetadataExposureCompensation')
make_head(_module, 'CapturedMetadataISOGains')
make_head(_module, 'CapturedMetadataWhiteBalanceGains')
make_head(_module, 'FaceCharacterization')
make_head(_module, 'FaceCharacterizationBlobHeader')
make_head(_module, 'FaceRectInfo')
make_head(_module, 'FaceRectInfoBlobHeader')
make_head(_module, 'HistogramBlobHeader')
make_head(_module, 'HistogramDataHeader')
make_head(_module, 'HistogramGrid')
make_head(_module, 'HistogramHeader')
make_head(_module, 'MetadataTimeStamps')
__all__ = [
    "CapturedMetadataExposureCompensation",
    "CapturedMetadataISOGains",
    "CapturedMetadataWhiteBalanceGains",
    "FaceCharacterization",
    "FaceCharacterizationBlobHeader",
    "FaceRectInfo",
    "FaceRectInfoBlobHeader",
    "HistogramBlobHeader",
    "HistogramDataHeader",
    "HistogramGrid",
    "HistogramHeader",
    "MF_MEDIASOURCE_STATUS_INFO",
    "MF_MEDIASOURCE_STATUS_INFO_FULLYSUPPORTED",
    "MF_MEDIASOURCE_STATUS_INFO_UNKNOWN",
    "MF_TRANSFER_VIDEO_FRAME_DEFAULT",
    "MF_TRANSFER_VIDEO_FRAME_FLAGS",
    "MF_TRANSFER_VIDEO_FRAME_IGNORE_PAR",
    "MF_TRANSFER_VIDEO_FRAME_STRETCH",
    "MetadataTimeStamps",
]
_arch_optional = [
]
