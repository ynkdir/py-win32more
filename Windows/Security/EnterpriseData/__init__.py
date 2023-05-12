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
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Networking
import Windows.Security.EnterpriseData
import Windows.Storage
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
class BufferProtectUnprotectResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.EnterpriseData.IBufferProtectUnprotectResult
    _classid_ = 'Windows.Security.EnterpriseData.BufferProtectUnprotectResult'
    @winrt_mixinmethod
    def get_Buffer(self: Windows.Security.EnterpriseData.IBufferProtectUnprotectResult) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_ProtectionInfo(self: Windows.Security.EnterpriseData.IBufferProtectUnprotectResult) -> Windows.Security.EnterpriseData.DataProtectionInfo: ...
    Buffer = property(get_Buffer, None)
    ProtectionInfo = property(get_ProtectionInfo, None)
class DataProtectionInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.EnterpriseData.IDataProtectionInfo
    _classid_ = 'Windows.Security.EnterpriseData.DataProtectionInfo'
    @winrt_mixinmethod
    def get_Status(self: Windows.Security.EnterpriseData.IDataProtectionInfo) -> Windows.Security.EnterpriseData.DataProtectionStatus: ...
    @winrt_mixinmethod
    def get_Identity(self: Windows.Security.EnterpriseData.IDataProtectionInfo) -> WinRT_String: ...
    Status = property(get_Status, None)
    Identity = property(get_Identity, None)
class DataProtectionManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.DataProtectionManager'
    @winrt_classmethod
    def ProtectAsync(cls: Windows.Security.EnterpriseData.IDataProtectionManagerStatics, data: Windows.Storage.Streams.IBuffer, identity: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.BufferProtectUnprotectResult]: ...
    @winrt_classmethod
    def UnprotectAsync(cls: Windows.Security.EnterpriseData.IDataProtectionManagerStatics, data: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.BufferProtectUnprotectResult]: ...
    @winrt_classmethod
    def ProtectStreamAsync(cls: Windows.Security.EnterpriseData.IDataProtectionManagerStatics, unprotectedStream: Windows.Storage.Streams.IInputStream, identity: WinRT_String, protectedStream: Windows.Storage.Streams.IOutputStream) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.DataProtectionInfo]: ...
    @winrt_classmethod
    def UnprotectStreamAsync(cls: Windows.Security.EnterpriseData.IDataProtectionManagerStatics, protectedStream: Windows.Storage.Streams.IInputStream, unprotectedStream: Windows.Storage.Streams.IOutputStream) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.DataProtectionInfo]: ...
    @winrt_classmethod
    def GetProtectionInfoAsync(cls: Windows.Security.EnterpriseData.IDataProtectionManagerStatics, protectedData: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.DataProtectionInfo]: ...
    @winrt_classmethod
    def GetStreamProtectionInfoAsync(cls: Windows.Security.EnterpriseData.IDataProtectionManagerStatics, protectedStream: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.DataProtectionInfo]: ...
DataProtectionStatus = Int32
DataProtectionStatus_ProtectedToOtherIdentity: DataProtectionStatus = 0
DataProtectionStatus_Protected: DataProtectionStatus = 1
DataProtectionStatus_Revoked: DataProtectionStatus = 2
DataProtectionStatus_Unprotected: DataProtectionStatus = 3
DataProtectionStatus_LicenseExpired: DataProtectionStatus = 4
DataProtectionStatus_AccessSuspended: DataProtectionStatus = 5
EnforcementLevel = Int32
EnforcementLevel_NoProtection: EnforcementLevel = 0
EnforcementLevel_Silent: EnforcementLevel = 1
EnforcementLevel_Override: EnforcementLevel = 2
EnforcementLevel_Block: EnforcementLevel = 3
EnterpriseDataContract: UInt32 = 327680
class FileProtectionInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.EnterpriseData.IFileProtectionInfo
    _classid_ = 'Windows.Security.EnterpriseData.FileProtectionInfo'
    @winrt_mixinmethod
    def get_Status(self: Windows.Security.EnterpriseData.IFileProtectionInfo) -> Windows.Security.EnterpriseData.FileProtectionStatus: ...
    @winrt_mixinmethod
    def get_IsRoamable(self: Windows.Security.EnterpriseData.IFileProtectionInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_Identity(self: Windows.Security.EnterpriseData.IFileProtectionInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsProtectWhileOpenSupported(self: Windows.Security.EnterpriseData.IFileProtectionInfo2) -> Boolean: ...
    Status = property(get_Status, None)
    IsRoamable = property(get_IsRoamable, None)
    Identity = property(get_Identity, None)
    IsProtectWhileOpenSupported = property(get_IsProtectWhileOpenSupported, None)
class FileProtectionManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.FileProtectionManager'
    @winrt_classmethod
    def UnprotectAsync(cls: Windows.Security.EnterpriseData.IFileProtectionManagerStatics3, target: Windows.Storage.IStorageItem) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.FileProtectionInfo]: ...
    @winrt_classmethod
    def UnprotectWithOptionsAsync(cls: Windows.Security.EnterpriseData.IFileProtectionManagerStatics3, target: Windows.Storage.IStorageItem, options: Windows.Security.EnterpriseData.FileUnprotectOptions) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.FileProtectionInfo]: ...
    @winrt_classmethod
    def IsContainerAsync(cls: Windows.Security.EnterpriseData.IFileProtectionManagerStatics2, file: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def LoadFileFromContainerWithTargetAndNameCollisionOptionAsync(cls: Windows.Security.EnterpriseData.IFileProtectionManagerStatics2, containerFile: Windows.Storage.IStorageFile, target: Windows.Storage.IStorageItem, collisionOption: Windows.Storage.NameCollisionOption) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectedContainerImportResult]: ...
    @winrt_classmethod
    def SaveFileAsContainerWithSharingAsync(cls: Windows.Security.EnterpriseData.IFileProtectionManagerStatics2, protectedFile: Windows.Storage.IStorageFile, sharedWithIdentities: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectedContainerExportResult]: ...
    @winrt_classmethod
    def ProtectAsync(cls: Windows.Security.EnterpriseData.IFileProtectionManagerStatics, target: Windows.Storage.IStorageItem, identity: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.FileProtectionInfo]: ...
    @winrt_classmethod
    def CopyProtectionAsync(cls: Windows.Security.EnterpriseData.IFileProtectionManagerStatics, source: Windows.Storage.IStorageItem, target: Windows.Storage.IStorageItem) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def GetProtectionInfoAsync(cls: Windows.Security.EnterpriseData.IFileProtectionManagerStatics, source: Windows.Storage.IStorageItem) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.FileProtectionInfo]: ...
    @winrt_classmethod
    def SaveFileAsContainerAsync(cls: Windows.Security.EnterpriseData.IFileProtectionManagerStatics, protectedFile: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectedContainerExportResult]: ...
    @winrt_classmethod
    def LoadFileFromContainerAsync(cls: Windows.Security.EnterpriseData.IFileProtectionManagerStatics, containerFile: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectedContainerImportResult]: ...
    @winrt_classmethod
    def LoadFileFromContainerWithTargetAsync(cls: Windows.Security.EnterpriseData.IFileProtectionManagerStatics, containerFile: Windows.Storage.IStorageFile, target: Windows.Storage.IStorageItem) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectedContainerImportResult]: ...
    @winrt_classmethod
    def CreateProtectedAndOpenAsync(cls: Windows.Security.EnterpriseData.IFileProtectionManagerStatics, parentFolder: Windows.Storage.IStorageFolder, desiredName: WinRT_String, identity: WinRT_String, collisionOption: Windows.Storage.CreationCollisionOption) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectedFileCreateResult]: ...
