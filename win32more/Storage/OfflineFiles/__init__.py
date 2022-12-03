from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Storage.OfflineFiles
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
OFFLINEFILES_SYNC_STATE_LOCAL_KNOWN = 1
OFFLINEFILES_SYNC_STATE_REMOTE_KNOWN = 2
OFFLINEFILES_CHANGES_NONE = 0
OFFLINEFILES_CHANGES_LOCAL_SIZE = 1
OFFLINEFILES_CHANGES_LOCAL_ATTRIBUTES = 2
OFFLINEFILES_CHANGES_LOCAL_TIME = 4
OFFLINEFILES_CHANGES_REMOTE_SIZE = 8
OFFLINEFILES_CHANGES_REMOTE_ATTRIBUTES = 16
OFFLINEFILES_CHANGES_REMOTE_TIME = 32
OFFLINEFILES_ITEM_FILTER_FLAG_MODIFIED_DATA = 1
OFFLINEFILES_ITEM_FILTER_FLAG_MODIFIED_ATTRIBUTES = 2
OFFLINEFILES_ITEM_FILTER_FLAG_MODIFIED = 4
OFFLINEFILES_ITEM_FILTER_FLAG_CREATED = 8
OFFLINEFILES_ITEM_FILTER_FLAG_DELETED = 16
OFFLINEFILES_ITEM_FILTER_FLAG_DIRTY = 32
OFFLINEFILES_ITEM_FILTER_FLAG_SPARSE = 64
OFFLINEFILES_ITEM_FILTER_FLAG_FILE = 128
OFFLINEFILES_ITEM_FILTER_FLAG_DIRECTORY = 256
OFFLINEFILES_ITEM_FILTER_FLAG_PINNED_USER = 512
OFFLINEFILES_ITEM_FILTER_FLAG_PINNED_OTHERS = 1024
OFFLINEFILES_ITEM_FILTER_FLAG_PINNED_COMPUTER = 2048
OFFLINEFILES_ITEM_FILTER_FLAG_PINNED = 4096
OFFLINEFILES_ITEM_FILTER_FLAG_GHOST = 8192
OFFLINEFILES_ITEM_FILTER_FLAG_SUSPENDED = 16384
OFFLINEFILES_ITEM_FILTER_FLAG_OFFLINE = 32768
OFFLINEFILES_ITEM_FILTER_FLAG_ONLINE = 65536
OFFLINEFILES_ITEM_FILTER_FLAG_USER_WRITE = 131072
OFFLINEFILES_ITEM_FILTER_FLAG_USER_READ = 262144
OFFLINEFILES_ITEM_FILTER_FLAG_USER_ANYACCESS = 524288
OFFLINEFILES_ITEM_FILTER_FLAG_OTHER_WRITE = 1048576
OFFLINEFILES_ITEM_FILTER_FLAG_OTHER_READ = 2097152
OFFLINEFILES_ITEM_FILTER_FLAG_OTHER_ANYACCESS = 4194304
OFFLINEFILES_ITEM_FILTER_FLAG_GUEST_WRITE = 8388608
OFFLINEFILES_ITEM_FILTER_FLAG_GUEST_READ = 16777216
OFFLINEFILES_ITEM_FILTER_FLAG_GUEST_ANYACCESS = 33554432
OFFLINEFILES_ITEM_QUERY_REMOTEINFO = 1
OFFLINEFILES_ITEM_QUERY_CONNECTIONSTATE = 2
OFFLINEFILES_ITEM_QUERY_LOCALDIRTYBYTECOUNT = 4
OFFLINEFILES_ITEM_QUERY_REMOTEDIRTYBYTECOUNT = 8
OFFLINEFILES_ITEM_QUERY_INCLUDETRANSPARENTCACHE = 16
OFFLINEFILES_ITEM_QUERY_ATTEMPT_TRANSITIONONLINE = 32
OFFLINEFILES_ITEM_QUERY_ADMIN = 2147483648
OFFLINEFILES_ENUM_FLAT = 1
OFFLINEFILES_ENUM_FLAT_FILESONLY = 2
OFFLINEFILES_SETTING_SCOPE_USER = 1
OFFLINEFILES_SETTING_SCOPE_COMPUTER = 2
OFFLINEFILES_SETTING_PinLinkTargets = 'LinkTargetCaching'
OFFLINEFILES_PINLINKTARGETS_NEVER = 0
OFFLINEFILES_PINLINKTARGETS_EXPLICIT = 1
OFFLINEFILES_PINLINKTARGETS_ALWAYS = 2
OFFLINEFILES_SYNC_CONTROL_FLAG_FILLSPARSE = 1
OFFLINEFILES_SYNC_CONTROL_FLAG_SYNCIN = 2
OFFLINEFILES_SYNC_CONTROL_FLAG_SYNCOUT = 4
OFFLINEFILES_SYNC_CONTROL_FLAG_PINNEWFILES = 8
OFFLINEFILES_SYNC_CONTROL_FLAG_PINLINKTARGETS = 16
OFFLINEFILES_SYNC_CONTROL_FLAG_PINFORUSER = 32
OFFLINEFILES_SYNC_CONTROL_FLAG_PINFORUSER_POLICY = 64
OFFLINEFILES_SYNC_CONTROL_FLAG_PINFORALL = 128
OFFLINEFILES_SYNC_CONTROL_FLAG_PINFORREDIR = 256
OFFLINEFILES_SYNC_CONTROL_FLAG_LOWPRIORITY = 512
OFFLINEFILES_SYNC_CONTROL_FLAG_ASYNCPROGRESS = 1024
OFFLINEFILES_SYNC_CONTROL_FLAG_INTERACTIVE = 2048
OFFLINEFILES_SYNC_CONTROL_FLAG_CONSOLE = 4096
OFFLINEFILES_SYNC_CONTROL_FLAG_SKIPSUSPENDEDDIRS = 8192
OFFLINEFILES_SYNC_CONTROL_FLAG_BACKGROUND = 65536
OFFLINEFILES_SYNC_CONTROL_FLAG_NONEWFILESOUT = 131072
OFFLINEFILES_SYNC_CONTROL_CR_MASK = 4026531840
OFFLINEFILES_SYNC_CONTROL_CR_DEFAULT = 0
OFFLINEFILES_SYNC_CONTROL_CR_KEEPLOCAL = 268435456
OFFLINEFILES_SYNC_CONTROL_CR_KEEPREMOTE = 536870912
OFFLINEFILES_SYNC_CONTROL_CR_KEEPLATEST = 805306368
OFFLINEFILES_PIN_CONTROL_FLAG_FORUSER = 32
OFFLINEFILES_PIN_CONTROL_FLAG_FORUSER_POLICY = 64
OFFLINEFILES_PIN_CONTROL_FLAG_FORALL = 128
OFFLINEFILES_PIN_CONTROL_FLAG_FORREDIR = 256
OFFLINEFILES_PIN_CONTROL_FLAG_FILL = 1
OFFLINEFILES_PIN_CONTROL_FLAG_LOWPRIORITY = 512
OFFLINEFILES_PIN_CONTROL_FLAG_ASYNCPROGRESS = 1024
OFFLINEFILES_PIN_CONTROL_FLAG_INTERACTIVE = 2048
OFFLINEFILES_PIN_CONTROL_FLAG_CONSOLE = 4096
OFFLINEFILES_PIN_CONTROL_FLAG_PINLINKTARGETS = 16
OFFLINEFILES_PIN_CONTROL_FLAG_BACKGROUND = 65536
OFFLINEFILES_ENCRYPTION_CONTROL_FLAG_LOWPRIORITY = 512
OFFLINEFILES_ENCRYPTION_CONTROL_FLAG_ASYNCPROGRESS = 1024
OFFLINEFILES_ENCRYPTION_CONTROL_FLAG_INTERACTIVE = 2048
OFFLINEFILES_ENCRYPTION_CONTROL_FLAG_CONSOLE = 4096
OFFLINEFILES_ENCRYPTION_CONTROL_FLAG_BACKGROUND = 65536
OFFLINEFILES_DELETE_FLAG_NOAUTOCACHED = 1
OFFLINEFILES_DELETE_FLAG_NOPINNED = 2
OFFLINEFILES_DELETE_FLAG_DELMODIFIED = 4
OFFLINEFILES_DELETE_FLAG_ADMIN = 2147483648
OFFLINEFILES_TRANSITION_FLAG_INTERACTIVE = 1
OFFLINEFILES_TRANSITION_FLAG_CONSOLE = 2
OFFLINEFILES_SYNC_ITEM_CHANGE_NONE = 0
OFFLINEFILES_SYNC_ITEM_CHANGE_CHANGETIME = 1
OFFLINEFILES_SYNC_ITEM_CHANGE_WRITETIME = 2
OFFLINEFILES_SYNC_ITEM_CHANGE_FILESIZE = 4
OFFLINEFILES_SYNC_ITEM_CHANGE_ATTRIBUTES = 8
def _define_OfflineFilesEnable():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.BOOL,POINTER(win32more.Foundation.BOOL))(('OfflineFilesEnable', windll['CSCAPI.dll']), ((1, 'bEnable'),(1, 'pbRebootRequired'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OfflineFilesStart():
    try:
        return WINFUNCTYPE(UInt32,)(('OfflineFilesStart', windll['CSCAPI.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_OfflineFilesQueryStatus():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Foundation.BOOL))(('OfflineFilesQueryStatus', windll['CSCAPI.dll']), ((1, 'pbActive'),(1, 'pbEnabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OfflineFilesQueryStatusEx():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Foundation.BOOL),POINTER(win32more.Foundation.BOOL))(('OfflineFilesQueryStatusEx', windll['CSCAPI.dll']), ((1, 'pbActive'),(1, 'pbEnabled'),(1, 'pbAvailable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IEnumOfflineFilesItems_head():
    class IEnumOfflineFilesItems(win32more.System.Com.IUnknown_head):
        Guid = Guid('da70e815-c361-4407-bc-0b-0d-70-46-e5-f2-cd')
    return IEnumOfflineFilesItems
def _define_IEnumOfflineFilesItems():
    IEnumOfflineFilesItems = win32more.Storage.OfflineFiles.IEnumOfflineFilesItems_head
    IEnumOfflineFilesItems.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.OfflineFiles.IOfflineFilesItem_head),POINTER(UInt32))(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumOfflineFilesItems.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'celt'),)))
    IEnumOfflineFilesItems.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumOfflineFilesItems.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.OfflineFiles.IEnumOfflineFilesItems_head))(6, 'Clone', ((1, 'ppenum'),)))
    win32more.System.Com.IUnknown
    return IEnumOfflineFilesItems
def _define_IEnumOfflineFilesSettings_head():
    class IEnumOfflineFilesSettings(win32more.System.Com.IUnknown_head):
        Guid = Guid('729680c4-1a38-47bc-9e-5c-02-c5-15-62-ac-30')
    return IEnumOfflineFilesSettings
def _define_IEnumOfflineFilesSettings():
    IEnumOfflineFilesSettings = win32more.Storage.OfflineFiles.IEnumOfflineFilesSettings_head
    IEnumOfflineFilesSettings.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.OfflineFiles.IOfflineFilesSetting_head),POINTER(UInt32))(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumOfflineFilesSettings.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'celt'),)))
    IEnumOfflineFilesSettings.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumOfflineFilesSettings.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.OfflineFiles.IEnumOfflineFilesSettings_head))(6, 'Clone', ((1, 'ppenum'),)))
    win32more.System.Com.IUnknown
    return IEnumOfflineFilesSettings
def _define_IOfflineFilesCache_head():
    class IOfflineFilesCache(win32more.System.Com.IUnknown_head):
        Guid = Guid('855d6203-7914-48b9-8d-40-4c-56-f5-ac-ff-c5')
    return IOfflineFilesCache
