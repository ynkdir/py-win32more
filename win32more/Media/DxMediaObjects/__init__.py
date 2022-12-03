from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Media.DxMediaObjects
import win32more.System.Com
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
_DMO_INPLACE_PROCESS_FLAGS = Int32
DMO_INPLACE_NORMAL = 0
DMO_INPLACE_ZERO = 1
_DMO_INPUT_DATA_BUFFER_FLAGS = Int32
DMO_INPUT_DATA_BUFFERF_SYNCPOINT = 1
DMO_INPUT_DATA_BUFFERF_TIME = 2
DMO_INPUT_DATA_BUFFERF_TIMELENGTH = 4
DMO_INPUT_DATA_BUFFERF_DISCONTINUITY = 8
_DMO_INPUT_STATUS_FLAGS = Int32
DMO_INPUT_STATUSF_ACCEPT_DATA = 1
_DMO_INPUT_STREAM_INFO_FLAGS = Int32
DMO_INPUT_STREAMF_WHOLE_SAMPLES = 1
DMO_INPUT_STREAMF_SINGLE_SAMPLE_PER_BUFFER = 2
DMO_INPUT_STREAMF_FIXED_SAMPLE_SIZE = 4
DMO_INPUT_STREAMF_HOLDS_BUFFERS = 8
_DMO_OUTPUT_DATA_BUFFER_FLAGS = Int32
DMO_OUTPUT_DATA_BUFFERF_SYNCPOINT = 1
DMO_OUTPUT_DATA_BUFFERF_TIME = 2
DMO_OUTPUT_DATA_BUFFERF_TIMELENGTH = 4
DMO_OUTPUT_DATA_BUFFERF_DISCONTINUITY = 8
DMO_OUTPUT_DATA_BUFFERF_INCOMPLETE = 16777216
_DMO_OUTPUT_STREAM_INFO_FLAGS = Int32
DMO_OUTPUT_STREAMF_WHOLE_SAMPLES = 1
DMO_OUTPUT_STREAMF_SINGLE_SAMPLE_PER_BUFFER = 2
DMO_OUTPUT_STREAMF_FIXED_SAMPLE_SIZE = 4
DMO_OUTPUT_STREAMF_DISCARDABLE = 8
DMO_OUTPUT_STREAMF_OPTIONAL = 16
_DMO_PROCESS_OUTPUT_FLAGS = Int32
DMO_PROCESS_OUTPUT_DISCARD_WHEN_NO_BUFFER = 1
_DMO_QUALITY_STATUS_FLAGS = Int32
DMO_QUALITY_STATUS_ENABLED = 1
_DMO_SET_TYPE_FLAGS = Int32
DMO_SET_TYPEF_TEST_ONLY = 1
DMO_SET_TYPEF_CLEAR = 2
_DMO_VIDEO_OUTPUT_STREAM_FLAGS = Int32
DMO_VOSF_NEEDS_PREVIOUS_SAMPLE = 1
DMO_E_INVALIDSTREAMINDEX = -2147220991
DMO_E_INVALIDTYPE = -2147220990
DMO_E_TYPE_NOT_SET = -2147220989
DMO_E_NOTACCEPTING = -2147220988
DMO_E_TYPE_NOT_ACCEPTED = -2147220987
DMO_E_NO_MORE_ITEMS = -2147220986
def _define_DMOCATEGORY_AUDIO_DECODER():
    return Guid('57f2db8b-e6bb-4513-9d-43-dc-d2-a6-59-31-25')
def _define_DMOCATEGORY_AUDIO_ENCODER():
    return Guid('33d9a761-90c8-11d0-bd-43-00-a0-c9-11-ce-86')
def _define_DMOCATEGORY_VIDEO_DECODER():
    return Guid('4a69b442-28be-4991-96-9c-b5-00-ad-f5-d8-a8')
def _define_DMOCATEGORY_VIDEO_ENCODER():
    return Guid('33d9a760-90c8-11d0-bd-43-00-a0-c9-11-ce-86')
