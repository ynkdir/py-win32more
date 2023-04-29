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
import Windows.Data.Xml.Dom
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Graphics.Printing.PrintTicket
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IPrintTicketCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('8c45508b-bbdc-4256-a1-42-2f-d6-15-ec-b4-16')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_XmlNamespace(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_XmlNode(self) -> Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_commethod(9)
    def get_DocumentBindingFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(10)
    def get_DocumentCollateFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(11)
    def get_DocumentDuplexFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(12)
    def get_DocumentHolePunchFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(13)
    def get_DocumentInputBinFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(14)
    def get_DocumentNUpFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(15)
    def get_DocumentStapleFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(16)
    def get_JobPasscodeFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(17)
    def get_PageBorderlessFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(18)
    def get_PageMediaSizeFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(19)
    def get_PageMediaTypeFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(20)
    def get_PageOrientationFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(21)
    def get_PageOutputColorFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(22)
    def get_PageOutputQualityFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(23)
    def get_PageResolutionFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(24)
    def GetFeature(self, name: WinRT_String, xmlNamespace: WinRT_String) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(25)
    def GetParameterDefinition(self, name: WinRT_String, xmlNamespace: WinRT_String) -> Windows.Graphics.Printing.PrintTicket.PrintTicketParameterDefinition: ...
    Name = property(get_Name, None)
    XmlNamespace = property(get_XmlNamespace, None)
    XmlNode = property(get_XmlNode, None)
    DocumentBindingFeature = property(get_DocumentBindingFeature, None)
    DocumentCollateFeature = property(get_DocumentCollateFeature, None)
    DocumentDuplexFeature = property(get_DocumentDuplexFeature, None)
    DocumentHolePunchFeature = property(get_DocumentHolePunchFeature, None)
    DocumentInputBinFeature = property(get_DocumentInputBinFeature, None)
    DocumentNUpFeature = property(get_DocumentNUpFeature, None)
    DocumentStapleFeature = property(get_DocumentStapleFeature, None)
    JobPasscodeFeature = property(get_JobPasscodeFeature, None)
    PageBorderlessFeature = property(get_PageBorderlessFeature, None)
    PageMediaSizeFeature = property(get_PageMediaSizeFeature, None)
    PageMediaTypeFeature = property(get_PageMediaTypeFeature, None)
    PageOrientationFeature = property(get_PageOrientationFeature, None)
    PageOutputColorFeature = property(get_PageOutputColorFeature, None)
    PageOutputQualityFeature = property(get_PageOutputQualityFeature, None)
    PageResolutionFeature = property(get_PageResolutionFeature, None)
class IPrintTicketFeature(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e7607d6a-59f5-4103-88-58-b9-77-10-96-3d-39')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_XmlNamespace(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_XmlNode(self) -> Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_commethod(9)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def GetOption(self, name: WinRT_String, xmlNamespace: WinRT_String) -> Windows.Graphics.Printing.PrintTicket.PrintTicketOption: ...
    @winrt_commethod(11)
    def get_Options(self) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.Printing.PrintTicket.PrintTicketOption]: ...
    @winrt_commethod(12)
    def GetSelectedOption(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketOption: ...
    @winrt_commethod(13)
    def SetSelectedOption(self, value: Windows.Graphics.Printing.PrintTicket.PrintTicketOption) -> Void: ...
    @winrt_commethod(14)
    def get_SelectionType(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeatureSelectionType: ...
    Name = property(get_Name, None)
    XmlNamespace = property(get_XmlNamespace, None)
    XmlNode = property(get_XmlNode, None)
    DisplayName = property(get_DisplayName, None)
    Options = property(get_Options, None)
    SelectionType = property(get_SelectionType, None)
class IPrintTicketOption(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b086cf90-b367-4e4b-bd-48-9c-78-a0-bb-31-ce')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_XmlNamespace(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_XmlNode(self) -> Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_commethod(9)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def GetPropertyNode(self, name: WinRT_String, xmlNamespace: WinRT_String) -> Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_commethod(11)
    def GetScoredPropertyNode(self, name: WinRT_String, xmlNamespace: WinRT_String) -> Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_commethod(12)
    def GetPropertyValue(self, name: WinRT_String, xmlNamespace: WinRT_String) -> Windows.Graphics.Printing.PrintTicket.PrintTicketValue: ...
    @winrt_commethod(13)
    def GetScoredPropertyValue(self, name: WinRT_String, xmlNamespace: WinRT_String) -> Windows.Graphics.Printing.PrintTicket.PrintTicketValue: ...
    Name = property(get_Name, None)
    XmlNamespace = property(get_XmlNamespace, None)
    XmlNode = property(get_XmlNode, None)
    DisplayName = property(get_DisplayName, None)
class IPrintTicketParameterDefinition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d6bab4e4-2962-4c01-b7-f3-9a-92-94-eb-83-35')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_XmlNamespace(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_XmlNode(self) -> Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_commethod(9)
    def get_DataType(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketParameterDataType: ...
    @winrt_commethod(10)
    def get_UnitType(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_RangeMin(self) -> Int32: ...
    @winrt_commethod(12)
    def get_RangeMax(self) -> Int32: ...
    Name = property(get_Name, None)
    XmlNamespace = property(get_XmlNamespace, None)
    XmlNode = property(get_XmlNode, None)
    DataType = property(get_DataType, None)
    UnitType = property(get_UnitType, None)
    RangeMin = property(get_RangeMin, None)
    RangeMax = property(get_RangeMax, None)
class IPrintTicketParameterInitializer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('5e3335bb-a0a5-48b1-9d-5c-07-11-6d-dc-59-7a')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_XmlNamespace(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_XmlNode(self) -> Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_commethod(9)
    def put_Value(self, value: Windows.Graphics.Printing.PrintTicket.PrintTicketValue) -> Void: ...
    @winrt_commethod(10)
    def get_Value(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketValue: ...
    Name = property(get_Name, None)
    XmlNamespace = property(get_XmlNamespace, None)
    XmlNode = property(get_XmlNode, None)
    Value = property(get_Value, put_Value)
class IPrintTicketValue(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('66b30a32-244d-4e22-a9-8b-bb-3c-f1-f2-dd-91')
    @winrt_commethod(6)
    def get_Type(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketValueType: ...
    @winrt_commethod(7)
    def GetValueAsInteger(self) -> Int32: ...
    @winrt_commethod(8)
    def GetValueAsString(self) -> WinRT_String: ...
    Type = property(get_Type, None)
class IWorkflowPrintTicket(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('41d52285-35e8-448e-a8-c5-e4-b6-a2-cf-82-6c')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_XmlNamespace(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_XmlNode(self) -> Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_commethod(9)
    def GetCapabilities(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketCapabilities: ...
    @winrt_commethod(10)
    def get_DocumentBindingFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(11)
    def get_DocumentCollateFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(12)
    def get_DocumentDuplexFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(13)
    def get_DocumentHolePunchFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(14)
    def get_DocumentInputBinFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(15)
    def get_DocumentNUpFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(16)
    def get_DocumentStapleFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(17)
    def get_JobPasscodeFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(18)
    def get_PageBorderlessFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(19)
    def get_PageMediaSizeFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(20)
    def get_PageMediaTypeFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(21)
    def get_PageOrientationFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(22)
    def get_PageOutputColorFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(23)
    def get_PageOutputQualityFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(24)
    def get_PageResolutionFeature(self) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(25)
    def GetFeature(self, name: WinRT_String, xmlNamespace: WinRT_String) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(26)
    def NotifyXmlChangedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(27)
    def ValidateAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicketValidationResult]: ...
    @winrt_commethod(28)
    def GetParameterInitializer(self, name: WinRT_String, xmlNamespace: WinRT_String) -> Windows.Graphics.Printing.PrintTicket.PrintTicketParameterInitializer: ...
    @winrt_commethod(29)
    def SetParameterInitializerAsInteger(self, name: WinRT_String, xmlNamespace: WinRT_String, integerValue: Int32) -> Windows.Graphics.Printing.PrintTicket.PrintTicketParameterInitializer: ...
    @winrt_commethod(30)
    def SetParameterInitializerAsString(self, name: WinRT_String, xmlNamespace: WinRT_String, stringValue: WinRT_String) -> Windows.Graphics.Printing.PrintTicket.PrintTicketParameterInitializer: ...
    @winrt_commethod(31)
    def MergeAndValidateTicket(self, deltaShemaTicket: Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket) -> Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket: ...
    Name = property(get_Name, None)
    XmlNamespace = property(get_XmlNamespace, None)
    XmlNode = property(get_XmlNode, None)
    DocumentBindingFeature = property(get_DocumentBindingFeature, None)
    DocumentCollateFeature = property(get_DocumentCollateFeature, None)
    DocumentDuplexFeature = property(get_DocumentDuplexFeature, None)
    DocumentHolePunchFeature = property(get_DocumentHolePunchFeature, None)
    DocumentInputBinFeature = property(get_DocumentInputBinFeature, None)
    DocumentNUpFeature = property(get_DocumentNUpFeature, None)
    DocumentStapleFeature = property(get_DocumentStapleFeature, None)
    JobPasscodeFeature = property(get_JobPasscodeFeature, None)
    PageBorderlessFeature = property(get_PageBorderlessFeature, None)
    PageMediaSizeFeature = property(get_PageMediaSizeFeature, None)
    PageMediaTypeFeature = property(get_PageMediaTypeFeature, None)
    PageOrientationFeature = property(get_PageOrientationFeature, None)
    PageOutputColorFeature = property(get_PageOutputColorFeature, None)
    PageOutputQualityFeature = property(get_PageOutputQualityFeature, None)
    PageResolutionFeature = property(get_PageResolutionFeature, None)
class IWorkflowPrintTicketValidationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0ad1f392-da7b-4a36-bf-36-6a-99-a6-2e-20-59')
    @winrt_commethod(6)
    def get_Validated(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    Validated = property(get_Validated, None)
    ExtendedError = property(get_ExtendedError, None)
class PrintTicketCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Graphics.Printing.PrintTicket.PrintTicketCapabilities'
    @winrt_mixinmethod
    def get_Name(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_XmlNamespace(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_XmlNode(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_mixinmethod
    def get_DocumentBindingFeature(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_DocumentCollateFeature(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_DocumentDuplexFeature(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_DocumentHolePunchFeature(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_DocumentInputBinFeature(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_DocumentNUpFeature(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_DocumentStapleFeature(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_JobPasscodeFeature(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageBorderlessFeature(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageMediaSizeFeature(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageMediaTypeFeature(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageOrientationFeature(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageOutputColorFeature(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageOutputQualityFeature(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageResolutionFeature(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def GetFeature(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities, name: WinRT_String, xmlNamespace: WinRT_String) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def GetParameterDefinition(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities, name: WinRT_String, xmlNamespace: WinRT_String) -> Windows.Graphics.Printing.PrintTicket.PrintTicketParameterDefinition: ...
    Name = property(get_Name, None)
    XmlNamespace = property(get_XmlNamespace, None)
    XmlNode = property(get_XmlNode, None)
    DocumentBindingFeature = property(get_DocumentBindingFeature, None)
    DocumentCollateFeature = property(get_DocumentCollateFeature, None)
    DocumentDuplexFeature = property(get_DocumentDuplexFeature, None)
    DocumentHolePunchFeature = property(get_DocumentHolePunchFeature, None)
    DocumentInputBinFeature = property(get_DocumentInputBinFeature, None)
    DocumentNUpFeature = property(get_DocumentNUpFeature, None)
    DocumentStapleFeature = property(get_DocumentStapleFeature, None)
    JobPasscodeFeature = property(get_JobPasscodeFeature, None)
    PageBorderlessFeature = property(get_PageBorderlessFeature, None)
    PageMediaSizeFeature = property(get_PageMediaSizeFeature, None)
    PageMediaTypeFeature = property(get_PageMediaTypeFeature, None)
    PageOrientationFeature = property(get_PageOrientationFeature, None)
    PageOutputColorFeature = property(get_PageOutputColorFeature, None)
    PageOutputQualityFeature = property(get_PageOutputQualityFeature, None)
    PageResolutionFeature = property(get_PageResolutionFeature, None)
class PrintTicketFeature(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Graphics.Printing.PrintTicket.PrintTicketFeature'
    @winrt_mixinmethod
    def get_Name(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketFeature) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_XmlNamespace(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketFeature) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_XmlNode(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketFeature) -> Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketFeature) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetOption(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketFeature, name: WinRT_String, xmlNamespace: WinRT_String) -> Windows.Graphics.Printing.PrintTicket.PrintTicketOption: ...
    @winrt_mixinmethod
    def get_Options(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketFeature) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.Printing.PrintTicket.PrintTicketOption]: ...
    @winrt_mixinmethod
    def GetSelectedOption(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketFeature) -> Windows.Graphics.Printing.PrintTicket.PrintTicketOption: ...
    @winrt_mixinmethod
    def SetSelectedOption(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketFeature, value: Windows.Graphics.Printing.PrintTicket.PrintTicketOption) -> Void: ...
    @winrt_mixinmethod
    def get_SelectionType(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketFeature) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeatureSelectionType: ...
    Name = property(get_Name, None)
    XmlNamespace = property(get_XmlNamespace, None)
    XmlNode = property(get_XmlNode, None)
    DisplayName = property(get_DisplayName, None)
    Options = property(get_Options, None)
    SelectionType = property(get_SelectionType, None)
PrintTicketFeatureSelectionType = Int32
PrintTicketFeatureSelectionType_PickOne: PrintTicketFeatureSelectionType = 0
PrintTicketFeatureSelectionType_PickMany: PrintTicketFeatureSelectionType = 1
class PrintTicketOption(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Graphics.Printing.PrintTicket.PrintTicketOption'
    @winrt_mixinmethod
    def get_Name(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketOption) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_XmlNamespace(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketOption) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_XmlNode(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketOption) -> Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketOption) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetPropertyNode(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketOption, name: WinRT_String, xmlNamespace: WinRT_String) -> Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_mixinmethod
    def GetScoredPropertyNode(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketOption, name: WinRT_String, xmlNamespace: WinRT_String) -> Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_mixinmethod
    def GetPropertyValue(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketOption, name: WinRT_String, xmlNamespace: WinRT_String) -> Windows.Graphics.Printing.PrintTicket.PrintTicketValue: ...
    @winrt_mixinmethod
    def GetScoredPropertyValue(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketOption, name: WinRT_String, xmlNamespace: WinRT_String) -> Windows.Graphics.Printing.PrintTicket.PrintTicketValue: ...
    Name = property(get_Name, None)
    XmlNamespace = property(get_XmlNamespace, None)
    XmlNode = property(get_XmlNode, None)
    DisplayName = property(get_DisplayName, None)
PrintTicketParameterDataType = Int32
PrintTicketParameterDataType_Integer: PrintTicketParameterDataType = 0
PrintTicketParameterDataType_NumericString: PrintTicketParameterDataType = 1
PrintTicketParameterDataType_String: PrintTicketParameterDataType = 2
class PrintTicketParameterDefinition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Graphics.Printing.PrintTicket.PrintTicketParameterDefinition'
    @winrt_mixinmethod
    def get_Name(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_XmlNamespace(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_XmlNode(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterDefinition) -> Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_mixinmethod
    def get_DataType(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterDefinition) -> Windows.Graphics.Printing.PrintTicket.PrintTicketParameterDataType: ...
    @winrt_mixinmethod
    def get_UnitType(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RangeMin(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterDefinition) -> Int32: ...
    @winrt_mixinmethod
    def get_RangeMax(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterDefinition) -> Int32: ...
    Name = property(get_Name, None)
    XmlNamespace = property(get_XmlNamespace, None)
    XmlNode = property(get_XmlNode, None)
    DataType = property(get_DataType, None)
    UnitType = property(get_UnitType, None)
    RangeMin = property(get_RangeMin, None)
    RangeMax = property(get_RangeMax, None)
class PrintTicketParameterInitializer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Graphics.Printing.PrintTicket.PrintTicketParameterInitializer'
    @winrt_mixinmethod
    def get_Name(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterInitializer) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_XmlNamespace(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterInitializer) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_XmlNode(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterInitializer) -> Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_mixinmethod
    def put_Value(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterInitializer, value: Windows.Graphics.Printing.PrintTicket.PrintTicketValue) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterInitializer) -> Windows.Graphics.Printing.PrintTicket.PrintTicketValue: ...
    Name = property(get_Name, None)
    XmlNamespace = property(get_XmlNamespace, None)
    XmlNode = property(get_XmlNode, None)
    Value = property(get_Value, put_Value)
class PrintTicketValue(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Graphics.Printing.PrintTicket.PrintTicketValue'
    @winrt_mixinmethod
    def get_Type(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketValue) -> Windows.Graphics.Printing.PrintTicket.PrintTicketValueType: ...
    @winrt_mixinmethod
    def GetValueAsInteger(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketValue) -> Int32: ...
    @winrt_mixinmethod
    def GetValueAsString(self: Windows.Graphics.Printing.PrintTicket.IPrintTicketValue) -> WinRT_String: ...
    Type = property(get_Type, None)
PrintTicketValueType = Int32
PrintTicketValueType_Integer: PrintTicketValueType = 0
PrintTicketValueType_String: PrintTicketValueType = 1
PrintTicketValueType_Unknown: PrintTicketValueType = 2
class WorkflowPrintTicket(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket'
    @winrt_mixinmethod
    def get_Name(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_XmlNamespace(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_XmlNode(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_mixinmethod
    def GetCapabilities(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> Windows.Graphics.Printing.PrintTicket.PrintTicketCapabilities: ...
    @winrt_mixinmethod
    def get_DocumentBindingFeature(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_DocumentCollateFeature(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_DocumentDuplexFeature(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_DocumentHolePunchFeature(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_DocumentInputBinFeature(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_DocumentNUpFeature(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_DocumentStapleFeature(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_JobPasscodeFeature(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageBorderlessFeature(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageMediaSizeFeature(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageMediaTypeFeature(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageOrientationFeature(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageOutputColorFeature(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageOutputQualityFeature(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageResolutionFeature(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def GetFeature(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket, name: WinRT_String, xmlNamespace: WinRT_String) -> Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def NotifyXmlChangedAsync(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ValidateAsync(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> Windows.Foundation.IAsyncOperation[Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicketValidationResult]: ...
    @winrt_mixinmethod
    def GetParameterInitializer(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket, name: WinRT_String, xmlNamespace: WinRT_String) -> Windows.Graphics.Printing.PrintTicket.PrintTicketParameterInitializer: ...
    @winrt_mixinmethod
    def SetParameterInitializerAsInteger(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket, name: WinRT_String, xmlNamespace: WinRT_String, integerValue: Int32) -> Windows.Graphics.Printing.PrintTicket.PrintTicketParameterInitializer: ...
    @winrt_mixinmethod
    def SetParameterInitializerAsString(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket, name: WinRT_String, xmlNamespace: WinRT_String, stringValue: WinRT_String) -> Windows.Graphics.Printing.PrintTicket.PrintTicketParameterInitializer: ...
    @winrt_mixinmethod
    def MergeAndValidateTicket(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket, deltaShemaTicket: Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket) -> Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket: ...
    Name = property(get_Name, None)
    XmlNamespace = property(get_XmlNamespace, None)
    XmlNode = property(get_XmlNode, None)
    DocumentBindingFeature = property(get_DocumentBindingFeature, None)
    DocumentCollateFeature = property(get_DocumentCollateFeature, None)
    DocumentDuplexFeature = property(get_DocumentDuplexFeature, None)
    DocumentHolePunchFeature = property(get_DocumentHolePunchFeature, None)
    DocumentInputBinFeature = property(get_DocumentInputBinFeature, None)
    DocumentNUpFeature = property(get_DocumentNUpFeature, None)
    DocumentStapleFeature = property(get_DocumentStapleFeature, None)
    JobPasscodeFeature = property(get_JobPasscodeFeature, None)
    PageBorderlessFeature = property(get_PageBorderlessFeature, None)
    PageMediaSizeFeature = property(get_PageMediaSizeFeature, None)
    PageMediaTypeFeature = property(get_PageMediaTypeFeature, None)
    PageOrientationFeature = property(get_PageOrientationFeature, None)
    PageOutputColorFeature = property(get_PageOutputColorFeature, None)
    PageOutputQualityFeature = property(get_PageOutputQualityFeature, None)
    PageResolutionFeature = property(get_PageResolutionFeature, None)
class WorkflowPrintTicketValidationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicketValidationResult'
    @winrt_mixinmethod
    def get_Validated(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicketValidationResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicketValidationResult) -> Windows.Foundation.HResult: ...
    Validated = property(get_Validated, None)
    ExtendedError = property(get_ExtendedError, None)
make_head(_module, 'IPrintTicketCapabilities')
make_head(_module, 'IPrintTicketFeature')
make_head(_module, 'IPrintTicketOption')
make_head(_module, 'IPrintTicketParameterDefinition')
make_head(_module, 'IPrintTicketParameterInitializer')
make_head(_module, 'IPrintTicketValue')
make_head(_module, 'IWorkflowPrintTicket')
make_head(_module, 'IWorkflowPrintTicketValidationResult')
make_head(_module, 'PrintTicketCapabilities')
make_head(_module, 'PrintTicketFeature')
make_head(_module, 'PrintTicketOption')
make_head(_module, 'PrintTicketParameterDefinition')
make_head(_module, 'PrintTicketParameterInitializer')
make_head(_module, 'PrintTicketValue')
make_head(_module, 'WorkflowPrintTicket')
make_head(_module, 'WorkflowPrintTicketValidationResult')
