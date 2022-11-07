from win32more import *
import win32more.Foundation
import win32more.Security.Tpm
import win32more.System.Com

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
TPMVSC_DEFAULT_ADMIN_ALGORITHM_ID = 130
TpmVirtualSmartCardManager = Guid('16a18e86-7f6e-4c20-ad89-4ffc0db7a96a')
RemoteTpmVirtualSmartCardManager = Guid('152ea2a8-70dc-4c59-8b2a-32aa3ca0dcac')
TPMVSC_ATTESTATION_TYPE = Int32
TPMVSC_ATTESTATION_NONE = 0
TPMVSC_ATTESTATION_AIK_ONLY = 1
TPMVSC_ATTESTATION_AIK_AND_CERTIFICATE = 2
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
def _define_ITpmVirtualSmartCardManagerStatusCallback_head():
    class ITpmVirtualSmartCardManagerStatusCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('1a1bb35f-abb8-451c-a1ae-33d98f1bef4a')
    return ITpmVirtualSmartCardManagerStatusCallback
def _define_ITpmVirtualSmartCardManagerStatusCallback():
    ITpmVirtualSmartCardManagerStatusCallback = win32more.Security.Tpm.ITpmVirtualSmartCardManagerStatusCallback_head
    ITpmVirtualSmartCardManagerStatusCallback.ReportProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Tpm.TPMVSCMGR_STATUS, use_last_error=False)(3, 'ReportProgress', ((1, 'Status'),)))
    ITpmVirtualSmartCardManagerStatusCallback.ReportError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.Tpm.TPMVSCMGR_ERROR, use_last_error=False)(4, 'ReportError', ((1, 'Error'),)))
    win32more.System.Com.IUnknown
    return ITpmVirtualSmartCardManagerStatusCallback
def _define_ITpmVirtualSmartCardManager_head():
    class ITpmVirtualSmartCardManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('112b1dff-d9dc-41f7-869f-d67fee7cb591')
    return ITpmVirtualSmartCardManager
def _define_ITpmVirtualSmartCardManager():
    ITpmVirtualSmartCardManager = win32more.Security.Tpm.ITpmVirtualSmartCardManager_head
    ITpmVirtualSmartCardManager.CreateVirtualSmartCard = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Byte,POINTER(Byte),UInt32,POINTER(Byte),UInt32,POINTER(Byte),UInt32,POINTER(Byte),UInt32,win32more.Foundation.BOOL,win32more.Security.Tpm.ITpmVirtualSmartCardManagerStatusCallback_head,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'CreateVirtualSmartCard', ((1, 'pszFriendlyName'),(1, 'bAdminAlgId'),(1, 'pbAdminKey'),(1, 'cbAdminKey'),(1, 'pbAdminKcv'),(1, 'cbAdminKcv'),(1, 'pbPuk'),(1, 'cbPuk'),(1, 'pbPin'),(1, 'cbPin'),(1, 'fGenerate'),(1, 'pStatusCallback'),(1, 'ppszInstanceId'),(1, 'pfNeedReboot'),)))
    ITpmVirtualSmartCardManager.DestroyVirtualSmartCard = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Security.Tpm.ITpmVirtualSmartCardManagerStatusCallback_head,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'DestroyVirtualSmartCard', ((1, 'pszInstanceId'),(1, 'pStatusCallback'),(1, 'pfNeedReboot'),)))
    win32more.System.Com.IUnknown
    return ITpmVirtualSmartCardManager
def _define_ITpmVirtualSmartCardManager2_head():
    class ITpmVirtualSmartCardManager2(win32more.Security.Tpm.ITpmVirtualSmartCardManager_head):
        Guid = Guid('fdf8a2b9-02de-47f4-bc26-aa85ab5e5267')
    return ITpmVirtualSmartCardManager2
def _define_ITpmVirtualSmartCardManager2():
    ITpmVirtualSmartCardManager2 = win32more.Security.Tpm.ITpmVirtualSmartCardManager2_head
    ITpmVirtualSmartCardManager2.CreateVirtualSmartCardWithPinPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Byte,POINTER(Byte),UInt32,POINTER(Byte),UInt32,POINTER(Byte),UInt32,POINTER(Byte),UInt32,POINTER(Byte),UInt32,win32more.Foundation.BOOL,win32more.Security.Tpm.ITpmVirtualSmartCardManagerStatusCallback_head,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'CreateVirtualSmartCardWithPinPolicy', ((1, 'pszFriendlyName'),(1, 'bAdminAlgId'),(1, 'pbAdminKey'),(1, 'cbAdminKey'),(1, 'pbAdminKcv'),(1, 'cbAdminKcv'),(1, 'pbPuk'),(1, 'cbPuk'),(1, 'pbPin'),(1, 'cbPin'),(1, 'pbPinPolicy'),(1, 'cbPinPolicy'),(1, 'fGenerate'),(1, 'pStatusCallback'),(1, 'ppszInstanceId'),(1, 'pfNeedReboot'),)))
    win32more.Security.Tpm.ITpmVirtualSmartCardManager
    return ITpmVirtualSmartCardManager2
