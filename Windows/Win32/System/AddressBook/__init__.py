from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation
import Windows.Win32.System.AddressBook
import Windows.Win32.System.Com
import Windows.Win32.System.Com.StructuredStorage
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ADRENTRY(EasyCastStructure):
    ulReserved1: UInt32
    cValues: UInt32
    rgPropVals: POINTER(Windows.Win32.System.AddressBook.SPropValue_head)
class ADRLIST(EasyCastStructure):
    cEntries: UInt32
    aEntries: Windows.Win32.System.AddressBook.ADRENTRY * 1
class ADRPARM(EasyCastStructure):
    cbABContEntryID: UInt32
    lpABContEntryID: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head)
    ulFlags: UInt32
    lpReserved: c_void_p
    ulHelpContext: UInt32
    lpszHelpFileName: POINTER(SByte)
    lpfnABSDI: Windows.Win32.System.AddressBook.LPFNABSDI
    lpfnDismiss: Windows.Win32.System.AddressBook.LPFNDISMISS
    lpvDismissContext: c_void_p
    lpszCaption: POINTER(SByte)
    lpszNewEntryTitle: POINTER(SByte)
    lpszDestWellsTitle: POINTER(SByte)
    cDestFields: UInt32
    nDestFieldFocus: UInt32
    lppszDestTitles: POINTER(POINTER(SByte))
    lpulDestComps: POINTER(UInt32)
    lpContRestriction: POINTER(Windows.Win32.System.AddressBook.SRestriction_head)
    lpHierRestriction: POINTER(Windows.Win32.System.AddressBook.SRestriction_head)
