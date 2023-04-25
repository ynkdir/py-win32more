from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation
import Windows.Win32.System.TpmBaseServices
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
def Tbsi_Context_Create(pContextParams: POINTER(Windows.Win32.System.TpmBaseServices.TBS_CONTEXT_PARAMS_head), phContext: POINTER(c_void_p)) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsip_Context_Close(hContext: c_void_p) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsip_Submit_Command(hContext: c_void_p, Locality: Windows.Win32.System.TpmBaseServices.TBS_COMMAND_LOCALITY, Priority: Windows.Win32.System.TpmBaseServices.TBS_COMMAND_PRIORITY, pabCommand: POINTER(Byte), cbCommand: UInt32, pabResult: POINTER(Byte), pcbResult: POINTER(UInt32)) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsip_Cancel_Commands(hContext: c_void_p) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsi_Physical_Presence_Command(hContext: c_void_p, pabInput: POINTER(Byte), cbInput: UInt32, pabOutput: POINTER(Byte), pcbOutput: POINTER(UInt32)) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsi_Get_TCG_Log(hContext: c_void_p, pOutputBuf: POINTER(Byte), pOutputBufLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsi_GetDeviceInfo(Size: UInt32, Info: c_void_p) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsi_Get_OwnerAuth(hContext: c_void_p, ownerauthType: UInt32, pOutputBuf: POINTER(Byte), pOutputBufLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsi_Revoke_Attestation() -> UInt32: ...
@winfunctype('tbs.dll')
def GetDeviceID(pbWindowsAIK: POINTER(Byte), cbWindowsAIK: UInt32, pcbResult: POINTER(UInt32), pfProtectedByTPM: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('tbs.dll')
def GetDeviceIDString(pszWindowsAIK: Windows.Win32.Foundation.PWSTR, cchWindowsAIK: UInt32, pcchResult: POINTER(UInt32), pfProtectedByTPM: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('tbs.dll')
def Tbsi_Create_Windows_Key(keyHandle: UInt32) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsi_Get_TCG_Log_Ex(logType: UInt32, pbOutput: POINTER(Byte), pcbOutput: POINTER(UInt32)) -> UInt32: ...
TBS_COMMAND_LOCALITY = UInt32
TBS_COMMAND_LOCALITY_ZERO: TBS_COMMAND_LOCALITY = 0
TBS_COMMAND_LOCALITY_ONE: TBS_COMMAND_LOCALITY = 1
TBS_COMMAND_LOCALITY_TWO: TBS_COMMAND_LOCALITY = 2
TBS_COMMAND_LOCALITY_THREE: TBS_COMMAND_LOCALITY = 3
TBS_COMMAND_LOCALITY_FOUR: TBS_COMMAND_LOCALITY = 4
TBS_COMMAND_PRIORITY = UInt32
TBS_COMMAND_PRIORITY_LOW: TBS_COMMAND_PRIORITY = 100
TBS_COMMAND_PRIORITY_NORMAL: TBS_COMMAND_PRIORITY = 200
TBS_COMMAND_PRIORITY_SYSTEM: TBS_COMMAND_PRIORITY = 400
TBS_COMMAND_PRIORITY_HIGH: TBS_COMMAND_PRIORITY = 300
TBS_COMMAND_PRIORITY_MAX: TBS_COMMAND_PRIORITY = 2147483648
class TBS_CONTEXT_PARAMS(EasyCastStructure):
    version: UInt32
class TBS_CONTEXT_PARAMS2(EasyCastStructure):
    version: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        asUINT32: UInt32
        class _Anonymous_e__Struct(EasyCastStructure):
            _bitfield: UInt32
class TPM_DEVICE_INFO(EasyCastStructure):
    structVersion: UInt32
    tpmVersion: UInt32
    tpmInterfaceType: UInt32
    tpmImpRevision: UInt32
class TPM_WNF_PROVISIONING(EasyCastStructure):
    status: UInt32
    message: Byte * 28
make_head(_module, 'TBS_CONTEXT_PARAMS')
make_head(_module, 'TBS_CONTEXT_PARAMS2')
make_head(_module, 'TPM_DEVICE_INFO')
make_head(_module, 'TPM_WNF_PROVISIONING')
