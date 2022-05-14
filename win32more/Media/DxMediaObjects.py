from win32more import *
import win32more.Media.DxMediaObjects
import win32more.Foundation
import win32more.System.Com

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.Media.DxMediaObjects, name, eval(f"_define_{name}()"))
    return getattr(win32more.Media.DxMediaObjects, name)
DMO_E_INVALIDSTREAMINDEX = -2147220991
DMO_E_INVALIDTYPE = -2147220990
DMO_E_TYPE_NOT_SET = -2147220989
DMO_E_NOTACCEPTING = -2147220988
DMO_E_TYPE_NOT_ACCEPTED = -2147220987
DMO_E_NO_MORE_ITEMS = -2147220986
DMOCATEGORY_AUDIO_DECODER = '57f2db8b-e6bb-4513-9d43-dcd2a6593125'
DMOCATEGORY_AUDIO_ENCODER = '33d9a761-90c8-11d0-bd43-00a0c911ce86'
DMOCATEGORY_VIDEO_DECODER = '4a69b442-28be-4991-969c-b500adf5d8a8'
DMOCATEGORY_VIDEO_ENCODER = '33d9a760-90c8-11d0-bd43-00a0c911ce86'
DMOCATEGORY_AUDIO_EFFECT = 'f3602b3f-0592-48df-a4cd-674721e7ebeb'
DMOCATEGORY_VIDEO_EFFECT = 'd990ee14-776c-4723-be46-3da2f56f10b9'
DMOCATEGORY_AUDIO_CAPTURE_EFFECT = 'f665aaba-3e09-4920-aa5f-219811148f09'
DMOCATEGORY_ACOUSTIC_ECHO_CANCEL = 'bf963d80-c559-11d0-8a2b-00a0c9255ac1'
DMOCATEGORY_AUDIO_NOISE_SUPPRESS = 'e07f903f-62fd-4e60-8cdd-dea7236665b5'
DMOCATEGORY_AGC = 'e88c9ba0-c557-11d0-8a2b-00a0c9255ac1'
def _define_DMO_MEDIA_TYPE_head():
    class DMO_MEDIA_TYPE(Structure):
        pass
    return DMO_MEDIA_TYPE
def _define_DMO_MEDIA_TYPE():
    DMO_MEDIA_TYPE = win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head
    DMO_MEDIA_TYPE._fields_ = [
        ("majortype", Guid),
        ("subtype", Guid),
        ("bFixedSizeSamples", win32more.Foundation.BOOL),
        ("bTemporalCompression", win32more.Foundation.BOOL),
        ("lSampleSize", UInt32),
        ("formattype", Guid),
        ("pUnk", win32more.System.Com.IUnknown_head),
        ("cbFormat", UInt32),
        ("pbFormat", c_char_p_no),
    ]
    return DMO_MEDIA_TYPE
