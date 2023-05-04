from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.WinRT.Storage
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
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{826abe3d-3acd-47d3-84f2-88aaedcf6304}')
    @commethod(3)
    def OplockBreaking(self) -> Windows.Win32.Foundation.HRESULT: ...
class IRandomAccessStreamFileAccessMode(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{332e5848-2e15-458e-85c4-c911c0c3d6f4}')
    @commethod(3)
    def GetMode(self, fileAccessMode: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IStorageFolderHandleAccess(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{df19938f-5462-48a0-be65-d2a3271a08d6}')
    @commethod(3)
    def Create(self, fileName: Windows.Win32.Foundation.PWSTR, creationOptions: Windows.Win32.System.WinRT.Storage.HANDLE_CREATION_OPTIONS, accessOptions: Windows.Win32.System.WinRT.Storage.HANDLE_ACCESS_OPTIONS, sharingOptions: Windows.Win32.System.WinRT.Storage.HANDLE_SHARING_OPTIONS, options: Windows.Win32.System.WinRT.Storage.HANDLE_OPTIONS, oplockBreakingHandler: Windows.Win32.System.WinRT.Storage.IOplockBreakingHandler_head, interopHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
class IStorageItemHandleAccess(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5ca296b2-2c25-4d22-b785-b885c8201e6a}')
    @commethod(3)
    def Create(self, accessOptions: Windows.Win32.System.WinRT.Storage.HANDLE_ACCESS_OPTIONS, sharingOptions: Windows.Win32.System.WinRT.Storage.HANDLE_SHARING_OPTIONS, options: Windows.Win32.System.WinRT.Storage.HANDLE_OPTIONS, oplockBreakingHandler: Windows.Win32.System.WinRT.Storage.IOplockBreakingHandler_head, interopHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
class IUnbufferedFileHandleOplockCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d1019a0e-6243-4329-8497-2e75894d7710}')
    @commethod(3)
    def OnBrokenCallback(self) -> Windows.Win32.Foundation.HRESULT: ...
class IUnbufferedFileHandleProvider(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a65c9109-42ab-4b94-a7b1-dd2e4e68515e}')
    @commethod(3)
    def OpenUnbufferedFileHandle(self, oplockBreakCallback: Windows.Win32.System.WinRT.Storage.IUnbufferedFileHandleOplockCallback_head, fileHandle: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CloseUnbufferedFileHandle(self) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IOplockBreakingHandler')
make_head(_module, 'IRandomAccessStreamFileAccessMode')
make_head(_module, 'IStorageFolderHandleAccess')
make_head(_module, 'IStorageItemHandleAccess')
make_head(_module, 'IUnbufferedFileHandleOplockCallback')
make_head(_module, 'IUnbufferedFileHandleProvider')
