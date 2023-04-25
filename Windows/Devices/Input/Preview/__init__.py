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
import Windows.Devices.HumanInterfaceDevice
import Windows.Devices.Input.Preview
import Windows.Foundation
import Windows.Foundation.Collections
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
GazeDeviceConfigurationStatePreview = Int32
GazeDeviceConfigurationStatePreview_Unknown: GazeDeviceConfigurationStatePreview = 0
GazeDeviceConfigurationStatePreview_Ready: GazeDeviceConfigurationStatePreview = 1
GazeDeviceConfigurationStatePreview_Configuring: GazeDeviceConfigurationStatePreview = 2
GazeDeviceConfigurationStatePreview_ScreenSetupNeeded: GazeDeviceConfigurationStatePreview = 3
GazeDeviceConfigurationStatePreview_UserCalibrationNeeded: GazeDeviceConfigurationStatePreview = 4
class GazeDevicePreview(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Input.Preview.GazeDevicePreview'
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.Input.Preview.IGazeDevicePreview) -> UInt32: ...
    @winrt_mixinmethod
    def get_CanTrackEyes(self: Windows.Devices.Input.Preview.IGazeDevicePreview) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanTrackHead(self: Windows.Devices.Input.Preview.IGazeDevicePreview) -> Boolean: ...
    @winrt_mixinmethod
    def get_ConfigurationState(self: Windows.Devices.Input.Preview.IGazeDevicePreview) -> Windows.Devices.Input.Preview.GazeDeviceConfigurationStatePreview: ...
    @winrt_mixinmethod
    def RequestCalibrationAsync(self: Windows.Devices.Input.Preview.IGazeDevicePreview) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def GetNumericControlDescriptions(self: Windows.Devices.Input.Preview.IGazeDevicePreview, usagePage: UInt16, usageId: UInt16) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.HumanInterfaceDevice.HidNumericControlDescription]: ...
    @winrt_mixinmethod
    def GetBooleanControlDescriptions(self: Windows.Devices.Input.Preview.IGazeDevicePreview, usagePage: UInt16, usageId: UInt16) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.HumanInterfaceDevice.HidBooleanControlDescription]: ...
    Id = property(get_Id, None)
    CanTrackEyes = property(get_CanTrackEyes, None)
    CanTrackHead = property(get_CanTrackHead, None)
    ConfigurationState = property(get_ConfigurationState, None)
class GazeDeviceWatcherAddedPreviewEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Input.Preview.GazeDeviceWatcherAddedPreviewEventArgs'
    @winrt_mixinmethod
    def get_Device(self: Windows.Devices.Input.Preview.IGazeDeviceWatcherAddedPreviewEventArgs) -> Windows.Devices.Input.Preview.GazeDevicePreview: ...
    Device = property(get_Device, None)