FileProtectionStatus = Int32
FileProtectionStatus_Undetermined: FileProtectionStatus = 0
FileProtectionStatus_Unknown: FileProtectionStatus = 0
FileProtectionStatus_Unprotected: FileProtectionStatus = 1
FileProtectionStatus_Revoked: FileProtectionStatus = 2
FileProtectionStatus_Protected: FileProtectionStatus = 3
FileProtectionStatus_ProtectedByOtherUser: FileProtectionStatus = 4
FileProtectionStatus_ProtectedToOtherEnterprise: FileProtectionStatus = 5
FileProtectionStatus_NotProtectable: FileProtectionStatus = 6
FileProtectionStatus_ProtectedToOtherIdentity: FileProtectionStatus = 7
FileProtectionStatus_LicenseExpired: FileProtectionStatus = 8
FileProtectionStatus_AccessSuspended: FileProtectionStatus = 9
FileProtectionStatus_FileInUse: FileProtectionStatus = 10
class FileRevocationManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.FileRevocationManager'
    @winrt_classmethod
    def ProtectAsync(cls: Windows.Security.EnterpriseData.IFileRevocationManagerStatics, storageItem: Windows.Storage.IStorageItem, enterpriseIdentity: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.FileProtectionStatus]: ...
    @winrt_classmethod
    def CopyProtectionAsync(cls: Windows.Security.EnterpriseData.IFileRevocationManagerStatics, sourceStorageItem: Windows.Storage.IStorageItem, targetStorageItem: Windows.Storage.IStorageItem) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def Revoke(cls: Windows.Security.EnterpriseData.IFileRevocationManagerStatics, enterpriseIdentity: WinRT_String) -> Void: ...
    @winrt_classmethod
    def GetStatusAsync(cls: Windows.Security.EnterpriseData.IFileRevocationManagerStatics, storageItem: Windows.Storage.IStorageItem) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.FileProtectionStatus]: ...
class FileUnprotectOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.EnterpriseData.IFileUnprotectOptions
    _classid_ = 'Windows.Security.EnterpriseData.FileUnprotectOptions'
    @winrt_factorymethod
    def Create(cls: Windows.Security.EnterpriseData.IFileUnprotectOptionsFactory, audit: Boolean) -> Windows.Security.EnterpriseData.FileUnprotectOptions: ...
    @winrt_mixinmethod
    def put_Audit(self: Windows.Security.EnterpriseData.IFileUnprotectOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Audit(self: Windows.Security.EnterpriseData.IFileUnprotectOptions) -> Boolean: ...
    Audit = property(get_Audit, put_Audit)
class IBufferProtectUnprotectResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IBufferProtectUnprotectResult'
    _iid_ = Guid('{47995edc-6cec-4e3a-b251-9e7485d79e7a}')
    @winrt_commethod(6)
    def get_Buffer(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_ProtectionInfo(self) -> Windows.Security.EnterpriseData.DataProtectionInfo: ...
    Buffer = property(get_Buffer, None)
    ProtectionInfo = property(get_ProtectionInfo, None)
class IDataProtectionInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IDataProtectionInfo'
    _iid_ = Guid('{8420b0c1-5e31-4405-9540-3f943af0cb26}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Security.EnterpriseData.DataProtectionStatus: ...
    @winrt_commethod(7)
    def get_Identity(self) -> WinRT_String: ...
    Status = property(get_Status, None)
    Identity = property(get_Identity, None)
class IDataProtectionManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IDataProtectionManagerStatics'
    _iid_ = Guid('{b6149b74-9144-4ee4-8a8a-30b5f361430e}')
    @winrt_commethod(6)
    def ProtectAsync(self, data: Windows.Storage.Streams.IBuffer, identity: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.BufferProtectUnprotectResult]: ...
    @winrt_commethod(7)
    def UnprotectAsync(self, data: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.BufferProtectUnprotectResult]: ...
    @winrt_commethod(8)
    def ProtectStreamAsync(self, unprotectedStream: Windows.Storage.Streams.IInputStream, identity: WinRT_String, protectedStream: Windows.Storage.Streams.IOutputStream) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.DataProtectionInfo]: ...
    @winrt_commethod(9)
    def UnprotectStreamAsync(self, protectedStream: Windows.Storage.Streams.IInputStream, unprotectedStream: Windows.Storage.Streams.IOutputStream) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.DataProtectionInfo]: ...
    @winrt_commethod(10)
    def GetProtectionInfoAsync(self, protectedData: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.DataProtectionInfo]: ...
    @winrt_commethod(11)
    def GetStreamProtectionInfoAsync(self, protectedStream: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.DataProtectionInfo]: ...
class IFileProtectionInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IFileProtectionInfo'
    _iid_ = Guid('{4ee96486-147e-4dd0-8faf-5253ed91ad0c}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Security.EnterpriseData.FileProtectionStatus: ...
    @winrt_commethod(7)
    def get_IsRoamable(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_Identity(self) -> WinRT_String: ...
    Status = property(get_Status, None)
    IsRoamable = property(get_IsRoamable, None)
    Identity = property(get_Identity, None)
class IFileProtectionInfo2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IFileProtectionInfo2'
    _iid_ = Guid('{82123a4c-557a-498d-8e94-944cd5836432}')
    @winrt_commethod(6)
    def get_IsProtectWhileOpenSupported(self) -> Boolean: ...
    IsProtectWhileOpenSupported = property(get_IsProtectWhileOpenSupported, None)
class IFileProtectionManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IFileProtectionManagerStatics'
    _iid_ = Guid('{5846fc9b-e613-426b-bb38-88cba1dc9adb}')
    @winrt_commethod(6)
    def ProtectAsync(self, target: Windows.Storage.IStorageItem, identity: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.FileProtectionInfo]: ...
    @winrt_commethod(7)
    def CopyProtectionAsync(self, source: Windows.Storage.IStorageItem, target: Windows.Storage.IStorageItem) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def GetProtectionInfoAsync(self, source: Windows.Storage.IStorageItem) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.FileProtectionInfo]: ...
    @winrt_commethod(9)
    def SaveFileAsContainerAsync(self, protectedFile: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectedContainerExportResult]: ...
    @winrt_commethod(10)
    def LoadFileFromContainerAsync(self, containerFile: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectedContainerImportResult]: ...
    @winrt_commethod(11)
    def LoadFileFromContainerWithTargetAsync(self, containerFile: Windows.Storage.IStorageFile, target: Windows.Storage.IStorageItem) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectedContainerImportResult]: ...
    @winrt_commethod(12)
    def CreateProtectedAndOpenAsync(self, parentFolder: Windows.Storage.IStorageFolder, desiredName: WinRT_String, identity: WinRT_String, collisionOption: Windows.Storage.CreationCollisionOption) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectedFileCreateResult]: ...
class IFileProtectionManagerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IFileProtectionManagerStatics2'
    _iid_ = Guid('{83d2a745-0483-41ab-b2d5-bc7f23d74ebb}')
    @winrt_commethod(6)
    def IsContainerAsync(self, file: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def LoadFileFromContainerWithTargetAndNameCollisionOptionAsync(self, containerFile: Windows.Storage.IStorageFile, target: Windows.Storage.IStorageItem, collisionOption: Windows.Storage.NameCollisionOption) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectedContainerImportResult]: ...
    @winrt_commethod(8)
    def SaveFileAsContainerWithSharingAsync(self, protectedFile: Windows.Storage.IStorageFile, sharedWithIdentities: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectedContainerExportResult]: ...
class IFileProtectionManagerStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IFileProtectionManagerStatics3'
    _iid_ = Guid('{6918849a-624f-46d6-b241-e9cd5fdf3e3f}')
    @winrt_commethod(6)
    def UnprotectAsync(self, target: Windows.Storage.IStorageItem) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.FileProtectionInfo]: ...
    @winrt_commethod(7)
    def UnprotectWithOptionsAsync(self, target: Windows.Storage.IStorageItem, options: Windows.Security.EnterpriseData.FileUnprotectOptions) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.FileProtectionInfo]: ...
class IFileRevocationManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IFileRevocationManagerStatics'
    _iid_ = Guid('{256bbc3d-1c5d-4260-8c75-9144cfb78ba9}')
    @winrt_commethod(6)
    def ProtectAsync(self, storageItem: Windows.Storage.IStorageItem, enterpriseIdentity: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.FileProtectionStatus]: ...
    @winrt_commethod(7)
    def CopyProtectionAsync(self, sourceStorageItem: Windows.Storage.IStorageItem, targetStorageItem: Windows.Storage.IStorageItem) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def Revoke(self, enterpriseIdentity: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def GetStatusAsync(self, storageItem: Windows.Storage.IStorageItem) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.FileProtectionStatus]: ...
class IFileUnprotectOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IFileUnprotectOptions'
    _iid_ = Guid('{7d1312f1-3b0d-4dd8-a1f8-1ec53822e2f3}')
    @winrt_commethod(6)
    def put_Audit(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_Audit(self) -> Boolean: ...
    Audit = property(get_Audit, put_Audit)
class IFileUnprotectOptionsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IFileUnprotectOptionsFactory'
    _iid_ = Guid('{51aeb39c-da8c-4c3f-9bfb-cb73a7cce0dd}')
    @winrt_commethod(6)
    def Create(self, audit: Boolean) -> Windows.Security.EnterpriseData.FileUnprotectOptions: ...
class IProtectedAccessResumedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectedAccessResumedEventArgs'
    _iid_ = Guid('{ac4dca59-5d80-4e95-8c5f-8539450eebe0}')
    @winrt_commethod(6)
    def get_Identities(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    Identities = property(get_Identities, None)
class IProtectedAccessSuspendingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectedAccessSuspendingEventArgs'
    _iid_ = Guid('{75a193e0-a344-429f-b975-04fc1f88c185}')
    @winrt_commethod(6)
    def get_Identities(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(7)
    def get_Deadline(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Identities = property(get_Identities, None)
    Deadline = property(get_Deadline, None)
class IProtectedContainerExportResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectedContainerExportResult'
    _iid_ = Guid('{3948ef95-f7fb-4b42-afb0-df70b41543c1}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Security.EnterpriseData.ProtectedImportExportStatus: ...
    @winrt_commethod(7)
    def get_File(self) -> Windows.Storage.StorageFile: ...
    Status = property(get_Status, None)
    File = property(get_File, None)
class IProtectedContainerImportResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectedContainerImportResult'
    _iid_ = Guid('{cdb780d1-e7bb-4d1a-9339-34dc41149f9b}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Security.EnterpriseData.ProtectedImportExportStatus: ...
    @winrt_commethod(7)
    def get_File(self) -> Windows.Storage.StorageFile: ...
    Status = property(get_Status, None)
    File = property(get_File, None)
class IProtectedContentRevokedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectedContentRevokedEventArgs'
    _iid_ = Guid('{63686821-58b9-47ee-93d9-f0f741cf43f0}')
    @winrt_commethod(6)
    def get_Identities(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    Identities = property(get_Identities, None)
class IProtectedFileCreateResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectedFileCreateResult'
    _iid_ = Guid('{28e3ed6a-e9e7-4a03-9f53-bdb16172699b}')
    @winrt_commethod(6)
    def get_File(self) -> Windows.Storage.StorageFile: ...
    @winrt_commethod(7)
    def get_Stream(self) -> Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_commethod(8)
    def get_ProtectionInfo(self) -> Windows.Security.EnterpriseData.FileProtectionInfo: ...
    File = property(get_File, None)
    Stream = property(get_Stream, None)
    ProtectionInfo = property(get_ProtectionInfo, None)
class IProtectionPolicyAuditInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectionPolicyAuditInfo'
    _iid_ = Guid('{425ab7e4-feb7-44fc-b3bb-c3c4d7ecbebb}')
    @winrt_commethod(6)
    def put_Action(self, value: Windows.Security.EnterpriseData.ProtectionPolicyAuditAction) -> Void: ...
    @winrt_commethod(7)
    def get_Action(self) -> Windows.Security.EnterpriseData.ProtectionPolicyAuditAction: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectionPolicyAuditInfoFactory'
    _iid_ = Guid('{7ed4180b-92e8-42d5-83d4-25440b423549}')
    @winrt_commethod(6)
    def Create(self, action: Windows.Security.EnterpriseData.ProtectionPolicyAuditAction, dataDescription: WinRT_String, sourceDescription: WinRT_String, targetDescription: WinRT_String) -> Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo: ...
    @winrt_commethod(7)
    def CreateWithActionAndDataDescription(self, action: Windows.Security.EnterpriseData.ProtectionPolicyAuditAction, dataDescription: WinRT_String) -> Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo: ...
class IProtectionPolicyManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectionPolicyManager'
    _iid_ = Guid('{d5703e18-a08d-47e6-a240-9934d7165eb5}')
    @winrt_commethod(6)
    def put_Identity(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_Identity(self) -> WinRT_String: ...
    Identity = property(get_Identity, put_Identity)
class IProtectionPolicyManager2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectionPolicyManager2'
    _iid_ = Guid('{abf7527a-8435-417f-99b6-51beaf365888}')
    @winrt_commethod(6)
    def put_ShowEnterpriseIndicator(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_ShowEnterpriseIndicator(self) -> Boolean: ...
    ShowEnterpriseIndicator = property(get_ShowEnterpriseIndicator, put_ShowEnterpriseIndicator)
class IProtectionPolicyManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics'
    _iid_ = Guid('{c0bffc66-8c3d-4d56-8804-c68f0ad32ec5}')
    @winrt_commethod(6)
    def IsIdentityManaged(self, identity: WinRT_String) -> Boolean: ...
    @winrt_commethod(7)
    def TryApplyProcessUIPolicy(self, identity: WinRT_String) -> Boolean: ...
    @winrt_commethod(8)
    def ClearProcessUIPolicy(self) -> Void: ...
    @winrt_commethod(9)
    def CreateCurrentThreadNetworkContext(self, identity: WinRT_String) -> Windows.Security.EnterpriseData.ThreadNetworkContext: ...
    @winrt_commethod(10)
    def GetPrimaryManagedIdentityForNetworkEndpointAsync(self, endpointHost: Windows.Networking.HostName) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(11)
    def RevokeContent(self, identity: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def GetForCurrentView(self) -> Windows.Security.EnterpriseData.ProtectionPolicyManager: ...
    @winrt_commethod(13)
    def add_ProtectedAccessSuspending(self, handler: Windows.Foundation.EventHandler[Windows.Security.EnterpriseData.ProtectedAccessSuspendingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_ProtectedAccessSuspending(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def add_ProtectedAccessResumed(self, handler: Windows.Foundation.EventHandler[Windows.Security.EnterpriseData.ProtectedAccessResumedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_ProtectedAccessResumed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_ProtectedContentRevoked(self, handler: Windows.Foundation.EventHandler[Windows.Security.EnterpriseData.ProtectedContentRevokedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_ProtectedContentRevoked(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def CheckAccess(self, sourceIdentity: WinRT_String, targetIdentity: WinRT_String) -> Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult: ...
    @winrt_commethod(20)
    def RequestAccessAsync(self, sourceIdentity: WinRT_String, targetIdentity: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
class IProtectionPolicyManagerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics2'
    _iid_ = Guid('{b68f9a8c-39e0-4649-b2e4-070ab8a579b3}')
    @winrt_commethod(6)
    def HasContentBeenRevokedSince(self, identity: WinRT_String, since: Windows.Foundation.DateTime) -> Boolean: ...
    @winrt_commethod(7)
    def CheckAccessForApp(self, sourceIdentity: WinRT_String, appPackageFamilyName: WinRT_String) -> Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult: ...
    @winrt_commethod(8)
    def RequestAccessForAppAsync(self, sourceIdentity: WinRT_String, appPackageFamilyName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(9)
    def GetEnforcementLevel(self, identity: WinRT_String) -> Windows.Security.EnterpriseData.EnforcementLevel: ...
    @winrt_commethod(10)
    def IsUserDecryptionAllowed(self, identity: WinRT_String) -> Boolean: ...
    @winrt_commethod(11)
    def IsProtectionUnderLockRequired(self, identity: WinRT_String) -> Boolean: ...
    @winrt_commethod(12)
    def add_PolicyChanged(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_PolicyChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def get_IsProtectionEnabled(self) -> Boolean: ...
    IsProtectionEnabled = property(get_IsProtectionEnabled, None)
class IProtectionPolicyManagerStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics3'
    _iid_ = Guid('{48ff9e8c-6a6f-4d9f-bced-18ab537aa015}')
    @winrt_commethod(6)
    def RequestAccessWithAuditingInfoAsync(self, sourceIdentity: WinRT_String, targetIdentity: WinRT_String, auditInfo: Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(7)
    def RequestAccessWithMessageAsync(self, sourceIdentity: WinRT_String, targetIdentity: WinRT_String, auditInfo: Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo, messageFromApp: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(8)
    def RequestAccessForAppWithAuditingInfoAsync(self, sourceIdentity: WinRT_String, appPackageFamilyName: WinRT_String, auditInfo: Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(9)
    def RequestAccessForAppWithMessageAsync(self, sourceIdentity: WinRT_String, appPackageFamilyName: WinRT_String, auditInfo: Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo, messageFromApp: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(10)
    def LogAuditEvent(self, sourceIdentity: WinRT_String, targetIdentity: WinRT_String, auditInfo: Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo) -> Void: ...
class IProtectionPolicyManagerStatics4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics4'
    _iid_ = Guid('{20b794db-ccbd-490f-8c83-49ccb77aea6c}')
    @winrt_commethod(6)
    def IsRoamableProtectionEnabled(self, identity: WinRT_String) -> Boolean: ...
    @winrt_commethod(7)
    def RequestAccessWithBehaviorAsync(self, sourceIdentity: WinRT_String, targetIdentity: WinRT_String, auditInfo: Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo, messageFromApp: WinRT_String, behavior: Windows.Security.EnterpriseData.ProtectionPolicyRequestAccessBehavior) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(8)
    def RequestAccessForAppWithBehaviorAsync(self, sourceIdentity: WinRT_String, appPackageFamilyName: WinRT_String, auditInfo: Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo, messageFromApp: WinRT_String, behavior: Windows.Security.EnterpriseData.ProtectionPolicyRequestAccessBehavior) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(9)
    def RequestAccessToFilesForAppAsync(self, sourceItemList: Windows.Foundation.Collections.IIterable[Windows.Storage.IStorageItem], appPackageFamilyName: WinRT_String, auditInfo: Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(10)
    def RequestAccessToFilesForAppWithMessageAndBehaviorAsync(self, sourceItemList: Windows.Foundation.Collections.IIterable[Windows.Storage.IStorageItem], appPackageFamilyName: WinRT_String, auditInfo: Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo, messageFromApp: WinRT_String, behavior: Windows.Security.EnterpriseData.ProtectionPolicyRequestAccessBehavior) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(11)
    def RequestAccessToFilesForProcessAsync(self, sourceItemList: Windows.Foundation.Collections.IIterable[Windows.Storage.IStorageItem], processId: UInt32, auditInfo: Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(12)
    def RequestAccessToFilesForProcessWithMessageAndBehaviorAsync(self, sourceItemList: Windows.Foundation.Collections.IIterable[Windows.Storage.IStorageItem], processId: UInt32, auditInfo: Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo, messageFromApp: WinRT_String, behavior: Windows.Security.EnterpriseData.ProtectionPolicyRequestAccessBehavior) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_commethod(13)
    def IsFileProtectionRequiredAsync(self, target: Windows.Storage.IStorageItem, identity: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(14)
    def IsFileProtectionRequiredForNewFileAsync(self, parentFolder: Windows.Storage.IStorageFolder, identity: WinRT_String, desiredName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(15)
    def get_PrimaryManagedIdentity(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def GetPrimaryManagedIdentityForIdentity(self, identity: WinRT_String) -> WinRT_String: ...
    PrimaryManagedIdentity = property(get_PrimaryManagedIdentity, None)
class IThreadNetworkContext(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.EnterpriseData.IThreadNetworkContext'
    _iid_ = Guid('{fa4ea8e9-ef13-405a-b12c-d7348c6f41fc}')
class ProtectedAccessResumedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.EnterpriseData.IProtectedAccessResumedEventArgs
    _classid_ = 'Windows.Security.EnterpriseData.ProtectedAccessResumedEventArgs'
    @winrt_mixinmethod
    def get_Identities(self: Windows.Security.EnterpriseData.IProtectedAccessResumedEventArgs) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    Identities = property(get_Identities, None)
class ProtectedAccessSuspendingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.EnterpriseData.IProtectedAccessSuspendingEventArgs
    _classid_ = 'Windows.Security.EnterpriseData.ProtectedAccessSuspendingEventArgs'
    @winrt_mixinmethod
    def get_Identities(self: Windows.Security.EnterpriseData.IProtectedAccessSuspendingEventArgs) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Deadline(self: Windows.Security.EnterpriseData.IProtectedAccessSuspendingEventArgs) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Security.EnterpriseData.IProtectedAccessSuspendingEventArgs) -> Windows.Foundation.Deferral: ...
    Identities = property(get_Identities, None)
    Deadline = property(get_Deadline, None)
class ProtectedContainerExportResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.EnterpriseData.IProtectedContainerExportResult
    _classid_ = 'Windows.Security.EnterpriseData.ProtectedContainerExportResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Security.EnterpriseData.IProtectedContainerExportResult) -> Windows.Security.EnterpriseData.ProtectedImportExportStatus: ...
    @winrt_mixinmethod
    def get_File(self: Windows.Security.EnterpriseData.IProtectedContainerExportResult) -> Windows.Storage.StorageFile: ...
    Status = property(get_Status, None)
    File = property(get_File, None)
class ProtectedContainerImportResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.EnterpriseData.IProtectedContainerImportResult
    _classid_ = 'Windows.Security.EnterpriseData.ProtectedContainerImportResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Security.EnterpriseData.IProtectedContainerImportResult) -> Windows.Security.EnterpriseData.ProtectedImportExportStatus: ...
    @winrt_mixinmethod
    def get_File(self: Windows.Security.EnterpriseData.IProtectedContainerImportResult) -> Windows.Storage.StorageFile: ...
    Status = property(get_Status, None)
    File = property(get_File, None)
class ProtectedContentRevokedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.EnterpriseData.IProtectedContentRevokedEventArgs
    _classid_ = 'Windows.Security.EnterpriseData.ProtectedContentRevokedEventArgs'
    @winrt_mixinmethod
    def get_Identities(self: Windows.Security.EnterpriseData.IProtectedContentRevokedEventArgs) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    Identities = property(get_Identities, None)
class ProtectedFileCreateResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.EnterpriseData.IProtectedFileCreateResult
    _classid_ = 'Windows.Security.EnterpriseData.ProtectedFileCreateResult'
    @winrt_mixinmethod
    def get_File(self: Windows.Security.EnterpriseData.IProtectedFileCreateResult) -> Windows.Storage.StorageFile: ...
    @winrt_mixinmethod
    def get_Stream(self: Windows.Security.EnterpriseData.IProtectedFileCreateResult) -> Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def get_ProtectionInfo(self: Windows.Security.EnterpriseData.IProtectedFileCreateResult) -> Windows.Security.EnterpriseData.FileProtectionInfo: ...
    File = property(get_File, None)
    Stream = property(get_Stream, None)
    ProtectionInfo = property(get_ProtectionInfo, None)
ProtectedImportExportStatus = Int32
ProtectedImportExportStatus_Ok: ProtectedImportExportStatus = 0
ProtectedImportExportStatus_Undetermined: ProtectedImportExportStatus = 1
ProtectedImportExportStatus_Unprotected: ProtectedImportExportStatus = 2
ProtectedImportExportStatus_Revoked: ProtectedImportExportStatus = 3
ProtectedImportExportStatus_NotRoamable: ProtectedImportExportStatus = 4
ProtectedImportExportStatus_ProtectedToOtherIdentity: ProtectedImportExportStatus = 5
ProtectedImportExportStatus_LicenseExpired: ProtectedImportExportStatus = 6
ProtectedImportExportStatus_AccessSuspended: ProtectedImportExportStatus = 7
ProtectionPolicyAuditAction = Int32
ProtectionPolicyAuditAction_Decrypt: ProtectionPolicyAuditAction = 0
ProtectionPolicyAuditAction_CopyToLocation: ProtectionPolicyAuditAction = 1
ProtectionPolicyAuditAction_SendToRecipient: ProtectionPolicyAuditAction = 2
ProtectionPolicyAuditAction_Other: ProtectionPolicyAuditAction = 3
class ProtectionPolicyAuditInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.EnterpriseData.IProtectionPolicyAuditInfo
    _classid_ = 'Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo'
    @winrt_factorymethod
    def Create(cls: Windows.Security.EnterpriseData.IProtectionPolicyAuditInfoFactory, action: Windows.Security.EnterpriseData.ProtectionPolicyAuditAction, dataDescription: WinRT_String, sourceDescription: WinRT_String, targetDescription: WinRT_String) -> Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo: ...
    @winrt_factorymethod
    def CreateWithActionAndDataDescription(cls: Windows.Security.EnterpriseData.IProtectionPolicyAuditInfoFactory, action: Windows.Security.EnterpriseData.ProtectionPolicyAuditAction, dataDescription: WinRT_String) -> Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo: ...
    @winrt_mixinmethod
    def put_Action(self: Windows.Security.EnterpriseData.IProtectionPolicyAuditInfo, value: Windows.Security.EnterpriseData.ProtectionPolicyAuditAction) -> Void: ...
    @winrt_mixinmethod
    def get_Action(self: Windows.Security.EnterpriseData.IProtectionPolicyAuditInfo) -> Windows.Security.EnterpriseData.ProtectionPolicyAuditAction: ...
    @winrt_mixinmethod
    def put_DataDescription(self: Windows.Security.EnterpriseData.IProtectionPolicyAuditInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DataDescription(self: Windows.Security.EnterpriseData.IProtectionPolicyAuditInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SourceDescription(self: Windows.Security.EnterpriseData.IProtectionPolicyAuditInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SourceDescription(self: Windows.Security.EnterpriseData.IProtectionPolicyAuditInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetDescription(self: Windows.Security.EnterpriseData.IProtectionPolicyAuditInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_TargetDescription(self: Windows.Security.EnterpriseData.IProtectionPolicyAuditInfo) -> WinRT_String: ...
    Action = property(get_Action, put_Action)
    DataDescription = property(get_DataDescription, put_DataDescription)
    SourceDescription = property(get_SourceDescription, put_SourceDescription)
    TargetDescription = property(get_TargetDescription, put_TargetDescription)
ProtectionPolicyEvaluationResult = Int32
ProtectionPolicyEvaluationResult_Allowed: ProtectionPolicyEvaluationResult = 0
ProtectionPolicyEvaluationResult_Blocked: ProtectionPolicyEvaluationResult = 1
ProtectionPolicyEvaluationResult_ConsentRequired: ProtectionPolicyEvaluationResult = 2
class _ProtectionPolicyManager_Meta_(ComPtr.__class__):
    pass
class ProtectionPolicyManager(ComPtr, metaclass=_ProtectionPolicyManager_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.EnterpriseData.IProtectionPolicyManager
    _classid_ = 'Windows.Security.EnterpriseData.ProtectionPolicyManager'
    @winrt_mixinmethod
    def put_Identity(self: Windows.Security.EnterpriseData.IProtectionPolicyManager, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Identity(self: Windows.Security.EnterpriseData.IProtectionPolicyManager) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ShowEnterpriseIndicator(self: Windows.Security.EnterpriseData.IProtectionPolicyManager2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ShowEnterpriseIndicator(self: Windows.Security.EnterpriseData.IProtectionPolicyManager2) -> Boolean: ...
    @winrt_classmethod
    def IsRoamableProtectionEnabled(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics4, identity: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def RequestAccessWithBehaviorAsync(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics4, sourceIdentity: WinRT_String, targetIdentity: WinRT_String, auditInfo: Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo, messageFromApp: WinRT_String, behavior: Windows.Security.EnterpriseData.ProtectionPolicyRequestAccessBehavior) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_classmethod
    def RequestAccessForAppWithBehaviorAsync(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics4, sourceIdentity: WinRT_String, appPackageFamilyName: WinRT_String, auditInfo: Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo, messageFromApp: WinRT_String, behavior: Windows.Security.EnterpriseData.ProtectionPolicyRequestAccessBehavior) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_classmethod
    def RequestAccessToFilesForAppAsync(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics4, sourceItemList: Windows.Foundation.Collections.IIterable[Windows.Storage.IStorageItem], appPackageFamilyName: WinRT_String, auditInfo: Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_classmethod
    def RequestAccessToFilesForAppWithMessageAndBehaviorAsync(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics4, sourceItemList: Windows.Foundation.Collections.IIterable[Windows.Storage.IStorageItem], appPackageFamilyName: WinRT_String, auditInfo: Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo, messageFromApp: WinRT_String, behavior: Windows.Security.EnterpriseData.ProtectionPolicyRequestAccessBehavior) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_classmethod
    def RequestAccessToFilesForProcessAsync(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics4, sourceItemList: Windows.Foundation.Collections.IIterable[Windows.Storage.IStorageItem], processId: UInt32, auditInfo: Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_classmethod
    def RequestAccessToFilesForProcessWithMessageAndBehaviorAsync(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics4, sourceItemList: Windows.Foundation.Collections.IIterable[Windows.Storage.IStorageItem], processId: UInt32, auditInfo: Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo, messageFromApp: WinRT_String, behavior: Windows.Security.EnterpriseData.ProtectionPolicyRequestAccessBehavior) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_classmethod
    def IsFileProtectionRequiredAsync(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics4, target: Windows.Storage.IStorageItem, identity: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def IsFileProtectionRequiredForNewFileAsync(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics4, parentFolder: Windows.Storage.IStorageFolder, identity: WinRT_String, desiredName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def get_PrimaryManagedIdentity(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics4) -> WinRT_String: ...
    @winrt_classmethod
    def GetPrimaryManagedIdentityForIdentity(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics4, identity: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def RequestAccessWithAuditingInfoAsync(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics3, sourceIdentity: WinRT_String, targetIdentity: WinRT_String, auditInfo: Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_classmethod
    def RequestAccessWithMessageAsync(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics3, sourceIdentity: WinRT_String, targetIdentity: WinRT_String, auditInfo: Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo, messageFromApp: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_classmethod
    def RequestAccessForAppWithAuditingInfoAsync(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics3, sourceIdentity: WinRT_String, appPackageFamilyName: WinRT_String, auditInfo: Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_classmethod
    def RequestAccessForAppWithMessageAsync(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics3, sourceIdentity: WinRT_String, appPackageFamilyName: WinRT_String, auditInfo: Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo, messageFromApp: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_classmethod
    def LogAuditEvent(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics3, sourceIdentity: WinRT_String, targetIdentity: WinRT_String, auditInfo: Windows.Security.EnterpriseData.ProtectionPolicyAuditInfo) -> Void: ...
    @winrt_classmethod
    def HasContentBeenRevokedSince(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics2, identity: WinRT_String, since: Windows.Foundation.DateTime) -> Boolean: ...
    @winrt_classmethod
    def CheckAccessForApp(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics2, sourceIdentity: WinRT_String, appPackageFamilyName: WinRT_String) -> Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult: ...
    @winrt_classmethod
    def RequestAccessForAppAsync(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics2, sourceIdentity: WinRT_String, appPackageFamilyName: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    @winrt_classmethod
    def GetEnforcementLevel(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics2, identity: WinRT_String) -> Windows.Security.EnterpriseData.EnforcementLevel: ...
    @winrt_classmethod
    def IsUserDecryptionAllowed(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics2, identity: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def IsProtectionUnderLockRequired(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics2, identity: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def add_PolicyChanged(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics2, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_PolicyChanged(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_IsProtectionEnabled(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics2) -> Boolean: ...
    @winrt_classmethod
    def IsIdentityManaged(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics, identity: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def TryApplyProcessUIPolicy(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics, identity: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def ClearProcessUIPolicy(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics) -> Void: ...
    @winrt_classmethod
    def CreateCurrentThreadNetworkContext(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics, identity: WinRT_String) -> Windows.Security.EnterpriseData.ThreadNetworkContext: ...
    @winrt_classmethod
    def GetPrimaryManagedIdentityForNetworkEndpointAsync(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics, endpointHost: Windows.Networking.HostName) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def RevokeContent(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics, identity: WinRT_String) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics) -> Windows.Security.EnterpriseData.ProtectionPolicyManager: ...
    @winrt_classmethod
    def add_ProtectedAccessSuspending(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics, handler: Windows.Foundation.EventHandler[Windows.Security.EnterpriseData.ProtectedAccessSuspendingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_ProtectedAccessSuspending(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_ProtectedAccessResumed(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics, handler: Windows.Foundation.EventHandler[Windows.Security.EnterpriseData.ProtectedAccessResumedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_ProtectedAccessResumed(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_ProtectedContentRevoked(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics, handler: Windows.Foundation.EventHandler[Windows.Security.EnterpriseData.ProtectedContentRevokedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_ProtectedContentRevoked(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def CheckAccess(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics, sourceIdentity: WinRT_String, targetIdentity: WinRT_String) -> Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: Windows.Security.EnterpriseData.IProtectionPolicyManagerStatics, sourceIdentity: WinRT_String, targetIdentity: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]: ...
    Identity = property(get_Identity, put_Identity)
    ShowEnterpriseIndicator = property(get_ShowEnterpriseIndicator, put_ShowEnterpriseIndicator)
    _ProtectionPolicyManager_Meta_.PrimaryManagedIdentity = property(get_PrimaryManagedIdentity.__wrapped__, None)
    _ProtectionPolicyManager_Meta_.IsProtectionEnabled = property(get_IsProtectionEnabled.__wrapped__, None)
ProtectionPolicyRequestAccessBehavior = Int32
ProtectionPolicyRequestAccessBehavior_Decrypt: ProtectionPolicyRequestAccessBehavior = 0
ProtectionPolicyRequestAccessBehavior_TreatOverridePolicyAsBlock: ProtectionPolicyRequestAccessBehavior = 1
class ThreadNetworkContext(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.EnterpriseData.IThreadNetworkContext
    _classid_ = 'Windows.Security.EnterpriseData.ThreadNetworkContext'
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
make_head(_module, 'BufferProtectUnprotectResult')
make_head(_module, 'DataProtectionInfo')
make_head(_module, 'DataProtectionManager')
make_head(_module, 'FileProtectionInfo')
make_head(_module, 'FileProtectionManager')
make_head(_module, 'FileRevocationManager')
make_head(_module, 'FileUnprotectOptions')
make_head(_module, 'IBufferProtectUnprotectResult')
make_head(_module, 'IDataProtectionInfo')
make_head(_module, 'IDataProtectionManagerStatics')
make_head(_module, 'IFileProtectionInfo')
make_head(_module, 'IFileProtectionInfo2')
make_head(_module, 'IFileProtectionManagerStatics')
make_head(_module, 'IFileProtectionManagerStatics2')
make_head(_module, 'IFileProtectionManagerStatics3')
make_head(_module, 'IFileRevocationManagerStatics')
make_head(_module, 'IFileUnprotectOptions')
make_head(_module, 'IFileUnprotectOptionsFactory')
make_head(_module, 'IProtectedAccessResumedEventArgs')
make_head(_module, 'IProtectedAccessSuspendingEventArgs')
make_head(_module, 'IProtectedContainerExportResult')
make_head(_module, 'IProtectedContainerImportResult')
make_head(_module, 'IProtectedContentRevokedEventArgs')
make_head(_module, 'IProtectedFileCreateResult')
make_head(_module, 'IProtectionPolicyAuditInfo')
make_head(_module, 'IProtectionPolicyAuditInfoFactory')
make_head(_module, 'IProtectionPolicyManager')
make_head(_module, 'IProtectionPolicyManager2')
make_head(_module, 'IProtectionPolicyManagerStatics')
make_head(_module, 'IProtectionPolicyManagerStatics2')
make_head(_module, 'IProtectionPolicyManagerStatics3')
make_head(_module, 'IProtectionPolicyManagerStatics4')
make_head(_module, 'IThreadNetworkContext')
make_head(_module, 'ProtectedAccessResumedEventArgs')
make_head(_module, 'ProtectedAccessSuspendingEventArgs')
make_head(_module, 'ProtectedContainerExportResult')
make_head(_module, 'ProtectedContainerImportResult')
make_head(_module, 'ProtectedContentRevokedEventArgs')
make_head(_module, 'ProtectedFileCreateResult')
make_head(_module, 'ProtectionPolicyAuditInfo')
make_head(_module, 'ProtectionPolicyManager')
make_head(_module, 'ThreadNetworkContext')
