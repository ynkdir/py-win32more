from win32more import *
import win32more.Foundation
import win32more.System.AddressBook
import win32more.System.Com
import win32more.System.Com.StructuredStorage

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
PROP_ID_SECURE_MIN = 26608
PROP_ID_SECURE_MAX = 26623
MAPI_DIM = 1
MAPI_P1 = 268435456
MAPI_SUBMITTED = 2147483648
MAPI_SHORTTERM = 128
MAPI_NOTRECIP = 64
MAPI_THISSESSION = 32
MAPI_NOW = 16
MAPI_NOTRESERVED = 8
MAPI_COMPOUND = 128
MV_FLAG = 4096
PROP_ID_NULL = 0
PROP_ID_INVALID = 65535
MV_INSTANCE = 8192
TABLE_CHANGED = 1
TABLE_ERROR = 2
TABLE_ROW_ADDED = 3
TABLE_ROW_DELETED = 4
TABLE_ROW_MODIFIED = 5
TABLE_SORT_DONE = 6
TABLE_RESTRICT_DONE = 7
TABLE_SETCOL_DONE = 8
TABLE_RELOAD = 9
MAPI_ERROR_VERSION = 0
MAPI_USE_DEFAULT = 64
MNID_ID = 0
MNID_STRING = 1
WAB_LOCAL_CONTAINERS = 1048576
WAB_PROFILE_CONTENTS = 2097152
WAB_IGNORE_PROFILES = 8388608
MAPI_ONE_OFF_NO_RICH_INFO = 1
UI_SERVICE = 2
SERVICE_UI_ALWAYS = 2
SERVICE_UI_ALLOWED = 16
UI_CURRENT_PROVIDER_FIRST = 4
WABOBJECT_LDAPURL_RETURN_MAILUSER = 1
WABOBJECT_ME_NEW = 1
WABOBJECT_ME_NOCREATE = 2
WAB_VCARD_FILE = 0
WAB_VCARD_STREAM = 1
WAB_USE_OE_SENDMAIL = 1
WAB_ENABLE_PROFILES = 4194304
WAB_DISPLAY_LDAPURL = 1
WAB_CONTEXT_ADRLIST = 2
WAB_DISPLAY_ISNTDS = 4
E_IMAPI_REQUEST_CANCELLED = -1062600702
E_IMAPI_RECORDER_REQUIRED = -1062600701
S_IMAPI_SPEEDADJUSTED = 11141124
S_IMAPI_ROTATIONADJUSTED = 11141125
S_IMAPI_BOTHADJUSTED = 11141126
E_IMAPI_BURN_VERIFICATION_FAILED = -1062600697
S_IMAPI_COMMAND_HAS_SENSE_DATA = 11141632
E_IMAPI_RECORDER_NO_SUCH_MODE_PAGE = -1062600191
E_IMAPI_RECORDER_MEDIA_NO_MEDIA = -1062600190
E_IMAPI_RECORDER_MEDIA_INCOMPATIBLE = -1062600189
E_IMAPI_RECORDER_MEDIA_UPSIDE_DOWN = -1062600188
E_IMAPI_RECORDER_MEDIA_BECOMING_READY = -1062600187
E_IMAPI_RECORDER_MEDIA_FORMAT_IN_PROGRESS = -1062600186
E_IMAPI_RECORDER_MEDIA_BUSY = -1062600185
E_IMAPI_RECORDER_INVALID_MODE_PARAMETERS = -1062600184
E_IMAPI_RECORDER_MEDIA_WRITE_PROTECTED = -1062600183
E_IMAPI_RECORDER_NO_SUCH_FEATURE = -1062600182
E_IMAPI_RECORDER_FEATURE_IS_NOT_CURRENT = -1062600181
E_IMAPI_RECORDER_GET_CONFIGURATION_NOT_SUPPORTED = -1062600180
E_IMAPI_RECORDER_COMMAND_TIMEOUT = -1062600179
E_IMAPI_RECORDER_DVD_STRUCTURE_NOT_PRESENT = -1062600178
E_IMAPI_RECORDER_MEDIA_SPEED_MISMATCH = -1062600177
E_IMAPI_RECORDER_LOCKED = -1062600176
E_IMAPI_RECORDER_CLIENT_NAME_IS_NOT_VALID = -1062600175
E_IMAPI_RECORDER_MEDIA_NOT_FORMATTED = -1062600174
E_IMAPI_RECORDER_INVALID_RESPONSE_FROM_DEVICE = -1062599937
E_IMAPI_LOSS_OF_STREAMING = -1062599936
E_IMAPI_UNEXPECTED_RESPONSE_FROM_DEVICE = -1062599935
S_IMAPI_WRITE_NOT_IN_PROGRESS = 11141890
E_IMAPI_DF2DATA_WRITE_IN_PROGRESS = -1062599680
E_IMAPI_DF2DATA_WRITE_NOT_IN_PROGRESS = -1062599679
E_IMAPI_DF2DATA_INVALID_MEDIA_STATE = -1062599678
E_IMAPI_DF2DATA_STREAM_NOT_SUPPORTED = -1062599677
E_IMAPI_DF2DATA_STREAM_TOO_LARGE_FOR_CURRENT_MEDIA = -1062599676
E_IMAPI_DF2DATA_MEDIA_NOT_BLANK = -1062599675
E_IMAPI_DF2DATA_MEDIA_IS_NOT_SUPPORTED = -1062599674
E_IMAPI_DF2DATA_RECORDER_NOT_SUPPORTED = -1062599673
E_IMAPI_DF2DATA_CLIENT_NAME_IS_NOT_VALID = -1062599672
E_IMAPI_DF2TAO_WRITE_IN_PROGRESS = -1062599424
E_IMAPI_DF2TAO_WRITE_NOT_IN_PROGRESS = -1062599423
E_IMAPI_DF2TAO_MEDIA_IS_NOT_PREPARED = -1062599422
E_IMAPI_DF2TAO_MEDIA_IS_PREPARED = -1062599421
E_IMAPI_DF2TAO_PROPERTY_FOR_BLANK_MEDIA_ONLY = -1062599420
E_IMAPI_DF2TAO_TABLE_OF_CONTENTS_EMPTY_DISC = -1062599419
E_IMAPI_DF2TAO_MEDIA_IS_NOT_BLANK = -1062599418
E_IMAPI_DF2TAO_MEDIA_IS_NOT_SUPPORTED = -1062599417
E_IMAPI_DF2TAO_TRACK_LIMIT_REACHED = -1062599416
E_IMAPI_DF2TAO_NOT_ENOUGH_SPACE = -1062599415
E_IMAPI_DF2TAO_NO_RECORDER_SPECIFIED = -1062599414
E_IMAPI_DF2TAO_INVALID_ISRC = -1062599413
E_IMAPI_DF2TAO_INVALID_MCN = -1062599412
E_IMAPI_DF2TAO_STREAM_NOT_SUPPORTED = -1062599411
E_IMAPI_DF2TAO_RECORDER_NOT_SUPPORTED = -1062599410
E_IMAPI_DF2TAO_CLIENT_NAME_IS_NOT_VALID = -1062599409
E_IMAPI_DF2RAW_WRITE_IN_PROGRESS = -1062599168
E_IMAPI_DF2RAW_WRITE_NOT_IN_PROGRESS = -1062599167
E_IMAPI_DF2RAW_MEDIA_IS_NOT_PREPARED = -1062599166
E_IMAPI_DF2RAW_MEDIA_IS_PREPARED = -1062599165
E_IMAPI_DF2RAW_CLIENT_NAME_IS_NOT_VALID = -1062599164
E_IMAPI_DF2RAW_MEDIA_IS_NOT_BLANK = -1062599162
E_IMAPI_DF2RAW_MEDIA_IS_NOT_SUPPORTED = -1062599161
E_IMAPI_DF2RAW_NOT_ENOUGH_SPACE = -1062599159
E_IMAPI_DF2RAW_NO_RECORDER_SPECIFIED = -1062599158
E_IMAPI_DF2RAW_STREAM_NOT_SUPPORTED = -1062599155
E_IMAPI_DF2RAW_DATA_BLOCK_TYPE_NOT_SUPPORTED = -1062599154
E_IMAPI_DF2RAW_STREAM_LEADIN_TOO_SHORT = -1062599153
E_IMAPI_DF2RAW_RECORDER_NOT_SUPPORTED = -1062599152
E_IMAPI_ERASE_RECORDER_IN_USE = -2136340224
E_IMAPI_ERASE_ONLY_ONE_RECORDER_SUPPORTED = -2136340223
E_IMAPI_ERASE_DISC_INFORMATION_TOO_SMALL = -2136340222
E_IMAPI_ERASE_MODE_PAGE_2A_TOO_SMALL = -2136340221
E_IMAPI_ERASE_MEDIA_IS_NOT_ERASABLE = -2136340220
E_IMAPI_ERASE_DRIVE_FAILED_ERASE_COMMAND = -2136340219
E_IMAPI_ERASE_TOOK_LONGER_THAN_ONE_HOUR = -2136340218
E_IMAPI_ERASE_UNEXPECTED_DRIVE_RESPONSE_DURING_ERASE = -2136340217
E_IMAPI_ERASE_DRIVE_FAILED_SPINUP_COMMAND = -2136340216
E_IMAPI_ERASE_MEDIA_IS_NOT_SUPPORTED = -1062598391
E_IMAPI_ERASE_RECORDER_NOT_SUPPORTED = -1062598390
E_IMAPI_ERASE_CLIENT_NAME_IS_NOT_VALID = -1062598389
E_IMAPI_RAW_IMAGE_IS_READ_ONLY = -2136339968
E_IMAPI_RAW_IMAGE_TOO_MANY_TRACKS = -2136339967
E_IMAPI_RAW_IMAGE_SECTOR_TYPE_NOT_SUPPORTED = -2136339966
E_IMAPI_RAW_IMAGE_NO_TRACKS = -2136339965
E_IMAPI_RAW_IMAGE_TRACKS_ALREADY_ADDED = -2136339964
E_IMAPI_RAW_IMAGE_INSUFFICIENT_SPACE = -2136339963
E_IMAPI_RAW_IMAGE_TOO_MANY_TRACK_INDEXES = -2136339962
E_IMAPI_RAW_IMAGE_TRACK_INDEX_NOT_FOUND = -2136339961
S_IMAPI_RAW_IMAGE_TRACK_INDEX_ALREADY_EXISTS = 11143688
E_IMAPI_RAW_IMAGE_TRACK_INDEX_OFFSET_ZERO_CANNOT_BE_CLEARED = -2136339959
E_IMAPI_RAW_IMAGE_TRACK_INDEX_TOO_CLOSE_TO_OTHER_INDEX = -2136339958
FACILITY_IMAPI2 = 170
IMAPI_E_FSI_INTERNAL_ERROR = -1062555392
IMAPI_E_INVALID_PARAM = -1062555391
IMAPI_E_READONLY = -1062555390
IMAPI_E_NO_OUTPUT = -1062555389
IMAPI_E_INVALID_VOLUME_NAME = -1062555388
IMAPI_E_INVALID_DATE = -1062555387
IMAPI_E_FILE_SYSTEM_NOT_EMPTY = -1062555386
IMAPI_E_NOT_FILE = -1062555384
IMAPI_E_NOT_DIR = -1062555383
IMAPI_E_DIR_NOT_EMPTY = -1062555382
IMAPI_E_NOT_IN_FILE_SYSTEM = -1062555381
IMAPI_E_INVALID_PATH = -1062555376
IMAPI_E_RESTRICTED_NAME_VIOLATION = -1062555375
IMAPI_E_DUP_NAME = -1062555374
IMAPI_E_NO_UNIQUE_NAME = -1062555373
IMAPI_E_ITEM_NOT_FOUND = -1062555368
IMAPI_E_FILE_NOT_FOUND = -1062555367
IMAPI_E_DIR_NOT_FOUND = -1062555366
IMAPI_E_IMAGE_SIZE_LIMIT = -1062555360
IMAPI_E_IMAGE_TOO_BIG = -1062555359
IMAPI_E_DATA_STREAM_INCONSISTENCY = -1062555352
IMAPI_E_DATA_STREAM_READ_FAILURE = -1062555351
IMAPI_E_DATA_STREAM_CREATE_FAILURE = -1062555350
IMAPI_E_DIRECTORY_READ_FAILURE = -1062555349
IMAPI_E_TOO_MANY_DIRS = -1062555344
IMAPI_E_ISO9660_LEVELS = -1062555343
IMAPI_E_DATA_TOO_BIG = -1062555342
IMAPI_E_INCOMPATIBLE_PREVIOUS_SESSION = -1062555341
IMAPI_E_STASHFILE_OPEN_FAILURE = -1062555336
IMAPI_E_STASHFILE_SEEK_FAILURE = -1062555335
IMAPI_E_STASHFILE_WRITE_FAILURE = -1062555334
IMAPI_E_STASHFILE_READ_FAILURE = -1062555333
IMAPI_E_INVALID_WORKING_DIRECTORY = -1062555328
IMAPI_E_WORKING_DIRECTORY_SPACE = -1062555327
IMAPI_E_STASHFILE_MOVE = -1062555326
IMAPI_E_BOOT_IMAGE_DATA = -1062555320
IMAPI_E_BOOT_OBJECT_CONFLICT = -1062555319
IMAPI_E_BOOT_EMULATION_IMAGE_SIZE_MISMATCH = -1062555318
IMAPI_E_EMPTY_DISC = -1062555312
IMAPI_E_NO_SUPPORTED_FILE_SYSTEM = -1062555311
IMAPI_E_FILE_SYSTEM_NOT_FOUND = -1062555310
IMAPI_E_FILE_SYSTEM_READ_CONSISTENCY_ERROR = -1062555309
IMAPI_E_FILE_SYSTEM_FEATURE_NOT_SUPPORTED = -1062555308
IMAPI_E_IMPORT_TYPE_COLLISION_FILE_EXISTS_AS_DIRECTORY = -1062555307
IMAPI_E_IMPORT_SEEK_FAILURE = -1062555306
IMAPI_E_IMPORT_READ_FAILURE = -1062555305
IMAPI_E_DISC_MISMATCH = -1062555304
IMAPI_E_IMPORT_MEDIA_NOT_ALLOWED = -1062555303
IMAPI_E_UDF_NOT_WRITE_COMPATIBLE = -1062555302
IMAPI_E_INCOMPATIBLE_MULTISESSION_TYPE = -1062555301
IMAPI_E_NO_COMPATIBLE_MULTISESSION_TYPE = -1062555300
IMAPI_E_MULTISESSION_NOT_SET = -1062555299
IMAPI_E_IMPORT_TYPE_COLLISION_DIRECTORY_EXISTS_AS_FILE = -1062555298
IMAPI_S_IMAGE_FEATURE_NOT_SUPPORTED = 11186527
IMAPI_E_PROPERTY_NOT_ACCESSIBLE = -1062555296
IMAPI_E_UDF_REVISION_CHANGE_NOT_ALLOWED = -1062555295
IMAPI_E_BAD_MULTISESSION_PARAMETER = -1062555294
IMAPI_E_FILE_SYSTEM_CHANGE_NOT_ALLOWED = -1062555293
IMAPI_E_IMAGEMANAGER_IMAGE_NOT_ALIGNED = -1062555136
IMAPI_E_IMAGEMANAGER_NO_VALID_VD_FOUND = -1062555135
IMAPI_E_IMAGEMANAGER_NO_IMAGE = -1062555134
IMAPI_E_IMAGEMANAGER_IMAGE_TOO_BIG = -1062555133
MAPI_E_CALL_FAILED = -2147467259
MAPI_E_NOT_ENOUGH_MEMORY = -2147024882
MAPI_E_INVALID_PARAMETER = -2147024809
MAPI_E_INTERFACE_NOT_SUPPORTED = -2147467262
MAPI_E_NO_ACCESS = -2147024891
TAD_ALL_ROWS = 1
PRILOWEST = -32768
PRIHIGHEST = 32767
PRIUSER = 0
def _define_ENTRYID_head():
    class ENTRYID(Structure):
        pass
    return ENTRYID
def _define_ENTRYID():
    ENTRYID = win32more.System.AddressBook.ENTRYID_head
    ENTRYID._fields_ = [
        ("abFlags", Byte * 4),
        ("ab", Byte * 0),
    ]
    return ENTRYID
def _define_MAPIUID_head():
    class MAPIUID(Structure):
        pass
    return MAPIUID
def _define_MAPIUID():
    MAPIUID = win32more.System.AddressBook.MAPIUID_head
    MAPIUID._fields_ = [
        ("ab", Byte * 16),
    ]
    return MAPIUID
def _define_SPropTagArray_head():
    class SPropTagArray(Structure):
        pass
    return SPropTagArray
def _define_SPropTagArray():
    SPropTagArray = win32more.System.AddressBook.SPropTagArray_head
    SPropTagArray._fields_ = [
        ("cValues", UInt32),
        ("aulPropTag", UInt32 * 0),
    ]
    return SPropTagArray
def _define_SBinary_head():
    class SBinary(Structure):
        pass
    return SBinary
def _define_SBinary():
    SBinary = win32more.System.AddressBook.SBinary_head
    SBinary._fields_ = [
        ("cb", UInt32),
        ("lpb", c_char_p_no),
    ]
    return SBinary
def _define_SShortArray_head():
    class SShortArray(Structure):
        pass
    return SShortArray
def _define_SShortArray():
    SShortArray = win32more.System.AddressBook.SShortArray_head
    SShortArray._fields_ = [
        ("cValues", UInt32),
        ("lpi", POINTER(Int16)),
    ]
    return SShortArray
def _define_SGuidArray_head():
    class SGuidArray(Structure):
        pass
    return SGuidArray
def _define_SGuidArray():
    SGuidArray = win32more.System.AddressBook.SGuidArray_head
    SGuidArray._fields_ = [
        ("cValues", UInt32),
        ("lpguid", POINTER(Guid)),
    ]
    return SGuidArray
def _define_SRealArray_head():
    class SRealArray(Structure):
        pass
    return SRealArray
def _define_SRealArray():
    SRealArray = win32more.System.AddressBook.SRealArray_head
    SRealArray._fields_ = [
        ("cValues", UInt32),
        ("lpflt", POINTER(Single)),
    ]
    return SRealArray