def _define_IOfflineFilesCache():
    IOfflineFilesCache = win32more.Storage.OfflineFiles.IOfflineFilesCache_head
    IOfflineFilesCache.Synchronize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.Foundation.PWSTR),UInt32,win32more.Foundation.BOOL,UInt32,win32more.Storage.OfflineFiles.IOfflineFilesSyncConflictHandler_head,win32more.Storage.OfflineFiles.IOfflineFilesSyncProgress_head,POINTER(Guid))(3, 'Synchronize', ((1, 'hwndParent'),(1, 'rgpszPaths'),(1, 'cPaths'),(1, 'bAsync'),(1, 'dwSyncControl'),(1, 'pISyncConflictHandler'),(1, 'pIProgress'),(1, 'pSyncId'),)))
    IOfflineFilesCache.DeleteItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),UInt32,UInt32,win32more.Foundation.BOOL,win32more.Storage.OfflineFiles.IOfflineFilesSimpleProgress_head)(4, 'DeleteItems', ((1, 'rgpszPaths'),(1, 'cPaths'),(1, 'dwFlags'),(1, 'bAsync'),(1, 'pIProgress'),)))
    IOfflineFilesCache.DeleteItemsForUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),UInt32,UInt32,win32more.Foundation.BOOL,win32more.Storage.OfflineFiles.IOfflineFilesSimpleProgress_head)(5, 'DeleteItemsForUser', ((1, 'pszUser'),(1, 'rgpszPaths'),(1, 'cPaths'),(1, 'dwFlags'),(1, 'bAsync'),(1, 'pIProgress'),)))
    IOfflineFilesCache.Pin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.Foundation.PWSTR),UInt32,win32more.Foundation.BOOL,win32more.Foundation.BOOL,UInt32,win32more.Storage.OfflineFiles.IOfflineFilesSyncProgress_head)(6, 'Pin', ((1, 'hwndParent'),(1, 'rgpszPaths'),(1, 'cPaths'),(1, 'bDeep'),(1, 'bAsync'),(1, 'dwPinControlFlags'),(1, 'pIProgress'),)))
    IOfflineFilesCache.Unpin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.Foundation.PWSTR),UInt32,win32more.Foundation.BOOL,win32more.Foundation.BOOL,UInt32,win32more.Storage.OfflineFiles.IOfflineFilesSyncProgress_head)(7, 'Unpin', ((1, 'hwndParent'),(1, 'rgpszPaths'),(1, 'cPaths'),(1, 'bDeep'),(1, 'bAsync'),(1, 'dwPinControlFlags'),(1, 'pIProgress'),)))
    IOfflineFilesCache.GetEncryptionStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Foundation.BOOL))(8, 'GetEncryptionStatus', ((1, 'pbEncrypted'),(1, 'pbPartial'),)))
    IOfflineFilesCache.Encrypt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.BOOL,UInt32,win32more.Foundation.BOOL,win32more.Storage.OfflineFiles.IOfflineFilesSyncProgress_head)(9, 'Encrypt', ((1, 'hwndParent'),(1, 'bEncrypt'),(1, 'dwEncryptionControlFlags'),(1, 'bAsync'),(1, 'pIProgress'),)))
    IOfflineFilesCache.FindItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Storage.OfflineFiles.IOfflineFilesItem_head))(10, 'FindItem', ((1, 'pszPath'),(1, 'dwQueryFlags'),(1, 'ppItem'),)))
    IOfflineFilesCache.FindItemEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Storage.OfflineFiles.IOfflineFilesItemFilter_head,win32more.Storage.OfflineFiles.IOfflineFilesItemFilter_head,win32more.Storage.OfflineFiles.IOfflineFilesItemFilter_head,win32more.Storage.OfflineFiles.IOfflineFilesItemFilter_head,UInt32,POINTER(win32more.Storage.OfflineFiles.IOfflineFilesItem_head))(11, 'FindItemEx', ((1, 'pszPath'),(1, 'pIncludeFileFilter'),(1, 'pIncludeDirFilter'),(1, 'pExcludeFileFilter'),(1, 'pExcludeDirFilter'),(1, 'dwQueryFlags'),(1, 'ppItem'),)))
    IOfflineFilesCache.RenameItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOL)(12, 'RenameItem', ((1, 'pszPathOriginal'),(1, 'pszPathNew'),(1, 'bReplaceIfExists'),)))
    IOfflineFilesCache.GetLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(13, 'GetLocation', ((1, 'ppszPath'),)))
    IOfflineFilesCache.GetDiskSpaceInformation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64),POINTER(UInt64),POINTER(UInt64),POINTER(UInt64),POINTER(UInt64))(14, 'GetDiskSpaceInformation', ((1, 'pcbVolumeTotal'),(1, 'pcbLimit'),(1, 'pcbUsed'),(1, 'pcbUnpinnedLimit'),(1, 'pcbUnpinnedUsed'),)))
    IOfflineFilesCache.SetDiskSpaceLimits = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,UInt64)(15, 'SetDiskSpaceLimits', ((1, 'cbLimit'),(1, 'cbUnpinnedLimit'),)))
    IOfflineFilesCache.ProcessAdminPinPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.OfflineFiles.IOfflineFilesSyncProgress_head,win32more.Storage.OfflineFiles.IOfflineFilesSyncProgress_head)(16, 'ProcessAdminPinPolicy', ((1, 'pPinProgress'),(1, 'pUnpinProgress'),)))
    IOfflineFilesCache.GetSettingObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.OfflineFiles.IOfflineFilesSetting_head))(17, 'GetSettingObject', ((1, 'pszSettingName'),(1, 'ppSetting'),)))
    IOfflineFilesCache.EnumSettingObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.OfflineFiles.IEnumOfflineFilesSettings_head))(18, 'EnumSettingObjects', ((1, 'ppEnum'),)))
    IOfflineFilesCache.IsPathCacheable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Storage.OfflineFiles.OFFLINEFILES_CACHING_MODE))(19, 'IsPathCacheable', ((1, 'pszPath'),(1, 'pbCacheable'),(1, 'pShareCachingMode'),)))
    win32more.System.Com.IUnknown
    return IOfflineFilesCache
def _define_IOfflineFilesCache2_head():
    class IOfflineFilesCache2(win32more.Storage.OfflineFiles.IOfflineFilesCache_head):
        Guid = Guid('8c075039-1551-4ed9-87-81-56-70-5c-04-d3-c0')
    return IOfflineFilesCache2
def _define_IOfflineFilesCache2():
    IOfflineFilesCache2 = win32more.Storage.OfflineFiles.IOfflineFilesCache2_head
    IOfflineFilesCache2.RenameItemEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOL)(20, 'RenameItemEx', ((1, 'pszPathOriginal'),(1, 'pszPathNew'),(1, 'bReplaceIfExists'),)))
    win32more.Storage.OfflineFiles.IOfflineFilesCache
    return IOfflineFilesCache2
def _define_IOfflineFilesChangeInfo_head():
    class IOfflineFilesChangeInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('a96e6fa4-e0d1-4c29-96-0b-ee-50-8f-e6-8c-72')
    return IOfflineFilesChangeInfo
def _define_IOfflineFilesChangeInfo():
    IOfflineFilesChangeInfo = win32more.Storage.OfflineFiles.IOfflineFilesChangeInfo_head
    IOfflineFilesChangeInfo.IsDirty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(3, 'IsDirty', ((1, 'pbDirty'),)))
    IOfflineFilesChangeInfo.IsDeletedOffline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(4, 'IsDeletedOffline', ((1, 'pbDeletedOffline'),)))
    IOfflineFilesChangeInfo.IsCreatedOffline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(5, 'IsCreatedOffline', ((1, 'pbCreatedOffline'),)))
    IOfflineFilesChangeInfo.IsLocallyModifiedData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(6, 'IsLocallyModifiedData', ((1, 'pbLocallyModifiedData'),)))
    IOfflineFilesChangeInfo.IsLocallyModifiedAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(7, 'IsLocallyModifiedAttributes', ((1, 'pbLocallyModifiedAttributes'),)))
    IOfflineFilesChangeInfo.IsLocallyModifiedTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(8, 'IsLocallyModifiedTime', ((1, 'pbLocallyModifiedTime'),)))
    win32more.System.Com.IUnknown
    return IOfflineFilesChangeInfo
def _define_IOfflineFilesConnectionInfo_head():
    class IOfflineFilesConnectionInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('efb23a09-a867-4be8-83-a6-86-96-9a-7d-08-56')
    return IOfflineFilesConnectionInfo
def _define_IOfflineFilesConnectionInfo():
    IOfflineFilesConnectionInfo = win32more.Storage.OfflineFiles.IOfflineFilesConnectionInfo_head
    IOfflineFilesConnectionInfo.GetConnectState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.OfflineFiles.OFFLINEFILES_CONNECT_STATE),POINTER(win32more.Storage.OfflineFiles.OFFLINEFILES_OFFLINE_REASON))(3, 'GetConnectState', ((1, 'pConnectState'),(1, 'pOfflineReason'),)))
    IOfflineFilesConnectionInfo.SetConnectState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,win32more.Storage.OfflineFiles.OFFLINEFILES_CONNECT_STATE)(4, 'SetConnectState', ((1, 'hwndParent'),(1, 'dwFlags'),(1, 'ConnectState'),)))
    IOfflineFilesConnectionInfo.TransitionOnline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32)(5, 'TransitionOnline', ((1, 'hwndParent'),(1, 'dwFlags'),)))
    IOfflineFilesConnectionInfo.TransitionOffline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,win32more.Foundation.BOOL,POINTER(win32more.Foundation.BOOL))(6, 'TransitionOffline', ((1, 'hwndParent'),(1, 'dwFlags'),(1, 'bForceOpenFilesClosed'),(1, 'pbOpenFilesPreventedTransition'),)))
    win32more.System.Com.IUnknown
    return IOfflineFilesConnectionInfo
def _define_IOfflineFilesDirectoryItem_head():
    class IOfflineFilesDirectoryItem(win32more.Storage.OfflineFiles.IOfflineFilesItem_head):
        Guid = Guid('2273597a-a08c-4a00-a3-7a-c1-ae-4e-9a-1c-fd')
    return IOfflineFilesDirectoryItem
def _define_IOfflineFilesDirectoryItem():
    IOfflineFilesDirectoryItem = win32more.Storage.OfflineFiles.IOfflineFilesDirectoryItem_head
    win32more.Storage.OfflineFiles.IOfflineFilesItem
    return IOfflineFilesDirectoryItem
def _define_IOfflineFilesDirtyInfo_head():
    class IOfflineFilesDirtyInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('0f50ce33-bac9-4eaa-a1-1d-da-0e-52-7d-04-7d')
    return IOfflineFilesDirtyInfo
def _define_IOfflineFilesDirtyInfo():
    IOfflineFilesDirtyInfo = win32more.Storage.OfflineFiles.IOfflineFilesDirtyInfo_head
    IOfflineFilesDirtyInfo.LocalDirtyByteCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.LARGE_INTEGER_head))(3, 'LocalDirtyByteCount', ((1, 'pDirtyByteCount'),)))
    IOfflineFilesDirtyInfo.RemoteDirtyByteCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.LARGE_INTEGER_head))(4, 'RemoteDirtyByteCount', ((1, 'pDirtyByteCount'),)))
    win32more.System.Com.IUnknown
    return IOfflineFilesDirtyInfo
def _define_IOfflineFilesErrorInfo_head():
    class IOfflineFilesErrorInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('7112fa5f-7571-435a-8e-b7-19-5c-7c-14-29-bc')
    return IOfflineFilesErrorInfo
def _define_IOfflineFilesErrorInfo():
    IOfflineFilesErrorInfo = win32more.Storage.OfflineFiles.IOfflineFilesErrorInfo_head
    IOfflineFilesErrorInfo.GetRawData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.BYTE_BLOB_head)))(3, 'GetRawData', ((1, 'ppBlob'),)))
    IOfflineFilesErrorInfo.GetDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(4, 'GetDescription', ((1, 'ppszDescription'),)))
    win32more.System.Com.IUnknown
    return IOfflineFilesErrorInfo
