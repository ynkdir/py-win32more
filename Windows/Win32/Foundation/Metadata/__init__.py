from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation.Metadata
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AgileAttribute(EasyCastStructure):
    pass
class AlsoUsableForAttribute(EasyCastStructure):
    otherType: String
Architecture = Int32
Architecture_None: Architecture = 0
Architecture_X86: Architecture = 1
Architecture_X64: Architecture = 2
Architecture_Arm64: Architecture = 4
Architecture_All: Architecture = 7
class CanReturnErrorsAsSuccessAttribute(EasyCastStructure):
    pass
class CanReturnMultipleSuccessValuesAttribute(EasyCastStructure):
    pass
class ComOutPtrAttribute(EasyCastStructure):
    pass
class ConstAttribute(EasyCastStructure):
    pass
class ConstantAttribute(EasyCastStructure):
    Value: String
class CppAttributeList(EasyCastStructure):
    AttributeList: String
class DoNotReleaseAttribute(EasyCastStructure):
    pass
class FlexibleArrayAttribute(EasyCastStructure):
    pass
class FreeWithAttribute(EasyCastStructure):
    Name: String
class GuidAttribute(EasyCastStructure):
    a: UInt32
    b: UInt16
    c: UInt16
    d: Byte
    e: Byte
    f: Byte
    g: Byte
    h: Byte
    i: Byte
    j: Byte
    k: Byte
class IgnoreIfReturnAttribute(EasyCastStructure):
    Value: String
class InvalidHandleValueAttribute(EasyCastStructure):
    Value: Int64
class MemorySizeAttribute(EasyCastStructure):
    pass
class MetadataTypedefAttribute(EasyCastStructure):
    pass
class NativeArrayInfoAttribute(EasyCastStructure):
    pass
class NativeEncodingAttribute(EasyCastStructure):
    Name: String
class NativeInheritanceAttribute(EasyCastStructure):
    BaseName: String
class NativeTypeNameAttribute(EasyCastStructure):
    Name: String
class NativeTypedefAttribute(EasyCastStructure):
    pass
class NotNullTerminatedAttribute(EasyCastStructure):
    pass
class NullNullTerminatedAttribute(EasyCastStructure):
    pass
class RAIIFreeAttribute(EasyCastStructure):
    Name: String
class ReservedAttribute(EasyCastStructure):
    pass
class RetValAttribute(EasyCastStructure):
    pass
class ReturnsUnownedHandle(EasyCastStructure):
    pass
class ScopedEnumAttribute(EasyCastStructure):
    pass
class StaticLibraryAttribute(EasyCastStructure):
    LibName: String
class StructSizeFieldAttribute(EasyCastStructure):
    field: String
class SupportedArchitectureAttribute(EasyCastStructure):
    arch: Windows.Win32.Foundation.Metadata.Architecture
class SupportedOSPlatformAttribute(EasyCastStructure):
    platform: String
