from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.ApplicationModel.DataTransfer.DragDrop
class DragDropModifiers(Enum, UInt32):
    None_ = 0
    Shift = 1
    Control = 2
    Alt = 4
    LeftButton = 8
    MiddleButton = 16
    RightButton = 32


make_ready(__name__)
