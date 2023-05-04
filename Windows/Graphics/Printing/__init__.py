from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.ApplicationModel.DataTransfer
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Graphics.Printing
import Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IPrintDocumentSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{dedc0c30-f1eb-47df-aae6-ed5427511f01}')
class IPrintManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{ff2a9694-8c99-44fd-ae4a-19d9aa9a0f0a}')
    @winrt_commethod(6)
    def add_PrintTaskRequested(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Printing.PrintManager, Windows.Graphics.Printing.PrintTaskRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PrintTaskRequested(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IPrintManagerStatic(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{58185dcd-e634-4654-84f0-e0152a8217ac}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.Graphics.Printing.PrintManager: ...
    @winrt_commethod(7)
    def ShowPrintUIAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class IPrintManagerStatic2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{35a99955-e6ab-4139-9abd-b86a729b3598}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
class IPrintPageInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{dd4be9c9-a6a1-4ada-930e-da872a4f23d3}')
    @winrt_commethod(6)
    def put_MediaSize(self, value: Windows.Graphics.Printing.PrintMediaSize) -> Void: ...
    @winrt_commethod(7)
    def get_MediaSize(self) -> Windows.Graphics.Printing.PrintMediaSize: ...
    @winrt_commethod(8)
    def put_PageSize(self, value: Windows.Foundation.Size) -> Void: ...
    @winrt_commethod(9)
    def get_PageSize(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(10)
    def put_DpiX(self, value: UInt32) -> Void: ...
    @winrt_commethod(11)
    def get_DpiX(self) -> UInt32: ...
    @winrt_commethod(12)
    def put_DpiY(self, value: UInt32) -> Void: ...
    @winrt_commethod(13)
    def get_DpiY(self) -> UInt32: ...
    @winrt_commethod(14)
    def put_Orientation(self, value: Windows.Graphics.Printing.PrintOrientation) -> Void: ...
    @winrt_commethod(15)
    def get_Orientation(self) -> Windows.Graphics.Printing.PrintOrientation: ...
    MediaSize = property(get_MediaSize, put_MediaSize)
    PageSize = property(get_PageSize, put_PageSize)
    DpiX = property(get_DpiX, put_DpiX)
    DpiY = property(get_DpiY, put_DpiY)
    Orientation = property(get_Orientation, put_Orientation)
class IPrintPageRange(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f8a06c54-6e7c-51c5-57fd-0660c2d71513}')
    @winrt_commethod(6)
    def get_FirstPageNumber(self) -> Int32: ...
    @winrt_commethod(7)
    def get_LastPageNumber(self) -> Int32: ...
    FirstPageNumber = property(get_FirstPageNumber, None)
    LastPageNumber = property(get_LastPageNumber, None)
class IPrintPageRangeFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{408fd45f-e047-5f85-7129-fb085a4fad14}')
    @winrt_commethod(6)
    def Create(self, firstPage: Int32, lastPage: Int32) -> Windows.Graphics.Printing.PrintPageRange: ...
    @winrt_commethod(7)
    def CreateWithSinglePage(self, page: Int32) -> Windows.Graphics.Printing.PrintPageRange: ...
class IPrintPageRangeOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{ce6db728-1357-46b2-a923-79f995f448fc}')
    @winrt_commethod(6)
    def put_AllowAllPages(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_AllowAllPages(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_AllowCurrentPage(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_AllowCurrentPage(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_AllowCustomSetOfPages(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_AllowCustomSetOfPages(self) -> Boolean: ...
    AllowAllPages = property(get_AllowAllPages, put_AllowAllPages)
    AllowCurrentPage = property(get_AllowCurrentPage, put_AllowCurrentPage)
    AllowCustomSetOfPages = property(get_AllowCustomSetOfPages, put_AllowCustomSetOfPages)
class IPrintTask(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{61d80247-6cf6-4fad-84e2-a5e82e2d4ceb}')
    @winrt_commethod(6)
    def get_Properties(self) -> Windows.ApplicationModel.DataTransfer.DataPackagePropertySet: ...
    @winrt_commethod(7)
    def get_Source(self) -> Windows.Graphics.Printing.IPrintDocumentSource: ...
    @winrt_commethod(8)
    def get_Options(self) -> Windows.Graphics.Printing.PrintTaskOptions: ...
    @winrt_commethod(9)
    def add_Previewing(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Printing.PrintTask, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Previewing(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_Submitting(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Printing.PrintTask, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Submitting(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_Progressing(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Printing.PrintTask, Windows.Graphics.Printing.PrintTaskProgressingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_Progressing(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def add_Completed(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Printing.PrintTask, Windows.Graphics.Printing.PrintTaskCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_Completed(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Properties = property(get_Properties, None)
    Source = property(get_Source, None)
    Options = property(get_Options, None)
class IPrintTask2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{36234877-3e53-4d9d-8f5e-316ac8dedae1}')
    @winrt_commethod(6)
    def put_IsPreviewEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_IsPreviewEnabled(self) -> Boolean: ...
    IsPreviewEnabled = property(get_IsPreviewEnabled, put_IsPreviewEnabled)
class IPrintTaskCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{5bcd34af-24e9-4c10-8d07-14c346ba3fce}')
    @winrt_commethod(6)
    def get_Completion(self) -> Windows.Graphics.Printing.PrintTaskCompletion: ...
    Completion = property(get_Completion, None)
class IPrintTaskOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{5a0a66bb-d289-41bb-96dd-57e28338ae3f}')
    @winrt_commethod(6)
    def put_Bordering(self, value: Windows.Graphics.Printing.PrintBordering) -> Void: ...
    @winrt_commethod(7)
    def get_Bordering(self) -> Windows.Graphics.Printing.PrintBordering: ...
    @winrt_commethod(8)
    def GetPagePrintTicket(self, printPageInfo: Windows.Graphics.Printing.PrintPageInfo) -> Windows.Storage.Streams.IRandomAccessStream: ...
    Bordering = property(get_Bordering, put_Bordering)
class IPrintTaskOptions2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{eb9b1606-9a36-4b59-8617-b217849262e1}')
    @winrt_commethod(6)
    def get_PageRangeOptions(self) -> Windows.Graphics.Printing.PrintPageRangeOptions: ...
    @winrt_commethod(7)
    def get_CustomPageRanges(self) -> Windows.Foundation.Collections.IVector[Windows.Graphics.Printing.PrintPageRange]: ...
    PageRangeOptions = property(get_PageRangeOptions, None)
    CustomPageRanges = property(get_CustomPageRanges, None)
class IPrintTaskOptionsCore(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{1bdbb474-4ed1-41eb-be3c-72d18ed67337}')
    @winrt_commethod(6)
    def GetPageDescription(self, jobPageNumber: UInt32) -> Windows.Graphics.Printing.PrintPageDescription: ...
class IPrintTaskOptionsCoreProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c1b71832-9e93-4e55-814b-3326a59efce1}')
    @winrt_commethod(6)
    def put_MediaSize(self, value: Windows.Graphics.Printing.PrintMediaSize) -> Void: ...
    @winrt_commethod(7)
    def get_MediaSize(self) -> Windows.Graphics.Printing.PrintMediaSize: ...
    @winrt_commethod(8)
    def put_MediaType(self, value: Windows.Graphics.Printing.PrintMediaType) -> Void: ...
    @winrt_commethod(9)
    def get_MediaType(self) -> Windows.Graphics.Printing.PrintMediaType: ...
    @winrt_commethod(10)
    def put_Orientation(self, value: Windows.Graphics.Printing.PrintOrientation) -> Void: ...
    @winrt_commethod(11)
    def get_Orientation(self) -> Windows.Graphics.Printing.PrintOrientation: ...
    @winrt_commethod(12)
    def put_PrintQuality(self, value: Windows.Graphics.Printing.PrintQuality) -> Void: ...
    @winrt_commethod(13)
    def get_PrintQuality(self) -> Windows.Graphics.Printing.PrintQuality: ...
    @winrt_commethod(14)
    def put_ColorMode(self, value: Windows.Graphics.Printing.PrintColorMode) -> Void: ...
    @winrt_commethod(15)
    def get_ColorMode(self) -> Windows.Graphics.Printing.PrintColorMode: ...
    @winrt_commethod(16)
    def put_Duplex(self, value: Windows.Graphics.Printing.PrintDuplex) -> Void: ...
    @winrt_commethod(17)
    def get_Duplex(self) -> Windows.Graphics.Printing.PrintDuplex: ...
    @winrt_commethod(18)
    def put_Collation(self, value: Windows.Graphics.Printing.PrintCollation) -> Void: ...
    @winrt_commethod(19)
    def get_Collation(self) -> Windows.Graphics.Printing.PrintCollation: ...
    @winrt_commethod(20)
    def put_Staple(self, value: Windows.Graphics.Printing.PrintStaple) -> Void: ...
    @winrt_commethod(21)
    def get_Staple(self) -> Windows.Graphics.Printing.PrintStaple: ...
    @winrt_commethod(22)
    def put_HolePunch(self, value: Windows.Graphics.Printing.PrintHolePunch) -> Void: ...
    @winrt_commethod(23)
    def get_HolePunch(self) -> Windows.Graphics.Printing.PrintHolePunch: ...
    @winrt_commethod(24)
    def put_Binding(self, value: Windows.Graphics.Printing.PrintBinding) -> Void: ...
    @winrt_commethod(25)
    def get_Binding(self) -> Windows.Graphics.Printing.PrintBinding: ...
    @winrt_commethod(26)
    def get_MinCopies(self) -> UInt32: ...
    @winrt_commethod(27)
    def get_MaxCopies(self) -> UInt32: ...
    @winrt_commethod(28)
    def put_NumberOfCopies(self, value: UInt32) -> Void: ...
    @winrt_commethod(29)
    def get_NumberOfCopies(self) -> UInt32: ...
    MediaSize = property(get_MediaSize, put_MediaSize)
    MediaType = property(get_MediaType, put_MediaType)
    Orientation = property(get_Orientation, put_Orientation)
    PrintQuality = property(get_PrintQuality, put_PrintQuality)
    ColorMode = property(get_ColorMode, put_ColorMode)
    Duplex = property(get_Duplex, put_Duplex)
    Collation = property(get_Collation, put_Collation)
    Staple = property(get_Staple, put_Staple)
    HolePunch = property(get_HolePunch, put_HolePunch)
    Binding = property(get_Binding, put_Binding)
    MinCopies = property(get_MinCopies, None)
    MaxCopies = property(get_MaxCopies, None)
    NumberOfCopies = property(get_NumberOfCopies, put_NumberOfCopies)
class IPrintTaskOptionsCoreUIConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{62e69e23-9a1e-4336-b74f-3cc7f4cff709}')
    @winrt_commethod(6)
    def get_DisplayedOptions(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    DisplayedOptions = property(get_DisplayedOptions, None)
class IPrintTaskProgressingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{810cd3cb-b410-4282-a073-5ac378234174}')
    @winrt_commethod(6)
    def get_DocumentPageCount(self) -> UInt32: ...
    DocumentPageCount = property(get_DocumentPageCount, None)
class IPrintTaskRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{6ff61e2e-2722-4240-a67c-f364849a17f3}')
    @winrt_commethod(6)
    def get_Deadline(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def CreatePrintTask(self, title: WinRT_String, handler: Windows.Graphics.Printing.PrintTaskSourceRequestedHandler) -> Windows.Graphics.Printing.PrintTask: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.Graphics.Printing.PrintTaskRequestedDeferral: ...
    Deadline = property(get_Deadline, None)
class IPrintTaskRequestedDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{cfefb3f0-ce3e-42c7-9496-64800c622c44}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IPrintTaskRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{d0aff924-a31b-454c-a7b6-5d0cc522fc16}')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.Graphics.Printing.PrintTaskRequest: ...
    Request = property(get_Request, None)
class IPrintTaskSourceRequestedArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f9f067be-f456-41f0-9c98-5ce73e851410}')
    @winrt_commethod(6)
    def get_Deadline(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def SetSource(self, source: Windows.Graphics.Printing.IPrintDocumentSource) -> Void: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.Graphics.Printing.PrintTaskSourceRequestedDeferral: ...
    Deadline = property(get_Deadline, None)
class IPrintTaskSourceRequestedDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{4a1560d1-6992-4d9d-8555-4ca4563fb166}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IPrintTaskTargetDeviceSupport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{295d70c0-c2cb-4b7d-b0ea-93095091a220}')
    @winrt_commethod(6)
    def put_IsPrinterTargetEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_IsPrinterTargetEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Is3DManufacturingTargetEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_Is3DManufacturingTargetEnabled(self) -> Boolean: ...
    IsPrinterTargetEnabled = property(get_IsPrinterTargetEnabled, put_IsPrinterTargetEnabled)
    Is3DManufacturingTargetEnabled = property(get_Is3DManufacturingTargetEnabled, put_Is3DManufacturingTargetEnabled)
class IStandardPrintTaskOptionsStatic(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b4483d26-0dd0-4cd4-baff-930fc7d6a574}')
    @winrt_commethod(6)
    def get_MediaSize(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_MediaType(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Orientation(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_PrintQuality(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_ColorMode(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Duplex(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_Collation(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_Staple(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_HolePunch(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_Binding(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_Copies(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def get_NUp(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def get_InputBin(self) -> WinRT_String: ...
    MediaSize = property(get_MediaSize, None)
    MediaType = property(get_MediaType, None)
    Orientation = property(get_Orientation, None)
    PrintQuality = property(get_PrintQuality, None)
    ColorMode = property(get_ColorMode, None)
    Duplex = property(get_Duplex, None)
    Collation = property(get_Collation, None)
    Staple = property(get_Staple, None)
    HolePunch = property(get_HolePunch, None)
    Binding = property(get_Binding, None)
    Copies = property(get_Copies, None)
    NUp = property(get_NUp, None)
    InputBin = property(get_InputBin, None)
class IStandardPrintTaskOptionsStatic2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{3be38bf4-7a44-4269-9a52-81261e289ee9}')
    @winrt_commethod(6)
    def get_Bordering(self) -> WinRT_String: ...
    Bordering = property(get_Bordering, None)
class IStandardPrintTaskOptionsStatic3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{bbf68e86-3858-41b3-a799-55dd9888d475}')
    @winrt_commethod(6)
    def get_CustomPageRanges(self) -> WinRT_String: ...
    CustomPageRanges = property(get_CustomPageRanges, None)
PrintBinding = Int32
PrintBinding_Default: PrintBinding = 0
PrintBinding_NotAvailable: PrintBinding = 1
PrintBinding_PrinterCustom: PrintBinding = 2
PrintBinding_None: PrintBinding = 3
PrintBinding_Bale: PrintBinding = 4
PrintBinding_BindBottom: PrintBinding = 5
PrintBinding_BindLeft: PrintBinding = 6
PrintBinding_BindRight: PrintBinding = 7
PrintBinding_BindTop: PrintBinding = 8
PrintBinding_Booklet: PrintBinding = 9
PrintBinding_EdgeStitchBottom: PrintBinding = 10
PrintBinding_EdgeStitchLeft: PrintBinding = 11
PrintBinding_EdgeStitchRight: PrintBinding = 12
PrintBinding_EdgeStitchTop: PrintBinding = 13
PrintBinding_Fold: PrintBinding = 14
PrintBinding_JogOffset: PrintBinding = 15
PrintBinding_Trim: PrintBinding = 16
PrintBordering = Int32
PrintBordering_Default: PrintBordering = 0
PrintBordering_NotAvailable: PrintBordering = 1
PrintBordering_PrinterCustom: PrintBordering = 2
PrintBordering_Bordered: PrintBordering = 3
PrintBordering_Borderless: PrintBordering = 4
PrintCollation = Int32
PrintCollation_Default: PrintCollation = 0
PrintCollation_NotAvailable: PrintCollation = 1
PrintCollation_PrinterCustom: PrintCollation = 2
PrintCollation_Collated: PrintCollation = 3
PrintCollation_Uncollated: PrintCollation = 4
PrintColorMode = Int32
PrintColorMode_Default: PrintColorMode = 0
PrintColorMode_NotAvailable: PrintColorMode = 1
PrintColorMode_PrinterCustom: PrintColorMode = 2
PrintColorMode_Color: PrintColorMode = 3
PrintColorMode_Grayscale: PrintColorMode = 4
PrintColorMode_Monochrome: PrintColorMode = 5
PrintDuplex = Int32
PrintDuplex_Default: PrintDuplex = 0
PrintDuplex_NotAvailable: PrintDuplex = 1
PrintDuplex_PrinterCustom: PrintDuplex = 2
PrintDuplex_OneSided: PrintDuplex = 3
PrintDuplex_TwoSidedShortEdge: PrintDuplex = 4
PrintDuplex_TwoSidedLongEdge: PrintDuplex = 5
PrintHolePunch = Int32
PrintHolePunch_Default: PrintHolePunch = 0
PrintHolePunch_NotAvailable: PrintHolePunch = 1
PrintHolePunch_PrinterCustom: PrintHolePunch = 2
PrintHolePunch_None: PrintHolePunch = 3
PrintHolePunch_LeftEdge: PrintHolePunch = 4
PrintHolePunch_RightEdge: PrintHolePunch = 5
PrintHolePunch_TopEdge: PrintHolePunch = 6
PrintHolePunch_BottomEdge: PrintHolePunch = 7
class PrintManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.IPrintManager
    _classid_ = 'Windows.Graphics.Printing.PrintManager'
    @winrt_mixinmethod
    def add_PrintTaskRequested(self: Windows.Graphics.Printing.IPrintManager, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Printing.PrintManager, Windows.Graphics.Printing.PrintTaskRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PrintTaskRequested(self: Windows.Graphics.Printing.IPrintManager, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def IsSupported(cls: Windows.Graphics.Printing.IPrintManagerStatic2) -> Boolean: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.Graphics.Printing.IPrintManagerStatic) -> Windows.Graphics.Printing.PrintManager: ...
    @winrt_classmethod
    def ShowPrintUIAsync(cls: Windows.Graphics.Printing.IPrintManagerStatic) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
PrintMediaSize = Int32
PrintMediaSize_Default: PrintMediaSize = 0
PrintMediaSize_NotAvailable: PrintMediaSize = 1
PrintMediaSize_PrinterCustom: PrintMediaSize = 2
PrintMediaSize_BusinessCard: PrintMediaSize = 3
PrintMediaSize_CreditCard: PrintMediaSize = 4
PrintMediaSize_IsoA0: PrintMediaSize = 5
PrintMediaSize_IsoA1: PrintMediaSize = 6
PrintMediaSize_IsoA10: PrintMediaSize = 7
PrintMediaSize_IsoA2: PrintMediaSize = 8
PrintMediaSize_IsoA3: PrintMediaSize = 9
PrintMediaSize_IsoA3Extra: PrintMediaSize = 10
PrintMediaSize_IsoA3Rotated: PrintMediaSize = 11
PrintMediaSize_IsoA4: PrintMediaSize = 12
PrintMediaSize_IsoA4Extra: PrintMediaSize = 13
PrintMediaSize_IsoA4Rotated: PrintMediaSize = 14
PrintMediaSize_IsoA5: PrintMediaSize = 15
PrintMediaSize_IsoA5Extra: PrintMediaSize = 16
PrintMediaSize_IsoA5Rotated: PrintMediaSize = 17
PrintMediaSize_IsoA6: PrintMediaSize = 18
PrintMediaSize_IsoA6Rotated: PrintMediaSize = 19
PrintMediaSize_IsoA7: PrintMediaSize = 20
PrintMediaSize_IsoA8: PrintMediaSize = 21
PrintMediaSize_IsoA9: PrintMediaSize = 22
PrintMediaSize_IsoB0: PrintMediaSize = 23
PrintMediaSize_IsoB1: PrintMediaSize = 24
PrintMediaSize_IsoB10: PrintMediaSize = 25
PrintMediaSize_IsoB2: PrintMediaSize = 26
PrintMediaSize_IsoB3: PrintMediaSize = 27
PrintMediaSize_IsoB4: PrintMediaSize = 28
PrintMediaSize_IsoB4Envelope: PrintMediaSize = 29
PrintMediaSize_IsoB5Envelope: PrintMediaSize = 30
PrintMediaSize_IsoB5Extra: PrintMediaSize = 31
PrintMediaSize_IsoB7: PrintMediaSize = 32
PrintMediaSize_IsoB8: PrintMediaSize = 33
PrintMediaSize_IsoB9: PrintMediaSize = 34
PrintMediaSize_IsoC0: PrintMediaSize = 35
PrintMediaSize_IsoC1: PrintMediaSize = 36
PrintMediaSize_IsoC10: PrintMediaSize = 37
PrintMediaSize_IsoC2: PrintMediaSize = 38
PrintMediaSize_IsoC3: PrintMediaSize = 39
PrintMediaSize_IsoC3Envelope: PrintMediaSize = 40
PrintMediaSize_IsoC4: PrintMediaSize = 41
PrintMediaSize_IsoC4Envelope: PrintMediaSize = 42
PrintMediaSize_IsoC5: PrintMediaSize = 43
PrintMediaSize_IsoC5Envelope: PrintMediaSize = 44
PrintMediaSize_IsoC6: PrintMediaSize = 45
PrintMediaSize_IsoC6C5Envelope: PrintMediaSize = 46
PrintMediaSize_IsoC6Envelope: PrintMediaSize = 47
PrintMediaSize_IsoC7: PrintMediaSize = 48
PrintMediaSize_IsoC8: PrintMediaSize = 49
PrintMediaSize_IsoC9: PrintMediaSize = 50
PrintMediaSize_IsoDLEnvelope: PrintMediaSize = 51
PrintMediaSize_IsoDLEnvelopeRotated: PrintMediaSize = 52
PrintMediaSize_IsoSRA3: PrintMediaSize = 53
PrintMediaSize_Japan2LPhoto: PrintMediaSize = 54
PrintMediaSize_JapanChou3Envelope: PrintMediaSize = 55
PrintMediaSize_JapanChou3EnvelopeRotated: PrintMediaSize = 56
PrintMediaSize_JapanChou4Envelope: PrintMediaSize = 57
PrintMediaSize_JapanChou4EnvelopeRotated: PrintMediaSize = 58
PrintMediaSize_JapanDoubleHagakiPostcard: PrintMediaSize = 59
PrintMediaSize_JapanDoubleHagakiPostcardRotated: PrintMediaSize = 60
PrintMediaSize_JapanHagakiPostcard: PrintMediaSize = 61
PrintMediaSize_JapanHagakiPostcardRotated: PrintMediaSize = 62
PrintMediaSize_JapanKaku2Envelope: PrintMediaSize = 63
PrintMediaSize_JapanKaku2EnvelopeRotated: PrintMediaSize = 64
PrintMediaSize_JapanKaku3Envelope: PrintMediaSize = 65
PrintMediaSize_JapanKaku3EnvelopeRotated: PrintMediaSize = 66
PrintMediaSize_JapanLPhoto: PrintMediaSize = 67
PrintMediaSize_JapanQuadrupleHagakiPostcard: PrintMediaSize = 68
PrintMediaSize_JapanYou1Envelope: PrintMediaSize = 69
PrintMediaSize_JapanYou2Envelope: PrintMediaSize = 70
PrintMediaSize_JapanYou3Envelope: PrintMediaSize = 71
PrintMediaSize_JapanYou4Envelope: PrintMediaSize = 72
PrintMediaSize_JapanYou4EnvelopeRotated: PrintMediaSize = 73
PrintMediaSize_JapanYou6Envelope: PrintMediaSize = 74
PrintMediaSize_JapanYou6EnvelopeRotated: PrintMediaSize = 75
PrintMediaSize_JisB0: PrintMediaSize = 76
PrintMediaSize_JisB1: PrintMediaSize = 77
PrintMediaSize_JisB10: PrintMediaSize = 78
PrintMediaSize_JisB2: PrintMediaSize = 79
PrintMediaSize_JisB3: PrintMediaSize = 80
PrintMediaSize_JisB4: PrintMediaSize = 81
PrintMediaSize_JisB4Rotated: PrintMediaSize = 82
PrintMediaSize_JisB5: PrintMediaSize = 83
PrintMediaSize_JisB5Rotated: PrintMediaSize = 84
PrintMediaSize_JisB6: PrintMediaSize = 85
PrintMediaSize_JisB6Rotated: PrintMediaSize = 86
PrintMediaSize_JisB7: PrintMediaSize = 87
PrintMediaSize_JisB8: PrintMediaSize = 88
PrintMediaSize_JisB9: PrintMediaSize = 89
PrintMediaSize_NorthAmerica10x11: PrintMediaSize = 90
PrintMediaSize_NorthAmerica10x12: PrintMediaSize = 91
PrintMediaSize_NorthAmerica10x14: PrintMediaSize = 92
PrintMediaSize_NorthAmerica11x17: PrintMediaSize = 93
PrintMediaSize_NorthAmerica14x17: PrintMediaSize = 94
PrintMediaSize_NorthAmerica4x6: PrintMediaSize = 95
PrintMediaSize_NorthAmerica4x8: PrintMediaSize = 96
PrintMediaSize_NorthAmerica5x7: PrintMediaSize = 97
PrintMediaSize_NorthAmerica8x10: PrintMediaSize = 98
PrintMediaSize_NorthAmerica9x11: PrintMediaSize = 99
PrintMediaSize_NorthAmericaArchitectureASheet: PrintMediaSize = 100
PrintMediaSize_NorthAmericaArchitectureBSheet: PrintMediaSize = 101
PrintMediaSize_NorthAmericaArchitectureCSheet: PrintMediaSize = 102
PrintMediaSize_NorthAmericaArchitectureDSheet: PrintMediaSize = 103
PrintMediaSize_NorthAmericaArchitectureESheet: PrintMediaSize = 104
PrintMediaSize_NorthAmericaCSheet: PrintMediaSize = 105
PrintMediaSize_NorthAmericaDSheet: PrintMediaSize = 106
PrintMediaSize_NorthAmericaESheet: PrintMediaSize = 107
PrintMediaSize_NorthAmericaExecutive: PrintMediaSize = 108
PrintMediaSize_NorthAmericaGermanLegalFanfold: PrintMediaSize = 109
PrintMediaSize_NorthAmericaGermanStandardFanfold: PrintMediaSize = 110
PrintMediaSize_NorthAmericaLegal: PrintMediaSize = 111
PrintMediaSize_NorthAmericaLegalExtra: PrintMediaSize = 112
PrintMediaSize_NorthAmericaLetter: PrintMediaSize = 113
PrintMediaSize_NorthAmericaLetterExtra: PrintMediaSize = 114
PrintMediaSize_NorthAmericaLetterPlus: PrintMediaSize = 115
PrintMediaSize_NorthAmericaLetterRotated: PrintMediaSize = 116
PrintMediaSize_NorthAmericaMonarchEnvelope: PrintMediaSize = 117
PrintMediaSize_NorthAmericaNote: PrintMediaSize = 118
PrintMediaSize_NorthAmericaNumber10Envelope: PrintMediaSize = 119
PrintMediaSize_NorthAmericaNumber10EnvelopeRotated: PrintMediaSize = 120
PrintMediaSize_NorthAmericaNumber11Envelope: PrintMediaSize = 121
PrintMediaSize_NorthAmericaNumber12Envelope: PrintMediaSize = 122
PrintMediaSize_NorthAmericaNumber14Envelope: PrintMediaSize = 123
PrintMediaSize_NorthAmericaNumber9Envelope: PrintMediaSize = 124
PrintMediaSize_NorthAmericaPersonalEnvelope: PrintMediaSize = 125
PrintMediaSize_NorthAmericaQuarto: PrintMediaSize = 126
PrintMediaSize_NorthAmericaStatement: PrintMediaSize = 127
PrintMediaSize_NorthAmericaSuperA: PrintMediaSize = 128
PrintMediaSize_NorthAmericaSuperB: PrintMediaSize = 129
PrintMediaSize_NorthAmericaTabloid: PrintMediaSize = 130
PrintMediaSize_NorthAmericaTabloidExtra: PrintMediaSize = 131
PrintMediaSize_OtherMetricA3Plus: PrintMediaSize = 132
PrintMediaSize_OtherMetricA4Plus: PrintMediaSize = 133
PrintMediaSize_OtherMetricFolio: PrintMediaSize = 134
PrintMediaSize_OtherMetricInviteEnvelope: PrintMediaSize = 135
PrintMediaSize_OtherMetricItalianEnvelope: PrintMediaSize = 136
PrintMediaSize_Prc10Envelope: PrintMediaSize = 137
PrintMediaSize_Prc10EnvelopeRotated: PrintMediaSize = 138
PrintMediaSize_Prc16K: PrintMediaSize = 139
PrintMediaSize_Prc16KRotated: PrintMediaSize = 140
PrintMediaSize_Prc1Envelope: PrintMediaSize = 141
PrintMediaSize_Prc1EnvelopeRotated: PrintMediaSize = 142
PrintMediaSize_Prc2Envelope: PrintMediaSize = 143
PrintMediaSize_Prc2EnvelopeRotated: PrintMediaSize = 144
PrintMediaSize_Prc32K: PrintMediaSize = 145
PrintMediaSize_Prc32KBig: PrintMediaSize = 146
PrintMediaSize_Prc32KRotated: PrintMediaSize = 147
PrintMediaSize_Prc3Envelope: PrintMediaSize = 148
PrintMediaSize_Prc3EnvelopeRotated: PrintMediaSize = 149
PrintMediaSize_Prc4Envelope: PrintMediaSize = 150
PrintMediaSize_Prc4EnvelopeRotated: PrintMediaSize = 151
PrintMediaSize_Prc5Envelope: PrintMediaSize = 152
PrintMediaSize_Prc5EnvelopeRotated: PrintMediaSize = 153
PrintMediaSize_Prc6Envelope: PrintMediaSize = 154
PrintMediaSize_Prc6EnvelopeRotated: PrintMediaSize = 155
PrintMediaSize_Prc7Envelope: PrintMediaSize = 156
PrintMediaSize_Prc7EnvelopeRotated: PrintMediaSize = 157
PrintMediaSize_Prc8Envelope: PrintMediaSize = 158
PrintMediaSize_Prc8EnvelopeRotated: PrintMediaSize = 159
PrintMediaSize_Prc9Envelope: PrintMediaSize = 160
PrintMediaSize_Prc9EnvelopeRotated: PrintMediaSize = 161
PrintMediaSize_Roll04Inch: PrintMediaSize = 162
PrintMediaSize_Roll06Inch: PrintMediaSize = 163
PrintMediaSize_Roll08Inch: PrintMediaSize = 164
PrintMediaSize_Roll12Inch: PrintMediaSize = 165
PrintMediaSize_Roll15Inch: PrintMediaSize = 166
PrintMediaSize_Roll18Inch: PrintMediaSize = 167
PrintMediaSize_Roll22Inch: PrintMediaSize = 168
PrintMediaSize_Roll24Inch: PrintMediaSize = 169
PrintMediaSize_Roll30Inch: PrintMediaSize = 170
PrintMediaSize_Roll36Inch: PrintMediaSize = 171
PrintMediaSize_Roll54Inch: PrintMediaSize = 172
PrintMediaType = Int32
PrintMediaType_Default: PrintMediaType = 0
PrintMediaType_NotAvailable: PrintMediaType = 1
PrintMediaType_PrinterCustom: PrintMediaType = 2
PrintMediaType_AutoSelect: PrintMediaType = 3
PrintMediaType_Archival: PrintMediaType = 4
PrintMediaType_BackPrintFilm: PrintMediaType = 5
PrintMediaType_Bond: PrintMediaType = 6
PrintMediaType_CardStock: PrintMediaType = 7
PrintMediaType_Continuous: PrintMediaType = 8
PrintMediaType_EnvelopePlain: PrintMediaType = 9
PrintMediaType_EnvelopeWindow: PrintMediaType = 10
PrintMediaType_Fabric: PrintMediaType = 11
PrintMediaType_HighResolution: PrintMediaType = 12
PrintMediaType_Label: PrintMediaType = 13
PrintMediaType_MultiLayerForm: PrintMediaType = 14
PrintMediaType_MultiPartForm: PrintMediaType = 15
PrintMediaType_Photographic: PrintMediaType = 16
PrintMediaType_PhotographicFilm: PrintMediaType = 17
PrintMediaType_PhotographicGlossy: PrintMediaType = 18
PrintMediaType_PhotographicHighGloss: PrintMediaType = 19
PrintMediaType_PhotographicMatte: PrintMediaType = 20
PrintMediaType_PhotographicSatin: PrintMediaType = 21
PrintMediaType_PhotographicSemiGloss: PrintMediaType = 22
PrintMediaType_Plain: PrintMediaType = 23
PrintMediaType_Screen: PrintMediaType = 24
PrintMediaType_ScreenPaged: PrintMediaType = 25
PrintMediaType_Stationery: PrintMediaType = 26
PrintMediaType_TabStockFull: PrintMediaType = 27
PrintMediaType_TabStockPreCut: PrintMediaType = 28
PrintMediaType_Transparency: PrintMediaType = 29
PrintMediaType_TShirtTransfer: PrintMediaType = 30
PrintMediaType_None: PrintMediaType = 31
PrintOrientation = Int32
PrintOrientation_Default: PrintOrientation = 0
PrintOrientation_NotAvailable: PrintOrientation = 1
PrintOrientation_PrinterCustom: PrintOrientation = 2
PrintOrientation_Portrait: PrintOrientation = 3
PrintOrientation_PortraitFlipped: PrintOrientation = 4
PrintOrientation_Landscape: PrintOrientation = 5
PrintOrientation_LandscapeFlipped: PrintOrientation = 6
class PrintPageDescription(EasyCastStructure):
    PageSize: Windows.Foundation.Size
    ImageableRect: Windows.Foundation.Rect
    DpiX: UInt32
    DpiY: UInt32
class PrintPageInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.IPrintPageInfo
    _classid_ = 'Windows.Graphics.Printing.PrintPageInfo'
    @winrt_activatemethod
    def New(cls) -> Windows.Graphics.Printing.PrintPageInfo: ...
    @winrt_mixinmethod
    def put_MediaSize(self: Windows.Graphics.Printing.IPrintPageInfo, value: Windows.Graphics.Printing.PrintMediaSize) -> Void: ...
    @winrt_mixinmethod
    def get_MediaSize(self: Windows.Graphics.Printing.IPrintPageInfo) -> Windows.Graphics.Printing.PrintMediaSize: ...
    @winrt_mixinmethod
    def put_PageSize(self: Windows.Graphics.Printing.IPrintPageInfo, value: Windows.Foundation.Size) -> Void: ...
    @winrt_mixinmethod
    def get_PageSize(self: Windows.Graphics.Printing.IPrintPageInfo) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def put_DpiX(self: Windows.Graphics.Printing.IPrintPageInfo, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_DpiX(self: Windows.Graphics.Printing.IPrintPageInfo) -> UInt32: ...
    @winrt_mixinmethod
    def put_DpiY(self: Windows.Graphics.Printing.IPrintPageInfo, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_DpiY(self: Windows.Graphics.Printing.IPrintPageInfo) -> UInt32: ...
    @winrt_mixinmethod
    def put_Orientation(self: Windows.Graphics.Printing.IPrintPageInfo, value: Windows.Graphics.Printing.PrintOrientation) -> Void: ...
    @winrt_mixinmethod
    def get_Orientation(self: Windows.Graphics.Printing.IPrintPageInfo) -> Windows.Graphics.Printing.PrintOrientation: ...
    MediaSize = property(get_MediaSize, put_MediaSize)
    PageSize = property(get_PageSize, put_PageSize)
    DpiX = property(get_DpiX, put_DpiX)
    DpiY = property(get_DpiY, put_DpiY)
    Orientation = property(get_Orientation, put_Orientation)
class PrintPageRange(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.IPrintPageRange
    _classid_ = 'Windows.Graphics.Printing.PrintPageRange'
    @winrt_factorymethod
    def Create(cls: Windows.Graphics.Printing.IPrintPageRangeFactory, firstPage: Int32, lastPage: Int32) -> Windows.Graphics.Printing.PrintPageRange: ...
    @winrt_factorymethod
    def CreateWithSinglePage(cls: Windows.Graphics.Printing.IPrintPageRangeFactory, page: Int32) -> Windows.Graphics.Printing.PrintPageRange: ...
    @winrt_mixinmethod
    def get_FirstPageNumber(self: Windows.Graphics.Printing.IPrintPageRange) -> Int32: ...
    @winrt_mixinmethod
    def get_LastPageNumber(self: Windows.Graphics.Printing.IPrintPageRange) -> Int32: ...
    FirstPageNumber = property(get_FirstPageNumber, None)
    LastPageNumber = property(get_LastPageNumber, None)
class PrintPageRangeOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.IPrintPageRangeOptions
    _classid_ = 'Windows.Graphics.Printing.PrintPageRangeOptions'
    @winrt_mixinmethod
    def put_AllowAllPages(self: Windows.Graphics.Printing.IPrintPageRangeOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AllowAllPages(self: Windows.Graphics.Printing.IPrintPageRangeOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowCurrentPage(self: Windows.Graphics.Printing.IPrintPageRangeOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AllowCurrentPage(self: Windows.Graphics.Printing.IPrintPageRangeOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowCustomSetOfPages(self: Windows.Graphics.Printing.IPrintPageRangeOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AllowCustomSetOfPages(self: Windows.Graphics.Printing.IPrintPageRangeOptions) -> Boolean: ...
    AllowAllPages = property(get_AllowAllPages, put_AllowAllPages)
    AllowCurrentPage = property(get_AllowCurrentPage, put_AllowCurrentPage)
    AllowCustomSetOfPages = property(get_AllowCustomSetOfPages, put_AllowCustomSetOfPages)
PrintQuality = Int32
PrintQuality_Default: PrintQuality = 0
PrintQuality_NotAvailable: PrintQuality = 1
PrintQuality_PrinterCustom: PrintQuality = 2
PrintQuality_Automatic: PrintQuality = 3
PrintQuality_Draft: PrintQuality = 4
PrintQuality_Fax: PrintQuality = 5
PrintQuality_High: PrintQuality = 6
PrintQuality_Normal: PrintQuality = 7
PrintQuality_Photographic: PrintQuality = 8
PrintQuality_Text: PrintQuality = 9
PrintStaple = Int32
PrintStaple_Default: PrintStaple = 0
PrintStaple_NotAvailable: PrintStaple = 1
PrintStaple_PrinterCustom: PrintStaple = 2
PrintStaple_None: PrintStaple = 3
PrintStaple_StapleTopLeft: PrintStaple = 4
PrintStaple_StapleTopRight: PrintStaple = 5
PrintStaple_StapleBottomLeft: PrintStaple = 6
PrintStaple_StapleBottomRight: PrintStaple = 7
PrintStaple_StapleDualLeft: PrintStaple = 8
PrintStaple_StapleDualRight: PrintStaple = 9
PrintStaple_StapleDualTop: PrintStaple = 10
PrintStaple_StapleDualBottom: PrintStaple = 11
PrintStaple_SaddleStitch: PrintStaple = 12
class PrintTask(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.IPrintTask
    _classid_ = 'Windows.Graphics.Printing.PrintTask'
    @winrt_mixinmethod
    def get_Properties(self: Windows.Graphics.Printing.IPrintTask) -> Windows.ApplicationModel.DataTransfer.DataPackagePropertySet: ...
    @winrt_mixinmethod
    def get_Source(self: Windows.Graphics.Printing.IPrintTask) -> Windows.Graphics.Printing.IPrintDocumentSource: ...
    @winrt_mixinmethod
    def get_Options(self: Windows.Graphics.Printing.IPrintTask) -> Windows.Graphics.Printing.PrintTaskOptions: ...
    @winrt_mixinmethod
    def add_Previewing(self: Windows.Graphics.Printing.IPrintTask, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Printing.PrintTask, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Previewing(self: Windows.Graphics.Printing.IPrintTask, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Submitting(self: Windows.Graphics.Printing.IPrintTask, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Printing.PrintTask, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Submitting(self: Windows.Graphics.Printing.IPrintTask, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Progressing(self: Windows.Graphics.Printing.IPrintTask, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Printing.PrintTask, Windows.Graphics.Printing.PrintTaskProgressingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Progressing(self: Windows.Graphics.Printing.IPrintTask, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Completed(self: Windows.Graphics.Printing.IPrintTask, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Printing.PrintTask, Windows.Graphics.Printing.PrintTaskCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Completed(self: Windows.Graphics.Printing.IPrintTask, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def put_IsPrinterTargetEnabled(self: Windows.Graphics.Printing.IPrintTaskTargetDeviceSupport, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsPrinterTargetEnabled(self: Windows.Graphics.Printing.IPrintTaskTargetDeviceSupport) -> Boolean: ...
    @winrt_mixinmethod
    def put_Is3DManufacturingTargetEnabled(self: Windows.Graphics.Printing.IPrintTaskTargetDeviceSupport, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Is3DManufacturingTargetEnabled(self: Windows.Graphics.Printing.IPrintTaskTargetDeviceSupport) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsPreviewEnabled(self: Windows.Graphics.Printing.IPrintTask2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsPreviewEnabled(self: Windows.Graphics.Printing.IPrintTask2) -> Boolean: ...
    Properties = property(get_Properties, None)
    Source = property(get_Source, None)
    Options = property(get_Options, None)
    IsPrinterTargetEnabled = property(get_IsPrinterTargetEnabled, put_IsPrinterTargetEnabled)
    Is3DManufacturingTargetEnabled = property(get_Is3DManufacturingTargetEnabled, put_Is3DManufacturingTargetEnabled)
    IsPreviewEnabled = property(get_IsPreviewEnabled, put_IsPreviewEnabled)
class PrintTaskCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.IPrintTaskCompletedEventArgs
    _classid_ = 'Windows.Graphics.Printing.PrintTaskCompletedEventArgs'
    @winrt_mixinmethod
    def get_Completion(self: Windows.Graphics.Printing.IPrintTaskCompletedEventArgs) -> Windows.Graphics.Printing.PrintTaskCompletion: ...
    Completion = property(get_Completion, None)
PrintTaskCompletion = Int32
PrintTaskCompletion_Abandoned: PrintTaskCompletion = 0
PrintTaskCompletion_Canceled: PrintTaskCompletion = 1
PrintTaskCompletion_Failed: PrintTaskCompletion = 2
PrintTaskCompletion_Submitted: PrintTaskCompletion = 3
class PrintTaskOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.IPrintTaskOptionsCore
    _classid_ = 'Windows.Graphics.Printing.PrintTaskOptions'
    @winrt_mixinmethod
    def GetPageDescription(self: Windows.Graphics.Printing.IPrintTaskOptionsCore, jobPageNumber: UInt32) -> Windows.Graphics.Printing.PrintPageDescription: ...
    @winrt_mixinmethod
    def put_MediaSize(self: Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties, value: Windows.Graphics.Printing.PrintMediaSize) -> Void: ...
    @winrt_mixinmethod
    def get_MediaSize(self: Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties) -> Windows.Graphics.Printing.PrintMediaSize: ...
    @winrt_mixinmethod
    def put_MediaType(self: Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties, value: Windows.Graphics.Printing.PrintMediaType) -> Void: ...
    @winrt_mixinmethod
    def get_MediaType(self: Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties) -> Windows.Graphics.Printing.PrintMediaType: ...
    @winrt_mixinmethod
    def put_Orientation(self: Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties, value: Windows.Graphics.Printing.PrintOrientation) -> Void: ...
    @winrt_mixinmethod
    def get_Orientation(self: Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties) -> Windows.Graphics.Printing.PrintOrientation: ...
    @winrt_mixinmethod
    def put_PrintQuality(self: Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties, value: Windows.Graphics.Printing.PrintQuality) -> Void: ...
    @winrt_mixinmethod
    def get_PrintQuality(self: Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties) -> Windows.Graphics.Printing.PrintQuality: ...
    @winrt_mixinmethod
    def put_ColorMode(self: Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties, value: Windows.Graphics.Printing.PrintColorMode) -> Void: ...
    @winrt_mixinmethod
    def get_ColorMode(self: Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties) -> Windows.Graphics.Printing.PrintColorMode: ...
    @winrt_mixinmethod
    def put_Duplex(self: Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties, value: Windows.Graphics.Printing.PrintDuplex) -> Void: ...
    @winrt_mixinmethod
    def get_Duplex(self: Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties) -> Windows.Graphics.Printing.PrintDuplex: ...
    @winrt_mixinmethod
    def put_Collation(self: Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties, value: Windows.Graphics.Printing.PrintCollation) -> Void: ...
    @winrt_mixinmethod
    def get_Collation(self: Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties) -> Windows.Graphics.Printing.PrintCollation: ...
    @winrt_mixinmethod
    def put_Staple(self: Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties, value: Windows.Graphics.Printing.PrintStaple) -> Void: ...
    @winrt_mixinmethod
    def get_Staple(self: Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties) -> Windows.Graphics.Printing.PrintStaple: ...
    @winrt_mixinmethod
    def put_HolePunch(self: Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties, value: Windows.Graphics.Printing.PrintHolePunch) -> Void: ...
    @winrt_mixinmethod
    def get_HolePunch(self: Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties) -> Windows.Graphics.Printing.PrintHolePunch: ...
    @winrt_mixinmethod
    def put_Binding(self: Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties, value: Windows.Graphics.Printing.PrintBinding) -> Void: ...
    @winrt_mixinmethod
    def get_Binding(self: Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties) -> Windows.Graphics.Printing.PrintBinding: ...
    @winrt_mixinmethod
    def get_MinCopies(self: Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties) -> UInt32: ...
    @winrt_mixinmethod
    def get_MaxCopies(self: Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties) -> UInt32: ...
    @winrt_mixinmethod
    def put_NumberOfCopies(self: Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_NumberOfCopies(self: Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties) -> UInt32: ...
    @winrt_mixinmethod
    def get_DisplayedOptions(self: Windows.Graphics.Printing.IPrintTaskOptionsCoreUIConfiguration) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def put_Bordering(self: Windows.Graphics.Printing.IPrintTaskOptions, value: Windows.Graphics.Printing.PrintBordering) -> Void: ...
    @winrt_mixinmethod
    def get_Bordering(self: Windows.Graphics.Printing.IPrintTaskOptions) -> Windows.Graphics.Printing.PrintBordering: ...
    @winrt_mixinmethod
    def GetPagePrintTicket(self: Windows.Graphics.Printing.IPrintTaskOptions, printPageInfo: Windows.Graphics.Printing.PrintPageInfo) -> Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def get_PageRangeOptions(self: Windows.Graphics.Printing.IPrintTaskOptions2) -> Windows.Graphics.Printing.PrintPageRangeOptions: ...
    @winrt_mixinmethod
    def get_CustomPageRanges(self: Windows.Graphics.Printing.IPrintTaskOptions2) -> Windows.Foundation.Collections.IVector[Windows.Graphics.Printing.PrintPageRange]: ...
    MediaSize = property(get_MediaSize, put_MediaSize)
    MediaType = property(get_MediaType, put_MediaType)
    Orientation = property(get_Orientation, put_Orientation)
    PrintQuality = property(get_PrintQuality, put_PrintQuality)
    ColorMode = property(get_ColorMode, put_ColorMode)
    Duplex = property(get_Duplex, put_Duplex)
    Collation = property(get_Collation, put_Collation)
    Staple = property(get_Staple, put_Staple)
    HolePunch = property(get_HolePunch, put_HolePunch)
    Binding = property(get_Binding, put_Binding)
    MinCopies = property(get_MinCopies, None)
    MaxCopies = property(get_MaxCopies, None)
    NumberOfCopies = property(get_NumberOfCopies, put_NumberOfCopies)
    DisplayedOptions = property(get_DisplayedOptions, None)
    Bordering = property(get_Bordering, put_Bordering)
    PageRangeOptions = property(get_PageRangeOptions, None)
    CustomPageRanges = property(get_CustomPageRanges, None)
class PrintTaskProgressingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.IPrintTaskProgressingEventArgs
    _classid_ = 'Windows.Graphics.Printing.PrintTaskProgressingEventArgs'
    @winrt_mixinmethod
    def get_DocumentPageCount(self: Windows.Graphics.Printing.IPrintTaskProgressingEventArgs) -> UInt32: ...
    DocumentPageCount = property(get_DocumentPageCount, None)
class PrintTaskRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.IPrintTaskRequest
    _classid_ = 'Windows.Graphics.Printing.PrintTaskRequest'
    @winrt_mixinmethod
    def get_Deadline(self: Windows.Graphics.Printing.IPrintTaskRequest) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def CreatePrintTask(self: Windows.Graphics.Printing.IPrintTaskRequest, title: WinRT_String, handler: Windows.Graphics.Printing.PrintTaskSourceRequestedHandler) -> Windows.Graphics.Printing.PrintTask: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Graphics.Printing.IPrintTaskRequest) -> Windows.Graphics.Printing.PrintTaskRequestedDeferral: ...
    Deadline = property(get_Deadline, None)
class PrintTaskRequestedDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.IPrintTaskRequestedDeferral
    _classid_ = 'Windows.Graphics.Printing.PrintTaskRequestedDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.Graphics.Printing.IPrintTaskRequestedDeferral) -> Void: ...
class PrintTaskRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.IPrintTaskRequestedEventArgs
    _classid_ = 'Windows.Graphics.Printing.PrintTaskRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.Graphics.Printing.IPrintTaskRequestedEventArgs) -> Windows.Graphics.Printing.PrintTaskRequest: ...
    Request = property(get_Request, None)
class PrintTaskSourceRequestedArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.IPrintTaskSourceRequestedArgs
    _classid_ = 'Windows.Graphics.Printing.PrintTaskSourceRequestedArgs'
    @winrt_mixinmethod
    def get_Deadline(self: Windows.Graphics.Printing.IPrintTaskSourceRequestedArgs) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def SetSource(self: Windows.Graphics.Printing.IPrintTaskSourceRequestedArgs, source: Windows.Graphics.Printing.IPrintDocumentSource) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Graphics.Printing.IPrintTaskSourceRequestedArgs) -> Windows.Graphics.Printing.PrintTaskSourceRequestedDeferral: ...
    Deadline = property(get_Deadline, None)
class PrintTaskSourceRequestedDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.IPrintTaskSourceRequestedDeferral
    _classid_ = 'Windows.Graphics.Printing.PrintTaskSourceRequestedDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.Graphics.Printing.IPrintTaskSourceRequestedDeferral) -> Void: ...
class PrintTaskSourceRequestedHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6c109fa8-5cb6-4b3a-8663-f39cb02dc9b4}')
    _classid_ = 'Windows.Graphics.Printing.PrintTaskSourceRequestedHandler'
    @winrt_commethod(3)
    def Invoke(self, args: Windows.Graphics.Printing.PrintTaskSourceRequestedArgs) -> Void: ...
class StandardPrintTaskOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    @winrt_classmethod
    def get_CustomPageRanges(cls: Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic3) -> WinRT_String: ...
    @winrt_classmethod
    def get_Bordering(cls: Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic2) -> WinRT_String: ...
    @winrt_classmethod
    def get_MediaSize(cls: Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic) -> WinRT_String: ...
    @winrt_classmethod
    def get_MediaType(cls: Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic) -> WinRT_String: ...
    @winrt_classmethod
    def get_Orientation(cls: Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic) -> WinRT_String: ...
    @winrt_classmethod
    def get_PrintQuality(cls: Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic) -> WinRT_String: ...
    @winrt_classmethod
    def get_ColorMode(cls: Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic) -> WinRT_String: ...
    @winrt_classmethod
    def get_Duplex(cls: Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic) -> WinRT_String: ...
    @winrt_classmethod
    def get_Collation(cls: Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic) -> WinRT_String: ...
    @winrt_classmethod
    def get_Staple(cls: Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic) -> WinRT_String: ...
    @winrt_classmethod
    def get_HolePunch(cls: Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic) -> WinRT_String: ...
    @winrt_classmethod
    def get_Binding(cls: Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic) -> WinRT_String: ...
    @winrt_classmethod
    def get_Copies(cls: Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic) -> WinRT_String: ...
    @winrt_classmethod
    def get_NUp(cls: Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic) -> WinRT_String: ...
    @winrt_classmethod
    def get_InputBin(cls: Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic) -> WinRT_String: ...
    CustomPageRanges = property(get_CustomPageRanges, None)
    Bordering = property(get_Bordering, None)
    MediaSize = property(get_MediaSize, None)
    MediaType = property(get_MediaType, None)
    Orientation = property(get_Orientation, None)
    PrintQuality = property(get_PrintQuality, None)
    ColorMode = property(get_ColorMode, None)
    Duplex = property(get_Duplex, None)
    Collation = property(get_Collation, None)
    Staple = property(get_Staple, None)
    HolePunch = property(get_HolePunch, None)
    Binding = property(get_Binding, None)
    Copies = property(get_Copies, None)
    NUp = property(get_NUp, None)
    InputBin = property(get_InputBin, None)
make_head(_module, 'IPrintDocumentSource')
make_head(_module, 'IPrintManager')
make_head(_module, 'IPrintManagerStatic')
make_head(_module, 'IPrintManagerStatic2')
make_head(_module, 'IPrintPageInfo')
make_head(_module, 'IPrintPageRange')
make_head(_module, 'IPrintPageRangeFactory')
make_head(_module, 'IPrintPageRangeOptions')
make_head(_module, 'IPrintTask')
make_head(_module, 'IPrintTask2')
make_head(_module, 'IPrintTaskCompletedEventArgs')
make_head(_module, 'IPrintTaskOptions')
make_head(_module, 'IPrintTaskOptions2')
make_head(_module, 'IPrintTaskOptionsCore')
make_head(_module, 'IPrintTaskOptionsCoreProperties')
make_head(_module, 'IPrintTaskOptionsCoreUIConfiguration')
make_head(_module, 'IPrintTaskProgressingEventArgs')
make_head(_module, 'IPrintTaskRequest')
make_head(_module, 'IPrintTaskRequestedDeferral')
make_head(_module, 'IPrintTaskRequestedEventArgs')
make_head(_module, 'IPrintTaskSourceRequestedArgs')
make_head(_module, 'IPrintTaskSourceRequestedDeferral')
make_head(_module, 'IPrintTaskTargetDeviceSupport')
make_head(_module, 'IStandardPrintTaskOptionsStatic')
make_head(_module, 'IStandardPrintTaskOptionsStatic2')
make_head(_module, 'IStandardPrintTaskOptionsStatic3')
make_head(_module, 'PrintManager')
make_head(_module, 'PrintPageDescription')
make_head(_module, 'PrintPageInfo')
make_head(_module, 'PrintPageRange')
make_head(_module, 'PrintPageRangeOptions')
make_head(_module, 'PrintTask')
make_head(_module, 'PrintTaskCompletedEventArgs')
make_head(_module, 'PrintTaskOptions')
make_head(_module, 'PrintTaskProgressingEventArgs')
make_head(_module, 'PrintTaskRequest')
make_head(_module, 'PrintTaskRequestedDeferral')
make_head(_module, 'PrintTaskRequestedEventArgs')
make_head(_module, 'PrintTaskSourceRequestedArgs')
make_head(_module, 'PrintTaskSourceRequestedDeferral')
make_head(_module, 'PrintTaskSourceRequestedHandler')
make_head(_module, 'StandardPrintTaskOptions')
