from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Com
import win32more.System.TransactionServer
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
Catalog = Guid('6eb22881-8a19-11d0-81-b6-00-a0-c9-23-1c-29')
CatalogCollection = Guid('6eb22883-8a19-11d0-81-b6-00-a0-c9-23-1c-29')
CatalogObject = Guid('6eb22882-8a19-11d0-81-b6-00-a0-c9-23-1c-29')
ComponentUtil = Guid('6eb22884-8a19-11d0-81-b6-00-a0-c9-23-1c-29')
def _define_ICatalog_head():
    class ICatalog(win32more.System.Com.IDispatch_head):
        Guid = Guid('6eb22870-8a19-11d0-81-b6-00-a0-c9-23-1c-29')
    return ICatalog
def _define_ICatalog():
    ICatalog = win32more.System.TransactionServer.ICatalog_head
    ICatalog.GetCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.IDispatch_head))(7, 'GetCollection', ((1, 'bstrCollName'),(1, 'ppCatalogCollection'),)))
    ICatalog.Connect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.IDispatch_head))(8, 'Connect', ((1, 'bstrConnectString'),(1, 'ppCatalogCollection'),)))
    ICatalog.get_MajorVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_MajorVersion', ((1, 'retval'),)))
    ICatalog.get_MinorVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(10, 'get_MinorVersion', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return ICatalog
def _define_IComponentUtil_head():
    class IComponentUtil(win32more.System.Com.IDispatch_head):
        Guid = Guid('6eb22873-8a19-11d0-81-b6-00-a0-c9-23-1c-29')
    return IComponentUtil
def _define_IComponentUtil():
    IComponentUtil = win32more.System.TransactionServer.IComponentUtil_head
    IComponentUtil.InstallComponent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR)(7, 'InstallComponent', ((1, 'bstrDLLFile'),(1, 'bstrTypelibFile'),(1, 'bstrProxyStubDLLFile'),)))
    IComponentUtil.ImportComponent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(8, 'ImportComponent', ((1, 'bstrCLSID'),)))
    IComponentUtil.ImportComponentByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(9, 'ImportComponentByName', ((1, 'bstrProgID'),)))
    IComponentUtil.GetCLSIDs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(10, 'GetCLSIDs', ((1, 'bstrDLLFile'),(1, 'bstrTypelibFile'),(1, 'aCLSIDs'),)))
    win32more.System.Com.IDispatch
    return IComponentUtil
def _define_IPackageUtil_head():
    class IPackageUtil(win32more.System.Com.IDispatch_head):
        Guid = Guid('6eb22874-8a19-11d0-81-b6-00-a0-c9-23-1c-29')
    return IPackageUtil
def _define_IPackageUtil():
    IPackageUtil = win32more.System.TransactionServer.IPackageUtil_head
    IPackageUtil.InstallPackage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32)(7, 'InstallPackage', ((1, 'bstrPackageFile'),(1, 'bstrInstallPath'),(1, 'lOptions'),)))
    IPackageUtil.ExportPackage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32)(8, 'ExportPackage', ((1, 'bstrPackageID'),(1, 'bstrPackageFile'),(1, 'lOptions'),)))
    IPackageUtil.ShutdownPackage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(9, 'ShutdownPackage', ((1, 'bstrPackageID'),)))
    win32more.System.Com.IDispatch
    return IPackageUtil
def _define_IRemoteComponentUtil_head():
    class IRemoteComponentUtil(win32more.System.Com.IDispatch_head):
        Guid = Guid('6eb22875-8a19-11d0-81-b6-00-a0-c9-23-1c-29')
    return IRemoteComponentUtil
def _define_IRemoteComponentUtil():
    IRemoteComponentUtil = win32more.System.TransactionServer.IRemoteComponentUtil_head
    IRemoteComponentUtil.InstallRemoteComponent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR)(7, 'InstallRemoteComponent', ((1, 'bstrServer'),(1, 'bstrPackageID'),(1, 'bstrCLSID'),)))
    IRemoteComponentUtil.InstallRemoteComponentByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR)(8, 'InstallRemoteComponentByName', ((1, 'bstrServer'),(1, 'bstrPackageName'),(1, 'bstrProgID'),)))
    win32more.System.Com.IDispatch
    return IRemoteComponentUtil
def _define_IRoleAssociationUtil_head():
    class IRoleAssociationUtil(win32more.System.Com.IDispatch_head):
        Guid = Guid('6eb22876-8a19-11d0-81-b6-00-a0-c9-23-1c-29')
    return IRoleAssociationUtil
