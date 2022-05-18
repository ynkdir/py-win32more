from win32more import *
import win32more.Foundation
import win32more.Media.Audio
import win32more.Media.Speech
import win32more.System.Com
import win32more.System.Com.Urlmon
import win32more.System.Registry

def __getattr__(name):
    module = globals()
    try:
        f = module[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    module[name] = f()
    return module[name]
def __dir__():
    return __all__
SP_LOW_CONFIDENCE = -1
SP_NORMAL_CONFIDENCE = 0
DEFAULT_WEIGHT = 1
SP_MAX_WORD_LENGTH = 128
SP_MAX_PRON_LENGTH = 384
SP_EMULATE_RESULT = 1073741824
SP_STREAMPOS_ASAP = 0
SP_STREAMPOS_REALTIME = -1
SPRP_NORMAL = 0
SP_MAX_LANGIDS = 20
SAPI_ERROR_BASE = 20480
Speech_Default_Weight = 1
Speech_Max_Word_Length = 128
Speech_Max_Pron_Length = 384
Speech_StreamPos_Asap = 0
Speech_StreamPos_RealTime = -1
SpeechAllElements = -1
SpNotifyTranslator = Guid('e2ae5372-5d40-11d2-960e-00c04f8ee628')
SpObjectTokenCategory = Guid('a910187f-0c7a-45ac-92cc-59edafb77b53')
SpObjectToken = Guid('ef411752-3736-4cb4-9c8c-8ef4ccb58efe')
SpResourceManager = Guid('96749373-3391-11d2-9ee3-00c04f797396')
SpStreamFormatConverter = Guid('7013943a-e2ec-11d2-a086-00c04f8ef9b5')
SpMMAudioEnum = Guid('ab1890a0-e91f-11d2-bb91-00c04f8ee6c0')
SpMMAudioIn = Guid('cf3d2e50-53f2-11d2-960c-00c04f8ee628')
SpMMAudioOut = Guid('a8c680eb-3d32-11d2-9ee7-00c04f797396')
SpStream = Guid('715d9c59-4442-11d2-9605-00c04f8ee628')
SpVoice = Guid('96749377-3391-11d2-9ee3-00c04f797396')
SpSharedRecoContext = Guid('47206204-5eca-11d2-960f-00c04f8ee628')
SpInprocRecognizer = Guid('41b89b6b-9399-11d2-9623-00c04f8ee628')
SpSharedRecognizer = Guid('3bee4890-4fe9-4a37-8c1e-5e7e12791c1f')
SpLexicon = Guid('0655e396-25d0-11d3-9c26-00c04f8ef87c')
SpUnCompressedLexicon = Guid('c9e37c15-df92-4727-85d6-72e5eeb6995a')
SpCompressedLexicon = Guid('90903716-2f42-11d3-9c26-00c04f8ef87c')
SpShortcut = Guid('0d722f1a-9fcf-4e62-96d8-6df8f01a26aa')
SpPhoneConverter = Guid('9185f743-1143-4c28-86b5-bff14f20e5c8')
SpPhoneticAlphabetConverter = Guid('4f414126-dfe3-4629-99ee-797978317ead')
SpNullPhoneConverter = Guid('455f24e9-7396-4a16-9715-7c0fdbe3efe3')
SpTextSelectionInformation = Guid('0f92030a-cbfd-4ab8-a164-ff5985547ff6')
SpPhraseInfoBuilder = Guid('c23fc28d-c55f-4720-8b32-91f73c2bd5d1')
SpAudioFormat = Guid('9ef96870-e160-4792-820d-48cf0649e4ec')
SpWaveFormatEx = Guid('c79a574c-63be-44b9-801f-283f87f898be')
SpInProcRecoContext = Guid('73ad6842-ace0-45e8-a4dd-8795881a2c2a')
SpCustomStream = Guid('8dbef13f-1948-4aa8-8cf0-048eebed95d8')
SpFileStream = Guid('947812b3-2ae1-4644-ba86-9e90ded7ec91')
SpMemoryStream = Guid('5fb7ef7d-dff4-468a-b6b7-2fcbd188f994')
SPDATAKEYLOCATION = Int32
SPDKL_DefaultLocation = 0
SPDKL_CurrentUser = 1
SPDKL_LocalMachine = 2
SPDKL_CurrentConfig = 5
SPSTREAMFORMAT = Int32
SPSF_Default = -1
SPSF_NoAssignedFormat = 0
SPSF_Text = 1
SPSF_NonStandardFormat = 2
SPSF_ExtendedAudioFormat = 3
SPSF_8kHz8BitMono = 4
SPSF_8kHz8BitStereo = 5
SPSF_8kHz16BitMono = 6
SPSF_8kHz16BitStereo = 7
SPSF_11kHz8BitMono = 8
SPSF_11kHz8BitStereo = 9
SPSF_11kHz16BitMono = 10
SPSF_11kHz16BitStereo = 11
SPSF_12kHz8BitMono = 12
SPSF_12kHz8BitStereo = 13
SPSF_12kHz16BitMono = 14
SPSF_12kHz16BitStereo = 15
SPSF_16kHz8BitMono = 16
SPSF_16kHz8BitStereo = 17
SPSF_16kHz16BitMono = 18
SPSF_16kHz16BitStereo = 19
SPSF_22kHz8BitMono = 20
SPSF_22kHz8BitStereo = 21
SPSF_22kHz16BitMono = 22
SPSF_22kHz16BitStereo = 23
SPSF_24kHz8BitMono = 24
SPSF_24kHz8BitStereo = 25
SPSF_24kHz16BitMono = 26
SPSF_24kHz16BitStereo = 27
SPSF_32kHz8BitMono = 28
SPSF_32kHz8BitStereo = 29
SPSF_32kHz16BitMono = 30
SPSF_32kHz16BitStereo = 31
SPSF_44kHz8BitMono = 32
SPSF_44kHz8BitStereo = 33
SPSF_44kHz16BitMono = 34
SPSF_44kHz16BitStereo = 35
SPSF_48kHz8BitMono = 36
SPSF_48kHz8BitStereo = 37
SPSF_48kHz16BitMono = 38
SPSF_48kHz16BitStereo = 39
SPSF_TrueSpeech_8kHz1BitMono = 40
SPSF_CCITT_ALaw_8kHzMono = 41
SPSF_CCITT_ALaw_8kHzStereo = 42
SPSF_CCITT_ALaw_11kHzMono = 43
SPSF_CCITT_ALaw_11kHzStereo = 44
SPSF_CCITT_ALaw_22kHzMono = 45
SPSF_CCITT_ALaw_22kHzStereo = 46
SPSF_CCITT_ALaw_44kHzMono = 47
SPSF_CCITT_ALaw_44kHzStereo = 48
SPSF_CCITT_uLaw_8kHzMono = 49
SPSF_CCITT_uLaw_8kHzStereo = 50
SPSF_CCITT_uLaw_11kHzMono = 51
SPSF_CCITT_uLaw_11kHzStereo = 52
SPSF_CCITT_uLaw_22kHzMono = 53
SPSF_CCITT_uLaw_22kHzStereo = 54
SPSF_CCITT_uLaw_44kHzMono = 55
SPSF_CCITT_uLaw_44kHzStereo = 56
SPSF_ADPCM_8kHzMono = 57
SPSF_ADPCM_8kHzStereo = 58
SPSF_ADPCM_11kHzMono = 59
SPSF_ADPCM_11kHzStereo = 60
SPSF_ADPCM_22kHzMono = 61
SPSF_ADPCM_22kHzStereo = 62
SPSF_ADPCM_44kHzMono = 63
SPSF_ADPCM_44kHzStereo = 64
SPSF_GSM610_8kHzMono = 65
SPSF_GSM610_11kHzMono = 66
SPSF_GSM610_22kHzMono = 67
SPSF_GSM610_44kHzMono = 68
SPSF_NUM_FORMATS = 69
def _define_ISpNotifyCallback_head():
    class ISpNotifyCallback(c_void_p):
        Guid = Guid(None)
    return ISpNotifyCallback
def _define_ISpNotifyCallback():
    ISpNotifyCallback = win32more.Media.Speech.ISpNotifyCallback_head
    ISpNotifyCallback.NotifyCallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM, use_last_error=False)(0, 'NotifyCallback', ((1, 'wParam'),(1, 'lParam'),)))
    return ISpNotifyCallback
def _define_SPNOTIFYCALLBACK():
    return CFUNCTYPE(Void,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM, use_last_error=False)
def _define_ISpNotifySource_head():
    class ISpNotifySource(win32more.System.Com.IUnknown_head):
        Guid = Guid('5eff4aef-8487-11d2-961c-00c04f8ee628')
    return ISpNotifySource
def _define_ISpNotifySource():
    ISpNotifySource = win32more.Media.Speech.ISpNotifySource_head
    ISpNotifySource.SetNotifySink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpNotifySink_head, use_last_error=False)(3, 'SetNotifySink', ((1, 'pNotifySink'),)))
    ISpNotifySource.SetNotifyWindowMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM, use_last_error=False)(4, 'SetNotifyWindowMessage', ((1, 'hWnd'),(1, 'Msg'),(1, 'wParam'),(1, 'lParam'),)))
    ISpNotifySource.SetNotifyCallbackFunction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPNOTIFYCALLBACK),win32more.Foundation.WPARAM,win32more.Foundation.LPARAM, use_last_error=False)(5, 'SetNotifyCallbackFunction', ((1, 'pfnCallback'),(1, 'wParam'),(1, 'lParam'),)))
    ISpNotifySource.SetNotifyCallbackInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpNotifyCallback_head,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM, use_last_error=False)(6, 'SetNotifyCallbackInterface', ((1, 'pSpCallback'),(1, 'wParam'),(1, 'lParam'),)))
    ISpNotifySource.SetNotifyWin32Event = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'SetNotifyWin32Event', ()))
    ISpNotifySource.WaitForNotifyEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(8, 'WaitForNotifyEvent', ((1, 'dwMilliseconds'),)))
    ISpNotifySource.GetNotifyEventHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HANDLE, use_last_error=False)(9, 'GetNotifyEventHandle', ()))
    return ISpNotifySource
def _define_ISpNotifySink_head():
    class ISpNotifySink(win32more.System.Com.IUnknown_head):
        Guid = Guid('259684dc-37c3-11d2-9603-00c04f8ee628')
    return ISpNotifySink
def _define_ISpNotifySink():
    ISpNotifySink = win32more.Media.Speech.ISpNotifySink_head
    ISpNotifySink.Notify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Notify', ()))
    return ISpNotifySink
def _define_ISpNotifyTranslator_head():
    class ISpNotifyTranslator(win32more.Media.Speech.ISpNotifySink_head):
        Guid = Guid('aca16614-5d3d-11d2-960e-00c04f8ee628')
    return ISpNotifyTranslator
def _define_ISpNotifyTranslator():
    ISpNotifyTranslator = win32more.Media.Speech.ISpNotifyTranslator_head
    ISpNotifyTranslator.InitWindowMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM, use_last_error=False)(4, 'InitWindowMessage', ((1, 'hWnd'),(1, 'Msg'),(1, 'wParam'),(1, 'lParam'),)))
    ISpNotifyTranslator.InitCallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPNOTIFYCALLBACK),win32more.Foundation.WPARAM,win32more.Foundation.LPARAM, use_last_error=False)(5, 'InitCallback', ((1, 'pfnCallback'),(1, 'wParam'),(1, 'lParam'),)))
    ISpNotifyTranslator.InitSpNotifyCallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpNotifyCallback_head,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM, use_last_error=False)(6, 'InitSpNotifyCallback', ((1, 'pSpCallback'),(1, 'wParam'),(1, 'lParam'),)))
    ISpNotifyTranslator.InitWin32Event = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,win32more.Foundation.BOOL, use_last_error=False)(7, 'InitWin32Event', ((1, 'hEvent'),(1, 'fCloseHandleOnRelease'),)))
    ISpNotifyTranslator.Wait = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(8, 'Wait', ((1, 'dwMilliseconds'),)))
    ISpNotifyTranslator.GetEventHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HANDLE, use_last_error=False)(9, 'GetEventHandle', ()))
    return ISpNotifyTranslator
def _define_ISpDataKey_head():
    class ISpDataKey(win32more.System.Com.IUnknown_head):
        Guid = Guid('14056581-e16c-11d2-bb90-00c04f8ee6c0')
    return ISpDataKey
def _define_ISpDataKey():
    ISpDataKey = win32more.Media.Speech.ISpDataKey_head
    ISpDataKey.SetData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,c_char_p_no, use_last_error=False)(3, 'SetData', ((1, 'pszValueName'),(1, 'cbData'),(1, 'pData'),)))
    ISpDataKey.GetData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32),c_char_p_no, use_last_error=False)(4, 'GetData', ((1, 'pszValueName'),(1, 'pcbData'),(1, 'pData'),)))
    ISpDataKey.SetStringValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(5, 'SetStringValue', ((1, 'pszValueName'),(1, 'pszValue'),)))
    ISpDataKey.GetStringValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(6, 'GetStringValue', ((1, 'pszValueName'),(1, 'ppszValue'),)))
    ISpDataKey.SetDWORD = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(7, 'SetDWORD', ((1, 'pszValueName'),(1, 'dwValue'),)))
    ISpDataKey.GetDWORD = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(8, 'GetDWORD', ((1, 'pszValueName'),(1, 'pdwValue'),)))
    ISpDataKey.OpenKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Media.Speech.ISpDataKey_head), use_last_error=False)(9, 'OpenKey', ((1, 'pszSubKeyName'),(1, 'ppSubKey'),)))
    ISpDataKey.CreateKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Media.Speech.ISpDataKey_head), use_last_error=False)(10, 'CreateKey', ((1, 'pszSubKey'),(1, 'ppSubKey'),)))
    ISpDataKey.DeleteKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(11, 'DeleteKey', ((1, 'pszSubKey'),)))
    ISpDataKey.DeleteValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(12, 'DeleteValue', ((1, 'pszValueName'),)))
    ISpDataKey.EnumKeys = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(13, 'EnumKeys', ((1, 'Index'),(1, 'ppszSubKeyName'),)))
    ISpDataKey.EnumValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(14, 'EnumValues', ((1, 'Index'),(1, 'ppszValueName'),)))
    return ISpDataKey
def _define_ISpRegDataKey_head():
    class ISpRegDataKey(win32more.Media.Speech.ISpDataKey_head):
        Guid = Guid('92a66e2b-c830-4149-83df-6fc2ba1e7a5b')
    return ISpRegDataKey
def _define_ISpRegDataKey():
    ISpRegDataKey = win32more.Media.Speech.ISpRegDataKey_head
    ISpRegDataKey.SetKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Registry.HKEY,win32more.Foundation.BOOL, use_last_error=False)(15, 'SetKey', ((1, 'hkey'),(1, 'fReadOnly'),)))
    return ISpRegDataKey
def _define_ISpObjectTokenCategory_head():
    class ISpObjectTokenCategory(win32more.Media.Speech.ISpDataKey_head):
        Guid = Guid('2d3d3845-39af-4850-bbf9-40b49780011d')
    return ISpObjectTokenCategory
def _define_ISpObjectTokenCategory():
    ISpObjectTokenCategory = win32more.Media.Speech.ISpObjectTokenCategory_head
    ISpObjectTokenCategory.SetId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=False)(15, 'SetId', ((1, 'pszCategoryId'),(1, 'fCreateIfNotExist'),)))
    ISpObjectTokenCategory.GetId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(16, 'GetId', ((1, 'ppszCoMemCategoryId'),)))
    ISpObjectTokenCategory.GetDataKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SPDATAKEYLOCATION,POINTER(win32more.Media.Speech.ISpDataKey_head), use_last_error=False)(17, 'GetDataKey', ((1, 'spdkl'),(1, 'ppDataKey'),)))
    ISpObjectTokenCategory.EnumTokens = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Media.Speech.IEnumSpObjectTokens_head), use_last_error=False)(18, 'EnumTokens', ((1, 'pzsReqAttribs'),(1, 'pszOptAttribs'),(1, 'ppEnum'),)))
    ISpObjectTokenCategory.SetDefaultTokenId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(19, 'SetDefaultTokenId', ((1, 'pszTokenId'),)))
    ISpObjectTokenCategory.GetDefaultTokenId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(20, 'GetDefaultTokenId', ((1, 'ppszCoMemTokenId'),)))
    return ISpObjectTokenCategory
def _define_ISpObjectToken_head():
    class ISpObjectToken(win32more.Media.Speech.ISpDataKey_head):
        Guid = Guid('14056589-e16c-11d2-bb90-00c04f8ee6c0')
    return ISpObjectToken
def _define_ISpObjectToken():
    ISpObjectToken = win32more.Media.Speech.ISpObjectToken_head
    ISpObjectToken.SetId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=False)(15, 'SetId', ((1, 'pszCategoryId'),(1, 'pszTokenId'),(1, 'fCreateIfNotExist'),)))
    ISpObjectToken.GetId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(16, 'GetId', ((1, 'ppszCoMemTokenId'),)))
    ISpObjectToken.GetCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpObjectTokenCategory_head), use_last_error=False)(17, 'GetCategory', ((1, 'ppTokenCategory'),)))
    ISpObjectToken.CreateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,UInt32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(18, 'CreateInstance', ((1, 'pUnkOuter'),(1, 'dwClsContext'),(1, 'riid'),(1, 'ppvObject'),)))
    ISpObjectToken.GetStorageFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(19, 'GetStorageFileName', ((1, 'clsidCaller'),(1, 'pszValueName'),(1, 'pszFileNameSpecifier'),(1, 'nFolder'),(1, 'ppszFilePath'),)))
    ISpObjectToken.RemoveStorageFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=False)(20, 'RemoveStorageFileName', ((1, 'clsidCaller'),(1, 'pszKeyName'),(1, 'fDeleteFile'),)))
    ISpObjectToken.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(21, 'Remove', ((1, 'pclsidCaller'),)))
    ISpObjectToken.IsUISupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,c_void_p,UInt32,win32more.System.Com.IUnknown_head,POINTER(win32more.Foundation.BOOL), use_last_error=False)(22, 'IsUISupported', ((1, 'pszTypeOfUI'),(1, 'pvExtraData'),(1, 'cbExtraData'),(1, 'punkObject'),(1, 'pfSupported'),)))
    ISpObjectToken.DisplayUI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_void_p,UInt32,win32more.System.Com.IUnknown_head, use_last_error=False)(23, 'DisplayUI', ((1, 'hwndParent'),(1, 'pszTitle'),(1, 'pszTypeOfUI'),(1, 'pvExtraData'),(1, 'cbExtraData'),(1, 'punkObject'),)))
    ISpObjectToken.MatchesAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BOOL), use_last_error=False)(24, 'MatchesAttributes', ((1, 'pszAttributes'),(1, 'pfMatches'),)))
    return ISpObjectToken
def _define_ISpObjectTokenInit_head():
    class ISpObjectTokenInit(win32more.Media.Speech.ISpObjectToken_head):
        Guid = Guid('b8aab0cf-346f-49d8-9499-c8b03f161d51')
    return ISpObjectTokenInit
def _define_ISpObjectTokenInit():
    ISpObjectTokenInit = win32more.Media.Speech.ISpObjectTokenInit_head
    ISpObjectTokenInit.InitFromDataKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Media.Speech.ISpDataKey_head, use_last_error=False)(25, 'InitFromDataKey', ((1, 'pszCategoryId'),(1, 'pszTokenId'),(1, 'pDataKey'),)))
    return ISpObjectTokenInit
def _define_IEnumSpObjectTokens_head():
    class IEnumSpObjectTokens(win32more.System.Com.IUnknown_head):
        Guid = Guid('06b64f9e-7fda-11d2-b4f2-00c04f797396')
    return IEnumSpObjectTokens
def _define_IEnumSpObjectTokens():
    IEnumSpObjectTokens = win32more.Media.Speech.IEnumSpObjectTokens_head
    IEnumSpObjectTokens.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.Speech.ISpObjectToken_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'pelt'),(1, 'pceltFetched'),)))
    IEnumSpObjectTokens.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'celt'),)))
    IEnumSpObjectTokens.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumSpObjectTokens.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.IEnumSpObjectTokens_head), use_last_error=False)(6, 'Clone', ((1, 'ppEnum'),)))
    IEnumSpObjectTokens.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.Speech.ISpObjectToken_head), use_last_error=False)(7, 'Item', ((1, 'Index'),(1, 'ppToken'),)))
    IEnumSpObjectTokens.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(8, 'GetCount', ((1, 'pCount'),)))
    return IEnumSpObjectTokens
def _define_ISpObjectWithToken_head():
    class ISpObjectWithToken(win32more.System.Com.IUnknown_head):
        Guid = Guid('5b559f40-e952-11d2-bb91-00c04f8ee6c0')
    return ISpObjectWithToken
def _define_ISpObjectWithToken():
    ISpObjectWithToken = win32more.Media.Speech.ISpObjectWithToken_head
    ISpObjectWithToken.SetObjectToken = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpObjectToken_head, use_last_error=False)(3, 'SetObjectToken', ((1, 'pToken'),)))
    ISpObjectWithToken.GetObjectToken = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpObjectToken_head), use_last_error=False)(4, 'GetObjectToken', ((1, 'ppToken'),)))
    return ISpObjectWithToken
def _define_ISpResourceManager_head():
    class ISpResourceManager(win32more.System.Com.IServiceProvider_head):
        Guid = Guid('93384e18-5014-43d5-adbb-a78e055926bd')
    return ISpResourceManager
def _define_ISpResourceManager():
    ISpResourceManager = win32more.Media.Speech.ISpResourceManager_head
    ISpResourceManager.SetObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head, use_last_error=False)(4, 'SetObject', ((1, 'guidServiceId'),(1, 'pUnkObject'),)))
    ISpResourceManager.GetObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(Guid),win32more.Foundation.BOOL,POINTER(c_void_p), use_last_error=False)(5, 'GetObject', ((1, 'guidServiceId'),(1, 'ObjectCLSID'),(1, 'ObjectIID'),(1, 'fReleaseWhenLastExternalRefReleased'),(1, 'ppObject'),)))
    return ISpResourceManager
SPEVENTLPARAMTYPE = Int32
SPET_LPARAM_IS_UNDEFINED = 0
SPET_LPARAM_IS_TOKEN = 1
SPET_LPARAM_IS_OBJECT = 2
SPET_LPARAM_IS_POINTER = 3
SPET_LPARAM_IS_STRING = 4
SPEVENTENUM = Int32
SPEI_UNDEFINED = 0
SPEI_START_INPUT_STREAM = 1
SPEI_END_INPUT_STREAM = 2
SPEI_VOICE_CHANGE = 3
SPEI_TTS_BOOKMARK = 4
SPEI_WORD_BOUNDARY = 5
SPEI_PHONEME = 6
SPEI_SENTENCE_BOUNDARY = 7
SPEI_VISEME = 8
SPEI_TTS_AUDIO_LEVEL = 9
SPEI_TTS_PRIVATE = 15
SPEI_MIN_TTS = 1
SPEI_MAX_TTS = 15
SPEI_END_SR_STREAM = 34
SPEI_SOUND_START = 35
SPEI_SOUND_END = 36
SPEI_PHRASE_START = 37
SPEI_RECOGNITION = 38
SPEI_HYPOTHESIS = 39
SPEI_SR_BOOKMARK = 40
SPEI_PROPERTY_NUM_CHANGE = 41
SPEI_PROPERTY_STRING_CHANGE = 42
SPEI_FALSE_RECOGNITION = 43
SPEI_INTERFERENCE = 44
SPEI_REQUEST_UI = 45
SPEI_RECO_STATE_CHANGE = 46
SPEI_ADAPTATION = 47
SPEI_START_SR_STREAM = 48
SPEI_RECO_OTHER_CONTEXT = 49
SPEI_SR_AUDIO_LEVEL = 50
SPEI_SR_RETAINEDAUDIO = 51
SPEI_SR_PRIVATE = 52
SPEI_RESERVED4 = 53
SPEI_RESERVED5 = 54
SPEI_RESERVED6 = 55
SPEI_MIN_SR = 34
SPEI_MAX_SR = 55
SPEI_RESERVED1 = 30
SPEI_RESERVED2 = 33
SPEI_RESERVED3 = 63
def _define_SPEVENT_head():
    class SPEVENT(Structure):
        pass
    return SPEVENT
def _define_SPEVENT():
    SPEVENT = win32more.Media.Speech.SPEVENT_head
    SPEVENT._fields_ = [
        ("_bitfield", Int32),
        ("ulStreamNum", UInt32),
        ("ullAudioStreamOffset", UInt64),
        ("wParam", win32more.Foundation.WPARAM),
        ("lParam", win32more.Foundation.LPARAM),
    ]
    return SPEVENT
def _define_SPSERIALIZEDEVENT_head():
    class SPSERIALIZEDEVENT(Structure):
        pass
    return SPSERIALIZEDEVENT
def _define_SPSERIALIZEDEVENT():
    SPSERIALIZEDEVENT = win32more.Media.Speech.SPSERIALIZEDEVENT_head
    SPSERIALIZEDEVENT._fields_ = [
        ("_bitfield", Int32),
        ("ulStreamNum", UInt32),
        ("ullAudioStreamOffset", UInt64),
        ("SerializedwParam", UInt32),
        ("SerializedlParam", Int32),
    ]
    return SPSERIALIZEDEVENT
def _define_SPSERIALIZEDEVENT64_head():
    class SPSERIALIZEDEVENT64(Structure):
        pass
    return SPSERIALIZEDEVENT64
def _define_SPSERIALIZEDEVENT64():
    SPSERIALIZEDEVENT64 = win32more.Media.Speech.SPSERIALIZEDEVENT64_head
    SPSERIALIZEDEVENT64._fields_ = [
        ("_bitfield", Int32),
        ("ulStreamNum", UInt32),
        ("ullAudioStreamOffset", UInt64),
        ("SerializedwParam", UInt64),
        ("SerializedlParam", Int64),
    ]
    return SPSERIALIZEDEVENT64
def _define_SPEVENTEX_head():
    class SPEVENTEX(Structure):
        pass
    return SPEVENTEX
def _define_SPEVENTEX():
    SPEVENTEX = win32more.Media.Speech.SPEVENTEX_head
    SPEVENTEX._fields_ = [
        ("_bitfield", Int32),
        ("ulStreamNum", UInt32),
        ("ullAudioStreamOffset", UInt64),
        ("wParam", win32more.Foundation.WPARAM),
        ("lParam", win32more.Foundation.LPARAM),
        ("ullAudioTimeOffset", UInt64),
    ]
    return SPEVENTEX
SPINTERFERENCE = Int32
SPINTERFERENCE_NONE = 0
SPINTERFERENCE_NOISE = 1
SPINTERFERENCE_NOSIGNAL = 2
SPINTERFERENCE_TOOLOUD = 3
SPINTERFERENCE_TOOQUIET = 4
SPINTERFERENCE_TOOFAST = 5
SPINTERFERENCE_TOOSLOW = 6
SPINTERFERENCE_LATENCY_WARNING = 7
SPINTERFERENCE_LATENCY_TRUNCATE_BEGIN = 8
SPINTERFERENCE_LATENCY_TRUNCATE_END = 9
SPENDSRSTREAMFLAGS = Int32
SPESF_NONE = 0
SPESF_STREAM_RELEASED = 1
SPESF_EMULATED = 2
SPVFEATURE = Int32
SPVFEATURE_STRESSED = 1
SPVFEATURE_EMPHASIS = 2
SPVISEMES = Int32
SP_VISEME_0 = 0
SP_VISEME_1 = 1
SP_VISEME_2 = 2
SP_VISEME_3 = 3
SP_VISEME_4 = 4
SP_VISEME_5 = 5
SP_VISEME_6 = 6
SP_VISEME_7 = 7
SP_VISEME_8 = 8
SP_VISEME_9 = 9
SP_VISEME_10 = 10
SP_VISEME_11 = 11
SP_VISEME_12 = 12
SP_VISEME_13 = 13
SP_VISEME_14 = 14
SP_VISEME_15 = 15
SP_VISEME_16 = 16
SP_VISEME_17 = 17
SP_VISEME_18 = 18
SP_VISEME_19 = 19
SP_VISEME_20 = 20
SP_VISEME_21 = 21
def _define_SPEVENTSOURCEINFO_head():
    class SPEVENTSOURCEINFO(Structure):
        pass
    return SPEVENTSOURCEINFO
def _define_SPEVENTSOURCEINFO():
    SPEVENTSOURCEINFO = win32more.Media.Speech.SPEVENTSOURCEINFO_head
    SPEVENTSOURCEINFO._fields_ = [
        ("ullEventInterest", UInt64),
        ("ullQueuedInterest", UInt64),
        ("ulCount", UInt32),
    ]
    return SPEVENTSOURCEINFO
def _define_ISpEventSource_head():
    class ISpEventSource(win32more.Media.Speech.ISpNotifySource_head):
        Guid = Guid('be7a9cce-5f9e-11d2-960f-00c04f8ee628')
    return ISpEventSource
def _define_ISpEventSource():
    ISpEventSource = win32more.Media.Speech.ISpEventSource_head
    ISpEventSource.SetInterest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,UInt64, use_last_error=False)(10, 'SetInterest', ((1, 'ullEventInterest'),(1, 'ullQueuedInterest'),)))
    ISpEventSource.GetEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.Speech.SPEVENT_head),POINTER(UInt32), use_last_error=False)(11, 'GetEvents', ((1, 'ulCount'),(1, 'pEventArray'),(1, 'pulFetched'),)))
    ISpEventSource.GetInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPEVENTSOURCEINFO_head), use_last_error=False)(12, 'GetInfo', ((1, 'pInfo'),)))
    return ISpEventSource
def _define_ISpEventSource2_head():
    class ISpEventSource2(win32more.Media.Speech.ISpEventSource_head):
        Guid = Guid('2373a435-6a4b-429e-a6ac-d4231a61975b')
    return ISpEventSource2
def _define_ISpEventSource2():
    ISpEventSource2 = win32more.Media.Speech.ISpEventSource2_head
    ISpEventSource2.GetEventsEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Media.Speech.SPEVENTEX_head),POINTER(UInt32), use_last_error=False)(13, 'GetEventsEx', ((1, 'ulCount'),(1, 'pEventArray'),(1, 'pulFetched'),)))
    return ISpEventSource2
def _define_ISpEventSink_head():
    class ISpEventSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('be7a9cc9-5f9e-11d2-960f-00c04f8ee628')
    return ISpEventSink
def _define_ISpEventSink():
    ISpEventSink = win32more.Media.Speech.ISpEventSink_head
    ISpEventSink.AddEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPEVENT_head),UInt32, use_last_error=False)(3, 'AddEvents', ((1, 'pEventArray'),(1, 'ulCount'),)))
    ISpEventSink.GetEventInterest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(4, 'GetEventInterest', ((1, 'pullEventInterest'),)))
    return ISpEventSink
def _define_ISpStreamFormat_head():
    class ISpStreamFormat(win32more.System.Com.IStream_head):
        Guid = Guid('bed530be-2606-4f4d-a1c0-54c5cda5566f')
    return ISpStreamFormat
def _define_ISpStreamFormat():
    ISpStreamFormat = win32more.Media.Speech.ISpStreamFormat_head
    ISpStreamFormat.GetFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(POINTER(win32more.Media.Audio.WAVEFORMATEX_head)), use_last_error=False)(14, 'GetFormat', ((1, 'pguidFormatId'),(1, 'ppCoMemWaveFormatEx'),)))
    return ISpStreamFormat
SPFILEMODE = Int32
SPFM_OPEN_READONLY = 0
SPFM_OPEN_READWRITE = 1
SPFM_CREATE = 2
SPFM_CREATE_ALWAYS = 3
SPFM_NUM_MODES = 4
def _define_ISpStream_head():
    class ISpStream(win32more.Media.Speech.ISpStreamFormat_head):
        Guid = Guid('12e3cca9-7518-44c5-a5e7-ba5a79cb929e')
    return ISpStream
def _define_ISpStream():
    ISpStream = win32more.Media.Speech.ISpStream_head
    ISpStream.SetBaseStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(Guid),POINTER(win32more.Media.Audio.WAVEFORMATEX_head), use_last_error=False)(15, 'SetBaseStream', ((1, 'pStream'),(1, 'rguidFormat'),(1, 'pWaveFormatEx'),)))
    ISpStream.GetBaseStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IStream_head), use_last_error=False)(16, 'GetBaseStream', ((1, 'ppStream'),)))
    ISpStream.BindToFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Media.Speech.SPFILEMODE,POINTER(Guid),POINTER(win32more.Media.Audio.WAVEFORMATEX_head),UInt64, use_last_error=False)(17, 'BindToFile', ((1, 'pszFileName'),(1, 'eMode'),(1, 'pFormatId'),(1, 'pWaveFormatEx'),(1, 'ullEventInterest'),)))
    ISpStream.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(18, 'Close', ()))
    return ISpStream
def _define_ISpStreamFormatConverter_head():
    class ISpStreamFormatConverter(win32more.Media.Speech.ISpStreamFormat_head):
        Guid = Guid('678a932c-ea71-4446-9b41-78fda6280a29')
    return ISpStreamFormatConverter
def _define_ISpStreamFormatConverter():
    ISpStreamFormatConverter = win32more.Media.Speech.ISpStreamFormatConverter_head
    ISpStreamFormatConverter.SetBaseStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpStreamFormat_head,win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=False)(15, 'SetBaseStream', ((1, 'pStream'),(1, 'fSetFormatToBaseStreamFormat'),(1, 'fWriteToBaseStream'),)))
    ISpStreamFormatConverter.GetBaseStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpStreamFormat_head), use_last_error=False)(16, 'GetBaseStream', ((1, 'ppStream'),)))
    ISpStreamFormatConverter.SetFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Media.Audio.WAVEFORMATEX_head), use_last_error=False)(17, 'SetFormat', ((1, 'rguidFormatIdOfConvertedStream'),(1, 'pWaveFormatExOfConvertedStream'),)))
    ISpStreamFormatConverter.ResetSeekPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(18, 'ResetSeekPosition', ()))
    ISpStreamFormatConverter.ScaleConvertedToBaseOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(UInt64), use_last_error=False)(19, 'ScaleConvertedToBaseOffset', ((1, 'ullOffsetConvertedStream'),(1, 'pullOffsetBaseStream'),)))
    ISpStreamFormatConverter.ScaleBaseToConvertedOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(UInt64), use_last_error=False)(20, 'ScaleBaseToConvertedOffset', ((1, 'ullOffsetBaseStream'),(1, 'pullOffsetConvertedStream'),)))
    return ISpStreamFormatConverter
SPAUDIOSTATE = Int32
SPAS_CLOSED = 0
SPAS_STOP = 1
SPAS_PAUSE = 2
SPAS_RUN = 3
def _define_SPAUDIOSTATUS_head():
    class SPAUDIOSTATUS(Structure):
        pass
    return SPAUDIOSTATUS
def _define_SPAUDIOSTATUS():
    SPAUDIOSTATUS = win32more.Media.Speech.SPAUDIOSTATUS_head
    SPAUDIOSTATUS._fields_ = [
        ("cbFreeBuffSpace", Int32),
        ("cbNonBlockingIO", UInt32),
        ("State", win32more.Media.Speech.SPAUDIOSTATE),
        ("CurSeekPos", UInt64),
        ("CurDevicePos", UInt64),
        ("dwAudioLevel", UInt32),
        ("dwReserved2", UInt32),
    ]
    return SPAUDIOSTATUS
def _define_SPAUDIOBUFFERINFO_head():
    class SPAUDIOBUFFERINFO(Structure):
        pass
    return SPAUDIOBUFFERINFO
