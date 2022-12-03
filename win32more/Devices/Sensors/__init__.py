from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
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
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
ACTIVITY_STATE = Int32
ActivityState_Unknown = 1
ActivityState_Stationary = 2
ActivityState_Fidgeting = 4
ActivityState_Walking = 8
ActivityState_Running = 16
ActivityState_InVehicle = 32
ActivityState_Biking = 64
ActivityState_Idle = 128
ActivityState_Max = 256
ActivityState_Force_Dword = -1
ACTIVITY_STATE_COUNT = Int32
ACTIVITY_STATE_COUNT_ActivityStateCount = 8
def _define_GUID_DEVINTERFACE_SENSOR():
    return Guid('ba1bb692-9b7a-4833-9a-1e-52-5e-d1-34-e7-e2')
def _define_SENSOR_EVENT_STATE_CHANGED():
    return Guid('bfd96016-6bd7-4560-ad-34-f2-f6-60-7e-8f-81')
def _define_SENSOR_EVENT_DATA_UPDATED():
    return Guid('2ed0f2a4-0087-41d3-87-db-67-73-37-0b-3c-88')
def _define_SENSOR_EVENT_PROPERTY_CHANGED():
    return Guid('2358f099-84c9-4d3d-90-df-c2-42-1e-2b-20-45')
def _define_SENSOR_EVENT_ACCELEROMETER_SHAKE():
    return Guid('825f5a94-0f48-4396-9c-a0-6e-cb-5c-99-d9-15')
def _define_SENSOR_EVENT_PARAMETER_COMMON_GUID():
    return Guid('64346e30-8728-4b34-bd-f6-4f-52-44-2c-5c-28')
def _define_SENSOR_EVENT_PARAMETER_EVENT_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64346e30-8728-4b34-bd-f6-4f-52-44-2c-5c-28'), pid=2)
def _define_SENSOR_EVENT_PARAMETER_STATE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('64346e30-8728-4b34-bd-f6-4f-52-44-2c-5c-28'), pid=3)
def _define_SENSOR_ERROR_PARAMETER_COMMON_GUID():
    return Guid('77112bcd-fce1-4f43-b8-b8-a8-82-56-ad-b4-b3')
def _define_SENSOR_PROPERTY_COMMON_GUID():
    return Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20')
def _define_SENSOR_PROPERTY_TYPE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=2)
def _define_SENSOR_PROPERTY_STATE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=3)
def _define_SENSOR_PROPERTY_PERSISTENT_UNIQUE_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=5)
def _define_SENSOR_PROPERTY_MANUFACTURER():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=6)
def _define_SENSOR_PROPERTY_MODEL():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=7)
def _define_SENSOR_PROPERTY_SERIAL_NUMBER():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=8)
def _define_SENSOR_PROPERTY_FRIENDLY_NAME():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=9)
def _define_SENSOR_PROPERTY_DESCRIPTION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=10)
def _define_SENSOR_PROPERTY_CONNECTION_TYPE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=11)
def _define_SENSOR_PROPERTY_MIN_REPORT_INTERVAL():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=12)
def _define_SENSOR_PROPERTY_CURRENT_REPORT_INTERVAL():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=13)
def _define_SENSOR_PROPERTY_CHANGE_SENSITIVITY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=14)
def _define_SENSOR_PROPERTY_DEVICE_PATH():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=15)
def _define_SENSOR_PROPERTY_LIGHT_RESPONSE_CURVE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=16)
def _define_SENSOR_PROPERTY_ACCURACY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=17)
def _define_SENSOR_PROPERTY_RESOLUTION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=18)
def _define_SENSOR_PROPERTY_LOCATION_DESIRED_ACCURACY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=19)
def _define_SENSOR_PROPERTY_RANGE_MINIMUM():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=20)
def _define_SENSOR_PROPERTY_RANGE_MAXIMUM():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=21)
def _define_SENSOR_PROPERTY_HID_USAGE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=22)
def _define_SENSOR_PROPERTY_RADIO_STATE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=23)
def _define_SENSOR_PROPERTY_RADIO_STATE_PREVIOUS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('7f8383ec-d3ec-495c-a8-cf-b8-bb-e8-5c-29-20'), pid=24)
def _define_SENSOR_CATEGORY_ALL():
    return Guid('c317c286-c468-4288-99-75-d4-c4-58-7c-44-2c')
def _define_SENSOR_CATEGORY_LOCATION():
    return Guid('bfa794e4-f964-4fdb-90-f6-51-05-6b-fe-4b-44')
def _define_SENSOR_CATEGORY_ENVIRONMENTAL():
    return Guid('323439aa-7f66-492b-ba-0c-73-e9-aa-0a-65-d5')
def _define_SENSOR_CATEGORY_MOTION():
    return Guid('cd09daf1-3b2e-4c3d-b5-98-b5-e5-ff-93-fd-46')
def _define_SENSOR_CATEGORY_ORIENTATION():
    return Guid('9e6c04b6-96fe-4954-b7-26-68-68-2a-47-3f-69')
def _define_SENSOR_CATEGORY_MECHANICAL():
    return Guid('8d131d68-8ef7-4656-80-b5-cc-cb-d9-37-91-c5')
def _define_SENSOR_CATEGORY_ELECTRICAL():
    return Guid('fb73fcd8-fc4a-483c-ac-58-27-b6-91-c6-be-ff')
def _define_SENSOR_CATEGORY_BIOMETRIC():
    return Guid('ca19690f-a2c7-477d-a9-9e-99-ec-6e-2b-56-48')
def _define_SENSOR_CATEGORY_LIGHT():
    return Guid('17a665c0-9063-4216-b2-02-5c-7a-25-5e-18-ce')
def _define_SENSOR_CATEGORY_SCANNER():
    return Guid('b000e77e-f5b5-420f-81-5d-02-70-a7-26-f2-70')
def _define_SENSOR_CATEGORY_OTHER():
    return Guid('2c90e7a9-f4c9-4fa2-af-37-56-d4-71-fe-5a-3d')
def _define_SENSOR_CATEGORY_UNSUPPORTED():
    return Guid('2beae7fa-19b0-48c5-a1-f6-b5-48-0d-c2-06-b0')
def _define_SENSOR_TYPE_LOCATION_GPS():
    return Guid('ed4ca589-327a-4ff9-a5-60-91-da-4b-48-27-5e')
def _define_SENSOR_TYPE_LOCATION_STATIC():
    return Guid('095f8184-0fa9-4445-8e-6e-b7-0f-32-0b-6b-4c')
def _define_SENSOR_TYPE_LOCATION_LOOKUP():
    return Guid('3b2eae4a-72ce-436d-96-d2-3c-5b-85-70-e9-87')
def _define_SENSOR_TYPE_LOCATION_TRIANGULATION():
    return Guid('691c341a-5406-4fe1-94-2f-22-46-cb-eb-39-e0')
def _define_SENSOR_TYPE_LOCATION_OTHER():
    return Guid('9b2d0566-0368-4f71-b8-8d-53-3f-13-20-31-de')
def _define_SENSOR_TYPE_LOCATION_BROADCAST():
    return Guid('d26988cf-5162-4039-bb-17-4c-58-b6-98-e4-4a')
def _define_SENSOR_TYPE_LOCATION_DEAD_RECKONING():
    return Guid('1a37d538-f28b-42da-9f-ce-a9-d0-a2-a6-d8-29')
def _define_SENSOR_TYPE_ENVIRONMENTAL_TEMPERATURE():
    return Guid('04fd0ec4-d5da-45fa-95-a9-5d-b3-8e-e1-93-06')
def _define_SENSOR_TYPE_ENVIRONMENTAL_ATMOSPHERIC_PRESSURE():
    return Guid('0e903829-ff8a-4a93-97-df-3d-cb-de-40-22-88')
def _define_SENSOR_TYPE_ENVIRONMENTAL_HUMIDITY():
    return Guid('5c72bf67-bd7e-4257-99-0b-98-a3-ba-3b-40-0a')
