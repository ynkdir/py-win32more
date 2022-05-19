from win32more import *
import win32more.Devices.DeviceQuery
import win32more.Devices.Properties
import win32more.Foundation

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
DEVPROP_OPERATOR = UInt32
DEVPROP_OPERATOR_MODIFIER_NOT = 65536
DEVPROP_OPERATOR_MODIFIER_IGNORE_CASE = 131072
DEVPROP_OPERATOR_NONE = 0
DEVPROP_OPERATOR_EXISTS = 1
DEVPROP_OPERATOR_NOT_EXISTS = 65537
DEVPROP_OPERATOR_EQUALS = 2
DEVPROP_OPERATOR_NOT_EQUALS = 65538
DEVPROP_OPERATOR_GREATER_THAN = 3
DEVPROP_OPERATOR_LESS_THAN = 4
DEVPROP_OPERATOR_GREATER_THAN_EQUALS = 5
DEVPROP_OPERATOR_LESS_THAN_EQUALS = 6
DEVPROP_OPERATOR_EQUALS_IGNORE_CASE = 131074
DEVPROP_OPERATOR_NOT_EQUALS_IGNORE_CASE = 196610
DEVPROP_OPERATOR_BITWISE_AND = 7
DEVPROP_OPERATOR_BITWISE_OR = 8
DEVPROP_OPERATOR_BEGINS_WITH = 9
DEVPROP_OPERATOR_ENDS_WITH = 10
DEVPROP_OPERATOR_CONTAINS = 11
DEVPROP_OPERATOR_BEGINS_WITH_IGNORE_CASE = 131081
DEVPROP_OPERATOR_ENDS_WITH_IGNORE_CASE = 131082
DEVPROP_OPERATOR_CONTAINS_IGNORE_CASE = 131083
DEVPROP_OPERATOR_LIST_CONTAINS = 4096
DEVPROP_OPERATOR_LIST_ELEMENT_BEGINS_WITH = 8192
DEVPROP_OPERATOR_LIST_ELEMENT_ENDS_WITH = 12288
DEVPROP_OPERATOR_LIST_ELEMENT_CONTAINS = 16384
DEVPROP_OPERATOR_LIST_CONTAINS_IGNORE_CASE = 135168
DEVPROP_OPERATOR_LIST_ELEMENT_BEGINS_WITH_IGNORE_CASE = 139264
DEVPROP_OPERATOR_LIST_ELEMENT_ENDS_WITH_IGNORE_CASE = 143360
DEVPROP_OPERATOR_LIST_ELEMENT_CONTAINS_IGNORE_CASE = 147456
DEVPROP_OPERATOR_AND_OPEN = 1048576
DEVPROP_OPERATOR_AND_CLOSE = 2097152
DEVPROP_OPERATOR_OR_OPEN = 3145728
DEVPROP_OPERATOR_OR_CLOSE = 4194304
DEVPROP_OPERATOR_NOT_OPEN = 5242880
DEVPROP_OPERATOR_NOT_CLOSE = 6291456
DEVPROP_OPERATOR_ARRAY_CONTAINS = 268435456
DEVPROP_OPERATOR_MASK_EVAL = 4095
DEVPROP_OPERATOR_MASK_LIST = 61440
DEVPROP_OPERATOR_MASK_MODIFIER = 983040
DEVPROP_OPERATOR_MASK_NOT_LOGICAL = 4027580415
DEVPROP_OPERATOR_MASK_LOGICAL = 267386880
DEVPROP_OPERATOR_MASK_ARRAY = 4026531840
def _define_DEVPROP_FILTER_EXPRESSION_head():
    class DEVPROP_FILTER_EXPRESSION(Structure):
        pass
    return DEVPROP_FILTER_EXPRESSION
