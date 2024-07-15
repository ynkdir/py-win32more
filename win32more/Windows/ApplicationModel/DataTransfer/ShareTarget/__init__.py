from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Contacts
import win32more.Windows.ApplicationModel.DataTransfer
import win32more.Windows.ApplicationModel.DataTransfer.ShareTarget
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
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
    Id = property(get_Id, put_Id)
    SupportedDataFormats = property(get_SupportedDataFormats, None)
    SupportedFileTypes = property(get_SupportedFileTypes, None)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
    Title = property(get_Title, put_Title)
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
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.QuickLink.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
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
    Id = property(get_Id, put_Id)
    SupportedDataFormats = property(get_SupportedDataFormats, None)
    SupportedFileTypes = property(get_SupportedFileTypes, None)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
    Title = property(get_Title, put_Title)
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
    Contacts = property(get_Contacts, None)
    Data = property(get_Data, None)
    QuickLinkId = property(get_QuickLinkId, None)


make_ready(__name__)
