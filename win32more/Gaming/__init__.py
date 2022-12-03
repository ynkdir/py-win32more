from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Gaming
import win32more.System.Com
import win32more.System.WinRT
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
ID_GDF_XML_STR = '__GDF_XML'
ID_GDF_THUMBNAIL_STR = '__GDF_THUMBNAIL'
def _define_HasExpandedResources():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(('HasExpandedResources', windll['api-ms-win-gaming-expandedresources-l1-1-0.dll']), ((1, 'hasExpandedResources'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetExpandedResourceExclusiveCpuCount():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(('GetExpandedResourceExclusiveCpuCount', windll['api-ms-win-gaming-expandedresources-l1-1-0.dll']), ((1, 'exclusiveCpuCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReleaseExclusiveCpuSets():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,)(('ReleaseExclusiveCpuSets', windll['api-ms-win-gaming-expandedresources-l1-1-0.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetGamingDeviceModelInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Gaming.GAMING_DEVICE_MODEL_INFORMATION_head))(('GetGamingDeviceModelInformation', windll['api-ms-win-gaming-deviceinformation-l1-1-0.dll']), ((1, 'information'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowGameInviteUI():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.Gaming.GameUICompletionRoutine,c_void_p)(('ShowGameInviteUI', windll['api-ms-win-gaming-tcui-l1-1-0.dll']), ((1, 'serviceConfigurationId'),(1, 'sessionTemplateName'),(1, 'sessionId'),(1, 'invitationDisplayText'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowPlayerPickerUI():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING,POINTER(win32more.System.WinRT.HSTRING),UIntPtr,POINTER(win32more.System.WinRT.HSTRING),UIntPtr,UIntPtr,UIntPtr,win32more.Gaming.PlayerPickerUICompletionRoutine,c_void_p)(('ShowPlayerPickerUI', windll['api-ms-win-gaming-tcui-l1-1-0.dll']), ((1, 'promptDisplayText'),(1, 'xuids'),(1, 'xuidsCount'),(1, 'preSelectedXuids'),(1, 'preSelectedXuidsCount'),(1, 'minSelectionCount'),(1, 'maxSelectionCount'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowProfileCardUI():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING,win32more.Gaming.GameUICompletionRoutine,c_void_p)(('ShowProfileCardUI', windll['api-ms-win-gaming-tcui-l1-1-0.dll']), ((1, 'targetUserXuid'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowChangeFriendRelationshipUI():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING,win32more.Gaming.GameUICompletionRoutine,c_void_p)(('ShowChangeFriendRelationshipUI', windll['api-ms-win-gaming-tcui-l1-1-0.dll']), ((1, 'targetUserXuid'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowTitleAchievementsUI():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Gaming.GameUICompletionRoutine,c_void_p)(('ShowTitleAchievementsUI', windll['api-ms-win-gaming-tcui-l1-1-0.dll']), ((1, 'titleId'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ProcessPendingGameUI():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(('ProcessPendingGameUI', windll['api-ms-win-gaming-tcui-l1-1-0.dll']), ((1, 'waitForCompletion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TryCancelPendingGameUI():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,)(('TryCancelPendingGameUI', windll['api-ms-win-gaming-tcui-l1-1-0.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_CheckGamingPrivilegeWithUI():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.Gaming.GameUICompletionRoutine,c_void_p)(('CheckGamingPrivilegeWithUI', windll['api-ms-win-gaming-tcui-l1-1-1.dll']), ((1, 'privilegeId'),(1, 'scope'),(1, 'policy'),(1, 'friendlyMessage'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CheckGamingPrivilegeSilently():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,POINTER(win32more.Foundation.BOOL))(('CheckGamingPrivilegeSilently', windll['api-ms-win-gaming-tcui-l1-1-1.dll']), ((1, 'privilegeId'),(1, 'scope'),(1, 'policy'),(1, 'hasPrivilege'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowGameInviteUIForUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.Gaming.GameUICompletionRoutine,c_void_p)(('ShowGameInviteUIForUser', windll['api-ms-win-gaming-tcui-l1-1-2.dll']), ((1, 'user'),(1, 'serviceConfigurationId'),(1, 'sessionTemplateName'),(1, 'sessionId'),(1, 'invitationDisplayText'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowPlayerPickerUIForUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,win32more.System.WinRT.HSTRING,POINTER(win32more.System.WinRT.HSTRING),UIntPtr,POINTER(win32more.System.WinRT.HSTRING),UIntPtr,UIntPtr,UIntPtr,win32more.Gaming.PlayerPickerUICompletionRoutine,c_void_p)(('ShowPlayerPickerUIForUser', windll['api-ms-win-gaming-tcui-l1-1-2.dll']), ((1, 'user'),(1, 'promptDisplayText'),(1, 'xuids'),(1, 'xuidsCount'),(1, 'preSelectedXuids'),(1, 'preSelectedXuidsCount'),(1, 'minSelectionCount'),(1, 'maxSelectionCount'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowProfileCardUIForUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,win32more.System.WinRT.HSTRING,win32more.Gaming.GameUICompletionRoutine,c_void_p)(('ShowProfileCardUIForUser', windll['api-ms-win-gaming-tcui-l1-1-2.dll']), ((1, 'user'),(1, 'targetUserXuid'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowChangeFriendRelationshipUIForUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,win32more.System.WinRT.HSTRING,win32more.Gaming.GameUICompletionRoutine,c_void_p)(('ShowChangeFriendRelationshipUIForUser', windll['api-ms-win-gaming-tcui-l1-1-2.dll']), ((1, 'user'),(1, 'targetUserXuid'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowTitleAchievementsUIForUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,UInt32,win32more.Gaming.GameUICompletionRoutine,c_void_p)(('ShowTitleAchievementsUIForUser', windll['api-ms-win-gaming-tcui-l1-1-2.dll']), ((1, 'user'),(1, 'titleId'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CheckGamingPrivilegeWithUIForUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,UInt32,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.Gaming.GameUICompletionRoutine,c_void_p)(('CheckGamingPrivilegeWithUIForUser', windll['api-ms-win-gaming-tcui-l1-1-2.dll']), ((1, 'user'),(1, 'privilegeId'),(1, 'scope'),(1, 'policy'),(1, 'friendlyMessage'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CheckGamingPrivilegeSilentlyForUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,UInt32,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,POINTER(win32more.Foundation.BOOL))(('CheckGamingPrivilegeSilentlyForUser', windll['api-ms-win-gaming-tcui-l1-1-2.dll']), ((1, 'user'),(1, 'privilegeId'),(1, 'scope'),(1, 'policy'),(1, 'hasPrivilege'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowGameInviteUIWithContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.Gaming.GameUICompletionRoutine,c_void_p)(('ShowGameInviteUIWithContext', windll['api-ms-win-gaming-tcui-l1-1-3.dll']), ((1, 'serviceConfigurationId'),(1, 'sessionTemplateName'),(1, 'sessionId'),(1, 'invitationDisplayText'),(1, 'customActivationContext'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowGameInviteUIWithContextForUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.Gaming.GameUICompletionRoutine,c_void_p)(('ShowGameInviteUIWithContextForUser', windll['api-ms-win-gaming-tcui-l1-1-3.dll']), ((1, 'user'),(1, 'serviceConfigurationId'),(1, 'sessionTemplateName'),(1, 'sessionId'),(1, 'invitationDisplayText'),(1, 'customActivationContext'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowGameInfoUI():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Gaming.GameUICompletionRoutine,c_void_p)(('ShowGameInfoUI', windll['api-ms-win-gaming-tcui-l1-1-4.dll']), ((1, 'titleId'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowGameInfoUIForUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,UInt32,win32more.Gaming.GameUICompletionRoutine,c_void_p)(('ShowGameInfoUIForUser', windll['api-ms-win-gaming-tcui-l1-1-4.dll']), ((1, 'user'),(1, 'titleId'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowFindFriendsUI():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Gaming.GameUICompletionRoutine,c_void_p)(('ShowFindFriendsUI', windll['api-ms-win-gaming-tcui-l1-1-4.dll']), ((1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowFindFriendsUIForUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,win32more.Gaming.GameUICompletionRoutine,c_void_p)(('ShowFindFriendsUIForUser', windll['api-ms-win-gaming-tcui-l1-1-4.dll']), ((1, 'user'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowCustomizeUserProfileUI():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Gaming.GameUICompletionRoutine,c_void_p)(('ShowCustomizeUserProfileUI', windll['api-ms-win-gaming-tcui-l1-1-4.dll']), ((1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowCustomizeUserProfileUIForUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,win32more.Gaming.GameUICompletionRoutine,c_void_p)(('ShowCustomizeUserProfileUIForUser', windll['api-ms-win-gaming-tcui-l1-1-4.dll']), ((1, 'user'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowUserSettingsUI():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Gaming.GameUICompletionRoutine,c_void_p)(('ShowUserSettingsUI', windll['api-ms-win-gaming-tcui-l1-1-4.dll']), ((1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShowUserSettingsUIForUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,win32more.Gaming.GameUICompletionRoutine,c_void_p)(('ShowUserSettingsUIForUser', windll['api-ms-win-gaming-tcui-l1-1-4.dll']), ((1, 'user'),(1, 'completionRoutine'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
GAME_INSTALL_SCOPE = Int32
GIS_NOT_INSTALLED = 1
GIS_CURRENT_USER = 2
GIS_ALL_USERS = 3
GameExplorer = Guid('9a5ea990-3034-4d6f-91-28-01-f3-c6-10-22-bc')
GameStatistics = Guid('dbc85a2c-c0dc-4961-b6-e2-d2-8b-62-c1-1a-d4')
GAMESTATS_OPEN_RESULT = Int32
GAMESTATS_OPEN_CREATED = 0
GAMESTATS_OPEN_OPENED = 1
GAMESTATS_OPEN_TYPE = Int32
GAMESTATS_OPEN_OPENORCREATE = 0
GAMESTATS_OPEN_OPENONLY = 1
def _define_GameUICompletionRoutine():
    return WINFUNCTYPE(Void,win32more.Foundation.HRESULT,c_void_p)
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
        ('vendorId', win32more.Gaming.GAMING_DEVICE_VENDOR_ID),
        ('deviceId', win32more.Gaming.GAMING_DEVICE_DEVICE_ID),
    ]
    return GAMING_DEVICE_MODEL_INFORMATION
GAMING_DEVICE_VENDOR_ID = Int32
GAMING_DEVICE_VENDOR_ID_NONE = 0
GAMING_DEVICE_VENDOR_ID_MICROSOFT = -1024700366
def _define_IGameExplorer_head():
    class IGameExplorer(win32more.System.Com.IUnknown_head):
        Guid = Guid('e7b2fb72-d728-49b3-a5-f2-18-eb-f5-f1-34-9e')
    return IGameExplorer
def _define_IGameExplorer():
    IGameExplorer = win32more.Gaming.IGameExplorer_head
    IGameExplorer.AddGame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Gaming.GAME_INSTALL_SCOPE,POINTER(Guid))(3, 'AddGame', ((1, 'bstrGDFBinaryPath'),(1, 'bstrGameInstallDirectory'),(1, 'installScope'),(1, 'pguidInstanceID'),)))
    IGameExplorer.RemoveGame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid)(4, 'RemoveGame', ((1, 'guidInstanceID'),)))
    IGameExplorer.UpdateGame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid)(5, 'UpdateGame', ((1, 'guidInstanceID'),)))
    IGameExplorer.VerifyAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BOOL))(6, 'VerifyAccess', ((1, 'bstrGDFBinaryPath'),(1, 'pfHasAccess'),)))
    win32more.System.Com.IUnknown
    return IGameExplorer
def _define_IGameExplorer2_head():
    class IGameExplorer2(win32more.System.Com.IUnknown_head):
        Guid = Guid('86874aa7-a1ed-450d-a7-eb-b8-9e-20-b2-ff-f3')
    return IGameExplorer2
def _define_IGameExplorer2():
    IGameExplorer2 = win32more.Gaming.IGameExplorer2_head
    IGameExplorer2.InstallGame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Gaming.GAME_INSTALL_SCOPE)(3, 'InstallGame', ((1, 'binaryGDFPath'),(1, 'installDirectory'),(1, 'installScope'),)))
    IGameExplorer2.UninstallGame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(4, 'UninstallGame', ((1, 'binaryGDFPath'),)))
    IGameExplorer2.CheckAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BOOL))(5, 'CheckAccess', ((1, 'binaryGDFPath'),(1, 'pHasAccess'),)))
    win32more.System.Com.IUnknown
    return IGameExplorer2
def _define_IGameStatistics_head():
    class IGameStatistics(win32more.System.Com.IUnknown_head):
        Guid = Guid('3887c9ca-04a0-42ae-bc-4c-5f-a6-c7-72-11-45')
    return IGameStatistics
def _define_IGameStatistics():
    IGameStatistics = win32more.Gaming.IGameStatistics_head
    IGameStatistics.GetMaxCategoryLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetMaxCategoryLength', ((1, 'cch'),)))
    IGameStatistics.GetMaxNameLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(4, 'GetMaxNameLength', ((1, 'cch'),)))
    IGameStatistics.GetMaxValueLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(5, 'GetMaxValueLength', ((1, 'cch'),)))
    IGameStatistics.GetMaxCategories = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16))(6, 'GetMaxCategories', ((1, 'pMax'),)))
    IGameStatistics.GetMaxStatsPerCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16))(7, 'GetMaxStatsPerCategory', ((1, 'pMax'),)))
    IGameStatistics.SetCategoryTitle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,win32more.Foundation.PWSTR)(8, 'SetCategoryTitle', ((1, 'categoryIndex'),(1, 'title'),)))
    IGameStatistics.GetCategoryTitle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.Foundation.PWSTR))(9, 'GetCategoryTitle', ((1, 'categoryIndex'),(1, 'pTitle'),)))
    IGameStatistics.GetStatistic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,UInt16,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR))(10, 'GetStatistic', ((1, 'categoryIndex'),(1, 'statIndex'),(1, 'pName'),(1, 'pValue'),)))
    IGameStatistics.SetStatistic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,UInt16,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(11, 'SetStatistic', ((1, 'categoryIndex'),(1, 'statIndex'),(1, 'name'),(1, 'value'),)))
    IGameStatistics.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(12, 'Save', ((1, 'trackChanges'),)))
    IGameStatistics.SetLastPlayedCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(13, 'SetLastPlayedCategory', ((1, 'categoryIndex'),)))
    IGameStatistics.GetLastPlayedCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(14, 'GetLastPlayedCategory', ((1, 'pCategoryIndex'),)))
    win32more.System.Com.IUnknown
    return IGameStatistics
def _define_IGameStatisticsMgr_head():
    class IGameStatisticsMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('aff3ea11-e70e-407d-95-dd-35-e6-12-c4-1c-e2')
    return IGameStatisticsMgr
def _define_IGameStatisticsMgr():
    IGameStatisticsMgr = win32more.Gaming.IGameStatisticsMgr_head
    IGameStatisticsMgr.GetGameStatistics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Gaming.GAMESTATS_OPEN_TYPE,POINTER(win32more.Gaming.GAMESTATS_OPEN_RESULT),POINTER(win32more.Gaming.IGameStatistics_head))(3, 'GetGameStatistics', ((1, 'GDFBinaryPath'),(1, 'openType'),(1, 'pOpenResult'),(1, 'ppiStats'),)))
    IGameStatisticsMgr.RemoveGameStatistics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(4, 'RemoveGameStatistics', ((1, 'GDFBinaryPath'),)))
    win32more.System.Com.IUnknown
    return IGameStatisticsMgr
def _define_IXblIdpAuthManager_head():
    class IXblIdpAuthManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('eb5ddb08-8bbf-449b-ac-21-b0-2d-de-b3-b1-36')
    return IXblIdpAuthManager
def _define_IXblIdpAuthManager():
    IXblIdpAuthManager = win32more.Gaming.IXblIdpAuthManager_head
    IXblIdpAuthManager.SetGamerAccount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(3, 'SetGamerAccount', ((1, 'msaAccountId'),(1, 'xuid'),)))
    IXblIdpAuthManager.GetGamerAccount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR))(4, 'GetGamerAccount', ((1, 'msaAccountId'),(1, 'xuid'),)))
    IXblIdpAuthManager.SetAppViewInitialized = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(5, 'SetAppViewInitialized', ((1, 'appSid'),(1, 'msaAccountId'),)))
    IXblIdpAuthManager.GetEnvironment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(6, 'GetEnvironment', ((1, 'environment'),)))
    IXblIdpAuthManager.GetSandbox = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(7, 'GetSandbox', ((1, 'sandbox'),)))
    IXblIdpAuthManager.GetTokenAndSignatureWithTokenResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_char_p_no,UInt32,win32more.Foundation.BOOL,POINTER(win32more.Gaming.IXblIdpAuthTokenResult_head))(8, 'GetTokenAndSignatureWithTokenResult', ((1, 'msaAccountId'),(1, 'appSid'),(1, 'msaTarget'),(1, 'msaPolicy'),(1, 'httpMethod'),(1, 'uri'),(1, 'headers'),(1, 'body'),(1, 'bodySize'),(1, 'forceRefresh'),(1, 'result'),)))
    win32more.System.Com.IUnknown
    return IXblIdpAuthManager
def _define_IXblIdpAuthTokenResult_head():
    class IXblIdpAuthTokenResult(win32more.System.Com.IUnknown_head):
        Guid = Guid('46ce0225-f267-4d68-b2-99-b2-76-25-52-de-c1')
    return IXblIdpAuthTokenResult
def _define_IXblIdpAuthTokenResult():
    IXblIdpAuthTokenResult = win32more.Gaming.IXblIdpAuthTokenResult_head
    IXblIdpAuthTokenResult.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Gaming.XBL_IDP_AUTH_TOKEN_STATUS))(3, 'GetStatus', ((1, 'status'),)))
    IXblIdpAuthTokenResult.GetErrorCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HRESULT))(4, 'GetErrorCode', ((1, 'errorCode'),)))
    IXblIdpAuthTokenResult.GetToken = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(5, 'GetToken', ((1, 'token'),)))
    IXblIdpAuthTokenResult.GetSignature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(6, 'GetSignature', ((1, 'signature'),)))
    IXblIdpAuthTokenResult.GetSandbox = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(7, 'GetSandbox', ((1, 'sandbox'),)))
    IXblIdpAuthTokenResult.GetEnvironment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(8, 'GetEnvironment', ((1, 'environment'),)))
    IXblIdpAuthTokenResult.GetMsaAccountId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(9, 'GetMsaAccountId', ((1, 'msaAccountId'),)))
    IXblIdpAuthTokenResult.GetXuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(10, 'GetXuid', ((1, 'xuid'),)))
    IXblIdpAuthTokenResult.GetGamertag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(11, 'GetGamertag', ((1, 'gamertag'),)))
    IXblIdpAuthTokenResult.GetAgeGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(12, 'GetAgeGroup', ((1, 'ageGroup'),)))
    IXblIdpAuthTokenResult.GetPrivileges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(13, 'GetPrivileges', ((1, 'privileges'),)))
    IXblIdpAuthTokenResult.GetMsaTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(14, 'GetMsaTarget', ((1, 'msaTarget'),)))
    IXblIdpAuthTokenResult.GetMsaPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(15, 'GetMsaPolicy', ((1, 'msaPolicy'),)))
    IXblIdpAuthTokenResult.GetMsaAppId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(16, 'GetMsaAppId', ((1, 'msaAppId'),)))
    IXblIdpAuthTokenResult.GetRedirect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(17, 'GetRedirect', ((1, 'redirect'),)))
    IXblIdpAuthTokenResult.GetMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(18, 'GetMessage', ((1, 'message'),)))
    IXblIdpAuthTokenResult.GetHelpId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(19, 'GetHelpId', ((1, 'helpId'),)))
    IXblIdpAuthTokenResult.GetEnforcementBans = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(20, 'GetEnforcementBans', ((1, 'enforcementBans'),)))
    IXblIdpAuthTokenResult.GetRestrictions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(21, 'GetRestrictions', ((1, 'restrictions'),)))
    IXblIdpAuthTokenResult.GetTitleRestrictions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(22, 'GetTitleRestrictions', ((1, 'titleRestrictions'),)))
    win32more.System.Com.IUnknown
    return IXblIdpAuthTokenResult
