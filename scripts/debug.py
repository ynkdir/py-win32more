# debugger to print WindowsAppSDK's debug output in console.
# py debug.py example\winui-xaml.py

import argparse
import os
import runpy
from contextlib import contextmanager
from ctypes import c_char
from multiprocessing import Event, Process, Queue

from win32more import Char, UInt32, UIntPtr, WinError
from win32more.Windows.Win32.Foundation import DBG_CONTINUE, DBG_EXCEPTION_NOT_HANDLED, ERROR_SEM_TIMEOUT, GetLastError
from win32more.Windows.Win32.System.Diagnostics.Debug import (
    DEBUG_EVENT,
    EXCEPTION_DEBUG_EVENT,
    OUTPUT_DEBUG_STRING_EVENT,
    ContinueDebugEvent,
    DebugActiveProcess,
    DebugActiveProcessStop,
    ReadProcessMemory,
    WaitForDebugEventEx,
)
from win32more.Windows.Win32.System.Threading import (
    PROCESS_VM_READ,
    GetExitCodeProcess,
    OpenProcess,
)


def debugger(queue, close_event, pid):
    r = DebugActiveProcess(pid)
    if r == 0:
        raise WinError()

    hprocess = OpenProcess(PROCESS_VM_READ, False, pid)
    if hprocess == 0:
        raise WinError()

    print(f"debugger attached: {pid}")

    queue.put(True)

    while True:
        if close_event.is_set():
            r = DebugActiveProcessStop(pid)
            if r == 0:
                raise WinError()
            return

        if GetExitCodeProcess(pid, UInt32()) != 0:
            return

        ev = DEBUG_EVENT()
        r = WaitForDebugEventEx(ev, 1000)
        if r == 0:
            if GetLastError() != ERROR_SEM_TIMEOUT:
                raise WinError()
            continue

        if ev.dwDebugEventCode == EXCEPTION_DEBUG_EVENT:
            r = ContinueDebugEvent(ev.dwProcessId, ev.dwThreadId, DBG_EXCEPTION_NOT_HANDLED)
            if r == 0:
                raise WinError()
        elif ev.dwDebugEventCode == OUTPUT_DEBUG_STRING_EVENT:
            if ev.u.DebugString.fUnicode == 0:
                numread = UIntPtr()
                buflen = ev.u.DebugString.nDebugStringLength + 1
                buf = (c_char * buflen)()
                r = ReadProcessMemory(hprocess, ev.u.DebugString.lpDebugStringData_as_intptr, buf, buflen, numread)
                if r == 0:
                    raise WinError()
                print(buf.value)
            else:
                numread = UIntPtr()
                buflen = ev.u.DebugString.nDebugStringLength + 1
                buf = (Char * buflen)()
                r = ReadProcessMemory(hprocess, ev.u.DebugString.lpDebugStringData_as_intptr, buf, buflen * 2, numread)
                if r == 0:
                    raise WinError()
                print(buf.value)
            r = ContinueDebugEvent(ev.dwProcessId, ev.dwThreadId, DBG_CONTINUE)
            if r == 0:
                raise WinError()
        else:
            r = ContinueDebugEvent(ev.dwProcessId, ev.dwThreadId, DBG_CONTINUE)
            if r == 0:
                raise WinError()


@contextmanager
def start_debugger():
    try:
        close_event = Event()
        queue = Queue()
        process = Process(target=debugger, args=(queue, close_event, os.getpid()))
        process.start()
        queue.get()
        yield process
    finally:
        close_event.set()
        process.join()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    with start_debugger():
        runpy.run_path(args.path, run_name="__main__")


if __name__ == "__main__":
    main()