def _define_ITpmVirtualSmartCardManager3_head():
    class ITpmVirtualSmartCardManager3(win32more.Security.Tpm.ITpmVirtualSmartCardManager2_head):
        Guid = Guid('3c745a97-f375-4150-be17-5950f694c699')
    return ITpmVirtualSmartCardManager3
def _define_ITpmVirtualSmartCardManager3():
    ITpmVirtualSmartCardManager3 = win32more.Security.Tpm.ITpmVirtualSmartCardManager3_head
    ITpmVirtualSmartCardManager3.CreateVirtualSmartCardWithAttestation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Byte,POINTER(Byte),UInt32,POINTER(Byte),UInt32,POINTER(Byte),UInt32,POINTER(Byte),UInt32,POINTER(Byte),UInt32,win32more.Security.Tpm.TPMVSC_ATTESTATION_TYPE,win32more.Foundation.BOOL,win32more.Security.Tpm.ITpmVirtualSmartCardManagerStatusCallback_head,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(6, 'CreateVirtualSmartCardWithAttestation', ((1, 'pszFriendlyName'),(1, 'bAdminAlgId'),(1, 'pbAdminKey'),(1, 'cbAdminKey'),(1, 'pbAdminKcv'),(1, 'cbAdminKcv'),(1, 'pbPuk'),(1, 'cbPuk'),(1, 'pbPin'),(1, 'cbPin'),(1, 'pbPinPolicy'),(1, 'cbPinPolicy'),(1, 'attestationType'),(1, 'fGenerate'),(1, 'pStatusCallback'),(1, 'ppszInstanceId'),)))
    win32more.Security.Tpm.ITpmVirtualSmartCardManager2
    return ITpmVirtualSmartCardManager3
__all__ = [
    "TPMVSC_DEFAULT_ADMIN_ALGORITHM_ID",
    "TpmVirtualSmartCardManager",
    "RemoteTpmVirtualSmartCardManager",
    "TPMVSC_ATTESTATION_TYPE",
    "TPMVSC_ATTESTATION_NONE",
    "TPMVSC_ATTESTATION_AIK_ONLY",
    "TPMVSC_ATTESTATION_AIK_AND_CERTIFICATE",
    "TPMVSCMGR_STATUS",
    "TPMVSCMGR_STATUS_VTPMSMARTCARD_INITIALIZING",
    "TPMVSCMGR_STATUS_VTPMSMARTCARD_CREATING",
    "TPMVSCMGR_STATUS_VTPMSMARTCARD_DESTROYING",
    "TPMVSCMGR_STATUS_VGIDSSIMULATOR_INITIALIZING",
    "TPMVSCMGR_STATUS_VGIDSSIMULATOR_CREATING",
    "TPMVSCMGR_STATUS_VGIDSSIMULATOR_DESTROYING",
    "TPMVSCMGR_STATUS_VREADER_INITIALIZING",
    "TPMVSCMGR_STATUS_VREADER_CREATING",
    "TPMVSCMGR_STATUS_VREADER_DESTROYING",
    "TPMVSCMGR_STATUS_GENERATE_WAITING",
    "TPMVSCMGR_STATUS_GENERATE_AUTHENTICATING",
    "TPMVSCMGR_STATUS_GENERATE_RUNNING",
    "TPMVSCMGR_STATUS_CARD_CREATED",
    "TPMVSCMGR_STATUS_CARD_DESTROYED",
    "TPMVSCMGR_ERROR",
    "TPMVSCMGR_ERROR_IMPERSONATION",
    "TPMVSCMGR_ERROR_PIN_COMPLEXITY",
    "TPMVSCMGR_ERROR_READER_COUNT_LIMIT",
    "TPMVSCMGR_ERROR_TERMINAL_SERVICES_SESSION",
    "TPMVSCMGR_ERROR_VTPMSMARTCARD_INITIALIZE",
    "TPMVSCMGR_ERROR_VTPMSMARTCARD_CREATE",
    "TPMVSCMGR_ERROR_VTPMSMARTCARD_DESTROY",
    "TPMVSCMGR_ERROR_VGIDSSIMULATOR_INITIALIZE",
    "TPMVSCMGR_ERROR_VGIDSSIMULATOR_CREATE",
    "TPMVSCMGR_ERROR_VGIDSSIMULATOR_DESTROY",
    "TPMVSCMGR_ERROR_VGIDSSIMULATOR_WRITE_PROPERTY",
    "TPMVSCMGR_ERROR_VGIDSSIMULATOR_READ_PROPERTY",
    "TPMVSCMGR_ERROR_VREADER_INITIALIZE",
    "TPMVSCMGR_ERROR_VREADER_CREATE",
    "TPMVSCMGR_ERROR_VREADER_DESTROY",
    "TPMVSCMGR_ERROR_GENERATE_LOCATE_READER",
    "TPMVSCMGR_ERROR_GENERATE_FILESYSTEM",
    "TPMVSCMGR_ERROR_CARD_CREATE",
    "TPMVSCMGR_ERROR_CARD_DESTROY",
    "ITpmVirtualSmartCardManagerStatusCallback",
    "ITpmVirtualSmartCardManager",
    "ITpmVirtualSmartCardManager2",
    "ITpmVirtualSmartCardManager3",
]
