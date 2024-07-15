from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Background
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Networking.BackgroundTransfer
import win32more.Windows.Security.Credentials
import win32more.Windows.Storage
import win32more.Windows.Storage.Streams
import win32more.Windows.UI.Notifications
import win32more.Windows.Web
import win32more.Windows.Win32.System.WinRT
class BackgroundDownloadProgress(Structure):
    BytesReceived: UInt64
    TotalBytesToReceive: UInt64
    Status: win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferStatus
    HasResponseChanged: Boolean
    HasRestarted: Boolean
class BackgroundDownloader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.BackgroundTransfer.IBackgroundDownloader
    _classid_ = 'Windows.Networking.BackgroundTransfer.BackgroundDownloader'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Networking.BackgroundTransfer.BackgroundDownloader.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Networking.BackgroundTransfer.BackgroundDownloader.CreateWithCompletionGroup(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundDownloader: ...
    @winrt_factorymethod
    def CreateWithCompletionGroup(cls: win32more.Windows.Networking.BackgroundTransfer.IBackgroundDownloaderFactory, completionGroup: win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferCompletionGroup) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundDownloader: ...
    @winrt_mixinmethod
    def CreateDownload(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundDownloader, uri: win32more.Windows.Foundation.Uri, resultFile: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Networking.BackgroundTransfer.DownloadOperation: ...
    @winrt_mixinmethod
    def CreateDownloadFromFile(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundDownloader, uri: win32more.Windows.Foundation.Uri, resultFile: win32more.Windows.Storage.IStorageFile, requestBodyFile: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Networking.BackgroundTransfer.DownloadOperation: ...
    @winrt_mixinmethod
    def CreateDownloadAsync(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundDownloader, uri: win32more.Windows.Foundation.Uri, resultFile: win32more.Windows.Storage.IStorageFile, requestBodyStream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.BackgroundTransfer.DownloadOperation]: ...
    @winrt_mixinmethod
    def SetRequestHeader(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferBase, headerName: WinRT_String, headerValue: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ServerCredential(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferBase) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ServerCredential(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferBase, credential: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_ProxyCredential(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferBase) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ProxyCredential(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferBase, credential: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_Method(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferBase) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Method(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferBase, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Group(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferBase) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Group(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferBase, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CostPolicy(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferBase) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy: ...
    @winrt_mixinmethod
    def put_CostPolicy(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferBase, value: win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy) -> Void: ...
    @winrt_mixinmethod
    def get_TransferGroup(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundDownloader2) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferGroup: ...
    @winrt_mixinmethod
    def put_TransferGroup(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundDownloader2, value: win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferGroup) -> Void: ...
    @winrt_mixinmethod
    def get_SuccessToastNotification(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundDownloader2) -> win32more.Windows.UI.Notifications.ToastNotification: ...
    @winrt_mixinmethod
    def put_SuccessToastNotification(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundDownloader2, value: win32more.Windows.UI.Notifications.ToastNotification) -> Void: ...
    @winrt_mixinmethod
    def get_FailureToastNotification(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundDownloader2) -> win32more.Windows.UI.Notifications.ToastNotification: ...
    @winrt_mixinmethod
    def put_FailureToastNotification(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundDownloader2, value: win32more.Windows.UI.Notifications.ToastNotification) -> Void: ...
    @winrt_mixinmethod
    def get_SuccessTileNotification(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundDownloader2) -> win32more.Windows.UI.Notifications.TileNotification: ...
    @winrt_mixinmethod
    def put_SuccessTileNotification(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundDownloader2, value: win32more.Windows.UI.Notifications.TileNotification) -> Void: ...
    @winrt_mixinmethod
    def get_FailureTileNotification(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundDownloader2) -> win32more.Windows.UI.Notifications.TileNotification: ...
    @winrt_mixinmethod
    def put_FailureTileNotification(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundDownloader2, value: win32more.Windows.UI.Notifications.TileNotification) -> Void: ...
    @winrt_mixinmethod
    def get_CompletionGroup(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundDownloader3) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferCompletionGroup: ...
    @winrt_classmethod
    def GetCurrentDownloadsForTransferGroupAsync(cls: win32more.Windows.Networking.BackgroundTransfer.IBackgroundDownloaderStaticMethods2, group: win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferGroup) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.BackgroundTransfer.DownloadOperation]]: ...
    @winrt_classmethod
    def RequestUnconstrainedDownloadsAsync(cls: win32more.Windows.Networking.BackgroundTransfer.IBackgroundDownloaderUserConsent, operations: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Networking.BackgroundTransfer.DownloadOperation]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.BackgroundTransfer.UnconstrainedTransferRequestResult]: ...
    @winrt_classmethod
    def GetCurrentDownloadsAsync(cls: win32more.Windows.Networking.BackgroundTransfer.IBackgroundDownloaderStaticMethods) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.BackgroundTransfer.DownloadOperation]]: ...
    @winrt_classmethod
    def GetCurrentDownloadsForGroupAsync(cls: win32more.Windows.Networking.BackgroundTransfer.IBackgroundDownloaderStaticMethods, group: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.BackgroundTransfer.DownloadOperation]]: ...
    CompletionGroup = property(get_CompletionGroup, None)
    CostPolicy = property(get_CostPolicy, put_CostPolicy)
    FailureTileNotification = property(get_FailureTileNotification, put_FailureTileNotification)
    FailureToastNotification = property(get_FailureToastNotification, put_FailureToastNotification)
    Group = property(get_Group, put_Group)
    Method = property(get_Method, put_Method)
    ProxyCredential = property(get_ProxyCredential, put_ProxyCredential)
    ServerCredential = property(get_ServerCredential, put_ServerCredential)
    SuccessTileNotification = property(get_SuccessTileNotification, put_SuccessTileNotification)
    SuccessToastNotification = property(get_SuccessToastNotification, put_SuccessToastNotification)
    TransferGroup = property(get_TransferGroup, put_TransferGroup)
class BackgroundTransferBehavior(Enum, Int32):
    Parallel = 0
    Serialized = 1
class BackgroundTransferCompletionGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferCompletionGroup
    _classid_ = 'Windows.Networking.BackgroundTransfer.BackgroundTransferCompletionGroup'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferCompletionGroup.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferCompletionGroup: ...
    @winrt_mixinmethod
    def get_Trigger(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferCompletionGroup) -> win32more.Windows.ApplicationModel.Background.IBackgroundTrigger: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferCompletionGroup) -> Boolean: ...
    @winrt_mixinmethod
    def Enable(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferCompletionGroup) -> Void: ...
    IsEnabled = property(get_IsEnabled, None)
    Trigger = property(get_Trigger, None)
class BackgroundTransferCompletionGroupTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferCompletionGroupTriggerDetails
    _classid_ = 'Windows.Networking.BackgroundTransfer.BackgroundTransferCompletionGroupTriggerDetails'
    @winrt_mixinmethod
    def get_Downloads(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferCompletionGroupTriggerDetails) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.BackgroundTransfer.DownloadOperation]: ...
    @winrt_mixinmethod
    def get_Uploads(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferCompletionGroupTriggerDetails) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.BackgroundTransfer.UploadOperation]: ...
    Downloads = property(get_Downloads, None)
    Uploads = property(get_Uploads, None)
