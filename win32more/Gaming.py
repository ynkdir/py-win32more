from win32more import *
import win32more.Gaming
import win32more.Foundation
import win32more.System.Com
import win32more.System.WinRT

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.Gaming, name, globals()[f"_define_{name}"]())
    return getattr(win32more.Gaming, name)
def __dir__():
    return __all__
GameExplorer = Guid('9a5ea990-3034-4d6f-9128-01f3c61022bc')
GameStatistics = Guid('dbc85a2c-c0dc-4961-b6e2-d28b62c11ad4')
GAME_INSTALL_SCOPE = Int32
GIS_NOT_INSTALLED = 1
GIS_CURRENT_USER = 2
GIS_ALL_USERS = 3
def _define_IGameExplorer_head():
    class IGameExplorer(win32more.System.Com.IUnknown_head):
        Guid = Guid('e7b2fb72-d728-49b3-a5f2-18ebf5f1349e')
    return IGameExplorer
def _define_IGameExplorer():
    IGameExplorer = win32more.Gaming.IGameExplorer_head
    IGameExplorer.AddGame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Gaming.GAME_INSTALL_SCOPE,POINTER(Guid), use_last_error=False)(3, 'AddGame', ((1, 'bstrGDFBinaryPath'),(1, 'bstrGameInstallDirectory'),(1, 'installScope'),(1, 'pguidInstanceID'),)))
    IGameExplorer.RemoveGame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid, use_last_error=False)(4, 'RemoveGame', ((1, 'guidInstanceID'),)))
    IGameExplorer.UpdateGame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid, use_last_error=False)(5, 'UpdateGame', ((1, 'guidInstanceID'),)))
    IGameExplorer.VerifyAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'VerifyAccess', ((1, 'bstrGDFBinaryPath'),(1, 'pfHasAccess'),)))
    return IGameExplorer
GAMESTATS_OPEN_TYPE = Int32
GAMESTATS_OPEN_OPENORCREATE = 0
GAMESTATS_OPEN_OPENONLY = 1
GAMESTATS_OPEN_RESULT = Int32
GAMESTATS_OPEN_CREATED = 0
GAMESTATS_OPEN_OPENED = 1
def _define_IGameStatistics_head():
    class IGameStatistics(win32more.System.Com.IUnknown_head):
        Guid = Guid('3887c9ca-04a0-42ae-bc4c-5fa6c7721145')
    return IGameStatistics
def _define_IGameStatistics():
    IGameStatistics = win32more.Gaming.IGameStatistics_head
    IGameStatistics.GetMaxCategoryLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetMaxCategoryLength', ((1, 'cch'),)))
    IGameStatistics.GetMaxNameLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetMaxNameLength', ((1, 'cch'),)))
    IGameStatistics.GetMaxValueLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetMaxValueLength', ((1, 'cch'),)))
    IGameStatistics.GetMaxCategories = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16), use_last_error=False)(6, 'GetMaxCategories', ((1, 'pMax'),)))
    IGameStatistics.GetMaxStatsPerCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16), use_last_error=False)(7, 'GetMaxStatsPerCategory', ((1, 'pMax'),)))
    IGameStatistics.SetCategoryTitle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,win32more.Foundation.PWSTR, use_last_error=False)(8, 'SetCategoryTitle', ((1, 'categoryIndex'),(1, 'title'),)))
    IGameStatistics.GetCategoryTitle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(9, 'GetCategoryTitle', ((1, 'categoryIndex'),(1, 'pTitle'),)))
    IGameStatistics.GetStatistic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,UInt16,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(10, 'GetStatistic', ((1, 'categoryIndex'),(1, 'statIndex'),(1, 'pName'),(1, 'pValue'),)))
    IGameStatistics.SetStatistic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,UInt16,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(11, 'SetStatistic', ((1, 'categoryIndex'),(1, 'statIndex'),(1, 'name'),(1, 'value'),)))
    IGameStatistics.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(12, 'Save', ((1, 'trackChanges'),)))
    IGameStatistics.SetLastPlayedCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(13, 'SetLastPlayedCategory', ((1, 'categoryIndex'),)))
    IGameStatistics.GetLastPlayedCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(14, 'GetLastPlayedCategory', ((1, 'pCategoryIndex'),)))
    return IGameStatistics
