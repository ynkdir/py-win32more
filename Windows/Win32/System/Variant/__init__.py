from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.Ole
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
@winfunctype('OLEAUT32.dll')
def VARIANT_UserSize(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> UInt32: ...
@winfunctype('OLEAUT32.dll')
def VARIANT_UserMarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> POINTER(Byte): ...
@winfunctype('OLEAUT32.dll')
def VARIANT_UserUnmarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> POINTER(Byte): ...
@winfunctype('OLEAUT32.dll')
def VARIANT_UserFree(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Void: ...
@winfunctype('OLEAUT32.dll')
def VARIANT_UserSize64(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> UInt32: ...
@winfunctype('OLEAUT32.dll')
def VARIANT_UserMarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> POINTER(Byte): ...
@winfunctype('OLEAUT32.dll')
def VARIANT_UserUnmarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> POINTER(Byte): ...
@winfunctype('OLEAUT32.dll')
def VARIANT_UserFree64(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Void: ...
@winfunctype('OLEAUT32.dll')
def DosDateTimeToVariantTime(wDosDate: UInt16, wDosTime: UInt16, pvtime: POINTER(Double)) -> Int32: ...
@winfunctype('OLEAUT32.dll')
def VariantTimeToDosDateTime(vtime: Double, pwDosDate: POINTER(UInt16), pwDosTime: POINTER(UInt16)) -> Int32: ...
@winfunctype('OLEAUT32.dll')
def SystemTimeToVariantTime(lpSystemTime: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head), pvtime: POINTER(Double)) -> Int32: ...
@winfunctype('OLEAUT32.dll')
def VariantTimeToSystemTime(vtime: Double, lpSystemTime: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head)) -> Int32: ...
@winfunctype('OLEAUT32.dll')
def VariantInit(pvarg: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Void: ...
@winfunctype('OLEAUT32.dll')
def VariantClear(pvarg: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VariantCopy(pvargDest: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvargSrc: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VariantCopyInd(pvarDest: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvargSrc: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VariantChangeType(pvargDest: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarSrc: POINTER(Windows.Win32.System.Variant.VARIANT_head), wFlags: Windows.Win32.System.Variant.VAR_CHANGE_FLAGS, vt: Windows.Win32.System.Variant.VARENUM) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VariantChangeTypeEx(pvargDest: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarSrc: POINTER(Windows.Win32.System.Variant.VARIANT_head), lcid: UInt32, wFlags: Windows.Win32.System.Variant.VAR_CHANGE_FLAGS, vt: Windows.Win32.System.Variant.VARENUM) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromResource(hinst: Windows.Win32.Foundation.HINSTANCE, id: UInt32, pvar: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromBuffer(pv: VoidPtr, cb: UInt32, pvar: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromGUIDAsString(guid: POINTER(Guid), pvar: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromFileTime(pft: POINTER(Windows.Win32.Foundation.FILETIME_head), pvar: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromFileTimeArray(prgft: POINTER(Windows.Win32.Foundation.FILETIME_head), cElems: UInt32, pvar: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromVariantArrayElem(varIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), iElem: UInt32, pvar: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromBooleanArray(prgf: POINTER(Windows.Win32.Foundation.BOOL), cElems: UInt32, pvar: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromInt16Array(prgn: POINTER(Int16), cElems: UInt32, pvar: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromUInt16Array(prgn: POINTER(UInt16), cElems: UInt32, pvar: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromInt32Array(prgn: POINTER(Int32), cElems: UInt32, pvar: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromUInt32Array(prgn: POINTER(UInt32), cElems: UInt32, pvar: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromInt64Array(prgn: POINTER(Int64), cElems: UInt32, pvar: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromUInt64Array(prgn: POINTER(UInt64), cElems: UInt32, pvar: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromDoubleArray(prgn: POINTER(Double), cElems: UInt32, pvar: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromStringArray(prgsz: POINTER(Windows.Win32.Foundation.PWSTR), cElems: UInt32, pvar: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToBooleanWithDefault(varIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), fDefault: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('PROPSYS.dll')
def VariantToInt16WithDefault(varIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), iDefault: Int16) -> Int16: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt16WithDefault(varIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), uiDefault: UInt16) -> UInt16: ...
@winfunctype('PROPSYS.dll')
def VariantToInt32WithDefault(varIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), lDefault: Int32) -> Int32: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt32WithDefault(varIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), ulDefault: UInt32) -> UInt32: ...
@winfunctype('PROPSYS.dll')
def VariantToInt64WithDefault(varIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), llDefault: Int64) -> Int64: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt64WithDefault(varIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), ullDefault: UInt64) -> UInt64: ...
@winfunctype('PROPSYS.dll')
def VariantToDoubleWithDefault(varIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), dblDefault: Double) -> Double: ...
@winfunctype('PROPSYS.dll')
def VariantToStringWithDefault(varIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), pszDefault: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('PROPSYS.dll')
def VariantToBoolean(varIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), pfRet: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToInt16(varIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), piRet: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt16(varIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), puiRet: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToInt32(varIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), plRet: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt32(varIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), pulRet: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToInt64(varIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), pllRet: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt64(varIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), pullRet: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToDouble(varIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), pdblRet: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToBuffer(varIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), pv: VoidPtr, cb: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToGUID(varIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), pguid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToString(varIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), pszBuf: Windows.Win32.Foundation.PWSTR, cchBuf: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToStringAlloc(varIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), ppszBuf: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToDosDateTime(varIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), pwDate: POINTER(UInt16), pwTime: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToFileTime(varIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), stfOut: Windows.Win32.System.Variant.PSTIME_FLAGS, pftOut: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetElementCount(varIn: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> UInt32: ...
@winfunctype('PROPSYS.dll')
def VariantToBooleanArray(var: POINTER(Windows.Win32.System.Variant.VARIANT_head), prgf: POINTER(Windows.Win32.Foundation.BOOL), crgn: UInt32, pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToInt16Array(var: POINTER(Windows.Win32.System.Variant.VARIANT_head), prgn: POINTER(Int16), crgn: UInt32, pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt16Array(var: POINTER(Windows.Win32.System.Variant.VARIANT_head), prgn: POINTER(UInt16), crgn: UInt32, pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToInt32Array(var: POINTER(Windows.Win32.System.Variant.VARIANT_head), prgn: POINTER(Int32), crgn: UInt32, pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt32Array(var: POINTER(Windows.Win32.System.Variant.VARIANT_head), prgn: POINTER(UInt32), crgn: UInt32, pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToInt64Array(var: POINTER(Windows.Win32.System.Variant.VARIANT_head), prgn: POINTER(Int64), crgn: UInt32, pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt64Array(var: POINTER(Windows.Win32.System.Variant.VARIANT_head), prgn: POINTER(UInt64), crgn: UInt32, pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToDoubleArray(var: POINTER(Windows.Win32.System.Variant.VARIANT_head), prgn: POINTER(Double), crgn: UInt32, pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToStringArray(var: POINTER(Windows.Win32.System.Variant.VARIANT_head), prgsz: POINTER(Windows.Win32.Foundation.PWSTR), crgsz: UInt32, pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToBooleanArrayAlloc(var: POINTER(Windows.Win32.System.Variant.VARIANT_head), pprgf: POINTER(POINTER(Windows.Win32.Foundation.BOOL)), pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToInt16ArrayAlloc(var: POINTER(Windows.Win32.System.Variant.VARIANT_head), pprgn: POINTER(POINTER(Int16)), pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt16ArrayAlloc(var: POINTER(Windows.Win32.System.Variant.VARIANT_head), pprgn: POINTER(POINTER(UInt16)), pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToInt32ArrayAlloc(var: POINTER(Windows.Win32.System.Variant.VARIANT_head), pprgn: POINTER(POINTER(Int32)), pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt32ArrayAlloc(var: POINTER(Windows.Win32.System.Variant.VARIANT_head), pprgn: POINTER(POINTER(UInt32)), pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToInt64ArrayAlloc(var: POINTER(Windows.Win32.System.Variant.VARIANT_head), pprgn: POINTER(POINTER(Int64)), pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToUInt64ArrayAlloc(var: POINTER(Windows.Win32.System.Variant.VARIANT_head), pprgn: POINTER(POINTER(UInt64)), pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToDoubleArrayAlloc(var: POINTER(Windows.Win32.System.Variant.VARIANT_head), pprgn: POINTER(POINTER(Double)), pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToStringArrayAlloc(var: POINTER(Windows.Win32.System.Variant.VARIANT_head), pprgsz: POINTER(POINTER(Windows.Win32.Foundation.PWSTR)), pcElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetBooleanElem(var: POINTER(Windows.Win32.System.Variant.VARIANT_head), iElem: UInt32, pfVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetInt16Elem(var: POINTER(Windows.Win32.System.Variant.VARIANT_head), iElem: UInt32, pnVal: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetUInt16Elem(var: POINTER(Windows.Win32.System.Variant.VARIANT_head), iElem: UInt32, pnVal: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetInt32Elem(var: POINTER(Windows.Win32.System.Variant.VARIANT_head), iElem: UInt32, pnVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetUInt32Elem(var: POINTER(Windows.Win32.System.Variant.VARIANT_head), iElem: UInt32, pnVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetInt64Elem(var: POINTER(Windows.Win32.System.Variant.VARIANT_head), iElem: UInt32, pnVal: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetUInt64Elem(var: POINTER(Windows.Win32.System.Variant.VARIANT_head), iElem: UInt32, pnVal: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetDoubleElem(var: POINTER(Windows.Win32.System.Variant.VARIANT_head), iElem: UInt32, pnVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantGetStringElem(var: POINTER(Windows.Win32.System.Variant.VARIANT_head), iElem: UInt32, ppszVal: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def ClearVariantArray(pvars: POINTER(Windows.Win32.System.Variant.VARIANT_head), cvars: UInt32) -> Void: ...
@winfunctype('PROPSYS.dll')
def VariantCompare(var1: POINTER(Windows.Win32.System.Variant.VARIANT_head), var2: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Int32: ...
DRAWPROGRESSFLAGS = Int32
DPF_NONE: DRAWPROGRESSFLAGS = 0
DPF_MARQUEE: DRAWPROGRESSFLAGS = 1
DPF_MARQUEE_COMPLETE: DRAWPROGRESSFLAGS = 2
DPF_ERROR: DRAWPROGRESSFLAGS = 4
DPF_WARNING: DRAWPROGRESSFLAGS = 8
DPF_STOPPED: DRAWPROGRESSFLAGS = 16
PSTIME_FLAGS = Int32
PSTF_UTC: PSTIME_FLAGS = 0
PSTF_LOCAL: PSTIME_FLAGS = 1
VARENUM = UInt16
VT_EMPTY: VARENUM = 0
VT_NULL: VARENUM = 1
VT_I2: VARENUM = 2
VT_I4: VARENUM = 3
VT_R4: VARENUM = 4
VT_R8: VARENUM = 5
VT_CY: VARENUM = 6
VT_DATE: VARENUM = 7
VT_BSTR: VARENUM = 8
VT_DISPATCH: VARENUM = 9
VT_ERROR: VARENUM = 10
VT_BOOL: VARENUM = 11
VT_VARIANT: VARENUM = 12
VT_UNKNOWN: VARENUM = 13
VT_DECIMAL: VARENUM = 14
VT_I1: VARENUM = 16
VT_UI1: VARENUM = 17
VT_UI2: VARENUM = 18
VT_UI4: VARENUM = 19
VT_I8: VARENUM = 20
VT_UI8: VARENUM = 21
VT_INT: VARENUM = 22
VT_UINT: VARENUM = 23
VT_VOID: VARENUM = 24
VT_HRESULT: VARENUM = 25
VT_PTR: VARENUM = 26
VT_SAFEARRAY: VARENUM = 27
VT_CARRAY: VARENUM = 28
VT_USERDEFINED: VARENUM = 29
VT_LPSTR: VARENUM = 30
VT_LPWSTR: VARENUM = 31
VT_RECORD: VARENUM = 36
VT_INT_PTR: VARENUM = 37
VT_UINT_PTR: VARENUM = 38
VT_FILETIME: VARENUM = 64
VT_BLOB: VARENUM = 65
VT_STREAM: VARENUM = 66
VT_STORAGE: VARENUM = 67
VT_STREAMED_OBJECT: VARENUM = 68
VT_STORED_OBJECT: VARENUM = 69
VT_BLOB_OBJECT: VARENUM = 70
VT_CF: VARENUM = 71
VT_CLSID: VARENUM = 72
VT_VERSIONED_STREAM: VARENUM = 73
VT_BSTR_BLOB: VARENUM = 4095
VT_VECTOR: VARENUM = 4096
VT_ARRAY: VARENUM = 8192
VT_BYREF: VARENUM = 16384
VT_RESERVED: VARENUM = 32768
VT_ILLEGAL: VARENUM = 65535
VT_ILLEGALMASKED: VARENUM = 4095
VT_TYPEMASK: VARENUM = 4095
class VARIANT(EasyCastStructure):
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
                llVal: Int64
                lVal: Int32
                bVal: Byte
                iVal: Int16
                fltVal: Single
                dblVal: Double
                boolVal: Windows.Win32.Foundation.VARIANT_BOOL
                __OBSOLETE__VARIANT_BOOL: Windows.Win32.Foundation.VARIANT_BOOL
                scode: Int32
                cyVal: Windows.Win32.System.Com.CY
                date: Double
                bstrVal: Windows.Win32.Foundation.BSTR
                punkVal: Windows.Win32.System.Com.IUnknown_head
                pdispVal: Windows.Win32.System.Com.IDispatch_head
                parray: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)
                pbVal: POINTER(Byte)
                piVal: POINTER(Int16)
                plVal: POINTER(Int32)
                pllVal: POINTER(Int64)
                pfltVal: POINTER(Single)
                pdblVal: POINTER(Double)
                pboolVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)
                __OBSOLETE__VARIANT_PBOOL: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)
                pscode: POINTER(Int32)
                pcyVal: POINTER(Windows.Win32.System.Com.CY_head)
                pdate: POINTER(Double)
                pbstrVal: POINTER(Windows.Win32.Foundation.BSTR)
                ppunkVal: POINTER(Windows.Win32.System.Com.IUnknown_head)
                ppdispVal: POINTER(Windows.Win32.System.Com.IDispatch_head)
                pparray: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))
                pvarVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)
                byref: VoidPtr
                cVal: Windows.Win32.Foundation.CHAR
                uiVal: UInt16
                ulVal: UInt32
                ullVal: UInt64
                intVal: Int32
                uintVal: UInt32
                pdecVal: POINTER(Windows.Win32.Foundation.DECIMAL_head)
                pcVal: Windows.Win32.Foundation.PSTR
                puiVal: POINTER(UInt16)
                pulVal: POINTER(UInt32)
                pullVal: POINTER(UInt64)
                pintVal: POINTER(Int32)
                puintVal: POINTER(UInt32)
                Anonymous: _Anonymous_e__Struct
                class _Anonymous_e__Struct(EasyCastStructure):
                    pvRecord: VoidPtr
                    pRecInfo: Windows.Win32.System.Ole.IRecordInfo_head
VAR_CHANGE_FLAGS = UInt16
VARIANT_NOVALUEPROP: VAR_CHANGE_FLAGS = 1
VARIANT_ALPHABOOL: VAR_CHANGE_FLAGS = 2
VARIANT_NOUSEROVERRIDE: VAR_CHANGE_FLAGS = 4
VARIANT_CALENDAR_HIJRI: VAR_CHANGE_FLAGS = 8
VARIANT_LOCALBOOL: VAR_CHANGE_FLAGS = 16
VARIANT_CALENDAR_THAI: VAR_CHANGE_FLAGS = 32
VARIANT_CALENDAR_GREGORIAN: VAR_CHANGE_FLAGS = 64
VARIANT_USE_NLS: VAR_CHANGE_FLAGS = 128
make_head(_module, 'VARIANT')
