from __future__ import annotations
from win32more._prelude import *
import win32more.Microsoft.Windows.Vision
class ScreenRegionBoundingBox(Structure):
    _name_ = 'Microsoft.Windows.Vision.ScreenRegionBoundingBox'
    Left: UInt32
    Top: UInt32
    Right: UInt32
    Bottom: UInt32
ScreenRegionDetectionContract: UInt32 = 65536
class ScreenRegionLabel(Enum, Int32):
    _name_ = 'Microsoft.Windows.Vision.ScreenRegionLabel'
    Text = 0
    Image = 1
    Table = 2
    Container = 3
    Menu = 4
    ToolBar = 5
    AddressBar = 6
    Toolpane = 7
    TabBar = 8
    TitleBar = 9


make_ready(__name__)
