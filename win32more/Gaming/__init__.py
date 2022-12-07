from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Gaming
import win32more.System.Com
import win32more.System.WinRT
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
ID_GDF_XML_STR: String = '__GDF_XML'
ID_GDF_THUMBNAIL_STR: String = '__GDF_THUMBNAIL'
@winfunctype('api-ms-win-gaming-expandedresources-l1-1-0.dll')
def HasExpandedResources(hasExpandedResources: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-expandedresources-l1-1-0.dll')
def GetExpandedResourceExclusiveCpuCount(exclusiveCpuCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-expandedresources-l1-1-0.dll')
def ReleaseExclusiveCpuSets() -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-deviceinformation-l1-1-0.dll')
def GetGamingDeviceModelInformation(information: POINTER(win32more.Gaming.GAMING_DEVICE_MODEL_INFORMATION_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-0.dll')
def ShowGameInviteUI(serviceConfigurationId: win32more.System.WinRT.HSTRING, sessionTemplateName: win32more.System.WinRT.HSTRING, sessionId: win32more.System.WinRT.HSTRING, invitationDisplayText: win32more.System.WinRT.HSTRING, completionRoutine: win32more.Gaming.GameUICompletionRoutine, context: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-0.dll')
def ShowPlayerPickerUI(promptDisplayText: win32more.System.WinRT.HSTRING, xuids: POINTER(win32more.System.WinRT.HSTRING), xuidsCount: UIntPtr, preSelectedXuids: POINTER(win32more.System.WinRT.HSTRING), preSelectedXuidsCount: UIntPtr, minSelectionCount: UIntPtr, maxSelectionCount: UIntPtr, completionRoutine: win32more.Gaming.PlayerPickerUICompletionRoutine, context: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-0.dll')
def ShowProfileCardUI(targetUserXuid: win32more.System.WinRT.HSTRING, completionRoutine: win32more.Gaming.GameUICompletionRoutine, context: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-0.dll')
def ShowChangeFriendRelationshipUI(targetUserXuid: win32more.System.WinRT.HSTRING, completionRoutine: win32more.Gaming.GameUICompletionRoutine, context: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-0.dll')
def ShowTitleAchievementsUI(titleId: UInt32, completionRoutine: win32more.Gaming.GameUICompletionRoutine, context: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-0.dll')
def ProcessPendingGameUI(waitForCompletion: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-0.dll')
def TryCancelPendingGameUI() -> win32more.Foundation.BOOL: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-1.dll')
def CheckGamingPrivilegeWithUI(privilegeId: UInt32, scope: win32more.System.WinRT.HSTRING, policy: win32more.System.WinRT.HSTRING, friendlyMessage: win32more.System.WinRT.HSTRING, completionRoutine: win32more.Gaming.GameUICompletionRoutine, context: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-1.dll')
def CheckGamingPrivilegeSilently(privilegeId: UInt32, scope: win32more.System.WinRT.HSTRING, policy: win32more.System.WinRT.HSTRING, hasPrivilege: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-2.dll')
def ShowGameInviteUIForUser(user: win32more.System.WinRT.IInspectable_head, serviceConfigurationId: win32more.System.WinRT.HSTRING, sessionTemplateName: win32more.System.WinRT.HSTRING, sessionId: win32more.System.WinRT.HSTRING, invitationDisplayText: win32more.System.WinRT.HSTRING, completionRoutine: win32more.Gaming.GameUICompletionRoutine, context: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-2.dll')
def ShowPlayerPickerUIForUser(user: win32more.System.WinRT.IInspectable_head, promptDisplayText: win32more.System.WinRT.HSTRING, xuids: POINTER(win32more.System.WinRT.HSTRING), xuidsCount: UIntPtr, preSelectedXuids: POINTER(win32more.System.WinRT.HSTRING), preSelectedXuidsCount: UIntPtr, minSelectionCount: UIntPtr, maxSelectionCount: UIntPtr, completionRoutine: win32more.Gaming.PlayerPickerUICompletionRoutine, context: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-2.dll')
def ShowProfileCardUIForUser(user: win32more.System.WinRT.IInspectable_head, targetUserXuid: win32more.System.WinRT.HSTRING, completionRoutine: win32more.Gaming.GameUICompletionRoutine, context: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-2.dll')
def ShowChangeFriendRelationshipUIForUser(user: win32more.System.WinRT.IInspectable_head, targetUserXuid: win32more.System.WinRT.HSTRING, completionRoutine: win32more.Gaming.GameUICompletionRoutine, context: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-2.dll')
def ShowTitleAchievementsUIForUser(user: win32more.System.WinRT.IInspectable_head, titleId: UInt32, completionRoutine: win32more.Gaming.GameUICompletionRoutine, context: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-2.dll')
def CheckGamingPrivilegeWithUIForUser(user: win32more.System.WinRT.IInspectable_head, privilegeId: UInt32, scope: win32more.System.WinRT.HSTRING, policy: win32more.System.WinRT.HSTRING, friendlyMessage: win32more.System.WinRT.HSTRING, completionRoutine: win32more.Gaming.GameUICompletionRoutine, context: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-2.dll')
def CheckGamingPrivilegeSilentlyForUser(user: win32more.System.WinRT.IInspectable_head, privilegeId: UInt32, scope: win32more.System.WinRT.HSTRING, policy: win32more.System.WinRT.HSTRING, hasPrivilege: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-3.dll')
def ShowGameInviteUIWithContext(serviceConfigurationId: win32more.System.WinRT.HSTRING, sessionTemplateName: win32more.System.WinRT.HSTRING, sessionId: win32more.System.WinRT.HSTRING, invitationDisplayText: win32more.System.WinRT.HSTRING, customActivationContext: win32more.System.WinRT.HSTRING, completionRoutine: win32more.Gaming.GameUICompletionRoutine, context: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-3.dll')
def ShowGameInviteUIWithContextForUser(user: win32more.System.WinRT.IInspectable_head, serviceConfigurationId: win32more.System.WinRT.HSTRING, sessionTemplateName: win32more.System.WinRT.HSTRING, sessionId: win32more.System.WinRT.HSTRING, invitationDisplayText: win32more.System.WinRT.HSTRING, customActivationContext: win32more.System.WinRT.HSTRING, completionRoutine: win32more.Gaming.GameUICompletionRoutine, context: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-4.dll')
def ShowGameInfoUI(titleId: UInt32, completionRoutine: win32more.Gaming.GameUICompletionRoutine, context: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-4.dll')
def ShowGameInfoUIForUser(user: win32more.System.WinRT.IInspectable_head, titleId: UInt32, completionRoutine: win32more.Gaming.GameUICompletionRoutine, context: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-4.dll')
def ShowFindFriendsUI(completionRoutine: win32more.Gaming.GameUICompletionRoutine, context: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-4.dll')
def ShowFindFriendsUIForUser(user: win32more.System.WinRT.IInspectable_head, completionRoutine: win32more.Gaming.GameUICompletionRoutine, context: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-4.dll')
def ShowCustomizeUserProfileUI(completionRoutine: win32more.Gaming.GameUICompletionRoutine, context: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-4.dll')
def ShowCustomizeUserProfileUIForUser(user: win32more.System.WinRT.IInspectable_head, completionRoutine: win32more.Gaming.GameUICompletionRoutine, context: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-4.dll')
def ShowUserSettingsUI(completionRoutine: win32more.Gaming.GameUICompletionRoutine, context: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-4.dll')
def ShowUserSettingsUIForUser(user: win32more.System.WinRT.IInspectable_head, completionRoutine: win32more.Gaming.GameUICompletionRoutine, context: c_void_p) -> win32more.Foundation.HRESULT: ...
GAME_INSTALL_SCOPE = Int32
GIS_NOT_INSTALLED: GAME_INSTALL_SCOPE = 1
GIS_CURRENT_USER: GAME_INSTALL_SCOPE = 2
GIS_ALL_USERS: GAME_INSTALL_SCOPE = 3
GameExplorer = Guid('9a5ea990-3034-4d6f-91-28-01-f3-c6-10-22-bc')
GameStatistics = Guid('dbc85a2c-c0dc-4961-b6-e2-d2-8b-62-c1-1a-d4')
GAMESTATS_OPEN_RESULT = Int32
GAMESTATS_OPEN_CREATED: GAMESTATS_OPEN_RESULT = 0
GAMESTATS_OPEN_OPENED: GAMESTATS_OPEN_RESULT = 1
GAMESTATS_OPEN_TYPE = Int32
GAMESTATS_OPEN_OPENORCREATE: GAMESTATS_OPEN_TYPE = 0
GAMESTATS_OPEN_OPENONLY: GAMESTATS_OPEN_TYPE = 1
@winfunctype_pointer
def GameUICompletionRoutine(returnCode: win32more.Foundation.HRESULT, context: c_void_p) -> Void: ...
GAMING_DEVICE_DEVICE_ID = Int32
GAMING_DEVICE_DEVICE_ID_NONE: GAMING_DEVICE_DEVICE_ID = 0
GAMING_DEVICE_DEVICE_ID_XBOX_ONE: GAMING_DEVICE_DEVICE_ID = 1988865574
GAMING_DEVICE_DEVICE_ID_XBOX_ONE_S: GAMING_DEVICE_DEVICE_ID = 712204761
GAMING_DEVICE_DEVICE_ID_XBOX_ONE_X: GAMING_DEVICE_DEVICE_ID = 1523980231
GAMING_DEVICE_DEVICE_ID_XBOX_ONE_X_DEVKIT: GAMING_DEVICE_DEVICE_ID = 284675555
class GAMING_DEVICE_MODEL_INFORMATION(Structure):
    vendorId: win32more.Gaming.GAMING_DEVICE_VENDOR_ID
    deviceId: win32more.Gaming.GAMING_DEVICE_DEVICE_ID
GAMING_DEVICE_VENDOR_ID = Int32
GAMING_DEVICE_VENDOR_ID_NONE: GAMING_DEVICE_VENDOR_ID = 0
GAMING_DEVICE_VENDOR_ID_MICROSOFT: GAMING_DEVICE_VENDOR_ID = -1024700366
class IGameExplorer(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('e7b2fb72-d728-49b3-a5-f2-18-eb-f5-f1-34-9e')
    @commethod(3)
    def AddGame(bstrGDFBinaryPath: win32more.Foundation.BSTR, bstrGameInstallDirectory: win32more.Foundation.BSTR, installScope: win32more.Gaming.GAME_INSTALL_SCOPE, pguidInstanceID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveGame(guidInstanceID: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def UpdateGame(guidInstanceID: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def VerifyAccess(bstrGDFBinaryPath: win32more.Foundation.BSTR, pfHasAccess: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IGameExplorer2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('86874aa7-a1ed-450d-a7-eb-b8-9e-20-b2-ff-f3')
    @commethod(3)
    def InstallGame(binaryGDFPath: win32more.Foundation.PWSTR, installDirectory: win32more.Foundation.PWSTR, installScope: win32more.Gaming.GAME_INSTALL_SCOPE) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UninstallGame(binaryGDFPath: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CheckAccess(binaryGDFPath: win32more.Foundation.PWSTR, pHasAccess: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IGameStatistics(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3887c9ca-04a0-42ae-bc-4c-5f-a6-c7-72-11-45')
    @commethod(3)
    def GetMaxCategoryLength(cch: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetMaxNameLength(cch: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetMaxValueLength(cch: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetMaxCategories(pMax: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetMaxStatsPerCategory(pMax: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetCategoryTitle(categoryIndex: UInt16, title: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetCategoryTitle(categoryIndex: UInt16, pTitle: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetStatistic(categoryIndex: UInt16, statIndex: UInt16, pName: POINTER(win32more.Foundation.PWSTR), pValue: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetStatistic(categoryIndex: UInt16, statIndex: UInt16, name: win32more.Foundation.PWSTR, value: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Save(trackChanges: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SetLastPlayedCategory(categoryIndex: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetLastPlayedCategory(pCategoryIndex: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IGameStatisticsMgr(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('aff3ea11-e70e-407d-95-dd-35-e6-12-c4-1c-e2')
    @commethod(3)
    def GetGameStatistics(GDFBinaryPath: win32more.Foundation.PWSTR, openType: win32more.Gaming.GAMESTATS_OPEN_TYPE, pOpenResult: POINTER(win32more.Gaming.GAMESTATS_OPEN_RESULT), ppiStats: POINTER(win32more.Gaming.IGameStatistics_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveGameStatistics(GDFBinaryPath: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class IXblIdpAuthManager(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('eb5ddb08-8bbf-449b-ac-21-b0-2d-de-b3-b1-36')
    @commethod(3)
    def SetGamerAccount(msaAccountId: win32more.Foundation.PWSTR, xuid: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetGamerAccount(msaAccountId: POINTER(win32more.Foundation.PWSTR), xuid: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetAppViewInitialized(appSid: win32more.Foundation.PWSTR, msaAccountId: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetEnvironment(environment: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetSandbox(sandbox: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetTokenAndSignatureWithTokenResult(msaAccountId: win32more.Foundation.PWSTR, appSid: win32more.Foundation.PWSTR, msaTarget: win32more.Foundation.PWSTR, msaPolicy: win32more.Foundation.PWSTR, httpMethod: win32more.Foundation.PWSTR, uri: win32more.Foundation.PWSTR, headers: win32more.Foundation.PWSTR, body: c_char_p_no, bodySize: UInt32, forceRefresh: win32more.Foundation.BOOL, result: POINTER(win32more.Gaming.IXblIdpAuthTokenResult_head)) -> win32more.Foundation.HRESULT: ...
class IXblIdpAuthTokenResult(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('46ce0225-f267-4d68-b2-99-b2-76-25-52-de-c1')
    @commethod(3)
    def GetStatus(status: POINTER(win32more.Gaming.XBL_IDP_AUTH_TOKEN_STATUS)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetErrorCode(errorCode: POINTER(win32more.Foundation.HRESULT)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetToken(token: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetSignature(signature: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetSandbox(sandbox: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetEnvironment(environment: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetMsaAccountId(msaAccountId: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetXuid(xuid: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetGamertag(gamertag: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetAgeGroup(ageGroup: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetPrivileges(privileges: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetMsaTarget(msaTarget: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetMsaPolicy(msaPolicy: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetMsaAppId(msaAppId: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetRedirect(redirect: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetMessage(message: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetHelpId(helpId: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetEnforcementBans(enforcementBans: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def GetRestrictions(restrictions: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def GetTitleRestrictions(titleRestrictions: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
class IXblIdpAuthTokenResult2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('75d760b0-60b9-412d-99-4f-26-b2-cd-5f-78-12')
    @commethod(3)
    def GetModernGamertag(value: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetModernGamertagSuffix(value: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetUniqueModernGamertag(value: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
KnownGamingPrivileges = Int32
XPRIVILEGE_BROADCAST: KnownGamingPrivileges = 190
XPRIVILEGE_VIEW_FRIENDS_LIST: KnownGamingPrivileges = 197
XPRIVILEGE_GAME_DVR: KnownGamingPrivileges = 198
XPRIVILEGE_SHARE_KINECT_CONTENT: KnownGamingPrivileges = 199
XPRIVILEGE_MULTIPLAYER_PARTIES: KnownGamingPrivileges = 203
XPRIVILEGE_COMMUNICATION_VOICE_INGAME: KnownGamingPrivileges = 205
XPRIVILEGE_COMMUNICATION_VOICE_SKYPE: KnownGamingPrivileges = 206
XPRIVILEGE_CLOUD_GAMING_MANAGE_SESSION: KnownGamingPrivileges = 207
XPRIVILEGE_CLOUD_GAMING_JOIN_SESSION: KnownGamingPrivileges = 208
XPRIVILEGE_CLOUD_SAVED_GAMES: KnownGamingPrivileges = 209
XPRIVILEGE_SHARE_CONTENT: KnownGamingPrivileges = 211
XPRIVILEGE_PREMIUM_CONTENT: KnownGamingPrivileges = 214
XPRIVILEGE_SUBSCRIPTION_CONTENT: KnownGamingPrivileges = 219
XPRIVILEGE_SOCIAL_NETWORK_SHARING: KnownGamingPrivileges = 220
XPRIVILEGE_PREMIUM_VIDEO: KnownGamingPrivileges = 224
XPRIVILEGE_VIDEO_COMMUNICATIONS: KnownGamingPrivileges = 235
XPRIVILEGE_PURCHASE_CONTENT: KnownGamingPrivileges = 245
XPRIVILEGE_USER_CREATED_CONTENT: KnownGamingPrivileges = 247
XPRIVILEGE_PROFILE_VIEWING: KnownGamingPrivileges = 249
XPRIVILEGE_COMMUNICATIONS: KnownGamingPrivileges = 252
XPRIVILEGE_MULTIPLAYER_SESSIONS: KnownGamingPrivileges = 254
XPRIVILEGE_ADD_FRIEND: KnownGamingPrivileges = 255
@winfunctype_pointer
def PlayerPickerUICompletionRoutine(returnCode: win32more.Foundation.HRESULT, context: c_void_p, selectedXuids: POINTER(win32more.System.WinRT.HSTRING), selectedXuidsCount: UIntPtr) -> Void: ...
XBL_IDP_AUTH_TOKEN_STATUS = Int32
XBL_IDP_AUTH_TOKEN_STATUS_SUCCESS: XBL_IDP_AUTH_TOKEN_STATUS = 0
XBL_IDP_AUTH_TOKEN_STATUS_OFFLINE_SUCCESS: XBL_IDP_AUTH_TOKEN_STATUS = 1
XBL_IDP_AUTH_TOKEN_STATUS_NO_ACCOUNT_SET: XBL_IDP_AUTH_TOKEN_STATUS = 2
XBL_IDP_AUTH_TOKEN_STATUS_LOAD_MSA_ACCOUNT_FAILED: XBL_IDP_AUTH_TOKEN_STATUS = 3
XBL_IDP_AUTH_TOKEN_STATUS_XBOX_VETO: XBL_IDP_AUTH_TOKEN_STATUS = 4
XBL_IDP_AUTH_TOKEN_STATUS_MSA_INTERRUPT: XBL_IDP_AUTH_TOKEN_STATUS = 5
XBL_IDP_AUTH_TOKEN_STATUS_OFFLINE_NO_CONSENT: XBL_IDP_AUTH_TOKEN_STATUS = 6
XBL_IDP_AUTH_TOKEN_STATUS_VIEW_NOT_SET: XBL_IDP_AUTH_TOKEN_STATUS = 7
XBL_IDP_AUTH_TOKEN_STATUS_UNKNOWN: XBL_IDP_AUTH_TOKEN_STATUS = -1
XblIdpAuthManager = Guid('ce23534b-56d8-4978-86-a2-7e-e5-70-64-04-68')
XblIdpAuthTokenResult = Guid('9f493441-744a-410c-ae-2b-9a-22-f7-c7-73-1f')
make_head(_module, 'GameUICompletionRoutine')
make_head(_module, 'GAMING_DEVICE_MODEL_INFORMATION')
make_head(_module, 'IGameExplorer')
make_head(_module, 'IGameExplorer2')
make_head(_module, 'IGameStatistics')
make_head(_module, 'IGameStatisticsMgr')
make_head(_module, 'IXblIdpAuthManager')
make_head(_module, 'IXblIdpAuthTokenResult')
make_head(_module, 'IXblIdpAuthTokenResult2')
make_head(_module, 'PlayerPickerUICompletionRoutine')
__all__ = [
    "CheckGamingPrivilegeSilently",
    "CheckGamingPrivilegeSilentlyForUser",
    "CheckGamingPrivilegeWithUI",
    "CheckGamingPrivilegeWithUIForUser",
    "GAMESTATS_OPEN_CREATED",
    "GAMESTATS_OPEN_OPENED",
    "GAMESTATS_OPEN_OPENONLY",
    "GAMESTATS_OPEN_OPENORCREATE",
    "GAMESTATS_OPEN_RESULT",
    "GAMESTATS_OPEN_TYPE",
    "GAME_INSTALL_SCOPE",
    "GAMING_DEVICE_DEVICE_ID",
    "GAMING_DEVICE_DEVICE_ID_NONE",
    "GAMING_DEVICE_DEVICE_ID_XBOX_ONE",
    "GAMING_DEVICE_DEVICE_ID_XBOX_ONE_S",
    "GAMING_DEVICE_DEVICE_ID_XBOX_ONE_X",
    "GAMING_DEVICE_DEVICE_ID_XBOX_ONE_X_DEVKIT",
    "GAMING_DEVICE_MODEL_INFORMATION",
    "GAMING_DEVICE_VENDOR_ID",
    "GAMING_DEVICE_VENDOR_ID_MICROSOFT",
    "GAMING_DEVICE_VENDOR_ID_NONE",
    "GIS_ALL_USERS",
    "GIS_CURRENT_USER",
    "GIS_NOT_INSTALLED",
    "GameExplorer",
    "GameStatistics",
    "GameUICompletionRoutine",
    "GetExpandedResourceExclusiveCpuCount",
    "GetGamingDeviceModelInformation",
    "HasExpandedResources",
    "ID_GDF_THUMBNAIL_STR",
    "ID_GDF_XML_STR",
    "IGameExplorer",
    "IGameExplorer2",
    "IGameStatistics",
    "IGameStatisticsMgr",
    "IXblIdpAuthManager",
    "IXblIdpAuthTokenResult",
    "IXblIdpAuthTokenResult2",
    "KnownGamingPrivileges",
    "PlayerPickerUICompletionRoutine",
    "ProcessPendingGameUI",
    "ReleaseExclusiveCpuSets",
    "ShowChangeFriendRelationshipUI",
    "ShowChangeFriendRelationshipUIForUser",
    "ShowCustomizeUserProfileUI",
    "ShowCustomizeUserProfileUIForUser",
    "ShowFindFriendsUI",
    "ShowFindFriendsUIForUser",
    "ShowGameInfoUI",
    "ShowGameInfoUIForUser",
    "ShowGameInviteUI",
    "ShowGameInviteUIForUser",
    "ShowGameInviteUIWithContext",
    "ShowGameInviteUIWithContextForUser",
    "ShowPlayerPickerUI",
    "ShowPlayerPickerUIForUser",
    "ShowProfileCardUI",
    "ShowProfileCardUIForUser",
    "ShowTitleAchievementsUI",
    "ShowTitleAchievementsUIForUser",
    "ShowUserSettingsUI",
    "ShowUserSettingsUIForUser",
    "TryCancelPendingGameUI",
    "XBL_IDP_AUTH_TOKEN_STATUS",
    "XBL_IDP_AUTH_TOKEN_STATUS_LOAD_MSA_ACCOUNT_FAILED",
    "XBL_IDP_AUTH_TOKEN_STATUS_MSA_INTERRUPT",
    "XBL_IDP_AUTH_TOKEN_STATUS_NO_ACCOUNT_SET",
    "XBL_IDP_AUTH_TOKEN_STATUS_OFFLINE_NO_CONSENT",
    "XBL_IDP_AUTH_TOKEN_STATUS_OFFLINE_SUCCESS",
    "XBL_IDP_AUTH_TOKEN_STATUS_SUCCESS",
    "XBL_IDP_AUTH_TOKEN_STATUS_UNKNOWN",
    "XBL_IDP_AUTH_TOKEN_STATUS_VIEW_NOT_SET",
    "XBL_IDP_AUTH_TOKEN_STATUS_XBOX_VETO",
    "XPRIVILEGE_ADD_FRIEND",
    "XPRIVILEGE_BROADCAST",
    "XPRIVILEGE_CLOUD_GAMING_JOIN_SESSION",
    "XPRIVILEGE_CLOUD_GAMING_MANAGE_SESSION",
    "XPRIVILEGE_CLOUD_SAVED_GAMES",
    "XPRIVILEGE_COMMUNICATIONS",
    "XPRIVILEGE_COMMUNICATION_VOICE_INGAME",
    "XPRIVILEGE_COMMUNICATION_VOICE_SKYPE",
    "XPRIVILEGE_GAME_DVR",
    "XPRIVILEGE_MULTIPLAYER_PARTIES",
    "XPRIVILEGE_MULTIPLAYER_SESSIONS",
    "XPRIVILEGE_PREMIUM_CONTENT",
    "XPRIVILEGE_PREMIUM_VIDEO",
    "XPRIVILEGE_PROFILE_VIEWING",
    "XPRIVILEGE_PURCHASE_CONTENT",
    "XPRIVILEGE_SHARE_CONTENT",
    "XPRIVILEGE_SHARE_KINECT_CONTENT",
    "XPRIVILEGE_SOCIAL_NETWORK_SHARING",
    "XPRIVILEGE_SUBSCRIPTION_CONTENT",
    "XPRIVILEGE_USER_CREATED_CONTENT",
    "XPRIVILEGE_VIDEO_COMMUNICATIONS",
    "XPRIVILEGE_VIEW_FRIENDS_LIST",
    "XblIdpAuthManager",
    "XblIdpAuthTokenResult",
]
