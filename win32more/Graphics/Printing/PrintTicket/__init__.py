from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.Graphics.Printing.PrintTicket
import win32more.Storage.Xps
import win32more.System.Com

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
PRINTTICKET_ISTREAM_APIS = 1
S_PT_NO_CONFLICT = 262145
S_PT_CONFLICT_RESOLVED = 262146
E_PRINTTICKET_FORMAT = 2147745795
E_PRINTCAPABILITIES_FORMAT = 2147745796
E_DELTA_PRINTTICKET_FORMAT = 2147745797
E_PRINTDEVICECAPABILITIES_FORMAT = 2147745798
EDefaultDevmodeType = Int32
EDefaultDevmodeType_kUserDefaultDevmode = 0
EDefaultDevmodeType_kPrinterDefaultDevmode = 1
EPrintTicketScope = Int32
EPrintTicketScope_kPTPageScope = 0
EPrintTicketScope_kPTDocumentScope = 1
EPrintTicketScope_kPTJobScope = 2
def _define_PTQuerySchemaVersionSupport():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("PTQuerySchemaVersionSupport", windll["prntvpt"]), ((1, 'pszPrinterName'),(1, 'pMaxVersion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PTOpenProvider():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Storage.Xps.HPTPROVIDER), use_last_error=False)(("PTOpenProvider", windll["prntvpt"]), ((1, 'pszPrinterName'),(1, 'dwVersion'),(1, 'phProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PTOpenProviderEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.Storage.Xps.HPTPROVIDER),POINTER(UInt32), use_last_error=False)(("PTOpenProviderEx", windll["prntvpt"]), ((1, 'pszPrinterName'),(1, 'dwMaxVersion'),(1, 'dwPrefVersion'),(1, 'phProvider'),(1, 'pUsedVersion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PTCloseProvider():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.HPTPROVIDER, use_last_error=False)(("PTCloseProvider", windll["prntvpt"]), ((1, 'hProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PTReleaseMemory():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("PTReleaseMemory", windll["prntvpt"]), ((1, 'pBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PTGetPrintCapabilities():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.HPTPROVIDER,win32more.System.Com.IStream_head,win32more.System.Com.IStream_head,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("PTGetPrintCapabilities", windll["prntvpt"]), ((1, 'hProvider'),(1, 'pPrintTicket'),(1, 'pCapabilities'),(1, 'pbstrErrorMessage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PTGetPrintDeviceCapabilities():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.HPTPROVIDER,win32more.System.Com.IStream_head,win32more.System.Com.IStream_head,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("PTGetPrintDeviceCapabilities", windll["prntvpt"]), ((1, 'hProvider'),(1, 'pPrintTicket'),(1, 'pDeviceCapabilities'),(1, 'pbstrErrorMessage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PTGetPrintDeviceResources():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.HPTPROVIDER,win32more.Foundation.PWSTR,win32more.System.Com.IStream_head,win32more.System.Com.IStream_head,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("PTGetPrintDeviceResources", windll["prntvpt"]), ((1, 'hProvider'),(1, 'pszLocaleName'),(1, 'pPrintTicket'),(1, 'pDeviceResources'),(1, 'pbstrErrorMessage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PTMergeAndValidatePrintTicket():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.HPTPROVIDER,win32more.System.Com.IStream_head,win32more.System.Com.IStream_head,win32more.Graphics.Printing.PrintTicket.EPrintTicketScope,win32more.System.Com.IStream_head,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("PTMergeAndValidatePrintTicket", windll["prntvpt"]), ((1, 'hProvider'),(1, 'pBaseTicket'),(1, 'pDeltaTicket'),(1, 'scope'),(1, 'pResultTicket'),(1, 'pbstrErrorMessage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PTConvertPrintTicketToDevMode():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.HPTPROVIDER,win32more.System.Com.IStream_head,win32more.Graphics.Printing.PrintTicket.EDefaultDevmodeType,win32more.Graphics.Printing.PrintTicket.EPrintTicketScope,POINTER(UInt32),POINTER(POINTER(win32more.Graphics.Gdi.DEVMODEA_head)),POINTER(win32more.Foundation.BSTR), use_last_error=False)(("PTConvertPrintTicketToDevMode", windll["prntvpt"]), ((1, 'hProvider'),(1, 'pPrintTicket'),(1, 'baseDevmodeType'),(1, 'scope'),(1, 'pcbDevmode'),(1, 'ppDevmode'),(1, 'pbstrErrorMessage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PTConvertDevModeToPrintTicket():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.HPTPROVIDER,UInt32,POINTER(win32more.Graphics.Gdi.DEVMODEA_head),win32more.Graphics.Printing.PrintTicket.EPrintTicketScope,win32more.System.Com.IStream_head, use_last_error=False)(("PTConvertDevModeToPrintTicket", windll["prntvpt"]), ((1, 'hProvider'),(1, 'cbDevmode'),(1, 'pDevmode'),(1, 'scope'),(1, 'pPrintTicket'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "PRINTTICKET_ISTREAM_APIS",
    "S_PT_NO_CONFLICT",
    "S_PT_CONFLICT_RESOLVED",
    "E_PRINTTICKET_FORMAT",
    "E_PRINTCAPABILITIES_FORMAT",
    "E_DELTA_PRINTTICKET_FORMAT",
    "E_PRINTDEVICECAPABILITIES_FORMAT",
    "EDefaultDevmodeType",
    "EDefaultDevmodeType_kUserDefaultDevmode",
    "EDefaultDevmodeType_kPrinterDefaultDevmode",
    "EPrintTicketScope",
    "EPrintTicketScope_kPTPageScope",
    "EPrintTicketScope_kPTDocumentScope",
    "EPrintTicketScope_kPTJobScope",
    "PTQuerySchemaVersionSupport",
    "PTOpenProvider",
    "PTOpenProviderEx",
    "PTCloseProvider",
    "PTReleaseMemory",
    "PTGetPrintCapabilities",
    "PTGetPrintDeviceCapabilities",
    "PTGetPrintDeviceResources",
    "PTMergeAndValidatePrintTicket",
    "PTConvertPrintTicketToDevMode",
    "PTConvertDevModeToPrintTicket",
]
