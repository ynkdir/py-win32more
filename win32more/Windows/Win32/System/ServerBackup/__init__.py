from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.ServerBackup
WSB_MAX_OB_STATUS_VALUE_TYPE_PAIR: UInt32 = 5
WSB_MAX_OB_STATUS_ENTRY: UInt32 = 5
WSBAPP_ASYNC_IN_PROGRESS: win32more.Windows.Win32.Foundation.HRESULT = 7995396
class IWsbApplicationAsync(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0843f6f7-895c-44a6-b0c2-05a5022aa3a1}')
    @commethod(3)
    def QueryStatus(self, phrResult: POINTER(win32more.Windows.Win32.Foundation.HRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Abort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWsbApplicationBackupSupport(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1eff3510-4a27-46ad-b9e0-08332f0f4f6d}')
    @commethod(3)
    def CheckConsistency(self, wszWriterMetadata: win32more.Windows.Win32.Foundation.PWSTR, wszComponentName: win32more.Windows.Win32.Foundation.PWSTR, wszComponentLogicalPath: win32more.Windows.Win32.Foundation.PWSTR, cVolumes: UInt32, rgwszSourceVolumePath: POINTER(win32more.Windows.Win32.Foundation.PWSTR), rgwszSnapshotVolumePath: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ppAsync: POINTER(win32more.Windows.Win32.System.ServerBackup.IWsbApplicationAsync)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWsbApplicationRestoreSupport(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8d3bdb38-4ee8-4718-85f9-c7dbc4ab77aa}')
    @commethod(3)
    def PreRestore(self, wszWriterMetadata: win32more.Windows.Win32.Foundation.PWSTR, wszComponentName: win32more.Windows.Win32.Foundation.PWSTR, wszComponentLogicalPath: win32more.Windows.Win32.Foundation.PWSTR, bNoRollForward: win32more.Windows.Win32.Foundation.BOOLEAN) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PostRestore(self, wszWriterMetadata: win32more.Windows.Win32.Foundation.PWSTR, wszComponentName: win32more.Windows.Win32.Foundation.PWSTR, wszComponentLogicalPath: win32more.Windows.Win32.Foundation.PWSTR, bNoRollForward: win32more.Windows.Win32.Foundation.BOOLEAN) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OrderComponents(self, cComponents: UInt32, rgComponentName: POINTER(win32more.Windows.Win32.Foundation.PWSTR), rgComponentLogicalPaths: POINTER(win32more.Windows.Win32.Foundation.PWSTR), prgComponentName: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR)), prgComponentLogicalPath: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsRollForwardSupported(self, pbRollForwardSupported: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class WSB_OB_REGISTRATION_INFO(Structure):
    m_wszResourceDLL: win32more.Windows.Win32.Foundation.PWSTR
    m_guidSnapinId: Guid
    m_dwProviderName: UInt32
    m_dwProviderIcon: UInt32
    m_bSupportsRemoting: win32more.Windows.Win32.Foundation.BOOLEAN
class WSB_OB_STATUS_ENTRY(Structure):
    m_dwIcon: UInt32
    m_dwStatusEntryName: UInt32
    m_dwStatusEntryValue: UInt32
    m_cValueTypePair: UInt32
    m_rgValueTypePair: POINTER(win32more.Windows.Win32.System.ServerBackup.WSB_OB_STATUS_ENTRY_VALUE_TYPE_PAIR)
WSB_OB_STATUS_ENTRY_PAIR_TYPE = Int32
WSB_OB_ET_UNDEFINED: win32more.Windows.Win32.System.ServerBackup.WSB_OB_STATUS_ENTRY_PAIR_TYPE = 0
WSB_OB_ET_STRING: win32more.Windows.Win32.System.ServerBackup.WSB_OB_STATUS_ENTRY_PAIR_TYPE = 1
WSB_OB_ET_NUMBER: win32more.Windows.Win32.System.ServerBackup.WSB_OB_STATUS_ENTRY_PAIR_TYPE = 2
WSB_OB_ET_DATETIME: win32more.Windows.Win32.System.ServerBackup.WSB_OB_STATUS_ENTRY_PAIR_TYPE = 3
WSB_OB_ET_TIME: win32more.Windows.Win32.System.ServerBackup.WSB_OB_STATUS_ENTRY_PAIR_TYPE = 4
WSB_OB_ET_SIZE: win32more.Windows.Win32.System.ServerBackup.WSB_OB_STATUS_ENTRY_PAIR_TYPE = 5
WSB_OB_ET_MAX: win32more.Windows.Win32.System.ServerBackup.WSB_OB_STATUS_ENTRY_PAIR_TYPE = 6
class WSB_OB_STATUS_ENTRY_VALUE_TYPE_PAIR(Structure):
    m_wszObStatusEntryPairValue: win32more.Windows.Win32.Foundation.PWSTR
    m_ObStatusEntryPairType: win32more.Windows.Win32.System.ServerBackup.WSB_OB_STATUS_ENTRY_PAIR_TYPE
class WSB_OB_STATUS_INFO(Structure):
    m_guidSnapinId: Guid
    m_cStatusEntry: UInt32
    m_rgStatusEntry: POINTER(win32more.Windows.Win32.System.ServerBackup.WSB_OB_STATUS_ENTRY)


make_ready(__name__)