_DMO_INPUT_DATA_BUFFER_FLAGS = Int32
DMO_INPUT_DATA_BUFFERF_SYNCPOINT = 1
DMO_INPUT_DATA_BUFFERF_TIME = 2
DMO_INPUT_DATA_BUFFERF_TIMELENGTH = 4
DMO_INPUT_DATA_BUFFERF_DISCONTINUITY = 8
_DMO_OUTPUT_DATA_BUFFER_FLAGS = Int32
DMO_OUTPUT_DATA_BUFFERF_SYNCPOINT = 1
DMO_OUTPUT_DATA_BUFFERF_TIME = 2
DMO_OUTPUT_DATA_BUFFERF_TIMELENGTH = 4
DMO_OUTPUT_DATA_BUFFERF_DISCONTINUITY = 8
DMO_OUTPUT_DATA_BUFFERF_INCOMPLETE = 16777216
_DMO_INPUT_STATUS_FLAGS = Int32
DMO_INPUT_STATUSF_ACCEPT_DATA = 1
_DMO_INPUT_STREAM_INFO_FLAGS = Int32
DMO_INPUT_STREAMF_WHOLE_SAMPLES = 1
DMO_INPUT_STREAMF_SINGLE_SAMPLE_PER_BUFFER = 2
DMO_INPUT_STREAMF_FIXED_SAMPLE_SIZE = 4
DMO_INPUT_STREAMF_HOLDS_BUFFERS = 8
_DMO_OUTPUT_STREAM_INFO_FLAGS = Int32
DMO_OUTPUT_STREAMF_WHOLE_SAMPLES = 1
DMO_OUTPUT_STREAMF_SINGLE_SAMPLE_PER_BUFFER = 2
DMO_OUTPUT_STREAMF_FIXED_SAMPLE_SIZE = 4
DMO_OUTPUT_STREAMF_DISCARDABLE = 8
DMO_OUTPUT_STREAMF_OPTIONAL = 16
_DMO_SET_TYPE_FLAGS = Int32
DMO_SET_TYPEF_TEST_ONLY = 1
DMO_SET_TYPEF_CLEAR = 2
_DMO_PROCESS_OUTPUT_FLAGS = Int32
DMO_PROCESS_OUTPUT_DISCARD_WHEN_NO_BUFFER = 1
def _define_IMediaBuffer_head():
    class IMediaBuffer(win32more.System.Com.IUnknown_head):
        Guid = Guid('59eff8b9-938c-4a26-82f2-95cb84cdc837')
    return IMediaBuffer
def _define_IMediaBuffer():
    IMediaBuffer = win32more.Media.DxMediaObjects.IMediaBuffer_head
    IMediaBuffer.SetLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(3, 'SetLength', ((1, 'cbLength'),)))
    IMediaBuffer.GetMaxLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetMaxLength', ((1, 'pcbMaxLength'),)))
    IMediaBuffer.GetBufferAndLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)(5, 'GetBufferAndLength', ((1, 'ppBuffer'),(1, 'pcbLength'),)))
    return IMediaBuffer
def _define_DMO_OUTPUT_DATA_BUFFER_head():
    class DMO_OUTPUT_DATA_BUFFER(Structure):
        pass
    return DMO_OUTPUT_DATA_BUFFER
def _define_DMO_OUTPUT_DATA_BUFFER():
    DMO_OUTPUT_DATA_BUFFER = win32more.Media.DxMediaObjects.DMO_OUTPUT_DATA_BUFFER_head
    DMO_OUTPUT_DATA_BUFFER._fields_ = [
        ("pBuffer", win32more.Media.DxMediaObjects.IMediaBuffer_head),
        ("dwStatus", UInt32),
        ("rtTimestamp", Int64),
        ("rtTimelength", Int64),
    ]
    return DMO_OUTPUT_DATA_BUFFER
def _define_IMediaObject_head():
    class IMediaObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('d8ad0f58-5494-4102-97c5-ec798e59bcf4')
    return IMediaObject