def _define_SPAUDIOBUFFERINFO():
    SPAUDIOBUFFERINFO = win32more.Media.Speech.SPAUDIOBUFFERINFO_head
    SPAUDIOBUFFERINFO._fields_ = [
        ("ulMsMinNotification", UInt32),
        ("ulMsBufferSize", UInt32),
        ("ulMsEventBias", UInt32),
    ]
    return SPAUDIOBUFFERINFO
def _define_ISpAudio_head():
    class ISpAudio(win32more.Media.Speech.ISpStreamFormat_head):
        Guid = Guid('c05c768f-fae8-4ec2-8e07-338321c12452')
    return ISpAudio
def _define_ISpAudio():
    ISpAudio = win32more.Media.Speech.ISpAudio_head
    ISpAudio.SetState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SPAUDIOSTATE,UInt64, use_last_error=False)(15, 'SetState', ((1, 'NewState'),(1, 'ullReserved'),)))
    ISpAudio.SetFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Media.Audio.WAVEFORMATEX_head), use_last_error=False)(16, 'SetFormat', ((1, 'rguidFmtId'),(1, 'pWaveFormatEx'),)))
    ISpAudio.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPAUDIOSTATUS_head), use_last_error=False)(17, 'GetStatus', ((1, 'pStatus'),)))
    ISpAudio.SetBufferInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPAUDIOBUFFERINFO_head), use_last_error=False)(18, 'SetBufferInfo', ((1, 'pBuffInfo'),)))
    ISpAudio.GetBufferInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPAUDIOBUFFERINFO_head), use_last_error=False)(19, 'GetBufferInfo', ((1, 'pBuffInfo'),)))
    ISpAudio.GetDefaultFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(POINTER(win32more.Media.Audio.WAVEFORMATEX_head)), use_last_error=False)(20, 'GetDefaultFormat', ((1, 'pFormatId'),(1, 'ppCoMemWaveFormatEx'),)))
    ISpAudio.EventHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HANDLE, use_last_error=False)(21, 'EventHandle', ()))
    ISpAudio.GetVolumeLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(22, 'GetVolumeLevel', ((1, 'pLevel'),)))
    ISpAudio.SetVolumeLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(23, 'SetVolumeLevel', ((1, 'Level'),)))
    ISpAudio.GetBufferNotifySize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(24, 'GetBufferNotifySize', ((1, 'pcbSize'),)))
    ISpAudio.SetBufferNotifySize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(25, 'SetBufferNotifySize', ((1, 'cbSize'),)))
    return ISpAudio
def _define_ISpMMSysAudio_head():
    class ISpMMSysAudio(win32more.Media.Speech.ISpAudio_head):
        Guid = Guid('15806f6e-1d70-4b48-98e6-3b1a007509ab')
    return ISpMMSysAudio
def _define_ISpMMSysAudio():
    ISpMMSysAudio = win32more.Media.Speech.ISpMMSysAudio_head
    ISpMMSysAudio.GetDeviceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(26, 'GetDeviceId', ((1, 'puDeviceId'),)))
    ISpMMSysAudio.SetDeviceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(27, 'SetDeviceId', ((1, 'uDeviceId'),)))
    ISpMMSysAudio.GetMMHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_void_p), use_last_error=False)(28, 'GetMMHandle', ((1, 'pHandle'),)))
    ISpMMSysAudio.GetLineId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(29, 'GetLineId', ((1, 'puLineId'),)))
    ISpMMSysAudio.SetLineId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(30, 'SetLineId', ((1, 'uLineId'),)))
    return ISpMMSysAudio
def _define_ISpTranscript_head():
    class ISpTranscript(win32more.System.Com.IUnknown_head):
        Guid = Guid('10f63bce-201a-11d3-ac70-00c04f8ee6c0')
    return ISpTranscript
def _define_ISpTranscript():
    ISpTranscript = win32more.Media.Speech.ISpTranscript_head
    ISpTranscript.GetTranscript = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetTranscript', ((1, 'ppszTranscript'),)))
    ISpTranscript.AppendTranscript = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(4, 'AppendTranscript', ((1, 'pszTranscript'),)))
    return ISpTranscript
SPDISPLYATTRIBUTES = Int32
SPAF_ONE_TRAILING_SPACE = 2
SPAF_TWO_TRAILING_SPACES = 4
SPAF_CONSUME_LEADING_SPACES = 8
SPAF_BUFFER_POSITION = 16
SPAF_ALL = 31
SPAF_USER_SPECIFIED = 128
def _define_SPPHRASEELEMENT_head():
    class SPPHRASEELEMENT(Structure):
        pass
    return SPPHRASEELEMENT
def _define_SPPHRASEELEMENT():
    SPPHRASEELEMENT = win32more.Media.Speech.SPPHRASEELEMENT_head
    SPPHRASEELEMENT._fields_ = [
        ("ulAudioTimeOffset", UInt32),
        ("ulAudioSizeTime", UInt32),
        ("ulAudioStreamOffset", UInt32),
        ("ulAudioSizeBytes", UInt32),
        ("ulRetainedStreamOffset", UInt32),
        ("ulRetainedSizeBytes", UInt32),
        ("pszDisplayText", win32more.Foundation.PWSTR),
        ("pszLexicalForm", win32more.Foundation.PWSTR),
        ("pszPronunciation", POINTER(UInt16)),
        ("bDisplayAttributes", Byte),
        ("RequiredConfidence", SByte),
        ("ActualConfidence", SByte),
        ("Reserved", Byte),
        ("SREngineConfidence", Single),
    ]
    return SPPHRASEELEMENT
def _define_SPPHRASERULE_head():
    class SPPHRASERULE(Structure):
        pass
    return SPPHRASERULE
def _define_SPPHRASERULE():
    SPPHRASERULE = win32more.Media.Speech.SPPHRASERULE_head
    SPPHRASERULE._fields_ = [
        ("pszName", win32more.Foundation.PWSTR),
        ("ulId", UInt32),
        ("ulFirstElement", UInt32),
        ("ulCountOfElements", UInt32),
        ("pNextSibling", POINTER(win32more.Media.Speech.SPPHRASERULE_head)),
        ("pFirstChild", POINTER(win32more.Media.Speech.SPPHRASERULE_head)),
        ("SREngineConfidence", Single),
        ("Confidence", SByte),
    ]
    return SPPHRASERULE
SPPHRASEPROPERTYUNIONTYPE = Int32
SPPPUT_UNUSED = 0
SPPPUT_ARRAY_INDEX = 1
def _define_SPPHRASEPROPERTY_head():
    class SPPHRASEPROPERTY(Structure):
        pass
    return SPPHRASEPROPERTY
def _define_SPPHRASEPROPERTY():
    SPPHRASEPROPERTY = win32more.Media.Speech.SPPHRASEPROPERTY_head
    class SPPHRASEPROPERTY__Anonymous_e__Union(Union):
        pass
    class SPPHRASEPROPERTY__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    SPPHRASEPROPERTY__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("bType", Byte),
        ("bReserved", Byte),
        ("usArrayIndex", UInt16),
    ]
    SPPHRASEPROPERTY__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    SPPHRASEPROPERTY__Anonymous_e__Union._fields_ = [
        ("ulId", UInt32),
        ("Anonymous", SPPHRASEPROPERTY__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    SPPHRASEPROPERTY._anonymous_ = [
        'Anonymous',
    ]
    SPPHRASEPROPERTY._fields_ = [
        ("pszName", win32more.Foundation.PWSTR),
        ("Anonymous", SPPHRASEPROPERTY__Anonymous_e__Union),
        ("pszValue", win32more.Foundation.PWSTR),
        ("vValue", win32more.System.Com.VARIANT),
        ("ulFirstElement", UInt32),
        ("ulCountOfElements", UInt32),
        ("pNextSibling", POINTER(win32more.Media.Speech.SPPHRASEPROPERTY_head)),
        ("pFirstChild", POINTER(win32more.Media.Speech.SPPHRASEPROPERTY_head)),
        ("SREngineConfidence", Single),
        ("Confidence", SByte),
    ]
    return SPPHRASEPROPERTY
def _define_SPPHRASEREPLACEMENT_head():
    class SPPHRASEREPLACEMENT(Structure):
        pass
    return SPPHRASEREPLACEMENT
def _define_SPPHRASEREPLACEMENT():
    SPPHRASEREPLACEMENT = win32more.Media.Speech.SPPHRASEREPLACEMENT_head
    SPPHRASEREPLACEMENT._fields_ = [
        ("bDisplayAttributes", Byte),
        ("pszReplacementText", win32more.Foundation.PWSTR),
        ("ulFirstElement", UInt32),
        ("ulCountOfElements", UInt32),
    ]
    return SPPHRASEREPLACEMENT
def _define_SPSEMANTICERRORINFO_head():
    class SPSEMANTICERRORINFO(Structure):
        pass
    return SPSEMANTICERRORINFO
def _define_SPSEMANTICERRORINFO():
    SPSEMANTICERRORINFO = win32more.Media.Speech.SPSEMANTICERRORINFO_head
    SPSEMANTICERRORINFO._fields_ = [
        ("ulLineNumber", UInt32),
        ("pszScriptLine", win32more.Foundation.PWSTR),
        ("pszSource", win32more.Foundation.PWSTR),
        ("pszDescription", win32more.Foundation.PWSTR),
        ("hrResultCode", win32more.Foundation.HRESULT),
    ]
    return SPSEMANTICERRORINFO
SPSEMANTICFORMAT = Int32
SPSMF_SAPI_PROPERTIES = 0
SPSMF_SRGS_SEMANTICINTERPRETATION_MS = 1
SPSMF_SRGS_SAPIPROPERTIES = 2
SPSMF_UPS = 4
SPSMF_SRGS_SEMANTICINTERPRETATION_W3C = 8
def _define_SPPHRASE_50_head():
    class SPPHRASE_50(Structure):
        pass
    return SPPHRASE_50
def _define_SPPHRASE_50():
    SPPHRASE_50 = win32more.Media.Speech.SPPHRASE_50_head
    SPPHRASE_50._fields_ = [
        ("cbSize", UInt32),
        ("LangID", UInt16),
        ("wHomophoneGroupId", UInt16),
        ("ullGrammarID", UInt64),
        ("ftStartTime", UInt64),
        ("ullAudioStreamPosition", UInt64),
        ("ulAudioSizeBytes", UInt32),
        ("ulRetainedSizeBytes", UInt32),
        ("ulAudioSizeTime", UInt32),
        ("Rule", win32more.Media.Speech.SPPHRASERULE),
        ("pProperties", POINTER(win32more.Media.Speech.SPPHRASEPROPERTY_head)),
        ("pElements", POINTER(win32more.Media.Speech.SPPHRASEELEMENT_head)),
        ("cReplacements", UInt32),
        ("pReplacements", POINTER(win32more.Media.Speech.SPPHRASEREPLACEMENT_head)),
        ("SREngineID", Guid),
        ("ulSREnginePrivateDataSize", UInt32),
        ("pSREnginePrivateData", c_char_p_no),
    ]
    return SPPHRASE_50
def _define_SPPHRASE_head():
    class SPPHRASE(Structure):
        pass
    return SPPHRASE
def _define_SPPHRASE():
    SPPHRASE = win32more.Media.Speech.SPPHRASE_head
    SPPHRASE._fields_ = [
        ("__AnonymousBase_sapi53_L5821_C34", win32more.Media.Speech.SPPHRASE_50),
        ("pSML", win32more.Foundation.PWSTR),
        ("pSemanticErrorInfo", POINTER(win32more.Media.Speech.SPSEMANTICERRORINFO_head)),
    ]
    return SPPHRASE
def _define_SPSERIALIZEDPHRASE_head():
    class SPSERIALIZEDPHRASE(Structure):
        pass
    return SPSERIALIZEDPHRASE
def _define_SPSERIALIZEDPHRASE():
    SPSERIALIZEDPHRASE = win32more.Media.Speech.SPSERIALIZEDPHRASE_head
    SPSERIALIZEDPHRASE._fields_ = [
        ("ulSerializedSize", UInt32),
    ]
    return SPSERIALIZEDPHRASE
def _define_SPRULE_head():
    class SPRULE(Structure):
        pass
    return SPRULE
def _define_SPRULE():
    SPRULE = win32more.Media.Speech.SPRULE_head
    SPRULE._fields_ = [
        ("pszRuleName", win32more.Foundation.PWSTR),
        ("ulRuleId", UInt32),
        ("dwAttributes", UInt32),
    ]
    return SPRULE
SPVALUETYPE = Int32
SPDF_PROPERTY = 1
SPDF_REPLACEMENT = 2
SPDF_RULE = 4
SPDF_DISPLAYTEXT = 8
SPDF_LEXICALFORM = 16
SPDF_PRONUNCIATION = 32
SPDF_AUDIO = 64
SPDF_ALTERNATES = 128
SPDF_ALL = 255
def _define_SPBINARYGRAMMAR_head():
    class SPBINARYGRAMMAR(Structure):
        pass
    return SPBINARYGRAMMAR
def _define_SPBINARYGRAMMAR():
    SPBINARYGRAMMAR = win32more.Media.Speech.SPBINARYGRAMMAR_head
    SPBINARYGRAMMAR._fields_ = [
        ("ulTotalSerializedSize", UInt32),
    ]
    return SPBINARYGRAMMAR
SPPHRASERNG = Int32
SPPR_ALL_ELEMENTS = -1
def _define_SPSTATEHANDLE___head():
    class SPSTATEHANDLE__(Structure):
        pass
    return SPSTATEHANDLE__
def _define_SPSTATEHANDLE__():
    SPSTATEHANDLE__ = win32more.Media.Speech.SPSTATEHANDLE___head
    SPSTATEHANDLE__._fields_ = [
        ("unused", Int32),
    ]
    return SPSTATEHANDLE__
SPRECOEVENTFLAGS = Int32
SPREF_AutoPause = 1
SPREF_Emulated = 2
SPREF_SMLTimeout = 4
SPREF_ExtendableParse = 8
SPREF_ReSent = 16
SPREF_Hypothesis = 32
SPREF_FalseRecognition = 64
SPPARTOFSPEECH = Int32
SPPS_NotOverriden = -1
SPPS_Unknown = 0
SPPS_Noun = 4096
SPPS_Verb = 8192
SPPS_Modifier = 12288
SPPS_Function = 16384
SPPS_Interjection = 20480
SPPS_Noncontent = 24576
SPPS_LMA = 28672
SPPS_SuppressWord = 61440
SPLEXICONTYPE = Int32
eLEXTYPE_USER = 1
eLEXTYPE_APP = 2
eLEXTYPE_VENDORLEXICON = 4
eLEXTYPE_LETTERTOSOUND = 8
eLEXTYPE_MORPHOLOGY = 16
eLEXTYPE_RESERVED4 = 32
eLEXTYPE_USER_SHORTCUT = 64
eLEXTYPE_RESERVED6 = 128
eLEXTYPE_RESERVED7 = 256
eLEXTYPE_RESERVED8 = 512
eLEXTYPE_RESERVED9 = 1024
eLEXTYPE_RESERVED10 = 2048
eLEXTYPE_PRIVATE1 = 4096
eLEXTYPE_PRIVATE2 = 8192
eLEXTYPE_PRIVATE3 = 16384
eLEXTYPE_PRIVATE4 = 32768
eLEXTYPE_PRIVATE5 = 65536
eLEXTYPE_PRIVATE6 = 131072
eLEXTYPE_PRIVATE7 = 262144
eLEXTYPE_PRIVATE8 = 524288
eLEXTYPE_PRIVATE9 = 1048576
eLEXTYPE_PRIVATE10 = 2097152
eLEXTYPE_PRIVATE11 = 4194304
eLEXTYPE_PRIVATE12 = 8388608
eLEXTYPE_PRIVATE13 = 16777216
eLEXTYPE_PRIVATE14 = 33554432
eLEXTYPE_PRIVATE15 = 67108864
eLEXTYPE_PRIVATE16 = 134217728
eLEXTYPE_PRIVATE17 = 268435456
eLEXTYPE_PRIVATE18 = 536870912
eLEXTYPE_PRIVATE19 = 1073741824
eLEXTYPE_PRIVATE20 = -2147483648
SPWORDTYPE = Int32
eWORDTYPE_ADDED = 1
eWORDTYPE_DELETED = 2
SPPRONUNCIATIONFLAGS = Int32
ePRONFLAG_USED = 1
def _define_SPWORDPRONUNCIATION_head():
    class SPWORDPRONUNCIATION(Structure):
        pass
    return SPWORDPRONUNCIATION
def _define_SPWORDPRONUNCIATION():
    SPWORDPRONUNCIATION = win32more.Media.Speech.SPWORDPRONUNCIATION_head
    SPWORDPRONUNCIATION._fields_ = [
        ("pNextWordPronunciation", POINTER(win32more.Media.Speech.SPWORDPRONUNCIATION_head)),
        ("eLexiconType", win32more.Media.Speech.SPLEXICONTYPE),
        ("LangID", UInt16),
        ("wPronunciationFlags", UInt16),
        ("ePartOfSpeech", win32more.Media.Speech.SPPARTOFSPEECH),
        ("szPronunciation", UInt16 * 0),
    ]
    return SPWORDPRONUNCIATION
def _define_SPWORDPRONUNCIATIONLIST_head():
    class SPWORDPRONUNCIATIONLIST(Structure):
        pass
    return SPWORDPRONUNCIATIONLIST
def _define_SPWORDPRONUNCIATIONLIST():
    SPWORDPRONUNCIATIONLIST = win32more.Media.Speech.SPWORDPRONUNCIATIONLIST_head
    SPWORDPRONUNCIATIONLIST._fields_ = [
        ("ulSize", UInt32),
        ("pvBuffer", c_char_p_no),
        ("pFirstWordPronunciation", POINTER(win32more.Media.Speech.SPWORDPRONUNCIATION_head)),
    ]
    return SPWORDPRONUNCIATIONLIST
def _define_SPWORD_head():
    class SPWORD(Structure):
        pass
    return SPWORD
def _define_SPWORD():
    SPWORD = win32more.Media.Speech.SPWORD_head
    SPWORD._fields_ = [
        ("pNextWord", POINTER(win32more.Media.Speech.SPWORD_head)),
        ("LangID", UInt16),
        ("wReserved", UInt16),
        ("eWordType", win32more.Media.Speech.SPWORDTYPE),
        ("pszWord", win32more.Foundation.PWSTR),
        ("pFirstWordPronunciation", POINTER(win32more.Media.Speech.SPWORDPRONUNCIATION_head)),
    ]
    return SPWORD
def _define_SPWORDLIST_head():
    class SPWORDLIST(Structure):
        pass
    return SPWORDLIST
def _define_SPWORDLIST():
    SPWORDLIST = win32more.Media.Speech.SPWORDLIST_head
    SPWORDLIST._fields_ = [
        ("ulSize", UInt32),
        ("pvBuffer", c_char_p_no),
        ("pFirstWord", POINTER(win32more.Media.Speech.SPWORD_head)),
    ]
    return SPWORDLIST
def _define_ISpLexicon_head():
    class ISpLexicon(win32more.System.Com.IUnknown_head):
        Guid = Guid('da41a7c2-5383-4db2-916b-6c1719e3db58')
    return ISpLexicon
def _define_ISpLexicon():
    ISpLexicon = win32more.Media.Speech.ISpLexicon_head
    ISpLexicon.GetPronunciations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt16,UInt32,POINTER(win32more.Media.Speech.SPWORDPRONUNCIATIONLIST_head), use_last_error=False)(3, 'GetPronunciations', ((1, 'pszWord'),(1, 'LangID'),(1, 'dwFlags'),(1, 'pWordPronunciationList'),)))
    ISpLexicon.AddPronunciation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt16,win32more.Media.Speech.SPPARTOFSPEECH,POINTER(UInt16), use_last_error=False)(4, 'AddPronunciation', ((1, 'pszWord'),(1, 'LangID'),(1, 'ePartOfSpeech'),(1, 'pszPronunciation'),)))
    ISpLexicon.RemovePronunciation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt16,win32more.Media.Speech.SPPARTOFSPEECH,POINTER(UInt16), use_last_error=False)(5, 'RemovePronunciation', ((1, 'pszWord'),(1, 'LangID'),(1, 'ePartOfSpeech'),(1, 'pszPronunciation'),)))
    ISpLexicon.GetGeneration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'GetGeneration', ((1, 'pdwGeneration'),)))
    ISpLexicon.GetGenerationChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(win32more.Media.Speech.SPWORDLIST_head), use_last_error=False)(7, 'GetGenerationChange', ((1, 'dwFlags'),(1, 'pdwGeneration'),(1, 'pWordList'),)))
    ISpLexicon.GetWords = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.Media.Speech.SPWORDLIST_head), use_last_error=False)(8, 'GetWords', ((1, 'dwFlags'),(1, 'pdwGeneration'),(1, 'pdwCookie'),(1, 'pWordList'),)))
    return ISpLexicon
def _define_ISpContainerLexicon_head():
    class ISpContainerLexicon(win32more.Media.Speech.ISpLexicon_head):
        Guid = Guid('8565572f-c094-41cc-b56e-10bd9c3ff044')
    return ISpContainerLexicon
def _define_ISpContainerLexicon():
    ISpContainerLexicon = win32more.Media.Speech.ISpContainerLexicon_head
    ISpContainerLexicon.AddLexicon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpLexicon_head,UInt32, use_last_error=False)(9, 'AddLexicon', ((1, 'pAddLexicon'),(1, 'dwFlags'),)))
    return ISpContainerLexicon
SPSHORTCUTTYPE = Int32
SPSHT_NotOverriden = -1
SPSHT_Unknown = 0
SPSHT_EMAIL = 4096
SPSHT_OTHER = 8192
SPPS_RESERVED1 = 12288
SPPS_RESERVED2 = 16384
SPPS_RESERVED3 = 20480
SPPS_RESERVED4 = 61440
def _define_SPSHORTCUTPAIR_head():
    class SPSHORTCUTPAIR(Structure):
        pass
    return SPSHORTCUTPAIR
def _define_SPSHORTCUTPAIR():
    SPSHORTCUTPAIR = win32more.Media.Speech.SPSHORTCUTPAIR_head
    SPSHORTCUTPAIR._fields_ = [
        ("pNextSHORTCUTPAIR", POINTER(win32more.Media.Speech.SPSHORTCUTPAIR_head)),
        ("LangID", UInt16),
        ("shType", win32more.Media.Speech.SPSHORTCUTTYPE),
        ("pszDisplay", win32more.Foundation.PWSTR),
        ("pszSpoken", win32more.Foundation.PWSTR),
    ]
    return SPSHORTCUTPAIR
def _define_SPSHORTCUTPAIRLIST_head():
    class SPSHORTCUTPAIRLIST(Structure):
        pass
    return SPSHORTCUTPAIRLIST
def _define_SPSHORTCUTPAIRLIST():
    SPSHORTCUTPAIRLIST = win32more.Media.Speech.SPSHORTCUTPAIRLIST_head
    SPSHORTCUTPAIRLIST._fields_ = [
        ("ulSize", UInt32),
        ("pvBuffer", c_char_p_no),
        ("pFirstShortcutPair", POINTER(win32more.Media.Speech.SPSHORTCUTPAIR_head)),
    ]
    return SPSHORTCUTPAIRLIST
def _define_ISpShortcut_head():
    class ISpShortcut(win32more.System.Com.IUnknown_head):
        Guid = Guid('3df681e2-ea56-11d9-8bde-f66bad1e3f3a')
    return ISpShortcut
def _define_ISpShortcut():
    ISpShortcut = win32more.Media.Speech.ISpShortcut_head
    ISpShortcut.AddShortcut = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt16,win32more.Foundation.PWSTR,win32more.Media.Speech.SPSHORTCUTTYPE, use_last_error=False)(3, 'AddShortcut', ((1, 'pszDisplay'),(1, 'LangID'),(1, 'pszSpoken'),(1, 'shType'),)))
    ISpShortcut.RemoveShortcut = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt16,win32more.Foundation.PWSTR,win32more.Media.Speech.SPSHORTCUTTYPE, use_last_error=False)(4, 'RemoveShortcut', ((1, 'pszDisplay'),(1, 'LangID'),(1, 'pszSpoken'),(1, 'shType'),)))
    ISpShortcut.GetShortcuts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.Media.Speech.SPSHORTCUTPAIRLIST_head), use_last_error=False)(5, 'GetShortcuts', ((1, 'LangID'),(1, 'pShortcutpairList'),)))
    ISpShortcut.GetGeneration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'GetGeneration', ((1, 'pdwGeneration'),)))
    ISpShortcut.GetWordsFromGenerationChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.Media.Speech.SPWORDLIST_head), use_last_error=False)(7, 'GetWordsFromGenerationChange', ((1, 'pdwGeneration'),(1, 'pWordList'),)))
    ISpShortcut.GetWords = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.Media.Speech.SPWORDLIST_head), use_last_error=False)(8, 'GetWords', ((1, 'pdwGeneration'),(1, 'pdwCookie'),(1, 'pWordList'),)))
    ISpShortcut.GetShortcutsForGeneration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.Media.Speech.SPSHORTCUTPAIRLIST_head), use_last_error=False)(9, 'GetShortcutsForGeneration', ((1, 'pdwGeneration'),(1, 'pdwCookie'),(1, 'pShortcutpairList'),)))
    ISpShortcut.GetGenerationChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.Media.Speech.SPSHORTCUTPAIRLIST_head), use_last_error=False)(10, 'GetGenerationChange', ((1, 'pdwGeneration'),(1, 'pShortcutpairList'),)))
    return ISpShortcut
def _define_ISpPhoneConverter_head():
    class ISpPhoneConverter(win32more.Media.Speech.ISpObjectWithToken_head):
        Guid = Guid('8445c581-0cac-4a38-abfe-9b2ce2826455')
    return ISpPhoneConverter
def _define_ISpPhoneConverter():
    ISpPhoneConverter = win32more.Media.Speech.ISpPhoneConverter_head
    ISpPhoneConverter.PhoneToId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt16), use_last_error=False)(5, 'PhoneToId', ((1, 'pszPhone'),(1, 'pId'),)))
    ISpPhoneConverter.IdToPhone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),win32more.Foundation.PWSTR, use_last_error=False)(6, 'IdToPhone', ((1, 'pId'),(1, 'pszPhone'),)))
    return ISpPhoneConverter
def _define_ISpPhoneticAlphabetConverter_head():
    class ISpPhoneticAlphabetConverter(win32more.System.Com.IUnknown_head):
        Guid = Guid('133adcd4-19b4-4020-9fdc-842e78253b17')
    return ISpPhoneticAlphabetConverter
def _define_ISpPhoneticAlphabetConverter():
    ISpPhoneticAlphabetConverter = win32more.Media.Speech.ISpPhoneticAlphabetConverter_head
    ISpPhoneticAlphabetConverter.GetLangId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16), use_last_error=False)(3, 'GetLangId', ((1, 'pLangID'),)))
    ISpPhoneticAlphabetConverter.SetLangId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16, use_last_error=False)(4, 'SetLangId', ((1, 'LangID'),)))
    ISpPhoneticAlphabetConverter.SAPI2UPS = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),POINTER(UInt16),UInt32, use_last_error=False)(5, 'SAPI2UPS', ((1, 'pszSAPIId'),(1, 'pszUPSId'),(1, 'cMaxLength'),)))
    ISpPhoneticAlphabetConverter.UPS2SAPI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),POINTER(UInt16),UInt32, use_last_error=False)(6, 'UPS2SAPI', ((1, 'pszUPSId'),(1, 'pszSAPIId'),(1, 'cMaxLength'),)))
    ISpPhoneticAlphabetConverter.GetMaxConvertLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.BOOL,POINTER(UInt32), use_last_error=False)(7, 'GetMaxConvertLength', ((1, 'cSrcLength'),(1, 'bSAPI2UPS'),(1, 'pcMaxDestLength'),)))
    return ISpPhoneticAlphabetConverter
def _define_ISpPhoneticAlphabetSelection_head():
    class ISpPhoneticAlphabetSelection(win32more.System.Com.IUnknown_head):
        Guid = Guid('b2745efd-42ce-48ca-81f1-a96e02538a90')
    return ISpPhoneticAlphabetSelection
def _define_ISpPhoneticAlphabetSelection():
    ISpPhoneticAlphabetSelection = win32more.Media.Speech.ISpPhoneticAlphabetSelection_head
    ISpPhoneticAlphabetSelection.IsAlphabetUPS = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'IsAlphabetUPS', ((1, 'pfIsUPS'),)))
    ISpPhoneticAlphabetSelection.SetAlphabetToUPS = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(4, 'SetAlphabetToUPS', ((1, 'fForceUPS'),)))
    return ISpPhoneticAlphabetSelection
def _define_SPVPITCH_head():
    class SPVPITCH(Structure):
        pass
    return SPVPITCH
def _define_SPVPITCH():
    SPVPITCH = win32more.Media.Speech.SPVPITCH_head
    SPVPITCH._fields_ = [
        ("MiddleAdj", Int32),
        ("RangeAdj", Int32),
    ]
    return SPVPITCH
SPVACTIONS = Int32
SPVA_Speak = 0
SPVA_Silence = 1
SPVA_Pronounce = 2
SPVA_Bookmark = 3
SPVA_SpellOut = 4
SPVA_Section = 5
SPVA_ParseUnknownTag = 6
def _define_SPVCONTEXT_head():
    class SPVCONTEXT(Structure):
        pass
    return SPVCONTEXT
def _define_SPVCONTEXT():
    SPVCONTEXT = win32more.Media.Speech.SPVCONTEXT_head
    SPVCONTEXT._fields_ = [
        ("pCategory", win32more.Foundation.PWSTR),
        ("pBefore", win32more.Foundation.PWSTR),
        ("pAfter", win32more.Foundation.PWSTR),
    ]
    return SPVCONTEXT
def _define_SPVSTATE_head():
    class SPVSTATE(Structure):
        pass
    return SPVSTATE
def _define_SPVSTATE():
    SPVSTATE = win32more.Media.Speech.SPVSTATE_head
    SPVSTATE._fields_ = [
        ("eAction", win32more.Media.Speech.SPVACTIONS),
        ("LangID", UInt16),
        ("wReserved", UInt16),
        ("EmphAdj", Int32),
        ("RateAdj", Int32),
        ("Volume", UInt32),
        ("PitchAdj", win32more.Media.Speech.SPVPITCH),
        ("SilenceMSecs", UInt32),
        ("pPhoneIds", POINTER(UInt16)),
        ("ePartOfSpeech", win32more.Media.Speech.SPPARTOFSPEECH),
        ("Context", win32more.Media.Speech.SPVCONTEXT),
    ]
    return SPVSTATE
SPRUNSTATE = Int32
SPRS_DONE = 1
SPRS_IS_SPEAKING = 2
SPVLIMITS = Int32
SPMIN_VOLUME = 0
SPMAX_VOLUME = 100
SPMIN_RATE = -10
SPMAX_RATE = 10
SPVPRIORITY = Int32
SPVPRI_NORMAL = 0
SPVPRI_ALERT = 1
SPVPRI_OVER = 2
def _define_SPVOICESTATUS_head():
    class SPVOICESTATUS(Structure):
        pass
    return SPVOICESTATUS
def _define_SPVOICESTATUS():
    SPVOICESTATUS = win32more.Media.Speech.SPVOICESTATUS_head
    SPVOICESTATUS._fields_ = [
        ("ulCurrentStream", UInt32),
        ("ulLastStreamQueued", UInt32),
        ("hrLastResult", win32more.Foundation.HRESULT),
        ("dwRunningState", UInt32),
        ("ulInputWordPos", UInt32),
        ("ulInputWordLen", UInt32),
        ("ulInputSentPos", UInt32),
        ("ulInputSentLen", UInt32),
        ("lBookmarkId", Int32),
        ("PhonemeId", UInt16),
        ("VisemeId", win32more.Media.Speech.SPVISEMES),
        ("dwReserved1", UInt32),
        ("dwReserved2", UInt32),
    ]
    return SPVOICESTATUS
SPEAKFLAGS = Int32
SPF_DEFAULT = 0
SPF_ASYNC = 1
SPF_PURGEBEFORESPEAK = 2
SPF_IS_FILENAME = 4
SPF_IS_XML = 8
SPF_IS_NOT_XML = 16
SPF_PERSIST_XML = 32
SPF_NLP_SPEAK_PUNC = 64
SPF_PARSE_SAPI = 128
SPF_PARSE_SSML = 256
SPF_PARSE_AUTODETECT = 0
SPF_NLP_MASK = 64
SPF_PARSE_MASK = 384
SPF_VOICE_MASK = 511
SPF_UNUSED_FLAGS = -512
def _define_ISpVoice_head():
    class ISpVoice(win32more.Media.Speech.ISpEventSource_head):
        Guid = Guid('6c44df74-72b9-4992-a1ec-ef996e0422d4')
    return ISpVoice
def _define_ISpVoice():
    ISpVoice = win32more.Media.Speech.ISpVoice_head
    ISpVoice.SetOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.BOOL, use_last_error=False)(13, 'SetOutput', ((1, 'pUnkOutput'),(1, 'fAllowFormatChanges'),)))
    ISpVoice.GetOutputObjectToken = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpObjectToken_head), use_last_error=False)(14, 'GetOutputObjectToken', ((1, 'ppObjectToken'),)))
    ISpVoice.GetOutputStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpStreamFormat_head), use_last_error=False)(15, 'GetOutputStream', ((1, 'ppStream'),)))
    ISpVoice.Pause = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(16, 'Pause', ()))
    ISpVoice.Resume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(17, 'Resume', ()))
    ISpVoice.SetVoice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpObjectToken_head, use_last_error=False)(18, 'SetVoice', ((1, 'pToken'),)))
    ISpVoice.GetVoice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpObjectToken_head), use_last_error=False)(19, 'GetVoice', ((1, 'ppToken'),)))
    ISpVoice.Speak = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32), use_last_error=False)(20, 'Speak', ((1, 'pwcs'),(1, 'dwFlags'),(1, 'pulStreamNumber'),)))
    ISpVoice.SpeakStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,UInt32,POINTER(UInt32), use_last_error=False)(21, 'SpeakStream', ((1, 'pStream'),(1, 'dwFlags'),(1, 'pulStreamNumber'),)))
    ISpVoice.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPVOICESTATUS_head),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(22, 'GetStatus', ((1, 'pStatus'),(1, 'ppszLastBookmark'),)))
    ISpVoice.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Int32,POINTER(UInt32), use_last_error=False)(23, 'Skip', ((1, 'pItemType'),(1, 'lNumItems'),(1, 'pulNumSkipped'),)))
    ISpVoice.SetPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SPVPRIORITY, use_last_error=False)(24, 'SetPriority', ((1, 'ePriority'),)))
    ISpVoice.GetPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPVPRIORITY), use_last_error=False)(25, 'GetPriority', ((1, 'pePriority'),)))
    ISpVoice.SetAlertBoundary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SPEVENTENUM, use_last_error=False)(26, 'SetAlertBoundary', ((1, 'eBoundary'),)))
    ISpVoice.GetAlertBoundary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPEVENTENUM), use_last_error=False)(27, 'GetAlertBoundary', ((1, 'peBoundary'),)))
    ISpVoice.SetRate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(28, 'SetRate', ((1, 'RateAdjust'),)))
    ISpVoice.GetRate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(29, 'GetRate', ((1, 'pRateAdjust'),)))
    ISpVoice.SetVolume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16, use_last_error=False)(30, 'SetVolume', ((1, 'usVolume'),)))
    ISpVoice.GetVolume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16), use_last_error=False)(31, 'GetVolume', ((1, 'pusVolume'),)))
    ISpVoice.WaitUntilDone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(32, 'WaitUntilDone', ((1, 'msTimeout'),)))
    ISpVoice.SetSyncSpeakTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(33, 'SetSyncSpeakTimeout', ((1, 'msTimeout'),)))
    ISpVoice.GetSyncSpeakTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(34, 'GetSyncSpeakTimeout', ((1, 'pmsTimeout'),)))
    ISpVoice.SpeakCompleteEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HANDLE, use_last_error=False)(35, 'SpeakCompleteEvent', ()))
    ISpVoice.IsUISupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,c_void_p,UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(36, 'IsUISupported', ((1, 'pszTypeOfUI'),(1, 'pvExtraData'),(1, 'cbExtraData'),(1, 'pfSupported'),)))
    ISpVoice.DisplayUI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_void_p,UInt32, use_last_error=False)(37, 'DisplayUI', ((1, 'hwndParent'),(1, 'pszTitle'),(1, 'pszTypeOfUI'),(1, 'pvExtraData'),(1, 'cbExtraData'),)))
    return ISpVoice
