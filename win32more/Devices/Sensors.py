from win32more import *
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
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
GUID_DEVINTERFACE_SENSOR = 'ba1bb692-9b7a-4833-9a1e-525ed134e7e2'
SENSOR_EVENT_STATE_CHANGED = 'bfd96016-6bd7-4560-ad34-f2f6607e8f81'
SENSOR_EVENT_DATA_UPDATED = '2ed0f2a4-0087-41d3-87db-6773370b3c88'
SENSOR_EVENT_PROPERTY_CHANGED = '2358f099-84c9-4d3d-90df-c2421e2b2045'
SENSOR_EVENT_ACCELEROMETER_SHAKE = '825f5a94-0f48-4396-9ca0-6ecb5c99d915'
SENSOR_EVENT_PARAMETER_COMMON_GUID = '64346e30-8728-4b34-bdf6-4f52442c5c28'
SENSOR_EVENT_PARAMETER_EVENT_ID = PROPERTYKEY(Fmtid='64346e30-8728-4b34-bdf6-4f52442c5c28', Pid=2)
SENSOR_EVENT_PARAMETER_STATE = PROPERTYKEY(Fmtid='64346e30-8728-4b34-bdf6-4f52442c5c28', Pid=3)
SENSOR_ERROR_PARAMETER_COMMON_GUID = '77112bcd-fce1-4f43-b8b8-a88256adb4b3'
SENSOR_PROPERTY_COMMON_GUID = '7f8383ec-d3ec-495c-a8cf-b8bbe85c2920'
SENSOR_PROPERTY_TYPE = PROPERTYKEY(Fmtid='7f8383ec-d3ec-495c-a8cf-b8bbe85c2920', Pid=2)
SENSOR_PROPERTY_STATE = PROPERTYKEY(Fmtid='7f8383ec-d3ec-495c-a8cf-b8bbe85c2920', Pid=3)
SENSOR_PROPERTY_PERSISTENT_UNIQUE_ID = PROPERTYKEY(Fmtid='7f8383ec-d3ec-495c-a8cf-b8bbe85c2920', Pid=5)
SENSOR_PROPERTY_MANUFACTURER = PROPERTYKEY(Fmtid='7f8383ec-d3ec-495c-a8cf-b8bbe85c2920', Pid=6)
SENSOR_PROPERTY_MODEL = PROPERTYKEY(Fmtid='7f8383ec-d3ec-495c-a8cf-b8bbe85c2920', Pid=7)
SENSOR_PROPERTY_SERIAL_NUMBER = PROPERTYKEY(Fmtid='7f8383ec-d3ec-495c-a8cf-b8bbe85c2920', Pid=8)
SENSOR_PROPERTY_FRIENDLY_NAME = PROPERTYKEY(Fmtid='7f8383ec-d3ec-495c-a8cf-b8bbe85c2920', Pid=9)
SENSOR_PROPERTY_DESCRIPTION = PROPERTYKEY(Fmtid='7f8383ec-d3ec-495c-a8cf-b8bbe85c2920', Pid=10)
SENSOR_PROPERTY_CONNECTION_TYPE = PROPERTYKEY(Fmtid='7f8383ec-d3ec-495c-a8cf-b8bbe85c2920', Pid=11)
SENSOR_PROPERTY_MIN_REPORT_INTERVAL = PROPERTYKEY(Fmtid='7f8383ec-d3ec-495c-a8cf-b8bbe85c2920', Pid=12)
SENSOR_PROPERTY_CURRENT_REPORT_INTERVAL = PROPERTYKEY(Fmtid='7f8383ec-d3ec-495c-a8cf-b8bbe85c2920', Pid=13)
SENSOR_PROPERTY_CHANGE_SENSITIVITY = PROPERTYKEY(Fmtid='7f8383ec-d3ec-495c-a8cf-b8bbe85c2920', Pid=14)
SENSOR_PROPERTY_DEVICE_PATH = PROPERTYKEY(Fmtid='7f8383ec-d3ec-495c-a8cf-b8bbe85c2920', Pid=15)
SENSOR_PROPERTY_LIGHT_RESPONSE_CURVE = PROPERTYKEY(Fmtid='7f8383ec-d3ec-495c-a8cf-b8bbe85c2920', Pid=16)
SENSOR_PROPERTY_ACCURACY = PROPERTYKEY(Fmtid='7f8383ec-d3ec-495c-a8cf-b8bbe85c2920', Pid=17)
SENSOR_PROPERTY_RESOLUTION = PROPERTYKEY(Fmtid='7f8383ec-d3ec-495c-a8cf-b8bbe85c2920', Pid=18)
SENSOR_PROPERTY_LOCATION_DESIRED_ACCURACY = PROPERTYKEY(Fmtid='7f8383ec-d3ec-495c-a8cf-b8bbe85c2920', Pid=19)
SENSOR_PROPERTY_RANGE_MINIMUM = PROPERTYKEY(Fmtid='7f8383ec-d3ec-495c-a8cf-b8bbe85c2920', Pid=20)
SENSOR_PROPERTY_RANGE_MAXIMUM = PROPERTYKEY(Fmtid='7f8383ec-d3ec-495c-a8cf-b8bbe85c2920', Pid=21)
SENSOR_PROPERTY_HID_USAGE = PROPERTYKEY(Fmtid='7f8383ec-d3ec-495c-a8cf-b8bbe85c2920', Pid=22)
SENSOR_PROPERTY_RADIO_STATE = PROPERTYKEY(Fmtid='7f8383ec-d3ec-495c-a8cf-b8bbe85c2920', Pid=23)
SENSOR_PROPERTY_RADIO_STATE_PREVIOUS = PROPERTYKEY(Fmtid='7f8383ec-d3ec-495c-a8cf-b8bbe85c2920', Pid=24)
SENSOR_CATEGORY_ALL = 'c317c286-c468-4288-9975-d4c4587c442c'
SENSOR_CATEGORY_LOCATION = 'bfa794e4-f964-4fdb-90f6-51056bfe4b44'
SENSOR_CATEGORY_ENVIRONMENTAL = '323439aa-7f66-492b-ba0c-73e9aa0a65d5'
SENSOR_CATEGORY_MOTION = 'cd09daf1-3b2e-4c3d-b598-b5e5ff93fd46'
SENSOR_CATEGORY_ORIENTATION = '9e6c04b6-96fe-4954-b726-68682a473f69'
SENSOR_CATEGORY_MECHANICAL = '8d131d68-8ef7-4656-80b5-cccbd93791c5'
SENSOR_CATEGORY_ELECTRICAL = 'fb73fcd8-fc4a-483c-ac58-27b691c6beff'
SENSOR_CATEGORY_BIOMETRIC = 'ca19690f-a2c7-477d-a99e-99ec6e2b5648'
SENSOR_CATEGORY_LIGHT = '17a665c0-9063-4216-b202-5c7a255e18ce'
SENSOR_CATEGORY_SCANNER = 'b000e77e-f5b5-420f-815d-0270a726f270'
SENSOR_CATEGORY_OTHER = '2c90e7a9-f4c9-4fa2-af37-56d471fe5a3d'
SENSOR_CATEGORY_UNSUPPORTED = '2beae7fa-19b0-48c5-a1f6-b5480dc206b0'
SENSOR_TYPE_LOCATION_GPS = 'ed4ca589-327a-4ff9-a560-91da4b48275e'
SENSOR_TYPE_LOCATION_STATIC = '095f8184-0fa9-4445-8e6e-b70f320b6b4c'
SENSOR_TYPE_LOCATION_LOOKUP = '3b2eae4a-72ce-436d-96d2-3c5b8570e987'
SENSOR_TYPE_LOCATION_TRIANGULATION = '691c341a-5406-4fe1-942f-2246cbeb39e0'
SENSOR_TYPE_LOCATION_OTHER = '9b2d0566-0368-4f71-b88d-533f132031de'
SENSOR_TYPE_LOCATION_BROADCAST = 'd26988cf-5162-4039-bb17-4c58b698e44a'
SENSOR_TYPE_LOCATION_DEAD_RECKONING = '1a37d538-f28b-42da-9fce-a9d0a2a6d829'
SENSOR_TYPE_ENVIRONMENTAL_TEMPERATURE = '04fd0ec4-d5da-45fa-95a9-5db38ee19306'
SENSOR_TYPE_ENVIRONMENTAL_ATMOSPHERIC_PRESSURE = '0e903829-ff8a-4a93-97df-3dcbde402288'
SENSOR_TYPE_ENVIRONMENTAL_HUMIDITY = '5c72bf67-bd7e-4257-990b-98a3ba3b400a'
SENSOR_TYPE_ENVIRONMENTAL_WIND_SPEED = 'dd50607b-a45f-42cd-8efd-ec61761c4226'
SENSOR_TYPE_ENVIRONMENTAL_WIND_DIRECTION = '9ef57a35-9306-434d-af09-37fa5a9c00bd'
SENSOR_TYPE_ACCELEROMETER_1D = 'c04d2387-7340-4cc2-991e-3b18cb8ef2f4'
SENSOR_TYPE_ACCELEROMETER_2D = 'b2c517a8-f6b5-4ba6-a423-5df560b4cc07'
SENSOR_TYPE_ACCELEROMETER_3D = 'c2fb0f5f-e2d2-4c78-bcd0-352a9582819d'
SENSOR_TYPE_MOTION_DETECTOR = '5c7c1a12-30a5-43b9-a4b2-cf09ec5b7be8'
SENSOR_TYPE_GYROMETER_1D = 'fa088734-f552-4584-8324-edfaf649652c'
SENSOR_TYPE_GYROMETER_2D = '31ef4f83-919b-48bf-8de0-5d7a9d240556'
SENSOR_TYPE_GYROMETER_3D = '09485f5a-759e-42c2-bd4b-a349b75c8643'
SENSOR_TYPE_SPEEDOMETER = '6bd73c1f-0bb4-4310-81b2-dfc18a52bf94'
SENSOR_TYPE_COMPASS_1D = 'a415f6c5-cb50-49d0-8e62-a8270bd7a26c'
SENSOR_TYPE_COMPASS_2D = '15655cc0-997a-4d30-84db-57caba3648bb'
SENSOR_TYPE_COMPASS_3D = '76b5ce0d-17dd-414d-93a1-e127f40bdf6e'
SENSOR_TYPE_INCLINOMETER_1D = 'b96f98c5-7a75-4ba7-94e9-ac868c966dd8'
SENSOR_TYPE_INCLINOMETER_2D = 'ab140f6d-83eb-4264-b70b-b16a5b256a01'
SENSOR_TYPE_INCLINOMETER_3D = 'b84919fb-ea85-4976-8444-6f6f5c6d31db'
SENSOR_TYPE_DISTANCE_1D = '5f14ab2f-1407-4306-a93f-b1dbabe4f9c0'
SENSOR_TYPE_DISTANCE_2D = '5cf9a46c-a9a2-4e55-b6a1-a04aafa95a92'
SENSOR_TYPE_DISTANCE_3D = 'a20cae31-0e25-4772-9fe5-96608a1354b2'
SENSOR_TYPE_AGGREGATED_QUADRANT_ORIENTATION = '9f81f1af-c4ab-4307-9904-c828bfb90829'
SENSOR_TYPE_AGGREGATED_DEVICE_ORIENTATION = 'cdb5d8f7-3cfd-41c8-8542-cce622cf5d6e'
SENSOR_TYPE_AGGREGATED_SIMPLE_DEVICE_ORIENTATION = '86a19291-0482-402c-bf4c-addac52b1c39'
SENSOR_TYPE_VOLTAGE = 'c5484637-4fb7-4953-98b8-a56d8aa1fb1e'
SENSOR_TYPE_CURRENT = '5adc9fce-15a0-4bbe-a1ad-2d38a9ae831c'
SENSOR_TYPE_CAPACITANCE = 'ca2ffb1c-2317-49c0-a0b4-b63ce63461a0'
SENSOR_TYPE_RESISTANCE = '9993d2c8-c157-4a52-a7b5-195c76037231'
SENSOR_TYPE_INDUCTANCE = 'dc1d933f-c435-4c7d-a2fe-607192a524d3'
SENSOR_TYPE_ELECTRICAL_POWER = '212f10f5-14ab-4376-9a43-a7794098c2fe'
SENSOR_TYPE_POTENTIOMETER = '2b3681a9-cadc-45aa-a6ff-54957c8bb440'
SENSOR_TYPE_FREQUENCY = '8cd2cbb6-73e6-4640-a709-72ae8fb60d7f'
SENSOR_TYPE_BOOLEAN_SWITCH = '9c7e371f-1041-460b-8d5c-71e4752e350c'
SENSOR_TYPE_MULTIVALUE_SWITCH = 'b3ee4d76-37a4-4402-b25e-99c60a775fa1'
SENSOR_TYPE_FORCE = 'c2ab2b02-1a1c-4778-a81b-954a1788cc75'
SENSOR_TYPE_SCALE = 'c06dd92c-7feb-438e-9bf6-82207fff5bb8'
SENSOR_TYPE_PRESSURE = '26d31f34-6352-41cf-b793-ea0713d53d77'
SENSOR_TYPE_STRAIN = 'c6d1ec0e-6803-4361-ad3d-85bcc58c6d29'
SENSOR_TYPE_BOOLEAN_SWITCH_ARRAY = '545c8ba5-b143-4545-868f-ca7fd986b4f6'
SENSOR_TYPE_HUMAN_PRESENCE = 'c138c12b-ad52-451c-9375-87f518ff10c6'
SENSOR_TYPE_HUMAN_PROXIMITY = '5220dae9-3179-4430-9f90-06266d2a34de'
SENSOR_TYPE_TOUCH = '17db3018-06c4-4f7d-81af-9274b7599c27'
SENSOR_TYPE_AMBIENT_LIGHT = '97f115c8-599a-4153-8894-d2d12899918a'
SENSOR_TYPE_RFID_SCANNER = '44328ef5-02dd-4e8d-ad5d-9249832b2eca'
SENSOR_TYPE_BARCODE_SCANNER = '990b3d8f-85bb-45ff-914d-998c04f372df'
SENSOR_TYPE_CUSTOM = 'e83af229-8640-4d18-a213-e22675ebb2c3'
SENSOR_TYPE_UNKNOWN = '10ba83e3-ef4f-41ed-9885-a87d6435a8e1'
SENSOR_DATA_TYPE_COMMON_GUID = 'db5e0cf2-cf1f-4c18-b46c-d86011d62150'
SENSOR_DATA_TYPE_TIMESTAMP = PROPERTYKEY(Fmtid='db5e0cf2-cf1f-4c18-b46c-d86011d62150', Pid=2)
SENSOR_DATA_TYPE_LOCATION_GUID = '055c74d8-ca6f-47d6-95c6-1ed3637a0ff4'
SENSOR_DATA_TYPE_LATITUDE_DEGREES = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=2)
SENSOR_DATA_TYPE_LONGITUDE_DEGREES = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=3)
SENSOR_DATA_TYPE_ALTITUDE_SEALEVEL_METERS = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=4)
SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_METERS = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=5)
SENSOR_DATA_TYPE_SPEED_KNOTS = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=6)
SENSOR_DATA_TYPE_TRUE_HEADING_DEGREES = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=7)
SENSOR_DATA_TYPE_MAGNETIC_HEADING_DEGREES = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=8)
SENSOR_DATA_TYPE_MAGNETIC_VARIATION = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=9)
SENSOR_DATA_TYPE_FIX_QUALITY = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=10)
SENSOR_DATA_TYPE_FIX_TYPE = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=11)
SENSOR_DATA_TYPE_POSITION_DILUTION_OF_PRECISION = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=12)
SENSOR_DATA_TYPE_HORIZONAL_DILUTION_OF_PRECISION = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=13)
SENSOR_DATA_TYPE_VERTICAL_DILUTION_OF_PRECISION = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=14)
SENSOR_DATA_TYPE_SATELLITES_USED_COUNT = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=15)
SENSOR_DATA_TYPE_SATELLITES_USED_PRNS = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=16)
SENSOR_DATA_TYPE_SATELLITES_IN_VIEW = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=17)
SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_PRNS = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=18)
SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_ELEVATION = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=19)
SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_AZIMUTH = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=20)
SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_STN_RATIO = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=21)
SENSOR_DATA_TYPE_ERROR_RADIUS_METERS = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=22)
SENSOR_DATA_TYPE_ADDRESS1 = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=23)
SENSOR_DATA_TYPE_ADDRESS2 = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=24)
SENSOR_DATA_TYPE_CITY = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=25)
SENSOR_DATA_TYPE_STATE_PROVINCE = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=26)
SENSOR_DATA_TYPE_POSTALCODE = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=27)
SENSOR_DATA_TYPE_COUNTRY_REGION = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=28)
SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_ERROR_METERS = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=29)
SENSOR_DATA_TYPE_ALTITUDE_SEALEVEL_ERROR_METERS = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=30)
SENSOR_DATA_TYPE_GPS_SELECTION_MODE = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=31)
SENSOR_DATA_TYPE_GPS_OPERATION_MODE = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=32)
SENSOR_DATA_TYPE_GPS_STATUS = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=33)
SENSOR_DATA_TYPE_GEOIDAL_SEPARATION = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=34)
SENSOR_DATA_TYPE_DGPS_DATA_AGE = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=35)
SENSOR_DATA_TYPE_ALTITUDE_ANTENNA_SEALEVEL_METERS = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=36)
SENSOR_DATA_TYPE_DIFFERENTIAL_REFERENCE_STATION_ID = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=37)
SENSOR_DATA_TYPE_NMEA_SENTENCE = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=38)
SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_ID = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=39)
SENSOR_DATA_TYPE_LOCATION_SOURCE = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=40)
SENSOR_DATA_TYPE_SATELLITES_USED_PRNS_AND_CONSTELLATIONS = PROPERTYKEY(Fmtid='055c74d8-ca6f-47d6-95c6-1ed3637a0ff4', Pid=41)
SENSOR_DATA_TYPE_ENVIRONMENTAL_GUID = '8b0aa2f1-2d57-42ee-8cc0-4d27622b46c4'
SENSOR_DATA_TYPE_TEMPERATURE_CELSIUS = PROPERTYKEY(Fmtid='8b0aa2f1-2d57-42ee-8cc0-4d27622b46c4', Pid=2)
SENSOR_DATA_TYPE_RELATIVE_HUMIDITY_PERCENT = PROPERTYKEY(Fmtid='8b0aa2f1-2d57-42ee-8cc0-4d27622b46c4', Pid=3)
SENSOR_DATA_TYPE_ATMOSPHERIC_PRESSURE_BAR = PROPERTYKEY(Fmtid='8b0aa2f1-2d57-42ee-8cc0-4d27622b46c4', Pid=4)
SENSOR_DATA_TYPE_WIND_DIRECTION_DEGREES_ANTICLOCKWISE = PROPERTYKEY(Fmtid='8b0aa2f1-2d57-42ee-8cc0-4d27622b46c4', Pid=5)
SENSOR_DATA_TYPE_WIND_SPEED_METERS_PER_SECOND = PROPERTYKEY(Fmtid='8b0aa2f1-2d57-42ee-8cc0-4d27622b46c4', Pid=6)
SENSOR_DATA_TYPE_MOTION_GUID = '3f8a69a2-07c5-4e48-a965-cd797aab56d5'
SENSOR_DATA_TYPE_ACCELERATION_X_G = PROPERTYKEY(Fmtid='3f8a69a2-07c5-4e48-a965-cd797aab56d5', Pid=2)
SENSOR_DATA_TYPE_ACCELERATION_Y_G = PROPERTYKEY(Fmtid='3f8a69a2-07c5-4e48-a965-cd797aab56d5', Pid=3)
SENSOR_DATA_TYPE_ACCELERATION_Z_G = PROPERTYKEY(Fmtid='3f8a69a2-07c5-4e48-a965-cd797aab56d5', Pid=4)
SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_X_DEGREES_PER_SECOND_SQUARED = PROPERTYKEY(Fmtid='3f8a69a2-07c5-4e48-a965-cd797aab56d5', Pid=5)
SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_Y_DEGREES_PER_SECOND_SQUARED = PROPERTYKEY(Fmtid='3f8a69a2-07c5-4e48-a965-cd797aab56d5', Pid=6)
SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_Z_DEGREES_PER_SECOND_SQUARED = PROPERTYKEY(Fmtid='3f8a69a2-07c5-4e48-a965-cd797aab56d5', Pid=7)
SENSOR_DATA_TYPE_SPEED_METERS_PER_SECOND = PROPERTYKEY(Fmtid='3f8a69a2-07c5-4e48-a965-cd797aab56d5', Pid=8)
SENSOR_DATA_TYPE_MOTION_STATE = PROPERTYKEY(Fmtid='3f8a69a2-07c5-4e48-a965-cd797aab56d5', Pid=9)
SENSOR_DATA_TYPE_ANGULAR_VELOCITY_X_DEGREES_PER_SECOND = PROPERTYKEY(Fmtid='3f8a69a2-07c5-4e48-a965-cd797aab56d5', Pid=10)
SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Y_DEGREES_PER_SECOND = PROPERTYKEY(Fmtid='3f8a69a2-07c5-4e48-a965-cd797aab56d5', Pid=11)
SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Z_DEGREES_PER_SECOND = PROPERTYKEY(Fmtid='3f8a69a2-07c5-4e48-a965-cd797aab56d5', Pid=12)
SENSOR_DATA_TYPE_ORIENTATION_GUID = '1637d8a2-4248-4275-865d-558de84aedfd'
SENSOR_DATA_TYPE_TILT_X_DEGREES = PROPERTYKEY(Fmtid='1637d8a2-4248-4275-865d-558de84aedfd', Pid=2)
SENSOR_DATA_TYPE_TILT_Y_DEGREES = PROPERTYKEY(Fmtid='1637d8a2-4248-4275-865d-558de84aedfd', Pid=3)
SENSOR_DATA_TYPE_TILT_Z_DEGREES = PROPERTYKEY(Fmtid='1637d8a2-4248-4275-865d-558de84aedfd', Pid=4)
SENSOR_DATA_TYPE_MAGNETIC_HEADING_X_DEGREES = PROPERTYKEY(Fmtid='1637d8a2-4248-4275-865d-558de84aedfd', Pid=5)
SENSOR_DATA_TYPE_MAGNETIC_HEADING_Y_DEGREES = PROPERTYKEY(Fmtid='1637d8a2-4248-4275-865d-558de84aedfd', Pid=6)
SENSOR_DATA_TYPE_MAGNETIC_HEADING_Z_DEGREES = PROPERTYKEY(Fmtid='1637d8a2-4248-4275-865d-558de84aedfd', Pid=7)
SENSOR_DATA_TYPE_DISTANCE_X_METERS = PROPERTYKEY(Fmtid='1637d8a2-4248-4275-865d-558de84aedfd', Pid=8)
SENSOR_DATA_TYPE_DISTANCE_Y_METERS = PROPERTYKEY(Fmtid='1637d8a2-4248-4275-865d-558de84aedfd', Pid=9)
SENSOR_DATA_TYPE_DISTANCE_Z_METERS = PROPERTYKEY(Fmtid='1637d8a2-4248-4275-865d-558de84aedfd', Pid=10)
SENSOR_DATA_TYPE_MAGNETIC_HEADING_COMPENSATED_MAGNETIC_NORTH_DEGREES = PROPERTYKEY(Fmtid='1637d8a2-4248-4275-865d-558de84aedfd', Pid=11)
SENSOR_DATA_TYPE_MAGNETIC_HEADING_COMPENSATED_TRUE_NORTH_DEGREES = PROPERTYKEY(Fmtid='1637d8a2-4248-4275-865d-558de84aedfd', Pid=12)
SENSOR_DATA_TYPE_MAGNETIC_HEADING_MAGNETIC_NORTH_DEGREES = PROPERTYKEY(Fmtid='1637d8a2-4248-4275-865d-558de84aedfd', Pid=13)
SENSOR_DATA_TYPE_MAGNETIC_HEADING_TRUE_NORTH_DEGREES = PROPERTYKEY(Fmtid='1637d8a2-4248-4275-865d-558de84aedfd', Pid=14)
SENSOR_DATA_TYPE_QUADRANT_ANGLE_DEGREES = PROPERTYKEY(Fmtid='1637d8a2-4248-4275-865d-558de84aedfd', Pid=15)
SENSOR_DATA_TYPE_ROTATION_MATRIX = PROPERTYKEY(Fmtid='1637d8a2-4248-4275-865d-558de84aedfd', Pid=16)
SENSOR_DATA_TYPE_QUATERNION = PROPERTYKEY(Fmtid='1637d8a2-4248-4275-865d-558de84aedfd', Pid=17)
SENSOR_DATA_TYPE_SIMPLE_DEVICE_ORIENTATION = PROPERTYKEY(Fmtid='1637d8a2-4248-4275-865d-558de84aedfd', Pid=18)
SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_X_MILLIGAUSS = PROPERTYKEY(Fmtid='1637d8a2-4248-4275-865d-558de84aedfd', Pid=19)
SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_Y_MILLIGAUSS = PROPERTYKEY(Fmtid='1637d8a2-4248-4275-865d-558de84aedfd', Pid=20)
SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_Z_MILLIGAUSS = PROPERTYKEY(Fmtid='1637d8a2-4248-4275-865d-558de84aedfd', Pid=21)
SENSOR_DATA_TYPE_MAGNETOMETER_ACCURACY = PROPERTYKEY(Fmtid='1637d8a2-4248-4275-865d-558de84aedfd', Pid=22)
SENSOR_DATA_TYPE_GUID_MECHANICAL_GUID = '38564a7c-f2f2-49bb-9b2b-ba60f66a58df'
SENSOR_DATA_TYPE_BOOLEAN_SWITCH_STATE = PROPERTYKEY(Fmtid='38564a7c-f2f2-49bb-9b2b-ba60f66a58df', Pid=2)
SENSOR_DATA_TYPE_MULTIVALUE_SWITCH_STATE = PROPERTYKEY(Fmtid='38564a7c-f2f2-49bb-9b2b-ba60f66a58df', Pid=3)
SENSOR_DATA_TYPE_FORCE_NEWTONS = PROPERTYKEY(Fmtid='38564a7c-f2f2-49bb-9b2b-ba60f66a58df', Pid=4)
SENSOR_DATA_TYPE_ABSOLUTE_PRESSURE_PASCAL = PROPERTYKEY(Fmtid='38564a7c-f2f2-49bb-9b2b-ba60f66a58df', Pid=5)
SENSOR_DATA_TYPE_GAUGE_PRESSURE_PASCAL = PROPERTYKEY(Fmtid='38564a7c-f2f2-49bb-9b2b-ba60f66a58df', Pid=6)
SENSOR_DATA_TYPE_STRAIN = PROPERTYKEY(Fmtid='38564a7c-f2f2-49bb-9b2b-ba60f66a58df', Pid=7)
SENSOR_DATA_TYPE_WEIGHT_KILOGRAMS = PROPERTYKEY(Fmtid='38564a7c-f2f2-49bb-9b2b-ba60f66a58df', Pid=8)
SENSOR_DATA_TYPE_BOOLEAN_SWITCH_ARRAY_STATES = PROPERTYKEY(Fmtid='38564a7c-f2f2-49bb-9b2b-ba60f66a58df', Pid=10)
SENSOR_DATA_TYPE_BIOMETRIC_GUID = '2299288a-6d9e-4b0b-b7ec-3528f89e40af'
SENSOR_DATA_TYPE_HUMAN_PRESENCE = PROPERTYKEY(Fmtid='2299288a-6d9e-4b0b-b7ec-3528f89e40af', Pid=2)
SENSOR_DATA_TYPE_HUMAN_PROXIMITY_METERS = PROPERTYKEY(Fmtid='2299288a-6d9e-4b0b-b7ec-3528f89e40af', Pid=3)
SENSOR_DATA_TYPE_TOUCH_STATE = PROPERTYKEY(Fmtid='2299288a-6d9e-4b0b-b7ec-3528f89e40af', Pid=4)
SENSOR_DATA_TYPE_LIGHT_GUID = 'e4c77ce2-dcb7-46e9-8439-4fec548833a6'
SENSOR_DATA_TYPE_LIGHT_LEVEL_LUX = PROPERTYKEY(Fmtid='e4c77ce2-dcb7-46e9-8439-4fec548833a6', Pid=2)
SENSOR_DATA_TYPE_LIGHT_TEMPERATURE_KELVIN = PROPERTYKEY(Fmtid='e4c77ce2-dcb7-46e9-8439-4fec548833a6', Pid=3)
SENSOR_DATA_TYPE_LIGHT_CHROMACITY = PROPERTYKEY(Fmtid='e4c77ce2-dcb7-46e9-8439-4fec548833a6', Pid=4)
SENSOR_DATA_TYPE_SCANNER_GUID = 'd7a59a3c-3421-44ab-8d3a-9de8ab6c4cae'
SENSOR_DATA_TYPE_RFID_TAG_40_BIT = PROPERTYKEY(Fmtid='d7a59a3c-3421-44ab-8d3a-9de8ab6c4cae', Pid=2)
SENSOR_DATA_TYPE_ELECTRICAL_GUID = 'bbb246d1-e242-4780-a2d3-cded84f35842'
SENSOR_DATA_TYPE_VOLTAGE_VOLTS = PROPERTYKEY(Fmtid='bbb246d1-e242-4780-a2d3-cded84f35842', Pid=2)
SENSOR_DATA_TYPE_CURRENT_AMPS = PROPERTYKEY(Fmtid='bbb246d1-e242-4780-a2d3-cded84f35842', Pid=3)
SENSOR_DATA_TYPE_CAPACITANCE_FARAD = PROPERTYKEY(Fmtid='bbb246d1-e242-4780-a2d3-cded84f35842', Pid=4)
SENSOR_DATA_TYPE_RESISTANCE_OHMS = PROPERTYKEY(Fmtid='bbb246d1-e242-4780-a2d3-cded84f35842', Pid=5)
SENSOR_DATA_TYPE_INDUCTANCE_HENRY = PROPERTYKEY(Fmtid='bbb246d1-e242-4780-a2d3-cded84f35842', Pid=6)
SENSOR_DATA_TYPE_ELECTRICAL_POWER_WATTS = PROPERTYKEY(Fmtid='bbb246d1-e242-4780-a2d3-cded84f35842', Pid=7)
SENSOR_DATA_TYPE_ELECTRICAL_PERCENT_OF_RANGE = PROPERTYKEY(Fmtid='bbb246d1-e242-4780-a2d3-cded84f35842', Pid=8)
SENSOR_DATA_TYPE_ELECTRICAL_FREQUENCY_HERTZ = PROPERTYKEY(Fmtid='bbb246d1-e242-4780-a2d3-cded84f35842', Pid=9)
SENSOR_DATA_TYPE_CUSTOM_GUID = 'b14c764f-07cf-41e8-9d82-ebe3d0776a6f'
SENSOR_DATA_TYPE_CUSTOM_USAGE = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=5)
SENSOR_DATA_TYPE_CUSTOM_BOOLEAN_ARRAY = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=6)
SENSOR_DATA_TYPE_CUSTOM_VALUE1 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=7)
SENSOR_DATA_TYPE_CUSTOM_VALUE2 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=8)
SENSOR_DATA_TYPE_CUSTOM_VALUE3 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=9)
SENSOR_DATA_TYPE_CUSTOM_VALUE4 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=10)
SENSOR_DATA_TYPE_CUSTOM_VALUE5 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=11)
SENSOR_DATA_TYPE_CUSTOM_VALUE6 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=12)
SENSOR_DATA_TYPE_CUSTOM_VALUE7 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=13)
SENSOR_DATA_TYPE_CUSTOM_VALUE8 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=14)
SENSOR_DATA_TYPE_CUSTOM_VALUE9 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=15)
SENSOR_DATA_TYPE_CUSTOM_VALUE10 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=16)
SENSOR_DATA_TYPE_CUSTOM_VALUE11 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=17)
SENSOR_DATA_TYPE_CUSTOM_VALUE12 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=18)
SENSOR_DATA_TYPE_CUSTOM_VALUE13 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=19)
SENSOR_DATA_TYPE_CUSTOM_VALUE14 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=20)
SENSOR_DATA_TYPE_CUSTOM_VALUE15 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=21)
SENSOR_DATA_TYPE_CUSTOM_VALUE16 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=22)
SENSOR_DATA_TYPE_CUSTOM_VALUE17 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=23)
SENSOR_DATA_TYPE_CUSTOM_VALUE18 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=24)
SENSOR_DATA_TYPE_CUSTOM_VALUE19 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=25)
SENSOR_DATA_TYPE_CUSTOM_VALUE20 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=26)
SENSOR_DATA_TYPE_CUSTOM_VALUE21 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=27)
SENSOR_DATA_TYPE_CUSTOM_VALUE22 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=28)
SENSOR_DATA_TYPE_CUSTOM_VALUE23 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=29)
SENSOR_DATA_TYPE_CUSTOM_VALUE24 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=30)
SENSOR_DATA_TYPE_CUSTOM_VALUE25 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=31)
SENSOR_DATA_TYPE_CUSTOM_VALUE26 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=32)
SENSOR_DATA_TYPE_CUSTOM_VALUE27 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=33)
SENSOR_DATA_TYPE_CUSTOM_VALUE28 = PROPERTYKEY(Fmtid='b14c764f-07cf-41e8-9d82-ebe3d0776a6f', Pid=34)
SENSOR_PROPERTY_TEST_GUID = 'e1e962f4-6e65-45f7-9c36-d487b7b1bd34'
SENSOR_PROPERTY_CLEAR_ASSISTANCE_DATA = PROPERTYKEY(Fmtid='e1e962f4-6e65-45f7-9c36-d487b7b1bd34', Pid=2)
SENSOR_PROPERTY_TURN_ON_OFF_NMEA = PROPERTYKEY(Fmtid='e1e962f4-6e65-45f7-9c36-d487b7b1bd34', Pid=3)
GNSS_CLEAR_ALL_ASSISTANCE_DATA = 1
GUID_SensorCategory_All = 'c317c286-c468-4288-9975-d4c4587c442c'
GUID_SensorCategory_Biometric = 'ca19690f-a2c7-477d-a99e-99ec6e2b5648'
GUID_SensorCategory_Electrical = 'fb73fcd8-fc4a-483c-ac58-27b691c6beff'
GUID_SensorCategory_Environmental = '323439aa-7f66-492b-ba0c-73e9aa0a65d5'
GUID_SensorCategory_Light = '17a665c0-9063-4216-b202-5c7a255e18ce'
GUID_SensorCategory_Location = 'bfa794e4-f964-4fdb-90f6-51056bfe4b44'
GUID_SensorCategory_Mechanical = '8d131d68-8ef7-4656-80b5-cccbd93791c5'
GUID_SensorCategory_Motion = 'cd09daf1-3b2e-4c3d-b598-b5e5ff93fd46'
GUID_SensorCategory_Orientation = '9e6c04b6-96fe-4954-b726-68682a473f69'
GUID_SensorCategory_Other = '2c90e7a9-f4c9-4fa2-af37-56d471fe5a3d'
GUID_SensorCategory_PersonalActivity = 'f1609081-1e12-412b-a14d-cbb0e95bd2e5'
GUID_SensorCategory_Scanner = 'b000e77e-f5b5-420f-815d-0270a726f270'
GUID_SensorCategory_Unsupported = '2beae7fa-19b0-48c5-a1f6-b5480dc206b0'
GUID_SensorType_Accelerometer3D = 'c2fb0f5f-e2d2-4c78-bcd0-352a9582819d'
GUID_SensorType_ActivityDetection = '9d9e0118-1807-4f2e-96e4-2ce57142e196'
GUID_SensorType_AmbientLight = '97f115c8-599a-4153-8894-d2d12899918a'
GUID_SensorType_Barometer = '0e903829-ff8a-4a93-97df-3dcbde402288'
GUID_SensorType_Custom = 'e83af229-8640-4d18-a213-e22675ebb2c3'
GUID_SensorType_FloorElevation = 'ade4987f-7ac4-4dfa-9722-0a027181c747'
GUID_SensorType_GeomagneticOrientation = 'e77195f8-2d1f-4823-971b-1c4467556c9d'
GUID_SensorType_GravityVector = '03b52c73-bb76-463f-9524-38de76eb700b'
GUID_SensorType_Gyrometer3D = '09485f5a-759e-42c2-bd4b-a349b75c8643'
GUID_SensorType_Humidity = '5c72bf67-bd7e-4257-990b-98a3ba3b400a'
GUID_SensorType_LinearAccelerometer = '038b0283-97b4-41c8-bc24-5ff1aa48fec7'
GUID_SensorType_Magnetometer3D = '55e5effb-15c7-40df-8698-a84b7c863c53'
GUID_SensorType_Orientation = 'cdb5d8f7-3cfd-41c8-8542-cce622cf5d6e'
GUID_SensorType_Pedometer = 'b19f89af-e3eb-444b-8dea-202575a71599'
GUID_SensorType_Proximity = '5220dae9-3179-4430-9f90-06266d2a34de'
GUID_SensorType_RelativeOrientation = '40993b51-4706-44dc-98d5-c920c037ffab'
GUID_SensorType_SimpleDeviceOrientation = '86a19291-0482-402c-bf4c-addac52b1c39'
GUID_SensorType_Temperature = '04fd0ec4-d5da-45fa-95a9-5db38ee19306'
GUID_SensorType_HingeAngle = '82358065-f4c4-4da1-b272-13c23332a207'
SENSOR_PROPERTY_LIST_HEADER_SIZE = 8
SensorManager = Guid('77a1c827-fcd2-4689-8915-9d613cc5fa3e')
SensorCollection = Guid('79c43adb-a429-469f-aa39-2f2b74b75937')
Sensor = Guid('e97ced00-523a-4133-bf6f-d3a2dae7f6ba')
SensorDataReport = Guid('4ea9d6ef-694b-4218-8816-ccda8da74bba')
SensorState = Int32
SENSOR_STATE_MIN = 0
SENSOR_STATE_READY = 0
SENSOR_STATE_NOT_AVAILABLE = 1
SENSOR_STATE_NO_DATA = 2
SENSOR_STATE_INITIALIZING = 3
SENSOR_STATE_ACCESS_DENIED = 4
SENSOR_STATE_ERROR = 5
SENSOR_STATE_MAX = 5
SensorConnectionType = Int32
SENSOR_CONNECTION_TYPE_PC_INTEGRATED = 0
SENSOR_CONNECTION_TYPE_PC_ATTACHED = 1
SENSOR_CONNECTION_TYPE_PC_EXTERNAL = 2
LOCATION_DESIRED_ACCURACY = Int32
LOCATION_DESIRED_ACCURACY_DEFAULT = 0
LOCATION_DESIRED_ACCURACY_HIGH = 1
LOCATION_POSITION_SOURCE = Int32
LOCATION_POSITION_SOURCE_CELLULAR = 0
LOCATION_POSITION_SOURCE_SATELLITE = 1
LOCATION_POSITION_SOURCE_WIFI = 2
LOCATION_POSITION_SOURCE_IPADDRESS = 3
LOCATION_POSITION_SOURCE_UNKNOWN = 4
SimpleDeviceOrientation = Int32
SIMPLE_DEVICE_ORIENTATION_NOT_ROTATED = 0
SIMPLE_DEVICE_ORIENTATION_ROTATED_90 = 1
SIMPLE_DEVICE_ORIENTATION_ROTATED_180 = 2
SIMPLE_DEVICE_ORIENTATION_ROTATED_270 = 3
SIMPLE_DEVICE_ORIENTATION_ROTATED_FACE_UP = 4
SIMPLE_DEVICE_ORIENTATION_ROTATED_FACE_DOWN = 5
MagnetometerAccuracy = Int32
MAGNETOMETER_ACCURACY_UNKNOWN = 0
MAGNETOMETER_ACCURACY_UNRELIABLE = 1
MAGNETOMETER_ACCURACY_APPROXIMATE = 2
MAGNETOMETER_ACCURACY_HIGH = 3
def _define_ISensorManager_head():
    class ISensorManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('bd77db67-45a8-42dc-8d00-6dcf15f8377a')
    return ISensorManager
