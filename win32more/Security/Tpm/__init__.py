from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Security.Tpm
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
TPMVSC_DEFAULT_ADMIN_ALGORITHM_ID = 130
def _define_ITpmVirtualSmartCardManager_head():
    class ITpmVirtualSmartCardManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('112b1dff-d9dc-41f7-86-9f-d6-7f-ee-7c-b5-91')
    return ITpmVirtualSmartCardManager
def _define_ITpmVirtualSmartCardManager():
    ITpmVirtualSmartCardManager = win32more.Security.Tpm.ITpmVirtualSmartCardManager_head
    ITpmVirtualSmartCardManager.CreateVirtualSmartCard = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Byte,c_char_p_no,UInt32,c_char_p_no,UInt32,c_char_p_no,UInt32,c_char_p_no,UInt32,win32more.Foundation.BOOL,win32more.Security.Tpm.ITpmVirtualSmartCardManagerStatusCallback_head,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.BOOL))(3, 'CreateVirtualSmartCard', ((1, 'pszFriendlyName'),(1, 'bAdminAlgId'),(1, 'pbAdminKey'),(1, 'cbAdminKey'),(1, 'pbAdminKcv'),(1, 'cbAdminKcv'),(1, 'pbPuk'),(1, 'cbPuk'),(1, 'pbPin'),(1, 'cbPin'),(1, 'fGenerate'),(1, 'pStatusCallback'),(1, 'ppszInstanceId'),(1, 'pfNeedReboot'),)))
    ITpmVirtualSmartCardManager.DestroyVirtualSmartCard = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Security.Tpm.ITpmVirtualSmartCardManagerStatusCallback_head,POINTER(win32more.Foundation.BOOL))(4, 'DestroyVirtualSmartCard', ((1, 'pszInstanceId'),(1, 'pStatusCallback'),(1, 'pfNeedReboot'),)))
    win32more.System.Com.IUnknown
    return ITpmVirtualSmartCardManager
def _define_ITpmVirtualSmartCardManager2_head():
    class ITpmVirtualSmartCardManager2(win32more.Security.Tpm.ITpmVirtualSmartCardManager_head):
        Guid = Guid('fdf8a2b9-02de-47f4-bc-26-aa-85-ab-5e-52-67')
    return ITpmVirtualSmartCardManager2
def _define_ITpmVirtualSmartCardManager2():
    ITpmVirtualSmartCardManager2 = win32more.Security.Tpm.ITpmVirtualSmartCardManager2_head
    ITpmVirtualSmartCardManager2.CreateVirtualSmartCardWithPinPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Byte,c_char_p_no,UInt32,c_char_p_no,UInt32,c_char_p_no,UInt32,c_char_p_no,UInt32,c_char_p_no,UInt32,win32more.Foundation.BOOL,win32more.Security.Tpm.ITpmVirtualSmartCardManagerStatusCallback_head,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.BOOL))(5, 'CreateVirtualSmartCardWithPinPolicy', ((1, 'pszFriendlyName'),(1, 'bAdminAlgId'),(1, 'pbAdminKey'),(1, 'cbAdminKey'),(1, 'pbAdminKcv'),(1, 'cbAdminKcv'),(1, 'pbPuk'),(1, 'cbPuk'),(1, 'pbPin'),(1, 'cbPin'),(1, 'pbPinPolicy'),(1, 'cbPinPolicy'),(1, 'fGenerate'),(1, 'pStatusCallback'),(1, 'ppszInstanceId'),(1, 'pfNeedReboot'),)))
    win32more.Security.Tpm.ITpmVirtualSmartCardManager
    return ITpmVirtualSmartCardManager2
def _define_ITpmVirtualSmartCardManager3_head():
    class ITpmVirtualSmartCardManager3(win32more.Security.Tpm.ITpmVirtualSmartCardManager2_head):
        Guid = Guid('3c745a97-f375-4150-be-17-59-50-f6-94-c6-99')
    return ITpmVirtualSmartCardManager3
