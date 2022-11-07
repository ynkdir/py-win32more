from win32more import *
import win32more.Foundation
import win32more.Media.MediaFoundation
import win32more.Media.Streaming
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
def _define_IMFDeviceTransform_head():
    class IMFDeviceTransform(win32more.System.Com.IUnknown_head):
        Guid = Guid('d818fbd8-fc46-42f2-87ac-1ea2d1f9bf32')
    return IMFDeviceTransform
def _define_IMFDeviceTransform():
    IMFDeviceTransform = win32more.Media.Streaming.IMFDeviceTransform_head
    IMFDeviceTransform.InitializeTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.MediaFoundation.IMFAttributes_head, use_last_error=False)(3, 'InitializeTransform', ((1, 'pAttributes'),)))
    IMFDeviceTransform.GetInputAvailableType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Media.MediaFoundation.IMFMediaType_head), use_last_error=False)(4, 'GetInputAvailableType', ((1, 'dwInputStreamID'),(1, 'dwTypeIndex'),(1, 'pMediaType'),)))
    IMFDeviceTransform.GetInputCurrentType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.MediaFoundation.IMFMediaType_head), use_last_error=False)(5, 'GetInputCurrentType', ((1, 'dwInputStreamID'),(1, 'pMediaType'),)))
    IMFDeviceTransform.GetInputStreamAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.MediaFoundation.IMFAttributes_head), use_last_error=False)(6, 'GetInputStreamAttributes', ((1, 'dwInputStreamID'),(1, 'ppAttributes'),)))
    IMFDeviceTransform.GetOutputAvailableType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Media.MediaFoundation.IMFMediaType_head), use_last_error=False)(7, 'GetOutputAvailableType', ((1, 'dwOutputStreamID'),(1, 'dwTypeIndex'),(1, 'pMediaType'),)))
    IMFDeviceTransform.GetOutputCurrentType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.MediaFoundation.IMFMediaType_head), use_last_error=False)(8, 'GetOutputCurrentType', ((1, 'dwOutputStreamID'),(1, 'pMediaType'),)))
    IMFDeviceTransform.GetOutputStreamAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.MediaFoundation.IMFAttributes_head), use_last_error=False)(9, 'GetOutputStreamAttributes', ((1, 'dwOutputStreamID'),(1, 'ppAttributes'),)))
    IMFDeviceTransform.GetStreamCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(10, 'GetStreamCount', ((1, 'pcInputStreams'),(1, 'pcOutputStreams'),)))
    IMFDeviceTransform.GetStreamIDs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),UInt32,POINTER(UInt32), use_last_error=False)(11, 'GetStreamIDs', ((1, 'dwInputIDArraySize'),(1, 'pdwInputStreamIds'),(1, 'dwOutputIDArraySize'),(1, 'pdwOutputStreamIds'),)))
    IMFDeviceTransform.ProcessEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.MediaFoundation.IMFMediaEvent_head, use_last_error=False)(12, 'ProcessEvent', ((1, 'dwInputStreamID'),(1, 'pEvent'),)))
    IMFDeviceTransform.ProcessInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.MediaFoundation.IMFSample_head,UInt32, use_last_error=False)(13, 'ProcessInput', ((1, 'dwInputStreamID'),(1, 'pSample'),(1, 'dwFlags'),)))
    IMFDeviceTransform.ProcessMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.MediaFoundation.MFT_MESSAGE_TYPE,UIntPtr, use_last_error=False)(14, 'ProcessMessage', ((1, 'eMessage'),(1, 'ulParam'),)))
    IMFDeviceTransform.ProcessOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Media.MediaFoundation.MFT_OUTPUT_DATA_BUFFER_head),POINTER(UInt32), use_last_error=False)(15, 'ProcessOutput', ((1, 'dwFlags'),(1, 'cOutputBufferCount'),(1, 'pOutputSample'),(1, 'pdwStatus'),)))
    IMFDeviceTransform.SetInputStreamState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.MediaFoundation.IMFMediaType_head,win32more.Media.MediaFoundation.DeviceStreamState,UInt32, use_last_error=False)(16, 'SetInputStreamState', ((1, 'dwStreamID'),(1, 'pMediaType'),(1, 'value'),(1, 'dwFlags'),)))
    IMFDeviceTransform.GetInputStreamState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.MediaFoundation.DeviceStreamState), use_last_error=False)(17, 'GetInputStreamState', ((1, 'dwStreamID'),(1, 'value'),)))
    IMFDeviceTransform.SetOutputStreamState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.MediaFoundation.IMFMediaType_head,win32more.Media.MediaFoundation.DeviceStreamState,UInt32, use_last_error=False)(18, 'SetOutputStreamState', ((1, 'dwStreamID'),(1, 'pMediaType'),(1, 'value'),(1, 'dwFlags'),)))
    IMFDeviceTransform.GetOutputStreamState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.MediaFoundation.DeviceStreamState), use_last_error=False)(19, 'GetOutputStreamState', ((1, 'dwStreamID'),(1, 'value'),)))
    IMFDeviceTransform.GetInputStreamPreferredState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.MediaFoundation.DeviceStreamState),POINTER(win32more.Media.MediaFoundation.IMFMediaType_head), use_last_error=False)(20, 'GetInputStreamPreferredState', ((1, 'dwStreamID'),(1, 'value'),(1, 'ppMediaType'),)))
    IMFDeviceTransform.FlushInputStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(21, 'FlushInputStream', ((1, 'dwStreamIndex'),(1, 'dwFlags'),)))
    IMFDeviceTransform.FlushOutputStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(22, 'FlushOutputStream', ((1, 'dwStreamIndex'),(1, 'dwFlags'),)))
    win32more.System.Com.IUnknown
    return IMFDeviceTransform