def _define_ISpPhrase_head():
    class ISpPhrase(win32more.System.Com.IUnknown_head):
        Guid = Guid('1a5c0354-b621-4b5a-8791-d306ed379e53')
    return ISpPhrase
def _define_ISpPhrase():
    ISpPhrase = win32more.Media.Speech.ISpPhrase_head
    ISpPhrase.GetPhrase = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Media.Speech.SPPHRASE_head)), use_last_error=False)(3, 'GetPhrase', ((1, 'ppCoMemPhrase'),)))
    ISpPhrase.GetSerializedPhrase = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Media.Speech.SPSERIALIZEDPHRASE_head)), use_last_error=False)(4, 'GetSerializedPhrase', ((1, 'ppCoMemPhrase'),)))
    ISpPhrase.GetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Foundation.BOOL,POINTER(win32more.Foundation.PWSTR),c_char_p_no, use_last_error=False)(5, 'GetText', ((1, 'ulStart'),(1, 'ulCount'),(1, 'fUseTextReplacements'),(1, 'ppszCoMemText'),(1, 'pbDisplayAttributes'),)))
    ISpPhrase.Discard = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'Discard', ((1, 'dwValueTypes'),)))
    return ISpPhrase
def _define_ISpPhraseAlt_head():
    class ISpPhraseAlt(win32more.Media.Speech.ISpPhrase_head):
        Guid = Guid('8fcebc98-4e49-4067-9c6c-d86a0e092e3d')
    return ISpPhraseAlt
def _define_ISpPhraseAlt():
    ISpPhraseAlt = win32more.Media.Speech.ISpPhraseAlt_head
    ISpPhraseAlt.GetAltInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpPhrase_head),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(7, 'GetAltInfo', ((1, 'ppParent'),(1, 'pulStartElementInParent'),(1, 'pcElementsInParent'),(1, 'pcElementsInAlt'),)))
    ISpPhraseAlt.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Commit', ()))
    return ISpPhraseAlt
SPXMLRESULTOPTIONS = Int32
SPXRO_SML = 0
SPXRO_Alternates_SML = 1
def _define_ISpPhrase2_head():
    class ISpPhrase2(win32more.Media.Speech.ISpPhrase_head):
        Guid = Guid('f264da52-e457-4696-b856-a737b717af79')
    return ISpPhrase2
def _define_ISpPhrase2():
    ISpPhrase2 = win32more.Media.Speech.ISpPhrase2_head
    ISpPhrase2.GetXMLResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),win32more.Media.Speech.SPXMLRESULTOPTIONS, use_last_error=False)(7, 'GetXMLResult', ((1, 'ppszCoMemXMLResult'),(1, 'Options'),)))
    ISpPhrase2.GetXMLErrorInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPSEMANTICERRORINFO_head), use_last_error=False)(8, 'GetXMLErrorInfo', ((1, 'pSemanticErrorInfo'),)))
    ISpPhrase2.GetAudio = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Media.Speech.ISpStreamFormat_head), use_last_error=False)(9, 'GetAudio', ((1, 'ulStartElement'),(1, 'cElements'),(1, 'ppStream'),)))
    return ISpPhrase2
def _define_SPRECORESULTTIMES_head():
    class SPRECORESULTTIMES(Structure):
        pass
    return SPRECORESULTTIMES
def _define_SPRECORESULTTIMES():
    SPRECORESULTTIMES = win32more.Media.Speech.SPRECORESULTTIMES_head
    SPRECORESULTTIMES._fields_ = [
        ("ftStreamTime", win32more.Foundation.FILETIME),
        ("ullLength", UInt64),
        ("dwTickCount", UInt32),
        ("ullStart", UInt64),
    ]
    return SPRECORESULTTIMES
def _define_SPSERIALIZEDRESULT_head():
    class SPSERIALIZEDRESULT(Structure):
        pass
    return SPSERIALIZEDRESULT
def _define_SPSERIALIZEDRESULT():
    SPSERIALIZEDRESULT = win32more.Media.Speech.SPSERIALIZEDRESULT_head
    SPSERIALIZEDRESULT._fields_ = [
        ("ulSerializedSize", UInt32),
    ]
    return SPSERIALIZEDRESULT
def _define_ISpRecoResult_head():
    class ISpRecoResult(win32more.Media.Speech.ISpPhrase_head):
        Guid = Guid('20b053be-e235-43cd-9a2a-8d17a48b7842')
    return ISpRecoResult
def _define_ISpRecoResult():
    ISpRecoResult = win32more.Media.Speech.ISpRecoResult_head
    ISpRecoResult.GetResultTimes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPRECORESULTTIMES_head), use_last_error=False)(7, 'GetResultTimes', ((1, 'pTimes'),)))
    ISpRecoResult.GetAlternates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,POINTER(win32more.Media.Speech.ISpPhraseAlt_head),POINTER(UInt32), use_last_error=False)(8, 'GetAlternates', ((1, 'ulStartElement'),(1, 'cElements'),(1, 'ulRequestCount'),(1, 'ppPhrases'),(1, 'pcPhrasesReturned'),)))
    ISpRecoResult.GetAudio = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Media.Speech.ISpStreamFormat_head), use_last_error=False)(9, 'GetAudio', ((1, 'ulStartElement'),(1, 'cElements'),(1, 'ppStream'),)))
    ISpRecoResult.SpeakAudio = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,POINTER(UInt32), use_last_error=False)(10, 'SpeakAudio', ((1, 'ulStartElement'),(1, 'cElements'),(1, 'dwFlags'),(1, 'pulStreamNumber'),)))
    ISpRecoResult.Serialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Media.Speech.SPSERIALIZEDRESULT_head)), use_last_error=False)(11, 'Serialize', ((1, 'ppCoMemSerializedResult'),)))
    ISpRecoResult.ScaleAudio = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Media.Audio.WAVEFORMATEX_head), use_last_error=False)(12, 'ScaleAudio', ((1, 'pAudioFormatId'),(1, 'pWaveFormatEx'),)))
    ISpRecoResult.GetRecoContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpRecoContext_head), use_last_error=False)(13, 'GetRecoContext', ((1, 'ppRecoContext'),)))
    return ISpRecoResult
SPCOMMITFLAGS = Int32
SPCF_NONE = 0
SPCF_ADD_TO_USER_LEXICON = 1
SPCF_DEFINITE_CORRECTION = 2
def _define_ISpRecoResult2_head():
    class ISpRecoResult2(win32more.Media.Speech.ISpRecoResult_head):
        Guid = Guid('27cac6c4-88f2-41f2-8817-0c95e59f1e6e')
    return ISpRecoResult2
def _define_ISpRecoResult2():
    ISpRecoResult2 = win32more.Media.Speech.ISpRecoResult2_head
    ISpRecoResult2.CommitAlternate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpPhraseAlt_head,POINTER(win32more.Media.Speech.ISpRecoResult_head), use_last_error=False)(14, 'CommitAlternate', ((1, 'pPhraseAlt'),(1, 'ppNewResult'),)))
    ISpRecoResult2.CommitText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(15, 'CommitText', ((1, 'ulStartElement'),(1, 'cElements'),(1, 'pszCorrectedData'),(1, 'eCommitFlags'),)))
    ISpRecoResult2.SetTextFeedback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=False)(16, 'SetTextFeedback', ((1, 'pszFeedback'),(1, 'fSuccessful'),)))
    return ISpRecoResult2
def _define_ISpXMLRecoResult_head():
    class ISpXMLRecoResult(win32more.Media.Speech.ISpRecoResult_head):
        Guid = Guid('ae39362b-45a8-4074-9b9e-ccf49aa2d0b6')
    return ISpXMLRecoResult
def _define_ISpXMLRecoResult():
    ISpXMLRecoResult = win32more.Media.Speech.ISpXMLRecoResult_head
    ISpXMLRecoResult.GetXMLResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),win32more.Media.Speech.SPXMLRESULTOPTIONS, use_last_error=False)(14, 'GetXMLResult', ((1, 'ppszCoMemXMLResult'),(1, 'Options'),)))
    ISpXMLRecoResult.GetXMLErrorInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPSEMANTICERRORINFO_head), use_last_error=False)(15, 'GetXMLErrorInfo', ((1, 'pSemanticErrorInfo'),)))
    return ISpXMLRecoResult
def _define_SPTEXTSELECTIONINFO_head():
    class SPTEXTSELECTIONINFO(Structure):
        pass
    return SPTEXTSELECTIONINFO
def _define_SPTEXTSELECTIONINFO():
    SPTEXTSELECTIONINFO = win32more.Media.Speech.SPTEXTSELECTIONINFO_head
    SPTEXTSELECTIONINFO._fields_ = [
        ("ulStartActiveOffset", UInt32),
        ("cchActiveChars", UInt32),
        ("ulStartSelection", UInt32),
        ("cchSelection", UInt32),
    ]
    return SPTEXTSELECTIONINFO
SPWORDPRONOUNCEABLE = Int32
SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE = 0
SPWP_UNKNOWN_WORD_PRONOUNCEABLE = 1
SPWP_KNOWN_WORD_PRONOUNCEABLE = 2
SPGRAMMARSTATE = Int32
SPGS_DISABLED = 0
SPGS_ENABLED = 1
SPGS_EXCLUSIVE = 3
SPCONTEXTSTATE = Int32
SPCS_DISABLED = 0
SPCS_ENABLED = 1
SPRULESTATE = Int32
SPRS_INACTIVE = 0
SPRS_ACTIVE = 1
SPRS_ACTIVE_WITH_AUTO_PAUSE = 3
SPRS_ACTIVE_USER_DELIMITED = 4
SPGRAMMARWORDTYPE = Int32
SPWT_DISPLAY = 0
SPWT_LEXICAL = 1
SPWT_PRONUNCIATION = 2
SPWT_LEXICAL_NO_SPECIAL_CHARS = 3
def _define_SPPROPERTYINFO_head():
    class SPPROPERTYINFO(Structure):
        pass
    return SPPROPERTYINFO
def _define_SPPROPERTYINFO():
    SPPROPERTYINFO = win32more.Media.Speech.SPPROPERTYINFO_head
    SPPROPERTYINFO._fields_ = [
        ("pszName", win32more.Foundation.PWSTR),
        ("ulId", UInt32),
        ("pszValue", win32more.Foundation.PWSTR),
        ("vValue", win32more.System.Com.VARIANT),
    ]
    return SPPROPERTYINFO
SPCFGRULEATTRIBUTES = Int32
SPRAF_TopLevel = 1
SPRAF_Active = 2
SPRAF_Export = 4
SPRAF_Import = 8
SPRAF_Interpreter = 16
SPRAF_Dynamic = 32
SPRAF_Root = 64
SPRAF_AutoPause = 65536
SPRAF_UserDelimited = 131072
def _define_ISpGrammarBuilder_head():
    class ISpGrammarBuilder(win32more.System.Com.IUnknown_head):
        Guid = Guid('8137828f-591a-4a42-be58-49ea7ebaac68')
    return ISpGrammarBuilder
def _define_ISpGrammarBuilder():
    ISpGrammarBuilder = win32more.Media.Speech.ISpGrammarBuilder_head
    ISpGrammarBuilder.ResetGrammar = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16, use_last_error=False)(3, 'ResetGrammar', ((1, 'NewLanguage'),)))
    ISpGrammarBuilder.GetRule = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,win32more.Foundation.BOOL,POINTER(POINTER(win32more.Media.Speech.SPSTATEHANDLE___head)), use_last_error=False)(4, 'GetRule', ((1, 'pszRuleName'),(1, 'dwRuleId'),(1, 'dwAttributes'),(1, 'fCreateIfNotExist'),(1, 'phInitialState'),)))
    ISpGrammarBuilder.ClearRule = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPSTATEHANDLE___head), use_last_error=False)(5, 'ClearRule', ((1, 'hState'),)))
    ISpGrammarBuilder.CreateNewState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPSTATEHANDLE___head),POINTER(POINTER(win32more.Media.Speech.SPSTATEHANDLE___head)), use_last_error=False)(6, 'CreateNewState', ((1, 'hState'),(1, 'phState'),)))
    ISpGrammarBuilder.AddWordTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPSTATEHANDLE___head),POINTER(win32more.Media.Speech.SPSTATEHANDLE___head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Media.Speech.SPGRAMMARWORDTYPE,Single,POINTER(win32more.Media.Speech.SPPROPERTYINFO_head), use_last_error=False)(7, 'AddWordTransition', ((1, 'hFromState'),(1, 'hToState'),(1, 'psz'),(1, 'pszSeparators'),(1, 'eWordType'),(1, 'Weight'),(1, 'pPropInfo'),)))
    ISpGrammarBuilder.AddRuleTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPSTATEHANDLE___head),POINTER(win32more.Media.Speech.SPSTATEHANDLE___head),POINTER(win32more.Media.Speech.SPSTATEHANDLE___head),Single,POINTER(win32more.Media.Speech.SPPROPERTYINFO_head), use_last_error=False)(8, 'AddRuleTransition', ((1, 'hFromState'),(1, 'hToState'),(1, 'hRule'),(1, 'Weight'),(1, 'pPropInfo'),)))
    ISpGrammarBuilder.AddResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPSTATEHANDLE___head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(9, 'AddResource', ((1, 'hRuleState'),(1, 'pszResourceName'),(1, 'pszResourceValue'),)))
    ISpGrammarBuilder.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(10, 'Commit', ((1, 'dwReserved'),)))
    return ISpGrammarBuilder
SPLOADOPTIONS = Int32
SPLO_STATIC = 0
SPLO_DYNAMIC = 1
def _define_ISpRecoGrammar_head():
    class ISpRecoGrammar(win32more.Media.Speech.ISpGrammarBuilder_head):
        Guid = Guid('2177db29-7f45-47d0-8554-067e91c80502')
    return ISpRecoGrammar
def _define_ISpRecoGrammar():
    ISpRecoGrammar = win32more.Media.Speech.ISpRecoGrammar_head
    ISpRecoGrammar.GetGrammarId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(11, 'GetGrammarId', ((1, 'pullGrammarId'),)))
    ISpRecoGrammar.GetRecoContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpRecoContext_head), use_last_error=False)(12, 'GetRecoContext', ((1, 'ppRecoCtxt'),)))
    ISpRecoGrammar.LoadCmdFromFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Media.Speech.SPLOADOPTIONS, use_last_error=False)(13, 'LoadCmdFromFile', ((1, 'pszFileName'),(1, 'Options'),)))
    ISpRecoGrammar.LoadCmdFromObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PWSTR,win32more.Media.Speech.SPLOADOPTIONS, use_last_error=False)(14, 'LoadCmdFromObject', ((1, 'rcid'),(1, 'pszGrammarName'),(1, 'Options'),)))
    ISpRecoGrammar.LoadCmdFromResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt16,win32more.Media.Speech.SPLOADOPTIONS, use_last_error=False)(15, 'LoadCmdFromResource', ((1, 'hModule'),(1, 'pszResourceName'),(1, 'pszResourceType'),(1, 'wLanguage'),(1, 'Options'),)))
    ISpRecoGrammar.LoadCmdFromMemory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPBINARYGRAMMAR_head),win32more.Media.Speech.SPLOADOPTIONS, use_last_error=False)(16, 'LoadCmdFromMemory', ((1, 'pGrammar'),(1, 'Options'),)))
    ISpRecoGrammar.LoadCmdFromProprietaryGrammar = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PWSTR,c_void_p,UInt32,win32more.Media.Speech.SPLOADOPTIONS, use_last_error=False)(17, 'LoadCmdFromProprietaryGrammar', ((1, 'rguidParam'),(1, 'pszStringParam'),(1, 'pvDataPrarm'),(1, 'cbDataSize'),(1, 'Options'),)))
    ISpRecoGrammar.SetRuleState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,c_void_p,win32more.Media.Speech.SPRULESTATE, use_last_error=False)(18, 'SetRuleState', ((1, 'pszName'),(1, 'pReserved'),(1, 'NewState'),)))
    ISpRecoGrammar.SetRuleIdState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Media.Speech.SPRULESTATE, use_last_error=False)(19, 'SetRuleIdState', ((1, 'ulRuleId'),(1, 'NewState'),)))
    ISpRecoGrammar.LoadDictation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Media.Speech.SPLOADOPTIONS, use_last_error=False)(20, 'LoadDictation', ((1, 'pszTopicName'),(1, 'Options'),)))
    ISpRecoGrammar.UnloadDictation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(21, 'UnloadDictation', ()))
    ISpRecoGrammar.SetDictationState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SPRULESTATE, use_last_error=False)(22, 'SetDictationState', ((1, 'NewState'),)))
    ISpRecoGrammar.SetWordSequenceData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32,POINTER(win32more.Media.Speech.SPTEXTSELECTIONINFO_head), use_last_error=False)(23, 'SetWordSequenceData', ((1, 'pText'),(1, 'cchText'),(1, 'pInfo'),)))
    ISpRecoGrammar.SetTextSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPTEXTSELECTIONINFO_head), use_last_error=False)(24, 'SetTextSelection', ((1, 'pInfo'),)))
    ISpRecoGrammar.IsPronounceable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Media.Speech.SPWORDPRONOUNCEABLE), use_last_error=False)(25, 'IsPronounceable', ((1, 'pszWord'),(1, 'pWordPronounceable'),)))
    ISpRecoGrammar.SetGrammarState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SPGRAMMARSTATE, use_last_error=False)(26, 'SetGrammarState', ((1, 'eGrammarState'),)))
    ISpRecoGrammar.SaveCmd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(27, 'SaveCmd', ((1, 'pStream'),(1, 'ppszCoMemErrorText'),)))
    ISpRecoGrammar.GetGrammarState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPGRAMMARSTATE), use_last_error=False)(28, 'GetGrammarState', ((1, 'peGrammarState'),)))
    return ISpRecoGrammar
SPMATCHINGMODE = Int32
SPMATCHINGMODE_AllWords = 0
SPMATCHINGMODE_Subsequence = 1
SPMATCHINGMODE_OrderedSubset = 3
SPMATCHINGMODE_SubsequenceContentRequired = 5
SPMATCHINGMODE_OrderedSubsetContentRequired = 7
PHONETICALPHABET = Int32
PA_Ipa = 0
PA_Ups = 1
PA_Sapi = 2
def _define_ISpGrammarBuilder2_head():
    class ISpGrammarBuilder2(win32more.System.Com.IUnknown_head):
        Guid = Guid('8ab10026-20cc-4b20-8c22-a49c9ba78f60')
    return ISpGrammarBuilder2
def _define_ISpGrammarBuilder2():
    ISpGrammarBuilder2 = win32more.Media.Speech.ISpGrammarBuilder2_head
    ISpGrammarBuilder2.AddTextSubset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPSTATEHANDLE___head),POINTER(win32more.Media.Speech.SPSTATEHANDLE___head),win32more.Foundation.PWSTR,win32more.Media.Speech.SPMATCHINGMODE, use_last_error=False)(3, 'AddTextSubset', ((1, 'hFromState'),(1, 'hToState'),(1, 'psz'),(1, 'eMatchMode'),)))
    ISpGrammarBuilder2.SetPhoneticAlphabet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.PHONETICALPHABET, use_last_error=False)(4, 'SetPhoneticAlphabet', ((1, 'phoneticALphabet'),)))
    return ISpGrammarBuilder2
def _define_ISpRecoGrammar2_head():
    class ISpRecoGrammar2(win32more.System.Com.IUnknown_head):
        Guid = Guid('4b37bc9e-9ed6-44a3-93d3-18f022b79ec3')
    return ISpRecoGrammar2
def _define_ISpRecoGrammar2():
    ISpRecoGrammar2 = win32more.Media.Speech.ISpRecoGrammar2_head
    ISpRecoGrammar2.GetRules = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Media.Speech.SPRULE_head)),POINTER(UInt32), use_last_error=False)(3, 'GetRules', ((1, 'ppCoMemRules'),(1, 'puNumRules'),)))
    ISpRecoGrammar2.LoadCmdFromFile2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Media.Speech.SPLOADOPTIONS,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(4, 'LoadCmdFromFile2', ((1, 'pszFileName'),(1, 'Options'),(1, 'pszSharingUri'),(1, 'pszBaseUri'),)))
    ISpRecoGrammar2.LoadCmdFromMemory2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPBINARYGRAMMAR_head),win32more.Media.Speech.SPLOADOPTIONS,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(5, 'LoadCmdFromMemory2', ((1, 'pGrammar'),(1, 'Options'),(1, 'pszSharingUri'),(1, 'pszBaseUri'),)))
    ISpRecoGrammar2.SetRulePriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,Int32, use_last_error=False)(6, 'SetRulePriority', ((1, 'pszRuleName'),(1, 'ulRuleId'),(1, 'nRulePriority'),)))
    ISpRecoGrammar2.SetRuleWeight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,Single, use_last_error=False)(7, 'SetRuleWeight', ((1, 'pszRuleName'),(1, 'ulRuleId'),(1, 'flWeight'),)))
    ISpRecoGrammar2.SetDictationWeight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(8, 'SetDictationWeight', ((1, 'flWeight'),)))
    ISpRecoGrammar2.SetGrammarLoader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpeechResourceLoader_head, use_last_error=False)(9, 'SetGrammarLoader', ((1, 'pLoader'),)))
    ISpRecoGrammar2.SetSMLSecurityManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.Urlmon.IInternetSecurityManager_head, use_last_error=False)(10, 'SetSMLSecurityManager', ((1, 'pSMLSecurityManager'),)))
    return ISpRecoGrammar2
def _define_ISpeechResourceLoader_head():
    class ISpeechResourceLoader(win32more.System.Com.IDispatch_head):
        Guid = Guid('b9ac5783-fcd0-4b21-b119-b4f8da8fd2c3')
    return ISpeechResourceLoader
def _define_ISpeechResourceLoader():
    ISpeechResourceLoader = win32more.Media.Speech.ISpeechResourceLoader_head
    ISpeechResourceLoader.LoadResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int16,POINTER(win32more.System.Com.IUnknown_head),POINTER(win32more.Foundation.BSTR),POINTER(Int16),POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'LoadResource', ((1, 'bstrResourceUri'),(1, 'fAlwaysReload'),(1, 'pStream'),(1, 'pbstrMIMEType'),(1, 'pfModified'),(1, 'pbstrRedirectUrl'),)))
    ISpeechResourceLoader.GetLocalCopy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'GetLocalCopy', ((1, 'bstrResourceUri'),(1, 'pbstrLocalPath'),(1, 'pbstrMIMEType'),(1, 'pbstrRedirectUrl'),)))
    ISpeechResourceLoader.ReleaseLocalCopy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(9, 'ReleaseLocalCopy', ((1, 'pbstrLocalPath'),)))
    return ISpeechResourceLoader
def _define_SPRECOCONTEXTSTATUS_head():
    class SPRECOCONTEXTSTATUS(Structure):
        pass
    return SPRECOCONTEXTSTATUS
def _define_SPRECOCONTEXTSTATUS():
    SPRECOCONTEXTSTATUS = win32more.Media.Speech.SPRECOCONTEXTSTATUS_head
    SPRECOCONTEXTSTATUS._fields_ = [
        ("eInterference", win32more.Media.Speech.SPINTERFERENCE),
        ("szRequestTypeOfUI", Char * 255),
        ("dwReserved1", UInt32),
        ("dwReserved2", UInt32),
    ]
    return SPRECOCONTEXTSTATUS
SPBOOKMARKOPTIONS = Int32
SPBO_NONE = 0
SPBO_PAUSE = 1
SPBO_AHEAD = 2
SPBO_TIME_UNITS = 4
SPAUDIOOPTIONS = Int32
SPAO_NONE = 0
SPAO_RETAIN_AUDIO = 1
def _define_ISpRecoContext_head():
    class ISpRecoContext(win32more.Media.Speech.ISpEventSource_head):
        Guid = Guid('f740a62f-7c15-489e-8234-940a33d9272d')
    return ISpRecoContext
def _define_ISpRecoContext():
    ISpRecoContext = win32more.Media.Speech.ISpRecoContext_head
    ISpRecoContext.GetRecognizer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpRecognizer_head), use_last_error=False)(13, 'GetRecognizer', ((1, 'ppRecognizer'),)))
    ISpRecoContext.CreateGrammar = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(win32more.Media.Speech.ISpRecoGrammar_head), use_last_error=False)(14, 'CreateGrammar', ((1, 'ullGrammarId'),(1, 'ppGrammar'),)))
    ISpRecoContext.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPRECOCONTEXTSTATUS_head), use_last_error=False)(15, 'GetStatus', ((1, 'pStatus'),)))
    ISpRecoContext.GetMaxAlternates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(16, 'GetMaxAlternates', ((1, 'pcAlternates'),)))
    ISpRecoContext.SetMaxAlternates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(17, 'SetMaxAlternates', ((1, 'cAlternates'),)))
    ISpRecoContext.SetAudioOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SPAUDIOOPTIONS,POINTER(Guid),POINTER(win32more.Media.Audio.WAVEFORMATEX_head), use_last_error=False)(18, 'SetAudioOptions', ((1, 'Options'),(1, 'pAudioFormatId'),(1, 'pWaveFormatEx'),)))
    ISpRecoContext.GetAudioOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPAUDIOOPTIONS),POINTER(Guid),POINTER(POINTER(win32more.Media.Audio.WAVEFORMATEX_head)), use_last_error=False)(19, 'GetAudioOptions', ((1, 'pOptions'),(1, 'pAudioFormatId'),(1, 'ppCoMemWFEX'),)))
    ISpRecoContext.DeserializeResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPSERIALIZEDRESULT_head),POINTER(win32more.Media.Speech.ISpRecoResult_head), use_last_error=False)(20, 'DeserializeResult', ((1, 'pSerializedResult'),(1, 'ppResult'),)))
    ISpRecoContext.Bookmark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SPBOOKMARKOPTIONS,UInt64,win32more.Foundation.LPARAM, use_last_error=False)(21, 'Bookmark', ((1, 'Options'),(1, 'ullStreamPosition'),(1, 'lparamEvent'),)))
    ISpRecoContext.SetAdaptationData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(22, 'SetAdaptationData', ((1, 'pAdaptationData'),(1, 'cch'),)))
    ISpRecoContext.Pause = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(23, 'Pause', ((1, 'dwReserved'),)))
    ISpRecoContext.Resume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(24, 'Resume', ((1, 'dwReserved'),)))
    ISpRecoContext.SetVoice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpVoice_head,win32more.Foundation.BOOL, use_last_error=False)(25, 'SetVoice', ((1, 'pVoice'),(1, 'fAllowFormatChanges'),)))
    ISpRecoContext.GetVoice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpVoice_head), use_last_error=False)(26, 'GetVoice', ((1, 'ppVoice'),)))
    ISpRecoContext.SetVoicePurgeEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64, use_last_error=False)(27, 'SetVoicePurgeEvent', ((1, 'ullEventInterest'),)))
    ISpRecoContext.GetVoicePurgeEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(28, 'GetVoicePurgeEvent', ((1, 'pullEventInterest'),)))
    ISpRecoContext.SetContextState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SPCONTEXTSTATE, use_last_error=False)(29, 'SetContextState', ((1, 'eContextState'),)))
    ISpRecoContext.GetContextState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPCONTEXTSTATE), use_last_error=False)(30, 'GetContextState', ((1, 'peContextState'),)))
    return ISpRecoContext
SPGRAMMAROPTIONS = Int32
SPGO_SAPI = 1
SPGO_SRGS = 2
SPGO_UPS = 4
SPGO_SRGS_MS_SCRIPT = 8
SPGO_SRGS_W3C_SCRIPT = 256
SPGO_SRGS_STG_SCRIPT = 512
SPGO_SRGS_SCRIPT = 778
SPGO_FILE = 16
SPGO_HTTP = 32
SPGO_RES = 64
SPGO_OBJECT = 128
SPGO_DEFAULT = 1019
SPGO_ALL = 1023
SPADAPTATIONSETTINGS = Int32
SPADS_Default = 0
SPADS_CurrentRecognizer = 1
SPADS_RecoProfile = 2
SPADS_Immediate = 4
SPADS_Reset = 8
SPADS_HighVolumeDataSource = 16
SPADAPTATIONRELEVANCE = Int32
SPAR_Unknown = 0
SPAR_Low = 1
SPAR_Medium = 2
SPAR_High = 3
def _define_ISpRecoContext2_head():
    class ISpRecoContext2(win32more.System.Com.IUnknown_head):
        Guid = Guid('bead311c-52ff-437f-9464-6b21054ca73d')
    return ISpRecoContext2
def _define_ISpRecoContext2():
    ISpRecoContext2 = win32more.Media.Speech.ISpRecoContext2_head
    ISpRecoContext2.SetGrammarOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(3, 'SetGrammarOptions', ((1, 'eGrammarOptions'),)))
    ISpRecoContext2.GetGrammarOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetGrammarOptions', ((1, 'peGrammarOptions'),)))
    ISpRecoContext2.SetAdaptationData2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Media.Speech.SPADAPTATIONRELEVANCE, use_last_error=False)(5, 'SetAdaptationData2', ((1, 'pAdaptationData'),(1, 'cch'),(1, 'pTopicName'),(1, 'eAdaptationSettings'),(1, 'eRelevance'),)))
    return ISpRecoContext2
def _define_ISpProperties_head():
    class ISpProperties(win32more.System.Com.IUnknown_head):
        Guid = Guid('5b4fb971-b115-4de1-ad97-e482e3bf6ee4')
    return ISpProperties
def _define_ISpProperties():
    ISpProperties = win32more.Media.Speech.ISpProperties_head
    ISpProperties.SetPropertyNum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Int32, use_last_error=False)(3, 'SetPropertyNum', ((1, 'pName'),(1, 'lValue'),)))
    ISpProperties.GetPropertyNum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Int32), use_last_error=False)(4, 'GetPropertyNum', ((1, 'pName'),(1, 'plValue'),)))
    ISpProperties.SetPropertyString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(5, 'SetPropertyString', ((1, 'pName'),(1, 'pValue'),)))
    ISpProperties.GetPropertyString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(6, 'GetPropertyString', ((1, 'pName'),(1, 'ppCoMemValue'),)))
    return ISpProperties
def _define_SPRECOGNIZERSTATUS_head():
    class SPRECOGNIZERSTATUS(Structure):
        pass
    return SPRECOGNIZERSTATUS
def _define_SPRECOGNIZERSTATUS():
    SPRECOGNIZERSTATUS = win32more.Media.Speech.SPRECOGNIZERSTATUS_head
    SPRECOGNIZERSTATUS._fields_ = [
        ("AudioStatus", win32more.Media.Speech.SPAUDIOSTATUS),
        ("ullRecognitionStreamPos", UInt64),
        ("ulStreamNumber", UInt32),
        ("ulNumActive", UInt32),
        ("clsidEngine", Guid),
        ("cLangIDs", UInt32),
        ("aLangID", UInt16 * 20),
        ("ullRecognitionStreamTime", UInt64),
    ]
    return SPRECOGNIZERSTATUS
SPWAVEFORMATTYPE = Int32
SPWF_INPUT = 0
SPWF_SRENGINE = 1
SPRECOSTATE = Int32
SPRST_INACTIVE = 0
SPRST_ACTIVE = 1
SPRST_ACTIVE_ALWAYS = 2
SPRST_INACTIVE_WITH_PURGE = 3
SPRST_NUM_STATES = 4
def _define_ISpRecognizer_head():
    class ISpRecognizer(win32more.Media.Speech.ISpProperties_head):
        Guid = Guid('c2b5f241-daa0-4507-9e16-5a1eaa2b7a5c')
    return ISpRecognizer
def _define_ISpRecognizer():
    ISpRecognizer = win32more.Media.Speech.ISpRecognizer_head
    ISpRecognizer.SetRecognizer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpObjectToken_head, use_last_error=False)(7, 'SetRecognizer', ((1, 'pRecognizer'),)))
    ISpRecognizer.GetRecognizer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpObjectToken_head), use_last_error=False)(8, 'GetRecognizer', ((1, 'ppRecognizer'),)))
    ISpRecognizer.SetInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.BOOL, use_last_error=False)(9, 'SetInput', ((1, 'pUnkInput'),(1, 'fAllowFormatChanges'),)))
    ISpRecognizer.GetInputObjectToken = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpObjectToken_head), use_last_error=False)(10, 'GetInputObjectToken', ((1, 'ppToken'),)))
    ISpRecognizer.GetInputStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpStreamFormat_head), use_last_error=False)(11, 'GetInputStream', ((1, 'ppStream'),)))
    ISpRecognizer.CreateRecoContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpRecoContext_head), use_last_error=False)(12, 'CreateRecoContext', ((1, 'ppNewCtxt'),)))
    ISpRecognizer.GetRecoProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpObjectToken_head), use_last_error=False)(13, 'GetRecoProfile', ((1, 'ppToken'),)))
    ISpRecognizer.SetRecoProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpObjectToken_head, use_last_error=False)(14, 'SetRecoProfile', ((1, 'pToken'),)))
    ISpRecognizer.IsSharedInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(15, 'IsSharedInstance', ()))
    ISpRecognizer.GetRecoState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPRECOSTATE), use_last_error=False)(16, 'GetRecoState', ((1, 'pState'),)))
    ISpRecognizer.SetRecoState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SPRECOSTATE, use_last_error=False)(17, 'SetRecoState', ((1, 'NewState'),)))
    ISpRecognizer.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPRECOGNIZERSTATUS_head), use_last_error=False)(18, 'GetStatus', ((1, 'pStatus'),)))
    ISpRecognizer.GetFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SPWAVEFORMATTYPE,POINTER(Guid),POINTER(POINTER(win32more.Media.Audio.WAVEFORMATEX_head)), use_last_error=False)(19, 'GetFormat', ((1, 'WaveFormatType'),(1, 'pFormatId'),(1, 'ppCoMemWFEX'),)))
    ISpRecognizer.IsUISupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,c_void_p,UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(20, 'IsUISupported', ((1, 'pszTypeOfUI'),(1, 'pvExtraData'),(1, 'cbExtraData'),(1, 'pfSupported'),)))
    ISpRecognizer.DisplayUI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_void_p,UInt32, use_last_error=False)(21, 'DisplayUI', ((1, 'hwndParent'),(1, 'pszTitle'),(1, 'pszTypeOfUI'),(1, 'pvExtraData'),(1, 'cbExtraData'),)))
    ISpRecognizer.EmulateRecognition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpPhrase_head, use_last_error=False)(22, 'EmulateRecognition', ((1, 'pPhrase'),)))
    return ISpRecognizer
