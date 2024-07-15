from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.DataTransfer
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Graphics.Printing
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class IPrintDocumentSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.IPrintDocumentSource'
    _iid_ = Guid('{dedc0c30-f1eb-47df-aae6-ed5427511f01}')
class IPrintManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.IPrintManager'
    _iid_ = Guid('{ff2a9694-8c99-44fd-ae4a-19d9aa9a0f0a}')
    @winrt_commethod(6)
    def add_PrintTaskRequested(self, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.PrintManager, win32more.Windows.Graphics.Printing.PrintTaskRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PrintTaskRequested(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    PrintTaskRequested = event()
class IPrintManagerStatic(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.IPrintManagerStatic'
    _iid_ = Guid('{58185dcd-e634-4654-84f0-e0152a8217ac}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.Graphics.Printing.PrintManager: ...
    @winrt_commethod(7)
    def ShowPrintUIAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class IPrintManagerStatic2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.IPrintManagerStatic2'
    _iid_ = Guid('{35a99955-e6ab-4139-9abd-b86a729b3598}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
class IPrintPageInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.IPrintPageInfo'
    _iid_ = Guid('{dd4be9c9-a6a1-4ada-930e-da872a4f23d3}')
    @winrt_commethod(6)
    def put_MediaSize(self, value: win32more.Windows.Graphics.Printing.PrintMediaSize) -> Void: ...
    @winrt_commethod(7)
    def get_MediaSize(self) -> win32more.Windows.Graphics.Printing.PrintMediaSize: ...
    @winrt_commethod(8)
    def put_PageSize(self, value: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_commethod(9)
    def get_PageSize(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(10)
    def put_DpiX(self, value: UInt32) -> Void: ...
    @winrt_commethod(11)
    def get_DpiX(self) -> UInt32: ...
    @winrt_commethod(12)
    def put_DpiY(self, value: UInt32) -> Void: ...
    @winrt_commethod(13)
    def get_DpiY(self) -> UInt32: ...
    @winrt_commethod(14)
    def put_Orientation(self, value: win32more.Windows.Graphics.Printing.PrintOrientation) -> Void: ...
    @winrt_commethod(15)
    def get_Orientation(self) -> win32more.Windows.Graphics.Printing.PrintOrientation: ...
    DpiX = property(get_DpiX, put_DpiX)
    DpiY = property(get_DpiY, put_DpiY)
    MediaSize = property(get_MediaSize, put_MediaSize)
    Orientation = property(get_Orientation, put_Orientation)
    PageSize = property(get_PageSize, put_PageSize)
class IPrintPageRange(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.IPrintPageRange'
    _iid_ = Guid('{f8a06c54-6e7c-51c5-57fd-0660c2d71513}')
    @winrt_commethod(6)
    def get_FirstPageNumber(self) -> Int32: ...
    @winrt_commethod(7)
    def get_LastPageNumber(self) -> Int32: ...
    FirstPageNumber = property(get_FirstPageNumber, None)
    LastPageNumber = property(get_LastPageNumber, None)
class IPrintPageRangeFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.IPrintPageRangeFactory'
    _iid_ = Guid('{408fd45f-e047-5f85-7129-fb085a4fad14}')
    @winrt_commethod(6)
    def Create(self, firstPage: Int32, lastPage: Int32) -> win32more.Windows.Graphics.Printing.PrintPageRange: ...
    @winrt_commethod(7)
    def CreateWithSinglePage(self, page: Int32) -> win32more.Windows.Graphics.Printing.PrintPageRange: ...
class IPrintPageRangeOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.IPrintPageRangeOptions'
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.IPrintTask'
    _iid_ = Guid('{61d80247-6cf6-4fad-84e2-a5e82e2d4ceb}')
    @winrt_commethod(6)
    def get_Properties(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackagePropertySet: ...
    @winrt_commethod(7)
    def get_Source(self) -> win32more.Windows.Graphics.Printing.IPrintDocumentSource: ...
    @winrt_commethod(8)
    def get_Options(self) -> win32more.Windows.Graphics.Printing.PrintTaskOptions: ...
    @winrt_commethod(9)
    def add_Previewing(self, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.PrintTask, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Previewing(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_Submitting(self, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.PrintTask, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Submitting(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_Progressing(self, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.PrintTask, win32more.Windows.Graphics.Printing.PrintTaskProgressingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_Progressing(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def add_Completed(self, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.PrintTask, win32more.Windows.Graphics.Printing.PrintTaskCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_Completed(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Options = property(get_Options, None)
    Properties = property(get_Properties, None)
    Source = property(get_Source, None)
    Previewing = event()
    Submitting = event()
    Progressing = event()
    Completed = event()
class IPrintTask2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.IPrintTask2'
    _iid_ = Guid('{36234877-3e53-4d9d-8f5e-316ac8dedae1}')
    @winrt_commethod(6)
    def put_IsPreviewEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_IsPreviewEnabled(self) -> Boolean: ...
    IsPreviewEnabled = property(get_IsPreviewEnabled, put_IsPreviewEnabled)
class IPrintTaskCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.IPrintTaskCompletedEventArgs'
    _iid_ = Guid('{5bcd34af-24e9-4c10-8d07-14c346ba3fce}')
    @winrt_commethod(6)
    def get_Completion(self) -> win32more.Windows.Graphics.Printing.PrintTaskCompletion: ...
    Completion = property(get_Completion, None)
class IPrintTaskOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.IPrintTaskOptions'
    _iid_ = Guid('{5a0a66bb-d289-41bb-96dd-57e28338ae3f}')
    @winrt_commethod(6)
    def put_Bordering(self, value: win32more.Windows.Graphics.Printing.PrintBordering) -> Void: ...
    @winrt_commethod(7)
    def get_Bordering(self) -> win32more.Windows.Graphics.Printing.PrintBordering: ...
    @winrt_commethod(8)
    def GetPagePrintTicket(self, printPageInfo: win32more.Windows.Graphics.Printing.PrintPageInfo) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    Bordering = property(get_Bordering, put_Bordering)
class IPrintTaskOptions2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.IPrintTaskOptions2'
    _iid_ = Guid('{eb9b1606-9a36-4b59-8617-b217849262e1}')
    @winrt_commethod(6)
    def get_PageRangeOptions(self) -> win32more.Windows.Graphics.Printing.PrintPageRangeOptions: ...
    @winrt_commethod(7)
    def get_CustomPageRanges(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing.PrintPageRange]: ...
    CustomPageRanges = property(get_CustomPageRanges, None)
    PageRangeOptions = property(get_PageRangeOptions, None)
class IPrintTaskOptionsCore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.IPrintTaskOptionsCore'
    _iid_ = Guid('{1bdbb474-4ed1-41eb-be3c-72d18ed67337}')
    @winrt_commethod(6)
    def GetPageDescription(self, jobPageNumber: UInt32) -> win32more.Windows.Graphics.Printing.PrintPageDescription: ...
class IPrintTaskOptionsCoreProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties'
    _iid_ = Guid('{c1b71832-9e93-4e55-814b-3326a59efce1}')
    @winrt_commethod(6)
    def put_MediaSize(self, value: win32more.Windows.Graphics.Printing.PrintMediaSize) -> Void: ...
    @winrt_commethod(7)
    def get_MediaSize(self) -> win32more.Windows.Graphics.Printing.PrintMediaSize: ...
    @winrt_commethod(8)
    def put_MediaType(self, value: win32more.Windows.Graphics.Printing.PrintMediaType) -> Void: ...
    @winrt_commethod(9)
    def get_MediaType(self) -> win32more.Windows.Graphics.Printing.PrintMediaType: ...
    @winrt_commethod(10)
    def put_Orientation(self, value: win32more.Windows.Graphics.Printing.PrintOrientation) -> Void: ...
    @winrt_commethod(11)
    def get_Orientation(self) -> win32more.Windows.Graphics.Printing.PrintOrientation: ...
    @winrt_commethod(12)
    def put_PrintQuality(self, value: win32more.Windows.Graphics.Printing.PrintQuality) -> Void: ...
    @winrt_commethod(13)
    def get_PrintQuality(self) -> win32more.Windows.Graphics.Printing.PrintQuality: ...
    @winrt_commethod(14)
    def put_ColorMode(self, value: win32more.Windows.Graphics.Printing.PrintColorMode) -> Void: ...
    @winrt_commethod(15)
    def get_ColorMode(self) -> win32more.Windows.Graphics.Printing.PrintColorMode: ...
    @winrt_commethod(16)
    def put_Duplex(self, value: win32more.Windows.Graphics.Printing.PrintDuplex) -> Void: ...
    @winrt_commethod(17)
    def get_Duplex(self) -> win32more.Windows.Graphics.Printing.PrintDuplex: ...
    @winrt_commethod(18)
    def put_Collation(self, value: win32more.Windows.Graphics.Printing.PrintCollation) -> Void: ...
    @winrt_commethod(19)
    def get_Collation(self) -> win32more.Windows.Graphics.Printing.PrintCollation: ...
    @winrt_commethod(20)
    def put_Staple(self, value: win32more.Windows.Graphics.Printing.PrintStaple) -> Void: ...
    @winrt_commethod(21)
    def get_Staple(self) -> win32more.Windows.Graphics.Printing.PrintStaple: ...
    @winrt_commethod(22)
    def put_HolePunch(self, value: win32more.Windows.Graphics.Printing.PrintHolePunch) -> Void: ...
    @winrt_commethod(23)
    def get_HolePunch(self) -> win32more.Windows.Graphics.Printing.PrintHolePunch: ...
    @winrt_commethod(24)
    def put_Binding(self, value: win32more.Windows.Graphics.Printing.PrintBinding) -> Void: ...
    @winrt_commethod(25)
    def get_Binding(self) -> win32more.Windows.Graphics.Printing.PrintBinding: ...
    @winrt_commethod(26)
    def get_MinCopies(self) -> UInt32: ...
    @winrt_commethod(27)
    def get_MaxCopies(self) -> UInt32: ...
    @winrt_commethod(28)
    def put_NumberOfCopies(self, value: UInt32) -> Void: ...
    @winrt_commethod(29)
    def get_NumberOfCopies(self) -> UInt32: ...
    Binding = property(get_Binding, put_Binding)
    Collation = property(get_Collation, put_Collation)
    ColorMode = property(get_ColorMode, put_ColorMode)
    Duplex = property(get_Duplex, put_Duplex)
    HolePunch = property(get_HolePunch, put_HolePunch)
    MaxCopies = property(get_MaxCopies, None)
    MediaSize = property(get_MediaSize, put_MediaSize)
    MediaType = property(get_MediaType, put_MediaType)
    MinCopies = property(get_MinCopies, None)
    NumberOfCopies = property(get_NumberOfCopies, put_NumberOfCopies)
    Orientation = property(get_Orientation, put_Orientation)
    PrintQuality = property(get_PrintQuality, put_PrintQuality)
    Staple = property(get_Staple, put_Staple)
class IPrintTaskOptionsCoreUIConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.IPrintTaskOptionsCoreUIConfiguration'
    _iid_ = Guid('{62e69e23-9a1e-4336-b74f-3cc7f4cff709}')
    @winrt_commethod(6)
    def get_DisplayedOptions(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    DisplayedOptions = property(get_DisplayedOptions, None)
class IPrintTaskProgressingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.IPrintTaskProgressingEventArgs'
    _iid_ = Guid('{810cd3cb-b410-4282-a073-5ac378234174}')
    @winrt_commethod(6)
    def get_DocumentPageCount(self) -> UInt32: ...
    DocumentPageCount = property(get_DocumentPageCount, None)
class IPrintTaskRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.IPrintTaskRequest'
    _iid_ = Guid('{6ff61e2e-2722-4240-a67c-f364849a17f3}')
    @winrt_commethod(6)
    def get_Deadline(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def CreatePrintTask(self, title: WinRT_String, handler: win32more.Windows.Graphics.Printing.PrintTaskSourceRequestedHandler) -> win32more.Windows.Graphics.Printing.PrintTask: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.Graphics.Printing.PrintTaskRequestedDeferral: ...
    Deadline = property(get_Deadline, None)
class IPrintTaskRequestedDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.IPrintTaskRequestedDeferral'
    _iid_ = Guid('{cfefb3f0-ce3e-42c7-9496-64800c622c44}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IPrintTaskRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.IPrintTaskRequestedEventArgs'
    _iid_ = Guid('{d0aff924-a31b-454c-a7b6-5d0cc522fc16}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.Graphics.Printing.PrintTaskRequest: ...
    Request = property(get_Request, None)
class IPrintTaskSourceRequestedArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.IPrintTaskSourceRequestedArgs'
    _iid_ = Guid('{f9f067be-f456-41f0-9c98-5ce73e851410}')
    @winrt_commethod(6)
    def get_Deadline(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def SetSource(self, source: win32more.Windows.Graphics.Printing.IPrintDocumentSource) -> Void: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.Graphics.Printing.PrintTaskSourceRequestedDeferral: ...
    Deadline = property(get_Deadline, None)
class IPrintTaskSourceRequestedDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.IPrintTaskSourceRequestedDeferral'
    _iid_ = Guid('{4a1560d1-6992-4d9d-8555-4ca4563fb166}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IPrintTaskTargetDeviceSupport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.IPrintTaskTargetDeviceSupport'
    _iid_ = Guid('{295d70c0-c2cb-4b7d-b0ea-93095091a220}')
    @winrt_commethod(6)
    def put_IsPrinterTargetEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_IsPrinterTargetEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Is3DManufacturingTargetEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_Is3DManufacturingTargetEnabled(self) -> Boolean: ...
    Is3DManufacturingTargetEnabled = property(get_Is3DManufacturingTargetEnabled, put_Is3DManufacturingTargetEnabled)
    IsPrinterTargetEnabled = property(get_IsPrinterTargetEnabled, put_IsPrinterTargetEnabled)
class IStandardPrintTaskOptionsStatic(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic'
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
    Binding = property(get_Binding, None)
    Collation = property(get_Collation, None)
    ColorMode = property(get_ColorMode, None)
    Copies = property(get_Copies, None)
    Duplex = property(get_Duplex, None)
    HolePunch = property(get_HolePunch, None)
    InputBin = property(get_InputBin, None)
    MediaSize = property(get_MediaSize, None)
    MediaType = property(get_MediaType, None)
    NUp = property(get_NUp, None)
    Orientation = property(get_Orientation, None)
    PrintQuality = property(get_PrintQuality, None)
    Staple = property(get_Staple, None)
class IStandardPrintTaskOptionsStatic2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic2'
    _iid_ = Guid('{3be38bf4-7a44-4269-9a52-81261e289ee9}')
    @winrt_commethod(6)
    def get_Bordering(self) -> WinRT_String: ...
    Bordering = property(get_Bordering, None)
class IStandardPrintTaskOptionsStatic3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic3'
    _iid_ = Guid('{bbf68e86-3858-41b3-a799-55dd9888d475}')
    @winrt_commethod(6)
    def get_CustomPageRanges(self) -> WinRT_String: ...
    CustomPageRanges = property(get_CustomPageRanges, None)
class PrintBinding(Enum, Int32):
    Default = 0
    NotAvailable = 1
    PrinterCustom = 2
    None_ = 3
    Bale = 4
    BindBottom = 5
    BindLeft = 6
    BindRight = 7
    BindTop = 8
    Booklet = 9
    EdgeStitchBottom = 10
    EdgeStitchLeft = 11
    EdgeStitchRight = 12
    EdgeStitchTop = 13
    Fold = 14
    JogOffset = 15
    Trim = 16
class PrintBordering(Enum, Int32):
    Default = 0
    NotAvailable = 1
    PrinterCustom = 2
    Bordered = 3
    Borderless = 4
class PrintCollation(Enum, Int32):
    Default = 0
    NotAvailable = 1
    PrinterCustom = 2
    Collated = 3
    Uncollated = 4
class PrintColorMode(Enum, Int32):
    Default = 0
    NotAvailable = 1
    PrinterCustom = 2
    Color = 3
    Grayscale = 4
    Monochrome = 5
    AutoSelect = 6
class PrintDuplex(Enum, Int32):
    Default = 0
    NotAvailable = 1
    PrinterCustom = 2
    OneSided = 3
    TwoSidedShortEdge = 4
    TwoSidedLongEdge = 5
class PrintHolePunch(Enum, Int32):
    Default = 0
    NotAvailable = 1
    PrinterCustom = 2
    None_ = 3
    LeftEdge = 4
    RightEdge = 5
    TopEdge = 6
    BottomEdge = 7
class PrintManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.IPrintManager
    _classid_ = 'Windows.Graphics.Printing.PrintManager'
    @winrt_mixinmethod
    def add_PrintTaskRequested(self: win32more.Windows.Graphics.Printing.IPrintManager, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.PrintManager, win32more.Windows.Graphics.Printing.PrintTaskRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PrintTaskRequested(self: win32more.Windows.Graphics.Printing.IPrintManager, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def IsSupported(cls: win32more.Windows.Graphics.Printing.IPrintManagerStatic2) -> Boolean: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.Graphics.Printing.IPrintManagerStatic) -> win32more.Windows.Graphics.Printing.PrintManager: ...
    @winrt_classmethod
    def ShowPrintUIAsync(cls: win32more.Windows.Graphics.Printing.IPrintManagerStatic) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    PrintTaskRequested = event()
class PrintMediaSize(Enum, Int32):
    Default = 0
    NotAvailable = 1
    PrinterCustom = 2
    BusinessCard = 3
    CreditCard = 4
    IsoA0 = 5
    IsoA1 = 6
    IsoA10 = 7
    IsoA2 = 8
    IsoA3 = 9
    IsoA3Extra = 10
    IsoA3Rotated = 11
    IsoA4 = 12
    IsoA4Extra = 13
    IsoA4Rotated = 14
    IsoA5 = 15
    IsoA5Extra = 16
    IsoA5Rotated = 17
    IsoA6 = 18
    IsoA6Rotated = 19
    IsoA7 = 20
    IsoA8 = 21
    IsoA9 = 22
    IsoB0 = 23
    IsoB1 = 24
    IsoB10 = 25
    IsoB2 = 26
    IsoB3 = 27
    IsoB4 = 28
    IsoB4Envelope = 29
    IsoB5Envelope = 30
    IsoB5Extra = 31
    IsoB7 = 32
    IsoB8 = 33
    IsoB9 = 34
    IsoC0 = 35
    IsoC1 = 36
    IsoC10 = 37
    IsoC2 = 38
    IsoC3 = 39
    IsoC3Envelope = 40
    IsoC4 = 41
    IsoC4Envelope = 42
    IsoC5 = 43
    IsoC5Envelope = 44
    IsoC6 = 45
    IsoC6C5Envelope = 46
    IsoC6Envelope = 47
    IsoC7 = 48
    IsoC8 = 49
    IsoC9 = 50
    IsoDLEnvelope = 51
    IsoDLEnvelopeRotated = 52
    IsoSRA3 = 53
    Japan2LPhoto = 54
    JapanChou3Envelope = 55
    JapanChou3EnvelopeRotated = 56
    JapanChou4Envelope = 57
    JapanChou4EnvelopeRotated = 58
    JapanDoubleHagakiPostcard = 59
    JapanDoubleHagakiPostcardRotated = 60
    JapanHagakiPostcard = 61
    JapanHagakiPostcardRotated = 62
    JapanKaku2Envelope = 63
    JapanKaku2EnvelopeRotated = 64
    JapanKaku3Envelope = 65
    JapanKaku3EnvelopeRotated = 66
    JapanLPhoto = 67
    JapanQuadrupleHagakiPostcard = 68
    JapanYou1Envelope = 69
    JapanYou2Envelope = 70
    JapanYou3Envelope = 71
    JapanYou4Envelope = 72
    JapanYou4EnvelopeRotated = 73
    JapanYou6Envelope = 74
    JapanYou6EnvelopeRotated = 75
    JisB0 = 76
    JisB1 = 77
    JisB10 = 78
    JisB2 = 79
    JisB3 = 80
    JisB4 = 81
    JisB4Rotated = 82
    JisB5 = 83
    JisB5Rotated = 84
    JisB6 = 85
    JisB6Rotated = 86
    JisB7 = 87
    JisB8 = 88
    JisB9 = 89
    NorthAmerica10x11 = 90
    NorthAmerica10x12 = 91
    NorthAmerica10x14 = 92
    NorthAmerica11x17 = 93
    NorthAmerica14x17 = 94
    NorthAmerica4x6 = 95
    NorthAmerica4x8 = 96
    NorthAmerica5x7 = 97
    NorthAmerica8x10 = 98
    NorthAmerica9x11 = 99
    NorthAmericaArchitectureASheet = 100
    NorthAmericaArchitectureBSheet = 101
    NorthAmericaArchitectureCSheet = 102
    NorthAmericaArchitectureDSheet = 103
    NorthAmericaArchitectureESheet = 104
    NorthAmericaCSheet = 105
    NorthAmericaDSheet = 106
    NorthAmericaESheet = 107
    NorthAmericaExecutive = 108
    NorthAmericaGermanLegalFanfold = 109
    NorthAmericaGermanStandardFanfold = 110
    NorthAmericaLegal = 111
    NorthAmericaLegalExtra = 112
    NorthAmericaLetter = 113
    NorthAmericaLetterExtra = 114
    NorthAmericaLetterPlus = 115
    NorthAmericaLetterRotated = 116
    NorthAmericaMonarchEnvelope = 117
    NorthAmericaNote = 118
    NorthAmericaNumber10Envelope = 119
    NorthAmericaNumber10EnvelopeRotated = 120
    NorthAmericaNumber11Envelope = 121
    NorthAmericaNumber12Envelope = 122
    NorthAmericaNumber14Envelope = 123
    NorthAmericaNumber9Envelope = 124
    NorthAmericaPersonalEnvelope = 125
    NorthAmericaQuarto = 126
    NorthAmericaStatement = 127
    NorthAmericaSuperA = 128
    NorthAmericaSuperB = 129
    NorthAmericaTabloid = 130
    NorthAmericaTabloidExtra = 131
    OtherMetricA3Plus = 132
    OtherMetricA4Plus = 133
    OtherMetricFolio = 134
    OtherMetricInviteEnvelope = 135
    OtherMetricItalianEnvelope = 136
    Prc10Envelope = 137
    Prc10EnvelopeRotated = 138
    Prc16K = 139
    Prc16KRotated = 140
    Prc1Envelope = 141
    Prc1EnvelopeRotated = 142
    Prc2Envelope = 143
    Prc2EnvelopeRotated = 144
    Prc32K = 145
    Prc32KBig = 146
    Prc32KRotated = 147
    Prc3Envelope = 148
    Prc3EnvelopeRotated = 149
    Prc4Envelope = 150
    Prc4EnvelopeRotated = 151
    Prc5Envelope = 152
    Prc5EnvelopeRotated = 153
    Prc6Envelope = 154
    Prc6EnvelopeRotated = 155
    Prc7Envelope = 156
    Prc7EnvelopeRotated = 157
    Prc8Envelope = 158
    Prc8EnvelopeRotated = 159
    Prc9Envelope = 160
    Prc9EnvelopeRotated = 161
    Roll04Inch = 162
    Roll06Inch = 163
    Roll08Inch = 164
    Roll12Inch = 165
    Roll15Inch = 166
    Roll18Inch = 167
    Roll22Inch = 168
    Roll24Inch = 169
    Roll30Inch = 170
    Roll36Inch = 171
    Roll54Inch = 172
class PrintMediaType(Enum, Int32):
    Default = 0
    NotAvailable = 1
    PrinterCustom = 2
    AutoSelect = 3
    Archival = 4
    BackPrintFilm = 5
    Bond = 6
    CardStock = 7
    Continuous = 8
    EnvelopePlain = 9
    EnvelopeWindow = 10
    Fabric = 11
    HighResolution = 12
    Label = 13
    MultiLayerForm = 14
    MultiPartForm = 15
    Photographic = 16
    PhotographicFilm = 17
    PhotographicGlossy = 18
    PhotographicHighGloss = 19
    PhotographicMatte = 20
    PhotographicSatin = 21
    PhotographicSemiGloss = 22
    Plain = 23
    Screen = 24
    ScreenPaged = 25
    Stationery = 26
    TabStockFull = 27
    TabStockPreCut = 28
    Transparency = 29
    TShirtTransfer = 30
    None_ = 31
class PrintOrientation(Enum, Int32):
    Default = 0
    NotAvailable = 1
    PrinterCustom = 2
    Portrait = 3
    PortraitFlipped = 4
    Landscape = 5
    LandscapeFlipped = 6
class PrintPageDescription(Structure):
    PageSize: win32more.Windows.Foundation.Size
    ImageableRect: win32more.Windows.Foundation.Rect
    DpiX: UInt32
    DpiY: UInt32
class PrintPageInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.IPrintPageInfo
    _classid_ = 'Windows.Graphics.Printing.PrintPageInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Graphics.Printing.PrintPageInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Graphics.Printing.PrintPageInfo: ...
    @winrt_mixinmethod
    def put_MediaSize(self: win32more.Windows.Graphics.Printing.IPrintPageInfo, value: win32more.Windows.Graphics.Printing.PrintMediaSize) -> Void: ...
    @winrt_mixinmethod
    def get_MediaSize(self: win32more.Windows.Graphics.Printing.IPrintPageInfo) -> win32more.Windows.Graphics.Printing.PrintMediaSize: ...
    @winrt_mixinmethod
    def put_PageSize(self: win32more.Windows.Graphics.Printing.IPrintPageInfo, value: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_mixinmethod
    def get_PageSize(self: win32more.Windows.Graphics.Printing.IPrintPageInfo) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def put_DpiX(self: win32more.Windows.Graphics.Printing.IPrintPageInfo, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_DpiX(self: win32more.Windows.Graphics.Printing.IPrintPageInfo) -> UInt32: ...
    @winrt_mixinmethod
    def put_DpiY(self: win32more.Windows.Graphics.Printing.IPrintPageInfo, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_DpiY(self: win32more.Windows.Graphics.Printing.IPrintPageInfo) -> UInt32: ...
    @winrt_mixinmethod
    def put_Orientation(self: win32more.Windows.Graphics.Printing.IPrintPageInfo, value: win32more.Windows.Graphics.Printing.PrintOrientation) -> Void: ...
    @winrt_mixinmethod
    def get_Orientation(self: win32more.Windows.Graphics.Printing.IPrintPageInfo) -> win32more.Windows.Graphics.Printing.PrintOrientation: ...
    DpiX = property(get_DpiX, put_DpiX)
    DpiY = property(get_DpiY, put_DpiY)
    MediaSize = property(get_MediaSize, put_MediaSize)
    Orientation = property(get_Orientation, put_Orientation)
    PageSize = property(get_PageSize, put_PageSize)
class PrintPageRange(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.IPrintPageRange
    _classid_ = 'Windows.Graphics.Printing.PrintPageRange'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Graphics.Printing.PrintPageRange.CreateWithSinglePage(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Graphics.Printing.PrintPageRange.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateWithSinglePage(cls: win32more.Windows.Graphics.Printing.IPrintPageRangeFactory, page: Int32) -> win32more.Windows.Graphics.Printing.PrintPageRange: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Graphics.Printing.IPrintPageRangeFactory, firstPage: Int32, lastPage: Int32) -> win32more.Windows.Graphics.Printing.PrintPageRange: ...
    @winrt_mixinmethod
    def get_FirstPageNumber(self: win32more.Windows.Graphics.Printing.IPrintPageRange) -> Int32: ...
    @winrt_mixinmethod
    def get_LastPageNumber(self: win32more.Windows.Graphics.Printing.IPrintPageRange) -> Int32: ...
    FirstPageNumber = property(get_FirstPageNumber, None)
    LastPageNumber = property(get_LastPageNumber, None)
class PrintPageRangeOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.IPrintPageRangeOptions
    _classid_ = 'Windows.Graphics.Printing.PrintPageRangeOptions'
    @winrt_mixinmethod
    def put_AllowAllPages(self: win32more.Windows.Graphics.Printing.IPrintPageRangeOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AllowAllPages(self: win32more.Windows.Graphics.Printing.IPrintPageRangeOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowCurrentPage(self: win32more.Windows.Graphics.Printing.IPrintPageRangeOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AllowCurrentPage(self: win32more.Windows.Graphics.Printing.IPrintPageRangeOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowCustomSetOfPages(self: win32more.Windows.Graphics.Printing.IPrintPageRangeOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AllowCustomSetOfPages(self: win32more.Windows.Graphics.Printing.IPrintPageRangeOptions) -> Boolean: ...
    AllowAllPages = property(get_AllowAllPages, put_AllowAllPages)
    AllowCurrentPage = property(get_AllowCurrentPage, put_AllowCurrentPage)
    AllowCustomSetOfPages = property(get_AllowCustomSetOfPages, put_AllowCustomSetOfPages)
class PrintQuality(Enum, Int32):
    Default = 0
    NotAvailable = 1
    PrinterCustom = 2
    Automatic = 3
    Draft = 4
    Fax = 5
    High = 6
    Normal = 7
    Photographic = 8
    Text = 9
class PrintStaple(Enum, Int32):
    Default = 0
    NotAvailable = 1
    PrinterCustom = 2
    None_ = 3
    StapleTopLeft = 4
    StapleTopRight = 5
    StapleBottomLeft = 6
    StapleBottomRight = 7
    StapleDualLeft = 8
    StapleDualRight = 9
    StapleDualTop = 10
    StapleDualBottom = 11
    SaddleStitch = 12
class PrintTask(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.IPrintTask
    _classid_ = 'Windows.Graphics.Printing.PrintTask'
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Graphics.Printing.IPrintTask) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackagePropertySet: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.Graphics.Printing.IPrintTask) -> win32more.Windows.Graphics.Printing.IPrintDocumentSource: ...
    @winrt_mixinmethod
    def get_Options(self: win32more.Windows.Graphics.Printing.IPrintTask) -> win32more.Windows.Graphics.Printing.PrintTaskOptions: ...
    @winrt_mixinmethod
    def add_Previewing(self: win32more.Windows.Graphics.Printing.IPrintTask, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.PrintTask, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Previewing(self: win32more.Windows.Graphics.Printing.IPrintTask, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Submitting(self: win32more.Windows.Graphics.Printing.IPrintTask, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.PrintTask, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Submitting(self: win32more.Windows.Graphics.Printing.IPrintTask, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Progressing(self: win32more.Windows.Graphics.Printing.IPrintTask, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.PrintTask, win32more.Windows.Graphics.Printing.PrintTaskProgressingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Progressing(self: win32more.Windows.Graphics.Printing.IPrintTask, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Completed(self: win32more.Windows.Graphics.Printing.IPrintTask, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.PrintTask, win32more.Windows.Graphics.Printing.PrintTaskCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Completed(self: win32more.Windows.Graphics.Printing.IPrintTask, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def put_IsPrinterTargetEnabled(self: win32more.Windows.Graphics.Printing.IPrintTaskTargetDeviceSupport, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsPrinterTargetEnabled(self: win32more.Windows.Graphics.Printing.IPrintTaskTargetDeviceSupport) -> Boolean: ...
    @winrt_mixinmethod
    def put_Is3DManufacturingTargetEnabled(self: win32more.Windows.Graphics.Printing.IPrintTaskTargetDeviceSupport, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Is3DManufacturingTargetEnabled(self: win32more.Windows.Graphics.Printing.IPrintTaskTargetDeviceSupport) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsPreviewEnabled(self: win32more.Windows.Graphics.Printing.IPrintTask2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsPreviewEnabled(self: win32more.Windows.Graphics.Printing.IPrintTask2) -> Boolean: ...
    Is3DManufacturingTargetEnabled = property(get_Is3DManufacturingTargetEnabled, put_Is3DManufacturingTargetEnabled)
    IsPreviewEnabled = property(get_IsPreviewEnabled, put_IsPreviewEnabled)
    IsPrinterTargetEnabled = property(get_IsPrinterTargetEnabled, put_IsPrinterTargetEnabled)
    Options = property(get_Options, None)
    Properties = property(get_Properties, None)
    Source = property(get_Source, None)
    Previewing = event()
    Submitting = event()
    Progressing = event()
    Completed = event()
class PrintTaskCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.IPrintTaskCompletedEventArgs
    _classid_ = 'Windows.Graphics.Printing.PrintTaskCompletedEventArgs'
    @winrt_mixinmethod
    def get_Completion(self: win32more.Windows.Graphics.Printing.IPrintTaskCompletedEventArgs) -> win32more.Windows.Graphics.Printing.PrintTaskCompletion: ...
    Completion = property(get_Completion, None)
class PrintTaskCompletion(Enum, Int32):
    Abandoned = 0
    Canceled = 1
    Failed = 2
    Submitted = 3
class PrintTaskOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.IPrintTaskOptionsCore
    _classid_ = 'Windows.Graphics.Printing.PrintTaskOptions'
    @winrt_mixinmethod
    def GetPageDescription(self: win32more.Windows.Graphics.Printing.IPrintTaskOptionsCore, jobPageNumber: UInt32) -> win32more.Windows.Graphics.Printing.PrintPageDescription: ...
    @winrt_mixinmethod
    def put_MediaSize(self: win32more.Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties, value: win32more.Windows.Graphics.Printing.PrintMediaSize) -> Void: ...
    @winrt_mixinmethod
    def get_MediaSize(self: win32more.Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties) -> win32more.Windows.Graphics.Printing.PrintMediaSize: ...
    @winrt_mixinmethod
    def put_MediaType(self: win32more.Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties, value: win32more.Windows.Graphics.Printing.PrintMediaType) -> Void: ...
    @winrt_mixinmethod
    def get_MediaType(self: win32more.Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties) -> win32more.Windows.Graphics.Printing.PrintMediaType: ...
    @winrt_mixinmethod
    def put_Orientation(self: win32more.Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties, value: win32more.Windows.Graphics.Printing.PrintOrientation) -> Void: ...
    @winrt_mixinmethod
    def get_Orientation(self: win32more.Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties) -> win32more.Windows.Graphics.Printing.PrintOrientation: ...
    @winrt_mixinmethod
    def put_PrintQuality(self: win32more.Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties, value: win32more.Windows.Graphics.Printing.PrintQuality) -> Void: ...
    @winrt_mixinmethod
    def get_PrintQuality(self: win32more.Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties) -> win32more.Windows.Graphics.Printing.PrintQuality: ...
    @winrt_mixinmethod
    def put_ColorMode(self: win32more.Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties, value: win32more.Windows.Graphics.Printing.PrintColorMode) -> Void: ...
    @winrt_mixinmethod
    def get_ColorMode(self: win32more.Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties) -> win32more.Windows.Graphics.Printing.PrintColorMode: ...
    @winrt_mixinmethod
    def put_Duplex(self: win32more.Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties, value: win32more.Windows.Graphics.Printing.PrintDuplex) -> Void: ...
    @winrt_mixinmethod
    def get_Duplex(self: win32more.Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties) -> win32more.Windows.Graphics.Printing.PrintDuplex: ...
    @winrt_mixinmethod
    def put_Collation(self: win32more.Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties, value: win32more.Windows.Graphics.Printing.PrintCollation) -> Void: ...
    @winrt_mixinmethod
    def get_Collation(self: win32more.Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties) -> win32more.Windows.Graphics.Printing.PrintCollation: ...
    @winrt_mixinmethod
    def put_Staple(self: win32more.Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties, value: win32more.Windows.Graphics.Printing.PrintStaple) -> Void: ...
    @winrt_mixinmethod
    def get_Staple(self: win32more.Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties) -> win32more.Windows.Graphics.Printing.PrintStaple: ...
    @winrt_mixinmethod
    def put_HolePunch(self: win32more.Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties, value: win32more.Windows.Graphics.Printing.PrintHolePunch) -> Void: ...
    @winrt_mixinmethod
    def get_HolePunch(self: win32more.Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties) -> win32more.Windows.Graphics.Printing.PrintHolePunch: ...
    @winrt_mixinmethod
    def put_Binding(self: win32more.Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties, value: win32more.Windows.Graphics.Printing.PrintBinding) -> Void: ...
    @winrt_mixinmethod
    def get_Binding(self: win32more.Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties) -> win32more.Windows.Graphics.Printing.PrintBinding: ...
    @winrt_mixinmethod
    def get_MinCopies(self: win32more.Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties) -> UInt32: ...
    @winrt_mixinmethod
    def get_MaxCopies(self: win32more.Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties) -> UInt32: ...
    @winrt_mixinmethod
    def put_NumberOfCopies(self: win32more.Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_NumberOfCopies(self: win32more.Windows.Graphics.Printing.IPrintTaskOptionsCoreProperties) -> UInt32: ...
    @winrt_mixinmethod
    def get_DisplayedOptions(self: win32more.Windows.Graphics.Printing.IPrintTaskOptionsCoreUIConfiguration) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def put_Bordering(self: win32more.Windows.Graphics.Printing.IPrintTaskOptions, value: win32more.Windows.Graphics.Printing.PrintBordering) -> Void: ...
    @winrt_mixinmethod
    def get_Bordering(self: win32more.Windows.Graphics.Printing.IPrintTaskOptions) -> win32more.Windows.Graphics.Printing.PrintBordering: ...
    @winrt_mixinmethod
    def GetPagePrintTicket(self: win32more.Windows.Graphics.Printing.IPrintTaskOptions, printPageInfo: win32more.Windows.Graphics.Printing.PrintPageInfo) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def get_PageRangeOptions(self: win32more.Windows.Graphics.Printing.IPrintTaskOptions2) -> win32more.Windows.Graphics.Printing.PrintPageRangeOptions: ...
    @winrt_mixinmethod
    def get_CustomPageRanges(self: win32more.Windows.Graphics.Printing.IPrintTaskOptions2) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing.PrintPageRange]: ...
    Binding = property(get_Binding, put_Binding)
    Bordering = property(get_Bordering, put_Bordering)
    Collation = property(get_Collation, put_Collation)
    ColorMode = property(get_ColorMode, put_ColorMode)
    CustomPageRanges = property(get_CustomPageRanges, None)
    DisplayedOptions = property(get_DisplayedOptions, None)
    Duplex = property(get_Duplex, put_Duplex)
    HolePunch = property(get_HolePunch, put_HolePunch)
    MaxCopies = property(get_MaxCopies, None)
    MediaSize = property(get_MediaSize, put_MediaSize)
    MediaType = property(get_MediaType, put_MediaType)
    MinCopies = property(get_MinCopies, None)
    NumberOfCopies = property(get_NumberOfCopies, put_NumberOfCopies)
    Orientation = property(get_Orientation, put_Orientation)
    PageRangeOptions = property(get_PageRangeOptions, None)
    PrintQuality = property(get_PrintQuality, put_PrintQuality)
    Staple = property(get_Staple, put_Staple)
class PrintTaskProgressingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.IPrintTaskProgressingEventArgs
    _classid_ = 'Windows.Graphics.Printing.PrintTaskProgressingEventArgs'
    @winrt_mixinmethod
    def get_DocumentPageCount(self: win32more.Windows.Graphics.Printing.IPrintTaskProgressingEventArgs) -> UInt32: ...
    DocumentPageCount = property(get_DocumentPageCount, None)
class PrintTaskRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.IPrintTaskRequest
    _classid_ = 'Windows.Graphics.Printing.PrintTaskRequest'
    @winrt_mixinmethod
    def get_Deadline(self: win32more.Windows.Graphics.Printing.IPrintTaskRequest) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def CreatePrintTask(self: win32more.Windows.Graphics.Printing.IPrintTaskRequest, title: WinRT_String, handler: win32more.Windows.Graphics.Printing.PrintTaskSourceRequestedHandler) -> win32more.Windows.Graphics.Printing.PrintTask: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Graphics.Printing.IPrintTaskRequest) -> win32more.Windows.Graphics.Printing.PrintTaskRequestedDeferral: ...
    Deadline = property(get_Deadline, None)
class PrintTaskRequestedDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.IPrintTaskRequestedDeferral
    _classid_ = 'Windows.Graphics.Printing.PrintTaskRequestedDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.Graphics.Printing.IPrintTaskRequestedDeferral) -> Void: ...
class PrintTaskRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.IPrintTaskRequestedEventArgs
    _classid_ = 'Windows.Graphics.Printing.PrintTaskRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.Graphics.Printing.IPrintTaskRequestedEventArgs) -> win32more.Windows.Graphics.Printing.PrintTaskRequest: ...
    Request = property(get_Request, None)
class PrintTaskSourceRequestedArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.IPrintTaskSourceRequestedArgs
    _classid_ = 'Windows.Graphics.Printing.PrintTaskSourceRequestedArgs'
    @winrt_mixinmethod
    def get_Deadline(self: win32more.Windows.Graphics.Printing.IPrintTaskSourceRequestedArgs) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def SetSource(self: win32more.Windows.Graphics.Printing.IPrintTaskSourceRequestedArgs, source: win32more.Windows.Graphics.Printing.IPrintDocumentSource) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Graphics.Printing.IPrintTaskSourceRequestedArgs) -> win32more.Windows.Graphics.Printing.PrintTaskSourceRequestedDeferral: ...
    Deadline = property(get_Deadline, None)
class PrintTaskSourceRequestedDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.IPrintTaskSourceRequestedDeferral
    _classid_ = 'Windows.Graphics.Printing.PrintTaskSourceRequestedDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.Graphics.Printing.IPrintTaskSourceRequestedDeferral) -> Void: ...
class PrintTaskSourceRequestedHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6c109fa8-5cb6-4b3a-8663-f39cb02dc9b4}')
    @winrt_commethod(3)
    def Invoke(self, args: win32more.Windows.Graphics.Printing.PrintTaskSourceRequestedArgs) -> Void: ...
class _StandardPrintTaskOptions_Meta_(ComPtr.__class__):
    pass
class StandardPrintTaskOptions(ComPtr, metaclass=_StandardPrintTaskOptions_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.StandardPrintTaskOptions'
    @winrt_classmethod
    def get_CustomPageRanges(cls: win32more.Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic3) -> WinRT_String: ...
    @winrt_classmethod
    def get_Bordering(cls: win32more.Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic2) -> WinRT_String: ...
    @winrt_classmethod
    def get_MediaSize(cls: win32more.Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic) -> WinRT_String: ...
    @winrt_classmethod
    def get_MediaType(cls: win32more.Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic) -> WinRT_String: ...
    @winrt_classmethod
    def get_Orientation(cls: win32more.Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic) -> WinRT_String: ...
    @winrt_classmethod
    def get_PrintQuality(cls: win32more.Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic) -> WinRT_String: ...
    @winrt_classmethod
    def get_ColorMode(cls: win32more.Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic) -> WinRT_String: ...
    @winrt_classmethod
    def get_Duplex(cls: win32more.Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic) -> WinRT_String: ...
    @winrt_classmethod
    def get_Collation(cls: win32more.Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic) -> WinRT_String: ...
    @winrt_classmethod
    def get_Staple(cls: win32more.Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic) -> WinRT_String: ...
    @winrt_classmethod
    def get_HolePunch(cls: win32more.Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic) -> WinRT_String: ...
    @winrt_classmethod
    def get_Binding(cls: win32more.Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic) -> WinRT_String: ...
    @winrt_classmethod
    def get_Copies(cls: win32more.Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic) -> WinRT_String: ...
    @winrt_classmethod
    def get_NUp(cls: win32more.Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic) -> WinRT_String: ...
    @winrt_classmethod
    def get_InputBin(cls: win32more.Windows.Graphics.Printing.IStandardPrintTaskOptionsStatic) -> WinRT_String: ...
    _StandardPrintTaskOptions_Meta_.Binding = property(get_Binding, None)
    _StandardPrintTaskOptions_Meta_.Bordering = property(get_Bordering, None)
    _StandardPrintTaskOptions_Meta_.Collation = property(get_Collation, None)
    _StandardPrintTaskOptions_Meta_.ColorMode = property(get_ColorMode, None)
    _StandardPrintTaskOptions_Meta_.Copies = property(get_Copies, None)
    _StandardPrintTaskOptions_Meta_.CustomPageRanges = property(get_CustomPageRanges, None)
    _StandardPrintTaskOptions_Meta_.Duplex = property(get_Duplex, None)
    _StandardPrintTaskOptions_Meta_.HolePunch = property(get_HolePunch, None)
    _StandardPrintTaskOptions_Meta_.InputBin = property(get_InputBin, None)
    _StandardPrintTaskOptions_Meta_.MediaSize = property(get_MediaSize, None)
    _StandardPrintTaskOptions_Meta_.MediaType = property(get_MediaType, None)
    _StandardPrintTaskOptions_Meta_.NUp = property(get_NUp, None)
    _StandardPrintTaskOptions_Meta_.Orientation = property(get_Orientation, None)
    _StandardPrintTaskOptions_Meta_.PrintQuality = property(get_PrintQuality, None)
    _StandardPrintTaskOptions_Meta_.Staple = property(get_Staple, None)


make_ready(__name__)
