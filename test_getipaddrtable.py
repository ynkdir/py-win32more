from win32more import *
from win32more.Foundation import ERROR_INSUFFICIENT_BUFFER, NO_ERROR
from win32more.NetworkManagement.IpHelper import GetIpAddrTable, MIB_IPADDRTABLE, MIB_IPADDRROW_XP
import socket

dwSize = ULONG(0)
if (r := GetIpAddrTable(None, dwSize, False)) != ERROR_INSUFFICIENT_BUFFER:
    raise WinError(r)

IpAddrTable = MIB_IPADDRTABLE()
resize(IpAddrTable, dwSize.value)
if (r := GetIpAddrTable(IpAddrTable, dwSize, False)) != NO_ERROR:
    raise WinError(r)

for row in cast(byref(IpAddrTable.table), POINTER(MIB_IPADDRROW_XP * IpAddrTable.dwNumEntries)).contents:
    print(socket.inet_ntoa(row.dwAddr.to_bytes(4, "big")))
