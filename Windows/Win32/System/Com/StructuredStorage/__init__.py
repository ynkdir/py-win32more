from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.Security
import Windows.Win32.System.Com
import Windows.Win32.System.Com.StructuredStorage
import Windows.Win32.System.Variant
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
def CoGetInterfaceAndReleaseStream(pStm: Windows.Win32.System.Com.IStream_head, iid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
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
def StgCreateStorageEx(pwcsName: Windows.Win32.Foundation.PWSTR, grfMode: Windows.Win32.System.Com.STGM, stgfmt: Windows.Win32.System.Com.StructuredStorage.STGFMT, grfAttrs: UInt32, pStgOptions: POINTER(Windows.Win32.System.Com.StructuredStorage.STGOPTIONS_head), pSecurityDescriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR, riid: POINTER(Guid), ppObjectOpen: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgOpenStorageEx(pwcsName: Windows.Win32.Foundation.PWSTR, grfMode: Windows.Win32.System.Com.STGM, stgfmt: Windows.Win32.System.Com.StructuredStorage.STGFMT, grfAttrs: UInt32, pStgOptions: POINTER(Windows.Win32.System.Com.StructuredStorage.STGOPTIONS_head), pSecurityDescriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR, riid: POINTER(Guid), ppObjectOpen: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
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
def PropVariantToWinRTPropertyValue(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def WinRTPropertyValueToPropVariant(punkPropertyValue: Windows.Win32.System.Com.IUnknown_head, ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromResource(hinst: Windows.Win32.Foundation.HINSTANCE, id: UInt32, ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromBuffer(pv: VoidPtr, cb: UInt32, ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromCLSID(clsid: POINTER(Guid), ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromGUIDAsString(guid: POINTER(Guid), ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromFileTime(pftIn: POINTER(Windows.Win32.Foundation.FILETIME_head), ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromPropVariantVectorElem(propvarIn: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantVectorFromPropVariant(propvarSingle: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), ppropvarVector: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromBooleanVector(prgf: POINTER(Windows.Win32.Foundation.BOOL), cElems: UInt32, ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromInt16Vector(prgn: POINTER(Int16), cElems: UInt32, ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromUInt16Vector(prgn: POINTER(UInt16), cElems: UInt32, ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromInt32Vector(prgn: POINTER(Int32), cElems: UInt32, ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromUInt32Vector(prgn: POINTER(UInt32), cElems: UInt32, ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromInt64Vector(prgn: POINTER(Int64), cElems: UInt32, ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromUInt64Vector(prgn: POINTER(UInt64), cElems: UInt32, ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromDoubleVector(prgn: POINTER(Double), cElems: UInt32, ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromFileTimeVector(prgft: POINTER(Windows.Win32.Foundation.FILETIME_head), cElems: UInt32, ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromStringVector(prgsz: POINTER(Windows.Win32.Foundation.PWSTR), cElems: UInt32, ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromStringAsVector(psz: Windows.Win32.Foundation.PWSTR, ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToBooleanWithDefault(propvarIn: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), fDefault: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt16WithDefault(propvarIn: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), iDefault: Int16) -> Int16: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt16WithDefault(propvarIn: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), uiDefault: UInt16) -> UInt16: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt32WithDefault(propvarIn: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), lDefault: Int32) -> Int32: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt32WithDefault(propvarIn: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), ulDefault: UInt32) -> UInt32: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt64WithDefault(propvarIn: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), llDefault: Int64) -> Int64: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt64WithDefault(propvarIn: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), ullDefault: UInt64) -> UInt64: ...
@winfunctype('PROPSYS.dll')
def PropVariantToDoubleWithDefault(propvarIn: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), dblDefault: Double) -> Double: ...
@winfunctype('PROPSYS.dll')
def PropVariantToStringWithDefault(propvarIn: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pszDefault: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('PROPSYS.dll')
def PropVariantToBoolean(propvarIn: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pfRet: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt16(propvarIn: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), piRet: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt16(propvarIn: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), puiRet: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt32(propvarIn: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), plRet: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt32(propvarIn: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pulRet: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt64(propvarIn: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pllRet: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt64(propvarIn: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pullRet: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToDouble(propvarIn: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pdblRet: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToBuffer(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pv: VoidPtr, cb: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToString(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), psz: Windows.Win32.Foundation.PWSTR, cch: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToGUID(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pguid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToStringAlloc(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), ppszOut: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToBSTR(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToFileTime(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pstfOut: Windows.Win32.System.Variant.PSTIME_FLAGS, pftOut: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetElementCount(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> UInt32: ...
@winfunctype('PROPSYS.dll')
def PropVariantToBooleanVector(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), prgf: POINTER(Windows.Win32.Foundation.BOOL), crgf: UInt32, pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt16Vector(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), prgn: POINTER(Int16), crgn: UInt32, pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt16Vector(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), prgn: POINTER(UInt16), crgn: UInt32, pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt32Vector(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), prgn: POINTER(Int32), crgn: UInt32, pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt32Vector(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), prgn: POINTER(UInt32), crgn: UInt32, pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt64Vector(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), prgn: POINTER(Int64), crgn: UInt32, pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt64Vector(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), prgn: POINTER(UInt64), crgn: UInt32, pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToDoubleVector(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), prgn: POINTER(Double), crgn: UInt32, pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToFileTimeVector(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), prgft: POINTER(Windows.Win32.Foundation.FILETIME_head), crgft: UInt32, pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToStringVector(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), prgsz: POINTER(Windows.Win32.Foundation.PWSTR), crgsz: UInt32, pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToBooleanVectorAlloc(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pprgf: POINTER(POINTER(Windows.Win32.Foundation.BOOL)), pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt16VectorAlloc(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pprgn: POINTER(POINTER(Int16)), pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt16VectorAlloc(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pprgn: POINTER(POINTER(UInt16)), pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt32VectorAlloc(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pprgn: POINTER(POINTER(Int32)), pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt32VectorAlloc(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pprgn: POINTER(POINTER(UInt32)), pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt64VectorAlloc(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pprgn: POINTER(POINTER(Int64)), pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt64VectorAlloc(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pprgn: POINTER(POINTER(UInt64)), pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToDoubleVectorAlloc(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pprgn: POINTER(POINTER(Double)), pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToFileTimeVectorAlloc(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pprgft: POINTER(POINTER(Windows.Win32.Foundation.FILETIME_head)), pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToStringVectorAlloc(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pprgsz: POINTER(POINTER(Windows.Win32.Foundation.PWSTR)), pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetBooleanElem(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, pfVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetInt16Elem(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, pnVal: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetUInt16Elem(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, pnVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetInt32Elem(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, pnVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetUInt32Elem(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, pnVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetInt64Elem(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, pnVal: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetUInt64Elem(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, pnVal: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetDoubleElem(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, pnVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetFileTimeElem(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, pftVal: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetStringElem(propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), iElem: UInt32, ppszVal: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def ClearPropVariantArray(rgPropVar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), cVars: UInt32) -> Void: ...
@winfunctype('PROPSYS.dll')
def PropVariantCompareEx(propvar1: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), propvar2: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), unit: Windows.Win32.System.Com.StructuredStorage.PROPVAR_COMPARE_UNIT, flags: Windows.Win32.System.Com.StructuredStorage.PROPVAR_COMPARE_FLAGS) -> Int32: ...
@winfunctype('PROPSYS.dll')
def PropVariantChangeType(ppropvarDest: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), propvarSrc: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), flags: Windows.Win32.System.Com.StructuredStorage.PROPVAR_CHANGE_FLAGS, vt: Windows.Win32.System.Variant.VARENUM) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToVariant(pPropVar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), pVar: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToPropVariant(pVar: POINTER(Windows.Win32.System.Variant.VARIANT_head), pPropVar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def StgSerializePropVariant(ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), ppProp: POINTER(POINTER(Windows.Win32.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE_head)), pcb: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def StgDeserializePropVariant(pprop: POINTER(Windows.Win32.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE_head), cbMax: UInt32, ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class BSTRBLOB(EasyCastStructure):
    cbSize: UInt32
    pData: POINTER(Byte)
class CABOOL(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)
class CABSTR(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Windows.Win32.Foundation.BSTR)
class CABSTRBLOB(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Windows.Win32.System.Com.StructuredStorage.BSTRBLOB_head)
class CAC(EasyCastStructure):
    cElems: UInt32
    pElems: Windows.Win32.Foundation.PSTR
class CACLIPDATA(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Windows.Win32.System.Com.StructuredStorage.CLIPDATA_head)
class CACLSID(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Guid)
class CACY(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Windows.Win32.System.Com.CY_head)
class CADATE(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Double)
class CADBL(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Double)
class CAFILETIME(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Windows.Win32.Foundation.FILETIME_head)
class CAFLT(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Single)
class CAH(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Int64)
class CAI(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Int16)
class CAL(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Int32)
class CALPSTR(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Windows.Win32.Foundation.PSTR)
class CALPWSTR(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Windows.Win32.Foundation.PWSTR)
class CAPROPVARIANT(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)
class CASCODE(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Int32)
class CAUB(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Byte)
class CAUH(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(UInt64)
class CAUI(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(UInt16)
class CAUL(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(UInt32)
class CLIPDATA(EasyCastStructure):
    cbSize: UInt32
    ulClipFmt: Int32
    pClipData: POINTER(Byte)
class IDirectWriterLock(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0e6d4d92-6738-11cf-9608-00aa00680db4}')
    @commethod(3)
    def WaitForWriteAccess(self, dwTimeout: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReleaseWriteAccess(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def HaveWriteAccess(self) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumSTATPROPSETSTG(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000013b-0000-0000-c000-000000000046}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(Windows.Win32.System.Com.StructuredStorage.STATPROPSETSTG_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(Windows.Win32.System.Com.StructuredStorage.IEnumSTATPROPSETSTG_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumSTATPROPSTG(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000139-0000-0000-c000-000000000046}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(Windows.Win32.System.Com.StructuredStorage.STATPROPSTG_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(Windows.Win32.System.Com.StructuredStorage.IEnumSTATPROPSTG_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumSTATSTG(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000000d-0000-0000-c000-000000000046}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(Windows.Win32.System.Com.STATSTG_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(Windows.Win32.System.Com.StructuredStorage.IEnumSTATSTG_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFillLockBytes(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{99caf010-415e-11cf-8814-00aa00b569f5}')
    @commethod(3)
    def FillAppend(self, pv: VoidPtr, cb: UInt32, pcbWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FillAt(self, ulOffset: UInt64, pv: VoidPtr, cb: UInt32, pcbWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetFillSize(self, ulSize: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Terminate(self, bCanceled: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class ILayoutStorage(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0e6d4d90-6738-11cf-9608-00aa00680db4}')
    @commethod(3)
    def LayoutScript(self, pStorageLayout: POINTER(Windows.Win32.System.Com.StorageLayout_head), nEntries: UInt32, glfInterleavedFlag: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginMonitor(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EndMonitor(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ReLayoutDocfile(self, pwcsNewDfName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ReLayoutDocfileOnILockBytes(self, pILockBytes: Windows.Win32.System.Com.StructuredStorage.ILockBytes_head) -> Windows.Win32.Foundation.HRESULT: ...
class ILockBytes(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000000a-0000-0000-c000-000000000046}')
    @commethod(3)
    def ReadAt(self, ulOffset: UInt64, pv: VoidPtr, cb: UInt32, pcbRead: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WriteAt(self, ulOffset: UInt64, pv: VoidPtr, cb: UInt32, pcbWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Flush(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetSize(self, cb: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def LockRegion(self, libOffset: UInt64, cb: UInt64, dwLockType: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UnlockRegion(self, libOffset: UInt64, cb: UInt64, dwLockType: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Stat(self, pstatstg: POINTER(Windows.Win32.System.Com.STATSTG_head), grfStatFlag: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IPersistStorage(ComPtr):
    extends: Windows.Win32.System.Com.IPersist
    _iid_ = Guid('{0000010a-0000-0000-c000-000000000046}')
    @commethod(4)
    def IsDirty(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InitNew(self, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Load(self, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Save(self, pStgSave: Windows.Win32.System.Com.StructuredStorage.IStorage_head, fSameAsLoad: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SaveCompleted(self, pStgNew: Windows.Win32.System.Com.StructuredStorage.IStorage_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def HandsOffStorage(self) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyBag(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{55272a00-42cb-11ce-8135-00aa004bb851}')
    @commethod(3)
    def Read(self, pszPropName: Windows.Win32.Foundation.PWSTR, pVar: POINTER(Windows.Win32.System.Variant.VARIANT_head), pErrorLog: Windows.Win32.System.Com.IErrorLog_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Write(self, pszPropName: Windows.Win32.Foundation.PWSTR, pVar: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyBag2(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{22f55882-280b-11d0-a8a9-00a0c90c2004}')
    @commethod(3)
    def Read(self, cProperties: UInt32, pPropBag: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPBAG2_head), pErrLog: Windows.Win32.System.Com.IErrorLog_head, pvarValue: POINTER(Windows.Win32.System.Variant.VARIANT_head), phrError: POINTER(Windows.Win32.Foundation.HRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Write(self, cProperties: UInt32, pPropBag: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPBAG2_head), pvarValue: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CountProperties(self, pcProperties: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPropertyInfo(self, iProperty: UInt32, cProperties: UInt32, pPropBag: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPBAG2_head), pcProperties: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def LoadObject(self, pstrName: Windows.Win32.Foundation.PWSTR, dwHint: UInt32, pUnkObject: Windows.Win32.System.Com.IUnknown_head, pErrLog: Windows.Win32.System.Com.IErrorLog_head) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertySetStorage(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000013a-0000-0000-c000-000000000046}')
    @commethod(3)
    def Create(self, rfmtid: POINTER(Guid), pclsid: POINTER(Guid), grfFlags: UInt32, grfMode: UInt32, ppprstg: POINTER(Windows.Win32.System.Com.StructuredStorage.IPropertyStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Open(self, rfmtid: POINTER(Guid), grfMode: UInt32, ppprstg: POINTER(Windows.Win32.System.Com.StructuredStorage.IPropertyStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Delete(self, rfmtid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Enum(self, ppenum: POINTER(Windows.Win32.System.Com.StructuredStorage.IEnumSTATPROPSETSTG_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyStorage(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000138-0000-0000-c000-000000000046}')
    @commethod(3)
    def ReadMultiple(self, cpspec: UInt32, rgpspec: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPSPEC_head), rgpropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WriteMultiple(self, cpspec: UInt32, rgpspec: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPSPEC_head), rgpropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), propidNameFirst: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DeleteMultiple(self, cpspec: UInt32, rgpspec: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPSPEC_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ReadPropertyNames(self, cpropid: UInt32, rgpropid: POINTER(UInt32), rglpwstrName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def WritePropertyNames(self, cpropid: UInt32, rgpropid: POINTER(UInt32), rglpwstrName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DeletePropertyNames(self, cpropid: UInt32, rgpropid: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Commit(self, grfCommitFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Revert(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Enum(self, ppenum: POINTER(Windows.Win32.System.Com.StructuredStorage.IEnumSTATPROPSTG_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetTimes(self, pctime: POINTER(Windows.Win32.Foundation.FILETIME_head), patime: POINTER(Windows.Win32.Foundation.FILETIME_head), pmtime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetClass(self, clsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Stat(self, pstatpsstg: POINTER(Windows.Win32.System.Com.StructuredStorage.STATPROPSETSTG_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRootStorage(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000012-0000-0000-c000-000000000046}')
    @commethod(3)
    def SwitchToFile(self, pszFile: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IStorage(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000000b-0000-0000-c000-000000000046}')
    @commethod(3)
    def CreateStream(self, pwcsName: Windows.Win32.Foundation.PWSTR, grfMode: Windows.Win32.System.Com.STGM, reserved1: UInt32, reserved2: UInt32, ppstm: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OpenStream(self, pwcsName: Windows.Win32.Foundation.PWSTR, reserved1: VoidPtr, grfMode: Windows.Win32.System.Com.STGM, reserved2: UInt32, ppstm: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateStorage(self, pwcsName: Windows.Win32.Foundation.PWSTR, grfMode: Windows.Win32.System.Com.STGM, reserved1: UInt32, reserved2: UInt32, ppstg: POINTER(Windows.Win32.System.Com.StructuredStorage.IStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OpenStorage(self, pwcsName: Windows.Win32.Foundation.PWSTR, pstgPriority: Windows.Win32.System.Com.StructuredStorage.IStorage_head, grfMode: Windows.Win32.System.Com.STGM, snbExclude: POINTER(POINTER(UInt16)), reserved: UInt32, ppstg: POINTER(Windows.Win32.System.Com.StructuredStorage.IStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CopyTo(self, ciidExclude: UInt32, rgiidExclude: POINTER(Guid), snbExclude: POINTER(POINTER(UInt16)), pstgDest: Windows.Win32.System.Com.StructuredStorage.IStorage_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def MoveElementTo(self, pwcsName: Windows.Win32.Foundation.PWSTR, pstgDest: Windows.Win32.System.Com.StructuredStorage.IStorage_head, pwcsNewName: Windows.Win32.Foundation.PWSTR, grfFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Commit(self, grfCommitFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Revert(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnumElements(self, reserved1: UInt32, reserved2: VoidPtr, reserved3: UInt32, ppenum: POINTER(Windows.Win32.System.Com.StructuredStorage.IEnumSTATSTG_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DestroyElement(self, pwcsName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def RenameElement(self, pwcsOldName: Windows.Win32.Foundation.PWSTR, pwcsNewName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetElementTimes(self, pwcsName: Windows.Win32.Foundation.PWSTR, pctime: POINTER(Windows.Win32.Foundation.FILETIME_head), patime: POINTER(Windows.Win32.Foundation.FILETIME_head), pmtime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetClass(self, clsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetStateBits(self, grfStateBits: UInt32, grfMask: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Stat(self, pstatstg: POINTER(Windows.Win32.System.Com.STATSTG_head), grfStatFlag: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class OLESTREAM(EasyCastStructure):
    lpstbl: POINTER(Windows.Win32.System.Com.StructuredStorage.OLESTREAMVTBL_head)
class OLESTREAMVTBL(EasyCastStructure):
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
class PROPBAG2(EasyCastStructure):
    dwType: UInt32
    vt: Windows.Win32.System.Variant.VARENUM
    cfType: UInt16
    dwHint: UInt32
    pstrName: Windows.Win32.Foundation.PWSTR
    clsid: Guid
class PROPSPEC(EasyCastStructure):
    ulKind: Windows.Win32.System.Com.StructuredStorage.PROPSPEC_KIND
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        propid: UInt32
        lpwstr: Windows.Win32.Foundation.PWSTR
PROPSPEC_KIND = UInt32
PRSPEC_LPWSTR: PROPSPEC_KIND = 0
PRSPEC_PROPID: PROPSPEC_KIND = 1
class PROPVARIANT(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        decVal: Windows.Win32.Foundation.DECIMAL
        class _Anonymous_e__Struct(EasyCastStructure):
            vt: Windows.Win32.System.Variant.VARENUM
            wReserved1: UInt16
            wReserved2: UInt16
            wReserved3: UInt16
            Anonymous: _Anonymous_e__Union
            class _Anonymous_e__Union(EasyCastUnion):
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
                pbVal: POINTER(Byte)
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
PROPVAR_CHANGE_FLAGS = Int32
PVCHF_DEFAULT: PROPVAR_CHANGE_FLAGS = 0
PVCHF_NOVALUEPROP: PROPVAR_CHANGE_FLAGS = 1
PVCHF_ALPHABOOL: PROPVAR_CHANGE_FLAGS = 2
PVCHF_NOUSEROVERRIDE: PROPVAR_CHANGE_FLAGS = 4
PVCHF_LOCALBOOL: PROPVAR_CHANGE_FLAGS = 8
PVCHF_NOHEXSTRING: PROPVAR_CHANGE_FLAGS = 16
PROPVAR_COMPARE_FLAGS = Int32
PVCF_DEFAULT: PROPVAR_COMPARE_FLAGS = 0
PVCF_TREATEMPTYASGREATERTHAN: PROPVAR_COMPARE_FLAGS = 1
PVCF_USESTRCMP: PROPVAR_COMPARE_FLAGS = 2
PVCF_USESTRCMPC: PROPVAR_COMPARE_FLAGS = 4
PVCF_USESTRCMPI: PROPVAR_COMPARE_FLAGS = 8
PVCF_USESTRCMPIC: PROPVAR_COMPARE_FLAGS = 16
PVCF_DIGITSASNUMBERS_CASESENSITIVE: PROPVAR_COMPARE_FLAGS = 32
PROPVAR_COMPARE_UNIT = Int32
PVCU_DEFAULT: PROPVAR_COMPARE_UNIT = 0
PVCU_SECOND: PROPVAR_COMPARE_UNIT = 1
PVCU_MINUTE: PROPVAR_COMPARE_UNIT = 2
PVCU_HOUR: PROPVAR_COMPARE_UNIT = 3
PVCU_DAY: PROPVAR_COMPARE_UNIT = 4
PVCU_MONTH: PROPVAR_COMPARE_UNIT = 5
PVCU_YEAR: PROPVAR_COMPARE_UNIT = 6
class RemSNB(EasyCastStructure):
    ulCntStr: UInt32
    ulCntChar: UInt32
    rgString: Char * 1
class SERIALIZEDPROPERTYVALUE(EasyCastStructure):
    dwType: UInt32
    rgb: Byte * 1
class STATPROPSETSTG(EasyCastStructure):
    fmtid: Guid
    clsid: Guid
    grfFlags: UInt32
    mtime: Windows.Win32.Foundation.FILETIME
    ctime: Windows.Win32.Foundation.FILETIME
    atime: Windows.Win32.Foundation.FILETIME
    dwOSVersion: UInt32
class STATPROPSTG(EasyCastStructure):
    lpwstrName: Windows.Win32.Foundation.PWSTR
    propid: UInt32
    vt: Windows.Win32.System.Variant.VARENUM
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
class STGOPTIONS(EasyCastStructure):
    usVersion: UInt16
    reserved: UInt16
    ulSectorSize: UInt32
    pwcsTemplateFile: Windows.Win32.Foundation.PWSTR
class VERSIONEDSTREAM(EasyCastStructure):
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
make_head(_module, 'PROPBAG2')
make_head(_module, 'PROPSPEC')
make_head(_module, 'PROPVARIANT')
make_head(_module, 'RemSNB')
make_head(_module, 'SERIALIZEDPROPERTYVALUE')
make_head(_module, 'STATPROPSETSTG')
make_head(_module, 'STATPROPSTG')
make_head(_module, 'STGOPTIONS')
make_head(_module, 'VERSIONEDSTREAM')
