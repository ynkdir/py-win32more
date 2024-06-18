from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Ole
import win32more.Windows.Win32.System.Variant
@winfunctype('OLEAUT32.dll')
def VARIANT_UserSize(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> UInt32: ...
@winfunctype('OLEAUT32.dll')
def VARIANT_UserMarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> POINTER(Byte): ...
@winfunctype('OLEAUT32.dll')
def VARIANT_UserUnmarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> POINTER(Byte): ...
@winfunctype('OLEAUT32.dll')
def VARIANT_UserFree(param0: POINTER(UInt32), param1: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> Void: ...
@winfunctype('OLEAUT32.dll')
def VARIANT_UserSize64(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> UInt32: ...
@winfunctype('OLEAUT32.dll')
def VARIANT_UserMarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> POINTER(Byte): ...
@winfunctype('OLEAUT32.dll')
def VARIANT_UserUnmarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> POINTER(Byte): ...
@winfunctype('OLEAUT32.dll')
def VARIANT_UserFree64(param0: POINTER(UInt32), param1: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> Void: ...
@winfunctype('OLEAUT32.dll')
def DosDateTimeToVariantTime(wDosDate: UInt16, wDosTime: UInt16, pvtime: POINTER(Double)) -> Int32: ...
@winfunctype('OLEAUT32.dll')
def VariantTimeToDosDateTime(vtime: Double, pwDosDate: POINTER(UInt16), pwDosTime: POINTER(UInt16)) -> Int32: ...
@winfunctype('OLEAUT32.dll')
def SystemTimeToVariantTime(lpSystemTime: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME), pvtime: POINTER(Double)) -> Int32: ...
@winfunctype('OLEAUT32.dll')
def VariantTimeToSystemTime(vtime: Double, lpSystemTime: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME)) -> Int32: ...
@winfunctype('OLEAUT32.dll')
def VariantInit(pvarg: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> Void: ...
@winfunctype('OLEAUT32.dll')
def VariantClear(pvarg: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VariantCopy(pvargDest: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvargSrc: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VariantCopyInd(pvarDest: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvargSrc: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VariantChangeType(pvargDest: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarSrc: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), wFlags: win32more.Windows.Win32.System.Variant.VAR_CHANGE_FLAGS, vt: win32more.Windows.Win32.System.Variant.VARENUM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VariantChangeTypeEx(pvargDest: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarSrc: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), lcid: UInt32, wFlags: win32more.Windows.Win32.System.Variant.VAR_CHANGE_FLAGS, vt: win32more.Windows.Win32.System.Variant.VARENUM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromResource(hinst: win32more.Windows.Win32.Foundation.HINSTANCE, id: UInt32, pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromBuffer(pv: VoidPtr, cb: UInt32, pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromGUIDAsString(guid: POINTER(Guid), pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromFileTime(pft: POINTER(win32more.Windows.Win32.Foundation.FILETIME), pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromFileTimeArray(prgft: POINTER(win32more.Windows.Win32.Foundation.FILETIME), cElems: UInt32, pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromVariantArrayElem(varIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), iElem: UInt32, pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromBooleanArray(prgf: POINTER(win32more.Windows.Win32.Foundation.BOOL), cElems: UInt32, pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromInt16Array(prgn: POINTER(Int16), cElems: UInt32, pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromUInt16Array(prgn: POINTER(UInt16), cElems: UInt32, pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromInt32Array(prgn: POINTER(Int32), cElems: UInt32, pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromUInt32Array(prgn: POINTER(UInt32), cElems: UInt32, pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromInt64Array(prgn: POINTER(Int64), cElems: UInt32, pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromUInt64Array(prgn: POINTER(UInt64), cElems: UInt32, pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromDoubleArray(prgn: POINTER(Double), cElems: UInt32, pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromStringArray(prgsz: POINTER(win32more.Windows.Win32.Foundation.PWSTR), cElems: UInt32, pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToBooleanWithDefault(varIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), fDefault: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('PROPSYS.dll')
def VariantToInt16WithDefault(varIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), iDefault: Int16) -> Int16: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt16WithDefault(varIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), uiDefault: UInt16) -> UInt16: ...
@winfunctype('PROPSYS.dll')
def VariantToInt32WithDefault(varIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), lDefault: Int32) -> Int32: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt32WithDefault(varIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), ulDefault: UInt32) -> UInt32: ...
@winfunctype('PROPSYS.dll')
def VariantToInt64WithDefault(varIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), llDefault: Int64) -> Int64: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt64WithDefault(varIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), ullDefault: UInt64) -> UInt64: ...
@winfunctype('PROPSYS.dll')
def VariantToDoubleWithDefault(varIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), dblDefault: Double) -> Double: ...
@winfunctype('PROPSYS.dll')
def VariantToStringWithDefault(varIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pszDefault: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.PWSTR: ...
@winfunctype('PROPSYS.dll')
def VariantToBoolean(varIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pfRet: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToInt16(varIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), piRet: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt16(varIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), puiRet: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToInt32(varIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), plRet: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt32(varIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pulRet: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToInt64(varIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pllRet: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt64(varIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pullRet: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToDouble(varIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pdblRet: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToBuffer(varIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pv: VoidPtr, cb: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToGUID(varIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pguid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToString(varIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pszBuf: win32more.Windows.Win32.Foundation.PWSTR, cchBuf: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToStringAlloc(varIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), ppszBuf: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToDosDateTime(varIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pwDate: POINTER(UInt16), pwTime: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToFileTime(varIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), stfOut: win32more.Windows.Win32.System.Variant.PSTIME_FLAGS, pftOut: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetElementCount(varIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> UInt32: ...
@winfunctype('PROPSYS.dll')
def VariantToBooleanArray(var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), prgf: POINTER(win32more.Windows.Win32.Foundation.BOOL), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToInt16Array(var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), prgn: POINTER(Int16), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt16Array(var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), prgn: POINTER(UInt16), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToInt32Array(var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), prgn: POINTER(Int32), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt32Array(var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), prgn: POINTER(UInt32), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToInt64Array(var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), prgn: POINTER(Int64), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt64Array(var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), prgn: POINTER(UInt64), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToDoubleArray(var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), prgn: POINTER(Double), crgn: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToStringArray(var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), prgsz: POINTER(win32more.Windows.Win32.Foundation.PWSTR), crgsz: UInt32, pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToBooleanArrayAlloc(var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pprgf: POINTER(POINTER(win32more.Windows.Win32.Foundation.BOOL)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToInt16ArrayAlloc(var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pprgn: POINTER(POINTER(Int16)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt16ArrayAlloc(var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pprgn: POINTER(POINTER(UInt16)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToInt32ArrayAlloc(var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pprgn: POINTER(POINTER(Int32)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt32ArrayAlloc(var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pprgn: POINTER(POINTER(UInt32)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToInt64ArrayAlloc(var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pprgn: POINTER(POINTER(Int64)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt64ArrayAlloc(var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pprgn: POINTER(POINTER(UInt64)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToDoubleArrayAlloc(var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pprgn: POINTER(POINTER(Double)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToStringArrayAlloc(var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pprgsz: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR)), pcElem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetBooleanElem(var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), iElem: UInt32, pfVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetInt16Elem(var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), iElem: UInt32, pnVal: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetUInt16Elem(var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), iElem: UInt32, pnVal: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetInt32Elem(var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), iElem: UInt32, pnVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetUInt32Elem(var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), iElem: UInt32, pnVal: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetInt64Elem(var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), iElem: UInt32, pnVal: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetUInt64Elem(var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), iElem: UInt32, pnVal: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetDoubleElem(var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), iElem: UInt32, pnVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetStringElem(var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), iElem: UInt32, ppszVal: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def ClearVariantArray(pvars: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), cvars: UInt32) -> Void: ...
@winfunctype('PROPSYS.dll')
def VariantCompare(var1: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), var2: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> Int32: ...
DRAWPROGRESSFLAGS = Int32
DPF_NONE: win32more.Windows.Win32.System.Variant.DRAWPROGRESSFLAGS = 0
DPF_MARQUEE: win32more.Windows.Win32.System.Variant.DRAWPROGRESSFLAGS = 1
DPF_MARQUEE_COMPLETE: win32more.Windows.Win32.System.Variant.DRAWPROGRESSFLAGS = 2
DPF_ERROR: win32more.Windows.Win32.System.Variant.DRAWPROGRESSFLAGS = 4
DPF_WARNING: win32more.Windows.Win32.System.Variant.DRAWPROGRESSFLAGS = 8
DPF_STOPPED: win32more.Windows.Win32.System.Variant.DRAWPROGRESSFLAGS = 16
PSTIME_FLAGS = Int32
PSTF_UTC: win32more.Windows.Win32.System.Variant.PSTIME_FLAGS = 0
PSTF_LOCAL: win32more.Windows.Win32.System.Variant.PSTIME_FLAGS = 1
VARENUM = UInt16
VT_EMPTY: win32more.Windows.Win32.System.Variant.VARENUM = 0
VT_NULL: win32more.Windows.Win32.System.Variant.VARENUM = 1
VT_I2: win32more.Windows.Win32.System.Variant.VARENUM = 2
VT_I4: win32more.Windows.Win32.System.Variant.VARENUM = 3
VT_R4: win32more.Windows.Win32.System.Variant.VARENUM = 4
VT_R8: win32more.Windows.Win32.System.Variant.VARENUM = 5
VT_CY: win32more.Windows.Win32.System.Variant.VARENUM = 6
VT_DATE: win32more.Windows.Win32.System.Variant.VARENUM = 7
VT_BSTR: win32more.Windows.Win32.System.Variant.VARENUM = 8
VT_DISPATCH: win32more.Windows.Win32.System.Variant.VARENUM = 9
VT_ERROR: win32more.Windows.Win32.System.Variant.VARENUM = 10
VT_BOOL: win32more.Windows.Win32.System.Variant.VARENUM = 11
VT_VARIANT: win32more.Windows.Win32.System.Variant.VARENUM = 12
VT_UNKNOWN: win32more.Windows.Win32.System.Variant.VARENUM = 13
VT_DECIMAL: win32more.Windows.Win32.System.Variant.VARENUM = 14
VT_I1: win32more.Windows.Win32.System.Variant.VARENUM = 16
VT_UI1: win32more.Windows.Win32.System.Variant.VARENUM = 17
VT_UI2: win32more.Windows.Win32.System.Variant.VARENUM = 18
VT_UI4: win32more.Windows.Win32.System.Variant.VARENUM = 19
VT_I8: win32more.Windows.Win32.System.Variant.VARENUM = 20
VT_UI8: win32more.Windows.Win32.System.Variant.VARENUM = 21
VT_INT: win32more.Windows.Win32.System.Variant.VARENUM = 22
VT_UINT: win32more.Windows.Win32.System.Variant.VARENUM = 23
VT_VOID: win32more.Windows.Win32.System.Variant.VARENUM = 24
VT_HRESULT: win32more.Windows.Win32.System.Variant.VARENUM = 25
VT_PTR: win32more.Windows.Win32.System.Variant.VARENUM = 26
VT_SAFEARRAY: win32more.Windows.Win32.System.Variant.VARENUM = 27
VT_CARRAY: win32more.Windows.Win32.System.Variant.VARENUM = 28
VT_USERDEFINED: win32more.Windows.Win32.System.Variant.VARENUM = 29
VT_LPSTR: win32more.Windows.Win32.System.Variant.VARENUM = 30
VT_LPWSTR: win32more.Windows.Win32.System.Variant.VARENUM = 31
VT_RECORD: win32more.Windows.Win32.System.Variant.VARENUM = 36
VT_INT_PTR: win32more.Windows.Win32.System.Variant.VARENUM = 37
VT_UINT_PTR: win32more.Windows.Win32.System.Variant.VARENUM = 38
VT_FILETIME: win32more.Windows.Win32.System.Variant.VARENUM = 64
VT_BLOB: win32more.Windows.Win32.System.Variant.VARENUM = 65
VT_STREAM: win32more.Windows.Win32.System.Variant.VARENUM = 66
VT_STORAGE: win32more.Windows.Win32.System.Variant.VARENUM = 67
VT_STREAMED_OBJECT: win32more.Windows.Win32.System.Variant.VARENUM = 68
VT_STORED_OBJECT: win32more.Windows.Win32.System.Variant.VARENUM = 69
VT_BLOB_OBJECT: win32more.Windows.Win32.System.Variant.VARENUM = 70
VT_CF: win32more.Windows.Win32.System.Variant.VARENUM = 71
VT_CLSID: win32more.Windows.Win32.System.Variant.VARENUM = 72
VT_VERSIONED_STREAM: win32more.Windows.Win32.System.Variant.VARENUM = 73
VT_BSTR_BLOB: win32more.Windows.Win32.System.Variant.VARENUM = 4095
VT_VECTOR: win32more.Windows.Win32.System.Variant.VARENUM = 4096
VT_ARRAY: win32more.Windows.Win32.System.Variant.VARENUM = 8192
VT_BYREF: win32more.Windows.Win32.System.Variant.VARENUM = 16384
VT_RESERVED: win32more.Windows.Win32.System.Variant.VARENUM = 32768
VT_ILLEGAL: win32more.Windows.Win32.System.Variant.VARENUM = 65535
VT_ILLEGALMASKED: win32more.Windows.Win32.System.Variant.VARENUM = 4095
VT_TYPEMASK: win32more.Windows.Win32.System.Variant.VARENUM = 4095
class VARIANT(Structure):
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
                llVal: Int64
                lVal: Int32
                bVal: Byte
                iVal: Int16
                fltVal: Single
                dblVal: Double
                boolVal: win32more.Windows.Win32.Foundation.VARIANT_BOOL
                __OBSOLETE__VARIANT_BOOL: win32more.Windows.Win32.Foundation.VARIANT_BOOL
                scode: Int32
                cyVal: win32more.Windows.Win32.System.Com.CY
                date: Double
                bstrVal: win32more.Windows.Win32.Foundation.BSTR
                punkVal: win32more.Windows.Win32.System.Com.IUnknown
                pdispVal: win32more.Windows.Win32.System.Com.IDispatch
                parray: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)
                pbVal: POINTER(Byte)
                piVal: POINTER(Int16)
                plVal: POINTER(Int32)
                pllVal: POINTER(Int64)
                pfltVal: POINTER(Single)
                pdblVal: POINTER(Double)
                pboolVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)
                __OBSOLETE__VARIANT_PBOOL: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)
                pscode: POINTER(Int32)
                pcyVal: POINTER(win32more.Windows.Win32.System.Com.CY)
                pdate: POINTER(Double)
                pbstrVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)
                ppunkVal: POINTER(win32more.Windows.Win32.System.Com.IUnknown)
                ppdispVal: POINTER(win32more.Windows.Win32.System.Com.IDispatch)
                pparray: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))
                pvarVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)
                byref: VoidPtr
                cVal: win32more.Windows.Win32.Foundation.CHAR
                uiVal: UInt16
                ulVal: UInt32
                ullVal: UInt64
                intVal: Int32
                uintVal: UInt32
                pdecVal: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)
                pcVal: win32more.Windows.Win32.Foundation.PSTR
                puiVal: POINTER(UInt16)
                pulVal: POINTER(UInt32)
                pullVal: POINTER(UInt64)
                pintVal: POINTER(Int32)
                puintVal: POINTER(UInt32)
                Anonymous: _Anonymous_e__Struct
                class _Anonymous_e__Struct(Structure):
                    pvRecord: VoidPtr
                    pRecInfo: win32more.Windows.Win32.System.Ole.IRecordInfo
VAR_CHANGE_FLAGS = UInt16
VARIANT_NOVALUEPROP: win32more.Windows.Win32.System.Variant.VAR_CHANGE_FLAGS = 1
VARIANT_ALPHABOOL: win32more.Windows.Win32.System.Variant.VAR_CHANGE_FLAGS = 2
VARIANT_NOUSEROVERRIDE: win32more.Windows.Win32.System.Variant.VAR_CHANGE_FLAGS = 4
VARIANT_CALENDAR_HIJRI: win32more.Windows.Win32.System.Variant.VAR_CHANGE_FLAGS = 8
VARIANT_LOCALBOOL: win32more.Windows.Win32.System.Variant.VAR_CHANGE_FLAGS = 16
VARIANT_CALENDAR_THAI: win32more.Windows.Win32.System.Variant.VAR_CHANGE_FLAGS = 32
VARIANT_CALENDAR_GREGORIAN: win32more.Windows.Win32.System.Variant.VAR_CHANGE_FLAGS = 64
VARIANT_USE_NLS: win32more.Windows.Win32.System.Variant.VAR_CHANGE_FLAGS = 128


make_ready(__name__)
