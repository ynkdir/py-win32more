from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.ApplicationModel.Contacts
import win32more.Windows.ApplicationModel.DataTransfer
import win32more.Windows.ApplicationModel.DataTransfer.ShareTarget
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage.Streams
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink'
    _iid_ = Guid('{603e4308-f0be-4adc-acc9-8b27ab9cf556}')
    @winrt_commethod(6)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Thumbnail(self) -> win32more.Windows.Storage.Streams.RandomAccessStreamReference: ...
    @winrt_commethod(9)
    def put_Thumbnail(self, value: win32more.Windows.Storage.Streams.RandomAccessStreamReference) -> Void: ...
    @winrt_commethod(10)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_Id(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_SupportedDataFormats(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(13)
    def get_SupportedFileTypes(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    Title = property(get_Title, put_Title)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
    Id = property(get_Id, put_Id)
    SupportedDataFormats = property(get_SupportedDataFormats, None)
    SupportedFileTypes = property(get_SupportedFileTypes, None)
class IShareOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation'
    _iid_ = Guid('{2246bab8-d0f8-41c1-a82a-4137db6504fb}')
    @winrt_commethod(6)
    def get_Data(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_commethod(7)
    def get_QuickLinkId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def RemoveThisQuickLink(self) -> Void: ...
    @winrt_commethod(9)
    def ReportStarted(self) -> Void: ...
    @winrt_commethod(10)
    def ReportDataRetrieved(self) -> Void: ...
    @winrt_commethod(11)
    def ReportSubmittedBackgroundTask(self) -> Void: ...
    @winrt_commethod(12)
    def ReportCompletedWithQuickLink(self, quicklink: win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.QuickLink) -> Void: ...
    @winrt_commethod(13)
    def ReportCompleted(self) -> Void: ...
    @winrt_commethod(14)
    def ReportError(self, value: WinRT_String) -> Void: ...
    Data = property(get_Data, None)
    QuickLinkId = property(get_QuickLinkId, None)
class IShareOperation2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation2'
    _iid_ = Guid('{0ffb97c1-9778-4a09-8e5b-cb5e482d0555}')
    @winrt_commethod(6)
    def DismissUI(self) -> Void: ...
class IShareOperation3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation3'
    _iid_ = Guid('{5ef6b382-b7a7-4571-a2a6-994a034988b2}')
    @winrt_commethod(6)
    def get_Contacts(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.Contact]: ...
    Contacts = property(get_Contacts, None)
class QuickLink(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ShareTarget.QuickLink'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.QuickLink: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink) -> win32more.Windows.Storage.Streams.RandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_Thumbnail(self: win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink, value: win32more.Windows.Storage.Streams.RandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Id(self: win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SupportedDataFormats(self: win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_SupportedFileTypes(self: win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.IQuickLink) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    Title = property(get_Title, put_Title)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
    Id = property(get_Id, put_Id)
    SupportedDataFormats = property(get_SupportedDataFormats, None)
    SupportedFileTypes = property(get_SupportedFileTypes, None)
class ShareOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ShareTarget.ShareOperation'
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_mixinmethod
    def get_QuickLinkId(self: win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def RemoveThisQuickLink(self: win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation) -> Void: ...
    @winrt_mixinmethod
    def ReportStarted(self: win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation) -> Void: ...
    @winrt_mixinmethod
    def ReportDataRetrieved(self: win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation) -> Void: ...
    @winrt_mixinmethod
    def ReportSubmittedBackgroundTask(self: win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation) -> Void: ...
    @winrt_mixinmethod
    def ReportCompletedWithQuickLink(self: win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation, quicklink: win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.QuickLink) -> Void: ...
    @winrt_mixinmethod
    def ReportCompleted(self: win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation) -> Void: ...
    @winrt_mixinmethod
    def ReportError(self: win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def DismissUI(self: win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation2) -> Void: ...
    @winrt_mixinmethod
    def get_Contacts(self: win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.IShareOperation3) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Contacts.Contact]: ...
    Data = property(get_Data, None)
    QuickLinkId = property(get_QuickLinkId, None)
    Contacts = property(get_Contacts, None)
make_head(_module, 'IQuickLink')
make_head(_module, 'IShareOperation')
make_head(_module, 'IShareOperation2')
make_head(_module, 'IShareOperation3')
make_head(_module, 'QuickLink')
make_head(_module, 'ShareOperation')