def _define_ITpmVirtualSmartCardManager3():
    ITpmVirtualSmartCardManager3 = win32more.Security.Tpm.ITpmVirtualSmartCardManager3_head
    ITpmVirtualSmartCardManager3.CreateVirtualSmartCardWithAttestation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Byte,c_char_p_no,UInt32,c_char_p_no,UInt32,c_char_p_no,UInt32,c_char_p_no,UInt32,c_char_p_no,UInt32,win32more.Security.Tpm.TPMVSC_ATTESTATION_TYPE,win32more.Foundation.BOOL,win32more.Security.Tpm.ITpmVirtualSmartCardManagerStatusCallback_head,POINTER(win32more.Foundation.PWSTR))(6, 'CreateVirtualSmartCardWithAttestation', ((1, 'pszFriendlyName'),(1, 'bAdminAlgId'),(1, 'pbAdminKey'),(1, 'cbAdminKey'),(1, 'pbAdminKcv'),(1, 'cbAdminKcv'),(1, 'pbPuk'),(1, 'cbPuk'),(1, 'pbPin'),(1, 'cbPin'),(1, 'pbPinPolicy'),(1, 'cbPinPolicy'),(1, 'attestationType'),(1, 'fGenerate'),(1, 'pStatusCallback'),(1, 'ppszInstanceId'),)))
    win32more.Security.Tpm.ITpmVirtualSmartCardManager2
    return ITpmVirtualSmartCardManager3
def _define_ITpmVirtualSmartCardManagerStatusCallback_head():
    class ITpmVirtualSmartCardManagerStatusCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('1a1bb35f-abb8-451c-a1-ae-33-d9-8f-1b-ef-4a')
    return ITpmVirtualSmartCardManagerStatusCallback
def _define_ITpmVirtualSmartCardManagerStatusCallback():
    ITpmVirtualSmartCardManagerStatusCallback = win32more.Security.Tpm.ITpmVirtualSmartCardManagerStatusCallback_head
    ITpmVirtualSmartCardManagerStatusCallback.ReportProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Tpm.TPMVSCMGR_STATUS)(3, 'ReportProgress', ((1, 'Status'),)))
    ITpmVirtualSmartCardManagerStatusCallback.ReportError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Tpm.TPMVSCMGR_ERROR)(4, 'ReportError', ((1, 'Error'),)))
    win32more.System.Com.IUnknown
    return ITpmVirtualSmartCardManagerStatusCallback