def _define_IRoleAssociationUtil():
    IRoleAssociationUtil = win32more.System.TransactionServer.IRoleAssociationUtil_head
    IRoleAssociationUtil.AssociateRole = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(7, 'AssociateRole', ((1, 'bstrRoleID'),)))
    IRoleAssociationUtil.AssociateRoleByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(8, 'AssociateRoleByName', ((1, 'bstrRoleName'),)))
    win32more.System.Com.IDispatch
    return IRoleAssociationUtil
MTSAdminErrorCodes = Int32
MTSAdminErrorCodes_mtsErrObjectErrors = -2146368511
MTSAdminErrorCodes_mtsErrObjectInvalid = -2146368510
MTSAdminErrorCodes_mtsErrKeyMissing = -2146368509
MTSAdminErrorCodes_mtsErrAlreadyInstalled = -2146368508
MTSAdminErrorCodes_mtsErrDownloadFailed = -2146368507
MTSAdminErrorCodes_mtsErrPDFWriteFail = -2146368505
MTSAdminErrorCodes_mtsErrPDFReadFail = -2146368504
MTSAdminErrorCodes_mtsErrPDFVersion = -2146368503
MTSAdminErrorCodes_mtsErrCoReqCompInstalled = -2146368496
MTSAdminErrorCodes_mtsErrBadPath = -2146368502
MTSAdminErrorCodes_mtsErrPackageExists = -2146368501
MTSAdminErrorCodes_mtsErrRoleExists = -2146368500
MTSAdminErrorCodes_mtsErrCantCopyFile = -2146368499
MTSAdminErrorCodes_mtsErrNoTypeLib = -2146368498
MTSAdminErrorCodes_mtsErrNoUser = -2146368497
MTSAdminErrorCodes_mtsErrInvalidUserids = -2146368496
MTSAdminErrorCodes_mtsErrNoRegistryCLSID = -2146368495
MTSAdminErrorCodes_mtsErrBadRegistryProgID = -2146368494
MTSAdminErrorCodes_mtsErrAuthenticationLevel = -2146368493
MTSAdminErrorCodes_mtsErrUserPasswdNotValid = -2146368492
MTSAdminErrorCodes_mtsErrNoRegistryRead = -2146368491
MTSAdminErrorCodes_mtsErrNoRegistryWrite = -2146368490
MTSAdminErrorCodes_mtsErrNoRegistryRepair = -2146368489
MTSAdminErrorCodes_mtsErrCLSIDOrIIDMismatch = -2146368488
MTSAdminErrorCodes_mtsErrRemoteInterface = -2146368487
MTSAdminErrorCodes_mtsErrDllRegisterServer = -2146368486
MTSAdminErrorCodes_mtsErrNoServerShare = -2146368485
MTSAdminErrorCodes_mtsErrNoAccessToUNC = -2146368484
MTSAdminErrorCodes_mtsErrDllLoadFailed = -2146368483
MTSAdminErrorCodes_mtsErrBadRegistryLibID = -2146368482
MTSAdminErrorCodes_mtsErrPackDirNotFound = -2146368481
MTSAdminErrorCodes_mtsErrTreatAs = -2146368480
MTSAdminErrorCodes_mtsErrBadForward = -2146368479
MTSAdminErrorCodes_mtsErrBadIID = -2146368478
MTSAdminErrorCodes_mtsErrRegistrarFailed = -2146368477
MTSAdminErrorCodes_mtsErrCompFileDoesNotExist = -2146368476
MTSAdminErrorCodes_mtsErrCompFileLoadDLLFail = -2146368475
MTSAdminErrorCodes_mtsErrCompFileGetClassObj = -2146368474
MTSAdminErrorCodes_mtsErrCompFileClassNotAvail = -2146368473
MTSAdminErrorCodes_mtsErrCompFileBadTLB = -2146368472
MTSAdminErrorCodes_mtsErrCompFileNotInstallable = -2146368471
MTSAdminErrorCodes_mtsErrNotChangeable = -2146368470
MTSAdminErrorCodes_mtsErrNotDeletable = -2146368469
MTSAdminErrorCodes_mtsErrSession = -2146368468
MTSAdminErrorCodes_mtsErrCompFileNoRegistrar = -2146368460
MTSPackageExportOptions = Int32
MTSPackageExportOptions_mtsExportUsers = 1
MTSPackageInstallOptions = Int32
MTSPackageInstallOptions_mtsInstallUsers = 1
PackageUtil = Guid('6eb22885-8a19-11d0-81-b6-00-a0-c9-23-1c-29')
RemoteComponentUtil = Guid('6eb22886-8a19-11d0-81-b6-00-a0-c9-23-1c-29')
RoleAssociationUtil = Guid('6eb22887-8a19-11d0-81-b6-00-a0-c9-23-1c-29')
__all__ = [
    "Catalog",
    "CatalogCollection",
    "CatalogObject",
    "ComponentUtil",
    "ICatalog",
    "IComponentUtil",
    "IPackageUtil",
    "IRemoteComponentUtil",
    "IRoleAssociationUtil",
    "MTSAdminErrorCodes",
    "MTSAdminErrorCodes_mtsErrAlreadyInstalled",
    "MTSAdminErrorCodes_mtsErrAuthenticationLevel",
    "MTSAdminErrorCodes_mtsErrBadForward",
    "MTSAdminErrorCodes_mtsErrBadIID",
    "MTSAdminErrorCodes_mtsErrBadPath",
    "MTSAdminErrorCodes_mtsErrBadRegistryLibID",
    "MTSAdminErrorCodes_mtsErrBadRegistryProgID",
    "MTSAdminErrorCodes_mtsErrCLSIDOrIIDMismatch",
    "MTSAdminErrorCodes_mtsErrCantCopyFile",
    "MTSAdminErrorCodes_mtsErrCoReqCompInstalled",
    "MTSAdminErrorCodes_mtsErrCompFileBadTLB",
    "MTSAdminErrorCodes_mtsErrCompFileClassNotAvail",
    "MTSAdminErrorCodes_mtsErrCompFileDoesNotExist",
    "MTSAdminErrorCodes_mtsErrCompFileGetClassObj",
    "MTSAdminErrorCodes_mtsErrCompFileLoadDLLFail",
    "MTSAdminErrorCodes_mtsErrCompFileNoRegistrar",
    "MTSAdminErrorCodes_mtsErrCompFileNotInstallable",
    "MTSAdminErrorCodes_mtsErrDllLoadFailed",
    "MTSAdminErrorCodes_mtsErrDllRegisterServer",
    "MTSAdminErrorCodes_mtsErrDownloadFailed",
    "MTSAdminErrorCodes_mtsErrInvalidUserids",
    "MTSAdminErrorCodes_mtsErrKeyMissing",
    "MTSAdminErrorCodes_mtsErrNoAccessToUNC",
    "MTSAdminErrorCodes_mtsErrNoRegistryCLSID",
    "MTSAdminErrorCodes_mtsErrNoRegistryRead",
    "MTSAdminErrorCodes_mtsErrNoRegistryRepair",
    "MTSAdminErrorCodes_mtsErrNoRegistryWrite",
    "MTSAdminErrorCodes_mtsErrNoServerShare",
    "MTSAdminErrorCodes_mtsErrNoTypeLib",
    "MTSAdminErrorCodes_mtsErrNoUser",
    "MTSAdminErrorCodes_mtsErrNotChangeable",
    "MTSAdminErrorCodes_mtsErrNotDeletable",
    "MTSAdminErrorCodes_mtsErrObjectErrors",
    "MTSAdminErrorCodes_mtsErrObjectInvalid",
    "MTSAdminErrorCodes_mtsErrPDFReadFail",
    "MTSAdminErrorCodes_mtsErrPDFVersion",
    "MTSAdminErrorCodes_mtsErrPDFWriteFail",
    "MTSAdminErrorCodes_mtsErrPackDirNotFound",
    "MTSAdminErrorCodes_mtsErrPackageExists",
    "MTSAdminErrorCodes_mtsErrRegistrarFailed",
    "MTSAdminErrorCodes_mtsErrRemoteInterface",
    "MTSAdminErrorCodes_mtsErrRoleExists",
    "MTSAdminErrorCodes_mtsErrSession",
    "MTSAdminErrorCodes_mtsErrTreatAs",
    "MTSAdminErrorCodes_mtsErrUserPasswdNotValid",
    "MTSPackageExportOptions",
    "MTSPackageExportOptions_mtsExportUsers",
    "MTSPackageInstallOptions",
    "MTSPackageInstallOptions_mtsInstallUsers",
    "PackageUtil",
    "RemoteComponentUtil",
    "RoleAssociationUtil",
]
