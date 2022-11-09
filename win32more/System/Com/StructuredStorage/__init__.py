from win32more.base import *
import win32more.Foundation
import win32more.Security
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
PROPSETFLAG_DEFAULT = 0
PROPSETFLAG_NONSIMPLE = 1
PROPSETFLAG_ANSI = 2
PROPSETFLAG_UNBUFFERED = 4
PROPSETFLAG_CASE_SENSITIVE = 8
PROPSET_BEHAVIOR_CASE_SENSITIVE = 1
PID_DICTIONARY = 0
PID_CODEPAGE = 1
PID_FIRST_USABLE = 2
PID_FIRST_NAME_DEFAULT = 4095
PID_LOCALE = 2147483648
PID_MODIFY_TIME = 2147483649
PID_SECURITY = 2147483650
PID_BEHAVIOR = 2147483651
PID_ILLEGAL = 4294967295
PID_MIN_READONLY = 2147483648
PID_MAX_READONLY = 3221225471
PRSPEC_INVALID = 4294967295
PROPSETHDR_OSVERSION_UNKNOWN = 4294967295
PIDDI_THUMBNAIL = 2
PIDSI_TITLE = 2
PIDSI_SUBJECT = 3
PIDSI_AUTHOR = 4
PIDSI_KEYWORDS = 5
PIDSI_COMMENTS = 6
PIDSI_TEMPLATE = 7
PIDSI_LASTAUTHOR = 8
PIDSI_REVNUMBER = 9
PIDSI_EDITTIME = 10
PIDSI_LASTPRINTED = 11
PIDSI_CREATE_DTM = 12
PIDSI_LASTSAVE_DTM = 13
PIDSI_PAGECOUNT = 14
PIDSI_WORDCOUNT = 15
PIDSI_CHARCOUNT = 16
PIDSI_THUMBNAIL = 17
PIDSI_APPNAME = 18
PIDSI_DOC_SECURITY = 19
PIDDSI_CATEGORY = 2
PIDDSI_PRESFORMAT = 3
PIDDSI_BYTECOUNT = 4
PIDDSI_LINECOUNT = 5
PIDDSI_PARCOUNT = 6
PIDDSI_SLIDECOUNT = 7
PIDDSI_NOTECOUNT = 8
PIDDSI_HIDDENCOUNT = 9
PIDDSI_MMCLIPCOUNT = 10
PIDDSI_SCALE = 11
PIDDSI_HEADINGPAIR = 12
PIDDSI_DOCPARTS = 13
PIDDSI_MANAGER = 14
PIDDSI_COMPANY = 15
PIDDSI_LINKSDIRTY = 16
PIDMSI_EDITOR = 2
PIDMSI_SUPPLIER = 3
PIDMSI_SOURCE = 4
PIDMSI_SEQUENCE_NO = 5
PIDMSI_PROJECT = 6
PIDMSI_STATUS = 7
PIDMSI_OWNER = 8
PIDMSI_RATING = 9
PIDMSI_PRODUCTION = 10
PIDMSI_COPYRIGHT = 11
CWCSTORAGENAME = 32
STGM_DIRECT = 0
STGM_TRANSACTED = 65536
STGM_SIMPLE = 134217728
STGM_READ = 0
STGM_WRITE = 1
STGM_READWRITE = 2
STGM_SHARE_DENY_NONE = 64
STGM_SHARE_DENY_READ = 48
STGM_SHARE_DENY_WRITE = 32
STGM_SHARE_EXCLUSIVE = 16
STGM_PRIORITY = 262144
STGM_DELETEONRELEASE = 67108864
STGM_NOSCRATCH = 1048576
STGM_CREATE = 4096
STGM_CONVERT = 131072
STGM_FAILIFTHERE = 0
STGM_NOSNAPSHOT = 2097152
STGM_DIRECT_SWMR = 4194304
STGFMT_STORAGE = 0
STGFMT_NATIVE = 1
STGFMT_FILE = 3
STGFMT_ANY = 4
STGFMT_DOCFILE = 5
STGFMT_DOCUMENT = 0
STGOPTIONS_VERSION = 1
CCH_MAX_PROPSTG_NAME = 31
PROPSPEC_KIND = UInt32
PRSPEC_LPWSTR = 0
PRSPEC_PROPID = 1
STGC = Int32
STGC_DEFAULT = 0
STGC_OVERWRITE = 1
STGC_ONLYIFCURRENT = 2
STGC_DANGEROUSLYCOMMITMERELYTODISKCACHE = 4
STGC_CONSOLIDATE = 8
STGMOVE = Int32
STGMOVE_MOVE = 0
STGMOVE_COPY = 1
STGMOVE_SHALLOWCOPY = 2
STATFLAG = Int32
STATFLAG_DEFAULT = 0
STATFLAG_NONAME = 1
STATFLAG_NOOPEN = 2
def _define_BSTRBLOB_head():
    class BSTRBLOB(Structure):
        pass
    return BSTRBLOB
def _define_BSTRBLOB():
    BSTRBLOB = win32more.System.Com.StructuredStorage.BSTRBLOB_head
    BSTRBLOB._fields_ = [
        ("cbSize", UInt32),
        ("pData", c_char_p_no),
    ]
    return BSTRBLOB
def _define_CLIPDATA_head():
    class CLIPDATA(Structure):
        pass
    return CLIPDATA
def _define_CLIPDATA():
    CLIPDATA = win32more.System.Com.StructuredStorage.CLIPDATA_head
    CLIPDATA._fields_ = [
        ("cbSize", UInt32),
        ("ulClipFmt", Int32),
        ("pClipData", c_char_p_no),
    ]
    return CLIPDATA
LOCKTYPE = Int32
LOCK_WRITE = 1
LOCK_EXCLUSIVE = 2
LOCK_ONLYONCE = 4
def _define_IEnumSTATSTG_head():
    class IEnumSTATSTG(win32more.System.Com.IUnknown_head):
        Guid = Guid('0000000d-0000-0000-c000-000000000046')
    return IEnumSTATSTG
def _define_IEnumSTATSTG():
    IEnumSTATSTG = win32more.System.Com.StructuredStorage.IEnumSTATSTG_head
    IEnumSTATSTG.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.STATSTG),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumSTATSTG.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'celt'),)))
    IEnumSTATSTG.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumSTATSTG.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.IEnumSTATSTG_head), use_last_error=False)(6, 'Clone', ((1, 'ppenum'),)))
    win32more.System.Com.IUnknown
    return IEnumSTATSTG
def _define_RemSNB_head():
    class RemSNB(Structure):
        pass
    return RemSNB
def _define_RemSNB():
    RemSNB = win32more.System.Com.StructuredStorage.RemSNB_head
    RemSNB._fields_ = [
        ("ulCntStr", UInt32),
        ("ulCntChar", UInt32),
        ("rgString", Char * 0),
    ]
    return RemSNB
def _define_IStorage_head():
    class IStorage(win32more.System.Com.IUnknown_head):
        Guid = Guid('0000000b-0000-0000-c000-000000000046')
    return IStorage