def _define_DMOCATEGORY_AUDIO_EFFECT():
    return Guid('f3602b3f-0592-48df-a4-cd-67-47-21-e7-eb-eb')
def _define_DMOCATEGORY_VIDEO_EFFECT():
    return Guid('d990ee14-776c-4723-be-46-3d-a2-f5-6f-10-b9')
def _define_DMOCATEGORY_AUDIO_CAPTURE_EFFECT():
    return Guid('f665aaba-3e09-4920-aa-5f-21-98-11-14-8f-09')
def _define_DMOCATEGORY_ACOUSTIC_ECHO_CANCEL():
    return Guid('bf963d80-c559-11d0-8a-2b-00-a0-c9-25-5a-c1')
def _define_DMOCATEGORY_AUDIO_NOISE_SUPPRESS():
    return Guid('e07f903f-62fd-4e60-8c-dd-de-a7-23-66-65-b5')
def _define_DMOCATEGORY_AGC():
    return Guid('e88c9ba0-c557-11d0-8a-2b-00-a0-c9-25-5a-c1')
def _define_DMORegister():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(Guid),UInt32,UInt32,POINTER(win32more.Media.DxMediaObjects.DMO_PARTIAL_MEDIATYPE_head),UInt32,POINTER(win32more.Media.DxMediaObjects.DMO_PARTIAL_MEDIATYPE_head))(('DMORegister', windll['msdmo.dll']), ((1, 'szName'),(1, 'clsidDMO'),(1, 'guidCategory'),(1, 'dwFlags'),(1, 'cInTypes'),(1, 'pInTypes'),(1, 'cOutTypes'),(1, 'pOutTypes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DMOUnregister():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid))(('DMOUnregister', windll['msdmo.dll']), ((1, 'clsidDMO'),(1, 'guidCategory'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DMOEnum():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,UInt32,POINTER(win32more.Media.DxMediaObjects.DMO_PARTIAL_MEDIATYPE_head),UInt32,POINTER(win32more.Media.DxMediaObjects.DMO_PARTIAL_MEDIATYPE_head),POINTER(win32more.Media.DxMediaObjects.IEnumDMO_head))(('DMOEnum', windll['msdmo.dll']), ((1, 'guidCategory'),(1, 'dwFlags'),(1, 'cInTypes'),(1, 'pInTypes'),(1, 'cOutTypes'),(1, 'pOutTypes'),(1, 'ppEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DMOGetTypes():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(UInt32),POINTER(win32more.Media.DxMediaObjects.DMO_PARTIAL_MEDIATYPE_head),UInt32,POINTER(UInt32),POINTER(win32more.Media.DxMediaObjects.DMO_PARTIAL_MEDIATYPE_head))(('DMOGetTypes', windll['msdmo.dll']), ((1, 'clsidDMO'),(1, 'ulInputTypesRequested'),(1, 'pulInputTypesSupplied'),(1, 'pInputTypes'),(1, 'ulOutputTypesRequested'),(1, 'pulOutputTypesSupplied'),(1, 'pOutputTypes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DMOGetName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PWSTR)(('DMOGetName', windll['msdmo.dll']), ((1, 'clsidDMO'),(1, 'szName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MoInitMediaType():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head),UInt32)(('MoInitMediaType', windll['msdmo.dll']), ((1, 'pmt'),(1, 'cbFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MoFreeMediaType():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head))(('MoFreeMediaType', windll['msdmo.dll']), ((1, 'pmt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MoCopyMediaType():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head),POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head))(('MoCopyMediaType', windll['msdmo.dll']), ((1, 'pmtDest'),(1, 'pmtSrc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MoCreateMediaType():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head)),UInt32)(('MoCreateMediaType', windll['msdmo.dll']), ((1, 'ppmt'),(1, 'cbFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MoDeleteMediaType():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head))(('MoDeleteMediaType', windll['msdmo.dll']), ((1, 'pmt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MoDuplicateMediaType():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head)),POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head))(('MoDuplicateMediaType', windll['msdmo.dll']), ((1, 'ppmtDest'),(1, 'pmtSrc'),))
    except (FileNotFoundError, AttributeError):
        return None
DMO_ENUM_FLAGS = Int32
DMO_ENUMF_INCLUDE_KEYED = 1
def _define_DMO_MEDIA_TYPE_head():
    class DMO_MEDIA_TYPE(Structure):
        pass
    return DMO_MEDIA_TYPE
def _define_DMO_MEDIA_TYPE():
    DMO_MEDIA_TYPE = win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head
    DMO_MEDIA_TYPE._fields_ = [
        ('majortype', Guid),
        ('subtype', Guid),
        ('bFixedSizeSamples', win32more.Foundation.BOOL),
        ('bTemporalCompression', win32more.Foundation.BOOL),
        ('lSampleSize', UInt32),
        ('formattype', Guid),
        ('pUnk', win32more.System.Com.IUnknown_head),
        ('cbFormat', UInt32),
        ('pbFormat', c_char_p_no),
    ]
    return DMO_MEDIA_TYPE
def _define_DMO_OUTPUT_DATA_BUFFER_head():
    class DMO_OUTPUT_DATA_BUFFER(Structure):
        pass
    return DMO_OUTPUT_DATA_BUFFER
def _define_DMO_OUTPUT_DATA_BUFFER():
    DMO_OUTPUT_DATA_BUFFER = win32more.Media.DxMediaObjects.DMO_OUTPUT_DATA_BUFFER_head
    DMO_OUTPUT_DATA_BUFFER._fields_ = [
        ('pBuffer', win32more.Media.DxMediaObjects.IMediaBuffer_head),
        ('dwStatus', UInt32),
        ('rtTimestamp', Int64),
        ('rtTimelength', Int64),
    ]
    return DMO_OUTPUT_DATA_BUFFER
def _define_DMO_PARTIAL_MEDIATYPE_head():
    class DMO_PARTIAL_MEDIATYPE(Structure):
        pass
    return DMO_PARTIAL_MEDIATYPE
def _define_DMO_PARTIAL_MEDIATYPE():
    DMO_PARTIAL_MEDIATYPE = win32more.Media.DxMediaObjects.DMO_PARTIAL_MEDIATYPE_head
    DMO_PARTIAL_MEDIATYPE._fields_ = [
        ('type', Guid),
        ('subtype', Guid),
    ]
    return DMO_PARTIAL_MEDIATYPE
DMO_REGISTER_FLAGS = Int32
DMO_REGISTERF_IS_KEYED = 1
def _define_IDMOQualityControl_head():
    class IDMOQualityControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('65abea96-cf36-453f-af-8a-70-5e-98-f1-62-60')
    return IDMOQualityControl
def _define_IDMOQualityControl():
    IDMOQualityControl = win32more.Media.DxMediaObjects.IDMOQualityControl_head
    IDMOQualityControl.SetNow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int64)(3, 'SetNow', ((1, 'rtNow'),)))
    IDMOQualityControl.SetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'SetStatus', ((1, 'dwFlags'),)))
    IDMOQualityControl.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(5, 'GetStatus', ((1, 'pdwFlags'),)))
    win32more.System.Com.IUnknown
    return IDMOQualityControl
def _define_IDMOVideoOutputOptimizations_head():
    class IDMOVideoOutputOptimizations(win32more.System.Com.IUnknown_head):
        Guid = Guid('be8f4f4e-5b16-4d29-b3-50-7f-6b-5d-92-98-ac')
    return IDMOVideoOutputOptimizations
def _define_IDMOVideoOutputOptimizations():
    IDMOVideoOutputOptimizations = win32more.Media.DxMediaObjects.IDMOVideoOutputOptimizations_head
    IDMOVideoOutputOptimizations.QueryOperationModePreferences = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32))(3, 'QueryOperationModePreferences', ((1, 'ulOutputStreamIndex'),(1, 'pdwRequestedCapabilities'),)))
    IDMOVideoOutputOptimizations.SetOperationMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32)(4, 'SetOperationMode', ((1, 'ulOutputStreamIndex'),(1, 'dwEnabledFeatures'),)))
    IDMOVideoOutputOptimizations.GetCurrentOperationMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32))(5, 'GetCurrentOperationMode', ((1, 'ulOutputStreamIndex'),(1, 'pdwEnabledFeatures'),)))
    IDMOVideoOutputOptimizations.GetCurrentSampleRequirements = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32))(6, 'GetCurrentSampleRequirements', ((1, 'ulOutputStreamIndex'),(1, 'pdwRequestedFeatures'),)))
    win32more.System.Com.IUnknown
    return IDMOVideoOutputOptimizations
