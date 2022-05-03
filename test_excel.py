# https://docs.microsoft.com/en-us/previous-versions/office/troubleshoot/office-developer/automate-excel-from-c

from contextlib import contextmanager
from win32more.all import *

# ctypes c_wchar_p to python str autoconversion is not always suitable...
SysAllocString.restype = c_void_p

# missing constants in win32metadata
LOCALE_SYSTEM_DEFAULT = 2048
LOCALE_USER_DEFAULT = 1024

@contextmanager
def Defer():
    def defer(f):
        funs.append(f)
    funs = []
    try:
        yield defer
    finally:
        for f in reversed(funs):
            f()

def HRCHECK(hr):
    if FAILED(hr):
        raise WinError(hr)
    return hr

def py_to_variant(v):
    if isinstance(v, VARIANT):
        return v
    elif isinstance(v, int):
        return VARIANT(vt=VT_INT, intVal=v)
    else:
        raise RuntimeError(f"unknown type {type(v)}")

def variant_to_py(v):
    if v.vt == VT_EMPTY:
        return None
    elif v.vt == VT_NULL:
        return None
    elif v.vt == VT_INT:
        return v.intval
    elif v.vt == VT_BSTR:
        return v.bstrVal
    elif v.vt == VT_DISPATCH:
        return v.pdispVal
    else:
        raise RuntimeError(f"unknown type {v.vt}")

def AutoWrap(autotype, pdisp, name, *args):
    dispid = Int32()
    HRCHECK(pdisp.GetIDsOfNames(GUID_NULL, PWSTR(name), 1, LOCALE_USER_DEFAULT, dispid))

    dp = DISPPARAMS()
    pargs = (VARIANT * len(args))()
    for i, e in enumerate(args):
        pargs[i] = py_to_variant(args[i])

    dp.cArgs = len(args)
    dp.rgvarg = pargs

    if autotype & DISPATCH_PROPERTYPUT:
        dp.cNamedArgs = 1
        dp.rgdispidNamedArgs = pointer(Int32(DISPID_PROPERTYPUT))

    result = VARIANT()

    HRCHECK(pdisp.Invoke(dispid, GUID_NULL, LOCALE_SYSTEM_DEFAULT, autotype, dp, result, None, None))

    return variant_to_py(result)

def main():
    with Defer() as defer:
        CoInitialize(None)
        defer(CoUninitialize)

        clsid = Guid()
        HRCHECK(CLSIDFromProgID("Excel.Application", clsid))

        pXlApp = IDispatch()
        HRCHECK(CoCreateInstance(clsid, None, CLSCTX_LOCAL_SERVER, IDispatch.Guid, pXlApp))
        defer(pXlApp.Release)

        # Make it visible
        AutoWrap(DISPATCH_PROPERTYPUT, pXlApp, "Visible", 1)

        # Get Workbooks collection
        pXlBooks = AutoWrap(DISPATCH_PROPERTYGET, pXlApp, "Workbooks")
        defer(pXlBooks.Release)

        # Call Workbooks.Add() to get a new workbook...
        pXlBook = AutoWrap(DISPATCH_PROPERTYGET, pXlBooks, "Add")
        defer(pXlBooks.Release)

        # Create a 15x15 safearray of variants
        sab = (SAFEARRAYBOUND * 2)()
        sab[0] = SAFEARRAYBOUND(lLbound=1, cElements=15)
        sab[1] = SAFEARRAYBOUND(lLbound=1, cElements=15)
        arr = VARIANT(vt=(VT_ARRAY|VT_VARIANT), parray=SafeArrayCreate(VT_VARIANT, 2, sab))
        defer(lambda: VariantClear(arr))

        # Fill safearray with some values
        for i in range(1, 16):
            for j in range(1, 16):
                SafeArrayPutElement(arr.parray, (Int32 * 2)(i, j), byref(VARIANT(vt=VT_I4, lVal=i*j)))

        # Get ActiveSheet object
        pXlSheet = AutoWrap(DISPATCH_PROPERTYGET, pXlApp, "ActiveSheet")
        defer(pXlSheet.Release)

        # Get Range object for the Range A1:O15
        parm = VARIANT(vt=VT_BSTR, byref=SysAllocString("A1:O15"))
        defer(lambda: VariantClear(parm))
        pXlRange = AutoWrap(DISPATCH_PROPERTYGET, pXlSheet, "Range", parm)
        defer(pXlRange.Release)

        # Set range with our safearray
        AutoWrap(DISPATCH_PROPERTYPUT, pXlRange, "Value", arr)

        # Wait for user
        MessageBox(0, "All done.", "Notice", MB_OK)

        # Set .Saved property of workbook to TRUE so we aren't prompted
        # to save when we tell Excel to quit
        AutoWrap(DISPATCH_PROPERTYPUT, pXlBook, "Saved", 1)

        # Tell Excel to quit (i.e. App.Quit)
        AutoWrap(DISPATCH_METHOD, pXlApp, "Quit")

if __name__ == "__main__":
    main()