def _define_ISpSerializeState_head():
    class ISpSerializeState(win32more.System.Com.IUnknown_head):
        Guid = Guid('21b501a0-0ec7-46c9-92c3-a2bc784c54b9')
    return ISpSerializeState
def _define_ISpSerializeState():
    ISpSerializeState = win32more.Media.Speech.ISpSerializeState_head
    ISpSerializeState.GetSerializedState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no),POINTER(UInt32),UInt32, use_last_error=False)(3, 'GetSerializedState', ((1, 'ppbData'),(1, 'pulSize'),(1, 'dwReserved'),)))
    ISpSerializeState.SetSerializedState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,UInt32, use_last_error=False)(4, 'SetSerializedState', ((1, 'pbData'),(1, 'ulSize'),(1, 'dwReserved'),)))
    return ISpSerializeState
def _define_ISpRecognizer2_head():
    class ISpRecognizer2(win32more.System.Com.IUnknown_head):
        Guid = Guid('8fc6d974-c81e-4098-93c5-0147f61ed4d3')
    return ISpRecognizer2
def _define_ISpRecognizer2():
    ISpRecognizer2 = win32more.Media.Speech.ISpRecognizer2_head
    ISpRecognizer2.EmulateRecognitionEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpPhrase_head,UInt32, use_last_error=False)(3, 'EmulateRecognitionEx', ((1, 'pPhrase'),(1, 'dwCompareFlags'),)))
    ISpRecognizer2.SetTrainingState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=False)(4, 'SetTrainingState', ((1, 'fDoingTraining'),(1, 'fAdaptFromTrainingData'),)))
    ISpRecognizer2.ResetAcousticModelAdaptation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'ResetAcousticModelAdaptation', ()))
    return ISpRecognizer2
def _define_SPNORMALIZATIONLIST_head():
    class SPNORMALIZATIONLIST(Structure):
        pass
    return SPNORMALIZATIONLIST
def _define_SPNORMALIZATIONLIST():
    SPNORMALIZATIONLIST = win32more.Media.Speech.SPNORMALIZATIONLIST_head
    SPNORMALIZATIONLIST._fields_ = [
        ("ulSize", UInt32),
        ("ppszzNormalizedList", POINTER(POINTER(UInt16))),
    ]
    return SPNORMALIZATIONLIST
def _define_ISpEnginePronunciation_head():
    class ISpEnginePronunciation(win32more.System.Com.IUnknown_head):
        Guid = Guid('c360ce4b-76d1-4214-ad68-52657d5083da')
    return ISpEnginePronunciation
def _define_ISpEnginePronunciation():
    ISpEnginePronunciation = win32more.Media.Speech.ISpEnginePronunciation_head
    ISpEnginePronunciation.Normalize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt16,POINTER(win32more.Media.Speech.SPNORMALIZATIONLIST_head), use_last_error=False)(3, 'Normalize', ((1, 'pszWord'),(1, 'pszLeftContext'),(1, 'pszRightContext'),(1, 'LangID'),(1, 'pNormalizationList'),)))
    ISpEnginePronunciation.GetPronunciations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt16,POINTER(win32more.Media.Speech.SPWORDPRONUNCIATIONLIST_head), use_last_error=False)(4, 'GetPronunciations', ((1, 'pszWord'),(1, 'pszLeftContext'),(1, 'pszRightContext'),(1, 'LangID'),(1, 'pEnginePronunciationList'),)))
    return ISpEnginePronunciation
def _define_SPDISPLAYTOKEN_head():
    class SPDISPLAYTOKEN(Structure):
        pass
    return SPDISPLAYTOKEN
def _define_SPDISPLAYTOKEN():
    SPDISPLAYTOKEN = win32more.Media.Speech.SPDISPLAYTOKEN_head
    SPDISPLAYTOKEN._fields_ = [
        ("pszLexical", win32more.Foundation.PWSTR),
        ("pszDisplay", win32more.Foundation.PWSTR),
        ("bDisplayAttributes", Byte),
    ]
    return SPDISPLAYTOKEN
def _define_SPDISPLAYPHRASE_head():
    class SPDISPLAYPHRASE(Structure):
        pass
    return SPDISPLAYPHRASE
def _define_SPDISPLAYPHRASE():
    SPDISPLAYPHRASE = win32more.Media.Speech.SPDISPLAYPHRASE_head
    SPDISPLAYPHRASE._fields_ = [
        ("ulNumTokens", UInt32),
        ("pTokens", POINTER(win32more.Media.Speech.SPDISPLAYTOKEN_head)),
    ]
    return SPDISPLAYPHRASE
def _define_ISpDisplayAlternates_head():
    class ISpDisplayAlternates(win32more.System.Com.IUnknown_head):
        Guid = Guid('c8d7c7e2-0dde-44b7-afe3-b0c991fbeb5e')
    return ISpDisplayAlternates
def _define_ISpDisplayAlternates():
    ISpDisplayAlternates = win32more.Media.Speech.ISpDisplayAlternates_head
    ISpDisplayAlternates.GetDisplayAlternates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SPDISPLAYPHRASE_head),UInt32,POINTER(POINTER(win32more.Media.Speech.SPDISPLAYPHRASE_head)),POINTER(UInt32), use_last_error=False)(3, 'GetDisplayAlternates', ((1, 'pPhrase'),(1, 'cRequestCount'),(1, 'ppCoMemPhrases'),(1, 'pcPhrasesReturned'),)))
    ISpDisplayAlternates.SetFullStopTrailSpace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'SetFullStopTrailSpace', ((1, 'ulTrailSpace'),)))
    return ISpDisplayAlternates
DISPID_SpeechDataKey = Int32
DISPID_SDKSetBinaryValue = 1
DISPID_SDKGetBinaryValue = 2
DISPID_SDKSetStringValue = 3
DISPID_SDKGetStringValue = 4
DISPID_SDKSetLongValue = 5
DISPID_SDKGetlongValue = 6
DISPID_SDKOpenKey = 7
DISPID_SDKCreateKey = 8
DISPID_SDKDeleteKey = 9
DISPID_SDKDeleteValue = 10
DISPID_SDKEnumKeys = 11
DISPID_SDKEnumValues = 12
DISPID_SpeechObjectToken = Int32
DISPID_SOTId = 1
DISPID_SOTDataKey = 2
DISPID_SOTCategory = 3
DISPID_SOTGetDescription = 4
DISPID_SOTSetId = 5
DISPID_SOTGetAttribute = 6
DISPID_SOTCreateInstance = 7
DISPID_SOTRemove = 8
DISPID_SOTGetStorageFileName = 9
DISPID_SOTRemoveStorageFileName = 10
DISPID_SOTIsUISupported = 11
DISPID_SOTDisplayUI = 12
DISPID_SOTMatchesAttributes = 13
SpeechDataKeyLocation = Int32
SpeechDataKeyLocation_SDKLDefaultLocation = 0
SpeechDataKeyLocation_SDKLCurrentUser = 1
SpeechDataKeyLocation_SDKLLocalMachine = 2
SpeechDataKeyLocation_SDKLCurrentConfig = 5
SpeechTokenContext = UInt32
SpeechTokenContext_STCInprocServer = 1
SpeechTokenContext_STCInprocHandler = 2
SpeechTokenContext_STCLocalServer = 4
SpeechTokenContext_STCRemoteServer = 16
SpeechTokenContext_STCAll = 23
SpeechTokenShellFolder = Int32
STSF_AppData = 26
STSF_LocalAppData = 28
STSF_CommonAppData = 35
STSF_FlagCreate = 32768
DISPID_SpeechObjectTokens = Int32
DISPID_SOTsCount = 1
DISPID_SOTsItem = 0
DISPID_SOTs_NewEnum = -4
DISPID_SpeechObjectTokenCategory = Int32
DISPID_SOTCId = 1
DISPID_SOTCDefault = 2
DISPID_SOTCSetId = 3
DISPID_SOTCGetDataKey = 4
DISPID_SOTCEnumerateTokens = 5
SpeechAudioFormatType = Int32
SpeechAudioFormatType_SAFTDefault = -1
SpeechAudioFormatType_SAFTNoAssignedFormat = 0
SpeechAudioFormatType_SAFTText = 1
SpeechAudioFormatType_SAFTNonStandardFormat = 2
SpeechAudioFormatType_SAFTExtendedAudioFormat = 3
SpeechAudioFormatType_SAFT8kHz8BitMono = 4
SpeechAudioFormatType_SAFT8kHz8BitStereo = 5
SpeechAudioFormatType_SAFT8kHz16BitMono = 6
SpeechAudioFormatType_SAFT8kHz16BitStereo = 7
SpeechAudioFormatType_SAFT11kHz8BitMono = 8
SpeechAudioFormatType_SAFT11kHz8BitStereo = 9
SpeechAudioFormatType_SAFT11kHz16BitMono = 10
SpeechAudioFormatType_SAFT11kHz16BitStereo = 11
SpeechAudioFormatType_SAFT12kHz8BitMono = 12
SpeechAudioFormatType_SAFT12kHz8BitStereo = 13
SpeechAudioFormatType_SAFT12kHz16BitMono = 14
SpeechAudioFormatType_SAFT12kHz16BitStereo = 15
SpeechAudioFormatType_SAFT16kHz8BitMono = 16
SpeechAudioFormatType_SAFT16kHz8BitStereo = 17
SpeechAudioFormatType_SAFT16kHz16BitMono = 18
SpeechAudioFormatType_SAFT16kHz16BitStereo = 19
SpeechAudioFormatType_SAFT22kHz8BitMono = 20
SpeechAudioFormatType_SAFT22kHz8BitStereo = 21
SpeechAudioFormatType_SAFT22kHz16BitMono = 22
SpeechAudioFormatType_SAFT22kHz16BitStereo = 23
SpeechAudioFormatType_SAFT24kHz8BitMono = 24
SpeechAudioFormatType_SAFT24kHz8BitStereo = 25
SpeechAudioFormatType_SAFT24kHz16BitMono = 26
SpeechAudioFormatType_SAFT24kHz16BitStereo = 27
SpeechAudioFormatType_SAFT32kHz8BitMono = 28
SpeechAudioFormatType_SAFT32kHz8BitStereo = 29
SpeechAudioFormatType_SAFT32kHz16BitMono = 30
SpeechAudioFormatType_SAFT32kHz16BitStereo = 31
SpeechAudioFormatType_SAFT44kHz8BitMono = 32
SpeechAudioFormatType_SAFT44kHz8BitStereo = 33
SpeechAudioFormatType_SAFT44kHz16BitMono = 34
SpeechAudioFormatType_SAFT44kHz16BitStereo = 35
SpeechAudioFormatType_SAFT48kHz8BitMono = 36
SpeechAudioFormatType_SAFT48kHz8BitStereo = 37
SpeechAudioFormatType_SAFT48kHz16BitMono = 38
SpeechAudioFormatType_SAFT48kHz16BitStereo = 39
SpeechAudioFormatType_SAFTTrueSpeech_8kHz1BitMono = 40
SpeechAudioFormatType_SAFTCCITT_ALaw_8kHzMono = 41
SpeechAudioFormatType_SAFTCCITT_ALaw_8kHzStereo = 42
SpeechAudioFormatType_SAFTCCITT_ALaw_11kHzMono = 43
SpeechAudioFormatType_SAFTCCITT_ALaw_11kHzStereo = 44
SpeechAudioFormatType_SAFTCCITT_ALaw_22kHzMono = 45
SpeechAudioFormatType_SAFTCCITT_ALaw_22kHzStereo = 46
SpeechAudioFormatType_SAFTCCITT_ALaw_44kHzMono = 47
SpeechAudioFormatType_SAFTCCITT_ALaw_44kHzStereo = 48
SpeechAudioFormatType_SAFTCCITT_uLaw_8kHzMono = 49
SpeechAudioFormatType_SAFTCCITT_uLaw_8kHzStereo = 50
SpeechAudioFormatType_SAFTCCITT_uLaw_11kHzMono = 51
SpeechAudioFormatType_SAFTCCITT_uLaw_11kHzStereo = 52
SpeechAudioFormatType_SAFTCCITT_uLaw_22kHzMono = 53
SpeechAudioFormatType_SAFTCCITT_uLaw_22kHzStereo = 54
SpeechAudioFormatType_SAFTCCITT_uLaw_44kHzMono = 55
SpeechAudioFormatType_SAFTCCITT_uLaw_44kHzStereo = 56
SpeechAudioFormatType_SAFTADPCM_8kHzMono = 57
SpeechAudioFormatType_SAFTADPCM_8kHzStereo = 58
SpeechAudioFormatType_SAFTADPCM_11kHzMono = 59
SpeechAudioFormatType_SAFTADPCM_11kHzStereo = 60
SpeechAudioFormatType_SAFTADPCM_22kHzMono = 61
SpeechAudioFormatType_SAFTADPCM_22kHzStereo = 62
SpeechAudioFormatType_SAFTADPCM_44kHzMono = 63
SpeechAudioFormatType_SAFTADPCM_44kHzStereo = 64
SpeechAudioFormatType_SAFTGSM610_8kHzMono = 65
SpeechAudioFormatType_SAFTGSM610_11kHzMono = 66
SpeechAudioFormatType_SAFTGSM610_22kHzMono = 67
SpeechAudioFormatType_SAFTGSM610_44kHzMono = 68
DISPID_SpeechAudioFormat = Int32
DISPID_SAFType = 1
DISPID_SAFGuid = 2
DISPID_SAFGetWaveFormatEx = 3
DISPID_SAFSetWaveFormatEx = 4
DISPID_SpeechBaseStream = Int32
DISPID_SBSFormat = 1
DISPID_SBSRead = 2
DISPID_SBSWrite = 3
DISPID_SBSSeek = 4
SpeechStreamSeekPositionType = UInt32
SpeechStreamSeekPositionType_SSSPTRelativeToStart = 0
SpeechStreamSeekPositionType_SSSPTRelativeToCurrentPosition = 1
SpeechStreamSeekPositionType_SSSPTRelativeToEnd = 2
DISPID_SpeechAudio = Int32
DISPID_SAStatus = 200
DISPID_SABufferInfo = 201
DISPID_SADefaultFormat = 202
DISPID_SAVolume = 203
DISPID_SABufferNotifySize = 204
DISPID_SAEventHandle = 205
DISPID_SASetState = 206
SpeechAudioState = Int32
SpeechAudioState_SASClosed = 0
SpeechAudioState_SASStop = 1
SpeechAudioState_SASPause = 2
SpeechAudioState_SASRun = 3
DISPID_SpeechMMSysAudio = Int32
DISPID_SMSADeviceId = 300
DISPID_SMSALineId = 301
DISPID_SMSAMMHandle = 302
DISPID_SpeechFileStream = Int32
DISPID_SFSOpen = 100
DISPID_SFSClose = 101
SpeechStreamFileMode = Int32
SpeechStreamFileMode_SSFMOpenForRead = 0
SpeechStreamFileMode_SSFMOpenReadWrite = 1
SpeechStreamFileMode_SSFMCreate = 2
SpeechStreamFileMode_SSFMCreateForWrite = 3
DISPID_SpeechCustomStream = Int32
DISPID_SCSBaseStream = 100
DISPID_SpeechMemoryStream = Int32
DISPID_SMSSetData = 100
DISPID_SMSGetData = 101
DISPID_SpeechAudioStatus = Int32
DISPID_SASFreeBufferSpace = 1
DISPID_SASNonBlockingIO = 2
DISPID_SASState = 3
DISPID_SASCurrentSeekPosition = 4
DISPID_SASCurrentDevicePosition = 5
DISPID_SpeechAudioBufferInfo = Int32
DISPID_SABIMinNotification = 1
DISPID_SABIBufferSize = 2
DISPID_SABIEventBias = 3
DISPID_SpeechWaveFormatEx = Int32
DISPID_SWFEFormatTag = 1
DISPID_SWFEChannels = 2
DISPID_SWFESamplesPerSec = 3
DISPID_SWFEAvgBytesPerSec = 4
DISPID_SWFEBlockAlign = 5
DISPID_SWFEBitsPerSample = 6
DISPID_SWFEExtraData = 7
DISPID_SpeechVoice = Int32
DISPID_SVStatus = 1
DISPID_SVVoice = 2
DISPID_SVAudioOutput = 3
DISPID_SVAudioOutputStream = 4
DISPID_SVRate = 5
DISPID_SVVolume = 6
DISPID_SVAllowAudioOuputFormatChangesOnNextSet = 7
DISPID_SVEventInterests = 8
DISPID_SVPriority = 9
DISPID_SVAlertBoundary = 10
DISPID_SVSyncronousSpeakTimeout = 11
DISPID_SVSpeak = 12
DISPID_SVSpeakStream = 13
DISPID_SVPause = 14
DISPID_SVResume = 15
DISPID_SVSkip = 16
DISPID_SVGetVoices = 17
DISPID_SVGetAudioOutputs = 18
DISPID_SVWaitUntilDone = 19
DISPID_SVSpeakCompleteEvent = 20
DISPID_SVIsUISupported = 21
DISPID_SVDisplayUI = 22
SpeechVoicePriority = Int32
SpeechVoicePriority_SVPNormal = 0
SpeechVoicePriority_SVPAlert = 1
SpeechVoicePriority_SVPOver = 2
SpeechVoiceSpeakFlags = Int32
SpeechVoiceSpeakFlags_SVSFDefault = 0
SpeechVoiceSpeakFlags_SVSFlagsAsync = 1
SpeechVoiceSpeakFlags_SVSFPurgeBeforeSpeak = 2
SpeechVoiceSpeakFlags_SVSFIsFilename = 4
SpeechVoiceSpeakFlags_SVSFIsXML = 8
SpeechVoiceSpeakFlags_SVSFIsNotXML = 16
SpeechVoiceSpeakFlags_SVSFPersistXML = 32
SpeechVoiceSpeakFlags_SVSFNLPSpeakPunc = 64
SpeechVoiceSpeakFlags_SVSFParseSapi = 128
SpeechVoiceSpeakFlags_SVSFParseSsml = 256
SpeechVoiceSpeakFlags_SVSFParseAutodetect = 0
SpeechVoiceSpeakFlags_SVSFNLPMask = 64
SpeechVoiceSpeakFlags_SVSFParseMask = 384
SpeechVoiceSpeakFlags_SVSFVoiceMask = 511
SpeechVoiceSpeakFlags_SVSFUnusedFlags = -512
SpeechVoiceEvents = Int32
SpeechVoiceEvents_SVEStartInputStream = 2
SpeechVoiceEvents_SVEEndInputStream = 4
SpeechVoiceEvents_SVEVoiceChange = 8
SpeechVoiceEvents_SVEBookmark = 16
SpeechVoiceEvents_SVEWordBoundary = 32
SpeechVoiceEvents_SVEPhoneme = 64
SpeechVoiceEvents_SVESentenceBoundary = 128
SpeechVoiceEvents_SVEViseme = 256
SpeechVoiceEvents_SVEAudioLevel = 512
SpeechVoiceEvents_SVEPrivate = 32768
SpeechVoiceEvents_SVEAllEvents = 33790
DISPID_SpeechVoiceStatus = Int32
DISPID_SVSCurrentStreamNumber = 1
DISPID_SVSLastStreamNumberQueued = 2
DISPID_SVSLastResult = 3
DISPID_SVSRunningState = 4
DISPID_SVSInputWordPosition = 5
DISPID_SVSInputWordLength = 6
DISPID_SVSInputSentencePosition = 7
DISPID_SVSInputSentenceLength = 8
DISPID_SVSLastBookmark = 9
DISPID_SVSLastBookmarkId = 10
DISPID_SVSPhonemeId = 11
DISPID_SVSVisemeId = 12
SpeechRunState = Int32
SpeechRunState_SRSEDone = 1
SpeechRunState_SRSEIsSpeaking = 2
SpeechVisemeType = Int32
SVP_0 = 0
SVP_1 = 1
SVP_2 = 2
SVP_3 = 3
SVP_4 = 4
SVP_5 = 5
SVP_6 = 6
SVP_7 = 7
SVP_8 = 8
SVP_9 = 9
SVP_10 = 10
SVP_11 = 11
SVP_12 = 12
SVP_13 = 13
SVP_14 = 14
SVP_15 = 15
SVP_16 = 16
SVP_17 = 17
SVP_18 = 18
SVP_19 = 19
SVP_20 = 20
SVP_21 = 21
SpeechVisemeFeature = Int32
SVF_None = 0
SVF_Stressed = 1
SVF_Emphasis = 2
DISPID_SpeechVoiceEvent = Int32
DISPID_SVEStreamStart = 1
DISPID_SVEStreamEnd = 2
DISPID_SVEVoiceChange = 3
DISPID_SVEBookmark = 4
DISPID_SVEWord = 5
DISPID_SVEPhoneme = 6
DISPID_SVESentenceBoundary = 7
DISPID_SVEViseme = 8
DISPID_SVEAudioLevel = 9
DISPID_SVEEnginePrivate = 10
DISPID_SpeechRecognizer = Int32
DISPID_SRRecognizer = 1
DISPID_SRAllowAudioInputFormatChangesOnNextSet = 2
DISPID_SRAudioInput = 3
DISPID_SRAudioInputStream = 4
DISPID_SRIsShared = 5
DISPID_SRState = 6
DISPID_SRStatus = 7
DISPID_SRProfile = 8
DISPID_SREmulateRecognition = 9
DISPID_SRCreateRecoContext = 10
DISPID_SRGetFormat = 11
DISPID_SRSetPropertyNumber = 12
DISPID_SRGetPropertyNumber = 13
DISPID_SRSetPropertyString = 14
DISPID_SRGetPropertyString = 15
DISPID_SRIsUISupported = 16
DISPID_SRDisplayUI = 17
DISPID_SRGetRecognizers = 18
DISPID_SVGetAudioInputs = 19
DISPID_SVGetProfiles = 20
SpeechRecognizerState = Int32
SpeechRecognizerState_SRSInactive = 0
SpeechRecognizerState_SRSActive = 1
SpeechRecognizerState_SRSActiveAlways = 2
SpeechRecognizerState_SRSInactiveWithPurge = 3
SpeechDisplayAttributes = Int32
SDA_No_Trailing_Space = 0
SDA_One_Trailing_Space = 2
SDA_Two_Trailing_Spaces = 4
SDA_Consume_Leading_Spaces = 8
SpeechFormatType = Int32
SpeechFormatType_SFTInput = 0
SpeechFormatType_SFTSREngine = 1
SpeechEmulationCompareFlags = Int32
SpeechEmulationCompareFlags_SECFIgnoreCase = 1
SpeechEmulationCompareFlags_SECFIgnoreKanaType = 65536
SpeechEmulationCompareFlags_SECFIgnoreWidth = 131072
SpeechEmulationCompareFlags_SECFNoSpecialChars = 536870912
SpeechEmulationCompareFlags_SECFEmulateResult = 1073741824
SpeechEmulationCompareFlags_SECFDefault = 196609
DISPID_SpeechRecognizerStatus = Int32
DISPID_SRSAudioStatus = 1
DISPID_SRSCurrentStreamPosition = 2
DISPID_SRSCurrentStreamNumber = 3
DISPID_SRSNumberOfActiveRules = 4
DISPID_SRSClsidEngine = 5
DISPID_SRSSupportedLanguages = 6
DISPID_SpeechRecoContext = Int32
DISPID_SRCRecognizer = 1
DISPID_SRCAudioInInterferenceStatus = 2
DISPID_SRCRequestedUIType = 3
DISPID_SRCVoice = 4
DISPID_SRAllowVoiceFormatMatchingOnNextSet = 5
DISPID_SRCVoicePurgeEvent = 6
DISPID_SRCEventInterests = 7
DISPID_SRCCmdMaxAlternates = 8
DISPID_SRCState = 9
DISPID_SRCRetainedAudio = 10
DISPID_SRCRetainedAudioFormat = 11
DISPID_SRCPause = 12
DISPID_SRCResume = 13
DISPID_SRCCreateGrammar = 14
DISPID_SRCCreateResultFromMemory = 15
DISPID_SRCBookmark = 16
DISPID_SRCSetAdaptationData = 17
SpeechRetainedAudioOptions = Int32
SpeechRetainedAudioOptions_SRAONone = 0
SpeechRetainedAudioOptions_SRAORetainAudio = 1
SpeechBookmarkOptions = Int32
SpeechBookmarkOptions_SBONone = 0
SpeechBookmarkOptions_SBOPause = 1
SpeechInterference = Int32
SpeechInterference_SINone = 0
SpeechInterference_SINoise = 1
SpeechInterference_SINoSignal = 2
SpeechInterference_SITooLoud = 3
SpeechInterference_SITooQuiet = 4
SpeechInterference_SITooFast = 5
SpeechInterference_SITooSlow = 6
SpeechRecoEvents = Int32
SpeechRecoEvents_SREStreamEnd = 1
SpeechRecoEvents_SRESoundStart = 2
SpeechRecoEvents_SRESoundEnd = 4
SpeechRecoEvents_SREPhraseStart = 8
SpeechRecoEvents_SRERecognition = 16
SpeechRecoEvents_SREHypothesis = 32
SpeechRecoEvents_SREBookmark = 64
SpeechRecoEvents_SREPropertyNumChange = 128
SpeechRecoEvents_SREPropertyStringChange = 256
SpeechRecoEvents_SREFalseRecognition = 512
SpeechRecoEvents_SREInterference = 1024
SpeechRecoEvents_SRERequestUI = 2048
SpeechRecoEvents_SREStateChange = 4096
SpeechRecoEvents_SREAdaptation = 8192
SpeechRecoEvents_SREStreamStart = 16384
SpeechRecoEvents_SRERecoOtherContext = 32768
SpeechRecoEvents_SREAudioLevel = 65536
SpeechRecoEvents_SREPrivate = 262144
SpeechRecoEvents_SREAllEvents = 393215
SpeechRecoContextState = Int32
SRCS_Disabled = 0
SRCS_Enabled = 1
DISPIDSPRG = Int32
DISPID_SRGId = 1
DISPID_SRGRecoContext = 2
DISPID_SRGState = 3
DISPID_SRGRules = 4
DISPID_SRGReset = 5
DISPID_SRGCommit = 6
DISPID_SRGCmdLoadFromFile = 7
DISPID_SRGCmdLoadFromObject = 8
DISPID_SRGCmdLoadFromResource = 9
DISPID_SRGCmdLoadFromMemory = 10
DISPID_SRGCmdLoadFromProprietaryGrammar = 11
DISPID_SRGCmdSetRuleState = 12
DISPID_SRGCmdSetRuleIdState = 13
DISPID_SRGDictationLoad = 14
DISPID_SRGDictationUnload = 15
DISPID_SRGDictationSetState = 16
DISPID_SRGSetWordSequenceData = 17
DISPID_SRGSetTextSelection = 18
DISPID_SRGIsPronounceable = 19
SpeechLoadOption = Int32
SpeechLoadOption_SLOStatic = 0
SpeechLoadOption_SLODynamic = 1
SpeechWordPronounceable = Int32
SpeechWordPronounceable_SWPUnknownWordUnpronounceable = 0
SpeechWordPronounceable_SWPUnknownWordPronounceable = 1
SpeechWordPronounceable_SWPKnownWordPronounceable = 2
SpeechGrammarState = Int32
SpeechGrammarState_SGSEnabled = 1
SpeechGrammarState_SGSDisabled = 0
SpeechGrammarState_SGSExclusive = 3
SpeechRuleState = Int32
SpeechRuleState_SGDSInactive = 0
SpeechRuleState_SGDSActive = 1
SpeechRuleState_SGDSActiveWithAutoPause = 3
SpeechRuleState_SGDSActiveUserDelimited = 4
SpeechRuleAttributes = Int32
SpeechRuleAttributes_SRATopLevel = 1
SpeechRuleAttributes_SRADefaultToActive = 2
SpeechRuleAttributes_SRAExport = 4
SpeechRuleAttributes_SRAImport = 8
SpeechRuleAttributes_SRAInterpreter = 16
SpeechRuleAttributes_SRADynamic = 32
SpeechRuleAttributes_SRARoot = 64
SpeechGrammarWordType = Int32
SpeechGrammarWordType_SGDisplay = 0
SpeechGrammarWordType_SGLexical = 1
SpeechGrammarWordType_SGPronounciation = 2
SpeechGrammarWordType_SGLexicalNoSpecialChars = 3
DISPID_SpeechRecoContextEvents = Int32
DISPID_SRCEStartStream = 1
DISPID_SRCEEndStream = 2
DISPID_SRCEBookmark = 3
DISPID_SRCESoundStart = 4
DISPID_SRCESoundEnd = 5
DISPID_SRCEPhraseStart = 6
DISPID_SRCERecognition = 7
DISPID_SRCEHypothesis = 8
DISPID_SRCEPropertyNumberChange = 9
DISPID_SRCEPropertyStringChange = 10
DISPID_SRCEFalseRecognition = 11
DISPID_SRCEInterference = 12
DISPID_SRCERequestUI = 13
DISPID_SRCERecognizerStateChange = 14
DISPID_SRCEAdaptation = 15
DISPID_SRCERecognitionForOtherContext = 16
DISPID_SRCEAudioLevel = 17
DISPID_SRCEEnginePrivate = 18
SpeechRecognitionType = Int32
SpeechRecognitionType_SRTStandard = 0
SpeechRecognitionType_SRTAutopause = 1
SpeechRecognitionType_SRTEmulated = 2
SpeechRecognitionType_SRTSMLTimeout = 4
SpeechRecognitionType_SRTExtendableParse = 8
SpeechRecognitionType_SRTReSent = 16
DISPID_SpeechGrammarRule = Int32
DISPID_SGRAttributes = 1
DISPID_SGRInitialState = 2
DISPID_SGRName = 3
DISPID_SGRId = 4
DISPID_SGRClear = 5
DISPID_SGRAddResource = 6
DISPID_SGRAddState = 7
DISPID_SpeechGrammarRules = Int32
DISPID_SGRsCount = 1
DISPID_SGRsDynamic = 2
DISPID_SGRsAdd = 3
DISPID_SGRsCommit = 4
DISPID_SGRsCommitAndSave = 5
DISPID_SGRsFindRule = 6
DISPID_SGRsItem = 0
DISPID_SGRs_NewEnum = -4
DISPID_SpeechGrammarRuleState = Int32
DISPID_SGRSRule = 1
DISPID_SGRSTransitions = 2
DISPID_SGRSAddWordTransition = 3
DISPID_SGRSAddRuleTransition = 4
DISPID_SGRSAddSpecialTransition = 5
SpeechSpecialTransitionType = Int32
SpeechSpecialTransitionType_SSTTWildcard = 1
SpeechSpecialTransitionType_SSTTDictation = 2
SpeechSpecialTransitionType_SSTTTextBuffer = 3
DISPID_SpeechGrammarRuleStateTransitions = Int32
DISPID_SGRSTsCount = 1
DISPID_SGRSTsItem = 0
DISPID_SGRSTs_NewEnum = -4
DISPID_SpeechGrammarRuleStateTransition = Int32
DISPID_SGRSTType = 1
DISPID_SGRSTText = 2
DISPID_SGRSTRule = 3
DISPID_SGRSTWeight = 4
DISPID_SGRSTPropertyName = 5
DISPID_SGRSTPropertyId = 6
DISPID_SGRSTPropertyValue = 7
DISPID_SGRSTNextState = 8
SpeechGrammarRuleStateTransitionType = Int32
SpeechGrammarRuleStateTransitionType_SGRSTTEpsilon = 0
SpeechGrammarRuleStateTransitionType_SGRSTTWord = 1
SpeechGrammarRuleStateTransitionType_SGRSTTRule = 2
SpeechGrammarRuleStateTransitionType_SGRSTTDictation = 3
SpeechGrammarRuleStateTransitionType_SGRSTTWildcard = 4
SpeechGrammarRuleStateTransitionType_SGRSTTTextBuffer = 5
DISPIDSPTSI = Int32
DISPIDSPTSI_ActiveOffset = 1
DISPIDSPTSI_ActiveLength = 2
DISPIDSPTSI_SelectionOffset = 3
DISPIDSPTSI_SelectionLength = 4
DISPID_SpeechRecoResult = Int32
DISPID_SRRRecoContext = 1
DISPID_SRRTimes = 2
DISPID_SRRAudioFormat = 3
DISPID_SRRPhraseInfo = 4
DISPID_SRRAlternates = 5
DISPID_SRRAudio = 6
DISPID_SRRSpeakAudio = 7
DISPID_SRRSaveToMemory = 8
DISPID_SRRDiscardResultInfo = 9
SpeechDiscardType = Int32
SpeechDiscardType_SDTProperty = 1
SpeechDiscardType_SDTReplacement = 2
SpeechDiscardType_SDTRule = 4
SpeechDiscardType_SDTDisplayText = 8
SpeechDiscardType_SDTLexicalForm = 16
SpeechDiscardType_SDTPronunciation = 32
SpeechDiscardType_SDTAudio = 64
SpeechDiscardType_SDTAlternates = 128
SpeechDiscardType_SDTAll = 255
DISPID_SpeechXMLRecoResult = Int32
DISPID_SRRGetXMLResult = 10
DISPID_SRRGetXMLErrorInfo = 11
DISPID_SpeechRecoResult2 = Int32
DISPID_SRRSetTextFeedback = 12
DISPID_SpeechPhraseBuilder = Int32
DISPID_SPPBRestorePhraseFromMemory = 1
DISPID_SpeechRecoResultTimes = Int32
DISPID_SRRTStreamTime = 1
DISPID_SRRTLength = 2
DISPID_SRRTTickCount = 3
DISPID_SRRTOffsetFromStart = 4
DISPID_SpeechPhraseAlternate = Int32
DISPID_SPARecoResult = 1
DISPID_SPAStartElementInResult = 2
DISPID_SPANumberOfElementsInResult = 3
DISPID_SPAPhraseInfo = 4
DISPID_SPACommit = 5
DISPID_SpeechPhraseAlternates = Int32
DISPID_SPAsCount = 1
DISPID_SPAsItem = 0
DISPID_SPAs_NewEnum = -4
DISPID_SpeechPhraseInfo = Int32
DISPID_SPILanguageId = 1
DISPID_SPIGrammarId = 2
DISPID_SPIStartTime = 3
DISPID_SPIAudioStreamPosition = 4
DISPID_SPIAudioSizeBytes = 5
DISPID_SPIRetainedSizeBytes = 6
DISPID_SPIAudioSizeTime = 7
DISPID_SPIRule = 8
DISPID_SPIProperties = 9
DISPID_SPIElements = 10
DISPID_SPIReplacements = 11
DISPID_SPIEngineId = 12
DISPID_SPIEnginePrivateData = 13
DISPID_SPISaveToMemory = 14
DISPID_SPIGetText = 15
DISPID_SPIGetDisplayAttributes = 16
DISPID_SpeechPhraseElement = Int32
DISPID_SPEAudioTimeOffset = 1
DISPID_SPEAudioSizeTime = 2
DISPID_SPEAudioStreamOffset = 3
DISPID_SPEAudioSizeBytes = 4
DISPID_SPERetainedStreamOffset = 5
DISPID_SPERetainedSizeBytes = 6
DISPID_SPEDisplayText = 7
DISPID_SPELexicalForm = 8
DISPID_SPEPronunciation = 9
DISPID_SPEDisplayAttributes = 10
DISPID_SPERequiredConfidence = 11
DISPID_SPEActualConfidence = 12
DISPID_SPEEngineConfidence = 13
SpeechEngineConfidence = Int32
SpeechEngineConfidence_SECLowConfidence = -1
SpeechEngineConfidence_SECNormalConfidence = 0
SpeechEngineConfidence_SECHighConfidence = 1
DISPID_SpeechPhraseElements = Int32
DISPID_SPEsCount = 1
DISPID_SPEsItem = 0
DISPID_SPEs_NewEnum = -4
DISPID_SpeechPhraseReplacement = Int32
DISPID_SPRDisplayAttributes = 1
DISPID_SPRText = 2
DISPID_SPRFirstElement = 3
DISPID_SPRNumberOfElements = 4
DISPID_SpeechPhraseReplacements = Int32
DISPID_SPRsCount = 1
DISPID_SPRsItem = 0
DISPID_SPRs_NewEnum = -4
DISPID_SpeechPhraseProperty = Int32
DISPID_SPPName = 1
DISPID_SPPId = 2
DISPID_SPPValue = 3
DISPID_SPPFirstElement = 4
DISPID_SPPNumberOfElements = 5
DISPID_SPPEngineConfidence = 6
DISPID_SPPConfidence = 7
DISPID_SPPParent = 8
DISPID_SPPChildren = 9
DISPID_SpeechPhraseProperties = Int32
DISPID_SPPsCount = 1
DISPID_SPPsItem = 0
DISPID_SPPs_NewEnum = -4
DISPID_SpeechPhraseRule = Int32
DISPID_SPRuleName = 1
DISPID_SPRuleId = 2
DISPID_SPRuleFirstElement = 3
DISPID_SPRuleNumberOfElements = 4
DISPID_SPRuleParent = 5
DISPID_SPRuleChildren = 6
DISPID_SPRuleConfidence = 7
DISPID_SPRuleEngineConfidence = 8
DISPID_SpeechPhraseRules = Int32
DISPID_SPRulesCount = 1
DISPID_SPRulesItem = 0
DISPID_SPRules_NewEnum = -4
DISPID_SpeechLexicon = Int32
DISPID_SLGenerationId = 1
DISPID_SLGetWords = 2
DISPID_SLAddPronunciation = 3
DISPID_SLAddPronunciationByPhoneIds = 4
DISPID_SLRemovePronunciation = 5
DISPID_SLRemovePronunciationByPhoneIds = 6
DISPID_SLGetPronunciations = 7
DISPID_SLGetGenerationChange = 8
SpeechLexiconType = Int32
SpeechLexiconType_SLTUser = 1
SpeechLexiconType_SLTApp = 2
SpeechPartOfSpeech = Int32
SpeechPartOfSpeech_SPSNotOverriden = -1
SpeechPartOfSpeech_SPSUnknown = 0
SpeechPartOfSpeech_SPSNoun = 4096
SpeechPartOfSpeech_SPSVerb = 8192
SpeechPartOfSpeech_SPSModifier = 12288
SpeechPartOfSpeech_SPSFunction = 16384
SpeechPartOfSpeech_SPSInterjection = 20480
SpeechPartOfSpeech_SPSLMA = 28672
SpeechPartOfSpeech_SPSSuppressWord = 61440
DISPID_SpeechLexiconWords = Int32
DISPID_SLWsCount = 1
DISPID_SLWsItem = 0
DISPID_SLWs_NewEnum = -4
SpeechWordType = Int32
SpeechWordType_SWTAdded = 1
SpeechWordType_SWTDeleted = 2
DISPID_SpeechLexiconWord = Int32
DISPID_SLWLangId = 1
DISPID_SLWType = 2
DISPID_SLWWord = 3
DISPID_SLWPronunciations = 4
DISPID_SpeechLexiconProns = Int32
DISPID_SLPsCount = 1
DISPID_SLPsItem = 0
DISPID_SLPs_NewEnum = -4
DISPID_SpeechLexiconPronunciation = Int32
DISPID_SLPType = 1
DISPID_SLPLangId = 2
DISPID_SLPPartOfSpeech = 3
DISPID_SLPPhoneIds = 4
DISPID_SLPSymbolic = 5
DISPID_SpeechPhoneConverter = Int32
DISPID_SPCLangId = 1
DISPID_SPCPhoneToId = 2
DISPID_SPCIdToPhone = 3
def _define_ISpeechDataKey_head():
    class ISpeechDataKey(win32more.System.Com.IDispatch_head):
        Guid = Guid('ce17c09b-4efa-44d5-a4c9-59d9585ab0cd')
    return ISpeechDataKey