def _define_IGameStatisticsMgr_head():
    class IGameStatisticsMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('aff3ea11-e70e-407d-95dd-35e612c41ce2')
    return IGameStatisticsMgr
def _define_IGameStatisticsMgr():
    IGameStatisticsMgr = win32more.Gaming.IGameStatisticsMgr_head
    IGameStatisticsMgr.GetGameStatistics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Gaming.GAMESTATS_OPEN_TYPE,POINTER(win32more.Gaming.GAMESTATS_OPEN_RESULT),POINTER(win32more.Gaming.IGameStatistics_head), use_last_error=False)(3, 'GetGameStatistics', ((1, 'GDFBinaryPath'),(1, 'openType'),(1, 'pOpenResult'),(1, 'ppiStats'),)))
    IGameStatisticsMgr.RemoveGameStatistics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(4, 'RemoveGameStatistics', ((1, 'GDFBinaryPath'),)))
    return IGameStatisticsMgr
def _define_IGameExplorer2_head():
    class IGameExplorer2(win32more.System.Com.IUnknown_head):
        Guid = Guid('86874aa7-a1ed-450d-a7eb-b89e20b2fff3')
    return IGameExplorer2
def _define_IGameExplorer2():
    IGameExplorer2 = win32more.Gaming.IGameExplorer2_head
    IGameExplorer2.InstallGame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Gaming.GAME_INSTALL_SCOPE, use_last_error=False)(3, 'InstallGame', ((1, 'binaryGDFPath'),(1, 'installDirectory'),(1, 'installScope'),)))
    IGameExplorer2.UninstallGame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(4, 'UninstallGame', ((1, 'binaryGDFPath'),)))
    IGameExplorer2.CheckAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'CheckAccess', ((1, 'binaryGDFPath'),(1, 'pHasAccess'),)))
    return IGameExplorer2
GAMING_DEVICE_VENDOR_ID = Int32
GAMING_DEVICE_VENDOR_ID_NONE = 0
GAMING_DEVICE_VENDOR_ID_MICROSOFT = -1024700366
GAMING_DEVICE_DEVICE_ID = Int32
GAMING_DEVICE_DEVICE_ID_NONE = 0
GAMING_DEVICE_DEVICE_ID_XBOX_ONE = 1988865574
GAMING_DEVICE_DEVICE_ID_XBOX_ONE_S = 712204761
GAMING_DEVICE_DEVICE_ID_XBOX_ONE_X = 1523980231
GAMING_DEVICE_DEVICE_ID_XBOX_ONE_X_DEVKIT = 284675555
def _define_GAMING_DEVICE_MODEL_INFORMATION_head():
    class GAMING_DEVICE_MODEL_INFORMATION(Structure):
        pass
    return GAMING_DEVICE_MODEL_INFORMATION
def _define_GAMING_DEVICE_MODEL_INFORMATION():
    GAMING_DEVICE_MODEL_INFORMATION = win32more.Gaming.GAMING_DEVICE_MODEL_INFORMATION_head
    GAMING_DEVICE_MODEL_INFORMATION._fields_ = [
        ("vendorId", win32more.Gaming.GAMING_DEVICE_VENDOR_ID),
        ("deviceId", win32more.Gaming.GAMING_DEVICE_DEVICE_ID),
    ]
    return GAMING_DEVICE_MODEL_INFORMATION
def _define_GameUICompletionRoutine():
    return CFUNCTYPE(Void,win32more.Foundation.HRESULT,c_void_p, use_last_error=False)
