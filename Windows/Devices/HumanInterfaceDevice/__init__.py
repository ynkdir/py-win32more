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
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.Devices.HumanInterfaceDevice
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Storage
import Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class HidBooleanControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.HumanInterfaceDevice.IHidBooleanControl
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.HidBooleanControl'
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.HumanInterfaceDevice.IHidBooleanControl) -> UInt32: ...
    @winrt_mixinmethod
    def get_UsagePage(self: Windows.Devices.HumanInterfaceDevice.IHidBooleanControl) -> UInt16: ...
    @winrt_mixinmethod
    def get_UsageId(self: Windows.Devices.HumanInterfaceDevice.IHidBooleanControl) -> UInt16: ...
    @winrt_mixinmethod
    def get_IsActive(self: Windows.Devices.HumanInterfaceDevice.IHidBooleanControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsActive(self: Windows.Devices.HumanInterfaceDevice.IHidBooleanControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ControlDescription(self: Windows.Devices.HumanInterfaceDevice.IHidBooleanControl) -> Windows.Devices.HumanInterfaceDevice.HidBooleanControlDescription: ...
    Id = property(get_Id, None)
    UsagePage = property(get_UsagePage, None)
    UsageId = property(get_UsageId, None)
    IsActive = property(get_IsActive, put_IsActive)
    ControlDescription = property(get_ControlDescription, None)
class HidBooleanControlDescription(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.HumanInterfaceDevice.IHidBooleanControlDescription
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.HidBooleanControlDescription'
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.HumanInterfaceDevice.IHidBooleanControlDescription) -> UInt32: ...
    @winrt_mixinmethod
    def get_ReportId(self: Windows.Devices.HumanInterfaceDevice.IHidBooleanControlDescription) -> UInt16: ...
    @winrt_mixinmethod
    def get_ReportType(self: Windows.Devices.HumanInterfaceDevice.IHidBooleanControlDescription) -> Windows.Devices.HumanInterfaceDevice.HidReportType: ...
    @winrt_mixinmethod
    def get_UsagePage(self: Windows.Devices.HumanInterfaceDevice.IHidBooleanControlDescription) -> UInt16: ...
    @winrt_mixinmethod
    def get_UsageId(self: Windows.Devices.HumanInterfaceDevice.IHidBooleanControlDescription) -> UInt16: ...
    @winrt_mixinmethod
    def get_ParentCollections(self: Windows.Devices.HumanInterfaceDevice.IHidBooleanControlDescription) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.HumanInterfaceDevice.HidCollection]: ...
    @winrt_mixinmethod
    def get_IsAbsolute(self: Windows.Devices.HumanInterfaceDevice.IHidBooleanControlDescription2) -> Boolean: ...
    Id = property(get_Id, None)
    ReportId = property(get_ReportId, None)
    ReportType = property(get_ReportType, None)
    UsagePage = property(get_UsagePage, None)
    UsageId = property(get_UsageId, None)
    ParentCollections = property(get_ParentCollections, None)
    IsAbsolute = property(get_IsAbsolute, None)
class HidCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.HumanInterfaceDevice.IHidCollection
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.HidCollection'
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.HumanInterfaceDevice.IHidCollection) -> UInt32: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Devices.HumanInterfaceDevice.IHidCollection) -> Windows.Devices.HumanInterfaceDevice.HidCollectionType: ...
    @winrt_mixinmethod
    def get_UsagePage(self: Windows.Devices.HumanInterfaceDevice.IHidCollection) -> UInt32: ...
    @winrt_mixinmethod
    def get_UsageId(self: Windows.Devices.HumanInterfaceDevice.IHidCollection) -> UInt32: ...
    Id = property(get_Id, None)
    Type = property(get_Type, None)
    UsagePage = property(get_UsagePage, None)
    UsageId = property(get_UsageId, None)
