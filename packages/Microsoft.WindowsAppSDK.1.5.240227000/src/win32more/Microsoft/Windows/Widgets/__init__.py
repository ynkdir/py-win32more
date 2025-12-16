from __future__ import annotations
from win32more._prelude import *
import win32more.Microsoft.Windows.Widgets
WidgetContract: UInt32 = 262144
class WidgetSize(Enum, Int32):
    _name_ = 'Microsoft.Windows.Widgets.WidgetSize'
    Small = 0
    Medium = 1
    Large = 2


make_ready(__name__)
