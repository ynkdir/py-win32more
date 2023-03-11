from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Security
import Windows.Win32.System.Com
import Windows.Win32.System.Com.StructuredStorage
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
def CoGetInstanceFromFile(pServerInfo: POINTER(Windows.Win32.System.Com.COSERVERINFO_head), pClsid: POINTER(Guid), punkOuter: Windows.Win32.System.Com.IUnknown_head, dwClsCtx: Windows.Win32.System.Com.CLSCTX, grfMode: UInt32, pwszName: Windows.Win32.Foundation.PWSTR, dwCount: UInt32, pResults: POINTER(Windows.Win32.System.Com.MULTI_QI_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetInstanceFromIStorage(pServerInfo: POINTER(Windows.Win32.System.Com.COSERVERINFO_head), pClsid: POINTER(Guid), punkOuter: Windows.Win32.System.Com.IUnknown_head, dwClsCtx: Windows.Win32.System.Com.CLSCTX, pstg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, dwCount: UInt32, pResults: POINTER(Windows.Win32.System.Com.MULTI_QI_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def StgOpenAsyncDocfileOnIFillLockBytes(pflb: Windows.Win32.System.Com.StructuredStorage.IFillLockBytes_head, grfMode: UInt32, asyncFlags: UInt32, ppstgOpen: POINTER(Windows.Win32.System.Com.StructuredStorage.IStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def StgGetIFillLockBytesOnILockBytes(pilb: Windows.Win32.System.Com.StructuredStorage.ILockBytes_head, ppflb: POINTER(Windows.Win32.System.Com.StructuredStorage.IFillLockBytes_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def StgGetIFillLockBytesOnFile(pwcsName: Windows.Win32.Foundation.PWSTR, ppflb: POINTER(Windows.Win32.System.Com.StructuredStorage.IFillLockBytes_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dflayout.dll')
def StgOpenLayoutDocfile(pwcsDfName: Windows.Win32.Foundation.PWSTR, grfMode: UInt32, reserved: UInt32, ppstgOpen: POINTER(Windows.Win32.System.Com.StructuredStorage.IStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreateStreamOnHGlobal(hGlobal: Windows.Win32.Foundation.HGLOBAL, fDeleteOnRelease: Windows.Win32.Foundation.BOOL, ppstm: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def GetHGlobalFromStream(pstm: Windows.Win32.System.Com.IStream_head, phglobal: POINTER(Windows.Win32.Foundation.HGLOBAL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetInterfaceAndReleaseStream(pStm: Windows.Win32.System.Com.IStream_head, iid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def PropVariantCopy(pvarDest: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pvarSrc: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def PropVariantClear(pvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def FreePropVariantArray(cVariants: UInt32, rgvars: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgCreateDocfile(pwcsName: Windows.Win32.Foundation.PWSTR, grfMode: Windows.Win32.System.Com.STGM, reserved: UInt32, ppstgOpen: POINTER(Windows.Win32.System.Com.StructuredStorage.IStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgCreateDocfileOnILockBytes(plkbyt: Windows.Win32.System.Com.StructuredStorage.ILockBytes_head, grfMode: Windows.Win32.System.Com.STGM, reserved: UInt32, ppstgOpen: POINTER(Windows.Win32.System.Com.StructuredStorage.IStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgOpenStorage(pwcsName: Windows.Win32.Foundation.PWSTR, pstgPriority: Windows.Win32.System.Com.StructuredStorage.IStorage_head, grfMode: Windows.Win32.System.Com.STGM, snbExclude: POINTER(POINTER(UInt16)), reserved: UInt32, ppstgOpen: POINTER(Windows.Win32.System.Com.StructuredStorage.IStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgOpenStorageOnILockBytes(plkbyt: Windows.Win32.System.Com.StructuredStorage.ILockBytes_head, pstgPriority: Windows.Win32.System.Com.StructuredStorage.IStorage_head, grfMode: Windows.Win32.System.Com.STGM, snbExclude: POINTER(POINTER(UInt16)), reserved: UInt32, ppstgOpen: POINTER(Windows.Win32.System.Com.StructuredStorage.IStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgIsStorageFile(pwcsName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgIsStorageILockBytes(plkbyt: Windows.Win32.System.Com.StructuredStorage.ILockBytes_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgSetTimes(lpszName: Windows.Win32.Foundation.PWSTR, pctime: POINTER(Windows.Win32.Foundation.FILETIME_head), patime: POINTER(Windows.Win32.Foundation.FILETIME_head), pmtime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgCreateStorageEx(pwcsName: Windows.Win32.Foundation.PWSTR, grfMode: Windows.Win32.System.Com.STGM, stgfmt: Windows.Win32.System.Com.StructuredStorage.STGFMT, grfAttrs: UInt32, pStgOptions: POINTER(Windows.Win32.System.Com.StructuredStorage.STGOPTIONS_head), pSecurityDescriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR, riid: POINTER(Guid), ppObjectOpen: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgOpenStorageEx(pwcsName: Windows.Win32.Foundation.PWSTR, grfMode: Windows.Win32.System.Com.STGM, stgfmt: Windows.Win32.System.Com.StructuredStorage.STGFMT, grfAttrs: UInt32, pStgOptions: POINTER(Windows.Win32.System.Com.StructuredStorage.STGOPTIONS_head), pSecurityDescriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR, riid: POINTER(Guid), ppObjectOpen: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgCreatePropStg(pUnk: Windows.Win32.System.Com.IUnknown_head, fmtid: POINTER(Guid), pclsid: POINTER(Guid), grfFlags: UInt32, dwReserved: UInt32, ppPropStg: POINTER(Windows.Win32.System.Com.StructuredStorage.IPropertyStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgOpenPropStg(pUnk: Windows.Win32.System.Com.IUnknown_head, fmtid: POINTER(Guid), grfFlags: UInt32, dwReserved: UInt32, ppPropStg: POINTER(Windows.Win32.System.Com.StructuredStorage.IPropertyStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgCreatePropSetStg(pStorage: Windows.Win32.System.Com.StructuredStorage.IStorage_head, dwReserved: UInt32, ppPropSetStg: POINTER(Windows.Win32.System.Com.StructuredStorage.IPropertySetStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def FmtIdToPropStgName(pfmtid: POINTER(Guid), oszName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def PropStgNameToFmtId(oszName: Windows.Win32.Foundation.PWSTR, pfmtid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def ReadClassStg(pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, pclsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def WriteClassStg(pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, rclsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def ReadClassStm(pStm: Windows.Win32.System.Com.IStream_head, pclsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def WriteClassStm(pStm: Windows.Win32.System.Com.IStream_head, rclsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def GetHGlobalFromILockBytes(plkbyt: Windows.Win32.System.Com.StructuredStorage.ILockBytes_head, phglobal: POINTER(Windows.Win32.Foundation.HGLOBAL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreateILockBytesOnHGlobal(hGlobal: Windows.Win32.Foundation.HGLOBAL, fDeleteOnRelease: Windows.Win32.Foundation.BOOL, pplkbyt: POINTER(Windows.Win32.System.Com.StructuredStorage.ILockBytes_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def GetConvertStg(pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def StgConvertVariantToProperty(pvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), CodePage: UInt16, pprop: POINTER(Windows.Win32.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE_head), pcb: POINTER(UInt32), pid: UInt32, fReserved: Windows.Win32.Foundation.BOOLEAN, pcIndirect: POINTER(UInt32)) -> POINTER(Windows.Win32.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE_head): ...
@winfunctype('ole32.dll')
def StgConvertPropertyToVariant(pprop: POINTER(Windows.Win32.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE_head), CodePage: UInt16, pvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pma: POINTER(Windows.Win32.System.Com.StructuredStorage.PMemoryAllocator_head)) -> Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('ole32.dll')
def StgPropertyLengthAsVariant(pProp: POINTER(Windows.Win32.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE_head), cbProp: UInt32, CodePage: UInt16, bReserved: Byte) -> UInt32: ...
@winfunctype('OLE32.dll')
def WriteFmtUserTypeStg(pstg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, cf: UInt16, lpszUserType: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def ReadFmtUserTypeStg(pstg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, pcf: POINTER(UInt16), lplpszUserType: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleConvertOLESTREAMToIStorage(lpolestream: POINTER(Windows.Win32.System.Com.StructuredStorage.OLESTREAM_head), pstg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ptd: POINTER(Windows.Win32.System.Com.DVTARGETDEVICE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleConvertIStorageToOLESTREAM(pstg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, lpolestream: POINTER(Windows.Win32.System.Com.StructuredStorage.OLESTREAM_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def SetConvertStg(pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, fConvert: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleConvertIStorageToOLESTREAMEx(pstg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, cfFormat: UInt16, lWidth: Int32, lHeight: Int32, dwSize: UInt32, pmedium: POINTER(Windows.Win32.System.Com.STGMEDIUM_head), polestm: POINTER(Windows.Win32.System.Com.StructuredStorage.OLESTREAM_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleConvertOLESTREAMToIStorageEx(polestm: POINTER(Windows.Win32.System.Com.StructuredStorage.OLESTREAM_head), pstg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, pcfFormat: POINTER(UInt16), plwWidth: POINTER(Int32), plHeight: POINTER(Int32), pdwSize: POINTER(UInt32), pmedium: POINTER(Windows.Win32.System.Com.STGMEDIUM_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def StgSerializePropVariant(ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), ppProp: POINTER(POINTER(Windows.Win32.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE_head)), pcb: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def StgDeserializePropVariant(pprop: POINTER(Windows.Win32.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE_head), cbMax: UInt32, ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class BSTRBLOB(Structure):
    cbSize: UInt32
    pData: c_char_p_no
class CABOOL(Structure):
    cElems: UInt32
    pElems: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)
class CABSTR(Structure):
    cElems: UInt32
    pElems: POINTER(Windows.Win32.Foundation.BSTR)
class CABSTRBLOB(Structure):
    cElems: UInt32
    pElems: POINTER(Windows.Win32.System.Com.StructuredStorage.BSTRBLOB_head)
class CAC(Structure):
    cElems: UInt32
    pElems: Windows.Win32.Foundation.PSTR
class CACLIPDATA(Structure):
    cElems: UInt32
    pElems: POINTER(Windows.Win32.System.Com.StructuredStorage.CLIPDATA_head)
class CACLSID(Structure):
    cElems: UInt32
    pElems: POINTER(Guid)
class CACY(Structure):
    cElems: UInt32
    pElems: POINTER(Windows.Win32.System.Com.CY_head)
class CADATE(Structure):
    cElems: UInt32
    pElems: POINTER(Double)
class CADBL(Structure):
    cElems: UInt32
    pElems: POINTER(Double)
class CAFILETIME(Structure):
    cElems: UInt32
    pElems: POINTER(Windows.Win32.Foundation.FILETIME_head)
class CAFLT(Structure):
    cElems: UInt32
    pElems: POINTER(Single)
class CAH(Structure):
    cElems: UInt32
    pElems: POINTER(Int64)
class CAI(Structure):
    cElems: UInt32
    pElems: POINTER(Int16)
class CAL(Structure):
    cElems: UInt32
    pElems: POINTER(Int32)
class CALPSTR(Structure):
    cElems: UInt32
    pElems: POINTER(Windows.Win32.Foundation.PSTR)
class CALPWSTR(Structure):
    cElems: UInt32
    pElems: POINTER(Windows.Win32.Foundation.PWSTR)
class CAPROPVARIANT(Structure):
    cElems: UInt32
    pElems: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)
class CASCODE(Structure):
    cElems: UInt32
    pElems: POINTER(Int32)
class CAUB(Structure):
    cElems: UInt32
    pElems: c_char_p_no
class CAUH(Structure):
    cElems: UInt32
    pElems: POINTER(UInt64)
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
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0e6d4d92-6738-11cf-96-08-00-aa-00-68-0d-b4')
    @commethod(3)
    def WaitForWriteAccess(dwTimeout: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReleaseWriteAccess() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def HaveWriteAccess() -> Windows.Win32.Foundation.HRESULT: ...
class IEnumSTATPROPSETSTG(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0000013b-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(Windows.Win32.System.Com.StructuredStorage.STATPROPSETSTG_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(Windows.Win32.System.Com.StructuredStorage.IEnumSTATPROPSETSTG_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumSTATPROPSTG(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('00000139-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(Windows.Win32.System.Com.StructuredStorage.STATPROPSTG_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(Windows.Win32.System.Com.StructuredStorage.IEnumSTATPROPSTG_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumSTATSTG(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0000000d-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(Windows.Win32.System.Com.STATSTG_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(Windows.Win32.System.Com.StructuredStorage.IEnumSTATSTG_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFillLockBytes(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('99caf010-415e-11cf-88-14-00-aa-00-b5-69-f5')
    @commethod(3)
    def FillAppend(pv: c_void_p, cb: UInt32, pcbWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FillAt(ulOffset: UInt64, pv: c_void_p, cb: UInt32, pcbWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetFillSize(ulSize: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Terminate(bCanceled: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class ILayoutStorage(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0e6d4d90-6738-11cf-96-08-00-aa-00-68-0d-b4')
    @commethod(3)
    def LayoutScript(pStorageLayout: POINTER(Windows.Win32.System.Com.StorageLayout_head), nEntries: UInt32, glfInterleavedFlag: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginMonitor() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EndMonitor() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ReLayoutDocfile(pwcsNewDfName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ReLayoutDocfileOnILockBytes(pILockBytes: Windows.Win32.System.Com.StructuredStorage.ILockBytes_head) -> Windows.Win32.Foundation.HRESULT: ...
class ILockBytes(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0000000a-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def ReadAt(ulOffset: UInt64, pv: c_void_p, cb: UInt32, pcbRead: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WriteAt(ulOffset: UInt64, pv: c_void_p, cb: UInt32, pcbWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Flush() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetSize(cb: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def LockRegion(libOffset: UInt64, cb: UInt64, dwLockType: Windows.Win32.System.Com.LOCKTYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UnlockRegion(libOffset: UInt64, cb: UInt64, dwLockType: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Stat(pstatstg: POINTER(Windows.Win32.System.Com.STATSTG_head), grfStatFlag: Windows.Win32.System.Com.STATFLAG) -> Windows.Win32.Foundation.HRESULT: ...
class IPersistStorage(c_void_p):
    extends: Windows.Win32.System.Com.IPersist
    Guid = Guid('0000010a-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(4)
    def IsDirty() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InitNew(pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Load(pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Save(pStgSave: Windows.Win32.System.Com.StructuredStorage.IStorage_head, fSameAsLoad: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SaveCompleted(pStgNew: Windows.Win32.System.Com.StructuredStorage.IStorage_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def HandsOffStorage() -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyBag(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('55272a00-42cb-11ce-81-35-00-aa-00-4b-b8-51')
    @commethod(3)
    def Read(pszPropName: Windows.Win32.Foundation.PWSTR, pVar: POINTER(Windows.Win32.System.Com.VARIANT_head), pErrorLog: Windows.Win32.System.Com.IErrorLog_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Write(pszPropName: Windows.Win32.Foundation.PWSTR, pVar: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyBag2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('22f55882-280b-11d0-a8-a9-00-a0-c9-0c-20-04')
    @commethod(3)
    def Read(cProperties: UInt32, pPropBag: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPBAG2_head), pErrLog: Windows.Win32.System.Com.IErrorLog_head, pvarValue: POINTER(Windows.Win32.System.Com.VARIANT_head), phrError: POINTER(Windows.Win32.Foundation.HRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Write(cProperties: UInt32, pPropBag: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPBAG2_head), pvarValue: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CountProperties(pcProperties: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPropertyInfo(iProperty: UInt32, cProperties: UInt32, pPropBag: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPBAG2_head), pcProperties: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def LoadObject(pstrName: Windows.Win32.Foundation.PWSTR, dwHint: UInt32, pUnkObject: Windows.Win32.System.Com.IUnknown_head, pErrLog: Windows.Win32.System.Com.IErrorLog_head) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertySetStorage(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0000013a-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Create(rfmtid: POINTER(Guid), pclsid: POINTER(Guid), grfFlags: UInt32, grfMode: UInt32, ppprstg: POINTER(Windows.Win32.System.Com.StructuredStorage.IPropertyStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Open(rfmtid: POINTER(Guid), grfMode: UInt32, ppprstg: POINTER(Windows.Win32.System.Com.StructuredStorage.IPropertyStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Delete(rfmtid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Enum(ppenum: POINTER(Windows.Win32.System.Com.StructuredStorage.IEnumSTATPROPSETSTG_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyStorage(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('00000138-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def ReadMultiple(cpspec: UInt32, rgpspec: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPSPEC_head), rgpropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WriteMultiple(cpspec: UInt32, rgpspec: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPSPEC_head), rgpropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), propidNameFirst: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DeleteMultiple(cpspec: UInt32, rgpspec: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPSPEC_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ReadPropertyNames(cpropid: UInt32, rgpropid: POINTER(UInt32), rglpwstrName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def WritePropertyNames(cpropid: UInt32, rgpropid: POINTER(UInt32), rglpwstrName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DeletePropertyNames(cpropid: UInt32, rgpropid: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Commit(grfCommitFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Revert() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Enum(ppenum: POINTER(Windows.Win32.System.Com.StructuredStorage.IEnumSTATPROPSTG_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetTimes(pctime: POINTER(Windows.Win32.Foundation.FILETIME_head), patime: POINTER(Windows.Win32.Foundation.FILETIME_head), pmtime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetClass(clsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Stat(pstatpsstg: POINTER(Windows.Win32.System.Com.StructuredStorage.STATPROPSETSTG_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRootStorage(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('00000012-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def SwitchToFile(pszFile: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IStorage(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0000000b-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def CreateStream(pwcsName: Windows.Win32.Foundation.PWSTR, grfMode: Windows.Win32.System.Com.STGM, reserved1: UInt32, reserved2: UInt32, ppstm: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OpenStream(pwcsName: Windows.Win32.Foundation.PWSTR, reserved1: c_void_p, grfMode: Windows.Win32.System.Com.STGM, reserved2: UInt32, ppstm: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateStorage(pwcsName: Windows.Win32.Foundation.PWSTR, grfMode: Windows.Win32.System.Com.STGM, reserved1: UInt32, reserved2: UInt32, ppstg: POINTER(Windows.Win32.System.Com.StructuredStorage.IStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OpenStorage(pwcsName: Windows.Win32.Foundation.PWSTR, pstgPriority: Windows.Win32.System.Com.StructuredStorage.IStorage_head, grfMode: Windows.Win32.System.Com.STGM, snbExclude: POINTER(POINTER(UInt16)), reserved: UInt32, ppstg: POINTER(Windows.Win32.System.Com.StructuredStorage.IStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CopyTo(ciidExclude: UInt32, rgiidExclude: POINTER(Guid), snbExclude: POINTER(POINTER(UInt16)), pstgDest: Windows.Win32.System.Com.StructuredStorage.IStorage_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def MoveElementTo(pwcsName: Windows.Win32.Foundation.PWSTR, pstgDest: Windows.Win32.System.Com.StructuredStorage.IStorage_head, pwcsNewName: Windows.Win32.Foundation.PWSTR, grfFlags: Windows.Win32.System.Com.StructuredStorage.STGMOVE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Commit(grfCommitFlags: Windows.Win32.System.Com.STGC) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Revert() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnumElements(reserved1: UInt32, reserved2: c_void_p, reserved3: UInt32, ppenum: POINTER(Windows.Win32.System.Com.StructuredStorage.IEnumSTATSTG_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DestroyElement(pwcsName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def RenameElement(pwcsOldName: Windows.Win32.Foundation.PWSTR, pwcsNewName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetElementTimes(pwcsName: Windows.Win32.Foundation.PWSTR, pctime: POINTER(Windows.Win32.Foundation.FILETIME_head), patime: POINTER(Windows.Win32.Foundation.FILETIME_head), pmtime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetClass(clsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetStateBits(grfStateBits: UInt32, grfMask: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Stat(pstatstg: POINTER(Windows.Win32.System.Com.STATSTG_head), grfStatFlag: Windows.Win32.System.Com.STATFLAG) -> Windows.Win32.Foundation.HRESULT: ...
class OLESTREAM(Structure):
    lpstbl: POINTER(Windows.Win32.System.Com.StructuredStorage.OLESTREAMVTBL_head)
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
    vt: Windows.Win32.System.Com.VARENUM
    cfType: UInt16
    dwHint: UInt32
    pstrName: Windows.Win32.Foundation.PWSTR
    clsid: Guid
class PROPSPEC(Structure):
    ulKind: Windows.Win32.System.Com.StructuredStorage.PROPSPEC_KIND
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        propid: UInt32
        lpwstr: Windows.Win32.Foundation.PWSTR
PROPSPEC_KIND = UInt32
PRSPEC_LPWSTR: PROPSPEC_KIND = 0
PRSPEC_PROPID: PROPSPEC_KIND = 1
class PROPVARIANT(Structure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        decVal: Windows.Win32.Foundation.DECIMAL
        class _Anonymous_e__Struct(Structure):
            vt: Windows.Win32.System.Com.VARENUM
            wReserved1: UInt16
            wReserved2: UInt16
            wReserved3: UInt16
            Anonymous: _Anonymous_e__Union
            class _Anonymous_e__Union(Union):
                cVal: Windows.Win32.Foundation.CHAR
                bVal: Byte
                iVal: Int16
                uiVal: UInt16
                lVal: Int32
                ulVal: UInt32
                intVal: Int32
                uintVal: UInt32
                hVal: Int64
                uhVal: UInt64
                fltVal: Single
                dblVal: Double
                boolVal: Windows.Win32.Foundation.VARIANT_BOOL
                __OBSOLETE__VARIANT_BOOL: Windows.Win32.Foundation.VARIANT_BOOL
                scode: Int32
                cyVal: Windows.Win32.System.Com.CY
                date: Double
                filetime: Windows.Win32.Foundation.FILETIME
                puuid: POINTER(Guid)
                pclipdata: POINTER(Windows.Win32.System.Com.StructuredStorage.CLIPDATA_head)
                bstrVal: Windows.Win32.Foundation.BSTR
                bstrblobVal: Windows.Win32.System.Com.StructuredStorage.BSTRBLOB
                blob: Windows.Win32.System.Com.BLOB
                pszVal: Windows.Win32.Foundation.PSTR
                pwszVal: Windows.Win32.Foundation.PWSTR
                punkVal: Windows.Win32.System.Com.IUnknown_head
                pdispVal: Windows.Win32.System.Com.IDispatch_head
                pStream: Windows.Win32.System.Com.IStream_head
                pStorage: Windows.Win32.System.Com.StructuredStorage.IStorage_head
                pVersionedStream: POINTER(Windows.Win32.System.Com.StructuredStorage.VERSIONEDSTREAM_head)
                parray: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)
                cac: Windows.Win32.System.Com.StructuredStorage.CAC
                caub: Windows.Win32.System.Com.StructuredStorage.CAUB
                cai: Windows.Win32.System.Com.StructuredStorage.CAI
                caui: Windows.Win32.System.Com.StructuredStorage.CAUI
                cal: Windows.Win32.System.Com.StructuredStorage.CAL
                caul: Windows.Win32.System.Com.StructuredStorage.CAUL
                cah: Windows.Win32.System.Com.StructuredStorage.CAH
                cauh: Windows.Win32.System.Com.StructuredStorage.CAUH
                caflt: Windows.Win32.System.Com.StructuredStorage.CAFLT
                cadbl: Windows.Win32.System.Com.StructuredStorage.CADBL
                cabool: Windows.Win32.System.Com.StructuredStorage.CABOOL
                cascode: Windows.Win32.System.Com.StructuredStorage.CASCODE
                cacy: Windows.Win32.System.Com.StructuredStorage.CACY
                cadate: Windows.Win32.System.Com.StructuredStorage.CADATE
                cafiletime: Windows.Win32.System.Com.StructuredStorage.CAFILETIME
                cauuid: Windows.Win32.System.Com.StructuredStorage.CACLSID
                caclipdata: Windows.Win32.System.Com.StructuredStorage.CACLIPDATA
                cabstr: Windows.Win32.System.Com.StructuredStorage.CABSTR
                cabstrblob: Windows.Win32.System.Com.StructuredStorage.CABSTRBLOB
                calpstr: Windows.Win32.System.Com.StructuredStorage.CALPSTR
                calpwstr: Windows.Win32.System.Com.StructuredStorage.CALPWSTR
                capropvar: Windows.Win32.System.Com.StructuredStorage.CAPROPVARIANT
                pcVal: Windows.Win32.Foundation.PSTR
                pbVal: c_char_p_no
                piVal: POINTER(Int16)
                puiVal: POINTER(UInt16)
                plVal: POINTER(Int32)
                pulVal: POINTER(UInt32)
                pintVal: POINTER(Int32)
                puintVal: POINTER(UInt32)
                pfltVal: POINTER(Single)
                pdblVal: POINTER(Double)
                pboolVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)
                pdecVal: POINTER(Windows.Win32.Foundation.DECIMAL_head)
                pscode: POINTER(Int32)
                pcyVal: POINTER(Windows.Win32.System.Com.CY_head)
                pdate: POINTER(Double)
                pbstrVal: POINTER(Windows.Win32.Foundation.BSTR)
                ppunkVal: POINTER(Windows.Win32.System.Com.IUnknown_head)
                ppdispVal: POINTER(Windows.Win32.System.Com.IDispatch_head)
                pparray: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))
                pvarVal: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)
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
    mtime: Windows.Win32.Foundation.FILETIME
    ctime: Windows.Win32.Foundation.FILETIME
    atime: Windows.Win32.Foundation.FILETIME
    dwOSVersion: UInt32
class STATPROPSTG(Structure):
    lpwstrName: Windows.Win32.Foundation.PWSTR
    propid: UInt32
    vt: Windows.Win32.System.Com.VARENUM
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
    pwcsTemplateFile: Windows.Win32.Foundation.PWSTR
class VERSIONEDSTREAM(Structure):
    guidVersion: Guid
    pStream: Windows.Win32.System.Com.IStream_head
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
