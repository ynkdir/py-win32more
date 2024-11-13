from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Devices.PortableDevices
import win32more.Windows.Win32.Devices.Properties
import win32more.Windows.Win32.Devices.Sensors
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.StructuredStorage
ACTIVITY_STATE = Int32
ActivityState_Unknown: win32more.Windows.Win32.Devices.Sensors.ACTIVITY_STATE = 1
ActivityState_Stationary: win32more.Windows.Win32.Devices.Sensors.ACTIVITY_STATE = 2
ActivityState_Fidgeting: win32more.Windows.Win32.Devices.Sensors.ACTIVITY_STATE = 4
ActivityState_Walking: win32more.Windows.Win32.Devices.Sensors.ACTIVITY_STATE = 8
ActivityState_Running: win32more.Windows.Win32.Devices.Sensors.ACTIVITY_STATE = 16
ActivityState_InVehicle: win32more.Windows.Win32.Devices.Sensors.ACTIVITY_STATE = 32
ActivityState_Biking: win32more.Windows.Win32.Devices.Sensors.ACTIVITY_STATE = 64
ActivityState_Idle: win32more.Windows.Win32.Devices.Sensors.ACTIVITY_STATE = 128
ActivityState_Max: win32more.Windows.Win32.Devices.Sensors.ACTIVITY_STATE = 256
ActivityState_Force_Dword: win32more.Windows.Win32.Devices.Sensors.ACTIVITY_STATE = -1
ACTIVITY_STATE_COUNT = Int32
ActivityStateCount: win32more.Windows.Win32.Devices.Sensors.ACTIVITY_STATE_COUNT = 8
AXIS = Int32
AXIS_X: win32more.Windows.Win32.Devices.Sensors.AXIS = 0
AXIS_Y: win32more.Windows.Win32.Devices.Sensors.AXIS = 1
AXIS_Z: win32more.Windows.Win32.Devices.Sensors.AXIS = 2
AXIS_MAX: win32more.Windows.Win32.Devices.Sensors.AXIS = 3
GUID_DEVINTERFACE_SENSOR: Guid = Guid('{ba1bb692-9b7a-4833-9a1e-525ed134e7e2}')
SENSOR_EVENT_STATE_CHANGED: Guid = Guid('{bfd96016-6bd7-4560-ad34-f2f6607e8f81}')
SENSOR_EVENT_DATA_UPDATED: Guid = Guid('{2ed0f2a4-0087-41d3-87db-6773370b3c88}')
SENSOR_EVENT_PROPERTY_CHANGED: Guid = Guid('{2358f099-84c9-4d3d-90df-c2421e2b2045}')
SENSOR_EVENT_ACCELEROMETER_SHAKE: Guid = Guid('{825f5a94-0f48-4396-9ca0-6ecb5c99d915}')
SENSOR_EVENT_PARAMETER_COMMON_GUID: Guid = Guid('{64346e30-8728-4b34-bdf6-4f52442c5c28}')
SENSOR_EVENT_PARAMETER_EVENT_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{64346e30-8728-4b34-bdf6-4f52442c5c28}'), pid=2)
SENSOR_EVENT_PARAMETER_STATE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{64346e30-8728-4b34-bdf6-4f52442c5c28}'), pid=3)
SENSOR_ERROR_PARAMETER_COMMON_GUID: Guid = Guid('{77112bcd-fce1-4f43-b8b8-a88256adb4b3}')
SENSOR_PROPERTY_COMMON_GUID: Guid = Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}')
SENSOR_PROPERTY_TYPE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=2)
SENSOR_PROPERTY_STATE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=3)
SENSOR_PROPERTY_PERSISTENT_UNIQUE_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=5)
SENSOR_PROPERTY_MANUFACTURER: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=6)
SENSOR_PROPERTY_MODEL: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=7)
SENSOR_PROPERTY_SERIAL_NUMBER: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=8)
SENSOR_PROPERTY_FRIENDLY_NAME: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=9)
SENSOR_PROPERTY_DESCRIPTION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=10)
SENSOR_PROPERTY_CONNECTION_TYPE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=11)
SENSOR_PROPERTY_MIN_REPORT_INTERVAL: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=12)
SENSOR_PROPERTY_CURRENT_REPORT_INTERVAL: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=13)
SENSOR_PROPERTY_CHANGE_SENSITIVITY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=14)
SENSOR_PROPERTY_DEVICE_PATH: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=15)
SENSOR_PROPERTY_LIGHT_RESPONSE_CURVE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=16)
SENSOR_PROPERTY_ACCURACY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=17)
SENSOR_PROPERTY_RESOLUTION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=18)
SENSOR_PROPERTY_LOCATION_DESIRED_ACCURACY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=19)
SENSOR_PROPERTY_RANGE_MINIMUM: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=20)
SENSOR_PROPERTY_RANGE_MAXIMUM: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=21)
SENSOR_PROPERTY_HID_USAGE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=22)
SENSOR_PROPERTY_RADIO_STATE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=23)
SENSOR_PROPERTY_RADIO_STATE_PREVIOUS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=24)
SENSOR_CATEGORY_ALL: Guid = Guid('{c317c286-c468-4288-9975-d4c4587c442c}')
SENSOR_CATEGORY_LOCATION: Guid = Guid('{bfa794e4-f964-4fdb-90f6-51056bfe4b44}')
SENSOR_CATEGORY_ENVIRONMENTAL: Guid = Guid('{323439aa-7f66-492b-ba0c-73e9aa0a65d5}')
SENSOR_CATEGORY_MOTION: Guid = Guid('{cd09daf1-3b2e-4c3d-b598-b5e5ff93fd46}')
SENSOR_CATEGORY_ORIENTATION: Guid = Guid('{9e6c04b6-96fe-4954-b726-68682a473f69}')
SENSOR_CATEGORY_MECHANICAL: Guid = Guid('{8d131d68-8ef7-4656-80b5-cccbd93791c5}')
SENSOR_CATEGORY_ELECTRICAL: Guid = Guid('{fb73fcd8-fc4a-483c-ac58-27b691c6beff}')
SENSOR_CATEGORY_BIOMETRIC: Guid = Guid('{ca19690f-a2c7-477d-a99e-99ec6e2b5648}')
SENSOR_CATEGORY_LIGHT: Guid = Guid('{17a665c0-9063-4216-b202-5c7a255e18ce}')
SENSOR_CATEGORY_SCANNER: Guid = Guid('{b000e77e-f5b5-420f-815d-0270a726f270}')
SENSOR_CATEGORY_OTHER: Guid = Guid('{2c90e7a9-f4c9-4fa2-af37-56d471fe5a3d}')
SENSOR_CATEGORY_UNSUPPORTED: Guid = Guid('{2beae7fa-19b0-48c5-a1f6-b5480dc206b0}')
SENSOR_TYPE_LOCATION_GPS: Guid = Guid('{ed4ca589-327a-4ff9-a560-91da4b48275e}')
SENSOR_TYPE_LOCATION_STATIC: Guid = Guid('{095f8184-0fa9-4445-8e6e-b70f320b6b4c}')
SENSOR_TYPE_LOCATION_LOOKUP: Guid = Guid('{3b2eae4a-72ce-436d-96d2-3c5b8570e987}')
SENSOR_TYPE_LOCATION_TRIANGULATION: Guid = Guid('{691c341a-5406-4fe1-942f-2246cbeb39e0}')
SENSOR_TYPE_LOCATION_OTHER: Guid = Guid('{9b2d0566-0368-4f71-b88d-533f132031de}')
SENSOR_TYPE_LOCATION_BROADCAST: Guid = Guid('{d26988cf-5162-4039-bb17-4c58b698e44a}')
SENSOR_TYPE_LOCATION_DEAD_RECKONING: Guid = Guid('{1a37d538-f28b-42da-9fce-a9d0a2a6d829}')
SENSOR_TYPE_ENVIRONMENTAL_TEMPERATURE: Guid = Guid('{04fd0ec4-d5da-45fa-95a9-5db38ee19306}')
SENSOR_TYPE_ENVIRONMENTAL_ATMOSPHERIC_PRESSURE: Guid = Guid('{0e903829-ff8a-4a93-97df-3dcbde402288}')
SENSOR_TYPE_ENVIRONMENTAL_HUMIDITY: Guid = Guid('{5c72bf67-bd7e-4257-990b-98a3ba3b400a}')
SENSOR_TYPE_ENVIRONMENTAL_WIND_SPEED: Guid = Guid('{dd50607b-a45f-42cd-8efd-ec61761c4226}')
SENSOR_TYPE_ENVIRONMENTAL_WIND_DIRECTION: Guid = Guid('{9ef57a35-9306-434d-af09-37fa5a9c00bd}')
SENSOR_TYPE_ACCELEROMETER_1D: Guid = Guid('{c04d2387-7340-4cc2-991e-3b18cb8ef2f4}')
SENSOR_TYPE_ACCELEROMETER_2D: Guid = Guid('{b2c517a8-f6b5-4ba6-a423-5df560b4cc07}')
SENSOR_TYPE_ACCELEROMETER_3D: Guid = Guid('{c2fb0f5f-e2d2-4c78-bcd0-352a9582819d}')
SENSOR_TYPE_MOTION_DETECTOR: Guid = Guid('{5c7c1a12-30a5-43b9-a4b2-cf09ec5b7be8}')
SENSOR_TYPE_GYROMETER_1D: Guid = Guid('{fa088734-f552-4584-8324-edfaf649652c}')
SENSOR_TYPE_GYROMETER_2D: Guid = Guid('{31ef4f83-919b-48bf-8de0-5d7a9d240556}')
SENSOR_TYPE_GYROMETER_3D: Guid = Guid('{09485f5a-759e-42c2-bd4b-a349b75c8643}')
SENSOR_TYPE_SPEEDOMETER: Guid = Guid('{6bd73c1f-0bb4-4310-81b2-dfc18a52bf94}')
SENSOR_TYPE_COMPASS_1D: Guid = Guid('{a415f6c5-cb50-49d0-8e62-a8270bd7a26c}')
SENSOR_TYPE_COMPASS_2D: Guid = Guid('{15655cc0-997a-4d30-84db-57caba3648bb}')
SENSOR_TYPE_COMPASS_3D: Guid = Guid('{76b5ce0d-17dd-414d-93a1-e127f40bdf6e}')
SENSOR_TYPE_INCLINOMETER_1D: Guid = Guid('{b96f98c5-7a75-4ba7-94e9-ac868c966dd8}')
SENSOR_TYPE_INCLINOMETER_2D: Guid = Guid('{ab140f6d-83eb-4264-b70b-b16a5b256a01}')
SENSOR_TYPE_INCLINOMETER_3D: Guid = Guid('{b84919fb-ea85-4976-8444-6f6f5c6d31db}')
SENSOR_TYPE_DISTANCE_1D: Guid = Guid('{5f14ab2f-1407-4306-a93f-b1dbabe4f9c0}')
SENSOR_TYPE_DISTANCE_2D: Guid = Guid('{5cf9a46c-a9a2-4e55-b6a1-a04aafa95a92}')
SENSOR_TYPE_DISTANCE_3D: Guid = Guid('{a20cae31-0e25-4772-9fe5-96608a1354b2}')
SENSOR_TYPE_AGGREGATED_QUADRANT_ORIENTATION: Guid = Guid('{9f81f1af-c4ab-4307-9904-c828bfb90829}')
SENSOR_TYPE_AGGREGATED_DEVICE_ORIENTATION: Guid = Guid('{cdb5d8f7-3cfd-41c8-8542-cce622cf5d6e}')
SENSOR_TYPE_AGGREGATED_SIMPLE_DEVICE_ORIENTATION: Guid = Guid('{86a19291-0482-402c-bf4c-addac52b1c39}')
SENSOR_TYPE_VOLTAGE: Guid = Guid('{c5484637-4fb7-4953-98b8-a56d8aa1fb1e}')
SENSOR_TYPE_CURRENT: Guid = Guid('{5adc9fce-15a0-4bbe-a1ad-2d38a9ae831c}')
SENSOR_TYPE_CAPACITANCE: Guid = Guid('{ca2ffb1c-2317-49c0-a0b4-b63ce63461a0}')
SENSOR_TYPE_RESISTANCE: Guid = Guid('{9993d2c8-c157-4a52-a7b5-195c76037231}')
SENSOR_TYPE_INDUCTANCE: Guid = Guid('{dc1d933f-c435-4c7d-a2fe-607192a524d3}')
SENSOR_TYPE_ELECTRICAL_POWER: Guid = Guid('{212f10f5-14ab-4376-9a43-a7794098c2fe}')
SENSOR_TYPE_POTENTIOMETER: Guid = Guid('{2b3681a9-cadc-45aa-a6ff-54957c8bb440}')
SENSOR_TYPE_FREQUENCY: Guid = Guid('{8cd2cbb6-73e6-4640-a709-72ae8fb60d7f}')
SENSOR_TYPE_BOOLEAN_SWITCH: Guid = Guid('{9c7e371f-1041-460b-8d5c-71e4752e350c}')
SENSOR_TYPE_MULTIVALUE_SWITCH: Guid = Guid('{b3ee4d76-37a4-4402-b25e-99c60a775fa1}')
SENSOR_TYPE_FORCE: Guid = Guid('{c2ab2b02-1a1c-4778-a81b-954a1788cc75}')
SENSOR_TYPE_SCALE: Guid = Guid('{c06dd92c-7feb-438e-9bf6-82207fff5bb8}')
SENSOR_TYPE_PRESSURE: Guid = Guid('{26d31f34-6352-41cf-b793-ea0713d53d77}')
SENSOR_TYPE_STRAIN: Guid = Guid('{c6d1ec0e-6803-4361-ad3d-85bcc58c6d29}')
SENSOR_TYPE_BOOLEAN_SWITCH_ARRAY: Guid = Guid('{545c8ba5-b143-4545-868f-ca7fd986b4f6}')
SENSOR_TYPE_HUMAN_PRESENCE: Guid = Guid('{c138c12b-ad52-451c-9375-87f518ff10c6}')
SENSOR_TYPE_HUMAN_PROXIMITY: Guid = Guid('{5220dae9-3179-4430-9f90-06266d2a34de}')
SENSOR_TYPE_TOUCH: Guid = Guid('{17db3018-06c4-4f7d-81af-9274b7599c27}')
SENSOR_TYPE_AMBIENT_LIGHT: Guid = Guid('{97f115c8-599a-4153-8894-d2d12899918a}')
SENSOR_TYPE_RFID_SCANNER: Guid = Guid('{44328ef5-02dd-4e8d-ad5d-9249832b2eca}')
SENSOR_TYPE_BARCODE_SCANNER: Guid = Guid('{990b3d8f-85bb-45ff-914d-998c04f372df}')
SENSOR_TYPE_CUSTOM: Guid = Guid('{e83af229-8640-4d18-a213-e22675ebb2c3}')
SENSOR_TYPE_UNKNOWN: Guid = Guid('{10ba83e3-ef4f-41ed-9885-a87d6435a8e1}')
SENSOR_DATA_TYPE_COMMON_GUID: Guid = Guid('{db5e0cf2-cf1f-4c18-b46c-d86011d62150}')
SENSOR_DATA_TYPE_TIMESTAMP: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{db5e0cf2-cf1f-4c18-b46c-d86011d62150}'), pid=2)
SENSOR_DATA_TYPE_LOCATION_GUID: Guid = Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}')
SENSOR_DATA_TYPE_LATITUDE_DEGREES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=2)
SENSOR_DATA_TYPE_LONGITUDE_DEGREES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=3)
SENSOR_DATA_TYPE_ALTITUDE_SEALEVEL_METERS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=4)
SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_METERS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=5)
SENSOR_DATA_TYPE_SPEED_KNOTS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=6)
SENSOR_DATA_TYPE_TRUE_HEADING_DEGREES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=7)
SENSOR_DATA_TYPE_MAGNETIC_HEADING_DEGREES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=8)
SENSOR_DATA_TYPE_MAGNETIC_VARIATION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=9)
SENSOR_DATA_TYPE_FIX_QUALITY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=10)
SENSOR_DATA_TYPE_FIX_TYPE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=11)
SENSOR_DATA_TYPE_POSITION_DILUTION_OF_PRECISION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=12)
SENSOR_DATA_TYPE_HORIZONAL_DILUTION_OF_PRECISION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=13)
SENSOR_DATA_TYPE_VERTICAL_DILUTION_OF_PRECISION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=14)
SENSOR_DATA_TYPE_SATELLITES_USED_COUNT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=15)
SENSOR_DATA_TYPE_SATELLITES_USED_PRNS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=16)
SENSOR_DATA_TYPE_SATELLITES_IN_VIEW: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=17)
SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_PRNS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=18)
SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_ELEVATION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=19)
SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_AZIMUTH: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=20)
SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_STN_RATIO: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=21)
SENSOR_DATA_TYPE_ERROR_RADIUS_METERS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=22)
SENSOR_DATA_TYPE_ADDRESS1: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=23)
SENSOR_DATA_TYPE_ADDRESS2: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=24)
SENSOR_DATA_TYPE_CITY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=25)
SENSOR_DATA_TYPE_STATE_PROVINCE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=26)
SENSOR_DATA_TYPE_POSTALCODE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=27)
SENSOR_DATA_TYPE_COUNTRY_REGION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=28)
SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_ERROR_METERS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=29)
SENSOR_DATA_TYPE_ALTITUDE_SEALEVEL_ERROR_METERS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=30)
SENSOR_DATA_TYPE_GPS_SELECTION_MODE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=31)
SENSOR_DATA_TYPE_GPS_OPERATION_MODE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=32)
SENSOR_DATA_TYPE_GPS_STATUS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=33)
SENSOR_DATA_TYPE_GEOIDAL_SEPARATION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=34)
SENSOR_DATA_TYPE_DGPS_DATA_AGE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=35)
SENSOR_DATA_TYPE_ALTITUDE_ANTENNA_SEALEVEL_METERS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=36)
SENSOR_DATA_TYPE_DIFFERENTIAL_REFERENCE_STATION_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=37)
SENSOR_DATA_TYPE_NMEA_SENTENCE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=38)
SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=39)
SENSOR_DATA_TYPE_LOCATION_SOURCE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=40)
SENSOR_DATA_TYPE_SATELLITES_USED_PRNS_AND_CONSTELLATIONS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=41)
SENSOR_DATA_TYPE_ENVIRONMENTAL_GUID: Guid = Guid('{8b0aa2f1-2d57-42ee-8cc0-4d27622b46c4}')
SENSOR_DATA_TYPE_TEMPERATURE_CELSIUS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{8b0aa2f1-2d57-42ee-8cc0-4d27622b46c4}'), pid=2)
SENSOR_DATA_TYPE_RELATIVE_HUMIDITY_PERCENT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{8b0aa2f1-2d57-42ee-8cc0-4d27622b46c4}'), pid=3)
SENSOR_DATA_TYPE_ATMOSPHERIC_PRESSURE_BAR: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{8b0aa2f1-2d57-42ee-8cc0-4d27622b46c4}'), pid=4)
SENSOR_DATA_TYPE_WIND_DIRECTION_DEGREES_ANTICLOCKWISE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{8b0aa2f1-2d57-42ee-8cc0-4d27622b46c4}'), pid=5)
SENSOR_DATA_TYPE_WIND_SPEED_METERS_PER_SECOND: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{8b0aa2f1-2d57-42ee-8cc0-4d27622b46c4}'), pid=6)
SENSOR_DATA_TYPE_MOTION_GUID: Guid = Guid('{3f8a69a2-07c5-4e48-a965-cd797aab56d5}')
SENSOR_DATA_TYPE_ACCELERATION_X_G: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{3f8a69a2-07c5-4e48-a965-cd797aab56d5}'), pid=2)
SENSOR_DATA_TYPE_ACCELERATION_Y_G: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{3f8a69a2-07c5-4e48-a965-cd797aab56d5}'), pid=3)
SENSOR_DATA_TYPE_ACCELERATION_Z_G: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{3f8a69a2-07c5-4e48-a965-cd797aab56d5}'), pid=4)
SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_X_DEGREES_PER_SECOND_SQUARED: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{3f8a69a2-07c5-4e48-a965-cd797aab56d5}'), pid=5)
SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_Y_DEGREES_PER_SECOND_SQUARED: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{3f8a69a2-07c5-4e48-a965-cd797aab56d5}'), pid=6)
SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_Z_DEGREES_PER_SECOND_SQUARED: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{3f8a69a2-07c5-4e48-a965-cd797aab56d5}'), pid=7)
SENSOR_DATA_TYPE_SPEED_METERS_PER_SECOND: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{3f8a69a2-07c5-4e48-a965-cd797aab56d5}'), pid=8)
SENSOR_DATA_TYPE_MOTION_STATE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{3f8a69a2-07c5-4e48-a965-cd797aab56d5}'), pid=9)
SENSOR_DATA_TYPE_ANGULAR_VELOCITY_X_DEGREES_PER_SECOND: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{3f8a69a2-07c5-4e48-a965-cd797aab56d5}'), pid=10)
SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Y_DEGREES_PER_SECOND: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{3f8a69a2-07c5-4e48-a965-cd797aab56d5}'), pid=11)
SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Z_DEGREES_PER_SECOND: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{3f8a69a2-07c5-4e48-a965-cd797aab56d5}'), pid=12)
SENSOR_DATA_TYPE_ORIENTATION_GUID: Guid = Guid('{1637d8a2-4248-4275-865d-558de84aedfd}')
SENSOR_DATA_TYPE_TILT_X_DEGREES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=2)
SENSOR_DATA_TYPE_TILT_Y_DEGREES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=3)
SENSOR_DATA_TYPE_TILT_Z_DEGREES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=4)
SENSOR_DATA_TYPE_MAGNETIC_HEADING_X_DEGREES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=5)
SENSOR_DATA_TYPE_MAGNETIC_HEADING_Y_DEGREES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=6)
SENSOR_DATA_TYPE_MAGNETIC_HEADING_Z_DEGREES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=7)
SENSOR_DATA_TYPE_DISTANCE_X_METERS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=8)
SENSOR_DATA_TYPE_DISTANCE_Y_METERS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=9)
SENSOR_DATA_TYPE_DISTANCE_Z_METERS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=10)
SENSOR_DATA_TYPE_MAGNETIC_HEADING_COMPENSATED_MAGNETIC_NORTH_DEGREES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=11)
SENSOR_DATA_TYPE_MAGNETIC_HEADING_COMPENSATED_TRUE_NORTH_DEGREES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=12)
SENSOR_DATA_TYPE_MAGNETIC_HEADING_MAGNETIC_NORTH_DEGREES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=13)
SENSOR_DATA_TYPE_MAGNETIC_HEADING_TRUE_NORTH_DEGREES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=14)
SENSOR_DATA_TYPE_QUADRANT_ANGLE_DEGREES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=15)
SENSOR_DATA_TYPE_ROTATION_MATRIX: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=16)
SENSOR_DATA_TYPE_QUATERNION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=17)
SENSOR_DATA_TYPE_SIMPLE_DEVICE_ORIENTATION: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=18)
SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_X_MILLIGAUSS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=19)
SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_Y_MILLIGAUSS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=20)
SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_Z_MILLIGAUSS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=21)
SENSOR_DATA_TYPE_MAGNETOMETER_ACCURACY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=22)
SENSOR_DATA_TYPE_GUID_MECHANICAL_GUID: Guid = Guid('{38564a7c-f2f2-49bb-9b2b-ba60f66a58df}')
SENSOR_DATA_TYPE_BOOLEAN_SWITCH_STATE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{38564a7c-f2f2-49bb-9b2b-ba60f66a58df}'), pid=2)
SENSOR_DATA_TYPE_MULTIVALUE_SWITCH_STATE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{38564a7c-f2f2-49bb-9b2b-ba60f66a58df}'), pid=3)
SENSOR_DATA_TYPE_FORCE_NEWTONS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{38564a7c-f2f2-49bb-9b2b-ba60f66a58df}'), pid=4)
SENSOR_DATA_TYPE_ABSOLUTE_PRESSURE_PASCAL: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{38564a7c-f2f2-49bb-9b2b-ba60f66a58df}'), pid=5)
SENSOR_DATA_TYPE_GAUGE_PRESSURE_PASCAL: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{38564a7c-f2f2-49bb-9b2b-ba60f66a58df}'), pid=6)
SENSOR_DATA_TYPE_STRAIN: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{38564a7c-f2f2-49bb-9b2b-ba60f66a58df}'), pid=7)
SENSOR_DATA_TYPE_WEIGHT_KILOGRAMS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{38564a7c-f2f2-49bb-9b2b-ba60f66a58df}'), pid=8)
SENSOR_DATA_TYPE_BOOLEAN_SWITCH_ARRAY_STATES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{38564a7c-f2f2-49bb-9b2b-ba60f66a58df}'), pid=10)
SENSOR_DATA_TYPE_BIOMETRIC_GUID: Guid = Guid('{2299288a-6d9e-4b0b-b7ec-3528f89e40af}')
SENSOR_DATA_TYPE_HUMAN_PRESENCE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2299288a-6d9e-4b0b-b7ec-3528f89e40af}'), pid=2)
SENSOR_DATA_TYPE_HUMAN_PROXIMITY_METERS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2299288a-6d9e-4b0b-b7ec-3528f89e40af}'), pid=3)
SENSOR_DATA_TYPE_TOUCH_STATE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{2299288a-6d9e-4b0b-b7ec-3528f89e40af}'), pid=4)
SENSOR_DATA_TYPE_LIGHT_GUID: Guid = Guid('{e4c77ce2-dcb7-46e9-8439-4fec548833a6}')
SENSOR_DATA_TYPE_LIGHT_LEVEL_LUX: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{e4c77ce2-dcb7-46e9-8439-4fec548833a6}'), pid=2)
SENSOR_DATA_TYPE_LIGHT_TEMPERATURE_KELVIN: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{e4c77ce2-dcb7-46e9-8439-4fec548833a6}'), pid=3)
SENSOR_DATA_TYPE_LIGHT_CHROMACITY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{e4c77ce2-dcb7-46e9-8439-4fec548833a6}'), pid=4)
SENSOR_DATA_TYPE_SCANNER_GUID: Guid = Guid('{d7a59a3c-3421-44ab-8d3a-9de8ab6c4cae}')
SENSOR_DATA_TYPE_RFID_TAG_40_BIT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{d7a59a3c-3421-44ab-8d3a-9de8ab6c4cae}'), pid=2)
SENSOR_DATA_TYPE_ELECTRICAL_GUID: Guid = Guid('{bbb246d1-e242-4780-a2d3-cded84f35842}')
SENSOR_DATA_TYPE_VOLTAGE_VOLTS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{bbb246d1-e242-4780-a2d3-cded84f35842}'), pid=2)
SENSOR_DATA_TYPE_CURRENT_AMPS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{bbb246d1-e242-4780-a2d3-cded84f35842}'), pid=3)
SENSOR_DATA_TYPE_CAPACITANCE_FARAD: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{bbb246d1-e242-4780-a2d3-cded84f35842}'), pid=4)
SENSOR_DATA_TYPE_RESISTANCE_OHMS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{bbb246d1-e242-4780-a2d3-cded84f35842}'), pid=5)
SENSOR_DATA_TYPE_INDUCTANCE_HENRY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{bbb246d1-e242-4780-a2d3-cded84f35842}'), pid=6)
SENSOR_DATA_TYPE_ELECTRICAL_POWER_WATTS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{bbb246d1-e242-4780-a2d3-cded84f35842}'), pid=7)
SENSOR_DATA_TYPE_ELECTRICAL_PERCENT_OF_RANGE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{bbb246d1-e242-4780-a2d3-cded84f35842}'), pid=8)
SENSOR_DATA_TYPE_ELECTRICAL_FREQUENCY_HERTZ: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{bbb246d1-e242-4780-a2d3-cded84f35842}'), pid=9)
SENSOR_DATA_TYPE_CUSTOM_GUID: Guid = Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}')
SENSOR_DATA_TYPE_CUSTOM_USAGE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=5)
SENSOR_DATA_TYPE_CUSTOM_BOOLEAN_ARRAY: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=6)
SENSOR_DATA_TYPE_CUSTOM_VALUE1: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=7)
SENSOR_DATA_TYPE_CUSTOM_VALUE2: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=8)
SENSOR_DATA_TYPE_CUSTOM_VALUE3: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=9)
SENSOR_DATA_TYPE_CUSTOM_VALUE4: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=10)
SENSOR_DATA_TYPE_CUSTOM_VALUE5: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=11)
SENSOR_DATA_TYPE_CUSTOM_VALUE6: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=12)
SENSOR_DATA_TYPE_CUSTOM_VALUE7: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=13)
SENSOR_DATA_TYPE_CUSTOM_VALUE8: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=14)
SENSOR_DATA_TYPE_CUSTOM_VALUE9: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=15)
SENSOR_DATA_TYPE_CUSTOM_VALUE10: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=16)
SENSOR_DATA_TYPE_CUSTOM_VALUE11: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=17)
SENSOR_DATA_TYPE_CUSTOM_VALUE12: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=18)
SENSOR_DATA_TYPE_CUSTOM_VALUE13: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=19)
SENSOR_DATA_TYPE_CUSTOM_VALUE14: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=20)
SENSOR_DATA_TYPE_CUSTOM_VALUE15: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=21)
SENSOR_DATA_TYPE_CUSTOM_VALUE16: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=22)
SENSOR_DATA_TYPE_CUSTOM_VALUE17: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=23)
SENSOR_DATA_TYPE_CUSTOM_VALUE18: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=24)
SENSOR_DATA_TYPE_CUSTOM_VALUE19: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=25)
SENSOR_DATA_TYPE_CUSTOM_VALUE20: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=26)
SENSOR_DATA_TYPE_CUSTOM_VALUE21: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=27)
SENSOR_DATA_TYPE_CUSTOM_VALUE22: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=28)
SENSOR_DATA_TYPE_CUSTOM_VALUE23: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=29)
SENSOR_DATA_TYPE_CUSTOM_VALUE24: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=30)
SENSOR_DATA_TYPE_CUSTOM_VALUE25: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=31)
SENSOR_DATA_TYPE_CUSTOM_VALUE26: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=32)
SENSOR_DATA_TYPE_CUSTOM_VALUE27: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=33)
SENSOR_DATA_TYPE_CUSTOM_VALUE28: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=34)
SENSOR_PROPERTY_TEST_GUID: Guid = Guid('{e1e962f4-6e65-45f7-9c36-d487b7b1bd34}')
SENSOR_PROPERTY_CLEAR_ASSISTANCE_DATA: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{e1e962f4-6e65-45f7-9c36-d487b7b1bd34}'), pid=2)
SENSOR_PROPERTY_TURN_ON_OFF_NMEA: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{e1e962f4-6e65-45f7-9c36-d487b7b1bd34}'), pid=3)
GNSS_CLEAR_ALL_ASSISTANCE_DATA: UInt32 = 1
GUID_SensorCategory_All: Guid = Guid('{c317c286-c468-4288-9975-d4c4587c442c}')
GUID_SensorCategory_Biometric: Guid = Guid('{ca19690f-a2c7-477d-a99e-99ec6e2b5648}')
GUID_SensorCategory_Electrical: Guid = Guid('{fb73fcd8-fc4a-483c-ac58-27b691c6beff}')
GUID_SensorCategory_Environmental: Guid = Guid('{323439aa-7f66-492b-ba0c-73e9aa0a65d5}')
GUID_SensorCategory_Light: Guid = Guid('{17a665c0-9063-4216-b202-5c7a255e18ce}')
GUID_SensorCategory_Location: Guid = Guid('{bfa794e4-f964-4fdb-90f6-51056bfe4b44}')
GUID_SensorCategory_Mechanical: Guid = Guid('{8d131d68-8ef7-4656-80b5-cccbd93791c5}')
GUID_SensorCategory_Motion: Guid = Guid('{cd09daf1-3b2e-4c3d-b598-b5e5ff93fd46}')
GUID_SensorCategory_Orientation: Guid = Guid('{9e6c04b6-96fe-4954-b726-68682a473f69}')
GUID_SensorCategory_Other: Guid = Guid('{2c90e7a9-f4c9-4fa2-af37-56d471fe5a3d}')
GUID_SensorCategory_PersonalActivity: Guid = Guid('{f1609081-1e12-412b-a14d-cbb0e95bd2e5}')
GUID_SensorCategory_Scanner: Guid = Guid('{b000e77e-f5b5-420f-815d-0270a726f270}')
GUID_SensorCategory_Unsupported: Guid = Guid('{2beae7fa-19b0-48c5-a1f6-b5480dc206b0}')
GUID_SensorType_Accelerometer3D: Guid = Guid('{c2fb0f5f-e2d2-4c78-bcd0-352a9582819d}')
GUID_SensorType_ActivityDetection: Guid = Guid('{9d9e0118-1807-4f2e-96e4-2ce57142e196}')
GUID_SensorType_AmbientLight: Guid = Guid('{97f115c8-599a-4153-8894-d2d12899918a}')
GUID_SensorType_Barometer: Guid = Guid('{0e903829-ff8a-4a93-97df-3dcbde402288}')
GUID_SensorType_Custom: Guid = Guid('{e83af229-8640-4d18-a213-e22675ebb2c3}')
GUID_SensorType_FloorElevation: Guid = Guid('{ade4987f-7ac4-4dfa-9722-0a027181c747}')
GUID_SensorType_GeomagneticOrientation: Guid = Guid('{e77195f8-2d1f-4823-971b-1c4467556c9d}')
GUID_SensorType_GravityVector: Guid = Guid('{03b52c73-bb76-463f-9524-38de76eb700b}')
GUID_SensorType_Gyrometer3D: Guid = Guid('{09485f5a-759e-42c2-bd4b-a349b75c8643}')
GUID_SensorType_Humidity: Guid = Guid('{5c72bf67-bd7e-4257-990b-98a3ba3b400a}')
GUID_SensorType_LinearAccelerometer: Guid = Guid('{038b0283-97b4-41c8-bc24-5ff1aa48fec7}')
GUID_SensorType_Magnetometer3D: Guid = Guid('{55e5effb-15c7-40df-8698-a84b7c863c53}')
GUID_SensorType_Orientation: Guid = Guid('{cdb5d8f7-3cfd-41c8-8542-cce622cf5d6e}')
GUID_SensorType_Pedometer: Guid = Guid('{b19f89af-e3eb-444b-8dea-202575a71599}')
GUID_SensorType_Proximity: Guid = Guid('{5220dae9-3179-4430-9f90-06266d2a34de}')
GUID_SensorType_RelativeOrientation: Guid = Guid('{40993b51-4706-44dc-98d5-c920c037ffab}')
GUID_SensorType_SimpleDeviceOrientation: Guid = Guid('{86a19291-0482-402c-bf4c-addac52b1c39}')
GUID_SensorType_Temperature: Guid = Guid('{04fd0ec4-d5da-45fa-95a9-5db38ee19306}')
GUID_SensorType_HingeAngle: Guid = Guid('{82358065-f4c4-4da1-b272-13c23332a207}')
SENSOR_PROPERTY_LIST_HEADER_SIZE: UInt32 = 8
@winfunctype('SensorsUtilsV2.dll')
def GetPerformanceTime(TimeMs: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def InitPropVariantFromFloat(fltVal: Single, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetPropVariant(pList: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST), pKey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), TypeCheck: win32more.Windows.Win32.Foundation.BOOLEAN, pValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeySetPropVariant(pList: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST), pKey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), TypeCheck: win32more.Windows.Win32.Foundation.BOOLEAN, pValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetFileTime(pList: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST), pKey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pRetValue: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetGuid(pList: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST), pKey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pRetValue: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetBool(pList: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST), pKey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pRetValue: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetUlong(pList: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST), pKey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pRetValue: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetUshort(pList: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST), pKey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pRetValue: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetFloat(pList: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST), pKey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pRetValue: POINTER(Single)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetDouble(pList: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST), pKey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pRetValue: POINTER(Double)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetInt32(pList: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST), pKey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pRetValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetInt64(pList: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST), pKey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pRetValue: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetNthUlong(pList: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST), pKey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), Occurrence: UInt32, pRetValue: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetNthUshort(pList: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST), pKey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), Occurrence: UInt32, pRetValue: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetNthInt64(pList: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST), pKey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), Occurrence: UInt32, pRetValue: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def IsKeyPresentInPropertyList(pList: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_PROPERTY_LIST), pKey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('SensorsUtilsV2.dll')
def IsKeyPresentInCollectionList(pList: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST), pKey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('SensorsUtilsV2.dll')
def IsCollectionListSame(ListA: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST), ListB: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('SensorsUtilsV2.dll')
def PropVariantGetInformation(PropVariantValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), PropVariantOffset: POINTER(UInt32), PropVariantSize: POINTER(UInt32), PropVariantPointer: POINTER(VoidPtr), RemappedType: POINTER(win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropertiesListCopy(Target: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_PROPERTY_LIST), Source: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_PROPERTY_LIST)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropertiesListGetFillableCount(BufferSizeBytes: UInt32) -> UInt32: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListGetMarshalledSize(Collection: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST)) -> UInt32: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListCopyAndMarshall(Target: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST), Source: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListMarshall(Target: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListGetMarshalledSizeWithoutSerialization(Collection: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST)) -> UInt32: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListUpdateMarshalledPointer(Collection: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def SerializationBufferAllocate(SizeInBytes: UInt32, pBuffer: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def SerializationBufferFree(Buffer: POINTER(Byte)) -> Void: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListGetSerializedSize(Collection: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST)) -> UInt32: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListSerializeToBuffer(SourceCollection: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST), TargetBufferSizeInBytes: UInt32, TargetBuffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListAllocateBufferAndSerialize(SourceCollection: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST), pTargetBufferSizeInBytes: POINTER(UInt32), pTargetBuffer: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListDeserializeFromBuffer(SourceBufferSizeInBytes: UInt32, SourceBuffer: POINTER(Byte), TargetCollection: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def SensorCollectionGetAt(Index: UInt32, pSensorsList: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST), pKey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListGetFillableCount(BufferSizeBytes: UInt32) -> UInt32: ...
@winfunctype('SensorsUtilsV2.dll')
def EvaluateActivityThresholds(newSample: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST), oldSample: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST), thresholds: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListSortSubscribedActivitiesByConfidence(thresholds: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST), pCollection: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def InitPropVariantFromCLSIDArray(members: POINTER(Guid), size: UInt32, ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SensorsUtilsV2.dll')
def IsSensorSubscribed(subscriptionList: POINTER(win32more.Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST), currentType: Guid) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('SensorsUtilsV2.dll')
def IsGUIDPresentInList(guidArray: POINTER(Guid), arrayLength: UInt32, guidElem: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
ELEVATION_CHANGE_MODE = Int32
ElevationChangeMode_Unknown: win32more.Windows.Win32.Devices.Sensors.ELEVATION_CHANGE_MODE = 0
ElevationChangeMode_Elevator: win32more.Windows.Win32.Devices.Sensors.ELEVATION_CHANGE_MODE = 1
ElevationChangeMode_Stepping: win32more.Windows.Win32.Devices.Sensors.ELEVATION_CHANGE_MODE = 2
ElevationChangeMode_Max: win32more.Windows.Win32.Devices.Sensors.ELEVATION_CHANGE_MODE = 3
ElevationChangeMode_Force_Dword: win32more.Windows.Win32.Devices.Sensors.ELEVATION_CHANGE_MODE = -1
HUMAN_PRESENCE_DETECTION_TYPE = Int32
HumanPresenceDetectionType_Undefined: win32more.Windows.Win32.Devices.Sensors.HUMAN_PRESENCE_DETECTION_TYPE = 0
HumanPresenceDetectionType_VendorDefinedNonBiometric: win32more.Windows.Win32.Devices.Sensors.HUMAN_PRESENCE_DETECTION_TYPE = 1
HumanPresenceDetectionType_VendorDefinedBiometric: win32more.Windows.Win32.Devices.Sensors.HUMAN_PRESENCE_DETECTION_TYPE = 2
HumanPresenceDetectionType_FacialBiometric: win32more.Windows.Win32.Devices.Sensors.HUMAN_PRESENCE_DETECTION_TYPE = 4
HumanPresenceDetectionType_AudioBiometric: win32more.Windows.Win32.Devices.Sensors.HUMAN_PRESENCE_DETECTION_TYPE = 8
HumanPresenceDetectionType_Force_Dword: win32more.Windows.Win32.Devices.Sensors.HUMAN_PRESENCE_DETECTION_TYPE = -1
HUMAN_PRESENCE_DETECTION_TYPE_COUNT = Int32
HumanPresenceDetectionTypeCount: win32more.Windows.Win32.Devices.Sensors.HUMAN_PRESENCE_DETECTION_TYPE_COUNT = 4
class ILocationPermissions(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d5fb0a7f-e74e-44f5-8e02-4806863a274f}')
    @commethod(3)
    def GetGlobalLocationPermission(self, pfEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CheckLocationCapability(self, dwClientThreadId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISensor(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5fa08f80-2657-458e-af75-46f73fa6ac5c}')
    @commethod(3)
    def GetID(self, pID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCategory(self, pSensorCategory: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetType(self, pSensorType: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFriendlyName(self, pFriendlyName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetProperty(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pProperty: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetProperties(self, pKeys: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection, ppProperties: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSupportedDataFields(self, ppDataFields: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetProperties(self, pProperties: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues, ppResults: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SupportsDataField(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pIsSupported: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetState(self, pState: POINTER(win32more.Windows.Win32.Devices.Sensors.SensorState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetData(self, ppDataReport: POINTER(win32more.Windows.Win32.Devices.Sensors.ISensorDataReport)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SupportsEvent(self, eventGuid: POINTER(Guid), pIsSupported: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetEventInterest(self, ppValues: POINTER(POINTER(Guid)), pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetEventInterest(self, pValues: POINTER(Guid), count: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetEventSink(self, pEvents: win32more.Windows.Win32.Devices.Sensors.ISensorEvents) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISensorCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{23571e11-e545-4dd8-a337-b89bf44b10df}')
    @commethod(3)
    def GetAt(self, ulIndex: UInt32, ppSensor: POINTER(win32more.Windows.Win32.Devices.Sensors.ISensor)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCount(self, pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Add(self, pSensor: win32more.Windows.Win32.Devices.Sensors.ISensor) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Remove(self, pSensor: win32more.Windows.Win32.Devices.Sensors.ISensor) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveByID(self, sensorID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Clear(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISensorDataReport(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0ab9df9b-c4b5-4796-8898-0470706a2e1d}')
    @commethod(3)
    def GetTimestamp(self, pTimeStamp: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSensorValue(self, pKey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSensorValues(self, pKeys: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection, ppValues: POINTER(win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISensorEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5d8dcc91-4641-47e7-b7c3-b74f48a6c391}')
    @commethod(3)
    def OnStateChanged(self, pSensor: win32more.Windows.Win32.Devices.Sensors.ISensor, state: win32more.Windows.Win32.Devices.Sensors.SensorState) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnDataUpdated(self, pSensor: win32more.Windows.Win32.Devices.Sensors.ISensor, pNewData: win32more.Windows.Win32.Devices.Sensors.ISensorDataReport) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnEvent(self, pSensor: win32more.Windows.Win32.Devices.Sensors.ISensor, eventID: POINTER(Guid), pEventData: win32more.Windows.Win32.Devices.PortableDevices.IPortableDeviceValues) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnLeave(self, ID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISensorManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bd77db67-45a8-42dc-8d00-6dcf15f8377a}')
    @commethod(3)
    def GetSensorsByCategory(self, sensorCategory: POINTER(Guid), ppSensorsFound: POINTER(win32more.Windows.Win32.Devices.Sensors.ISensorCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSensorsByType(self, sensorType: POINTER(Guid), ppSensorsFound: POINTER(win32more.Windows.Win32.Devices.Sensors.ISensorCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSensorByID(self, sensorID: POINTER(Guid), ppSensor: POINTER(win32more.Windows.Win32.Devices.Sensors.ISensor)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetEventSink(self, pEvents: win32more.Windows.Win32.Devices.Sensors.ISensorManagerEvents) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RequestPermissions(self, hParent: win32more.Windows.Win32.Foundation.HWND, pSensors: win32more.Windows.Win32.Devices.Sensors.ISensorCollection, fModal: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISensorManagerEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9b3b0b86-266a-4aad-b21f-fde5501001b7}')
    @commethod(3)
    def OnSensorEnter(self, pSensor: win32more.Windows.Win32.Devices.Sensors.ISensor, state: win32more.Windows.Win32.Devices.Sensors.SensorState) -> win32more.Windows.Win32.Foundation.HRESULT: ...
LOCATION_DESIRED_ACCURACY = Int32
LOCATION_DESIRED_ACCURACY_DEFAULT: win32more.Windows.Win32.Devices.Sensors.LOCATION_DESIRED_ACCURACY = 0
LOCATION_DESIRED_ACCURACY_HIGH: win32more.Windows.Win32.Devices.Sensors.LOCATION_DESIRED_ACCURACY = 1
LOCATION_POSITION_SOURCE = Int32
LOCATION_POSITION_SOURCE_CELLULAR: win32more.Windows.Win32.Devices.Sensors.LOCATION_POSITION_SOURCE = 0
LOCATION_POSITION_SOURCE_SATELLITE: win32more.Windows.Win32.Devices.Sensors.LOCATION_POSITION_SOURCE = 1
LOCATION_POSITION_SOURCE_WIFI: win32more.Windows.Win32.Devices.Sensors.LOCATION_POSITION_SOURCE = 2
LOCATION_POSITION_SOURCE_IPADDRESS: win32more.Windows.Win32.Devices.Sensors.LOCATION_POSITION_SOURCE = 3
LOCATION_POSITION_SOURCE_UNKNOWN: win32more.Windows.Win32.Devices.Sensors.LOCATION_POSITION_SOURCE = 4
MAGNETOMETER_ACCURACY = Int32
MagnetometerAccuracy_Unknown: win32more.Windows.Win32.Devices.Sensors.MAGNETOMETER_ACCURACY = 0
MagnetometerAccuracy_Unreliable: win32more.Windows.Win32.Devices.Sensors.MAGNETOMETER_ACCURACY = 1
MagnetometerAccuracy_Approximate: win32more.Windows.Win32.Devices.Sensors.MAGNETOMETER_ACCURACY = 2
MagnetometerAccuracy_High: win32more.Windows.Win32.Devices.Sensors.MAGNETOMETER_ACCURACY = 3
class MATRIX3X3(Structure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous1: _Anonymous1_e__Struct
        Anonymous2: _Anonymous2_e__Struct
        M: Single * 9
        class _Anonymous1_e__Struct(Structure):
            A11: Single
            A12: Single
            A13: Single
            A21: Single
            A22: Single
            A23: Single
            A31: Single
            A32: Single
            A33: Single
        class _Anonymous2_e__Struct(Structure):
            V1: win32more.Windows.Win32.Devices.Sensors.VEC3D
            V2: win32more.Windows.Win32.Devices.Sensors.VEC3D
            V3: win32more.Windows.Win32.Devices.Sensors.VEC3D
MagnetometerAccuracy = Int32
MAGNETOMETER_ACCURACY_UNKNOWN: win32more.Windows.Win32.Devices.Sensors.MagnetometerAccuracy = 0
MAGNETOMETER_ACCURACY_UNRELIABLE: win32more.Windows.Win32.Devices.Sensors.MagnetometerAccuracy = 1
MAGNETOMETER_ACCURACY_APPROXIMATE: win32more.Windows.Win32.Devices.Sensors.MagnetometerAccuracy = 2
MAGNETOMETER_ACCURACY_HIGH: win32more.Windows.Win32.Devices.Sensors.MagnetometerAccuracy = 3
PEDOMETER_STEP_TYPE = Int32
PedometerStepType_Unknown: win32more.Windows.Win32.Devices.Sensors.PEDOMETER_STEP_TYPE = 1
PedometerStepType_Walking: win32more.Windows.Win32.Devices.Sensors.PEDOMETER_STEP_TYPE = 2
PedometerStepType_Running: win32more.Windows.Win32.Devices.Sensors.PEDOMETER_STEP_TYPE = 4
PedometerStepType_Max: win32more.Windows.Win32.Devices.Sensors.PEDOMETER_STEP_TYPE = 8
PedometerStepType_Force_Dword: win32more.Windows.Win32.Devices.Sensors.PEDOMETER_STEP_TYPE = -1
PEDOMETER_STEP_TYPE_COUNT = Int32
PedometerStepTypeCount: win32more.Windows.Win32.Devices.Sensors.PEDOMETER_STEP_TYPE_COUNT = 3
PROXIMITY_SENSOR_CAPABILITIES = Int32
Proximity_Sensor_Human_Presence_Capable: win32more.Windows.Win32.Devices.Sensors.PROXIMITY_SENSOR_CAPABILITIES = 1
Proximity_Sensor_Human_Engagement_Capable: win32more.Windows.Win32.Devices.Sensors.PROXIMITY_SENSOR_CAPABILITIES = 2
Proximity_Sensor_Supported_Capabilities: win32more.Windows.Win32.Devices.Sensors.PROXIMITY_SENSOR_CAPABILITIES = 3
PROXIMITY_TYPE = Int32
ProximityType_ObjectProximity: win32more.Windows.Win32.Devices.Sensors.PROXIMITY_TYPE = 0
ProximityType_HumanProximity: win32more.Windows.Win32.Devices.Sensors.PROXIMITY_TYPE = 1
ProximityType_Force_Dword: win32more.Windows.Win32.Devices.Sensors.PROXIMITY_TYPE = -1
class QUATERNION(Structure):
    X: Single
    Y: Single
    Z: Single
    W: Single
class SENSOR_COLLECTION_LIST(Structure):
    AllocatedSizeInBytes: UInt32
    Count: UInt32
    List: win32more.Windows.Win32.Devices.Sensors.SENSOR_VALUE_PAIR * 1
SENSOR_CONNECTION_TYPES = Int32
SensorConnectionType_Integrated: win32more.Windows.Win32.Devices.Sensors.SENSOR_CONNECTION_TYPES = 0
SensorConnectionType_Attached: win32more.Windows.Win32.Devices.Sensors.SENSOR_CONNECTION_TYPES = 1
SensorConnectionType_External: win32more.Windows.Win32.Devices.Sensors.SENSOR_CONNECTION_TYPES = 2
class SENSOR_PROPERTY_LIST(Structure):
    AllocatedSizeInBytes: UInt32
    Count: UInt32
    List: win32more.Windows.Win32.Foundation.PROPERTYKEY * 1
SENSOR_STATE = Int32
SensorState_Initializing: win32more.Windows.Win32.Devices.Sensors.SENSOR_STATE = 0
SensorState_Idle: win32more.Windows.Win32.Devices.Sensors.SENSOR_STATE = 1
SensorState_Active: win32more.Windows.Win32.Devices.Sensors.SENSOR_STATE = 2
SensorState_Error: win32more.Windows.Win32.Devices.Sensors.SENSOR_STATE = 3
class SENSOR_VALUE_PAIR(Structure):
    Key: win32more.Windows.Win32.Foundation.PROPERTYKEY
    Value: win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT
SIMPLE_DEVICE_ORIENTATION = Int32
SimpleDeviceOrientation_NotRotated: win32more.Windows.Win32.Devices.Sensors.SIMPLE_DEVICE_ORIENTATION = 0
SimpleDeviceOrientation_Rotated90DegreesCounterclockwise: win32more.Windows.Win32.Devices.Sensors.SIMPLE_DEVICE_ORIENTATION = 1
SimpleDeviceOrientation_Rotated180DegreesCounterclockwise: win32more.Windows.Win32.Devices.Sensors.SIMPLE_DEVICE_ORIENTATION = 2
SimpleDeviceOrientation_Rotated270DegreesCounterclockwise: win32more.Windows.Win32.Devices.Sensors.SIMPLE_DEVICE_ORIENTATION = 3
SimpleDeviceOrientation_Faceup: win32more.Windows.Win32.Devices.Sensors.SIMPLE_DEVICE_ORIENTATION = 4
SimpleDeviceOrientation_Facedown: win32more.Windows.Win32.Devices.Sensors.SIMPLE_DEVICE_ORIENTATION = 5
Sensor = Guid('{e97ced00-523a-4133-bf6f-d3a2dae7f6ba}')
SensorCollection = Guid('{79c43adb-a429-469f-aa39-2f2b74b75937}')
SensorConnectionType = Int32
SENSOR_CONNECTION_TYPE_PC_INTEGRATED: win32more.Windows.Win32.Devices.Sensors.SensorConnectionType = 0
SENSOR_CONNECTION_TYPE_PC_ATTACHED: win32more.Windows.Win32.Devices.Sensors.SensorConnectionType = 1
SENSOR_CONNECTION_TYPE_PC_EXTERNAL: win32more.Windows.Win32.Devices.Sensors.SensorConnectionType = 2
SensorDataReport = Guid('{4ea9d6ef-694b-4218-8816-ccda8da74bba}')
SensorManager = Guid('{77a1c827-fcd2-4689-8915-9d613cc5fa3e}')
SensorState = Int32
SENSOR_STATE_MIN: win32more.Windows.Win32.Devices.Sensors.SensorState = 0
SENSOR_STATE_READY: win32more.Windows.Win32.Devices.Sensors.SensorState = 0
SENSOR_STATE_NOT_AVAILABLE: win32more.Windows.Win32.Devices.Sensors.SensorState = 1
SENSOR_STATE_NO_DATA: win32more.Windows.Win32.Devices.Sensors.SensorState = 2
SENSOR_STATE_INITIALIZING: win32more.Windows.Win32.Devices.Sensors.SensorState = 3
SENSOR_STATE_ACCESS_DENIED: win32more.Windows.Win32.Devices.Sensors.SensorState = 4
SENSOR_STATE_ERROR: win32more.Windows.Win32.Devices.Sensors.SensorState = 5
SENSOR_STATE_MAX: win32more.Windows.Win32.Devices.Sensors.SensorState = 5
SimpleDeviceOrientation = Int32
SIMPLE_DEVICE_ORIENTATION_NOT_ROTATED: win32more.Windows.Win32.Devices.Sensors.SimpleDeviceOrientation = 0
SIMPLE_DEVICE_ORIENTATION_ROTATED_90: win32more.Windows.Win32.Devices.Sensors.SimpleDeviceOrientation = 1
SIMPLE_DEVICE_ORIENTATION_ROTATED_180: win32more.Windows.Win32.Devices.Sensors.SimpleDeviceOrientation = 2
SIMPLE_DEVICE_ORIENTATION_ROTATED_270: win32more.Windows.Win32.Devices.Sensors.SimpleDeviceOrientation = 3
SIMPLE_DEVICE_ORIENTATION_ROTATED_FACE_UP: win32more.Windows.Win32.Devices.Sensors.SimpleDeviceOrientation = 4
SIMPLE_DEVICE_ORIENTATION_ROTATED_FACE_DOWN: win32more.Windows.Win32.Devices.Sensors.SimpleDeviceOrientation = 5
class VEC3D(Structure):
    X: Single
    Y: Single
    Z: Single


make_ready(__name__)
