from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Graphics.Printing
import win32more.Windows.UI.Xaml
import win32more.Windows.UI.Xaml.Printing
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class AddPagesEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Printing.IAddPagesEventArgs
    _classid_ = 'Windows.UI.Xaml.Printing.AddPagesEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Printing.AddPagesEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Printing.AddPagesEventArgs: ...
    @winrt_mixinmethod
    def get_PrintTaskOptions(self: win32more.Windows.UI.Xaml.Printing.IAddPagesEventArgs) -> win32more.Windows.Graphics.Printing.PrintTaskOptions: ...
    PrintTaskOptions = property(get_PrintTaskOptions, None)
class AddPagesEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d4b57970-57a0-4209-847c-c093b54bc729}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Printing.AddPagesEventArgs) -> Void: ...
class GetPreviewPageEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Printing.IGetPreviewPageEventArgs
    _classid_ = 'Windows.UI.Xaml.Printing.GetPreviewPageEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Printing.GetPreviewPageEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Printing.GetPreviewPageEventArgs: ...
    @winrt_mixinmethod
    def get_PageNumber(self: win32more.Windows.UI.Xaml.Printing.IGetPreviewPageEventArgs) -> Int32: ...
    PageNumber = property(get_PageNumber, None)
class GetPreviewPageEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ccb3e9ed-9c11-4e50-ab49-e98086bbfdef}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Printing.GetPreviewPageEventArgs) -> Void: ...
class IAddPagesEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Printing.IAddPagesEventArgs'
    _iid_ = Guid('{e2e52be5-056c-4420-9795-cb3526ce0c20}')
    @winrt_commethod(6)
    def get_PrintTaskOptions(self) -> win32more.Windows.Graphics.Printing.PrintTaskOptions: ...
    PrintTaskOptions = property(get_PrintTaskOptions, None)
class IGetPreviewPageEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Printing.IGetPreviewPageEventArgs'
    _iid_ = Guid('{a43d703d-dea9-4df6-a7ed-35049cd485c7}')
    @winrt_commethod(6)
    def get_PageNumber(self) -> Int32: ...
    PageNumber = property(get_PageNumber, None)
class IPaginateEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Printing.IPaginateEventArgs'
    _iid_ = Guid('{ed945fd6-79ab-42b7-930a-3d6e09011d21}')
    @winrt_commethod(6)
    def get_PrintTaskOptions(self) -> win32more.Windows.Graphics.Printing.PrintTaskOptions: ...
    @winrt_commethod(7)
    def get_CurrentPreviewPageNumber(self) -> Int32: ...
    CurrentPreviewPageNumber = property(get_CurrentPreviewPageNumber, None)
    PrintTaskOptions = property(get_PrintTaskOptions, None)
