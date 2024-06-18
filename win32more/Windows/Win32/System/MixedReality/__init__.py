from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.System.MixedReality
PERCEPTIONFIELD_StateStream_TimeStamps: Guid = Guid('{aa886119-f32f-49bf-92ca-f9ddf784d297}')
class PERCEPTION_PAYLOAD_FIELD(Structure):
    FieldId: Guid
    OffsetInBytes: UInt32
    SizeInBytes: UInt32
class PERCEPTION_STATE_STREAM_TIMESTAMPS(Structure):
    InputTimestampInQpcCounts: Int64
    AvailableTimestampInQpcCounts: Int64


make_ready(__name__)
