from win32more.all import *
import socket
import struct

dwSize = ULONG(0)
if GetIpAddrTable(None, byref(dwSize), False) != WIN32_ERROR_ERROR_INSUFFICIENT_BUFFER:
    raise RuntimeError("GetIpAddrTable")

IpAddrTable = MIB_IPADDRTABLE()
resize(IpAddrTable, dwSize.value)
if GetIpAddrTable(byref(IpAddrTable), byref(dwSize), False) != WIN32_ERROR_NO_ERROR:
    raise RuntimeError("GetIpAddrTable")

for row in cast(byref(IpAddrTable.table), POINTER(MIB_IPADDRROW_XP * IpAddrTable.dwNumEntries)).contents:
    print(socket.inet_ntoa(struct.pack("L", row.dwAddr)))
