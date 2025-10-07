from ._win32 import *
from ._winapi import FAILED, SUCCEEDED, CoIncrementMTAUsage, Guid  #noqa: F401

# Initialize COM Multithreaded Apartment.
# Call CoInitializeEx(None, COINIT_APARTMENTTHREADED) explicitly for Single-Threaded Apartment.
if FAILED(CoIncrementMTAUsage(VoidPtr())):
    raise WinError()
