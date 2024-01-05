from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import Annotated, Generic, K, MulticastDelegate, SZArray, T, TProgress, TResult, TSender, V, WinRT_String, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation.Metadata
import win32more.Windows.Win32.System.WinRT
class ApiInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.Metadata.ApiInformation'
    @winrt_classmethod
    def IsTypePresent(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, typeName: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def IsMethodPresent(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, typeName: WinRT_String, methodName: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def IsMethodPresentWithArity(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, typeName: WinRT_String, methodName: WinRT_String, inputParameterCount: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsEventPresent(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, typeName: WinRT_String, eventName: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def IsPropertyPresent(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, typeName: WinRT_String, propertyName: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def IsReadOnlyPropertyPresent(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, typeName: WinRT_String, propertyName: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def IsWriteablePropertyPresent(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, typeName: WinRT_String, propertyName: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def IsEnumNamedValuePresent(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, enumTypeName: WinRT_String, valueName: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def IsApiContractPresentByMajor(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, contractName: WinRT_String, majorVersion: UInt16) -> Boolean: ...
    @winrt_classmethod
    def IsApiContractPresentByMajorAndMinor(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, contractName: WinRT_String, majorVersion: UInt16, minorVersion: UInt16) -> Boolean: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.Metadata.IApiInformationStatics'
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


make_ready(__name__)