def _define_SLongArray_head():
    class SLongArray(Structure):
        pass
    return SLongArray
def _define_SLongArray():
    SLongArray = win32more.System.AddressBook.SLongArray_head
    SLongArray._fields_ = [
        ("cValues", UInt32),
        ("lpl", POINTER(Int32)),
    ]
    return SLongArray
def _define_SLargeIntegerArray_head():
    class SLargeIntegerArray(Structure):
        pass
    return SLargeIntegerArray
def _define_SLargeIntegerArray():
    SLargeIntegerArray = win32more.System.AddressBook.SLargeIntegerArray_head
    SLargeIntegerArray._fields_ = [
        ("cValues", UInt32),
        ("lpli", POINTER(win32more.Foundation.LARGE_INTEGER_head)),
    ]
    return SLargeIntegerArray
def _define_SDateTimeArray_head():
    class SDateTimeArray(Structure):
        pass
    return SDateTimeArray
def _define_SDateTimeArray():
    SDateTimeArray = win32more.System.AddressBook.SDateTimeArray_head
    SDateTimeArray._fields_ = [
        ("cValues", UInt32),
        ("lpft", POINTER(win32more.Foundation.FILETIME_head)),
    ]
    return SDateTimeArray
def _define_SAppTimeArray_head():
    class SAppTimeArray(Structure):
        pass
    return SAppTimeArray
def _define_SAppTimeArray():
    SAppTimeArray = win32more.System.AddressBook.SAppTimeArray_head
    SAppTimeArray._fields_ = [
        ("cValues", UInt32),
        ("lpat", POINTER(Double)),
    ]
    return SAppTimeArray
def _define_SCurrencyArray_head():
    class SCurrencyArray(Structure):
        pass
    return SCurrencyArray
def _define_SCurrencyArray():
    SCurrencyArray = win32more.System.AddressBook.SCurrencyArray_head
    SCurrencyArray._fields_ = [
        ("cValues", UInt32),
        ("lpcur", POINTER(win32more.System.Com.CY_head)),
    ]
    return SCurrencyArray
def _define_SBinaryArray_head():
    class SBinaryArray(Structure):
        pass
    return SBinaryArray
def _define_SBinaryArray():
    SBinaryArray = win32more.System.AddressBook.SBinaryArray_head
    SBinaryArray._fields_ = [
        ("cValues", UInt32),
        ("lpbin", POINTER(win32more.System.AddressBook.SBinary_head)),
    ]
    return SBinaryArray
def _define_SDoubleArray_head():
    class SDoubleArray(Structure):
        pass
    return SDoubleArray
def _define_SDoubleArray():
    SDoubleArray = win32more.System.AddressBook.SDoubleArray_head
    SDoubleArray._fields_ = [
        ("cValues", UInt32),
        ("lpdbl", POINTER(Double)),
    ]
    return SDoubleArray
def _define_SWStringArray_head():
    class SWStringArray(Structure):
        pass
    return SWStringArray
def _define_SWStringArray():
    SWStringArray = win32more.System.AddressBook.SWStringArray_head
    SWStringArray._fields_ = [
        ("cValues", UInt32),
        ("lppszW", POINTER(win32more.Foundation.PWSTR)),
    ]
    return SWStringArray
def _define_SLPSTRArray_head():
    class SLPSTRArray(Structure):
        pass
    return SLPSTRArray
def _define_SLPSTRArray():
    SLPSTRArray = win32more.System.AddressBook.SLPSTRArray_head
    SLPSTRArray._fields_ = [
        ("cValues", UInt32),
        ("lppszA", POINTER(win32more.Foundation.PSTR)),
    ]
    return SLPSTRArray
def _define__PV_head():
    class _PV(Union):
        pass
    return _PV
def _define__PV():
    _PV = win32more.System.AddressBook._PV_head
    _PV._fields_ = [
        ("i", Int16),
        ("l", Int32),
        ("ul", UInt32),
        ("flt", Single),
        ("dbl", Double),
        ("b", UInt16),
        ("cur", win32more.System.Com.CY),
        ("at", Double),
        ("ft", win32more.Foundation.FILETIME),
        ("lpszA", win32more.Foundation.PSTR),
        ("bin", win32more.System.AddressBook.SBinary),
        ("lpszW", win32more.Foundation.PWSTR),
        ("lpguid", POINTER(Guid)),
        ("li", win32more.Foundation.LARGE_INTEGER),
        ("MVi", win32more.System.AddressBook.SShortArray),
        ("MVl", win32more.System.AddressBook.SLongArray),
        ("MVflt", win32more.System.AddressBook.SRealArray),
        ("MVdbl", win32more.System.AddressBook.SDoubleArray),
        ("MVcur", win32more.System.AddressBook.SCurrencyArray),
        ("MVat", win32more.System.AddressBook.SAppTimeArray),
        ("MVft", win32more.System.AddressBook.SDateTimeArray),
        ("MVbin", win32more.System.AddressBook.SBinaryArray),
        ("MVszA", win32more.System.AddressBook.SLPSTRArray),
        ("MVszW", win32more.System.AddressBook.SWStringArray),
        ("MVguid", win32more.System.AddressBook.SGuidArray),
        ("MVli", win32more.System.AddressBook.SLargeIntegerArray),
        ("err", Int32),
        ("x", Int32),
    ]
    return _PV
def _define_SPropValue_head():
    class SPropValue(Structure):
        pass
    return SPropValue
def _define_SPropValue():
    SPropValue = win32more.System.AddressBook.SPropValue_head
    SPropValue._fields_ = [
        ("ulPropTag", UInt32),
        ("dwAlignPad", UInt32),
        ("Value", win32more.System.AddressBook._PV),
    ]
    return SPropValue
def _define_SPropProblem_head():
    class SPropProblem(Structure):
        pass
    return SPropProblem
def _define_SPropProblem():
    SPropProblem = win32more.System.AddressBook.SPropProblem_head
    SPropProblem._fields_ = [
        ("ulIndex", UInt32),
        ("ulPropTag", UInt32),
        ("scode", Int32),
    ]
    return SPropProblem
def _define_SPropProblemArray_head():
    class SPropProblemArray(Structure):
        pass
    return SPropProblemArray
def _define_SPropProblemArray():
    SPropProblemArray = win32more.System.AddressBook.SPropProblemArray_head
    SPropProblemArray._fields_ = [
        ("cProblem", UInt32),
        ("aProblem", win32more.System.AddressBook.SPropProblem * 0),
    ]
    return SPropProblemArray
def _define_FLATENTRY_head():
    class FLATENTRY(Structure):
        pass
    return FLATENTRY
def _define_FLATENTRY():
    FLATENTRY = win32more.System.AddressBook.FLATENTRY_head
    FLATENTRY._fields_ = [
        ("cb", UInt32),
        ("abEntry", Byte * 0),
    ]
    return FLATENTRY
def _define_FLATENTRYLIST_head():
    class FLATENTRYLIST(Structure):
        pass
    return FLATENTRYLIST
def _define_FLATENTRYLIST():
    FLATENTRYLIST = win32more.System.AddressBook.FLATENTRYLIST_head
    FLATENTRYLIST._fields_ = [
        ("cEntries", UInt32),
        ("cbEntries", UInt32),
        ("abEntries", Byte * 0),
    ]
    return FLATENTRYLIST
def _define_MTSID_head():
    class MTSID(Structure):
        pass
    return MTSID
def _define_MTSID():
    MTSID = win32more.System.AddressBook.MTSID_head
    MTSID._fields_ = [
        ("cb", UInt32),
        ("ab", Byte * 0),
    ]
    return MTSID
def _define_FLATMTSIDLIST_head():
    class FLATMTSIDLIST(Structure):
        pass
    return FLATMTSIDLIST
def _define_FLATMTSIDLIST():
    FLATMTSIDLIST = win32more.System.AddressBook.FLATMTSIDLIST_head
    FLATMTSIDLIST._fields_ = [
        ("cMTSIDs", UInt32),
        ("cbMTSIDs", UInt32),
        ("abMTSIDs", Byte * 0),
    ]
    return FLATMTSIDLIST
def _define_ADRENTRY_head():
    class ADRENTRY(Structure):
        pass
    return ADRENTRY
def _define_ADRENTRY():
    ADRENTRY = win32more.System.AddressBook.ADRENTRY_head
    ADRENTRY._fields_ = [
        ("ulReserved1", UInt32),
        ("cValues", UInt32),
        ("rgPropVals", POINTER(win32more.System.AddressBook.SPropValue_head)),
    ]
    return ADRENTRY
def _define_ADRLIST_head():
    class ADRLIST(Structure):
        pass
    return ADRLIST
def _define_ADRLIST():
    ADRLIST = win32more.System.AddressBook.ADRLIST_head
    ADRLIST._fields_ = [
        ("cEntries", UInt32),
        ("aEntries", win32more.System.AddressBook.ADRENTRY * 0),
    ]
    return ADRLIST
def _define_SRow_head():
    class SRow(Structure):
        pass
    return SRow
def _define_SRow():
    SRow = win32more.System.AddressBook.SRow_head
    SRow._fields_ = [
        ("ulAdrEntryPad", UInt32),
        ("cValues", UInt32),
        ("lpProps", POINTER(win32more.System.AddressBook.SPropValue_head)),
    ]
    return SRow
def _define_SRowSet_head():
    class SRowSet(Structure):
        pass
    return SRowSet
def _define_SRowSet():
    SRowSet = win32more.System.AddressBook.SRowSet_head
    SRowSet._fields_ = [
        ("cRows", UInt32),
        ("aRow", win32more.System.AddressBook.SRow * 0),
    ]
    return SRowSet
def _define_LPALLOCATEBUFFER():
    return CFUNCTYPE(Int32,UInt32,POINTER(c_void_p), use_last_error=False)
def _define_LPALLOCATEMORE():
    return CFUNCTYPE(Int32,UInt32,c_void_p,POINTER(c_void_p), use_last_error=False)
def _define_LPFREEBUFFER():
    return CFUNCTYPE(UInt32,c_void_p, use_last_error=False)
def _define_MAPIERROR_head():
    class MAPIERROR(Structure):
        pass
    return MAPIERROR
def _define_MAPIERROR():
    MAPIERROR = win32more.System.AddressBook.MAPIERROR_head
    MAPIERROR._fields_ = [
        ("ulVersion", UInt32),
        ("lpszError", POINTER(SByte)),
        ("lpszComponent", POINTER(SByte)),
        ("ulLowLevelError", UInt32),
        ("ulContext", UInt32),
    ]
    return MAPIERROR
def _define_ERROR_NOTIFICATION_head():
    class ERROR_NOTIFICATION(Structure):
        pass
    return ERROR_NOTIFICATION
def _define_ERROR_NOTIFICATION():
    ERROR_NOTIFICATION = win32more.System.AddressBook.ERROR_NOTIFICATION_head
    ERROR_NOTIFICATION._fields_ = [
        ("cbEntryID", UInt32),
        ("lpEntryID", POINTER(win32more.System.AddressBook.ENTRYID_head)),
        ("scode", Int32),
        ("ulFlags", UInt32),
        ("lpMAPIError", POINTER(win32more.System.AddressBook.MAPIERROR_head)),
    ]
    return ERROR_NOTIFICATION
def _define_NEWMAIL_NOTIFICATION_head():
    class NEWMAIL_NOTIFICATION(Structure):
        pass
    return NEWMAIL_NOTIFICATION
def _define_NEWMAIL_NOTIFICATION():
    NEWMAIL_NOTIFICATION = win32more.System.AddressBook.NEWMAIL_NOTIFICATION_head
    NEWMAIL_NOTIFICATION._fields_ = [
        ("cbEntryID", UInt32),
        ("lpEntryID", POINTER(win32more.System.AddressBook.ENTRYID_head)),
        ("cbParentID", UInt32),
        ("lpParentID", POINTER(win32more.System.AddressBook.ENTRYID_head)),
        ("ulFlags", UInt32),
        ("lpszMessageClass", POINTER(SByte)),
        ("ulMessageFlags", UInt32),
    ]
    return NEWMAIL_NOTIFICATION
def _define_OBJECT_NOTIFICATION_head():
    class OBJECT_NOTIFICATION(Structure):
        pass
    return OBJECT_NOTIFICATION
def _define_OBJECT_NOTIFICATION():
    OBJECT_NOTIFICATION = win32more.System.AddressBook.OBJECT_NOTIFICATION_head
    OBJECT_NOTIFICATION._fields_ = [
        ("cbEntryID", UInt32),
        ("lpEntryID", POINTER(win32more.System.AddressBook.ENTRYID_head)),
        ("ulObjType", UInt32),
        ("cbParentID", UInt32),
        ("lpParentID", POINTER(win32more.System.AddressBook.ENTRYID_head)),
        ("cbOldID", UInt32),
        ("lpOldID", POINTER(win32more.System.AddressBook.ENTRYID_head)),
        ("cbOldParentID", UInt32),
        ("lpOldParentID", POINTER(win32more.System.AddressBook.ENTRYID_head)),
        ("lpPropTagArray", POINTER(win32more.System.AddressBook.SPropTagArray_head)),
    ]
    return OBJECT_NOTIFICATION
def _define_TABLE_NOTIFICATION_head():
    class TABLE_NOTIFICATION(Structure):
        pass
    return TABLE_NOTIFICATION
def _define_TABLE_NOTIFICATION():
    TABLE_NOTIFICATION = win32more.System.AddressBook.TABLE_NOTIFICATION_head
    TABLE_NOTIFICATION._fields_ = [
        ("ulTableEvent", UInt32),
        ("hResult", win32more.Foundation.HRESULT),
        ("propIndex", win32more.System.AddressBook.SPropValue),
        ("propPrior", win32more.System.AddressBook.SPropValue),
        ("row", win32more.System.AddressBook.SRow),
        ("ulPad", UInt32),
    ]
    return TABLE_NOTIFICATION
def _define_EXTENDED_NOTIFICATION_head():
    class EXTENDED_NOTIFICATION(Structure):
        pass
    return EXTENDED_NOTIFICATION
def _define_EXTENDED_NOTIFICATION():
    EXTENDED_NOTIFICATION = win32more.System.AddressBook.EXTENDED_NOTIFICATION_head
    EXTENDED_NOTIFICATION._fields_ = [
        ("ulEvent", UInt32),
        ("cb", UInt32),
        ("pbEventParameters", c_char_p_no),
    ]
    return EXTENDED_NOTIFICATION
def _define_STATUS_OBJECT_NOTIFICATION_head():
    class STATUS_OBJECT_NOTIFICATION(Structure):
        pass
    return STATUS_OBJECT_NOTIFICATION
def _define_STATUS_OBJECT_NOTIFICATION():
    STATUS_OBJECT_NOTIFICATION = win32more.System.AddressBook.STATUS_OBJECT_NOTIFICATION_head
    STATUS_OBJECT_NOTIFICATION._fields_ = [
        ("cbEntryID", UInt32),
        ("lpEntryID", POINTER(win32more.System.AddressBook.ENTRYID_head)),
        ("cValues", UInt32),
        ("lpPropVals", POINTER(win32more.System.AddressBook.SPropValue_head)),
    ]
    return STATUS_OBJECT_NOTIFICATION
def _define_NOTIFICATION_head():
    class NOTIFICATION(Structure):
        pass
    return NOTIFICATION
def _define_NOTIFICATION():
    NOTIFICATION = win32more.System.AddressBook.NOTIFICATION_head
    class NOTIFICATION__info_e__Union(Union):
        pass
    NOTIFICATION__info_e__Union._fields_ = [
        ("err", win32more.System.AddressBook.ERROR_NOTIFICATION),
        ("newmail", win32more.System.AddressBook.NEWMAIL_NOTIFICATION),
        ("obj", win32more.System.AddressBook.OBJECT_NOTIFICATION),
        ("tab", win32more.System.AddressBook.TABLE_NOTIFICATION),
        ("ext", win32more.System.AddressBook.EXTENDED_NOTIFICATION),
        ("statobj", win32more.System.AddressBook.STATUS_OBJECT_NOTIFICATION),
    ]
    NOTIFICATION._fields_ = [
        ("ulEventType", UInt32),
        ("ulAlignPad", UInt32),
        ("info", NOTIFICATION__info_e__Union),
    ]
    return NOTIFICATION
def _define_IMAPIAdviseSink_head():
    class IMAPIAdviseSink(win32more.System.Com.IUnknown_head):
        Guid = Guid(None)
    return IMAPIAdviseSink
def _define_IMAPIAdviseSink():
    IMAPIAdviseSink = win32more.System.AddressBook.IMAPIAdviseSink_head
    IMAPIAdviseSink.OnNotify = COMMETHOD(WINFUNCTYPE(UInt32,UInt32,POINTER(win32more.System.AddressBook.NOTIFICATION_head), use_last_error=False)(3, 'OnNotify', ((1, 'cNotif'),(1, 'lpNotifications'),)))
    return IMAPIAdviseSink
def _define_LPNOTIFCALLBACK():
    return CFUNCTYPE(Int32,c_void_p,UInt32,POINTER(win32more.System.AddressBook.NOTIFICATION_head), use_last_error=False)
def _define_IMAPIProgress_head():
    class IMAPIProgress(win32more.System.Com.IUnknown_head):
        Guid = Guid(None)
    return IMAPIProgress
def _define_IMAPIProgress():
    IMAPIProgress = win32more.System.AddressBook.IMAPIProgress_head
    IMAPIProgress.Progress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32, use_last_error=False)(3, 'Progress', ((1, 'ulValue'),(1, 'ulCount'),(1, 'ulTotal'),)))
    IMAPIProgress.GetFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetFlags', ((1, 'lpulFlags'),)))
    IMAPIProgress.GetMax = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetMax', ((1, 'lpulMax'),)))
    IMAPIProgress.GetMin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'GetMin', ((1, 'lpulMin'),)))
    IMAPIProgress.SetLimits = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(7, 'SetLimits', ((1, 'lpulMin'),(1, 'lpulMax'),(1, 'lpulFlags'),)))
    return IMAPIProgress
def _define_MAPINAMEID_head():
    class MAPINAMEID(Structure):
        pass
    return MAPINAMEID
