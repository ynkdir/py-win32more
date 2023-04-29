from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.TransactionServer
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
Catalog = Guid('6eb22881-8a19-11d0-81-b6-00-a0-c9-23-1c-29')
CatalogCollection = Guid('6eb22883-8a19-11d0-81-b6-00-a0-c9-23-1c-29')
CatalogObject = Guid('6eb22882-8a19-11d0-81-b6-00-a0-c9-23-1c-29')
ComponentUtil = Guid('6eb22884-8a19-11d0-81-b6-00-a0-c9-23-1c-29')
class ICatalog(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('6eb22870-8a19-11d0-81-b6-00-a0-c9-23-1c-29')
    @commethod(7)
    def GetCollection(self, bstrCollName: Windows.Win32.Foundation.BSTR, ppCatalogCollection: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Connect(self, bstrConnectString: Windows.Win32.Foundation.BSTR, ppCatalogCollection: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_MajorVersion(self, retval: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_MinorVersion(self, retval: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IComponentUtil(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('6eb22873-8a19-11d0-81-b6-00-a0-c9-23-1c-29')
    @commethod(7)
    def InstallComponent(self, bstrDLLFile: Windows.Win32.Foundation.BSTR, bstrTypelibFile: Windows.Win32.Foundation.BSTR, bstrProxyStubDLLFile: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ImportComponent(self, bstrCLSID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ImportComponentByName(self, bstrProgID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetCLSIDs(self, bstrDLLFile: Windows.Win32.Foundation.BSTR, bstrTypelibFile: Windows.Win32.Foundation.BSTR, aCLSIDs: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IPackageUtil(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('6eb22874-8a19-11d0-81-b6-00-a0-c9-23-1c-29')
    @commethod(7)
    def InstallPackage(self, bstrPackageFile: Windows.Win32.Foundation.BSTR, bstrInstallPath: Windows.Win32.Foundation.BSTR, lOptions: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ExportPackage(self, bstrPackageID: Windows.Win32.Foundation.BSTR, bstrPackageFile: Windows.Win32.Foundation.BSTR, lOptions: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ShutdownPackage(self, bstrPackageID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IRemoteComponentUtil(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('6eb22875-8a19-11d0-81-b6-00-a0-c9-23-1c-29')
    @commethod(7)
    def InstallRemoteComponent(self, bstrServer: Windows.Win32.Foundation.BSTR, bstrPackageID: Windows.Win32.Foundation.BSTR, bstrCLSID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def InstallRemoteComponentByName(self, bstrServer: Windows.Win32.Foundation.BSTR, bstrPackageName: Windows.Win32.Foundation.BSTR, bstrProgID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IRoleAssociationUtil(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('6eb22876-8a19-11d0-81-b6-00-a0-c9-23-1c-29')
    @commethod(7)
    def AssociateRole(self, bstrRoleID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AssociateRoleByName(self, bstrRoleName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
MTSAdminErrorCodes = Int32
MTSAdminErrorCodes_mtsErrObjectErrors: MTSAdminErrorCodes = -2146368511
MTSAdminErrorCodes_mtsErrObjectInvalid: MTSAdminErrorCodes = -2146368510
MTSAdminErrorCodes_mtsErrKeyMissing: MTSAdminErrorCodes = -2146368509
MTSAdminErrorCodes_mtsErrAlreadyInstalled: MTSAdminErrorCodes = -2146368508
MTSAdminErrorCodes_mtsErrDownloadFailed: MTSAdminErrorCodes = -2146368507
MTSAdminErrorCodes_mtsErrPDFWriteFail: MTSAdminErrorCodes = -2146368505
MTSAdminErrorCodes_mtsErrPDFReadFail: MTSAdminErrorCodes = -2146368504
MTSAdminErrorCodes_mtsErrPDFVersion: MTSAdminErrorCodes = -2146368503
MTSAdminErrorCodes_mtsErrCoReqCompInstalled: MTSAdminErrorCodes = -2146368496
MTSAdminErrorCodes_mtsErrBadPath: MTSAdminErrorCodes = -2146368502
MTSAdminErrorCodes_mtsErrPackageExists: MTSAdminErrorCodes = -2146368501
MTSAdminErrorCodes_mtsErrRoleExists: MTSAdminErrorCodes = -2146368500
MTSAdminErrorCodes_mtsErrCantCopyFile: MTSAdminErrorCodes = -2146368499
MTSAdminErrorCodes_mtsErrNoTypeLib: MTSAdminErrorCodes = -2146368498
MTSAdminErrorCodes_mtsErrNoUser: MTSAdminErrorCodes = -2146368497
MTSAdminErrorCodes_mtsErrInvalidUserids: MTSAdminErrorCodes = -2146368496
MTSAdminErrorCodes_mtsErrNoRegistryCLSID: MTSAdminErrorCodes = -2146368495
MTSAdminErrorCodes_mtsErrBadRegistryProgID: MTSAdminErrorCodes = -2146368494
MTSAdminErrorCodes_mtsErrAuthenticationLevel: MTSAdminErrorCodes = -2146368493
MTSAdminErrorCodes_mtsErrUserPasswdNotValid: MTSAdminErrorCodes = -2146368492
MTSAdminErrorCodes_mtsErrNoRegistryRead: MTSAdminErrorCodes = -2146368491
MTSAdminErrorCodes_mtsErrNoRegistryWrite: MTSAdminErrorCodes = -2146368490
MTSAdminErrorCodes_mtsErrNoRegistryRepair: MTSAdminErrorCodes = -2146368489
MTSAdminErrorCodes_mtsErrCLSIDOrIIDMismatch: MTSAdminErrorCodes = -2146368488
MTSAdminErrorCodes_mtsErrRemoteInterface: MTSAdminErrorCodes = -2146368487
MTSAdminErrorCodes_mtsErrDllRegisterServer: MTSAdminErrorCodes = -2146368486
MTSAdminErrorCodes_mtsErrNoServerShare: MTSAdminErrorCodes = -2146368485
MTSAdminErrorCodes_mtsErrNoAccessToUNC: MTSAdminErrorCodes = -2146368484
MTSAdminErrorCodes_mtsErrDllLoadFailed: MTSAdminErrorCodes = -2146368483
MTSAdminErrorCodes_mtsErrBadRegistryLibID: MTSAdminErrorCodes = -2146368482
MTSAdminErrorCodes_mtsErrPackDirNotFound: MTSAdminErrorCodes = -2146368481
MTSAdminErrorCodes_mtsErrTreatAs: MTSAdminErrorCodes = -2146368480
MTSAdminErrorCodes_mtsErrBadForward: MTSAdminErrorCodes = -2146368479
MTSAdminErrorCodes_mtsErrBadIID: MTSAdminErrorCodes = -2146368478
MTSAdminErrorCodes_mtsErrRegistrarFailed: MTSAdminErrorCodes = -2146368477
MTSAdminErrorCodes_mtsErrCompFileDoesNotExist: MTSAdminErrorCodes = -2146368476
MTSAdminErrorCodes_mtsErrCompFileLoadDLLFail: MTSAdminErrorCodes = -2146368475
MTSAdminErrorCodes_mtsErrCompFileGetClassObj: MTSAdminErrorCodes = -2146368474
MTSAdminErrorCodes_mtsErrCompFileClassNotAvail: MTSAdminErrorCodes = -2146368473
MTSAdminErrorCodes_mtsErrCompFileBadTLB: MTSAdminErrorCodes = -2146368472
MTSAdminErrorCodes_mtsErrCompFileNotInstallable: MTSAdminErrorCodes = -2146368471
MTSAdminErrorCodes_mtsErrNotChangeable: MTSAdminErrorCodes = -2146368470
MTSAdminErrorCodes_mtsErrNotDeletable: MTSAdminErrorCodes = -2146368469
MTSAdminErrorCodes_mtsErrSession: MTSAdminErrorCodes = -2146368468
MTSAdminErrorCodes_mtsErrCompFileNoRegistrar: MTSAdminErrorCodes = -2146368460
MTSPackageExportOptions = Int32
MTSPackageExportOptions_mtsExportUsers: MTSPackageExportOptions = 1
MTSPackageInstallOptions = Int32
MTSPackageInstallOptions_mtsInstallUsers: MTSPackageInstallOptions = 1
PackageUtil = Guid('6eb22885-8a19-11d0-81-b6-00-a0-c9-23-1c-29')
RemoteComponentUtil = Guid('6eb22886-8a19-11d0-81-b6-00-a0-c9-23-1c-29')
RoleAssociationUtil = Guid('6eb22887-8a19-11d0-81-b6-00-a0-c9-23-1c-29')
make_head(_module, 'ICatalog')
make_head(_module, 'IComponentUtil')
make_head(_module, 'IPackageUtil')
make_head(_module, 'IRemoteComponentUtil')
make_head(_module, 'IRoleAssociationUtil')