def _define_IEnumDMO_head():
    class IEnumDMO(win32more.System.Com.IUnknown_head):
        Guid = Guid('2c3cd98a-2bfa-4a53-9c-27-52-49-ba-64-ba-0f')
    return IEnumDMO
def _define_IEnumDMO():
    IEnumDMO = win32more.Media.DxMediaObjects.IEnumDMO_head
    IEnumDMO.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(win32more.Foundation.PWSTR),POINTER(UInt32))(3, 'Next', ((1, 'cItemsToFetch'),(1, 'pCLSID'),(1, 'Names'),(1, 'pcItemsFetched'),)))
    IEnumDMO.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'cItemsToSkip'),)))
    IEnumDMO.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumDMO.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DxMediaObjects.IEnumDMO_head))(6, 'Clone', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return IEnumDMO
def _define_IMediaBuffer_head():
    class IMediaBuffer(win32more.System.Com.IUnknown_head):
        Guid = Guid('59eff8b9-938c-4a26-82-f2-95-cb-84-cd-c8-37')
    return IMediaBuffer
def _define_IMediaBuffer():
    IMediaBuffer = win32more.Media.DxMediaObjects.IMediaBuffer_head
    IMediaBuffer.SetLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(3, 'SetLength', ((1, 'cbLength'),)))
    IMediaBuffer.GetMaxLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(4, 'GetMaxLength', ((1, 'pcbMaxLength'),)))
    IMediaBuffer.GetBufferAndLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no),POINTER(UInt32))(5, 'GetBufferAndLength', ((1, 'ppBuffer'),(1, 'pcbLength'),)))
    win32more.System.Com.IUnknown
    return IMediaBuffer