def _define_DEVPROP_FILTER_EXPRESSION():
    DEVPROP_FILTER_EXPRESSION = win32more.Devices.DeviceQuery.DEVPROP_FILTER_EXPRESSION_head
    DEVPROP_FILTER_EXPRESSION._fields_ = [
        ("Operator", win32more.Devices.DeviceQuery.DEVPROP_OPERATOR),
        ("Property", win32more.Devices.Properties.DEVPROPERTY),
    ]
    return DEVPROP_FILTER_EXPRESSION
DEV_OBJECT_TYPE = Int32
DEV_OBJECT_TYPE_DevObjectTypeUnknown = 0
DEV_OBJECT_TYPE_DevObjectTypeDeviceInterface = 1
DEV_OBJECT_TYPE_DevObjectTypeDeviceContainer = 2
DEV_OBJECT_TYPE_DevObjectTypeDevice = 3
DEV_OBJECT_TYPE_DevObjectTypeDeviceInterfaceClass = 4
DEV_OBJECT_TYPE_DevObjectTypeAEP = 5
DEV_OBJECT_TYPE_DevObjectTypeAEPContainer = 6
DEV_OBJECT_TYPE_DevObjectTypeDeviceInstallerClass = 7
DEV_OBJECT_TYPE_DevObjectTypeDeviceInterfaceDisplay = 8
DEV_OBJECT_TYPE_DevObjectTypeDeviceContainerDisplay = 9
DEV_OBJECT_TYPE_DevObjectTypeAEPService = 10
DEV_OBJECT_TYPE_DevObjectTypeDevicePanel = 11
DEV_QUERY_FLAGS = Int32
DEV_QUERY_FLAGS_DevQueryFlagNone = 0
DEV_QUERY_FLAGS_DevQueryFlagUpdateResults = 1
DEV_QUERY_FLAGS_DevQueryFlagAllProperties = 2
DEV_QUERY_FLAGS_DevQueryFlagLocalize = 4
DEV_QUERY_FLAGS_DevQueryFlagAsyncClose = 8
DEV_QUERY_STATE = Int32
DEV_QUERY_STATE_DevQueryStateInitialized = 0
DEV_QUERY_STATE_DevQueryStateEnumCompleted = 1
DEV_QUERY_STATE_DevQueryStateAborted = 2
DEV_QUERY_STATE_DevQueryStateClosed = 3
DEV_QUERY_RESULT_ACTION = Int32
DEV_QUERY_RESULT_ACTION_DevQueryResultStateChange = 0
DEV_QUERY_RESULT_ACTION_DevQueryResultAdd = 1
DEV_QUERY_RESULT_ACTION_DevQueryResultUpdate = 2
DEV_QUERY_RESULT_ACTION_DevQueryResultRemove = 3
def _define_DEV_OBJECT_head():
    class DEV_OBJECT(Structure):
        pass
    return DEV_OBJECT
def _define_DEV_OBJECT():
    DEV_OBJECT = win32more.Devices.DeviceQuery.DEV_OBJECT_head
    DEV_OBJECT._fields_ = [
        ("ObjectType", win32more.Devices.DeviceQuery.DEV_OBJECT_TYPE),
        ("pszObjectId", win32more.Foundation.PWSTR),
        ("cPropertyCount", UInt32),
        ("pProperties", POINTER(win32more.Devices.Properties.DEVPROPERTY_head)),
    ]
    return DEV_OBJECT
def _define_DEV_QUERY_RESULT_ACTION_DATA_head():
    class DEV_QUERY_RESULT_ACTION_DATA(Structure):
        pass
    return DEV_QUERY_RESULT_ACTION_DATA
