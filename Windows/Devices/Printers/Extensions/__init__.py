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
import Windows.Devices.Printers.Extensions
import Windows.Foundation
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
ExtensionsContract: UInt32 = 131072
class IPrint3DWorkflow(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c56f74bd-3669-4a66-ab-42-c8-15-19-30-cd-34')
    @winrt_commethod(6)
    def get_DeviceID(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetPrintModelPackage(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(8)
    def get_IsPrintReady(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsPrintReady(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def add_PrintRequested(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Devices.Printers.Extensions.Print3DWorkflow, Windows.Devices.Printers.Extensions.Print3DWorkflowPrintRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_PrintRequested(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceID = property(get_DeviceID, None)
    IsPrintReady = property(get_IsPrintReady, put_IsPrintReady)
class IPrint3DWorkflow2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a2a6c54f-8ac1-4918-97-41-e3-4f-30-04-23-9e')
    @winrt_commethod(6)
    def add_PrinterChanged(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Devices.Printers.Extensions.Print3DWorkflow, Windows.Devices.Printers.Extensions.Print3DWorkflowPrinterChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PrinterChanged(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IPrint3DWorkflowPrintRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('19f8c858-5ac8-4b55-8a-5f-e6-15-67-da-fb-4d')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Devices.Printers.Extensions.Print3DWorkflowStatus: ...
    @winrt_commethod(7)
    def SetExtendedStatus(self, value: Windows.Devices.Printers.Extensions.Print3DWorkflowDetail) -> Void: ...
    @winrt_commethod(8)
    def SetSource(self, source: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(9)
    def SetSourceChanged(self, value: Boolean) -> Void: ...
    Status = property(get_Status, None)
class IPrint3DWorkflowPrinterChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('45226402-95fc-4847-93-b3-13-4d-bf-5c-60-f7')
    @winrt_commethod(6)
    def get_NewDeviceId(self) -> WinRT_String: ...
    NewDeviceId = property(get_NewDeviceId, None)
class IPrintExtensionContextStatic(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e70d9fc1-ff79-4aa4-8c-9b-0c-93-ae-df-de-8a')
    @winrt_commethod(6)
    def FromDeviceId(self, deviceId: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
class IPrintNotificationEventDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e00e4c8a-4828-4da1-8b-b8-86-72-df-85-15-e7')
    @winrt_commethod(6)
    def get_PrinterName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EventData(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_EventData(self, value: WinRT_String) -> Void: ...
    PrinterName = property(get_PrinterName, None)
    EventData = property(get_EventData, put_EventData)
class IPrintTaskConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e3c22451-3aa4-4885-92-40-31-1f-5f-8f-be-9d')
    @winrt_commethod(6)
    def get_PrinterExtensionContext(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def add_SaveRequested(self, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Devices.Printers.Extensions.PrintTaskConfiguration, Windows.Devices.Printers.Extensions.PrintTaskConfigurationSaveRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_SaveRequested(self, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    PrinterExtensionContext = property(get_PrinterExtensionContext, None)
class IPrintTaskConfigurationSaveRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('eeaf2fcb-621e-4b62-ac-77-b2-81-cc-e0-8d-60')
    @winrt_commethod(6)
    def Cancel(self) -> Void: ...
    @winrt_commethod(7)
    def Save(self, printerExtensionContext: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.Devices.Printers.Extensions.PrintTaskConfigurationSaveRequestedDeferral: ...
    @winrt_commethod(9)
    def get_Deadline(self) -> Windows.Foundation.DateTime: ...
    Deadline = property(get_Deadline, None)
class IPrintTaskConfigurationSaveRequestedDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e959d568-f729-44a4-87-1d-bd-06-28-69-6a-33')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IPrintTaskConfigurationSaveRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e06c2879-0d61-4938-91-d0-96-a4-5b-ee-84-79')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.Devices.Printers.Extensions.PrintTaskConfigurationSaveRequest: ...
    Request = property(get_Request, None)
class Print3DWorkflow(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Printers.Extensions.Print3DWorkflow'
    @winrt_mixinmethod
    def get_DeviceID(self: Windows.Devices.Printers.Extensions.IPrint3DWorkflow) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetPrintModelPackage(self: Windows.Devices.Printers.Extensions.IPrint3DWorkflow) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_IsPrintReady(self: Windows.Devices.Printers.Extensions.IPrint3DWorkflow) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsPrintReady(self: Windows.Devices.Printers.Extensions.IPrint3DWorkflow, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def add_PrintRequested(self: Windows.Devices.Printers.Extensions.IPrint3DWorkflow, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Devices.Printers.Extensions.Print3DWorkflow, Windows.Devices.Printers.Extensions.Print3DWorkflowPrintRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PrintRequested(self: Windows.Devices.Printers.Extensions.IPrint3DWorkflow, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PrinterChanged(self: Windows.Devices.Printers.Extensions.IPrint3DWorkflow2, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Devices.Printers.Extensions.Print3DWorkflow, Windows.Devices.Printers.Extensions.Print3DWorkflowPrinterChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PrinterChanged(self: Windows.Devices.Printers.Extensions.IPrint3DWorkflow2, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceID = property(get_DeviceID, None)
    IsPrintReady = property(get_IsPrintReady, put_IsPrintReady)
Print3DWorkflowDetail = Int32
Print3DWorkflowDetail_Unknown: Print3DWorkflowDetail = 0
Print3DWorkflowDetail_ModelExceedsPrintBed: Print3DWorkflowDetail = 1
Print3DWorkflowDetail_UploadFailed: Print3DWorkflowDetail = 2
Print3DWorkflowDetail_InvalidMaterialSelection: Print3DWorkflowDetail = 3
Print3DWorkflowDetail_InvalidModel: Print3DWorkflowDetail = 4
Print3DWorkflowDetail_ModelNotManifold: Print3DWorkflowDetail = 5
Print3DWorkflowDetail_InvalidPrintTicket: Print3DWorkflowDetail = 6
class Print3DWorkflowPrintRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Printers.Extensions.Print3DWorkflowPrintRequestedEventArgs'
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Printers.Extensions.IPrint3DWorkflowPrintRequestedEventArgs) -> Windows.Devices.Printers.Extensions.Print3DWorkflowStatus: ...
    @winrt_mixinmethod
    def SetExtendedStatus(self: Windows.Devices.Printers.Extensions.IPrint3DWorkflowPrintRequestedEventArgs, value: Windows.Devices.Printers.Extensions.Print3DWorkflowDetail) -> Void: ...
    @winrt_mixinmethod
    def SetSource(self: Windows.Devices.Printers.Extensions.IPrint3DWorkflowPrintRequestedEventArgs, source: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def SetSourceChanged(self: Windows.Devices.Printers.Extensions.IPrint3DWorkflowPrintRequestedEventArgs, value: Boolean) -> Void: ...
    Status = property(get_Status, None)
class Print3DWorkflowPrinterChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Printers.Extensions.Print3DWorkflowPrinterChangedEventArgs'
    @winrt_mixinmethod
    def get_NewDeviceId(self: Windows.Devices.Printers.Extensions.IPrint3DWorkflowPrinterChangedEventArgs) -> WinRT_String: ...
    NewDeviceId = property(get_NewDeviceId, None)
Print3DWorkflowStatus = Int32
Print3DWorkflowStatus_Abandoned: Print3DWorkflowStatus = 0
Print3DWorkflowStatus_Canceled: Print3DWorkflowStatus = 1
Print3DWorkflowStatus_Failed: Print3DWorkflowStatus = 2
Print3DWorkflowStatus_Slicing: Print3DWorkflowStatus = 3
Print3DWorkflowStatus_Submitted: Print3DWorkflowStatus = 4
class PrintExtensionContext(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Printers.Extensions.PrintExtensionContext'
    @winrt_classmethod
    def FromDeviceId(cls: Windows.Devices.Printers.Extensions.IPrintExtensionContextStatic, deviceId: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
class PrintNotificationEventDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Printers.Extensions.PrintNotificationEventDetails'
    @winrt_mixinmethod
    def get_PrinterName(self: Windows.Devices.Printers.Extensions.IPrintNotificationEventDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EventData(self: Windows.Devices.Printers.Extensions.IPrintNotificationEventDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_EventData(self: Windows.Devices.Printers.Extensions.IPrintNotificationEventDetails, value: WinRT_String) -> Void: ...
    PrinterName = property(get_PrinterName, None)
    EventData = property(get_EventData, put_EventData)
class PrintTaskConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Printers.Extensions.PrintTaskConfiguration'
    @winrt_mixinmethod
    def get_PrinterExtensionContext(self: Windows.Devices.Printers.Extensions.IPrintTaskConfiguration) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def add_SaveRequested(self: Windows.Devices.Printers.Extensions.IPrintTaskConfiguration, eventHandler: Windows.Foundation.TypedEventHandler[Windows.Devices.Printers.Extensions.PrintTaskConfiguration, Windows.Devices.Printers.Extensions.PrintTaskConfigurationSaveRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SaveRequested(self: Windows.Devices.Printers.Extensions.IPrintTaskConfiguration, eventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    PrinterExtensionContext = property(get_PrinterExtensionContext, None)
class PrintTaskConfigurationSaveRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Printers.Extensions.PrintTaskConfigurationSaveRequest'
    @winrt_mixinmethod
    def Cancel(self: Windows.Devices.Printers.Extensions.IPrintTaskConfigurationSaveRequest) -> Void: ...
    @winrt_mixinmethod
    def Save(self: Windows.Devices.Printers.Extensions.IPrintTaskConfigurationSaveRequest, printerExtensionContext: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Devices.Printers.Extensions.IPrintTaskConfigurationSaveRequest) -> Windows.Devices.Printers.Extensions.PrintTaskConfigurationSaveRequestedDeferral: ...
    @winrt_mixinmethod
    def get_Deadline(self: Windows.Devices.Printers.Extensions.IPrintTaskConfigurationSaveRequest) -> Windows.Foundation.DateTime: ...
    Deadline = property(get_Deadline, None)
class PrintTaskConfigurationSaveRequestedDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Printers.Extensions.PrintTaskConfigurationSaveRequestedDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.Devices.Printers.Extensions.IPrintTaskConfigurationSaveRequestedDeferral) -> Void: ...
class PrintTaskConfigurationSaveRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Printers.Extensions.PrintTaskConfigurationSaveRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.Devices.Printers.Extensions.IPrintTaskConfigurationSaveRequestedEventArgs) -> Windows.Devices.Printers.Extensions.PrintTaskConfigurationSaveRequest: ...
    Request = property(get_Request, None)
make_head(_module, 'IPrint3DWorkflow')
make_head(_module, 'IPrint3DWorkflow2')
make_head(_module, 'IPrint3DWorkflowPrintRequestedEventArgs')
make_head(_module, 'IPrint3DWorkflowPrinterChangedEventArgs')
make_head(_module, 'IPrintExtensionContextStatic')
make_head(_module, 'IPrintNotificationEventDetails')
make_head(_module, 'IPrintTaskConfiguration')
make_head(_module, 'IPrintTaskConfigurationSaveRequest')
make_head(_module, 'IPrintTaskConfigurationSaveRequestedDeferral')
make_head(_module, 'IPrintTaskConfigurationSaveRequestedEventArgs')
make_head(_module, 'Print3DWorkflow')
make_head(_module, 'Print3DWorkflowPrintRequestedEventArgs')
make_head(_module, 'Print3DWorkflowPrinterChangedEventArgs')
make_head(_module, 'PrintExtensionContext')
make_head(_module, 'PrintNotificationEventDetails')
make_head(_module, 'PrintTaskConfiguration')
make_head(_module, 'PrintTaskConfigurationSaveRequest')
make_head(_module, 'PrintTaskConfigurationSaveRequestedDeferral')
make_head(_module, 'PrintTaskConfigurationSaveRequestedEventArgs')