def _define_MAPINAMEID():
    MAPINAMEID = win32more.System.AddressBook.MAPINAMEID_head
    class MAPINAMEID__Kind_e__Union(Union):
        pass
    MAPINAMEID__Kind_e__Union._fields_ = [
        ("lID", Int32),
        ("lpwstrName", win32more.Foundation.PWSTR),
    ]
    MAPINAMEID._fields_ = [
        ("lpguid", POINTER(Guid)),
        ("ulKind", UInt32),
        ("Kind", MAPINAMEID__Kind_e__Union),
    ]
    return MAPINAMEID
def _define_IMAPIProp_head():
    class IMAPIProp(win32more.System.Com.IUnknown_head):
        Guid = Guid(None)
    return IMAPIProp
def _define_IMAPIProp():
    IMAPIProp = win32more.System.AddressBook.IMAPIProp_head
    IMAPIProp.GetLastError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.System.AddressBook.MAPIERROR_head)), use_last_error=False)(3, 'GetLastError', ((1, 'hResult'),(1, 'ulFlags'),(1, 'lppMAPIError'),)))
    IMAPIProp.SaveChanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'SaveChanges', ((1, 'ulFlags'),)))
    IMAPIProp.GetProps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.SPropTagArray_head),UInt32,POINTER(UInt32),POINTER(POINTER(win32more.System.AddressBook.SPropValue_head)), use_last_error=False)(5, 'GetProps', ((1, 'lpPropTagArray'),(1, 'ulFlags'),(1, 'lpcValues'),(1, 'lppPropArray'),)))
    IMAPIProp.GetPropList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.System.AddressBook.SPropTagArray_head)), use_last_error=False)(6, 'GetPropList', ((1, 'ulFlags'),(1, 'lppPropTagArray'),)))
    IMAPIProp.OpenProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),UInt32,UInt32,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'OpenProperty', ((1, 'ulPropTag'),(1, 'lpiid'),(1, 'ulInterfaceOptions'),(1, 'ulFlags'),(1, 'lppUnk'),)))
    IMAPIProp.SetProps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.SPropValue_head),POINTER(POINTER(win32more.System.AddressBook.SPropProblemArray_head)), use_last_error=False)(8, 'SetProps', ((1, 'cValues'),(1, 'lpPropArray'),(1, 'lppProblems'),)))
    IMAPIProp.DeleteProps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.SPropTagArray_head),POINTER(POINTER(win32more.System.AddressBook.SPropProblemArray_head)), use_last_error=False)(9, 'DeleteProps', ((1, 'lpPropTagArray'),(1, 'lppProblems'),)))
    IMAPIProp.CopyTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(win32more.System.AddressBook.SPropTagArray_head),UIntPtr,win32more.System.AddressBook.IMAPIProgress_head,POINTER(Guid),c_void_p,UInt32,POINTER(POINTER(win32more.System.AddressBook.SPropProblemArray_head)), use_last_error=False)(10, 'CopyTo', ((1, 'ciidExclude'),(1, 'rgiidExclude'),(1, 'lpExcludeProps'),(1, 'ulUIParam'),(1, 'lpProgress'),(1, 'lpInterface'),(1, 'lpDestObj'),(1, 'ulFlags'),(1, 'lppProblems'),)))
    IMAPIProp.CopyProps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.SPropTagArray_head),UIntPtr,win32more.System.AddressBook.IMAPIProgress_head,POINTER(Guid),c_void_p,UInt32,POINTER(POINTER(win32more.System.AddressBook.SPropProblemArray_head)), use_last_error=False)(11, 'CopyProps', ((1, 'lpIncludeProps'),(1, 'ulUIParam'),(1, 'lpProgress'),(1, 'lpInterface'),(1, 'lpDestObj'),(1, 'ulFlags'),(1, 'lppProblems'),)))
    IMAPIProp.GetNamesFromIDs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.AddressBook.SPropTagArray_head)),POINTER(Guid),UInt32,POINTER(UInt32),POINTER(POINTER(POINTER(win32more.System.AddressBook.MAPINAMEID_head))), use_last_error=False)(12, 'GetNamesFromIDs', ((1, 'lppPropTags'),(1, 'lpPropSetGuid'),(1, 'ulFlags'),(1, 'lpcPropNames'),(1, 'lpppPropNames'),)))
    IMAPIProp.GetIDsFromNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.System.AddressBook.MAPINAMEID_head)),UInt32,POINTER(POINTER(win32more.System.AddressBook.SPropTagArray_head)), use_last_error=False)(13, 'GetIDsFromNames', ((1, 'cPropNames'),(1, 'lppPropNames'),(1, 'ulFlags'),(1, 'lppPropTags'),)))
    return IMAPIProp
def _define_SSortOrder_head():
    class SSortOrder(Structure):
        pass
    return SSortOrder
def _define_SSortOrder():
    SSortOrder = win32more.System.AddressBook.SSortOrder_head
    SSortOrder._fields_ = [
        ("ulPropTag", UInt32),
        ("ulOrder", UInt32),
    ]
    return SSortOrder
def _define_SSortOrderSet_head():
    class SSortOrderSet(Structure):
        pass
    return SSortOrderSet
def _define_SSortOrderSet():
    SSortOrderSet = win32more.System.AddressBook.SSortOrderSet_head
    SSortOrderSet._fields_ = [
        ("cSorts", UInt32),
        ("cCategories", UInt32),
        ("cExpanded", UInt32),
        ("aSort", win32more.System.AddressBook.SSortOrder * 0),
    ]
    return SSortOrderSet
def _define_SAndRestriction_head():
    class SAndRestriction(Structure):
        pass
    return SAndRestriction
def _define_SAndRestriction():
    SAndRestriction = win32more.System.AddressBook.SAndRestriction_head
    SAndRestriction._fields_ = [
        ("cRes", UInt32),
        ("lpRes", POINTER(win32more.System.AddressBook.SRestriction_head)),
    ]
    return SAndRestriction
def _define_SOrRestriction_head():
    class SOrRestriction(Structure):
        pass
    return SOrRestriction
def _define_SOrRestriction():
    SOrRestriction = win32more.System.AddressBook.SOrRestriction_head
    SOrRestriction._fields_ = [
        ("cRes", UInt32),
        ("lpRes", POINTER(win32more.System.AddressBook.SRestriction_head)),
    ]
    return SOrRestriction
def _define_SNotRestriction_head():
    class SNotRestriction(Structure):
        pass
    return SNotRestriction
def _define_SNotRestriction():
    SNotRestriction = win32more.System.AddressBook.SNotRestriction_head
    SNotRestriction._fields_ = [
        ("ulReserved", UInt32),
        ("lpRes", POINTER(win32more.System.AddressBook.SRestriction_head)),
    ]
    return SNotRestriction
def _define_SContentRestriction_head():
    class SContentRestriction(Structure):
        pass
    return SContentRestriction
def _define_SContentRestriction():
    SContentRestriction = win32more.System.AddressBook.SContentRestriction_head
    SContentRestriction._fields_ = [
        ("ulFuzzyLevel", UInt32),
        ("ulPropTag", UInt32),
        ("lpProp", POINTER(win32more.System.AddressBook.SPropValue_head)),
    ]
    return SContentRestriction
def _define_SBitMaskRestriction_head():
    class SBitMaskRestriction(Structure):
        pass
    return SBitMaskRestriction
def _define_SBitMaskRestriction():
    SBitMaskRestriction = win32more.System.AddressBook.SBitMaskRestriction_head
    SBitMaskRestriction._fields_ = [
        ("relBMR", UInt32),
        ("ulPropTag", UInt32),
        ("ulMask", UInt32),
    ]
    return SBitMaskRestriction
def _define_SPropertyRestriction_head():
    class SPropertyRestriction(Structure):
        pass
    return SPropertyRestriction
def _define_SPropertyRestriction():
    SPropertyRestriction = win32more.System.AddressBook.SPropertyRestriction_head
    SPropertyRestriction._fields_ = [
        ("relop", UInt32),
        ("ulPropTag", UInt32),
        ("lpProp", POINTER(win32more.System.AddressBook.SPropValue_head)),
    ]
    return SPropertyRestriction
def _define_SComparePropsRestriction_head():
    class SComparePropsRestriction(Structure):
        pass
    return SComparePropsRestriction
def _define_SComparePropsRestriction():
    SComparePropsRestriction = win32more.System.AddressBook.SComparePropsRestriction_head
    SComparePropsRestriction._fields_ = [
        ("relop", UInt32),
        ("ulPropTag1", UInt32),
        ("ulPropTag2", UInt32),
    ]
    return SComparePropsRestriction
def _define_SSizeRestriction_head():
    class SSizeRestriction(Structure):
        pass
    return SSizeRestriction
def _define_SSizeRestriction():
    SSizeRestriction = win32more.System.AddressBook.SSizeRestriction_head
    SSizeRestriction._fields_ = [
        ("relop", UInt32),
        ("ulPropTag", UInt32),
        ("cb", UInt32),
    ]
    return SSizeRestriction
def _define_SExistRestriction_head():
    class SExistRestriction(Structure):
        pass
    return SExistRestriction
def _define_SExistRestriction():
    SExistRestriction = win32more.System.AddressBook.SExistRestriction_head
    SExistRestriction._fields_ = [
        ("ulReserved1", UInt32),
        ("ulPropTag", UInt32),
        ("ulReserved2", UInt32),
    ]
    return SExistRestriction
def _define_SSubRestriction_head():
    class SSubRestriction(Structure):
        pass
    return SSubRestriction
def _define_SSubRestriction():
    SSubRestriction = win32more.System.AddressBook.SSubRestriction_head
    SSubRestriction._fields_ = [
        ("ulSubObject", UInt32),
        ("lpRes", POINTER(win32more.System.AddressBook.SRestriction_head)),
    ]
    return SSubRestriction
def _define_SCommentRestriction_head():
    class SCommentRestriction(Structure):
        pass
    return SCommentRestriction
def _define_SCommentRestriction():
    SCommentRestriction = win32more.System.AddressBook.SCommentRestriction_head
    SCommentRestriction._fields_ = [
        ("cValues", UInt32),
        ("lpRes", POINTER(win32more.System.AddressBook.SRestriction_head)),
        ("lpProp", POINTER(win32more.System.AddressBook.SPropValue_head)),
    ]
    return SCommentRestriction
def _define_SRestriction_head():
    class SRestriction(Structure):
        pass
    return SRestriction
def _define_SRestriction():
    SRestriction = win32more.System.AddressBook.SRestriction_head
    class SRestriction__res_e__Union(Union):
        pass
    SRestriction__res_e__Union._fields_ = [
        ("resCompareProps", win32more.System.AddressBook.SComparePropsRestriction),
        ("resAnd", win32more.System.AddressBook.SAndRestriction),
        ("resOr", win32more.System.AddressBook.SOrRestriction),
        ("resNot", win32more.System.AddressBook.SNotRestriction),
        ("resContent", win32more.System.AddressBook.SContentRestriction),
        ("resProperty", win32more.System.AddressBook.SPropertyRestriction),
        ("resBitMask", win32more.System.AddressBook.SBitMaskRestriction),
        ("resSize", win32more.System.AddressBook.SSizeRestriction),
        ("resExist", win32more.System.AddressBook.SExistRestriction),
        ("resSub", win32more.System.AddressBook.SSubRestriction),
        ("resComment", win32more.System.AddressBook.SCommentRestriction),
    ]
    SRestriction._fields_ = [
        ("rt", UInt32),
        ("res", SRestriction__res_e__Union),
    ]
    return SRestriction
def _define_IMAPITable_head():
    class IMAPITable(win32more.System.Com.IUnknown_head):
        Guid = Guid(None)
    return IMAPITable
def _define_IMAPITable():
    IMAPITable = win32more.System.AddressBook.IMAPITable_head
    IMAPITable.GetLastError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.System.AddressBook.MAPIERROR_head)), use_last_error=False)(3, 'GetLastError', ((1, 'hResult'),(1, 'ulFlags'),(1, 'lppMAPIError'),)))
    IMAPITable.Advise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.AddressBook.IMAPIAdviseSink_head,POINTER(UInt32), use_last_error=False)(4, 'Advise', ((1, 'ulEventMask'),(1, 'lpAdviseSink'),(1, 'lpulConnection'),)))
    IMAPITable.Unadvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'Unadvise', ((1, 'ulConnection'),)))
    IMAPITable.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(6, 'GetStatus', ((1, 'lpulTableStatus'),(1, 'lpulTableType'),)))
    IMAPITable.SetColumns = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.SPropTagArray_head),UInt32, use_last_error=False)(7, 'SetColumns', ((1, 'lpPropTagArray'),(1, 'ulFlags'),)))
    IMAPITable.QueryColumns = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.System.AddressBook.SPropTagArray_head)), use_last_error=False)(8, 'QueryColumns', ((1, 'ulFlags'),(1, 'lpPropTagArray'),)))
    IMAPITable.GetRowCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(9, 'GetRowCount', ((1, 'ulFlags'),(1, 'lpulCount'),)))
    IMAPITable.SeekRow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32,POINTER(Int32), use_last_error=False)(10, 'SeekRow', ((1, 'bkOrigin'),(1, 'lRowCount'),(1, 'lplRowsSought'),)))
    IMAPITable.SeekRowApprox = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(11, 'SeekRowApprox', ((1, 'ulNumerator'),(1, 'ulDenominator'),)))
    IMAPITable.QueryPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(12, 'QueryPosition', ((1, 'lpulRow'),(1, 'lpulNumerator'),(1, 'lpulDenominator'),)))
    IMAPITable.FindRow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.SRestriction_head),UInt32,UInt32, use_last_error=False)(13, 'FindRow', ((1, 'lpRestriction'),(1, 'bkOrigin'),(1, 'ulFlags'),)))
    IMAPITable.Restrict = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.SRestriction_head),UInt32, use_last_error=False)(14, 'Restrict', ((1, 'lpRestriction'),(1, 'ulFlags'),)))
    IMAPITable.CreateBookmark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(15, 'CreateBookmark', ((1, 'lpbkPosition'),)))
    IMAPITable.FreeBookmark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(16, 'FreeBookmark', ((1, 'bkPosition'),)))
    IMAPITable.SortTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.SSortOrderSet_head),UInt32, use_last_error=False)(17, 'SortTable', ((1, 'lpSortCriteria'),(1, 'ulFlags'),)))
    IMAPITable.QuerySortOrder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.AddressBook.SSortOrderSet_head)), use_last_error=False)(18, 'QuerySortOrder', ((1, 'lppSortCriteria'),)))
    IMAPITable.QueryRows = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32,POINTER(POINTER(win32more.System.AddressBook.SRowSet_head)), use_last_error=False)(19, 'QueryRows', ((1, 'lRowCount'),(1, 'ulFlags'),(1, 'lppRows'),)))
    IMAPITable.Abort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(20, 'Abort', ()))
    IMAPITable.ExpandRow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_char_p_no,UInt32,UInt32,POINTER(POINTER(win32more.System.AddressBook.SRowSet_head)),POINTER(UInt32), use_last_error=False)(21, 'ExpandRow', ((1, 'cbInstanceKey'),(1, 'pbInstanceKey'),(1, 'ulRowCount'),(1, 'ulFlags'),(1, 'lppRows'),(1, 'lpulMoreRows'),)))
    IMAPITable.CollapseRow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_char_p_no,UInt32,POINTER(UInt32), use_last_error=False)(22, 'CollapseRow', ((1, 'cbInstanceKey'),(1, 'pbInstanceKey'),(1, 'ulFlags'),(1, 'lpulRowCount'),)))
    IMAPITable.WaitForCompletion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(UInt32), use_last_error=False)(23, 'WaitForCompletion', ((1, 'ulFlags'),(1, 'ulTimeout'),(1, 'lpulTableStatus'),)))
    IMAPITable.GetCollapseState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,c_char_p_no,POINTER(UInt32),POINTER(c_char_p_no), use_last_error=False)(24, 'GetCollapseState', ((1, 'ulFlags'),(1, 'cbInstanceKey'),(1, 'lpbInstanceKey'),(1, 'lpcbCollapseState'),(1, 'lppbCollapseState'),)))
    IMAPITable.SetCollapseState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,c_char_p_no,POINTER(UInt32), use_last_error=False)(25, 'SetCollapseState', ((1, 'ulFlags'),(1, 'cbCollapseState'),(1, 'pbCollapseState'),(1, 'lpbkLocation'),)))
    return IMAPITable
def _define_IProfSect_head():
    class IProfSect(win32more.System.AddressBook.IMAPIProp_head):
        Guid = Guid(None)
    return IProfSect
def _define_IProfSect():
    IProfSect = win32more.System.AddressBook.IProfSect_head
    return IProfSect
def _define_IMAPIStatus_head():
    class IMAPIStatus(win32more.System.AddressBook.IMAPIProp_head):
        Guid = Guid(None)
    return IMAPIStatus
def _define_IMAPIStatus():
    IMAPIStatus = win32more.System.AddressBook.IMAPIStatus_head
    IMAPIStatus.ValidateState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,UInt32, use_last_error=False)(14, 'ValidateState', ((1, 'ulUIParam'),(1, 'ulFlags'),)))
    IMAPIStatus.SettingsDialog = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,UInt32, use_last_error=False)(15, 'SettingsDialog', ((1, 'ulUIParam'),(1, 'ulFlags'),)))
    IMAPIStatus.ChangePassword = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(SByte),POINTER(SByte),UInt32, use_last_error=False)(16, 'ChangePassword', ((1, 'lpOldPass'),(1, 'lpNewPass'),(1, 'ulFlags'),)))
    IMAPIStatus.FlushQueues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,UInt32,POINTER(win32more.System.AddressBook.ENTRYID),UInt32, use_last_error=False)(17, 'FlushQueues', ((1, 'ulUIParam'),(1, 'cbTargetTransport'),(1, 'lpTargetTransport'),(1, 'ulFlags'),)))
    return IMAPIStatus
def _define_IMAPIContainer_head():
    class IMAPIContainer(win32more.System.AddressBook.IMAPIProp_head):
        Guid = Guid(None)
    return IMAPIContainer
