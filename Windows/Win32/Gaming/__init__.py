from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Gaming
import Windows.Win32.System.Com
import Windows.Win32.System.WinRT
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
ID_GDF_XML_STR: String = '__GDF_XML'
ID_GDF_THUMBNAIL_STR: String = '__GDF_THUMBNAIL'
@winfunctype('api-ms-win-gaming-expandedresources-l1-1-0.dll')
def HasExpandedResources(hasExpandedResources: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-expandedresources-l1-1-0.dll')
def GetExpandedResourceExclusiveCpuCount(exclusiveCpuCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-expandedresources-l1-1-0.dll')
def ReleaseExclusiveCpuSets() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-deviceinformation-l1-1-0.dll')
def GetGamingDeviceModelInformation(information: POINTER(Windows.Win32.Gaming.GAMING_DEVICE_MODEL_INFORMATION_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-0.dll')
def ShowGameInviteUI(serviceConfigurationId: Windows.Win32.System.WinRT.HSTRING, sessionTemplateName: Windows.Win32.System.WinRT.HSTRING, sessionId: Windows.Win32.System.WinRT.HSTRING, invitationDisplayText: Windows.Win32.System.WinRT.HSTRING, completionRoutine: Windows.Win32.Gaming.GameUICompletionRoutine, context: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-0.dll')
def ShowPlayerPickerUI(promptDisplayText: Windows.Win32.System.WinRT.HSTRING, xuids: POINTER(Windows.Win32.System.WinRT.HSTRING), xuidsCount: UIntPtr, preSelectedXuids: POINTER(Windows.Win32.System.WinRT.HSTRING), preSelectedXuidsCount: UIntPtr, minSelectionCount: UIntPtr, maxSelectionCount: UIntPtr, completionRoutine: Windows.Win32.Gaming.PlayerPickerUICompletionRoutine, context: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-0.dll')
def ShowProfileCardUI(targetUserXuid: Windows.Win32.System.WinRT.HSTRING, completionRoutine: Windows.Win32.Gaming.GameUICompletionRoutine, context: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-0.dll')
def ShowChangeFriendRelationshipUI(targetUserXuid: Windows.Win32.System.WinRT.HSTRING, completionRoutine: Windows.Win32.Gaming.GameUICompletionRoutine, context: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-0.dll')
def ShowTitleAchievementsUI(titleId: UInt32, completionRoutine: Windows.Win32.Gaming.GameUICompletionRoutine, context: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-0.dll')
def ProcessPendingGameUI(waitForCompletion: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-0.dll')
def TryCancelPendingGameUI() -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-1.dll')
def CheckGamingPrivilegeWithUI(privilegeId: UInt32, scope: Windows.Win32.System.WinRT.HSTRING, policy: Windows.Win32.System.WinRT.HSTRING, friendlyMessage: Windows.Win32.System.WinRT.HSTRING, completionRoutine: Windows.Win32.Gaming.GameUICompletionRoutine, context: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-1.dll')
def CheckGamingPrivilegeSilently(privilegeId: UInt32, scope: Windows.Win32.System.WinRT.HSTRING, policy: Windows.Win32.System.WinRT.HSTRING, hasPrivilege: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-2.dll')
def ShowGameInviteUIForUser(user: Windows.Win32.System.WinRT.IInspectable_head, serviceConfigurationId: Windows.Win32.System.WinRT.HSTRING, sessionTemplateName: Windows.Win32.System.WinRT.HSTRING, sessionId: Windows.Win32.System.WinRT.HSTRING, invitationDisplayText: Windows.Win32.System.WinRT.HSTRING, completionRoutine: Windows.Win32.Gaming.GameUICompletionRoutine, context: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-2.dll')
def ShowPlayerPickerUIForUser(user: Windows.Win32.System.WinRT.IInspectable_head, promptDisplayText: Windows.Win32.System.WinRT.HSTRING, xuids: POINTER(Windows.Win32.System.WinRT.HSTRING), xuidsCount: UIntPtr, preSelectedXuids: POINTER(Windows.Win32.System.WinRT.HSTRING), preSelectedXuidsCount: UIntPtr, minSelectionCount: UIntPtr, maxSelectionCount: UIntPtr, completionRoutine: Windows.Win32.Gaming.PlayerPickerUICompletionRoutine, context: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-2.dll')
def ShowProfileCardUIForUser(user: Windows.Win32.System.WinRT.IInspectable_head, targetUserXuid: Windows.Win32.System.WinRT.HSTRING, completionRoutine: Windows.Win32.Gaming.GameUICompletionRoutine, context: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-2.dll')
def ShowChangeFriendRelationshipUIForUser(user: Windows.Win32.System.WinRT.IInspectable_head, targetUserXuid: Windows.Win32.System.WinRT.HSTRING, completionRoutine: Windows.Win32.Gaming.GameUICompletionRoutine, context: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-2.dll')
def ShowTitleAchievementsUIForUser(user: Windows.Win32.System.WinRT.IInspectable_head, titleId: UInt32, completionRoutine: Windows.Win32.Gaming.GameUICompletionRoutine, context: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-2.dll')
def CheckGamingPrivilegeWithUIForUser(user: Windows.Win32.System.WinRT.IInspectable_head, privilegeId: UInt32, scope: Windows.Win32.System.WinRT.HSTRING, policy: Windows.Win32.System.WinRT.HSTRING, friendlyMessage: Windows.Win32.System.WinRT.HSTRING, completionRoutine: Windows.Win32.Gaming.GameUICompletionRoutine, context: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-2.dll')
def CheckGamingPrivilegeSilentlyForUser(user: Windows.Win32.System.WinRT.IInspectable_head, privilegeId: UInt32, scope: Windows.Win32.System.WinRT.HSTRING, policy: Windows.Win32.System.WinRT.HSTRING, hasPrivilege: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-3.dll')
def ShowGameInviteUIWithContext(serviceConfigurationId: Windows.Win32.System.WinRT.HSTRING, sessionTemplateName: Windows.Win32.System.WinRT.HSTRING, sessionId: Windows.Win32.System.WinRT.HSTRING, invitationDisplayText: Windows.Win32.System.WinRT.HSTRING, customActivationContext: Windows.Win32.System.WinRT.HSTRING, completionRoutine: Windows.Win32.Gaming.GameUICompletionRoutine, context: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-3.dll')
def ShowGameInviteUIWithContextForUser(user: Windows.Win32.System.WinRT.IInspectable_head, serviceConfigurationId: Windows.Win32.System.WinRT.HSTRING, sessionTemplateName: Windows.Win32.System.WinRT.HSTRING, sessionId: Windows.Win32.System.WinRT.HSTRING, invitationDisplayText: Windows.Win32.System.WinRT.HSTRING, customActivationContext: Windows.Win32.System.WinRT.HSTRING, completionRoutine: Windows.Win32.Gaming.GameUICompletionRoutine, context: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-4.dll')
def ShowGameInfoUI(titleId: UInt32, completionRoutine: Windows.Win32.Gaming.GameUICompletionRoutine, context: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-4.dll')
def ShowGameInfoUIForUser(user: Windows.Win32.System.WinRT.IInspectable_head, titleId: UInt32, completionRoutine: Windows.Win32.Gaming.GameUICompletionRoutine, context: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-4.dll')
def ShowFindFriendsUI(completionRoutine: Windows.Win32.Gaming.GameUICompletionRoutine, context: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-4.dll')
def ShowFindFriendsUIForUser(user: Windows.Win32.System.WinRT.IInspectable_head, completionRoutine: Windows.Win32.Gaming.GameUICompletionRoutine, context: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-4.dll')
def ShowCustomizeUserProfileUI(completionRoutine: Windows.Win32.Gaming.GameUICompletionRoutine, context: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-4.dll')
def ShowCustomizeUserProfileUIForUser(user: Windows.Win32.System.WinRT.IInspectable_head, completionRoutine: Windows.Win32.Gaming.GameUICompletionRoutine, context: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-4.dll')
def ShowUserSettingsUI(completionRoutine: Windows.Win32.Gaming.GameUICompletionRoutine, context: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-gaming-tcui-l1-1-4.dll')
def ShowUserSettingsUIForUser(user: Windows.Win32.System.WinRT.IInspectable_head, completionRoutine: Windows.Win32.Gaming.GameUICompletionRoutine, context: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
GAMESTATS_OPEN_RESULT = Int32
GAMESTATS_OPEN_CREATED: GAMESTATS_OPEN_RESULT = 0
GAMESTATS_OPEN_OPENED: GAMESTATS_OPEN_RESULT = 1
GAMESTATS_OPEN_TYPE = Int32
GAMESTATS_OPEN_OPENORCREATE: GAMESTATS_OPEN_TYPE = 0
GAMESTATS_OPEN_OPENONLY: GAMESTATS_OPEN_TYPE = 1
GAME_INSTALL_SCOPE = Int32
GIS_NOT_INSTALLED: GAME_INSTALL_SCOPE = 1
GIS_CURRENT_USER: GAME_INSTALL_SCOPE = 2
GIS_ALL_USERS: GAME_INSTALL_SCOPE = 3
GAMING_DEVICE_DEVICE_ID = Int32
GAMING_DEVICE_DEVICE_ID_NONE: GAMING_DEVICE_DEVICE_ID = 0
GAMING_DEVICE_DEVICE_ID_XBOX_ONE: GAMING_DEVICE_DEVICE_ID = 1988865574
GAMING_DEVICE_DEVICE_ID_XBOX_ONE_S: GAMING_DEVICE_DEVICE_ID = 712204761
GAMING_DEVICE_DEVICE_ID_XBOX_ONE_X: GAMING_DEVICE_DEVICE_ID = 1523980231
GAMING_DEVICE_DEVICE_ID_XBOX_ONE_X_DEVKIT: GAMING_DEVICE_DEVICE_ID = 284675555
class GAMING_DEVICE_MODEL_INFORMATION(Structure):
    vendorId: Windows.Win32.Gaming.GAMING_DEVICE_VENDOR_ID
    deviceId: Windows.Win32.Gaming.GAMING_DEVICE_DEVICE_ID
GAMING_DEVICE_VENDOR_ID = Int32
GAMING_DEVICE_VENDOR_ID_NONE: GAMING_DEVICE_VENDOR_ID = 0
GAMING_DEVICE_VENDOR_ID_MICROSOFT: GAMING_DEVICE_VENDOR_ID = -1024700366
GameExplorer = Guid('9a5ea990-3034-4d6f-91-28-01-f3-c6-10-22-bc')
GameStatistics = Guid('dbc85a2c-c0dc-4961-b6-e2-d2-8b-62-c1-1a-d4')
@winfunctype_pointer
def GameUICompletionRoutine(returnCode: Windows.Win32.Foundation.HRESULT, context: c_void_p) -> Void: ...
class IGameExplorer(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e7b2fb72-d728-49b3-a5-f2-18-eb-f5-f1-34-9e')
    @commethod(3)
    def AddGame(bstrGDFBinaryPath: Windows.Win32.Foundation.BSTR, bstrGameInstallDirectory: Windows.Win32.Foundation.BSTR, installScope: Windows.Win32.Gaming.GAME_INSTALL_SCOPE, pguidInstanceID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveGame(guidInstanceID: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def UpdateGame(guidInstanceID: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def VerifyAccess(bstrGDFBinaryPath: Windows.Win32.Foundation.BSTR, pfHasAccess: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IGameExplorer2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('86874aa7-a1ed-450d-a7-eb-b8-9e-20-b2-ff-f3')
    @commethod(3)
    def InstallGame(binaryGDFPath: Windows.Win32.Foundation.PWSTR, installDirectory: Windows.Win32.Foundation.PWSTR, installScope: Windows.Win32.Gaming.GAME_INSTALL_SCOPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UninstallGame(binaryGDFPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CheckAccess(binaryGDFPath: Windows.Win32.Foundation.PWSTR, pHasAccess: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IGameStatistics(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3887c9ca-04a0-42ae-bc-4c-5f-a6-c7-72-11-45')
    @commethod(3)
    def GetMaxCategoryLength(cch: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMaxNameLength(cch: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMaxValueLength(cch: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMaxCategories(pMax: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetMaxStatsPerCategory(pMax: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetCategoryTitle(categoryIndex: UInt16, title: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCategoryTitle(categoryIndex: UInt16, pTitle: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetStatistic(categoryIndex: UInt16, statIndex: UInt16, pName: POINTER(Windows.Win32.Foundation.PWSTR), pValue: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetStatistic(categoryIndex: UInt16, statIndex: UInt16, name: Windows.Win32.Foundation.PWSTR, value: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Save(trackChanges: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetLastPlayedCategory(categoryIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetLastPlayedCategory(pCategoryIndex: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IGameStatisticsMgr(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('aff3ea11-e70e-407d-95-dd-35-e6-12-c4-1c-e2')
    @commethod(3)
    def GetGameStatistics(GDFBinaryPath: Windows.Win32.Foundation.PWSTR, openType: Windows.Win32.Gaming.GAMESTATS_OPEN_TYPE, pOpenResult: POINTER(Windows.Win32.Gaming.GAMESTATS_OPEN_RESULT), ppiStats: POINTER(Windows.Win32.Gaming.IGameStatistics_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveGameStatistics(GDFBinaryPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IXblIdpAuthManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('eb5ddb08-8bbf-449b-ac-21-b0-2d-de-b3-b1-36')
    @commethod(3)
    def SetGamerAccount(msaAccountId: Windows.Win32.Foundation.PWSTR, xuid: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetGamerAccount(msaAccountId: POINTER(Windows.Win32.Foundation.PWSTR), xuid: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetAppViewInitialized(appSid: Windows.Win32.Foundation.PWSTR, msaAccountId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetEnvironment(environment: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSandbox(sandbox: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTokenAndSignatureWithTokenResult(msaAccountId: Windows.Win32.Foundation.PWSTR, appSid: Windows.Win32.Foundation.PWSTR, msaTarget: Windows.Win32.Foundation.PWSTR, msaPolicy: Windows.Win32.Foundation.PWSTR, httpMethod: Windows.Win32.Foundation.PWSTR, uri: Windows.Win32.Foundation.PWSTR, headers: Windows.Win32.Foundation.PWSTR, body: c_char_p_no, bodySize: UInt32, forceRefresh: Windows.Win32.Foundation.BOOL, result: POINTER(Windows.Win32.Gaming.IXblIdpAuthTokenResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXblIdpAuthTokenResult(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('46ce0225-f267-4d68-b2-99-b2-76-25-52-de-c1')
    @commethod(3)
    def GetStatus(status: POINTER(Windows.Win32.Gaming.XBL_IDP_AUTH_TOKEN_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetErrorCode(errorCode: POINTER(Windows.Win32.Foundation.HRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetToken(token: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSignature(signature: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSandbox(sandbox: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetEnvironment(environment: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetMsaAccountId(msaAccountId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetXuid(xuid: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetGamertag(gamertag: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetAgeGroup(ageGroup: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetPrivileges(privileges: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetMsaTarget(msaTarget: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetMsaPolicy(msaPolicy: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetMsaAppId(msaAppId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetRedirect(redirect: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetMessage(message: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetHelpId(helpId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetEnforcementBans(enforcementBans: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetRestrictions(restrictions: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetTitleRestrictions(titleRestrictions: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IXblIdpAuthTokenResult2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('75d760b0-60b9-412d-99-4f-26-b2-cd-5f-78-12')
    @commethod(3)
    def GetModernGamertag(value: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetModernGamertagSuffix(value: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetUniqueModernGamertag(value: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
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
def PlayerPickerUICompletionRoutine(returnCode: Windows.Win32.Foundation.HRESULT, context: c_void_p, selectedXuids: POINTER(Windows.Win32.System.WinRT.HSTRING), selectedXuidsCount: UIntPtr) -> Void: ...
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
make_head(_module, 'GAMING_DEVICE_MODEL_INFORMATION')
make_head(_module, 'GameUICompletionRoutine')
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
_arch_optional = [
]