def _define_SENSOR_TYPE_ENVIRONMENTAL_WIND_SPEED():
    return Guid('dd50607b-a45f-42cd-8e-fd-ec-61-76-1c-42-26')
def _define_SENSOR_TYPE_ENVIRONMENTAL_WIND_DIRECTION():
    return Guid('9ef57a35-9306-434d-af-09-37-fa-5a-9c-00-bd')
def _define_SENSOR_TYPE_ACCELEROMETER_1D():
    return Guid('c04d2387-7340-4cc2-99-1e-3b-18-cb-8e-f2-f4')
def _define_SENSOR_TYPE_ACCELEROMETER_2D():
    return Guid('b2c517a8-f6b5-4ba6-a4-23-5d-f5-60-b4-cc-07')
def _define_SENSOR_TYPE_ACCELEROMETER_3D():
    return Guid('c2fb0f5f-e2d2-4c78-bc-d0-35-2a-95-82-81-9d')
def _define_SENSOR_TYPE_MOTION_DETECTOR():
    return Guid('5c7c1a12-30a5-43b9-a4-b2-cf-09-ec-5b-7b-e8')
def _define_SENSOR_TYPE_GYROMETER_1D():
    return Guid('fa088734-f552-4584-83-24-ed-fa-f6-49-65-2c')
def _define_SENSOR_TYPE_GYROMETER_2D():
    return Guid('31ef4f83-919b-48bf-8d-e0-5d-7a-9d-24-05-56')
def _define_SENSOR_TYPE_GYROMETER_3D():
    return Guid('09485f5a-759e-42c2-bd-4b-a3-49-b7-5c-86-43')
def _define_SENSOR_TYPE_SPEEDOMETER():
    return Guid('6bd73c1f-0bb4-4310-81-b2-df-c1-8a-52-bf-94')
def _define_SENSOR_TYPE_COMPASS_1D():
    return Guid('a415f6c5-cb50-49d0-8e-62-a8-27-0b-d7-a2-6c')
def _define_SENSOR_TYPE_COMPASS_2D():
    return Guid('15655cc0-997a-4d30-84-db-57-ca-ba-36-48-bb')
def _define_SENSOR_TYPE_COMPASS_3D():
    return Guid('76b5ce0d-17dd-414d-93-a1-e1-27-f4-0b-df-6e')
def _define_SENSOR_TYPE_INCLINOMETER_1D():
    return Guid('b96f98c5-7a75-4ba7-94-e9-ac-86-8c-96-6d-d8')
def _define_SENSOR_TYPE_INCLINOMETER_2D():
    return Guid('ab140f6d-83eb-4264-b7-0b-b1-6a-5b-25-6a-01')
def _define_SENSOR_TYPE_INCLINOMETER_3D():
    return Guid('b84919fb-ea85-4976-84-44-6f-6f-5c-6d-31-db')
def _define_SENSOR_TYPE_DISTANCE_1D():
    return Guid('5f14ab2f-1407-4306-a9-3f-b1-db-ab-e4-f9-c0')
def _define_SENSOR_TYPE_DISTANCE_2D():
    return Guid('5cf9a46c-a9a2-4e55-b6-a1-a0-4a-af-a9-5a-92')
def _define_SENSOR_TYPE_DISTANCE_3D():
    return Guid('a20cae31-0e25-4772-9f-e5-96-60-8a-13-54-b2')
def _define_SENSOR_TYPE_AGGREGATED_QUADRANT_ORIENTATION():
    return Guid('9f81f1af-c4ab-4307-99-04-c8-28-bf-b9-08-29')
def _define_SENSOR_TYPE_AGGREGATED_DEVICE_ORIENTATION():
    return Guid('cdb5d8f7-3cfd-41c8-85-42-cc-e6-22-cf-5d-6e')
def _define_SENSOR_TYPE_AGGREGATED_SIMPLE_DEVICE_ORIENTATION():
    return Guid('86a19291-0482-402c-bf-4c-ad-da-c5-2b-1c-39')
def _define_SENSOR_TYPE_VOLTAGE():
    return Guid('c5484637-4fb7-4953-98-b8-a5-6d-8a-a1-fb-1e')
def _define_SENSOR_TYPE_CURRENT():
    return Guid('5adc9fce-15a0-4bbe-a1-ad-2d-38-a9-ae-83-1c')
def _define_SENSOR_TYPE_CAPACITANCE():
    return Guid('ca2ffb1c-2317-49c0-a0-b4-b6-3c-e6-34-61-a0')
def _define_SENSOR_TYPE_RESISTANCE():
    return Guid('9993d2c8-c157-4a52-a7-b5-19-5c-76-03-72-31')
def _define_SENSOR_TYPE_INDUCTANCE():
    return Guid('dc1d933f-c435-4c7d-a2-fe-60-71-92-a5-24-d3')
def _define_SENSOR_TYPE_ELECTRICAL_POWER():
    return Guid('212f10f5-14ab-4376-9a-43-a7-79-40-98-c2-fe')
def _define_SENSOR_TYPE_POTENTIOMETER():
    return Guid('2b3681a9-cadc-45aa-a6-ff-54-95-7c-8b-b4-40')
def _define_SENSOR_TYPE_FREQUENCY():
    return Guid('8cd2cbb6-73e6-4640-a7-09-72-ae-8f-b6-0d-7f')
def _define_SENSOR_TYPE_BOOLEAN_SWITCH():
    return Guid('9c7e371f-1041-460b-8d-5c-71-e4-75-2e-35-0c')
def _define_SENSOR_TYPE_MULTIVALUE_SWITCH():
    return Guid('b3ee4d76-37a4-4402-b2-5e-99-c6-0a-77-5f-a1')
def _define_SENSOR_TYPE_FORCE():
    return Guid('c2ab2b02-1a1c-4778-a8-1b-95-4a-17-88-cc-75')
def _define_SENSOR_TYPE_SCALE():
    return Guid('c06dd92c-7feb-438e-9b-f6-82-20-7f-ff-5b-b8')
def _define_SENSOR_TYPE_PRESSURE():
    return Guid('26d31f34-6352-41cf-b7-93-ea-07-13-d5-3d-77')
def _define_SENSOR_TYPE_STRAIN():
    return Guid('c6d1ec0e-6803-4361-ad-3d-85-bc-c5-8c-6d-29')
def _define_SENSOR_TYPE_BOOLEAN_SWITCH_ARRAY():
    return Guid('545c8ba5-b143-4545-86-8f-ca-7f-d9-86-b4-f6')
def _define_SENSOR_TYPE_HUMAN_PRESENCE():
    return Guid('c138c12b-ad52-451c-93-75-87-f5-18-ff-10-c6')
def _define_SENSOR_TYPE_HUMAN_PROXIMITY():
    return Guid('5220dae9-3179-4430-9f-90-06-26-6d-2a-34-de')
def _define_SENSOR_TYPE_TOUCH():
    return Guid('17db3018-06c4-4f7d-81-af-92-74-b7-59-9c-27')
def _define_SENSOR_TYPE_AMBIENT_LIGHT():
    return Guid('97f115c8-599a-4153-88-94-d2-d1-28-99-91-8a')
def _define_SENSOR_TYPE_RFID_SCANNER():
    return Guid('44328ef5-02dd-4e8d-ad-5d-92-49-83-2b-2e-ca')
def _define_SENSOR_TYPE_BARCODE_SCANNER():
    return Guid('990b3d8f-85bb-45ff-91-4d-99-8c-04-f3-72-df')
def _define_SENSOR_TYPE_CUSTOM():
    return Guid('e83af229-8640-4d18-a2-13-e2-26-75-eb-b2-c3')
def _define_SENSOR_TYPE_UNKNOWN():
    return Guid('10ba83e3-ef4f-41ed-98-85-a8-7d-64-35-a8-e1')
def _define_SENSOR_DATA_TYPE_COMMON_GUID():
    return Guid('db5e0cf2-cf1f-4c18-b4-6c-d8-60-11-d6-21-50')