def _define_DEV_QUERY_RESULT_ACTION_DATA():
    DEV_QUERY_RESULT_ACTION_DATA = win32more.Devices.DeviceQuery.DEV_QUERY_RESULT_ACTION_DATA_head
    class DEV_QUERY_RESULT_ACTION_DATA__DEV_QUERY_RESULT_UPDATE_PAYLOAD(Union):
        pass
    DEV_QUERY_RESULT_ACTION_DATA__DEV_QUERY_RESULT_UPDATE_PAYLOAD._fields_ = [
        ("State", win32more.Devices.DeviceQuery.DEV_QUERY_STATE),
        ("DeviceObject", win32more.Devices.DeviceQuery.DEV_OBJECT),
    ]
    DEV_QUERY_RESULT_ACTION_DATA._fields_ = [
        ("Action", win32more.Devices.DeviceQuery.DEV_QUERY_RESULT_ACTION),
        ("Data", DEV_QUERY_RESULT_ACTION_DATA__DEV_QUERY_RESULT_UPDATE_PAYLOAD),
    ]
    return DEV_QUERY_RESULT_ACTION_DATA
def _define_DEV_QUERY_PARAMETER_head():
    class DEV_QUERY_PARAMETER(Structure):
        pass
    return DEV_QUERY_PARAMETER
def _define_DEV_QUERY_PARAMETER():
    DEV_QUERY_PARAMETER = win32more.Devices.DeviceQuery.DEV_QUERY_PARAMETER_head
    DEV_QUERY_PARAMETER._fields_ = [
        ("Key", win32more.Devices.Properties.DEVPROPKEY),
        ("Type", UInt32),
        ("BufferSize", UInt32),
        ("Buffer", c_void_p),
    ]
    return DEV_QUERY_PARAMETER
def _define_HDEVQUERY___head():
    class HDEVQUERY__(Structure):
        pass
    return HDEVQUERY__
def _define_HDEVQUERY__():
    HDEVQUERY__ = win32more.Devices.DeviceQuery.HDEVQUERY___head
    HDEVQUERY__._fields_ = [
        ("unused", Int32),
    ]
    return HDEVQUERY__
def _define_PDEV_QUERY_RESULT_CALLBACK():
    return CFUNCTYPE(Void,POINTER(win32more.Devices.DeviceQuery.HDEVQUERY___head),c_void_p,POINTER(win32more.Devices.DeviceQuery.DEV_QUERY_RESULT_ACTION_DATA_head), use_last_error=False)