def _define_PlayerPickerUICompletionRoutine():
    return CFUNCTYPE(Void,win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.System.WinRT.HSTRING),UIntPtr, use_last_error=False)
KnownGamingPrivileges = Int32
XPRIVILEGE_BROADCAST = 190
XPRIVILEGE_VIEW_FRIENDS_LIST = 197
XPRIVILEGE_GAME_DVR = 198
XPRIVILEGE_SHARE_KINECT_CONTENT = 199
XPRIVILEGE_MULTIPLAYER_PARTIES = 203
XPRIVILEGE_COMMUNICATION_VOICE_INGAME = 205
XPRIVILEGE_COMMUNICATION_VOICE_SKYPE = 206
XPRIVILEGE_CLOUD_GAMING_MANAGE_SESSION = 207
XPRIVILEGE_CLOUD_GAMING_JOIN_SESSION = 208
XPRIVILEGE_CLOUD_SAVED_GAMES = 209
XPRIVILEGE_SHARE_CONTENT = 211
XPRIVILEGE_PREMIUM_CONTENT = 214
XPRIVILEGE_SUBSCRIPTION_CONTENT = 219
XPRIVILEGE_SOCIAL_NETWORK_SHARING = 220
XPRIVILEGE_PREMIUM_VIDEO = 224
XPRIVILEGE_VIDEO_COMMUNICATIONS = 235
XPRIVILEGE_PURCHASE_CONTENT = 245
XPRIVILEGE_USER_CREATED_CONTENT = 247
XPRIVILEGE_PROFILE_VIEWING = 249
XPRIVILEGE_COMMUNICATIONS = 252
XPRIVILEGE_MULTIPLAYER_SESSIONS = 254
XPRIVILEGE_ADD_FRIEND = 255
XblIdpAuthManager = Guid('ce23534b-56d8-4978-86a2-7ee570640468')
XblIdpAuthTokenResult = Guid('9f493441-744a-410c-ae2b-9a22f7c7731f')
XBL_IDP_AUTH_TOKEN_STATUS = Int32
XBL_IDP_AUTH_TOKEN_STATUS_SUCCESS = 0
XBL_IDP_AUTH_TOKEN_STATUS_OFFLINE_SUCCESS = 1
XBL_IDP_AUTH_TOKEN_STATUS_NO_ACCOUNT_SET = 2
XBL_IDP_AUTH_TOKEN_STATUS_LOAD_MSA_ACCOUNT_FAILED = 3
XBL_IDP_AUTH_TOKEN_STATUS_XBOX_VETO = 4
XBL_IDP_AUTH_TOKEN_STATUS_MSA_INTERRUPT = 5
XBL_IDP_AUTH_TOKEN_STATUS_OFFLINE_NO_CONSENT = 6
XBL_IDP_AUTH_TOKEN_STATUS_VIEW_NOT_SET = 7
XBL_IDP_AUTH_TOKEN_STATUS_UNKNOWN = -1
def _define_IXblIdpAuthManager_head():
    class IXblIdpAuthManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('eb5ddb08-8bbf-449b-ac21-b02ddeb3b136')
    return IXblIdpAuthManager
def _define_IXblIdpAuthManager():
    IXblIdpAuthManager = win32more.Gaming.IXblIdpAuthManager_head
    IXblIdpAuthManager.SetGamerAccount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(3, 'SetGamerAccount', ((1, 'msaAccountId'),(1, 'xuid'),)))
    IXblIdpAuthManager.GetGamerAccount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(4, 'GetGamerAccount', ((1, 'msaAccountId'),(1, 'xuid'),)))
    IXblIdpAuthManager.SetAppViewInitialized = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(5, 'SetAppViewInitialized', ((1, 'appSid'),(1, 'msaAccountId'),)))
    IXblIdpAuthManager.GetEnvironment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(6, 'GetEnvironment', ((1, 'environment'),)))
    IXblIdpAuthManager.GetSandbox = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(7, 'GetSandbox', ((1, 'sandbox'),)))
    IXblIdpAuthManager.GetTokenAndSignatureWithTokenResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(Byte),UInt32,win32more.Foundation.BOOL,POINTER(win32more.Gaming.IXblIdpAuthTokenResult_head), use_last_error=False)(8, 'GetTokenAndSignatureWithTokenResult', ((1, 'msaAccountId'),(1, 'appSid'),(1, 'msaTarget'),(1, 'msaPolicy'),(1, 'httpMethod'),(1, 'uri'),(1, 'headers'),(1, 'body'),(1, 'bodySize'),(1, 'forceRefresh'),(1, 'result'),)))
    return IXblIdpAuthManager