def _define_IOfflineFilesEvents_head():
    class IOfflineFilesEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('e25585c1-0caa-4eb1-87-3b-1c-ae-5b-77-c3-14')
    return IOfflineFilesEvents
def _define_IOfflineFilesEvents():
    IOfflineFilesEvents = win32more.Storage.OfflineFiles.IOfflineFilesEvents_head
    IOfflineFilesEvents.CacheMoved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(3, 'CacheMoved', ((1, 'pszOldPath'),(1, 'pszNewPath'),)))
    IOfflineFilesEvents.CacheIsFull = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'CacheIsFull', ()))
    IOfflineFilesEvents.CacheIsCorrupted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'CacheIsCorrupted', ()))
    IOfflineFilesEvents.Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(6, 'Enabled', ((1, 'bEnabled'),)))
    IOfflineFilesEvents.EncryptionChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Foundation.BOOL,win32more.Foundation.BOOL,win32more.Foundation.BOOL)(7, 'EncryptionChanged', ((1, 'bWasEncrypted'),(1, 'bWasPartial'),(1, 'bIsEncrypted'),(1, 'bIsPartial'),)))
    IOfflineFilesEvents.SyncBegin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(8, 'SyncBegin', ((1, 'rSyncId'),)))
    IOfflineFilesEvents.SyncFileResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PWSTR,win32more.Foundation.HRESULT)(9, 'SyncFileResult', ((1, 'rSyncId'),(1, 'pszFile'),(1, 'hrResult'),)))
    IOfflineFilesEvents.SyncConflictRecAdded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.FILETIME_head),win32more.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE)(10, 'SyncConflictRecAdded', ((1, 'pszConflictPath'),(1, 'pftConflictDateTime'),(1, 'ConflictSyncState'),)))
    IOfflineFilesEvents.SyncConflictRecUpdated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.FILETIME_head),win32more.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE)(11, 'SyncConflictRecUpdated', ((1, 'pszConflictPath'),(1, 'pftConflictDateTime'),(1, 'ConflictSyncState'),)))
    IOfflineFilesEvents.SyncConflictRecRemoved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.FILETIME_head),win32more.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE)(12, 'SyncConflictRecRemoved', ((1, 'pszConflictPath'),(1, 'pftConflictDateTime'),(1, 'ConflictSyncState'),)))
    IOfflineFilesEvents.SyncEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.HRESULT)(13, 'SyncEnd', ((1, 'rSyncId'),(1, 'hrResult'),)))
    IOfflineFilesEvents.NetTransportArrived = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(14, 'NetTransportArrived', ()))
    IOfflineFilesEvents.NoNetTransports = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(15, 'NoNetTransports', ()))
    IOfflineFilesEvents.ItemDisconnected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE)(16, 'ItemDisconnected', ((1, 'pszPath'),(1, 'ItemType'),)))
    IOfflineFilesEvents.ItemReconnected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE)(17, 'ItemReconnected', ((1, 'pszPath'),(1, 'ItemType'),)))
    IOfflineFilesEvents.ItemAvailableOffline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE)(18, 'ItemAvailableOffline', ((1, 'pszPath'),(1, 'ItemType'),)))
    IOfflineFilesEvents.ItemNotAvailableOffline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE)(19, 'ItemNotAvailableOffline', ((1, 'pszPath'),(1, 'ItemType'),)))
    IOfflineFilesEvents.ItemPinned = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE)(20, 'ItemPinned', ((1, 'pszPath'),(1, 'ItemType'),)))
    IOfflineFilesEvents.ItemNotPinned = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE)(21, 'ItemNotPinned', ((1, 'pszPath'),(1, 'ItemType'),)))
    IOfflineFilesEvents.ItemModified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE,win32more.Foundation.BOOL,win32more.Foundation.BOOL)(22, 'ItemModified', ((1, 'pszPath'),(1, 'ItemType'),(1, 'bModifiedData'),(1, 'bModifiedAttributes'),)))
    IOfflineFilesEvents.ItemAddedToCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE)(23, 'ItemAddedToCache', ((1, 'pszPath'),(1, 'ItemType'),)))
    IOfflineFilesEvents.ItemDeletedFromCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE)(24, 'ItemDeletedFromCache', ((1, 'pszPath'),(1, 'ItemType'),)))
    IOfflineFilesEvents.ItemRenamed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE)(25, 'ItemRenamed', ((1, 'pszOldPath'),(1, 'pszNewPath'),(1, 'ItemType'),)))
    IOfflineFilesEvents.DataLost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(26, 'DataLost', ()))
    IOfflineFilesEvents.Ping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(27, 'Ping', ()))
    win32more.System.Com.IUnknown
    return IOfflineFilesEvents
def _define_IOfflineFilesEvents2_head():
    class IOfflineFilesEvents2(win32more.Storage.OfflineFiles.IOfflineFilesEvents_head):
        Guid = Guid('1ead8f56-ff76-4faa-a7-95-6f-6e-f7-92-49-8b')
    return IOfflineFilesEvents2
def _define_IOfflineFilesEvents2():
    IOfflineFilesEvents2 = win32more.Storage.OfflineFiles.IOfflineFilesEvents2_head
    IOfflineFilesEvents2.ItemReconnectBegin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(28, 'ItemReconnectBegin', ()))
    IOfflineFilesEvents2.ItemReconnectEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(29, 'ItemReconnectEnd', ()))
    IOfflineFilesEvents2.CacheEvictBegin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(30, 'CacheEvictBegin', ()))
    IOfflineFilesEvents2.CacheEvictEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(31, 'CacheEvictEnd', ()))
    IOfflineFilesEvents2.BackgroundSyncBegin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(32, 'BackgroundSyncBegin', ((1, 'dwSyncControlFlags'),)))
    IOfflineFilesEvents2.BackgroundSyncEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(33, 'BackgroundSyncEnd', ((1, 'dwSyncControlFlags'),)))
    IOfflineFilesEvents2.PolicyChangeDetected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(34, 'PolicyChangeDetected', ()))
    IOfflineFilesEvents2.PreferenceChangeDetected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(35, 'PreferenceChangeDetected', ()))
    IOfflineFilesEvents2.SettingsChangesApplied = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(36, 'SettingsChangesApplied', ()))
    win32more.Storage.OfflineFiles.IOfflineFilesEvents
    return IOfflineFilesEvents2
def _define_IOfflineFilesEvents3_head():
    class IOfflineFilesEvents3(win32more.Storage.OfflineFiles.IOfflineFilesEvents2_head):
        Guid = Guid('9ba04a45-ee69-42f0-9a-b1-7d-b5-c8-80-58-08')
    return IOfflineFilesEvents3
def _define_IOfflineFilesEvents3():
    IOfflineFilesEvents3 = win32more.Storage.OfflineFiles.IOfflineFilesEvents3_head
    IOfflineFilesEvents3.TransparentCacheItemNotify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Storage.OfflineFiles.OFFLINEFILES_EVENTS,win32more.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE,win32more.Foundation.BOOL,win32more.Foundation.BOOL,win32more.Foundation.PWSTR)(37, 'TransparentCacheItemNotify', ((1, 'pszPath'),(1, 'EventType'),(1, 'ItemType'),(1, 'bModifiedData'),(1, 'bModifiedAttributes'),(1, 'pzsOldPath'),)))
    IOfflineFilesEvents3.PrefetchFileBegin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(38, 'PrefetchFileBegin', ((1, 'pszPath'),)))
    IOfflineFilesEvents3.PrefetchFileEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.HRESULT)(39, 'PrefetchFileEnd', ((1, 'pszPath'),(1, 'hrResult'),)))
    win32more.Storage.OfflineFiles.IOfflineFilesEvents2
    return IOfflineFilesEvents3
def _define_IOfflineFilesEvents4_head():
    class IOfflineFilesEvents4(win32more.Storage.OfflineFiles.IOfflineFilesEvents3_head):
        Guid = Guid('dbd69b1e-c7d2-473e-b3-5f-9d-8c-24-c0-c4-84')
    return IOfflineFilesEvents4
def _define_IOfflineFilesEvents4():
    IOfflineFilesEvents4 = win32more.Storage.OfflineFiles.IOfflineFilesEvents4_head
    IOfflineFilesEvents4.PrefetchCloseHandleBegin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(40, 'PrefetchCloseHandleBegin', ()))
    IOfflineFilesEvents4.PrefetchCloseHandleEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Foundation.HRESULT)(41, 'PrefetchCloseHandleEnd', ((1, 'dwClosedHandleCount'),(1, 'dwOpenHandleCount'),(1, 'hrResult'),)))
    win32more.Storage.OfflineFiles.IOfflineFilesEvents3
    return IOfflineFilesEvents4
def _define_IOfflineFilesEventsFilter_head():
    class IOfflineFilesEventsFilter(win32more.System.Com.IUnknown_head):
        Guid = Guid('33fc4e1b-0716-40fa-ba-65-6e-62-a8-4a-84-6f')
    return IOfflineFilesEventsFilter
def _define_IOfflineFilesEventsFilter():
    IOfflineFilesEventsFilter = win32more.Storage.OfflineFiles.IOfflineFilesEventsFilter_head
    IOfflineFilesEventsFilter.GetPathFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Storage.OfflineFiles.OFFLINEFILES_PATHFILTER_MATCH))(3, 'GetPathFilter', ((1, 'ppszFilter'),(1, 'pMatch'),)))
    IOfflineFilesEventsFilter.GetIncludedEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.OfflineFiles.OFFLINEFILES_EVENTS),POINTER(UInt32))(4, 'GetIncludedEvents', ((1, 'cElements'),(1, 'prgEvents'),(1, 'pcEvents'),)))
    IOfflineFilesEventsFilter.GetExcludedEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.OfflineFiles.OFFLINEFILES_EVENTS),POINTER(UInt32))(5, 'GetExcludedEvents', ((1, 'cElements'),(1, 'prgEvents'),(1, 'pcEvents'),)))
    win32more.System.Com.IUnknown
    return IOfflineFilesEventsFilter
def _define_IOfflineFilesFileItem_head():
    class IOfflineFilesFileItem(win32more.Storage.OfflineFiles.IOfflineFilesItem_head):
        Guid = Guid('8dfadead-26c2-4eff-8a-72-6b-50-72-3d-9a-00')
    return IOfflineFilesFileItem
def _define_IOfflineFilesFileItem():
    IOfflineFilesFileItem = win32more.Storage.OfflineFiles.IOfflineFilesFileItem_head
    IOfflineFilesFileItem.IsSparse = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(8, 'IsSparse', ((1, 'pbIsSparse'),)))
    IOfflineFilesFileItem.IsEncrypted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(9, 'IsEncrypted', ((1, 'pbIsEncrypted'),)))
    win32more.Storage.OfflineFiles.IOfflineFilesItem
    return IOfflineFilesFileItem
def _define_IOfflineFilesFileSysInfo_head():
    class IOfflineFilesFileSysInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('bc1a163f-7bfd-4d88-9c-66-96-ea-9a-6a-3d-6b')
    return IOfflineFilesFileSysInfo
def _define_IOfflineFilesFileSysInfo():
    IOfflineFilesFileSysInfo = win32more.Storage.OfflineFiles.IOfflineFilesFileSysInfo_head
    IOfflineFilesFileSysInfo.GetAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.OfflineFiles.OFFLINEFILES_ITEM_COPY,POINTER(UInt32))(3, 'GetAttributes', ((1, 'copy'),(1, 'pdwAttributes'),)))
    IOfflineFilesFileSysInfo.GetTimes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.OfflineFiles.OFFLINEFILES_ITEM_COPY,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head))(4, 'GetTimes', ((1, 'copy'),(1, 'pftCreationTime'),(1, 'pftLastWriteTime'),(1, 'pftChangeTime'),(1, 'pftLastAccessTime'),)))
    IOfflineFilesFileSysInfo.GetFileSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.OfflineFiles.OFFLINEFILES_ITEM_COPY,POINTER(win32more.Foundation.LARGE_INTEGER_head))(5, 'GetFileSize', ((1, 'copy'),(1, 'pSize'),)))
    win32more.System.Com.IUnknown
    return IOfflineFilesFileSysInfo
