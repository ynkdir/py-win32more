from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Devices.DeviceQuery
import win32more.Devices.Properties
import win32more.Foundation
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
@winfunctype('api-ms-win-devices-query-l1-1-0.dll')
def DevCreateObjectQuery(ObjectType: win32more.Devices.DeviceQuery.DEV_OBJECT_TYPE, QueryFlags: UInt32, cRequestedProperties: UInt32, pRequestedProperties: POINTER(win32more.Devices.Properties.DEVPROPCOMPKEY_head), cFilterExpressionCount: UInt32, pFilter: POINTER(win32more.Devices.DeviceQuery.DEVPROP_FILTER_EXPRESSION_head), pCallback: win32more.Devices.DeviceQuery.PDEV_QUERY_RESULT_CALLBACK, pContext: c_void_p, phDevQuery: POINTER(POINTER(win32more.Devices.DeviceQuery.HDEVQUERY___head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-devices-query-l1-1-1.dll')
def DevCreateObjectQueryEx(ObjectType: win32more.Devices.DeviceQuery.DEV_OBJECT_TYPE, QueryFlags: UInt32, cRequestedProperties: UInt32, pRequestedProperties: POINTER(win32more.Devices.Properties.DEVPROPCOMPKEY_head), cFilterExpressionCount: UInt32, pFilter: POINTER(win32more.Devices.DeviceQuery.DEVPROP_FILTER_EXPRESSION_head), cExtendedParameterCount: UInt32, pExtendedParameters: POINTER(win32more.Devices.DeviceQuery.DEV_QUERY_PARAMETER_head), pCallback: win32more.Devices.DeviceQuery.PDEV_QUERY_RESULT_CALLBACK, pContext: c_void_p, phDevQuery: POINTER(POINTER(win32more.Devices.DeviceQuery.HDEVQUERY___head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-devices-query-l1-1-0.dll')
def DevCreateObjectQueryFromId(ObjectType: win32more.Devices.DeviceQuery.DEV_OBJECT_TYPE, pszObjectId: win32more.Foundation.PWSTR, QueryFlags: UInt32, cRequestedProperties: UInt32, pRequestedProperties: POINTER(win32more.Devices.Properties.DEVPROPCOMPKEY_head), cFilterExpressionCount: UInt32, pFilter: POINTER(win32more.Devices.DeviceQuery.DEVPROP_FILTER_EXPRESSION_head), pCallback: win32more.Devices.DeviceQuery.PDEV_QUERY_RESULT_CALLBACK, pContext: c_void_p, phDevQuery: POINTER(POINTER(win32more.Devices.DeviceQuery.HDEVQUERY___head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-devices-query-l1-1-1.dll')
def DevCreateObjectQueryFromIdEx(ObjectType: win32more.Devices.DeviceQuery.DEV_OBJECT_TYPE, pszObjectId: win32more.Foundation.PWSTR, QueryFlags: UInt32, cRequestedProperties: UInt32, pRequestedProperties: POINTER(win32more.Devices.Properties.DEVPROPCOMPKEY_head), cFilterExpressionCount: UInt32, pFilter: POINTER(win32more.Devices.DeviceQuery.DEVPROP_FILTER_EXPRESSION_head), cExtendedParameterCount: UInt32, pExtendedParameters: POINTER(win32more.Devices.DeviceQuery.DEV_QUERY_PARAMETER_head), pCallback: win32more.Devices.DeviceQuery.PDEV_QUERY_RESULT_CALLBACK, pContext: c_void_p, phDevQuery: POINTER(POINTER(win32more.Devices.DeviceQuery.HDEVQUERY___head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-devices-query-l1-1-0.dll')
def DevCreateObjectQueryFromIds(ObjectType: win32more.Devices.DeviceQuery.DEV_OBJECT_TYPE, pszzObjectIds: win32more.Foundation.PWSTR, QueryFlags: UInt32, cRequestedProperties: UInt32, pRequestedProperties: POINTER(win32more.Devices.Properties.DEVPROPCOMPKEY_head), cFilterExpressionCount: UInt32, pFilter: POINTER(win32more.Devices.DeviceQuery.DEVPROP_FILTER_EXPRESSION_head), pCallback: win32more.Devices.DeviceQuery.PDEV_QUERY_RESULT_CALLBACK, pContext: c_void_p, phDevQuery: POINTER(POINTER(win32more.Devices.DeviceQuery.HDEVQUERY___head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-devices-query-l1-1-1.dll')
def DevCreateObjectQueryFromIdsEx(ObjectType: win32more.Devices.DeviceQuery.DEV_OBJECT_TYPE, pszzObjectIds: win32more.Foundation.PWSTR, QueryFlags: UInt32, cRequestedProperties: UInt32, pRequestedProperties: POINTER(win32more.Devices.Properties.DEVPROPCOMPKEY_head), cFilterExpressionCount: UInt32, pFilter: POINTER(win32more.Devices.DeviceQuery.DEVPROP_FILTER_EXPRESSION_head), cExtendedParameterCount: UInt32, pExtendedParameters: POINTER(win32more.Devices.DeviceQuery.DEV_QUERY_PARAMETER_head), pCallback: win32more.Devices.DeviceQuery.PDEV_QUERY_RESULT_CALLBACK, pContext: c_void_p, phDevQuery: POINTER(POINTER(win32more.Devices.DeviceQuery.HDEVQUERY___head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-devices-query-l1-1-0.dll')
def DevCloseObjectQuery(hDevQuery: POINTER(win32more.Devices.DeviceQuery.HDEVQUERY___head)) -> Void: ...
@winfunctype('api-ms-win-devices-query-l1-1-0.dll')
def DevGetObjects(ObjectType: win32more.Devices.DeviceQuery.DEV_OBJECT_TYPE, QueryFlags: UInt32, cRequestedProperties: UInt32, pRequestedProperties: POINTER(win32more.Devices.Properties.DEVPROPCOMPKEY_head), cFilterExpressionCount: UInt32, pFilter: POINTER(win32more.Devices.DeviceQuery.DEVPROP_FILTER_EXPRESSION_head), pcObjectCount: POINTER(UInt32), ppObjects: POINTER(POINTER(win32more.Devices.DeviceQuery.DEV_OBJECT_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-devices-query-l1-1-1.dll')
def DevGetObjectsEx(ObjectType: win32more.Devices.DeviceQuery.DEV_OBJECT_TYPE, QueryFlags: UInt32, cRequestedProperties: UInt32, pRequestedProperties: POINTER(win32more.Devices.Properties.DEVPROPCOMPKEY_head), cFilterExpressionCount: UInt32, pFilter: POINTER(win32more.Devices.DeviceQuery.DEVPROP_FILTER_EXPRESSION_head), cExtendedParameterCount: UInt32, pExtendedParameters: POINTER(win32more.Devices.DeviceQuery.DEV_QUERY_PARAMETER_head), pcObjectCount: POINTER(UInt32), ppObjects: POINTER(POINTER(win32more.Devices.DeviceQuery.DEV_OBJECT_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-devices-query-l1-1-0.dll')
def DevFreeObjects(cObjectCount: UInt32, pObjects: POINTER(win32more.Devices.DeviceQuery.DEV_OBJECT_head)) -> Void: ...
@winfunctype('api-ms-win-devices-query-l1-1-0.dll')
def DevGetObjectProperties(ObjectType: win32more.Devices.DeviceQuery.DEV_OBJECT_TYPE, pszObjectId: win32more.Foundation.PWSTR, QueryFlags: UInt32, cRequestedProperties: UInt32, pRequestedProperties: POINTER(win32more.Devices.Properties.DEVPROPCOMPKEY_head), pcPropertyCount: POINTER(UInt32), ppProperties: POINTER(POINTER(win32more.Devices.Properties.DEVPROPERTY_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-devices-query-l1-1-1.dll')
def DevGetObjectPropertiesEx(ObjectType: win32more.Devices.DeviceQuery.DEV_OBJECT_TYPE, pszObjectId: win32more.Foundation.PWSTR, QueryFlags: UInt32, cRequestedProperties: UInt32, pRequestedProperties: POINTER(win32more.Devices.Properties.DEVPROPCOMPKEY_head), cExtendedParameterCount: UInt32, pExtendedParameters: POINTER(win32more.Devices.DeviceQuery.DEV_QUERY_PARAMETER_head), pcPropertyCount: POINTER(UInt32), ppProperties: POINTER(POINTER(win32more.Devices.Properties.DEVPROPERTY_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('api-ms-win-devices-query-l1-1-0.dll')
def DevFreeObjectProperties(cPropertyCount: UInt32, pProperties: POINTER(win32more.Devices.Properties.DEVPROPERTY_head)) -> Void: ...
@winfunctype('api-ms-win-devices-query-l1-1-0.dll')
def DevFindProperty(pKey: POINTER(win32more.Devices.Properties.DEVPROPKEY_head), Store: win32more.Devices.Properties.DEVPROPSTORE, pszLocaleName: win32more.Foundation.PWSTR, cProperties: UInt32, pProperties: POINTER(win32more.Devices.Properties.DEVPROPERTY_head)) -> POINTER(win32more.Devices.Properties.DEVPROPERTY_head): ...
class DEV_OBJECT(Structure):
    ObjectType: win32more.Devices.DeviceQuery.DEV_OBJECT_TYPE
    pszObjectId: win32more.Foundation.PWSTR
    cPropertyCount: UInt32
    pProperties: POINTER(win32more.Devices.Properties.DEVPROPERTY_head)
DEV_OBJECT_TYPE = Int32
DEV_OBJECT_TYPE_DevObjectTypeUnknown: DEV_OBJECT_TYPE = 0
DEV_OBJECT_TYPE_DevObjectTypeDeviceInterface: DEV_OBJECT_TYPE = 1
DEV_OBJECT_TYPE_DevObjectTypeDeviceContainer: DEV_OBJECT_TYPE = 2
DEV_OBJECT_TYPE_DevObjectTypeDevice: DEV_OBJECT_TYPE = 3
DEV_OBJECT_TYPE_DevObjectTypeDeviceInterfaceClass: DEV_OBJECT_TYPE = 4
DEV_OBJECT_TYPE_DevObjectTypeAEP: DEV_OBJECT_TYPE = 5
DEV_OBJECT_TYPE_DevObjectTypeAEPContainer: DEV_OBJECT_TYPE = 6
DEV_OBJECT_TYPE_DevObjectTypeDeviceInstallerClass: DEV_OBJECT_TYPE = 7
DEV_OBJECT_TYPE_DevObjectTypeDeviceInterfaceDisplay: DEV_OBJECT_TYPE = 8
DEV_OBJECT_TYPE_DevObjectTypeDeviceContainerDisplay: DEV_OBJECT_TYPE = 9
DEV_OBJECT_TYPE_DevObjectTypeAEPService: DEV_OBJECT_TYPE = 10
DEV_OBJECT_TYPE_DevObjectTypeDevicePanel: DEV_OBJECT_TYPE = 11
DEV_QUERY_FLAGS = Int32
DEV_QUERY_FLAGS_DevQueryFlagNone: DEV_QUERY_FLAGS = 0
DEV_QUERY_FLAGS_DevQueryFlagUpdateResults: DEV_QUERY_FLAGS = 1
DEV_QUERY_FLAGS_DevQueryFlagAllProperties: DEV_QUERY_FLAGS = 2
DEV_QUERY_FLAGS_DevQueryFlagLocalize: DEV_QUERY_FLAGS = 4
DEV_QUERY_FLAGS_DevQueryFlagAsyncClose: DEV_QUERY_FLAGS = 8
class DEV_QUERY_PARAMETER(Structure):
    Key: win32more.Devices.Properties.DEVPROPKEY
    Type: UInt32
    BufferSize: UInt32
    Buffer: c_void_p
DEV_QUERY_RESULT_ACTION = Int32
DEV_QUERY_RESULT_ACTION_DevQueryResultStateChange: DEV_QUERY_RESULT_ACTION = 0
DEV_QUERY_RESULT_ACTION_DevQueryResultAdd: DEV_QUERY_RESULT_ACTION = 1
DEV_QUERY_RESULT_ACTION_DevQueryResultUpdate: DEV_QUERY_RESULT_ACTION = 2
DEV_QUERY_RESULT_ACTION_DevQueryResultRemove: DEV_QUERY_RESULT_ACTION = 3
class DEV_QUERY_RESULT_ACTION_DATA(Structure):
    Action: win32more.Devices.DeviceQuery.DEV_QUERY_RESULT_ACTION
    Data: _DEV_QUERY_RESULT_UPDATE_PAYLOAD
    class _DEV_QUERY_RESULT_UPDATE_PAYLOAD(Union):
        State: win32more.Devices.DeviceQuery.DEV_QUERY_STATE
        DeviceObject: win32more.Devices.DeviceQuery.DEV_OBJECT
DEV_QUERY_STATE = Int32
DEV_QUERY_STATE_DevQueryStateInitialized: DEV_QUERY_STATE = 0
DEV_QUERY_STATE_DevQueryStateEnumCompleted: DEV_QUERY_STATE = 1
DEV_QUERY_STATE_DevQueryStateAborted: DEV_QUERY_STATE = 2
DEV_QUERY_STATE_DevQueryStateClosed: DEV_QUERY_STATE = 3
class DEVPROP_FILTER_EXPRESSION(Structure):
    Operator: win32more.Devices.DeviceQuery.DEVPROP_OPERATOR
    Property: win32more.Devices.Properties.DEVPROPERTY
DEVPROP_OPERATOR = UInt32
DEVPROP_OPERATOR_MODIFIER_NOT: DEVPROP_OPERATOR = 65536
DEVPROP_OPERATOR_MODIFIER_IGNORE_CASE: DEVPROP_OPERATOR = 131072
DEVPROP_OPERATOR_NONE: DEVPROP_OPERATOR = 0
DEVPROP_OPERATOR_EXISTS: DEVPROP_OPERATOR = 1
DEVPROP_OPERATOR_NOT_EXISTS: DEVPROP_OPERATOR = 65537
DEVPROP_OPERATOR_EQUALS: DEVPROP_OPERATOR = 2
DEVPROP_OPERATOR_NOT_EQUALS: DEVPROP_OPERATOR = 65538
DEVPROP_OPERATOR_GREATER_THAN: DEVPROP_OPERATOR = 3
DEVPROP_OPERATOR_LESS_THAN: DEVPROP_OPERATOR = 4
DEVPROP_OPERATOR_GREATER_THAN_EQUALS: DEVPROP_OPERATOR = 5
DEVPROP_OPERATOR_LESS_THAN_EQUALS: DEVPROP_OPERATOR = 6
DEVPROP_OPERATOR_EQUALS_IGNORE_CASE: DEVPROP_OPERATOR = 131074
DEVPROP_OPERATOR_NOT_EQUALS_IGNORE_CASE: DEVPROP_OPERATOR = 196610
DEVPROP_OPERATOR_BITWISE_AND: DEVPROP_OPERATOR = 7
DEVPROP_OPERATOR_BITWISE_OR: DEVPROP_OPERATOR = 8
DEVPROP_OPERATOR_BEGINS_WITH: DEVPROP_OPERATOR = 9
DEVPROP_OPERATOR_ENDS_WITH: DEVPROP_OPERATOR = 10
DEVPROP_OPERATOR_CONTAINS: DEVPROP_OPERATOR = 11
DEVPROP_OPERATOR_BEGINS_WITH_IGNORE_CASE: DEVPROP_OPERATOR = 131081
DEVPROP_OPERATOR_ENDS_WITH_IGNORE_CASE: DEVPROP_OPERATOR = 131082
DEVPROP_OPERATOR_CONTAINS_IGNORE_CASE: DEVPROP_OPERATOR = 131083
DEVPROP_OPERATOR_LIST_CONTAINS: DEVPROP_OPERATOR = 4096
DEVPROP_OPERATOR_LIST_ELEMENT_BEGINS_WITH: DEVPROP_OPERATOR = 8192
DEVPROP_OPERATOR_LIST_ELEMENT_ENDS_WITH: DEVPROP_OPERATOR = 12288
DEVPROP_OPERATOR_LIST_ELEMENT_CONTAINS: DEVPROP_OPERATOR = 16384
DEVPROP_OPERATOR_LIST_CONTAINS_IGNORE_CASE: DEVPROP_OPERATOR = 135168
DEVPROP_OPERATOR_LIST_ELEMENT_BEGINS_WITH_IGNORE_CASE: DEVPROP_OPERATOR = 139264
DEVPROP_OPERATOR_LIST_ELEMENT_ENDS_WITH_IGNORE_CASE: DEVPROP_OPERATOR = 143360
DEVPROP_OPERATOR_LIST_ELEMENT_CONTAINS_IGNORE_CASE: DEVPROP_OPERATOR = 147456
DEVPROP_OPERATOR_AND_OPEN: DEVPROP_OPERATOR = 1048576
DEVPROP_OPERATOR_AND_CLOSE: DEVPROP_OPERATOR = 2097152
DEVPROP_OPERATOR_OR_OPEN: DEVPROP_OPERATOR = 3145728
DEVPROP_OPERATOR_OR_CLOSE: DEVPROP_OPERATOR = 4194304
DEVPROP_OPERATOR_NOT_OPEN: DEVPROP_OPERATOR = 5242880
DEVPROP_OPERATOR_NOT_CLOSE: DEVPROP_OPERATOR = 6291456
DEVPROP_OPERATOR_ARRAY_CONTAINS: DEVPROP_OPERATOR = 268435456
DEVPROP_OPERATOR_MASK_EVAL: DEVPROP_OPERATOR = 4095
DEVPROP_OPERATOR_MASK_LIST: DEVPROP_OPERATOR = 61440
DEVPROP_OPERATOR_MASK_MODIFIER: DEVPROP_OPERATOR = 983040
DEVPROP_OPERATOR_MASK_NOT_LOGICAL: DEVPROP_OPERATOR = 4027580415
DEVPROP_OPERATOR_MASK_LOGICAL: DEVPROP_OPERATOR = 267386880
DEVPROP_OPERATOR_MASK_ARRAY: DEVPROP_OPERATOR = 4026531840
class HDEVQUERY__(Structure):
    unused: Int32
@winfunctype_pointer
def PDEV_QUERY_RESULT_CALLBACK(hDevQuery: POINTER(win32more.Devices.DeviceQuery.HDEVQUERY___head), pContext: c_void_p, pActionData: POINTER(win32more.Devices.DeviceQuery.DEV_QUERY_RESULT_ACTION_DATA_head)) -> Void: ...
make_head(_module, 'DEV_OBJECT')
make_head(_module, 'DEV_QUERY_PARAMETER')
make_head(_module, 'DEV_QUERY_RESULT_ACTION_DATA')
make_head(_module, 'DEVPROP_FILTER_EXPRESSION')
make_head(_module, 'HDEVQUERY__')
make_head(_module, 'PDEV_QUERY_RESULT_CALLBACK')
__all__ = [
    "DEVPROP_FILTER_EXPRESSION",
    "DEVPROP_OPERATOR",
    "DEVPROP_OPERATOR_AND_CLOSE",
    "DEVPROP_OPERATOR_AND_OPEN",
    "DEVPROP_OPERATOR_ARRAY_CONTAINS",
    "DEVPROP_OPERATOR_BEGINS_WITH",
    "DEVPROP_OPERATOR_BEGINS_WITH_IGNORE_CASE",
    "DEVPROP_OPERATOR_BITWISE_AND",
    "DEVPROP_OPERATOR_BITWISE_OR",
    "DEVPROP_OPERATOR_CONTAINS",
    "DEVPROP_OPERATOR_CONTAINS_IGNORE_CASE",
    "DEVPROP_OPERATOR_ENDS_WITH",
    "DEVPROP_OPERATOR_ENDS_WITH_IGNORE_CASE",
    "DEVPROP_OPERATOR_EQUALS",
    "DEVPROP_OPERATOR_EQUALS_IGNORE_CASE",
    "DEVPROP_OPERATOR_EXISTS",
    "DEVPROP_OPERATOR_GREATER_THAN",
    "DEVPROP_OPERATOR_GREATER_THAN_EQUALS",
    "DEVPROP_OPERATOR_LESS_THAN",
    "DEVPROP_OPERATOR_LESS_THAN_EQUALS",
    "DEVPROP_OPERATOR_LIST_CONTAINS",
    "DEVPROP_OPERATOR_LIST_CONTAINS_IGNORE_CASE",
    "DEVPROP_OPERATOR_LIST_ELEMENT_BEGINS_WITH",
    "DEVPROP_OPERATOR_LIST_ELEMENT_BEGINS_WITH_IGNORE_CASE",
    "DEVPROP_OPERATOR_LIST_ELEMENT_CONTAINS",
    "DEVPROP_OPERATOR_LIST_ELEMENT_CONTAINS_IGNORE_CASE",
    "DEVPROP_OPERATOR_LIST_ELEMENT_ENDS_WITH",
    "DEVPROP_OPERATOR_LIST_ELEMENT_ENDS_WITH_IGNORE_CASE",
    "DEVPROP_OPERATOR_MASK_ARRAY",
    "DEVPROP_OPERATOR_MASK_EVAL",
    "DEVPROP_OPERATOR_MASK_LIST",
    "DEVPROP_OPERATOR_MASK_LOGICAL",
    "DEVPROP_OPERATOR_MASK_MODIFIER",
    "DEVPROP_OPERATOR_MASK_NOT_LOGICAL",
    "DEVPROP_OPERATOR_MODIFIER_IGNORE_CASE",
    "DEVPROP_OPERATOR_MODIFIER_NOT",
    "DEVPROP_OPERATOR_NONE",
    "DEVPROP_OPERATOR_NOT_CLOSE",
    "DEVPROP_OPERATOR_NOT_EQUALS",
    "DEVPROP_OPERATOR_NOT_EQUALS_IGNORE_CASE",
    "DEVPROP_OPERATOR_NOT_EXISTS",
    "DEVPROP_OPERATOR_NOT_OPEN",
    "DEVPROP_OPERATOR_OR_CLOSE",
    "DEVPROP_OPERATOR_OR_OPEN",
    "DEV_OBJECT",
    "DEV_OBJECT_TYPE",
    "DEV_OBJECT_TYPE_DevObjectTypeAEP",
    "DEV_OBJECT_TYPE_DevObjectTypeAEPContainer",
    "DEV_OBJECT_TYPE_DevObjectTypeAEPService",
    "DEV_OBJECT_TYPE_DevObjectTypeDevice",
    "DEV_OBJECT_TYPE_DevObjectTypeDeviceContainer",
    "DEV_OBJECT_TYPE_DevObjectTypeDeviceContainerDisplay",
    "DEV_OBJECT_TYPE_DevObjectTypeDeviceInstallerClass",
    "DEV_OBJECT_TYPE_DevObjectTypeDeviceInterface",
    "DEV_OBJECT_TYPE_DevObjectTypeDeviceInterfaceClass",
    "DEV_OBJECT_TYPE_DevObjectTypeDeviceInterfaceDisplay",
    "DEV_OBJECT_TYPE_DevObjectTypeDevicePanel",
    "DEV_OBJECT_TYPE_DevObjectTypeUnknown",
    "DEV_QUERY_FLAGS",
    "DEV_QUERY_FLAGS_DevQueryFlagAllProperties",
    "DEV_QUERY_FLAGS_DevQueryFlagAsyncClose",
    "DEV_QUERY_FLAGS_DevQueryFlagLocalize",
    "DEV_QUERY_FLAGS_DevQueryFlagNone",
    "DEV_QUERY_FLAGS_DevQueryFlagUpdateResults",
    "DEV_QUERY_PARAMETER",
    "DEV_QUERY_RESULT_ACTION",
    "DEV_QUERY_RESULT_ACTION_DATA",
    "DEV_QUERY_RESULT_ACTION_DevQueryResultAdd",
    "DEV_QUERY_RESULT_ACTION_DevQueryResultRemove",
    "DEV_QUERY_RESULT_ACTION_DevQueryResultStateChange",
    "DEV_QUERY_RESULT_ACTION_DevQueryResultUpdate",
    "DEV_QUERY_STATE",
    "DEV_QUERY_STATE_DevQueryStateAborted",
    "DEV_QUERY_STATE_DevQueryStateClosed",
    "DEV_QUERY_STATE_DevQueryStateEnumCompleted",
    "DEV_QUERY_STATE_DevQueryStateInitialized",
    "DevCloseObjectQuery",
    "DevCreateObjectQuery",
    "DevCreateObjectQueryEx",
    "DevCreateObjectQueryFromId",
    "DevCreateObjectQueryFromIdEx",
    "DevCreateObjectQueryFromIds",
    "DevCreateObjectQueryFromIdsEx",
    "DevFindProperty",
    "DevFreeObjectProperties",
    "DevFreeObjects",
    "DevGetObjectProperties",
    "DevGetObjectPropertiesEx",
    "DevGetObjects",
    "DevGetObjectsEx",
    "HDEVQUERY__",
    "PDEV_QUERY_RESULT_CALLBACK",
]
_arch_optional = [
]
