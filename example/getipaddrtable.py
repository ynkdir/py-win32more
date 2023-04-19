import socket
from ctypes import POINTER, WinError, byref, cast, resize
from ctypes.wintypes import ULONG

from Windows.Win32.Foundation import ERROR_INSUFFICIENT_BUFFER, NO_ERROR
from Windows.Win32.NetworkManagement.IpHelper import (MIB_IPADDRROW_XP,
                                                      MIB_IPADDRTABLE,
                                                      GetIpAddrTable)

dwSize = ULONG(0)
if (r := GetIpAddrTable(None, dwSize, False)) != ERROR_INSUFFICIENT_BUFFER:
    raise WinError(r)

IpAddrTable = MIB_IPADDRTABLE()
resize(IpAddrTable, dwSize.value)
if (r := GetIpAddrTable(IpAddrTable, dwSize, False)) != NO_ERROR:
    raise WinError(r)

for row in cast(byref(IpAddrTable.table), POINTER(MIB_IPADDRROW_XP * IpAddrTable.dwNumEntries)).contents:
    print(socket.inet_ntoa(row.dwAddr.to_bytes(4, "little")))
