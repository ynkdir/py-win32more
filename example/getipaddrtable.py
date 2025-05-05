import socket

from win32more import UInt32, WinError
from win32more.Windows.Win32.Foundation import ERROR_INSUFFICIENT_BUFFER, NO_ERROR
from win32more.Windows.Win32.NetworkManagement.IpHelper import MIB_IPADDRTABLE, GetIpAddrTable

dwSize = UInt32(0)
if (r := GetIpAddrTable(None, dwSize, False)) != ERROR_INSUFFICIENT_BUFFER:
    raise WinError(r)

buffer = bytearray(dwSize.value)

IpAddrTable = MIB_IPADDRTABLE.from_buffer(buffer)
if (r := GetIpAddrTable(IpAddrTable, dwSize, False)) != NO_ERROR:
    raise WinError(r)

# IpAddrTable.table is flexible array member.
for row in IpAddrTable.table[: IpAddrTable.dwNumEntries]:
    print(socket.inet_ntoa(row.dwAddr.to_bytes(4, "little")))
