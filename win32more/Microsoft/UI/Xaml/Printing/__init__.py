from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Microsoft.UI.Xaml
import win32more.Microsoft.UI.Xaml.Printing
import win32more.Windows.Foundation
import win32more.Windows.Graphics.Printing
class AddPagesEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Printing.IAddPagesEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Printing.AddPagesEventArgs'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Printing.AddPagesEventArgs: ...
    @winrt_mixinmethod
    def get_PrintTaskOptions(self: win32more.Microsoft.UI.Xaml.Printing.IAddPagesEventArgs) -> win32more.Windows.Graphics.Printing.PrintTaskOptions: ...
    PrintTaskOptions = property(get_PrintTaskOptions, None)
class AddPagesEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ed77566a-bd03-5118-b7c3-d9cea64307dd}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Printing.AddPagesEventArgs) -> Void: ...
class GetPreviewPageEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Printing.IGetPreviewPageEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Printing.GetPreviewPageEventArgs'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Printing.GetPreviewPageEventArgs: ...
    @winrt_mixinmethod
    def get_PageNumber(self: win32more.Microsoft.UI.Xaml.Printing.IGetPreviewPageEventArgs) -> Int32: ...
    PageNumber = property(get_PageNumber, None)
class GetPreviewPageEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1c801689-a018-5574-9109-bcef62176da2}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Printing.GetPreviewPageEventArgs) -> Void: ...
class IAddPagesEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Printing.IAddPagesEventArgs'
    _iid_ = Guid('{a69f3cb3-6b74-5ee8-b034-188098a98c5d}')
    @winrt_commethod(6)
    def get_PrintTaskOptions(self) -> win32more.Windows.Graphics.Printing.PrintTaskOptions: ...
    PrintTaskOptions = property(get_PrintTaskOptions, None)
class IGetPreviewPageEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Printing.IGetPreviewPageEventArgs'
    _iid_ = Guid('{a68fbe17-f577-597f-b3ab-b379447149e6}')
    @winrt_commethod(6)
    def get_PageNumber(self) -> Int32: ...
    PageNumber = property(get_PageNumber, None)
class IPaginateEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Printing.IPaginateEventArgs'
    _iid_ = Guid('{6499c196-11a9-5ef8-91cb-52fb963bf172}')
    @winrt_commethod(6)
    def get_PrintTaskOptions(self) -> win32more.Windows.Graphics.Printing.PrintTaskOptions: ...
    @winrt_commethod(7)
    def get_CurrentPreviewPageNumber(self) -> Int32: ...
    PrintTaskOptions = property(get_PrintTaskOptions, None)
    CurrentPreviewPageNumber = property(get_CurrentPreviewPageNumber, None)