def _define_IMAPIContainer():
    IMAPIContainer = win32more.System.AddressBook.IMAPIContainer_head
    IMAPIContainer.GetContentsTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.IMAPITable_head), use_last_error=False)(14, 'GetContentsTable', ((1, 'ulFlags'),(1, 'lppTable'),)))
    IMAPIContainer.GetHierarchyTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.IMAPITable_head), use_last_error=False)(15, 'GetHierarchyTable', ((1, 'ulFlags'),(1, 'lppTable'),)))
    IMAPIContainer.OpenEntry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.ENTRYID_head),POINTER(Guid),UInt32,POINTER(UInt32),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(16, 'OpenEntry', ((1, 'cbEntryID'),(1, 'lpEntryID'),(1, 'lpInterface'),(1, 'ulFlags'),(1, 'lpulObjType'),(1, 'lppUnk'),)))
    IMAPIContainer.SetSearchCriteria = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.SRestriction_head),POINTER(win32more.System.AddressBook.SBinaryArray_head),UInt32, use_last_error=False)(17, 'SetSearchCriteria', ((1, 'lpRestriction'),(1, 'lpContainerList'),(1, 'ulSearchFlags'),)))
    IMAPIContainer.GetSearchCriteria = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.System.AddressBook.SRestriction_head)),POINTER(POINTER(win32more.System.AddressBook.SBinaryArray_head)),POINTER(UInt32), use_last_error=False)(18, 'GetSearchCriteria', ((1, 'ulFlags'),(1, 'lppRestriction'),(1, 'lppContainerList'),(1, 'lpulSearchState'),)))
    return IMAPIContainer
def _define__flaglist_head():
    class _flaglist(Structure):
        pass
    return _flaglist
def _define__flaglist():
    _flaglist = win32more.System.AddressBook._flaglist_head
    _flaglist._fields_ = [
        ("cFlags", UInt32),
        ("ulFlag", UInt32 * 0),
    ]
    return _flaglist
def _define_IABContainer_head():
    class IABContainer(win32more.System.AddressBook.IMAPIContainer_head):
        Guid = Guid(None)
    return IABContainer
def _define_IABContainer():
    IABContainer = win32more.System.AddressBook.IABContainer_head
    IABContainer.CreateEntry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.ENTRYID_head),UInt32,POINTER(win32more.System.AddressBook.IMAPIProp_head), use_last_error=False)(19, 'CreateEntry', ((1, 'cbEntryID'),(1, 'lpEntryID'),(1, 'ulCreateFlags'),(1, 'lppMAPIPropEntry'),)))
    IABContainer.CopyEntries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.SBinaryArray_head),UIntPtr,win32more.System.AddressBook.IMAPIProgress_head,UInt32, use_last_error=False)(20, 'CopyEntries', ((1, 'lpEntries'),(1, 'ulUIParam'),(1, 'lpProgress'),(1, 'ulFlags'),)))
    IABContainer.DeleteEntries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.SBinaryArray_head),UInt32, use_last_error=False)(21, 'DeleteEntries', ((1, 'lpEntries'),(1, 'ulFlags'),)))
    IABContainer.ResolveNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.SPropTagArray_head),UInt32,POINTER(win32more.System.AddressBook.ADRLIST_head),POINTER(win32more.System.AddressBook._flaglist_head), use_last_error=False)(22, 'ResolveNames', ((1, 'lpPropTagArray'),(1, 'ulFlags'),(1, 'lpAdrList'),(1, 'lpFlagList'),)))
    return IABContainer
def _define_IMailUser_head():
    class IMailUser(win32more.System.AddressBook.IMAPIProp_head):
        Guid = Guid(None)
    return IMailUser
def _define_IMailUser():
    IMailUser = win32more.System.AddressBook.IMailUser_head
    return IMailUser
def _define_IDistList_head():
    class IDistList(win32more.System.AddressBook.IMAPIContainer_head):
        Guid = Guid(None)
    return IDistList
def _define_IDistList():
    IDistList = win32more.System.AddressBook.IDistList_head
    IDistList.CreateEntry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.ENTRYID_head),UInt32,POINTER(win32more.System.AddressBook.IMAPIProp_head), use_last_error=False)(19, 'CreateEntry', ((1, 'cbEntryID'),(1, 'lpEntryID'),(1, 'ulCreateFlags'),(1, 'lppMAPIPropEntry'),)))
    IDistList.CopyEntries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.SBinaryArray_head),UIntPtr,win32more.System.AddressBook.IMAPIProgress_head,UInt32, use_last_error=False)(20, 'CopyEntries', ((1, 'lpEntries'),(1, 'ulUIParam'),(1, 'lpProgress'),(1, 'ulFlags'),)))
    IDistList.DeleteEntries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.SBinaryArray_head),UInt32, use_last_error=False)(21, 'DeleteEntries', ((1, 'lpEntries'),(1, 'ulFlags'),)))
    IDistList.ResolveNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.SPropTagArray_head),UInt32,POINTER(win32more.System.AddressBook.ADRLIST_head),POINTER(win32more.System.AddressBook._flaglist_head), use_last_error=False)(22, 'ResolveNames', ((1, 'lpPropTagArray'),(1, 'ulFlags'),(1, 'lpAdrList'),(1, 'lpFlagList'),)))
    return IDistList
def _define_IMAPIFolder_head():
    class IMAPIFolder(win32more.System.AddressBook.IMAPIContainer_head):
        Guid = Guid(None)
    return IMAPIFolder
def _define_IMAPIFolder():
    IMAPIFolder = win32more.System.AddressBook.IMAPIFolder_head
    IMAPIFolder.CreateMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(win32more.System.AddressBook.IMessage_head), use_last_error=False)(19, 'CreateMessage', ((1, 'lpInterface'),(1, 'ulFlags'),(1, 'lppMessage'),)))
    IMAPIFolder.CopyMessages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.SBinaryArray_head),POINTER(Guid),c_void_p,UIntPtr,win32more.System.AddressBook.IMAPIProgress_head,UInt32, use_last_error=False)(20, 'CopyMessages', ((1, 'lpMsgList'),(1, 'lpInterface'),(1, 'lpDestFolder'),(1, 'ulUIParam'),(1, 'lpProgress'),(1, 'ulFlags'),)))
    IMAPIFolder.DeleteMessages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.SBinaryArray_head),UIntPtr,win32more.System.AddressBook.IMAPIProgress_head,UInt32, use_last_error=False)(21, 'DeleteMessages', ((1, 'lpMsgList'),(1, 'ulUIParam'),(1, 'lpProgress'),(1, 'ulFlags'),)))
    IMAPIFolder.CreateFolder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(SByte),POINTER(SByte),POINTER(Guid),UInt32,POINTER(win32more.System.AddressBook.IMAPIFolder_head), use_last_error=False)(22, 'CreateFolder', ((1, 'ulFolderType'),(1, 'lpszFolderName'),(1, 'lpszFolderComment'),(1, 'lpInterface'),(1, 'ulFlags'),(1, 'lppFolder'),)))
    IMAPIFolder.CopyFolder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.ENTRYID_head),POINTER(Guid),c_void_p,POINTER(SByte),UIntPtr,win32more.System.AddressBook.IMAPIProgress_head,UInt32, use_last_error=False)(23, 'CopyFolder', ((1, 'cbEntryID'),(1, 'lpEntryID'),(1, 'lpInterface'),(1, 'lpDestFolder'),(1, 'lpszNewFolderName'),(1, 'ulUIParam'),(1, 'lpProgress'),(1, 'ulFlags'),)))
    IMAPIFolder.DeleteFolder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.ENTRYID_head),UIntPtr,win32more.System.AddressBook.IMAPIProgress_head,UInt32, use_last_error=False)(24, 'DeleteFolder', ((1, 'cbEntryID'),(1, 'lpEntryID'),(1, 'ulUIParam'),(1, 'lpProgress'),(1, 'ulFlags'),)))
    IMAPIFolder.SetReadFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.SBinaryArray_head),UIntPtr,win32more.System.AddressBook.IMAPIProgress_head,UInt32, use_last_error=False)(25, 'SetReadFlags', ((1, 'lpMsgList'),(1, 'ulUIParam'),(1, 'lpProgress'),(1, 'ulFlags'),)))
    IMAPIFolder.GetMessageStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.ENTRYID_head),UInt32,POINTER(UInt32), use_last_error=False)(26, 'GetMessageStatus', ((1, 'cbEntryID'),(1, 'lpEntryID'),(1, 'ulFlags'),(1, 'lpulMessageStatus'),)))
    IMAPIFolder.SetMessageStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.ENTRYID_head),UInt32,UInt32,POINTER(UInt32), use_last_error=False)(27, 'SetMessageStatus', ((1, 'cbEntryID'),(1, 'lpEntryID'),(1, 'ulNewStatus'),(1, 'ulNewStatusMask'),(1, 'lpulOldStatus'),)))
    IMAPIFolder.SaveContentsSort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.SSortOrderSet_head),UInt32, use_last_error=False)(28, 'SaveContentsSort', ((1, 'lpSortCriteria'),(1, 'ulFlags'),)))
    IMAPIFolder.EmptyFolder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,win32more.System.AddressBook.IMAPIProgress_head,UInt32, use_last_error=False)(29, 'EmptyFolder', ((1, 'ulUIParam'),(1, 'lpProgress'),(1, 'ulFlags'),)))
    return IMAPIFolder
def _define_IMsgStore_head():
    class IMsgStore(win32more.System.AddressBook.IMAPIProp_head):
        Guid = Guid(None)
    return IMsgStore
def _define_IMsgStore():
    IMsgStore = win32more.System.AddressBook.IMsgStore_head
    IMsgStore.Advise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.ENTRYID_head),UInt32,win32more.System.AddressBook.IMAPIAdviseSink_head,POINTER(UInt32), use_last_error=False)(14, 'Advise', ((1, 'cbEntryID'),(1, 'lpEntryID'),(1, 'ulEventMask'),(1, 'lpAdviseSink'),(1, 'lpulConnection'),)))
    IMsgStore.Unadvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(15, 'Unadvise', ((1, 'ulConnection'),)))
    IMsgStore.CompareEntryIDs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.ENTRYID_head),UInt32,POINTER(win32more.System.AddressBook.ENTRYID_head),UInt32,POINTER(UInt32), use_last_error=False)(16, 'CompareEntryIDs', ((1, 'cbEntryID1'),(1, 'lpEntryID1'),(1, 'cbEntryID2'),(1, 'lpEntryID2'),(1, 'ulFlags'),(1, 'lpulResult'),)))
    IMsgStore.OpenEntry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.ENTRYID_head),POINTER(Guid),UInt32,POINTER(UInt32),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(17, 'OpenEntry', ((1, 'cbEntryID'),(1, 'lpEntryID'),(1, 'lpInterface'),(1, 'ulFlags'),(1, 'lpulObjType'),(1, 'ppUnk'),)))
    IMsgStore.SetReceiveFolder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(SByte),UInt32,UInt32,POINTER(win32more.System.AddressBook.ENTRYID_head), use_last_error=False)(18, 'SetReceiveFolder', ((1, 'lpszMessageClass'),(1, 'ulFlags'),(1, 'cbEntryID'),(1, 'lpEntryID'),)))
    IMsgStore.GetReceiveFolder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(SByte),UInt32,POINTER(UInt32),POINTER(POINTER(win32more.System.AddressBook.ENTRYID_head)),POINTER(POINTER(SByte)), use_last_error=False)(19, 'GetReceiveFolder', ((1, 'lpszMessageClass'),(1, 'ulFlags'),(1, 'lpcbEntryID'),(1, 'lppEntryID'),(1, 'lppszExplicitClass'),)))
    IMsgStore.GetReceiveFolderTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.IMAPITable_head), use_last_error=False)(20, 'GetReceiveFolderTable', ((1, 'ulFlags'),(1, 'lppTable'),)))
    IMsgStore.StoreLogoff = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(21, 'StoreLogoff', ((1, 'lpulFlags'),)))
    IMsgStore.AbortSubmit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.ENTRYID_head),UInt32, use_last_error=False)(22, 'AbortSubmit', ((1, 'cbEntryID'),(1, 'lpEntryID'),(1, 'ulFlags'),)))
    IMsgStore.GetOutgoingQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.IMAPITable_head), use_last_error=False)(23, 'GetOutgoingQueue', ((1, 'ulFlags'),(1, 'lppTable'),)))
    IMsgStore.SetLockState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IMessage_head,UInt32, use_last_error=False)(24, 'SetLockState', ((1, 'lpMessage'),(1, 'ulLockState'),)))
    IMsgStore.FinishedMsg = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.System.AddressBook.ENTRYID_head), use_last_error=False)(25, 'FinishedMsg', ((1, 'ulFlags'),(1, 'cbEntryID'),(1, 'lpEntryID'),)))
    IMsgStore.NotifyNewMail = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.NOTIFICATION_head), use_last_error=False)(26, 'NotifyNewMail', ((1, 'lpNotification'),)))
    return IMsgStore
def _define_IMessage_head():
    class IMessage(win32more.System.AddressBook.IMAPIProp_head):
        Guid = Guid(None)
    return IMessage
def _define_IMessage():
    IMessage = win32more.System.AddressBook.IMessage_head
    IMessage.GetAttachmentTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.IMAPITable_head), use_last_error=False)(14, 'GetAttachmentTable', ((1, 'ulFlags'),(1, 'lppTable'),)))
    IMessage.OpenAttach = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),UInt32,POINTER(win32more.System.AddressBook.IAttach_head), use_last_error=False)(15, 'OpenAttach', ((1, 'ulAttachmentNum'),(1, 'lpInterface'),(1, 'ulFlags'),(1, 'lppAttach'),)))
    IMessage.CreateAttach = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(UInt32),POINTER(win32more.System.AddressBook.IAttach_head), use_last_error=False)(16, 'CreateAttach', ((1, 'lpInterface'),(1, 'ulFlags'),(1, 'lpulAttachmentNum'),(1, 'lppAttach'),)))
    IMessage.DeleteAttach = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UIntPtr,win32more.System.AddressBook.IMAPIProgress_head,UInt32, use_last_error=False)(17, 'DeleteAttach', ((1, 'ulAttachmentNum'),(1, 'ulUIParam'),(1, 'lpProgress'),(1, 'ulFlags'),)))
    IMessage.GetRecipientTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.IMAPITable_head), use_last_error=False)(18, 'GetRecipientTable', ((1, 'ulFlags'),(1, 'lppTable'),)))
    IMessage.ModifyRecipients = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.ADRLIST_head), use_last_error=False)(19, 'ModifyRecipients', ((1, 'ulFlags'),(1, 'lpMods'),)))
    IMessage.SubmitMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(20, 'SubmitMessage', ((1, 'ulFlags'),)))
    IMessage.SetReadFlag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(21, 'SetReadFlag', ((1, 'ulFlags'),)))
    return IMessage
def _define_IAttach_head():
    class IAttach(win32more.System.AddressBook.IMAPIProp_head):
        Guid = Guid(None)
    return IAttach
def _define_IAttach():
    IAttach = win32more.System.AddressBook.IAttach_head
    return IAttach
def _define_LPFNABSDI():
    return CFUNCTYPE(win32more.Foundation.BOOL,UIntPtr,c_void_p, use_last_error=False)
def _define_LPFNDISMISS():
    return CFUNCTYPE(Void,UIntPtr,c_void_p, use_last_error=False)
def _define_LPFNBUTTON():
    return CFUNCTYPE(Int32,UIntPtr,c_void_p,UInt32,POINTER(win32more.System.AddressBook.ENTRYID_head),UInt32, use_last_error=False)
def _define_ADRPARM_head():
    class ADRPARM(Structure):
        pass
    return ADRPARM
def _define_ADRPARM():
    ADRPARM = win32more.System.AddressBook.ADRPARM_head
    ADRPARM._fields_ = [
        ("cbABContEntryID", UInt32),
        ("lpABContEntryID", POINTER(win32more.System.AddressBook.ENTRYID_head)),
        ("ulFlags", UInt32),
        ("lpReserved", c_void_p),
        ("ulHelpContext", UInt32),
        ("lpszHelpFileName", POINTER(SByte)),
        ("lpfnABSDI", win32more.System.AddressBook.LPFNABSDI),
        ("lpfnDismiss", win32more.System.AddressBook.LPFNDISMISS),
        ("lpvDismissContext", c_void_p),
        ("lpszCaption", POINTER(SByte)),
        ("lpszNewEntryTitle", POINTER(SByte)),
        ("lpszDestWellsTitle", POINTER(SByte)),
        ("cDestFields", UInt32),
        ("nDestFieldFocus", UInt32),
        ("lppszDestTitles", POINTER(POINTER(SByte))),
        ("lpulDestComps", POINTER(UInt32)),
        ("lpContRestriction", POINTER(win32more.System.AddressBook.SRestriction_head)),
        ("lpHierRestriction", POINTER(win32more.System.AddressBook.SRestriction_head)),
    ]
    return ADRPARM
def _define_IMAPIControl_head():
    class IMAPIControl(win32more.System.Com.IUnknown_head):
        Guid = Guid(None)
    return IMAPIControl
def _define_IMAPIControl():
    IMAPIControl = win32more.System.AddressBook.IMAPIControl_head
    IMAPIControl.GetLastError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.System.AddressBook.MAPIERROR_head)), use_last_error=False)(3, 'GetLastError', ((1, 'hResult'),(1, 'ulFlags'),(1, 'lppMAPIError'),)))
    IMAPIControl.Activate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UIntPtr, use_last_error=False)(4, 'Activate', ((1, 'ulFlags'),(1, 'ulUIParam'),)))
    IMAPIControl.GetState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(5, 'GetState', ((1, 'ulFlags'),(1, 'lpulState'),)))
    return IMAPIControl
def _define_DTBLLABEL_head():
    class DTBLLABEL(Structure):
        pass
    return DTBLLABEL
def _define_DTBLLABEL():
    DTBLLABEL = win32more.System.AddressBook.DTBLLABEL_head
    DTBLLABEL._fields_ = [
        ("ulbLpszLabelName", UInt32),
        ("ulFlags", UInt32),
    ]
    return DTBLLABEL
def _define_DTBLEDIT_head():
    class DTBLEDIT(Structure):
        pass
    return DTBLEDIT
def _define_DTBLEDIT():
    DTBLEDIT = win32more.System.AddressBook.DTBLEDIT_head
    DTBLEDIT._fields_ = [
        ("ulbLpszCharsAllowed", UInt32),
        ("ulFlags", UInt32),
        ("ulNumCharsAllowed", UInt32),
        ("ulPropTag", UInt32),
    ]
    return DTBLEDIT
