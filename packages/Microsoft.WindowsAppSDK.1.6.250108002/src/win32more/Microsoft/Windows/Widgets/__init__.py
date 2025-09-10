from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Microsoft.Windows.Widgets
WidgetContract: UInt32 = 458752
class WidgetSize(Enum, Int32):
    Small = 0
    Medium = 1
    Large = 2


make_ready(__name__)