def _define_IXblIdpAuthTokenResult_head():
    class IXblIdpAuthTokenResult(win32more.System.Com.IUnknown_head):
        Guid = Guid('46ce0225-f267-4d68-b299-b2762552dec1')
    return IXblIdpAuthTokenResult
def _define_IXblIdpAuthTokenResult():
    IXblIdpAuthTokenResult = win32more.Gaming.IXblIdpAuthTokenResult_head
    IXblIdpAuthTokenResult.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Gaming.XBL_IDP_AUTH_TOKEN_STATUS), use_last_error=False)(3, 'GetStatus', ((1, 'status'),)))
    IXblIdpAuthTokenResult.GetErrorCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HRESULT), use_last_error=False)(4, 'GetErrorCode', ((1, 'errorCode'),)))
    IXblIdpAuthTokenResult.GetToken = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(5, 'GetToken', ((1, 'token'),)))
    IXblIdpAuthTokenResult.GetSignature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(6, 'GetSignature', ((1, 'signature'),)))
    IXblIdpAuthTokenResult.GetSandbox = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(7, 'GetSandbox', ((1, 'sandbox'),)))
    IXblIdpAuthTokenResult.GetEnvironment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(8, 'GetEnvironment', ((1, 'environment'),)))
    IXblIdpAuthTokenResult.GetMsaAccountId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(9, 'GetMsaAccountId', ((1, 'msaAccountId'),)))
    IXblIdpAuthTokenResult.GetXuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(10, 'GetXuid', ((1, 'xuid'),)))
    IXblIdpAuthTokenResult.GetGamertag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(11, 'GetGamertag', ((1, 'gamertag'),)))
    IXblIdpAuthTokenResult.GetAgeGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(12, 'GetAgeGroup', ((1, 'ageGroup'),)))
    IXblIdpAuthTokenResult.GetPrivileges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(13, 'GetPrivileges', ((1, 'privileges'),)))
    IXblIdpAuthTokenResult.GetMsaTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(14, 'GetMsaTarget', ((1, 'msaTarget'),)))
    IXblIdpAuthTokenResult.GetMsaPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(15, 'GetMsaPolicy', ((1, 'msaPolicy'),)))
    IXblIdpAuthTokenResult.GetMsaAppId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(16, 'GetMsaAppId', ((1, 'msaAppId'),)))
    IXblIdpAuthTokenResult.GetRedirect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(17, 'GetRedirect', ((1, 'redirect'),)))
    IXblIdpAuthTokenResult.GetMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(18, 'GetMessage', ((1, 'message'),)))
    IXblIdpAuthTokenResult.GetHelpId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(19, 'GetHelpId', ((1, 'helpId'),)))
    IXblIdpAuthTokenResult.GetEnforcementBans = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(20, 'GetEnforcementBans', ((1, 'enforcementBans'),)))
    IXblIdpAuthTokenResult.GetRestrictions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(21, 'GetRestrictions', ((1, 'restrictions'),)))
    IXblIdpAuthTokenResult.GetTitleRestrictions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(22, 'GetTitleRestrictions', ((1, 'titleRestrictions'),)))
    return IXblIdpAuthTokenResult
