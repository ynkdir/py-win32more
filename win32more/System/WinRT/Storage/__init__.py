from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Com
import win32more.System.WinRT.Storage
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
HANDLE_ACCESS_OPTIONS = UInt32
HAO_NONE = 0
HAO_READ_ATTRIBUTES = 128
HAO_READ = 1179785
HAO_WRITE = 1179926
HAO_DELETE = 65536
HANDLE_CREATION_OPTIONS = Int32
HCO_CREATE_NEW = 1
HCO_CREATE_ALWAYS = 2
HCO_OPEN_EXISTING = 3
HCO_OPEN_ALWAYS = 4
HCO_TRUNCATE_EXISTING = 5
HANDLE_OPTIONS = UInt32
HO_NONE = 0
HO_OPEN_REQUIRING_OPLOCK = 262144
HO_DELETE_ON_CLOSE = 67108864
HO_SEQUENTIAL_SCAN = 134217728
HO_RANDOM_ACCESS = 268435456
HO_NO_BUFFERING = 536870912
HO_OVERLAPPED = 1073741824
HO_WRITE_THROUGH = 2147483648
HANDLE_SHARING_OPTIONS = UInt32
HSO_SHARE_NONE = 0
HSO_SHARE_READ = 1
HSO_SHARE_WRITE = 2
HSO_SHARE_DELETE = 4
def _define_IOplockBreakingHandler_head():
    class IOplockBreakingHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('826abe3d-3acd-47d3-84-f2-88-aa-ed-cf-63-04')
    return IOplockBreakingHandler
def _define_IOplockBreakingHandler():
    IOplockBreakingHandler = win32more.System.WinRT.Storage.IOplockBreakingHandler_head
    IOplockBreakingHandler.OplockBreaking = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'OplockBreaking', ()))
    win32more.System.Com.IUnknown
    return IOplockBreakingHandler
def _define_IRandomAccessStreamFileAccessMode_head():
    class IRandomAccessStreamFileAccessMode(win32more.System.Com.IUnknown_head):
        Guid = Guid('332e5848-2e15-458e-85-c4-c9-11-c0-c3-d6-f4')
    return IRandomAccessStreamFileAccessMode
def _define_IRandomAccessStreamFileAccessMode():
    IRandomAccessStreamFileAccessMode = win32more.System.WinRT.Storage.IRandomAccessStreamFileAccessMode_head
    IRandomAccessStreamFileAccessMode.GetMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetMode', ((1, 'fileAccessMode'),)))
    win32more.System.Com.IUnknown
    return IRandomAccessStreamFileAccessMode
def _define_IStorageFolderHandleAccess_head():
    class IStorageFolderHandleAccess(win32more.System.Com.IUnknown_head):
        Guid = Guid('df19938f-5462-48a0-be-65-d2-a3-27-1a-08-d6')
    return IStorageFolderHandleAccess
def _define_IStorageFolderHandleAccess():
    IStorageFolderHandleAccess = win32more.System.WinRT.Storage.IStorageFolderHandleAccess_head
    IStorageFolderHandleAccess.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.WinRT.Storage.HANDLE_CREATION_OPTIONS,win32more.System.WinRT.Storage.HANDLE_ACCESS_OPTIONS,win32more.System.WinRT.Storage.HANDLE_SHARING_OPTIONS,win32more.System.WinRT.Storage.HANDLE_OPTIONS,win32more.System.WinRT.Storage.IOplockBreakingHandler_head,POINTER(win32more.Foundation.HANDLE))(3, 'Create', ((1, 'fileName'),(1, 'creationOptions'),(1, 'accessOptions'),(1, 'sharingOptions'),(1, 'options'),(1, 'oplockBreakingHandler'),(1, 'interopHandle'),)))
    win32more.System.Com.IUnknown
    return IStorageFolderHandleAccess
