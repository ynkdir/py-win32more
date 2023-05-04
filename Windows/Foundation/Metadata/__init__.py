from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Foundation.Metadata
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ApiInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    @winrt_classmethod
    def IsTypePresent(cls: Windows.Foundation.Metadata.IApiInformationStatics, typeName: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def IsMethodPresent(cls: Windows.Foundation.Metadata.IApiInformationStatics, typeName: WinRT_String, methodName: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def IsMethodPresentWithArity(cls: Windows.Foundation.Metadata.IApiInformationStatics, typeName: WinRT_String, methodName: WinRT_String, inputParameterCount: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsEventPresent(cls: Windows.Foundation.Metadata.IApiInformationStatics, typeName: WinRT_String, eventName: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def IsPropertyPresent(cls: Windows.Foundation.Metadata.IApiInformationStatics, typeName: WinRT_String, propertyName: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def IsReadOnlyPropertyPresent(cls: Windows.Foundation.Metadata.IApiInformationStatics, typeName: WinRT_String, propertyName: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def IsWriteablePropertyPresent(cls: Windows.Foundation.Metadata.IApiInformationStatics, typeName: WinRT_String, propertyName: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def IsEnumNamedValuePresent(cls: Windows.Foundation.Metadata.IApiInformationStatics, enumTypeName: WinRT_String, valueName: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def IsApiContractPresentByMajor(cls: Windows.Foundation.Metadata.IApiInformationStatics, contractName: WinRT_String, majorVersion: UInt16) -> Boolean: ...
    @winrt_classmethod
    def IsApiContractPresentByMajorAndMinor(cls: Windows.Foundation.Metadata.IApiInformationStatics, contractName: WinRT_String, majorVersion: UInt16, minorVersion: UInt16) -> Boolean: ...
AttributeTargets = UInt32
AttributeTargets_All: AttributeTargets = 4294967295
AttributeTargets_Delegate: AttributeTargets = 1
AttributeTargets_Enum: AttributeTargets = 2
AttributeTargets_Event: AttributeTargets = 4
AttributeTargets_Field: AttributeTargets = 8
AttributeTargets_Interface: AttributeTargets = 16
AttributeTargets_Method: AttributeTargets = 64
AttributeTargets_Parameter: AttributeTargets = 128
AttributeTargets_Property: AttributeTargets = 256
AttributeTargets_RuntimeClass: AttributeTargets = 512
AttributeTargets_Struct: AttributeTargets = 1024
AttributeTargets_InterfaceImpl: AttributeTargets = 2048
AttributeTargets_ApiContract: AttributeTargets = 8192
CompositionType = Int32
CompositionType_Protected: CompositionType = 1
CompositionType_Public: CompositionType = 2
DeprecationType = Int32
DeprecationType_Deprecate: DeprecationType = 0
DeprecationType_Remove: DeprecationType = 1
FeatureStage = Int32
FeatureStage_AlwaysDisabled: FeatureStage = 0
FeatureStage_DisabledByDefault: FeatureStage = 1
FeatureStage_EnabledByDefault: FeatureStage = 2
FeatureStage_AlwaysEnabled: FeatureStage = 3
GCPressureAmount = Int32
GCPressureAmount_Low: GCPressureAmount = 0
GCPressureAmount_Medium: GCPressureAmount = 1
GCPressureAmount_High: GCPressureAmount = 2
class IApiInformationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{997439fe-f681-4a11-b416-c13a47e8ba36}')
    @winrt_commethod(6)
    def IsTypePresent(self, typeName: WinRT_String) -> Boolean: ...
    @winrt_commethod(7)
    def IsMethodPresent(self, typeName: WinRT_String, methodName: WinRT_String) -> Boolean: ...
    @winrt_commethod(8)
    def IsMethodPresentWithArity(self, typeName: WinRT_String, methodName: WinRT_String, inputParameterCount: UInt32) -> Boolean: ...
    @winrt_commethod(9)
    def IsEventPresent(self, typeName: WinRT_String, eventName: WinRT_String) -> Boolean: ...
    @winrt_commethod(10)
    def IsPropertyPresent(self, typeName: WinRT_String, propertyName: WinRT_String) -> Boolean: ...
    @winrt_commethod(11)
    def IsReadOnlyPropertyPresent(self, typeName: WinRT_String, propertyName: WinRT_String) -> Boolean: ...
    @winrt_commethod(12)
    def IsWriteablePropertyPresent(self, typeName: WinRT_String, propertyName: WinRT_String) -> Boolean: ...
    @winrt_commethod(13)
    def IsEnumNamedValuePresent(self, enumTypeName: WinRT_String, valueName: WinRT_String) -> Boolean: ...
    @winrt_commethod(14)
    def IsApiContractPresentByMajor(self, contractName: WinRT_String, majorVersion: UInt16) -> Boolean: ...
    @winrt_commethod(15)
    def IsApiContractPresentByMajorAndMinor(self, contractName: WinRT_String, majorVersion: UInt16, minorVersion: UInt16) -> Boolean: ...
MarshalingType = Int32
MarshalingType_None: MarshalingType = 1
MarshalingType_Agile: MarshalingType = 2
MarshalingType_Standard: MarshalingType = 3
MarshalingType_InvalidMarshaling: MarshalingType = 0
Platform = Int32
Platform_Windows: Platform = 0
Platform_WindowsPhone: Platform = 1
ThreadingModel = Int32
ThreadingModel_STA: ThreadingModel = 1
ThreadingModel_MTA: ThreadingModel = 2
ThreadingModel_Both: ThreadingModel = 3
ThreadingModel_InvalidThreading: ThreadingModel = 0
make_head(_module, 'ApiInformation')
make_head(_module, 'IApiInformationStatics')