RemoteTpmVirtualSmartCardManager = Guid('152ea2a8-70dc-4c59-8b-2a-32-aa-3c-a0-dc-ac')
TpmVirtualSmartCardManager = Guid('16a18e86-7f6e-4c20-ad-89-4f-fc-0d-b7-a9-6a')
TPMVSC_ATTESTATION_TYPE = Int32
TPMVSC_ATTESTATION_NONE = 0
TPMVSC_ATTESTATION_AIK_ONLY = 1
TPMVSC_ATTESTATION_AIK_AND_CERTIFICATE = 2
TPMVSCMGR_ERROR = Int32
TPMVSCMGR_ERROR_IMPERSONATION = 0
TPMVSCMGR_ERROR_PIN_COMPLEXITY = 1
TPMVSCMGR_ERROR_READER_COUNT_LIMIT = 2
TPMVSCMGR_ERROR_TERMINAL_SERVICES_SESSION = 3
TPMVSCMGR_ERROR_VTPMSMARTCARD_INITIALIZE = 4
TPMVSCMGR_ERROR_VTPMSMARTCARD_CREATE = 5
TPMVSCMGR_ERROR_VTPMSMARTCARD_DESTROY = 6
TPMVSCMGR_ERROR_VGIDSSIMULATOR_INITIALIZE = 7
TPMVSCMGR_ERROR_VGIDSSIMULATOR_CREATE = 8
TPMVSCMGR_ERROR_VGIDSSIMULATOR_DESTROY = 9
TPMVSCMGR_ERROR_VGIDSSIMULATOR_WRITE_PROPERTY = 10
TPMVSCMGR_ERROR_VGIDSSIMULATOR_READ_PROPERTY = 11
TPMVSCMGR_ERROR_VREADER_INITIALIZE = 12
TPMVSCMGR_ERROR_VREADER_CREATE = 13
TPMVSCMGR_ERROR_VREADER_DESTROY = 14
TPMVSCMGR_ERROR_GENERATE_LOCATE_READER = 15
TPMVSCMGR_ERROR_GENERATE_FILESYSTEM = 16
TPMVSCMGR_ERROR_CARD_CREATE = 17
TPMVSCMGR_ERROR_CARD_DESTROY = 18
TPMVSCMGR_STATUS = Int32
TPMVSCMGR_STATUS_VTPMSMARTCARD_INITIALIZING = 0
TPMVSCMGR_STATUS_VTPMSMARTCARD_CREATING = 1
TPMVSCMGR_STATUS_VTPMSMARTCARD_DESTROYING = 2
TPMVSCMGR_STATUS_VGIDSSIMULATOR_INITIALIZING = 3
TPMVSCMGR_STATUS_VGIDSSIMULATOR_CREATING = 4
TPMVSCMGR_STATUS_VGIDSSIMULATOR_DESTROYING = 5
TPMVSCMGR_STATUS_VREADER_INITIALIZING = 6
TPMVSCMGR_STATUS_VREADER_CREATING = 7
TPMVSCMGR_STATUS_VREADER_DESTROYING = 8
TPMVSCMGR_STATUS_GENERATE_WAITING = 9
TPMVSCMGR_STATUS_GENERATE_AUTHENTICATING = 10
TPMVSCMGR_STATUS_GENERATE_RUNNING = 11
TPMVSCMGR_STATUS_CARD_CREATED = 12
TPMVSCMGR_STATUS_CARD_DESTROYED = 13
__all__ = [
    "ITpmVirtualSmartCardManager",
    "ITpmVirtualSmartCardManager2",
    "ITpmVirtualSmartCardManager3",
    "ITpmVirtualSmartCardManagerStatusCallback",
    "RemoteTpmVirtualSmartCardManager",
    "TPMVSCMGR_ERROR",
    "TPMVSCMGR_ERROR_CARD_CREATE",
    "TPMVSCMGR_ERROR_CARD_DESTROY",
    "TPMVSCMGR_ERROR_GENERATE_FILESYSTEM",
    "TPMVSCMGR_ERROR_GENERATE_LOCATE_READER",
    "TPMVSCMGR_ERROR_IMPERSONATION",
    "TPMVSCMGR_ERROR_PIN_COMPLEXITY",
    "TPMVSCMGR_ERROR_READER_COUNT_LIMIT",
    "TPMVSCMGR_ERROR_TERMINAL_SERVICES_SESSION",
    "TPMVSCMGR_ERROR_VGIDSSIMULATOR_CREATE",
    "TPMVSCMGR_ERROR_VGIDSSIMULATOR_DESTROY",
    "TPMVSCMGR_ERROR_VGIDSSIMULATOR_INITIALIZE",
    "TPMVSCMGR_ERROR_VGIDSSIMULATOR_READ_PROPERTY",
    "TPMVSCMGR_ERROR_VGIDSSIMULATOR_WRITE_PROPERTY",
    "TPMVSCMGR_ERROR_VREADER_CREATE",
    "TPMVSCMGR_ERROR_VREADER_DESTROY",
    "TPMVSCMGR_ERROR_VREADER_INITIALIZE",
    "TPMVSCMGR_ERROR_VTPMSMARTCARD_CREATE",
    "TPMVSCMGR_ERROR_VTPMSMARTCARD_DESTROY",
    "TPMVSCMGR_ERROR_VTPMSMARTCARD_INITIALIZE",
    "TPMVSCMGR_STATUS",
    "TPMVSCMGR_STATUS_CARD_CREATED",
    "TPMVSCMGR_STATUS_CARD_DESTROYED",
    "TPMVSCMGR_STATUS_GENERATE_AUTHENTICATING",
    "TPMVSCMGR_STATUS_GENERATE_RUNNING",
    "TPMVSCMGR_STATUS_GENERATE_WAITING",
    "TPMVSCMGR_STATUS_VGIDSSIMULATOR_CREATING",
    "TPMVSCMGR_STATUS_VGIDSSIMULATOR_DESTROYING",
    "TPMVSCMGR_STATUS_VGIDSSIMULATOR_INITIALIZING",
    "TPMVSCMGR_STATUS_VREADER_CREATING",
    "TPMVSCMGR_STATUS_VREADER_DESTROYING",
    "TPMVSCMGR_STATUS_VREADER_INITIALIZING",
    "TPMVSCMGR_STATUS_VTPMSMARTCARD_CREATING",
    "TPMVSCMGR_STATUS_VTPMSMARTCARD_DESTROYING",
    "TPMVSCMGR_STATUS_VTPMSMARTCARD_INITIALIZING",
    "TPMVSC_ATTESTATION_AIK_AND_CERTIFICATE",
    "TPMVSC_ATTESTATION_AIK_ONLY",
    "TPMVSC_ATTESTATION_NONE",
    "TPMVSC_ATTESTATION_TYPE",
    "TPMVSC_DEFAULT_ADMIN_ALGORITHM_ID",
    "TpmVirtualSmartCardManager",
]
