from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Networking
import win32more.Windows.Security.EnterpriseData
import win32more.Windows.Storage
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class BufferProtectUnprotectResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.EnterpriseData.IBufferProtectUnprotectResult
    _classid_ = 'Windows.Security.EnterpriseData.BufferProtectUnprotectResult'
    @winrt_mixinmethod
    def get_Buffer(self: win32more.Windows.Security.EnterpriseData.IBufferProtectUnprotectResult) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_ProtectionInfo(self: win32more.Windows.Security.EnterpriseData.IBufferProtectUnprotectResult) -> win32more.Windows.Security.EnterpriseData.DataProtectionInfo: ...
    Buffer = property(get_Buffer, None)
    ProtectionInfo = property(get_ProtectionInfo, None)
class DataProtectionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.EnterpriseData.IDataProtectionInfo
    _classid_ = 'Windows.Security.EnterpriseData.DataProtectionInfo'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Security.EnterpriseData.IDataProtectionInfo) -> win32more.Windows.Security.EnterpriseData.DataProtectionStatus: ...
    @winrt_mixinmethod
    def get_Identity(self: win32more.Windows.Security.EnterpriseData.IDataProtectionInfo) -> WinRT_String: ...
    Identity = property(get_Identity, None)
    Status = property(get_Status, None)
class DataProtectionManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.DataProtectionManager'
    @winrt_classmethod
    def ProtectAsync(cls: win32more.Windows.Security.EnterpriseData.IDataProtectionManagerStatics, data: win32more.Windows.Storage.Streams.IBuffer, identity: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.BufferProtectUnprotectResult]: ...
    @winrt_classmethod
    def UnprotectAsync(cls: win32more.Windows.Security.EnterpriseData.IDataProtectionManagerStatics, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.BufferProtectUnprotectResult]: ...
    @winrt_classmethod
    def ProtectStreamAsync(cls: win32more.Windows.Security.EnterpriseData.IDataProtectionManagerStatics, unprotectedStream: win32more.Windows.Storage.Streams.IInputStream, identity: WinRT_String, protectedStream: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.DataProtectionInfo]: ...
    @winrt_classmethod
    def UnprotectStreamAsync(cls: win32more.Windows.Security.EnterpriseData.IDataProtectionManagerStatics, protectedStream: win32more.Windows.Storage.Streams.IInputStream, unprotectedStream: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.DataProtectionInfo]: ...
    @winrt_classmethod
    def GetProtectionInfoAsync(cls: win32more.Windows.Security.EnterpriseData.IDataProtectionManagerStatics, protectedData: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.DataProtectionInfo]: ...
    @winrt_classmethod
    def GetStreamProtectionInfoAsync(cls: win32more.Windows.Security.EnterpriseData.IDataProtectionManagerStatics, protectedStream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.DataProtectionInfo]: ...
class DataProtectionStatus(Enum, Int32):
    ProtectedToOtherIdentity = 0
    Protected = 1
    Revoked = 2
    Unprotected = 3
    LicenseExpired = 4
    AccessSuspended = 5
class EnforcementLevel(Enum, Int32):
    NoProtection = 0
    Silent = 1
    Override = 2
    Block = 3
