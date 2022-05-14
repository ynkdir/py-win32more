from win32more import *
import win32more.System.LibraryLoader
import win32more.Foundation

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.System.LibraryLoader, name, eval(f"_define_{name}()"))
    return getattr(win32more.System.LibraryLoader, name)
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
def _define_ENUMUILANG_head():
    class ENUMUILANG(Structure):
        pass
    return ENUMUILANG
def _define_ENUMUILANG():
    ENUMUILANG = win32more.System.LibraryLoader.ENUMUILANG_head
    ENUMUILANG._fields_ = [
        ("NumOfEnumUILang", UInt32),
        ("SizeOfEnumUIBuffer", UInt32),
        ("pEnumUIBuffer", POINTER(UInt16)),
    ]
    return ENUMUILANG
def _define_ENUMRESLANGPROCA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt16,IntPtr, use_last_error=False)
def _define_ENUMRESLANGPROCW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt16,IntPtr, use_last_error=False)
def _define_ENUMRESNAMEPROCA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,IntPtr, use_last_error=False)
def _define_ENUMRESNAMEPROCW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,IntPtr, use_last_error=False)
def _define_ENUMRESTYPEPROCA():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR,IntPtr, use_last_error=False)
def _define_ENUMRESTYPEPROCW():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,IntPtr, use_last_error=False)
def _define_PGET_MODULE_HANDLE_EXA():
    return CFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.PSTR,POINTER(win32more.Foundation.HINSTANCE), use_last_error=False)
def _define_PGET_MODULE_HANDLE_EXW():
    return CFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.HINSTANCE), use_last_error=False)
def _define_REDIRECTION_FUNCTION_DESCRIPTOR_head():
    class REDIRECTION_FUNCTION_DESCRIPTOR(Structure):
        pass
    return REDIRECTION_FUNCTION_DESCRIPTOR
def _define_REDIRECTION_FUNCTION_DESCRIPTOR():
    REDIRECTION_FUNCTION_DESCRIPTOR = win32more.System.LibraryLoader.REDIRECTION_FUNCTION_DESCRIPTOR_head
    REDIRECTION_FUNCTION_DESCRIPTOR._fields_ = [
        ("DllName", win32more.Foundation.PSTR),
        ("FunctionName", win32more.Foundation.PSTR),
        ("RedirectionTarget", c_void_p),
    ]
    return REDIRECTION_FUNCTION_DESCRIPTOR
def _define_REDIRECTION_DESCRIPTOR_head():
    class REDIRECTION_DESCRIPTOR(Structure):
        pass
    return REDIRECTION_DESCRIPTOR
def _define_REDIRECTION_DESCRIPTOR():
    REDIRECTION_DESCRIPTOR = win32more.System.LibraryLoader.REDIRECTION_DESCRIPTOR_head
    REDIRECTION_DESCRIPTOR._fields_ = [
        ("Version", UInt32),
        ("FunctionCount", UInt32),
        ("Redirections", POINTER(win32more.System.LibraryLoader.REDIRECTION_FUNCTION_DESCRIPTOR_head)),
    ]
    return REDIRECTION_DESCRIPTOR
