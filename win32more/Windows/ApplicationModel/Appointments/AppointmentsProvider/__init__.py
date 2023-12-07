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
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.ApplicationModel.Appointments
import win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider
import win32more.Windows.Foundation
class AddAppointmentOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IAddAppointmentOperation
    _classid_ = 'Windows.ApplicationModel.Appointments.AppointmentsProvider.AddAppointmentOperation'
    @winrt_mixinmethod
    def get_AppointmentInformation(self: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IAddAppointmentOperation) -> win32more.Windows.ApplicationModel.Appointments.Appointment: ...
    @winrt_mixinmethod
    def get_SourcePackageFamilyName(self: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IAddAppointmentOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompleted(self: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IAddAppointmentOperation, itemId: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def ReportCanceled(self: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IAddAppointmentOperation) -> Void: ...
    @winrt_mixinmethod
    def ReportError(self: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IAddAppointmentOperation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def DismissUI(self: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IAddAppointmentOperation) -> Void: ...
    AppointmentInformation = property(get_AppointmentInformation, None)
    SourcePackageFamilyName = property(get_SourcePackageFamilyName, None)
class _AppointmentsProviderLaunchActionVerbs_Meta_(ComPtr.__class__):
    pass
class AppointmentsProviderLaunchActionVerbs(ComPtr, metaclass=_AppointmentsProviderLaunchActionVerbs_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Appointments.AppointmentsProvider.AppointmentsProviderLaunchActionVerbs'
    @winrt_classmethod
    def get_ShowAppointmentDetails(cls: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IAppointmentsProviderLaunchActionVerbsStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def get_AddAppointment(cls: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IAppointmentsProviderLaunchActionVerbsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_ReplaceAppointment(cls: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IAppointmentsProviderLaunchActionVerbsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RemoveAppointment(cls: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IAppointmentsProviderLaunchActionVerbsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_ShowTimeFrame(cls: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IAppointmentsProviderLaunchActionVerbsStatics) -> WinRT_String: ...
    _AppointmentsProviderLaunchActionVerbs_Meta_.ShowAppointmentDetails = property(get_ShowAppointmentDetails.__wrapped__, None)
    _AppointmentsProviderLaunchActionVerbs_Meta_.AddAppointment = property(get_AddAppointment.__wrapped__, None)
    _AppointmentsProviderLaunchActionVerbs_Meta_.ReplaceAppointment = property(get_ReplaceAppointment.__wrapped__, None)
    _AppointmentsProviderLaunchActionVerbs_Meta_.RemoveAppointment = property(get_RemoveAppointment.__wrapped__, None)
    _AppointmentsProviderLaunchActionVerbs_Meta_.ShowTimeFrame = property(get_ShowTimeFrame.__wrapped__, None)
class IAddAppointmentOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Appointments.AppointmentsProvider.IAddAppointmentOperation'
    _iid_ = Guid('{ec4a9af3-620d-4c69-add7-9794e918081f}')
    @winrt_commethod(6)
    def get_AppointmentInformation(self) -> win32more.Windows.ApplicationModel.Appointments.Appointment: ...
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
class IAppointmentsProviderLaunchActionVerbsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Appointments.AppointmentsProvider.IAppointmentsProviderLaunchActionVerbsStatics'
    _iid_ = Guid('{36dbba28-9e2e-49c6-8ef7-3ab7a5dcc8b8}')
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
class IAppointmentsProviderLaunchActionVerbsStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Appointments.AppointmentsProvider.IAppointmentsProviderLaunchActionVerbsStatics2'
    _iid_ = Guid('{ef9049a4-af21-473c-88dc-76cd89f60ca5}')
    @winrt_commethod(6)
    def get_ShowAppointmentDetails(self) -> WinRT_String: ...
    ShowAppointmentDetails = property(get_ShowAppointmentDetails, None)
class IRemoveAppointmentOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Appointments.AppointmentsProvider.IRemoveAppointmentOperation'
    _iid_ = Guid('{08b66aba-fe33-46cd-a50c-a8ffb3260537}')
    @winrt_commethod(6)
    def get_AppointmentId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_InstanceStartDate(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
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
class IReplaceAppointmentOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Appointments.AppointmentsProvider.IReplaceAppointmentOperation'
    _iid_ = Guid('{f4903d9b-9e61-4de2-a732-2687c07d1de8}')
    @winrt_commethod(6)
    def get_AppointmentId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_AppointmentInformation(self) -> win32more.Windows.ApplicationModel.Appointments.Appointment: ...
    @winrt_commethod(8)
    def get_InstanceStartDate(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
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
class RemoveAppointmentOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IRemoveAppointmentOperation
    _classid_ = 'Windows.ApplicationModel.Appointments.AppointmentsProvider.RemoveAppointmentOperation'
    @winrt_mixinmethod
    def get_AppointmentId(self: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IRemoveAppointmentOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_InstanceStartDate(self: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IRemoveAppointmentOperation) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_SourcePackageFamilyName(self: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IRemoveAppointmentOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompleted(self: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IRemoveAppointmentOperation) -> Void: ...
    @winrt_mixinmethod
    def ReportCanceled(self: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IRemoveAppointmentOperation) -> Void: ...
    @winrt_mixinmethod
    def ReportError(self: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IRemoveAppointmentOperation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def DismissUI(self: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IRemoveAppointmentOperation) -> Void: ...
    AppointmentId = property(get_AppointmentId, None)
    InstanceStartDate = property(get_InstanceStartDate, None)
    SourcePackageFamilyName = property(get_SourcePackageFamilyName, None)
class ReplaceAppointmentOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IReplaceAppointmentOperation
    _classid_ = 'Windows.ApplicationModel.Appointments.AppointmentsProvider.ReplaceAppointmentOperation'
    @winrt_mixinmethod
    def get_AppointmentId(self: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IReplaceAppointmentOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppointmentInformation(self: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IReplaceAppointmentOperation) -> win32more.Windows.ApplicationModel.Appointments.Appointment: ...
    @winrt_mixinmethod
    def get_InstanceStartDate(self: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IReplaceAppointmentOperation) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_SourcePackageFamilyName(self: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IReplaceAppointmentOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompleted(self: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IReplaceAppointmentOperation, itemId: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def ReportCanceled(self: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IReplaceAppointmentOperation) -> Void: ...
    @winrt_mixinmethod
    def ReportError(self: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IReplaceAppointmentOperation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def DismissUI(self: win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.IReplaceAppointmentOperation) -> Void: ...
    AppointmentId = property(get_AppointmentId, None)
    AppointmentInformation = property(get_AppointmentInformation, None)
    InstanceStartDate = property(get_InstanceStartDate, None)
    SourcePackageFamilyName = property(get_SourcePackageFamilyName, None)
make_ready(__name__)