class GazeDeviceWatcherPreview(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Input.Preview.GazeDeviceWatcherPreview'
    @winrt_mixinmethod
    def add_Added(self: Windows.Devices.Input.Preview.IGazeDeviceWatcherPreview, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.Preview.GazeDeviceWatcherPreview, Windows.Devices.Input.Preview.GazeDeviceWatcherAddedPreviewEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Added(self: Windows.Devices.Input.Preview.IGazeDeviceWatcherPreview, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Removed(self: Windows.Devices.Input.Preview.IGazeDeviceWatcherPreview, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.Preview.GazeDeviceWatcherPreview, Windows.Devices.Input.Preview.GazeDeviceWatcherRemovedPreviewEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Removed(self: Windows.Devices.Input.Preview.IGazeDeviceWatcherPreview, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Updated(self: Windows.Devices.Input.Preview.IGazeDeviceWatcherPreview, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.Preview.GazeDeviceWatcherPreview, Windows.Devices.Input.Preview.GazeDeviceWatcherUpdatedPreviewEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Updated(self: Windows.Devices.Input.Preview.IGazeDeviceWatcherPreview, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: Windows.Devices.Input.Preview.IGazeDeviceWatcherPreview, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.Preview.GazeDeviceWatcherPreview, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: Windows.Devices.Input.Preview.IGazeDeviceWatcherPreview, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Start(self: Windows.Devices.Input.Preview.IGazeDeviceWatcherPreview) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Devices.Input.Preview.IGazeDeviceWatcherPreview) -> Void: ...
class GazeDeviceWatcherRemovedPreviewEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Input.Preview.GazeDeviceWatcherRemovedPreviewEventArgs'
    @winrt_mixinmethod
    def get_Device(self: Windows.Devices.Input.Preview.IGazeDeviceWatcherRemovedPreviewEventArgs) -> Windows.Devices.Input.Preview.GazeDevicePreview: ...
    Device = property(get_Device, None)
class GazeDeviceWatcherUpdatedPreviewEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Input.Preview.GazeDeviceWatcherUpdatedPreviewEventArgs'
    @winrt_mixinmethod
    def get_Device(self: Windows.Devices.Input.Preview.IGazeDeviceWatcherUpdatedPreviewEventArgs) -> Windows.Devices.Input.Preview.GazeDevicePreview: ...
    Device = property(get_Device, None)
class GazeEnteredPreviewEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Input.Preview.GazeEnteredPreviewEventArgs'
    @winrt_mixinmethod
    def get_Handled(self: Windows.Devices.Input.Preview.IGazeEnteredPreviewEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.Devices.Input.Preview.IGazeEnteredPreviewEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CurrentPoint(self: Windows.Devices.Input.Preview.IGazeEnteredPreviewEventArgs) -> Windows.Devices.Input.Preview.GazePointPreview: ...
    Handled = property(get_Handled, put_Handled)
    CurrentPoint = property(get_CurrentPoint, None)
class GazeExitedPreviewEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Input.Preview.GazeExitedPreviewEventArgs'
    @winrt_mixinmethod
    def get_Handled(self: Windows.Devices.Input.Preview.IGazeExitedPreviewEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.Devices.Input.Preview.IGazeExitedPreviewEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CurrentPoint(self: Windows.Devices.Input.Preview.IGazeExitedPreviewEventArgs) -> Windows.Devices.Input.Preview.GazePointPreview: ...
    Handled = property(get_Handled, put_Handled)
    CurrentPoint = property(get_CurrentPoint, None)
class GazeInputSourcePreview(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Input.Preview.GazeInputSourcePreview'
    @winrt_mixinmethod
    def add_GazeMoved(self: Windows.Devices.Input.Preview.IGazeInputSourcePreview, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.Preview.GazeInputSourcePreview, Windows.Devices.Input.Preview.GazeMovedPreviewEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GazeMoved(self: Windows.Devices.Input.Preview.IGazeInputSourcePreview, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_GazeEntered(self: Windows.Devices.Input.Preview.IGazeInputSourcePreview, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.Preview.GazeInputSourcePreview, Windows.Devices.Input.Preview.GazeEnteredPreviewEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GazeEntered(self: Windows.Devices.Input.Preview.IGazeInputSourcePreview, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_GazeExited(self: Windows.Devices.Input.Preview.IGazeInputSourcePreview, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.Preview.GazeInputSourcePreview, Windows.Devices.Input.Preview.GazeExitedPreviewEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GazeExited(self: Windows.Devices.Input.Preview.IGazeInputSourcePreview, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.Devices.Input.Preview.IGazeInputSourcePreviewStatics) -> Windows.Devices.Input.Preview.GazeInputSourcePreview: ...
    @winrt_classmethod
    def CreateWatcher(cls: Windows.Devices.Input.Preview.IGazeInputSourcePreviewStatics) -> Windows.Devices.Input.Preview.GazeDeviceWatcherPreview: ...
class GazeMovedPreviewEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Input.Preview.GazeMovedPreviewEventArgs'
    @winrt_mixinmethod
    def get_Handled(self: Windows.Devices.Input.Preview.IGazeMovedPreviewEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.Devices.Input.Preview.IGazeMovedPreviewEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CurrentPoint(self: Windows.Devices.Input.Preview.IGazeMovedPreviewEventArgs) -> Windows.Devices.Input.Preview.GazePointPreview: ...
    @winrt_mixinmethod
    def GetIntermediatePoints(self: Windows.Devices.Input.Preview.IGazeMovedPreviewEventArgs) -> Windows.Foundation.Collections.IVector[Windows.Devices.Input.Preview.GazePointPreview]: ...
    Handled = property(get_Handled, put_Handled)
    CurrentPoint = property(get_CurrentPoint, None)
class GazePointPreview(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Input.Preview.GazePointPreview'
    @winrt_mixinmethod
    def get_SourceDevice(self: Windows.Devices.Input.Preview.IGazePointPreview) -> Windows.Devices.Input.Preview.GazeDevicePreview: ...
    @winrt_mixinmethod
    def get_EyeGazePosition(self: Windows.Devices.Input.Preview.IGazePointPreview) -> Windows.Foundation.IReference[Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def get_HeadGazePosition(self: Windows.Devices.Input.Preview.IGazePointPreview) -> Windows.Foundation.IReference[Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Input.Preview.IGazePointPreview) -> UInt64: ...
    @winrt_mixinmethod
    def get_HidInputReport(self: Windows.Devices.Input.Preview.IGazePointPreview) -> Windows.Devices.HumanInterfaceDevice.HidInputReport: ...
    SourceDevice = property(get_SourceDevice, None)
    EyeGazePosition = property(get_EyeGazePosition, None)
    HeadGazePosition = property(get_HeadGazePosition, None)
    Timestamp = property(get_Timestamp, None)
    HidInputReport = property(get_HidInputReport, None)
class IGazeDevicePreview(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e79e7ee9-b389-11e7-b2-01-c8-d3-ff-b7-57-21')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_CanTrackEyes(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_CanTrackHead(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_ConfigurationState(self) -> Windows.Devices.Input.Preview.GazeDeviceConfigurationStatePreview: ...
    @winrt_commethod(10)
    def RequestCalibrationAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(11)
    def GetNumericControlDescriptions(self, usagePage: UInt16, usageId: UInt16) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.HumanInterfaceDevice.HidNumericControlDescription]: ...
    @winrt_commethod(12)
    def GetBooleanControlDescriptions(self, usagePage: UInt16, usageId: UInt16) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.HumanInterfaceDevice.HidBooleanControlDescription]: ...
    Id = property(get_Id, None)
    CanTrackEyes = property(get_CanTrackEyes, None)
    CanTrackHead = property(get_CanTrackHead, None)
    ConfigurationState = property(get_ConfigurationState, None)
class IGazeDeviceWatcherAddedPreviewEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e79e7eed-b389-11e7-b2-01-c8-d3-ff-b7-57-21')
    @winrt_commethod(6)
    def get_Device(self) -> Windows.Devices.Input.Preview.GazeDevicePreview: ...
    Device = property(get_Device, None)
class IGazeDeviceWatcherPreview(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e79e7ee7-b389-11e7-b2-01-c8-d3-ff-b7-57-21')
    @winrt_commethod(6)
    def add_Added(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.Preview.GazeDeviceWatcherPreview, Windows.Devices.Input.Preview.GazeDeviceWatcherAddedPreviewEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Added(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Removed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.Preview.GazeDeviceWatcherPreview, Windows.Devices.Input.Preview.GazeDeviceWatcherRemovedPreviewEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Removed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Updated(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.Preview.GazeDeviceWatcherPreview, Windows.Devices.Input.Preview.GazeDeviceWatcherUpdatedPreviewEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Updated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_EnumerationCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.Preview.GazeDeviceWatcherPreview, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_EnumerationCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def Start(self) -> Void: ...
    @winrt_commethod(15)
    def Stop(self) -> Void: ...
class IGazeDeviceWatcherRemovedPreviewEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f2631f08-0e3f-431f-a6-06-50-b3-5a-f9-4a-1c')
    @winrt_commethod(6)
    def get_Device(self) -> Windows.Devices.Input.Preview.GazeDevicePreview: ...
    Device = property(get_Device, None)
class IGazeDeviceWatcherUpdatedPreviewEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7fe830ef-7f08-4737-88-e1-4a-83-ae-4e-48-85')
    @winrt_commethod(6)
    def get_Device(self) -> Windows.Devices.Input.Preview.GazeDevicePreview: ...
    Device = property(get_Device, None)
class IGazeEnteredPreviewEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2567bf43-1225-489f-9d-d1-da-a7-c5-0f-bf-4b')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_CurrentPoint(self) -> Windows.Devices.Input.Preview.GazePointPreview: ...
    Handled = property(get_Handled, put_Handled)
    CurrentPoint = property(get_CurrentPoint, None)
class IGazeExitedPreviewEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5d0af07e-7d83-40ef-9f-0a-fb-c1-bb-dc-c5-ac')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_CurrentPoint(self) -> Windows.Devices.Input.Preview.GazePointPreview: ...
    Handled = property(get_Handled, put_Handled)
    CurrentPoint = property(get_CurrentPoint, None)
class IGazeInputSourcePreview(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e79e7ee8-b389-11e7-b2-01-c8-d3-ff-b7-57-21')
    @winrt_commethod(6)
    def add_GazeMoved(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.Preview.GazeInputSourcePreview, Windows.Devices.Input.Preview.GazeMovedPreviewEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_GazeMoved(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_GazeEntered(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.Preview.GazeInputSourcePreview, Windows.Devices.Input.Preview.GazeEnteredPreviewEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_GazeEntered(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_GazeExited(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.Preview.GazeInputSourcePreview, Windows.Devices.Input.Preview.GazeExitedPreviewEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_GazeExited(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IGazeInputSourcePreviewStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e79e7ee6-b389-11e7-b2-01-c8-d3-ff-b7-57-21')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.Devices.Input.Preview.GazeInputSourcePreview: ...
    @winrt_commethod(7)
    def CreateWatcher(self) -> Windows.Devices.Input.Preview.GazeDeviceWatcherPreview: ...
class IGazeMovedPreviewEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e79e7eeb-b389-11e7-b2-01-c8-d3-ff-b7-57-21')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_CurrentPoint(self) -> Windows.Devices.Input.Preview.GazePointPreview: ...
    @winrt_commethod(9)
    def GetIntermediatePoints(self) -> Windows.Foundation.Collections.IVector[Windows.Devices.Input.Preview.GazePointPreview]: ...
    Handled = property(get_Handled, put_Handled)
    CurrentPoint = property(get_CurrentPoint, None)
class IGazePointPreview(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e79e7eea-b389-11e7-b2-01-c8-d3-ff-b7-57-21')
    @winrt_commethod(6)
    def get_SourceDevice(self) -> Windows.Devices.Input.Preview.GazeDevicePreview: ...
    @winrt_commethod(7)
    def get_EyeGazePosition(self) -> Windows.Foundation.IReference[Windows.Foundation.Point]: ...
    @winrt_commethod(8)
    def get_HeadGazePosition(self) -> Windows.Foundation.IReference[Windows.Foundation.Point]: ...
    @winrt_commethod(9)
    def get_Timestamp(self) -> UInt64: ...
    @winrt_commethod(10)
    def get_HidInputReport(self) -> Windows.Devices.HumanInterfaceDevice.HidInputReport: ...
    SourceDevice = property(get_SourceDevice, None)
    EyeGazePosition = property(get_EyeGazePosition, None)
    HeadGazePosition = property(get_HeadGazePosition, None)
    Timestamp = property(get_Timestamp, None)
    HidInputReport = property(get_HidInputReport, None)
make_head(_module, 'GazeDevicePreview')
make_head(_module, 'GazeDeviceWatcherAddedPreviewEventArgs')
make_head(_module, 'GazeDeviceWatcherPreview')
make_head(_module, 'GazeDeviceWatcherRemovedPreviewEventArgs')
make_head(_module, 'GazeDeviceWatcherUpdatedPreviewEventArgs')
make_head(_module, 'GazeEnteredPreviewEventArgs')
make_head(_module, 'GazeExitedPreviewEventArgs')
make_head(_module, 'GazeInputSourcePreview')
make_head(_module, 'GazeMovedPreviewEventArgs')
make_head(_module, 'GazePointPreview')
make_head(_module, 'IGazeDevicePreview')
make_head(_module, 'IGazeDeviceWatcherAddedPreviewEventArgs')
make_head(_module, 'IGazeDeviceWatcherPreview')
make_head(_module, 'IGazeDeviceWatcherRemovedPreviewEventArgs')
make_head(_module, 'IGazeDeviceWatcherUpdatedPreviewEventArgs')
make_head(_module, 'IGazeEnteredPreviewEventArgs')
make_head(_module, 'IGazeExitedPreviewEventArgs')
make_head(_module, 'IGazeInputSourcePreview')
make_head(_module, 'IGazeInputSourcePreviewStatics')
make_head(_module, 'IGazeMovedPreviewEventArgs')
make_head(_module, 'IGazePointPreview')
