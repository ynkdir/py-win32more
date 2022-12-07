from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.LibraryLoader
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
FIND_RESOURCE_DIRECTORY_TYPES: UInt32 = 256
FIND_RESOURCE_DIRECTORY_NAMES: UInt32 = 512
FIND_RESOURCE_DIRECTORY_LANGUAGES: UInt32 = 1024
RESOURCE_ENUM_LN: UInt32 = 1
RESOURCE_ENUM_MUI: UInt32 = 2
RESOURCE_ENUM_MUI_SYSTEM: UInt32 = 4
RESOURCE_ENUM_VALIDATE: UInt32 = 8
RESOURCE_ENUM_MODULE_EXACT: UInt32 = 16
SUPPORT_LANG_NUMBER: UInt32 = 32
GET_MODULE_HANDLE_EX_FLAG_PIN: UInt32 = 1
GET_MODULE_HANDLE_EX_FLAG_UNCHANGED_REFCOUNT: UInt32 = 2
GET_MODULE_HANDLE_EX_FLAG_FROM_ADDRESS: UInt32 = 4
CURRENT_IMPORT_REDIRECTION_VERSION: UInt32 = 1
LOAD_LIBRARY_OS_INTEGRITY_CONTINUITY: UInt32 = 32768
@winfunctype('KERNEL32.dll')
def DisableThreadLibraryCalls(hLibModule: win32more.Foundation.HINSTANCE) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindResourceExW(hModule: win32more.Foundation.HINSTANCE, lpType: win32more.Foundation.PWSTR, lpName: win32more.Foundation.PWSTR, wLanguage: UInt16) -> win32more.Foundation.HRSRC: ...
@winfunctype('KERNEL32.dll')
def FreeLibrary(hLibModule: win32more.Foundation.HINSTANCE) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FreeLibraryAndExitThread(hLibModule: win32more.Foundation.HINSTANCE, dwExitCode: UInt32) -> Void: ...
@winfunctype('KERNEL32.dll')
def FreeResource(hResData: IntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetModuleFileNameA(hModule: win32more.Foundation.HINSTANCE, lpFilename: win32more.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetModuleFileNameW(hModule: win32more.Foundation.HINSTANCE, lpFilename: win32more.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetModuleHandleA(lpModuleName: win32more.Foundation.PSTR) -> win32more.Foundation.HINSTANCE: ...
@winfunctype('KERNEL32.dll')
def GetModuleHandleW(lpModuleName: win32more.Foundation.PWSTR) -> win32more.Foundation.HINSTANCE: ...
@winfunctype('KERNEL32.dll')
def GetModuleHandleExA(dwFlags: UInt32, lpModuleName: win32more.Foundation.PSTR, phModule: POINTER(win32more.Foundation.HINSTANCE)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetModuleHandleExW(dwFlags: UInt32, lpModuleName: win32more.Foundation.PWSTR, phModule: POINTER(win32more.Foundation.HINSTANCE)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcAddress(hModule: win32more.Foundation.HINSTANCE, lpProcName: win32more.Foundation.PSTR) -> win32more.Foundation.FARPROC: ...
@winfunctype('KERNEL32.dll')
def LoadLibraryExA(lpLibFileName: win32more.Foundation.PSTR, hFile: win32more.Foundation.HANDLE, dwFlags: win32more.System.LibraryLoader.LOAD_LIBRARY_FLAGS) -> win32more.Foundation.HINSTANCE: ...
@winfunctype('KERNEL32.dll')
def LoadLibraryExW(lpLibFileName: win32more.Foundation.PWSTR, hFile: win32more.Foundation.HANDLE, dwFlags: win32more.System.LibraryLoader.LOAD_LIBRARY_FLAGS) -> win32more.Foundation.HINSTANCE: ...
@winfunctype('KERNEL32.dll')
def LoadResource(hModule: win32more.Foundation.HINSTANCE, hResInfo: win32more.Foundation.HRSRC) -> IntPtr: ...
@winfunctype('KERNEL32.dll')
def LockResource(hResData: IntPtr) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def SizeofResource(hModule: win32more.Foundation.HINSTANCE, hResInfo: win32more.Foundation.HRSRC) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def AddDllDirectory(NewDirectory: win32more.Foundation.PWSTR) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def RemoveDllDirectory(Cookie: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetDefaultDllDirectories(DirectoryFlags: win32more.System.LibraryLoader.LOAD_LIBRARY_FLAGS) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceLanguagesExA(hModule: win32more.Foundation.HINSTANCE, lpType: win32more.Foundation.PSTR, lpName: win32more.Foundation.PSTR, lpEnumFunc: win32more.System.LibraryLoader.ENUMRESLANGPROCA, lParam: IntPtr, dwFlags: UInt32, LangId: UInt16) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceLanguagesExW(hModule: win32more.Foundation.HINSTANCE, lpType: win32more.Foundation.PWSTR, lpName: win32more.Foundation.PWSTR, lpEnumFunc: win32more.System.LibraryLoader.ENUMRESLANGPROCW, lParam: IntPtr, dwFlags: UInt32, LangId: UInt16) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceNamesExA(hModule: win32more.Foundation.HINSTANCE, lpType: win32more.Foundation.PSTR, lpEnumFunc: win32more.System.LibraryLoader.ENUMRESNAMEPROCA, lParam: IntPtr, dwFlags: UInt32, LangId: UInt16) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceNamesExW(hModule: win32more.Foundation.HINSTANCE, lpType: win32more.Foundation.PWSTR, lpEnumFunc: win32more.System.LibraryLoader.ENUMRESNAMEPROCW, lParam: IntPtr, dwFlags: UInt32, LangId: UInt16) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceTypesExA(hModule: win32more.Foundation.HINSTANCE, lpEnumFunc: win32more.System.LibraryLoader.ENUMRESTYPEPROCA, lParam: IntPtr, dwFlags: UInt32, LangId: UInt16) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceTypesExW(hModule: win32more.Foundation.HINSTANCE, lpEnumFunc: win32more.System.LibraryLoader.ENUMRESTYPEPROCW, lParam: IntPtr, dwFlags: UInt32, LangId: UInt16) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindResourceW(hModule: win32more.Foundation.HINSTANCE, lpName: win32more.Foundation.PWSTR, lpType: win32more.Foundation.PWSTR) -> win32more.Foundation.HRSRC: ...
@winfunctype('KERNEL32.dll')
def LoadLibraryA(lpLibFileName: win32more.Foundation.PSTR) -> win32more.Foundation.HINSTANCE: ...
@winfunctype('KERNEL32.dll')
def LoadLibraryW(lpLibFileName: win32more.Foundation.PWSTR) -> win32more.Foundation.HINSTANCE: ...
@winfunctype('KERNEL32.dll')
def EnumResourceNamesW(hModule: win32more.Foundation.HINSTANCE, lpType: win32more.Foundation.PWSTR, lpEnumFunc: win32more.System.LibraryLoader.ENUMRESNAMEPROCW, lParam: IntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceNamesA(hModule: win32more.Foundation.HINSTANCE, lpType: win32more.Foundation.PSTR, lpEnumFunc: win32more.System.LibraryLoader.ENUMRESNAMEPROCA, lParam: IntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def LoadModule(lpModuleName: win32more.Foundation.PSTR, lpParameterBlock: c_void_p) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def LoadPackagedLibrary(lpwLibFileName: win32more.Foundation.PWSTR, Reserved: UInt32) -> win32more.Foundation.HINSTANCE: ...
@winfunctype('KERNEL32.dll')
def FindResourceA(hModule: win32more.Foundation.HINSTANCE, lpName: win32more.Foundation.PSTR, lpType: win32more.Foundation.PSTR) -> win32more.Foundation.HRSRC: ...
@winfunctype('KERNEL32.dll')
def FindResourceExA(hModule: win32more.Foundation.HINSTANCE, lpType: win32more.Foundation.PSTR, lpName: win32more.Foundation.PSTR, wLanguage: UInt16) -> win32more.Foundation.HRSRC: ...
@winfunctype('KERNEL32.dll')
def EnumResourceTypesA(hModule: win32more.Foundation.HINSTANCE, lpEnumFunc: win32more.System.LibraryLoader.ENUMRESTYPEPROCA, lParam: IntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceTypesW(hModule: win32more.Foundation.HINSTANCE, lpEnumFunc: win32more.System.LibraryLoader.ENUMRESTYPEPROCW, lParam: IntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceLanguagesA(hModule: win32more.Foundation.HINSTANCE, lpType: win32more.Foundation.PSTR, lpName: win32more.Foundation.PSTR, lpEnumFunc: win32more.System.LibraryLoader.ENUMRESLANGPROCA, lParam: IntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceLanguagesW(hModule: win32more.Foundation.HINSTANCE, lpType: win32more.Foundation.PWSTR, lpName: win32more.Foundation.PWSTR, lpEnumFunc: win32more.System.LibraryLoader.ENUMRESLANGPROCW, lParam: IntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def BeginUpdateResourceA(pFileName: win32more.Foundation.PSTR, bDeleteExistingResources: win32more.Foundation.BOOL) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def BeginUpdateResourceW(pFileName: win32more.Foundation.PWSTR, bDeleteExistingResources: win32more.Foundation.BOOL) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def UpdateResourceA(hUpdate: win32more.Foundation.HANDLE, lpType: win32more.Foundation.PSTR, lpName: win32more.Foundation.PSTR, wLanguage: UInt16, lpData: c_void_p, cb: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def UpdateResourceW(hUpdate: win32more.Foundation.HANDLE, lpType: win32more.Foundation.PWSTR, lpName: win32more.Foundation.PWSTR, wLanguage: UInt16, lpData: c_void_p, cb: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EndUpdateResourceA(hUpdate: win32more.Foundation.HANDLE, fDiscard: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EndUpdateResourceW(hUpdate: win32more.Foundation.HANDLE, fDiscard: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetDllDirectoryA(lpPathName: win32more.Foundation.PSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetDllDirectoryW(lpPathName: win32more.Foundation.PWSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetDllDirectoryA(nBufferLength: UInt32, lpBuffer: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetDllDirectoryW(nBufferLength: UInt32, lpBuffer: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype_pointer
def ENUMRESLANGPROCA(hModule: win32more.Foundation.HINSTANCE, lpType: win32more.Foundation.PSTR, lpName: win32more.Foundation.PSTR, wLanguage: UInt16, lParam: IntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def ENUMRESLANGPROCW(hModule: win32more.Foundation.HINSTANCE, lpType: win32more.Foundation.PWSTR, lpName: win32more.Foundation.PWSTR, wLanguage: UInt16, lParam: IntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def ENUMRESNAMEPROCA(hModule: win32more.Foundation.HINSTANCE, lpType: win32more.Foundation.PSTR, lpName: win32more.Foundation.PSTR, lParam: IntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def ENUMRESNAMEPROCW(hModule: win32more.Foundation.HINSTANCE, lpType: win32more.Foundation.PWSTR, lpName: win32more.Foundation.PWSTR, lParam: IntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def ENUMRESTYPEPROCA(hModule: win32more.Foundation.HINSTANCE, lpType: win32more.Foundation.PSTR, lParam: IntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def ENUMRESTYPEPROCW(hModule: win32more.Foundation.HINSTANCE, lpType: win32more.Foundation.PWSTR, lParam: IntPtr) -> win32more.Foundation.BOOL: ...
class ENUMUILANG(Structure):
    NumOfEnumUILang: UInt32
    SizeOfEnumUIBuffer: UInt32
    pEnumUIBuffer: POINTER(UInt16)
LOAD_LIBRARY_FLAGS = UInt32
DONT_RESOLVE_DLL_REFERENCES: LOAD_LIBRARY_FLAGS = 1
LOAD_LIBRARY_AS_DATAFILE: LOAD_LIBRARY_FLAGS = 2
LOAD_WITH_ALTERED_SEARCH_PATH: LOAD_LIBRARY_FLAGS = 8
LOAD_IGNORE_CODE_AUTHZ_LEVEL: LOAD_LIBRARY_FLAGS = 16
LOAD_LIBRARY_AS_IMAGE_RESOURCE: LOAD_LIBRARY_FLAGS = 32
LOAD_LIBRARY_AS_DATAFILE_EXCLUSIVE: LOAD_LIBRARY_FLAGS = 64
LOAD_LIBRARY_REQUIRE_SIGNED_TARGET: LOAD_LIBRARY_FLAGS = 128
LOAD_LIBRARY_SEARCH_DLL_LOAD_DIR: LOAD_LIBRARY_FLAGS = 256
LOAD_LIBRARY_SEARCH_APPLICATION_DIR: LOAD_LIBRARY_FLAGS = 512
LOAD_LIBRARY_SEARCH_USER_DIRS: LOAD_LIBRARY_FLAGS = 1024
LOAD_LIBRARY_SEARCH_SYSTEM32: LOAD_LIBRARY_FLAGS = 2048
LOAD_LIBRARY_SEARCH_DEFAULT_DIRS: LOAD_LIBRARY_FLAGS = 4096
LOAD_LIBRARY_SAFE_CURRENT_DIRS: LOAD_LIBRARY_FLAGS = 8192
LOAD_LIBRARY_SEARCH_SYSTEM32_NO_FORWARDER: LOAD_LIBRARY_FLAGS = 16384
@winfunctype_pointer
def PGET_MODULE_HANDLE_EXA(dwFlags: UInt32, lpModuleName: win32more.Foundation.PSTR, phModule: POINTER(win32more.Foundation.HINSTANCE)) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def PGET_MODULE_HANDLE_EXW(dwFlags: UInt32, lpModuleName: win32more.Foundation.PWSTR, phModule: POINTER(win32more.Foundation.HINSTANCE)) -> win32more.Foundation.BOOL: ...
class REDIRECTION_DESCRIPTOR(Structure):
    Version: UInt32
    FunctionCount: UInt32
    Redirections: POINTER(win32more.System.LibraryLoader.REDIRECTION_FUNCTION_DESCRIPTOR_head)
class REDIRECTION_FUNCTION_DESCRIPTOR(Structure):
    DllName: win32more.Foundation.PSTR
    FunctionName: win32more.Foundation.PSTR
    RedirectionTarget: c_void_p
make_head(_module, 'ENUMRESLANGPROCA')
make_head(_module, 'ENUMRESLANGPROCW')
make_head(_module, 'ENUMRESNAMEPROCA')
make_head(_module, 'ENUMRESNAMEPROCW')
make_head(_module, 'ENUMRESTYPEPROCA')
make_head(_module, 'ENUMRESTYPEPROCW')
make_head(_module, 'ENUMUILANG')
make_head(_module, 'PGET_MODULE_HANDLE_EXA')
make_head(_module, 'PGET_MODULE_HANDLE_EXW')
make_head(_module, 'REDIRECTION_DESCRIPTOR')
make_head(_module, 'REDIRECTION_FUNCTION_DESCRIPTOR')
__all__ = [
    "AddDllDirectory",
    "BeginUpdateResourceA",
    "BeginUpdateResourceW",
    "CURRENT_IMPORT_REDIRECTION_VERSION",
    "DONT_RESOLVE_DLL_REFERENCES",
    "DisableThreadLibraryCalls",
    "ENUMRESLANGPROCA",
    "ENUMRESLANGPROCW",
    "ENUMRESNAMEPROCA",
    "ENUMRESNAMEPROCW",
    "ENUMRESTYPEPROCA",
    "ENUMRESTYPEPROCW",
    "ENUMUILANG",
    "EndUpdateResourceA",
    "EndUpdateResourceW",
    "EnumResourceLanguagesA",
    "EnumResourceLanguagesExA",
    "EnumResourceLanguagesExW",
    "EnumResourceLanguagesW",
    "EnumResourceNamesA",
    "EnumResourceNamesExA",
    "EnumResourceNamesExW",
    "EnumResourceNamesW",
    "EnumResourceTypesA",
    "EnumResourceTypesExA",
    "EnumResourceTypesExW",
    "EnumResourceTypesW",
    "FIND_RESOURCE_DIRECTORY_LANGUAGES",
    "FIND_RESOURCE_DIRECTORY_NAMES",
    "FIND_RESOURCE_DIRECTORY_TYPES",
    "FindResourceA",
    "FindResourceExA",
    "FindResourceExW",
    "FindResourceW",
    "FreeLibrary",
    "FreeLibraryAndExitThread",
    "FreeResource",
    "GET_MODULE_HANDLE_EX_FLAG_FROM_ADDRESS",
    "GET_MODULE_HANDLE_EX_FLAG_PIN",
    "GET_MODULE_HANDLE_EX_FLAG_UNCHANGED_REFCOUNT",
    "GetDllDirectoryA",
    "GetDllDirectoryW",
    "GetModuleFileNameA",
    "GetModuleFileNameW",
    "GetModuleHandleA",
    "GetModuleHandleExA",
    "GetModuleHandleExW",
    "GetModuleHandleW",
    "GetProcAddress",
    "LOAD_IGNORE_CODE_AUTHZ_LEVEL",
    "LOAD_LIBRARY_AS_DATAFILE",
    "LOAD_LIBRARY_AS_DATAFILE_EXCLUSIVE",
    "LOAD_LIBRARY_AS_IMAGE_RESOURCE",
    "LOAD_LIBRARY_FLAGS",
    "LOAD_LIBRARY_OS_INTEGRITY_CONTINUITY",
    "LOAD_LIBRARY_REQUIRE_SIGNED_TARGET",
    "LOAD_LIBRARY_SAFE_CURRENT_DIRS",
    "LOAD_LIBRARY_SEARCH_APPLICATION_DIR",
    "LOAD_LIBRARY_SEARCH_DEFAULT_DIRS",
    "LOAD_LIBRARY_SEARCH_DLL_LOAD_DIR",
    "LOAD_LIBRARY_SEARCH_SYSTEM32",
    "LOAD_LIBRARY_SEARCH_SYSTEM32_NO_FORWARDER",
    "LOAD_LIBRARY_SEARCH_USER_DIRS",
    "LOAD_WITH_ALTERED_SEARCH_PATH",
    "LoadLibraryA",
    "LoadLibraryExA",
    "LoadLibraryExW",
    "LoadLibraryW",
    "LoadModule",
    "LoadPackagedLibrary",
    "LoadResource",
    "LockResource",
    "PGET_MODULE_HANDLE_EXA",
    "PGET_MODULE_HANDLE_EXW",
    "REDIRECTION_DESCRIPTOR",
    "REDIRECTION_FUNCTION_DESCRIPTOR",
    "RESOURCE_ENUM_LN",
    "RESOURCE_ENUM_MODULE_EXACT",
    "RESOURCE_ENUM_MUI",
    "RESOURCE_ENUM_MUI_SYSTEM",
    "RESOURCE_ENUM_VALIDATE",
    "RemoveDllDirectory",
    "SUPPORT_LANG_NUMBER",
    "SetDefaultDllDirectories",
    "SetDllDirectoryA",
    "SetDllDirectoryW",
    "SizeofResource",
    "UpdateResourceA",
    "UpdateResourceW",
]
