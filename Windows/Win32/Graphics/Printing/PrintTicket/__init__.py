from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Gdi
import Windows.Win32.Graphics.Printing.PrintTicket
import Windows.Win32.Storage.Xps
import Windows.Win32.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
PRINTTICKET_ISTREAM_APIS: UInt32 = 1
S_PT_NO_CONFLICT: UInt32 = 262145
S_PT_CONFLICT_RESOLVED: UInt32 = 262146
E_PRINTTICKET_FORMAT: UInt32 = 2147745795
E_PRINTCAPABILITIES_FORMAT: UInt32 = 2147745796
E_DELTA_PRINTTICKET_FORMAT: UInt32 = 2147745797
E_PRINTDEVICECAPABILITIES_FORMAT: UInt32 = 2147745798
@winfunctype('prntvpt.dll')
def PTQuerySchemaVersionSupport(pszPrinterName: Windows.Win32.Foundation.PWSTR, pMaxVersion: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTOpenProvider(pszPrinterName: Windows.Win32.Foundation.PWSTR, dwVersion: UInt32, phProvider: POINTER(Windows.Win32.Storage.Xps.HPTPROVIDER)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTOpenProviderEx(pszPrinterName: Windows.Win32.Foundation.PWSTR, dwMaxVersion: UInt32, dwPrefVersion: UInt32, phProvider: POINTER(Windows.Win32.Storage.Xps.HPTPROVIDER), pUsedVersion: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTCloseProvider(hProvider: Windows.Win32.Storage.Xps.HPTPROVIDER) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTReleaseMemory(pBuffer: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTGetPrintCapabilities(hProvider: Windows.Win32.Storage.Xps.HPTPROVIDER, pPrintTicket: Windows.Win32.System.Com.IStream_head, pCapabilities: Windows.Win32.System.Com.IStream_head, pbstrErrorMessage: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTGetPrintDeviceCapabilities(hProvider: Windows.Win32.Storage.Xps.HPTPROVIDER, pPrintTicket: Windows.Win32.System.Com.IStream_head, pDeviceCapabilities: Windows.Win32.System.Com.IStream_head, pbstrErrorMessage: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTGetPrintDeviceResources(hProvider: Windows.Win32.Storage.Xps.HPTPROVIDER, pszLocaleName: Windows.Win32.Foundation.PWSTR, pPrintTicket: Windows.Win32.System.Com.IStream_head, pDeviceResources: Windows.Win32.System.Com.IStream_head, pbstrErrorMessage: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTMergeAndValidatePrintTicket(hProvider: Windows.Win32.Storage.Xps.HPTPROVIDER, pBaseTicket: Windows.Win32.System.Com.IStream_head, pDeltaTicket: Windows.Win32.System.Com.IStream_head, scope: Windows.Win32.Graphics.Printing.PrintTicket.EPrintTicketScope, pResultTicket: Windows.Win32.System.Com.IStream_head, pbstrErrorMessage: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTConvertPrintTicketToDevMode(hProvider: Windows.Win32.Storage.Xps.HPTPROVIDER, pPrintTicket: Windows.Win32.System.Com.IStream_head, baseDevmodeType: Windows.Win32.Graphics.Printing.PrintTicket.EDefaultDevmodeType, scope: Windows.Win32.Graphics.Printing.PrintTicket.EPrintTicketScope, pcbDevmode: POINTER(UInt32), ppDevmode: POINTER(POINTER(Windows.Win32.Graphics.Gdi.DEVMODEA_head)), pbstrErrorMessage: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTConvertDevModeToPrintTicket(hProvider: Windows.Win32.Storage.Xps.HPTPROVIDER, cbDevmode: UInt32, pDevmode: POINTER(Windows.Win32.Graphics.Gdi.DEVMODEA_head), scope: Windows.Win32.Graphics.Printing.PrintTicket.EPrintTicketScope, pPrintTicket: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
EDefaultDevmodeType = Int32
EDefaultDevmodeType_kUserDefaultDevmode: EDefaultDevmodeType = 0
EDefaultDevmodeType_kPrinterDefaultDevmode: EDefaultDevmodeType = 1
EPrintTicketScope = Int32
EPrintTicketScope_kPTPageScope: EPrintTicketScope = 0
EPrintTicketScope_kPTDocumentScope: EPrintTicketScope = 1
EPrintTicketScope_kPTJobScope: EPrintTicketScope = 2
