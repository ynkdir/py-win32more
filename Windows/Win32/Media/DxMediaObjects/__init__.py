from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Media.DxMediaObjects
import Windows.Win32.System.Com
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
DMO_E_INVALIDSTREAMINDEX: Windows.Win32.Foundation.HRESULT = -2147220991
DMO_E_INVALIDTYPE: Windows.Win32.Foundation.HRESULT = -2147220990
DMO_E_TYPE_NOT_SET: Windows.Win32.Foundation.HRESULT = -2147220989
DMO_E_NOTACCEPTING: Windows.Win32.Foundation.HRESULT = -2147220988
DMO_E_TYPE_NOT_ACCEPTED: Windows.Win32.Foundation.HRESULT = -2147220987
DMO_E_NO_MORE_ITEMS: Windows.Win32.Foundation.HRESULT = -2147220986
DMOCATEGORY_AUDIO_DECODER: Guid = Guid('57f2db8b-e6bb-4513-9d-43-dc-d2-a6-59-31-25')
DMOCATEGORY_AUDIO_ENCODER: Guid = Guid('33d9a761-90c8-11d0-bd-43-00-a0-c9-11-ce-86')
DMOCATEGORY_VIDEO_DECODER: Guid = Guid('4a69b442-28be-4991-96-9c-b5-00-ad-f5-d8-a8')
DMOCATEGORY_VIDEO_ENCODER: Guid = Guid('33d9a760-90c8-11d0-bd-43-00-a0-c9-11-ce-86')
DMOCATEGORY_AUDIO_EFFECT: Guid = Guid('f3602b3f-0592-48df-a4-cd-67-47-21-e7-eb-eb')
DMOCATEGORY_VIDEO_EFFECT: Guid = Guid('d990ee14-776c-4723-be-46-3d-a2-f5-6f-10-b9')
DMOCATEGORY_AUDIO_CAPTURE_EFFECT: Guid = Guid('f665aaba-3e09-4920-aa-5f-21-98-11-14-8f-09')
DMOCATEGORY_ACOUSTIC_ECHO_CANCEL: Guid = Guid('bf963d80-c559-11d0-8a-2b-00-a0-c9-25-5a-c1')
DMOCATEGORY_AUDIO_NOISE_SUPPRESS: Guid = Guid('e07f903f-62fd-4e60-8c-dd-de-a7-23-66-65-b5')
DMOCATEGORY_AGC: Guid = Guid('e88c9ba0-c557-11d0-8a-2b-00-a0-c9-25-5a-c1')
@winfunctype('msdmo.dll')
def DMORegister(szName: Windows.Win32.Foundation.PWSTR, clsidDMO: POINTER(Guid), guidCategory: POINTER(Guid), dwFlags: UInt32, cInTypes: UInt32, pInTypes: POINTER(Windows.Win32.Media.DxMediaObjects.DMO_PARTIAL_MEDIATYPE_head), cOutTypes: UInt32, pOutTypes: POINTER(Windows.Win32.Media.DxMediaObjects.DMO_PARTIAL_MEDIATYPE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdmo.dll')
def DMOUnregister(clsidDMO: POINTER(Guid), guidCategory: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdmo.dll')
def DMOEnum(guidCategory: POINTER(Guid), dwFlags: UInt32, cInTypes: UInt32, pInTypes: POINTER(Windows.Win32.Media.DxMediaObjects.DMO_PARTIAL_MEDIATYPE_head), cOutTypes: UInt32, pOutTypes: POINTER(Windows.Win32.Media.DxMediaObjects.DMO_PARTIAL_MEDIATYPE_head), ppEnum: POINTER(Windows.Win32.Media.DxMediaObjects.IEnumDMO_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdmo.dll')
def DMOGetTypes(clsidDMO: POINTER(Guid), ulInputTypesRequested: UInt32, pulInputTypesSupplied: POINTER(UInt32), pInputTypes: POINTER(Windows.Win32.Media.DxMediaObjects.DMO_PARTIAL_MEDIATYPE_head), ulOutputTypesRequested: UInt32, pulOutputTypesSupplied: POINTER(UInt32), pOutputTypes: POINTER(Windows.Win32.Media.DxMediaObjects.DMO_PARTIAL_MEDIATYPE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdmo.dll')
def DMOGetName(clsidDMO: POINTER(Guid), szName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdmo.dll')
def MoInitMediaType(pmt: POINTER(Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE_head), cbFormat: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdmo.dll')
def MoFreeMediaType(pmt: POINTER(Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdmo.dll')
def MoCopyMediaType(pmtDest: POINTER(Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE_head), pmtSrc: POINTER(Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdmo.dll')
def MoCreateMediaType(ppmt: POINTER(POINTER(Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE_head)), cbFormat: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdmo.dll')
def MoDeleteMediaType(pmt: POINTER(Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdmo.dll')
def MoDuplicateMediaType(ppmtDest: POINTER(POINTER(Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE_head)), pmtSrc: POINTER(Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE_head)) -> Windows.Win32.Foundation.HRESULT: ...
DMO_ENUM_FLAGS = Int32
DMO_ENUMF_INCLUDE_KEYED: DMO_ENUM_FLAGS = 1
class DMO_MEDIA_TYPE(Structure):
    majortype: Guid
    subtype: Guid
    bFixedSizeSamples: Windows.Win32.Foundation.BOOL
    bTemporalCompression: Windows.Win32.Foundation.BOOL
    lSampleSize: UInt32
    formattype: Guid
    pUnk: Windows.Win32.System.Com.IUnknown_head
    cbFormat: UInt32
    pbFormat: c_char_p_no
class DMO_OUTPUT_DATA_BUFFER(Structure):
    pBuffer: Windows.Win32.Media.DxMediaObjects.IMediaBuffer_head
    dwStatus: UInt32
    rtTimestamp: Int64
    rtTimelength: Int64
class DMO_PARTIAL_MEDIATYPE(Structure):
    type: Guid
    subtype: Guid
DMO_REGISTER_FLAGS = Int32
DMO_REGISTERF_IS_KEYED: DMO_REGISTER_FLAGS = 1
class IDMOQualityControl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('65abea96-cf36-453f-af-8a-70-5e-98-f1-62-60')
    @commethod(3)
    def SetNow(rtNow: Int64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetStatus(dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStatus(pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IDMOVideoOutputOptimizations(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('be8f4f4e-5b16-4d29-b3-50-7f-6b-5d-92-98-ac')
    @commethod(3)
    def QueryOperationModePreferences(ulOutputStreamIndex: UInt32, pdwRequestedCapabilities: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetOperationMode(ulOutputStreamIndex: UInt32, dwEnabledFeatures: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrentOperationMode(ulOutputStreamIndex: UInt32, pdwEnabledFeatures: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCurrentSampleRequirements(ulOutputStreamIndex: UInt32, pdwRequestedFeatures: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumDMO(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2c3cd98a-2bfa-4a53-9c-27-52-49-ba-64-ba-0f')
    @commethod(3)
    def Next(cItemsToFetch: UInt32, pCLSID: POINTER(Guid), Names: POINTER(Windows.Win32.Foundation.PWSTR), pcItemsFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(cItemsToSkip: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(Windows.Win32.Media.DxMediaObjects.IEnumDMO_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMediaBuffer(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('59eff8b9-938c-4a26-82-f2-95-cb-84-cd-c8-37')
    @commethod(3)
    def SetLength(cbLength: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMaxLength(pcbMaxLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetBufferAndLength(ppBuffer: POINTER(c_char_p_no), pcbLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMediaObject(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d8ad0f58-5494-4102-97-c5-ec-79-8e-59-bc-f4')
    @commethod(3)
    def GetStreamCount(pcInputStreams: POINTER(UInt32), pcOutputStreams: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInputStreamInfo(dwInputStreamIndex: UInt32, pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetOutputStreamInfo(dwOutputStreamIndex: UInt32, pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetInputType(dwInputStreamIndex: UInt32, dwTypeIndex: UInt32, pmt: POINTER(Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetOutputType(dwOutputStreamIndex: UInt32, dwTypeIndex: UInt32, pmt: POINTER(Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetInputType(dwInputStreamIndex: UInt32, pmt: POINTER(Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE_head), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetOutputType(dwOutputStreamIndex: UInt32, pmt: POINTER(Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE_head), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetInputCurrentType(dwInputStreamIndex: UInt32, pmt: POINTER(Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetOutputCurrentType(dwOutputStreamIndex: UInt32, pmt: POINTER(Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetInputSizeInfo(dwInputStreamIndex: UInt32, pcbSize: POINTER(UInt32), pcbMaxLookahead: POINTER(UInt32), pcbAlignment: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetOutputSizeInfo(dwOutputStreamIndex: UInt32, pcbSize: POINTER(UInt32), pcbAlignment: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetInputMaxLatency(dwInputStreamIndex: UInt32, prtMaxLatency: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetInputMaxLatency(dwInputStreamIndex: UInt32, rtMaxLatency: Int64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Flush() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Discontinuity(dwInputStreamIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def AllocateStreamingResources() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def FreeStreamingResources() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetInputStatus(dwInputStreamIndex: UInt32, dwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def ProcessInput(dwInputStreamIndex: UInt32, pBuffer: Windows.Win32.Media.DxMediaObjects.IMediaBuffer_head, dwFlags: UInt32, rtTimestamp: Int64, rtTimelength: Int64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def ProcessOutput(dwFlags: UInt32, cOutputBufferCount: UInt32, pOutputBuffers: POINTER(Windows.Win32.Media.DxMediaObjects.DMO_OUTPUT_DATA_BUFFER_head), pdwStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Lock(bLock: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IMediaObjectInPlace(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('651b9ad0-0fc7-4aa9-95-38-d8-99-31-01-07-41')
    @commethod(3)
    def Process(ulSize: UInt32, pData: c_char_p_no, refTimeStart: Int64, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Clone(ppMediaObject: POINTER(Windows.Win32.Media.DxMediaObjects.IMediaObjectInPlace_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLatency(pLatencyTime: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
_DMO_INPLACE_PROCESS_FLAGS = Int32
DMO_INPLACE_NORMAL: _DMO_INPLACE_PROCESS_FLAGS = 0
DMO_INPLACE_ZERO: _DMO_INPLACE_PROCESS_FLAGS = 1
_DMO_INPUT_DATA_BUFFER_FLAGS = Int32
DMO_INPUT_DATA_BUFFERF_SYNCPOINT: _DMO_INPUT_DATA_BUFFER_FLAGS = 1
DMO_INPUT_DATA_BUFFERF_TIME: _DMO_INPUT_DATA_BUFFER_FLAGS = 2
DMO_INPUT_DATA_BUFFERF_TIMELENGTH: _DMO_INPUT_DATA_BUFFER_FLAGS = 4
DMO_INPUT_DATA_BUFFERF_DISCONTINUITY: _DMO_INPUT_DATA_BUFFER_FLAGS = 8
_DMO_INPUT_STATUS_FLAGS = Int32
DMO_INPUT_STATUSF_ACCEPT_DATA: _DMO_INPUT_STATUS_FLAGS = 1
_DMO_INPUT_STREAM_INFO_FLAGS = Int32
DMO_INPUT_STREAMF_WHOLE_SAMPLES: _DMO_INPUT_STREAM_INFO_FLAGS = 1
DMO_INPUT_STREAMF_SINGLE_SAMPLE_PER_BUFFER: _DMO_INPUT_STREAM_INFO_FLAGS = 2
DMO_INPUT_STREAMF_FIXED_SAMPLE_SIZE: _DMO_INPUT_STREAM_INFO_FLAGS = 4
DMO_INPUT_STREAMF_HOLDS_BUFFERS: _DMO_INPUT_STREAM_INFO_FLAGS = 8
_DMO_OUTPUT_DATA_BUFFER_FLAGS = Int32
DMO_OUTPUT_DATA_BUFFERF_SYNCPOINT: _DMO_OUTPUT_DATA_BUFFER_FLAGS = 1
DMO_OUTPUT_DATA_BUFFERF_TIME: _DMO_OUTPUT_DATA_BUFFER_FLAGS = 2
DMO_OUTPUT_DATA_BUFFERF_TIMELENGTH: _DMO_OUTPUT_DATA_BUFFER_FLAGS = 4
DMO_OUTPUT_DATA_BUFFERF_DISCONTINUITY: _DMO_OUTPUT_DATA_BUFFER_FLAGS = 8
DMO_OUTPUT_DATA_BUFFERF_INCOMPLETE: _DMO_OUTPUT_DATA_BUFFER_FLAGS = 16777216
_DMO_OUTPUT_STREAM_INFO_FLAGS = Int32
DMO_OUTPUT_STREAMF_WHOLE_SAMPLES: _DMO_OUTPUT_STREAM_INFO_FLAGS = 1
DMO_OUTPUT_STREAMF_SINGLE_SAMPLE_PER_BUFFER: _DMO_OUTPUT_STREAM_INFO_FLAGS = 2
DMO_OUTPUT_STREAMF_FIXED_SAMPLE_SIZE: _DMO_OUTPUT_STREAM_INFO_FLAGS = 4
DMO_OUTPUT_STREAMF_DISCARDABLE: _DMO_OUTPUT_STREAM_INFO_FLAGS = 8
DMO_OUTPUT_STREAMF_OPTIONAL: _DMO_OUTPUT_STREAM_INFO_FLAGS = 16
_DMO_PROCESS_OUTPUT_FLAGS = Int32
DMO_PROCESS_OUTPUT_DISCARD_WHEN_NO_BUFFER: _DMO_PROCESS_OUTPUT_FLAGS = 1
_DMO_QUALITY_STATUS_FLAGS = Int32
DMO_QUALITY_STATUS_ENABLED: _DMO_QUALITY_STATUS_FLAGS = 1
_DMO_SET_TYPE_FLAGS = Int32
DMO_SET_TYPEF_TEST_ONLY: _DMO_SET_TYPE_FLAGS = 1
DMO_SET_TYPEF_CLEAR: _DMO_SET_TYPE_FLAGS = 2
_DMO_VIDEO_OUTPUT_STREAM_FLAGS = Int32
DMO_VOSF_NEEDS_PREVIOUS_SAMPLE: _DMO_VIDEO_OUTPUT_STREAM_FLAGS = 1
make_head(_module, 'DMO_MEDIA_TYPE')
make_head(_module, 'DMO_OUTPUT_DATA_BUFFER')
make_head(_module, 'DMO_PARTIAL_MEDIATYPE')
make_head(_module, 'IDMOQualityControl')
make_head(_module, 'IDMOVideoOutputOptimizations')
make_head(_module, 'IEnumDMO')
make_head(_module, 'IMediaBuffer')
make_head(_module, 'IMediaObject')
make_head(_module, 'IMediaObjectInPlace')
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
_arch_optional = [
]