def _define_IStorage():
    IStorage = win32more.System.Com.StructuredStorage.IStorage_head
    IStorage.CreateStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,UInt32,POINTER(win32more.System.Com.IStream_head), use_last_error=False)(3, 'CreateStream', ((1, 'pwcsName'),(1, 'grfMode'),(1, 'reserved1'),(1, 'reserved2'),(1, 'ppstm'),)))
    IStorage.OpenStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,c_void_p,UInt32,UInt32,POINTER(win32more.System.Com.IStream_head), use_last_error=False)(4, 'OpenStream', ((1, 'pwcsName'),(1, 'reserved1'),(1, 'grfMode'),(1, 'reserved2'),(1, 'ppstm'),)))
    IStorage.CreateStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,UInt32,POINTER(win32more.System.Com.StructuredStorage.IStorage_head), use_last_error=False)(5, 'CreateStorage', ((1, 'pwcsName'),(1, 'grfMode'),(1, 'reserved1'),(1, 'reserved2'),(1, 'ppstg'),)))
    IStorage.OpenStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.StructuredStorage.IStorage_head,UInt32,POINTER(POINTER(UInt16)),UInt32,POINTER(win32more.System.Com.StructuredStorage.IStorage_head), use_last_error=False)(6, 'OpenStorage', ((1, 'pwcsName'),(1, 'pstgPriority'),(1, 'grfMode'),(1, 'snbExclude'),(1, 'reserved'),(1, 'ppstg'),)))
    IStorage.CopyTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(POINTER(UInt16)),win32more.System.Com.StructuredStorage.IStorage_head, use_last_error=False)(7, 'CopyTo', ((1, 'ciidExclude'),(1, 'rgiidExclude'),(1, 'snbExclude'),(1, 'pstgDest'),)))
    IStorage.MoveElementTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.StructuredStorage.IStorage_head,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(8, 'MoveElementTo', ((1, 'pwcsName'),(1, 'pstgDest'),(1, 'pwcsNewName'),(1, 'grfFlags'),)))
    IStorage.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(9, 'Commit', ((1, 'grfCommitFlags'),)))
    IStorage.Revert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'Revert', ()))
    IStorage.EnumElements = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,UInt32,POINTER(win32more.System.Com.StructuredStorage.IEnumSTATSTG_head), use_last_error=False)(11, 'EnumElements', ((1, 'reserved1'),(1, 'reserved2'),(1, 'reserved3'),(1, 'ppenum'),)))
    IStorage.DestroyElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(12, 'DestroyElement', ((1, 'pwcsName'),)))
    IStorage.RenameElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(13, 'RenameElement', ((1, 'pwcsOldName'),(1, 'pwcsNewName'),)))
    IStorage.SetElementTimes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(14, 'SetElementTimes', ((1, 'pwcsName'),(1, 'pctime'),(1, 'patime'),(1, 'pmtime'),)))
    IStorage.SetClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(15, 'SetClass', ((1, 'clsid'),)))
    IStorage.SetStateBits = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(16, 'SetStateBits', ((1, 'grfStateBits'),(1, 'grfMask'),)))
    IStorage.Stat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.STATSTG_head),UInt32, use_last_error=False)(17, 'Stat', ((1, 'pstatstg'),(1, 'grfStatFlag'),)))
    win32more.System.Com.IUnknown
    return IStorage
def _define_IPersistStorage_head():
    class IPersistStorage(win32more.System.Com.IPersist_head):
        Guid = Guid('0000010a-0000-0000-c000-000000000046')
    return IPersistStorage
def _define_IPersistStorage():
    IPersistStorage = win32more.System.Com.StructuredStorage.IPersistStorage_head
    IPersistStorage.IsDirty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'IsDirty', ()))
    IPersistStorage.InitNew = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IStorage_head, use_last_error=False)(5, 'InitNew', ((1, 'pStg'),)))
    IPersistStorage.Load = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IStorage_head, use_last_error=False)(6, 'Load', ((1, 'pStg'),)))
    IPersistStorage.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IStorage_head,win32more.Foundation.BOOL, use_last_error=False)(7, 'Save', ((1, 'pStgSave'),(1, 'fSameAsLoad'),)))
    IPersistStorage.SaveCompleted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IStorage_head, use_last_error=False)(8, 'SaveCompleted', ((1, 'pStgNew'),)))
    IPersistStorage.HandsOffStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'HandsOffStorage', ()))
    win32more.System.Com.IPersist
    return IPersistStorage
def _define_ILockBytes_head():
    class ILockBytes(win32more.System.Com.IUnknown_head):
        Guid = Guid('0000000a-0000-0000-c000-000000000046')
    return ILockBytes
def _define_ILockBytes():
    ILockBytes = win32more.System.Com.StructuredStorage.ILockBytes_head
    ILockBytes.ReadAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.ULARGE_INTEGER,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(3, 'ReadAt', ((1, 'ulOffset'),(1, 'pv'),(1, 'cb'),(1, 'pcbRead'),)))
    ILockBytes.WriteAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.ULARGE_INTEGER,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(4, 'WriteAt', ((1, 'ulOffset'),(1, 'pv'),(1, 'cb'),(1, 'pcbWritten'),)))
    ILockBytes.Flush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Flush', ()))
    ILockBytes.SetSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.ULARGE_INTEGER, use_last_error=False)(6, 'SetSize', ((1, 'cb'),)))
    ILockBytes.LockRegion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.ULARGE_INTEGER,win32more.Foundation.ULARGE_INTEGER,UInt32, use_last_error=False)(7, 'LockRegion', ((1, 'libOffset'),(1, 'cb'),(1, 'dwLockType'),)))
    ILockBytes.UnlockRegion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.ULARGE_INTEGER,win32more.Foundation.ULARGE_INTEGER,UInt32, use_last_error=False)(8, 'UnlockRegion', ((1, 'libOffset'),(1, 'cb'),(1, 'dwLockType'),)))
    ILockBytes.Stat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.STATSTG_head),UInt32, use_last_error=False)(9, 'Stat', ((1, 'pstatstg'),(1, 'grfStatFlag'),)))
    win32more.System.Com.IUnknown
    return ILockBytes
def _define_IRootStorage_head():
    class IRootStorage(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000012-0000-0000-c000-000000000046')
    return IRootStorage
def _define_IRootStorage():
    IRootStorage = win32more.System.Com.StructuredStorage.IRootStorage_head
    IRootStorage.SwitchToFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(3, 'SwitchToFile', ((1, 'pszFile'),)))
    win32more.System.Com.IUnknown
    return IRootStorage
def _define_IFillLockBytes_head():
    class IFillLockBytes(win32more.System.Com.IUnknown_head):
        Guid = Guid('99caf010-415e-11cf-8814-00aa00b569f5')
    return IFillLockBytes
def _define_IFillLockBytes():
    IFillLockBytes = win32more.System.Com.StructuredStorage.IFillLockBytes_head
    IFillLockBytes.FillAppend = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(3, 'FillAppend', ((1, 'pv'),(1, 'cb'),(1, 'pcbWritten'),)))
    IFillLockBytes.FillAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.ULARGE_INTEGER,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(4, 'FillAt', ((1, 'ulOffset'),(1, 'pv'),(1, 'cb'),(1, 'pcbWritten'),)))
    IFillLockBytes.SetFillSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.ULARGE_INTEGER, use_last_error=False)(5, 'SetFillSize', ((1, 'ulSize'),)))
    IFillLockBytes.Terminate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(6, 'Terminate', ((1, 'bCanceled'),)))
    win32more.System.Com.IUnknown
    return IFillLockBytes
def _define_ILayoutStorage_head():
    class ILayoutStorage(win32more.System.Com.IUnknown_head):
        Guid = Guid('0e6d4d90-6738-11cf-9608-00aa00680db4')
    return ILayoutStorage
def _define_ILayoutStorage():
    ILayoutStorage = win32more.System.Com.StructuredStorage.ILayoutStorage_head
    ILayoutStorage.LayoutScript = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StorageLayout),UInt32,UInt32, use_last_error=False)(3, 'LayoutScript', ((1, 'pStorageLayout'),(1, 'nEntries'),(1, 'glfInterleavedFlag'),)))
    ILayoutStorage.BeginMonitor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'BeginMonitor', ()))
    ILayoutStorage.EndMonitor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'EndMonitor', ()))
    ILayoutStorage.ReLayoutDocfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(6, 'ReLayoutDocfile', ((1, 'pwcsNewDfName'),)))
    ILayoutStorage.ReLayoutDocfileOnILockBytes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.ILockBytes_head, use_last_error=False)(7, 'ReLayoutDocfileOnILockBytes', ((1, 'pILockBytes'),)))
    win32more.System.Com.IUnknown
    return ILayoutStorage
def _define_IDirectWriterLock_head():
    class IDirectWriterLock(win32more.System.Com.IUnknown_head):
        Guid = Guid('0e6d4d92-6738-11cf-9608-00aa00680db4')
    return IDirectWriterLock
def _define_IDirectWriterLock():
    IDirectWriterLock = win32more.System.Com.StructuredStorage.IDirectWriterLock_head
    IDirectWriterLock.WaitForWriteAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(3, 'WaitForWriteAccess', ((1, 'dwTimeout'),)))
    IDirectWriterLock.ReleaseWriteAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'ReleaseWriteAccess', ()))
    IDirectWriterLock.HaveWriteAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'HaveWriteAccess', ()))
    win32more.System.Com.IUnknown
    return IDirectWriterLock
