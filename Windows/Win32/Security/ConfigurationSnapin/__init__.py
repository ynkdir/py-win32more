from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.Security.ConfigurationSnapin
import Windows.Win32.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
cNodetypeSceTemplateServices: Guid = Guid('{24a7f717-1f0c-11d1-affb-00c04fb984f9}')
cNodetypeSceAnalysisServices: Guid = Guid('{678050c7-1ff8-11d1-affb-00c04fb984f9}')
cNodetypeSceEventLog: Guid = Guid('{2ce06698-4bf3-11d1-8c30-00c04fb984f9}')
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
class ISceSvcAttachmentData(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{17c35fde-200d-11d1-affb-00c04fb984f9}')
    @commethod(3)
    def GetData(self, scesvcHandle: VoidPtr, sceType: Windows.Win32.Security.ConfigurationSnapin.SCESVC_INFO_TYPE, ppvData: POINTER(VoidPtr), psceEnumHandle: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Initialize(self, lpServiceName: POINTER(SByte), lpTemplateName: POINTER(SByte), lpSceSvcPersistInfo: Windows.Win32.Security.ConfigurationSnapin.ISceSvcAttachmentPersistInfo_head, pscesvcHandle: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FreeBuffer(self, pvData: VoidPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CloseHandle(self, scesvcHandle: VoidPtr) -> Windows.Win32.Foundation.HRESULT: ...
class ISceSvcAttachmentPersistInfo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6d90e0d0-200d-11d1-affb-00c04fb984f9}')
    @commethod(3)
    def Save(self, lpTemplateName: POINTER(SByte), scesvcHandle: POINTER(VoidPtr), ppvData: POINTER(VoidPtr), pbOverwriteAll: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsDirty(self, lpTemplateName: POINTER(SByte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FreeBuffer(self, pvData: VoidPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFSCE_FREE_INFO(pvServiceInfo: VoidPtr) -> UInt32: ...
@cfunctype_pointer
def PFSCE_LOG_INFO(ErrLevel: Windows.Win32.Security.ConfigurationSnapin.SCE_LOG_ERR_LEVEL, Win32rc: UInt32, pErrFmt: POINTER(SByte)) -> UInt32: ...
@winfunctype_pointer
def PFSCE_QUERY_INFO(sceHandle: VoidPtr, sceType: Windows.Win32.Security.ConfigurationSnapin.SCESVC_INFO_TYPE, lpPrefix: POINTER(SByte), bExact: Windows.Win32.Foundation.BOOL, ppvInfo: POINTER(VoidPtr), psceEnumHandle: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PFSCE_SET_INFO(sceHandle: VoidPtr, sceType: Windows.Win32.Security.ConfigurationSnapin.SCESVC_INFO_TYPE, lpPrefix: POINTER(SByte), bExact: Windows.Win32.Foundation.BOOL, pvInfo: VoidPtr) -> UInt32: ...
@winfunctype_pointer
def PF_ConfigAnalyzeService(pSceCbInfo: POINTER(Windows.Win32.Security.ConfigurationSnapin.SCESVC_CALLBACK_INFO_head)) -> UInt32: ...
@winfunctype_pointer
def PF_UpdateService(pSceCbInfo: POINTER(Windows.Win32.Security.ConfigurationSnapin.SCESVC_CALLBACK_INFO_head), ServiceInfo: POINTER(Windows.Win32.Security.ConfigurationSnapin.SCESVC_CONFIGURATION_INFO_head)) -> UInt32: ...
class SCESVC_ANALYSIS_INFO(EasyCastStructure):
    Count: UInt32
    Lines: POINTER(Windows.Win32.Security.ConfigurationSnapin.SCESVC_ANALYSIS_LINE_head)
class SCESVC_ANALYSIS_LINE(EasyCastStructure):
    Key: POINTER(SByte)
    Value: POINTER(Byte)
    ValueLen: UInt32
class SCESVC_CALLBACK_INFO(EasyCastStructure):
    sceHandle: VoidPtr
    pfQueryInfo: Windows.Win32.Security.ConfigurationSnapin.PFSCE_QUERY_INFO
    pfSetInfo: Windows.Win32.Security.ConfigurationSnapin.PFSCE_SET_INFO
    pfFreeInfo: Windows.Win32.Security.ConfigurationSnapin.PFSCE_FREE_INFO
    pfLogInfo: Windows.Win32.Security.ConfigurationSnapin.PFSCE_LOG_INFO
class SCESVC_CONFIGURATION_INFO(EasyCastStructure):
    Count: UInt32
    Lines: POINTER(Windows.Win32.Security.ConfigurationSnapin.SCESVC_CONFIGURATION_LINE_head)
class SCESVC_CONFIGURATION_LINE(EasyCastStructure):
    Key: POINTER(SByte)
    Value: POINTER(SByte)
    ValueLen: UInt32
SCESVC_INFO_TYPE = Int32
SCESVC_INFO_TYPE_SceSvcConfigurationInfo: SCESVC_INFO_TYPE = 0
SCESVC_INFO_TYPE_SceSvcMergedPolicyInfo: SCESVC_INFO_TYPE = 1
SCESVC_INFO_TYPE_SceSvcAnalysisInfo: SCESVC_INFO_TYPE = 2
SCESVC_INFO_TYPE_SceSvcInternalUse: SCESVC_INFO_TYPE = 3
SCE_LOG_ERR_LEVEL = Int32
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
