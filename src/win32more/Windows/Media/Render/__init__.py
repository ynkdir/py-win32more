from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.Media.Render
class AudioRenderCategory(Enum, Int32):
    Other = 0
    ForegroundOnlyMedia = 1
    BackgroundCapableMedia = 2
    Communications = 3
    Alerts = 4
    SoundEffects = 5
    GameEffects = 6
    GameMedia = 7
    GameChat = 8
    Speech = 9
    Movie = 10
    Media = 11


make_ready(__name__)
