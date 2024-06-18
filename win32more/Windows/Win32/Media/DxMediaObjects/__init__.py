from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Media.DxMediaObjects
import win32more.Windows.Win32.System.Com
DMO_E_INVALIDSTREAMINDEX: win32more.Windows.Win32.Foundation.HRESULT = -2147220991
DMO_E_INVALIDTYPE: win32more.Windows.Win32.Foundation.HRESULT = -2147220990
DMO_E_TYPE_NOT_SET: win32more.Windows.Win32.Foundation.HRESULT = -2147220989
DMO_E_NOTACCEPTING: win32more.Windows.Win32.Foundation.HRESULT = -2147220988
DMO_E_TYPE_NOT_ACCEPTED: win32more.Windows.Win32.Foundation.HRESULT = -2147220987
DMO_E_NO_MORE_ITEMS: win32more.Windows.Win32.Foundation.HRESULT = -2147220986
DMOCATEGORY_AUDIO_DECODER: Guid = Guid('{57f2db8b-e6bb-4513-9d43-dcd2a6593125}')
DMOCATEGORY_AUDIO_ENCODER: Guid = Guid('{33d9a761-90c8-11d0-bd43-00a0c911ce86}')
DMOCATEGORY_VIDEO_DECODER: Guid = Guid('{4a69b442-28be-4991-969c-b500adf5d8a8}')
DMOCATEGORY_VIDEO_ENCODER: Guid = Guid('{33d9a760-90c8-11d0-bd43-00a0c911ce86}')
DMOCATEGORY_AUDIO_EFFECT: Guid = Guid('{f3602b3f-0592-48df-a4cd-674721e7ebeb}')
DMOCATEGORY_VIDEO_EFFECT: Guid = Guid('{d990ee14-776c-4723-be46-3da2f56f10b9}')
DMOCATEGORY_AUDIO_CAPTURE_EFFECT: Guid = Guid('{f665aaba-3e09-4920-aa5f-219811148f09}')
DMOCATEGORY_ACOUSTIC_ECHO_CANCEL: Guid = Guid('{bf963d80-c559-11d0-8a2b-00a0c9255ac1}')
DMOCATEGORY_AUDIO_NOISE_SUPPRESS: Guid = Guid('{e07f903f-62fd-4e60-8cdd-dea7236665b5}')
DMOCATEGORY_AGC: Guid = Guid('{e88c9ba0-c557-11d0-8a2b-00a0c9255ac1}')
@winfunctype('msdmo.dll')
def DMORegister(szName: win32more.Windows.Win32.Foundation.PWSTR, clsidDMO: POINTER(Guid), guidCategory: POINTER(Guid), dwFlags: UInt32, cInTypes: UInt32, pInTypes: POINTER(win32more.Windows.Win32.Media.DxMediaObjects.DMO_PARTIAL_MEDIATYPE), cOutTypes: UInt32, pOutTypes: POINTER(win32more.Windows.Win32.Media.DxMediaObjects.DMO_PARTIAL_MEDIATYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdmo.dll')
def DMOUnregister(clsidDMO: POINTER(Guid), guidCategory: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdmo.dll')
def DMOEnum(guidCategory: POINTER(Guid), dwFlags: UInt32, cInTypes: UInt32, pInTypes: POINTER(win32more.Windows.Win32.Media.DxMediaObjects.DMO_PARTIAL_MEDIATYPE), cOutTypes: UInt32, pOutTypes: POINTER(win32more.Windows.Win32.Media.DxMediaObjects.DMO_PARTIAL_MEDIATYPE), ppEnum: POINTER(win32more.Windows.Win32.Media.DxMediaObjects.IEnumDMO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdmo.dll')
def DMOGetTypes(clsidDMO: POINTER(Guid), ulInputTypesRequested: UInt32, pulInputTypesSupplied: POINTER(UInt32), pInputTypes: POINTER(win32more.Windows.Win32.Media.DxMediaObjects.DMO_PARTIAL_MEDIATYPE), ulOutputTypesRequested: UInt32, pulOutputTypesSupplied: POINTER(UInt32), pOutputTypes: POINTER(win32more.Windows.Win32.Media.DxMediaObjects.DMO_PARTIAL_MEDIATYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdmo.dll')
def DMOGetName(clsidDMO: POINTER(Guid), szName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdmo.dll')
def MoInitMediaType(pmt: POINTER(win32more.Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE), cbFormat: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdmo.dll')
def MoFreeMediaType(pmt: POINTER(win32more.Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdmo.dll')
def MoCopyMediaType(pmtDest: POINTER(win32more.Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE), pmtSrc: POINTER(win32more.Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdmo.dll')
def MoCreateMediaType(ppmt: POINTER(POINTER(win32more.Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE)), cbFormat: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdmo.dll')
def MoDeleteMediaType(pmt: POINTER(win32more.Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('msdmo.dll')
def MoDuplicateMediaType(ppmtDest: POINTER(POINTER(win32more.Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE)), pmtSrc: POINTER(win32more.Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
DMO_ENUM_FLAGS = Int32
DMO_ENUMF_INCLUDE_KEYED: win32more.Windows.Win32.Media.DxMediaObjects.DMO_ENUM_FLAGS = 1
class DMO_MEDIA_TYPE(Structure):
    majortype: Guid
    subtype: Guid
    bFixedSizeSamples: win32more.Windows.Win32.Foundation.BOOL
    bTemporalCompression: win32more.Windows.Win32.Foundation.BOOL
    lSampleSize: UInt32
    formattype: Guid
    pUnk: win32more.Windows.Win32.System.Com.IUnknown
    cbFormat: UInt32
    pbFormat: POINTER(Byte)
class DMO_OUTPUT_DATA_BUFFER(Structure):
    pBuffer: win32more.Windows.Win32.Media.DxMediaObjects.IMediaBuffer
    dwStatus: UInt32
    rtTimestamp: Int64
    rtTimelength: Int64
class DMO_PARTIAL_MEDIATYPE(Structure):
    type: Guid
    subtype: Guid
DMO_REGISTER_FLAGS = Int32
DMO_REGISTERF_IS_KEYED: win32more.Windows.Win32.Media.DxMediaObjects.DMO_REGISTER_FLAGS = 1
class IDMOQualityControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{65abea96-cf36-453f-af8a-705e98f16260}')
    @commethod(3)
    def SetNow(self, rtNow: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetStatus(self, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStatus(self, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDMOVideoOutputOptimizations(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{be8f4f4e-5b16-4d29-b350-7f6b5d9298ac}')
    @commethod(3)
    def QueryOperationModePreferences(self, ulOutputStreamIndex: UInt32, pdwRequestedCapabilities: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetOperationMode(self, ulOutputStreamIndex: UInt32, dwEnabledFeatures: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrentOperationMode(self, ulOutputStreamIndex: UInt32, pdwEnabledFeatures: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCurrentSampleRequirements(self, ulOutputStreamIndex: UInt32, pdwRequestedFeatures: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumDMO(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2c3cd98a-2bfa-4a53-9c27-5249ba64ba0f}')
    @commethod(3)
    def Next(self, cItemsToFetch: UInt32, pCLSID: POINTER(Guid), Names: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pcItemsFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cItemsToSkip: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.Media.DxMediaObjects.IEnumDMO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMediaBuffer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{59eff8b9-938c-4a26-82f2-95cb84cdc837}')
    @commethod(3)
    def SetLength(self, cbLength: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMaxLength(self, pcbMaxLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetBufferAndLength(self, ppBuffer: POINTER(POINTER(Byte)), pcbLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMediaObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d8ad0f58-5494-4102-97c5-ec798e59bcf4}')
    @commethod(3)
    def GetStreamCount(self, pcInputStreams: POINTER(UInt32), pcOutputStreams: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInputStreamInfo(self, dwInputStreamIndex: UInt32, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetOutputStreamInfo(self, dwOutputStreamIndex: UInt32, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetInputType(self, dwInputStreamIndex: UInt32, dwTypeIndex: UInt32, pmt: POINTER(win32more.Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetOutputType(self, dwOutputStreamIndex: UInt32, dwTypeIndex: UInt32, pmt: POINTER(win32more.Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetInputType(self, dwInputStreamIndex: UInt32, pmt: POINTER(win32more.Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetOutputType(self, dwOutputStreamIndex: UInt32, pmt: POINTER(win32more.Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetInputCurrentType(self, dwInputStreamIndex: UInt32, pmt: POINTER(win32more.Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetOutputCurrentType(self, dwOutputStreamIndex: UInt32, pmt: POINTER(win32more.Windows.Win32.Media.DxMediaObjects.DMO_MEDIA_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetInputSizeInfo(self, dwInputStreamIndex: UInt32, pcbSize: POINTER(UInt32), pcbMaxLookahead: POINTER(UInt32), pcbAlignment: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetOutputSizeInfo(self, dwOutputStreamIndex: UInt32, pcbSize: POINTER(UInt32), pcbAlignment: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetInputMaxLatency(self, dwInputStreamIndex: UInt32, prtMaxLatency: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetInputMaxLatency(self, dwInputStreamIndex: UInt32, rtMaxLatency: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Flush(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Discontinuity(self, dwInputStreamIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def AllocateStreamingResources(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def FreeStreamingResources(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetInputStatus(self, dwInputStreamIndex: UInt32, dwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def ProcessInput(self, dwInputStreamIndex: UInt32, pBuffer: win32more.Windows.Win32.Media.DxMediaObjects.IMediaBuffer, dwFlags: UInt32, rtTimestamp: Int64, rtTimelength: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def ProcessOutput(self, dwFlags: UInt32, cOutputBufferCount: UInt32, pOutputBuffers: POINTER(win32more.Windows.Win32.Media.DxMediaObjects.DMO_OUTPUT_DATA_BUFFER), pdwStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Lock(self, bLock: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMediaObjectInPlace(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{651b9ad0-0fc7-4aa9-9538-d89931010741}')
    @commethod(3)
    def Process(self, ulSize: UInt32, pData: POINTER(Byte), refTimeStart: Int64, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Clone(self, ppMediaObject: POINTER(win32more.Windows.Win32.Media.DxMediaObjects.IMediaObjectInPlace)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLatency(self, pLatencyTime: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
_DMO_INPLACE_PROCESS_FLAGS = Int32
DMO_INPLACE_NORMAL: win32more.Windows.Win32.Media.DxMediaObjects._DMO_INPLACE_PROCESS_FLAGS = 0
DMO_INPLACE_ZERO: win32more.Windows.Win32.Media.DxMediaObjects._DMO_INPLACE_PROCESS_FLAGS = 1
_DMO_INPUT_DATA_BUFFER_FLAGS = Int32
DMO_INPUT_DATA_BUFFERF_SYNCPOINT: win32more.Windows.Win32.Media.DxMediaObjects._DMO_INPUT_DATA_BUFFER_FLAGS = 1
DMO_INPUT_DATA_BUFFERF_TIME: win32more.Windows.Win32.Media.DxMediaObjects._DMO_INPUT_DATA_BUFFER_FLAGS = 2
DMO_INPUT_DATA_BUFFERF_TIMELENGTH: win32more.Windows.Win32.Media.DxMediaObjects._DMO_INPUT_DATA_BUFFER_FLAGS = 4
DMO_INPUT_DATA_BUFFERF_DISCONTINUITY: win32more.Windows.Win32.Media.DxMediaObjects._DMO_INPUT_DATA_BUFFER_FLAGS = 8
_DMO_INPUT_STATUS_FLAGS = Int32
DMO_INPUT_STATUSF_ACCEPT_DATA: win32more.Windows.Win32.Media.DxMediaObjects._DMO_INPUT_STATUS_FLAGS = 1
_DMO_INPUT_STREAM_INFO_FLAGS = Int32
DMO_INPUT_STREAMF_WHOLE_SAMPLES: win32more.Windows.Win32.Media.DxMediaObjects._DMO_INPUT_STREAM_INFO_FLAGS = 1
DMO_INPUT_STREAMF_SINGLE_SAMPLE_PER_BUFFER: win32more.Windows.Win32.Media.DxMediaObjects._DMO_INPUT_STREAM_INFO_FLAGS = 2
DMO_INPUT_STREAMF_FIXED_SAMPLE_SIZE: win32more.Windows.Win32.Media.DxMediaObjects._DMO_INPUT_STREAM_INFO_FLAGS = 4
DMO_INPUT_STREAMF_HOLDS_BUFFERS: win32more.Windows.Win32.Media.DxMediaObjects._DMO_INPUT_STREAM_INFO_FLAGS = 8
_DMO_OUTPUT_DATA_BUFFER_FLAGS = Int32
DMO_OUTPUT_DATA_BUFFERF_SYNCPOINT: win32more.Windows.Win32.Media.DxMediaObjects._DMO_OUTPUT_DATA_BUFFER_FLAGS = 1
DMO_OUTPUT_DATA_BUFFERF_TIME: win32more.Windows.Win32.Media.DxMediaObjects._DMO_OUTPUT_DATA_BUFFER_FLAGS = 2
DMO_OUTPUT_DATA_BUFFERF_TIMELENGTH: win32more.Windows.Win32.Media.DxMediaObjects._DMO_OUTPUT_DATA_BUFFER_FLAGS = 4
DMO_OUTPUT_DATA_BUFFERF_DISCONTINUITY: win32more.Windows.Win32.Media.DxMediaObjects._DMO_OUTPUT_DATA_BUFFER_FLAGS = 8
DMO_OUTPUT_DATA_BUFFERF_INCOMPLETE: win32more.Windows.Win32.Media.DxMediaObjects._DMO_OUTPUT_DATA_BUFFER_FLAGS = 16777216
_DMO_OUTPUT_STREAM_INFO_FLAGS = Int32
DMO_OUTPUT_STREAMF_WHOLE_SAMPLES: win32more.Windows.Win32.Media.DxMediaObjects._DMO_OUTPUT_STREAM_INFO_FLAGS = 1
DMO_OUTPUT_STREAMF_SINGLE_SAMPLE_PER_BUFFER: win32more.Windows.Win32.Media.DxMediaObjects._DMO_OUTPUT_STREAM_INFO_FLAGS = 2
DMO_OUTPUT_STREAMF_FIXED_SAMPLE_SIZE: win32more.Windows.Win32.Media.DxMediaObjects._DMO_OUTPUT_STREAM_INFO_FLAGS = 4
DMO_OUTPUT_STREAMF_DISCARDABLE: win32more.Windows.Win32.Media.DxMediaObjects._DMO_OUTPUT_STREAM_INFO_FLAGS = 8
DMO_OUTPUT_STREAMF_OPTIONAL: win32more.Windows.Win32.Media.DxMediaObjects._DMO_OUTPUT_STREAM_INFO_FLAGS = 16
_DMO_PROCESS_OUTPUT_FLAGS = Int32
DMO_PROCESS_OUTPUT_DISCARD_WHEN_NO_BUFFER: win32more.Windows.Win32.Media.DxMediaObjects._DMO_PROCESS_OUTPUT_FLAGS = 1
_DMO_QUALITY_STATUS_FLAGS = Int32
DMO_QUALITY_STATUS_ENABLED: win32more.Windows.Win32.Media.DxMediaObjects._DMO_QUALITY_STATUS_FLAGS = 1
_DMO_SET_TYPE_FLAGS = Int32
DMO_SET_TYPEF_TEST_ONLY: win32more.Windows.Win32.Media.DxMediaObjects._DMO_SET_TYPE_FLAGS = 1
DMO_SET_TYPEF_CLEAR: win32more.Windows.Win32.Media.DxMediaObjects._DMO_SET_TYPE_FLAGS = 2
_DMO_VIDEO_OUTPUT_STREAM_FLAGS = Int32
DMO_VOSF_NEEDS_PREVIOUS_SAMPLE: win32more.Windows.Win32.Media.DxMediaObjects._DMO_VIDEO_OUTPUT_STREAM_FLAGS = 1


make_ready(__name__)