def _define_IStorageItemHandleAccess_head():
    class IStorageItemHandleAccess(win32more.System.Com.IUnknown_head):
        Guid = Guid('5ca296b2-2c25-4d22-b7-85-b8-85-c8-20-1e-6a')
    return IStorageItemHandleAccess
def _define_IStorageItemHandleAccess():
    IStorageItemHandleAccess = win32more.System.WinRT.Storage.IStorageItemHandleAccess_head
    IStorageItemHandleAccess.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.Storage.HANDLE_ACCESS_OPTIONS,win32more.System.WinRT.Storage.HANDLE_SHARING_OPTIONS,win32more.System.WinRT.Storage.HANDLE_OPTIONS,win32more.System.WinRT.Storage.IOplockBreakingHandler_head,POINTER(win32more.Foundation.HANDLE))(3, 'Create', ((1, 'accessOptions'),(1, 'sharingOptions'),(1, 'options'),(1, 'oplockBreakingHandler'),(1, 'interopHandle'),)))
    win32more.System.Com.IUnknown
    return IStorageItemHandleAccess
def _define_IUnbufferedFileHandleOplockCallback_head():
    class IUnbufferedFileHandleOplockCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('d1019a0e-6243-4329-84-97-2e-75-89-4d-77-10')
    return IUnbufferedFileHandleOplockCallback
def _define_IUnbufferedFileHandleOplockCallback():
    IUnbufferedFileHandleOplockCallback = win32more.System.WinRT.Storage.IUnbufferedFileHandleOplockCallback_head
    IUnbufferedFileHandleOplockCallback.OnBrokenCallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'OnBrokenCallback', ()))
    win32more.System.Com.IUnknown
    return IUnbufferedFileHandleOplockCallback
def _define_IUnbufferedFileHandleProvider_head():
    class IUnbufferedFileHandleProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('a65c9109-42ab-4b94-a7-b1-dd-2e-4e-68-51-5e')
    return IUnbufferedFileHandleProvider
def _define_IUnbufferedFileHandleProvider():
    IUnbufferedFileHandleProvider = win32more.System.WinRT.Storage.IUnbufferedFileHandleProvider_head
    IUnbufferedFileHandleProvider.OpenUnbufferedFileHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.Storage.IUnbufferedFileHandleOplockCallback_head,POINTER(UIntPtr))(3, 'OpenUnbufferedFileHandle', ((1, 'oplockBreakCallback'),(1, 'fileHandle'),)))
    IUnbufferedFileHandleProvider.CloseUnbufferedFileHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'CloseUnbufferedFileHandle', ()))
    win32more.System.Com.IUnknown
    return IUnbufferedFileHandleProvider
__all__ = [
    "HANDLE_ACCESS_OPTIONS",
    "HANDLE_CREATION_OPTIONS",
    "HANDLE_OPTIONS",
    "HANDLE_SHARING_OPTIONS",
    "HAO_DELETE",
    "HAO_NONE",
    "HAO_READ",
    "HAO_READ_ATTRIBUTES",
    "HAO_WRITE",
    "HCO_CREATE_ALWAYS",
    "HCO_CREATE_NEW",
    "HCO_OPEN_ALWAYS",
    "HCO_OPEN_EXISTING",
    "HCO_TRUNCATE_EXISTING",
    "HO_DELETE_ON_CLOSE",
    "HO_NONE",
    "HO_NO_BUFFERING",
    "HO_OPEN_REQUIRING_OPLOCK",
    "HO_OVERLAPPED",
    "HO_RANDOM_ACCESS",
    "HO_SEQUENTIAL_SCAN",
    "HO_WRITE_THROUGH",
    "HSO_SHARE_DELETE",
    "HSO_SHARE_NONE",
    "HSO_SHARE_READ",
    "HSO_SHARE_WRITE",
    "IOplockBreakingHandler",
    "IRandomAccessStreamFileAccessMode",
    "IStorageFolderHandleAccess",
    "IStorageItemHandleAccess",
    "IUnbufferedFileHandleOplockCallback",
    "IUnbufferedFileHandleProvider",
]