def _define_ISensorManager():
    ISensorManager = win32more.Devices.Sensors.ISensorManager_head
    ISensorManager.GetSensorsByCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.Sensors.ISensorCollection_head), use_last_error=False)(3, 'GetSensorsByCategory', ((1, 'sensorCategory'),(1, 'ppSensorsFound'),)))
    ISensorManager.GetSensorsByType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.Sensors.ISensorCollection_head), use_last_error=False)(4, 'GetSensorsByType', ((1, 'sensorType'),(1, 'ppSensorsFound'),)))
    ISensorManager.GetSensorByID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.Sensors.ISensor_head), use_last_error=False)(5, 'GetSensorByID', ((1, 'sensorID'),(1, 'ppSensor'),)))
    ISensorManager.SetEventSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Sensors.ISensorManagerEvents_head, use_last_error=False)(6, 'SetEventSink', ((1, 'pEvents'),)))
    ISensorManager.RequestPermissions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Devices.Sensors.ISensorCollection_head,win32more.Foundation.BOOL, use_last_error=False)(7, 'RequestPermissions', ((1, 'hParent'),(1, 'pSensors'),(1, 'fModal'),)))
    return ISensorManager
def _define_ILocationPermissions_head():
    class ILocationPermissions(win32more.System.Com.IUnknown_head):
        Guid = Guid('d5fb0a7f-e74e-44f5-8e02-4806863a274f')
    return ILocationPermissions
