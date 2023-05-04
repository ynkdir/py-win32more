from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.System.MixedReality
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
PERCEPTIONFIELD_StateStream_TimeStamps: Guid = Guid('{aa886119-f32f-49bf-92ca-f9ddf784d297}')
class PERCEPTION_PAYLOAD_FIELD(EasyCastStructure):
    FieldId: Guid
    OffsetInBytes: UInt32
    SizeInBytes: UInt32
class PERCEPTION_STATE_STREAM_TIMESTAMPS(EasyCastStructure):
    InputTimestampInQpcCounts: Int64
    AvailableTimestampInQpcCounts: Int64
make_head(_module, 'PERCEPTION_PAYLOAD_FIELD')
make_head(_module, 'PERCEPTION_STATE_STREAM_TIMESTAMPS')