def _define_VERSIONEDSTREAM_head():
    class VERSIONEDSTREAM(Structure):
        pass
    return VERSIONEDSTREAM
def _define_VERSIONEDSTREAM():
    VERSIONEDSTREAM = win32more.System.Com.StructuredStorage.VERSIONEDSTREAM_head
    VERSIONEDSTREAM._fields_ = [
        ("guidVersion", Guid),
        ("pStream", win32more.System.Com.IStream_head),
    ]
    return VERSIONEDSTREAM
def _define_CAC_head():
    class CAC(Structure):
        pass
    return CAC
def _define_CAC():
    CAC = win32more.System.Com.StructuredStorage.CAC_head
    CAC._fields_ = [
        ("cElems", UInt32),
        ("pElems", win32more.Foundation.PSTR),
    ]
    return CAC
def _define_CAUB_head():
    class CAUB(Structure):
        pass
    return CAUB
def _define_CAUB():
    CAUB = win32more.System.Com.StructuredStorage.CAUB_head
    CAUB._fields_ = [
        ("cElems", UInt32),
        ("pElems", c_char_p_no),
    ]
    return CAUB
def _define_CAI_head():
    class CAI(Structure):
        pass
    return CAI
def _define_CAI():
    CAI = win32more.System.Com.StructuredStorage.CAI_head
    CAI._fields_ = [
        ("cElems", UInt32),
        ("pElems", POINTER(Int16)),
    ]
    return CAI
def _define_CAUI_head():
    class CAUI(Structure):
        pass
    return CAUI
def _define_CAUI():
    CAUI = win32more.System.Com.StructuredStorage.CAUI_head
    CAUI._fields_ = [
        ("cElems", UInt32),
        ("pElems", POINTER(UInt16)),
    ]
    return CAUI
def _define_CAL_head():
    class CAL(Structure):
        pass
    return CAL
def _define_CAL():
    CAL = win32more.System.Com.StructuredStorage.CAL_head
    CAL._fields_ = [
        ("cElems", UInt32),
        ("pElems", POINTER(Int32)),
    ]
    return CAL
def _define_CAUL_head():
    class CAUL(Structure):
        pass
    return CAUL
def _define_CAUL():
    CAUL = win32more.System.Com.StructuredStorage.CAUL_head
    CAUL._fields_ = [
        ("cElems", UInt32),
        ("pElems", POINTER(UInt32)),
    ]
    return CAUL
def _define_CAFLT_head():
    class CAFLT(Structure):
        pass
    return CAFLT
def _define_CAFLT():
    CAFLT = win32more.System.Com.StructuredStorage.CAFLT_head
    CAFLT._fields_ = [
        ("cElems", UInt32),
        ("pElems", POINTER(Single)),
    ]
    return CAFLT
def _define_CADBL_head():
    class CADBL(Structure):
        pass
    return CADBL
def _define_CADBL():
    CADBL = win32more.System.Com.StructuredStorage.CADBL_head
    CADBL._fields_ = [
        ("cElems", UInt32),
        ("pElems", POINTER(Double)),
    ]
    return CADBL
def _define_CACY_head():
    class CACY(Structure):
        pass
    return CACY
def _define_CACY():
    CACY = win32more.System.Com.StructuredStorage.CACY_head
    CACY._fields_ = [
        ("cElems", UInt32),
        ("pElems", POINTER(win32more.System.Com.CY_head)),
    ]
    return CACY
def _define_CADATE_head():
    class CADATE(Structure):
        pass
    return CADATE
def _define_CADATE():
    CADATE = win32more.System.Com.StructuredStorage.CADATE_head
    CADATE._fields_ = [
        ("cElems", UInt32),
        ("pElems", POINTER(Double)),
    ]
    return CADATE
def _define_CABSTR_head():
    class CABSTR(Structure):
        pass
    return CABSTR
def _define_CABSTR():
    CABSTR = win32more.System.Com.StructuredStorage.CABSTR_head
    CABSTR._fields_ = [
        ("cElems", UInt32),
        ("pElems", POINTER(win32more.Foundation.BSTR)),
    ]
    return CABSTR
def _define_CABSTRBLOB_head():
    class CABSTRBLOB(Structure):
        pass
    return CABSTRBLOB
def _define_CABSTRBLOB():
    CABSTRBLOB = win32more.System.Com.StructuredStorage.CABSTRBLOB_head
    CABSTRBLOB._fields_ = [
        ("cElems", UInt32),
        ("pElems", POINTER(win32more.System.Com.StructuredStorage.BSTRBLOB_head)),
    ]
    return CABSTRBLOB
def _define_CABOOL_head():
    class CABOOL(Structure):
        pass
    return CABOOL
def _define_CABOOL():
    CABOOL = win32more.System.Com.StructuredStorage.CABOOL_head
    CABOOL._fields_ = [
        ("cElems", UInt32),
        ("pElems", POINTER(Int16)),
    ]
    return CABOOL
def _define_CASCODE_head():
    class CASCODE(Structure):
        pass
    return CASCODE
def _define_CASCODE():
    CASCODE = win32more.System.Com.StructuredStorage.CASCODE_head
    CASCODE._fields_ = [
        ("cElems", UInt32),
        ("pElems", POINTER(Int32)),
    ]
    return CASCODE
def _define_CAPROPVARIANT_head():
    class CAPROPVARIANT(Structure):
        pass
    return CAPROPVARIANT
def _define_CAPROPVARIANT():
    CAPROPVARIANT = win32more.System.Com.StructuredStorage.CAPROPVARIANT_head
    CAPROPVARIANT._fields_ = [
        ("cElems", UInt32),
        ("pElems", POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)),
    ]
    return CAPROPVARIANT
def _define_CAH_head():
    class CAH(Structure):
        pass
    return CAH
def _define_CAH():
    CAH = win32more.System.Com.StructuredStorage.CAH_head
    CAH._fields_ = [
        ("cElems", UInt32),
        ("pElems", POINTER(win32more.Foundation.LARGE_INTEGER_head)),
    ]
    return CAH
def _define_CAUH_head():
    class CAUH(Structure):
        pass
    return CAUH
def _define_CAUH():
    CAUH = win32more.System.Com.StructuredStorage.CAUH_head
    CAUH._fields_ = [
        ("cElems", UInt32),
        ("pElems", POINTER(win32more.Foundation.ULARGE_INTEGER_head)),
    ]
    return CAUH
def _define_CALPSTR_head():
    class CALPSTR(Structure):
        pass
    return CALPSTR
def _define_CALPSTR():
    CALPSTR = win32more.System.Com.StructuredStorage.CALPSTR_head
    CALPSTR._fields_ = [
        ("cElems", UInt32),
        ("pElems", POINTER(win32more.Foundation.PSTR)),
    ]
    return CALPSTR
def _define_CALPWSTR_head():
    class CALPWSTR(Structure):
        pass
    return CALPWSTR
def _define_CALPWSTR():
    CALPWSTR = win32more.System.Com.StructuredStorage.CALPWSTR_head
    CALPWSTR._fields_ = [
        ("cElems", UInt32),
        ("pElems", POINTER(win32more.Foundation.PWSTR)),
    ]
    return CALPWSTR
def _define_CAFILETIME_head():
    class CAFILETIME(Structure):
        pass
    return CAFILETIME
def _define_CAFILETIME():
    CAFILETIME = win32more.System.Com.StructuredStorage.CAFILETIME_head
    CAFILETIME._fields_ = [
        ("cElems", UInt32),
        ("pElems", POINTER(win32more.Foundation.FILETIME_head)),
    ]
    return CAFILETIME
def _define_CACLIPDATA_head():
    class CACLIPDATA(Structure):
        pass
    return CACLIPDATA
def _define_CACLIPDATA():
    CACLIPDATA = win32more.System.Com.StructuredStorage.CACLIPDATA_head
    CACLIPDATA._fields_ = [
        ("cElems", UInt32),
        ("pElems", POINTER(win32more.System.Com.StructuredStorage.CLIPDATA_head)),
    ]
    return CACLIPDATA