def _define_ILocationPermissions():
    ILocationPermissions = win32more.Devices.Sensors.ILocationPermissions_head
    ILocationPermissions.GetGlobalLocationPermission = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'GetGlobalLocationPermission', ((1, 'pfEnabled'),)))
    ILocationPermissions.CheckLocationCapability = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'CheckLocationCapability', ((1, 'dwClientThreadId'),)))
    return ILocationPermissions
def _define_ISensorCollection_head():
    class ISensorCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('23571e11-e545-4dd8-a337-b89bf44b10df')
    return ISensorCollection
def _define_ISensorCollection():
    ISensorCollection = win32more.Devices.Sensors.ISensorCollection_head
    ISensorCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Devices.Sensors.ISensor_head), use_last_error=False)(3, 'GetAt', ((1, 'ulIndex'),(1, 'ppSensor'),)))
    ISensorCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetCount', ((1, 'pCount'),)))
    ISensorCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Sensors.ISensor_head, use_last_error=False)(5, 'Add', ((1, 'pSensor'),)))
    ISensorCollection.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Sensors.ISensor_head, use_last_error=False)(6, 'Remove', ((1, 'pSensor'),)))
    ISensorCollection.RemoveByID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(7, 'RemoveByID', ((1, 'sensorID'),)))
    ISensorCollection.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Clear', ()))
    return ISensorCollection
