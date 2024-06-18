from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Storage.Cabinets
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
def FCICreate(perf: POINTER(win32more.Windows.Win32.Storage.Cabinets.ERF), pfnfcifp: win32more.Windows.Win32.Storage.Cabinets.PFNFCIFILEPLACED, pfna: win32more.Windows.Win32.Storage.Cabinets.PFNFCIALLOC, pfnf: win32more.Windows.Win32.Storage.Cabinets.PFNFCIFREE, pfnopen: win32more.Windows.Win32.Storage.Cabinets.PFNFCIOPEN, pfnread: win32more.Windows.Win32.Storage.Cabinets.PFNFCIREAD, pfnwrite: win32more.Windows.Win32.Storage.Cabinets.PFNFCIWRITE, pfnclose: win32more.Windows.Win32.Storage.Cabinets.PFNFCICLOSE, pfnseek: win32more.Windows.Win32.Storage.Cabinets.PFNFCISEEK, pfndelete: win32more.Windows.Win32.Storage.Cabinets.PFNFCIDELETE, pfnfcigtf: win32more.Windows.Win32.Storage.Cabinets.PFNFCIGETTEMPFILE, pccab: POINTER(win32more.Windows.Win32.Storage.Cabinets.CCAB), pv: VoidPtr) -> VoidPtr: ...
@cfunctype('Cabinet.dll')
def FCIAddFile(hfci: VoidPtr, pszSourceFile: win32more.Windows.Win32.Foundation.PSTR, pszFileName: win32more.Windows.Win32.Foundation.PSTR, fExecute: win32more.Windows.Win32.Foundation.BOOL, pfnfcignc: win32more.Windows.Win32.Storage.Cabinets.PFNFCIGETNEXTCABINET, pfnfcis: win32more.Windows.Win32.Storage.Cabinets.PFNFCISTATUS, pfnfcigoi: win32more.Windows.Win32.Storage.Cabinets.PFNFCIGETOPENINFO, typeCompress: UInt16) -> win32more.Windows.Win32.Foundation.BOOL: ...
@cfunctype('Cabinet.dll')
def FCIFlushCabinet(hfci: VoidPtr, fGetNextCab: win32more.Windows.Win32.Foundation.BOOL, pfnfcignc: win32more.Windows.Win32.Storage.Cabinets.PFNFCIGETNEXTCABINET, pfnfcis: win32more.Windows.Win32.Storage.Cabinets.PFNFCISTATUS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@cfunctype('Cabinet.dll')
def FCIFlushFolder(hfci: VoidPtr, pfnfcignc: win32more.Windows.Win32.Storage.Cabinets.PFNFCIGETNEXTCABINET, pfnfcis: win32more.Windows.Win32.Storage.Cabinets.PFNFCISTATUS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@cfunctype('Cabinet.dll')
def FCIDestroy(hfci: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@cfunctype('Cabinet.dll')
def FDICreate(pfnalloc: win32more.Windows.Win32.Storage.Cabinets.PFNALLOC, pfnfree: win32more.Windows.Win32.Storage.Cabinets.PFNFREE, pfnopen: win32more.Windows.Win32.Storage.Cabinets.PFNOPEN, pfnread: win32more.Windows.Win32.Storage.Cabinets.PFNREAD, pfnwrite: win32more.Windows.Win32.Storage.Cabinets.PFNWRITE, pfnclose: win32more.Windows.Win32.Storage.Cabinets.PFNCLOSE, pfnseek: win32more.Windows.Win32.Storage.Cabinets.PFNSEEK, cpuType: win32more.Windows.Win32.Storage.Cabinets.FDICREATE_CPU_TYPE, perf: POINTER(win32more.Windows.Win32.Storage.Cabinets.ERF)) -> VoidPtr: ...
@cfunctype('Cabinet.dll')
def FDIIsCabinet(hfdi: VoidPtr, hf: IntPtr, pfdici: POINTER(win32more.Windows.Win32.Storage.Cabinets.FDICABINETINFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@cfunctype('Cabinet.dll')
def FDICopy(hfdi: VoidPtr, pszCabinet: win32more.Windows.Win32.Foundation.PSTR, pszCabPath: win32more.Windows.Win32.Foundation.PSTR, flags: Int32, pfnfdin: win32more.Windows.Win32.Storage.Cabinets.PFNFDINOTIFY, pfnfdid: win32more.Windows.Win32.Storage.Cabinets.PFNFDIDECRYPT, pvUser: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@cfunctype('Cabinet.dll')
def FDIDestroy(hfdi: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@cfunctype('Cabinet.dll')
def FDITruncateCabinet(hfdi: VoidPtr, pszCabinetName: win32more.Windows.Win32.Foundation.PSTR, iFolderToDelete: UInt16) -> win32more.Windows.Win32.Foundation.BOOL: ...
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
    szDisk: win32more.Windows.Win32.Foundation.CHAR * 256
    szCab: win32more.Windows.Win32.Foundation.CHAR * 256
    szCabPath: win32more.Windows.Win32.Foundation.CHAR * 256
class ERF(Structure):
    erfOper: Int32
    erfType: Int32
    fError: win32more.Windows.Win32.Foundation.BOOL
FCIERROR = Int32
FCIERR_NONE: win32more.Windows.Win32.Storage.Cabinets.FCIERROR = 0
FCIERR_OPEN_SRC: win32more.Windows.Win32.Storage.Cabinets.FCIERROR = 1
FCIERR_READ_SRC: win32more.Windows.Win32.Storage.Cabinets.FCIERROR = 2
FCIERR_ALLOC_FAIL: win32more.Windows.Win32.Storage.Cabinets.FCIERROR = 3
FCIERR_TEMP_FILE: win32more.Windows.Win32.Storage.Cabinets.FCIERROR = 4
FCIERR_BAD_COMPR_TYPE: win32more.Windows.Win32.Storage.Cabinets.FCIERROR = 5
FCIERR_CAB_FILE: win32more.Windows.Win32.Storage.Cabinets.FCIERROR = 6
FCIERR_USER_ABORT: win32more.Windows.Win32.Storage.Cabinets.FCIERROR = 7
FCIERR_MCI_FAIL: win32more.Windows.Win32.Storage.Cabinets.FCIERROR = 8
FCIERR_CAB_FORMAT_LIMIT: win32more.Windows.Win32.Storage.Cabinets.FCIERROR = 9
class FDICABINETINFO(Structure):
    cbCabinet: Int32
    cFolders: UInt16
    cFiles: UInt16
    setID: UInt16
    iCabinet: UInt16
    fReserve: win32more.Windows.Win32.Foundation.BOOL
    hasprev: win32more.Windows.Win32.Foundation.BOOL
    hasnext: win32more.Windows.Win32.Foundation.BOOL
FDICREATE_CPU_TYPE = Int32
cpuUNKNOWN: win32more.Windows.Win32.Storage.Cabinets.FDICREATE_CPU_TYPE = -1
cpu80286: win32more.Windows.Win32.Storage.Cabinets.FDICREATE_CPU_TYPE = 0
cpu80386: win32more.Windows.Win32.Storage.Cabinets.FDICREATE_CPU_TYPE = 1
class FDIDECRYPT(Structure):
    fdidt: win32more.Windows.Win32.Storage.Cabinets.FDIDECRYPTTYPE
    pvUser: VoidPtr
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        cabinet: _cabinet_e__Struct
        folder: _folder_e__Struct
        decrypt: _decrypt_e__Struct
        class _cabinet_e__Struct(Structure):
            pHeaderReserve: VoidPtr
            cbHeaderReserve: UInt16
            setID: UInt16
            iCabinet: Int32
        class _folder_e__Struct(Structure):
            pFolderReserve: VoidPtr
            cbFolderReserve: UInt16
            iFolder: UInt16
        class _decrypt_e__Struct(Structure):
            pDataReserve: VoidPtr
            cbDataReserve: UInt16
            pbData: VoidPtr
            cbData: UInt16
            fSplit: win32more.Windows.Win32.Foundation.BOOL
            cbPartial: UInt16
FDIDECRYPTTYPE = Int32
fdidtNEW_CABINET: win32more.Windows.Win32.Storage.Cabinets.FDIDECRYPTTYPE = 0
fdidtNEW_FOLDER: win32more.Windows.Win32.Storage.Cabinets.FDIDECRYPTTYPE = 1
fdidtDECRYPT: win32more.Windows.Win32.Storage.Cabinets.FDIDECRYPTTYPE = 2
FDIERROR = Int32
FDIERROR_NONE: win32more.Windows.Win32.Storage.Cabinets.FDIERROR = 0
FDIERROR_CABINET_NOT_FOUND: win32more.Windows.Win32.Storage.Cabinets.FDIERROR = 1
FDIERROR_NOT_A_CABINET: win32more.Windows.Win32.Storage.Cabinets.FDIERROR = 2
FDIERROR_UNKNOWN_CABINET_VERSION: win32more.Windows.Win32.Storage.Cabinets.FDIERROR = 3
FDIERROR_CORRUPT_CABINET: win32more.Windows.Win32.Storage.Cabinets.FDIERROR = 4
FDIERROR_ALLOC_FAIL: win32more.Windows.Win32.Storage.Cabinets.FDIERROR = 5
FDIERROR_BAD_COMPR_TYPE: win32more.Windows.Win32.Storage.Cabinets.FDIERROR = 6
FDIERROR_MDI_FAIL: win32more.Windows.Win32.Storage.Cabinets.FDIERROR = 7
FDIERROR_TARGET_FILE: win32more.Windows.Win32.Storage.Cabinets.FDIERROR = 8
FDIERROR_RESERVE_MISMATCH: win32more.Windows.Win32.Storage.Cabinets.FDIERROR = 9
FDIERROR_WRONG_CABINET: win32more.Windows.Win32.Storage.Cabinets.FDIERROR = 10
FDIERROR_USER_ABORT: win32more.Windows.Win32.Storage.Cabinets.FDIERROR = 11
FDIERROR_EOF: win32more.Windows.Win32.Storage.Cabinets.FDIERROR = 12
class FDINOTIFICATION(Structure):
    cb: Int32
    psz1: win32more.Windows.Win32.Foundation.PSTR
    psz2: win32more.Windows.Win32.Foundation.PSTR
    psz3: win32more.Windows.Win32.Foundation.PSTR
    pv: VoidPtr
    hf: IntPtr
    date: UInt16
    time: UInt16
    attribs: UInt16
    setID: UInt16
    iCabinet: UInt16
    iFolder: UInt16
    fdie: win32more.Windows.Win32.Storage.Cabinets.FDIERROR
FDINOTIFICATIONTYPE = Int32
fdintCABINET_INFO: win32more.Windows.Win32.Storage.Cabinets.FDINOTIFICATIONTYPE = 0
fdintPARTIAL_FILE: win32more.Windows.Win32.Storage.Cabinets.FDINOTIFICATIONTYPE = 1
fdintCOPY_FILE: win32more.Windows.Win32.Storage.Cabinets.FDINOTIFICATIONTYPE = 2
fdintCLOSE_FILE_INFO: win32more.Windows.Win32.Storage.Cabinets.FDINOTIFICATIONTYPE = 3
fdintNEXT_CABINET: win32more.Windows.Win32.Storage.Cabinets.FDINOTIFICATIONTYPE = 4
fdintENUMERATE: win32more.Windows.Win32.Storage.Cabinets.FDINOTIFICATIONTYPE = 5
if ARCH in 'X64,ARM64':
    class FDISPILLFILE(Structure):
        ach: win32more.Windows.Win32.Foundation.CHAR * 2
        cbFile: Int32
elif ARCH in 'X86':
    class FDISPILLFILE(Structure):
        ach: win32more.Windows.Win32.Foundation.CHAR * 2
        cbFile: Int32
        _pack_ = 1
@cfunctype_pointer
def PFNALLOC(cb: UInt32) -> VoidPtr: ...
@cfunctype_pointer
def PFNCLOSE(hf: IntPtr) -> Int32: ...
@cfunctype_pointer
def PFNFCIALLOC(cb: UInt32) -> VoidPtr: ...
@cfunctype_pointer
def PFNFCICLOSE(hf: IntPtr, err: POINTER(Int32), pv: VoidPtr) -> Int32: ...
@cfunctype_pointer
def PFNFCIDELETE(pszFile: win32more.Windows.Win32.Foundation.PSTR, err: POINTER(Int32), pv: VoidPtr) -> Int32: ...
@cfunctype_pointer
def PFNFCIFILEPLACED(pccab: POINTER(win32more.Windows.Win32.Storage.Cabinets.CCAB), pszFile: win32more.Windows.Win32.Foundation.PSTR, cbFile: Int32, fContinuation: win32more.Windows.Win32.Foundation.BOOL, pv: VoidPtr) -> Int32: ...
@cfunctype_pointer
def PFNFCIFREE(memory: VoidPtr) -> Void: ...
@cfunctype_pointer
def PFNFCIGETNEXTCABINET(pccab: POINTER(win32more.Windows.Win32.Storage.Cabinets.CCAB), cbPrevCab: UInt32, pv: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@cfunctype_pointer
def PFNFCIGETOPENINFO(pszName: win32more.Windows.Win32.Foundation.PSTR, pdate: POINTER(UInt16), ptime: POINTER(UInt16), pattribs: POINTER(UInt16), err: POINTER(Int32), pv: VoidPtr) -> IntPtr: ...
@cfunctype_pointer
def PFNFCIGETTEMPFILE(pszTempName: win32more.Windows.Win32.Foundation.PSTR, cbTempName: Int32, pv: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@cfunctype_pointer
def PFNFCIOPEN(pszFile: win32more.Windows.Win32.Foundation.PSTR, oflag: Int32, pmode: Int32, err: POINTER(Int32), pv: VoidPtr) -> IntPtr: ...
@cfunctype_pointer
def PFNFCIREAD(hf: IntPtr, memory: VoidPtr, cb: UInt32, err: POINTER(Int32), pv: VoidPtr) -> UInt32: ...
@cfunctype_pointer
def PFNFCISEEK(hf: IntPtr, dist: Int32, seektype: Int32, err: POINTER(Int32), pv: VoidPtr) -> Int32: ...
@cfunctype_pointer
def PFNFCISTATUS(typeStatus: UInt32, cb1: UInt32, cb2: UInt32, pv: VoidPtr) -> Int32: ...
@cfunctype_pointer
def PFNFCIWRITE(hf: IntPtr, memory: VoidPtr, cb: UInt32, err: POINTER(Int32), pv: VoidPtr) -> UInt32: ...
@cfunctype_pointer
def PFNFDIDECRYPT(pfdid: POINTER(win32more.Windows.Win32.Storage.Cabinets.FDIDECRYPT)) -> Int32: ...
@cfunctype_pointer
def PFNFDINOTIFY(fdint: win32more.Windows.Win32.Storage.Cabinets.FDINOTIFICATIONTYPE, pfdin: POINTER(win32more.Windows.Win32.Storage.Cabinets.FDINOTIFICATION)) -> IntPtr: ...
@cfunctype_pointer
def PFNFREE(pv: VoidPtr) -> Void: ...
@cfunctype_pointer
def PFNOPEN(pszFile: win32more.Windows.Win32.Foundation.PSTR, oflag: Int32, pmode: Int32) -> IntPtr: ...
@cfunctype_pointer
def PFNREAD(hf: IntPtr, pv: VoidPtr, cb: UInt32) -> UInt32: ...
@cfunctype_pointer
def PFNSEEK(hf: IntPtr, dist: Int32, seektype: Int32) -> Int32: ...
@cfunctype_pointer
def PFNWRITE(hf: IntPtr, pv: VoidPtr, cb: UInt32) -> UInt32: ...


make_ready(__name__)
