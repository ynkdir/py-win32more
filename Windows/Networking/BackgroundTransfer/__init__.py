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
import Windows.ApplicationModel.Background
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Networking.BackgroundTransfer
import Windows.Security.Credentials
import Windows.Storage
import Windows.Storage.Streams
import Windows.UI.Notifications
import Windows.Web
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class BackgroundDownloadProgress(EasyCastStructure):
    BytesReceived: UInt64
    TotalBytesToReceive: UInt64
    Status: Windows.Networking.BackgroundTransfer.BackgroundTransferStatus
    HasResponseChanged: Boolean
    HasRestarted: Boolean
class BackgroundDownloader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.BackgroundTransfer.IBackgroundDownloader
    _classid_ = 'Windows.Networking.BackgroundTransfer.BackgroundDownloader'
    @winrt_factorymethod
    def CreateWithCompletionGroup(cls: Windows.Networking.BackgroundTransfer.IBackgroundDownloaderFactory, completionGroup: Windows.Networking.BackgroundTransfer.BackgroundTransferCompletionGroup) -> Windows.Networking.BackgroundTransfer.BackgroundDownloader: ...
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Networking.BackgroundTransfer.BackgroundDownloader: ...
    @winrt_mixinmethod
    def CreateDownload(self: Windows.Networking.BackgroundTransfer.IBackgroundDownloader, uri: Windows.Foundation.Uri, resultFile: Windows.Storage.IStorageFile) -> Windows.Networking.BackgroundTransfer.DownloadOperation: ...
    @winrt_mixinmethod
    def CreateDownloadFromFile(self: Windows.Networking.BackgroundTransfer.IBackgroundDownloader, uri: Windows.Foundation.Uri, resultFile: Windows.Storage.IStorageFile, requestBodyFile: Windows.Storage.IStorageFile) -> Windows.Networking.BackgroundTransfer.DownloadOperation: ...
    @winrt_mixinmethod
    def CreateDownloadAsync(self: Windows.Networking.BackgroundTransfer.IBackgroundDownloader, uri: Windows.Foundation.Uri, resultFile: Windows.Storage.IStorageFile, requestBodyStream: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncOperation[Windows.Networking.BackgroundTransfer.DownloadOperation]: ...
    @winrt_mixinmethod
    def SetRequestHeader(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferBase, headerName: WinRT_String, headerValue: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ServerCredential(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferBase) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ServerCredential(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferBase, credential: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_ProxyCredential(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferBase) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ProxyCredential(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferBase, credential: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_Method(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferBase) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Method(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferBase, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Group(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferBase) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Group(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferBase, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CostPolicy(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferBase) -> Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy: ...
    @winrt_mixinmethod
    def put_CostPolicy(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferBase, value: Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy) -> Void: ...
    @winrt_mixinmethod
    def get_TransferGroup(self: Windows.Networking.BackgroundTransfer.IBackgroundDownloader2) -> Windows.Networking.BackgroundTransfer.BackgroundTransferGroup: ...
    @winrt_mixinmethod
    def put_TransferGroup(self: Windows.Networking.BackgroundTransfer.IBackgroundDownloader2, value: Windows.Networking.BackgroundTransfer.BackgroundTransferGroup) -> Void: ...
    @winrt_mixinmethod
    def get_SuccessToastNotification(self: Windows.Networking.BackgroundTransfer.IBackgroundDownloader2) -> Windows.UI.Notifications.ToastNotification: ...
    @winrt_mixinmethod
    def put_SuccessToastNotification(self: Windows.Networking.BackgroundTransfer.IBackgroundDownloader2, value: Windows.UI.Notifications.ToastNotification) -> Void: ...
    @winrt_mixinmethod
    def get_FailureToastNotification(self: Windows.Networking.BackgroundTransfer.IBackgroundDownloader2) -> Windows.UI.Notifications.ToastNotification: ...
    @winrt_mixinmethod
    def put_FailureToastNotification(self: Windows.Networking.BackgroundTransfer.IBackgroundDownloader2, value: Windows.UI.Notifications.ToastNotification) -> Void: ...
    @winrt_mixinmethod
    def get_SuccessTileNotification(self: Windows.Networking.BackgroundTransfer.IBackgroundDownloader2) -> Windows.UI.Notifications.TileNotification: ...
    @winrt_mixinmethod
    def put_SuccessTileNotification(self: Windows.Networking.BackgroundTransfer.IBackgroundDownloader2, value: Windows.UI.Notifications.TileNotification) -> Void: ...
    @winrt_mixinmethod
    def get_FailureTileNotification(self: Windows.Networking.BackgroundTransfer.IBackgroundDownloader2) -> Windows.UI.Notifications.TileNotification: ...
    @winrt_mixinmethod
    def put_FailureTileNotification(self: Windows.Networking.BackgroundTransfer.IBackgroundDownloader2, value: Windows.UI.Notifications.TileNotification) -> Void: ...
    @winrt_mixinmethod
    def get_CompletionGroup(self: Windows.Networking.BackgroundTransfer.IBackgroundDownloader3) -> Windows.Networking.BackgroundTransfer.BackgroundTransferCompletionGroup: ...
    @winrt_classmethod
    def GetCurrentDownloadsForTransferGroupAsync(cls: Windows.Networking.BackgroundTransfer.IBackgroundDownloaderStaticMethods2, group: Windows.Networking.BackgroundTransfer.BackgroundTransferGroup) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.BackgroundTransfer.DownloadOperation]]: ...
    @winrt_classmethod
    def RequestUnconstrainedDownloadsAsync(cls: Windows.Networking.BackgroundTransfer.IBackgroundDownloaderUserConsent, operations: Windows.Foundation.Collections.IIterable[Windows.Networking.BackgroundTransfer.DownloadOperation]) -> Windows.Foundation.IAsyncOperation[Windows.Networking.BackgroundTransfer.UnconstrainedTransferRequestResult]: ...
    @winrt_classmethod
    def GetCurrentDownloadsAsync(cls: Windows.Networking.BackgroundTransfer.IBackgroundDownloaderStaticMethods) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.BackgroundTransfer.DownloadOperation]]: ...
    @winrt_classmethod
    def GetCurrentDownloadsForGroupAsync(cls: Windows.Networking.BackgroundTransfer.IBackgroundDownloaderStaticMethods, group: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.BackgroundTransfer.DownloadOperation]]: ...
    ServerCredential = property(get_ServerCredential, put_ServerCredential)
    ProxyCredential = property(get_ProxyCredential, put_ProxyCredential)
    Method = property(get_Method, put_Method)
    Group = property(get_Group, put_Group)
    CostPolicy = property(get_CostPolicy, put_CostPolicy)
    TransferGroup = property(get_TransferGroup, put_TransferGroup)
    SuccessToastNotification = property(get_SuccessToastNotification, put_SuccessToastNotification)
    FailureToastNotification = property(get_FailureToastNotification, put_FailureToastNotification)
    SuccessTileNotification = property(get_SuccessTileNotification, put_SuccessTileNotification)
    FailureTileNotification = property(get_FailureTileNotification, put_FailureTileNotification)
    CompletionGroup = property(get_CompletionGroup, None)
BackgroundTransferBehavior = Int32
BackgroundTransferBehavior_Parallel: BackgroundTransferBehavior = 0
BackgroundTransferBehavior_Serialized: BackgroundTransferBehavior = 1
class BackgroundTransferCompletionGroup(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.BackgroundTransfer.IBackgroundTransferCompletionGroup
    _classid_ = 'Windows.Networking.BackgroundTransfer.BackgroundTransferCompletionGroup'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Networking.BackgroundTransfer.BackgroundTransferCompletionGroup: ...
    @winrt_mixinmethod
    def get_Trigger(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferCompletionGroup) -> Windows.ApplicationModel.Background.IBackgroundTrigger: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferCompletionGroup) -> Boolean: ...
    @winrt_mixinmethod
    def Enable(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferCompletionGroup) -> Void: ...
    Trigger = property(get_Trigger, None)
    IsEnabled = property(get_IsEnabled, None)
class BackgroundTransferCompletionGroupTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.BackgroundTransfer.IBackgroundTransferCompletionGroupTriggerDetails
    _classid_ = 'Windows.Networking.BackgroundTransfer.BackgroundTransferCompletionGroupTriggerDetails'
    @winrt_mixinmethod
    def get_Downloads(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferCompletionGroupTriggerDetails) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.BackgroundTransfer.DownloadOperation]: ...
    @winrt_mixinmethod
    def get_Uploads(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferCompletionGroupTriggerDetails) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.BackgroundTransfer.UploadOperation]: ...
    Downloads = property(get_Downloads, None)
    Uploads = property(get_Uploads, None)
