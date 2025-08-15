from __future__ import annotations
from win32more.win32.prelude import *
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Diagnostics.Ceip
@winfunctype('KERNEL32.dll')
def CeipIsOptedIn() -> win32more.Windows.Win32.Foundation.BOOL: ...


make_ready(__name__)
