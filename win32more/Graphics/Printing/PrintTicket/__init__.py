from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.Graphics.Printing.PrintTicket
import win32more.Storage.Xps
import win32more.System.Com
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
PRINTTICKET_ISTREAM_APIS: UInt32 = 1
S_PT_NO_CONFLICT: UInt32 = 262145
S_PT_CONFLICT_RESOLVED: UInt32 = 262146
E_PRINTTICKET_FORMAT: UInt32 = 2147745795
E_PRINTCAPABILITIES_FORMAT: UInt32 = 2147745796
E_DELTA_PRINTTICKET_FORMAT: UInt32 = 2147745797
E_PRINTDEVICECAPABILITIES_FORMAT: UInt32 = 2147745798
@winfunctype('prntvpt.dll')
def PTQuerySchemaVersionSupport(pszPrinterName: win32more.Foundation.PWSTR, pMaxVersion: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTOpenProvider(pszPrinterName: win32more.Foundation.PWSTR, dwVersion: UInt32, phProvider: POINTER(win32more.Storage.Xps.HPTPROVIDER)) -> win32more.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTOpenProviderEx(pszPrinterName: win32more.Foundation.PWSTR, dwMaxVersion: UInt32, dwPrefVersion: UInt32, phProvider: POINTER(win32more.Storage.Xps.HPTPROVIDER), pUsedVersion: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTCloseProvider(hProvider: win32more.Storage.Xps.HPTPROVIDER) -> win32more.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTReleaseMemory(pBuffer: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTGetPrintCapabilities(hProvider: win32more.Storage.Xps.HPTPROVIDER, pPrintTicket: win32more.System.Com.IStream_head, pCapabilities: win32more.System.Com.IStream_head, pbstrErrorMessage: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTGetPrintDeviceCapabilities(hProvider: win32more.Storage.Xps.HPTPROVIDER, pPrintTicket: win32more.System.Com.IStream_head, pDeviceCapabilities: win32more.System.Com.IStream_head, pbstrErrorMessage: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTGetPrintDeviceResources(hProvider: win32more.Storage.Xps.HPTPROVIDER, pszLocaleName: win32more.Foundation.PWSTR, pPrintTicket: win32more.System.Com.IStream_head, pDeviceResources: win32more.System.Com.IStream_head, pbstrErrorMessage: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTMergeAndValidatePrintTicket(hProvider: win32more.Storage.Xps.HPTPROVIDER, pBaseTicket: win32more.System.Com.IStream_head, pDeltaTicket: win32more.System.Com.IStream_head, scope: win32more.Graphics.Printing.PrintTicket.EPrintTicketScope, pResultTicket: win32more.System.Com.IStream_head, pbstrErrorMessage: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTConvertPrintTicketToDevMode(hProvider: win32more.Storage.Xps.HPTPROVIDER, pPrintTicket: win32more.System.Com.IStream_head, baseDevmodeType: win32more.Graphics.Printing.PrintTicket.EDefaultDevmodeType, scope: win32more.Graphics.Printing.PrintTicket.EPrintTicketScope, pcbDevmode: POINTER(UInt32), ppDevmode: POINTER(POINTER(win32more.Graphics.Gdi.DEVMODEA_head)), pbstrErrorMessage: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTConvertDevModeToPrintTicket(hProvider: win32more.Storage.Xps.HPTPROVIDER, cbDevmode: UInt32, pDevmode: POINTER(win32more.Graphics.Gdi.DEVMODEA_head), scope: win32more.Graphics.Printing.PrintTicket.EPrintTicketScope, pPrintTicket: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
EDefaultDevmodeType = Int32
EDefaultDevmodeType_kUserDefaultDevmode: EDefaultDevmodeType = 0
EDefaultDevmodeType_kPrinterDefaultDevmode: EDefaultDevmodeType = 1
EPrintTicketScope = Int32
EPrintTicketScope_kPTPageScope: EPrintTicketScope = 0
EPrintTicketScope_kPTDocumentScope: EPrintTicketScope = 1
EPrintTicketScope_kPTJobScope: EPrintTicketScope = 2
__all__ = [
    "EDefaultDevmodeType",
    "EDefaultDevmodeType_kPrinterDefaultDevmode",
    "EDefaultDevmodeType_kUserDefaultDevmode",
    "EPrintTicketScope",
    "EPrintTicketScope_kPTDocumentScope",
    "EPrintTicketScope_kPTJobScope",
    "EPrintTicketScope_kPTPageScope",
    "E_DELTA_PRINTTICKET_FORMAT",
    "E_PRINTCAPABILITIES_FORMAT",
    "E_PRINTDEVICECAPABILITIES_FORMAT",
    "E_PRINTTICKET_FORMAT",
    "PRINTTICKET_ISTREAM_APIS",
    "PTCloseProvider",
    "PTConvertDevModeToPrintTicket",
    "PTConvertPrintTicketToDevMode",
    "PTGetPrintCapabilities",
    "PTGetPrintDeviceCapabilities",
    "PTGetPrintDeviceResources",
    "PTMergeAndValidatePrintTicket",
    "PTOpenProvider",
    "PTOpenProviderEx",
    "PTQuerySchemaVersionSupport",
    "PTReleaseMemory",
    "S_PT_CONFLICT_RESOLVED",
    "S_PT_NO_CONFLICT",
]
_arch_optional = [
]
