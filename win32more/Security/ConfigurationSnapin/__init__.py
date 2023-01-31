from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Security.ConfigurationSnapin
import win32more.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
cNodetypeSceTemplateServices: Guid = Guid('24a7f717-1f0c-11d1-af-fb-00-c0-4f-b9-84-f9')
cNodetypeSceAnalysisServices: Guid = Guid('678050c7-1ff8-11d1-af-fb-00-c0-4f-b9-84-f9')
cNodetypeSceEventLog: Guid = Guid('2ce06698-4bf3-11d1-8c-30-00-c0-4f-b9-84-f9')
SCESTATUS_SUCCESS: Int32 = 0
SCESTATUS_INVALID_PARAMETER: Int32 = 1
SCESTATUS_RECORD_NOT_FOUND: Int32 = 2
SCESTATUS_INVALID_DATA: Int32 = 3
SCESTATUS_OBJECT_EXIST: Int32 = 4
SCESTATUS_BUFFER_TOO_SMALL: Int32 = 5
SCESTATUS_PROFILE_NOT_FOUND: Int32 = 6
SCESTATUS_BAD_FORMAT: Int32 = 7
SCESTATUS_NOT_ENOUGH_RESOURCE: Int32 = 8
SCESTATUS_ACCESS_DENIED: Int32 = 9
SCESTATUS_CANT_DELETE: Int32 = 10
SCESTATUS_PREFIX_OVERFLOW: Int32 = 11
SCESTATUS_OTHER_ERROR: Int32 = 12
SCESTATUS_ALREADY_RUNNING: Int32 = 13
SCESTATUS_SERVICE_NOT_SUPPORT: Int32 = 14
SCESTATUS_MOD_NOT_FOUND: Int32 = 15
SCESTATUS_EXCEPTION_IN_SERVER: Int32 = 16
SCESTATUS_NO_TEMPLATE_GIVEN: Int32 = 17
SCESTATUS_NO_MAPPING: Int32 = 18
SCESTATUS_TRUST_FAIL: Int32 = 19
SCE_ROOT_PATH: String = 'Software\\Microsoft\\Windows NT\\CurrentVersion\\SeCEdit'
SCESVC_ENUMERATION_MAX: Int32 = 100
struuidNodetypeSceTemplateServices: String = '{24a7f717-1f0c-11d1-affb-00c04fb984f9}'
lstruuidNodetypeSceTemplateServices: String = '{24a7f717-1f0c-11d1-affb-00c04fb984f9}'
struuidNodetypeSceAnalysisServices: String = '{678050c7-1ff8-11d1-affb-00c04fb984f9}'
lstruuidNodetypeSceAnalysisServices: String = '{678050c7-1ff8-11d1-affb-00c04fb984f9}'
struuidNodetypeSceEventLog: String = '{2ce06698-4bf3-11d1-8c30-00c04fb984f9}'
lstruuidNodetypeSceEventLog: String = '{2ce06698-4bf3-11d1-8c30-00c04fb984f9}'
CCF_SCESVC_ATTACHMENT: String = 'CCF_SCESVC_ATTACHMENT'
CCF_SCESVC_ATTACHMENT_DATA: String = 'CCF_SCESVC_ATTACHMENT_DATA'
class ISceSvcAttachmentData(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('17c35fde-200d-11d1-af-fb-00-c0-4f-b9-84-f9')
    @commethod(3)
    def GetData(scesvcHandle: c_void_p, sceType: win32more.Security.ConfigurationSnapin.SCESVC_INFO_TYPE, ppvData: POINTER(c_void_p), psceEnumHandle: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Initialize(lpServiceName: POINTER(SByte), lpTemplateName: POINTER(SByte), lpSceSvcPersistInfo: win32more.Security.ConfigurationSnapin.ISceSvcAttachmentPersistInfo_head, pscesvcHandle: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def FreeBuffer(pvData: c_void_p) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def CloseHandle(scesvcHandle: c_void_p) -> win32more.Foundation.HRESULT: ...
class ISceSvcAttachmentPersistInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('6d90e0d0-200d-11d1-af-fb-00-c0-4f-b9-84-f9')
    @commethod(3)
    def Save(lpTemplateName: POINTER(SByte), scesvcHandle: POINTER(c_void_p), ppvData: POINTER(c_void_p), pbOverwriteAll: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def IsDirty(lpTemplateName: POINTER(SByte)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def FreeBuffer(pvData: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PFSCE_FREE_INFO(pvServiceInfo: c_void_p) -> UInt32: ...
@cfunctype_pointer
def PFSCE_LOG_INFO(ErrLevel: win32more.Security.ConfigurationSnapin.SCE_LOG_ERR_LEVEL, Win32rc: UInt32, pErrFmt: POINTER(SByte)) -> UInt32: ...
@winfunctype_pointer
def PFSCE_QUERY_INFO(sceHandle: c_void_p, sceType: win32more.Security.ConfigurationSnapin.SCESVC_INFO_TYPE, lpPrefix: POINTER(SByte), bExact: win32more.Foundation.BOOL, ppvInfo: POINTER(c_void_p), psceEnumHandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PFSCE_SET_INFO(sceHandle: c_void_p, sceType: win32more.Security.ConfigurationSnapin.SCESVC_INFO_TYPE, lpPrefix: POINTER(SByte), bExact: win32more.Foundation.BOOL, pvInfo: c_void_p) -> UInt32: ...
@winfunctype_pointer
def PF_ConfigAnalyzeService(pSceCbInfo: POINTER(win32more.Security.ConfigurationSnapin.SCESVC_CALLBACK_INFO_head)) -> UInt32: ...
@winfunctype_pointer
def PF_UpdateService(pSceCbInfo: POINTER(win32more.Security.ConfigurationSnapin.SCESVC_CALLBACK_INFO_head), ServiceInfo: POINTER(win32more.Security.ConfigurationSnapin.SCESVC_CONFIGURATION_INFO_head)) -> UInt32: ...
class SCESVC_ANALYSIS_INFO(Structure):
    Count: UInt32
    Lines: POINTER(win32more.Security.ConfigurationSnapin.SCESVC_ANALYSIS_LINE_head)
class SCESVC_ANALYSIS_LINE(Structure):
    Key: POINTER(SByte)
    Value: c_char_p_no
    ValueLen: UInt32
class SCESVC_CALLBACK_INFO(Structure):
    sceHandle: c_void_p
    pfQueryInfo: win32more.Security.ConfigurationSnapin.PFSCE_QUERY_INFO
    pfSetInfo: win32more.Security.ConfigurationSnapin.PFSCE_SET_INFO
    pfFreeInfo: win32more.Security.ConfigurationSnapin.PFSCE_FREE_INFO
    pfLogInfo: win32more.Security.ConfigurationSnapin.PFSCE_LOG_INFO
class SCESVC_CONFIGURATION_INFO(Structure):
    Count: UInt32
    Lines: POINTER(win32more.Security.ConfigurationSnapin.SCESVC_CONFIGURATION_LINE_head)
class SCESVC_CONFIGURATION_LINE(Structure):
    Key: POINTER(SByte)
    Value: POINTER(SByte)
    ValueLen: UInt32
SCESVC_INFO_TYPE = Int32
SCESVC_INFO_TYPE_SceSvcConfigurationInfo: SCESVC_INFO_TYPE = 0
SCESVC_INFO_TYPE_SceSvcMergedPolicyInfo: SCESVC_INFO_TYPE = 1
SCESVC_INFO_TYPE_SceSvcAnalysisInfo: SCESVC_INFO_TYPE = 2
SCESVC_INFO_TYPE_SceSvcInternalUse: SCESVC_INFO_TYPE = 3
SCE_LOG_ERR_LEVEL = UInt32
SCE_LOG_LEVEL_ALWAYS: SCE_LOG_ERR_LEVEL = 0
SCE_LOG_LEVEL_ERROR: SCE_LOG_ERR_LEVEL = 1
SCE_LOG_LEVEL_DETAIL: SCE_LOG_ERR_LEVEL = 2
SCE_LOG_LEVEL_DEBUG: SCE_LOG_ERR_LEVEL = 3
make_head(_module, 'ISceSvcAttachmentData')
make_head(_module, 'ISceSvcAttachmentPersistInfo')
make_head(_module, 'PFSCE_FREE_INFO')
make_head(_module, 'PFSCE_LOG_INFO')
make_head(_module, 'PFSCE_QUERY_INFO')
make_head(_module, 'PFSCE_SET_INFO')
make_head(_module, 'PF_ConfigAnalyzeService')
make_head(_module, 'PF_UpdateService')
make_head(_module, 'SCESVC_ANALYSIS_INFO')
make_head(_module, 'SCESVC_ANALYSIS_LINE')
make_head(_module, 'SCESVC_CALLBACK_INFO')
make_head(_module, 'SCESVC_CONFIGURATION_INFO')
make_head(_module, 'SCESVC_CONFIGURATION_LINE')
__all__ = [
    "CCF_SCESVC_ATTACHMENT",
    "CCF_SCESVC_ATTACHMENT_DATA",
    "ISceSvcAttachmentData",
    "ISceSvcAttachmentPersistInfo",
    "PFSCE_FREE_INFO",
    "PFSCE_LOG_INFO",
    "PFSCE_QUERY_INFO",
    "PFSCE_SET_INFO",
    "PF_ConfigAnalyzeService",
    "PF_UpdateService",
    "SCESTATUS_ACCESS_DENIED",
    "SCESTATUS_ALREADY_RUNNING",
    "SCESTATUS_BAD_FORMAT",
    "SCESTATUS_BUFFER_TOO_SMALL",
    "SCESTATUS_CANT_DELETE",
    "SCESTATUS_EXCEPTION_IN_SERVER",
    "SCESTATUS_INVALID_DATA",
    "SCESTATUS_INVALID_PARAMETER",
    "SCESTATUS_MOD_NOT_FOUND",
    "SCESTATUS_NOT_ENOUGH_RESOURCE",
    "SCESTATUS_NO_MAPPING",
    "SCESTATUS_NO_TEMPLATE_GIVEN",
    "SCESTATUS_OBJECT_EXIST",
    "SCESTATUS_OTHER_ERROR",
    "SCESTATUS_PREFIX_OVERFLOW",
    "SCESTATUS_PROFILE_NOT_FOUND",
    "SCESTATUS_RECORD_NOT_FOUND",
    "SCESTATUS_SERVICE_NOT_SUPPORT",
    "SCESTATUS_SUCCESS",
    "SCESTATUS_TRUST_FAIL",
    "SCESVC_ANALYSIS_INFO",
    "SCESVC_ANALYSIS_LINE",
    "SCESVC_CALLBACK_INFO",
    "SCESVC_CONFIGURATION_INFO",
    "SCESVC_CONFIGURATION_LINE",
    "SCESVC_ENUMERATION_MAX",
    "SCESVC_INFO_TYPE",
    "SCESVC_INFO_TYPE_SceSvcAnalysisInfo",
    "SCESVC_INFO_TYPE_SceSvcConfigurationInfo",
    "SCESVC_INFO_TYPE_SceSvcInternalUse",
    "SCESVC_INFO_TYPE_SceSvcMergedPolicyInfo",
    "SCE_LOG_ERR_LEVEL",
    "SCE_LOG_LEVEL_ALWAYS",
    "SCE_LOG_LEVEL_DEBUG",
    "SCE_LOG_LEVEL_DETAIL",
    "SCE_LOG_LEVEL_ERROR",
    "SCE_ROOT_PATH",
    "cNodetypeSceAnalysisServices",
    "cNodetypeSceEventLog",
    "cNodetypeSceTemplateServices",
    "lstruuidNodetypeSceAnalysisServices",
    "lstruuidNodetypeSceEventLog",
    "lstruuidNodetypeSceTemplateServices",
    "struuidNodetypeSceAnalysisServices",
    "struuidNodetypeSceEventLog",
    "struuidNodetypeSceTemplateServices",
]
_arch_optional = [
]
