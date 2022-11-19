from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Com
import win32more.System.TransactionServer

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
Catalog = Guid('6eb22881-8a19-11d0-81b6-00a0c9231c29')
CatalogObject = Guid('6eb22882-8a19-11d0-81b6-00a0c9231c29')
CatalogCollection = Guid('6eb22883-8a19-11d0-81b6-00a0c9231c29')
ComponentUtil = Guid('6eb22884-8a19-11d0-81b6-00a0c9231c29')
PackageUtil = Guid('6eb22885-8a19-11d0-81b6-00a0c9231c29')
RemoteComponentUtil = Guid('6eb22886-8a19-11d0-81b6-00a0c9231c29')
RoleAssociationUtil = Guid('6eb22887-8a19-11d0-81b6-00a0c9231c29')
def _define_ICatalog_head():
    class ICatalog(win32more.System.Com.IDispatch_head):
        Guid = Guid('6eb22870-8a19-11d0-81b6-00a0c9231c29')
    return ICatalog
def _define_ICatalog():
    ICatalog = win32more.System.TransactionServer.ICatalog_head
    ICatalog.GetCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(7, 'GetCollection', ((1, 'bstrCollName'),(1, 'ppCatalogCollection'),)))
    ICatalog.Connect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(8, 'Connect', ((1, 'bstrConnectString'),(1, 'ppCatalogCollection'),)))
    ICatalog.get_MajorVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_MajorVersion', ((1, 'retval'),)))
    ICatalog.get_MinorVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_MinorVersion', ((1, 'retval'),)))
    win32more.System.Com.IDispatch
    return ICatalog
def _define_IComponentUtil_head():
    class IComponentUtil(win32more.System.Com.IDispatch_head):
        Guid = Guid('6eb22873-8a19-11d0-81b6-00a0c9231c29')
    return IComponentUtil
def _define_IComponentUtil():
    IComponentUtil = win32more.System.TransactionServer.IComponentUtil_head
    IComponentUtil.InstallComponent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(7, 'InstallComponent', ((1, 'bstrDLLFile'),(1, 'bstrTypelibFile'),(1, 'bstrProxyStubDLLFile'),)))
    IComponentUtil.ImportComponent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'ImportComponent', ((1, 'bstrCLSID'),)))
    IComponentUtil.ImportComponentByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(9, 'ImportComponentByName', ((1, 'bstrProgID'),)))
    IComponentUtil.GetCLSIDs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(10, 'GetCLSIDs', ((1, 'bstrDLLFile'),(1, 'bstrTypelibFile'),(1, 'aCLSIDs'),)))
    win32more.System.Com.IDispatch
    return IComponentUtil
def _define_IPackageUtil_head():
    class IPackageUtil(win32more.System.Com.IDispatch_head):
        Guid = Guid('6eb22874-8a19-11d0-81b6-00a0c9231c29')
    return IPackageUtil
def _define_IPackageUtil():
    IPackageUtil = win32more.System.TransactionServer.IPackageUtil_head
    IPackageUtil.InstallPackage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32, use_last_error=False)(7, 'InstallPackage', ((1, 'bstrPackageFile'),(1, 'bstrInstallPath'),(1, 'lOptions'),)))
    IPackageUtil.ExportPackage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32, use_last_error=False)(8, 'ExportPackage', ((1, 'bstrPackageID'),(1, 'bstrPackageFile'),(1, 'lOptions'),)))
    IPackageUtil.ShutdownPackage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(9, 'ShutdownPackage', ((1, 'bstrPackageID'),)))
    win32more.System.Com.IDispatch
    return IPackageUtil
def _define_IRemoteComponentUtil_head():
    class IRemoteComponentUtil(win32more.System.Com.IDispatch_head):
        Guid = Guid('6eb22875-8a19-11d0-81b6-00a0c9231c29')
    return IRemoteComponentUtil
def _define_IRemoteComponentUtil():
    IRemoteComponentUtil = win32more.System.TransactionServer.IRemoteComponentUtil_head
    IRemoteComponentUtil.InstallRemoteComponent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(7, 'InstallRemoteComponent', ((1, 'bstrServer'),(1, 'bstrPackageID'),(1, 'bstrCLSID'),)))
    IRemoteComponentUtil.InstallRemoteComponentByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(8, 'InstallRemoteComponentByName', ((1, 'bstrServer'),(1, 'bstrPackageName'),(1, 'bstrProgID'),)))
    win32more.System.Com.IDispatch
    return IRemoteComponentUtil
def _define_IRoleAssociationUtil_head():
    class IRoleAssociationUtil(win32more.System.Com.IDispatch_head):
        Guid = Guid('6eb22876-8a19-11d0-81b6-00a0c9231c29')
    return IRoleAssociationUtil
