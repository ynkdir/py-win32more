from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Devices.DeviceQuery
import win32more.Windows.Win32.Devices.Properties
import win32more.Windows.Win32.Foundation
@winfunctype('api-ms-win-devices-query-l1-1-0.dll')
def DevCreateObjectQuery(ObjectType: win32more.Windows.Win32.Devices.DeviceQuery.DEV_OBJECT_TYPE, QueryFlags: UInt32, cRequestedProperties: UInt32, pRequestedProperties: POINTER(win32more.Windows.Win32.Devices.Properties.DEVPROPCOMPKEY), cFilterExpressionCount: UInt32, pFilter: POINTER(win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_FILTER_EXPRESSION), pCallback: win32more.Windows.Win32.Devices.DeviceQuery.PDEV_QUERY_RESULT_CALLBACK, pContext: VoidPtr, phDevQuery: POINTER(win32more.Windows.Win32.Devices.DeviceQuery.HDEVQUERY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-devices-query-l1-1-1.dll')
def DevCreateObjectQueryEx(ObjectType: win32more.Windows.Win32.Devices.DeviceQuery.DEV_OBJECT_TYPE, QueryFlags: UInt32, cRequestedProperties: UInt32, pRequestedProperties: POINTER(win32more.Windows.Win32.Devices.Properties.DEVPROPCOMPKEY), cFilterExpressionCount: UInt32, pFilter: POINTER(win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_FILTER_EXPRESSION), cExtendedParameterCount: UInt32, pExtendedParameters: POINTER(win32more.Windows.Win32.Devices.DeviceQuery.DEV_QUERY_PARAMETER), pCallback: win32more.Windows.Win32.Devices.DeviceQuery.PDEV_QUERY_RESULT_CALLBACK, pContext: VoidPtr, phDevQuery: POINTER(win32more.Windows.Win32.Devices.DeviceQuery.HDEVQUERY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-devices-query-l1-1-0.dll')
def DevCreateObjectQueryFromId(ObjectType: win32more.Windows.Win32.Devices.DeviceQuery.DEV_OBJECT_TYPE, pszObjectId: win32more.Windows.Win32.Foundation.PWSTR, QueryFlags: UInt32, cRequestedProperties: UInt32, pRequestedProperties: POINTER(win32more.Windows.Win32.Devices.Properties.DEVPROPCOMPKEY), cFilterExpressionCount: UInt32, pFilter: POINTER(win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_FILTER_EXPRESSION), pCallback: win32more.Windows.Win32.Devices.DeviceQuery.PDEV_QUERY_RESULT_CALLBACK, pContext: VoidPtr, phDevQuery: POINTER(win32more.Windows.Win32.Devices.DeviceQuery.HDEVQUERY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-devices-query-l1-1-1.dll')
def DevCreateObjectQueryFromIdEx(ObjectType: win32more.Windows.Win32.Devices.DeviceQuery.DEV_OBJECT_TYPE, pszObjectId: win32more.Windows.Win32.Foundation.PWSTR, QueryFlags: UInt32, cRequestedProperties: UInt32, pRequestedProperties: POINTER(win32more.Windows.Win32.Devices.Properties.DEVPROPCOMPKEY), cFilterExpressionCount: UInt32, pFilter: POINTER(win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_FILTER_EXPRESSION), cExtendedParameterCount: UInt32, pExtendedParameters: POINTER(win32more.Windows.Win32.Devices.DeviceQuery.DEV_QUERY_PARAMETER), pCallback: win32more.Windows.Win32.Devices.DeviceQuery.PDEV_QUERY_RESULT_CALLBACK, pContext: VoidPtr, phDevQuery: POINTER(win32more.Windows.Win32.Devices.DeviceQuery.HDEVQUERY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-devices-query-l1-1-0.dll')
def DevCreateObjectQueryFromIds(ObjectType: win32more.Windows.Win32.Devices.DeviceQuery.DEV_OBJECT_TYPE, pszzObjectIds: win32more.Windows.Win32.Foundation.PWSTR, QueryFlags: UInt32, cRequestedProperties: UInt32, pRequestedProperties: POINTER(win32more.Windows.Win32.Devices.Properties.DEVPROPCOMPKEY), cFilterExpressionCount: UInt32, pFilter: POINTER(win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_FILTER_EXPRESSION), pCallback: win32more.Windows.Win32.Devices.DeviceQuery.PDEV_QUERY_RESULT_CALLBACK, pContext: VoidPtr, phDevQuery: POINTER(win32more.Windows.Win32.Devices.DeviceQuery.HDEVQUERY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-devices-query-l1-1-1.dll')
def DevCreateObjectQueryFromIdsEx(ObjectType: win32more.Windows.Win32.Devices.DeviceQuery.DEV_OBJECT_TYPE, pszzObjectIds: win32more.Windows.Win32.Foundation.PWSTR, QueryFlags: UInt32, cRequestedProperties: UInt32, pRequestedProperties: POINTER(win32more.Windows.Win32.Devices.Properties.DEVPROPCOMPKEY), cFilterExpressionCount: UInt32, pFilter: POINTER(win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_FILTER_EXPRESSION), cExtendedParameterCount: UInt32, pExtendedParameters: POINTER(win32more.Windows.Win32.Devices.DeviceQuery.DEV_QUERY_PARAMETER), pCallback: win32more.Windows.Win32.Devices.DeviceQuery.PDEV_QUERY_RESULT_CALLBACK, pContext: VoidPtr, phDevQuery: POINTER(win32more.Windows.Win32.Devices.DeviceQuery.HDEVQUERY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-devices-query-l1-1-0.dll')
def DevCloseObjectQuery(hDevQuery: win32more.Windows.Win32.Devices.DeviceQuery.HDEVQUERY) -> Void: ...
@winfunctype('api-ms-win-devices-query-l1-1-0.dll')
def DevGetObjects(ObjectType: win32more.Windows.Win32.Devices.DeviceQuery.DEV_OBJECT_TYPE, QueryFlags: UInt32, cRequestedProperties: UInt32, pRequestedProperties: POINTER(win32more.Windows.Win32.Devices.Properties.DEVPROPCOMPKEY), cFilterExpressionCount: UInt32, pFilter: POINTER(win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_FILTER_EXPRESSION), pcObjectCount: POINTER(UInt32), ppObjects: POINTER(POINTER(win32more.Windows.Win32.Devices.DeviceQuery.DEV_OBJECT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-devices-query-l1-1-1.dll')
def DevGetObjectsEx(ObjectType: win32more.Windows.Win32.Devices.DeviceQuery.DEV_OBJECT_TYPE, QueryFlags: UInt32, cRequestedProperties: UInt32, pRequestedProperties: POINTER(win32more.Windows.Win32.Devices.Properties.DEVPROPCOMPKEY), cFilterExpressionCount: UInt32, pFilter: POINTER(win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_FILTER_EXPRESSION), cExtendedParameterCount: UInt32, pExtendedParameters: POINTER(win32more.Windows.Win32.Devices.DeviceQuery.DEV_QUERY_PARAMETER), pcObjectCount: POINTER(UInt32), ppObjects: POINTER(POINTER(win32more.Windows.Win32.Devices.DeviceQuery.DEV_OBJECT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-devices-query-l1-1-0.dll')
def DevFreeObjects(cObjectCount: UInt32, pObjects: POINTER(win32more.Windows.Win32.Devices.DeviceQuery.DEV_OBJECT)) -> Void: ...
@winfunctype('api-ms-win-devices-query-l1-1-0.dll')
def DevGetObjectProperties(ObjectType: win32more.Windows.Win32.Devices.DeviceQuery.DEV_OBJECT_TYPE, pszObjectId: win32more.Windows.Win32.Foundation.PWSTR, QueryFlags: UInt32, cRequestedProperties: UInt32, pRequestedProperties: POINTER(win32more.Windows.Win32.Devices.Properties.DEVPROPCOMPKEY), pcPropertyCount: POINTER(UInt32), ppProperties: POINTER(POINTER(win32more.Windows.Win32.Devices.Properties.DEVPROPERTY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-devices-query-l1-1-1.dll')
def DevGetObjectPropertiesEx(ObjectType: win32more.Windows.Win32.Devices.DeviceQuery.DEV_OBJECT_TYPE, pszObjectId: win32more.Windows.Win32.Foundation.PWSTR, QueryFlags: UInt32, cRequestedProperties: UInt32, pRequestedProperties: POINTER(win32more.Windows.Win32.Devices.Properties.DEVPROPCOMPKEY), cExtendedParameterCount: UInt32, pExtendedParameters: POINTER(win32more.Windows.Win32.Devices.DeviceQuery.DEV_QUERY_PARAMETER), pcPropertyCount: POINTER(UInt32), ppProperties: POINTER(POINTER(win32more.Windows.Win32.Devices.Properties.DEVPROPERTY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-devices-query-l1-1-0.dll')
def DevFreeObjectProperties(cPropertyCount: UInt32, pProperties: POINTER(win32more.Windows.Win32.Devices.Properties.DEVPROPERTY)) -> Void: ...
@winfunctype('api-ms-win-devices-query-l1-1-0.dll')
def DevFindProperty(pKey: POINTER(win32more.Windows.Win32.Foundation.DEVPROPKEY), Store: win32more.Windows.Win32.Devices.Properties.DEVPROPSTORE, pszLocaleName: win32more.Windows.Win32.Foundation.PWSTR, cProperties: UInt32, pProperties: POINTER(win32more.Windows.Win32.Devices.Properties.DEVPROPERTY)) -> POINTER(win32more.Windows.Win32.Devices.Properties.DEVPROPERTY): ...
class DEVPROP_FILTER_EXPRESSION(Structure):
    Operator: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR
    Property: win32more.Windows.Win32.Devices.Properties.DEVPROPERTY
DEVPROP_OPERATOR = UInt32
DEVPROP_OPERATOR_MODIFIER_NOT: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 65536
DEVPROP_OPERATOR_MODIFIER_IGNORE_CASE: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 131072
DEVPROP_OPERATOR_NONE: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 0
DEVPROP_OPERATOR_EXISTS: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 1
DEVPROP_OPERATOR_NOT_EXISTS: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 65537
DEVPROP_OPERATOR_EQUALS: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 2
DEVPROP_OPERATOR_NOT_EQUALS: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 65538
DEVPROP_OPERATOR_GREATER_THAN: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 3
DEVPROP_OPERATOR_LESS_THAN: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 4
DEVPROP_OPERATOR_GREATER_THAN_EQUALS: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 5
DEVPROP_OPERATOR_LESS_THAN_EQUALS: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 6
DEVPROP_OPERATOR_EQUALS_IGNORE_CASE: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 131074
DEVPROP_OPERATOR_NOT_EQUALS_IGNORE_CASE: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 196610
DEVPROP_OPERATOR_BITWISE_AND: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 7
DEVPROP_OPERATOR_BITWISE_OR: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 8
DEVPROP_OPERATOR_BEGINS_WITH: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 9
DEVPROP_OPERATOR_ENDS_WITH: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 10
DEVPROP_OPERATOR_CONTAINS: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 11
DEVPROP_OPERATOR_BEGINS_WITH_IGNORE_CASE: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 131081
DEVPROP_OPERATOR_ENDS_WITH_IGNORE_CASE: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 131082
DEVPROP_OPERATOR_CONTAINS_IGNORE_CASE: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 131083
DEVPROP_OPERATOR_LIST_CONTAINS: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 4096
DEVPROP_OPERATOR_LIST_ELEMENT_BEGINS_WITH: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 8192
DEVPROP_OPERATOR_LIST_ELEMENT_ENDS_WITH: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 12288
DEVPROP_OPERATOR_LIST_ELEMENT_CONTAINS: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 16384
DEVPROP_OPERATOR_LIST_CONTAINS_IGNORE_CASE: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 135168
DEVPROP_OPERATOR_LIST_ELEMENT_BEGINS_WITH_IGNORE_CASE: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 139264
DEVPROP_OPERATOR_LIST_ELEMENT_ENDS_WITH_IGNORE_CASE: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 143360
DEVPROP_OPERATOR_LIST_ELEMENT_CONTAINS_IGNORE_CASE: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 147456
DEVPROP_OPERATOR_AND_OPEN: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 1048576
DEVPROP_OPERATOR_AND_CLOSE: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 2097152
DEVPROP_OPERATOR_OR_OPEN: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 3145728
DEVPROP_OPERATOR_OR_CLOSE: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 4194304
DEVPROP_OPERATOR_NOT_OPEN: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 5242880
DEVPROP_OPERATOR_NOT_CLOSE: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 6291456
DEVPROP_OPERATOR_ARRAY_CONTAINS: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 268435456
DEVPROP_OPERATOR_MASK_EVAL: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 4095
DEVPROP_OPERATOR_MASK_LIST: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 61440
DEVPROP_OPERATOR_MASK_MODIFIER: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 983040
DEVPROP_OPERATOR_MASK_NOT_LOGICAL: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 4027580415
DEVPROP_OPERATOR_MASK_LOGICAL: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 267386880
DEVPROP_OPERATOR_MASK_ARRAY: win32more.Windows.Win32.Devices.DeviceQuery.DEVPROP_OPERATOR = 4026531840
class DEV_OBJECT(Structure):
    ObjectType: win32more.Windows.Win32.Devices.DeviceQuery.DEV_OBJECT_TYPE
    pszObjectId: win32more.Windows.Win32.Foundation.PWSTR
    cPropertyCount: UInt32
    pProperties: POINTER(win32more.Windows.Win32.Devices.Properties.DEVPROPERTY)
DEV_OBJECT_TYPE = Int32
DevObjectTypeUnknown: win32more.Windows.Win32.Devices.DeviceQuery.DEV_OBJECT_TYPE = 0
DevObjectTypeDeviceInterface: win32more.Windows.Win32.Devices.DeviceQuery.DEV_OBJECT_TYPE = 1
DevObjectTypeDeviceContainer: win32more.Windows.Win32.Devices.DeviceQuery.DEV_OBJECT_TYPE = 2
DevObjectTypeDevice: win32more.Windows.Win32.Devices.DeviceQuery.DEV_OBJECT_TYPE = 3
DevObjectTypeDeviceInterfaceClass: win32more.Windows.Win32.Devices.DeviceQuery.DEV_OBJECT_TYPE = 4
DevObjectTypeAEP: win32more.Windows.Win32.Devices.DeviceQuery.DEV_OBJECT_TYPE = 5
DevObjectTypeAEPContainer: win32more.Windows.Win32.Devices.DeviceQuery.DEV_OBJECT_TYPE = 6
DevObjectTypeDeviceInstallerClass: win32more.Windows.Win32.Devices.DeviceQuery.DEV_OBJECT_TYPE = 7
DevObjectTypeDeviceInterfaceDisplay: win32more.Windows.Win32.Devices.DeviceQuery.DEV_OBJECT_TYPE = 8
DevObjectTypeDeviceContainerDisplay: win32more.Windows.Win32.Devices.DeviceQuery.DEV_OBJECT_TYPE = 9
DevObjectTypeAEPService: win32more.Windows.Win32.Devices.DeviceQuery.DEV_OBJECT_TYPE = 10
DevObjectTypeDevicePanel: win32more.Windows.Win32.Devices.DeviceQuery.DEV_OBJECT_TYPE = 11
DEV_QUERY_FLAGS = Int32
DevQueryFlagNone: win32more.Windows.Win32.Devices.DeviceQuery.DEV_QUERY_FLAGS = 0
DevQueryFlagUpdateResults: win32more.Windows.Win32.Devices.DeviceQuery.DEV_QUERY_FLAGS = 1
DevQueryFlagAllProperties: win32more.Windows.Win32.Devices.DeviceQuery.DEV_QUERY_FLAGS = 2
DevQueryFlagLocalize: win32more.Windows.Win32.Devices.DeviceQuery.DEV_QUERY_FLAGS = 4
DevQueryFlagAsyncClose: win32more.Windows.Win32.Devices.DeviceQuery.DEV_QUERY_FLAGS = 8
class DEV_QUERY_PARAMETER(Structure):
    Key: win32more.Windows.Win32.Foundation.DEVPROPKEY
    Type: win32more.Windows.Win32.Devices.Properties.DEVPROPTYPE
    BufferSize: UInt32
    Buffer: VoidPtr
DEV_QUERY_RESULT_ACTION = Int32
DevQueryResultStateChange: win32more.Windows.Win32.Devices.DeviceQuery.DEV_QUERY_RESULT_ACTION = 0
DevQueryResultAdd: win32more.Windows.Win32.Devices.DeviceQuery.DEV_QUERY_RESULT_ACTION = 1
DevQueryResultUpdate: win32more.Windows.Win32.Devices.DeviceQuery.DEV_QUERY_RESULT_ACTION = 2
DevQueryResultRemove: win32more.Windows.Win32.Devices.DeviceQuery.DEV_QUERY_RESULT_ACTION = 3
class DEV_QUERY_RESULT_ACTION_DATA(Structure):
    Action: win32more.Windows.Win32.Devices.DeviceQuery.DEV_QUERY_RESULT_ACTION
    Data: _DEV_QUERY_RESULT_UPDATE_PAYLOAD
    class _DEV_QUERY_RESULT_UPDATE_PAYLOAD(Union):
        State: win32more.Windows.Win32.Devices.DeviceQuery.DEV_QUERY_STATE
        DeviceObject: win32more.Windows.Win32.Devices.DeviceQuery.DEV_OBJECT
DEV_QUERY_STATE = Int32
DevQueryStateInitialized: win32more.Windows.Win32.Devices.DeviceQuery.DEV_QUERY_STATE = 0
DevQueryStateEnumCompleted: win32more.Windows.Win32.Devices.DeviceQuery.DEV_QUERY_STATE = 1
DevQueryStateAborted: win32more.Windows.Win32.Devices.DeviceQuery.DEV_QUERY_STATE = 2
DevQueryStateClosed: win32more.Windows.Win32.Devices.DeviceQuery.DEV_QUERY_STATE = 3
HDEVQUERY = VoidPtr
@winfunctype_pointer
def PDEV_QUERY_RESULT_CALLBACK(hDevQuery: win32more.Windows.Win32.Devices.DeviceQuery.HDEVQUERY, pContext: VoidPtr, pActionData: POINTER(win32more.Windows.Win32.Devices.DeviceQuery.DEV_QUERY_RESULT_ACTION_DATA)) -> Void: ...


make_ready(__name__)
