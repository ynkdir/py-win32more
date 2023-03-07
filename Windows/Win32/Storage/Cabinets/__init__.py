from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Storage.Cabinets
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
INCLUDED_FCI: UInt32 = 1
_A_NAME_IS_UTF: UInt32 = 128
_A_EXEC: UInt32 = 64
statusFile: UInt32 = 0
statusFolder: UInt32 = 1
statusCabinet: UInt32 = 2
INCLUDED_TYPES_FCI_FDI: UInt32 = 1
CB_MAX_DISK: Int32 = 2147483647
CB_MAX_FILENAME: UInt32 = 256
CB_MAX_CABINET_NAME: UInt32 = 256
CB_MAX_CAB_PATH: UInt32 = 256
CB_MAX_DISK_NAME: UInt32 = 256
tcompMASK_TYPE: UInt32 = 15
tcompTYPE_NONE: UInt32 = 0
tcompTYPE_MSZIP: UInt32 = 1
tcompTYPE_QUANTUM: UInt32 = 2
tcompTYPE_LZX: UInt32 = 3
tcompBAD: UInt32 = 15
tcompMASK_LZX_WINDOW: UInt32 = 7936
tcompLZX_WINDOW_LO: UInt32 = 3840
tcompLZX_WINDOW_HI: UInt32 = 5376
tcompSHIFT_LZX_WINDOW: UInt32 = 8
tcompMASK_QUANTUM_LEVEL: UInt32 = 240
tcompQUANTUM_LEVEL_LO: UInt32 = 16
tcompQUANTUM_LEVEL_HI: UInt32 = 112
tcompSHIFT_QUANTUM_LEVEL: UInt32 = 4
tcompMASK_QUANTUM_MEM: UInt32 = 7936
tcompQUANTUM_MEM_LO: UInt32 = 2560
tcompQUANTUM_MEM_HI: UInt32 = 5376
tcompSHIFT_QUANTUM_MEM: UInt32 = 8
tcompMASK_RESERVED: UInt32 = 57344
INCLUDED_FDI: UInt32 = 1
@cfunctype('Cabinet.dll')
def FCICreate(perf: POINTER(Windows.Win32.Storage.Cabinets.ERF_head), pfnfcifp: Windows.Win32.Storage.Cabinets.PFNFCIFILEPLACED, pfna: Windows.Win32.Storage.Cabinets.PFNFCIALLOC, pfnf: Windows.Win32.Storage.Cabinets.PFNFCIFREE, pfnopen: Windows.Win32.Storage.Cabinets.PFNFCIOPEN, pfnread: Windows.Win32.Storage.Cabinets.PFNFCIREAD, pfnwrite: Windows.Win32.Storage.Cabinets.PFNFCIWRITE, pfnclose: Windows.Win32.Storage.Cabinets.PFNFCICLOSE, pfnseek: Windows.Win32.Storage.Cabinets.PFNFCISEEK, pfndelete: Windows.Win32.Storage.Cabinets.PFNFCIDELETE, pfnfcigtf: Windows.Win32.Storage.Cabinets.PFNFCIGETTEMPFILE, pccab: POINTER(Windows.Win32.Storage.Cabinets.CCAB_head), pv: c_void_p) -> c_void_p: ...
@cfunctype('Cabinet.dll')
def FCIAddFile(hfci: c_void_p, pszSourceFile: Windows.Win32.Foundation.PSTR, pszFileName: Windows.Win32.Foundation.PSTR, fExecute: Windows.Win32.Foundation.BOOL, pfnfcignc: Windows.Win32.Storage.Cabinets.PFNFCIGETNEXTCABINET, pfnfcis: Windows.Win32.Storage.Cabinets.PFNFCISTATUS, pfnfcigoi: Windows.Win32.Storage.Cabinets.PFNFCIGETOPENINFO, typeCompress: UInt16) -> Windows.Win32.Foundation.BOOL: ...
@cfunctype('Cabinet.dll')
def FCIFlushCabinet(hfci: c_void_p, fGetNextCab: Windows.Win32.Foundation.BOOL, pfnfcignc: Windows.Win32.Storage.Cabinets.PFNFCIGETNEXTCABINET, pfnfcis: Windows.Win32.Storage.Cabinets.PFNFCISTATUS) -> Windows.Win32.Foundation.BOOL: ...
@cfunctype('Cabinet.dll')
def FCIFlushFolder(hfci: c_void_p, pfnfcignc: Windows.Win32.Storage.Cabinets.PFNFCIGETNEXTCABINET, pfnfcis: Windows.Win32.Storage.Cabinets.PFNFCISTATUS) -> Windows.Win32.Foundation.BOOL: ...
@cfunctype('Cabinet.dll')
def FCIDestroy(hfci: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@cfunctype('Cabinet.dll')
def FDICreate(pfnalloc: Windows.Win32.Storage.Cabinets.PFNALLOC, pfnfree: Windows.Win32.Storage.Cabinets.PFNFREE, pfnopen: Windows.Win32.Storage.Cabinets.PFNOPEN, pfnread: Windows.Win32.Storage.Cabinets.PFNREAD, pfnwrite: Windows.Win32.Storage.Cabinets.PFNWRITE, pfnclose: Windows.Win32.Storage.Cabinets.PFNCLOSE, pfnseek: Windows.Win32.Storage.Cabinets.PFNSEEK, cpuType: Windows.Win32.Storage.Cabinets.FDICREATE_CPU_TYPE, perf: POINTER(Windows.Win32.Storage.Cabinets.ERF_head)) -> c_void_p: ...
@cfunctype('Cabinet.dll')
def FDIIsCabinet(hfdi: c_void_p, hf: IntPtr, pfdici: POINTER(Windows.Win32.Storage.Cabinets.FDICABINETINFO_head)) -> Windows.Win32.Foundation.BOOL: ...
@cfunctype('Cabinet.dll')
def FDICopy(hfdi: c_void_p, pszCabinet: Windows.Win32.Foundation.PSTR, pszCabPath: Windows.Win32.Foundation.PSTR, flags: Int32, pfnfdin: Windows.Win32.Storage.Cabinets.PFNFDINOTIFY, pfnfdid: Windows.Win32.Storage.Cabinets.PFNFDIDECRYPT, pvUser: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@cfunctype('Cabinet.dll')
def FDIDestroy(hfdi: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@cfunctype('Cabinet.dll')
def FDITruncateCabinet(hfdi: c_void_p, pszCabinetName: Windows.Win32.Foundation.PSTR, iFolderToDelete: UInt16) -> Windows.Win32.Foundation.BOOL: ...
class CCAB(Structure):
    cb: UInt32
    cbFolderThresh: UInt32
    cbReserveCFHeader: UInt32
    cbReserveCFFolder: UInt32
    cbReserveCFData: UInt32
    iCab: Int32
    iDisk: Int32
    fFailOnIncompressible: Int32
    setID: UInt16
    szDisk: Windows.Win32.Foundation.CHAR * 256
    szCab: Windows.Win32.Foundation.CHAR * 256
    szCabPath: Windows.Win32.Foundation.CHAR * 256
class ERF(Structure):
    erfOper: Int32
    erfType: Int32
    fError: Windows.Win32.Foundation.BOOL
FCIERROR = Int32
FCIERR_NONE: FCIERROR = 0
FCIERR_OPEN_SRC: FCIERROR = 1
FCIERR_READ_SRC: FCIERROR = 2
FCIERR_ALLOC_FAIL: FCIERROR = 3
FCIERR_TEMP_FILE: FCIERROR = 4
FCIERR_BAD_COMPR_TYPE: FCIERROR = 5
FCIERR_CAB_FILE: FCIERROR = 6
FCIERR_USER_ABORT: FCIERROR = 7
FCIERR_MCI_FAIL: FCIERROR = 8
FCIERR_CAB_FORMAT_LIMIT: FCIERROR = 9
class FDICABINETINFO(Structure):
    cbCabinet: Int32
    cFolders: UInt16
    cFiles: UInt16
    setID: UInt16
    iCabinet: UInt16
    fReserve: Windows.Win32.Foundation.BOOL
    hasprev: Windows.Win32.Foundation.BOOL
    hasnext: Windows.Win32.Foundation.BOOL
FDICREATE_CPU_TYPE = Int32
FDICREATE_CPU_TYPE_cpuUNKNOWN: FDICREATE_CPU_TYPE = -1
FDICREATE_CPU_TYPE_cpu80286: FDICREATE_CPU_TYPE = 0
FDICREATE_CPU_TYPE_cpu80386: FDICREATE_CPU_TYPE = 1
class FDIDECRYPT(Structure):
    fdidt: Windows.Win32.Storage.Cabinets.FDIDECRYPTTYPE
    pvUser: c_void_p
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        cabinet: _cabinet_e__Struct
        folder: _folder_e__Struct
        decrypt: _decrypt_e__Struct
        class _cabinet_e__Struct(Structure):
            pHeaderReserve: c_void_p
            cbHeaderReserve: UInt16
            setID: UInt16
            iCabinet: Int32
        class _folder_e__Struct(Structure):
            pFolderReserve: c_void_p
            cbFolderReserve: UInt16
            iFolder: UInt16
        class _decrypt_e__Struct(Structure):
            pDataReserve: c_void_p
            cbDataReserve: UInt16
            pbData: c_void_p
            cbData: UInt16
            fSplit: Windows.Win32.Foundation.BOOL
            cbPartial: UInt16
FDIDECRYPTTYPE = Int32
FDIDECRYPTTYPE_fdidtNEW_CABINET: FDIDECRYPTTYPE = 0
FDIDECRYPTTYPE_fdidtNEW_FOLDER: FDIDECRYPTTYPE = 1
FDIDECRYPTTYPE_fdidtDECRYPT: FDIDECRYPTTYPE = 2
FDIERROR = Int32
FDIERROR_NONE: FDIERROR = 0
FDIERROR_CABINET_NOT_FOUND: FDIERROR = 1
FDIERROR_NOT_A_CABINET: FDIERROR = 2
FDIERROR_UNKNOWN_CABINET_VERSION: FDIERROR = 3
FDIERROR_CORRUPT_CABINET: FDIERROR = 4
FDIERROR_ALLOC_FAIL: FDIERROR = 5
FDIERROR_BAD_COMPR_TYPE: FDIERROR = 6
FDIERROR_MDI_FAIL: FDIERROR = 7
FDIERROR_TARGET_FILE: FDIERROR = 8
FDIERROR_RESERVE_MISMATCH: FDIERROR = 9
FDIERROR_WRONG_CABINET: FDIERROR = 10
FDIERROR_USER_ABORT: FDIERROR = 11
FDIERROR_EOF: FDIERROR = 12
class FDINOTIFICATION(Structure):
    cb: Int32
    psz1: Windows.Win32.Foundation.PSTR
    psz2: Windows.Win32.Foundation.PSTR
    psz3: Windows.Win32.Foundation.PSTR
    pv: c_void_p
    hf: IntPtr
    date: UInt16
    time: UInt16
    attribs: UInt16
    setID: UInt16
    iCabinet: UInt16
    iFolder: UInt16
    fdie: Windows.Win32.Storage.Cabinets.FDIERROR
FDINOTIFICATIONTYPE = Int32
FDINOTIFICATIONTYPE_fdintCABINET_INFO: FDINOTIFICATIONTYPE = 0
FDINOTIFICATIONTYPE_fdintPARTIAL_FILE: FDINOTIFICATIONTYPE = 1
FDINOTIFICATIONTYPE_fdintCOPY_FILE: FDINOTIFICATIONTYPE = 2
FDINOTIFICATIONTYPE_fdintCLOSE_FILE_INFO: FDINOTIFICATIONTYPE = 3
FDINOTIFICATIONTYPE_fdintNEXT_CABINET: FDINOTIFICATIONTYPE = 4
FDINOTIFICATIONTYPE_fdintENUMERATE: FDINOTIFICATIONTYPE = 5
if ARCH in 'X64,ARM64':
    class FDISPILLFILE(Structure):
        ach: Windows.Win32.Foundation.CHAR * 2
        cbFile: Int32
if ARCH in 'X86':
    class FDISPILLFILE(Structure):
        ach: Windows.Win32.Foundation.CHAR * 2
        cbFile: Int32
        _pack_ = 1
@cfunctype_pointer
def PFNALLOC(cb: UInt32) -> c_void_p: ...
@cfunctype_pointer
def PFNCLOSE(hf: IntPtr) -> Int32: ...
@cfunctype_pointer
def PFNFCIALLOC(cb: UInt32) -> c_void_p: ...
@cfunctype_pointer
def PFNFCICLOSE(hf: IntPtr, err: POINTER(Int32), pv: c_void_p) -> Int32: ...
@cfunctype_pointer
def PFNFCIDELETE(pszFile: Windows.Win32.Foundation.PSTR, err: POINTER(Int32), pv: c_void_p) -> Int32: ...
@cfunctype_pointer
def PFNFCIFILEPLACED(pccab: POINTER(Windows.Win32.Storage.Cabinets.CCAB_head), pszFile: Windows.Win32.Foundation.PSTR, cbFile: Int32, fContinuation: Windows.Win32.Foundation.BOOL, pv: c_void_p) -> Int32: ...
@cfunctype_pointer
def PFNFCIFREE(memory: c_void_p) -> Void: ...
@cfunctype_pointer
def PFNFCIGETNEXTCABINET(pccab: POINTER(Windows.Win32.Storage.Cabinets.CCAB_head), cbPrevCab: UInt32, pv: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@cfunctype_pointer
def PFNFCIGETOPENINFO(pszName: Windows.Win32.Foundation.PSTR, pdate: POINTER(UInt16), ptime: POINTER(UInt16), pattribs: POINTER(UInt16), err: POINTER(Int32), pv: c_void_p) -> IntPtr: ...
@cfunctype_pointer
def PFNFCIGETTEMPFILE(pszTempName: Windows.Win32.Foundation.PSTR, cbTempName: Int32, pv: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@cfunctype_pointer
def PFNFCIOPEN(pszFile: Windows.Win32.Foundation.PSTR, oflag: Int32, pmode: Int32, err: POINTER(Int32), pv: c_void_p) -> IntPtr: ...
@cfunctype_pointer
def PFNFCIREAD(hf: IntPtr, memory: c_void_p, cb: UInt32, err: POINTER(Int32), pv: c_void_p) -> UInt32: ...
@cfunctype_pointer
def PFNFCISEEK(hf: IntPtr, dist: Int32, seektype: Int32, err: POINTER(Int32), pv: c_void_p) -> Int32: ...
@cfunctype_pointer
def PFNFCISTATUS(typeStatus: UInt32, cb1: UInt32, cb2: UInt32, pv: c_void_p) -> Int32: ...
@cfunctype_pointer
def PFNFCIWRITE(hf: IntPtr, memory: c_void_p, cb: UInt32, err: POINTER(Int32), pv: c_void_p) -> UInt32: ...
@cfunctype_pointer
def PFNFDIDECRYPT(pfdid: POINTER(Windows.Win32.Storage.Cabinets.FDIDECRYPT_head)) -> Int32: ...
@cfunctype_pointer
def PFNFDINOTIFY(fdint: Windows.Win32.Storage.Cabinets.FDINOTIFICATIONTYPE, pfdin: POINTER(Windows.Win32.Storage.Cabinets.FDINOTIFICATION_head)) -> IntPtr: ...
@cfunctype_pointer
def PFNFREE(pv: c_void_p) -> Void: ...
@cfunctype_pointer
def PFNOPEN(pszFile: Windows.Win32.Foundation.PSTR, oflag: Int32, pmode: Int32) -> IntPtr: ...
@cfunctype_pointer
def PFNREAD(hf: IntPtr, pv: c_void_p, cb: UInt32) -> UInt32: ...
@cfunctype_pointer
def PFNSEEK(hf: IntPtr, dist: Int32, seektype: Int32) -> Int32: ...
@cfunctype_pointer
def PFNWRITE(hf: IntPtr, pv: c_void_p, cb: UInt32) -> UInt32: ...
make_head(_module, 'CCAB')
make_head(_module, 'ERF')
make_head(_module, 'FDICABINETINFO')
make_head(_module, 'FDIDECRYPT')
make_head(_module, 'FDINOTIFICATION')
if ARCH in 'X64,ARM64':
    make_head(_module, 'FDISPILLFILE')
if ARCH in 'X86':
    make_head(_module, 'FDISPILLFILE')
make_head(_module, 'PFNALLOC')
make_head(_module, 'PFNCLOSE')
make_head(_module, 'PFNFCIALLOC')
make_head(_module, 'PFNFCICLOSE')
make_head(_module, 'PFNFCIDELETE')
make_head(_module, 'PFNFCIFILEPLACED')
make_head(_module, 'PFNFCIFREE')
make_head(_module, 'PFNFCIGETNEXTCABINET')
make_head(_module, 'PFNFCIGETOPENINFO')
make_head(_module, 'PFNFCIGETTEMPFILE')
make_head(_module, 'PFNFCIOPEN')
make_head(_module, 'PFNFCIREAD')
make_head(_module, 'PFNFCISEEK')
make_head(_module, 'PFNFCISTATUS')
make_head(_module, 'PFNFCIWRITE')
make_head(_module, 'PFNFDIDECRYPT')
make_head(_module, 'PFNFDINOTIFY')
make_head(_module, 'PFNFREE')
make_head(_module, 'PFNOPEN')
make_head(_module, 'PFNREAD')
make_head(_module, 'PFNSEEK')
make_head(_module, 'PFNWRITE')
__all__ = [
    "CB_MAX_CABINET_NAME",
    "CB_MAX_CAB_PATH",
    "CB_MAX_DISK",
    "CB_MAX_DISK_NAME",
    "CB_MAX_FILENAME",
    "CCAB",
    "ERF",
    "FCIAddFile",
    "FCICreate",
    "FCIDestroy",
    "FCIERROR",
    "FCIERR_ALLOC_FAIL",
    "FCIERR_BAD_COMPR_TYPE",
    "FCIERR_CAB_FILE",
    "FCIERR_CAB_FORMAT_LIMIT",
    "FCIERR_MCI_FAIL",
    "FCIERR_NONE",
    "FCIERR_OPEN_SRC",
    "FCIERR_READ_SRC",
    "FCIERR_TEMP_FILE",
    "FCIERR_USER_ABORT",
    "FCIFlushCabinet",
    "FCIFlushFolder",
    "FDICABINETINFO",
    "FDICREATE_CPU_TYPE",
    "FDICREATE_CPU_TYPE_cpu80286",
    "FDICREATE_CPU_TYPE_cpu80386",
    "FDICREATE_CPU_TYPE_cpuUNKNOWN",
    "FDICopy",
    "FDICreate",
    "FDIDECRYPT",
    "FDIDECRYPTTYPE",
    "FDIDECRYPTTYPE_fdidtDECRYPT",
    "FDIDECRYPTTYPE_fdidtNEW_CABINET",
    "FDIDECRYPTTYPE_fdidtNEW_FOLDER",
    "FDIDestroy",
    "FDIERROR",
    "FDIERROR_ALLOC_FAIL",
    "FDIERROR_BAD_COMPR_TYPE",
    "FDIERROR_CABINET_NOT_FOUND",
    "FDIERROR_CORRUPT_CABINET",
    "FDIERROR_EOF",
    "FDIERROR_MDI_FAIL",
    "FDIERROR_NONE",
    "FDIERROR_NOT_A_CABINET",
    "FDIERROR_RESERVE_MISMATCH",
    "FDIERROR_TARGET_FILE",
    "FDIERROR_UNKNOWN_CABINET_VERSION",
    "FDIERROR_USER_ABORT",
    "FDIERROR_WRONG_CABINET",
    "FDIIsCabinet",
    "FDINOTIFICATION",
    "FDINOTIFICATIONTYPE",
    "FDINOTIFICATIONTYPE_fdintCABINET_INFO",
    "FDINOTIFICATIONTYPE_fdintCLOSE_FILE_INFO",
    "FDINOTIFICATIONTYPE_fdintCOPY_FILE",
    "FDINOTIFICATIONTYPE_fdintENUMERATE",
    "FDINOTIFICATIONTYPE_fdintNEXT_CABINET",
    "FDINOTIFICATIONTYPE_fdintPARTIAL_FILE",
    "FDISPILLFILE",
    "FDITruncateCabinet",
    "INCLUDED_FCI",
    "INCLUDED_FDI",
    "INCLUDED_TYPES_FCI_FDI",
    "PFNALLOC",
    "PFNCLOSE",
    "PFNFCIALLOC",
    "PFNFCICLOSE",
    "PFNFCIDELETE",
    "PFNFCIFILEPLACED",
    "PFNFCIFREE",
    "PFNFCIGETNEXTCABINET",
    "PFNFCIGETOPENINFO",
    "PFNFCIGETTEMPFILE",
    "PFNFCIOPEN",
    "PFNFCIREAD",
    "PFNFCISEEK",
    "PFNFCISTATUS",
    "PFNFCIWRITE",
    "PFNFDIDECRYPT",
    "PFNFDINOTIFY",
    "PFNFREE",
    "PFNOPEN",
    "PFNREAD",
    "PFNSEEK",
    "PFNWRITE",
    "_A_EXEC",
    "_A_NAME_IS_UTF",
    "statusCabinet",
    "statusFile",
    "statusFolder",
    "tcompBAD",
    "tcompLZX_WINDOW_HI",
    "tcompLZX_WINDOW_LO",
    "tcompMASK_LZX_WINDOW",
    "tcompMASK_QUANTUM_LEVEL",
    "tcompMASK_QUANTUM_MEM",
    "tcompMASK_RESERVED",
    "tcompMASK_TYPE",
    "tcompQUANTUM_LEVEL_HI",
    "tcompQUANTUM_LEVEL_LO",
    "tcompQUANTUM_MEM_HI",
    "tcompQUANTUM_MEM_LO",
    "tcompSHIFT_LZX_WINDOW",
    "tcompSHIFT_QUANTUM_LEVEL",
    "tcompSHIFT_QUANTUM_MEM",
    "tcompTYPE_LZX",
    "tcompTYPE_MSZIP",
    "tcompTYPE_NONE",
    "tcompTYPE_QUANTUM",
]
_arch_optional = [
]