def _define_IMediaObject_head():
    class IMediaObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('d8ad0f58-5494-4102-97-c5-ec-79-8e-59-bc-f4')
    return IMediaObject
def _define_IMediaObject():
    IMediaObject = win32more.Media.DxMediaObjects.IMediaObject_head
    IMediaObject.GetStreamCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32))(3, 'GetStreamCount', ((1, 'pcInputStreams'),(1, 'pcOutputStreams'),)))
    IMediaObject.GetInputStreamInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32))(4, 'GetInputStreamInfo', ((1, 'dwInputStreamIndex'),(1, 'pdwFlags'),)))
    IMediaObject.GetOutputStreamInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32))(5, 'GetOutputStreamInfo', ((1, 'dwOutputStreamIndex'),(1, 'pdwFlags'),)))
    IMediaObject.GetInputType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head))(6, 'GetInputType', ((1, 'dwInputStreamIndex'),(1, 'dwTypeIndex'),(1, 'pmt'),)))
    IMediaObject.GetOutputType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head))(7, 'GetOutputType', ((1, 'dwOutputStreamIndex'),(1, 'dwTypeIndex'),(1, 'pmt'),)))
    IMediaObject.SetInputType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head),UInt32)(8, 'SetInputType', ((1, 'dwInputStreamIndex'),(1, 'pmt'),(1, 'dwFlags'),)))
    IMediaObject.SetOutputType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head),UInt32)(9, 'SetOutputType', ((1, 'dwOutputStreamIndex'),(1, 'pmt'),(1, 'dwFlags'),)))
    IMediaObject.GetInputCurrentType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head))(10, 'GetInputCurrentType', ((1, 'dwInputStreamIndex'),(1, 'pmt'),)))
    IMediaObject.GetOutputCurrentType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.DxMediaObjects.DMO_MEDIA_TYPE_head))(11, 'GetOutputCurrentType', ((1, 'dwOutputStreamIndex'),(1, 'pmt'),)))
    IMediaObject.GetInputSizeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(12, 'GetInputSizeInfo', ((1, 'dwInputStreamIndex'),(1, 'pcbSize'),(1, 'pcbMaxLookahead'),(1, 'pcbAlignment'),)))
    IMediaObject.GetOutputSizeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(UInt32))(13, 'GetOutputSizeInfo', ((1, 'dwOutputStreamIndex'),(1, 'pcbSize'),(1, 'pcbAlignment'),)))
    IMediaObject.GetInputMaxLatency = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Int64))(14, 'GetInputMaxLatency', ((1, 'dwInputStreamIndex'),(1, 'prtMaxLatency'),)))
    IMediaObject.SetInputMaxLatency = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int64)(15, 'SetInputMaxLatency', ((1, 'dwInputStreamIndex'),(1, 'rtMaxLatency'),)))
    IMediaObject.Flush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(16, 'Flush', ()))
    IMediaObject.Discontinuity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(17, 'Discontinuity', ((1, 'dwInputStreamIndex'),)))
    IMediaObject.AllocateStreamingResources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(18, 'AllocateStreamingResources', ()))
    IMediaObject.FreeStreamingResources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(19, 'FreeStreamingResources', ()))
    IMediaObject.GetInputStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32))(20, 'GetInputStatus', ((1, 'dwInputStreamIndex'),(1, 'dwFlags'),)))
    IMediaObject.ProcessInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.DxMediaObjects.IMediaBuffer_head,UInt32,Int64,Int64)(21, 'ProcessInput', ((1, 'dwInputStreamIndex'),(1, 'pBuffer'),(1, 'dwFlags'),(1, 'rtTimestamp'),(1, 'rtTimelength'),)))
    IMediaObject.ProcessOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Media.DxMediaObjects.DMO_OUTPUT_DATA_BUFFER_head),POINTER(UInt32))(22, 'ProcessOutput', ((1, 'dwFlags'),(1, 'cOutputBufferCount'),(1, 'pOutputBuffers'),(1, 'pdwStatus'),)))
    IMediaObject.Lock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(23, 'Lock', ((1, 'bLock'),)))
    win32more.System.Com.IUnknown
    return IMediaObject
