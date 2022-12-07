from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.System.MixedReality
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
PERCEPTIONFIELD_StateStream_TimeStamps: Guid = Guid('aa886119-f32f-49bf-92-ca-f9-dd-f7-84-d2-97')
class PERCEPTION_PAYLOAD_FIELD(Structure):
    FieldId: Guid
    OffsetInBytes: UInt32
    SizeInBytes: UInt32
class PERCEPTION_STATE_STREAM_TIMESTAMPS(Structure):
    InputTimestampInQpcCounts: Int64
    AvailableTimestampInQpcCounts: Int64
make_head(_module, 'PERCEPTION_PAYLOAD_FIELD')
make_head(_module, 'PERCEPTION_STATE_STREAM_TIMESTAMPS')
__all__ = [
    "PERCEPTIONFIELD_StateStream_TimeStamps",
    "PERCEPTION_PAYLOAD_FIELD",
    "PERCEPTION_STATE_STREAM_TIMESTAMPS",
]
