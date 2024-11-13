from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Media
import win32more.Windows.Win32.Media.Audio
import win32more.Windows.Win32.Media.Multimedia
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.StructuredStorage
import win32more.Windows.Win32.UI.Shell.PropertiesSystem
import win32more.Windows.Win32.UI.WindowsAndMessaging
class ACMDRIVERDETAILSA(Structure):
    cbStruct: UInt32
    fccType: UInt32
    fccComp: UInt32
    wMid: UInt16
    wPid: UInt16
    vdwACM: UInt32
    vdwDriver: UInt32
    fdwSupport: UInt32
    cFormatTags: UInt32
    cFilterTags: UInt32
    hicon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON
    szShortName: win32more.Windows.Win32.Foundation.CHAR * 32
    szLongName: win32more.Windows.Win32.Foundation.CHAR * 128
    szCopyright: win32more.Windows.Win32.Foundation.CHAR * 80
    szLicensing: win32more.Windows.Win32.Foundation.CHAR * 128
    szFeatures: win32more.Windows.Win32.Foundation.CHAR * 512
    _pack_ = 1
class ACMDRIVERDETAILSW(Structure):
    cbStruct: UInt32
    fccType: UInt32
    fccComp: UInt32
    wMid: UInt16
    wPid: UInt16
    vdwACM: UInt32
    vdwDriver: UInt32
    fdwSupport: UInt32
    cFormatTags: UInt32
    cFilterTags: UInt32
    hicon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON
    szShortName: Char * 32
    szLongName: Char * 128
    szCopyright: Char * 80
    szLicensing: Char * 128
    szFeatures: Char * 512
    _pack_ = 1
ACMDRIVERDETAILS = UnicodeAlias('ACMDRIVERDETAILSW')
@winfunctype_pointer
def ACMDRIVERENUMCB(hadid: win32more.Windows.Win32.Media.Audio.HACMDRIVERID, dwInstance: UIntPtr, fdwSupport: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
class ACMDRVFORMATSUGGEST(Structure):
    cbStruct: UInt32
    fdwSuggest: UInt32
    pwfxSrc: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)
    cbwfxSrc: UInt32
    pwfxDst: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)
    cbwfxDst: UInt32
    _pack_ = 1
class ACMDRVOPENDESCA(Structure):
    cbStruct: UInt32
    fccType: UInt32
    fccComp: UInt32
    dwVersion: UInt32
    dwFlags: UInt32
    dwError: UInt32
    pszSectionName: win32more.Windows.Win32.Foundation.PSTR
    pszAliasName: win32more.Windows.Win32.Foundation.PSTR
    dnDevNode: UInt32
    _pack_ = 1
class ACMDRVOPENDESCW(Structure):
    cbStruct: UInt32
    fccType: UInt32
    fccComp: UInt32
    dwVersion: UInt32
    dwFlags: UInt32
    dwError: UInt32
    pszSectionName: win32more.Windows.Win32.Foundation.PWSTR
    pszAliasName: win32more.Windows.Win32.Foundation.PWSTR
    dnDevNode: UInt32
    _pack_ = 1
ACMDRVOPENDESC = UnicodeAlias('ACMDRVOPENDESCW')
class ACMDRVSTREAMHEADER(Structure):
    cbStruct: UInt32
    fdwStatus: UInt32
    dwUser: UIntPtr
    pbSrc: POINTER(Byte)
    cbSrcLength: UInt32
    cbSrcLengthUsed: UInt32
    dwSrcUser: UIntPtr
    pbDst: POINTER(Byte)
    cbDstLength: UInt32
    cbDstLengthUsed: UInt32
    dwDstUser: UIntPtr
    fdwConvert: UInt32
    padshNext: POINTER(win32more.Windows.Win32.Media.Audio.ACMDRVSTREAMHEADER)
    fdwDriver: UInt32
    dwDriver: UIntPtr
    fdwPrepared: UInt32
    dwPrepared: UIntPtr
    pbPreparedSrc: POINTER(Byte)
    cbPreparedSrcLength: UInt32
    pbPreparedDst: POINTER(Byte)
    cbPreparedDstLength: UInt32
    _pack_ = 1
class ACMDRVSTREAMINSTANCE(Structure):
    cbStruct: UInt32
    pwfxSrc: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)
    pwfxDst: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)
    pwfltr: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFILTER)
    dwCallback: UIntPtr
    dwInstance: UIntPtr
    fdwOpen: UInt32
    fdwDriver: UInt32
    dwDriver: UIntPtr
    has: win32more.Windows.Win32.Media.Audio.HACMSTREAM
    _pack_ = 1
class ACMDRVSTREAMSIZE(Structure):
    cbStruct: UInt32
    fdwSize: UInt32
    cbSrcLength: UInt32
    cbDstLength: UInt32
    _pack_ = 1
class ACMFILTERCHOOSEA(Structure):
    cbStruct: UInt32
    fdwStyle: UInt32
    hwndOwner: win32more.Windows.Win32.Foundation.HWND
    pwfltr: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFILTER)
    cbwfltr: UInt32
    pszTitle: win32more.Windows.Win32.Foundation.PSTR
    szFilterTag: win32more.Windows.Win32.Foundation.CHAR * 48
    szFilter: win32more.Windows.Win32.Foundation.CHAR * 128
    pszName: win32more.Windows.Win32.Foundation.PSTR
    cchName: UInt32
    fdwEnum: UInt32
    pwfltrEnum: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFILTER)
    hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
    pszTemplateName: win32more.Windows.Win32.Foundation.PSTR
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    pfnHook: win32more.Windows.Win32.Media.Audio.ACMFILTERCHOOSEHOOKPROCA
    _pack_ = 1
@winfunctype_pointer
def ACMFILTERCHOOSEHOOKPROCA(hwnd: win32more.Windows.Win32.Foundation.HWND, uMsg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> UInt32: ...
@winfunctype_pointer
def ACMFILTERCHOOSEHOOKPROCW(hwnd: win32more.Windows.Win32.Foundation.HWND, uMsg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> UInt32: ...
ACMFILTERCHOOSEHOOKPROC = UnicodeAlias('ACMFILTERCHOOSEHOOKPROCW')
class ACMFILTERCHOOSEW(Structure):
    cbStruct: UInt32
    fdwStyle: UInt32
    hwndOwner: win32more.Windows.Win32.Foundation.HWND
    pwfltr: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFILTER)
    cbwfltr: UInt32
    pszTitle: win32more.Windows.Win32.Foundation.PWSTR
    szFilterTag: Char * 48
    szFilter: Char * 128
    pszName: win32more.Windows.Win32.Foundation.PWSTR
    cchName: UInt32
    fdwEnum: UInt32
    pwfltrEnum: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFILTER)
    hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
    pszTemplateName: win32more.Windows.Win32.Foundation.PWSTR
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    pfnHook: win32more.Windows.Win32.Media.Audio.ACMFILTERCHOOSEHOOKPROCW
    _pack_ = 1
ACMFILTERCHOOSE = UnicodeAlias('ACMFILTERCHOOSEW')
class ACMFILTERDETAILSA(Structure):
    cbStruct: UInt32
    dwFilterIndex: UInt32
    dwFilterTag: UInt32
    fdwSupport: UInt32
    pwfltr: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFILTER)
    cbwfltr: UInt32
    szFilter: win32more.Windows.Win32.Foundation.CHAR * 128
    _pack_ = 1
class ACMFILTERDETAILSW(Structure):
    cbStruct: UInt32
    dwFilterIndex: UInt32
    dwFilterTag: UInt32
    fdwSupport: UInt32
    pwfltr: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFILTER)
    cbwfltr: UInt32
    szFilter: Char * 128
    _pack_ = 1
