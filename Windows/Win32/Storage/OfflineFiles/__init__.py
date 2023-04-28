from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation
import Windows.Win32.Storage.OfflineFiles
import Windows.Win32.System.Com
import Windows.Win32.System.Variant
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
OFFLINEFILES_SYNC_STATE_LOCAL_KNOWN: UInt32 = 1
OFFLINEFILES_SYNC_STATE_REMOTE_KNOWN: UInt32 = 2
OFFLINEFILES_CHANGES_NONE: UInt32 = 0
OFFLINEFILES_CHANGES_LOCAL_SIZE: UInt32 = 1
OFFLINEFILES_CHANGES_LOCAL_ATTRIBUTES: UInt32 = 2
OFFLINEFILES_CHANGES_LOCAL_TIME: UInt32 = 4
OFFLINEFILES_CHANGES_REMOTE_SIZE: UInt32 = 8
OFFLINEFILES_CHANGES_REMOTE_ATTRIBUTES: UInt32 = 16
OFFLINEFILES_CHANGES_REMOTE_TIME: UInt32 = 32
OFFLINEFILES_ITEM_FILTER_FLAG_MODIFIED_DATA: UInt32 = 1
OFFLINEFILES_ITEM_FILTER_FLAG_MODIFIED_ATTRIBUTES: UInt32 = 2
OFFLINEFILES_ITEM_FILTER_FLAG_MODIFIED: UInt32 = 4
OFFLINEFILES_ITEM_FILTER_FLAG_CREATED: UInt32 = 8
OFFLINEFILES_ITEM_FILTER_FLAG_DELETED: UInt32 = 16
OFFLINEFILES_ITEM_FILTER_FLAG_DIRTY: UInt32 = 32
OFFLINEFILES_ITEM_FILTER_FLAG_SPARSE: UInt32 = 64
OFFLINEFILES_ITEM_FILTER_FLAG_FILE: UInt32 = 128
OFFLINEFILES_ITEM_FILTER_FLAG_DIRECTORY: UInt32 = 256
OFFLINEFILES_ITEM_FILTER_FLAG_PINNED_USER: UInt32 = 512
OFFLINEFILES_ITEM_FILTER_FLAG_PINNED_OTHERS: UInt32 = 1024
OFFLINEFILES_ITEM_FILTER_FLAG_PINNED_COMPUTER: UInt32 = 2048
OFFLINEFILES_ITEM_FILTER_FLAG_PINNED: UInt32 = 4096
OFFLINEFILES_ITEM_FILTER_FLAG_GHOST: UInt32 = 8192
OFFLINEFILES_ITEM_FILTER_FLAG_SUSPENDED: UInt32 = 16384
OFFLINEFILES_ITEM_FILTER_FLAG_OFFLINE: UInt32 = 32768
OFFLINEFILES_ITEM_FILTER_FLAG_ONLINE: UInt32 = 65536
OFFLINEFILES_ITEM_FILTER_FLAG_USER_WRITE: UInt32 = 131072
OFFLINEFILES_ITEM_FILTER_FLAG_USER_READ: UInt32 = 262144
OFFLINEFILES_ITEM_FILTER_FLAG_USER_ANYACCESS: UInt32 = 524288
OFFLINEFILES_ITEM_FILTER_FLAG_OTHER_WRITE: UInt32 = 1048576
OFFLINEFILES_ITEM_FILTER_FLAG_OTHER_READ: UInt32 = 2097152
OFFLINEFILES_ITEM_FILTER_FLAG_OTHER_ANYACCESS: UInt32 = 4194304
OFFLINEFILES_ITEM_FILTER_FLAG_GUEST_WRITE: UInt32 = 8388608
OFFLINEFILES_ITEM_FILTER_FLAG_GUEST_READ: UInt32 = 16777216
OFFLINEFILES_ITEM_FILTER_FLAG_GUEST_ANYACCESS: UInt32 = 33554432
OFFLINEFILES_ITEM_QUERY_REMOTEINFO: UInt32 = 1
OFFLINEFILES_ITEM_QUERY_CONNECTIONSTATE: UInt32 = 2
OFFLINEFILES_ITEM_QUERY_LOCALDIRTYBYTECOUNT: UInt32 = 4
OFFLINEFILES_ITEM_QUERY_REMOTEDIRTYBYTECOUNT: UInt32 = 8
OFFLINEFILES_ITEM_QUERY_INCLUDETRANSPARENTCACHE: UInt32 = 16
OFFLINEFILES_ITEM_QUERY_ATTEMPT_TRANSITIONONLINE: UInt32 = 32
OFFLINEFILES_ITEM_QUERY_ADMIN: UInt32 = 2147483648
OFFLINEFILES_ENUM_FLAT: UInt32 = 1
OFFLINEFILES_ENUM_FLAT_FILESONLY: UInt32 = 2
OFFLINEFILES_SETTING_SCOPE_USER: UInt32 = 1
OFFLINEFILES_SETTING_SCOPE_COMPUTER: UInt32 = 2
OFFLINEFILES_SETTING_PinLinkTargets: String = 'LinkTargetCaching'
OFFLINEFILES_PINLINKTARGETS_NEVER: UInt32 = 0
OFFLINEFILES_PINLINKTARGETS_EXPLICIT: UInt32 = 1
OFFLINEFILES_PINLINKTARGETS_ALWAYS: UInt32 = 2
OFFLINEFILES_SYNC_CONTROL_FLAG_FILLSPARSE: UInt32 = 1
OFFLINEFILES_SYNC_CONTROL_FLAG_SYNCIN: UInt32 = 2
OFFLINEFILES_SYNC_CONTROL_FLAG_SYNCOUT: UInt32 = 4
OFFLINEFILES_SYNC_CONTROL_FLAG_PINNEWFILES: UInt32 = 8
OFFLINEFILES_SYNC_CONTROL_FLAG_PINLINKTARGETS: UInt32 = 16
OFFLINEFILES_SYNC_CONTROL_FLAG_PINFORUSER: UInt32 = 32
OFFLINEFILES_SYNC_CONTROL_FLAG_PINFORUSER_POLICY: UInt32 = 64
OFFLINEFILES_SYNC_CONTROL_FLAG_PINFORALL: UInt32 = 128
OFFLINEFILES_SYNC_CONTROL_FLAG_PINFORREDIR: UInt32 = 256
OFFLINEFILES_SYNC_CONTROL_FLAG_LOWPRIORITY: UInt32 = 512
OFFLINEFILES_SYNC_CONTROL_FLAG_ASYNCPROGRESS: UInt32 = 1024
OFFLINEFILES_SYNC_CONTROL_FLAG_INTERACTIVE: UInt32 = 2048
OFFLINEFILES_SYNC_CONTROL_FLAG_CONSOLE: UInt32 = 4096
OFFLINEFILES_SYNC_CONTROL_FLAG_SKIPSUSPENDEDDIRS: UInt32 = 8192
OFFLINEFILES_SYNC_CONTROL_FLAG_BACKGROUND: UInt32 = 65536
OFFLINEFILES_SYNC_CONTROL_FLAG_NONEWFILESOUT: UInt32 = 131072
OFFLINEFILES_SYNC_CONTROL_CR_MASK: UInt32 = 4026531840
OFFLINEFILES_SYNC_CONTROL_CR_DEFAULT: UInt32 = 0
OFFLINEFILES_SYNC_CONTROL_CR_KEEPLOCAL: UInt32 = 268435456
OFFLINEFILES_SYNC_CONTROL_CR_KEEPREMOTE: UInt32 = 536870912
OFFLINEFILES_SYNC_CONTROL_CR_KEEPLATEST: UInt32 = 805306368
OFFLINEFILES_PIN_CONTROL_FLAG_FORUSER: UInt32 = 32
OFFLINEFILES_PIN_CONTROL_FLAG_FORUSER_POLICY: UInt32 = 64
OFFLINEFILES_PIN_CONTROL_FLAG_FORALL: UInt32 = 128
OFFLINEFILES_PIN_CONTROL_FLAG_FORREDIR: UInt32 = 256
OFFLINEFILES_PIN_CONTROL_FLAG_FILL: UInt32 = 1
OFFLINEFILES_PIN_CONTROL_FLAG_LOWPRIORITY: UInt32 = 512
OFFLINEFILES_PIN_CONTROL_FLAG_ASYNCPROGRESS: UInt32 = 1024
OFFLINEFILES_PIN_CONTROL_FLAG_INTERACTIVE: UInt32 = 2048
OFFLINEFILES_PIN_CONTROL_FLAG_CONSOLE: UInt32 = 4096
OFFLINEFILES_PIN_CONTROL_FLAG_PINLINKTARGETS: UInt32 = 16
OFFLINEFILES_PIN_CONTROL_FLAG_BACKGROUND: UInt32 = 65536
OFFLINEFILES_ENCRYPTION_CONTROL_FLAG_LOWPRIORITY: UInt32 = 512
OFFLINEFILES_ENCRYPTION_CONTROL_FLAG_ASYNCPROGRESS: UInt32 = 1024
OFFLINEFILES_ENCRYPTION_CONTROL_FLAG_INTERACTIVE: UInt32 = 2048
OFFLINEFILES_ENCRYPTION_CONTROL_FLAG_CONSOLE: UInt32 = 4096
OFFLINEFILES_ENCRYPTION_CONTROL_FLAG_BACKGROUND: UInt32 = 65536
OFFLINEFILES_DELETE_FLAG_NOAUTOCACHED: UInt32 = 1
OFFLINEFILES_DELETE_FLAG_NOPINNED: UInt32 = 2
OFFLINEFILES_DELETE_FLAG_DELMODIFIED: UInt32 = 4
OFFLINEFILES_DELETE_FLAG_ADMIN: UInt32 = 2147483648
OFFLINEFILES_TRANSITION_FLAG_INTERACTIVE: UInt32 = 1
OFFLINEFILES_TRANSITION_FLAG_CONSOLE: UInt32 = 2
OFFLINEFILES_SYNC_ITEM_CHANGE_NONE: UInt32 = 0
OFFLINEFILES_SYNC_ITEM_CHANGE_CHANGETIME: UInt32 = 1
OFFLINEFILES_SYNC_ITEM_CHANGE_WRITETIME: UInt32 = 2
OFFLINEFILES_SYNC_ITEM_CHANGE_FILESIZE: UInt32 = 4
OFFLINEFILES_SYNC_ITEM_CHANGE_ATTRIBUTES: UInt32 = 8
@winfunctype('CSCAPI.dll')
def OfflineFilesEnable(bEnable: Windows.Win32.Foundation.BOOL, pbRebootRequired: POINTER(Windows.Win32.Foundation.BOOL)) -> UInt32: ...
@winfunctype('CSCAPI.dll')
def OfflineFilesStart() -> UInt32: ...
@winfunctype('CSCAPI.dll')
def OfflineFilesQueryStatus(pbActive: POINTER(Windows.Win32.Foundation.BOOL), pbEnabled: POINTER(Windows.Win32.Foundation.BOOL)) -> UInt32: ...
@winfunctype('CSCAPI.dll')
def OfflineFilesQueryStatusEx(pbActive: POINTER(Windows.Win32.Foundation.BOOL), pbEnabled: POINTER(Windows.Win32.Foundation.BOOL), pbAvailable: POINTER(Windows.Win32.Foundation.BOOL)) -> UInt32: ...
class IEnumOfflineFilesItems(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('da70e815-c361-4407-bc-0b-0d-70-46-e5-f2-cd')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(Windows.Win32.Storage.OfflineFiles.IOfflineFilesItem_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(Windows.Win32.Storage.OfflineFiles.IEnumOfflineFilesItems_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumOfflineFilesSettings(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('729680c4-1a38-47bc-9e-5c-02-c5-15-62-ac-30')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(Windows.Win32.Storage.OfflineFiles.IOfflineFilesSetting_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(Windows.Win32.Storage.OfflineFiles.IEnumOfflineFilesSettings_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesCache(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('855d6203-7914-48b9-8d-40-4c-56-f5-ac-ff-c5')
    @commethod(3)
    def Synchronize(self, hwndParent: Windows.Win32.Foundation.HWND, rgpszPaths: POINTER(Windows.Win32.Foundation.PWSTR), cPaths: UInt32, bAsync: Windows.Win32.Foundation.BOOL, dwSyncControl: UInt32, pISyncConflictHandler: Windows.Win32.Storage.OfflineFiles.IOfflineFilesSyncConflictHandler_head, pIProgress: Windows.Win32.Storage.OfflineFiles.IOfflineFilesSyncProgress_head, pSyncId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DeleteItems(self, rgpszPaths: POINTER(Windows.Win32.Foundation.PWSTR), cPaths: UInt32, dwFlags: UInt32, bAsync: Windows.Win32.Foundation.BOOL, pIProgress: Windows.Win32.Storage.OfflineFiles.IOfflineFilesSimpleProgress_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DeleteItemsForUser(self, pszUser: Windows.Win32.Foundation.PWSTR, rgpszPaths: POINTER(Windows.Win32.Foundation.PWSTR), cPaths: UInt32, dwFlags: UInt32, bAsync: Windows.Win32.Foundation.BOOL, pIProgress: Windows.Win32.Storage.OfflineFiles.IOfflineFilesSimpleProgress_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Pin(self, hwndParent: Windows.Win32.Foundation.HWND, rgpszPaths: POINTER(Windows.Win32.Foundation.PWSTR), cPaths: UInt32, bDeep: Windows.Win32.Foundation.BOOL, bAsync: Windows.Win32.Foundation.BOOL, dwPinControlFlags: UInt32, pIProgress: Windows.Win32.Storage.OfflineFiles.IOfflineFilesSyncProgress_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Unpin(self, hwndParent: Windows.Win32.Foundation.HWND, rgpszPaths: POINTER(Windows.Win32.Foundation.PWSTR), cPaths: UInt32, bDeep: Windows.Win32.Foundation.BOOL, bAsync: Windows.Win32.Foundation.BOOL, dwPinControlFlags: UInt32, pIProgress: Windows.Win32.Storage.OfflineFiles.IOfflineFilesSyncProgress_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetEncryptionStatus(self, pbEncrypted: POINTER(Windows.Win32.Foundation.BOOL), pbPartial: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Encrypt(self, hwndParent: Windows.Win32.Foundation.HWND, bEncrypt: Windows.Win32.Foundation.BOOL, dwEncryptionControlFlags: UInt32, bAsync: Windows.Win32.Foundation.BOOL, pIProgress: Windows.Win32.Storage.OfflineFiles.IOfflineFilesSyncProgress_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def FindItem(self, pszPath: Windows.Win32.Foundation.PWSTR, dwQueryFlags: UInt32, ppItem: POINTER(Windows.Win32.Storage.OfflineFiles.IOfflineFilesItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def FindItemEx(self, pszPath: Windows.Win32.Foundation.PWSTR, pIncludeFileFilter: Windows.Win32.Storage.OfflineFiles.IOfflineFilesItemFilter_head, pIncludeDirFilter: Windows.Win32.Storage.OfflineFiles.IOfflineFilesItemFilter_head, pExcludeFileFilter: Windows.Win32.Storage.OfflineFiles.IOfflineFilesItemFilter_head, pExcludeDirFilter: Windows.Win32.Storage.OfflineFiles.IOfflineFilesItemFilter_head, dwQueryFlags: UInt32, ppItem: POINTER(Windows.Win32.Storage.OfflineFiles.IOfflineFilesItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RenameItem(self, pszPathOriginal: Windows.Win32.Foundation.PWSTR, pszPathNew: Windows.Win32.Foundation.PWSTR, bReplaceIfExists: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetLocation(self, ppszPath: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetDiskSpaceInformation(self, pcbVolumeTotal: POINTER(UInt64), pcbLimit: POINTER(UInt64), pcbUsed: POINTER(UInt64), pcbUnpinnedLimit: POINTER(UInt64), pcbUnpinnedUsed: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetDiskSpaceLimits(self, cbLimit: UInt64, cbUnpinnedLimit: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def ProcessAdminPinPolicy(self, pPinProgress: Windows.Win32.Storage.OfflineFiles.IOfflineFilesSyncProgress_head, pUnpinProgress: Windows.Win32.Storage.OfflineFiles.IOfflineFilesSyncProgress_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetSettingObject(self, pszSettingName: Windows.Win32.Foundation.PWSTR, ppSetting: POINTER(Windows.Win32.Storage.OfflineFiles.IOfflineFilesSetting_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def EnumSettingObjects(self, ppEnum: POINTER(Windows.Win32.Storage.OfflineFiles.IEnumOfflineFilesSettings_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def IsPathCacheable(self, pszPath: Windows.Win32.Foundation.PWSTR, pbCacheable: POINTER(Windows.Win32.Foundation.BOOL), pShareCachingMode: POINTER(Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_CACHING_MODE)) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesCache2(c_void_p):
    extends: Windows.Win32.Storage.OfflineFiles.IOfflineFilesCache
    Guid = Guid('8c075039-1551-4ed9-87-81-56-70-5c-04-d3-c0')
    @commethod(20)
    def RenameItemEx(self, pszPathOriginal: Windows.Win32.Foundation.PWSTR, pszPathNew: Windows.Win32.Foundation.PWSTR, bReplaceIfExists: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesChangeInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a96e6fa4-e0d1-4c29-96-0b-ee-50-8f-e6-8c-72')
    @commethod(3)
    def IsDirty(self, pbDirty: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsDeletedOffline(self, pbDeletedOffline: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsCreatedOffline(self, pbCreatedOffline: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsLocallyModifiedData(self, pbLocallyModifiedData: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsLocallyModifiedAttributes(self, pbLocallyModifiedAttributes: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsLocallyModifiedTime(self, pbLocallyModifiedTime: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesConnectionInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('efb23a09-a867-4be8-83-a6-86-96-9a-7d-08-56')
    @commethod(3)
    def GetConnectState(self, pConnectState: POINTER(Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_CONNECT_STATE), pOfflineReason: POINTER(Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_OFFLINE_REASON)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetConnectState(self, hwndParent: Windows.Win32.Foundation.HWND, dwFlags: UInt32, ConnectState: Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_CONNECT_STATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def TransitionOnline(self, hwndParent: Windows.Win32.Foundation.HWND, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def TransitionOffline(self, hwndParent: Windows.Win32.Foundation.HWND, dwFlags: UInt32, bForceOpenFilesClosed: Windows.Win32.Foundation.BOOL, pbOpenFilesPreventedTransition: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesDirectoryItem(c_void_p):
    extends: Windows.Win32.Storage.OfflineFiles.IOfflineFilesItem
    Guid = Guid('2273597a-a08c-4a00-a3-7a-c1-ae-4e-9a-1c-fd')
class IOfflineFilesDirtyInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0f50ce33-bac9-4eaa-a1-1d-da-0e-52-7d-04-7d')
    @commethod(3)
    def LocalDirtyByteCount(self, pDirtyByteCount: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoteDirtyByteCount(self, pDirtyByteCount: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesErrorInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7112fa5f-7571-435a-8e-b7-19-5c-7c-14-29-bc')
    @commethod(3)
    def GetRawData(self, ppBlob: POINTER(POINTER(Windows.Win32.System.Com.BYTE_BLOB_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDescription(self, ppszDescription: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e25585c1-0caa-4eb1-87-3b-1c-ae-5b-77-c3-14')
    @commethod(3)
    def CacheMoved(self, pszOldPath: Windows.Win32.Foundation.PWSTR, pszNewPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CacheIsFull(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CacheIsCorrupted(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Enabled(self, bEnabled: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EncryptionChanged(self, bWasEncrypted: Windows.Win32.Foundation.BOOL, bWasPartial: Windows.Win32.Foundation.BOOL, bIsEncrypted: Windows.Win32.Foundation.BOOL, bIsPartial: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SyncBegin(self, rSyncId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SyncFileResult(self, rSyncId: POINTER(Guid), pszFile: Windows.Win32.Foundation.PWSTR, hrResult: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SyncConflictRecAdded(self, pszConflictPath: Windows.Win32.Foundation.PWSTR, pftConflictDateTime: POINTER(Windows.Win32.Foundation.FILETIME_head), ConflictSyncState: Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SyncConflictRecUpdated(self, pszConflictPath: Windows.Win32.Foundation.PWSTR, pftConflictDateTime: POINTER(Windows.Win32.Foundation.FILETIME_head), ConflictSyncState: Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SyncConflictRecRemoved(self, pszConflictPath: Windows.Win32.Foundation.PWSTR, pftConflictDateTime: POINTER(Windows.Win32.Foundation.FILETIME_head), ConflictSyncState: Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SyncEnd(self, rSyncId: POINTER(Guid), hrResult: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def NetTransportArrived(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def NoNetTransports(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def ItemDisconnected(self, pszPath: Windows.Win32.Foundation.PWSTR, ItemType: Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def ItemReconnected(self, pszPath: Windows.Win32.Foundation.PWSTR, ItemType: Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def ItemAvailableOffline(self, pszPath: Windows.Win32.Foundation.PWSTR, ItemType: Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ItemNotAvailableOffline(self, pszPath: Windows.Win32.Foundation.PWSTR, ItemType: Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def ItemPinned(self, pszPath: Windows.Win32.Foundation.PWSTR, ItemType: Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def ItemNotPinned(self, pszPath: Windows.Win32.Foundation.PWSTR, ItemType: Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def ItemModified(self, pszPath: Windows.Win32.Foundation.PWSTR, ItemType: Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE, bModifiedData: Windows.Win32.Foundation.BOOL, bModifiedAttributes: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def ItemAddedToCache(self, pszPath: Windows.Win32.Foundation.PWSTR, ItemType: Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def ItemDeletedFromCache(self, pszPath: Windows.Win32.Foundation.PWSTR, ItemType: Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def ItemRenamed(self, pszOldPath: Windows.Win32.Foundation.PWSTR, pszNewPath: Windows.Win32.Foundation.PWSTR, ItemType: Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def DataLost(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def Ping(self) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesEvents2(c_void_p):
    extends: Windows.Win32.Storage.OfflineFiles.IOfflineFilesEvents
    Guid = Guid('1ead8f56-ff76-4faa-a7-95-6f-6e-f7-92-49-8b')
    @commethod(28)
    def ItemReconnectBegin(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def ItemReconnectEnd(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def CacheEvictBegin(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def CacheEvictEnd(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def BackgroundSyncBegin(self, dwSyncControlFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def BackgroundSyncEnd(self, dwSyncControlFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def PolicyChangeDetected(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def PreferenceChangeDetected(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def SettingsChangesApplied(self) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesEvents3(c_void_p):
    extends: Windows.Win32.Storage.OfflineFiles.IOfflineFilesEvents2
    Guid = Guid('9ba04a45-ee69-42f0-9a-b1-7d-b5-c8-80-58-08')
    @commethod(37)
    def TransparentCacheItemNotify(self, pszPath: Windows.Win32.Foundation.PWSTR, EventType: Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS, ItemType: Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE, bModifiedData: Windows.Win32.Foundation.BOOL, bModifiedAttributes: Windows.Win32.Foundation.BOOL, pzsOldPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def PrefetchFileBegin(self, pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def PrefetchFileEnd(self, pszPath: Windows.Win32.Foundation.PWSTR, hrResult: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesEvents4(c_void_p):
    extends: Windows.Win32.Storage.OfflineFiles.IOfflineFilesEvents3
    Guid = Guid('dbd69b1e-c7d2-473e-b3-5f-9d-8c-24-c0-c4-84')
    @commethod(40)
    def PrefetchCloseHandleBegin(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def PrefetchCloseHandleEnd(self, dwClosedHandleCount: UInt32, dwOpenHandleCount: UInt32, hrResult: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesEventsFilter(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('33fc4e1b-0716-40fa-ba-65-6e-62-a8-4a-84-6f')
    @commethod(3)
    def GetPathFilter(self, ppszFilter: POINTER(Windows.Win32.Foundation.PWSTR), pMatch: POINTER(Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_PATHFILTER_MATCH)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIncludedEvents(self, cElements: UInt32, prgEvents: POINTER(Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS), pcEvents: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetExcludedEvents(self, cElements: UInt32, prgEvents: POINTER(Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS), pcEvents: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesFileItem(c_void_p):
    extends: Windows.Win32.Storage.OfflineFiles.IOfflineFilesItem
    Guid = Guid('8dfadead-26c2-4eff-8a-72-6b-50-72-3d-9a-00')
    @commethod(8)
    def IsSparse(self, pbIsSparse: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def IsEncrypted(self, pbIsEncrypted: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesFileSysInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('bc1a163f-7bfd-4d88-9c-66-96-ea-9a-6a-3d-6b')
    @commethod(3)
    def GetAttributes(self, copy: Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_COPY, pdwAttributes: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTimes(self, copy: Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_COPY, pftCreationTime: POINTER(Windows.Win32.Foundation.FILETIME_head), pftLastWriteTime: POINTER(Windows.Win32.Foundation.FILETIME_head), pftChangeTime: POINTER(Windows.Win32.Foundation.FILETIME_head), pftLastAccessTime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFileSize(self, copy: Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_COPY, pSize: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesGhostInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2b09d48c-8ab5-464f-a7-55-a5-9d-92-f9-94-29')
    @commethod(3)
    def IsGhosted(self, pbGhosted: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesItem(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4a753da6-e044-4f12-a7-18-5d-14-d0-79-a9-06')
    @commethod(3)
    def GetItemType(self, pItemType: POINTER(Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPath(self, ppszPath: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetParentItem(self, ppItem: POINTER(Windows.Win32.Storage.OfflineFiles.IOfflineFilesItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Refresh(self, dwQueryFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsMarkedForDeletion(self, pbMarkedForDeletion: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesItemContainer(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3836f049-9413-45dd-bf-46-b5-aa-a8-2d-c3-10')
    @commethod(3)
    def EnumItems(self, dwQueryFlags: UInt32, ppenum: POINTER(Windows.Win32.Storage.OfflineFiles.IEnumOfflineFilesItems_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumItemsEx(self, pIncludeFileFilter: Windows.Win32.Storage.OfflineFiles.IOfflineFilesItemFilter_head, pIncludeDirFilter: Windows.Win32.Storage.OfflineFiles.IOfflineFilesItemFilter_head, pExcludeFileFilter: Windows.Win32.Storage.OfflineFiles.IOfflineFilesItemFilter_head, pExcludeDirFilter: Windows.Win32.Storage.OfflineFiles.IOfflineFilesItemFilter_head, dwEnumFlags: UInt32, dwQueryFlags: UInt32, ppenum: POINTER(Windows.Win32.Storage.OfflineFiles.IEnumOfflineFilesItems_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesItemFilter(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f4b5a26c-dc05-4f20-ad-a4-55-1f-10-77-be-5c')
    @commethod(3)
    def GetFilterFlags(self, pullFlags: POINTER(UInt64), pullMask: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTimeFilter(self, pftTime: POINTER(Windows.Win32.Foundation.FILETIME_head), pbEvalTimeOfDay: POINTER(Windows.Win32.Foundation.BOOL), pTimeType: POINTER(Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TIME), pCompare: POINTER(Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_COMPARE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPatternFilter(self, pszPattern: Windows.Win32.Foundation.PWSTR, cchPattern: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesPinInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5b2b0655-b3fd-497d-ad-eb-bd-15-6b-c8-35-5b')
    @commethod(3)
    def IsPinned(self, pbPinned: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsPinnedForUser(self, pbPinnedForUser: POINTER(Windows.Win32.Foundation.BOOL), pbInherit: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsPinnedForUserByPolicy(self, pbPinnedForUser: POINTER(Windows.Win32.Foundation.BOOL), pbInherit: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsPinnedForComputer(self, pbPinnedForComputer: POINTER(Windows.Win32.Foundation.BOOL), pbInherit: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsPinnedForFolderRedirection(self, pbPinnedForFolderRedirection: POINTER(Windows.Win32.Foundation.BOOL), pbInherit: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesPinInfo2(c_void_p):
    extends: Windows.Win32.Storage.OfflineFiles.IOfflineFilesPinInfo
    Guid = Guid('623c58a2-42ed-4ad7-b6-9a-0f-1b-30-a7-2d-0d')
    @commethod(8)
    def IsPartlyPinned(self, pbPartlyPinned: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesProgress(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fad63237-c55b-4911-98-50-bc-f9-6d-4c-97-9e')
    @commethod(3)
    def Begin(self, pbAbort: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def QueryAbort(self, pbAbort: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def End(self, hrResult: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesServerItem(c_void_p):
    extends: Windows.Win32.Storage.OfflineFiles.IOfflineFilesItem
    Guid = Guid('9b1c9576-a92b-4151-8e-9e-7c-7b-3e-c2-e0-16')
class IOfflineFilesSetting(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d871d3f7-f613-48a1-82-7e-7a-34-e5-60-ff-f6')
    @commethod(3)
    def GetName(self, ppszName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetValueType(self, pType: POINTER(Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SETTING_VALUE_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPreference(self, pvarValue: POINTER(Windows.Win32.System.Variant.VARIANT_head), dwScope: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPreferenceScope(self, pdwScope: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetPreference(self, pvarValue: POINTER(Windows.Win32.System.Variant.VARIANT_head), dwScope: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DeletePreference(self, dwScope: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPolicy(self, pvarValue: POINTER(Windows.Win32.System.Variant.VARIANT_head), dwScope: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetPolicyScope(self, pdwScope: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetValue(self, pvarValue: POINTER(Windows.Win32.System.Variant.VARIANT_head), pbSetByPolicy: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesShareInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7bcc43e7-31ce-4ca4-8c-cd-1c-ff-2d-c4-94-da')
    @commethod(3)
    def GetShareItem(self, ppShareItem: POINTER(Windows.Win32.Storage.OfflineFiles.IOfflineFilesShareItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetShareCachingMode(self, pCachingMode: POINTER(Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_CACHING_MODE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsShareDfsJunction(self, pbIsDfsJunction: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesShareItem(c_void_p):
    extends: Windows.Win32.Storage.OfflineFiles.IOfflineFilesItem
    Guid = Guid('bab7e48d-4804-41b5-a4-4d-0f-19-9b-06-b1-45')
class IOfflineFilesSimpleProgress(c_void_p):
    extends: Windows.Win32.Storage.OfflineFiles.IOfflineFilesProgress
    Guid = Guid('c34f7f9b-c43d-4f9d-a7-76-c0-eb-6d-e5-d4-01')
    @commethod(6)
    def ItemBegin(self, pszFile: Windows.Win32.Foundation.PWSTR, pResponse: POINTER(Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_OP_RESPONSE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ItemResult(self, pszFile: Windows.Win32.Foundation.PWSTR, hrResult: Windows.Win32.Foundation.HRESULT, pResponse: POINTER(Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_OP_RESPONSE)) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesSuspend(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('62c4560f-bc0b-48ca-ad-9d-34-cb-52-8d-99-a9')
    @commethod(3)
    def SuspendRoot(self, bSuspend: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesSuspendInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a457c25b-4e9c-4b04-85-af-89-32-cc-d9-78-89')
    @commethod(3)
    def IsSuspended(self, pbSuspended: POINTER(Windows.Win32.Foundation.BOOL), pbSuspendedRoot: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesSyncConflictHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b6dd5092-c65c-46b6-97-b8-fa-dd-08-e7-e1-be')
    @commethod(3)
    def ResolveConflict(self, pszPath: Windows.Win32.Foundation.PWSTR, fStateKnown: UInt32, state: Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE, fChangeDetails: UInt32, pConflictResolution: POINTER(Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_CONFLICT_RESOLVE), ppszNewName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesSyncErrorInfo(c_void_p):
    extends: Windows.Win32.Storage.OfflineFiles.IOfflineFilesErrorInfo
    Guid = Guid('59f95e46-eb54-49d1-be-76-de-95-45-8d-01-b0')
    @commethod(5)
    def GetSyncOperation(self, pSyncOp: POINTER(Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_OPERATION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetItemChangeFlags(self, pdwItemChangeFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def InfoEnumerated(self, pbLocalEnumerated: POINTER(Windows.Win32.Foundation.BOOL), pbRemoteEnumerated: POINTER(Windows.Win32.Foundation.BOOL), pbOriginalEnumerated: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def InfoAvailable(self, pbLocalInfo: POINTER(Windows.Win32.Foundation.BOOL), pbRemoteInfo: POINTER(Windows.Win32.Foundation.BOOL), pbOriginalInfo: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetLocalInfo(self, ppInfo: POINTER(Windows.Win32.Storage.OfflineFiles.IOfflineFilesSyncErrorItemInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRemoteInfo(self, ppInfo: POINTER(Windows.Win32.Storage.OfflineFiles.IOfflineFilesSyncErrorItemInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetOriginalInfo(self, ppInfo: POINTER(Windows.Win32.Storage.OfflineFiles.IOfflineFilesSyncErrorItemInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesSyncErrorItemInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ecdbaf0d-6a18-4d55-80-17-10-8f-76-60-ba-44')
    @commethod(3)
    def GetFileAttributes(self, pdwAttributes: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFileTimes(self, pftLastWrite: POINTER(Windows.Win32.Foundation.FILETIME_head), pftChange: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFileSize(self, pSize: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesSyncProgress(c_void_p):
    extends: Windows.Win32.Storage.OfflineFiles.IOfflineFilesProgress
    Guid = Guid('6931f49a-6fc7-4c1b-b2-65-56-79-3f-c4-51-b7')
    @commethod(6)
    def SyncItemBegin(self, pszFile: Windows.Win32.Foundation.PWSTR, pResponse: POINTER(Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_OP_RESPONSE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SyncItemResult(self, pszFile: Windows.Win32.Foundation.PWSTR, hrResult: Windows.Win32.Foundation.HRESULT, pErrorInfo: Windows.Win32.Storage.OfflineFiles.IOfflineFilesSyncErrorInfo_head, pResponse: POINTER(Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_OP_RESPONSE)) -> Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesTransparentCacheInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('bcaf4a01-5b68-4b56-a6-a1-8d-27-86-ed-e8-e3')
    @commethod(3)
    def IsTransparentlyCached(self, pbTransparentlyCached: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
OFFLINEFILES_CACHING_MODE = Int32
OFFLINEFILES_CACHING_MODE_NONE: OFFLINEFILES_CACHING_MODE = 0
OFFLINEFILES_CACHING_MODE_NOCACHING: OFFLINEFILES_CACHING_MODE = 1
OFFLINEFILES_CACHING_MODE_MANUAL: OFFLINEFILES_CACHING_MODE = 2
OFFLINEFILES_CACHING_MODE_AUTO_DOC: OFFLINEFILES_CACHING_MODE = 3
OFFLINEFILES_CACHING_MODE_AUTO_PROGANDDOC: OFFLINEFILES_CACHING_MODE = 4
OFFLINEFILES_COMPARE = Int32
OFFLINEFILES_COMPARE_EQ: OFFLINEFILES_COMPARE = 0
OFFLINEFILES_COMPARE_NEQ: OFFLINEFILES_COMPARE = 1
OFFLINEFILES_COMPARE_LT: OFFLINEFILES_COMPARE = 2
OFFLINEFILES_COMPARE_GT: OFFLINEFILES_COMPARE = 3
OFFLINEFILES_COMPARE_LTE: OFFLINEFILES_COMPARE = 4
OFFLINEFILES_COMPARE_GTE: OFFLINEFILES_COMPARE = 5
OFFLINEFILES_CONNECT_STATE = Int32
OFFLINEFILES_CONNECT_STATE_UNKNOWN: OFFLINEFILES_CONNECT_STATE = 0
OFFLINEFILES_CONNECT_STATE_OFFLINE: OFFLINEFILES_CONNECT_STATE = 1
OFFLINEFILES_CONNECT_STATE_ONLINE: OFFLINEFILES_CONNECT_STATE = 2
OFFLINEFILES_CONNECT_STATE_TRANSPARENTLY_CACHED: OFFLINEFILES_CONNECT_STATE = 3
OFFLINEFILES_CONNECT_STATE_PARTLY_TRANSPARENTLY_CACHED: OFFLINEFILES_CONNECT_STATE = 4
OFFLINEFILES_EVENTS = Int32
OFFLINEFILES_EVENT_CACHEMOVED: OFFLINEFILES_EVENTS = 0
OFFLINEFILES_EVENT_CACHEISFULL: OFFLINEFILES_EVENTS = 1
OFFLINEFILES_EVENT_CACHEISCORRUPTED: OFFLINEFILES_EVENTS = 2
OFFLINEFILES_EVENT_ENABLED: OFFLINEFILES_EVENTS = 3
OFFLINEFILES_EVENT_ENCRYPTIONCHANGED: OFFLINEFILES_EVENTS = 4
OFFLINEFILES_EVENT_SYNCBEGIN: OFFLINEFILES_EVENTS = 5
OFFLINEFILES_EVENT_SYNCFILERESULT: OFFLINEFILES_EVENTS = 6
OFFLINEFILES_EVENT_SYNCCONFLICTRECADDED: OFFLINEFILES_EVENTS = 7
OFFLINEFILES_EVENT_SYNCCONFLICTRECUPDATED: OFFLINEFILES_EVENTS = 8
OFFLINEFILES_EVENT_SYNCCONFLICTRECREMOVED: OFFLINEFILES_EVENTS = 9
OFFLINEFILES_EVENT_SYNCEND: OFFLINEFILES_EVENTS = 10
OFFLINEFILES_EVENT_BACKGROUNDSYNCBEGIN: OFFLINEFILES_EVENTS = 11
OFFLINEFILES_EVENT_BACKGROUNDSYNCEND: OFFLINEFILES_EVENTS = 12
OFFLINEFILES_EVENT_NETTRANSPORTARRIVED: OFFLINEFILES_EVENTS = 13
OFFLINEFILES_EVENT_NONETTRANSPORTS: OFFLINEFILES_EVENTS = 14
OFFLINEFILES_EVENT_ITEMDISCONNECTED: OFFLINEFILES_EVENTS = 15
OFFLINEFILES_EVENT_ITEMRECONNECTED: OFFLINEFILES_EVENTS = 16
OFFLINEFILES_EVENT_ITEMAVAILABLEOFFLINE: OFFLINEFILES_EVENTS = 17
OFFLINEFILES_EVENT_ITEMNOTAVAILABLEOFFLINE: OFFLINEFILES_EVENTS = 18
OFFLINEFILES_EVENT_ITEMPINNED: OFFLINEFILES_EVENTS = 19
OFFLINEFILES_EVENT_ITEMNOTPINNED: OFFLINEFILES_EVENTS = 20
OFFLINEFILES_EVENT_ITEMMODIFIED: OFFLINEFILES_EVENTS = 21
OFFLINEFILES_EVENT_ITEMADDEDTOCACHE: OFFLINEFILES_EVENTS = 22
OFFLINEFILES_EVENT_ITEMDELETEDFROMCACHE: OFFLINEFILES_EVENTS = 23
OFFLINEFILES_EVENT_ITEMRENAMED: OFFLINEFILES_EVENTS = 24
OFFLINEFILES_EVENT_DATALOST: OFFLINEFILES_EVENTS = 25
OFFLINEFILES_EVENT_PING: OFFLINEFILES_EVENTS = 26
OFFLINEFILES_EVENT_ITEMRECONNECTBEGIN: OFFLINEFILES_EVENTS = 27
OFFLINEFILES_EVENT_ITEMRECONNECTEND: OFFLINEFILES_EVENTS = 28
OFFLINEFILES_EVENT_CACHEEVICTBEGIN: OFFLINEFILES_EVENTS = 29
OFFLINEFILES_EVENT_CACHEEVICTEND: OFFLINEFILES_EVENTS = 30
OFFLINEFILES_EVENT_POLICYCHANGEDETECTED: OFFLINEFILES_EVENTS = 31
OFFLINEFILES_EVENT_PREFERENCECHANGEDETECTED: OFFLINEFILES_EVENTS = 32
OFFLINEFILES_EVENT_SETTINGSCHANGESAPPLIED: OFFLINEFILES_EVENTS = 33
OFFLINEFILES_EVENT_TRANSPARENTCACHEITEMNOTIFY: OFFLINEFILES_EVENTS = 34
OFFLINEFILES_EVENT_PREFETCHFILEBEGIN: OFFLINEFILES_EVENTS = 35
OFFLINEFILES_EVENT_PREFETCHFILEEND: OFFLINEFILES_EVENTS = 36
OFFLINEFILES_EVENT_PREFETCHCLOSEHANDLEBEGIN: OFFLINEFILES_EVENTS = 37
OFFLINEFILES_EVENT_PREFETCHCLOSEHANDLEEND: OFFLINEFILES_EVENTS = 38
OFFLINEFILES_NUM_EVENTS: OFFLINEFILES_EVENTS = 39
OFFLINEFILES_ITEM_COPY = Int32
OFFLINEFILES_ITEM_COPY_LOCAL: OFFLINEFILES_ITEM_COPY = 0
OFFLINEFILES_ITEM_COPY_REMOTE: OFFLINEFILES_ITEM_COPY = 1
OFFLINEFILES_ITEM_COPY_ORIGINAL: OFFLINEFILES_ITEM_COPY = 2
OFFLINEFILES_ITEM_TIME = Int32
OFFLINEFILES_ITEM_TIME_CREATION: OFFLINEFILES_ITEM_TIME = 0
OFFLINEFILES_ITEM_TIME_LASTACCESS: OFFLINEFILES_ITEM_TIME = 1
OFFLINEFILES_ITEM_TIME_LASTWRITE: OFFLINEFILES_ITEM_TIME = 2
OFFLINEFILES_ITEM_TYPE = Int32
OFFLINEFILES_ITEM_TYPE_FILE: OFFLINEFILES_ITEM_TYPE = 0
OFFLINEFILES_ITEM_TYPE_DIRECTORY: OFFLINEFILES_ITEM_TYPE = 1
OFFLINEFILES_ITEM_TYPE_SHARE: OFFLINEFILES_ITEM_TYPE = 2
OFFLINEFILES_ITEM_TYPE_SERVER: OFFLINEFILES_ITEM_TYPE = 3
OFFLINEFILES_OFFLINE_REASON = Int32
OFFLINEFILES_OFFLINE_REASON_UNKNOWN: OFFLINEFILES_OFFLINE_REASON = 0
OFFLINEFILES_OFFLINE_REASON_NOT_APPLICABLE: OFFLINEFILES_OFFLINE_REASON = 1
OFFLINEFILES_OFFLINE_REASON_CONNECTION_FORCED: OFFLINEFILES_OFFLINE_REASON = 2
OFFLINEFILES_OFFLINE_REASON_CONNECTION_SLOW: OFFLINEFILES_OFFLINE_REASON = 3
OFFLINEFILES_OFFLINE_REASON_CONNECTION_ERROR: OFFLINEFILES_OFFLINE_REASON = 4
OFFLINEFILES_OFFLINE_REASON_ITEM_VERSION_CONFLICT: OFFLINEFILES_OFFLINE_REASON = 5
OFFLINEFILES_OFFLINE_REASON_ITEM_SUSPENDED: OFFLINEFILES_OFFLINE_REASON = 6
OFFLINEFILES_OP_RESPONSE = Int32
OFFLINEFILES_OP_CONTINUE: OFFLINEFILES_OP_RESPONSE = 0
OFFLINEFILES_OP_RETRY: OFFLINEFILES_OP_RESPONSE = 1
OFFLINEFILES_OP_ABORT: OFFLINEFILES_OP_RESPONSE = 2
OFFLINEFILES_PATHFILTER_MATCH = Int32
OFFLINEFILES_PATHFILTER_SELF: OFFLINEFILES_PATHFILTER_MATCH = 0
OFFLINEFILES_PATHFILTER_CHILD: OFFLINEFILES_PATHFILTER_MATCH = 1
OFFLINEFILES_PATHFILTER_DESCENDENT: OFFLINEFILES_PATHFILTER_MATCH = 2
OFFLINEFILES_PATHFILTER_SELFORCHILD: OFFLINEFILES_PATHFILTER_MATCH = 3
OFFLINEFILES_PATHFILTER_SELFORDESCENDENT: OFFLINEFILES_PATHFILTER_MATCH = 4
OFFLINEFILES_SETTING_VALUE_TYPE = Int32
OFFLINEFILES_SETTING_VALUE_UI4: OFFLINEFILES_SETTING_VALUE_TYPE = 0
OFFLINEFILES_SETTING_VALUE_BSTR: OFFLINEFILES_SETTING_VALUE_TYPE = 1
OFFLINEFILES_SETTING_VALUE_BSTR_DBLNULTERM: OFFLINEFILES_SETTING_VALUE_TYPE = 2
OFFLINEFILES_SETTING_VALUE_2DIM_ARRAY_BSTR_UI4: OFFLINEFILES_SETTING_VALUE_TYPE = 3
OFFLINEFILES_SETTING_VALUE_2DIM_ARRAY_BSTR_BSTR: OFFLINEFILES_SETTING_VALUE_TYPE = 4
OFFLINEFILES_SYNC_CONFLICT_RESOLVE = Int32
OFFLINEFILES_SYNC_CONFLICT_RESOLVE_NONE: OFFLINEFILES_SYNC_CONFLICT_RESOLVE = 0
OFFLINEFILES_SYNC_CONFLICT_RESOLVE_KEEPLOCAL: OFFLINEFILES_SYNC_CONFLICT_RESOLVE = 1
OFFLINEFILES_SYNC_CONFLICT_RESOLVE_KEEPREMOTE: OFFLINEFILES_SYNC_CONFLICT_RESOLVE = 2
OFFLINEFILES_SYNC_CONFLICT_RESOLVE_KEEPALLCHANGES: OFFLINEFILES_SYNC_CONFLICT_RESOLVE = 3
OFFLINEFILES_SYNC_CONFLICT_RESOLVE_KEEPLATEST: OFFLINEFILES_SYNC_CONFLICT_RESOLVE = 4
OFFLINEFILES_SYNC_CONFLICT_RESOLVE_LOG: OFFLINEFILES_SYNC_CONFLICT_RESOLVE = 5
OFFLINEFILES_SYNC_CONFLICT_RESOLVE_SKIP: OFFLINEFILES_SYNC_CONFLICT_RESOLVE = 6
OFFLINEFILES_SYNC_CONFLICT_ABORT: OFFLINEFILES_SYNC_CONFLICT_RESOLVE = 7
OFFLINEFILES_SYNC_CONFLICT_RESOLVE_NUMCODES: OFFLINEFILES_SYNC_CONFLICT_RESOLVE = 8
OFFLINEFILES_SYNC_OPERATION = Int32
OFFLINEFILES_SYNC_OPERATION_CREATE_COPY_ON_SERVER: OFFLINEFILES_SYNC_OPERATION = 0
OFFLINEFILES_SYNC_OPERATION_CREATE_COPY_ON_CLIENT: OFFLINEFILES_SYNC_OPERATION = 1
OFFLINEFILES_SYNC_OPERATION_SYNC_TO_SERVER: OFFLINEFILES_SYNC_OPERATION = 2
OFFLINEFILES_SYNC_OPERATION_SYNC_TO_CLIENT: OFFLINEFILES_SYNC_OPERATION = 3
OFFLINEFILES_SYNC_OPERATION_DELETE_SERVER_COPY: OFFLINEFILES_SYNC_OPERATION = 4
OFFLINEFILES_SYNC_OPERATION_DELETE_CLIENT_COPY: OFFLINEFILES_SYNC_OPERATION = 5
OFFLINEFILES_SYNC_OPERATION_PIN: OFFLINEFILES_SYNC_OPERATION = 6
OFFLINEFILES_SYNC_OPERATION_PREPARE: OFFLINEFILES_SYNC_OPERATION = 7
OFFLINEFILES_SYNC_STATE = Int32
OFFLINEFILES_SYNC_STATE_Stable: OFFLINEFILES_SYNC_STATE = 0
OFFLINEFILES_SYNC_STATE_FileOnClient_DirOnServer: OFFLINEFILES_SYNC_STATE = 1
OFFLINEFILES_SYNC_STATE_FileOnClient_NoServerCopy: OFFLINEFILES_SYNC_STATE = 2
OFFLINEFILES_SYNC_STATE_DirOnClient_FileOnServer: OFFLINEFILES_SYNC_STATE = 3
OFFLINEFILES_SYNC_STATE_DirOnClient_FileChangedOnServer: OFFLINEFILES_SYNC_STATE = 4
OFFLINEFILES_SYNC_STATE_DirOnClient_NoServerCopy: OFFLINEFILES_SYNC_STATE = 5
OFFLINEFILES_SYNC_STATE_FileCreatedOnClient_NoServerCopy: OFFLINEFILES_SYNC_STATE = 6
OFFLINEFILES_SYNC_STATE_FileCreatedOnClient_FileChangedOnServer: OFFLINEFILES_SYNC_STATE = 7
OFFLINEFILES_SYNC_STATE_FileCreatedOnClient_DirChangedOnServer: OFFLINEFILES_SYNC_STATE = 8
OFFLINEFILES_SYNC_STATE_FileCreatedOnClient_FileOnServer: OFFLINEFILES_SYNC_STATE = 9
OFFLINEFILES_SYNC_STATE_FileCreatedOnClient_DirOnServer: OFFLINEFILES_SYNC_STATE = 10
OFFLINEFILES_SYNC_STATE_FileCreatedOnClient_DeletedOnServer: OFFLINEFILES_SYNC_STATE = 11
OFFLINEFILES_SYNC_STATE_FileChangedOnClient_ChangedOnServer: OFFLINEFILES_SYNC_STATE = 12
OFFLINEFILES_SYNC_STATE_FileChangedOnClient_DirOnServer: OFFLINEFILES_SYNC_STATE = 13
OFFLINEFILES_SYNC_STATE_FileChangedOnClient_DirChangedOnServer: OFFLINEFILES_SYNC_STATE = 14
OFFLINEFILES_SYNC_STATE_FileChangedOnClient_DeletedOnServer: OFFLINEFILES_SYNC_STATE = 15
OFFLINEFILES_SYNC_STATE_FileSparseOnClient_ChangedOnServer: OFFLINEFILES_SYNC_STATE = 16
OFFLINEFILES_SYNC_STATE_FileSparseOnClient_DeletedOnServer: OFFLINEFILES_SYNC_STATE = 17
OFFLINEFILES_SYNC_STATE_FileSparseOnClient_DirOnServer: OFFLINEFILES_SYNC_STATE = 18
OFFLINEFILES_SYNC_STATE_FileSparseOnClient_DirChangedOnServer: OFFLINEFILES_SYNC_STATE = 19
OFFLINEFILES_SYNC_STATE_DirCreatedOnClient_NoServerCopy: OFFLINEFILES_SYNC_STATE = 20
OFFLINEFILES_SYNC_STATE_DirCreatedOnClient_DirOnServer: OFFLINEFILES_SYNC_STATE = 21
OFFLINEFILES_SYNC_STATE_DirCreatedOnClient_FileOnServer: OFFLINEFILES_SYNC_STATE = 22
OFFLINEFILES_SYNC_STATE_DirCreatedOnClient_FileChangedOnServer: OFFLINEFILES_SYNC_STATE = 23
OFFLINEFILES_SYNC_STATE_DirCreatedOnClient_DirChangedOnServer: OFFLINEFILES_SYNC_STATE = 24
OFFLINEFILES_SYNC_STATE_DirCreatedOnClient_DeletedOnServer: OFFLINEFILES_SYNC_STATE = 25
OFFLINEFILES_SYNC_STATE_DirChangedOnClient_FileOnServer: OFFLINEFILES_SYNC_STATE = 26
OFFLINEFILES_SYNC_STATE_DirChangedOnClient_FileChangedOnServer: OFFLINEFILES_SYNC_STATE = 27
OFFLINEFILES_SYNC_STATE_DirChangedOnClient_ChangedOnServer: OFFLINEFILES_SYNC_STATE = 28
OFFLINEFILES_SYNC_STATE_DirChangedOnClient_DeletedOnServer: OFFLINEFILES_SYNC_STATE = 29
OFFLINEFILES_SYNC_STATE_NoClientCopy_FileOnServer: OFFLINEFILES_SYNC_STATE = 30
OFFLINEFILES_SYNC_STATE_NoClientCopy_DirOnServer: OFFLINEFILES_SYNC_STATE = 31
OFFLINEFILES_SYNC_STATE_NoClientCopy_FileChangedOnServer: OFFLINEFILES_SYNC_STATE = 32
OFFLINEFILES_SYNC_STATE_NoClientCopy_DirChangedOnServer: OFFLINEFILES_SYNC_STATE = 33
OFFLINEFILES_SYNC_STATE_DeletedOnClient_FileOnServer: OFFLINEFILES_SYNC_STATE = 34
OFFLINEFILES_SYNC_STATE_DeletedOnClient_DirOnServer: OFFLINEFILES_SYNC_STATE = 35
OFFLINEFILES_SYNC_STATE_DeletedOnClient_FileChangedOnServer: OFFLINEFILES_SYNC_STATE = 36
OFFLINEFILES_SYNC_STATE_DeletedOnClient_DirChangedOnServer: OFFLINEFILES_SYNC_STATE = 37
OFFLINEFILES_SYNC_STATE_FileSparseOnClient: OFFLINEFILES_SYNC_STATE = 38
OFFLINEFILES_SYNC_STATE_FileChangedOnClient: OFFLINEFILES_SYNC_STATE = 39
OFFLINEFILES_SYNC_STATE_FileRenamedOnClient: OFFLINEFILES_SYNC_STATE = 40
OFFLINEFILES_SYNC_STATE_DirSparseOnClient: OFFLINEFILES_SYNC_STATE = 41
OFFLINEFILES_SYNC_STATE_DirChangedOnClient: OFFLINEFILES_SYNC_STATE = 42
OFFLINEFILES_SYNC_STATE_DirRenamedOnClient: OFFLINEFILES_SYNC_STATE = 43
OFFLINEFILES_SYNC_STATE_FileChangedOnServer: OFFLINEFILES_SYNC_STATE = 44
OFFLINEFILES_SYNC_STATE_FileRenamedOnServer: OFFLINEFILES_SYNC_STATE = 45
OFFLINEFILES_SYNC_STATE_FileDeletedOnServer: OFFLINEFILES_SYNC_STATE = 46
OFFLINEFILES_SYNC_STATE_DirChangedOnServer: OFFLINEFILES_SYNC_STATE = 47
OFFLINEFILES_SYNC_STATE_DirRenamedOnServer: OFFLINEFILES_SYNC_STATE = 48
OFFLINEFILES_SYNC_STATE_DirDeletedOnServer: OFFLINEFILES_SYNC_STATE = 49
OFFLINEFILES_SYNC_STATE_FileReplacedAndDeletedOnClient_FileOnServer: OFFLINEFILES_SYNC_STATE = 50
OFFLINEFILES_SYNC_STATE_FileReplacedAndDeletedOnClient_FileChangedOnServer: OFFLINEFILES_SYNC_STATE = 51
OFFLINEFILES_SYNC_STATE_FileReplacedAndDeletedOnClient_DirOnServer: OFFLINEFILES_SYNC_STATE = 52
OFFLINEFILES_SYNC_STATE_FileReplacedAndDeletedOnClient_DirChangedOnServer: OFFLINEFILES_SYNC_STATE = 53
OFFLINEFILES_SYNC_STATE_NUMSTATES: OFFLINEFILES_SYNC_STATE = 54
OfflineFilesCache = Guid('48c6be7c-3871-43cc-b4-6f-14-49-a1-bb-2f-f3')
OfflineFilesSetting = Guid('fd3659e9-a920-4123-ad-64-7f-c7-6c-7a-ac-df')
make_head(_module, 'IEnumOfflineFilesItems')
make_head(_module, 'IEnumOfflineFilesSettings')
make_head(_module, 'IOfflineFilesCache')
make_head(_module, 'IOfflineFilesCache2')
make_head(_module, 'IOfflineFilesChangeInfo')
make_head(_module, 'IOfflineFilesConnectionInfo')
make_head(_module, 'IOfflineFilesDirectoryItem')
make_head(_module, 'IOfflineFilesDirtyInfo')
make_head(_module, 'IOfflineFilesErrorInfo')
make_head(_module, 'IOfflineFilesEvents')
make_head(_module, 'IOfflineFilesEvents2')
make_head(_module, 'IOfflineFilesEvents3')
make_head(_module, 'IOfflineFilesEvents4')
make_head(_module, 'IOfflineFilesEventsFilter')
make_head(_module, 'IOfflineFilesFileItem')
make_head(_module, 'IOfflineFilesFileSysInfo')
make_head(_module, 'IOfflineFilesGhostInfo')
make_head(_module, 'IOfflineFilesItem')
make_head(_module, 'IOfflineFilesItemContainer')
make_head(_module, 'IOfflineFilesItemFilter')
make_head(_module, 'IOfflineFilesPinInfo')
make_head(_module, 'IOfflineFilesPinInfo2')
make_head(_module, 'IOfflineFilesProgress')
make_head(_module, 'IOfflineFilesServerItem')
make_head(_module, 'IOfflineFilesSetting')
make_head(_module, 'IOfflineFilesShareInfo')
make_head(_module, 'IOfflineFilesShareItem')
make_head(_module, 'IOfflineFilesSimpleProgress')
make_head(_module, 'IOfflineFilesSuspend')
make_head(_module, 'IOfflineFilesSuspendInfo')
make_head(_module, 'IOfflineFilesSyncConflictHandler')
make_head(_module, 'IOfflineFilesSyncErrorInfo')
make_head(_module, 'IOfflineFilesSyncErrorItemInfo')
make_head(_module, 'IOfflineFilesSyncProgress')
make_head(_module, 'IOfflineFilesTransparentCacheInfo')
