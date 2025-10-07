# ruff: noqa: F401, F403, F405
from ._win32 import *
from ._win32api import FAILED, SUCCEEDED, CoIncrementMTAUsage, Guid

# Initialize COM Multithreaded Apartment.
# Call CoInitializeEx(None, COINIT_APARTMENTTHREADED) explicitly for Single-Threaded Apartment.
if FAILED(CoIncrementMTAUsage(VoidPtr())):
    raise WinError()
