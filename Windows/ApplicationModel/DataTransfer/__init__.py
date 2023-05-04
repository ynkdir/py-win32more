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
import Windows.ApplicationModel.DataTransfer
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Security.EnterpriseData
import Windows.Storage
import Windows.Storage.Streams
import Windows.UI
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
    extends: Windows.Win32.System.WinRT.IInspectable
    @winrt_classmethod
    def GetHistoryItemsAsync(cls: Windows.ApplicationModel.DataTransfer.IClipboardStatics2) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.DataTransfer.ClipboardHistoryItemsResult]: ...
    @winrt_classmethod
    def ClearHistory(cls: Windows.ApplicationModel.DataTransfer.IClipboardStatics2) -> Boolean: ...
    @winrt_classmethod
    def DeleteItemFromHistory(cls: Windows.ApplicationModel.DataTransfer.IClipboardStatics2, item: Windows.ApplicationModel.DataTransfer.ClipboardHistoryItem) -> Boolean: ...
    @winrt_classmethod
    def SetHistoryItemAsContent(cls: Windows.ApplicationModel.DataTransfer.IClipboardStatics2, item: Windows.ApplicationModel.DataTransfer.ClipboardHistoryItem) -> Windows.ApplicationModel.DataTransfer.SetHistoryItemAsContentStatus: ...
    @winrt_classmethod
    def IsHistoryEnabled(cls: Windows.ApplicationModel.DataTransfer.IClipboardStatics2) -> Boolean: ...
    @winrt_classmethod
    def IsRoamingEnabled(cls: Windows.ApplicationModel.DataTransfer.IClipboardStatics2) -> Boolean: ...
    @winrt_classmethod
    def SetContentWithOptions(cls: Windows.ApplicationModel.DataTransfer.IClipboardStatics2, content: Windows.ApplicationModel.DataTransfer.DataPackage, options: Windows.ApplicationModel.DataTransfer.ClipboardContentOptions) -> Boolean: ...
    @winrt_classmethod
    def add_HistoryChanged(cls: Windows.ApplicationModel.DataTransfer.IClipboardStatics2, handler: Windows.Foundation.EventHandler[Windows.ApplicationModel.DataTransfer.ClipboardHistoryChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_HistoryChanged(cls: Windows.ApplicationModel.DataTransfer.IClipboardStatics2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_RoamingEnabledChanged(cls: Windows.ApplicationModel.DataTransfer.IClipboardStatics2, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_RoamingEnabledChanged(cls: Windows.ApplicationModel.DataTransfer.IClipboardStatics2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_HistoryEnabledChanged(cls: Windows.ApplicationModel.DataTransfer.IClipboardStatics2, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_HistoryEnabledChanged(cls: Windows.ApplicationModel.DataTransfer.IClipboardStatics2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetContent(cls: Windows.ApplicationModel.DataTransfer.IClipboardStatics) -> Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_classmethod
    def SetContent(cls: Windows.ApplicationModel.DataTransfer.IClipboardStatics, content: Windows.ApplicationModel.DataTransfer.DataPackage) -> Void: ...
    @winrt_classmethod
    def Flush(cls: Windows.ApplicationModel.DataTransfer.IClipboardStatics) -> Void: ...
    @winrt_classmethod
    def Clear(cls: Windows.ApplicationModel.DataTransfer.IClipboardStatics) -> Void: ...
    @winrt_classmethod
    def add_ContentChanged(cls: Windows.ApplicationModel.DataTransfer.IClipboardStatics, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_ContentChanged(cls: Windows.ApplicationModel.DataTransfer.IClipboardStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ClipboardContentOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.IClipboardContentOptions
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ClipboardContentOptions'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.DataTransfer.ClipboardContentOptions: ...
    @winrt_mixinmethod
    def get_IsRoamable(self: Windows.ApplicationModel.DataTransfer.IClipboardContentOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsRoamable(self: Windows.ApplicationModel.DataTransfer.IClipboardContentOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsAllowedInHistory(self: Windows.ApplicationModel.DataTransfer.IClipboardContentOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsAllowedInHistory(self: Windows.ApplicationModel.DataTransfer.IClipboardContentOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_RoamingFormats(self: Windows.ApplicationModel.DataTransfer.IClipboardContentOptions) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_HistoryFormats(self: Windows.ApplicationModel.DataTransfer.IClipboardContentOptions) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    IsRoamable = property(get_IsRoamable, put_IsRoamable)
    IsAllowedInHistory = property(get_IsAllowedInHistory, put_IsAllowedInHistory)
    RoamingFormats = property(get_RoamingFormats, None)
    HistoryFormats = property(get_HistoryFormats, None)
class ClipboardHistoryChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.IClipboardHistoryChangedEventArgs
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ClipboardHistoryChangedEventArgs'
class ClipboardHistoryItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.IClipboardHistoryItem
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ClipboardHistoryItem'
    @winrt_mixinmethod
    def get_Id(self: Windows.ApplicationModel.DataTransfer.IClipboardHistoryItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.ApplicationModel.DataTransfer.IClipboardHistoryItem) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Content(self: Windows.ApplicationModel.DataTransfer.IClipboardHistoryItem) -> Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    Id = property(get_Id, None)
    Timestamp = property(get_Timestamp, None)
    Content = property(get_Content, None)
class ClipboardHistoryItemsResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.IClipboardHistoryItemsResult
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ClipboardHistoryItemsResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.ApplicationModel.DataTransfer.IClipboardHistoryItemsResult) -> Windows.ApplicationModel.DataTransfer.ClipboardHistoryItemsResultStatus: ...
    @winrt_mixinmethod
    def get_Items(self: Windows.ApplicationModel.DataTransfer.IClipboardHistoryItemsResult) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.DataTransfer.ClipboardHistoryItem]: ...
    Status = property(get_Status, None)
    Items = property(get_Items, None)
ClipboardHistoryItemsResultStatus = Int32
ClipboardHistoryItemsResultStatus_Success: ClipboardHistoryItemsResultStatus = 0
ClipboardHistoryItemsResultStatus_AccessDenied: ClipboardHistoryItemsResultStatus = 1
ClipboardHistoryItemsResultStatus_ClipboardHistoryDisabled: ClipboardHistoryItemsResultStatus = 2
class DataPackage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.IDataPackage
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DataPackage'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.DataTransfer.DataPackage: ...
    @winrt_mixinmethod
    def GetView(self: Windows.ApplicationModel.DataTransfer.IDataPackage) -> Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.ApplicationModel.DataTransfer.IDataPackage) -> Windows.ApplicationModel.DataTransfer.DataPackagePropertySet: ...
    @winrt_mixinmethod
    def get_RequestedOperation(self: Windows.ApplicationModel.DataTransfer.IDataPackage) -> Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    @winrt_mixinmethod
    def put_RequestedOperation(self: Windows.ApplicationModel.DataTransfer.IDataPackage, value: Windows.ApplicationModel.DataTransfer.DataPackageOperation) -> Void: ...
    @winrt_mixinmethod
    def add_OperationCompleted(self: Windows.ApplicationModel.DataTransfer.IDataPackage, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.DataTransfer.DataPackage, Windows.ApplicationModel.DataTransfer.OperationCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OperationCompleted(self: Windows.ApplicationModel.DataTransfer.IDataPackage, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Destroyed(self: Windows.ApplicationModel.DataTransfer.IDataPackage, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.DataTransfer.DataPackage, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Destroyed(self: Windows.ApplicationModel.DataTransfer.IDataPackage, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SetData(self: Windows.ApplicationModel.DataTransfer.IDataPackage, formatId: WinRT_String, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def SetDataProvider(self: Windows.ApplicationModel.DataTransfer.IDataPackage, formatId: WinRT_String, delayRenderer: Windows.ApplicationModel.DataTransfer.DataProviderHandler) -> Void: ...
    @winrt_mixinmethod
    def SetText(self: Windows.ApplicationModel.DataTransfer.IDataPackage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def SetUri(self: Windows.ApplicationModel.DataTransfer.IDataPackage, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def SetHtmlFormat(self: Windows.ApplicationModel.DataTransfer.IDataPackage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ResourceMap(self: Windows.ApplicationModel.DataTransfer.IDataPackage) -> Windows.Foundation.Collections.IMap[WinRT_String, Windows.Storage.Streams.RandomAccessStreamReference]: ...
    @winrt_mixinmethod
    def SetRtf(self: Windows.ApplicationModel.DataTransfer.IDataPackage, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def SetBitmap(self: Windows.ApplicationModel.DataTransfer.IDataPackage, value: Windows.Storage.Streams.RandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def SetStorageItemsReadOnly(self: Windows.ApplicationModel.DataTransfer.IDataPackage, value: Windows.Foundation.Collections.IIterable[Windows.Storage.IStorageItem]) -> Void: ...
    @winrt_mixinmethod
    def SetStorageItems(self: Windows.ApplicationModel.DataTransfer.IDataPackage, value: Windows.Foundation.Collections.IIterable[Windows.Storage.IStorageItem], readOnly: Boolean) -> Void: ...
    @winrt_mixinmethod
    def SetApplicationLink(self: Windows.ApplicationModel.DataTransfer.IDataPackage2, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def SetWebLink(self: Windows.ApplicationModel.DataTransfer.IDataPackage2, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def add_ShareCompleted(self: Windows.ApplicationModel.DataTransfer.IDataPackage3, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.DataTransfer.DataPackage, Windows.ApplicationModel.DataTransfer.ShareCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ShareCompleted(self: Windows.ApplicationModel.DataTransfer.IDataPackage3, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ShareCanceled(self: Windows.ApplicationModel.DataTransfer.IDataPackage4, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.DataTransfer.DataPackage, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ShareCanceled(self: Windows.ApplicationModel.DataTransfer.IDataPackage4, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Properties = property(get_Properties, None)
    RequestedOperation = property(get_RequestedOperation, put_RequestedOperation)
    ResourceMap = property(get_ResourceMap, None)
DataPackageOperation = UInt32
DataPackageOperation_None: DataPackageOperation = 0
DataPackageOperation_Copy: DataPackageOperation = 1
DataPackageOperation_Move: DataPackageOperation = 2
DataPackageOperation_Link: DataPackageOperation = 4
class DataPackagePropertySet(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DataPackagePropertySet'
    @winrt_mixinmethod
    def get_Title(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_Thumbnail(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet, value: Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_FileTypes(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_ApplicationName(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ApplicationName(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ApplicationListingUri(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_ApplicationListingUri(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def Lookup(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def Insert(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String, value: Windows.Win32.System.WinRT.IInspectable_head) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]]) -> Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]]: ...
    @winrt_mixinmethod
    def get_ContentSourceWebLink(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet2) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_ContentSourceWebLink(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet2, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ContentSourceApplicationLink(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet2) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_ContentSourceApplicationLink(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet2, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_PackageFamilyName(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PackageFamilyName(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Square30x30Logo(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet2) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_Square30x30Logo(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet2, value: Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_LogoBackgroundColor(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet2) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_LogoBackgroundColor(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet2, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_EnterpriseId(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet3) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_EnterpriseId(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet3, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ContentSourceUserActivityJson(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet4) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContentSourceUserActivityJson(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySet4, value: WinRT_String) -> Void: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DataPackagePropertySetView'
    @winrt_mixinmethod
    def get_Title(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView) -> Windows.Storage.Streams.RandomAccessStreamReference: ...
    @winrt_mixinmethod
    def get_FileTypes(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_ApplicationName(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ApplicationListingUri(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_PackageFamilyName(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ContentSourceWebLink(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView2) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_ContentSourceApplicationLink(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView2) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Square30x30Logo(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView2) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def get_LogoBackgroundColor(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView2) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def get_EnterpriseId(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView3) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ContentSourceUserActivityJson(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView4) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsFromRoamingClipboard(self: Windows.ApplicationModel.DataTransfer.IDataPackagePropertySetView5) -> Boolean: ...
    @winrt_mixinmethod
    def Lookup(self: Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def Split(self: Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], first: POINTER(Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]), second: POINTER(Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head])) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]]) -> Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]]: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.IDataPackageView
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DataPackageView'
    @winrt_mixinmethod
    def get_Properties(self: Windows.ApplicationModel.DataTransfer.IDataPackageView) -> Windows.ApplicationModel.DataTransfer.DataPackagePropertySetView: ...
    @winrt_mixinmethod
    def get_RequestedOperation(self: Windows.ApplicationModel.DataTransfer.IDataPackageView) -> Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    @winrt_mixinmethod
    def ReportOperationCompleted(self: Windows.ApplicationModel.DataTransfer.IDataPackageView, value: Windows.ApplicationModel.DataTransfer.DataPackageOperation) -> Void: ...
    @winrt_mixinmethod
    def get_AvailableFormats(self: Windows.ApplicationModel.DataTransfer.IDataPackageView) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def Contains(self: Windows.ApplicationModel.DataTransfer.IDataPackageView, formatId: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetDataAsync(self: Windows.ApplicationModel.DataTransfer.IDataPackageView, formatId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def GetTextAsync(self: Windows.ApplicationModel.DataTransfer.IDataPackageView) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def GetCustomTextAsync(self: Windows.ApplicationModel.DataTransfer.IDataPackageView, formatId: WinRT_String) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def GetUriAsync(self: Windows.ApplicationModel.DataTransfer.IDataPackageView) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Uri]: ...
    @winrt_mixinmethod
    def GetHtmlFormatAsync(self: Windows.ApplicationModel.DataTransfer.IDataPackageView) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def GetResourceMapAsync(self: Windows.ApplicationModel.DataTransfer.IDataPackageView) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Storage.Streams.RandomAccessStreamReference]]: ...
    @winrt_mixinmethod
    def GetRtfAsync(self: Windows.ApplicationModel.DataTransfer.IDataPackageView) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def GetBitmapAsync(self: Windows.ApplicationModel.DataTransfer.IDataPackageView) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.RandomAccessStreamReference]: ...
    @winrt_mixinmethod
    def GetStorageItemsAsync(self: Windows.ApplicationModel.DataTransfer.IDataPackageView) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.IStorageItem]]: ...
    @winrt_mixinmethod
    def GetApplicationLinkAsync(self: Windows.ApplicationModel.DataTransfer.IDataPackageView2) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Uri]: ...
    @winrt_mixinmethod
    def GetWebLinkAsync(self: Windows.ApplicationModel.DataTransfer.IDataPackageView2) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Uri]: ...
    @winrt_mixinmethod
    def RequestAccessAsync(self: Windows.ApplicationModel.DataTransfer.IDataPackageView3) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_mixinmethod
    def RequestAccessWithEnterpriseIdAsync(self: Windows.ApplicationModel.DataTransfer.IDataPackageView3, enterpriseId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_mixinmethod
    def UnlockAndAssumeEnterpriseIdentity(self: Windows.ApplicationModel.DataTransfer.IDataPackageView3) -> Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult: ...
    @winrt_mixinmethod
    def SetAcceptedFormatId(self: Windows.ApplicationModel.DataTransfer.IDataPackageView4, formatId: WinRT_String) -> Void: ...
    Properties = property(get_Properties, None)
    RequestedOperation = property(get_RequestedOperation, None)
    AvailableFormats = property(get_AvailableFormats, None)
class DataProviderDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.IDataProviderDeferral
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DataProviderDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.ApplicationModel.DataTransfer.IDataProviderDeferral) -> Void: ...
class DataProviderHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e7ecd720-f2f4-4a2d-920e-170a2f482a27}')
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DataProviderHandler'
    @winrt_commethod(3)
    def Invoke(self, request: Windows.ApplicationModel.DataTransfer.DataProviderRequest) -> Void: ...
class DataProviderRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.IDataProviderRequest
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DataProviderRequest'
    @winrt_mixinmethod
    def get_FormatId(self: Windows.ApplicationModel.DataTransfer.IDataProviderRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Deadline(self: Windows.ApplicationModel.DataTransfer.IDataProviderRequest) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.DataTransfer.IDataProviderRequest) -> Windows.ApplicationModel.DataTransfer.DataProviderDeferral: ...
    @winrt_mixinmethod
    def SetData(self: Windows.ApplicationModel.DataTransfer.IDataProviderRequest, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    FormatId = property(get_FormatId, None)
    Deadline = property(get_Deadline, None)
class DataRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.IDataRequest
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DataRequest'
    @winrt_mixinmethod
    def get_Data(self: Windows.ApplicationModel.DataTransfer.IDataRequest) -> Windows.ApplicationModel.DataTransfer.DataPackage: ...
    @winrt_mixinmethod
    def put_Data(self: Windows.ApplicationModel.DataTransfer.IDataRequest, value: Windows.ApplicationModel.DataTransfer.DataPackage) -> Void: ...
    @winrt_mixinmethod
    def get_Deadline(self: Windows.ApplicationModel.DataTransfer.IDataRequest) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def FailWithDisplayText(self: Windows.ApplicationModel.DataTransfer.IDataRequest, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.DataTransfer.IDataRequest) -> Windows.ApplicationModel.DataTransfer.DataRequestDeferral: ...
    Data = property(get_Data, put_Data)
    Deadline = property(get_Deadline, None)
class DataRequestDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.IDataRequestDeferral
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DataRequestDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.ApplicationModel.DataTransfer.IDataRequestDeferral) -> Void: ...
class DataRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.IDataRequestedEventArgs
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DataRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.DataTransfer.IDataRequestedEventArgs) -> Windows.ApplicationModel.DataTransfer.DataRequest: ...
    Request = property(get_Request, None)
class DataTransferManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.IDataTransferManager
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DataTransferManager'
    @winrt_mixinmethod
    def add_DataRequested(self: Windows.ApplicationModel.DataTransfer.IDataTransferManager, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.DataTransfer.DataTransferManager, Windows.ApplicationModel.DataTransfer.DataRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DataRequested(self: Windows.ApplicationModel.DataTransfer.IDataTransferManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TargetApplicationChosen(self: Windows.ApplicationModel.DataTransfer.IDataTransferManager, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.DataTransfer.DataTransferManager, Windows.ApplicationModel.DataTransfer.TargetApplicationChosenEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TargetApplicationChosen(self: Windows.ApplicationModel.DataTransfer.IDataTransferManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ShareProvidersRequested(self: Windows.ApplicationModel.DataTransfer.IDataTransferManager2, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.DataTransfer.DataTransferManager, Windows.ApplicationModel.DataTransfer.ShareProvidersRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ShareProvidersRequested(self: Windows.ApplicationModel.DataTransfer.IDataTransferManager2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def ShowShareUIWithOptions(cls: Windows.ApplicationModel.DataTransfer.IDataTransferManagerStatics3, options: Windows.ApplicationModel.DataTransfer.ShareUIOptions) -> Void: ...
    @winrt_classmethod
    def IsSupported(cls: Windows.ApplicationModel.DataTransfer.IDataTransferManagerStatics2) -> Boolean: ...
    @winrt_classmethod
    def ShowShareUI(cls: Windows.ApplicationModel.DataTransfer.IDataTransferManagerStatics) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.ApplicationModel.DataTransfer.IDataTransferManagerStatics) -> Windows.ApplicationModel.DataTransfer.DataTransferManager: ...
class HtmlFormatHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    @winrt_classmethod
    def GetStaticFragment(cls: Windows.ApplicationModel.DataTransfer.IHtmlFormatHelperStatics, htmlFormat: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def CreateHtmlFormat(cls: Windows.ApplicationModel.DataTransfer.IHtmlFormatHelperStatics, htmlFragment: WinRT_String) -> WinRT_String: ...
class IClipboardContentOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    def get_RoamingFormats(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(11)
    def get_HistoryFormats(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    IsRoamable = property(get_IsRoamable, put_IsRoamable)
    IsAllowedInHistory = property(get_IsAllowedInHistory, put_IsAllowedInHistory)
    RoamingFormats = property(get_RoamingFormats, None)
    HistoryFormats = property(get_HistoryFormats, None)
class IClipboardHistoryChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c0be453f-8ea2-53ce-9aba-8d2212573452}')
class IClipboardHistoryItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0173bd8a-afff-5c50-ab92-3d19f481ec58}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def get_Content(self) -> Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    Id = property(get_Id, None)
    Timestamp = property(get_Timestamp, None)
    Content = property(get_Content, None)
class IClipboardHistoryItemsResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e6dfdee6-0ee2-52e3-852b-f295db65939a}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.ApplicationModel.DataTransfer.ClipboardHistoryItemsResultStatus: ...
    @winrt_commethod(7)
    def get_Items(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.DataTransfer.ClipboardHistoryItem]: ...
    Status = property(get_Status, None)
    Items = property(get_Items, None)
class IClipboardStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c627e291-34e2-4963-8eed-93cbb0ea3d70}')
    @winrt_commethod(6)
    def GetContent(self) -> Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_commethod(7)
    def SetContent(self, content: Windows.ApplicationModel.DataTransfer.DataPackage) -> Void: ...
    @winrt_commethod(8)
    def Flush(self) -> Void: ...
    @winrt_commethod(9)
    def Clear(self) -> Void: ...
    @winrt_commethod(10)
    def add_ContentChanged(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ContentChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IClipboardStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{d2ac1b6a-d29f-554b-b303-f0452345fe02}')
    @winrt_commethod(6)
    def GetHistoryItemsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.DataTransfer.ClipboardHistoryItemsResult]: ...
    @winrt_commethod(7)
    def ClearHistory(self) -> Boolean: ...
    @winrt_commethod(8)
    def DeleteItemFromHistory(self, item: Windows.ApplicationModel.DataTransfer.ClipboardHistoryItem) -> Boolean: ...
    @winrt_commethod(9)
    def SetHistoryItemAsContent(self, item: Windows.ApplicationModel.DataTransfer.ClipboardHistoryItem) -> Windows.ApplicationModel.DataTransfer.SetHistoryItemAsContentStatus: ...
    @winrt_commethod(10)
    def IsHistoryEnabled(self) -> Boolean: ...
    @winrt_commethod(11)
    def IsRoamingEnabled(self) -> Boolean: ...
    @winrt_commethod(12)
    def SetContentWithOptions(self, content: Windows.ApplicationModel.DataTransfer.DataPackage, options: Windows.ApplicationModel.DataTransfer.ClipboardContentOptions) -> Boolean: ...
    @winrt_commethod(13)
    def add_HistoryChanged(self, handler: Windows.Foundation.EventHandler[Windows.ApplicationModel.DataTransfer.ClipboardHistoryChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_HistoryChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def add_RoamingEnabledChanged(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_RoamingEnabledChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_HistoryEnabledChanged(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_HistoryEnabledChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IDataPackage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{61ebf5c7-efea-4346-9554-981d7e198ffe}')
    @winrt_commethod(6)
    def GetView(self) -> Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_commethod(7)
    def get_Properties(self) -> Windows.ApplicationModel.DataTransfer.DataPackagePropertySet: ...
    @winrt_commethod(8)
    def get_RequestedOperation(self) -> Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    @winrt_commethod(9)
    def put_RequestedOperation(self, value: Windows.ApplicationModel.DataTransfer.DataPackageOperation) -> Void: ...
    @winrt_commethod(10)
    def add_OperationCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.DataTransfer.DataPackage, Windows.ApplicationModel.DataTransfer.OperationCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_OperationCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_Destroyed(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.DataTransfer.DataPackage, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_Destroyed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def SetData(self, formatId: WinRT_String, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(15)
    def SetDataProvider(self, formatId: WinRT_String, delayRenderer: Windows.ApplicationModel.DataTransfer.DataProviderHandler) -> Void: ...
    @winrt_commethod(16)
    def SetText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(17)
    def SetUri(self, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(18)
    def SetHtmlFormat(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(19)
    def get_ResourceMap(self) -> Windows.Foundation.Collections.IMap[WinRT_String, Windows.Storage.Streams.RandomAccessStreamReference]: ...
    @winrt_commethod(20)
    def SetRtf(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(21)
    def SetBitmap(self, value: Windows.Storage.Streams.RandomAccessStreamReference) -> Void: ...
    @winrt_commethod(22)
    def SetStorageItemsReadOnly(self, value: Windows.Foundation.Collections.IIterable[Windows.Storage.IStorageItem]) -> Void: ...
    @winrt_commethod(23)
    def SetStorageItems(self, value: Windows.Foundation.Collections.IIterable[Windows.Storage.IStorageItem], readOnly: Boolean) -> Void: ...
    Properties = property(get_Properties, None)
    RequestedOperation = property(get_RequestedOperation, put_RequestedOperation)
    ResourceMap = property(get_ResourceMap, None)
class IDataPackage2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{041c1fe9-2409-45e1-a538-4c53eeee04a7}')
    @winrt_commethod(6)
    def SetApplicationLink(self, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(7)
    def SetWebLink(self, value: Windows.Foundation.Uri) -> Void: ...
class IDataPackage3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{88f31f5d-787b-4d32-965a-a9838105a056}')
    @winrt_commethod(6)
    def add_ShareCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.DataTransfer.DataPackage, Windows.ApplicationModel.DataTransfer.ShareCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ShareCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IDataPackage4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{13a24ec8-9382-536f-852a-3045e1b29a3b}')
    @winrt_commethod(6)
    def add_ShareCanceled(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.DataTransfer.DataPackage, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ShareCanceled(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IDataPackagePropertySet(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    def get_Thumbnail(self) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(11)
    def put_Thumbnail(self, value: Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(12)
    def get_FileTypes(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(13)
    def get_ApplicationName(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_ApplicationName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_ApplicationListingUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(16)
    def put_ApplicationListingUri(self, value: Windows.Foundation.Uri) -> Void: ...
    Title = property(get_Title, put_Title)
    Description = property(get_Description, put_Description)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
    FileTypes = property(get_FileTypes, None)
    ApplicationName = property(get_ApplicationName, put_ApplicationName)
    ApplicationListingUri = property(get_ApplicationListingUri, put_ApplicationListingUri)
class IDataPackagePropertySet2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{eb505d4a-9800-46aa-b181-7b6f0f2b919a}')
    @winrt_commethod(6)
    def get_ContentSourceWebLink(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_ContentSourceWebLink(self, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def get_ContentSourceApplicationLink(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(9)
    def put_ContentSourceApplicationLink(self, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(10)
    def get_PackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_PackageFamilyName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_Square30x30Logo(self) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(13)
    def put_Square30x30Logo(self, value: Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(14)
    def get_LogoBackgroundColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(15)
    def put_LogoBackgroundColor(self, value: Windows.UI.Color) -> Void: ...
    ContentSourceWebLink = property(get_ContentSourceWebLink, put_ContentSourceWebLink)
    ContentSourceApplicationLink = property(get_ContentSourceApplicationLink, put_ContentSourceApplicationLink)
    PackageFamilyName = property(get_PackageFamilyName, put_PackageFamilyName)
    Square30x30Logo = property(get_Square30x30Logo, put_Square30x30Logo)
    LogoBackgroundColor = property(get_LogoBackgroundColor, put_LogoBackgroundColor)
class IDataPackagePropertySet3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{9e87fd9b-5205-401b-874a-455653bd39e8}')
    @winrt_commethod(6)
    def get_EnterpriseId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_EnterpriseId(self, value: WinRT_String) -> Void: ...
    EnterpriseId = property(get_EnterpriseId, put_EnterpriseId)
class IDataPackagePropertySet4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{6390ebf5-1739-4c74-b22f-865fab5e8545}')
    @winrt_commethod(6)
    def get_ContentSourceUserActivityJson(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_ContentSourceUserActivityJson(self, value: WinRT_String) -> Void: ...
    ContentSourceUserActivityJson = property(get_ContentSourceUserActivityJson, put_ContentSourceUserActivityJson)
class IDataPackagePropertySetView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b94cec01-0c1a-4c57-be55-75d01289735d}')
    @winrt_commethod(6)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Thumbnail(self) -> Windows.Storage.Streams.RandomAccessStreamReference: ...
    @winrt_commethod(9)
    def get_FileTypes(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(10)
    def get_ApplicationName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_ApplicationListingUri(self) -> Windows.Foundation.Uri: ...
    Title = property(get_Title, None)
    Description = property(get_Description, None)
    Thumbnail = property(get_Thumbnail, None)
    FileTypes = property(get_FileTypes, None)
    ApplicationName = property(get_ApplicationName, None)
    ApplicationListingUri = property(get_ApplicationListingUri, None)
class IDataPackagePropertySetView2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{6054509b-8ebe-4feb-9c1e-75e69de54b84}')
    @winrt_commethod(6)
    def get_PackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ContentSourceWebLink(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_ContentSourceApplicationLink(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(9)
    def get_Square30x30Logo(self) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(10)
    def get_LogoBackgroundColor(self) -> Windows.UI.Color: ...
    PackageFamilyName = property(get_PackageFamilyName, None)
    ContentSourceWebLink = property(get_ContentSourceWebLink, None)
    ContentSourceApplicationLink = property(get_ContentSourceApplicationLink, None)
    Square30x30Logo = property(get_Square30x30Logo, None)
    LogoBackgroundColor = property(get_LogoBackgroundColor, None)
class IDataPackagePropertySetView3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{db764ce5-d174-495c-84fc-1a51f6ab45d7}')
    @winrt_commethod(6)
    def get_EnterpriseId(self) -> WinRT_String: ...
    EnterpriseId = property(get_EnterpriseId, None)
class IDataPackagePropertySetView4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{4474c80d-d16f-40ae-9580-6f8562b94235}')
    @winrt_commethod(6)
    def get_ContentSourceUserActivityJson(self) -> WinRT_String: ...
    ContentSourceUserActivityJson = property(get_ContentSourceUserActivityJson, None)
class IDataPackagePropertySetView5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{6f0a9445-3760-50bb-8523-c4202ded7d78}')
    @winrt_commethod(6)
    def get_IsFromRoamingClipboard(self) -> Boolean: ...
    IsFromRoamingClipboard = property(get_IsFromRoamingClipboard, None)
class IDataPackageView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{7b840471-5900-4d85-a90b-10cb85fe3552}')
    @winrt_commethod(6)
    def get_Properties(self) -> Windows.ApplicationModel.DataTransfer.DataPackagePropertySetView: ...
    @winrt_commethod(7)
    def get_RequestedOperation(self) -> Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    @winrt_commethod(8)
    def ReportOperationCompleted(self, value: Windows.ApplicationModel.DataTransfer.DataPackageOperation) -> Void: ...
    @winrt_commethod(9)
    def get_AvailableFormats(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(10)
    def Contains(self, formatId: WinRT_String) -> Boolean: ...
    @winrt_commethod(11)
    def GetDataAsync(self, formatId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_commethod(12)
    def GetTextAsync(self) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(13)
    def GetCustomTextAsync(self, formatId: WinRT_String) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(14)
    def GetUriAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Uri]: ...
    @winrt_commethod(15)
    def GetHtmlFormatAsync(self) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(16)
    def GetResourceMapAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Storage.Streams.RandomAccessStreamReference]]: ...
    @winrt_commethod(17)
    def GetRtfAsync(self) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(18)
    def GetBitmapAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.RandomAccessStreamReference]: ...
    @winrt_commethod(19)
    def GetStorageItemsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Storage.IStorageItem]]: ...
    Properties = property(get_Properties, None)
    RequestedOperation = property(get_RequestedOperation, None)
    AvailableFormats = property(get_AvailableFormats, None)
class IDataPackageView2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{40ecba95-2450-4c1d-b6b4-ed45463dee9c}')
    @winrt_commethod(6)
    def GetApplicationLinkAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Uri]: ...
    @winrt_commethod(7)
    def GetWebLinkAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Uri]: ...
class IDataPackageView3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{d37771a8-ddad-4288-8428-d1cae394128b}')
    @winrt_commethod(6)
    def RequestAccessAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(7)
    def RequestAccessWithEnterpriseIdAsync(self, enterpriseId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(8)
    def UnlockAndAssumeEnterpriseIdentity(self) -> Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult: ...
class IDataPackageView4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{dfe96f1f-e042-4433-a09f-26d6ffda8b85}')
    @winrt_commethod(6)
    def SetAcceptedFormatId(self, formatId: WinRT_String) -> Void: ...
class IDataProviderDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c2cf2373-2d26-43d9-b69d-dcb86d03f6da}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IDataProviderRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{ebbc7157-d3c8-47da-acde-f82388d5f716}')
    @winrt_commethod(6)
    def get_FormatId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Deadline(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.ApplicationModel.DataTransfer.DataProviderDeferral: ...
    @winrt_commethod(9)
    def SetData(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    FormatId = property(get_FormatId, None)
    Deadline = property(get_Deadline, None)
class IDataRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{4341ae3b-fc12-4e53-8c02-ac714c415a27}')
    @winrt_commethod(6)
    def get_Data(self) -> Windows.ApplicationModel.DataTransfer.DataPackage: ...
    @winrt_commethod(7)
    def put_Data(self, value: Windows.ApplicationModel.DataTransfer.DataPackage) -> Void: ...
    @winrt_commethod(8)
    def get_Deadline(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(9)
    def FailWithDisplayText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def GetDeferral(self) -> Windows.ApplicationModel.DataTransfer.DataRequestDeferral: ...
    Data = property(get_Data, put_Data)
    Deadline = property(get_Deadline, None)
class IDataRequestDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{6dc4b89f-0386-4263-87c1-ed7dce30890e}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IDataRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{cb8ba807-6ac5-43c9-8ac5-9ba232163182}')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.DataTransfer.DataRequest: ...
    Request = property(get_Request, None)
class IDataTransferManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a5caee9b-8708-49d1-8d36-67d25a8da00c}')
    @winrt_commethod(6)
    def add_DataRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.DataTransfer.DataTransferManager, Windows.ApplicationModel.DataTransfer.DataRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_DataRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_TargetApplicationChosen(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.DataTransfer.DataTransferManager, Windows.ApplicationModel.DataTransfer.TargetApplicationChosenEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_TargetApplicationChosen(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IDataTransferManager2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{30ae7d71-8ba8-4c02-8e3f-ddb23b388715}')
    @winrt_commethod(6)
    def add_ShareProvidersRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.DataTransfer.DataTransferManager, Windows.ApplicationModel.DataTransfer.ShareProvidersRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ShareProvidersRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IDataTransferManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a9da01aa-e00e-4cfe-aa44-2dd932dca3d8}')
    @winrt_commethod(6)
    def ShowShareUI(self) -> Void: ...
    @winrt_commethod(7)
    def GetForCurrentView(self) -> Windows.ApplicationModel.DataTransfer.DataTransferManager: ...
class IDataTransferManagerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c54ec2ec-9f97-4d63-9868-395e271ad8f5}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
class IDataTransferManagerStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{05845473-6c82-4f5c-ac23-62e458361fac}')
    @winrt_commethod(6)
    def ShowShareUIWithOptions(self, options: Windows.ApplicationModel.DataTransfer.ShareUIOptions) -> Void: ...
class IHtmlFormatHelperStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e22e7749-dd70-446f-aefc-61cee59f655e}')
    @winrt_commethod(6)
    def GetStaticFragment(self, htmlFormat: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(7)
    def CreateHtmlFormat(self, htmlFragment: WinRT_String) -> WinRT_String: ...
class IOperationCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e7af329d-051d-4fab-b1a9-47fd77f70a41}')
    @winrt_commethod(6)
    def get_Operation(self) -> Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    Operation = property(get_Operation, None)
class IOperationCompletedEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{858fa073-1e19-4105-b2f7-c8478808d562}')
    @winrt_commethod(6)
    def get_AcceptedFormatId(self) -> WinRT_String: ...
    AcceptedFormatId = property(get_AcceptedFormatId, None)
class IShareCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{4574c442-f913-4f60-9df7-cc4060ab1916}')
    @winrt_commethod(6)
    def get_ShareTarget(self) -> Windows.ApplicationModel.DataTransfer.ShareTargetInfo: ...
    ShareTarget = property(get_ShareTarget, None)
class IShareProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2fabe026-443e-4cda-af25-8d81070efd80}')
    @winrt_commethod(6)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayIcon(self) -> Windows.Storage.Streams.RandomAccessStreamReference: ...
    @winrt_commethod(8)
    def get_BackgroundColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(9)
    def get_Tag(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(10)
    def put_Tag(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    Title = property(get_Title, None)
    DisplayIcon = property(get_DisplayIcon, None)
    BackgroundColor = property(get_BackgroundColor, None)
    Tag = property(get_Tag, put_Tag)
class IShareProviderFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{172a174c-e79e-4f6d-b07d-128f469e0296}')
    @winrt_commethod(6)
    def Create(self, title: WinRT_String, displayIcon: Windows.Storage.Streams.RandomAccessStreamReference, backgroundColor: Windows.UI.Color, handler: Windows.ApplicationModel.DataTransfer.ShareProviderHandler) -> Windows.ApplicationModel.DataTransfer.ShareProvider: ...
class IShareProviderOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{19cef937-d435-4179-b6af-14e0492b69f6}')
    @winrt_commethod(6)
    def get_Data(self) -> Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_commethod(7)
    def get_Provider(self) -> Windows.ApplicationModel.DataTransfer.ShareProvider: ...
    @winrt_commethod(8)
    def ReportCompleted(self) -> Void: ...
    Data = property(get_Data, None)
    Provider = property(get_Provider, None)
class IShareProvidersRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f888f356-a3f8-4fce-85e4-8826e63be799}')
    @winrt_commethod(6)
    def get_Providers(self) -> Windows.Foundation.Collections.IVector[Windows.ApplicationModel.DataTransfer.ShareProvider]: ...
    @winrt_commethod(7)
    def get_Data(self) -> Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Providers = property(get_Providers, None)
    Data = property(get_Data, None)
class IShareTargetInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{385be607-c6e8-4114-b294-28f3bb6f9904}')
    @winrt_commethod(6)
    def get_AppUserModelId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ShareProvider(self) -> Windows.ApplicationModel.DataTransfer.ShareProvider: ...
    AppUserModelId = property(get_AppUserModelId, None)
    ShareProvider = property(get_ShareProvider, None)
class IShareUIOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{72fa8a80-342f-4d90-9551-2ae04e37680c}')
    @winrt_commethod(6)
    def get_Theme(self) -> Windows.ApplicationModel.DataTransfer.ShareUITheme: ...
    @winrt_commethod(7)
    def put_Theme(self, value: Windows.ApplicationModel.DataTransfer.ShareUITheme) -> Void: ...
    @winrt_commethod(8)
    def get_SelectionRect(self) -> Windows.Foundation.IReference[Windows.Foundation.Rect]: ...
    @winrt_commethod(9)
    def put_SelectionRect(self, value: Windows.Foundation.IReference[Windows.Foundation.Rect]) -> Void: ...
    Theme = property(get_Theme, put_Theme)
    SelectionRect = property(get_SelectionRect, put_SelectionRect)
class ISharedStorageAccessManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c6132ada-34b1-4849-bd5f-d09fee3158c5}')
    @winrt_commethod(6)
    def AddFile(self, file: Windows.Storage.IStorageFile) -> WinRT_String: ...
    @winrt_commethod(7)
    def RedeemTokenForFileAsync(self, token: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_commethod(8)
    def RemoveFile(self, token: WinRT_String) -> Void: ...
class IStandardDataFormatsStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{42a254f4-9d76-42e8-861b-47c25dd0cf71}')
    @winrt_commethod(6)
    def get_WebLink(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ApplicationLink(self) -> WinRT_String: ...
    WebLink = property(get_WebLink, None)
    ApplicationLink = property(get_ApplicationLink, None)
class IStandardDataFormatsStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{3b57b069-01d4-474c-8b5f-bc8e27f38b21}')
    @winrt_commethod(6)
    def get_UserActivityJsonArray(self) -> WinRT_String: ...
    UserActivityJsonArray = property(get_UserActivityJsonArray, None)
class ITargetApplicationChosenEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{ca6fb8ac-2987-4ee3-9c54-d8afbcb86c1d}')
    @winrt_commethod(6)
    def get_ApplicationName(self) -> WinRT_String: ...
    ApplicationName = property(get_ApplicationName, None)
class OperationCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.IOperationCompletedEventArgs
    _classid_ = 'Windows.ApplicationModel.DataTransfer.OperationCompletedEventArgs'
    @winrt_mixinmethod
    def get_Operation(self: Windows.ApplicationModel.DataTransfer.IOperationCompletedEventArgs) -> Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    @winrt_mixinmethod
    def get_AcceptedFormatId(self: Windows.ApplicationModel.DataTransfer.IOperationCompletedEventArgs2) -> WinRT_String: ...
    Operation = property(get_Operation, None)
    AcceptedFormatId = property(get_AcceptedFormatId, None)
SetHistoryItemAsContentStatus = Int32
SetHistoryItemAsContentStatus_Success: SetHistoryItemAsContentStatus = 0
SetHistoryItemAsContentStatus_AccessDenied: SetHistoryItemAsContentStatus = 1
SetHistoryItemAsContentStatus_ItemDeleted: SetHistoryItemAsContentStatus = 2
class ShareCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.IShareCompletedEventArgs
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ShareCompletedEventArgs'
    @winrt_mixinmethod
    def get_ShareTarget(self: Windows.ApplicationModel.DataTransfer.IShareCompletedEventArgs) -> Windows.ApplicationModel.DataTransfer.ShareTargetInfo: ...
    ShareTarget = property(get_ShareTarget, None)
class ShareProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.IShareProvider
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ShareProvider'
    @winrt_factorymethod
    def Create(cls: Windows.ApplicationModel.DataTransfer.IShareProviderFactory, title: WinRT_String, displayIcon: Windows.Storage.Streams.RandomAccessStreamReference, backgroundColor: Windows.UI.Color, handler: Windows.ApplicationModel.DataTransfer.ShareProviderHandler) -> Windows.ApplicationModel.DataTransfer.ShareProvider: ...
    @winrt_mixinmethod
    def get_Title(self: Windows.ApplicationModel.DataTransfer.IShareProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayIcon(self: Windows.ApplicationModel.DataTransfer.IShareProvider) -> Windows.Storage.Streams.RandomAccessStreamReference: ...
    @winrt_mixinmethod
    def get_BackgroundColor(self: Windows.ApplicationModel.DataTransfer.IShareProvider) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def get_Tag(self: Windows.ApplicationModel.DataTransfer.IShareProvider) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def put_Tag(self: Windows.ApplicationModel.DataTransfer.IShareProvider, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    Title = property(get_Title, None)
    DisplayIcon = property(get_DisplayIcon, None)
    BackgroundColor = property(get_BackgroundColor, None)
    Tag = property(get_Tag, put_Tag)
class ShareProviderHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e7f9d9ba-e1ba-4e4d-bd65-d43845d3212f}')
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ShareProviderHandler'
    @winrt_commethod(3)
    def Invoke(self, operation: Windows.ApplicationModel.DataTransfer.ShareProviderOperation) -> Void: ...
class ShareProviderOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.IShareProviderOperation
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ShareProviderOperation'
    @winrt_mixinmethod
    def get_Data(self: Windows.ApplicationModel.DataTransfer.IShareProviderOperation) -> Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_mixinmethod
    def get_Provider(self: Windows.ApplicationModel.DataTransfer.IShareProviderOperation) -> Windows.ApplicationModel.DataTransfer.ShareProvider: ...
    @winrt_mixinmethod
    def ReportCompleted(self: Windows.ApplicationModel.DataTransfer.IShareProviderOperation) -> Void: ...
    Data = property(get_Data, None)
    Provider = property(get_Provider, None)
class ShareProvidersRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.IShareProvidersRequestedEventArgs
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ShareProvidersRequestedEventArgs'
    @winrt_mixinmethod
    def get_Providers(self: Windows.ApplicationModel.DataTransfer.IShareProvidersRequestedEventArgs) -> Windows.Foundation.Collections.IVector[Windows.ApplicationModel.DataTransfer.ShareProvider]: ...
    @winrt_mixinmethod
    def get_Data(self: Windows.ApplicationModel.DataTransfer.IShareProvidersRequestedEventArgs) -> Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.DataTransfer.IShareProvidersRequestedEventArgs) -> Windows.Foundation.Deferral: ...
    Providers = property(get_Providers, None)
    Data = property(get_Data, None)
class ShareTargetInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.IShareTargetInfo
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ShareTargetInfo'
    @winrt_mixinmethod
    def get_AppUserModelId(self: Windows.ApplicationModel.DataTransfer.IShareTargetInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ShareProvider(self: Windows.ApplicationModel.DataTransfer.IShareTargetInfo) -> Windows.ApplicationModel.DataTransfer.ShareProvider: ...
    AppUserModelId = property(get_AppUserModelId, None)
    ShareProvider = property(get_ShareProvider, None)
class ShareUIOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.IShareUIOptions
    _classid_ = 'Windows.ApplicationModel.DataTransfer.ShareUIOptions'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.DataTransfer.ShareUIOptions: ...
    @winrt_mixinmethod
    def get_Theme(self: Windows.ApplicationModel.DataTransfer.IShareUIOptions) -> Windows.ApplicationModel.DataTransfer.ShareUITheme: ...
    @winrt_mixinmethod
    def put_Theme(self: Windows.ApplicationModel.DataTransfer.IShareUIOptions, value: Windows.ApplicationModel.DataTransfer.ShareUITheme) -> Void: ...
    @winrt_mixinmethod
    def get_SelectionRect(self: Windows.ApplicationModel.DataTransfer.IShareUIOptions) -> Windows.Foundation.IReference[Windows.Foundation.Rect]: ...
    @winrt_mixinmethod
    def put_SelectionRect(self: Windows.ApplicationModel.DataTransfer.IShareUIOptions, value: Windows.Foundation.IReference[Windows.Foundation.Rect]) -> Void: ...
    Theme = property(get_Theme, put_Theme)
    SelectionRect = property(get_SelectionRect, put_SelectionRect)
ShareUITheme = Int32
ShareUITheme_Default: ShareUITheme = 0
ShareUITheme_Light: ShareUITheme = 1
ShareUITheme_Dark: ShareUITheme = 2
class SharedStorageAccessManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    @winrt_classmethod
    def AddFile(cls: Windows.ApplicationModel.DataTransfer.ISharedStorageAccessManagerStatics, file: Windows.Storage.IStorageFile) -> WinRT_String: ...
    @winrt_classmethod
    def RedeemTokenForFileAsync(cls: Windows.ApplicationModel.DataTransfer.ISharedStorageAccessManagerStatics, token: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_classmethod
    def RemoveFile(cls: Windows.ApplicationModel.DataTransfer.ISharedStorageAccessManagerStatics, token: WinRT_String) -> Void: ...
class StandardDataFormats(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    @winrt_classmethod
    def get_UserActivityJsonArray(cls: Windows.ApplicationModel.DataTransfer.IStandardDataFormatsStatics3) -> WinRT_String: ...
    @winrt_classmethod
    def get_WebLink(cls: Windows.ApplicationModel.DataTransfer.IStandardDataFormatsStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_ApplicationLink(cls: Windows.ApplicationModel.DataTransfer.IStandardDataFormatsStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_Text(cls: Windows.ApplicationModel.DataTransfer.IStandardDataFormatsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Uri(cls: Windows.ApplicationModel.DataTransfer.IStandardDataFormatsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Html(cls: Windows.ApplicationModel.DataTransfer.IStandardDataFormatsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Rtf(cls: Windows.ApplicationModel.DataTransfer.IStandardDataFormatsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Bitmap(cls: Windows.ApplicationModel.DataTransfer.IStandardDataFormatsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_StorageItems(cls: Windows.ApplicationModel.DataTransfer.IStandardDataFormatsStatics) -> WinRT_String: ...
    UserActivityJsonArray = property(get_UserActivityJsonArray, None)
    WebLink = property(get_WebLink, None)
    ApplicationLink = property(get_ApplicationLink, None)
    Text = property(get_Text, None)
    Uri = property(get_Uri, None)
    Html = property(get_Html, None)
    Rtf = property(get_Rtf, None)
    Bitmap = property(get_Bitmap, None)
    StorageItems = property(get_StorageItems, None)
class TargetApplicationChosenEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.ITargetApplicationChosenEventArgs
    _classid_ = 'Windows.ApplicationModel.DataTransfer.TargetApplicationChosenEventArgs'
    @winrt_mixinmethod
    def get_ApplicationName(self: Windows.ApplicationModel.DataTransfer.ITargetApplicationChosenEventArgs) -> WinRT_String: ...
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
make_head(_module, 'DataProviderHandler')
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
make_head(_module, 'ShareProviderHandler')
make_head(_module, 'ShareProviderOperation')
make_head(_module, 'ShareProvidersRequestedEventArgs')
make_head(_module, 'ShareTargetInfo')
make_head(_module, 'ShareUIOptions')
make_head(_module, 'SharedStorageAccessManager')
make_head(_module, 'StandardDataFormats')
make_head(_module, 'TargetApplicationChosenEventArgs')
