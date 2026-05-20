from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.Wdk.Devices.Bluetooth
import win32more.Windows.Win32.Foundation
GUID_BTHDDI_SDP_NODE_INTERFACE: Guid = Guid('{81a7fdf3-86c1-4be8-a8c8-2a6d188b4177}')
GUID_BTHDDI_SDP_PARSE_INTERFACE: Guid = Guid('{4e719439-9cf1-4bab-ac1d-3279865743d2}')
GUID_BTHDDI_PROFILE_DRIVER_INTERFACE: Guid = Guid('{94a59aa8-4383-4286-aa4f-34a160f40004}')
GUID_BTH_DEVICE_INTERFACE: Guid = Guid('{00f40965-e89d-4487-9890-87c3abb211f4}')
DEVPKEY_Bluetooth_DeviceAddress: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{2bd67d8b-8beb-48d5-87e0-6cda3428040a}'), pid=1)
DEVPKEY_Bluetooth_ServiceGUID: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{2bd67d8b-8beb-48d5-87e0-6cda3428040a}'), pid=2)
DEVPKEY_Bluetooth_DeviceFlags: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{2bd67d8b-8beb-48d5-87e0-6cda3428040a}'), pid=3)
DEVPKEY_Bluetooth_DeviceManufacturer: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{2bd67d8b-8beb-48d5-87e0-6cda3428040a}'), pid=4)
DEVPKEY_Bluetooth_DeviceModelNumber: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{2bd67d8b-8beb-48d5-87e0-6cda3428040a}'), pid=5)
DEVPKEY_Bluetooth_DeviceVIDSource: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{2bd67d8b-8beb-48d5-87e0-6cda3428040a}'), pid=6)
DEVPKEY_Bluetooth_DeviceVID: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{2bd67d8b-8beb-48d5-87e0-6cda3428040a}'), pid=7)
DEVPKEY_Bluetooth_DevicePID: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{2bd67d8b-8beb-48d5-87e0-6cda3428040a}'), pid=8)
DEVPKEY_Bluetooth_DeviceProductVersion: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{2bd67d8b-8beb-48d5-87e0-6cda3428040a}'), pid=9)
DEVPKEY_Bluetooth_ClassOfDevice_Deprecated: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{2bd67d8b-8beb-48d5-87e0-6cda3428040a}'), pid=4)
DEVPKEY_Bluetooth_LastConnectedTime_Deprecated: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{2bd67d8b-8beb-48d5-87e0-6cda3428040a}'), pid=5)
DEVPKEY_Bluetooth_ClassOfDevice: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{2bd67d8b-8beb-48d5-87e0-6cda3428040a}'), pid=10)
DEVPKEY_Bluetooth_LastConnectedTime: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{2bd67d8b-8beb-48d5-87e0-6cda3428040a}'), pid=11)
DEVPKEY_Bluetooth_LastSeenTime: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{2bd67d8b-8beb-48d5-87e0-6cda3428040a}'), pid=12)


make_ready(__name__)
