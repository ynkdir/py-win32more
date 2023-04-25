from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, WinRT_String, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
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
class Clipboard(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.DataTransfer.Clipboard'
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
class ClipboardContentOptions(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.DataTransfer.ClipboardContentOptions'
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
class ClipboardHistoryChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.DataTransfer.ClipboardHistoryChangedEventArgs'
class ClipboardHistoryItem(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.DataTransfer.ClipboardHistoryItem'
    @winrt_mixinmethod
    def get_Id(self: Windows.ApplicationModel.DataTransfer.IClipboardHistoryItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.ApplicationModel.DataTransfer.IClipboardHistoryItem) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Content(self: Windows.ApplicationModel.DataTransfer.IClipboardHistoryItem) -> Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    Id = property(get_Id, None)
    Timestamp = property(get_Timestamp, None)
    Content = property(get_Content, None)
class ClipboardHistoryItemsResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.DataTransfer.ClipboardHistoryItemsResult'
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
class DataPackage(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.DataTransfer.DataPackage'
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
class DataPackagePropertySet(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.DataTransfer.DataPackagePropertySet'
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
class DataPackagePropertySetView(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.DataTransfer.DataPackagePropertySetView'
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
class DataPackageView(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.DataTransfer.DataPackageView'
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
class DataProviderDeferral(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.DataTransfer.DataProviderDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.ApplicationModel.DataTransfer.IDataProviderDeferral) -> Void: ...
class DataProviderHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e7ecd720-f2f4-4a2d-92-0e-17-0a-2f-48-2a-27')
    ClassId = 'Windows.ApplicationModel.DataTransfer.DataProviderHandler'
    @winrt_commethod(3)
    def Invoke(self, request: Windows.ApplicationModel.DataTransfer.DataProviderRequest) -> Void: ...
class DataProviderRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.DataTransfer.DataProviderRequest'
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
class DataRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.DataTransfer.DataRequest'
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
class DataRequestDeferral(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.DataTransfer.DataRequestDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.ApplicationModel.DataTransfer.IDataRequestDeferral) -> Void: ...
class DataRequestedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.DataTransfer.DataRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.DataTransfer.IDataRequestedEventArgs) -> Windows.ApplicationModel.DataTransfer.DataRequest: ...
    Request = property(get_Request, None)
class DataTransferManager(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.DataTransfer.DataTransferManager'
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
class HtmlFormatHelper(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.DataTransfer.HtmlFormatHelper'
    @winrt_classmethod
    def GetStaticFragment(cls: Windows.ApplicationModel.DataTransfer.IHtmlFormatHelperStatics, htmlFormat: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def CreateHtmlFormat(cls: Windows.ApplicationModel.DataTransfer.IHtmlFormatHelperStatics, htmlFragment: WinRT_String) -> WinRT_String: ...
class IClipboardContentOptions(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e888a98c-ad4b-5447-a0-56-ab-35-56-27-6d-2b')
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
class IClipboardHistoryChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c0be453f-8ea2-53ce-9a-ba-8d-22-12-57-34-52')
class IClipboardHistoryItem(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0173bd8a-afff-5c50-ab-92-3d-19-f4-81-ec-58')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def get_Content(self) -> Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    Id = property(get_Id, None)
    Timestamp = property(get_Timestamp, None)
    Content = property(get_Content, None)
class IClipboardHistoryItemsResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e6dfdee6-0ee2-52e3-85-2b-f2-95-db-65-93-9a')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.ApplicationModel.DataTransfer.ClipboardHistoryItemsResultStatus: ...
    @winrt_commethod(7)
    def get_Items(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.DataTransfer.ClipboardHistoryItem]: ...
    Status = property(get_Status, None)
    Items = property(get_Items, None)
class IClipboardStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c627e291-34e2-4963-8e-ed-93-cb-b0-ea-3d-70')
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
class IClipboardStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d2ac1b6a-d29f-554b-b3-03-f0-45-23-45-fe-02')
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
class IDataPackage(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('61ebf5c7-efea-4346-95-54-98-1d-7e-19-8f-fe')
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
class IDataPackage2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('041c1fe9-2409-45e1-a5-38-4c-53-ee-ee-04-a7')
    @winrt_commethod(6)
    def SetApplicationLink(self, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(7)
    def SetWebLink(self, value: Windows.Foundation.Uri) -> Void: ...
class IDataPackage3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('88f31f5d-787b-4d32-96-5a-a9-83-81-05-a0-56')
    @winrt_commethod(6)
    def add_ShareCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.DataTransfer.DataPackage, Windows.ApplicationModel.DataTransfer.ShareCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ShareCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IDataPackage4(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('13a24ec8-9382-536f-85-2a-30-45-e1-b2-9a-3b')
    @winrt_commethod(6)
    def add_ShareCanceled(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.DataTransfer.DataPackage, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ShareCanceled(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IDataPackagePropertySet(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cd1c93eb-4c4c-443a-a8-d3-f5-c2-41-e9-16-89')
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
class IDataPackagePropertySet2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('eb505d4a-9800-46aa-b1-81-7b-6f-0f-2b-91-9a')
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
class IDataPackagePropertySet3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9e87fd9b-5205-401b-87-4a-45-56-53-bd-39-e8')
    @winrt_commethod(6)
    def get_EnterpriseId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_EnterpriseId(self, value: WinRT_String) -> Void: ...
    EnterpriseId = property(get_EnterpriseId, put_EnterpriseId)
class IDataPackagePropertySet4(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6390ebf5-1739-4c74-b2-2f-86-5f-ab-5e-85-45')
    @winrt_commethod(6)
    def get_ContentSourceUserActivityJson(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_ContentSourceUserActivityJson(self, value: WinRT_String) -> Void: ...
    ContentSourceUserActivityJson = property(get_ContentSourceUserActivityJson, put_ContentSourceUserActivityJson)
class IDataPackagePropertySetView(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b94cec01-0c1a-4c57-be-55-75-d0-12-89-73-5d')
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
class IDataPackagePropertySetView2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6054509b-8ebe-4feb-9c-1e-75-e6-9d-e5-4b-84')
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
class IDataPackagePropertySetView3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('db764ce5-d174-495c-84-fc-1a-51-f6-ab-45-d7')
    @winrt_commethod(6)
    def get_EnterpriseId(self) -> WinRT_String: ...
    EnterpriseId = property(get_EnterpriseId, None)
class IDataPackagePropertySetView4(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4474c80d-d16f-40ae-95-80-6f-85-62-b9-42-35')
    @winrt_commethod(6)
    def get_ContentSourceUserActivityJson(self) -> WinRT_String: ...
    ContentSourceUserActivityJson = property(get_ContentSourceUserActivityJson, None)
class IDataPackagePropertySetView5(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6f0a9445-3760-50bb-85-23-c4-20-2d-ed-7d-78')
    @winrt_commethod(6)
    def get_IsFromRoamingClipboard(self) -> Boolean: ...
    IsFromRoamingClipboard = property(get_IsFromRoamingClipboard, None)
class IDataPackageView(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7b840471-5900-4d85-a9-0b-10-cb-85-fe-35-52')
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
class IDataPackageView2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('40ecba95-2450-4c1d-b6-b4-ed-45-46-3d-ee-9c')
    @winrt_commethod(6)
    def GetApplicationLinkAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Uri]: ...
    @winrt_commethod(7)
    def GetWebLinkAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Uri]: ...
class IDataPackageView3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d37771a8-ddad-4288-84-28-d1-ca-e3-94-12-8b')
    @winrt_commethod(6)
    def RequestAccessAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(7)
    def RequestAccessWithEnterpriseIdAsync(self, enterpriseId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(8)
    def UnlockAndAssumeEnterpriseIdentity(self) -> Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult: ...
class IDataPackageView4(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('dfe96f1f-e042-4433-a0-9f-26-d6-ff-da-8b-85')
    @winrt_commethod(6)
    def SetAcceptedFormatId(self, formatId: WinRT_String) -> Void: ...
class IDataProviderDeferral(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c2cf2373-2d26-43d9-b6-9d-dc-b8-6d-03-f6-da')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IDataProviderRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ebbc7157-d3c8-47da-ac-de-f8-23-88-d5-f7-16')
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
class IDataRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4341ae3b-fc12-4e53-8c-02-ac-71-4c-41-5a-27')
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
class IDataRequestDeferral(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6dc4b89f-0386-4263-87-c1-ed-7d-ce-30-89-0e')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IDataRequestedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cb8ba807-6ac5-43c9-8a-c5-9b-a2-32-16-31-82')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.DataTransfer.DataRequest: ...
    Request = property(get_Request, None)
class IDataTransferManager(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a5caee9b-8708-49d1-8d-36-67-d2-5a-8d-a0-0c')
    @winrt_commethod(6)
    def add_DataRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.DataTransfer.DataTransferManager, Windows.ApplicationModel.DataTransfer.DataRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_DataRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_TargetApplicationChosen(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.DataTransfer.DataTransferManager, Windows.ApplicationModel.DataTransfer.TargetApplicationChosenEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_TargetApplicationChosen(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IDataTransferManager2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('30ae7d71-8ba8-4c02-8e-3f-dd-b2-3b-38-87-15')
    @winrt_commethod(6)
    def add_ShareProvidersRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.DataTransfer.DataTransferManager, Windows.ApplicationModel.DataTransfer.ShareProvidersRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ShareProvidersRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IDataTransferManagerStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a9da01aa-e00e-4cfe-aa-44-2d-d9-32-dc-a3-d8')
    @winrt_commethod(6)
    def ShowShareUI(self) -> Void: ...
    @winrt_commethod(7)
    def GetForCurrentView(self) -> Windows.ApplicationModel.DataTransfer.DataTransferManager: ...
class IDataTransferManagerStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c54ec2ec-9f97-4d63-98-68-39-5e-27-1a-d8-f5')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
class IDataTransferManagerStatics3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('05845473-6c82-4f5c-ac-23-62-e4-58-36-1f-ac')
    @winrt_commethod(6)
    def ShowShareUIWithOptions(self, options: Windows.ApplicationModel.DataTransfer.ShareUIOptions) -> Void: ...
class IHtmlFormatHelperStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e22e7749-dd70-446f-ae-fc-61-ce-e5-9f-65-5e')
    @winrt_commethod(6)
    def GetStaticFragment(self, htmlFormat: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(7)
    def CreateHtmlFormat(self, htmlFragment: WinRT_String) -> WinRT_String: ...
class IOperationCompletedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e7af329d-051d-4fab-b1-a9-47-fd-77-f7-0a-41')
    @winrt_commethod(6)
    def get_Operation(self) -> Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    Operation = property(get_Operation, None)
class IOperationCompletedEventArgs2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('858fa073-1e19-4105-b2-f7-c8-47-88-08-d5-62')
    @winrt_commethod(6)
    def get_AcceptedFormatId(self) -> WinRT_String: ...
    AcceptedFormatId = property(get_AcceptedFormatId, None)
class IShareCompletedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4574c442-f913-4f60-9d-f7-cc-40-60-ab-19-16')
    @winrt_commethod(6)
    def get_ShareTarget(self) -> Windows.ApplicationModel.DataTransfer.ShareTargetInfo: ...
    ShareTarget = property(get_ShareTarget, None)
class IShareProvider(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2fabe026-443e-4cda-af-25-8d-81-07-0e-fd-80')
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
class IShareProviderFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('172a174c-e79e-4f6d-b0-7d-12-8f-46-9e-02-96')
    @winrt_commethod(6)
    def Create(self, title: WinRT_String, displayIcon: Windows.Storage.Streams.RandomAccessStreamReference, backgroundColor: Windows.UI.Color, handler: Windows.ApplicationModel.DataTransfer.ShareProviderHandler) -> Windows.ApplicationModel.DataTransfer.ShareProvider: ...
class IShareProviderOperation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('19cef937-d435-4179-b6-af-14-e0-49-2b-69-f6')
    @winrt_commethod(6)
    def get_Data(self) -> Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_commethod(7)
    def get_Provider(self) -> Windows.ApplicationModel.DataTransfer.ShareProvider: ...
    @winrt_commethod(8)
    def ReportCompleted(self) -> Void: ...
    Data = property(get_Data, None)
    Provider = property(get_Provider, None)
class IShareProvidersRequestedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f888f356-a3f8-4fce-85-e4-88-26-e6-3b-e7-99')
    @winrt_commethod(6)
    def get_Providers(self) -> Windows.Foundation.Collections.IVector[Windows.ApplicationModel.DataTransfer.ShareProvider]: ...
    @winrt_commethod(7)
    def get_Data(self) -> Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Providers = property(get_Providers, None)
    Data = property(get_Data, None)
class IShareTargetInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('385be607-c6e8-4114-b2-94-28-f3-bb-6f-99-04')
    @winrt_commethod(6)
    def get_AppUserModelId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ShareProvider(self) -> Windows.ApplicationModel.DataTransfer.ShareProvider: ...
    AppUserModelId = property(get_AppUserModelId, None)
    ShareProvider = property(get_ShareProvider, None)
class IShareUIOptions(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('72fa8a80-342f-4d90-95-51-2a-e0-4e-37-68-0c')
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
class ISharedStorageAccessManagerStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c6132ada-34b1-4849-bd-5f-d0-9f-ee-31-58-c5')
    @winrt_commethod(6)
    def AddFile(self, file: Windows.Storage.IStorageFile) -> WinRT_String: ...
    @winrt_commethod(7)
    def RedeemTokenForFileAsync(self, token: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_commethod(8)
    def RemoveFile(self, token: WinRT_String) -> Void: ...
class IStandardDataFormatsStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7ed681a1-a880-40c9-b4-ed-0b-ee-1e-15-f5-49')
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
class IStandardDataFormatsStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('42a254f4-9d76-42e8-86-1b-47-c2-5d-d0-cf-71')
    @winrt_commethod(6)
    def get_WebLink(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ApplicationLink(self) -> WinRT_String: ...
    WebLink = property(get_WebLink, None)
    ApplicationLink = property(get_ApplicationLink, None)
class IStandardDataFormatsStatics3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3b57b069-01d4-474c-8b-5f-bc-8e-27-f3-8b-21')
    @winrt_commethod(6)
    def get_UserActivityJsonArray(self) -> WinRT_String: ...
    UserActivityJsonArray = property(get_UserActivityJsonArray, None)
class ITargetApplicationChosenEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ca6fb8ac-2987-4ee3-9c-54-d8-af-bc-b8-6c-1d')
    @winrt_commethod(6)
    def get_ApplicationName(self) -> WinRT_String: ...
    ApplicationName = property(get_ApplicationName, None)
class OperationCompletedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.DataTransfer.OperationCompletedEventArgs'
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
class ShareCompletedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.DataTransfer.ShareCompletedEventArgs'
    @winrt_mixinmethod
    def get_ShareTarget(self: Windows.ApplicationModel.DataTransfer.IShareCompletedEventArgs) -> Windows.ApplicationModel.DataTransfer.ShareTargetInfo: ...
    ShareTarget = property(get_ShareTarget, None)
class ShareProvider(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.DataTransfer.ShareProvider'
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
class ShareProviderHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e7f9d9ba-e1ba-4e4d-bd-65-d4-38-45-d3-21-2f')
    ClassId = 'Windows.ApplicationModel.DataTransfer.ShareProviderHandler'
    @winrt_commethod(3)
    def Invoke(self, operation: Windows.ApplicationModel.DataTransfer.ShareProviderOperation) -> Void: ...
class ShareProviderOperation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.DataTransfer.ShareProviderOperation'
    @winrt_mixinmethod
    def get_Data(self: Windows.ApplicationModel.DataTransfer.IShareProviderOperation) -> Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_mixinmethod
    def get_Provider(self: Windows.ApplicationModel.DataTransfer.IShareProviderOperation) -> Windows.ApplicationModel.DataTransfer.ShareProvider: ...
    @winrt_mixinmethod
    def ReportCompleted(self: Windows.ApplicationModel.DataTransfer.IShareProviderOperation) -> Void: ...
    Data = property(get_Data, None)
    Provider = property(get_Provider, None)
class ShareProvidersRequestedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.DataTransfer.ShareProvidersRequestedEventArgs'
    @winrt_mixinmethod
    def get_Providers(self: Windows.ApplicationModel.DataTransfer.IShareProvidersRequestedEventArgs) -> Windows.Foundation.Collections.IVector[Windows.ApplicationModel.DataTransfer.ShareProvider]: ...
    @winrt_mixinmethod
    def get_Data(self: Windows.ApplicationModel.DataTransfer.IShareProvidersRequestedEventArgs) -> Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.DataTransfer.IShareProvidersRequestedEventArgs) -> Windows.Foundation.Deferral: ...
    Providers = property(get_Providers, None)
    Data = property(get_Data, None)
class ShareTargetInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.DataTransfer.ShareTargetInfo'
    @winrt_mixinmethod
    def get_AppUserModelId(self: Windows.ApplicationModel.DataTransfer.IShareTargetInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ShareProvider(self: Windows.ApplicationModel.DataTransfer.IShareTargetInfo) -> Windows.ApplicationModel.DataTransfer.ShareProvider: ...
    AppUserModelId = property(get_AppUserModelId, None)
    ShareProvider = property(get_ShareProvider, None)
class ShareUIOptions(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.DataTransfer.ShareUIOptions'
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
class SharedStorageAccessManager(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.DataTransfer.SharedStorageAccessManager'
    @winrt_classmethod
    def AddFile(cls: Windows.ApplicationModel.DataTransfer.ISharedStorageAccessManagerStatics, file: Windows.Storage.IStorageFile) -> WinRT_String: ...
    @winrt_classmethod
    def RedeemTokenForFileAsync(cls: Windows.ApplicationModel.DataTransfer.ISharedStorageAccessManagerStatics, token: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Storage.StorageFile]: ...
    @winrt_classmethod
    def RemoveFile(cls: Windows.ApplicationModel.DataTransfer.ISharedStorageAccessManagerStatics, token: WinRT_String) -> Void: ...
class StandardDataFormats(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.DataTransfer.StandardDataFormats'
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
class TargetApplicationChosenEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.DataTransfer.TargetApplicationChosenEventArgs'
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