def _define_IOfflineFilesGhostInfo_head():
    class IOfflineFilesGhostInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('2b09d48c-8ab5-464f-a7-55-a5-9d-92-f9-94-29')
    return IOfflineFilesGhostInfo
def _define_IOfflineFilesGhostInfo():
    IOfflineFilesGhostInfo = win32more.Storage.OfflineFiles.IOfflineFilesGhostInfo_head
    IOfflineFilesGhostInfo.IsGhosted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(3, 'IsGhosted', ((1, 'pbGhosted'),)))
    win32more.System.Com.IUnknown
    return IOfflineFilesGhostInfo
def _define_IOfflineFilesItem_head():
    class IOfflineFilesItem(win32more.System.Com.IUnknown_head):
        Guid = Guid('4a753da6-e044-4f12-a7-18-5d-14-d0-79-a9-06')
    return IOfflineFilesItem
def _define_IOfflineFilesItem():
    IOfflineFilesItem = win32more.Storage.OfflineFiles.IOfflineFilesItem_head
    IOfflineFilesItem.GetItemType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE))(3, 'GetItemType', ((1, 'pItemType'),)))
    IOfflineFilesItem.GetPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(4, 'GetPath', ((1, 'ppszPath'),)))
    IOfflineFilesItem.GetParentItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.OfflineFiles.IOfflineFilesItem_head))(5, 'GetParentItem', ((1, 'ppItem'),)))
    IOfflineFilesItem.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'Refresh', ((1, 'dwQueryFlags'),)))
    IOfflineFilesItem.IsMarkedForDeletion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(7, 'IsMarkedForDeletion', ((1, 'pbMarkedForDeletion'),)))
    win32more.System.Com.IUnknown
    return IOfflineFilesItem
def _define_IOfflineFilesItemContainer_head():
    class IOfflineFilesItemContainer(win32more.System.Com.IUnknown_head):
        Guid = Guid('3836f049-9413-45dd-bf-46-b5-aa-a8-2d-c3-10')
    return IOfflineFilesItemContainer
def _define_IOfflineFilesItemContainer():
    IOfflineFilesItemContainer = win32more.Storage.OfflineFiles.IOfflineFilesItemContainer_head
    IOfflineFilesItemContainer.EnumItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.OfflineFiles.IEnumOfflineFilesItems_head))(3, 'EnumItems', ((1, 'dwQueryFlags'),(1, 'ppenum'),)))
    IOfflineFilesItemContainer.EnumItemsEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.OfflineFiles.IOfflineFilesItemFilter_head,win32more.Storage.OfflineFiles.IOfflineFilesItemFilter_head,win32more.Storage.OfflineFiles.IOfflineFilesItemFilter_head,win32more.Storage.OfflineFiles.IOfflineFilesItemFilter_head,UInt32,UInt32,POINTER(win32more.Storage.OfflineFiles.IEnumOfflineFilesItems_head))(4, 'EnumItemsEx', ((1, 'pIncludeFileFilter'),(1, 'pIncludeDirFilter'),(1, 'pExcludeFileFilter'),(1, 'pExcludeDirFilter'),(1, 'dwEnumFlags'),(1, 'dwQueryFlags'),(1, 'ppenum'),)))
    win32more.System.Com.IUnknown
    return IOfflineFilesItemContainer
def _define_IOfflineFilesItemFilter_head():
    class IOfflineFilesItemFilter(win32more.System.Com.IUnknown_head):
        Guid = Guid('f4b5a26c-dc05-4f20-ad-a4-55-1f-10-77-be-5c')
    return IOfflineFilesItemFilter
def _define_IOfflineFilesItemFilter():
    IOfflineFilesItemFilter = win32more.Storage.OfflineFiles.IOfflineFilesItemFilter_head
    IOfflineFilesItemFilter.GetFilterFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64),POINTER(UInt64))(3, 'GetFilterFlags', ((1, 'pullFlags'),(1, 'pullMask'),)))
    IOfflineFilesItemFilter.GetTimeFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.BOOL),POINTER(win32more.Storage.OfflineFiles.OFFLINEFILES_ITEM_TIME),POINTER(win32more.Storage.OfflineFiles.OFFLINEFILES_COMPARE))(4, 'GetTimeFilter', ((1, 'pftTime'),(1, 'pbEvalTimeOfDay'),(1, 'pTimeType'),(1, 'pCompare'),)))
    IOfflineFilesItemFilter.GetPatternFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32)(5, 'GetPatternFilter', ((1, 'pszPattern'),(1, 'cchPattern'),)))
    win32more.System.Com.IUnknown
    return IOfflineFilesItemFilter
def _define_IOfflineFilesPinInfo_head():
    class IOfflineFilesPinInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('5b2b0655-b3fd-497d-ad-eb-bd-15-6b-c8-35-5b')
    return IOfflineFilesPinInfo
def _define_IOfflineFilesPinInfo():
    IOfflineFilesPinInfo = win32more.Storage.OfflineFiles.IOfflineFilesPinInfo_head
    IOfflineFilesPinInfo.IsPinned = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(3, 'IsPinned', ((1, 'pbPinned'),)))
    IOfflineFilesPinInfo.IsPinnedForUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Foundation.BOOL))(4, 'IsPinnedForUser', ((1, 'pbPinnedForUser'),(1, 'pbInherit'),)))
    IOfflineFilesPinInfo.IsPinnedForUserByPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Foundation.BOOL))(5, 'IsPinnedForUserByPolicy', ((1, 'pbPinnedForUser'),(1, 'pbInherit'),)))
    IOfflineFilesPinInfo.IsPinnedForComputer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Foundation.BOOL))(6, 'IsPinnedForComputer', ((1, 'pbPinnedForComputer'),(1, 'pbInherit'),)))
    IOfflineFilesPinInfo.IsPinnedForFolderRedirection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Foundation.BOOL))(7, 'IsPinnedForFolderRedirection', ((1, 'pbPinnedForFolderRedirection'),(1, 'pbInherit'),)))
    win32more.System.Com.IUnknown
    return IOfflineFilesPinInfo
def _define_IOfflineFilesPinInfo2_head():
    class IOfflineFilesPinInfo2(win32more.Storage.OfflineFiles.IOfflineFilesPinInfo_head):
        Guid = Guid('623c58a2-42ed-4ad7-b6-9a-0f-1b-30-a7-2d-0d')
    return IOfflineFilesPinInfo2
def _define_IOfflineFilesPinInfo2():
    IOfflineFilesPinInfo2 = win32more.Storage.OfflineFiles.IOfflineFilesPinInfo2_head
    IOfflineFilesPinInfo2.IsPartlyPinned = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(8, 'IsPartlyPinned', ((1, 'pbPartlyPinned'),)))
    win32more.Storage.OfflineFiles.IOfflineFilesPinInfo
    return IOfflineFilesPinInfo2
def _define_IOfflineFilesProgress_head():
    class IOfflineFilesProgress(win32more.System.Com.IUnknown_head):
        Guid = Guid('fad63237-c55b-4911-98-50-bc-f9-6d-4c-97-9e')
    return IOfflineFilesProgress
def _define_IOfflineFilesProgress():
    IOfflineFilesProgress = win32more.Storage.OfflineFiles.IOfflineFilesProgress_head
    IOfflineFilesProgress.Begin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(3, 'Begin', ((1, 'pbAbort'),)))
    IOfflineFilesProgress.QueryAbort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(4, 'QueryAbort', ((1, 'pbAbort'),)))
    IOfflineFilesProgress.End = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT)(5, 'End', ((1, 'hrResult'),)))
    win32more.System.Com.IUnknown
    return IOfflineFilesProgress
def _define_IOfflineFilesServerItem_head():
    class IOfflineFilesServerItem(win32more.Storage.OfflineFiles.IOfflineFilesItem_head):
        Guid = Guid('9b1c9576-a92b-4151-8e-9e-7c-7b-3e-c2-e0-16')
    return IOfflineFilesServerItem
def _define_IOfflineFilesServerItem():
    IOfflineFilesServerItem = win32more.Storage.OfflineFiles.IOfflineFilesServerItem_head
    win32more.Storage.OfflineFiles.IOfflineFilesItem
    return IOfflineFilesServerItem
def _define_IOfflineFilesSetting_head():
    class IOfflineFilesSetting(win32more.System.Com.IUnknown_head):
        Guid = Guid('d871d3f7-f613-48a1-82-7e-7a-34-e5-60-ff-f6')
    return IOfflineFilesSetting
def _define_IOfflineFilesSetting():
    IOfflineFilesSetting = win32more.Storage.OfflineFiles.IOfflineFilesSetting_head
    IOfflineFilesSetting.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(3, 'GetName', ((1, 'ppszName'),)))
    IOfflineFilesSetting.GetValueType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.OfflineFiles.OFFLINEFILES_SETTING_VALUE_TYPE))(4, 'GetValueType', ((1, 'pType'),)))
    IOfflineFilesSetting.GetPreference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),UInt32)(5, 'GetPreference', ((1, 'pvarValue'),(1, 'dwScope'),)))
    IOfflineFilesSetting.GetPreferenceScope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(6, 'GetPreferenceScope', ((1, 'pdwScope'),)))
    IOfflineFilesSetting.SetPreference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),UInt32)(7, 'SetPreference', ((1, 'pvarValue'),(1, 'dwScope'),)))
    IOfflineFilesSetting.DeletePreference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(8, 'DeletePreference', ((1, 'dwScope'),)))
    IOfflineFilesSetting.GetPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),UInt32)(9, 'GetPolicy', ((1, 'pvarValue'),(1, 'dwScope'),)))
    IOfflineFilesSetting.GetPolicyScope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(10, 'GetPolicyScope', ((1, 'pdwScope'),)))
    IOfflineFilesSetting.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.Foundation.BOOL))(11, 'GetValue', ((1, 'pvarValue'),(1, 'pbSetByPolicy'),)))
    win32more.System.Com.IUnknown
    return IOfflineFilesSetting
def _define_IOfflineFilesShareInfo_head():
    class IOfflineFilesShareInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('7bcc43e7-31ce-4ca4-8c-cd-1c-ff-2d-c4-94-da')
    return IOfflineFilesShareInfo
def _define_IOfflineFilesShareInfo():
    IOfflineFilesShareInfo = win32more.Storage.OfflineFiles.IOfflineFilesShareInfo_head
    IOfflineFilesShareInfo.GetShareItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.OfflineFiles.IOfflineFilesShareItem_head))(3, 'GetShareItem', ((1, 'ppShareItem'),)))
    IOfflineFilesShareInfo.GetShareCachingMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.OfflineFiles.OFFLINEFILES_CACHING_MODE))(4, 'GetShareCachingMode', ((1, 'pCachingMode'),)))
    IOfflineFilesShareInfo.IsShareDfsJunction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(5, 'IsShareDfsJunction', ((1, 'pbIsDfsJunction'),)))
    win32more.System.Com.IUnknown
    return IOfflineFilesShareInfo
def _define_IOfflineFilesShareItem_head():
    class IOfflineFilesShareItem(win32more.Storage.OfflineFiles.IOfflineFilesItem_head):
        Guid = Guid('bab7e48d-4804-41b5-a4-4d-0f-19-9b-06-b1-45')
    return IOfflineFilesShareItem
def _define_IOfflineFilesShareItem():
    IOfflineFilesShareItem = win32more.Storage.OfflineFiles.IOfflineFilesShareItem_head
    win32more.Storage.OfflineFiles.IOfflineFilesItem
    return IOfflineFilesShareItem
