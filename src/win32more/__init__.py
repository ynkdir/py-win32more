from .win32 import *

# Force import order "winrt -> Windows.Foundation" to avoid circular import problem.
import win32more.winrt
