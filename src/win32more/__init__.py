from .win32 import *

# Initialize COM Multithreaded Apartment.
# Call CoInitializeEx(None, COINIT_APARTMENTTHREADED) explicitly for Single-Threaded Apartment.
cookie = VoidPtr()
hr = windll["ole32.dll"].CoIncrementMTAUsage(pointer(cookie))
if FAILED(hr):
    raise WinError(hr)
del hr
del cookie
