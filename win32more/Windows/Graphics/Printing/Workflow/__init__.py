from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.ApplicationModel.Activation
import win32more.Windows.Devices.Printers
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Graphics.Printing.PrintTicket
import win32more.Windows.Graphics.Printing.Workflow
import win32more.Windows.Storage
import win32more.Windows.Storage.Streams
import win32more.Windows.System
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IPrintWorkflowBackgroundSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowBackgroundSession'
    _iid_ = Guid('{5b7913ba-0c5e-528a-7458-86a46cbddc45}')
    @winrt_commethod(6)
    def add_SetupRequested(self, setupEventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowBackgroundSession, win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowBackgroundSetupRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SetupRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Submitted(self, submittedEventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowBackgroundSession, win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowSubmittedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Submitted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_Status(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowSessionStatus: ...
    @winrt_commethod(11)
    def Start(self) -> Void: ...
    Status = property(get_Status, None)
class IPrintWorkflowBackgroundSetupRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowBackgroundSetupRequestedEventArgs'
    _iid_ = Guid('{43e97342-1750-59c9-61fb-383748a20362}')
    @winrt_commethod(6)
    def GetUserPrintTicketAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket]: ...
    @winrt_commethod(7)
    def get_Configuration(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowConfiguration: ...
    @winrt_commethod(8)
    def SetRequiresUI(self) -> Void: ...
    @winrt_commethod(9)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Configuration = property(get_Configuration, None)
class IPrintWorkflowConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowConfiguration'
    _iid_ = Guid('{d0aac4ed-fd4b-5df5-4bb6-8d0d159ebe3f}')
    @winrt_commethod(6)
    def get_SourceAppDisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_JobTitle(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_SessionId(self) -> WinRT_String: ...
    SourceAppDisplayName = property(get_SourceAppDisplayName, None)
    JobTitle = property(get_JobTitle, None)
    SessionId = property(get_SessionId, None)
class IPrintWorkflowConfiguration2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowConfiguration2'
    _iid_ = Guid('{de350a50-a6d4-5be2-8b9a-09d3d39ea780}')
    @winrt_commethod(6)
    def AbortPrintFlow(self, reason: win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowJobAbortReason) -> Void: ...
class IPrintWorkflowForegroundSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowForegroundSession'
    _iid_ = Guid('{c79b63d0-f8ec-4ceb-953a-c8876157dd33}')
    @winrt_commethod(6)
    def add_SetupRequested(self, setupEventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowForegroundSession, win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowForegroundSetupRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SetupRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_XpsDataAvailable(self, xpsDataAvailableEventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowForegroundSession, win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowXpsDataAvailableEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_XpsDataAvailable(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_Status(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowSessionStatus: ...
    @winrt_commethod(11)
    def Start(self) -> Void: ...
    Status = property(get_Status, None)
class IPrintWorkflowForegroundSetupRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowForegroundSetupRequestedEventArgs'
    _iid_ = Guid('{bbe38247-9c1b-4dd3-9b2b-c80468d941b3}')
    @winrt_commethod(6)
    def GetUserPrintTicketAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket]: ...
    @winrt_commethod(7)
    def get_Configuration(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowConfiguration: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Configuration = property(get_Configuration, None)
class IPrintWorkflowJobActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowJobActivatedEventArgs'
    _iid_ = Guid('{d4bd5e6d-034e-5e00-a616-f961a033dcc8}')
    @winrt_commethod(6)
    def get_Session(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowJobUISession: ...
    Session = property(get_Session, None)
class IPrintWorkflowJobBackgroundSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowJobBackgroundSession'
    _iid_ = Guid('{c5ec6ad8-20c9-5d51-8507-2734b46f96c5}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowSessionStatus: ...
    @winrt_commethod(7)
    def add_JobStarting(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowJobBackgroundSession, win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowJobStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_JobStarting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_PdlModificationRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowJobBackgroundSession, win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPdlModificationRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_PdlModificationRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def Start(self) -> Void: ...
    Status = property(get_Status, None)
class IPrintWorkflowJobNotificationEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowJobNotificationEventArgs'
    _iid_ = Guid('{0ae16fba-5398-5eba-b472-978650186a9a}')
    @winrt_commethod(6)
    def get_Configuration(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowConfiguration: ...
    @winrt_commethod(7)
    def get_PrinterJob(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPrinterJob: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Configuration = property(get_Configuration, None)
    PrinterJob = property(get_PrinterJob, None)
class IPrintWorkflowJobStartingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowJobStartingEventArgs'
    _iid_ = Guid('{e3d99ba8-31ad-5e09-b0d7-601b97f161ad}')
    @winrt_commethod(6)
    def get_Configuration(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowConfiguration: ...
    @winrt_commethod(7)
    def get_Printer(self) -> win32more.Windows.Devices.Printers.IppPrintDevice: ...
    @winrt_commethod(8)
    def SetSkipSystemRendering(self) -> Void: ...
    @winrt_commethod(9)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Configuration = property(get_Configuration, None)
    Printer = property(get_Printer, None)
class IPrintWorkflowJobTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowJobTriggerDetails'
    _iid_ = Guid('{ff296129-60e2-51db-ba8c-e2ccddb516b9}')
    @winrt_commethod(6)
    def get_PrintWorkflowJobSession(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowJobBackgroundSession: ...
    PrintWorkflowJobSession = property(get_PrintWorkflowJobSession, None)
class IPrintWorkflowJobUISession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowJobUISession'
    _iid_ = Guid('{00c8736b-7637-5687-a302-0f664d2aac65}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowSessionStatus: ...
    @winrt_commethod(7)
    def add_PdlDataAvailable(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowJobUISession, win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPdlDataAvailableEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_PdlDataAvailable(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_JobNotification(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowJobUISession, win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowJobNotificationEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_JobNotification(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def Start(self) -> Void: ...
    Status = property(get_Status, None)
class IPrintWorkflowObjectModelSourceFileContent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowObjectModelSourceFileContent'
    _iid_ = Guid('{c36c8a6a-8a2a-419a-b3c3-2090e6bfab2f}')
class IPrintWorkflowObjectModelSourceFileContentFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowObjectModelSourceFileContentFactory'
    _iid_ = Guid('{93b1b903-f013-56d6-b708-99ac2ccb12ee}')
    @winrt_commethod(6)
    def CreateInstance(self, xpsStream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowObjectModelSourceFileContent: ...
class IPrintWorkflowObjectModelTargetPackage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowObjectModelTargetPackage'
    _iid_ = Guid('{7d96bc74-9b54-4ca1-ad3a-979c3d44ddac}')
class IPrintWorkflowPdlConverter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlConverter'
    _iid_ = Guid('{40604b62-0ae4-51f1-818f-731dc0b005ab}')
    @winrt_commethod(6)
    def ConvertPdlAsync(self, printTicket: win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket, inputStream: win32more.Windows.Storage.Streams.IInputStream, outputStream: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncAction: ...
class IPrintWorkflowPdlConverter2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlConverter2'
    _iid_ = Guid('{854ceec1-7837-5b93-b7af-57a6998c2f71}')
    @winrt_commethod(6)
    def ConvertPdlAsync(self, printTicket: win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket, inputStream: win32more.Windows.Storage.Streams.IInputStream, outputStream: win32more.Windows.Storage.Streams.IOutputStream, hostBasedProcessingOperations: win32more.Windows.Graphics.Printing.Workflow.PdlConversionHostBasedProcessingOperations) -> win32more.Windows.Foundation.IAsyncAction: ...
class IPrintWorkflowPdlDataAvailableEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlDataAvailableEventArgs'
    _iid_ = Guid('{d4ad6b50-1547-5991-a0ef-e2ee20211518}')
    @winrt_commethod(6)
    def get_Configuration(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowConfiguration: ...
    @winrt_commethod(7)
    def get_PrinterJob(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPrinterJob: ...
    @winrt_commethod(8)
    def get_SourceContent(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPdlSourceContent: ...
    @winrt_commethod(9)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Configuration = property(get_Configuration, None)
    PrinterJob = property(get_PrinterJob, None)
    SourceContent = property(get_SourceContent, None)
class IPrintWorkflowPdlModificationRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlModificationRequestedEventArgs'
    _iid_ = Guid('{1a339a61-2e13-5edd-a707-ceec61d7333b}')
    @winrt_commethod(6)
    def get_Configuration(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowConfiguration: ...
    @winrt_commethod(7)
    def get_PrinterJob(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPrinterJob: ...
    @winrt_commethod(8)
    def get_SourceContent(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPdlSourceContent: ...
    @winrt_commethod(9)
    def get_UILauncher(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowUILauncher: ...
    @winrt_commethod(10)
    def CreateJobOnPrinter(self, targetContentType: WinRT_String) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPdlTargetStream: ...
    @winrt_commethod(11)
    def CreateJobOnPrinterWithAttributes(self, jobAttributes: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Devices.Printers.IppAttributeValue]], targetContentType: WinRT_String) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPdlTargetStream: ...
    @winrt_commethod(12)
    def CreateJobOnPrinterWithAttributesBuffer(self, jobAttributesBuffer: win32more.Windows.Storage.Streams.IBuffer, targetContentType: WinRT_String) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPdlTargetStream: ...
    @winrt_commethod(13)
    def GetPdlConverter(self, conversionType: win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPdlConversionType) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPdlConverter: ...
    @winrt_commethod(14)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Configuration = property(get_Configuration, None)
    PrinterJob = property(get_PrinterJob, None)
    SourceContent = property(get_SourceContent, None)
    UILauncher = property(get_UILauncher, None)
class IPrintWorkflowPdlModificationRequestedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlModificationRequestedEventArgs2'
    _iid_ = Guid('{8d692147-6c62-5e31-a0e7-d49f92c111c0}')
    @winrt_commethod(6)
    def CreateJobOnPrinterWithAttributes(self, jobAttributes: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Devices.Printers.IppAttributeValue]], targetContentType: WinRT_String, operationAttributes: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Devices.Printers.IppAttributeValue]], jobAttributesMergePolicy: win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowAttributesMergePolicy, operationAttributesMergePolicy: win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowAttributesMergePolicy) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPdlTargetStream: ...
    @winrt_commethod(7)
    def CreateJobOnPrinterWithAttributesBuffer(self, jobAttributesBuffer: win32more.Windows.Storage.Streams.IBuffer, targetContentType: WinRT_String, operationAttributesBuffer: win32more.Windows.Storage.Streams.IBuffer, jobAttributesMergePolicy: win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowAttributesMergePolicy, operationAttributesMergePolicy: win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowAttributesMergePolicy) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPdlTargetStream: ...
class IPrintWorkflowPdlSourceContent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlSourceContent'
    _iid_ = Guid('{92f7fc41-32b8-56ab-845e-b1e68b3aedd5}')
    @winrt_commethod(6)
    def get_ContentType(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetInputStream(self) -> win32more.Windows.Storage.Streams.IInputStream: ...
    @winrt_commethod(8)
    def GetContentFileAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    ContentType = property(get_ContentType, None)
class IPrintWorkflowPdlTargetStream(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlTargetStream'
    _iid_ = Guid('{a742dfe5-1ee3-52a9-9f9f-2e2043180fd1}')
    @winrt_commethod(6)
    def GetOutputStream(self) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    @winrt_commethod(7)
    def CompleteStreamSubmission(self, status: win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowSubmittedStatus) -> Void: ...
class IPrintWorkflowPrinterJob(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowPrinterJob'
    _iid_ = Guid('{12009f94-0d14-5443-bc09-250311ce570b}')
    @winrt_commethod(6)
    def get_JobId(self) -> Int32: ...
    @winrt_commethod(7)
    def get_Printer(self) -> win32more.Windows.Devices.Printers.IppPrintDevice: ...
    @winrt_commethod(8)
    def GetJobStatus(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPrinterJobStatus: ...
    @winrt_commethod(9)
    def GetJobPrintTicket(self) -> win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket: ...
    @winrt_commethod(10)
    def GetJobAttributesAsBuffer(self, attributeNames: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(11)
    def GetJobAttributes(self, attributeNames: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Devices.Printers.IppAttributeValue]: ...
    @winrt_commethod(12)
    def SetJobAttributesFromBuffer(self, jobAttributesBuffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Devices.Printers.IppSetAttributesResult: ...
    @winrt_commethod(13)
    def SetJobAttributes(self, jobAttributes: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Devices.Printers.IppAttributeValue]]) -> win32more.Windows.Devices.Printers.IppSetAttributesResult: ...
    JobId = property(get_JobId, None)
    Printer = property(get_Printer, None)
class IPrintWorkflowSourceContent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowSourceContent'
    _iid_ = Guid('{1a28c641-ceb1-4533-bb73-fbe63eefdb18}')
    @winrt_commethod(6)
    def GetJobPrintTicketAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket]: ...
    @winrt_commethod(7)
    def GetSourceSpoolDataAsStreamContent(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowSpoolStreamContent: ...
    @winrt_commethod(8)
    def GetSourceSpoolDataAsXpsObjectModel(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowObjectModelSourceFileContent: ...
class IPrintWorkflowSpoolStreamContent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowSpoolStreamContent'
    _iid_ = Guid('{72e55ece-e406-4b74-84e1-3ff3fdcdaf70}')
    @winrt_commethod(6)
    def GetInputStream(self) -> win32more.Windows.Storage.Streams.IInputStream: ...
class IPrintWorkflowStreamTarget(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowStreamTarget'
    _iid_ = Guid('{b23bba84-8565-488b-9839-1c9e7c7aa916}')
    @winrt_commethod(6)
    def GetOutputStream(self) -> win32more.Windows.Storage.Streams.IOutputStream: ...
class IPrintWorkflowSubmittedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowSubmittedEventArgs'
    _iid_ = Guid('{3add0a41-3794-5569-5c87-40e8ff720f83}')
    @winrt_commethod(6)
    def get_Operation(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowSubmittedOperation: ...
    @winrt_commethod(7)
    def GetTarget(self, jobPrintTicket: win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowTarget: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Operation = property(get_Operation, None)
class IPrintWorkflowSubmittedOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowSubmittedOperation'
    _iid_ = Guid('{2e4e6216-3be1-5f0f-5c81-a5a2bd4eab0e}')
    @winrt_commethod(6)
    def Complete(self, status: win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowSubmittedStatus) -> Void: ...
    @winrt_commethod(7)
    def get_Configuration(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowConfiguration: ...
    @winrt_commethod(8)
    def get_XpsContent(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowSourceContent: ...
    Configuration = property(get_Configuration, None)
    XpsContent = property(get_XpsContent, None)
class IPrintWorkflowTarget(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowTarget'
    _iid_ = Guid('{29da276c-0a73-5aed-4f3d-970d3251f057}')
    @winrt_commethod(6)
    def get_TargetAsStream(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowStreamTarget: ...
    @winrt_commethod(7)
    def get_TargetAsXpsObjectModelPackage(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowObjectModelTargetPackage: ...
    TargetAsStream = property(get_TargetAsStream, None)
    TargetAsXpsObjectModelPackage = property(get_TargetAsXpsObjectModelPackage, None)
class IPrintWorkflowTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowTriggerDetails'
    _iid_ = Guid('{5739d868-9d86-4052-b0cb-f310becd59bb}')
    @winrt_commethod(6)
    def get_PrintWorkflowSession(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowBackgroundSession: ...
    PrintWorkflowSession = property(get_PrintWorkflowSession, None)
class IPrintWorkflowUIActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowUIActivatedEventArgs'
    _iid_ = Guid('{bc8a844d-09eb-5746-72a6-8dc8b5edbe9b}')
    @winrt_commethod(6)
    def get_PrintWorkflowSession(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowForegroundSession: ...
    PrintWorkflowSession = property(get_PrintWorkflowSession, None)
class IPrintWorkflowUILauncher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowUILauncher'
    _iid_ = Guid('{64e9e22f-14cc-5828-96fb-39163fb6c378}')
    @winrt_commethod(6)
    def IsUILaunchEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def LaunchAndCompleteUIAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowUICompletionStatus]: ...
class IPrintWorkflowXpsDataAvailableEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.Workflow.IPrintWorkflowXpsDataAvailableEventArgs'
    _iid_ = Guid('{4d11c331-54d1-434e-be0e-82c5fa58e5b2}')
    @winrt_commethod(6)
    def get_Operation(self) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowSubmittedOperation: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Operation = property(get_Operation, None)
PdlConversionHostBasedProcessingOperations = UInt32
PdlConversionHostBasedProcessingOperations_None: PdlConversionHostBasedProcessingOperations = 0
PdlConversionHostBasedProcessingOperations_PageRotation: PdlConversionHostBasedProcessingOperations = 1
PdlConversionHostBasedProcessingOperations_PageOrdering: PdlConversionHostBasedProcessingOperations = 2
PdlConversionHostBasedProcessingOperations_Copies: PdlConversionHostBasedProcessingOperations = 4
PdlConversionHostBasedProcessingOperations_BlankPageInsertion: PdlConversionHostBasedProcessingOperations = 8
PdlConversionHostBasedProcessingOperations_All: PdlConversionHostBasedProcessingOperations = 4294967295
PrintWorkflowAttributesMergePolicy = Int32
PrintWorkflowAttributesMergePolicy_MergePreferPrintTicketOnConflict: PrintWorkflowAttributesMergePolicy = 0
PrintWorkflowAttributesMergePolicy_MergePreferPsaOnConflict: PrintWorkflowAttributesMergePolicy = 1
PrintWorkflowAttributesMergePolicy_DoNotMergeWithPrintTicket: PrintWorkflowAttributesMergePolicy = 2
class PrintWorkflowBackgroundSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowBackgroundSession
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowBackgroundSession'
    @winrt_mixinmethod
    def add_SetupRequested(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowBackgroundSession, setupEventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowBackgroundSession, win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowBackgroundSetupRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SetupRequested(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowBackgroundSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Submitted(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowBackgroundSession, submittedEventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowBackgroundSession, win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowSubmittedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Submitted(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowBackgroundSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowBackgroundSession) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowSessionStatus: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowBackgroundSession) -> Void: ...
    Status = property(get_Status, None)
class PrintWorkflowBackgroundSetupRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowBackgroundSetupRequestedEventArgs
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowBackgroundSetupRequestedEventArgs'
    @winrt_mixinmethod
    def GetUserPrintTicketAsync(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowBackgroundSetupRequestedEventArgs) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket]: ...
    @winrt_mixinmethod
    def get_Configuration(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowBackgroundSetupRequestedEventArgs) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowConfiguration: ...
    @winrt_mixinmethod
    def SetRequiresUI(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowBackgroundSetupRequestedEventArgs) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowBackgroundSetupRequestedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Configuration = property(get_Configuration, None)
class PrintWorkflowConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowConfiguration
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowConfiguration'
    @winrt_mixinmethod
    def AbortPrintFlow(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowConfiguration2, reason: win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowJobAbortReason) -> Void: ...
    @winrt_mixinmethod
    def get_SourceAppDisplayName(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_JobTitle(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SessionId(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowConfiguration) -> WinRT_String: ...
    SourceAppDisplayName = property(get_SourceAppDisplayName, None)
    JobTitle = property(get_JobTitle, None)
    SessionId = property(get_SessionId, None)
class PrintWorkflowForegroundSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowForegroundSession
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowForegroundSession'
    @winrt_mixinmethod
    def add_SetupRequested(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowForegroundSession, setupEventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowForegroundSession, win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowForegroundSetupRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SetupRequested(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowForegroundSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_XpsDataAvailable(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowForegroundSession, xpsDataAvailableEventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowForegroundSession, win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowXpsDataAvailableEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_XpsDataAvailable(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowForegroundSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowForegroundSession) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowSessionStatus: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowForegroundSession) -> Void: ...
    Status = property(get_Status, None)
class PrintWorkflowForegroundSetupRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowForegroundSetupRequestedEventArgs
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowForegroundSetupRequestedEventArgs'
    @winrt_mixinmethod
    def GetUserPrintTicketAsync(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowForegroundSetupRequestedEventArgs) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket]: ...
    @winrt_mixinmethod
    def get_Configuration(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowForegroundSetupRequestedEventArgs) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowConfiguration: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowForegroundSetupRequestedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Configuration = property(get_Configuration, None)
PrintWorkflowJobAbortReason = Int32
PrintWorkflowJobAbortReason_JobFailed: PrintWorkflowJobAbortReason = 0
PrintWorkflowJobAbortReason_UserCanceled: PrintWorkflowJobAbortReason = 1
class PrintWorkflowJobActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowJobActivatedEventArgs
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowJobActivatedEventArgs'
    @winrt_mixinmethod
    def get_Session(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowJobActivatedEventArgs) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowJobUISession: ...
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
class PrintWorkflowJobBackgroundSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowJobBackgroundSession
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowJobBackgroundSession'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowJobBackgroundSession) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowSessionStatus: ...
    @winrt_mixinmethod
    def add_JobStarting(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowJobBackgroundSession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowJobBackgroundSession, win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowJobStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_JobStarting(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowJobBackgroundSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PdlModificationRequested(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowJobBackgroundSession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowJobBackgroundSession, win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPdlModificationRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PdlModificationRequested(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowJobBackgroundSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowJobBackgroundSession) -> Void: ...
    Status = property(get_Status, None)
class PrintWorkflowJobNotificationEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowJobNotificationEventArgs
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowJobNotificationEventArgs'
    @winrt_mixinmethod
    def get_Configuration(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowJobNotificationEventArgs) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowConfiguration: ...
    @winrt_mixinmethod
    def get_PrinterJob(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowJobNotificationEventArgs) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPrinterJob: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowJobNotificationEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Configuration = property(get_Configuration, None)
    PrinterJob = property(get_PrinterJob, None)
class PrintWorkflowJobStartingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowJobStartingEventArgs
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowJobStartingEventArgs'
    @winrt_mixinmethod
    def get_Configuration(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowJobStartingEventArgs) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowConfiguration: ...
    @winrt_mixinmethod
    def get_Printer(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowJobStartingEventArgs) -> win32more.Windows.Devices.Printers.IppPrintDevice: ...
    @winrt_mixinmethod
    def SetSkipSystemRendering(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowJobStartingEventArgs) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowJobStartingEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Configuration = property(get_Configuration, None)
    Printer = property(get_Printer, None)
class PrintWorkflowJobTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowJobTriggerDetails
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowJobTriggerDetails'
    @winrt_mixinmethod
    def get_PrintWorkflowJobSession(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowJobTriggerDetails) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowJobBackgroundSession: ...
    PrintWorkflowJobSession = property(get_PrintWorkflowJobSession, None)
class PrintWorkflowJobUISession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowJobUISession
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowJobUISession'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowJobUISession) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowSessionStatus: ...
    @winrt_mixinmethod
    def add_PdlDataAvailable(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowJobUISession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowJobUISession, win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPdlDataAvailableEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PdlDataAvailable(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowJobUISession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_JobNotification(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowJobUISession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowJobUISession, win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowJobNotificationEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_JobNotification(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowJobUISession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowJobUISession) -> Void: ...
    Status = property(get_Status, None)
class PrintWorkflowObjectModelSourceFileContent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowObjectModelSourceFileContent
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowObjectModelSourceFileContent'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.Graphics.Printing.Workflow.IPrintWorkflowObjectModelSourceFileContentFactory, xpsStream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowObjectModelSourceFileContent: ...
class PrintWorkflowObjectModelTargetPackage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowObjectModelTargetPackage
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowObjectModelTargetPackage'
PrintWorkflowPdlConversionType = Int32
PrintWorkflowPdlConversionType_XpsToPdf: PrintWorkflowPdlConversionType = 0
PrintWorkflowPdlConversionType_XpsToPwgr: PrintWorkflowPdlConversionType = 1
PrintWorkflowPdlConversionType_XpsToPclm: PrintWorkflowPdlConversionType = 2
class PrintWorkflowPdlConverter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlConverter
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowPdlConverter'
    @winrt_mixinmethod
    def ConvertPdlAsync(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlConverter, printTicket: win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket, inputStream: win32more.Windows.Storage.Streams.IInputStream, outputStream: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ConvertPdlAsync_2(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlConverter2, printTicket: win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket, inputStream: win32more.Windows.Storage.Streams.IInputStream, outputStream: win32more.Windows.Storage.Streams.IOutputStream, hostBasedProcessingOperations: win32more.Windows.Graphics.Printing.Workflow.PdlConversionHostBasedProcessingOperations) -> win32more.Windows.Foundation.IAsyncAction: ...
class PrintWorkflowPdlDataAvailableEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlDataAvailableEventArgs
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowPdlDataAvailableEventArgs'
    @winrt_mixinmethod
    def get_Configuration(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlDataAvailableEventArgs) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowConfiguration: ...
    @winrt_mixinmethod
    def get_PrinterJob(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlDataAvailableEventArgs) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPrinterJob: ...
    @winrt_mixinmethod
    def get_SourceContent(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlDataAvailableEventArgs) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPdlSourceContent: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlDataAvailableEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Configuration = property(get_Configuration, None)
    PrinterJob = property(get_PrinterJob, None)
    SourceContent = property(get_SourceContent, None)
class PrintWorkflowPdlModificationRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlModificationRequestedEventArgs
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowPdlModificationRequestedEventArgs'
    @winrt_mixinmethod
    def get_Configuration(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlModificationRequestedEventArgs) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowConfiguration: ...
    @winrt_mixinmethod
    def get_PrinterJob(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlModificationRequestedEventArgs) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPrinterJob: ...
    @winrt_mixinmethod
    def get_SourceContent(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlModificationRequestedEventArgs) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPdlSourceContent: ...
    @winrt_mixinmethod
    def get_UILauncher(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlModificationRequestedEventArgs) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowUILauncher: ...
    @winrt_mixinmethod
    def CreateJobOnPrinter(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlModificationRequestedEventArgs, targetContentType: WinRT_String) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPdlTargetStream: ...
    @winrt_mixinmethod
    def CreateJobOnPrinterWithAttributes(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlModificationRequestedEventArgs, jobAttributes: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Devices.Printers.IppAttributeValue]], targetContentType: WinRT_String) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPdlTargetStream: ...
    @winrt_mixinmethod
    def CreateJobOnPrinterWithAttributesBuffer(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlModificationRequestedEventArgs, jobAttributesBuffer: win32more.Windows.Storage.Streams.IBuffer, targetContentType: WinRT_String) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPdlTargetStream: ...
    @winrt_mixinmethod
    def GetPdlConverter(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlModificationRequestedEventArgs, conversionType: win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPdlConversionType) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPdlConverter: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlModificationRequestedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    @winrt_mixinmethod
    def CreateJobOnPrinterWithAttributes_2(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlModificationRequestedEventArgs2, jobAttributes: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Devices.Printers.IppAttributeValue]], targetContentType: WinRT_String, operationAttributes: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Devices.Printers.IppAttributeValue]], jobAttributesMergePolicy: win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowAttributesMergePolicy, operationAttributesMergePolicy: win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowAttributesMergePolicy) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPdlTargetStream: ...
    @winrt_mixinmethod
    def CreateJobOnPrinterWithAttributesBuffer_2(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlModificationRequestedEventArgs2, jobAttributesBuffer: win32more.Windows.Storage.Streams.IBuffer, targetContentType: WinRT_String, operationAttributesBuffer: win32more.Windows.Storage.Streams.IBuffer, jobAttributesMergePolicy: win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowAttributesMergePolicy, operationAttributesMergePolicy: win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowAttributesMergePolicy) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPdlTargetStream: ...
    Configuration = property(get_Configuration, None)
    PrinterJob = property(get_PrinterJob, None)
    SourceContent = property(get_SourceContent, None)
    UILauncher = property(get_UILauncher, None)
class PrintWorkflowPdlSourceContent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlSourceContent
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowPdlSourceContent'
    @winrt_mixinmethod
    def get_ContentType(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlSourceContent) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetInputStream(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlSourceContent) -> win32more.Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def GetContentFileAsync(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlSourceContent) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.StorageFile]: ...
    ContentType = property(get_ContentType, None)
class PrintWorkflowPdlTargetStream(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlTargetStream
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowPdlTargetStream'
    @winrt_mixinmethod
    def GetOutputStream(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlTargetStream) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def CompleteStreamSubmission(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPdlTargetStream, status: win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowSubmittedStatus) -> Void: ...
class PrintWorkflowPrinterJob(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPrinterJob
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowPrinterJob'
    @winrt_mixinmethod
    def get_JobId(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPrinterJob) -> Int32: ...
    @winrt_mixinmethod
    def get_Printer(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPrinterJob) -> win32more.Windows.Devices.Printers.IppPrintDevice: ...
    @winrt_mixinmethod
    def GetJobStatus(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPrinterJob) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowPrinterJobStatus: ...
    @winrt_mixinmethod
    def GetJobPrintTicket(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPrinterJob) -> win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket: ...
    @winrt_mixinmethod
    def GetJobAttributesAsBuffer(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPrinterJob, attributeNames: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def GetJobAttributes(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPrinterJob, attributeNames: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Devices.Printers.IppAttributeValue]: ...
    @winrt_mixinmethod
    def SetJobAttributesFromBuffer(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPrinterJob, jobAttributesBuffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Devices.Printers.IppSetAttributesResult: ...
    @winrt_mixinmethod
    def SetJobAttributes(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowPrinterJob, jobAttributes: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Devices.Printers.IppAttributeValue]]) -> win32more.Windows.Devices.Printers.IppSetAttributesResult: ...
    JobId = property(get_JobId, None)
    Printer = property(get_Printer, None)
PrintWorkflowPrinterJobStatus = Int32
PrintWorkflowPrinterJobStatus_Error: PrintWorkflowPrinterJobStatus = 0
PrintWorkflowPrinterJobStatus_Aborted: PrintWorkflowPrinterJobStatus = 1
PrintWorkflowPrinterJobStatus_InProgress: PrintWorkflowPrinterJobStatus = 2
PrintWorkflowPrinterJobStatus_Completed: PrintWorkflowPrinterJobStatus = 3
PrintWorkflowSessionStatus = Int32
PrintWorkflowSessionStatus_Started: PrintWorkflowSessionStatus = 0
PrintWorkflowSessionStatus_Completed: PrintWorkflowSessionStatus = 1
PrintWorkflowSessionStatus_Aborted: PrintWorkflowSessionStatus = 2
PrintWorkflowSessionStatus_Closed: PrintWorkflowSessionStatus = 3
PrintWorkflowSessionStatus_PdlDataAvailableForModification: PrintWorkflowSessionStatus = 4
class PrintWorkflowSourceContent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowSourceContent
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowSourceContent'
    @winrt_mixinmethod
    def GetJobPrintTicketAsync(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowSourceContent) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket]: ...
    @winrt_mixinmethod
    def GetSourceSpoolDataAsStreamContent(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowSourceContent) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowSpoolStreamContent: ...
    @winrt_mixinmethod
    def GetSourceSpoolDataAsXpsObjectModel(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowSourceContent) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowObjectModelSourceFileContent: ...
class PrintWorkflowSpoolStreamContent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowSpoolStreamContent
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowSpoolStreamContent'
    @winrt_mixinmethod
    def GetInputStream(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowSpoolStreamContent) -> win32more.Windows.Storage.Streams.IInputStream: ...
class PrintWorkflowStreamTarget(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowStreamTarget
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowStreamTarget'
    @winrt_mixinmethod
    def GetOutputStream(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowStreamTarget) -> win32more.Windows.Storage.Streams.IOutputStream: ...
class PrintWorkflowSubmittedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowSubmittedEventArgs
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowSubmittedEventArgs'
    @winrt_mixinmethod
    def get_Operation(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowSubmittedEventArgs) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowSubmittedOperation: ...
    @winrt_mixinmethod
    def GetTarget(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowSubmittedEventArgs, jobPrintTicket: win32more.Windows.Graphics.Printing.PrintTicket.WorkflowPrintTicket) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowTarget: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowSubmittedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Operation = property(get_Operation, None)
class PrintWorkflowSubmittedOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowSubmittedOperation
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowSubmittedOperation'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowSubmittedOperation, status: win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowSubmittedStatus) -> Void: ...
    @winrt_mixinmethod
    def get_Configuration(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowSubmittedOperation) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowConfiguration: ...
    @winrt_mixinmethod
    def get_XpsContent(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowSubmittedOperation) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowSourceContent: ...
    Configuration = property(get_Configuration, None)
    XpsContent = property(get_XpsContent, None)
PrintWorkflowSubmittedStatus = Int32
PrintWorkflowSubmittedStatus_Succeeded: PrintWorkflowSubmittedStatus = 0
PrintWorkflowSubmittedStatus_Canceled: PrintWorkflowSubmittedStatus = 1
PrintWorkflowSubmittedStatus_Failed: PrintWorkflowSubmittedStatus = 2
class PrintWorkflowTarget(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowTarget
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowTarget'
    @winrt_mixinmethod
    def get_TargetAsStream(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowTarget) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowStreamTarget: ...
    @winrt_mixinmethod
    def get_TargetAsXpsObjectModelPackage(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowTarget) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowObjectModelTargetPackage: ...
    TargetAsStream = property(get_TargetAsStream, None)
    TargetAsXpsObjectModelPackage = property(get_TargetAsXpsObjectModelPackage, None)
class PrintWorkflowTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowTriggerDetails
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowTriggerDetails'
    @winrt_mixinmethod
    def get_PrintWorkflowSession(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowTriggerDetails) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowBackgroundSession: ...
    PrintWorkflowSession = property(get_PrintWorkflowSession, None)
class PrintWorkflowUIActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowUIActivatedEventArgs
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowUIActivatedEventArgs'
    @winrt_mixinmethod
    def get_PrintWorkflowSession(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowUIActivatedEventArgs) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowForegroundSession: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    PrintWorkflowSession = property(get_PrintWorkflowSession, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
PrintWorkflowUICompletionStatus = Int32
PrintWorkflowUICompletionStatus_Completed: PrintWorkflowUICompletionStatus = 0
PrintWorkflowUICompletionStatus_LaunchFailed: PrintWorkflowUICompletionStatus = 1
PrintWorkflowUICompletionStatus_JobFailed: PrintWorkflowUICompletionStatus = 2
PrintWorkflowUICompletionStatus_UserCanceled: PrintWorkflowUICompletionStatus = 3
class PrintWorkflowUILauncher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowUILauncher
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowUILauncher'
    @winrt_mixinmethod
    def IsUILaunchEnabled(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowUILauncher) -> Boolean: ...
    @winrt_mixinmethod
    def LaunchAndCompleteUIAsync(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowUILauncher) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowUICompletionStatus]: ...
class PrintWorkflowXpsDataAvailableEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowXpsDataAvailableEventArgs
    _classid_ = 'Windows.Graphics.Printing.Workflow.PrintWorkflowXpsDataAvailableEventArgs'
    @winrt_mixinmethod
    def get_Operation(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowXpsDataAvailableEventArgs) -> win32more.Windows.Graphics.Printing.Workflow.PrintWorkflowSubmittedOperation: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Graphics.Printing.Workflow.IPrintWorkflowXpsDataAvailableEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Operation = property(get_Operation, None)
make_head(_module, 'IPrintWorkflowBackgroundSession')
make_head(_module, 'IPrintWorkflowBackgroundSetupRequestedEventArgs')
make_head(_module, 'IPrintWorkflowConfiguration')
make_head(_module, 'IPrintWorkflowConfiguration2')
make_head(_module, 'IPrintWorkflowForegroundSession')
make_head(_module, 'IPrintWorkflowForegroundSetupRequestedEventArgs')
make_head(_module, 'IPrintWorkflowJobActivatedEventArgs')
make_head(_module, 'IPrintWorkflowJobBackgroundSession')
make_head(_module, 'IPrintWorkflowJobNotificationEventArgs')
make_head(_module, 'IPrintWorkflowJobStartingEventArgs')
make_head(_module, 'IPrintWorkflowJobTriggerDetails')
make_head(_module, 'IPrintWorkflowJobUISession')
make_head(_module, 'IPrintWorkflowObjectModelSourceFileContent')
make_head(_module, 'IPrintWorkflowObjectModelSourceFileContentFactory')
make_head(_module, 'IPrintWorkflowObjectModelTargetPackage')
make_head(_module, 'IPrintWorkflowPdlConverter')
make_head(_module, 'IPrintWorkflowPdlConverter2')
make_head(_module, 'IPrintWorkflowPdlDataAvailableEventArgs')
make_head(_module, 'IPrintWorkflowPdlModificationRequestedEventArgs')
make_head(_module, 'IPrintWorkflowPdlModificationRequestedEventArgs2')
make_head(_module, 'IPrintWorkflowPdlSourceContent')
make_head(_module, 'IPrintWorkflowPdlTargetStream')
make_head(_module, 'IPrintWorkflowPrinterJob')
make_head(_module, 'IPrintWorkflowSourceContent')
make_head(_module, 'IPrintWorkflowSpoolStreamContent')
make_head(_module, 'IPrintWorkflowStreamTarget')
make_head(_module, 'IPrintWorkflowSubmittedEventArgs')
make_head(_module, 'IPrintWorkflowSubmittedOperation')
make_head(_module, 'IPrintWorkflowTarget')
make_head(_module, 'IPrintWorkflowTriggerDetails')
make_head(_module, 'IPrintWorkflowUIActivatedEventArgs')
make_head(_module, 'IPrintWorkflowUILauncher')
make_head(_module, 'IPrintWorkflowXpsDataAvailableEventArgs')
make_head(_module, 'PrintWorkflowBackgroundSession')
make_head(_module, 'PrintWorkflowBackgroundSetupRequestedEventArgs')
make_head(_module, 'PrintWorkflowConfiguration')
make_head(_module, 'PrintWorkflowForegroundSession')
make_head(_module, 'PrintWorkflowForegroundSetupRequestedEventArgs')
make_head(_module, 'PrintWorkflowJobActivatedEventArgs')
make_head(_module, 'PrintWorkflowJobBackgroundSession')
make_head(_module, 'PrintWorkflowJobNotificationEventArgs')
make_head(_module, 'PrintWorkflowJobStartingEventArgs')
make_head(_module, 'PrintWorkflowJobTriggerDetails')
make_head(_module, 'PrintWorkflowJobUISession')
make_head(_module, 'PrintWorkflowObjectModelSourceFileContent')
make_head(_module, 'PrintWorkflowObjectModelTargetPackage')
make_head(_module, 'PrintWorkflowPdlConverter')
make_head(_module, 'PrintWorkflowPdlDataAvailableEventArgs')
make_head(_module, 'PrintWorkflowPdlModificationRequestedEventArgs')
make_head(_module, 'PrintWorkflowPdlSourceContent')
make_head(_module, 'PrintWorkflowPdlTargetStream')
make_head(_module, 'PrintWorkflowPrinterJob')
make_head(_module, 'PrintWorkflowSourceContent')
make_head(_module, 'PrintWorkflowSpoolStreamContent')
make_head(_module, 'PrintWorkflowStreamTarget')
make_head(_module, 'PrintWorkflowSubmittedEventArgs')
make_head(_module, 'PrintWorkflowSubmittedOperation')
make_head(_module, 'PrintWorkflowTarget')
make_head(_module, 'PrintWorkflowTriggerDetails')
make_head(_module, 'PrintWorkflowUIActivatedEventArgs')
make_head(_module, 'PrintWorkflowUILauncher')
make_head(_module, 'PrintWorkflowXpsDataAvailableEventArgs')