def _define_SENSOR_DATA_TYPE_TIMESTAMP():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('db5e0cf2-cf1f-4c18-b4-6c-d8-60-11-d6-21-50'), pid=2)
def _define_SENSOR_DATA_TYPE_LOCATION_GUID():
    return Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4')
def _define_SENSOR_DATA_TYPE_LATITUDE_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=2)
def _define_SENSOR_DATA_TYPE_LONGITUDE_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=3)
def _define_SENSOR_DATA_TYPE_ALTITUDE_SEALEVEL_METERS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=4)
def _define_SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_METERS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=5)
def _define_SENSOR_DATA_TYPE_SPEED_KNOTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=6)
def _define_SENSOR_DATA_TYPE_TRUE_HEADING_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=7)
def _define_SENSOR_DATA_TYPE_MAGNETIC_HEADING_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=8)
def _define_SENSOR_DATA_TYPE_MAGNETIC_VARIATION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=9)
def _define_SENSOR_DATA_TYPE_FIX_QUALITY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=10)
def _define_SENSOR_DATA_TYPE_FIX_TYPE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=11)
def _define_SENSOR_DATA_TYPE_POSITION_DILUTION_OF_PRECISION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=12)
def _define_SENSOR_DATA_TYPE_HORIZONAL_DILUTION_OF_PRECISION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=13)
def _define_SENSOR_DATA_TYPE_VERTICAL_DILUTION_OF_PRECISION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=14)
def _define_SENSOR_DATA_TYPE_SATELLITES_USED_COUNT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=15)
def _define_SENSOR_DATA_TYPE_SATELLITES_USED_PRNS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=16)
def _define_SENSOR_DATA_TYPE_SATELLITES_IN_VIEW():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=17)
def _define_SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_PRNS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=18)
def _define_SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_ELEVATION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=19)
def _define_SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_AZIMUTH():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=20)
def _define_SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_STN_RATIO():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=21)
def _define_SENSOR_DATA_TYPE_ERROR_RADIUS_METERS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=22)
def _define_SENSOR_DATA_TYPE_ADDRESS1():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=23)
def _define_SENSOR_DATA_TYPE_ADDRESS2():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=24)
def _define_SENSOR_DATA_TYPE_CITY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=25)
def _define_SENSOR_DATA_TYPE_STATE_PROVINCE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=26)
def _define_SENSOR_DATA_TYPE_POSTALCODE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=27)
def _define_SENSOR_DATA_TYPE_COUNTRY_REGION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=28)
def _define_SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_ERROR_METERS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=29)
def _define_SENSOR_DATA_TYPE_ALTITUDE_SEALEVEL_ERROR_METERS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=30)
def _define_SENSOR_DATA_TYPE_GPS_SELECTION_MODE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=31)
def _define_SENSOR_DATA_TYPE_GPS_OPERATION_MODE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=32)
def _define_SENSOR_DATA_TYPE_GPS_STATUS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=33)
def _define_SENSOR_DATA_TYPE_GEOIDAL_SEPARATION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=34)
def _define_SENSOR_DATA_TYPE_DGPS_DATA_AGE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=35)
def _define_SENSOR_DATA_TYPE_ALTITUDE_ANTENNA_SEALEVEL_METERS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=36)
def _define_SENSOR_DATA_TYPE_DIFFERENTIAL_REFERENCE_STATION_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=37)
def _define_SENSOR_DATA_TYPE_NMEA_SENTENCE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=38)
def _define_SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=39)
def _define_SENSOR_DATA_TYPE_LOCATION_SOURCE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=40)
def _define_SENSOR_DATA_TYPE_SATELLITES_USED_PRNS_AND_CONSTELLATIONS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('055c74d8-ca6f-47d6-95-c6-1e-d3-63-7a-0f-f4'), pid=41)
def _define_SENSOR_DATA_TYPE_ENVIRONMENTAL_GUID():
    return Guid('8b0aa2f1-2d57-42ee-8c-c0-4d-27-62-2b-46-c4')
def _define_SENSOR_DATA_TYPE_TEMPERATURE_CELSIUS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8b0aa2f1-2d57-42ee-8c-c0-4d-27-62-2b-46-c4'), pid=2)
def _define_SENSOR_DATA_TYPE_RELATIVE_HUMIDITY_PERCENT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8b0aa2f1-2d57-42ee-8c-c0-4d-27-62-2b-46-c4'), pid=3)
def _define_SENSOR_DATA_TYPE_ATMOSPHERIC_PRESSURE_BAR():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8b0aa2f1-2d57-42ee-8c-c0-4d-27-62-2b-46-c4'), pid=4)
def _define_SENSOR_DATA_TYPE_WIND_DIRECTION_DEGREES_ANTICLOCKWISE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8b0aa2f1-2d57-42ee-8c-c0-4d-27-62-2b-46-c4'), pid=5)
def _define_SENSOR_DATA_TYPE_WIND_SPEED_METERS_PER_SECOND():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8b0aa2f1-2d57-42ee-8c-c0-4d-27-62-2b-46-c4'), pid=6)
def _define_SENSOR_DATA_TYPE_MOTION_GUID():
    return Guid('3f8a69a2-07c5-4e48-a9-65-cd-79-7a-ab-56-d5')
def _define_SENSOR_DATA_TYPE_ACCELERATION_X_G():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3f8a69a2-07c5-4e48-a9-65-cd-79-7a-ab-56-d5'), pid=2)
def _define_SENSOR_DATA_TYPE_ACCELERATION_Y_G():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3f8a69a2-07c5-4e48-a9-65-cd-79-7a-ab-56-d5'), pid=3)
def _define_SENSOR_DATA_TYPE_ACCELERATION_Z_G():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3f8a69a2-07c5-4e48-a9-65-cd-79-7a-ab-56-d5'), pid=4)
def _define_SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_X_DEGREES_PER_SECOND_SQUARED():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3f8a69a2-07c5-4e48-a9-65-cd-79-7a-ab-56-d5'), pid=5)
def _define_SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_Y_DEGREES_PER_SECOND_SQUARED():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3f8a69a2-07c5-4e48-a9-65-cd-79-7a-ab-56-d5'), pid=6)
def _define_SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_Z_DEGREES_PER_SECOND_SQUARED():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3f8a69a2-07c5-4e48-a9-65-cd-79-7a-ab-56-d5'), pid=7)
def _define_SENSOR_DATA_TYPE_SPEED_METERS_PER_SECOND():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3f8a69a2-07c5-4e48-a9-65-cd-79-7a-ab-56-d5'), pid=8)
def _define_SENSOR_DATA_TYPE_MOTION_STATE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3f8a69a2-07c5-4e48-a9-65-cd-79-7a-ab-56-d5'), pid=9)
def _define_SENSOR_DATA_TYPE_ANGULAR_VELOCITY_X_DEGREES_PER_SECOND():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3f8a69a2-07c5-4e48-a9-65-cd-79-7a-ab-56-d5'), pid=10)
def _define_SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Y_DEGREES_PER_SECOND():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3f8a69a2-07c5-4e48-a9-65-cd-79-7a-ab-56-d5'), pid=11)
def _define_SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Z_DEGREES_PER_SECOND():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('3f8a69a2-07c5-4e48-a9-65-cd-79-7a-ab-56-d5'), pid=12)
def _define_SENSOR_DATA_TYPE_ORIENTATION_GUID():
    return Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd')
