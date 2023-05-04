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
import Windows.ApplicationModel
import Windows.ApplicationModel.Activation
import Windows.Data.Xml.Dom
import Windows.Devices.Printers
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Graphics.Printing.PrintSupport
import Windows.Graphics.Printing.PrintTicket
import Windows.System
import Windows.UI.Shell
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IPrintSupportExtensionSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionSession'
    _iid_ = Guid('{eea45f1a-f4c6-54b3-a0b8-a559839aa4c3}')
    @winrt_commethod(6)
    def get_Printer(self) -> Windows.Devices.Printers.IppPrintDevice: ...
    @winrt_commethod(7)
    def add_PrintTicketValidationRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Printing.PrintSupport.PrintSupportExtensionSession, Windows.Graphics.Printing.PrintSupport.PrintSupportPrintTicketValidationRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_PrintTicketValidationRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_PrintDeviceCapabilitiesChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Printing.PrintSupport.PrintSupportExtensionSession, Windows.Graphics.Printing.PrintSupport.PrintSupportPrintDeviceCapabilitiesChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_PrintDeviceCapabilitiesChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def Start(self) -> Void: ...
    Printer = property(get_Printer, None)
class IPrintSupportExtensionSession2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionSession2'
    _iid_ = Guid('{10fa8c11-6de8-5765-8fcf-e716e0f27ed1}')
    @winrt_commethod(6)
    def add_PrinterSelected(self, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Printing.PrintSupport.PrintSupportExtensionSession, Windows.Graphics.Printing.PrintSupport.PrintSupportPrinterSelectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PrinterSelected(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IPrintSupportExtensionTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionTriggerDetails'
    _iid_ = Guid('{ae083711-9b09-55d1-a0ae-2a14c5f83d6a}')
    @winrt_commethod(6)
    def get_Session(self) -> Windows.Graphics.Printing.PrintSupport.PrintSupportExtensionSession: ...
    Session = property(get_Session, None)
class IPrintSupportPrintDeviceCapabilitiesChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesChangedEventArgs'
    _iid_ = Guid('{15969bf0-9028-5722-8a37-7d7c34b41dd6}')
    @winrt_commethod(6)
    def GetCurrentPrintDeviceCapabilities(self) -> Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_commethod(7)
    def UpdatePrintDeviceCapabilities(self, updatedPdc: Windows.Data.Xml.Dom.XmlDocument) -> Void: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
class IPrintSupportPrintDeviceCapabilitiesChangedEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesChangedEventArgs2'
    _iid_ = Guid('{469df9e7-fd07-5eeb-a07d-9fcc67f089ba}')
    @winrt_commethod(6)
    def SetSupportedPdlPassthroughContentTypes(self, supportedPdlContentTypes: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Void: ...
    @winrt_commethod(7)
    def get_ResourceLanguage(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetCurrentPrintDeviceResources(self) -> Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_commethod(9)
    def UpdatePrintDeviceResources(self, updatedPdr: Windows.Data.Xml.Dom.XmlDocument) -> Void: ...
    @winrt_commethod(10)
    def SetPrintDeviceCapabilitiesUpdatePolicy(self, updatePolicy: Windows.Graphics.Printing.PrintSupport.PrintSupportPrintDeviceCapabilitiesUpdatePolicy) -> Void: ...
    ResourceLanguage = property(get_ResourceLanguage, None)
class IPrintSupportPrintDeviceCapabilitiesUpdatePolicy(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesUpdatePolicy'
    _iid_ = Guid('{5f5fc025-8c35-5529-8038-8cdc3634bbcd}')
class IPrintSupportPrintDeviceCapabilitiesUpdatePolicyStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesUpdatePolicyStatics'
    _iid_ = Guid('{3d9e1a70-7c39-551f-aa1f-f8ca35b3119e}')
    @winrt_commethod(6)
    def CreatePeriodicRefresh(self, updatePeriod: Windows.Foundation.TimeSpan) -> Windows.Graphics.Printing.PrintSupport.PrintSupportPrintDeviceCapabilitiesUpdatePolicy: ...
    @winrt_commethod(7)
    def CreatePrintJobRefresh(self, numberOfJobs: UInt32) -> Windows.Graphics.Printing.PrintSupport.PrintSupportPrintDeviceCapabilitiesUpdatePolicy: ...
class IPrintSupportPrintTicketElement(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintTicketValidationRequestedEventArgs'
    _iid_ = Guid('{338e4e69-db55-55c7-8338-ef64680a8f90}')
    @winrt_commethod(6)
    def get_PrintTicket(self) -> Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket: ...
    @winrt_commethod(7)
    def SetPrintTicketValidationStatus(self, status: Windows.Graphics.Printing.PrintSupport.WorkflowPrintTicketValidationStatus) -> Void: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    PrintTicket = property(get_PrintTicket, None)
class IPrintSupportPrinterSelectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.IPrintSupportPrinterSelectedEventArgs'
    _iid_ = Guid('{7b1cb7d9-a8a4-5c09-adb2-66165f817977}')
    @winrt_commethod(6)
    def get_SourceAppInfo(self) -> Windows.ApplicationModel.AppInfo: ...
    @winrt_commethod(7)
    def get_PrintTicket(self) -> Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket: ...
    @winrt_commethod(8)
    def put_PrintTicket(self, value: Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket) -> Void: ...
    @winrt_commethod(9)
    def SetAdditionalFeatures(self, features: Windows.Foundation.Collections.IIterable[Windows.Graphics.Printing.PrintSupport.PrintSupportPrintTicketElement]) -> Void: ...
    @winrt_commethod(10)
    def SetAdditionalParameters(self, parameters: Windows.Foundation.Collections.IIterable[Windows.Graphics.Printing.PrintSupport.PrintSupportPrintTicketElement]) -> Void: ...
    @winrt_commethod(11)
    def get_AllowedAdditionalFeaturesAndParametersCount(self) -> UInt32: ...
    @winrt_commethod(12)
    def SetAdaptiveCard(self, adaptiveCard: Windows.UI.Shell.IAdaptiveCard) -> Void: ...
    @winrt_commethod(13)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    SourceAppInfo = property(get_SourceAppInfo, None)
    PrintTicket = property(get_PrintTicket, put_PrintTicket)
    AllowedAdditionalFeaturesAndParametersCount = property(get_AllowedAdditionalFeaturesAndParametersCount, None)
class IPrintSupportSessionInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.IPrintSupportSessionInfo'
    _iid_ = Guid('{852149af-777d-53e9-9ee9-45d3f4b5be9c}')
    @winrt_commethod(6)
    def get_SourceAppInfo(self) -> Windows.ApplicationModel.AppInfo: ...
    @winrt_commethod(7)
    def get_Printer(self) -> Windows.Devices.Printers.IppPrintDevice: ...
    SourceAppInfo = property(get_SourceAppInfo, None)
    Printer = property(get_Printer, None)
class IPrintSupportSettingsActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.IPrintSupportSettingsActivatedEventArgs'
    _iid_ = Guid('{1e1b565e-a013-55ea-9b8c-eea39d9fb6c1}')
    @winrt_commethod(6)
    def get_Session(self) -> Windows.Graphics.Printing.PrintSupport.PrintSupportSettingsUISession: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Session = property(get_Session, None)
class IPrintSupportSettingsUISession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.IPrintSupportSettingsUISession'
    _iid_ = Guid('{c6da2251-83c3-55e4-a0f8-5de8b062adbf}')
    @winrt_commethod(6)
    def get_SessionPrintTicket(self) -> Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket: ...
    @winrt_commethod(7)
    def get_DocumentTitle(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_LaunchKind(self) -> Windows.Graphics.Printing.PrintSupport.SettingsLaunchKind: ...
    @winrt_commethod(9)
    def UpdatePrintTicket(self, printTicket: Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket) -> Void: ...
    @winrt_commethod(10)
    def get_SessionInfo(self) -> Windows.Graphics.Printing.PrintSupport.PrintSupportSessionInfo: ...
    SessionPrintTicket = property(get_SessionPrintTicket, None)
    DocumentTitle = property(get_DocumentTitle, None)
    LaunchKind = property(get_LaunchKind, None)
    SessionInfo = property(get_SessionInfo, None)
class PrintSupportExtensionSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionSession
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.PrintSupportExtensionSession'
    @winrt_mixinmethod
    def get_Printer(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionSession) -> Windows.Devices.Printers.IppPrintDevice: ...
    @winrt_mixinmethod
    def add_PrintTicketValidationRequested(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionSession, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Printing.PrintSupport.PrintSupportExtensionSession, Windows.Graphics.Printing.PrintSupport.PrintSupportPrintTicketValidationRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PrintTicketValidationRequested(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PrintDeviceCapabilitiesChanged(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionSession, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Printing.PrintSupport.PrintSupportExtensionSession, Windows.Graphics.Printing.PrintSupport.PrintSupportPrintDeviceCapabilitiesChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PrintDeviceCapabilitiesChanged(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Start(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionSession) -> Void: ...
    @winrt_mixinmethod
    def add_PrinterSelected(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionSession2, handler: Windows.Foundation.TypedEventHandler[Windows.Graphics.Printing.PrintSupport.PrintSupportExtensionSession, Windows.Graphics.Printing.PrintSupport.PrintSupportPrinterSelectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PrinterSelected(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionSession2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Printer = property(get_Printer, None)
class PrintSupportExtensionTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionTriggerDetails
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.PrintSupportExtensionTriggerDetails'
    @winrt_mixinmethod
    def get_Session(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportExtensionTriggerDetails) -> Windows.Graphics.Printing.PrintSupport.PrintSupportExtensionSession: ...
    Session = property(get_Session, None)
class PrintSupportPrintDeviceCapabilitiesChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesChangedEventArgs
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.PrintSupportPrintDeviceCapabilitiesChangedEventArgs'
    @winrt_mixinmethod
    def GetCurrentPrintDeviceCapabilities(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesChangedEventArgs) -> Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_mixinmethod
    def UpdatePrintDeviceCapabilities(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesChangedEventArgs, updatedPdc: Windows.Data.Xml.Dom.XmlDocument) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesChangedEventArgs) -> Windows.Foundation.Deferral: ...
    @winrt_mixinmethod
    def SetSupportedPdlPassthroughContentTypes(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesChangedEventArgs2, supportedPdlContentTypes: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Void: ...
    @winrt_mixinmethod
    def get_ResourceLanguage(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesChangedEventArgs2) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetCurrentPrintDeviceResources(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesChangedEventArgs2) -> Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_mixinmethod
    def UpdatePrintDeviceResources(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesChangedEventArgs2, updatedPdr: Windows.Data.Xml.Dom.XmlDocument) -> Void: ...
    @winrt_mixinmethod
    def SetPrintDeviceCapabilitiesUpdatePolicy(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesChangedEventArgs2, updatePolicy: Windows.Graphics.Printing.PrintSupport.PrintSupportPrintDeviceCapabilitiesUpdatePolicy) -> Void: ...
    ResourceLanguage = property(get_ResourceLanguage, None)
class PrintSupportPrintDeviceCapabilitiesUpdatePolicy(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesUpdatePolicy
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.PrintSupportPrintDeviceCapabilitiesUpdatePolicy'
    @winrt_classmethod
    def CreatePeriodicRefresh(cls: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesUpdatePolicyStatics, updatePeriod: Windows.Foundation.TimeSpan) -> Windows.Graphics.Printing.PrintSupport.PrintSupportPrintDeviceCapabilitiesUpdatePolicy: ...
    @winrt_classmethod
    def CreatePrintJobRefresh(cls: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintDeviceCapabilitiesUpdatePolicyStatics, numberOfJobs: UInt32) -> Windows.Graphics.Printing.PrintSupport.PrintSupportPrintDeviceCapabilitiesUpdatePolicy: ...
class PrintSupportPrintTicketElement(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintTicketElement
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.PrintSupportPrintTicketElement'
    @winrt_activatemethod
    def New(cls) -> Windows.Graphics.Printing.PrintSupport.PrintSupportPrintTicketElement: ...
    @winrt_mixinmethod
    def get_LocalName(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintTicketElement) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_LocalName(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintTicketElement, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_NamespaceUri(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintTicketElement) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NamespaceUri(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintTicketElement, value: WinRT_String) -> Void: ...
    LocalName = property(get_LocalName, put_LocalName)
    NamespaceUri = property(get_NamespaceUri, put_NamespaceUri)
class PrintSupportPrintTicketValidationRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintTicketValidationRequestedEventArgs
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.PrintSupportPrintTicketValidationRequestedEventArgs'
    @winrt_mixinmethod
    def get_PrintTicket(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintTicketValidationRequestedEventArgs) -> Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket: ...
    @winrt_mixinmethod
    def SetPrintTicketValidationStatus(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintTicketValidationRequestedEventArgs, status: Windows.Graphics.Printing.PrintSupport.WorkflowPrintTicketValidationStatus) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrintTicketValidationRequestedEventArgs) -> Windows.Foundation.Deferral: ...
    PrintTicket = property(get_PrintTicket, None)
class PrintSupportPrinterSelectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrinterSelectedEventArgs
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.PrintSupportPrinterSelectedEventArgs'
    @winrt_mixinmethod
    def get_SourceAppInfo(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrinterSelectedEventArgs) -> Windows.ApplicationModel.AppInfo: ...
    @winrt_mixinmethod
    def get_PrintTicket(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrinterSelectedEventArgs) -> Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket: ...
    @winrt_mixinmethod
    def put_PrintTicket(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrinterSelectedEventArgs, value: Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket) -> Void: ...
    @winrt_mixinmethod
    def SetAdditionalFeatures(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrinterSelectedEventArgs, features: Windows.Foundation.Collections.IIterable[Windows.Graphics.Printing.PrintSupport.PrintSupportPrintTicketElement]) -> Void: ...
    @winrt_mixinmethod
    def SetAdditionalParameters(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrinterSelectedEventArgs, parameters: Windows.Foundation.Collections.IIterable[Windows.Graphics.Printing.PrintSupport.PrintSupportPrintTicketElement]) -> Void: ...
    @winrt_mixinmethod
    def get_AllowedAdditionalFeaturesAndParametersCount(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrinterSelectedEventArgs) -> UInt32: ...
    @winrt_mixinmethod
    def SetAdaptiveCard(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrinterSelectedEventArgs, adaptiveCard: Windows.UI.Shell.IAdaptiveCard) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportPrinterSelectedEventArgs) -> Windows.Foundation.Deferral: ...
    SourceAppInfo = property(get_SourceAppInfo, None)
    PrintTicket = property(get_PrintTicket, put_PrintTicket)
    AllowedAdditionalFeaturesAndParametersCount = property(get_AllowedAdditionalFeaturesAndParametersCount, None)
class PrintSupportSessionInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.PrintSupport.IPrintSupportSessionInfo
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.PrintSupportSessionInfo'
    @winrt_mixinmethod
    def get_SourceAppInfo(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportSessionInfo) -> Windows.ApplicationModel.AppInfo: ...
    @winrt_mixinmethod
    def get_Printer(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportSessionInfo) -> Windows.Devices.Printers.IppPrintDevice: ...
    SourceAppInfo = property(get_SourceAppInfo, None)
    Printer = property(get_Printer, None)
class PrintSupportSettingsActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.PrintSupport.IPrintSupportSettingsActivatedEventArgs
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.PrintSupportSettingsActivatedEventArgs'
    @winrt_mixinmethod
    def get_Session(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportSettingsActivatedEventArgs) -> Windows.Graphics.Printing.PrintSupport.PrintSupportSettingsUISession: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportSettingsActivatedEventArgs) -> Windows.Foundation.Deferral: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    Session = property(get_Session, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class PrintSupportSettingsUISession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Printing.PrintSupport.IPrintSupportSettingsUISession
    _classid_ = 'Windows.Graphics.Printing.PrintSupport.PrintSupportSettingsUISession'
    @winrt_mixinmethod
    def get_SessionPrintTicket(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportSettingsUISession) -> Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket: ...
    @winrt_mixinmethod
    def get_DocumentTitle(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportSettingsUISession) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LaunchKind(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportSettingsUISession) -> Windows.Graphics.Printing.PrintSupport.SettingsLaunchKind: ...
    @winrt_mixinmethod
    def UpdatePrintTicket(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportSettingsUISession, printTicket: Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket) -> Void: ...
    @winrt_mixinmethod
    def get_SessionInfo(self: Windows.Graphics.Printing.PrintSupport.IPrintSupportSettingsUISession) -> Windows.Graphics.Printing.PrintSupport.PrintSupportSessionInfo: ...
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
make_head(_module, 'IPrintSupportExtensionSession')
make_head(_module, 'IPrintSupportExtensionSession2')
make_head(_module, 'IPrintSupportExtensionTriggerDetails')
make_head(_module, 'IPrintSupportPrintDeviceCapabilitiesChangedEventArgs')
make_head(_module, 'IPrintSupportPrintDeviceCapabilitiesChangedEventArgs2')
make_head(_module, 'IPrintSupportPrintDeviceCapabilitiesUpdatePolicy')
make_head(_module, 'IPrintSupportPrintDeviceCapabilitiesUpdatePolicyStatics')
make_head(_module, 'IPrintSupportPrintTicketElement')
make_head(_module, 'IPrintSupportPrintTicketValidationRequestedEventArgs')
make_head(_module, 'IPrintSupportPrinterSelectedEventArgs')
make_head(_module, 'IPrintSupportSessionInfo')
make_head(_module, 'IPrintSupportSettingsActivatedEventArgs')
make_head(_module, 'IPrintSupportSettingsUISession')
make_head(_module, 'PrintSupportExtensionSession')
make_head(_module, 'PrintSupportExtensionTriggerDetails')
make_head(_module, 'PrintSupportPrintDeviceCapabilitiesChangedEventArgs')
make_head(_module, 'PrintSupportPrintDeviceCapabilitiesUpdatePolicy')
make_head(_module, 'PrintSupportPrintTicketElement')
make_head(_module, 'PrintSupportPrintTicketValidationRequestedEventArgs')
make_head(_module, 'PrintSupportPrinterSelectedEventArgs')
make_head(_module, 'PrintSupportSessionInfo')
make_head(_module, 'PrintSupportSettingsActivatedEventArgs')
make_head(_module, 'PrintSupportSettingsUISession')
