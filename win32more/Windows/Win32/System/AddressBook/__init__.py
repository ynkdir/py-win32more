from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.AddressBook
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.StructuredStorage
class ADRENTRY(Structure):
    ulReserved1: UInt32
    cValues: UInt32
    rgPropVals: POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue)
class ADRLIST(Structure):
    cEntries: UInt32
    aEntries: win32more.Windows.Win32.System.AddressBook.ADRENTRY * 1
class ADRPARM(Structure):
    cbABContEntryID: UInt32
    lpABContEntryID: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID)
    ulFlags: UInt32
    lpReserved: VoidPtr
    ulHelpContext: UInt32
    lpszHelpFileName: POINTER(SByte)
    lpfnABSDI: win32more.Windows.Win32.System.AddressBook.LPFNABSDI
    lpfnDismiss: win32more.Windows.Win32.System.AddressBook.LPFNDISMISS
    lpvDismissContext: VoidPtr
    lpszCaption: POINTER(SByte)
    lpszNewEntryTitle: POINTER(SByte)
    lpszDestWellsTitle: POINTER(SByte)
    cDestFields: UInt32
    nDestFieldFocus: UInt32
    lppszDestTitles: POINTER(POINTER(SByte))
    lpulDestComps: POINTER(UInt32)
    lpContRestriction: POINTER(win32more.Windows.Win32.System.AddressBook.SRestriction)
    lpHierRestriction: POINTER(win32more.Windows.Win32.System.AddressBook.SRestriction)
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
E_IMAPI_REQUEST_CANCELLED: win32more.Windows.Win32.Foundation.HRESULT = -1062600702
E_IMAPI_RECORDER_REQUIRED: win32more.Windows.Win32.Foundation.HRESULT = -1062600701
S_IMAPI_SPEEDADJUSTED: win32more.Windows.Win32.Foundation.HRESULT = 11141124
S_IMAPI_ROTATIONADJUSTED: win32more.Windows.Win32.Foundation.HRESULT = 11141125
S_IMAPI_BOTHADJUSTED: win32more.Windows.Win32.Foundation.HRESULT = 11141126
E_IMAPI_BURN_VERIFICATION_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -1062600697
S_IMAPI_COMMAND_HAS_SENSE_DATA: win32more.Windows.Win32.Foundation.HRESULT = 11141632
E_IMAPI_RECORDER_NO_SUCH_MODE_PAGE: win32more.Windows.Win32.Foundation.HRESULT = -1062600191
E_IMAPI_RECORDER_MEDIA_NO_MEDIA: win32more.Windows.Win32.Foundation.HRESULT = -1062600190
E_IMAPI_RECORDER_MEDIA_INCOMPATIBLE: win32more.Windows.Win32.Foundation.HRESULT = -1062600189
E_IMAPI_RECORDER_MEDIA_UPSIDE_DOWN: win32more.Windows.Win32.Foundation.HRESULT = -1062600188
E_IMAPI_RECORDER_MEDIA_BECOMING_READY: win32more.Windows.Win32.Foundation.HRESULT = -1062600187
E_IMAPI_RECORDER_MEDIA_FORMAT_IN_PROGRESS: win32more.Windows.Win32.Foundation.HRESULT = -1062600186
E_IMAPI_RECORDER_MEDIA_BUSY: win32more.Windows.Win32.Foundation.HRESULT = -1062600185
E_IMAPI_RECORDER_INVALID_MODE_PARAMETERS: win32more.Windows.Win32.Foundation.HRESULT = -1062600184
E_IMAPI_RECORDER_MEDIA_WRITE_PROTECTED: win32more.Windows.Win32.Foundation.HRESULT = -1062600183
E_IMAPI_RECORDER_NO_SUCH_FEATURE: win32more.Windows.Win32.Foundation.HRESULT = -1062600182
E_IMAPI_RECORDER_FEATURE_IS_NOT_CURRENT: win32more.Windows.Win32.Foundation.HRESULT = -1062600181
E_IMAPI_RECORDER_GET_CONFIGURATION_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -1062600180
E_IMAPI_RECORDER_COMMAND_TIMEOUT: win32more.Windows.Win32.Foundation.HRESULT = -1062600179
E_IMAPI_RECORDER_DVD_STRUCTURE_NOT_PRESENT: win32more.Windows.Win32.Foundation.HRESULT = -1062600178
E_IMAPI_RECORDER_MEDIA_SPEED_MISMATCH: win32more.Windows.Win32.Foundation.HRESULT = -1062600177
E_IMAPI_RECORDER_LOCKED: win32more.Windows.Win32.Foundation.HRESULT = -1062600176
E_IMAPI_RECORDER_CLIENT_NAME_IS_NOT_VALID: win32more.Windows.Win32.Foundation.HRESULT = -1062600175
E_IMAPI_RECORDER_MEDIA_NOT_FORMATTED: win32more.Windows.Win32.Foundation.HRESULT = -1062600174
E_IMAPI_RECORDER_INVALID_RESPONSE_FROM_DEVICE: win32more.Windows.Win32.Foundation.HRESULT = -1062599937
E_IMAPI_LOSS_OF_STREAMING: win32more.Windows.Win32.Foundation.HRESULT = -1062599936
E_IMAPI_UNEXPECTED_RESPONSE_FROM_DEVICE: win32more.Windows.Win32.Foundation.HRESULT = -1062599935
S_IMAPI_WRITE_NOT_IN_PROGRESS: win32more.Windows.Win32.Foundation.HRESULT = 11141890
E_IMAPI_DF2DATA_WRITE_IN_PROGRESS: win32more.Windows.Win32.Foundation.HRESULT = -1062599680
E_IMAPI_DF2DATA_WRITE_NOT_IN_PROGRESS: win32more.Windows.Win32.Foundation.HRESULT = -1062599679
E_IMAPI_DF2DATA_INVALID_MEDIA_STATE: win32more.Windows.Win32.Foundation.HRESULT = -1062599678
E_IMAPI_DF2DATA_STREAM_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -1062599677
E_IMAPI_DF2DATA_STREAM_TOO_LARGE_FOR_CURRENT_MEDIA: win32more.Windows.Win32.Foundation.HRESULT = -1062599676
E_IMAPI_DF2DATA_MEDIA_NOT_BLANK: win32more.Windows.Win32.Foundation.HRESULT = -1062599675
E_IMAPI_DF2DATA_MEDIA_IS_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -1062599674
E_IMAPI_DF2DATA_RECORDER_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -1062599673
E_IMAPI_DF2DATA_CLIENT_NAME_IS_NOT_VALID: win32more.Windows.Win32.Foundation.HRESULT = -1062599672
E_IMAPI_DF2TAO_WRITE_IN_PROGRESS: win32more.Windows.Win32.Foundation.HRESULT = -1062599424
E_IMAPI_DF2TAO_WRITE_NOT_IN_PROGRESS: win32more.Windows.Win32.Foundation.HRESULT = -1062599423
E_IMAPI_DF2TAO_MEDIA_IS_NOT_PREPARED: win32more.Windows.Win32.Foundation.HRESULT = -1062599422
E_IMAPI_DF2TAO_MEDIA_IS_PREPARED: win32more.Windows.Win32.Foundation.HRESULT = -1062599421
E_IMAPI_DF2TAO_PROPERTY_FOR_BLANK_MEDIA_ONLY: win32more.Windows.Win32.Foundation.HRESULT = -1062599420
E_IMAPI_DF2TAO_TABLE_OF_CONTENTS_EMPTY_DISC: win32more.Windows.Win32.Foundation.HRESULT = -1062599419
E_IMAPI_DF2TAO_MEDIA_IS_NOT_BLANK: win32more.Windows.Win32.Foundation.HRESULT = -1062599418
E_IMAPI_DF2TAO_MEDIA_IS_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -1062599417
E_IMAPI_DF2TAO_TRACK_LIMIT_REACHED: win32more.Windows.Win32.Foundation.HRESULT = -1062599416
E_IMAPI_DF2TAO_NOT_ENOUGH_SPACE: win32more.Windows.Win32.Foundation.HRESULT = -1062599415
E_IMAPI_DF2TAO_NO_RECORDER_SPECIFIED: win32more.Windows.Win32.Foundation.HRESULT = -1062599414
E_IMAPI_DF2TAO_INVALID_ISRC: win32more.Windows.Win32.Foundation.HRESULT = -1062599413
E_IMAPI_DF2TAO_INVALID_MCN: win32more.Windows.Win32.Foundation.HRESULT = -1062599412
E_IMAPI_DF2TAO_STREAM_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -1062599411
E_IMAPI_DF2TAO_RECORDER_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -1062599410
E_IMAPI_DF2TAO_CLIENT_NAME_IS_NOT_VALID: win32more.Windows.Win32.Foundation.HRESULT = -1062599409
E_IMAPI_DF2RAW_WRITE_IN_PROGRESS: win32more.Windows.Win32.Foundation.HRESULT = -1062599168
E_IMAPI_DF2RAW_WRITE_NOT_IN_PROGRESS: win32more.Windows.Win32.Foundation.HRESULT = -1062599167
E_IMAPI_DF2RAW_MEDIA_IS_NOT_PREPARED: win32more.Windows.Win32.Foundation.HRESULT = -1062599166
E_IMAPI_DF2RAW_MEDIA_IS_PREPARED: win32more.Windows.Win32.Foundation.HRESULT = -1062599165
E_IMAPI_DF2RAW_CLIENT_NAME_IS_NOT_VALID: win32more.Windows.Win32.Foundation.HRESULT = -1062599164
E_IMAPI_DF2RAW_MEDIA_IS_NOT_BLANK: win32more.Windows.Win32.Foundation.HRESULT = -1062599162
E_IMAPI_DF2RAW_MEDIA_IS_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -1062599161
E_IMAPI_DF2RAW_NOT_ENOUGH_SPACE: win32more.Windows.Win32.Foundation.HRESULT = -1062599159
E_IMAPI_DF2RAW_NO_RECORDER_SPECIFIED: win32more.Windows.Win32.Foundation.HRESULT = -1062599158
E_IMAPI_DF2RAW_STREAM_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -1062599155
E_IMAPI_DF2RAW_DATA_BLOCK_TYPE_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -1062599154
E_IMAPI_DF2RAW_STREAM_LEADIN_TOO_SHORT: win32more.Windows.Win32.Foundation.HRESULT = -1062599153
E_IMAPI_DF2RAW_RECORDER_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -1062599152
E_IMAPI_ERASE_RECORDER_IN_USE: win32more.Windows.Win32.Foundation.HRESULT = -2136340224
E_IMAPI_ERASE_ONLY_ONE_RECORDER_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2136340223
E_IMAPI_ERASE_DISC_INFORMATION_TOO_SMALL: win32more.Windows.Win32.Foundation.HRESULT = -2136340222
E_IMAPI_ERASE_MODE_PAGE_2A_TOO_SMALL: win32more.Windows.Win32.Foundation.HRESULT = -2136340221
E_IMAPI_ERASE_MEDIA_IS_NOT_ERASABLE: win32more.Windows.Win32.Foundation.HRESULT = -2136340220
E_IMAPI_ERASE_DRIVE_FAILED_ERASE_COMMAND: win32more.Windows.Win32.Foundation.HRESULT = -2136340219
E_IMAPI_ERASE_TOOK_LONGER_THAN_ONE_HOUR: win32more.Windows.Win32.Foundation.HRESULT = -2136340218
E_IMAPI_ERASE_UNEXPECTED_DRIVE_RESPONSE_DURING_ERASE: win32more.Windows.Win32.Foundation.HRESULT = -2136340217
E_IMAPI_ERASE_DRIVE_FAILED_SPINUP_COMMAND: win32more.Windows.Win32.Foundation.HRESULT = -2136340216
E_IMAPI_ERASE_MEDIA_IS_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -1062598391
E_IMAPI_ERASE_RECORDER_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -1062598390
E_IMAPI_ERASE_CLIENT_NAME_IS_NOT_VALID: win32more.Windows.Win32.Foundation.HRESULT = -1062598389
E_IMAPI_RAW_IMAGE_IS_READ_ONLY: win32more.Windows.Win32.Foundation.HRESULT = -2136339968
E_IMAPI_RAW_IMAGE_TOO_MANY_TRACKS: win32more.Windows.Win32.Foundation.HRESULT = -2136339967
E_IMAPI_RAW_IMAGE_SECTOR_TYPE_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2136339966
E_IMAPI_RAW_IMAGE_NO_TRACKS: win32more.Windows.Win32.Foundation.HRESULT = -2136339965
E_IMAPI_RAW_IMAGE_TRACKS_ALREADY_ADDED: win32more.Windows.Win32.Foundation.HRESULT = -2136339964
E_IMAPI_RAW_IMAGE_INSUFFICIENT_SPACE: win32more.Windows.Win32.Foundation.HRESULT = -2136339963
E_IMAPI_RAW_IMAGE_TOO_MANY_TRACK_INDEXES: win32more.Windows.Win32.Foundation.HRESULT = -2136339962
E_IMAPI_RAW_IMAGE_TRACK_INDEX_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2136339961
S_IMAPI_RAW_IMAGE_TRACK_INDEX_ALREADY_EXISTS: win32more.Windows.Win32.Foundation.HRESULT = 11143688
E_IMAPI_RAW_IMAGE_TRACK_INDEX_OFFSET_ZERO_CANNOT_BE_CLEARED: win32more.Windows.Win32.Foundation.HRESULT = -2136339959
E_IMAPI_RAW_IMAGE_TRACK_INDEX_TOO_CLOSE_TO_OTHER_INDEX: win32more.Windows.Win32.Foundation.HRESULT = -2136339958
FACILITY_IMAPI2: UInt32 = 170
IMAPI_E_FSI_INTERNAL_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -1062555392
IMAPI_E_INVALID_PARAM: win32more.Windows.Win32.Foundation.HRESULT = -1062555391
IMAPI_E_READONLY: win32more.Windows.Win32.Foundation.HRESULT = -1062555390
IMAPI_E_NO_OUTPUT: win32more.Windows.Win32.Foundation.HRESULT = -1062555389
IMAPI_E_INVALID_VOLUME_NAME: win32more.Windows.Win32.Foundation.HRESULT = -1062555388
IMAPI_E_INVALID_DATE: win32more.Windows.Win32.Foundation.HRESULT = -1062555387
IMAPI_E_FILE_SYSTEM_NOT_EMPTY: win32more.Windows.Win32.Foundation.HRESULT = -1062555386
IMAPI_E_NOT_FILE: win32more.Windows.Win32.Foundation.HRESULT = -1062555384
IMAPI_E_NOT_DIR: win32more.Windows.Win32.Foundation.HRESULT = -1062555383
IMAPI_E_DIR_NOT_EMPTY: win32more.Windows.Win32.Foundation.HRESULT = -1062555382
IMAPI_E_NOT_IN_FILE_SYSTEM: win32more.Windows.Win32.Foundation.HRESULT = -1062555381
IMAPI_E_INVALID_PATH: win32more.Windows.Win32.Foundation.HRESULT = -1062555376
IMAPI_E_RESTRICTED_NAME_VIOLATION: win32more.Windows.Win32.Foundation.HRESULT = -1062555375
IMAPI_E_DUP_NAME: win32more.Windows.Win32.Foundation.HRESULT = -1062555374
IMAPI_E_NO_UNIQUE_NAME: win32more.Windows.Win32.Foundation.HRESULT = -1062555373
IMAPI_E_ITEM_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -1062555368
IMAPI_E_FILE_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -1062555367
IMAPI_E_DIR_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -1062555366
IMAPI_E_IMAGE_SIZE_LIMIT: win32more.Windows.Win32.Foundation.HRESULT = -1062555360
IMAPI_E_IMAGE_TOO_BIG: win32more.Windows.Win32.Foundation.HRESULT = -1062555359
IMAPI_E_DATA_STREAM_INCONSISTENCY: win32more.Windows.Win32.Foundation.HRESULT = -1062555352
IMAPI_E_DATA_STREAM_READ_FAILURE: win32more.Windows.Win32.Foundation.HRESULT = -1062555351
IMAPI_E_DATA_STREAM_CREATE_FAILURE: win32more.Windows.Win32.Foundation.HRESULT = -1062555350
IMAPI_E_DIRECTORY_READ_FAILURE: win32more.Windows.Win32.Foundation.HRESULT = -1062555349
IMAPI_E_TOO_MANY_DIRS: win32more.Windows.Win32.Foundation.HRESULT = -1062555344
IMAPI_E_ISO9660_LEVELS: win32more.Windows.Win32.Foundation.HRESULT = -1062555343
IMAPI_E_DATA_TOO_BIG: win32more.Windows.Win32.Foundation.HRESULT = -1062555342
IMAPI_E_INCOMPATIBLE_PREVIOUS_SESSION: win32more.Windows.Win32.Foundation.HRESULT = -1062555341
IMAPI_E_STASHFILE_OPEN_FAILURE: win32more.Windows.Win32.Foundation.HRESULT = -1062555336
IMAPI_E_STASHFILE_SEEK_FAILURE: win32more.Windows.Win32.Foundation.HRESULT = -1062555335
IMAPI_E_STASHFILE_WRITE_FAILURE: win32more.Windows.Win32.Foundation.HRESULT = -1062555334
IMAPI_E_STASHFILE_READ_FAILURE: win32more.Windows.Win32.Foundation.HRESULT = -1062555333
IMAPI_E_INVALID_WORKING_DIRECTORY: win32more.Windows.Win32.Foundation.HRESULT = -1062555328
IMAPI_E_WORKING_DIRECTORY_SPACE: win32more.Windows.Win32.Foundation.HRESULT = -1062555327
IMAPI_E_STASHFILE_MOVE: win32more.Windows.Win32.Foundation.HRESULT = -1062555326
IMAPI_E_BOOT_IMAGE_DATA: win32more.Windows.Win32.Foundation.HRESULT = -1062555320
IMAPI_E_BOOT_OBJECT_CONFLICT: win32more.Windows.Win32.Foundation.HRESULT = -1062555319
IMAPI_E_BOOT_EMULATION_IMAGE_SIZE_MISMATCH: win32more.Windows.Win32.Foundation.HRESULT = -1062555318
IMAPI_E_EMPTY_DISC: win32more.Windows.Win32.Foundation.HRESULT = -1062555312
IMAPI_E_NO_SUPPORTED_FILE_SYSTEM: win32more.Windows.Win32.Foundation.HRESULT = -1062555311
IMAPI_E_FILE_SYSTEM_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -1062555310
IMAPI_E_FILE_SYSTEM_READ_CONSISTENCY_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -1062555309
IMAPI_E_FILE_SYSTEM_FEATURE_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -1062555308
IMAPI_E_IMPORT_TYPE_COLLISION_FILE_EXISTS_AS_DIRECTORY: win32more.Windows.Win32.Foundation.HRESULT = -1062555307
IMAPI_E_IMPORT_SEEK_FAILURE: win32more.Windows.Win32.Foundation.HRESULT = -1062555306
IMAPI_E_IMPORT_READ_FAILURE: win32more.Windows.Win32.Foundation.HRESULT = -1062555305
IMAPI_E_DISC_MISMATCH: win32more.Windows.Win32.Foundation.HRESULT = -1062555304
IMAPI_E_IMPORT_MEDIA_NOT_ALLOWED: win32more.Windows.Win32.Foundation.HRESULT = -1062555303
IMAPI_E_UDF_NOT_WRITE_COMPATIBLE: win32more.Windows.Win32.Foundation.HRESULT = -1062555302
IMAPI_E_INCOMPATIBLE_MULTISESSION_TYPE: win32more.Windows.Win32.Foundation.HRESULT = -1062555301
IMAPI_E_NO_COMPATIBLE_MULTISESSION_TYPE: win32more.Windows.Win32.Foundation.HRESULT = -1062555300
IMAPI_E_MULTISESSION_NOT_SET: win32more.Windows.Win32.Foundation.HRESULT = -1062555299
IMAPI_E_IMPORT_TYPE_COLLISION_DIRECTORY_EXISTS_AS_FILE: win32more.Windows.Win32.Foundation.HRESULT = -1062555298
IMAPI_S_IMAGE_FEATURE_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = 11186527
IMAPI_E_PROPERTY_NOT_ACCESSIBLE: win32more.Windows.Win32.Foundation.HRESULT = -1062555296
IMAPI_E_UDF_REVISION_CHANGE_NOT_ALLOWED: win32more.Windows.Win32.Foundation.HRESULT = -1062555295
IMAPI_E_BAD_MULTISESSION_PARAMETER: win32more.Windows.Win32.Foundation.HRESULT = -1062555294
IMAPI_E_FILE_SYSTEM_CHANGE_NOT_ALLOWED: win32more.Windows.Win32.Foundation.HRESULT = -1062555293
IMAPI_E_IMAGEMANAGER_IMAGE_NOT_ALIGNED: win32more.Windows.Win32.Foundation.HRESULT = -1062555136
IMAPI_E_IMAGEMANAGER_NO_VALID_VD_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -1062555135
IMAPI_E_IMAGEMANAGER_NO_IMAGE: win32more.Windows.Win32.Foundation.HRESULT = -1062555134
IMAPI_E_IMAGEMANAGER_IMAGE_TOO_BIG: win32more.Windows.Win32.Foundation.HRESULT = -1062555133
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
def CreateTable(lpInterface: POINTER(Guid), lpAllocateBuffer: win32more.Windows.Win32.System.AddressBook.LPALLOCATEBUFFER, lpAllocateMore: win32more.Windows.Win32.System.AddressBook.LPALLOCATEMORE, lpFreeBuffer: win32more.Windows.Win32.System.AddressBook.LPFREEBUFFER, lpvReserved: VoidPtr, ulTableType: UInt32, ulPropTagIndexColumn: UInt32, lpSPropTagArrayColumns: POINTER(win32more.Windows.Win32.System.AddressBook.SPropTagArray), lppTableData: POINTER(win32more.Windows.Win32.System.AddressBook.ITableData)) -> Int32: ...
@winfunctype('MAPI32.dll')
def CreateIProp(lpInterface: POINTER(Guid), lpAllocateBuffer: win32more.Windows.Win32.System.AddressBook.LPALLOCATEBUFFER, lpAllocateMore: win32more.Windows.Win32.System.AddressBook.LPALLOCATEMORE, lpFreeBuffer: win32more.Windows.Win32.System.AddressBook.LPFREEBUFFER, lpvReserved: VoidPtr, lppPropData: POINTER(win32more.Windows.Win32.System.AddressBook.IPropData)) -> Int32: ...
@winfunctype('MAPI32.dll')
def MAPIInitIdle(lpvReserved: VoidPtr) -> Int32: ...
@winfunctype('MAPI32.dll')
def MAPIDeinitIdle() -> Void: ...
@winfunctype('MAPI32.dll')
def FtgRegisterIdleRoutine(lpfnIdle: win32more.Windows.Win32.System.AddressBook.PFNIDLE, lpvIdleParam: VoidPtr, priIdle: Int16, csecIdle: UInt32, iroIdle: UInt16) -> VoidPtr: ...
@winfunctype('MAPI32.dll')
def DeregisterIdleRoutine(ftg: VoidPtr) -> Void: ...
@winfunctype('MAPI32.dll')
def EnableIdleRoutine(ftg: VoidPtr, fEnable: win32more.Windows.Win32.Foundation.BOOL) -> Void: ...
@winfunctype('MAPI32.dll')
def ChangeIdleRoutine(ftg: VoidPtr, lpfnIdle: win32more.Windows.Win32.System.AddressBook.PFNIDLE, lpvIdleParam: VoidPtr, priIdle: Int16, csecIdle: UInt32, iroIdle: UInt16, ircIdle: UInt16) -> Void: ...
@winfunctype('MAPI32.dll')
def MAPIGetDefaultMalloc() -> win32more.Windows.Win32.System.Com.IMalloc: ...
@winfunctype('MAPI32.dll')
def OpenStreamOnFile(lpAllocateBuffer: win32more.Windows.Win32.System.AddressBook.LPALLOCATEBUFFER, lpFreeBuffer: win32more.Windows.Win32.System.AddressBook.LPFREEBUFFER, ulFlags: UInt32, lpszFileName: POINTER(SByte), lpszPrefix: POINTER(SByte), lppStream: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def PropCopyMore(lpSPropValueDest: POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue), lpSPropValueSrc: POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue), lpfAllocMore: win32more.Windows.Win32.System.AddressBook.LPALLOCATEMORE, lpvObject: VoidPtr) -> Int32: ...
@winfunctype('MAPI32.dll')
def UlPropSize(lpSPropValue: POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue)) -> UInt32: ...
@winfunctype('MAPI32.dll')
def FEqualNames(lpName1: POINTER(win32more.Windows.Win32.System.AddressBook.MAPINAMEID), lpName2: POINTER(win32more.Windows.Win32.System.AddressBook.MAPINAMEID)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAPI32.dll')
def FPropContainsProp(lpSPropValueDst: POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue), lpSPropValueSrc: POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue), ulFuzzyLevel: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAPI32.dll')
def FPropCompareProp(lpSPropValue1: POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue), ulRelOp: UInt32, lpSPropValue2: POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAPI32.dll')
def LPropCompareProp(lpSPropValueA: POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue), lpSPropValueB: POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue)) -> Int32: ...
@winfunctype('MAPI32.dll')
def HrAddColumns(lptbl: win32more.Windows.Win32.System.AddressBook.IMAPITable, lpproptagColumnsNew: POINTER(win32more.Windows.Win32.System.AddressBook.SPropTagArray), lpAllocateBuffer: win32more.Windows.Win32.System.AddressBook.LPALLOCATEBUFFER, lpFreeBuffer: win32more.Windows.Win32.System.AddressBook.LPFREEBUFFER) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def HrAddColumnsEx(lptbl: win32more.Windows.Win32.System.AddressBook.IMAPITable, lpproptagColumnsNew: POINTER(win32more.Windows.Win32.System.AddressBook.SPropTagArray), lpAllocateBuffer: win32more.Windows.Win32.System.AddressBook.LPALLOCATEBUFFER, lpFreeBuffer: win32more.Windows.Win32.System.AddressBook.LPFREEBUFFER, lpfnFilterColumns: IntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def HrAllocAdviseSink(lpfnCallback: win32more.Windows.Win32.System.AddressBook.LPNOTIFCALLBACK, lpvContext: VoidPtr, lppAdviseSink: POINTER(win32more.Windows.Win32.System.AddressBook.IMAPIAdviseSink)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def HrThisThreadAdviseSink(lpAdviseSink: win32more.Windows.Win32.System.AddressBook.IMAPIAdviseSink, lppAdviseSink: POINTER(win32more.Windows.Win32.System.AddressBook.IMAPIAdviseSink)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def HrDispatchNotifications(ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def BuildDisplayTable(lpAllocateBuffer: win32more.Windows.Win32.System.AddressBook.LPALLOCATEBUFFER, lpAllocateMore: win32more.Windows.Win32.System.AddressBook.LPALLOCATEMORE, lpFreeBuffer: win32more.Windows.Win32.System.AddressBook.LPFREEBUFFER, lpMalloc: win32more.Windows.Win32.System.Com.IMalloc, hInstance: win32more.Windows.Win32.Foundation.HINSTANCE, cPages: UInt32, lpPage: POINTER(win32more.Windows.Win32.System.AddressBook.DTPAGE), ulFlags: UInt32, lppTable: POINTER(win32more.Windows.Win32.System.AddressBook.IMAPITable), lppTblData: POINTER(win32more.Windows.Win32.System.AddressBook.ITableData)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def ScCountNotifications(cNotifications: Int32, lpNotifications: POINTER(win32more.Windows.Win32.System.AddressBook.NOTIFICATION), lpcb: POINTER(UInt32)) -> Int32: ...
@winfunctype('MAPI32.dll')
def ScCopyNotifications(cNotification: Int32, lpNotifications: POINTER(win32more.Windows.Win32.System.AddressBook.NOTIFICATION), lpvDst: VoidPtr, lpcb: POINTER(UInt32)) -> Int32: ...
@winfunctype('MAPI32.dll')
def ScRelocNotifications(cNotification: Int32, lpNotifications: POINTER(win32more.Windows.Win32.System.AddressBook.NOTIFICATION), lpvBaseOld: VoidPtr, lpvBaseNew: VoidPtr, lpcb: POINTER(UInt32)) -> Int32: ...
@winfunctype('MAPI32.dll')
def ScCountProps(cValues: Int32, lpPropArray: POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue), lpcb: POINTER(UInt32)) -> Int32: ...
@winfunctype('MAPI32.dll')
def LpValFindProp(ulPropTag: UInt32, cValues: UInt32, lpPropArray: POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue)) -> POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue): ...
@winfunctype('MAPI32.dll')
def ScCopyProps(cValues: Int32, lpPropArray: POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue), lpvDst: VoidPtr, lpcb: POINTER(UInt32)) -> Int32: ...
@winfunctype('MAPI32.dll')
def ScRelocProps(cValues: Int32, lpPropArray: POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue), lpvBaseOld: VoidPtr, lpvBaseNew: VoidPtr, lpcb: POINTER(UInt32)) -> Int32: ...
@winfunctype('MAPI32.dll')
def ScDupPropset(cValues: Int32, lpPropArray: POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue), lpAllocateBuffer: win32more.Windows.Win32.System.AddressBook.LPALLOCATEBUFFER, lppPropArray: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue))) -> Int32: ...
@winfunctype('MAPI32.dll')
def UlAddRef(lpunk: VoidPtr) -> UInt32: ...
@winfunctype('MAPI32.dll')
def UlRelease(lpunk: VoidPtr) -> UInt32: ...
@winfunctype('MAPI32.dll')
def HrGetOneProp(lpMapiProp: win32more.Windows.Win32.System.AddressBook.IMAPIProp, ulPropTag: UInt32, lppProp: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def HrSetOneProp(lpMapiProp: win32more.Windows.Win32.System.AddressBook.IMAPIProp, lpProp: POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def FPropExists(lpMapiProp: win32more.Windows.Win32.System.AddressBook.IMAPIProp, ulPropTag: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('MAPI32.dll')
def PpropFindProp(lpPropArray: POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue), cValues: UInt32, ulPropTag: UInt32) -> POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue): ...
@winfunctype('MAPI32.dll')
def FreePadrlist(lpAdrlist: POINTER(win32more.Windows.Win32.System.AddressBook.ADRLIST)) -> Void: ...
@winfunctype('MAPI32.dll')
def FreeProws(lpRows: POINTER(win32more.Windows.Win32.System.AddressBook.SRowSet)) -> Void: ...
@winfunctype('MAPI32.dll')
def HrQueryAllRows(lpTable: win32more.Windows.Win32.System.AddressBook.IMAPITable, lpPropTags: POINTER(win32more.Windows.Win32.System.AddressBook.SPropTagArray), lpRestriction: POINTER(win32more.Windows.Win32.System.AddressBook.SRestriction), lpSortOrderSet: POINTER(win32more.Windows.Win32.System.AddressBook.SSortOrderSet), crowsMax: Int32, lppRows: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.SRowSet))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def SzFindCh(lpsz: POINTER(SByte), ch: UInt16) -> POINTER(SByte): ...
@winfunctype('MAPI32.dll')
def SzFindLastCh(lpsz: POINTER(SByte), ch: UInt16) -> POINTER(SByte): ...
@winfunctype('MAPI32.dll')
def SzFindSz(lpsz: POINTER(SByte), lpszKey: POINTER(SByte)) -> POINTER(SByte): ...
@winfunctype('MAPI32.dll')
def UFromSz(lpsz: POINTER(SByte)) -> UInt32: ...
@winfunctype('MAPI32.dll')
def ScUNCFromLocalPath(lpszLocal: win32more.Windows.Win32.Foundation.PSTR, lpszUNC: win32more.Windows.Win32.Foundation.PSTR, cchUNC: UInt32) -> Int32: ...
@winfunctype('MAPI32.dll')
def ScLocalPathFromUNC(lpszUNC: win32more.Windows.Win32.Foundation.PSTR, lpszLocal: win32more.Windows.Win32.Foundation.PSTR, cchLocal: UInt32) -> Int32: ...
@winfunctype('MAPI32.dll')
def FtAddFt(ftAddend1: win32more.Windows.Win32.Foundation.FILETIME, ftAddend2: win32more.Windows.Win32.Foundation.FILETIME) -> win32more.Windows.Win32.Foundation.FILETIME: ...
@winfunctype('MAPI32.dll')
def FtMulDwDw(ftMultiplicand: UInt32, ftMultiplier: UInt32) -> win32more.Windows.Win32.Foundation.FILETIME: ...
@winfunctype('MAPI32.dll')
def FtMulDw(ftMultiplier: UInt32, ftMultiplicand: win32more.Windows.Win32.Foundation.FILETIME) -> win32more.Windows.Win32.Foundation.FILETIME: ...
@winfunctype('MAPI32.dll')
def FtSubFt(ftMinuend: win32more.Windows.Win32.Foundation.FILETIME, ftSubtrahend: win32more.Windows.Win32.Foundation.FILETIME) -> win32more.Windows.Win32.Foundation.FILETIME: ...
@winfunctype('MAPI32.dll')
def FtNegFt(ft: win32more.Windows.Win32.Foundation.FILETIME) -> win32more.Windows.Win32.Foundation.FILETIME: ...
@winfunctype('MAPI32.dll')
def ScCreateConversationIndex(cbParent: UInt32, lpbParent: POINTER(Byte), lpcbConvIndex: POINTER(UInt32), lppbConvIndex: POINTER(POINTER(Byte))) -> Int32: ...
@winfunctype('MAPI32.dll')
def WrapStoreEntryID(ulFlags: UInt32, lpszDLLName: POINTER(SByte), cbOrigEntry: UInt32, lpOrigEntry: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID), lpcbWrappedEntry: POINTER(UInt32), lppWrappedEntry: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def RTFSync(lpMessage: win32more.Windows.Win32.System.AddressBook.IMessage, ulFlags: UInt32, lpfMessageUpdated: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def WrapCompressedRTFStream(lpCompressedRTFStream: win32more.Windows.Win32.System.Com.IStream, ulFlags: UInt32, lpUncompressedRTFStream: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def HrIStorageFromStream(lpUnkIn: win32more.Windows.Win32.System.Com.IUnknown, lpInterface: POINTER(Guid), ulFlags: UInt32, lppStorageOut: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MAPI32.dll')
def ScInitMapiUtil(ulFlags: UInt32) -> Int32: ...
@winfunctype('MAPI32.dll')
def DeinitMapiUtil() -> Void: ...
@winfunctype_pointer
def CALLERRELEASE(ulCallerData: UInt32, lpTblData: win32more.Windows.Win32.System.AddressBook.ITableData, lpVue: win32more.Windows.Win32.System.AddressBook.IMAPITable) -> Void: ...
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
    lpbNotif: POINTER(Byte)
    cbNotif: UInt32
    lpszFilter: POINTER(SByte)
    ulItemID: UInt32
    ctl: _ctl_e__Union
    class _ctl_e__Union(Union):
        lpv: VoidPtr
        lplabel: POINTER(win32more.Windows.Win32.System.AddressBook.DTBLLABEL)
        lpedit: POINTER(win32more.Windows.Win32.System.AddressBook.DTBLEDIT)
        lplbx: POINTER(win32more.Windows.Win32.System.AddressBook.DTBLLBX)
        lpcombobox: POINTER(win32more.Windows.Win32.System.AddressBook.DTBLCOMBOBOX)
        lpddlbx: POINTER(win32more.Windows.Win32.System.AddressBook.DTBLDDLBX)
        lpcheckbox: POINTER(win32more.Windows.Win32.System.AddressBook.DTBLCHECKBOX)
        lpgroupbox: POINTER(win32more.Windows.Win32.System.AddressBook.DTBLGROUPBOX)
        lpbutton: POINTER(win32more.Windows.Win32.System.AddressBook.DTBLBUTTON)
        lpradiobutton: POINTER(win32more.Windows.Win32.System.AddressBook.DTBLRADIOBUTTON)
        lpmvlbx: POINTER(win32more.Windows.Win32.System.AddressBook.DTBLMVLISTBOX)
        lpmvddlbx: POINTER(win32more.Windows.Win32.System.AddressBook.DTBLMVDDLBX)
        lppage: POINTER(win32more.Windows.Win32.System.AddressBook.DTBLPAGE)
class DTPAGE(Structure):
    cctl: UInt32
    lpszResourceName: POINTER(SByte)
    Anonymous: _Anonymous_e__Union
    lpctl: POINTER(win32more.Windows.Win32.System.AddressBook.DTCTL)
    class _Anonymous_e__Union(Union):
        lpszComponent: POINTER(SByte)
        ulItemID: UInt32
class ENTRYID(Structure):
    abFlags: Byte * 4
    ab: Byte * 1
class ERROR_NOTIFICATION(Structure):
    cbEntryID: UInt32
    lpEntryID: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID)
    scode: Int32
    ulFlags: UInt32
    lpMAPIError: POINTER(win32more.Windows.Win32.System.AddressBook.MAPIERROR)
class EXTENDED_NOTIFICATION(Structure):
    ulEvent: UInt32
    cb: UInt32
    pbEventParameters: POINTER(Byte)
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
class FlagList(Structure):
    cFlags: UInt32
    ulFlag: UInt32 * 1
Gender = Int32
genderUnspecified: win32more.Windows.Win32.System.AddressBook.Gender = 0
genderFemale: win32more.Windows.Win32.System.AddressBook.Gender = 1
genderMale: win32more.Windows.Win32.System.AddressBook.Gender = 2
class IABContainer(ComPtr):
    extends: win32more.Windows.Win32.System.AddressBook.IMAPIContainer
    @commethod(19)
    def CreateEntry(self, cbEntryID: UInt32, lpEntryID: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID), ulCreateFlags: UInt32, lppMAPIPropEntry: POINTER(win32more.Windows.Win32.System.AddressBook.IMAPIProp)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def CopyEntries(self, lpEntries: POINTER(win32more.Windows.Win32.System.AddressBook.SBinaryArray), ulUIParam: UIntPtr, lpProgress: win32more.Windows.Win32.System.AddressBook.IMAPIProgress, ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def DeleteEntries(self, lpEntries: POINTER(win32more.Windows.Win32.System.AddressBook.SBinaryArray), ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def ResolveNames(self, lpPropTagArray: POINTER(win32more.Windows.Win32.System.AddressBook.SPropTagArray), ulFlags: UInt32, lpAdrList: POINTER(win32more.Windows.Win32.System.AddressBook.ADRLIST), lpFlagList: POINTER(win32more.Windows.Win32.System.AddressBook.FlagList)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAddrBook(ComPtr):
    extends: win32more.Windows.Win32.System.AddressBook.IMAPIProp
    @commethod(14)
    def OpenEntry(self, cbEntryID: UInt32, lpEntryID: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID), lpInterface: POINTER(Guid), ulFlags: UInt32, lpulObjType: POINTER(UInt32), lppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CompareEntryIDs(self, cbEntryID1: UInt32, lpEntryID1: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID), cbEntryID2: UInt32, lpEntryID2: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID), ulFlags: UInt32, lpulResult: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Advise(self, cbEntryID: UInt32, lpEntryID: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID), ulEventMask: UInt32, lpAdviseSink: win32more.Windows.Win32.System.AddressBook.IMAPIAdviseSink, lpulConnection: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Unadvise(self, ulConnection: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def CreateOneOff(self, lpszName: POINTER(SByte), lpszAdrType: POINTER(SByte), lpszAddress: POINTER(SByte), ulFlags: UInt32, lpcbEntryID: POINTER(UInt32), lppEntryID: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def NewEntry(self, ulUIParam: UInt32, ulFlags: UInt32, cbEIDContainer: UInt32, lpEIDContainer: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID), cbEIDNewEntryTpl: UInt32, lpEIDNewEntryTpl: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID), lpcbEIDNewEntry: POINTER(UInt32), lppEIDNewEntry: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def ResolveName(self, ulUIParam: UIntPtr, ulFlags: UInt32, lpszNewEntryTitle: POINTER(SByte), lpAdrList: POINTER(win32more.Windows.Win32.System.AddressBook.ADRLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Address(self, lpulUIParam: POINTER(UInt32), lpAdrParms: POINTER(win32more.Windows.Win32.System.AddressBook.ADRPARM), lppAdrList: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.ADRLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Details(self, lpulUIParam: POINTER(UIntPtr), lpfnDismiss: win32more.Windows.Win32.System.AddressBook.LPFNDISMISS, lpvDismissContext: VoidPtr, cbEntryID: UInt32, lpEntryID: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID), lpfButtonCallback: win32more.Windows.Win32.System.AddressBook.LPFNBUTTON, lpvButtonContext: VoidPtr, lpszButtonText: POINTER(SByte), ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def RecipOptions(self, ulUIParam: UInt32, ulFlags: UInt32, lpRecip: POINTER(win32more.Windows.Win32.System.AddressBook.ADRENTRY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def QueryDefaultRecipOpt(self, lpszAdrType: POINTER(SByte), ulFlags: UInt32, lpcValues: POINTER(UInt32), lppOptions: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetPAB(self, lpcbEntryID: POINTER(UInt32), lppEntryID: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SetPAB(self, cbEntryID: UInt32, lpEntryID: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetDefaultDir(self, lpcbEntryID: POINTER(UInt32), lppEntryID: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def SetDefaultDir(self, cbEntryID: UInt32, lpEntryID: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetSearchPath(self, ulFlags: UInt32, lppSearchPath: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.SRowSet))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def SetSearchPath(self, ulFlags: UInt32, lpSearchPath: POINTER(win32more.Windows.Win32.System.AddressBook.SRowSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def PrepareRecips(self, ulFlags: UInt32, lpPropTagArray: POINTER(win32more.Windows.Win32.System.AddressBook.SPropTagArray), lpRecipList: POINTER(win32more.Windows.Win32.System.AddressBook.ADRLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAttach(ComPtr):
    extends: win32more.Windows.Win32.System.AddressBook.IMAPIProp
class IDistList(ComPtr):
    extends: win32more.Windows.Win32.System.AddressBook.IMAPIContainer
    @commethod(19)
    def CreateEntry(self, cbEntryID: UInt32, lpEntryID: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID), ulCreateFlags: UInt32, lppMAPIPropEntry: POINTER(win32more.Windows.Win32.System.AddressBook.IMAPIProp)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def CopyEntries(self, lpEntries: POINTER(win32more.Windows.Win32.System.AddressBook.SBinaryArray), ulUIParam: UIntPtr, lpProgress: win32more.Windows.Win32.System.AddressBook.IMAPIProgress, ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def DeleteEntries(self, lpEntries: POINTER(win32more.Windows.Win32.System.AddressBook.SBinaryArray), ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def ResolveNames(self, lpPropTagArray: POINTER(win32more.Windows.Win32.System.AddressBook.SPropTagArray), ulFlags: UInt32, lpAdrList: POINTER(win32more.Windows.Win32.System.AddressBook.ADRLIST), lpFlagList: POINTER(win32more.Windows.Win32.System.AddressBook.FlagList)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMAPIAdviseSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def OnNotify(self, cNotif: UInt32, lpNotifications: POINTER(win32more.Windows.Win32.System.AddressBook.NOTIFICATION)) -> UInt32: ...
class IMAPIContainer(ComPtr):
    extends: win32more.Windows.Win32.System.AddressBook.IMAPIProp
    @commethod(14)
    def GetContentsTable(self, ulFlags: UInt32, lppTable: POINTER(win32more.Windows.Win32.System.AddressBook.IMAPITable)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetHierarchyTable(self, ulFlags: UInt32, lppTable: POINTER(win32more.Windows.Win32.System.AddressBook.IMAPITable)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def OpenEntry(self, cbEntryID: UInt32, lpEntryID: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID), lpInterface: POINTER(Guid), ulFlags: UInt32, lpulObjType: POINTER(UInt32), lppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetSearchCriteria(self, lpRestriction: POINTER(win32more.Windows.Win32.System.AddressBook.SRestriction), lpContainerList: POINTER(win32more.Windows.Win32.System.AddressBook.SBinaryArray), ulSearchFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetSearchCriteria(self, ulFlags: UInt32, lppRestriction: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.SRestriction)), lppContainerList: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.SBinaryArray)), lpulSearchState: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMAPIControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetLastError(self, hResult: win32more.Windows.Win32.Foundation.HRESULT, ulFlags: UInt32, lppMAPIError: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.MAPIERROR))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Activate(self, ulFlags: UInt32, ulUIParam: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetState(self, ulFlags: UInt32, lpulState: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMAPIFolder(ComPtr):
    extends: win32more.Windows.Win32.System.AddressBook.IMAPIContainer
    @commethod(19)
    def CreateMessage(self, lpInterface: POINTER(Guid), ulFlags: UInt32, lppMessage: POINTER(win32more.Windows.Win32.System.AddressBook.IMessage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def CopyMessages(self, lpMsgList: POINTER(win32more.Windows.Win32.System.AddressBook.SBinaryArray), lpInterface: POINTER(Guid), lpDestFolder: VoidPtr, ulUIParam: UIntPtr, lpProgress: win32more.Windows.Win32.System.AddressBook.IMAPIProgress, ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def DeleteMessages(self, lpMsgList: POINTER(win32more.Windows.Win32.System.AddressBook.SBinaryArray), ulUIParam: UIntPtr, lpProgress: win32more.Windows.Win32.System.AddressBook.IMAPIProgress, ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def CreateFolder(self, ulFolderType: UInt32, lpszFolderName: POINTER(SByte), lpszFolderComment: POINTER(SByte), lpInterface: POINTER(Guid), ulFlags: UInt32, lppFolder: POINTER(win32more.Windows.Win32.System.AddressBook.IMAPIFolder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def CopyFolder(self, cbEntryID: UInt32, lpEntryID: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID), lpInterface: POINTER(Guid), lpDestFolder: VoidPtr, lpszNewFolderName: POINTER(SByte), ulUIParam: UIntPtr, lpProgress: win32more.Windows.Win32.System.AddressBook.IMAPIProgress, ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def DeleteFolder(self, cbEntryID: UInt32, lpEntryID: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID), ulUIParam: UIntPtr, lpProgress: win32more.Windows.Win32.System.AddressBook.IMAPIProgress, ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetReadFlags(self, lpMsgList: POINTER(win32more.Windows.Win32.System.AddressBook.SBinaryArray), ulUIParam: UIntPtr, lpProgress: win32more.Windows.Win32.System.AddressBook.IMAPIProgress, ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetMessageStatus(self, cbEntryID: UInt32, lpEntryID: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID), ulFlags: UInt32, lpulMessageStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetMessageStatus(self, cbEntryID: UInt32, lpEntryID: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID), ulNewStatus: UInt32, ulNewStatusMask: UInt32, lpulOldStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def SaveContentsSort(self, lpSortCriteria: POINTER(win32more.Windows.Win32.System.AddressBook.SSortOrderSet), ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def EmptyFolder(self, ulUIParam: UIntPtr, lpProgress: win32more.Windows.Win32.System.AddressBook.IMAPIProgress, ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMAPIProgress(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def Progress(self, ulValue: UInt32, ulCount: UInt32, ulTotal: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFlags(self, lpulFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMax(self, lpulMax: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMin(self, lpulMin: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetLimits(self, lpulMin: POINTER(UInt32), lpulMax: POINTER(UInt32), lpulFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMAPIProp(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetLastError(self, hResult: win32more.Windows.Win32.Foundation.HRESULT, ulFlags: UInt32, lppMAPIError: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.MAPIERROR))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SaveChanges(self, ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetProps(self, lpPropTagArray: POINTER(win32more.Windows.Win32.System.AddressBook.SPropTagArray), ulFlags: UInt32, lpcValues: POINTER(UInt32), lppPropArray: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPropList(self, ulFlags: UInt32, lppPropTagArray: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.SPropTagArray))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OpenProperty(self, ulPropTag: UInt32, lpiid: POINTER(Guid), ulInterfaceOptions: UInt32, ulFlags: UInt32, lppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetProps(self, cValues: UInt32, lpPropArray: POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue), lppProblems: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.SPropProblemArray))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def DeleteProps(self, lpPropTagArray: POINTER(win32more.Windows.Win32.System.AddressBook.SPropTagArray), lppProblems: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.SPropProblemArray))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CopyTo(self, ciidExclude: UInt32, rgiidExclude: POINTER(Guid), lpExcludeProps: POINTER(win32more.Windows.Win32.System.AddressBook.SPropTagArray), ulUIParam: UIntPtr, lpProgress: win32more.Windows.Win32.System.AddressBook.IMAPIProgress, lpInterface: POINTER(Guid), lpDestObj: VoidPtr, ulFlags: UInt32, lppProblems: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.SPropProblemArray))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CopyProps(self, lpIncludeProps: POINTER(win32more.Windows.Win32.System.AddressBook.SPropTagArray), ulUIParam: UIntPtr, lpProgress: win32more.Windows.Win32.System.AddressBook.IMAPIProgress, lpInterface: POINTER(Guid), lpDestObj: VoidPtr, ulFlags: UInt32, lppProblems: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.SPropProblemArray))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetNamesFromIDs(self, lppPropTags: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.SPropTagArray)), lpPropSetGuid: POINTER(Guid), ulFlags: UInt32, lpcPropNames: POINTER(UInt32), lpppPropNames: POINTER(POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.MAPINAMEID)))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetIDsFromNames(self, cPropNames: UInt32, lppPropNames: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.MAPINAMEID)), ulFlags: UInt32, lppPropTags: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.SPropTagArray))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMAPIStatus(ComPtr):
    extends: win32more.Windows.Win32.System.AddressBook.IMAPIProp
    @commethod(14)
    def ValidateState(self, ulUIParam: UIntPtr, ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SettingsDialog(self, ulUIParam: UIntPtr, ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def ChangePassword(self, lpOldPass: POINTER(SByte), lpNewPass: POINTER(SByte), ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def FlushQueues(self, ulUIParam: UIntPtr, cbTargetTransport: UInt32, lpTargetTransport: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID), ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMAPITable(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetLastError(self, hResult: win32more.Windows.Win32.Foundation.HRESULT, ulFlags: UInt32, lppMAPIError: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.MAPIERROR))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Advise(self, ulEventMask: UInt32, lpAdviseSink: win32more.Windows.Win32.System.AddressBook.IMAPIAdviseSink, lpulConnection: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Unadvise(self, ulConnection: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStatus(self, lpulTableStatus: POINTER(UInt32), lpulTableType: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetColumns(self, lpPropTagArray: POINTER(win32more.Windows.Win32.System.AddressBook.SPropTagArray), ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def QueryColumns(self, ulFlags: UInt32, lpPropTagArray: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.SPropTagArray))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRowCount(self, ulFlags: UInt32, lpulCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SeekRow(self, bkOrigin: UInt32, lRowCount: Int32, lplRowsSought: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SeekRowApprox(self, ulNumerator: UInt32, ulDenominator: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def QueryPosition(self, lpulRow: POINTER(UInt32), lpulNumerator: POINTER(UInt32), lpulDenominator: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def FindRow(self, lpRestriction: POINTER(win32more.Windows.Win32.System.AddressBook.SRestriction), bkOrigin: UInt32, ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Restrict(self, lpRestriction: POINTER(win32more.Windows.Win32.System.AddressBook.SRestriction), ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CreateBookmark(self, lpbkPosition: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def FreeBookmark(self, bkPosition: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SortTable(self, lpSortCriteria: POINTER(win32more.Windows.Win32.System.AddressBook.SSortOrderSet), ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def QuerySortOrder(self, lppSortCriteria: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.SSortOrderSet))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def QueryRows(self, lRowCount: Int32, ulFlags: UInt32, lppRows: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.SRowSet))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def Abort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def ExpandRow(self, cbInstanceKey: UInt32, pbInstanceKey: POINTER(Byte), ulRowCount: UInt32, ulFlags: UInt32, lppRows: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.SRowSet)), lpulMoreRows: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def CollapseRow(self, cbInstanceKey: UInt32, pbInstanceKey: POINTER(Byte), ulFlags: UInt32, lpulRowCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def WaitForCompletion(self, ulFlags: UInt32, ulTimeout: UInt32, lpulTableStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetCollapseState(self, ulFlags: UInt32, cbInstanceKey: UInt32, lpbInstanceKey: POINTER(Byte), lpcbCollapseState: POINTER(UInt32), lppbCollapseState: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetCollapseState(self, ulFlags: UInt32, cbCollapseState: UInt32, pbCollapseState: POINTER(Byte), lpbkLocation: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMailUser(ComPtr):
    extends: win32more.Windows.Win32.System.AddressBook.IMAPIProp
class IMessage(ComPtr):
    extends: win32more.Windows.Win32.System.AddressBook.IMAPIProp
    @commethod(14)
    def GetAttachmentTable(self, ulFlags: UInt32, lppTable: POINTER(win32more.Windows.Win32.System.AddressBook.IMAPITable)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def OpenAttach(self, ulAttachmentNum: UInt32, lpInterface: POINTER(Guid), ulFlags: UInt32, lppAttach: POINTER(win32more.Windows.Win32.System.AddressBook.IAttach)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def CreateAttach(self, lpInterface: POINTER(Guid), ulFlags: UInt32, lpulAttachmentNum: POINTER(UInt32), lppAttach: POINTER(win32more.Windows.Win32.System.AddressBook.IAttach)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def DeleteAttach(self, ulAttachmentNum: UInt32, ulUIParam: UIntPtr, lpProgress: win32more.Windows.Win32.System.AddressBook.IMAPIProgress, ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetRecipientTable(self, ulFlags: UInt32, lppTable: POINTER(win32more.Windows.Win32.System.AddressBook.IMAPITable)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ModifyRecipients(self, ulFlags: UInt32, lpMods: POINTER(win32more.Windows.Win32.System.AddressBook.ADRLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SubmitMessage(self, ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetReadFlag(self, ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMsgStore(ComPtr):
    extends: win32more.Windows.Win32.System.AddressBook.IMAPIProp
    @commethod(14)
    def Advise(self, cbEntryID: UInt32, lpEntryID: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID), ulEventMask: UInt32, lpAdviseSink: win32more.Windows.Win32.System.AddressBook.IMAPIAdviseSink, lpulConnection: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Unadvise(self, ulConnection: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def CompareEntryIDs(self, cbEntryID1: UInt32, lpEntryID1: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID), cbEntryID2: UInt32, lpEntryID2: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID), ulFlags: UInt32, lpulResult: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def OpenEntry(self, cbEntryID: UInt32, lpEntryID: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID), lpInterface: POINTER(Guid), ulFlags: UInt32, lpulObjType: POINTER(UInt32), ppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetReceiveFolder(self, lpszMessageClass: POINTER(SByte), ulFlags: UInt32, cbEntryID: UInt32, lpEntryID: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetReceiveFolder(self, lpszMessageClass: POINTER(SByte), ulFlags: UInt32, lpcbEntryID: POINTER(UInt32), lppEntryID: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID)), lppszExplicitClass: POINTER(POINTER(SByte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetReceiveFolderTable(self, ulFlags: UInt32, lppTable: POINTER(win32more.Windows.Win32.System.AddressBook.IMAPITable)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def StoreLogoff(self, lpulFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def AbortSubmit(self, cbEntryID: UInt32, lpEntryID: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID), ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetOutgoingQueue(self, ulFlags: UInt32, lppTable: POINTER(win32more.Windows.Win32.System.AddressBook.IMAPITable)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetLockState(self, lpMessage: win32more.Windows.Win32.System.AddressBook.IMessage, ulLockState: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def FinishedMsg(self, ulFlags: UInt32, cbEntryID: UInt32, lpEntryID: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def NotifyNewMail(self, lpNotification: POINTER(win32more.Windows.Win32.System.AddressBook.NOTIFICATION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProfSect(ComPtr):
    extends: win32more.Windows.Win32.System.AddressBook.IMAPIProp
class IPropData(ComPtr):
    extends: win32more.Windows.Win32.System.AddressBook.IMAPIProp
    @commethod(14)
    def HrSetObjAccess(self, ulAccess: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def HrSetPropAccess(self, lpPropTagArray: POINTER(win32more.Windows.Win32.System.AddressBook.SPropTagArray), rgulAccess: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def HrGetPropAccess(self, lppPropTagArray: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.SPropTagArray)), lprgulAccess: POINTER(POINTER(UInt32))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def HrAddObjProps(self, lppPropTagArray: POINTER(win32more.Windows.Win32.System.AddressBook.SPropTagArray), lprgulAccess: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.SPropProblemArray))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProviderAdmin(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetLastError(self, hResult: win32more.Windows.Win32.Foundation.HRESULT, ulFlags: UInt32, lppMAPIError: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.MAPIERROR))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProviderTable(self, ulFlags: UInt32, lppTable: POINTER(win32more.Windows.Win32.System.AddressBook.IMAPITable)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateProvider(self, lpszProvider: POINTER(SByte), cValues: UInt32, lpProps: POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue), ulUIParam: UIntPtr, ulFlags: UInt32, lpUID: POINTER(win32more.Windows.Win32.System.AddressBook.MAPIUID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DeleteProvider(self, lpUID: POINTER(win32more.Windows.Win32.System.AddressBook.MAPIUID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OpenProfileSection(self, lpUID: POINTER(win32more.Windows.Win32.System.AddressBook.MAPIUID), lpInterface: POINTER(Guid), ulFlags: UInt32, lppProfSect: POINTER(win32more.Windows.Win32.System.AddressBook.IProfSect)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITableData(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def HrGetView(self, lpSSortOrderSet: POINTER(win32more.Windows.Win32.System.AddressBook.SSortOrderSet), lpfCallerRelease: POINTER(win32more.Windows.Win32.System.AddressBook.CALLERRELEASE), ulCallerData: UInt32, lppMAPITable: POINTER(win32more.Windows.Win32.System.AddressBook.IMAPITable)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def HrModifyRow(self, param0: POINTER(win32more.Windows.Win32.System.AddressBook.SRow)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def HrDeleteRow(self, lpSPropValue: POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def HrQueryRow(self, lpsPropValue: POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue), lppSRow: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.SRow)), lpuliRow: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def HrEnumRow(self, ulRowNumber: UInt32, lppSRow: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.SRow))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def HrNotify(self, ulFlags: UInt32, cValues: UInt32, lpSPropValue: POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def HrInsertRow(self, uliRow: UInt32, lpSRow: POINTER(win32more.Windows.Win32.System.AddressBook.SRow)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def HrModifyRows(self, ulFlags: UInt32, lpSRowSet: POINTER(win32more.Windows.Win32.System.AddressBook.SRowSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def HrDeleteRows(self, ulFlags: UInt32, lprowsetToDelete: POINTER(win32more.Windows.Win32.System.AddressBook.SRowSet), cRowsDeleted: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWABExtInit(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ea22ebf0-87a4-11d1-9acf-00a0c91f9c8b}')
    @commethod(3)
    def Initialize(self, lpWABExtDisplay: POINTER(win32more.Windows.Win32.System.AddressBook.WABEXTDISPLAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWABObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetLastError(self, hResult: win32more.Windows.Win32.Foundation.HRESULT, ulFlags: UInt32, lppMAPIError: POINTER(POINTER(win32more.Windows.Win32.System.AddressBook.MAPIERROR))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AllocateBuffer(self, cbSize: UInt32, lppBuffer: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AllocateMore(self, cbSize: UInt32, lpObject: VoidPtr, lppBuffer: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FreeBuffer(self, lpBuffer: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Backup(self, lpFileName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Import(self, lpWIP: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Find(self, lpIAB: win32more.Windows.Win32.System.AddressBook.IAddrBook, hWnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def VCardDisplay(self, lpIAB: win32more.Windows.Win32.System.AddressBook.IAddrBook, hWnd: win32more.Windows.Win32.Foundation.HWND, lpszFileName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def LDAPUrl(self, lpIAB: win32more.Windows.Win32.System.AddressBook.IAddrBook, hWnd: win32more.Windows.Win32.Foundation.HWND, ulFlags: UInt32, lpszURL: win32more.Windows.Win32.Foundation.PSTR, lppMailUser: POINTER(win32more.Windows.Win32.System.AddressBook.IMailUser)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def VCardCreate(self, lpIAB: win32more.Windows.Win32.System.AddressBook.IAddrBook, ulFlags: UInt32, lpszVCard: win32more.Windows.Win32.Foundation.PSTR, lpMailUser: win32more.Windows.Win32.System.AddressBook.IMailUser) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def VCardRetrieve(self, lpIAB: win32more.Windows.Win32.System.AddressBook.IAddrBook, ulFlags: UInt32, lpszVCard: win32more.Windows.Win32.Foundation.PSTR, lppMailUser: POINTER(win32more.Windows.Win32.System.AddressBook.IMailUser)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetMe(self, lpIAB: win32more.Windows.Win32.System.AddressBook.IAddrBook, ulFlags: UInt32, lpdwAction: POINTER(UInt32), lpsbEID: POINTER(win32more.Windows.Win32.System.AddressBook.SBinary), hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetMe(self, lpIAB: win32more.Windows.Win32.System.AddressBook.IAddrBook, ulFlags: UInt32, sbEID: win32more.Windows.Win32.System.AddressBook.SBinary, hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPALLOCATEBUFFER(cbSize: UInt32, lppBuffer: POINTER(VoidPtr)) -> Int32: ...
@winfunctype_pointer
def LPALLOCATEMORE(cbSize: UInt32, lpObject: VoidPtr, lppBuffer: POINTER(VoidPtr)) -> Int32: ...
@winfunctype_pointer
def LPCREATECONVERSATIONINDEX(cbParent: UInt32, lpbParent: POINTER(Byte), lpcbConvIndex: POINTER(UInt32), lppbConvIndex: POINTER(POINTER(Byte))) -> Int32: ...
@winfunctype_pointer
def LPDISPATCHNOTIFICATIONS(ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPFNABSDI(ulUIParam: UIntPtr, lpvmsg: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def LPFNBUTTON(ulUIParam: UIntPtr, lpvContext: VoidPtr, cbEntryID: UInt32, lpSelection: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID), ulFlags: UInt32) -> Int32: ...
@winfunctype_pointer
def LPFNDISMISS(ulUIParam: UIntPtr, lpvContext: VoidPtr) -> Void: ...
@winfunctype_pointer
def LPFREEBUFFER(lpBuffer: VoidPtr) -> UInt32: ...
@winfunctype_pointer
def LPNOTIFCALLBACK(lpvContext: VoidPtr, cNotification: UInt32, lpNotifications: POINTER(win32more.Windows.Win32.System.AddressBook.NOTIFICATION)) -> Int32: ...
@winfunctype_pointer
def LPOPENSTREAMONFILE(lpAllocateBuffer: win32more.Windows.Win32.System.AddressBook.LPALLOCATEBUFFER, lpFreeBuffer: win32more.Windows.Win32.System.AddressBook.LPFREEBUFFER, ulFlags: UInt32, lpszFileName: POINTER(SByte), lpszPrefix: POINTER(SByte), lppStream: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
LPWABACTIONITEM = IntPtr
@winfunctype_pointer
def LPWABALLOCATEBUFFER(lpWABObject: win32more.Windows.Win32.System.AddressBook.IWABObject, cbSize: UInt32, lppBuffer: POINTER(VoidPtr)) -> Int32: ...
@winfunctype_pointer
def LPWABALLOCATEMORE(lpWABObject: win32more.Windows.Win32.System.AddressBook.IWABObject, cbSize: UInt32, lpObject: VoidPtr, lppBuffer: POINTER(VoidPtr)) -> Int32: ...
@winfunctype_pointer
def LPWABFREEBUFFER(lpWABObject: win32more.Windows.Win32.System.AddressBook.IWABObject, lpBuffer: VoidPtr) -> UInt32: ...
@winfunctype_pointer
def LPWABOPEN(lppAdrBook: POINTER(win32more.Windows.Win32.System.AddressBook.IAddrBook), lppWABObject: POINTER(win32more.Windows.Win32.System.AddressBook.IWABObject), lpWP: POINTER(win32more.Windows.Win32.System.AddressBook.WAB_PARAM), Reserved2: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPWABOPENEX(lppAdrBook: POINTER(win32more.Windows.Win32.System.AddressBook.IAddrBook), lppWABObject: POINTER(win32more.Windows.Win32.System.AddressBook.IWABObject), lpWP: POINTER(win32more.Windows.Win32.System.AddressBook.WAB_PARAM), Reserved: UInt32, fnAllocateBuffer: win32more.Windows.Win32.System.AddressBook.LPALLOCATEBUFFER, fnAllocateMore: win32more.Windows.Win32.System.AddressBook.LPALLOCATEMORE, fnFreeBuffer: win32more.Windows.Win32.System.AddressBook.LPFREEBUFFER) -> win32more.Windows.Win32.Foundation.HRESULT: ...
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
        lpwstrName: win32more.Windows.Win32.Foundation.PWSTR
class MAPIUID(Structure):
    ab: Byte * 16
class MTSID(Structure):
    cb: UInt32
    ab: Byte * 1
class NEWMAIL_NOTIFICATION(Structure):
    cbEntryID: UInt32
    lpEntryID: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID)
    cbParentID: UInt32
    lpParentID: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID)
    ulFlags: UInt32
    lpszMessageClass: POINTER(SByte)
    ulMessageFlags: UInt32
class NOTIFICATION(Structure):
    ulEventType: UInt32
    ulAlignPad: UInt32
    info: _info_e__Union
    class _info_e__Union(Union):
        err: win32more.Windows.Win32.System.AddressBook.ERROR_NOTIFICATION
        newmail: win32more.Windows.Win32.System.AddressBook.NEWMAIL_NOTIFICATION
        obj: win32more.Windows.Win32.System.AddressBook.OBJECT_NOTIFICATION
        tab: win32more.Windows.Win32.System.AddressBook.TABLE_NOTIFICATION
        ext: win32more.Windows.Win32.System.AddressBook.EXTENDED_NOTIFICATION
        statobj: win32more.Windows.Win32.System.AddressBook.STATUS_OBJECT_NOTIFICATION
class NOTIFKEY(Structure):
    cb: UInt32
    ab: Byte * 1
class OBJECT_NOTIFICATION(Structure):
    cbEntryID: UInt32
    lpEntryID: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID)
    ulObjType: UInt32
    cbParentID: UInt32
    lpParentID: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID)
    cbOldID: UInt32
    lpOldID: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID)
    cbOldParentID: UInt32
    lpOldParentID: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID)
    lpPropTagArray: POINTER(win32more.Windows.Win32.System.AddressBook.SPropTagArray)
@winfunctype_pointer
def PFNIDLE(param0: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
class SAndRestriction(Structure):
    cRes: UInt32
    lpRes: POINTER(win32more.Windows.Win32.System.AddressBook.SRestriction)
class SAppTimeArray(Structure):
    cValues: UInt32
    lpat: POINTER(Double)
class SBinary(Structure):
    cb: UInt32
    lpb: POINTER(Byte)
class SBinaryArray(Structure):
    cValues: UInt32
    lpbin: POINTER(win32more.Windows.Win32.System.AddressBook.SBinary)
class SBitMaskRestriction(Structure):
    relBMR: UInt32
    ulPropTag: UInt32
    ulMask: UInt32
class SCommentRestriction(Structure):
    cValues: UInt32
    lpRes: POINTER(win32more.Windows.Win32.System.AddressBook.SRestriction)
    lpProp: POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue)
class SComparePropsRestriction(Structure):
    relop: UInt32
    ulPropTag1: UInt32
    ulPropTag2: UInt32
class SContentRestriction(Structure):
    ulFuzzyLevel: UInt32
    ulPropTag: UInt32
    lpProp: POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue)
class SCurrencyArray(Structure):
    cValues: UInt32
    lpcur: POINTER(win32more.Windows.Win32.System.Com.CY)
class SDateTimeArray(Structure):
    cValues: UInt32
    lpft: POINTER(win32more.Windows.Win32.Foundation.FILETIME)
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
class SLPSTRArray(Structure):
    cValues: UInt32
    lppszA: POINTER(win32more.Windows.Win32.Foundation.PSTR)
class SLargeIntegerArray(Structure):
    cValues: UInt32
    lpli: POINTER(Int64)
class SLongArray(Structure):
    cValues: UInt32
    lpl: POINTER(Int32)
class SNotRestriction(Structure):
    ulReserved: UInt32
    lpRes: POINTER(win32more.Windows.Win32.System.AddressBook.SRestriction)
class SOrRestriction(Structure):
    cRes: UInt32
    lpRes: POINTER(win32more.Windows.Win32.System.AddressBook.SRestriction)
class SPropProblem(Structure):
    ulIndex: UInt32
    ulPropTag: UInt32
    scode: Int32
class SPropProblemArray(Structure):
    cProblem: UInt32
    aProblem: win32more.Windows.Win32.System.AddressBook.SPropProblem * 1
class SPropTagArray(Structure):
    cValues: UInt32
    aulPropTag: UInt32 * 1
class SPropValue(Structure):
    ulPropTag: UInt32
    dwAlignPad: UInt32
    Value: win32more.Windows.Win32.System.AddressBook.__UPV
class SPropertyRestriction(Structure):
    relop: UInt32
    ulPropTag: UInt32
    lpProp: POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue)
class SRealArray(Structure):
    cValues: UInt32
    lpflt: POINTER(Single)
class SRestriction(Structure):
    rt: UInt32
    res: _res_e__Union
    class _res_e__Union(Union):
        resCompareProps: win32more.Windows.Win32.System.AddressBook.SComparePropsRestriction
        resAnd: win32more.Windows.Win32.System.AddressBook.SAndRestriction
        resOr: win32more.Windows.Win32.System.AddressBook.SOrRestriction
        resNot: win32more.Windows.Win32.System.AddressBook.SNotRestriction
        resContent: win32more.Windows.Win32.System.AddressBook.SContentRestriction
        resProperty: win32more.Windows.Win32.System.AddressBook.SPropertyRestriction
        resBitMask: win32more.Windows.Win32.System.AddressBook.SBitMaskRestriction
        resSize: win32more.Windows.Win32.System.AddressBook.SSizeRestriction
        resExist: win32more.Windows.Win32.System.AddressBook.SExistRestriction
        resSub: win32more.Windows.Win32.System.AddressBook.SSubRestriction
        resComment: win32more.Windows.Win32.System.AddressBook.SCommentRestriction
class SRow(Structure):
    ulAdrEntryPad: UInt32
    cValues: UInt32
    lpProps: POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue)
class SRowSet(Structure):
    cRows: UInt32
    aRow: win32more.Windows.Win32.System.AddressBook.SRow * 1
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
    aSort: win32more.Windows.Win32.System.AddressBook.SSortOrder * 1
class SSubRestriction(Structure):
    ulSubObject: UInt32
    lpRes: POINTER(win32more.Windows.Win32.System.AddressBook.SRestriction)
class STATUS_OBJECT_NOTIFICATION(Structure):
    cbEntryID: UInt32
    lpEntryID: POINTER(win32more.Windows.Win32.System.AddressBook.ENTRYID)
    cValues: UInt32
    lpPropVals: POINTER(win32more.Windows.Win32.System.AddressBook.SPropValue)
class SWStringArray(Structure):
    cValues: UInt32
    lppszW: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
class TABLE_NOTIFICATION(Structure):
    ulTableEvent: UInt32
    hResult: win32more.Windows.Win32.Foundation.HRESULT
    propIndex: win32more.Windows.Win32.System.AddressBook.SPropValue
    propPrior: win32more.Windows.Win32.System.AddressBook.SPropValue
    row: win32more.Windows.Win32.System.AddressBook.SRow
    ulPad: UInt32
class WABEXTDISPLAY(Structure):
    cbSize: UInt32
    lpWABObject: win32more.Windows.Win32.System.AddressBook.IWABObject
    lpAdrBook: win32more.Windows.Win32.System.AddressBook.IAddrBook
    lpPropObj: win32more.Windows.Win32.System.AddressBook.IMAPIProp
    fReadOnly: win32more.Windows.Win32.Foundation.BOOL
    fDataChanged: win32more.Windows.Win32.Foundation.BOOL
    ulFlags: UInt32
    lpv: VoidPtr
    lpsz: POINTER(SByte)
class WABIMPORTPARAM(Structure):
    cbSize: UInt32
    lpAdrBook: win32more.Windows.Win32.System.AddressBook.IAddrBook
    hWnd: win32more.Windows.Win32.Foundation.HWND
    ulFlags: UInt32
    lpszFileName: win32more.Windows.Win32.Foundation.PSTR
class WAB_PARAM(Structure):
    cbSize: UInt32
    hwnd: win32more.Windows.Win32.Foundation.HWND
    szFileName: win32more.Windows.Win32.Foundation.PSTR
    ulFlags: UInt32
    guidPSExt: Guid
class __UPV(Union):
    i: Int16
    l: Int32
    ul: UInt32
    flt: Single
    dbl: Double
    b: UInt16
    cur: win32more.Windows.Win32.System.Com.CY
    at: Double
    ft: win32more.Windows.Win32.Foundation.FILETIME
    lpszA: win32more.Windows.Win32.Foundation.PSTR
    bin: win32more.Windows.Win32.System.AddressBook.SBinary
    lpszW: win32more.Windows.Win32.Foundation.PWSTR
    lpguid: POINTER(Guid)
    li: Int64
    MVi: win32more.Windows.Win32.System.AddressBook.SShortArray
    MVl: win32more.Windows.Win32.System.AddressBook.SLongArray
    MVflt: win32more.Windows.Win32.System.AddressBook.SRealArray
    MVdbl: win32more.Windows.Win32.System.AddressBook.SDoubleArray
    MVcur: win32more.Windows.Win32.System.AddressBook.SCurrencyArray
    MVat: win32more.Windows.Win32.System.AddressBook.SAppTimeArray
    MVft: win32more.Windows.Win32.System.AddressBook.SDateTimeArray
    MVbin: win32more.Windows.Win32.System.AddressBook.SBinaryArray
    MVszA: win32more.Windows.Win32.System.AddressBook.SLPSTRArray
    MVszW: win32more.Windows.Win32.System.AddressBook.SWStringArray
    MVguid: win32more.Windows.Win32.System.AddressBook.SGuidArray
    MVli: win32more.Windows.Win32.System.AddressBook.SLargeIntegerArray
    err: Int32
    x: Int32


make_ready(__name__)
