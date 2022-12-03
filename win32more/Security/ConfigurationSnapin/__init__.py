from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Security.ConfigurationSnapin
import win32more.System.Com
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
def _define_cNodetypeSceTemplateServices():
    return Guid('24a7f717-1f0c-11d1-af-fb-00-c0-4f-b9-84-f9')
def _define_cNodetypeSceAnalysisServices():
    return Guid('678050c7-1ff8-11d1-af-fb-00-c0-4f-b9-84-f9')
def _define_cNodetypeSceEventLog():
    return Guid('2ce06698-4bf3-11d1-8c-30-00-c0-4f-b9-84-f9')
SCESTATUS_SUCCESS = 0
SCESTATUS_INVALID_PARAMETER = 1
SCESTATUS_RECORD_NOT_FOUND = 2
SCESTATUS_INVALID_DATA = 3
SCESTATUS_OBJECT_EXIST = 4
SCESTATUS_BUFFER_TOO_SMALL = 5
SCESTATUS_PROFILE_NOT_FOUND = 6
SCESTATUS_BAD_FORMAT = 7
SCESTATUS_NOT_ENOUGH_RESOURCE = 8
SCESTATUS_ACCESS_DENIED = 9
SCESTATUS_CANT_DELETE = 10
SCESTATUS_PREFIX_OVERFLOW = 11
SCESTATUS_OTHER_ERROR = 12
SCESTATUS_ALREADY_RUNNING = 13
SCESTATUS_SERVICE_NOT_SUPPORT = 14
SCESTATUS_MOD_NOT_FOUND = 15
SCESTATUS_EXCEPTION_IN_SERVER = 16
SCESTATUS_NO_TEMPLATE_GIVEN = 17
SCESTATUS_NO_MAPPING = 18
SCESTATUS_TRUST_FAIL = 19
SCE_ROOT_PATH = 'Software\\Microsoft\\Windows NT\\CurrentVersion\\SeCEdit'
SCESVC_ENUMERATION_MAX = 100
struuidNodetypeSceTemplateServices = '{24a7f717-1f0c-11d1-affb-00c04fb984f9}'
lstruuidNodetypeSceTemplateServices = '{24a7f717-1f0c-11d1-affb-00c04fb984f9}'
struuidNodetypeSceAnalysisServices = '{678050c7-1ff8-11d1-affb-00c04fb984f9}'
lstruuidNodetypeSceAnalysisServices = '{678050c7-1ff8-11d1-affb-00c04fb984f9}'
struuidNodetypeSceEventLog = '{2ce06698-4bf3-11d1-8c30-00c04fb984f9}'
lstruuidNodetypeSceEventLog = '{2ce06698-4bf3-11d1-8c30-00c04fb984f9}'
CCF_SCESVC_ATTACHMENT = 'CCF_SCESVC_ATTACHMENT'
CCF_SCESVC_ATTACHMENT_DATA = 'CCF_SCESVC_ATTACHMENT_DATA'
def _define_ISceSvcAttachmentData_head():
    class ISceSvcAttachmentData(win32more.System.Com.IUnknown_head):
        Guid = Guid('17c35fde-200d-11d1-af-fb-00-c0-4f-b9-84-f9')
    return ISceSvcAttachmentData
def _define_ISceSvcAttachmentData():
    ISceSvcAttachmentData = win32more.Security.ConfigurationSnapin.ISceSvcAttachmentData_head
    ISceSvcAttachmentData.GetData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Security.ConfigurationSnapin.SCESVC_INFO_TYPE,POINTER(c_void_p),POINTER(UInt32))(3, 'GetData', ((1, 'scesvcHandle'),(1, 'sceType'),(1, 'ppvData'),(1, 'psceEnumHandle'),)))
    ISceSvcAttachmentData.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(SByte),POINTER(SByte),win32more.Security.ConfigurationSnapin.ISceSvcAttachmentPersistInfo_head,POINTER(c_void_p))(4, 'Initialize', ((1, 'lpServiceName'),(1, 'lpTemplateName'),(1, 'lpSceSvcPersistInfo'),(1, 'pscesvcHandle'),)))
    ISceSvcAttachmentData.FreeBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p)(5, 'FreeBuffer', ((1, 'pvData'),)))
    ISceSvcAttachmentData.CloseHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p)(6, 'CloseHandle', ((1, 'scesvcHandle'),)))
    win32more.System.Com.IUnknown
    return ISceSvcAttachmentData
def _define_ISceSvcAttachmentPersistInfo_head():
    class ISceSvcAttachmentPersistInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('6d90e0d0-200d-11d1-af-fb-00-c0-4f-b9-84-f9')
    return ISceSvcAttachmentPersistInfo
def _define_ISceSvcAttachmentPersistInfo():
    ISceSvcAttachmentPersistInfo = win32more.Security.ConfigurationSnapin.ISceSvcAttachmentPersistInfo_head
    ISceSvcAttachmentPersistInfo.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(SByte),POINTER(c_void_p),POINTER(c_void_p),POINTER(win32more.Foundation.BOOL))(3, 'Save', ((1, 'lpTemplateName'),(1, 'scesvcHandle'),(1, 'ppvData'),(1, 'pbOverwriteAll'),)))
    ISceSvcAttachmentPersistInfo.IsDirty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(SByte))(4, 'IsDirty', ((1, 'lpTemplateName'),)))
    ISceSvcAttachmentPersistInfo.FreeBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p)(5, 'FreeBuffer', ((1, 'pvData'),)))
    win32more.System.Com.IUnknown
    return ISceSvcAttachmentPersistInfo
