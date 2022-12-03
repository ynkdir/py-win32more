from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Media.Streaming
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define_CapturedMetadataExposureCompensation_head():
    class CapturedMetadataExposureCompensation(Structure):
        pass
    return CapturedMetadataExposureCompensation
def _define_CapturedMetadataExposureCompensation():
    CapturedMetadataExposureCompensation = win32more.Media.Streaming.CapturedMetadataExposureCompensation_head
    CapturedMetadataExposureCompensation._fields_ = [
        ('Flags', UInt64),
        ('Value', Int32),
    ]
    return CapturedMetadataExposureCompensation
def _define_CapturedMetadataISOGains_head():
    class CapturedMetadataISOGains(Structure):
        pass
    return CapturedMetadataISOGains
def _define_CapturedMetadataISOGains():
    CapturedMetadataISOGains = win32more.Media.Streaming.CapturedMetadataISOGains_head
    CapturedMetadataISOGains._fields_ = [
        ('AnalogGain', Single),
        ('DigitalGain', Single),
    ]
    return CapturedMetadataISOGains
def _define_CapturedMetadataWhiteBalanceGains_head():
    class CapturedMetadataWhiteBalanceGains(Structure):
        pass
    return CapturedMetadataWhiteBalanceGains
def _define_CapturedMetadataWhiteBalanceGains():
    CapturedMetadataWhiteBalanceGains = win32more.Media.Streaming.CapturedMetadataWhiteBalanceGains_head
    CapturedMetadataWhiteBalanceGains._fields_ = [
        ('R', Single),
        ('G', Single),
        ('B', Single),
    ]
    return CapturedMetadataWhiteBalanceGains
def _define_FaceCharacterization_head():
    class FaceCharacterization(Structure):
        pass
    return FaceCharacterization
def _define_FaceCharacterization():
    FaceCharacterization = win32more.Media.Streaming.FaceCharacterization_head
    FaceCharacterization._fields_ = [
        ('BlinkScoreLeft', UInt32),
        ('BlinkScoreRight', UInt32),
        ('FacialExpression', UInt32),
        ('FacialExpressionScore', UInt32),
    ]
    return FaceCharacterization
def _define_FaceCharacterizationBlobHeader_head():
    class FaceCharacterizationBlobHeader(Structure):
        pass
    return FaceCharacterizationBlobHeader
def _define_FaceCharacterizationBlobHeader():
    FaceCharacterizationBlobHeader = win32more.Media.Streaming.FaceCharacterizationBlobHeader_head
    FaceCharacterizationBlobHeader._fields_ = [
        ('Size', UInt32),
        ('Count', UInt32),
    ]
    return FaceCharacterizationBlobHeader
def _define_FaceRectInfo_head():
    class FaceRectInfo(Structure):
        pass
    return FaceRectInfo
def _define_FaceRectInfo():
    FaceRectInfo = win32more.Media.Streaming.FaceRectInfo_head
    FaceRectInfo._fields_ = [
        ('Region', win32more.Foundation.RECT),
        ('confidenceLevel', Int32),
    ]
    return FaceRectInfo
def _define_FaceRectInfoBlobHeader_head():
    class FaceRectInfoBlobHeader(Structure):
        pass
    return FaceRectInfoBlobHeader
def _define_FaceRectInfoBlobHeader():
    FaceRectInfoBlobHeader = win32more.Media.Streaming.FaceRectInfoBlobHeader_head
    FaceRectInfoBlobHeader._fields_ = [
        ('Size', UInt32),
        ('Count', UInt32),
    ]
    return FaceRectInfoBlobHeader
def _define_HistogramBlobHeader_head():
    class HistogramBlobHeader(Structure):
        pass
    return HistogramBlobHeader
def _define_HistogramBlobHeader():
    HistogramBlobHeader = win32more.Media.Streaming.HistogramBlobHeader_head
    HistogramBlobHeader._fields_ = [
        ('Size', UInt32),
        ('Histograms', UInt32),
    ]
    return HistogramBlobHeader
def _define_HistogramDataHeader_head():
    class HistogramDataHeader(Structure):
        pass
    return HistogramDataHeader
def _define_HistogramDataHeader():
    HistogramDataHeader = win32more.Media.Streaming.HistogramDataHeader_head
    HistogramDataHeader._fields_ = [
        ('Size', UInt32),
        ('ChannelMask', UInt32),
        ('Linear', UInt32),
    ]
    return HistogramDataHeader
def _define_HistogramGrid_head():
    class HistogramGrid(Structure):
        pass
    return HistogramGrid
def _define_HistogramGrid():
    HistogramGrid = win32more.Media.Streaming.HistogramGrid_head
    HistogramGrid._fields_ = [
        ('Width', UInt32),
        ('Height', UInt32),
        ('Region', win32more.Foundation.RECT),
    ]
    return HistogramGrid
def _define_HistogramHeader_head():
    class HistogramHeader(Structure):
        pass
    return HistogramHeader
def _define_HistogramHeader():
    HistogramHeader = win32more.Media.Streaming.HistogramHeader_head
    HistogramHeader._fields_ = [
        ('Size', UInt32),
        ('Bins', UInt32),
        ('FourCC', UInt32),
        ('ChannelMasks', UInt32),
        ('Grid', win32more.Media.Streaming.HistogramGrid),
    ]
    return HistogramHeader
def _define_MetadataTimeStamps_head():
    class MetadataTimeStamps(Structure):
        pass
    return MetadataTimeStamps
def _define_MetadataTimeStamps():
    MetadataTimeStamps = win32more.Media.Streaming.MetadataTimeStamps_head
    MetadataTimeStamps._fields_ = [
        ('Flags', UInt32),
        ('Device', Int64),
        ('Presentation', Int64),
    ]
    return MetadataTimeStamps
MF_MEDIASOURCE_STATUS_INFO = Int32
MF_MEDIASOURCE_STATUS_INFO_FULLYSUPPORTED = 0
MF_MEDIASOURCE_STATUS_INFO_UNKNOWN = 1
MF_TRANSFER_VIDEO_FRAME_FLAGS = Int32
MF_TRANSFER_VIDEO_FRAME_DEFAULT = 0
MF_TRANSFER_VIDEO_FRAME_STRETCH = 1
MF_TRANSFER_VIDEO_FRAME_IGNORE_PAR = 2
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
