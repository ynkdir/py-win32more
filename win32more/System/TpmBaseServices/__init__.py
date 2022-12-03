from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.TpmBaseServices
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
TBS_CONTEXT_VERSION_ONE = 1
TBS_SUCCESS = 0
TBS_OWNERAUTH_TYPE_FULL = 1
TBS_OWNERAUTH_TYPE_ADMIN = 2
TBS_OWNERAUTH_TYPE_USER = 3
TBS_OWNERAUTH_TYPE_ENDORSEMENT = 4
TBS_OWNERAUTH_TYPE_ENDORSEMENT_20 = 12
TBS_OWNERAUTH_TYPE_STORAGE_20 = 13
TBS_CONTEXT_VERSION_TWO = 2
TPM_WNF_INFO_CLEAR_SUCCESSFUL = 1
TPM_WNF_INFO_OWNERSHIP_SUCCESSFUL = 2
TPM_WNF_INFO_NO_REBOOT_REQUIRED = 1
TPM_VERSION_UNKNOWN = 0
TPM_VERSION_12 = 1
TPM_VERSION_20 = 2
TPM_IFTYPE_UNKNOWN = 0
TPM_IFTYPE_1 = 1
TPM_IFTYPE_TRUSTZONE = 2
TPM_IFTYPE_HW = 3
TPM_IFTYPE_EMULATOR = 4
TPM_IFTYPE_SPB = 5
TBS_TCGLOG_SRTM_CURRENT = 0
TBS_TCGLOG_DRTM_CURRENT = 1
TBS_TCGLOG_SRTM_BOOT = 2
TBS_TCGLOG_SRTM_RESUME = 3
TBS_TCGLOG_DRTM_BOOT = 4
TBS_TCGLOG_DRTM_RESUME = 5
def _define_Tbsi_Context_Create():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.TpmBaseServices.TBS_CONTEXT_PARAMS_head),POINTER(c_void_p))(('Tbsi_Context_Create', windll['tbs.dll']), ((1, 'pContextParams'),(1, 'phContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Tbsip_Context_Close():
    try:
        return WINFUNCTYPE(UInt32,c_void_p)(('Tbsip_Context_Close', windll['tbs.dll']), ((1, 'hContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Tbsip_Submit_Command():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,win32more.System.TpmBaseServices.TBS_COMMAND_LOCALITY,win32more.System.TpmBaseServices.TBS_COMMAND_PRIORITY,c_char_p_no,UInt32,c_char_p_no,POINTER(UInt32))(('Tbsip_Submit_Command', windll['tbs.dll']), ((1, 'hContext'),(1, 'Locality'),(1, 'Priority'),(1, 'pabCommand'),(1, 'cbCommand'),(1, 'pabResult'),(1, 'pcbResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Tbsip_Cancel_Commands():
    try:
        return WINFUNCTYPE(UInt32,c_void_p)(('Tbsip_Cancel_Commands', windll['tbs.dll']), ((1, 'hContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Tbsi_Physical_Presence_Command():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,c_char_p_no,UInt32,c_char_p_no,POINTER(UInt32))(('Tbsi_Physical_Presence_Command', windll['tbs.dll']), ((1, 'hContext'),(1, 'pabInput'),(1, 'cbInput'),(1, 'pabOutput'),(1, 'pcbOutput'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Tbsi_Get_TCG_Log():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,c_char_p_no,POINTER(UInt32))(('Tbsi_Get_TCG_Log', windll['tbs.dll']), ((1, 'hContext'),(1, 'pOutputBuf'),(1, 'pOutputBufLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Tbsi_GetDeviceInfo():
    try:
        return WINFUNCTYPE(UInt32,UInt32,c_void_p)(('Tbsi_GetDeviceInfo', windll['tbs.dll']), ((1, 'Size'),(1, 'Info'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Tbsi_Get_OwnerAuth():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,c_char_p_no,POINTER(UInt32))(('Tbsi_Get_OwnerAuth', windll['tbs.dll']), ((1, 'hContext'),(1, 'ownerauthType'),(1, 'pOutputBuf'),(1, 'pOutputBufLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Tbsi_Revoke_Attestation():
    try:
        return WINFUNCTYPE(UInt32,)(('Tbsi_Revoke_Attestation', windll['tbs.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDeviceID():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,POINTER(UInt32),POINTER(win32more.Foundation.BOOL))(('GetDeviceID', windll['tbs.dll']), ((1, 'pbWindowsAIK'),(1, 'cbWindowsAIK'),(1, 'pcbResult'),(1, 'pfProtectedByTPM'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDeviceIDString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),POINTER(win32more.Foundation.BOOL))(('GetDeviceIDString', windll['tbs.dll']), ((1, 'pszWindowsAIK'),(1, 'cchWindowsAIK'),(1, 'pcchResult'),(1, 'pfProtectedByTPM'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Tbsi_Create_Windows_Key():
    try:
        return WINFUNCTYPE(UInt32,UInt32)(('Tbsi_Create_Windows_Key', windll['tbs.dll']), ((1, 'keyHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Tbsi_Get_TCG_Log_Ex():
    try:
        return WINFUNCTYPE(UInt32,UInt32,c_char_p_no,POINTER(UInt32))(('Tbsi_Get_TCG_Log_Ex', windll['tbs.dll']), ((1, 'logType'),(1, 'pbOutput'),(1, 'pcbOutput'),))
    except (FileNotFoundError, AttributeError):
        return None
TBS_COMMAND_LOCALITY = UInt32
TBS_COMMAND_LOCALITY_ZERO = 0
TBS_COMMAND_LOCALITY_ONE = 1
TBS_COMMAND_LOCALITY_TWO = 2
TBS_COMMAND_LOCALITY_THREE = 3
TBS_COMMAND_LOCALITY_FOUR = 4
TBS_COMMAND_PRIORITY = UInt32
TBS_COMMAND_PRIORITY_LOW = 100
TBS_COMMAND_PRIORITY_NORMAL = 200
TBS_COMMAND_PRIORITY_SYSTEM = 400
TBS_COMMAND_PRIORITY_HIGH = 300
TBS_COMMAND_PRIORITY_MAX = 2147483648
def _define_TBS_CONTEXT_PARAMS_head():
    class TBS_CONTEXT_PARAMS(Structure):
        pass
    return TBS_CONTEXT_PARAMS
def _define_TBS_CONTEXT_PARAMS():
    TBS_CONTEXT_PARAMS = win32more.System.TpmBaseServices.TBS_CONTEXT_PARAMS_head
    TBS_CONTEXT_PARAMS._fields_ = [
        ('version', UInt32),
    ]
    return TBS_CONTEXT_PARAMS
def _define_TBS_CONTEXT_PARAMS2_head():
    class TBS_CONTEXT_PARAMS2(Structure):
        pass
    return TBS_CONTEXT_PARAMS2
def _define_TBS_CONTEXT_PARAMS2():
    TBS_CONTEXT_PARAMS2 = win32more.System.TpmBaseServices.TBS_CONTEXT_PARAMS2_head
    class TBS_CONTEXT_PARAMS2__Anonymous_e__Union(Union):
        pass
    class TBS_CONTEXT_PARAMS2__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    TBS_CONTEXT_PARAMS2__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ('_bitfield', UInt32),
    ]
    TBS_CONTEXT_PARAMS2__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    TBS_CONTEXT_PARAMS2__Anonymous_e__Union._fields_ = [
        ('Anonymous', TBS_CONTEXT_PARAMS2__Anonymous_e__Union__Anonymous_e__Struct),
        ('asUINT32', UInt32),
    ]
    TBS_CONTEXT_PARAMS2._anonymous_ = [
        'Anonymous',
    ]
    TBS_CONTEXT_PARAMS2._fields_ = [
        ('version', UInt32),
        ('Anonymous', TBS_CONTEXT_PARAMS2__Anonymous_e__Union),
    ]
    return TBS_CONTEXT_PARAMS2
def _define_TPM_DEVICE_INFO_head():
    class TPM_DEVICE_INFO(Structure):
        pass
    return TPM_DEVICE_INFO
def _define_TPM_DEVICE_INFO():
    TPM_DEVICE_INFO = win32more.System.TpmBaseServices.TPM_DEVICE_INFO_head
    TPM_DEVICE_INFO._fields_ = [
        ('structVersion', UInt32),
        ('tpmVersion', UInt32),
        ('tpmInterfaceType', UInt32),
        ('tpmImpRevision', UInt32),
    ]
    return TPM_DEVICE_INFO
def _define_TPM_WNF_PROVISIONING_head():
    class TPM_WNF_PROVISIONING(Structure):
        pass
    return TPM_WNF_PROVISIONING
def _define_TPM_WNF_PROVISIONING():
    TPM_WNF_PROVISIONING = win32more.System.TpmBaseServices.TPM_WNF_PROVISIONING_head
    TPM_WNF_PROVISIONING._fields_ = [
        ('status', UInt32),
        ('message', Byte * 28),
    ]
    return TPM_WNF_PROVISIONING
__all__ = [
    "GetDeviceID",
    "GetDeviceIDString",
    "TBS_COMMAND_LOCALITY",
    "TBS_COMMAND_LOCALITY_FOUR",
    "TBS_COMMAND_LOCALITY_ONE",
    "TBS_COMMAND_LOCALITY_THREE",
    "TBS_COMMAND_LOCALITY_TWO",
    "TBS_COMMAND_LOCALITY_ZERO",
    "TBS_COMMAND_PRIORITY",
    "TBS_COMMAND_PRIORITY_HIGH",
    "TBS_COMMAND_PRIORITY_LOW",
    "TBS_COMMAND_PRIORITY_MAX",
    "TBS_COMMAND_PRIORITY_NORMAL",
    "TBS_COMMAND_PRIORITY_SYSTEM",
    "TBS_CONTEXT_PARAMS",
    "TBS_CONTEXT_PARAMS2",
    "TBS_CONTEXT_VERSION_ONE",
    "TBS_CONTEXT_VERSION_TWO",
    "TBS_OWNERAUTH_TYPE_ADMIN",
    "TBS_OWNERAUTH_TYPE_ENDORSEMENT",
    "TBS_OWNERAUTH_TYPE_ENDORSEMENT_20",
    "TBS_OWNERAUTH_TYPE_FULL",
    "TBS_OWNERAUTH_TYPE_STORAGE_20",
    "TBS_OWNERAUTH_TYPE_USER",
    "TBS_SUCCESS",
    "TBS_TCGLOG_DRTM_BOOT",
    "TBS_TCGLOG_DRTM_CURRENT",
    "TBS_TCGLOG_DRTM_RESUME",
    "TBS_TCGLOG_SRTM_BOOT",
    "TBS_TCGLOG_SRTM_CURRENT",
    "TBS_TCGLOG_SRTM_RESUME",
    "TPM_DEVICE_INFO",
    "TPM_IFTYPE_1",
    "TPM_IFTYPE_EMULATOR",
    "TPM_IFTYPE_HW",
    "TPM_IFTYPE_SPB",
    "TPM_IFTYPE_TRUSTZONE",
    "TPM_IFTYPE_UNKNOWN",
    "TPM_VERSION_12",
    "TPM_VERSION_20",
    "TPM_VERSION_UNKNOWN",
    "TPM_WNF_INFO_CLEAR_SUCCESSFUL",
    "TPM_WNF_INFO_NO_REBOOT_REQUIRED",
    "TPM_WNF_INFO_OWNERSHIP_SUCCESSFUL",
    "TPM_WNF_PROVISIONING",
    "Tbsi_Context_Create",
    "Tbsi_Create_Windows_Key",
    "Tbsi_GetDeviceInfo",
    "Tbsi_Get_OwnerAuth",
    "Tbsi_Get_TCG_Log",
    "Tbsi_Get_TCG_Log_Ex",
    "Tbsi_Physical_Presence_Command",
    "Tbsi_Revoke_Attestation",
    "Tbsip_Cancel_Commands",
    "Tbsip_Context_Close",
    "Tbsip_Submit_Command",
]
