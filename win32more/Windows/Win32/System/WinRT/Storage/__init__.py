from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT.Storage
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
HANDLE_ACCESS_OPTIONS = Int32
HAO_NONE: HANDLE_ACCESS_OPTIONS = 0
HAO_READ_ATTRIBUTES: HANDLE_ACCESS_OPTIONS = 128
HAO_READ: HANDLE_ACCESS_OPTIONS = 1179785
HAO_WRITE: HANDLE_ACCESS_OPTIONS = 1179926
HAO_DELETE: HANDLE_ACCESS_OPTIONS = 65536
HANDLE_CREATION_OPTIONS = Int32
HCO_CREATE_NEW: HANDLE_CREATION_OPTIONS = 1
HCO_CREATE_ALWAYS: HANDLE_CREATION_OPTIONS = 2
HCO_OPEN_EXISTING: HANDLE_CREATION_OPTIONS = 3
HCO_OPEN_ALWAYS: HANDLE_CREATION_OPTIONS = 4
HCO_TRUNCATE_EXISTING: HANDLE_CREATION_OPTIONS = 5
HANDLE_OPTIONS = UInt32
HO_NONE: HANDLE_OPTIONS = 0
HO_OPEN_REQUIRING_OPLOCK: HANDLE_OPTIONS = 262144
HO_DELETE_ON_CLOSE: HANDLE_OPTIONS = 67108864
HO_SEQUENTIAL_SCAN: HANDLE_OPTIONS = 134217728
HO_RANDOM_ACCESS: HANDLE_OPTIONS = 268435456
HO_NO_BUFFERING: HANDLE_OPTIONS = 536870912
HO_OVERLAPPED: HANDLE_OPTIONS = 1073741824
HO_WRITE_THROUGH: HANDLE_OPTIONS = 2147483648
HANDLE_SHARING_OPTIONS = Int32
HSO_SHARE_NONE: HANDLE_SHARING_OPTIONS = 0
HSO_SHARE_READ: HANDLE_SHARING_OPTIONS = 1
HSO_SHARE_WRITE: HANDLE_SHARING_OPTIONS = 2
HSO_SHARE_DELETE: HANDLE_SHARING_OPTIONS = 4
class IOplockBreakingHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{826abe3d-3acd-47d3-84f2-88aaedcf6304}')
    @commethod(3)
    def OplockBreaking(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRandomAccessStreamFileAccessMode(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{332e5848-2e15-458e-85c4-c911c0c3d6f4}')
    @commethod(3)
    def GetMode(self, fileAccessMode: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IStorageFolderHandleAccess(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{df19938f-5462-48a0-be65-d2a3271a08d6}')
    @commethod(3)
    def Create(self, fileName: win32more.Windows.Win32.Foundation.PWSTR, creationOptions: win32more.Windows.Win32.System.WinRT.Storage.HANDLE_CREATION_OPTIONS, accessOptions: win32more.Windows.Win32.System.WinRT.Storage.HANDLE_ACCESS_OPTIONS, sharingOptions: win32more.Windows.Win32.System.WinRT.Storage.HANDLE_SHARING_OPTIONS, options: win32more.Windows.Win32.System.WinRT.Storage.HANDLE_OPTIONS, oplockBreakingHandler: win32more.Windows.Win32.System.WinRT.Storage.IOplockBreakingHandler_head, interopHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IStorageItemHandleAccess(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5ca296b2-2c25-4d22-b785-b885c8201e6a}')
    @commethod(3)
    def Create(self, accessOptions: win32more.Windows.Win32.System.WinRT.Storage.HANDLE_ACCESS_OPTIONS, sharingOptions: win32more.Windows.Win32.System.WinRT.Storage.HANDLE_SHARING_OPTIONS, options: win32more.Windows.Win32.System.WinRT.Storage.HANDLE_OPTIONS, oplockBreakingHandler: win32more.Windows.Win32.System.WinRT.Storage.IOplockBreakingHandler_head, interopHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUnbufferedFileHandleOplockCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d1019a0e-6243-4329-8497-2e75894d7710}')
    @commethod(3)
    def OnBrokenCallback(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUnbufferedFileHandleProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a65c9109-42ab-4b94-a7b1-dd2e4e68515e}')
    @commethod(3)
    def OpenUnbufferedFileHandle(self, oplockBreakCallback: win32more.Windows.Win32.System.WinRT.Storage.IUnbufferedFileHandleOplockCallback_head, fileHandle: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CloseUnbufferedFileHandle(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IOplockBreakingHandler')
make_head(_module, 'IRandomAccessStreamFileAccessMode')
make_head(_module, 'IStorageFolderHandleAccess')
make_head(_module, 'IStorageItemHandleAccess')
make_head(_module, 'IUnbufferedFileHandleOplockCallback')
make_head(_module, 'IUnbufferedFileHandleProvider')
