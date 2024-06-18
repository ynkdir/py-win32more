from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.TpmBaseServices
TBS_CONTEXT_VERSION_ONE: UInt32 = 1
TBS_SUCCESS: UInt32 = 0
TBS_OWNERAUTH_TYPE_FULL: UInt32 = 1
TBS_OWNERAUTH_TYPE_ADMIN: UInt32 = 2
TBS_OWNERAUTH_TYPE_USER: UInt32 = 3
TBS_OWNERAUTH_TYPE_ENDORSEMENT: UInt32 = 4
TBS_OWNERAUTH_TYPE_ENDORSEMENT_20: UInt32 = 12
TBS_OWNERAUTH_TYPE_STORAGE_20: UInt32 = 13
TBS_CONTEXT_VERSION_TWO: UInt32 = 2
TPM_WNF_INFO_CLEAR_SUCCESSFUL: UInt32 = 1
TPM_WNF_INFO_OWNERSHIP_SUCCESSFUL: UInt32 = 2
TPM_WNF_INFO_NO_REBOOT_REQUIRED: UInt32 = 1
TPM_VERSION_UNKNOWN: UInt32 = 0
TPM_VERSION_12: UInt32 = 1
TPM_VERSION_20: UInt32 = 2
TPM_IFTYPE_UNKNOWN: UInt32 = 0
TPM_IFTYPE_1: UInt32 = 1
TPM_IFTYPE_TRUSTZONE: UInt32 = 2
TPM_IFTYPE_HW: UInt32 = 3
TPM_IFTYPE_EMULATOR: UInt32 = 4
TPM_IFTYPE_SPB: UInt32 = 5
TBS_TCGLOG_SRTM_CURRENT: UInt32 = 0
TBS_TCGLOG_DRTM_CURRENT: UInt32 = 1
TBS_TCGLOG_SRTM_BOOT: UInt32 = 2
TBS_TCGLOG_SRTM_RESUME: UInt32 = 3
TBS_TCGLOG_DRTM_BOOT: UInt32 = 4
TBS_TCGLOG_DRTM_RESUME: UInt32 = 5
@winfunctype('tbs.dll')
def Tbsi_Context_Create(pContextParams: POINTER(win32more.Windows.Win32.System.TpmBaseServices.TBS_CONTEXT_PARAMS), phContext: POINTER(VoidPtr)) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsip_Context_Close(hContext: VoidPtr) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsip_Submit_Command(hContext: VoidPtr, Locality: win32more.Windows.Win32.System.TpmBaseServices.TBS_COMMAND_LOCALITY, Priority: win32more.Windows.Win32.System.TpmBaseServices.TBS_COMMAND_PRIORITY, pabCommand: POINTER(Byte), cbCommand: UInt32, pabResult: POINTER(Byte), pcbResult: POINTER(UInt32)) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsip_Cancel_Commands(hContext: VoidPtr) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsi_Physical_Presence_Command(hContext: VoidPtr, pabInput: POINTER(Byte), cbInput: UInt32, pabOutput: POINTER(Byte), pcbOutput: POINTER(UInt32)) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsi_Get_TCG_Log(hContext: VoidPtr, pOutputBuf: POINTER(Byte), pOutputBufLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsi_GetDeviceInfo(Size: UInt32, Info: VoidPtr) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsi_Get_OwnerAuth(hContext: VoidPtr, ownerauthType: UInt32, pOutputBuf: POINTER(Byte), pOutputBufLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsi_Revoke_Attestation() -> UInt32: ...
@winfunctype('tbs.dll')
def GetDeviceID(pbWindowsAIK: POINTER(Byte), cbWindowsAIK: UInt32, pcbResult: POINTER(UInt32), pfProtectedByTPM: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('tbs.dll')
def GetDeviceIDString(pszWindowsAIK: win32more.Windows.Win32.Foundation.PWSTR, cchWindowsAIK: UInt32, pcchResult: POINTER(UInt32), pfProtectedByTPM: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('tbs.dll')
def Tbsi_Create_Windows_Key(keyHandle: UInt32) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsi_Get_TCG_Log_Ex(logType: UInt32, pbOutput: POINTER(Byte), pcbOutput: POINTER(UInt32)) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsi_Is_Tpm_Present() -> win32more.Windows.Win32.Foundation.BOOL: ...
TBS_COMMAND_LOCALITY = UInt32
TBS_COMMAND_LOCALITY_ZERO: win32more.Windows.Win32.System.TpmBaseServices.TBS_COMMAND_LOCALITY = 0
TBS_COMMAND_LOCALITY_ONE: win32more.Windows.Win32.System.TpmBaseServices.TBS_COMMAND_LOCALITY = 1
TBS_COMMAND_LOCALITY_TWO: win32more.Windows.Win32.System.TpmBaseServices.TBS_COMMAND_LOCALITY = 2
TBS_COMMAND_LOCALITY_THREE: win32more.Windows.Win32.System.TpmBaseServices.TBS_COMMAND_LOCALITY = 3
TBS_COMMAND_LOCALITY_FOUR: win32more.Windows.Win32.System.TpmBaseServices.TBS_COMMAND_LOCALITY = 4
TBS_COMMAND_PRIORITY = UInt32
TBS_COMMAND_PRIORITY_LOW: win32more.Windows.Win32.System.TpmBaseServices.TBS_COMMAND_PRIORITY = 100
TBS_COMMAND_PRIORITY_NORMAL: win32more.Windows.Win32.System.TpmBaseServices.TBS_COMMAND_PRIORITY = 200
TBS_COMMAND_PRIORITY_SYSTEM: win32more.Windows.Win32.System.TpmBaseServices.TBS_COMMAND_PRIORITY = 400
TBS_COMMAND_PRIORITY_HIGH: win32more.Windows.Win32.System.TpmBaseServices.TBS_COMMAND_PRIORITY = 300
TBS_COMMAND_PRIORITY_MAX: win32more.Windows.Win32.System.TpmBaseServices.TBS_COMMAND_PRIORITY = 2147483648
class TBS_CONTEXT_PARAMS(Structure):
    version: UInt32
class TBS_CONTEXT_PARAMS2(Structure):
    version: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        asUINT32: UInt32
        class _Anonymous_e__Struct(Structure):
            requestRaw: Annotated[UInt32, 1]
            includeTpm12: Annotated[UInt32, 1]
            includeTpm20: Annotated[UInt32, 1]
class TPM_DEVICE_INFO(Structure):
    structVersion: UInt32
    tpmVersion: UInt32
    tpmInterfaceType: UInt32
    tpmImpRevision: UInt32
class TPM_WNF_PROVISIONING(Structure):
    status: UInt32
    message: Byte * 28


make_ready(__name__)
