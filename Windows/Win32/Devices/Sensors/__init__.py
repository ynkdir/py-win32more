from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Devices.PortableDevices
import Windows.Win32.Devices.Properties
import Windows.Win32.Devices.Sensors
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.Com.StructuredStorage
import Windows.Win32.UI.Shell.PropertiesSystem
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
ACTIVITY_STATE = Int32
ActivityState_Unknown: ACTIVITY_STATE = 1
ActivityState_Stationary: ACTIVITY_STATE = 2
ActivityState_Fidgeting: ACTIVITY_STATE = 4
ActivityState_Walking: ACTIVITY_STATE = 8
ActivityState_Running: ACTIVITY_STATE = 16
ActivityState_InVehicle: ACTIVITY_STATE = 32
ActivityState_Biking: ACTIVITY_STATE = 64
ActivityState_Idle: ACTIVITY_STATE = 128
ActivityState_Max: ACTIVITY_STATE = 256
ActivityState_Force_Dword: ACTIVITY_STATE = -1
ACTIVITY_STATE_COUNT = Int32
ACTIVITY_STATE_COUNT_ActivityStateCount: ACTIVITY_STATE_COUNT = 8
AXIS = Int32
AXIS_X: AXIS = 0
AXIS_Y: AXIS = 1
AXIS_Z: AXIS = 2
AXIS_MAX: AXIS = 3
GUID_DEVINTERFACE_SENSOR: Guid = Guid('{ba1bb692-9b7a-4833-9a1e-525ed134e7e2}')
SENSOR_EVENT_STATE_CHANGED: Guid = Guid('{bfd96016-6bd7-4560-ad34-f2f6607e8f81}')
SENSOR_EVENT_DATA_UPDATED: Guid = Guid('{2ed0f2a4-0087-41d3-87db-6773370b3c88}')
SENSOR_EVENT_PROPERTY_CHANGED: Guid = Guid('{2358f099-84c9-4d3d-90df-c2421e2b2045}')
SENSOR_EVENT_ACCELEROMETER_SHAKE: Guid = Guid('{825f5a94-0f48-4396-9ca0-6ecb5c99d915}')
SENSOR_EVENT_PARAMETER_COMMON_GUID: Guid = Guid('{64346e30-8728-4b34-bdf6-4f52442c5c28}')
def SENSOR_EVENT_PARAMETER_EVENT_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64346e30-8728-4b34-bdf6-4f52442c5c28}'), pid=2)
def SENSOR_EVENT_PARAMETER_STATE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{64346e30-8728-4b34-bdf6-4f52442c5c28}'), pid=3)
SENSOR_ERROR_PARAMETER_COMMON_GUID: Guid = Guid('{77112bcd-fce1-4f43-b8b8-a88256adb4b3}')
SENSOR_PROPERTY_COMMON_GUID: Guid = Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}')
def SENSOR_PROPERTY_TYPE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=2)
def SENSOR_PROPERTY_STATE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=3)
def SENSOR_PROPERTY_PERSISTENT_UNIQUE_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=5)
def SENSOR_PROPERTY_MANUFACTURER():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=6)
def SENSOR_PROPERTY_MODEL():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=7)
def SENSOR_PROPERTY_SERIAL_NUMBER():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=8)
def SENSOR_PROPERTY_FRIENDLY_NAME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=9)
def SENSOR_PROPERTY_DESCRIPTION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=10)
def SENSOR_PROPERTY_CONNECTION_TYPE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=11)
def SENSOR_PROPERTY_MIN_REPORT_INTERVAL():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=12)
def SENSOR_PROPERTY_CURRENT_REPORT_INTERVAL():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=13)
def SENSOR_PROPERTY_CHANGE_SENSITIVITY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=14)
def SENSOR_PROPERTY_DEVICE_PATH():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=15)
def SENSOR_PROPERTY_LIGHT_RESPONSE_CURVE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=16)
def SENSOR_PROPERTY_ACCURACY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=17)
def SENSOR_PROPERTY_RESOLUTION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=18)
def SENSOR_PROPERTY_LOCATION_DESIRED_ACCURACY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=19)
def SENSOR_PROPERTY_RANGE_MINIMUM():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=20)
def SENSOR_PROPERTY_RANGE_MAXIMUM():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=21)
def SENSOR_PROPERTY_HID_USAGE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=22)
def SENSOR_PROPERTY_RADIO_STATE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=23)
def SENSOR_PROPERTY_RADIO_STATE_PREVIOUS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{7f8383ec-d3ec-495c-a8cf-b8bbe85c2920}'), pid=24)
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
def SENSOR_DATA_TYPE_TIMESTAMP():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{db5e0cf2-cf1f-4c18-b46c-d86011d62150}'), pid=2)
SENSOR_DATA_TYPE_LOCATION_GUID: Guid = Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}')
def SENSOR_DATA_TYPE_LATITUDE_DEGREES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=2)
def SENSOR_DATA_TYPE_LONGITUDE_DEGREES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=3)
def SENSOR_DATA_TYPE_ALTITUDE_SEALEVEL_METERS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=4)
def SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_METERS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=5)
def SENSOR_DATA_TYPE_SPEED_KNOTS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=6)
def SENSOR_DATA_TYPE_TRUE_HEADING_DEGREES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=7)
def SENSOR_DATA_TYPE_MAGNETIC_HEADING_DEGREES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=8)
def SENSOR_DATA_TYPE_MAGNETIC_VARIATION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=9)
def SENSOR_DATA_TYPE_FIX_QUALITY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=10)
def SENSOR_DATA_TYPE_FIX_TYPE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=11)
def SENSOR_DATA_TYPE_POSITION_DILUTION_OF_PRECISION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=12)
def SENSOR_DATA_TYPE_HORIZONAL_DILUTION_OF_PRECISION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=13)
def SENSOR_DATA_TYPE_VERTICAL_DILUTION_OF_PRECISION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=14)
def SENSOR_DATA_TYPE_SATELLITES_USED_COUNT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=15)
def SENSOR_DATA_TYPE_SATELLITES_USED_PRNS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=16)
def SENSOR_DATA_TYPE_SATELLITES_IN_VIEW():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=17)
def SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_PRNS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=18)
def SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_ELEVATION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=19)
def SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_AZIMUTH():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=20)
def SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_STN_RATIO():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=21)
def SENSOR_DATA_TYPE_ERROR_RADIUS_METERS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=22)
def SENSOR_DATA_TYPE_ADDRESS1():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=23)
def SENSOR_DATA_TYPE_ADDRESS2():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=24)
def SENSOR_DATA_TYPE_CITY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=25)
def SENSOR_DATA_TYPE_STATE_PROVINCE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=26)
def SENSOR_DATA_TYPE_POSTALCODE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=27)
def SENSOR_DATA_TYPE_COUNTRY_REGION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=28)
def SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_ERROR_METERS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=29)
def SENSOR_DATA_TYPE_ALTITUDE_SEALEVEL_ERROR_METERS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=30)
def SENSOR_DATA_TYPE_GPS_SELECTION_MODE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=31)
def SENSOR_DATA_TYPE_GPS_OPERATION_MODE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=32)
def SENSOR_DATA_TYPE_GPS_STATUS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=33)
def SENSOR_DATA_TYPE_GEOIDAL_SEPARATION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=34)
def SENSOR_DATA_TYPE_DGPS_DATA_AGE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=35)
def SENSOR_DATA_TYPE_ALTITUDE_ANTENNA_SEALEVEL_METERS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=36)
def SENSOR_DATA_TYPE_DIFFERENTIAL_REFERENCE_STATION_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=37)
def SENSOR_DATA_TYPE_NMEA_SENTENCE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=38)
def SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=39)
def SENSOR_DATA_TYPE_LOCATION_SOURCE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=40)
def SENSOR_DATA_TYPE_SATELLITES_USED_PRNS_AND_CONSTELLATIONS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{055c74d8-ca6f-47d6-95c6-1ed3637a0ff4}'), pid=41)
SENSOR_DATA_TYPE_ENVIRONMENTAL_GUID: Guid = Guid('{8b0aa2f1-2d57-42ee-8cc0-4d27622b46c4}')
def SENSOR_DATA_TYPE_TEMPERATURE_CELSIUS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8b0aa2f1-2d57-42ee-8cc0-4d27622b46c4}'), pid=2)
def SENSOR_DATA_TYPE_RELATIVE_HUMIDITY_PERCENT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8b0aa2f1-2d57-42ee-8cc0-4d27622b46c4}'), pid=3)
def SENSOR_DATA_TYPE_ATMOSPHERIC_PRESSURE_BAR():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8b0aa2f1-2d57-42ee-8cc0-4d27622b46c4}'), pid=4)
def SENSOR_DATA_TYPE_WIND_DIRECTION_DEGREES_ANTICLOCKWISE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8b0aa2f1-2d57-42ee-8cc0-4d27622b46c4}'), pid=5)
def SENSOR_DATA_TYPE_WIND_SPEED_METERS_PER_SECOND():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8b0aa2f1-2d57-42ee-8cc0-4d27622b46c4}'), pid=6)
SENSOR_DATA_TYPE_MOTION_GUID: Guid = Guid('{3f8a69a2-07c5-4e48-a965-cd797aab56d5}')
def SENSOR_DATA_TYPE_ACCELERATION_X_G():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{3f8a69a2-07c5-4e48-a965-cd797aab56d5}'), pid=2)
def SENSOR_DATA_TYPE_ACCELERATION_Y_G():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{3f8a69a2-07c5-4e48-a965-cd797aab56d5}'), pid=3)
def SENSOR_DATA_TYPE_ACCELERATION_Z_G():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{3f8a69a2-07c5-4e48-a965-cd797aab56d5}'), pid=4)
def SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_X_DEGREES_PER_SECOND_SQUARED():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{3f8a69a2-07c5-4e48-a965-cd797aab56d5}'), pid=5)
def SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_Y_DEGREES_PER_SECOND_SQUARED():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{3f8a69a2-07c5-4e48-a965-cd797aab56d5}'), pid=6)
def SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_Z_DEGREES_PER_SECOND_SQUARED():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{3f8a69a2-07c5-4e48-a965-cd797aab56d5}'), pid=7)
def SENSOR_DATA_TYPE_SPEED_METERS_PER_SECOND():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{3f8a69a2-07c5-4e48-a965-cd797aab56d5}'), pid=8)
def SENSOR_DATA_TYPE_MOTION_STATE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{3f8a69a2-07c5-4e48-a965-cd797aab56d5}'), pid=9)
def SENSOR_DATA_TYPE_ANGULAR_VELOCITY_X_DEGREES_PER_SECOND():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{3f8a69a2-07c5-4e48-a965-cd797aab56d5}'), pid=10)
def SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Y_DEGREES_PER_SECOND():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{3f8a69a2-07c5-4e48-a965-cd797aab56d5}'), pid=11)
def SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Z_DEGREES_PER_SECOND():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{3f8a69a2-07c5-4e48-a965-cd797aab56d5}'), pid=12)
SENSOR_DATA_TYPE_ORIENTATION_GUID: Guid = Guid('{1637d8a2-4248-4275-865d-558de84aedfd}')
def SENSOR_DATA_TYPE_TILT_X_DEGREES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=2)
def SENSOR_DATA_TYPE_TILT_Y_DEGREES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=3)
def SENSOR_DATA_TYPE_TILT_Z_DEGREES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=4)
def SENSOR_DATA_TYPE_MAGNETIC_HEADING_X_DEGREES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=5)
def SENSOR_DATA_TYPE_MAGNETIC_HEADING_Y_DEGREES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=6)
def SENSOR_DATA_TYPE_MAGNETIC_HEADING_Z_DEGREES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=7)
def SENSOR_DATA_TYPE_DISTANCE_X_METERS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=8)
def SENSOR_DATA_TYPE_DISTANCE_Y_METERS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=9)
def SENSOR_DATA_TYPE_DISTANCE_Z_METERS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=10)
def SENSOR_DATA_TYPE_MAGNETIC_HEADING_COMPENSATED_MAGNETIC_NORTH_DEGREES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=11)
def SENSOR_DATA_TYPE_MAGNETIC_HEADING_COMPENSATED_TRUE_NORTH_DEGREES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=12)
def SENSOR_DATA_TYPE_MAGNETIC_HEADING_MAGNETIC_NORTH_DEGREES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=13)
def SENSOR_DATA_TYPE_MAGNETIC_HEADING_TRUE_NORTH_DEGREES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=14)
def SENSOR_DATA_TYPE_QUADRANT_ANGLE_DEGREES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=15)
def SENSOR_DATA_TYPE_ROTATION_MATRIX():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=16)
def SENSOR_DATA_TYPE_QUATERNION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=17)
def SENSOR_DATA_TYPE_SIMPLE_DEVICE_ORIENTATION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=18)
def SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_X_MILLIGAUSS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=19)
def SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_Y_MILLIGAUSS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=20)
def SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_Z_MILLIGAUSS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=21)
def SENSOR_DATA_TYPE_MAGNETOMETER_ACCURACY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{1637d8a2-4248-4275-865d-558de84aedfd}'), pid=22)
SENSOR_DATA_TYPE_GUID_MECHANICAL_GUID: Guid = Guid('{38564a7c-f2f2-49bb-9b2b-ba60f66a58df}')
def SENSOR_DATA_TYPE_BOOLEAN_SWITCH_STATE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{38564a7c-f2f2-49bb-9b2b-ba60f66a58df}'), pid=2)
def SENSOR_DATA_TYPE_MULTIVALUE_SWITCH_STATE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{38564a7c-f2f2-49bb-9b2b-ba60f66a58df}'), pid=3)
def SENSOR_DATA_TYPE_FORCE_NEWTONS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{38564a7c-f2f2-49bb-9b2b-ba60f66a58df}'), pid=4)
def SENSOR_DATA_TYPE_ABSOLUTE_PRESSURE_PASCAL():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{38564a7c-f2f2-49bb-9b2b-ba60f66a58df}'), pid=5)
def SENSOR_DATA_TYPE_GAUGE_PRESSURE_PASCAL():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{38564a7c-f2f2-49bb-9b2b-ba60f66a58df}'), pid=6)
def SENSOR_DATA_TYPE_STRAIN():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{38564a7c-f2f2-49bb-9b2b-ba60f66a58df}'), pid=7)
def SENSOR_DATA_TYPE_WEIGHT_KILOGRAMS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{38564a7c-f2f2-49bb-9b2b-ba60f66a58df}'), pid=8)
def SENSOR_DATA_TYPE_BOOLEAN_SWITCH_ARRAY_STATES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{38564a7c-f2f2-49bb-9b2b-ba60f66a58df}'), pid=10)
SENSOR_DATA_TYPE_BIOMETRIC_GUID: Guid = Guid('{2299288a-6d9e-4b0b-b7ec-3528f89e40af}')
def SENSOR_DATA_TYPE_HUMAN_PRESENCE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{2299288a-6d9e-4b0b-b7ec-3528f89e40af}'), pid=2)
def SENSOR_DATA_TYPE_HUMAN_PROXIMITY_METERS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{2299288a-6d9e-4b0b-b7ec-3528f89e40af}'), pid=3)
def SENSOR_DATA_TYPE_TOUCH_STATE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{2299288a-6d9e-4b0b-b7ec-3528f89e40af}'), pid=4)
SENSOR_DATA_TYPE_LIGHT_GUID: Guid = Guid('{e4c77ce2-dcb7-46e9-8439-4fec548833a6}')
def SENSOR_DATA_TYPE_LIGHT_LEVEL_LUX():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e4c77ce2-dcb7-46e9-8439-4fec548833a6}'), pid=2)
def SENSOR_DATA_TYPE_LIGHT_TEMPERATURE_KELVIN():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e4c77ce2-dcb7-46e9-8439-4fec548833a6}'), pid=3)
def SENSOR_DATA_TYPE_LIGHT_CHROMACITY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e4c77ce2-dcb7-46e9-8439-4fec548833a6}'), pid=4)
SENSOR_DATA_TYPE_SCANNER_GUID: Guid = Guid('{d7a59a3c-3421-44ab-8d3a-9de8ab6c4cae}')
def SENSOR_DATA_TYPE_RFID_TAG_40_BIT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{d7a59a3c-3421-44ab-8d3a-9de8ab6c4cae}'), pid=2)
SENSOR_DATA_TYPE_ELECTRICAL_GUID: Guid = Guid('{bbb246d1-e242-4780-a2d3-cded84f35842}')
def SENSOR_DATA_TYPE_VOLTAGE_VOLTS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{bbb246d1-e242-4780-a2d3-cded84f35842}'), pid=2)
def SENSOR_DATA_TYPE_CURRENT_AMPS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{bbb246d1-e242-4780-a2d3-cded84f35842}'), pid=3)
def SENSOR_DATA_TYPE_CAPACITANCE_FARAD():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{bbb246d1-e242-4780-a2d3-cded84f35842}'), pid=4)
def SENSOR_DATA_TYPE_RESISTANCE_OHMS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{bbb246d1-e242-4780-a2d3-cded84f35842}'), pid=5)
def SENSOR_DATA_TYPE_INDUCTANCE_HENRY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{bbb246d1-e242-4780-a2d3-cded84f35842}'), pid=6)
def SENSOR_DATA_TYPE_ELECTRICAL_POWER_WATTS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{bbb246d1-e242-4780-a2d3-cded84f35842}'), pid=7)
def SENSOR_DATA_TYPE_ELECTRICAL_PERCENT_OF_RANGE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{bbb246d1-e242-4780-a2d3-cded84f35842}'), pid=8)
def SENSOR_DATA_TYPE_ELECTRICAL_FREQUENCY_HERTZ():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{bbb246d1-e242-4780-a2d3-cded84f35842}'), pid=9)
SENSOR_DATA_TYPE_CUSTOM_GUID: Guid = Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}')
def SENSOR_DATA_TYPE_CUSTOM_USAGE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=5)
def SENSOR_DATA_TYPE_CUSTOM_BOOLEAN_ARRAY():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=6)
def SENSOR_DATA_TYPE_CUSTOM_VALUE1():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=7)
def SENSOR_DATA_TYPE_CUSTOM_VALUE2():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=8)
def SENSOR_DATA_TYPE_CUSTOM_VALUE3():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=9)
def SENSOR_DATA_TYPE_CUSTOM_VALUE4():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=10)
def SENSOR_DATA_TYPE_CUSTOM_VALUE5():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=11)
def SENSOR_DATA_TYPE_CUSTOM_VALUE6():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=12)
def SENSOR_DATA_TYPE_CUSTOM_VALUE7():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=13)
def SENSOR_DATA_TYPE_CUSTOM_VALUE8():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=14)
def SENSOR_DATA_TYPE_CUSTOM_VALUE9():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=15)
def SENSOR_DATA_TYPE_CUSTOM_VALUE10():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=16)
def SENSOR_DATA_TYPE_CUSTOM_VALUE11():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=17)
def SENSOR_DATA_TYPE_CUSTOM_VALUE12():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=18)
def SENSOR_DATA_TYPE_CUSTOM_VALUE13():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=19)
def SENSOR_DATA_TYPE_CUSTOM_VALUE14():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=20)
def SENSOR_DATA_TYPE_CUSTOM_VALUE15():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=21)
def SENSOR_DATA_TYPE_CUSTOM_VALUE16():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=22)
def SENSOR_DATA_TYPE_CUSTOM_VALUE17():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=23)
def SENSOR_DATA_TYPE_CUSTOM_VALUE18():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=24)
def SENSOR_DATA_TYPE_CUSTOM_VALUE19():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=25)
def SENSOR_DATA_TYPE_CUSTOM_VALUE20():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=26)
def SENSOR_DATA_TYPE_CUSTOM_VALUE21():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=27)
def SENSOR_DATA_TYPE_CUSTOM_VALUE22():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=28)
def SENSOR_DATA_TYPE_CUSTOM_VALUE23():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=29)
def SENSOR_DATA_TYPE_CUSTOM_VALUE24():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=30)
def SENSOR_DATA_TYPE_CUSTOM_VALUE25():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=31)
def SENSOR_DATA_TYPE_CUSTOM_VALUE26():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=32)
def SENSOR_DATA_TYPE_CUSTOM_VALUE27():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=33)
def SENSOR_DATA_TYPE_CUSTOM_VALUE28():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{b14c764f-07cf-41e8-9d82-ebe3d0776a6f}'), pid=34)
SENSOR_PROPERTY_TEST_GUID: Guid = Guid('{e1e962f4-6e65-45f7-9c36-d487b7b1bd34}')
def SENSOR_PROPERTY_CLEAR_ASSISTANCE_DATA():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e1e962f4-6e65-45f7-9c36-d487b7b1bd34}'), pid=2)
def SENSOR_PROPERTY_TURN_ON_OFF_NMEA():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{e1e962f4-6e65-45f7-9c36-d487b7b1bd34}'), pid=3)
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
def GetPerformanceTime(TimeMs: POINTER(UInt32)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def InitPropVariantFromFloat(fltVal: Single, ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetPropVariant(pList: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), TypeCheck: Windows.Win32.Foundation.BOOLEAN, pValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeySetPropVariant(pList: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), TypeCheck: Windows.Win32.Foundation.BOOLEAN, pValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetFileTime(pList: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pRetValue: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetGuid(pList: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pRetValue: POINTER(Guid)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetBool(pList: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pRetValue: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetUlong(pList: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pRetValue: POINTER(UInt32)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetUshort(pList: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pRetValue: POINTER(UInt16)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetFloat(pList: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pRetValue: POINTER(Single)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetDouble(pList: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pRetValue: POINTER(Double)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetInt32(pList: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pRetValue: POINTER(Int32)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetInt64(pList: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pRetValue: POINTER(Int64)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetNthUlong(pList: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), Occurrence: UInt32, pRetValue: POINTER(UInt32)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetNthUshort(pList: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), Occurrence: UInt32, pRetValue: POINTER(UInt16)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetNthInt64(pList: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), Occurrence: UInt32, pRetValue: POINTER(Int64)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def IsKeyPresentInPropertyList(pList: POINTER(Windows.Win32.Devices.Sensors.SENSOR_PROPERTY_LIST_head), pKey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('SensorsUtilsV2.dll')
def IsKeyPresentInCollectionList(pList: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('SensorsUtilsV2.dll')
def IsCollectionListSame(ListA: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head), ListB: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head)) -> Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('SensorsUtilsV2.dll')
def PropVariantGetInformation(PropVariantValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), PropVariantOffset: POINTER(UInt32), PropVariantSize: POINTER(UInt32), PropVariantPointer: POINTER(VoidPtr), RemappedType: POINTER(Windows.Win32.Devices.Properties.DEVPROPTYPE)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropertiesListCopy(Target: POINTER(Windows.Win32.Devices.Sensors.SENSOR_PROPERTY_LIST_head), Source: POINTER(Windows.Win32.Devices.Sensors.SENSOR_PROPERTY_LIST_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropertiesListGetFillableCount(BufferSizeBytes: UInt32) -> UInt32: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListGetMarshalledSize(Collection: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head)) -> UInt32: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListCopyAndMarshall(Target: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head), Source: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListMarshall(Target: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListGetMarshalledSizeWithoutSerialization(Collection: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head)) -> UInt32: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListUpdateMarshalledPointer(Collection: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def SerializationBufferAllocate(SizeInBytes: UInt32, pBuffer: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def SerializationBufferFree(Buffer: POINTER(Byte)) -> Void: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListGetSerializedSize(Collection: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head)) -> UInt32: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListSerializeToBuffer(SourceCollection: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head), TargetBufferSizeInBytes: UInt32, TargetBuffer: POINTER(Byte)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListAllocateBufferAndSerialize(SourceCollection: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pTargetBufferSizeInBytes: POINTER(UInt32), pTargetBuffer: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListDeserializeFromBuffer(SourceBufferSizeInBytes: UInt32, SourceBuffer: POINTER(Byte), TargetCollection: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def SensorCollectionGetAt(Index: UInt32, pSensorsList: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListGetFillableCount(BufferSizeBytes: UInt32) -> UInt32: ...
@winfunctype('SensorsUtilsV2.dll')
def EvaluateActivityThresholds(newSample: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head), oldSample: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head), thresholds: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head)) -> Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListSortSubscribedActivitiesByConfidence(thresholds: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pCollection: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head)) -> Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def InitPropVariantFromCLSIDArray(members: POINTER(Guid), size: UInt32, ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SensorsUtilsV2.dll')
def IsSensorSubscribed(subscriptionList: POINTER(Windows.Win32.Devices.Sensors.SENSOR_COLLECTION_LIST_head), currentType: Guid) -> Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('SensorsUtilsV2.dll')
def IsGUIDPresentInList(guidArray: POINTER(Guid), arrayLength: UInt32, guidElem: POINTER(Guid)) -> Windows.Win32.Foundation.BOOLEAN: ...
ELEVATION_CHANGE_MODE = Int32
ElevationChangeMode_Unknown: ELEVATION_CHANGE_MODE = 0
ElevationChangeMode_Elevator: ELEVATION_CHANGE_MODE = 1
ElevationChangeMode_Stepping: ELEVATION_CHANGE_MODE = 2
ElevationChangeMode_Max: ELEVATION_CHANGE_MODE = 3
ElevationChangeMode_Force_Dword: ELEVATION_CHANGE_MODE = -1
HUMAN_PRESENCE_DETECTION_TYPE = Int32
HumanPresenceDetectionType_VendorDefinedNonBiometric: HUMAN_PRESENCE_DETECTION_TYPE = 1
HumanPresenceDetectionType_VendorDefinedBiometric: HUMAN_PRESENCE_DETECTION_TYPE = 2
HumanPresenceDetectionType_FacialBiometric: HUMAN_PRESENCE_DETECTION_TYPE = 4
HumanPresenceDetectionType_AudioBiometric: HUMAN_PRESENCE_DETECTION_TYPE = 8
HumanPresenceDetectionType_Force_Dword: HUMAN_PRESENCE_DETECTION_TYPE = -1
HUMAN_PRESENCE_DETECTION_TYPE_COUNT = Int32
HUMAN_PRESENCE_DETECTION_TYPE_COUNT_HumanPresenceDetectionTypeCount: HUMAN_PRESENCE_DETECTION_TYPE_COUNT = 4
class ILocationPermissions(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d5fb0a7f-e74e-44f5-8e02-4806863a274f}')
    @commethod(3)
    def GetGlobalLocationPermission(self, pfEnabled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CheckLocationCapability(self, dwClientThreadId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISensor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5fa08f80-2657-458e-af75-46f73fa6ac5c}')
    @commethod(3)
    def GetID(self, pID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCategory(self, pSensorCategory: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetType(self, pSensorType: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFriendlyName(self, pFriendlyName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetProperty(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pProperty: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetProperties(self, pKeys: Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection_head, ppProperties: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSupportedDataFields(self, ppDataFields: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetProperties(self, pProperties: Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head, ppResults: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SupportsDataField(self, key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pIsSupported: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetState(self, pState: POINTER(Windows.Win32.Devices.Sensors.SensorState)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetData(self, ppDataReport: POINTER(Windows.Win32.Devices.Sensors.ISensorDataReport_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SupportsEvent(self, eventGuid: POINTER(Guid), pIsSupported: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetEventInterest(self, ppValues: POINTER(POINTER(Guid)), pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetEventInterest(self, pValues: POINTER(Guid), count: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetEventSink(self, pEvents: Windows.Win32.Devices.Sensors.ISensorEvents_head) -> Windows.Win32.Foundation.HRESULT: ...
class ISensorCollection(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{23571e11-e545-4dd8-a337-b89bf44b10df}')
    @commethod(3)
    def GetAt(self, ulIndex: UInt32, ppSensor: POINTER(Windows.Win32.Devices.Sensors.ISensor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCount(self, pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Add(self, pSensor: Windows.Win32.Devices.Sensors.ISensor_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Remove(self, pSensor: Windows.Win32.Devices.Sensors.ISensor_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveByID(self, sensorID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Clear(self) -> Windows.Win32.Foundation.HRESULT: ...
class ISensorDataReport(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0ab9df9b-c4b5-4796-8898-0470706a2e1d}')
    @commethod(3)
    def GetTimestamp(self, pTimeStamp: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSensorValue(self, pKey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSensorValues(self, pKeys: Windows.Win32.Devices.PortableDevices.IPortableDeviceKeyCollection_head, ppValues: POINTER(Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISensorEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5d8dcc91-4641-47e7-b7c3-b74f48a6c391}')
    @commethod(3)
    def OnStateChanged(self, pSensor: Windows.Win32.Devices.Sensors.ISensor_head, state: Windows.Win32.Devices.Sensors.SensorState) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnDataUpdated(self, pSensor: Windows.Win32.Devices.Sensors.ISensor_head, pNewData: Windows.Win32.Devices.Sensors.ISensorDataReport_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnEvent(self, pSensor: Windows.Win32.Devices.Sensors.ISensor_head, eventID: POINTER(Guid), pEventData: Windows.Win32.Devices.PortableDevices.IPortableDeviceValues_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnLeave(self, ID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class ISensorManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bd77db67-45a8-42dc-8d00-6dcf15f8377a}')
    @commethod(3)
    def GetSensorsByCategory(self, sensorCategory: POINTER(Guid), ppSensorsFound: POINTER(Windows.Win32.Devices.Sensors.ISensorCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSensorsByType(self, sensorType: POINTER(Guid), ppSensorsFound: POINTER(Windows.Win32.Devices.Sensors.ISensorCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSensorByID(self, sensorID: POINTER(Guid), ppSensor: POINTER(Windows.Win32.Devices.Sensors.ISensor_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetEventSink(self, pEvents: Windows.Win32.Devices.Sensors.ISensorManagerEvents_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RequestPermissions(self, hParent: Windows.Win32.Foundation.HWND, pSensors: Windows.Win32.Devices.Sensors.ISensorCollection_head, fModal: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class ISensorManagerEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9b3b0b86-266a-4aad-b21f-fde5501001b7}')
    @commethod(3)
    def OnSensorEnter(self, pSensor: Windows.Win32.Devices.Sensors.ISensor_head, state: Windows.Win32.Devices.Sensors.SensorState) -> Windows.Win32.Foundation.HRESULT: ...
LOCATION_DESIRED_ACCURACY = Int32
LOCATION_DESIRED_ACCURACY_DEFAULT: LOCATION_DESIRED_ACCURACY = 0
LOCATION_DESIRED_ACCURACY_HIGH: LOCATION_DESIRED_ACCURACY = 1
LOCATION_POSITION_SOURCE = Int32
LOCATION_POSITION_SOURCE_CELLULAR: LOCATION_POSITION_SOURCE = 0
LOCATION_POSITION_SOURCE_SATELLITE: LOCATION_POSITION_SOURCE = 1
LOCATION_POSITION_SOURCE_WIFI: LOCATION_POSITION_SOURCE = 2
LOCATION_POSITION_SOURCE_IPADDRESS: LOCATION_POSITION_SOURCE = 3
LOCATION_POSITION_SOURCE_UNKNOWN: LOCATION_POSITION_SOURCE = 4
MAGNETOMETER_ACCURACY = Int32
MagnetometerAccuracy_Unknown: MAGNETOMETER_ACCURACY = 0
MagnetometerAccuracy_Unreliable: MAGNETOMETER_ACCURACY = 1
MagnetometerAccuracy_Approximate: MAGNETOMETER_ACCURACY = 2
MagnetometerAccuracy_High: MAGNETOMETER_ACCURACY = 3
class MATRIX3X3(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous1: _Anonymous1_e__Struct
        Anonymous2: _Anonymous2_e__Struct
        M: Single * 9
        class _Anonymous1_e__Struct(EasyCastStructure):
            A11: Single
            A12: Single
            A13: Single
            A21: Single
            A22: Single
            A23: Single
            A31: Single
            A32: Single
            A33: Single
        class _Anonymous2_e__Struct(EasyCastStructure):
            V1: Windows.Win32.Devices.Sensors.VEC3D
            V2: Windows.Win32.Devices.Sensors.VEC3D
            V3: Windows.Win32.Devices.Sensors.VEC3D
MagnetometerAccuracy = Int32
MAGNETOMETER_ACCURACY_UNKNOWN: MagnetometerAccuracy = 0
MAGNETOMETER_ACCURACY_UNRELIABLE: MagnetometerAccuracy = 1
MAGNETOMETER_ACCURACY_APPROXIMATE: MagnetometerAccuracy = 2
MAGNETOMETER_ACCURACY_HIGH: MagnetometerAccuracy = 3
PEDOMETER_STEP_TYPE = Int32
PedometerStepType_Unknown: PEDOMETER_STEP_TYPE = 1
PedometerStepType_Walking: PEDOMETER_STEP_TYPE = 2
PedometerStepType_Running: PEDOMETER_STEP_TYPE = 4
PedometerStepType_Max: PEDOMETER_STEP_TYPE = 8
PedometerStepType_Force_Dword: PEDOMETER_STEP_TYPE = -1
PEDOMETER_STEP_TYPE_COUNT = Int32
PEDOMETER_STEP_TYPE_COUNT_PedometerStepTypeCount: PEDOMETER_STEP_TYPE_COUNT = 3
PROXIMITY_SENSOR_CAPABILITIES = Int32
Proximity_Sensor_Human_Presence_Capable: PROXIMITY_SENSOR_CAPABILITIES = 1
Proximity_Sensor_Human_Engagement_Capable: PROXIMITY_SENSOR_CAPABILITIES = 2
Proximity_Sensor_Supported_Capabilities: PROXIMITY_SENSOR_CAPABILITIES = 3
PROXIMITY_TYPE = Int32
ProximityType_ObjectProximity: PROXIMITY_TYPE = 0
ProximityType_HumanProximity: PROXIMITY_TYPE = 1
ProximityType_Force_Dword: PROXIMITY_TYPE = -1
class QUATERNION(EasyCastStructure):
    X: Single
    Y: Single
    Z: Single
    W: Single
class SENSOR_COLLECTION_LIST(EasyCastStructure):
    AllocatedSizeInBytes: UInt32
    Count: UInt32
    List: Windows.Win32.Devices.Sensors.SENSOR_VALUE_PAIR * 1
SENSOR_CONNECTION_TYPES = Int32
SensorConnectionType_Integrated: SENSOR_CONNECTION_TYPES = 0
SensorConnectionType_Attached: SENSOR_CONNECTION_TYPES = 1
SensorConnectionType_External: SENSOR_CONNECTION_TYPES = 2
class SENSOR_PROPERTY_LIST(EasyCastStructure):
    AllocatedSizeInBytes: UInt32
    Count: UInt32
    List: Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY * 1
SENSOR_STATE = Int32
SensorState_Initializing: SENSOR_STATE = 0
SensorState_Idle: SENSOR_STATE = 1
SensorState_Active: SENSOR_STATE = 2
SensorState_Error: SENSOR_STATE = 3
class SENSOR_VALUE_PAIR(EasyCastStructure):
    Key: Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY
    Value: Windows.Win32.System.Com.StructuredStorage.PROPVARIANT
SIMPLE_DEVICE_ORIENTATION = Int32
SimpleDeviceOrientation_NotRotated: SIMPLE_DEVICE_ORIENTATION = 0
SimpleDeviceOrientation_Rotated90DegreesCounterclockwise: SIMPLE_DEVICE_ORIENTATION = 1
SimpleDeviceOrientation_Rotated180DegreesCounterclockwise: SIMPLE_DEVICE_ORIENTATION = 2
SimpleDeviceOrientation_Rotated270DegreesCounterclockwise: SIMPLE_DEVICE_ORIENTATION = 3
SimpleDeviceOrientation_Faceup: SIMPLE_DEVICE_ORIENTATION = 4
SimpleDeviceOrientation_Facedown: SIMPLE_DEVICE_ORIENTATION = 5
Sensor = Guid('{e97ced00-523a-4133-bf6f-d3a2dae7f6ba}')
SensorCollection = Guid('{79c43adb-a429-469f-aa39-2f2b74b75937}')
SensorConnectionType = Int32
SENSOR_CONNECTION_TYPE_PC_INTEGRATED: SensorConnectionType = 0
SENSOR_CONNECTION_TYPE_PC_ATTACHED: SensorConnectionType = 1
SENSOR_CONNECTION_TYPE_PC_EXTERNAL: SensorConnectionType = 2
SensorDataReport = Guid('{4ea9d6ef-694b-4218-8816-ccda8da74bba}')
SensorManager = Guid('{77a1c827-fcd2-4689-8915-9d613cc5fa3e}')
SensorState = Int32
SENSOR_STATE_MIN: SensorState = 0
SENSOR_STATE_READY: SensorState = 0
SENSOR_STATE_NOT_AVAILABLE: SensorState = 1
SENSOR_STATE_NO_DATA: SensorState = 2
SENSOR_STATE_INITIALIZING: SensorState = 3
SENSOR_STATE_ACCESS_DENIED: SensorState = 4
SENSOR_STATE_ERROR: SensorState = 5
SENSOR_STATE_MAX: SensorState = 5
SimpleDeviceOrientation = Int32
SIMPLE_DEVICE_ORIENTATION_NOT_ROTATED: SimpleDeviceOrientation = 0
SIMPLE_DEVICE_ORIENTATION_ROTATED_90: SimpleDeviceOrientation = 1
SIMPLE_DEVICE_ORIENTATION_ROTATED_180: SimpleDeviceOrientation = 2
SIMPLE_DEVICE_ORIENTATION_ROTATED_270: SimpleDeviceOrientation = 3
SIMPLE_DEVICE_ORIENTATION_ROTATED_FACE_UP: SimpleDeviceOrientation = 4
SIMPLE_DEVICE_ORIENTATION_ROTATED_FACE_DOWN: SimpleDeviceOrientation = 5
class VEC3D(EasyCastStructure):
    X: Single
    Y: Single
    Z: Single
make_head(_module, 'SENSOR_EVENT_PARAMETER_EVENT_ID')
make_head(_module, 'SENSOR_EVENT_PARAMETER_STATE')
make_head(_module, 'SENSOR_PROPERTY_TYPE')
make_head(_module, 'SENSOR_PROPERTY_STATE')
make_head(_module, 'SENSOR_PROPERTY_PERSISTENT_UNIQUE_ID')
make_head(_module, 'SENSOR_PROPERTY_MANUFACTURER')
make_head(_module, 'SENSOR_PROPERTY_MODEL')
make_head(_module, 'SENSOR_PROPERTY_SERIAL_NUMBER')
make_head(_module, 'SENSOR_PROPERTY_FRIENDLY_NAME')
make_head(_module, 'SENSOR_PROPERTY_DESCRIPTION')
make_head(_module, 'SENSOR_PROPERTY_CONNECTION_TYPE')
make_head(_module, 'SENSOR_PROPERTY_MIN_REPORT_INTERVAL')
make_head(_module, 'SENSOR_PROPERTY_CURRENT_REPORT_INTERVAL')
make_head(_module, 'SENSOR_PROPERTY_CHANGE_SENSITIVITY')
make_head(_module, 'SENSOR_PROPERTY_DEVICE_PATH')
make_head(_module, 'SENSOR_PROPERTY_LIGHT_RESPONSE_CURVE')
make_head(_module, 'SENSOR_PROPERTY_ACCURACY')
make_head(_module, 'SENSOR_PROPERTY_RESOLUTION')
make_head(_module, 'SENSOR_PROPERTY_LOCATION_DESIRED_ACCURACY')
make_head(_module, 'SENSOR_PROPERTY_RANGE_MINIMUM')
make_head(_module, 'SENSOR_PROPERTY_RANGE_MAXIMUM')
make_head(_module, 'SENSOR_PROPERTY_HID_USAGE')
make_head(_module, 'SENSOR_PROPERTY_RADIO_STATE')
make_head(_module, 'SENSOR_PROPERTY_RADIO_STATE_PREVIOUS')
make_head(_module, 'SENSOR_DATA_TYPE_TIMESTAMP')
make_head(_module, 'SENSOR_DATA_TYPE_LATITUDE_DEGREES')
make_head(_module, 'SENSOR_DATA_TYPE_LONGITUDE_DEGREES')
make_head(_module, 'SENSOR_DATA_TYPE_ALTITUDE_SEALEVEL_METERS')
make_head(_module, 'SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_METERS')
make_head(_module, 'SENSOR_DATA_TYPE_SPEED_KNOTS')
make_head(_module, 'SENSOR_DATA_TYPE_TRUE_HEADING_DEGREES')
make_head(_module, 'SENSOR_DATA_TYPE_MAGNETIC_HEADING_DEGREES')
make_head(_module, 'SENSOR_DATA_TYPE_MAGNETIC_VARIATION')
make_head(_module, 'SENSOR_DATA_TYPE_FIX_QUALITY')
make_head(_module, 'SENSOR_DATA_TYPE_FIX_TYPE')
make_head(_module, 'SENSOR_DATA_TYPE_POSITION_DILUTION_OF_PRECISION')
make_head(_module, 'SENSOR_DATA_TYPE_HORIZONAL_DILUTION_OF_PRECISION')
make_head(_module, 'SENSOR_DATA_TYPE_VERTICAL_DILUTION_OF_PRECISION')
make_head(_module, 'SENSOR_DATA_TYPE_SATELLITES_USED_COUNT')
make_head(_module, 'SENSOR_DATA_TYPE_SATELLITES_USED_PRNS')
make_head(_module, 'SENSOR_DATA_TYPE_SATELLITES_IN_VIEW')
make_head(_module, 'SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_PRNS')
make_head(_module, 'SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_ELEVATION')
make_head(_module, 'SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_AZIMUTH')
make_head(_module, 'SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_STN_RATIO')
make_head(_module, 'SENSOR_DATA_TYPE_ERROR_RADIUS_METERS')
make_head(_module, 'SENSOR_DATA_TYPE_ADDRESS1')
make_head(_module, 'SENSOR_DATA_TYPE_ADDRESS2')
make_head(_module, 'SENSOR_DATA_TYPE_CITY')
make_head(_module, 'SENSOR_DATA_TYPE_STATE_PROVINCE')
make_head(_module, 'SENSOR_DATA_TYPE_POSTALCODE')
make_head(_module, 'SENSOR_DATA_TYPE_COUNTRY_REGION')
make_head(_module, 'SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_ERROR_METERS')
make_head(_module, 'SENSOR_DATA_TYPE_ALTITUDE_SEALEVEL_ERROR_METERS')
make_head(_module, 'SENSOR_DATA_TYPE_GPS_SELECTION_MODE')
make_head(_module, 'SENSOR_DATA_TYPE_GPS_OPERATION_MODE')
make_head(_module, 'SENSOR_DATA_TYPE_GPS_STATUS')
make_head(_module, 'SENSOR_DATA_TYPE_GEOIDAL_SEPARATION')
make_head(_module, 'SENSOR_DATA_TYPE_DGPS_DATA_AGE')
make_head(_module, 'SENSOR_DATA_TYPE_ALTITUDE_ANTENNA_SEALEVEL_METERS')
make_head(_module, 'SENSOR_DATA_TYPE_DIFFERENTIAL_REFERENCE_STATION_ID')
make_head(_module, 'SENSOR_DATA_TYPE_NMEA_SENTENCE')
make_head(_module, 'SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_ID')
make_head(_module, 'SENSOR_DATA_TYPE_LOCATION_SOURCE')
make_head(_module, 'SENSOR_DATA_TYPE_SATELLITES_USED_PRNS_AND_CONSTELLATIONS')
make_head(_module, 'SENSOR_DATA_TYPE_TEMPERATURE_CELSIUS')
make_head(_module, 'SENSOR_DATA_TYPE_RELATIVE_HUMIDITY_PERCENT')
make_head(_module, 'SENSOR_DATA_TYPE_ATMOSPHERIC_PRESSURE_BAR')
make_head(_module, 'SENSOR_DATA_TYPE_WIND_DIRECTION_DEGREES_ANTICLOCKWISE')
make_head(_module, 'SENSOR_DATA_TYPE_WIND_SPEED_METERS_PER_SECOND')
make_head(_module, 'SENSOR_DATA_TYPE_ACCELERATION_X_G')
make_head(_module, 'SENSOR_DATA_TYPE_ACCELERATION_Y_G')
make_head(_module, 'SENSOR_DATA_TYPE_ACCELERATION_Z_G')
make_head(_module, 'SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_X_DEGREES_PER_SECOND_SQUARED')
make_head(_module, 'SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_Y_DEGREES_PER_SECOND_SQUARED')
make_head(_module, 'SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_Z_DEGREES_PER_SECOND_SQUARED')
make_head(_module, 'SENSOR_DATA_TYPE_SPEED_METERS_PER_SECOND')
make_head(_module, 'SENSOR_DATA_TYPE_MOTION_STATE')
make_head(_module, 'SENSOR_DATA_TYPE_ANGULAR_VELOCITY_X_DEGREES_PER_SECOND')
make_head(_module, 'SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Y_DEGREES_PER_SECOND')
make_head(_module, 'SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Z_DEGREES_PER_SECOND')
make_head(_module, 'SENSOR_DATA_TYPE_TILT_X_DEGREES')
make_head(_module, 'SENSOR_DATA_TYPE_TILT_Y_DEGREES')
make_head(_module, 'SENSOR_DATA_TYPE_TILT_Z_DEGREES')
make_head(_module, 'SENSOR_DATA_TYPE_MAGNETIC_HEADING_X_DEGREES')
make_head(_module, 'SENSOR_DATA_TYPE_MAGNETIC_HEADING_Y_DEGREES')
make_head(_module, 'SENSOR_DATA_TYPE_MAGNETIC_HEADING_Z_DEGREES')
make_head(_module, 'SENSOR_DATA_TYPE_DISTANCE_X_METERS')
make_head(_module, 'SENSOR_DATA_TYPE_DISTANCE_Y_METERS')
make_head(_module, 'SENSOR_DATA_TYPE_DISTANCE_Z_METERS')
make_head(_module, 'SENSOR_DATA_TYPE_MAGNETIC_HEADING_COMPENSATED_MAGNETIC_NORTH_DEGREES')
make_head(_module, 'SENSOR_DATA_TYPE_MAGNETIC_HEADING_COMPENSATED_TRUE_NORTH_DEGREES')
make_head(_module, 'SENSOR_DATA_TYPE_MAGNETIC_HEADING_MAGNETIC_NORTH_DEGREES')
make_head(_module, 'SENSOR_DATA_TYPE_MAGNETIC_HEADING_TRUE_NORTH_DEGREES')
make_head(_module, 'SENSOR_DATA_TYPE_QUADRANT_ANGLE_DEGREES')
make_head(_module, 'SENSOR_DATA_TYPE_ROTATION_MATRIX')
make_head(_module, 'SENSOR_DATA_TYPE_QUATERNION')
make_head(_module, 'SENSOR_DATA_TYPE_SIMPLE_DEVICE_ORIENTATION')
make_head(_module, 'SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_X_MILLIGAUSS')
make_head(_module, 'SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_Y_MILLIGAUSS')
make_head(_module, 'SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_Z_MILLIGAUSS')
make_head(_module, 'SENSOR_DATA_TYPE_MAGNETOMETER_ACCURACY')
make_head(_module, 'SENSOR_DATA_TYPE_BOOLEAN_SWITCH_STATE')
make_head(_module, 'SENSOR_DATA_TYPE_MULTIVALUE_SWITCH_STATE')
make_head(_module, 'SENSOR_DATA_TYPE_FORCE_NEWTONS')
make_head(_module, 'SENSOR_DATA_TYPE_ABSOLUTE_PRESSURE_PASCAL')
make_head(_module, 'SENSOR_DATA_TYPE_GAUGE_PRESSURE_PASCAL')
make_head(_module, 'SENSOR_DATA_TYPE_STRAIN')
make_head(_module, 'SENSOR_DATA_TYPE_WEIGHT_KILOGRAMS')
make_head(_module, 'SENSOR_DATA_TYPE_BOOLEAN_SWITCH_ARRAY_STATES')
make_head(_module, 'SENSOR_DATA_TYPE_HUMAN_PRESENCE')
make_head(_module, 'SENSOR_DATA_TYPE_HUMAN_PROXIMITY_METERS')
make_head(_module, 'SENSOR_DATA_TYPE_TOUCH_STATE')
make_head(_module, 'SENSOR_DATA_TYPE_LIGHT_LEVEL_LUX')
make_head(_module, 'SENSOR_DATA_TYPE_LIGHT_TEMPERATURE_KELVIN')
make_head(_module, 'SENSOR_DATA_TYPE_LIGHT_CHROMACITY')
make_head(_module, 'SENSOR_DATA_TYPE_RFID_TAG_40_BIT')
make_head(_module, 'SENSOR_DATA_TYPE_VOLTAGE_VOLTS')
make_head(_module, 'SENSOR_DATA_TYPE_CURRENT_AMPS')
make_head(_module, 'SENSOR_DATA_TYPE_CAPACITANCE_FARAD')
make_head(_module, 'SENSOR_DATA_TYPE_RESISTANCE_OHMS')
make_head(_module, 'SENSOR_DATA_TYPE_INDUCTANCE_HENRY')
make_head(_module, 'SENSOR_DATA_TYPE_ELECTRICAL_POWER_WATTS')
make_head(_module, 'SENSOR_DATA_TYPE_ELECTRICAL_PERCENT_OF_RANGE')
make_head(_module, 'SENSOR_DATA_TYPE_ELECTRICAL_FREQUENCY_HERTZ')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_USAGE')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_BOOLEAN_ARRAY')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE1')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE2')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE3')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE4')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE5')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE6')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE7')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE8')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE9')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE10')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE11')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE12')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE13')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE14')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE15')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE16')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE17')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE18')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE19')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE20')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE21')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE22')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE23')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE24')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE25')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE26')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE27')
make_head(_module, 'SENSOR_DATA_TYPE_CUSTOM_VALUE28')
make_head(_module, 'SENSOR_PROPERTY_CLEAR_ASSISTANCE_DATA')
make_head(_module, 'SENSOR_PROPERTY_TURN_ON_OFF_NMEA')
make_head(_module, 'ILocationPermissions')
make_head(_module, 'ISensor')
make_head(_module, 'ISensorCollection')
make_head(_module, 'ISensorDataReport')
make_head(_module, 'ISensorEvents')
make_head(_module, 'ISensorManager')
make_head(_module, 'ISensorManagerEvents')
make_head(_module, 'MATRIX3X3')
make_head(_module, 'QUATERNION')
make_head(_module, 'SENSOR_COLLECTION_LIST')
make_head(_module, 'SENSOR_PROPERTY_LIST')
make_head(_module, 'SENSOR_VALUE_PAIR')
make_head(_module, 'VEC3D')