class IPrintDocument(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Printing.IPrintDocument'
    _iid_ = Guid('{1e40f1fc-5d33-5fe9-ba3e-954c0d161524}')
    @winrt_commethod(6)
    def get_DocumentSource(self) -> win32more.Windows.Graphics.Printing.IPrintDocumentSource: ...
    @winrt_commethod(7)
    def add_Paginate(self, handler: win32more.Microsoft.UI.Xaml.Printing.PaginateEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Paginate(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_GetPreviewPage(self, handler: win32more.Microsoft.UI.Xaml.Printing.GetPreviewPageEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_GetPreviewPage(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_AddPages(self, handler: win32more.Microsoft.UI.Xaml.Printing.AddPagesEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_AddPages(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def AddPage(self, pageVisual: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(14)
    def AddPagesComplete(self) -> Void: ...
    @winrt_commethod(15)
    def SetPreviewPageCount(self, count: Int32, type: win32more.Microsoft.UI.Xaml.Printing.PreviewPageCountType) -> Void: ...
    @winrt_commethod(16)
    def SetPreviewPage(self, pageNumber: Int32, pageVisual: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(17)
    def InvalidatePreview(self) -> Void: ...
    DocumentSource = property(get_DocumentSource, None)
class IPrintDocumentFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Printing.IPrintDocumentFactory'
    _iid_ = Guid('{c4c1bc12-84d1-539c-b416-d7e54c45ab58}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Printing.PrintDocument: ...
class IPrintDocumentStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Printing.IPrintDocumentStatics'
    _iid_ = Guid('{8975e4bc-8fc8-5e8f-a55a-bf71b9a827b7}')
    @winrt_commethod(6)
    def get_DocumentSourceProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    DocumentSourceProperty = property(get_DocumentSourceProperty, None)
class PaginateEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Printing.IPaginateEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Printing.PaginateEventArgs'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Printing.PaginateEventArgs: ...
    @winrt_mixinmethod
    def get_PrintTaskOptions(self: win32more.Microsoft.UI.Xaml.Printing.IPaginateEventArgs) -> win32more.Windows.Graphics.Printing.PrintTaskOptions: ...
    @winrt_mixinmethod
    def get_CurrentPreviewPageNumber(self: win32more.Microsoft.UI.Xaml.Printing.IPaginateEventArgs) -> Int32: ...
    PrintTaskOptions = property(get_PrintTaskOptions, None)
    CurrentPreviewPageNumber = property(get_CurrentPreviewPageNumber, None)
class PaginateEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c291876c-343a-5b9b-a36c-8415ba4cd9dd}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Printing.PaginateEventArgs) -> Void: ...
PreviewPageCountType = Int32
PreviewPageCountType_Final: PreviewPageCountType = 0
PreviewPageCountType_Intermediate: PreviewPageCountType = 1
class _PrintDocument_Meta_(ComPtr.__class__):
    pass
class PrintDocument(ComPtr, metaclass=_PrintDocument_Meta_):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Printing.IPrintDocument
    _classid_ = 'Microsoft.UI.Xaml.Printing.PrintDocument'
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Printing.IPrintDocumentFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Printing.PrintDocument: ...
    @winrt_mixinmethod
    def get_DocumentSource(self: win32more.Microsoft.UI.Xaml.Printing.IPrintDocument) -> win32more.Windows.Graphics.Printing.IPrintDocumentSource: ...
    @winrt_mixinmethod
    def add_Paginate(self: win32more.Microsoft.UI.Xaml.Printing.IPrintDocument, handler: win32more.Microsoft.UI.Xaml.Printing.PaginateEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Paginate(self: win32more.Microsoft.UI.Xaml.Printing.IPrintDocument, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_GetPreviewPage(self: win32more.Microsoft.UI.Xaml.Printing.IPrintDocument, handler: win32more.Microsoft.UI.Xaml.Printing.GetPreviewPageEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GetPreviewPage(self: win32more.Microsoft.UI.Xaml.Printing.IPrintDocument, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AddPages(self: win32more.Microsoft.UI.Xaml.Printing.IPrintDocument, handler: win32more.Microsoft.UI.Xaml.Printing.AddPagesEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AddPages(self: win32more.Microsoft.UI.Xaml.Printing.IPrintDocument, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def AddPage(self: win32more.Microsoft.UI.Xaml.Printing.IPrintDocument, pageVisual: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def AddPagesComplete(self: win32more.Microsoft.UI.Xaml.Printing.IPrintDocument) -> Void: ...
    @winrt_mixinmethod
    def SetPreviewPageCount(self: win32more.Microsoft.UI.Xaml.Printing.IPrintDocument, count: Int32, type: win32more.Microsoft.UI.Xaml.Printing.PreviewPageCountType) -> Void: ...
    @winrt_mixinmethod
    def SetPreviewPage(self: win32more.Microsoft.UI.Xaml.Printing.IPrintDocument, pageNumber: Int32, pageVisual: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def InvalidatePreview(self: win32more.Microsoft.UI.Xaml.Printing.IPrintDocument) -> Void: ...
    @winrt_classmethod
    def get_DocumentSourceProperty(cls: win32more.Microsoft.UI.Xaml.Printing.IPrintDocumentStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    DocumentSource = property(get_DocumentSource, None)
    _PrintDocument_Meta_.DocumentSourceProperty = property(get_DocumentSourceProperty.__wrapped__, None)
make_ready(__name__)
