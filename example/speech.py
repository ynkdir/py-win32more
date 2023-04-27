from contextlib import ExitStack
from ctypes import WinError

from Windows import FAILED
from Windows.Win32.Foundation import PWSTR, S_OK
from Windows.Win32.Media.Speech import (
    SPF_DEFAULT,
    IEnumSpObjectTokens,
    ISpObjectToken,
    ISpObjectTokenCategory,
    ISpVoice,
    SpObjectTokenCategory,
    SpVoice,
)
from Windows.Win32.System.Com import (
    CLSCTX_INPROC_SERVER,
    CoCreateInstance,
    CoInitialize,
    CoTaskMemFree,
    CoUninitialize,
)


def enum_tokens():
    with ExitStack() as defer:
        cat = ISpObjectTokenCategory()
        hr = CoCreateInstance(
            SpObjectTokenCategory,
            None,
            CLSCTX_INPROC_SERVER,
            ISpObjectTokenCategory.Guid,
            cat,
        )
        if FAILED(hr):
            raise WinError(hr)
        defer.callback(cat.Release)

        hr = cat.SetId(
            r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices", False
        )
        if FAILED(hr):
            raise WinError(hr)

        et = IEnumSpObjectTokens()
        hr = cat.EnumTokens(None, None, et)
        if FAILED(hr):
            raise WinError(hr)
        defer.callback(et.Release)

        while True:
            with ExitStack() as defer2:
                tok = ISpObjectToken()
                hr = et.Next(1, tok, None)
                if FAILED(hr):
                    raise WinError(hr)
                if hr != S_OK:
                    break
                defer2.callback(tok.Release)

                s = PWSTR()
                hr = tok.GetId(s)
                if FAILED(hr):
                    raise WinError(hr)
                defer2.callback(CoTaskMemFree, s)

                yield s.value


def speak(msg):
    with ExitStack() as defer:
        sapi = ISpVoice()
        hr = CoCreateInstance(SpVoice, None, CLSCTX_INPROC_SERVER, ISpVoice.Guid, sapi)
        if FAILED(hr):
            raise WinError(hr)
        defer.callback(sapi.Release)

        hr = sapi.Speak(msg, SPF_DEFAULT, None)
        if FAILED(hr):
            raise WinError(hr)


def main():
    with ExitStack() as defer:
        hr = CoInitialize(None)
        if FAILED(hr):
            raise WinError(hr)
        defer.callback(CoUninitialize)

        for s in enum_tokens():
            print(s)
        speak("hello, world")


if __name__ == "__main__":
    main()
