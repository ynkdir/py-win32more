from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.Graphics.Canvas
import win32more.Microsoft.Graphics.Canvas.Printing
import win32more.Windows.Foundation
import win32more.Windows.Graphics.Printing
import win32more.Windows.Win32.System.WinRT
class CanvasPreviewEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPreviewEventArgs
    _classid_ = 'Microsoft.Graphics.Canvas.Printing.CanvasPreviewEventArgs'
    @winrt_mixinmethod
    def get_PageNumber(self: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPreviewEventArgs) -> UInt32: ...
    @winrt_mixinmethod
    def get_PrintTaskOptions(self: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPreviewEventArgs) -> win32more.Windows.Graphics.Printing.PrintTaskOptions: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPreviewEventArgs) -> win32more.Microsoft.Graphics.Canvas.Printing.CanvasPrintDeferral: ...
    @winrt_mixinmethod
    def get_DrawingSession(self: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPreviewEventArgs) -> win32more.Microsoft.Graphics.Canvas.CanvasDrawingSession: ...
    DrawingSession = property(get_DrawingSession, None)
    PageNumber = property(get_PageNumber, None)
    PrintTaskOptions = property(get_PrintTaskOptions, None)
class CanvasPrintDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPrintDeferral
    _classid_ = 'Microsoft.Graphics.Canvas.Printing.CanvasPrintDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPrintDeferral) -> Void: ...
