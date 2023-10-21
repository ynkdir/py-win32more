from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation.Metadata
class AgileAttribute(EasyCastStructure):
    pass
class AlsoUsableForAttribute(EasyCastStructure):
    otherType: String
class AnsiAttribute(EasyCastStructure):
    pass
Architecture = Int32
Architecture_None: win32more.Windows.Win32.Foundation.Metadata.Architecture = 0
Architecture_X86: win32more.Windows.Win32.Foundation.Metadata.Architecture = 1
Architecture_X64: win32more.Windows.Win32.Foundation.Metadata.Architecture = 2
Architecture_Arm64: win32more.Windows.Win32.Foundation.Metadata.Architecture = 4
Architecture_All: win32more.Windows.Win32.Foundation.Metadata.Architecture = 7
class AssociatedConstantAttribute(EasyCastStructure):
    Name: String
class AssociatedEnumAttribute(EasyCastStructure):
    Name: String
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
class DocumentationAttribute(EasyCastStructure):
    Uri: String
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
class NativeBitfieldAttribute(EasyCastStructure):
    name: String
    offset: Int64
    length: Int64
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
class ScopedEnumAttribute(EasyCastStructure):
    pass
class StaticLibraryAttribute(EasyCastStructure):
    LibName: String
class StructSizeFieldAttribute(EasyCastStructure):
    field: String
class SupportedArchitectureAttribute(EasyCastStructure):
    arch: win32more.Windows.Win32.Foundation.Metadata.Architecture
class SupportedOSPlatformAttribute(EasyCastStructure):
    platform: String
class UnicodeAttribute(EasyCastStructure):
    pass


make_ready(__name__)