def _define_IMediaObject():
    IMediaObject = win32more.Media.DxMediaObjects.IMediaObject_head
    IMediaObject.GetStreamCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(3, 'GetStreamCount', ((1, 'pcInputStreams'),(1, 'pcOutputStreams'),)))
    IMediaObject.GetInputStreamInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(4, 'GetInputStreamInfo', ((1, 'dwInputStreamIndex'),(1, 'pdwFlags'),)))
    IMediaObject.GetOutputStreamInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(5, 'GetOutputStreamInfo', ((1, 'dwOutputStreamIndex'),(1, 'pdwFlags'),)))
    IMediaObject.GetInputType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head), use_last_error=False)(6, 'GetInputType', ((1, 'dwInputStreamIndex'),(1, 'dwTypeIndex'),(1, 'pmt'),)))
    IMediaObject.GetOutputType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head), use_last_error=False)(7, 'GetOutputType', ((1, 'dwOutputStreamIndex'),(1, 'dwTypeIndex'),(1, 'pmt'),)))
    IMediaObject.SetInputType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head),UInt32, use_last_error=False)(8, 'SetInputType', ((1, 'dwInputStreamIndex'),(1, 'pmt'),(1, 'dwFlags'),)))
    IMediaObject.SetOutputType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head),UInt32, use_last_error=False)(9, 'SetOutputType', ((1, 'dwOutputStreamIndex'),(1, 'pmt'),(1, 'dwFlags'),)))
    IMediaObject.GetInputCurrentType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head), use_last_error=False)(10, 'GetInputCurrentType', ((1, 'dwInputStreamIndex'),(1, 'pmt'),)))
    IMediaObject.GetOutputCurrentType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head), use_last_error=False)(11, 'GetOutputCurrentType', ((1, 'dwOutputStreamIndex'),(1, 'pmt'),)))
    IMediaObject.GetInputSizeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(12, 'GetInputSizeInfo', ((1, 'dwInputStreamIndex'),(1, 'pcbSize'),(1, 'pcbMaxLookahead'),(1, 'pcbAlignment'),)))
    IMediaObject.GetOutputSizeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(13, 'GetOutputSizeInfo', ((1, 'dwOutputStreamIndex'),(1, 'pcbSize'),(1, 'pcbAlignment'),)))
    IMediaObject.GetInputMaxLatency = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Int64), use_last_error=False)(14, 'GetInputMaxLatency', ((1, 'dwInputStreamIndex'),(1, 'prtMaxLatency'),)))
    IMediaObject.SetInputMaxLatency = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int64, use_last_error=False)(15, 'SetInputMaxLatency', ((1, 'dwInputStreamIndex'),(1, 'rtMaxLatency'),)))
    IMediaObject.Flush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(16, 'Flush', ()))
    IMediaObject.Discontinuity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(17, 'Discontinuity', ((1, 'dwInputStreamIndex'),)))
    IMediaObject.AllocateStreamingResources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(18, 'AllocateStreamingResources', ()))
    IMediaObject.FreeStreamingResources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(19, 'FreeStreamingResources', ()))
    IMediaObject.GetInputStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(20, 'GetInputStatus', ((1, 'dwInputStreamIndex'),(1, 'dwFlags'),)))
    IMediaObject.ProcessInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.DxMediaObjects.IMediaBuffer_head,UInt32,Int64,Int64, use_last_error=False)(21, 'ProcessInput', ((1, 'dwInputStreamIndex'),(1, 'pBuffer'),(1, 'dwFlags'),(1, 'rtTimestamp'),(1, 'rtTimelength'),)))
    IMediaObject.ProcessOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Media.DxMediaObjects.DMO_OUTPUT_DATA_BUFFER),POINTER(UInt32), use_last_error=False)(22, 'ProcessOutput', ((1, 'dwFlags'),(1, 'cOutputBufferCount'),(1, 'pOutputBuffers'),(1, 'pdwStatus'),)))
    IMediaObject.Lock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(23, 'Lock', ((1, 'bLock'),)))
    return IMediaObject
def _define_IEnumDMO_head():
    class IEnumDMO(win32more.System.Com.IUnknown_head):
        Guid = Guid('2c3cd98a-2bfa-4a53-9c27-5249ba64ba0f')
    return IEnumDMO
def _define_IEnumDMO():
    IEnumDMO = win32more.Media.DxMediaObjects.IEnumDMO_head
    IEnumDMO.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(win32more.Foundation.PWSTR),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'cItemsToFetch'),(1, 'pCLSID'),(1, 'Names'),(1, 'pcItemsFetched'),)))
    IEnumDMO.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'cItemsToSkip'),)))
    IEnumDMO.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumDMO.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DxMediaObjects.IEnumDMO_head), use_last_error=False)(6, 'Clone', ((1, 'ppEnum'),)))
    return IEnumDMO
_DMO_INPLACE_PROCESS_FLAGS = Int32
DMO_INPLACE_NORMAL = 0
DMO_INPLACE_ZERO = 1
def _define_IMediaObjectInPlace_head():
    class IMediaObjectInPlace(win32more.System.Com.IUnknown_head):
        Guid = Guid('651b9ad0-0fc7-4aa9-9538-d89931010741')
    return IMediaObjectInPlace
