from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.TransactionServer
Catalog = Guid('{6eb22881-8a19-11d0-81b6-00a0c9231c29}')
CatalogCollection = Guid('{6eb22883-8a19-11d0-81b6-00a0c9231c29}')
CatalogObject = Guid('{6eb22882-8a19-11d0-81b6-00a0c9231c29}')
ComponentUtil = Guid('{6eb22884-8a19-11d0-81b6-00a0c9231c29}')
class ICatalog(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6eb22870-8a19-11d0-81b6-00a0c9231c29}')
    @commethod(7)
    def GetCollection(self, bstrCollName: win32more.Windows.Win32.Foundation.BSTR, ppCatalogCollection: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Connect(self, bstrConnectString: win32more.Windows.Win32.Foundation.BSTR, ppCatalogCollection: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_MajorVersion(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_MinorVersion(self, retval: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComponentUtil(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6eb22873-8a19-11d0-81b6-00a0c9231c29}')
    @commethod(7)
    def InstallComponent(self, bstrDLLFile: win32more.Windows.Win32.Foundation.BSTR, bstrTypelibFile: win32more.Windows.Win32.Foundation.BSTR, bstrProxyStubDLLFile: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ImportComponent(self, bstrCLSID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ImportComponentByName(self, bstrProgID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetCLSIDs(self, bstrDLLFile: win32more.Windows.Win32.Foundation.BSTR, bstrTypelibFile: win32more.Windows.Win32.Foundation.BSTR, aCLSIDs: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPackageUtil(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6eb22874-8a19-11d0-81b6-00a0c9231c29}')
    @commethod(7)
    def InstallPackage(self, bstrPackageFile: win32more.Windows.Win32.Foundation.BSTR, bstrInstallPath: win32more.Windows.Win32.Foundation.BSTR, lOptions: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ExportPackage(self, bstrPackageID: win32more.Windows.Win32.Foundation.BSTR, bstrPackageFile: win32more.Windows.Win32.Foundation.BSTR, lOptions: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ShutdownPackage(self, bstrPackageID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRemoteComponentUtil(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6eb22875-8a19-11d0-81b6-00a0c9231c29}')
    @commethod(7)
    def InstallRemoteComponent(self, bstrServer: win32more.Windows.Win32.Foundation.BSTR, bstrPackageID: win32more.Windows.Win32.Foundation.BSTR, bstrCLSID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def InstallRemoteComponentByName(self, bstrServer: win32more.Windows.Win32.Foundation.BSTR, bstrPackageName: win32more.Windows.Win32.Foundation.BSTR, bstrProgID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRoleAssociationUtil(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6eb22876-8a19-11d0-81b6-00a0c9231c29}')
    @commethod(7)
    def AssociateRole(self, bstrRoleID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AssociateRoleByName(self, bstrRoleName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
MTSAdminErrorCodes = Int32
mtsErrObjectErrors: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368511
mtsErrObjectInvalid: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368510
mtsErrKeyMissing: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368509
mtsErrAlreadyInstalled: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368508
mtsErrDownloadFailed: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368507
mtsErrPDFWriteFail: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368505
mtsErrPDFReadFail: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368504
mtsErrPDFVersion: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368503
mtsErrCoReqCompInstalled: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368496
mtsErrBadPath: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368502
mtsErrPackageExists: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368501
mtsErrRoleExists: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368500
mtsErrCantCopyFile: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368499
mtsErrNoTypeLib: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368498
mtsErrNoUser: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368497
mtsErrInvalidUserids: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368496
mtsErrNoRegistryCLSID: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368495
mtsErrBadRegistryProgID: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368494
mtsErrAuthenticationLevel: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368493
mtsErrUserPasswdNotValid: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368492
mtsErrNoRegistryRead: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368491
mtsErrNoRegistryWrite: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368490
mtsErrNoRegistryRepair: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368489
mtsErrCLSIDOrIIDMismatch: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368488
mtsErrRemoteInterface: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368487
mtsErrDllRegisterServer: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368486
mtsErrNoServerShare: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368485
mtsErrNoAccessToUNC: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368484
mtsErrDllLoadFailed: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368483
mtsErrBadRegistryLibID: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368482
mtsErrPackDirNotFound: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368481
mtsErrTreatAs: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368480
mtsErrBadForward: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368479
mtsErrBadIID: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368478
mtsErrRegistrarFailed: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368477
mtsErrCompFileDoesNotExist: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368476
mtsErrCompFileLoadDLLFail: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368475
mtsErrCompFileGetClassObj: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368474
mtsErrCompFileClassNotAvail: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368473
mtsErrCompFileBadTLB: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368472
mtsErrCompFileNotInstallable: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368471
mtsErrNotChangeable: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368470
mtsErrNotDeletable: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368469
mtsErrSession: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368468
mtsErrCompFileNoRegistrar: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368460
MTSPackageExportOptions = Int32
mtsExportUsers: win32more.Windows.Win32.System.TransactionServer.MTSPackageExportOptions = 1
MTSPackageInstallOptions = Int32
mtsInstallUsers: win32more.Windows.Win32.System.TransactionServer.MTSPackageInstallOptions = 1
PackageUtil = Guid('{6eb22885-8a19-11d0-81b6-00a0c9231c29}')
RemoteComponentUtil = Guid('{6eb22886-8a19-11d0-81b6-00a0c9231c29}')
RoleAssociationUtil = Guid('{6eb22887-8a19-11d0-81b6-00a0c9231c29}')


make_ready(__name__)
