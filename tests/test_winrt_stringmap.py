from contextlib import ExitStack
from ctypes import WinError

from Windows import FAILED
from Windows.Foundation.Collections import StringMap
from Windows.Win32.System.WinRT import (
    RO_INIT_SINGLETHREADED,
    RoInitialize,
    RoUninitialize,
)


def main() -> None:
    with ExitStack() as defer:
        hr = RoInitialize(RO_INIT_SINGLETHREADED)
        if FAILED(hr):
            raise WinError(hr)
        defer.callback(RoUninitialize)

        x = StringMap.New()
        defer.callback(x.Release)

        x.Insert("key1", "value1")
        x.Insert("key2", "value2")
        print("key1 =", x.Lookup("key1"))
        print("key2 =", x.Lookup("key2"))


if __name__ == "__main__":
    main()