def _define_DisableThreadLibraryCalls():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE, use_last_error=True)(("DisableThreadLibraryCalls", windll["KERNEL32"]), ((1, 'hLibModule'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindResourceExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRSRC,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt16, use_last_error=False)(("FindResourceExW", windll["KERNEL32"]), ((1, 'hModule'),(1, 'lpType'),(1, 'lpName'),(1, 'wLanguage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindResourceEx():
    return win32more.System.LibraryLoader.FindResourceExW
def _define_FreeLibrary():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE, use_last_error=True)(("FreeLibrary", windll["KERNEL32"]), ((1, 'hLibModule'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FreeLibraryAndExitThread():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.HINSTANCE,UInt32, use_last_error=False)(("FreeLibraryAndExitThread", windll["KERNEL32"]), ((1, 'hLibModule'),(1, 'dwExitCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FreeResource():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr, use_last_error=False)(("FreeResource", windll["KERNEL32"]), ((1, 'hResData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetModuleFileNameA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HINSTANCE,POINTER(Byte),UInt32, use_last_error=True)(("GetModuleFileNameA", windll["KERNEL32"]), ((1, 'hModule'),(1, 'lpFilename'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetModuleFileNameW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HINSTANCE,POINTER(Char),UInt32, use_last_error=True)(("GetModuleFileNameW", windll["KERNEL32"]), ((1, 'hModule'),(1, 'lpFilename'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetModuleFileName():
    return win32more.System.LibraryLoader.GetModuleFileNameW
def _define_GetModuleHandleA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR, use_last_error=True)(("GetModuleHandleA", windll["KERNEL32"]), ((1, 'lpModuleName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetModuleHandleW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR, use_last_error=True)(("GetModuleHandleW", windll["KERNEL32"]), ((1, 'lpModuleName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetModuleHandle():
    return win32more.System.LibraryLoader.GetModuleHandleW
def _define_GetModuleHandleExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.PSTR,POINTER(win32more.Foundation.HINSTANCE), use_last_error=True)(("GetModuleHandleExA", windll["KERNEL32"]), ((1, 'dwFlags'),(1, 'lpModuleName'),(1, 'phModule'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetModuleHandleExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.HINSTANCE), use_last_error=True)(("GetModuleHandleExW", windll["KERNEL32"]), ((1, 'dwFlags'),(1, 'lpModuleName'),(1, 'phModule'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetModuleHandleEx():
    return win32more.System.LibraryLoader.GetModuleHandleExW
def _define_GetProcAddress():
    try:
        return WINFUNCTYPE(win32more.Foundation.FARPROC,win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR, use_last_error=True)(("GetProcAddress", windll["KERNEL32"]), ((1, 'hModule'),(1, 'lpProcName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadLibraryExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR,win32more.Foundation.HANDLE,win32more.System.LibraryLoader.LOAD_LIBRARY_FLAGS, use_last_error=True)(("LoadLibraryExA", windll["KERNEL32"]), ((1, 'lpLibFileName'),(1, 'hFile'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadLibraryExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,win32more.Foundation.HANDLE,win32more.System.LibraryLoader.LOAD_LIBRARY_FLAGS, use_last_error=True)(("LoadLibraryExW", windll["KERNEL32"]), ((1, 'lpLibFileName'),(1, 'hFile'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadLibraryEx():
    return win32more.System.LibraryLoader.LoadLibraryExW
def _define_LoadResource():
    try:
        return WINFUNCTYPE(IntPtr,win32more.Foundation.HINSTANCE,win32more.Foundation.HRSRC, use_last_error=True)(("LoadResource", windll["KERNEL32"]), ((1, 'hModule'),(1, 'hResInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LockResource():
    try:
        return WINFUNCTYPE(c_void_p,IntPtr, use_last_error=False)(("LockResource", windll["KERNEL32"]), ((1, 'hResData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SizeofResource():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HINSTANCE,win32more.Foundation.HRSRC, use_last_error=True)(("SizeofResource", windll["KERNEL32"]), ((1, 'hModule'),(1, 'hResInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddDllDirectory():
    try:
        return WINFUNCTYPE(c_void_p,win32more.Foundation.PWSTR, use_last_error=True)(("AddDllDirectory", windll["KERNEL32"]), ((1, 'NewDirectory'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveDllDirectory():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p, use_last_error=True)(("RemoveDllDirectory", windll["KERNEL32"]), ((1, 'Cookie'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetDefaultDllDirectories():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.LibraryLoader.LOAD_LIBRARY_FLAGS, use_last_error=True)(("SetDefaultDllDirectories", windll["KERNEL32"]), ((1, 'DirectoryFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumResourceLanguagesExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.System.LibraryLoader.ENUMRESLANGPROCA,IntPtr,UInt32,UInt16, use_last_error=True)(("EnumResourceLanguagesExA", windll["KERNEL32"]), ((1, 'hModule'),(1, 'lpType'),(1, 'lpName'),(1, 'lpEnumFunc'),(1, 'lParam'),(1, 'dwFlags'),(1, 'LangId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumResourceLanguagesExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.System.LibraryLoader.ENUMRESLANGPROCW,IntPtr,UInt32,UInt16, use_last_error=True)(("EnumResourceLanguagesExW", windll["KERNEL32"]), ((1, 'hModule'),(1, 'lpType'),(1, 'lpName'),(1, 'lpEnumFunc'),(1, 'lParam'),(1, 'dwFlags'),(1, 'LangId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumResourceLanguagesEx():
    return win32more.System.LibraryLoader.EnumResourceLanguagesExW
def _define_EnumResourceNamesExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR,win32more.System.LibraryLoader.ENUMRESNAMEPROCA,IntPtr,UInt32,UInt16, use_last_error=True)(("EnumResourceNamesExA", windll["KERNEL32"]), ((1, 'hModule'),(1, 'lpType'),(1, 'lpEnumFunc'),(1, 'lParam'),(1, 'dwFlags'),(1, 'LangId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumResourceNamesExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,win32more.System.LibraryLoader.ENUMRESNAMEPROCW,IntPtr,UInt32,UInt16, use_last_error=True)(("EnumResourceNamesExW", windll["KERNEL32"]), ((1, 'hModule'),(1, 'lpType'),(1, 'lpEnumFunc'),(1, 'lParam'),(1, 'dwFlags'),(1, 'LangId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumResourceNamesEx():
    return win32more.System.LibraryLoader.EnumResourceNamesExW
def _define_EnumResourceTypesExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.System.LibraryLoader.ENUMRESTYPEPROCA,IntPtr,UInt32,UInt16, use_last_error=True)(("EnumResourceTypesExA", windll["KERNEL32"]), ((1, 'hModule'),(1, 'lpEnumFunc'),(1, 'lParam'),(1, 'dwFlags'),(1, 'LangId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumResourceTypesExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.System.LibraryLoader.ENUMRESTYPEPROCW,IntPtr,UInt32,UInt16, use_last_error=True)(("EnumResourceTypesExW", windll["KERNEL32"]), ((1, 'hModule'),(1, 'lpEnumFunc'),(1, 'lParam'),(1, 'dwFlags'),(1, 'LangId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumResourceTypesEx():
    return win32more.System.LibraryLoader.EnumResourceTypesExW
def _define_FindResourceW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRSRC,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("FindResourceW", windll["KERNEL32"]), ((1, 'hModule'),(1, 'lpName'),(1, 'lpType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindResource():
    return win32more.System.LibraryLoader.FindResourceW
def _define_LoadLibraryA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR, use_last_error=True)(("LoadLibraryA", windll["KERNEL32"]), ((1, 'lpLibFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadLibraryW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR, use_last_error=True)(("LoadLibraryW", windll["KERNEL32"]), ((1, 'lpLibFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadLibrary():
    return win32more.System.LibraryLoader.LoadLibraryW
def _define_EnumResourceNamesW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,win32more.System.LibraryLoader.ENUMRESNAMEPROCW,IntPtr, use_last_error=False)(("EnumResourceNamesW", windll["KERNEL32"]), ((1, 'hModule'),(1, 'lpType'),(1, 'lpEnumFunc'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumResourceNames():
    return win32more.System.LibraryLoader.EnumResourceNamesW
def _define_EnumResourceNamesA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR,win32more.System.LibraryLoader.ENUMRESNAMEPROCA,IntPtr, use_last_error=True)(("EnumResourceNamesA", windll["KERNEL32"]), ((1, 'hModule'),(1, 'lpType'),(1, 'lpEnumFunc'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadModule():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,c_void_p, use_last_error=False)(("LoadModule", windll["KERNEL32"]), ((1, 'lpModuleName'),(1, 'lpParameterBlock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadPackagedLibrary():
    try:
        return WINFUNCTYPE(win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,UInt32, use_last_error=True)(("LoadPackagedLibrary", windll["KERNEL32"]), ((1, 'lpwLibFileName'),(1, 'Reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindResourceA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRSRC,win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=True)(("FindResourceA", windll["KERNEL32"]), ((1, 'hModule'),(1, 'lpName'),(1, 'lpType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindResourceExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRSRC,win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt16, use_last_error=True)(("FindResourceExA", windll["KERNEL32"]), ((1, 'hModule'),(1, 'lpType'),(1, 'lpName'),(1, 'wLanguage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumResourceTypesA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.System.LibraryLoader.ENUMRESTYPEPROCA,IntPtr, use_last_error=True)(("EnumResourceTypesA", windll["KERNEL32"]), ((1, 'hModule'),(1, 'lpEnumFunc'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumResourceTypesW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.System.LibraryLoader.ENUMRESTYPEPROCW,IntPtr, use_last_error=True)(("EnumResourceTypesW", windll["KERNEL32"]), ((1, 'hModule'),(1, 'lpEnumFunc'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumResourceTypes():
    return win32more.System.LibraryLoader.EnumResourceTypesW
def _define_EnumResourceLanguagesA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.System.LibraryLoader.ENUMRESLANGPROCA,IntPtr, use_last_error=True)(("EnumResourceLanguagesA", windll["KERNEL32"]), ((1, 'hModule'),(1, 'lpType'),(1, 'lpName'),(1, 'lpEnumFunc'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumResourceLanguagesW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.System.LibraryLoader.ENUMRESLANGPROCW,IntPtr, use_last_error=True)(("EnumResourceLanguagesW", windll["KERNEL32"]), ((1, 'hModule'),(1, 'lpType'),(1, 'lpName'),(1, 'lpEnumFunc'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumResourceLanguages():
    return win32more.System.LibraryLoader.EnumResourceLanguagesW
def _define_BeginUpdateResourceA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PSTR,win32more.Foundation.BOOL, use_last_error=True)(("BeginUpdateResourceA", windll["KERNEL32"]), ((1, 'pFileName'),(1, 'bDeleteExistingResources'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BeginUpdateResourceW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=True)(("BeginUpdateResourceW", windll["KERNEL32"]), ((1, 'pFileName'),(1, 'bDeleteExistingResources'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BeginUpdateResource():
    return win32more.System.LibraryLoader.BeginUpdateResourceW
def _define_UpdateResourceA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt16,c_void_p,UInt32, use_last_error=True)(("UpdateResourceA", windll["KERNEL32"]), ((1, 'hUpdate'),(1, 'lpType'),(1, 'lpName'),(1, 'wLanguage'),(1, 'lpData'),(1, 'cb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UpdateResourceW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt16,c_void_p,UInt32, use_last_error=True)(("UpdateResourceW", windll["KERNEL32"]), ((1, 'hUpdate'),(1, 'lpType'),(1, 'lpName'),(1, 'wLanguage'),(1, 'lpData'),(1, 'cb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UpdateResource():
    return win32more.System.LibraryLoader.UpdateResourceW
def _define_EndUpdateResourceA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.BOOL, use_last_error=True)(("EndUpdateResourceA", windll["KERNEL32"]), ((1, 'hUpdate'),(1, 'fDiscard'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EndUpdateResourceW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.BOOL, use_last_error=True)(("EndUpdateResourceW", windll["KERNEL32"]), ((1, 'hUpdate'),(1, 'fDiscard'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EndUpdateResource():
    return win32more.System.LibraryLoader.EndUpdateResourceW
def _define_SetDllDirectoryA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR, use_last_error=True)(("SetDllDirectoryA", windll["KERNEL32"]), ((1, 'lpPathName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetDllDirectoryW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR, use_last_error=True)(("SetDllDirectoryW", windll["KERNEL32"]), ((1, 'lpPathName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetDllDirectory():
    return win32more.System.LibraryLoader.SetDllDirectoryW
def _define_GetDllDirectoryA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(Byte), use_last_error=True)(("GetDllDirectoryA", windll["KERNEL32"]), ((1, 'nBufferLength'),(1, 'lpBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDllDirectoryW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(Char), use_last_error=True)(("GetDllDirectoryW", windll["KERNEL32"]), ((1, 'nBufferLength'),(1, 'lpBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDllDirectory():
    return win32more.System.LibraryLoader.GetDllDirectoryW
__all__ = [
    "FIND_RESOURCE_DIRECTORY_TYPES",
    "FIND_RESOURCE_DIRECTORY_NAMES",
    "FIND_RESOURCE_DIRECTORY_LANGUAGES",
    "RESOURCE_ENUM_LN",
    "RESOURCE_ENUM_MUI",
    "RESOURCE_ENUM_MUI_SYSTEM",
    "RESOURCE_ENUM_VALIDATE",
    "RESOURCE_ENUM_MODULE_EXACT",
    "SUPPORT_LANG_NUMBER",
    "GET_MODULE_HANDLE_EX_FLAG_PIN",
    "GET_MODULE_HANDLE_EX_FLAG_UNCHANGED_REFCOUNT",
    "GET_MODULE_HANDLE_EX_FLAG_FROM_ADDRESS",
    "CURRENT_IMPORT_REDIRECTION_VERSION",
    "LOAD_LIBRARY_OS_INTEGRITY_CONTINUITY",
    "LOAD_LIBRARY_FLAGS",
    "DONT_RESOLVE_DLL_REFERENCES",
    "LOAD_LIBRARY_AS_DATAFILE",
    "LOAD_WITH_ALTERED_SEARCH_PATH",
    "LOAD_IGNORE_CODE_AUTHZ_LEVEL",
    "LOAD_LIBRARY_AS_IMAGE_RESOURCE",
    "LOAD_LIBRARY_AS_DATAFILE_EXCLUSIVE",
    "LOAD_LIBRARY_REQUIRE_SIGNED_TARGET",
    "LOAD_LIBRARY_SEARCH_DLL_LOAD_DIR",
    "LOAD_LIBRARY_SEARCH_APPLICATION_DIR",
    "LOAD_LIBRARY_SEARCH_USER_DIRS",
    "LOAD_LIBRARY_SEARCH_SYSTEM32",
    "LOAD_LIBRARY_SEARCH_DEFAULT_DIRS",
    "LOAD_LIBRARY_SAFE_CURRENT_DIRS",
    "LOAD_LIBRARY_SEARCH_SYSTEM32_NO_FORWARDER",
    "ENUMUILANG",
    "ENUMRESLANGPROCA",
    "ENUMRESLANGPROCW",
    "ENUMRESNAMEPROCA",
    "ENUMRESNAMEPROCW",
    "ENUMRESTYPEPROCA",
    "ENUMRESTYPEPROCW",
    "PGET_MODULE_HANDLE_EXA",
    "PGET_MODULE_HANDLE_EXW",
    "REDIRECTION_FUNCTION_DESCRIPTOR",
    "REDIRECTION_DESCRIPTOR",
    "DisableThreadLibraryCalls",
    "FindResourceExW",
    "FindResourceEx",
    "FreeLibrary",
    "FreeLibraryAndExitThread",
    "FreeResource",
    "GetModuleFileNameA",
    "GetModuleFileNameW",
    "GetModuleFileName",
    "GetModuleHandleA",
    "GetModuleHandleW",
    "GetModuleHandle",
    "GetModuleHandleExA",
    "GetModuleHandleExW",
    "GetModuleHandleEx",
    "GetProcAddress",
    "LoadLibraryExA",
    "LoadLibraryExW",
    "LoadLibraryEx",
    "LoadResource",
    "LockResource",
    "SizeofResource",
    "AddDllDirectory",
    "RemoveDllDirectory",
    "SetDefaultDllDirectories",
    "EnumResourceLanguagesExA",
    "EnumResourceLanguagesExW",
    "EnumResourceLanguagesEx",
    "EnumResourceNamesExA",
    "EnumResourceNamesExW",
    "EnumResourceNamesEx",
    "EnumResourceTypesExA",
    "EnumResourceTypesExW",
    "EnumResourceTypesEx",
    "FindResourceW",
    "FindResource",
    "LoadLibraryA",
    "LoadLibraryW",
    "LoadLibrary",
    "EnumResourceNamesW",
    "EnumResourceNames",
    "EnumResourceNamesA",
    "LoadModule",
    "LoadPackagedLibrary",
    "FindResourceA",
    "FindResourceExA",
    "EnumResourceTypesA",
    "EnumResourceTypesW",
    "EnumResourceTypes",
    "EnumResourceLanguagesA",
    "EnumResourceLanguagesW",
    "EnumResourceLanguages",
    "BeginUpdateResourceA",
    "BeginUpdateResourceW",
    "BeginUpdateResource",
    "UpdateResourceA",
    "UpdateResourceW",
    "UpdateResource",
    "EndUpdateResourceA",
    "EndUpdateResourceW",
    "EndUpdateResource",
    "SetDllDirectoryA",
    "SetDllDirectoryW",
    "SetDllDirectory",
    "GetDllDirectoryA",
    "GetDllDirectoryW",
    "GetDllDirectory",
]
