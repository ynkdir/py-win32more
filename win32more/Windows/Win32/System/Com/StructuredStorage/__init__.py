from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.StructuredStorage
import win32more.Windows.Win32.System.Variant
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
def CoGetInstanceFromFile(pServerInfo: POINTER(win32more.Windows.Win32.System.Com.COSERVERINFO), pClsid: POINTER(Guid), punkOuter: win32more.Windows.Win32.System.Com.IUnknown, dwClsCtx: win32more.Windows.Win32.System.Com.CLSCTX, grfMode: UInt32, pwszName: win32more.Windows.Win32.Foundation.PWSTR, dwCount: UInt32, pResults: POINTER(win32more.Windows.Win32.System.Com.MULTI_QI)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetInstanceFromIStorage(pServerInfo: POINTER(win32more.Windows.Win32.System.Com.COSERVERINFO), pClsid: POINTER(Guid), punkOuter: win32more.Windows.Win32.System.Com.IUnknown, dwClsCtx: win32more.Windows.Win32.System.Com.CLSCTX, pstg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, dwCount: UInt32, pResults: POINTER(win32more.Windows.Win32.System.Com.MULTI_QI)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def StgOpenAsyncDocfileOnIFillLockBytes(pflb: win32more.Windows.Win32.System.Com.StructuredStorage.IFillLockBytes, grfMode: UInt32, asyncFlags: UInt32, ppstgOpen: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def StgGetIFillLockBytesOnILockBytes(pilb: win32more.Windows.Win32.System.Com.StructuredStorage.ILockBytes, ppflb: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IFillLockBytes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def StgGetIFillLockBytesOnFile(pwcsName: win32more.Windows.Win32.Foundation.PWSTR, ppflb: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IFillLockBytes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dflayout.dll')
def StgOpenLayoutDocfile(pwcsDfName: win32more.Windows.Win32.Foundation.PWSTR, grfMode: UInt32, reserved: UInt32, ppstgOpen: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreateStreamOnHGlobal(hGlobal: win32more.Windows.Win32.Foundation.HGLOBAL, fDeleteOnRelease: win32more.Windows.Win32.Foundation.BOOL, ppstm: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def GetHGlobalFromStream(pstm: win32more.Windows.Win32.System.Com.IStream, phglobal: POINTER(win32more.Windows.Win32.Foundation.HGLOBAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetInterfaceAndReleaseStream(pStm: win32more.Windows.Win32.System.Com.IStream, iid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def PropVariantCopy(pvarDest: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pvarSrc: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def PropVariantClear(pvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def FreePropVariantArray(cVariants: UInt32, rgvars: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgCreateDocfile(pwcsName: win32more.Windows.Win32.Foundation.PWSTR, grfMode: win32more.Windows.Win32.System.Com.STGM, reserved: UInt32, ppstgOpen: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgCreateDocfileOnILockBytes(plkbyt: win32more.Windows.Win32.System.Com.StructuredStorage.ILockBytes, grfMode: win32more.Windows.Win32.System.Com.STGM, reserved: UInt32, ppstgOpen: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgOpenStorage(pwcsName: win32more.Windows.Win32.Foundation.PWSTR, pstgPriority: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, grfMode: win32more.Windows.Win32.System.Com.STGM, snbExclude: POINTER(POINTER(UInt16)), reserved: UInt32, ppstgOpen: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgOpenStorageOnILockBytes(plkbyt: win32more.Windows.Win32.System.Com.StructuredStorage.ILockBytes, pstgPriority: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, grfMode: win32more.Windows.Win32.System.Com.STGM, snbExclude: POINTER(POINTER(UInt16)), reserved: UInt32, ppstgOpen: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgIsStorageFile(pwcsName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgIsStorageILockBytes(plkbyt: win32more.Windows.Win32.System.Com.StructuredStorage.ILockBytes) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgSetTimes(lpszName: win32more.Windows.Win32.Foundation.PWSTR, pctime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), patime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), pmtime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgCreateStorageEx(pwcsName: win32more.Windows.Win32.Foundation.PWSTR, grfMode: win32more.Windows.Win32.System.Com.STGM, stgfmt: win32more.Windows.Win32.System.Com.StructuredStorage.STGFMT, grfAttrs: UInt32, pStgOptions: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.STGOPTIONS), pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, riid: POINTER(Guid), ppObjectOpen: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgOpenStorageEx(pwcsName: win32more.Windows.Win32.Foundation.PWSTR, grfMode: win32more.Windows.Win32.System.Com.STGM, stgfmt: win32more.Windows.Win32.System.Com.StructuredStorage.STGFMT, grfAttrs: UInt32, pStgOptions: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.STGOPTIONS), pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR, riid: POINTER(Guid), ppObjectOpen: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgCreatePropStg(pUnk: win32more.Windows.Win32.System.Com.IUnknown, fmtid: POINTER(Guid), pclsid: POINTER(Guid), grfFlags: UInt32, dwReserved: UInt32, ppPropStg: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgOpenPropStg(pUnk: win32more.Windows.Win32.System.Com.IUnknown, fmtid: POINTER(Guid), grfFlags: UInt32, dwReserved: UInt32, ppPropStg: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StgCreatePropSetStg(pStorage: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, dwReserved: UInt32, ppPropSetStg: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IPropertySetStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def FmtIdToPropStgName(pfmtid: POINTER(Guid), oszName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def PropStgNameToFmtId(oszName: win32more.Windows.Win32.Foundation.PWSTR, pfmtid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def ReadClassStg(pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, pclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def WriteClassStg(pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, rclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def ReadClassStm(pStm: win32more.Windows.Win32.System.Com.IStream, pclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def WriteClassStm(pStm: win32more.Windows.Win32.System.Com.IStream, rclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def GetHGlobalFromILockBytes(plkbyt: win32more.Windows.Win32.System.Com.StructuredStorage.ILockBytes, phglobal: POINTER(win32more.Windows.Win32.Foundation.HGLOBAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreateILockBytesOnHGlobal(hGlobal: win32more.Windows.Win32.Foundation.HGLOBAL, fDeleteOnRelease: win32more.Windows.Win32.Foundation.BOOL, pplkbyt: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.ILockBytes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def GetConvertStg(pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def StgConvertVariantToProperty(pvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), CodePage: UInt16, pprop: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE), pcb: POINTER(UInt32), pid: UInt32, fReserved: win32more.Windows.Win32.Foundation.BOOLEAN, pcIndirect: POINTER(UInt32)) -> POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE): ...
@winfunctype('ole32.dll')
def StgConvertPropertyToVariant(pprop: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE), CodePage: UInt16, pvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pma: win32more.Windows.Win32.System.Com.StructuredStorage.IMemoryAllocator) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('ole32.dll')
def StgPropertyLengthAsVariant(pProp: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE), cbProp: UInt32, CodePage: UInt16, bReserved: Byte) -> UInt32: ...
@winfunctype('OLE32.dll')
def WriteFmtUserTypeStg(pstg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, cf: UInt16, lpszUserType: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def ReadFmtUserTypeStg(pstg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, pcf: POINTER(UInt16), lplpszUserType: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleConvertOLESTREAMToIStorage(lpolestream: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.OLESTREAM), pstg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, ptd: POINTER(win32more.Windows.Win32.System.Com.DVTARGETDEVICE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleConvertIStorageToOLESTREAM(pstg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, lpolestream: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.OLESTREAM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def SetConvertStg(pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, fConvert: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleConvertIStorageToOLESTREAMEx(pstg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, cfFormat: UInt16, lWidth: Int32, lHeight: Int32, dwSize: UInt32, pmedium: POINTER(win32more.Windows.Win32.System.Com.STGMEDIUM), polestm: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.OLESTREAM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleConvertOLESTREAMToIStorageEx(polestm: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.OLESTREAM), pstg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, pcfFormat: POINTER(UInt16), plwWidth: POINTER(Int32), plHeight: POINTER(Int32), pdwSize: POINTER(UInt32), pmedium: POINTER(win32more.Windows.Win32.System.Com.STGMEDIUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToWinRTPropertyValue(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def WinRTPropertyValueToPropVariant(punkPropertyValue: win32more.Windows.Win32.System.Com.IUnknown, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromResource(hinst: win32more.Windows.Win32.Foundation.HINSTANCE, id: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromBuffer(pv: VoidPtr, cb: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromCLSID(clsid: POINTER(Guid), ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromGUIDAsString(guid: POINTER(Guid), ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromFileTime(pftIn: POINTER(win32more.Windows.Win32.Foundation.FILETIME), ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromPropVariantVectorElem(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), iElem: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantVectorFromPropVariant(propvarSingle: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), ppropvarVector: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromBooleanVector(prgf: POINTER(win32more.Windows.Win32.Foundation.BOOL), cElems: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromInt16Vector(prgn: POINTER(Int16), cElems: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromUInt16Vector(prgn: POINTER(UInt16), cElems: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromInt32Vector(prgn: POINTER(Int32), cElems: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromUInt32Vector(prgn: POINTER(UInt32), cElems: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromInt64Vector(prgn: POINTER(Int64), cElems: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromUInt64Vector(prgn: POINTER(UInt64), cElems: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromDoubleVector(prgn: POINTER(Double), cElems: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromFileTimeVector(prgft: POINTER(win32more.Windows.Win32.Foundation.FILETIME), cElems: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromStringVector(prgsz: POINTER(win32more.Windows.Win32.Foundation.PWSTR), cElems: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitPropVariantFromStringAsVector(psz: win32more.Windows.Win32.Foundation.PWSTR, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToBooleanWithDefault(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), fDefault: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt16WithDefault(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), iDefault: Int16) -> Int16: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt16WithDefault(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), uiDefault: UInt16) -> UInt16: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt32WithDefault(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), lDefault: Int32) -> Int32: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt32WithDefault(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), ulDefault: UInt32) -> UInt32: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt64WithDefault(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), llDefault: Int64) -> Int64: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt64WithDefault(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), ullDefault: UInt64) -> UInt64: ...
@winfunctype('PROPSYS.dll')
def PropVariantToDoubleWithDefault(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), dblDefault: Double) -> Double: ...
@winfunctype('PROPSYS.dll')
def PropVariantToStringWithDefault(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pszDefault: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.PWSTR: ...
@winfunctype('PROPSYS.dll')
def PropVariantToBoolean(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pfRet: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt16(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), piRet: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt16(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), puiRet: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt32(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), plRet: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt32(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pulRet: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt64(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pllRet: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt64(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pullRet: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToDouble(propvarIn: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pdblRet: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToBuffer(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pv: VoidPtr, cb: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToString(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), psz: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToGUID(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pguid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToStringAlloc(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), ppszOut: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToBSTR(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pbstrOut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToFileTime(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pstfOut: win32more.Windows.Win32.System.Variant.PSTIME_FLAGS, pftOut: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetElementCount(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> UInt32: ...
@winfunctype('PROPSYS.dll')
def PropVariantToBooleanVector(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), prgf: POINTER(win32more.Windows.Win32.Foundation.BOOL), crgf: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt16Vector(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), prgn: POINTER(Int16), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt16Vector(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), prgn: POINTER(UInt16), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt32Vector(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), prgn: POINTER(Int32), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt32Vector(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), prgn: POINTER(UInt32), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt64Vector(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), prgn: POINTER(Int64), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt64Vector(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), prgn: POINTER(UInt64), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToDoubleVector(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), prgn: POINTER(Double), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToFileTimeVector(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), prgft: POINTER(win32more.Windows.Win32.Foundation.FILETIME), crgft: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToStringVector(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), prgsz: POINTER(win32more.Windows.Win32.Foundation.PWSTR), crgsz: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToBooleanVectorAlloc(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pprgf: POINTER(POINTER(win32more.Windows.Win32.Foundation.BOOL)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt16VectorAlloc(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pprgn: POINTER(POINTER(Int16)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt16VectorAlloc(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pprgn: POINTER(POINTER(UInt16)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt32VectorAlloc(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pprgn: POINTER(POINTER(Int32)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt32VectorAlloc(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pprgn: POINTER(POINTER(UInt32)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToInt64VectorAlloc(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pprgn: POINTER(POINTER(Int64)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToUInt64VectorAlloc(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pprgn: POINTER(POINTER(UInt64)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToDoubleVectorAlloc(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pprgn: POINTER(POINTER(Double)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToFileTimeVectorAlloc(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pprgft: POINTER(POINTER(win32more.Windows.Win32.Foundation.FILETIME)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToStringVectorAlloc(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pprgsz: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetBooleanElem(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), iElem: UInt32, pfVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetInt16Elem(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), iElem: UInt32, pnVal: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetUInt16Elem(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), iElem: UInt32, pnVal: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetInt32Elem(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), iElem: UInt32, pnVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetUInt32Elem(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), iElem: UInt32, pnVal: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetInt64Elem(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), iElem: UInt32, pnVal: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetUInt64Elem(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), iElem: UInt32, pnVal: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetDoubleElem(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), iElem: UInt32, pnVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetFileTimeElem(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), iElem: UInt32, pftVal: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantGetStringElem(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), iElem: UInt32, ppszVal: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def ClearPropVariantArray(rgPropVar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), cVars: UInt32) -> Void: ...
@winfunctype('PROPSYS.dll')
def PropVariantCompareEx(propvar1: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), propvar2: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), unit: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVAR_COMPARE_UNIT, flags: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVAR_COMPARE_FLAGS) -> Int32: ...
@winfunctype('PROPSYS.dll')
def PropVariantChangeType(ppropvarDest: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), propvarSrc: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), flags: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVAR_CHANGE_FLAGS, vt: win32more.Windows.Win32.System.Variant.VARENUM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToVariant(pPropVar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pVar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToPropVariant(pVar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pPropVar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def StgSerializePropVariant(ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), ppProp: POINTER(POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE)), pcb: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def StgDeserializePropVariant(pprop: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.SERIALIZEDPROPERTYVALUE), cbMax: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class BSTRBLOB(Structure):
    cbSize: UInt32
    pData: POINTER(Byte)
class CABOOL(Structure):
    cElems: UInt32
    pElems: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)
class CABSTR(Structure):
    cElems: UInt32
    pElems: POINTER(win32more.Windows.Win32.Foundation.BSTR)
class CABSTRBLOB(Structure):
    cElems: UInt32
    pElems: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.BSTRBLOB)
class CAC(Structure):
    cElems: UInt32
    pElems: win32more.Windows.Win32.Foundation.PSTR
class CACLIPDATA(Structure):
    cElems: UInt32
    pElems: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.CLIPDATA)
class CACLSID(Structure):
    cElems: UInt32
    pElems: POINTER(Guid)
class CACY(Structure):
    cElems: UInt32
    pElems: POINTER(win32more.Windows.Win32.System.Com.CY)
class CADATE(Structure):
    cElems: UInt32
    pElems: POINTER(Double)
class CADBL(Structure):
    cElems: UInt32
    pElems: POINTER(Double)
class CAFILETIME(Structure):
    cElems: UInt32
    pElems: POINTER(win32more.Windows.Win32.Foundation.FILETIME)
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
    pElems: POINTER(win32more.Windows.Win32.Foundation.PSTR)
class CALPWSTR(Structure):
    cElems: UInt32
    pElems: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
class CAPROPVARIANT(Structure):
    cElems: UInt32
    pElems: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)
class CASCODE(Structure):
    cElems: UInt32
    pElems: POINTER(Int32)
class CAUB(Structure):
    cElems: UInt32
    pElems: POINTER(Byte)
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
    pClipData: POINTER(Byte)
class IDirectWriterLock(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0e6d4d92-6738-11cf-9608-00aa00680db4}')
    @commethod(3)
    def WaitForWriteAccess(self, dwTimeout: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReleaseWriteAccess(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def HaveWriteAccess(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumSTATPROPSETSTG(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000013b-0000-0000-c000-000000000046}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.STATPROPSETSTG), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IEnumSTATPROPSETSTG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumSTATPROPSTG(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000139-0000-0000-c000-000000000046}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.STATPROPSTG), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IEnumSTATPROPSTG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumSTATSTG(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000000d-0000-0000-c000-000000000046}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.System.Com.STATSTG), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IEnumSTATSTG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFillLockBytes(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{99caf010-415e-11cf-8814-00aa00b569f5}')
    @commethod(3)
    def FillAppend(self, pv: VoidPtr, cb: UInt32, pcbWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FillAt(self, ulOffset: UInt64, pv: VoidPtr, cb: UInt32, pcbWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetFillSize(self, ulSize: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Terminate(self, bCanceled: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILayoutStorage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0e6d4d90-6738-11cf-9608-00aa00680db4}')
    @commethod(3)
    def LayoutScript(self, pStorageLayout: POINTER(win32more.Windows.Win32.System.Com.StorageLayout), nEntries: UInt32, glfInterleavedFlag: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginMonitor(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EndMonitor(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ReLayoutDocfile(self, pwcsNewDfName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ReLayoutDocfileOnILockBytes(self, pILockBytes: win32more.Windows.Win32.System.Com.StructuredStorage.ILockBytes) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILockBytes(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000000a-0000-0000-c000-000000000046}')
    @commethod(3)
    def ReadAt(self, ulOffset: UInt64, pv: VoidPtr, cb: UInt32, pcbRead: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WriteAt(self, ulOffset: UInt64, pv: VoidPtr, cb: UInt32, pcbWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Flush(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetSize(self, cb: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def LockRegion(self, libOffset: UInt64, cb: UInt64, dwLockType: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UnlockRegion(self, libOffset: UInt64, cb: UInt64, dwLockType: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Stat(self, pstatstg: POINTER(win32more.Windows.Win32.System.Com.STATSTG), grfStatFlag: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMemoryAllocator(ComPtr):
    extends: None
    @commethod(0)
    def Allocate(self, cbSize: UInt32) -> VoidPtr: ...
    @commethod(1)
    def Free(self, pv: VoidPtr) -> Void: ...
class IPersistStorage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IPersist
    _iid_ = Guid('{0000010a-0000-0000-c000-000000000046}')
    @commethod(4)
    def IsDirty(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InitNew(self, pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Load(self, pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Save(self, pStgSave: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, fSameAsLoad: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SaveCompleted(self, pStgNew: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def HandsOffStorage(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyBag(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{55272a00-42cb-11ce-8135-00aa004bb851}')
    @commethod(3)
    def Read(self, pszPropName: win32more.Windows.Win32.Foundation.PWSTR, pVar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pErrorLog: win32more.Windows.Win32.System.Com.IErrorLog) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Write(self, pszPropName: win32more.Windows.Win32.Foundation.PWSTR, pVar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyBag2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{22f55882-280b-11d0-a8a9-00a0c90c2004}')
    @commethod(3)
    def Read(self, cProperties: UInt32, pPropBag: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPBAG2), pErrLog: win32more.Windows.Win32.System.Com.IErrorLog, pvarValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), phrError: POINTER(win32more.Windows.Win32.Foundation.HRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Write(self, cProperties: UInt32, pPropBag: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPBAG2), pvarValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CountProperties(self, pcProperties: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPropertyInfo(self, iProperty: UInt32, cProperties: UInt32, pPropBag: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPBAG2), pcProperties: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def LoadObject(self, pstrName: win32more.Windows.Win32.Foundation.PWSTR, dwHint: UInt32, pUnkObject: win32more.Windows.Win32.System.Com.IUnknown, pErrLog: win32more.Windows.Win32.System.Com.IErrorLog) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertySetStorage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000013a-0000-0000-c000-000000000046}')
    @commethod(3)
    def Create(self, rfmtid: POINTER(Guid), pclsid: POINTER(Guid), grfFlags: UInt32, grfMode: UInt32, ppprstg: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Open(self, rfmtid: POINTER(Guid), grfMode: UInt32, ppprstg: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Delete(self, rfmtid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Enum(self, ppenum: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IEnumSTATPROPSETSTG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyStorage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000138-0000-0000-c000-000000000046}')
    @commethod(3)
    def ReadMultiple(self, cpspec: UInt32, rgpspec: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPSPEC), rgpropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WriteMultiple(self, cpspec: UInt32, rgpspec: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPSPEC), rgpropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), propidNameFirst: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DeleteMultiple(self, cpspec: UInt32, rgpspec: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPSPEC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ReadPropertyNames(self, cpropid: UInt32, rgpropid: POINTER(UInt32), rglpwstrName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def WritePropertyNames(self, cpropid: UInt32, rgpropid: POINTER(UInt32), rglpwstrName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DeletePropertyNames(self, cpropid: UInt32, rgpropid: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Commit(self, grfCommitFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Revert(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Enum(self, ppenum: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IEnumSTATPROPSTG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetTimes(self, pctime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), patime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), pmtime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetClass(self, clsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Stat(self, pstatpsstg: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.STATPROPSETSTG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRootStorage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000012-0000-0000-c000-000000000046}')
    @commethod(3)
    def SwitchToFile(self, pszFile: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IStorage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000000b-0000-0000-c000-000000000046}')
    @commethod(3)
    def CreateStream(self, pwcsName: win32more.Windows.Win32.Foundation.PWSTR, grfMode: win32more.Windows.Win32.System.Com.STGM, reserved1: UInt32, reserved2: UInt32, ppstm: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OpenStream(self, pwcsName: win32more.Windows.Win32.Foundation.PWSTR, reserved1: VoidPtr, grfMode: win32more.Windows.Win32.System.Com.STGM, reserved2: UInt32, ppstm: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateStorage(self, pwcsName: win32more.Windows.Win32.Foundation.PWSTR, grfMode: win32more.Windows.Win32.System.Com.STGM, reserved1: UInt32, reserved2: UInt32, ppstg: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OpenStorage(self, pwcsName: win32more.Windows.Win32.Foundation.PWSTR, pstgPriority: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, grfMode: win32more.Windows.Win32.System.Com.STGM, snbExclude: POINTER(POINTER(UInt16)), reserved: UInt32, ppstg: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CopyTo(self, ciidExclude: UInt32, rgiidExclude: POINTER(Guid), snbExclude: POINTER(POINTER(UInt16)), pstgDest: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def MoveElementTo(self, pwcsName: win32more.Windows.Win32.Foundation.PWSTR, pstgDest: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, pwcsNewName: win32more.Windows.Win32.Foundation.PWSTR, grfFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Commit(self, grfCommitFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Revert(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnumElements(self, reserved1: UInt32, reserved2: VoidPtr, reserved3: UInt32, ppenum: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IEnumSTATSTG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DestroyElement(self, pwcsName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def RenameElement(self, pwcsOldName: win32more.Windows.Win32.Foundation.PWSTR, pwcsNewName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetElementTimes(self, pwcsName: win32more.Windows.Win32.Foundation.PWSTR, pctime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), patime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), pmtime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetClass(self, clsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetStateBits(self, grfStateBits: UInt32, grfMask: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Stat(self, pstatstg: POINTER(win32more.Windows.Win32.System.Com.STATSTG), grfStatFlag: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class OLESTREAM(Structure):
    lpstbl: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.OLESTREAMVTBL)
class OLESTREAMVTBL(Structure):
    Get: IntPtr
    Put: IntPtr
PIDMSI_STATUS_VALUE = Int32
PIDMSI_STATUS_NORMAL: win32more.Windows.Win32.System.Com.StructuredStorage.PIDMSI_STATUS_VALUE = 0
PIDMSI_STATUS_NEW: win32more.Windows.Win32.System.Com.StructuredStorage.PIDMSI_STATUS_VALUE = 1
PIDMSI_STATUS_PRELIM: win32more.Windows.Win32.System.Com.StructuredStorage.PIDMSI_STATUS_VALUE = 2
PIDMSI_STATUS_DRAFT: win32more.Windows.Win32.System.Com.StructuredStorage.PIDMSI_STATUS_VALUE = 3
PIDMSI_STATUS_INPROGRESS: win32more.Windows.Win32.System.Com.StructuredStorage.PIDMSI_STATUS_VALUE = 4
PIDMSI_STATUS_EDIT: win32more.Windows.Win32.System.Com.StructuredStorage.PIDMSI_STATUS_VALUE = 5
PIDMSI_STATUS_REVIEW: win32more.Windows.Win32.System.Com.StructuredStorage.PIDMSI_STATUS_VALUE = 6
PIDMSI_STATUS_PROOF: win32more.Windows.Win32.System.Com.StructuredStorage.PIDMSI_STATUS_VALUE = 7
PIDMSI_STATUS_FINAL: win32more.Windows.Win32.System.Com.StructuredStorage.PIDMSI_STATUS_VALUE = 8
PIDMSI_STATUS_OTHER: win32more.Windows.Win32.System.Com.StructuredStorage.PIDMSI_STATUS_VALUE = 32767
class PROPBAG2(Structure):
    dwType: UInt32
    vt: win32more.Windows.Win32.System.Variant.VARENUM
    cfType: UInt16
    dwHint: UInt32
    pstrName: win32more.Windows.Win32.Foundation.PWSTR
    clsid: Guid
class PROPSPEC(Structure):
    ulKind: win32more.Windows.Win32.System.Com.StructuredStorage.PROPSPEC_KIND
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        propid: UInt32
        lpwstr: win32more.Windows.Win32.Foundation.PWSTR
PROPSPEC_KIND = UInt32
PRSPEC_LPWSTR: win32more.Windows.Win32.System.Com.StructuredStorage.PROPSPEC_KIND = 0
PRSPEC_PROPID: win32more.Windows.Win32.System.Com.StructuredStorage.PROPSPEC_KIND = 1
class PROPVARIANT(Structure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        decVal: win32more.Windows.Win32.Foundation.DECIMAL
        class _Anonymous_e__Struct(Structure):
            vt: win32more.Windows.Win32.System.Variant.VARENUM
            wReserved1: UInt16
            wReserved2: UInt16
            wReserved3: UInt16
            Anonymous: _Anonymous_e__Union
            class _Anonymous_e__Union(Union):
                cVal: win32more.Windows.Win32.Foundation.CHAR
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
                boolVal: win32more.Windows.Win32.Foundation.VARIANT_BOOL
                __OBSOLETE__VARIANT_BOOL: win32more.Windows.Win32.Foundation.VARIANT_BOOL
                scode: Int32
                cyVal: win32more.Windows.Win32.System.Com.CY
                date: Double
                filetime: win32more.Windows.Win32.Foundation.FILETIME
                puuid: POINTER(Guid)
                pclipdata: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.CLIPDATA)
                bstrVal: win32more.Windows.Win32.Foundation.BSTR
                bstrblobVal: win32more.Windows.Win32.System.Com.StructuredStorage.BSTRBLOB
                blob: win32more.Windows.Win32.System.Com.BLOB
                pszVal: win32more.Windows.Win32.Foundation.PSTR
                pwszVal: win32more.Windows.Win32.Foundation.PWSTR
                punkVal: win32more.Windows.Win32.System.Com.IUnknown
                pdispVal: win32more.Windows.Win32.System.Com.IDispatch
                pStream: win32more.Windows.Win32.System.Com.IStream
                pStorage: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage
                pVersionedStream: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.VERSIONEDSTREAM)
                parray: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)
                cac: win32more.Windows.Win32.System.Com.StructuredStorage.CAC
                caub: win32more.Windows.Win32.System.Com.StructuredStorage.CAUB
                cai: win32more.Windows.Win32.System.Com.StructuredStorage.CAI
                caui: win32more.Windows.Win32.System.Com.StructuredStorage.CAUI
                cal: win32more.Windows.Win32.System.Com.StructuredStorage.CAL
                caul: win32more.Windows.Win32.System.Com.StructuredStorage.CAUL
                cah: win32more.Windows.Win32.System.Com.StructuredStorage.CAH
                cauh: win32more.Windows.Win32.System.Com.StructuredStorage.CAUH
                caflt: win32more.Windows.Win32.System.Com.StructuredStorage.CAFLT
                cadbl: win32more.Windows.Win32.System.Com.StructuredStorage.CADBL
                cabool: win32more.Windows.Win32.System.Com.StructuredStorage.CABOOL
                cascode: win32more.Windows.Win32.System.Com.StructuredStorage.CASCODE
                cacy: win32more.Windows.Win32.System.Com.StructuredStorage.CACY
                cadate: win32more.Windows.Win32.System.Com.StructuredStorage.CADATE
                cafiletime: win32more.Windows.Win32.System.Com.StructuredStorage.CAFILETIME
                cauuid: win32more.Windows.Win32.System.Com.StructuredStorage.CACLSID
                caclipdata: win32more.Windows.Win32.System.Com.StructuredStorage.CACLIPDATA
                cabstr: win32more.Windows.Win32.System.Com.StructuredStorage.CABSTR
                cabstrblob: win32more.Windows.Win32.System.Com.StructuredStorage.CABSTRBLOB
                calpstr: win32more.Windows.Win32.System.Com.StructuredStorage.CALPSTR
                calpwstr: win32more.Windows.Win32.System.Com.StructuredStorage.CALPWSTR
                capropvar: win32more.Windows.Win32.System.Com.StructuredStorage.CAPROPVARIANT
                pcVal: win32more.Windows.Win32.Foundation.PSTR
                pbVal: POINTER(Byte)
                piVal: POINTER(Int16)
                puiVal: POINTER(UInt16)
                plVal: POINTER(Int32)
                pulVal: POINTER(UInt32)
                pintVal: POINTER(Int32)
                puintVal: POINTER(UInt32)
                pfltVal: POINTER(Single)
                pdblVal: POINTER(Double)
                pboolVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)
                pdecVal: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)
                pscode: POINTER(Int32)
                pcyVal: POINTER(win32more.Windows.Win32.System.Com.CY)
                pdate: POINTER(Double)
                pbstrVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)
                ppunkVal: POINTER(win32more.Windows.Win32.System.Com.IUnknown)
                ppdispVal: POINTER(win32more.Windows.Win32.System.Com.IDispatch)
                pparray: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))
                pvarVal: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)
PROPVAR_CHANGE_FLAGS = Int32
PVCHF_DEFAULT: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVAR_CHANGE_FLAGS = 0
PVCHF_NOVALUEPROP: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVAR_CHANGE_FLAGS = 1
PVCHF_ALPHABOOL: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVAR_CHANGE_FLAGS = 2
PVCHF_NOUSEROVERRIDE: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVAR_CHANGE_FLAGS = 4
PVCHF_LOCALBOOL: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVAR_CHANGE_FLAGS = 8
PVCHF_NOHEXSTRING: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVAR_CHANGE_FLAGS = 16
PROPVAR_COMPARE_FLAGS = Int32
PVCF_DEFAULT: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVAR_COMPARE_FLAGS = 0
PVCF_TREATEMPTYASGREATERTHAN: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVAR_COMPARE_FLAGS = 1
PVCF_USESTRCMP: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVAR_COMPARE_FLAGS = 2
PVCF_USESTRCMPC: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVAR_COMPARE_FLAGS = 4
PVCF_USESTRCMPI: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVAR_COMPARE_FLAGS = 8
PVCF_USESTRCMPIC: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVAR_COMPARE_FLAGS = 16
PVCF_DIGITSASNUMBERS_CASESENSITIVE: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVAR_COMPARE_FLAGS = 32
PROPVAR_COMPARE_UNIT = Int32
PVCU_DEFAULT: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVAR_COMPARE_UNIT = 0
PVCU_SECOND: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVAR_COMPARE_UNIT = 1
PVCU_MINUTE: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVAR_COMPARE_UNIT = 2
PVCU_HOUR: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVAR_COMPARE_UNIT = 3
PVCU_DAY: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVAR_COMPARE_UNIT = 4
PVCU_MONTH: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVAR_COMPARE_UNIT = 5
PVCU_YEAR: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVAR_COMPARE_UNIT = 6
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
    mtime: win32more.Windows.Win32.Foundation.FILETIME
    ctime: win32more.Windows.Win32.Foundation.FILETIME
    atime: win32more.Windows.Win32.Foundation.FILETIME
    dwOSVersion: UInt32
class STATPROPSTG(Structure):
    lpwstrName: win32more.Windows.Win32.Foundation.PWSTR
    propid: UInt32
    vt: win32more.Windows.Win32.System.Variant.VARENUM
STGFMT = UInt32
STGFMT_STORAGE: win32more.Windows.Win32.System.Com.StructuredStorage.STGFMT = 0
STGFMT_NATIVE: win32more.Windows.Win32.System.Com.StructuredStorage.STGFMT = 1
STGFMT_FILE: win32more.Windows.Win32.System.Com.StructuredStorage.STGFMT = 3
STGFMT_ANY: win32more.Windows.Win32.System.Com.StructuredStorage.STGFMT = 4
STGFMT_DOCFILE: win32more.Windows.Win32.System.Com.StructuredStorage.STGFMT = 5
STGFMT_DOCUMENT: win32more.Windows.Win32.System.Com.StructuredStorage.STGFMT = 0
STGMOVE = Int32
STGMOVE_MOVE: win32more.Windows.Win32.System.Com.StructuredStorage.STGMOVE = 0
STGMOVE_COPY: win32more.Windows.Win32.System.Com.StructuredStorage.STGMOVE = 1
STGMOVE_SHALLOWCOPY: win32more.Windows.Win32.System.Com.StructuredStorage.STGMOVE = 2
class STGOPTIONS(Structure):
    usVersion: UInt16
    reserved: UInt16
    ulSectorSize: UInt32
    pwcsTemplateFile: win32more.Windows.Win32.Foundation.PWSTR
class VERSIONEDSTREAM(Structure):
    guidVersion: Guid
    pStream: win32more.Windows.Win32.System.Com.IStream


make_ready(__name__)
