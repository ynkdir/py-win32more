from __future__ import annotations
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
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.ApplicationModel
import win32more.Windows.ApplicationModel.Activation
import win32more.Windows.Data.Xml.Dom
import win32more.Windows.Devices.Printers
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Graphics.Printing.PrintSupport
import win32more.Windows.Graphics.Printing.PrintTicket
import win32more.Windows.System
import win32more.Windows.UI.Shell
class IPrintSupportExtensionSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionSession'
    _iid_ = Guid('{eea45f1a-f4c6-54b3-a0b8-a559839aa4c3}')
    @winrt_commethod(6)
    def get_Printer(self) -> win32more.Windows.Devices.Printers.IppPrintDevice: ...
    @winrt_commethod(7)
    def add_PrintTicketValidationRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportExtensionSession, win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportPrintTicketValidationRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_PrintTicketValidationRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_PrintDeviceCapabilitiesChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportExtensionSession, win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportPrintDeviceCapabilitiesChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_PrintDeviceCapabilitiesChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def Start(self) -> Void: ...
    Printer = property(get_Printer, None)
class IPrintSupportExtensionSession2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionSession2'
    _iid_ = Guid('{10fa8c11-6de8-5765-8fcf-e716e0f27ed1}')
    @winrt_commethod(6)
    def add_PrinterSelected(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportExtensionSession, win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportPrinterSelectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PrinterSelected(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IPrintSupportExtensionTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionTriggerDetails'
    _iid_ = Guid('{ae083711-9b09-55d1-a0ae-2a14c5f83d6a}')
    @winrt_commethod(6)
    def get_Session(self) -> win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportExtensionSession: ...
    Session = property(get_Session, None)
class IPrintSupportPrintDeviceCapabilitiesChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesChangedEventArgs'
    _iid_ = Guid('{15969bf0-9028-5722-8a37-7d7c34b41dd6}')
    @winrt_commethod(6)
    def GetCurrentPrintDeviceCapabilities(self) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_commethod(7)
    def UpdatePrintDeviceCapabilities(self, updatedPdc: win32more.Windows.Data.Xml.Dom.XmlDocument) -> Void: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
class IPrintSupportPrintDeviceCapabilitiesChangedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesChangedEventArgs2'
    _iid_ = Guid('{469df9e7-fd07-5eeb-a07d-9fcc67f089ba}')
    @winrt_commethod(6)
    def SetSupportedPdlPassthroughContentTypes(self, supportedPdlContentTypes: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> Void: ...
    @winrt_commethod(7)
    def get_ResourceLanguage(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetCurrentPrintDeviceResources(self) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_commethod(9)
    def UpdatePrintDeviceResources(self, updatedPdr: win32more.Windows.Data.Xml.Dom.XmlDocument) -> Void: ...
    @winrt_commethod(10)
    def SetPrintDeviceCapabilitiesUpdatePolicy(self, updatePolicy: win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportPrintDeviceCapabilitiesUpdatePolicy) -> Void: ...
    ResourceLanguage = property(get_ResourceLanguage, None)
class IPrintSupportPrintDeviceCapabilitiesUpdatePolicy(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesUpdatePolicy'
    _iid_ = Guid('{5f5fc025-8c35-5529-8038-8cdc3634bbcd}')
class IPrintSupportPrintDeviceCapabilitiesUpdatePolicyStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesUpdatePolicyStatics'
    _iid_ = Guid('{3d9e1a70-7c39-551f-aa1f-f8ca35b3119e}')
    @winrt_commethod(6)
    def CreatePeriodicRefresh(self, updatePeriod: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportPrintDeviceCapabilitiesUpdatePolicy: ...
    @winrt_commethod(7)
    def CreatePrintJobRefresh(self, numberOfJobs: UInt32) -> win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportPrintDeviceCapabilitiesUpdatePolicy: ...
class IPrintSupportPrintTicketElement(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintTicketElement'
    _iid_ = Guid('{4b2a4489-730d-5be7-80e6-8332941abf13}')
    @winrt_commethod(6)
    def get_LocalName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_LocalName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_NamespaceUri(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_NamespaceUri(self, value: WinRT_String) -> Void: ...
    LocalName = property(get_LocalName, put_LocalName)
    NamespaceUri = property(get_NamespaceUri, put_NamespaceUri)
class IPrintSupportPrintTicketValidationRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintTicketValidationRequestedEventArgs'
    _iid_ = Guid('{338e4e69-db55-55c7-8338-ef64680a8f90}')
    @winrt_commethod(6)
    def get_PrintTicket(self) -> win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket: ...
    @winrt_commethod(7)
    def SetPrintTicketValidationStatus(self, status: win32more.Windows.Graphics.Printing.PrintSupport.WorkflowPrintTicketValidationStatus) -> Void: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    PrintTicket = property(get_PrintTicket, None)
class IPrintSupportPrinterSelectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.IPrintSupportPrinterSelectedEventArgs'
    _iid_ = Guid('{7b1cb7d9-a8a4-5c09-adb2-66165f817977}')
    @winrt_commethod(6)
    def get_SourceAppInfo(self) -> win32more.Windows.ApplicationModel.AppInfo: ...
    @winrt_commethod(7)
    def get_PrintTicket(self) -> win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket: ...
    @winrt_commethod(8)
    def put_PrintTicket(self, value: win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket) -> Void: ...
    @winrt_commethod(9)
    def SetAdditionalFeatures(self, features: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportPrintTicketElement]) -> Void: ...
    @winrt_commethod(10)
    def SetAdditionalParameters(self, parameters: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportPrintTicketElement]) -> Void: ...
    @winrt_commethod(11)
    def get_AllowedAdditionalFeaturesAndParametersCount(self) -> UInt32: ...
    @winrt_commethod(12)
    def SetAdaptiveCard(self, adaptiveCard: win32more.Windows.UI.Shell.IAdaptiveCard) -> Void: ...
    @winrt_commethod(13)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    SourceAppInfo = property(get_SourceAppInfo, None)
    PrintTicket = property(get_PrintTicket, put_PrintTicket)
    AllowedAdditionalFeaturesAndParametersCount = property(get_AllowedAdditionalFeaturesAndParametersCount, None)
class IPrintSupportSessionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.IPrintSupportSessionInfo'
    _iid_ = Guid('{852149af-777d-53e9-9ee9-45d3f4b5be9c}')
    @winrt_commethod(6)
    def get_SourceAppInfo(self) -> win32more.Windows.ApplicationModel.AppInfo: ...
    @winrt_commethod(7)
    def get_Printer(self) -> win32more.Windows.Devices.Printers.IppPrintDevice: ...
    SourceAppInfo = property(get_SourceAppInfo, None)
    Printer = property(get_Printer, None)
class IPrintSupportSettingsActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.IPrintSupportSettingsActivatedEventArgs'
    _iid_ = Guid('{1e1b565e-a013-55ea-9b8c-eea39d9fb6c1}')
    @winrt_commethod(6)
    def get_Session(self) -> win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportSettingsUISession: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Session = property(get_Session, None)
class IPrintSupportSettingsUISession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.IPrintSupportSettingsUISession'
    _iid_ = Guid('{c6da2251-83c3-55e4-a0f8-5de8b062adbf}')
    @winrt_commethod(6)
    def get_SessionPrintTicket(self) -> win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket: ...
    @winrt_commethod(7)
    def get_DocumentTitle(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_LaunchKind(self) -> win32more.Windows.Graphics.Printing.PrintSupport.SettingsLaunchKind: ...
    @winrt_commethod(9)
    def UpdatePrintTicket(self, printTicket: win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket) -> Void: ...
    @winrt_commethod(10)
    def get_SessionInfo(self) -> win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportSessionInfo: ...
    SessionPrintTicket = property(get_SessionPrintTicket, None)
    DocumentTitle = property(get_DocumentTitle, None)
    LaunchKind = property(get_LaunchKind, None)
    SessionInfo = property(get_SessionInfo, None)
class PrintSupportExtensionSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionSession
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.PrintSupportExtensionSession'
    @winrt_mixinmethod
    def get_Printer(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionSession) -> win32more.Windows.Devices.Printers.IppPrintDevice: ...
    @winrt_mixinmethod
    def add_PrintTicketValidationRequested(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionSession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportExtensionSession, win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportPrintTicketValidationRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PrintTicketValidationRequested(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PrintDeviceCapabilitiesChanged(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionSession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportExtensionSession, win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportPrintDeviceCapabilitiesChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PrintDeviceCapabilitiesChanged(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionSession) -> Void: ...
    @winrt_mixinmethod
    def add_PrinterSelected(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionSession2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportExtensionSession, win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportPrinterSelectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PrinterSelected(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionSession2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Printer = property(get_Printer, None)
class PrintSupportExtensionTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionTriggerDetails
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.PrintSupportExtensionTriggerDetails'
    @winrt_mixinmethod
    def get_Session(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionTriggerDetails) -> win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportExtensionSession: ...
    Session = property(get_Session, None)
class PrintSupportPrintDeviceCapabilitiesChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesChangedEventArgs
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.PrintSupportPrintDeviceCapabilitiesChangedEventArgs'
    @winrt_mixinmethod
    def GetCurrentPrintDeviceCapabilities(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesChangedEventArgs) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_mixinmethod
    def UpdatePrintDeviceCapabilities(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesChangedEventArgs, updatedPdc: win32more.Windows.Data.Xml.Dom.XmlDocument) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesChangedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    @winrt_mixinmethod
    def SetSupportedPdlPassthroughContentTypes(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesChangedEventArgs2, supportedPdlContentTypes: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> Void: ...
    @winrt_mixinmethod
    def get_ResourceLanguage(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesChangedEventArgs2) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetCurrentPrintDeviceResources(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesChangedEventArgs2) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_mixinmethod
    def UpdatePrintDeviceResources(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesChangedEventArgs2, updatedPdr: win32more.Windows.Data.Xml.Dom.XmlDocument) -> Void: ...
    @winrt_mixinmethod
    def SetPrintDeviceCapabilitiesUpdatePolicy(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesChangedEventArgs2, updatePolicy: win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportPrintDeviceCapabilitiesUpdatePolicy) -> Void: ...
    ResourceLanguage = property(get_ResourceLanguage, None)
class PrintSupportPrintDeviceCapabilitiesUpdatePolicy(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesUpdatePolicy
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.PrintSupportPrintDeviceCapabilitiesUpdatePolicy'
    @winrt_classmethod
    def CreatePeriodicRefresh(cls: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesUpdatePolicyStatics, updatePeriod: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportPrintDeviceCapabilitiesUpdatePolicy: ...
    @winrt_classmethod
    def CreatePrintJobRefresh(cls: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesUpdatePolicyStatics, numberOfJobs: UInt32) -> win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportPrintDeviceCapabilitiesUpdatePolicy: ...
class PrintSupportPrintTicketElement(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintTicketElement
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.PrintSupportPrintTicketElement'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportPrintTicketElement.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportPrintTicketElement: ...
    @winrt_mixinmethod
    def get_LocalName(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintTicketElement) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_LocalName(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintTicketElement, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_NamespaceUri(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintTicketElement) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NamespaceUri(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintTicketElement, value: WinRT_String) -> Void: ...
    LocalName = property(get_LocalName, put_LocalName)
    NamespaceUri = property(get_NamespaceUri, put_NamespaceUri)
class PrintSupportPrintTicketValidationRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintTicketValidationRequestedEventArgs
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.PrintSupportPrintTicketValidationRequestedEventArgs'
    @winrt_mixinmethod
    def get_PrintTicket(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintTicketValidationRequestedEventArgs) -> win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket: ...
    @winrt_mixinmethod
    def SetPrintTicketValidationStatus(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintTicketValidationRequestedEventArgs, status: win32more.Windows.Graphics.Printing.PrintSupport.WorkflowPrintTicketValidationStatus) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintTicketValidationRequestedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    PrintTicket = property(get_PrintTicket, None)
class PrintSupportPrinterSelectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrinterSelectedEventArgs
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.PrintSupportPrinterSelectedEventArgs'
    @winrt_mixinmethod
    def get_SourceAppInfo(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrinterSelectedEventArgs) -> win32more.Windows.ApplicationModel.AppInfo: ...
    @winrt_mixinmethod
    def get_PrintTicket(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrinterSelectedEventArgs) -> win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket: ...
    @winrt_mixinmethod
    def put_PrintTicket(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrinterSelectedEventArgs, value: win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket) -> Void: ...
    @winrt_mixinmethod
    def SetAdditionalFeatures(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrinterSelectedEventArgs, features: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportPrintTicketElement]) -> Void: ...
    @winrt_mixinmethod
    def SetAdditionalParameters(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrinterSelectedEventArgs, parameters: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportPrintTicketElement]) -> Void: ...
    @winrt_mixinmethod
    def get_AllowedAdditionalFeaturesAndParametersCount(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrinterSelectedEventArgs) -> UInt32: ...
    @winrt_mixinmethod
    def SetAdaptiveCard(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrinterSelectedEventArgs, adaptiveCard: win32more.Windows.UI.Shell.IAdaptiveCard) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportPrinterSelectedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    SourceAppInfo = property(get_SourceAppInfo, None)
    PrintTicket = property(get_PrintTicket, put_PrintTicket)
    AllowedAdditionalFeaturesAndParametersCount = property(get_AllowedAdditionalFeaturesAndParametersCount, None)
class PrintSupportSessionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportSessionInfo
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.PrintSupportSessionInfo'
    @winrt_mixinmethod
    def get_SourceAppInfo(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportSessionInfo) -> win32more.Windows.ApplicationModel.AppInfo: ...
    @winrt_mixinmethod
    def get_Printer(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportSessionInfo) -> win32more.Windows.Devices.Printers.IppPrintDevice: ...
    SourceAppInfo = property(get_SourceAppInfo, None)
    Printer = property(get_Printer, None)
class PrintSupportSettingsActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportSettingsActivatedEventArgs
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.PrintSupportSettingsActivatedEventArgs'
    @winrt_mixinmethod
    def get_Session(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportSettingsActivatedEventArgs) -> win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportSettingsUISession: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportSettingsActivatedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    Session = property(get_Session, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class PrintSupportSettingsUISession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportSettingsUISession
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.PrintSupportSettingsUISession'
    @winrt_mixinmethod
    def get_SessionPrintTicket(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportSettingsUISession) -> win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket: ...
    @winrt_mixinmethod
    def get_DocumentTitle(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportSettingsUISession) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LaunchKind(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportSettingsUISession) -> win32more.Windows.Graphics.Printing.PrintSupport.SettingsLaunchKind: ...
    @winrt_mixinmethod
    def UpdatePrintTicket(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportSettingsUISession, printTicket: win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket) -> Void: ...
    @winrt_mixinmethod
    def get_SessionInfo(self: win32more.Windows.Graphics.Printing.PrintSupport.IPrintSupportSettingsUISession) -> win32more.Windows.Graphics.Printing.PrintSupport.PrintSupportSessionInfo: ...
    SessionPrintTicket = property(get_SessionPrintTicket, None)
    DocumentTitle = property(get_DocumentTitle, None)
    LaunchKind = property(get_LaunchKind, None)
    SessionInfo = property(get_SessionInfo, None)
SettingsLaunchKind = Int32
SettingsLaunchKind_JobPrintTicket: SettingsLaunchKind = 0
SettingsLaunchKind_UserDefaultPrintTicket: SettingsLaunchKind = 1
WorkflowPrintTicketValidationStatus = Int32
WorkflowPrintTicketValidationStatus_Resolved: WorkflowPrintTicketValidationStatus = 0
WorkflowPrintTicketValidationStatus_Conflicting: WorkflowPrintTicketValidationStatus = 1
WorkflowPrintTicketValidationStatus_Invalid: WorkflowPrintTicketValidationStatus = 2


make_ready(__name__)