class IPrintDocument(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Printing.IPrintDocument'
    _iid_ = Guid('{e44327c3-a999-485b-b1d8-72dc517821e6}')
    @winrt_commethod(6)
    def get_DocumentSource(self) -> win32more.Windows.Graphics.Printing.IPrintDocumentSource: ...
    @winrt_commethod(7)
    def add_Paginate(self, handler: win32more.Windows.UI.Xaml.Printing.PaginateEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Paginate(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_GetPreviewPage(self, handler: win32more.Windows.UI.Xaml.Printing.GetPreviewPageEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_GetPreviewPage(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_AddPages(self, handler: win32more.Windows.UI.Xaml.Printing.AddPagesEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_AddPages(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def AddPage(self, pageVisual: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(14)
    def AddPagesComplete(self) -> Void: ...
    @winrt_commethod(15)
    def SetPreviewPageCount(self, count: Int32, type: win32more.Windows.UI.Xaml.Printing.PreviewPageCountType) -> Void: ...
    @winrt_commethod(16)
    def SetPreviewPage(self, pageNumber: Int32, pageVisual: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(17)
    def InvalidatePreview(self) -> Void: ...
    DocumentSource = property(get_DocumentSource, None)
    Paginate = event()
    GetPreviewPage = event()
    AddPages = event()
class IPrintDocumentFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Printing.IPrintDocumentFactory'
    _iid_ = Guid('{fb87b18f-2606-4a2f-99d4-a7cdbc35d7c7}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Printing.PrintDocument: ...
class IPrintDocumentStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Printing.IPrintDocumentStatics'
    _iid_ = Guid('{fd970a3c-b152-49e0-a6bd-6aa6477e43c7}')
    @winrt_commethod(6)
    def get_DocumentSourceProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    DocumentSourceProperty = property(get_DocumentSourceProperty, None)
class PaginateEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Printing.IPaginateEventArgs
    _classid_ = 'Windows.UI.Xaml.Printing.PaginateEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Printing.PaginateEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Printing.PaginateEventArgs: ...
    @winrt_mixinmethod
    def get_PrintTaskOptions(self: win32more.Windows.UI.Xaml.Printing.IPaginateEventArgs) -> win32more.Windows.Graphics.Printing.PrintTaskOptions: ...
    @winrt_mixinmethod
    def get_CurrentPreviewPageNumber(self: win32more.Windows.UI.Xaml.Printing.IPaginateEventArgs) -> Int32: ...
    CurrentPreviewPageNumber = property(get_CurrentPreviewPageNumber, None)
    PrintTaskOptions = property(get_PrintTaskOptions, None)
class PaginateEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0cc05b61-811b-4a32-9965-13eb78dbb01b}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Printing.PaginateEventArgs) -> Void: ...
class PreviewPageCountType(Enum, Int32):
    Final = 0
    Intermediate = 1
class _PrintDocument_Meta_(ComPtr.__class__):
    pass
class PrintDocument(ComPtr, metaclass=_PrintDocument_Meta_):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Printing.IPrintDocument
    _classid_ = 'Windows.UI.Xaml.Printing.PrintDocument'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Printing.PrintDocument.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Printing.IPrintDocumentFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Printing.PrintDocument: ...
    @winrt_mixinmethod
    def get_DocumentSource(self: win32more.Windows.UI.Xaml.Printing.IPrintDocument) -> win32more.Windows.Graphics.Printing.IPrintDocumentSource: ...
    @winrt_mixinmethod
    def add_Paginate(self: win32more.Windows.UI.Xaml.Printing.IPrintDocument, handler: win32more.Windows.UI.Xaml.Printing.PaginateEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Paginate(self: win32more.Windows.UI.Xaml.Printing.IPrintDocument, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_GetPreviewPage(self: win32more.Windows.UI.Xaml.Printing.IPrintDocument, handler: win32more.Windows.UI.Xaml.Printing.GetPreviewPageEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GetPreviewPage(self: win32more.Windows.UI.Xaml.Printing.IPrintDocument, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AddPages(self: win32more.Windows.UI.Xaml.Printing.IPrintDocument, handler: win32more.Windows.UI.Xaml.Printing.AddPagesEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AddPages(self: win32more.Windows.UI.Xaml.Printing.IPrintDocument, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def AddPage(self: win32more.Windows.UI.Xaml.Printing.IPrintDocument, pageVisual: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def AddPagesComplete(self: win32more.Windows.UI.Xaml.Printing.IPrintDocument) -> Void: ...
    @winrt_mixinmethod
    def SetPreviewPageCount(self: win32more.Windows.UI.Xaml.Printing.IPrintDocument, count: Int32, type: win32more.Windows.UI.Xaml.Printing.PreviewPageCountType) -> Void: ...
    @winrt_mixinmethod
    def SetPreviewPage(self: win32more.Windows.UI.Xaml.Printing.IPrintDocument, pageNumber: Int32, pageVisual: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def InvalidatePreview(self: win32more.Windows.UI.Xaml.Printing.IPrintDocument) -> Void: ...
    @winrt_classmethod
    def get_DocumentSourceProperty(cls: win32more.Windows.UI.Xaml.Printing.IPrintDocumentStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    DocumentSource = property(get_DocumentSource, None)
    _PrintDocument_Meta_.DocumentSourceProperty = property(get_DocumentSourceProperty, None)
    Paginate = event()
    GetPreviewPage = event()
    AddPages = event()


make_ready(__name__)
