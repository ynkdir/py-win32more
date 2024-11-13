from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Media.Streaming
DEVPKEY_Device_PacketWakeSupported: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{88ad39db-0d0c-4a38-8435-4043826b5c91}'), pid=0)
DEVPKEY_Device_SendPacketWakeSupported: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{88ad39db-0d0c-4a38-8435-4043826b5c91}'), pid=1)
DEVPKEY_Device_UDN: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{88ad39db-0d0c-4a38-8435-4043826b5c91}'), pid=6)
DEVPKEY_Device_SupportsAudio: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{88ad39db-0d0c-4a38-8435-4043826b5c91}'), pid=8)
DEVPKEY_Device_SupportsVideo: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{88ad39db-0d0c-4a38-8435-4043826b5c91}'), pid=9)
DEVPKEY_Device_SupportsImages: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{88ad39db-0d0c-4a38-8435-4043826b5c91}'), pid=10)
DEVPKEY_Device_SinkProtocolInfo: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{88ad39db-0d0c-4a38-8435-4043826b5c91}'), pid=14)
DEVPKEY_Device_DLNADOC: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{88ad39db-0d0c-4a38-8435-4043826b5c91}'), pid=15)
DEVPKEY_Device_DLNACAP: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{88ad39db-0d0c-4a38-8435-4043826b5c91}'), pid=16)
DEVPKEY_Device_SupportsSearch: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{88ad39db-0d0c-4a38-8435-4043826b5c91}'), pid=17)
DEVPKEY_Device_SupportsMute: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{88ad39db-0d0c-4a38-8435-4043826b5c91}'), pid=18)
DEVPKEY_Device_MaxVolume: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{88ad39db-0d0c-4a38-8435-4043826b5c91}'), pid=19)
DEVPKEY_Device_SupportsSetNextAVT: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{88ad39db-0d0c-4a38-8435-4043826b5c91}'), pid=20)
GUID_DEVINTERFACE_DMR: Guid = Guid('{d0875fb4-2196-4c7a-a63d-e416addd60a1}')
GUID_DEVINTERFACE_DMP: Guid = Guid('{25b4e268-2a05-496e-803b-266837fbda4b}')
GUID_DEVINTERFACE_DMS: Guid = Guid('{c96037ae-a558-4470-b432-115a31b85553}')
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
    Region: win32more.Windows.Win32.Foundation.RECT
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
    Region: win32more.Windows.Win32.Foundation.RECT
class HistogramHeader(Structure):
    Size: UInt32
    Bins: UInt32
    FourCC: UInt32
    ChannelMasks: UInt32
    Grid: win32more.Windows.Win32.Media.Streaming.HistogramGrid
MF_MEDIASOURCE_STATUS_INFO = Int32
MF_MEDIASOURCE_STATUS_INFO_FULLYSUPPORTED: win32more.Windows.Win32.Media.Streaming.MF_MEDIASOURCE_STATUS_INFO = 0
MF_MEDIASOURCE_STATUS_INFO_UNKNOWN: win32more.Windows.Win32.Media.Streaming.MF_MEDIASOURCE_STATUS_INFO = 1
MF_TRANSFER_VIDEO_FRAME_FLAGS = Int32
MF_TRANSFER_VIDEO_FRAME_DEFAULT: win32more.Windows.Win32.Media.Streaming.MF_TRANSFER_VIDEO_FRAME_FLAGS = 0
MF_TRANSFER_VIDEO_FRAME_STRETCH: win32more.Windows.Win32.Media.Streaming.MF_TRANSFER_VIDEO_FRAME_FLAGS = 1
MF_TRANSFER_VIDEO_FRAME_IGNORE_PAR: win32more.Windows.Win32.Media.Streaming.MF_TRANSFER_VIDEO_FRAME_FLAGS = 2
class MetadataTimeStamps(Structure):
    Flags: UInt32
    Device: Int64
    Presentation: Int64


make_ready(__name__)
