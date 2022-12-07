from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.AddressBook
import win32more.System.Com
import win32more.System.Com.StructuredStorage
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
class __UPV(Union):
    i: Int16
    l: Int32
    ul: UInt32
    flt: Single
    dbl: Double
    b: UInt16
    cur: win32more.System.Com.CY
    at: Double
    ft: win32more.Foundation.FILETIME
    lpszA: win32more.Foundation.PSTR
    bin: win32more.System.AddressBook.SBinary
    lpszW: win32more.Foundation.PWSTR
    lpguid: POINTER(Guid)
    li: win32more.Foundation.LARGE_INTEGER
    MVi: win32more.System.AddressBook.SShortArray
    MVl: win32more.System.AddressBook.SLongArray
    MVflt: win32more.System.AddressBook.SRealArray
    MVdbl: win32more.System.AddressBook.SDoubleArray
    MVcur: win32more.System.AddressBook.SCurrencyArray
    MVat: win32more.System.AddressBook.SAppTimeArray
    MVft: win32more.System.AddressBook.SDateTimeArray
    MVbin: win32more.System.AddressBook.SBinaryArray
    MVszA: win32more.System.AddressBook.SLPSTRArray
    MVszW: win32more.System.AddressBook.SWStringArray
    MVguid: win32more.System.AddressBook.SGuidArray
    MVli: win32more.System.AddressBook.SLargeIntegerArray
    err: Int32
    x: Int32
class _WABACTIONITEM(Structure):
    pass
class ADRENTRY(Structure):
    ulReserved1: UInt32
    cValues: UInt32
    rgPropVals: POINTER(win32more.System.AddressBook.SPropValue_head)
class ADRLIST(Structure):
    cEntries: UInt32
    aEntries: win32more.System.AddressBook.ADRENTRY * 1
