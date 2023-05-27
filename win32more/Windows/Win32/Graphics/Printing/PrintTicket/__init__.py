from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.Graphics.Printing.PrintTicket
import win32more.Windows.Win32.Storage.Xps
import win32more.Windows.Win32.System.Com
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
def PTQuerySchemaVersionSupport(pszPrinterName: win32more.Windows.Win32.Foundation.PWSTR, pMaxVersion: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTOpenProvider(pszPrinterName: win32more.Windows.Win32.Foundation.PWSTR, dwVersion: UInt32, phProvider: POINTER(win32more.Windows.Win32.Storage.Xps.HPTPROVIDER)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTOpenProviderEx(pszPrinterName: win32more.Windows.Win32.Foundation.PWSTR, dwMaxVersion: UInt32, dwPrefVersion: UInt32, phProvider: POINTER(win32more.Windows.Win32.Storage.Xps.HPTPROVIDER), pUsedVersion: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTCloseProvider(hProvider: win32more.Windows.Win32.Storage.Xps.HPTPROVIDER) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTReleaseMemory(pBuffer: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTGetPrintCapabilities(hProvider: win32more.Windows.Win32.Storage.Xps.HPTPROVIDER, pPrintTicket: win32more.Windows.Win32.System.Com.IStream_head, pCapabilities: win32more.Windows.Win32.System.Com.IStream_head, pbstrErrorMessage: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTGetPrintDeviceCapabilities(hProvider: win32more.Windows.Win32.Storage.Xps.HPTPROVIDER, pPrintTicket: win32more.Windows.Win32.System.Com.IStream_head, pDeviceCapabilities: win32more.Windows.Win32.System.Com.IStream_head, pbstrErrorMessage: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTGetPrintDeviceResources(hProvider: win32more.Windows.Win32.Storage.Xps.HPTPROVIDER, pszLocaleName: win32more.Windows.Win32.Foundation.PWSTR, pPrintTicket: win32more.Windows.Win32.System.Com.IStream_head, pDeviceResources: win32more.Windows.Win32.System.Com.IStream_head, pbstrErrorMessage: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTMergeAndValidatePrintTicket(hProvider: win32more.Windows.Win32.Storage.Xps.HPTPROVIDER, pBaseTicket: win32more.Windows.Win32.System.Com.IStream_head, pDeltaTicket: win32more.Windows.Win32.System.Com.IStream_head, scope: win32more.Windows.Win32.Graphics.Printing.PrintTicket.EPrintTicketScope, pResultTicket: win32more.Windows.Win32.System.Com.IStream_head, pbstrErrorMessage: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTConvertPrintTicketToDevMode(hProvider: win32more.Windows.Win32.Storage.Xps.HPTPROVIDER, pPrintTicket: win32more.Windows.Win32.System.Com.IStream_head, baseDevmodeType: win32more.Windows.Win32.Graphics.Printing.PrintTicket.EDefaultDevmodeType, scope: win32more.Windows.Win32.Graphics.Printing.PrintTicket.EPrintTicketScope, pcbDevmode: POINTER(UInt32), ppDevmode: POINTER(POINTER(win32more.Windows.Win32.Graphics.Gdi.DEVMODEA_head)), pbstrErrorMessage: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('prntvpt.dll')
def PTConvertDevModeToPrintTicket(hProvider: win32more.Windows.Win32.Storage.Xps.HPTPROVIDER, cbDevmode: UInt32, pDevmode: POINTER(win32more.Windows.Win32.Graphics.Gdi.DEVMODEA_head), scope: win32more.Windows.Win32.Graphics.Printing.PrintTicket.EPrintTicketScope, pPrintTicket: win32more.Windows.Win32.System.Com.IStream_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
EDefaultDevmodeType = Int32
EDefaultDevmodeType_kUserDefaultDevmode: EDefaultDevmodeType = 0
EDefaultDevmodeType_kPrinterDefaultDevmode: EDefaultDevmodeType = 1
EPrintTicketScope = Int32
EPrintTicketScope_kPTPageScope: EPrintTicketScope = 0
EPrintTicketScope_kPTDocumentScope: EPrintTicketScope = 1
EPrintTicketScope_kPTJobScope: EPrintTicketScope = 2
