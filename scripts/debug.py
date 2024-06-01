# debugger to print WindowsAppSDK's debug output in console.
# py debug.py example\winui-xaml.py
#
# To debug with Visal Studio (not work with venv or py launcher which fork process).
# devenv.exe /debugexe /path/to/python.exe /path/to/script.py

import argparse
import os
import runpy
from contextlib import contextmanager
from ctypes import addressof, c_char, c_wchar_p, pointer, resize, sizeof
from multiprocessing import Event, Process, Queue

from win32more import UInt32, UIntPtr, WinError
from win32more.Windows.Win32.Foundation import DBG_EXCEPTION_NOT_HANDLED, ERROR_SEM_TIMEOUT, CloseHandle, GetLastError
from win32more.Windows.Win32.Storage.FileSystem import FILE_NAME_INFO, FileNameInfo, GetFileInformationByHandleEx
from win32more.Windows.Win32.System.Diagnostics.Debug import (
    DEBUG_EVENT,
    EXCEPTION_DEBUG_EVENT,
    LOAD_DLL_DEBUG_EVENT,
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

WINRT_ORIGINATE_ERROR = 1074266625


def _ReadProcessMemory(hprocess, address, size):
    numread = UIntPtr()
    buf = (c_char * size)()
    r = ReadProcessMemory(hprocess, address, buf, size, numread)
    if r == 0:
        raise WinError()
    return buf[:]


def _get_file_name_by_handle(hfile):
    buf = FILE_NAME_INFO()
    resize(buf, 1024)
    r = GetFileInformationByHandleEx(hfile, FileNameInfo, pointer(buf), sizeof(buf))
    if r == 0:
        raise WinError()
    return c_wchar_p(addressof(buf) + FILE_NAME_INFO.FileName.offset).value


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
            record = ev.u.Exception.ExceptionRecord
            if record.ExceptionCode == WINRT_ORIGINATE_ERROR:
                buf = _ReadProcessMemory(hprocess, record.ExceptionInformation[2], record.ExceptionInformation[1] * 2)
                msg = buf.decode("utf-16le")
                print(f"WinRT originate error - 0x{record.ExceptionInformation[0]:08X} : '{msg}'")
            else:
                print("ExceptionCode:", ev.u.Exception.ExceptionRecord.ExceptionCode)
                print("ExceptionFlags:", ev.u.Exception.ExceptionRecord.ExceptionFlags)
                print("ExceptionRecord:", ev.u.Exception.ExceptionRecord.ExceptionRecord)
                print("ExceptionAddress:", ev.u.Exception.ExceptionRecord.ExceptionAddress)
                print("NumberParameters:", ev.u.Exception.ExceptionRecord.NumberParameters)
                print("ExceptionInformation:", ev.u.Exception.ExceptionRecord.ExceptionInformation)
                for i in range(ev.u.Exception.ExceptionRecord.NumberParameters):
                    print(f"ExceptionInformation[{i}]:", ev.u.Exception.ExceptionRecord.ExceptionInformation[i])
        elif ev.dwDebugEventCode == OUTPUT_DEBUG_STRING_EVENT:
            buf = _ReadProcessMemory(
                hprocess, ev.u.DebugString.lpDebugStringData_as_intptr, ev.u.DebugString.nDebugStringLength
            )
            if ev.u.DebugString.fUnicode == 0:
                # print(buf.rstrip(b"\r\n\x00"))
                pass
            else:
                print(buf.decode("utf-16le").rstrip("\r\n\x00"))
        elif ev.dwDebugEventCode == LOAD_DLL_DEBUG_EVENT:
            if ev.u.LoadDll.hFile != 0:
                dllname = _get_file_name_by_handle(ev.u.LoadDll.hFile)
                print(f"{dllname} loaded")
                CloseHandle(ev.u.LoadDll.hFile)

        r = ContinueDebugEvent(ev.dwProcessId, ev.dwThreadId, DBG_EXCEPTION_NOT_HANDLED)
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
