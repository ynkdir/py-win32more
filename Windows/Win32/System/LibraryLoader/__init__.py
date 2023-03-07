from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.System.LibraryLoader
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
def DisableThreadLibraryCalls(hLibModule: Windows.Win32.Foundation.HINSTANCE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindResourceExW(hModule: Windows.Win32.Foundation.HINSTANCE, lpType: Windows.Win32.Foundation.PWSTR, lpName: Windows.Win32.Foundation.PWSTR, wLanguage: UInt16) -> Windows.Win32.Foundation.HRSRC: ...
@winfunctype('KERNEL32.dll')
def FreeLibrary(hLibModule: Windows.Win32.Foundation.HINSTANCE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FreeLibraryAndExitThread(hLibModule: Windows.Win32.Foundation.HINSTANCE, dwExitCode: UInt32) -> Void: ...
@winfunctype('KERNEL32.dll')
def FreeResource(hResData: Windows.Win32.Foundation.HGLOBAL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetModuleFileNameA(hModule: Windows.Win32.Foundation.HINSTANCE, lpFilename: Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetModuleFileNameW(hModule: Windows.Win32.Foundation.HINSTANCE, lpFilename: Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetModuleHandleA(lpModuleName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HINSTANCE: ...
@winfunctype('KERNEL32.dll')
def GetModuleHandleW(lpModuleName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HINSTANCE: ...
@winfunctype('KERNEL32.dll')
def GetModuleHandleExA(dwFlags: UInt32, lpModuleName: Windows.Win32.Foundation.PSTR, phModule: POINTER(Windows.Win32.Foundation.HINSTANCE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetModuleHandleExW(dwFlags: UInt32, lpModuleName: Windows.Win32.Foundation.PWSTR, phModule: POINTER(Windows.Win32.Foundation.HINSTANCE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcAddress(hModule: Windows.Win32.Foundation.HINSTANCE, lpProcName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.FARPROC: ...
@winfunctype('KERNEL32.dll')
def LoadLibraryExA(lpLibFileName: Windows.Win32.Foundation.PSTR, hFile: Windows.Win32.Foundation.HANDLE, dwFlags: Windows.Win32.System.LibraryLoader.LOAD_LIBRARY_FLAGS) -> Windows.Win32.Foundation.HINSTANCE: ...
@winfunctype('KERNEL32.dll')
def LoadLibraryExW(lpLibFileName: Windows.Win32.Foundation.PWSTR, hFile: Windows.Win32.Foundation.HANDLE, dwFlags: Windows.Win32.System.LibraryLoader.LOAD_LIBRARY_FLAGS) -> Windows.Win32.Foundation.HINSTANCE: ...
@winfunctype('KERNEL32.dll')
def LoadResource(hModule: Windows.Win32.Foundation.HINSTANCE, hResInfo: Windows.Win32.Foundation.HRSRC) -> Windows.Win32.Foundation.HGLOBAL: ...
@winfunctype('KERNEL32.dll')
def LockResource(hResData: Windows.Win32.Foundation.HGLOBAL) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def SizeofResource(hModule: Windows.Win32.Foundation.HINSTANCE, hResInfo: Windows.Win32.Foundation.HRSRC) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def AddDllDirectory(NewDirectory: Windows.Win32.Foundation.PWSTR) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def RemoveDllDirectory(Cookie: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetDefaultDllDirectories(DirectoryFlags: Windows.Win32.System.LibraryLoader.LOAD_LIBRARY_FLAGS) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceLanguagesExA(hModule: Windows.Win32.Foundation.HINSTANCE, lpType: Windows.Win32.Foundation.PSTR, lpName: Windows.Win32.Foundation.PSTR, lpEnumFunc: Windows.Win32.System.LibraryLoader.ENUMRESLANGPROCA, lParam: IntPtr, dwFlags: UInt32, LangId: UInt16) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceLanguagesExW(hModule: Windows.Win32.Foundation.HINSTANCE, lpType: Windows.Win32.Foundation.PWSTR, lpName: Windows.Win32.Foundation.PWSTR, lpEnumFunc: Windows.Win32.System.LibraryLoader.ENUMRESLANGPROCW, lParam: IntPtr, dwFlags: UInt32, LangId: UInt16) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceNamesExA(hModule: Windows.Win32.Foundation.HINSTANCE, lpType: Windows.Win32.Foundation.PSTR, lpEnumFunc: Windows.Win32.System.LibraryLoader.ENUMRESNAMEPROCA, lParam: IntPtr, dwFlags: UInt32, LangId: UInt16) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceNamesExW(hModule: Windows.Win32.Foundation.HINSTANCE, lpType: Windows.Win32.Foundation.PWSTR, lpEnumFunc: Windows.Win32.System.LibraryLoader.ENUMRESNAMEPROCW, lParam: IntPtr, dwFlags: UInt32, LangId: UInt16) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceTypesExA(hModule: Windows.Win32.Foundation.HINSTANCE, lpEnumFunc: Windows.Win32.System.LibraryLoader.ENUMRESTYPEPROCA, lParam: IntPtr, dwFlags: UInt32, LangId: UInt16) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceTypesExW(hModule: Windows.Win32.Foundation.HINSTANCE, lpEnumFunc: Windows.Win32.System.LibraryLoader.ENUMRESTYPEPROCW, lParam: IntPtr, dwFlags: UInt32, LangId: UInt16) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindResourceW(hModule: Windows.Win32.Foundation.HINSTANCE, lpName: Windows.Win32.Foundation.PWSTR, lpType: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRSRC: ...
@winfunctype('KERNEL32.dll')
def LoadLibraryA(lpLibFileName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HINSTANCE: ...
@winfunctype('KERNEL32.dll')
def LoadLibraryW(lpLibFileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HINSTANCE: ...
@winfunctype('KERNEL32.dll')
def EnumResourceNamesW(hModule: Windows.Win32.Foundation.HINSTANCE, lpType: Windows.Win32.Foundation.PWSTR, lpEnumFunc: Windows.Win32.System.LibraryLoader.ENUMRESNAMEPROCW, lParam: IntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceNamesA(hModule: Windows.Win32.Foundation.HINSTANCE, lpType: Windows.Win32.Foundation.PSTR, lpEnumFunc: Windows.Win32.System.LibraryLoader.ENUMRESNAMEPROCA, lParam: IntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def LoadModule(lpModuleName: Windows.Win32.Foundation.PSTR, lpParameterBlock: c_void_p) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def LoadPackagedLibrary(lpwLibFileName: Windows.Win32.Foundation.PWSTR, Reserved: UInt32) -> Windows.Win32.Foundation.HINSTANCE: ...
@winfunctype('KERNEL32.dll')
def FindResourceA(hModule: Windows.Win32.Foundation.HINSTANCE, lpName: Windows.Win32.Foundation.PSTR, lpType: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRSRC: ...
@winfunctype('KERNEL32.dll')
def FindResourceExA(hModule: Windows.Win32.Foundation.HINSTANCE, lpType: Windows.Win32.Foundation.PSTR, lpName: Windows.Win32.Foundation.PSTR, wLanguage: UInt16) -> Windows.Win32.Foundation.HRSRC: ...
@winfunctype('KERNEL32.dll')
def EnumResourceTypesA(hModule: Windows.Win32.Foundation.HINSTANCE, lpEnumFunc: Windows.Win32.System.LibraryLoader.ENUMRESTYPEPROCA, lParam: IntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceTypesW(hModule: Windows.Win32.Foundation.HINSTANCE, lpEnumFunc: Windows.Win32.System.LibraryLoader.ENUMRESTYPEPROCW, lParam: IntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceLanguagesA(hModule: Windows.Win32.Foundation.HINSTANCE, lpType: Windows.Win32.Foundation.PSTR, lpName: Windows.Win32.Foundation.PSTR, lpEnumFunc: Windows.Win32.System.LibraryLoader.ENUMRESLANGPROCA, lParam: IntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceLanguagesW(hModule: Windows.Win32.Foundation.HINSTANCE, lpType: Windows.Win32.Foundation.PWSTR, lpName: Windows.Win32.Foundation.PWSTR, lpEnumFunc: Windows.Win32.System.LibraryLoader.ENUMRESLANGPROCW, lParam: IntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def BeginUpdateResourceA(pFileName: Windows.Win32.Foundation.PSTR, bDeleteExistingResources: Windows.Win32.Foundation.BOOL) -> Windows.Win32.System.LibraryLoader.UPDATERESOURCE_HANDLE: ...
@winfunctype('KERNEL32.dll')
def BeginUpdateResourceW(pFileName: Windows.Win32.Foundation.PWSTR, bDeleteExistingResources: Windows.Win32.Foundation.BOOL) -> Windows.Win32.System.LibraryLoader.UPDATERESOURCE_HANDLE: ...
@winfunctype('KERNEL32.dll')
def UpdateResourceA(hUpdate: Windows.Win32.System.LibraryLoader.UPDATERESOURCE_HANDLE, lpType: Windows.Win32.Foundation.PSTR, lpName: Windows.Win32.Foundation.PSTR, wLanguage: UInt16, lpData: c_void_p, cb: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def UpdateResourceW(hUpdate: Windows.Win32.System.LibraryLoader.UPDATERESOURCE_HANDLE, lpType: Windows.Win32.Foundation.PWSTR, lpName: Windows.Win32.Foundation.PWSTR, wLanguage: UInt16, lpData: c_void_p, cb: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EndUpdateResourceA(hUpdate: Windows.Win32.System.LibraryLoader.UPDATERESOURCE_HANDLE, fDiscard: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EndUpdateResourceW(hUpdate: Windows.Win32.System.LibraryLoader.UPDATERESOURCE_HANDLE, fDiscard: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetDllDirectoryA(lpPathName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetDllDirectoryW(lpPathName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetDllDirectoryA(nBufferLength: UInt32, lpBuffer: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetDllDirectoryW(nBufferLength: UInt32, lpBuffer: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype_pointer
def ENUMRESLANGPROCA(hModule: Windows.Win32.Foundation.HINSTANCE, lpType: Windows.Win32.Foundation.PSTR, lpName: Windows.Win32.Foundation.PSTR, wLanguage: UInt16, lParam: IntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def ENUMRESLANGPROCW(hModule: Windows.Win32.Foundation.HINSTANCE, lpType: Windows.Win32.Foundation.PWSTR, lpName: Windows.Win32.Foundation.PWSTR, wLanguage: UInt16, lParam: IntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def ENUMRESNAMEPROCA(hModule: Windows.Win32.Foundation.HINSTANCE, lpType: Windows.Win32.Foundation.PSTR, lpName: Windows.Win32.Foundation.PSTR, lParam: IntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def ENUMRESNAMEPROCW(hModule: Windows.Win32.Foundation.HINSTANCE, lpType: Windows.Win32.Foundation.PWSTR, lpName: Windows.Win32.Foundation.PWSTR, lParam: IntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def ENUMRESTYPEPROCA(hModule: Windows.Win32.Foundation.HINSTANCE, lpType: Windows.Win32.Foundation.PSTR, lParam: IntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def ENUMRESTYPEPROCW(hModule: Windows.Win32.Foundation.HINSTANCE, lpType: Windows.Win32.Foundation.PWSTR, lParam: IntPtr) -> Windows.Win32.Foundation.BOOL: ...
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
def PGET_MODULE_HANDLE_EXA(dwFlags: UInt32, lpModuleName: Windows.Win32.Foundation.PSTR, phModule: POINTER(Windows.Win32.Foundation.HINSTANCE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PGET_MODULE_HANDLE_EXW(dwFlags: UInt32, lpModuleName: Windows.Win32.Foundation.PWSTR, phModule: POINTER(Windows.Win32.Foundation.HINSTANCE)) -> Windows.Win32.Foundation.BOOL: ...
class REDIRECTION_DESCRIPTOR(Structure):
    Version: UInt32
    FunctionCount: UInt32
    Redirections: POINTER(Windows.Win32.System.LibraryLoader.REDIRECTION_FUNCTION_DESCRIPTOR_head)
class REDIRECTION_FUNCTION_DESCRIPTOR(Structure):
    DllName: Windows.Win32.Foundation.PSTR
    FunctionName: Windows.Win32.Foundation.PSTR
    RedirectionTarget: c_void_p
UPDATERESOURCE_HANDLE = IntPtr
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
    "UPDATERESOURCE_HANDLE",
    "UpdateResourceA",
    "UpdateResourceW",
]
_arch_optional = [
]
