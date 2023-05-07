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
import Windows.Foundation
import Windows.Graphics.Printing
import Windows.UI.Xaml
import Windows.UI.Xaml.Printing
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AddPagesEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Printing.IAddPagesEventArgs
    _classid_ = 'Windows.UI.Xaml.Printing.AddPagesEventArgs'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Printing.AddPagesEventArgs: ...
    @winrt_mixinmethod
    def get_PrintTaskOptions(self: Windows.UI.Xaml.Printing.IAddPagesEventArgs) -> Windows.Graphics.Printing.PrintTaskOptions: ...
    PrintTaskOptions = property(get_PrintTaskOptions, None)
class AddPagesEventHandler(ComPtr):
    # System.MulticastDelegate
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Xaml.Printing.AddPagesEventHandler'
    _iid_ = Guid('{d4b57970-57a0-4209-847c-c093b54bc729}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Printing.AddPagesEventArgs) -> Void: ...
class GetPreviewPageEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Printing.IGetPreviewPageEventArgs
    _classid_ = 'Windows.UI.Xaml.Printing.GetPreviewPageEventArgs'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Printing.GetPreviewPageEventArgs: ...
    @winrt_mixinmethod
    def get_PageNumber(self: Windows.UI.Xaml.Printing.IGetPreviewPageEventArgs) -> Int32: ...
    PageNumber = property(get_PageNumber, None)
class GetPreviewPageEventHandler(ComPtr):
    # System.MulticastDelegate
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Xaml.Printing.GetPreviewPageEventHandler'
    _iid_ = Guid('{ccb3e9ed-9c11-4e50-ab49-e98086bbfdef}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Printing.GetPreviewPageEventArgs) -> Void: ...
class IAddPagesEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Printing.IAddPagesEventArgs'
    _iid_ = Guid('{e2e52be5-056c-4420-9795-cb3526ce0c20}')
    @winrt_commethod(6)
    def get_PrintTaskOptions(self: Windows.UI.Xaml.Printing.IAddPagesEventArgs) -> Windows.Graphics.Printing.PrintTaskOptions: ...
    PrintTaskOptions = property(get_PrintTaskOptions, None)
class IGetPreviewPageEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Printing.IGetPreviewPageEventArgs'
    _iid_ = Guid('{a43d703d-dea9-4df6-a7ed-35049cd485c7}')
    @winrt_commethod(6)
    def get_PageNumber(self: Windows.UI.Xaml.Printing.IGetPreviewPageEventArgs) -> Int32: ...
    PageNumber = property(get_PageNumber, None)
class IPaginateEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Printing.IPaginateEventArgs'
    _iid_ = Guid('{ed945fd6-79ab-42b7-930a-3d6e09011d21}')
    @winrt_commethod(6)
    def get_PrintTaskOptions(self: Windows.UI.Xaml.Printing.IPaginateEventArgs) -> Windows.Graphics.Printing.PrintTaskOptions: ...
    @winrt_commethod(7)
    def get_CurrentPreviewPageNumber(self: Windows.UI.Xaml.Printing.IPaginateEventArgs) -> Int32: ...
    PrintTaskOptions = property(get_PrintTaskOptions, None)
    CurrentPreviewPageNumber = property(get_CurrentPreviewPageNumber, None)
class IPrintDocument(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Printing.IPrintDocument'
    _iid_ = Guid('{e44327c3-a999-485b-b1d8-72dc517821e6}')
    @winrt_commethod(6)
    def get_DocumentSource(self: Windows.UI.Xaml.Printing.IPrintDocument) -> Windows.Graphics.Printing.IPrintDocumentSource: ...
    @winrt_commethod(7)
    def add_Paginate(self: Windows.UI.Xaml.Printing.IPrintDocument, handler: Windows.UI.Xaml.Printing.PaginateEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Paginate(self: Windows.UI.Xaml.Printing.IPrintDocument, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_GetPreviewPage(self: Windows.UI.Xaml.Printing.IPrintDocument, handler: Windows.UI.Xaml.Printing.GetPreviewPageEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_GetPreviewPage(self: Windows.UI.Xaml.Printing.IPrintDocument, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_AddPages(self: Windows.UI.Xaml.Printing.IPrintDocument, handler: Windows.UI.Xaml.Printing.AddPagesEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_AddPages(self: Windows.UI.Xaml.Printing.IPrintDocument, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def AddPage(self: Windows.UI.Xaml.Printing.IPrintDocument, pageVisual: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(14)
    def AddPagesComplete(self: Windows.UI.Xaml.Printing.IPrintDocument) -> Void: ...
    @winrt_commethod(15)
    def SetPreviewPageCount(self: Windows.UI.Xaml.Printing.IPrintDocument, count: Int32, type: Windows.UI.Xaml.Printing.PreviewPageCountType) -> Void: ...
    @winrt_commethod(16)
    def SetPreviewPage(self: Windows.UI.Xaml.Printing.IPrintDocument, pageNumber: Int32, pageVisual: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(17)
    def InvalidatePreview(self: Windows.UI.Xaml.Printing.IPrintDocument) -> Void: ...
    DocumentSource = property(get_DocumentSource, None)
class IPrintDocumentFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Printing.IPrintDocumentFactory'
    _iid_ = Guid('{fb87b18f-2606-4a2f-99d4-a7cdbc35d7c7}')
    @winrt_commethod(6)
    def CreateInstance(self: Windows.UI.Xaml.Printing.IPrintDocumentFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Printing.PrintDocument: ...
class IPrintDocumentStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Printing.IPrintDocumentStatics'
    _iid_ = Guid('{fd970a3c-b152-49e0-a6bd-6aa6477e43c7}')
    @winrt_commethod(6)
    def get_DocumentSourceProperty(self: Windows.UI.Xaml.Printing.IPrintDocumentStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    DocumentSourceProperty = property(get_DocumentSourceProperty, None)
class PaginateEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Printing.IPaginateEventArgs
    _classid_ = 'Windows.UI.Xaml.Printing.PaginateEventArgs'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Printing.PaginateEventArgs: ...
    @winrt_mixinmethod
    def get_PrintTaskOptions(self: Windows.UI.Xaml.Printing.IPaginateEventArgs) -> Windows.Graphics.Printing.PrintTaskOptions: ...
    @winrt_mixinmethod
    def get_CurrentPreviewPageNumber(self: Windows.UI.Xaml.Printing.IPaginateEventArgs) -> Int32: ...
    PrintTaskOptions = property(get_PrintTaskOptions, None)
    CurrentPreviewPageNumber = property(get_CurrentPreviewPageNumber, None)
class PaginateEventHandler(ComPtr):
    # System.MulticastDelegate
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Xaml.Printing.PaginateEventHandler'
    _iid_ = Guid('{0cc05b61-811b-4a32-9965-13eb78dbb01b}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Printing.PaginateEventArgs) -> Void: ...
PreviewPageCountType = Int32
PreviewPageCountType_Final: PreviewPageCountType = 0
PreviewPageCountType_Intermediate: PreviewPageCountType = 1
class _PrintDocument_Meta_(ComPtr.__class__):
    pass
class PrintDocument(ComPtr, metaclass=_PrintDocument_Meta_):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Printing.IPrintDocument
    _classid_ = 'Windows.UI.Xaml.Printing.PrintDocument'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.Printing.IPrintDocumentFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Printing.PrintDocument: ...
    @winrt_mixinmethod
    def get_DocumentSource(self: Windows.UI.Xaml.Printing.IPrintDocument) -> Windows.Graphics.Printing.IPrintDocumentSource: ...
    @winrt_mixinmethod
    def add_Paginate(self: Windows.UI.Xaml.Printing.IPrintDocument, handler: Windows.UI.Xaml.Printing.PaginateEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Paginate(self: Windows.UI.Xaml.Printing.IPrintDocument, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_GetPreviewPage(self: Windows.UI.Xaml.Printing.IPrintDocument, handler: Windows.UI.Xaml.Printing.GetPreviewPageEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GetPreviewPage(self: Windows.UI.Xaml.Printing.IPrintDocument, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AddPages(self: Windows.UI.Xaml.Printing.IPrintDocument, handler: Windows.UI.Xaml.Printing.AddPagesEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AddPages(self: Windows.UI.Xaml.Printing.IPrintDocument, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def AddPage(self: Windows.UI.Xaml.Printing.IPrintDocument, pageVisual: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def AddPagesComplete(self: Windows.UI.Xaml.Printing.IPrintDocument) -> Void: ...
    @winrt_mixinmethod
    def SetPreviewPageCount(self: Windows.UI.Xaml.Printing.IPrintDocument, count: Int32, type: Windows.UI.Xaml.Printing.PreviewPageCountType) -> Void: ...
    @winrt_mixinmethod
    def SetPreviewPage(self: Windows.UI.Xaml.Printing.IPrintDocument, pageNumber: Int32, pageVisual: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def InvalidatePreview(self: Windows.UI.Xaml.Printing.IPrintDocument) -> Void: ...
    @winrt_classmethod
    def get_DocumentSourceProperty(cls: Windows.UI.Xaml.Printing.IPrintDocumentStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    DocumentSource = property(get_DocumentSource, None)
    _PrintDocument_Meta_.DocumentSourceProperty = property(get_DocumentSourceProperty.__wrapped__, None)
make_head(_module, 'AddPagesEventArgs')
make_head(_module, 'AddPagesEventHandler')
make_head(_module, 'GetPreviewPageEventArgs')
make_head(_module, 'GetPreviewPageEventHandler')
make_head(_module, 'IAddPagesEventArgs')
make_head(_module, 'IGetPreviewPageEventArgs')
make_head(_module, 'IPaginateEventArgs')
make_head(_module, 'IPrintDocument')
make_head(_module, 'IPrintDocumentFactory')
make_head(_module, 'IPrintDocumentStatics')
make_head(_module, 'PaginateEventArgs')
make_head(_module, 'PaginateEventHandler')
make_head(_module, 'PrintDocument')