def _define_IMediaObjectInPlace():
    IMediaObjectInPlace = win32more.Media.DxMediaObjects.IMediaObjectInPlace_head
    IMediaObjectInPlace.Process = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_char_p_no,Int64,UInt32, use_last_error=False)(3, 'Process', ((1, 'ulSize'),(1, 'pData'),(1, 'refTimeStart'),(1, 'dwFlags'),)))
    IMediaObjectInPlace.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DxMediaObjects.IMediaObjectInPlace_head), use_last_error=False)(4, 'Clone', ((1, 'ppMediaObject'),)))
    IMediaObjectInPlace.GetLatency = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int64), use_last_error=False)(5, 'GetLatency', ((1, 'pLatencyTime'),)))
    return IMediaObjectInPlace
_DMO_QUALITY_STATUS_FLAGS = Int32
DMO_QUALITY_STATUS_ENABLED = 1
def _define_IDMOQualityControl_head():
    class IDMOQualityControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('65abea96-cf36-453f-af8a-705e98f16260')
    return IDMOQualityControl
def _define_IDMOQualityControl():
    IDMOQualityControl = win32more.Media.DxMediaObjects.IDMOQualityControl_head
    IDMOQualityControl.SetNow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int64, use_last_error=False)(3, 'SetNow', ((1, 'rtNow'),)))
    IDMOQualityControl.SetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'SetStatus', ((1, 'dwFlags'),)))
    IDMOQualityControl.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetStatus', ((1, 'pdwFlags'),)))
    return IDMOQualityControl
_DMO_VIDEO_OUTPUT_STREAM_FLAGS = Int32
DMO_VOSF_NEEDS_PREVIOUS_SAMPLE = 1
def _define_IDMOVideoOutputOptimizations_head():
    class IDMOVideoOutputOptimizations(win32more.System.Com.IUnknown_head):
        Guid = Guid('be8f4f4e-5b16-4d29-b350-7f6b5d9298ac')
    return IDMOVideoOutputOptimizations
def _define_IDMOVideoOutputOptimizations():
    IDMOVideoOutputOptimizations = win32more.Media.DxMediaObjects.IDMOVideoOutputOptimizations_head
    IDMOVideoOutputOptimizations.QueryOperationModePreferences = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(3, 'QueryOperationModePreferences', ((1, 'ulOutputStreamIndex'),(1, 'pdwRequestedCapabilities'),)))
    IDMOVideoOutputOptimizations.SetOperationMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(4, 'SetOperationMode', ((1, 'ulOutputStreamIndex'),(1, 'dwEnabledFeatures'),)))
    IDMOVideoOutputOptimizations.GetCurrentOperationMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(5, 'GetCurrentOperationMode', ((1, 'ulOutputStreamIndex'),(1, 'pdwEnabledFeatures'),)))
    IDMOVideoOutputOptimizations.GetCurrentSampleRequirements = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(6, 'GetCurrentSampleRequirements', ((1, 'ulOutputStreamIndex'),(1, 'pdwRequestedFeatures'),)))
    return IDMOVideoOutputOptimizations
def _define_DMO_PARTIAL_MEDIATYPE_head():
    class DMO_PARTIAL_MEDIATYPE(Structure):
        pass
    return DMO_PARTIAL_MEDIATYPE
def _define_DMO_PARTIAL_MEDIATYPE():
    DMO_PARTIAL_MEDIATYPE = win32more.Media.DxMediaObjects.DMO_PARTIAL_MEDIATYPE_head
    DMO_PARTIAL_MEDIATYPE._fields_ = [
        ("type", Guid),
        ("subtype", Guid),
    ]
    return DMO_PARTIAL_MEDIATYPE