def _define_ISpeechDataKey():
    ISpeechDataKey = win32more.Media.Speech.ISpeechDataKey_head
    ISpeechDataKey.SetBinaryValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(7, 'SetBinaryValue', ((1, 'ValueName'),(1, 'Value'),)))
    ISpeechDataKey.GetBinaryValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'GetBinaryValue', ((1, 'ValueName'),(1, 'Value'),)))
    ISpeechDataKey.SetStringValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(9, 'SetStringValue', ((1, 'ValueName'),(1, 'Value'),)))
    ISpeechDataKey.GetStringValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'GetStringValue', ((1, 'ValueName'),(1, 'Value'),)))
    ISpeechDataKey.SetLongValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32, use_last_error=False)(11, 'SetLongValue', ((1, 'ValueName'),(1, 'Value'),)))
    ISpeechDataKey.GetLongValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(Int32), use_last_error=False)(12, 'GetLongValue', ((1, 'ValueName'),(1, 'Value'),)))
    ISpeechDataKey.OpenKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Media.Speech.ISpeechDataKey_head), use_last_error=False)(13, 'OpenKey', ((1, 'SubKeyName'),(1, 'SubKey'),)))
    ISpeechDataKey.CreateKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Media.Speech.ISpeechDataKey_head), use_last_error=False)(14, 'CreateKey', ((1, 'SubKeyName'),(1, 'SubKey'),)))
    ISpeechDataKey.DeleteKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(15, 'DeleteKey', ((1, 'SubKeyName'),)))
    ISpeechDataKey.DeleteValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(16, 'DeleteValue', ((1, 'ValueName'),)))
    ISpeechDataKey.EnumKeys = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'EnumKeys', ((1, 'Index'),(1, 'SubKeyName'),)))
    ISpeechDataKey.EnumValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(18, 'EnumValues', ((1, 'Index'),(1, 'ValueName'),)))
    return ISpeechDataKey
def _define_ISpeechObjectToken_head():
    class ISpeechObjectToken(win32more.System.Com.IDispatch_head):
        Guid = Guid('c74a3adc-b727-4500-a84a-b526721c8b8c')
    return ISpeechObjectToken
def _define_ISpeechObjectToken():
    ISpeechObjectToken = win32more.Media.Speech.ISpeechObjectToken_head
    ISpeechObjectToken.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Id', ((1, 'ObjectId'),)))
    ISpeechObjectToken.get_DataKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechDataKey_head), use_last_error=False)(8, 'get_DataKey', ((1, 'DataKey'),)))
    ISpeechObjectToken.get_Category = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechObjectTokenCategory_head), use_last_error=False)(9, 'get_Category', ((1, 'Category'),)))
    ISpeechObjectToken.GetDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'GetDescription', ((1, 'Locale'),(1, 'Description'),)))
    ISpeechObjectToken.SetId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int16, use_last_error=False)(11, 'SetId', ((1, 'Id'),(1, 'CategoryID'),(1, 'CreateIfNotExist'),)))
    ISpeechObjectToken.GetAttribute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'GetAttribute', ((1, 'AttributeName'),(1, 'AttributeValue'),)))
    ISpeechObjectToken.CreateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Media.Speech.SpeechTokenContext,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(13, 'CreateInstance', ((1, 'pUnkOuter'),(1, 'ClsContext'),(1, 'Object'),)))
    ISpeechObjectToken.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(14, 'Remove', ((1, 'ObjectStorageCLSID'),)))
    ISpeechObjectToken.GetStorageFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Media.Speech.SpeechTokenShellFolder,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'GetStorageFileName', ((1, 'ObjectStorageCLSID'),(1, 'KeyName'),(1, 'FileName'),(1, 'Folder'),(1, 'FilePath'),)))
    ISpeechObjectToken.RemoveStorageFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int16, use_last_error=False)(16, 'RemoveStorageFileName', ((1, 'ObjectStorageCLSID'),(1, 'KeyName'),(1, 'DeleteFileA'),)))
    ISpeechObjectToken.IsUISupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),win32more.System.Com.IUnknown_head,POINTER(Int16), use_last_error=False)(17, 'IsUISupported', ((1, 'TypeOfUI'),(1, 'ExtraData'),(1, 'Object'),(1, 'Supported'),)))
    ISpeechObjectToken.DisplayUI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),win32more.System.Com.IUnknown_head, use_last_error=False)(18, 'DisplayUI', ((1, 'hWnd'),(1, 'Title'),(1, 'TypeOfUI'),(1, 'ExtraData'),(1, 'Object'),)))
    ISpeechObjectToken.MatchesAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(Int16), use_last_error=False)(19, 'MatchesAttributes', ((1, 'Attributes'),(1, 'Matches'),)))
    return ISpeechObjectToken
def _define_ISpeechObjectTokens_head():
    class ISpeechObjectTokens(win32more.System.Com.IDispatch_head):
        Guid = Guid('9285b776-2e7b-4bc0-b53e-580eb6fa967f')
    return ISpeechObjectTokens
def _define_ISpeechObjectTokens():
    ISpeechObjectTokens = win32more.Media.Speech.ISpeechObjectTokens_head
    ISpeechObjectTokens.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'Count'),)))
    ISpeechObjectTokens.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Media.Speech.ISpeechObjectToken_head), use_last_error=False)(8, 'Item', ((1, 'Index'),(1, 'Token'),)))
    ISpeechObjectTokens.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'ppEnumVARIANT'),)))
    return ISpeechObjectTokens
def _define_ISpeechObjectTokenCategory_head():
    class ISpeechObjectTokenCategory(win32more.System.Com.IDispatch_head):
        Guid = Guid('ca7eac50-2d01-4145-86d4-5ae7d70f4469')
    return ISpeechObjectTokenCategory
def _define_ISpeechObjectTokenCategory():
    ISpeechObjectTokenCategory = win32more.Media.Speech.ISpeechObjectTokenCategory_head
    ISpeechObjectTokenCategory.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Id', ((1, 'Id'),)))
    ISpeechObjectTokenCategory.put_Default = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_Default', ((1, 'TokenId'),)))
    ISpeechObjectTokenCategory.get_Default = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_Default', ((1, 'TokenId'),)))
    ISpeechObjectTokenCategory.SetId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int16, use_last_error=False)(10, 'SetId', ((1, 'Id'),(1, 'CreateIfNotExist'),)))
    ISpeechObjectTokenCategory.GetDataKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SpeechDataKeyLocation,POINTER(win32more.Media.Speech.ISpeechDataKey_head), use_last_error=False)(11, 'GetDataKey', ((1, 'Location'),(1, 'DataKey'),)))
    ISpeechObjectTokenCategory.EnumerateTokens = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.Media.Speech.ISpeechObjectTokens_head), use_last_error=False)(12, 'EnumerateTokens', ((1, 'RequiredAttributes'),(1, 'OptionalAttributes'),(1, 'Tokens'),)))
    return ISpeechObjectTokenCategory
def _define_ISpeechAudioBufferInfo_head():
    class ISpeechAudioBufferInfo(win32more.System.Com.IDispatch_head):
        Guid = Guid('11b103d8-1142-4edf-a093-82fb3915f8cc')
    return ISpeechAudioBufferInfo
def _define_ISpeechAudioBufferInfo():
    ISpeechAudioBufferInfo = win32more.Media.Speech.ISpeechAudioBufferInfo_head
    ISpeechAudioBufferInfo.get_MinNotification = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_MinNotification', ((1, 'MinNotification'),)))
    ISpeechAudioBufferInfo.put_MinNotification = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(8, 'put_MinNotification', ((1, 'MinNotification'),)))
    ISpeechAudioBufferInfo.get_BufferSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_BufferSize', ((1, 'BufferSize'),)))
    ISpeechAudioBufferInfo.put_BufferSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(10, 'put_BufferSize', ((1, 'BufferSize'),)))
    ISpeechAudioBufferInfo.get_EventBias = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'get_EventBias', ((1, 'EventBias'),)))
    ISpeechAudioBufferInfo.put_EventBias = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(12, 'put_EventBias', ((1, 'EventBias'),)))
    return ISpeechAudioBufferInfo
def _define_ISpeechAudioStatus_head():
    class ISpeechAudioStatus(win32more.System.Com.IDispatch_head):
        Guid = Guid('c62d9c91-7458-47f6-862d-1ef86fb0b278')
    return ISpeechAudioStatus
def _define_ISpeechAudioStatus():
    ISpeechAudioStatus = win32more.Media.Speech.ISpeechAudioStatus_head
    ISpeechAudioStatus.get_FreeBufferSpace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_FreeBufferSpace', ((1, 'FreeBufferSpace'),)))
    ISpeechAudioStatus.get_NonBlockingIO = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_NonBlockingIO', ((1, 'NonBlockingIO'),)))
    ISpeechAudioStatus.get_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SpeechAudioState), use_last_error=False)(9, 'get_State', ((1, 'State'),)))
    ISpeechAudioStatus.get_CurrentSeekPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(10, 'get_CurrentSeekPosition', ((1, 'CurrentSeekPosition'),)))
    ISpeechAudioStatus.get_CurrentDevicePosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(11, 'get_CurrentDevicePosition', ((1, 'CurrentDevicePosition'),)))
    return ISpeechAudioStatus
def _define_ISpeechAudioFormat_head():
    class ISpeechAudioFormat(win32more.System.Com.IDispatch_head):
        Guid = Guid('e6e9c590-3e18-40e3-8299-061f98bde7c7')
    return ISpeechAudioFormat
def _define_ISpeechAudioFormat():
    ISpeechAudioFormat = win32more.Media.Speech.ISpeechAudioFormat_head
    ISpeechAudioFormat.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SpeechAudioFormatType), use_last_error=False)(7, 'get_Type', ((1, 'AudioFormat'),)))
    ISpeechAudioFormat.put_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SpeechAudioFormatType, use_last_error=False)(8, 'put_Type', ((1, 'AudioFormat'),)))
    ISpeechAudioFormat.get_Guid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_Guid', ((1, 'Guid'),)))
    ISpeechAudioFormat.put_Guid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_Guid', ((1, 'Guid'),)))
    ISpeechAudioFormat.GetWaveFormatEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechWaveFormatEx_head), use_last_error=False)(11, 'GetWaveFormatEx', ((1, 'SpeechWaveFormatEx'),)))
    ISpeechAudioFormat.SetWaveFormatEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpeechWaveFormatEx_head, use_last_error=False)(12, 'SetWaveFormatEx', ((1, 'SpeechWaveFormatEx'),)))
    return ISpeechAudioFormat
def _define_ISpeechWaveFormatEx_head():
    class ISpeechWaveFormatEx(win32more.System.Com.IDispatch_head):
        Guid = Guid('7a1ef0d5-1581-4741-88e4-209a49f11a10')
    return ISpeechWaveFormatEx
def _define_ISpeechWaveFormatEx():
    ISpeechWaveFormatEx = win32more.Media.Speech.ISpeechWaveFormatEx_head
    ISpeechWaveFormatEx.get_FormatTag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(7, 'get_FormatTag', ((1, 'FormatTag'),)))
    ISpeechWaveFormatEx.put_FormatTag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(8, 'put_FormatTag', ((1, 'FormatTag'),)))
    ISpeechWaveFormatEx.get_Channels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(9, 'get_Channels', ((1, 'Channels'),)))
    ISpeechWaveFormatEx.put_Channels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(10, 'put_Channels', ((1, 'Channels'),)))
    ISpeechWaveFormatEx.get_SamplesPerSec = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'get_SamplesPerSec', ((1, 'SamplesPerSec'),)))
    ISpeechWaveFormatEx.put_SamplesPerSec = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(12, 'put_SamplesPerSec', ((1, 'SamplesPerSec'),)))
    ISpeechWaveFormatEx.get_AvgBytesPerSec = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'get_AvgBytesPerSec', ((1, 'AvgBytesPerSec'),)))
    ISpeechWaveFormatEx.put_AvgBytesPerSec = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(14, 'put_AvgBytesPerSec', ((1, 'AvgBytesPerSec'),)))
    ISpeechWaveFormatEx.get_BlockAlign = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(15, 'get_BlockAlign', ((1, 'BlockAlign'),)))
    ISpeechWaveFormatEx.put_BlockAlign = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(16, 'put_BlockAlign', ((1, 'BlockAlign'),)))
    ISpeechWaveFormatEx.get_BitsPerSample = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(17, 'get_BitsPerSample', ((1, 'BitsPerSample'),)))
    ISpeechWaveFormatEx.put_BitsPerSample = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(18, 'put_BitsPerSample', ((1, 'BitsPerSample'),)))
    ISpeechWaveFormatEx.get_ExtraData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(19, 'get_ExtraData', ((1, 'ExtraData'),)))
    ISpeechWaveFormatEx.put_ExtraData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(20, 'put_ExtraData', ((1, 'ExtraData'),)))
    return ISpeechWaveFormatEx
def _define_ISpeechBaseStream_head():
    class ISpeechBaseStream(win32more.System.Com.IDispatch_head):
        Guid = Guid('6450336f-7d49-4ced-8097-49d6dee37294')
    return ISpeechBaseStream
def _define_ISpeechBaseStream():
    ISpeechBaseStream = win32more.Media.Speech.ISpeechBaseStream_head
    ISpeechBaseStream.get_Format = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechAudioFormat_head), use_last_error=False)(7, 'get_Format', ((1, 'AudioFormat'),)))
    ISpeechBaseStream.putref_Format = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpeechAudioFormat_head, use_last_error=False)(8, 'putref_Format', ((1, 'AudioFormat'),)))
    ISpeechBaseStream.Read = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),Int32,POINTER(Int32), use_last_error=False)(9, 'Read', ((1, 'Buffer'),(1, 'NumberOfBytes'),(1, 'BytesRead'),)))
    ISpeechBaseStream.Write = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(Int32), use_last_error=False)(10, 'Write', ((1, 'Buffer'),(1, 'BytesWritten'),)))
    ISpeechBaseStream.Seek = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,win32more.Media.Speech.SpeechStreamSeekPositionType,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(11, 'Seek', ((1, 'Position'),(1, 'Origin'),(1, 'NewPosition'),)))
    return ISpeechBaseStream
def _define_ISpeechFileStream_head():
    class ISpeechFileStream(win32more.Media.Speech.ISpeechBaseStream_head):
        Guid = Guid('af67f125-ab39-4e93-b4a2-cc2e66e182a7')
    return ISpeechFileStream
def _define_ISpeechFileStream():
    ISpeechFileStream = win32more.Media.Speech.ISpeechFileStream_head
    ISpeechFileStream.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Media.Speech.SpeechStreamFileMode,Int16, use_last_error=False)(12, 'Open', ((1, 'FileName'),(1, 'FileMode'),(1, 'DoEvents'),)))
    ISpeechFileStream.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(13, 'Close', ()))
    return ISpeechFileStream
def _define_ISpeechMemoryStream_head():
    class ISpeechMemoryStream(win32more.Media.Speech.ISpeechBaseStream_head):
        Guid = Guid('eeb14b68-808b-4abe-a5ea-b51da7588008')
    return ISpeechMemoryStream
def _define_ISpeechMemoryStream():
    ISpeechMemoryStream = win32more.Media.Speech.ISpeechMemoryStream_head
    ISpeechMemoryStream.SetData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(12, 'SetData', ((1, 'Data'),)))
    ISpeechMemoryStream.GetData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(13, 'GetData', ((1, 'pData'),)))
    return ISpeechMemoryStream
def _define_ISpeechCustomStream_head():
    class ISpeechCustomStream(win32more.Media.Speech.ISpeechBaseStream_head):
        Guid = Guid('1a9e9f4f-104f-4db8-a115-efd7fd0c97ae')
    return ISpeechCustomStream
def _define_ISpeechCustomStream():
    ISpeechCustomStream = win32more.Media.Speech.ISpeechCustomStream_head
    ISpeechCustomStream.get_BaseStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(12, 'get_BaseStream', ((1, 'ppUnkStream'),)))
    ISpeechCustomStream.putref_BaseStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(13, 'putref_BaseStream', ((1, 'pUnkStream'),)))
    return ISpeechCustomStream
def _define_ISpeechAudio_head():
    class ISpeechAudio(win32more.Media.Speech.ISpeechBaseStream_head):
        Guid = Guid('cff8e175-019e-11d3-a08e-00c04f8ef9b5')
    return ISpeechAudio
def _define_ISpeechAudio():
    ISpeechAudio = win32more.Media.Speech.ISpeechAudio_head
    ISpeechAudio.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechAudioStatus_head), use_last_error=False)(12, 'get_Status', ((1, 'Status'),)))
    ISpeechAudio.get_BufferInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechAudioBufferInfo_head), use_last_error=False)(13, 'get_BufferInfo', ((1, 'BufferInfo'),)))
    ISpeechAudio.get_DefaultFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechAudioFormat_head), use_last_error=False)(14, 'get_DefaultFormat', ((1, 'StreamFormat'),)))
    ISpeechAudio.get_Volume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(15, 'get_Volume', ((1, 'Volume'),)))
    ISpeechAudio.put_Volume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(16, 'put_Volume', ((1, 'Volume'),)))
    ISpeechAudio.get_BufferNotifySize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(17, 'get_BufferNotifySize', ((1, 'BufferNotifySize'),)))
    ISpeechAudio.put_BufferNotifySize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(18, 'put_BufferNotifySize', ((1, 'BufferNotifySize'),)))
    ISpeechAudio.get_EventHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(19, 'get_EventHandle', ((1, 'EventHandle'),)))
    ISpeechAudio.SetState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SpeechAudioState, use_last_error=False)(20, 'SetState', ((1, 'State'),)))
    return ISpeechAudio
def _define_ISpeechMMSysAudio_head():
    class ISpeechMMSysAudio(win32more.Media.Speech.ISpeechAudio_head):
        Guid = Guid('3c76af6d-1fd7-4831-81d1-3b71d5a13c44')
    return ISpeechMMSysAudio
def _define_ISpeechMMSysAudio():
    ISpeechMMSysAudio = win32more.Media.Speech.ISpeechMMSysAudio_head
    ISpeechMMSysAudio.get_DeviceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(21, 'get_DeviceId', ((1, 'DeviceId'),)))
    ISpeechMMSysAudio.put_DeviceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(22, 'put_DeviceId', ((1, 'DeviceId'),)))
    ISpeechMMSysAudio.get_LineId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(23, 'get_LineId', ((1, 'LineId'),)))
    ISpeechMMSysAudio.put_LineId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(24, 'put_LineId', ((1, 'LineId'),)))
    ISpeechMMSysAudio.get_MMHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(25, 'get_MMHandle', ((1, 'Handle'),)))
    return ISpeechMMSysAudio
def _define_ISpeechVoice_head():
    class ISpeechVoice(win32more.System.Com.IDispatch_head):
        Guid = Guid('269316d8-57bd-11d2-9eee-00c04f797396')
    return ISpeechVoice
def _define_ISpeechVoice():
    ISpeechVoice = win32more.Media.Speech.ISpeechVoice_head
    ISpeechVoice.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechVoiceStatus_head), use_last_error=False)(7, 'get_Status', ((1, 'Status'),)))
    ISpeechVoice.get_Voice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechObjectToken_head), use_last_error=False)(8, 'get_Voice', ((1, 'Voice'),)))
    ISpeechVoice.putref_Voice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpeechObjectToken_head, use_last_error=False)(9, 'putref_Voice', ((1, 'Voice'),)))
    ISpeechVoice.get_AudioOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechObjectToken_head), use_last_error=False)(10, 'get_AudioOutput', ((1, 'AudioOutput'),)))
    ISpeechVoice.putref_AudioOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpeechObjectToken_head, use_last_error=False)(11, 'putref_AudioOutput', ((1, 'AudioOutput'),)))
    ISpeechVoice.get_AudioOutputStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechBaseStream_head), use_last_error=False)(12, 'get_AudioOutputStream', ((1, 'AudioOutputStream'),)))
    ISpeechVoice.putref_AudioOutputStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpeechBaseStream_head, use_last_error=False)(13, 'putref_AudioOutputStream', ((1, 'AudioOutputStream'),)))
    ISpeechVoice.get_Rate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(14, 'get_Rate', ((1, 'Rate'),)))
    ISpeechVoice.put_Rate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(15, 'put_Rate', ((1, 'Rate'),)))
    ISpeechVoice.get_Volume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(16, 'get_Volume', ((1, 'Volume'),)))
    ISpeechVoice.put_Volume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(17, 'put_Volume', ((1, 'Volume'),)))
    ISpeechVoice.put_AllowAudioOutputFormatChangesOnNextSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(18, 'put_AllowAudioOutputFormatChangesOnNextSet', ((1, 'Allow'),)))
    ISpeechVoice.get_AllowAudioOutputFormatChangesOnNextSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(19, 'get_AllowAudioOutputFormatChangesOnNextSet', ((1, 'Allow'),)))
    ISpeechVoice.get_EventInterests = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SpeechVoiceEvents), use_last_error=False)(20, 'get_EventInterests', ((1, 'EventInterestFlags'),)))
    ISpeechVoice.put_EventInterests = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SpeechVoiceEvents, use_last_error=False)(21, 'put_EventInterests', ((1, 'EventInterestFlags'),)))
    ISpeechVoice.put_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SpeechVoicePriority, use_last_error=False)(22, 'put_Priority', ((1, 'Priority'),)))
    ISpeechVoice.get_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SpeechVoicePriority), use_last_error=False)(23, 'get_Priority', ((1, 'Priority'),)))
    ISpeechVoice.put_AlertBoundary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SpeechVoiceEvents, use_last_error=False)(24, 'put_AlertBoundary', ((1, 'Boundary'),)))
    ISpeechVoice.get_AlertBoundary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SpeechVoiceEvents), use_last_error=False)(25, 'get_AlertBoundary', ((1, 'Boundary'),)))
    ISpeechVoice.put_SynchronousSpeakTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(26, 'put_SynchronousSpeakTimeout', ((1, 'msTimeout'),)))
    ISpeechVoice.get_SynchronousSpeakTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(27, 'get_SynchronousSpeakTimeout', ((1, 'msTimeout'),)))
    ISpeechVoice.Speak = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Media.Speech.SpeechVoiceSpeakFlags,POINTER(Int32), use_last_error=False)(28, 'Speak', ((1, 'Text'),(1, 'Flags'),(1, 'StreamNumber'),)))
    ISpeechVoice.SpeakStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpeechBaseStream_head,win32more.Media.Speech.SpeechVoiceSpeakFlags,POINTER(Int32), use_last_error=False)(29, 'SpeakStream', ((1, 'Stream'),(1, 'Flags'),(1, 'StreamNumber'),)))
    ISpeechVoice.Pause = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(30, 'Pause', ()))
    ISpeechVoice.Resume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(31, 'Resume', ()))
    ISpeechVoice.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,POINTER(Int32), use_last_error=False)(32, 'Skip', ((1, 'Type'),(1, 'NumItems'),(1, 'NumSkipped'),)))
    ISpeechVoice.GetVoices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.Media.Speech.ISpeechObjectTokens_head), use_last_error=False)(33, 'GetVoices', ((1, 'RequiredAttributes'),(1, 'OptionalAttributes'),(1, 'ObjectTokens'),)))
    ISpeechVoice.GetAudioOutputs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.Media.Speech.ISpeechObjectTokens_head), use_last_error=False)(34, 'GetAudioOutputs', ((1, 'RequiredAttributes'),(1, 'OptionalAttributes'),(1, 'ObjectTokens'),)))
    ISpeechVoice.WaitUntilDone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int16), use_last_error=False)(35, 'WaitUntilDone', ((1, 'msTimeout'),(1, 'Done'),)))
    ISpeechVoice.SpeakCompleteEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(36, 'SpeakCompleteEvent', ((1, 'Handle'),)))
    ISpeechVoice.IsUISupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),POINTER(Int16), use_last_error=False)(37, 'IsUISupported', ((1, 'TypeOfUI'),(1, 'ExtraData'),(1, 'Supported'),)))
    ISpeechVoice.DisplayUI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(38, 'DisplayUI', ((1, 'hWndParent'),(1, 'Title'),(1, 'TypeOfUI'),(1, 'ExtraData'),)))
    return ISpeechVoice
def _define_ISpeechVoiceStatus_head():
    class ISpeechVoiceStatus(win32more.System.Com.IDispatch_head):
        Guid = Guid('8be47b07-57f6-11d2-9eee-00c04f797396')
    return ISpeechVoiceStatus
def _define_ISpeechVoiceStatus():
    ISpeechVoiceStatus = win32more.Media.Speech.ISpeechVoiceStatus_head
    ISpeechVoiceStatus.get_CurrentStreamNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_CurrentStreamNumber', ((1, 'StreamNumber'),)))
    ISpeechVoiceStatus.get_LastStreamNumberQueued = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_LastStreamNumberQueued', ((1, 'StreamNumber'),)))
    ISpeechVoiceStatus.get_LastHResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_LastHResult', ((1, 'HResult'),)))
    ISpeechVoiceStatus.get_RunningState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SpeechRunState), use_last_error=False)(10, 'get_RunningState', ((1, 'State'),)))
    ISpeechVoiceStatus.get_InputWordPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'get_InputWordPosition', ((1, 'Position'),)))
    ISpeechVoiceStatus.get_InputWordLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(12, 'get_InputWordLength', ((1, 'Length'),)))
    ISpeechVoiceStatus.get_InputSentencePosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'get_InputSentencePosition', ((1, 'Position'),)))
    ISpeechVoiceStatus.get_InputSentenceLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(14, 'get_InputSentenceLength', ((1, 'Length'),)))
    ISpeechVoiceStatus.get_LastBookmark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_LastBookmark', ((1, 'Bookmark'),)))
    ISpeechVoiceStatus.get_LastBookmarkId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(16, 'get_LastBookmarkId', ((1, 'BookmarkId'),)))
    ISpeechVoiceStatus.get_PhonemeId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(17, 'get_PhonemeId', ((1, 'PhoneId'),)))
    ISpeechVoiceStatus.get_VisemeId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(18, 'get_VisemeId', ((1, 'VisemeId'),)))
    return ISpeechVoiceStatus
def _define__ISpeechVoiceEvents_head():
    class _ISpeechVoiceEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('a372acd1-3bef-4bbd-8ffb-cb3e2b416af8')
    return _ISpeechVoiceEvents
def _define__ISpeechVoiceEvents():
    _ISpeechVoiceEvents = win32more.Media.Speech._ISpeechVoiceEvents_head
    return _ISpeechVoiceEvents
def _define_ISpeechRecognizer_head():
    class ISpeechRecognizer(win32more.System.Com.IDispatch_head):
        Guid = Guid('2d5f1c0c-bd75-4b08-9478-3b11fea2586c')
    return ISpeechRecognizer
def _define_ISpeechRecognizer():
    ISpeechRecognizer = win32more.Media.Speech.ISpeechRecognizer_head
    ISpeechRecognizer.putref_Recognizer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpeechObjectToken_head, use_last_error=False)(7, 'putref_Recognizer', ((1, 'Recognizer'),)))
    ISpeechRecognizer.get_Recognizer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechObjectToken_head), use_last_error=False)(8, 'get_Recognizer', ((1, 'Recognizer'),)))
    ISpeechRecognizer.put_AllowAudioInputFormatChangesOnNextSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(9, 'put_AllowAudioInputFormatChangesOnNextSet', ((1, 'Allow'),)))
    ISpeechRecognizer.get_AllowAudioInputFormatChangesOnNextSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(10, 'get_AllowAudioInputFormatChangesOnNextSet', ((1, 'Allow'),)))
    ISpeechRecognizer.putref_AudioInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpeechObjectToken_head, use_last_error=False)(11, 'putref_AudioInput', ((1, 'AudioInput'),)))
    ISpeechRecognizer.get_AudioInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechObjectToken_head), use_last_error=False)(12, 'get_AudioInput', ((1, 'AudioInput'),)))
    ISpeechRecognizer.putref_AudioInputStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpeechBaseStream_head, use_last_error=False)(13, 'putref_AudioInputStream', ((1, 'AudioInputStream'),)))
    ISpeechRecognizer.get_AudioInputStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechBaseStream_head), use_last_error=False)(14, 'get_AudioInputStream', ((1, 'AudioInputStream'),)))
    ISpeechRecognizer.get_IsShared = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(15, 'get_IsShared', ((1, 'Shared'),)))
    ISpeechRecognizer.put_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SpeechRecognizerState, use_last_error=False)(16, 'put_State', ((1, 'State'),)))
    ISpeechRecognizer.get_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SpeechRecognizerState), use_last_error=False)(17, 'get_State', ((1, 'State'),)))
    ISpeechRecognizer.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechRecognizerStatus_head), use_last_error=False)(18, 'get_Status', ((1, 'Status'),)))
    ISpeechRecognizer.putref_Profile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpeechObjectToken_head, use_last_error=False)(19, 'putref_Profile', ((1, 'Profile'),)))
    ISpeechRecognizer.get_Profile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechObjectToken_head), use_last_error=False)(20, 'get_Profile', ((1, 'Profile'),)))
    ISpeechRecognizer.EmulateRecognition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head),Int32, use_last_error=False)(21, 'EmulateRecognition', ((1, 'TextElements'),(1, 'ElementDisplayAttributes'),(1, 'LanguageId'),)))
    ISpeechRecognizer.CreateRecoContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechRecoContext_head), use_last_error=False)(22, 'CreateRecoContext', ((1, 'NewContext'),)))
    ISpeechRecognizer.GetFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SpeechFormatType,POINTER(win32more.Media.Speech.ISpeechAudioFormat_head), use_last_error=False)(23, 'GetFormat', ((1, 'Type'),(1, 'Format'),)))
    ISpeechRecognizer.SetPropertyNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,POINTER(Int16), use_last_error=False)(24, 'SetPropertyNumber', ((1, 'Name'),(1, 'Value'),(1, 'Supported'),)))
    ISpeechRecognizer.GetPropertyNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(Int32),POINTER(Int16), use_last_error=False)(25, 'GetPropertyNumber', ((1, 'Name'),(1, 'Value'),(1, 'Supported'),)))
    ISpeechRecognizer.SetPropertyString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(Int16), use_last_error=False)(26, 'SetPropertyString', ((1, 'Name'),(1, 'Value'),(1, 'Supported'),)))
    ISpeechRecognizer.GetPropertyString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR),POINTER(Int16), use_last_error=False)(27, 'GetPropertyString', ((1, 'Name'),(1, 'Value'),(1, 'Supported'),)))
    ISpeechRecognizer.IsUISupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),POINTER(Int16), use_last_error=False)(28, 'IsUISupported', ((1, 'TypeOfUI'),(1, 'ExtraData'),(1, 'Supported'),)))
    ISpeechRecognizer.DisplayUI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(29, 'DisplayUI', ((1, 'hWndParent'),(1, 'Title'),(1, 'TypeOfUI'),(1, 'ExtraData'),)))
    ISpeechRecognizer.GetRecognizers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.Media.Speech.ISpeechObjectTokens_head), use_last_error=False)(30, 'GetRecognizers', ((1, 'RequiredAttributes'),(1, 'OptionalAttributes'),(1, 'ObjectTokens'),)))
    ISpeechRecognizer.GetAudioInputs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.Media.Speech.ISpeechObjectTokens_head), use_last_error=False)(31, 'GetAudioInputs', ((1, 'RequiredAttributes'),(1, 'OptionalAttributes'),(1, 'ObjectTokens'),)))
    ISpeechRecognizer.GetProfiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.Media.Speech.ISpeechObjectTokens_head), use_last_error=False)(32, 'GetProfiles', ((1, 'RequiredAttributes'),(1, 'OptionalAttributes'),(1, 'ObjectTokens'),)))
    return ISpeechRecognizer
