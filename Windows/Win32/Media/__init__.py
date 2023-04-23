from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation
import Windows.Win32.Media
import Windows.Win32.Media.Multimedia
import Windows.Win32.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
TIMERR_NOERROR: UInt32 = 0
TIMERR_NOCANDO: UInt32 = 97
TIMERR_STRUCT: UInt32 = 129
MAXPNAMELEN: UInt32 = 32
MAXERRORLENGTH: UInt32 = 256
MM_MICROSOFT: UInt32 = 1
MM_MIDI_MAPPER: UInt32 = 1
MM_WAVE_MAPPER: UInt32 = 2
MM_SNDBLST_MIDIOUT: UInt32 = 3
MM_SNDBLST_MIDIIN: UInt32 = 4
MM_SNDBLST_SYNTH: UInt32 = 5
MM_SNDBLST_WAVEOUT: UInt32 = 6
MM_SNDBLST_WAVEIN: UInt32 = 7
MM_ADLIB: UInt32 = 9
MM_MPU401_MIDIOUT: UInt32 = 10
MM_MPU401_MIDIIN: UInt32 = 11
MM_PC_JOYSTICK: UInt32 = 12
TIME_MS: UInt32 = 1
TIME_SAMPLES: UInt32 = 2
TIME_BYTES: UInt32 = 4
TIME_SMPTE: UInt32 = 8
TIME_MIDI: UInt32 = 16
TIME_TICKS: UInt32 = 32
MM_JOY1MOVE: UInt32 = 928
MM_JOY2MOVE: UInt32 = 929
MM_JOY1ZMOVE: UInt32 = 930
MM_JOY2ZMOVE: UInt32 = 931
MM_JOY1BUTTONDOWN: UInt32 = 949
MM_JOY2BUTTONDOWN: UInt32 = 950
MM_JOY1BUTTONUP: UInt32 = 951
MM_JOY2BUTTONUP: UInt32 = 952
MM_MCINOTIFY: UInt32 = 953
MM_WOM_OPEN: UInt32 = 955
MM_WOM_CLOSE: UInt32 = 956
MM_WOM_DONE: UInt32 = 957
MM_WIM_OPEN: UInt32 = 958
MM_WIM_CLOSE: UInt32 = 959
MM_WIM_DATA: UInt32 = 960
MM_MIM_OPEN: UInt32 = 961
MM_MIM_CLOSE: UInt32 = 962
MM_MIM_DATA: UInt32 = 963
MM_MIM_LONGDATA: UInt32 = 964
MM_MIM_ERROR: UInt32 = 965
MM_MIM_LONGERROR: UInt32 = 966
MM_MOM_OPEN: UInt32 = 967
MM_MOM_CLOSE: UInt32 = 968
MM_MOM_DONE: UInt32 = 969
MM_DRVM_OPEN: UInt32 = 976
MM_DRVM_CLOSE: UInt32 = 977
MM_DRVM_DATA: UInt32 = 978
MM_DRVM_ERROR: UInt32 = 979
MM_STREAM_OPEN: UInt32 = 980
MM_STREAM_CLOSE: UInt32 = 981
MM_STREAM_DONE: UInt32 = 982
MM_STREAM_ERROR: UInt32 = 983
MM_MOM_POSITIONCB: UInt32 = 970
MM_MCISIGNAL: UInt32 = 971
MM_MIM_MOREDATA: UInt32 = 972
MM_MIXM_LINE_CHANGE: UInt32 = 976
MM_MIXM_CONTROL_CHANGE: UInt32 = 977
MMSYSERR_BASE: UInt32 = 0
WAVERR_BASE: UInt32 = 32
MIDIERR_BASE: UInt32 = 64
TIMERR_BASE: UInt32 = 96
JOYERR_BASE: UInt32 = 160
MCIERR_BASE: UInt32 = 256
MIXERR_BASE: UInt32 = 1024
MCI_STRING_OFFSET: UInt32 = 512
MCI_VD_OFFSET: UInt32 = 1024
MCI_CD_OFFSET: UInt32 = 1088
MCI_WAVE_OFFSET: UInt32 = 1152
MCI_SEQ_OFFSET: UInt32 = 1216
MMSYSERR_NOERROR: UInt32 = 0
MMSYSERR_ERROR: UInt32 = 1
MMSYSERR_BADDEVICEID: UInt32 = 2
MMSYSERR_NOTENABLED: UInt32 = 3
MMSYSERR_ALLOCATED: UInt32 = 4
MMSYSERR_INVALHANDLE: UInt32 = 5
MMSYSERR_NODRIVER: UInt32 = 6
MMSYSERR_NOMEM: UInt32 = 7
MMSYSERR_NOTSUPPORTED: UInt32 = 8
MMSYSERR_BADERRNUM: UInt32 = 9
MMSYSERR_INVALFLAG: UInt32 = 10
MMSYSERR_INVALPARAM: UInt32 = 11
MMSYSERR_HANDLEBUSY: UInt32 = 12
MMSYSERR_INVALIDALIAS: UInt32 = 13
MMSYSERR_BADDB: UInt32 = 14
MMSYSERR_KEYNOTFOUND: UInt32 = 15
MMSYSERR_READERROR: UInt32 = 16
MMSYSERR_WRITEERROR: UInt32 = 17
MMSYSERR_DELETEERROR: UInt32 = 18
MMSYSERR_VALNOTFOUND: UInt32 = 19
MMSYSERR_NODRIVERCB: UInt32 = 20
MMSYSERR_MOREDATA: UInt32 = 21
MMSYSERR_LASTERROR: UInt32 = 21
TIME_ONESHOT: UInt32 = 0
TIME_PERIODIC: UInt32 = 1
TIME_CALLBACK_FUNCTION: UInt32 = 0
TIME_CALLBACK_EVENT_SET: UInt32 = 16
TIME_CALLBACK_EVENT_PULSE: UInt32 = 32
TIME_KILL_SYNCHRONOUS: UInt32 = 256
@winfunctype('WINMM.dll')
def timeGetSystemTime(pmmt: POINTER(Windows.Win32.Media.MMTIME_head), cbmmt: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def timeGetTime() -> UInt32: ...
@winfunctype('WINMM.dll')
def timeGetDevCaps(ptc: POINTER(Windows.Win32.Media.TIMECAPS_head), cbtc: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def timeBeginPeriod(uPeriod: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def timeEndPeriod(uPeriod: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def timeSetEvent(uDelay: UInt32, uResolution: UInt32, fptc: Windows.Win32.Media.LPTIMECALLBACK, dwUser: UIntPtr, fuEvent: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def timeKillEvent(uTimerID: UInt32) -> UInt32: ...
HTASK = IntPtr
class IReferenceClock(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('56a86897-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    @commethod(3)
    def GetTime(self, pTime: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AdviseTime(self, baseTime: Int64, streamTime: Int64, hEvent: Windows.Win32.Foundation.HANDLE, pdwAdviseCookie: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AdvisePeriodic(self, startTime: Int64, periodTime: Int64, hSemaphore: Windows.Win32.Foundation.HANDLE, pdwAdviseCookie: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Unadvise(self, dwAdviseCookie: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
class IReferenceClock2(c_void_p):
    extends: Windows.Win32.Media.IReferenceClock
    Guid = Guid('36b73885-c2c8-11cf-8b-46-00-80-5f-6c-ef-60')
class IReferenceClockTimerControl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ebec459c-2eca-4d42-a8-af-30-df-55-76-14-b8')
    @commethod(3)
    def SetDefaultTimerResolution(self, timerResolution: Int64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDefaultTimerResolution(self, pTimerResolution: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPDRVCALLBACK(hdrvr: Windows.Win32.Media.Multimedia.HDRVR, uMsg: UInt32, dwUser: UIntPtr, dw1: UIntPtr, dw2: UIntPtr) -> Void: ...
@winfunctype_pointer
def LPTIMECALLBACK(uTimerID: UInt32, uMsg: UInt32, dwUser: UIntPtr, dw1: UIntPtr, dw2: UIntPtr) -> Void: ...
class MMTIME(EasyCastStructure):
    wType: UInt32
    u: _u_e__Union
    _pack_ = 1
    class _u_e__Union(EasyCastUnion):
        ms: UInt32
        sample: UInt32
        cb: UInt32
        ticks: UInt32
        smpte: _smpte_e__Struct
        midi: _midi_e__Struct
        _pack_ = 1
        class _smpte_e__Struct(EasyCastStructure):
            hour: Byte
            min: Byte
            sec: Byte
            frame: Byte
            fps: Byte
            dummy: Byte
            pad: Byte * 2
        class _midi_e__Struct(EasyCastStructure):
            songptrpos: UInt32
            _pack_ = 1
class TIMECAPS(EasyCastStructure):
    wPeriodMin: UInt32
    wPeriodMax: UInt32
class TIMECODE(EasyCastUnion):
    Anonymous: _Anonymous_e__Struct
    qw: UInt64
    class _Anonymous_e__Struct(EasyCastStructure):
        wFrameRate: UInt16
        wFrameFract: UInt16
        dwFrames: UInt32
class TIMECODE_SAMPLE(EasyCastStructure):
    qwTick: Int64
    timecode: Windows.Win32.Media.TIMECODE
    dwUser: UInt32
    dwFlags: Windows.Win32.Media.TIMECODE_SAMPLE_FLAGS
TIMECODE_SAMPLE_FLAGS = UInt32
ED_DEVCAP_TIMECODE_READ: TIMECODE_SAMPLE_FLAGS = 4121
ED_DEVCAP_ATN_READ: TIMECODE_SAMPLE_FLAGS = 5047
ED_DEVCAP_RTC_READ: TIMECODE_SAMPLE_FLAGS = 5050
make_head(_module, 'IReferenceClock')
make_head(_module, 'IReferenceClock2')
make_head(_module, 'IReferenceClockTimerControl')
make_head(_module, 'LPDRVCALLBACK')
make_head(_module, 'LPTIMECALLBACK')
make_head(_module, 'MMTIME')
make_head(_module, 'TIMECAPS')
make_head(_module, 'TIMECODE')
make_head(_module, 'TIMECODE_SAMPLE')
