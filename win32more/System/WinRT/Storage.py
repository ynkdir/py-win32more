from win32more import *
import win32more.Foundation
import win32more.System.Com
import win32more.System.WinRT.Storage

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define_IRandomAccessStreamFileAccessMode_head():
    class IRandomAccessStreamFileAccessMode(win32more.System.Com.IUnknown_head):
        Guid = Guid('332e5848-2e15-458e-85c4-c911c0c3d6f4')
    return IRandomAccessStreamFileAccessMode
def _define_IRandomAccessStreamFileAccessMode():
    IRandomAccessStreamFileAccessMode = win32more.System.WinRT.Storage.IRandomAccessStreamFileAccessMode_head
    IRandomAccessStreamFileAccessMode.GetMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetMode', ((1, 'fileAccessMode'),)))
    return IRandomAccessStreamFileAccessMode
def _define_IUnbufferedFileHandleOplockCallback_head():
    class IUnbufferedFileHandleOplockCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('d1019a0e-6243-4329-8497-2e75894d7710')
    return IUnbufferedFileHandleOplockCallback
def _define_IUnbufferedFileHandleOplockCallback():
    IUnbufferedFileHandleOplockCallback = win32more.System.WinRT.Storage.IUnbufferedFileHandleOplockCallback_head
    IUnbufferedFileHandleOplockCallback.OnBrokenCallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'OnBrokenCallback', ()))
    return IUnbufferedFileHandleOplockCallback
def _define_IUnbufferedFileHandleProvider_head():
    class IUnbufferedFileHandleProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('a65c9109-42ab-4b94-a7b1-dd2e4e68515e')
    return IUnbufferedFileHandleProvider
def _define_IUnbufferedFileHandleProvider():
    IUnbufferedFileHandleProvider = win32more.System.WinRT.Storage.IUnbufferedFileHandleProvider_head
    IUnbufferedFileHandleProvider.OpenUnbufferedFileHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.Storage.IUnbufferedFileHandleOplockCallback_head,POINTER(UIntPtr), use_last_error=False)(3, 'OpenUnbufferedFileHandle', ((1, 'oplockBreakCallback'),(1, 'fileHandle'),)))
    IUnbufferedFileHandleProvider.CloseUnbufferedFileHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'CloseUnbufferedFileHandle', ()))
    return IUnbufferedFileHandleProvider
HANDLE_OPTIONS = UInt32
HO_NONE = 0
HO_OPEN_REQUIRING_OPLOCK = 262144
HO_DELETE_ON_CLOSE = 67108864
HO_SEQUENTIAL_SCAN = 134217728
HO_RANDOM_ACCESS = 268435456
HO_NO_BUFFERING = 536870912
HO_OVERLAPPED = 1073741824
HO_WRITE_THROUGH = 2147483648
HANDLE_ACCESS_OPTIONS = UInt32
HAO_NONE = 0
HAO_READ_ATTRIBUTES = 128
HAO_READ = 1179785
HAO_WRITE = 1179926
HAO_DELETE = 65536
HANDLE_SHARING_OPTIONS = UInt32
HSO_SHARE_NONE = 0
HSO_SHARE_READ = 1
HSO_SHARE_WRITE = 2
HSO_SHARE_DELETE = 4
HANDLE_CREATION_OPTIONS = Int32
HCO_CREATE_NEW = 1
HCO_CREATE_ALWAYS = 2
HCO_OPEN_EXISTING = 3
HCO_OPEN_ALWAYS = 4
HCO_TRUNCATE_EXISTING = 5
def _define_IOplockBreakingHandler_head():
    class IOplockBreakingHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('826abe3d-3acd-47d3-84f2-88aaedcf6304')
    return IOplockBreakingHandler
def _define_IOplockBreakingHandler():
    IOplockBreakingHandler = win32more.System.WinRT.Storage.IOplockBreakingHandler_head
    IOplockBreakingHandler.OplockBreaking = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'OplockBreaking', ()))
    return IOplockBreakingHandler
def _define_IStorageItemHandleAccess_head():
    class IStorageItemHandleAccess(win32more.System.Com.IUnknown_head):
        Guid = Guid('5ca296b2-2c25-4d22-b785-b885c8201e6a')
    return IStorageItemHandleAccess
def _define_IStorageItemHandleAccess():
    IStorageItemHandleAccess = win32more.System.WinRT.Storage.IStorageItemHandleAccess_head
    IStorageItemHandleAccess.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.Storage.HANDLE_ACCESS_OPTIONS,win32more.System.WinRT.Storage.HANDLE_SHARING_OPTIONS,win32more.System.WinRT.Storage.HANDLE_OPTIONS,win32more.System.WinRT.Storage.IOplockBreakingHandler_head,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(3, 'Create', ((1, 'accessOptions'),(1, 'sharingOptions'),(1, 'options'),(1, 'oplockBreakingHandler'),(1, 'interopHandle'),)))
    return IStorageItemHandleAccess
def _define_IStorageFolderHandleAccess_head():
    class IStorageFolderHandleAccess(win32more.System.Com.IUnknown_head):
        Guid = Guid('df19938f-5462-48a0-be65-d2a3271a08d6')
    return IStorageFolderHandleAccess
def _define_IStorageFolderHandleAccess():
    IStorageFolderHandleAccess = win32more.System.WinRT.Storage.IStorageFolderHandleAccess_head
    IStorageFolderHandleAccess.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.WinRT.Storage.HANDLE_CREATION_OPTIONS,win32more.System.WinRT.Storage.HANDLE_ACCESS_OPTIONS,win32more.System.WinRT.Storage.HANDLE_SHARING_OPTIONS,win32more.System.WinRT.Storage.HANDLE_OPTIONS,win32more.System.WinRT.Storage.IOplockBreakingHandler_head,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(3, 'Create', ((1, 'fileName'),(1, 'creationOptions'),(1, 'accessOptions'),(1, 'sharingOptions'),(1, 'options'),(1, 'oplockBreakingHandler'),(1, 'interopHandle'),)))
    return IStorageFolderHandleAccess
__all__ = [
    "IRandomAccessStreamFileAccessMode",
    "IUnbufferedFileHandleOplockCallback",
    "IUnbufferedFileHandleProvider",
    "HANDLE_OPTIONS",
    "HO_NONE",
    "HO_OPEN_REQUIRING_OPLOCK",
    "HO_DELETE_ON_CLOSE",
    "HO_SEQUENTIAL_SCAN",
    "HO_RANDOM_ACCESS",
    "HO_NO_BUFFERING",
    "HO_OVERLAPPED",
    "HO_WRITE_THROUGH",
    "HANDLE_ACCESS_OPTIONS",
    "HAO_NONE",
    "HAO_READ_ATTRIBUTES",
    "HAO_READ",
    "HAO_WRITE",
    "HAO_DELETE",
    "HANDLE_SHARING_OPTIONS",
    "HSO_SHARE_NONE",
    "HSO_SHARE_READ",
    "HSO_SHARE_WRITE",
    "HSO_SHARE_DELETE",
    "HANDLE_CREATION_OPTIONS",
    "HCO_CREATE_NEW",
    "HCO_CREATE_ALWAYS",
    "HCO_OPEN_EXISTING",
    "HCO_OPEN_ALWAYS",
    "HCO_TRUNCATE_EXISTING",
    "IOplockBreakingHandler",
    "IStorageItemHandleAccess",
    "IStorageFolderHandleAccess",
]