ACMFILTERDETAILS = UnicodeAlias('ACMFILTERDETAILSW')
@winfunctype_pointer
def ACMFILTERENUMCBA(hadid: win32more.Windows.Win32.Media.Audio.HACMDRIVERID, pafd: POINTER(win32more.Windows.Win32.Media.Audio.ACMFILTERDETAILSA), dwInstance: UIntPtr, fdwSupport: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def ACMFILTERENUMCBW(hadid: win32more.Windows.Win32.Media.Audio.HACMDRIVERID, pafd: POINTER(win32more.Windows.Win32.Media.Audio.ACMFILTERDETAILSW), dwInstance: UIntPtr, fdwSupport: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
ACMFILTERENUMCB = UnicodeAlias('ACMFILTERENUMCBW')
class ACMFILTERTAGDETAILSA(Structure):
    cbStruct: UInt32
    dwFilterTagIndex: UInt32
    dwFilterTag: UInt32
    cbFilterSize: UInt32
    fdwSupport: UInt32
    cStandardFilters: UInt32
    szFilterTag: win32more.Windows.Win32.Foundation.CHAR * 48
    _pack_ = 1
class ACMFILTERTAGDETAILSW(Structure):
    cbStruct: UInt32
    dwFilterTagIndex: UInt32
    dwFilterTag: UInt32
    cbFilterSize: UInt32
    fdwSupport: UInt32
    cStandardFilters: UInt32
    szFilterTag: Char * 48
    _pack_ = 1
ACMFILTERTAGDETAILS = UnicodeAlias('ACMFILTERTAGDETAILSW')
@winfunctype_pointer
def ACMFILTERTAGENUMCBA(hadid: win32more.Windows.Win32.Media.Audio.HACMDRIVERID, paftd: POINTER(win32more.Windows.Win32.Media.Audio.ACMFILTERTAGDETAILSA), dwInstance: UIntPtr, fdwSupport: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def ACMFILTERTAGENUMCBW(hadid: win32more.Windows.Win32.Media.Audio.HACMDRIVERID, paftd: POINTER(win32more.Windows.Win32.Media.Audio.ACMFILTERTAGDETAILSW), dwInstance: UIntPtr, fdwSupport: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
ACMFILTERTAGENUMCB = UnicodeAlias('ACMFILTERTAGENUMCBW')
class ACMFORMATCHOOSEA(Structure):
    cbStruct: UInt32
    fdwStyle: UInt32
    hwndOwner: win32more.Windows.Win32.Foundation.HWND
    pwfx: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)
    cbwfx: UInt32
    pszTitle: win32more.Windows.Win32.Foundation.PSTR
    szFormatTag: win32more.Windows.Win32.Foundation.CHAR * 48
    szFormat: win32more.Windows.Win32.Foundation.CHAR * 128
    pszName: win32more.Windows.Win32.Foundation.PSTR
    cchName: UInt32
    fdwEnum: UInt32
    pwfxEnum: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)
    hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
    pszTemplateName: win32more.Windows.Win32.Foundation.PSTR
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    pfnHook: win32more.Windows.Win32.Media.Audio.ACMFORMATCHOOSEHOOKPROCA
    _pack_ = 1
@winfunctype_pointer
def ACMFORMATCHOOSEHOOKPROCA(hwnd: win32more.Windows.Win32.Foundation.HWND, uMsg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> UInt32: ...
@winfunctype_pointer
def ACMFORMATCHOOSEHOOKPROCW(hwnd: win32more.Windows.Win32.Foundation.HWND, uMsg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> UInt32: ...
ACMFORMATCHOOSEHOOKPROC = UnicodeAlias('ACMFORMATCHOOSEHOOKPROCW')
class ACMFORMATCHOOSEW(Structure):
    cbStruct: UInt32
    fdwStyle: UInt32
    hwndOwner: win32more.Windows.Win32.Foundation.HWND
    pwfx: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)
    cbwfx: UInt32
    pszTitle: win32more.Windows.Win32.Foundation.PWSTR
    szFormatTag: Char * 48
    szFormat: Char * 128
    pszName: win32more.Windows.Win32.Foundation.PWSTR
    cchName: UInt32
    fdwEnum: UInt32
    pwfxEnum: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)
    hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
    pszTemplateName: win32more.Windows.Win32.Foundation.PWSTR
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    pfnHook: win32more.Windows.Win32.Media.Audio.ACMFORMATCHOOSEHOOKPROCW
    _pack_ = 1
ACMFORMATCHOOSE = UnicodeAlias('ACMFORMATCHOOSEW')
class ACMFORMATDETAILSA(Structure):
    cbStruct: UInt32
    dwFormatIndex: UInt32
    dwFormatTag: UInt32
    fdwSupport: UInt32
    pwfx: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)
    cbwfx: UInt32
    szFormat: win32more.Windows.Win32.Foundation.CHAR * 128
    _pack_ = 1
@winfunctype_pointer
def ACMFORMATENUMCBA(hadid: win32more.Windows.Win32.Media.Audio.HACMDRIVERID, pafd: POINTER(win32more.Windows.Win32.Media.Audio.ACMFORMATDETAILSA), dwInstance: UIntPtr, fdwSupport: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def ACMFORMATENUMCBW(hadid: win32more.Windows.Win32.Media.Audio.HACMDRIVERID, pafd: POINTER(win32more.Windows.Win32.Media.Audio.tACMFORMATDETAILSW), dwInstance: UIntPtr, fdwSupport: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
ACMFORMATENUMCB = UnicodeAlias('ACMFORMATENUMCBW')
class ACMFORMATTAGDETAILSA(Structure):
    cbStruct: UInt32
    dwFormatTagIndex: UInt32
    dwFormatTag: UInt32
    cbFormatSize: UInt32
    fdwSupport: UInt32
    cStandardFormats: UInt32
    szFormatTag: win32more.Windows.Win32.Foundation.CHAR * 48
    _pack_ = 1
class ACMFORMATTAGDETAILSW(Structure):
    cbStruct: UInt32
    dwFormatTagIndex: UInt32
    dwFormatTag: UInt32
    cbFormatSize: UInt32
    fdwSupport: UInt32
    cStandardFormats: UInt32
    szFormatTag: Char * 48
    _pack_ = 1
ACMFORMATTAGDETAILS = UnicodeAlias('ACMFORMATTAGDETAILSW')
@winfunctype_pointer
def ACMFORMATTAGENUMCBA(hadid: win32more.Windows.Win32.Media.Audio.HACMDRIVERID, paftd: POINTER(win32more.Windows.Win32.Media.Audio.ACMFORMATTAGDETAILSA), dwInstance: UIntPtr, fdwSupport: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def ACMFORMATTAGENUMCBW(hadid: win32more.Windows.Win32.Media.Audio.HACMDRIVERID, paftd: POINTER(win32more.Windows.Win32.Media.Audio.ACMFORMATTAGDETAILSW), dwInstance: UIntPtr, fdwSupport: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
ACMFORMATTAGENUMCB = UnicodeAlias('ACMFORMATTAGENUMCBW')
if ARCH in 'X64,ARM64':
    class ACMSTREAMHEADER(Structure):
        cbStruct: UInt32
        fdwStatus: UInt32
        dwUser: UIntPtr
        pbSrc: POINTER(Byte)
        cbSrcLength: UInt32
        cbSrcLengthUsed: UInt32
        dwSrcUser: UIntPtr
        pbDst: POINTER(Byte)
        cbDstLength: UInt32
        cbDstLengthUsed: UInt32
        dwDstUser: UIntPtr
        dwReservedDriver: UInt32 * 15
        _pack_ = 1
elif ARCH in 'X86':
    class ACMSTREAMHEADER(Structure):
        cbStruct: UInt32
        fdwStatus: UInt32
        dwUser: UIntPtr
        pbSrc: POINTER(Byte)
        cbSrcLength: UInt32
        cbSrcLengthUsed: UInt32
        dwSrcUser: UIntPtr
        pbDst: POINTER(Byte)
        cbDstLength: UInt32
        cbDstLengthUsed: UInt32
        dwDstUser: UIntPtr
        dwReservedDriver: UInt32 * 10
        _pack_ = 1
AMBISONICS_CHANNEL_ORDERING = Int32
AMBISONICS_CHANNEL_ORDERING_ACN: win32more.Windows.Win32.Media.Audio.AMBISONICS_CHANNEL_ORDERING = 0
AMBISONICS_NORMALIZATION = Int32
AMBISONICS_NORMALIZATION_SN3D: win32more.Windows.Win32.Media.Audio.AMBISONICS_NORMALIZATION = 0
AMBISONICS_NORMALIZATION_N3D: win32more.Windows.Win32.Media.Audio.AMBISONICS_NORMALIZATION = 1
class AMBISONICS_PARAMS(Structure):
    u32Size: UInt32
    u32Version: UInt32
    u32Type: win32more.Windows.Win32.Media.Audio.AMBISONICS_TYPE
    u32ChannelOrdering: win32more.Windows.Win32.Media.Audio.AMBISONICS_CHANNEL_ORDERING
    u32Normalization: win32more.Windows.Win32.Media.Audio.AMBISONICS_NORMALIZATION
    u32Order: UInt32
    u32NumChannels: UInt32
    pu32ChannelMap: POINTER(UInt32)
AMBISONICS_TYPE = Int32
AMBISONICS_TYPE_FULL3D: win32more.Windows.Win32.Media.Audio.AMBISONICS_TYPE = 0
AUDCLNT_SHAREMODE = Int32
AUDCLNT_SHAREMODE_SHARED: win32more.Windows.Win32.Media.Audio.AUDCLNT_SHAREMODE = 0
AUDCLNT_SHAREMODE_EXCLUSIVE: win32more.Windows.Win32.Media.Audio.AUDCLNT_SHAREMODE = 1
AUDCLNT_STREAMOPTIONS = Int32
AUDCLNT_STREAMOPTIONS_NONE: win32more.Windows.Win32.Media.Audio.AUDCLNT_STREAMOPTIONS = 0
AUDCLNT_STREAMOPTIONS_RAW: win32more.Windows.Win32.Media.Audio.AUDCLNT_STREAMOPTIONS = 1
AUDCLNT_STREAMOPTIONS_MATCH_FORMAT: win32more.Windows.Win32.Media.Audio.AUDCLNT_STREAMOPTIONS = 2
AUDCLNT_STREAMOPTIONS_AMBISONICS: win32more.Windows.Win32.Media.Audio.AUDCLNT_STREAMOPTIONS = 4
class AUDIOCLIENT_ACTIVATION_PARAMS(Structure):
    ActivationType: win32more.Windows.Win32.Media.Audio.AUDIOCLIENT_ACTIVATION_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        ProcessLoopbackParams: win32more.Windows.Win32.Media.Audio.AUDIOCLIENT_PROCESS_LOOPBACK_PARAMS
AUDIOCLIENT_ACTIVATION_TYPE = Int32
AUDIOCLIENT_ACTIVATION_TYPE_DEFAULT: win32more.Windows.Win32.Media.Audio.AUDIOCLIENT_ACTIVATION_TYPE = 0
AUDIOCLIENT_ACTIVATION_TYPE_PROCESS_LOOPBACK: win32more.Windows.Win32.Media.Audio.AUDIOCLIENT_ACTIVATION_TYPE = 1
class AUDIOCLIENT_PROCESS_LOOPBACK_PARAMS(Structure):
    TargetProcessId: UInt32
    ProcessLoopbackMode: win32more.Windows.Win32.Media.Audio.PROCESS_LOOPBACK_MODE
AUDIO_DUCKING_OPTIONS = Int32
AUDIO_DUCKING_OPTIONS_DEFAULT: win32more.Windows.Win32.Media.Audio.AUDIO_DUCKING_OPTIONS = 0
AUDIO_DUCKING_OPTIONS_DO_NOT_DUCK_OTHER_STREAMS: win32more.Windows.Win32.Media.Audio.AUDIO_DUCKING_OPTIONS = 1
class AUDIO_EFFECT(Structure):
    id: Guid
    canSetState: win32more.Windows.Win32.Foundation.BOOL
    state: win32more.Windows.Win32.Media.Audio.AUDIO_EFFECT_STATE
AUDIO_EFFECT_STATE = Int32
AUDIO_EFFECT_STATE_OFF: win32more.Windows.Win32.Media.Audio.AUDIO_EFFECT_STATE = 0
AUDIO_EFFECT_STATE_ON: win32more.Windows.Win32.Media.Audio.AUDIO_EFFECT_STATE = 1
AUDIO_STREAM_CATEGORY = Int32
AudioCategory_Other: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY = 0
AudioCategory_ForegroundOnlyMedia: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY = 1
AudioCategory_Communications: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY = 3
AudioCategory_Alerts: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY = 4
AudioCategory_SoundEffects: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY = 5
AudioCategory_GameEffects: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY = 6
AudioCategory_GameMedia: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY = 7
AudioCategory_GameChat: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY = 8
AudioCategory_Speech: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY = 9
AudioCategory_Movie: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY = 10
AudioCategory_Media: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY = 11
AudioCategory_FarFieldSpeech: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY = 12
AudioCategory_UniformSpeech: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY = 13
AudioCategory_VoiceTyping: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY = 14
AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE = Int32
AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE_DEFAULT: win32more.Windows.Win32.Media.Audio.AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE = 0
AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE_USER: win32more.Windows.Win32.Media.Audio.AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE = 1
AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE_VOLATILE: win32more.Windows.Win32.Media.Audio.AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE = 2
AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE_ENUM_COUNT: win32more.Windows.Win32.Media.Audio.AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE = 3
class AUDIO_VOLUME_NOTIFICATION_DATA(Structure):
    guidEventContext: Guid
    bMuted: win32more.Windows.Win32.Foundation.BOOL
    fMasterVolume: Single
    nChannels: UInt32
    afChannelVolumes: Single * 1
class AUXCAPS2A(Structure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: win32more.Windows.Win32.Foundation.CHAR * 32
    wTechnology: UInt16
    wReserved1: UInt16
    dwSupport: UInt32
    ManufacturerGuid: Guid
    ProductGuid: Guid
    NameGuid: Guid
    _pack_ = 1
class AUXCAPS2W(Structure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Char * 32
    wTechnology: UInt16
    wReserved1: UInt16
    dwSupport: UInt32
    ManufacturerGuid: Guid
    ProductGuid: Guid
    NameGuid: Guid
    _pack_ = 1
AUXCAPS2 = UnicodeAlias('AUXCAPS2W')
class AUXCAPSA(Structure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: win32more.Windows.Win32.Foundation.CHAR * 32
    wTechnology: UInt16
    wReserved1: UInt16
    dwSupport: UInt32
    _pack_ = 1
class AUXCAPSW(Structure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Char * 32
    wTechnology: UInt16
    wReserved1: UInt16
    dwSupport: UInt32
    _pack_ = 1
AUXCAPS = UnicodeAlias('AUXCAPSW')
MIXERCONTROL_CONTROLTYPE_CUSTOM: UInt32 = 0
MIXERCONTROL_CONTROLTYPE_BOOLEANMETER: UInt32 = 268500992
MIXERCONTROL_CONTROLTYPE_SIGNEDMETER: UInt32 = 268566528
MIXERCONTROL_CONTROLTYPE_PEAKMETER: UInt32 = 268566529
MIXERCONTROL_CONTROLTYPE_UNSIGNEDMETER: UInt32 = 268632064
MIXERCONTROL_CONTROLTYPE_BOOLEAN: UInt32 = 536936448
MIXERCONTROL_CONTROLTYPE_ONOFF: UInt32 = 536936449
MIXERCONTROL_CONTROLTYPE_MUTE: UInt32 = 536936450
MIXERCONTROL_CONTROLTYPE_MONO: UInt32 = 536936451
MIXERCONTROL_CONTROLTYPE_LOUDNESS: UInt32 = 536936452
MIXERCONTROL_CONTROLTYPE_STEREOENH: UInt32 = 536936453
MIXERCONTROL_CONTROLTYPE_BASS_BOOST: UInt32 = 536945271
MIXERCONTROL_CONTROLTYPE_BUTTON: UInt32 = 553713664
MIXERCONTROL_CONTROLTYPE_DECIBELS: UInt32 = 805568512
MIXERCONTROL_CONTROLTYPE_SIGNED: UInt32 = 805437440
MIXERCONTROL_CONTROLTYPE_UNSIGNED: UInt32 = 805502976
MIXERCONTROL_CONTROLTYPE_PERCENT: UInt32 = 805634048
MIXERCONTROL_CONTROLTYPE_SLIDER: UInt32 = 1073872896
MIXERCONTROL_CONTROLTYPE_PAN: UInt32 = 1073872897
MIXERCONTROL_CONTROLTYPE_QSOUNDPAN: UInt32 = 1073872898
MIXERCONTROL_CONTROLTYPE_FADER: UInt32 = 1342373888
MIXERCONTROL_CONTROLTYPE_VOLUME: UInt32 = 1342373889
MIXERCONTROL_CONTROLTYPE_BASS: UInt32 = 1342373890
MIXERCONTROL_CONTROLTYPE_TREBLE: UInt32 = 1342373891
MIXERCONTROL_CONTROLTYPE_EQUALIZER: UInt32 = 1342373892
MIXERCONTROL_CONTROLTYPE_SINGLESELECT: UInt32 = 1879113728
MIXERCONTROL_CONTROLTYPE_MUX: UInt32 = 1879113729
MIXERCONTROL_CONTROLTYPE_MULTIPLESELECT: UInt32 = 1895890944
MIXERCONTROL_CONTROLTYPE_MIXER: UInt32 = 1895890945
MIXERCONTROL_CONTROLTYPE_MICROTIME: UInt32 = 1610809344
MIXERCONTROL_CONTROLTYPE_MILLITIME: UInt32 = 1627586560
WAVE_MAPPER: UInt32 = 4294967295
ENDPOINT_FORMAT_RESET_MIX_ONLY: UInt32 = 1
ENDPOINT_HARDWARE_SUPPORT_VOLUME: UInt32 = 1
ENDPOINT_HARDWARE_SUPPORT_MUTE: UInt32 = 2
ENDPOINT_HARDWARE_SUPPORT_METER: UInt32 = 4
AUDIOCLOCK_CHARACTERISTIC_FIXED_FREQ: UInt32 = 1
AMBISONICS_PARAM_VERSION_1: UInt32 = 1
AUDCLNT_E_NOT_INITIALIZED: win32more.Windows.Win32.Foundation.HRESULT = -2004287487
AUDCLNT_E_ALREADY_INITIALIZED: win32more.Windows.Win32.Foundation.HRESULT = -2004287486
AUDCLNT_E_WRONG_ENDPOINT_TYPE: win32more.Windows.Win32.Foundation.HRESULT = -2004287485
AUDCLNT_E_DEVICE_INVALIDATED: win32more.Windows.Win32.Foundation.HRESULT = -2004287484
AUDCLNT_E_NOT_STOPPED: win32more.Windows.Win32.Foundation.HRESULT = -2004287483
AUDCLNT_E_BUFFER_TOO_LARGE: win32more.Windows.Win32.Foundation.HRESULT = -2004287482
AUDCLNT_E_OUT_OF_ORDER: win32more.Windows.Win32.Foundation.HRESULT = -2004287481
AUDCLNT_E_UNSUPPORTED_FORMAT: win32more.Windows.Win32.Foundation.HRESULT = -2004287480
AUDCLNT_E_INVALID_SIZE: win32more.Windows.Win32.Foundation.HRESULT = -2004287479
AUDCLNT_E_DEVICE_IN_USE: win32more.Windows.Win32.Foundation.HRESULT = -2004287478
AUDCLNT_E_BUFFER_OPERATION_PENDING: win32more.Windows.Win32.Foundation.HRESULT = -2004287477
AUDCLNT_E_THREAD_NOT_REGISTERED: win32more.Windows.Win32.Foundation.HRESULT = -2004287476
AUDCLNT_E_EXCLUSIVE_MODE_NOT_ALLOWED: win32more.Windows.Win32.Foundation.HRESULT = -2004287474
AUDCLNT_E_ENDPOINT_CREATE_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2004287473
AUDCLNT_E_SERVICE_NOT_RUNNING: win32more.Windows.Win32.Foundation.HRESULT = -2004287472
AUDCLNT_E_EVENTHANDLE_NOT_EXPECTED: win32more.Windows.Win32.Foundation.HRESULT = -2004287471
AUDCLNT_E_EXCLUSIVE_MODE_ONLY: win32more.Windows.Win32.Foundation.HRESULT = -2004287470
AUDCLNT_E_BUFDURATION_PERIOD_NOT_EQUAL: win32more.Windows.Win32.Foundation.HRESULT = -2004287469
AUDCLNT_E_EVENTHANDLE_NOT_SET: win32more.Windows.Win32.Foundation.HRESULT = -2004287468
AUDCLNT_E_INCORRECT_BUFFER_SIZE: win32more.Windows.Win32.Foundation.HRESULT = -2004287467
AUDCLNT_E_BUFFER_SIZE_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2004287466
AUDCLNT_E_CPUUSAGE_EXCEEDED: win32more.Windows.Win32.Foundation.HRESULT = -2004287465
AUDCLNT_E_BUFFER_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2004287464
AUDCLNT_E_BUFFER_SIZE_NOT_ALIGNED: win32more.Windows.Win32.Foundation.HRESULT = -2004287463
AUDCLNT_E_INVALID_DEVICE_PERIOD: win32more.Windows.Win32.Foundation.HRESULT = -2004287456
AUDCLNT_E_INVALID_STREAM_FLAG: win32more.Windows.Win32.Foundation.HRESULT = -2004287455
AUDCLNT_E_ENDPOINT_OFFLOAD_NOT_CAPABLE: win32more.Windows.Win32.Foundation.HRESULT = -2004287454
AUDCLNT_E_OUT_OF_OFFLOAD_RESOURCES: win32more.Windows.Win32.Foundation.HRESULT = -2004287453
AUDCLNT_E_OFFLOAD_MODE_ONLY: win32more.Windows.Win32.Foundation.HRESULT = -2004287452
AUDCLNT_E_NONOFFLOAD_MODE_ONLY: win32more.Windows.Win32.Foundation.HRESULT = -2004287451
AUDCLNT_E_RESOURCES_INVALIDATED: win32more.Windows.Win32.Foundation.HRESULT = -2004287450
AUDCLNT_E_RAW_MODE_UNSUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2004287449
AUDCLNT_E_ENGINE_PERIODICITY_LOCKED: win32more.Windows.Win32.Foundation.HRESULT = -2004287448
AUDCLNT_E_ENGINE_FORMAT_LOCKED: win32more.Windows.Win32.Foundation.HRESULT = -2004287447
AUDCLNT_E_HEADTRACKING_ENABLED: win32more.Windows.Win32.Foundation.HRESULT = -2004287440
AUDCLNT_E_HEADTRACKING_UNSUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2004287424
AUDCLNT_E_EFFECT_NOT_AVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = -2004287423
AUDCLNT_E_EFFECT_STATE_READ_ONLY: win32more.Windows.Win32.Foundation.HRESULT = -2004287422
AUDCLNT_S_BUFFER_EMPTY: win32more.Windows.Win32.Foundation.HRESULT = 143196161
AUDCLNT_S_THREAD_ALREADY_REGISTERED: win32more.Windows.Win32.Foundation.HRESULT = 143196162
AUDCLNT_S_POSITION_STALLED: win32more.Windows.Win32.Foundation.HRESULT = 143196163
AUDCLNT_STREAMFLAGS_CROSSPROCESS: UInt32 = 65536
AUDCLNT_STREAMFLAGS_LOOPBACK: UInt32 = 131072
AUDCLNT_STREAMFLAGS_EVENTCALLBACK: UInt32 = 262144
AUDCLNT_STREAMFLAGS_NOPERSIST: UInt32 = 524288
AUDCLNT_STREAMFLAGS_RATEADJUST: UInt32 = 1048576
AUDCLNT_STREAMFLAGS_SRC_DEFAULT_QUALITY: UInt32 = 134217728
AUDCLNT_STREAMFLAGS_AUTOCONVERTPCM: UInt32 = 2147483648
AUDCLNT_SESSIONFLAGS_EXPIREWHENUNOWNED: UInt32 = 268435456
AUDCLNT_SESSIONFLAGS_DISPLAY_HIDE: UInt32 = 536870912
AUDCLNT_SESSIONFLAGS_DISPLAY_HIDEWHENEXPIRED: UInt32 = 1073741824
SPTLAUDCLNT_E_DESTROYED: win32more.Windows.Win32.Foundation.HRESULT = -2004287232
SPTLAUDCLNT_E_OUT_OF_ORDER: win32more.Windows.Win32.Foundation.HRESULT = -2004287231
SPTLAUDCLNT_E_RESOURCES_INVALIDATED: win32more.Windows.Win32.Foundation.HRESULT = -2004287230
SPTLAUDCLNT_E_NO_MORE_OBJECTS: win32more.Windows.Win32.Foundation.HRESULT = -2004287229
SPTLAUDCLNT_E_PROPERTY_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2004287228
SPTLAUDCLNT_E_ERRORS_IN_OBJECT_CALLS: win32more.Windows.Win32.Foundation.HRESULT = -2004287227
SPTLAUDCLNT_E_METADATA_FORMAT_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2004287226
SPTLAUDCLNT_E_STREAM_NOT_AVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = -2004287225
SPTLAUDCLNT_E_INVALID_LICENSE: win32more.Windows.Win32.Foundation.HRESULT = -2004287224
SPTLAUDCLNT_E_STREAM_NOT_STOPPED: win32more.Windows.Win32.Foundation.HRESULT = -2004287222
SPTLAUDCLNT_E_STATIC_OBJECT_NOT_AVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = -2004287221
SPTLAUDCLNT_E_OBJECT_ALREADY_ACTIVE: win32more.Windows.Win32.Foundation.HRESULT = -2004287220
SPTLAUDCLNT_E_INTERNAL: win32more.Windows.Win32.Foundation.HRESULT = -2004287219
DEVICE_STATEMASK_ALL: UInt32 = 15
PKEY_AudioEndpoint_FormFactor: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1da5d803-d492-4edd-8c23-e0c0ffee7f0e}'), pid=0)
PKEY_AudioEndpoint_ControlPanelPageProvider: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1da5d803-d492-4edd-8c23-e0c0ffee7f0e}'), pid=1)
PKEY_AudioEndpoint_Association: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1da5d803-d492-4edd-8c23-e0c0ffee7f0e}'), pid=2)
PKEY_AudioEndpoint_PhysicalSpeakers: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1da5d803-d492-4edd-8c23-e0c0ffee7f0e}'), pid=3)
PKEY_AudioEndpoint_GUID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1da5d803-d492-4edd-8c23-e0c0ffee7f0e}'), pid=4)
PKEY_AudioEndpoint_Disable_SysFx: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1da5d803-d492-4edd-8c23-e0c0ffee7f0e}'), pid=5)
ENDPOINT_SYSFX_ENABLED: UInt32 = 0
ENDPOINT_SYSFX_DISABLED: UInt32 = 1
PKEY_AudioEndpoint_FullRangeSpeakers: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1da5d803-d492-4edd-8c23-e0c0ffee7f0e}'), pid=6)
PKEY_AudioEndpoint_Supports_EventDriven_Mode: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1da5d803-d492-4edd-8c23-e0c0ffee7f0e}'), pid=7)
PKEY_AudioEndpoint_JackSubType: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1da5d803-d492-4edd-8c23-e0c0ffee7f0e}'), pid=8)
PKEY_AudioEndpoint_Default_VolumeInDb: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1da5d803-d492-4edd-8c23-e0c0ffee7f0e}'), pid=9)
PKEY_AudioEngine_DeviceFormat: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f19f064d-082c-4e27-bc73-6882a1bb8e4c}'), pid=0)
PKEY_AudioEngine_OEMFormat: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{e4870e26-3cc5-4cd2-ba46-ca0a9a70ed04}'), pid=3)
PKEY_AudioEndpointLogo_IconEffects: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f1ab780d-2010-4ed3-a3a6-8b87f0f0c476}'), pid=0)
PKEY_AudioEndpointLogo_IconPath: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{f1ab780d-2010-4ed3-a3a6-8b87f0f0c476}'), pid=1)
PKEY_AudioEndpointSettings_MenuText: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{14242002-0320-4de4-9555-a7d82b73c286}'), pid=0)
PKEY_AudioEndpointSettings_LaunchContract: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{14242002-0320-4de4-9555-a7d82b73c286}'), pid=1)
DEVINTERFACE_AUDIO_RENDER: Guid = Guid('{e6327cad-dcec-4949-ae8a-991e976a79d2}')
DEVINTERFACE_AUDIO_CAPTURE: Guid = Guid('{2eef81be-33fa-4800-9670-1cd474972c3f}')
DEVINTERFACE_MIDI_OUTPUT: Guid = Guid('{6dc23320-ab33-4ce4-80d4-bbb3ebbf2814}')
DEVINTERFACE_MIDI_INPUT: Guid = Guid('{504be32c-ccf6-4d2c-b73f-6f8b3747e22b}')
EVENTCONTEXT_VOLUMESLIDER: Guid = Guid('{e2c2e9de-09b1-4b04-84e5-07931225ee04}')
SPATIAL_AUDIO_STANDARD_COMMANDS_START: UInt32 = 200
SPATIAL_AUDIO_POSITION: UInt32 = 200
SPTLAUD_MD_CLNT_E_COMMAND_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2004286976
SPTLAUD_MD_CLNT_E_OBJECT_NOT_INITIALIZED: win32more.Windows.Win32.Foundation.HRESULT = -2004286975
SPTLAUD_MD_CLNT_E_INVALID_ARGS: win32more.Windows.Win32.Foundation.HRESULT = -2004286974
SPTLAUD_MD_CLNT_E_METADATA_FORMAT_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2004286973
SPTLAUD_MD_CLNT_E_VALUE_BUFFER_INCORRECT_SIZE: win32more.Windows.Win32.Foundation.HRESULT = -2004286972
SPTLAUD_MD_CLNT_E_MEMORY_BOUNDS: win32more.Windows.Win32.Foundation.HRESULT = -2004286971
SPTLAUD_MD_CLNT_E_NO_MORE_COMMANDS: win32more.Windows.Win32.Foundation.HRESULT = -2004286970
SPTLAUD_MD_CLNT_E_BUFFER_ALREADY_ATTACHED: win32more.Windows.Win32.Foundation.HRESULT = -2004286969
SPTLAUD_MD_CLNT_E_BUFFER_NOT_ATTACHED: win32more.Windows.Win32.Foundation.HRESULT = -2004286968
SPTLAUD_MD_CLNT_E_FRAMECOUNT_OUT_OF_RANGE: win32more.Windows.Win32.Foundation.HRESULT = -2004286967
SPTLAUD_MD_CLNT_E_NO_ITEMS_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2004286960
SPTLAUD_MD_CLNT_E_ITEM_COPY_OVERFLOW: win32more.Windows.Win32.Foundation.HRESULT = -2004286959
SPTLAUD_MD_CLNT_E_NO_ITEMS_OPEN: win32more.Windows.Win32.Foundation.HRESULT = -2004286958
SPTLAUD_MD_CLNT_E_ITEMS_ALREADY_OPEN: win32more.Windows.Win32.Foundation.HRESULT = -2004286957
SPTLAUD_MD_CLNT_E_ATTACH_FAILED_INTERNAL_BUFFER: win32more.Windows.Win32.Foundation.HRESULT = -2004286956
SPTLAUD_MD_CLNT_E_DETACH_FAILED_INTERNAL_BUFFER: win32more.Windows.Win32.Foundation.HRESULT = -2004286955
SPTLAUD_MD_CLNT_E_NO_BUFFER_ATTACHED: win32more.Windows.Win32.Foundation.HRESULT = -2004286954
SPTLAUD_MD_CLNT_E_NO_MORE_ITEMS: win32more.Windows.Win32.Foundation.HRESULT = -2004286953
SPTLAUD_MD_CLNT_E_FRAMEOFFSET_OUT_OF_RANGE: win32more.Windows.Win32.Foundation.HRESULT = -2004286952
SPTLAUD_MD_CLNT_E_ITEM_MUST_HAVE_COMMANDS: win32more.Windows.Win32.Foundation.HRESULT = -2004286951
SPTLAUD_MD_CLNT_E_NO_ITEMOFFSET_WRITTEN: win32more.Windows.Win32.Foundation.HRESULT = -2004286944
SPTLAUD_MD_CLNT_E_NO_ITEMS_WRITTEN: win32more.Windows.Win32.Foundation.HRESULT = -2004286943
SPTLAUD_MD_CLNT_E_COMMAND_ALREADY_WRITTEN: win32more.Windows.Win32.Foundation.HRESULT = -2004286942
SPTLAUD_MD_CLNT_E_FORMAT_MISMATCH: win32more.Windows.Win32.Foundation.HRESULT = -2004286941
SPTLAUD_MD_CLNT_E_BUFFER_STILL_ATTACHED: win32more.Windows.Win32.Foundation.HRESULT = -2004286940
SPTLAUD_MD_CLNT_E_ITEMS_LOCKED_FOR_WRITING: win32more.Windows.Win32.Foundation.HRESULT = -2004286939
VIRTUAL_AUDIO_DEVICE_PROCESS_LOOPBACK: String = 'VAD\\Process_Loopback'
WAVERR_BADFORMAT: UInt32 = 32
WAVERR_STILLPLAYING: UInt32 = 33
WAVERR_UNPREPARED: UInt32 = 34
WAVERR_SYNC: UInt32 = 35
WAVERR_LASTERROR: UInt32 = 35
WHDR_DONE: UInt32 = 1
WHDR_PREPARED: UInt32 = 2
WHDR_BEGINLOOP: UInt32 = 4
WHDR_ENDLOOP: UInt32 = 8
WHDR_INQUEUE: UInt32 = 16
WAVECAPS_PITCH: UInt32 = 1
WAVECAPS_PLAYBACKRATE: UInt32 = 2
WAVECAPS_VOLUME: UInt32 = 4
WAVECAPS_LRVOLUME: UInt32 = 8
WAVECAPS_SYNC: UInt32 = 16
WAVECAPS_SAMPLEACCURATE: UInt32 = 32
WAVE_INVALIDFORMAT: UInt32 = 0
WAVE_FORMAT_1M08: UInt32 = 1
WAVE_FORMAT_1S08: UInt32 = 2
WAVE_FORMAT_1M16: UInt32 = 4
WAVE_FORMAT_1S16: UInt32 = 8
WAVE_FORMAT_2M08: UInt32 = 16
WAVE_FORMAT_2S08: UInt32 = 32
WAVE_FORMAT_2M16: UInt32 = 64
WAVE_FORMAT_2S16: UInt32 = 128
WAVE_FORMAT_4M08: UInt32 = 256
WAVE_FORMAT_4S08: UInt32 = 512
WAVE_FORMAT_4M16: UInt32 = 1024
WAVE_FORMAT_4S16: UInt32 = 2048
WAVE_FORMAT_44M08: UInt32 = 256
WAVE_FORMAT_44S08: UInt32 = 512
WAVE_FORMAT_44M16: UInt32 = 1024
WAVE_FORMAT_44S16: UInt32 = 2048
WAVE_FORMAT_48M08: UInt32 = 4096
WAVE_FORMAT_48S08: UInt32 = 8192
WAVE_FORMAT_48M16: UInt32 = 16384
WAVE_FORMAT_48S16: UInt32 = 32768
WAVE_FORMAT_96M08: UInt32 = 65536
WAVE_FORMAT_96S08: UInt32 = 131072
WAVE_FORMAT_96M16: UInt32 = 262144
WAVE_FORMAT_96S16: UInt32 = 524288
WAVE_FORMAT_PCM: UInt32 = 1
MIDIERR_UNPREPARED: UInt32 = 64
MIDIERR_STILLPLAYING: UInt32 = 65
MIDIERR_NOMAP: UInt32 = 66
MIDIERR_NOTREADY: UInt32 = 67
MIDIERR_NODEVICE: UInt32 = 68
MIDIERR_INVALIDSETUP: UInt32 = 69
MIDIERR_BADOPENMODE: UInt32 = 70
MIDIERR_DONT_CONTINUE: UInt32 = 71
MIDIERR_LASTERROR: UInt32 = 71
MIDIPATCHSIZE: UInt32 = 128
MIDI_CACHE_ALL: UInt32 = 1
MIDI_CACHE_BESTFIT: UInt32 = 2
MIDI_CACHE_QUERY: UInt32 = 3
MIDI_UNCACHE: UInt32 = 4
MOD_MIDIPORT: UInt32 = 1
MOD_SYNTH: UInt32 = 2
MOD_SQSYNTH: UInt32 = 3
MOD_FMSYNTH: UInt32 = 4
MOD_MAPPER: UInt32 = 5
MOD_WAVETABLE: UInt32 = 6
MOD_SWSYNTH: UInt32 = 7
MIDICAPS_VOLUME: UInt32 = 1
MIDICAPS_LRVOLUME: UInt32 = 2
MIDICAPS_CACHE: UInt32 = 4
MIDICAPS_STREAM: UInt32 = 8
MHDR_DONE: UInt32 = 1
MHDR_PREPARED: UInt32 = 2
MHDR_INQUEUE: UInt32 = 4
MHDR_ISSTRM: UInt32 = 8
MEVT_F_SHORT: Int32 = 0
MEVT_F_LONG: Int32 = -2147483648
MEVT_F_CALLBACK: Int32 = 1073741824
MEVT_SHORTMSG: Byte = 0
MEVT_TEMPO: Byte = 1
MEVT_NOP: Byte = 2
MEVT_LONGMSG: Byte = 128
MEVT_COMMENT: Byte = 130
MEVT_VERSION: Byte = 132
MIDISTRM_ERROR: Int32 = -2
MIDIPROP_SET: Int32 = -2147483648
MIDIPROP_GET: Int32 = 1073741824
MIDIPROP_TIMEDIV: Int32 = 1
MIDIPROP_TEMPO: Int32 = 2
AUXCAPS_CDAUDIO: UInt32 = 1
AUXCAPS_AUXIN: UInt32 = 2
AUXCAPS_VOLUME: UInt32 = 1
AUXCAPS_LRVOLUME: UInt32 = 2
MIXER_SHORT_NAME_CHARS: UInt32 = 16
MIXER_LONG_NAME_CHARS: UInt32 = 64
MIXERR_INVALLINE: UInt32 = 1024
MIXERR_INVALCONTROL: UInt32 = 1025
MIXERR_INVALVALUE: UInt32 = 1026
MIXERR_LASTERROR: UInt32 = 1026
MIXER_OBJECTF_HANDLE: Int32 = -2147483648
MIXER_OBJECTF_MIXER: Int32 = 0
MIXER_OBJECTF_WAVEOUT: Int32 = 268435456
MIXER_OBJECTF_WAVEIN: Int32 = 536870912
MIXER_OBJECTF_MIDIOUT: Int32 = 805306368
MIXER_OBJECTF_MIDIIN: Int32 = 1073741824
MIXER_OBJECTF_AUX: Int32 = 1342177280
MIXERLINE_LINEF_ACTIVE: Int32 = 1
MIXERLINE_LINEF_DISCONNECTED: Int32 = 32768
MIXERLINE_LINEF_SOURCE: Int32 = -2147483648
MIXERLINE_COMPONENTTYPE_DST_FIRST: Int32 = 0
MIXERLINE_COMPONENTTYPE_DST_LAST: UInt32 = 8
MIXERLINE_COMPONENTTYPE_SRC_FIRST: Int32 = 4096
MIXERLINE_COMPONENTTYPE_SRC_LAST: UInt32 = 4106
MIXERLINE_TARGETTYPE_UNDEFINED: UInt32 = 0
MIXERLINE_TARGETTYPE_WAVEOUT: UInt32 = 1
MIXERLINE_TARGETTYPE_WAVEIN: UInt32 = 2
MIXERLINE_TARGETTYPE_MIDIOUT: UInt32 = 3
MIXERLINE_TARGETTYPE_MIDIIN: UInt32 = 4
MIXERLINE_TARGETTYPE_AUX: UInt32 = 5
MIXER_GETLINEINFOF_DESTINATION: Int32 = 0
MIXER_GETLINEINFOF_SOURCE: Int32 = 1
MIXER_GETLINEINFOF_LINEID: Int32 = 2
MIXER_GETLINEINFOF_COMPONENTTYPE: Int32 = 3
MIXER_GETLINEINFOF_TARGETTYPE: Int32 = 4
MIXER_GETLINEINFOF_QUERYMASK: Int32 = 15
MIXERCONTROL_CONTROLF_UNIFORM: Int32 = 1
MIXERCONTROL_CONTROLF_MULTIPLE: Int32 = 2
MIXERCONTROL_CONTROLF_DISABLED: Int32 = -2147483648
MIXERCONTROL_CT_CLASS_MASK: Int32 = -268435456
MIXERCONTROL_CT_CLASS_CUSTOM: Int32 = 0
MIXERCONTROL_CT_CLASS_METER: Int32 = 268435456
MIXERCONTROL_CT_CLASS_SWITCH: Int32 = 536870912
MIXERCONTROL_CT_CLASS_NUMBER: Int32 = 805306368
MIXERCONTROL_CT_CLASS_SLIDER: Int32 = 1073741824
MIXERCONTROL_CT_CLASS_FADER: Int32 = 1342177280
MIXERCONTROL_CT_CLASS_TIME: Int32 = 1610612736
MIXERCONTROL_CT_CLASS_LIST: Int32 = 1879048192
MIXERCONTROL_CT_SUBCLASS_MASK: Int32 = 251658240
MIXERCONTROL_CT_SC_SWITCH_BOOLEAN: Int32 = 0
MIXERCONTROL_CT_SC_SWITCH_BUTTON: Int32 = 16777216
MIXERCONTROL_CT_SC_METER_POLLED: Int32 = 0
MIXERCONTROL_CT_SC_TIME_MICROSECS: Int32 = 0
MIXERCONTROL_CT_SC_TIME_MILLISECS: Int32 = 16777216
MIXERCONTROL_CT_SC_LIST_SINGLE: Int32 = 0
MIXERCONTROL_CT_SC_LIST_MULTIPLE: Int32 = 16777216
MIXERCONTROL_CT_UNITS_MASK: Int32 = 16711680
MIXERCONTROL_CT_UNITS_CUSTOM: Int32 = 0
MIXERCONTROL_CT_UNITS_BOOLEAN: Int32 = 65536
MIXERCONTROL_CT_UNITS_SIGNED: Int32 = 131072
MIXERCONTROL_CT_UNITS_UNSIGNED: Int32 = 196608
MIXERCONTROL_CT_UNITS_DECIBELS: Int32 = 262144
MIXERCONTROL_CT_UNITS_PERCENT: Int32 = 327680
MIXER_GETLINECONTROLSF_ALL: Int32 = 0
MIXER_GETLINECONTROLSF_ONEBYID: Int32 = 1
MIXER_GETLINECONTROLSF_ONEBYTYPE: Int32 = 2
MIXER_GETLINECONTROLSF_QUERYMASK: Int32 = 15
MIXER_GETCONTROLDETAILSF_VALUE: Int32 = 0
MIXER_GETCONTROLDETAILSF_LISTTEXT: Int32 = 1
MIXER_GETCONTROLDETAILSF_QUERYMASK: Int32 = 15
MIXER_SETCONTROLDETAILSF_VALUE: Int32 = 0
MIXER_SETCONTROLDETAILSF_CUSTOM: Int32 = 1
MIXER_SETCONTROLDETAILSF_QUERYMASK: Int32 = 15
DRV_MAPPER_PREFERRED_INPUT_GET: UInt32 = 16384
DRV_MAPPER_PREFERRED_OUTPUT_GET: UInt32 = 16386
DRVM_MAPPER: UInt32 = 8192
DRVM_MAPPER_STATUS: UInt32 = 8192
WIDM_MAPPER_STATUS: UInt32 = 8192
WAVEIN_MAPPER_STATUS_DEVICE: UInt32 = 0
WAVEIN_MAPPER_STATUS_MAPPED: UInt32 = 1
WAVEIN_MAPPER_STATUS_FORMAT: UInt32 = 2
WODM_MAPPER_STATUS: UInt32 = 8192
WAVEOUT_MAPPER_STATUS_DEVICE: UInt32 = 0
WAVEOUT_MAPPER_STATUS_MAPPED: UInt32 = 1
WAVEOUT_MAPPER_STATUS_FORMAT: UInt32 = 2
ACMERR_BASE: UInt32 = 512
ACMERR_NOTPOSSIBLE: UInt32 = 512
ACMERR_BUSY: UInt32 = 513
ACMERR_UNPREPARED: UInt32 = 514
ACMERR_CANCELED: UInt32 = 515
ACM_METRIC_COUNT_DRIVERS: UInt32 = 1
ACM_METRIC_COUNT_CODECS: UInt32 = 2
ACM_METRIC_COUNT_CONVERTERS: UInt32 = 3
ACM_METRIC_COUNT_FILTERS: UInt32 = 4
ACM_METRIC_COUNT_DISABLED: UInt32 = 5
ACM_METRIC_COUNT_HARDWARE: UInt32 = 6
ACM_METRIC_COUNT_LOCAL_DRIVERS: UInt32 = 20
ACM_METRIC_COUNT_LOCAL_CODECS: UInt32 = 21
ACM_METRIC_COUNT_LOCAL_CONVERTERS: UInt32 = 22
ACM_METRIC_COUNT_LOCAL_FILTERS: UInt32 = 23
ACM_METRIC_COUNT_LOCAL_DISABLED: UInt32 = 24
ACM_METRIC_HARDWARE_WAVE_INPUT: UInt32 = 30
ACM_METRIC_HARDWARE_WAVE_OUTPUT: UInt32 = 31
ACM_METRIC_MAX_SIZE_FORMAT: UInt32 = 50
ACM_METRIC_MAX_SIZE_FILTER: UInt32 = 51
ACM_METRIC_DRIVER_SUPPORT: UInt32 = 100
ACM_METRIC_DRIVER_PRIORITY: UInt32 = 101
ACM_DRIVERENUMF_NOLOCAL: Int32 = 1073741824
ACM_DRIVERENUMF_DISABLED: Int32 = -2147483648
ACM_DRIVERADDF_NAME: Int32 = 1
ACM_DRIVERADDF_FUNCTION: Int32 = 3
ACM_DRIVERADDF_NOTIFYHWND: Int32 = 4
ACM_DRIVERADDF_TYPEMASK: Int32 = 7
ACM_DRIVERADDF_LOCAL: Int32 = 0
ACM_DRIVERADDF_GLOBAL: Int32 = 8
ACMDM_USER: UInt32 = 16384
ACMDM_RESERVED_LOW: UInt32 = 24576
ACMDM_RESERVED_HIGH: UInt32 = 28671
ACMDM_DRIVER_ABOUT: UInt32 = 24587
ACM_DRIVERPRIORITYF_ENABLE: Int32 = 1
ACM_DRIVERPRIORITYF_DISABLE: Int32 = 2
ACM_DRIVERPRIORITYF_ABLEMASK: Int32 = 3
ACM_DRIVERPRIORITYF_BEGIN: Int32 = 65536
ACM_DRIVERPRIORITYF_END: Int32 = 131072
ACM_DRIVERPRIORITYF_DEFERMASK: Int32 = 196608
ACMDRIVERDETAILS_SHORTNAME_CHARS: UInt32 = 32
ACMDRIVERDETAILS_LONGNAME_CHARS: UInt32 = 128
ACMDRIVERDETAILS_COPYRIGHT_CHARS: UInt32 = 80
ACMDRIVERDETAILS_LICENSING_CHARS: UInt32 = 128
ACMDRIVERDETAILS_FEATURES_CHARS: UInt32 = 512
ACMDRIVERDETAILS_SUPPORTF_CODEC: Int32 = 1
ACMDRIVERDETAILS_SUPPORTF_CONVERTER: Int32 = 2
ACMDRIVERDETAILS_SUPPORTF_FILTER: Int32 = 4
ACMDRIVERDETAILS_SUPPORTF_HARDWARE: Int32 = 8
ACMDRIVERDETAILS_SUPPORTF_ASYNC: Int32 = 16
ACMDRIVERDETAILS_SUPPORTF_LOCAL: Int32 = 1073741824
ACMDRIVERDETAILS_SUPPORTF_DISABLED: Int32 = -2147483648
ACMFORMATTAGDETAILS_FORMATTAG_CHARS: UInt32 = 48
ACM_FORMATTAGDETAILSF_INDEX: Int32 = 0
ACM_FORMATTAGDETAILSF_FORMATTAG: Int32 = 1
ACM_FORMATTAGDETAILSF_LARGESTSIZE: Int32 = 2
ACM_FORMATTAGDETAILSF_QUERYMASK: Int32 = 15
ACMFORMATDETAILS_FORMAT_CHARS: UInt32 = 128
ACM_FORMATDETAILSF_INDEX: Int32 = 0
ACM_FORMATDETAILSF_FORMAT: Int32 = 1
ACM_FORMATDETAILSF_QUERYMASK: Int32 = 15
ACM_FORMATENUMF_WFORMATTAG: Int32 = 65536
ACM_FORMATENUMF_NCHANNELS: Int32 = 131072
ACM_FORMATENUMF_NSAMPLESPERSEC: Int32 = 262144
ACM_FORMATENUMF_WBITSPERSAMPLE: Int32 = 524288
ACM_FORMATENUMF_CONVERT: Int32 = 1048576
ACM_FORMATENUMF_SUGGEST: Int32 = 2097152
ACM_FORMATENUMF_HARDWARE: Int32 = 4194304
ACM_FORMATENUMF_INPUT: Int32 = 8388608
ACM_FORMATENUMF_OUTPUT: Int32 = 16777216
ACM_FORMATSUGGESTF_WFORMATTAG: Int32 = 65536
ACM_FORMATSUGGESTF_NCHANNELS: Int32 = 131072
ACM_FORMATSUGGESTF_NSAMPLESPERSEC: Int32 = 262144
ACM_FORMATSUGGESTF_WBITSPERSAMPLE: Int32 = 524288
ACM_FORMATSUGGESTF_TYPEMASK: Int32 = 16711680
ACMHELPMSGSTRINGA: String = 'acmchoose_help'
ACMHELPMSGSTRINGW: String = 'acmchoose_help'
ACMHELPMSGCONTEXTMENUA: String = 'acmchoose_contextmenu'
ACMHELPMSGCONTEXTMENUW: String = 'acmchoose_contextmenu'
ACMHELPMSGCONTEXTHELPA: String = 'acmchoose_contexthelp'
ACMHELPMSGCONTEXTHELPW: String = 'acmchoose_contexthelp'
ACMHELPMSGSTRING: String = 'acmchoose_help'
ACMHELPMSGCONTEXTMENU: String = 'acmchoose_contextmenu'
ACMHELPMSGCONTEXTHELP: String = 'acmchoose_contexthelp'
MM_ACM_FORMATCHOOSE: UInt32 = 32768
FORMATCHOOSE_MESSAGE: UInt32 = 0
FORMATCHOOSE_FORMATTAG_VERIFY: UInt32 = 0
FORMATCHOOSE_FORMAT_VERIFY: UInt32 = 1
FORMATCHOOSE_CUSTOM_VERIFY: UInt32 = 2
ACMFORMATCHOOSE_STYLEF_SHOWHELP: Int32 = 4
ACMFORMATCHOOSE_STYLEF_ENABLEHOOK: Int32 = 8
ACMFORMATCHOOSE_STYLEF_ENABLETEMPLATE: Int32 = 16
ACMFORMATCHOOSE_STYLEF_ENABLETEMPLATEHANDLE: Int32 = 32
ACMFORMATCHOOSE_STYLEF_INITTOWFXSTRUCT: Int32 = 64
ACMFORMATCHOOSE_STYLEF_CONTEXTHELP: Int32 = 128
ACMFILTERTAGDETAILS_FILTERTAG_CHARS: UInt32 = 48
ACM_FILTERTAGDETAILSF_INDEX: Int32 = 0
ACM_FILTERTAGDETAILSF_FILTERTAG: Int32 = 1
ACM_FILTERTAGDETAILSF_LARGESTSIZE: Int32 = 2
ACM_FILTERTAGDETAILSF_QUERYMASK: Int32 = 15
ACMFILTERDETAILS_FILTER_CHARS: UInt32 = 128
ACM_FILTERDETAILSF_INDEX: Int32 = 0
ACM_FILTERDETAILSF_FILTER: Int32 = 1
ACM_FILTERDETAILSF_QUERYMASK: Int32 = 15
ACM_FILTERENUMF_DWFILTERTAG: Int32 = 65536
MM_ACM_FILTERCHOOSE: UInt32 = 32768
FILTERCHOOSE_MESSAGE: UInt32 = 0
FILTERCHOOSE_FILTERTAG_VERIFY: UInt32 = 0
FILTERCHOOSE_FILTER_VERIFY: UInt32 = 1
FILTERCHOOSE_CUSTOM_VERIFY: UInt32 = 2
ACMFILTERCHOOSE_STYLEF_SHOWHELP: Int32 = 4
ACMFILTERCHOOSE_STYLEF_ENABLEHOOK: Int32 = 8
ACMFILTERCHOOSE_STYLEF_ENABLETEMPLATE: Int32 = 16
ACMFILTERCHOOSE_STYLEF_ENABLETEMPLATEHANDLE: Int32 = 32
ACMFILTERCHOOSE_STYLEF_INITTOFILTERSTRUCT: Int32 = 64
ACMFILTERCHOOSE_STYLEF_CONTEXTHELP: Int32 = 128
ACMSTREAMHEADER_STATUSF_DONE: Int32 = 65536
ACMSTREAMHEADER_STATUSF_PREPARED: Int32 = 131072
ACMSTREAMHEADER_STATUSF_INQUEUE: Int32 = 1048576
ACM_STREAMOPENF_QUERY: UInt32 = 1
ACM_STREAMOPENF_ASYNC: UInt32 = 2
ACM_STREAMOPENF_NONREALTIME: UInt32 = 4
ACM_STREAMSIZEF_SOURCE: Int32 = 0
ACM_STREAMSIZEF_DESTINATION: Int32 = 1
ACM_STREAMSIZEF_QUERYMASK: Int32 = 15
ACM_STREAMCONVERTF_BLOCKALIGN: UInt32 = 4
ACM_STREAMCONVERTF_START: UInt32 = 16
ACM_STREAMCONVERTF_END: UInt32 = 32
SND_RING: Int32 = 1048576
SND_ALIAS_START: UInt32 = 0
ACMDM_DRIVER_NOTIFY: UInt32 = 24577
ACMDM_DRIVER_DETAILS: UInt32 = 24586
ACMDM_HARDWARE_WAVE_CAPS_INPUT: UInt32 = 24596
ACMDM_HARDWARE_WAVE_CAPS_OUTPUT: UInt32 = 24597
ACMDM_FORMATTAG_DETAILS: UInt32 = 24601
ACMDM_FORMAT_DETAILS: UInt32 = 24602
ACMDM_FORMAT_SUGGEST: UInt32 = 24603
ACMDM_FILTERTAG_DETAILS: UInt32 = 24626
ACMDM_FILTER_DETAILS: UInt32 = 24627
ACMDM_STREAM_OPEN: UInt32 = 24652
ACMDM_STREAM_CLOSE: UInt32 = 24653
ACMDM_STREAM_SIZE: UInt32 = 24654
ACMDM_STREAM_CONVERT: UInt32 = 24655
ACMDM_STREAM_RESET: UInt32 = 24656
ACMDM_STREAM_PREPARE: UInt32 = 24657
ACMDM_STREAM_UNPREPARE: UInt32 = 24658
ACMDM_STREAM_UPDATE: UInt32 = 24659
@winfunctype('OLE32.dll')
def CoRegisterMessageFilter(lpMessageFilter: win32more.Windows.Win32.Media.Audio.IMessageFilter, lplpMessageFilter: POINTER(win32more.Windows.Win32.Media.Audio.IMessageFilter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WINMM.dll')
def sndPlaySoundA(pszSound: win32more.Windows.Win32.Foundation.PSTR, fuSound: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINMM.dll')
def sndPlaySoundW(pszSound: win32more.Windows.Win32.Foundation.PWSTR, fuSound: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
sndPlaySound = UnicodeAlias('sndPlaySoundW')
@winfunctype('WINMM.dll')
def PlaySoundA(pszSound: win32more.Windows.Win32.Foundation.PSTR, hmod: win32more.Windows.Win32.Foundation.HMODULE, fdwSound: win32more.Windows.Win32.Media.Audio.SND_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINMM.dll')
def PlaySoundW(pszSound: win32more.Windows.Win32.Foundation.PWSTR, hmod: win32more.Windows.Win32.Foundation.HMODULE, fdwSound: win32more.Windows.Win32.Media.Audio.SND_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
PlaySound = UnicodeAlias('PlaySoundW')
@winfunctype('WINMM.dll')
def waveOutGetNumDevs() -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutGetDevCapsA(uDeviceID: UIntPtr, pwoc: POINTER(win32more.Windows.Win32.Media.Audio.WAVEOUTCAPSA), cbwoc: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutGetDevCapsW(uDeviceID: UIntPtr, pwoc: POINTER(win32more.Windows.Win32.Media.Audio.WAVEOUTCAPSW), cbwoc: UInt32) -> UInt32: ...
waveOutGetDevCaps = UnicodeAlias('waveOutGetDevCapsW')
@winfunctype('WINMM.dll')
def waveOutGetVolume(hwo: win32more.Windows.Win32.Media.Audio.HWAVEOUT, pdwVolume: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutSetVolume(hwo: win32more.Windows.Win32.Media.Audio.HWAVEOUT, dwVolume: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutGetErrorTextA(mmrError: UInt32, pszText: win32more.Windows.Win32.Foundation.PSTR, cchText: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutGetErrorTextW(mmrError: UInt32, pszText: win32more.Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> UInt32: ...
waveOutGetErrorText = UnicodeAlias('waveOutGetErrorTextW')
@winfunctype('WINMM.dll')
def waveOutOpen(phwo: POINTER(win32more.Windows.Win32.Media.Audio.HWAVEOUT), uDeviceID: UInt32, pwfx: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), dwCallback: UIntPtr, dwInstance: UIntPtr, fdwOpen: win32more.Windows.Win32.Media.Audio.MIDI_WAVE_OPEN_TYPE) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutClose(hwo: win32more.Windows.Win32.Media.Audio.HWAVEOUT) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutPrepareHeader(hwo: win32more.Windows.Win32.Media.Audio.HWAVEOUT, pwh: POINTER(win32more.Windows.Win32.Media.Audio.WAVEHDR), cbwh: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutUnprepareHeader(hwo: win32more.Windows.Win32.Media.Audio.HWAVEOUT, pwh: POINTER(win32more.Windows.Win32.Media.Audio.WAVEHDR), cbwh: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutWrite(hwo: win32more.Windows.Win32.Media.Audio.HWAVEOUT, pwh: POINTER(win32more.Windows.Win32.Media.Audio.WAVEHDR), cbwh: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutPause(hwo: win32more.Windows.Win32.Media.Audio.HWAVEOUT) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutRestart(hwo: win32more.Windows.Win32.Media.Audio.HWAVEOUT) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutReset(hwo: win32more.Windows.Win32.Media.Audio.HWAVEOUT) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutBreakLoop(hwo: win32more.Windows.Win32.Media.Audio.HWAVEOUT) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutGetPosition(hwo: win32more.Windows.Win32.Media.Audio.HWAVEOUT, pmmt: POINTER(win32more.Windows.Win32.Media.MMTIME), cbmmt: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutGetPitch(hwo: win32more.Windows.Win32.Media.Audio.HWAVEOUT, pdwPitch: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutSetPitch(hwo: win32more.Windows.Win32.Media.Audio.HWAVEOUT, dwPitch: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutGetPlaybackRate(hwo: win32more.Windows.Win32.Media.Audio.HWAVEOUT, pdwRate: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutSetPlaybackRate(hwo: win32more.Windows.Win32.Media.Audio.HWAVEOUT, dwRate: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutGetID(hwo: win32more.Windows.Win32.Media.Audio.HWAVEOUT, puDeviceID: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutMessage(hwo: win32more.Windows.Win32.Media.Audio.HWAVEOUT, uMsg: UInt32, dw1: UIntPtr, dw2: UIntPtr) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInGetNumDevs() -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInGetDevCapsA(uDeviceID: UIntPtr, pwic: POINTER(win32more.Windows.Win32.Media.Audio.WAVEINCAPSA), cbwic: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInGetDevCapsW(uDeviceID: UIntPtr, pwic: POINTER(win32more.Windows.Win32.Media.Audio.WAVEINCAPSW), cbwic: UInt32) -> UInt32: ...
waveInGetDevCaps = UnicodeAlias('waveInGetDevCapsW')
@winfunctype('WINMM.dll')
def waveInGetErrorTextA(mmrError: UInt32, pszText: win32more.Windows.Win32.Foundation.PSTR, cchText: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInGetErrorTextW(mmrError: UInt32, pszText: win32more.Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> UInt32: ...
waveInGetErrorText = UnicodeAlias('waveInGetErrorTextW')
@winfunctype('WINMM.dll')
def waveInOpen(phwi: POINTER(win32more.Windows.Win32.Media.Audio.HWAVEIN), uDeviceID: UInt32, pwfx: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), dwCallback: UIntPtr, dwInstance: UIntPtr, fdwOpen: win32more.Windows.Win32.Media.Audio.MIDI_WAVE_OPEN_TYPE) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInClose(hwi: win32more.Windows.Win32.Media.Audio.HWAVEIN) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInPrepareHeader(hwi: win32more.Windows.Win32.Media.Audio.HWAVEIN, pwh: POINTER(win32more.Windows.Win32.Media.Audio.WAVEHDR), cbwh: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInUnprepareHeader(hwi: win32more.Windows.Win32.Media.Audio.HWAVEIN, pwh: POINTER(win32more.Windows.Win32.Media.Audio.WAVEHDR), cbwh: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInAddBuffer(hwi: win32more.Windows.Win32.Media.Audio.HWAVEIN, pwh: POINTER(win32more.Windows.Win32.Media.Audio.WAVEHDR), cbwh: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInStart(hwi: win32more.Windows.Win32.Media.Audio.HWAVEIN) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInStop(hwi: win32more.Windows.Win32.Media.Audio.HWAVEIN) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInReset(hwi: win32more.Windows.Win32.Media.Audio.HWAVEIN) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInGetPosition(hwi: win32more.Windows.Win32.Media.Audio.HWAVEIN, pmmt: POINTER(win32more.Windows.Win32.Media.MMTIME), cbmmt: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInGetID(hwi: win32more.Windows.Win32.Media.Audio.HWAVEIN, puDeviceID: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInMessage(hwi: win32more.Windows.Win32.Media.Audio.HWAVEIN, uMsg: UInt32, dw1: UIntPtr, dw2: UIntPtr) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutGetNumDevs() -> UInt32: ...
@winfunctype('WINMM.dll')
def midiStreamOpen(phms: POINTER(win32more.Windows.Win32.Media.Audio.HMIDISTRM), puDeviceID: POINTER(UInt32), cMidi: UInt32, dwCallback: UIntPtr, dwInstance: UIntPtr, fdwOpen: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiStreamClose(hms: win32more.Windows.Win32.Media.Audio.HMIDISTRM) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiStreamProperty(hms: win32more.Windows.Win32.Media.Audio.HMIDISTRM, lppropdata: POINTER(Byte), dwProperty: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiStreamPosition(hms: win32more.Windows.Win32.Media.Audio.HMIDISTRM, lpmmt: POINTER(win32more.Windows.Win32.Media.MMTIME), cbmmt: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiStreamOut(hms: win32more.Windows.Win32.Media.Audio.HMIDISTRM, pmh: POINTER(win32more.Windows.Win32.Media.Audio.MIDIHDR), cbmh: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiStreamPause(hms: win32more.Windows.Win32.Media.Audio.HMIDISTRM) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiStreamRestart(hms: win32more.Windows.Win32.Media.Audio.HMIDISTRM) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiStreamStop(hms: win32more.Windows.Win32.Media.Audio.HMIDISTRM) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiConnect(hmi: win32more.Windows.Win32.Media.Audio.HMIDI, hmo: win32more.Windows.Win32.Media.Audio.HMIDIOUT, pReserved: VoidPtr) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiDisconnect(hmi: win32more.Windows.Win32.Media.Audio.HMIDI, hmo: win32more.Windows.Win32.Media.Audio.HMIDIOUT, pReserved: VoidPtr) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutGetDevCapsA(uDeviceID: UIntPtr, pmoc: POINTER(win32more.Windows.Win32.Media.Audio.MIDIOUTCAPSA), cbmoc: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutGetDevCapsW(uDeviceID: UIntPtr, pmoc: POINTER(win32more.Windows.Win32.Media.Audio.MIDIOUTCAPSW), cbmoc: UInt32) -> UInt32: ...
midiOutGetDevCaps = UnicodeAlias('midiOutGetDevCapsW')
@winfunctype('WINMM.dll')
def midiOutGetVolume(hmo: win32more.Windows.Win32.Media.Audio.HMIDIOUT, pdwVolume: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutSetVolume(hmo: win32more.Windows.Win32.Media.Audio.HMIDIOUT, dwVolume: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutGetErrorTextA(mmrError: UInt32, pszText: win32more.Windows.Win32.Foundation.PSTR, cchText: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutGetErrorTextW(mmrError: UInt32, pszText: win32more.Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> UInt32: ...
midiOutGetErrorText = UnicodeAlias('midiOutGetErrorTextW')
@winfunctype('WINMM.dll')
def midiOutOpen(phmo: POINTER(win32more.Windows.Win32.Media.Audio.HMIDIOUT), uDeviceID: UInt32, dwCallback: UIntPtr, dwInstance: UIntPtr, fdwOpen: win32more.Windows.Win32.Media.Audio.MIDI_WAVE_OPEN_TYPE) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutClose(hmo: win32more.Windows.Win32.Media.Audio.HMIDIOUT) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutPrepareHeader(hmo: win32more.Windows.Win32.Media.Audio.HMIDIOUT, pmh: POINTER(win32more.Windows.Win32.Media.Audio.MIDIHDR), cbmh: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutUnprepareHeader(hmo: win32more.Windows.Win32.Media.Audio.HMIDIOUT, pmh: POINTER(win32more.Windows.Win32.Media.Audio.MIDIHDR), cbmh: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutShortMsg(hmo: win32more.Windows.Win32.Media.Audio.HMIDIOUT, dwMsg: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutLongMsg(hmo: win32more.Windows.Win32.Media.Audio.HMIDIOUT, pmh: POINTER(win32more.Windows.Win32.Media.Audio.MIDIHDR), cbmh: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutReset(hmo: win32more.Windows.Win32.Media.Audio.HMIDIOUT) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutCachePatches(hmo: win32more.Windows.Win32.Media.Audio.HMIDIOUT, uBank: UInt32, pwpa: POINTER(UInt16), fuCache: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutCacheDrumPatches(hmo: win32more.Windows.Win32.Media.Audio.HMIDIOUT, uPatch: UInt32, pwkya: POINTER(UInt16), fuCache: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutGetID(hmo: win32more.Windows.Win32.Media.Audio.HMIDIOUT, puDeviceID: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutMessage(hmo: win32more.Windows.Win32.Media.Audio.HMIDIOUT, uMsg: UInt32, dw1: UIntPtr, dw2: UIntPtr) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInGetNumDevs() -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInGetDevCapsA(uDeviceID: UIntPtr, pmic: POINTER(win32more.Windows.Win32.Media.Audio.MIDIINCAPSA), cbmic: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInGetDevCapsW(uDeviceID: UIntPtr, pmic: POINTER(win32more.Windows.Win32.Media.Audio.MIDIINCAPSW), cbmic: UInt32) -> UInt32: ...
midiInGetDevCaps = UnicodeAlias('midiInGetDevCapsW')
@winfunctype('WINMM.dll')
def midiInGetErrorTextA(mmrError: UInt32, pszText: win32more.Windows.Win32.Foundation.PSTR, cchText: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInGetErrorTextW(mmrError: UInt32, pszText: win32more.Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> UInt32: ...
midiInGetErrorText = UnicodeAlias('midiInGetErrorTextW')
@winfunctype('WINMM.dll')
def midiInOpen(phmi: POINTER(win32more.Windows.Win32.Media.Audio.HMIDIIN), uDeviceID: UInt32, dwCallback: UIntPtr, dwInstance: UIntPtr, fdwOpen: win32more.Windows.Win32.Media.Audio.MIDI_WAVE_OPEN_TYPE) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInClose(hmi: win32more.Windows.Win32.Media.Audio.HMIDIIN) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInPrepareHeader(hmi: win32more.Windows.Win32.Media.Audio.HMIDIIN, pmh: POINTER(win32more.Windows.Win32.Media.Audio.MIDIHDR), cbmh: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInUnprepareHeader(hmi: win32more.Windows.Win32.Media.Audio.HMIDIIN, pmh: POINTER(win32more.Windows.Win32.Media.Audio.MIDIHDR), cbmh: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInAddBuffer(hmi: win32more.Windows.Win32.Media.Audio.HMIDIIN, pmh: POINTER(win32more.Windows.Win32.Media.Audio.MIDIHDR), cbmh: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInStart(hmi: win32more.Windows.Win32.Media.Audio.HMIDIIN) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInStop(hmi: win32more.Windows.Win32.Media.Audio.HMIDIIN) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInReset(hmi: win32more.Windows.Win32.Media.Audio.HMIDIIN) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInGetID(hmi: win32more.Windows.Win32.Media.Audio.HMIDIIN, puDeviceID: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInMessage(hmi: win32more.Windows.Win32.Media.Audio.HMIDIIN, uMsg: UInt32, dw1: UIntPtr, dw2: UIntPtr) -> UInt32: ...
@winfunctype('WINMM.dll')
def auxGetNumDevs() -> UInt32: ...
@winfunctype('WINMM.dll')
def auxGetDevCapsA(uDeviceID: UIntPtr, pac: POINTER(win32more.Windows.Win32.Media.Audio.AUXCAPSA), cbac: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def auxGetDevCapsW(uDeviceID: UIntPtr, pac: POINTER(win32more.Windows.Win32.Media.Audio.AUXCAPSW), cbac: UInt32) -> UInt32: ...
auxGetDevCaps = UnicodeAlias('auxGetDevCapsW')
@winfunctype('WINMM.dll')
def auxSetVolume(uDeviceID: UInt32, dwVolume: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def auxGetVolume(uDeviceID: UInt32, pdwVolume: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WINMM.dll')
def auxOutMessage(uDeviceID: UInt32, uMsg: UInt32, dw1: UIntPtr, dw2: UIntPtr) -> UInt32: ...
@winfunctype('WINMM.dll')
def mixerGetNumDevs() -> UInt32: ...
@winfunctype('WINMM.dll')
def mixerGetDevCapsA(uMxId: UIntPtr, pmxcaps: POINTER(win32more.Windows.Win32.Media.Audio.MIXERCAPSA), cbmxcaps: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def mixerGetDevCapsW(uMxId: UIntPtr, pmxcaps: POINTER(win32more.Windows.Win32.Media.Audio.MIXERCAPSW), cbmxcaps: UInt32) -> UInt32: ...
mixerGetDevCaps = UnicodeAlias('mixerGetDevCapsW')
@winfunctype('WINMM.dll')
def mixerOpen(phmx: POINTER(win32more.Windows.Win32.Media.Audio.HMIXER), uMxId: UInt32, dwCallback: UIntPtr, dwInstance: UIntPtr, fdwOpen: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def mixerClose(hmx: win32more.Windows.Win32.Media.Audio.HMIXER) -> UInt32: ...
@winfunctype('WINMM.dll')
def mixerMessage(hmx: win32more.Windows.Win32.Media.Audio.HMIXER, uMsg: UInt32, dwParam1: UIntPtr, dwParam2: UIntPtr) -> UInt32: ...
@winfunctype('WINMM.dll')
def mixerGetLineInfoA(hmxobj: win32more.Windows.Win32.Media.Audio.HMIXEROBJ, pmxl: POINTER(win32more.Windows.Win32.Media.Audio.MIXERLINEA), fdwInfo: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def mixerGetLineInfoW(hmxobj: win32more.Windows.Win32.Media.Audio.HMIXEROBJ, pmxl: POINTER(win32more.Windows.Win32.Media.Audio.MIXERLINEW), fdwInfo: UInt32) -> UInt32: ...
mixerGetLineInfo = UnicodeAlias('mixerGetLineInfoW')
@winfunctype('WINMM.dll')
def mixerGetID(hmxobj: win32more.Windows.Win32.Media.Audio.HMIXEROBJ, puMxId: POINTER(UInt32), fdwId: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def mixerGetLineControlsA(hmxobj: win32more.Windows.Win32.Media.Audio.HMIXEROBJ, pmxlc: POINTER(win32more.Windows.Win32.Media.Audio.MIXERLINECONTROLSA), fdwControls: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def mixerGetLineControlsW(hmxobj: win32more.Windows.Win32.Media.Audio.HMIXEROBJ, pmxlc: POINTER(win32more.Windows.Win32.Media.Audio.MIXERLINECONTROLSW), fdwControls: UInt32) -> UInt32: ...
mixerGetLineControls = UnicodeAlias('mixerGetLineControlsW')
@winfunctype('WINMM.dll')
def mixerGetControlDetailsA(hmxobj: win32more.Windows.Win32.Media.Audio.HMIXEROBJ, pmxcd: POINTER(win32more.Windows.Win32.Media.Audio.MIXERCONTROLDETAILS), fdwDetails: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def mixerGetControlDetailsW(hmxobj: win32more.Windows.Win32.Media.Audio.HMIXEROBJ, pmxcd: POINTER(win32more.Windows.Win32.Media.Audio.MIXERCONTROLDETAILS), fdwDetails: UInt32) -> UInt32: ...
mixerGetControlDetails = UnicodeAlias('mixerGetControlDetailsW')
@winfunctype('WINMM.dll')
def mixerSetControlDetails(hmxobj: win32more.Windows.Win32.Media.Audio.HMIXEROBJ, pmxcd: POINTER(win32more.Windows.Win32.Media.Audio.MIXERCONTROLDETAILS), fdwDetails: UInt32) -> UInt32: ...
@winfunctype('MMDevAPI.dll')
def ActivateAudioInterfaceAsync(deviceInterfacePath: win32more.Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), activationParams: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), completionHandler: win32more.Windows.Win32.Media.Audio.IActivateAudioInterfaceCompletionHandler, activationOperation: POINTER(win32more.Windows.Win32.Media.Audio.IActivateAudioInterfaceAsyncOperation)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Windows.Media.MediaControl.dll')
def CreateRenderAudioStateMonitor(audioStateMonitor: POINTER(win32more.Windows.Win32.Media.Audio.IAudioStateMonitor)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Windows.Media.MediaControl.dll')
def CreateRenderAudioStateMonitorForCategory(category: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY, audioStateMonitor: POINTER(win32more.Windows.Win32.Media.Audio.IAudioStateMonitor)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Windows.Media.MediaControl.dll')
def CreateRenderAudioStateMonitorForCategoryAndDeviceRole(category: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY, role: win32more.Windows.Win32.Media.Audio.ERole, audioStateMonitor: POINTER(win32more.Windows.Win32.Media.Audio.IAudioStateMonitor)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Windows.Media.MediaControl.dll')
def CreateRenderAudioStateMonitorForCategoryAndDeviceId(category: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY, deviceId: win32more.Windows.Win32.Foundation.PWSTR, audioStateMonitor: POINTER(win32more.Windows.Win32.Media.Audio.IAudioStateMonitor)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Windows.Media.MediaControl.dll')
def CreateCaptureAudioStateMonitor(audioStateMonitor: POINTER(win32more.Windows.Win32.Media.Audio.IAudioStateMonitor)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Windows.Media.MediaControl.dll')
def CreateCaptureAudioStateMonitorForCategory(category: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY, audioStateMonitor: POINTER(win32more.Windows.Win32.Media.Audio.IAudioStateMonitor)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Windows.Media.MediaControl.dll')
def CreateCaptureAudioStateMonitorForCategoryAndDeviceRole(category: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY, role: win32more.Windows.Win32.Media.Audio.ERole, audioStateMonitor: POINTER(win32more.Windows.Win32.Media.Audio.IAudioStateMonitor)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Windows.Media.MediaControl.dll')
def CreateCaptureAudioStateMonitorForCategoryAndDeviceId(category: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY, deviceId: win32more.Windows.Win32.Foundation.PWSTR, audioStateMonitor: POINTER(win32more.Windows.Win32.Media.Audio.IAudioStateMonitor)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSACM32.dll')
def acmGetVersion() -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmMetrics(hao: win32more.Windows.Win32.Media.Audio.HACMOBJ, uMetric: UInt32, pMetric: VoidPtr) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmDriverEnum(fnCallback: win32more.Windows.Win32.Media.Audio.ACMDRIVERENUMCB, dwInstance: UIntPtr, fdwEnum: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmDriverID(hao: win32more.Windows.Win32.Media.Audio.HACMOBJ, phadid: POINTER(win32more.Windows.Win32.Media.Audio.HACMDRIVERID), fdwDriverID: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmDriverAddA(phadid: POINTER(win32more.Windows.Win32.Media.Audio.HACMDRIVERID), hinstModule: win32more.Windows.Win32.Foundation.HINSTANCE, lParam: win32more.Windows.Win32.Foundation.LPARAM, dwPriority: UInt32, fdwAdd: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmDriverAddW(phadid: POINTER(win32more.Windows.Win32.Media.Audio.HACMDRIVERID), hinstModule: win32more.Windows.Win32.Foundation.HINSTANCE, lParam: win32more.Windows.Win32.Foundation.LPARAM, dwPriority: UInt32, fdwAdd: UInt32) -> UInt32: ...
acmDriverAdd = UnicodeAlias('acmDriverAddW')
@winfunctype('MSACM32.dll')
def acmDriverRemove(hadid: win32more.Windows.Win32.Media.Audio.HACMDRIVERID, fdwRemove: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmDriverOpen(phad: POINTER(win32more.Windows.Win32.Media.Audio.HACMDRIVER), hadid: win32more.Windows.Win32.Media.Audio.HACMDRIVERID, fdwOpen: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmDriverClose(had: win32more.Windows.Win32.Media.Audio.HACMDRIVER, fdwClose: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmDriverMessage(had: win32more.Windows.Win32.Media.Audio.HACMDRIVER, uMsg: UInt32, lParam1: win32more.Windows.Win32.Foundation.LPARAM, lParam2: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.LRESULT: ...
@winfunctype('MSACM32.dll')
def acmDriverPriority(hadid: win32more.Windows.Win32.Media.Audio.HACMDRIVERID, dwPriority: UInt32, fdwPriority: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmDriverDetailsA(hadid: win32more.Windows.Win32.Media.Audio.HACMDRIVERID, padd: POINTER(win32more.Windows.Win32.Media.Audio.ACMDRIVERDETAILSA), fdwDetails: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmDriverDetailsW(hadid: win32more.Windows.Win32.Media.Audio.HACMDRIVERID, padd: POINTER(win32more.Windows.Win32.Media.Audio.ACMDRIVERDETAILSW), fdwDetails: UInt32) -> UInt32: ...
acmDriverDetails = UnicodeAlias('acmDriverDetailsW')
@winfunctype('MSACM32.dll')
def acmFormatTagDetailsA(had: win32more.Windows.Win32.Media.Audio.HACMDRIVER, paftd: POINTER(win32more.Windows.Win32.Media.Audio.ACMFORMATTAGDETAILSA), fdwDetails: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFormatTagDetailsW(had: win32more.Windows.Win32.Media.Audio.HACMDRIVER, paftd: POINTER(win32more.Windows.Win32.Media.Audio.ACMFORMATTAGDETAILSW), fdwDetails: UInt32) -> UInt32: ...
acmFormatTagDetails = UnicodeAlias('acmFormatTagDetailsW')
@winfunctype('MSACM32.dll')
def acmFormatTagEnumA(had: win32more.Windows.Win32.Media.Audio.HACMDRIVER, paftd: POINTER(win32more.Windows.Win32.Media.Audio.ACMFORMATTAGDETAILSA), fnCallback: win32more.Windows.Win32.Media.Audio.ACMFORMATTAGENUMCBA, dwInstance: UIntPtr, fdwEnum: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFormatTagEnumW(had: win32more.Windows.Win32.Media.Audio.HACMDRIVER, paftd: POINTER(win32more.Windows.Win32.Media.Audio.ACMFORMATTAGDETAILSW), fnCallback: win32more.Windows.Win32.Media.Audio.ACMFORMATTAGENUMCBW, dwInstance: UIntPtr, fdwEnum: UInt32) -> UInt32: ...
acmFormatTagEnum = UnicodeAlias('acmFormatTagEnumW')
@winfunctype('MSACM32.dll')
def acmFormatDetailsA(had: win32more.Windows.Win32.Media.Audio.HACMDRIVER, pafd: POINTER(win32more.Windows.Win32.Media.Audio.ACMFORMATDETAILSA), fdwDetails: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFormatDetailsW(had: win32more.Windows.Win32.Media.Audio.HACMDRIVER, pafd: POINTER(win32more.Windows.Win32.Media.Audio.tACMFORMATDETAILSW), fdwDetails: UInt32) -> UInt32: ...
acmFormatDetails = UnicodeAlias('acmFormatDetailsW')
@winfunctype('MSACM32.dll')
def acmFormatEnumA(had: win32more.Windows.Win32.Media.Audio.HACMDRIVER, pafd: POINTER(win32more.Windows.Win32.Media.Audio.ACMFORMATDETAILSA), fnCallback: win32more.Windows.Win32.Media.Audio.ACMFORMATENUMCBA, dwInstance: UIntPtr, fdwEnum: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFormatEnumW(had: win32more.Windows.Win32.Media.Audio.HACMDRIVER, pafd: POINTER(win32more.Windows.Win32.Media.Audio.tACMFORMATDETAILSW), fnCallback: win32more.Windows.Win32.Media.Audio.ACMFORMATENUMCBW, dwInstance: UIntPtr, fdwEnum: UInt32) -> UInt32: ...
acmFormatEnum = UnicodeAlias('acmFormatEnumW')
@winfunctype('MSACM32.dll')
def acmFormatSuggest(had: win32more.Windows.Win32.Media.Audio.HACMDRIVER, pwfxSrc: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), pwfxDst: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), cbwfxDst: UInt32, fdwSuggest: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFormatChooseA(pafmtc: POINTER(win32more.Windows.Win32.Media.Audio.ACMFORMATCHOOSEA)) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFormatChooseW(pafmtc: POINTER(win32more.Windows.Win32.Media.Audio.ACMFORMATCHOOSEW)) -> UInt32: ...
acmFormatChoose = UnicodeAlias('acmFormatChooseW')
@winfunctype('MSACM32.dll')
def acmFilterTagDetailsA(had: win32more.Windows.Win32.Media.Audio.HACMDRIVER, paftd: POINTER(win32more.Windows.Win32.Media.Audio.ACMFILTERTAGDETAILSA), fdwDetails: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFilterTagDetailsW(had: win32more.Windows.Win32.Media.Audio.HACMDRIVER, paftd: POINTER(win32more.Windows.Win32.Media.Audio.ACMFILTERTAGDETAILSW), fdwDetails: UInt32) -> UInt32: ...
acmFilterTagDetails = UnicodeAlias('acmFilterTagDetailsW')
@winfunctype('MSACM32.dll')
def acmFilterTagEnumA(had: win32more.Windows.Win32.Media.Audio.HACMDRIVER, paftd: POINTER(win32more.Windows.Win32.Media.Audio.ACMFILTERTAGDETAILSA), fnCallback: win32more.Windows.Win32.Media.Audio.ACMFILTERTAGENUMCBA, dwInstance: UIntPtr, fdwEnum: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFilterTagEnumW(had: win32more.Windows.Win32.Media.Audio.HACMDRIVER, paftd: POINTER(win32more.Windows.Win32.Media.Audio.ACMFILTERTAGDETAILSW), fnCallback: win32more.Windows.Win32.Media.Audio.ACMFILTERTAGENUMCBW, dwInstance: UIntPtr, fdwEnum: UInt32) -> UInt32: ...
acmFilterTagEnum = UnicodeAlias('acmFilterTagEnumW')
@winfunctype('MSACM32.dll')
def acmFilterDetailsA(had: win32more.Windows.Win32.Media.Audio.HACMDRIVER, pafd: POINTER(win32more.Windows.Win32.Media.Audio.ACMFILTERDETAILSA), fdwDetails: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFilterDetailsW(had: win32more.Windows.Win32.Media.Audio.HACMDRIVER, pafd: POINTER(win32more.Windows.Win32.Media.Audio.ACMFILTERDETAILSW), fdwDetails: UInt32) -> UInt32: ...
acmFilterDetails = UnicodeAlias('acmFilterDetailsW')
@winfunctype('MSACM32.dll')
def acmFilterEnumA(had: win32more.Windows.Win32.Media.Audio.HACMDRIVER, pafd: POINTER(win32more.Windows.Win32.Media.Audio.ACMFILTERDETAILSA), fnCallback: win32more.Windows.Win32.Media.Audio.ACMFILTERENUMCBA, dwInstance: UIntPtr, fdwEnum: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFilterEnumW(had: win32more.Windows.Win32.Media.Audio.HACMDRIVER, pafd: POINTER(win32more.Windows.Win32.Media.Audio.ACMFILTERDETAILSW), fnCallback: win32more.Windows.Win32.Media.Audio.ACMFILTERENUMCBW, dwInstance: UIntPtr, fdwEnum: UInt32) -> UInt32: ...
acmFilterEnum = UnicodeAlias('acmFilterEnumW')
@winfunctype('MSACM32.dll')
def acmFilterChooseA(pafltrc: POINTER(win32more.Windows.Win32.Media.Audio.ACMFILTERCHOOSEA)) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFilterChooseW(pafltrc: POINTER(win32more.Windows.Win32.Media.Audio.ACMFILTERCHOOSEW)) -> UInt32: ...
acmFilterChoose = UnicodeAlias('acmFilterChooseW')
@winfunctype('MSACM32.dll')
def acmStreamOpen(phas: POINTER(win32more.Windows.Win32.Media.Audio.HACMSTREAM), had: win32more.Windows.Win32.Media.Audio.HACMDRIVER, pwfxSrc: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), pwfxDst: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), pwfltr: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFILTER), dwCallback: UIntPtr, dwInstance: UIntPtr, fdwOpen: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmStreamClose(has: win32more.Windows.Win32.Media.Audio.HACMSTREAM, fdwClose: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmStreamSize(has: win32more.Windows.Win32.Media.Audio.HACMSTREAM, cbInput: UInt32, pdwOutputBytes: POINTER(UInt32), fdwSize: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmStreamReset(has: win32more.Windows.Win32.Media.Audio.HACMSTREAM, fdwReset: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmStreamMessage(has: win32more.Windows.Win32.Media.Audio.HACMSTREAM, uMsg: UInt32, lParam1: win32more.Windows.Win32.Foundation.LPARAM, lParam2: win32more.Windows.Win32.Foundation.LPARAM) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmStreamConvert(has: win32more.Windows.Win32.Media.Audio.HACMSTREAM, pash: POINTER(win32more.Windows.Win32.Media.Audio.ACMSTREAMHEADER), fdwConvert: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmStreamPrepareHeader(has: win32more.Windows.Win32.Media.Audio.HACMSTREAM, pash: POINTER(win32more.Windows.Win32.Media.Audio.ACMSTREAMHEADER), fdwPrepare: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmStreamUnprepareHeader(has: win32more.Windows.Win32.Media.Audio.HACMSTREAM, pash: POINTER(win32more.Windows.Win32.Media.Audio.ACMSTREAMHEADER), fdwUnprepare: UInt32) -> UInt32: ...
class AudioClient3ActivationParams(Structure):
    tracingContextId: Guid
class AudioClientProperties(Structure):
    cbSize: UInt32
    bIsOffload: win32more.Windows.Win32.Foundation.BOOL
    eCategory: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY
    Options: win32more.Windows.Win32.Media.Audio.AUDCLNT_STREAMOPTIONS
class AudioExtensionParams(Structure):
    AddPageParam: win32more.Windows.Win32.Foundation.LPARAM
    pEndpoint: win32more.Windows.Win32.Media.Audio.IMMDevice
    pPnpInterface: win32more.Windows.Win32.Media.Audio.IMMDevice
    pPnpDevnode: win32more.Windows.Win32.Media.Audio.IMMDevice
AudioObjectType = Int32
AudioObjectType_None: win32more.Windows.Win32.Media.Audio.AudioObjectType = 0
AudioObjectType_Dynamic: win32more.Windows.Win32.Media.Audio.AudioObjectType = 1
AudioObjectType_FrontLeft: win32more.Windows.Win32.Media.Audio.AudioObjectType = 2
AudioObjectType_FrontRight: win32more.Windows.Win32.Media.Audio.AudioObjectType = 4
AudioObjectType_FrontCenter: win32more.Windows.Win32.Media.Audio.AudioObjectType = 8
AudioObjectType_LowFrequency: win32more.Windows.Win32.Media.Audio.AudioObjectType = 16
AudioObjectType_SideLeft: win32more.Windows.Win32.Media.Audio.AudioObjectType = 32
AudioObjectType_SideRight: win32more.Windows.Win32.Media.Audio.AudioObjectType = 64
AudioObjectType_BackLeft: win32more.Windows.Win32.Media.Audio.AudioObjectType = 128
AudioObjectType_BackRight: win32more.Windows.Win32.Media.Audio.AudioObjectType = 256
AudioObjectType_TopFrontLeft: win32more.Windows.Win32.Media.Audio.AudioObjectType = 512
AudioObjectType_TopFrontRight: win32more.Windows.Win32.Media.Audio.AudioObjectType = 1024
AudioObjectType_TopBackLeft: win32more.Windows.Win32.Media.Audio.AudioObjectType = 2048
AudioObjectType_TopBackRight: win32more.Windows.Win32.Media.Audio.AudioObjectType = 4096
AudioObjectType_BottomFrontLeft: win32more.Windows.Win32.Media.Audio.AudioObjectType = 8192
AudioObjectType_BottomFrontRight: win32more.Windows.Win32.Media.Audio.AudioObjectType = 16384
AudioObjectType_BottomBackLeft: win32more.Windows.Win32.Media.Audio.AudioObjectType = 32768
AudioObjectType_BottomBackRight: win32more.Windows.Win32.Media.Audio.AudioObjectType = 65536
AudioObjectType_BackCenter: win32more.Windows.Win32.Media.Audio.AudioObjectType = 131072
AudioSessionDisconnectReason = Int32
DisconnectReasonDeviceRemoval: win32more.Windows.Win32.Media.Audio.AudioSessionDisconnectReason = 0
DisconnectReasonServerShutdown: win32more.Windows.Win32.Media.Audio.AudioSessionDisconnectReason = 1
DisconnectReasonFormatChanged: win32more.Windows.Win32.Media.Audio.AudioSessionDisconnectReason = 2
DisconnectReasonSessionLogoff: win32more.Windows.Win32.Media.Audio.AudioSessionDisconnectReason = 3
DisconnectReasonSessionDisconnected: win32more.Windows.Win32.Media.Audio.AudioSessionDisconnectReason = 4
DisconnectReasonExclusiveModeOverride: win32more.Windows.Win32.Media.Audio.AudioSessionDisconnectReason = 5
AudioSessionState = Int32
AudioSessionStateInactive: win32more.Windows.Win32.Media.Audio.AudioSessionState = 0
AudioSessionStateActive: win32more.Windows.Win32.Media.Audio.AudioSessionState = 1
AudioSessionStateExpired: win32more.Windows.Win32.Media.Audio.AudioSessionState = 2
AudioStateMonitorSoundLevel = Int32
Muted: win32more.Windows.Win32.Media.Audio.AudioStateMonitorSoundLevel = 0
Low: win32more.Windows.Win32.Media.Audio.AudioStateMonitorSoundLevel = 1
Full: win32more.Windows.Win32.Media.Audio.AudioStateMonitorSoundLevel = 2
class ConnectorType(Enum, Int32):
    Unknown_Connector = 0
    Physical_Internal = 1
    Physical_External = 2
    Software_IO = 3
    Software_Fixed = 4
    Network = 5
DEVICE_STATE = UInt32
DEVICE_STATE_ACTIVE: win32more.Windows.Win32.Media.Audio.DEVICE_STATE = 1
DEVICE_STATE_DISABLED: win32more.Windows.Win32.Media.Audio.DEVICE_STATE = 2
DEVICE_STATE_NOTPRESENT: win32more.Windows.Win32.Media.Audio.DEVICE_STATE = 4
DEVICE_STATE_UNPLUGGED: win32more.Windows.Win32.Media.Audio.DEVICE_STATE = 8
class DIRECTX_AUDIO_ACTIVATION_PARAMS(Structure):
    cbDirectXAudioActivationParams: UInt32
    guidAudioSession: Guid
    dwAudioStreamFlags: UInt32
DataFlow = Int32
In: win32more.Windows.Win32.Media.Audio.DataFlow = 0
Out: win32more.Windows.Win32.Media.Audio.DataFlow = 1
DeviceTopology = Guid('{1df639d0-5ec1-47aa-9379-828dc1aa8c59}')
class ECHOWAVEFILTER(Structure):
    wfltr: win32more.Windows.Win32.Media.Audio.WAVEFILTER
    dwVolume: UInt32
    dwDelay: UInt32
    _pack_ = 1
EDataFlow = Int32
eRender: win32more.Windows.Win32.Media.Audio.EDataFlow = 0
eCapture: win32more.Windows.Win32.Media.Audio.EDataFlow = 1
eAll: win32more.Windows.Win32.Media.Audio.EDataFlow = 2
EDataFlow_enum_count: win32more.Windows.Win32.Media.Audio.EDataFlow = 3
ERole = Int32
eConsole: win32more.Windows.Win32.Media.Audio.ERole = 0
eMultimedia: win32more.Windows.Win32.Media.Audio.ERole = 1
eCommunications: win32more.Windows.Win32.Media.Audio.ERole = 2
ERole_enum_count: win32more.Windows.Win32.Media.Audio.ERole = 3
EndpointFormFactor = Int32
RemoteNetworkDevice: win32more.Windows.Win32.Media.Audio.EndpointFormFactor = 0
Speakers: win32more.Windows.Win32.Media.Audio.EndpointFormFactor = 1
LineLevel: win32more.Windows.Win32.Media.Audio.EndpointFormFactor = 2
Headphones: win32more.Windows.Win32.Media.Audio.EndpointFormFactor = 3
Microphone: win32more.Windows.Win32.Media.Audio.EndpointFormFactor = 4
Headset: win32more.Windows.Win32.Media.Audio.EndpointFormFactor = 5
Handset: win32more.Windows.Win32.Media.Audio.EndpointFormFactor = 6
UnknownDigitalPassthrough: win32more.Windows.Win32.Media.Audio.EndpointFormFactor = 7
SPDIF: win32more.Windows.Win32.Media.Audio.EndpointFormFactor = 8
DigitalAudioDisplayDevice: win32more.Windows.Win32.Media.Audio.EndpointFormFactor = 9
UnknownFormFactor: win32more.Windows.Win32.Media.Audio.EndpointFormFactor = 10
EndpointFormFactor_enum_count: win32more.Windows.Win32.Media.Audio.EndpointFormFactor = 11
HACMDRIVER = VoidPtr
HACMDRIVERID = VoidPtr
HACMOBJ = VoidPtr
HACMSTREAM = VoidPtr
HMIDI = VoidPtr
HMIDIIN = VoidPtr
HMIDIOUT = VoidPtr
HMIDISTRM = VoidPtr
HMIXER = VoidPtr
HMIXEROBJ = VoidPtr
HWAVE = VoidPtr
HWAVEIN = VoidPtr
HWAVEOUT = VoidPtr
class IAcousticEchoCancellationControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f4ae25b5-aaa3-437d-b6b3-dbbe2d0e9549}')
    @commethod(3)
    def SetEchoCancellationRenderEndpoint(self, endpointId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActivateAudioInterfaceAsyncOperation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{72a22d78-cde4-431d-b8cc-843a71199b6d}')
    @commethod(3)
    def GetActivateResult(self, activateResult: POINTER(win32more.Windows.Win32.Foundation.HRESULT), activatedInterface: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActivateAudioInterfaceCompletionHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{41d949ab-9862-444a-80f6-c261334da5eb}')
    @commethod(3)
    def ActivateCompleted(self, activateOperation: win32more.Windows.Win32.Media.Audio.IActivateAudioInterfaceAsyncOperation) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioAmbisonicsControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{28724c91-df35-4856-9f76-d6a26413f3df}')
    @commethod(3)
    def SetData(self, pAmbisonicsParams: POINTER(win32more.Windows.Win32.Media.Audio.AMBISONICS_PARAMS), cbAmbisonicsParams: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetHeadTracking(self, bEnableHeadTracking: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetHeadTracking(self, pbEnableHeadTracking: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetRotation(self, X: Single, Y: Single, Z: Single, W: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioAutoGainControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{85401fd4-6de4-4b9d-9869-2d6753a82f3c}')
    @commethod(3)
    def GetEnabled(self, pbEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetEnabled(self, bEnable: win32more.Windows.Win32.Foundation.BOOL, pguidEventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioBass(ComPtr):
    extends: win32more.Windows.Win32.Media.Audio.IPerChannelDbLevel
    _iid_ = Guid('{a2b1a1d9-4db3-425d-a2b2-bd335cb3e2e5}')
class IAudioCaptureClient(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c8adbd64-e71e-48a0-a4de-185c395cd317}')
    @commethod(3)
    def GetBuffer(self, ppData: POINTER(POINTER(Byte)), pNumFramesToRead: POINTER(UInt32), pdwFlags: POINTER(UInt32), pu64DevicePosition: POINTER(UInt64), pu64QPCPosition: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReleaseBuffer(self, NumFramesRead: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNextPacketSize(self, pNumFramesInNextPacket: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioChannelConfig(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bb11c46f-ec28-493c-b88a-5db88062ce98}')
    @commethod(3)
    def SetChannelConfig(self, dwConfig: UInt32, pguidEventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetChannelConfig(self, pdwConfig: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioClient(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1cb9ad4c-dbfa-4c32-b178-c2f568a703b2}')
    @commethod(3)
    def Initialize(self, ShareMode: win32more.Windows.Win32.Media.Audio.AUDCLNT_SHAREMODE, StreamFlags: UInt32, hnsBufferDuration: Int64, hnsPeriodicity: Int64, pFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), AudioSessionGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetBufferSize(self, pNumBufferFrames: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStreamLatency(self, phnsLatency: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCurrentPadding(self, pNumPaddingFrames: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsFormatSupported(self, ShareMode: win32more.Windows.Win32.Media.Audio.AUDCLNT_SHAREMODE, pFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), ppClosestMatch: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetMixFormat(self, ppDeviceFormat: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDevicePeriod(self, phnsDefaultDevicePeriod: POINTER(Int64), phnsMinimumDevicePeriod: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Start(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Stop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetEventHandle(self, eventHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetService(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioClient2(ComPtr):
    extends: win32more.Windows.Win32.Media.Audio.IAudioClient
    _iid_ = Guid('{726778cd-f60a-4eda-82de-e47610cd78aa}')
    @commethod(15)
    def IsOffloadCapable(self, Category: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY, pbOffloadCapable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetClientProperties(self, pProperties: POINTER(win32more.Windows.Win32.Media.Audio.AudioClientProperties)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetBufferSizeLimits(self, pFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), bEventDriven: win32more.Windows.Win32.Foundation.BOOL, phnsMinBufferDuration: POINTER(Int64), phnsMaxBufferDuration: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioClient3(ComPtr):
    extends: win32more.Windows.Win32.Media.Audio.IAudioClient2
    _iid_ = Guid('{7ed4ee07-8e67-4cd4-8c1a-2b7a5987ad42}')
    @commethod(18)
    def GetSharedModeEnginePeriod(self, pFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), pDefaultPeriodInFrames: POINTER(UInt32), pFundamentalPeriodInFrames: POINTER(UInt32), pMinPeriodInFrames: POINTER(UInt32), pMaxPeriodInFrames: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetCurrentSharedModeEnginePeriod(self, ppFormat: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)), pCurrentPeriodInFrames: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def InitializeSharedAudioStream(self, StreamFlags: UInt32, PeriodInFrames: UInt32, pFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), AudioSessionGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioClientDuckingControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c789d381-a28c-4168-b28f-d3a837924dc3}')
    @commethod(3)
    def SetDuckingOptionsForCurrentStream(self, options: win32more.Windows.Win32.Media.Audio.AUDIO_DUCKING_OPTIONS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioClock(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cd63314f-3fba-4a1b-812c-ef96358728e7}')
    @commethod(3)
    def GetFrequency(self, pu64Frequency: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPosition(self, pu64Position: POINTER(UInt64), pu64QPCPosition: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCharacteristics(self, pdwCharacteristics: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioClock2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6f49ff73-6727-49ac-a008-d98cf5e70048}')
    @commethod(3)
    def GetDevicePosition(self, DevicePosition: POINTER(UInt64), QPCPosition: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioClockAdjustment(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f6e4c0a0-46d9-4fb8-be21-57a3ef2b626c}')
    @commethod(3)
    def SetSampleRate(self, flSampleRate: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioEffectsChangedNotificationClient(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a5ded44f-3c5d-4b2b-bd1e-5dc1ee20bbf6}')
    @commethod(3)
    def OnAudioEffectsChanged(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioEffectsManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4460b3ae-4b44-4527-8676-7548a8acd260}')
    @commethod(3)
    def RegisterAudioEffectsChangedNotificationCallback(self, client: win32more.Windows.Win32.Media.Audio.IAudioEffectsChangedNotificationClient) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterAudioEffectsChangedNotificationCallback(self, client: win32more.Windows.Win32.Media.Audio.IAudioEffectsChangedNotificationClient) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAudioEffects(self, effects: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.AUDIO_EFFECT)), numEffects: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetAudioEffectState(self, effectId: Guid, state: win32more.Windows.Win32.Media.Audio.AUDIO_EFFECT_STATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioFormatEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcdaa858-895a-4a22-a5eb-67bda506096d}')
    @commethod(3)
    def GetCount(self, count: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFormat(self, index: UInt32, format: POINTER(POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioInputSelector(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4f03dc02-5e6e-4653-8f72-a030c123d598}')
    @commethod(3)
    def GetSelection(self, pnIdSelected: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSelection(self, nIdSelect: UInt32, pguidEventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioLoudness(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7d8b1437-dd53-4350-9c1b-1ee2890bd938}')
    @commethod(3)
    def GetEnabled(self, pbEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetEnabled(self, bEnable: win32more.Windows.Win32.Foundation.BOOL, pguidEventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioMidrange(ComPtr):
    extends: win32more.Windows.Win32.Media.Audio.IPerChannelDbLevel
    _iid_ = Guid('{5e54b6d7-b44b-40d9-9a9e-e691d9ce6edf}')
class IAudioMute(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{df45aeea-b74a-4b6b-afad-2366b6aa012e}')
    @commethod(3)
    def SetMute(self, bMuted: win32more.Windows.Win32.Foundation.BOOL, pguidEventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMute(self, pbMuted: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioOutputSelector(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bb515f69-94a7-429e-8b9c-271b3f11a3ab}')
    @commethod(3)
    def GetSelection(self, pnIdSelected: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSelection(self, nIdSelect: UInt32, pguidEventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioPeakMeter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dd79923c-0599-45e0-b8b6-c8df7db6e796}')
    @commethod(3)
    def GetChannelCount(self, pcChannels: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLevel(self, nChannel: UInt32, pfLevel: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioRenderClient(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f294acfc-3146-4483-a7bf-addca7c260e2}')
    @commethod(3)
    def GetBuffer(self, NumFramesRequested: UInt32, ppData: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReleaseBuffer(self, NumFramesWritten: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioSessionControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f4b1a599-7266-4319-a8ca-e70acb11e8cd}')
    @commethod(3)
    def GetState(self, pRetVal: POINTER(win32more.Windows.Win32.Media.Audio.AudioSessionState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDisplayName(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDisplayName(self, Value: win32more.Windows.Win32.Foundation.PWSTR, EventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetIconPath(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetIconPath(self, Value: win32more.Windows.Win32.Foundation.PWSTR, EventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetGroupingParam(self, pRetVal: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetGroupingParam(self, Override: POINTER(Guid), EventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RegisterAudioSessionNotification(self, NewNotifications: win32more.Windows.Win32.Media.Audio.IAudioSessionEvents) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def UnregisterAudioSessionNotification(self, NewNotifications: win32more.Windows.Win32.Media.Audio.IAudioSessionEvents) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioSessionControl2(ComPtr):
    extends: win32more.Windows.Win32.Media.Audio.IAudioSessionControl
    _iid_ = Guid('{bfb7ff88-7239-4fc9-8fa2-07c950be9c6d}')
    @commethod(12)
    def GetSessionIdentifier(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetSessionInstanceIdentifier(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetProcessId(self, pRetVal: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def IsSystemSoundsSession(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetDuckingPreference(self, optOut: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioSessionEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e2f5bb11-0570-40ca-acdd-3aa01277dee8}')
    @commethod(3)
    def GetCount(self, SessionCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSession(self, SessionCount: Int32, Session: POINTER(win32more.Windows.Win32.Media.Audio.IAudioSessionControl)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioSessionEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{24918acc-64b3-37c1-8ca9-74a66e9957a8}')
    @commethod(3)
    def OnDisplayNameChanged(self, NewDisplayName: win32more.Windows.Win32.Foundation.PWSTR, EventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnIconPathChanged(self, NewIconPath: win32more.Windows.Win32.Foundation.PWSTR, EventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnSimpleVolumeChanged(self, NewVolume: Single, NewMute: win32more.Windows.Win32.Foundation.BOOL, EventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnChannelVolumeChanged(self, ChannelCount: UInt32, NewChannelVolumeArray: POINTER(Single), ChangedChannel: UInt32, EventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnGroupingParamChanged(self, NewGroupingParam: POINTER(Guid), EventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnStateChanged(self, NewState: win32more.Windows.Win32.Media.Audio.AudioSessionState) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnSessionDisconnected(self, DisconnectReason: win32more.Windows.Win32.Media.Audio.AudioSessionDisconnectReason) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioSessionManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bfa971f1-4d5e-40bb-935e-967039bfbee4}')
    @commethod(3)
    def GetAudioSessionControl(self, AudioSessionGuid: POINTER(Guid), StreamFlags: UInt32, SessionControl: POINTER(win32more.Windows.Win32.Media.Audio.IAudioSessionControl)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSimpleAudioVolume(self, AudioSessionGuid: POINTER(Guid), StreamFlags: UInt32, AudioVolume: POINTER(win32more.Windows.Win32.Media.Audio.ISimpleAudioVolume)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioSessionManager2(ComPtr):
    extends: win32more.Windows.Win32.Media.Audio.IAudioSessionManager
    _iid_ = Guid('{77aa99a0-1bd6-484f-8bc7-2c654c9a9b6f}')
    @commethod(5)
    def GetSessionEnumerator(self, SessionEnum: POINTER(win32more.Windows.Win32.Media.Audio.IAudioSessionEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RegisterSessionNotification(self, SessionNotification: win32more.Windows.Win32.Media.Audio.IAudioSessionNotification) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UnregisterSessionNotification(self, SessionNotification: win32more.Windows.Win32.Media.Audio.IAudioSessionNotification) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RegisterDuckNotification(self, sessionID: win32more.Windows.Win32.Foundation.PWSTR, duckNotification: win32more.Windows.Win32.Media.Audio.IAudioVolumeDuckNotification) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def UnregisterDuckNotification(self, duckNotification: win32more.Windows.Win32.Media.Audio.IAudioVolumeDuckNotification) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioSessionNotification(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{641dd20b-4d41-49cc-aba3-174b9477bb08}')
    @commethod(3)
    def OnSessionCreated(self, NewSession: win32more.Windows.Win32.Media.Audio.IAudioSessionControl) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioStateMonitor(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{63bd8738-e30d-4c77-bf5c-834e87c657e2}')
    @commethod(3)
    def RegisterCallback(self, callback: win32more.Windows.Win32.Media.Audio.PAudioStateMonitorCallback, context: VoidPtr, registration: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterCallback(self, registration: Int64) -> Void: ...
    @commethod(5)
    def GetSoundLevel(self) -> win32more.Windows.Win32.Media.Audio.AudioStateMonitorSoundLevel: ...
class IAudioStreamVolume(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{93014887-242d-4068-8a15-cf5e93b90fe3}')
    @commethod(3)
    def GetChannelCount(self, pdwCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetChannelVolume(self, dwIndex: UInt32, fLevel: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetChannelVolume(self, dwIndex: UInt32, pfLevel: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetAllVolumes(self, dwCount: UInt32, pfVolumes: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetAllVolumes(self, dwCount: UInt32, pfVolumes: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioSystemEffectsPropertyChangeNotificationClient(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{20049d40-56d5-400e-a2ef-385599feed49}')
    @commethod(3)
    def OnPropertyChanged(self, type: win32more.Windows.Win32.Media.Audio.AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE, key: win32more.Windows.Win32.Foundation.PROPERTYKEY) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioSystemEffectsPropertyStore(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{302ae7f9-d7e0-43e4-971b-1f8293613d2a}')
    @commethod(3)
    def OpenDefaultPropertyStore(self, stgmAccess: UInt32, propStore: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OpenUserPropertyStore(self, stgmAccess: UInt32, propStore: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OpenVolatilePropertyStore(self, stgmAccess: UInt32, propStore: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ResetUserPropertyStore(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ResetVolatilePropertyStore(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RegisterPropertyChangeNotification(self, callback: win32more.Windows.Win32.Media.Audio.IAudioSystemEffectsPropertyChangeNotificationClient) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def UnregisterPropertyChangeNotification(self, callback: win32more.Windows.Win32.Media.Audio.IAudioSystemEffectsPropertyChangeNotificationClient) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioTreble(ComPtr):
    extends: win32more.Windows.Win32.Media.Audio.IPerChannelDbLevel
    _iid_ = Guid('{0a717812-694e-4907-b74b-bafa5cfdca7b}')
class IAudioViewManagerService(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a7a7ef10-1f49-45e0-ad35-612057cc8f74}')
    @commethod(3)
    def SetAudioStreamWindow(self, hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioVolumeDuckNotification(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c3b284d4-6d39-4359-b3cf-b56ddb3bb39c}')
    @commethod(3)
    def OnVolumeDuckNotification(self, sessionID: win32more.Windows.Win32.Foundation.PWSTR, countCommunicationSessions: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnVolumeUnduckNotification(self, sessionID: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioVolumeLevel(ComPtr):
    extends: win32more.Windows.Win32.Media.Audio.IPerChannelDbLevel
    _iid_ = Guid('{7fb7b48f-531d-44a2-bcb3-5ad5a134b3dc}')
class IChannelAudioVolume(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1c158861-b533-4b30-b1cf-e853e51c59b8}')
    @commethod(3)
    def GetChannelCount(self, pdwCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetChannelVolume(self, dwIndex: UInt32, fLevel: Single, EventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetChannelVolume(self, dwIndex: UInt32, pfLevel: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetAllVolumes(self, dwCount: UInt32, pfVolumes: POINTER(Single), EventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetAllVolumes(self, dwCount: UInt32, pfVolumes: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IConnector(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9c2c4058-23f5-41de-877a-df3af236a09e}')
    @commethod(3)
    def GetType(self, pType: POINTER(win32more.Windows.Win32.Media.Audio.ConnectorType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDataFlow(self, pFlow: POINTER(win32more.Windows.Win32.Media.Audio.DataFlow)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ConnectTo(self, pConnectTo: win32more.Windows.Win32.Media.Audio.IConnector) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Disconnect(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsConnected(self, pbConnected: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetConnectedTo(self, ppConTo: POINTER(win32more.Windows.Win32.Media.Audio.IConnector)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetConnectorIdConnectedTo(self, ppwstrConnectorId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDeviceIdConnectedTo(self, ppwstrDeviceId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IControlChangeNotify(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a09513ed-c709-4d21-bd7b-5f34c47f3947}')
    @commethod(3)
    def OnNotify(self, dwSenderProcessId: UInt32, pguidEventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IControlInterface(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{45d37c3f-5140-444a-ae24-400789f3cbf3}')
    @commethod(3)
    def GetName(self, ppwstrName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIID(self, pIID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDeviceSpecificProperty(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3b22bcbf-2586-4af0-8583-205d391b807c}')
    @commethod(3)
    def GetType(self, pVType: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetValue(self, pvValue: VoidPtr, pcbValue: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetValue(self, pvValue: VoidPtr, cbValue: UInt32, pguidEventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Get4BRange(self, plMin: POINTER(Int32), plMax: POINTER(Int32), plStepping: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDeviceTopology(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2a07407e-6497-4a18-9787-32f79bd0d98f}')
    @commethod(3)
    def GetConnectorCount(self, pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetConnector(self, nIndex: UInt32, ppConnector: POINTER(win32more.Windows.Win32.Media.Audio.IConnector)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSubunitCount(self, pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSubunit(self, nIndex: UInt32, ppSubunit: POINTER(win32more.Windows.Win32.Media.Audio.ISubunit)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPartById(self, nId: UInt32, ppPart: POINTER(win32more.Windows.Win32.Media.Audio.IPart)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDeviceId(self, ppwstrDeviceId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSignalPath(self, pIPartFrom: win32more.Windows.Win32.Media.Audio.IPart, pIPartTo: win32more.Windows.Win32.Media.Audio.IPart, bRejectMixedPaths: win32more.Windows.Win32.Foundation.BOOL, ppParts: POINTER(win32more.Windows.Win32.Media.Audio.IPartsList)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMMDevice(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d666063f-1587-4e43-81f1-b948e807363f}')
    @commethod(3)
    def Activate(self, iid: POINTER(Guid), dwClsCtx: win32more.Windows.Win32.System.Com.CLSCTX, pActivationParams: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), ppInterface: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OpenPropertyStore(self, stgmAccess: win32more.Windows.Win32.System.Com.STGM, ppProperties: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetId(self, ppstrId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetState(self, pdwState: POINTER(win32more.Windows.Win32.Media.Audio.DEVICE_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMMDeviceActivator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3b0d0ea4-d0a9-4b0e-935b-09516746fac0}')
    @commethod(3)
    def Activate(self, iid: POINTER(Guid), pDevice: win32more.Windows.Win32.Media.Audio.IMMDevice, pActivationParams: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), ppInterface: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMMDeviceCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0bd7a1be-7a1a-44db-8397-cc5392387b5e}')
    @commethod(3)
    def GetCount(self, pcDevices: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Item(self, nDevice: UInt32, ppDevice: POINTER(win32more.Windows.Win32.Media.Audio.IMMDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMMDeviceEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a95664d2-9614-4f35-a746-de8db63617e6}')
    @commethod(3)
    def EnumAudioEndpoints(self, dataFlow: win32more.Windows.Win32.Media.Audio.EDataFlow, dwStateMask: win32more.Windows.Win32.Media.Audio.DEVICE_STATE, ppDevices: POINTER(win32more.Windows.Win32.Media.Audio.IMMDeviceCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDefaultAudioEndpoint(self, dataFlow: win32more.Windows.Win32.Media.Audio.EDataFlow, role: win32more.Windows.Win32.Media.Audio.ERole, ppEndpoint: POINTER(win32more.Windows.Win32.Media.Audio.IMMDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDevice(self, pwstrId: win32more.Windows.Win32.Foundation.PWSTR, ppDevice: POINTER(win32more.Windows.Win32.Media.Audio.IMMDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RegisterEndpointNotificationCallback(self, pClient: win32more.Windows.Win32.Media.Audio.IMMNotificationClient) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UnregisterEndpointNotificationCallback(self, pClient: win32more.Windows.Win32.Media.Audio.IMMNotificationClient) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMMEndpoint(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1be09788-6894-4089-8586-9a2a6c265ac5}')
    @commethod(3)
    def GetDataFlow(self, pDataFlow: POINTER(win32more.Windows.Win32.Media.Audio.EDataFlow)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMMNotificationClient(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7991eec9-7e89-4d85-8390-6c703cec60c0}')
    @commethod(3)
    def OnDeviceStateChanged(self, pwstrDeviceId: win32more.Windows.Win32.Foundation.PWSTR, dwNewState: win32more.Windows.Win32.Media.Audio.DEVICE_STATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnDeviceAdded(self, pwstrDeviceId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnDeviceRemoved(self, pwstrDeviceId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnDefaultDeviceChanged(self, flow: win32more.Windows.Win32.Media.Audio.EDataFlow, role: win32more.Windows.Win32.Media.Audio.ERole, pwstrDefaultDeviceId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnPropertyValueChanged(self, pwstrDeviceId: win32more.Windows.Win32.Foundation.PWSTR, key: win32more.Windows.Win32.Foundation.PROPERTYKEY) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMessageFilter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000016-0000-0000-c000-000000000046}')
    @commethod(3)
    def HandleInComingCall(self, dwCallType: UInt32, htaskCaller: win32more.Windows.Win32.Media.HTASK, dwTickCount: UInt32, lpInterfaceInfo: POINTER(win32more.Windows.Win32.System.Com.INTERFACEINFO)) -> UInt32: ...
    @commethod(4)
    def RetryRejectedCall(self, htaskCallee: win32more.Windows.Win32.Media.HTASK, dwTickCount: UInt32, dwRejectType: UInt32) -> UInt32: ...
    @commethod(5)
    def MessagePending(self, htaskCallee: win32more.Windows.Win32.Media.HTASK, dwTickCount: UInt32, dwPendingType: UInt32) -> UInt32: ...
class IPart(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ae2de0e4-5bca-4f2d-aa46-5d13f8fdb3a9}')
    @commethod(3)
    def GetName(self, ppwstrName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLocalId(self, pnId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetGlobalId(self, ppwstrGlobalId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPartType(self, pPartType: POINTER(win32more.Windows.Win32.Media.Audio.PartType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSubType(self, pSubType: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetControlInterfaceCount(self, pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetControlInterface(self, nIndex: UInt32, ppInterfaceDesc: POINTER(win32more.Windows.Win32.Media.Audio.IControlInterface)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EnumPartsIncoming(self, ppParts: POINTER(win32more.Windows.Win32.Media.Audio.IPartsList)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnumPartsOutgoing(self, ppParts: POINTER(win32more.Windows.Win32.Media.Audio.IPartsList)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetTopologyObject(self, ppTopology: POINTER(win32more.Windows.Win32.Media.Audio.IDeviceTopology)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Activate(self, dwClsContext: UInt32, refiid: POINTER(Guid), ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RegisterControlChangeCallback(self, riid: POINTER(Guid), pNotify: win32more.Windows.Win32.Media.Audio.IControlChangeNotify) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def UnregisterControlChangeCallback(self, pNotify: win32more.Windows.Win32.Media.Audio.IControlChangeNotify) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPartsList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6daa848c-5eb0-45cc-aea5-998a2cda1ffb}')
    @commethod(3)
    def GetCount(self, pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPart(self, nIndex: UInt32, ppPart: POINTER(win32more.Windows.Win32.Media.Audio.IPart)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPerChannelDbLevel(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c2f8e001-f205-4bc9-99bc-c13b1e048ccb}')
    @commethod(3)
    def GetChannelCount(self, pcChannels: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLevelRange(self, nChannel: UInt32, pfMinLevelDB: POINTER(Single), pfMaxLevelDB: POINTER(Single), pfStepping: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLevel(self, nChannel: UInt32, pfLevelDB: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetLevel(self, nChannel: UInt32, fLevelDB: Single, pguidEventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetLevelUniform(self, fLevelDB: Single, pguidEventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetLevelAllChannels(self, aLevelsDB: POINTER(Single), cChannels: UInt32, pguidEventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISimpleAudioVolume(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{87ce5498-68d6-44e5-9215-6da47ef883d8}')
    @commethod(3)
    def SetMasterVolume(self, fLevel: Single, EventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMasterVolume(self, pfLevel: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetMute(self, bMute: win32more.Windows.Win32.Foundation.BOOL, EventContext: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMute(self, pbMute: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioClient(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bbf8e066-aaaa-49be-9a4d-fd2a858ea27f}')
    @commethod(3)
    def GetStaticObjectPosition(self, type: win32more.Windows.Win32.Media.Audio.AudioObjectType, x: POINTER(Single), y: POINTER(Single), z: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNativeStaticObjectTypeMask(self, mask: POINTER(win32more.Windows.Win32.Media.Audio.AudioObjectType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMaxDynamicObjectCount(self, value: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSupportedAudioObjectFormatEnumerator(self, enumerator: POINTER(win32more.Windows.Win32.Media.Audio.IAudioFormatEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetMaxFrameCount(self, objectFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), frameCountPerBuffer: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsAudioObjectFormatSupported(self, objectFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def IsSpatialAudioStreamAvailable(self, streamUuid: POINTER(Guid), auxiliaryInfo: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ActivateSpatialAudioStream(self, activationParams: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), riid: POINTER(Guid), stream: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioClient2(ComPtr):
    extends: win32more.Windows.Win32.Media.Audio.ISpatialAudioClient
    _iid_ = Guid('{caabe452-a66a-4bee-a93e-e320463f6a53}')
    @commethod(11)
    def IsOffloadCapable(self, category: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY, isOffloadCapable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetMaxFrameCountForCategory(self, category: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY, offloadEnabled: win32more.Windows.Win32.Foundation.BOOL, objectFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX), frameCountPerBuffer: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioMetadataClient(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{777d4a3b-f6ff-4a26-85dc-68d7cdeda1d4}')
    @commethod(3)
    def ActivateSpatialAudioMetadataItems(self, maxItemCount: UInt16, frameCount: UInt16, metadataItemsBuffer: POINTER(win32more.Windows.Win32.Media.Audio.ISpatialAudioMetadataItemsBuffer), metadataItems: POINTER(win32more.Windows.Win32.Media.Audio.ISpatialAudioMetadataItems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSpatialAudioMetadataItemsBufferLength(self, maxItemCount: UInt16, bufferLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ActivateSpatialAudioMetadataWriter(self, overflowMode: win32more.Windows.Win32.Media.Audio.SpatialAudioMetadataWriterOverflowMode, metadataWriter: POINTER(win32more.Windows.Win32.Media.Audio.ISpatialAudioMetadataWriter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ActivateSpatialAudioMetadataCopier(self, metadataCopier: POINTER(win32more.Windows.Win32.Media.Audio.ISpatialAudioMetadataCopier)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ActivateSpatialAudioMetadataReader(self, metadataReader: POINTER(win32more.Windows.Win32.Media.Audio.ISpatialAudioMetadataReader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioMetadataCopier(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d224b233-e251-4fd0-9ca2-d5ecf9a68404}')
    @commethod(3)
    def Open(self, metadataItems: win32more.Windows.Win32.Media.Audio.ISpatialAudioMetadataItems) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CopyMetadataForFrames(self, copyFrameCount: UInt16, copyMode: win32more.Windows.Win32.Media.Audio.SpatialAudioMetadataCopyMode, dstMetadataItems: win32more.Windows.Win32.Media.Audio.ISpatialAudioMetadataItems, itemsCopied: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioMetadataItems(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bcd7c78f-3098-4f22-b547-a2f25a381269}')
    @commethod(3)
    def GetFrameCount(self, frameCount: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetItemCount(self, itemCount: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMaxItemCount(self, maxItemCount: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMaxValueBufferLength(self, maxValueBufferLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetInfo(self, info: POINTER(win32more.Windows.Win32.Media.Audio.SpatialAudioMetadataItemsInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioMetadataItemsBuffer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{42640a16-e1bd-42d9-9ff6-031ab71a2dba}')
    @commethod(3)
    def AttachToBuffer(self, buffer: POINTER(Byte), bufferLength: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AttachToPopulatedBuffer(self, buffer: POINTER(Byte), bufferLength: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DetachBuffer(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioMetadataReader(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b78e86a2-31d9-4c32-94d2-7df40fc7ebec}')
    @commethod(3)
    def Open(self, metadataItems: win32more.Windows.Win32.Media.Audio.ISpatialAudioMetadataItems) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReadNextItem(self, commandCount: POINTER(Byte), frameOffset: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ReadNextItemCommand(self, commandID: POINTER(Byte), valueBuffer: VoidPtr, maxValueBufferLength: UInt32, valueBufferLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioMetadataWriter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1b17ca01-2955-444d-a430-537dc589a844}')
    @commethod(3)
    def Open(self, metadataItems: win32more.Windows.Win32.Media.Audio.ISpatialAudioMetadataItems) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WriteNextItem(self, frameOffset: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def WriteNextItemCommand(self, commandID: Byte, valueBuffer: VoidPtr, valueBufferLength: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioObject(ComPtr):
    extends: win32more.Windows.Win32.Media.Audio.ISpatialAudioObjectBase
    _iid_ = Guid('{dde28967-521b-46e5-8f00-bd6f2bc8ab1d}')
    @commethod(7)
    def SetPosition(self, x: Single, y: Single, z: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetVolume(self, volume: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioObjectBase(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cce0b8f2-8d4d-4efb-a8cf-3d6ecf1c30e0}')
    @commethod(3)
    def GetBuffer(self, buffer: POINTER(POINTER(Byte)), bufferLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetEndOfStream(self, frameCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsActive(self, isActive: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAudioObjectType(self, audioObjectType: POINTER(win32more.Windows.Win32.Media.Audio.AudioObjectType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioObjectForHrtf(ComPtr):
    extends: win32more.Windows.Win32.Media.Audio.ISpatialAudioObjectBase
    _iid_ = Guid('{d7436ade-1978-4e14-aba0-555bd8eb83b4}')
    @commethod(7)
    def SetPosition(self, x: Single, y: Single, z: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetGain(self, gain: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetOrientation(self, orientation: POINTER(POINTER(Single))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetEnvironment(self, environment: win32more.Windows.Win32.Media.Audio.SpatialAudioHrtfEnvironmentType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetDistanceDecay(self, distanceDecay: POINTER(win32more.Windows.Win32.Media.Audio.SpatialAudioHrtfDistanceDecay)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetDirectivity(self, directivity: POINTER(win32more.Windows.Win32.Media.Audio.SpatialAudioHrtfDirectivityUnion)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioObjectForMetadataCommands(ComPtr):
    extends: win32more.Windows.Win32.Media.Audio.ISpatialAudioObjectBase
    _iid_ = Guid('{0df2c94b-f5f9-472d-af6b-c46e0ac9cd05}')
    @commethod(7)
    def WriteNextMetadataCommand(self, commandID: Byte, valueBuffer: VoidPtr, valueBufferLength: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioObjectForMetadataItems(ComPtr):
    extends: win32more.Windows.Win32.Media.Audio.ISpatialAudioObjectBase
    _iid_ = Guid('{ddea49ff-3bc0-4377-8aad-9fbcfd808566}')
    @commethod(7)
    def GetSpatialAudioMetadataItems(self, metadataItems: POINTER(win32more.Windows.Win32.Media.Audio.ISpatialAudioMetadataItems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioObjectRenderStream(ComPtr):
    extends: win32more.Windows.Win32.Media.Audio.ISpatialAudioObjectRenderStreamBase
    _iid_ = Guid('{bab5f473-b423-477b-85f5-b5a332a04153}')
    @commethod(10)
    def ActivateSpatialAudioObject(self, type: win32more.Windows.Win32.Media.Audio.AudioObjectType, audioObject: POINTER(win32more.Windows.Win32.Media.Audio.ISpatialAudioObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioObjectRenderStreamBase(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{feaaf403-c1d8-450d-aa05-e0ccee7502a8}')
    @commethod(3)
    def GetAvailableDynamicObjectCount(self, value: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetService(self, riid: POINTER(Guid), service: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Start(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Stop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def BeginUpdatingAudioObjects(self, availableDynamicObjectCount: POINTER(UInt32), frameCountPerBuffer: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EndUpdatingAudioObjects(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioObjectRenderStreamForHrtf(ComPtr):
    extends: win32more.Windows.Win32.Media.Audio.ISpatialAudioObjectRenderStreamBase
    _iid_ = Guid('{e08deef9-5363-406e-9fdc-080ee247bbe0}')
    @commethod(10)
    def ActivateSpatialAudioObjectForHrtf(self, type: win32more.Windows.Win32.Media.Audio.AudioObjectType, audioObject: POINTER(win32more.Windows.Win32.Media.Audio.ISpatialAudioObjectForHrtf)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioObjectRenderStreamForMetadata(ComPtr):
    extends: win32more.Windows.Win32.Media.Audio.ISpatialAudioObjectRenderStreamBase
    _iid_ = Guid('{bbc9c907-48d5-4a2e-a0c7-f7f0d67c1fb1}')
    @commethod(10)
    def ActivateSpatialAudioObjectForMetadataCommands(self, type: win32more.Windows.Win32.Media.Audio.AudioObjectType, audioObject: POINTER(win32more.Windows.Win32.Media.Audio.ISpatialAudioObjectForMetadataCommands)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ActivateSpatialAudioObjectForMetadataItems(self, type: win32more.Windows.Win32.Media.Audio.AudioObjectType, audioObject: POINTER(win32more.Windows.Win32.Media.Audio.ISpatialAudioObjectForMetadataItems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioObjectRenderStreamNotify(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dddf83e6-68d7-4c70-883f-a1836afb4a50}')
    @commethod(3)
    def OnAvailableDynamicObjectCountChange(self, sender: win32more.Windows.Win32.Media.Audio.ISpatialAudioObjectRenderStreamBase, hnsComplianceDeadlineTime: Int64, availableDynamicObjectCountChange: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISubunit(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{82149a85-dba6-4487-86bb-ea8f7fefcc71}')
@winfunctype_pointer
def LPACMDRIVERPROC(param0: UIntPtr, param1: win32more.Windows.Win32.Media.Audio.HACMDRIVERID, param2: UInt32, param3: win32more.Windows.Win32.Foundation.LPARAM, param4: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.LRESULT: ...
@winfunctype_pointer
def LPMIDICALLBACK(hdrvr: win32more.Windows.Win32.Media.Multimedia.HDRVR, uMsg: UInt32, dwUser: UIntPtr, dw1: UIntPtr, dw2: UIntPtr) -> Void: ...
@winfunctype_pointer
def LPWAVECALLBACK(hdrvr: win32more.Windows.Win32.Media.Multimedia.HDRVR, uMsg: UInt32, dwUser: UIntPtr, dw1: UIntPtr, dw2: UIntPtr) -> Void: ...
class MIDIEVENT(Structure):
    dwDeltaTime: UInt32
    dwStreamID: UInt32
    dwEvent: UInt32
    dwParms: UInt32 * 1
    _pack_ = 1
class MIDIHDR(Structure):
    lpData: win32more.Windows.Win32.Foundation.PSTR
    dwBufferLength: UInt32
    dwBytesRecorded: UInt32
    dwUser: UIntPtr
    dwFlags: UInt32
    lpNext: POINTER(win32more.Windows.Win32.Media.Audio.MIDIHDR)
    reserved: UIntPtr
    dwOffset: UInt32
    dwReserved: UIntPtr * 8
    _pack_ = 1
class MIDIINCAPS2A(Structure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: win32more.Windows.Win32.Foundation.CHAR * 32
    dwSupport: UInt32
    ManufacturerGuid: Guid
    ProductGuid: Guid
    NameGuid: Guid
    _pack_ = 1
class MIDIINCAPS2W(Structure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Char * 32
    dwSupport: UInt32
    ManufacturerGuid: Guid
    ProductGuid: Guid
    NameGuid: Guid
    _pack_ = 1
MIDIINCAPS2 = UnicodeAlias('MIDIINCAPS2W')
class MIDIINCAPSA(Structure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: win32more.Windows.Win32.Foundation.CHAR * 32
    dwSupport: UInt32
    _pack_ = 1
class MIDIINCAPSW(Structure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Char * 32
    dwSupport: UInt32
    _pack_ = 1
MIDIINCAPS = UnicodeAlias('MIDIINCAPSW')
class MIDIOUTCAPS2A(Structure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: win32more.Windows.Win32.Foundation.CHAR * 32
    wTechnology: UInt16
    wVoices: UInt16
    wNotes: UInt16
    wChannelMask: UInt16
    dwSupport: UInt32
    ManufacturerGuid: Guid
    ProductGuid: Guid
    NameGuid: Guid
    _pack_ = 1
class MIDIOUTCAPS2W(Structure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Char * 32
    wTechnology: UInt16
    wVoices: UInt16
    wNotes: UInt16
    wChannelMask: UInt16
    dwSupport: UInt32
    ManufacturerGuid: Guid
    ProductGuid: Guid
    NameGuid: Guid
    _pack_ = 1
MIDIOUTCAPS2 = UnicodeAlias('MIDIOUTCAPS2W')
class MIDIOUTCAPSA(Structure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: win32more.Windows.Win32.Foundation.CHAR * 32
    wTechnology: UInt16
    wVoices: UInt16
    wNotes: UInt16
    wChannelMask: UInt16
    dwSupport: UInt32
    _pack_ = 1
class MIDIOUTCAPSW(Structure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Char * 32
    wTechnology: UInt16
    wVoices: UInt16
    wNotes: UInt16
    wChannelMask: UInt16
    dwSupport: UInt32
    _pack_ = 1
MIDIOUTCAPS = UnicodeAlias('MIDIOUTCAPSW')
class MIDIPROPTEMPO(Structure):
    cbStruct: UInt32
    dwTempo: UInt32
    _pack_ = 1
class MIDIPROPTIMEDIV(Structure):
    cbStruct: UInt32
    dwTimeDiv: UInt32
    _pack_ = 1
class MIDISTRMBUFFVER(Structure):
    dwVersion: UInt32
    dwMid: UInt32
    dwOEMVersion: UInt32
    _pack_ = 1
MIDI_WAVE_OPEN_TYPE = UInt32
CALLBACK_TYPEMASK: win32more.Windows.Win32.Media.Audio.MIDI_WAVE_OPEN_TYPE = 458752
CALLBACK_NULL: win32more.Windows.Win32.Media.Audio.MIDI_WAVE_OPEN_TYPE = 0
CALLBACK_WINDOW: win32more.Windows.Win32.Media.Audio.MIDI_WAVE_OPEN_TYPE = 65536
CALLBACK_TASK: win32more.Windows.Win32.Media.Audio.MIDI_WAVE_OPEN_TYPE = 131072
CALLBACK_FUNCTION: win32more.Windows.Win32.Media.Audio.MIDI_WAVE_OPEN_TYPE = 196608
CALLBACK_THREAD: win32more.Windows.Win32.Media.Audio.MIDI_WAVE_OPEN_TYPE = 131072
CALLBACK_EVENT: win32more.Windows.Win32.Media.Audio.MIDI_WAVE_OPEN_TYPE = 327680
WAVE_FORMAT_QUERY: win32more.Windows.Win32.Media.Audio.MIDI_WAVE_OPEN_TYPE = 1
WAVE_ALLOWSYNC: win32more.Windows.Win32.Media.Audio.MIDI_WAVE_OPEN_TYPE = 2
WAVE_MAPPED: win32more.Windows.Win32.Media.Audio.MIDI_WAVE_OPEN_TYPE = 4
WAVE_FORMAT_DIRECT: win32more.Windows.Win32.Media.Audio.MIDI_WAVE_OPEN_TYPE = 8
WAVE_FORMAT_DIRECT_QUERY: win32more.Windows.Win32.Media.Audio.MIDI_WAVE_OPEN_TYPE = 9
WAVE_MAPPED_DEFAULT_COMMUNICATION_DEVICE: win32more.Windows.Win32.Media.Audio.MIDI_WAVE_OPEN_TYPE = 16
MIDI_IO_STATUS: win32more.Windows.Win32.Media.Audio.MIDI_WAVE_OPEN_TYPE = 32
class MIXERCAPS2A(Structure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: win32more.Windows.Win32.Foundation.CHAR * 32
    fdwSupport: UInt32
    cDestinations: UInt32
    ManufacturerGuid: Guid
    ProductGuid: Guid
    NameGuid: Guid
    _pack_ = 1
class MIXERCAPS2W(Structure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Char * 32
    fdwSupport: UInt32
    cDestinations: UInt32
    ManufacturerGuid: Guid
    ProductGuid: Guid
    NameGuid: Guid
    _pack_ = 1
MIXERCAPS2 = UnicodeAlias('MIXERCAPS2W')
class MIXERCAPSA(Structure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: win32more.Windows.Win32.Foundation.CHAR * 32
    fdwSupport: UInt32
    cDestinations: UInt32
    _pack_ = 1
class MIXERCAPSW(Structure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Char * 32
    fdwSupport: UInt32
    cDestinations: UInt32
    _pack_ = 1
MIXERCAPS = UnicodeAlias('MIXERCAPSW')
class MIXERCONTROLA(Structure):
    cbStruct: UInt32
    dwControlID: UInt32
    dwControlType: UInt32
    fdwControl: UInt32
    cMultipleItems: UInt32
    szShortName: win32more.Windows.Win32.Foundation.CHAR * 16
    szName: win32more.Windows.Win32.Foundation.CHAR * 64
    Bounds: _Bounds_e__Union
    Metrics: _Metrics_e__Union
    _pack_ = 1
    class _Bounds_e__Union(Union):
        Anonymous1: _Anonymous1_e__Struct
        Anonymous2: _Anonymous2_e__Struct
        dwReserved: UInt32 * 6
        _pack_ = 1
        class _Anonymous1_e__Struct(Structure):
            lMinimum: Int32
            lMaximum: Int32
            _pack_ = 1
        class _Anonymous2_e__Struct(Structure):
            dwMinimum: UInt32
            dwMaximum: UInt32
            _pack_ = 1
    class _Metrics_e__Union(Union):
        cSteps: UInt32
        cbCustomData: UInt32
        dwReserved: UInt32 * 6
        _pack_ = 1
class MIXERCONTROLDETAILS(Structure):
    cbStruct: UInt32
    dwControlID: UInt32
    cChannels: UInt32
    Anonymous: _Anonymous_e__Union
    cbDetails: UInt32
    paDetails: VoidPtr
    _pack_ = 1
    class _Anonymous_e__Union(Union):
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        cMultipleItems: UInt32
        _pack_ = 1
class MIXERCONTROLDETAILS_BOOLEAN(Structure):
    fValue: Int32
    _pack_ = 1
class MIXERCONTROLDETAILS_LISTTEXTA(Structure):
    dwParam1: UInt32
    dwParam2: UInt32
    szName: win32more.Windows.Win32.Foundation.CHAR * 64
    _pack_ = 1
class MIXERCONTROLDETAILS_LISTTEXTW(Structure):
    dwParam1: UInt32
    dwParam2: UInt32
    szName: Char * 64
    _pack_ = 1
MIXERCONTROLDETAILS_LISTTEXT = UnicodeAlias('MIXERCONTROLDETAILS_LISTTEXTW')
class MIXERCONTROLDETAILS_SIGNED(Structure):
    lValue: Int32
    _pack_ = 1
class MIXERCONTROLDETAILS_UNSIGNED(Structure):
    dwValue: UInt32
    _pack_ = 1
class MIXERCONTROLW(Structure):
    cbStruct: UInt32
    dwControlID: UInt32
    dwControlType: UInt32
    fdwControl: UInt32
    cMultipleItems: UInt32
    szShortName: Char * 16
    szName: Char * 64
    Bounds: _Bounds_e__Union
    Metrics: _Metrics_e__Union
    _pack_ = 1
    class _Bounds_e__Union(Union):
        Anonymous1: _Anonymous1_e__Struct
        Anonymous2: _Anonymous2_e__Struct
        dwReserved: UInt32 * 6
        _pack_ = 1
        class _Anonymous1_e__Struct(Structure):
            lMinimum: Int32
            lMaximum: Int32
            _pack_ = 1
        class _Anonymous2_e__Struct(Structure):
            dwMinimum: UInt32
            dwMaximum: UInt32
            _pack_ = 1
    class _Metrics_e__Union(Union):
        cSteps: UInt32
        cbCustomData: UInt32
        dwReserved: UInt32 * 6
        _pack_ = 1
MIXERCONTROL = UnicodeAlias('MIXERCONTROLW')
class MIXERLINEA(Structure):
    cbStruct: UInt32
    dwDestination: UInt32
    dwSource: UInt32
    dwLineID: UInt32
    fdwLine: UInt32
    dwUser: UIntPtr
    dwComponentType: win32more.Windows.Win32.Media.Audio.MIXERLINE_COMPONENTTYPE
    cChannels: UInt32
    cConnections: UInt32
    cControls: UInt32
    szShortName: win32more.Windows.Win32.Foundation.CHAR * 16
    szName: win32more.Windows.Win32.Foundation.CHAR * 64
    Target: _Target_e__Struct
    _pack_ = 1
    class _Target_e__Struct(Structure):
        dwType: UInt32
        dwDeviceID: UInt32
        wMid: UInt16
        wPid: UInt16
        vDriverVersion: UInt32
        szPname: win32more.Windows.Win32.Foundation.CHAR * 32
        _pack_ = 1
class MIXERLINECONTROLSA(Structure):
    cbStruct: UInt32
    dwLineID: UInt32
    Anonymous: _Anonymous_e__Union
    cControls: UInt32
    cbmxctrl: UInt32
    pamxctrl: POINTER(win32more.Windows.Win32.Media.Audio.MIXERCONTROLA)
    _pack_ = 1
    class _Anonymous_e__Union(Union):
        dwControlID: UInt32
        dwControlType: UInt32
        _pack_ = 1
class MIXERLINECONTROLSW(Structure):
    cbStruct: UInt32
    dwLineID: UInt32
    Anonymous: _Anonymous_e__Union
    cControls: UInt32
    cbmxctrl: UInt32
    pamxctrl: POINTER(win32more.Windows.Win32.Media.Audio.MIXERCONTROLW)
    _pack_ = 1
    class _Anonymous_e__Union(Union):
        dwControlID: UInt32
        dwControlType: UInt32
        _pack_ = 1
MIXERLINECONTROLS = UnicodeAlias('MIXERLINECONTROLSW')
class MIXERLINEW(Structure):
    cbStruct: UInt32
    dwDestination: UInt32
    dwSource: UInt32
    dwLineID: UInt32
    fdwLine: UInt32
    dwUser: UIntPtr
    dwComponentType: win32more.Windows.Win32.Media.Audio.MIXERLINE_COMPONENTTYPE
    cChannels: UInt32
    cConnections: UInt32
    cControls: UInt32
    szShortName: Char * 16
    szName: Char * 64
    Target: _Target_e__Struct
    _pack_ = 1
    class _Target_e__Struct(Structure):
        dwType: UInt32
        dwDeviceID: UInt32
        wMid: UInt16
        wPid: UInt16
        vDriverVersion: UInt32
        szPname: Char * 32
        _pack_ = 1
MIXERLINE = UnicodeAlias('MIXERLINEW')
MIXERLINE_COMPONENTTYPE = UInt32
MIXERLINE_COMPONENTTYPE_DST_DIGITAL: win32more.Windows.Win32.Media.Audio.MIXERLINE_COMPONENTTYPE = 1
MIXERLINE_COMPONENTTYPE_DST_HEADPHONES: win32more.Windows.Win32.Media.Audio.MIXERLINE_COMPONENTTYPE = 5
MIXERLINE_COMPONENTTYPE_DST_LINE: win32more.Windows.Win32.Media.Audio.MIXERLINE_COMPONENTTYPE = 2
MIXERLINE_COMPONENTTYPE_DST_MONITOR: win32more.Windows.Win32.Media.Audio.MIXERLINE_COMPONENTTYPE = 3
MIXERLINE_COMPONENTTYPE_DST_SPEAKERS: win32more.Windows.Win32.Media.Audio.MIXERLINE_COMPONENTTYPE = 4
MIXERLINE_COMPONENTTYPE_DST_TELEPHONE: win32more.Windows.Win32.Media.Audio.MIXERLINE_COMPONENTTYPE = 6
MIXERLINE_COMPONENTTYPE_DST_UNDEFINED: win32more.Windows.Win32.Media.Audio.MIXERLINE_COMPONENTTYPE = 0
MIXERLINE_COMPONENTTYPE_DST_VOICEIN: win32more.Windows.Win32.Media.Audio.MIXERLINE_COMPONENTTYPE = 8
MIXERLINE_COMPONENTTYPE_DST_WAVEIN: win32more.Windows.Win32.Media.Audio.MIXERLINE_COMPONENTTYPE = 7
MIXERLINE_COMPONENTTYPE_SRC_ANALOG: win32more.Windows.Win32.Media.Audio.MIXERLINE_COMPONENTTYPE = 4106
MIXERLINE_COMPONENTTYPE_SRC_AUXILIARY: win32more.Windows.Win32.Media.Audio.MIXERLINE_COMPONENTTYPE = 4105
MIXERLINE_COMPONENTTYPE_SRC_COMPACTDISC: win32more.Windows.Win32.Media.Audio.MIXERLINE_COMPONENTTYPE = 4101
MIXERLINE_COMPONENTTYPE_SRC_DIGITAL: win32more.Windows.Win32.Media.Audio.MIXERLINE_COMPONENTTYPE = 4097
MIXERLINE_COMPONENTTYPE_SRC_LINE: win32more.Windows.Win32.Media.Audio.MIXERLINE_COMPONENTTYPE = 4098
MIXERLINE_COMPONENTTYPE_SRC_MICROPHONE: win32more.Windows.Win32.Media.Audio.MIXERLINE_COMPONENTTYPE = 4099
MIXERLINE_COMPONENTTYPE_SRC_PCSPEAKER: win32more.Windows.Win32.Media.Audio.MIXERLINE_COMPONENTTYPE = 4103
MIXERLINE_COMPONENTTYPE_SRC_SYNTHESIZER: win32more.Windows.Win32.Media.Audio.MIXERLINE_COMPONENTTYPE = 4100
MIXERLINE_COMPONENTTYPE_SRC_TELEPHONE: win32more.Windows.Win32.Media.Audio.MIXERLINE_COMPONENTTYPE = 4102
MIXERLINE_COMPONENTTYPE_SRC_UNDEFINED: win32more.Windows.Win32.Media.Audio.MIXERLINE_COMPONENTTYPE = 4096
MIXERLINE_COMPONENTTYPE_SRC_WAVEOUT: win32more.Windows.Win32.Media.Audio.MIXERLINE_COMPONENTTYPE = 4104
MMDeviceEnumerator = Guid('{bcde0395-e52f-467c-8e3d-c4579291692e}')
@winfunctype_pointer
def PAudioStateMonitorCallback(audioStateMonitor: win32more.Windows.Win32.Media.Audio.IAudioStateMonitor, context: VoidPtr) -> Void: ...
class PCMWAVEFORMAT(Structure):
    wf: win32more.Windows.Win32.Media.Audio.WAVEFORMAT
    wBitsPerSample: UInt16
    _pack_ = 1
PROCESS_LOOPBACK_MODE = Int32
PROCESS_LOOPBACK_MODE_INCLUDE_TARGET_PROCESS_TREE: win32more.Windows.Win32.Media.Audio.PROCESS_LOOPBACK_MODE = 0
PROCESS_LOOPBACK_MODE_EXCLUDE_TARGET_PROCESS_TREE: win32more.Windows.Win32.Media.Audio.PROCESS_LOOPBACK_MODE = 1
PartType = Int32
Connector: win32more.Windows.Win32.Media.Audio.PartType = 0
Subunit: win32more.Windows.Win32.Media.Audio.PartType = 1
SND_FLAGS = UInt32
SND_APPLICATION: win32more.Windows.Win32.Media.Audio.SND_FLAGS = 128
SND_ALIAS: win32more.Windows.Win32.Media.Audio.SND_FLAGS = 65536
SND_ALIAS_ID: win32more.Windows.Win32.Media.Audio.SND_FLAGS = 1114112
SND_FILENAME: win32more.Windows.Win32.Media.Audio.SND_FLAGS = 131072
SND_RESOURCE: win32more.Windows.Win32.Media.Audio.SND_FLAGS = 262148
SND_ASYNC: win32more.Windows.Win32.Media.Audio.SND_FLAGS = 1
SND_NODEFAULT: win32more.Windows.Win32.Media.Audio.SND_FLAGS = 2
SND_LOOP: win32more.Windows.Win32.Media.Audio.SND_FLAGS = 8
SND_MEMORY: win32more.Windows.Win32.Media.Audio.SND_FLAGS = 4
SND_NOSTOP: win32more.Windows.Win32.Media.Audio.SND_FLAGS = 16
SND_NOWAIT: win32more.Windows.Win32.Media.Audio.SND_FLAGS = 8192
SND_PURGE: win32more.Windows.Win32.Media.Audio.SND_FLAGS = 64
SND_SENTRY: win32more.Windows.Win32.Media.Audio.SND_FLAGS = 524288
SND_SYNC: win32more.Windows.Win32.Media.Audio.SND_FLAGS = 0
SND_SYSTEM: win32more.Windows.Win32.Media.Audio.SND_FLAGS = 2097152
SPATIAL_AUDIO_STREAM_OPTIONS = Int32
SPATIAL_AUDIO_STREAM_OPTIONS_NONE: win32more.Windows.Win32.Media.Audio.SPATIAL_AUDIO_STREAM_OPTIONS = 0
SPATIAL_AUDIO_STREAM_OPTIONS_OFFLOAD: win32more.Windows.Win32.Media.Audio.SPATIAL_AUDIO_STREAM_OPTIONS = 1
class SpatialAudioClientActivationParams(Structure):
    tracingContextId: Guid
    appId: Guid
    majorVersion: Int32
    minorVersion1: Int32
    minorVersion2: Int32
    minorVersion3: Int32
class SpatialAudioHrtfActivationParams(Structure):
    ObjectFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)
    StaticObjectTypeMask: win32more.Windows.Win32.Media.Audio.AudioObjectType
    MinDynamicObjectCount: UInt32
    MaxDynamicObjectCount: UInt32
    Category: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY
    EventHandle: win32more.Windows.Win32.Foundation.HANDLE
    NotifyObject: win32more.Windows.Win32.Media.Audio.ISpatialAudioObjectRenderStreamNotify
    DistanceDecay: POINTER(win32more.Windows.Win32.Media.Audio.SpatialAudioHrtfDistanceDecay)
    Directivity: POINTER(win32more.Windows.Win32.Media.Audio.SpatialAudioHrtfDirectivityUnion)
    Environment: POINTER(win32more.Windows.Win32.Media.Audio.SpatialAudioHrtfEnvironmentType)
    Orientation: POINTER(Single)
    _pack_ = 1
class SpatialAudioHrtfActivationParams2(Structure):
    ObjectFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)
    StaticObjectTypeMask: win32more.Windows.Win32.Media.Audio.AudioObjectType
    MinDynamicObjectCount: UInt32
    MaxDynamicObjectCount: UInt32
    Category: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY
    EventHandle: win32more.Windows.Win32.Foundation.HANDLE
    NotifyObject: win32more.Windows.Win32.Media.Audio.ISpatialAudioObjectRenderStreamNotify
    DistanceDecay: POINTER(win32more.Windows.Win32.Media.Audio.SpatialAudioHrtfDistanceDecay)
    Directivity: POINTER(win32more.Windows.Win32.Media.Audio.SpatialAudioHrtfDirectivityUnion)
    Environment: POINTER(win32more.Windows.Win32.Media.Audio.SpatialAudioHrtfEnvironmentType)
    Orientation: POINTER(Single)
    Options: win32more.Windows.Win32.Media.Audio.SPATIAL_AUDIO_STREAM_OPTIONS
    _pack_ = 1
class SpatialAudioHrtfDirectivity(Structure):
    Type: win32more.Windows.Win32.Media.Audio.SpatialAudioHrtfDirectivityType
    Scaling: Single
    _pack_ = 1
class SpatialAudioHrtfDirectivityCardioid(Structure):
    directivity: win32more.Windows.Win32.Media.Audio.SpatialAudioHrtfDirectivity
    Order: Single
    _pack_ = 1
class SpatialAudioHrtfDirectivityCone(Structure):
    directivity: win32more.Windows.Win32.Media.Audio.SpatialAudioHrtfDirectivity
    InnerAngle: Single
    OuterAngle: Single
    _pack_ = 1
SpatialAudioHrtfDirectivityType = Int32
SpatialAudioHrtfDirectivity_OmniDirectional: win32more.Windows.Win32.Media.Audio.SpatialAudioHrtfDirectivityType = 0
SpatialAudioHrtfDirectivity_Cardioid: win32more.Windows.Win32.Media.Audio.SpatialAudioHrtfDirectivityType = 1
SpatialAudioHrtfDirectivity_Cone: win32more.Windows.Win32.Media.Audio.SpatialAudioHrtfDirectivityType = 2
class SpatialAudioHrtfDirectivityUnion(Union):
    Cone: win32more.Windows.Win32.Media.Audio.SpatialAudioHrtfDirectivityCone
    Cardiod: win32more.Windows.Win32.Media.Audio.SpatialAudioHrtfDirectivityCardioid
    Omni: win32more.Windows.Win32.Media.Audio.SpatialAudioHrtfDirectivity
class SpatialAudioHrtfDistanceDecay(Structure):
    Type: win32more.Windows.Win32.Media.Audio.SpatialAudioHrtfDistanceDecayType
    MaxGain: Single
    MinGain: Single
    UnityGainDistance: Single
    CutoffDistance: Single
    _pack_ = 1
SpatialAudioHrtfDistanceDecayType = Int32
SpatialAudioHrtfDistanceDecay_NaturalDecay: win32more.Windows.Win32.Media.Audio.SpatialAudioHrtfDistanceDecayType = 0
SpatialAudioHrtfDistanceDecay_CustomDecay: win32more.Windows.Win32.Media.Audio.SpatialAudioHrtfDistanceDecayType = 1
SpatialAudioHrtfEnvironmentType = Int32
SpatialAudioHrtfEnvironment_Small: win32more.Windows.Win32.Media.Audio.SpatialAudioHrtfEnvironmentType = 0
SpatialAudioHrtfEnvironment_Medium: win32more.Windows.Win32.Media.Audio.SpatialAudioHrtfEnvironmentType = 1
SpatialAudioHrtfEnvironment_Large: win32more.Windows.Win32.Media.Audio.SpatialAudioHrtfEnvironmentType = 2
SpatialAudioHrtfEnvironment_Outdoors: win32more.Windows.Win32.Media.Audio.SpatialAudioHrtfEnvironmentType = 3
SpatialAudioHrtfEnvironment_Average: win32more.Windows.Win32.Media.Audio.SpatialAudioHrtfEnvironmentType = 4
SpatialAudioMetadataCopyMode = Int32
SpatialAudioMetadataCopy_Overwrite: win32more.Windows.Win32.Media.Audio.SpatialAudioMetadataCopyMode = 0
SpatialAudioMetadataCopy_Append: win32more.Windows.Win32.Media.Audio.SpatialAudioMetadataCopyMode = 1
SpatialAudioMetadataCopy_AppendMergeWithLast: win32more.Windows.Win32.Media.Audio.SpatialAudioMetadataCopyMode = 2
SpatialAudioMetadataCopy_AppendMergeWithFirst: win32more.Windows.Win32.Media.Audio.SpatialAudioMetadataCopyMode = 3
class SpatialAudioMetadataItemsInfo(Structure):
    FrameCount: UInt16
    ItemCount: UInt16
    MaxItemCount: UInt16
    MaxValueBufferLength: UInt32
    _pack_ = 1
SpatialAudioMetadataWriterOverflowMode = Int32
SpatialAudioMetadataWriterOverflow_Fail: win32more.Windows.Win32.Media.Audio.SpatialAudioMetadataWriterOverflowMode = 0
SpatialAudioMetadataWriterOverflow_MergeWithNew: win32more.Windows.Win32.Media.Audio.SpatialAudioMetadataWriterOverflowMode = 1
SpatialAudioMetadataWriterOverflow_MergeWithLast: win32more.Windows.Win32.Media.Audio.SpatialAudioMetadataWriterOverflowMode = 2
class SpatialAudioObjectRenderStreamActivationParams(Structure):
    ObjectFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)
    StaticObjectTypeMask: win32more.Windows.Win32.Media.Audio.AudioObjectType
    MinDynamicObjectCount: UInt32
    MaxDynamicObjectCount: UInt32
    Category: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY
    EventHandle: win32more.Windows.Win32.Foundation.HANDLE
    NotifyObject: win32more.Windows.Win32.Media.Audio.ISpatialAudioObjectRenderStreamNotify
    _pack_ = 1
class SpatialAudioObjectRenderStreamActivationParams2(Structure):
    ObjectFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)
    StaticObjectTypeMask: win32more.Windows.Win32.Media.Audio.AudioObjectType
    MinDynamicObjectCount: UInt32
    MaxDynamicObjectCount: UInt32
    Category: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY
    EventHandle: win32more.Windows.Win32.Foundation.HANDLE
    NotifyObject: win32more.Windows.Win32.Media.Audio.ISpatialAudioObjectRenderStreamNotify
    Options: win32more.Windows.Win32.Media.Audio.SPATIAL_AUDIO_STREAM_OPTIONS
    _pack_ = 1
class SpatialAudioObjectRenderStreamForMetadataActivationParams(Structure):
    ObjectFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)
    StaticObjectTypeMask: win32more.Windows.Win32.Media.Audio.AudioObjectType
    MinDynamicObjectCount: UInt32
    MaxDynamicObjectCount: UInt32
    Category: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY
    EventHandle: win32more.Windows.Win32.Foundation.HANDLE
    MetadataFormatId: Guid
    MaxMetadataItemCount: UInt16
    MetadataActivationParams: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)
    NotifyObject: win32more.Windows.Win32.Media.Audio.ISpatialAudioObjectRenderStreamNotify
    _pack_ = 1
class SpatialAudioObjectRenderStreamForMetadataActivationParams2(Structure):
    ObjectFormat: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)
    StaticObjectTypeMask: win32more.Windows.Win32.Media.Audio.AudioObjectType
    MinDynamicObjectCount: UInt32
    MaxDynamicObjectCount: UInt32
    Category: win32more.Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY
    EventHandle: win32more.Windows.Win32.Foundation.HANDLE
    MetadataFormatId: Guid
    MaxMetadataItemCount: UInt32
    MetadataActivationParams: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)
    NotifyObject: win32more.Windows.Win32.Media.Audio.ISpatialAudioObjectRenderStreamNotify
    Options: win32more.Windows.Win32.Media.Audio.SPATIAL_AUDIO_STREAM_OPTIONS
    _pack_ = 1
class VOLUMEWAVEFILTER(Structure):
    wfltr: win32more.Windows.Win32.Media.Audio.WAVEFILTER
    dwVolume: UInt32
    _pack_ = 1
class WAVEFILTER(Structure):
    cbStruct: UInt32
    dwFilterTag: UInt32
    fdwFilter: UInt32
    dwReserved: UInt32 * 5
    _pack_ = 1
class WAVEFORMAT(Structure):
    wFormatTag: UInt16
    nChannels: UInt16
    nSamplesPerSec: UInt32
    nAvgBytesPerSec: UInt32
    nBlockAlign: UInt16
    _pack_ = 1
class WAVEFORMATEX(Structure):
    wFormatTag: UInt16
    nChannels: UInt16
    nSamplesPerSec: UInt32
    nAvgBytesPerSec: UInt32
    nBlockAlign: UInt16
    wBitsPerSample: UInt16
    cbSize: UInt16
    _pack_ = 1
class WAVEFORMATEXTENSIBLE(Structure):
    Format: win32more.Windows.Win32.Media.Audio.WAVEFORMATEX
    Samples: _Samples_e__Union
    dwChannelMask: UInt32
    SubFormat: Guid
    _pack_ = 1
    class _Samples_e__Union(Union):
        wValidBitsPerSample: UInt16
        wSamplesPerBlock: UInt16
        wReserved: UInt16
        _pack_ = 1
class WAVEHDR(Structure):
    lpData: win32more.Windows.Win32.Foundation.PSTR
    dwBufferLength: UInt32
    dwBytesRecorded: UInt32
    dwUser: UIntPtr
    dwFlags: UInt32
    dwLoops: UInt32
    lpNext: POINTER(win32more.Windows.Win32.Media.Audio.WAVEHDR)
    reserved: UIntPtr
    _pack_ = 1
class WAVEINCAPS2A(Structure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: win32more.Windows.Win32.Foundation.CHAR * 32
    dwFormats: UInt32
    wChannels: UInt16
    wReserved1: UInt16
    ManufacturerGuid: Guid
    ProductGuid: Guid
    NameGuid: Guid
    _pack_ = 1
class WAVEINCAPS2W(Structure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Char * 32
    dwFormats: UInt32
    wChannels: UInt16
    wReserved1: UInt16
    ManufacturerGuid: Guid
    ProductGuid: Guid
    NameGuid: Guid
    _pack_ = 1
WAVEINCAPS2 = UnicodeAlias('WAVEINCAPS2W')
class WAVEINCAPSA(Structure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: win32more.Windows.Win32.Foundation.CHAR * 32
    dwFormats: UInt32
    wChannels: UInt16
    wReserved1: UInt16
    _pack_ = 1
class WAVEINCAPSW(Structure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Char * 32
    dwFormats: UInt32
    wChannels: UInt16
    wReserved1: UInt16
    _pack_ = 1
WAVEINCAPS = UnicodeAlias('WAVEINCAPSW')
class WAVEOUTCAPS2A(Structure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: win32more.Windows.Win32.Foundation.CHAR * 32
    dwFormats: UInt32
    wChannels: UInt16
    wReserved1: UInt16
    dwSupport: UInt32
    ManufacturerGuid: Guid
    ProductGuid: Guid
    NameGuid: Guid
    _pack_ = 1
class WAVEOUTCAPS2W(Structure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Char * 32
    dwFormats: UInt32
    wChannels: UInt16
    wReserved1: UInt16
    dwSupport: UInt32
    ManufacturerGuid: Guid
    ProductGuid: Guid
    NameGuid: Guid
    _pack_ = 1
WAVEOUTCAPS2 = UnicodeAlias('WAVEOUTCAPS2W')
class WAVEOUTCAPSA(Structure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: win32more.Windows.Win32.Foundation.CHAR * 32
    dwFormats: UInt32
    wChannels: UInt16
    wReserved1: UInt16
    dwSupport: UInt32
    _pack_ = 1
class WAVEOUTCAPSW(Structure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Char * 32
    dwFormats: UInt32
    wChannels: UInt16
    wReserved1: UInt16
    dwSupport: UInt32
    _pack_ = 1
WAVEOUTCAPS = UnicodeAlias('WAVEOUTCAPSW')
_AUDCLNT_BUFFERFLAGS = Int32
AUDCLNT_BUFFERFLAGS_DATA_DISCONTINUITY: win32more.Windows.Win32.Media.Audio._AUDCLNT_BUFFERFLAGS = 1
AUDCLNT_BUFFERFLAGS_SILENT: win32more.Windows.Win32.Media.Audio._AUDCLNT_BUFFERFLAGS = 2
AUDCLNT_BUFFERFLAGS_TIMESTAMP_ERROR: win32more.Windows.Win32.Media.Audio._AUDCLNT_BUFFERFLAGS = 4
class tACMFORMATDETAILSW(Structure):
    cbStruct: UInt32
    dwFormatIndex: UInt32
    dwFormatTag: UInt32
    fdwSupport: UInt32
    pwfx: POINTER(win32more.Windows.Win32.Media.Audio.WAVEFORMATEX)
    cbwfx: UInt32
    szFormat: Char * 128
    _pack_ = 1


make_ready(__name__)
