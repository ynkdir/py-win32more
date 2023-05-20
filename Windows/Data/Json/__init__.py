from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.Data.Json
import Windows.Foundation
import Windows.Foundation.Collections
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IJsonArray(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Json.IJsonArray'
    _iid_ = Guid('{08c1ddb6-0cbd-4a9a-b5d3-2f852dc37e81}')
    @winrt_commethod(6)
    def GetObjectAt(self, index: UInt32) -> Windows.Data.Json.JsonObject: ...
    @winrt_commethod(7)
    def GetArrayAt(self, index: UInt32) -> Windows.Data.Json.JsonArray: ...
    @winrt_commethod(8)
    def GetStringAt(self, index: UInt32) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetNumberAt(self, index: UInt32) -> Double: ...
    @winrt_commethod(10)
    def GetBooleanAt(self, index: UInt32) -> Boolean: ...
class IJsonArrayStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Json.IJsonArrayStatics'
    _iid_ = Guid('{db1434a9-e164-499f-93e2-8a8f49bb90ba}')
    @winrt_commethod(6)
    def Parse(self, input: WinRT_String) -> Windows.Data.Json.JsonArray: ...
    @winrt_commethod(7)
    def TryParse(self, input: WinRT_String, result: POINTER(Windows.Data.Json.JsonArray)) -> Boolean: ...
class IJsonErrorStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Json.IJsonErrorStatics2'
    _iid_ = Guid('{404030da-87d0-436c-83ab-fc7b12c0cc26}')
    @winrt_commethod(6)
    def GetJsonStatus(self, hresult: Int32) -> Windows.Data.Json.JsonErrorStatus: ...
class IJsonObject(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Json.IJsonObject'
    _iid_ = Guid('{064e24dd-29c2-4f83-9ac1-9ee11578beb3}')
    @winrt_commethod(6)
    def GetNamedValue(self, name: WinRT_String) -> Windows.Data.Json.JsonValue: ...
    @winrt_commethod(7)
    def SetNamedValue(self, name: WinRT_String, value: Windows.Data.Json.IJsonValue) -> Void: ...
    @winrt_commethod(8)
    def GetNamedObject(self, name: WinRT_String) -> Windows.Data.Json.JsonObject: ...
    @winrt_commethod(9)
    def GetNamedArray(self, name: WinRT_String) -> Windows.Data.Json.JsonArray: ...
    @winrt_commethod(10)
    def GetNamedString(self, name: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(11)
    def GetNamedNumber(self, name: WinRT_String) -> Double: ...
    @winrt_commethod(12)
    def GetNamedBoolean(self, name: WinRT_String) -> Boolean: ...
class IJsonObjectStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Json.IJsonObjectStatics'
    _iid_ = Guid('{2289f159-54de-45d8-abcc-22603fa066a0}')
    @winrt_commethod(6)
    def Parse(self, input: WinRT_String) -> Windows.Data.Json.JsonObject: ...
    @winrt_commethod(7)
    def TryParse(self, input: WinRT_String, result: POINTER(Windows.Data.Json.JsonObject)) -> Boolean: ...
class IJsonObjectWithDefaultValues(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Json.IJsonObjectWithDefaultValues'
    _iid_ = Guid('{d960d2a2-b7f0-4f00-8e44-d82cf415ea13}')
    @winrt_commethod(6)
    def GetNamedValueOrDefault(self, name: WinRT_String, defaultValue: Windows.Data.Json.JsonValue) -> Windows.Data.Json.JsonValue: ...
    @winrt_commethod(7)
    def GetNamedObjectOrDefault(self, name: WinRT_String, defaultValue: Windows.Data.Json.JsonObject) -> Windows.Data.Json.JsonObject: ...
    @winrt_commethod(8)
    def GetNamedStringOrDefault(self, name: WinRT_String, defaultValue: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetNamedArrayOrDefault(self, name: WinRT_String, defaultValue: Windows.Data.Json.JsonArray) -> Windows.Data.Json.JsonArray: ...
    @winrt_commethod(10)
    def GetNamedNumberOrDefault(self, name: WinRT_String, defaultValue: Double) -> Double: ...
    @winrt_commethod(11)
    def GetNamedBooleanOrDefault(self, name: WinRT_String, defaultValue: Boolean) -> Boolean: ...
class IJsonValue(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Json.IJsonValue'
    _iid_ = Guid('{a3219ecb-f0b3-4dcd-beee-19d48cd3ed1e}')
    @winrt_commethod(6)
    def get_ValueType(self) -> Windows.Data.Json.JsonValueType: ...
    @winrt_commethod(7)
    def Stringify(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetString(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetNumber(self) -> Double: ...
    @winrt_commethod(10)
    def GetBoolean(self) -> Boolean: ...
    @winrt_commethod(11)
    def GetArray(self) -> Windows.Data.Json.JsonArray: ...
    @winrt_commethod(12)
    def GetObject(self) -> Windows.Data.Json.JsonObject: ...
    ValueType = property(get_ValueType, None)
class IJsonValueStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Json.IJsonValueStatics'
    _iid_ = Guid('{5f6b544a-2f53-48e1-91a3-f78b50a6345c}')
    @winrt_commethod(6)
    def Parse(self, input: WinRT_String) -> Windows.Data.Json.JsonValue: ...
    @winrt_commethod(7)
    def TryParse(self, input: WinRT_String, result: POINTER(Windows.Data.Json.JsonValue)) -> Boolean: ...
    @winrt_commethod(8)
    def CreateBooleanValue(self, input: Boolean) -> Windows.Data.Json.JsonValue: ...
    @winrt_commethod(9)
    def CreateNumberValue(self, input: Double) -> Windows.Data.Json.JsonValue: ...
    @winrt_commethod(10)
    def CreateStringValue(self, input: WinRT_String) -> Windows.Data.Json.JsonValue: ...
class IJsonValueStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Json.IJsonValueStatics2'
    _iid_ = Guid('{1d9ecbe4-3fe8-4335-8392-93d8e36865f0}')
    @winrt_commethod(6)
    def CreateNullValue(self) -> Windows.Data.Json.JsonValue: ...
class JsonArray(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Data.Json.IJsonArray
    _classid_ = 'Windows.Data.Json.JsonArray'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Data.Json.JsonArray: ...
    @winrt_mixinmethod
    def GetObjectAt(self: Windows.Data.Json.IJsonArray, index: UInt32) -> Windows.Data.Json.JsonObject: ...
    @winrt_mixinmethod
    def GetArrayAt(self: Windows.Data.Json.IJsonArray, index: UInt32) -> Windows.Data.Json.JsonArray: ...
    @winrt_mixinmethod
    def GetStringAt(self: Windows.Data.Json.IJsonArray, index: UInt32) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetNumberAt(self: Windows.Data.Json.IJsonArray, index: UInt32) -> Double: ...
    @winrt_mixinmethod
    def GetBooleanAt(self: Windows.Data.Json.IJsonArray, index: UInt32) -> Boolean: ...
    @winrt_mixinmethod
    def get_ValueType(self: Windows.Data.Json.IJsonValue) -> Windows.Data.Json.JsonValueType: ...
    @winrt_mixinmethod
    def Stringify(self: Windows.Data.Json.IJsonValue) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetString(self: Windows.Data.Json.IJsonValue) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetNumber(self: Windows.Data.Json.IJsonValue) -> Double: ...
    @winrt_mixinmethod
    def GetBoolean(self: Windows.Data.Json.IJsonValue) -> Boolean: ...
    @winrt_mixinmethod
    def GetArray(self: Windows.Data.Json.IJsonValue) -> Windows.Data.Json.JsonArray: ...
    @winrt_mixinmethod
    def GetObject(self: Windows.Data.Json.IJsonValue) -> Windows.Data.Json.JsonObject: ...
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVector[Windows.Data.Json.IJsonValue], index: UInt32) -> Windows.Data.Json.IJsonValue: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVector[Windows.Data.Json.IJsonValue]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IVector[Windows.Data.Json.IJsonValue]) -> Windows.Foundation.Collections.IVectorView[Windows.Data.Json.IJsonValue]: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVector[Windows.Data.Json.IJsonValue], value: Windows.Data.Json.IJsonValue, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: Windows.Foundation.Collections.IVector[Windows.Data.Json.IJsonValue], index: UInt32, value: Windows.Data.Json.IJsonValue) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: Windows.Foundation.Collections.IVector[Windows.Data.Json.IJsonValue], index: UInt32, value: Windows.Data.Json.IJsonValue) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: Windows.Foundation.Collections.IVector[Windows.Data.Json.IJsonValue], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: Windows.Foundation.Collections.IVector[Windows.Data.Json.IJsonValue], value: Windows.Data.Json.IJsonValue) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Foundation.Collections.IVector[Windows.Data.Json.IJsonValue]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IVector[Windows.Data.Json.IJsonValue]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVector[Windows.Data.Json.IJsonValue], startIndex: UInt32, items: Annotated[SZArray[Windows.Data.Json.IJsonValue], 'Out']) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: Windows.Foundation.Collections.IVector[Windows.Data.Json.IJsonValue], items: Annotated[SZArray[Windows.Data.Json.IJsonValue], 'In']) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Data.Json.IJsonValue]) -> Windows.Foundation.Collections.IIterator[Windows.Data.Json.IJsonValue]: ...
    @winrt_mixinmethod
    def ToString(self: Windows.Foundation.IStringable) -> WinRT_String: ...
    @winrt_classmethod
    def Parse(cls: Windows.Data.Json.IJsonArrayStatics, input: WinRT_String) -> Windows.Data.Json.JsonArray: ...
    @winrt_classmethod
    def TryParse(cls: Windows.Data.Json.IJsonArrayStatics, input: WinRT_String, result: POINTER(Windows.Data.Json.JsonArray)) -> Boolean: ...
    ValueType = property(get_ValueType, None)
    Size = property(get_Size, None)
