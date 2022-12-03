from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Com
import win32more.System.ServerBackup
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
WSB_MAX_OB_STATUS_VALUE_TYPE_PAIR = 5
WSB_MAX_OB_STATUS_ENTRY = 5
WSBAPP_ASYNC_IN_PROGRESS = 7995396
def _define_IWsbApplicationAsync_head():
    class IWsbApplicationAsync(win32more.System.Com.IUnknown_head):
        Guid = Guid('0843f6f7-895c-44a6-b0-c2-05-a5-02-2a-a3-a1')
    return IWsbApplicationAsync
def _define_IWsbApplicationAsync():
    IWsbApplicationAsync = win32more.System.ServerBackup.IWsbApplicationAsync_head
    IWsbApplicationAsync.QueryStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HRESULT))(3, 'QueryStatus', ((1, 'phrResult'),)))
    IWsbApplicationAsync.Abort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Abort', ()))
    win32more.System.Com.IUnknown
    return IWsbApplicationAsync
def _define_IWsbApplicationBackupSupport_head():
    class IWsbApplicationBackupSupport(win32more.System.Com.IUnknown_head):
        Guid = Guid('1eff3510-4a27-46ad-b9-e0-08-33-2f-0f-4f-6d')
    return IWsbApplicationBackupSupport
def _define_IWsbApplicationBackupSupport():
    IWsbApplicationBackupSupport = win32more.System.ServerBackup.IWsbApplicationBackupSupport_head
    IWsbApplicationBackupSupport.CheckConsistency = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR),POINTER(win32more.System.ServerBackup.IWsbApplicationAsync_head))(3, 'CheckConsistency', ((1, 'wszWriterMetadata'),(1, 'wszComponentName'),(1, 'wszComponentLogicalPath'),(1, 'cVolumes'),(1, 'rgwszSourceVolumePath'),(1, 'rgwszSnapshotVolumePath'),(1, 'ppAsync'),)))
    win32more.System.Com.IUnknown
    return IWsbApplicationBackupSupport
def _define_IWsbApplicationRestoreSupport_head():
    class IWsbApplicationRestoreSupport(win32more.System.Com.IUnknown_head):
        Guid = Guid('8d3bdb38-4ee8-4718-85-f9-c7-db-c4-ab-77-aa')
    return IWsbApplicationRestoreSupport
def _define_IWsbApplicationRestoreSupport():
    IWsbApplicationRestoreSupport = win32more.System.ServerBackup.IWsbApplicationRestoreSupport_head
    IWsbApplicationRestoreSupport.PreRestore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOLEAN)(3, 'PreRestore', ((1, 'wszWriterMetadata'),(1, 'wszComponentName'),(1, 'wszComponentLogicalPath'),(1, 'bNoRollForward'),)))
    IWsbApplicationRestoreSupport.PostRestore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOLEAN)(4, 'PostRestore', ((1, 'wszWriterMetadata'),(1, 'wszComponentName'),(1, 'wszComponentLogicalPath'),(1, 'bNoRollForward'),)))
    IWsbApplicationRestoreSupport.OrderComponents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR),POINTER(POINTER(win32more.Foundation.PWSTR)),POINTER(POINTER(win32more.Foundation.PWSTR)))(5, 'OrderComponents', ((1, 'cComponents'),(1, 'rgComponentName'),(1, 'rgComponentLogicalPaths'),(1, 'prgComponentName'),(1, 'prgComponentLogicalPath'),)))
    IWsbApplicationRestoreSupport.IsRollForwardSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no)(6, 'IsRollForwardSupported', ((1, 'pbRollForwardSupported'),)))
    win32more.System.Com.IUnknown
    return IWsbApplicationRestoreSupport
def _define_WSB_OB_REGISTRATION_INFO_head():
    class WSB_OB_REGISTRATION_INFO(Structure):
        pass
    return WSB_OB_REGISTRATION_INFO
def _define_WSB_OB_REGISTRATION_INFO():
    WSB_OB_REGISTRATION_INFO = win32more.System.ServerBackup.WSB_OB_REGISTRATION_INFO_head
    WSB_OB_REGISTRATION_INFO._fields_ = [
        ('m_wszResourceDLL', win32more.Foundation.PWSTR),
        ('m_guidSnapinId', Guid),
        ('m_dwProviderName', UInt32),
        ('m_dwProviderIcon', UInt32),
        ('m_bSupportsRemoting', win32more.Foundation.BOOLEAN),
    ]
    return WSB_OB_REGISTRATION_INFO