class BackgroundTransferContentPart(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.BackgroundTransfer.IBackgroundTransferContentPart
    _classid_ = 'Windows.Networking.BackgroundTransfer.BackgroundTransferContentPart'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Networking.BackgroundTransfer.BackgroundTransferContentPart: ...
    @winrt_factorymethod
    def CreateWithName(cls: Windows.Networking.BackgroundTransfer.IBackgroundTransferContentPartFactory, name: WinRT_String) -> Windows.Networking.BackgroundTransfer.BackgroundTransferContentPart: ...
    @winrt_factorymethod
    def CreateWithNameAndFileName(cls: Windows.Networking.BackgroundTransfer.IBackgroundTransferContentPartFactory, name: WinRT_String, fileName: WinRT_String) -> Windows.Networking.BackgroundTransfer.BackgroundTransferContentPart: ...
    @winrt_mixinmethod
    def SetHeader(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferContentPart, headerName: WinRT_String, headerValue: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def SetText(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferContentPart, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def SetFile(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferContentPart, value: Windows.Storage.IStorageFile) -> Void: ...
BackgroundTransferCostPolicy = Int32
BackgroundTransferCostPolicy_Default: BackgroundTransferCostPolicy = 0
BackgroundTransferCostPolicy_UnrestrictedOnly: BackgroundTransferCostPolicy = 1
BackgroundTransferCostPolicy_Always: BackgroundTransferCostPolicy = 2
class BackgroundTransferError(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.BackgroundTransferError'
    @winrt_classmethod
    def GetStatus(cls: Windows.Networking.BackgroundTransfer.IBackgroundTransferErrorStaticMethods, hresult: Int32) -> Windows.Web.WebErrorStatus: ...
class BackgroundTransferFileRange(EasyCastStructure):
    Offset: UInt64
    Length: UInt64
class BackgroundTransferGroup(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.BackgroundTransfer.IBackgroundTransferGroup
    _classid_ = 'Windows.Networking.BackgroundTransfer.BackgroundTransferGroup'
    @winrt_mixinmethod
    def get_Name(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferGroup) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TransferBehavior(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferGroup) -> Windows.Networking.BackgroundTransfer.BackgroundTransferBehavior: ...
    @winrt_mixinmethod
    def put_TransferBehavior(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferGroup, value: Windows.Networking.BackgroundTransfer.BackgroundTransferBehavior) -> Void: ...
    @winrt_classmethod
    def CreateGroup(cls: Windows.Networking.BackgroundTransfer.IBackgroundTransferGroupStatics, name: WinRT_String) -> Windows.Networking.BackgroundTransfer.BackgroundTransferGroup: ...
    Name = property(get_Name, None)
    TransferBehavior = property(get_TransferBehavior, put_TransferBehavior)
BackgroundTransferPriority = Int32
BackgroundTransferPriority_Default: BackgroundTransferPriority = 0
BackgroundTransferPriority_High: BackgroundTransferPriority = 1
BackgroundTransferPriority_Low: BackgroundTransferPriority = 2
class BackgroundTransferRangesDownloadedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.BackgroundTransfer.IBackgroundTransferRangesDownloadedEventArgs
    _classid_ = 'Windows.Networking.BackgroundTransfer.BackgroundTransferRangesDownloadedEventArgs'
    @winrt_mixinmethod
    def get_WasDownloadRestarted(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferRangesDownloadedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_AddedRanges(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferRangesDownloadedEventArgs) -> Windows.Foundation.Collections.IVector[Windows.Networking.BackgroundTransfer.BackgroundTransferFileRange]: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferRangesDownloadedEventArgs) -> Windows.Foundation.Deferral: ...
    WasDownloadRestarted = property(get_WasDownloadRestarted, None)
    AddedRanges = property(get_AddedRanges, None)
BackgroundTransferStatus = Int32
BackgroundTransferStatus_Idle: BackgroundTransferStatus = 0
BackgroundTransferStatus_Running: BackgroundTransferStatus = 1
BackgroundTransferStatus_PausedByApplication: BackgroundTransferStatus = 2
BackgroundTransferStatus_PausedCostedNetwork: BackgroundTransferStatus = 3
BackgroundTransferStatus_PausedNoNetwork: BackgroundTransferStatus = 4
BackgroundTransferStatus_Completed: BackgroundTransferStatus = 5
BackgroundTransferStatus_Canceled: BackgroundTransferStatus = 6
BackgroundTransferStatus_Error: BackgroundTransferStatus = 7
BackgroundTransferStatus_PausedRecoverableWebErrorStatus: BackgroundTransferStatus = 8
BackgroundTransferStatus_PausedSystemPolicy: BackgroundTransferStatus = 32
class BackgroundUploadProgress(EasyCastStructure):
    BytesReceived: UInt64
    BytesSent: UInt64
    TotalBytesToReceive: UInt64
    TotalBytesToSend: UInt64
    Status: Windows.Networking.BackgroundTransfer.BackgroundTransferStatus
    HasResponseChanged: Boolean
    HasRestarted: Boolean
class BackgroundUploader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.BackgroundTransfer.IBackgroundUploader
    _classid_ = 'Windows.Networking.BackgroundTransfer.BackgroundUploader'
    @winrt_factorymethod
    def CreateWithCompletionGroup(cls: Windows.Networking.BackgroundTransfer.IBackgroundUploaderFactory, completionGroup: Windows.Networking.BackgroundTransfer.BackgroundTransferCompletionGroup) -> Windows.Networking.BackgroundTransfer.BackgroundUploader: ...
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Networking.BackgroundTransfer.BackgroundUploader: ...
    @winrt_mixinmethod
    def CreateUpload(self: Windows.Networking.BackgroundTransfer.IBackgroundUploader, uri: Windows.Foundation.Uri, sourceFile: Windows.Storage.IStorageFile) -> Windows.Networking.BackgroundTransfer.UploadOperation: ...
    @winrt_mixinmethod
    def CreateUploadFromStreamAsync(self: Windows.Networking.BackgroundTransfer.IBackgroundUploader, uri: Windows.Foundation.Uri, sourceStream: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncOperation[Windows.Networking.BackgroundTransfer.UploadOperation]: ...
    @winrt_mixinmethod
    def CreateUploadWithFormDataAndAutoBoundaryAsync(self: Windows.Networking.BackgroundTransfer.IBackgroundUploader, uri: Windows.Foundation.Uri, parts: Windows.Foundation.Collections.IIterable[Windows.Networking.BackgroundTransfer.BackgroundTransferContentPart]) -> Windows.Foundation.IAsyncOperation[Windows.Networking.BackgroundTransfer.UploadOperation]: ...
    @winrt_mixinmethod
    def CreateUploadWithSubTypeAsync(self: Windows.Networking.BackgroundTransfer.IBackgroundUploader, uri: Windows.Foundation.Uri, parts: Windows.Foundation.Collections.IIterable[Windows.Networking.BackgroundTransfer.BackgroundTransferContentPart], subType: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.BackgroundTransfer.UploadOperation]: ...
    @winrt_mixinmethod
    def CreateUploadWithSubTypeAndBoundaryAsync(self: Windows.Networking.BackgroundTransfer.IBackgroundUploader, uri: Windows.Foundation.Uri, parts: Windows.Foundation.Collections.IIterable[Windows.Networking.BackgroundTransfer.BackgroundTransferContentPart], subType: WinRT_String, boundary: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.BackgroundTransfer.UploadOperation]: ...
    @winrt_mixinmethod
    def SetRequestHeader(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferBase, headerName: WinRT_String, headerValue: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ServerCredential(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferBase) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ServerCredential(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferBase, credential: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_ProxyCredential(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferBase) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ProxyCredential(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferBase, credential: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_Method(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferBase) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Method(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferBase, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Group(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferBase) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Group(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferBase, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CostPolicy(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferBase) -> Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy: ...
    @winrt_mixinmethod
    def put_CostPolicy(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferBase, value: Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy) -> Void: ...
    @winrt_mixinmethod
    def get_TransferGroup(self: Windows.Networking.BackgroundTransfer.IBackgroundUploader2) -> Windows.Networking.BackgroundTransfer.BackgroundTransferGroup: ...
    @winrt_mixinmethod
    def put_TransferGroup(self: Windows.Networking.BackgroundTransfer.IBackgroundUploader2, value: Windows.Networking.BackgroundTransfer.BackgroundTransferGroup) -> Void: ...
    @winrt_mixinmethod
    def get_SuccessToastNotification(self: Windows.Networking.BackgroundTransfer.IBackgroundUploader2) -> Windows.UI.Notifications.ToastNotification: ...
    @winrt_mixinmethod
    def put_SuccessToastNotification(self: Windows.Networking.BackgroundTransfer.IBackgroundUploader2, value: Windows.UI.Notifications.ToastNotification) -> Void: ...
    @winrt_mixinmethod
    def get_FailureToastNotification(self: Windows.Networking.BackgroundTransfer.IBackgroundUploader2) -> Windows.UI.Notifications.ToastNotification: ...
    @winrt_mixinmethod
    def put_FailureToastNotification(self: Windows.Networking.BackgroundTransfer.IBackgroundUploader2, value: Windows.UI.Notifications.ToastNotification) -> Void: ...
    @winrt_mixinmethod
    def get_SuccessTileNotification(self: Windows.Networking.BackgroundTransfer.IBackgroundUploader2) -> Windows.UI.Notifications.TileNotification: ...
    @winrt_mixinmethod
    def put_SuccessTileNotification(self: Windows.Networking.BackgroundTransfer.IBackgroundUploader2, value: Windows.UI.Notifications.TileNotification) -> Void: ...
    @winrt_mixinmethod
    def get_FailureTileNotification(self: Windows.Networking.BackgroundTransfer.IBackgroundUploader2) -> Windows.UI.Notifications.TileNotification: ...
    @winrt_mixinmethod
    def put_FailureTileNotification(self: Windows.Networking.BackgroundTransfer.IBackgroundUploader2, value: Windows.UI.Notifications.TileNotification) -> Void: ...
    @winrt_mixinmethod
    def get_CompletionGroup(self: Windows.Networking.BackgroundTransfer.IBackgroundUploader3) -> Windows.Networking.BackgroundTransfer.BackgroundTransferCompletionGroup: ...
    @winrt_classmethod
    def GetCurrentUploadsForTransferGroupAsync(cls: Windows.Networking.BackgroundTransfer.IBackgroundUploaderStaticMethods2, group: Windows.Networking.BackgroundTransfer.BackgroundTransferGroup) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.BackgroundTransfer.UploadOperation]]: ...
    @winrt_classmethod
    def RequestUnconstrainedUploadsAsync(cls: Windows.Networking.BackgroundTransfer.IBackgroundUploaderUserConsent, operations: Windows.Foundation.Collections.IIterable[Windows.Networking.BackgroundTransfer.UploadOperation]) -> Windows.Foundation.IAsyncOperation[Windows.Networking.BackgroundTransfer.UnconstrainedTransferRequestResult]: ...
    @winrt_classmethod
    def GetCurrentUploadsAsync(cls: Windows.Networking.BackgroundTransfer.IBackgroundUploaderStaticMethods) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.BackgroundTransfer.UploadOperation]]: ...
    @winrt_classmethod
    def GetCurrentUploadsForGroupAsync(cls: Windows.Networking.BackgroundTransfer.IBackgroundUploaderStaticMethods, group: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.BackgroundTransfer.UploadOperation]]: ...
    ServerCredential = property(get_ServerCredential, put_ServerCredential)
    ProxyCredential = property(get_ProxyCredential, put_ProxyCredential)
    Method = property(get_Method, put_Method)
    Group = property(get_Group, put_Group)
    CostPolicy = property(get_CostPolicy, put_CostPolicy)
    TransferGroup = property(get_TransferGroup, put_TransferGroup)
    SuccessToastNotification = property(get_SuccessToastNotification, put_SuccessToastNotification)
    FailureToastNotification = property(get_FailureToastNotification, put_FailureToastNotification)
    SuccessTileNotification = property(get_SuccessTileNotification, put_SuccessTileNotification)
    FailureTileNotification = property(get_FailureTileNotification, put_FailureTileNotification)
    CompletionGroup = property(get_CompletionGroup, None)
class _ContentPrefetcher_Meta_(ComPtr.__class__):
    pass
class ContentPrefetcher(ComPtr, metaclass=_ContentPrefetcher_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.ContentPrefetcher'
    @winrt_classmethod
    def get_LastSuccessfulPrefetchTime(cls: Windows.Networking.BackgroundTransfer.IContentPrefetcherTime) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_classmethod
    def get_ContentUris(cls: Windows.Networking.BackgroundTransfer.IContentPrefetcher) -> Windows.Foundation.Collections.IVector[Windows.Foundation.Uri]: ...
    @winrt_classmethod
    def put_IndirectContentUri(cls: Windows.Networking.BackgroundTransfer.IContentPrefetcher, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_classmethod
    def get_IndirectContentUri(cls: Windows.Networking.BackgroundTransfer.IContentPrefetcher) -> Windows.Foundation.Uri: ...
    _ContentPrefetcher_Meta_.LastSuccessfulPrefetchTime = property(get_LastSuccessfulPrefetchTime.__wrapped__, None)
    _ContentPrefetcher_Meta_.ContentUris = property(get_ContentUris.__wrapped__, None)
    _ContentPrefetcher_Meta_.IndirectContentUri = property(get_IndirectContentUri.__wrapped__, put_IndirectContentUri.__wrapped__)
class DownloadOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.BackgroundTransfer.IDownloadOperation
    _classid_ = 'Windows.Networking.BackgroundTransfer.DownloadOperation'
    @winrt_mixinmethod
    def get_ResultFile(self: Windows.Networking.BackgroundTransfer.IDownloadOperation) -> Windows.Storage.IStorageFile: ...
    @winrt_mixinmethod
    def get_Progress(self: Windows.Networking.BackgroundTransfer.IDownloadOperation) -> Windows.Networking.BackgroundTransfer.BackgroundDownloadProgress: ...
    @winrt_mixinmethod
    def StartAsync(self: Windows.Networking.BackgroundTransfer.IDownloadOperation) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Networking.BackgroundTransfer.DownloadOperation, Windows.Networking.BackgroundTransfer.DownloadOperation]: ...
    @winrt_mixinmethod
    def AttachAsync(self: Windows.Networking.BackgroundTransfer.IDownloadOperation) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Networking.BackgroundTransfer.DownloadOperation, Windows.Networking.BackgroundTransfer.DownloadOperation]: ...
    @winrt_mixinmethod
    def Pause(self: Windows.Networking.BackgroundTransfer.IDownloadOperation) -> Void: ...
    @winrt_mixinmethod
    def Resume(self: Windows.Networking.BackgroundTransfer.IDownloadOperation) -> Void: ...
    @winrt_mixinmethod
    def get_Guid(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation) -> Guid: ...
    @winrt_mixinmethod
    def get_RequestedUri(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Method(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Group(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CostPolicy(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation) -> Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy: ...
    @winrt_mixinmethod
    def put_CostPolicy(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation, value: Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy) -> Void: ...
    @winrt_mixinmethod
    def GetResultStreamAt(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation, position: UInt64) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def GetResponseInformation(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation) -> Windows.Networking.BackgroundTransfer.ResponseInformation: ...
    @winrt_mixinmethod
    def get_Priority(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferOperationPriority) -> Windows.Networking.BackgroundTransfer.BackgroundTransferPriority: ...
    @winrt_mixinmethod
    def put_Priority(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferOperationPriority, value: Windows.Networking.BackgroundTransfer.BackgroundTransferPriority) -> Void: ...
    @winrt_mixinmethod
    def get_TransferGroup(self: Windows.Networking.BackgroundTransfer.IDownloadOperation2) -> Windows.Networking.BackgroundTransfer.BackgroundTransferGroup: ...
    @winrt_mixinmethod
    def get_IsRandomAccessRequired(self: Windows.Networking.BackgroundTransfer.IDownloadOperation3) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsRandomAccessRequired(self: Windows.Networking.BackgroundTransfer.IDownloadOperation3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetResultRandomAccessStreamReference(self: Windows.Networking.BackgroundTransfer.IDownloadOperation3) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def GetDownloadedRanges(self: Windows.Networking.BackgroundTransfer.IDownloadOperation3) -> Windows.Foundation.Collections.IVector[Windows.Networking.BackgroundTransfer.BackgroundTransferFileRange]: ...
    @winrt_mixinmethod
    def add_RangesDownloaded(self: Windows.Networking.BackgroundTransfer.IDownloadOperation3, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.BackgroundTransfer.DownloadOperation, Windows.Networking.BackgroundTransfer.BackgroundTransferRangesDownloadedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RangesDownloaded(self: Windows.Networking.BackgroundTransfer.IDownloadOperation3, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def put_RequestedUri(self: Windows.Networking.BackgroundTransfer.IDownloadOperation3, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_RecoverableWebErrorStatuses(self: Windows.Networking.BackgroundTransfer.IDownloadOperation3) -> Windows.Foundation.Collections.IVector[Windows.Web.WebErrorStatus]: ...
    @winrt_mixinmethod
    def get_CurrentWebErrorStatus(self: Windows.Networking.BackgroundTransfer.IDownloadOperation3) -> Windows.Foundation.IReference[Windows.Web.WebErrorStatus]: ...
    @winrt_mixinmethod
    def MakeCurrentInTransferGroup(self: Windows.Networking.BackgroundTransfer.IDownloadOperation4) -> Void: ...
    @winrt_mixinmethod
    def SetRequestHeader(self: Windows.Networking.BackgroundTransfer.IDownloadOperation5, headerName: WinRT_String, headerValue: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def RemoveRequestHeader(self: Windows.Networking.BackgroundTransfer.IDownloadOperation5, headerName: WinRT_String) -> Void: ...
    ResultFile = property(get_ResultFile, None)
    Progress = property(get_Progress, None)
    Guid = property(get_Guid, None)
    RequestedUri = property(get_RequestedUri, put_RequestedUri)
    Method = property(get_Method, None)
    Group = property(get_Group, None)
    CostPolicy = property(get_CostPolicy, put_CostPolicy)
    Priority = property(get_Priority, put_Priority)
    TransferGroup = property(get_TransferGroup, None)
    IsRandomAccessRequired = property(get_IsRandomAccessRequired, put_IsRandomAccessRequired)
    RecoverableWebErrorStatuses = property(get_RecoverableWebErrorStatuses, None)
    CurrentWebErrorStatus = property(get_CurrentWebErrorStatus, None)
class IBackgroundDownloader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundDownloader'
    _iid_ = Guid('{c1c79333-6649-4b1d-a826-a4b3dd234d0b}')
    @winrt_commethod(6)
    def CreateDownload(self, uri: Windows.Foundation.Uri, resultFile: Windows.Storage.IStorageFile) -> Windows.Networking.BackgroundTransfer.DownloadOperation: ...
    @winrt_commethod(7)
    def CreateDownloadFromFile(self, uri: Windows.Foundation.Uri, resultFile: Windows.Storage.IStorageFile, requestBodyFile: Windows.Storage.IStorageFile) -> Windows.Networking.BackgroundTransfer.DownloadOperation: ...
    @winrt_commethod(8)
    def CreateDownloadAsync(self, uri: Windows.Foundation.Uri, resultFile: Windows.Storage.IStorageFile, requestBodyStream: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncOperation[Windows.Networking.BackgroundTransfer.DownloadOperation]: ...
class IBackgroundDownloader2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundDownloader2'
    _iid_ = Guid('{a94a5847-348d-4a35-890e-8a1ef3798479}')
    @winrt_commethod(6)
    def get_TransferGroup(self) -> Windows.Networking.BackgroundTransfer.BackgroundTransferGroup: ...
    @winrt_commethod(7)
    def put_TransferGroup(self, value: Windows.Networking.BackgroundTransfer.BackgroundTransferGroup) -> Void: ...
    @winrt_commethod(8)
    def get_SuccessToastNotification(self) -> Windows.UI.Notifications.ToastNotification: ...
    @winrt_commethod(9)
    def put_SuccessToastNotification(self, value: Windows.UI.Notifications.ToastNotification) -> Void: ...
    @winrt_commethod(10)
    def get_FailureToastNotification(self) -> Windows.UI.Notifications.ToastNotification: ...
    @winrt_commethod(11)
    def put_FailureToastNotification(self, value: Windows.UI.Notifications.ToastNotification) -> Void: ...
    @winrt_commethod(12)
    def get_SuccessTileNotification(self) -> Windows.UI.Notifications.TileNotification: ...
    @winrt_commethod(13)
    def put_SuccessTileNotification(self, value: Windows.UI.Notifications.TileNotification) -> Void: ...
    @winrt_commethod(14)
    def get_FailureTileNotification(self) -> Windows.UI.Notifications.TileNotification: ...
    @winrt_commethod(15)
    def put_FailureTileNotification(self, value: Windows.UI.Notifications.TileNotification) -> Void: ...
    TransferGroup = property(get_TransferGroup, put_TransferGroup)
    SuccessToastNotification = property(get_SuccessToastNotification, put_SuccessToastNotification)
    FailureToastNotification = property(get_FailureToastNotification, put_FailureToastNotification)
    SuccessTileNotification = property(get_SuccessTileNotification, put_SuccessTileNotification)
    FailureTileNotification = property(get_FailureTileNotification, put_FailureTileNotification)
class IBackgroundDownloader3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundDownloader3'
    _iid_ = Guid('{d11a8c48-86e8-48e2-b615-6976aabf861d}')
    @winrt_commethod(6)
    def get_CompletionGroup(self) -> Windows.Networking.BackgroundTransfer.BackgroundTransferCompletionGroup: ...
    CompletionGroup = property(get_CompletionGroup, None)
class IBackgroundDownloaderFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundDownloaderFactory'
    _iid_ = Guid('{26836c24-d89e-46f4-a29a-4f4d4f144155}')
    @winrt_commethod(6)
    def CreateWithCompletionGroup(self, completionGroup: Windows.Networking.BackgroundTransfer.BackgroundTransferCompletionGroup) -> Windows.Networking.BackgroundTransfer.BackgroundDownloader: ...
class IBackgroundDownloaderStaticMethods(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundDownloaderStaticMethods'
    _iid_ = Guid('{52a65a35-c64e-426c-9919-540d0d21a650}')
    @winrt_commethod(6)
    def GetCurrentDownloadsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.BackgroundTransfer.DownloadOperation]]: ...
    @winrt_commethod(7)
    def GetCurrentDownloadsForGroupAsync(self, group: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.BackgroundTransfer.DownloadOperation]]: ...
class IBackgroundDownloaderStaticMethods2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundDownloaderStaticMethods2'
    _iid_ = Guid('{2faa1327-1ad4-4ca5-b2cd-08dbf0746afe}')
    @winrt_commethod(6)
    def GetCurrentDownloadsForTransferGroupAsync(self, group: Windows.Networking.BackgroundTransfer.BackgroundTransferGroup) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.BackgroundTransfer.DownloadOperation]]: ...
class IBackgroundDownloaderUserConsent(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundDownloaderUserConsent'
    _iid_ = Guid('{5d14e906-9266-4808-bd71-5925f2a3130a}')
    @winrt_commethod(6)
    def RequestUnconstrainedDownloadsAsync(self, operations: Windows.Foundation.Collections.IIterable[Windows.Networking.BackgroundTransfer.DownloadOperation]) -> Windows.Foundation.IAsyncOperation[Windows.Networking.BackgroundTransfer.UnconstrainedTransferRequestResult]: ...
class IBackgroundTransferBase(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundTransferBase'
    _iid_ = Guid('{2a9da250-c769-458c-afe8-feb8d4d3b2ef}')
    @winrt_commethod(6)
    def SetRequestHeader(self, headerName: WinRT_String, headerValue: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_ServerCredential(self) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(8)
    def put_ServerCredential(self, credential: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_commethod(9)
    def get_ProxyCredential(self) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(10)
    def put_ProxyCredential(self, credential: Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_commethod(11)
    def get_Method(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_Method(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def get_Group(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_Group(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_CostPolicy(self) -> Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy: ...
    @winrt_commethod(16)
    def put_CostPolicy(self, value: Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy) -> Void: ...
    ServerCredential = property(get_ServerCredential, put_ServerCredential)
    ProxyCredential = property(get_ProxyCredential, put_ProxyCredential)
    Method = property(get_Method, put_Method)
    Group = property(get_Group, put_Group)
    CostPolicy = property(get_CostPolicy, put_CostPolicy)
class IBackgroundTransferCompletionGroup(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundTransferCompletionGroup'
    _iid_ = Guid('{2d930225-986b-574d-7950-0add47f5d706}')
    @winrt_commethod(6)
    def get_Trigger(self) -> Windows.ApplicationModel.Background.IBackgroundTrigger: ...
    @winrt_commethod(7)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def Enable(self) -> Void: ...
    Trigger = property(get_Trigger, None)
    IsEnabled = property(get_IsEnabled, None)
class IBackgroundTransferCompletionGroupTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundTransferCompletionGroupTriggerDetails'
    _iid_ = Guid('{7b6be286-6e47-5136-7fcb-fa4389f46f5b}')
    @winrt_commethod(6)
    def get_Downloads(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.BackgroundTransfer.DownloadOperation]: ...
    @winrt_commethod(7)
    def get_Uploads(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.BackgroundTransfer.UploadOperation]: ...
    Downloads = property(get_Downloads, None)
    Uploads = property(get_Uploads, None)
class IBackgroundTransferContentPart(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundTransferContentPart'
    _iid_ = Guid('{e8e15657-d7d1-4ed8-838e-674ac217ace6}')
    @winrt_commethod(6)
    def SetHeader(self, headerName: WinRT_String, headerValue: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def SetText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def SetFile(self, value: Windows.Storage.IStorageFile) -> Void: ...
class IBackgroundTransferContentPartFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundTransferContentPartFactory'
    _iid_ = Guid('{90ef98a9-7a01-4a0b-9f80-a0b0bb370f8d}')
    @winrt_commethod(6)
    def CreateWithName(self, name: WinRT_String) -> Windows.Networking.BackgroundTransfer.BackgroundTransferContentPart: ...
    @winrt_commethod(7)
    def CreateWithNameAndFileName(self, name: WinRT_String, fileName: WinRT_String) -> Windows.Networking.BackgroundTransfer.BackgroundTransferContentPart: ...
class IBackgroundTransferErrorStaticMethods(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundTransferErrorStaticMethods'
    _iid_ = Guid('{aad33b04-1192-4bf4-8b68-39c5add244e2}')
    @winrt_commethod(6)
    def GetStatus(self, hresult: Int32) -> Windows.Web.WebErrorStatus: ...
class IBackgroundTransferGroup(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundTransferGroup'
    _iid_ = Guid('{d8c3e3e4-6459-4540-85eb-aaa1c8903677}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_TransferBehavior(self) -> Windows.Networking.BackgroundTransfer.BackgroundTransferBehavior: ...
    @winrt_commethod(8)
    def put_TransferBehavior(self, value: Windows.Networking.BackgroundTransfer.BackgroundTransferBehavior) -> Void: ...
    Name = property(get_Name, None)
    TransferBehavior = property(get_TransferBehavior, put_TransferBehavior)
class IBackgroundTransferGroupStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundTransferGroupStatics'
    _iid_ = Guid('{02ec50b2-7d18-495b-aa22-32a97d45d3e2}')
    @winrt_commethod(6)
    def CreateGroup(self, name: WinRT_String) -> Windows.Networking.BackgroundTransfer.BackgroundTransferGroup: ...
class IBackgroundTransferOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation'
    _iid_ = Guid('{ded06846-90ca-44fb-8fb1-124154c0d539}')
    @winrt_commethod(6)
    def get_Guid(self) -> Guid: ...
    @winrt_commethod(7)
    def get_RequestedUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_Method(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Group(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_CostPolicy(self) -> Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy: ...
    @winrt_commethod(11)
    def put_CostPolicy(self, value: Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy) -> Void: ...
    @winrt_commethod(12)
    def GetResultStreamAt(self, position: UInt64) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_commethod(13)
    def GetResponseInformation(self) -> Windows.Networking.BackgroundTransfer.ResponseInformation: ...
    Guid = property(get_Guid, None)
    RequestedUri = property(get_RequestedUri, None)
    Method = property(get_Method, None)
    Group = property(get_Group, None)
    CostPolicy = property(get_CostPolicy, put_CostPolicy)
class IBackgroundTransferOperationPriority(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundTransferOperationPriority'
    _iid_ = Guid('{04854327-5254-4b3a-915e-0aa49275c0f9}')
    @winrt_commethod(6)
    def get_Priority(self) -> Windows.Networking.BackgroundTransfer.BackgroundTransferPriority: ...
    @winrt_commethod(7)
    def put_Priority(self, value: Windows.Networking.BackgroundTransfer.BackgroundTransferPriority) -> Void: ...
    Priority = property(get_Priority, put_Priority)
class IBackgroundTransferRangesDownloadedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundTransferRangesDownloadedEventArgs'
    _iid_ = Guid('{3ebc7453-bf48-4a88-9248-b0c165184f5c}')
    @winrt_commethod(6)
    def get_WasDownloadRestarted(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_AddedRanges(self) -> Windows.Foundation.Collections.IVector[Windows.Networking.BackgroundTransfer.BackgroundTransferFileRange]: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    WasDownloadRestarted = property(get_WasDownloadRestarted, None)
    AddedRanges = property(get_AddedRanges, None)
class IBackgroundUploader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundUploader'
    _iid_ = Guid('{c595c9ae-cead-465b-8801-c55ac90a01ce}')
    @winrt_commethod(6)
    def CreateUpload(self, uri: Windows.Foundation.Uri, sourceFile: Windows.Storage.IStorageFile) -> Windows.Networking.BackgroundTransfer.UploadOperation: ...
    @winrt_commethod(7)
    def CreateUploadFromStreamAsync(self, uri: Windows.Foundation.Uri, sourceStream: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncOperation[Windows.Networking.BackgroundTransfer.UploadOperation]: ...
    @winrt_commethod(8)
    def CreateUploadWithFormDataAndAutoBoundaryAsync(self, uri: Windows.Foundation.Uri, parts: Windows.Foundation.Collections.IIterable[Windows.Networking.BackgroundTransfer.BackgroundTransferContentPart]) -> Windows.Foundation.IAsyncOperation[Windows.Networking.BackgroundTransfer.UploadOperation]: ...
    @winrt_commethod(9)
    def CreateUploadWithSubTypeAsync(self, uri: Windows.Foundation.Uri, parts: Windows.Foundation.Collections.IIterable[Windows.Networking.BackgroundTransfer.BackgroundTransferContentPart], subType: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.BackgroundTransfer.UploadOperation]: ...
    @winrt_commethod(10)
    def CreateUploadWithSubTypeAndBoundaryAsync(self, uri: Windows.Foundation.Uri, parts: Windows.Foundation.Collections.IIterable[Windows.Networking.BackgroundTransfer.BackgroundTransferContentPart], subType: WinRT_String, boundary: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.BackgroundTransfer.UploadOperation]: ...
class IBackgroundUploader2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundUploader2'
    _iid_ = Guid('{8e0612ce-0c34-4463-807f-198a1b8bd4ad}')
    @winrt_commethod(6)
    def get_TransferGroup(self) -> Windows.Networking.BackgroundTransfer.BackgroundTransferGroup: ...
    @winrt_commethod(7)
    def put_TransferGroup(self, value: Windows.Networking.BackgroundTransfer.BackgroundTransferGroup) -> Void: ...
    @winrt_commethod(8)
    def get_SuccessToastNotification(self) -> Windows.UI.Notifications.ToastNotification: ...
    @winrt_commethod(9)
    def put_SuccessToastNotification(self, value: Windows.UI.Notifications.ToastNotification) -> Void: ...
    @winrt_commethod(10)
    def get_FailureToastNotification(self) -> Windows.UI.Notifications.ToastNotification: ...
    @winrt_commethod(11)
    def put_FailureToastNotification(self, value: Windows.UI.Notifications.ToastNotification) -> Void: ...
    @winrt_commethod(12)
    def get_SuccessTileNotification(self) -> Windows.UI.Notifications.TileNotification: ...
    @winrt_commethod(13)
    def put_SuccessTileNotification(self, value: Windows.UI.Notifications.TileNotification) -> Void: ...
    @winrt_commethod(14)
    def get_FailureTileNotification(self) -> Windows.UI.Notifications.TileNotification: ...
    @winrt_commethod(15)
    def put_FailureTileNotification(self, value: Windows.UI.Notifications.TileNotification) -> Void: ...
    TransferGroup = property(get_TransferGroup, put_TransferGroup)
    SuccessToastNotification = property(get_SuccessToastNotification, put_SuccessToastNotification)
    FailureToastNotification = property(get_FailureToastNotification, put_FailureToastNotification)
    SuccessTileNotification = property(get_SuccessTileNotification, put_SuccessTileNotification)
    FailureTileNotification = property(get_FailureTileNotification, put_FailureTileNotification)
class IBackgroundUploader3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundUploader3'
    _iid_ = Guid('{b95e9439-5bf0-4b3a-8c47-2c6199a854b9}')
    @winrt_commethod(6)
    def get_CompletionGroup(self) -> Windows.Networking.BackgroundTransfer.BackgroundTransferCompletionGroup: ...
    CompletionGroup = property(get_CompletionGroup, None)
class IBackgroundUploaderFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundUploaderFactory'
    _iid_ = Guid('{736203c7-10e7-48a0-ac3c-1ac71095ec57}')
    @winrt_commethod(6)
    def CreateWithCompletionGroup(self, completionGroup: Windows.Networking.BackgroundTransfer.BackgroundTransferCompletionGroup) -> Windows.Networking.BackgroundTransfer.BackgroundUploader: ...
class IBackgroundUploaderStaticMethods(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundUploaderStaticMethods'
    _iid_ = Guid('{f2875cfb-9b05-4741-9121-740a83e247df}')
    @winrt_commethod(6)
    def GetCurrentUploadsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.BackgroundTransfer.UploadOperation]]: ...
    @winrt_commethod(7)
    def GetCurrentUploadsForGroupAsync(self, group: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.BackgroundTransfer.UploadOperation]]: ...
class IBackgroundUploaderStaticMethods2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundUploaderStaticMethods2'
    _iid_ = Guid('{e919ac62-ea08-42f0-a2ac-07e467549080}')
    @winrt_commethod(6)
    def GetCurrentUploadsForTransferGroupAsync(self, group: Windows.Networking.BackgroundTransfer.BackgroundTransferGroup) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.BackgroundTransfer.UploadOperation]]: ...
class IBackgroundUploaderUserConsent(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundUploaderUserConsent'
    _iid_ = Guid('{3bb384cb-0760-461d-907f-5138f84d44c1}')
    @winrt_commethod(6)
    def RequestUnconstrainedUploadsAsync(self, operations: Windows.Foundation.Collections.IIterable[Windows.Networking.BackgroundTransfer.UploadOperation]) -> Windows.Foundation.IAsyncOperation[Windows.Networking.BackgroundTransfer.UnconstrainedTransferRequestResult]: ...
class IContentPrefetcher(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IContentPrefetcher'
    _iid_ = Guid('{a8d6f754-7dc1-4cd9-8810-2a6aa9417e11}')
    @winrt_commethod(6)
    def get_ContentUris(self) -> Windows.Foundation.Collections.IVector[Windows.Foundation.Uri]: ...
    @winrt_commethod(7)
    def put_IndirectContentUri(self, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def get_IndirectContentUri(self) -> Windows.Foundation.Uri: ...
    ContentUris = property(get_ContentUris, None)
    IndirectContentUri = property(get_IndirectContentUri, put_IndirectContentUri)
class IContentPrefetcherTime(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IContentPrefetcherTime'
    _iid_ = Guid('{e361fd08-132a-4fde-a7cc-fcb0e66523af}')
    @winrt_commethod(6)
    def get_LastSuccessfulPrefetchTime(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    LastSuccessfulPrefetchTime = property(get_LastSuccessfulPrefetchTime, None)
class IDownloadOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IDownloadOperation'
    _iid_ = Guid('{bd87ebb0-5714-4e09-ba68-bef73903b0d7}')
    @winrt_commethod(6)
    def get_ResultFile(self) -> Windows.Storage.IStorageFile: ...
    @winrt_commethod(7)
    def get_Progress(self) -> Windows.Networking.BackgroundTransfer.BackgroundDownloadProgress: ...
    @winrt_commethod(8)
    def StartAsync(self) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Networking.BackgroundTransfer.DownloadOperation, Windows.Networking.BackgroundTransfer.DownloadOperation]: ...
    @winrt_commethod(9)
    def AttachAsync(self) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Networking.BackgroundTransfer.DownloadOperation, Windows.Networking.BackgroundTransfer.DownloadOperation]: ...
    @winrt_commethod(10)
    def Pause(self) -> Void: ...
    @winrt_commethod(11)
    def Resume(self) -> Void: ...
    ResultFile = property(get_ResultFile, None)
    Progress = property(get_Progress, None)
class IDownloadOperation2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IDownloadOperation2'
    _iid_ = Guid('{a3cced40-8f9c-4353-9cd4-290dee387c38}')
    @winrt_commethod(6)
    def get_TransferGroup(self) -> Windows.Networking.BackgroundTransfer.BackgroundTransferGroup: ...
    TransferGroup = property(get_TransferGroup, None)
class IDownloadOperation3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IDownloadOperation3'
    _iid_ = Guid('{5027351c-7d5e-4adc-b8d3-df5c6031b9cc}')
    @winrt_commethod(6)
    def get_IsRandomAccessRequired(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsRandomAccessRequired(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def GetResultRandomAccessStreamReference(self) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(9)
    def GetDownloadedRanges(self) -> Windows.Foundation.Collections.IVector[Windows.Networking.BackgroundTransfer.BackgroundTransferFileRange]: ...
    @winrt_commethod(10)
    def add_RangesDownloaded(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Networking.BackgroundTransfer.DownloadOperation, Windows.Networking.BackgroundTransfer.BackgroundTransferRangesDownloadedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_RangesDownloaded(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def put_RequestedUri(self, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(13)
    def get_RecoverableWebErrorStatuses(self) -> Windows.Foundation.Collections.IVector[Windows.Web.WebErrorStatus]: ...
    @winrt_commethod(14)
    def get_CurrentWebErrorStatus(self) -> Windows.Foundation.IReference[Windows.Web.WebErrorStatus]: ...
    IsRandomAccessRequired = property(get_IsRandomAccessRequired, put_IsRandomAccessRequired)
    RequestedUri = property(None, put_RequestedUri)
    RecoverableWebErrorStatuses = property(get_RecoverableWebErrorStatuses, None)
    CurrentWebErrorStatus = property(get_CurrentWebErrorStatus, None)
class IDownloadOperation4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IDownloadOperation4'
    _iid_ = Guid('{0cdaaef4-8cef-404a-966d-f058400bed80}')
    @winrt_commethod(6)
    def MakeCurrentInTransferGroup(self) -> Void: ...
class IDownloadOperation5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IDownloadOperation5'
    _iid_ = Guid('{a699a86f-5590-463a-b8d6-1e491a2760a5}')
    @winrt_commethod(6)
    def SetRequestHeader(self, headerName: WinRT_String, headerValue: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def RemoveRequestHeader(self, headerName: WinRT_String) -> Void: ...
class IResponseInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IResponseInformation'
    _iid_ = Guid('{f8bb9a12-f713-4792-8b68-d9d297f91d2e}')
    @winrt_commethod(6)
    def get_IsResumable(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_ActualUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_StatusCode(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_Headers(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    IsResumable = property(get_IsResumable, None)
    ActualUri = property(get_ActualUri, None)
    StatusCode = property(get_StatusCode, None)
    Headers = property(get_Headers, None)
class IUnconstrainedTransferRequestResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IUnconstrainedTransferRequestResult'
    _iid_ = Guid('{4c24b81f-d944-4112-a98e-6a69522b7ebb}')
    @winrt_commethod(6)
    def get_IsUnconstrained(self) -> Boolean: ...
    IsUnconstrained = property(get_IsUnconstrained, None)
class IUploadOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IUploadOperation'
    _iid_ = Guid('{3e5624e0-7389-434c-8b35-427fd36bbdae}')
    @winrt_commethod(6)
    def get_SourceFile(self) -> Windows.Storage.IStorageFile: ...
    @winrt_commethod(7)
    def get_Progress(self) -> Windows.Networking.BackgroundTransfer.BackgroundUploadProgress: ...
    @winrt_commethod(8)
    def StartAsync(self) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Networking.BackgroundTransfer.UploadOperation, Windows.Networking.BackgroundTransfer.UploadOperation]: ...
    @winrt_commethod(9)
    def AttachAsync(self) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Networking.BackgroundTransfer.UploadOperation, Windows.Networking.BackgroundTransfer.UploadOperation]: ...
    SourceFile = property(get_SourceFile, None)
    Progress = property(get_Progress, None)
class IUploadOperation2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IUploadOperation2'
    _iid_ = Guid('{556189f2-2774-4df6-9fa5-209f2bfb12f7}')
    @winrt_commethod(6)
    def get_TransferGroup(self) -> Windows.Networking.BackgroundTransfer.BackgroundTransferGroup: ...
    TransferGroup = property(get_TransferGroup, None)
class IUploadOperation3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IUploadOperation3'
    _iid_ = Guid('{42c92ca3-de39-4546-bc62-3774b4294de3}')
    @winrt_commethod(6)
    def MakeCurrentInTransferGroup(self) -> Void: ...
class IUploadOperation4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IUploadOperation4'
    _iid_ = Guid('{50edef31-fac5-41ee-b030-dc77caee9faa}')
    @winrt_commethod(6)
    def SetRequestHeader(self, headerName: WinRT_String, headerValue: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def RemoveRequestHeader(self, headerName: WinRT_String) -> Void: ...
class ResponseInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.BackgroundTransfer.IResponseInformation
    _classid_ = 'Windows.Networking.BackgroundTransfer.ResponseInformation'
    @winrt_mixinmethod
    def get_IsResumable(self: Windows.Networking.BackgroundTransfer.IResponseInformation) -> Boolean: ...
    @winrt_mixinmethod
    def get_ActualUri(self: Windows.Networking.BackgroundTransfer.IResponseInformation) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_StatusCode(self: Windows.Networking.BackgroundTransfer.IResponseInformation) -> UInt32: ...
    @winrt_mixinmethod
    def get_Headers(self: Windows.Networking.BackgroundTransfer.IResponseInformation) -> Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    IsResumable = property(get_IsResumable, None)
    ActualUri = property(get_ActualUri, None)
    StatusCode = property(get_StatusCode, None)
    Headers = property(get_Headers, None)
class UnconstrainedTransferRequestResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.BackgroundTransfer.IUnconstrainedTransferRequestResult
    _classid_ = 'Windows.Networking.BackgroundTransfer.UnconstrainedTransferRequestResult'
    @winrt_mixinmethod
    def get_IsUnconstrained(self: Windows.Networking.BackgroundTransfer.IUnconstrainedTransferRequestResult) -> Boolean: ...
    IsUnconstrained = property(get_IsUnconstrained, None)
class UploadOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Networking.BackgroundTransfer.IUploadOperation
    _classid_ = 'Windows.Networking.BackgroundTransfer.UploadOperation'
    @winrt_mixinmethod
    def get_SourceFile(self: Windows.Networking.BackgroundTransfer.IUploadOperation) -> Windows.Storage.IStorageFile: ...
    @winrt_mixinmethod
    def get_Progress(self: Windows.Networking.BackgroundTransfer.IUploadOperation) -> Windows.Networking.BackgroundTransfer.BackgroundUploadProgress: ...
    @winrt_mixinmethod
    def StartAsync(self: Windows.Networking.BackgroundTransfer.IUploadOperation) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Networking.BackgroundTransfer.UploadOperation, Windows.Networking.BackgroundTransfer.UploadOperation]: ...
    @winrt_mixinmethod
    def AttachAsync(self: Windows.Networking.BackgroundTransfer.IUploadOperation) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Networking.BackgroundTransfer.UploadOperation, Windows.Networking.BackgroundTransfer.UploadOperation]: ...
    @winrt_mixinmethod
    def get_Guid(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation) -> Guid: ...
    @winrt_mixinmethod
    def get_RequestedUri(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Method(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Group(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CostPolicy(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation) -> Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy: ...
    @winrt_mixinmethod
    def put_CostPolicy(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation, value: Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy) -> Void: ...
    @winrt_mixinmethod
    def GetResultStreamAt(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation, position: UInt64) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def GetResponseInformation(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation) -> Windows.Networking.BackgroundTransfer.ResponseInformation: ...
    @winrt_mixinmethod
    def get_Priority(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferOperationPriority) -> Windows.Networking.BackgroundTransfer.BackgroundTransferPriority: ...
    @winrt_mixinmethod
    def put_Priority(self: Windows.Networking.BackgroundTransfer.IBackgroundTransferOperationPriority, value: Windows.Networking.BackgroundTransfer.BackgroundTransferPriority) -> Void: ...
    @winrt_mixinmethod
    def get_TransferGroup(self: Windows.Networking.BackgroundTransfer.IUploadOperation2) -> Windows.Networking.BackgroundTransfer.BackgroundTransferGroup: ...
    @winrt_mixinmethod
    def MakeCurrentInTransferGroup(self: Windows.Networking.BackgroundTransfer.IUploadOperation3) -> Void: ...
    @winrt_mixinmethod
    def SetRequestHeader(self: Windows.Networking.BackgroundTransfer.IUploadOperation4, headerName: WinRT_String, headerValue: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def RemoveRequestHeader(self: Windows.Networking.BackgroundTransfer.IUploadOperation4, headerName: WinRT_String) -> Void: ...
    SourceFile = property(get_SourceFile, None)
    Progress = property(get_Progress, None)
    Guid = property(get_Guid, None)
    RequestedUri = property(get_RequestedUri, None)
    Method = property(get_Method, None)
    Group = property(get_Group, None)
    CostPolicy = property(get_CostPolicy, put_CostPolicy)
    Priority = property(get_Priority, put_Priority)
    TransferGroup = property(get_TransferGroup, None)
make_head(_module, 'BackgroundDownloadProgress')
make_head(_module, 'BackgroundDownloader')
make_head(_module, 'BackgroundTransferCompletionGroup')
make_head(_module, 'BackgroundTransferCompletionGroupTriggerDetails')
make_head(_module, 'BackgroundTransferContentPart')
make_head(_module, 'BackgroundTransferError')
make_head(_module, 'BackgroundTransferFileRange')
make_head(_module, 'BackgroundTransferGroup')
make_head(_module, 'BackgroundTransferRangesDownloadedEventArgs')
make_head(_module, 'BackgroundUploadProgress')
make_head(_module, 'BackgroundUploader')
make_head(_module, 'ContentPrefetcher')
make_head(_module, 'DownloadOperation')
make_head(_module, 'IBackgroundDownloader')
make_head(_module, 'IBackgroundDownloader2')
make_head(_module, 'IBackgroundDownloader3')
make_head(_module, 'IBackgroundDownloaderFactory')
make_head(_module, 'IBackgroundDownloaderStaticMethods')
make_head(_module, 'IBackgroundDownloaderStaticMethods2')
make_head(_module, 'IBackgroundDownloaderUserConsent')
make_head(_module, 'IBackgroundTransferBase')
make_head(_module, 'IBackgroundTransferCompletionGroup')
make_head(_module, 'IBackgroundTransferCompletionGroupTriggerDetails')
make_head(_module, 'IBackgroundTransferContentPart')
make_head(_module, 'IBackgroundTransferContentPartFactory')
make_head(_module, 'IBackgroundTransferErrorStaticMethods')
make_head(_module, 'IBackgroundTransferGroup')
make_head(_module, 'IBackgroundTransferGroupStatics')
make_head(_module, 'IBackgroundTransferOperation')
make_head(_module, 'IBackgroundTransferOperationPriority')
make_head(_module, 'IBackgroundTransferRangesDownloadedEventArgs')
make_head(_module, 'IBackgroundUploader')
make_head(_module, 'IBackgroundUploader2')
make_head(_module, 'IBackgroundUploader3')
make_head(_module, 'IBackgroundUploaderFactory')
make_head(_module, 'IBackgroundUploaderStaticMethods')
make_head(_module, 'IBackgroundUploaderStaticMethods2')
make_head(_module, 'IBackgroundUploaderUserConsent')
make_head(_module, 'IContentPrefetcher')
make_head(_module, 'IContentPrefetcherTime')
make_head(_module, 'IDownloadOperation')
make_head(_module, 'IDownloadOperation2')
make_head(_module, 'IDownloadOperation3')
make_head(_module, 'IDownloadOperation4')
make_head(_module, 'IDownloadOperation5')
make_head(_module, 'IResponseInformation')
make_head(_module, 'IUnconstrainedTransferRequestResult')
make_head(_module, 'IUploadOperation')
make_head(_module, 'IUploadOperation2')
make_head(_module, 'IUploadOperation3')
make_head(_module, 'IUploadOperation4')
make_head(_module, 'ResponseInformation')
make_head(_module, 'UnconstrainedTransferRequestResult')
make_head(_module, 'UploadOperation')
