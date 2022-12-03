from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.LibraryLoader
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
FIND_RESOURCE_DIRECTORY_TYPES = 256
FIND_RESOURCE_DIRECTORY_NAMES = 512
FIND_RESOURCE_DIRECTORY_LANGUAGES = 1024
RESOURCE_ENUM_LN = 1
RESOURCE_ENUM_MUI = 2
RESOURCE_ENUM_MUI_SYSTEM = 4
RESOURCE_ENUM_VALIDATE = 8
RESOURCE_ENUM_MODULE_EXACT = 16
SUPPORT_LANG_NUMBER = 32
GET_MODULE_HANDLE_EX_FLAG_PIN = 1
GET_MODULE_HANDLE_EX_FLAG_UNCHANGED_REFCOUNT = 2
GET_MODULE_HANDLE_EX_FLAG_FROM_ADDRESS = 4
CURRENT_IMPORT_REDIRECTION_VERSION = 1
LOAD_LIBRARY_OS_INTEGRITY_CONTINUITY = 32768
def _define_DisableThreadLibraryCalls():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE)(('DisableThreadLibraryCalls', windll['KERNEL32.dll']), ((1, 'hLibModule'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindResourceExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRSRC,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt16)(('FindResourceExW', windll['KERNEL32.dll']), ((1, 'hModule'),(1, 'lpType'),(1, 'lpName'),(1, 'wLanguage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FreeLibrary():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE)(('FreeLibrary', windll['KERNEL32.dll']), ((1, 'hLibModule'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FreeLibraryAndExitThread():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.HINSTANCE,UInt32)(('FreeLibraryAndExitThread', windll['KERNEL32.dll']), ((1, 'hLibModule'),(1, 'dwExitCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FreeResource():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr)(('FreeResource', windll['KERNEL32.dll']), ((1, 'hResData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetModuleFileNameA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR,UInt32)(('GetModuleFileNameA', windll['KERNEL32.dll']), ((1, 'hModule'),(1, 'lpFilename'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetModuleFileNameW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,UInt32)(('GetModuleFileNameW', windll['KERNEL32.dll']), ((1, 'hModule'),(1, 'lpFilename'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetModuleHandleA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR)(('GetModuleHandleA', windll['KERNEL32.dll']), ((1, 'lpModuleName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetModuleHandleW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR)(('GetModuleHandleW', windll['KERNEL32.dll']), ((1, 'lpModuleName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetModuleHandleExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.PSTR,POINTER(win32more.Foundation.HINSTANCE))(('GetModuleHandleExA', windll['KERNEL32.dll']), ((1, 'dwFlags'),(1, 'lpModuleName'),(1, 'phModule'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetModuleHandleExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.HINSTANCE))(('GetModuleHandleExW', windll['KERNEL32.dll']), ((1, 'dwFlags'),(1, 'lpModuleName'),(1, 'phModule'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProcAddress():
    try:
        return WINFUNCTYPE(win32more.Foundation.FARPROC,win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR)(('GetProcAddress', windll['KERNEL32.dll']), ((1, 'hModule'),(1, 'lpProcName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadLibraryExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR,win32more.Foundation.HANDLE,win32more.System.LibraryLoader.LOAD_LIBRARY_FLAGS)(('LoadLibraryExA', windll['KERNEL32.dll']), ((1, 'lpLibFileName'),(1, 'hFile'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadLibraryExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,win32more.Foundation.HANDLE,win32more.System.LibraryLoader.LOAD_LIBRARY_FLAGS)(('LoadLibraryExW', windll['KERNEL32.dll']), ((1, 'lpLibFileName'),(1, 'hFile'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadResource():
    try:
        return WINFUNCTYPE(IntPtr,win32more.Foundation.HINSTANCE,win32more.Foundation.HRSRC)(('LoadResource', windll['KERNEL32.dll']), ((1, 'hModule'),(1, 'hResInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LockResource():
    try:
        return WINFUNCTYPE(c_void_p,IntPtr)(('LockResource', windll['KERNEL32.dll']), ((1, 'hResData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SizeofResource():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HINSTANCE,win32more.Foundation.HRSRC)(('SizeofResource', windll['KERNEL32.dll']), ((1, 'hModule'),(1, 'hResInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddDllDirectory():
    try:
        return WINFUNCTYPE(c_void_p,win32more.Foundation.PWSTR)(('AddDllDirectory', windll['KERNEL32.dll']), ((1, 'NewDirectory'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveDllDirectory():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p)(('RemoveDllDirectory', windll['KERNEL32.dll']), ((1, 'Cookie'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetDefaultDllDirectories():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.LibraryLoader.LOAD_LIBRARY_FLAGS)(('SetDefaultDllDirectories', windll['KERNEL32.dll']), ((1, 'DirectoryFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumResourceLanguagesExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.System.LibraryLoader.ENUMRESLANGPROCA,IntPtr,UInt32,UInt16)(('EnumResourceLanguagesExA', windll['KERNEL32.dll']), ((1, 'hModule'),(1, 'lpType'),(1, 'lpName'),(1, 'lpEnumFunc'),(1, 'lParam'),(1, 'dwFlags'),(1, 'LangId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumResourceLanguagesExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.System.LibraryLoader.ENUMRESLANGPROCW,IntPtr,UInt32,UInt16)(('EnumResourceLanguagesExW', windll['KERNEL32.dll']), ((1, 'hModule'),(1, 'lpType'),(1, 'lpName'),(1, 'lpEnumFunc'),(1, 'lParam'),(1, 'dwFlags'),(1, 'LangId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumResourceNamesExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR,win32more.System.LibraryLoader.ENUMRESNAMEPROCA,IntPtr,UInt32,UInt16)(('EnumResourceNamesExA', windll['KERNEL32.dll']), ((1, 'hModule'),(1, 'lpType'),(1, 'lpEnumFunc'),(1, 'lParam'),(1, 'dwFlags'),(1, 'LangId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumResourceNamesExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,win32more.System.LibraryLoader.ENUMRESNAMEPROCW,IntPtr,UInt32,UInt16)(('EnumResourceNamesExW', windll['KERNEL32.dll']), ((1, 'hModule'),(1, 'lpType'),(1, 'lpEnumFunc'),(1, 'lParam'),(1, 'dwFlags'),(1, 'LangId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumResourceTypesExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.System.LibraryLoader.ENUMRESTYPEPROCA,IntPtr,UInt32,UInt16)(('EnumResourceTypesExA', windll['KERNEL32.dll']), ((1, 'hModule'),(1, 'lpEnumFunc'),(1, 'lParam'),(1, 'dwFlags'),(1, 'LangId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumResourceTypesExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.System.LibraryLoader.ENUMRESTYPEPROCW,IntPtr,UInt32,UInt16)(('EnumResourceTypesExW', windll['KERNEL32.dll']), ((1, 'hModule'),(1, 'lpEnumFunc'),(1, 'lParam'),(1, 'dwFlags'),(1, 'LangId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindResourceW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRSRC,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('FindResourceW', windll['KERNEL32.dll']), ((1, 'hModule'),(1, 'lpName'),(1, 'lpType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadLibraryA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR)(('LoadLibraryA', windll['KERNEL32.dll']), ((1, 'lpLibFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadLibraryW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR)(('LoadLibraryW', windll['KERNEL32.dll']), ((1, 'lpLibFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumResourceNamesW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,win32more.System.LibraryLoader.ENUMRESNAMEPROCW,IntPtr)(('EnumResourceNamesW', windll['KERNEL32.dll']), ((1, 'hModule'),(1, 'lpType'),(1, 'lpEnumFunc'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumResourceNamesA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR,win32more.System.LibraryLoader.ENUMRESNAMEPROCA,IntPtr)(('EnumResourceNamesA', windll['KERNEL32.dll']), ((1, 'hModule'),(1, 'lpType'),(1, 'lpEnumFunc'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadModule():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,c_void_p)(('LoadModule', windll['KERNEL32.dll']), ((1, 'lpModuleName'),(1, 'lpParameterBlock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadPackagedLibrary():
    try:
        return WINFUNCTYPE(win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,UInt32)(('LoadPackagedLibrary', windll['KERNEL32.dll']), ((1, 'lpwLibFileName'),(1, 'Reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindResourceA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRSRC,win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('FindResourceA', windll['KERNEL32.dll']), ((1, 'hModule'),(1, 'lpName'),(1, 'lpType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindResourceExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRSRC,win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt16)(('FindResourceExA', windll['KERNEL32.dll']), ((1, 'hModule'),(1, 'lpType'),(1, 'lpName'),(1, 'wLanguage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumResourceTypesA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.System.LibraryLoader.ENUMRESTYPEPROCA,IntPtr)(('EnumResourceTypesA', windll['KERNEL32.dll']), ((1, 'hModule'),(1, 'lpEnumFunc'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumResourceTypesW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.System.LibraryLoader.ENUMRESTYPEPROCW,IntPtr)(('EnumResourceTypesW', windll['KERNEL32.dll']), ((1, 'hModule'),(1, 'lpEnumFunc'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumResourceLanguagesA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.System.LibraryLoader.ENUMRESLANGPROCA,IntPtr)(('EnumResourceLanguagesA', windll['KERNEL32.dll']), ((1, 'hModule'),(1, 'lpType'),(1, 'lpName'),(1, 'lpEnumFunc'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumResourceLanguagesW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.System.LibraryLoader.ENUMRESLANGPROCW,IntPtr)(('EnumResourceLanguagesW', windll['KERNEL32.dll']), ((1, 'hModule'),(1, 'lpType'),(1, 'lpName'),(1, 'lpEnumFunc'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BeginUpdateResourceA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PSTR,win32more.Foundation.BOOL)(('BeginUpdateResourceA', windll['KERNEL32.dll']), ((1, 'pFileName'),(1, 'bDeleteExistingResources'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BeginUpdateResourceW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.BOOL)(('BeginUpdateResourceW', windll['KERNEL32.dll']), ((1, 'pFileName'),(1, 'bDeleteExistingResources'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UpdateResourceA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt16,c_void_p,UInt32)(('UpdateResourceA', windll['KERNEL32.dll']), ((1, 'hUpdate'),(1, 'lpType'),(1, 'lpName'),(1, 'wLanguage'),(1, 'lpData'),(1, 'cb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UpdateResourceW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt16,c_void_p,UInt32)(('UpdateResourceW', windll['KERNEL32.dll']), ((1, 'hUpdate'),(1, 'lpType'),(1, 'lpName'),(1, 'wLanguage'),(1, 'lpData'),(1, 'cb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EndUpdateResourceA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.BOOL)(('EndUpdateResourceA', windll['KERNEL32.dll']), ((1, 'hUpdate'),(1, 'fDiscard'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EndUpdateResourceW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.BOOL)(('EndUpdateResourceW', windll['KERNEL32.dll']), ((1, 'hUpdate'),(1, 'fDiscard'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetDllDirectoryA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR)(('SetDllDirectoryA', windll['KERNEL32.dll']), ((1, 'lpPathName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetDllDirectoryW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR)(('SetDllDirectoryW', windll['KERNEL32.dll']), ((1, 'lpPathName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDllDirectoryA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.PSTR)(('GetDllDirectoryA', windll['KERNEL32.dll']), ((1, 'nBufferLength'),(1, 'lpBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDllDirectoryW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.PWSTR)(('GetDllDirectoryW', windll['KERNEL32.dll']), ((1, 'nBufferLength'),(1, 'lpBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ENUMRESLANGPROCA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt16,IntPtr)
def _define_ENUMRESLANGPROCW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt16,IntPtr)
def _define_ENUMRESNAMEPROCA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,IntPtr)
def _define_ENUMRESNAMEPROCW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,IntPtr)
def _define_ENUMRESTYPEPROCA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR,IntPtr)
def _define_ENUMRESTYPEPROCW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,IntPtr)
def _define_ENUMUILANG_head():
    class ENUMUILANG(Structure):
        pass
    return ENUMUILANG
def _define_ENUMUILANG():
    ENUMUILANG = win32more.System.LibraryLoader.ENUMUILANG_head
    ENUMUILANG._fields_ = [
        ('NumOfEnumUILang', UInt32),
        ('SizeOfEnumUIBuffer', UInt32),
        ('pEnumUIBuffer', POINTER(UInt16)),
    ]
    return ENUMUILANG
LOAD_LIBRARY_FLAGS = UInt32
DONT_RESOLVE_DLL_REFERENCES = 1
LOAD_LIBRARY_AS_DATAFILE = 2
LOAD_WITH_ALTERED_SEARCH_PATH = 8
LOAD_IGNORE_CODE_AUTHZ_LEVEL = 16
LOAD_LIBRARY_AS_IMAGE_RESOURCE = 32
LOAD_LIBRARY_AS_DATAFILE_EXCLUSIVE = 64
LOAD_LIBRARY_REQUIRE_SIGNED_TARGET = 128
LOAD_LIBRARY_SEARCH_DLL_LOAD_DIR = 256
LOAD_LIBRARY_SEARCH_APPLICATION_DIR = 512
LOAD_LIBRARY_SEARCH_USER_DIRS = 1024
LOAD_LIBRARY_SEARCH_SYSTEM32 = 2048
LOAD_LIBRARY_SEARCH_DEFAULT_DIRS = 4096
LOAD_LIBRARY_SAFE_CURRENT_DIRS = 8192
LOAD_LIBRARY_SEARCH_SYSTEM32_NO_FORWARDER = 16384
def _define_PGET_MODULE_HANDLE_EXA():
    return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.PSTR,POINTER(win32more.Foundation.HINSTANCE))
def _define_PGET_MODULE_HANDLE_EXW():
    return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.HINSTANCE))
def _define_REDIRECTION_DESCRIPTOR_head():
    class REDIRECTION_DESCRIPTOR(Structure):
        pass
    return REDIRECTION_DESCRIPTOR
def _define_REDIRECTION_DESCRIPTOR():
    REDIRECTION_DESCRIPTOR = win32more.System.LibraryLoader.REDIRECTION_DESCRIPTOR_head
    REDIRECTION_DESCRIPTOR._fields_ = [
        ('Version', UInt32),
        ('FunctionCount', UInt32),
        ('Redirections', POINTER(win32more.System.LibraryLoader.REDIRECTION_FUNCTION_DESCRIPTOR_head)),
    ]
    return REDIRECTION_DESCRIPTOR
def _define_REDIRECTION_FUNCTION_DESCRIPTOR_head():
    class REDIRECTION_FUNCTION_DESCRIPTOR(Structure):
        pass
    return REDIRECTION_FUNCTION_DESCRIPTOR
def _define_REDIRECTION_FUNCTION_DESCRIPTOR():
    REDIRECTION_FUNCTION_DESCRIPTOR = win32more.System.LibraryLoader.REDIRECTION_FUNCTION_DESCRIPTOR_head
    REDIRECTION_FUNCTION_DESCRIPTOR._fields_ = [
        ('DllName', win32more.Foundation.PSTR),
        ('FunctionName', win32more.Foundation.PSTR),
        ('RedirectionTarget', c_void_p),
    ]
    return REDIRECTION_FUNCTION_DESCRIPTOR
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