def _define_DevCreateObjectQuery():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.DeviceQuery.DEV_OBJECT_TYPE,UInt32,UInt32,POINTER(win32more.Devices.Properties.DEVPROPCOMPKEY),UInt32,POINTER(win32more.Devices.DeviceQuery.DEVPROP_FILTER_EXPRESSION),win32more.Devices.DeviceQuery.PDEV_QUERY_RESULT_CALLBACK,c_void_p,POINTER(POINTER(win32more.Devices.DeviceQuery.HDEVQUERY___head)), use_last_error=False)(("DevCreateObjectQuery", windll["api-ms-win-devices-query-l1-1-0"]), ((1, 'ObjectType'),(1, 'QueryFlags'),(1, 'cRequestedProperties'),(1, 'pRequestedProperties'),(1, 'cFilterExpressionCount'),(1, 'pFilter'),(1, 'pCallback'),(1, 'pContext'),(1, 'phDevQuery'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DevCreateObjectQueryEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.DeviceQuery.DEV_OBJECT_TYPE,UInt32,UInt32,POINTER(win32more.Devices.Properties.DEVPROPCOMPKEY),UInt32,POINTER(win32more.Devices.DeviceQuery.DEVPROP_FILTER_EXPRESSION),UInt32,POINTER(win32more.Devices.DeviceQuery.DEV_QUERY_PARAMETER),win32more.Devices.DeviceQuery.PDEV_QUERY_RESULT_CALLBACK,c_void_p,POINTER(POINTER(win32more.Devices.DeviceQuery.HDEVQUERY___head)), use_last_error=False)(("DevCreateObjectQueryEx", windll["api-ms-win-devices-query-l1-1-1"]), ((1, 'ObjectType'),(1, 'QueryFlags'),(1, 'cRequestedProperties'),(1, 'pRequestedProperties'),(1, 'cFilterExpressionCount'),(1, 'pFilter'),(1, 'cExtendedParameterCount'),(1, 'pExtendedParameters'),(1, 'pCallback'),(1, 'pContext'),(1, 'phDevQuery'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DevCreateObjectQueryFromId():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.DeviceQuery.DEV_OBJECT_TYPE,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.Devices.Properties.DEVPROPCOMPKEY),UInt32,POINTER(win32more.Devices.DeviceQuery.DEVPROP_FILTER_EXPRESSION),win32more.Devices.DeviceQuery.PDEV_QUERY_RESULT_CALLBACK,c_void_p,POINTER(POINTER(win32more.Devices.DeviceQuery.HDEVQUERY___head)), use_last_error=False)(("DevCreateObjectQueryFromId", windll["api-ms-win-devices-query-l1-1-0"]), ((1, 'ObjectType'),(1, 'pszObjectId'),(1, 'QueryFlags'),(1, 'cRequestedProperties'),(1, 'pRequestedProperties'),(1, 'cFilterExpressionCount'),(1, 'pFilter'),(1, 'pCallback'),(1, 'pContext'),(1, 'phDevQuery'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DevCreateObjectQueryFromIdEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.DeviceQuery.DEV_OBJECT_TYPE,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.Devices.Properties.DEVPROPCOMPKEY),UInt32,POINTER(win32more.Devices.DeviceQuery.DEVPROP_FILTER_EXPRESSION),UInt32,POINTER(win32more.Devices.DeviceQuery.DEV_QUERY_PARAMETER),win32more.Devices.DeviceQuery.PDEV_QUERY_RESULT_CALLBACK,c_void_p,POINTER(POINTER(win32more.Devices.DeviceQuery.HDEVQUERY___head)), use_last_error=False)(("DevCreateObjectQueryFromIdEx", windll["api-ms-win-devices-query-l1-1-1"]), ((1, 'ObjectType'),(1, 'pszObjectId'),(1, 'QueryFlags'),(1, 'cRequestedProperties'),(1, 'pRequestedProperties'),(1, 'cFilterExpressionCount'),(1, 'pFilter'),(1, 'cExtendedParameterCount'),(1, 'pExtendedParameters'),(1, 'pCallback'),(1, 'pContext'),(1, 'phDevQuery'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DevCreateObjectQueryFromIds():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.DeviceQuery.DEV_OBJECT_TYPE,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.Devices.Properties.DEVPROPCOMPKEY),UInt32,POINTER(win32more.Devices.DeviceQuery.DEVPROP_FILTER_EXPRESSION),win32more.Devices.DeviceQuery.PDEV_QUERY_RESULT_CALLBACK,c_void_p,POINTER(POINTER(win32more.Devices.DeviceQuery.HDEVQUERY___head)), use_last_error=False)(("DevCreateObjectQueryFromIds", windll["api-ms-win-devices-query-l1-1-0"]), ((1, 'ObjectType'),(1, 'pszzObjectIds'),(1, 'QueryFlags'),(1, 'cRequestedProperties'),(1, 'pRequestedProperties'),(1, 'cFilterExpressionCount'),(1, 'pFilter'),(1, 'pCallback'),(1, 'pContext'),(1, 'phDevQuery'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DevCreateObjectQueryFromIdsEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.DeviceQuery.DEV_OBJECT_TYPE,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.Devices.Properties.DEVPROPCOMPKEY),UInt32,POINTER(win32more.Devices.DeviceQuery.DEVPROP_FILTER_EXPRESSION),UInt32,POINTER(win32more.Devices.DeviceQuery.DEV_QUERY_PARAMETER),win32more.Devices.DeviceQuery.PDEV_QUERY_RESULT_CALLBACK,c_void_p,POINTER(POINTER(win32more.Devices.DeviceQuery.HDEVQUERY___head)), use_last_error=False)(("DevCreateObjectQueryFromIdsEx", windll["api-ms-win-devices-query-l1-1-1"]), ((1, 'ObjectType'),(1, 'pszzObjectIds'),(1, 'QueryFlags'),(1, 'cRequestedProperties'),(1, 'pRequestedProperties'),(1, 'cFilterExpressionCount'),(1, 'pFilter'),(1, 'cExtendedParameterCount'),(1, 'pExtendedParameters'),(1, 'pCallback'),(1, 'pContext'),(1, 'phDevQuery'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DevCloseObjectQuery():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Devices.DeviceQuery.HDEVQUERY___head), use_last_error=False)(("DevCloseObjectQuery", windll["api-ms-win-devices-query-l1-1-0"]), ((1, 'hDevQuery'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DevGetObjects():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.DeviceQuery.DEV_OBJECT_TYPE,UInt32,UInt32,POINTER(win32more.Devices.Properties.DEVPROPCOMPKEY),UInt32,POINTER(win32more.Devices.DeviceQuery.DEVPROP_FILTER_EXPRESSION),POINTER(UInt32),POINTER(POINTER(win32more.Devices.DeviceQuery.DEV_OBJECT_head)), use_last_error=False)(("DevGetObjects", windll["api-ms-win-devices-query-l1-1-0"]), ((1, 'ObjectType'),(1, 'QueryFlags'),(1, 'cRequestedProperties'),(1, 'pRequestedProperties'),(1, 'cFilterExpressionCount'),(1, 'pFilter'),(1, 'pcObjectCount'),(1, 'ppObjects'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DevGetObjectsEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.DeviceQuery.DEV_OBJECT_TYPE,UInt32,UInt32,POINTER(win32more.Devices.Properties.DEVPROPCOMPKEY),UInt32,POINTER(win32more.Devices.DeviceQuery.DEVPROP_FILTER_EXPRESSION),UInt32,POINTER(win32more.Devices.DeviceQuery.DEV_QUERY_PARAMETER),POINTER(UInt32),POINTER(POINTER(win32more.Devices.DeviceQuery.DEV_OBJECT_head)), use_last_error=False)(("DevGetObjectsEx", windll["api-ms-win-devices-query-l1-1-1"]), ((1, 'ObjectType'),(1, 'QueryFlags'),(1, 'cRequestedProperties'),(1, 'pRequestedProperties'),(1, 'cFilterExpressionCount'),(1, 'pFilter'),(1, 'cExtendedParameterCount'),(1, 'pExtendedParameters'),(1, 'pcObjectCount'),(1, 'ppObjects'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DevFreeObjects():
    try:
        return WINFUNCTYPE(Void,UInt32,POINTER(win32more.Devices.DeviceQuery.DEV_OBJECT), use_last_error=False)(("DevFreeObjects", windll["api-ms-win-devices-query-l1-1-0"]), ((1, 'cObjectCount'),(1, 'pObjects'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DevGetObjectProperties():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.DeviceQuery.DEV_OBJECT_TYPE,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.Devices.Properties.DEVPROPCOMPKEY),POINTER(UInt32),POINTER(POINTER(win32more.Devices.Properties.DEVPROPERTY_head)), use_last_error=False)(("DevGetObjectProperties", windll["api-ms-win-devices-query-l1-1-0"]), ((1, 'ObjectType'),(1, 'pszObjectId'),(1, 'QueryFlags'),(1, 'cRequestedProperties'),(1, 'pRequestedProperties'),(1, 'pcPropertyCount'),(1, 'ppProperties'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DevGetObjectPropertiesEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.DeviceQuery.DEV_OBJECT_TYPE,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.Devices.Properties.DEVPROPCOMPKEY),UInt32,POINTER(win32more.Devices.DeviceQuery.DEV_QUERY_PARAMETER),POINTER(UInt32),POINTER(POINTER(win32more.Devices.Properties.DEVPROPERTY_head)), use_last_error=False)(("DevGetObjectPropertiesEx", windll["api-ms-win-devices-query-l1-1-1"]), ((1, 'ObjectType'),(1, 'pszObjectId'),(1, 'QueryFlags'),(1, 'cRequestedProperties'),(1, 'pRequestedProperties'),(1, 'cExtendedParameterCount'),(1, 'pExtendedParameters'),(1, 'pcPropertyCount'),(1, 'ppProperties'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DevFreeObjectProperties():
    try:
        return WINFUNCTYPE(Void,UInt32,POINTER(win32more.Devices.Properties.DEVPROPERTY), use_last_error=False)(("DevFreeObjectProperties", windll["api-ms-win-devices-query-l1-1-0"]), ((1, 'cPropertyCount'),(1, 'pProperties'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DevFindProperty():
    try:
        return WINFUNCTYPE(POINTER(win32more.Devices.Properties.DEVPROPERTY_head),POINTER(win32more.Devices.Properties.DEVPROPKEY_head),win32more.Devices.Properties.DEVPROPSTORE,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Devices.Properties.DEVPROPERTY), use_last_error=False)(("DevFindProperty", windll["api-ms-win-devices-query-l1-1-0"]), ((1, 'pKey'),(1, 'Store'),(1, 'pszLocaleName'),(1, 'cProperties'),(1, 'pProperties'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "DEVPROP_OPERATOR",
    "DEVPROP_OPERATOR_MODIFIER_NOT",
    "DEVPROP_OPERATOR_MODIFIER_IGNORE_CASE",
    "DEVPROP_OPERATOR_NONE",
    "DEVPROP_OPERATOR_EXISTS",
    "DEVPROP_OPERATOR_NOT_EXISTS",
    "DEVPROP_OPERATOR_EQUALS",
    "DEVPROP_OPERATOR_NOT_EQUALS",
    "DEVPROP_OPERATOR_GREATER_THAN",
    "DEVPROP_OPERATOR_LESS_THAN",
    "DEVPROP_OPERATOR_GREATER_THAN_EQUALS",
    "DEVPROP_OPERATOR_LESS_THAN_EQUALS",
    "DEVPROP_OPERATOR_EQUALS_IGNORE_CASE",
    "DEVPROP_OPERATOR_NOT_EQUALS_IGNORE_CASE",
    "DEVPROP_OPERATOR_BITWISE_AND",
    "DEVPROP_OPERATOR_BITWISE_OR",
    "DEVPROP_OPERATOR_BEGINS_WITH",
    "DEVPROP_OPERATOR_ENDS_WITH",
    "DEVPROP_OPERATOR_CONTAINS",
    "DEVPROP_OPERATOR_BEGINS_WITH_IGNORE_CASE",
    "DEVPROP_OPERATOR_ENDS_WITH_IGNORE_CASE",
    "DEVPROP_OPERATOR_CONTAINS_IGNORE_CASE",
    "DEVPROP_OPERATOR_LIST_CONTAINS",
    "DEVPROP_OPERATOR_LIST_ELEMENT_BEGINS_WITH",
    "DEVPROP_OPERATOR_LIST_ELEMENT_ENDS_WITH",
    "DEVPROP_OPERATOR_LIST_ELEMENT_CONTAINS",
    "DEVPROP_OPERATOR_LIST_CONTAINS_IGNORE_CASE",
    "DEVPROP_OPERATOR_LIST_ELEMENT_BEGINS_WITH_IGNORE_CASE",
    "DEVPROP_OPERATOR_LIST_ELEMENT_ENDS_WITH_IGNORE_CASE",
    "DEVPROP_OPERATOR_LIST_ELEMENT_CONTAINS_IGNORE_CASE",
    "DEVPROP_OPERATOR_AND_OPEN",
    "DEVPROP_OPERATOR_AND_CLOSE",
    "DEVPROP_OPERATOR_OR_OPEN",
    "DEVPROP_OPERATOR_OR_CLOSE",
    "DEVPROP_OPERATOR_NOT_OPEN",
    "DEVPROP_OPERATOR_NOT_CLOSE",
    "DEVPROP_OPERATOR_ARRAY_CONTAINS",
    "DEVPROP_OPERATOR_MASK_EVAL",
    "DEVPROP_OPERATOR_MASK_LIST",
    "DEVPROP_OPERATOR_MASK_MODIFIER",
    "DEVPROP_OPERATOR_MASK_NOT_LOGICAL",
    "DEVPROP_OPERATOR_MASK_LOGICAL",
    "DEVPROP_OPERATOR_MASK_ARRAY",
    "DEVPROP_FILTER_EXPRESSION",
    "DEV_OBJECT_TYPE",
    "DEV_OBJECT_TYPE_DevObjectTypeUnknown",
    "DEV_OBJECT_TYPE_DevObjectTypeDeviceInterface",
    "DEV_OBJECT_TYPE_DevObjectTypeDeviceContainer",
    "DEV_OBJECT_TYPE_DevObjectTypeDevice",
    "DEV_OBJECT_TYPE_DevObjectTypeDeviceInterfaceClass",
    "DEV_OBJECT_TYPE_DevObjectTypeAEP",
    "DEV_OBJECT_TYPE_DevObjectTypeAEPContainer",
    "DEV_OBJECT_TYPE_DevObjectTypeDeviceInstallerClass",
    "DEV_OBJECT_TYPE_DevObjectTypeDeviceInterfaceDisplay",
    "DEV_OBJECT_TYPE_DevObjectTypeDeviceContainerDisplay",
    "DEV_OBJECT_TYPE_DevObjectTypeAEPService",
    "DEV_OBJECT_TYPE_DevObjectTypeDevicePanel",
    "DEV_QUERY_FLAGS",
    "DEV_QUERY_FLAGS_DevQueryFlagNone",
    "DEV_QUERY_FLAGS_DevQueryFlagUpdateResults",
    "DEV_QUERY_FLAGS_DevQueryFlagAllProperties",
    "DEV_QUERY_FLAGS_DevQueryFlagLocalize",
    "DEV_QUERY_FLAGS_DevQueryFlagAsyncClose",
    "DEV_QUERY_STATE",
    "DEV_QUERY_STATE_DevQueryStateInitialized",
    "DEV_QUERY_STATE_DevQueryStateEnumCompleted",
    "DEV_QUERY_STATE_DevQueryStateAborted",
    "DEV_QUERY_STATE_DevQueryStateClosed",
    "DEV_QUERY_RESULT_ACTION",
    "DEV_QUERY_RESULT_ACTION_DevQueryResultStateChange",
    "DEV_QUERY_RESULT_ACTION_DevQueryResultAdd",
    "DEV_QUERY_RESULT_ACTION_DevQueryResultUpdate",
    "DEV_QUERY_RESULT_ACTION_DevQueryResultRemove",
    "DEV_OBJECT",
    "DEV_QUERY_RESULT_ACTION_DATA",
    "DEV_QUERY_PARAMETER",
    "HDEVQUERY__",
    "PDEV_QUERY_RESULT_CALLBACK",
    "DevCreateObjectQuery",
    "DevCreateObjectQueryEx",
    "DevCreateObjectQueryFromId",
    "DevCreateObjectQueryFromIdEx",
    "DevCreateObjectQueryFromIds",
    "DevCreateObjectQueryFromIdsEx",
    "DevCloseObjectQuery",
    "DevGetObjects",
    "DevGetObjectsEx",
    "DevFreeObjects",
    "DevGetObjectProperties",
    "DevGetObjectPropertiesEx",
    "DevFreeObjectProperties",
    "DevFindProperty",
]
