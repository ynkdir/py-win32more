from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Data.Xml.Dom
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Graphics.Printing.PrintTicket
class IPrintTicketCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities'
    _iid_ = Guid('{8c45508b-bbdc-4256-a142-2fd615ecb416}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_XmlNamespace(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_XmlNode(self) -> win32more.Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_commethod(9)
    def get_DocumentBindingFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(10)
    def get_DocumentCollateFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(11)
    def get_DocumentDuplexFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(12)
    def get_DocumentHolePunchFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(13)
    def get_DocumentInputBinFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(14)
    def get_DocumentNUpFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(15)
    def get_DocumentStapleFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(16)
    def get_JobPasscodeFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(17)
    def get_PageBorderlessFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(18)
    def get_PageMediaSizeFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(19)
    def get_PageMediaTypeFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(20)
    def get_PageOrientationFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(21)
    def get_PageOutputColorFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(22)
    def get_PageOutputQualityFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(23)
    def get_PageResolutionFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(24)
    def GetFeature(self, name: WinRT_String, xmlNamespace: WinRT_String) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(25)
    def GetParameterDefinition(self, name: WinRT_String, xmlNamespace: WinRT_String) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketParameterDefinition: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintTicket.IPrintTicketFeature'
    _iid_ = Guid('{e7607d6a-59f5-4103-8858-b97710963d39}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_XmlNamespace(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_XmlNode(self) -> win32more.Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_commethod(9)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def GetOption(self, name: WinRT_String, xmlNamespace: WinRT_String) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketOption: ...
    @winrt_commethod(11)
    def get_Options(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketOption]: ...
    @winrt_commethod(12)
    def GetSelectedOption(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketOption: ...
    @winrt_commethod(13)
    def SetSelectedOption(self, value: win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketOption) -> Void: ...
    @winrt_commethod(14)
    def get_SelectionType(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeatureSelectionType: ...
    Name = property(get_Name, None)
    XmlNamespace = property(get_XmlNamespace, None)
    XmlNode = property(get_XmlNode, None)
    DisplayName = property(get_DisplayName, None)
    Options = property(get_Options, None)
    SelectionType = property(get_SelectionType, None)
class IPrintTicketOption(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintTicket.IPrintTicketOption'
    _iid_ = Guid('{b086cf90-b367-4e4b-bd48-9c78a0bb31ce}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_XmlNamespace(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_XmlNode(self) -> win32more.Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_commethod(9)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def GetPropertyNode(self, name: WinRT_String, xmlNamespace: WinRT_String) -> win32more.Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_commethod(11)
    def GetScoredPropertyNode(self, name: WinRT_String, xmlNamespace: WinRT_String) -> win32more.Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_commethod(12)
    def GetPropertyValue(self, name: WinRT_String, xmlNamespace: WinRT_String) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketValue: ...
    @winrt_commethod(13)
    def GetScoredPropertyValue(self, name: WinRT_String, xmlNamespace: WinRT_String) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketValue: ...
    Name = property(get_Name, None)
    XmlNamespace = property(get_XmlNamespace, None)
    XmlNode = property(get_XmlNode, None)
    DisplayName = property(get_DisplayName, None)
class IPrintTicketParameterDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterDefinition'
    _iid_ = Guid('{d6bab4e4-2962-4c01-b7f3-9a9294eb8335}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_XmlNamespace(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_XmlNode(self) -> win32more.Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_commethod(9)
    def get_DataType(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketParameterDataType: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterInitializer'
    _iid_ = Guid('{5e3335bb-a0a5-48b1-9d5c-07116ddc597a}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_XmlNamespace(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_XmlNode(self) -> win32more.Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_commethod(9)
    def put_Value(self, value: win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketValue) -> Void: ...
    @winrt_commethod(10)
    def get_Value(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketValue: ...
    Name = property(get_Name, None)
    XmlNamespace = property(get_XmlNamespace, None)
    XmlNode = property(get_XmlNode, None)
    Value = property(get_Value, put_Value)
class IPrintTicketValue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintTicket.IPrintTicketValue'
    _iid_ = Guid('{66b30a32-244d-4e22-a98b-bb3cf1f2dd91}')
    @winrt_commethod(6)
    def get_Type(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketValueType: ...
    @winrt_commethod(7)
    def GetValueAsInteger(self) -> Int32: ...
    @winrt_commethod(8)
    def GetValueAsString(self) -> WinRT_String: ...
    Type = property(get_Type, None)
class IWorkflowPrintTicket(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket'
    _iid_ = Guid('{41d52285-35e8-448e-a8c5-e4b6a2cf826c}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_XmlNamespace(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_XmlNode(self) -> win32more.Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_commethod(9)
    def GetCapabilities(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketCapabilities: ...
    @winrt_commethod(10)
    def get_DocumentBindingFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(11)
    def get_DocumentCollateFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(12)
    def get_DocumentDuplexFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(13)
    def get_DocumentHolePunchFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(14)
    def get_DocumentInputBinFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(15)
    def get_DocumentNUpFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(16)
    def get_DocumentStapleFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(17)
    def get_JobPasscodeFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(18)
    def get_PageBorderlessFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(19)
    def get_PageMediaSizeFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(20)
    def get_PageMediaTypeFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(21)
    def get_PageOrientationFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(22)
    def get_PageOutputColorFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(23)
    def get_PageOutputQualityFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(24)
    def get_PageResolutionFeature(self) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(25)
    def GetFeature(self, name: WinRT_String, xmlNamespace: WinRT_String) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_commethod(26)
    def NotifyXmlChangedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(27)
    def ValidateAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicketValidationResult]: ...
    @winrt_commethod(28)
    def GetParameterInitializer(self, name: WinRT_String, xmlNamespace: WinRT_String) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketParameterInitializer: ...
    @winrt_commethod(29)
    def SetParameterInitializerAsInteger(self, name: WinRT_String, xmlNamespace: WinRT_String, integerValue: Int32) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketParameterInitializer: ...
    @winrt_commethod(30)
    def SetParameterInitializerAsString(self, name: WinRT_String, xmlNamespace: WinRT_String, stringValue: WinRT_String) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketParameterInitializer: ...
    @winrt_commethod(31)
    def MergeAndValidateTicket(self, deltaShemaTicket: win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket) -> win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicketValidationResult'
    _iid_ = Guid('{0ad1f392-da7b-4a36-bf36-6a99a62e2059}')
    @winrt_commethod(6)
    def get_Validated(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    Validated = property(get_Validated, None)
    ExtendedError = property(get_ExtendedError, None)
class PrintTicketCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities
    _classid_ = 'Windows.Graphics.Printing.PrintTicket.PrintTicketCapabilities'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_XmlNamespace(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_XmlNode(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> win32more.Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_mixinmethod
    def get_DocumentBindingFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_DocumentCollateFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_DocumentDuplexFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_DocumentHolePunchFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_DocumentInputBinFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_DocumentNUpFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_DocumentStapleFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_JobPasscodeFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageBorderlessFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageMediaSizeFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageMediaTypeFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageOrientationFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageOutputColorFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageOutputQualityFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageResolutionFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def GetFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities, name: WinRT_String, xmlNamespace: WinRT_String) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def GetParameterDefinition(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketCapabilities, name: WinRT_String, xmlNamespace: WinRT_String) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketParameterDefinition: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketFeature
    _classid_ = 'Windows.Graphics.Printing.PrintTicket.PrintTicketFeature'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketFeature) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_XmlNamespace(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketFeature) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_XmlNode(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketFeature) -> win32more.Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketFeature) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetOption(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketFeature, name: WinRT_String, xmlNamespace: WinRT_String) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketOption: ...
    @winrt_mixinmethod
    def get_Options(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketFeature) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketOption]: ...
    @winrt_mixinmethod
    def GetSelectedOption(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketFeature) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketOption: ...
    @winrt_mixinmethod
    def SetSelectedOption(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketFeature, value: win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketOption) -> Void: ...
    @winrt_mixinmethod
    def get_SelectionType(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketFeature) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeatureSelectionType: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketOption
    _classid_ = 'Windows.Graphics.Printing.PrintTicket.PrintTicketOption'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketOption) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_XmlNamespace(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketOption) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_XmlNode(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketOption) -> win32more.Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketOption) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetPropertyNode(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketOption, name: WinRT_String, xmlNamespace: WinRT_String) -> win32more.Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_mixinmethod
    def GetScoredPropertyNode(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketOption, name: WinRT_String, xmlNamespace: WinRT_String) -> win32more.Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_mixinmethod
    def GetPropertyValue(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketOption, name: WinRT_String, xmlNamespace: WinRT_String) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketValue: ...
    @winrt_mixinmethod
    def GetScoredPropertyValue(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketOption, name: WinRT_String, xmlNamespace: WinRT_String) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketValue: ...
    Name = property(get_Name, None)
    XmlNamespace = property(get_XmlNamespace, None)
    XmlNode = property(get_XmlNode, None)
    DisplayName = property(get_DisplayName, None)
PrintTicketParameterDataType = Int32
PrintTicketParameterDataType_Integer: PrintTicketParameterDataType = 0
PrintTicketParameterDataType_NumericString: PrintTicketParameterDataType = 1
PrintTicketParameterDataType_String: PrintTicketParameterDataType = 2
class PrintTicketParameterDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterDefinition
    _classid_ = 'Windows.Graphics.Printing.PrintTicket.PrintTicketParameterDefinition'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_XmlNamespace(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_XmlNode(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterDefinition) -> win32more.Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_mixinmethod
    def get_DataType(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterDefinition) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketParameterDataType: ...
    @winrt_mixinmethod
    def get_UnitType(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RangeMin(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterDefinition) -> Int32: ...
    @winrt_mixinmethod
    def get_RangeMax(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterDefinition) -> Int32: ...
    Name = property(get_Name, None)
    XmlNamespace = property(get_XmlNamespace, None)
    XmlNode = property(get_XmlNode, None)
    DataType = property(get_DataType, None)
    UnitType = property(get_UnitType, None)
    RangeMin = property(get_RangeMin, None)
    RangeMax = property(get_RangeMax, None)
class PrintTicketParameterInitializer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterInitializer
    _classid_ = 'Windows.Graphics.Printing.PrintTicket.PrintTicketParameterInitializer'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterInitializer) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_XmlNamespace(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterInitializer) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_XmlNode(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterInitializer) -> win32more.Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterInitializer, value: win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketValue) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketParameterInitializer) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketValue: ...
    Name = property(get_Name, None)
    XmlNamespace = property(get_XmlNamespace, None)
    XmlNode = property(get_XmlNode, None)
    Value = property(get_Value, put_Value)
class PrintTicketValue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketValue
    _classid_ = 'Windows.Graphics.Printing.PrintTicket.PrintTicketValue'
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketValue) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketValueType: ...
    @winrt_mixinmethod
    def GetValueAsInteger(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketValue) -> Int32: ...
    @winrt_mixinmethod
    def GetValueAsString(self: win32more.Windows.Graphics.Printing.PrintTicket.IPrintTicketValue) -> WinRT_String: ...
    Type = property(get_Type, None)
PrintTicketValueType = Int32
PrintTicketValueType_Integer: PrintTicketValueType = 0
PrintTicketValueType_String: PrintTicketValueType = 1
PrintTicketValueType_Unknown: PrintTicketValueType = 2
class WorkflowPrintTicket(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket
    _classid_ = 'Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_XmlNamespace(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_XmlNode(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> win32more.Windows.Data.Xml.Dom.IXmlNode: ...
    @winrt_mixinmethod
    def GetCapabilities(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketCapabilities: ...
    @winrt_mixinmethod
    def get_DocumentBindingFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_DocumentCollateFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_DocumentDuplexFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_DocumentHolePunchFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_DocumentInputBinFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_DocumentNUpFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_DocumentStapleFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_JobPasscodeFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageBorderlessFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageMediaSizeFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageMediaTypeFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageOrientationFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageOutputColorFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageOutputQualityFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def get_PageResolutionFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def GetFeature(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket, name: WinRT_String, xmlNamespace: WinRT_String) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketFeature: ...
    @winrt_mixinmethod
    def NotifyXmlChangedAsync(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ValidateAsync(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicketValidationResult]: ...
    @winrt_mixinmethod
    def GetParameterInitializer(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket, name: WinRT_String, xmlNamespace: WinRT_String) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketParameterInitializer: ...
    @winrt_mixinmethod
    def SetParameterInitializerAsInteger(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket, name: WinRT_String, xmlNamespace: WinRT_String, integerValue: Int32) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketParameterInitializer: ...
    @winrt_mixinmethod
    def SetParameterInitializerAsString(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket, name: WinRT_String, xmlNamespace: WinRT_String, stringValue: WinRT_String) -> win32more.Windows.Graphics.Printing.PrintTicket.PrintTicketParameterInitializer: ...
    @winrt_mixinmethod
    def MergeAndValidateTicket(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicket, deltaShemaTicket: win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket) -> win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicketValidationResult
    _classid_ = 'Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicketValidationResult'
    @winrt_mixinmethod
    def get_Validated(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicketValidationResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Graphics.Printing.PrintTicket.IWorkflowPrintTicketValidationResult) -> win32more.Windows.Foundation.HResult: ...
    Validated = property(get_Validated, None)
    ExtendedError = property(get_ExtendedError, None)
make_ready(__name__)