def _define_SENSOR_DATA_TYPE_TILT_X_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=2)
def _define_SENSOR_DATA_TYPE_TILT_Y_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=3)
def _define_SENSOR_DATA_TYPE_TILT_Z_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=4)
def _define_SENSOR_DATA_TYPE_MAGNETIC_HEADING_X_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=5)
def _define_SENSOR_DATA_TYPE_MAGNETIC_HEADING_Y_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=6)
def _define_SENSOR_DATA_TYPE_MAGNETIC_HEADING_Z_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=7)
def _define_SENSOR_DATA_TYPE_DISTANCE_X_METERS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=8)
def _define_SENSOR_DATA_TYPE_DISTANCE_Y_METERS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=9)
def _define_SENSOR_DATA_TYPE_DISTANCE_Z_METERS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=10)
def _define_SENSOR_DATA_TYPE_MAGNETIC_HEADING_COMPENSATED_MAGNETIC_NORTH_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=11)
def _define_SENSOR_DATA_TYPE_MAGNETIC_HEADING_COMPENSATED_TRUE_NORTH_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=12)
def _define_SENSOR_DATA_TYPE_MAGNETIC_HEADING_MAGNETIC_NORTH_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=13)
def _define_SENSOR_DATA_TYPE_MAGNETIC_HEADING_TRUE_NORTH_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=14)
def _define_SENSOR_DATA_TYPE_QUADRANT_ANGLE_DEGREES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=15)
def _define_SENSOR_DATA_TYPE_ROTATION_MATRIX():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=16)
def _define_SENSOR_DATA_TYPE_QUATERNION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=17)
def _define_SENSOR_DATA_TYPE_SIMPLE_DEVICE_ORIENTATION():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=18)
def _define_SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_X_MILLIGAUSS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=19)
def _define_SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_Y_MILLIGAUSS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=20)
def _define_SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_Z_MILLIGAUSS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=21)
def _define_SENSOR_DATA_TYPE_MAGNETOMETER_ACCURACY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1637d8a2-4248-4275-86-5d-55-8d-e8-4a-ed-fd'), pid=22)
def _define_SENSOR_DATA_TYPE_GUID_MECHANICAL_GUID():
    return Guid('38564a7c-f2f2-49bb-9b-2b-ba-60-f6-6a-58-df')
def _define_SENSOR_DATA_TYPE_BOOLEAN_SWITCH_STATE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('38564a7c-f2f2-49bb-9b-2b-ba-60-f6-6a-58-df'), pid=2)
def _define_SENSOR_DATA_TYPE_MULTIVALUE_SWITCH_STATE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('38564a7c-f2f2-49bb-9b-2b-ba-60-f6-6a-58-df'), pid=3)
def _define_SENSOR_DATA_TYPE_FORCE_NEWTONS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('38564a7c-f2f2-49bb-9b-2b-ba-60-f6-6a-58-df'), pid=4)
def _define_SENSOR_DATA_TYPE_ABSOLUTE_PRESSURE_PASCAL():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('38564a7c-f2f2-49bb-9b-2b-ba-60-f6-6a-58-df'), pid=5)
def _define_SENSOR_DATA_TYPE_GAUGE_PRESSURE_PASCAL():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('38564a7c-f2f2-49bb-9b-2b-ba-60-f6-6a-58-df'), pid=6)
def _define_SENSOR_DATA_TYPE_STRAIN():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('38564a7c-f2f2-49bb-9b-2b-ba-60-f6-6a-58-df'), pid=7)
def _define_SENSOR_DATA_TYPE_WEIGHT_KILOGRAMS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('38564a7c-f2f2-49bb-9b-2b-ba-60-f6-6a-58-df'), pid=8)
def _define_SENSOR_DATA_TYPE_BOOLEAN_SWITCH_ARRAY_STATES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('38564a7c-f2f2-49bb-9b-2b-ba-60-f6-6a-58-df'), pid=10)
def _define_SENSOR_DATA_TYPE_BIOMETRIC_GUID():
    return Guid('2299288a-6d9e-4b0b-b7-ec-35-28-f8-9e-40-af')
def _define_SENSOR_DATA_TYPE_HUMAN_PRESENCE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2299288a-6d9e-4b0b-b7-ec-35-28-f8-9e-40-af'), pid=2)
def _define_SENSOR_DATA_TYPE_HUMAN_PROXIMITY_METERS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2299288a-6d9e-4b0b-b7-ec-35-28-f8-9e-40-af'), pid=3)
def _define_SENSOR_DATA_TYPE_TOUCH_STATE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('2299288a-6d9e-4b0b-b7-ec-35-28-f8-9e-40-af'), pid=4)
def _define_SENSOR_DATA_TYPE_LIGHT_GUID():
    return Guid('e4c77ce2-dcb7-46e9-84-39-4f-ec-54-88-33-a6')
def _define_SENSOR_DATA_TYPE_LIGHT_LEVEL_LUX():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e4c77ce2-dcb7-46e9-84-39-4f-ec-54-88-33-a6'), pid=2)
def _define_SENSOR_DATA_TYPE_LIGHT_TEMPERATURE_KELVIN():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e4c77ce2-dcb7-46e9-84-39-4f-ec-54-88-33-a6'), pid=3)
def _define_SENSOR_DATA_TYPE_LIGHT_CHROMACITY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e4c77ce2-dcb7-46e9-84-39-4f-ec-54-88-33-a6'), pid=4)
def _define_SENSOR_DATA_TYPE_SCANNER_GUID():
    return Guid('d7a59a3c-3421-44ab-8d-3a-9d-e8-ab-6c-4c-ae')
def _define_SENSOR_DATA_TYPE_RFID_TAG_40_BIT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('d7a59a3c-3421-44ab-8d-3a-9d-e8-ab-6c-4c-ae'), pid=2)
def _define_SENSOR_DATA_TYPE_ELECTRICAL_GUID():
    return Guid('bbb246d1-e242-4780-a2-d3-cd-ed-84-f3-58-42')
def _define_SENSOR_DATA_TYPE_VOLTAGE_VOLTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bbb246d1-e242-4780-a2-d3-cd-ed-84-f3-58-42'), pid=2)
def _define_SENSOR_DATA_TYPE_CURRENT_AMPS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bbb246d1-e242-4780-a2-d3-cd-ed-84-f3-58-42'), pid=3)
def _define_SENSOR_DATA_TYPE_CAPACITANCE_FARAD():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bbb246d1-e242-4780-a2-d3-cd-ed-84-f3-58-42'), pid=4)
def _define_SENSOR_DATA_TYPE_RESISTANCE_OHMS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bbb246d1-e242-4780-a2-d3-cd-ed-84-f3-58-42'), pid=5)
def _define_SENSOR_DATA_TYPE_INDUCTANCE_HENRY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bbb246d1-e242-4780-a2-d3-cd-ed-84-f3-58-42'), pid=6)
def _define_SENSOR_DATA_TYPE_ELECTRICAL_POWER_WATTS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bbb246d1-e242-4780-a2-d3-cd-ed-84-f3-58-42'), pid=7)
def _define_SENSOR_DATA_TYPE_ELECTRICAL_PERCENT_OF_RANGE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bbb246d1-e242-4780-a2-d3-cd-ed-84-f3-58-42'), pid=8)
def _define_SENSOR_DATA_TYPE_ELECTRICAL_FREQUENCY_HERTZ():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('bbb246d1-e242-4780-a2-d3-cd-ed-84-f3-58-42'), pid=9)
def _define_SENSOR_DATA_TYPE_CUSTOM_GUID():
    return Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f')
def _define_SENSOR_DATA_TYPE_CUSTOM_USAGE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=5)
def _define_SENSOR_DATA_TYPE_CUSTOM_BOOLEAN_ARRAY():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=6)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE1():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=7)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE2():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=8)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE3():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=9)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE4():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=10)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE5():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=11)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE6():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=12)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE7():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=13)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE8():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=14)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE9():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=15)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE10():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=16)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE11():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=17)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE12():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=18)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE13():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=19)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE14():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=20)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE15():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=21)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE16():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=22)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE17():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=23)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE18():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=24)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE19():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=25)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE20():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=26)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE21():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=27)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE22():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=28)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE23():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=29)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE24():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=30)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE25():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=31)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE26():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=32)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE27():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=33)
def _define_SENSOR_DATA_TYPE_CUSTOM_VALUE28():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('b14c764f-07cf-41e8-9d-82-eb-e3-d0-77-6a-6f'), pid=34)
def _define_SENSOR_PROPERTY_TEST_GUID():
    return Guid('e1e962f4-6e65-45f7-9c-36-d4-87-b7-b1-bd-34')