def _define_CACLSID_head():
    class CACLSID(Structure):
        pass
    return CACLSID
def _define_CACLSID():
    CACLSID = win32more.System.Com.StructuredStorage.CACLSID_head
    CACLSID._fields_ = [
        ("cElems", UInt32),
        ("pElems", POINTER(Guid)),
    ]
    return CACLSID
def _define_PROPVARIANT_head():
    class PROPVARIANT(Structure):
        pass
    return PROPVARIANT
def _define_PROPVARIANT():
    PROPVARIANT = win32more.System.Com.StructuredStorage.PROPVARIANT_head
    class PROPVARIANT__Anonymous_e__Union(Union):
        pass
    class PROPVARIANT__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    class PROPVARIANT__Anonymous_e__Union__Anonymous_e__Struct__Anonymous_e__Union(Union):
        pass
    PROPVARIANT__Anonymous_e__Union__Anonymous_e__Struct__Anonymous_e__Union._fields_ = [
        ("cVal", win32more.Foundation.CHAR),
        ("bVal", Byte),
        ("iVal", Int16),
        ("uiVal", UInt16),
        ("lVal", Int32),
        ("ulVal", UInt32),
        ("intVal", Int32),
        ("uintVal", UInt32),
        ("hVal", win32more.Foundation.LARGE_INTEGER),
        ("uhVal", win32more.Foundation.ULARGE_INTEGER),
        ("fltVal", Single),
        ("dblVal", Double),
        ("boolVal", Int16),
        ("__OBSOLETE__VARIANT_BOOL", Int16),
        ("scode", Int32),
        ("cyVal", win32more.System.Com.CY),
        ("date", Double),
        ("filetime", win32more.Foundation.FILETIME),
        ("puuid", POINTER(Guid)),
        ("pclipdata", POINTER(win32more.System.Com.StructuredStorage.CLIPDATA_head)),
        ("bstrVal", win32more.Foundation.BSTR),
        ("bstrblobVal", win32more.System.Com.StructuredStorage.BSTRBLOB),
        ("blob", win32more.System.Com.BLOB),
        ("pszVal", win32more.Foundation.PSTR),
        ("pwszVal", win32more.Foundation.PWSTR),
        ("punkVal", win32more.System.Com.IUnknown_head),
        ("pdispVal", win32more.System.Com.IDispatch_head),
        ("pStream", win32more.System.Com.IStream_head),
        ("pStorage", win32more.System.Com.StructuredStorage.IStorage_head),
        ("pVersionedStream", POINTER(win32more.System.Com.StructuredStorage.VERSIONEDSTREAM_head)),
        ("parray", POINTER(win32more.System.Com.SAFEARRAY_head)),
        ("cac", win32more.System.Com.StructuredStorage.CAC),
        ("caub", win32more.System.Com.StructuredStorage.CAUB),
        ("cai", win32more.System.Com.StructuredStorage.CAI),
        ("caui", win32more.System.Com.StructuredStorage.CAUI),
        ("cal", win32more.System.Com.StructuredStorage.CAL),
        ("caul", win32more.System.Com.StructuredStorage.CAUL),
        ("cah", win32more.System.Com.StructuredStorage.CAH),
        ("cauh", win32more.System.Com.StructuredStorage.CAUH),
        ("caflt", win32more.System.Com.StructuredStorage.CAFLT),
        ("cadbl", win32more.System.Com.StructuredStorage.CADBL),
        ("cabool", win32more.System.Com.StructuredStorage.CABOOL),
        ("cascode", win32more.System.Com.StructuredStorage.CASCODE),
        ("cacy", win32more.System.Com.StructuredStorage.CACY),
        ("cadate", win32more.System.Com.StructuredStorage.CADATE),
        ("cafiletime", win32more.System.Com.StructuredStorage.CAFILETIME),
        ("cauuid", win32more.System.Com.StructuredStorage.CACLSID),
        ("caclipdata", win32more.System.Com.StructuredStorage.CACLIPDATA),
        ("cabstr", win32more.System.Com.StructuredStorage.CABSTR),
        ("cabstrblob", win32more.System.Com.StructuredStorage.CABSTRBLOB),
        ("calpstr", win32more.System.Com.StructuredStorage.CALPSTR),
        ("calpwstr", win32more.System.Com.StructuredStorage.CALPWSTR),
        ("capropvar", win32more.System.Com.StructuredStorage.CAPROPVARIANT),
        ("pcVal", win32more.Foundation.PSTR),
        ("pbVal", c_char_p_no),
        ("piVal", POINTER(Int16)),
        ("puiVal", POINTER(UInt16)),
        ("plVal", POINTER(Int32)),
        ("pulVal", POINTER(UInt32)),
        ("pintVal", POINTER(Int32)),
        ("puintVal", POINTER(UInt32)),
        ("pfltVal", POINTER(Single)),
        ("pdblVal", POINTER(Double)),
        ("pboolVal", POINTER(Int16)),
        ("pdecVal", POINTER(win32more.Foundation.DECIMAL_head)),
        ("pscode", POINTER(Int32)),
        ("pcyVal", POINTER(win32more.System.Com.CY_head)),
        ("pdate", POINTER(Double)),
        ("pbstrVal", POINTER(win32more.Foundation.BSTR)),
        ("ppunkVal", POINTER(win32more.System.Com.IUnknown_head)),
        ("ppdispVal", POINTER(win32more.System.Com.IDispatch_head)),
        ("pparray", POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))),
        ("pvarVal", POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)),
    ]
    PROPVARIANT__Anonymous_e__Union__Anonymous_e__Struct._anonymous_ = [
        'Anonymous',
    ]
    PROPVARIANT__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("vt", UInt16),
        ("wReserved1", UInt16),
        ("wReserved2", UInt16),
        ("wReserved3", UInt16),
        ("Anonymous", PROPVARIANT__Anonymous_e__Union__Anonymous_e__Struct__Anonymous_e__Union),
    ]
    PROPVARIANT__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    PROPVARIANT__Anonymous_e__Union._fields_ = [
        ("Anonymous", PROPVARIANT__Anonymous_e__Union__Anonymous_e__Struct),
        ("decVal", win32more.Foundation.DECIMAL),
    ]
    PROPVARIANT._anonymous_ = [
        'Anonymous',
    ]
    PROPVARIANT._fields_ = [
        ("Anonymous", PROPVARIANT__Anonymous_e__Union),
    ]
    return PROPVARIANT
def _define_PROPSPEC_head():
    class PROPSPEC(Structure):
        pass
    return PROPSPEC
def _define_PROPSPEC():
    PROPSPEC = win32more.System.Com.StructuredStorage.PROPSPEC_head
    class PROPSPEC__Anonymous_e__Union(Union):
        pass
    PROPSPEC__Anonymous_e__Union._fields_ = [
        ("propid", UInt32),
        ("lpwstr", win32more.Foundation.PWSTR),
    ]
    PROPSPEC._anonymous_ = [
        'Anonymous',
    ]
    PROPSPEC._fields_ = [
        ("ulKind", win32more.System.Com.StructuredStorage.PROPSPEC_KIND),
        ("Anonymous", PROPSPEC__Anonymous_e__Union),
    ]
    return PROPSPEC
def _define_STATPROPSTG_head():
    class STATPROPSTG(Structure):
        pass
    return STATPROPSTG
def _define_STATPROPSTG():
    STATPROPSTG = win32more.System.Com.StructuredStorage.STATPROPSTG_head
    STATPROPSTG._fields_ = [
        ("lpwstrName", win32more.Foundation.PWSTR),
        ("propid", UInt32),
        ("vt", UInt16),
    ]
    return STATPROPSTG
def _define_STATPROPSETSTG_head():
    class STATPROPSETSTG(Structure):
        pass
    return STATPROPSETSTG
