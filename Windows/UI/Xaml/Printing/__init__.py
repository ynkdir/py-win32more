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
    ClassId = 'Windows.UI.Xaml.Printing.AddPagesEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Printing.AddPagesEventArgs: ...
    @winrt_mixinmethod
    def get_PrintTaskOptions(self: Windows.UI.Xaml.Printing.IAddPagesEventArgs) -> Windows.Graphics.Printing.PrintTaskOptions: ...
    PrintTaskOptions = property(get_PrintTaskOptions, None)
class AddPagesEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d4b57970-57a0-4209-84-7c-c0-93-b5-4b-c7-29')
    ClassId = 'Windows.UI.Xaml.Printing.AddPagesEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Printing.AddPagesEventArgs) -> Void: ...
class GetPreviewPageEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Printing.GetPreviewPageEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Printing.GetPreviewPageEventArgs: ...
    @winrt_mixinmethod
    def get_PageNumber(self: Windows.UI.Xaml.Printing.IGetPreviewPageEventArgs) -> Int32: ...
    PageNumber = property(get_PageNumber, None)
class GetPreviewPageEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ccb3e9ed-9c11-4e50-ab-49-e9-80-86-bb-fd-ef')
    ClassId = 'Windows.UI.Xaml.Printing.GetPreviewPageEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Printing.GetPreviewPageEventArgs) -> Void: ...
class IAddPagesEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e2e52be5-056c-4420-97-95-cb-35-26-ce-0c-20')
    @winrt_commethod(6)
    def get_PrintTaskOptions(self) -> Windows.Graphics.Printing.PrintTaskOptions: ...
    PrintTaskOptions = property(get_PrintTaskOptions, None)
class IGetPreviewPageEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a43d703d-dea9-4df6-a7-ed-35-04-9c-d4-85-c7')
    @winrt_commethod(6)
    def get_PageNumber(self) -> Int32: ...
    PageNumber = property(get_PageNumber, None)
class IPaginateEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ed945fd6-79ab-42b7-93-0a-3d-6e-09-01-1d-21')
    @winrt_commethod(6)
    def get_PrintTaskOptions(self) -> Windows.Graphics.Printing.PrintTaskOptions: ...
    @winrt_commethod(7)
    def get_CurrentPreviewPageNumber(self) -> Int32: ...
    PrintTaskOptions = property(get_PrintTaskOptions, None)
    CurrentPreviewPageNumber = property(get_CurrentPreviewPageNumber, None)
class IPrintDocument(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e44327c3-a999-485b-b1-d8-72-dc-51-78-21-e6')
    @winrt_commethod(6)
    def get_DocumentSource(self) -> Windows.Graphics.Printing.IPrintDocumentSource: ...
    @winrt_commethod(7)
    def add_Paginate(self, handler: Windows.UI.Xaml.Printing.PaginateEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Paginate(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_GetPreviewPage(self, handler: Windows.UI.Xaml.Printing.GetPreviewPageEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_GetPreviewPage(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_AddPages(self, handler: Windows.UI.Xaml.Printing.AddPagesEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_AddPages(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def AddPage(self, pageVisual: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(14)
    def AddPagesComplete(self) -> Void: ...
    @winrt_commethod(15)
    def SetPreviewPageCount(self, count: Int32, type: Windows.UI.Xaml.Printing.PreviewPageCountType) -> Void: ...
    @winrt_commethod(16)
    def SetPreviewPage(self, pageNumber: Int32, pageVisual: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(17)
    def InvalidatePreview(self) -> Void: ...
    DocumentSource = property(get_DocumentSource, None)
class IPrintDocumentFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fb87b18f-2606-4a2f-99-d4-a7-cd-bc-35-d7-c7')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Printing.PrintDocument: ...
class IPrintDocumentStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fd970a3c-b152-49e0-a6-bd-6a-a6-47-7e-43-c7')
    @winrt_commethod(6)
    def get_DocumentSourceProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    DocumentSourceProperty = property(get_DocumentSourceProperty, None)
class PaginateEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Printing.PaginateEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Printing.PaginateEventArgs: ...
    @winrt_mixinmethod
    def get_PrintTaskOptions(self: Windows.UI.Xaml.Printing.IPaginateEventArgs) -> Windows.Graphics.Printing.PrintTaskOptions: ...
    @winrt_mixinmethod
    def get_CurrentPreviewPageNumber(self: Windows.UI.Xaml.Printing.IPaginateEventArgs) -> Int32: ...
    PrintTaskOptions = property(get_PrintTaskOptions, None)
    CurrentPreviewPageNumber = property(get_CurrentPreviewPageNumber, None)
class PaginateEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0cc05b61-811b-4a32-99-65-13-eb-78-db-b0-1b')
    ClassId = 'Windows.UI.Xaml.Printing.PaginateEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Printing.PaginateEventArgs) -> Void: ...
PreviewPageCountType = Int32
PreviewPageCountType_Final: PreviewPageCountType = 0
PreviewPageCountType_Intermediate: PreviewPageCountType = 1
class PrintDocument(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    @winrt_commethod(20)
    def get_DocumentSource(self) -> Windows.Graphics.Printing.IPrintDocumentSource: ...
    @winrt_commethod(21)
    def add_Paginate(self, handler: Windows.UI.Xaml.Printing.PaginateEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_Paginate(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(23)
    def add_GetPreviewPage(self, handler: Windows.UI.Xaml.Printing.GetPreviewPageEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(24)
    def remove_GetPreviewPage(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(25)
    def add_AddPages(self, handler: Windows.UI.Xaml.Printing.AddPagesEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(26)
    def remove_AddPages(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(27)
    def AddPage(self, pageVisual: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(28)
    def AddPagesComplete(self) -> Void: ...
    @winrt_commethod(29)
    def SetPreviewPageCount(self, count: Int32, type: Windows.UI.Xaml.Printing.PreviewPageCountType) -> Void: ...
    @winrt_commethod(30)
    def SetPreviewPage(self, pageNumber: Int32, pageVisual: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(31)
    def InvalidatePreview(self) -> Void: ...
    @winrt_classmethod
    def get_DocumentSourceProperty(cls: Windows.UI.Xaml.Printing.IPrintDocumentStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    DocumentSource = property(get_DocumentSource, None)
    DocumentSourceProperty = property(get_DocumentSourceProperty, None)
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