class CanvasPrintDocument(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPrintDocument
    _classid_ = 'Microsoft.Graphics.Canvas.Printing.CanvasPrintDocument'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.Graphics.Canvas.Printing.CanvasPrintDocument.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.Graphics.Canvas.Printing.CanvasPrintDocument.CreateWithDevice(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.Graphics.Canvas.Printing.CanvasPrintDocument: ...
    @winrt_factorymethod
    def CreateWithDevice(cls: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPrintDocumentFactory, device: win32more.Microsoft.Graphics.Canvas.CanvasDevice) -> win32more.Microsoft.Graphics.Canvas.Printing.CanvasPrintDocument: ...
    @winrt_mixinmethod
    def add_PrintTaskOptionsChanged(self: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPrintDocument, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Graphics.Canvas.Printing.CanvasPrintDocument, win32more.Microsoft.Graphics.Canvas.Printing.CanvasPrintTaskOptionsChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PrintTaskOptionsChanged(self: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPrintDocument, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Preview(self: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPrintDocument, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Graphics.Canvas.Printing.CanvasPrintDocument, win32more.Microsoft.Graphics.Canvas.Printing.CanvasPreviewEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Preview(self: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPrintDocument, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Print(self: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPrintDocument, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Graphics.Canvas.Printing.CanvasPrintDocument, win32more.Microsoft.Graphics.Canvas.Printing.CanvasPrintEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Print(self: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPrintDocument, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def InvalidatePreview(self: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPrintDocument) -> Void: ...
    @winrt_mixinmethod
    def SetPageCount(self: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPrintDocument, count: UInt32) -> Void: ...
    @winrt_mixinmethod
    def SetIntermediatePageCount(self: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPrintDocument, count: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def get_Device(self: win32more.Microsoft.Graphics.Canvas.ICanvasResourceCreator) -> win32more.Microsoft.Graphics.Canvas.CanvasDevice: ...
    Device = property(get_Device, None)
    PrintTaskOptionsChanged = event()
    Preview = event()
    Print = event()
class CanvasPrintEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPrintEventArgs
    _classid_ = 'Microsoft.Graphics.Canvas.Printing.CanvasPrintEventArgs'
    @winrt_mixinmethod
    def get_PrintTaskOptions(self: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPrintEventArgs) -> win32more.Windows.Graphics.Printing.PrintTaskOptions: ...
    @winrt_mixinmethod
    def get_Dpi(self: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPrintEventArgs) -> Single: ...
    @winrt_mixinmethod
    def put_Dpi(self: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPrintEventArgs, value: Single) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPrintEventArgs) -> win32more.Microsoft.Graphics.Canvas.Printing.CanvasPrintDeferral: ...
    @winrt_mixinmethod
    def CreateDrawingSession(self: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPrintEventArgs) -> win32more.Microsoft.Graphics.Canvas.CanvasDrawingSession: ...
    Dpi = property(get_Dpi, put_Dpi)
    PrintTaskOptions = property(get_PrintTaskOptions, None)
class CanvasPrintTaskOptionsChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPrintTaskOptionsChangedEventArgs
    _classid_ = 'Microsoft.Graphics.Canvas.Printing.CanvasPrintTaskOptionsChangedEventArgs'
    @winrt_mixinmethod
    def get_CurrentPreviewPageNumber(self: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPrintTaskOptionsChangedEventArgs) -> UInt32: ...
    @winrt_mixinmethod
    def put_NewPreviewPageNumber(self: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPrintTaskOptionsChangedEventArgs, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_NewPreviewPageNumber(self: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPrintTaskOptionsChangedEventArgs) -> UInt32: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPrintTaskOptionsChangedEventArgs) -> win32more.Microsoft.Graphics.Canvas.Printing.CanvasPrintDeferral: ...
    @winrt_mixinmethod
    def get_PrintTaskOptions(self: win32more.Microsoft.Graphics.Canvas.Printing.ICanvasPrintTaskOptionsChangedEventArgs) -> win32more.Windows.Graphics.Printing.PrintTaskOptions: ...
    CurrentPreviewPageNumber = property(get_CurrentPreviewPageNumber, None)
    NewPreviewPageNumber = property(get_NewPreviewPageNumber, put_NewPreviewPageNumber)
    PrintTaskOptions = property(get_PrintTaskOptions, None)
class ICanvasPreviewEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Graphics.Canvas.Printing.ICanvasPreviewEventArgs'
    _iid_ = Guid('{0a6a80a0-b07d-4db2-bdeb-0368bb18c0f8}')
    @winrt_commethod(6)
    def get_PageNumber(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_PrintTaskOptions(self) -> win32more.Windows.Graphics.Printing.PrintTaskOptions: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Microsoft.Graphics.Canvas.Printing.CanvasPrintDeferral: ...
    @winrt_commethod(9)
    def get_DrawingSession(self) -> win32more.Microsoft.Graphics.Canvas.CanvasDrawingSession: ...
    DrawingSession = property(get_DrawingSession, None)
    PageNumber = property(get_PageNumber, None)
    PrintTaskOptions = property(get_PrintTaskOptions, None)
class ICanvasPrintDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Graphics.Canvas.Printing.ICanvasPrintDeferral'
    _iid_ = Guid('{08ca99a2-5801-4ea4-8687-896cbda69a47}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class ICanvasPrintDocument(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Microsoft.Graphics.Canvas.Printing.ICanvasPrintDocument'
    _iid_ = Guid('{0a99cdee-bf11-49d0-aa34-3ba5c32c51a5}')
    @winrt_commethod(6)
    def add_PrintTaskOptionsChanged(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Graphics.Canvas.Printing.CanvasPrintDocument, win32more.Microsoft.Graphics.Canvas.Printing.CanvasPrintTaskOptionsChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PrintTaskOptionsChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Preview(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Graphics.Canvas.Printing.CanvasPrintDocument, win32more.Microsoft.Graphics.Canvas.Printing.CanvasPreviewEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Preview(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Print(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Graphics.Canvas.Printing.CanvasPrintDocument, win32more.Microsoft.Graphics.Canvas.Printing.CanvasPrintEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Print(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def InvalidatePreview(self) -> Void: ...
    @winrt_commethod(13)
    def SetPageCount(self, count: UInt32) -> Void: ...
    @winrt_commethod(14)
    def SetIntermediatePageCount(self, count: UInt32) -> Void: ...
    PrintTaskOptionsChanged = event()
    Preview = event()
    Print = event()
class ICanvasPrintDocumentFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Graphics.Canvas.Printing.ICanvasPrintDocumentFactory'
    _iid_ = Guid('{a201af1e-ce4a-401d-a719-2bf004d5c26a}')
    @winrt_commethod(6)
    def CreateWithDevice(self, device: win32more.Microsoft.Graphics.Canvas.CanvasDevice) -> win32more.Microsoft.Graphics.Canvas.Printing.CanvasPrintDocument: ...
class ICanvasPrintEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Graphics.Canvas.Printing.ICanvasPrintEventArgs'
    _iid_ = Guid('{0c6148c4-0216-4561-a817-34c8942aac8b}')
    @winrt_commethod(6)
    def get_PrintTaskOptions(self) -> win32more.Windows.Graphics.Printing.PrintTaskOptions: ...
    @winrt_commethod(7)
    def get_Dpi(self) -> Single: ...
    @winrt_commethod(8)
    def put_Dpi(self, value: Single) -> Void: ...
    @winrt_commethod(9)
    def GetDeferral(self) -> win32more.Microsoft.Graphics.Canvas.Printing.CanvasPrintDeferral: ...
    @winrt_commethod(10)
    def CreateDrawingSession(self) -> win32more.Microsoft.Graphics.Canvas.CanvasDrawingSession: ...
    Dpi = property(get_Dpi, put_Dpi)
    PrintTaskOptions = property(get_PrintTaskOptions, None)
class ICanvasPrintTaskOptionsChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Graphics.Canvas.Printing.ICanvasPrintTaskOptionsChangedEventArgs'
    _iid_ = Guid('{f92089ba-6c99-4cac-b28a-b5dcec7a310d}')
    @winrt_commethod(6)
    def get_CurrentPreviewPageNumber(self) -> UInt32: ...
    @winrt_commethod(7)
    def put_NewPreviewPageNumber(self, value: UInt32) -> Void: ...
    @winrt_commethod(8)
    def get_NewPreviewPageNumber(self) -> UInt32: ...
    @winrt_commethod(9)
    def GetDeferral(self) -> win32more.Microsoft.Graphics.Canvas.Printing.CanvasPrintDeferral: ...
    @winrt_commethod(10)
    def get_PrintTaskOptions(self) -> win32more.Windows.Graphics.Printing.PrintTaskOptions: ...
    CurrentPreviewPageNumber = property(get_CurrentPreviewPageNumber, None)
    NewPreviewPageNumber = property(get_NewPreviewPageNumber, put_NewPreviewPageNumber)
    PrintTaskOptions = property(get_PrintTaskOptions, None)


make_ready(__name__)
