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
import Windows.ApplicationModel.Contacts
import Windows.ApplicationModel.DataTransfer
import Windows.ApplicationModel.DataTransfer.ShareTarget
import Windows.Foundation.Collections
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
class IQuickLink(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink'
    _iid_ = Guid('{603e4308-f0be-4adc-acc9-8b27ab9cf556}')
    @winrt_commethod(6)
    def get_Title(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Title(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Thumbnail(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink) -> Windows.Storage.Streams.RandomAccessStreamReference: ...
    @winrt_commethod(9)
    def put_Thumbnail(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink, value: Windows.Storage.Streams.RandomAccessStreamReference) -> Void: ...
    @winrt_commethod(10)
    def get_Id(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_Id(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_SupportedDataFormats(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(13)
    def get_SupportedFileTypes(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    Title = property(get_Title, put_Title)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
    Id = property(get_Id, put_Id)
    SupportedDataFormats = property(get_SupportedDataFormats, None)
    SupportedFileTypes = property(get_SupportedFileTypes, None)
class IShareOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation'
    _iid_ = Guid('{2246bab8-d0f8-41c1-a82a-4137db6504fb}')
    @winrt_commethod(6)
    def get_Data(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation) -> Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_commethod(7)
    def get_QuickLinkId(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation) -> WinRT_String: ...
    @winrt_commethod(8)
    def RemoveThisQuickLink(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation) -> Void: ...
    @winrt_commethod(9)
    def ReportStarted(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation) -> Void: ...
    @winrt_commethod(10)
    def ReportDataRetrieved(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation) -> Void: ...
    @winrt_commethod(11)
    def ReportSubmittedBackgroundTask(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation) -> Void: ...
    @winrt_commethod(12)
    def ReportCompletedWithQuickLink(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation, quicklink: Windows.ApplicationModel.DataTransfer.ShareTarget.QuickLink) -> Void: ...
    @winrt_commethod(13)
    def ReportCompleted(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation) -> Void: ...
    @winrt_commethod(14)
    def ReportError(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation, value: WinRT_String) -> Void: ...
    Data = property(get_Data, None)
    QuickLinkId = property(get_QuickLinkId, None)
class IShareOperation2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation2'
    _iid_ = Guid('{0ffb97c1-9778-4a09-8e5b-cb5e482d0555}')
    @winrt_commethod(6)
    def DismissUI(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation2) -> Void: ...
class IShareOperation3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation3'
    _iid_ = Guid('{5ef6b382-b7a7-4571-a2a6-994a034988b2}')
    @winrt_commethod(6)
    def get_Contacts(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation3) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Contacts.Contact]: ...
    Contacts = property(get_Contacts, None)
class QuickLink(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ShareTarget.QuickLink'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.DataTransfer.ShareTarget.QuickLink: ...
    @winrt_mixinmethod
    def get_Title(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink) -> Windows.Storage.Streams.RandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_Thumbnail(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink, value: Windows.Storage.Streams.RandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Id(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SupportedDataFormats(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_SupportedFileTypes(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    Title = property(get_Title, put_Title)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
    Id = property(get_Id, put_Id)
    SupportedDataFormats = property(get_SupportedDataFormats, None)
    SupportedFileTypes = property(get_SupportedFileTypes, None)
class ShareOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ShareTarget.ShareOperation'
    @winrt_mixinmethod
    def get_Data(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation) -> Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_mixinmethod
    def get_QuickLinkId(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def RemoveThisQuickLink(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation) -> Void: ...
    @winrt_mixinmethod
    def ReportStarted(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation) -> Void: ...
    @winrt_mixinmethod
    def ReportDataRetrieved(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation) -> Void: ...
    @winrt_mixinmethod
    def ReportSubmittedBackgroundTask(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation) -> Void: ...
    @winrt_mixinmethod
    def ReportCompletedWithQuickLink(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation, quicklink: Windows.ApplicationModel.DataTransfer.ShareTarget.QuickLink) -> Void: ...
    @winrt_mixinmethod
    def ReportCompleted(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation) -> Void: ...
    @winrt_mixinmethod
    def ReportError(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def DismissUI(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation2) -> Void: ...
    @winrt_mixinmethod
    def get_Contacts(self: Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation3) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Contacts.Contact]: ...
    Data = property(get_Data, None)
    QuickLinkId = property(get_QuickLinkId, None)
    Contacts = property(get_Contacts, None)
make_head(_module, 'IQuickLink')
make_head(_module, 'IShareOperation')
make_head(_module, 'IShareOperation2')
make_head(_module, 'IShareOperation3')
make_head(_module, 'QuickLink')
make_head(_module, 'ShareOperation')
