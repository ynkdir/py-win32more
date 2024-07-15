from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Appointments
import win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider
import win32more.Windows.Foundation
import win32more.Windows.Win32.System.WinRT
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
    _AppointmentsProviderLaunchActionVerbs_Meta_.AddAppointment = property(get_AddAppointment, None)
    _AppointmentsProviderLaunchActionVerbs_Meta_.RemoveAppointment = property(get_RemoveAppointment, None)
    _AppointmentsProviderLaunchActionVerbs_Meta_.ReplaceAppointment = property(get_ReplaceAppointment, None)
    _AppointmentsProviderLaunchActionVerbs_Meta_.ShowAppointmentDetails = property(get_ShowAppointmentDetails, None)
    _AppointmentsProviderLaunchActionVerbs_Meta_.ShowTimeFrame = property(get_ShowTimeFrame, None)
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
    RemoveAppointment = property(get_RemoveAppointment, None)
    ReplaceAppointment = property(get_ReplaceAppointment, None)
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