class ADRPARM(Structure):
    cbABContEntryID: UInt32
    lpABContEntryID: POINTER(win32more.System.AddressBook.ENTRYID_head)
    ulFlags: UInt32
    lpReserved: c_void_p
    ulHelpContext: UInt32
    lpszHelpFileName: POINTER(SByte)
    lpfnABSDI: win32more.System.AddressBook.LPFNABSDI
    lpfnDismiss: win32more.System.AddressBook.LPFNDISMISS
    lpvDismissContext: c_void_p
    lpszCaption: POINTER(SByte)
    lpszNewEntryTitle: POINTER(SByte)
    lpszDestWellsTitle: POINTER(SByte)
    cDestFields: UInt32
    nDestFieldFocus: UInt32
    lppszDestTitles: POINTER(POINTER(SByte))
    lpulDestComps: POINTER(UInt32)
    lpContRestriction: POINTER(win32more.System.AddressBook.SRestriction_head)
    lpHierRestriction: POINTER(win32more.System.AddressBook.SRestriction_head)
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
E_IMAPI_REQUEST_CANCELLED: win32more.Foundation.HRESULT = -1062600702
E_IMAPI_RECORDER_REQUIRED: win32more.Foundation.HRESULT = -1062600701
S_IMAPI_SPEEDADJUSTED: win32more.Foundation.HRESULT = 11141124
S_IMAPI_ROTATIONADJUSTED: win32more.Foundation.HRESULT = 11141125
S_IMAPI_BOTHADJUSTED: win32more.Foundation.HRESULT = 11141126
E_IMAPI_BURN_VERIFICATION_FAILED: win32more.Foundation.HRESULT = -1062600697
S_IMAPI_COMMAND_HAS_SENSE_DATA: win32more.Foundation.HRESULT = 11141632
E_IMAPI_RECORDER_NO_SUCH_MODE_PAGE: win32more.Foundation.HRESULT = -1062600191
E_IMAPI_RECORDER_MEDIA_NO_MEDIA: win32more.Foundation.HRESULT = -1062600190
E_IMAPI_RECORDER_MEDIA_INCOMPATIBLE: win32more.Foundation.HRESULT = -1062600189
E_IMAPI_RECORDER_MEDIA_UPSIDE_DOWN: win32more.Foundation.HRESULT = -1062600188
E_IMAPI_RECORDER_MEDIA_BECOMING_READY: win32more.Foundation.HRESULT = -1062600187
E_IMAPI_RECORDER_MEDIA_FORMAT_IN_PROGRESS: win32more.Foundation.HRESULT = -1062600186
E_IMAPI_RECORDER_MEDIA_BUSY: win32more.Foundation.HRESULT = -1062600185
E_IMAPI_RECORDER_INVALID_MODE_PARAMETERS: win32more.Foundation.HRESULT = -1062600184
E_IMAPI_RECORDER_MEDIA_WRITE_PROTECTED: win32more.Foundation.HRESULT = -1062600183
E_IMAPI_RECORDER_NO_SUCH_FEATURE: win32more.Foundation.HRESULT = -1062600182
E_IMAPI_RECORDER_FEATURE_IS_NOT_CURRENT: win32more.Foundation.HRESULT = -1062600181
E_IMAPI_RECORDER_GET_CONFIGURATION_NOT_SUPPORTED: win32more.Foundation.HRESULT = -1062600180
E_IMAPI_RECORDER_COMMAND_TIMEOUT: win32more.Foundation.HRESULT = -1062600179
E_IMAPI_RECORDER_DVD_STRUCTURE_NOT_PRESENT: win32more.Foundation.HRESULT = -1062600178
E_IMAPI_RECORDER_MEDIA_SPEED_MISMATCH: win32more.Foundation.HRESULT = -1062600177
E_IMAPI_RECORDER_LOCKED: win32more.Foundation.HRESULT = -1062600176
E_IMAPI_RECORDER_CLIENT_NAME_IS_NOT_VALID: win32more.Foundation.HRESULT = -1062600175
E_IMAPI_RECORDER_MEDIA_NOT_FORMATTED: win32more.Foundation.HRESULT = -1062600174
E_IMAPI_RECORDER_INVALID_RESPONSE_FROM_DEVICE: win32more.Foundation.HRESULT = -1062599937
E_IMAPI_LOSS_OF_STREAMING: win32more.Foundation.HRESULT = -1062599936
E_IMAPI_UNEXPECTED_RESPONSE_FROM_DEVICE: win32more.Foundation.HRESULT = -1062599935
S_IMAPI_WRITE_NOT_IN_PROGRESS: win32more.Foundation.HRESULT = 11141890
E_IMAPI_DF2DATA_WRITE_IN_PROGRESS: win32more.Foundation.HRESULT = -1062599680
E_IMAPI_DF2DATA_WRITE_NOT_IN_PROGRESS: win32more.Foundation.HRESULT = -1062599679
E_IMAPI_DF2DATA_INVALID_MEDIA_STATE: win32more.Foundation.HRESULT = -1062599678
E_IMAPI_DF2DATA_STREAM_NOT_SUPPORTED: win32more.Foundation.HRESULT = -1062599677
E_IMAPI_DF2DATA_STREAM_TOO_LARGE_FOR_CURRENT_MEDIA: win32more.Foundation.HRESULT = -1062599676
E_IMAPI_DF2DATA_MEDIA_NOT_BLANK: win32more.Foundation.HRESULT = -1062599675
E_IMAPI_DF2DATA_MEDIA_IS_NOT_SUPPORTED: win32more.Foundation.HRESULT = -1062599674
E_IMAPI_DF2DATA_RECORDER_NOT_SUPPORTED: win32more.Foundation.HRESULT = -1062599673
E_IMAPI_DF2DATA_CLIENT_NAME_IS_NOT_VALID: win32more.Foundation.HRESULT = -1062599672
E_IMAPI_DF2TAO_WRITE_IN_PROGRESS: win32more.Foundation.HRESULT = -1062599424
E_IMAPI_DF2TAO_WRITE_NOT_IN_PROGRESS: win32more.Foundation.HRESULT = -1062599423
E_IMAPI_DF2TAO_MEDIA_IS_NOT_PREPARED: win32more.Foundation.HRESULT = -1062599422
E_IMAPI_DF2TAO_MEDIA_IS_PREPARED: win32more.Foundation.HRESULT = -1062599421
E_IMAPI_DF2TAO_PROPERTY_FOR_BLANK_MEDIA_ONLY: win32more.Foundation.HRESULT = -1062599420
E_IMAPI_DF2TAO_TABLE_OF_CONTENTS_EMPTY_DISC: win32more.Foundation.HRESULT = -1062599419
E_IMAPI_DF2TAO_MEDIA_IS_NOT_BLANK: win32more.Foundation.HRESULT = -1062599418
E_IMAPI_DF2TAO_MEDIA_IS_NOT_SUPPORTED: win32more.Foundation.HRESULT = -1062599417
E_IMAPI_DF2TAO_TRACK_LIMIT_REACHED: win32more.Foundation.HRESULT = -1062599416
E_IMAPI_DF2TAO_NOT_ENOUGH_SPACE: win32more.Foundation.HRESULT = -1062599415
E_IMAPI_DF2TAO_NO_RECORDER_SPECIFIED: win32more.Foundation.HRESULT = -1062599414
E_IMAPI_DF2TAO_INVALID_ISRC: win32more.Foundation.HRESULT = -1062599413
E_IMAPI_DF2TAO_INVALID_MCN: win32more.Foundation.HRESULT = -1062599412
E_IMAPI_DF2TAO_STREAM_NOT_SUPPORTED: win32more.Foundation.HRESULT = -1062599411
E_IMAPI_DF2TAO_RECORDER_NOT_SUPPORTED: win32more.Foundation.HRESULT = -1062599410
E_IMAPI_DF2TAO_CLIENT_NAME_IS_NOT_VALID: win32more.Foundation.HRESULT = -1062599409
E_IMAPI_DF2RAW_WRITE_IN_PROGRESS: win32more.Foundation.HRESULT = -1062599168
E_IMAPI_DF2RAW_WRITE_NOT_IN_PROGRESS: win32more.Foundation.HRESULT = -1062599167
E_IMAPI_DF2RAW_MEDIA_IS_NOT_PREPARED: win32more.Foundation.HRESULT = -1062599166
E_IMAPI_DF2RAW_MEDIA_IS_PREPARED: win32more.Foundation.HRESULT = -1062599165
E_IMAPI_DF2RAW_CLIENT_NAME_IS_NOT_VALID: win32more.Foundation.HRESULT = -1062599164
E_IMAPI_DF2RAW_MEDIA_IS_NOT_BLANK: win32more.Foundation.HRESULT = -1062599162
E_IMAPI_DF2RAW_MEDIA_IS_NOT_SUPPORTED: win32more.Foundation.HRESULT = -1062599161
E_IMAPI_DF2RAW_NOT_ENOUGH_SPACE: win32more.Foundation.HRESULT = -1062599159
E_IMAPI_DF2RAW_NO_RECORDER_SPECIFIED: win32more.Foundation.HRESULT = -1062599158
E_IMAPI_DF2RAW_STREAM_NOT_SUPPORTED: win32more.Foundation.HRESULT = -1062599155
E_IMAPI_DF2RAW_DATA_BLOCK_TYPE_NOT_SUPPORTED: win32more.Foundation.HRESULT = -1062599154
E_IMAPI_DF2RAW_STREAM_LEADIN_TOO_SHORT: win32more.Foundation.HRESULT = -1062599153
E_IMAPI_DF2RAW_RECORDER_NOT_SUPPORTED: win32more.Foundation.HRESULT = -1062599152
E_IMAPI_ERASE_RECORDER_IN_USE: win32more.Foundation.HRESULT = -2136340224
E_IMAPI_ERASE_ONLY_ONE_RECORDER_SUPPORTED: win32more.Foundation.HRESULT = -2136340223
E_IMAPI_ERASE_DISC_INFORMATION_TOO_SMALL: win32more.Foundation.HRESULT = -2136340222
E_IMAPI_ERASE_MODE_PAGE_2A_TOO_SMALL: win32more.Foundation.HRESULT = -2136340221
E_IMAPI_ERASE_MEDIA_IS_NOT_ERASABLE: win32more.Foundation.HRESULT = -2136340220
E_IMAPI_ERASE_DRIVE_FAILED_ERASE_COMMAND: win32more.Foundation.HRESULT = -2136340219
E_IMAPI_ERASE_TOOK_LONGER_THAN_ONE_HOUR: win32more.Foundation.HRESULT = -2136340218
E_IMAPI_ERASE_UNEXPECTED_DRIVE_RESPONSE_DURING_ERASE: win32more.Foundation.HRESULT = -2136340217
E_IMAPI_ERASE_DRIVE_FAILED_SPINUP_COMMAND: win32more.Foundation.HRESULT = -2136340216
E_IMAPI_ERASE_MEDIA_IS_NOT_SUPPORTED: win32more.Foundation.HRESULT = -1062598391
E_IMAPI_ERASE_RECORDER_NOT_SUPPORTED: win32more.Foundation.HRESULT = -1062598390
E_IMAPI_ERASE_CLIENT_NAME_IS_NOT_VALID: win32more.Foundation.HRESULT = -1062598389
E_IMAPI_RAW_IMAGE_IS_READ_ONLY: win32more.Foundation.HRESULT = -2136339968
E_IMAPI_RAW_IMAGE_TOO_MANY_TRACKS: win32more.Foundation.HRESULT = -2136339967
E_IMAPI_RAW_IMAGE_SECTOR_TYPE_NOT_SUPPORTED: win32more.Foundation.HRESULT = -2136339966
E_IMAPI_RAW_IMAGE_NO_TRACKS: win32more.Foundation.HRESULT = -2136339965
E_IMAPI_RAW_IMAGE_TRACKS_ALREADY_ADDED: win32more.Foundation.HRESULT = -2136339964
E_IMAPI_RAW_IMAGE_INSUFFICIENT_SPACE: win32more.Foundation.HRESULT = -2136339963
E_IMAPI_RAW_IMAGE_TOO_MANY_TRACK_INDEXES: win32more.Foundation.HRESULT = -2136339962
E_IMAPI_RAW_IMAGE_TRACK_INDEX_NOT_FOUND: win32more.Foundation.HRESULT = -2136339961
S_IMAPI_RAW_IMAGE_TRACK_INDEX_ALREADY_EXISTS: win32more.Foundation.HRESULT = 11143688
E_IMAPI_RAW_IMAGE_TRACK_INDEX_OFFSET_ZERO_CANNOT_BE_CLEARED: win32more.Foundation.HRESULT = -2136339959
E_IMAPI_RAW_IMAGE_TRACK_INDEX_TOO_CLOSE_TO_OTHER_INDEX: win32more.Foundation.HRESULT = -2136339958
FACILITY_IMAPI2: UInt32 = 170
IMAPI_E_FSI_INTERNAL_ERROR: win32more.Foundation.HRESULT = -1062555392
IMAPI_E_INVALID_PARAM: win32more.Foundation.HRESULT = -1062555391
IMAPI_E_READONLY: win32more.Foundation.HRESULT = -1062555390
IMAPI_E_NO_OUTPUT: win32more.Foundation.HRESULT = -1062555389
IMAPI_E_INVALID_VOLUME_NAME: win32more.Foundation.HRESULT = -1062555388
IMAPI_E_INVALID_DATE: win32more.Foundation.HRESULT = -1062555387
IMAPI_E_FILE_SYSTEM_NOT_EMPTY: win32more.Foundation.HRESULT = -1062555386
IMAPI_E_NOT_FILE: win32more.Foundation.HRESULT = -1062555384
IMAPI_E_NOT_DIR: win32more.Foundation.HRESULT = -1062555383
IMAPI_E_DIR_NOT_EMPTY: win32more.Foundation.HRESULT = -1062555382
IMAPI_E_NOT_IN_FILE_SYSTEM: win32more.Foundation.HRESULT = -1062555381
IMAPI_E_INVALID_PATH: win32more.Foundation.HRESULT = -1062555376
IMAPI_E_RESTRICTED_NAME_VIOLATION: win32more.Foundation.HRESULT = -1062555375
IMAPI_E_DUP_NAME: win32more.Foundation.HRESULT = -1062555374
IMAPI_E_NO_UNIQUE_NAME: win32more.Foundation.HRESULT = -1062555373
IMAPI_E_ITEM_NOT_FOUND: win32more.Foundation.HRESULT = -1062555368
IMAPI_E_FILE_NOT_FOUND: win32more.Foundation.HRESULT = -1062555367
IMAPI_E_DIR_NOT_FOUND: win32more.Foundation.HRESULT = -1062555366
IMAPI_E_IMAGE_SIZE_LIMIT: win32more.Foundation.HRESULT = -1062555360
IMAPI_E_IMAGE_TOO_BIG: win32more.Foundation.HRESULT = -1062555359
IMAPI_E_DATA_STREAM_INCONSISTENCY: win32more.Foundation.HRESULT = -1062555352
IMAPI_E_DATA_STREAM_READ_FAILURE: win32more.Foundation.HRESULT = -1062555351
IMAPI_E_DATA_STREAM_CREATE_FAILURE: win32more.Foundation.HRESULT = -1062555350
IMAPI_E_DIRECTORY_READ_FAILURE: win32more.Foundation.HRESULT = -1062555349
IMAPI_E_TOO_MANY_DIRS: win32more.Foundation.HRESULT = -1062555344
IMAPI_E_ISO9660_LEVELS: win32more.Foundation.HRESULT = -1062555343
IMAPI_E_DATA_TOO_BIG: win32more.Foundation.HRESULT = -1062555342
IMAPI_E_INCOMPATIBLE_PREVIOUS_SESSION: win32more.Foundation.HRESULT = -1062555341
IMAPI_E_STASHFILE_OPEN_FAILURE: win32more.Foundation.HRESULT = -1062555336
IMAPI_E_STASHFILE_SEEK_FAILURE: win32more.Foundation.HRESULT = -1062555335
IMAPI_E_STASHFILE_WRITE_FAILURE: win32more.Foundation.HRESULT = -1062555334
IMAPI_E_STASHFILE_READ_FAILURE: win32more.Foundation.HRESULT = -1062555333
IMAPI_E_INVALID_WORKING_DIRECTORY: win32more.Foundation.HRESULT = -1062555328
IMAPI_E_WORKING_DIRECTORY_SPACE: win32more.Foundation.HRESULT = -1062555327
IMAPI_E_STASHFILE_MOVE: win32more.Foundation.HRESULT = -1062555326
IMAPI_E_BOOT_IMAGE_DATA: win32more.Foundation.HRESULT = -1062555320
IMAPI_E_BOOT_OBJECT_CONFLICT: win32more.Foundation.HRESULT = -1062555319
IMAPI_E_BOOT_EMULATION_IMAGE_SIZE_MISMATCH: win32more.Foundation.HRESULT = -1062555318
IMAPI_E_EMPTY_DISC: win32more.Foundation.HRESULT = -1062555312
IMAPI_E_NO_SUPPORTED_FILE_SYSTEM: win32more.Foundation.HRESULT = -1062555311
IMAPI_E_FILE_SYSTEM_NOT_FOUND: win32more.Foundation.HRESULT = -1062555310
IMAPI_E_FILE_SYSTEM_READ_CONSISTENCY_ERROR: win32more.Foundation.HRESULT = -1062555309
IMAPI_E_FILE_SYSTEM_FEATURE_NOT_SUPPORTED: win32more.Foundation.HRESULT = -1062555308
IMAPI_E_IMPORT_TYPE_COLLISION_FILE_EXISTS_AS_DIRECTORY: win32more.Foundation.HRESULT = -1062555307
IMAPI_E_IMPORT_SEEK_FAILURE: win32more.Foundation.HRESULT = -1062555306
IMAPI_E_IMPORT_READ_FAILURE: win32more.Foundation.HRESULT = -1062555305
IMAPI_E_DISC_MISMATCH: win32more.Foundation.HRESULT = -1062555304
IMAPI_E_IMPORT_MEDIA_NOT_ALLOWED: win32more.Foundation.HRESULT = -1062555303
IMAPI_E_UDF_NOT_WRITE_COMPATIBLE: win32more.Foundation.HRESULT = -1062555302
IMAPI_E_INCOMPATIBLE_MULTISESSION_TYPE: win32more.Foundation.HRESULT = -1062555301
IMAPI_E_NO_COMPATIBLE_MULTISESSION_TYPE: win32more.Foundation.HRESULT = -1062555300
IMAPI_E_MULTISESSION_NOT_SET: win32more.Foundation.HRESULT = -1062555299
IMAPI_E_IMPORT_TYPE_COLLISION_DIRECTORY_EXISTS_AS_FILE: win32more.Foundation.HRESULT = -1062555298
IMAPI_S_IMAGE_FEATURE_NOT_SUPPORTED: win32more.Foundation.HRESULT = 11186527
IMAPI_E_PROPERTY_NOT_ACCESSIBLE: win32more.Foundation.HRESULT = -1062555296
IMAPI_E_UDF_REVISION_CHANGE_NOT_ALLOWED: win32more.Foundation.HRESULT = -1062555295
IMAPI_E_BAD_MULTISESSION_PARAMETER: win32more.Foundation.HRESULT = -1062555294
IMAPI_E_FILE_SYSTEM_CHANGE_NOT_ALLOWED: win32more.Foundation.HRESULT = -1062555293
IMAPI_E_IMAGEMANAGER_IMAGE_NOT_ALIGNED: win32more.Foundation.HRESULT = -1062555136
IMAPI_E_IMAGEMANAGER_NO_VALID_VD_FOUND: win32more.Foundation.HRESULT = -1062555135
IMAPI_E_IMAGEMANAGER_NO_IMAGE: win32more.Foundation.HRESULT = -1062555134
IMAPI_E_IMAGEMANAGER_IMAGE_TOO_BIG: win32more.Foundation.HRESULT = -1062555133
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
def CreateTable(lpInterface: POINTER(Guid), lpAllocateBuffer: win32more.System.AddressBook.LPALLOCATEBUFFER, lpAllocateMore: win32more.System.AddressBook.LPALLOCATEMORE, lpFreeBuffer: win32more.System.AddressBook.LPFREEBUFFER, lpvReserved: c_void_p, ulTableType: UInt32, ulPropTagIndexColumn: UInt32, lpSPropTagArrayColumns: POINTER(win32more.System.AddressBook.SPropTagArray_head), lppTableData: POINTER(win32more.System.AddressBook.ITableData_head)) -> Int32: ...
@winfunctype('MAPI32.dll')
def CreateIProp(lpInterface: POINTER(Guid), lpAllocateBuffer: win32more.System.AddressBook.LPALLOCATEBUFFER, lpAllocateMore: win32more.System.AddressBook.LPALLOCATEMORE, lpFreeBuffer: win32more.System.AddressBook.LPFREEBUFFER, lpvReserved: c_void_p, lppPropData: POINTER(win32more.System.AddressBook.IPropData_head)) -> Int32: ...
@winfunctype('MAPI32.dll')
def MAPIInitIdle(lpvReserved: c_void_p) -> Int32: ...
@winfunctype('MAPI32.dll')
def MAPIDeinitIdle() -> Void: ...
@winfunctype('MAPI32.dll')
def FtgRegisterIdleRoutine(lpfnIdle: win32more.System.AddressBook.PFNIDLE, lpvIdleParam: c_void_p, priIdle: Int16, csecIdle: UInt32, iroIdle: UInt16) -> c_void_p: ...
@winfunctype('MAPI32.dll')
def DeregisterIdleRoutine(ftg: c_void_p) -> Void: ...
@winfunctype('MAPI32.dll')
def EnableIdleRoutine(ftg: c_void_p, fEnable: win32more.Foundation.BOOL) -> Void: ...
@winfunctype('MAPI32.dll')
def ChangeIdleRoutine(ftg: c_void_p, lpfnIdle: win32more.System.AddressBook.PFNIDLE, lpvIdleParam: c_void_p, priIdle: Int16, csecIdle: UInt32, iroIdle: UInt16, ircIdle: UInt16) -> Void: ...
@winfunctype('MAPI32.dll')
def MAPIGetDefaultMalloc() -> win32more.System.Com.IMalloc_head: ...
@winfunctype('MAPI32.dll')
def OpenStreamOnFile(lpAllocateBuffer: win32more.System.AddressBook.LPALLOCATEBUFFER, lpFreeBuffer: win32more.System.AddressBook.LPFREEBUFFER, ulFlags: UInt32, lpszFileName: POINTER(SByte), lpszPrefix: POINTER(SByte), lppStream: POINTER(win32more.System.Com.IStream_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def PropCopyMore(lpSPropValueDest: POINTER(win32more.System.AddressBook.SPropValue_head), lpSPropValueSrc: POINTER(win32more.System.AddressBook.SPropValue_head), lpfAllocMore: win32more.System.AddressBook.LPALLOCATEMORE, lpvObject: c_void_p) -> Int32: ...
@winfunctype('MAPI32.dll')
def UlPropSize(lpSPropValue: POINTER(win32more.System.AddressBook.SPropValue_head)) -> UInt32: ...
@winfunctype('MAPI32.dll')
def FEqualNames(lpName1: POINTER(win32more.System.AddressBook.MAPINAMEID_head), lpName2: POINTER(win32more.System.AddressBook.MAPINAMEID_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('MAPI32.dll')
def FPropContainsProp(lpSPropValueDst: POINTER(win32more.System.AddressBook.SPropValue_head), lpSPropValueSrc: POINTER(win32more.System.AddressBook.SPropValue_head), ulFuzzyLevel: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('MAPI32.dll')
def FPropCompareProp(lpSPropValue1: POINTER(win32more.System.AddressBook.SPropValue_head), ulRelOp: UInt32, lpSPropValue2: POINTER(win32more.System.AddressBook.SPropValue_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('MAPI32.dll')
def LPropCompareProp(lpSPropValueA: POINTER(win32more.System.AddressBook.SPropValue_head), lpSPropValueB: POINTER(win32more.System.AddressBook.SPropValue_head)) -> Int32: ...
@winfunctype('MAPI32.dll')
def HrAddColumns(lptbl: win32more.System.AddressBook.IMAPITable_head, lpproptagColumnsNew: POINTER(win32more.System.AddressBook.SPropTagArray_head), lpAllocateBuffer: win32more.System.AddressBook.LPALLOCATEBUFFER, lpFreeBuffer: win32more.System.AddressBook.LPFREEBUFFER) -> win32more.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def HrAddColumnsEx(lptbl: win32more.System.AddressBook.IMAPITable_head, lpproptagColumnsNew: POINTER(win32more.System.AddressBook.SPropTagArray_head), lpAllocateBuffer: win32more.System.AddressBook.LPALLOCATEBUFFER, lpFreeBuffer: win32more.System.AddressBook.LPFREEBUFFER, lpfnFilterColumns: IntPtr) -> win32more.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def HrAllocAdviseSink(lpfnCallback: win32more.System.AddressBook.LPNOTIFCALLBACK, lpvContext: c_void_p, lppAdviseSink: POINTER(win32more.System.AddressBook.IMAPIAdviseSink_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def HrThisThreadAdviseSink(lpAdviseSink: win32more.System.AddressBook.IMAPIAdviseSink_head, lppAdviseSink: POINTER(win32more.System.AddressBook.IMAPIAdviseSink_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def HrDispatchNotifications(ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def BuildDisplayTable(lpAllocateBuffer: win32more.System.AddressBook.LPALLOCATEBUFFER, lpAllocateMore: win32more.System.AddressBook.LPALLOCATEMORE, lpFreeBuffer: win32more.System.AddressBook.LPFREEBUFFER, lpMalloc: win32more.System.Com.IMalloc_head, hInstance: win32more.Foundation.HINSTANCE, cPages: UInt32, lpPage: POINTER(win32more.System.AddressBook.DTPAGE_head), ulFlags: UInt32, lppTable: POINTER(win32more.System.AddressBook.IMAPITable_head), lppTblData: POINTER(win32more.System.AddressBook.ITableData_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def ScCountNotifications(cNotifications: Int32, lpNotifications: POINTER(win32more.System.AddressBook.NOTIFICATION_head), lpcb: POINTER(UInt32)) -> Int32: ...
@winfunctype('MAPI32.dll')
def ScCopyNotifications(cNotification: Int32, lpNotifications: POINTER(win32more.System.AddressBook.NOTIFICATION_head), lpvDst: c_void_p, lpcb: POINTER(UInt32)) -> Int32: ...
@winfunctype('MAPI32.dll')
def ScRelocNotifications(cNotification: Int32, lpNotifications: POINTER(win32more.System.AddressBook.NOTIFICATION_head), lpvBaseOld: c_void_p, lpvBaseNew: c_void_p, lpcb: POINTER(UInt32)) -> Int32: ...
@winfunctype('MAPI32.dll')
def ScCountProps(cValues: Int32, lpPropArray: POINTER(win32more.System.AddressBook.SPropValue_head), lpcb: POINTER(UInt32)) -> Int32: ...
@winfunctype('MAPI32.dll')
def LpValFindProp(ulPropTag: UInt32, cValues: UInt32, lpPropArray: POINTER(win32more.System.AddressBook.SPropValue_head)) -> POINTER(win32more.System.AddressBook.SPropValue_head): ...
@winfunctype('MAPI32.dll')
def ScCopyProps(cValues: Int32, lpPropArray: POINTER(win32more.System.AddressBook.SPropValue_head), lpvDst: c_void_p, lpcb: POINTER(UInt32)) -> Int32: ...
@winfunctype('MAPI32.dll')
def ScRelocProps(cValues: Int32, lpPropArray: POINTER(win32more.System.AddressBook.SPropValue_head), lpvBaseOld: c_void_p, lpvBaseNew: c_void_p, lpcb: POINTER(UInt32)) -> Int32: ...
@winfunctype('MAPI32.dll')
def ScDupPropset(cValues: Int32, lpPropArray: POINTER(win32more.System.AddressBook.SPropValue_head), lpAllocateBuffer: win32more.System.AddressBook.LPALLOCATEBUFFER, lppPropArray: POINTER(POINTER(win32more.System.AddressBook.SPropValue_head))) -> Int32: ...
@winfunctype('MAPI32.dll')
def UlAddRef(lpunk: c_void_p) -> UInt32: ...
@winfunctype('MAPI32.dll')
def UlRelease(lpunk: c_void_p) -> UInt32: ...
@winfunctype('MAPI32.dll')
def HrGetOneProp(lpMapiProp: win32more.System.AddressBook.IMAPIProp_head, ulPropTag: UInt32, lppProp: POINTER(POINTER(win32more.System.AddressBook.SPropValue_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def HrSetOneProp(lpMapiProp: win32more.System.AddressBook.IMAPIProp_head, lpProp: POINTER(win32more.System.AddressBook.SPropValue_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def FPropExists(lpMapiProp: win32more.System.AddressBook.IMAPIProp_head, ulPropTag: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('MAPI32.dll')
def PpropFindProp(lpPropArray: POINTER(win32more.System.AddressBook.SPropValue_head), cValues: UInt32, ulPropTag: UInt32) -> POINTER(win32more.System.AddressBook.SPropValue_head): ...
@winfunctype('MAPI32.dll')
def FreePadrlist(lpAdrlist: POINTER(win32more.System.AddressBook.ADRLIST_head)) -> Void: ...
@winfunctype('MAPI32.dll')
def FreeProws(lpRows: POINTER(win32more.System.AddressBook.SRowSet_head)) -> Void: ...
@winfunctype('MAPI32.dll')
def HrQueryAllRows(lpTable: win32more.System.AddressBook.IMAPITable_head, lpPropTags: POINTER(win32more.System.AddressBook.SPropTagArray_head), lpRestriction: POINTER(win32more.System.AddressBook.SRestriction_head), lpSortOrderSet: POINTER(win32more.System.AddressBook.SSortOrderSet_head), crowsMax: Int32, lppRows: POINTER(POINTER(win32more.System.AddressBook.SRowSet_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def SzFindCh(lpsz: POINTER(SByte), ch: UInt16) -> POINTER(SByte): ...
@winfunctype('MAPI32.dll')
def SzFindLastCh(lpsz: POINTER(SByte), ch: UInt16) -> POINTER(SByte): ...
@winfunctype('MAPI32.dll')
def SzFindSz(lpsz: POINTER(SByte), lpszKey: POINTER(SByte)) -> POINTER(SByte): ...
@winfunctype('MAPI32.dll')
def UFromSz(lpsz: POINTER(SByte)) -> UInt32: ...
@winfunctype('MAPI32.dll')
def ScUNCFromLocalPath(lpszLocal: win32more.Foundation.PSTR, lpszUNC: win32more.Foundation.PSTR, cchUNC: UInt32) -> Int32: ...
@winfunctype('MAPI32.dll')
def ScLocalPathFromUNC(lpszUNC: win32more.Foundation.PSTR, lpszLocal: win32more.Foundation.PSTR, cchLocal: UInt32) -> Int32: ...
@winfunctype('MAPI32.dll')
def FtAddFt(ftAddend1: win32more.Foundation.FILETIME, ftAddend2: win32more.Foundation.FILETIME) -> win32more.Foundation.FILETIME: ...
@winfunctype('MAPI32.dll')
def FtMulDwDw(ftMultiplicand: UInt32, ftMultiplier: UInt32) -> win32more.Foundation.FILETIME: ...
@winfunctype('MAPI32.dll')
def FtMulDw(ftMultiplier: UInt32, ftMultiplicand: win32more.Foundation.FILETIME) -> win32more.Foundation.FILETIME: ...
@winfunctype('MAPI32.dll')
def FtSubFt(ftMinuend: win32more.Foundation.FILETIME, ftSubtrahend: win32more.Foundation.FILETIME) -> win32more.Foundation.FILETIME: ...
@winfunctype('MAPI32.dll')
def FtNegFt(ft: win32more.Foundation.FILETIME) -> win32more.Foundation.FILETIME: ...
@winfunctype('MAPI32.dll')
def ScCreateConversationIndex(cbParent: UInt32, lpbParent: c_char_p_no, lpcbConvIndex: POINTER(UInt32), lppbConvIndex: POINTER(c_char_p_no)) -> Int32: ...
@winfunctype('MAPI32.dll')
def WrapStoreEntryID(ulFlags: UInt32, lpszDLLName: POINTER(SByte), cbOrigEntry: UInt32, lpOrigEntry: POINTER(win32more.System.AddressBook.ENTRYID_head), lpcbWrappedEntry: POINTER(UInt32), lppWrappedEntry: POINTER(POINTER(win32more.System.AddressBook.ENTRYID_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def RTFSync(lpMessage: win32more.System.AddressBook.IMessage_head, ulFlags: UInt32, lpfMessageUpdated: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def WrapCompressedRTFStream(lpCompressedRTFStream: win32more.System.Com.IStream_head, ulFlags: UInt32, lpUncompressedRTFStream: POINTER(win32more.System.Com.IStream_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def HrIStorageFromStream(lpUnkIn: win32more.System.Com.IUnknown_head, lpInterface: POINTER(Guid), ulFlags: UInt32, lppStorageOut: POINTER(win32more.System.Com.StructuredStorage.IStorage_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def ScInitMapiUtil(ulFlags: UInt32) -> Int32: ...
@winfunctype('MAPI32.dll')
def DeinitMapiUtil() -> Void: ...
@winfunctype_pointer
def CALLERRELEASE(ulCallerData: UInt32, lpTblData: win32more.System.AddressBook.ITableData_head, lpVue: win32more.System.AddressBook.IMAPITable_head) -> Void: ...
class DTBLBUTTON(Structure):
    ulbLpszLabel: UInt32
    ulFlags: UInt32
    ulPRControl: UInt32
class DTBLCHECKBOX(Structure):
    ulbLpszLabel: UInt32
    ulFlags: UInt32
    ulPRPropertyName: UInt32
class DTBLCOMBOBOX(Structure):
    ulbLpszCharsAllowed: UInt32
    ulFlags: UInt32
    ulNumCharsAllowed: UInt32
    ulPRPropertyName: UInt32
    ulPRTableName: UInt32
class DTBLDDLBX(Structure):
    ulFlags: UInt32
    ulPRDisplayProperty: UInt32
    ulPRSetProperty: UInt32
    ulPRTableName: UInt32
class DTBLEDIT(Structure):
    ulbLpszCharsAllowed: UInt32
    ulFlags: UInt32
    ulNumCharsAllowed: UInt32
    ulPropTag: UInt32
class DTBLGROUPBOX(Structure):
    ulbLpszLabel: UInt32
    ulFlags: UInt32
class DTBLLABEL(Structure):
    ulbLpszLabelName: UInt32
    ulFlags: UInt32
class DTBLLBX(Structure):
    ulFlags: UInt32
    ulPRSetProperty: UInt32
    ulPRTableName: UInt32
class DTBLMVDDLBX(Structure):
    ulFlags: UInt32
    ulMVPropTag: UInt32
class DTBLMVLISTBOX(Structure):
    ulFlags: UInt32
    ulMVPropTag: UInt32
class DTBLPAGE(Structure):
    ulbLpszLabel: UInt32
    ulFlags: UInt32
    ulbLpszComponent: UInt32
    ulContext: UInt32
class DTBLRADIOBUTTON(Structure):
    ulbLpszLabel: UInt32
    ulFlags: UInt32
    ulcButtons: UInt32
    ulPropTag: UInt32
    lReturnValue: Int32
class DTCTL(Structure):
    ulCtlType: UInt32
    ulCtlFlags: UInt32
    lpbNotif: c_char_p_no
    cbNotif: UInt32
    lpszFilter: POINTER(SByte)
    ulItemID: UInt32
    ctl: _ctl_e__Union
    class _ctl_e__Union(Union):
        lpv: c_void_p
        lplabel: POINTER(win32more.System.AddressBook.DTBLLABEL_head)
        lpedit: POINTER(win32more.System.AddressBook.DTBLEDIT_head)
        lplbx: POINTER(win32more.System.AddressBook.DTBLLBX_head)
        lpcombobox: POINTER(win32more.System.AddressBook.DTBLCOMBOBOX_head)
        lpddlbx: POINTER(win32more.System.AddressBook.DTBLDDLBX_head)
        lpcheckbox: POINTER(win32more.System.AddressBook.DTBLCHECKBOX_head)
        lpgroupbox: POINTER(win32more.System.AddressBook.DTBLGROUPBOX_head)
        lpbutton: POINTER(win32more.System.AddressBook.DTBLBUTTON_head)
        lpradiobutton: POINTER(win32more.System.AddressBook.DTBLRADIOBUTTON_head)
        lpmvlbx: POINTER(win32more.System.AddressBook.DTBLMVLISTBOX_head)
        lpmvddlbx: POINTER(win32more.System.AddressBook.DTBLMVDDLBX_head)
        lppage: POINTER(win32more.System.AddressBook.DTBLPAGE_head)
class DTPAGE(Structure):
    cctl: UInt32
    lpszResourceName: POINTER(SByte)
    Anonymous: _Anonymous_e__Union
    lpctl: POINTER(win32more.System.AddressBook.DTCTL_head)
    class _Anonymous_e__Union(Union):
        lpszComponent: POINTER(SByte)
        ulItemID: UInt32
class ENTRYID(Structure):
    abFlags: Byte * 4
    ab: Byte * 1
class ERROR_NOTIFICATION(Structure):
    cbEntryID: UInt32
    lpEntryID: POINTER(win32more.System.AddressBook.ENTRYID_head)
    scode: Int32
    ulFlags: UInt32
    lpMAPIError: POINTER(win32more.System.AddressBook.MAPIERROR_head)
class EXTENDED_NOTIFICATION(Structure):
    ulEvent: UInt32
    cb: UInt32
    pbEventParameters: c_char_p_no
class FlagList(Structure):
    cFlags: UInt32
    ulFlag: UInt32 * 1
class FLATENTRY(Structure):
    cb: UInt32
    abEntry: Byte * 1
class FLATENTRYLIST(Structure):
    cEntries: UInt32
    cbEntries: UInt32
    abEntries: Byte * 1
class FLATMTSIDLIST(Structure):
    cMTSIDs: UInt32
    cbMTSIDs: UInt32
    abMTSIDs: Byte * 1
Gender = Int32
Gender_genderUnspecified: Gender = 0
Gender_genderFemale: Gender = 1
Gender_genderMale: Gender = 2
class IABContainer(c_void_p):
    extends: win32more.System.AddressBook.IMAPIContainer
    @commethod(19)
    def CreateEntry(cbEntryID: UInt32, lpEntryID: POINTER(win32more.System.AddressBook.ENTRYID_head), ulCreateFlags: UInt32, lppMAPIPropEntry: POINTER(win32more.System.AddressBook.IMAPIProp_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def CopyEntries(lpEntries: POINTER(win32more.System.AddressBook.SBinaryArray_head), ulUIParam: UIntPtr, lpProgress: win32more.System.AddressBook.IMAPIProgress_head, ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def DeleteEntries(lpEntries: POINTER(win32more.System.AddressBook.SBinaryArray_head), ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def ResolveNames(lpPropTagArray: POINTER(win32more.System.AddressBook.SPropTagArray_head), ulFlags: UInt32, lpAdrList: POINTER(win32more.System.AddressBook.ADRLIST_head), lpFlagList: POINTER(win32more.System.AddressBook.FlagList_head)) -> win32more.Foundation.HRESULT: ...
class IAddrBook(c_void_p):
    extends: win32more.System.AddressBook.IMAPIProp
    @commethod(14)
    def OpenEntry(cbEntryID: UInt32, lpEntryID: POINTER(win32more.System.AddressBook.ENTRYID_head), lpInterface: POINTER(Guid), ulFlags: UInt32, lpulObjType: POINTER(UInt32), lppUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def CompareEntryIDs(cbEntryID1: UInt32, lpEntryID1: POINTER(win32more.System.AddressBook.ENTRYID_head), cbEntryID2: UInt32, lpEntryID2: POINTER(win32more.System.AddressBook.ENTRYID_head), ulFlags: UInt32, lpulResult: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def Advise(cbEntryID: UInt32, lpEntryID: POINTER(win32more.System.AddressBook.ENTRYID_head), ulEventMask: UInt32, lpAdviseSink: win32more.System.AddressBook.IMAPIAdviseSink_head, lpulConnection: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def Unadvise(ulConnection: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def CreateOneOff(lpszName: POINTER(SByte), lpszAdrType: POINTER(SByte), lpszAddress: POINTER(SByte), ulFlags: UInt32, lpcbEntryID: POINTER(UInt32), lppEntryID: POINTER(POINTER(win32more.System.AddressBook.ENTRYID_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def NewEntry(ulUIParam: UInt32, ulFlags: UInt32, cbEIDContainer: UInt32, lpEIDContainer: POINTER(win32more.System.AddressBook.ENTRYID_head), cbEIDNewEntryTpl: UInt32, lpEIDNewEntryTpl: POINTER(win32more.System.AddressBook.ENTRYID_head), lpcbEIDNewEntry: POINTER(UInt32), lppEIDNewEntry: POINTER(POINTER(win32more.System.AddressBook.ENTRYID_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def ResolveName(ulUIParam: UIntPtr, ulFlags: UInt32, lpszNewEntryTitle: POINTER(SByte), lpAdrList: POINTER(win32more.System.AddressBook.ADRLIST_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def Address(lpulUIParam: POINTER(UInt32), lpAdrParms: POINTER(win32more.System.AddressBook.ADRPARM_head), lppAdrList: POINTER(POINTER(win32more.System.AddressBook.ADRLIST_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def Details(lpulUIParam: POINTER(UIntPtr), lpfnDismiss: win32more.System.AddressBook.LPFNDISMISS, lpvDismissContext: c_void_p, cbEntryID: UInt32, lpEntryID: POINTER(win32more.System.AddressBook.ENTRYID_head), lpfButtonCallback: win32more.System.AddressBook.LPFNBUTTON, lpvButtonContext: c_void_p, lpszButtonText: POINTER(SByte), ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def RecipOptions(ulUIParam: UInt32, ulFlags: UInt32, lpRecip: POINTER(win32more.System.AddressBook.ADRENTRY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def QueryDefaultRecipOpt(lpszAdrType: POINTER(SByte), ulFlags: UInt32, lpcValues: POINTER(UInt32), lppOptions: POINTER(POINTER(win32more.System.AddressBook.SPropValue_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def GetPAB(lpcbEntryID: POINTER(UInt32), lppEntryID: POINTER(POINTER(win32more.System.AddressBook.ENTRYID_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def SetPAB(cbEntryID: UInt32, lpEntryID: POINTER(win32more.System.AddressBook.ENTRYID_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def GetDefaultDir(lpcbEntryID: POINTER(UInt32), lppEntryID: POINTER(POINTER(win32more.System.AddressBook.ENTRYID_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def SetDefaultDir(cbEntryID: UInt32, lpEntryID: POINTER(win32more.System.AddressBook.ENTRYID_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def GetSearchPath(ulFlags: UInt32, lppSearchPath: POINTER(POINTER(win32more.System.AddressBook.SRowSet_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def SetSearchPath(ulFlags: UInt32, lpSearchPath: POINTER(win32more.System.AddressBook.SRowSet_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def PrepareRecips(ulFlags: UInt32, lpPropTagArray: POINTER(win32more.System.AddressBook.SPropTagArray_head), lpRecipList: POINTER(win32more.System.AddressBook.ADRLIST_head)) -> win32more.Foundation.HRESULT: ...
class IAttach(c_void_p):
    extends: win32more.System.AddressBook.IMAPIProp
class IDistList(c_void_p):
    extends: win32more.System.AddressBook.IMAPIContainer
    @commethod(19)
    def CreateEntry(cbEntryID: UInt32, lpEntryID: POINTER(win32more.System.AddressBook.ENTRYID_head), ulCreateFlags: UInt32, lppMAPIPropEntry: POINTER(win32more.System.AddressBook.IMAPIProp_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def CopyEntries(lpEntries: POINTER(win32more.System.AddressBook.SBinaryArray_head), ulUIParam: UIntPtr, lpProgress: win32more.System.AddressBook.IMAPIProgress_head, ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def DeleteEntries(lpEntries: POINTER(win32more.System.AddressBook.SBinaryArray_head), ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def ResolveNames(lpPropTagArray: POINTER(win32more.System.AddressBook.SPropTagArray_head), ulFlags: UInt32, lpAdrList: POINTER(win32more.System.AddressBook.ADRLIST_head), lpFlagList: POINTER(win32more.System.AddressBook.FlagList_head)) -> win32more.Foundation.HRESULT: ...
class IMailUser(c_void_p):
    extends: win32more.System.AddressBook.IMAPIProp
class IMAPIAdviseSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    @commethod(3)
    def OnNotify(cNotif: UInt32, lpNotifications: POINTER(win32more.System.AddressBook.NOTIFICATION_head)) -> UInt32: ...
class IMAPIContainer(c_void_p):
    extends: win32more.System.AddressBook.IMAPIProp
    @commethod(14)
    def GetContentsTable(ulFlags: UInt32, lppTable: POINTER(win32more.System.AddressBook.IMAPITable_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetHierarchyTable(ulFlags: UInt32, lppTable: POINTER(win32more.System.AddressBook.IMAPITable_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def OpenEntry(cbEntryID: UInt32, lpEntryID: POINTER(win32more.System.AddressBook.ENTRYID_head), lpInterface: POINTER(Guid), ulFlags: UInt32, lpulObjType: POINTER(UInt32), lppUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def SetSearchCriteria(lpRestriction: POINTER(win32more.System.AddressBook.SRestriction_head), lpContainerList: POINTER(win32more.System.AddressBook.SBinaryArray_head), ulSearchFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetSearchCriteria(ulFlags: UInt32, lppRestriction: POINTER(POINTER(win32more.System.AddressBook.SRestriction_head)), lppContainerList: POINTER(POINTER(win32more.System.AddressBook.SBinaryArray_head)), lpulSearchState: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IMAPIControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    @commethod(3)
    def GetLastError(hResult: win32more.Foundation.HRESULT, ulFlags: UInt32, lppMAPIError: POINTER(POINTER(win32more.System.AddressBook.MAPIERROR_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Activate(ulFlags: UInt32, ulUIParam: UIntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetState(ulFlags: UInt32, lpulState: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IMAPIFolder(c_void_p):
    extends: win32more.System.AddressBook.IMAPIContainer
    @commethod(19)
    def CreateMessage(lpInterface: POINTER(Guid), ulFlags: UInt32, lppMessage: POINTER(win32more.System.AddressBook.IMessage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def CopyMessages(lpMsgList: POINTER(win32more.System.AddressBook.SBinaryArray_head), lpInterface: POINTER(Guid), lpDestFolder: c_void_p, ulUIParam: UIntPtr, lpProgress: win32more.System.AddressBook.IMAPIProgress_head, ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def DeleteMessages(lpMsgList: POINTER(win32more.System.AddressBook.SBinaryArray_head), ulUIParam: UIntPtr, lpProgress: win32more.System.AddressBook.IMAPIProgress_head, ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def CreateFolder(ulFolderType: UInt32, lpszFolderName: POINTER(SByte), lpszFolderComment: POINTER(SByte), lpInterface: POINTER(Guid), ulFlags: UInt32, lppFolder: POINTER(win32more.System.AddressBook.IMAPIFolder_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def CopyFolder(cbEntryID: UInt32, lpEntryID: POINTER(win32more.System.AddressBook.ENTRYID_head), lpInterface: POINTER(Guid), lpDestFolder: c_void_p, lpszNewFolderName: POINTER(SByte), ulUIParam: UIntPtr, lpProgress: win32more.System.AddressBook.IMAPIProgress_head, ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def DeleteFolder(cbEntryID: UInt32, lpEntryID: POINTER(win32more.System.AddressBook.ENTRYID_head), ulUIParam: UIntPtr, lpProgress: win32more.System.AddressBook.IMAPIProgress_head, ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def SetReadFlags(lpMsgList: POINTER(win32more.System.AddressBook.SBinaryArray_head), ulUIParam: UIntPtr, lpProgress: win32more.System.AddressBook.IMAPIProgress_head, ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def GetMessageStatus(cbEntryID: UInt32, lpEntryID: POINTER(win32more.System.AddressBook.ENTRYID_head), ulFlags: UInt32, lpulMessageStatus: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def SetMessageStatus(cbEntryID: UInt32, lpEntryID: POINTER(win32more.System.AddressBook.ENTRYID_head), ulNewStatus: UInt32, ulNewStatusMask: UInt32, lpulOldStatus: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def SaveContentsSort(lpSortCriteria: POINTER(win32more.System.AddressBook.SSortOrderSet_head), ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def EmptyFolder(ulUIParam: UIntPtr, lpProgress: win32more.System.AddressBook.IMAPIProgress_head, ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
class IMAPIProgress(c_void_p):
    extends: win32more.System.Com.IUnknown
    @commethod(3)
    def Progress(ulValue: UInt32, ulCount: UInt32, ulTotal: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetFlags(lpulFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetMax(lpulMax: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetMin(lpulMin: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetLimits(lpulMin: POINTER(UInt32), lpulMax: POINTER(UInt32), lpulFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IMAPIProp(c_void_p):
    extends: win32more.System.Com.IUnknown
    @commethod(3)
    def GetLastError(hResult: win32more.Foundation.HRESULT, ulFlags: UInt32, lppMAPIError: POINTER(POINTER(win32more.System.AddressBook.MAPIERROR_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SaveChanges(ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetProps(lpPropTagArray: POINTER(win32more.System.AddressBook.SPropTagArray_head), ulFlags: UInt32, lpcValues: POINTER(UInt32), lppPropArray: POINTER(POINTER(win32more.System.AddressBook.SPropValue_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetPropList(ulFlags: UInt32, lppPropTagArray: POINTER(POINTER(win32more.System.AddressBook.SPropTagArray_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def OpenProperty(ulPropTag: UInt32, lpiid: POINTER(Guid), ulInterfaceOptions: UInt32, ulFlags: UInt32, lppUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetProps(cValues: UInt32, lpPropArray: POINTER(win32more.System.AddressBook.SPropValue_head), lppProblems: POINTER(POINTER(win32more.System.AddressBook.SPropProblemArray_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def DeleteProps(lpPropTagArray: POINTER(win32more.System.AddressBook.SPropTagArray_head), lppProblems: POINTER(POINTER(win32more.System.AddressBook.SPropProblemArray_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def CopyTo(ciidExclude: UInt32, rgiidExclude: POINTER(Guid), lpExcludeProps: POINTER(win32more.System.AddressBook.SPropTagArray_head), ulUIParam: UIntPtr, lpProgress: win32more.System.AddressBook.IMAPIProgress_head, lpInterface: POINTER(Guid), lpDestObj: c_void_p, ulFlags: UInt32, lppProblems: POINTER(POINTER(win32more.System.AddressBook.SPropProblemArray_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def CopyProps(lpIncludeProps: POINTER(win32more.System.AddressBook.SPropTagArray_head), ulUIParam: UIntPtr, lpProgress: win32more.System.AddressBook.IMAPIProgress_head, lpInterface: POINTER(Guid), lpDestObj: c_void_p, ulFlags: UInt32, lppProblems: POINTER(POINTER(win32more.System.AddressBook.SPropProblemArray_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetNamesFromIDs(lppPropTags: POINTER(POINTER(win32more.System.AddressBook.SPropTagArray_head)), lpPropSetGuid: POINTER(Guid), ulFlags: UInt32, lpcPropNames: POINTER(UInt32), lpppPropNames: POINTER(POINTER(POINTER(win32more.System.AddressBook.MAPINAMEID_head)))) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetIDsFromNames(cPropNames: UInt32, lppPropNames: POINTER(POINTER(win32more.System.AddressBook.MAPINAMEID_head)), ulFlags: UInt32, lppPropTags: POINTER(POINTER(win32more.System.AddressBook.SPropTagArray_head))) -> win32more.Foundation.HRESULT: ...
class IMAPIStatus(c_void_p):
    extends: win32more.System.AddressBook.IMAPIProp
    @commethod(14)
    def ValidateState(ulUIParam: UIntPtr, ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SettingsDialog(ulUIParam: UIntPtr, ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def ChangePassword(lpOldPass: POINTER(SByte), lpNewPass: POINTER(SByte), ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def FlushQueues(ulUIParam: UIntPtr, cbTargetTransport: UInt32, lpTargetTransport: POINTER(win32more.System.AddressBook.ENTRYID_head), ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
class IMAPITable(c_void_p):
    extends: win32more.System.Com.IUnknown
    @commethod(3)
    def GetLastError(hResult: win32more.Foundation.HRESULT, ulFlags: UInt32, lppMAPIError: POINTER(POINTER(win32more.System.AddressBook.MAPIERROR_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Advise(ulEventMask: UInt32, lpAdviseSink: win32more.System.AddressBook.IMAPIAdviseSink_head, lpulConnection: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Unadvise(ulConnection: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetStatus(lpulTableStatus: POINTER(UInt32), lpulTableType: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetColumns(lpPropTagArray: POINTER(win32more.System.AddressBook.SPropTagArray_head), ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def QueryColumns(ulFlags: UInt32, lpPropTagArray: POINTER(POINTER(win32more.System.AddressBook.SPropTagArray_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetRowCount(ulFlags: UInt32, lpulCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SeekRow(bkOrigin: UInt32, lRowCount: Int32, lplRowsSought: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SeekRowApprox(ulNumerator: UInt32, ulDenominator: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def QueryPosition(lpulRow: POINTER(UInt32), lpulNumerator: POINTER(UInt32), lpulDenominator: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def FindRow(lpRestriction: POINTER(win32more.System.AddressBook.SRestriction_head), bkOrigin: UInt32, ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def Restrict(lpRestriction: POINTER(win32more.System.AddressBook.SRestriction_head), ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def CreateBookmark(lpbkPosition: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def FreeBookmark(bkPosition: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def SortTable(lpSortCriteria: POINTER(win32more.System.AddressBook.SSortOrderSet_head), ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def QuerySortOrder(lppSortCriteria: POINTER(POINTER(win32more.System.AddressBook.SSortOrderSet_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def QueryRows(lRowCount: Int32, ulFlags: UInt32, lppRows: POINTER(POINTER(win32more.System.AddressBook.SRowSet_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def Abort() -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def ExpandRow(cbInstanceKey: UInt32, pbInstanceKey: c_char_p_no, ulRowCount: UInt32, ulFlags: UInt32, lppRows: POINTER(POINTER(win32more.System.AddressBook.SRowSet_head)), lpulMoreRows: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def CollapseRow(cbInstanceKey: UInt32, pbInstanceKey: c_char_p_no, ulFlags: UInt32, lpulRowCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def WaitForCompletion(ulFlags: UInt32, ulTimeout: UInt32, lpulTableStatus: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def GetCollapseState(ulFlags: UInt32, cbInstanceKey: UInt32, lpbInstanceKey: c_char_p_no, lpcbCollapseState: POINTER(UInt32), lppbCollapseState: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def SetCollapseState(ulFlags: UInt32, cbCollapseState: UInt32, pbCollapseState: c_char_p_no, lpbkLocation: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IMessage(c_void_p):
    extends: win32more.System.AddressBook.IMAPIProp
    @commethod(14)
    def GetAttachmentTable(ulFlags: UInt32, lppTable: POINTER(win32more.System.AddressBook.IMAPITable_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def OpenAttach(ulAttachmentNum: UInt32, lpInterface: POINTER(Guid), ulFlags: UInt32, lppAttach: POINTER(win32more.System.AddressBook.IAttach_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def CreateAttach(lpInterface: POINTER(Guid), ulFlags: UInt32, lpulAttachmentNum: POINTER(UInt32), lppAttach: POINTER(win32more.System.AddressBook.IAttach_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def DeleteAttach(ulAttachmentNum: UInt32, ulUIParam: UIntPtr, lpProgress: win32more.System.AddressBook.IMAPIProgress_head, ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetRecipientTable(ulFlags: UInt32, lppTable: POINTER(win32more.System.AddressBook.IMAPITable_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def ModifyRecipients(ulFlags: UInt32, lpMods: POINTER(win32more.System.AddressBook.ADRLIST_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def SubmitMessage(ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def SetReadFlag(ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
class IMsgStore(c_void_p):
    extends: win32more.System.AddressBook.IMAPIProp
    @commethod(14)
    def Advise(cbEntryID: UInt32, lpEntryID: POINTER(win32more.System.AddressBook.ENTRYID_head), ulEventMask: UInt32, lpAdviseSink: win32more.System.AddressBook.IMAPIAdviseSink_head, lpulConnection: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def Unadvise(ulConnection: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def CompareEntryIDs(cbEntryID1: UInt32, lpEntryID1: POINTER(win32more.System.AddressBook.ENTRYID_head), cbEntryID2: UInt32, lpEntryID2: POINTER(win32more.System.AddressBook.ENTRYID_head), ulFlags: UInt32, lpulResult: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def OpenEntry(cbEntryID: UInt32, lpEntryID: POINTER(win32more.System.AddressBook.ENTRYID_head), lpInterface: POINTER(Guid), ulFlags: UInt32, lpulObjType: POINTER(UInt32), ppUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def SetReceiveFolder(lpszMessageClass: POINTER(SByte), ulFlags: UInt32, cbEntryID: UInt32, lpEntryID: POINTER(win32more.System.AddressBook.ENTRYID_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetReceiveFolder(lpszMessageClass: POINTER(SByte), ulFlags: UInt32, lpcbEntryID: POINTER(UInt32), lppEntryID: POINTER(POINTER(win32more.System.AddressBook.ENTRYID_head)), lppszExplicitClass: POINTER(POINTER(SByte))) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetReceiveFolderTable(ulFlags: UInt32, lppTable: POINTER(win32more.System.AddressBook.IMAPITable_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def StoreLogoff(lpulFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def AbortSubmit(cbEntryID: UInt32, lpEntryID: POINTER(win32more.System.AddressBook.ENTRYID_head), ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def GetOutgoingQueue(ulFlags: UInt32, lppTable: POINTER(win32more.System.AddressBook.IMAPITable_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def SetLockState(lpMessage: win32more.System.AddressBook.IMessage_head, ulLockState: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def FinishedMsg(ulFlags: UInt32, cbEntryID: UInt32, lpEntryID: POINTER(win32more.System.AddressBook.ENTRYID_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def NotifyNewMail(lpNotification: POINTER(win32more.System.AddressBook.NOTIFICATION_head)) -> win32more.Foundation.HRESULT: ...
class IProfSect(c_void_p):
    extends: win32more.System.AddressBook.IMAPIProp
class IPropData(c_void_p):
    extends: win32more.System.AddressBook.IMAPIProp
    @commethod(14)
    def HrSetObjAccess(ulAccess: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def HrSetPropAccess(lpPropTagArray: POINTER(win32more.System.AddressBook.SPropTagArray_head), rgulAccess: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def HrGetPropAccess(lppPropTagArray: POINTER(POINTER(win32more.System.AddressBook.SPropTagArray_head)), lprgulAccess: POINTER(POINTER(UInt32))) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def HrAddObjProps(lppPropTagArray: POINTER(win32more.System.AddressBook.SPropTagArray_head), lprgulAccess: POINTER(POINTER(win32more.System.AddressBook.SPropProblemArray_head))) -> win32more.Foundation.HRESULT: ...
class IProviderAdmin(c_void_p):
    extends: win32more.System.Com.IUnknown
    @commethod(3)
    def GetLastError(hResult: win32more.Foundation.HRESULT, ulFlags: UInt32, lppMAPIError: POINTER(POINTER(win32more.System.AddressBook.MAPIERROR_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetProviderTable(ulFlags: UInt32, lppTable: POINTER(win32more.System.AddressBook.IMAPITable_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CreateProvider(lpszProvider: POINTER(SByte), cValues: UInt32, lpProps: POINTER(win32more.System.AddressBook.SPropValue_head), ulUIParam: UIntPtr, ulFlags: UInt32, lpUID: POINTER(win32more.System.AddressBook.MAPIUID_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def DeleteProvider(lpUID: POINTER(win32more.System.AddressBook.MAPIUID_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def OpenProfileSection(lpUID: POINTER(win32more.System.AddressBook.MAPIUID_head), lpInterface: POINTER(Guid), ulFlags: UInt32, lppProfSect: POINTER(win32more.System.AddressBook.IProfSect_head)) -> win32more.Foundation.HRESULT: ...
class ITableData(c_void_p):
    extends: win32more.System.Com.IUnknown
    @commethod(3)
    def HrGetView(lpSSortOrderSet: POINTER(win32more.System.AddressBook.SSortOrderSet_head), lpfCallerRelease: POINTER(win32more.System.AddressBook.CALLERRELEASE), ulCallerData: UInt32, lppMAPITable: POINTER(win32more.System.AddressBook.IMAPITable_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def HrModifyRow(param0: POINTER(win32more.System.AddressBook.SRow_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def HrDeleteRow(lpSPropValue: POINTER(win32more.System.AddressBook.SPropValue_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def HrQueryRow(lpsPropValue: POINTER(win32more.System.AddressBook.SPropValue_head), lppSRow: POINTER(POINTER(win32more.System.AddressBook.SRow_head)), lpuliRow: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def HrEnumRow(ulRowNumber: UInt32, lppSRow: POINTER(POINTER(win32more.System.AddressBook.SRow_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def HrNotify(ulFlags: UInt32, cValues: UInt32, lpSPropValue: POINTER(win32more.System.AddressBook.SPropValue_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def HrInsertRow(uliRow: UInt32, lpSRow: POINTER(win32more.System.AddressBook.SRow_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def HrModifyRows(ulFlags: UInt32, lpSRowSet: POINTER(win32more.System.AddressBook.SRowSet_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def HrDeleteRows(ulFlags: UInt32, lprowsetToDelete: POINTER(win32more.System.AddressBook.SRowSet_head), cRowsDeleted: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IWABExtInit(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ea22ebf0-87a4-11d1-9a-cf-00-a0-c9-1f-9c-8b')
    @commethod(3)
    def Initialize(lpWABExtDisplay: POINTER(win32more.System.AddressBook.WABEXTDISPLAY_head)) -> win32more.Foundation.HRESULT: ...
class IWABObject(c_void_p):
    extends: win32more.System.Com.IUnknown
    @commethod(3)
    def GetLastError(hResult: win32more.Foundation.HRESULT, ulFlags: UInt32, lppMAPIError: POINTER(POINTER(win32more.System.AddressBook.MAPIERROR_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def AllocateBuffer(cbSize: UInt32, lppBuffer: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def AllocateMore(cbSize: UInt32, lpObject: c_void_p, lppBuffer: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def FreeBuffer(lpBuffer: c_void_p) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Backup(lpFileName: win32more.Foundation.PSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Import(lpWIP: win32more.Foundation.PSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Find(lpIAB: win32more.System.AddressBook.IAddrBook_head, hWnd: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def VCardDisplay(lpIAB: win32more.System.AddressBook.IAddrBook_head, hWnd: win32more.Foundation.HWND, lpszFileName: win32more.Foundation.PSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def LDAPUrl(lpIAB: win32more.System.AddressBook.IAddrBook_head, hWnd: win32more.Foundation.HWND, ulFlags: UInt32, lpszURL: win32more.Foundation.PSTR, lppMailUser: POINTER(win32more.System.AddressBook.IMailUser_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def VCardCreate(lpIAB: win32more.System.AddressBook.IAddrBook_head, ulFlags: UInt32, lpszVCard: win32more.Foundation.PSTR, lpMailUser: win32more.System.AddressBook.IMailUser_head) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def VCardRetrieve(lpIAB: win32more.System.AddressBook.IAddrBook_head, ulFlags: UInt32, lpszVCard: win32more.Foundation.PSTR, lppMailUser: POINTER(win32more.System.AddressBook.IMailUser_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetMe(lpIAB: win32more.System.AddressBook.IAddrBook_head, ulFlags: UInt32, lpdwAction: POINTER(UInt32), lpsbEID: POINTER(win32more.System.AddressBook.SBinary_head), hwnd: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SetMe(lpIAB: win32more.System.AddressBook.IAddrBook_head, ulFlags: UInt32, sbEID: win32more.System.AddressBook.SBinary, hwnd: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def LPALLOCATEBUFFER(cbSize: UInt32, lppBuffer: POINTER(c_void_p)) -> Int32: ...
@winfunctype_pointer
def LPALLOCATEMORE(cbSize: UInt32, lpObject: c_void_p, lppBuffer: POINTER(c_void_p)) -> Int32: ...
@winfunctype_pointer
def LPCREATECONVERSATIONINDEX(cbParent: UInt32, lpbParent: c_char_p_no, lpcbConvIndex: POINTER(UInt32), lppbConvIndex: POINTER(c_char_p_no)) -> Int32: ...
@winfunctype_pointer
def LPDISPATCHNOTIFICATIONS(ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def LPFNABSDI(ulUIParam: UIntPtr, lpvmsg: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def LPFNBUTTON(ulUIParam: UIntPtr, lpvContext: c_void_p, cbEntryID: UInt32, lpSelection: POINTER(win32more.System.AddressBook.ENTRYID_head), ulFlags: UInt32) -> Int32: ...
@winfunctype_pointer
def LPFNDISMISS(ulUIParam: UIntPtr, lpvContext: c_void_p) -> Void: ...
@winfunctype_pointer
def LPFREEBUFFER(lpBuffer: c_void_p) -> UInt32: ...
@winfunctype_pointer
def LPNOTIFCALLBACK(lpvContext: c_void_p, cNotification: UInt32, lpNotifications: POINTER(win32more.System.AddressBook.NOTIFICATION_head)) -> Int32: ...
@winfunctype_pointer
def LPOPENSTREAMONFILE(lpAllocateBuffer: win32more.System.AddressBook.LPALLOCATEBUFFER, lpFreeBuffer: win32more.System.AddressBook.LPFREEBUFFER, ulFlags: UInt32, lpszFileName: POINTER(SByte), lpszPrefix: POINTER(SByte), lppStream: POINTER(win32more.System.Com.IStream_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def LPWABALLOCATEBUFFER(lpWABObject: win32more.System.AddressBook.IWABObject_head, cbSize: UInt32, lppBuffer: POINTER(c_void_p)) -> Int32: ...
@winfunctype_pointer
def LPWABALLOCATEMORE(lpWABObject: win32more.System.AddressBook.IWABObject_head, cbSize: UInt32, lpObject: c_void_p, lppBuffer: POINTER(c_void_p)) -> Int32: ...
@winfunctype_pointer
def LPWABFREEBUFFER(lpWABObject: win32more.System.AddressBook.IWABObject_head, lpBuffer: c_void_p) -> UInt32: ...
@winfunctype_pointer
def LPWABOPEN(lppAdrBook: POINTER(win32more.System.AddressBook.IAddrBook_head), lppWABObject: POINTER(win32more.System.AddressBook.IWABObject_head), lpWP: POINTER(win32more.System.AddressBook.WAB_PARAM_head), Reserved2: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def LPWABOPENEX(lppAdrBook: POINTER(win32more.System.AddressBook.IAddrBook_head), lppWABObject: POINTER(win32more.System.AddressBook.IWABObject_head), lpWP: POINTER(win32more.System.AddressBook.WAB_PARAM_head), Reserved: UInt32, fnAllocateBuffer: win32more.System.AddressBook.LPALLOCATEBUFFER, fnAllocateMore: win32more.System.AddressBook.LPALLOCATEMORE, fnFreeBuffer: win32more.System.AddressBook.LPFREEBUFFER) -> win32more.Foundation.HRESULT: ...
class MAPIERROR(Structure):
    ulVersion: UInt32
    lpszError: POINTER(SByte)
    lpszComponent: POINTER(SByte)
    ulLowLevelError: UInt32
    ulContext: UInt32
class MAPINAMEID(Structure):
    lpguid: POINTER(Guid)
    ulKind: UInt32
    Kind: _Kind_e__Union
    class _Kind_e__Union(Union):
        lID: Int32
        lpwstrName: win32more.Foundation.PWSTR
class MAPIUID(Structure):
    ab: Byte * 16
class MTSID(Structure):
    cb: UInt32
    ab: Byte * 1
class NEWMAIL_NOTIFICATION(Structure):
    cbEntryID: UInt32
    lpEntryID: POINTER(win32more.System.AddressBook.ENTRYID_head)
    cbParentID: UInt32
    lpParentID: POINTER(win32more.System.AddressBook.ENTRYID_head)
    ulFlags: UInt32
    lpszMessageClass: POINTER(SByte)
    ulMessageFlags: UInt32
class NOTIFICATION(Structure):
    ulEventType: UInt32
    ulAlignPad: UInt32
    info: _info_e__Union
    class _info_e__Union(Union):
        err: win32more.System.AddressBook.ERROR_NOTIFICATION
        newmail: win32more.System.AddressBook.NEWMAIL_NOTIFICATION
        obj: win32more.System.AddressBook.OBJECT_NOTIFICATION
        tab: win32more.System.AddressBook.TABLE_NOTIFICATION
        ext: win32more.System.AddressBook.EXTENDED_NOTIFICATION
        statobj: win32more.System.AddressBook.STATUS_OBJECT_NOTIFICATION
class NOTIFKEY(Structure):
    cb: UInt32
    ab: Byte * 1
class OBJECT_NOTIFICATION(Structure):
    cbEntryID: UInt32
    lpEntryID: POINTER(win32more.System.AddressBook.ENTRYID_head)
    ulObjType: UInt32
    cbParentID: UInt32
    lpParentID: POINTER(win32more.System.AddressBook.ENTRYID_head)
    cbOldID: UInt32
    lpOldID: POINTER(win32more.System.AddressBook.ENTRYID_head)
    cbOldParentID: UInt32
    lpOldParentID: POINTER(win32more.System.AddressBook.ENTRYID_head)
    lpPropTagArray: POINTER(win32more.System.AddressBook.SPropTagArray_head)
@winfunctype_pointer
def PFNIDLE(param0: c_void_p) -> win32more.Foundation.BOOL: ...
class SAndRestriction(Structure):
    cRes: UInt32
    lpRes: POINTER(win32more.System.AddressBook.SRestriction_head)
class SAppTimeArray(Structure):
    cValues: UInt32
    lpat: POINTER(Double)
class SBinary(Structure):
    cb: UInt32
    lpb: c_char_p_no
class SBinaryArray(Structure):
    cValues: UInt32
    lpbin: POINTER(win32more.System.AddressBook.SBinary_head)
class SBitMaskRestriction(Structure):
    relBMR: UInt32
    ulPropTag: UInt32
    ulMask: UInt32
class SCommentRestriction(Structure):
    cValues: UInt32
    lpRes: POINTER(win32more.System.AddressBook.SRestriction_head)
    lpProp: POINTER(win32more.System.AddressBook.SPropValue_head)
class SComparePropsRestriction(Structure):
    relop: UInt32
    ulPropTag1: UInt32
    ulPropTag2: UInt32
class SContentRestriction(Structure):
    ulFuzzyLevel: UInt32
    ulPropTag: UInt32
    lpProp: POINTER(win32more.System.AddressBook.SPropValue_head)
class SCurrencyArray(Structure):
    cValues: UInt32
    lpcur: POINTER(win32more.System.Com.CY_head)
class SDateTimeArray(Structure):
    cValues: UInt32
    lpft: POINTER(win32more.Foundation.FILETIME_head)
class SDoubleArray(Structure):
    cValues: UInt32
    lpdbl: POINTER(Double)
class SExistRestriction(Structure):
    ulReserved1: UInt32
    ulPropTag: UInt32
    ulReserved2: UInt32
class SGuidArray(Structure):
    cValues: UInt32
    lpguid: POINTER(Guid)
class SLargeIntegerArray(Structure):
    cValues: UInt32
    lpli: POINTER(win32more.Foundation.LARGE_INTEGER_head)
class SLongArray(Structure):
    cValues: UInt32
    lpl: POINTER(Int32)
class SLPSTRArray(Structure):
    cValues: UInt32
    lppszA: POINTER(win32more.Foundation.PSTR)
class SNotRestriction(Structure):
    ulReserved: UInt32
    lpRes: POINTER(win32more.System.AddressBook.SRestriction_head)
class SOrRestriction(Structure):
    cRes: UInt32
    lpRes: POINTER(win32more.System.AddressBook.SRestriction_head)
class SPropertyRestriction(Structure):
    relop: UInt32
    ulPropTag: UInt32
    lpProp: POINTER(win32more.System.AddressBook.SPropValue_head)
class SPropProblem(Structure):
    ulIndex: UInt32
    ulPropTag: UInt32
    scode: Int32
class SPropProblemArray(Structure):
    cProblem: UInt32
    aProblem: win32more.System.AddressBook.SPropProblem * 1
class SPropTagArray(Structure):
    cValues: UInt32
    aulPropTag: UInt32 * 1
class SPropValue(Structure):
    ulPropTag: UInt32
    dwAlignPad: UInt32
    Value: win32more.System.AddressBook.__UPV
class SRealArray(Structure):
    cValues: UInt32
    lpflt: POINTER(Single)
class SRestriction(Structure):
    rt: UInt32
    res: _res_e__Union
    class _res_e__Union(Union):
        resCompareProps: win32more.System.AddressBook.SComparePropsRestriction
        resAnd: win32more.System.AddressBook.SAndRestriction
        resOr: win32more.System.AddressBook.SOrRestriction
        resNot: win32more.System.AddressBook.SNotRestriction
        resContent: win32more.System.AddressBook.SContentRestriction
        resProperty: win32more.System.AddressBook.SPropertyRestriction
        resBitMask: win32more.System.AddressBook.SBitMaskRestriction
        resSize: win32more.System.AddressBook.SSizeRestriction
        resExist: win32more.System.AddressBook.SExistRestriction
        resSub: win32more.System.AddressBook.SSubRestriction
        resComment: win32more.System.AddressBook.SCommentRestriction
class SRow(Structure):
    ulAdrEntryPad: UInt32
    cValues: UInt32
    lpProps: POINTER(win32more.System.AddressBook.SPropValue_head)
class SRowSet(Structure):
    cRows: UInt32
    aRow: win32more.System.AddressBook.SRow * 1
class SShortArray(Structure):
    cValues: UInt32
    lpi: POINTER(Int16)
class SSizeRestriction(Structure):
    relop: UInt32
    ulPropTag: UInt32
    cb: UInt32
class SSortOrder(Structure):
    ulPropTag: UInt32
    ulOrder: UInt32
class SSortOrderSet(Structure):
    cSorts: UInt32
    cCategories: UInt32
    cExpanded: UInt32
    aSort: win32more.System.AddressBook.SSortOrder * 1
class SSubRestriction(Structure):
    ulSubObject: UInt32
    lpRes: POINTER(win32more.System.AddressBook.SRestriction_head)
class STATUS_OBJECT_NOTIFICATION(Structure):
    cbEntryID: UInt32
    lpEntryID: POINTER(win32more.System.AddressBook.ENTRYID_head)
    cValues: UInt32
    lpPropVals: POINTER(win32more.System.AddressBook.SPropValue_head)
class SWStringArray(Structure):
    cValues: UInt32
    lppszW: POINTER(win32more.Foundation.PWSTR)
class TABLE_NOTIFICATION(Structure):
    ulTableEvent: UInt32
    hResult: win32more.Foundation.HRESULT
    propIndex: win32more.System.AddressBook.SPropValue
    propPrior: win32more.System.AddressBook.SPropValue
    row: win32more.System.AddressBook.SRow
    ulPad: UInt32
class WAB_PARAM(Structure):
    cbSize: UInt32
    hwnd: win32more.Foundation.HWND
    szFileName: win32more.Foundation.PSTR
    ulFlags: UInt32
    guidPSExt: Guid
class WABEXTDISPLAY(Structure):
    cbSize: UInt32
    lpWABObject: win32more.System.AddressBook.IWABObject_head
    lpAdrBook: win32more.System.AddressBook.IAddrBook_head
    lpPropObj: win32more.System.AddressBook.IMAPIProp_head
    fReadOnly: win32more.Foundation.BOOL
    fDataChanged: win32more.Foundation.BOOL
    ulFlags: UInt32
    lpv: c_void_p
    lpsz: POINTER(SByte)
class WABIMPORTPARAM(Structure):
    cbSize: UInt32
    lpAdrBook: win32more.System.AddressBook.IAddrBook_head
    hWnd: win32more.Foundation.HWND
    ulFlags: UInt32
    lpszFileName: win32more.Foundation.PSTR
make_head(_module, '__UPV')
make_head(_module, '_WABACTIONITEM')
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
make_head(_module, 'FlagList')
make_head(_module, 'FLATENTRY')
make_head(_module, 'FLATENTRYLIST')
make_head(_module, 'FLATMTSIDLIST')
make_head(_module, 'IABContainer')
make_head(_module, 'IAddrBook')
make_head(_module, 'IAttach')
make_head(_module, 'IDistList')
make_head(_module, 'IMailUser')
make_head(_module, 'IMAPIAdviseSink')
make_head(_module, 'IMAPIContainer')
make_head(_module, 'IMAPIControl')
make_head(_module, 'IMAPIFolder')
make_head(_module, 'IMAPIProgress')
make_head(_module, 'IMAPIProp')
make_head(_module, 'IMAPIStatus')
make_head(_module, 'IMAPITable')
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
make_head(_module, 'SLargeIntegerArray')
make_head(_module, 'SLongArray')
make_head(_module, 'SLPSTRArray')
make_head(_module, 'SNotRestriction')
make_head(_module, 'SOrRestriction')
make_head(_module, 'SPropertyRestriction')
make_head(_module, 'SPropProblem')
make_head(_module, 'SPropProblemArray')
make_head(_module, 'SPropTagArray')
make_head(_module, 'SPropValue')
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
make_head(_module, 'WAB_PARAM')
make_head(_module, 'WABEXTDISPLAY')
make_head(_module, 'WABIMPORTPARAM')
__all__ = [
    "ADRENTRY",
    "ADRLIST",
    "ADRPARM",
    "BuildDisplayTable",
    "CALLERRELEASE",
    "ChangeIdleRoutine",
    "CreateIProp",
    "CreateTable",
    "DTBLBUTTON",
    "DTBLCHECKBOX",
    "DTBLCOMBOBOX",
    "DTBLDDLBX",
    "DTBLEDIT",
    "DTBLGROUPBOX",
    "DTBLLABEL",
    "DTBLLBX",
    "DTBLMVDDLBX",
    "DTBLMVLISTBOX",
    "DTBLPAGE",
    "DTBLRADIOBUTTON",
    "DTCTL",
    "DTPAGE",
    "DeinitMapiUtil",
    "DeregisterIdleRoutine",
    "ENTRYID",
    "ERROR_NOTIFICATION",
    "EXTENDED_NOTIFICATION",
    "E_IMAPI_BURN_VERIFICATION_FAILED",
    "E_IMAPI_DF2DATA_CLIENT_NAME_IS_NOT_VALID",
    "E_IMAPI_DF2DATA_INVALID_MEDIA_STATE",
    "E_IMAPI_DF2DATA_MEDIA_IS_NOT_SUPPORTED",
    "E_IMAPI_DF2DATA_MEDIA_NOT_BLANK",
    "E_IMAPI_DF2DATA_RECORDER_NOT_SUPPORTED",
    "E_IMAPI_DF2DATA_STREAM_NOT_SUPPORTED",
    "E_IMAPI_DF2DATA_STREAM_TOO_LARGE_FOR_CURRENT_MEDIA",
    "E_IMAPI_DF2DATA_WRITE_IN_PROGRESS",
    "E_IMAPI_DF2DATA_WRITE_NOT_IN_PROGRESS",
    "E_IMAPI_DF2RAW_CLIENT_NAME_IS_NOT_VALID",
    "E_IMAPI_DF2RAW_DATA_BLOCK_TYPE_NOT_SUPPORTED",
    "E_IMAPI_DF2RAW_MEDIA_IS_NOT_BLANK",
    "E_IMAPI_DF2RAW_MEDIA_IS_NOT_PREPARED",
    "E_IMAPI_DF2RAW_MEDIA_IS_NOT_SUPPORTED",
    "E_IMAPI_DF2RAW_MEDIA_IS_PREPARED",
    "E_IMAPI_DF2RAW_NOT_ENOUGH_SPACE",
    "E_IMAPI_DF2RAW_NO_RECORDER_SPECIFIED",
    "E_IMAPI_DF2RAW_RECORDER_NOT_SUPPORTED",
    "E_IMAPI_DF2RAW_STREAM_LEADIN_TOO_SHORT",
    "E_IMAPI_DF2RAW_STREAM_NOT_SUPPORTED",
    "E_IMAPI_DF2RAW_WRITE_IN_PROGRESS",
    "E_IMAPI_DF2RAW_WRITE_NOT_IN_PROGRESS",
    "E_IMAPI_DF2TAO_CLIENT_NAME_IS_NOT_VALID",
    "E_IMAPI_DF2TAO_INVALID_ISRC",
    "E_IMAPI_DF2TAO_INVALID_MCN",
    "E_IMAPI_DF2TAO_MEDIA_IS_NOT_BLANK",
    "E_IMAPI_DF2TAO_MEDIA_IS_NOT_PREPARED",
    "E_IMAPI_DF2TAO_MEDIA_IS_NOT_SUPPORTED",
    "E_IMAPI_DF2TAO_MEDIA_IS_PREPARED",
    "E_IMAPI_DF2TAO_NOT_ENOUGH_SPACE",
    "E_IMAPI_DF2TAO_NO_RECORDER_SPECIFIED",
    "E_IMAPI_DF2TAO_PROPERTY_FOR_BLANK_MEDIA_ONLY",
    "E_IMAPI_DF2TAO_RECORDER_NOT_SUPPORTED",
    "E_IMAPI_DF2TAO_STREAM_NOT_SUPPORTED",
    "E_IMAPI_DF2TAO_TABLE_OF_CONTENTS_EMPTY_DISC",
    "E_IMAPI_DF2TAO_TRACK_LIMIT_REACHED",
    "E_IMAPI_DF2TAO_WRITE_IN_PROGRESS",
    "E_IMAPI_DF2TAO_WRITE_NOT_IN_PROGRESS",
    "E_IMAPI_ERASE_CLIENT_NAME_IS_NOT_VALID",
    "E_IMAPI_ERASE_DISC_INFORMATION_TOO_SMALL",
    "E_IMAPI_ERASE_DRIVE_FAILED_ERASE_COMMAND",
    "E_IMAPI_ERASE_DRIVE_FAILED_SPINUP_COMMAND",
    "E_IMAPI_ERASE_MEDIA_IS_NOT_ERASABLE",
    "E_IMAPI_ERASE_MEDIA_IS_NOT_SUPPORTED",
    "E_IMAPI_ERASE_MODE_PAGE_2A_TOO_SMALL",
    "E_IMAPI_ERASE_ONLY_ONE_RECORDER_SUPPORTED",
    "E_IMAPI_ERASE_RECORDER_IN_USE",
    "E_IMAPI_ERASE_RECORDER_NOT_SUPPORTED",
    "E_IMAPI_ERASE_TOOK_LONGER_THAN_ONE_HOUR",
    "E_IMAPI_ERASE_UNEXPECTED_DRIVE_RESPONSE_DURING_ERASE",
    "E_IMAPI_LOSS_OF_STREAMING",
    "E_IMAPI_RAW_IMAGE_INSUFFICIENT_SPACE",
    "E_IMAPI_RAW_IMAGE_IS_READ_ONLY",
    "E_IMAPI_RAW_IMAGE_NO_TRACKS",
    "E_IMAPI_RAW_IMAGE_SECTOR_TYPE_NOT_SUPPORTED",
    "E_IMAPI_RAW_IMAGE_TOO_MANY_TRACKS",
    "E_IMAPI_RAW_IMAGE_TOO_MANY_TRACK_INDEXES",
    "E_IMAPI_RAW_IMAGE_TRACKS_ALREADY_ADDED",
    "E_IMAPI_RAW_IMAGE_TRACK_INDEX_NOT_FOUND",
    "E_IMAPI_RAW_IMAGE_TRACK_INDEX_OFFSET_ZERO_CANNOT_BE_CLEARED",
    "E_IMAPI_RAW_IMAGE_TRACK_INDEX_TOO_CLOSE_TO_OTHER_INDEX",
    "E_IMAPI_RECORDER_CLIENT_NAME_IS_NOT_VALID",
    "E_IMAPI_RECORDER_COMMAND_TIMEOUT",
    "E_IMAPI_RECORDER_DVD_STRUCTURE_NOT_PRESENT",
    "E_IMAPI_RECORDER_FEATURE_IS_NOT_CURRENT",
    "E_IMAPI_RECORDER_GET_CONFIGURATION_NOT_SUPPORTED",
    "E_IMAPI_RECORDER_INVALID_MODE_PARAMETERS",
    "E_IMAPI_RECORDER_INVALID_RESPONSE_FROM_DEVICE",
    "E_IMAPI_RECORDER_LOCKED",
    "E_IMAPI_RECORDER_MEDIA_BECOMING_READY",
    "E_IMAPI_RECORDER_MEDIA_BUSY",
    "E_IMAPI_RECORDER_MEDIA_FORMAT_IN_PROGRESS",
    "E_IMAPI_RECORDER_MEDIA_INCOMPATIBLE",
    "E_IMAPI_RECORDER_MEDIA_NOT_FORMATTED",
    "E_IMAPI_RECORDER_MEDIA_NO_MEDIA",
    "E_IMAPI_RECORDER_MEDIA_SPEED_MISMATCH",
    "E_IMAPI_RECORDER_MEDIA_UPSIDE_DOWN",
    "E_IMAPI_RECORDER_MEDIA_WRITE_PROTECTED",
    "E_IMAPI_RECORDER_NO_SUCH_FEATURE",
    "E_IMAPI_RECORDER_NO_SUCH_MODE_PAGE",
    "E_IMAPI_RECORDER_REQUIRED",
    "E_IMAPI_REQUEST_CANCELLED",
    "E_IMAPI_UNEXPECTED_RESPONSE_FROM_DEVICE",
    "EnableIdleRoutine",
    "FACILITY_IMAPI2",
    "FEqualNames",
    "FLATENTRY",
    "FLATENTRYLIST",
    "FLATMTSIDLIST",
    "FPropCompareProp",
    "FPropContainsProp",
    "FPropExists",
    "FlagList",
    "FreePadrlist",
    "FreeProws",
    "FtAddFt",
    "FtMulDw",
    "FtMulDwDw",
    "FtNegFt",
    "FtSubFt",
    "FtgRegisterIdleRoutine",
    "Gender",
    "Gender_genderFemale",
    "Gender_genderMale",
    "Gender_genderUnspecified",
    "HrAddColumns",
    "HrAddColumnsEx",
    "HrAllocAdviseSink",
    "HrDispatchNotifications",
    "HrGetOneProp",
    "HrIStorageFromStream",
    "HrQueryAllRows",
    "HrSetOneProp",
    "HrThisThreadAdviseSink",
    "IABContainer",
    "IAddrBook",
    "IAttach",
    "IDistList",
    "IMAPIAdviseSink",
    "IMAPIContainer",
    "IMAPIControl",
    "IMAPIFolder",
    "IMAPIProgress",
    "IMAPIProp",
    "IMAPIStatus",
    "IMAPITable",
    "IMAPI_E_BAD_MULTISESSION_PARAMETER",
    "IMAPI_E_BOOT_EMULATION_IMAGE_SIZE_MISMATCH",
    "IMAPI_E_BOOT_IMAGE_DATA",
    "IMAPI_E_BOOT_OBJECT_CONFLICT",
    "IMAPI_E_DATA_STREAM_CREATE_FAILURE",
    "IMAPI_E_DATA_STREAM_INCONSISTENCY",
    "IMAPI_E_DATA_STREAM_READ_FAILURE",
    "IMAPI_E_DATA_TOO_BIG",
    "IMAPI_E_DIRECTORY_READ_FAILURE",
    "IMAPI_E_DIR_NOT_EMPTY",
    "IMAPI_E_DIR_NOT_FOUND",
    "IMAPI_E_DISC_MISMATCH",
    "IMAPI_E_DUP_NAME",
    "IMAPI_E_EMPTY_DISC",
    "IMAPI_E_FILE_NOT_FOUND",
    "IMAPI_E_FILE_SYSTEM_CHANGE_NOT_ALLOWED",
    "IMAPI_E_FILE_SYSTEM_FEATURE_NOT_SUPPORTED",
    "IMAPI_E_FILE_SYSTEM_NOT_EMPTY",
    "IMAPI_E_FILE_SYSTEM_NOT_FOUND",
    "IMAPI_E_FILE_SYSTEM_READ_CONSISTENCY_ERROR",
    "IMAPI_E_FSI_INTERNAL_ERROR",
    "IMAPI_E_IMAGEMANAGER_IMAGE_NOT_ALIGNED",
    "IMAPI_E_IMAGEMANAGER_IMAGE_TOO_BIG",
    "IMAPI_E_IMAGEMANAGER_NO_IMAGE",
    "IMAPI_E_IMAGEMANAGER_NO_VALID_VD_FOUND",
    "IMAPI_E_IMAGE_SIZE_LIMIT",
    "IMAPI_E_IMAGE_TOO_BIG",
    "IMAPI_E_IMPORT_MEDIA_NOT_ALLOWED",
    "IMAPI_E_IMPORT_READ_FAILURE",
    "IMAPI_E_IMPORT_SEEK_FAILURE",
    "IMAPI_E_IMPORT_TYPE_COLLISION_DIRECTORY_EXISTS_AS_FILE",
    "IMAPI_E_IMPORT_TYPE_COLLISION_FILE_EXISTS_AS_DIRECTORY",
    "IMAPI_E_INCOMPATIBLE_MULTISESSION_TYPE",
    "IMAPI_E_INCOMPATIBLE_PREVIOUS_SESSION",
    "IMAPI_E_INVALID_DATE",
    "IMAPI_E_INVALID_PARAM",
    "IMAPI_E_INVALID_PATH",
    "IMAPI_E_INVALID_VOLUME_NAME",
    "IMAPI_E_INVALID_WORKING_DIRECTORY",
    "IMAPI_E_ISO9660_LEVELS",
    "IMAPI_E_ITEM_NOT_FOUND",
    "IMAPI_E_MULTISESSION_NOT_SET",
    "IMAPI_E_NOT_DIR",
    "IMAPI_E_NOT_FILE",
    "IMAPI_E_NOT_IN_FILE_SYSTEM",
    "IMAPI_E_NO_COMPATIBLE_MULTISESSION_TYPE",
    "IMAPI_E_NO_OUTPUT",
    "IMAPI_E_NO_SUPPORTED_FILE_SYSTEM",
    "IMAPI_E_NO_UNIQUE_NAME",
    "IMAPI_E_PROPERTY_NOT_ACCESSIBLE",
    "IMAPI_E_READONLY",
    "IMAPI_E_RESTRICTED_NAME_VIOLATION",
    "IMAPI_E_STASHFILE_MOVE",
    "IMAPI_E_STASHFILE_OPEN_FAILURE",
    "IMAPI_E_STASHFILE_READ_FAILURE",
    "IMAPI_E_STASHFILE_SEEK_FAILURE",
    "IMAPI_E_STASHFILE_WRITE_FAILURE",
    "IMAPI_E_TOO_MANY_DIRS",
    "IMAPI_E_UDF_NOT_WRITE_COMPATIBLE",
    "IMAPI_E_UDF_REVISION_CHANGE_NOT_ALLOWED",
    "IMAPI_E_WORKING_DIRECTORY_SPACE",
    "IMAPI_S_IMAGE_FEATURE_NOT_SUPPORTED",
    "IMailUser",
    "IMessage",
    "IMsgStore",
    "IProfSect",
    "IPropData",
    "IProviderAdmin",
    "ITableData",
    "IWABExtInit",
    "IWABObject",
    "LPALLOCATEBUFFER",
    "LPALLOCATEMORE",
    "LPCREATECONVERSATIONINDEX",
    "LPDISPATCHNOTIFICATIONS",
    "LPFNABSDI",
    "LPFNBUTTON",
    "LPFNDISMISS",
    "LPFREEBUFFER",
    "LPNOTIFCALLBACK",
    "LPOPENSTREAMONFILE",
    "LPWABALLOCATEBUFFER",
    "LPWABALLOCATEMORE",
    "LPWABFREEBUFFER",
    "LPWABOPEN",
    "LPWABOPENEX",
    "LPropCompareProp",
    "LpValFindProp",
    "MAPIDeinitIdle",
    "MAPIERROR",
    "MAPIGetDefaultMalloc",
    "MAPIInitIdle",
    "MAPINAMEID",
    "MAPIUID",
    "MAPI_COMPOUND",
    "MAPI_DIM",
    "MAPI_ERROR_VERSION",
    "MAPI_E_CALL_FAILED",
    "MAPI_E_INTERFACE_NOT_SUPPORTED",
    "MAPI_E_INVALID_PARAMETER",
    "MAPI_E_NOT_ENOUGH_MEMORY",
    "MAPI_E_NO_ACCESS",
    "MAPI_NOTRECIP",
    "MAPI_NOTRESERVED",
    "MAPI_NOW",
    "MAPI_ONE_OFF_NO_RICH_INFO",
    "MAPI_P1",
    "MAPI_SHORTTERM",
    "MAPI_SUBMITTED",
    "MAPI_THISSESSION",
    "MAPI_USE_DEFAULT",
    "MNID_ID",
    "MNID_STRING",
    "MTSID",
    "MV_FLAG",
    "MV_INSTANCE",
    "NEWMAIL_NOTIFICATION",
    "NOTIFICATION",
    "NOTIFKEY",
    "OBJECT_NOTIFICATION",
    "OPENSTREAMONFILE",
    "OpenStreamOnFile",
    "PFNIDLE",
    "PRIHIGHEST",
    "PRILOWEST",
    "PRIUSER",
    "PROP_ID_INVALID",
    "PROP_ID_NULL",
    "PROP_ID_SECURE_MAX",
    "PROP_ID_SECURE_MIN",
    "PpropFindProp",
    "PropCopyMore",
    "RTFSync",
    "SAndRestriction",
    "SAppTimeArray",
    "SBinary",
    "SBinaryArray",
    "SBitMaskRestriction",
    "SCommentRestriction",
    "SComparePropsRestriction",
    "SContentRestriction",
    "SCurrencyArray",
    "SDateTimeArray",
    "SDoubleArray",
    "SERVICE_UI_ALLOWED",
    "SERVICE_UI_ALWAYS",
    "SExistRestriction",
    "SGuidArray",
    "SLPSTRArray",
    "SLargeIntegerArray",
    "SLongArray",
    "SNotRestriction",
    "SOrRestriction",
    "SPropProblem",
    "SPropProblemArray",
    "SPropTagArray",
    "SPropValue",
    "SPropertyRestriction",
    "SRealArray",
    "SRestriction",
    "SRow",
    "SRowSet",
    "SShortArray",
    "SSizeRestriction",
    "SSortOrder",
    "SSortOrderSet",
    "SSubRestriction",
    "STATUS_OBJECT_NOTIFICATION",
    "SWStringArray",
    "S_IMAPI_BOTHADJUSTED",
    "S_IMAPI_COMMAND_HAS_SENSE_DATA",
    "S_IMAPI_RAW_IMAGE_TRACK_INDEX_ALREADY_EXISTS",
    "S_IMAPI_ROTATIONADJUSTED",
    "S_IMAPI_SPEEDADJUSTED",
    "S_IMAPI_WRITE_NOT_IN_PROGRESS",
    "ScCopyNotifications",
    "ScCopyProps",
    "ScCountNotifications",
    "ScCountProps",
    "ScCreateConversationIndex",
    "ScDupPropset",
    "ScInitMapiUtil",
    "ScLocalPathFromUNC",
    "ScRelocNotifications",
    "ScRelocProps",
    "ScUNCFromLocalPath",
    "SzFindCh",
    "SzFindLastCh",
    "SzFindSz",
    "TABLE_CHANGED",
    "TABLE_ERROR",
    "TABLE_NOTIFICATION",
    "TABLE_RELOAD",
    "TABLE_RESTRICT_DONE",
    "TABLE_ROW_ADDED",
    "TABLE_ROW_DELETED",
    "TABLE_ROW_MODIFIED",
    "TABLE_SETCOL_DONE",
    "TABLE_SORT_DONE",
    "TAD_ALL_ROWS",
    "UFromSz",
    "UI_CURRENT_PROVIDER_FIRST",
    "UI_SERVICE",
    "UlAddRef",
    "UlPropSize",
    "UlRelease",
    "WABEXTDISPLAY",
    "WABIMPORTPARAM",
    "WABOBJECT_LDAPURL_RETURN_MAILUSER",
    "WABOBJECT_ME_NEW",
    "WABOBJECT_ME_NOCREATE",
    "WAB_CONTEXT_ADRLIST",
    "WAB_DISPLAY_ISNTDS",
    "WAB_DISPLAY_LDAPURL",
    "WAB_DLL_NAME",
    "WAB_DLL_PATH_KEY",
    "WAB_ENABLE_PROFILES",
    "WAB_IGNORE_PROFILES",
    "WAB_LOCAL_CONTAINERS",
    "WAB_PARAM",
    "WAB_PROFILE_CONTENTS",
    "WAB_USE_OE_SENDMAIL",
    "WAB_VCARD_FILE",
    "WAB_VCARD_STREAM",
    "WrapCompressedRTFStream",
    "WrapStoreEntryID",
    "_WABACTIONITEM",
    "__UPV",
    "cchProfileNameMax",
    "cchProfilePassMax",
    "fMapiUnicode",
    "hrSuccess",
    "szHrDispatchNotifications",
    "szMAPINotificationMsg",
    "szScCreateConversationIndex",
]