def _define_DTBLLBX_head():
    class DTBLLBX(Structure):
        pass
    return DTBLLBX
def _define_DTBLLBX():
    DTBLLBX = win32more.System.AddressBook.DTBLLBX_head
    DTBLLBX._fields_ = [
        ("ulFlags", UInt32),
        ("ulPRSetProperty", UInt32),
        ("ulPRTableName", UInt32),
    ]
    return DTBLLBX
def _define_DTBLCOMBOBOX_head():
    class DTBLCOMBOBOX(Structure):
        pass
    return DTBLCOMBOBOX
def _define_DTBLCOMBOBOX():
    DTBLCOMBOBOX = win32more.System.AddressBook.DTBLCOMBOBOX_head
    DTBLCOMBOBOX._fields_ = [
        ("ulbLpszCharsAllowed", UInt32),
        ("ulFlags", UInt32),
        ("ulNumCharsAllowed", UInt32),
        ("ulPRPropertyName", UInt32),
        ("ulPRTableName", UInt32),
    ]
    return DTBLCOMBOBOX
def _define_DTBLDDLBX_head():
    class DTBLDDLBX(Structure):
        pass
    return DTBLDDLBX
def _define_DTBLDDLBX():
    DTBLDDLBX = win32more.System.AddressBook.DTBLDDLBX_head
    DTBLDDLBX._fields_ = [
        ("ulFlags", UInt32),
        ("ulPRDisplayProperty", UInt32),
        ("ulPRSetProperty", UInt32),
        ("ulPRTableName", UInt32),
    ]
    return DTBLDDLBX
def _define_DTBLCHECKBOX_head():
    class DTBLCHECKBOX(Structure):
        pass
    return DTBLCHECKBOX
def _define_DTBLCHECKBOX():
    DTBLCHECKBOX = win32more.System.AddressBook.DTBLCHECKBOX_head
    DTBLCHECKBOX._fields_ = [
        ("ulbLpszLabel", UInt32),
        ("ulFlags", UInt32),
        ("ulPRPropertyName", UInt32),
    ]
    return DTBLCHECKBOX
def _define_DTBLGROUPBOX_head():
    class DTBLGROUPBOX(Structure):
        pass
    return DTBLGROUPBOX
def _define_DTBLGROUPBOX():
    DTBLGROUPBOX = win32more.System.AddressBook.DTBLGROUPBOX_head
    DTBLGROUPBOX._fields_ = [
        ("ulbLpszLabel", UInt32),
        ("ulFlags", UInt32),
    ]
    return DTBLGROUPBOX
def _define_DTBLBUTTON_head():
    class DTBLBUTTON(Structure):
        pass
    return DTBLBUTTON
def _define_DTBLBUTTON():
    DTBLBUTTON = win32more.System.AddressBook.DTBLBUTTON_head
    DTBLBUTTON._fields_ = [
        ("ulbLpszLabel", UInt32),
        ("ulFlags", UInt32),
        ("ulPRControl", UInt32),
    ]
    return DTBLBUTTON
def _define_DTBLPAGE_head():
    class DTBLPAGE(Structure):
        pass
    return DTBLPAGE
def _define_DTBLPAGE():
    DTBLPAGE = win32more.System.AddressBook.DTBLPAGE_head
    DTBLPAGE._fields_ = [
        ("ulbLpszLabel", UInt32),
        ("ulFlags", UInt32),
        ("ulbLpszComponent", UInt32),
        ("ulContext", UInt32),
    ]
    return DTBLPAGE
def _define_DTBLRADIOBUTTON_head():
    class DTBLRADIOBUTTON(Structure):
        pass
    return DTBLRADIOBUTTON
def _define_DTBLRADIOBUTTON():
    DTBLRADIOBUTTON = win32more.System.AddressBook.DTBLRADIOBUTTON_head
    DTBLRADIOBUTTON._fields_ = [
        ("ulbLpszLabel", UInt32),
        ("ulFlags", UInt32),
        ("ulcButtons", UInt32),
        ("ulPropTag", UInt32),
        ("lReturnValue", Int32),
    ]
    return DTBLRADIOBUTTON
def _define_DTBLMVLISTBOX_head():
    class DTBLMVLISTBOX(Structure):
        pass
    return DTBLMVLISTBOX
def _define_DTBLMVLISTBOX():
    DTBLMVLISTBOX = win32more.System.AddressBook.DTBLMVLISTBOX_head
    DTBLMVLISTBOX._fields_ = [
        ("ulFlags", UInt32),
        ("ulMVPropTag", UInt32),
    ]
    return DTBLMVLISTBOX
def _define_DTBLMVDDLBX_head():
    class DTBLMVDDLBX(Structure):
        pass
    return DTBLMVDDLBX
def _define_DTBLMVDDLBX():
    DTBLMVDDLBX = win32more.System.AddressBook.DTBLMVDDLBX_head
    DTBLMVDDLBX._fields_ = [
        ("ulFlags", UInt32),
        ("ulMVPropTag", UInt32),
    ]
    return DTBLMVDDLBX
def _define_IProviderAdmin_head():
    class IProviderAdmin(win32more.System.Com.IUnknown_head):
        Guid = Guid(None)
    return IProviderAdmin
def _define_IProviderAdmin():
    IProviderAdmin = win32more.System.AddressBook.IProviderAdmin_head
    IProviderAdmin.GetLastError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.System.AddressBook.MAPIERROR_head)), use_last_error=False)(3, 'GetLastError', ((1, 'hResult'),(1, 'ulFlags'),(1, 'lppMAPIError'),)))
    IProviderAdmin.GetProviderTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.IMAPITable_head), use_last_error=False)(4, 'GetProviderTable', ((1, 'ulFlags'),(1, 'lppTable'),)))
    IProviderAdmin.CreateProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(SByte),UInt32,POINTER(win32more.System.AddressBook.SPropValue),UIntPtr,UInt32,POINTER(win32more.System.AddressBook.MAPIUID_head), use_last_error=False)(5, 'CreateProvider', ((1, 'lpszProvider'),(1, 'cValues'),(1, 'lpProps'),(1, 'ulUIParam'),(1, 'ulFlags'),(1, 'lpUID'),)))
    IProviderAdmin.DeleteProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.MAPIUID_head), use_last_error=False)(6, 'DeleteProvider', ((1, 'lpUID'),)))
    IProviderAdmin.OpenProfileSection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.MAPIUID_head),POINTER(Guid),UInt32,POINTER(win32more.System.AddressBook.IProfSect_head), use_last_error=False)(7, 'OpenProfileSection', ((1, 'lpUID'),(1, 'lpInterface'),(1, 'ulFlags'),(1, 'lppProfSect'),)))
    return IProviderAdmin
Gender = Int32
Gender_genderUnspecified = 0
Gender_genderFemale = 1
Gender_genderMale = 2
def _define_CALLERRELEASE():
    return CFUNCTYPE(Void,UInt32,win32more.System.AddressBook.ITableData_head,win32more.System.AddressBook.IMAPITable_head, use_last_error=False)
def _define_ITableData_head():
    class ITableData(win32more.System.Com.IUnknown_head):
        Guid = Guid(None)
    return ITableData
def _define_ITableData():
    ITableData = win32more.System.AddressBook.ITableData_head
    ITableData.HrGetView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.SSortOrderSet_head),POINTER(win32more.System.AddressBook.CALLERRELEASE),UInt32,POINTER(win32more.System.AddressBook.IMAPITable_head), use_last_error=False)(3, 'HrGetView', ((1, 'lpSSortOrderSet'),(1, 'lpfCallerRelease'),(1, 'ulCallerData'),(1, 'lppMAPITable'),)))
    ITableData.HrModifyRow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.SRow_head), use_last_error=False)(4, 'HrModifyRow', ((1, 'param0'),)))
    ITableData.HrDeleteRow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.SPropValue_head), use_last_error=False)(5, 'HrDeleteRow', ((1, 'lpSPropValue'),)))
    ITableData.HrQueryRow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.SPropValue_head),POINTER(POINTER(win32more.System.AddressBook.SRow_head)),POINTER(UInt32), use_last_error=False)(6, 'HrQueryRow', ((1, 'lpsPropValue'),(1, 'lppSRow'),(1, 'lpuliRow'),)))
    ITableData.HrEnumRow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.System.AddressBook.SRow_head)), use_last_error=False)(7, 'HrEnumRow', ((1, 'ulRowNumber'),(1, 'lppSRow'),)))
    ITableData.HrNotify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.System.AddressBook.SPropValue_head), use_last_error=False)(8, 'HrNotify', ((1, 'ulFlags'),(1, 'cValues'),(1, 'lpSPropValue'),)))
    ITableData.HrInsertRow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.SRow_head), use_last_error=False)(9, 'HrInsertRow', ((1, 'uliRow'),(1, 'lpSRow'),)))
    ITableData.HrModifyRows = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.SRowSet_head), use_last_error=False)(10, 'HrModifyRows', ((1, 'ulFlags'),(1, 'lpSRowSet'),)))
    ITableData.HrDeleteRows = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.SRowSet_head),POINTER(UInt32), use_last_error=False)(11, 'HrDeleteRows', ((1, 'ulFlags'),(1, 'lprowsetToDelete'),(1, 'cRowsDeleted'),)))
    return ITableData
def _define_IPropData_head():
    class IPropData(win32more.System.AddressBook.IMAPIProp_head):
        Guid = Guid(None)
    return IPropData
def _define_IPropData():
    IPropData = win32more.System.AddressBook.IPropData_head
    IPropData.HrSetObjAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(14, 'HrSetObjAccess', ((1, 'ulAccess'),)))
    IPropData.HrSetPropAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.SPropTagArray_head),POINTER(UInt32), use_last_error=False)(15, 'HrSetPropAccess', ((1, 'lpPropTagArray'),(1, 'rgulAccess'),)))
    IPropData.HrGetPropAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.AddressBook.SPropTagArray_head)),POINTER(POINTER(UInt32)), use_last_error=False)(16, 'HrGetPropAccess', ((1, 'lppPropTagArray'),(1, 'lprgulAccess'),)))
    IPropData.HrAddObjProps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.SPropTagArray_head),POINTER(POINTER(win32more.System.AddressBook.SPropProblemArray_head)), use_last_error=False)(17, 'HrAddObjProps', ((1, 'lppPropTagArray'),(1, 'lprgulAccess'),)))
    return IPropData
def _define_FNIDLE():
    return CFUNCTYPE(win32more.Foundation.BOOL,c_void_p, use_last_error=False)
def _define_PFNIDLE():
    return CFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)
def _define_LPOPENSTREAMONFILE():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.LPALLOCATEBUFFER,win32more.System.AddressBook.LPFREEBUFFER,UInt32,POINTER(SByte),POINTER(SByte),POINTER(win32more.System.Com.IStream_head), use_last_error=False)
def _define_DTCTL_head():
    class DTCTL(Structure):
        pass
    return DTCTL
def _define_DTCTL():
    DTCTL = win32more.System.AddressBook.DTCTL_head
    class DTCTL__ctl_e__Union(Union):
        pass
    DTCTL__ctl_e__Union._fields_ = [
        ("lpv", c_void_p),
        ("lplabel", POINTER(win32more.System.AddressBook.DTBLLABEL_head)),
        ("lpedit", POINTER(win32more.System.AddressBook.DTBLEDIT_head)),
        ("lplbx", POINTER(win32more.System.AddressBook.DTBLLBX_head)),
        ("lpcombobox", POINTER(win32more.System.AddressBook.DTBLCOMBOBOX_head)),
        ("lpddlbx", POINTER(win32more.System.AddressBook.DTBLDDLBX_head)),
        ("lpcheckbox", POINTER(win32more.System.AddressBook.DTBLCHECKBOX_head)),
        ("lpgroupbox", POINTER(win32more.System.AddressBook.DTBLGROUPBOX_head)),
        ("lpbutton", POINTER(win32more.System.AddressBook.DTBLBUTTON_head)),
        ("lpradiobutton", POINTER(win32more.System.AddressBook.DTBLRADIOBUTTON_head)),
        ("lpmvlbx", POINTER(win32more.System.AddressBook.DTBLMVLISTBOX_head)),
        ("lpmvddlbx", POINTER(win32more.System.AddressBook.DTBLMVDDLBX_head)),
        ("lppage", POINTER(win32more.System.AddressBook.DTBLPAGE_head)),
    ]
    DTCTL._fields_ = [
        ("ulCtlType", UInt32),
        ("ulCtlFlags", UInt32),
        ("lpbNotif", c_char_p_no),
        ("cbNotif", UInt32),
        ("lpszFilter", POINTER(SByte)),
        ("ulItemID", UInt32),
        ("ctl", DTCTL__ctl_e__Union),
    ]
    return DTCTL
def _define_DTPAGE_head():
    class DTPAGE(Structure):
        pass
    return DTPAGE
def _define_DTPAGE():
    DTPAGE = win32more.System.AddressBook.DTPAGE_head
    class DTPAGE__Anonymous_e__Union(Union):
        pass
    DTPAGE__Anonymous_e__Union._fields_ = [
        ("lpszComponent", POINTER(SByte)),
        ("ulItemID", UInt32),
    ]
    DTPAGE._anonymous_ = [
        'Anonymous',
    ]
    DTPAGE._fields_ = [
        ("cctl", UInt32),
        ("lpszResourceName", POINTER(SByte)),
        ("Anonymous", DTPAGE__Anonymous_e__Union),
        ("lpctl", POINTER(win32more.System.AddressBook.DTCTL_head)),
    ]
    return DTPAGE
def _define_LPDISPATCHNOTIFICATIONS():
    return CFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)
def _define_LPCREATECONVERSATIONINDEX():
    return CFUNCTYPE(Int32,UInt32,c_char_p_no,POINTER(UInt32),POINTER(c_char_p_no), use_last_error=False)
def _define_IAddrBook_head():
    class IAddrBook(win32more.System.AddressBook.IMAPIProp_head):
        Guid = Guid(None)
    return IAddrBook
def _define_IAddrBook():
    IAddrBook = win32more.System.AddressBook.IAddrBook_head
    IAddrBook.OpenEntry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.ENTRYID_head),POINTER(Guid),UInt32,POINTER(UInt32),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(14, 'OpenEntry', ((1, 'cbEntryID'),(1, 'lpEntryID'),(1, 'lpInterface'),(1, 'ulFlags'),(1, 'lpulObjType'),(1, 'lppUnk'),)))
    IAddrBook.CompareEntryIDs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.ENTRYID_head),UInt32,POINTER(win32more.System.AddressBook.ENTRYID_head),UInt32,POINTER(UInt32), use_last_error=False)(15, 'CompareEntryIDs', ((1, 'cbEntryID1'),(1, 'lpEntryID1'),(1, 'cbEntryID2'),(1, 'lpEntryID2'),(1, 'ulFlags'),(1, 'lpulResult'),)))
    IAddrBook.Advise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.ENTRYID_head),UInt32,win32more.System.AddressBook.IMAPIAdviseSink_head,POINTER(UInt32), use_last_error=False)(16, 'Advise', ((1, 'cbEntryID'),(1, 'lpEntryID'),(1, 'ulEventMask'),(1, 'lpAdviseSink'),(1, 'lpulConnection'),)))
    IAddrBook.Unadvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(17, 'Unadvise', ((1, 'ulConnection'),)))
    IAddrBook.CreateOneOff = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(SByte),POINTER(SByte),POINTER(SByte),UInt32,POINTER(UInt32),POINTER(POINTER(win32more.System.AddressBook.ENTRYID_head)), use_last_error=False)(18, 'CreateOneOff', ((1, 'lpszName'),(1, 'lpszAdrType'),(1, 'lpszAddress'),(1, 'ulFlags'),(1, 'lpcbEntryID'),(1, 'lppEntryID'),)))
    IAddrBook.NewEntry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,POINTER(win32more.System.AddressBook.ENTRYID_head),UInt32,POINTER(win32more.System.AddressBook.ENTRYID_head),POINTER(UInt32),POINTER(POINTER(win32more.System.AddressBook.ENTRYID_head)), use_last_error=False)(19, 'NewEntry', ((1, 'ulUIParam'),(1, 'ulFlags'),(1, 'cbEIDContainer'),(1, 'lpEIDContainer'),(1, 'cbEIDNewEntryTpl'),(1, 'lpEIDNewEntryTpl'),(1, 'lpcbEIDNewEntry'),(1, 'lppEIDNewEntry'),)))
    IAddrBook.ResolveName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,UInt32,POINTER(SByte),POINTER(win32more.System.AddressBook.ADRLIST_head), use_last_error=False)(20, 'ResolveName', ((1, 'ulUIParam'),(1, 'ulFlags'),(1, 'lpszNewEntryTitle'),(1, 'lpAdrList'),)))
    IAddrBook.Address = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.System.AddressBook.ADRPARM_head),POINTER(POINTER(win32more.System.AddressBook.ADRLIST_head)), use_last_error=False)(21, 'Address', ((1, 'lpulUIParam'),(1, 'lpAdrParms'),(1, 'lppAdrList'),)))
    IAddrBook.Details = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UIntPtr),win32more.System.AddressBook.LPFNDISMISS,c_void_p,UInt32,POINTER(win32more.System.AddressBook.ENTRYID_head),win32more.System.AddressBook.LPFNBUTTON,c_void_p,POINTER(SByte),UInt32, use_last_error=False)(22, 'Details', ((1, 'lpulUIParam'),(1, 'lpfnDismiss'),(1, 'lpvDismissContext'),(1, 'cbEntryID'),(1, 'lpEntryID'),(1, 'lpfButtonCallback'),(1, 'lpvButtonContext'),(1, 'lpszButtonText'),(1, 'ulFlags'),)))
    IAddrBook.RecipOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.System.AddressBook.ADRENTRY_head), use_last_error=False)(23, 'RecipOptions', ((1, 'ulUIParam'),(1, 'ulFlags'),(1, 'lpRecip'),)))
    IAddrBook.QueryDefaultRecipOpt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(SByte),UInt32,POINTER(UInt32),POINTER(POINTER(win32more.System.AddressBook.SPropValue_head)), use_last_error=False)(24, 'QueryDefaultRecipOpt', ((1, 'lpszAdrType'),(1, 'ulFlags'),(1, 'lpcValues'),(1, 'lppOptions'),)))
    IAddrBook.GetPAB = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(win32more.System.AddressBook.ENTRYID_head)), use_last_error=False)(25, 'GetPAB', ((1, 'lpcbEntryID'),(1, 'lppEntryID'),)))
    IAddrBook.SetPAB = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.ENTRYID_head), use_last_error=False)(26, 'SetPAB', ((1, 'cbEntryID'),(1, 'lpEntryID'),)))
    IAddrBook.GetDefaultDir = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(win32more.System.AddressBook.ENTRYID_head)), use_last_error=False)(27, 'GetDefaultDir', ((1, 'lpcbEntryID'),(1, 'lppEntryID'),)))
    IAddrBook.SetDefaultDir = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.ENTRYID_head), use_last_error=False)(28, 'SetDefaultDir', ((1, 'cbEntryID'),(1, 'lpEntryID'),)))
    IAddrBook.GetSearchPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.System.AddressBook.SRowSet_head)), use_last_error=False)(29, 'GetSearchPath', ((1, 'ulFlags'),(1, 'lppSearchPath'),)))
    IAddrBook.SetSearchPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.SRowSet_head), use_last_error=False)(30, 'SetSearchPath', ((1, 'ulFlags'),(1, 'lpSearchPath'),)))
    IAddrBook.PrepareRecips = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.AddressBook.SPropTagArray_head),POINTER(win32more.System.AddressBook.ADRLIST_head), use_last_error=False)(31, 'PrepareRecips', ((1, 'ulFlags'),(1, 'lpPropTagArray'),(1, 'lpRecipList'),)))
    return IAddrBook