HidCollectionType = Int32
HidCollectionType_Physical: HidCollectionType = 0
HidCollectionType_Application: HidCollectionType = 1
HidCollectionType_Logical: HidCollectionType = 2
HidCollectionType_Report: HidCollectionType = 3
HidCollectionType_NamedArray: HidCollectionType = 4
HidCollectionType_UsageSwitch: HidCollectionType = 5
HidCollectionType_UsageModifier: HidCollectionType = 6
HidCollectionType_Other: HidCollectionType = 7
class HidDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.HumanInterfaceDevice.IHidDevice
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.HidDevice'
    @winrt_mixinmethod
    def get_VendorId(self: Windows.Devices.HumanInterfaceDevice.IHidDevice) -> UInt16: ...
    @winrt_mixinmethod
    def get_ProductId(self: Windows.Devices.HumanInterfaceDevice.IHidDevice) -> UInt16: ...
    @winrt_mixinmethod
    def get_Version(self: Windows.Devices.HumanInterfaceDevice.IHidDevice) -> UInt16: ...
    @winrt_mixinmethod
    def get_UsagePage(self: Windows.Devices.HumanInterfaceDevice.IHidDevice) -> UInt16: ...
    @winrt_mixinmethod
    def get_UsageId(self: Windows.Devices.HumanInterfaceDevice.IHidDevice) -> UInt16: ...
    @winrt_mixinmethod
    def GetInputReportAsync(self: Windows.Devices.HumanInterfaceDevice.IHidDevice) -> Windows.Foundation.IAsyncOperation[Windows.Devices.HumanInterfaceDevice.HidInputReport]: ...
    @winrt_mixinmethod
    def GetInputReportByIdAsync(self: Windows.Devices.HumanInterfaceDevice.IHidDevice, reportId: UInt16) -> Windows.Foundation.IAsyncOperation[Windows.Devices.HumanInterfaceDevice.HidInputReport]: ...
    @winrt_mixinmethod
    def GetFeatureReportAsync(self: Windows.Devices.HumanInterfaceDevice.IHidDevice) -> Windows.Foundation.IAsyncOperation[Windows.Devices.HumanInterfaceDevice.HidFeatureReport]: ...
    @winrt_mixinmethod
    def GetFeatureReportByIdAsync(self: Windows.Devices.HumanInterfaceDevice.IHidDevice, reportId: UInt16) -> Windows.Foundation.IAsyncOperation[Windows.Devices.HumanInterfaceDevice.HidFeatureReport]: ...
    @winrt_mixinmethod
    def CreateOutputReport(self: Windows.Devices.HumanInterfaceDevice.IHidDevice) -> Windows.Devices.HumanInterfaceDevice.HidOutputReport: ...
    @winrt_mixinmethod
    def CreateOutputReportById(self: Windows.Devices.HumanInterfaceDevice.IHidDevice, reportId: UInt16) -> Windows.Devices.HumanInterfaceDevice.HidOutputReport: ...
    @winrt_mixinmethod
    def CreateFeatureReport(self: Windows.Devices.HumanInterfaceDevice.IHidDevice) -> Windows.Devices.HumanInterfaceDevice.HidFeatureReport: ...
    @winrt_mixinmethod
    def CreateFeatureReportById(self: Windows.Devices.HumanInterfaceDevice.IHidDevice, reportId: UInt16) -> Windows.Devices.HumanInterfaceDevice.HidFeatureReport: ...
    @winrt_mixinmethod
    def SendOutputReportAsync(self: Windows.Devices.HumanInterfaceDevice.IHidDevice, outputReport: Windows.Devices.HumanInterfaceDevice.HidOutputReport) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def SendFeatureReportAsync(self: Windows.Devices.HumanInterfaceDevice.IHidDevice, featureReport: Windows.Devices.HumanInterfaceDevice.HidFeatureReport) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def GetBooleanControlDescriptions(self: Windows.Devices.HumanInterfaceDevice.IHidDevice, reportType: Windows.Devices.HumanInterfaceDevice.HidReportType, usagePage: UInt16, usageId: UInt16) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.HumanInterfaceDevice.HidBooleanControlDescription]: ...
    @winrt_mixinmethod
    def GetNumericControlDescriptions(self: Windows.Devices.HumanInterfaceDevice.IHidDevice, reportType: Windows.Devices.HumanInterfaceDevice.HidReportType, usagePage: UInt16, usageId: UInt16) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.HumanInterfaceDevice.HidNumericControlDescription]: ...
    @winrt_mixinmethod
    def add_InputReportReceived(self: Windows.Devices.HumanInterfaceDevice.IHidDevice, reportHandler: Windows.Foundation.TypedEventHandler[Windows.Devices.HumanInterfaceDevice.HidDevice, Windows.Devices.HumanInterfaceDevice.HidInputReportReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_InputReportReceived(self: Windows.Devices.HumanInterfaceDevice.IHidDevice, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.HumanInterfaceDevice.IHidDeviceStatics, usagePage: UInt16, usageId: UInt16) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorVidPid(cls: Windows.Devices.HumanInterfaceDevice.IHidDeviceStatics, usagePage: UInt16, usageId: UInt16, vendorId: UInt16, productId: UInt16) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.HumanInterfaceDevice.IHidDeviceStatics, deviceId: WinRT_String, accessMode: Windows.Storage.FileAccessMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.HumanInterfaceDevice.HidDevice]: ...
    VendorId = property(get_VendorId, None)
    ProductId = property(get_ProductId, None)
    Version = property(get_Version, None)
    UsagePage = property(get_UsagePage, None)
    UsageId = property(get_UsageId, None)
class HidFeatureReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.HumanInterfaceDevice.IHidFeatureReport
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.HidFeatureReport'
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.HumanInterfaceDevice.IHidFeatureReport) -> UInt16: ...
    @winrt_mixinmethod
    def get_Data(self: Windows.Devices.HumanInterfaceDevice.IHidFeatureReport) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_Data(self: Windows.Devices.HumanInterfaceDevice.IHidFeatureReport, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def GetBooleanControl(self: Windows.Devices.HumanInterfaceDevice.IHidFeatureReport, usagePage: UInt16, usageId: UInt16) -> Windows.Devices.HumanInterfaceDevice.HidBooleanControl: ...
    @winrt_mixinmethod
    def GetBooleanControlByDescription(self: Windows.Devices.HumanInterfaceDevice.IHidFeatureReport, controlDescription: Windows.Devices.HumanInterfaceDevice.HidBooleanControlDescription) -> Windows.Devices.HumanInterfaceDevice.HidBooleanControl: ...
    @winrt_mixinmethod
    def GetNumericControl(self: Windows.Devices.HumanInterfaceDevice.IHidFeatureReport, usagePage: UInt16, usageId: UInt16) -> Windows.Devices.HumanInterfaceDevice.HidNumericControl: ...
    @winrt_mixinmethod
    def GetNumericControlByDescription(self: Windows.Devices.HumanInterfaceDevice.IHidFeatureReport, controlDescription: Windows.Devices.HumanInterfaceDevice.HidNumericControlDescription) -> Windows.Devices.HumanInterfaceDevice.HidNumericControl: ...
    Id = property(get_Id, None)
    Data = property(get_Data, put_Data)
class HidInputReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.HumanInterfaceDevice.IHidInputReport
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.HidInputReport'
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.HumanInterfaceDevice.IHidInputReport) -> UInt16: ...
    @winrt_mixinmethod
    def get_Data(self: Windows.Devices.HumanInterfaceDevice.IHidInputReport) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_ActivatedBooleanControls(self: Windows.Devices.HumanInterfaceDevice.IHidInputReport) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.HumanInterfaceDevice.HidBooleanControl]: ...
    @winrt_mixinmethod
    def get_TransitionedBooleanControls(self: Windows.Devices.HumanInterfaceDevice.IHidInputReport) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.HumanInterfaceDevice.HidBooleanControl]: ...
    @winrt_mixinmethod
    def GetBooleanControl(self: Windows.Devices.HumanInterfaceDevice.IHidInputReport, usagePage: UInt16, usageId: UInt16) -> Windows.Devices.HumanInterfaceDevice.HidBooleanControl: ...
    @winrt_mixinmethod
    def GetBooleanControlByDescription(self: Windows.Devices.HumanInterfaceDevice.IHidInputReport, controlDescription: Windows.Devices.HumanInterfaceDevice.HidBooleanControlDescription) -> Windows.Devices.HumanInterfaceDevice.HidBooleanControl: ...
    @winrt_mixinmethod
    def GetNumericControl(self: Windows.Devices.HumanInterfaceDevice.IHidInputReport, usagePage: UInt16, usageId: UInt16) -> Windows.Devices.HumanInterfaceDevice.HidNumericControl: ...
    @winrt_mixinmethod
    def GetNumericControlByDescription(self: Windows.Devices.HumanInterfaceDevice.IHidInputReport, controlDescription: Windows.Devices.HumanInterfaceDevice.HidNumericControlDescription) -> Windows.Devices.HumanInterfaceDevice.HidNumericControl: ...
    Id = property(get_Id, None)
    Data = property(get_Data, None)
    ActivatedBooleanControls = property(get_ActivatedBooleanControls, None)
    TransitionedBooleanControls = property(get_TransitionedBooleanControls, None)
class HidInputReportReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.HumanInterfaceDevice.IHidInputReportReceivedEventArgs
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.HidInputReportReceivedEventArgs'
    @winrt_mixinmethod
    def get_Report(self: Windows.Devices.HumanInterfaceDevice.IHidInputReportReceivedEventArgs) -> Windows.Devices.HumanInterfaceDevice.HidInputReport: ...
    Report = property(get_Report, None)
class HidNumericControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.HumanInterfaceDevice.IHidNumericControl
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.HidNumericControl'
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.HumanInterfaceDevice.IHidNumericControl) -> UInt32: ...
    @winrt_mixinmethod
    def get_IsGrouped(self: Windows.Devices.HumanInterfaceDevice.IHidNumericControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_UsagePage(self: Windows.Devices.HumanInterfaceDevice.IHidNumericControl) -> UInt16: ...
    @winrt_mixinmethod
    def get_UsageId(self: Windows.Devices.HumanInterfaceDevice.IHidNumericControl) -> UInt16: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Devices.HumanInterfaceDevice.IHidNumericControl) -> Int64: ...
    @winrt_mixinmethod
    def put_Value(self: Windows.Devices.HumanInterfaceDevice.IHidNumericControl, value: Int64) -> Void: ...
    @winrt_mixinmethod
    def get_ScaledValue(self: Windows.Devices.HumanInterfaceDevice.IHidNumericControl) -> Int64: ...
    @winrt_mixinmethod
    def put_ScaledValue(self: Windows.Devices.HumanInterfaceDevice.IHidNumericControl, value: Int64) -> Void: ...
    @winrt_mixinmethod
    def get_ControlDescription(self: Windows.Devices.HumanInterfaceDevice.IHidNumericControl) -> Windows.Devices.HumanInterfaceDevice.HidNumericControlDescription: ...
    Id = property(get_Id, None)
    IsGrouped = property(get_IsGrouped, None)
    UsagePage = property(get_UsagePage, None)
    UsageId = property(get_UsageId, None)
    Value = property(get_Value, put_Value)
    ScaledValue = property(get_ScaledValue, put_ScaledValue)
    ControlDescription = property(get_ControlDescription, None)
