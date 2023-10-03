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
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.ApplicationModel.DataTransfer
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Security.EnterpriseData
import win32more.Windows.Storage
import win32more.Windows.Storage.Streams
import win32more.Windows.UI
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class Clipboard(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.Clipboard'
    @winrt_classmethod
    def GetHistoryItemsAsync(cls: win32more.Windows.ApplicationModel.DataTransfer.IClipboardStatics2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.DataTransfer.ClipboardHistoryItemsResult]: ...
    @winrt_classmethod
    def ClearHistory(cls: win32more.Windows.ApplicationModel.DataTransfer.IClipboardStatics2) -> Boolean: ...
    @winrt_classmethod
    def DeleteItemFromHistory(cls: win32more.Windows.ApplicationModel.DataTransfer.IClipboardStatics2, item: win32more.Windows.ApplicationModel.DataTransfer.ClipboardHistoryItem) -> Boolean: ...
    @winrt_classmethod
    def SetHistoryItemAsContent(cls: win32more.Windows.ApplicationModel.DataTransfer.IClipboardStatics2, item: win32more.Windows.ApplicationModel.DataTransfer.ClipboardHistoryItem) -> win32more.Windows.ApplicationModel.DataTransfer.SetHistoryItemAsContentStatus: ...
    @winrt_classmethod
    def IsHistoryEnabled(cls: win32more.Windows.ApplicationModel.DataTransfer.IClipboardStatics2) -> Boolean: ...
    @winrt_classmethod
    def IsRoamingEnabled(cls: win32more.Windows.ApplicationModel.DataTransfer.IClipboardStatics2) -> Boolean: ...
    @winrt_classmethod
    def SetContentWithOptions(cls: win32more.Windows.ApplicationModel.DataTransfer.IClipboardStatics2, content: win32more.Windows.ApplicationModel.DataTransfer.DataPackage, options: win32more.Windows.ApplicationModel.DataTransfer.ClipboardContentOptions) -> Boolean: ...
    @winrt_classmethod
    def add_HistoryChanged(cls: win32more.Windows.ApplicationModel.DataTransfer.IClipboardStatics2, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.ApplicationModel.DataTransfer.ClipboardHistoryChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_HistoryChanged(cls: win32more.Windows.ApplicationModel.DataTransfer.IClipboardStatics2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_RoamingEnabledChanged(cls: win32more.Windows.ApplicationModel.DataTransfer.IClipboardStatics2, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_RoamingEnabledChanged(cls: win32more.Windows.ApplicationModel.DataTransfer.IClipboardStatics2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_HistoryEnabledChanged(cls: win32more.Windows.ApplicationModel.DataTransfer.IClipboardStatics2, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_HistoryEnabledChanged(cls: win32more.Windows.ApplicationModel.DataTransfer.IClipboardStatics2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetContent(cls: win32more.Windows.ApplicationModel.DataTransfer.IClipboardStatics) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_classmethod
    def SetContent(cls: win32more.Windows.ApplicationModel.DataTransfer.IClipboardStatics, content: win32more.Windows.ApplicationModel.DataTransfer.DataPackage) -> Void: ...
    @winrt_classmethod
    def Flush(cls: win32more.Windows.ApplicationModel.DataTransfer.IClipboardStatics) -> Void: ...
    @winrt_classmethod
    def Clear(cls: win32more.Windows.ApplicationModel.DataTransfer.IClipboardStatics) -> Void: ...
    @winrt_classmethod
    def add_ContentChanged(cls: win32more.Windows.ApplicationModel.DataTransfer.IClipboardStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_ContentChanged(cls: win32more.Windows.ApplicationModel.DataTransfer.IClipboardStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class ClipboardContentOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.DataTransfer.IClipboardContentOptions
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ClipboardContentOptions'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.DataTransfer.ClipboardContentOptions: ...
    @winrt_mixinmethod
    def get_IsRoamable(self: win32more.Windows.ApplicationModel.DataTransfer.IClipboardContentOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsRoamable(self: win32more.Windows.ApplicationModel.DataTransfer.IClipboardContentOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsAllowedInHistory(self: win32more.Windows.ApplicationModel.DataTransfer.IClipboardContentOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsAllowedInHistory(self: win32more.Windows.ApplicationModel.DataTransfer.IClipboardContentOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_RoamingFormats(self: win32more.Windows.ApplicationModel.DataTransfer.IClipboardContentOptions) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_HistoryFormats(self: win32more.Windows.ApplicationModel.DataTransfer.IClipboardContentOptions) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    IsRoamable = property(get_IsRoamable, put_IsRoamable)
    IsAllowedInHistory = property(get_IsAllowedInHistory, put_IsAllowedInHistory)
    RoamingFormats = property(get_RoamingFormats, None)
    HistoryFormats = property(get_HistoryFormats, None)
class ClipboardHistoryChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.DataTransfer.IClipboardHistoryChangedEventArgs
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ClipboardHistoryChangedEventArgs'
class ClipboardHistoryItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.DataTransfer.IClipboardHistoryItem
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ClipboardHistoryItem'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.DataTransfer.IClipboardHistoryItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.ApplicationModel.DataTransfer.IClipboardHistoryItem) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Content(self: win32more.Windows.ApplicationModel.DataTransfer.IClipboardHistoryItem) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    Id = property(get_Id, None)
    Timestamp = property(get_Timestamp, None)
    Content = property(get_Content, None)
class ClipboardHistoryItemsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.DataTransfer.IClipboardHistoryItemsResult
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ClipboardHistoryItemsResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.ApplicationModel.DataTransfer.IClipboardHistoryItemsResult) -> win32more.Windows.ApplicationModel.DataTransfer.ClipboardHistoryItemsResultStatus: ...
    @winrt_mixinmethod
    def get_Items(self: win32more.Windows.ApplicationModel.DataTransfer.IClipboardHistoryItemsResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.DataTransfer.ClipboardHistoryItem]: ...
    Status = property(get_Status, None)
    Items = property(get_Items, None)
ClipboardHistoryItemsResultStatus = Int32
ClipboardHistoryItemsResultStatus_Success: ClipboardHistoryItemsResultStatus = 0
ClipboardHistoryItemsResultStatus_AccessDenied: ClipboardHistoryItemsResultStatus = 1
ClipboardHistoryItemsResultStatus_ClipboardHistoryDisabled: ClipboardHistoryItemsResultStatus = 2
class DataPackage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.DataTransfer.IDataPackage
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DataPackage'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackage: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackage) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackage) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackagePropertySet: ...
    @winrt_mixinmethod
    def get_RequestedOperation(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackage) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    @winrt_mixinmethod
    def put_RequestedOperation(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackage, value: win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation) -> Void: ...
    @winrt_mixinmethod
    def add_OperationCompleted(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackage, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.DataTransfer.DataPackage, win32more.Windows.ApplicationModel.DataTransfer.OperationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OperationCompleted(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackage, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Destroyed(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackage, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.DataTransfer.DataPackage, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Destroyed(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackage, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SetData(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackage, formatId: WinRT_String, value: win32more.Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def SetDataProvider(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackage, formatId: WinRT_String, delayRenderer: win32more.Windows.ApplicationModel.DataTransfer.DataProviderHandler) -> Void: ...
    @winrt_mixinmethod
    def SetText(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def SetUri(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackage, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def SetHtmlFormat(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ResourceMap(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackage) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Storage.Streams.RandomAccessStreamReference]: ...
    @winrt_mixinmethod
    def SetRtf(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def SetBitmap(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackage, value: win32more.Windows.Storage.Streams.RandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def SetStorageItemsReadOnly(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackage, value: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.IStorageItem]) -> Void: ...
    @winrt_mixinmethod
    def SetStorageItems(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackage, value: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.IStorageItem], readOnly: Boolean) -> Void: ...
    @winrt_mixinmethod
    def SetApplicationLink(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackage2, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def SetWebLink(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackage2, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def add_ShareCompleted(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackage3, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.DataTransfer.DataPackage, win32more.Windows.ApplicationModel.DataTransfer.ShareCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ShareCompleted(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackage3, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ShareCanceled(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackage4, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.DataTransfer.DataPackage, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ShareCanceled(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackage4, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Properties = property(get_Properties, None)
    RequestedOperation = property(get_RequestedOperation, put_RequestedOperation)
    ResourceMap = property(get_ResourceMap, None)
DataPackageOperation = UInt32
DataPackageOperation_None: DataPackageOperation = 0
DataPackageOperation_Copy: DataPackageOperation = 1
DataPackageOperation_Move: DataPackageOperation = 2
DataPackageOperation_Link: DataPackageOperation = 4
class DataPackagePropertySet(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DataPackagePropertySet'
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_Thumbnail(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_FileTypes(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_ApplicationName(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ApplicationName(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ApplicationListingUri(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_ApplicationListingUri(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def Lookup(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def Insert(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String, value: win32more.Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]]: ...
    @winrt_mixinmethod
    def get_ContentSourceWebLink(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet2) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_ContentSourceWebLink(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet2, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ContentSourceApplicationLink(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet2) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_ContentSourceApplicationLink(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet2, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_PackageFamilyName(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PackageFamilyName(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Square30x30Logo(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet2) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_Square30x30Logo(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet2, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_LogoBackgroundColor(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet2) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_LogoBackgroundColor(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet2, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_EnterpriseId(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet3) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_EnterpriseId(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet3, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ContentSourceUserActivityJson(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet4) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContentSourceUserActivityJson(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet4, value: WinRT_String) -> Void: ...
    Title = property(get_Title, put_Title)
    Description = property(get_Description, put_Description)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
    FileTypes = property(get_FileTypes, None)
    ApplicationName = property(get_ApplicationName, put_ApplicationName)
    ApplicationListingUri = property(get_ApplicationListingUri, put_ApplicationListingUri)
    Size = property(get_Size, None)
    ContentSourceWebLink = property(get_ContentSourceWebLink, put_ContentSourceWebLink)
    ContentSourceApplicationLink = property(get_ContentSourceApplicationLink, put_ContentSourceApplicationLink)
    PackageFamilyName = property(get_PackageFamilyName, put_PackageFamilyName)
    Square30x30Logo = property(get_Square30x30Logo, put_Square30x30Logo)
    LogoBackgroundColor = property(get_LogoBackgroundColor, put_LogoBackgroundColor)
    EnterpriseId = property(get_EnterpriseId, put_EnterpriseId)
    ContentSourceUserActivityJson = property(get_ContentSourceUserActivityJson, put_ContentSourceUserActivityJson)
class DataPackagePropertySetView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DataPackagePropertySetView'
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView) -> win32more.Windows.Storage.Streams.RandomAccessStreamReference: ...
    @winrt_mixinmethod
    def get_FileTypes(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_ApplicationName(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ApplicationListingUri(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_PackageFamilyName(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ContentSourceWebLink(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView2) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_ContentSourceApplicationLink(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView2) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Square30x30Logo(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView2) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def get_LogoBackgroundColor(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView2) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def get_EnterpriseId(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView3) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ContentSourceUserActivityJson(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView4) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsFromRoamingClipboard(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView5) -> Boolean: ...
    @winrt_mixinmethod
    def Lookup(self: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def Split(self: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head], first: POINTER(win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]), second: POINTER(win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head])) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]]: ...
    Title = property(get_Title, None)
    Description = property(get_Description, None)
    Thumbnail = property(get_Thumbnail, None)
    FileTypes = property(get_FileTypes, None)
    ApplicationName = property(get_ApplicationName, None)
    ApplicationListingUri = property(get_ApplicationListingUri, None)
    PackageFamilyName = property(get_PackageFamilyName, None)
    ContentSourceWebLink = property(get_ContentSourceWebLink, None)
    ContentSourceApplicationLink = property(get_ContentSourceApplicationLink, None)
    Square30x30Logo = property(get_Square30x30Logo, None)
    LogoBackgroundColor = property(get_LogoBackgroundColor, None)
    EnterpriseId = property(get_EnterpriseId, None)
    ContentSourceUserActivityJson = property(get_ContentSourceUserActivityJson, None)
    IsFromRoamingClipboard = property(get_IsFromRoamingClipboard, None)
    Size = property(get_Size, None)
class DataPackageView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.DataTransfer.IDataPackageView
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DataPackageView'
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackageView) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackagePropertySetView: ...
    @winrt_mixinmethod
    def get_RequestedOperation(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackageView) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    @winrt_mixinmethod
    def ReportOperationCompleted(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackageView, value: win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation) -> Void: ...
    @winrt_mixinmethod
    def get_AvailableFormats(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackageView) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def Contains(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackageView, formatId: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetDataAsync(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackageView, formatId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def GetTextAsync(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackageView) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def GetCustomTextAsync(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackageView, formatId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def GetUriAsync(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackageView) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Uri]: ...
    @winrt_mixinmethod
    def GetHtmlFormatAsync(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackageView) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def GetResourceMapAsync(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackageView) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Storage.Streams.RandomAccessStreamReference]]: ...
    @winrt_mixinmethod
    def GetRtfAsync(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackageView) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def GetBitmapAsync(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackageView) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.RandomAccessStreamReference]: ...
    @winrt_mixinmethod
    def GetStorageItemsAsync(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackageView) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.IStorageItem]]: ...
    @winrt_mixinmethod
    def GetApplicationLinkAsync(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackageView2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Uri]: ...
    @winrt_mixinmethod
    def GetWebLinkAsync(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackageView2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Uri]: ...
    @winrt_mixinmethod
    def RequestAccessAsync(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackageView3) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_mixinmethod
    def RequestAccessWithEnterpriseIdAsync(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackageView3, enterpriseId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_mixinmethod
    def UnlockAndAssumeEnterpriseIdentity(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackageView3) -> win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult: ...
    @winrt_mixinmethod
    def SetAcceptedFormatId(self: win32more.Windows.ApplicationModel.DataTransfer.IDataPackageView4, formatId: WinRT_String) -> Void: ...
    Properties = property(get_Properties, None)
    RequestedOperation = property(get_RequestedOperation, None)
    AvailableFormats = property(get_AvailableFormats, None)
class DataProviderDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.DataTransfer.IDataProviderDeferral
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DataProviderDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.ApplicationModel.DataTransfer.IDataProviderDeferral) -> Void: ...
class DataProviderHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e7ecd720-f2f4-4a2d-920e-170a2f482a27}')
    def Invoke(self, request: win32more.Windows.ApplicationModel.DataTransfer.DataProviderRequest) -> Void: ...
class DataProviderRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.DataTransfer.IDataProviderRequest
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DataProviderRequest'
    @winrt_mixinmethod
    def get_FormatId(self: win32more.Windows.ApplicationModel.DataTransfer.IDataProviderRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Deadline(self: win32more.Windows.ApplicationModel.DataTransfer.IDataProviderRequest) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.DataTransfer.IDataProviderRequest) -> win32more.Windows.ApplicationModel.DataTransfer.DataProviderDeferral: ...
    @winrt_mixinmethod
    def SetData(self: win32more.Windows.ApplicationModel.DataTransfer.IDataProviderRequest, value: win32more.Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    FormatId = property(get_FormatId, None)
    Deadline = property(get_Deadline, None)
class DataRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.DataTransfer.IDataRequest
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DataRequest'
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.ApplicationModel.DataTransfer.IDataRequest) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackage: ...
    @winrt_mixinmethod
    def put_Data(self: win32more.Windows.ApplicationModel.DataTransfer.IDataRequest, value: win32more.Windows.ApplicationModel.DataTransfer.DataPackage) -> Void: ...
    @winrt_mixinmethod
    def get_Deadline(self: win32more.Windows.ApplicationModel.DataTransfer.IDataRequest) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def FailWithDisplayText(self: win32more.Windows.ApplicationModel.DataTransfer.IDataRequest, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.DataTransfer.IDataRequest) -> win32more.Windows.ApplicationModel.DataTransfer.DataRequestDeferral: ...
    Data = property(get_Data, put_Data)
    Deadline = property(get_Deadline, None)
class DataRequestDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.DataTransfer.IDataRequestDeferral
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DataRequestDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.ApplicationModel.DataTransfer.IDataRequestDeferral) -> Void: ...
class DataRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.DataTransfer.IDataRequestedEventArgs
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DataRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.DataTransfer.IDataRequestedEventArgs) -> win32more.Windows.ApplicationModel.DataTransfer.DataRequest: ...
    Request = property(get_Request, None)
class DataTransferManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.DataTransfer.IDataTransferManager
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DataTransferManager'
    @winrt_mixinmethod
    def add_DataRequested(self: win32more.Windows.ApplicationModel.DataTransfer.IDataTransferManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.DataTransfer.DataTransferManager, win32more.Windows.ApplicationModel.DataTransfer.DataRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DataRequested(self: win32more.Windows.ApplicationModel.DataTransfer.IDataTransferManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TargetApplicationChosen(self: win32more.Windows.ApplicationModel.DataTransfer.IDataTransferManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.DataTransfer.DataTransferManager, win32more.Windows.ApplicationModel.DataTransfer.TargetApplicationChosenEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TargetApplicationChosen(self: win32more.Windows.ApplicationModel.DataTransfer.IDataTransferManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ShareProvidersRequested(self: win32more.Windows.ApplicationModel.DataTransfer.IDataTransferManager2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.DataTransfer.DataTransferManager, win32more.Windows.ApplicationModel.DataTransfer.ShareProvidersRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ShareProvidersRequested(self: win32more.Windows.ApplicationModel.DataTransfer.IDataTransferManager2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def ShowShareUIWithOptions(cls: win32more.Windows.ApplicationModel.DataTransfer.IDataTransferManagerStatics3, options: win32more.Windows.ApplicationModel.DataTransfer.ShareUIOptions) -> Void: ...
    @winrt_classmethod
    def IsSupported(cls: win32more.Windows.ApplicationModel.DataTransfer.IDataTransferManagerStatics2) -> Boolean: ...
    @winrt_classmethod
    def ShowShareUI(cls: win32more.Windows.ApplicationModel.DataTransfer.IDataTransferManagerStatics) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.ApplicationModel.DataTransfer.IDataTransferManagerStatics) -> win32more.Windows.ApplicationModel.DataTransfer.DataTransferManager: ...
class HtmlFormatHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.HtmlFormatHelper'
    @winrt_classmethod
    def GetStaticFragment(cls: win32more.Windows.ApplicationModel.DataTransfer.IHtmlFormatHelperStatics, htmlFormat: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def CreateHtmlFormat(cls: win32more.Windows.ApplicationModel.DataTransfer.IHtmlFormatHelperStatics, htmlFragment: WinRT_String) -> WinRT_String: ...
class IClipboardContentOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IClipboardContentOptions'
    _iid_ = Guid('{e888a98c-ad4b-5447-a056-ab3556276d2b}')
    @winrt_commethod(6)
    def get_IsRoamable(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsRoamable(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_IsAllowedInHistory(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsAllowedInHistory(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_RoamingFormats(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(11)
    def get_HistoryFormats(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    IsRoamable = property(get_IsRoamable, put_IsRoamable)
    IsAllowedInHistory = property(get_IsAllowedInHistory, put_IsAllowedInHistory)
    RoamingFormats = property(get_RoamingFormats, None)
    HistoryFormats = property(get_HistoryFormats, None)
class IClipboardHistoryChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IClipboardHistoryChangedEventArgs'
    _iid_ = Guid('{c0be453f-8ea2-53ce-9aba-8d2212573452}')
class IClipboardHistoryItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IClipboardHistoryItem'
    _iid_ = Guid('{0173bd8a-afff-5c50-ab92-3d19f481ec58}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def get_Content(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    Id = property(get_Id, None)
    Timestamp = property(get_Timestamp, None)
    Content = property(get_Content, None)
class IClipboardHistoryItemsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IClipboardHistoryItemsResult'
    _iid_ = Guid('{e6dfdee6-0ee2-52e3-852b-f295db65939a}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.ApplicationModel.DataTransfer.ClipboardHistoryItemsResultStatus: ...
    @winrt_commethod(7)
    def get_Items(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.DataTransfer.ClipboardHistoryItem]: ...
    Status = property(get_Status, None)
    Items = property(get_Items, None)
class IClipboardStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IClipboardStatics'
    _iid_ = Guid('{c627e291-34e2-4963-8eed-93cbb0ea3d70}')
    @winrt_commethod(6)
    def GetContent(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_commethod(7)
    def SetContent(self, content: win32more.Windows.ApplicationModel.DataTransfer.DataPackage) -> Void: ...
    @winrt_commethod(8)
    def Flush(self) -> Void: ...
    @winrt_commethod(9)
    def Clear(self) -> Void: ...
    @winrt_commethod(10)
    def add_ContentChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ContentChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IClipboardStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IClipboardStatics2'
    _iid_ = Guid('{d2ac1b6a-d29f-554b-b303-f0452345fe02}')
    @winrt_commethod(6)
    def GetHistoryItemsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.DataTransfer.ClipboardHistoryItemsResult]: ...
    @winrt_commethod(7)
    def ClearHistory(self) -> Boolean: ...
    @winrt_commethod(8)
    def DeleteItemFromHistory(self, item: win32more.Windows.ApplicationModel.DataTransfer.ClipboardHistoryItem) -> Boolean: ...
    @winrt_commethod(9)
    def SetHistoryItemAsContent(self, item: win32more.Windows.ApplicationModel.DataTransfer.ClipboardHistoryItem) -> win32more.Windows.ApplicationModel.DataTransfer.SetHistoryItemAsContentStatus: ...
    @winrt_commethod(10)
    def IsHistoryEnabled(self) -> Boolean: ...
    @winrt_commethod(11)
    def IsRoamingEnabled(self) -> Boolean: ...
    @winrt_commethod(12)
    def SetContentWithOptions(self, content: win32more.Windows.ApplicationModel.DataTransfer.DataPackage, options: win32more.Windows.ApplicationModel.DataTransfer.ClipboardContentOptions) -> Boolean: ...
    @winrt_commethod(13)
    def add_HistoryChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.ApplicationModel.DataTransfer.ClipboardHistoryChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_HistoryChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def add_RoamingEnabledChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_RoamingEnabledChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_HistoryEnabledChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_HistoryEnabledChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IDataPackage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IDataPackage'
    _iid_ = Guid('{61ebf5c7-efea-4346-9554-981d7e198ffe}')
    @winrt_commethod(6)
    def GetView(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_commethod(7)
    def get_Properties(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackagePropertySet: ...
    @winrt_commethod(8)
    def get_RequestedOperation(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    @winrt_commethod(9)
    def put_RequestedOperation(self, value: win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation) -> Void: ...
    @winrt_commethod(10)
    def add_OperationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.DataTransfer.DataPackage, win32more.Windows.ApplicationModel.DataTransfer.OperationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_OperationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_Destroyed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.DataTransfer.DataPackage, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_Destroyed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def SetData(self, formatId: WinRT_String, value: win32more.Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(15)
    def SetDataProvider(self, formatId: WinRT_String, delayRenderer: win32more.Windows.ApplicationModel.DataTransfer.DataProviderHandler) -> Void: ...
    @winrt_commethod(16)
    def SetText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(17)
    def SetUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(18)
    def SetHtmlFormat(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(19)
    def get_ResourceMap(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Storage.Streams.RandomAccessStreamReference]: ...
    @winrt_commethod(20)
    def SetRtf(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(21)
    def SetBitmap(self, value: win32more.Windows.Storage.Streams.RandomAccessStreamReference) -> Void: ...
    @winrt_commethod(22)
    def SetStorageItemsReadOnly(self, value: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.IStorageItem]) -> Void: ...
    @winrt_commethod(23)
    def SetStorageItems(self, value: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.IStorageItem], readOnly: Boolean) -> Void: ...
    Properties = property(get_Properties, None)
    RequestedOperation = property(get_RequestedOperation, put_RequestedOperation)
    ResourceMap = property(get_ResourceMap, None)
class IDataPackage2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IDataPackage2'
    _iid_ = Guid('{041c1fe9-2409-45e1-a538-4c53eeee04a7}')
    @winrt_commethod(6)
    def SetApplicationLink(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(7)
    def SetWebLink(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
class IDataPackage3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IDataPackage3'
    _iid_ = Guid('{88f31f5d-787b-4d32-965a-a9838105a056}')
    @winrt_commethod(6)
    def add_ShareCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.DataTransfer.DataPackage, win32more.Windows.ApplicationModel.DataTransfer.ShareCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ShareCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IDataPackage4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IDataPackage4'
    _iid_ = Guid('{13a24ec8-9382-536f-852a-3045e1b29a3b}')
    @winrt_commethod(6)
    def add_ShareCanceled(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.DataTransfer.DataPackage, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ShareCanceled(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IDataPackagePropertySet(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet'
    _iid_ = Guid('{cd1c93eb-4c4c-443a-a8d3-f5c241e91689}')
    @winrt_commethod(6)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Thumbnail(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(11)
    def put_Thumbnail(self, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(12)
    def get_FileTypes(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(13)
    def get_ApplicationName(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_ApplicationName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_ApplicationListingUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(16)
    def put_ApplicationListingUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    Title = property(get_Title, put_Title)
    Description = property(get_Description, put_Description)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
    FileTypes = property(get_FileTypes, None)
    ApplicationName = property(get_ApplicationName, put_ApplicationName)
    ApplicationListingUri = property(get_ApplicationListingUri, put_ApplicationListingUri)
class IDataPackagePropertySet2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet2'
    _iid_ = Guid('{eb505d4a-9800-46aa-b181-7b6f0f2b919a}')
    @winrt_commethod(6)
    def get_ContentSourceWebLink(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_ContentSourceWebLink(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def get_ContentSourceApplicationLink(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(9)
    def put_ContentSourceApplicationLink(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(10)
    def get_PackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_PackageFamilyName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_Square30x30Logo(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(13)
    def put_Square30x30Logo(self, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(14)
    def get_LogoBackgroundColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(15)
    def put_LogoBackgroundColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    ContentSourceWebLink = property(get_ContentSourceWebLink, put_ContentSourceWebLink)
    ContentSourceApplicationLink = property(get_ContentSourceApplicationLink, put_ContentSourceApplicationLink)
    PackageFamilyName = property(get_PackageFamilyName, put_PackageFamilyName)
    Square30x30Logo = property(get_Square30x30Logo, put_Square30x30Logo)
    LogoBackgroundColor = property(get_LogoBackgroundColor, put_LogoBackgroundColor)
class IDataPackagePropertySet3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet3'
    _iid_ = Guid('{9e87fd9b-5205-401b-874a-455653bd39e8}')
    @winrt_commethod(6)
    def get_EnterpriseId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_EnterpriseId(self, value: WinRT_String) -> Void: ...
    EnterpriseId = property(get_EnterpriseId, put_EnterpriseId)
class IDataPackagePropertySet4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet4'
    _iid_ = Guid('{6390ebf5-1739-4c74-b22f-865fab5e8545}')
    @winrt_commethod(6)
    def get_ContentSourceUserActivityJson(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_ContentSourceUserActivityJson(self, value: WinRT_String) -> Void: ...
    ContentSourceUserActivityJson = property(get_ContentSourceUserActivityJson, put_ContentSourceUserActivityJson)
class IDataPackagePropertySetView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView'
    _iid_ = Guid('{b94cec01-0c1a-4c57-be55-75d01289735d}')
    @winrt_commethod(6)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Thumbnail(self) -> win32more.Windows.Storage.Streams.RandomAccessStreamReference: ...
    @winrt_commethod(9)
    def get_FileTypes(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(10)
    def get_ApplicationName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_ApplicationListingUri(self) -> win32more.Windows.Foundation.Uri: ...
    Title = property(get_Title, None)
    Description = property(get_Description, None)
    Thumbnail = property(get_Thumbnail, None)
    FileTypes = property(get_FileTypes, None)
    ApplicationName = property(get_ApplicationName, None)
    ApplicationListingUri = property(get_ApplicationListingUri, None)
class IDataPackagePropertySetView2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView2'
    _iid_ = Guid('{6054509b-8ebe-4feb-9c1e-75e69de54b84}')
    @winrt_commethod(6)
    def get_PackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ContentSourceWebLink(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_ContentSourceApplicationLink(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(9)
    def get_Square30x30Logo(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(10)
    def get_LogoBackgroundColor(self) -> win32more.Windows.UI.Color: ...
    PackageFamilyName = property(get_PackageFamilyName, None)
    ContentSourceWebLink = property(get_ContentSourceWebLink, None)
    ContentSourceApplicationLink = property(get_ContentSourceApplicationLink, None)
    Square30x30Logo = property(get_Square30x30Logo, None)
    LogoBackgroundColor = property(get_LogoBackgroundColor, None)
class IDataPackagePropertySetView3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView3'
    _iid_ = Guid('{db764ce5-d174-495c-84fc-1a51f6ab45d7}')
    @winrt_commethod(6)
    def get_EnterpriseId(self) -> WinRT_String: ...
    EnterpriseId = property(get_EnterpriseId, None)
class IDataPackagePropertySetView4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView4'
    _iid_ = Guid('{4474c80d-d16f-40ae-9580-6f8562b94235}')
    @winrt_commethod(6)
    def get_ContentSourceUserActivityJson(self) -> WinRT_String: ...
    ContentSourceUserActivityJson = property(get_ContentSourceUserActivityJson, None)
class IDataPackagePropertySetView5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView5'
    _iid_ = Guid('{6f0a9445-3760-50bb-8523-c4202ded7d78}')
    @winrt_commethod(6)
    def get_IsFromRoamingClipboard(self) -> Boolean: ...
    IsFromRoamingClipboard = property(get_IsFromRoamingClipboard, None)
class IDataPackageView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IDataPackageView'
    _iid_ = Guid('{7b840471-5900-4d85-a90b-10cb85fe3552}')
    @winrt_commethod(6)
    def get_Properties(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackagePropertySetView: ...
    @winrt_commethod(7)
    def get_RequestedOperation(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    @winrt_commethod(8)
    def ReportOperationCompleted(self, value: win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation) -> Void: ...
    @winrt_commethod(9)
    def get_AvailableFormats(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(10)
    def Contains(self, formatId: WinRT_String) -> Boolean: ...
    @winrt_commethod(11)
    def GetDataAsync(self, formatId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_commethod(12)
    def GetTextAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(13)
    def GetCustomTextAsync(self, formatId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(14)
    def GetUriAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Uri]: ...
    @winrt_commethod(15)
    def GetHtmlFormatAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(16)
    def GetResourceMapAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Storage.Streams.RandomAccessStreamReference]]: ...
    @winrt_commethod(17)
    def GetRtfAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(18)
    def GetBitmapAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.RandomAccessStreamReference]: ...
    @winrt_commethod(19)
    def GetStorageItemsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.IStorageItem]]: ...
    Properties = property(get_Properties, None)
    RequestedOperation = property(get_RequestedOperation, None)
    AvailableFormats = property(get_AvailableFormats, None)
class IDataPackageView2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IDataPackageView2'
    _iid_ = Guid('{40ecba95-2450-4c1d-b6b4-ed45463dee9c}')
    @winrt_commethod(6)
    def GetApplicationLinkAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Uri]: ...
    @winrt_commethod(7)
    def GetWebLinkAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Uri]: ...
class IDataPackageView3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IDataPackageView3'
    _iid_ = Guid('{d37771a8-ddad-4288-8428-d1cae394128b}')
    @winrt_commethod(6)
    def RequestAccessAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(7)
    def RequestAccessWithEnterpriseIdAsync(self, enterpriseId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(8)
    def UnlockAndAssumeEnterpriseIdentity(self) -> win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult: ...
class IDataPackageView4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IDataPackageView4'
    _iid_ = Guid('{dfe96f1f-e042-4433-a09f-26d6ffda8b85}')
    @winrt_commethod(6)
    def SetAcceptedFormatId(self, formatId: WinRT_String) -> Void: ...
class IDataProviderDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IDataProviderDeferral'
    _iid_ = Guid('{c2cf2373-2d26-43d9-b69d-dcb86d03f6da}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IDataProviderRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IDataProviderRequest'
    _iid_ = Guid('{ebbc7157-d3c8-47da-acde-f82388d5f716}')
    @winrt_commethod(6)
    def get_FormatId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Deadline(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataProviderDeferral: ...
    @winrt_commethod(9)
    def SetData(self, value: win32more.Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    FormatId = property(get_FormatId, None)
    Deadline = property(get_Deadline, None)
class IDataRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IDataRequest'
    _iid_ = Guid('{4341ae3b-fc12-4e53-8c02-ac714c415a27}')
    @winrt_commethod(6)
    def get_Data(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackage: ...
    @winrt_commethod(7)
    def put_Data(self, value: win32more.Windows.ApplicationModel.DataTransfer.DataPackage) -> Void: ...
    @winrt_commethod(8)
    def get_Deadline(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(9)
    def FailWithDisplayText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def GetDeferral(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataRequestDeferral: ...
    Data = property(get_Data, put_Data)
    Deadline = property(get_Deadline, None)
class IDataRequestDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IDataRequestDeferral'
    _iid_ = Guid('{6dc4b89f-0386-4263-87c1-ed7dce30890e}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IDataRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IDataRequestedEventArgs'
    _iid_ = Guid('{cb8ba807-6ac5-43c9-8ac5-9ba232163182}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataRequest: ...
    Request = property(get_Request, None)
class IDataTransferManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IDataTransferManager'
    _iid_ = Guid('{a5caee9b-8708-49d1-8d36-67d25a8da00c}')
    @winrt_commethod(6)
    def add_DataRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.DataTransfer.DataTransferManager, win32more.Windows.ApplicationModel.DataTransfer.DataRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_DataRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_TargetApplicationChosen(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.DataTransfer.DataTransferManager, win32more.Windows.ApplicationModel.DataTransfer.TargetApplicationChosenEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_TargetApplicationChosen(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IDataTransferManager2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IDataTransferManager2'
    _iid_ = Guid('{30ae7d71-8ba8-4c02-8e3f-ddb23b388715}')
    @winrt_commethod(6)
    def add_ShareProvidersRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.DataTransfer.DataTransferManager, win32more.Windows.ApplicationModel.DataTransfer.ShareProvidersRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ShareProvidersRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IDataTransferManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IDataTransferManagerStatics'
    _iid_ = Guid('{a9da01aa-e00e-4cfe-aa44-2dd932dca3d8}')
    @winrt_commethod(6)
    def ShowShareUI(self) -> Void: ...
    @winrt_commethod(7)
    def GetForCurrentView(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataTransferManager: ...
class IDataTransferManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IDataTransferManagerStatics2'
    _iid_ = Guid('{c54ec2ec-9f97-4d63-9868-395e271ad8f5}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
class IDataTransferManagerStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IDataTransferManagerStatics3'
    _iid_ = Guid('{05845473-6c82-4f5c-ac23-62e458361fac}')
    @winrt_commethod(6)
    def ShowShareUIWithOptions(self, options: win32more.Windows.ApplicationModel.DataTransfer.ShareUIOptions) -> Void: ...
class IHtmlFormatHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IHtmlFormatHelperStatics'
    _iid_ = Guid('{e22e7749-dd70-446f-aefc-61cee59f655e}')
    @winrt_commethod(6)
    def GetStaticFragment(self, htmlFormat: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(7)
    def CreateHtmlFormat(self, htmlFragment: WinRT_String) -> WinRT_String: ...
class IOperationCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IOperationCompletedEventArgs'
    _iid_ = Guid('{e7af329d-051d-4fab-b1a9-47fd77f70a41}')
    @winrt_commethod(6)
    def get_Operation(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    Operation = property(get_Operation, None)
class IOperationCompletedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IOperationCompletedEventArgs2'
    _iid_ = Guid('{858fa073-1e19-4105-b2f7-c8478808d562}')
    @winrt_commethod(6)
    def get_AcceptedFormatId(self) -> WinRT_String: ...
    AcceptedFormatId = property(get_AcceptedFormatId, None)
class IShareCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IShareCompletedEventArgs'
    _iid_ = Guid('{4574c442-f913-4f60-9df7-cc4060ab1916}')
    @winrt_commethod(6)
    def get_ShareTarget(self) -> win32more.Windows.ApplicationModel.DataTransfer.ShareTargetInfo: ...
    ShareTarget = property(get_ShareTarget, None)
class IShareProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IShareProvider'
    _iid_ = Guid('{2fabe026-443e-4cda-af25-8d81070efd80}')
    @winrt_commethod(6)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayIcon(self) -> win32more.Windows.Storage.Streams.RandomAccessStreamReference: ...
    @winrt_commethod(8)
    def get_BackgroundColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(9)
    def get_Tag(self) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(10)
    def put_Tag(self, value: win32more.Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    Title = property(get_Title, None)
    DisplayIcon = property(get_DisplayIcon, None)
    BackgroundColor = property(get_BackgroundColor, None)
    Tag = property(get_Tag, put_Tag)
class IShareProviderFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IShareProviderFactory'
    _iid_ = Guid('{172a174c-e79e-4f6d-b07d-128f469e0296}')
    @winrt_commethod(6)
    def Create(self, title: WinRT_String, displayIcon: win32more.Windows.Storage.Streams.RandomAccessStreamReference, backgroundColor: win32more.Windows.UI.Color, handler: win32more.Windows.ApplicationModel.DataTransfer.ShareProviderHandler) -> win32more.Windows.ApplicationModel.DataTransfer.ShareProvider: ...
class IShareProviderOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IShareProviderOperation'
    _iid_ = Guid('{19cef937-d435-4179-b6af-14e0492b69f6}')
    @winrt_commethod(6)
    def get_Data(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_commethod(7)
    def get_Provider(self) -> win32more.Windows.ApplicationModel.DataTransfer.ShareProvider: ...
    @winrt_commethod(8)
    def ReportCompleted(self) -> Void: ...
    Data = property(get_Data, None)
    Provider = property(get_Provider, None)
class IShareProvidersRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IShareProvidersRequestedEventArgs'
    _iid_ = Guid('{f888f356-a3f8-4fce-85e4-8826e63be799}')
    @winrt_commethod(6)
    def get_Providers(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.DataTransfer.ShareProvider]: ...
    @winrt_commethod(7)
    def get_Data(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Providers = property(get_Providers, None)
    Data = property(get_Data, None)
class IShareTargetInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IShareTargetInfo'
    _iid_ = Guid('{385be607-c6e8-4114-b294-28f3bb6f9904}')
    @winrt_commethod(6)
    def get_AppUserModelId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ShareProvider(self) -> win32more.Windows.ApplicationModel.DataTransfer.ShareProvider: ...
    AppUserModelId = property(get_AppUserModelId, None)
    ShareProvider = property(get_ShareProvider, None)
class IShareUIOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IShareUIOptions'
    _iid_ = Guid('{72fa8a80-342f-4d90-9551-2ae04e37680c}')
    @winrt_commethod(6)
    def get_Theme(self) -> win32more.Windows.ApplicationModel.DataTransfer.ShareUITheme: ...
    @winrt_commethod(7)
    def put_Theme(self, value: win32more.Windows.ApplicationModel.DataTransfer.ShareUITheme) -> Void: ...
    @winrt_commethod(8)
    def get_SelectionRect(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]: ...
    @winrt_commethod(9)
    def put_SelectionRect(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]) -> Void: ...
    Theme = property(get_Theme, put_Theme)
    SelectionRect = property(get_SelectionRect, put_SelectionRect)
class ISharedStorageAccessManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ISharedStorageAccessManagerStatics'
    _iid_ = Guid('{c6132ada-34b1-4849-bd5f-d09fee3158c5}')
    @winrt_commethod(6)
    def AddFile(self, file: win32more.Windows.Storage.IStorageFile) -> WinRT_String: ...
    @winrt_commethod(7)
    def RedeemTokenForFileAsync(self, token: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_commethod(8)
    def RemoveFile(self, token: WinRT_String) -> Void: ...
class IStandardDataFormatsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IStandardDataFormatsStatics'
    _iid_ = Guid('{7ed681a1-a880-40c9-b4ed-0bee1e15f549}')
    @winrt_commethod(6)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Uri(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Html(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Rtf(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Bitmap(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_StorageItems(self) -> WinRT_String: ...
    Text = property(get_Text, None)
    Uri = property(get_Uri, None)
    Html = property(get_Html, None)
    Rtf = property(get_Rtf, None)
    Bitmap = property(get_Bitmap, None)
    StorageItems = property(get_StorageItems, None)
class IStandardDataFormatsStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IStandardDataFormatsStatics2'
    _iid_ = Guid('{42a254f4-9d76-42e8-861b-47c25dd0cf71}')
    @winrt_commethod(6)
    def get_WebLink(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ApplicationLink(self) -> WinRT_String: ...
    WebLink = property(get_WebLink, None)
    ApplicationLink = property(get_ApplicationLink, None)
class IStandardDataFormatsStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.IStandardDataFormatsStatics3'
    _iid_ = Guid('{3b57b069-01d4-474c-8b5f-bc8e27f38b21}')
    @winrt_commethod(6)
    def get_UserActivityJsonArray(self) -> WinRT_String: ...
    UserActivityJsonArray = property(get_UserActivityJsonArray, None)
class ITargetApplicationChosenEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ITargetApplicationChosenEventArgs'
    _iid_ = Guid('{ca6fb8ac-2987-4ee3-9c54-d8afbcb86c1d}')
    @winrt_commethod(6)
    def get_ApplicationName(self) -> WinRT_String: ...
    ApplicationName = property(get_ApplicationName, None)
class OperationCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.DataTransfer.IOperationCompletedEventArgs
    _classid_ = 'Windows.ApplicationModel.DataTransfer.OperationCompletedEventArgs'
    @winrt_mixinmethod
    def get_Operation(self: win32more.Windows.ApplicationModel.DataTransfer.IOperationCompletedEventArgs) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    @winrt_mixinmethod
    def get_AcceptedFormatId(self: win32more.Windows.ApplicationModel.DataTransfer.IOperationCompletedEventArgs2) -> WinRT_String: ...
    Operation = property(get_Operation, None)
    AcceptedFormatId = property(get_AcceptedFormatId, None)
SetHistoryItemAsContentStatus = Int32
SetHistoryItemAsContentStatus_Success: SetHistoryItemAsContentStatus = 0
SetHistoryItemAsContentStatus_AccessDenied: SetHistoryItemAsContentStatus = 1
SetHistoryItemAsContentStatus_ItemDeleted: SetHistoryItemAsContentStatus = 2
class ShareCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.DataTransfer.IShareCompletedEventArgs
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ShareCompletedEventArgs'
    @winrt_mixinmethod
    def get_ShareTarget(self: win32more.Windows.ApplicationModel.DataTransfer.IShareCompletedEventArgs) -> win32more.Windows.ApplicationModel.DataTransfer.ShareTargetInfo: ...
    ShareTarget = property(get_ShareTarget, None)
class ShareProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.DataTransfer.IShareProvider
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ShareProvider'
    @winrt_factorymethod
    def Create(cls: win32more.Windows.ApplicationModel.DataTransfer.IShareProviderFactory, title: WinRT_String, displayIcon: win32more.Windows.Storage.Streams.RandomAccessStreamReference, backgroundColor: win32more.Windows.UI.Color, handler: win32more.Windows.ApplicationModel.DataTransfer.ShareProviderHandler) -> win32more.Windows.ApplicationModel.DataTransfer.ShareProvider: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.ApplicationModel.DataTransfer.IShareProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayIcon(self: win32more.Windows.ApplicationModel.DataTransfer.IShareProvider) -> win32more.Windows.Storage.Streams.RandomAccessStreamReference: ...
    @winrt_mixinmethod
    def get_BackgroundColor(self: win32more.Windows.ApplicationModel.DataTransfer.IShareProvider) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def get_Tag(self: win32more.Windows.ApplicationModel.DataTransfer.IShareProvider) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def put_Tag(self: win32more.Windows.ApplicationModel.DataTransfer.IShareProvider, value: win32more.Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    Title = property(get_Title, None)
    DisplayIcon = property(get_DisplayIcon, None)
    BackgroundColor = property(get_BackgroundColor, None)
    Tag = property(get_Tag, put_Tag)
class ShareProviderHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e7f9d9ba-e1ba-4e4d-bd65-d43845d3212f}')
    def Invoke(self, operation: win32more.Windows.ApplicationModel.DataTransfer.ShareProviderOperation) -> Void: ...
class ShareProviderOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.DataTransfer.IShareProviderOperation
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ShareProviderOperation'
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.ApplicationModel.DataTransfer.IShareProviderOperation) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_mixinmethod
    def get_Provider(self: win32more.Windows.ApplicationModel.DataTransfer.IShareProviderOperation) -> win32more.Windows.ApplicationModel.DataTransfer.ShareProvider: ...
    @winrt_mixinmethod
    def ReportCompleted(self: win32more.Windows.ApplicationModel.DataTransfer.IShareProviderOperation) -> Void: ...
    Data = property(get_Data, None)
    Provider = property(get_Provider, None)
class ShareProvidersRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.DataTransfer.IShareProvidersRequestedEventArgs
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ShareProvidersRequestedEventArgs'
    @winrt_mixinmethod
    def get_Providers(self: win32more.Windows.ApplicationModel.DataTransfer.IShareProvidersRequestedEventArgs) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.DataTransfer.ShareProvider]: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.ApplicationModel.DataTransfer.IShareProvidersRequestedEventArgs) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.DataTransfer.IShareProvidersRequestedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Providers = property(get_Providers, None)
    Data = property(get_Data, None)
class ShareTargetInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.DataTransfer.IShareTargetInfo
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ShareTargetInfo'
    @winrt_mixinmethod
    def get_AppUserModelId(self: win32more.Windows.ApplicationModel.DataTransfer.IShareTargetInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ShareProvider(self: win32more.Windows.ApplicationModel.DataTransfer.IShareTargetInfo) -> win32more.Windows.ApplicationModel.DataTransfer.ShareProvider: ...
    AppUserModelId = property(get_AppUserModelId, None)
    ShareProvider = property(get_ShareProvider, None)
class ShareUIOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.DataTransfer.IShareUIOptions
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ShareUIOptions'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.DataTransfer.ShareUIOptions: ...
    @winrt_mixinmethod
    def get_Theme(self: win32more.Windows.ApplicationModel.DataTransfer.IShareUIOptions) -> win32more.Windows.ApplicationModel.DataTransfer.ShareUITheme: ...
    @winrt_mixinmethod
    def put_Theme(self: win32more.Windows.ApplicationModel.DataTransfer.IShareUIOptions, value: win32more.Windows.ApplicationModel.DataTransfer.ShareUITheme) -> Void: ...
    @winrt_mixinmethod
    def get_SelectionRect(self: win32more.Windows.ApplicationModel.DataTransfer.IShareUIOptions) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]: ...
    @winrt_mixinmethod
    def put_SelectionRect(self: win32more.Windows.ApplicationModel.DataTransfer.IShareUIOptions, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]) -> Void: ...
    Theme = property(get_Theme, put_Theme)
    SelectionRect = property(get_SelectionRect, put_SelectionRect)
ShareUITheme = Int32
ShareUITheme_Default: ShareUITheme = 0
ShareUITheme_Light: ShareUITheme = 1
ShareUITheme_Dark: ShareUITheme = 2
class SharedStorageAccessManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.SharedStorageAccessManager'
    @winrt_classmethod
    def AddFile(cls: win32more.Windows.ApplicationModel.DataTransfer.ISharedStorageAccessManagerStatics, file: win32more.Windows.Storage.IStorageFile) -> WinRT_String: ...
    @winrt_classmethod
    def RedeemTokenForFileAsync(cls: win32more.Windows.ApplicationModel.DataTransfer.ISharedStorageAccessManagerStatics, token: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    @winrt_classmethod
    def RemoveFile(cls: win32more.Windows.ApplicationModel.DataTransfer.ISharedStorageAccessManagerStatics, token: WinRT_String) -> Void: ...
class _StandardDataFormats_Meta_(ComPtr.__class__):
    pass
class StandardDataFormats(ComPtr, metaclass=_StandardDataFormats_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.StandardDataFormats'
    @winrt_classmethod
    def get_UserActivityJsonArray(cls: win32more.Windows.ApplicationModel.DataTransfer.IStandardDataFormatsStatics3) -> WinRT_String: ...
    @winrt_classmethod
    def get_WebLink(cls: win32more.Windows.ApplicationModel.DataTransfer.IStandardDataFormatsStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_ApplicationLink(cls: win32more.Windows.ApplicationModel.DataTransfer.IStandardDataFormatsStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_Text(cls: win32more.Windows.ApplicationModel.DataTransfer.IStandardDataFormatsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Uri(cls: win32more.Windows.ApplicationModel.DataTransfer.IStandardDataFormatsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Html(cls: win32more.Windows.ApplicationModel.DataTransfer.IStandardDataFormatsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Rtf(cls: win32more.Windows.ApplicationModel.DataTransfer.IStandardDataFormatsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Bitmap(cls: win32more.Windows.ApplicationModel.DataTransfer.IStandardDataFormatsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_StorageItems(cls: win32more.Windows.ApplicationModel.DataTransfer.IStandardDataFormatsStatics) -> WinRT_String: ...
    _StandardDataFormats_Meta_.UserActivityJsonArray = property(get_UserActivityJsonArray.__wrapped__, None)
    _StandardDataFormats_Meta_.WebLink = property(get_WebLink.__wrapped__, None)
    _StandardDataFormats_Meta_.ApplicationLink = property(get_ApplicationLink.__wrapped__, None)
    _StandardDataFormats_Meta_.Text = property(get_Text.__wrapped__, None)
    _StandardDataFormats_Meta_.Uri = property(get_Uri.__wrapped__, None)
    _StandardDataFormats_Meta_.Html = property(get_Html.__wrapped__, None)
    _StandardDataFormats_Meta_.Rtf = property(get_Rtf.__wrapped__, None)
    _StandardDataFormats_Meta_.Bitmap = property(get_Bitmap.__wrapped__, None)
    _StandardDataFormats_Meta_.StorageItems = property(get_StorageItems.__wrapped__, None)
class TargetApplicationChosenEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.DataTransfer.ITargetApplicationChosenEventArgs
    _classid_ = 'Windows.ApplicationModel.DataTransfer.TargetApplicationChosenEventArgs'
    @winrt_mixinmethod
    def get_ApplicationName(self: win32more.Windows.ApplicationModel.DataTransfer.ITargetApplicationChosenEventArgs) -> WinRT_String: ...
    ApplicationName = property(get_ApplicationName, None)
make_head(_module, 'Clipboard')
make_head(_module, 'ClipboardContentOptions')
make_head(_module, 'ClipboardHistoryChangedEventArgs')
make_head(_module, 'ClipboardHistoryItem')
make_head(_module, 'ClipboardHistoryItemsResult')
make_head(_module, 'DataPackage')
make_head(_module, 'DataPackagePropertySet')
make_head(_module, 'DataPackagePropertySetView')
make_head(_module, 'DataPackageView')
make_head(_module, 'DataProviderDeferral')
make_head(_module, 'DataProviderRequest')
make_head(_module, 'DataRequest')
make_head(_module, 'DataRequestDeferral')
make_head(_module, 'DataRequestedEventArgs')
make_head(_module, 'DataTransferManager')
make_head(_module, 'HtmlFormatHelper')
make_head(_module, 'IClipboardContentOptions')
make_head(_module, 'IClipboardHistoryChangedEventArgs')
make_head(_module, 'IClipboardHistoryItem')
make_head(_module, 'IClipboardHistoryItemsResult')
make_head(_module, 'IClipboardStatics')
make_head(_module, 'IClipboardStatics2')
make_head(_module, 'IDataPackage')
make_head(_module, 'IDataPackage2')
make_head(_module, 'IDataPackage3')
make_head(_module, 'IDataPackage4')
make_head(_module, 'IDataPackagePropertySet')
make_head(_module, 'IDataPackagePropertySet2')
make_head(_module, 'IDataPackagePropertySet3')
make_head(_module, 'IDataPackagePropertySet4')
make_head(_module, 'IDataPackagePropertySetView')
make_head(_module, 'IDataPackagePropertySetView2')
make_head(_module, 'IDataPackagePropertySetView3')
make_head(_module, 'IDataPackagePropertySetView4')
make_head(_module, 'IDataPackagePropertySetView5')
make_head(_module, 'IDataPackageView')
make_head(_module, 'IDataPackageView2')
make_head(_module, 'IDataPackageView3')
make_head(_module, 'IDataPackageView4')
make_head(_module, 'IDataProviderDeferral')
make_head(_module, 'IDataProviderRequest')
make_head(_module, 'IDataRequest')
make_head(_module, 'IDataRequestDeferral')
make_head(_module, 'IDataRequestedEventArgs')
make_head(_module, 'IDataTransferManager')
make_head(_module, 'IDataTransferManager2')
make_head(_module, 'IDataTransferManagerStatics')
make_head(_module, 'IDataTransferManagerStatics2')
make_head(_module, 'IDataTransferManagerStatics3')
make_head(_module, 'IHtmlFormatHelperStatics')
make_head(_module, 'IOperationCompletedEventArgs')
make_head(_module, 'IOperationCompletedEventArgs2')
make_head(_module, 'IShareCompletedEventArgs')
make_head(_module, 'IShareProvider')
make_head(_module, 'IShareProviderFactory')
make_head(_module, 'IShareProviderOperation')
make_head(_module, 'IShareProvidersRequestedEventArgs')
make_head(_module, 'IShareTargetInfo')
make_head(_module, 'IShareUIOptions')
make_head(_module, 'ISharedStorageAccessManagerStatics')
make_head(_module, 'IStandardDataFormatsStatics')
make_head(_module, 'IStandardDataFormatsStatics2')
make_head(_module, 'IStandardDataFormatsStatics3')
make_head(_module, 'ITargetApplicationChosenEventArgs')
make_head(_module, 'OperationCompletedEventArgs')
make_head(_module, 'ShareCompletedEventArgs')
make_head(_module, 'ShareProvider')
make_head(_module, 'ShareProviderOperation')
make_head(_module, 'ShareProvidersRequestedEventArgs')
make_head(_module, 'ShareTargetInfo')
make_head(_module, 'ShareUIOptions')
make_head(_module, 'SharedStorageAccessManager')
make_head(_module, 'StandardDataFormats')
make_head(_module, 'TargetApplicationChosenEventArgs')