def _define_ISpeechRecognizerStatus_head():
    class ISpeechRecognizerStatus(win32more.System.Com.IDispatch_head):
        Guid = Guid('bff9e781-53ec-484e-bb8a-0e1b5551e35c')
    return ISpeechRecognizerStatus
def _define_ISpeechRecognizerStatus():
    ISpeechRecognizerStatus = win32more.Media.Speech.ISpeechRecognizerStatus_head
    ISpeechRecognizerStatus.get_AudioStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechAudioStatus_head), use_last_error=False)(7, 'get_AudioStatus', ((1, 'AudioStatus'),)))
    ISpeechRecognizerStatus.get_CurrentStreamPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'get_CurrentStreamPosition', ((1, 'pCurrentStreamPos'),)))
    ISpeechRecognizerStatus.get_CurrentStreamNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_CurrentStreamNumber', ((1, 'StreamNumber'),)))
    ISpeechRecognizerStatus.get_NumberOfActiveRules = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_NumberOfActiveRules', ((1, 'NumberOfActiveRules'),)))
    ISpeechRecognizerStatus.get_ClsidEngine = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_ClsidEngine', ((1, 'ClsidEngine'),)))
    ISpeechRecognizerStatus.get_SupportedLanguages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(12, 'get_SupportedLanguages', ((1, 'SupportedLanguages'),)))
    return ISpeechRecognizerStatus
def _define_ISpeechRecoContext_head():
    class ISpeechRecoContext(win32more.System.Com.IDispatch_head):
        Guid = Guid('580aa49d-7e1e-4809-b8e2-57da806104b8')
    return ISpeechRecoContext
def _define_ISpeechRecoContext():
    ISpeechRecoContext = win32more.Media.Speech.ISpeechRecoContext_head
    ISpeechRecoContext.get_Recognizer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechRecognizer_head), use_last_error=False)(7, 'get_Recognizer', ((1, 'Recognizer'),)))
    ISpeechRecoContext.get_AudioInputInterferenceStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SpeechInterference), use_last_error=False)(8, 'get_AudioInputInterferenceStatus', ((1, 'Interference'),)))
    ISpeechRecoContext.get_RequestedUIType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_RequestedUIType', ((1, 'UIType'),)))
    ISpeechRecoContext.putref_Voice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpeechVoice_head, use_last_error=False)(10, 'putref_Voice', ((1, 'Voice'),)))
    ISpeechRecoContext.get_Voice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechVoice_head), use_last_error=False)(11, 'get_Voice', ((1, 'Voice'),)))
    ISpeechRecoContext.put_AllowVoiceFormatMatchingOnNextSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(12, 'put_AllowVoiceFormatMatchingOnNextSet', ((1, 'Allow'),)))
    ISpeechRecoContext.get_AllowVoiceFormatMatchingOnNextSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(13, 'get_AllowVoiceFormatMatchingOnNextSet', ((1, 'pAllow'),)))
    ISpeechRecoContext.put_VoicePurgeEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SpeechRecoEvents, use_last_error=False)(14, 'put_VoicePurgeEvent', ((1, 'EventInterest'),)))
    ISpeechRecoContext.get_VoicePurgeEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SpeechRecoEvents), use_last_error=False)(15, 'get_VoicePurgeEvent', ((1, 'EventInterest'),)))
    ISpeechRecoContext.put_EventInterests = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SpeechRecoEvents, use_last_error=False)(16, 'put_EventInterests', ((1, 'EventInterest'),)))
    ISpeechRecoContext.get_EventInterests = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SpeechRecoEvents), use_last_error=False)(17, 'get_EventInterests', ((1, 'EventInterest'),)))
    ISpeechRecoContext.put_CmdMaxAlternates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(18, 'put_CmdMaxAlternates', ((1, 'MaxAlternates'),)))
    ISpeechRecoContext.get_CmdMaxAlternates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(19, 'get_CmdMaxAlternates', ((1, 'MaxAlternates'),)))
    ISpeechRecoContext.put_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SpeechRecoContextState, use_last_error=False)(20, 'put_State', ((1, 'State'),)))
    ISpeechRecoContext.get_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SpeechRecoContextState), use_last_error=False)(21, 'get_State', ((1, 'State'),)))
    ISpeechRecoContext.put_RetainedAudio = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SpeechRetainedAudioOptions, use_last_error=False)(22, 'put_RetainedAudio', ((1, 'Option'),)))
    ISpeechRecoContext.get_RetainedAudio = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SpeechRetainedAudioOptions), use_last_error=False)(23, 'get_RetainedAudio', ((1, 'Option'),)))
    ISpeechRecoContext.putref_RetainedAudioFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpeechAudioFormat_head, use_last_error=False)(24, 'putref_RetainedAudioFormat', ((1, 'Format'),)))
    ISpeechRecoContext.get_RetainedAudioFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechAudioFormat_head), use_last_error=False)(25, 'get_RetainedAudioFormat', ((1, 'Format'),)))
    ISpeechRecoContext.Pause = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(26, 'Pause', ()))
    ISpeechRecoContext.Resume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(27, 'Resume', ()))
    ISpeechRecoContext.CreateGrammar = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Media.Speech.ISpeechRecoGrammar_head), use_last_error=False)(28, 'CreateGrammar', ((1, 'GrammarId'),(1, 'Grammar'),)))
    ISpeechRecoContext.CreateResultFromMemory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.Media.Speech.ISpeechRecoResult_head), use_last_error=False)(29, 'CreateResultFromMemory', ((1, 'ResultBlock'),(1, 'Result'),)))
    ISpeechRecoContext.Bookmark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SpeechBookmarkOptions,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT, use_last_error=False)(30, 'Bookmark', ((1, 'Options'),(1, 'StreamPos'),(1, 'BookmarkId'),)))
    ISpeechRecoContext.SetAdaptationData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(31, 'SetAdaptationData', ((1, 'AdaptationString'),)))
    return ISpeechRecoContext
def _define_ISpeechRecoGrammar_head():
    class ISpeechRecoGrammar(win32more.System.Com.IDispatch_head):
        Guid = Guid('b6d6f79f-2158-4e50-b5bc-9a9ccd852a09')
    return ISpeechRecoGrammar
def _define_ISpeechRecoGrammar():
    ISpeechRecoGrammar = win32more.Media.Speech.ISpeechRecoGrammar_head
    ISpeechRecoGrammar.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_Id', ((1, 'Id'),)))
    ISpeechRecoGrammar.get_RecoContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechRecoContext_head), use_last_error=False)(8, 'get_RecoContext', ((1, 'RecoContext'),)))
    ISpeechRecoGrammar.put_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SpeechGrammarState, use_last_error=False)(9, 'put_State', ((1, 'State'),)))
    ISpeechRecoGrammar.get_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SpeechGrammarState), use_last_error=False)(10, 'get_State', ((1, 'State'),)))
    ISpeechRecoGrammar.get_Rules = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechGrammarRules_head), use_last_error=False)(11, 'get_Rules', ((1, 'Rules'),)))
    ISpeechRecoGrammar.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(12, 'Reset', ((1, 'NewLanguage'),)))
    ISpeechRecoGrammar.CmdLoadFromFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Media.Speech.SpeechLoadOption, use_last_error=False)(13, 'CmdLoadFromFile', ((1, 'FileName'),(1, 'LoadOption'),)))
    ISpeechRecoGrammar.CmdLoadFromObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Media.Speech.SpeechLoadOption, use_last_error=False)(14, 'CmdLoadFromObject', ((1, 'ClassId'),(1, 'GrammarName'),(1, 'LoadOption'),)))
    ISpeechRecoGrammar.CmdLoadFromResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT,Int32,win32more.Media.Speech.SpeechLoadOption, use_last_error=False)(15, 'CmdLoadFromResource', ((1, 'hModule'),(1, 'ResourceName'),(1, 'ResourceType'),(1, 'LanguageId'),(1, 'LoadOption'),)))
    ISpeechRecoGrammar.CmdLoadFromMemory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,win32more.Media.Speech.SpeechLoadOption, use_last_error=False)(16, 'CmdLoadFromMemory', ((1, 'GrammarData'),(1, 'LoadOption'),)))
    ISpeechRecoGrammar.CmdLoadFromProprietaryGrammar = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,win32more.Media.Speech.SpeechLoadOption, use_last_error=False)(17, 'CmdLoadFromProprietaryGrammar', ((1, 'ProprietaryGuid'),(1, 'ProprietaryString'),(1, 'ProprietaryData'),(1, 'LoadOption'),)))
    ISpeechRecoGrammar.CmdSetRuleState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Media.Speech.SpeechRuleState, use_last_error=False)(18, 'CmdSetRuleState', ((1, 'Name'),(1, 'State'),)))
    ISpeechRecoGrammar.CmdSetRuleIdState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Media.Speech.SpeechRuleState, use_last_error=False)(19, 'CmdSetRuleIdState', ((1, 'RuleId'),(1, 'State'),)))
    ISpeechRecoGrammar.DictationLoad = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Media.Speech.SpeechLoadOption, use_last_error=False)(20, 'DictationLoad', ((1, 'TopicName'),(1, 'LoadOption'),)))
    ISpeechRecoGrammar.DictationUnload = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(21, 'DictationUnload', ()))
    ISpeechRecoGrammar.DictationSetState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SpeechRuleState, use_last_error=False)(22, 'DictationSetState', ((1, 'State'),)))
    ISpeechRecoGrammar.SetWordSequenceData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.Media.Speech.ISpeechTextSelectionInformation_head, use_last_error=False)(23, 'SetWordSequenceData', ((1, 'Text'),(1, 'TextLength'),(1, 'Info'),)))
    ISpeechRecoGrammar.SetTextSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpeechTextSelectionInformation_head, use_last_error=False)(24, 'SetTextSelection', ((1, 'Info'),)))
    ISpeechRecoGrammar.IsPronounceable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Media.Speech.SpeechWordPronounceable), use_last_error=False)(25, 'IsPronounceable', ((1, 'Word'),(1, 'WordPronounceable'),)))
    return ISpeechRecoGrammar
def _define__ISpeechRecoContextEvents_head():
    class _ISpeechRecoContextEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('7b8fcb42-0e9d-4f00-a048-7b04d6179d3d')
    return _ISpeechRecoContextEvents
def _define__ISpeechRecoContextEvents():
    _ISpeechRecoContextEvents = win32more.Media.Speech._ISpeechRecoContextEvents_head
    return _ISpeechRecoContextEvents
def _define_ISpeechGrammarRule_head():
    class ISpeechGrammarRule(win32more.System.Com.IDispatch_head):
        Guid = Guid('afe719cf-5dd1-44f2-999c-7a399f1cfccc')
    return ISpeechGrammarRule
def _define_ISpeechGrammarRule():
    ISpeechGrammarRule = win32more.Media.Speech.ISpeechGrammarRule_head
    ISpeechGrammarRule.get_Attributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SpeechRuleAttributes), use_last_error=False)(7, 'get_Attributes', ((1, 'Attributes'),)))
    ISpeechGrammarRule.get_InitialState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechGrammarRuleState_head), use_last_error=False)(8, 'get_InitialState', ((1, 'State'),)))
    ISpeechGrammarRule.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_Name', ((1, 'Name'),)))
    ISpeechGrammarRule.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_Id', ((1, 'Id'),)))
    ISpeechGrammarRule.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'Clear', ()))
    ISpeechGrammarRule.AddResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(12, 'AddResource', ((1, 'ResourceName'),(1, 'ResourceValue'),)))
    ISpeechGrammarRule.AddState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechGrammarRuleState_head), use_last_error=False)(13, 'AddState', ((1, 'State'),)))
    return ISpeechGrammarRule
def _define_ISpeechGrammarRules_head():
    class ISpeechGrammarRules(win32more.System.Com.IDispatch_head):
        Guid = Guid('6ffa3b44-fc2d-40d1-8afc-32911c7f1ad1')
    return ISpeechGrammarRules
def _define_ISpeechGrammarRules():
    ISpeechGrammarRules = win32more.Media.Speech.ISpeechGrammarRules_head
    ISpeechGrammarRules.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'Count'),)))
    ISpeechGrammarRules.FindRule = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Media.Speech.ISpeechGrammarRule_head), use_last_error=False)(8, 'FindRule', ((1, 'RuleNameOrId'),(1, 'Rule'),)))
    ISpeechGrammarRules.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Media.Speech.ISpeechGrammarRule_head), use_last_error=False)(9, 'Item', ((1, 'Index'),(1, 'Rule'),)))
    ISpeechGrammarRules.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(10, 'get__NewEnum', ((1, 'EnumVARIANT'),)))
    ISpeechGrammarRules.get_Dynamic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(11, 'get_Dynamic', ((1, 'Dynamic'),)))
    ISpeechGrammarRules.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Media.Speech.SpeechRuleAttributes,Int32,POINTER(win32more.Media.Speech.ISpeechGrammarRule_head), use_last_error=False)(12, 'Add', ((1, 'RuleName'),(1, 'Attributes'),(1, 'RuleId'),(1, 'Rule'),)))
    ISpeechGrammarRules.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(13, 'Commit', ()))
    ISpeechGrammarRules.CommitAndSave = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(14, 'CommitAndSave', ((1, 'ErrorText'),(1, 'SaveStream'),)))
    return ISpeechGrammarRules
def _define_ISpeechGrammarRuleState_head():
    class ISpeechGrammarRuleState(win32more.System.Com.IDispatch_head):
        Guid = Guid('d4286f2c-ee67-45ae-b928-28d695362eda')
    return ISpeechGrammarRuleState
def _define_ISpeechGrammarRuleState():
    ISpeechGrammarRuleState = win32more.Media.Speech.ISpeechGrammarRuleState_head
    ISpeechGrammarRuleState.get_Rule = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechGrammarRule_head), use_last_error=False)(7, 'get_Rule', ((1, 'Rule'),)))
    ISpeechGrammarRuleState.get_Transitions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechGrammarRuleStateTransitions_head), use_last_error=False)(8, 'get_Transitions', ((1, 'Transitions'),)))
    ISpeechGrammarRuleState.AddWordTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpeechGrammarRuleState_head,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Media.Speech.SpeechGrammarWordType,win32more.Foundation.BSTR,Int32,POINTER(win32more.System.Com.VARIANT_head),Single, use_last_error=False)(9, 'AddWordTransition', ((1, 'DestState'),(1, 'Words'),(1, 'Separators'),(1, 'Type'),(1, 'PropertyName'),(1, 'PropertyId'),(1, 'PropertyValue'),(1, 'Weight'),)))
    ISpeechGrammarRuleState.AddRuleTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpeechGrammarRuleState_head,win32more.Media.Speech.ISpeechGrammarRule_head,win32more.Foundation.BSTR,Int32,POINTER(win32more.System.Com.VARIANT_head),Single, use_last_error=False)(10, 'AddRuleTransition', ((1, 'DestinationState'),(1, 'Rule'),(1, 'PropertyName'),(1, 'PropertyId'),(1, 'PropertyValue'),(1, 'Weight'),)))
    ISpeechGrammarRuleState.AddSpecialTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpeechGrammarRuleState_head,win32more.Media.Speech.SpeechSpecialTransitionType,win32more.Foundation.BSTR,Int32,POINTER(win32more.System.Com.VARIANT_head),Single, use_last_error=False)(11, 'AddSpecialTransition', ((1, 'DestinationState'),(1, 'Type'),(1, 'PropertyName'),(1, 'PropertyId'),(1, 'PropertyValue'),(1, 'Weight'),)))
    return ISpeechGrammarRuleState
def _define_ISpeechGrammarRuleStateTransition_head():
    class ISpeechGrammarRuleStateTransition(win32more.System.Com.IDispatch_head):
        Guid = Guid('cafd1db1-41d1-4a06-9863-e2e81da17a9a')
    return ISpeechGrammarRuleStateTransition
def _define_ISpeechGrammarRuleStateTransition():
    ISpeechGrammarRuleStateTransition = win32more.Media.Speech.ISpeechGrammarRuleStateTransition_head
    ISpeechGrammarRuleStateTransition.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SpeechGrammarRuleStateTransitionType), use_last_error=False)(7, 'get_Type', ((1, 'Type'),)))
    ISpeechGrammarRuleStateTransition.get_Text = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_Text', ((1, 'Text'),)))
    ISpeechGrammarRuleStateTransition.get_Rule = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechGrammarRule_head), use_last_error=False)(9, 'get_Rule', ((1, 'Rule'),)))
    ISpeechGrammarRuleStateTransition.get_Weight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(10, 'get_Weight', ((1, 'Weight'),)))
    ISpeechGrammarRuleStateTransition.get_PropertyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_PropertyName', ((1, 'PropertyName'),)))
    ISpeechGrammarRuleStateTransition.get_PropertyId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(12, 'get_PropertyId', ((1, 'PropertyId'),)))
    ISpeechGrammarRuleStateTransition.get_PropertyValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(13, 'get_PropertyValue', ((1, 'PropertyValue'),)))
    ISpeechGrammarRuleStateTransition.get_NextState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechGrammarRuleState_head), use_last_error=False)(14, 'get_NextState', ((1, 'NextState'),)))
    return ISpeechGrammarRuleStateTransition
def _define_ISpeechGrammarRuleStateTransitions_head():
    class ISpeechGrammarRuleStateTransitions(win32more.System.Com.IDispatch_head):
        Guid = Guid('eabce657-75bc-44a2-aa7f-c56476742963')
    return ISpeechGrammarRuleStateTransitions
def _define_ISpeechGrammarRuleStateTransitions():
    ISpeechGrammarRuleStateTransitions = win32more.Media.Speech.ISpeechGrammarRuleStateTransitions_head
    ISpeechGrammarRuleStateTransitions.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'Count'),)))
    ISpeechGrammarRuleStateTransitions.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Media.Speech.ISpeechGrammarRuleStateTransition_head), use_last_error=False)(8, 'Item', ((1, 'Index'),(1, 'Transition'),)))
    ISpeechGrammarRuleStateTransitions.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'EnumVARIANT'),)))
    return ISpeechGrammarRuleStateTransitions
def _define_ISpeechTextSelectionInformation_head():
    class ISpeechTextSelectionInformation(win32more.System.Com.IDispatch_head):
        Guid = Guid('3b9c7e7a-6eee-4ded-9092-11657279adbe')
    return ISpeechTextSelectionInformation
def _define_ISpeechTextSelectionInformation():
    ISpeechTextSelectionInformation = win32more.Media.Speech.ISpeechTextSelectionInformation_head
    ISpeechTextSelectionInformation.put_ActiveOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(7, 'put_ActiveOffset', ((1, 'ActiveOffset'),)))
    ISpeechTextSelectionInformation.get_ActiveOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_ActiveOffset', ((1, 'ActiveOffset'),)))
    ISpeechTextSelectionInformation.put_ActiveLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(9, 'put_ActiveLength', ((1, 'ActiveLength'),)))
    ISpeechTextSelectionInformation.get_ActiveLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_ActiveLength', ((1, 'ActiveLength'),)))
    ISpeechTextSelectionInformation.put_SelectionOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'put_SelectionOffset', ((1, 'SelectionOffset'),)))
    ISpeechTextSelectionInformation.get_SelectionOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(12, 'get_SelectionOffset', ((1, 'SelectionOffset'),)))
    ISpeechTextSelectionInformation.put_SelectionLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(13, 'put_SelectionLength', ((1, 'SelectionLength'),)))
    ISpeechTextSelectionInformation.get_SelectionLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(14, 'get_SelectionLength', ((1, 'SelectionLength'),)))
    return ISpeechTextSelectionInformation
def _define_ISpeechRecoResult_head():
    class ISpeechRecoResult(win32more.System.Com.IDispatch_head):
        Guid = Guid('ed2879cf-ced9-4ee6-a534-de0191d5468d')
    return ISpeechRecoResult
def _define_ISpeechRecoResult():
    ISpeechRecoResult = win32more.Media.Speech.ISpeechRecoResult_head
    ISpeechRecoResult.get_RecoContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechRecoContext_head), use_last_error=False)(7, 'get_RecoContext', ((1, 'RecoContext'),)))
    ISpeechRecoResult.get_Times = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechRecoResultTimes_head), use_last_error=False)(8, 'get_Times', ((1, 'Times'),)))
    ISpeechRecoResult.putref_AudioFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpeechAudioFormat_head, use_last_error=False)(9, 'putref_AudioFormat', ((1, 'Format'),)))
    ISpeechRecoResult.get_AudioFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechAudioFormat_head), use_last_error=False)(10, 'get_AudioFormat', ((1, 'Format'),)))
    ISpeechRecoResult.get_PhraseInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechPhraseInfo_head), use_last_error=False)(11, 'get_PhraseInfo', ((1, 'PhraseInfo'),)))
    ISpeechRecoResult.Alternates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Int32,POINTER(win32more.Media.Speech.ISpeechPhraseAlternates_head), use_last_error=False)(12, 'Alternates', ((1, 'RequestCount'),(1, 'StartElement'),(1, 'Elements'),(1, 'Alternates'),)))
    ISpeechRecoResult.Audio = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.Media.Speech.ISpeechMemoryStream_head), use_last_error=False)(13, 'Audio', ((1, 'StartElement'),(1, 'Elements'),(1, 'Stream'),)))
    ISpeechRecoResult.SpeakAudio = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,win32more.Media.Speech.SpeechVoiceSpeakFlags,POINTER(Int32), use_last_error=False)(14, 'SpeakAudio', ((1, 'StartElement'),(1, 'Elements'),(1, 'Flags'),(1, 'StreamNumber'),)))
    ISpeechRecoResult.SaveToMemory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(15, 'SaveToMemory', ((1, 'ResultBlock'),)))
    ISpeechRecoResult.DiscardResultInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SpeechDiscardType, use_last_error=False)(16, 'DiscardResultInfo', ((1, 'ValueTypes'),)))
    return ISpeechRecoResult
def _define_ISpeechRecoResult2_head():
    class ISpeechRecoResult2(win32more.Media.Speech.ISpeechRecoResult_head):
        Guid = Guid('8e0a246d-d3c8-45de-8657-04290c458c3c')
    return ISpeechRecoResult2
def _define_ISpeechRecoResult2():
    ISpeechRecoResult2 = win32more.Media.Speech.ISpeechRecoResult2_head
    ISpeechRecoResult2.SetTextFeedback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int16, use_last_error=False)(17, 'SetTextFeedback', ((1, 'Feedback'),(1, 'WasSuccessful'),)))
    return ISpeechRecoResult2
def _define_ISpeechRecoResultTimes_head():
    class ISpeechRecoResultTimes(win32more.System.Com.IDispatch_head):
        Guid = Guid('62b3b8fb-f6e7-41be-bdcb-056b1c29efc0')
    return ISpeechRecoResultTimes
def _define_ISpeechRecoResultTimes():
    ISpeechRecoResultTimes = win32more.Media.Speech.ISpeechRecoResultTimes_head
    ISpeechRecoResultTimes.get_StreamTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_StreamTime', ((1, 'Time'),)))
    ISpeechRecoResultTimes.get_Length = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'get_Length', ((1, 'Length'),)))
    ISpeechRecoResultTimes.get_TickCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_TickCount', ((1, 'TickCount'),)))
    ISpeechRecoResultTimes.get_OffsetFromStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(10, 'get_OffsetFromStart', ((1, 'OffsetFromStart'),)))
    return ISpeechRecoResultTimes
def _define_ISpeechPhraseAlternate_head():
    class ISpeechPhraseAlternate(win32more.System.Com.IDispatch_head):
        Guid = Guid('27864a2a-2b9f-4cb8-92d3-0d2722fd1e73')
    return ISpeechPhraseAlternate
def _define_ISpeechPhraseAlternate():
    ISpeechPhraseAlternate = win32more.Media.Speech.ISpeechPhraseAlternate_head
    ISpeechPhraseAlternate.get_RecoResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechRecoResult_head), use_last_error=False)(7, 'get_RecoResult', ((1, 'RecoResult'),)))
    ISpeechPhraseAlternate.get_StartElementInResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_StartElementInResult', ((1, 'StartElement'),)))
    ISpeechPhraseAlternate.get_NumberOfElementsInResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_NumberOfElementsInResult', ((1, 'NumberOfElements'),)))
    ISpeechPhraseAlternate.get_PhraseInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechPhraseInfo_head), use_last_error=False)(10, 'get_PhraseInfo', ((1, 'PhraseInfo'),)))
    ISpeechPhraseAlternate.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'Commit', ()))
    return ISpeechPhraseAlternate
def _define_ISpeechPhraseAlternates_head():
    class ISpeechPhraseAlternates(win32more.System.Com.IDispatch_head):
        Guid = Guid('b238b6d5-f276-4c3d-a6c1-2974801c3cc2')
    return ISpeechPhraseAlternates
def _define_ISpeechPhraseAlternates():
    ISpeechPhraseAlternates = win32more.Media.Speech.ISpeechPhraseAlternates_head
    ISpeechPhraseAlternates.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'Count'),)))
    ISpeechPhraseAlternates.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Media.Speech.ISpeechPhraseAlternate_head), use_last_error=False)(8, 'Item', ((1, 'Index'),(1, 'PhraseAlternate'),)))
    ISpeechPhraseAlternates.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'EnumVARIANT'),)))
    return ISpeechPhraseAlternates
def _define_ISpeechPhraseInfo_head():
    class ISpeechPhraseInfo(win32more.System.Com.IDispatch_head):
        Guid = Guid('961559cf-4e67-4662-8bf0-d93f1fcd61b3')
    return ISpeechPhraseInfo
def _define_ISpeechPhraseInfo():
    ISpeechPhraseInfo = win32more.Media.Speech.ISpeechPhraseInfo_head
    ISpeechPhraseInfo.get_LanguageId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_LanguageId', ((1, 'LanguageId'),)))
    ISpeechPhraseInfo.get_GrammarId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'get_GrammarId', ((1, 'GrammarId'),)))
    ISpeechPhraseInfo.get_StartTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(9, 'get_StartTime', ((1, 'StartTime'),)))
    ISpeechPhraseInfo.get_AudioStreamPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(10, 'get_AudioStreamPosition', ((1, 'AudioStreamPosition'),)))
    ISpeechPhraseInfo.get_AudioSizeBytes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'get_AudioSizeBytes', ((1, 'pAudioSizeBytes'),)))
    ISpeechPhraseInfo.get_RetainedSizeBytes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(12, 'get_RetainedSizeBytes', ((1, 'RetainedSizeBytes'),)))
    ISpeechPhraseInfo.get_AudioSizeTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'get_AudioSizeTime', ((1, 'AudioSizeTime'),)))
    ISpeechPhraseInfo.get_Rule = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechPhraseRule_head), use_last_error=False)(14, 'get_Rule', ((1, 'Rule'),)))
    ISpeechPhraseInfo.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechPhraseProperties_head), use_last_error=False)(15, 'get_Properties', ((1, 'Properties'),)))
    ISpeechPhraseInfo.get_Elements = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechPhraseElements_head), use_last_error=False)(16, 'get_Elements', ((1, 'Elements'),)))
    ISpeechPhraseInfo.get_Replacements = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechPhraseReplacements_head), use_last_error=False)(17, 'get_Replacements', ((1, 'Replacements'),)))
    ISpeechPhraseInfo.get_EngineId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(18, 'get_EngineId', ((1, 'EngineIdGuid'),)))
    ISpeechPhraseInfo.get_EnginePrivateData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(19, 'get_EnginePrivateData', ((1, 'PrivateData'),)))
    ISpeechPhraseInfo.SaveToMemory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(20, 'SaveToMemory', ((1, 'PhraseBlock'),)))
    ISpeechPhraseInfo.GetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Int16,POINTER(win32more.Foundation.BSTR), use_last_error=False)(21, 'GetText', ((1, 'StartElement'),(1, 'Elements'),(1, 'UseReplacements'),(1, 'Text'),)))
    ISpeechPhraseInfo.GetDisplayAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Int16,POINTER(win32more.Media.Speech.SpeechDisplayAttributes), use_last_error=False)(22, 'GetDisplayAttributes', ((1, 'StartElement'),(1, 'Elements'),(1, 'UseReplacements'),(1, 'DisplayAttributes'),)))
    return ISpeechPhraseInfo
def _define_ISpeechPhraseElement_head():
    class ISpeechPhraseElement(win32more.System.Com.IDispatch_head):
        Guid = Guid('e6176f96-e373-4801-b223-3b62c068c0b4')
    return ISpeechPhraseElement
def _define_ISpeechPhraseElement():
    ISpeechPhraseElement = win32more.Media.Speech.ISpeechPhraseElement_head
    ISpeechPhraseElement.get_AudioTimeOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_AudioTimeOffset', ((1, 'AudioTimeOffset'),)))
    ISpeechPhraseElement.get_AudioSizeTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_AudioSizeTime', ((1, 'AudioSizeTime'),)))
    ISpeechPhraseElement.get_AudioStreamOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_AudioStreamOffset', ((1, 'AudioStreamOffset'),)))
    ISpeechPhraseElement.get_AudioSizeBytes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_AudioSizeBytes', ((1, 'AudioSizeBytes'),)))
    ISpeechPhraseElement.get_RetainedStreamOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'get_RetainedStreamOffset', ((1, 'RetainedStreamOffset'),)))
    ISpeechPhraseElement.get_RetainedSizeBytes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(12, 'get_RetainedSizeBytes', ((1, 'RetainedSizeBytes'),)))
    ISpeechPhraseElement.get_DisplayText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_DisplayText', ((1, 'DisplayText'),)))
    ISpeechPhraseElement.get_LexicalForm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_LexicalForm', ((1, 'LexicalForm'),)))
    ISpeechPhraseElement.get_Pronunciation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(15, 'get_Pronunciation', ((1, 'Pronunciation'),)))
    ISpeechPhraseElement.get_DisplayAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SpeechDisplayAttributes), use_last_error=False)(16, 'get_DisplayAttributes', ((1, 'DisplayAttributes'),)))
    ISpeechPhraseElement.get_RequiredConfidence = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SpeechEngineConfidence), use_last_error=False)(17, 'get_RequiredConfidence', ((1, 'RequiredConfidence'),)))
    ISpeechPhraseElement.get_ActualConfidence = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SpeechEngineConfidence), use_last_error=False)(18, 'get_ActualConfidence', ((1, 'ActualConfidence'),)))
    ISpeechPhraseElement.get_EngineConfidence = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(19, 'get_EngineConfidence', ((1, 'EngineConfidence'),)))
    return ISpeechPhraseElement
def _define_ISpeechPhraseElements_head():
    class ISpeechPhraseElements(win32more.System.Com.IDispatch_head):
        Guid = Guid('0626b328-3478-467d-a0b3-d0853b93dda3')
    return ISpeechPhraseElements
def _define_ISpeechPhraseElements():
    ISpeechPhraseElements = win32more.Media.Speech.ISpeechPhraseElements_head
    ISpeechPhraseElements.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'Count'),)))
    ISpeechPhraseElements.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Media.Speech.ISpeechPhraseElement_head), use_last_error=False)(8, 'Item', ((1, 'Index'),(1, 'Element'),)))
    ISpeechPhraseElements.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'EnumVARIANT'),)))
    return ISpeechPhraseElements
def _define_ISpeechPhraseReplacement_head():
    class ISpeechPhraseReplacement(win32more.System.Com.IDispatch_head):
        Guid = Guid('2890a410-53a7-4fb5-94ec-06d4998e3d02')
    return ISpeechPhraseReplacement
def _define_ISpeechPhraseReplacement():
    ISpeechPhraseReplacement = win32more.Media.Speech.ISpeechPhraseReplacement_head
    ISpeechPhraseReplacement.get_DisplayAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SpeechDisplayAttributes), use_last_error=False)(7, 'get_DisplayAttributes', ((1, 'DisplayAttributes'),)))
    ISpeechPhraseReplacement.get_Text = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_Text', ((1, 'Text'),)))
    ISpeechPhraseReplacement.get_FirstElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_FirstElement', ((1, 'FirstElement'),)))
    ISpeechPhraseReplacement.get_NumberOfElements = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_NumberOfElements', ((1, 'NumberOfElements'),)))
    return ISpeechPhraseReplacement
def _define_ISpeechPhraseReplacements_head():
    class ISpeechPhraseReplacements(win32more.System.Com.IDispatch_head):
        Guid = Guid('38bc662f-2257-4525-959e-2069d2596c05')
    return ISpeechPhraseReplacements
def _define_ISpeechPhraseReplacements():
    ISpeechPhraseReplacements = win32more.Media.Speech.ISpeechPhraseReplacements_head
    ISpeechPhraseReplacements.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'Count'),)))
    ISpeechPhraseReplacements.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Media.Speech.ISpeechPhraseReplacement_head), use_last_error=False)(8, 'Item', ((1, 'Index'),(1, 'Reps'),)))
    ISpeechPhraseReplacements.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'EnumVARIANT'),)))
    return ISpeechPhraseReplacements
def _define_ISpeechPhraseProperty_head():
    class ISpeechPhraseProperty(win32more.System.Com.IDispatch_head):
        Guid = Guid('ce563d48-961e-4732-a2e1-378a42b430be')
    return ISpeechPhraseProperty
def _define_ISpeechPhraseProperty():
    ISpeechPhraseProperty = win32more.Media.Speech.ISpeechPhraseProperty_head
    ISpeechPhraseProperty.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Name', ((1, 'Name'),)))
    ISpeechPhraseProperty.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Id', ((1, 'Id'),)))
    ISpeechPhraseProperty.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(9, 'get_Value', ((1, 'Value'),)))
    ISpeechPhraseProperty.get_FirstElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_FirstElement', ((1, 'FirstElement'),)))
    ISpeechPhraseProperty.get_NumberOfElements = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'get_NumberOfElements', ((1, 'NumberOfElements'),)))
    ISpeechPhraseProperty.get_EngineConfidence = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(12, 'get_EngineConfidence', ((1, 'Confidence'),)))
    ISpeechPhraseProperty.get_Confidence = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SpeechEngineConfidence), use_last_error=False)(13, 'get_Confidence', ((1, 'Confidence'),)))
    ISpeechPhraseProperty.get_Parent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechPhraseProperty_head), use_last_error=False)(14, 'get_Parent', ((1, 'ParentProperty'),)))
    ISpeechPhraseProperty.get_Children = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechPhraseProperties_head), use_last_error=False)(15, 'get_Children', ((1, 'Children'),)))
    return ISpeechPhraseProperty
def _define_ISpeechPhraseProperties_head():
    class ISpeechPhraseProperties(win32more.System.Com.IDispatch_head):
        Guid = Guid('08166b47-102e-4b23-a599-bdb98dbfd1f4')
    return ISpeechPhraseProperties
def _define_ISpeechPhraseProperties():
    ISpeechPhraseProperties = win32more.Media.Speech.ISpeechPhraseProperties_head
    ISpeechPhraseProperties.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'Count'),)))
    ISpeechPhraseProperties.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Media.Speech.ISpeechPhraseProperty_head), use_last_error=False)(8, 'Item', ((1, 'Index'),(1, 'Property'),)))
    ISpeechPhraseProperties.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'EnumVARIANT'),)))
    return ISpeechPhraseProperties
def _define_ISpeechPhraseRule_head():
    class ISpeechPhraseRule(win32more.System.Com.IDispatch_head):
        Guid = Guid('a7bfe112-a4a0-48d9-b602-c313843f6964')
    return ISpeechPhraseRule