DMO_REGISTER_FLAGS = Int32
DMO_REGISTERF_IS_KEYED = 1
DMO_ENUM_FLAGS = Int32
DMO_ENUMF_INCLUDE_KEYED = 1
def _define_DMORegister():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(Guid),UInt32,UInt32,POINTER(win32more.Media.DxMediaObjects.DMO_PARTIAL_MEDIATYPE_head),UInt32,POINTER(win32more.Media.DxMediaObjects.DMO_PARTIAL_MEDIATYPE_head), use_last_error=False)(("DMORegister", windll["msdmo"]), ((1, 'szName'),(1, 'clsidDMO'),(1, 'guidCategory'),(1, 'dwFlags'),(1, 'cInTypes'),(1, 'pInTypes'),(1, 'cOutTypes'),(1, 'pOutTypes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DMOUnregister():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid), use_last_error=False)(("DMOUnregister", windll["msdmo"]), ((1, 'clsidDMO'),(1, 'guidCategory'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DMOEnum():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,UInt32,POINTER(win32more.Media.DxMediaObjects.DMO_PARTIAL_MEDIATYPE_head),UInt32,POINTER(win32more.Media.DxMediaObjects.DMO_PARTIAL_MEDIATYPE_head),POINTER(win32more.Media.DxMediaObjects.IEnumDMO_head), use_last_error=False)(("DMOEnum", windll["msdmo"]), ((1, 'guidCategory'),(1, 'dwFlags'),(1, 'cInTypes'),(1, 'pInTypes'),(1, 'cOutTypes'),(1, 'pOutTypes'),(1, 'ppEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DMOGetTypes():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(UInt32),POINTER(win32more.Media.DxMediaObjects.DMO_PARTIAL_MEDIATYPE_head),UInt32,POINTER(UInt32),POINTER(win32more.Media.DxMediaObjects.DMO_PARTIAL_MEDIATYPE_head), use_last_error=False)(("DMOGetTypes", windll["msdmo"]), ((1, 'clsidDMO'),(1, 'ulInputTypesRequested'),(1, 'pulInputTypesSupplied'),(1, 'pInputTypes'),(1, 'ulOutputTypesRequested'),(1, 'pulOutputTypesSupplied'),(1, 'pOutputTypes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DMOGetName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Char), use_last_error=False)(("DMOGetName", windll["msdmo"]), ((1, 'clsidDMO'),(1, 'szName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MoInitMediaType():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head),UInt32, use_last_error=False)(("MoInitMediaType", windll["msdmo"]), ((1, 'pmt'),(1, 'cbFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MoFreeMediaType():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head), use_last_error=False)(("MoFreeMediaType", windll["msdmo"]), ((1, 'pmt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MoCopyMediaType():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head),POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head), use_last_error=False)(("MoCopyMediaType", windll["msdmo"]), ((1, 'pmtDest'),(1, 'pmtSrc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MoCreateMediaType():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head)),UInt32, use_last_error=False)(("MoCreateMediaType", windll["msdmo"]), ((1, 'ppmt'),(1, 'cbFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MoDeleteMediaType():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head), use_last_error=False)(("MoDeleteMediaType", windll["msdmo"]), ((1, 'pmt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MoDuplicateMediaType():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head)),POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head), use_last_error=False)(("MoDuplicateMediaType", windll["msdmo"]), ((1, 'ppmtDest'),(1, 'pmtSrc'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "DMO_E_INVALIDSTREAMINDEX",
    "DMO_E_INVALIDTYPE",
    "DMO_E_TYPE_NOT_SET",
    "DMO_E_NOTACCEPTING",
    "DMO_E_TYPE_NOT_ACCEPTED",
    "DMO_E_NO_MORE_ITEMS",
    "DMOCATEGORY_AUDIO_DECODER",
    "DMOCATEGORY_AUDIO_ENCODER",
    "DMOCATEGORY_VIDEO_DECODER",
    "DMOCATEGORY_VIDEO_ENCODER",
    "DMOCATEGORY_AUDIO_EFFECT",
    "DMOCATEGORY_VIDEO_EFFECT",
    "DMOCATEGORY_AUDIO_CAPTURE_EFFECT",
    "DMOCATEGORY_ACOUSTIC_ECHO_CANCEL",
    "DMOCATEGORY_AUDIO_NOISE_SUPPRESS",
    "DMOCATEGORY_AGC",
    "DMO_MEDIA_TYPE",
    "_DMO_INPUT_DATA_BUFFER_FLAGS",
    "DMO_INPUT_DATA_BUFFERF_SYNCPOINT",
    "DMO_INPUT_DATA_BUFFERF_TIME",
    "DMO_INPUT_DATA_BUFFERF_TIMELENGTH",
    "DMO_INPUT_DATA_BUFFERF_DISCONTINUITY",
    "_DMO_OUTPUT_DATA_BUFFER_FLAGS",
    "DMO_OUTPUT_DATA_BUFFERF_SYNCPOINT",
    "DMO_OUTPUT_DATA_BUFFERF_TIME",
    "DMO_OUTPUT_DATA_BUFFERF_TIMELENGTH",
    "DMO_OUTPUT_DATA_BUFFERF_DISCONTINUITY",
    "DMO_OUTPUT_DATA_BUFFERF_INCOMPLETE",
    "_DMO_INPUT_STATUS_FLAGS",
    "DMO_INPUT_STATUSF_ACCEPT_DATA",
    "_DMO_INPUT_STREAM_INFO_FLAGS",
    "DMO_INPUT_STREAMF_WHOLE_SAMPLES",
    "DMO_INPUT_STREAMF_SINGLE_SAMPLE_PER_BUFFER",
    "DMO_INPUT_STREAMF_FIXED_SAMPLE_SIZE",
    "DMO_INPUT_STREAMF_HOLDS_BUFFERS",
    "_DMO_OUTPUT_STREAM_INFO_FLAGS",
    "DMO_OUTPUT_STREAMF_WHOLE_SAMPLES",
    "DMO_OUTPUT_STREAMF_SINGLE_SAMPLE_PER_BUFFER",
    "DMO_OUTPUT_STREAMF_FIXED_SAMPLE_SIZE",
    "DMO_OUTPUT_STREAMF_DISCARDABLE",
    "DMO_OUTPUT_STREAMF_OPTIONAL",
    "_DMO_SET_TYPE_FLAGS",
    "DMO_SET_TYPEF_TEST_ONLY",
    "DMO_SET_TYPEF_CLEAR",
    "_DMO_PROCESS_OUTPUT_FLAGS",
    "DMO_PROCESS_OUTPUT_DISCARD_WHEN_NO_BUFFER",
    "IMediaBuffer",
    "DMO_OUTPUT_DATA_BUFFER",
    "IMediaObject",
    "IEnumDMO",
    "_DMO_INPLACE_PROCESS_FLAGS",
    "DMO_INPLACE_NORMAL",
    "DMO_INPLACE_ZERO",
    "IMediaObjectInPlace",
    "_DMO_QUALITY_STATUS_FLAGS",
    "DMO_QUALITY_STATUS_ENABLED",
    "IDMOQualityControl",
    "_DMO_VIDEO_OUTPUT_STREAM_FLAGS",
    "DMO_VOSF_NEEDS_PREVIOUS_SAMPLE",
    "IDMOVideoOutputOptimizations",
    "DMO_PARTIAL_MEDIATYPE",
    "DMO_REGISTER_FLAGS",
    "DMO_REGISTERF_IS_KEYED",
    "DMO_ENUM_FLAGS",
    "DMO_ENUMF_INCLUDE_KEYED",
    "DMORegister",
    "DMOUnregister",
    "DMOEnum",
    "DMOGetTypes",
    "DMOGetName",
    "MoInitMediaType",
    "MoFreeMediaType",
    "MoCopyMediaType",
    "MoCreateMediaType",
    "MoDeleteMediaType",
    "MoDuplicateMediaType",
]
