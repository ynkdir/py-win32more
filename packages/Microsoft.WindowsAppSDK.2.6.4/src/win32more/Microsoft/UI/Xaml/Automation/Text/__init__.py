from __future__ import annotations
from win32more._prelude import *
import win32more.Microsoft.UI.Xaml.Automation.Text
class TextPatternRangeEndpoint(Enum, Int32):
    _name_ = 'Microsoft.UI.Xaml.Automation.Text.TextPatternRangeEndpoint'
    Start = 0
    End = 1
class TextUnit(Enum, Int32):
    _name_ = 'Microsoft.UI.Xaml.Automation.Text.TextUnit'
    Character = 0
    Format = 1
    Word = 2
    Line = 3
    Paragraph = 4
    Page = 5
    Document = 6


make_ready(__name__)