def _define_ISensor_head():
    class ISensor(win32more.System.Com.IUnknown_head):
        Guid = Guid('5fa08f80-2657-458e-af75-46f73fa6ac5c')
    return ISensor
def _define_ISensor():
    ISensor = win32more.Devices.Sensors.ISensor_head
    ISensor.GetID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(3, 'GetID', ((1, 'pID'),)))
    ISensor.GetCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(4, 'GetCategory', ((1, 'pSensorCategory'),)))
    ISensor.GetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(5, 'GetType', ((1, 'pSensorType'),)))
    ISensor.GetFriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(6, 'GetFriendlyName', ((1, 'pFriendlyName'),)))
    ISensor.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(7, 'GetProperty', ((1, 'key'),(1, 'pProperty'),)))
    ISensor.GetProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head,POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head), use_last_error=False)(8, 'GetProperties', ((1, 'pKeys'),(1, 'ppProperties'),)))
    ISensor.GetSupportedDataFields = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head), use_last_error=False)(9, 'GetSupportedDataFields', ((1, 'ppDataFields'),)))
    ISensor.SetProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDeviceValues_head,POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head), use_last_error=False)(10, 'SetProperties', ((1, 'pProperties'),(1, 'ppResults'),)))
    ISensor.SupportsDataField = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(Int16), use_last_error=False)(11, 'SupportsDataField', ((1, 'key'),(1, 'pIsSupported'),)))
    ISensor.GetState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Sensors.SensorState), use_last_error=False)(12, 'GetState', ((1, 'pState'),)))
    ISensor.GetData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Sensors.ISensorDataReport_head), use_last_error=False)(13, 'GetData', ((1, 'ppDataReport'),)))
    ISensor.SupportsEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Int16), use_last_error=False)(14, 'SupportsEvent', ((1, 'eventGuid'),(1, 'pIsSupported'),)))
    ISensor.GetEventInterest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(Guid)),POINTER(UInt32), use_last_error=False)(15, 'GetEventInterest', ((1, 'ppValues'),(1, 'pCount'),)))
    ISensor.SetEventInterest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32, use_last_error=False)(16, 'SetEventInterest', ((1, 'pValues'),(1, 'count'),)))
    ISensor.SetEventSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Sensors.ISensorEvents_head, use_last_error=False)(17, 'SetEventSink', ((1, 'pEvents'),)))
    return ISensor
