from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.ApplicationModel.Appointments
import Windows.ApplicationModel.Appointments.AppointmentsProvider
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
class AddAppointmentOperation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Appointments.AppointmentsProvider.AddAppointmentOperation'
    @winrt_mixinmethod
    def get_AppointmentInformation(self: Windows.ApplicationModel.Appointments.AppointmentsProvider.IAddAppointmentOperation) -> Windows.ApplicationModel.Appointments.Appointment: ...
    @winrt_mixinmethod
    def get_SourcePackageFamilyName(self: Windows.ApplicationModel.Appointments.AppointmentsProvider.IAddAppointmentOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompleted(self: Windows.ApplicationModel.Appointments.AppointmentsProvider.IAddAppointmentOperation, itemId: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def ReportCanceled(self: Windows.ApplicationModel.Appointments.AppointmentsProvider.IAddAppointmentOperation) -> Void: ...
    @winrt_mixinmethod
    def ReportError(self: Windows.ApplicationModel.Appointments.AppointmentsProvider.IAddAppointmentOperation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def DismissUI(self: Windows.ApplicationModel.Appointments.AppointmentsProvider.IAddAppointmentOperation) -> Void: ...
    AppointmentInformation = property(get_AppointmentInformation, None)
    SourcePackageFamilyName = property(get_SourcePackageFamilyName, None)
class AppointmentsProviderLaunchActionVerbs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Appointments.AppointmentsProvider.AppointmentsProviderLaunchActionVerbs'
    @winrt_classmethod
    def get_ShowAppointmentDetails(cls: Windows.ApplicationModel.Appointments.AppointmentsProvider.IAppointmentsProviderLaunchActionVerbsStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_AddAppointment(cls: Windows.ApplicationModel.Appointments.AppointmentsProvider.IAppointmentsProviderLaunchActionVerbsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_ReplaceAppointment(cls: Windows.ApplicationModel.Appointments.AppointmentsProvider.IAppointmentsProviderLaunchActionVerbsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RemoveAppointment(cls: Windows.ApplicationModel.Appointments.AppointmentsProvider.IAppointmentsProviderLaunchActionVerbsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_ShowTimeFrame(cls: Windows.ApplicationModel.Appointments.AppointmentsProvider.IAppointmentsProviderLaunchActionVerbsStatics) -> WinRT_String: ...
    ShowAppointmentDetails = property(get_ShowAppointmentDetails, None)
    AddAppointment = property(get_AddAppointment, None)
    ReplaceAppointment = property(get_ReplaceAppointment, None)
    RemoveAppointment = property(get_RemoveAppointment, None)
    ShowTimeFrame = property(get_ShowTimeFrame, None)
class IAddAppointmentOperation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ec4a9af3-620d-4c69-ad-d7-97-94-e9-18-08-1f')
    @winrt_commethod(6)
    def get_AppointmentInformation(self) -> Windows.ApplicationModel.Appointments.Appointment: ...
    @winrt_commethod(7)
    def get_SourcePackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def ReportCompleted(self, itemId: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def ReportCanceled(self) -> Void: ...
    @winrt_commethod(10)
    def ReportError(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def DismissUI(self) -> Void: ...
    AppointmentInformation = property(get_AppointmentInformation, None)
    SourcePackageFamilyName = property(get_SourcePackageFamilyName, None)
class IAppointmentsProviderLaunchActionVerbsStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('36dbba28-9e2e-49c6-8e-f7-3a-b7-a5-dc-c8-b8')
    @winrt_commethod(6)
    def get_AddAppointment(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ReplaceAppointment(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_RemoveAppointment(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_ShowTimeFrame(self) -> WinRT_String: ...
    AddAppointment = property(get_AddAppointment, None)
    ReplaceAppointment = property(get_ReplaceAppointment, None)
    RemoveAppointment = property(get_RemoveAppointment, None)
    ShowTimeFrame = property(get_ShowTimeFrame, None)
class IAppointmentsProviderLaunchActionVerbsStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ef9049a4-af21-473c-88-dc-76-cd-89-f6-0c-a5')
    @winrt_commethod(6)
    def get_ShowAppointmentDetails(self) -> WinRT_String: ...
    ShowAppointmentDetails = property(get_ShowAppointmentDetails, None)
class IRemoveAppointmentOperation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('08b66aba-fe33-46cd-a5-0c-a8-ff-b3-26-05-37')
    @winrt_commethod(6)
    def get_AppointmentId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_InstanceStartDate(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(8)
    def get_SourcePackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def ReportCompleted(self) -> Void: ...
    @winrt_commethod(10)
    def ReportCanceled(self) -> Void: ...
    @winrt_commethod(11)
    def ReportError(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def DismissUI(self) -> Void: ...
    AppointmentId = property(get_AppointmentId, None)
    InstanceStartDate = property(get_InstanceStartDate, None)
    SourcePackageFamilyName = property(get_SourcePackageFamilyName, None)
class IReplaceAppointmentOperation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f4903d9b-9e61-4de2-a7-32-26-87-c0-7d-1d-e8')
    @winrt_commethod(6)
    def get_AppointmentId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_AppointmentInformation(self) -> Windows.ApplicationModel.Appointments.Appointment: ...
    @winrt_commethod(8)
    def get_InstanceStartDate(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(9)
    def get_SourcePackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def ReportCompleted(self, itemId: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def ReportCanceled(self) -> Void: ...
    @winrt_commethod(12)
    def ReportError(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def DismissUI(self) -> Void: ...
    AppointmentId = property(get_AppointmentId, None)
    AppointmentInformation = property(get_AppointmentInformation, None)
    InstanceStartDate = property(get_InstanceStartDate, None)
    SourcePackageFamilyName = property(get_SourcePackageFamilyName, None)
class RemoveAppointmentOperation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Appointments.AppointmentsProvider.RemoveAppointmentOperation'
    @winrt_mixinmethod
    def get_AppointmentId(self: Windows.ApplicationModel.Appointments.AppointmentsProvider.IRemoveAppointmentOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_InstanceStartDate(self: Windows.ApplicationModel.Appointments.AppointmentsProvider.IRemoveAppointmentOperation) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_SourcePackageFamilyName(self: Windows.ApplicationModel.Appointments.AppointmentsProvider.IRemoveAppointmentOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompleted(self: Windows.ApplicationModel.Appointments.AppointmentsProvider.IRemoveAppointmentOperation) -> Void: ...
    @winrt_mixinmethod
    def ReportCanceled(self: Windows.ApplicationModel.Appointments.AppointmentsProvider.IRemoveAppointmentOperation) -> Void: ...
    @winrt_mixinmethod
    def ReportError(self: Windows.ApplicationModel.Appointments.AppointmentsProvider.IRemoveAppointmentOperation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def DismissUI(self: Windows.ApplicationModel.Appointments.AppointmentsProvider.IRemoveAppointmentOperation) -> Void: ...
    AppointmentId = property(get_AppointmentId, None)
    InstanceStartDate = property(get_InstanceStartDate, None)
    SourcePackageFamilyName = property(get_SourcePackageFamilyName, None)
class ReplaceAppointmentOperation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Appointments.AppointmentsProvider.ReplaceAppointmentOperation'
    @winrt_mixinmethod
    def get_AppointmentId(self: Windows.ApplicationModel.Appointments.AppointmentsProvider.IReplaceAppointmentOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppointmentInformation(self: Windows.ApplicationModel.Appointments.AppointmentsProvider.IReplaceAppointmentOperation) -> Windows.ApplicationModel.Appointments.Appointment: ...
    @winrt_mixinmethod
    def get_InstanceStartDate(self: Windows.ApplicationModel.Appointments.AppointmentsProvider.IReplaceAppointmentOperation) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_SourcePackageFamilyName(self: Windows.ApplicationModel.Appointments.AppointmentsProvider.IReplaceAppointmentOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompleted(self: Windows.ApplicationModel.Appointments.AppointmentsProvider.IReplaceAppointmentOperation, itemId: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def ReportCanceled(self: Windows.ApplicationModel.Appointments.AppointmentsProvider.IReplaceAppointmentOperation) -> Void: ...
    @winrt_mixinmethod
    def ReportError(self: Windows.ApplicationModel.Appointments.AppointmentsProvider.IReplaceAppointmentOperation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def DismissUI(self: Windows.ApplicationModel.Appointments.AppointmentsProvider.IReplaceAppointmentOperation) -> Void: ...
    AppointmentId = property(get_AppointmentId, None)
    AppointmentInformation = property(get_AppointmentInformation, None)
    InstanceStartDate = property(get_InstanceStartDate, None)
    SourcePackageFamilyName = property(get_SourcePackageFamilyName, None)
make_head(_module, 'AddAppointmentOperation')
make_head(_module, 'AppointmentsProviderLaunchActionVerbs')
make_head(_module, 'IAddAppointmentOperation')
make_head(_module, 'IAppointmentsProviderLaunchActionVerbsStatics')
make_head(_module, 'IAppointmentsProviderLaunchActionVerbsStatics2')
make_head(_module, 'IRemoveAppointmentOperation')
make_head(_module, 'IReplaceAppointmentOperation')
make_head(_module, 'RemoveAppointmentOperation')
make_head(_module, 'ReplaceAppointmentOperation')
