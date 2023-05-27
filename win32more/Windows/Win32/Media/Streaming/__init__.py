from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Media.Streaming
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class CapturedMetadataExposureCompensation(EasyCastStructure):
    Flags: UInt64
    Value: Int32
class CapturedMetadataISOGains(EasyCastStructure):
    AnalogGain: Single
    DigitalGain: Single
class CapturedMetadataWhiteBalanceGains(EasyCastStructure):
    R: Single
    G: Single
    B: Single
class FaceCharacterization(EasyCastStructure):
    BlinkScoreLeft: UInt32
    BlinkScoreRight: UInt32
    FacialExpression: UInt32
    FacialExpressionScore: UInt32
class FaceCharacterizationBlobHeader(EasyCastStructure):
    Size: UInt32
    Count: UInt32
class FaceRectInfo(EasyCastStructure):
    Region: win32more.Windows.Win32.Foundation.RECT
    confidenceLevel: Int32
class FaceRectInfoBlobHeader(EasyCastStructure):
    Size: UInt32
    Count: UInt32
class HistogramBlobHeader(EasyCastStructure):
    Size: UInt32
    Histograms: UInt32
class HistogramDataHeader(EasyCastStructure):
    Size: UInt32
    ChannelMask: UInt32
    Linear: UInt32
class HistogramGrid(EasyCastStructure):
    Width: UInt32
    Height: UInt32
    Region: win32more.Windows.Win32.Foundation.RECT
class HistogramHeader(EasyCastStructure):
    Size: UInt32
    Bins: UInt32
    FourCC: UInt32
    ChannelMasks: UInt32
    Grid: win32more.Windows.Win32.Media.Streaming.HistogramGrid
MF_MEDIASOURCE_STATUS_INFO = Int32
MF_MEDIASOURCE_STATUS_INFO_FULLYSUPPORTED: MF_MEDIASOURCE_STATUS_INFO = 0
MF_MEDIASOURCE_STATUS_INFO_UNKNOWN: MF_MEDIASOURCE_STATUS_INFO = 1
MF_TRANSFER_VIDEO_FRAME_FLAGS = Int32
MF_TRANSFER_VIDEO_FRAME_DEFAULT: MF_TRANSFER_VIDEO_FRAME_FLAGS = 0
MF_TRANSFER_VIDEO_FRAME_STRETCH: MF_TRANSFER_VIDEO_FRAME_FLAGS = 1
MF_TRANSFER_VIDEO_FRAME_IGNORE_PAR: MF_TRANSFER_VIDEO_FRAME_FLAGS = 2
class MetadataTimeStamps(EasyCastStructure):
    Flags: UInt32
    Device: Int64
    Presentation: Int64
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