class HidNumericControlDescription(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.HidNumericControlDescription'
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> UInt32: ...
    @winrt_mixinmethod
    def get_ReportId(self: Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> UInt16: ...
    @winrt_mixinmethod
    def get_ReportType(self: Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> Windows.Devices.HumanInterfaceDevice.HidReportType: ...
    @winrt_mixinmethod
    def get_ReportSize(self: Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> UInt32: ...
    @winrt_mixinmethod
    def get_ReportCount(self: Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> UInt32: ...
    @winrt_mixinmethod
    def get_UsagePage(self: Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> UInt16: ...
    @winrt_mixinmethod
    def get_UsageId(self: Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> UInt16: ...
    @winrt_mixinmethod
    def get_LogicalMinimum(self: Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> Int32: ...
    @winrt_mixinmethod
    def get_LogicalMaximum(self: Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> Int32: ...
    @winrt_mixinmethod
    def get_PhysicalMinimum(self: Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> Int32: ...
    @winrt_mixinmethod
    def get_PhysicalMaximum(self: Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> Int32: ...
    @winrt_mixinmethod
    def get_UnitExponent(self: Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> UInt32: ...
    @winrt_mixinmethod
    def get_Unit(self: Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> UInt32: ...
    @winrt_mixinmethod
    def get_IsAbsolute(self: Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasNull(self: Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> Boolean: ...
    @winrt_mixinmethod
    def get_ParentCollections(self: Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.HumanInterfaceDevice.HidCollection]: ...
    Id = property(get_Id, None)
    ReportId = property(get_ReportId, None)
    ReportType = property(get_ReportType, None)
    ReportSize = property(get_ReportSize, None)
    ReportCount = property(get_ReportCount, None)
    UsagePage = property(get_UsagePage, None)
    UsageId = property(get_UsageId, None)
    LogicalMinimum = property(get_LogicalMinimum, None)
    LogicalMaximum = property(get_LogicalMaximum, None)
    PhysicalMinimum = property(get_PhysicalMinimum, None)
    PhysicalMaximum = property(get_PhysicalMaximum, None)
    UnitExponent = property(get_UnitExponent, None)
    Unit = property(get_Unit, None)
    IsAbsolute = property(get_IsAbsolute, None)
    HasNull = property(get_HasNull, None)
    ParentCollections = property(get_ParentCollections, None)
class HidOutputReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.HumanInterfaceDevice.IHidOutputReport
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.HidOutputReport'
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.HumanInterfaceDevice.IHidOutputReport) -> UInt16: ...
    @winrt_mixinmethod
    def get_Data(self: Windows.Devices.HumanInterfaceDevice.IHidOutputReport) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_Data(self: Windows.Devices.HumanInterfaceDevice.IHidOutputReport, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def GetBooleanControl(self: Windows.Devices.HumanInterfaceDevice.IHidOutputReport, usagePage: UInt16, usageId: UInt16) -> Windows.Devices.HumanInterfaceDevice.HidBooleanControl: ...
    @winrt_mixinmethod
    def GetBooleanControlByDescription(self: Windows.Devices.HumanInterfaceDevice.IHidOutputReport, controlDescription: Windows.Devices.HumanInterfaceDevice.HidBooleanControlDescription) -> Windows.Devices.HumanInterfaceDevice.HidBooleanControl: ...
    @winrt_mixinmethod
    def GetNumericControl(self: Windows.Devices.HumanInterfaceDevice.IHidOutputReport, usagePage: UInt16, usageId: UInt16) -> Windows.Devices.HumanInterfaceDevice.HidNumericControl: ...
    @winrt_mixinmethod
    def GetNumericControlByDescription(self: Windows.Devices.HumanInterfaceDevice.IHidOutputReport, controlDescription: Windows.Devices.HumanInterfaceDevice.HidNumericControlDescription) -> Windows.Devices.HumanInterfaceDevice.HidNumericControl: ...
    Id = property(get_Id, None)
    Data = property(get_Data, put_Data)
HidReportType = Int32
HidReportType_Input: HidReportType = 0
HidReportType_Output: HidReportType = 1
HidReportType_Feature: HidReportType = 2
class IHidBooleanControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.IHidBooleanControl'
    _iid_ = Guid('{524df48a-3695-408c-bba2-e2eb5abfbc20}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_UsagePage(self) -> UInt16: ...
    @winrt_commethod(8)
    def get_UsageId(self) -> UInt16: ...
    @winrt_commethod(9)
    def get_IsActive(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_IsActive(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_ControlDescription(self) -> Windows.Devices.HumanInterfaceDevice.HidBooleanControlDescription: ...
    Id = property(get_Id, None)
    UsagePage = property(get_UsagePage, None)
    UsageId = property(get_UsageId, None)
    IsActive = property(get_IsActive, put_IsActive)
    ControlDescription = property(get_ControlDescription, None)
class IHidBooleanControlDescription(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.IHidBooleanControlDescription'
    _iid_ = Guid('{6196e543-29d8-4a2a-8683-849e207bbe31}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_ReportId(self) -> UInt16: ...
    @winrt_commethod(8)
    def get_ReportType(self) -> Windows.Devices.HumanInterfaceDevice.HidReportType: ...
    @winrt_commethod(9)
    def get_UsagePage(self) -> UInt16: ...
    @winrt_commethod(10)
    def get_UsageId(self) -> UInt16: ...
    @winrt_commethod(11)
    def get_ParentCollections(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.HumanInterfaceDevice.HidCollection]: ...
    Id = property(get_Id, None)
    ReportId = property(get_ReportId, None)
    ReportType = property(get_ReportType, None)
    UsagePage = property(get_UsagePage, None)
    UsageId = property(get_UsageId, None)
    ParentCollections = property(get_ParentCollections, None)
class IHidBooleanControlDescription2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.IHidBooleanControlDescription2'
    _iid_ = Guid('{c8eed2ea-8a77-4c36-aa00-5ff0449d3e73}')
    @winrt_commethod(6)
    def get_IsAbsolute(self) -> Boolean: ...
    IsAbsolute = property(get_IsAbsolute, None)
class IHidCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.IHidCollection'
    _iid_ = Guid('{7189f5a3-32f1-46e3-befd-44d2663b7e6a}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Type(self) -> Windows.Devices.HumanInterfaceDevice.HidCollectionType: ...
    @winrt_commethod(8)
    def get_UsagePage(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_UsageId(self) -> UInt32: ...
    Id = property(get_Id, None)
    Type = property(get_Type, None)
    UsagePage = property(get_UsagePage, None)
    UsageId = property(get_UsageId, None)
class IHidDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.IHidDevice'
    _iid_ = Guid('{5f8a14e7-2200-432e-95da-d09b87d574a8}')
    @winrt_commethod(6)
    def get_VendorId(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_ProductId(self) -> UInt16: ...
    @winrt_commethod(8)
    def get_Version(self) -> UInt16: ...
    @winrt_commethod(9)
    def get_UsagePage(self) -> UInt16: ...
    @winrt_commethod(10)
    def get_UsageId(self) -> UInt16: ...
    @winrt_commethod(11)
    def GetInputReportAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.HumanInterfaceDevice.HidInputReport]: ...
    @winrt_commethod(12)
    def GetInputReportByIdAsync(self, reportId: UInt16) -> Windows.Foundation.IAsyncOperation[Windows.Devices.HumanInterfaceDevice.HidInputReport]: ...
    @winrt_commethod(13)
    def GetFeatureReportAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.HumanInterfaceDevice.HidFeatureReport]: ...
    @winrt_commethod(14)
    def GetFeatureReportByIdAsync(self, reportId: UInt16) -> Windows.Foundation.IAsyncOperation[Windows.Devices.HumanInterfaceDevice.HidFeatureReport]: ...
    @winrt_commethod(15)
    def CreateOutputReport(self) -> Windows.Devices.HumanInterfaceDevice.HidOutputReport: ...
    @winrt_commethod(16)
    def CreateOutputReportById(self, reportId: UInt16) -> Windows.Devices.HumanInterfaceDevice.HidOutputReport: ...
    @winrt_commethod(17)
    def CreateFeatureReport(self) -> Windows.Devices.HumanInterfaceDevice.HidFeatureReport: ...
    @winrt_commethod(18)
    def CreateFeatureReportById(self, reportId: UInt16) -> Windows.Devices.HumanInterfaceDevice.HidFeatureReport: ...
    @winrt_commethod(19)
    def SendOutputReportAsync(self, outputReport: Windows.Devices.HumanInterfaceDevice.HidOutputReport) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_commethod(20)
    def SendFeatureReportAsync(self, featureReport: Windows.Devices.HumanInterfaceDevice.HidFeatureReport) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_commethod(21)
    def GetBooleanControlDescriptions(self, reportType: Windows.Devices.HumanInterfaceDevice.HidReportType, usagePage: UInt16, usageId: UInt16) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.HumanInterfaceDevice.HidBooleanControlDescription]: ...
    @winrt_commethod(22)
    def GetNumericControlDescriptions(self, reportType: Windows.Devices.HumanInterfaceDevice.HidReportType, usagePage: UInt16, usageId: UInt16) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.HumanInterfaceDevice.HidNumericControlDescription]: ...
    @winrt_commethod(23)
    def add_InputReportReceived(self, reportHandler: Windows.Foundation.TypedEventHandler[Windows.Devices.HumanInterfaceDevice.HidDevice, Windows.Devices.HumanInterfaceDevice.HidInputReportReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(24)
    def remove_InputReportReceived(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    VendorId = property(get_VendorId, None)
    ProductId = property(get_ProductId, None)
    Version = property(get_Version, None)
    UsagePage = property(get_UsagePage, None)
    UsageId = property(get_UsageId, None)
class IHidDeviceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.IHidDeviceStatics'
    _iid_ = Guid('{9e5981e4-9856-418c-9f73-77de0cd85754}')
    @winrt_commethod(6)
    def GetDeviceSelector(self, usagePage: UInt16, usageId: UInt16) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDeviceSelectorVidPid(self, usagePage: UInt16, usageId: UInt16, vendorId: UInt16, productId: UInt16) -> WinRT_String: ...
    @winrt_commethod(8)
    def FromIdAsync(self, deviceId: WinRT_String, accessMode: Windows.Storage.FileAccessMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.HumanInterfaceDevice.HidDevice]: ...
class IHidFeatureReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.IHidFeatureReport'
    _iid_ = Guid('{841d9b79-5ae5-46e3-82ef-1fec5c8942f4}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_Data(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def put_Data(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(9)
    def GetBooleanControl(self, usagePage: UInt16, usageId: UInt16) -> Windows.Devices.HumanInterfaceDevice.HidBooleanControl: ...
    @winrt_commethod(10)
    def GetBooleanControlByDescription(self, controlDescription: Windows.Devices.HumanInterfaceDevice.HidBooleanControlDescription) -> Windows.Devices.HumanInterfaceDevice.HidBooleanControl: ...
    @winrt_commethod(11)
    def GetNumericControl(self, usagePage: UInt16, usageId: UInt16) -> Windows.Devices.HumanInterfaceDevice.HidNumericControl: ...
    @winrt_commethod(12)
    def GetNumericControlByDescription(self, controlDescription: Windows.Devices.HumanInterfaceDevice.HidNumericControlDescription) -> Windows.Devices.HumanInterfaceDevice.HidNumericControl: ...
    Id = property(get_Id, None)
    Data = property(get_Data, put_Data)
class IHidInputReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.IHidInputReport'
    _iid_ = Guid('{c35d0e50-f7e7-4e8d-b23e-cabbe56b90e9}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_Data(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def get_ActivatedBooleanControls(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.HumanInterfaceDevice.HidBooleanControl]: ...
    @winrt_commethod(9)
    def get_TransitionedBooleanControls(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.HumanInterfaceDevice.HidBooleanControl]: ...
    @winrt_commethod(10)
    def GetBooleanControl(self, usagePage: UInt16, usageId: UInt16) -> Windows.Devices.HumanInterfaceDevice.HidBooleanControl: ...
    @winrt_commethod(11)
    def GetBooleanControlByDescription(self, controlDescription: Windows.Devices.HumanInterfaceDevice.HidBooleanControlDescription) -> Windows.Devices.HumanInterfaceDevice.HidBooleanControl: ...
    @winrt_commethod(12)
    def GetNumericControl(self, usagePage: UInt16, usageId: UInt16) -> Windows.Devices.HumanInterfaceDevice.HidNumericControl: ...
    @winrt_commethod(13)
    def GetNumericControlByDescription(self, controlDescription: Windows.Devices.HumanInterfaceDevice.HidNumericControlDescription) -> Windows.Devices.HumanInterfaceDevice.HidNumericControl: ...
    Id = property(get_Id, None)
    Data = property(get_Data, None)
    ActivatedBooleanControls = property(get_ActivatedBooleanControls, None)
    TransitionedBooleanControls = property(get_TransitionedBooleanControls, None)
class IHidInputReportReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.IHidInputReportReceivedEventArgs'
    _iid_ = Guid('{7059c5cb-59b2-4dc2-985c-0adc6136fa2d}')
    @winrt_commethod(6)
    def get_Report(self) -> Windows.Devices.HumanInterfaceDevice.HidInputReport: ...
    Report = property(get_Report, None)
class IHidNumericControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.IHidNumericControl'
    _iid_ = Guid('{e38a12a5-35a7-4b75-89c8-fb1f28b10823}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_IsGrouped(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_UsagePage(self) -> UInt16: ...
    @winrt_commethod(9)
    def get_UsageId(self) -> UInt16: ...
    @winrt_commethod(10)
    def get_Value(self) -> Int64: ...
    @winrt_commethod(11)
    def put_Value(self, value: Int64) -> Void: ...
    @winrt_commethod(12)
    def get_ScaledValue(self) -> Int64: ...
    @winrt_commethod(13)
    def put_ScaledValue(self, value: Int64) -> Void: ...
    @winrt_commethod(14)
    def get_ControlDescription(self) -> Windows.Devices.HumanInterfaceDevice.HidNumericControlDescription: ...
    Id = property(get_Id, None)
    IsGrouped = property(get_IsGrouped, None)
    UsagePage = property(get_UsagePage, None)
    UsageId = property(get_UsageId, None)
    Value = property(get_Value, put_Value)
    ScaledValue = property(get_ScaledValue, put_ScaledValue)
    ControlDescription = property(get_ControlDescription, None)
class IHidNumericControlDescription(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.IHidNumericControlDescription'
    _iid_ = Guid('{638d5e86-1d97-4c75-927f-5ff58ba05e32}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_ReportId(self) -> UInt16: ...
    @winrt_commethod(8)
    def get_ReportType(self) -> Windows.Devices.HumanInterfaceDevice.HidReportType: ...
    @winrt_commethod(9)
    def get_ReportSize(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_ReportCount(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_UsagePage(self) -> UInt16: ...
    @winrt_commethod(12)
    def get_UsageId(self) -> UInt16: ...
    @winrt_commethod(13)
    def get_LogicalMinimum(self) -> Int32: ...
    @winrt_commethod(14)
    def get_LogicalMaximum(self) -> Int32: ...
    @winrt_commethod(15)
    def get_PhysicalMinimum(self) -> Int32: ...
    @winrt_commethod(16)
    def get_PhysicalMaximum(self) -> Int32: ...
    @winrt_commethod(17)
    def get_UnitExponent(self) -> UInt32: ...
    @winrt_commethod(18)
    def get_Unit(self) -> UInt32: ...
    @winrt_commethod(19)
    def get_IsAbsolute(self) -> Boolean: ...
    @winrt_commethod(20)
    def get_HasNull(self) -> Boolean: ...
    @winrt_commethod(21)
    def get_ParentCollections(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.HumanInterfaceDevice.HidCollection]: ...
    Id = property(get_Id, None)
    ReportId = property(get_ReportId, None)
    ReportType = property(get_ReportType, None)
    ReportSize = property(get_ReportSize, None)
    ReportCount = property(get_ReportCount, None)
    UsagePage = property(get_UsagePage, None)
    UsageId = property(get_UsageId, None)
    LogicalMinimum = property(get_LogicalMinimum, None)
    LogicalMaximum = property(get_LogicalMaximum, None)
    PhysicalMinimum = property(get_PhysicalMinimum, None)
    PhysicalMaximum = property(get_PhysicalMaximum, None)
    UnitExponent = property(get_UnitExponent, None)
    Unit = property(get_Unit, None)
    IsAbsolute = property(get_IsAbsolute, None)
    HasNull = property(get_HasNull, None)
    ParentCollections = property(get_ParentCollections, None)
class IHidOutputReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.HumanInterfaceDevice.IHidOutputReport'
    _iid_ = Guid('{62cb2544-c896-4463-93c1-df9db053c450}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_Data(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def put_Data(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(9)
    def GetBooleanControl(self, usagePage: UInt16, usageId: UInt16) -> Windows.Devices.HumanInterfaceDevice.HidBooleanControl: ...
    @winrt_commethod(10)
    def GetBooleanControlByDescription(self, controlDescription: Windows.Devices.HumanInterfaceDevice.HidBooleanControlDescription) -> Windows.Devices.HumanInterfaceDevice.HidBooleanControl: ...
    @winrt_commethod(11)
    def GetNumericControl(self, usagePage: UInt16, usageId: UInt16) -> Windows.Devices.HumanInterfaceDevice.HidNumericControl: ...
    @winrt_commethod(12)
    def GetNumericControlByDescription(self, controlDescription: Windows.Devices.HumanInterfaceDevice.HidNumericControlDescription) -> Windows.Devices.HumanInterfaceDevice.HidNumericControl: ...
    Id = property(get_Id, None)
    Data = property(get_Data, put_Data)
make_head(_module, 'HidBooleanControl')
make_head(_module, 'HidBooleanControlDescription')
make_head(_module, 'HidCollection')
make_head(_module, 'HidDevice')
make_head(_module, 'HidFeatureReport')
make_head(_module, 'HidInputReport')
make_head(_module, 'HidInputReportReceivedEventArgs')
make_head(_module, 'HidNumericControl')
make_head(_module, 'HidNumericControlDescription')
make_head(_module, 'HidOutputReport')
make_head(_module, 'IHidBooleanControl')
make_head(_module, 'IHidBooleanControlDescription')
make_head(_module, 'IHidBooleanControlDescription2')
make_head(_module, 'IHidCollection')
make_head(_module, 'IHidDevice')
make_head(_module, 'IHidDeviceStatics')
make_head(_module, 'IHidFeatureReport')
make_head(_module, 'IHidInputReport')
make_head(_module, 'IHidInputReportReceivedEventArgs')
make_head(_module, 'IHidNumericControl')
make_head(_module, 'IHidNumericControlDescription')
make_head(_module, 'IHidOutputReport')