EnterpriseDataContract: UInt32 = 327680
class FileProtectionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.EnterpriseData.IFileProtectionInfo
    _classid_ = 'Windows.Security.EnterpriseData.FileProtectionInfo'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Security.EnterpriseData.IFileProtectionInfo) -> win32more.Windows.Security.EnterpriseData.FileProtectionStatus: ...
    @winrt_mixinmethod
    def get_IsRoamable(self: win32more.Windows.Security.EnterpriseData.IFileProtectionInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_Identity(self: win32more.Windows.Security.EnterpriseData.IFileProtectionInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsProtectWhileOpenSupported(self: win32more.Windows.Security.EnterpriseData.IFileProtectionInfo2) -> Boolean: ...
    Identity = property(get_Identity, None)
    IsProtectWhileOpenSupported = property(get_IsProtectWhileOpenSupported, None)
    IsRoamable = property(get_IsRoamable, None)
    Status = property(get_Status, None)
class FileProtectionManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.FileProtectionManager'
    @winrt_classmethod
    def UnprotectAsync(cls: win32more.Windows.Security.EnterpriseData.IFileProtectionManagerStatics3, target: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.FileProtectionInfo]: ...
    @winrt_classmethod
    def UnprotectWithOptionsAsync(cls: win32more.Windows.Security.EnterpriseData.IFileProtectionManagerStatics3, target: win32more.Windows.Storage.IStorageItem, options: win32more.Windows.Security.EnterpriseData.FileUnprotectOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.FileProtectionInfo]: ...
    @winrt_classmethod
    def IsContainerAsync(cls: win32more.Windows.Security.EnterpriseData.IFileProtectionManagerStatics2, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def LoadFileFromContainerWithTargetAndNameCollisionOptionAsync(cls: win32more.Windows.Security.EnterpriseData.IFileProtectionManagerStatics2, containerFile: win32more.Windows.Storage.IStorageFile, target: win32more.Windows.Storage.IStorageItem, collisionOption: win32more.Windows.Storage.NameCollisionOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectedContainerImportResult]: ...
    @winrt_classmethod
    def SaveFileAsContainerWithSharingAsync(cls: win32more.Windows.Security.EnterpriseData.IFileProtectionManagerStatics2, protectedFile: win32more.Windows.Storage.IStorageFile, sharedWithIdentities: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectedContainerExportResult]: ...
    @winrt_classmethod
    def ProtectAsync(cls: win32more.Windows.Security.EnterpriseData.IFileProtectionManagerStatics, target: win32more.Windows.Storage.IStorageItem, identity: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.FileProtectionInfo]: ...
    @winrt_classmethod
    def CopyProtectionAsync(cls: win32more.Windows.Security.EnterpriseData.IFileProtectionManagerStatics, source: win32more.Windows.Storage.IStorageItem, target: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def GetProtectionInfoAsync(cls: win32more.Windows.Security.EnterpriseData.IFileProtectionManagerStatics, source: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.FileProtectionInfo]: ...
    @winrt_classmethod
    def SaveFileAsContainerAsync(cls: win32more.Windows.Security.EnterpriseData.IFileProtectionManagerStatics, protectedFile: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectedContainerExportResult]: ...
    @winrt_classmethod
    def LoadFileFromContainerAsync(cls: win32more.Windows.Security.EnterpriseData.IFileProtectionManagerStatics, containerFile: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectedContainerImportResult]: ...
    @winrt_classmethod
    def LoadFileFromContainerWithTargetAsync(cls: win32more.Windows.Security.EnterpriseData.IFileProtectionManagerStatics, containerFile: win32more.Windows.Storage.IStorageFile, target: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectedContainerImportResult]: ...
    @winrt_classmethod
    def CreateProtectedAndOpenAsync(cls: win32more.Windows.Security.EnterpriseData.IFileProtectionManagerStatics, parentFolder: win32more.Windows.Storage.IStorageFolder, desiredName: WinRT_String, identity: WinRT_String, collisionOption: win32more.Windows.Storage.CreationCollisionOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectedFileCreateResult]: ...
class FileProtectionStatus(Enum, Int32):
    Undetermined = 0
    Unknown = 0
    Unprotected = 1
    Revoked = 2
    Protected = 3
    ProtectedByOtherUser = 4
    ProtectedToOtherEnterprise = 5
    NotProtectable = 6
    ProtectedToOtherIdentity = 7
    LicenseExpired = 8
    AccessSuspended = 9
    FileInUse = 10
class FileRevocationManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.FileRevocationManager'
    @winrt_classmethod
    def ProtectAsync(cls: win32more.Windows.Security.EnterpriseData.IFileRevocationManagerStatics, storageItem: win32more.Windows.Storage.IStorageItem, enterpriseIdentity: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.FileProtectionStatus]: ...
    @winrt_classmethod
    def CopyProtectionAsync(cls: win32more.Windows.Security.EnterpriseData.IFileRevocationManagerStatics, sourceStorageItem: win32more.Windows.Storage.IStorageItem, targetStorageItem: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def Revoke(cls: win32more.Windows.Security.EnterpriseData.IFileRevocationManagerStatics, enterpriseIdentity: WinRT_String) -> Void: ...
    @winrt_classmethod
    def GetStatusAsync(cls: win32more.Windows.Security.EnterpriseData.IFileRevocationManagerStatics, storageItem: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.FileProtectionStatus]: ...
class FileUnprotectOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.EnterpriseData.IFileUnprotectOptions
    _classid_ = 'Windows.Security.EnterpriseData.FileUnprotectOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Security.EnterpriseData.FileUnprotectOptions.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Security.EnterpriseData.IFileUnprotectOptionsFactory, audit: Boolean) -> win32more.Windows.Security.EnterpriseData.FileUnprotectOptions: ...
    @winrt_mixinmethod
    def put_Audit(self: win32more.Windows.Security.EnterpriseData.IFileUnprotectOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Audit(self: win32more.Windows.Security.EnterpriseData.IFileUnprotectOptions) -> Boolean: ...
    Audit = property(get_Audit, put_Audit)
class IBufferProtectUnprotectResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IBufferProtectUnprotectResult'
    _iid_ = Guid('{47995edc-6cec-4e3a-b251-9e7485d79e7a}')
    @winrt_commethod(6)
    def get_Buffer(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_ProtectionInfo(self) -> win32more.Windows.Security.EnterpriseData.DataProtectionInfo: ...
    Buffer = property(get_Buffer, None)
    ProtectionInfo = property(get_ProtectionInfo, None)
class IDataProtectionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IDataProtectionInfo'
    _iid_ = Guid('{8420b0c1-5e31-4405-9540-3f943af0cb26}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Security.EnterpriseData.DataProtectionStatus: ...
    @winrt_commethod(7)
    def get_Identity(self) -> WinRT_String: ...
    Identity = property(get_Identity, None)
    Status = property(get_Status, None)
class IDataProtectionManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IDataProtectionManagerStatics'
    _iid_ = Guid('{b6149b74-9144-4ee4-8a8a-30b5f361430e}')
    @winrt_commethod(6)
    def ProtectAsync(self, data: win32more.Windows.Storage.Streams.IBuffer, identity: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.BufferProtectUnprotectResult]: ...
    @winrt_commethod(7)
    def UnprotectAsync(self, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.BufferProtectUnprotectResult]: ...
    @winrt_commethod(8)
    def ProtectStreamAsync(self, unprotectedStream: win32more.Windows.Storage.Streams.IInputStream, identity: WinRT_String, protectedStream: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.DataProtectionInfo]: ...
    @winrt_commethod(9)
    def UnprotectStreamAsync(self, protectedStream: win32more.Windows.Storage.Streams.IInputStream, unprotectedStream: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.DataProtectionInfo]: ...
    @winrt_commethod(10)
    def GetProtectionInfoAsync(self, protectedData: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.DataProtectionInfo]: ...
    @winrt_commethod(11)
    def GetStreamProtectionInfoAsync(self, protectedStream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.DataProtectionInfo]: ...
class IFileProtectionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IFileProtectionInfo'
    _iid_ = Guid('{4ee96486-147e-4dd0-8faf-5253ed91ad0c}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Security.EnterpriseData.FileProtectionStatus: ...
    @winrt_commethod(7)
    def get_IsRoamable(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_Identity(self) -> WinRT_String: ...
    Identity = property(get_Identity, None)
    IsRoamable = property(get_IsRoamable, None)
    Status = property(get_Status, None)
class IFileProtectionInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IFileProtectionInfo2'
    _iid_ = Guid('{82123a4c-557a-498d-8e94-944cd5836432}')
    @winrt_commethod(6)
    def get_IsProtectWhileOpenSupported(self) -> Boolean: ...
    IsProtectWhileOpenSupported = property(get_IsProtectWhileOpenSupported, None)
class IFileProtectionManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IFileProtectionManagerStatics'
    _iid_ = Guid('{5846fc9b-e613-426b-bb38-88cba1dc9adb}')
    @winrt_commethod(6)
    def ProtectAsync(self, target: win32more.Windows.Storage.IStorageItem, identity: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.FileProtectionInfo]: ...
    @winrt_commethod(7)
    def CopyProtectionAsync(self, source: win32more.Windows.Storage.IStorageItem, target: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def GetProtectionInfoAsync(self, source: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.FileProtectionInfo]: ...
    @winrt_commethod(9)
    def SaveFileAsContainerAsync(self, protectedFile: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectedContainerExportResult]: ...
    @winrt_commethod(10)
    def LoadFileFromContainerAsync(self, containerFile: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectedContainerImportResult]: ...
    @winrt_commethod(11)
    def LoadFileFromContainerWithTargetAsync(self, containerFile: win32more.Windows.Storage.IStorageFile, target: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectedContainerImportResult]: ...
    @winrt_commethod(12)
    def CreateProtectedAndOpenAsync(self, parentFolder: win32more.Windows.Storage.IStorageFolder, desiredName: WinRT_String, identity: WinRT_String, collisionOption: win32more.Windows.Storage.CreationCollisionOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectedFileCreateResult]: ...
class IFileProtectionManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IFileProtectionManagerStatics2'
    _iid_ = Guid('{83d2a745-0483-41ab-b2d5-bc7f23d74ebb}')
    @winrt_commethod(6)
    def IsContainerAsync(self, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def LoadFileFromContainerWithTargetAndNameCollisionOptionAsync(self, containerFile: win32more.Windows.Storage.IStorageFile, target: win32more.Windows.Storage.IStorageItem, collisionOption: win32more.Windows.Storage.NameCollisionOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectedContainerImportResult]: ...
    @winrt_commethod(8)
    def SaveFileAsContainerWithSharingAsync(self, protectedFile: win32more.Windows.Storage.IStorageFile, sharedWithIdentities: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectedContainerExportResult]: ...
class IFileProtectionManagerStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IFileProtectionManagerStatics3'
    _iid_ = Guid('{6918849a-624f-46d6-b241-e9cd5fdf3e3f}')
    @winrt_commethod(6)
    def UnprotectAsync(self, target: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.FileProtectionInfo]: ...
    @winrt_commethod(7)
    def UnprotectWithOptionsAsync(self, target: win32more.Windows.Storage.IStorageItem, options: win32more.Windows.Security.EnterpriseData.FileUnprotectOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.FileProtectionInfo]: ...
class IFileRevocationManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IFileRevocationManagerStatics'
    _iid_ = Guid('{256bbc3d-1c5d-4260-8c75-9144cfb78ba9}')
    @winrt_commethod(6)
    def ProtectAsync(self, storageItem: win32more.Windows.Storage.IStorageItem, enterpriseIdentity: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.FileProtectionStatus]: ...
    @winrt_commethod(7)
    def CopyProtectionAsync(self, sourceStorageItem: win32more.Windows.Storage.IStorageItem, targetStorageItem: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def Revoke(self, enterpriseIdentity: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def GetStatusAsync(self, storageItem: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.FileProtectionStatus]: ...
class IFileUnprotectOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IFileUnprotectOptions'
    _iid_ = Guid('{7d1312f1-3b0d-4dd8-a1f8-1ec53822e2f3}')
    @winrt_commethod(6)
    def put_Audit(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_Audit(self) -> Boolean: ...
    Audit = property(get_Audit, put_Audit)
class IFileUnprotectOptionsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IFileUnprotectOptionsFactory'
    _iid_ = Guid('{51aeb39c-da8c-4c3f-9bfb-cb73a7cce0dd}')
    @winrt_commethod(6)
    def Create(self, audit: Boolean) -> win32more.Windows.Security.EnterpriseData.FileUnprotectOptions: ...
class IProtectedAccessResumedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectedAccessResumedEventArgs'
    _iid_ = Guid('{ac4dca59-5d80-4e95-8c5f-8539450eebe0}')
    @winrt_commethod(6)
    def get_Identities(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    Identities = property(get_Identities, None)
class IProtectedAccessSuspendingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectedAccessSuspendingEventArgs'
    _iid_ = Guid('{75a193e0-a344-429f-b975-04fc1f88c185}')
    @winrt_commethod(6)
    def get_Identities(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(7)
    def get_Deadline(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Deadline = property(get_Deadline, None)
    Identities = property(get_Identities, None)
class IProtectedContainerExportResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectedContainerExportResult'
    _iid_ = Guid('{3948ef95-f7fb-4b42-afb0-df70b41543c1}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Security.EnterpriseData.ProtectedImportExportStatus: ...
    @winrt_commethod(7)
    def get_File(self) -> win32more.Windows.Storage.StorageFile: ...
    File = property(get_File, None)
    Status = property(get_Status, None)
class IProtectedContainerImportResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectedContainerImportResult'
    _iid_ = Guid('{cdb780d1-e7bb-4d1a-9339-34dc41149f9b}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Security.EnterpriseData.ProtectedImportExportStatus: ...
    @winrt_commethod(7)
    def get_File(self) -> win32more.Windows.Storage.StorageFile: ...
    File = property(get_File, None)
    Status = property(get_Status, None)
class IProtectedContentRevokedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectedContentRevokedEventArgs'
    _iid_ = Guid('{63686821-58b9-47ee-93d9-f0f741cf43f0}')
    @winrt_commethod(6)
    def get_Identities(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    Identities = property(get_Identities, None)
class IProtectedFileCreateResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectedFileCreateResult'
    _iid_ = Guid('{28e3ed6a-e9e7-4a03-9f53-bdb16172699b}')
    @winrt_commethod(6)
    def get_File(self) -> win32more.Windows.Storage.StorageFile: ...
    @winrt_commethod(7)
    def get_Stream(self) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_commethod(8)
    def get_ProtectionInfo(self) -> win32more.Windows.Security.EnterpriseData.FileProtectionInfo: ...
    File = property(get_File, None)
    ProtectionInfo = property(get_ProtectionInfo, None)
    Stream = property(get_Stream, None)
class IProtectionPolicyAuditInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectionPolicyAuditInfo'
    _iid_ = Guid('{425ab7e4-feb7-44fc-b3bb-c3c4d7ecbebb}')
    @winrt_commethod(6)
    def put_Action(self, value: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditAction) -> Void: ...
    @winrt_commethod(7)
    def get_Action(self) -> win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditAction: ...
    @winrt_commethod(8)
    def put_DataDescription(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_DataDescription(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def put_SourceDescription(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def get_SourceDescription(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_TargetDescription(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def get_TargetDescription(self) -> WinRT_String: ...
    Action = property(get_Action, put_Action)
    DataDescription = property(get_DataDescription, put_DataDescription)
    SourceDescription = property(get_SourceDescription, put_SourceDescription)
    TargetDescription = property(get_TargetDescription, put_TargetDescription)
class IProtectionPolicyAuditInfoFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectionPolicyAuditInfoFactory'
    _iid_ = Guid('{7ed4180b-92e8-42d5-83d4-25440b423549}')
    @winrt_commethod(6)
    def Create(self, action: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditAction, dataDescription: WinRT_String, sourceDescription: WinRT_String, targetDescription: WinRT_String) -> win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo: ...
    @winrt_commethod(7)
    def CreateWithActionAndDataDescription(self, action: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditAction, dataDescription: WinRT_String) -> win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo: ...
class IProtectionPolicyManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectionPolicyManager'
    _iid_ = Guid('{d5703e18-a08d-47e6-a240-9934d7165eb5}')
    @winrt_commethod(6)
    def put_Identity(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_Identity(self) -> WinRT_String: ...
    Identity = property(get_Identity, put_Identity)
class IProtectionPolicyManager2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectionPolicyManager2'
    _iid_ = Guid('{abf7527a-8435-417f-99b6-51beaf365888}')
    @winrt_commethod(6)
    def put_ShowEnterpriseIndicator(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_ShowEnterpriseIndicator(self) -> Boolean: ...
    ShowEnterpriseIndicator = property(get_ShowEnterpriseIndicator, put_ShowEnterpriseIndicator)
class IProtectionPolicyManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics'
    _iid_ = Guid('{c0bffc66-8c3d-4d56-8804-c68f0ad32ec5}')
    @winrt_commethod(6)
    def IsIdentityManaged(self, identity: WinRT_String) -> Boolean: ...
    @winrt_commethod(7)
    def TryApplyProcessUIPolicy(self, identity: WinRT_String) -> Boolean: ...
    @winrt_commethod(8)
    def ClearProcessUIPolicy(self) -> Void: ...
    @winrt_commethod(9)
    def CreateCurrentThreadNetworkContext(self, identity: WinRT_String) -> win32more.Windows.Security.EnterpriseData.ThreadNetworkContext: ...
    @winrt_commethod(10)
    def GetPrimaryManagedIdentityForNetworkEndpointAsync(self, endpointHost: win32more.Windows.Networking.HostName) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(11)
    def RevokeContent(self, identity: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def GetForCurrentView(self) -> win32more.Windows.Security.EnterpriseData.ProtectionPolicyManager: ...
    @winrt_commethod(13)
    def add_ProtectedAccessSuspending(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Security.EnterpriseData.ProtectedAccessSuspendingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_ProtectedAccessSuspending(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def add_ProtectedAccessResumed(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Security.EnterpriseData.ProtectedAccessResumedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_ProtectedAccessResumed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_ProtectedContentRevoked(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Security.EnterpriseData.ProtectedContentRevokedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_ProtectedContentRevoked(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def CheckAccess(self, sourceIdentity: WinRT_String, targetIdentity: WinRT_String) -> win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult: ...
    @winrt_commethod(20)
    def RequestAccessAsync(self, sourceIdentity: WinRT_String, targetIdentity: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    ProtectedAccessSuspending = event()
    ProtectedAccessResumed = event()
    ProtectedContentRevoked = event()
class IProtectionPolicyManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics2'
    _iid_ = Guid('{b68f9a8c-39e0-4649-b2e4-070ab8a579b3}')
    @winrt_commethod(6)
    def HasContentBeenRevokedSince(self, identity: WinRT_String, since: win32more.Windows.Foundation.DateTime) -> Boolean: ...
    @winrt_commethod(7)
    def CheckAccessForApp(self, sourceIdentity: WinRT_String, appPackageFamilyName: WinRT_String) -> win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult: ...
    @winrt_commethod(8)
    def RequestAccessForAppAsync(self, sourceIdentity: WinRT_String, appPackageFamilyName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(9)
    def GetEnforcementLevel(self, identity: WinRT_String) -> win32more.Windows.Security.EnterpriseData.EnforcementLevel: ...
    @winrt_commethod(10)
    def IsUserDecryptionAllowed(self, identity: WinRT_String) -> Boolean: ...
    @winrt_commethod(11)
    def IsProtectionUnderLockRequired(self, identity: WinRT_String) -> Boolean: ...
    @winrt_commethod(12)
    def add_PolicyChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_PolicyChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def get_IsProtectionEnabled(self) -> Boolean: ...
    IsProtectionEnabled = property(get_IsProtectionEnabled, None)
    PolicyChanged = event()
class IProtectionPolicyManagerStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics3'
    _iid_ = Guid('{48ff9e8c-6a6f-4d9f-bced-18ab537aa015}')
    @winrt_commethod(6)
    def RequestAccessWithAuditingInfoAsync(self, sourceIdentity: WinRT_String, targetIdentity: WinRT_String, auditInfo: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(7)
    def RequestAccessWithMessageAsync(self, sourceIdentity: WinRT_String, targetIdentity: WinRT_String, auditInfo: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo, messageFromApp: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(8)
    def RequestAccessForAppWithAuditingInfoAsync(self, sourceIdentity: WinRT_String, appPackageFamilyName: WinRT_String, auditInfo: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(9)
    def RequestAccessForAppWithMessageAsync(self, sourceIdentity: WinRT_String, appPackageFamilyName: WinRT_String, auditInfo: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo, messageFromApp: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(10)
    def LogAuditEvent(self, sourceIdentity: WinRT_String, targetIdentity: WinRT_String, auditInfo: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo) -> Void: ...
class IProtectionPolicyManagerStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics4'
    _iid_ = Guid('{20b794db-ccbd-490f-8c83-49ccb77aea6c}')
    @winrt_commethod(6)
    def IsRoamableProtectionEnabled(self, identity: WinRT_String) -> Boolean: ...
    @winrt_commethod(7)
    def RequestAccessWithBehaviorAsync(self, sourceIdentity: WinRT_String, targetIdentity: WinRT_String, auditInfo: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo, messageFromApp: WinRT_String, behavior: win32more.Windows.Security.EnterpriseData.ProtectionPolicyRequestAccessBehavior) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(8)
    def RequestAccessForAppWithBehaviorAsync(self, sourceIdentity: WinRT_String, appPackageFamilyName: WinRT_String, auditInfo: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo, messageFromApp: WinRT_String, behavior: win32more.Windows.Security.EnterpriseData.ProtectionPolicyRequestAccessBehavior) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(9)
    def RequestAccessToFilesForAppAsync(self, sourceItemList: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.IStorageItem], appPackageFamilyName: WinRT_String, auditInfo: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(10)
    def RequestAccessToFilesForAppWithMessageAndBehaviorAsync(self, sourceItemList: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.IStorageItem], appPackageFamilyName: WinRT_String, auditInfo: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo, messageFromApp: WinRT_String, behavior: win32more.Windows.Security.EnterpriseData.ProtectionPolicyRequestAccessBehavior) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(11)
    def RequestAccessToFilesForProcessAsync(self, sourceItemList: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.IStorageItem], processId: UInt32, auditInfo: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(12)
    def RequestAccessToFilesForProcessWithMessageAndBehaviorAsync(self, sourceItemList: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.IStorageItem], processId: UInt32, auditInfo: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo, messageFromApp: WinRT_String, behavior: win32more.Windows.Security.EnterpriseData.ProtectionPolicyRequestAccessBehavior) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(13)
    def IsFileProtectionRequiredAsync(self, target: win32more.Windows.Storage.IStorageItem, identity: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(14)
    def IsFileProtectionRequiredForNewFileAsync(self, parentFolder: win32more.Windows.Storage.IStorageFolder, identity: WinRT_String, desiredName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(15)
    def get_PrimaryManagedIdentity(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def GetPrimaryManagedIdentityForIdentity(self, identity: WinRT_String) -> WinRT_String: ...
    PrimaryManagedIdentity = property(get_PrimaryManagedIdentity, None)
class IThreadNetworkContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IThreadNetworkContext'
    _iid_ = Guid('{fa4ea8e9-ef13-405a-b12c-d7348c6f41fc}')
class ProtectedAccessResumedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.EnterpriseData.IProtectedAccessResumedEventArgs
    _classid_ = 'Windows.Security.EnterpriseData.ProtectedAccessResumedEventArgs'
    @winrt_mixinmethod
    def get_Identities(self: win32more.Windows.Security.EnterpriseData.IProtectedAccessResumedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    Identities = property(get_Identities, None)
class ProtectedAccessSuspendingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.EnterpriseData.IProtectedAccessSuspendingEventArgs
    _classid_ = 'Windows.Security.EnterpriseData.ProtectedAccessSuspendingEventArgs'
    @winrt_mixinmethod
    def get_Identities(self: win32more.Windows.Security.EnterpriseData.IProtectedAccessSuspendingEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Deadline(self: win32more.Windows.Security.EnterpriseData.IProtectedAccessSuspendingEventArgs) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Security.EnterpriseData.IProtectedAccessSuspendingEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Deadline = property(get_Deadline, None)
    Identities = property(get_Identities, None)
class ProtectedContainerExportResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.EnterpriseData.IProtectedContainerExportResult
    _classid_ = 'Windows.Security.EnterpriseData.ProtectedContainerExportResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Security.EnterpriseData.IProtectedContainerExportResult) -> win32more.Windows.Security.EnterpriseData.ProtectedImportExportStatus: ...
    @winrt_mixinmethod
    def get_File(self: win32more.Windows.Security.EnterpriseData.IProtectedContainerExportResult) -> win32more.Windows.Storage.StorageFile: ...
    File = property(get_File, None)
    Status = property(get_Status, None)
class ProtectedContainerImportResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.EnterpriseData.IProtectedContainerImportResult
    _classid_ = 'Windows.Security.EnterpriseData.ProtectedContainerImportResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Security.EnterpriseData.IProtectedContainerImportResult) -> win32more.Windows.Security.EnterpriseData.ProtectedImportExportStatus: ...
    @winrt_mixinmethod
    def get_File(self: win32more.Windows.Security.EnterpriseData.IProtectedContainerImportResult) -> win32more.Windows.Storage.StorageFile: ...
    File = property(get_File, None)
    Status = property(get_Status, None)
class ProtectedContentRevokedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.EnterpriseData.IProtectedContentRevokedEventArgs
    _classid_ = 'Windows.Security.EnterpriseData.ProtectedContentRevokedEventArgs'
    @winrt_mixinmethod
    def get_Identities(self: win32more.Windows.Security.EnterpriseData.IProtectedContentRevokedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    Identities = property(get_Identities, None)
class ProtectedFileCreateResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.EnterpriseData.IProtectedFileCreateResult
    _classid_ = 'Windows.Security.EnterpriseData.ProtectedFileCreateResult'
    @winrt_mixinmethod
    def get_File(self: win32more.Windows.Security.EnterpriseData.IProtectedFileCreateResult) -> win32more.Windows.Storage.StorageFile: ...
    @winrt_mixinmethod
    def get_Stream(self: win32more.Windows.Security.EnterpriseData.IProtectedFileCreateResult) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def get_ProtectionInfo(self: win32more.Windows.Security.EnterpriseData.IProtectedFileCreateResult) -> win32more.Windows.Security.EnterpriseData.FileProtectionInfo: ...
    File = property(get_File, None)
    ProtectionInfo = property(get_ProtectionInfo, None)
    Stream = property(get_Stream, None)
class ProtectedImportExportStatus(Enum, Int32):
    Ok = 0
    Undetermined = 1
    Unprotected = 2
    Revoked = 3
    NotRoamable = 4
    ProtectedToOtherIdentity = 5
    LicenseExpired = 6
    AccessSuspended = 7
class ProtectionPolicyAuditAction(Enum, Int32):
    Decrypt = 0
    CopyToLocation = 1
    SendToRecipient = 2
    Other = 3
class ProtectionPolicyAuditInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.EnterpriseData.IProtectionPolicyAuditInfo
    _classid_ = 'Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo.CreateWithActionAndDataDescription(*args))
        elif len(args) == 4:
            super().__init__(move=win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateWithActionAndDataDescription(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyAuditInfoFactory, action: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditAction, dataDescription: WinRT_String) -> win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyAuditInfoFactory, action: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditAction, dataDescription: WinRT_String, sourceDescription: WinRT_String, targetDescription: WinRT_String) -> win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo: ...
    @winrt_mixinmethod
    def put_Action(self: win32more.Windows.Security.EnterpriseData.IProtectionPolicyAuditInfo, value: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditAction) -> Void: ...
    @winrt_mixinmethod
    def get_Action(self: win32more.Windows.Security.EnterpriseData.IProtectionPolicyAuditInfo) -> win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditAction: ...
    @winrt_mixinmethod
    def put_DataDescription(self: win32more.Windows.Security.EnterpriseData.IProtectionPolicyAuditInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DataDescription(self: win32more.Windows.Security.EnterpriseData.IProtectionPolicyAuditInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SourceDescription(self: win32more.Windows.Security.EnterpriseData.IProtectionPolicyAuditInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SourceDescription(self: win32more.Windows.Security.EnterpriseData.IProtectionPolicyAuditInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetDescription(self: win32more.Windows.Security.EnterpriseData.IProtectionPolicyAuditInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_TargetDescription(self: win32more.Windows.Security.EnterpriseData.IProtectionPolicyAuditInfo) -> WinRT_String: ...
    Action = property(get_Action, put_Action)
    DataDescription = property(get_DataDescription, put_DataDescription)
    SourceDescription = property(get_SourceDescription, put_SourceDescription)
    TargetDescription = property(get_TargetDescription, put_TargetDescription)
class ProtectionPolicyEvaluationResult(Enum, Int32):
    Allowed = 0
    Blocked = 1
    ConsentRequired = 2
class _ProtectionPolicyManager_Meta_(ComPtr.__class__):
    pass
class ProtectionPolicyManager(ComPtr, metaclass=_ProtectionPolicyManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManager
    _classid_ = 'Windows.Security.EnterpriseData.ProtectionPolicyManager'
    @winrt_mixinmethod
    def put_Identity(self: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManager, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Identity(self: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManager) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ShowEnterpriseIndicator(self: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManager2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ShowEnterpriseIndicator(self: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManager2) -> Boolean: ...
    @winrt_classmethod
    def IsRoamableProtectionEnabled(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics4, identity: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def RequestAccessWithBehaviorAsync(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics4, sourceIdentity: WinRT_String, targetIdentity: WinRT_String, auditInfo: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo, messageFromApp: WinRT_String, behavior: win32more.Windows.Security.EnterpriseData.ProtectionPolicyRequestAccessBehavior) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_classmethod
    def RequestAccessForAppWithBehaviorAsync(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics4, sourceIdentity: WinRT_String, appPackageFamilyName: WinRT_String, auditInfo: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo, messageFromApp: WinRT_String, behavior: win32more.Windows.Security.EnterpriseData.ProtectionPolicyRequestAccessBehavior) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_classmethod
    def RequestAccessToFilesForAppAsync(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics4, sourceItemList: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.IStorageItem], appPackageFamilyName: WinRT_String, auditInfo: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_classmethod
    def RequestAccessToFilesForAppWithMessageAndBehaviorAsync(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics4, sourceItemList: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.IStorageItem], appPackageFamilyName: WinRT_String, auditInfo: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo, messageFromApp: WinRT_String, behavior: win32more.Windows.Security.EnterpriseData.ProtectionPolicyRequestAccessBehavior) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_classmethod
    def RequestAccessToFilesForProcessAsync(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics4, sourceItemList: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.IStorageItem], processId: UInt32, auditInfo: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_classmethod
    def RequestAccessToFilesForProcessWithMessageAndBehaviorAsync(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics4, sourceItemList: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Storage.IStorageItem], processId: UInt32, auditInfo: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo, messageFromApp: WinRT_String, behavior: win32more.Windows.Security.EnterpriseData.ProtectionPolicyRequestAccessBehavior) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_classmethod
    def IsFileProtectionRequiredAsync(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics4, target: win32more.Windows.Storage.IStorageItem, identity: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def IsFileProtectionRequiredForNewFileAsync(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics4, parentFolder: win32more.Windows.Storage.IStorageFolder, identity: WinRT_String, desiredName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def get_PrimaryManagedIdentity(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics4) -> WinRT_String: ...
    @winrt_classmethod
    def GetPrimaryManagedIdentityForIdentity(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics4, identity: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def RequestAccessWithAuditingInfoAsync(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics3, sourceIdentity: WinRT_String, targetIdentity: WinRT_String, auditInfo: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_classmethod
    def RequestAccessWithMessageAsync(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics3, sourceIdentity: WinRT_String, targetIdentity: WinRT_String, auditInfo: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo, messageFromApp: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_classmethod
    def RequestAccessForAppWithAuditingInfoAsync(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics3, sourceIdentity: WinRT_String, appPackageFamilyName: WinRT_String, auditInfo: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_classmethod
    def RequestAccessForAppWithMessageAsync(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics3, sourceIdentity: WinRT_String, appPackageFamilyName: WinRT_String, auditInfo: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo, messageFromApp: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_classmethod
    def LogAuditEvent(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics3, sourceIdentity: WinRT_String, targetIdentity: WinRT_String, auditInfo: win32more.Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo) -> Void: ...
    @winrt_classmethod
    def HasContentBeenRevokedSince(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics2, identity: WinRT_String, since: win32more.Windows.Foundation.DateTime) -> Boolean: ...
    @winrt_classmethod
    def CheckAccessForApp(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics2, sourceIdentity: WinRT_String, appPackageFamilyName: WinRT_String) -> win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult: ...
    @winrt_classmethod
    def RequestAccessForAppAsync(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics2, sourceIdentity: WinRT_String, appPackageFamilyName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_classmethod
    def GetEnforcementLevel(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics2, identity: WinRT_String) -> win32more.Windows.Security.EnterpriseData.EnforcementLevel: ...
    @winrt_classmethod
    def IsUserDecryptionAllowed(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics2, identity: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def IsProtectionUnderLockRequired(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics2, identity: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def add_PolicyChanged(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics2, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_PolicyChanged(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_IsProtectionEnabled(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics2) -> Boolean: ...
    @winrt_classmethod
    def IsIdentityManaged(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics, identity: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def TryApplyProcessUIPolicy(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics, identity: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def ClearProcessUIPolicy(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics) -> Void: ...
    @winrt_classmethod
    def CreateCurrentThreadNetworkContext(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics, identity: WinRT_String) -> win32more.Windows.Security.EnterpriseData.ThreadNetworkContext: ...
    @winrt_classmethod
    def GetPrimaryManagedIdentityForNetworkEndpointAsync(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics, endpointHost: win32more.Windows.Networking.HostName) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def RevokeContent(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics, identity: WinRT_String) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics) -> win32more.Windows.Security.EnterpriseData.ProtectionPolicyManager: ...
    @winrt_classmethod
    def add_ProtectedAccessSuspending(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Security.EnterpriseData.ProtectedAccessSuspendingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_ProtectedAccessSuspending(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_ProtectedAccessResumed(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Security.EnterpriseData.ProtectedAccessResumedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_ProtectedAccessResumed(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_ProtectedContentRevoked(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Security.EnterpriseData.ProtectedContentRevokedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_ProtectedContentRevoked(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def CheckAccess(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics, sourceIdentity: WinRT_String, targetIdentity: WinRT_String) -> win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: win32more.Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics, sourceIdentity: WinRT_String, targetIdentity: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    Identity = property(get_Identity, put_Identity)
    ShowEnterpriseIndicator = property(get_ShowEnterpriseIndicator, put_ShowEnterpriseIndicator)
    _ProtectionPolicyManager_Meta_.IsProtectionEnabled = property(get_IsProtectionEnabled, None)
    _ProtectionPolicyManager_Meta_.PrimaryManagedIdentity = property(get_PrimaryManagedIdentity, None)
class ProtectionPolicyRequestAccessBehavior(Enum, Int32):
    Decrypt = 0
    TreatOverridePolicyAsBlock = 1
class ThreadNetworkContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Security.EnterpriseData.IThreadNetworkContext
    _classid_ = 'Windows.Security.EnterpriseData.ThreadNetworkContext'
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...


make_ready(__name__)