def _define_IRoleAssociationUtil():
    IRoleAssociationUtil = win32more.System.TransactionServer.IRoleAssociationUtil_head
    IRoleAssociationUtil.AssociateRole = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(7, 'AssociateRole', ((1, 'bstrRoleID'),)))
    IRoleAssociationUtil.AssociateRoleByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'AssociateRoleByName', ((1, 'bstrRoleName'),)))
    win32more.System.Com.IDispatch
    return IRoleAssociationUtil
__MIDL___MIDL_itf_mtxadmin_0107_0001 = Int32
__MIDL___MIDL_itf_mtxadmin_0107_0001_mtsInstallUsers = 1
__MIDL___MIDL_itf_mtxadmin_0107_0002 = Int32
__MIDL___MIDL_itf_mtxadmin_0107_0002_mtsExportUsers = 1
__MIDL___MIDL_itf_mtxadmin_0107_0003 = Int32
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrObjectErrors = -2146368511
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrObjectInvalid = -2146368510
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrKeyMissing = -2146368509
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrAlreadyInstalled = -2146368508
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrDownloadFailed = -2146368507
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrPDFWriteFail = -2146368505
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrPDFReadFail = -2146368504
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrPDFVersion = -2146368503
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrCoReqCompInstalled = -2146368496
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrBadPath = -2146368502
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrPackageExists = -2146368501
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrRoleExists = -2146368500
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrCantCopyFile = -2146368499
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrNoTypeLib = -2146368498
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrNoUser = -2146368497
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrInvalidUserids = -2146368496
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrNoRegistryCLSID = -2146368495
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrBadRegistryProgID = -2146368494
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrAuthenticationLevel = -2146368493
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrUserPasswdNotValid = -2146368492
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrNoRegistryRead = -2146368491
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrNoRegistryWrite = -2146368490
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrNoRegistryRepair = -2146368489
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrCLSIDOrIIDMismatch = -2146368488
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrRemoteInterface = -2146368487
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrDllRegisterServer = -2146368486
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrNoServerShare = -2146368485
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrNoAccessToUNC = -2146368484
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrDllLoadFailed = -2146368483
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrBadRegistryLibID = -2146368482
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrPackDirNotFound = -2146368481
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrTreatAs = -2146368480
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrBadForward = -2146368479
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrBadIID = -2146368478
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrRegistrarFailed = -2146368477
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrCompFileDoesNotExist = -2146368476
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrCompFileLoadDLLFail = -2146368475
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrCompFileGetClassObj = -2146368474
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrCompFileClassNotAvail = -2146368473
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrCompFileBadTLB = -2146368472
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrCompFileNotInstallable = -2146368471
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrNotChangeable = -2146368470
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrNotDeletable = -2146368469
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrSession = -2146368468
__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrCompFileNoRegistrar = -2146368460
__all__ = [
    "Catalog",
    "CatalogObject",
    "CatalogCollection",
    "ComponentUtil",
    "PackageUtil",
    "RemoteComponentUtil",
    "RoleAssociationUtil",
    "ICatalog",
    "IComponentUtil",
    "IPackageUtil",
    "IRemoteComponentUtil",
    "IRoleAssociationUtil",
    "__MIDL___MIDL_itf_mtxadmin_0107_0001",
    "__MIDL___MIDL_itf_mtxadmin_0107_0001_mtsInstallUsers",
    "__MIDL___MIDL_itf_mtxadmin_0107_0002",
    "__MIDL___MIDL_itf_mtxadmin_0107_0002_mtsExportUsers",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrObjectErrors",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrObjectInvalid",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrKeyMissing",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrAlreadyInstalled",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrDownloadFailed",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrPDFWriteFail",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrPDFReadFail",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrPDFVersion",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrCoReqCompInstalled",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrBadPath",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrPackageExists",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrRoleExists",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrCantCopyFile",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrNoTypeLib",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrNoUser",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrInvalidUserids",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrNoRegistryCLSID",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrBadRegistryProgID",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrAuthenticationLevel",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrUserPasswdNotValid",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrNoRegistryRead",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrNoRegistryWrite",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrNoRegistryRepair",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrCLSIDOrIIDMismatch",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrRemoteInterface",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrDllRegisterServer",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrNoServerShare",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrNoAccessToUNC",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrDllLoadFailed",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrBadRegistryLibID",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrPackDirNotFound",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrTreatAs",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrBadForward",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrBadIID",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrRegistrarFailed",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrCompFileDoesNotExist",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrCompFileLoadDLLFail",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrCompFileGetClassObj",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrCompFileClassNotAvail",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrCompFileBadTLB",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrCompFileNotInstallable",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrNotChangeable",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrNotDeletable",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrSession",
    "__MIDL___MIDL_itf_mtxadmin_0107_0003_mtsErrCompFileNoRegistrar",
]