def _define_WSB_OB_STATUS_ENTRY_head():
    class WSB_OB_STATUS_ENTRY(Structure):
        pass
    return WSB_OB_STATUS_ENTRY
def _define_WSB_OB_STATUS_ENTRY():
    WSB_OB_STATUS_ENTRY = win32more.System.ServerBackup.WSB_OB_STATUS_ENTRY_head
    WSB_OB_STATUS_ENTRY._fields_ = [
        ('m_dwIcon', UInt32),
        ('m_dwStatusEntryName', UInt32),
        ('m_dwStatusEntryValue', UInt32),
        ('m_cValueTypePair', UInt32),
        ('m_rgValueTypePair', POINTER(win32more.System.ServerBackup.WSB_OB_STATUS_ENTRY_VALUE_TYPE_PAIR_head)),
    ]
    return WSB_OB_STATUS_ENTRY
WSB_OB_STATUS_ENTRY_PAIR_TYPE = Int32
WSB_OB_ET_UNDEFINED = 0
WSB_OB_ET_STRING = 1
WSB_OB_ET_NUMBER = 2
WSB_OB_ET_DATETIME = 3
WSB_OB_ET_TIME = 4
WSB_OB_ET_SIZE = 5
WSB_OB_ET_MAX = 6
def _define_WSB_OB_STATUS_ENTRY_VALUE_TYPE_PAIR_head():
    class WSB_OB_STATUS_ENTRY_VALUE_TYPE_PAIR(Structure):
        pass
    return WSB_OB_STATUS_ENTRY_VALUE_TYPE_PAIR
def _define_WSB_OB_STATUS_ENTRY_VALUE_TYPE_PAIR():
    WSB_OB_STATUS_ENTRY_VALUE_TYPE_PAIR = win32more.System.ServerBackup.WSB_OB_STATUS_ENTRY_VALUE_TYPE_PAIR_head
    WSB_OB_STATUS_ENTRY_VALUE_TYPE_PAIR._fields_ = [
        ('m_wszObStatusEntryPairValue', win32more.Foundation.PWSTR),
        ('m_ObStatusEntryPairType', win32more.System.ServerBackup.WSB_OB_STATUS_ENTRY_PAIR_TYPE),
    ]
    return WSB_OB_STATUS_ENTRY_VALUE_TYPE_PAIR
def _define_WSB_OB_STATUS_INFO_head():
    class WSB_OB_STATUS_INFO(Structure):
        pass
    return WSB_OB_STATUS_INFO
def _define_WSB_OB_STATUS_INFO():
    WSB_OB_STATUS_INFO = win32more.System.ServerBackup.WSB_OB_STATUS_INFO_head
    WSB_OB_STATUS_INFO._fields_ = [
        ('m_guidSnapinId', Guid),
        ('m_cStatusEntry', UInt32),
        ('m_rgStatusEntry', POINTER(win32more.System.ServerBackup.WSB_OB_STATUS_ENTRY_head)),
    ]
    return WSB_OB_STATUS_INFO
__all__ = [
    "IWsbApplicationAsync",
    "IWsbApplicationBackupSupport",
    "IWsbApplicationRestoreSupport",
    "WSBAPP_ASYNC_IN_PROGRESS",
    "WSB_MAX_OB_STATUS_ENTRY",
    "WSB_MAX_OB_STATUS_VALUE_TYPE_PAIR",
    "WSB_OB_ET_DATETIME",
    "WSB_OB_ET_MAX",
    "WSB_OB_ET_NUMBER",
    "WSB_OB_ET_SIZE",
    "WSB_OB_ET_STRING",
    "WSB_OB_ET_TIME",
    "WSB_OB_ET_UNDEFINED",
    "WSB_OB_REGISTRATION_INFO",
    "WSB_OB_STATUS_ENTRY",
    "WSB_OB_STATUS_ENTRY_PAIR_TYPE",
    "WSB_OB_STATUS_ENTRY_VALUE_TYPE_PAIR",
    "WSB_OB_STATUS_INFO",
]