def _define_ISensorDataReport_head():
    class ISensorDataReport(win32more.System.Com.IUnknown_head):
        Guid = Guid('0ab9df9b-c4b5-4796-8898-0470706a2e1d')
    return ISensorDataReport
def _define_ISensorDataReport():
    ISensorDataReport = win32more.Devices.Sensors.ISensorDataReport_head
    ISensorDataReport.GetTimestamp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.SYSTEMTIME_head), use_last_error=False)(3, 'GetTimestamp', ((1, 'pTimeStamp'),)))
    ISensorDataReport.GetSensorValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(4, 'GetSensorValue', ((1, 'pKey'),(1, 'pValue'),)))
    ISensorDataReport.GetSensorValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.PortableDevices.IPortableDeviceKeyCollection_head,POINTER(win32more.Devices.PortableDevices.IPortableDeviceValues_head), use_last_error=False)(5, 'GetSensorValues', ((1, 'pKeys'),(1, 'ppValues'),)))
    return ISensorDataReport
def _define_ISensorManagerEvents_head():
    class ISensorManagerEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('9b3b0b86-266a-4aad-b21f-fde5501001b7')
    return ISensorManagerEvents
def _define_ISensorManagerEvents():
    ISensorManagerEvents = win32more.Devices.Sensors.ISensorManagerEvents_head
    ISensorManagerEvents.OnSensorEnter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Sensors.ISensor_head,win32more.Devices.Sensors.SensorState, use_last_error=False)(3, 'OnSensorEnter', ((1, 'pSensor'),(1, 'state'),)))
    return ISensorManagerEvents
def _define_ISensorEvents_head():
    class ISensorEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('5d8dcc91-4641-47e7-b7c3-b74f48a6c391')
    return ISensorEvents
def _define_ISensorEvents():
    ISensorEvents = win32more.Devices.Sensors.ISensorEvents_head
    ISensorEvents.OnStateChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Sensors.ISensor_head,win32more.Devices.Sensors.SensorState, use_last_error=False)(3, 'OnStateChanged', ((1, 'pSensor'),(1, 'state'),)))
    ISensorEvents.OnDataUpdated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Sensors.ISensor_head,win32more.Devices.Sensors.ISensorDataReport_head, use_last_error=False)(4, 'OnDataUpdated', ((1, 'pSensor'),(1, 'pNewData'),)))
    ISensorEvents.OnEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Sensors.ISensor_head,POINTER(Guid),win32more.Devices.PortableDevices.IPortableDeviceValues_head, use_last_error=False)(5, 'OnEvent', ((1, 'pSensor'),(1, 'eventID'),(1, 'pEventData'),)))
    ISensorEvents.OnLeave = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(6, 'OnLeave', ((1, 'ID'),)))
    return ISensorEvents
ACTIVITY_STATE_COUNT = Int32
ACTIVITY_STATE_COUNT_ActivityStateCount = 8
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
ELEVATION_CHANGE_MODE = Int32
ElevationChangeMode_Unknown = 0
ElevationChangeMode_Elevator = 1
ElevationChangeMode_Stepping = 2
ElevationChangeMode_Max = 3
ElevationChangeMode_Force_Dword = -1
MAGNETOMETER_ACCURACY = Int32
MagnetometerAccuracy_Unknown = 0
MagnetometerAccuracy_Unreliable = 1
MagnetometerAccuracy_Approximate = 2
MagnetometerAccuracy_High = 3
PEDOMETER_STEP_TYPE_COUNT = Int32
PEDOMETER_STEP_TYPE_COUNT_PedometerStepTypeCount = 3
PEDOMETER_STEP_TYPE = Int32
PedometerStepType_Unknown = 1
PedometerStepType_Walking = 2
PedometerStepType_Running = 4
PedometerStepType_Max = 8
PedometerStepType_Force_Dword = -1
PROXIMITY_TYPE = Int32
ProximityType_ObjectProximity = 0
ProximityType_HumanProximity = 1
ProximityType_Force_Dword = -1
HUMAN_PRESENCE_DETECTION_TYPE_COUNT = Int32
HUMAN_PRESENCE_DETECTION_TYPE_COUNT_HumanPresenceDetectionTypeCount = 4
HUMAN_PRESENCE_DETECTION_TYPE = Int32
HumanPresenceDetectionType_VendorDefinedNonBiometric = 1
HumanPresenceDetectionType_VendorDefinedBiometric = 2
HumanPresenceDetectionType_FacialBiometric = 4
HumanPresenceDetectionType_AudioBiometric = 8
HumanPresenceDetectionType_Force_Dword = -1
SIMPLE_DEVICE_ORIENTATION = Int32
SimpleDeviceOrientation_NotRotated = 0
SimpleDeviceOrientation_Rotated90DegreesCounterclockwise = 1
SimpleDeviceOrientation_Rotated180DegreesCounterclockwise = 2
SimpleDeviceOrientation_Rotated270DegreesCounterclockwise = 3
SimpleDeviceOrientation_Faceup = 4
SimpleDeviceOrientation_Facedown = 5
SENSOR_STATE = Int32
SensorState_Initializing = 0
SensorState_Idle = 1
SensorState_Active = 2
SensorState_Error = 3
SENSOR_CONNECTION_TYPES = Int32
SensorConnectionType_Integrated = 0
SensorConnectionType_Attached = 1
SensorConnectionType_External = 2
def _define_SENSOR_VALUE_PAIR_head():
    class SENSOR_VALUE_PAIR(Structure):
        pass
    return SENSOR_VALUE_PAIR
def _define_SENSOR_VALUE_PAIR():
    SENSOR_VALUE_PAIR = win32more.Devices.Sensors.SENSOR_VALUE_PAIR_head
    SENSOR_VALUE_PAIR._fields_ = [
        ("Key", win32more.UI.Shell.PropertiesSystem.PROPERTYKEY),
        ("Value", win32more.System.Com.StructuredStorage.PROPVARIANT),
    ]
    return SENSOR_VALUE_PAIR
def _define_SENSOR_COLLECTION_LIST_head():
    class SENSOR_COLLECTION_LIST(Structure):
        pass
    return SENSOR_COLLECTION_LIST
def _define_SENSOR_COLLECTION_LIST():
    SENSOR_COLLECTION_LIST = win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head
    SENSOR_COLLECTION_LIST._fields_ = [
        ("AllocatedSizeInBytes", UInt32),
        ("Count", UInt32),
        ("List", win32more.Devices.Sensors.SENSOR_VALUE_PAIR * 0),
    ]
    return SENSOR_COLLECTION_LIST
def _define_SENSOR_PROPERTY_LIST_head():
    class SENSOR_PROPERTY_LIST(Structure):
        pass
    return SENSOR_PROPERTY_LIST
def _define_SENSOR_PROPERTY_LIST():
    SENSOR_PROPERTY_LIST = win32more.Devices.Sensors.SENSOR_PROPERTY_LIST_head
    SENSOR_PROPERTY_LIST._fields_ = [
        ("AllocatedSizeInBytes", UInt32),
        ("Count", UInt32),
        ("List", win32more.UI.Shell.PropertiesSystem.PROPERTYKEY * 0),
    ]
    return SENSOR_PROPERTY_LIST
def _define_VEC3D_head():
    class VEC3D(Structure):
        pass
    return VEC3D
def _define_VEC3D():
    VEC3D = win32more.Devices.Sensors.VEC3D_head
    VEC3D._fields_ = [
        ("X", Single),
        ("Y", Single),
        ("Z", Single),
    ]
    return VEC3D
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
        ("A11", Single),
        ("A12", Single),
        ("A13", Single),
        ("A21", Single),
        ("A22", Single),
        ("A23", Single),
        ("A31", Single),
        ("A32", Single),
        ("A33", Single),
    ]
    class MATRIX3X3__Anonymous_e__Union__Anonymous2_e__Struct(Structure):
        pass
    MATRIX3X3__Anonymous_e__Union__Anonymous2_e__Struct._fields_ = [
        ("V1", win32more.Devices.Sensors.VEC3D),
        ("V2", win32more.Devices.Sensors.VEC3D),
        ("V3", win32more.Devices.Sensors.VEC3D),
    ]
    MATRIX3X3__Anonymous_e__Union._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    MATRIX3X3__Anonymous_e__Union._fields_ = [
        ("Anonymous1", MATRIX3X3__Anonymous_e__Union__Anonymous1_e__Struct),
        ("Anonymous2", MATRIX3X3__Anonymous_e__Union__Anonymous2_e__Struct),
        ("M", Single * 9),
    ]
    MATRIX3X3._anonymous_ = [
        'Anonymous',
    ]
    MATRIX3X3._fields_ = [
        ("Anonymous", MATRIX3X3__Anonymous_e__Union),
    ]
    return MATRIX3X3
def _define_QUATERNION_head():
    class QUATERNION(Structure):
        pass
    return QUATERNION
def _define_QUATERNION():
    QUATERNION = win32more.Devices.Sensors.QUATERNION_head
    QUATERNION._fields_ = [
        ("X", Single),
        ("Y", Single),
        ("Z", Single),
        ("W", Single),
    ]
    return QUATERNION
