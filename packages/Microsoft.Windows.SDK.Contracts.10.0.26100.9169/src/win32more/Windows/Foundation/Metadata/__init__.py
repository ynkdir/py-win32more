from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.Foundation.Metadata
class ApiInformation(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Foundation.Metadata.ApiInformation'
    @winrt_classmethod
    def IsTypePresent(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, typeName: hstr) -> Boolean: ...
    @winrt_classmethod
    def IsMethodPresent(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, typeName: hstr, methodName: hstr) -> Boolean: ...
    @winrt_classmethod
    def IsMethodPresentWithArity(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, typeName: hstr, methodName: hstr, inputParameterCount: UInt32) -> Boolean: ...
    @winrt_classmethod
    def IsEventPresent(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, typeName: hstr, eventName: hstr) -> Boolean: ...
    @winrt_classmethod
    def IsPropertyPresent(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, typeName: hstr, propertyName: hstr) -> Boolean: ...
    @winrt_classmethod
    def IsReadOnlyPropertyPresent(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, typeName: hstr, propertyName: hstr) -> Boolean: ...
    @winrt_classmethod
    def IsWriteablePropertyPresent(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, typeName: hstr, propertyName: hstr) -> Boolean: ...
    @winrt_classmethod
    def IsEnumNamedValuePresent(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, enumTypeName: hstr, valueName: hstr) -> Boolean: ...
    @winrt_classmethod
    def IsApiContractPresentByMajor(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, contractName: hstr, majorVersion: UInt16) -> Boolean: ...
    @winrt_classmethod
    def IsApiContractPresentByMajorAndMinor(cls: win32more.Windows.Foundation.Metadata.IApiInformationStatics, contractName: hstr, majorVersion: UInt16, minorVersion: UInt16) -> Boolean: ...
class AttributeTargets(Enum, UInt32):
    _name_ = 'Windows.Foundation.Metadata.AttributeTargets'
    All = 4294967295
    Delegate = 1
    Enum = 2
    Event = 4
    Field = 8
    Interface = 16
    Method = 64
    Parameter = 128
    Property = 256
    RuntimeClass = 512
    Struct = 1024
    InterfaceImpl = 2048
    ApiContract = 8192
class CompositionType(Enum, Int32):
    _name_ = 'Windows.Foundation.Metadata.CompositionType'
    Protected = 1
    Public = 2
class DeprecationType(Enum, Int32):
    _name_ = 'Windows.Foundation.Metadata.DeprecationType'
    Deprecate = 0
    Remove = 1
class FeatureStage(Enum, Int32):
    _name_ = 'Windows.Foundation.Metadata.FeatureStage'
    AlwaysDisabled = 0
    DisabledByDefault = 1
    EnabledByDefault = 2
    AlwaysEnabled = 3
class GCPressureAmount(Enum, Int32):
    _name_ = 'Windows.Foundation.Metadata.GCPressureAmount'
    Low = 0
    Medium = 1
    High = 2
class IApiInformationStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Foundation.Metadata.IApiInformationStatics'
    _iid_ = Guid('{997439fe-f681-4a11-b416-c13a47e8ba36}')
    @winrt_commethod(6)
    def IsTypePresent(self, typeName: hstr) -> Boolean: ...
    @winrt_commethod(7)
    def IsMethodPresent(self, typeName: hstr, methodName: hstr) -> Boolean: ...
    @winrt_commethod(8)
    def IsMethodPresentWithArity(self, typeName: hstr, methodName: hstr, inputParameterCount: UInt32) -> Boolean: ...
    @winrt_commethod(9)
    def IsEventPresent(self, typeName: hstr, eventName: hstr) -> Boolean: ...
    @winrt_commethod(10)
    def IsPropertyPresent(self, typeName: hstr, propertyName: hstr) -> Boolean: ...
    @winrt_commethod(11)
    def IsReadOnlyPropertyPresent(self, typeName: hstr, propertyName: hstr) -> Boolean: ...
    @winrt_commethod(12)
    def IsWriteablePropertyPresent(self, typeName: hstr, propertyName: hstr) -> Boolean: ...
    @winrt_commethod(13)
    def IsEnumNamedValuePresent(self, enumTypeName: hstr, valueName: hstr) -> Boolean: ...
    @winrt_commethod(14)
    def IsApiContractPresentByMajor(self, contractName: hstr, majorVersion: UInt16) -> Boolean: ...
    @winrt_commethod(15)
    def IsApiContractPresentByMajorAndMinor(self, contractName: hstr, majorVersion: UInt16, minorVersion: UInt16) -> Boolean: ...
class MarshalingType(Enum, Int32):
    _name_ = 'Windows.Foundation.Metadata.MarshalingType'
    None_ = 1
    Agile = 2
    Standard = 3
    InvalidMarshaling = 0
class Platform(Enum, Int32):
    _name_ = 'Windows.Foundation.Metadata.Platform'
    Windows = 0
    WindowsPhone = 1
class ThreadingModel(Enum, Int32):
    _name_ = 'Windows.Foundation.Metadata.ThreadingModel'
    STA = 1
    MTA = 2
    Both = 3
    InvalidThreading = 0


make_ready(__name__)