def _define__WABACTIONITEM_head():
    class _WABACTIONITEM(Structure):
        pass
    return _WABACTIONITEM
def _define__WABACTIONITEM():
    _WABACTIONITEM = win32more.System.AddressBook._WABACTIONITEM_head
    return _WABACTIONITEM
def _define_IWABObject_head():
    class IWABObject(win32more.System.Com.IUnknown_head):
        Guid = Guid(None)
    return IWABObject
def _define_IWABObject():
    IWABObject = win32more.System.AddressBook.IWABObject_head
    IWABObject.GetLastError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.System.AddressBook.MAPIERROR_head)), use_last_error=False)(3, 'GetLastError', ((1, 'hResult'),(1, 'ulFlags'),(1, 'lppMAPIError'),)))
    IWABObject.AllocateBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(c_void_p), use_last_error=False)(4, 'AllocateBuffer', ((1, 'cbSize'),(1, 'lppBuffer'),)))
    IWABObject.AllocateMore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,POINTER(c_void_p), use_last_error=False)(5, 'AllocateMore', ((1, 'cbSize'),(1, 'lpObject'),(1, 'lppBuffer'),)))
    IWABObject.FreeBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(6, 'FreeBuffer', ((1, 'lpBuffer'),)))
    IWABObject.Backup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR, use_last_error=False)(7, 'Backup', ((1, 'lpFileName'),)))
    IWABObject.Import = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR, use_last_error=False)(8, 'Import', ((1, 'lpWIP'),)))
    IWABObject.Find = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IAddrBook_head,win32more.Foundation.HWND, use_last_error=False)(9, 'Find', ((1, 'lpIAB'),(1, 'hWnd'),)))
    IWABObject.VCardDisplay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IAddrBook_head,win32more.Foundation.HWND,win32more.Foundation.PSTR, use_last_error=False)(10, 'VCardDisplay', ((1, 'lpIAB'),(1, 'hWnd'),(1, 'lpszFileName'),)))
    IWABObject.LDAPUrl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IAddrBook_head,win32more.Foundation.HWND,UInt32,win32more.Foundation.PSTR,POINTER(win32more.System.AddressBook.IMailUser_head), use_last_error=False)(11, 'LDAPUrl', ((1, 'lpIAB'),(1, 'hWnd'),(1, 'ulFlags'),(1, 'lpszURL'),(1, 'lppMailUser'),)))
    IWABObject.VCardCreate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IAddrBook_head,UInt32,win32more.Foundation.PSTR,win32more.System.AddressBook.IMailUser_head, use_last_error=False)(12, 'VCardCreate', ((1, 'lpIAB'),(1, 'ulFlags'),(1, 'lpszVCard'),(1, 'lpMailUser'),)))
    IWABObject.VCardRetrieve = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IAddrBook_head,UInt32,win32more.Foundation.PSTR,POINTER(win32more.System.AddressBook.IMailUser_head), use_last_error=False)(13, 'VCardRetrieve', ((1, 'lpIAB'),(1, 'ulFlags'),(1, 'lpszVCard'),(1, 'lppMailUser'),)))
    IWABObject.GetMe = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IAddrBook_head,UInt32,POINTER(UInt32),POINTER(win32more.System.AddressBook.SBinary_head),win32more.Foundation.HWND, use_last_error=False)(14, 'GetMe', ((1, 'lpIAB'),(1, 'ulFlags'),(1, 'lpdwAction'),(1, 'lpsbEID'),(1, 'hwnd'),)))
    IWABObject.SetMe = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IAddrBook_head,UInt32,win32more.System.AddressBook.SBinary,win32more.Foundation.HWND, use_last_error=False)(15, 'SetMe', ((1, 'lpIAB'),(1, 'ulFlags'),(1, 'sbEID'),(1, 'hwnd'),)))
    return IWABObject
def _define_IWABOBJECT_QueryInterface_METHOD():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)
def _define_IWABOBJECT_AddRef_METHOD():
    return CFUNCTYPE(UInt32, use_last_error=False)
def _define_IWABOBJECT_Release_METHOD():
    return CFUNCTYPE(UInt32, use_last_error=False)
def _define_IWABOBJECT_GetLastError_METHOD():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.System.AddressBook.MAPIERROR_head)), use_last_error=False)
def _define_IWABOBJECT_AllocateBuffer_METHOD():
    return CFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(c_void_p), use_last_error=False)
def _define_IWABOBJECT_AllocateMore_METHOD():
    return CFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,POINTER(c_void_p), use_last_error=False)
def _define_IWABOBJECT_FreeBuffer_METHOD():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)
def _define_IWABOBJECT_Backup_METHOD():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR, use_last_error=False)
def _define_IWABOBJECT_Import_METHOD():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR, use_last_error=False)
def _define_IWABOBJECT_Find_METHOD():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IAddrBook_head,win32more.Foundation.HWND, use_last_error=False)
def _define_IWABOBJECT_VCardDisplay_METHOD():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IAddrBook_head,win32more.Foundation.HWND,win32more.Foundation.PSTR, use_last_error=False)
def _define_IWABOBJECT_LDAPUrl_METHOD():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IAddrBook_head,win32more.Foundation.HWND,UInt32,win32more.Foundation.PSTR,POINTER(win32more.System.AddressBook.IMailUser_head), use_last_error=False)
def _define_IWABOBJECT_VCardCreate_METHOD():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IAddrBook_head,UInt32,win32more.Foundation.PSTR,win32more.System.AddressBook.IMailUser_head, use_last_error=False)
def _define_IWABOBJECT_VCardRetrieve_METHOD():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IAddrBook_head,UInt32,win32more.Foundation.PSTR,POINTER(win32more.System.AddressBook.IMailUser_head), use_last_error=False)
def _define_IWABOBJECT_GetMe_METHOD():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IAddrBook_head,UInt32,POINTER(UInt32),POINTER(win32more.System.AddressBook.SBinary_head),win32more.Foundation.HWND, use_last_error=False)
def _define_IWABOBJECT_SetMe_METHOD():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IAddrBook_head,UInt32,win32more.System.AddressBook.SBinary,win32more.Foundation.HWND, use_last_error=False)
def _define_IWABOBJECT__head():
    class IWABOBJECT_(c_void_p):
        Guid = Guid(None)
    return IWABOBJECT_
def _define_IWABOBJECT_():
    IWABOBJECT_ = win32more.System.AddressBook.IWABOBJECT__head
    IWABOBJECT_.QueryInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(0, 'QueryInterface', ((1, 'riid'),(1, 'ppvObj'),)))
    IWABOBJECT_.AddRef = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(1, 'AddRef', ()))
    IWABOBJECT_.Release = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(2, 'Release', ()))
    IWABOBJECT_.GetLastError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.System.AddressBook.MAPIERROR_head)), use_last_error=False)(3, 'GetLastError', ((1, 'hResult'),(1, 'ulFlags'),(1, 'lppMAPIError'),)))
    IWABOBJECT_.AllocateBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(c_void_p), use_last_error=False)(4, 'AllocateBuffer', ((1, 'cbSize'),(1, 'lppBuffer'),)))
    IWABOBJECT_.AllocateMore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,POINTER(c_void_p), use_last_error=False)(5, 'AllocateMore', ((1, 'cbSize'),(1, 'lpObject'),(1, 'lppBuffer'),)))
    IWABOBJECT_.FreeBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(6, 'FreeBuffer', ((1, 'lpBuffer'),)))
    IWABOBJECT_.Backup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR, use_last_error=False)(7, 'Backup', ((1, 'lpFileName'),)))
    IWABOBJECT_.Import = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR, use_last_error=False)(8, 'Import', ((1, 'lpWIP'),)))
    IWABOBJECT_.Find = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IAddrBook_head,win32more.Foundation.HWND, use_last_error=False)(9, 'Find', ((1, 'lpIAB'),(1, 'hWnd'),)))
    IWABOBJECT_.VCardDisplay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IAddrBook_head,win32more.Foundation.HWND,win32more.Foundation.PSTR, use_last_error=False)(10, 'VCardDisplay', ((1, 'lpIAB'),(1, 'hWnd'),(1, 'lpszFileName'),)))
    IWABOBJECT_.LDAPUrl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IAddrBook_head,win32more.Foundation.HWND,UInt32,win32more.Foundation.PSTR,POINTER(win32more.System.AddressBook.IMailUser_head), use_last_error=False)(11, 'LDAPUrl', ((1, 'lpIAB'),(1, 'hWnd'),(1, 'ulFlags'),(1, 'lpszURL'),(1, 'lppMailUser'),)))
    IWABOBJECT_.VCardCreate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IAddrBook_head,UInt32,win32more.Foundation.PSTR,win32more.System.AddressBook.IMailUser_head, use_last_error=False)(12, 'VCardCreate', ((1, 'lpIAB'),(1, 'ulFlags'),(1, 'lpszVCard'),(1, 'lpMailUser'),)))
    IWABOBJECT_.VCardRetrieve = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IAddrBook_head,UInt32,win32more.Foundation.PSTR,POINTER(win32more.System.AddressBook.IMailUser_head), use_last_error=False)(13, 'VCardRetrieve', ((1, 'lpIAB'),(1, 'ulFlags'),(1, 'lpszVCard'),(1, 'lppMailUser'),)))
    IWABOBJECT_.GetMe = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IAddrBook_head,UInt32,POINTER(UInt32),POINTER(win32more.System.AddressBook.SBinary_head),win32more.Foundation.HWND, use_last_error=False)(14, 'GetMe', ((1, 'lpIAB'),(1, 'ulFlags'),(1, 'lpdwAction'),(1, 'lpsbEID'),(1, 'hwnd'),)))
    IWABOBJECT_.SetMe = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IAddrBook_head,UInt32,win32more.System.AddressBook.SBinary,win32more.Foundation.HWND, use_last_error=False)(15, 'SetMe', ((1, 'lpIAB'),(1, 'ulFlags'),(1, 'sbEID'),(1, 'hwnd'),)))
    return IWABOBJECT_
def _define_WAB_PARAM_head():
    class WAB_PARAM(Structure):
        pass
    return WAB_PARAM
def _define_WAB_PARAM():
    WAB_PARAM = win32more.System.AddressBook.WAB_PARAM_head
    WAB_PARAM._fields_ = [
        ("cbSize", UInt32),
        ("hwnd", win32more.Foundation.HWND),
        ("szFileName", win32more.Foundation.PSTR),
        ("ulFlags", UInt32),
        ("guidPSExt", Guid),
    ]
    return WAB_PARAM
def _define_LPWABOPEN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.IAddrBook_head),POINTER(win32more.System.AddressBook.IWABObject_head),POINTER(win32more.System.AddressBook.WAB_PARAM_head),UInt32, use_last_error=False)
def _define_LPWABOPENEX():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.IAddrBook_head),POINTER(win32more.System.AddressBook.IWABObject_head),POINTER(win32more.System.AddressBook.WAB_PARAM_head),UInt32,win32more.System.AddressBook.LPALLOCATEBUFFER,win32more.System.AddressBook.LPALLOCATEMORE,win32more.System.AddressBook.LPFREEBUFFER, use_last_error=False)
def _define_WABIMPORTPARAM_head():
    class WABIMPORTPARAM(Structure):
        pass
    return WABIMPORTPARAM
def _define_WABIMPORTPARAM():
    WABIMPORTPARAM = win32more.System.AddressBook.WABIMPORTPARAM_head
    WABIMPORTPARAM._fields_ = [
        ("cbSize", UInt32),
        ("lpAdrBook", win32more.System.AddressBook.IAddrBook_head),
        ("hWnd", win32more.Foundation.HWND),
        ("ulFlags", UInt32),
        ("lpszFileName", win32more.Foundation.PSTR),
    ]
    return WABIMPORTPARAM
def _define_WABEXTDISPLAY_head():
    class WABEXTDISPLAY(Structure):
        pass
    return WABEXTDISPLAY
def _define_WABEXTDISPLAY():
    WABEXTDISPLAY = win32more.System.AddressBook.WABEXTDISPLAY_head
    WABEXTDISPLAY._fields_ = [
        ("cbSize", UInt32),
        ("lpWABObject", win32more.System.AddressBook.IWABObject_head),
        ("lpAdrBook", win32more.System.AddressBook.IAddrBook_head),
        ("lpPropObj", win32more.System.AddressBook.IMAPIProp_head),
        ("fReadOnly", win32more.Foundation.BOOL),
        ("fDataChanged", win32more.Foundation.BOOL),
        ("ulFlags", UInt32),
        ("lpv", c_void_p),
        ("lpsz", POINTER(SByte)),
    ]
    return WABEXTDISPLAY
def _define_IWABExtInit_head():
    class IWABExtInit(win32more.System.Com.IUnknown_head):
        Guid = Guid('ea22ebf0-87a4-11d1-9acf-00a0c91f9c8b')
    return IWABExtInit
def _define_IWABExtInit():
    IWABExtInit = win32more.System.AddressBook.IWABExtInit_head
    IWABExtInit.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AddressBook.WABEXTDISPLAY_head), use_last_error=False)(3, 'Initialize', ((1, 'lpWABExtDisplay'),)))
    return IWABExtInit
def _define_LPWABALLOCATEBUFFER():
    return CFUNCTYPE(Int32,win32more.System.AddressBook.IWABObject_head,UInt32,POINTER(c_void_p), use_last_error=False)
def _define_LPWABALLOCATEMORE():
    return CFUNCTYPE(Int32,win32more.System.AddressBook.IWABObject_head,UInt32,c_void_p,POINTER(c_void_p), use_last_error=False)
def _define_LPWABFREEBUFFER():
    return CFUNCTYPE(UInt32,win32more.System.AddressBook.IWABObject_head,c_void_p, use_last_error=False)
def _define_NOTIFKEY_head():
    class NOTIFKEY(Structure):
        pass
    return NOTIFKEY
def _define_NOTIFKEY():
    NOTIFKEY = win32more.System.AddressBook.NOTIFKEY_head
    NOTIFKEY._fields_ = [
        ("cb", UInt32),
        ("ab", Byte * 0),
    ]
    return NOTIFKEY