def _define_IXblIdpAuthTokenResult2_head():
    class IXblIdpAuthTokenResult2(win32more.System.Com.IUnknown_head):
        Guid = Guid('75d760b0-60b9-412d-994f-26b2cd5f7812')
    return IXblIdpAuthTokenResult2
def _define_IXblIdpAuthTokenResult2():
    IXblIdpAuthTokenResult2 = win32more.Gaming.IXblIdpAuthTokenResult2_head
    IXblIdpAuthTokenResult2.GetModernGamertag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetModernGamertag', ((1, 'value'),)))
    IXblIdpAuthTokenResult2.GetModernGamertagSuffix = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(4, 'GetModernGamertagSuffix', ((1, 'value'),)))
    IXblIdpAuthTokenResult2.GetUniqueModernGamertag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(5, 'GetUniqueModernGamertag', ((1, 'value'),)))
    return IXblIdpAuthTokenResult2
def _define_HasExpandedResources():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("HasExpandedResources", windll["api-ms-win-gaming-expandedresources-l1-1-0"]), ((1, 'hasExpandedResources'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetExpandedResourceExclusiveCpuCount():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(("GetExpandedResourceExclusiveCpuCount", windll["api-ms-win-gaming-expandedresources-l1-1-0"]), ((1, 'exclusiveCpuCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReleaseExclusiveCpuSets():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(("ReleaseExclusiveCpuSets", windll["api-ms-win-gaming-expandedresources-l1-1-0"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetGamingDeviceModelInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Gaming.GAMING_DEVICE_MODEL_INFORMATION_head), use_last_error=False)(("GetGamingDeviceModelInformation", windll["api-ms-win-gaming-deviceinformation-l1-1-0"]), ((1, 'information'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowGameInviteUI():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.Gaming.GameUICompletionRoutine,c_void_p, use_last_error=False)(("ShowGameInviteUI", windll["api-ms-win-gaming-tcui-l1-1-0"]), ((1, 'serviceConfigurationId'),(1, 'sessionTemplateName'),(1, 'sessionId'),(1, 'invitationDisplayText'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowPlayerPickerUI():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING,POINTER(win32more.System.WinRT.HSTRING),UIntPtr,POINTER(win32more.System.WinRT.HSTRING),UIntPtr,UIntPtr,UIntPtr,win32more.Gaming.PlayerPickerUICompletionRoutine,c_void_p, use_last_error=False)(("ShowPlayerPickerUI", windll["api-ms-win-gaming-tcui-l1-1-0"]), ((1, 'promptDisplayText'),(1, 'xuids'),(1, 'xuidsCount'),(1, 'preSelectedXuids'),(1, 'preSelectedXuidsCount'),(1, 'minSelectionCount'),(1, 'maxSelectionCount'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowProfileCardUI():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING,win32more.Gaming.GameUICompletionRoutine,c_void_p, use_last_error=False)(("ShowProfileCardUI", windll["api-ms-win-gaming-tcui-l1-1-0"]), ((1, 'targetUserXuid'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowChangeFriendRelationshipUI():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING,win32more.Gaming.GameUICompletionRoutine,c_void_p, use_last_error=False)(("ShowChangeFriendRelationshipUI", windll["api-ms-win-gaming-tcui-l1-1-0"]), ((1, 'targetUserXuid'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowTitleAchievementsUI():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Gaming.GameUICompletionRoutine,c_void_p, use_last_error=False)(("ShowTitleAchievementsUI", windll["api-ms-win-gaming-tcui-l1-1-0"]), ((1, 'titleId'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ProcessPendingGameUI():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(("ProcessPendingGameUI", windll["api-ms-win-gaming-tcui-l1-1-0"]), ((1, 'waitForCompletion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TryCancelPendingGameUI():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(("TryCancelPendingGameUI", windll["api-ms-win-gaming-tcui-l1-1-0"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_CheckGamingPrivilegeWithUI():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.Gaming.GameUICompletionRoutine,c_void_p, use_last_error=False)(("CheckGamingPrivilegeWithUI", windll["api-ms-win-gaming-tcui-l1-1-1"]), ((1, 'privilegeId'),(1, 'scope'),(1, 'policy'),(1, 'friendlyMessage'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CheckGamingPrivilegeSilently():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("CheckGamingPrivilegeSilently", windll["api-ms-win-gaming-tcui-l1-1-1"]), ((1, 'privilegeId'),(1, 'scope'),(1, 'policy'),(1, 'hasPrivilege'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowGameInviteUIForUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.Gaming.GameUICompletionRoutine,c_void_p, use_last_error=False)(("ShowGameInviteUIForUser", windll["api-ms-win-gaming-tcui-l1-1-2"]), ((1, 'user'),(1, 'serviceConfigurationId'),(1, 'sessionTemplateName'),(1, 'sessionId'),(1, 'invitationDisplayText'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowPlayerPickerUIForUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,win32more.System.WinRT.HSTRING,POINTER(win32more.System.WinRT.HSTRING),UIntPtr,POINTER(win32more.System.WinRT.HSTRING),UIntPtr,UIntPtr,UIntPtr,win32more.Gaming.PlayerPickerUICompletionRoutine,c_void_p, use_last_error=False)(("ShowPlayerPickerUIForUser", windll["api-ms-win-gaming-tcui-l1-1-2"]), ((1, 'user'),(1, 'promptDisplayText'),(1, 'xuids'),(1, 'xuidsCount'),(1, 'preSelectedXuids'),(1, 'preSelectedXuidsCount'),(1, 'minSelectionCount'),(1, 'maxSelectionCount'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowProfileCardUIForUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,win32more.System.WinRT.HSTRING,win32more.Gaming.GameUICompletionRoutine,c_void_p, use_last_error=False)(("ShowProfileCardUIForUser", windll["api-ms-win-gaming-tcui-l1-1-2"]), ((1, 'user'),(1, 'targetUserXuid'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowChangeFriendRelationshipUIForUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,win32more.System.WinRT.HSTRING,win32more.Gaming.GameUICompletionRoutine,c_void_p, use_last_error=False)(("ShowChangeFriendRelationshipUIForUser", windll["api-ms-win-gaming-tcui-l1-1-2"]), ((1, 'user'),(1, 'targetUserXuid'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowTitleAchievementsUIForUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,UInt32,win32more.Gaming.GameUICompletionRoutine,c_void_p, use_last_error=False)(("ShowTitleAchievementsUIForUser", windll["api-ms-win-gaming-tcui-l1-1-2"]), ((1, 'user'),(1, 'titleId'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CheckGamingPrivilegeWithUIForUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,UInt32,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.Gaming.GameUICompletionRoutine,c_void_p, use_last_error=False)(("CheckGamingPrivilegeWithUIForUser", windll["api-ms-win-gaming-tcui-l1-1-2"]), ((1, 'user'),(1, 'privilegeId'),(1, 'scope'),(1, 'policy'),(1, 'friendlyMessage'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CheckGamingPrivilegeSilentlyForUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,UInt32,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("CheckGamingPrivilegeSilentlyForUser", windll["api-ms-win-gaming-tcui-l1-1-2"]), ((1, 'user'),(1, 'privilegeId'),(1, 'scope'),(1, 'policy'),(1, 'hasPrivilege'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowGameInviteUIWithContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.Gaming.GameUICompletionRoutine,c_void_p, use_last_error=False)(("ShowGameInviteUIWithContext", windll["api-ms-win-gaming-tcui-l1-1-3"]), ((1, 'serviceConfigurationId'),(1, 'sessionTemplateName'),(1, 'sessionId'),(1, 'invitationDisplayText'),(1, 'customActivationContext'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowGameInviteUIWithContextForUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.Gaming.GameUICompletionRoutine,c_void_p, use_last_error=False)(("ShowGameInviteUIWithContextForUser", windll["api-ms-win-gaming-tcui-l1-1-3"]), ((1, 'user'),(1, 'serviceConfigurationId'),(1, 'sessionTemplateName'),(1, 'sessionId'),(1, 'invitationDisplayText'),(1, 'customActivationContext'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowGameInfoUI():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Gaming.GameUICompletionRoutine,c_void_p, use_last_error=False)(("ShowGameInfoUI", windll["api-ms-win-gaming-tcui-l1-1-4"]), ((1, 'titleId'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowGameInfoUIForUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,UInt32,win32more.Gaming.GameUICompletionRoutine,c_void_p, use_last_error=False)(("ShowGameInfoUIForUser", windll["api-ms-win-gaming-tcui-l1-1-4"]), ((1, 'user'),(1, 'titleId'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowFindFriendsUI():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Gaming.GameUICompletionRoutine,c_void_p, use_last_error=False)(("ShowFindFriendsUI", windll["api-ms-win-gaming-tcui-l1-1-4"]), ((1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowFindFriendsUIForUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,win32more.Gaming.GameUICompletionRoutine,c_void_p, use_last_error=False)(("ShowFindFriendsUIForUser", windll["api-ms-win-gaming-tcui-l1-1-4"]), ((1, 'user'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowCustomizeUserProfileUI():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Gaming.GameUICompletionRoutine,c_void_p, use_last_error=False)(("ShowCustomizeUserProfileUI", windll["api-ms-win-gaming-tcui-l1-1-4"]), ((1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowCustomizeUserProfileUIForUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,win32more.Gaming.GameUICompletionRoutine,c_void_p, use_last_error=False)(("ShowCustomizeUserProfileUIForUser", windll["api-ms-win-gaming-tcui-l1-1-4"]), ((1, 'user'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowUserSettingsUI():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Gaming.GameUICompletionRoutine,c_void_p, use_last_error=False)(("ShowUserSettingsUI", windll["api-ms-win-gaming-tcui-l1-1-4"]), ((1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowUserSettingsUIForUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,win32more.Gaming.GameUICompletionRoutine,c_void_p, use_last_error=False)(("ShowUserSettingsUIForUser", windll["api-ms-win-gaming-tcui-l1-1-4"]), ((1, 'user'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "GameExplorer",
    "GameStatistics",
    "GAME_INSTALL_SCOPE",
    "GIS_NOT_INSTALLED",
    "GIS_CURRENT_USER",
    "GIS_ALL_USERS",
    "IGameExplorer",
    "GAMESTATS_OPEN_TYPE",
    "GAMESTATS_OPEN_OPENORCREATE",
    "GAMESTATS_OPEN_OPENONLY",
    "GAMESTATS_OPEN_RESULT",
    "GAMESTATS_OPEN_CREATED",
    "GAMESTATS_OPEN_OPENED",
    "IGameStatistics",
    "IGameStatisticsMgr",
    "IGameExplorer2",
    "GAMING_DEVICE_VENDOR_ID",
    "GAMING_DEVICE_VENDOR_ID_NONE",
    "GAMING_DEVICE_VENDOR_ID_MICROSOFT",
    "GAMING_DEVICE_DEVICE_ID",
    "GAMING_DEVICE_DEVICE_ID_NONE",
    "GAMING_DEVICE_DEVICE_ID_XBOX_ONE",
    "GAMING_DEVICE_DEVICE_ID_XBOX_ONE_S",
    "GAMING_DEVICE_DEVICE_ID_XBOX_ONE_X",
    "GAMING_DEVICE_DEVICE_ID_XBOX_ONE_X_DEVKIT",
    "GAMING_DEVICE_MODEL_INFORMATION",
    "GameUICompletionRoutine",
    "PlayerPickerUICompletionRoutine",
    "KnownGamingPrivileges",
    "XPRIVILEGE_BROADCAST",
    "XPRIVILEGE_VIEW_FRIENDS_LIST",
    "XPRIVILEGE_GAME_DVR",
    "XPRIVILEGE_SHARE_KINECT_CONTENT",
    "XPRIVILEGE_MULTIPLAYER_PARTIES",
    "XPRIVILEGE_COMMUNICATION_VOICE_INGAME",
    "XPRIVILEGE_COMMUNICATION_VOICE_SKYPE",
    "XPRIVILEGE_CLOUD_GAMING_MANAGE_SESSION",
    "XPRIVILEGE_CLOUD_GAMING_JOIN_SESSION",
    "XPRIVILEGE_CLOUD_SAVED_GAMES",
    "XPRIVILEGE_SHARE_CONTENT",
    "XPRIVILEGE_PREMIUM_CONTENT",
    "XPRIVILEGE_SUBSCRIPTION_CONTENT",
    "XPRIVILEGE_SOCIAL_NETWORK_SHARING",
    "XPRIVILEGE_PREMIUM_VIDEO",
    "XPRIVILEGE_VIDEO_COMMUNICATIONS",
    "XPRIVILEGE_PURCHASE_CONTENT",
    "XPRIVILEGE_USER_CREATED_CONTENT",
    "XPRIVILEGE_PROFILE_VIEWING",
    "XPRIVILEGE_COMMUNICATIONS",
    "XPRIVILEGE_MULTIPLAYER_SESSIONS",
    "XPRIVILEGE_ADD_FRIEND",
    "XblIdpAuthManager",
    "XblIdpAuthTokenResult",
    "XBL_IDP_AUTH_TOKEN_STATUS",
    "XBL_IDP_AUTH_TOKEN_STATUS_SUCCESS",
    "XBL_IDP_AUTH_TOKEN_STATUS_OFFLINE_SUCCESS",
    "XBL_IDP_AUTH_TOKEN_STATUS_NO_ACCOUNT_SET",
    "XBL_IDP_AUTH_TOKEN_STATUS_LOAD_MSA_ACCOUNT_FAILED",
    "XBL_IDP_AUTH_TOKEN_STATUS_XBOX_VETO",
    "XBL_IDP_AUTH_TOKEN_STATUS_MSA_INTERRUPT",
    "XBL_IDP_AUTH_TOKEN_STATUS_OFFLINE_NO_CONSENT",
    "XBL_IDP_AUTH_TOKEN_STATUS_VIEW_NOT_SET",
    "XBL_IDP_AUTH_TOKEN_STATUS_UNKNOWN",
    "IXblIdpAuthManager",
    "IXblIdpAuthTokenResult",
    "IXblIdpAuthTokenResult2",
    "HasExpandedResources",
    "GetExpandedResourceExclusiveCpuCount",
    "ReleaseExclusiveCpuSets",
    "GetGamingDeviceModelInformation",
    "ShowGameInviteUI",
    "ShowPlayerPickerUI",
    "ShowProfileCardUI",
    "ShowChangeFriendRelationshipUI",
    "ShowTitleAchievementsUI",
    "ProcessPendingGameUI",
    "TryCancelPendingGameUI",
    "CheckGamingPrivilegeWithUI",
    "CheckGamingPrivilegeSilently",
    "ShowGameInviteUIForUser",
    "ShowPlayerPickerUIForUser",
    "ShowProfileCardUIForUser",
    "ShowChangeFriendRelationshipUIForUser",
    "ShowTitleAchievementsUIForUser",
    "CheckGamingPrivilegeWithUIForUser",
    "CheckGamingPrivilegeSilentlyForUser",
    "ShowGameInviteUIWithContext",
    "ShowGameInviteUIWithContextForUser",
    "ShowGameInfoUI",
    "ShowGameInfoUIForUser",
    "ShowFindFriendsUI",
    "ShowFindFriendsUIForUser",
    "ShowCustomizeUserProfileUI",
    "ShowCustomizeUserProfileUIForUser",
    "ShowUserSettingsUI",
    "ShowUserSettingsUIForUser",
]