def _define_ISpeechPhraseRule():
    ISpeechPhraseRule = win32more.Media.Speech.ISpeechPhraseRule_head
    ISpeechPhraseRule.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Name', ((1, 'Name'),)))
    ISpeechPhraseRule.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Id', ((1, 'Id'),)))
    ISpeechPhraseRule.get_FirstElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_FirstElement', ((1, 'FirstElement'),)))
    ISpeechPhraseRule.get_NumberOfElements = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_NumberOfElements', ((1, 'NumberOfElements'),)))
    ISpeechPhraseRule.get_Parent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechPhraseRule_head), use_last_error=False)(11, 'get_Parent', ((1, 'Parent'),)))
    ISpeechPhraseRule.get_Children = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechPhraseRules_head), use_last_error=False)(12, 'get_Children', ((1, 'Children'),)))
    ISpeechPhraseRule.get_Confidence = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SpeechEngineConfidence), use_last_error=False)(13, 'get_Confidence', ((1, 'ActualConfidence'),)))
    ISpeechPhraseRule.get_EngineConfidence = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(14, 'get_EngineConfidence', ((1, 'EngineConfidence'),)))
    return ISpeechPhraseRule
def _define_ISpeechPhraseRules_head():
    class ISpeechPhraseRules(win32more.System.Com.IDispatch_head):
        Guid = Guid('9047d593-01dd-4b72-81a3-e4a0ca69f407')
    return ISpeechPhraseRules
def _define_ISpeechPhraseRules():
    ISpeechPhraseRules = win32more.Media.Speech.ISpeechPhraseRules_head
    ISpeechPhraseRules.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'Count'),)))
    ISpeechPhraseRules.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Media.Speech.ISpeechPhraseRule_head), use_last_error=False)(8, 'Item', ((1, 'Index'),(1, 'Rule'),)))
    ISpeechPhraseRules.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'EnumVARIANT'),)))
    return ISpeechPhraseRules
def _define_ISpeechLexicon_head():
    class ISpeechLexicon(win32more.System.Com.IDispatch_head):
        Guid = Guid('3da7627a-c7ae-4b23-8708-638c50362c25')
    return ISpeechLexicon
def _define_ISpeechLexicon():
    ISpeechLexicon = win32more.Media.Speech.ISpeechLexicon_head
    ISpeechLexicon.get_GenerationId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_GenerationId', ((1, 'GenerationId'),)))
    ISpeechLexicon.GetWords = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SpeechLexiconType,POINTER(Int32),POINTER(win32more.Media.Speech.ISpeechLexiconWords_head), use_last_error=False)(8, 'GetWords', ((1, 'Flags'),(1, 'GenerationID'),(1, 'Words'),)))
    ISpeechLexicon.AddPronunciation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.Media.Speech.SpeechPartOfSpeech,win32more.Foundation.BSTR, use_last_error=False)(9, 'AddPronunciation', ((1, 'bstrWord'),(1, 'LangId'),(1, 'PartOfSpeech'),(1, 'bstrPronunciation'),)))
    ISpeechLexicon.AddPronunciationByPhoneIds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.Media.Speech.SpeechPartOfSpeech,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(10, 'AddPronunciationByPhoneIds', ((1, 'bstrWord'),(1, 'LangId'),(1, 'PartOfSpeech'),(1, 'PhoneIds'),)))
    ISpeechLexicon.RemovePronunciation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.Media.Speech.SpeechPartOfSpeech,win32more.Foundation.BSTR, use_last_error=False)(11, 'RemovePronunciation', ((1, 'bstrWord'),(1, 'LangId'),(1, 'PartOfSpeech'),(1, 'bstrPronunciation'),)))
    ISpeechLexicon.RemovePronunciationByPhoneIds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.Media.Speech.SpeechPartOfSpeech,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(12, 'RemovePronunciationByPhoneIds', ((1, 'bstrWord'),(1, 'LangId'),(1, 'PartOfSpeech'),(1, 'PhoneIds'),)))
    ISpeechLexicon.GetPronunciations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.Media.Speech.SpeechLexiconType,POINTER(win32more.Media.Speech.ISpeechLexiconPronunciations_head), use_last_error=False)(13, 'GetPronunciations', ((1, 'bstrWord'),(1, 'LangId'),(1, 'TypeFlags'),(1, 'ppPronunciations'),)))
    ISpeechLexicon.GetGenerationChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(win32more.Media.Speech.ISpeechLexiconWords_head), use_last_error=False)(14, 'GetGenerationChange', ((1, 'GenerationID'),(1, 'ppWords'),)))
    return ISpeechLexicon
def _define_ISpeechLexiconWords_head():
    class ISpeechLexiconWords(win32more.System.Com.IDispatch_head):
        Guid = Guid('8d199862-415e-47d5-ac4f-faa608b424e6')
    return ISpeechLexiconWords
def _define_ISpeechLexiconWords():
    ISpeechLexiconWords = win32more.Media.Speech.ISpeechLexiconWords_head
    ISpeechLexiconWords.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'Count'),)))
    ISpeechLexiconWords.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Media.Speech.ISpeechLexiconWord_head), use_last_error=False)(8, 'Item', ((1, 'Index'),(1, 'Word'),)))
    ISpeechLexiconWords.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'EnumVARIANT'),)))
    return ISpeechLexiconWords
def _define_ISpeechLexiconWord_head():
    class ISpeechLexiconWord(win32more.System.Com.IDispatch_head):
        Guid = Guid('4e5b933c-c9be-48ed-8842-1ee51bb1d4ff')
    return ISpeechLexiconWord
def _define_ISpeechLexiconWord():
    ISpeechLexiconWord = win32more.Media.Speech.ISpeechLexiconWord_head
    ISpeechLexiconWord.get_LangId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_LangId', ((1, 'LangId'),)))
    ISpeechLexiconWord.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SpeechWordType), use_last_error=False)(8, 'get_Type', ((1, 'WordType'),)))
    ISpeechLexiconWord.get_Word = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_Word', ((1, 'Word'),)))
    ISpeechLexiconWord.get_Pronunciations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechLexiconPronunciations_head), use_last_error=False)(10, 'get_Pronunciations', ((1, 'Pronunciations'),)))
    return ISpeechLexiconWord
def _define_ISpeechLexiconPronunciations_head():
    class ISpeechLexiconPronunciations(win32more.System.Com.IDispatch_head):
        Guid = Guid('72829128-5682-4704-a0d4-3e2bb6f2ead3')
    return ISpeechLexiconPronunciations
def _define_ISpeechLexiconPronunciations():
    ISpeechLexiconPronunciations = win32more.Media.Speech.ISpeechLexiconPronunciations_head
    ISpeechLexiconPronunciations.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'Count'),)))
    ISpeechLexiconPronunciations.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Media.Speech.ISpeechLexiconPronunciation_head), use_last_error=False)(8, 'Item', ((1, 'Index'),(1, 'Pronunciation'),)))
    ISpeechLexiconPronunciations.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'EnumVARIANT'),)))
    return ISpeechLexiconPronunciations
def _define_ISpeechLexiconPronunciation_head():
    class ISpeechLexiconPronunciation(win32more.System.Com.IDispatch_head):
        Guid = Guid('95252c5d-9e43-4f4a-9899-48ee73352f9f')
    return ISpeechLexiconPronunciation
def _define_ISpeechLexiconPronunciation():
    ISpeechLexiconPronunciation = win32more.Media.Speech.ISpeechLexiconPronunciation_head
    ISpeechLexiconPronunciation.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SpeechLexiconType), use_last_error=False)(7, 'get_Type', ((1, 'LexiconType'),)))
    ISpeechLexiconPronunciation.get_LangId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_LangId', ((1, 'LangId'),)))
    ISpeechLexiconPronunciation.get_PartOfSpeech = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.SpeechPartOfSpeech), use_last_error=False)(9, 'get_PartOfSpeech', ((1, 'PartOfSpeech'),)))
    ISpeechLexiconPronunciation.get_PhoneIds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(10, 'get_PhoneIds', ((1, 'PhoneIds'),)))
    ISpeechLexiconPronunciation.get_Symbolic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_Symbolic', ((1, 'Symbolic'),)))
    return ISpeechLexiconPronunciation
def _define_ISpeechXMLRecoResult_head():
    class ISpeechXMLRecoResult(win32more.Media.Speech.ISpeechRecoResult_head):
        Guid = Guid('aaec54af-8f85-4924-944d-b79d39d72e19')
    return ISpeechXMLRecoResult
def _define_ISpeechXMLRecoResult():
    ISpeechXMLRecoResult = win32more.Media.Speech.ISpeechXMLRecoResult_head
    ISpeechXMLRecoResult.GetXMLResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SPXMLRESULTOPTIONS,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'GetXMLResult', ((1, 'Options'),(1, 'pResult'),)))
    ISpeechXMLRecoResult.GetXMLErrorInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR),POINTER(Int32),POINTER(Int16), use_last_error=False)(18, 'GetXMLErrorInfo', ((1, 'LineNumber'),(1, 'ScriptLine'),(1, 'Source'),(1, 'Description'),(1, 'ResultCode'),(1, 'IsError'),)))
    return ISpeechXMLRecoResult
def _define_ISpeechRecoResultDispatch_head():
    class ISpeechRecoResultDispatch(win32more.System.Com.IDispatch_head):
        Guid = Guid('6d60eb64-aced-40a6-bbf3-4e557f71dee2')
    return ISpeechRecoResultDispatch
def _define_ISpeechRecoResultDispatch():
    ISpeechRecoResultDispatch = win32more.Media.Speech.ISpeechRecoResultDispatch_head
    ISpeechRecoResultDispatch.get_RecoContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechRecoContext_head), use_last_error=False)(7, 'get_RecoContext', ((1, 'RecoContext'),)))
    ISpeechRecoResultDispatch.get_Times = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechRecoResultTimes_head), use_last_error=False)(8, 'get_Times', ((1, 'Times'),)))
    ISpeechRecoResultDispatch.putref_AudioFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.ISpeechAudioFormat_head, use_last_error=False)(9, 'putref_AudioFormat', ((1, 'Format'),)))
    ISpeechRecoResultDispatch.get_AudioFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechAudioFormat_head), use_last_error=False)(10, 'get_AudioFormat', ((1, 'Format'),)))
    ISpeechRecoResultDispatch.get_PhraseInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.Speech.ISpeechPhraseInfo_head), use_last_error=False)(11, 'get_PhraseInfo', ((1, 'PhraseInfo'),)))
    ISpeechRecoResultDispatch.Alternates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Int32,POINTER(win32more.Media.Speech.ISpeechPhraseAlternates_head), use_last_error=False)(12, 'Alternates', ((1, 'RequestCount'),(1, 'StartElement'),(1, 'Elements'),(1, 'Alternates'),)))
    ISpeechRecoResultDispatch.Audio = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.Media.Speech.ISpeechMemoryStream_head), use_last_error=False)(13, 'Audio', ((1, 'StartElement'),(1, 'Elements'),(1, 'Stream'),)))
    ISpeechRecoResultDispatch.SpeakAudio = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,win32more.Media.Speech.SpeechVoiceSpeakFlags,POINTER(Int32), use_last_error=False)(14, 'SpeakAudio', ((1, 'StartElement'),(1, 'Elements'),(1, 'Flags'),(1, 'StreamNumber'),)))
    ISpeechRecoResultDispatch.SaveToMemory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(15, 'SaveToMemory', ((1, 'ResultBlock'),)))
    ISpeechRecoResultDispatch.DiscardResultInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SpeechDiscardType, use_last_error=False)(16, 'DiscardResultInfo', ((1, 'ValueTypes'),)))
    ISpeechRecoResultDispatch.GetXMLResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.Speech.SPXMLRESULTOPTIONS,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'GetXMLResult', ((1, 'Options'),(1, 'pResult'),)))
    ISpeechRecoResultDispatch.GetXMLErrorInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.HRESULT),POINTER(Int16), use_last_error=False)(18, 'GetXMLErrorInfo', ((1, 'LineNumber'),(1, 'ScriptLine'),(1, 'Source'),(1, 'Description'),(1, 'ResultCode'),(1, 'IsError'),)))
    ISpeechRecoResultDispatch.SetTextFeedback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int16, use_last_error=False)(19, 'SetTextFeedback', ((1, 'Feedback'),(1, 'WasSuccessful'),)))
    return ISpeechRecoResultDispatch
def _define_ISpeechPhraseInfoBuilder_head():
    class ISpeechPhraseInfoBuilder(win32more.System.Com.IDispatch_head):
        Guid = Guid('3b151836-df3a-4e0a-846c-d2adc9334333')
    return ISpeechPhraseInfoBuilder
def _define_ISpeechPhraseInfoBuilder():
    ISpeechPhraseInfoBuilder = win32more.Media.Speech.ISpeechPhraseInfoBuilder_head
    ISpeechPhraseInfoBuilder.RestorePhraseFromMemory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.Media.Speech.ISpeechPhraseInfo_head), use_last_error=False)(7, 'RestorePhraseFromMemory', ((1, 'PhraseInMemory'),(1, 'PhraseInfo'),)))
    return ISpeechPhraseInfoBuilder
def _define_ISpeechPhoneConverter_head():
    class ISpeechPhoneConverter(win32more.System.Com.IDispatch_head):
        Guid = Guid('c3e4f353-433f-43d6-89a1-6a62a7054c3d')
    return ISpeechPhoneConverter
def _define_ISpeechPhoneConverter():
    ISpeechPhoneConverter = win32more.Media.Speech.ISpeechPhoneConverter_head
    ISpeechPhoneConverter.get_LanguageId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_LanguageId', ((1, 'LanguageId'),)))
    ISpeechPhoneConverter.put_LanguageId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(8, 'put_LanguageId', ((1, 'LanguageId'),)))
    ISpeechPhoneConverter.PhoneToId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(9, 'PhoneToId', ((1, 'Phonemes'),(1, 'IdArray'),)))
    ISpeechPhoneConverter.IdToPhone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'IdToPhone', ((1, 'IdArray'),(1, 'Phonemes'),)))
    return ISpeechPhoneConverter