def _define_IMFDeviceTransformCallback_head():
    class IMFDeviceTransformCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('6d5cb646-29ec-41fb-8179-8c4c6d750811')
    return IMFDeviceTransformCallback
def _define_IMFDeviceTransformCallback():
    IMFDeviceTransformCallback = win32more.Media.Streaming.IMFDeviceTransformCallback_head
    IMFDeviceTransformCallback.OnBufferSent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.MediaFoundation.IMFAttributes_head,UInt32, use_last_error=False)(3, 'OnBufferSent', ((1, 'pCallbackAttributes'),(1, 'pinId'),)))
    win32more.System.Com.IUnknown
    return IMFDeviceTransformCallback
MF_TRANSFER_VIDEO_FRAME_FLAGS = Int32
MF_TRANSFER_VIDEO_FRAME_DEFAULT = 0
MF_TRANSFER_VIDEO_FRAME_STRETCH = 1
MF_TRANSFER_VIDEO_FRAME_IGNORE_PAR = 2
MF_MEDIASOURCE_STATUS_INFO = Int32
MF_MEDIASOURCE_STATUS_INFO_FULLYSUPPORTED = 0
MF_MEDIASOURCE_STATUS_INFO_UNKNOWN = 1
def _define_FaceRectInfoBlobHeader_head():
    class FaceRectInfoBlobHeader(Structure):
        pass
    return FaceRectInfoBlobHeader
def _define_FaceRectInfoBlobHeader():
    FaceRectInfoBlobHeader = win32more.Media.Streaming.FaceRectInfoBlobHeader_head
    FaceRectInfoBlobHeader._fields_ = [
        ("Size", UInt32),
        ("Count", UInt32),
    ]
    return FaceRectInfoBlobHeader
def _define_FaceRectInfo_head():
    class FaceRectInfo(Structure):
        pass
    return FaceRectInfo
def _define_FaceRectInfo():
    FaceRectInfo = win32more.Media.Streaming.FaceRectInfo_head
    FaceRectInfo._fields_ = [
        ("Region", win32more.Foundation.RECT),
        ("confidenceLevel", Int32),
    ]
    return FaceRectInfo
def _define_FaceCharacterizationBlobHeader_head():
    class FaceCharacterizationBlobHeader(Structure):
        pass
    return FaceCharacterizationBlobHeader
def _define_FaceCharacterizationBlobHeader():
    FaceCharacterizationBlobHeader = win32more.Media.Streaming.FaceCharacterizationBlobHeader_head
    FaceCharacterizationBlobHeader._fields_ = [
        ("Size", UInt32),
        ("Count", UInt32),
    ]
    return FaceCharacterizationBlobHeader
def _define_FaceCharacterization_head():
    class FaceCharacterization(Structure):
        pass
    return FaceCharacterization
def _define_FaceCharacterization():
    FaceCharacterization = win32more.Media.Streaming.FaceCharacterization_head
    FaceCharacterization._fields_ = [
        ("BlinkScoreLeft", UInt32),
        ("BlinkScoreRight", UInt32),
        ("FacialExpression", UInt32),
        ("FacialExpressionScore", UInt32),
    ]
    return FaceCharacterization
def _define_CapturedMetadataExposureCompensation_head():
    class CapturedMetadataExposureCompensation(Structure):
        pass
    return CapturedMetadataExposureCompensation
