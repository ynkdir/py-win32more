from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.ServerBackup
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
WSB_MAX_OB_STATUS_VALUE_TYPE_PAIR: UInt32 = 5
WSB_MAX_OB_STATUS_ENTRY: UInt32 = 5
WSBAPP_ASYNC_IN_PROGRESS: Windows.Win32.Foundation.HRESULT = 7995396
class IWsbApplicationAsync(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0843f6f7-895c-44a6-b0-c2-05-a5-02-2a-a3-a1')
    @commethod(3)
    def QueryStatus(phrResult: POINTER(Windows.Win32.Foundation.HRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Abort() -> Windows.Win32.Foundation.HRESULT: ...
class IWsbApplicationBackupSupport(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1eff3510-4a27-46ad-b9-e0-08-33-2f-0f-4f-6d')
    @commethod(3)
    def CheckConsistency(wszWriterMetadata: Windows.Win32.Foundation.PWSTR, wszComponentName: Windows.Win32.Foundation.PWSTR, wszComponentLogicalPath: Windows.Win32.Foundation.PWSTR, cVolumes: UInt32, rgwszSourceVolumePath: POINTER(Windows.Win32.Foundation.PWSTR), rgwszSnapshotVolumePath: POINTER(Windows.Win32.Foundation.PWSTR), ppAsync: POINTER(Windows.Win32.System.ServerBackup.IWsbApplicationAsync_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWsbApplicationRestoreSupport(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8d3bdb38-4ee8-4718-85-f9-c7-db-c4-ab-77-aa')
    @commethod(3)
    def PreRestore(wszWriterMetadata: Windows.Win32.Foundation.PWSTR, wszComponentName: Windows.Win32.Foundation.PWSTR, wszComponentLogicalPath: Windows.Win32.Foundation.PWSTR, bNoRollForward: Windows.Win32.Foundation.BOOLEAN) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PostRestore(wszWriterMetadata: Windows.Win32.Foundation.PWSTR, wszComponentName: Windows.Win32.Foundation.PWSTR, wszComponentLogicalPath: Windows.Win32.Foundation.PWSTR, bNoRollForward: Windows.Win32.Foundation.BOOLEAN) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OrderComponents(cComponents: UInt32, rgComponentName: POINTER(Windows.Win32.Foundation.PWSTR), rgComponentLogicalPaths: POINTER(Windows.Win32.Foundation.PWSTR), prgComponentName: POINTER(POINTER(Windows.Win32.Foundation.PWSTR)), prgComponentLogicalPath: POINTER(POINTER(Windows.Win32.Foundation.PWSTR))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsRollForwardSupported(pbRollForwardSupported: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
class WSB_OB_REGISTRATION_INFO(Structure):
    m_wszResourceDLL: Windows.Win32.Foundation.PWSTR
    m_guidSnapinId: Guid
    m_dwProviderName: UInt32
    m_dwProviderIcon: UInt32
    m_bSupportsRemoting: Windows.Win32.Foundation.BOOLEAN
class WSB_OB_STATUS_ENTRY(Structure):
    m_dwIcon: UInt32
    m_dwStatusEntryName: UInt32
    m_dwStatusEntryValue: UInt32
    m_cValueTypePair: UInt32
    m_rgValueTypePair: POINTER(Windows.Win32.System.ServerBackup.WSB_OB_STATUS_ENTRY_VALUE_TYPE_PAIR_head)
WSB_OB_STATUS_ENTRY_PAIR_TYPE = Int32
WSB_OB_ET_UNDEFINED: WSB_OB_STATUS_ENTRY_PAIR_TYPE = 0
WSB_OB_ET_STRING: WSB_OB_STATUS_ENTRY_PAIR_TYPE = 1
WSB_OB_ET_NUMBER: WSB_OB_STATUS_ENTRY_PAIR_TYPE = 2
WSB_OB_ET_DATETIME: WSB_OB_STATUS_ENTRY_PAIR_TYPE = 3
WSB_OB_ET_TIME: WSB_OB_STATUS_ENTRY_PAIR_TYPE = 4
WSB_OB_ET_SIZE: WSB_OB_STATUS_ENTRY_PAIR_TYPE = 5
WSB_OB_ET_MAX: WSB_OB_STATUS_ENTRY_PAIR_TYPE = 6
class WSB_OB_STATUS_ENTRY_VALUE_TYPE_PAIR(Structure):
    m_wszObStatusEntryPairValue: Windows.Win32.Foundation.PWSTR
    m_ObStatusEntryPairType: Windows.Win32.System.ServerBackup.WSB_OB_STATUS_ENTRY_PAIR_TYPE
class WSB_OB_STATUS_INFO(Structure):
    m_guidSnapinId: Guid
    m_cStatusEntry: UInt32
    m_rgStatusEntry: POINTER(Windows.Win32.System.ServerBackup.WSB_OB_STATUS_ENTRY_head)
make_head(_module, 'IWsbApplicationAsync')
make_head(_module, 'IWsbApplicationBackupSupport')
make_head(_module, 'IWsbApplicationRestoreSupport')
make_head(_module, 'WSB_OB_REGISTRATION_INFO')
make_head(_module, 'WSB_OB_STATUS_ENTRY')
make_head(_module, 'WSB_OB_STATUS_ENTRY_VALUE_TYPE_PAIR')
make_head(_module, 'WSB_OB_STATUS_INFO')
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
_arch_optional = [
]