def _define_IXblIdpAuthTokenResult2_head():
    class IXblIdpAuthTokenResult2(win32more.System.Com.IUnknown_head):
        Guid = Guid('75d760b0-60b9-412d-99-4f-26-b2-cd-5f-78-12')
    return IXblIdpAuthTokenResult2
def _define_IXblIdpAuthTokenResult2():
    IXblIdpAuthTokenResult2 = win32more.Gaming.IXblIdpAuthTokenResult2_head
    IXblIdpAuthTokenResult2.GetModernGamertag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(3, 'GetModernGamertag', ((1, 'value'),)))
    IXblIdpAuthTokenResult2.GetModernGamertagSuffix = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(4, 'GetModernGamertagSuffix', ((1, 'value'),)))
    IXblIdpAuthTokenResult2.GetUniqueModernGamertag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(5, 'GetUniqueModernGamertag', ((1, 'value'),)))
    win32more.System.Com.IUnknown
    return IXblIdpAuthTokenResult2
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
def _define_PlayerPickerUICompletionRoutine():
    return WINFUNCTYPE(Void,win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.System.WinRT.HSTRING),UIntPtr)
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
XblIdpAuthManager = Guid('ce23534b-56d8-4978-86-a2-7e-e5-70-64-04-68')
XblIdpAuthTokenResult = Guid('9f493441-744a-410c-ae-2b-9a-22-f7-c7-73-1f')
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
