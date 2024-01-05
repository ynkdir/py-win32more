from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
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
MTSAdminErrorCodes_mtsErrObjectErrors: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368511
MTSAdminErrorCodes_mtsErrObjectInvalid: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368510
MTSAdminErrorCodes_mtsErrKeyMissing: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368509
MTSAdminErrorCodes_mtsErrAlreadyInstalled: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368508
MTSAdminErrorCodes_mtsErrDownloadFailed: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368507
MTSAdminErrorCodes_mtsErrPDFWriteFail: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368505
MTSAdminErrorCodes_mtsErrPDFReadFail: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368504
MTSAdminErrorCodes_mtsErrPDFVersion: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368503
MTSAdminErrorCodes_mtsErrCoReqCompInstalled: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368496
MTSAdminErrorCodes_mtsErrBadPath: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368502
MTSAdminErrorCodes_mtsErrPackageExists: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368501
MTSAdminErrorCodes_mtsErrRoleExists: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368500
MTSAdminErrorCodes_mtsErrCantCopyFile: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368499
MTSAdminErrorCodes_mtsErrNoTypeLib: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368498
MTSAdminErrorCodes_mtsErrNoUser: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368497
MTSAdminErrorCodes_mtsErrInvalidUserids: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368496
MTSAdminErrorCodes_mtsErrNoRegistryCLSID: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368495
MTSAdminErrorCodes_mtsErrBadRegistryProgID: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368494
MTSAdminErrorCodes_mtsErrAuthenticationLevel: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368493
MTSAdminErrorCodes_mtsErrUserPasswdNotValid: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368492
MTSAdminErrorCodes_mtsErrNoRegistryRead: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368491
MTSAdminErrorCodes_mtsErrNoRegistryWrite: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368490
MTSAdminErrorCodes_mtsErrNoRegistryRepair: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368489
MTSAdminErrorCodes_mtsErrCLSIDOrIIDMismatch: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368488
MTSAdminErrorCodes_mtsErrRemoteInterface: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368487
MTSAdminErrorCodes_mtsErrDllRegisterServer: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368486
MTSAdminErrorCodes_mtsErrNoServerShare: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368485
MTSAdminErrorCodes_mtsErrNoAccessToUNC: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368484
MTSAdminErrorCodes_mtsErrDllLoadFailed: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368483
MTSAdminErrorCodes_mtsErrBadRegistryLibID: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368482
MTSAdminErrorCodes_mtsErrPackDirNotFound: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368481
MTSAdminErrorCodes_mtsErrTreatAs: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368480
MTSAdminErrorCodes_mtsErrBadForward: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368479
MTSAdminErrorCodes_mtsErrBadIID: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368478
MTSAdminErrorCodes_mtsErrRegistrarFailed: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368477
MTSAdminErrorCodes_mtsErrCompFileDoesNotExist: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368476
MTSAdminErrorCodes_mtsErrCompFileLoadDLLFail: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368475
MTSAdminErrorCodes_mtsErrCompFileGetClassObj: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368474
MTSAdminErrorCodes_mtsErrCompFileClassNotAvail: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368473
MTSAdminErrorCodes_mtsErrCompFileBadTLB: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368472
MTSAdminErrorCodes_mtsErrCompFileNotInstallable: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368471
MTSAdminErrorCodes_mtsErrNotChangeable: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368470
MTSAdminErrorCodes_mtsErrNotDeletable: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368469
MTSAdminErrorCodes_mtsErrSession: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368468
MTSAdminErrorCodes_mtsErrCompFileNoRegistrar: win32more.Windows.Win32.System.TransactionServer.MTSAdminErrorCodes = -2146368460
MTSPackageExportOptions = Int32
MTSPackageExportOptions_mtsExportUsers: win32more.Windows.Win32.System.TransactionServer.MTSPackageExportOptions = 1
MTSPackageInstallOptions = Int32
MTSPackageInstallOptions_mtsInstallUsers: win32more.Windows.Win32.System.TransactionServer.MTSPackageInstallOptions = 1
PackageUtil = Guid('{6eb22885-8a19-11d0-81b6-00a0c9231c29}')
RemoteComponentUtil = Guid('{6eb22886-8a19-11d0-81b6-00a0c9231c29}')
RoleAssociationUtil = Guid('{6eb22887-8a19-11d0-81b6-00a0c9231c29}')


make_ready(__name__)
