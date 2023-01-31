from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Devices.PortableDevices
import win32more.Devices.Sensors
import win32more.Foundation
import win32more.System.Com
import win32more.System.Com.StructuredStorage
import win32more.UI.Shell.PropertiesSystem
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
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
GUID_DEVINTERFACE_SENSOR: Guid = Guid('ba1bb692-9b7a-4833-9a-1e-52-5e-d1-34-e7-e2')
SENSOR_EVENT_STATE_CHANGED: Guid = Guid('bfd96016-6bd7-4560-ad-34-f2-f6-60-7e-8f-81')
SENSOR_EVENT_DATA_UPDATED: Guid = Guid('2ed0f2a4-0087-41d3-87-db-67-73-37-0b-3c-88')
SENSOR_EVENT_PROPERTY_CHANGED: Guid = Guid('2358f099-84c9-4d3d-90-df-c2-42-1e-2b-20-45')
SENSOR_EVENT_ACCELEROMETER_SHAKE: Guid = Guid('825f5a94-0f48-4396-9c-a0-6e-cb-5c-99-d9-15')
SENSOR_EVENT_PARAMETER_COMMON_GUID: Guid = Guid('64346e30-8728-4b34-bd-f6-4f-52-44-2c-5c-28')
def SENSOR_EVENT_PARAMETER_EVENT_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64346e30-8728-4b34-bd-f6-4f-52-44-2c-5c-28'), pid=2)
def SENSOR_EVENT_PARAMETER_STATE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64346e30-8728-4b34-bd-f6-4f-52-44-2c-5c-28'), pid=3)
SENSOR_ERROR_PARAMETER_COMMON_GUID: Guid = Guid('77112bcd-fce1-4f43-b8-b8-a8-82-56-ad-b4-b3')
SENSOR_PROPERTY_COMMON_GUID: Guid = Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20')
def SENSOR_PROPERTY_TYPE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=2)
def SENSOR_PROPERTY_STATE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=3)
def SENSOR_PROPERTY_PERSISTENT_UNIQUE_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=5)
def SENSOR_PROPERTY_MANUFACTURER():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=6)
def SENSOR_PROPERTY_MODEL():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=7)
def SENSOR_PROPERTY_SERIAL_NUMBER():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=8)
def SENSOR_PROPERTY_FRIENDLY_NAME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=9)
def SENSOR_PROPERTY_DESCRIPTION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=10)
def SENSOR_PROPERTY_CONNECTION_TYPE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=11)
def SENSOR_PROPERTY_MIN_REPORT_INTERVAL():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=12)
def SENSOR_PROPERTY_CURRENT_REPORT_INTERVAL():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=13)
def SENSOR_PROPERTY_CHANGE_SENSITIVITY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=14)
def SENSOR_PROPERTY_DEVICE_PATH():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=15)
def SENSOR_PROPERTY_LIGHT_RESPONSE_CURVE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=16)
def SENSOR_PROPERTY_ACCURACY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=17)
def SENSOR_PROPERTY_RESOLUTION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=18)
def SENSOR_PROPERTY_LOCATION_DESIRED_ACCURACY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=19)
def SENSOR_PROPERTY_RANGE_MINIMUM():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=20)
def SENSOR_PROPERTY_RANGE_MAXIMUM():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=21)
def SENSOR_PROPERTY_HID_USAGE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=22)
def SENSOR_PROPERTY_RADIO_STATE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=23)
def SENSOR_PROPERTY_RADIO_STATE_PREVIOUS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=24)
SENSOR_CATEGORY_ALL: Guid = Guid('c317c286-c468-4288-99-75-d4-c4-58-7c-44-2c')
SENSOR_CATEGORY_LOCATION: Guid = Guid('bfa794e4-f964-4fdb-90-f6-51-05-6b-fe-4b-44')
SENSOR_CATEGORY_ENVIRONMENTAL: Guid = Guid('323439aa-7f66-492b-ba-0c-73-e9-aa-0a-65-d5')
SENSOR_CATEGORY_MOTION: Guid = Guid('cd09daf1-3b2e-4c3d-b5-98-b5-e5-ff-93-fd-46')
SENSOR_CATEGORY_ORIENTATION: Guid = Guid('9e6c04b6-96fe-4954-b7-26-68-68-2a-47-3f-69')
SENSOR_CATEGORY_MECHANICAL: Guid = Guid('8d131d68-8ef7-4656-80-b5-cc-cb-d9-37-91-c5')
SENSOR_CATEGORY_ELECTRICAL: Guid = Guid('fb73fcd8-fc4a-483c-ac-58-27-b6-91-c6-be-ff')
SENSOR_CATEGORY_BIOMETRIC: Guid = Guid('ca19690f-a2c7-477d-a9-9e-99-ec-6e-2b-56-48')
SENSOR_CATEGORY_LIGHT: Guid = Guid('17a665c0-9063-4216-b2-02-5c-7a-25-5e-18-ce')
SENSOR_CATEGORY_SCANNER: Guid = Guid('b000e77e-f5b5-420f-81-5d-02-70-a7-26-f2-70')
SENSOR_CATEGORY_OTHER: Guid = Guid('2c90e7a9-f4c9-4fa2-af-37-56-d4-71-fe-5a-3d')
SENSOR_CATEGORY_UNSUPPORTED: Guid = Guid('2beae7fa-19b0-48c5-a1-f6-b5-48-0d-c2-06-b0')
SENSOR_TYPE_LOCATION_GPS: Guid = Guid('ed4ca589-327a-4ff9-a5-60-91-da-4b-48-27-5e')
SENSOR_TYPE_LOCATION_STATIC: Guid = Guid('095f8184-0fa9-4445-8e-6e-b7-0f-32-0b-6b-4c')
SENSOR_TYPE_LOCATION_LOOKUP: Guid = Guid('3b2eae4a-72ce-436d-96-d2-3c-5b-85-70-e9-87')
SENSOR_TYPE_LOCATION_TRIANGULATION: Guid = Guid('691c341a-5406-4fe1-94-2f-22-46-cb-eb-39-e0')
SENSOR_TYPE_LOCATION_OTHER: Guid = Guid('9b2d0566-0368-4f71-b8-8d-53-3f-13-20-31-de')
SENSOR_TYPE_LOCATION_BROADCAST: Guid = Guid('d26988cf-5162-4039-bb-17-4c-58-b6-98-e4-4a')
SENSOR_TYPE_LOCATION_DEAD_RECKONING: Guid = Guid('1a37d538-f28b-42da-9f-ce-a9-d0-a2-a6-d8-29')
SENSOR_TYPE_ENVIRONMENTAL_TEMPERATURE: Guid = Guid('04fd0ec4-d5da-45fa-95-a9-5d-b3-8e-e1-93-06')
SENSOR_TYPE_ENVIRONMENTAL_ATMOSPHERIC_PRESSURE: Guid = Guid('0e903829-ff8a-4a93-97-df-3d-cb-de-40-22-88')
SENSOR_TYPE_ENVIRONMENTAL_HUMIDITY: Guid = Guid('5c72bf67-bd7e-4257-99-0b-98-a3-ba-3b-40-0a')
SENSOR_TYPE_ENVIRONMENTAL_WIND_SPEED: Guid = Guid('dd50607b-a45f-42cd-8e-fd-ec-61-76-1c-42-26')
SENSOR_TYPE_ENVIRONMENTAL_WIND_DIRECTION: Guid = Guid('9ef57a35-9306-434d-af-09-37-fa-5a-9c-00-bd')
SENSOR_TYPE_ACCELEROMETER_1D: Guid = Guid('c04d2387-7340-4cc2-99-1e-3b-18-cb-8e-f2-f4')
SENSOR_TYPE_ACCELEROMETER_2D: Guid = Guid('b2c517a8-f6b5-4ba6-a4-23-5d-f5-60-b4-cc-07')
SENSOR_TYPE_ACCELEROMETER_3D: Guid = Guid('c2fb0f5f-e2d2-4c78-bc-d0-35-2a-95-82-81-9d')
SENSOR_TYPE_MOTION_DETECTOR: Guid = Guid('5c7c1a12-30a5-43b9-a4-b2-cf-09-ec-5b-7b-e8')
SENSOR_TYPE_GYROMETER_1D: Guid = Guid('fa088734-f552-4584-83-24-ed-fa-f6-49-65-2c')
SENSOR_TYPE_GYROMETER_2D: Guid = Guid('31ef4f83-919b-48bf-8d-e0-5d-7a-9d-24-05-56')
SENSOR_TYPE_GYROMETER_3D: Guid = Guid('09485f5a-759e-42c2-bd-4b-a3-49-b7-5c-86-43')
SENSOR_TYPE_SPEEDOMETER: Guid = Guid('6bd73c1f-0bb4-4310-81-b2-df-c1-8a-52-bf-94')
SENSOR_TYPE_COMPASS_1D: Guid = Guid('a415f6c5-cb50-49d0-8e-62-a8-27-0b-d7-a2-6c')
SENSOR_TYPE_COMPASS_2D: Guid = Guid('15655cc0-997a-4d30-84-db-57-ca-ba-36-48-bb')
SENSOR_TYPE_COMPASS_3D: Guid = Guid('76b5ce0d-17dd-414d-93-a1-e1-27-f4-0b-df-6e')
SENSOR_TYPE_INCLINOMETER_1D: Guid = Guid('b96f98c5-7a75-4ba7-94-e9-ac-86-8c-96-6d-d8')
SENSOR_TYPE_INCLINOMETER_2D: Guid = Guid('ab140f6d-83eb-4264-b7-0b-b1-6a-5b-25-6a-01')
SENSOR_TYPE_INCLINOMETER_3D: Guid = Guid('b84919fb-ea85-4976-84-44-6f-6f-5c-6d-31-db')
SENSOR_TYPE_DISTANCE_1D: Guid = Guid('5f14ab2f-1407-4306-a9-3f-b1-db-ab-e4-f9-c0')
SENSOR_TYPE_DISTANCE_2D: Guid = Guid('5cf9a46c-a9a2-4e55-b6-a1-a0-4a-af-a9-5a-92')
SENSOR_TYPE_DISTANCE_3D: Guid = Guid('a20cae31-0e25-4772-9f-e5-96-60-8a-13-54-b2')
SENSOR_TYPE_AGGREGATED_QUADRANT_ORIENTATION: Guid = Guid('9f81f1af-c4ab-4307-99-04-c8-28-bf-b9-08-29')
SENSOR_TYPE_AGGREGATED_DEVICE_ORIENTATION: Guid = Guid('cdb5d8f7-3cfd-41c8-85-42-cc-e6-22-cf-5d-6e')
SENSOR_TYPE_AGGREGATED_SIMPLE_DEVICE_ORIENTATION: Guid = Guid('86a19291-0482-402c-bf-4c-ad-da-c5-2b-1c-39')
SENSOR_TYPE_VOLTAGE: Guid = Guid('c5484637-4fb7-4953-98-b8-a5-6d-8a-a1-fb-1e')
SENSOR_TYPE_CURRENT: Guid = Guid('5adc9fce-15a0-4bbe-a1-ad-2d-38-a9-ae-83-1c')
SENSOR_TYPE_CAPACITANCE: Guid = Guid('ca2ffb1c-2317-49c0-a0-b4-b6-3c-e6-34-61-a0')
SENSOR_TYPE_RESISTANCE: Guid = Guid('9993d2c8-c157-4a52-a7-b5-19-5c-76-03-72-31')
SENSOR_TYPE_INDUCTANCE: Guid = Guid('dc1d933f-c435-4c7d-a2-fe-60-71-92-a5-24-d3')
SENSOR_TYPE_ELECTRICAL_POWER: Guid = Guid('212f10f5-14ab-4376-9a-43-a7-79-40-98-c2-fe')
SENSOR_TYPE_POTENTIOMETER: Guid = Guid('2b3681a9-cadc-45aa-a6-ff-54-95-7c-8b-b4-40')
SENSOR_TYPE_FREQUENCY: Guid = Guid('8cd2cbb6-73e6-4640-a7-09-72-ae-8f-b6-0d-7f')
SENSOR_TYPE_BOOLEAN_SWITCH: Guid = Guid('9c7e371f-1041-460b-8d-5c-71-e4-75-2e-35-0c')
SENSOR_TYPE_MULTIVALUE_SWITCH: Guid = Guid('b3ee4d76-37a4-4402-b2-5e-99-c6-0a-77-5f-a1')
SENSOR_TYPE_FORCE: Guid = Guid('c2ab2b02-1a1c-4778-a8-1b-95-4a-17-88-cc-75')
SENSOR_TYPE_SCALE: Guid = Guid('c06dd92c-7feb-438e-9b-f6-82-20-7f-ff-5b-b8')
SENSOR_TYPE_PRESSURE: Guid = Guid('26d31f34-6352-41cf-b7-93-ea-07-13-d5-3d-77')
SENSOR_TYPE_STRAIN: Guid = Guid('c6d1ec0e-6803-4361-ad-3d-85-bc-c5-8c-6d-29')
SENSOR_TYPE_BOOLEAN_SWITCH_ARRAY: Guid = Guid('545c8ba5-b143-4545-86-8f-ca-7f-d9-86-b4-f6')
SENSOR_TYPE_HUMAN_PRESENCE: Guid = Guid('c138c12b-ad52-451c-93-75-87-f5-18-ff-10-c6')
SENSOR_TYPE_HUMAN_PROXIMITY: Guid = Guid('5220dae9-3179-4430-9f-90-06-26-6d-2a-34-de')
SENSOR_TYPE_TOUCH: Guid = Guid('17db3018-06c4-4f7d-81-af-92-74-b7-59-9c-27')
SENSOR_TYPE_AMBIENT_LIGHT: Guid = Guid('97f115c8-599a-4153-88-94-d2-d1-28-99-91-8a')
SENSOR_TYPE_RFID_SCANNER: Guid = Guid('44328ef5-02dd-4e8d-ad-5d-92-49-83-2b-2e-ca')
SENSOR_TYPE_BARCODE_SCANNER: Guid = Guid('990b3d8f-85bb-45ff-91-4d-99-8c-04-f3-72-df')
SENSOR_TYPE_CUSTOM: Guid = Guid('e83af229-8640-4d18-a2-13-e2-26-75-eb-b2-c3')
SENSOR_TYPE_UNKNOWN: Guid = Guid('10ba83e3-ef4f-41ed-98-85-a8-7d-64-35-a8-e1')
SENSOR_DATA_TYPE_COMMON_GUID: Guid = Guid('db5e0cf2-cf1f-4c18-b4-6c-d8-60-11-d6-21-50')
def SENSOR_DATA_TYPE_TIMESTAMP():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('db5e0cf2-cf1f-4c18-b4-6c-d8-60-11-d6-21-50'), pid=2)
SENSOR_DATA_TYPE_LOCATION_GUID: Guid = Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4')
def SENSOR_DATA_TYPE_LATITUDE_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=2)
def SENSOR_DATA_TYPE_LONGITUDE_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=3)
def SENSOR_DATA_TYPE_ALTITUDE_SEALEVEL_METERS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=4)
def SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_METERS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=5)
def SENSOR_DATA_TYPE_SPEED_KNOTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=6)
def SENSOR_DATA_TYPE_TRUE_HEADING_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=7)
def SENSOR_DATA_TYPE_MAGNETIC_HEADING_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=8)
def SENSOR_DATA_TYPE_MAGNETIC_VARIATION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=9)
def SENSOR_DATA_TYPE_FIX_QUALITY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=10)
def SENSOR_DATA_TYPE_FIX_TYPE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=11)
def SENSOR_DATA_TYPE_POSITION_DILUTION_OF_PRECISION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=12)
def SENSOR_DATA_TYPE_HORIZONAL_DILUTION_OF_PRECISION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=13)
def SENSOR_DATA_TYPE_VERTICAL_DILUTION_OF_PRECISION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=14)
def SENSOR_DATA_TYPE_SATELLITES_USED_COUNT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=15)
def SENSOR_DATA_TYPE_SATELLITES_USED_PRNS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=16)
def SENSOR_DATA_TYPE_SATELLITES_IN_VIEW():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=17)
def SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_PRNS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=18)
def SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_ELEVATION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=19)
def SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_AZIMUTH():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=20)
def SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_STN_RATIO():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=21)
def SENSOR_DATA_TYPE_ERROR_RADIUS_METERS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=22)
def SENSOR_DATA_TYPE_ADDRESS1():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=23)
def SENSOR_DATA_TYPE_ADDRESS2():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=24)
def SENSOR_DATA_TYPE_CITY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=25)
def SENSOR_DATA_TYPE_STATE_PROVINCE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=26)
def SENSOR_DATA_TYPE_POSTALCODE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=27)
def SENSOR_DATA_TYPE_COUNTRY_REGION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=28)
def SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_ERROR_METERS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=29)
def SENSOR_DATA_TYPE_ALTITUDE_SEALEVEL_ERROR_METERS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=30)
def SENSOR_DATA_TYPE_GPS_SELECTION_MODE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=31)
def SENSOR_DATA_TYPE_GPS_OPERATION_MODE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=32)
def SENSOR_DATA_TYPE_GPS_STATUS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=33)
def SENSOR_DATA_TYPE_GEOIDAL_SEPARATION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=34)
def SENSOR_DATA_TYPE_DGPS_DATA_AGE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=35)
def SENSOR_DATA_TYPE_ALTITUDE_ANTENNA_SEALEVEL_METERS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=36)
def SENSOR_DATA_TYPE_DIFFERENTIAL_REFERENCE_STATION_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=37)
def SENSOR_DATA_TYPE_NMEA_SENTENCE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=38)
def SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=39)
def SENSOR_DATA_TYPE_LOCATION_SOURCE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=40)
def SENSOR_DATA_TYPE_SATELLITES_USED_PRNS_AND_CONSTELLATIONS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=41)
SENSOR_DATA_TYPE_ENVIRONMENTAL_GUID: Guid = Guid('8b0aa2f1-2d57-42ee-8c-c0-4d-27-62-2b-46-c4')
def SENSOR_DATA_TYPE_TEMPERATURE_CELSIUS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8b0aa2f1-2d57-42ee-8c-c0-4d-27-62-2b-46-c4'), pid=2)
def SENSOR_DATA_TYPE_RELATIVE_HUMIDITY_PERCENT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8b0aa2f1-2d57-42ee-8c-c0-4d-27-62-2b-46-c4'), pid=3)
def SENSOR_DATA_TYPE_ATMOSPHERIC_PRESSURE_BAR():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8b0aa2f1-2d57-42ee-8c-c0-4d-27-62-2b-46-c4'), pid=4)
def SENSOR_DATA_TYPE_WIND_DIRECTION_DEGREES_ANTICLOCKWISE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8b0aa2f1-2d57-42ee-8c-c0-4d-27-62-2b-46-c4'), pid=5)
def SENSOR_DATA_TYPE_WIND_SPEED_METERS_PER_SECOND():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8b0aa2f1-2d57-42ee-8c-c0-4d-27-62-2b-46-c4'), pid=6)
SENSOR_DATA_TYPE_MOTION_GUID: Guid = Guid('3f8a69a2-07c5-4e48-a9-65-cd-79-7a-ab-56-d5')
def SENSOR_DATA_TYPE_ACCELERATION_X_G():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3f8a69a2-07c5-4e48-a9-65-cd-79-7a-ab-56-d5'), pid=2)
def SENSOR_DATA_TYPE_ACCELERATION_Y_G():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3f8a69a2-07c5-4e48-a9-65-cd-79-7a-ab-56-d5'), pid=3)
def SENSOR_DATA_TYPE_ACCELERATION_Z_G():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3f8a69a2-07c5-4e48-a9-65-cd-79-7a-ab-56-d5'), pid=4)
def SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_X_DEGREES_PER_SECOND_SQUARED():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3f8a69a2-07c5-4e48-a9-65-cd-79-7a-ab-56-d5'), pid=5)
def SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_Y_DEGREES_PER_SECOND_SQUARED():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3f8a69a2-07c5-4e48-a9-65-cd-79-7a-ab-56-d5'), pid=6)
def SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_Z_DEGREES_PER_SECOND_SQUARED():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3f8a69a2-07c5-4e48-a9-65-cd-79-7a-ab-56-d5'), pid=7)
def SENSOR_DATA_TYPE_SPEED_METERS_PER_SECOND():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3f8a69a2-07c5-4e48-a9-65-cd-79-7a-ab-56-d5'), pid=8)
def SENSOR_DATA_TYPE_MOTION_STATE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3f8a69a2-07c5-4e48-a9-65-cd-79-7a-ab-56-d5'), pid=9)
def SENSOR_DATA_TYPE_ANGULAR_VELOCITY_X_DEGREES_PER_SECOND():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3f8a69a2-07c5-4e48-a9-65-cd-79-7a-ab-56-d5'), pid=10)
def SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Y_DEGREES_PER_SECOND():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3f8a69a2-07c5-4e48-a9-65-cd-79-7a-ab-56-d5'), pid=11)
def SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Z_DEGREES_PER_SECOND():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3f8a69a2-07c5-4e48-a9-65-cd-79-7a-ab-56-d5'), pid=12)
SENSOR_DATA_TYPE_ORIENTATION_GUID: Guid = Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd')
def SENSOR_DATA_TYPE_TILT_X_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=2)
def SENSOR_DATA_TYPE_TILT_Y_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=3)
def SENSOR_DATA_TYPE_TILT_Z_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=4)
def SENSOR_DATA_TYPE_MAGNETIC_HEADING_X_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=5)
def SENSOR_DATA_TYPE_MAGNETIC_HEADING_Y_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=6)
def SENSOR_DATA_TYPE_MAGNETIC_HEADING_Z_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=7)
def SENSOR_DATA_TYPE_DISTANCE_X_METERS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=8)
def SENSOR_DATA_TYPE_DISTANCE_Y_METERS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=9)
def SENSOR_DATA_TYPE_DISTANCE_Z_METERS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=10)
def SENSOR_DATA_TYPE_MAGNETIC_HEADING_COMPENSATED_MAGNETIC_NORTH_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=11)
def SENSOR_DATA_TYPE_MAGNETIC_HEADING_COMPENSATED_TRUE_NORTH_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=12)
def SENSOR_DATA_TYPE_MAGNETIC_HEADING_MAGNETIC_NORTH_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=13)
def SENSOR_DATA_TYPE_MAGNETIC_HEADING_TRUE_NORTH_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=14)
def SENSOR_DATA_TYPE_QUADRANT_ANGLE_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=15)
def SENSOR_DATA_TYPE_ROTATION_MATRIX():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=16)
def SENSOR_DATA_TYPE_QUATERNION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=17)
def SENSOR_DATA_TYPE_SIMPLE_DEVICE_ORIENTATION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=18)
def SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_X_MILLIGAUSS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=19)
def SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_Y_MILLIGAUSS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=20)
def SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_Z_MILLIGAUSS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=21)
def SENSOR_DATA_TYPE_MAGNETOMETER_ACCURACY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=22)
SENSOR_DATA_TYPE_GUID_MECHANICAL_GUID: Guid = Guid('38564a7c-f2f2-49bb-9b-2b-ba-60-f6-6a-58-df')
def SENSOR_DATA_TYPE_BOOLEAN_SWITCH_STATE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('38564a7c-f2f2-49bb-9b-2b-ba-60-f6-6a-58-df'), pid=2)
def SENSOR_DATA_TYPE_MULTIVALUE_SWITCH_STATE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('38564a7c-f2f2-49bb-9b-2b-ba-60-f6-6a-58-df'), pid=3)
def SENSOR_DATA_TYPE_FORCE_NEWTONS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('38564a7c-f2f2-49bb-9b-2b-ba-60-f6-6a-58-df'), pid=4)
def SENSOR_DATA_TYPE_ABSOLUTE_PRESSURE_PASCAL():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('38564a7c-f2f2-49bb-9b-2b-ba-60-f6-6a-58-df'), pid=5)
def SENSOR_DATA_TYPE_GAUGE_PRESSURE_PASCAL():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('38564a7c-f2f2-49bb-9b-2b-ba-60-f6-6a-58-df'), pid=6)
def SENSOR_DATA_TYPE_STRAIN():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('38564a7c-f2f2-49bb-9b-2b-ba-60-f6-6a-58-df'), pid=7)
def SENSOR_DATA_TYPE_WEIGHT_KILOGRAMS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('38564a7c-f2f2-49bb-9b-2b-ba-60-f6-6a-58-df'), pid=8)
def SENSOR_DATA_TYPE_BOOLEAN_SWITCH_ARRAY_STATES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('38564a7c-f2f2-49bb-9b-2b-ba-60-f6-6a-58-df'), pid=10)
SENSOR_DATA_TYPE_BIOMETRIC_GUID: Guid = Guid('2299288a-6d9e-4b0b-b7-ec-35-28-f8-9e-40-af')
def SENSOR_DATA_TYPE_HUMAN_PRESENCE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2299288a-6d9e-4b0b-b7-ec-35-28-f8-9e-40-af'), pid=2)
def SENSOR_DATA_TYPE_HUMAN_PROXIMITY_METERS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2299288a-6d9e-4b0b-b7-ec-35-28-f8-9e-40-af'), pid=3)
def SENSOR_DATA_TYPE_TOUCH_STATE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2299288a-6d9e-4b0b-b7-ec-35-28-f8-9e-40-af'), pid=4)
SENSOR_DATA_TYPE_LIGHT_GUID: Guid = Guid('e4c77ce2-dcb7-46e9-84-39-4f-ec-54-88-33-a6')
def SENSOR_DATA_TYPE_LIGHT_LEVEL_LUX():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e4c77ce2-dcb7-46e9-84-39-4f-ec-54-88-33-a6'), pid=2)
def SENSOR_DATA_TYPE_LIGHT_TEMPERATURE_KELVIN():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e4c77ce2-dcb7-46e9-84-39-4f-ec-54-88-33-a6'), pid=3)
def SENSOR_DATA_TYPE_LIGHT_CHROMACITY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e4c77ce2-dcb7-46e9-84-39-4f-ec-54-88-33-a6'), pid=4)
SENSOR_DATA_TYPE_SCANNER_GUID: Guid = Guid('d7a59a3c-3421-44ab-8d-3a-9d-e8-ab-6c-4c-ae')
def SENSOR_DATA_TYPE_RFID_TAG_40_BIT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d7a59a3c-3421-44ab-8d-3a-9d-e8-ab-6c-4c-ae'), pid=2)
SENSOR_DATA_TYPE_ELECTRICAL_GUID: Guid = Guid('bbb246d1-e242-4780-a2-d3-cd-ed-84-f3-58-42')
def SENSOR_DATA_TYPE_VOLTAGE_VOLTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bbb246d1-e242-4780-a2-d3-cd-ed-84-f3-58-42'), pid=2)
def SENSOR_DATA_TYPE_CURRENT_AMPS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bbb246d1-e242-4780-a2-d3-cd-ed-84-f3-58-42'), pid=3)
def SENSOR_DATA_TYPE_CAPACITANCE_FARAD():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bbb246d1-e242-4780-a2-d3-cd-ed-84-f3-58-42'), pid=4)
def SENSOR_DATA_TYPE_RESISTANCE_OHMS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bbb246d1-e242-4780-a2-d3-cd-ed-84-f3-58-42'), pid=5)
def SENSOR_DATA_TYPE_INDUCTANCE_HENRY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bbb246d1-e242-4780-a2-d3-cd-ed-84-f3-58-42'), pid=6)
def SENSOR_DATA_TYPE_ELECTRICAL_POWER_WATTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bbb246d1-e242-4780-a2-d3-cd-ed-84-f3-58-42'), pid=7)
def SENSOR_DATA_TYPE_ELECTRICAL_PERCENT_OF_RANGE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bbb246d1-e242-4780-a2-d3-cd-ed-84-f3-58-42'), pid=8)
def SENSOR_DATA_TYPE_ELECTRICAL_FREQUENCY_HERTZ():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bbb246d1-e242-4780-a2-d3-cd-ed-84-f3-58-42'), pid=9)
SENSOR_DATA_TYPE_CUSTOM_GUID: Guid = Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f')
def SENSOR_DATA_TYPE_CUSTOM_USAGE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=5)
def SENSOR_DATA_TYPE_CUSTOM_BOOLEAN_ARRAY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=6)
def SENSOR_DATA_TYPE_CUSTOM_VALUE1():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=7)
def SENSOR_DATA_TYPE_CUSTOM_VALUE2():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=8)
def SENSOR_DATA_TYPE_CUSTOM_VALUE3():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=9)
def SENSOR_DATA_TYPE_CUSTOM_VALUE4():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=10)
def SENSOR_DATA_TYPE_CUSTOM_VALUE5():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=11)
def SENSOR_DATA_TYPE_CUSTOM_VALUE6():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=12)
def SENSOR_DATA_TYPE_CUSTOM_VALUE7():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=13)
def SENSOR_DATA_TYPE_CUSTOM_VALUE8():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=14)
def SENSOR_DATA_TYPE_CUSTOM_VALUE9():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=15)
def SENSOR_DATA_TYPE_CUSTOM_VALUE10():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=16)
def SENSOR_DATA_TYPE_CUSTOM_VALUE11():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=17)
def SENSOR_DATA_TYPE_CUSTOM_VALUE12():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=18)
def SENSOR_DATA_TYPE_CUSTOM_VALUE13():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=19)
def SENSOR_DATA_TYPE_CUSTOM_VALUE14():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=20)
def SENSOR_DATA_TYPE_CUSTOM_VALUE15():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=21)
def SENSOR_DATA_TYPE_CUSTOM_VALUE16():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=22)
def SENSOR_DATA_TYPE_CUSTOM_VALUE17():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=23)
def SENSOR_DATA_TYPE_CUSTOM_VALUE18():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=24)
def SENSOR_DATA_TYPE_CUSTOM_VALUE19():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=25)
def SENSOR_DATA_TYPE_CUSTOM_VALUE20():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=26)
def SENSOR_DATA_TYPE_CUSTOM_VALUE21():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=27)
def SENSOR_DATA_TYPE_CUSTOM_VALUE22():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=28)
def SENSOR_DATA_TYPE_CUSTOM_VALUE23():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=29)
def SENSOR_DATA_TYPE_CUSTOM_VALUE24():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=30)
def SENSOR_DATA_TYPE_CUSTOM_VALUE25():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=31)
def SENSOR_DATA_TYPE_CUSTOM_VALUE26():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=32)
def SENSOR_DATA_TYPE_CUSTOM_VALUE27():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=33)
def SENSOR_DATA_TYPE_CUSTOM_VALUE28():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=34)
SENSOR_PROPERTY_TEST_GUID: Guid = Guid('e1e962f4-6e65-45f7-9c-36-d4-87-b7-b1-bd-34')
def SENSOR_PROPERTY_CLEAR_ASSISTANCE_DATA():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e1e962f4-6e65-45f7-9c-36-d4-87-b7-b1-bd-34'), pid=2)
def SENSOR_PROPERTY_TURN_ON_OFF_NMEA():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e1e962f4-6e65-45f7-9c-36-d4-87-b7-b1-bd-34'), pid=3)
GNSS_CLEAR_ALL_ASSISTANCE_DATA: UInt32 = 1
GUID_SensorCategory_All: Guid = Guid('c317c286-c468-4288-99-75-d4-c4-58-7c-44-2c')
GUID_SensorCategory_Biometric: Guid = Guid('ca19690f-a2c7-477d-a9-9e-99-ec-6e-2b-56-48')
GUID_SensorCategory_Electrical: Guid = Guid('fb73fcd8-fc4a-483c-ac-58-27-b6-91-c6-be-ff')
GUID_SensorCategory_Environmental: Guid = Guid('323439aa-7f66-492b-ba-0c-73-e9-aa-0a-65-d5')
GUID_SensorCategory_Light: Guid = Guid('17a665c0-9063-4216-b2-02-5c-7a-25-5e-18-ce')
GUID_SensorCategory_Location: Guid = Guid('bfa794e4-f964-4fdb-90-f6-51-05-6b-fe-4b-44')
GUID_SensorCategory_Mechanical: Guid = Guid('8d131d68-8ef7-4656-80-b5-cc-cb-d9-37-91-c5')
GUID_SensorCategory_Motion: Guid = Guid('cd09daf1-3b2e-4c3d-b5-98-b5-e5-ff-93-fd-46')
GUID_SensorCategory_Orientation: Guid = Guid('9e6c04b6-96fe-4954-b7-26-68-68-2a-47-3f-69')
GUID_SensorCategory_Other: Guid = Guid('2c90e7a9-f4c9-4fa2-af-37-56-d4-71-fe-5a-3d')
GUID_SensorCategory_PersonalActivity: Guid = Guid('f1609081-1e12-412b-a1-4d-cb-b0-e9-5b-d2-e5')
GUID_SensorCategory_Scanner: Guid = Guid('b000e77e-f5b5-420f-81-5d-02-70-a7-26-f2-70')
GUID_SensorCategory_Unsupported: Guid = Guid('2beae7fa-19b0-48c5-a1-f6-b5-48-0d-c2-06-b0')
GUID_SensorType_Accelerometer3D: Guid = Guid('c2fb0f5f-e2d2-4c78-bc-d0-35-2a-95-82-81-9d')
GUID_SensorType_ActivityDetection: Guid = Guid('9d9e0118-1807-4f2e-96-e4-2c-e5-71-42-e1-96')
GUID_SensorType_AmbientLight: Guid = Guid('97f115c8-599a-4153-88-94-d2-d1-28-99-91-8a')
GUID_SensorType_Barometer: Guid = Guid('0e903829-ff8a-4a93-97-df-3d-cb-de-40-22-88')
GUID_SensorType_Custom: Guid = Guid('e83af229-8640-4d18-a2-13-e2-26-75-eb-b2-c3')
GUID_SensorType_FloorElevation: Guid = Guid('ade4987f-7ac4-4dfa-97-22-0a-02-71-81-c7-47')
GUID_SensorType_GeomagneticOrientation: Guid = Guid('e77195f8-2d1f-4823-97-1b-1c-44-67-55-6c-9d')
GUID_SensorType_GravityVector: Guid = Guid('03b52c73-bb76-463f-95-24-38-de-76-eb-70-0b')
GUID_SensorType_Gyrometer3D: Guid = Guid('09485f5a-759e-42c2-bd-4b-a3-49-b7-5c-86-43')
GUID_SensorType_Humidity: Guid = Guid('5c72bf67-bd7e-4257-99-0b-98-a3-ba-3b-40-0a')
GUID_SensorType_LinearAccelerometer: Guid = Guid('038b0283-97b4-41c8-bc-24-5f-f1-aa-48-fe-c7')
GUID_SensorType_Magnetometer3D: Guid = Guid('55e5effb-15c7-40df-86-98-a8-4b-7c-86-3c-53')
GUID_SensorType_Orientation: Guid = Guid('cdb5d8f7-3cfd-41c8-85-42-cc-e6-22-cf-5d-6e')
GUID_SensorType_Pedometer: Guid = Guid('b19f89af-e3eb-444b-8d-ea-20-25-75-a7-15-99')
GUID_SensorType_Proximity: Guid = Guid('5220dae9-3179-4430-9f-90-06-26-6d-2a-34-de')
GUID_SensorType_RelativeOrientation: Guid = Guid('40993b51-4706-44dc-98-d5-c9-20-c0-37-ff-ab')
GUID_SensorType_SimpleDeviceOrientation: Guid = Guid('86a19291-0482-402c-bf-4c-ad-da-c5-2b-1c-39')
GUID_SensorType_Temperature: Guid = Guid('04fd0ec4-d5da-45fa-95-a9-5d-b3-8e-e1-93-06')
GUID_SensorType_HingeAngle: Guid = Guid('82358065-f4c4-4da1-b2-72-13-c2-33-32-a2-07')
SENSOR_PROPERTY_LIST_HEADER_SIZE: UInt32 = 8
@winfunctype('SensorsUtilsV2.dll')
def GetPerformanceTime(TimeMs: POINTER(UInt32)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def InitPropVariantFromFloat(fltVal: Single, ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetPropVariant(pList: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), TypeCheck: win32more.Foundation.BOOLEAN, pValue: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeySetPropVariant(pList: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), TypeCheck: win32more.Foundation.BOOLEAN, pValue: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetFileTime(pList: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pRetValue: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetGuid(pList: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pRetValue: POINTER(Guid)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetBool(pList: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pRetValue: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetUlong(pList: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pRetValue: POINTER(UInt32)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetUshort(pList: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pRetValue: POINTER(UInt16)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetFloat(pList: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pRetValue: POINTER(Single)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetDouble(pList: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pRetValue: POINTER(Double)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetInt32(pList: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pRetValue: POINTER(Int32)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetInt64(pList: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pRetValue: POINTER(Int64)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetNthUlong(pList: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), Occurrence: UInt32, pRetValue: POINTER(UInt32)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetNthUshort(pList: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), Occurrence: UInt32, pRetValue: POINTER(UInt16)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropKeyFindKeyGetNthInt64(pList: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), Occurrence: UInt32, pRetValue: POINTER(Int64)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def IsKeyPresentInPropertyList(pList: POINTER(win32more.Devices.Sensors.SENSOR_PROPERTY_LIST_head), pKey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> win32more.Foundation.BOOLEAN: ...
@winfunctype('SensorsUtilsV2.dll')
def IsKeyPresentInCollectionList(pList: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> win32more.Foundation.BOOLEAN: ...
@winfunctype('SensorsUtilsV2.dll')
def IsCollectionListSame(ListA: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), ListB: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head)) -> win32more.Foundation.BOOLEAN: ...
@winfunctype('SensorsUtilsV2.dll')
def PropVariantGetInformation(PropVariantValue: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), PropVariantOffset: POINTER(UInt32), PropVariantSize: POINTER(UInt32), PropVariantPointer: POINTER(c_void_p), RemappedType: POINTER(UInt32)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropertiesListCopy(Target: POINTER(win32more.Devices.Sensors.SENSOR_PROPERTY_LIST_head), Source: POINTER(win32more.Devices.Sensors.SENSOR_PROPERTY_LIST_head)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def PropertiesListGetFillableCount(BufferSizeBytes: UInt32) -> UInt32: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListGetMarshalledSize(Collection: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head)) -> UInt32: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListCopyAndMarshall(Target: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), Source: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListMarshall(Target: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListGetMarshalledSizeWithoutSerialization(Collection: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head)) -> UInt32: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListUpdateMarshalledPointer(Collection: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def SerializationBufferAllocate(SizeInBytes: UInt32, pBuffer: POINTER(c_char_p_no)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def SerializationBufferFree(Buffer: c_char_p_no) -> Void: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListGetSerializedSize(Collection: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head)) -> UInt32: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListSerializeToBuffer(SourceCollection: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), TargetBufferSizeInBytes: UInt32, TargetBuffer: c_char_p_no) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListAllocateBufferAndSerialize(SourceCollection: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pTargetBufferSizeInBytes: POINTER(UInt32), pTargetBuffer: POINTER(c_char_p_no)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListDeserializeFromBuffer(SourceBufferSizeInBytes: UInt32, SourceBuffer: c_char_p_no, TargetCollection: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def SensorCollectionGetAt(Index: UInt32, pSensorsList: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pKey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pValue: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListGetFillableCount(BufferSizeBytes: UInt32) -> UInt32: ...
@winfunctype('SensorsUtilsV2.dll')
def EvaluateActivityThresholds(newSample: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), oldSample: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), thresholds: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head)) -> win32more.Foundation.BOOLEAN: ...
@winfunctype('SensorsUtilsV2.dll')
def CollectionsListSortSubscribedActivitiesByConfidence(thresholds: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), pCollection: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head)) -> win32more.Foundation.NTSTATUS: ...
@winfunctype('SensorsUtilsV2.dll')
def InitPropVariantFromCLSIDArray(members: POINTER(Guid), size: UInt32, ppropvar: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('SensorsUtilsV2.dll')
def IsSensorSubscribed(subscriptionList: POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), currentType: Guid) -> win32more.Foundation.BOOLEAN: ...
@winfunctype('SensorsUtilsV2.dll')
def IsGUIDPresentInList(guidArray: POINTER(Guid), arrayLength: UInt32, guidElem: POINTER(Guid)) -> win32more.Foundation.BOOLEAN: ...
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
class ILocationPermissions(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d5fb0a7f-e74e-44f5-8e-02-48-06-86-3a-27-4f')
    @commethod(3)
    def GetGlobalLocationPermission(pfEnabled: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CheckLocationCapability(dwClientThreadId: UInt32) -> win32more.Foundation.HRESULT: ...
class ISensor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5fa08f80-2657-458e-af-75-46-f7-3f-a6-ac-5c')
    @commethod(3)
    def GetID(pID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetCategory(pSensorCategory: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetType(pSensorType: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetFriendlyName(pFriendlyName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetProperty(key: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pProperty: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetProperties(pKeys: win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head, ppProperties: POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetSupportedDataFields(ppDataFields: POINTER(win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetProperties(pProperties: win32more.Devices.PortableDevices.IPortableDeviceValues_head, ppResults: POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SupportsDataField(key: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pIsSupported: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetState(pState: POINTER(win32more.Devices.Sensors.SensorState)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetData(ppDataReport: POINTER(win32more.Devices.Sensors.ISensorDataReport_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SupportsEvent(eventGuid: POINTER(Guid), pIsSupported: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetEventInterest(ppValues: POINTER(POINTER(Guid)), pCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SetEventInterest(pValues: POINTER(Guid), count: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def SetEventSink(pEvents: win32more.Devices.Sensors.ISensorEvents_head) -> win32more.Foundation.HRESULT: ...
class ISensorCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('23571e11-e545-4dd8-a3-37-b8-9b-f4-4b-10-df')
    @commethod(3)
    def GetAt(ulIndex: UInt32, ppSensor: POINTER(win32more.Devices.Sensors.ISensor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetCount(pCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Add(pSensor: win32more.Devices.Sensors.ISensor_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Remove(pSensor: win32more.Devices.Sensors.ISensor_head) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveByID(sensorID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Clear() -> win32more.Foundation.HRESULT: ...
class ISensorDataReport(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0ab9df9b-c4b5-4796-88-98-04-70-70-6a-2e-1d')
    @commethod(3)
    def GetTimestamp(pTimeStamp: POINTER(win32more.Foundation.SYSTEMTIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetSensorValue(pKey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pValue: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetSensorValues(pKeys: win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head, ppValues: POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head)) -> win32more.Foundation.HRESULT: ...
class ISensorEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5d8dcc91-4641-47e7-b7-c3-b7-4f-48-a6-c3-91')
    @commethod(3)
    def OnStateChanged(pSensor: win32more.Devices.Sensors.ISensor_head, state: win32more.Devices.Sensors.SensorState) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnDataUpdated(pSensor: win32more.Devices.Sensors.ISensor_head, pNewData: win32more.Devices.Sensors.ISensorDataReport_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnEvent(pSensor: win32more.Devices.Sensors.ISensor_head, eventID: POINTER(Guid), pEventData: win32more.Devices.PortableDevices.IPortableDeviceValues_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def OnLeave(ID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class ISensorManager(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('bd77db67-45a8-42dc-8d-00-6d-cf-15-f8-37-7a')
    @commethod(3)
    def GetSensorsByCategory(sensorCategory: POINTER(Guid), ppSensorsFound: POINTER(win32more.Devices.Sensors.ISensorCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetSensorsByType(sensorType: POINTER(Guid), ppSensorsFound: POINTER(win32more.Devices.Sensors.ISensorCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetSensorByID(sensorID: POINTER(Guid), ppSensor: POINTER(win32more.Devices.Sensors.ISensor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetEventSink(pEvents: win32more.Devices.Sensors.ISensorManagerEvents_head) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def RequestPermissions(hParent: win32more.Foundation.HWND, pSensors: win32more.Devices.Sensors.ISensorCollection_head, fModal: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
class ISensorManagerEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9b3b0b86-266a-4aad-b2-1f-fd-e5-50-10-01-b7')
    @commethod(3)
    def OnSensorEnter(pSensor: win32more.Devices.Sensors.ISensor_head, state: win32more.Devices.Sensors.SensorState) -> win32more.Foundation.HRESULT: ...
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
            V1: win32more.Devices.Sensors.VEC3D
            V2: win32more.Devices.Sensors.VEC3D
            V3: win32more.Devices.Sensors.VEC3D
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
PROXIMITY_TYPE = Int32
ProximityType_ObjectProximity: PROXIMITY_TYPE = 0
ProximityType_HumanProximity: PROXIMITY_TYPE = 1
ProximityType_Force_Dword: PROXIMITY_TYPE = -1
class QUATERNION(Structure):
    X: Single
    Y: Single
    Z: Single
    W: Single
class SENSOR_COLLECTION_LIST(Structure):
    AllocatedSizeInBytes: UInt32
    Count: UInt32
    List: win32more.Devices.Sensors.SENSOR_VALUE_PAIR * 1
SENSOR_CONNECTION_TYPES = Int32
SensorConnectionType_Integrated: SENSOR_CONNECTION_TYPES = 0
SensorConnectionType_Attached: SENSOR_CONNECTION_TYPES = 1
SensorConnectionType_External: SENSOR_CONNECTION_TYPES = 2
class SENSOR_PROPERTY_LIST(Structure):
    AllocatedSizeInBytes: UInt32
    Count: UInt32
    List: win32more.UI.Shell.PropertiesSystem.PROPERTYKEY * 1
SENSOR_STATE = Int32
SensorState_Initializing: SENSOR_STATE = 0
SensorState_Idle: SENSOR_STATE = 1
SensorState_Active: SENSOR_STATE = 2
SensorState_Error: SENSOR_STATE = 3
class SENSOR_VALUE_PAIR(Structure):
    Key: win32more.UI.Shell.PropertiesSystem.PROPERTYKEY
    Value: win32more.System.Com.StructuredStorage.PROPVARIANT
SIMPLE_DEVICE_ORIENTATION = Int32
SimpleDeviceOrientation_NotRotated: SIMPLE_DEVICE_ORIENTATION = 0
SimpleDeviceOrientation_Rotated90DegreesCounterclockwise: SIMPLE_DEVICE_ORIENTATION = 1
SimpleDeviceOrientation_Rotated180DegreesCounterclockwise: SIMPLE_DEVICE_ORIENTATION = 2
SimpleDeviceOrientation_Rotated270DegreesCounterclockwise: SIMPLE_DEVICE_ORIENTATION = 3
SimpleDeviceOrientation_Faceup: SIMPLE_DEVICE_ORIENTATION = 4
SimpleDeviceOrientation_Facedown: SIMPLE_DEVICE_ORIENTATION = 5
Sensor = Guid('e97ced00-523a-4133-bf-6f-d3-a2-da-e7-f6-ba')
SensorCollection = Guid('79c43adb-a429-469f-aa-39-2f-2b-74-b7-59-37')
SensorConnectionType = Int32
SENSOR_CONNECTION_TYPE_PC_INTEGRATED: SensorConnectionType = 0
SENSOR_CONNECTION_TYPE_PC_ATTACHED: SensorConnectionType = 1
SENSOR_CONNECTION_TYPE_PC_EXTERNAL: SensorConnectionType = 2
SensorDataReport = Guid('4ea9d6ef-694b-4218-88-16-cc-da-8d-a7-4b-ba')
SensorManager = Guid('77a1c827-fcd2-4689-89-15-9d-61-3c-c5-fa-3e')
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
class VEC3D(Structure):
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
__all__ = [
    "ACTIVITY_STATE",
    "ACTIVITY_STATE_COUNT",
    "ACTIVITY_STATE_COUNT_ActivityStateCount",
    "AXIS",
    "AXIS_MAX",
    "AXIS_X",
    "AXIS_Y",
    "AXIS_Z",
    "ActivityState_Biking",
    "ActivityState_Fidgeting",
    "ActivityState_Force_Dword",
    "ActivityState_Idle",
    "ActivityState_InVehicle",
    "ActivityState_Max",
    "ActivityState_Running",
    "ActivityState_Stationary",
    "ActivityState_Unknown",
    "ActivityState_Walking",
    "CollectionsListAllocateBufferAndSerialize",
    "CollectionsListCopyAndMarshall",
    "CollectionsListDeserializeFromBuffer",
    "CollectionsListGetFillableCount",
    "CollectionsListGetMarshalledSize",
    "CollectionsListGetMarshalledSizeWithoutSerialization",
    "CollectionsListGetSerializedSize",
    "CollectionsListMarshall",
    "CollectionsListSerializeToBuffer",
    "CollectionsListSortSubscribedActivitiesByConfidence",
    "CollectionsListUpdateMarshalledPointer",
    "ELEVATION_CHANGE_MODE",
    "ElevationChangeMode_Elevator",
    "ElevationChangeMode_Force_Dword",
    "ElevationChangeMode_Max",
    "ElevationChangeMode_Stepping",
    "ElevationChangeMode_Unknown",
    "EvaluateActivityThresholds",
    "GNSS_CLEAR_ALL_ASSISTANCE_DATA",
    "GUID_DEVINTERFACE_SENSOR",
    "GUID_SensorCategory_All",
    "GUID_SensorCategory_Biometric",
    "GUID_SensorCategory_Electrical",
    "GUID_SensorCategory_Environmental",
    "GUID_SensorCategory_Light",
    "GUID_SensorCategory_Location",
    "GUID_SensorCategory_Mechanical",
    "GUID_SensorCategory_Motion",
    "GUID_SensorCategory_Orientation",
    "GUID_SensorCategory_Other",
    "GUID_SensorCategory_PersonalActivity",
    "GUID_SensorCategory_Scanner",
    "GUID_SensorCategory_Unsupported",
    "GUID_SensorType_Accelerometer3D",
    "GUID_SensorType_ActivityDetection",
    "GUID_SensorType_AmbientLight",
    "GUID_SensorType_Barometer",
    "GUID_SensorType_Custom",
    "GUID_SensorType_FloorElevation",
    "GUID_SensorType_GeomagneticOrientation",
    "GUID_SensorType_GravityVector",
    "GUID_SensorType_Gyrometer3D",
    "GUID_SensorType_HingeAngle",
    "GUID_SensorType_Humidity",
    "GUID_SensorType_LinearAccelerometer",
    "GUID_SensorType_Magnetometer3D",
    "GUID_SensorType_Orientation",
    "GUID_SensorType_Pedometer",
    "GUID_SensorType_Proximity",
    "GUID_SensorType_RelativeOrientation",
    "GUID_SensorType_SimpleDeviceOrientation",
    "GUID_SensorType_Temperature",
    "GetPerformanceTime",
    "HUMAN_PRESENCE_DETECTION_TYPE",
    "HUMAN_PRESENCE_DETECTION_TYPE_COUNT",
    "HUMAN_PRESENCE_DETECTION_TYPE_COUNT_HumanPresenceDetectionTypeCount",
    "HumanPresenceDetectionType_AudioBiometric",
    "HumanPresenceDetectionType_FacialBiometric",
    "HumanPresenceDetectionType_Force_Dword",
    "HumanPresenceDetectionType_VendorDefinedBiometric",
    "HumanPresenceDetectionType_VendorDefinedNonBiometric",
    "ILocationPermissions",
    "ISensor",
    "ISensorCollection",
    "ISensorDataReport",
    "ISensorEvents",
    "ISensorManager",
    "ISensorManagerEvents",
    "InitPropVariantFromCLSIDArray",
    "InitPropVariantFromFloat",
    "IsCollectionListSame",
    "IsGUIDPresentInList",
    "IsKeyPresentInCollectionList",
    "IsKeyPresentInPropertyList",
    "IsSensorSubscribed",
    "LOCATION_DESIRED_ACCURACY",
    "LOCATION_DESIRED_ACCURACY_DEFAULT",
    "LOCATION_DESIRED_ACCURACY_HIGH",
    "LOCATION_POSITION_SOURCE",
    "LOCATION_POSITION_SOURCE_CELLULAR",
    "LOCATION_POSITION_SOURCE_IPADDRESS",
    "LOCATION_POSITION_SOURCE_SATELLITE",
    "LOCATION_POSITION_SOURCE_UNKNOWN",
    "LOCATION_POSITION_SOURCE_WIFI",
    "MAGNETOMETER_ACCURACY",
    "MAGNETOMETER_ACCURACY_APPROXIMATE",
    "MAGNETOMETER_ACCURACY_HIGH",
    "MAGNETOMETER_ACCURACY_UNKNOWN",
    "MAGNETOMETER_ACCURACY_UNRELIABLE",
    "MATRIX3X3",
    "MagnetometerAccuracy",
    "MagnetometerAccuracy_Approximate",
    "MagnetometerAccuracy_High",
    "MagnetometerAccuracy_Unknown",
    "MagnetometerAccuracy_Unreliable",
    "PEDOMETER_STEP_TYPE",
    "PEDOMETER_STEP_TYPE_COUNT",
    "PEDOMETER_STEP_TYPE_COUNT_PedometerStepTypeCount",
    "PROXIMITY_TYPE",
    "PedometerStepType_Force_Dword",
    "PedometerStepType_Max",
    "PedometerStepType_Running",
    "PedometerStepType_Unknown",
    "PedometerStepType_Walking",
    "PropKeyFindKeyGetBool",
    "PropKeyFindKeyGetDouble",
    "PropKeyFindKeyGetFileTime",
    "PropKeyFindKeyGetFloat",
    "PropKeyFindKeyGetGuid",
    "PropKeyFindKeyGetInt32",
    "PropKeyFindKeyGetInt64",
    "PropKeyFindKeyGetNthInt64",
    "PropKeyFindKeyGetNthUlong",
    "PropKeyFindKeyGetNthUshort",
    "PropKeyFindKeyGetPropVariant",
    "PropKeyFindKeyGetUlong",
    "PropKeyFindKeyGetUshort",
    "PropKeyFindKeySetPropVariant",
    "PropVariantGetInformation",
    "PropertiesListCopy",
    "PropertiesListGetFillableCount",
    "ProximityType_Force_Dword",
    "ProximityType_HumanProximity",
    "ProximityType_ObjectProximity",
    "QUATERNION",
    "SENSOR_CATEGORY_ALL",
    "SENSOR_CATEGORY_BIOMETRIC",
    "SENSOR_CATEGORY_ELECTRICAL",
    "SENSOR_CATEGORY_ENVIRONMENTAL",
    "SENSOR_CATEGORY_LIGHT",
    "SENSOR_CATEGORY_LOCATION",
    "SENSOR_CATEGORY_MECHANICAL",
    "SENSOR_CATEGORY_MOTION",
    "SENSOR_CATEGORY_ORIENTATION",
    "SENSOR_CATEGORY_OTHER",
    "SENSOR_CATEGORY_SCANNER",
    "SENSOR_CATEGORY_UNSUPPORTED",
    "SENSOR_COLLECTION_LIST",
    "SENSOR_CONNECTION_TYPES",
    "SENSOR_CONNECTION_TYPE_PC_ATTACHED",
    "SENSOR_CONNECTION_TYPE_PC_EXTERNAL",
    "SENSOR_CONNECTION_TYPE_PC_INTEGRATED",
    "SENSOR_DATA_TYPE_ABSOLUTE_PRESSURE_PASCAL",
    "SENSOR_DATA_TYPE_ACCELERATION_X_G",
    "SENSOR_DATA_TYPE_ACCELERATION_Y_G",
    "SENSOR_DATA_TYPE_ACCELERATION_Z_G",
    "SENSOR_DATA_TYPE_ADDRESS1",
    "SENSOR_DATA_TYPE_ADDRESS2",
    "SENSOR_DATA_TYPE_ALTITUDE_ANTENNA_SEALEVEL_METERS",
    "SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_ERROR_METERS",
    "SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_METERS",
    "SENSOR_DATA_TYPE_ALTITUDE_SEALEVEL_ERROR_METERS",
    "SENSOR_DATA_TYPE_ALTITUDE_SEALEVEL_METERS",
    "SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_X_DEGREES_PER_SECOND_SQUARED",
    "SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_Y_DEGREES_PER_SECOND_SQUARED",
    "SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_Z_DEGREES_PER_SECOND_SQUARED",
    "SENSOR_DATA_TYPE_ANGULAR_VELOCITY_X_DEGREES_PER_SECOND",
    "SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Y_DEGREES_PER_SECOND",
    "SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Z_DEGREES_PER_SECOND",
    "SENSOR_DATA_TYPE_ATMOSPHERIC_PRESSURE_BAR",
    "SENSOR_DATA_TYPE_BIOMETRIC_GUID",
    "SENSOR_DATA_TYPE_BOOLEAN_SWITCH_ARRAY_STATES",
    "SENSOR_DATA_TYPE_BOOLEAN_SWITCH_STATE",
    "SENSOR_DATA_TYPE_CAPACITANCE_FARAD",
    "SENSOR_DATA_TYPE_CITY",
    "SENSOR_DATA_TYPE_COMMON_GUID",
    "SENSOR_DATA_TYPE_COUNTRY_REGION",
    "SENSOR_DATA_TYPE_CURRENT_AMPS",
    "SENSOR_DATA_TYPE_CUSTOM_BOOLEAN_ARRAY",
    "SENSOR_DATA_TYPE_CUSTOM_GUID",
    "SENSOR_DATA_TYPE_CUSTOM_USAGE",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE1",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE10",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE11",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE12",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE13",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE14",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE15",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE16",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE17",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE18",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE19",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE2",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE20",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE21",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE22",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE23",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE24",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE25",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE26",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE27",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE28",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE3",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE4",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE5",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE6",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE7",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE8",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE9",
    "SENSOR_DATA_TYPE_DGPS_DATA_AGE",
    "SENSOR_DATA_TYPE_DIFFERENTIAL_REFERENCE_STATION_ID",
    "SENSOR_DATA_TYPE_DISTANCE_X_METERS",
    "SENSOR_DATA_TYPE_DISTANCE_Y_METERS",
    "SENSOR_DATA_TYPE_DISTANCE_Z_METERS",
    "SENSOR_DATA_TYPE_ELECTRICAL_FREQUENCY_HERTZ",
    "SENSOR_DATA_TYPE_ELECTRICAL_GUID",
    "SENSOR_DATA_TYPE_ELECTRICAL_PERCENT_OF_RANGE",
    "SENSOR_DATA_TYPE_ELECTRICAL_POWER_WATTS",
    "SENSOR_DATA_TYPE_ENVIRONMENTAL_GUID",
    "SENSOR_DATA_TYPE_ERROR_RADIUS_METERS",
    "SENSOR_DATA_TYPE_FIX_QUALITY",
    "SENSOR_DATA_TYPE_FIX_TYPE",
    "SENSOR_DATA_TYPE_FORCE_NEWTONS",
    "SENSOR_DATA_TYPE_GAUGE_PRESSURE_PASCAL",
    "SENSOR_DATA_TYPE_GEOIDAL_SEPARATION",
    "SENSOR_DATA_TYPE_GPS_OPERATION_MODE",
    "SENSOR_DATA_TYPE_GPS_SELECTION_MODE",
    "SENSOR_DATA_TYPE_GPS_STATUS",
    "SENSOR_DATA_TYPE_GUID_MECHANICAL_GUID",
    "SENSOR_DATA_TYPE_HORIZONAL_DILUTION_OF_PRECISION",
    "SENSOR_DATA_TYPE_HUMAN_PRESENCE",
    "SENSOR_DATA_TYPE_HUMAN_PROXIMITY_METERS",
    "SENSOR_DATA_TYPE_INDUCTANCE_HENRY",
    "SENSOR_DATA_TYPE_LATITUDE_DEGREES",
    "SENSOR_DATA_TYPE_LIGHT_CHROMACITY",
    "SENSOR_DATA_TYPE_LIGHT_GUID",
    "SENSOR_DATA_TYPE_LIGHT_LEVEL_LUX",
    "SENSOR_DATA_TYPE_LIGHT_TEMPERATURE_KELVIN",
    "SENSOR_DATA_TYPE_LOCATION_GUID",
    "SENSOR_DATA_TYPE_LOCATION_SOURCE",
    "SENSOR_DATA_TYPE_LONGITUDE_DEGREES",
    "SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_X_MILLIGAUSS",
    "SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_Y_MILLIGAUSS",
    "SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_Z_MILLIGAUSS",
    "SENSOR_DATA_TYPE_MAGNETIC_HEADING_COMPENSATED_MAGNETIC_NORTH_DEGREES",
    "SENSOR_DATA_TYPE_MAGNETIC_HEADING_COMPENSATED_TRUE_NORTH_DEGREES",
    "SENSOR_DATA_TYPE_MAGNETIC_HEADING_DEGREES",
    "SENSOR_DATA_TYPE_MAGNETIC_HEADING_MAGNETIC_NORTH_DEGREES",
    "SENSOR_DATA_TYPE_MAGNETIC_HEADING_TRUE_NORTH_DEGREES",
    "SENSOR_DATA_TYPE_MAGNETIC_HEADING_X_DEGREES",
    "SENSOR_DATA_TYPE_MAGNETIC_HEADING_Y_DEGREES",
    "SENSOR_DATA_TYPE_MAGNETIC_HEADING_Z_DEGREES",
    "SENSOR_DATA_TYPE_MAGNETIC_VARIATION",
    "SENSOR_DATA_TYPE_MAGNETOMETER_ACCURACY",
    "SENSOR_DATA_TYPE_MOTION_GUID",
    "SENSOR_DATA_TYPE_MOTION_STATE",
    "SENSOR_DATA_TYPE_MULTIVALUE_SWITCH_STATE",
    "SENSOR_DATA_TYPE_NMEA_SENTENCE",
    "SENSOR_DATA_TYPE_ORIENTATION_GUID",
    "SENSOR_DATA_TYPE_POSITION_DILUTION_OF_PRECISION",
    "SENSOR_DATA_TYPE_POSTALCODE",
    "SENSOR_DATA_TYPE_QUADRANT_ANGLE_DEGREES",
    "SENSOR_DATA_TYPE_QUATERNION",
    "SENSOR_DATA_TYPE_RELATIVE_HUMIDITY_PERCENT",
    "SENSOR_DATA_TYPE_RESISTANCE_OHMS",
    "SENSOR_DATA_TYPE_RFID_TAG_40_BIT",
    "SENSOR_DATA_TYPE_ROTATION_MATRIX",
    "SENSOR_DATA_TYPE_SATELLITES_IN_VIEW",
    "SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_AZIMUTH",
    "SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_ELEVATION",
    "SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_ID",
    "SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_PRNS",
    "SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_STN_RATIO",
    "SENSOR_DATA_TYPE_SATELLITES_USED_COUNT",
    "SENSOR_DATA_TYPE_SATELLITES_USED_PRNS",
    "SENSOR_DATA_TYPE_SATELLITES_USED_PRNS_AND_CONSTELLATIONS",
    "SENSOR_DATA_TYPE_SCANNER_GUID",
    "SENSOR_DATA_TYPE_SIMPLE_DEVICE_ORIENTATION",
    "SENSOR_DATA_TYPE_SPEED_KNOTS",
    "SENSOR_DATA_TYPE_SPEED_METERS_PER_SECOND",
    "SENSOR_DATA_TYPE_STATE_PROVINCE",
    "SENSOR_DATA_TYPE_STRAIN",
    "SENSOR_DATA_TYPE_TEMPERATURE_CELSIUS",
    "SENSOR_DATA_TYPE_TILT_X_DEGREES",
    "SENSOR_DATA_TYPE_TILT_Y_DEGREES",
    "SENSOR_DATA_TYPE_TILT_Z_DEGREES",
    "SENSOR_DATA_TYPE_TIMESTAMP",
    "SENSOR_DATA_TYPE_TOUCH_STATE",
    "SENSOR_DATA_TYPE_TRUE_HEADING_DEGREES",
    "SENSOR_DATA_TYPE_VERTICAL_DILUTION_OF_PRECISION",
    "SENSOR_DATA_TYPE_VOLTAGE_VOLTS",
    "SENSOR_DATA_TYPE_WEIGHT_KILOGRAMS",
    "SENSOR_DATA_TYPE_WIND_DIRECTION_DEGREES_ANTICLOCKWISE",
    "SENSOR_DATA_TYPE_WIND_SPEED_METERS_PER_SECOND",
    "SENSOR_ERROR_PARAMETER_COMMON_GUID",
    "SENSOR_EVENT_ACCELEROMETER_SHAKE",
    "SENSOR_EVENT_DATA_UPDATED",
    "SENSOR_EVENT_PARAMETER_COMMON_GUID",
    "SENSOR_EVENT_PARAMETER_EVENT_ID",
    "SENSOR_EVENT_PARAMETER_STATE",
    "SENSOR_EVENT_PROPERTY_CHANGED",
    "SENSOR_EVENT_STATE_CHANGED",
    "SENSOR_PROPERTY_ACCURACY",
    "SENSOR_PROPERTY_CHANGE_SENSITIVITY",
    "SENSOR_PROPERTY_CLEAR_ASSISTANCE_DATA",
    "SENSOR_PROPERTY_COMMON_GUID",
    "SENSOR_PROPERTY_CONNECTION_TYPE",
    "SENSOR_PROPERTY_CURRENT_REPORT_INTERVAL",
    "SENSOR_PROPERTY_DESCRIPTION",
    "SENSOR_PROPERTY_DEVICE_PATH",
    "SENSOR_PROPERTY_FRIENDLY_NAME",
    "SENSOR_PROPERTY_HID_USAGE",
    "SENSOR_PROPERTY_LIGHT_RESPONSE_CURVE",
    "SENSOR_PROPERTY_LIST",
    "SENSOR_PROPERTY_LIST_HEADER_SIZE",
    "SENSOR_PROPERTY_LOCATION_DESIRED_ACCURACY",
    "SENSOR_PROPERTY_MANUFACTURER",
    "SENSOR_PROPERTY_MIN_REPORT_INTERVAL",
    "SENSOR_PROPERTY_MODEL",
    "SENSOR_PROPERTY_PERSISTENT_UNIQUE_ID",
    "SENSOR_PROPERTY_RADIO_STATE",
    "SENSOR_PROPERTY_RADIO_STATE_PREVIOUS",
    "SENSOR_PROPERTY_RANGE_MAXIMUM",
    "SENSOR_PROPERTY_RANGE_MINIMUM",
    "SENSOR_PROPERTY_RESOLUTION",
    "SENSOR_PROPERTY_SERIAL_NUMBER",
    "SENSOR_PROPERTY_STATE",
    "SENSOR_PROPERTY_TEST_GUID",
    "SENSOR_PROPERTY_TURN_ON_OFF_NMEA",
    "SENSOR_PROPERTY_TYPE",
    "SENSOR_STATE",
    "SENSOR_STATE_ACCESS_DENIED",
    "SENSOR_STATE_ERROR",
    "SENSOR_STATE_INITIALIZING",
    "SENSOR_STATE_MAX",
    "SENSOR_STATE_MIN",
    "SENSOR_STATE_NOT_AVAILABLE",
    "SENSOR_STATE_NO_DATA",
    "SENSOR_STATE_READY",
    "SENSOR_TYPE_ACCELEROMETER_1D",
    "SENSOR_TYPE_ACCELEROMETER_2D",
    "SENSOR_TYPE_ACCELEROMETER_3D",
    "SENSOR_TYPE_AGGREGATED_DEVICE_ORIENTATION",
    "SENSOR_TYPE_AGGREGATED_QUADRANT_ORIENTATION",
    "SENSOR_TYPE_AGGREGATED_SIMPLE_DEVICE_ORIENTATION",
    "SENSOR_TYPE_AMBIENT_LIGHT",
    "SENSOR_TYPE_BARCODE_SCANNER",
    "SENSOR_TYPE_BOOLEAN_SWITCH",
    "SENSOR_TYPE_BOOLEAN_SWITCH_ARRAY",
    "SENSOR_TYPE_CAPACITANCE",
    "SENSOR_TYPE_COMPASS_1D",
    "SENSOR_TYPE_COMPASS_2D",
    "SENSOR_TYPE_COMPASS_3D",
    "SENSOR_TYPE_CURRENT",
    "SENSOR_TYPE_CUSTOM",
    "SENSOR_TYPE_DISTANCE_1D",
    "SENSOR_TYPE_DISTANCE_2D",
    "SENSOR_TYPE_DISTANCE_3D",
    "SENSOR_TYPE_ELECTRICAL_POWER",
    "SENSOR_TYPE_ENVIRONMENTAL_ATMOSPHERIC_PRESSURE",
    "SENSOR_TYPE_ENVIRONMENTAL_HUMIDITY",
    "SENSOR_TYPE_ENVIRONMENTAL_TEMPERATURE",
    "SENSOR_TYPE_ENVIRONMENTAL_WIND_DIRECTION",
    "SENSOR_TYPE_ENVIRONMENTAL_WIND_SPEED",
    "SENSOR_TYPE_FORCE",
    "SENSOR_TYPE_FREQUENCY",
    "SENSOR_TYPE_GYROMETER_1D",
    "SENSOR_TYPE_GYROMETER_2D",
    "SENSOR_TYPE_GYROMETER_3D",
    "SENSOR_TYPE_HUMAN_PRESENCE",
    "SENSOR_TYPE_HUMAN_PROXIMITY",
    "SENSOR_TYPE_INCLINOMETER_1D",
    "SENSOR_TYPE_INCLINOMETER_2D",
    "SENSOR_TYPE_INCLINOMETER_3D",
    "SENSOR_TYPE_INDUCTANCE",
    "SENSOR_TYPE_LOCATION_BROADCAST",
    "SENSOR_TYPE_LOCATION_DEAD_RECKONING",
    "SENSOR_TYPE_LOCATION_GPS",
    "SENSOR_TYPE_LOCATION_LOOKUP",
    "SENSOR_TYPE_LOCATION_OTHER",
    "SENSOR_TYPE_LOCATION_STATIC",
    "SENSOR_TYPE_LOCATION_TRIANGULATION",
    "SENSOR_TYPE_MOTION_DETECTOR",
    "SENSOR_TYPE_MULTIVALUE_SWITCH",
    "SENSOR_TYPE_POTENTIOMETER",
    "SENSOR_TYPE_PRESSURE",
    "SENSOR_TYPE_RESISTANCE",
    "SENSOR_TYPE_RFID_SCANNER",
    "SENSOR_TYPE_SCALE",
    "SENSOR_TYPE_SPEEDOMETER",
    "SENSOR_TYPE_STRAIN",
    "SENSOR_TYPE_TOUCH",
    "SENSOR_TYPE_UNKNOWN",
    "SENSOR_TYPE_VOLTAGE",
    "SENSOR_VALUE_PAIR",
    "SIMPLE_DEVICE_ORIENTATION",
    "SIMPLE_DEVICE_ORIENTATION_NOT_ROTATED",
    "SIMPLE_DEVICE_ORIENTATION_ROTATED_180",
    "SIMPLE_DEVICE_ORIENTATION_ROTATED_270",
    "SIMPLE_DEVICE_ORIENTATION_ROTATED_90",
    "SIMPLE_DEVICE_ORIENTATION_ROTATED_FACE_DOWN",
    "SIMPLE_DEVICE_ORIENTATION_ROTATED_FACE_UP",
    "Sensor",
    "SensorCollection",
    "SensorCollectionGetAt",
    "SensorConnectionType",
    "SensorConnectionType_Attached",
    "SensorConnectionType_External",
    "SensorConnectionType_Integrated",
    "SensorDataReport",
    "SensorManager",
    "SensorState",
    "SensorState_Active",
    "SensorState_Error",
    "SensorState_Idle",
    "SensorState_Initializing",
    "SerializationBufferAllocate",
    "SerializationBufferFree",
    "SimpleDeviceOrientation",
    "SimpleDeviceOrientation_Facedown",
    "SimpleDeviceOrientation_Faceup",
    "SimpleDeviceOrientation_NotRotated",
    "SimpleDeviceOrientation_Rotated180DegreesCounterclockwise",
    "SimpleDeviceOrientation_Rotated270DegreesCounterclockwise",
    "SimpleDeviceOrientation_Rotated90DegreesCounterclockwise",
    "VEC3D",
]
_arch_optional = [
]