AXIS = Int32
AXIS_X = 0
AXIS_Y = 1
AXIS_Z = 2
AXIS_MAX = 3
def _define_GetPerformanceTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(UInt32), use_last_error=False)(("GetPerformanceTime", windll["SensorsUtilsV2"]), ((1, 'TimeMs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromFloat():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Single,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("InitPropVariantFromFloat", windll["SensorsUtilsV2"]), ((1, 'fltVal'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeyGetPropVariant():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),win32more.Foundation.BOOLEAN,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("PropKeyFindKeyGetPropVariant", windll["SensorsUtilsV2"]), ((1, 'pList'),(1, 'pKey'),(1, 'TypeCheck'),(1, 'pValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeySetPropVariant():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),win32more.Foundation.BOOLEAN,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("PropKeyFindKeySetPropVariant", windll["SensorsUtilsV2"]), ((1, 'pList'),(1, 'pKey'),(1, 'TypeCheck'),(1, 'pValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeyGetFileTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(("PropKeyFindKeyGetFileTime", windll["SensorsUtilsV2"]), ((1, 'pList'),(1, 'pKey'),(1, 'pRetValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeyGetGuid():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(Guid), use_last_error=False)(("PropKeyFindKeyGetGuid", windll["SensorsUtilsV2"]), ((1, 'pList'),(1, 'pKey'),(1, 'pRetValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeyGetBool():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(("PropKeyFindKeyGetBool", windll["SensorsUtilsV2"]), ((1, 'pList'),(1, 'pKey'),(1, 'pRetValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeyGetUlong():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(UInt32), use_last_error=False)(("PropKeyFindKeyGetUlong", windll["SensorsUtilsV2"]), ((1, 'pList'),(1, 'pKey'),(1, 'pRetValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeyGetUshort():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(UInt16), use_last_error=False)(("PropKeyFindKeyGetUshort", windll["SensorsUtilsV2"]), ((1, 'pList'),(1, 'pKey'),(1, 'pRetValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeyGetFloat():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(Single), use_last_error=False)(("PropKeyFindKeyGetFloat", windll["SensorsUtilsV2"]), ((1, 'pList'),(1, 'pKey'),(1, 'pRetValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeyGetDouble():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(Double), use_last_error=False)(("PropKeyFindKeyGetDouble", windll["SensorsUtilsV2"]), ((1, 'pList'),(1, 'pKey'),(1, 'pRetValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeyGetInt32():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(Int32), use_last_error=False)(("PropKeyFindKeyGetInt32", windll["SensorsUtilsV2"]), ((1, 'pList'),(1, 'pKey'),(1, 'pRetValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeyGetInt64():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(Int64), use_last_error=False)(("PropKeyFindKeyGetInt64", windll["SensorsUtilsV2"]), ((1, 'pList'),(1, 'pKey'),(1, 'pRetValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeyGetNthUlong():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),UInt32,POINTER(UInt32), use_last_error=False)(("PropKeyFindKeyGetNthUlong", windll["SensorsUtilsV2"]), ((1, 'pList'),(1, 'pKey'),(1, 'Occurrence'),(1, 'pRetValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeyGetNthUshort():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),UInt32,POINTER(UInt16), use_last_error=False)(("PropKeyFindKeyGetNthUshort", windll["SensorsUtilsV2"]), ((1, 'pList'),(1, 'pKey'),(1, 'Occurrence'),(1, 'pRetValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropKeyFindKeyGetNthInt64():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),UInt32,POINTER(Int64), use_last_error=False)(("PropKeyFindKeyGetNthInt64", windll["SensorsUtilsV2"]), ((1, 'pList'),(1, 'pKey'),(1, 'Occurrence'),(1, 'pRetValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsKeyPresentInPropertyList():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.Devices.Sensors.SENSOR_PROPERTY_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), use_last_error=False)(("IsKeyPresentInPropertyList", windll["SensorsUtilsV2"]), ((1, 'pList'),(1, 'pKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsKeyPresentInCollectionList():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), use_last_error=False)(("IsKeyPresentInCollectionList", windll["SensorsUtilsV2"]), ((1, 'pList'),(1, 'pKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsCollectionListSame():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), use_last_error=False)(("IsCollectionListSame", windll["SensorsUtilsV2"]), ((1, 'ListA'),(1, 'ListB'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropVariantGetInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(UInt32),POINTER(UInt32),POINTER(c_void_p),POINTER(UInt32), use_last_error=False)(("PropVariantGetInformation", windll["SensorsUtilsV2"]), ((1, 'PropVariantValue'),(1, 'PropVariantOffset'),(1, 'PropVariantSize'),(1, 'PropVariantPointer'),(1, 'RemappedType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropertiesListCopy():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_PROPERTY_LIST_head),POINTER(win32more.Devices.Sensors.SENSOR_PROPERTY_LIST_head), use_last_error=False)(("PropertiesListCopy", windll["SensorsUtilsV2"]), ((1, 'Target'),(1, 'Source'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PropertiesListGetFillableCount():
    try:
        return WINFUNCTYPE(UInt32,UInt32, use_last_error=False)(("PropertiesListGetFillableCount", windll["SensorsUtilsV2"]), ((1, 'BufferSizeBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CollectionsListGetMarshalledSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), use_last_error=False)(("CollectionsListGetMarshalledSize", windll["SensorsUtilsV2"]), ((1, 'Collection'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CollectionsListCopyAndMarshall():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), use_last_error=False)(("CollectionsListCopyAndMarshall", windll["SensorsUtilsV2"]), ((1, 'Target'),(1, 'Source'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CollectionsListMarshall():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), use_last_error=False)(("CollectionsListMarshall", windll["SensorsUtilsV2"]), ((1, 'Target'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CollectionsListGetMarshalledSizeWithoutSerialization():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), use_last_error=False)(("CollectionsListGetMarshalledSizeWithoutSerialization", windll["SensorsUtilsV2"]), ((1, 'Collection'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CollectionsListUpdateMarshalledPointer():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), use_last_error=False)(("CollectionsListUpdateMarshalledPointer", windll["SensorsUtilsV2"]), ((1, 'Collection'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SerializationBufferAllocate():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt32,POINTER(c_char_p_no), use_last_error=False)(("SerializationBufferAllocate", windll["SensorsUtilsV2"]), ((1, 'SizeInBytes'),(1, 'pBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SerializationBufferFree():
    try:
        return WINFUNCTYPE(Void,c_char_p_no, use_last_error=False)(("SerializationBufferFree", windll["SensorsUtilsV2"]), ((1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CollectionsListGetSerializedSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), use_last_error=False)(("CollectionsListGetSerializedSize", windll["SensorsUtilsV2"]), ((1, 'Collection'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CollectionsListSerializeToBuffer():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),UInt32,c_char_p_no, use_last_error=False)(("CollectionsListSerializeToBuffer", windll["SensorsUtilsV2"]), ((1, 'SourceCollection'),(1, 'TargetBufferSizeInBytes'),(1, 'TargetBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CollectionsListAllocateBufferAndSerialize():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(UInt32),POINTER(c_char_p_no), use_last_error=False)(("CollectionsListAllocateBufferAndSerialize", windll["SensorsUtilsV2"]), ((1, 'SourceCollection'),(1, 'pTargetBufferSizeInBytes'),(1, 'pTargetBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CollectionsListDeserializeFromBuffer():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt32,c_char_p_no,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), use_last_error=False)(("CollectionsListDeserializeFromBuffer", windll["SensorsUtilsV2"]), ((1, 'SourceBufferSizeInBytes'),(1, 'SourceBuffer'),(1, 'TargetCollection'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SensorCollectionGetAt():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,UInt32,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("SensorCollectionGetAt", windll["SensorsUtilsV2"]), ((1, 'Index'),(1, 'pSensorsList'),(1, 'pKey'),(1, 'pValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CollectionsListGetFillableCount():
    try:
        return WINFUNCTYPE(UInt32,UInt32, use_last_error=False)(("CollectionsListGetFillableCount", windll["SensorsUtilsV2"]), ((1, 'BufferSizeBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EvaluateActivityThresholds():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), use_last_error=False)(("EvaluateActivityThresholds", windll["SensorsUtilsV2"]), ((1, 'newSample'),(1, 'oldSample'),(1, 'thresholds'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CollectionsListSortSubscribedActivitiesByConfidence():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head), use_last_error=False)(("CollectionsListSortSubscribedActivitiesByConfidence", windll["SensorsUtilsV2"]), ((1, 'thresholds'),(1, 'pCollection'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitPropVariantFromCLSIDArray():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(("InitPropVariantFromCLSIDArray", windll["SensorsUtilsV2"]), ((1, 'members'),(1, 'size'),(1, 'ppropvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsSensorSubscribed():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.Devices.Sensors.SENSOR_COLLECTION_LIST_head),Guid, use_last_error=False)(("IsSensorSubscribed", windll["SensorsUtilsV2"]), ((1, 'subscriptionList'),(1, 'currentType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsGUIDPresentInList():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(Guid),UInt32,POINTER(Guid), use_last_error=False)(("IsGUIDPresentInList", windll["SensorsUtilsV2"]), ((1, 'guidArray'),(1, 'arrayLength'),(1, 'guidElem'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "GUID_DEVINTERFACE_SENSOR",
    "SENSOR_EVENT_STATE_CHANGED",
    "SENSOR_EVENT_DATA_UPDATED",
    "SENSOR_EVENT_PROPERTY_CHANGED",
    "SENSOR_EVENT_ACCELEROMETER_SHAKE",
    "SENSOR_EVENT_PARAMETER_COMMON_GUID",
    "SENSOR_EVENT_PARAMETER_EVENT_ID",
    "SENSOR_EVENT_PARAMETER_STATE",
    "SENSOR_ERROR_PARAMETER_COMMON_GUID",
    "SENSOR_PROPERTY_COMMON_GUID",
    "SENSOR_PROPERTY_TYPE",
    "SENSOR_PROPERTY_STATE",
    "SENSOR_PROPERTY_PERSISTENT_UNIQUE_ID",
    "SENSOR_PROPERTY_MANUFACTURER",
    "SENSOR_PROPERTY_MODEL",
    "SENSOR_PROPERTY_SERIAL_NUMBER",
    "SENSOR_PROPERTY_FRIENDLY_NAME",
    "SENSOR_PROPERTY_DESCRIPTION",
    "SENSOR_PROPERTY_CONNECTION_TYPE",
    "SENSOR_PROPERTY_MIN_REPORT_INTERVAL",
    "SENSOR_PROPERTY_CURRENT_REPORT_INTERVAL",
    "SENSOR_PROPERTY_CHANGE_SENSITIVITY",
    "SENSOR_PROPERTY_DEVICE_PATH",
    "SENSOR_PROPERTY_LIGHT_RESPONSE_CURVE",
    "SENSOR_PROPERTY_ACCURACY",
    "SENSOR_PROPERTY_RESOLUTION",
    "SENSOR_PROPERTY_LOCATION_DESIRED_ACCURACY",
    "SENSOR_PROPERTY_RANGE_MINIMUM",
    "SENSOR_PROPERTY_RANGE_MAXIMUM",
    "SENSOR_PROPERTY_HID_USAGE",
    "SENSOR_PROPERTY_RADIO_STATE",
    "SENSOR_PROPERTY_RADIO_STATE_PREVIOUS",
    "SENSOR_CATEGORY_ALL",
    "SENSOR_CATEGORY_LOCATION",
    "SENSOR_CATEGORY_ENVIRONMENTAL",
    "SENSOR_CATEGORY_MOTION",
    "SENSOR_CATEGORY_ORIENTATION",
    "SENSOR_CATEGORY_MECHANICAL",
    "SENSOR_CATEGORY_ELECTRICAL",
    "SENSOR_CATEGORY_BIOMETRIC",
    "SENSOR_CATEGORY_LIGHT",
    "SENSOR_CATEGORY_SCANNER",
    "SENSOR_CATEGORY_OTHER",
    "SENSOR_CATEGORY_UNSUPPORTED",
    "SENSOR_TYPE_LOCATION_GPS",
    "SENSOR_TYPE_LOCATION_STATIC",
    "SENSOR_TYPE_LOCATION_LOOKUP",
    "SENSOR_TYPE_LOCATION_TRIANGULATION",
    "SENSOR_TYPE_LOCATION_OTHER",
    "SENSOR_TYPE_LOCATION_BROADCAST",
    "SENSOR_TYPE_LOCATION_DEAD_RECKONING",
    "SENSOR_TYPE_ENVIRONMENTAL_TEMPERATURE",
    "SENSOR_TYPE_ENVIRONMENTAL_ATMOSPHERIC_PRESSURE",
    "SENSOR_TYPE_ENVIRONMENTAL_HUMIDITY",
    "SENSOR_TYPE_ENVIRONMENTAL_WIND_SPEED",
    "SENSOR_TYPE_ENVIRONMENTAL_WIND_DIRECTION",
    "SENSOR_TYPE_ACCELEROMETER_1D",
    "SENSOR_TYPE_ACCELEROMETER_2D",
    "SENSOR_TYPE_ACCELEROMETER_3D",
    "SENSOR_TYPE_MOTION_DETECTOR",
    "SENSOR_TYPE_GYROMETER_1D",
    "SENSOR_TYPE_GYROMETER_2D",
    "SENSOR_TYPE_GYROMETER_3D",
    "SENSOR_TYPE_SPEEDOMETER",
    "SENSOR_TYPE_COMPASS_1D",
    "SENSOR_TYPE_COMPASS_2D",
    "SENSOR_TYPE_COMPASS_3D",
    "SENSOR_TYPE_INCLINOMETER_1D",
    "SENSOR_TYPE_INCLINOMETER_2D",
    "SENSOR_TYPE_INCLINOMETER_3D",
    "SENSOR_TYPE_DISTANCE_1D",
    "SENSOR_TYPE_DISTANCE_2D",
    "SENSOR_TYPE_DISTANCE_3D",
    "SENSOR_TYPE_AGGREGATED_QUADRANT_ORIENTATION",
    "SENSOR_TYPE_AGGREGATED_DEVICE_ORIENTATION",
    "SENSOR_TYPE_AGGREGATED_SIMPLE_DEVICE_ORIENTATION",
    "SENSOR_TYPE_VOLTAGE",
    "SENSOR_TYPE_CURRENT",
    "SENSOR_TYPE_CAPACITANCE",
    "SENSOR_TYPE_RESISTANCE",
    "SENSOR_TYPE_INDUCTANCE",
    "SENSOR_TYPE_ELECTRICAL_POWER",
    "SENSOR_TYPE_POTENTIOMETER",
    "SENSOR_TYPE_FREQUENCY",
    "SENSOR_TYPE_BOOLEAN_SWITCH",
    "SENSOR_TYPE_MULTIVALUE_SWITCH",
    "SENSOR_TYPE_FORCE",
    "SENSOR_TYPE_SCALE",
    "SENSOR_TYPE_PRESSURE",
    "SENSOR_TYPE_STRAIN",
    "SENSOR_TYPE_BOOLEAN_SWITCH_ARRAY",
    "SENSOR_TYPE_HUMAN_PRESENCE",
    "SENSOR_TYPE_HUMAN_PROXIMITY",
    "SENSOR_TYPE_TOUCH",
    "SENSOR_TYPE_AMBIENT_LIGHT",
    "SENSOR_TYPE_RFID_SCANNER",
    "SENSOR_TYPE_BARCODE_SCANNER",
    "SENSOR_TYPE_CUSTOM",
    "SENSOR_TYPE_UNKNOWN",
    "SENSOR_DATA_TYPE_COMMON_GUID",
    "SENSOR_DATA_TYPE_TIMESTAMP",
    "SENSOR_DATA_TYPE_LOCATION_GUID",
    "SENSOR_DATA_TYPE_LATITUDE_DEGREES",
    "SENSOR_DATA_TYPE_LONGITUDE_DEGREES",
    "SENSOR_DATA_TYPE_ALTITUDE_SEALEVEL_METERS",
    "SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_METERS",
    "SENSOR_DATA_TYPE_SPEED_KNOTS",
    "SENSOR_DATA_TYPE_TRUE_HEADING_DEGREES",
    "SENSOR_DATA_TYPE_MAGNETIC_HEADING_DEGREES",
    "SENSOR_DATA_TYPE_MAGNETIC_VARIATION",
    "SENSOR_DATA_TYPE_FIX_QUALITY",
    "SENSOR_DATA_TYPE_FIX_TYPE",
    "SENSOR_DATA_TYPE_POSITION_DILUTION_OF_PRECISION",
    "SENSOR_DATA_TYPE_HORIZONAL_DILUTION_OF_PRECISION",
    "SENSOR_DATA_TYPE_VERTICAL_DILUTION_OF_PRECISION",
    "SENSOR_DATA_TYPE_SATELLITES_USED_COUNT",
    "SENSOR_DATA_TYPE_SATELLITES_USED_PRNS",
    "SENSOR_DATA_TYPE_SATELLITES_IN_VIEW",
    "SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_PRNS",
    "SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_ELEVATION",
    "SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_AZIMUTH",
    "SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_STN_RATIO",
    "SENSOR_DATA_TYPE_ERROR_RADIUS_METERS",
    "SENSOR_DATA_TYPE_ADDRESS1",
    "SENSOR_DATA_TYPE_ADDRESS2",
    "SENSOR_DATA_TYPE_CITY",
    "SENSOR_DATA_TYPE_STATE_PROVINCE",
    "SENSOR_DATA_TYPE_POSTALCODE",
    "SENSOR_DATA_TYPE_COUNTRY_REGION",
    "SENSOR_DATA_TYPE_ALTITUDE_ELLIPSOID_ERROR_METERS",
    "SENSOR_DATA_TYPE_ALTITUDE_SEALEVEL_ERROR_METERS",
    "SENSOR_DATA_TYPE_GPS_SELECTION_MODE",
    "SENSOR_DATA_TYPE_GPS_OPERATION_MODE",
    "SENSOR_DATA_TYPE_GPS_STATUS",
    "SENSOR_DATA_TYPE_GEOIDAL_SEPARATION",
    "SENSOR_DATA_TYPE_DGPS_DATA_AGE",
    "SENSOR_DATA_TYPE_ALTITUDE_ANTENNA_SEALEVEL_METERS",
    "SENSOR_DATA_TYPE_DIFFERENTIAL_REFERENCE_STATION_ID",
    "SENSOR_DATA_TYPE_NMEA_SENTENCE",
    "SENSOR_DATA_TYPE_SATELLITES_IN_VIEW_ID",
    "SENSOR_DATA_TYPE_LOCATION_SOURCE",
    "SENSOR_DATA_TYPE_SATELLITES_USED_PRNS_AND_CONSTELLATIONS",
    "SENSOR_DATA_TYPE_ENVIRONMENTAL_GUID",
    "SENSOR_DATA_TYPE_TEMPERATURE_CELSIUS",
    "SENSOR_DATA_TYPE_RELATIVE_HUMIDITY_PERCENT",
    "SENSOR_DATA_TYPE_ATMOSPHERIC_PRESSURE_BAR",
    "SENSOR_DATA_TYPE_WIND_DIRECTION_DEGREES_ANTICLOCKWISE",
    "SENSOR_DATA_TYPE_WIND_SPEED_METERS_PER_SECOND",
    "SENSOR_DATA_TYPE_MOTION_GUID",
    "SENSOR_DATA_TYPE_ACCELERATION_X_G",
    "SENSOR_DATA_TYPE_ACCELERATION_Y_G",
    "SENSOR_DATA_TYPE_ACCELERATION_Z_G",
    "SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_X_DEGREES_PER_SECOND_SQUARED",
    "SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_Y_DEGREES_PER_SECOND_SQUARED",
    "SENSOR_DATA_TYPE_ANGULAR_ACCELERATION_Z_DEGREES_PER_SECOND_SQUARED",
    "SENSOR_DATA_TYPE_SPEED_METERS_PER_SECOND",
    "SENSOR_DATA_TYPE_MOTION_STATE",
    "SENSOR_DATA_TYPE_ANGULAR_VELOCITY_X_DEGREES_PER_SECOND",
    "SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Y_DEGREES_PER_SECOND",
    "SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Z_DEGREES_PER_SECOND",
    "SENSOR_DATA_TYPE_ORIENTATION_GUID",
    "SENSOR_DATA_TYPE_TILT_X_DEGREES",
    "SENSOR_DATA_TYPE_TILT_Y_DEGREES",
    "SENSOR_DATA_TYPE_TILT_Z_DEGREES",
    "SENSOR_DATA_TYPE_MAGNETIC_HEADING_X_DEGREES",
    "SENSOR_DATA_TYPE_MAGNETIC_HEADING_Y_DEGREES",
    "SENSOR_DATA_TYPE_MAGNETIC_HEADING_Z_DEGREES",
    "SENSOR_DATA_TYPE_DISTANCE_X_METERS",
    "SENSOR_DATA_TYPE_DISTANCE_Y_METERS",
    "SENSOR_DATA_TYPE_DISTANCE_Z_METERS",
    "SENSOR_DATA_TYPE_MAGNETIC_HEADING_COMPENSATED_MAGNETIC_NORTH_DEGREES",
    "SENSOR_DATA_TYPE_MAGNETIC_HEADING_COMPENSATED_TRUE_NORTH_DEGREES",
    "SENSOR_DATA_TYPE_MAGNETIC_HEADING_MAGNETIC_NORTH_DEGREES",
    "SENSOR_DATA_TYPE_MAGNETIC_HEADING_TRUE_NORTH_DEGREES",
    "SENSOR_DATA_TYPE_QUADRANT_ANGLE_DEGREES",
    "SENSOR_DATA_TYPE_ROTATION_MATRIX",
    "SENSOR_DATA_TYPE_QUATERNION",
    "SENSOR_DATA_TYPE_SIMPLE_DEVICE_ORIENTATION",
    "SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_X_MILLIGAUSS",
    "SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_Y_MILLIGAUSS",
    "SENSOR_DATA_TYPE_MAGNETIC_FIELD_STRENGTH_Z_MILLIGAUSS",
    "SENSOR_DATA_TYPE_MAGNETOMETER_ACCURACY",
    "SENSOR_DATA_TYPE_GUID_MECHANICAL_GUID",
    "SENSOR_DATA_TYPE_BOOLEAN_SWITCH_STATE",
    "SENSOR_DATA_TYPE_MULTIVALUE_SWITCH_STATE",
    "SENSOR_DATA_TYPE_FORCE_NEWTONS",
    "SENSOR_DATA_TYPE_ABSOLUTE_PRESSURE_PASCAL",
    "SENSOR_DATA_TYPE_GAUGE_PRESSURE_PASCAL",
    "SENSOR_DATA_TYPE_STRAIN",
    "SENSOR_DATA_TYPE_WEIGHT_KILOGRAMS",
    "SENSOR_DATA_TYPE_BOOLEAN_SWITCH_ARRAY_STATES",
    "SENSOR_DATA_TYPE_BIOMETRIC_GUID",
    "SENSOR_DATA_TYPE_HUMAN_PRESENCE",
    "SENSOR_DATA_TYPE_HUMAN_PROXIMITY_METERS",
    "SENSOR_DATA_TYPE_TOUCH_STATE",
    "SENSOR_DATA_TYPE_LIGHT_GUID",
    "SENSOR_DATA_TYPE_LIGHT_LEVEL_LUX",
    "SENSOR_DATA_TYPE_LIGHT_TEMPERATURE_KELVIN",
    "SENSOR_DATA_TYPE_LIGHT_CHROMACITY",
    "SENSOR_DATA_TYPE_SCANNER_GUID",
    "SENSOR_DATA_TYPE_RFID_TAG_40_BIT",
    "SENSOR_DATA_TYPE_ELECTRICAL_GUID",
    "SENSOR_DATA_TYPE_VOLTAGE_VOLTS",
    "SENSOR_DATA_TYPE_CURRENT_AMPS",
    "SENSOR_DATA_TYPE_CAPACITANCE_FARAD",
    "SENSOR_DATA_TYPE_RESISTANCE_OHMS",
    "SENSOR_DATA_TYPE_INDUCTANCE_HENRY",
    "SENSOR_DATA_TYPE_ELECTRICAL_POWER_WATTS",
    "SENSOR_DATA_TYPE_ELECTRICAL_PERCENT_OF_RANGE",
    "SENSOR_DATA_TYPE_ELECTRICAL_FREQUENCY_HERTZ",
    "SENSOR_DATA_TYPE_CUSTOM_GUID",
    "SENSOR_DATA_TYPE_CUSTOM_USAGE",
    "SENSOR_DATA_TYPE_CUSTOM_BOOLEAN_ARRAY",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE1",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE2",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE3",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE4",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE5",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE6",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE7",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE8",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE9",
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
    "SENSOR_DATA_TYPE_CUSTOM_VALUE20",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE21",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE22",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE23",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE24",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE25",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE26",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE27",
    "SENSOR_DATA_TYPE_CUSTOM_VALUE28",
    "SENSOR_PROPERTY_TEST_GUID",
    "SENSOR_PROPERTY_CLEAR_ASSISTANCE_DATA",
    "SENSOR_PROPERTY_TURN_ON_OFF_NMEA",
    "GNSS_CLEAR_ALL_ASSISTANCE_DATA",
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
    "GUID_SensorType_Humidity",
    "GUID_SensorType_LinearAccelerometer",
    "GUID_SensorType_Magnetometer3D",
    "GUID_SensorType_Orientation",
    "GUID_SensorType_Pedometer",
    "GUID_SensorType_Proximity",
    "GUID_SensorType_RelativeOrientation",
    "GUID_SensorType_SimpleDeviceOrientation",
    "GUID_SensorType_Temperature",
    "GUID_SensorType_HingeAngle",
    "SENSOR_PROPERTY_LIST_HEADER_SIZE",
    "SensorManager",
    "SensorCollection",
    "Sensor",
    "SensorDataReport",
    "SensorState",
    "SENSOR_STATE_MIN",
    "SENSOR_STATE_READY",
    "SENSOR_STATE_NOT_AVAILABLE",
    "SENSOR_STATE_NO_DATA",
    "SENSOR_STATE_INITIALIZING",
    "SENSOR_STATE_ACCESS_DENIED",
    "SENSOR_STATE_ERROR",
    "SENSOR_STATE_MAX",
    "SensorConnectionType",
    "SENSOR_CONNECTION_TYPE_PC_INTEGRATED",
    "SENSOR_CONNECTION_TYPE_PC_ATTACHED",
    "SENSOR_CONNECTION_TYPE_PC_EXTERNAL",
    "LOCATION_DESIRED_ACCURACY",
    "LOCATION_DESIRED_ACCURACY_DEFAULT",
    "LOCATION_DESIRED_ACCURACY_HIGH",
    "LOCATION_POSITION_SOURCE",
    "LOCATION_POSITION_SOURCE_CELLULAR",
    "LOCATION_POSITION_SOURCE_SATELLITE",
    "LOCATION_POSITION_SOURCE_WIFI",
    "LOCATION_POSITION_SOURCE_IPADDRESS",
    "LOCATION_POSITION_SOURCE_UNKNOWN",
    "SimpleDeviceOrientation",
    "SIMPLE_DEVICE_ORIENTATION_NOT_ROTATED",
    "SIMPLE_DEVICE_ORIENTATION_ROTATED_90",
    "SIMPLE_DEVICE_ORIENTATION_ROTATED_180",
    "SIMPLE_DEVICE_ORIENTATION_ROTATED_270",
    "SIMPLE_DEVICE_ORIENTATION_ROTATED_FACE_UP",
    "SIMPLE_DEVICE_ORIENTATION_ROTATED_FACE_DOWN",
    "MagnetometerAccuracy",
    "MAGNETOMETER_ACCURACY_UNKNOWN",
    "MAGNETOMETER_ACCURACY_UNRELIABLE",
    "MAGNETOMETER_ACCURACY_APPROXIMATE",
    "MAGNETOMETER_ACCURACY_HIGH",
    "ISensorManager",
    "ILocationPermissions",
    "ISensorCollection",
    "ISensor",
    "ISensorDataReport",
    "ISensorManagerEvents",
    "ISensorEvents",
    "ACTIVITY_STATE_COUNT",
    "ACTIVITY_STATE_COUNT_ActivityStateCount",
    "ACTIVITY_STATE",
    "ActivityState_Unknown",
    "ActivityState_Stationary",
    "ActivityState_Fidgeting",
    "ActivityState_Walking",
    "ActivityState_Running",
    "ActivityState_InVehicle",
    "ActivityState_Biking",
    "ActivityState_Idle",
    "ActivityState_Max",
    "ActivityState_Force_Dword",
    "ELEVATION_CHANGE_MODE",
    "ElevationChangeMode_Unknown",
    "ElevationChangeMode_Elevator",
    "ElevationChangeMode_Stepping",
    "ElevationChangeMode_Max",
    "ElevationChangeMode_Force_Dword",
    "MAGNETOMETER_ACCURACY",
    "MagnetometerAccuracy_Unknown",
    "MagnetometerAccuracy_Unreliable",
    "MagnetometerAccuracy_Approximate",
    "MagnetometerAccuracy_High",
    "PEDOMETER_STEP_TYPE_COUNT",
    "PEDOMETER_STEP_TYPE_COUNT_PedometerStepTypeCount",
    "PEDOMETER_STEP_TYPE",
    "PedometerStepType_Unknown",
    "PedometerStepType_Walking",
    "PedometerStepType_Running",
    "PedometerStepType_Max",
    "PedometerStepType_Force_Dword",
    "PROXIMITY_TYPE",
    "ProximityType_ObjectProximity",
    "ProximityType_HumanProximity",
    "ProximityType_Force_Dword",
    "HUMAN_PRESENCE_DETECTION_TYPE_COUNT",
    "HUMAN_PRESENCE_DETECTION_TYPE_COUNT_HumanPresenceDetectionTypeCount",
    "HUMAN_PRESENCE_DETECTION_TYPE",
    "HumanPresenceDetectionType_VendorDefinedNonBiometric",
    "HumanPresenceDetectionType_VendorDefinedBiometric",
    "HumanPresenceDetectionType_FacialBiometric",
    "HumanPresenceDetectionType_AudioBiometric",
    "HumanPresenceDetectionType_Force_Dword",
    "SIMPLE_DEVICE_ORIENTATION",
    "SimpleDeviceOrientation_NotRotated",
    "SimpleDeviceOrientation_Rotated90DegreesCounterclockwise",
    "SimpleDeviceOrientation_Rotated180DegreesCounterclockwise",
    "SimpleDeviceOrientation_Rotated270DegreesCounterclockwise",
    "SimpleDeviceOrientation_Faceup",
    "SimpleDeviceOrientation_Facedown",
    "SENSOR_STATE",
    "SensorState_Initializing",
    "SensorState_Idle",
    "SensorState_Active",
    "SensorState_Error",
    "SENSOR_CONNECTION_TYPES",
    "SensorConnectionType_Integrated",
    "SensorConnectionType_Attached",
    "SensorConnectionType_External",
    "SENSOR_VALUE_PAIR",
    "SENSOR_COLLECTION_LIST",
    "SENSOR_PROPERTY_LIST",
    "VEC3D",
    "MATRIX3X3",
    "QUATERNION",
    "AXIS",
    "AXIS_X",
    "AXIS_Y",
    "AXIS_Z",
    "AXIS_MAX",
    "GetPerformanceTime",
    "InitPropVariantFromFloat",
    "PropKeyFindKeyGetPropVariant",
    "PropKeyFindKeySetPropVariant",
    "PropKeyFindKeyGetFileTime",
    "PropKeyFindKeyGetGuid",
    "PropKeyFindKeyGetBool",
    "PropKeyFindKeyGetUlong",
    "PropKeyFindKeyGetUshort",
    "PropKeyFindKeyGetFloat",
    "PropKeyFindKeyGetDouble",
    "PropKeyFindKeyGetInt32",
    "PropKeyFindKeyGetInt64",
    "PropKeyFindKeyGetNthUlong",
    "PropKeyFindKeyGetNthUshort",
    "PropKeyFindKeyGetNthInt64",
    "IsKeyPresentInPropertyList",
    "IsKeyPresentInCollectionList",
    "IsCollectionListSame",
    "PropVariantGetInformation",
    "PropertiesListCopy",
    "PropertiesListGetFillableCount",
    "CollectionsListGetMarshalledSize",
    "CollectionsListCopyAndMarshall",
    "CollectionsListMarshall",
    "CollectionsListGetMarshalledSizeWithoutSerialization",
    "CollectionsListUpdateMarshalledPointer",
    "SerializationBufferAllocate",
    "SerializationBufferFree",
    "CollectionsListGetSerializedSize",
    "CollectionsListSerializeToBuffer",
    "CollectionsListAllocateBufferAndSerialize",
    "CollectionsListDeserializeFromBuffer",
    "SensorCollectionGetAt",
    "CollectionsListGetFillableCount",
    "EvaluateActivityThresholds",
    "CollectionsListSortSubscribedActivitiesByConfidence",
    "InitPropVariantFromCLSIDArray",
    "IsSensorSubscribed",
    "IsGUIDPresentInList",
]