class BackgroundTransferContentPart(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferContentPart
    _classid_ = 'Windows.Networking.BackgroundTransfer.BackgroundTransferContentPart'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferContentPart.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferContentPart.CreateWithName(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferContentPart.CreateWithNameAndFileName(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferContentPart: ...
    @winrt_factorymethod
    def CreateWithName(cls: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferContentPartFactory, name: WinRT_String) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferContentPart: ...
    @winrt_factorymethod
    def CreateWithNameAndFileName(cls: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferContentPartFactory, name: WinRT_String, fileName: WinRT_String) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferContentPart: ...
    @winrt_mixinmethod
    def SetHeader(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferContentPart, headerName: WinRT_String, headerValue: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def SetText(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferContentPart, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def SetFile(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferContentPart, value: win32more.Windows.Storage.IStorageFile) -> Void: ...
class BackgroundTransferCostPolicy(Enum, Int32):
    Default = 0
    UnrestrictedOnly = 1
    Always = 2
class BackgroundTransferError(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.BackgroundTransferError'
    @winrt_classmethod
    def GetStatus(cls: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferErrorStaticMethods, hresult: Int32) -> win32more.Windows.Web.WebErrorStatus: ...
class BackgroundTransferFileRange(Structure):
    Offset: UInt64
    Length: UInt64
class BackgroundTransferGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferGroup
    _classid_ = 'Windows.Networking.BackgroundTransfer.BackgroundTransferGroup'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferGroup) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TransferBehavior(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferGroup) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferBehavior: ...
    @winrt_mixinmethod
    def put_TransferBehavior(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferGroup, value: win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferBehavior) -> Void: ...
    @winrt_classmethod
    def CreateGroup(cls: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferGroupStatics, name: WinRT_String) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferGroup: ...
    Name = property(get_Name, None)
    TransferBehavior = property(get_TransferBehavior, put_TransferBehavior)
class BackgroundTransferPriority(Enum, Int32):
    Default = 0
    High = 1
    Low = 2
class BackgroundTransferRangesDownloadedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferRangesDownloadedEventArgs
    _classid_ = 'Windows.Networking.BackgroundTransfer.BackgroundTransferRangesDownloadedEventArgs'
    @winrt_mixinmethod
    def get_WasDownloadRestarted(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferRangesDownloadedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_AddedRanges(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferRangesDownloadedEventArgs) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferFileRange]: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferRangesDownloadedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    AddedRanges = property(get_AddedRanges, None)
    WasDownloadRestarted = property(get_WasDownloadRestarted, None)
class BackgroundTransferStatus(Enum, Int32):
    Idle = 0
    Running = 1
    PausedByApplication = 2
    PausedCostedNetwork = 3
    PausedNoNetwork = 4
    Completed = 5
    Canceled = 6
    Error = 7
    PausedRecoverableWebErrorStatus = 8
    PausedSystemPolicy = 32
class BackgroundUploadProgress(Structure):
    BytesReceived: UInt64
    BytesSent: UInt64
    TotalBytesToReceive: UInt64
    TotalBytesToSend: UInt64
    Status: win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferStatus
    HasResponseChanged: Boolean
    HasRestarted: Boolean
class BackgroundUploader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.BackgroundTransfer.IBackgroundUploader
    _classid_ = 'Windows.Networking.BackgroundTransfer.BackgroundUploader'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Networking.BackgroundTransfer.BackgroundUploader.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Networking.BackgroundTransfer.BackgroundUploader.CreateWithCompletionGroup(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundUploader: ...
    @winrt_factorymethod
    def CreateWithCompletionGroup(cls: win32more.Windows.Networking.BackgroundTransfer.IBackgroundUploaderFactory, completionGroup: win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferCompletionGroup) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundUploader: ...
    @winrt_mixinmethod
    def CreateUpload(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundUploader, uri: win32more.Windows.Foundation.Uri, sourceFile: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Networking.BackgroundTransfer.UploadOperation: ...
    @winrt_mixinmethod
    def CreateUploadFromStreamAsync(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundUploader, uri: win32more.Windows.Foundation.Uri, sourceStream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.BackgroundTransfer.UploadOperation]: ...
    @winrt_mixinmethod
    def CreateUploadWithFormDataAndAutoBoundaryAsync(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundUploader, uri: win32more.Windows.Foundation.Uri, parts: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferContentPart]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.BackgroundTransfer.UploadOperation]: ...
    @winrt_mixinmethod
    def CreateUploadWithSubTypeAsync(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundUploader, uri: win32more.Windows.Foundation.Uri, parts: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferContentPart], subType: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.BackgroundTransfer.UploadOperation]: ...
    @winrt_mixinmethod
    def CreateUploadWithSubTypeAndBoundaryAsync(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundUploader, uri: win32more.Windows.Foundation.Uri, parts: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferContentPart], subType: WinRT_String, boundary: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.BackgroundTransfer.UploadOperation]: ...
    @winrt_mixinmethod
    def SetRequestHeader(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferBase, headerName: WinRT_String, headerValue: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ServerCredential(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferBase) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ServerCredential(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferBase, credential: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_ProxyCredential(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferBase) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def put_ProxyCredential(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferBase, credential: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_mixinmethod
    def get_Method(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferBase) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Method(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferBase, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Group(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferBase) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Group(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferBase, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CostPolicy(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferBase) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy: ...
    @winrt_mixinmethod
    def put_CostPolicy(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferBase, value: win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy) -> Void: ...
    @winrt_mixinmethod
    def get_TransferGroup(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundUploader2) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferGroup: ...
    @winrt_mixinmethod
    def put_TransferGroup(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundUploader2, value: win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferGroup) -> Void: ...
    @winrt_mixinmethod
    def get_SuccessToastNotification(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundUploader2) -> win32more.Windows.UI.Notifications.ToastNotification: ...
    @winrt_mixinmethod
    def put_SuccessToastNotification(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundUploader2, value: win32more.Windows.UI.Notifications.ToastNotification) -> Void: ...
    @winrt_mixinmethod
    def get_FailureToastNotification(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundUploader2) -> win32more.Windows.UI.Notifications.ToastNotification: ...
    @winrt_mixinmethod
    def put_FailureToastNotification(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundUploader2, value: win32more.Windows.UI.Notifications.ToastNotification) -> Void: ...
    @winrt_mixinmethod
    def get_SuccessTileNotification(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundUploader2) -> win32more.Windows.UI.Notifications.TileNotification: ...
    @winrt_mixinmethod
    def put_SuccessTileNotification(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundUploader2, value: win32more.Windows.UI.Notifications.TileNotification) -> Void: ...
    @winrt_mixinmethod
    def get_FailureTileNotification(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundUploader2) -> win32more.Windows.UI.Notifications.TileNotification: ...
    @winrt_mixinmethod
    def put_FailureTileNotification(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundUploader2, value: win32more.Windows.UI.Notifications.TileNotification) -> Void: ...
    @winrt_mixinmethod
    def get_CompletionGroup(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundUploader3) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferCompletionGroup: ...
    @winrt_classmethod
    def GetCurrentUploadsForTransferGroupAsync(cls: win32more.Windows.Networking.BackgroundTransfer.IBackgroundUploaderStaticMethods2, group: win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferGroup) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.BackgroundTransfer.UploadOperation]]: ...
    @winrt_classmethod
    def RequestUnconstrainedUploadsAsync(cls: win32more.Windows.Networking.BackgroundTransfer.IBackgroundUploaderUserConsent, operations: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Networking.BackgroundTransfer.UploadOperation]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.BackgroundTransfer.UnconstrainedTransferRequestResult]: ...
    @winrt_classmethod
    def GetCurrentUploadsAsync(cls: win32more.Windows.Networking.BackgroundTransfer.IBackgroundUploaderStaticMethods) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.BackgroundTransfer.UploadOperation]]: ...
    @winrt_classmethod
    def GetCurrentUploadsForGroupAsync(cls: win32more.Windows.Networking.BackgroundTransfer.IBackgroundUploaderStaticMethods, group: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.BackgroundTransfer.UploadOperation]]: ...
    CompletionGroup = property(get_CompletionGroup, None)
    CostPolicy = property(get_CostPolicy, put_CostPolicy)
    FailureTileNotification = property(get_FailureTileNotification, put_FailureTileNotification)
    FailureToastNotification = property(get_FailureToastNotification, put_FailureToastNotification)
    Group = property(get_Group, put_Group)
    Method = property(get_Method, put_Method)
    ProxyCredential = property(get_ProxyCredential, put_ProxyCredential)
    ServerCredential = property(get_ServerCredential, put_ServerCredential)
    SuccessTileNotification = property(get_SuccessTileNotification, put_SuccessTileNotification)
    SuccessToastNotification = property(get_SuccessToastNotification, put_SuccessToastNotification)
    TransferGroup = property(get_TransferGroup, put_TransferGroup)
class _ContentPrefetcher_Meta_(ComPtr.__class__):
    pass
class ContentPrefetcher(ComPtr, metaclass=_ContentPrefetcher_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.ContentPrefetcher'
    @winrt_classmethod
    def get_LastSuccessfulPrefetchTime(cls: win32more.Windows.Networking.BackgroundTransfer.IContentPrefetcherTime) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_classmethod
    def get_ContentUris(cls: win32more.Windows.Networking.BackgroundTransfer.IContentPrefetcher) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Foundation.Uri]: ...
    @winrt_classmethod
    def put_IndirectContentUri(cls: win32more.Windows.Networking.BackgroundTransfer.IContentPrefetcher, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_classmethod
    def get_IndirectContentUri(cls: win32more.Windows.Networking.BackgroundTransfer.IContentPrefetcher) -> win32more.Windows.Foundation.Uri: ...
    _ContentPrefetcher_Meta_.ContentUris = property(get_ContentUris, None)
    _ContentPrefetcher_Meta_.IndirectContentUri = property(get_IndirectContentUri, put_IndirectContentUri)
    _ContentPrefetcher_Meta_.LastSuccessfulPrefetchTime = property(get_LastSuccessfulPrefetchTime, None)
class DownloadOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.BackgroundTransfer.IDownloadOperation
    _classid_ = 'Windows.Networking.BackgroundTransfer.DownloadOperation'
    @winrt_mixinmethod
    def get_ResultFile(self: win32more.Windows.Networking.BackgroundTransfer.IDownloadOperation) -> win32more.Windows.Storage.IStorageFile: ...
    @winrt_mixinmethod
    def get_Progress(self: win32more.Windows.Networking.BackgroundTransfer.IDownloadOperation) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundDownloadProgress: ...
    @winrt_mixinmethod
    def StartAsync(self: win32more.Windows.Networking.BackgroundTransfer.IDownloadOperation) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Networking.BackgroundTransfer.DownloadOperation, win32more.Windows.Networking.BackgroundTransfer.DownloadOperation]: ...
    @winrt_mixinmethod
    def AttachAsync(self: win32more.Windows.Networking.BackgroundTransfer.IDownloadOperation) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Networking.BackgroundTransfer.DownloadOperation, win32more.Windows.Networking.BackgroundTransfer.DownloadOperation]: ...
    @winrt_mixinmethod
    def Pause(self: win32more.Windows.Networking.BackgroundTransfer.IDownloadOperation) -> Void: ...
    @winrt_mixinmethod
    def Resume(self: win32more.Windows.Networking.BackgroundTransfer.IDownloadOperation) -> Void: ...
    @winrt_mixinmethod
    def get_Guid(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation) -> Guid: ...
    @winrt_mixinmethod
    def get_RequestedUri(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Method(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Group(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CostPolicy(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy: ...
    @winrt_mixinmethod
    def put_CostPolicy(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation, value: win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy) -> Void: ...
    @winrt_mixinmethod
    def GetResultStreamAt(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation, position: UInt64) -> win32more.Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def GetResponseInformation(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation) -> win32more.Windows.Networking.BackgroundTransfer.ResponseInformation: ...
    @winrt_mixinmethod
    def get_Priority(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferOperationPriority) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferPriority: ...
    @winrt_mixinmethod
    def put_Priority(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferOperationPriority, value: win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferPriority) -> Void: ...
    @winrt_mixinmethod
    def get_TransferGroup(self: win32more.Windows.Networking.BackgroundTransfer.IDownloadOperation2) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferGroup: ...
    @winrt_mixinmethod
    def get_IsRandomAccessRequired(self: win32more.Windows.Networking.BackgroundTransfer.IDownloadOperation3) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsRandomAccessRequired(self: win32more.Windows.Networking.BackgroundTransfer.IDownloadOperation3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetResultRandomAccessStreamReference(self: win32more.Windows.Networking.BackgroundTransfer.IDownloadOperation3) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def GetDownloadedRanges(self: win32more.Windows.Networking.BackgroundTransfer.IDownloadOperation3) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferFileRange]: ...
    @winrt_mixinmethod
    def add_RangesDownloaded(self: win32more.Windows.Networking.BackgroundTransfer.IDownloadOperation3, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.BackgroundTransfer.DownloadOperation, win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferRangesDownloadedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RangesDownloaded(self: win32more.Windows.Networking.BackgroundTransfer.IDownloadOperation3, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def put_RequestedUri(self: win32more.Windows.Networking.BackgroundTransfer.IDownloadOperation3, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_RecoverableWebErrorStatuses(self: win32more.Windows.Networking.BackgroundTransfer.IDownloadOperation3) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Web.WebErrorStatus]: ...
    @winrt_mixinmethod
    def get_CurrentWebErrorStatus(self: win32more.Windows.Networking.BackgroundTransfer.IDownloadOperation3) -> win32more.Windows.Foundation.IReference[win32more.Windows.Web.WebErrorStatus]: ...
    @winrt_mixinmethod
    def MakeCurrentInTransferGroup(self: win32more.Windows.Networking.BackgroundTransfer.IDownloadOperation4) -> Void: ...
    @winrt_mixinmethod
    def SetRequestHeader(self: win32more.Windows.Networking.BackgroundTransfer.IDownloadOperation5, headerName: WinRT_String, headerValue: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def RemoveRequestHeader(self: win32more.Windows.Networking.BackgroundTransfer.IDownloadOperation5, headerName: WinRT_String) -> Void: ...
    CostPolicy = property(get_CostPolicy, put_CostPolicy)
    CurrentWebErrorStatus = property(get_CurrentWebErrorStatus, None)
    Group = property(get_Group, None)
    Guid = property(get_Guid, None)
    IsRandomAccessRequired = property(get_IsRandomAccessRequired, put_IsRandomAccessRequired)
    Method = property(get_Method, None)
    Priority = property(get_Priority, put_Priority)
    Progress = property(get_Progress, None)
    RecoverableWebErrorStatuses = property(get_RecoverableWebErrorStatuses, None)
    RequestedUri = property(get_RequestedUri, put_RequestedUri)
    ResultFile = property(get_ResultFile, None)
    TransferGroup = property(get_TransferGroup, None)
    RangesDownloaded = event()
class IBackgroundDownloader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundDownloader'
    _iid_ = Guid('{c1c79333-6649-4b1d-a826-a4b3dd234d0b}')
    @winrt_commethod(6)
    def CreateDownload(self, uri: win32more.Windows.Foundation.Uri, resultFile: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Networking.BackgroundTransfer.DownloadOperation: ...
    @winrt_commethod(7)
    def CreateDownloadFromFile(self, uri: win32more.Windows.Foundation.Uri, resultFile: win32more.Windows.Storage.IStorageFile, requestBodyFile: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Networking.BackgroundTransfer.DownloadOperation: ...
    @winrt_commethod(8)
    def CreateDownloadAsync(self, uri: win32more.Windows.Foundation.Uri, resultFile: win32more.Windows.Storage.IStorageFile, requestBodyStream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.BackgroundTransfer.DownloadOperation]: ...
class IBackgroundDownloader2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundDownloader2'
    _iid_ = Guid('{a94a5847-348d-4a35-890e-8a1ef3798479}')
    @winrt_commethod(6)
    def get_TransferGroup(self) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferGroup: ...
    @winrt_commethod(7)
    def put_TransferGroup(self, value: win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferGroup) -> Void: ...
    @winrt_commethod(8)
    def get_SuccessToastNotification(self) -> win32more.Windows.UI.Notifications.ToastNotification: ...
    @winrt_commethod(9)
    def put_SuccessToastNotification(self, value: win32more.Windows.UI.Notifications.ToastNotification) -> Void: ...
    @winrt_commethod(10)
    def get_FailureToastNotification(self) -> win32more.Windows.UI.Notifications.ToastNotification: ...
    @winrt_commethod(11)
    def put_FailureToastNotification(self, value: win32more.Windows.UI.Notifications.ToastNotification) -> Void: ...
    @winrt_commethod(12)
    def get_SuccessTileNotification(self) -> win32more.Windows.UI.Notifications.TileNotification: ...
    @winrt_commethod(13)
    def put_SuccessTileNotification(self, value: win32more.Windows.UI.Notifications.TileNotification) -> Void: ...
    @winrt_commethod(14)
    def get_FailureTileNotification(self) -> win32more.Windows.UI.Notifications.TileNotification: ...
    @winrt_commethod(15)
    def put_FailureTileNotification(self, value: win32more.Windows.UI.Notifications.TileNotification) -> Void: ...
    FailureTileNotification = property(get_FailureTileNotification, put_FailureTileNotification)
    FailureToastNotification = property(get_FailureToastNotification, put_FailureToastNotification)
    SuccessTileNotification = property(get_SuccessTileNotification, put_SuccessTileNotification)
    SuccessToastNotification = property(get_SuccessToastNotification, put_SuccessToastNotification)
    TransferGroup = property(get_TransferGroup, put_TransferGroup)
class IBackgroundDownloader3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundDownloader3'
    _iid_ = Guid('{d11a8c48-86e8-48e2-b615-6976aabf861d}')
    @winrt_commethod(6)
    def get_CompletionGroup(self) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferCompletionGroup: ...
    CompletionGroup = property(get_CompletionGroup, None)
class IBackgroundDownloaderFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundDownloaderFactory'
    _iid_ = Guid('{26836c24-d89e-46f4-a29a-4f4d4f144155}')
    @winrt_commethod(6)
    def CreateWithCompletionGroup(self, completionGroup: win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferCompletionGroup) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundDownloader: ...
class IBackgroundDownloaderStaticMethods(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundDownloaderStaticMethods'
    _iid_ = Guid('{52a65a35-c64e-426c-9919-540d0d21a650}')
    @winrt_commethod(6)
    def GetCurrentDownloadsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.BackgroundTransfer.DownloadOperation]]: ...
    @winrt_commethod(7)
    def GetCurrentDownloadsForGroupAsync(self, group: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.BackgroundTransfer.DownloadOperation]]: ...
class IBackgroundDownloaderStaticMethods2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundDownloaderStaticMethods2'
    _iid_ = Guid('{2faa1327-1ad4-4ca5-b2cd-08dbf0746afe}')
    @winrt_commethod(6)
    def GetCurrentDownloadsForTransferGroupAsync(self, group: win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferGroup) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.BackgroundTransfer.DownloadOperation]]: ...
class IBackgroundDownloaderUserConsent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundDownloaderUserConsent'
    _iid_ = Guid('{5d14e906-9266-4808-bd71-5925f2a3130a}')
    @winrt_commethod(6)
    def RequestUnconstrainedDownloadsAsync(self, operations: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Networking.BackgroundTransfer.DownloadOperation]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.BackgroundTransfer.UnconstrainedTransferRequestResult]: ...
class IBackgroundTransferBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundTransferBase'
    _iid_ = Guid('{2a9da250-c769-458c-afe8-feb8d4d3b2ef}')
    @winrt_commethod(6)
    def SetRequestHeader(self, headerName: WinRT_String, headerValue: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_ServerCredential(self) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(8)
    def put_ServerCredential(self, credential: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_commethod(9)
    def get_ProxyCredential(self) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(10)
    def put_ProxyCredential(self, credential: win32more.Windows.Security.Credentials.PasswordCredential) -> Void: ...
    @winrt_commethod(11)
    def get_Method(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_Method(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def get_Group(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_Group(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_CostPolicy(self) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy: ...
    @winrt_commethod(16)
    def put_CostPolicy(self, value: win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy) -> Void: ...
    CostPolicy = property(get_CostPolicy, put_CostPolicy)
    Group = property(get_Group, put_Group)
    Method = property(get_Method, put_Method)
    ProxyCredential = property(get_ProxyCredential, put_ProxyCredential)
    ServerCredential = property(get_ServerCredential, put_ServerCredential)
class IBackgroundTransferCompletionGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundTransferCompletionGroup'
    _iid_ = Guid('{2d930225-986b-574d-7950-0add47f5d706}')
    @winrt_commethod(6)
    def get_Trigger(self) -> win32more.Windows.ApplicationModel.Background.IBackgroundTrigger: ...
    @winrt_commethod(7)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def Enable(self) -> Void: ...
    IsEnabled = property(get_IsEnabled, None)
    Trigger = property(get_Trigger, None)
class IBackgroundTransferCompletionGroupTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundTransferCompletionGroupTriggerDetails'
    _iid_ = Guid('{7b6be286-6e47-5136-7fcb-fa4389f46f5b}')
    @winrt_commethod(6)
    def get_Downloads(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.BackgroundTransfer.DownloadOperation]: ...
    @winrt_commethod(7)
    def get_Uploads(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.BackgroundTransfer.UploadOperation]: ...
    Downloads = property(get_Downloads, None)
    Uploads = property(get_Uploads, None)
class IBackgroundTransferContentPart(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundTransferContentPart'
    _iid_ = Guid('{e8e15657-d7d1-4ed8-838e-674ac217ace6}')
    @winrt_commethod(6)
    def SetHeader(self, headerName: WinRT_String, headerValue: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def SetText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def SetFile(self, value: win32more.Windows.Storage.IStorageFile) -> Void: ...
class IBackgroundTransferContentPartFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundTransferContentPartFactory'
    _iid_ = Guid('{90ef98a9-7a01-4a0b-9f80-a0b0bb370f8d}')
    @winrt_commethod(6)
    def CreateWithName(self, name: WinRT_String) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferContentPart: ...
    @winrt_commethod(7)
    def CreateWithNameAndFileName(self, name: WinRT_String, fileName: WinRT_String) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferContentPart: ...
class IBackgroundTransferErrorStaticMethods(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundTransferErrorStaticMethods'
    _iid_ = Guid('{aad33b04-1192-4bf4-8b68-39c5add244e2}')
    @winrt_commethod(6)
    def GetStatus(self, hresult: Int32) -> win32more.Windows.Web.WebErrorStatus: ...
class IBackgroundTransferGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundTransferGroup'
    _iid_ = Guid('{d8c3e3e4-6459-4540-85eb-aaa1c8903677}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_TransferBehavior(self) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferBehavior: ...
    @winrt_commethod(8)
    def put_TransferBehavior(self, value: win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferBehavior) -> Void: ...
    Name = property(get_Name, None)
    TransferBehavior = property(get_TransferBehavior, put_TransferBehavior)
class IBackgroundTransferGroupStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundTransferGroupStatics'
    _iid_ = Guid('{02ec50b2-7d18-495b-aa22-32a97d45d3e2}')
    @winrt_commethod(6)
    def CreateGroup(self, name: WinRT_String) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferGroup: ...
class IBackgroundTransferOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation'
    _iid_ = Guid('{ded06846-90ca-44fb-8fb1-124154c0d539}')
    @winrt_commethod(6)
    def get_Guid(self) -> Guid: ...
    @winrt_commethod(7)
    def get_RequestedUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_Method(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Group(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_CostPolicy(self) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy: ...
    @winrt_commethod(11)
    def put_CostPolicy(self, value: win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy) -> Void: ...
    @winrt_commethod(12)
    def GetResultStreamAt(self, position: UInt64) -> win32more.Windows.Storage.Streams.IInputStream: ...
    @winrt_commethod(13)
    def GetResponseInformation(self) -> win32more.Windows.Networking.BackgroundTransfer.ResponseInformation: ...
    CostPolicy = property(get_CostPolicy, put_CostPolicy)
    Group = property(get_Group, None)
    Guid = property(get_Guid, None)
    Method = property(get_Method, None)
    RequestedUri = property(get_RequestedUri, None)
class IBackgroundTransferOperationPriority(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundTransferOperationPriority'
    _iid_ = Guid('{04854327-5254-4b3a-915e-0aa49275c0f9}')
    @winrt_commethod(6)
    def get_Priority(self) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferPriority: ...
    @winrt_commethod(7)
    def put_Priority(self, value: win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferPriority) -> Void: ...
    Priority = property(get_Priority, put_Priority)
class IBackgroundTransferRangesDownloadedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundTransferRangesDownloadedEventArgs'
    _iid_ = Guid('{3ebc7453-bf48-4a88-9248-b0c165184f5c}')
    @winrt_commethod(6)
    def get_WasDownloadRestarted(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_AddedRanges(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferFileRange]: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    AddedRanges = property(get_AddedRanges, None)
    WasDownloadRestarted = property(get_WasDownloadRestarted, None)
class IBackgroundUploader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundUploader'
    _iid_ = Guid('{c595c9ae-cead-465b-8801-c55ac90a01ce}')
    @winrt_commethod(6)
    def CreateUpload(self, uri: win32more.Windows.Foundation.Uri, sourceFile: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Networking.BackgroundTransfer.UploadOperation: ...
    @winrt_commethod(7)
    def CreateUploadFromStreamAsync(self, uri: win32more.Windows.Foundation.Uri, sourceStream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.BackgroundTransfer.UploadOperation]: ...
    @winrt_commethod(8)
    def CreateUploadWithFormDataAndAutoBoundaryAsync(self, uri: win32more.Windows.Foundation.Uri, parts: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferContentPart]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.BackgroundTransfer.UploadOperation]: ...
    @winrt_commethod(9)
    def CreateUploadWithSubTypeAsync(self, uri: win32more.Windows.Foundation.Uri, parts: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferContentPart], subType: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.BackgroundTransfer.UploadOperation]: ...
    @winrt_commethod(10)
    def CreateUploadWithSubTypeAndBoundaryAsync(self, uri: win32more.Windows.Foundation.Uri, parts: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferContentPart], subType: WinRT_String, boundary: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.BackgroundTransfer.UploadOperation]: ...
class IBackgroundUploader2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundUploader2'
    _iid_ = Guid('{8e0612ce-0c34-4463-807f-198a1b8bd4ad}')
    @winrt_commethod(6)
    def get_TransferGroup(self) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferGroup: ...
    @winrt_commethod(7)
    def put_TransferGroup(self, value: win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferGroup) -> Void: ...
    @winrt_commethod(8)
    def get_SuccessToastNotification(self) -> win32more.Windows.UI.Notifications.ToastNotification: ...
    @winrt_commethod(9)
    def put_SuccessToastNotification(self, value: win32more.Windows.UI.Notifications.ToastNotification) -> Void: ...
    @winrt_commethod(10)
    def get_FailureToastNotification(self) -> win32more.Windows.UI.Notifications.ToastNotification: ...
    @winrt_commethod(11)
    def put_FailureToastNotification(self, value: win32more.Windows.UI.Notifications.ToastNotification) -> Void: ...
    @winrt_commethod(12)
    def get_SuccessTileNotification(self) -> win32more.Windows.UI.Notifications.TileNotification: ...
    @winrt_commethod(13)
    def put_SuccessTileNotification(self, value: win32more.Windows.UI.Notifications.TileNotification) -> Void: ...
    @winrt_commethod(14)
    def get_FailureTileNotification(self) -> win32more.Windows.UI.Notifications.TileNotification: ...
    @winrt_commethod(15)
    def put_FailureTileNotification(self, value: win32more.Windows.UI.Notifications.TileNotification) -> Void: ...
    FailureTileNotification = property(get_FailureTileNotification, put_FailureTileNotification)
    FailureToastNotification = property(get_FailureToastNotification, put_FailureToastNotification)
    SuccessTileNotification = property(get_SuccessTileNotification, put_SuccessTileNotification)
    SuccessToastNotification = property(get_SuccessToastNotification, put_SuccessToastNotification)
    TransferGroup = property(get_TransferGroup, put_TransferGroup)
class IBackgroundUploader3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundUploader3'
    _iid_ = Guid('{b95e9439-5bf0-4b3a-8c47-2c6199a854b9}')
    @winrt_commethod(6)
    def get_CompletionGroup(self) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferCompletionGroup: ...
    CompletionGroup = property(get_CompletionGroup, None)
class IBackgroundUploaderFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundUploaderFactory'
    _iid_ = Guid('{736203c7-10e7-48a0-ac3c-1ac71095ec57}')
    @winrt_commethod(6)
    def CreateWithCompletionGroup(self, completionGroup: win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferCompletionGroup) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundUploader: ...
class IBackgroundUploaderStaticMethods(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundUploaderStaticMethods'
    _iid_ = Guid('{f2875cfb-9b05-4741-9121-740a83e247df}')
    @winrt_commethod(6)
    def GetCurrentUploadsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.BackgroundTransfer.UploadOperation]]: ...
    @winrt_commethod(7)
    def GetCurrentUploadsForGroupAsync(self, group: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.BackgroundTransfer.UploadOperation]]: ...
class IBackgroundUploaderStaticMethods2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundUploaderStaticMethods2'
    _iid_ = Guid('{e919ac62-ea08-42f0-a2ac-07e467549080}')
    @winrt_commethod(6)
    def GetCurrentUploadsForTransferGroupAsync(self, group: win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferGroup) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.BackgroundTransfer.UploadOperation]]: ...
class IBackgroundUploaderUserConsent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IBackgroundUploaderUserConsent'
    _iid_ = Guid('{3bb384cb-0760-461d-907f-5138f84d44c1}')
    @winrt_commethod(6)
    def RequestUnconstrainedUploadsAsync(self, operations: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Networking.BackgroundTransfer.UploadOperation]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.BackgroundTransfer.UnconstrainedTransferRequestResult]: ...
class IContentPrefetcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IContentPrefetcher'
    _iid_ = Guid('{a8d6f754-7dc1-4cd9-8810-2a6aa9417e11}')
    @winrt_commethod(6)
    def get_ContentUris(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Foundation.Uri]: ...
    @winrt_commethod(7)
    def put_IndirectContentUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def get_IndirectContentUri(self) -> win32more.Windows.Foundation.Uri: ...
    ContentUris = property(get_ContentUris, None)
    IndirectContentUri = property(get_IndirectContentUri, put_IndirectContentUri)
class IContentPrefetcherTime(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IContentPrefetcherTime'
    _iid_ = Guid('{e361fd08-132a-4fde-a7cc-fcb0e66523af}')
    @winrt_commethod(6)
    def get_LastSuccessfulPrefetchTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    LastSuccessfulPrefetchTime = property(get_LastSuccessfulPrefetchTime, None)
class IDownloadOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IDownloadOperation'
    _iid_ = Guid('{bd87ebb0-5714-4e09-ba68-bef73903b0d7}')
    @winrt_commethod(6)
    def get_ResultFile(self) -> win32more.Windows.Storage.IStorageFile: ...
    @winrt_commethod(7)
    def get_Progress(self) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundDownloadProgress: ...
    @winrt_commethod(8)
    def StartAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Networking.BackgroundTransfer.DownloadOperation, win32more.Windows.Networking.BackgroundTransfer.DownloadOperation]: ...
    @winrt_commethod(9)
    def AttachAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Networking.BackgroundTransfer.DownloadOperation, win32more.Windows.Networking.BackgroundTransfer.DownloadOperation]: ...
    @winrt_commethod(10)
    def Pause(self) -> Void: ...
    @winrt_commethod(11)
    def Resume(self) -> Void: ...
    Progress = property(get_Progress, None)
    ResultFile = property(get_ResultFile, None)
class IDownloadOperation2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IDownloadOperation2'
    _iid_ = Guid('{a3cced40-8f9c-4353-9cd4-290dee387c38}')
    @winrt_commethod(6)
    def get_TransferGroup(self) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferGroup: ...
    TransferGroup = property(get_TransferGroup, None)
class IDownloadOperation3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IDownloadOperation3'
    _iid_ = Guid('{5027351c-7d5e-4adc-b8d3-df5c6031b9cc}')
    @winrt_commethod(6)
    def get_IsRandomAccessRequired(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsRandomAccessRequired(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def GetResultRandomAccessStreamReference(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(9)
    def GetDownloadedRanges(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferFileRange]: ...
    @winrt_commethod(10)
    def add_RangesDownloaded(self, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.BackgroundTransfer.DownloadOperation, win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferRangesDownloadedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_RangesDownloaded(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def put_RequestedUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(13)
    def get_RecoverableWebErrorStatuses(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Web.WebErrorStatus]: ...
    @winrt_commethod(14)
    def get_CurrentWebErrorStatus(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Web.WebErrorStatus]: ...
    CurrentWebErrorStatus = property(get_CurrentWebErrorStatus, None)
    IsRandomAccessRequired = property(get_IsRandomAccessRequired, put_IsRandomAccessRequired)
    RecoverableWebErrorStatuses = property(get_RecoverableWebErrorStatuses, None)
    RequestedUri = property(None, put_RequestedUri)
    RangesDownloaded = event()
class IDownloadOperation4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IDownloadOperation4'
    _iid_ = Guid('{0cdaaef4-8cef-404a-966d-f058400bed80}')
    @winrt_commethod(6)
    def MakeCurrentInTransferGroup(self) -> Void: ...
class IDownloadOperation5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IDownloadOperation5'
    _iid_ = Guid('{a699a86f-5590-463a-b8d6-1e491a2760a5}')
    @winrt_commethod(6)
    def SetRequestHeader(self, headerName: WinRT_String, headerValue: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def RemoveRequestHeader(self, headerName: WinRT_String) -> Void: ...
class IResponseInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IResponseInformation'
    _iid_ = Guid('{f8bb9a12-f713-4792-8b68-d9d297f91d2e}')
    @winrt_commethod(6)
    def get_IsResumable(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_ActualUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_StatusCode(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_Headers(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    ActualUri = property(get_ActualUri, None)
    Headers = property(get_Headers, None)
    IsResumable = property(get_IsResumable, None)
    StatusCode = property(get_StatusCode, None)
class IUnconstrainedTransferRequestResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IUnconstrainedTransferRequestResult'
    _iid_ = Guid('{4c24b81f-d944-4112-a98e-6a69522b7ebb}')
    @winrt_commethod(6)
    def get_IsUnconstrained(self) -> Boolean: ...
    IsUnconstrained = property(get_IsUnconstrained, None)
class IUploadOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IUploadOperation'
    _iid_ = Guid('{3e5624e0-7389-434c-8b35-427fd36bbdae}')
    @winrt_commethod(6)
    def get_SourceFile(self) -> win32more.Windows.Storage.IStorageFile: ...
    @winrt_commethod(7)
    def get_Progress(self) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundUploadProgress: ...
    @winrt_commethod(8)
    def StartAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Networking.BackgroundTransfer.UploadOperation, win32more.Windows.Networking.BackgroundTransfer.UploadOperation]: ...
    @winrt_commethod(9)
    def AttachAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Networking.BackgroundTransfer.UploadOperation, win32more.Windows.Networking.BackgroundTransfer.UploadOperation]: ...
    Progress = property(get_Progress, None)
    SourceFile = property(get_SourceFile, None)
class IUploadOperation2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IUploadOperation2'
    _iid_ = Guid('{556189f2-2774-4df6-9fa5-209f2bfb12f7}')
    @winrt_commethod(6)
    def get_TransferGroup(self) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferGroup: ...
    TransferGroup = property(get_TransferGroup, None)
class IUploadOperation3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IUploadOperation3'
    _iid_ = Guid('{42c92ca3-de39-4546-bc62-3774b4294de3}')
    @winrt_commethod(6)
    def MakeCurrentInTransferGroup(self) -> Void: ...
class IUploadOperation4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.BackgroundTransfer.IUploadOperation4'
    _iid_ = Guid('{50edef31-fac5-41ee-b030-dc77caee9faa}')
    @winrt_commethod(6)
    def SetRequestHeader(self, headerName: WinRT_String, headerValue: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def RemoveRequestHeader(self, headerName: WinRT_String) -> Void: ...
class ResponseInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.BackgroundTransfer.IResponseInformation
    _classid_ = 'Windows.Networking.BackgroundTransfer.ResponseInformation'
    @winrt_mixinmethod
    def get_IsResumable(self: win32more.Windows.Networking.BackgroundTransfer.IResponseInformation) -> Boolean: ...
    @winrt_mixinmethod
    def get_ActualUri(self: win32more.Windows.Networking.BackgroundTransfer.IResponseInformation) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_StatusCode(self: win32more.Windows.Networking.BackgroundTransfer.IResponseInformation) -> UInt32: ...
    @winrt_mixinmethod
    def get_Headers(self: win32more.Windows.Networking.BackgroundTransfer.IResponseInformation) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    ActualUri = property(get_ActualUri, None)
    Headers = property(get_Headers, None)
    IsResumable = property(get_IsResumable, None)
    StatusCode = property(get_StatusCode, None)
class UnconstrainedTransferRequestResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.BackgroundTransfer.IUnconstrainedTransferRequestResult
    _classid_ = 'Windows.Networking.BackgroundTransfer.UnconstrainedTransferRequestResult'
    @winrt_mixinmethod
    def get_IsUnconstrained(self: win32more.Windows.Networking.BackgroundTransfer.IUnconstrainedTransferRequestResult) -> Boolean: ...
    IsUnconstrained = property(get_IsUnconstrained, None)
class UploadOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.BackgroundTransfer.IUploadOperation
    _classid_ = 'Windows.Networking.BackgroundTransfer.UploadOperation'
    @winrt_mixinmethod
    def get_SourceFile(self: win32more.Windows.Networking.BackgroundTransfer.IUploadOperation) -> win32more.Windows.Storage.IStorageFile: ...
    @winrt_mixinmethod
    def get_Progress(self: win32more.Windows.Networking.BackgroundTransfer.IUploadOperation) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundUploadProgress: ...
    @winrt_mixinmethod
    def StartAsync(self: win32more.Windows.Networking.BackgroundTransfer.IUploadOperation) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Networking.BackgroundTransfer.UploadOperation, win32more.Windows.Networking.BackgroundTransfer.UploadOperation]: ...
    @winrt_mixinmethod
    def AttachAsync(self: win32more.Windows.Networking.BackgroundTransfer.IUploadOperation) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Networking.BackgroundTransfer.UploadOperation, win32more.Windows.Networking.BackgroundTransfer.UploadOperation]: ...
    @winrt_mixinmethod
    def get_Guid(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation) -> Guid: ...
    @winrt_mixinmethod
    def get_RequestedUri(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Method(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Group(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CostPolicy(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy: ...
    @winrt_mixinmethod
    def put_CostPolicy(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation, value: win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy) -> Void: ...
    @winrt_mixinmethod
    def GetResultStreamAt(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation, position: UInt64) -> win32more.Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def GetResponseInformation(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferOperation) -> win32more.Windows.Networking.BackgroundTransfer.ResponseInformation: ...
    @winrt_mixinmethod
    def get_Priority(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferOperationPriority) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferPriority: ...
    @winrt_mixinmethod
    def put_Priority(self: win32more.Windows.Networking.BackgroundTransfer.IBackgroundTransferOperationPriority, value: win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferPriority) -> Void: ...
    @winrt_mixinmethod
    def get_TransferGroup(self: win32more.Windows.Networking.BackgroundTransfer.IUploadOperation2) -> win32more.Windows.Networking.BackgroundTransfer.BackgroundTransferGroup: ...
    @winrt_mixinmethod
    def MakeCurrentInTransferGroup(self: win32more.Windows.Networking.BackgroundTransfer.IUploadOperation3) -> Void: ...
    @winrt_mixinmethod
    def SetRequestHeader(self: win32more.Windows.Networking.BackgroundTransfer.IUploadOperation4, headerName: WinRT_String, headerValue: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def RemoveRequestHeader(self: win32more.Windows.Networking.BackgroundTransfer.IUploadOperation4, headerName: WinRT_String) -> Void: ...
    CostPolicy = property(get_CostPolicy, put_CostPolicy)
    Group = property(get_Group, None)
    Guid = property(get_Guid, None)
    Method = property(get_Method, None)
    Priority = property(get_Priority, put_Priority)
    Progress = property(get_Progress, None)
    RequestedUri = property(get_RequestedUri, None)
    SourceFile = property(get_SourceFile, None)
    TransferGroup = property(get_TransferGroup, None)


make_ready(__name__)
