import Windows.all as win32
from ctypes import cast, byref, resize, POINTER
from ctypes.wintypes import ULONG
import socket

dwSize = ULONG(0)
if (r := win32.GetIpAddrTable(None, dwSize, False)) != win32.ERROR_INSUFFICIENT_BUFFER:
    raise win32.WinError(r)

IpAddrTable = win32.MIB_IPADDRTABLE()
resize(IpAddrTable, dwSize.value)
if (r := win32.GetIpAddrTable(IpAddrTable, dwSize, False)) != win32.NO_ERROR:
    raise win32.WinError(r)

for row in cast(byref(IpAddrTable.table), POINTER(win32.MIB_IPADDRROW_XP * IpAddrTable.dwNumEntries)).contents:
    print(socket.inet_ntoa(row.dwAddr.to_bytes(4, "big")))