def _define_STATPROPSETSTG():
    STATPROPSETSTG = win32more.System.Com.StructuredStorage.STATPROPSETSTG_head
    STATPROPSETSTG._fields_ = [
        ("fmtid", Guid),
        ("clsid", Guid),
        ("grfFlags", UInt32),
        ("mtime", win32more.Foundation.FILETIME),
        ("ctime", win32more.Foundation.FILETIME),
        ("atime", win32more.Foundation.FILETIME),
        ("dwOSVersion", UInt32),
    ]
    return STATPROPSETSTG
def _define_IPropertyStorage_head():
    class IPropertyStorage(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000138-0000-0000-c000-000000000046')
    return IPropertyStorage
def _define_IPropertyStorage():
    IPropertyStorage = win32more.System.Com.StructuredStorage.IPropertyStorage_head
    IPropertyStorage.ReadMultiple = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPSPEC),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT), use_last_error=False)(3, 'ReadMultiple', ((1, 'cpspec'),(1, 'rgpspec'),(1, 'rgpropvar'),)))
    IPropertyStorage.WriteMultiple = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPSPEC),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT),UInt32, use_last_error=False)(4, 'WriteMultiple', ((1, 'cpspec'),(1, 'rgpspec'),(1, 'rgpropvar'),(1, 'propidNameFirst'),)))
    IPropertyStorage.DeleteMultiple = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPSPEC), use_last_error=False)(5, 'DeleteMultiple', ((1, 'cpspec'),(1, 'rgpspec'),)))
    IPropertyStorage.ReadPropertyNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(6, 'ReadPropertyNames', ((1, 'cpropid'),(1, 'rgpropid'),(1, 'rglpwstrName'),)))
    IPropertyStorage.WritePropertyNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(7, 'WritePropertyNames', ((1, 'cpropid'),(1, 'rgpropid'),(1, 'rglpwstrName'),)))
    IPropertyStorage.DeletePropertyNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(8, 'DeletePropertyNames', ((1, 'cpropid'),(1, 'rgpropid'),)))
    IPropertyStorage.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(9, 'Commit', ((1, 'grfCommitFlags'),)))
    IPropertyStorage.Revert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'Revert', ()))
    IPropertyStorage.Enum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.IEnumSTATPROPSTG_head), use_last_error=False)(11, 'Enum', ((1, 'ppenum'),)))
    IPropertyStorage.SetTimes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(12, 'SetTimes', ((1, 'pctime'),(1, 'patime'),(1, 'pmtime'),)))
    IPropertyStorage.SetClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(13, 'SetClass', ((1, 'clsid'),)))
    IPropertyStorage.Stat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.STATPROPSETSTG_head), use_last_error=False)(14, 'Stat', ((1, 'pstatpsstg'),)))
    win32more.System.Com.IUnknown
    return IPropertyStorage
def _define_IPropertySetStorage_head():
    class IPropertySetStorage(win32more.System.Com.IUnknown_head):
        Guid = Guid('0000013a-0000-0000-c000-000000000046')
    return IPropertySetStorage
def _define_IPropertySetStorage():
    IPropertySetStorage = win32more.System.Com.StructuredStorage.IPropertySetStorage_head
    IPropertySetStorage.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),UInt32,UInt32,POINTER(win32more.System.Com.StructuredStorage.IPropertyStorage_head), use_last_error=False)(3, 'Create', ((1, 'rfmtid'),(1, 'pclsid'),(1, 'grfFlags'),(1, 'grfMode'),(1, 'ppprstg'),)))
    IPropertySetStorage.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(win32more.System.Com.StructuredStorage.IPropertyStorage_head), use_last_error=False)(4, 'Open', ((1, 'rfmtid'),(1, 'grfMode'),(1, 'ppprstg'),)))
    IPropertySetStorage.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(5, 'Delete', ((1, 'rfmtid'),)))
    IPropertySetStorage.Enum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.IEnumSTATPROPSETSTG_head), use_last_error=False)(6, 'Enum', ((1, 'ppenum'),)))
    win32more.System.Com.IUnknown
    return IPropertySetStorage
def _define_IEnumSTATPROPSTG_head():
    class IEnumSTATPROPSTG(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000139-0000-0000-c000-000000000046')
    return IEnumSTATPROPSTG
def _define_IEnumSTATPROPSTG():
    IEnumSTATPROPSTG = win32more.System.Com.StructuredStorage.IEnumSTATPROPSTG_head
    IEnumSTATPROPSTG.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.StructuredStorage.STATPROPSTG),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumSTATPROPSTG.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'celt'),)))
    IEnumSTATPROPSTG.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumSTATPROPSTG.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.IEnumSTATPROPSTG_head), use_last_error=False)(6, 'Clone', ((1, 'ppenum'),)))
    win32more.System.Com.IUnknown
    return IEnumSTATPROPSTG
def _define_IEnumSTATPROPSETSTG_head():
    class IEnumSTATPROPSETSTG(win32more.System.Com.IUnknown_head):
        Guid = Guid('0000013b-0000-0000-c000-000000000046')
    return IEnumSTATPROPSETSTG
def _define_IEnumSTATPROPSETSTG():
    IEnumSTATPROPSETSTG = win32more.System.Com.StructuredStorage.IEnumSTATPROPSETSTG_head
    IEnumSTATPROPSETSTG.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.StructuredStorage.STATPROPSETSTG),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumSTATPROPSETSTG.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'celt'),)))
    IEnumSTATPROPSETSTG.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumSTATPROPSETSTG.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.IEnumSTATPROPSETSTG_head), use_last_error=False)(6, 'Clone', ((1, 'ppenum'),)))
    win32more.System.Com.IUnknown
    return IEnumSTATPROPSETSTG
def _define_STGOPTIONS_head():
    class STGOPTIONS(Structure):
        pass
    return STGOPTIONS
def _define_STGOPTIONS():
    STGOPTIONS = win32more.System.Com.StructuredStorage.STGOPTIONS_head
    STGOPTIONS._fields_ = [
        ("usVersion", UInt16),
        ("reserved", UInt16),
        ("ulSectorSize", UInt32),
        ("pwcsTemplateFile", win32more.Foundation.PWSTR),
    ]
    return STGOPTIONS
PIDMSI_STATUS_VALUE = Int32
PIDMSI_STATUS_NORMAL = 0
PIDMSI_STATUS_NEW = 1
PIDMSI_STATUS_PRELIM = 2
PIDMSI_STATUS_DRAFT = 3
PIDMSI_STATUS_INPROGRESS = 4
PIDMSI_STATUS_EDIT = 5
PIDMSI_STATUS_REVIEW = 6
PIDMSI_STATUS_PROOF = 7
PIDMSI_STATUS_FINAL = 8
PIDMSI_STATUS_OTHER = 32767
def _define_SERIALIZEDPROPERTYVALUE_head():
    class SERIALIZEDPROPERTYVALUE(Structure):
        pass
    return SERIALIZEDPROPERTYVALUE
def _define_SERIALIZEDPROPERTYVALUE():
    SERIALIZEDPROPERTYVALUE = win32more.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE_head
    SERIALIZEDPROPERTYVALUE._fields_ = [
        ("dwType", UInt32),
        ("rgb", Byte * 0),
    ]
    return SERIALIZEDPROPERTYVALUE
def _define_PMemoryAllocator_head():
    class PMemoryAllocator(Structure):
        pass
    return PMemoryAllocator
def _define_PMemoryAllocator():
    PMemoryAllocator = win32more.System.Com.StructuredStorage.PMemoryAllocator_head
    return PMemoryAllocator
def _define_IPropertyBag_head():
    class IPropertyBag(win32more.System.Com.IUnknown_head):
        Guid = Guid('55272a00-42cb-11ce-8135-00aa004bb851')
    return IPropertyBag
def _define_IPropertyBag():
    IPropertyBag = win32more.System.Com.StructuredStorage.IPropertyBag_head
    IPropertyBag.Read = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.VARIANT_head),win32more.System.Com.IErrorLog_head, use_last_error=False)(3, 'Read', ((1, 'pszPropName'),(1, 'pVar'),(1, 'pErrorLog'),)))
    IPropertyBag.Write = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(4, 'Write', ((1, 'pszPropName'),(1, 'pVar'),)))
    win32more.System.Com.IUnknown
    return IPropertyBag
