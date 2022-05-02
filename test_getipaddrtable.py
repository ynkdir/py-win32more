from win32more.all import *
import socket
import struct

dwSize = ULONG(0)
if (r := GetIpAddrTable(None, dwSize, False)) != ERROR_INSUFFICIENT_BUFFER:
    raise WinError(r)

IpAddrTable = MIB_IPADDRTABLE()
resize(IpAddrTable, dwSize.value)
if (r := GetIpAddrTable(IpAddrTable, dwSize, False)) != NO_ERROR:
    raise WinError(r)

for row in cast(byref(IpAddrTable.table), POINTER(MIB_IPADDRROW_XP * IpAddrTable.dwNumEntries)).contents:
    print(socket.inet_ntoa(struct.pack("L", row.dwAddr)))