def _define_IMediaObjectInPlace_head():
    class IMediaObjectInPlace(win32more.System.Com.IUnknown_head):
        Guid = Guid('651b9ad0-0fc7-4aa9-95-38-d8-99-31-01-07-41')
    return IMediaObjectInPlace
def _define_IMediaObjectInPlace():
    IMediaObjectInPlace = win32more.Media.DxMediaObjects.IMediaObjectInPlace_head
    IMediaObjectInPlace.Process = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_char_p_no,Int64,UInt32)(3, 'Process', ((1, 'ulSize'),(1, 'pData'),(1, 'refTimeStart'),(1, 'dwFlags'),)))
    IMediaObjectInPlace.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.DxMediaObjects.IMediaObjectInPlace_head))(4, 'Clone', ((1, 'ppMediaObject'),)))
    IMediaObjectInPlace.GetLatency = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int64))(5, 'GetLatency', ((1, 'pLatencyTime'),)))
    win32more.System.Com.IUnknown
    return IMediaObjectInPlace
__all__ = [
    "DMOCATEGORY_ACOUSTIC_ECHO_CANCEL",
    "DMOCATEGORY_AGC",
    "DMOCATEGORY_AUDIO_CAPTURE_EFFECT",
    "DMOCATEGORY_AUDIO_DECODER",
    "DMOCATEGORY_AUDIO_EFFECT",
    "DMOCATEGORY_AUDIO_ENCODER",
    "DMOCATEGORY_AUDIO_NOISE_SUPPRESS",
    "DMOCATEGORY_VIDEO_DECODER",
    "DMOCATEGORY_VIDEO_EFFECT",
    "DMOCATEGORY_VIDEO_ENCODER",
    "DMOEnum",
    "DMOGetName",
    "DMOGetTypes",
    "DMORegister",
    "DMOUnregister",
    "DMO_ENUMF_INCLUDE_KEYED",
    "DMO_ENUM_FLAGS",
    "DMO_E_INVALIDSTREAMINDEX",
    "DMO_E_INVALIDTYPE",
    "DMO_E_NOTACCEPTING",
    "DMO_E_NO_MORE_ITEMS",
    "DMO_E_TYPE_NOT_ACCEPTED",
    "DMO_E_TYPE_NOT_SET",
    "DMO_INPLACE_NORMAL",
    "DMO_INPLACE_ZERO",
    "DMO_INPUT_DATA_BUFFERF_DISCONTINUITY",
    "DMO_INPUT_DATA_BUFFERF_SYNCPOINT",
    "DMO_INPUT_DATA_BUFFERF_TIME",
    "DMO_INPUT_DATA_BUFFERF_TIMELENGTH",
    "DMO_INPUT_STATUSF_ACCEPT_DATA",
    "DMO_INPUT_STREAMF_FIXED_SAMPLE_SIZE",
    "DMO_INPUT_STREAMF_HOLDS_BUFFERS",
    "DMO_INPUT_STREAMF_SINGLE_SAMPLE_PER_BUFFER",
    "DMO_INPUT_STREAMF_WHOLE_SAMPLES",
    "DMO_MEDIA_TYPE",
    "DMO_OUTPUT_DATA_BUFFER",
    "DMO_OUTPUT_DATA_BUFFERF_DISCONTINUITY",
    "DMO_OUTPUT_DATA_BUFFERF_INCOMPLETE",
    "DMO_OUTPUT_DATA_BUFFERF_SYNCPOINT",
    "DMO_OUTPUT_DATA_BUFFERF_TIME",
    "DMO_OUTPUT_DATA_BUFFERF_TIMELENGTH",
    "DMO_OUTPUT_STREAMF_DISCARDABLE",
    "DMO_OUTPUT_STREAMF_FIXED_SAMPLE_SIZE",
    "DMO_OUTPUT_STREAMF_OPTIONAL",
    "DMO_OUTPUT_STREAMF_SINGLE_SAMPLE_PER_BUFFER",
    "DMO_OUTPUT_STREAMF_WHOLE_SAMPLES",
    "DMO_PARTIAL_MEDIATYPE",
    "DMO_PROCESS_OUTPUT_DISCARD_WHEN_NO_BUFFER",
    "DMO_QUALITY_STATUS_ENABLED",
    "DMO_REGISTERF_IS_KEYED",
    "DMO_REGISTER_FLAGS",
    "DMO_SET_TYPEF_CLEAR",
    "DMO_SET_TYPEF_TEST_ONLY",
    "DMO_VOSF_NEEDS_PREVIOUS_SAMPLE",
    "IDMOQualityControl",
    "IDMOVideoOutputOptimizations",
    "IEnumDMO",
    "IMediaBuffer",
    "IMediaObject",
    "IMediaObjectInPlace",
    "MoCopyMediaType",
    "MoCreateMediaType",
    "MoDeleteMediaType",
    "MoDuplicateMediaType",
    "MoFreeMediaType",
    "MoInitMediaType",
    "_DMO_INPLACE_PROCESS_FLAGS",
    "_DMO_INPUT_DATA_BUFFER_FLAGS",
    "_DMO_INPUT_STATUS_FLAGS",
    "_DMO_INPUT_STREAM_INFO_FLAGS",
    "_DMO_OUTPUT_DATA_BUFFER_FLAGS",
    "_DMO_OUTPUT_STREAM_INFO_FLAGS",
    "_DMO_PROCESS_OUTPUT_FLAGS",
    "_DMO_QUALITY_STATUS_FLAGS",
    "_DMO_SET_TYPE_FLAGS",
    "_DMO_VIDEO_OUTPUT_STREAM_FLAGS",
]