def _define_IOfflineFilesSimpleProgress_head():
    class IOfflineFilesSimpleProgress(win32more.Storage.OfflineFiles.IOfflineFilesProgress_head):
        Guid = Guid('c34f7f9b-c43d-4f9d-a7-76-c0-eb-6d-e5-d4-01')
    return IOfflineFilesSimpleProgress
def _define_IOfflineFilesSimpleProgress():
    IOfflineFilesSimpleProgress = win32more.Storage.OfflineFiles.IOfflineFilesSimpleProgress_head
    IOfflineFilesSimpleProgress.ItemBegin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.OfflineFiles.OFFLINEFILES_OP_RESPONSE))(6, 'ItemBegin', ((1, 'pszFile'),(1, 'pResponse'),)))
    IOfflineFilesSimpleProgress.ItemResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.HRESULT,POINTER(win32more.Storage.OfflineFiles.OFFLINEFILES_OP_RESPONSE))(7, 'ItemResult', ((1, 'pszFile'),(1, 'hrResult'),(1, 'pResponse'),)))
    win32more.Storage.OfflineFiles.IOfflineFilesProgress
    return IOfflineFilesSimpleProgress
def _define_IOfflineFilesSuspend_head():
    class IOfflineFilesSuspend(win32more.System.Com.IUnknown_head):
        Guid = Guid('62c4560f-bc0b-48ca-ad-9d-34-cb-52-8d-99-a9')
    return IOfflineFilesSuspend
def _define_IOfflineFilesSuspend():
    IOfflineFilesSuspend = win32more.Storage.OfflineFiles.IOfflineFilesSuspend_head
    IOfflineFilesSuspend.SuspendRoot = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(3, 'SuspendRoot', ((1, 'bSuspend'),)))
    win32more.System.Com.IUnknown
    return IOfflineFilesSuspend
def _define_IOfflineFilesSuspendInfo_head():
    class IOfflineFilesSuspendInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('a457c25b-4e9c-4b04-85-af-89-32-cc-d9-78-89')
    return IOfflineFilesSuspendInfo
def _define_IOfflineFilesSuspendInfo():
    IOfflineFilesSuspendInfo = win32more.Storage.OfflineFiles.IOfflineFilesSuspendInfo_head
    IOfflineFilesSuspendInfo.IsSuspended = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Foundation.BOOL))(3, 'IsSuspended', ((1, 'pbSuspended'),(1, 'pbSuspendedRoot'),)))
    win32more.System.Com.IUnknown
    return IOfflineFilesSuspendInfo
def _define_IOfflineFilesSyncConflictHandler_head():
    class IOfflineFilesSyncConflictHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('b6dd5092-c65c-46b6-97-b8-fa-dd-08-e7-e1-be')
    return IOfflineFilesSyncConflictHandler
def _define_IOfflineFilesSyncConflictHandler():
    IOfflineFilesSyncConflictHandler = win32more.Storage.OfflineFiles.IOfflineFilesSyncConflictHandler_head
    IOfflineFilesSyncConflictHandler.ResolveConflict = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE,UInt32,POINTER(win32more.Storage.OfflineFiles.OFFLINEFILES_SYNC_CONFLICT_RESOLVE),POINTER(win32more.Foundation.PWSTR))(3, 'ResolveConflict', ((1, 'pszPath'),(1, 'fStateKnown'),(1, 'state'),(1, 'fChangeDetails'),(1, 'pConflictResolution'),(1, 'ppszNewName'),)))
    win32more.System.Com.IUnknown
    return IOfflineFilesSyncConflictHandler
def _define_IOfflineFilesSyncErrorInfo_head():
    class IOfflineFilesSyncErrorInfo(win32more.Storage.OfflineFiles.IOfflineFilesErrorInfo_head):
        Guid = Guid('59f95e46-eb54-49d1-be-76-de-95-45-8d-01-b0')
    return IOfflineFilesSyncErrorInfo
def _define_IOfflineFilesSyncErrorInfo():
    IOfflineFilesSyncErrorInfo = win32more.Storage.OfflineFiles.IOfflineFilesSyncErrorInfo_head
    IOfflineFilesSyncErrorInfo.GetSyncOperation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.OfflineFiles.OFFLINEFILES_SYNC_OPERATION))(5, 'GetSyncOperation', ((1, 'pSyncOp'),)))
    IOfflineFilesSyncErrorInfo.GetItemChangeFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(6, 'GetItemChangeFlags', ((1, 'pdwItemChangeFlags'),)))
    IOfflineFilesSyncErrorInfo.InfoEnumerated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Foundation.BOOL),POINTER(win32more.Foundation.BOOL))(7, 'InfoEnumerated', ((1, 'pbLocalEnumerated'),(1, 'pbRemoteEnumerated'),(1, 'pbOriginalEnumerated'),)))
    IOfflineFilesSyncErrorInfo.InfoAvailable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Foundation.BOOL),POINTER(win32more.Foundation.BOOL))(8, 'InfoAvailable', ((1, 'pbLocalInfo'),(1, 'pbRemoteInfo'),(1, 'pbOriginalInfo'),)))
    IOfflineFilesSyncErrorInfo.GetLocalInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.OfflineFiles.IOfflineFilesSyncErrorItemInfo_head))(9, 'GetLocalInfo', ((1, 'ppInfo'),)))
    IOfflineFilesSyncErrorInfo.GetRemoteInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.OfflineFiles.IOfflineFilesSyncErrorItemInfo_head))(10, 'GetRemoteInfo', ((1, 'ppInfo'),)))
    IOfflineFilesSyncErrorInfo.GetOriginalInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.OfflineFiles.IOfflineFilesSyncErrorItemInfo_head))(11, 'GetOriginalInfo', ((1, 'ppInfo'),)))
    win32more.Storage.OfflineFiles.IOfflineFilesErrorInfo
    return IOfflineFilesSyncErrorInfo
def _define_IOfflineFilesSyncErrorItemInfo_head():
    class IOfflineFilesSyncErrorItemInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('ecdbaf0d-6a18-4d55-80-17-10-8f-76-60-ba-44')
    return IOfflineFilesSyncErrorItemInfo
def _define_IOfflineFilesSyncErrorItemInfo():
    IOfflineFilesSyncErrorItemInfo = win32more.Storage.OfflineFiles.IOfflineFilesSyncErrorItemInfo_head
    IOfflineFilesSyncErrorItemInfo.GetFileAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetFileAttributes', ((1, 'pdwAttributes'),)))
    IOfflineFilesSyncErrorItemInfo.GetFileTimes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head))(4, 'GetFileTimes', ((1, 'pftLastWrite'),(1, 'pftChange'),)))
    IOfflineFilesSyncErrorItemInfo.GetFileSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.LARGE_INTEGER_head))(5, 'GetFileSize', ((1, 'pSize'),)))
    win32more.System.Com.IUnknown
    return IOfflineFilesSyncErrorItemInfo
def _define_IOfflineFilesSyncProgress_head():
    class IOfflineFilesSyncProgress(win32more.Storage.OfflineFiles.IOfflineFilesProgress_head):
        Guid = Guid('6931f49a-6fc7-4c1b-b2-65-56-79-3f-c4-51-b7')
    return IOfflineFilesSyncProgress
def _define_IOfflineFilesSyncProgress():
    IOfflineFilesSyncProgress = win32more.Storage.OfflineFiles.IOfflineFilesSyncProgress_head
    IOfflineFilesSyncProgress.SyncItemBegin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.OfflineFiles.OFFLINEFILES_OP_RESPONSE))(6, 'SyncItemBegin', ((1, 'pszFile'),(1, 'pResponse'),)))
    IOfflineFilesSyncProgress.SyncItemResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.HRESULT,win32more.Storage.OfflineFiles.IOfflineFilesSyncErrorInfo_head,POINTER(win32more.Storage.OfflineFiles.OFFLINEFILES_OP_RESPONSE))(7, 'SyncItemResult', ((1, 'pszFile'),(1, 'hrResult'),(1, 'pErrorInfo'),(1, 'pResponse'),)))
    win32more.Storage.OfflineFiles.IOfflineFilesProgress
    return IOfflineFilesSyncProgress
def _define_IOfflineFilesTransparentCacheInfo_head():
    class IOfflineFilesTransparentCacheInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('bcaf4a01-5b68-4b56-a6-a1-8d-27-86-ed-e8-e3')
    return IOfflineFilesTransparentCacheInfo
def _define_IOfflineFilesTransparentCacheInfo():
    IOfflineFilesTransparentCacheInfo = win32more.Storage.OfflineFiles.IOfflineFilesTransparentCacheInfo_head
    IOfflineFilesTransparentCacheInfo.IsTransparentlyCached = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(3, 'IsTransparentlyCached', ((1, 'pbTransparentlyCached'),)))
    win32more.System.Com.IUnknown
    return IOfflineFilesTransparentCacheInfo
