from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Storage.OfflineFiles
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Variant
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
def OfflineFilesEnable(bEnable: win32more.Windows.Win32.Foundation.BOOL, pbRebootRequired: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> UInt32: ...
@winfunctype('CSCAPI.dll')
def OfflineFilesStart() -> UInt32: ...
@winfunctype('CSCAPI.dll')
def OfflineFilesQueryStatus(pbActive: POINTER(win32more.Windows.Win32.Foundation.BOOL), pbEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> UInt32: ...
@winfunctype('CSCAPI.dll')
def OfflineFilesQueryStatusEx(pbActive: POINTER(win32more.Windows.Win32.Foundation.BOOL), pbEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL), pbAvailable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> UInt32: ...
class IEnumOfflineFilesItems(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{da70e815-c361-4407-bc0b-0d7046e5f2cd}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesItem), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.IEnumOfflineFilesItems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumOfflineFilesSettings(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{729680c4-1a38-47bc-9e5c-02c51562ac30}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesSetting), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.IEnumOfflineFilesSettings)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesCache(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{855d6203-7914-48b9-8d40-4c56f5acffc5}')
    @commethod(3)
    def Synchronize(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, rgpszPaths: POINTER(win32more.Windows.Win32.Foundation.PWSTR), cPaths: UInt32, bAsync: win32more.Windows.Win32.Foundation.BOOL, dwSyncControl: UInt32, pISyncConflictHandler: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesSyncConflictHandler, pIProgress: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesSyncProgress, pSyncId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DeleteItems(self, rgpszPaths: POINTER(win32more.Windows.Win32.Foundation.PWSTR), cPaths: UInt32, dwFlags: UInt32, bAsync: win32more.Windows.Win32.Foundation.BOOL, pIProgress: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesSimpleProgress) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DeleteItemsForUser(self, pszUser: win32more.Windows.Win32.Foundation.PWSTR, rgpszPaths: POINTER(win32more.Windows.Win32.Foundation.PWSTR), cPaths: UInt32, dwFlags: UInt32, bAsync: win32more.Windows.Win32.Foundation.BOOL, pIProgress: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesSimpleProgress) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Pin(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, rgpszPaths: POINTER(win32more.Windows.Win32.Foundation.PWSTR), cPaths: UInt32, bDeep: win32more.Windows.Win32.Foundation.BOOL, bAsync: win32more.Windows.Win32.Foundation.BOOL, dwPinControlFlags: UInt32, pIProgress: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesSyncProgress) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Unpin(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, rgpszPaths: POINTER(win32more.Windows.Win32.Foundation.PWSTR), cPaths: UInt32, bDeep: win32more.Windows.Win32.Foundation.BOOL, bAsync: win32more.Windows.Win32.Foundation.BOOL, dwPinControlFlags: UInt32, pIProgress: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesSyncProgress) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetEncryptionStatus(self, pbEncrypted: POINTER(win32more.Windows.Win32.Foundation.BOOL), pbPartial: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Encrypt(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, bEncrypt: win32more.Windows.Win32.Foundation.BOOL, dwEncryptionControlFlags: UInt32, bAsync: win32more.Windows.Win32.Foundation.BOOL, pIProgress: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesSyncProgress) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def FindItem(self, pszPath: win32more.Windows.Win32.Foundation.PWSTR, dwQueryFlags: UInt32, ppItem: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def FindItemEx(self, pszPath: win32more.Windows.Win32.Foundation.PWSTR, pIncludeFileFilter: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesItemFilter, pIncludeDirFilter: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesItemFilter, pExcludeFileFilter: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesItemFilter, pExcludeDirFilter: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesItemFilter, dwQueryFlags: UInt32, ppItem: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RenameItem(self, pszPathOriginal: win32more.Windows.Win32.Foundation.PWSTR, pszPathNew: win32more.Windows.Win32.Foundation.PWSTR, bReplaceIfExists: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetLocation(self, ppszPath: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetDiskSpaceInformation(self, pcbVolumeTotal: POINTER(UInt64), pcbLimit: POINTER(UInt64), pcbUsed: POINTER(UInt64), pcbUnpinnedLimit: POINTER(UInt64), pcbUnpinnedUsed: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetDiskSpaceLimits(self, cbLimit: UInt64, cbUnpinnedLimit: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def ProcessAdminPinPolicy(self, pPinProgress: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesSyncProgress, pUnpinProgress: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesSyncProgress) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetSettingObject(self, pszSettingName: win32more.Windows.Win32.Foundation.PWSTR, ppSetting: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesSetting)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def EnumSettingObjects(self, ppEnum: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.IEnumOfflineFilesSettings)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def IsPathCacheable(self, pszPath: win32more.Windows.Win32.Foundation.PWSTR, pbCacheable: POINTER(win32more.Windows.Win32.Foundation.BOOL), pShareCachingMode: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_CACHING_MODE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesCache2(ComPtr):
    extends: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesCache
    _iid_ = Guid('{8c075039-1551-4ed9-8781-56705c04d3c0}')
    @commethod(20)
    def RenameItemEx(self, pszPathOriginal: win32more.Windows.Win32.Foundation.PWSTR, pszPathNew: win32more.Windows.Win32.Foundation.PWSTR, bReplaceIfExists: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesChangeInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a96e6fa4-e0d1-4c29-960b-ee508fe68c72}')
    @commethod(3)
    def IsDirty(self, pbDirty: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsDeletedOffline(self, pbDeletedOffline: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsCreatedOffline(self, pbCreatedOffline: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsLocallyModifiedData(self, pbLocallyModifiedData: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsLocallyModifiedAttributes(self, pbLocallyModifiedAttributes: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsLocallyModifiedTime(self, pbLocallyModifiedTime: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesConnectionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{efb23a09-a867-4be8-83a6-86969a7d0856}')
    @commethod(3)
    def GetConnectState(self, pConnectState: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_CONNECT_STATE), pOfflineReason: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_OFFLINE_REASON)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetConnectState(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, dwFlags: UInt32, ConnectState: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_CONNECT_STATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def TransitionOnline(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def TransitionOffline(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, dwFlags: UInt32, bForceOpenFilesClosed: win32more.Windows.Win32.Foundation.BOOL, pbOpenFilesPreventedTransition: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesDirectoryItem(ComPtr):
    extends: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesItem
    _iid_ = Guid('{2273597a-a08c-4a00-a37a-c1ae4e9a1cfd}')
class IOfflineFilesDirtyInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0f50ce33-bac9-4eaa-a11d-da0e527d047d}')
    @commethod(3)
    def LocalDirtyByteCount(self, pDirtyByteCount: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoteDirtyByteCount(self, pDirtyByteCount: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesErrorInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7112fa5f-7571-435a-8eb7-195c7c1429bc}')
    @commethod(3)
    def GetRawData(self, ppBlob: POINTER(POINTER(win32more.Windows.Win32.System.Com.BYTE_BLOB))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDescription(self, ppszDescription: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e25585c1-0caa-4eb1-873b-1cae5b77c314}')
    @commethod(3)
    def CacheMoved(self, pszOldPath: win32more.Windows.Win32.Foundation.PWSTR, pszNewPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CacheIsFull(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CacheIsCorrupted(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Enabled(self, bEnabled: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EncryptionChanged(self, bWasEncrypted: win32more.Windows.Win32.Foundation.BOOL, bWasPartial: win32more.Windows.Win32.Foundation.BOOL, bIsEncrypted: win32more.Windows.Win32.Foundation.BOOL, bIsPartial: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SyncBegin(self, rSyncId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SyncFileResult(self, rSyncId: POINTER(Guid), pszFile: win32more.Windows.Win32.Foundation.PWSTR, hrResult: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SyncConflictRecAdded(self, pszConflictPath: win32more.Windows.Win32.Foundation.PWSTR, pftConflictDateTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), ConflictSyncState: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SyncConflictRecUpdated(self, pszConflictPath: win32more.Windows.Win32.Foundation.PWSTR, pftConflictDateTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), ConflictSyncState: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SyncConflictRecRemoved(self, pszConflictPath: win32more.Windows.Win32.Foundation.PWSTR, pftConflictDateTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), ConflictSyncState: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SyncEnd(self, rSyncId: POINTER(Guid), hrResult: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def NetTransportArrived(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def NoNetTransports(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def ItemDisconnected(self, pszPath: win32more.Windows.Win32.Foundation.PWSTR, ItemType: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def ItemReconnected(self, pszPath: win32more.Windows.Win32.Foundation.PWSTR, ItemType: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def ItemAvailableOffline(self, pszPath: win32more.Windows.Win32.Foundation.PWSTR, ItemType: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ItemNotAvailableOffline(self, pszPath: win32more.Windows.Win32.Foundation.PWSTR, ItemType: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def ItemPinned(self, pszPath: win32more.Windows.Win32.Foundation.PWSTR, ItemType: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def ItemNotPinned(self, pszPath: win32more.Windows.Win32.Foundation.PWSTR, ItemType: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def ItemModified(self, pszPath: win32more.Windows.Win32.Foundation.PWSTR, ItemType: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE, bModifiedData: win32more.Windows.Win32.Foundation.BOOL, bModifiedAttributes: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def ItemAddedToCache(self, pszPath: win32more.Windows.Win32.Foundation.PWSTR, ItemType: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def ItemDeletedFromCache(self, pszPath: win32more.Windows.Win32.Foundation.PWSTR, ItemType: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def ItemRenamed(self, pszOldPath: win32more.Windows.Win32.Foundation.PWSTR, pszNewPath: win32more.Windows.Win32.Foundation.PWSTR, ItemType: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def DataLost(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def Ping(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesEvents2(ComPtr):
    extends: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesEvents
    _iid_ = Guid('{1ead8f56-ff76-4faa-a795-6f6ef792498b}')
    @commethod(28)
    def ItemReconnectBegin(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def ItemReconnectEnd(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def CacheEvictBegin(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def CacheEvictEnd(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def BackgroundSyncBegin(self, dwSyncControlFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def BackgroundSyncEnd(self, dwSyncControlFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def PolicyChangeDetected(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def PreferenceChangeDetected(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def SettingsChangesApplied(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesEvents3(ComPtr):
    extends: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesEvents2
    _iid_ = Guid('{9ba04a45-ee69-42f0-9ab1-7db5c8805808}')
    @commethod(37)
    def TransparentCacheItemNotify(self, pszPath: win32more.Windows.Win32.Foundation.PWSTR, EventType: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS, ItemType: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE, bModifiedData: win32more.Windows.Win32.Foundation.BOOL, bModifiedAttributes: win32more.Windows.Win32.Foundation.BOOL, pzsOldPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def PrefetchFileBegin(self, pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def PrefetchFileEnd(self, pszPath: win32more.Windows.Win32.Foundation.PWSTR, hrResult: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesEvents4(ComPtr):
    extends: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesEvents3
    _iid_ = Guid('{dbd69b1e-c7d2-473e-b35f-9d8c24c0c484}')
    @commethod(40)
    def PrefetchCloseHandleBegin(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def PrefetchCloseHandleEnd(self, dwClosedHandleCount: UInt32, dwOpenHandleCount: UInt32, hrResult: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesEventsFilter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{33fc4e1b-0716-40fa-ba65-6e62a84a846f}')
    @commethod(3)
    def GetPathFilter(self, ppszFilter: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pMatch: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_PATHFILTER_MATCH)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIncludedEvents(self, cElements: UInt32, prgEvents: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS), pcEvents: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetExcludedEvents(self, cElements: UInt32, prgEvents: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS), pcEvents: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesFileItem(ComPtr):
    extends: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesItem
    _iid_ = Guid('{8dfadead-26c2-4eff-8a72-6b50723d9a00}')
    @commethod(8)
    def IsSparse(self, pbIsSparse: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def IsEncrypted(self, pbIsEncrypted: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesFileSysInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bc1a163f-7bfd-4d88-9c66-96ea9a6a3d6b}')
    @commethod(3)
    def GetAttributes(self, copy: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_COPY, pdwAttributes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTimes(self, copy: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_COPY, pftCreationTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), pftLastWriteTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), pftChangeTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), pftLastAccessTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFileSize(self, copy: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_COPY, pSize: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesGhostInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2b09d48c-8ab5-464f-a755-a59d92f99429}')
    @commethod(3)
    def IsGhosted(self, pbGhosted: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesItem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4a753da6-e044-4f12-a718-5d14d079a906}')
    @commethod(3)
    def GetItemType(self, pItemType: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPath(self, ppszPath: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetParentItem(self, ppItem: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Refresh(self, dwQueryFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsMarkedForDeletion(self, pbMarkedForDeletion: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesItemContainer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3836f049-9413-45dd-bf46-b5aaa82dc310}')
    @commethod(3)
    def EnumItems(self, dwQueryFlags: UInt32, ppenum: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.IEnumOfflineFilesItems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumItemsEx(self, pIncludeFileFilter: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesItemFilter, pIncludeDirFilter: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesItemFilter, pExcludeFileFilter: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesItemFilter, pExcludeDirFilter: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesItemFilter, dwEnumFlags: UInt32, dwQueryFlags: UInt32, ppenum: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.IEnumOfflineFilesItems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesItemFilter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f4b5a26c-dc05-4f20-ada4-551f1077be5c}')
    @commethod(3)
    def GetFilterFlags(self, pullFlags: POINTER(UInt64), pullMask: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTimeFilter(self, pftTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), pbEvalTimeOfDay: POINTER(win32more.Windows.Win32.Foundation.BOOL), pTimeType: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TIME), pCompare: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_COMPARE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPatternFilter(self, pszPattern: win32more.Windows.Win32.Foundation.PWSTR, cchPattern: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesPinInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5b2b0655-b3fd-497d-adeb-bd156bc8355b}')
    @commethod(3)
    def IsPinned(self, pbPinned: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsPinnedForUser(self, pbPinnedForUser: POINTER(win32more.Windows.Win32.Foundation.BOOL), pbInherit: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsPinnedForUserByPolicy(self, pbPinnedForUser: POINTER(win32more.Windows.Win32.Foundation.BOOL), pbInherit: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsPinnedForComputer(self, pbPinnedForComputer: POINTER(win32more.Windows.Win32.Foundation.BOOL), pbInherit: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsPinnedForFolderRedirection(self, pbPinnedForFolderRedirection: POINTER(win32more.Windows.Win32.Foundation.BOOL), pbInherit: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesPinInfo2(ComPtr):
    extends: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesPinInfo
    _iid_ = Guid('{623c58a2-42ed-4ad7-b69a-0f1b30a72d0d}')
    @commethod(8)
    def IsPartlyPinned(self, pbPartlyPinned: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesProgress(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fad63237-c55b-4911-9850-bcf96d4c979e}')
    @commethod(3)
    def Begin(self, pbAbort: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def QueryAbort(self, pbAbort: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def End(self, hrResult: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesServerItem(ComPtr):
    extends: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesItem
    _iid_ = Guid('{9b1c9576-a92b-4151-8e9e-7c7b3ec2e016}')
class IOfflineFilesSetting(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d871d3f7-f613-48a1-827e-7a34e560fff6}')
    @commethod(3)
    def GetName(self, ppszName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetValueType(self, pType: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SETTING_VALUE_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPreference(self, pvarValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), dwScope: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPreferenceScope(self, pdwScope: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetPreference(self, pvarValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), dwScope: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DeletePreference(self, dwScope: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPolicy(self, pvarValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), dwScope: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetPolicyScope(self, pdwScope: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetValue(self, pvarValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pbSetByPolicy: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesShareInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7bcc43e7-31ce-4ca4-8ccd-1cff2dc494da}')
    @commethod(3)
    def GetShareItem(self, ppShareItem: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesShareItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetShareCachingMode(self, pCachingMode: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_CACHING_MODE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsShareDfsJunction(self, pbIsDfsJunction: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesShareItem(ComPtr):
    extends: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesItem
    _iid_ = Guid('{bab7e48d-4804-41b5-a44d-0f199b06b145}')
class IOfflineFilesSimpleProgress(ComPtr):
    extends: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesProgress
    _iid_ = Guid('{c34f7f9b-c43d-4f9d-a776-c0eb6de5d401}')
    @commethod(6)
    def ItemBegin(self, pszFile: win32more.Windows.Win32.Foundation.PWSTR, pResponse: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_OP_RESPONSE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ItemResult(self, pszFile: win32more.Windows.Win32.Foundation.PWSTR, hrResult: win32more.Windows.Win32.Foundation.HRESULT, pResponse: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_OP_RESPONSE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesSuspend(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{62c4560f-bc0b-48ca-ad9d-34cb528d99a9}')
    @commethod(3)
    def SuspendRoot(self, bSuspend: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesSuspendInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a457c25b-4e9c-4b04-85af-8932ccd97889}')
    @commethod(3)
    def IsSuspended(self, pbSuspended: POINTER(win32more.Windows.Win32.Foundation.BOOL), pbSuspendedRoot: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesSyncConflictHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b6dd5092-c65c-46b6-97b8-fadd08e7e1be}')
    @commethod(3)
    def ResolveConflict(self, pszPath: win32more.Windows.Win32.Foundation.PWSTR, fStateKnown: UInt32, state: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE, fChangeDetails: UInt32, pConflictResolution: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_CONFLICT_RESOLVE), ppszNewName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesSyncErrorInfo(ComPtr):
    extends: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesErrorInfo
    _iid_ = Guid('{59f95e46-eb54-49d1-be76-de95458d01b0}')
    @commethod(5)
    def GetSyncOperation(self, pSyncOp: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_OPERATION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetItemChangeFlags(self, pdwItemChangeFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def InfoEnumerated(self, pbLocalEnumerated: POINTER(win32more.Windows.Win32.Foundation.BOOL), pbRemoteEnumerated: POINTER(win32more.Windows.Win32.Foundation.BOOL), pbOriginalEnumerated: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def InfoAvailable(self, pbLocalInfo: POINTER(win32more.Windows.Win32.Foundation.BOOL), pbRemoteInfo: POINTER(win32more.Windows.Win32.Foundation.BOOL), pbOriginalInfo: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetLocalInfo(self, ppInfo: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesSyncErrorItemInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRemoteInfo(self, ppInfo: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesSyncErrorItemInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetOriginalInfo(self, ppInfo: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesSyncErrorItemInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesSyncErrorItemInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ecdbaf0d-6a18-4d55-8017-108f7660ba44}')
    @commethod(3)
    def GetFileAttributes(self, pdwAttributes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFileTimes(self, pftLastWrite: POINTER(win32more.Windows.Win32.Foundation.FILETIME), pftChange: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFileSize(self, pSize: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesSyncProgress(ComPtr):
    extends: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesProgress
    _iid_ = Guid('{6931f49a-6fc7-4c1b-b265-56793fc451b7}')
    @commethod(6)
    def SyncItemBegin(self, pszFile: win32more.Windows.Win32.Foundation.PWSTR, pResponse: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_OP_RESPONSE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SyncItemResult(self, pszFile: win32more.Windows.Win32.Foundation.PWSTR, hrResult: win32more.Windows.Win32.Foundation.HRESULT, pErrorInfo: win32more.Windows.Win32.Storage.OfflineFiles.IOfflineFilesSyncErrorInfo, pResponse: POINTER(win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_OP_RESPONSE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOfflineFilesTransparentCacheInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bcaf4a01-5b68-4b56-a6a1-8d2786ede8e3}')
    @commethod(3)
    def IsTransparentlyCached(self, pbTransparentlyCached: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
OFFLINEFILES_CACHING_MODE = Int32
OFFLINEFILES_CACHING_MODE_NONE: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_CACHING_MODE = 0
OFFLINEFILES_CACHING_MODE_NOCACHING: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_CACHING_MODE = 1
OFFLINEFILES_CACHING_MODE_MANUAL: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_CACHING_MODE = 2
OFFLINEFILES_CACHING_MODE_AUTO_DOC: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_CACHING_MODE = 3
OFFLINEFILES_CACHING_MODE_AUTO_PROGANDDOC: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_CACHING_MODE = 4
OFFLINEFILES_COMPARE = Int32
OFFLINEFILES_COMPARE_EQ: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_COMPARE = 0
OFFLINEFILES_COMPARE_NEQ: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_COMPARE = 1
OFFLINEFILES_COMPARE_LT: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_COMPARE = 2
OFFLINEFILES_COMPARE_GT: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_COMPARE = 3
OFFLINEFILES_COMPARE_LTE: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_COMPARE = 4
OFFLINEFILES_COMPARE_GTE: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_COMPARE = 5
OFFLINEFILES_CONNECT_STATE = Int32
OFFLINEFILES_CONNECT_STATE_UNKNOWN: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_CONNECT_STATE = 0
OFFLINEFILES_CONNECT_STATE_OFFLINE: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_CONNECT_STATE = 1
OFFLINEFILES_CONNECT_STATE_ONLINE: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_CONNECT_STATE = 2
OFFLINEFILES_CONNECT_STATE_TRANSPARENTLY_CACHED: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_CONNECT_STATE = 3
OFFLINEFILES_CONNECT_STATE_PARTLY_TRANSPARENTLY_CACHED: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_CONNECT_STATE = 4
OFFLINEFILES_EVENTS = Int32
OFFLINEFILES_EVENT_CACHEMOVED: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 0
OFFLINEFILES_EVENT_CACHEISFULL: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 1
OFFLINEFILES_EVENT_CACHEISCORRUPTED: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 2
OFFLINEFILES_EVENT_ENABLED: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 3
OFFLINEFILES_EVENT_ENCRYPTIONCHANGED: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 4
OFFLINEFILES_EVENT_SYNCBEGIN: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 5
OFFLINEFILES_EVENT_SYNCFILERESULT: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 6
OFFLINEFILES_EVENT_SYNCCONFLICTRECADDED: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 7
OFFLINEFILES_EVENT_SYNCCONFLICTRECUPDATED: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 8
OFFLINEFILES_EVENT_SYNCCONFLICTRECREMOVED: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 9
OFFLINEFILES_EVENT_SYNCEND: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 10
OFFLINEFILES_EVENT_BACKGROUNDSYNCBEGIN: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 11
OFFLINEFILES_EVENT_BACKGROUNDSYNCEND: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 12
OFFLINEFILES_EVENT_NETTRANSPORTARRIVED: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 13
OFFLINEFILES_EVENT_NONETTRANSPORTS: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 14
OFFLINEFILES_EVENT_ITEMDISCONNECTED: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 15
OFFLINEFILES_EVENT_ITEMRECONNECTED: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 16
OFFLINEFILES_EVENT_ITEMAVAILABLEOFFLINE: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 17
OFFLINEFILES_EVENT_ITEMNOTAVAILABLEOFFLINE: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 18
OFFLINEFILES_EVENT_ITEMPINNED: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 19
OFFLINEFILES_EVENT_ITEMNOTPINNED: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 20
OFFLINEFILES_EVENT_ITEMMODIFIED: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 21
OFFLINEFILES_EVENT_ITEMADDEDTOCACHE: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 22
OFFLINEFILES_EVENT_ITEMDELETEDFROMCACHE: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 23
OFFLINEFILES_EVENT_ITEMRENAMED: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 24
OFFLINEFILES_EVENT_DATALOST: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 25
OFFLINEFILES_EVENT_PING: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 26
OFFLINEFILES_EVENT_ITEMRECONNECTBEGIN: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 27
OFFLINEFILES_EVENT_ITEMRECONNECTEND: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 28
OFFLINEFILES_EVENT_CACHEEVICTBEGIN: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 29
OFFLINEFILES_EVENT_CACHEEVICTEND: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 30
OFFLINEFILES_EVENT_POLICYCHANGEDETECTED: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 31
OFFLINEFILES_EVENT_PREFERENCECHANGEDETECTED: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 32
OFFLINEFILES_EVENT_SETTINGSCHANGESAPPLIED: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 33
OFFLINEFILES_EVENT_TRANSPARENTCACHEITEMNOTIFY: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 34
OFFLINEFILES_EVENT_PREFETCHFILEBEGIN: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 35
OFFLINEFILES_EVENT_PREFETCHFILEEND: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 36
OFFLINEFILES_EVENT_PREFETCHCLOSEHANDLEBEGIN: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 37
OFFLINEFILES_EVENT_PREFETCHCLOSEHANDLEEND: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 38
OFFLINEFILES_NUM_EVENTS: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_EVENTS = 39
OFFLINEFILES_ITEM_COPY = Int32
OFFLINEFILES_ITEM_COPY_LOCAL: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_COPY = 0
OFFLINEFILES_ITEM_COPY_REMOTE: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_COPY = 1
OFFLINEFILES_ITEM_COPY_ORIGINAL: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_COPY = 2
OFFLINEFILES_ITEM_TIME = Int32
OFFLINEFILES_ITEM_TIME_CREATION: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TIME = 0
OFFLINEFILES_ITEM_TIME_LASTACCESS: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TIME = 1
OFFLINEFILES_ITEM_TIME_LASTWRITE: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TIME = 2
OFFLINEFILES_ITEM_TYPE = Int32
OFFLINEFILES_ITEM_TYPE_FILE: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE = 0
OFFLINEFILES_ITEM_TYPE_DIRECTORY: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE = 1
OFFLINEFILES_ITEM_TYPE_SHARE: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE = 2
OFFLINEFILES_ITEM_TYPE_SERVER: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_ITEM_TYPE = 3
OFFLINEFILES_OFFLINE_REASON = Int32
OFFLINEFILES_OFFLINE_REASON_UNKNOWN: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_OFFLINE_REASON = 0
OFFLINEFILES_OFFLINE_REASON_NOT_APPLICABLE: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_OFFLINE_REASON = 1
OFFLINEFILES_OFFLINE_REASON_CONNECTION_FORCED: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_OFFLINE_REASON = 2
OFFLINEFILES_OFFLINE_REASON_CONNECTION_SLOW: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_OFFLINE_REASON = 3
OFFLINEFILES_OFFLINE_REASON_CONNECTION_ERROR: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_OFFLINE_REASON = 4
OFFLINEFILES_OFFLINE_REASON_ITEM_VERSION_CONFLICT: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_OFFLINE_REASON = 5
OFFLINEFILES_OFFLINE_REASON_ITEM_SUSPENDED: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_OFFLINE_REASON = 6
OFFLINEFILES_OP_RESPONSE = Int32
OFFLINEFILES_OP_CONTINUE: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_OP_RESPONSE = 0
OFFLINEFILES_OP_RETRY: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_OP_RESPONSE = 1
OFFLINEFILES_OP_ABORT: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_OP_RESPONSE = 2
OFFLINEFILES_PATHFILTER_MATCH = Int32
OFFLINEFILES_PATHFILTER_SELF: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_PATHFILTER_MATCH = 0
OFFLINEFILES_PATHFILTER_CHILD: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_PATHFILTER_MATCH = 1
OFFLINEFILES_PATHFILTER_DESCENDENT: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_PATHFILTER_MATCH = 2
OFFLINEFILES_PATHFILTER_SELFORCHILD: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_PATHFILTER_MATCH = 3
OFFLINEFILES_PATHFILTER_SELFORDESCENDENT: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_PATHFILTER_MATCH = 4
OFFLINEFILES_SETTING_VALUE_TYPE = Int32
OFFLINEFILES_SETTING_VALUE_UI4: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SETTING_VALUE_TYPE = 0
OFFLINEFILES_SETTING_VALUE_BSTR: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SETTING_VALUE_TYPE = 1
OFFLINEFILES_SETTING_VALUE_BSTR_DBLNULTERM: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SETTING_VALUE_TYPE = 2
OFFLINEFILES_SETTING_VALUE_2DIM_ARRAY_BSTR_UI4: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SETTING_VALUE_TYPE = 3
OFFLINEFILES_SETTING_VALUE_2DIM_ARRAY_BSTR_BSTR: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SETTING_VALUE_TYPE = 4
OFFLINEFILES_SYNC_CONFLICT_RESOLVE = Int32
OFFLINEFILES_SYNC_CONFLICT_RESOLVE_NONE: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_CONFLICT_RESOLVE = 0
OFFLINEFILES_SYNC_CONFLICT_RESOLVE_KEEPLOCAL: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_CONFLICT_RESOLVE = 1
OFFLINEFILES_SYNC_CONFLICT_RESOLVE_KEEPREMOTE: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_CONFLICT_RESOLVE = 2
OFFLINEFILES_SYNC_CONFLICT_RESOLVE_KEEPALLCHANGES: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_CONFLICT_RESOLVE = 3
OFFLINEFILES_SYNC_CONFLICT_RESOLVE_KEEPLATEST: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_CONFLICT_RESOLVE = 4
OFFLINEFILES_SYNC_CONFLICT_RESOLVE_LOG: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_CONFLICT_RESOLVE = 5
OFFLINEFILES_SYNC_CONFLICT_RESOLVE_SKIP: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_CONFLICT_RESOLVE = 6
OFFLINEFILES_SYNC_CONFLICT_ABORT: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_CONFLICT_RESOLVE = 7
OFFLINEFILES_SYNC_CONFLICT_RESOLVE_NUMCODES: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_CONFLICT_RESOLVE = 8
OFFLINEFILES_SYNC_OPERATION = Int32
OFFLINEFILES_SYNC_OPERATION_CREATE_COPY_ON_SERVER: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_OPERATION = 0
OFFLINEFILES_SYNC_OPERATION_CREATE_COPY_ON_CLIENT: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_OPERATION = 1
OFFLINEFILES_SYNC_OPERATION_SYNC_TO_SERVER: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_OPERATION = 2
OFFLINEFILES_SYNC_OPERATION_SYNC_TO_CLIENT: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_OPERATION = 3
OFFLINEFILES_SYNC_OPERATION_DELETE_SERVER_COPY: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_OPERATION = 4
OFFLINEFILES_SYNC_OPERATION_DELETE_CLIENT_COPY: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_OPERATION = 5
OFFLINEFILES_SYNC_OPERATION_PIN: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_OPERATION = 6
OFFLINEFILES_SYNC_OPERATION_PREPARE: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_OPERATION = 7
OFFLINEFILES_SYNC_STATE = Int32
OFFLINEFILES_SYNC_STATE_Stable: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 0
OFFLINEFILES_SYNC_STATE_FileOnClient_DirOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 1
OFFLINEFILES_SYNC_STATE_FileOnClient_NoServerCopy: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 2
OFFLINEFILES_SYNC_STATE_DirOnClient_FileOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 3
OFFLINEFILES_SYNC_STATE_DirOnClient_FileChangedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 4
OFFLINEFILES_SYNC_STATE_DirOnClient_NoServerCopy: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 5
OFFLINEFILES_SYNC_STATE_FileCreatedOnClient_NoServerCopy: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 6
OFFLINEFILES_SYNC_STATE_FileCreatedOnClient_FileChangedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 7
OFFLINEFILES_SYNC_STATE_FileCreatedOnClient_DirChangedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 8
OFFLINEFILES_SYNC_STATE_FileCreatedOnClient_FileOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 9
OFFLINEFILES_SYNC_STATE_FileCreatedOnClient_DirOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 10
OFFLINEFILES_SYNC_STATE_FileCreatedOnClient_DeletedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 11
OFFLINEFILES_SYNC_STATE_FileChangedOnClient_ChangedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 12
OFFLINEFILES_SYNC_STATE_FileChangedOnClient_DirOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 13
OFFLINEFILES_SYNC_STATE_FileChangedOnClient_DirChangedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 14
OFFLINEFILES_SYNC_STATE_FileChangedOnClient_DeletedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 15
OFFLINEFILES_SYNC_STATE_FileSparseOnClient_ChangedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 16
OFFLINEFILES_SYNC_STATE_FileSparseOnClient_DeletedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 17
OFFLINEFILES_SYNC_STATE_FileSparseOnClient_DirOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 18
OFFLINEFILES_SYNC_STATE_FileSparseOnClient_DirChangedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 19
OFFLINEFILES_SYNC_STATE_DirCreatedOnClient_NoServerCopy: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 20
OFFLINEFILES_SYNC_STATE_DirCreatedOnClient_DirOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 21
OFFLINEFILES_SYNC_STATE_DirCreatedOnClient_FileOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 22
OFFLINEFILES_SYNC_STATE_DirCreatedOnClient_FileChangedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 23
OFFLINEFILES_SYNC_STATE_DirCreatedOnClient_DirChangedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 24
OFFLINEFILES_SYNC_STATE_DirCreatedOnClient_DeletedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 25
OFFLINEFILES_SYNC_STATE_DirChangedOnClient_FileOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 26
OFFLINEFILES_SYNC_STATE_DirChangedOnClient_FileChangedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 27
OFFLINEFILES_SYNC_STATE_DirChangedOnClient_ChangedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 28
OFFLINEFILES_SYNC_STATE_DirChangedOnClient_DeletedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 29
OFFLINEFILES_SYNC_STATE_NoClientCopy_FileOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 30
OFFLINEFILES_SYNC_STATE_NoClientCopy_DirOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 31
OFFLINEFILES_SYNC_STATE_NoClientCopy_FileChangedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 32
OFFLINEFILES_SYNC_STATE_NoClientCopy_DirChangedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 33
OFFLINEFILES_SYNC_STATE_DeletedOnClient_FileOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 34
OFFLINEFILES_SYNC_STATE_DeletedOnClient_DirOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 35
OFFLINEFILES_SYNC_STATE_DeletedOnClient_FileChangedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 36
OFFLINEFILES_SYNC_STATE_DeletedOnClient_DirChangedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 37
OFFLINEFILES_SYNC_STATE_FileSparseOnClient: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 38
OFFLINEFILES_SYNC_STATE_FileChangedOnClient: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 39
OFFLINEFILES_SYNC_STATE_FileRenamedOnClient: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 40
OFFLINEFILES_SYNC_STATE_DirSparseOnClient: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 41
OFFLINEFILES_SYNC_STATE_DirChangedOnClient: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 42
OFFLINEFILES_SYNC_STATE_DirRenamedOnClient: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 43
OFFLINEFILES_SYNC_STATE_FileChangedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 44
OFFLINEFILES_SYNC_STATE_FileRenamedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 45
OFFLINEFILES_SYNC_STATE_FileDeletedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 46
OFFLINEFILES_SYNC_STATE_DirChangedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 47
OFFLINEFILES_SYNC_STATE_DirRenamedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 48
OFFLINEFILES_SYNC_STATE_DirDeletedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 49
OFFLINEFILES_SYNC_STATE_FileReplacedAndDeletedOnClient_FileOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 50
OFFLINEFILES_SYNC_STATE_FileReplacedAndDeletedOnClient_FileChangedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 51
OFFLINEFILES_SYNC_STATE_FileReplacedAndDeletedOnClient_DirOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 52
OFFLINEFILES_SYNC_STATE_FileReplacedAndDeletedOnClient_DirChangedOnServer: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 53
OFFLINEFILES_SYNC_STATE_NUMSTATES: win32more.Windows.Win32.Storage.OfflineFiles.OFFLINEFILES_SYNC_STATE = 54
OfflineFilesCache = Guid('{48c6be7c-3871-43cc-b46f-1449a1bb2ff3}')
OfflineFilesSetting = Guid('{fd3659e9-a920-4123-ad64-7fc76c7aacdf}')


make_ready(__name__)