def _define_PF_ConfigAnalyzeService():
    return WINFUNCTYPE(UInt32,POINTER(win32more.Security.ConfigurationSnapin.SCESVC_CALLBACK_INFO_head))
def _define_PF_UpdateService():
    return WINFUNCTYPE(UInt32,POINTER(win32more.Security.ConfigurationSnapin.SCESVC_CALLBACK_INFO_head),POINTER(win32more.Security.ConfigurationSnapin.SCESVC_CONFIGURATION_INFO_head))
def _define_PFSCE_FREE_INFO():
    return WINFUNCTYPE(UInt32,c_void_p)
def _define_PFSCE_LOG_INFO():
    return CFUNCTYPE(UInt32,win32more.Security.ConfigurationSnapin.SCE_LOG_ERR_LEVEL,UInt32,POINTER(SByte))
def _define_PFSCE_QUERY_INFO():
    return WINFUNCTYPE(UInt32,c_void_p,win32more.Security.ConfigurationSnapin.SCESVC_INFO_TYPE,POINTER(SByte),win32more.Foundation.BOOL,POINTER(c_void_p),POINTER(UInt32))
def _define_PFSCE_SET_INFO():
    return WINFUNCTYPE(UInt32,c_void_p,win32more.Security.ConfigurationSnapin.SCESVC_INFO_TYPE,POINTER(SByte),win32more.Foundation.BOOL,c_void_p)
SCE_LOG_ERR_LEVEL = UInt32
SCE_LOG_LEVEL_ALWAYS = 0
SCE_LOG_LEVEL_ERROR = 1
SCE_LOG_LEVEL_DETAIL = 2
SCE_LOG_LEVEL_DEBUG = 3
def _define_SCESVC_ANALYSIS_INFO_head():
    class SCESVC_ANALYSIS_INFO(Structure):
        pass
    return SCESVC_ANALYSIS_INFO
def _define_SCESVC_ANALYSIS_INFO():
    SCESVC_ANALYSIS_INFO = win32more.Security.ConfigurationSnapin.SCESVC_ANALYSIS_INFO_head
    SCESVC_ANALYSIS_INFO._fields_ = [
        ('Count', UInt32),
        ('Lines', POINTER(win32more.Security.ConfigurationSnapin.SCESVC_ANALYSIS_LINE_head)),
    ]
    return SCESVC_ANALYSIS_INFO
def _define_SCESVC_ANALYSIS_LINE_head():
    class SCESVC_ANALYSIS_LINE(Structure):
        pass
    return SCESVC_ANALYSIS_LINE
def _define_SCESVC_ANALYSIS_LINE():
    SCESVC_ANALYSIS_LINE = win32more.Security.ConfigurationSnapin.SCESVC_ANALYSIS_LINE_head
    SCESVC_ANALYSIS_LINE._fields_ = [
        ('Key', POINTER(SByte)),
        ('Value', c_char_p_no),
        ('ValueLen', UInt32),
    ]
    return SCESVC_ANALYSIS_LINE
def _define_SCESVC_CALLBACK_INFO_head():
    class SCESVC_CALLBACK_INFO(Structure):
        pass
    return SCESVC_CALLBACK_INFO
def _define_SCESVC_CALLBACK_INFO():
    SCESVC_CALLBACK_INFO = win32more.Security.ConfigurationSnapin.SCESVC_CALLBACK_INFO_head
    SCESVC_CALLBACK_INFO._fields_ = [
        ('sceHandle', c_void_p),
        ('pfQueryInfo', win32more.Security.ConfigurationSnapin.PFSCE_QUERY_INFO),
        ('pfSetInfo', win32more.Security.ConfigurationSnapin.PFSCE_SET_INFO),
        ('pfFreeInfo', win32more.Security.ConfigurationSnapin.PFSCE_FREE_INFO),
        ('pfLogInfo', win32more.Security.ConfigurationSnapin.PFSCE_LOG_INFO),
    ]
    return SCESVC_CALLBACK_INFO
def _define_SCESVC_CONFIGURATION_INFO_head():
    class SCESVC_CONFIGURATION_INFO(Structure):
        pass
    return SCESVC_CONFIGURATION_INFO
def _define_SCESVC_CONFIGURATION_INFO():
    SCESVC_CONFIGURATION_INFO = win32more.Security.ConfigurationSnapin.SCESVC_CONFIGURATION_INFO_head
    SCESVC_CONFIGURATION_INFO._fields_ = [
        ('Count', UInt32),
        ('Lines', POINTER(win32more.Security.ConfigurationSnapin.SCESVC_CONFIGURATION_LINE_head)),
    ]
    return SCESVC_CONFIGURATION_INFO
def _define_SCESVC_CONFIGURATION_LINE_head():
    class SCESVC_CONFIGURATION_LINE(Structure):
        pass
    return SCESVC_CONFIGURATION_LINE
def _define_SCESVC_CONFIGURATION_LINE():
    SCESVC_CONFIGURATION_LINE = win32more.Security.ConfigurationSnapin.SCESVC_CONFIGURATION_LINE_head
    SCESVC_CONFIGURATION_LINE._fields_ = [
        ('Key', POINTER(SByte)),
        ('Value', POINTER(SByte)),
        ('ValueLen', UInt32),
    ]
    return SCESVC_CONFIGURATION_LINE
SCESVC_INFO_TYPE = Int32
SCESVC_INFO_TYPE_SceSvcConfigurationInfo = 0
SCESVC_INFO_TYPE_SceSvcMergedPolicyInfo = 1
SCESVC_INFO_TYPE_SceSvcAnalysisInfo = 2
SCESVC_INFO_TYPE_SceSvcInternalUse = 3
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