__all__ = [
    "SP_LOW_CONFIDENCE",
    "SP_NORMAL_CONFIDENCE",
    "DEFAULT_WEIGHT",
    "SP_MAX_WORD_LENGTH",
    "SP_MAX_PRON_LENGTH",
    "SP_EMULATE_RESULT",
    "SP_STREAMPOS_ASAP",
    "SP_STREAMPOS_REALTIME",
    "SPRP_NORMAL",
    "SP_MAX_LANGIDS",
    "SAPI_ERROR_BASE",
    "Speech_Default_Weight",
    "Speech_Max_Word_Length",
    "Speech_Max_Pron_Length",
    "Speech_StreamPos_Asap",
    "Speech_StreamPos_RealTime",
    "SpeechAllElements",
    "SpNotifyTranslator",
    "SpObjectTokenCategory",
    "SpObjectToken",
    "SpResourceManager",
    "SpStreamFormatConverter",
    "SpMMAudioEnum",
    "SpMMAudioIn",
    "SpMMAudioOut",
    "SpStream",
    "SpVoice",
    "SpSharedRecoContext",
    "SpInprocRecognizer",
    "SpSharedRecognizer",
    "SpLexicon",
    "SpUnCompressedLexicon",
    "SpCompressedLexicon",
    "SpShortcut",
    "SpPhoneConverter",
    "SpPhoneticAlphabetConverter",
    "SpNullPhoneConverter",
    "SpTextSelectionInformation",
    "SpPhraseInfoBuilder",
    "SpAudioFormat",
    "SpWaveFormatEx",
    "SpInProcRecoContext",
    "SpCustomStream",
    "SpFileStream",
    "SpMemoryStream",
    "SPDATAKEYLOCATION",
    "SPDKL_DefaultLocation",
    "SPDKL_CurrentUser",
    "SPDKL_LocalMachine",
    "SPDKL_CurrentConfig",
    "SPSTREAMFORMAT",
    "SPSF_Default",
    "SPSF_NoAssignedFormat",
    "SPSF_Text",
    "SPSF_NonStandardFormat",
    "SPSF_ExtendedAudioFormat",
    "SPSF_8kHz8BitMono",
    "SPSF_8kHz8BitStereo",
    "SPSF_8kHz16BitMono",
    "SPSF_8kHz16BitStereo",
    "SPSF_11kHz8BitMono",
    "SPSF_11kHz8BitStereo",
    "SPSF_11kHz16BitMono",
    "SPSF_11kHz16BitStereo",
    "SPSF_12kHz8BitMono",
    "SPSF_12kHz8BitStereo",
    "SPSF_12kHz16BitMono",
    "SPSF_12kHz16BitStereo",
    "SPSF_16kHz8BitMono",
    "SPSF_16kHz8BitStereo",
    "SPSF_16kHz16BitMono",
    "SPSF_16kHz16BitStereo",
    "SPSF_22kHz8BitMono",
    "SPSF_22kHz8BitStereo",
    "SPSF_22kHz16BitMono",
    "SPSF_22kHz16BitStereo",
    "SPSF_24kHz8BitMono",
    "SPSF_24kHz8BitStereo",
    "SPSF_24kHz16BitMono",
    "SPSF_24kHz16BitStereo",
    "SPSF_32kHz8BitMono",
    "SPSF_32kHz8BitStereo",
    "SPSF_32kHz16BitMono",
    "SPSF_32kHz16BitStereo",
    "SPSF_44kHz8BitMono",
    "SPSF_44kHz8BitStereo",
    "SPSF_44kHz16BitMono",
    "SPSF_44kHz16BitStereo",
    "SPSF_48kHz8BitMono",
    "SPSF_48kHz8BitStereo",
    "SPSF_48kHz16BitMono",
    "SPSF_48kHz16BitStereo",
    "SPSF_TrueSpeech_8kHz1BitMono",
    "SPSF_CCITT_ALaw_8kHzMono",
    "SPSF_CCITT_ALaw_8kHzStereo",
    "SPSF_CCITT_ALaw_11kHzMono",
    "SPSF_CCITT_ALaw_11kHzStereo",
    "SPSF_CCITT_ALaw_22kHzMono",
    "SPSF_CCITT_ALaw_22kHzStereo",
    "SPSF_CCITT_ALaw_44kHzMono",
    "SPSF_CCITT_ALaw_44kHzStereo",
    "SPSF_CCITT_uLaw_8kHzMono",
    "SPSF_CCITT_uLaw_8kHzStereo",
    "SPSF_CCITT_uLaw_11kHzMono",
    "SPSF_CCITT_uLaw_11kHzStereo",
    "SPSF_CCITT_uLaw_22kHzMono",
    "SPSF_CCITT_uLaw_22kHzStereo",
    "SPSF_CCITT_uLaw_44kHzMono",
    "SPSF_CCITT_uLaw_44kHzStereo",
    "SPSF_ADPCM_8kHzMono",
    "SPSF_ADPCM_8kHzStereo",
    "SPSF_ADPCM_11kHzMono",
    "SPSF_ADPCM_11kHzStereo",
    "SPSF_ADPCM_22kHzMono",
    "SPSF_ADPCM_22kHzStereo",
    "SPSF_ADPCM_44kHzMono",
    "SPSF_ADPCM_44kHzStereo",
    "SPSF_GSM610_8kHzMono",
    "SPSF_GSM610_11kHzMono",
    "SPSF_GSM610_22kHzMono",
    "SPSF_GSM610_44kHzMono",
    "SPSF_NUM_FORMATS",
    "ISpNotifyCallback",
    "SPNOTIFYCALLBACK",
    "ISpNotifySource",
    "ISpNotifySink",
    "ISpNotifyTranslator",
    "ISpDataKey",
    "ISpRegDataKey",
    "ISpObjectTokenCategory",
    "ISpObjectToken",
    "ISpObjectTokenInit",
    "IEnumSpObjectTokens",
    "ISpObjectWithToken",
    "ISpResourceManager",
    "SPEVENTLPARAMTYPE",
    "SPET_LPARAM_IS_UNDEFINED",
    "SPET_LPARAM_IS_TOKEN",
    "SPET_LPARAM_IS_OBJECT",
    "SPET_LPARAM_IS_POINTER",
    "SPET_LPARAM_IS_STRING",
    "SPEVENTENUM",
    "SPEI_UNDEFINED",
    "SPEI_START_INPUT_STREAM",
    "SPEI_END_INPUT_STREAM",
    "SPEI_VOICE_CHANGE",
    "SPEI_TTS_BOOKMARK",
    "SPEI_WORD_BOUNDARY",
    "SPEI_PHONEME",
    "SPEI_SENTENCE_BOUNDARY",
    "SPEI_VISEME",
    "SPEI_TTS_AUDIO_LEVEL",
    "SPEI_TTS_PRIVATE",
    "SPEI_MIN_TTS",
    "SPEI_MAX_TTS",
    "SPEI_END_SR_STREAM",
    "SPEI_SOUND_START",
    "SPEI_SOUND_END",
    "SPEI_PHRASE_START",
    "SPEI_RECOGNITION",
    "SPEI_HYPOTHESIS",
    "SPEI_SR_BOOKMARK",
    "SPEI_PROPERTY_NUM_CHANGE",
    "SPEI_PROPERTY_STRING_CHANGE",
    "SPEI_FALSE_RECOGNITION",
    "SPEI_INTERFERENCE",
    "SPEI_REQUEST_UI",
    "SPEI_RECO_STATE_CHANGE",
    "SPEI_ADAPTATION",
    "SPEI_START_SR_STREAM",
    "SPEI_RECO_OTHER_CONTEXT",
    "SPEI_SR_AUDIO_LEVEL",
    "SPEI_SR_RETAINEDAUDIO",
    "SPEI_SR_PRIVATE",
    "SPEI_RESERVED4",
    "SPEI_RESERVED5",
    "SPEI_RESERVED6",
    "SPEI_MIN_SR",
    "SPEI_MAX_SR",
    "SPEI_RESERVED1",
    "SPEI_RESERVED2",
    "SPEI_RESERVED3",
    "SPEVENT",
    "SPSERIALIZEDEVENT",
    "SPSERIALIZEDEVENT64",
    "SPEVENTEX",
    "SPINTERFERENCE",
    "SPINTERFERENCE_NONE",
    "SPINTERFERENCE_NOISE",
    "SPINTERFERENCE_NOSIGNAL",
    "SPINTERFERENCE_TOOLOUD",
    "SPINTERFERENCE_TOOQUIET",
    "SPINTERFERENCE_TOOFAST",
    "SPINTERFERENCE_TOOSLOW",
    "SPINTERFERENCE_LATENCY_WARNING",
    "SPINTERFERENCE_LATENCY_TRUNCATE_BEGIN",
    "SPINTERFERENCE_LATENCY_TRUNCATE_END",
    "SPENDSRSTREAMFLAGS",
    "SPESF_NONE",
    "SPESF_STREAM_RELEASED",
    "SPESF_EMULATED",
    "SPVFEATURE",
    "SPVFEATURE_STRESSED",
    "SPVFEATURE_EMPHASIS",
    "SPVISEMES",
    "SP_VISEME_0",
    "SP_VISEME_1",
    "SP_VISEME_2",
    "SP_VISEME_3",
    "SP_VISEME_4",
    "SP_VISEME_5",
    "SP_VISEME_6",
    "SP_VISEME_7",
    "SP_VISEME_8",
    "SP_VISEME_9",
    "SP_VISEME_10",
    "SP_VISEME_11",
    "SP_VISEME_12",
    "SP_VISEME_13",
    "SP_VISEME_14",
    "SP_VISEME_15",
    "SP_VISEME_16",
    "SP_VISEME_17",
    "SP_VISEME_18",
    "SP_VISEME_19",
    "SP_VISEME_20",
    "SP_VISEME_21",
    "SPEVENTSOURCEINFO",
    "ISpEventSource",
    "ISpEventSource2",
    "ISpEventSink",
    "ISpStreamFormat",
    "SPFILEMODE",
    "SPFM_OPEN_READONLY",
    "SPFM_OPEN_READWRITE",
    "SPFM_CREATE",
    "SPFM_CREATE_ALWAYS",
    "SPFM_NUM_MODES",
    "ISpStream",
    "ISpStreamFormatConverter",
    "SPAUDIOSTATE",
    "SPAS_CLOSED",
    "SPAS_STOP",
    "SPAS_PAUSE",
    "SPAS_RUN",
    "SPAUDIOSTATUS",
    "SPAUDIOBUFFERINFO",
    "ISpAudio",
    "ISpMMSysAudio",
    "ISpTranscript",
    "SPDISPLYATTRIBUTES",
    "SPAF_ONE_TRAILING_SPACE",
    "SPAF_TWO_TRAILING_SPACES",
    "SPAF_CONSUME_LEADING_SPACES",
    "SPAF_BUFFER_POSITION",
    "SPAF_ALL",
    "SPAF_USER_SPECIFIED",
    "SPPHRASEELEMENT",
    "SPPHRASERULE",
    "SPPHRASEPROPERTYUNIONTYPE",
    "SPPPUT_UNUSED",
    "SPPPUT_ARRAY_INDEX",
    "SPPHRASEPROPERTY",
    "SPPHRASEREPLACEMENT",
    "SPSEMANTICERRORINFO",
    "SPSEMANTICFORMAT",
    "SPSMF_SAPI_PROPERTIES",
    "SPSMF_SRGS_SEMANTICINTERPRETATION_MS",
    "SPSMF_SRGS_SAPIPROPERTIES",
    "SPSMF_UPS",
    "SPSMF_SRGS_SEMANTICINTERPRETATION_W3C",
    "SPPHRASE_50",
    "SPPHRASE",
    "SPSERIALIZEDPHRASE",
    "SPRULE",
    "SPVALUETYPE",
    "SPDF_PROPERTY",
    "SPDF_REPLACEMENT",
    "SPDF_RULE",
    "SPDF_DISPLAYTEXT",
    "SPDF_LEXICALFORM",
    "SPDF_PRONUNCIATION",
    "SPDF_AUDIO",
    "SPDF_ALTERNATES",
    "SPDF_ALL",
    "SPBINARYGRAMMAR",
    "SPPHRASERNG",
    "SPPR_ALL_ELEMENTS",
    "SPSTATEHANDLE__",
    "SPRECOEVENTFLAGS",
    "SPREF_AutoPause",
    "SPREF_Emulated",
    "SPREF_SMLTimeout",
    "SPREF_ExtendableParse",
    "SPREF_ReSent",
    "SPREF_Hypothesis",
    "SPREF_FalseRecognition",
    "SPPARTOFSPEECH",
    "SPPS_NotOverriden",
    "SPPS_Unknown",
    "SPPS_Noun",
    "SPPS_Verb",
    "SPPS_Modifier",
    "SPPS_Function",
    "SPPS_Interjection",
    "SPPS_Noncontent",
    "SPPS_LMA",
    "SPPS_SuppressWord",
    "SPLEXICONTYPE",
    "eLEXTYPE_USER",
    "eLEXTYPE_APP",
    "eLEXTYPE_VENDORLEXICON",
    "eLEXTYPE_LETTERTOSOUND",
    "eLEXTYPE_MORPHOLOGY",
    "eLEXTYPE_RESERVED4",
    "eLEXTYPE_USER_SHORTCUT",
    "eLEXTYPE_RESERVED6",
    "eLEXTYPE_RESERVED7",
    "eLEXTYPE_RESERVED8",
    "eLEXTYPE_RESERVED9",
    "eLEXTYPE_RESERVED10",
    "eLEXTYPE_PRIVATE1",
    "eLEXTYPE_PRIVATE2",
    "eLEXTYPE_PRIVATE3",
    "eLEXTYPE_PRIVATE4",
    "eLEXTYPE_PRIVATE5",
    "eLEXTYPE_PRIVATE6",
    "eLEXTYPE_PRIVATE7",
    "eLEXTYPE_PRIVATE8",
    "eLEXTYPE_PRIVATE9",
    "eLEXTYPE_PRIVATE10",
    "eLEXTYPE_PRIVATE11",
    "eLEXTYPE_PRIVATE12",
    "eLEXTYPE_PRIVATE13",
    "eLEXTYPE_PRIVATE14",
    "eLEXTYPE_PRIVATE15",
    "eLEXTYPE_PRIVATE16",
    "eLEXTYPE_PRIVATE17",
    "eLEXTYPE_PRIVATE18",
    "eLEXTYPE_PRIVATE19",
    "eLEXTYPE_PRIVATE20",
    "SPWORDTYPE",
    "eWORDTYPE_ADDED",
    "eWORDTYPE_DELETED",
    "SPPRONUNCIATIONFLAGS",
    "ePRONFLAG_USED",
    "SPWORDPRONUNCIATION",
    "SPWORDPRONUNCIATIONLIST",
    "SPWORD",
    "SPWORDLIST",
    "ISpLexicon",
    "ISpContainerLexicon",
    "SPSHORTCUTTYPE",
    "SPSHT_NotOverriden",
    "SPSHT_Unknown",
    "SPSHT_EMAIL",
    "SPSHT_OTHER",
    "SPPS_RESERVED1",
    "SPPS_RESERVED2",
    "SPPS_RESERVED3",
    "SPPS_RESERVED4",
    "SPSHORTCUTPAIR",
    "SPSHORTCUTPAIRLIST",
    "ISpShortcut",
    "ISpPhoneConverter",
    "ISpPhoneticAlphabetConverter",
    "ISpPhoneticAlphabetSelection",
    "SPVPITCH",
    "SPVACTIONS",
    "SPVA_Speak",
    "SPVA_Silence",
    "SPVA_Pronounce",
    "SPVA_Bookmark",
    "SPVA_SpellOut",
    "SPVA_Section",
    "SPVA_ParseUnknownTag",
    "SPVCONTEXT",
    "SPVSTATE",
    "SPRUNSTATE",
    "SPRS_DONE",
    "SPRS_IS_SPEAKING",
    "SPVLIMITS",
    "SPMIN_VOLUME",
    "SPMAX_VOLUME",
    "SPMIN_RATE",
    "SPMAX_RATE",
    "SPVPRIORITY",
    "SPVPRI_NORMAL",
    "SPVPRI_ALERT",
    "SPVPRI_OVER",
    "SPVOICESTATUS",
    "SPEAKFLAGS",
    "SPF_DEFAULT",
    "SPF_ASYNC",
    "SPF_PURGEBEFORESPEAK",
    "SPF_IS_FILENAME",
    "SPF_IS_XML",
    "SPF_IS_NOT_XML",
    "SPF_PERSIST_XML",
    "SPF_NLP_SPEAK_PUNC",
    "SPF_PARSE_SAPI",
    "SPF_PARSE_SSML",
    "SPF_PARSE_AUTODETECT",
    "SPF_NLP_MASK",
    "SPF_PARSE_MASK",
    "SPF_VOICE_MASK",
    "SPF_UNUSED_FLAGS",
    "ISpVoice",
    "ISpPhrase",
    "ISpPhraseAlt",
    "SPXMLRESULTOPTIONS",
    "SPXRO_SML",
    "SPXRO_Alternates_SML",
    "ISpPhrase2",
    "SPRECORESULTTIMES",
    "SPSERIALIZEDRESULT",
    "ISpRecoResult",
    "SPCOMMITFLAGS",
    "SPCF_NONE",
    "SPCF_ADD_TO_USER_LEXICON",
    "SPCF_DEFINITE_CORRECTION",
    "ISpRecoResult2",
    "ISpXMLRecoResult",
    "SPTEXTSELECTIONINFO",
    "SPWORDPRONOUNCEABLE",
    "SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE",
    "SPWP_UNKNOWN_WORD_PRONOUNCEABLE",
    "SPWP_KNOWN_WORD_PRONOUNCEABLE",
    "SPGRAMMARSTATE",
    "SPGS_DISABLED",
    "SPGS_ENABLED",
    "SPGS_EXCLUSIVE",
    "SPCONTEXTSTATE",
    "SPCS_DISABLED",
    "SPCS_ENABLED",
    "SPRULESTATE",
    "SPRS_INACTIVE",
    "SPRS_ACTIVE",
    "SPRS_ACTIVE_WITH_AUTO_PAUSE",
    "SPRS_ACTIVE_USER_DELIMITED",
    "SPGRAMMARWORDTYPE",
    "SPWT_DISPLAY",
    "SPWT_LEXICAL",
    "SPWT_PRONUNCIATION",
    "SPWT_LEXICAL_NO_SPECIAL_CHARS",
    "SPPROPERTYINFO",
    "SPCFGRULEATTRIBUTES",
    "SPRAF_TopLevel",
    "SPRAF_Active",
    "SPRAF_Export",
    "SPRAF_Import",
    "SPRAF_Interpreter",
    "SPRAF_Dynamic",
    "SPRAF_Root",
    "SPRAF_AutoPause",
    "SPRAF_UserDelimited",
    "ISpGrammarBuilder",
    "SPLOADOPTIONS",
    "SPLO_STATIC",
    "SPLO_DYNAMIC",
    "ISpRecoGrammar",
    "SPMATCHINGMODE",
    "SPMATCHINGMODE_AllWords",
    "SPMATCHINGMODE_Subsequence",
    "SPMATCHINGMODE_OrderedSubset",
    "SPMATCHINGMODE_SubsequenceContentRequired",
    "SPMATCHINGMODE_OrderedSubsetContentRequired",
    "PHONETICALPHABET",
    "PA_Ipa",
    "PA_Ups",
    "PA_Sapi",
    "ISpGrammarBuilder2",
    "ISpRecoGrammar2",
    "ISpeechResourceLoader",
    "SPRECOCONTEXTSTATUS",
    "SPBOOKMARKOPTIONS",
    "SPBO_NONE",
    "SPBO_PAUSE",
    "SPBO_AHEAD",
    "SPBO_TIME_UNITS",
    "SPAUDIOOPTIONS",
    "SPAO_NONE",
    "SPAO_RETAIN_AUDIO",
    "ISpRecoContext",
    "SPGRAMMAROPTIONS",
    "SPGO_SAPI",
    "SPGO_SRGS",
    "SPGO_UPS",
    "SPGO_SRGS_MS_SCRIPT",
    "SPGO_SRGS_W3C_SCRIPT",
    "SPGO_SRGS_STG_SCRIPT",
    "SPGO_SRGS_SCRIPT",
    "SPGO_FILE",
    "SPGO_HTTP",
    "SPGO_RES",
    "SPGO_OBJECT",
    "SPGO_DEFAULT",
    "SPGO_ALL",
    "SPADAPTATIONSETTINGS",
    "SPADS_Default",
    "SPADS_CurrentRecognizer",
    "SPADS_RecoProfile",
    "SPADS_Immediate",
    "SPADS_Reset",
    "SPADS_HighVolumeDataSource",
    "SPADAPTATIONRELEVANCE",
    "SPAR_Unknown",
    "SPAR_Low",
    "SPAR_Medium",
    "SPAR_High",
    "ISpRecoContext2",
    "ISpProperties",
    "SPRECOGNIZERSTATUS",
    "SPWAVEFORMATTYPE",
    "SPWF_INPUT",
    "SPWF_SRENGINE",
    "SPRECOSTATE",
    "SPRST_INACTIVE",
    "SPRST_ACTIVE",
    "SPRST_ACTIVE_ALWAYS",
    "SPRST_INACTIVE_WITH_PURGE",
    "SPRST_NUM_STATES",
    "ISpRecognizer",
    "ISpSerializeState",
    "ISpRecognizer2",
    "SPNORMALIZATIONLIST",
    "ISpEnginePronunciation",
    "SPDISPLAYTOKEN",
    "SPDISPLAYPHRASE",
    "ISpDisplayAlternates",
    "DISPID_SpeechDataKey",
    "DISPID_SDKSetBinaryValue",
    "DISPID_SDKGetBinaryValue",
    "DISPID_SDKSetStringValue",
    "DISPID_SDKGetStringValue",
    "DISPID_SDKSetLongValue",
    "DISPID_SDKGetlongValue",
    "DISPID_SDKOpenKey",
    "DISPID_SDKCreateKey",
    "DISPID_SDKDeleteKey",
    "DISPID_SDKDeleteValue",
    "DISPID_SDKEnumKeys",
    "DISPID_SDKEnumValues",
    "DISPID_SpeechObjectToken",
    "DISPID_SOTId",
    "DISPID_SOTDataKey",
    "DISPID_SOTCategory",
    "DISPID_SOTGetDescription",
    "DISPID_SOTSetId",
    "DISPID_SOTGetAttribute",
    "DISPID_SOTCreateInstance",
    "DISPID_SOTRemove",
    "DISPID_SOTGetStorageFileName",
    "DISPID_SOTRemoveStorageFileName",
    "DISPID_SOTIsUISupported",
    "DISPID_SOTDisplayUI",
    "DISPID_SOTMatchesAttributes",
    "SpeechDataKeyLocation",
    "SpeechDataKeyLocation_SDKLDefaultLocation",
    "SpeechDataKeyLocation_SDKLCurrentUser",
    "SpeechDataKeyLocation_SDKLLocalMachine",
    "SpeechDataKeyLocation_SDKLCurrentConfig",
    "SpeechTokenContext",
    "SpeechTokenContext_STCInprocServer",
    "SpeechTokenContext_STCInprocHandler",
    "SpeechTokenContext_STCLocalServer",
    "SpeechTokenContext_STCRemoteServer",
    "SpeechTokenContext_STCAll",
    "SpeechTokenShellFolder",
    "STSF_AppData",
    "STSF_LocalAppData",
    "STSF_CommonAppData",
    "STSF_FlagCreate",
    "DISPID_SpeechObjectTokens",
    "DISPID_SOTsCount",
    "DISPID_SOTsItem",
    "DISPID_SOTs_NewEnum",
    "DISPID_SpeechObjectTokenCategory",
    "DISPID_SOTCId",
    "DISPID_SOTCDefault",
    "DISPID_SOTCSetId",
    "DISPID_SOTCGetDataKey",
    "DISPID_SOTCEnumerateTokens",
    "SpeechAudioFormatType",
    "SpeechAudioFormatType_SAFTDefault",
    "SpeechAudioFormatType_SAFTNoAssignedFormat",
    "SpeechAudioFormatType_SAFTText",
    "SpeechAudioFormatType_SAFTNonStandardFormat",
    "SpeechAudioFormatType_SAFTExtendedAudioFormat",
    "SpeechAudioFormatType_SAFT8kHz8BitMono",
    "SpeechAudioFormatType_SAFT8kHz8BitStereo",
    "SpeechAudioFormatType_SAFT8kHz16BitMono",
    "SpeechAudioFormatType_SAFT8kHz16BitStereo",
    "SpeechAudioFormatType_SAFT11kHz8BitMono",
    "SpeechAudioFormatType_SAFT11kHz8BitStereo",
    "SpeechAudioFormatType_SAFT11kHz16BitMono",
    "SpeechAudioFormatType_SAFT11kHz16BitStereo",
    "SpeechAudioFormatType_SAFT12kHz8BitMono",
    "SpeechAudioFormatType_SAFT12kHz8BitStereo",
    "SpeechAudioFormatType_SAFT12kHz16BitMono",
    "SpeechAudioFormatType_SAFT12kHz16BitStereo",
    "SpeechAudioFormatType_SAFT16kHz8BitMono",
    "SpeechAudioFormatType_SAFT16kHz8BitStereo",
    "SpeechAudioFormatType_SAFT16kHz16BitMono",
    "SpeechAudioFormatType_SAFT16kHz16BitStereo",
    "SpeechAudioFormatType_SAFT22kHz8BitMono",
    "SpeechAudioFormatType_SAFT22kHz8BitStereo",
    "SpeechAudioFormatType_SAFT22kHz16BitMono",
    "SpeechAudioFormatType_SAFT22kHz16BitStereo",
    "SpeechAudioFormatType_SAFT24kHz8BitMono",
    "SpeechAudioFormatType_SAFT24kHz8BitStereo",
    "SpeechAudioFormatType_SAFT24kHz16BitMono",
    "SpeechAudioFormatType_SAFT24kHz16BitStereo",
    "SpeechAudioFormatType_SAFT32kHz8BitMono",
    "SpeechAudioFormatType_SAFT32kHz8BitStereo",
    "SpeechAudioFormatType_SAFT32kHz16BitMono",
    "SpeechAudioFormatType_SAFT32kHz16BitStereo",
    "SpeechAudioFormatType_SAFT44kHz8BitMono",
    "SpeechAudioFormatType_SAFT44kHz8BitStereo",
    "SpeechAudioFormatType_SAFT44kHz16BitMono",
    "SpeechAudioFormatType_SAFT44kHz16BitStereo",
    "SpeechAudioFormatType_SAFT48kHz8BitMono",
    "SpeechAudioFormatType_SAFT48kHz8BitStereo",
    "SpeechAudioFormatType_SAFT48kHz16BitMono",
    "SpeechAudioFormatType_SAFT48kHz16BitStereo",
    "SpeechAudioFormatType_SAFTTrueSpeech_8kHz1BitMono",
    "SpeechAudioFormatType_SAFTCCITT_ALaw_8kHzMono",
    "SpeechAudioFormatType_SAFTCCITT_ALaw_8kHzStereo",
    "SpeechAudioFormatType_SAFTCCITT_ALaw_11kHzMono",
    "SpeechAudioFormatType_SAFTCCITT_ALaw_11kHzStereo",
    "SpeechAudioFormatType_SAFTCCITT_ALaw_22kHzMono",
    "SpeechAudioFormatType_SAFTCCITT_ALaw_22kHzStereo",
    "SpeechAudioFormatType_SAFTCCITT_ALaw_44kHzMono",
    "SpeechAudioFormatType_SAFTCCITT_ALaw_44kHzStereo",
    "SpeechAudioFormatType_SAFTCCITT_uLaw_8kHzMono",
    "SpeechAudioFormatType_SAFTCCITT_uLaw_8kHzStereo",
    "SpeechAudioFormatType_SAFTCCITT_uLaw_11kHzMono",
    "SpeechAudioFormatType_SAFTCCITT_uLaw_11kHzStereo",
    "SpeechAudioFormatType_SAFTCCITT_uLaw_22kHzMono",
    "SpeechAudioFormatType_SAFTCCITT_uLaw_22kHzStereo",
    "SpeechAudioFormatType_SAFTCCITT_uLaw_44kHzMono",
    "SpeechAudioFormatType_SAFTCCITT_uLaw_44kHzStereo",
    "SpeechAudioFormatType_SAFTADPCM_8kHzMono",
    "SpeechAudioFormatType_SAFTADPCM_8kHzStereo",
    "SpeechAudioFormatType_SAFTADPCM_11kHzMono",
    "SpeechAudioFormatType_SAFTADPCM_11kHzStereo",
    "SpeechAudioFormatType_SAFTADPCM_22kHzMono",
    "SpeechAudioFormatType_SAFTADPCM_22kHzStereo",
    "SpeechAudioFormatType_SAFTADPCM_44kHzMono",
    "SpeechAudioFormatType_SAFTADPCM_44kHzStereo",
    "SpeechAudioFormatType_SAFTGSM610_8kHzMono",
    "SpeechAudioFormatType_SAFTGSM610_11kHzMono",
    "SpeechAudioFormatType_SAFTGSM610_22kHzMono",
    "SpeechAudioFormatType_SAFTGSM610_44kHzMono",
    "DISPID_SpeechAudioFormat",
    "DISPID_SAFType",
    "DISPID_SAFGuid",
    "DISPID_SAFGetWaveFormatEx",
    "DISPID_SAFSetWaveFormatEx",
    "DISPID_SpeechBaseStream",
    "DISPID_SBSFormat",
    "DISPID_SBSRead",
    "DISPID_SBSWrite",
    "DISPID_SBSSeek",
    "SpeechStreamSeekPositionType",
    "SpeechStreamSeekPositionType_SSSPTRelativeToStart",
    "SpeechStreamSeekPositionType_SSSPTRelativeToCurrentPosition",
    "SpeechStreamSeekPositionType_SSSPTRelativeToEnd",
    "DISPID_SpeechAudio",
    "DISPID_SAStatus",
    "DISPID_SABufferInfo",
    "DISPID_SADefaultFormat",
    "DISPID_SAVolume",
    "DISPID_SABufferNotifySize",
    "DISPID_SAEventHandle",
    "DISPID_SASetState",
    "SpeechAudioState",
    "SpeechAudioState_SASClosed",
    "SpeechAudioState_SASStop",
    "SpeechAudioState_SASPause",
    "SpeechAudioState_SASRun",
    "DISPID_SpeechMMSysAudio",
    "DISPID_SMSADeviceId",
    "DISPID_SMSALineId",
    "DISPID_SMSAMMHandle",
    "DISPID_SpeechFileStream",
    "DISPID_SFSOpen",
    "DISPID_SFSClose",
    "SpeechStreamFileMode",
    "SpeechStreamFileMode_SSFMOpenForRead",
    "SpeechStreamFileMode_SSFMOpenReadWrite",
    "SpeechStreamFileMode_SSFMCreate",
    "SpeechStreamFileMode_SSFMCreateForWrite",
    "DISPID_SpeechCustomStream",
    "DISPID_SCSBaseStream",
    "DISPID_SpeechMemoryStream",
    "DISPID_SMSSetData",
    "DISPID_SMSGetData",
    "DISPID_SpeechAudioStatus",
    "DISPID_SASFreeBufferSpace",
    "DISPID_SASNonBlockingIO",
    "DISPID_SASState",
    "DISPID_SASCurrentSeekPosition",
    "DISPID_SASCurrentDevicePosition",
    "DISPID_SpeechAudioBufferInfo",
    "DISPID_SABIMinNotification",
    "DISPID_SABIBufferSize",
    "DISPID_SABIEventBias",
    "DISPID_SpeechWaveFormatEx",
    "DISPID_SWFEFormatTag",
    "DISPID_SWFEChannels",
    "DISPID_SWFESamplesPerSec",
    "DISPID_SWFEAvgBytesPerSec",
    "DISPID_SWFEBlockAlign",
    "DISPID_SWFEBitsPerSample",
    "DISPID_SWFEExtraData",
    "DISPID_SpeechVoice",
    "DISPID_SVStatus",
    "DISPID_SVVoice",
    "DISPID_SVAudioOutput",
    "DISPID_SVAudioOutputStream",
    "DISPID_SVRate",
    "DISPID_SVVolume",
    "DISPID_SVAllowAudioOuputFormatChangesOnNextSet",
    "DISPID_SVEventInterests",
    "DISPID_SVPriority",
    "DISPID_SVAlertBoundary",
    "DISPID_SVSyncronousSpeakTimeout",
    "DISPID_SVSpeak",
    "DISPID_SVSpeakStream",
    "DISPID_SVPause",
    "DISPID_SVResume",
    "DISPID_SVSkip",
    "DISPID_SVGetVoices",
    "DISPID_SVGetAudioOutputs",
    "DISPID_SVWaitUntilDone",
    "DISPID_SVSpeakCompleteEvent",
    "DISPID_SVIsUISupported",
    "DISPID_SVDisplayUI",
    "SpeechVoicePriority",
    "SpeechVoicePriority_SVPNormal",
    "SpeechVoicePriority_SVPAlert",
    "SpeechVoicePriority_SVPOver",
    "SpeechVoiceSpeakFlags",
    "SpeechVoiceSpeakFlags_SVSFDefault",
    "SpeechVoiceSpeakFlags_SVSFlagsAsync",
    "SpeechVoiceSpeakFlags_SVSFPurgeBeforeSpeak",
    "SpeechVoiceSpeakFlags_SVSFIsFilename",
    "SpeechVoiceSpeakFlags_SVSFIsXML",
    "SpeechVoiceSpeakFlags_SVSFIsNotXML",
    "SpeechVoiceSpeakFlags_SVSFPersistXML",
    "SpeechVoiceSpeakFlags_SVSFNLPSpeakPunc",
    "SpeechVoiceSpeakFlags_SVSFParseSapi",
    "SpeechVoiceSpeakFlags_SVSFParseSsml",
    "SpeechVoiceSpeakFlags_SVSFParseAutodetect",
    "SpeechVoiceSpeakFlags_SVSFNLPMask",
    "SpeechVoiceSpeakFlags_SVSFParseMask",
    "SpeechVoiceSpeakFlags_SVSFVoiceMask",
    "SpeechVoiceSpeakFlags_SVSFUnusedFlags",
    "SpeechVoiceEvents",
    "SpeechVoiceEvents_SVEStartInputStream",
    "SpeechVoiceEvents_SVEEndInputStream",
    "SpeechVoiceEvents_SVEVoiceChange",
    "SpeechVoiceEvents_SVEBookmark",
    "SpeechVoiceEvents_SVEWordBoundary",
    "SpeechVoiceEvents_SVEPhoneme",
    "SpeechVoiceEvents_SVESentenceBoundary",
    "SpeechVoiceEvents_SVEViseme",
    "SpeechVoiceEvents_SVEAudioLevel",
    "SpeechVoiceEvents_SVEPrivate",
    "SpeechVoiceEvents_SVEAllEvents",
    "DISPID_SpeechVoiceStatus",
    "DISPID_SVSCurrentStreamNumber",
    "DISPID_SVSLastStreamNumberQueued",
    "DISPID_SVSLastResult",
    "DISPID_SVSRunningState",
    "DISPID_SVSInputWordPosition",
    "DISPID_SVSInputWordLength",
    "DISPID_SVSInputSentencePosition",
    "DISPID_SVSInputSentenceLength",
    "DISPID_SVSLastBookmark",
    "DISPID_SVSLastBookmarkId",
    "DISPID_SVSPhonemeId",
    "DISPID_SVSVisemeId",
    "SpeechRunState",
    "SpeechRunState_SRSEDone",
    "SpeechRunState_SRSEIsSpeaking",
    "SpeechVisemeType",
    "SVP_0",
    "SVP_1",
    "SVP_2",
    "SVP_3",
    "SVP_4",
    "SVP_5",
    "SVP_6",
    "SVP_7",
    "SVP_8",
    "SVP_9",
    "SVP_10",
    "SVP_11",
    "SVP_12",
    "SVP_13",
    "SVP_14",
    "SVP_15",
    "SVP_16",
    "SVP_17",
    "SVP_18",
    "SVP_19",
    "SVP_20",
    "SVP_21",
    "SpeechVisemeFeature",
    "SVF_None",
    "SVF_Stressed",
    "SVF_Emphasis",
    "DISPID_SpeechVoiceEvent",
    "DISPID_SVEStreamStart",
    "DISPID_SVEStreamEnd",
    "DISPID_SVEVoiceChange",
    "DISPID_SVEBookmark",
    "DISPID_SVEWord",
    "DISPID_SVEPhoneme",
    "DISPID_SVESentenceBoundary",
    "DISPID_SVEViseme",
    "DISPID_SVEAudioLevel",
    "DISPID_SVEEnginePrivate",
    "DISPID_SpeechRecognizer",
    "DISPID_SRRecognizer",
    "DISPID_SRAllowAudioInputFormatChangesOnNextSet",
    "DISPID_SRAudioInput",
    "DISPID_SRAudioInputStream",
    "DISPID_SRIsShared",
    "DISPID_SRState",
    "DISPID_SRStatus",
    "DISPID_SRProfile",
    "DISPID_SREmulateRecognition",
    "DISPID_SRCreateRecoContext",
    "DISPID_SRGetFormat",
    "DISPID_SRSetPropertyNumber",
    "DISPID_SRGetPropertyNumber",
    "DISPID_SRSetPropertyString",
    "DISPID_SRGetPropertyString",
    "DISPID_SRIsUISupported",
    "DISPID_SRDisplayUI",
    "DISPID_SRGetRecognizers",
    "DISPID_SVGetAudioInputs",
    "DISPID_SVGetProfiles",
    "SpeechRecognizerState",
    "SpeechRecognizerState_SRSInactive",
    "SpeechRecognizerState_SRSActive",
    "SpeechRecognizerState_SRSActiveAlways",
    "SpeechRecognizerState_SRSInactiveWithPurge",
    "SpeechDisplayAttributes",
    "SDA_No_Trailing_Space",
    "SDA_One_Trailing_Space",
    "SDA_Two_Trailing_Spaces",
    "SDA_Consume_Leading_Spaces",
    "SpeechFormatType",
    "SpeechFormatType_SFTInput",
    "SpeechFormatType_SFTSREngine",
    "SpeechEmulationCompareFlags",
    "SpeechEmulationCompareFlags_SECFIgnoreCase",
    "SpeechEmulationCompareFlags_SECFIgnoreKanaType",
    "SpeechEmulationCompareFlags_SECFIgnoreWidth",
    "SpeechEmulationCompareFlags_SECFNoSpecialChars",
    "SpeechEmulationCompareFlags_SECFEmulateResult",
    "SpeechEmulationCompareFlags_SECFDefault",
    "DISPID_SpeechRecognizerStatus",
    "DISPID_SRSAudioStatus",
    "DISPID_SRSCurrentStreamPosition",
    "DISPID_SRSCurrentStreamNumber",
    "DISPID_SRSNumberOfActiveRules",
    "DISPID_SRSClsidEngine",
    "DISPID_SRSSupportedLanguages",
    "DISPID_SpeechRecoContext",
    "DISPID_SRCRecognizer",
    "DISPID_SRCAudioInInterferenceStatus",
    "DISPID_SRCRequestedUIType",
    "DISPID_SRCVoice",
    "DISPID_SRAllowVoiceFormatMatchingOnNextSet",
    "DISPID_SRCVoicePurgeEvent",
    "DISPID_SRCEventInterests",
    "DISPID_SRCCmdMaxAlternates",
    "DISPID_SRCState",
    "DISPID_SRCRetainedAudio",
    "DISPID_SRCRetainedAudioFormat",
    "DISPID_SRCPause",
    "DISPID_SRCResume",
    "DISPID_SRCCreateGrammar",
    "DISPID_SRCCreateResultFromMemory",
    "DISPID_SRCBookmark",
    "DISPID_SRCSetAdaptationData",
    "SpeechRetainedAudioOptions",
    "SpeechRetainedAudioOptions_SRAONone",
    "SpeechRetainedAudioOptions_SRAORetainAudio",
    "SpeechBookmarkOptions",
    "SpeechBookmarkOptions_SBONone",
    "SpeechBookmarkOptions_SBOPause",
    "SpeechInterference",
    "SpeechInterference_SINone",
    "SpeechInterference_SINoise",
    "SpeechInterference_SINoSignal",
    "SpeechInterference_SITooLoud",
    "SpeechInterference_SITooQuiet",
    "SpeechInterference_SITooFast",
    "SpeechInterference_SITooSlow",
    "SpeechRecoEvents",
    "SpeechRecoEvents_SREStreamEnd",
    "SpeechRecoEvents_SRESoundStart",
    "SpeechRecoEvents_SRESoundEnd",
    "SpeechRecoEvents_SREPhraseStart",
    "SpeechRecoEvents_SRERecognition",
    "SpeechRecoEvents_SREHypothesis",
    "SpeechRecoEvents_SREBookmark",
    "SpeechRecoEvents_SREPropertyNumChange",
    "SpeechRecoEvents_SREPropertyStringChange",
    "SpeechRecoEvents_SREFalseRecognition",
    "SpeechRecoEvents_SREInterference",
    "SpeechRecoEvents_SRERequestUI",
    "SpeechRecoEvents_SREStateChange",
    "SpeechRecoEvents_SREAdaptation",
    "SpeechRecoEvents_SREStreamStart",
    "SpeechRecoEvents_SRERecoOtherContext",
    "SpeechRecoEvents_SREAudioLevel",
    "SpeechRecoEvents_SREPrivate",
    "SpeechRecoEvents_SREAllEvents",
    "SpeechRecoContextState",
    "SRCS_Disabled",
    "SRCS_Enabled",
    "DISPIDSPRG",
    "DISPID_SRGId",
    "DISPID_SRGRecoContext",
    "DISPID_SRGState",
    "DISPID_SRGRules",
    "DISPID_SRGReset",
    "DISPID_SRGCommit",
    "DISPID_SRGCmdLoadFromFile",
    "DISPID_SRGCmdLoadFromObject",
    "DISPID_SRGCmdLoadFromResource",
    "DISPID_SRGCmdLoadFromMemory",
    "DISPID_SRGCmdLoadFromProprietaryGrammar",
    "DISPID_SRGCmdSetRuleState",
    "DISPID_SRGCmdSetRuleIdState",
    "DISPID_SRGDictationLoad",
    "DISPID_SRGDictationUnload",
    "DISPID_SRGDictationSetState",
    "DISPID_SRGSetWordSequenceData",
    "DISPID_SRGSetTextSelection",
    "DISPID_SRGIsPronounceable",
    "SpeechLoadOption",
    "SpeechLoadOption_SLOStatic",
    "SpeechLoadOption_SLODynamic",
    "SpeechWordPronounceable",
    "SpeechWordPronounceable_SWPUnknownWordUnpronounceable",
    "SpeechWordPronounceable_SWPUnknownWordPronounceable",
    "SpeechWordPronounceable_SWPKnownWordPronounceable",
    "SpeechGrammarState",
    "SpeechGrammarState_SGSEnabled",
    "SpeechGrammarState_SGSDisabled",
    "SpeechGrammarState_SGSExclusive",
    "SpeechRuleState",
    "SpeechRuleState_SGDSInactive",
    "SpeechRuleState_SGDSActive",
    "SpeechRuleState_SGDSActiveWithAutoPause",
    "SpeechRuleState_SGDSActiveUserDelimited",
    "SpeechRuleAttributes",
    "SpeechRuleAttributes_SRATopLevel",
    "SpeechRuleAttributes_SRADefaultToActive",
    "SpeechRuleAttributes_SRAExport",
    "SpeechRuleAttributes_SRAImport",
    "SpeechRuleAttributes_SRAInterpreter",
    "SpeechRuleAttributes_SRADynamic",
    "SpeechRuleAttributes_SRARoot",
    "SpeechGrammarWordType",
    "SpeechGrammarWordType_SGDisplay",
    "SpeechGrammarWordType_SGLexical",
    "SpeechGrammarWordType_SGPronounciation",
    "SpeechGrammarWordType_SGLexicalNoSpecialChars",
    "DISPID_SpeechRecoContextEvents",
    "DISPID_SRCEStartStream",
    "DISPID_SRCEEndStream",
    "DISPID_SRCEBookmark",
    "DISPID_SRCESoundStart",
    "DISPID_SRCESoundEnd",
    "DISPID_SRCEPhraseStart",
    "DISPID_SRCERecognition",
    "DISPID_SRCEHypothesis",
    "DISPID_SRCEPropertyNumberChange",
    "DISPID_SRCEPropertyStringChange",
    "DISPID_SRCEFalseRecognition",
    "DISPID_SRCEInterference",
    "DISPID_SRCERequestUI",
    "DISPID_SRCERecognizerStateChange",
    "DISPID_SRCEAdaptation",
    "DISPID_SRCERecognitionForOtherContext",
    "DISPID_SRCEAudioLevel",
    "DISPID_SRCEEnginePrivate",
    "SpeechRecognitionType",
    "SpeechRecognitionType_SRTStandard",
    "SpeechRecognitionType_SRTAutopause",
    "SpeechRecognitionType_SRTEmulated",
    "SpeechRecognitionType_SRTSMLTimeout",
    "SpeechRecognitionType_SRTExtendableParse",
    "SpeechRecognitionType_SRTReSent",
    "DISPID_SpeechGrammarRule",
    "DISPID_SGRAttributes",
    "DISPID_SGRInitialState",
    "DISPID_SGRName",
    "DISPID_SGRId",
    "DISPID_SGRClear",
    "DISPID_SGRAddResource",
    "DISPID_SGRAddState",
    "DISPID_SpeechGrammarRules",
    "DISPID_SGRsCount",
    "DISPID_SGRsDynamic",
    "DISPID_SGRsAdd",
    "DISPID_SGRsCommit",
    "DISPID_SGRsCommitAndSave",
    "DISPID_SGRsFindRule",
    "DISPID_SGRsItem",
    "DISPID_SGRs_NewEnum",
    "DISPID_SpeechGrammarRuleState",
    "DISPID_SGRSRule",
    "DISPID_SGRSTransitions",
    "DISPID_SGRSAddWordTransition",
    "DISPID_SGRSAddRuleTransition",
    "DISPID_SGRSAddSpecialTransition",
    "SpeechSpecialTransitionType",
    "SpeechSpecialTransitionType_SSTTWildcard",
    "SpeechSpecialTransitionType_SSTTDictation",
    "SpeechSpecialTransitionType_SSTTTextBuffer",
    "DISPID_SpeechGrammarRuleStateTransitions",
    "DISPID_SGRSTsCount",
    "DISPID_SGRSTsItem",
    "DISPID_SGRSTs_NewEnum",
    "DISPID_SpeechGrammarRuleStateTransition",
    "DISPID_SGRSTType",
    "DISPID_SGRSTText",
    "DISPID_SGRSTRule",
    "DISPID_SGRSTWeight",
    "DISPID_SGRSTPropertyName",
    "DISPID_SGRSTPropertyId",
    "DISPID_SGRSTPropertyValue",
    "DISPID_SGRSTNextState",
    "SpeechGrammarRuleStateTransitionType",
    "SpeechGrammarRuleStateTransitionType_SGRSTTEpsilon",
    "SpeechGrammarRuleStateTransitionType_SGRSTTWord",
    "SpeechGrammarRuleStateTransitionType_SGRSTTRule",
    "SpeechGrammarRuleStateTransitionType_SGRSTTDictation",
    "SpeechGrammarRuleStateTransitionType_SGRSTTWildcard",
    "SpeechGrammarRuleStateTransitionType_SGRSTTTextBuffer",
    "DISPIDSPTSI",
    "DISPIDSPTSI_ActiveOffset",
    "DISPIDSPTSI_ActiveLength",
    "DISPIDSPTSI_SelectionOffset",
    "DISPIDSPTSI_SelectionLength",
    "DISPID_SpeechRecoResult",
    "DISPID_SRRRecoContext",
    "DISPID_SRRTimes",
    "DISPID_SRRAudioFormat",
    "DISPID_SRRPhraseInfo",
    "DISPID_SRRAlternates",
    "DISPID_SRRAudio",
    "DISPID_SRRSpeakAudio",
    "DISPID_SRRSaveToMemory",
    "DISPID_SRRDiscardResultInfo",
    "SpeechDiscardType",
    "SpeechDiscardType_SDTProperty",
    "SpeechDiscardType_SDTReplacement",
    "SpeechDiscardType_SDTRule",
    "SpeechDiscardType_SDTDisplayText",
    "SpeechDiscardType_SDTLexicalForm",
    "SpeechDiscardType_SDTPronunciation",
    "SpeechDiscardType_SDTAudio",
    "SpeechDiscardType_SDTAlternates",
    "SpeechDiscardType_SDTAll",
    "DISPID_SpeechXMLRecoResult",
    "DISPID_SRRGetXMLResult",
    "DISPID_SRRGetXMLErrorInfo",
    "DISPID_SpeechRecoResult2",
    "DISPID_SRRSetTextFeedback",
    "DISPID_SpeechPhraseBuilder",
    "DISPID_SPPBRestorePhraseFromMemory",
    "DISPID_SpeechRecoResultTimes",
    "DISPID_SRRTStreamTime",
    "DISPID_SRRTLength",
    "DISPID_SRRTTickCount",
    "DISPID_SRRTOffsetFromStart",
    "DISPID_SpeechPhraseAlternate",
    "DISPID_SPARecoResult",
    "DISPID_SPAStartElementInResult",
    "DISPID_SPANumberOfElementsInResult",
    "DISPID_SPAPhraseInfo",
    "DISPID_SPACommit",
    "DISPID_SpeechPhraseAlternates",
    "DISPID_SPAsCount",
    "DISPID_SPAsItem",
    "DISPID_SPAs_NewEnum",
    "DISPID_SpeechPhraseInfo",
    "DISPID_SPILanguageId",
    "DISPID_SPIGrammarId",
    "DISPID_SPIStartTime",
    "DISPID_SPIAudioStreamPosition",
    "DISPID_SPIAudioSizeBytes",
    "DISPID_SPIRetainedSizeBytes",
    "DISPID_SPIAudioSizeTime",
    "DISPID_SPIRule",
    "DISPID_SPIProperties",
    "DISPID_SPIElements",
    "DISPID_SPIReplacements",
    "DISPID_SPIEngineId",
    "DISPID_SPIEnginePrivateData",
    "DISPID_SPISaveToMemory",
    "DISPID_SPIGetText",
    "DISPID_SPIGetDisplayAttributes",
    "DISPID_SpeechPhraseElement",
    "DISPID_SPEAudioTimeOffset",
    "DISPID_SPEAudioSizeTime",
    "DISPID_SPEAudioStreamOffset",
    "DISPID_SPEAudioSizeBytes",
    "DISPID_SPERetainedStreamOffset",
    "DISPID_SPERetainedSizeBytes",
    "DISPID_SPEDisplayText",
    "DISPID_SPELexicalForm",
    "DISPID_SPEPronunciation",
    "DISPID_SPEDisplayAttributes",
    "DISPID_SPERequiredConfidence",
    "DISPID_SPEActualConfidence",
    "DISPID_SPEEngineConfidence",
    "SpeechEngineConfidence",
    "SpeechEngineConfidence_SECLowConfidence",
    "SpeechEngineConfidence_SECNormalConfidence",
    "SpeechEngineConfidence_SECHighConfidence",
    "DISPID_SpeechPhraseElements",
    "DISPID_SPEsCount",
    "DISPID_SPEsItem",
    "DISPID_SPEs_NewEnum",
    "DISPID_SpeechPhraseReplacement",
    "DISPID_SPRDisplayAttributes",
    "DISPID_SPRText",
    "DISPID_SPRFirstElement",
    "DISPID_SPRNumberOfElements",
    "DISPID_SpeechPhraseReplacements",
    "DISPID_SPRsCount",
    "DISPID_SPRsItem",
    "DISPID_SPRs_NewEnum",
    "DISPID_SpeechPhraseProperty",
    "DISPID_SPPName",
    "DISPID_SPPId",
    "DISPID_SPPValue",
    "DISPID_SPPFirstElement",
    "DISPID_SPPNumberOfElements",
    "DISPID_SPPEngineConfidence",
    "DISPID_SPPConfidence",
    "DISPID_SPPParent",
    "DISPID_SPPChildren",
    "DISPID_SpeechPhraseProperties",
    "DISPID_SPPsCount",
    "DISPID_SPPsItem",
    "DISPID_SPPs_NewEnum",
    "DISPID_SpeechPhraseRule",
    "DISPID_SPRuleName",
    "DISPID_SPRuleId",
    "DISPID_SPRuleFirstElement",
    "DISPID_SPRuleNumberOfElements",
    "DISPID_SPRuleParent",
    "DISPID_SPRuleChildren",
    "DISPID_SPRuleConfidence",
    "DISPID_SPRuleEngineConfidence",
    "DISPID_SpeechPhraseRules",
    "DISPID_SPRulesCount",
    "DISPID_SPRulesItem",
    "DISPID_SPRules_NewEnum",
    "DISPID_SpeechLexicon",
    "DISPID_SLGenerationId",
    "DISPID_SLGetWords",
    "DISPID_SLAddPronunciation",
    "DISPID_SLAddPronunciationByPhoneIds",
    "DISPID_SLRemovePronunciation",
    "DISPID_SLRemovePronunciationByPhoneIds",
    "DISPID_SLGetPronunciations",
    "DISPID_SLGetGenerationChange",
    "SpeechLexiconType",
    "SpeechLexiconType_SLTUser",
    "SpeechLexiconType_SLTApp",
    "SpeechPartOfSpeech",
    "SpeechPartOfSpeech_SPSNotOverriden",
    "SpeechPartOfSpeech_SPSUnknown",
    "SpeechPartOfSpeech_SPSNoun",
    "SpeechPartOfSpeech_SPSVerb",
    "SpeechPartOfSpeech_SPSModifier",
    "SpeechPartOfSpeech_SPSFunction",
    "SpeechPartOfSpeech_SPSInterjection",
    "SpeechPartOfSpeech_SPSLMA",
    "SpeechPartOfSpeech_SPSSuppressWord",
    "DISPID_SpeechLexiconWords",
    "DISPID_SLWsCount",
    "DISPID_SLWsItem",
    "DISPID_SLWs_NewEnum",
    "SpeechWordType",
    "SpeechWordType_SWTAdded",
    "SpeechWordType_SWTDeleted",
    "DISPID_SpeechLexiconWord",
    "DISPID_SLWLangId",
    "DISPID_SLWType",
    "DISPID_SLWWord",
    "DISPID_SLWPronunciations",
    "DISPID_SpeechLexiconProns",
    "DISPID_SLPsCount",
    "DISPID_SLPsItem",
    "DISPID_SLPs_NewEnum",
    "DISPID_SpeechLexiconPronunciation",
    "DISPID_SLPType",
    "DISPID_SLPLangId",
    "DISPID_SLPPartOfSpeech",
    "DISPID_SLPPhoneIds",
    "DISPID_SLPSymbolic",
    "DISPID_SpeechPhoneConverter",
    "DISPID_SPCLangId",
    "DISPID_SPCPhoneToId",
    "DISPID_SPCIdToPhone",
    "ISpeechDataKey",
    "ISpeechObjectToken",
    "ISpeechObjectTokens",
    "ISpeechObjectTokenCategory",
    "ISpeechAudioBufferInfo",
    "ISpeechAudioStatus",
    "ISpeechAudioFormat",
    "ISpeechWaveFormatEx",
    "ISpeechBaseStream",
    "ISpeechFileStream",
    "ISpeechMemoryStream",
    "ISpeechCustomStream",
    "ISpeechAudio",
    "ISpeechMMSysAudio",
    "ISpeechVoice",
    "ISpeechVoiceStatus",
    "_ISpeechVoiceEvents",
    "ISpeechRecognizer",
    "ISpeechRecognizerStatus",
    "ISpeechRecoContext",
    "ISpeechRecoGrammar",
    "_ISpeechRecoContextEvents",
    "ISpeechGrammarRule",
    "ISpeechGrammarRules",
    "ISpeechGrammarRuleState",
    "ISpeechGrammarRuleStateTransition",
    "ISpeechGrammarRuleStateTransitions",
    "ISpeechTextSelectionInformation",
    "ISpeechRecoResult",
    "ISpeechRecoResult2",
    "ISpeechRecoResultTimes",
    "ISpeechPhraseAlternate",
    "ISpeechPhraseAlternates",
    "ISpeechPhraseInfo",
    "ISpeechPhraseElement",
    "ISpeechPhraseElements",
    "ISpeechPhraseReplacement",
    "ISpeechPhraseReplacements",
    "ISpeechPhraseProperty",
    "ISpeechPhraseProperties",
    "ISpeechPhraseRule",
    "ISpeechPhraseRules",
    "ISpeechLexicon",
    "ISpeechLexiconWords",
    "ISpeechLexiconWord",
    "ISpeechLexiconPronunciations",
    "ISpeechLexiconPronunciation",
    "ISpeechXMLRecoResult",
    "ISpeechRecoResultDispatch",
    "ISpeechPhraseInfoBuilder",
    "ISpeechPhoneConverter",
]