class JsonError(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Json.JsonError'
    @winrt_classmethod
    def GetJsonStatus(cls: Windows.Data.Json.IJsonErrorStatics2, hresult: Int32) -> Windows.Data.Json.JsonErrorStatus: ...
JsonErrorStatus = Int32
JsonErrorStatus_Unknown: JsonErrorStatus = 0
JsonErrorStatus_InvalidJsonString: JsonErrorStatus = 1
JsonErrorStatus_InvalidJsonNumber: JsonErrorStatus = 2
JsonErrorStatus_JsonValueNotFound: JsonErrorStatus = 3
JsonErrorStatus_ImplementationLimit: JsonErrorStatus = 4
class JsonObject(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Data.Json.IJsonObject
    _classid_ = 'Windows.Data.Json.JsonObject'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Data.Json.JsonObject: ...
    @winrt_mixinmethod
    def GetNamedValue(self: Windows.Data.Json.IJsonObject, name: WinRT_String) -> Windows.Data.Json.JsonValue: ...
    @winrt_mixinmethod
    def SetNamedValue(self: Windows.Data.Json.IJsonObject, name: WinRT_String, value: Windows.Data.Json.IJsonValue) -> Void: ...
    @winrt_mixinmethod
    def GetNamedObject(self: Windows.Data.Json.IJsonObject, name: WinRT_String) -> Windows.Data.Json.JsonObject: ...
    @winrt_mixinmethod
    def GetNamedArray(self: Windows.Data.Json.IJsonObject, name: WinRT_String) -> Windows.Data.Json.JsonArray: ...
    @winrt_mixinmethod
    def GetNamedString(self: Windows.Data.Json.IJsonObject, name: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetNamedNumber(self: Windows.Data.Json.IJsonObject, name: WinRT_String) -> Double: ...
    @winrt_mixinmethod
    def GetNamedBoolean(self: Windows.Data.Json.IJsonObject, name: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def get_ValueType(self: Windows.Data.Json.IJsonValue) -> Windows.Data.Json.JsonValueType: ...
    @winrt_mixinmethod
    def Stringify(self: Windows.Data.Json.IJsonValue) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetString(self: Windows.Data.Json.IJsonValue) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetNumber(self: Windows.Data.Json.IJsonValue) -> Double: ...
    @winrt_mixinmethod
    def GetBoolean(self: Windows.Data.Json.IJsonValue) -> Boolean: ...
    @winrt_mixinmethod
    def GetArray(self: Windows.Data.Json.IJsonValue) -> Windows.Data.Json.JsonArray: ...
    @winrt_mixinmethod
    def GetObject(self: Windows.Data.Json.IJsonValue) -> Windows.Data.Json.JsonObject: ...
    @winrt_mixinmethod
    def Lookup(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Data.Json.IJsonValue], key: WinRT_String) -> Windows.Data.Json.IJsonValue: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Data.Json.IJsonValue]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Data.Json.IJsonValue], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Data.Json.IJsonValue]) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Data.Json.IJsonValue]: ...
    @winrt_mixinmethod
    def Insert(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Data.Json.IJsonValue], key: WinRT_String, value: Windows.Data.Json.IJsonValue) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Data.Json.IJsonValue], key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Data.Json.IJsonValue]) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Data.Json.IJsonValue]]) -> Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Data.Json.IJsonValue]]: ...
    @winrt_mixinmethod
    def GetNamedValueOrDefault(self: Windows.Data.Json.IJsonObjectWithDefaultValues, name: WinRT_String, defaultValue: Windows.Data.Json.JsonValue) -> Windows.Data.Json.JsonValue: ...
    @winrt_mixinmethod
    def GetNamedObjectOrDefault(self: Windows.Data.Json.IJsonObjectWithDefaultValues, name: WinRT_String, defaultValue: Windows.Data.Json.JsonObject) -> Windows.Data.Json.JsonObject: ...
    @winrt_mixinmethod
    def GetNamedStringOrDefault(self: Windows.Data.Json.IJsonObjectWithDefaultValues, name: WinRT_String, defaultValue: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetNamedArrayOrDefault(self: Windows.Data.Json.IJsonObjectWithDefaultValues, name: WinRT_String, defaultValue: Windows.Data.Json.JsonArray) -> Windows.Data.Json.JsonArray: ...
    @winrt_mixinmethod
    def GetNamedNumberOrDefault(self: Windows.Data.Json.IJsonObjectWithDefaultValues, name: WinRT_String, defaultValue: Double) -> Double: ...
    @winrt_mixinmethod
    def GetNamedBooleanOrDefault(self: Windows.Data.Json.IJsonObjectWithDefaultValues, name: WinRT_String, defaultValue: Boolean) -> Boolean: ...
    @winrt_mixinmethod
    def ToString(self: Windows.Foundation.IStringable) -> WinRT_String: ...
    @winrt_classmethod
    def Parse(cls: Windows.Data.Json.IJsonObjectStatics, input: WinRT_String) -> Windows.Data.Json.JsonObject: ...
    @winrt_classmethod
    def TryParse(cls: Windows.Data.Json.IJsonObjectStatics, input: WinRT_String, result: POINTER(Windows.Data.Json.JsonObject)) -> Boolean: ...
    ValueType = property(get_ValueType, None)
    Size = property(get_Size, None)
class JsonValue(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Data.Json.IJsonValue
    _classid_ = 'Windows.Data.Json.JsonValue'
    @winrt_mixinmethod
    def get_ValueType(self: Windows.Data.Json.IJsonValue) -> Windows.Data.Json.JsonValueType: ...
    @winrt_mixinmethod
    def Stringify(self: Windows.Data.Json.IJsonValue) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetString(self: Windows.Data.Json.IJsonValue) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetNumber(self: Windows.Data.Json.IJsonValue) -> Double: ...
    @winrt_mixinmethod
    def GetBoolean(self: Windows.Data.Json.IJsonValue) -> Boolean: ...
    @winrt_mixinmethod
    def GetArray(self: Windows.Data.Json.IJsonValue) -> Windows.Data.Json.JsonArray: ...
    @winrt_mixinmethod
    def GetObject(self: Windows.Data.Json.IJsonValue) -> Windows.Data.Json.JsonObject: ...
    @winrt_mixinmethod
    def ToString(self: Windows.Foundation.IStringable) -> WinRT_String: ...
    @winrt_classmethod
    def CreateNullValue(cls: Windows.Data.Json.IJsonValueStatics2) -> Windows.Data.Json.JsonValue: ...
    @winrt_classmethod
    def Parse(cls: Windows.Data.Json.IJsonValueStatics, input: WinRT_String) -> Windows.Data.Json.JsonValue: ...
    @winrt_classmethod
    def TryParse(cls: Windows.Data.Json.IJsonValueStatics, input: WinRT_String, result: POINTER(Windows.Data.Json.JsonValue)) -> Boolean: ...
    @winrt_classmethod
    def CreateBooleanValue(cls: Windows.Data.Json.IJsonValueStatics, input: Boolean) -> Windows.Data.Json.JsonValue: ...
    @winrt_classmethod
    def CreateNumberValue(cls: Windows.Data.Json.IJsonValueStatics, input: Double) -> Windows.Data.Json.JsonValue: ...
    @winrt_classmethod
    def CreateStringValue(cls: Windows.Data.Json.IJsonValueStatics, input: WinRT_String) -> Windows.Data.Json.JsonValue: ...
    ValueType = property(get_ValueType, None)
JsonValueType = Int32
JsonValueType_Null: JsonValueType = 0
JsonValueType_Boolean: JsonValueType = 1
JsonValueType_Number: JsonValueType = 2
JsonValueType_String: JsonValueType = 3
JsonValueType_Array: JsonValueType = 4
JsonValueType_Object: JsonValueType = 5
make_head(_module, 'IJsonArray')
make_head(_module, 'IJsonArrayStatics')
make_head(_module, 'IJsonErrorStatics2')
make_head(_module, 'IJsonObject')
make_head(_module, 'IJsonObjectStatics')
make_head(_module, 'IJsonObjectWithDefaultValues')
make_head(_module, 'IJsonValue')
make_head(_module, 'IJsonValueStatics')
make_head(_module, 'IJsonValueStatics2')
make_head(_module, 'JsonArray')
make_head(_module, 'JsonError')
make_head(_module, 'JsonObject')
make_head(_module, 'JsonValue')
