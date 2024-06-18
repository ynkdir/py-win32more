from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation.Metadata
class AgileAttribute(Structure):
    pass
class AlsoUsableForAttribute(Structure):
    otherType: String
class AnsiAttribute(Structure):
    pass
Architecture = Int32
None_: win32more.Windows.Win32.Foundation.Metadata.Architecture = 0
X86: win32more.Windows.Win32.Foundation.Metadata.Architecture = 1
X64: win32more.Windows.Win32.Foundation.Metadata.Architecture = 2
Arm64: win32more.Windows.Win32.Foundation.Metadata.Architecture = 4
All: win32more.Windows.Win32.Foundation.Metadata.Architecture = 7
class AssociatedConstantAttribute(Structure):
    Name: String
class AssociatedEnumAttribute(Structure):
    Name: String
class CanReturnErrorsAsSuccessAttribute(Structure):
    pass
class CanReturnMultipleSuccessValuesAttribute(Structure):
    pass
class ComOutPtrAttribute(Structure):
    pass
class ConstAttribute(Structure):
    pass
class ConstantAttribute(Structure):
    Value: String
class CppAttributeList(Structure):
    AttributeList: String
class DoNotReleaseAttribute(Structure):
    pass
class DocumentationAttribute(Structure):
    Uri: String
class FlexibleArrayAttribute(Structure):
    pass
class FreeWithAttribute(Structure):
    Name: String
class GuidAttribute(Structure):
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
class IgnoreIfReturnAttribute(Structure):
    Value: String
class InvalidHandleValueAttribute(Structure):
    Value: Int64
class MemorySizeAttribute(Structure):
    pass
class MetadataTypedefAttribute(Structure):
    pass
class NativeArrayInfoAttribute(Structure):
    pass
class NativeBitfieldAttribute(Structure):
    name: String
    offset: Int64
    length: Int64
class NativeEncodingAttribute(Structure):
    Name: String
class NativeInheritanceAttribute(Structure):
    BaseName: String
class NativeTypeNameAttribute(Structure):
    Name: String
class NativeTypedefAttribute(Structure):
    pass
class NotNullTerminatedAttribute(Structure):
    pass
class NullNullTerminatedAttribute(Structure):
    pass
class RAIIFreeAttribute(Structure):
    Name: String
class ReservedAttribute(Structure):
    pass
class RetValAttribute(Structure):
    pass
class RetainedAttribute(Structure):
    pass
class ScopedEnumAttribute(Structure):
    pass
class StaticLibraryAttribute(Structure):
    LibName: String
class StructSizeFieldAttribute(Structure):
    field: String
class SupportedArchitectureAttribute(Structure):
    arch: win32more.Windows.Win32.Foundation.Metadata.Architecture
class SupportedOSPlatformAttribute(Structure):
    platform: String
class UnicodeAttribute(Structure):
    pass


make_ready(__name__)