def _define_SENSOR_PROPERTY_CLEAR_ASSISTANCE_DATA():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e1e962f4-6e65-45f7-9c-36-d4-87-b7-b1-bd-34'), pid=2)
def _define_SENSOR_PROPERTY_TURN_ON_OFF_NMEA():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e1e962f4-6e65-45f7-9c-36-d4-87-b7-b1-bd-34'), pid=3)
GNSS_CLEAR_ALL_ASSISTANCE_DATA = 1
def _define_GUID_SensorCategory_All():
    return Guid('c317c286-c468-4288-99-75-d4-c4-58-7c-44-2c')
def _define_GUID_SensorCategory_Biometric():
    return Guid('ca19690f-a2c7-477d-a9-9e-99-ec-6e-2b-56-48')
def _define_GUID_SensorCategory_Electrical():
    return Guid('fb73fcd8-fc4a-483c-ac-58-27-b6-91-c6-be-ff')
def _define_GUID_SensorCategory_Environmental():
    return Guid('323439aa-7f66-492b-ba-0c-73-e9-aa-0a-65-d5')
def _define_GUID_SensorCategory_Light():
    return Guid('17a665c0-9063-4216-b2-02-5c-7a-25-5e-18-ce')
def _define_GUID_SensorCategory_Location():
    return Guid('bfa794e4-f964-4fdb-90-f6-51-05-6b-fe-4b-44')
def _define_GUID_SensorCategory_Mechanical():
    return Guid('8d131d68-8ef7-4656-80-b5-cc-cb-d9-37-91-c5')
def _define_GUID_SensorCategory_Motion():
    return Guid('cd09daf1-3b2e-4c3d-b5-98-b5-e5-ff-93-fd-46')
def _define_GUID_SensorCategory_Orientation():
    return Guid('9e6c04b6-96fe-4954-b7-26-68-68-2a-47-3f-69')
def _define_GUID_SensorCategory_Other():
    return Guid('2c90e7a9-f4c9-4fa2-af-37-56-d4-71-fe-5a-3d')
def _define_GUID_SensorCategory_PersonalActivity():
    return Guid('f1609081-1e12-412b-a1-4d-cb-b0-e9-5b-d2-e5')
def _define_GUID_SensorCategory_Scanner():
    return Guid('b000e77e-f5b5-420f-81-5d-02-70-a7-26-f2-70')
def _define_GUID_SensorCategory_Unsupported():
    return Guid('2beae7fa-19b0-48c5-a1-f6-b5-48-0d-c2-06-b0')
def _define_GUID_SensorType_Accelerometer3D():
    return Guid('c2fb0f5f-e2d2-4c78-bc-d0-35-2a-95-82-81-9d')
def _define_GUID_SensorType_ActivityDetection():
    return Guid('9d9e0118-1807-4f2e-96-e4-2c-e5-71-42-e1-96')
def _define_GUID_SensorType_AmbientLight():
    return Guid('97f115c8-599a-4153-88-94-d2-d1-28-99-91-8a')
def _define_GUID_SensorType_Barometer():
    return Guid('0e903829-ff8a-4a93-97-df-3d-cb-de-40-22-88')
def _define_GUID_SensorType_Custom():
    return Guid('e83af229-8640-4d18-a2-13-e2-26-75-eb-b2-c3')
def _define_GUID_SensorType_FloorElevation():
    return Guid('ade4987f-7ac4-4dfa-97-22-0a-02-71-81-c7-47')
def _define_GUID_SensorType_GeomagneticOrientation():
    return Guid('e77195f8-2d1f-4823-97-1b-1c-44-67-55-6c-9d')
def _define_GUID_SensorType_GravityVector():
    return Guid('03b52c73-bb76-463f-95-24-38-de-76-eb-70-0b')
def _define_GUID_SensorType_Gyrometer3D():
    return Guid('09485f5a-759e-42c2-bd-4b-a3-49-b7-5c-86-43')
def _define_GUID_SensorType_Humidity():
    return Guid('5c72bf67-bd7e-4257-99-0b-98-a3-ba-3b-40-0a')
def _define_GUID_SensorType_LinearAccelerometer():
    return Guid('038b0283-97b4-41c8-bc-24-5f-f1-aa-48-fe-c7')
def _define_GUID_SensorType_Magnetometer3D():
    return Guid('55e5effb-15c7-40df-86-98-a8-4b-7c-86-3c-53')
def _define_GUID_SensorType_Orientation():
    return Guid('cdb5d8f7-3cfd-41c8-85-42-cc-e6-22-cf-5d-6e')
def _define_GUID_SensorType_Pedometer():
    return Guid('b19f89af-e3eb-444b-8d-ea-20-25-75-a7-15-99')
def _define_GUID_SensorType_Proximity():
    return Guid('5220dae9-3179-4430-9f-90-06-26-6d-2a-34-de')
def _define_GUID_SensorType_RelativeOrientation():
    return Guid('40993b51-4706-44dc-98-d5-c9-20-c0-37-ff-ab')
def _define_GUID_SensorType_SimpleDeviceOrientation():
    return Guid('86a19291-0482-402c-bf-4c-ad-da-c5-2b-1c-39')
def _define_GUID_SensorType_Temperature():
    return Guid('04fd0ec4-d5da-45fa-95-a9-5d-b3-8e-e1-93-06')
def _define_GUID_SensorType_HingeAngle():
    return Guid('82358065-f4c4-4da1-b2-72-13-c2-33-32-a2-07')
