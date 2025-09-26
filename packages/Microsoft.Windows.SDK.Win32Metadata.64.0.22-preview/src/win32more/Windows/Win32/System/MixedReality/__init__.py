from __future__ import annotations
from win32more.win32.prelude import *
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
