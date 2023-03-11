from contextlib import contextmanager
from ctypes import WinError
from Windows.all import (FAILED, PWSTR,
    S_OK, CLSCTX_INPROC_SERVER, SPF_DEFAULT, SpVoice, SpObjectTokenCategory,
    CoInitialize, CoUninitialize, CoCreateInstance, CoTaskMemFree,
    ISpObjectToken, ISpObjectTokenCategory, IEnumSpObjectTokens, ISpVoice)

@contextmanager
def ComPtr(ptr):
    try:
        yield ptr
    finally:
        ptr.Release()

# useful for default?
def errcheck(hr, func, args):
    if FAILED(hr):
        raise WinError(hr)
    return hr, *args

CoCreateInstance.errcheck = errcheck
ISpObjectTokenCategory.EnumTokens.errcheck = errcheck
IEnumSpObjectTokens.Next.errcheck = errcheck
ISpObjectToken.GetId.errcheck = errcheck
ISpVoice.Speak.errcheck = errcheck

def enum_tokens():
    cat = ISpObjectTokenCategory()
    CoCreateInstance(SpObjectTokenCategory, None, CLSCTX_INPROC_SERVER, ISpObjectTokenCategory.Guid, cat)
    with ComPtr(cat):
        cat.SetId(r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices", False)
        et = IEnumSpObjectTokens()
        cat.EnumTokens(None, None, et)
        with ComPtr(et):
            tok = ISpObjectToken()
            while et.Next(1, tok, None) == S_OK:
                with ComPtr(tok):
                    s = PWSTR()
                    tok.GetId(s)
                    yield s.value
                    CoTaskMemFree(s)

def speak(msg):
    sapi = ISpVoice()
    CoCreateInstance(SpVoice, None, CLSCTX_INPROC_SERVER, ISpVoice.Guid, sapi)
    with ComPtr(sapi):
        sapi.Speak(msg, SPF_DEFAULT, None)

def main():
    CoInitialize(None)
    for s in enum_tokens():
        print(s)
    speak("hello, world")
    CoUninitialize()

if __name__ == "__main__":
    main()
