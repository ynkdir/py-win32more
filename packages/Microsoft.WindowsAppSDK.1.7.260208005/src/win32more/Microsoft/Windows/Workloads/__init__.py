from __future__ import annotations
from win32more._prelude import *
import win32more.Microsoft.Windows.Workloads
class WorkloadPriority(Enum, Int32):
    _name_ = 'Microsoft.Windows.Workloads.WorkloadPriority'
    Undefined = 0
    Background = 1
    Foreground = 9
WorkloadsContract: UInt32 = 524288


make_ready(__name__)