SENSOR_PROPERTY_LIST_HEADER_SIZE = 8
def _define_GetPerformanceTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(UInt32))(('GetPerformanceTime', windll['SensorsUtilsV2.dll']), ((1, 'TimeMs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromFloat():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Single,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('InitPropVariantFromFloat', windll['SensorsUtilsV2.dll']), ((1, 'fltVal'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeyGetPropVariant():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),win32more.Foundation.BOOLEAN,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('PropKeyFindKeyGetPropVariant', windll['SensorsUtilsV2.dll']), ((1, 'pList'),(1, 'pKey'),(1, 'TypeCheck'),(1, 'pValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeySetPropVariant():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),win32more.Foundation.BOOLEAN,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('PropKeyFindKeySetPropVariant', windll['SensorsUtilsV2.dll']), ((1, 'pList'),(1, 'pKey'),(1, 'TypeCheck'),(1, 'pValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeyGetFileTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Foundation.FILETIME_head))(('PropKeyFindKeyGetFileTime', windll['SensorsUtilsV2.dll']), ((1, 'pList'),(1, 'pKey'),(1, 'pRetValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeyGetGuid():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(Guid))(('PropKeyFindKeyGetGuid', windll['SensorsUtilsV2.dll']), ((1, 'pList'),(1, 'pKey'),(1, 'pRetValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeyGetBool():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Foundation.BOOL))(('PropKeyFindKeyGetBool', windll['SensorsUtilsV2.dll']), ((1, 'pList'),(1, 'pKey'),(1, 'pRetValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeyGetUlong():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(UInt32))(('PropKeyFindKeyGetUlong', windll['SensorsUtilsV2.dll']), ((1, 'pList'),(1, 'pKey'),(1, 'pRetValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeyGetUshort():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(UInt16))(('PropKeyFindKeyGetUshort', windll['SensorsUtilsV2.dll']), ((1, 'pList'),(1, 'pKey'),(1, 'pRetValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeyGetFloat():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(Single))(('PropKeyFindKeyGetFloat', windll['SensorsUtilsV2.dll']), ((1, 'pList'),(1, 'pKey'),(1, 'pRetValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeyGetDouble():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(Double))(('PropKeyFindKeyGetDouble', windll['SensorsUtilsV2.dll']), ((1, 'pList'),(1, 'pKey'),(1, 'pRetValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeyGetInt32():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(Int32))(('PropKeyFindKeyGetInt32', windll['SensorsUtilsV2.dll']), ((1, 'pList'),(1, 'pKey'),(1, 'pRetValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeyGetInt64():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(Int64))(('PropKeyFindKeyGetInt64', windll['SensorsUtilsV2.dll']), ((1, 'pList'),(1, 'pKey'),(1, 'pRetValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeyGetNthUlong():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),UInt32,POINTER(UInt32))(('PropKeyFindKeyGetNthUlong', windll['SensorsUtilsV2.dll']), ((1, 'pList'),(1, 'pKey'),(1, 'Occurrence'),(1, 'pRetValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeyGetNthUshort():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),UInt32,POINTER(UInt16))(('PropKeyFindKeyGetNthUshort', windll['SensorsUtilsV2.dll']), ((1, 'pList'),(1, 'pKey'),(1, 'Occurrence'),(1, 'pRetValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeyGetNthInt64():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),UInt32,POINTER(Int64))(('PropKeyFindKeyGetNthInt64', windll['SensorsUtilsV2.dll']), ((1, 'pList'),(1, 'pKey'),(1, 'Occurrence'),(1, 'pRetValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsKeyPresentInPropertyList():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.Devices.Sensors.SENSOR_PROPERTY_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head))(('IsKeyPresentInPropertyList', windll['SensorsUtilsV2.dll']), ((1, 'pList'),(1, 'pKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsKeyPresentInCollectionList():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head))(('IsKeyPresentInCollectionList', windll['SensorsUtilsV2.dll']), ((1, 'pList'),(1, 'pKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsCollectionListSame():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head))(('IsCollectionListSame', windll['SensorsUtilsV2.dll']), ((1, 'ListA'),(1, 'ListB'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantGetInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(UInt32),POINTER(UInt32),POINTER(c_void_p),POINTER(UInt32))(('PropVariantGetInformation', windll['SensorsUtilsV2.dll']), ((1, 'PropVariantValue'),(1, 'PropVariantOffset'),(1, 'PropVariantSize'),(1, 'PropVariantPointer'),(1, 'RemappedType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropertiesListCopy():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_PROPERTY_LIST_head),POINTER(win32more.Devices.Sensors.SENSOR_PROPERTY_LIST_head))(('PropertiesListCopy', windll['SensorsUtilsV2.dll']), ((1, 'Target'),(1, 'Source'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropertiesListGetFillableCount():
    try:
        return WINFUNCTYPE(UInt32,UInt32)(('PropertiesListGetFillableCount', windll['SensorsUtilsV2.dll']), ((1, 'BufferSizeBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CollectionsListGetMarshalledSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head))(('CollectionsListGetMarshalledSize', windll['SensorsUtilsV2.dll']), ((1, 'Collection'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CollectionsListCopyAndMarshall():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head))(('CollectionsListCopyAndMarshall', windll['SensorsUtilsV2.dll']), ((1, 'Target'),(1, 'Source'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CollectionsListMarshall():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head))(('CollectionsListMarshall', windll['SensorsUtilsV2.dll']), ((1, 'Target'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CollectionsListGetMarshalledSizeWithoutSerialization():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head))(('CollectionsListGetMarshalledSizeWithoutSerialization', windll['SensorsUtilsV2.dll']), ((1, 'Collection'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CollectionsListUpdateMarshalledPointer():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head))(('CollectionsListUpdateMarshalledPointer', windll['SensorsUtilsV2.dll']), ((1, 'Collection'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SerializationBufferAllocate():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt32,POINTER(c_char_p_no))(('SerializationBufferAllocate', windll['SensorsUtilsV2.dll']), ((1, 'SizeInBytes'),(1, 'pBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SerializationBufferFree():
    try:
        return WINFUNCTYPE(Void,c_char_p_no)(('SerializationBufferFree', windll['SensorsUtilsV2.dll']), ((1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CollectionsListGetSerializedSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head))(('CollectionsListGetSerializedSize', windll['SensorsUtilsV2.dll']), ((1, 'Collection'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CollectionsListSerializeToBuffer():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),UInt32,c_char_p_no)(('CollectionsListSerializeToBuffer', windll['SensorsUtilsV2.dll']), ((1, 'SourceCollection'),(1, 'TargetBufferSizeInBytes'),(1, 'TargetBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CollectionsListAllocateBufferAndSerialize():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(UInt32),POINTER(c_char_p_no))(('CollectionsListAllocateBufferAndSerialize', windll['SensorsUtilsV2.dll']), ((1, 'SourceCollection'),(1, 'pTargetBufferSizeInBytes'),(1, 'pTargetBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CollectionsListDeserializeFromBuffer():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt32,c_char_p_no,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head))(('CollectionsListDeserializeFromBuffer', windll['SensorsUtilsV2.dll']), ((1, 'SourceBufferSizeInBytes'),(1, 'SourceBuffer'),(1, 'TargetCollection'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SensorCollectionGetAt():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt32,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('SensorCollectionGetAt', windll['SensorsUtilsV2.dll']), ((1, 'Index'),(1, 'pSensorsList'),(1, 'pKey'),(1, 'pValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CollectionsListGetFillableCount():
    try:
        return WINFUNCTYPE(UInt32,UInt32)(('CollectionsListGetFillableCount', windll['SensorsUtilsV2.dll']), ((1, 'BufferSizeBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvaluateActivityThresholds():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head))(('EvaluateActivityThresholds', windll['SensorsUtilsV2.dll']), ((1, 'newSample'),(1, 'oldSample'),(1, 'thresholds'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CollectionsListSortSubscribedActivitiesByConfidence():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head))(('CollectionsListSortSubscribedActivitiesByConfidence', windll['SensorsUtilsV2.dll']), ((1, 'thresholds'),(1, 'pCollection'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromCLSIDArray():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(('InitPropVariantFromCLSIDArray', windll['SensorsUtilsV2.dll']), ((1, 'members'),(1, 'size'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsSensorSubscribed():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),Guid)(('IsSensorSubscribed', windll['SensorsUtilsV2.dll']), ((1, 'subscriptionList'),(1, 'currentType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsGUIDPresentInList():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(Guid),UInt32,POINTER(Guid))(('IsGUIDPresentInList', windll['SensorsUtilsV2.dll']), ((1, 'guidArray'),(1, 'arrayLength'),(1, 'guidElem'),))
    except (FileNotFoundError, AttributeError):
        return None
AXIS = Int32
AXIS_X = 0
AXIS_Y = 1
AXIS_Z = 2
AXIS_MAX = 3
ELEVATION_CHANGE_MODE = Int32
ElevationChangeMode_Unknown = 0
ElevationChangeMode_Elevator = 1
ElevationChangeMode_Stepping = 2
ElevationChangeMode_Max = 3
ElevationChangeMode_Force_Dword = -1
HUMAN_PRESENCE_DETECTION_TYPE = Int32
HumanPresenceDetectionType_VendorDefinedNonBiometric = 1
HumanPresenceDetectionType_VendorDefinedBiometric = 2
HumanPresenceDetectionType_FacialBiometric = 4
HumanPresenceDetectionType_AudioBiometric = 8
HumanPresenceDetectionType_Force_Dword = -1
HUMAN_PRESENCE_DETECTION_TYPE_COUNT = Int32
HUMAN_PRESENCE_DETECTION_TYPE_COUNT_HumanPresenceDetectionTypeCount = 4
def _define_ILocationPermissions_head():
    class ILocationPermissions(win32more.System.Com.IUnknown_head):
        Guid = Guid('d5fb0a7f-e74e-44f5-8e-02-48-06-86-3a-27-4f')
    return ILocationPermissions
def _define_ILocationPermissions():
    ILocationPermissions = win32more.Devices.Sensors.ILocationPermissions_head
    ILocationPermissions.GetGlobalLocationPermission = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(3, 'GetGlobalLocationPermission', ((1, 'pfEnabled'),)))
    ILocationPermissions.CheckLocationCapability = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'CheckLocationCapability', ((1, 'dwClientThreadId'),)))
    win32more.System.Com.IUnknown
    return ILocationPermissions
def _define_ISensor_head():
    class ISensor(win32more.System.Com.IUnknown_head):
        Guid = Guid('5fa08f80-2657-458e-af-75-46-f7-3f-a6-ac-5c')
    return ISensor
def _define_ISensor():
    ISensor = win32more.Devices.Sensors.ISensor_head
    ISensor.GetID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(3, 'GetID', ((1, 'pID'),)))
    ISensor.GetCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(4, 'GetCategory', ((1, 'pSensorCategory'),)))
    ISensor.GetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(5, 'GetType', ((1, 'pSensorType'),)))
    ISensor.GetFriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(6, 'GetFriendlyName', ((1, 'pFriendlyName'),)))
    ISensor.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(7, 'GetProperty', ((1, 'key'),(1, 'pProperty'),)))
    ISensor.GetProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head,POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head))(8, 'GetProperties', ((1, 'pKeys'),(1, 'ppProperties'),)))
    ISensor.GetSupportedDataFields = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head))(9, 'GetSupportedDataFields', ((1, 'ppDataFields'),)))
    ISensor.SetProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head))(10, 'SetProperties', ((1, 'pProperties'),(1, 'ppResults'),)))
    ISensor.SupportsDataField = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Foundation.VARIANT_BOOL))(11, 'SupportsDataField', ((1, 'key'),(1, 'pIsSupported'),)))
    ISensor.GetState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Sensors.SensorState))(12, 'GetState', ((1, 'pState'),)))
    ISensor.GetData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Sensors.ISensorDataReport_head))(13, 'GetData', ((1, 'ppDataReport'),)))
    ISensor.SupportsEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Foundation.VARIANT_BOOL))(14, 'SupportsEvent', ((1, 'eventGuid'),(1, 'pIsSupported'),)))
    ISensor.GetEventInterest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(Guid)),POINTER(UInt32))(15, 'GetEventInterest', ((1, 'ppValues'),(1, 'pCount'),)))
    ISensor.SetEventInterest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32)(16, 'SetEventInterest', ((1, 'pValues'),(1, 'count'),)))
    ISensor.SetEventSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Sensors.ISensorEvents_head)(17, 'SetEventSink', ((1, 'pEvents'),)))
    win32more.System.Com.IUnknown
    return ISensor
