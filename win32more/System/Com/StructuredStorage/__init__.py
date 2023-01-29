from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Security
import win32more.System.Com
import win32more.System.Com.StructuredStorage
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
PROPSETFLAG_DEFAULT: UInt32 = 0
PROPSETFLAG_NONSIMPLE: UInt32 = 1
PROPSETFLAG_ANSI: UInt32 = 2
PROPSETFLAG_UNBUFFERED: UInt32 = 4
PROPSETFLAG_CASE_SENSITIVE: UInt32 = 8
PROPSET_BEHAVIOR_CASE_SENSITIVE: UInt32 = 1
PID_DICTIONARY: UInt32 = 0
PID_CODEPAGE: UInt32 = 1
PID_FIRST_USABLE: UInt32 = 2
PID_FIRST_NAME_DEFAULT: UInt32 = 4095
PID_LOCALE: UInt32 = 2147483648
PID_MODIFY_TIME: UInt32 = 2147483649
PID_SECURITY: UInt32 = 2147483650
PID_BEHAVIOR: UInt32 = 2147483651
PID_ILLEGAL: UInt32 = 4294967295
PID_MIN_READONLY: UInt32 = 2147483648
PID_MAX_READONLY: UInt32 = 3221225471
PRSPEC_INVALID: UInt32 = 4294967295
PROPSETHDR_OSVERSION_UNKNOWN: UInt32 = 4294967295
PIDDI_THUMBNAIL: Int32 = 2
PIDSI_TITLE: Int32 = 2
PIDSI_SUBJECT: Int32 = 3
PIDSI_AUTHOR: Int32 = 4
PIDSI_KEYWORDS: Int32 = 5
PIDSI_COMMENTS: Int32 = 6
PIDSI_TEMPLATE: Int32 = 7
PIDSI_LASTAUTHOR: Int32 = 8
PIDSI_REVNUMBER: Int32 = 9
PIDSI_EDITTIME: Int32 = 10
PIDSI_LASTPRINTED: Int32 = 11
PIDSI_CREATE_DTM: Int32 = 12
PIDSI_LASTSAVE_DTM: Int32 = 13
PIDSI_PAGECOUNT: Int32 = 14
PIDSI_WORDCOUNT: Int32 = 15
PIDSI_CHARCOUNT: Int32 = 16
PIDSI_THUMBNAIL: Int32 = 17
PIDSI_APPNAME: Int32 = 18
PIDSI_DOC_SECURITY: Int32 = 19
PIDDSI_CATEGORY: UInt32 = 2
PIDDSI_PRESFORMAT: UInt32 = 3
PIDDSI_BYTECOUNT: UInt32 = 4
PIDDSI_LINECOUNT: UInt32 = 5
PIDDSI_PARCOUNT: UInt32 = 6
PIDDSI_SLIDECOUNT: UInt32 = 7
PIDDSI_NOTECOUNT: UInt32 = 8
PIDDSI_HIDDENCOUNT: UInt32 = 9
PIDDSI_MMCLIPCOUNT: UInt32 = 10
PIDDSI_SCALE: UInt32 = 11
PIDDSI_HEADINGPAIR: UInt32 = 12
PIDDSI_DOCPARTS: UInt32 = 13
PIDDSI_MANAGER: UInt32 = 14
PIDDSI_COMPANY: UInt32 = 15
PIDDSI_LINKSDIRTY: UInt32 = 16
PIDMSI_EDITOR: Int32 = 2
PIDMSI_SUPPLIER: Int32 = 3
PIDMSI_SOURCE: Int32 = 4
PIDMSI_SEQUENCE_NO: Int32 = 5
PIDMSI_PROJECT: Int32 = 6
PIDMSI_STATUS: Int32 = 7
PIDMSI_OWNER: Int32 = 8
PIDMSI_RATING: Int32 = 9
PIDMSI_PRODUCTION: Int32 = 10
PIDMSI_COPYRIGHT: Int32 = 11
CWCSTORAGENAME: UInt32 = 32
STGOPTIONS_VERSION: UInt32 = 1
CCH_MAX_PROPSTG_NAME: UInt32 = 31
@winfunctype('OLE32.dll')
def CoGetInstanceFromFile(pServerInfo: POINTER(win32more.System.Com.COSERVERINFO_head), pClsid: POINTER(Guid), punkOuter: win32more.System.Com.IUnknown_head, dwClsCtx: win32more.System.Com.CLSCTX, grfMode: UInt32, pwszName: win32more.Foundation.PWSTR, dwCount: UInt32, pResults: POINTER(win32more.System.Com.MULTI_QI_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetInstanceFromIStorage(pServerInfo: POINTER(win32more.System.Com.COSERVERINFO_head), pClsid: POINTER(Guid), punkOuter: win32more.System.Com.IUnknown_head, dwClsCtx: win32more.System.Com.CLSCTX, pstg: win32more.System.Com.StructuredStorage.IStorage_head, dwCount: UInt32, pResults: POINTER(win32more.System.Com.MULTI_QI_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def StgOpenAsyncDocfileOnIFillLockBytes(pflb: win32more.System.Com.StructuredStorage.IFillLockBytes_head, grfMode: UInt32, asyncFlags: UInt32, ppstgOpen: POINTER(win32more.System.Com.StructuredStorage.IStorage_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def StgGetIFillLockBytesOnILockBytes(pilb: win32more.System.Com.StructuredStorage.ILockBytes_head, ppflb: POINTER(win32more.System.Com.StructuredStorage.IFillLockBytes_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def StgGetIFillLockBytesOnFile(pwcsName: win32more.Foundation.PWSTR, ppflb: POINTER(win32more.System.Com.StructuredStorage.IFillLockBytes_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('dflayout.dll')
def StgOpenLayoutDocfile(pwcsDfName: win32more.Foundation.PWSTR, grfMode: UInt32, reserved: UInt32, ppstgOpen: POINTER(win32more.System.Com.StructuredStorage.IStorage_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreateStreamOnHGlobal(hGlobal: IntPtr, fDeleteOnRelease: win32more.Foundation.BOOL, ppstm: POINTER(win32more.System.Com.IStream_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def GetHGlobalFromStream(pstm: win32more.System.Com.IStream_head, phglobal: POINTER(IntPtr)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetInterfaceAndReleaseStream(pStm: win32more.System.Com.IStream_head, iid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def PropVariantCopy(pvarDest: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pvarSrc: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def PropVariantClear(pvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def FreePropVariantArray(cVariants: UInt32, rgvars: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgCreateDocfile(pwcsName: win32more.Foundation.PWSTR, grfMode: win32more.System.Com.STGM, reserved: UInt32, ppstgOpen: POINTER(win32more.System.Com.StructuredStorage.IStorage_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgCreateDocfileOnILockBytes(plkbyt: win32more.System.Com.StructuredStorage.ILockBytes_head, grfMode: win32more.System.Com.STGM, reserved: UInt32, ppstgOpen: POINTER(win32more.System.Com.StructuredStorage.IStorage_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgOpenStorage(pwcsName: win32more.Foundation.PWSTR, pstgPriority: win32more.System.Com.StructuredStorage.IStorage_head, grfMode: win32more.System.Com.STGM, snbExclude: POINTER(POINTER(UInt16)), reserved: UInt32, ppstgOpen: POINTER(win32more.System.Com.StructuredStorage.IStorage_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgOpenStorageOnILockBytes(plkbyt: win32more.System.Com.StructuredStorage.ILockBytes_head, pstgPriority: win32more.System.Com.StructuredStorage.IStorage_head, grfMode: win32more.System.Com.STGM, snbExclude: POINTER(POINTER(UInt16)), reserved: UInt32, ppstgOpen: POINTER(win32more.System.Com.StructuredStorage.IStorage_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgIsStorageFile(pwcsName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgIsStorageILockBytes(plkbyt: win32more.System.Com.StructuredStorage.ILockBytes_head) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgSetTimes(lpszName: win32more.Foundation.PWSTR, pctime: POINTER(win32more.Foundation.FILETIME_head), patime: POINTER(win32more.Foundation.FILETIME_head), pmtime: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgCreateStorageEx(pwcsName: win32more.Foundation.PWSTR, grfMode: win32more.System.Com.STGM, stgfmt: win32more.System.Com.StructuredStorage.STGFMT, grfAttrs: UInt32, pStgOptions: POINTER(win32more.System.Com.StructuredStorage.STGOPTIONS_head), pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, riid: POINTER(Guid), ppObjectOpen: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgOpenStorageEx(pwcsName: win32more.Foundation.PWSTR, grfMode: win32more.System.Com.STGM, stgfmt: win32more.System.Com.StructuredStorage.STGFMT, grfAttrs: UInt32, pStgOptions: POINTER(win32more.System.Com.StructuredStorage.STGOPTIONS_head), pSecurityDescriptor: win32more.Security.PSECURITY_DESCRIPTOR, riid: POINTER(Guid), ppObjectOpen: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgCreatePropStg(pUnk: win32more.System.Com.IUnknown_head, fmtid: POINTER(Guid), pclsid: POINTER(Guid), grfFlags: UInt32, dwReserved: UInt32, ppPropStg: POINTER(win32more.System.Com.StructuredStorage.IPropertyStorage_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgOpenPropStg(pUnk: win32more.System.Com.IUnknown_head, fmtid: POINTER(Guid), grfFlags: UInt32, dwReserved: UInt32, ppPropStg: POINTER(win32more.System.Com.StructuredStorage.IPropertyStorage_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgCreatePropSetStg(pStorage: win32more.System.Com.StructuredStorage.IStorage_head, dwReserved: UInt32, ppPropSetStg: POINTER(win32more.System.Com.StructuredStorage.IPropertySetStorage_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def FmtIdToPropStgName(pfmtid: POINTER(Guid), oszName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def PropStgNameToFmtId(oszName: win32more.Foundation.PWSTR, pfmtid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def ReadClassStg(pStg: win32more.System.Com.StructuredStorage.IStorage_head, pclsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def WriteClassStg(pStg: win32more.System.Com.StructuredStorage.IStorage_head, rclsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def ReadClassStm(pStm: win32more.System.Com.IStream_head, pclsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def WriteClassStm(pStm: win32more.System.Com.IStream_head, rclsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def GetHGlobalFromILockBytes(plkbyt: win32more.System.Com.StructuredStorage.ILockBytes_head, phglobal: POINTER(IntPtr)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreateILockBytesOnHGlobal(hGlobal: IntPtr, fDeleteOnRelease: win32more.Foundation.BOOL, pplkbyt: POINTER(win32more.System.Com.StructuredStorage.ILockBytes_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def GetConvertStg(pStg: win32more.System.Com.StructuredStorage.IStorage_head) -> win32more.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def StgConvertVariantToProperty(pvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), CodePage: UInt16, pprop: POINTER(win32more.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE_head), pcb: POINTER(UInt32), pid: UInt32, fReserved: win32more.Foundation.BOOLEAN, pcIndirect: POINTER(UInt32)) -> POINTER(win32more.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE_head): ...
@winfunctype('ole32.dll')
def StgConvertPropertyToVariant(pprop: POINTER(win32more.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE_head), CodePage: UInt16, pvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), pma: POINTER(win32more.System.Com.StructuredStorage.PMemoryAllocator_head)) -> win32more.Foundation.BOOLEAN: ...
@winfunctype('ole32.dll')
def StgPropertyLengthAsVariant(pProp: POINTER(win32more.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE_head), cbProp: UInt32, CodePage: UInt16, bReserved: Byte) -> UInt32: ...
@winfunctype('OLE32.dll')
def WriteFmtUserTypeStg(pstg: win32more.System.Com.StructuredStorage.IStorage_head, cf: UInt16, lpszUserType: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def ReadFmtUserTypeStg(pstg: win32more.System.Com.StructuredStorage.IStorage_head, pcf: POINTER(UInt16), lplpszUserType: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleConvertOLESTREAMToIStorage(lpolestream: POINTER(win32more.System.Com.StructuredStorage.OLESTREAM_head), pstg: win32more.System.Com.StructuredStorage.IStorage_head, ptd: POINTER(win32more.System.Com.DVTARGETDEVICE_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleConvertIStorageToOLESTREAM(pstg: win32more.System.Com.StructuredStorage.IStorage_head, lpolestream: POINTER(win32more.System.Com.StructuredStorage.OLESTREAM_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def SetConvertStg(pStg: win32more.System.Com.StructuredStorage.IStorage_head, fConvert: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleConvertIStorageToOLESTREAMEx(pstg: win32more.System.Com.StructuredStorage.IStorage_head, cfFormat: UInt16, lWidth: Int32, lHeight: Int32, dwSize: UInt32, pmedium: POINTER(win32more.System.Com.STGMEDIUM_head), polestm: POINTER(win32more.System.Com.StructuredStorage.OLESTREAM_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleConvertOLESTREAMToIStorageEx(polestm: POINTER(win32more.System.Com.StructuredStorage.OLESTREAM_head), pstg: win32more.System.Com.StructuredStorage.IStorage_head, pcfFormat: POINTER(UInt16), plwWidth: POINTER(Int32), plHeight: POINTER(Int32), pdwSize: POINTER(UInt32), pmedium: POINTER(win32more.System.Com.STGMEDIUM_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def StgSerializePropVariant(ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), ppProp: POINTER(POINTER(win32more.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE_head)), pcb: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def StgDeserializePropVariant(pprop: POINTER(win32more.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE_head), cbMax: UInt32, ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
class BSTRBLOB(Structure):
    cbSize: UInt32
    pData: c_char_p_no
class CABOOL(Structure):
    cElems: UInt32
    pElems: POINTER(win32more.Foundation.VARIANT_BOOL)
class CABSTR(Structure):
    cElems: UInt32
    pElems: POINTER(win32more.Foundation.BSTR)
class CABSTRBLOB(Structure):
    cElems: UInt32
    pElems: POINTER(win32more.System.Com.StructuredStorage.BSTRBLOB_head)
class CAC(Structure):
    cElems: UInt32
    pElems: win32more.Foundation.PSTR
class CACLIPDATA(Structure):
    cElems: UInt32
    pElems: POINTER(win32more.System.Com.StructuredStorage.CLIPDATA_head)
class CACLSID(Structure):
    cElems: UInt32
    pElems: POINTER(Guid)
class CACY(Structure):
    cElems: UInt32
    pElems: POINTER(win32more.System.Com.CY_head)
class CADATE(Structure):
    cElems: UInt32
    pElems: POINTER(Double)
class CADBL(Structure):
    cElems: UInt32
    pElems: POINTER(Double)
class CAFILETIME(Structure):
    cElems: UInt32
    pElems: POINTER(win32more.Foundation.FILETIME_head)
class CAFLT(Structure):
    cElems: UInt32
    pElems: POINTER(Single)
class CAH(Structure):
    cElems: UInt32
    pElems: POINTER(win32more.Foundation.LARGE_INTEGER_head)
class CAI(Structure):
    cElems: UInt32
    pElems: POINTER(Int16)
class CAL(Structure):
    cElems: UInt32
    pElems: POINTER(Int32)
class CALPSTR(Structure):
    cElems: UInt32
    pElems: POINTER(win32more.Foundation.PSTR)
class CALPWSTR(Structure):
    cElems: UInt32
    pElems: POINTER(win32more.Foundation.PWSTR)
class CAPROPVARIANT(Structure):
    cElems: UInt32
    pElems: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)
class CASCODE(Structure):
    cElems: UInt32
    pElems: POINTER(Int32)
class CAUB(Structure):
    cElems: UInt32
    pElems: c_char_p_no
class CAUH(Structure):
    cElems: UInt32
    pElems: POINTER(win32more.Foundation.ULARGE_INTEGER_head)
class CAUI(Structure):
    cElems: UInt32
    pElems: POINTER(UInt16)
class CAUL(Structure):
    cElems: UInt32
    pElems: POINTER(UInt32)
class CLIPDATA(Structure):
    cbSize: UInt32
    ulClipFmt: Int32
    pClipData: c_char_p_no
class IDirectWriterLock(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0e6d4d92-6738-11cf-96-08-00-aa-00-68-0d-b4')
    @commethod(3)
    def WaitForWriteAccess(dwTimeout: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ReleaseWriteAccess() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def HaveWriteAccess() -> win32more.Foundation.HRESULT: ...
class IEnumSTATPROPSETSTG(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0000013b-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(win32more.System.Com.StructuredStorage.STATPROPSETSTG_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(win32more.System.Com.StructuredStorage.IEnumSTATPROPSETSTG_head)) -> win32more.Foundation.HRESULT: ...
class IEnumSTATPROPSTG(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000139-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(win32more.System.Com.StructuredStorage.STATPROPSTG_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(win32more.System.Com.StructuredStorage.IEnumSTATPROPSTG_head)) -> win32more.Foundation.HRESULT: ...
class IEnumSTATSTG(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0000000d-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(win32more.System.Com.STATSTG_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(win32more.System.Com.StructuredStorage.IEnumSTATSTG_head)) -> win32more.Foundation.HRESULT: ...
class IFillLockBytes(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('99caf010-415e-11cf-88-14-00-aa-00-b5-69-f5')
    @commethod(3)
    def FillAppend(pv: c_void_p, cb: UInt32, pcbWritten: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def FillAt(ulOffset: win32more.Foundation.ULARGE_INTEGER, pv: c_void_p, cb: UInt32, pcbWritten: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetFillSize(ulSize: win32more.Foundation.ULARGE_INTEGER) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Terminate(bCanceled: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
class ILayoutStorage(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0e6d4d90-6738-11cf-96-08-00-aa-00-68-0d-b4')
    @commethod(3)
    def LayoutScript(pStorageLayout: POINTER(win32more.System.Com.StorageLayout_head), nEntries: UInt32, glfInterleavedFlag: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def BeginMonitor() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def EndMonitor() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def ReLayoutDocfile(pwcsNewDfName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def ReLayoutDocfileOnILockBytes(pILockBytes: win32more.System.Com.StructuredStorage.ILockBytes_head) -> win32more.Foundation.HRESULT: ...
class ILockBytes(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0000000a-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def ReadAt(ulOffset: win32more.Foundation.ULARGE_INTEGER, pv: c_void_p, cb: UInt32, pcbRead: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def WriteAt(ulOffset: win32more.Foundation.ULARGE_INTEGER, pv: c_void_p, cb: UInt32, pcbWritten: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Flush() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetSize(cb: win32more.Foundation.ULARGE_INTEGER) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def LockRegion(libOffset: win32more.Foundation.ULARGE_INTEGER, cb: win32more.Foundation.ULARGE_INTEGER, dwLockType: win32more.System.Com.LOCKTYPE) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def UnlockRegion(libOffset: win32more.Foundation.ULARGE_INTEGER, cb: win32more.Foundation.ULARGE_INTEGER, dwLockType: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Stat(pstatstg: POINTER(win32more.System.Com.STATSTG_head), grfStatFlag: win32more.System.Com.STATFLAG) -> win32more.Foundation.HRESULT: ...
class IPersistStorage(c_void_p):
    extends: win32more.System.Com.IPersist
    Guid = Guid('0000010a-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(4)
    def IsDirty() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def InitNew(pStg: win32more.System.Com.StructuredStorage.IStorage_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Load(pStg: win32more.System.Com.StructuredStorage.IStorage_head) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Save(pStgSave: win32more.System.Com.StructuredStorage.IStorage_head, fSameAsLoad: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SaveCompleted(pStgNew: win32more.System.Com.StructuredStorage.IStorage_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def HandsOffStorage() -> win32more.Foundation.HRESULT: ...
class IPropertyBag(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('55272a00-42cb-11ce-81-35-00-aa-00-4b-b8-51')
    @commethod(3)
    def Read(pszPropName: win32more.Foundation.PWSTR, pVar: POINTER(win32more.System.Com.VARIANT_head), pErrorLog: win32more.System.Com.IErrorLog_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Write(pszPropName: win32more.Foundation.PWSTR, pVar: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class IPropertyBag2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('22f55882-280b-11d0-a8-a9-00-a0-c9-0c-20-04')
    @commethod(3)
    def Read(cProperties: UInt32, pPropBag: POINTER(win32more.System.Com.StructuredStorage.PROPBAG2_head), pErrLog: win32more.System.Com.IErrorLog_head, pvarValue: POINTER(win32more.System.Com.VARIANT_head), phrError: POINTER(win32more.Foundation.HRESULT)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Write(cProperties: UInt32, pPropBag: POINTER(win32more.System.Com.StructuredStorage.PROPBAG2_head), pvarValue: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CountProperties(pcProperties: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetPropertyInfo(iProperty: UInt32, cProperties: UInt32, pPropBag: POINTER(win32more.System.Com.StructuredStorage.PROPBAG2_head), pcProperties: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def LoadObject(pstrName: win32more.Foundation.PWSTR, dwHint: UInt32, pUnkObject: win32more.System.Com.IUnknown_head, pErrLog: win32more.System.Com.IErrorLog_head) -> win32more.Foundation.HRESULT: ...
class IPropertySetStorage(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0000013a-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Create(rfmtid: POINTER(Guid), pclsid: POINTER(Guid), grfFlags: UInt32, grfMode: UInt32, ppprstg: POINTER(win32more.System.Com.StructuredStorage.IPropertyStorage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Open(rfmtid: POINTER(Guid), grfMode: UInt32, ppprstg: POINTER(win32more.System.Com.StructuredStorage.IPropertyStorage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Delete(rfmtid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Enum(ppenum: POINTER(win32more.System.Com.StructuredStorage.IEnumSTATPROPSETSTG_head)) -> win32more.Foundation.HRESULT: ...
class IPropertyStorage(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000138-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def ReadMultiple(cpspec: UInt32, rgpspec: POINTER(win32more.System.Com.StructuredStorage.PROPSPEC_head), rgpropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def WriteMultiple(cpspec: UInt32, rgpspec: POINTER(win32more.System.Com.StructuredStorage.PROPSPEC_head), rgpropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), propidNameFirst: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def DeleteMultiple(cpspec: UInt32, rgpspec: POINTER(win32more.System.Com.StructuredStorage.PROPSPEC_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def ReadPropertyNames(cpropid: UInt32, rgpropid: POINTER(UInt32), rglpwstrName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def WritePropertyNames(cpropid: UInt32, rgpropid: POINTER(UInt32), rglpwstrName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def DeletePropertyNames(cpropid: UInt32, rgpropid: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Commit(grfCommitFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Revert() -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Enum(ppenum: POINTER(win32more.System.Com.StructuredStorage.IEnumSTATPROPSTG_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetTimes(pctime: POINTER(win32more.Foundation.FILETIME_head), patime: POINTER(win32more.Foundation.FILETIME_head), pmtime: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SetClass(clsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def Stat(pstatpsstg: POINTER(win32more.System.Com.StructuredStorage.STATPROPSETSTG_head)) -> win32more.Foundation.HRESULT: ...
class IRootStorage(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000012-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def SwitchToFile(pszFile: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class IStorage(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0000000b-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def CreateStream(pwcsName: win32more.Foundation.PWSTR, grfMode: win32more.System.Com.STGM, reserved1: UInt32, reserved2: UInt32, ppstm: POINTER(win32more.System.Com.IStream_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OpenStream(pwcsName: win32more.Foundation.PWSTR, reserved1: c_void_p, grfMode: win32more.System.Com.STGM, reserved2: UInt32, ppstm: POINTER(win32more.System.Com.IStream_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CreateStorage(pwcsName: win32more.Foundation.PWSTR, grfMode: win32more.System.Com.STGM, reserved1: UInt32, reserved2: UInt32, ppstg: POINTER(win32more.System.Com.StructuredStorage.IStorage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def OpenStorage(pwcsName: win32more.Foundation.PWSTR, pstgPriority: win32more.System.Com.StructuredStorage.IStorage_head, grfMode: win32more.System.Com.STGM, snbExclude: POINTER(POINTER(UInt16)), reserved: UInt32, ppstg: POINTER(win32more.System.Com.StructuredStorage.IStorage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def CopyTo(ciidExclude: UInt32, rgiidExclude: POINTER(Guid), snbExclude: POINTER(POINTER(UInt16)), pstgDest: win32more.System.Com.StructuredStorage.IStorage_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def MoveElementTo(pwcsName: win32more.Foundation.PWSTR, pstgDest: win32more.System.Com.StructuredStorage.IStorage_head, pwcsNewName: win32more.Foundation.PWSTR, grfFlags: win32more.System.Com.StructuredStorage.STGMOVE) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Commit(grfCommitFlags: win32more.System.Com.STGC) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Revert() -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def EnumElements(reserved1: UInt32, reserved2: c_void_p, reserved3: UInt32, ppenum: POINTER(win32more.System.Com.StructuredStorage.IEnumSTATSTG_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def DestroyElement(pwcsName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def RenameElement(pwcsOldName: win32more.Foundation.PWSTR, pwcsNewName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetElementTimes(pwcsName: win32more.Foundation.PWSTR, pctime: POINTER(win32more.Foundation.FILETIME_head), patime: POINTER(win32more.Foundation.FILETIME_head), pmtime: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SetClass(clsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SetStateBits(grfStateBits: UInt32, grfMask: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def Stat(pstatstg: POINTER(win32more.System.Com.STATSTG_head), grfStatFlag: win32more.System.Com.STATFLAG) -> win32more.Foundation.HRESULT: ...
class OLESTREAM(Structure):
    lpstbl: POINTER(win32more.System.Com.StructuredStorage.OLESTREAMVTBL_head)
class OLESTREAMVTBL(Structure):
    Get: IntPtr
    Put: IntPtr
PIDMSI_STATUS_VALUE = Int32
PIDMSI_STATUS_NORMAL: PIDMSI_STATUS_VALUE = 0
PIDMSI_STATUS_NEW: PIDMSI_STATUS_VALUE = 1
PIDMSI_STATUS_PRELIM: PIDMSI_STATUS_VALUE = 2
PIDMSI_STATUS_DRAFT: PIDMSI_STATUS_VALUE = 3
PIDMSI_STATUS_INPROGRESS: PIDMSI_STATUS_VALUE = 4
PIDMSI_STATUS_EDIT: PIDMSI_STATUS_VALUE = 5
PIDMSI_STATUS_REVIEW: PIDMSI_STATUS_VALUE = 6
PIDMSI_STATUS_PROOF: PIDMSI_STATUS_VALUE = 7
PIDMSI_STATUS_FINAL: PIDMSI_STATUS_VALUE = 8
PIDMSI_STATUS_OTHER: PIDMSI_STATUS_VALUE = 32767
class PMemoryAllocator(Structure):
    pass
class PROPBAG2(Structure):
    dwType: UInt32
    vt: win32more.System.Com.VARENUM
    cfType: UInt16
    dwHint: UInt32
    pstrName: win32more.Foundation.PWSTR
    clsid: Guid
class PROPSPEC(Structure):
    ulKind: win32more.System.Com.StructuredStorage.PROPSPEC_KIND
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        propid: UInt32
        lpwstr: win32more.Foundation.PWSTR
PROPSPEC_KIND = UInt32
PRSPEC_LPWSTR: PROPSPEC_KIND = 0
PRSPEC_PROPID: PROPSPEC_KIND = 1
class PROPVARIANT(Structure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        decVal: win32more.Foundation.DECIMAL
        class _Anonymous_e__Struct(Structure):
            vt: win32more.System.Com.VARENUM
            wReserved1: UInt16
            wReserved2: UInt16
            wReserved3: UInt16
            Anonymous: _Anonymous_e__Union
            class _Anonymous_e__Union(Union):
                cVal: win32more.Foundation.CHAR
                bVal: Byte
                iVal: Int16
                uiVal: UInt16
                lVal: Int32
                ulVal: UInt32
                intVal: Int32
                uintVal: UInt32
                hVal: win32more.Foundation.LARGE_INTEGER
                uhVal: win32more.Foundation.ULARGE_INTEGER
                fltVal: Single
                dblVal: Double
                boolVal: win32more.Foundation.VARIANT_BOOL
                __OBSOLETE__VARIANT_BOOL: win32more.Foundation.VARIANT_BOOL
                scode: Int32
                cyVal: win32more.System.Com.CY
                date: Double
                filetime: win32more.Foundation.FILETIME
                puuid: POINTER(Guid)
                pclipdata: POINTER(win32more.System.Com.StructuredStorage.CLIPDATA_head)
                bstrVal: win32more.Foundation.BSTR
                bstrblobVal: win32more.System.Com.StructuredStorage.BSTRBLOB
                blob: win32more.System.Com.BLOB
                pszVal: win32more.Foundation.PSTR
                pwszVal: win32more.Foundation.PWSTR
                punkVal: win32more.System.Com.IUnknown_head
                pdispVal: win32more.System.Com.IDispatch_head
                pStream: win32more.System.Com.IStream_head
                pStorage: win32more.System.Com.StructuredStorage.IStorage_head
                pVersionedStream: POINTER(win32more.System.Com.StructuredStorage.VERSIONEDSTREAM_head)
                parray: POINTER(win32more.System.Com.SAFEARRAY_head)
                cac: win32more.System.Com.StructuredStorage.CAC
                caub: win32more.System.Com.StructuredStorage.CAUB
                cai: win32more.System.Com.StructuredStorage.CAI
                caui: win32more.System.Com.StructuredStorage.CAUI
                cal: win32more.System.Com.StructuredStorage.CAL
                caul: win32more.System.Com.StructuredStorage.CAUL
                cah: win32more.System.Com.StructuredStorage.CAH
                cauh: win32more.System.Com.StructuredStorage.CAUH
                caflt: win32more.System.Com.StructuredStorage.CAFLT
                cadbl: win32more.System.Com.StructuredStorage.CADBL
                cabool: win32more.System.Com.StructuredStorage.CABOOL
                cascode: win32more.System.Com.StructuredStorage.CASCODE
                cacy: win32more.System.Com.StructuredStorage.CACY
                cadate: win32more.System.Com.StructuredStorage.CADATE
                cafiletime: win32more.System.Com.StructuredStorage.CAFILETIME
                cauuid: win32more.System.Com.StructuredStorage.CACLSID
                caclipdata: win32more.System.Com.StructuredStorage.CACLIPDATA
                cabstr: win32more.System.Com.StructuredStorage.CABSTR
                cabstrblob: win32more.System.Com.StructuredStorage.CABSTRBLOB
                calpstr: win32more.System.Com.StructuredStorage.CALPSTR
                calpwstr: win32more.System.Com.StructuredStorage.CALPWSTR
                capropvar: win32more.System.Com.StructuredStorage.CAPROPVARIANT
                pcVal: win32more.Foundation.PSTR
                pbVal: c_char_p_no
                piVal: POINTER(Int16)
                puiVal: POINTER(UInt16)
                plVal: POINTER(Int32)
                pulVal: POINTER(UInt32)
                pintVal: POINTER(Int32)
                puintVal: POINTER(UInt32)
                pfltVal: POINTER(Single)
                pdblVal: POINTER(Double)
                pboolVal: POINTER(win32more.Foundation.VARIANT_BOOL)
                pdecVal: POINTER(win32more.Foundation.DECIMAL_head)
                pscode: POINTER(Int32)
                pcyVal: POINTER(win32more.System.Com.CY_head)
                pdate: POINTER(Double)
                pbstrVal: POINTER(win32more.Foundation.BSTR)
                ppunkVal: POINTER(win32more.System.Com.IUnknown_head)
                ppdispVal: POINTER(win32more.System.Com.IDispatch_head)
                pparray: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))
                pvarVal: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)
class RemSNB(Structure):
    ulCntStr: UInt32
    ulCntChar: UInt32
    rgString: Char * 1
class SERIALIZEDPROPERTYVALUE(Structure):
    dwType: UInt32
    rgb: Byte * 1
class STATPROPSETSTG(Structure):
    fmtid: Guid
    clsid: Guid
    grfFlags: UInt32
    mtime: win32more.Foundation.FILETIME
    ctime: win32more.Foundation.FILETIME
    atime: win32more.Foundation.FILETIME
    dwOSVersion: UInt32
class STATPROPSTG(Structure):
    lpwstrName: win32more.Foundation.PWSTR
    propid: UInt32
    vt: win32more.System.Com.VARENUM
STGFMT = UInt32
STGFMT_STORAGE: STGFMT = 0
STGFMT_NATIVE: STGFMT = 1
STGFMT_FILE: STGFMT = 3
STGFMT_ANY: STGFMT = 4
STGFMT_DOCFILE: STGFMT = 5
STGFMT_DOCUMENT: STGFMT = 0
STGMOVE = Int32
STGMOVE_MOVE: STGMOVE = 0
STGMOVE_COPY: STGMOVE = 1
STGMOVE_SHALLOWCOPY: STGMOVE = 2
class STGOPTIONS(Structure):
    usVersion: UInt16
    reserved: UInt16
    ulSectorSize: UInt32
    pwcsTemplateFile: win32more.Foundation.PWSTR
class VERSIONEDSTREAM(Structure):
    guidVersion: Guid
    pStream: win32more.System.Com.IStream_head
make_head(_module, 'BSTRBLOB')
make_head(_module, 'CABOOL')
make_head(_module, 'CABSTR')
make_head(_module, 'CABSTRBLOB')
make_head(_module, 'CAC')
make_head(_module, 'CACLIPDATA')
make_head(_module, 'CACLSID')
make_head(_module, 'CACY')
make_head(_module, 'CADATE')
make_head(_module, 'CADBL')
make_head(_module, 'CAFILETIME')
make_head(_module, 'CAFLT')
make_head(_module, 'CAH')
make_head(_module, 'CAI')
make_head(_module, 'CAL')
make_head(_module, 'CALPSTR')
make_head(_module, 'CALPWSTR')
make_head(_module, 'CAPROPVARIANT')
make_head(_module, 'CASCODE')
make_head(_module, 'CAUB')
make_head(_module, 'CAUH')
make_head(_module, 'CAUI')
make_head(_module, 'CAUL')
make_head(_module, 'CLIPDATA')
make_head(_module, 'IDirectWriterLock')
make_head(_module, 'IEnumSTATPROPSETSTG')
make_head(_module, 'IEnumSTATPROPSTG')
make_head(_module, 'IEnumSTATSTG')
make_head(_module, 'IFillLockBytes')
make_head(_module, 'ILayoutStorage')
make_head(_module, 'ILockBytes')
make_head(_module, 'IPersistStorage')
make_head(_module, 'IPropertyBag')
make_head(_module, 'IPropertyBag2')
make_head(_module, 'IPropertySetStorage')
make_head(_module, 'IPropertyStorage')
make_head(_module, 'IRootStorage')
make_head(_module, 'IStorage')
make_head(_module, 'OLESTREAM')
make_head(_module, 'OLESTREAMVTBL')
make_head(_module, 'PMemoryAllocator')
make_head(_module, 'PROPBAG2')
make_head(_module, 'PROPSPEC')
make_head(_module, 'PROPVARIANT')
make_head(_module, 'RemSNB')
make_head(_module, 'SERIALIZEDPROPERTYVALUE')
make_head(_module, 'STATPROPSETSTG')
make_head(_module, 'STATPROPSTG')
make_head(_module, 'STGOPTIONS')
make_head(_module, 'VERSIONEDSTREAM')
__all__ = [
    "BSTRBLOB",
    "CABOOL",
    "CABSTR",
    "CABSTRBLOB",
    "CAC",
    "CACLIPDATA",
    "CACLSID",
    "CACY",
    "CADATE",
    "CADBL",
    "CAFILETIME",
    "CAFLT",
    "CAH",
    "CAI",
    "CAL",
    "CALPSTR",
    "CALPWSTR",
    "CAPROPVARIANT",
    "CASCODE",
    "CAUB",
    "CAUH",
    "CAUI",
    "CAUL",
    "CCH_MAX_PROPSTG_NAME",
    "CLIPDATA",
    "CWCSTORAGENAME",
    "CoGetInstanceFromFile",
    "CoGetInstanceFromIStorage",
    "CoGetInterfaceAndReleaseStream",
    "CreateILockBytesOnHGlobal",
    "CreateStreamOnHGlobal",
    "FmtIdToPropStgName",
    "FreePropVariantArray",
    "GetConvertStg",
    "GetHGlobalFromILockBytes",
    "GetHGlobalFromStream",
    "IDirectWriterLock",
    "IEnumSTATPROPSETSTG",
    "IEnumSTATPROPSTG",
    "IEnumSTATSTG",
    "IFillLockBytes",
    "ILayoutStorage",
    "ILockBytes",
    "IPersistStorage",
    "IPropertyBag",
    "IPropertyBag2",
    "IPropertySetStorage",
    "IPropertyStorage",
    "IRootStorage",
    "IStorage",
    "OLESTREAM",
    "OLESTREAMVTBL",
    "OleConvertIStorageToOLESTREAM",
    "OleConvertIStorageToOLESTREAMEx",
    "OleConvertOLESTREAMToIStorage",
    "OleConvertOLESTREAMToIStorageEx",
    "PIDDI_THUMBNAIL",
    "PIDDSI_BYTECOUNT",
    "PIDDSI_CATEGORY",
    "PIDDSI_COMPANY",
    "PIDDSI_DOCPARTS",
    "PIDDSI_HEADINGPAIR",
    "PIDDSI_HIDDENCOUNT",
    "PIDDSI_LINECOUNT",
    "PIDDSI_LINKSDIRTY",
    "PIDDSI_MANAGER",
    "PIDDSI_MMCLIPCOUNT",
    "PIDDSI_NOTECOUNT",
    "PIDDSI_PARCOUNT",
    "PIDDSI_PRESFORMAT",
    "PIDDSI_SCALE",
    "PIDDSI_SLIDECOUNT",
    "PIDMSI_COPYRIGHT",
    "PIDMSI_EDITOR",
    "PIDMSI_OWNER",
    "PIDMSI_PRODUCTION",
    "PIDMSI_PROJECT",
    "PIDMSI_RATING",
    "PIDMSI_SEQUENCE_NO",
    "PIDMSI_SOURCE",
    "PIDMSI_STATUS",
    "PIDMSI_STATUS_DRAFT",
    "PIDMSI_STATUS_EDIT",
    "PIDMSI_STATUS_FINAL",
    "PIDMSI_STATUS_INPROGRESS",
    "PIDMSI_STATUS_NEW",
    "PIDMSI_STATUS_NORMAL",
    "PIDMSI_STATUS_OTHER",
    "PIDMSI_STATUS_PRELIM",
    "PIDMSI_STATUS_PROOF",
    "PIDMSI_STATUS_REVIEW",
    "PIDMSI_STATUS_VALUE",
    "PIDMSI_SUPPLIER",
    "PIDSI_APPNAME",
    "PIDSI_AUTHOR",
    "PIDSI_CHARCOUNT",
    "PIDSI_COMMENTS",
    "PIDSI_CREATE_DTM",
    "PIDSI_DOC_SECURITY",
    "PIDSI_EDITTIME",
    "PIDSI_KEYWORDS",
    "PIDSI_LASTAUTHOR",
    "PIDSI_LASTPRINTED",
    "PIDSI_LASTSAVE_DTM",
    "PIDSI_PAGECOUNT",
    "PIDSI_REVNUMBER",
    "PIDSI_SUBJECT",
    "PIDSI_TEMPLATE",
    "PIDSI_THUMBNAIL",
    "PIDSI_TITLE",
    "PIDSI_WORDCOUNT",
    "PID_BEHAVIOR",
    "PID_CODEPAGE",
    "PID_DICTIONARY",
    "PID_FIRST_NAME_DEFAULT",
    "PID_FIRST_USABLE",
    "PID_ILLEGAL",
    "PID_LOCALE",
    "PID_MAX_READONLY",
    "PID_MIN_READONLY",
    "PID_MODIFY_TIME",
    "PID_SECURITY",
    "PMemoryAllocator",
    "PROPBAG2",
    "PROPSETFLAG_ANSI",
    "PROPSETFLAG_CASE_SENSITIVE",
    "PROPSETFLAG_DEFAULT",
    "PROPSETFLAG_NONSIMPLE",
    "PROPSETFLAG_UNBUFFERED",
    "PROPSETHDR_OSVERSION_UNKNOWN",
    "PROPSET_BEHAVIOR_CASE_SENSITIVE",
    "PROPSPEC",
    "PROPSPEC_KIND",
    "PROPVARIANT",
    "PRSPEC_INVALID",
    "PRSPEC_LPWSTR",
    "PRSPEC_PROPID",
    "PropStgNameToFmtId",
    "PropVariantClear",
    "PropVariantCopy",
    "ReadClassStg",
    "ReadClassStm",
    "ReadFmtUserTypeStg",
    "RemSNB",
    "SERIALIZEDPROPERTYVALUE",
    "STATPROPSETSTG",
    "STATPROPSTG",
    "STGFMT",
    "STGFMT_ANY",
    "STGFMT_DOCFILE",
    "STGFMT_DOCUMENT",
    "STGFMT_FILE",
    "STGFMT_NATIVE",
    "STGFMT_STORAGE",
    "STGMOVE",
    "STGMOVE_COPY",
    "STGMOVE_MOVE",
    "STGMOVE_SHALLOWCOPY",
    "STGOPTIONS",
    "STGOPTIONS_VERSION",
    "SetConvertStg",
    "StgConvertPropertyToVariant",
    "StgConvertVariantToProperty",
    "StgCreateDocfile",
    "StgCreateDocfileOnILockBytes",
    "StgCreatePropSetStg",
    "StgCreatePropStg",
    "StgCreateStorageEx",
    "StgDeserializePropVariant",
    "StgGetIFillLockBytesOnFile",
    "StgGetIFillLockBytesOnILockBytes",
    "StgIsStorageFile",
    "StgIsStorageILockBytes",
    "StgOpenAsyncDocfileOnIFillLockBytes",
    "StgOpenLayoutDocfile",
    "StgOpenPropStg",
    "StgOpenStorage",
    "StgOpenStorageEx",
    "StgOpenStorageOnILockBytes",
    "StgPropertyLengthAsVariant",
    "StgSerializePropVariant",
    "StgSetTimes",
    "VERSIONEDSTREAM",
    "WriteClassStg",
    "WriteClassStm",
    "WriteFmtUserTypeStg",
]
_arch_optional = [
]