def _define_OLESTREAMVTBL_head():
    class OLESTREAMVTBL(Structure):
        pass
    return OLESTREAMVTBL
def _define_OLESTREAMVTBL():
    OLESTREAMVTBL = win32more.System.Com.StructuredStorage.OLESTREAMVTBL_head
    OLESTREAMVTBL._fields_ = [
        ("Get", IntPtr),
        ("Put", IntPtr),
    ]
    return OLESTREAMVTBL
def _define_OLESTREAM_head():
    class OLESTREAM(Structure):
        pass
    return OLESTREAM
def _define_OLESTREAM():
    OLESTREAM = win32more.System.Com.StructuredStorage.OLESTREAM_head
    OLESTREAM._fields_ = [
        ("lpstbl", POINTER(win32more.System.Com.StructuredStorage.OLESTREAMVTBL_head)),
    ]
    return OLESTREAM
def _define_PROPBAG2_head():
    class PROPBAG2(Structure):
        pass
    return PROPBAG2
def _define_PROPBAG2():
    PROPBAG2 = win32more.System.Com.StructuredStorage.PROPBAG2_head
    PROPBAG2._fields_ = [
        ("dwType", UInt32),
        ("vt", UInt16),
        ("cfType", UInt16),
        ("dwHint", UInt32),
        ("pstrName", win32more.Foundation.PWSTR),
        ("clsid", Guid),
    ]
    return PROPBAG2
def _define_IPropertyBag2_head():
    class IPropertyBag2(win32more.System.Com.IUnknown_head):
        Guid = Guid('22f55882-280b-11d0-a8a9-00a0c90c2004')
    return IPropertyBag2
def _define_IPropertyBag2():
    IPropertyBag2 = win32more.System.Com.StructuredStorage.IPropertyBag2_head
    IPropertyBag2.Read = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPBAG2),win32more.System.Com.IErrorLog_head,POINTER(win32more.System.Com.VARIANT),POINTER(win32more.Foundation.HRESULT), use_last_error=False)(3, 'Read', ((1, 'cProperties'),(1, 'pPropBag'),(1, 'pErrLog'),(1, 'pvarValue'),(1, 'phrError'),)))
    IPropertyBag2.Write = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPBAG2),POINTER(win32more.System.Com.VARIANT), use_last_error=False)(4, 'Write', ((1, 'cProperties'),(1, 'pPropBag'),(1, 'pvarValue'),)))
    IPropertyBag2.CountProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'CountProperties', ((1, 'pcProperties'),)))
    IPropertyBag2.GetPropertyInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPBAG2),POINTER(UInt32), use_last_error=False)(6, 'GetPropertyInfo', ((1, 'iProperty'),(1, 'cProperties'),(1, 'pPropBag'),(1, 'pcProperties'),)))
    IPropertyBag2.LoadObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.System.Com.IUnknown_head,win32more.System.Com.IErrorLog_head, use_last_error=False)(7, 'LoadObject', ((1, 'pstrName'),(1, 'dwHint'),(1, 'pUnkObject'),(1, 'pErrLog'),)))
    win32more.System.Com.IUnknown
    return IPropertyBag2
