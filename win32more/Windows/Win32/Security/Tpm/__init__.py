from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security.Tpm
import win32more.Windows.Win32.System.Com
TPMVSC_DEFAULT_ADMIN_ALGORITHM_ID: UInt32 = 130
class ITpmVirtualSmartCardManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{112b1dff-d9dc-41f7-869f-d67fee7cb591}')
    @commethod(3)
    def CreateVirtualSmartCard(self, pszFriendlyName: win32more.Windows.Win32.Foundation.PWSTR, bAdminAlgId: Byte, pbAdminKey: POINTER(Byte), cbAdminKey: UInt32, pbAdminKcv: POINTER(Byte), cbAdminKcv: UInt32, pbPuk: POINTER(Byte), cbPuk: UInt32, pbPin: POINTER(Byte), cbPin: UInt32, fGenerate: win32more.Windows.Win32.Foundation.BOOL, pStatusCallback: win32more.Windows.Win32.Security.Tpm.ITpmVirtualSmartCardManagerStatusCallback, ppszInstanceId: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pfNeedReboot: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DestroyVirtualSmartCard(self, pszInstanceId: win32more.Windows.Win32.Foundation.PWSTR, pStatusCallback: win32more.Windows.Win32.Security.Tpm.ITpmVirtualSmartCardManagerStatusCallback, pfNeedReboot: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITpmVirtualSmartCardManager2(ComPtr):
    extends: win32more.Windows.Win32.Security.Tpm.ITpmVirtualSmartCardManager
    _iid_ = Guid('{fdf8a2b9-02de-47f4-bc26-aa85ab5e5267}')
    @commethod(5)
    def CreateVirtualSmartCardWithPinPolicy(self, pszFriendlyName: win32more.Windows.Win32.Foundation.PWSTR, bAdminAlgId: Byte, pbAdminKey: POINTER(Byte), cbAdminKey: UInt32, pbAdminKcv: POINTER(Byte), cbAdminKcv: UInt32, pbPuk: POINTER(Byte), cbPuk: UInt32, pbPin: POINTER(Byte), cbPin: UInt32, pbPinPolicy: POINTER(Byte), cbPinPolicy: UInt32, fGenerate: win32more.Windows.Win32.Foundation.BOOL, pStatusCallback: win32more.Windows.Win32.Security.Tpm.ITpmVirtualSmartCardManagerStatusCallback, ppszInstanceId: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pfNeedReboot: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITpmVirtualSmartCardManager3(ComPtr):
    extends: win32more.Windows.Win32.Security.Tpm.ITpmVirtualSmartCardManager2
    _iid_ = Guid('{3c745a97-f375-4150-be17-5950f694c699}')
    @commethod(6)
    def CreateVirtualSmartCardWithAttestation(self, pszFriendlyName: win32more.Windows.Win32.Foundation.PWSTR, bAdminAlgId: Byte, pbAdminKey: POINTER(Byte), cbAdminKey: UInt32, pbAdminKcv: POINTER(Byte), cbAdminKcv: UInt32, pbPuk: POINTER(Byte), cbPuk: UInt32, pbPin: POINTER(Byte), cbPin: UInt32, pbPinPolicy: POINTER(Byte), cbPinPolicy: UInt32, attestationType: win32more.Windows.Win32.Security.Tpm.TPMVSC_ATTESTATION_TYPE, fGenerate: win32more.Windows.Win32.Foundation.BOOL, pStatusCallback: win32more.Windows.Win32.Security.Tpm.ITpmVirtualSmartCardManagerStatusCallback, ppszInstanceId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITpmVirtualSmartCardManagerStatusCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1a1bb35f-abb8-451c-a1ae-33d98f1bef4a}')
    @commethod(3)
    def ReportProgress(self, Status: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_STATUS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReportError(self, Error: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_ERROR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
RemoteTpmVirtualSmartCardManager = Guid('{152ea2a8-70dc-4c59-8b2a-32aa3ca0dcac}')
TPMVSCMGR_ERROR = Int32
TPMVSCMGR_ERROR_IMPERSONATION: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_ERROR = 0
TPMVSCMGR_ERROR_PIN_COMPLEXITY: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_ERROR = 1
TPMVSCMGR_ERROR_READER_COUNT_LIMIT: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_ERROR = 2
TPMVSCMGR_ERROR_TERMINAL_SERVICES_SESSION: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_ERROR = 3
TPMVSCMGR_ERROR_VTPMSMARTCARD_INITIALIZE: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_ERROR = 4
TPMVSCMGR_ERROR_VTPMSMARTCARD_CREATE: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_ERROR = 5
TPMVSCMGR_ERROR_VTPMSMARTCARD_DESTROY: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_ERROR = 6
TPMVSCMGR_ERROR_VGIDSSIMULATOR_INITIALIZE: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_ERROR = 7
TPMVSCMGR_ERROR_VGIDSSIMULATOR_CREATE: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_ERROR = 8
TPMVSCMGR_ERROR_VGIDSSIMULATOR_DESTROY: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_ERROR = 9
TPMVSCMGR_ERROR_VGIDSSIMULATOR_WRITE_PROPERTY: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_ERROR = 10
TPMVSCMGR_ERROR_VGIDSSIMULATOR_READ_PROPERTY: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_ERROR = 11
TPMVSCMGR_ERROR_VREADER_INITIALIZE: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_ERROR = 12
TPMVSCMGR_ERROR_VREADER_CREATE: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_ERROR = 13
TPMVSCMGR_ERROR_VREADER_DESTROY: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_ERROR = 14
TPMVSCMGR_ERROR_GENERATE_LOCATE_READER: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_ERROR = 15
TPMVSCMGR_ERROR_GENERATE_FILESYSTEM: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_ERROR = 16
TPMVSCMGR_ERROR_CARD_CREATE: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_ERROR = 17
TPMVSCMGR_ERROR_CARD_DESTROY: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_ERROR = 18
TPMVSCMGR_STATUS = Int32
TPMVSCMGR_STATUS_VTPMSMARTCARD_INITIALIZING: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_STATUS = 0
TPMVSCMGR_STATUS_VTPMSMARTCARD_CREATING: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_STATUS = 1
TPMVSCMGR_STATUS_VTPMSMARTCARD_DESTROYING: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_STATUS = 2
TPMVSCMGR_STATUS_VGIDSSIMULATOR_INITIALIZING: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_STATUS = 3
TPMVSCMGR_STATUS_VGIDSSIMULATOR_CREATING: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_STATUS = 4
TPMVSCMGR_STATUS_VGIDSSIMULATOR_DESTROYING: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_STATUS = 5
TPMVSCMGR_STATUS_VREADER_INITIALIZING: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_STATUS = 6
TPMVSCMGR_STATUS_VREADER_CREATING: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_STATUS = 7
TPMVSCMGR_STATUS_VREADER_DESTROYING: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_STATUS = 8
TPMVSCMGR_STATUS_GENERATE_WAITING: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_STATUS = 9
TPMVSCMGR_STATUS_GENERATE_AUTHENTICATING: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_STATUS = 10
TPMVSCMGR_STATUS_GENERATE_RUNNING: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_STATUS = 11
TPMVSCMGR_STATUS_CARD_CREATED: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_STATUS = 12
TPMVSCMGR_STATUS_CARD_DESTROYED: win32more.Windows.Win32.Security.Tpm.TPMVSCMGR_STATUS = 13
TPMVSC_ATTESTATION_TYPE = Int32
TPMVSC_ATTESTATION_NONE: win32more.Windows.Win32.Security.Tpm.TPMVSC_ATTESTATION_TYPE = 0
TPMVSC_ATTESTATION_AIK_ONLY: win32more.Windows.Win32.Security.Tpm.TPMVSC_ATTESTATION_TYPE = 1
TPMVSC_ATTESTATION_AIK_AND_CERTIFICATE: win32more.Windows.Win32.Security.Tpm.TPMVSC_ATTESTATION_TYPE = 2
TpmVirtualSmartCardManager = Guid('{16a18e86-7f6e-4c20-ad89-4ffc0db7a96a}')


make_ready(__name__)