def _define_ISensorCollection_head():
    class ISensorCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('23571e11-e545-4dd8-a3-37-b8-9b-f4-4b-10-df')
    return ISensorCollection
def _define_ISensorCollection():
    ISensorCollection = win32more.Devices.Sensors.ISensorCollection_head
    ISensorCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Devices.Sensors.ISensor_head))(3, 'GetAt', ((1, 'ulIndex'),(1, 'ppSensor'),)))
    ISensorCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(4, 'GetCount', ((1, 'pCount'),)))
    ISensorCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Sensors.ISensor_head)(5, 'Add', ((1, 'pSensor'),)))
    ISensorCollection.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Sensors.ISensor_head)(6, 'Remove', ((1, 'pSensor'),)))
    ISensorCollection.RemoveByID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(7, 'RemoveByID', ((1, 'sensorID'),)))
    ISensorCollection.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'Clear', ()))
    win32more.System.Com.IUnknown
    return ISensorCollection
def _define_ISensorDataReport_head():
    class ISensorDataReport(win32more.System.Com.IUnknown_head):
        Guid = Guid('0ab9df9b-c4b5-4796-88-98-04-70-70-6a-2e-1d')
    return ISensorDataReport
def _define_ISensorDataReport():
    ISensorDataReport = win32more.Devices.Sensors.ISensorDataReport_head
    ISensorDataReport.GetTimestamp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.SYSTEMTIME_head))(3, 'GetTimestamp', ((1, 'pTimeStamp'),)))
    ISensorDataReport.GetSensorValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(4, 'GetSensorValue', ((1, 'pKey'),(1, 'pValue'),)))
    ISensorDataReport.GetSensorValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head,POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head))(5, 'GetSensorValues', ((1, 'pKeys'),(1, 'ppValues'),)))
    win32more.System.Com.IUnknown
    return ISensorDataReport
def _define_ISensorEvents_head():
    class ISensorEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('5d8dcc91-4641-47e7-b7-c3-b7-4f-48-a6-c3-91')
    return ISensorEvents
def _define_ISensorEvents():
    ISensorEvents = win32more.Devices.Sensors.ISensorEvents_head
    ISensorEvents.OnStateChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Sensors.ISensor_head,win32more.Devices.Sensors.SensorState)(3, 'OnStateChanged', ((1, 'pSensor'),(1, 'state'),)))
    ISensorEvents.OnDataUpdated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Sensors.ISensor_head,win32more.Devices.Sensors.ISensorDataReport_head)(4, 'OnDataUpdated', ((1, 'pSensor'),(1, 'pNewData'),)))
    ISensorEvents.OnEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Sensors.ISensor_head,POINTER(Guid),win32more.Devices.PortableDevices.IPortableDeviceValues_head)(5, 'OnEvent', ((1, 'pSensor'),(1, 'eventID'),(1, 'pEventData'),)))
    ISensorEvents.OnLeave = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(6, 'OnLeave', ((1, 'ID'),)))
    win32more.System.Com.IUnknown
    return ISensorEvents
def _define_ISensorManager_head():
    class ISensorManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('bd77db67-45a8-42dc-8d-00-6d-cf-15-f8-37-7a')
    return ISensorManager
def _define_ISensorManager():
    ISensorManager = win32more.Devices.Sensors.ISensorManager_head
    ISensorManager.GetSensorsByCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.Sensors.ISensorCollection_head))(3, 'GetSensorsByCategory', ((1, 'sensorCategory'),(1, 'ppSensorsFound'),)))
    ISensorManager.GetSensorsByType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.Sensors.ISensorCollection_head))(4, 'GetSensorsByType', ((1, 'sensorType'),(1, 'ppSensorsFound'),)))
    ISensorManager.GetSensorByID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.Sensors.ISensor_head))(5, 'GetSensorByID', ((1, 'sensorID'),(1, 'ppSensor'),)))
    ISensorManager.SetEventSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Sensors.ISensorManagerEvents_head)(6, 'SetEventSink', ((1, 'pEvents'),)))
    ISensorManager.RequestPermissions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Devices.Sensors.ISensorCollection_head,win32more.Foundation.BOOL)(7, 'RequestPermissions', ((1, 'hParent'),(1, 'pSensors'),(1, 'fModal'),)))
    win32more.System.Com.IUnknown
    return ISensorManager
def _define_ISensorManagerEvents_head():
    class ISensorManagerEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('9b3b0b86-266a-4aad-b2-1f-fd-e5-50-10-01-b7')
    return ISensorManagerEvents
def _define_ISensorManagerEvents():
    ISensorManagerEvents = win32more.Devices.Sensors.ISensorManagerEvents_head
    ISensorManagerEvents.OnSensorEnter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Sensors.ISensor_head,win32more.Devices.Sensors.SensorState)(3, 'OnSensorEnter', ((1, 'pSensor'),(1, 'state'),)))
    win32more.System.Com.IUnknown
    return ISensorManagerEvents