def _define_CoGetInstanceFromFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.COSERVERINFO_head),POINTER(Guid),win32more.System.Com.IUnknown_head,win32more.System.Com.CLSCTX,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.System.Com.MULTI_QI), use_last_error=False)(("CoGetInstanceFromFile", windll["OLE32"]), ((1, 'pServerInfo'),(1, 'pClsid'),(1, 'punkOuter'),(1, 'dwClsCtx'),(1, 'grfMode'),(1, 'pwszName'),(1, 'dwCount'),(1, 'pResults'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoGetInstanceFromIStorage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.COSERVERINFO_head),POINTER(Guid),win32more.System.Com.IUnknown_head,win32more.System.Com.CLSCTX,win32more.System.Com.StructuredStorage.IStorage_head,UInt32,POINTER(win32more.System.Com.MULTI_QI), use_last_error=False)(("CoGetInstanceFromIStorage", windll["OLE32"]), ((1, 'pServerInfo'),(1, 'pClsid'),(1, 'punkOuter'),(1, 'dwClsCtx'),(1, 'pstg'),(1, 'dwCount'),(1, 'pResults'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StgOpenAsyncDocfileOnIFillLockBytes():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IFillLockBytes_head,UInt32,UInt32,POINTER(win32more.System.Com.StructuredStorage.IStorage_head), use_last_error=False)(("StgOpenAsyncDocfileOnIFillLockBytes", windll["ole32"]), ((1, 'pflb'),(1, 'grfMode'),(1, 'asyncFlags'),(1, 'ppstgOpen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StgGetIFillLockBytesOnILockBytes():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.ILockBytes_head,POINTER(win32more.System.Com.StructuredStorage.IFillLockBytes_head), use_last_error=False)(("StgGetIFillLockBytesOnILockBytes", windll["ole32"]), ((1, 'pilb'),(1, 'ppflb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StgGetIFillLockBytesOnFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.StructuredStorage.IFillLockBytes_head), use_last_error=False)(("StgGetIFillLockBytesOnFile", windll["ole32"]), ((1, 'pwcsName'),(1, 'ppflb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StgOpenLayoutDocfile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.System.Com.StructuredStorage.IStorage_head), use_last_error=False)(("StgOpenLayoutDocfile", windll["dflayout"]), ((1, 'pwcsDfName'),(1, 'grfMode'),(1, 'reserved'),(1, 'ppstgOpen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateStreamOnHGlobal():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,win32more.Foundation.BOOL,POINTER(win32more.System.Com.IStream_head), use_last_error=False)(("CreateStreamOnHGlobal", windll["OLE32"]), ((1, 'hGlobal'),(1, 'fDeleteOnRelease'),(1, 'ppstm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetHGlobalFromStream():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(IntPtr), use_last_error=False)(("GetHGlobalFromStream", windll["OLE32"]), ((1, 'pstm'),(1, 'phglobal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoGetInterfaceAndReleaseStream():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("CoGetInterfaceAndReleaseStream", windll["OLE32"]), ((1, 'pStm'),(1, 'iid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantCopy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("PropVariantCopy", windll["OLE32"]), ((1, 'pvarDest'),(1, 'pvarSrc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantClear():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("PropVariantClear", windll["OLE32"]), ((1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FreePropVariantArray():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT), use_last_error=False)(("FreePropVariantArray", windll["OLE32"]), ((1, 'cVariants'),(1, 'rgvars'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StgCreateDocfile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.System.Com.StructuredStorage.IStorage_head), use_last_error=False)(("StgCreateDocfile", windll["OLE32"]), ((1, 'pwcsName'),(1, 'grfMode'),(1, 'reserved'),(1, 'ppstgOpen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StgCreateDocfileOnILockBytes():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.ILockBytes_head,UInt32,UInt32,POINTER(win32more.System.Com.StructuredStorage.IStorage_head), use_last_error=False)(("StgCreateDocfileOnILockBytes", windll["OLE32"]), ((1, 'plkbyt'),(1, 'grfMode'),(1, 'reserved'),(1, 'ppstgOpen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StgOpenStorage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.StructuredStorage.IStorage_head,UInt32,POINTER(POINTER(UInt16)),UInt32,POINTER(win32more.System.Com.StructuredStorage.IStorage_head), use_last_error=False)(("StgOpenStorage", windll["OLE32"]), ((1, 'pwcsName'),(1, 'pstgPriority'),(1, 'grfMode'),(1, 'snbExclude'),(1, 'reserved'),(1, 'ppstgOpen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StgOpenStorageOnILockBytes():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.ILockBytes_head,win32more.System.Com.StructuredStorage.IStorage_head,UInt32,POINTER(POINTER(UInt16)),UInt32,POINTER(win32more.System.Com.StructuredStorage.IStorage_head), use_last_error=False)(("StgOpenStorageOnILockBytes", windll["OLE32"]), ((1, 'plkbyt'),(1, 'pstgPriority'),(1, 'grfMode'),(1, 'snbExclude'),(1, 'reserved'),(1, 'ppstgOpen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StgIsStorageFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(("StgIsStorageFile", windll["OLE32"]), ((1, 'pwcsName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StgIsStorageILockBytes():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.ILockBytes_head, use_last_error=False)(("StgIsStorageILockBytes", windll["OLE32"]), ((1, 'plkbyt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StgSetTimes():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(("StgSetTimes", windll["OLE32"]), ((1, 'lpszName'),(1, 'pctime'),(1, 'patime'),(1, 'pmtime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StgCreateStorageEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,UInt32,POINTER(win32more.System.Com.StructuredStorage.STGOPTIONS_head),POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("StgCreateStorageEx", windll["OLE32"]), ((1, 'pwcsName'),(1, 'grfMode'),(1, 'stgfmt'),(1, 'grfAttrs'),(1, 'pStgOptions'),(1, 'pSecurityDescriptor'),(1, 'riid'),(1, 'ppObjectOpen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StgOpenStorageEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,UInt32,POINTER(win32more.System.Com.StructuredStorage.STGOPTIONS_head),POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("StgOpenStorageEx", windll["OLE32"]), ((1, 'pwcsName'),(1, 'grfMode'),(1, 'stgfmt'),(1, 'grfAttrs'),(1, 'pStgOptions'),(1, 'pSecurityDescriptor'),(1, 'riid'),(1, 'ppObjectOpen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StgCreatePropStg():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(Guid),POINTER(Guid),UInt32,UInt32,POINTER(win32more.System.Com.StructuredStorage.IPropertyStorage_head), use_last_error=False)(("StgCreatePropStg", windll["OLE32"]), ((1, 'pUnk'),(1, 'fmtid'),(1, 'pclsid'),(1, 'grfFlags'),(1, 'dwReserved'),(1, 'ppPropStg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StgOpenPropStg():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(Guid),UInt32,UInt32,POINTER(win32more.System.Com.StructuredStorage.IPropertyStorage_head), use_last_error=False)(("StgOpenPropStg", windll["OLE32"]), ((1, 'pUnk'),(1, 'fmtid'),(1, 'grfFlags'),(1, 'dwReserved'),(1, 'ppPropStg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StgCreatePropSetStg():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IStorage_head,UInt32,POINTER(win32more.System.Com.StructuredStorage.IPropertySetStorage_head), use_last_error=False)(("StgCreatePropSetStg", windll["OLE32"]), ((1, 'pStorage'),(1, 'dwReserved'),(1, 'ppPropSetStg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FmtIdToPropStgName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PWSTR, use_last_error=False)(("FmtIdToPropStgName", windll["OLE32"]), ((1, 'pfmtid'),(1, 'oszName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropStgNameToFmtId():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid), use_last_error=False)(("PropStgNameToFmtId", windll["OLE32"]), ((1, 'oszName'),(1, 'pfmtid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadClassStg():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IStorage_head,POINTER(Guid), use_last_error=False)(("ReadClassStg", windll["OLE32"]), ((1, 'pStg'),(1, 'pclsid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WriteClassStg():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IStorage_head,POINTER(Guid), use_last_error=False)(("WriteClassStg", windll["OLE32"]), ((1, 'pStg'),(1, 'rclsid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadClassStm():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(Guid), use_last_error=False)(("ReadClassStm", windll["OLE32"]), ((1, 'pStm'),(1, 'pclsid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WriteClassStm():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(Guid), use_last_error=False)(("WriteClassStm", windll["OLE32"]), ((1, 'pStm'),(1, 'rclsid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetHGlobalFromILockBytes():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.ILockBytes_head,POINTER(IntPtr), use_last_error=False)(("GetHGlobalFromILockBytes", windll["OLE32"]), ((1, 'plkbyt'),(1, 'phglobal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateILockBytesOnHGlobal():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,win32more.Foundation.BOOL,POINTER(win32more.System.Com.StructuredStorage.ILockBytes_head), use_last_error=False)(("CreateILockBytesOnHGlobal", windll["OLE32"]), ((1, 'hGlobal'),(1, 'fDeleteOnRelease'),(1, 'pplkbyt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConvertStg():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IStorage_head, use_last_error=False)(("GetConvertStg", windll["OLE32"]), ((1, 'pStg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StgConvertVariantToProperty():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),UInt16,POINTER(win32more.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE_head),POINTER(UInt32),UInt32,win32more.Foundation.BOOLEAN,POINTER(UInt32), use_last_error=False)(("StgConvertVariantToProperty", windll["ole32"]), ((1, 'pvar'),(1, 'CodePage'),(1, 'pprop'),(1, 'pcb'),(1, 'pid'),(1, 'fReserved'),(1, 'pcIndirect'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StgConvertPropertyToVariant():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE_head),UInt16,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PMemoryAllocator_head), use_last_error=False)(("StgConvertPropertyToVariant", windll["ole32"]), ((1, 'pprop'),(1, 'CodePage'),(1, 'pvar'),(1, 'pma'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StgPropertyLengthAsVariant():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE_head),UInt32,UInt16,Byte, use_last_error=False)(("StgPropertyLengthAsVariant", windll["ole32"]), ((1, 'pProp'),(1, 'cbProp'),(1, 'CodePage'),(1, 'bReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WriteFmtUserTypeStg():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IStorage_head,UInt16,win32more.Foundation.PWSTR, use_last_error=False)(("WriteFmtUserTypeStg", windll["OLE32"]), ((1, 'pstg'),(1, 'cf'),(1, 'lpszUserType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadFmtUserTypeStg():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IStorage_head,POINTER(UInt16),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("ReadFmtUserTypeStg", windll["OLE32"]), ((1, 'pstg'),(1, 'pcf'),(1, 'lplpszUserType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleConvertOLESTREAMToIStorage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.OLESTREAM_head),win32more.System.Com.StructuredStorage.IStorage_head,POINTER(win32more.System.Com.DVTARGETDEVICE_head), use_last_error=False)(("OleConvertOLESTREAMToIStorage", windll["ole32"]), ((1, 'lpolestream'),(1, 'pstg'),(1, 'ptd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleConvertIStorageToOLESTREAM():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IStorage_head,POINTER(win32more.System.Com.StructuredStorage.OLESTREAM_head), use_last_error=False)(("OleConvertIStorageToOLESTREAM", windll["ole32"]), ((1, 'pstg'),(1, 'lpolestream'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetConvertStg():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IStorage_head,win32more.Foundation.BOOL, use_last_error=False)(("SetConvertStg", windll["OLE32"]), ((1, 'pStg'),(1, 'fConvert'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleConvertIStorageToOLESTREAMEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IStorage_head,UInt16,Int32,Int32,UInt32,POINTER(win32more.System.Com.STGMEDIUM_head),POINTER(win32more.System.Com.StructuredStorage.OLESTREAM_head), use_last_error=False)(("OleConvertIStorageToOLESTREAMEx", windll["ole32"]), ((1, 'pstg'),(1, 'cfFormat'),(1, 'lWidth'),(1, 'lHeight'),(1, 'dwSize'),(1, 'pmedium'),(1, 'polestm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleConvertOLESTREAMToIStorageEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.OLESTREAM_head),win32more.System.Com.StructuredStorage.IStorage_head,POINTER(UInt16),POINTER(Int32),POINTER(Int32),POINTER(UInt32),POINTER(win32more.System.Com.STGMEDIUM_head), use_last_error=False)(("OleConvertOLESTREAMToIStorageEx", windll["ole32"]), ((1, 'polestm'),(1, 'pstg'),(1, 'pcfFormat'),(1, 'plwWidth'),(1, 'plHeight'),(1, 'pdwSize'),(1, 'pmedium'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StgSerializePropVariant():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(POINTER(win32more.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE_head)),POINTER(UInt32), use_last_error=False)(("StgSerializePropVariant", windll["PROPSYS"]), ((1, 'ppropvar'),(1, 'ppProp'),(1, 'pcb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StgDeserializePropVariant():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE_head),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("StgDeserializePropVariant", windll["PROPSYS"]), ((1, 'pprop'),(1, 'cbMax'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "PROPSETFLAG_DEFAULT",
    "PROPSETFLAG_NONSIMPLE",
    "PROPSETFLAG_ANSI",
    "PROPSETFLAG_UNBUFFERED",
    "PROPSETFLAG_CASE_SENSITIVE",
    "PROPSET_BEHAVIOR_CASE_SENSITIVE",
    "PID_DICTIONARY",
    "PID_CODEPAGE",
    "PID_FIRST_USABLE",
    "PID_FIRST_NAME_DEFAULT",
    "PID_LOCALE",
    "PID_MODIFY_TIME",
    "PID_SECURITY",
    "PID_BEHAVIOR",
    "PID_ILLEGAL",
    "PID_MIN_READONLY",
    "PID_MAX_READONLY",
    "PRSPEC_INVALID",
    "PROPSETHDR_OSVERSION_UNKNOWN",
    "PIDDI_THUMBNAIL",
    "PIDSI_TITLE",
    "PIDSI_SUBJECT",
    "PIDSI_AUTHOR",
    "PIDSI_KEYWORDS",
    "PIDSI_COMMENTS",
    "PIDSI_TEMPLATE",
    "PIDSI_LASTAUTHOR",
    "PIDSI_REVNUMBER",
    "PIDSI_EDITTIME",
    "PIDSI_LASTPRINTED",
    "PIDSI_CREATE_DTM",
    "PIDSI_LASTSAVE_DTM",
    "PIDSI_PAGECOUNT",
    "PIDSI_WORDCOUNT",
    "PIDSI_CHARCOUNT",
    "PIDSI_THUMBNAIL",
    "PIDSI_APPNAME",
    "PIDSI_DOC_SECURITY",
    "PIDDSI_CATEGORY",
    "PIDDSI_PRESFORMAT",
    "PIDDSI_BYTECOUNT",
    "PIDDSI_LINECOUNT",
    "PIDDSI_PARCOUNT",
    "PIDDSI_SLIDECOUNT",
    "PIDDSI_NOTECOUNT",
    "PIDDSI_HIDDENCOUNT",
    "PIDDSI_MMCLIPCOUNT",
    "PIDDSI_SCALE",
    "PIDDSI_HEADINGPAIR",
    "PIDDSI_DOCPARTS",
    "PIDDSI_MANAGER",
    "PIDDSI_COMPANY",
    "PIDDSI_LINKSDIRTY",
    "PIDMSI_EDITOR",
    "PIDMSI_SUPPLIER",
    "PIDMSI_SOURCE",
    "PIDMSI_SEQUENCE_NO",
    "PIDMSI_PROJECT",
    "PIDMSI_STATUS",
    "PIDMSI_OWNER",
    "PIDMSI_RATING",
    "PIDMSI_PRODUCTION",
    "PIDMSI_COPYRIGHT",
    "CWCSTORAGENAME",
    "STGM_DIRECT",
    "STGM_TRANSACTED",
    "STGM_SIMPLE",
    "STGM_READ",
    "STGM_WRITE",
    "STGM_READWRITE",
    "STGM_SHARE_DENY_NONE",
    "STGM_SHARE_DENY_READ",
    "STGM_SHARE_DENY_WRITE",
    "STGM_SHARE_EXCLUSIVE",
    "STGM_PRIORITY",
    "STGM_DELETEONRELEASE",
    "STGM_NOSCRATCH",
    "STGM_CREATE",
    "STGM_CONVERT",
    "STGM_FAILIFTHERE",
    "STGM_NOSNAPSHOT",
    "STGM_DIRECT_SWMR",
    "STGFMT_STORAGE",
    "STGFMT_NATIVE",
    "STGFMT_FILE",
    "STGFMT_ANY",
    "STGFMT_DOCFILE",
    "STGFMT_DOCUMENT",
    "STGOPTIONS_VERSION",
    "CCH_MAX_PROPSTG_NAME",
    "PROPSPEC_KIND",
    "PRSPEC_LPWSTR",
    "PRSPEC_PROPID",
    "STGC",
    "STGC_DEFAULT",
    "STGC_OVERWRITE",
    "STGC_ONLYIFCURRENT",
    "STGC_DANGEROUSLYCOMMITMERELYTODISKCACHE",
    "STGC_CONSOLIDATE",
    "STGMOVE",
    "STGMOVE_MOVE",
    "STGMOVE_COPY",
    "STGMOVE_SHALLOWCOPY",
    "STATFLAG",
    "STATFLAG_DEFAULT",
    "STATFLAG_NONAME",
    "STATFLAG_NOOPEN",
    "BSTRBLOB",
    "CLIPDATA",
    "LOCKTYPE",
    "LOCK_WRITE",
    "LOCK_EXCLUSIVE",
    "LOCK_ONLYONCE",
    "IEnumSTATSTG",
    "RemSNB",
    "IStorage",
    "IPersistStorage",
    "ILockBytes",
    "IRootStorage",
    "IFillLockBytes",
    "ILayoutStorage",
    "IDirectWriterLock",
    "VERSIONEDSTREAM",
    "CAC",
    "CAUB",
    "CAI",
    "CAUI",
    "CAL",
    "CAUL",
    "CAFLT",
    "CADBL",
    "CACY",
    "CADATE",
    "CABSTR",
    "CABSTRBLOB",
    "CABOOL",
    "CASCODE",
    "CAPROPVARIANT",
    "CAH",
    "CAUH",
    "CALPSTR",
    "CALPWSTR",
    "CAFILETIME",
    "CACLIPDATA",
    "CACLSID",
    "PROPVARIANT",
    "PROPSPEC",
    "STATPROPSTG",
    "STATPROPSETSTG",
    "IPropertyStorage",
    "IPropertySetStorage",
    "IEnumSTATPROPSTG",
    "IEnumSTATPROPSETSTG",
    "STGOPTIONS",
    "PIDMSI_STATUS_VALUE",
    "PIDMSI_STATUS_NORMAL",
    "PIDMSI_STATUS_NEW",
    "PIDMSI_STATUS_PRELIM",
    "PIDMSI_STATUS_DRAFT",
    "PIDMSI_STATUS_INPROGRESS",
    "PIDMSI_STATUS_EDIT",
    "PIDMSI_STATUS_REVIEW",
    "PIDMSI_STATUS_PROOF",
    "PIDMSI_STATUS_FINAL",
    "PIDMSI_STATUS_OTHER",
    "SERIALIZEDPROPERTYVALUE",
    "PMemoryAllocator",
    "IPropertyBag",
    "OLESTREAMVTBL",
    "OLESTREAM",
    "PROPBAG2",
    "IPropertyBag2",
    "CoGetInstanceFromFile",
    "CoGetInstanceFromIStorage",
    "StgOpenAsyncDocfileOnIFillLockBytes",
    "StgGetIFillLockBytesOnILockBytes",
    "StgGetIFillLockBytesOnFile",
    "StgOpenLayoutDocfile",
    "CreateStreamOnHGlobal",
    "GetHGlobalFromStream",
    "CoGetInterfaceAndReleaseStream",
    "PropVariantCopy",
    "PropVariantClear",
    "FreePropVariantArray",
    "StgCreateDocfile",
    "StgCreateDocfileOnILockBytes",
    "StgOpenStorage",
    "StgOpenStorageOnILockBytes",
    "StgIsStorageFile",
    "StgIsStorageILockBytes",
    "StgSetTimes",
    "StgCreateStorageEx",
    "StgOpenStorageEx",
    "StgCreatePropStg",
    "StgOpenPropStg",
    "StgCreatePropSetStg",
    "FmtIdToPropStgName",
    "PropStgNameToFmtId",
    "ReadClassStg",
    "WriteClassStg",
    "ReadClassStm",
    "WriteClassStm",
    "GetHGlobalFromILockBytes",
    "CreateILockBytesOnHGlobal",
    "GetConvertStg",
    "StgConvertVariantToProperty",
    "StgConvertPropertyToVariant",
    "StgPropertyLengthAsVariant",
    "WriteFmtUserTypeStg",
    "ReadFmtUserTypeStg",
    "OleConvertOLESTREAMToIStorage",
    "OleConvertIStorageToOLESTREAM",
    "SetConvertStg",
    "OleConvertIStorageToOLESTREAMEx",
    "OleConvertOLESTREAMToIStorageEx",
    "StgSerializePropVariant",
    "StgDeserializePropVariant",
]
