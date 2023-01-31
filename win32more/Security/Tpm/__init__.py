from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Security.Tpm
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
TPMVSC_DEFAULT_ADMIN_ALGORITHM_ID: UInt32 = 130
class ITpmVirtualSmartCardManager(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('112b1dff-d9dc-41f7-86-9f-d6-7f-ee-7c-b5-91')
    @commethod(3)
    def CreateVirtualSmartCard(pszFriendlyName: win32more.Foundation.PWSTR, bAdminAlgId: Byte, pbAdminKey: c_char_p_no, cbAdminKey: UInt32, pbAdminKcv: c_char_p_no, cbAdminKcv: UInt32, pbPuk: c_char_p_no, cbPuk: UInt32, pbPin: c_char_p_no, cbPin: UInt32, fGenerate: win32more.Foundation.BOOL, pStatusCallback: win32more.Security.Tpm.ITpmVirtualSmartCardManagerStatusCallback_head, ppszInstanceId: POINTER(win32more.Foundation.PWSTR), pfNeedReboot: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def DestroyVirtualSmartCard(pszInstanceId: win32more.Foundation.PWSTR, pStatusCallback: win32more.Security.Tpm.ITpmVirtualSmartCardManagerStatusCallback_head, pfNeedReboot: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class ITpmVirtualSmartCardManager2(c_void_p):
    extends: win32more.Security.Tpm.ITpmVirtualSmartCardManager
    Guid = Guid('fdf8a2b9-02de-47f4-bc-26-aa-85-ab-5e-52-67')
    @commethod(5)
    def CreateVirtualSmartCardWithPinPolicy(pszFriendlyName: win32more.Foundation.PWSTR, bAdminAlgId: Byte, pbAdminKey: c_char_p_no, cbAdminKey: UInt32, pbAdminKcv: c_char_p_no, cbAdminKcv: UInt32, pbPuk: c_char_p_no, cbPuk: UInt32, pbPin: c_char_p_no, cbPin: UInt32, pbPinPolicy: c_char_p_no, cbPinPolicy: UInt32, fGenerate: win32more.Foundation.BOOL, pStatusCallback: win32more.Security.Tpm.ITpmVirtualSmartCardManagerStatusCallback_head, ppszInstanceId: POINTER(win32more.Foundation.PWSTR), pfNeedReboot: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class ITpmVirtualSmartCardManager3(c_void_p):
    extends: win32more.Security.Tpm.ITpmVirtualSmartCardManager2
    Guid = Guid('3c745a97-f375-4150-be-17-59-50-f6-94-c6-99')
    @commethod(6)
    def CreateVirtualSmartCardWithAttestation(pszFriendlyName: win32more.Foundation.PWSTR, bAdminAlgId: Byte, pbAdminKey: c_char_p_no, cbAdminKey: UInt32, pbAdminKcv: c_char_p_no, cbAdminKcv: UInt32, pbPuk: c_char_p_no, cbPuk: UInt32, pbPin: c_char_p_no, cbPin: UInt32, pbPinPolicy: c_char_p_no, cbPinPolicy: UInt32, attestationType: win32more.Security.Tpm.TPMVSC_ATTESTATION_TYPE, fGenerate: win32more.Foundation.BOOL, pStatusCallback: win32more.Security.Tpm.ITpmVirtualSmartCardManagerStatusCallback_head, ppszInstanceId: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
class ITpmVirtualSmartCardManagerStatusCallback(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1a1bb35f-abb8-451c-a1-ae-33-d9-8f-1b-ef-4a')
    @commethod(3)
    def ReportProgress(Status: win32more.Security.Tpm.TPMVSCMGR_STATUS) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ReportError(Error: win32more.Security.Tpm.TPMVSCMGR_ERROR) -> win32more.Foundation.HRESULT: ...
RemoteTpmVirtualSmartCardManager = Guid('152ea2a8-70dc-4c59-8b-2a-32-aa-3c-a0-dc-ac')
TPMVSCMGR_ERROR = Int32
TPMVSCMGR_ERROR_IMPERSONATION: TPMVSCMGR_ERROR = 0
TPMVSCMGR_ERROR_PIN_COMPLEXITY: TPMVSCMGR_ERROR = 1
TPMVSCMGR_ERROR_READER_COUNT_LIMIT: TPMVSCMGR_ERROR = 2
TPMVSCMGR_ERROR_TERMINAL_SERVICES_SESSION: TPMVSCMGR_ERROR = 3
TPMVSCMGR_ERROR_VTPMSMARTCARD_INITIALIZE: TPMVSCMGR_ERROR = 4
TPMVSCMGR_ERROR_VTPMSMARTCARD_CREATE: TPMVSCMGR_ERROR = 5
TPMVSCMGR_ERROR_VTPMSMARTCARD_DESTROY: TPMVSCMGR_ERROR = 6
TPMVSCMGR_ERROR_VGIDSSIMULATOR_INITIALIZE: TPMVSCMGR_ERROR = 7
TPMVSCMGR_ERROR_VGIDSSIMULATOR_CREATE: TPMVSCMGR_ERROR = 8
TPMVSCMGR_ERROR_VGIDSSIMULATOR_DESTROY: TPMVSCMGR_ERROR = 9
TPMVSCMGR_ERROR_VGIDSSIMULATOR_WRITE_PROPERTY: TPMVSCMGR_ERROR = 10
TPMVSCMGR_ERROR_VGIDSSIMULATOR_READ_PROPERTY: TPMVSCMGR_ERROR = 11
TPMVSCMGR_ERROR_VREADER_INITIALIZE: TPMVSCMGR_ERROR = 12
TPMVSCMGR_ERROR_VREADER_CREATE: TPMVSCMGR_ERROR = 13
TPMVSCMGR_ERROR_VREADER_DESTROY: TPMVSCMGR_ERROR = 14
TPMVSCMGR_ERROR_GENERATE_LOCATE_READER: TPMVSCMGR_ERROR = 15
TPMVSCMGR_ERROR_GENERATE_FILESYSTEM: TPMVSCMGR_ERROR = 16
TPMVSCMGR_ERROR_CARD_CREATE: TPMVSCMGR_ERROR = 17
TPMVSCMGR_ERROR_CARD_DESTROY: TPMVSCMGR_ERROR = 18
TPMVSCMGR_STATUS = Int32
TPMVSCMGR_STATUS_VTPMSMARTCARD_INITIALIZING: TPMVSCMGR_STATUS = 0
TPMVSCMGR_STATUS_VTPMSMARTCARD_CREATING: TPMVSCMGR_STATUS = 1
TPMVSCMGR_STATUS_VTPMSMARTCARD_DESTROYING: TPMVSCMGR_STATUS = 2
TPMVSCMGR_STATUS_VGIDSSIMULATOR_INITIALIZING: TPMVSCMGR_STATUS = 3
TPMVSCMGR_STATUS_VGIDSSIMULATOR_CREATING: TPMVSCMGR_STATUS = 4
TPMVSCMGR_STATUS_VGIDSSIMULATOR_DESTROYING: TPMVSCMGR_STATUS = 5
TPMVSCMGR_STATUS_VREADER_INITIALIZING: TPMVSCMGR_STATUS = 6
TPMVSCMGR_STATUS_VREADER_CREATING: TPMVSCMGR_STATUS = 7
TPMVSCMGR_STATUS_VREADER_DESTROYING: TPMVSCMGR_STATUS = 8
TPMVSCMGR_STATUS_GENERATE_WAITING: TPMVSCMGR_STATUS = 9
TPMVSCMGR_STATUS_GENERATE_AUTHENTICATING: TPMVSCMGR_STATUS = 10
TPMVSCMGR_STATUS_GENERATE_RUNNING: TPMVSCMGR_STATUS = 11
TPMVSCMGR_STATUS_CARD_CREATED: TPMVSCMGR_STATUS = 12
TPMVSCMGR_STATUS_CARD_DESTROYED: TPMVSCMGR_STATUS = 13
TPMVSC_ATTESTATION_TYPE = Int32
TPMVSC_ATTESTATION_NONE: TPMVSC_ATTESTATION_TYPE = 0
TPMVSC_ATTESTATION_AIK_ONLY: TPMVSC_ATTESTATION_TYPE = 1
TPMVSC_ATTESTATION_AIK_AND_CERTIFICATE: TPMVSC_ATTESTATION_TYPE = 2
TpmVirtualSmartCardManager = Guid('16a18e86-7f6e-4c20-ad-89-4f-fc-0d-b7-a9-6a')
make_head(_module, 'ITpmVirtualSmartCardManager')
make_head(_module, 'ITpmVirtualSmartCardManager2')
make_head(_module, 'ITpmVirtualSmartCardManager3')
make_head(_module, 'ITpmVirtualSmartCardManagerStatusCallback')
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
_arch_optional = [
]