def _define_CapturedMetadataExposureCompensation():
    CapturedMetadataExposureCompensation = win32more.Media.Streaming.CapturedMetadataExposureCompensation_head
    CapturedMetadataExposureCompensation._fields_ = [
        ("Flags", UInt64),
        ("Value", Int32),
    ]
    return CapturedMetadataExposureCompensation
def _define_CapturedMetadataISOGains_head():
    class CapturedMetadataISOGains(Structure):
        pass
    return CapturedMetadataISOGains
def _define_CapturedMetadataISOGains():
    CapturedMetadataISOGains = win32more.Media.Streaming.CapturedMetadataISOGains_head
    CapturedMetadataISOGains._fields_ = [
        ("AnalogGain", Single),
        ("DigitalGain", Single),
    ]
    return CapturedMetadataISOGains
def _define_CapturedMetadataWhiteBalanceGains_head():
    class CapturedMetadataWhiteBalanceGains(Structure):
        pass
    return CapturedMetadataWhiteBalanceGains
def _define_CapturedMetadataWhiteBalanceGains():
    CapturedMetadataWhiteBalanceGains = win32more.Media.Streaming.CapturedMetadataWhiteBalanceGains_head
    CapturedMetadataWhiteBalanceGains._fields_ = [
        ("R", Single),
        ("G", Single),
        ("B", Single),
    ]
    return CapturedMetadataWhiteBalanceGains
def _define_MetadataTimeStamps_head():
    class MetadataTimeStamps(Structure):
        pass
    return MetadataTimeStamps
def _define_MetadataTimeStamps():
    MetadataTimeStamps = win32more.Media.Streaming.MetadataTimeStamps_head
    MetadataTimeStamps._fields_ = [
        ("Flags", UInt32),
        ("Device", Int64),
        ("Presentation", Int64),
    ]
    return MetadataTimeStamps
def _define_HistogramGrid_head():
    class HistogramGrid(Structure):
        pass
    return HistogramGrid
def _define_HistogramGrid():
    HistogramGrid = win32more.Media.Streaming.HistogramGrid_head
    HistogramGrid._fields_ = [
        ("Width", UInt32),
        ("Height", UInt32),
        ("Region", win32more.Foundation.RECT),
    ]
    return HistogramGrid
def _define_HistogramBlobHeader_head():
    class HistogramBlobHeader(Structure):
        pass
    return HistogramBlobHeader
def _define_HistogramBlobHeader():
    HistogramBlobHeader = win32more.Media.Streaming.HistogramBlobHeader_head
    HistogramBlobHeader._fields_ = [
        ("Size", UInt32),
        ("Histograms", UInt32),
    ]
    return HistogramBlobHeader
def _define_HistogramHeader_head():
    class HistogramHeader(Structure):
        pass
    return HistogramHeader
def _define_HistogramHeader():
    HistogramHeader = win32more.Media.Streaming.HistogramHeader_head
    HistogramHeader._fields_ = [
        ("Size", UInt32),
        ("Bins", UInt32),
        ("FourCC", UInt32),
        ("ChannelMasks", UInt32),
        ("Grid", win32more.Media.Streaming.HistogramGrid),
    ]
    return HistogramHeader
def _define_HistogramDataHeader_head():
    class HistogramDataHeader(Structure):
        pass
    return HistogramDataHeader
def _define_HistogramDataHeader():
    HistogramDataHeader = win32more.Media.Streaming.HistogramDataHeader_head
    HistogramDataHeader._fields_ = [
        ("Size", UInt32),
        ("ChannelMask", UInt32),
        ("Linear", UInt32),
    ]
    return HistogramDataHeader
__all__ = [
    "IMFDeviceTransform",
    "IMFDeviceTransformCallback",
    "MF_TRANSFER_VIDEO_FRAME_FLAGS",
    "MF_TRANSFER_VIDEO_FRAME_DEFAULT",
    "MF_TRANSFER_VIDEO_FRAME_STRETCH",
    "MF_TRANSFER_VIDEO_FRAME_IGNORE_PAR",
    "MF_MEDIASOURCE_STATUS_INFO",
    "MF_MEDIASOURCE_STATUS_INFO_FULLYSUPPORTED",
    "MF_MEDIASOURCE_STATUS_INFO_UNKNOWN",
    "FaceRectInfoBlobHeader",
    "FaceRectInfo",
    "FaceCharacterizationBlobHeader",
    "FaceCharacterization",
    "CapturedMetadataExposureCompensation",
    "CapturedMetadataISOGains",
    "CapturedMetadataWhiteBalanceGains",
    "MetadataTimeStamps",
    "HistogramGrid",
    "HistogramBlobHeader",
    "HistogramHeader",
    "HistogramDataHeader",
]