PROP_ID_SECURE_MIN: UInt32 = 26608
PROP_ID_SECURE_MAX: UInt32 = 26623
MAPI_DIM: UInt32 = 1
fMapiUnicode: UInt32 = 0
hrSuccess: UInt32 = 0
MAPI_P1: UInt32 = 268435456
MAPI_SUBMITTED: UInt32 = 2147483648
MAPI_SHORTTERM: UInt32 = 128
MAPI_NOTRECIP: UInt32 = 64
MAPI_THISSESSION: UInt32 = 32
MAPI_NOW: UInt32 = 16
MAPI_NOTRESERVED: UInt32 = 8
MAPI_COMPOUND: UInt32 = 128
cchProfileNameMax: UInt32 = 64
cchProfilePassMax: UInt32 = 64
MV_FLAG: UInt32 = 4096
PROP_ID_NULL: UInt32 = 0
PROP_ID_INVALID: UInt32 = 65535
MV_INSTANCE: UInt32 = 8192
TABLE_CHANGED: UInt32 = 1
TABLE_ERROR: UInt32 = 2
TABLE_ROW_ADDED: UInt32 = 3
TABLE_ROW_DELETED: UInt32 = 4
TABLE_ROW_MODIFIED: UInt32 = 5
TABLE_SORT_DONE: UInt32 = 6
TABLE_RESTRICT_DONE: UInt32 = 7
TABLE_SETCOL_DONE: UInt32 = 8
TABLE_RELOAD: UInt32 = 9
szMAPINotificationMsg: String = 'MAPI Notify window message'
MAPI_ERROR_VERSION: Int32 = 0
MAPI_USE_DEFAULT: UInt32 = 64
MNID_ID: UInt32 = 0
MNID_STRING: UInt32 = 1
WAB_LOCAL_CONTAINERS: UInt32 = 1048576
WAB_PROFILE_CONTENTS: UInt32 = 2097152
WAB_IGNORE_PROFILES: UInt32 = 8388608
MAPI_ONE_OFF_NO_RICH_INFO: UInt32 = 1
UI_SERVICE: UInt32 = 2
SERVICE_UI_ALWAYS: UInt32 = 2
SERVICE_UI_ALLOWED: UInt32 = 16
UI_CURRENT_PROVIDER_FIRST: UInt32 = 4
WABOBJECT_LDAPURL_RETURN_MAILUSER: UInt32 = 1
WABOBJECT_ME_NEW: UInt32 = 1
WABOBJECT_ME_NOCREATE: UInt32 = 2
WAB_VCARD_FILE: UInt32 = 0
WAB_VCARD_STREAM: UInt32 = 1
WAB_USE_OE_SENDMAIL: UInt32 = 1
WAB_ENABLE_PROFILES: UInt32 = 4194304
WAB_DISPLAY_LDAPURL: UInt32 = 1
WAB_CONTEXT_ADRLIST: UInt32 = 2
WAB_DISPLAY_ISNTDS: UInt32 = 4
WAB_DLL_NAME: String = 'WAB32.DLL'
WAB_DLL_PATH_KEY: String = 'Software\\Microsoft\\WAB\\DLLPath'
E_IMAPI_REQUEST_CANCELLED: Windows.Win32.Foundation.HRESULT = -1062600702
E_IMAPI_RECORDER_REQUIRED: Windows.Win32.Foundation.HRESULT = -1062600701
S_IMAPI_SPEEDADJUSTED: Windows.Win32.Foundation.HRESULT = 11141124
S_IMAPI_ROTATIONADJUSTED: Windows.Win32.Foundation.HRESULT = 11141125
S_IMAPI_BOTHADJUSTED: Windows.Win32.Foundation.HRESULT = 11141126
E_IMAPI_BURN_VERIFICATION_FAILED: Windows.Win32.Foundation.HRESULT = -1062600697
S_IMAPI_COMMAND_HAS_SENSE_DATA: Windows.Win32.Foundation.HRESULT = 11141632
E_IMAPI_RECORDER_NO_SUCH_MODE_PAGE: Windows.Win32.Foundation.HRESULT = -1062600191
E_IMAPI_RECORDER_MEDIA_NO_MEDIA: Windows.Win32.Foundation.HRESULT = -1062600190
E_IMAPI_RECORDER_MEDIA_INCOMPATIBLE: Windows.Win32.Foundation.HRESULT = -1062600189
E_IMAPI_RECORDER_MEDIA_UPSIDE_DOWN: Windows.Win32.Foundation.HRESULT = -1062600188
E_IMAPI_RECORDER_MEDIA_BECOMING_READY: Windows.Win32.Foundation.HRESULT = -1062600187
E_IMAPI_RECORDER_MEDIA_FORMAT_IN_PROGRESS: Windows.Win32.Foundation.HRESULT = -1062600186
E_IMAPI_RECORDER_MEDIA_BUSY: Windows.Win32.Foundation.HRESULT = -1062600185
E_IMAPI_RECORDER_INVALID_MODE_PARAMETERS: Windows.Win32.Foundation.HRESULT = -1062600184
E_IMAPI_RECORDER_MEDIA_WRITE_PROTECTED: Windows.Win32.Foundation.HRESULT = -1062600183
E_IMAPI_RECORDER_NO_SUCH_FEATURE: Windows.Win32.Foundation.HRESULT = -1062600182
E_IMAPI_RECORDER_FEATURE_IS_NOT_CURRENT: Windows.Win32.Foundation.HRESULT = -1062600181
E_IMAPI_RECORDER_GET_CONFIGURATION_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1062600180
E_IMAPI_RECORDER_COMMAND_TIMEOUT: Windows.Win32.Foundation.HRESULT = -1062600179
E_IMAPI_RECORDER_DVD_STRUCTURE_NOT_PRESENT: Windows.Win32.Foundation.HRESULT = -1062600178
E_IMAPI_RECORDER_MEDIA_SPEED_MISMATCH: Windows.Win32.Foundation.HRESULT = -1062600177
E_IMAPI_RECORDER_LOCKED: Windows.Win32.Foundation.HRESULT = -1062600176
E_IMAPI_RECORDER_CLIENT_NAME_IS_NOT_VALID: Windows.Win32.Foundation.HRESULT = -1062600175
E_IMAPI_RECORDER_MEDIA_NOT_FORMATTED: Windows.Win32.Foundation.HRESULT = -1062600174
E_IMAPI_RECORDER_INVALID_RESPONSE_FROM_DEVICE: Windows.Win32.Foundation.HRESULT = -1062599937
E_IMAPI_LOSS_OF_STREAMING: Windows.Win32.Foundation.HRESULT = -1062599936
E_IMAPI_UNEXPECTED_RESPONSE_FROM_DEVICE: Windows.Win32.Foundation.HRESULT = -1062599935
S_IMAPI_WRITE_NOT_IN_PROGRESS: Windows.Win32.Foundation.HRESULT = 11141890
E_IMAPI_DF2DATA_WRITE_IN_PROGRESS: Windows.Win32.Foundation.HRESULT = -1062599680
E_IMAPI_DF2DATA_WRITE_NOT_IN_PROGRESS: Windows.Win32.Foundation.HRESULT = -1062599679
E_IMAPI_DF2DATA_INVALID_MEDIA_STATE: Windows.Win32.Foundation.HRESULT = -1062599678
E_IMAPI_DF2DATA_STREAM_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1062599677
E_IMAPI_DF2DATA_STREAM_TOO_LARGE_FOR_CURRENT_MEDIA: Windows.Win32.Foundation.HRESULT = -1062599676
E_IMAPI_DF2DATA_MEDIA_NOT_BLANK: Windows.Win32.Foundation.HRESULT = -1062599675
E_IMAPI_DF2DATA_MEDIA_IS_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1062599674
E_IMAPI_DF2DATA_RECORDER_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1062599673
E_IMAPI_DF2DATA_CLIENT_NAME_IS_NOT_VALID: Windows.Win32.Foundation.HRESULT = -1062599672
E_IMAPI_DF2TAO_WRITE_IN_PROGRESS: Windows.Win32.Foundation.HRESULT = -1062599424
E_IMAPI_DF2TAO_WRITE_NOT_IN_PROGRESS: Windows.Win32.Foundation.HRESULT = -1062599423
E_IMAPI_DF2TAO_MEDIA_IS_NOT_PREPARED: Windows.Win32.Foundation.HRESULT = -1062599422
E_IMAPI_DF2TAO_MEDIA_IS_PREPARED: Windows.Win32.Foundation.HRESULT = -1062599421
E_IMAPI_DF2TAO_PROPERTY_FOR_BLANK_MEDIA_ONLY: Windows.Win32.Foundation.HRESULT = -1062599420
E_IMAPI_DF2TAO_TABLE_OF_CONTENTS_EMPTY_DISC: Windows.Win32.Foundation.HRESULT = -1062599419
E_IMAPI_DF2TAO_MEDIA_IS_NOT_BLANK: Windows.Win32.Foundation.HRESULT = -1062599418
E_IMAPI_DF2TAO_MEDIA_IS_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1062599417
E_IMAPI_DF2TAO_TRACK_LIMIT_REACHED: Windows.Win32.Foundation.HRESULT = -1062599416
E_IMAPI_DF2TAO_NOT_ENOUGH_SPACE: Windows.Win32.Foundation.HRESULT = -1062599415
E_IMAPI_DF2TAO_NO_RECORDER_SPECIFIED: Windows.Win32.Foundation.HRESULT = -1062599414
E_IMAPI_DF2TAO_INVALID_ISRC: Windows.Win32.Foundation.HRESULT = -1062599413
E_IMAPI_DF2TAO_INVALID_MCN: Windows.Win32.Foundation.HRESULT = -1062599412
E_IMAPI_DF2TAO_STREAM_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1062599411
E_IMAPI_DF2TAO_RECORDER_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1062599410
E_IMAPI_DF2TAO_CLIENT_NAME_IS_NOT_VALID: Windows.Win32.Foundation.HRESULT = -1062599409
E_IMAPI_DF2RAW_WRITE_IN_PROGRESS: Windows.Win32.Foundation.HRESULT = -1062599168
E_IMAPI_DF2RAW_WRITE_NOT_IN_PROGRESS: Windows.Win32.Foundation.HRESULT = -1062599167
E_IMAPI_DF2RAW_MEDIA_IS_NOT_PREPARED: Windows.Win32.Foundation.HRESULT = -1062599166
E_IMAPI_DF2RAW_MEDIA_IS_PREPARED: Windows.Win32.Foundation.HRESULT = -1062599165
E_IMAPI_DF2RAW_CLIENT_NAME_IS_NOT_VALID: Windows.Win32.Foundation.HRESULT = -1062599164
E_IMAPI_DF2RAW_MEDIA_IS_NOT_BLANK: Windows.Win32.Foundation.HRESULT = -1062599162
E_IMAPI_DF2RAW_MEDIA_IS_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1062599161
E_IMAPI_DF2RAW_NOT_ENOUGH_SPACE: Windows.Win32.Foundation.HRESULT = -1062599159
E_IMAPI_DF2RAW_NO_RECORDER_SPECIFIED: Windows.Win32.Foundation.HRESULT = -1062599158
E_IMAPI_DF2RAW_STREAM_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1062599155
E_IMAPI_DF2RAW_DATA_BLOCK_TYPE_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1062599154
E_IMAPI_DF2RAW_STREAM_LEADIN_TOO_SHORT: Windows.Win32.Foundation.HRESULT = -1062599153
E_IMAPI_DF2RAW_RECORDER_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1062599152
E_IMAPI_ERASE_RECORDER_IN_USE: Windows.Win32.Foundation.HRESULT = -2136340224
E_IMAPI_ERASE_ONLY_ONE_RECORDER_SUPPORTED: Windows.Win32.Foundation.HRESULT = -2136340223
E_IMAPI_ERASE_DISC_INFORMATION_TOO_SMALL: Windows.Win32.Foundation.HRESULT = -2136340222
E_IMAPI_ERASE_MODE_PAGE_2A_TOO_SMALL: Windows.Win32.Foundation.HRESULT = -2136340221
E_IMAPI_ERASE_MEDIA_IS_NOT_ERASABLE: Windows.Win32.Foundation.HRESULT = -2136340220
E_IMAPI_ERASE_DRIVE_FAILED_ERASE_COMMAND: Windows.Win32.Foundation.HRESULT = -2136340219
E_IMAPI_ERASE_TOOK_LONGER_THAN_ONE_HOUR: Windows.Win32.Foundation.HRESULT = -2136340218
E_IMAPI_ERASE_UNEXPECTED_DRIVE_RESPONSE_DURING_ERASE: Windows.Win32.Foundation.HRESULT = -2136340217
E_IMAPI_ERASE_DRIVE_FAILED_SPINUP_COMMAND: Windows.Win32.Foundation.HRESULT = -2136340216
E_IMAPI_ERASE_MEDIA_IS_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1062598391
E_IMAPI_ERASE_RECORDER_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1062598390
E_IMAPI_ERASE_CLIENT_NAME_IS_NOT_VALID: Windows.Win32.Foundation.HRESULT = -1062598389
E_IMAPI_RAW_IMAGE_IS_READ_ONLY: Windows.Win32.Foundation.HRESULT = -2136339968
E_IMAPI_RAW_IMAGE_TOO_MANY_TRACKS: Windows.Win32.Foundation.HRESULT = -2136339967
E_IMAPI_RAW_IMAGE_SECTOR_TYPE_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -2136339966
E_IMAPI_RAW_IMAGE_NO_TRACKS: Windows.Win32.Foundation.HRESULT = -2136339965
E_IMAPI_RAW_IMAGE_TRACKS_ALREADY_ADDED: Windows.Win32.Foundation.HRESULT = -2136339964
E_IMAPI_RAW_IMAGE_INSUFFICIENT_SPACE: Windows.Win32.Foundation.HRESULT = -2136339963
E_IMAPI_RAW_IMAGE_TOO_MANY_TRACK_INDEXES: Windows.Win32.Foundation.HRESULT = -2136339962
E_IMAPI_RAW_IMAGE_TRACK_INDEX_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -2136339961
S_IMAPI_RAW_IMAGE_TRACK_INDEX_ALREADY_EXISTS: Windows.Win32.Foundation.HRESULT = 11143688
E_IMAPI_RAW_IMAGE_TRACK_INDEX_OFFSET_ZERO_CANNOT_BE_CLEARED: Windows.Win32.Foundation.HRESULT = -2136339959
E_IMAPI_RAW_IMAGE_TRACK_INDEX_TOO_CLOSE_TO_OTHER_INDEX: Windows.Win32.Foundation.HRESULT = -2136339958
FACILITY_IMAPI2: UInt32 = 170
IMAPI_E_FSI_INTERNAL_ERROR: Windows.Win32.Foundation.HRESULT = -1062555392
IMAPI_E_INVALID_PARAM: Windows.Win32.Foundation.HRESULT = -1062555391
IMAPI_E_READONLY: Windows.Win32.Foundation.HRESULT = -1062555390
IMAPI_E_NO_OUTPUT: Windows.Win32.Foundation.HRESULT = -1062555389
IMAPI_E_INVALID_VOLUME_NAME: Windows.Win32.Foundation.HRESULT = -1062555388
IMAPI_E_INVALID_DATE: Windows.Win32.Foundation.HRESULT = -1062555387
IMAPI_E_FILE_SYSTEM_NOT_EMPTY: Windows.Win32.Foundation.HRESULT = -1062555386
IMAPI_E_NOT_FILE: Windows.Win32.Foundation.HRESULT = -1062555384
IMAPI_E_NOT_DIR: Windows.Win32.Foundation.HRESULT = -1062555383
IMAPI_E_DIR_NOT_EMPTY: Windows.Win32.Foundation.HRESULT = -1062555382
IMAPI_E_NOT_IN_FILE_SYSTEM: Windows.Win32.Foundation.HRESULT = -1062555381
IMAPI_E_INVALID_PATH: Windows.Win32.Foundation.HRESULT = -1062555376
IMAPI_E_RESTRICTED_NAME_VIOLATION: Windows.Win32.Foundation.HRESULT = -1062555375
IMAPI_E_DUP_NAME: Windows.Win32.Foundation.HRESULT = -1062555374
IMAPI_E_NO_UNIQUE_NAME: Windows.Win32.Foundation.HRESULT = -1062555373
IMAPI_E_ITEM_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -1062555368
IMAPI_E_FILE_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -1062555367
IMAPI_E_DIR_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -1062555366
IMAPI_E_IMAGE_SIZE_LIMIT: Windows.Win32.Foundation.HRESULT = -1062555360
IMAPI_E_IMAGE_TOO_BIG: Windows.Win32.Foundation.HRESULT = -1062555359
IMAPI_E_DATA_STREAM_INCONSISTENCY: Windows.Win32.Foundation.HRESULT = -1062555352
IMAPI_E_DATA_STREAM_READ_FAILURE: Windows.Win32.Foundation.HRESULT = -1062555351
IMAPI_E_DATA_STREAM_CREATE_FAILURE: Windows.Win32.Foundation.HRESULT = -1062555350
IMAPI_E_DIRECTORY_READ_FAILURE: Windows.Win32.Foundation.HRESULT = -1062555349
IMAPI_E_TOO_MANY_DIRS: Windows.Win32.Foundation.HRESULT = -1062555344
IMAPI_E_ISO9660_LEVELS: Windows.Win32.Foundation.HRESULT = -1062555343
IMAPI_E_DATA_TOO_BIG: Windows.Win32.Foundation.HRESULT = -1062555342
IMAPI_E_INCOMPATIBLE_PREVIOUS_SESSION: Windows.Win32.Foundation.HRESULT = -1062555341
IMAPI_E_STASHFILE_OPEN_FAILURE: Windows.Win32.Foundation.HRESULT = -1062555336
IMAPI_E_STASHFILE_SEEK_FAILURE: Windows.Win32.Foundation.HRESULT = -1062555335
IMAPI_E_STASHFILE_WRITE_FAILURE: Windows.Win32.Foundation.HRESULT = -1062555334
IMAPI_E_STASHFILE_READ_FAILURE: Windows.Win32.Foundation.HRESULT = -1062555333
IMAPI_E_INVALID_WORKING_DIRECTORY: Windows.Win32.Foundation.HRESULT = -1062555328
IMAPI_E_WORKING_DIRECTORY_SPACE: Windows.Win32.Foundation.HRESULT = -1062555327
IMAPI_E_STASHFILE_MOVE: Windows.Win32.Foundation.HRESULT = -1062555326
IMAPI_E_BOOT_IMAGE_DATA: Windows.Win32.Foundation.HRESULT = -1062555320
IMAPI_E_BOOT_OBJECT_CONFLICT: Windows.Win32.Foundation.HRESULT = -1062555319
IMAPI_E_BOOT_EMULATION_IMAGE_SIZE_MISMATCH: Windows.Win32.Foundation.HRESULT = -1062555318
IMAPI_E_EMPTY_DISC: Windows.Win32.Foundation.HRESULT = -1062555312
IMAPI_E_NO_SUPPORTED_FILE_SYSTEM: Windows.Win32.Foundation.HRESULT = -1062555311
IMAPI_E_FILE_SYSTEM_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -1062555310
IMAPI_E_FILE_SYSTEM_READ_CONSISTENCY_ERROR: Windows.Win32.Foundation.HRESULT = -1062555309
IMAPI_E_FILE_SYSTEM_FEATURE_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1062555308
IMAPI_E_IMPORT_TYPE_COLLISION_FILE_EXISTS_AS_DIRECTORY: Windows.Win32.Foundation.HRESULT = -1062555307
IMAPI_E_IMPORT_SEEK_FAILURE: Windows.Win32.Foundation.HRESULT = -1062555306
IMAPI_E_IMPORT_READ_FAILURE: Windows.Win32.Foundation.HRESULT = -1062555305
IMAPI_E_DISC_MISMATCH: Windows.Win32.Foundation.HRESULT = -1062555304
IMAPI_E_IMPORT_MEDIA_NOT_ALLOWED: Windows.Win32.Foundation.HRESULT = -1062555303
IMAPI_E_UDF_NOT_WRITE_COMPATIBLE: Windows.Win32.Foundation.HRESULT = -1062555302
IMAPI_E_INCOMPATIBLE_MULTISESSION_TYPE: Windows.Win32.Foundation.HRESULT = -1062555301
IMAPI_E_NO_COMPATIBLE_MULTISESSION_TYPE: Windows.Win32.Foundation.HRESULT = -1062555300
IMAPI_E_MULTISESSION_NOT_SET: Windows.Win32.Foundation.HRESULT = -1062555299
IMAPI_E_IMPORT_TYPE_COLLISION_DIRECTORY_EXISTS_AS_FILE: Windows.Win32.Foundation.HRESULT = -1062555298
IMAPI_S_IMAGE_FEATURE_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = 11186527
IMAPI_E_PROPERTY_NOT_ACCESSIBLE: Windows.Win32.Foundation.HRESULT = -1062555296
IMAPI_E_UDF_REVISION_CHANGE_NOT_ALLOWED: Windows.Win32.Foundation.HRESULT = -1062555295
IMAPI_E_BAD_MULTISESSION_PARAMETER: Windows.Win32.Foundation.HRESULT = -1062555294
IMAPI_E_FILE_SYSTEM_CHANGE_NOT_ALLOWED: Windows.Win32.Foundation.HRESULT = -1062555293
IMAPI_E_IMAGEMANAGER_IMAGE_NOT_ALIGNED: Windows.Win32.Foundation.HRESULT = -1062555136
IMAPI_E_IMAGEMANAGER_NO_VALID_VD_FOUND: Windows.Win32.Foundation.HRESULT = -1062555135
IMAPI_E_IMAGEMANAGER_NO_IMAGE: Windows.Win32.Foundation.HRESULT = -1062555134
IMAPI_E_IMAGEMANAGER_IMAGE_TOO_BIG: Windows.Win32.Foundation.HRESULT = -1062555133
MAPI_E_CALL_FAILED: Int32 = -2147467259
MAPI_E_NOT_ENOUGH_MEMORY: Int32 = -2147024882
MAPI_E_INVALID_PARAMETER: Int32 = -2147024809
MAPI_E_INTERFACE_NOT_SUPPORTED: Int32 = -2147467262
MAPI_E_NO_ACCESS: Int32 = -2147024891
TAD_ALL_ROWS: UInt32 = 1
PRILOWEST: Int32 = -32768
PRIHIGHEST: UInt32 = 32767
PRIUSER: UInt32 = 0
OPENSTREAMONFILE: String = 'OpenStreamOnFile'
szHrDispatchNotifications: String = 'HrDispatchNotifications'
szScCreateConversationIndex: String = 'ScCreateConversationIndex'
@winfunctype('rtm.dll')
def CreateTable(lpInterface: POINTER(Guid), lpAllocateBuffer: Windows.Win32.System.AddressBook.LPALLOCATEBUFFER, lpAllocateMore: Windows.Win32.System.AddressBook.LPALLOCATEMORE, lpFreeBuffer: Windows.Win32.System.AddressBook.LPFREEBUFFER, lpvReserved: c_void_p, ulTableType: UInt32, ulPropTagIndexColumn: UInt32, lpSPropTagArrayColumns: POINTER(Windows.Win32.System.AddressBook.SPropTagArray_head), lppTableData: POINTER(Windows.Win32.System.AddressBook.ITableData_head)) -> Int32: ...
@winfunctype('MAPI32.dll')
def CreateIProp(lpInterface: POINTER(Guid), lpAllocateBuffer: Windows.Win32.System.AddressBook.LPALLOCATEBUFFER, lpAllocateMore: Windows.Win32.System.AddressBook.LPALLOCATEMORE, lpFreeBuffer: Windows.Win32.System.AddressBook.LPFREEBUFFER, lpvReserved: c_void_p, lppPropData: POINTER(Windows.Win32.System.AddressBook.IPropData_head)) -> Int32: ...
@winfunctype('MAPI32.dll')
def MAPIInitIdle(lpvReserved: c_void_p) -> Int32: ...
@winfunctype('MAPI32.dll')
def MAPIDeinitIdle() -> Void: ...
@winfunctype('MAPI32.dll')
def FtgRegisterIdleRoutine(lpfnIdle: Windows.Win32.System.AddressBook.PFNIDLE, lpvIdleParam: c_void_p, priIdle: Int16, csecIdle: UInt32, iroIdle: UInt16) -> c_void_p: ...
@winfunctype('MAPI32.dll')
def DeregisterIdleRoutine(ftg: c_void_p) -> Void: ...
@winfunctype('MAPI32.dll')
def EnableIdleRoutine(ftg: c_void_p, fEnable: Windows.Win32.Foundation.BOOL) -> Void: ...
@winfunctype('MAPI32.dll')
def ChangeIdleRoutine(ftg: c_void_p, lpfnIdle: Windows.Win32.System.AddressBook.PFNIDLE, lpvIdleParam: c_void_p, priIdle: Int16, csecIdle: UInt32, iroIdle: UInt16, ircIdle: UInt16) -> Void: ...
@winfunctype('MAPI32.dll')
def MAPIGetDefaultMalloc() -> Windows.Win32.System.Com.IMalloc_head: ...
@winfunctype('MAPI32.dll')
def OpenStreamOnFile(lpAllocateBuffer: Windows.Win32.System.AddressBook.LPALLOCATEBUFFER, lpFreeBuffer: Windows.Win32.System.AddressBook.LPFREEBUFFER, ulFlags: UInt32, lpszFileName: POINTER(SByte), lpszPrefix: POINTER(SByte), lppStream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def PropCopyMore(lpSPropValueDest: POINTER(Windows.Win32.System.AddressBook.SPropValue_head), lpSPropValueSrc: POINTER(Windows.Win32.System.AddressBook.SPropValue_head), lpfAllocMore: Windows.Win32.System.AddressBook.LPALLOCATEMORE, lpvObject: c_void_p) -> Int32: ...
@winfunctype('MAPI32.dll')
def UlPropSize(lpSPropValue: POINTER(Windows.Win32.System.AddressBook.SPropValue_head)) -> UInt32: ...
@winfunctype('MAPI32.dll')
def FEqualNames(lpName1: POINTER(Windows.Win32.System.AddressBook.MAPINAMEID_head), lpName2: POINTER(Windows.Win32.System.AddressBook.MAPINAMEID_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAPI32.dll')
def FPropContainsProp(lpSPropValueDst: POINTER(Windows.Win32.System.AddressBook.SPropValue_head), lpSPropValueSrc: POINTER(Windows.Win32.System.AddressBook.SPropValue_head), ulFuzzyLevel: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAPI32.dll')
def FPropCompareProp(lpSPropValue1: POINTER(Windows.Win32.System.AddressBook.SPropValue_head), ulRelOp: UInt32, lpSPropValue2: POINTER(Windows.Win32.System.AddressBook.SPropValue_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAPI32.dll')
def LPropCompareProp(lpSPropValueA: POINTER(Windows.Win32.System.AddressBook.SPropValue_head), lpSPropValueB: POINTER(Windows.Win32.System.AddressBook.SPropValue_head)) -> Int32: ...
@winfunctype('MAPI32.dll')
def HrAddColumns(lptbl: Windows.Win32.System.AddressBook.IMAPITable_head, lpproptagColumnsNew: POINTER(Windows.Win32.System.AddressBook.SPropTagArray_head), lpAllocateBuffer: Windows.Win32.System.AddressBook.LPALLOCATEBUFFER, lpFreeBuffer: Windows.Win32.System.AddressBook.LPFREEBUFFER) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def HrAddColumnsEx(lptbl: Windows.Win32.System.AddressBook.IMAPITable_head, lpproptagColumnsNew: POINTER(Windows.Win32.System.AddressBook.SPropTagArray_head), lpAllocateBuffer: Windows.Win32.System.AddressBook.LPALLOCATEBUFFER, lpFreeBuffer: Windows.Win32.System.AddressBook.LPFREEBUFFER, lpfnFilterColumns: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def HrAllocAdviseSink(lpfnCallback: Windows.Win32.System.AddressBook.LPNOTIFCALLBACK, lpvContext: c_void_p, lppAdviseSink: POINTER(Windows.Win32.System.AddressBook.IMAPIAdviseSink_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def HrThisThreadAdviseSink(lpAdviseSink: Windows.Win32.System.AddressBook.IMAPIAdviseSink_head, lppAdviseSink: POINTER(Windows.Win32.System.AddressBook.IMAPIAdviseSink_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def HrDispatchNotifications(ulFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def BuildDisplayTable(lpAllocateBuffer: Windows.Win32.System.AddressBook.LPALLOCATEBUFFER, lpAllocateMore: Windows.Win32.System.AddressBook.LPALLOCATEMORE, lpFreeBuffer: Windows.Win32.System.AddressBook.LPFREEBUFFER, lpMalloc: Windows.Win32.System.Com.IMalloc_head, hInstance: Windows.Win32.Foundation.HMODULE, cPages: UInt32, lpPage: POINTER(Windows.Win32.System.AddressBook.DTPAGE_head), ulFlags: UInt32, lppTable: POINTER(Windows.Win32.System.AddressBook.IMAPITable_head), lppTblData: POINTER(Windows.Win32.System.AddressBook.ITableData_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def ScCountNotifications(cNotifications: Int32, lpNotifications: POINTER(Windows.Win32.System.AddressBook.NOTIFICATION_head), lpcb: POINTER(UInt32)) -> Int32: ...
@winfunctype('MAPI32.dll')
def ScCopyNotifications(cNotification: Int32, lpNotifications: POINTER(Windows.Win32.System.AddressBook.NOTIFICATION_head), lpvDst: c_void_p, lpcb: POINTER(UInt32)) -> Int32: ...
@winfunctype('MAPI32.dll')
def ScRelocNotifications(cNotification: Int32, lpNotifications: POINTER(Windows.Win32.System.AddressBook.NOTIFICATION_head), lpvBaseOld: c_void_p, lpvBaseNew: c_void_p, lpcb: POINTER(UInt32)) -> Int32: ...
@winfunctype('MAPI32.dll')
def ScCountProps(cValues: Int32, lpPropArray: POINTER(Windows.Win32.System.AddressBook.SPropValue_head), lpcb: POINTER(UInt32)) -> Int32: ...
@winfunctype('MAPI32.dll')
def LpValFindProp(ulPropTag: UInt32, cValues: UInt32, lpPropArray: POINTER(Windows.Win32.System.AddressBook.SPropValue_head)) -> POINTER(Windows.Win32.System.AddressBook.SPropValue_head): ...
@winfunctype('MAPI32.dll')
def ScCopyProps(cValues: Int32, lpPropArray: POINTER(Windows.Win32.System.AddressBook.SPropValue_head), lpvDst: c_void_p, lpcb: POINTER(UInt32)) -> Int32: ...
@winfunctype('MAPI32.dll')
def ScRelocProps(cValues: Int32, lpPropArray: POINTER(Windows.Win32.System.AddressBook.SPropValue_head), lpvBaseOld: c_void_p, lpvBaseNew: c_void_p, lpcb: POINTER(UInt32)) -> Int32: ...
@winfunctype('MAPI32.dll')
def ScDupPropset(cValues: Int32, lpPropArray: POINTER(Windows.Win32.System.AddressBook.SPropValue_head), lpAllocateBuffer: Windows.Win32.System.AddressBook.LPALLOCATEBUFFER, lppPropArray: POINTER(POINTER(Windows.Win32.System.AddressBook.SPropValue_head))) -> Int32: ...
@winfunctype('MAPI32.dll')
def UlAddRef(lpunk: c_void_p) -> UInt32: ...
@winfunctype('MAPI32.dll')
def UlRelease(lpunk: c_void_p) -> UInt32: ...
@winfunctype('MAPI32.dll')
def HrGetOneProp(lpMapiProp: Windows.Win32.System.AddressBook.IMAPIProp_head, ulPropTag: UInt32, lppProp: POINTER(POINTER(Windows.Win32.System.AddressBook.SPropValue_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def HrSetOneProp(lpMapiProp: Windows.Win32.System.AddressBook.IMAPIProp_head, lpProp: POINTER(Windows.Win32.System.AddressBook.SPropValue_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def FPropExists(lpMapiProp: Windows.Win32.System.AddressBook.IMAPIProp_head, ulPropTag: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAPI32.dll')
def PpropFindProp(lpPropArray: POINTER(Windows.Win32.System.AddressBook.SPropValue_head), cValues: UInt32, ulPropTag: UInt32) -> POINTER(Windows.Win32.System.AddressBook.SPropValue_head): ...
@winfunctype('MAPI32.dll')
def FreePadrlist(lpAdrlist: POINTER(Windows.Win32.System.AddressBook.ADRLIST_head)) -> Void: ...
@winfunctype('MAPI32.dll')
def FreeProws(lpRows: POINTER(Windows.Win32.System.AddressBook.SRowSet_head)) -> Void: ...
@winfunctype('MAPI32.dll')
def HrQueryAllRows(lpTable: Windows.Win32.System.AddressBook.IMAPITable_head, lpPropTags: POINTER(Windows.Win32.System.AddressBook.SPropTagArray_head), lpRestriction: POINTER(Windows.Win32.System.AddressBook.SRestriction_head), lpSortOrderSet: POINTER(Windows.Win32.System.AddressBook.SSortOrderSet_head), crowsMax: Int32, lppRows: POINTER(POINTER(Windows.Win32.System.AddressBook.SRowSet_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def SzFindCh(lpsz: POINTER(SByte), ch: UInt16) -> POINTER(SByte): ...
@winfunctype('MAPI32.dll')
def SzFindLastCh(lpsz: POINTER(SByte), ch: UInt16) -> POINTER(SByte): ...
@winfunctype('MAPI32.dll')
def SzFindSz(lpsz: POINTER(SByte), lpszKey: POINTER(SByte)) -> POINTER(SByte): ...
@winfunctype('MAPI32.dll')
def UFromSz(lpsz: POINTER(SByte)) -> UInt32: ...
@winfunctype('MAPI32.dll')
def ScUNCFromLocalPath(lpszLocal: Windows.Win32.Foundation.PSTR, lpszUNC: Windows.Win32.Foundation.PSTR, cchUNC: UInt32) -> Int32: ...
@winfunctype('MAPI32.dll')
def ScLocalPathFromUNC(lpszUNC: Windows.Win32.Foundation.PSTR, lpszLocal: Windows.Win32.Foundation.PSTR, cchLocal: UInt32) -> Int32: ...
@winfunctype('MAPI32.dll')
def FtAddFt(ftAddend1: Windows.Win32.Foundation.FILETIME, ftAddend2: Windows.Win32.Foundation.FILETIME) -> Windows.Win32.Foundation.FILETIME: ...
@winfunctype('MAPI32.dll')
def FtMulDwDw(ftMultiplicand: UInt32, ftMultiplier: UInt32) -> Windows.Win32.Foundation.FILETIME: ...
@winfunctype('MAPI32.dll')
def FtMulDw(ftMultiplier: UInt32, ftMultiplicand: Windows.Win32.Foundation.FILETIME) -> Windows.Win32.Foundation.FILETIME: ...
@winfunctype('MAPI32.dll')
def FtSubFt(ftMinuend: Windows.Win32.Foundation.FILETIME, ftSubtrahend: Windows.Win32.Foundation.FILETIME) -> Windows.Win32.Foundation.FILETIME: ...
@winfunctype('MAPI32.dll')
def FtNegFt(ft: Windows.Win32.Foundation.FILETIME) -> Windows.Win32.Foundation.FILETIME: ...
@winfunctype('MAPI32.dll')
def ScCreateConversationIndex(cbParent: UInt32, lpbParent: POINTER(Byte), lpcbConvIndex: POINTER(UInt32), lppbConvIndex: POINTER(POINTER(Byte))) -> Int32: ...
@winfunctype('MAPI32.dll')
def WrapStoreEntryID(ulFlags: UInt32, lpszDLLName: POINTER(SByte), cbOrigEntry: UInt32, lpOrigEntry: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head), lpcbWrappedEntry: POINTER(UInt32), lppWrappedEntry: POINTER(POINTER(Windows.Win32.System.AddressBook.ENTRYID_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def RTFSync(lpMessage: Windows.Win32.System.AddressBook.IMessage_head, ulFlags: UInt32, lpfMessageUpdated: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def WrapCompressedRTFStream(lpCompressedRTFStream: Windows.Win32.System.Com.IStream_head, ulFlags: UInt32, lpUncompressedRTFStream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def HrIStorageFromStream(lpUnkIn: Windows.Win32.System.Com.IUnknown_head, lpInterface: POINTER(Guid), ulFlags: UInt32, lppStorageOut: POINTER(Windows.Win32.System.Com.StructuredStorage.IStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def ScInitMapiUtil(ulFlags: UInt32) -> Int32: ...
@winfunctype('MAPI32.dll')
def DeinitMapiUtil() -> Void: ...
@winfunctype_pointer
def CALLERRELEASE(ulCallerData: UInt32, lpTblData: Windows.Win32.System.AddressBook.ITableData_head, lpVue: Windows.Win32.System.AddressBook.IMAPITable_head) -> Void: ...
class DTBLBUTTON(EasyCastStructure):
    ulbLpszLabel: UInt32
    ulFlags: UInt32
    ulPRControl: UInt32
class DTBLCHECKBOX(EasyCastStructure):
    ulbLpszLabel: UInt32
    ulFlags: UInt32
    ulPRPropertyName: UInt32
class DTBLCOMBOBOX(EasyCastStructure):
    ulbLpszCharsAllowed: UInt32
    ulFlags: UInt32
    ulNumCharsAllowed: UInt32
    ulPRPropertyName: UInt32
    ulPRTableName: UInt32
class DTBLDDLBX(EasyCastStructure):
    ulFlags: UInt32
    ulPRDisplayProperty: UInt32
    ulPRSetProperty: UInt32
    ulPRTableName: UInt32
class DTBLEDIT(EasyCastStructure):
    ulbLpszCharsAllowed: UInt32
    ulFlags: UInt32
    ulNumCharsAllowed: UInt32
    ulPropTag: UInt32
class DTBLGROUPBOX(EasyCastStructure):
    ulbLpszLabel: UInt32
    ulFlags: UInt32
class DTBLLABEL(EasyCastStructure):
    ulbLpszLabelName: UInt32
    ulFlags: UInt32
class DTBLLBX(EasyCastStructure):
    ulFlags: UInt32
    ulPRSetProperty: UInt32
    ulPRTableName: UInt32
class DTBLMVDDLBX(EasyCastStructure):
    ulFlags: UInt32
    ulMVPropTag: UInt32
class DTBLMVLISTBOX(EasyCastStructure):
    ulFlags: UInt32
    ulMVPropTag: UInt32
class DTBLPAGE(EasyCastStructure):
    ulbLpszLabel: UInt32
    ulFlags: UInt32
    ulbLpszComponent: UInt32
    ulContext: UInt32
class DTBLRADIOBUTTON(EasyCastStructure):
    ulbLpszLabel: UInt32
    ulFlags: UInt32
    ulcButtons: UInt32
    ulPropTag: UInt32
    lReturnValue: Int32
class DTCTL(EasyCastStructure):
    ulCtlType: UInt32
    ulCtlFlags: UInt32
    lpbNotif: POINTER(Byte)
    cbNotif: UInt32
    lpszFilter: POINTER(SByte)
    ulItemID: UInt32
    ctl: _ctl_e__Union
    class _ctl_e__Union(EasyCastUnion):
        lpv: c_void_p
        lplabel: POINTER(Windows.Win32.System.AddressBook.DTBLLABEL_head)
        lpedit: POINTER(Windows.Win32.System.AddressBook.DTBLEDIT_head)
        lplbx: POINTER(Windows.Win32.System.AddressBook.DTBLLBX_head)
        lpcombobox: POINTER(Windows.Win32.System.AddressBook.DTBLCOMBOBOX_head)
        lpddlbx: POINTER(Windows.Win32.System.AddressBook.DTBLDDLBX_head)
        lpcheckbox: POINTER(Windows.Win32.System.AddressBook.DTBLCHECKBOX_head)
        lpgroupbox: POINTER(Windows.Win32.System.AddressBook.DTBLGROUPBOX_head)
        lpbutton: POINTER(Windows.Win32.System.AddressBook.DTBLBUTTON_head)
        lpradiobutton: POINTER(Windows.Win32.System.AddressBook.DTBLRADIOBUTTON_head)
        lpmvlbx: POINTER(Windows.Win32.System.AddressBook.DTBLMVLISTBOX_head)
        lpmvddlbx: POINTER(Windows.Win32.System.AddressBook.DTBLMVDDLBX_head)
        lppage: POINTER(Windows.Win32.System.AddressBook.DTBLPAGE_head)
class DTPAGE(EasyCastStructure):
    cctl: UInt32
    lpszResourceName: POINTER(SByte)
    Anonymous: _Anonymous_e__Union
    lpctl: POINTER(Windows.Win32.System.AddressBook.DTCTL_head)
    class _Anonymous_e__Union(EasyCastUnion):
        lpszComponent: POINTER(SByte)
        ulItemID: UInt32
class ENTRYID(EasyCastStructure):
    abFlags: Byte * 4
    ab: Byte * 1
class ERROR_NOTIFICATION(EasyCastStructure):
    cbEntryID: UInt32
    lpEntryID: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head)
    scode: Int32
    ulFlags: UInt32
    lpMAPIError: POINTER(Windows.Win32.System.AddressBook.MAPIERROR_head)
class EXTENDED_NOTIFICATION(EasyCastStructure):
    ulEvent: UInt32
    cb: UInt32
    pbEventParameters: POINTER(Byte)
class FLATENTRY(EasyCastStructure):
    cb: UInt32
    abEntry: Byte * 1
class FLATENTRYLIST(EasyCastStructure):
    cEntries: UInt32
    cbEntries: UInt32
    abEntries: Byte * 1
class FLATMTSIDLIST(EasyCastStructure):
    cMTSIDs: UInt32
    cbMTSIDs: UInt32
    abMTSIDs: Byte * 1
class FlagList(EasyCastStructure):
    cFlags: UInt32
    ulFlag: UInt32 * 1
Gender = Int32
Gender_genderUnspecified: Gender = 0
Gender_genderFemale: Gender = 1
Gender_genderMale: Gender = 2
class IABContainer(c_void_p):
    extends: Windows.Win32.System.AddressBook.IMAPIContainer
    @commethod(19)
    def CreateEntry(self, cbEntryID: UInt32, lpEntryID: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head), ulCreateFlags: UInt32, lppMAPIPropEntry: POINTER(Windows.Win32.System.AddressBook.IMAPIProp_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def CopyEntries(self, lpEntries: POINTER(Windows.Win32.System.AddressBook.SBinaryArray_head), ulUIParam: UIntPtr, lpProgress: Windows.Win32.System.AddressBook.IMAPIProgress_head, ulFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def DeleteEntries(self, lpEntries: POINTER(Windows.Win32.System.AddressBook.SBinaryArray_head), ulFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def ResolveNames(self, lpPropTagArray: POINTER(Windows.Win32.System.AddressBook.SPropTagArray_head), ulFlags: UInt32, lpAdrList: POINTER(Windows.Win32.System.AddressBook.ADRLIST_head), lpFlagList: POINTER(Windows.Win32.System.AddressBook.FlagList_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAddrBook(c_void_p):
    extends: Windows.Win32.System.AddressBook.IMAPIProp
    @commethod(14)
    def OpenEntry(self, cbEntryID: UInt32, lpEntryID: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head), lpInterface: POINTER(Guid), ulFlags: UInt32, lpulObjType: POINTER(UInt32), lppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CompareEntryIDs(self, cbEntryID1: UInt32, lpEntryID1: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head), cbEntryID2: UInt32, lpEntryID2: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head), ulFlags: UInt32, lpulResult: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Advise(self, cbEntryID: UInt32, lpEntryID: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head), ulEventMask: UInt32, lpAdviseSink: Windows.Win32.System.AddressBook.IMAPIAdviseSink_head, lpulConnection: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Unadvise(self, ulConnection: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def CreateOneOff(self, lpszName: POINTER(SByte), lpszAdrType: POINTER(SByte), lpszAddress: POINTER(SByte), ulFlags: UInt32, lpcbEntryID: POINTER(UInt32), lppEntryID: POINTER(POINTER(Windows.Win32.System.AddressBook.ENTRYID_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def NewEntry(self, ulUIParam: UInt32, ulFlags: UInt32, cbEIDContainer: UInt32, lpEIDContainer: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head), cbEIDNewEntryTpl: UInt32, lpEIDNewEntryTpl: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head), lpcbEIDNewEntry: POINTER(UInt32), lppEIDNewEntry: POINTER(POINTER(Windows.Win32.System.AddressBook.ENTRYID_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def ResolveName(self, ulUIParam: UIntPtr, ulFlags: UInt32, lpszNewEntryTitle: POINTER(SByte), lpAdrList: POINTER(Windows.Win32.System.AddressBook.ADRLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Address(self, lpulUIParam: POINTER(UInt32), lpAdrParms: POINTER(Windows.Win32.System.AddressBook.ADRPARM_head), lppAdrList: POINTER(POINTER(Windows.Win32.System.AddressBook.ADRLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Details(self, lpulUIParam: POINTER(UIntPtr), lpfnDismiss: Windows.Win32.System.AddressBook.LPFNDISMISS, lpvDismissContext: c_void_p, cbEntryID: UInt32, lpEntryID: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head), lpfButtonCallback: Windows.Win32.System.AddressBook.LPFNBUTTON, lpvButtonContext: c_void_p, lpszButtonText: POINTER(SByte), ulFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def RecipOptions(self, ulUIParam: UInt32, ulFlags: UInt32, lpRecip: POINTER(Windows.Win32.System.AddressBook.ADRENTRY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def QueryDefaultRecipOpt(self, lpszAdrType: POINTER(SByte), ulFlags: UInt32, lpcValues: POINTER(UInt32), lppOptions: POINTER(POINTER(Windows.Win32.System.AddressBook.SPropValue_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetPAB(self, lpcbEntryID: POINTER(UInt32), lppEntryID: POINTER(POINTER(Windows.Win32.System.AddressBook.ENTRYID_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SetPAB(self, cbEntryID: UInt32, lpEntryID: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetDefaultDir(self, lpcbEntryID: POINTER(UInt32), lppEntryID: POINTER(POINTER(Windows.Win32.System.AddressBook.ENTRYID_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def SetDefaultDir(self, cbEntryID: UInt32, lpEntryID: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetSearchPath(self, ulFlags: UInt32, lppSearchPath: POINTER(POINTER(Windows.Win32.System.AddressBook.SRowSet_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def SetSearchPath(self, ulFlags: UInt32, lpSearchPath: POINTER(Windows.Win32.System.AddressBook.SRowSet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def PrepareRecips(self, ulFlags: UInt32, lpPropTagArray: POINTER(Windows.Win32.System.AddressBook.SPropTagArray_head), lpRecipList: POINTER(Windows.Win32.System.AddressBook.ADRLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAttach(c_void_p):
    extends: Windows.Win32.System.AddressBook.IMAPIProp
class IDistList(c_void_p):
    extends: Windows.Win32.System.AddressBook.IMAPIContainer
    @commethod(19)
    def CreateEntry(self, cbEntryID: UInt32, lpEntryID: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head), ulCreateFlags: UInt32, lppMAPIPropEntry: POINTER(Windows.Win32.System.AddressBook.IMAPIProp_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def CopyEntries(self, lpEntries: POINTER(Windows.Win32.System.AddressBook.SBinaryArray_head), ulUIParam: UIntPtr, lpProgress: Windows.Win32.System.AddressBook.IMAPIProgress_head, ulFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def DeleteEntries(self, lpEntries: POINTER(Windows.Win32.System.AddressBook.SBinaryArray_head), ulFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def ResolveNames(self, lpPropTagArray: POINTER(Windows.Win32.System.AddressBook.SPropTagArray_head), ulFlags: UInt32, lpAdrList: POINTER(Windows.Win32.System.AddressBook.ADRLIST_head), lpFlagList: POINTER(Windows.Win32.System.AddressBook.FlagList_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMAPIAdviseSink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def OnNotify(self, cNotif: UInt32, lpNotifications: POINTER(Windows.Win32.System.AddressBook.NOTIFICATION_head)) -> UInt32: ...
class IMAPIContainer(c_void_p):
    extends: Windows.Win32.System.AddressBook.IMAPIProp
    @commethod(14)
    def GetContentsTable(self, ulFlags: UInt32, lppTable: POINTER(Windows.Win32.System.AddressBook.IMAPITable_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetHierarchyTable(self, ulFlags: UInt32, lppTable: POINTER(Windows.Win32.System.AddressBook.IMAPITable_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def OpenEntry(self, cbEntryID: UInt32, lpEntryID: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head), lpInterface: POINTER(Guid), ulFlags: UInt32, lpulObjType: POINTER(UInt32), lppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetSearchCriteria(self, lpRestriction: POINTER(Windows.Win32.System.AddressBook.SRestriction_head), lpContainerList: POINTER(Windows.Win32.System.AddressBook.SBinaryArray_head), ulSearchFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetSearchCriteria(self, ulFlags: UInt32, lppRestriction: POINTER(POINTER(Windows.Win32.System.AddressBook.SRestriction_head)), lppContainerList: POINTER(POINTER(Windows.Win32.System.AddressBook.SBinaryArray_head)), lpulSearchState: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMAPIControl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetLastError(self, hResult: Windows.Win32.Foundation.HRESULT, ulFlags: UInt32, lppMAPIError: POINTER(POINTER(Windows.Win32.System.AddressBook.MAPIERROR_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Activate(self, ulFlags: UInt32, ulUIParam: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetState(self, ulFlags: UInt32, lpulState: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMAPIFolder(c_void_p):
    extends: Windows.Win32.System.AddressBook.IMAPIContainer
    @commethod(19)
    def CreateMessage(self, lpInterface: POINTER(Guid), ulFlags: UInt32, lppMessage: POINTER(Windows.Win32.System.AddressBook.IMessage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def CopyMessages(self, lpMsgList: POINTER(Windows.Win32.System.AddressBook.SBinaryArray_head), lpInterface: POINTER(Guid), lpDestFolder: c_void_p, ulUIParam: UIntPtr, lpProgress: Windows.Win32.System.AddressBook.IMAPIProgress_head, ulFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def DeleteMessages(self, lpMsgList: POINTER(Windows.Win32.System.AddressBook.SBinaryArray_head), ulUIParam: UIntPtr, lpProgress: Windows.Win32.System.AddressBook.IMAPIProgress_head, ulFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def CreateFolder(self, ulFolderType: UInt32, lpszFolderName: POINTER(SByte), lpszFolderComment: POINTER(SByte), lpInterface: POINTER(Guid), ulFlags: UInt32, lppFolder: POINTER(Windows.Win32.System.AddressBook.IMAPIFolder_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def CopyFolder(self, cbEntryID: UInt32, lpEntryID: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head), lpInterface: POINTER(Guid), lpDestFolder: c_void_p, lpszNewFolderName: POINTER(SByte), ulUIParam: UIntPtr, lpProgress: Windows.Win32.System.AddressBook.IMAPIProgress_head, ulFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def DeleteFolder(self, cbEntryID: UInt32, lpEntryID: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head), ulUIParam: UIntPtr, lpProgress: Windows.Win32.System.AddressBook.IMAPIProgress_head, ulFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetReadFlags(self, lpMsgList: POINTER(Windows.Win32.System.AddressBook.SBinaryArray_head), ulUIParam: UIntPtr, lpProgress: Windows.Win32.System.AddressBook.IMAPIProgress_head, ulFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetMessageStatus(self, cbEntryID: UInt32, lpEntryID: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head), ulFlags: UInt32, lpulMessageStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetMessageStatus(self, cbEntryID: UInt32, lpEntryID: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head), ulNewStatus: UInt32, ulNewStatusMask: UInt32, lpulOldStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def SaveContentsSort(self, lpSortCriteria: POINTER(Windows.Win32.System.AddressBook.SSortOrderSet_head), ulFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def EmptyFolder(self, ulUIParam: UIntPtr, lpProgress: Windows.Win32.System.AddressBook.IMAPIProgress_head, ulFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMAPIProgress(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def Progress(self, ulValue: UInt32, ulCount: UInt32, ulTotal: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFlags(self, lpulFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMax(self, lpulMax: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMin(self, lpulMin: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetLimits(self, lpulMin: POINTER(UInt32), lpulMax: POINTER(UInt32), lpulFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMAPIProp(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetLastError(self, hResult: Windows.Win32.Foundation.HRESULT, ulFlags: UInt32, lppMAPIError: POINTER(POINTER(Windows.Win32.System.AddressBook.MAPIERROR_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SaveChanges(self, ulFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetProps(self, lpPropTagArray: POINTER(Windows.Win32.System.AddressBook.SPropTagArray_head), ulFlags: UInt32, lpcValues: POINTER(UInt32), lppPropArray: POINTER(POINTER(Windows.Win32.System.AddressBook.SPropValue_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPropList(self, ulFlags: UInt32, lppPropTagArray: POINTER(POINTER(Windows.Win32.System.AddressBook.SPropTagArray_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OpenProperty(self, ulPropTag: UInt32, lpiid: POINTER(Guid), ulInterfaceOptions: UInt32, ulFlags: UInt32, lppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetProps(self, cValues: UInt32, lpPropArray: POINTER(Windows.Win32.System.AddressBook.SPropValue_head), lppProblems: POINTER(POINTER(Windows.Win32.System.AddressBook.SPropProblemArray_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def DeleteProps(self, lpPropTagArray: POINTER(Windows.Win32.System.AddressBook.SPropTagArray_head), lppProblems: POINTER(POINTER(Windows.Win32.System.AddressBook.SPropProblemArray_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CopyTo(self, ciidExclude: UInt32, rgiidExclude: POINTER(Guid), lpExcludeProps: POINTER(Windows.Win32.System.AddressBook.SPropTagArray_head), ulUIParam: UIntPtr, lpProgress: Windows.Win32.System.AddressBook.IMAPIProgress_head, lpInterface: POINTER(Guid), lpDestObj: c_void_p, ulFlags: UInt32, lppProblems: POINTER(POINTER(Windows.Win32.System.AddressBook.SPropProblemArray_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CopyProps(self, lpIncludeProps: POINTER(Windows.Win32.System.AddressBook.SPropTagArray_head), ulUIParam: UIntPtr, lpProgress: Windows.Win32.System.AddressBook.IMAPIProgress_head, lpInterface: POINTER(Guid), lpDestObj: c_void_p, ulFlags: UInt32, lppProblems: POINTER(POINTER(Windows.Win32.System.AddressBook.SPropProblemArray_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetNamesFromIDs(self, lppPropTags: POINTER(POINTER(Windows.Win32.System.AddressBook.SPropTagArray_head)), lpPropSetGuid: POINTER(Guid), ulFlags: UInt32, lpcPropNames: POINTER(UInt32), lpppPropNames: POINTER(POINTER(POINTER(Windows.Win32.System.AddressBook.MAPINAMEID_head)))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetIDsFromNames(self, cPropNames: UInt32, lppPropNames: POINTER(POINTER(Windows.Win32.System.AddressBook.MAPINAMEID_head)), ulFlags: UInt32, lppPropTags: POINTER(POINTER(Windows.Win32.System.AddressBook.SPropTagArray_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IMAPIStatus(c_void_p):
    extends: Windows.Win32.System.AddressBook.IMAPIProp
    @commethod(14)
    def ValidateState(self, ulUIParam: UIntPtr, ulFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SettingsDialog(self, ulUIParam: UIntPtr, ulFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def ChangePassword(self, lpOldPass: POINTER(SByte), lpNewPass: POINTER(SByte), ulFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def FlushQueues(self, ulUIParam: UIntPtr, cbTargetTransport: UInt32, lpTargetTransport: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head), ulFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMAPITable(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetLastError(self, hResult: Windows.Win32.Foundation.HRESULT, ulFlags: UInt32, lppMAPIError: POINTER(POINTER(Windows.Win32.System.AddressBook.MAPIERROR_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Advise(self, ulEventMask: UInt32, lpAdviseSink: Windows.Win32.System.AddressBook.IMAPIAdviseSink_head, lpulConnection: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Unadvise(self, ulConnection: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStatus(self, lpulTableStatus: POINTER(UInt32), lpulTableType: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetColumns(self, lpPropTagArray: POINTER(Windows.Win32.System.AddressBook.SPropTagArray_head), ulFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def QueryColumns(self, ulFlags: UInt32, lpPropTagArray: POINTER(POINTER(Windows.Win32.System.AddressBook.SPropTagArray_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRowCount(self, ulFlags: UInt32, lpulCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SeekRow(self, bkOrigin: UInt32, lRowCount: Int32, lplRowsSought: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SeekRowApprox(self, ulNumerator: UInt32, ulDenominator: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def QueryPosition(self, lpulRow: POINTER(UInt32), lpulNumerator: POINTER(UInt32), lpulDenominator: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def FindRow(self, lpRestriction: POINTER(Windows.Win32.System.AddressBook.SRestriction_head), bkOrigin: UInt32, ulFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Restrict(self, lpRestriction: POINTER(Windows.Win32.System.AddressBook.SRestriction_head), ulFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CreateBookmark(self, lpbkPosition: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def FreeBookmark(self, bkPosition: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SortTable(self, lpSortCriteria: POINTER(Windows.Win32.System.AddressBook.SSortOrderSet_head), ulFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def QuerySortOrder(self, lppSortCriteria: POINTER(POINTER(Windows.Win32.System.AddressBook.SSortOrderSet_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def QueryRows(self, lRowCount: Int32, ulFlags: UInt32, lppRows: POINTER(POINTER(Windows.Win32.System.AddressBook.SRowSet_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def Abort(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def ExpandRow(self, cbInstanceKey: UInt32, pbInstanceKey: POINTER(Byte), ulRowCount: UInt32, ulFlags: UInt32, lppRows: POINTER(POINTER(Windows.Win32.System.AddressBook.SRowSet_head)), lpulMoreRows: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def CollapseRow(self, cbInstanceKey: UInt32, pbInstanceKey: POINTER(Byte), ulFlags: UInt32, lpulRowCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def WaitForCompletion(self, ulFlags: UInt32, ulTimeout: UInt32, lpulTableStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetCollapseState(self, ulFlags: UInt32, cbInstanceKey: UInt32, lpbInstanceKey: POINTER(Byte), lpcbCollapseState: POINTER(UInt32), lppbCollapseState: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetCollapseState(self, ulFlags: UInt32, cbCollapseState: UInt32, pbCollapseState: POINTER(Byte), lpbkLocation: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMailUser(c_void_p):
    extends: Windows.Win32.System.AddressBook.IMAPIProp
class IMessage(c_void_p):
    extends: Windows.Win32.System.AddressBook.IMAPIProp
    @commethod(14)
    def GetAttachmentTable(self, ulFlags: UInt32, lppTable: POINTER(Windows.Win32.System.AddressBook.IMAPITable_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def OpenAttach(self, ulAttachmentNum: UInt32, lpInterface: POINTER(Guid), ulFlags: UInt32, lppAttach: POINTER(Windows.Win32.System.AddressBook.IAttach_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def CreateAttach(self, lpInterface: POINTER(Guid), ulFlags: UInt32, lpulAttachmentNum: POINTER(UInt32), lppAttach: POINTER(Windows.Win32.System.AddressBook.IAttach_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def DeleteAttach(self, ulAttachmentNum: UInt32, ulUIParam: UIntPtr, lpProgress: Windows.Win32.System.AddressBook.IMAPIProgress_head, ulFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetRecipientTable(self, ulFlags: UInt32, lppTable: POINTER(Windows.Win32.System.AddressBook.IMAPITable_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ModifyRecipients(self, ulFlags: UInt32, lpMods: POINTER(Windows.Win32.System.AddressBook.ADRLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SubmitMessage(self, ulFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetReadFlag(self, ulFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IMsgStore(c_void_p):
    extends: Windows.Win32.System.AddressBook.IMAPIProp
    @commethod(14)
    def Advise(self, cbEntryID: UInt32, lpEntryID: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head), ulEventMask: UInt32, lpAdviseSink: Windows.Win32.System.AddressBook.IMAPIAdviseSink_head, lpulConnection: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Unadvise(self, ulConnection: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def CompareEntryIDs(self, cbEntryID1: UInt32, lpEntryID1: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head), cbEntryID2: UInt32, lpEntryID2: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head), ulFlags: UInt32, lpulResult: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def OpenEntry(self, cbEntryID: UInt32, lpEntryID: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head), lpInterface: POINTER(Guid), ulFlags: UInt32, lpulObjType: POINTER(UInt32), ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetReceiveFolder(self, lpszMessageClass: POINTER(SByte), ulFlags: UInt32, cbEntryID: UInt32, lpEntryID: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetReceiveFolder(self, lpszMessageClass: POINTER(SByte), ulFlags: UInt32, lpcbEntryID: POINTER(UInt32), lppEntryID: POINTER(POINTER(Windows.Win32.System.AddressBook.ENTRYID_head)), lppszExplicitClass: POINTER(POINTER(SByte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetReceiveFolderTable(self, ulFlags: UInt32, lppTable: POINTER(Windows.Win32.System.AddressBook.IMAPITable_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def StoreLogoff(self, lpulFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def AbortSubmit(self, cbEntryID: UInt32, lpEntryID: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head), ulFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetOutgoingQueue(self, ulFlags: UInt32, lppTable: POINTER(Windows.Win32.System.AddressBook.IMAPITable_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetLockState(self, lpMessage: Windows.Win32.System.AddressBook.IMessage_head, ulLockState: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def FinishedMsg(self, ulFlags: UInt32, cbEntryID: UInt32, lpEntryID: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def NotifyNewMail(self, lpNotification: POINTER(Windows.Win32.System.AddressBook.NOTIFICATION_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IProfSect(c_void_p):
    extends: Windows.Win32.System.AddressBook.IMAPIProp
class IPropData(c_void_p):
    extends: Windows.Win32.System.AddressBook.IMAPIProp
    @commethod(14)
    def HrSetObjAccess(self, ulAccess: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def HrSetPropAccess(self, lpPropTagArray: POINTER(Windows.Win32.System.AddressBook.SPropTagArray_head), rgulAccess: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def HrGetPropAccess(self, lppPropTagArray: POINTER(POINTER(Windows.Win32.System.AddressBook.SPropTagArray_head)), lprgulAccess: POINTER(POINTER(UInt32))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def HrAddObjProps(self, lppPropTagArray: POINTER(Windows.Win32.System.AddressBook.SPropTagArray_head), lprgulAccess: POINTER(POINTER(Windows.Win32.System.AddressBook.SPropProblemArray_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IProviderAdmin(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetLastError(self, hResult: Windows.Win32.Foundation.HRESULT, ulFlags: UInt32, lppMAPIError: POINTER(POINTER(Windows.Win32.System.AddressBook.MAPIERROR_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProviderTable(self, ulFlags: UInt32, lppTable: POINTER(Windows.Win32.System.AddressBook.IMAPITable_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateProvider(self, lpszProvider: POINTER(SByte), cValues: UInt32, lpProps: POINTER(Windows.Win32.System.AddressBook.SPropValue_head), ulUIParam: UIntPtr, ulFlags: UInt32, lpUID: POINTER(Windows.Win32.System.AddressBook.MAPIUID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DeleteProvider(self, lpUID: POINTER(Windows.Win32.System.AddressBook.MAPIUID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OpenProfileSection(self, lpUID: POINTER(Windows.Win32.System.AddressBook.MAPIUID_head), lpInterface: POINTER(Guid), ulFlags: UInt32, lppProfSect: POINTER(Windows.Win32.System.AddressBook.IProfSect_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITableData(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def HrGetView(self, lpSSortOrderSet: POINTER(Windows.Win32.System.AddressBook.SSortOrderSet_head), lpfCallerRelease: POINTER(Windows.Win32.System.AddressBook.CALLERRELEASE), ulCallerData: UInt32, lppMAPITable: POINTER(Windows.Win32.System.AddressBook.IMAPITable_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def HrModifyRow(self, param0: POINTER(Windows.Win32.System.AddressBook.SRow_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def HrDeleteRow(self, lpSPropValue: POINTER(Windows.Win32.System.AddressBook.SPropValue_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def HrQueryRow(self, lpsPropValue: POINTER(Windows.Win32.System.AddressBook.SPropValue_head), lppSRow: POINTER(POINTER(Windows.Win32.System.AddressBook.SRow_head)), lpuliRow: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def HrEnumRow(self, ulRowNumber: UInt32, lppSRow: POINTER(POINTER(Windows.Win32.System.AddressBook.SRow_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def HrNotify(self, ulFlags: UInt32, cValues: UInt32, lpSPropValue: POINTER(Windows.Win32.System.AddressBook.SPropValue_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def HrInsertRow(self, uliRow: UInt32, lpSRow: POINTER(Windows.Win32.System.AddressBook.SRow_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def HrModifyRows(self, ulFlags: UInt32, lpSRowSet: POINTER(Windows.Win32.System.AddressBook.SRowSet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def HrDeleteRows(self, ulFlags: UInt32, lprowsetToDelete: POINTER(Windows.Win32.System.AddressBook.SRowSet_head), cRowsDeleted: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWABExtInit(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ea22ebf0-87a4-11d1-9a-cf-00-a0-c9-1f-9c-8b')
    @commethod(3)
    def Initialize(self, lpWABExtDisplay: POINTER(Windows.Win32.System.AddressBook.WABEXTDISPLAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWABObject(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetLastError(self, hResult: Windows.Win32.Foundation.HRESULT, ulFlags: UInt32, lppMAPIError: POINTER(POINTER(Windows.Win32.System.AddressBook.MAPIERROR_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AllocateBuffer(self, cbSize: UInt32, lppBuffer: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AllocateMore(self, cbSize: UInt32, lpObject: c_void_p, lppBuffer: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FreeBuffer(self, lpBuffer: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Backup(self, lpFileName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Import(self, lpWIP: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Find(self, lpIAB: Windows.Win32.System.AddressBook.IAddrBook_head, hWnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def VCardDisplay(self, lpIAB: Windows.Win32.System.AddressBook.IAddrBook_head, hWnd: Windows.Win32.Foundation.HWND, lpszFileName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def LDAPUrl(self, lpIAB: Windows.Win32.System.AddressBook.IAddrBook_head, hWnd: Windows.Win32.Foundation.HWND, ulFlags: UInt32, lpszURL: Windows.Win32.Foundation.PSTR, lppMailUser: POINTER(Windows.Win32.System.AddressBook.IMailUser_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def VCardCreate(self, lpIAB: Windows.Win32.System.AddressBook.IAddrBook_head, ulFlags: UInt32, lpszVCard: Windows.Win32.Foundation.PSTR, lpMailUser: Windows.Win32.System.AddressBook.IMailUser_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def VCardRetrieve(self, lpIAB: Windows.Win32.System.AddressBook.IAddrBook_head, ulFlags: UInt32, lpszVCard: Windows.Win32.Foundation.PSTR, lppMailUser: POINTER(Windows.Win32.System.AddressBook.IMailUser_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetMe(self, lpIAB: Windows.Win32.System.AddressBook.IAddrBook_head, ulFlags: UInt32, lpdwAction: POINTER(UInt32), lpsbEID: POINTER(Windows.Win32.System.AddressBook.SBinary_head), hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetMe(self, lpIAB: Windows.Win32.System.AddressBook.IAddrBook_head, ulFlags: UInt32, sbEID: Windows.Win32.System.AddressBook.SBinary, hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPALLOCATEBUFFER(cbSize: UInt32, lppBuffer: POINTER(c_void_p)) -> Int32: ...
@winfunctype_pointer
def LPALLOCATEMORE(cbSize: UInt32, lpObject: c_void_p, lppBuffer: POINTER(c_void_p)) -> Int32: ...
@winfunctype_pointer
def LPCREATECONVERSATIONINDEX(cbParent: UInt32, lpbParent: POINTER(Byte), lpcbConvIndex: POINTER(UInt32), lppbConvIndex: POINTER(POINTER(Byte))) -> Int32: ...
@winfunctype_pointer
def LPDISPATCHNOTIFICATIONS(ulFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPFNABSDI(ulUIParam: UIntPtr, lpvmsg: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def LPFNBUTTON(ulUIParam: UIntPtr, lpvContext: c_void_p, cbEntryID: UInt32, lpSelection: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head), ulFlags: UInt32) -> Int32: ...
@winfunctype_pointer
def LPFNDISMISS(ulUIParam: UIntPtr, lpvContext: c_void_p) -> Void: ...
@winfunctype_pointer
def LPFREEBUFFER(lpBuffer: c_void_p) -> UInt32: ...
@winfunctype_pointer
def LPNOTIFCALLBACK(lpvContext: c_void_p, cNotification: UInt32, lpNotifications: POINTER(Windows.Win32.System.AddressBook.NOTIFICATION_head)) -> Int32: ...
@winfunctype_pointer
def LPOPENSTREAMONFILE(lpAllocateBuffer: Windows.Win32.System.AddressBook.LPALLOCATEBUFFER, lpFreeBuffer: Windows.Win32.System.AddressBook.LPFREEBUFFER, ulFlags: UInt32, lpszFileName: POINTER(SByte), lpszPrefix: POINTER(SByte), lppStream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPWABALLOCATEBUFFER(lpWABObject: Windows.Win32.System.AddressBook.IWABObject_head, cbSize: UInt32, lppBuffer: POINTER(c_void_p)) -> Int32: ...
@winfunctype_pointer
def LPWABALLOCATEMORE(lpWABObject: Windows.Win32.System.AddressBook.IWABObject_head, cbSize: UInt32, lpObject: c_void_p, lppBuffer: POINTER(c_void_p)) -> Int32: ...
@winfunctype_pointer
def LPWABFREEBUFFER(lpWABObject: Windows.Win32.System.AddressBook.IWABObject_head, lpBuffer: c_void_p) -> UInt32: ...
@winfunctype_pointer
def LPWABOPEN(lppAdrBook: POINTER(Windows.Win32.System.AddressBook.IAddrBook_head), lppWABObject: POINTER(Windows.Win32.System.AddressBook.IWABObject_head), lpWP: POINTER(Windows.Win32.System.AddressBook.WAB_PARAM_head), Reserved2: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPWABOPENEX(lppAdrBook: POINTER(Windows.Win32.System.AddressBook.IAddrBook_head), lppWABObject: POINTER(Windows.Win32.System.AddressBook.IWABObject_head), lpWP: POINTER(Windows.Win32.System.AddressBook.WAB_PARAM_head), Reserved: UInt32, fnAllocateBuffer: Windows.Win32.System.AddressBook.LPALLOCATEBUFFER, fnAllocateMore: Windows.Win32.System.AddressBook.LPALLOCATEMORE, fnFreeBuffer: Windows.Win32.System.AddressBook.LPFREEBUFFER) -> Windows.Win32.Foundation.HRESULT: ...
class MAPIERROR(EasyCastStructure):
    ulVersion: UInt32
    lpszError: POINTER(SByte)
    lpszComponent: POINTER(SByte)
    ulLowLevelError: UInt32
    ulContext: UInt32
class MAPINAMEID(EasyCastStructure):
    lpguid: POINTER(Guid)
    ulKind: UInt32
    Kind: _Kind_e__Union
    class _Kind_e__Union(EasyCastUnion):
        lID: Int32
        lpwstrName: Windows.Win32.Foundation.PWSTR
class MAPIUID(EasyCastStructure):
    ab: Byte * 16
class MTSID(EasyCastStructure):
    cb: UInt32
    ab: Byte * 1
class NEWMAIL_NOTIFICATION(EasyCastStructure):
    cbEntryID: UInt32
    lpEntryID: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head)
    cbParentID: UInt32
    lpParentID: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head)
    ulFlags: UInt32
    lpszMessageClass: POINTER(SByte)
    ulMessageFlags: UInt32
class NOTIFICATION(EasyCastStructure):
    ulEventType: UInt32
    ulAlignPad: UInt32
    info: _info_e__Union
    class _info_e__Union(EasyCastUnion):
        err: Windows.Win32.System.AddressBook.ERROR_NOTIFICATION
        newmail: Windows.Win32.System.AddressBook.NEWMAIL_NOTIFICATION
        obj: Windows.Win32.System.AddressBook.OBJECT_NOTIFICATION
        tab: Windows.Win32.System.AddressBook.TABLE_NOTIFICATION
        ext: Windows.Win32.System.AddressBook.EXTENDED_NOTIFICATION
        statobj: Windows.Win32.System.AddressBook.STATUS_OBJECT_NOTIFICATION
class NOTIFKEY(EasyCastStructure):
    cb: UInt32
    ab: Byte * 1
class OBJECT_NOTIFICATION(EasyCastStructure):
    cbEntryID: UInt32
    lpEntryID: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head)
    ulObjType: UInt32
    cbParentID: UInt32
    lpParentID: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head)
    cbOldID: UInt32
    lpOldID: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head)
    cbOldParentID: UInt32
    lpOldParentID: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head)
    lpPropTagArray: POINTER(Windows.Win32.System.AddressBook.SPropTagArray_head)
@winfunctype_pointer
def PFNIDLE(param0: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
class SAndRestriction(EasyCastStructure):
    cRes: UInt32
    lpRes: POINTER(Windows.Win32.System.AddressBook.SRestriction_head)
class SAppTimeArray(EasyCastStructure):
    cValues: UInt32
    lpat: POINTER(Double)
class SBinary(EasyCastStructure):
    cb: UInt32
    lpb: POINTER(Byte)
class SBinaryArray(EasyCastStructure):
    cValues: UInt32
    lpbin: POINTER(Windows.Win32.System.AddressBook.SBinary_head)
class SBitMaskRestriction(EasyCastStructure):
    relBMR: UInt32
    ulPropTag: UInt32
    ulMask: UInt32
class SCommentRestriction(EasyCastStructure):
    cValues: UInt32
    lpRes: POINTER(Windows.Win32.System.AddressBook.SRestriction_head)
    lpProp: POINTER(Windows.Win32.System.AddressBook.SPropValue_head)
class SComparePropsRestriction(EasyCastStructure):
    relop: UInt32
    ulPropTag1: UInt32
    ulPropTag2: UInt32
class SContentRestriction(EasyCastStructure):
    ulFuzzyLevel: UInt32
    ulPropTag: UInt32
    lpProp: POINTER(Windows.Win32.System.AddressBook.SPropValue_head)
class SCurrencyArray(EasyCastStructure):
    cValues: UInt32
    lpcur: POINTER(Windows.Win32.System.Com.CY_head)
class SDateTimeArray(EasyCastStructure):
    cValues: UInt32
    lpft: POINTER(Windows.Win32.Foundation.FILETIME_head)
class SDoubleArray(EasyCastStructure):
    cValues: UInt32
    lpdbl: POINTER(Double)
class SExistRestriction(EasyCastStructure):
    ulReserved1: UInt32
    ulPropTag: UInt32
    ulReserved2: UInt32
class SGuidArray(EasyCastStructure):
    cValues: UInt32
    lpguid: POINTER(Guid)
class SLPSTRArray(EasyCastStructure):
    cValues: UInt32
    lppszA: POINTER(Windows.Win32.Foundation.PSTR)
class SLargeIntegerArray(EasyCastStructure):
    cValues: UInt32
    lpli: POINTER(Int64)
class SLongArray(EasyCastStructure):
    cValues: UInt32
    lpl: POINTER(Int32)
class SNotRestriction(EasyCastStructure):
    ulReserved: UInt32
    lpRes: POINTER(Windows.Win32.System.AddressBook.SRestriction_head)
class SOrRestriction(EasyCastStructure):
    cRes: UInt32
    lpRes: POINTER(Windows.Win32.System.AddressBook.SRestriction_head)
class SPropProblem(EasyCastStructure):
    ulIndex: UInt32
    ulPropTag: UInt32
    scode: Int32
class SPropProblemArray(EasyCastStructure):
    cProblem: UInt32
    aProblem: Windows.Win32.System.AddressBook.SPropProblem * 1
class SPropTagArray(EasyCastStructure):
    cValues: UInt32
    aulPropTag: UInt32 * 1
class SPropValue(EasyCastStructure):
    ulPropTag: UInt32
    dwAlignPad: UInt32
    Value: Windows.Win32.System.AddressBook.__UPV
class SPropertyRestriction(EasyCastStructure):
    relop: UInt32
    ulPropTag: UInt32
    lpProp: POINTER(Windows.Win32.System.AddressBook.SPropValue_head)
class SRealArray(EasyCastStructure):
    cValues: UInt32
    lpflt: POINTER(Single)
class SRestriction(EasyCastStructure):
    rt: UInt32
    res: _res_e__Union
    class _res_e__Union(EasyCastUnion):
        resCompareProps: Windows.Win32.System.AddressBook.SComparePropsRestriction
        resAnd: Windows.Win32.System.AddressBook.SAndRestriction
        resOr: Windows.Win32.System.AddressBook.SOrRestriction
        resNot: Windows.Win32.System.AddressBook.SNotRestriction
        resContent: Windows.Win32.System.AddressBook.SContentRestriction
        resProperty: Windows.Win32.System.AddressBook.SPropertyRestriction
        resBitMask: Windows.Win32.System.AddressBook.SBitMaskRestriction
        resSize: Windows.Win32.System.AddressBook.SSizeRestriction
        resExist: Windows.Win32.System.AddressBook.SExistRestriction
        resSub: Windows.Win32.System.AddressBook.SSubRestriction
        resComment: Windows.Win32.System.AddressBook.SCommentRestriction
class SRow(EasyCastStructure):
    ulAdrEntryPad: UInt32
    cValues: UInt32
    lpProps: POINTER(Windows.Win32.System.AddressBook.SPropValue_head)
class SRowSet(EasyCastStructure):
    cRows: UInt32
    aRow: Windows.Win32.System.AddressBook.SRow * 1
class SShortArray(EasyCastStructure):
    cValues: UInt32
    lpi: POINTER(Int16)
class SSizeRestriction(EasyCastStructure):
    relop: UInt32
    ulPropTag: UInt32
    cb: UInt32
class SSortOrder(EasyCastStructure):
    ulPropTag: UInt32
    ulOrder: UInt32
class SSortOrderSet(EasyCastStructure):
    cSorts: UInt32
    cCategories: UInt32
    cExpanded: UInt32
    aSort: Windows.Win32.System.AddressBook.SSortOrder * 1
class SSubRestriction(EasyCastStructure):
    ulSubObject: UInt32
    lpRes: POINTER(Windows.Win32.System.AddressBook.SRestriction_head)
class STATUS_OBJECT_NOTIFICATION(EasyCastStructure):
    cbEntryID: UInt32
    lpEntryID: POINTER(Windows.Win32.System.AddressBook.ENTRYID_head)
    cValues: UInt32
    lpPropVals: POINTER(Windows.Win32.System.AddressBook.SPropValue_head)
class SWStringArray(EasyCastStructure):
    cValues: UInt32
    lppszW: POINTER(Windows.Win32.Foundation.PWSTR)
class TABLE_NOTIFICATION(EasyCastStructure):
    ulTableEvent: UInt32
    hResult: Windows.Win32.Foundation.HRESULT
    propIndex: Windows.Win32.System.AddressBook.SPropValue
    propPrior: Windows.Win32.System.AddressBook.SPropValue
    row: Windows.Win32.System.AddressBook.SRow
    ulPad: UInt32
class WABEXTDISPLAY(EasyCastStructure):
    cbSize: UInt32
    lpWABObject: Windows.Win32.System.AddressBook.IWABObject_head
    lpAdrBook: Windows.Win32.System.AddressBook.IAddrBook_head
    lpPropObj: Windows.Win32.System.AddressBook.IMAPIProp_head
    fReadOnly: Windows.Win32.Foundation.BOOL
    fDataChanged: Windows.Win32.Foundation.BOOL
    ulFlags: UInt32
    lpv: c_void_p
    lpsz: POINTER(SByte)
class WABIMPORTPARAM(EasyCastStructure):
    cbSize: UInt32
    lpAdrBook: Windows.Win32.System.AddressBook.IAddrBook_head
    hWnd: Windows.Win32.Foundation.HWND
    ulFlags: UInt32
    lpszFileName: Windows.Win32.Foundation.PSTR
class WAB_PARAM(EasyCastStructure):
    cbSize: UInt32
    hwnd: Windows.Win32.Foundation.HWND
    szFileName: Windows.Win32.Foundation.PSTR
    ulFlags: UInt32
    guidPSExt: Guid
class _WABACTIONITEM(EasyCastStructure):
    pass
class __UPV(EasyCastUnion):
    i: Int16
    l: Int32
    ul: UInt32
    flt: Single
    dbl: Double
    b: UInt16
    cur: Windows.Win32.System.Com.CY
    at: Double
    ft: Windows.Win32.Foundation.FILETIME
    lpszA: Windows.Win32.Foundation.PSTR
    bin: Windows.Win32.System.AddressBook.SBinary
    lpszW: Windows.Win32.Foundation.PWSTR
    lpguid: POINTER(Guid)
    li: Int64
    MVi: Windows.Win32.System.AddressBook.SShortArray
    MVl: Windows.Win32.System.AddressBook.SLongArray
    MVflt: Windows.Win32.System.AddressBook.SRealArray
    MVdbl: Windows.Win32.System.AddressBook.SDoubleArray
    MVcur: Windows.Win32.System.AddressBook.SCurrencyArray
    MVat: Windows.Win32.System.AddressBook.SAppTimeArray
    MVft: Windows.Win32.System.AddressBook.SDateTimeArray
    MVbin: Windows.Win32.System.AddressBook.SBinaryArray
    MVszA: Windows.Win32.System.AddressBook.SLPSTRArray
    MVszW: Windows.Win32.System.AddressBook.SWStringArray
    MVguid: Windows.Win32.System.AddressBook.SGuidArray
    MVli: Windows.Win32.System.AddressBook.SLargeIntegerArray
    err: Int32
    x: Int32
make_head(_module, 'ADRENTRY')
make_head(_module, 'ADRLIST')
make_head(_module, 'ADRPARM')
make_head(_module, 'CALLERRELEASE')
make_head(_module, 'DTBLBUTTON')
make_head(_module, 'DTBLCHECKBOX')
make_head(_module, 'DTBLCOMBOBOX')
make_head(_module, 'DTBLDDLBX')
make_head(_module, 'DTBLEDIT')
make_head(_module, 'DTBLGROUPBOX')
make_head(_module, 'DTBLLABEL')
make_head(_module, 'DTBLLBX')
make_head(_module, 'DTBLMVDDLBX')
make_head(_module, 'DTBLMVLISTBOX')
make_head(_module, 'DTBLPAGE')
make_head(_module, 'DTBLRADIOBUTTON')
make_head(_module, 'DTCTL')
make_head(_module, 'DTPAGE')
make_head(_module, 'ENTRYID')
make_head(_module, 'ERROR_NOTIFICATION')
make_head(_module, 'EXTENDED_NOTIFICATION')
make_head(_module, 'FLATENTRY')
make_head(_module, 'FLATENTRYLIST')
make_head(_module, 'FLATMTSIDLIST')
make_head(_module, 'FlagList')
make_head(_module, 'IABContainer')
make_head(_module, 'IAddrBook')
make_head(_module, 'IAttach')
make_head(_module, 'IDistList')
make_head(_module, 'IMAPIAdviseSink')
make_head(_module, 'IMAPIContainer')
make_head(_module, 'IMAPIControl')
make_head(_module, 'IMAPIFolder')
make_head(_module, 'IMAPIProgress')
make_head(_module, 'IMAPIProp')
make_head(_module, 'IMAPIStatus')
make_head(_module, 'IMAPITable')
make_head(_module, 'IMailUser')
make_head(_module, 'IMessage')
make_head(_module, 'IMsgStore')
make_head(_module, 'IProfSect')
make_head(_module, 'IPropData')
make_head(_module, 'IProviderAdmin')
make_head(_module, 'ITableData')
make_head(_module, 'IWABExtInit')
make_head(_module, 'IWABObject')
make_head(_module, 'LPALLOCATEBUFFER')
make_head(_module, 'LPALLOCATEMORE')
make_head(_module, 'LPCREATECONVERSATIONINDEX')
make_head(_module, 'LPDISPATCHNOTIFICATIONS')
make_head(_module, 'LPFNABSDI')
make_head(_module, 'LPFNBUTTON')
make_head(_module, 'LPFNDISMISS')
make_head(_module, 'LPFREEBUFFER')
make_head(_module, 'LPNOTIFCALLBACK')
make_head(_module, 'LPOPENSTREAMONFILE')
make_head(_module, 'LPWABALLOCATEBUFFER')
make_head(_module, 'LPWABALLOCATEMORE')
make_head(_module, 'LPWABFREEBUFFER')
make_head(_module, 'LPWABOPEN')
make_head(_module, 'LPWABOPENEX')
make_head(_module, 'MAPIERROR')
make_head(_module, 'MAPINAMEID')
make_head(_module, 'MAPIUID')
make_head(_module, 'MTSID')
make_head(_module, 'NEWMAIL_NOTIFICATION')
make_head(_module, 'NOTIFICATION')
make_head(_module, 'NOTIFKEY')
make_head(_module, 'OBJECT_NOTIFICATION')
make_head(_module, 'PFNIDLE')
make_head(_module, 'SAndRestriction')
make_head(_module, 'SAppTimeArray')
make_head(_module, 'SBinary')
make_head(_module, 'SBinaryArray')
make_head(_module, 'SBitMaskRestriction')
make_head(_module, 'SCommentRestriction')
make_head(_module, 'SComparePropsRestriction')
make_head(_module, 'SContentRestriction')
make_head(_module, 'SCurrencyArray')
make_head(_module, 'SDateTimeArray')
make_head(_module, 'SDoubleArray')
make_head(_module, 'SExistRestriction')
make_head(_module, 'SGuidArray')
make_head(_module, 'SLPSTRArray')
make_head(_module, 'SLargeIntegerArray')
make_head(_module, 'SLongArray')
make_head(_module, 'SNotRestriction')
make_head(_module, 'SOrRestriction')
make_head(_module, 'SPropProblem')
make_head(_module, 'SPropProblemArray')
make_head(_module, 'SPropTagArray')
make_head(_module, 'SPropValue')
make_head(_module, 'SPropertyRestriction')
make_head(_module, 'SRealArray')
make_head(_module, 'SRestriction')
make_head(_module, 'SRow')
make_head(_module, 'SRowSet')
make_head(_module, 'SShortArray')
make_head(_module, 'SSizeRestriction')
make_head(_module, 'SSortOrder')
make_head(_module, 'SSortOrderSet')
make_head(_module, 'SSubRestriction')
make_head(_module, 'STATUS_OBJECT_NOTIFICATION')
make_head(_module, 'SWStringArray')
make_head(_module, 'TABLE_NOTIFICATION')
make_head(_module, 'WABEXTDISPLAY')
make_head(_module, 'WABIMPORTPARAM')
make_head(_module, 'WAB_PARAM')
make_head(_module, '_WABACTIONITEM')
make_head(_module, '__UPV')