def _define_CreateTable():
    try:
        return WINFUNCTYPE(Int32,POINTER(Guid),win32more.System.AddressBook.LPALLOCATEBUFFER,win32more.System.AddressBook.LPALLOCATEMORE,win32more.System.AddressBook.LPFREEBUFFER,c_void_p,UInt32,UInt32,POINTER(win32more.System.AddressBook.SPropTagArray_head),POINTER(win32more.System.AddressBook.ITableData_head), use_last_error=False)(("CreateTable", windll["rtm"]), ((1, 'lpInterface'),(1, 'lpAllocateBuffer'),(1, 'lpAllocateMore'),(1, 'lpFreeBuffer'),(1, 'lpvReserved'),(1, 'ulTableType'),(1, 'ulPropTagIndexColumn'),(1, 'lpSPropTagArrayColumns'),(1, 'lppTableData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateIProp():
    try:
        return WINFUNCTYPE(Int32,POINTER(Guid),win32more.System.AddressBook.LPALLOCATEBUFFER,win32more.System.AddressBook.LPALLOCATEMORE,win32more.System.AddressBook.LPFREEBUFFER,c_void_p,POINTER(win32more.System.AddressBook.IPropData_head), use_last_error=False)(("CreateIProp", windll["MAPI32"]), ((1, 'lpInterface'),(1, 'lpAllocateBuffer'),(1, 'lpAllocateMore'),(1, 'lpFreeBuffer'),(1, 'lpvReserved'),(1, 'lppPropData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MAPIInitIdle():
    try:
        return WINFUNCTYPE(Int32,c_void_p, use_last_error=False)(("MAPIInitIdle", windll["MAPI32"]), ((1, 'lpvReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MAPIDeinitIdle():
    try:
        return WINFUNCTYPE(Void, use_last_error=False)(("MAPIDeinitIdle", windll["MAPI32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_FtgRegisterIdleRoutine():
    try:
        return WINFUNCTYPE(c_void_p,win32more.System.AddressBook.PFNIDLE,c_void_p,Int16,UInt32,UInt16, use_last_error=False)(("FtgRegisterIdleRoutine", windll["MAPI32"]), ((1, 'lpfnIdle'),(1, 'lpvIdleParam'),(1, 'priIdle'),(1, 'csecIdle'),(1, 'iroIdle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeregisterIdleRoutine():
    try:
        return WINFUNCTYPE(Void,c_void_p, use_last_error=False)(("DeregisterIdleRoutine", windll["MAPI32"]), ((1, 'ftg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnableIdleRoutine():
    try:
        return WINFUNCTYPE(Void,c_void_p,win32more.Foundation.BOOL, use_last_error=False)(("EnableIdleRoutine", windll["MAPI32"]), ((1, 'ftg'),(1, 'fEnable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ChangeIdleRoutine():
    try:
        return WINFUNCTYPE(Void,c_void_p,win32more.System.AddressBook.PFNIDLE,c_void_p,Int16,UInt32,UInt16,UInt16, use_last_error=False)(("ChangeIdleRoutine", windll["MAPI32"]), ((1, 'ftg'),(1, 'lpfnIdle'),(1, 'lpvIdleParam'),(1, 'priIdle'),(1, 'csecIdle'),(1, 'iroIdle'),(1, 'ircIdle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MAPIGetDefaultMalloc():
    try:
        return WINFUNCTYPE(win32more.System.Com.IMalloc_head, use_last_error=False)(("MAPIGetDefaultMalloc", windll["MAPI32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenStreamOnFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.LPALLOCATEBUFFER,win32more.System.AddressBook.LPFREEBUFFER,UInt32,POINTER(SByte),POINTER(SByte),POINTER(win32more.System.Com.IStream_head), use_last_error=False)(("OpenStreamOnFile", windll["MAPI32"]), ((1, 'lpAllocateBuffer'),(1, 'lpFreeBuffer'),(1, 'ulFlags'),(1, 'lpszFileName'),(1, 'lpszPrefix'),(1, 'lppStream'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropCopyMore():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.AddressBook.SPropValue_head),POINTER(win32more.System.AddressBook.SPropValue_head),win32more.System.AddressBook.LPALLOCATEMORE,c_void_p, use_last_error=False)(("PropCopyMore", windll["MAPI32"]), ((1, 'lpSPropValueDest'),(1, 'lpSPropValueSrc'),(1, 'lpfAllocMore'),(1, 'lpvObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UlPropSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.AddressBook.SPropValue_head), use_last_error=False)(("UlPropSize", windll["MAPI32"]), ((1, 'lpSPropValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FEqualNames():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.AddressBook.MAPINAMEID_head),POINTER(win32more.System.AddressBook.MAPINAMEID_head), use_last_error=False)(("FEqualNames", windll["MAPI32"]), ((1, 'lpName1'),(1, 'lpName2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FPropContainsProp():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.AddressBook.SPropValue_head),POINTER(win32more.System.AddressBook.SPropValue_head),UInt32, use_last_error=False)(("FPropContainsProp", windll["MAPI32"]), ((1, 'lpSPropValueDst'),(1, 'lpSPropValueSrc'),(1, 'ulFuzzyLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FPropCompareProp():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.AddressBook.SPropValue_head),UInt32,POINTER(win32more.System.AddressBook.SPropValue_head), use_last_error=False)(("FPropCompareProp", windll["MAPI32"]), ((1, 'lpSPropValue1'),(1, 'ulRelOp'),(1, 'lpSPropValue2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LPropCompareProp():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.AddressBook.SPropValue_head),POINTER(win32more.System.AddressBook.SPropValue_head), use_last_error=False)(("LPropCompareProp", windll["MAPI32"]), ((1, 'lpSPropValueA'),(1, 'lpSPropValueB'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HrAddColumns():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IMAPITable_head,POINTER(win32more.System.AddressBook.SPropTagArray_head),win32more.System.AddressBook.LPALLOCATEBUFFER,win32more.System.AddressBook.LPFREEBUFFER, use_last_error=False)(("HrAddColumns", windll["MAPI32"]), ((1, 'lptbl'),(1, 'lpproptagColumnsNew'),(1, 'lpAllocateBuffer'),(1, 'lpFreeBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HrAddColumnsEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IMAPITable_head,POINTER(win32more.System.AddressBook.SPropTagArray_head),win32more.System.AddressBook.LPALLOCATEBUFFER,win32more.System.AddressBook.LPFREEBUFFER,IntPtr, use_last_error=False)(("HrAddColumnsEx", windll["MAPI32"]), ((1, 'lptbl'),(1, 'lpproptagColumnsNew'),(1, 'lpAllocateBuffer'),(1, 'lpFreeBuffer'),(1, 'lpfnFilterColumns'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HrAllocAdviseSink():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.LPNOTIFCALLBACK,c_void_p,POINTER(win32more.System.AddressBook.IMAPIAdviseSink_head), use_last_error=False)(("HrAllocAdviseSink", windll["MAPI32"]), ((1, 'lpfnCallback'),(1, 'lpvContext'),(1, 'lppAdviseSink'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HrThisThreadAdviseSink():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IMAPIAdviseSink_head,POINTER(win32more.System.AddressBook.IMAPIAdviseSink_head), use_last_error=False)(("HrThisThreadAdviseSink", windll["MAPI32"]), ((1, 'lpAdviseSink'),(1, 'lppAdviseSink'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HrDispatchNotifications():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(("HrDispatchNotifications", windll["MAPI32"]), ((1, 'ulFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BuildDisplayTable():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.LPALLOCATEBUFFER,win32more.System.AddressBook.LPALLOCATEMORE,win32more.System.AddressBook.LPFREEBUFFER,win32more.System.Com.IMalloc_head,win32more.Foundation.HINSTANCE,UInt32,POINTER(win32more.System.AddressBook.DTPAGE_head),UInt32,POINTER(win32more.System.AddressBook.IMAPITable_head),POINTER(win32more.System.AddressBook.ITableData_head), use_last_error=False)(("BuildDisplayTable", windll["MAPI32"]), ((1, 'lpAllocateBuffer'),(1, 'lpAllocateMore'),(1, 'lpFreeBuffer'),(1, 'lpMalloc'),(1, 'hInstance'),(1, 'cPages'),(1, 'lpPage'),(1, 'ulFlags'),(1, 'lppTable'),(1, 'lppTblData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ScCountNotifications():
    try:
        return WINFUNCTYPE(Int32,Int32,POINTER(win32more.System.AddressBook.NOTIFICATION_head),POINTER(UInt32), use_last_error=False)(("ScCountNotifications", windll["MAPI32"]), ((1, 'cNotifications'),(1, 'lpNotifications'),(1, 'lpcb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ScCopyNotifications():
    try:
        return WINFUNCTYPE(Int32,Int32,POINTER(win32more.System.AddressBook.NOTIFICATION_head),c_void_p,POINTER(UInt32), use_last_error=False)(("ScCopyNotifications", windll["MAPI32"]), ((1, 'cNotification'),(1, 'lpNotifications'),(1, 'lpvDst'),(1, 'lpcb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ScRelocNotifications():
    try:
        return WINFUNCTYPE(Int32,Int32,POINTER(win32more.System.AddressBook.NOTIFICATION_head),c_void_p,c_void_p,POINTER(UInt32), use_last_error=False)(("ScRelocNotifications", windll["MAPI32"]), ((1, 'cNotification'),(1, 'lpNotifications'),(1, 'lpvBaseOld'),(1, 'lpvBaseNew'),(1, 'lpcb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ScCountProps():
    try:
        return WINFUNCTYPE(Int32,Int32,POINTER(win32more.System.AddressBook.SPropValue_head),POINTER(UInt32), use_last_error=False)(("ScCountProps", windll["MAPI32"]), ((1, 'cValues'),(1, 'lpPropArray'),(1, 'lpcb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LpValFindProp():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.AddressBook.SPropValue_head),UInt32,UInt32,POINTER(win32more.System.AddressBook.SPropValue_head), use_last_error=False)(("LpValFindProp", windll["MAPI32"]), ((1, 'ulPropTag'),(1, 'cValues'),(1, 'lpPropArray'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ScCopyProps():
    try:
        return WINFUNCTYPE(Int32,Int32,POINTER(win32more.System.AddressBook.SPropValue_head),c_void_p,POINTER(UInt32), use_last_error=False)(("ScCopyProps", windll["MAPI32"]), ((1, 'cValues'),(1, 'lpPropArray'),(1, 'lpvDst'),(1, 'lpcb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ScRelocProps():
    try:
        return WINFUNCTYPE(Int32,Int32,POINTER(win32more.System.AddressBook.SPropValue_head),c_void_p,c_void_p,POINTER(UInt32), use_last_error=False)(("ScRelocProps", windll["MAPI32"]), ((1, 'cValues'),(1, 'lpPropArray'),(1, 'lpvBaseOld'),(1, 'lpvBaseNew'),(1, 'lpcb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ScDupPropset():
    try:
        return WINFUNCTYPE(Int32,Int32,POINTER(win32more.System.AddressBook.SPropValue_head),win32more.System.AddressBook.LPALLOCATEBUFFER,POINTER(POINTER(win32more.System.AddressBook.SPropValue_head)), use_last_error=False)(("ScDupPropset", windll["MAPI32"]), ((1, 'cValues'),(1, 'lpPropArray'),(1, 'lpAllocateBuffer'),(1, 'lppPropArray'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UlAddRef():
    try:
        return WINFUNCTYPE(UInt32,c_void_p, use_last_error=False)(("UlAddRef", windll["MAPI32"]), ((1, 'lpunk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UlRelease():
    try:
        return WINFUNCTYPE(UInt32,c_void_p, use_last_error=False)(("UlRelease", windll["MAPI32"]), ((1, 'lpunk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HrGetOneProp():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IMAPIProp_head,UInt32,POINTER(POINTER(win32more.System.AddressBook.SPropValue_head)), use_last_error=False)(("HrGetOneProp", windll["MAPI32"]), ((1, 'lpMapiProp'),(1, 'ulPropTag'),(1, 'lppProp'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HrSetOneProp():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IMAPIProp_head,POINTER(win32more.System.AddressBook.SPropValue_head), use_last_error=False)(("HrSetOneProp", windll["MAPI32"]), ((1, 'lpMapiProp'),(1, 'lpProp'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FPropExists():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.AddressBook.IMAPIProp_head,UInt32, use_last_error=False)(("FPropExists", windll["MAPI32"]), ((1, 'lpMapiProp'),(1, 'ulPropTag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PpropFindProp():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.AddressBook.SPropValue_head),POINTER(win32more.System.AddressBook.SPropValue_head),UInt32,UInt32, use_last_error=False)(("PpropFindProp", windll["MAPI32"]), ((1, 'lpPropArray'),(1, 'cValues'),(1, 'ulPropTag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FreePadrlist():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.AddressBook.ADRLIST_head), use_last_error=False)(("FreePadrlist", windll["MAPI32"]), ((1, 'lpAdrlist'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FreeProws():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.AddressBook.SRowSet_head), use_last_error=False)(("FreeProws", windll["MAPI32"]), ((1, 'lpRows'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HrQueryAllRows():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IMAPITable_head,POINTER(win32more.System.AddressBook.SPropTagArray_head),POINTER(win32more.System.AddressBook.SRestriction_head),POINTER(win32more.System.AddressBook.SSortOrderSet_head),Int32,POINTER(POINTER(win32more.System.AddressBook.SRowSet_head)), use_last_error=False)(("HrQueryAllRows", windll["MAPI32"]), ((1, 'lpTable'),(1, 'lpPropTags'),(1, 'lpRestriction'),(1, 'lpSortOrderSet'),(1, 'crowsMax'),(1, 'lppRows'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SzFindCh():
    try:
        return WINFUNCTYPE(POINTER(SByte),POINTER(SByte),UInt16, use_last_error=False)(("SzFindCh", windll["MAPI32"]), ((1, 'lpsz'),(1, 'ch'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SzFindLastCh():
    try:
        return WINFUNCTYPE(POINTER(SByte),POINTER(SByte),UInt16, use_last_error=False)(("SzFindLastCh", windll["MAPI32"]), ((1, 'lpsz'),(1, 'ch'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SzFindSz():
    try:
        return WINFUNCTYPE(POINTER(SByte),POINTER(SByte),POINTER(SByte), use_last_error=False)(("SzFindSz", windll["MAPI32"]), ((1, 'lpsz'),(1, 'lpszKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UFromSz():
    try:
        return WINFUNCTYPE(UInt32,POINTER(SByte), use_last_error=False)(("UFromSz", windll["MAPI32"]), ((1, 'lpsz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ScUNCFromLocalPath():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,POINTER(Byte),UInt32, use_last_error=False)(("ScUNCFromLocalPath", windll["MAPI32"]), ((1, 'lpszLocal'),(1, 'lpszUNC'),(1, 'cchUNC'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ScLocalPathFromUNC():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,POINTER(Byte),UInt32, use_last_error=False)(("ScLocalPathFromUNC", windll["MAPI32"]), ((1, 'lpszUNC'),(1, 'lpszLocal'),(1, 'cchLocal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FtAddFt():
    try:
        return WINFUNCTYPE(win32more.Foundation.FILETIME,win32more.Foundation.FILETIME,win32more.Foundation.FILETIME, use_last_error=False)(("FtAddFt", windll["MAPI32"]), ((1, 'ftAddend1'),(1, 'ftAddend2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FtMulDwDw():
    try:
        return WINFUNCTYPE(win32more.Foundation.FILETIME,UInt32,UInt32, use_last_error=False)(("FtMulDwDw", windll["MAPI32"]), ((1, 'ftMultiplicand'),(1, 'ftMultiplier'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FtMulDw():
    try:
        return WINFUNCTYPE(win32more.Foundation.FILETIME,UInt32,win32more.Foundation.FILETIME, use_last_error=False)(("FtMulDw", windll["MAPI32"]), ((1, 'ftMultiplier'),(1, 'ftMultiplicand'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FtSubFt():
    try:
        return WINFUNCTYPE(win32more.Foundation.FILETIME,win32more.Foundation.FILETIME,win32more.Foundation.FILETIME, use_last_error=False)(("FtSubFt", windll["MAPI32"]), ((1, 'ftMinuend'),(1, 'ftSubtrahend'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FtNegFt():
    try:
        return WINFUNCTYPE(win32more.Foundation.FILETIME,win32more.Foundation.FILETIME, use_last_error=False)(("FtNegFt", windll["MAPI32"]), ((1, 'ft'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ScCreateConversationIndex():
    try:
        return WINFUNCTYPE(Int32,UInt32,c_char_p_no,POINTER(UInt32),POINTER(c_char_p_no), use_last_error=False)(("ScCreateConversationIndex", windll["MAPI32"]), ((1, 'cbParent'),(1, 'lpbParent'),(1, 'lpcbConvIndex'),(1, 'lppbConvIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WrapStoreEntryID():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(SByte),UInt32,POINTER(win32more.System.AddressBook.ENTRYID_head),POINTER(UInt32),POINTER(POINTER(win32more.System.AddressBook.ENTRYID_head)), use_last_error=False)(("WrapStoreEntryID", windll["MAPI32"]), ((1, 'ulFlags'),(1, 'lpszDLLName'),(1, 'cbOrigEntry'),(1, 'lpOrigEntry'),(1, 'lpcbWrappedEntry'),(1, 'lppWrappedEntry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RTFSync():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AddressBook.IMessage_head,UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("RTFSync", windll["MAPI32"]), ((1, 'lpMessage'),(1, 'ulFlags'),(1, 'lpfMessageUpdated'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WrapCompressedRTFStream():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,UInt32,POINTER(win32more.System.Com.IStream_head), use_last_error=False)(("WrapCompressedRTFStream", windll["MAPI32"]), ((1, 'lpCompressedRTFStream'),(1, 'ulFlags'),(1, 'lpUncompressedRTFStream'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HrIStorageFromStream():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(Guid),UInt32,POINTER(win32more.System.Com.StructuredStorage.IStorage_head), use_last_error=False)(("HrIStorageFromStream", windll["MAPI32"]), ((1, 'lpUnkIn'),(1, 'lpInterface'),(1, 'ulFlags'),(1, 'lppStorageOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ScInitMapiUtil():
    try:
        return WINFUNCTYPE(Int32,UInt32, use_last_error=False)(("ScInitMapiUtil", windll["MAPI32"]), ((1, 'ulFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeinitMapiUtil():
    try:
        return WINFUNCTYPE(Void, use_last_error=False)(("DeinitMapiUtil", windll["MAPI32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "PROP_ID_SECURE_MIN",
    "PROP_ID_SECURE_MAX",
    "MAPI_DIM",
    "MAPI_P1",
    "MAPI_SUBMITTED",
    "MAPI_SHORTTERM",
    "MAPI_NOTRECIP",
    "MAPI_THISSESSION",
    "MAPI_NOW",
    "MAPI_NOTRESERVED",
    "MAPI_COMPOUND",
    "MV_FLAG",
    "PROP_ID_NULL",
    "PROP_ID_INVALID",
    "MV_INSTANCE",
    "TABLE_CHANGED",
    "TABLE_ERROR",
    "TABLE_ROW_ADDED",
    "TABLE_ROW_DELETED",
    "TABLE_ROW_MODIFIED",
    "TABLE_SORT_DONE",
    "TABLE_RESTRICT_DONE",
    "TABLE_SETCOL_DONE",
    "TABLE_RELOAD",
    "MAPI_ERROR_VERSION",
    "MAPI_USE_DEFAULT",
    "MNID_ID",
    "MNID_STRING",
    "WAB_LOCAL_CONTAINERS",
    "WAB_PROFILE_CONTENTS",
    "WAB_IGNORE_PROFILES",
    "MAPI_ONE_OFF_NO_RICH_INFO",
    "UI_SERVICE",
    "SERVICE_UI_ALWAYS",
    "SERVICE_UI_ALLOWED",
    "UI_CURRENT_PROVIDER_FIRST",
    "WABOBJECT_LDAPURL_RETURN_MAILUSER",
    "WABOBJECT_ME_NEW",
    "WABOBJECT_ME_NOCREATE",
    "WAB_VCARD_FILE",
    "WAB_VCARD_STREAM",
    "WAB_USE_OE_SENDMAIL",
    "WAB_ENABLE_PROFILES",
    "WAB_DISPLAY_LDAPURL",
    "WAB_CONTEXT_ADRLIST",
    "WAB_DISPLAY_ISNTDS",
    "E_IMAPI_REQUEST_CANCELLED",
    "E_IMAPI_RECORDER_REQUIRED",
    "S_IMAPI_SPEEDADJUSTED",
    "S_IMAPI_ROTATIONADJUSTED",
    "S_IMAPI_BOTHADJUSTED",
    "E_IMAPI_BURN_VERIFICATION_FAILED",
    "S_IMAPI_COMMAND_HAS_SENSE_DATA",
    "E_IMAPI_RECORDER_NO_SUCH_MODE_PAGE",
    "E_IMAPI_RECORDER_MEDIA_NO_MEDIA",
    "E_IMAPI_RECORDER_MEDIA_INCOMPATIBLE",
    "E_IMAPI_RECORDER_MEDIA_UPSIDE_DOWN",
    "E_IMAPI_RECORDER_MEDIA_BECOMING_READY",
    "E_IMAPI_RECORDER_MEDIA_FORMAT_IN_PROGRESS",
    "E_IMAPI_RECORDER_MEDIA_BUSY",
    "E_IMAPI_RECORDER_INVALID_MODE_PARAMETERS",
    "E_IMAPI_RECORDER_MEDIA_WRITE_PROTECTED",
    "E_IMAPI_RECORDER_NO_SUCH_FEATURE",
    "E_IMAPI_RECORDER_FEATURE_IS_NOT_CURRENT",
    "E_IMAPI_RECORDER_GET_CONFIGURATION_NOT_SUPPORTED",
    "E_IMAPI_RECORDER_COMMAND_TIMEOUT",
    "E_IMAPI_RECORDER_DVD_STRUCTURE_NOT_PRESENT",
    "E_IMAPI_RECORDER_MEDIA_SPEED_MISMATCH",
    "E_IMAPI_RECORDER_LOCKED",
    "E_IMAPI_RECORDER_CLIENT_NAME_IS_NOT_VALID",
    "E_IMAPI_RECORDER_MEDIA_NOT_FORMATTED",
    "E_IMAPI_RECORDER_INVALID_RESPONSE_FROM_DEVICE",
    "E_IMAPI_LOSS_OF_STREAMING",
    "E_IMAPI_UNEXPECTED_RESPONSE_FROM_DEVICE",
    "S_IMAPI_WRITE_NOT_IN_PROGRESS",
    "E_IMAPI_DF2DATA_WRITE_IN_PROGRESS",
    "E_IMAPI_DF2DATA_WRITE_NOT_IN_PROGRESS",
    "E_IMAPI_DF2DATA_INVALID_MEDIA_STATE",
    "E_IMAPI_DF2DATA_STREAM_NOT_SUPPORTED",
    "E_IMAPI_DF2DATA_STREAM_TOO_LARGE_FOR_CURRENT_MEDIA",
    "E_IMAPI_DF2DATA_MEDIA_NOT_BLANK",
    "E_IMAPI_DF2DATA_MEDIA_IS_NOT_SUPPORTED",
    "E_IMAPI_DF2DATA_RECORDER_NOT_SUPPORTED",
    "E_IMAPI_DF2DATA_CLIENT_NAME_IS_NOT_VALID",
    "E_IMAPI_DF2TAO_WRITE_IN_PROGRESS",
    "E_IMAPI_DF2TAO_WRITE_NOT_IN_PROGRESS",
    "E_IMAPI_DF2TAO_MEDIA_IS_NOT_PREPARED",
    "E_IMAPI_DF2TAO_MEDIA_IS_PREPARED",
    "E_IMAPI_DF2TAO_PROPERTY_FOR_BLANK_MEDIA_ONLY",
    "E_IMAPI_DF2TAO_TABLE_OF_CONTENTS_EMPTY_DISC",
    "E_IMAPI_DF2TAO_MEDIA_IS_NOT_BLANK",
    "E_IMAPI_DF2TAO_MEDIA_IS_NOT_SUPPORTED",
    "E_IMAPI_DF2TAO_TRACK_LIMIT_REACHED",
    "E_IMAPI_DF2TAO_NOT_ENOUGH_SPACE",
    "E_IMAPI_DF2TAO_NO_RECORDER_SPECIFIED",
    "E_IMAPI_DF2TAO_INVALID_ISRC",
    "E_IMAPI_DF2TAO_INVALID_MCN",
    "E_IMAPI_DF2TAO_STREAM_NOT_SUPPORTED",
    "E_IMAPI_DF2TAO_RECORDER_NOT_SUPPORTED",
    "E_IMAPI_DF2TAO_CLIENT_NAME_IS_NOT_VALID",
    "E_IMAPI_DF2RAW_WRITE_IN_PROGRESS",
    "E_IMAPI_DF2RAW_WRITE_NOT_IN_PROGRESS",
    "E_IMAPI_DF2RAW_MEDIA_IS_NOT_PREPARED",
    "E_IMAPI_DF2RAW_MEDIA_IS_PREPARED",
    "E_IMAPI_DF2RAW_CLIENT_NAME_IS_NOT_VALID",
    "E_IMAPI_DF2RAW_MEDIA_IS_NOT_BLANK",
    "E_IMAPI_DF2RAW_MEDIA_IS_NOT_SUPPORTED",
    "E_IMAPI_DF2RAW_NOT_ENOUGH_SPACE",
    "E_IMAPI_DF2RAW_NO_RECORDER_SPECIFIED",
    "E_IMAPI_DF2RAW_STREAM_NOT_SUPPORTED",
    "E_IMAPI_DF2RAW_DATA_BLOCK_TYPE_NOT_SUPPORTED",
    "E_IMAPI_DF2RAW_STREAM_LEADIN_TOO_SHORT",
    "E_IMAPI_DF2RAW_RECORDER_NOT_SUPPORTED",
    "E_IMAPI_ERASE_RECORDER_IN_USE",
    "E_IMAPI_ERASE_ONLY_ONE_RECORDER_SUPPORTED",
    "E_IMAPI_ERASE_DISC_INFORMATION_TOO_SMALL",
    "E_IMAPI_ERASE_MODE_PAGE_2A_TOO_SMALL",
    "E_IMAPI_ERASE_MEDIA_IS_NOT_ERASABLE",
    "E_IMAPI_ERASE_DRIVE_FAILED_ERASE_COMMAND",
    "E_IMAPI_ERASE_TOOK_LONGER_THAN_ONE_HOUR",
    "E_IMAPI_ERASE_UNEXPECTED_DRIVE_RESPONSE_DURING_ERASE",
    "E_IMAPI_ERASE_DRIVE_FAILED_SPINUP_COMMAND",
    "E_IMAPI_ERASE_MEDIA_IS_NOT_SUPPORTED",
    "E_IMAPI_ERASE_RECORDER_NOT_SUPPORTED",
    "E_IMAPI_ERASE_CLIENT_NAME_IS_NOT_VALID",
    "E_IMAPI_RAW_IMAGE_IS_READ_ONLY",
    "E_IMAPI_RAW_IMAGE_TOO_MANY_TRACKS",
    "E_IMAPI_RAW_IMAGE_SECTOR_TYPE_NOT_SUPPORTED",
    "E_IMAPI_RAW_IMAGE_NO_TRACKS",
    "E_IMAPI_RAW_IMAGE_TRACKS_ALREADY_ADDED",
    "E_IMAPI_RAW_IMAGE_INSUFFICIENT_SPACE",
    "E_IMAPI_RAW_IMAGE_TOO_MANY_TRACK_INDEXES",
    "E_IMAPI_RAW_IMAGE_TRACK_INDEX_NOT_FOUND",
    "S_IMAPI_RAW_IMAGE_TRACK_INDEX_ALREADY_EXISTS",
    "E_IMAPI_RAW_IMAGE_TRACK_INDEX_OFFSET_ZERO_CANNOT_BE_CLEARED",
    "E_IMAPI_RAW_IMAGE_TRACK_INDEX_TOO_CLOSE_TO_OTHER_INDEX",
    "FACILITY_IMAPI2",
    "IMAPI_E_FSI_INTERNAL_ERROR",
    "IMAPI_E_INVALID_PARAM",
    "IMAPI_E_READONLY",
    "IMAPI_E_NO_OUTPUT",
    "IMAPI_E_INVALID_VOLUME_NAME",
    "IMAPI_E_INVALID_DATE",
    "IMAPI_E_FILE_SYSTEM_NOT_EMPTY",
    "IMAPI_E_NOT_FILE",
    "IMAPI_E_NOT_DIR",
    "IMAPI_E_DIR_NOT_EMPTY",
    "IMAPI_E_NOT_IN_FILE_SYSTEM",
    "IMAPI_E_INVALID_PATH",
    "IMAPI_E_RESTRICTED_NAME_VIOLATION",
    "IMAPI_E_DUP_NAME",
    "IMAPI_E_NO_UNIQUE_NAME",
    "IMAPI_E_ITEM_NOT_FOUND",
    "IMAPI_E_FILE_NOT_FOUND",
    "IMAPI_E_DIR_NOT_FOUND",
    "IMAPI_E_IMAGE_SIZE_LIMIT",
    "IMAPI_E_IMAGE_TOO_BIG",
    "IMAPI_E_DATA_STREAM_INCONSISTENCY",
    "IMAPI_E_DATA_STREAM_READ_FAILURE",
    "IMAPI_E_DATA_STREAM_CREATE_FAILURE",
    "IMAPI_E_DIRECTORY_READ_FAILURE",
    "IMAPI_E_TOO_MANY_DIRS",
    "IMAPI_E_ISO9660_LEVELS",
    "IMAPI_E_DATA_TOO_BIG",
    "IMAPI_E_INCOMPATIBLE_PREVIOUS_SESSION",
    "IMAPI_E_STASHFILE_OPEN_FAILURE",
    "IMAPI_E_STASHFILE_SEEK_FAILURE",
    "IMAPI_E_STASHFILE_WRITE_FAILURE",
    "IMAPI_E_STASHFILE_READ_FAILURE",
    "IMAPI_E_INVALID_WORKING_DIRECTORY",
    "IMAPI_E_WORKING_DIRECTORY_SPACE",
    "IMAPI_E_STASHFILE_MOVE",
    "IMAPI_E_BOOT_IMAGE_DATA",
    "IMAPI_E_BOOT_OBJECT_CONFLICT",
    "IMAPI_E_BOOT_EMULATION_IMAGE_SIZE_MISMATCH",
    "IMAPI_E_EMPTY_DISC",
    "IMAPI_E_NO_SUPPORTED_FILE_SYSTEM",
    "IMAPI_E_FILE_SYSTEM_NOT_FOUND",
    "IMAPI_E_FILE_SYSTEM_READ_CONSISTENCY_ERROR",
    "IMAPI_E_FILE_SYSTEM_FEATURE_NOT_SUPPORTED",
    "IMAPI_E_IMPORT_TYPE_COLLISION_FILE_EXISTS_AS_DIRECTORY",
    "IMAPI_E_IMPORT_SEEK_FAILURE",
    "IMAPI_E_IMPORT_READ_FAILURE",
    "IMAPI_E_DISC_MISMATCH",
    "IMAPI_E_IMPORT_MEDIA_NOT_ALLOWED",
    "IMAPI_E_UDF_NOT_WRITE_COMPATIBLE",
    "IMAPI_E_INCOMPATIBLE_MULTISESSION_TYPE",
    "IMAPI_E_NO_COMPATIBLE_MULTISESSION_TYPE",
    "IMAPI_E_MULTISESSION_NOT_SET",
    "IMAPI_E_IMPORT_TYPE_COLLISION_DIRECTORY_EXISTS_AS_FILE",
    "IMAPI_S_IMAGE_FEATURE_NOT_SUPPORTED",
    "IMAPI_E_PROPERTY_NOT_ACCESSIBLE",
    "IMAPI_E_UDF_REVISION_CHANGE_NOT_ALLOWED",
    "IMAPI_E_BAD_MULTISESSION_PARAMETER",
    "IMAPI_E_FILE_SYSTEM_CHANGE_NOT_ALLOWED",
    "IMAPI_E_IMAGEMANAGER_IMAGE_NOT_ALIGNED",
    "IMAPI_E_IMAGEMANAGER_NO_VALID_VD_FOUND",
    "IMAPI_E_IMAGEMANAGER_NO_IMAGE",
    "IMAPI_E_IMAGEMANAGER_IMAGE_TOO_BIG",
    "MAPI_E_CALL_FAILED",
    "MAPI_E_NOT_ENOUGH_MEMORY",
    "MAPI_E_INVALID_PARAMETER",
    "MAPI_E_INTERFACE_NOT_SUPPORTED",
    "MAPI_E_NO_ACCESS",
    "TAD_ALL_ROWS",
    "PRILOWEST",
    "PRIHIGHEST",
    "PRIUSER",
    "ENTRYID",
    "MAPIUID",
    "SPropTagArray",
    "SBinary",
    "SShortArray",
    "SGuidArray",
    "SRealArray",
    "SLongArray",
    "SLargeIntegerArray",
    "SDateTimeArray",
    "SAppTimeArray",
    "SCurrencyArray",
    "SBinaryArray",
    "SDoubleArray",
    "SWStringArray",
    "SLPSTRArray",
    "_PV",
    "SPropValue",
    "SPropProblem",
    "SPropProblemArray",
    "FLATENTRY",
    "FLATENTRYLIST",
    "MTSID",
    "FLATMTSIDLIST",
    "ADRENTRY",
    "ADRLIST",
    "SRow",
    "SRowSet",
    "LPALLOCATEBUFFER",
    "LPALLOCATEMORE",
    "LPFREEBUFFER",
    "MAPIERROR",
    "ERROR_NOTIFICATION",
    "NEWMAIL_NOTIFICATION",
    "OBJECT_NOTIFICATION",
    "TABLE_NOTIFICATION",
    "EXTENDED_NOTIFICATION",
    "STATUS_OBJECT_NOTIFICATION",
    "NOTIFICATION",
    "IMAPIAdviseSink",
    "LPNOTIFCALLBACK",
    "IMAPIProgress",
    "MAPINAMEID",
    "IMAPIProp",
    "SSortOrder",
    "SSortOrderSet",
    "SAndRestriction",
    "SOrRestriction",
    "SNotRestriction",
    "SContentRestriction",
    "SBitMaskRestriction",
    "SPropertyRestriction",
    "SComparePropsRestriction",
    "SSizeRestriction",
    "SExistRestriction",
    "SSubRestriction",
    "SCommentRestriction",
    "SRestriction",
    "IMAPITable",
    "IProfSect",
    "IMAPIStatus",
    "IMAPIContainer",
    "_flaglist",
    "IABContainer",
    "IMailUser",
    "IDistList",
    "IMAPIFolder",
    "IMsgStore",
    "IMessage",
    "IAttach",
    "LPFNABSDI",
    "LPFNDISMISS",
    "LPFNBUTTON",
    "ADRPARM",
    "IMAPIControl",
    "DTBLLABEL",
    "DTBLEDIT",
    "DTBLLBX",
    "DTBLCOMBOBOX",
    "DTBLDDLBX",
    "DTBLCHECKBOX",
    "DTBLGROUPBOX",
    "DTBLBUTTON",
    "DTBLPAGE",
    "DTBLRADIOBUTTON",
    "DTBLMVLISTBOX",
    "DTBLMVDDLBX",
    "IProviderAdmin",
    "Gender",
    "Gender_genderUnspecified",
    "Gender_genderFemale",
    "Gender_genderMale",
    "CALLERRELEASE",
    "ITableData",
    "IPropData",
    "FNIDLE",
    "PFNIDLE",
    "LPOPENSTREAMONFILE",
    "DTCTL",
    "DTPAGE",
    "LPDISPATCHNOTIFICATIONS",
    "LPCREATECONVERSATIONINDEX",
    "IAddrBook",
    "_WABACTIONITEM",
    "IWABObject",
    "IWABOBJECT_QueryInterface_METHOD",
    "IWABOBJECT_AddRef_METHOD",
    "IWABOBJECT_Release_METHOD",
    "IWABOBJECT_GetLastError_METHOD",
    "IWABOBJECT_AllocateBuffer_METHOD",
    "IWABOBJECT_AllocateMore_METHOD",
    "IWABOBJECT_FreeBuffer_METHOD",
    "IWABOBJECT_Backup_METHOD",
    "IWABOBJECT_Import_METHOD",
    "IWABOBJECT_Find_METHOD",
    "IWABOBJECT_VCardDisplay_METHOD",
    "IWABOBJECT_LDAPUrl_METHOD",
    "IWABOBJECT_VCardCreate_METHOD",
    "IWABOBJECT_VCardRetrieve_METHOD",
    "IWABOBJECT_GetMe_METHOD",
    "IWABOBJECT_SetMe_METHOD",
    "IWABOBJECT_",
    "WAB_PARAM",
    "LPWABOPEN",
    "LPWABOPENEX",
    "WABIMPORTPARAM",
    "WABEXTDISPLAY",
    "IWABExtInit",
    "LPWABALLOCATEBUFFER",
    "LPWABALLOCATEMORE",
    "LPWABFREEBUFFER",
    "NOTIFKEY",
    "CreateTable",
    "CreateIProp",
    "MAPIInitIdle",
    "MAPIDeinitIdle",
    "FtgRegisterIdleRoutine",
    "DeregisterIdleRoutine",
    "EnableIdleRoutine",
    "ChangeIdleRoutine",
    "MAPIGetDefaultMalloc",
    "OpenStreamOnFile",
    "PropCopyMore",
    "UlPropSize",
    "FEqualNames",
    "FPropContainsProp",
    "FPropCompareProp",
    "LPropCompareProp",
    "HrAddColumns",
    "HrAddColumnsEx",
    "HrAllocAdviseSink",
    "HrThisThreadAdviseSink",
    "HrDispatchNotifications",
    "BuildDisplayTable",
    "ScCountNotifications",
    "ScCopyNotifications",
    "ScRelocNotifications",
    "ScCountProps",
    "LpValFindProp",
    "ScCopyProps",
    "ScRelocProps",
    "ScDupPropset",
    "UlAddRef",
    "UlRelease",
    "HrGetOneProp",
    "HrSetOneProp",
    "FPropExists",
    "PpropFindProp",
    "FreePadrlist",
    "FreeProws",
    "HrQueryAllRows",
    "SzFindCh",
    "SzFindLastCh",
    "SzFindSz",
    "UFromSz",
    "ScUNCFromLocalPath",
    "ScLocalPathFromUNC",
    "FtAddFt",
    "FtMulDwDw",
    "FtMulDw",
    "FtSubFt",
    "FtNegFt",
    "ScCreateConversationIndex",
    "WrapStoreEntryID",
    "RTFSync",
    "WrapCompressedRTFStream",
    "HrIStorageFromStream",
    "ScInitMapiUtil",
    "DeinitMapiUtil",
]