OFFLINEFILES_CACHING_MODE = Int32
OFFLINEFILES_CACHING_MODE_NONE = 0
OFFLINEFILES_CACHING_MODE_NOCACHING = 1
OFFLINEFILES_CACHING_MODE_MANUAL = 2
OFFLINEFILES_CACHING_MODE_AUTO_DOC = 3
OFFLINEFILES_CACHING_MODE_AUTO_PROGANDDOC = 4
OFFLINEFILES_COMPARE = Int32
OFFLINEFILES_COMPARE_EQ = 0
OFFLINEFILES_COMPARE_NEQ = 1
OFFLINEFILES_COMPARE_LT = 2
OFFLINEFILES_COMPARE_GT = 3
OFFLINEFILES_COMPARE_LTE = 4
OFFLINEFILES_COMPARE_GTE = 5
OFFLINEFILES_CONNECT_STATE = Int32
OFFLINEFILES_CONNECT_STATE_UNKNOWN = 0
OFFLINEFILES_CONNECT_STATE_OFFLINE = 1
OFFLINEFILES_CONNECT_STATE_ONLINE = 2
OFFLINEFILES_CONNECT_STATE_TRANSPARENTLY_CACHED = 3
OFFLINEFILES_CONNECT_STATE_PARTLY_TRANSPARENTLY_CACHED = 4
OFFLINEFILES_EVENTS = Int32
OFFLINEFILES_EVENT_CACHEMOVED = 0
OFFLINEFILES_EVENT_CACHEISFULL = 1
OFFLINEFILES_EVENT_CACHEISCORRUPTED = 2
OFFLINEFILES_EVENT_ENABLED = 3
OFFLINEFILES_EVENT_ENCRYPTIONCHANGED = 4
OFFLINEFILES_EVENT_SYNCBEGIN = 5
OFFLINEFILES_EVENT_SYNCFILERESULT = 6
OFFLINEFILES_EVENT_SYNCCONFLICTRECADDED = 7
OFFLINEFILES_EVENT_SYNCCONFLICTRECUPDATED = 8
OFFLINEFILES_EVENT_SYNCCONFLICTRECREMOVED = 9
OFFLINEFILES_EVENT_SYNCEND = 10
OFFLINEFILES_EVENT_BACKGROUNDSYNCBEGIN = 11
OFFLINEFILES_EVENT_BACKGROUNDSYNCEND = 12
OFFLINEFILES_EVENT_NETTRANSPORTARRIVED = 13
OFFLINEFILES_EVENT_NONETTRANSPORTS = 14
OFFLINEFILES_EVENT_ITEMDISCONNECTED = 15
OFFLINEFILES_EVENT_ITEMRECONNECTED = 16
OFFLINEFILES_EVENT_ITEMAVAILABLEOFFLINE = 17
OFFLINEFILES_EVENT_ITEMNOTAVAILABLEOFFLINE = 18
OFFLINEFILES_EVENT_ITEMPINNED = 19
OFFLINEFILES_EVENT_ITEMNOTPINNED = 20
OFFLINEFILES_EVENT_ITEMMODIFIED = 21
OFFLINEFILES_EVENT_ITEMADDEDTOCACHE = 22
OFFLINEFILES_EVENT_ITEMDELETEDFROMCACHE = 23
OFFLINEFILES_EVENT_ITEMRENAMED = 24
OFFLINEFILES_EVENT_DATALOST = 25
OFFLINEFILES_EVENT_PING = 26
OFFLINEFILES_EVENT_ITEMRECONNECTBEGIN = 27
OFFLINEFILES_EVENT_ITEMRECONNECTEND = 28
OFFLINEFILES_EVENT_CACHEEVICTBEGIN = 29
OFFLINEFILES_EVENT_CACHEEVICTEND = 30
OFFLINEFILES_EVENT_POLICYCHANGEDETECTED = 31
OFFLINEFILES_EVENT_PREFERENCECHANGEDETECTED = 32
OFFLINEFILES_EVENT_SETTINGSCHANGESAPPLIED = 33
OFFLINEFILES_EVENT_TRANSPARENTCACHEITEMNOTIFY = 34
OFFLINEFILES_EVENT_PREFETCHFILEBEGIN = 35
OFFLINEFILES_EVENT_PREFETCHFILEEND = 36
OFFLINEFILES_EVENT_PREFETCHCLOSEHANDLEBEGIN = 37
OFFLINEFILES_EVENT_PREFETCHCLOSEHANDLEEND = 38
OFFLINEFILES_NUM_EVENTS = 39
OFFLINEFILES_ITEM_COPY = Int32
OFFLINEFILES_ITEM_COPY_LOCAL = 0
OFFLINEFILES_ITEM_COPY_REMOTE = 1
OFFLINEFILES_ITEM_COPY_ORIGINAL = 2
OFFLINEFILES_ITEM_TIME = Int32
OFFLINEFILES_ITEM_TIME_CREATION = 0
OFFLINEFILES_ITEM_TIME_LASTACCESS = 1
OFFLINEFILES_ITEM_TIME_LASTWRITE = 2
OFFLINEFILES_ITEM_TYPE = Int32
OFFLINEFILES_ITEM_TYPE_FILE = 0
OFFLINEFILES_ITEM_TYPE_DIRECTORY = 1
OFFLINEFILES_ITEM_TYPE_SHARE = 2
OFFLINEFILES_ITEM_TYPE_SERVER = 3
OFFLINEFILES_OFFLINE_REASON = Int32
OFFLINEFILES_OFFLINE_REASON_UNKNOWN = 0
OFFLINEFILES_OFFLINE_REASON_NOT_APPLICABLE = 1
OFFLINEFILES_OFFLINE_REASON_CONNECTION_FORCED = 2
OFFLINEFILES_OFFLINE_REASON_CONNECTION_SLOW = 3
OFFLINEFILES_OFFLINE_REASON_CONNECTION_ERROR = 4
OFFLINEFILES_OFFLINE_REASON_ITEM_VERSION_CONFLICT = 5
OFFLINEFILES_OFFLINE_REASON_ITEM_SUSPENDED = 6
OFFLINEFILES_OP_RESPONSE = Int32
OFFLINEFILES_OP_CONTINUE = 0
OFFLINEFILES_OP_RETRY = 1
OFFLINEFILES_OP_ABORT = 2
OFFLINEFILES_PATHFILTER_MATCH = Int32
OFFLINEFILES_PATHFILTER_SELF = 0
OFFLINEFILES_PATHFILTER_CHILD = 1
OFFLINEFILES_PATHFILTER_DESCENDENT = 2
OFFLINEFILES_PATHFILTER_SELFORCHILD = 3
OFFLINEFILES_PATHFILTER_SELFORDESCENDENT = 4
OFFLINEFILES_SETTING_VALUE_TYPE = Int32
OFFLINEFILES_SETTING_VALUE_UI4 = 0
OFFLINEFILES_SETTING_VALUE_BSTR = 1
OFFLINEFILES_SETTING_VALUE_BSTR_DBLNULTERM = 2
OFFLINEFILES_SETTING_VALUE_2DIM_ARRAY_BSTR_UI4 = 3
OFFLINEFILES_SETTING_VALUE_2DIM_ARRAY_BSTR_BSTR = 4
OFFLINEFILES_SYNC_CONFLICT_RESOLVE = Int32
OFFLINEFILES_SYNC_CONFLICT_RESOLVE_NONE = 0
OFFLINEFILES_SYNC_CONFLICT_RESOLVE_KEEPLOCAL = 1
OFFLINEFILES_SYNC_CONFLICT_RESOLVE_KEEPREMOTE = 2
OFFLINEFILES_SYNC_CONFLICT_RESOLVE_KEEPALLCHANGES = 3
OFFLINEFILES_SYNC_CONFLICT_RESOLVE_KEEPLATEST = 4
OFFLINEFILES_SYNC_CONFLICT_RESOLVE_LOG = 5
OFFLINEFILES_SYNC_CONFLICT_RESOLVE_SKIP = 6
OFFLINEFILES_SYNC_CONFLICT_ABORT = 7
OFFLINEFILES_SYNC_CONFLICT_RESOLVE_NUMCODES = 8
OFFLINEFILES_SYNC_OPERATION = Int32
OFFLINEFILES_SYNC_OPERATION_CREATE_COPY_ON_SERVER = 0
OFFLINEFILES_SYNC_OPERATION_CREATE_COPY_ON_CLIENT = 1
OFFLINEFILES_SYNC_OPERATION_SYNC_TO_SERVER = 2
OFFLINEFILES_SYNC_OPERATION_SYNC_TO_CLIENT = 3
OFFLINEFILES_SYNC_OPERATION_DELETE_SERVER_COPY = 4
OFFLINEFILES_SYNC_OPERATION_DELETE_CLIENT_COPY = 5
OFFLINEFILES_SYNC_OPERATION_PIN = 6
OFFLINEFILES_SYNC_OPERATION_PREPARE = 7
OFFLINEFILES_SYNC_STATE = Int32
OFFLINEFILES_SYNC_STATE_Stable = 0
OFFLINEFILES_SYNC_STATE_FileOnClient_DirOnServer = 1
OFFLINEFILES_SYNC_STATE_FileOnClient_NoServerCopy = 2
OFFLINEFILES_SYNC_STATE_DirOnClient_FileOnServer = 3
OFFLINEFILES_SYNC_STATE_DirOnClient_FileChangedOnServer = 4
OFFLINEFILES_SYNC_STATE_DirOnClient_NoServerCopy = 5
OFFLINEFILES_SYNC_STATE_FileCreatedOnClient_NoServerCopy = 6
OFFLINEFILES_SYNC_STATE_FileCreatedOnClient_FileChangedOnServer = 7
OFFLINEFILES_SYNC_STATE_FileCreatedOnClient_DirChangedOnServer = 8
OFFLINEFILES_SYNC_STATE_FileCreatedOnClient_FileOnServer = 9
OFFLINEFILES_SYNC_STATE_FileCreatedOnClient_DirOnServer = 10
OFFLINEFILES_SYNC_STATE_FileCreatedOnClient_DeletedOnServer = 11
OFFLINEFILES_SYNC_STATE_FileChangedOnClient_ChangedOnServer = 12
OFFLINEFILES_SYNC_STATE_FileChangedOnClient_DirOnServer = 13
OFFLINEFILES_SYNC_STATE_FileChangedOnClient_DirChangedOnServer = 14
OFFLINEFILES_SYNC_STATE_FileChangedOnClient_DeletedOnServer = 15
OFFLINEFILES_SYNC_STATE_FileSparseOnClient_ChangedOnServer = 16
OFFLINEFILES_SYNC_STATE_FileSparseOnClient_DeletedOnServer = 17
OFFLINEFILES_SYNC_STATE_FileSparseOnClient_DirOnServer = 18
OFFLINEFILES_SYNC_STATE_FileSparseOnClient_DirChangedOnServer = 19
OFFLINEFILES_SYNC_STATE_DirCreatedOnClient_NoServerCopy = 20
OFFLINEFILES_SYNC_STATE_DirCreatedOnClient_DirOnServer = 21
OFFLINEFILES_SYNC_STATE_DirCreatedOnClient_FileOnServer = 22
OFFLINEFILES_SYNC_STATE_DirCreatedOnClient_FileChangedOnServer = 23
OFFLINEFILES_SYNC_STATE_DirCreatedOnClient_DirChangedOnServer = 24
OFFLINEFILES_SYNC_STATE_DirCreatedOnClient_DeletedOnServer = 25
OFFLINEFILES_SYNC_STATE_DirChangedOnClient_FileOnServer = 26
OFFLINEFILES_SYNC_STATE_DirChangedOnClient_FileChangedOnServer = 27
OFFLINEFILES_SYNC_STATE_DirChangedOnClient_ChangedOnServer = 28
OFFLINEFILES_SYNC_STATE_DirChangedOnClient_DeletedOnServer = 29
OFFLINEFILES_SYNC_STATE_NoClientCopy_FileOnServer = 30
OFFLINEFILES_SYNC_STATE_NoClientCopy_DirOnServer = 31
OFFLINEFILES_SYNC_STATE_NoClientCopy_FileChangedOnServer = 32
OFFLINEFILES_SYNC_STATE_NoClientCopy_DirChangedOnServer = 33
OFFLINEFILES_SYNC_STATE_DeletedOnClient_FileOnServer = 34
OFFLINEFILES_SYNC_STATE_DeletedOnClient_DirOnServer = 35
OFFLINEFILES_SYNC_STATE_DeletedOnClient_FileChangedOnServer = 36
OFFLINEFILES_SYNC_STATE_DeletedOnClient_DirChangedOnServer = 37
OFFLINEFILES_SYNC_STATE_FileSparseOnClient = 38
OFFLINEFILES_SYNC_STATE_FileChangedOnClient = 39
OFFLINEFILES_SYNC_STATE_FileRenamedOnClient = 40
OFFLINEFILES_SYNC_STATE_DirSparseOnClient = 41
OFFLINEFILES_SYNC_STATE_DirChangedOnClient = 42
OFFLINEFILES_SYNC_STATE_DirRenamedOnClient = 43
OFFLINEFILES_SYNC_STATE_FileChangedOnServer = 44
OFFLINEFILES_SYNC_STATE_FileRenamedOnServer = 45
OFFLINEFILES_SYNC_STATE_FileDeletedOnServer = 46
OFFLINEFILES_SYNC_STATE_DirChangedOnServer = 47
OFFLINEFILES_SYNC_STATE_DirRenamedOnServer = 48
OFFLINEFILES_SYNC_STATE_DirDeletedOnServer = 49
OFFLINEFILES_SYNC_STATE_FileReplacedAndDeletedOnClient_FileOnServer = 50
OFFLINEFILES_SYNC_STATE_FileReplacedAndDeletedOnClient_FileChangedOnServer = 51
OFFLINEFILES_SYNC_STATE_FileReplacedAndDeletedOnClient_DirOnServer = 52
OFFLINEFILES_SYNC_STATE_FileReplacedAndDeletedOnClient_DirChangedOnServer = 53
OFFLINEFILES_SYNC_STATE_NUMSTATES = 54
OfflineFilesCache = Guid('48c6be7c-3871-43cc-b4-6f-14-49-a1-bb-2f-f3')
OfflineFilesSetting = Guid('fd3659e9-a920-4123-ad-64-7f-c7-6c-7a-ac-df')
__all__ = [
    "IEnumOfflineFilesItems",
    "IEnumOfflineFilesSettings",
    "IOfflineFilesCache",
    "IOfflineFilesCache2",
    "IOfflineFilesChangeInfo",
    "IOfflineFilesConnectionInfo",
    "IOfflineFilesDirectoryItem",
    "IOfflineFilesDirtyInfo",
    "IOfflineFilesErrorInfo",
    "IOfflineFilesEvents",
    "IOfflineFilesEvents2",
    "IOfflineFilesEvents3",
    "IOfflineFilesEvents4",
    "IOfflineFilesEventsFilter",
    "IOfflineFilesFileItem",
    "IOfflineFilesFileSysInfo",
    "IOfflineFilesGhostInfo",
    "IOfflineFilesItem",
    "IOfflineFilesItemContainer",
    "IOfflineFilesItemFilter",
    "IOfflineFilesPinInfo",
    "IOfflineFilesPinInfo2",
    "IOfflineFilesProgress",
    "IOfflineFilesServerItem",
    "IOfflineFilesSetting",
    "IOfflineFilesShareInfo",
    "IOfflineFilesShareItem",
    "IOfflineFilesSimpleProgress",
    "IOfflineFilesSuspend",
    "IOfflineFilesSuspendInfo",
    "IOfflineFilesSyncConflictHandler",
    "IOfflineFilesSyncErrorInfo",
    "IOfflineFilesSyncErrorItemInfo",
    "IOfflineFilesSyncProgress",
    "IOfflineFilesTransparentCacheInfo",
    "OFFLINEFILES_CACHING_MODE",
    "OFFLINEFILES_CACHING_MODE_AUTO_DOC",
    "OFFLINEFILES_CACHING_MODE_AUTO_PROGANDDOC",
    "OFFLINEFILES_CACHING_MODE_MANUAL",
    "OFFLINEFILES_CACHING_MODE_NOCACHING",
    "OFFLINEFILES_CACHING_MODE_NONE",
    "OFFLINEFILES_CHANGES_LOCAL_ATTRIBUTES",
    "OFFLINEFILES_CHANGES_LOCAL_SIZE",
    "OFFLINEFILES_CHANGES_LOCAL_TIME",
    "OFFLINEFILES_CHANGES_NONE",
    "OFFLINEFILES_CHANGES_REMOTE_ATTRIBUTES",
    "OFFLINEFILES_CHANGES_REMOTE_SIZE",
    "OFFLINEFILES_CHANGES_REMOTE_TIME",
    "OFFLINEFILES_COMPARE",
    "OFFLINEFILES_COMPARE_EQ",
    "OFFLINEFILES_COMPARE_GT",
    "OFFLINEFILES_COMPARE_GTE",
    "OFFLINEFILES_COMPARE_LT",
    "OFFLINEFILES_COMPARE_LTE",
    "OFFLINEFILES_COMPARE_NEQ",
    "OFFLINEFILES_CONNECT_STATE",
    "OFFLINEFILES_CONNECT_STATE_OFFLINE",
    "OFFLINEFILES_CONNECT_STATE_ONLINE",
    "OFFLINEFILES_CONNECT_STATE_PARTLY_TRANSPARENTLY_CACHED",
    "OFFLINEFILES_CONNECT_STATE_TRANSPARENTLY_CACHED",
    "OFFLINEFILES_CONNECT_STATE_UNKNOWN",
    "OFFLINEFILES_DELETE_FLAG_ADMIN",
    "OFFLINEFILES_DELETE_FLAG_DELMODIFIED",
    "OFFLINEFILES_DELETE_FLAG_NOAUTOCACHED",
    "OFFLINEFILES_DELETE_FLAG_NOPINNED",
    "OFFLINEFILES_ENCRYPTION_CONTROL_FLAG_ASYNCPROGRESS",
    "OFFLINEFILES_ENCRYPTION_CONTROL_FLAG_BACKGROUND",
    "OFFLINEFILES_ENCRYPTION_CONTROL_FLAG_CONSOLE",
    "OFFLINEFILES_ENCRYPTION_CONTROL_FLAG_INTERACTIVE",
    "OFFLINEFILES_ENCRYPTION_CONTROL_FLAG_LOWPRIORITY",
    "OFFLINEFILES_ENUM_FLAT",
    "OFFLINEFILES_ENUM_FLAT_FILESONLY",
    "OFFLINEFILES_EVENTS",
    "OFFLINEFILES_EVENT_BACKGROUNDSYNCBEGIN",
    "OFFLINEFILES_EVENT_BACKGROUNDSYNCEND",
    "OFFLINEFILES_EVENT_CACHEEVICTBEGIN",
    "OFFLINEFILES_EVENT_CACHEEVICTEND",
    "OFFLINEFILES_EVENT_CACHEISCORRUPTED",
    "OFFLINEFILES_EVENT_CACHEISFULL",
    "OFFLINEFILES_EVENT_CACHEMOVED",
    "OFFLINEFILES_EVENT_DATALOST",
    "OFFLINEFILES_EVENT_ENABLED",
    "OFFLINEFILES_EVENT_ENCRYPTIONCHANGED",
    "OFFLINEFILES_EVENT_ITEMADDEDTOCACHE",
    "OFFLINEFILES_EVENT_ITEMAVAILABLEOFFLINE",
    "OFFLINEFILES_EVENT_ITEMDELETEDFROMCACHE",
    "OFFLINEFILES_EVENT_ITEMDISCONNECTED",
    "OFFLINEFILES_EVENT_ITEMMODIFIED",
    "OFFLINEFILES_EVENT_ITEMNOTAVAILABLEOFFLINE",
    "OFFLINEFILES_EVENT_ITEMNOTPINNED",
    "OFFLINEFILES_EVENT_ITEMPINNED",
    "OFFLINEFILES_EVENT_ITEMRECONNECTBEGIN",
    "OFFLINEFILES_EVENT_ITEMRECONNECTED",
    "OFFLINEFILES_EVENT_ITEMRECONNECTEND",
    "OFFLINEFILES_EVENT_ITEMRENAMED",
    "OFFLINEFILES_EVENT_NETTRANSPORTARRIVED",
    "OFFLINEFILES_EVENT_NONETTRANSPORTS",
    "OFFLINEFILES_EVENT_PING",
    "OFFLINEFILES_EVENT_POLICYCHANGEDETECTED",
    "OFFLINEFILES_EVENT_PREFERENCECHANGEDETECTED",
    "OFFLINEFILES_EVENT_PREFETCHCLOSEHANDLEBEGIN",
    "OFFLINEFILES_EVENT_PREFETCHCLOSEHANDLEEND",
    "OFFLINEFILES_EVENT_PREFETCHFILEBEGIN",
    "OFFLINEFILES_EVENT_PREFETCHFILEEND",
    "OFFLINEFILES_EVENT_SETTINGSCHANGESAPPLIED",
    "OFFLINEFILES_EVENT_SYNCBEGIN",
    "OFFLINEFILES_EVENT_SYNCCONFLICTRECADDED",
    "OFFLINEFILES_EVENT_SYNCCONFLICTRECREMOVED",
    "OFFLINEFILES_EVENT_SYNCCONFLICTRECUPDATED",
    "OFFLINEFILES_EVENT_SYNCEND",
    "OFFLINEFILES_EVENT_SYNCFILERESULT",
    "OFFLINEFILES_EVENT_TRANSPARENTCACHEITEMNOTIFY",
    "OFFLINEFILES_ITEM_COPY",
    "OFFLINEFILES_ITEM_COPY_LOCAL",
    "OFFLINEFILES_ITEM_COPY_ORIGINAL",
    "OFFLINEFILES_ITEM_COPY_REMOTE",
    "OFFLINEFILES_ITEM_FILTER_FLAG_CREATED",
    "OFFLINEFILES_ITEM_FILTER_FLAG_DELETED",
    "OFFLINEFILES_ITEM_FILTER_FLAG_DIRECTORY",
    "OFFLINEFILES_ITEM_FILTER_FLAG_DIRTY",
    "OFFLINEFILES_ITEM_FILTER_FLAG_FILE",
    "OFFLINEFILES_ITEM_FILTER_FLAG_GHOST",
    "OFFLINEFILES_ITEM_FILTER_FLAG_GUEST_ANYACCESS",
    "OFFLINEFILES_ITEM_FILTER_FLAG_GUEST_READ",
    "OFFLINEFILES_ITEM_FILTER_FLAG_GUEST_WRITE",
    "OFFLINEFILES_ITEM_FILTER_FLAG_MODIFIED",
    "OFFLINEFILES_ITEM_FILTER_FLAG_MODIFIED_ATTRIBUTES",
    "OFFLINEFILES_ITEM_FILTER_FLAG_MODIFIED_DATA",
    "OFFLINEFILES_ITEM_FILTER_FLAG_OFFLINE",
    "OFFLINEFILES_ITEM_FILTER_FLAG_ONLINE",
    "OFFLINEFILES_ITEM_FILTER_FLAG_OTHER_ANYACCESS",
    "OFFLINEFILES_ITEM_FILTER_FLAG_OTHER_READ",
    "OFFLINEFILES_ITEM_FILTER_FLAG_OTHER_WRITE",
    "OFFLINEFILES_ITEM_FILTER_FLAG_PINNED",
    "OFFLINEFILES_ITEM_FILTER_FLAG_PINNED_COMPUTER",
    "OFFLINEFILES_ITEM_FILTER_FLAG_PINNED_OTHERS",
    "OFFLINEFILES_ITEM_FILTER_FLAG_PINNED_USER",
    "OFFLINEFILES_ITEM_FILTER_FLAG_SPARSE",
    "OFFLINEFILES_ITEM_FILTER_FLAG_SUSPENDED",
    "OFFLINEFILES_ITEM_FILTER_FLAG_USER_ANYACCESS",
    "OFFLINEFILES_ITEM_FILTER_FLAG_USER_READ",
    "OFFLINEFILES_ITEM_FILTER_FLAG_USER_WRITE",
    "OFFLINEFILES_ITEM_QUERY_ADMIN",
    "OFFLINEFILES_ITEM_QUERY_ATTEMPT_TRANSITIONONLINE",
    "OFFLINEFILES_ITEM_QUERY_CONNECTIONSTATE",
    "OFFLINEFILES_ITEM_QUERY_INCLUDETRANSPARENTCACHE",
    "OFFLINEFILES_ITEM_QUERY_LOCALDIRTYBYTECOUNT",
    "OFFLINEFILES_ITEM_QUERY_REMOTEDIRTYBYTECOUNT",
    "OFFLINEFILES_ITEM_QUERY_REMOTEINFO",
    "OFFLINEFILES_ITEM_TIME",
    "OFFLINEFILES_ITEM_TIME_CREATION",
    "OFFLINEFILES_ITEM_TIME_LASTACCESS",
    "OFFLINEFILES_ITEM_TIME_LASTWRITE",
    "OFFLINEFILES_ITEM_TYPE",
    "OFFLINEFILES_ITEM_TYPE_DIRECTORY",
    "OFFLINEFILES_ITEM_TYPE_FILE",
    "OFFLINEFILES_ITEM_TYPE_SERVER",
    "OFFLINEFILES_ITEM_TYPE_SHARE",
    "OFFLINEFILES_NUM_EVENTS",
    "OFFLINEFILES_OFFLINE_REASON",
    "OFFLINEFILES_OFFLINE_REASON_CONNECTION_ERROR",
    "OFFLINEFILES_OFFLINE_REASON_CONNECTION_FORCED",
    "OFFLINEFILES_OFFLINE_REASON_CONNECTION_SLOW",
    "OFFLINEFILES_OFFLINE_REASON_ITEM_SUSPENDED",
    "OFFLINEFILES_OFFLINE_REASON_ITEM_VERSION_CONFLICT",
    "OFFLINEFILES_OFFLINE_REASON_NOT_APPLICABLE",
    "OFFLINEFILES_OFFLINE_REASON_UNKNOWN",
    "OFFLINEFILES_OP_ABORT",
    "OFFLINEFILES_OP_CONTINUE",
    "OFFLINEFILES_OP_RESPONSE",
    "OFFLINEFILES_OP_RETRY",
    "OFFLINEFILES_PATHFILTER_CHILD",
    "OFFLINEFILES_PATHFILTER_DESCENDENT",
    "OFFLINEFILES_PATHFILTER_MATCH",
    "OFFLINEFILES_PATHFILTER_SELF",
    "OFFLINEFILES_PATHFILTER_SELFORCHILD",
    "OFFLINEFILES_PATHFILTER_SELFORDESCENDENT",
    "OFFLINEFILES_PINLINKTARGETS_ALWAYS",
    "OFFLINEFILES_PINLINKTARGETS_EXPLICIT",
    "OFFLINEFILES_PINLINKTARGETS_NEVER",
    "OFFLINEFILES_PIN_CONTROL_FLAG_ASYNCPROGRESS",
    "OFFLINEFILES_PIN_CONTROL_FLAG_BACKGROUND",
    "OFFLINEFILES_PIN_CONTROL_FLAG_CONSOLE",
    "OFFLINEFILES_PIN_CONTROL_FLAG_FILL",
    "OFFLINEFILES_PIN_CONTROL_FLAG_FORALL",
    "OFFLINEFILES_PIN_CONTROL_FLAG_FORREDIR",
    "OFFLINEFILES_PIN_CONTROL_FLAG_FORUSER",
    "OFFLINEFILES_PIN_CONTROL_FLAG_FORUSER_POLICY",
    "OFFLINEFILES_PIN_CONTROL_FLAG_INTERACTIVE",
    "OFFLINEFILES_PIN_CONTROL_FLAG_LOWPRIORITY",
    "OFFLINEFILES_PIN_CONTROL_FLAG_PINLINKTARGETS",
    "OFFLINEFILES_SETTING_PinLinkTargets",
    "OFFLINEFILES_SETTING_SCOPE_COMPUTER",
    "OFFLINEFILES_SETTING_SCOPE_USER",
    "OFFLINEFILES_SETTING_VALUE_2DIM_ARRAY_BSTR_BSTR",
    "OFFLINEFILES_SETTING_VALUE_2DIM_ARRAY_BSTR_UI4",
    "OFFLINEFILES_SETTING_VALUE_BSTR",
    "OFFLINEFILES_SETTING_VALUE_BSTR_DBLNULTERM",
    "OFFLINEFILES_SETTING_VALUE_TYPE",
    "OFFLINEFILES_SETTING_VALUE_UI4",
    "OFFLINEFILES_SYNC_CONFLICT_ABORT",
    "OFFLINEFILES_SYNC_CONFLICT_RESOLVE",
    "OFFLINEFILES_SYNC_CONFLICT_RESOLVE_KEEPALLCHANGES",
    "OFFLINEFILES_SYNC_CONFLICT_RESOLVE_KEEPLATEST",
    "OFFLINEFILES_SYNC_CONFLICT_RESOLVE_KEEPLOCAL",
    "OFFLINEFILES_SYNC_CONFLICT_RESOLVE_KEEPREMOTE",
    "OFFLINEFILES_SYNC_CONFLICT_RESOLVE_LOG",
    "OFFLINEFILES_SYNC_CONFLICT_RESOLVE_NONE",
    "OFFLINEFILES_SYNC_CONFLICT_RESOLVE_NUMCODES",
    "OFFLINEFILES_SYNC_CONFLICT_RESOLVE_SKIP",
    "OFFLINEFILES_SYNC_CONTROL_CR_DEFAULT",
    "OFFLINEFILES_SYNC_CONTROL_CR_KEEPLATEST",
    "OFFLINEFILES_SYNC_CONTROL_CR_KEEPLOCAL",
    "OFFLINEFILES_SYNC_CONTROL_CR_KEEPREMOTE",
    "OFFLINEFILES_SYNC_CONTROL_CR_MASK",
    "OFFLINEFILES_SYNC_CONTROL_FLAG_ASYNCPROGRESS",
    "OFFLINEFILES_SYNC_CONTROL_FLAG_BACKGROUND",
    "OFFLINEFILES_SYNC_CONTROL_FLAG_CONSOLE",
    "OFFLINEFILES_SYNC_CONTROL_FLAG_FILLSPARSE",
    "OFFLINEFILES_SYNC_CONTROL_FLAG_INTERACTIVE",
    "OFFLINEFILES_SYNC_CONTROL_FLAG_LOWPRIORITY",
    "OFFLINEFILES_SYNC_CONTROL_FLAG_NONEWFILESOUT",
    "OFFLINEFILES_SYNC_CONTROL_FLAG_PINFORALL",
    "OFFLINEFILES_SYNC_CONTROL_FLAG_PINFORREDIR",
    "OFFLINEFILES_SYNC_CONTROL_FLAG_PINFORUSER",
    "OFFLINEFILES_SYNC_CONTROL_FLAG_PINFORUSER_POLICY",
    "OFFLINEFILES_SYNC_CONTROL_FLAG_PINLINKTARGETS",
    "OFFLINEFILES_SYNC_CONTROL_FLAG_PINNEWFILES",
    "OFFLINEFILES_SYNC_CONTROL_FLAG_SKIPSUSPENDEDDIRS",
    "OFFLINEFILES_SYNC_CONTROL_FLAG_SYNCIN",
    "OFFLINEFILES_SYNC_CONTROL_FLAG_SYNCOUT",
    "OFFLINEFILES_SYNC_ITEM_CHANGE_ATTRIBUTES",
    "OFFLINEFILES_SYNC_ITEM_CHANGE_CHANGETIME",
    "OFFLINEFILES_SYNC_ITEM_CHANGE_FILESIZE",
    "OFFLINEFILES_SYNC_ITEM_CHANGE_NONE",
    "OFFLINEFILES_SYNC_ITEM_CHANGE_WRITETIME",
    "OFFLINEFILES_SYNC_OPERATION",
    "OFFLINEFILES_SYNC_OPERATION_CREATE_COPY_ON_CLIENT",
    "OFFLINEFILES_SYNC_OPERATION_CREATE_COPY_ON_SERVER",
    "OFFLINEFILES_SYNC_OPERATION_DELETE_CLIENT_COPY",
    "OFFLINEFILES_SYNC_OPERATION_DELETE_SERVER_COPY",
    "OFFLINEFILES_SYNC_OPERATION_PIN",
    "OFFLINEFILES_SYNC_OPERATION_PREPARE",
    "OFFLINEFILES_SYNC_OPERATION_SYNC_TO_CLIENT",
    "OFFLINEFILES_SYNC_OPERATION_SYNC_TO_SERVER",
    "OFFLINEFILES_SYNC_STATE",
    "OFFLINEFILES_SYNC_STATE_DeletedOnClient_DirChangedOnServer",
    "OFFLINEFILES_SYNC_STATE_DeletedOnClient_DirOnServer",
    "OFFLINEFILES_SYNC_STATE_DeletedOnClient_FileChangedOnServer",
    "OFFLINEFILES_SYNC_STATE_DeletedOnClient_FileOnServer",
    "OFFLINEFILES_SYNC_STATE_DirChangedOnClient",
    "OFFLINEFILES_SYNC_STATE_DirChangedOnClient_ChangedOnServer",
    "OFFLINEFILES_SYNC_STATE_DirChangedOnClient_DeletedOnServer",
    "OFFLINEFILES_SYNC_STATE_DirChangedOnClient_FileChangedOnServer",
    "OFFLINEFILES_SYNC_STATE_DirChangedOnClient_FileOnServer",
    "OFFLINEFILES_SYNC_STATE_DirChangedOnServer",
    "OFFLINEFILES_SYNC_STATE_DirCreatedOnClient_DeletedOnServer",
    "OFFLINEFILES_SYNC_STATE_DirCreatedOnClient_DirChangedOnServer",
    "OFFLINEFILES_SYNC_STATE_DirCreatedOnClient_DirOnServer",
    "OFFLINEFILES_SYNC_STATE_DirCreatedOnClient_FileChangedOnServer",
    "OFFLINEFILES_SYNC_STATE_DirCreatedOnClient_FileOnServer",
    "OFFLINEFILES_SYNC_STATE_DirCreatedOnClient_NoServerCopy",
    "OFFLINEFILES_SYNC_STATE_DirDeletedOnServer",
    "OFFLINEFILES_SYNC_STATE_DirOnClient_FileChangedOnServer",
    "OFFLINEFILES_SYNC_STATE_DirOnClient_FileOnServer",
    "OFFLINEFILES_SYNC_STATE_DirOnClient_NoServerCopy",
    "OFFLINEFILES_SYNC_STATE_DirRenamedOnClient",
    "OFFLINEFILES_SYNC_STATE_DirRenamedOnServer",
    "OFFLINEFILES_SYNC_STATE_DirSparseOnClient",
    "OFFLINEFILES_SYNC_STATE_FileChangedOnClient",
    "OFFLINEFILES_SYNC_STATE_FileChangedOnClient_ChangedOnServer",
    "OFFLINEFILES_SYNC_STATE_FileChangedOnClient_DeletedOnServer",
    "OFFLINEFILES_SYNC_STATE_FileChangedOnClient_DirChangedOnServer",
    "OFFLINEFILES_SYNC_STATE_FileChangedOnClient_DirOnServer",
    "OFFLINEFILES_SYNC_STATE_FileChangedOnServer",
    "OFFLINEFILES_SYNC_STATE_FileCreatedOnClient_DeletedOnServer",
    "OFFLINEFILES_SYNC_STATE_FileCreatedOnClient_DirChangedOnServer",
    "OFFLINEFILES_SYNC_STATE_FileCreatedOnClient_DirOnServer",
    "OFFLINEFILES_SYNC_STATE_FileCreatedOnClient_FileChangedOnServer",
    "OFFLINEFILES_SYNC_STATE_FileCreatedOnClient_FileOnServer",
    "OFFLINEFILES_SYNC_STATE_FileCreatedOnClient_NoServerCopy",
    "OFFLINEFILES_SYNC_STATE_FileDeletedOnServer",
    "OFFLINEFILES_SYNC_STATE_FileOnClient_DirOnServer",
    "OFFLINEFILES_SYNC_STATE_FileOnClient_NoServerCopy",
    "OFFLINEFILES_SYNC_STATE_FileRenamedOnClient",
    "OFFLINEFILES_SYNC_STATE_FileRenamedOnServer",
    "OFFLINEFILES_SYNC_STATE_FileReplacedAndDeletedOnClient_DirChangedOnServer",
    "OFFLINEFILES_SYNC_STATE_FileReplacedAndDeletedOnClient_DirOnServer",
    "OFFLINEFILES_SYNC_STATE_FileReplacedAndDeletedOnClient_FileChangedOnServer",
    "OFFLINEFILES_SYNC_STATE_FileReplacedAndDeletedOnClient_FileOnServer",
    "OFFLINEFILES_SYNC_STATE_FileSparseOnClient",
    "OFFLINEFILES_SYNC_STATE_FileSparseOnClient_ChangedOnServer",
    "OFFLINEFILES_SYNC_STATE_FileSparseOnClient_DeletedOnServer",
    "OFFLINEFILES_SYNC_STATE_FileSparseOnClient_DirChangedOnServer",
    "OFFLINEFILES_SYNC_STATE_FileSparseOnClient_DirOnServer",
    "OFFLINEFILES_SYNC_STATE_LOCAL_KNOWN",
    "OFFLINEFILES_SYNC_STATE_NUMSTATES",
    "OFFLINEFILES_SYNC_STATE_NoClientCopy_DirChangedOnServer",
    "OFFLINEFILES_SYNC_STATE_NoClientCopy_DirOnServer",
    "OFFLINEFILES_SYNC_STATE_NoClientCopy_FileChangedOnServer",
    "OFFLINEFILES_SYNC_STATE_NoClientCopy_FileOnServer",
    "OFFLINEFILES_SYNC_STATE_REMOTE_KNOWN",
    "OFFLINEFILES_SYNC_STATE_Stable",
    "OFFLINEFILES_TRANSITION_FLAG_CONSOLE",
    "OFFLINEFILES_TRANSITION_FLAG_INTERACTIVE",
    "OfflineFilesCache",
    "OfflineFilesEnable",
    "OfflineFilesQueryStatus",
    "OfflineFilesQueryStatusEx",
    "OfflineFilesSetting",
    "OfflineFilesStart",
]