LOCATION_DESIRED_ACCURACY = Int32
LOCATION_DESIRED_ACCURACY_DEFAULT = 0
LOCATION_DESIRED_ACCURACY_HIGH = 1
LOCATION_POSITION_SOURCE = Int32
LOCATION_POSITION_SOURCE_CELLULAR = 0
LOCATION_POSITION_SOURCE_SATELLITE = 1
LOCATION_POSITION_SOURCE_WIFI = 2
LOCATION_POSITION_SOURCE_IPADDRESS = 3
LOCATION_POSITION_SOURCE_UNKNOWN = 4
MAGNETOMETER_ACCURACY = Int32
MagnetometerAccuracy_Unknown = 0
MagnetometerAccuracy_Unreliable = 1
MagnetometerAccuracy_Approximate = 2
MagnetometerAccuracy_High = 3
MagnetometerAccuracy = Int32
MAGNETOMETER_ACCURACY_UNKNOWN = 0
MAGNETOMETER_ACCURACY_UNRELIABLE = 1
MAGNETOMETER_ACCURACY_APPROXIMATE = 2
MAGNETOMETER_ACCURACY_HIGH = 3
def _define_MATRIX3X3_head():
    class MATRIX3X3(Structure):
        pass
    return MATRIX3X3
def _define_MATRIX3X3():
    MATRIX3X3 = win32more.Devices.Sensors.MATRIX3X3_head
    class MATRIX3X3__Anonymous_e__Union(Union):
        pass
    class MATRIX3X3__Anonymous_e__Union__Anonymous1_e__Struct(Structure):
        pass
    MATRIX3X3__Anonymous_e__Union__Anonymous1_e__Struct._fields_ = [
        ('A11', Single),
        ('A12', Single),
        ('A13', Single),
        ('A21', Single),
        ('A22', Single),
        ('A23', Single),
        ('A31', Single),
        ('A32', Single),
        ('A33', Single),
    ]
    class MATRIX3X3__Anonymous_e__Union__Anonymous2_e__Struct(Structure):
        pass
    MATRIX3X3__Anonymous_e__Union__Anonymous2_e__Struct._fields_ = [
        ('V1', win32more.Devices.Sensors.VEC3D),
        ('V2', win32more.Devices.Sensors.VEC3D),
        ('V3', win32more.Devices.Sensors.VEC3D),
    ]
    MATRIX3X3__Anonymous_e__Union._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    MATRIX3X3__Anonymous_e__Union._fields_ = [
        ('Anonymous1', MATRIX3X3__Anonymous_e__Union__Anonymous1_e__Struct),
        ('Anonymous2', MATRIX3X3__Anonymous_e__Union__Anonymous2_e__Struct),
        ('M', Single * 9),
    ]
    MATRIX3X3._anonymous_ = [
        'Anonymous',
    ]
    MATRIX3X3._fields_ = [
        ('Anonymous', MATRIX3X3__Anonymous_e__Union),
    ]
    return MATRIX3X3
PEDOMETER_STEP_TYPE = Int32
PedometerStepType_Unknown = 1
PedometerStepType_Walking = 2
PedometerStepType_Running = 4
PedometerStepType_Max = 8
PedometerStepType_Force_Dword = -1
PEDOMETER_STEP_TYPE_COUNT = Int32
PEDOMETER_STEP_TYPE_COUNT_PedometerStepTypeCount = 3
PROXIMITY_TYPE = Int32
ProximityType_ObjectProximity = 0
ProximityType_HumanProximity = 1
ProximityType_Force_Dword = -1
def _define_QUATERNION_head():
    class QUATERNION(Structure):
        pass
    return QUATERNION
def _define_QUATERNION():
    QUATERNION = win32more.Devices.Sensors.QUATERNION_head
    QUATERNION._fields_ = [
        ('X', Single),
        ('Y', Single),
        ('Z', Single),
        ('W', Single),
    ]
    return QUATERNION
Sensor = Guid('e97ced00-523a-4133-bf-6f-d3-a2-da-e7-f6-ba')
def _define_SENSOR_COLLECTION_LIST_head():
    class SENSOR_COLLECTION_LIST(Structure):
        pass
    return SENSOR_COLLECTION_LIST
def _define_SENSOR_COLLECTION_LIST():
    SENSOR_COLLECTION_LIST = win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head
    SENSOR_COLLECTION_LIST._fields_ = [
        ('AllocatedSizeInBytes', UInt32),
        ('Count', UInt32),
        ('List', win32more.Devices.Sensors.SENSOR_VALUE_PAIR * 1),
    ]
    return SENSOR_COLLECTION_LIST
SENSOR_CONNECTION_TYPES = Int32
SensorConnectionType_Integrated = 0
SensorConnectionType_Attached = 1
SensorConnectionType_External = 2
def _define_SENSOR_PROPERTY_LIST_head():
    class SENSOR_PROPERTY_LIST(Structure):
        pass
    return SENSOR_PROPERTY_LIST
def _define_SENSOR_PROPERTY_LIST():
    SENSOR_PROPERTY_LIST = win32more.Devices.Sensors.SENSOR_PROPERTY_LIST_head
    SENSOR_PROPERTY_LIST._fields_ = [
        ('AllocatedSizeInBytes', UInt32),
        ('Count', UInt32),
        ('List', win32more.UI.Shell.PropertiesSystem.PROPERTYKEY * 1),
    ]
    return SENSOR_PROPERTY_LIST
SENSOR_STATE = Int32
SensorState_Initializing = 0
SensorState_Idle = 1
SensorState_Active = 2
SensorState_Error = 3
def _define_SENSOR_VALUE_PAIR_head():
    class SENSOR_VALUE_PAIR(Structure):
        pass
    return SENSOR_VALUE_PAIR
def _define_SENSOR_VALUE_PAIR():
    SENSOR_VALUE_PAIR = win32more.Devices.Sensors.SENSOR_VALUE_PAIR_head
    SENSOR_VALUE_PAIR._fields_ = [
        ('Key', win32more.UI.Shell.PropertiesSystem.PROPERTYKEY),
        ('Value', win32more.System.Com.StructuredStorage.PROPVARIANT),
    ]
    return SENSOR_VALUE_PAIR
SensorCollection = Guid('79c43adb-a429-469f-aa-39-2f-2b-74-b7-59-37')
SensorConnectionType = Int32
SENSOR_CONNECTION_TYPE_PC_INTEGRATED = 0
SENSOR_CONNECTION_TYPE_PC_ATTACHED = 1
SENSOR_CONNECTION_TYPE_PC_EXTERNAL = 2
SensorDataReport = Guid('4ea9d6ef-694b-4218-88-16-cc-da-8d-a7-4b-ba')
SensorManager = Guid('77a1c827-fcd2-4689-89-15-9d-61-3c-c5-fa-3e')
SensorState = Int32
SENSOR_STATE_MIN = 0
SENSOR_STATE_READY = 0
SENSOR_STATE_NOT_AVAILABLE = 1
SENSOR_STATE_NO_DATA = 2
SENSOR_STATE_INITIALIZING = 3
SENSOR_STATE_ACCESS_DENIED = 4
SENSOR_STATE_ERROR = 5
SENSOR_STATE_MAX = 5
SIMPLE_DEVICE_ORIENTATION = Int32
SimpleDeviceOrientation_NotRotated = 0
SimpleDeviceOrientation_Rotated90DegreesCounterclockwise = 1
SimpleDeviceOrientation_Rotated180DegreesCounterclockwise = 2
SimpleDeviceOrientation_Rotated270DegreesCounterclockwise = 3
SimpleDeviceOrientation_Faceup = 4
SimpleDeviceOrientation_Facedown = 5
SimpleDeviceOrientation = Int32
SIMPLE_DEVICE_ORIENTATION_NOT_ROTATED = 0
SIMPLE_DEVICE_ORIENTATION_ROTATED_90 = 1
SIMPLE_DEVICE_ORIENTATION_ROTATED_180 = 2
SIMPLE_DEVICE_ORIENTATION_ROTATED_270 = 3
SIMPLE_DEVICE_ORIENTATION_ROTATED_FACE_UP = 4
SIMPLE_DEVICE_ORIENTATION_ROTATED_FACE_DOWN = 5
def _define_VEC3D_head():
    class VEC3D(Structure):
        pass
    return VEC3D
def _define_VEC3D():
    VEC3D = win32more.Devices.Sensors.VEC3D_head
    VEC3D._fields_ = [
        ('X', Single),
        ('Y', Single),
        ('Z', Single),
    ]
    return VEC3D
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
