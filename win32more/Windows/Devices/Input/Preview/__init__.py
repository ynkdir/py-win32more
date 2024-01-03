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
import win32more.Windows.Devices.HumanInterfaceDevice
import win32more.Windows.Devices.Input.Preview
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
GazeDeviceConfigurationStatePreview = Int32
GazeDeviceConfigurationStatePreview_Unknown: GazeDeviceConfigurationStatePreview = 0
GazeDeviceConfigurationStatePreview_Ready: GazeDeviceConfigurationStatePreview = 1
GazeDeviceConfigurationStatePreview_Configuring: GazeDeviceConfigurationStatePreview = 2
GazeDeviceConfigurationStatePreview_ScreenSetupNeeded: GazeDeviceConfigurationStatePreview = 3
GazeDeviceConfigurationStatePreview_UserCalibrationNeeded: GazeDeviceConfigurationStatePreview = 4
class GazeDevicePreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Input.Preview.IGazeDevicePreview
    _classid_ = 'Windows.Devices.Input.Preview.GazeDevicePreview'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.Input.Preview.IGazeDevicePreview) -> UInt32: ...
    @winrt_mixinmethod
    def get_CanTrackEyes(self: win32more.Windows.Devices.Input.Preview.IGazeDevicePreview) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanTrackHead(self: win32more.Windows.Devices.Input.Preview.IGazeDevicePreview) -> Boolean: ...
    @winrt_mixinmethod
    def get_ConfigurationState(self: win32more.Windows.Devices.Input.Preview.IGazeDevicePreview) -> win32more.Windows.Devices.Input.Preview.GazeDeviceConfigurationStatePreview: ...
    @winrt_mixinmethod
    def RequestCalibrationAsync(self: win32more.Windows.Devices.Input.Preview.IGazeDevicePreview) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def GetNumericControlDescriptions(self: win32more.Windows.Devices.Input.Preview.IGazeDevicePreview, usagePage: UInt16, usageId: UInt16) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.HumanInterfaceDevice.HidNumericControlDescription]: ...
    @winrt_mixinmethod
    def GetBooleanControlDescriptions(self: win32more.Windows.Devices.Input.Preview.IGazeDevicePreview, usagePage: UInt16, usageId: UInt16) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControlDescription]: ...
    Id = property(get_Id, None)
    CanTrackEyes = property(get_CanTrackEyes, None)
    CanTrackHead = property(get_CanTrackHead, None)
    ConfigurationState = property(get_ConfigurationState, None)
class GazeDeviceWatcherAddedPreviewEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Input.Preview.IGazeDeviceWatcherAddedPreviewEventArgs
    _classid_ = 'Windows.Devices.Input.Preview.GazeDeviceWatcherAddedPreviewEventArgs'
    @winrt_mixinmethod
    def get_Device(self: win32more.Windows.Devices.Input.Preview.IGazeDeviceWatcherAddedPreviewEventArgs) -> win32more.Windows.Devices.Input.Preview.GazeDevicePreview: ...
    Device = property(get_Device, None)
class GazeDeviceWatcherPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Input.Preview.IGazeDeviceWatcherPreview
    _classid_ = 'Windows.Devices.Input.Preview.GazeDeviceWatcherPreview'
    @winrt_mixinmethod
    def add_Added(self: win32more.Windows.Devices.Input.Preview.IGazeDeviceWatcherPreview, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.Preview.GazeDeviceWatcherPreview, win32more.Windows.Devices.Input.Preview.GazeDeviceWatcherAddedPreviewEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Added(self: win32more.Windows.Devices.Input.Preview.IGazeDeviceWatcherPreview, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Removed(self: win32more.Windows.Devices.Input.Preview.IGazeDeviceWatcherPreview, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.Preview.GazeDeviceWatcherPreview, win32more.Windows.Devices.Input.Preview.GazeDeviceWatcherRemovedPreviewEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Removed(self: win32more.Windows.Devices.Input.Preview.IGazeDeviceWatcherPreview, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Updated(self: win32more.Windows.Devices.Input.Preview.IGazeDeviceWatcherPreview, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.Preview.GazeDeviceWatcherPreview, win32more.Windows.Devices.Input.Preview.GazeDeviceWatcherUpdatedPreviewEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Updated(self: win32more.Windows.Devices.Input.Preview.IGazeDeviceWatcherPreview, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnumerationCompleted(self: win32more.Windows.Devices.Input.Preview.IGazeDeviceWatcherPreview, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.Preview.GazeDeviceWatcherPreview, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnumerationCompleted(self: win32more.Windows.Devices.Input.Preview.IGazeDeviceWatcherPreview, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Devices.Input.Preview.IGazeDeviceWatcherPreview) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Devices.Input.Preview.IGazeDeviceWatcherPreview) -> Void: ...
class GazeDeviceWatcherRemovedPreviewEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Input.Preview.IGazeDeviceWatcherRemovedPreviewEventArgs
    _classid_ = 'Windows.Devices.Input.Preview.GazeDeviceWatcherRemovedPreviewEventArgs'
    @winrt_mixinmethod
    def get_Device(self: win32more.Windows.Devices.Input.Preview.IGazeDeviceWatcherRemovedPreviewEventArgs) -> win32more.Windows.Devices.Input.Preview.GazeDevicePreview: ...
    Device = property(get_Device, None)
class GazeDeviceWatcherUpdatedPreviewEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Input.Preview.IGazeDeviceWatcherUpdatedPreviewEventArgs
    _classid_ = 'Windows.Devices.Input.Preview.GazeDeviceWatcherUpdatedPreviewEventArgs'
    @winrt_mixinmethod
    def get_Device(self: win32more.Windows.Devices.Input.Preview.IGazeDeviceWatcherUpdatedPreviewEventArgs) -> win32more.Windows.Devices.Input.Preview.GazeDevicePreview: ...
    Device = property(get_Device, None)
class GazeEnteredPreviewEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Input.Preview.IGazeEnteredPreviewEventArgs
    _classid_ = 'Windows.Devices.Input.Preview.GazeEnteredPreviewEventArgs'
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.Devices.Input.Preview.IGazeEnteredPreviewEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.Devices.Input.Preview.IGazeEnteredPreviewEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CurrentPoint(self: win32more.Windows.Devices.Input.Preview.IGazeEnteredPreviewEventArgs) -> win32more.Windows.Devices.Input.Preview.GazePointPreview: ...
    Handled = property(get_Handled, put_Handled)
    CurrentPoint = property(get_CurrentPoint, None)
class GazeExitedPreviewEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Input.Preview.IGazeExitedPreviewEventArgs
    _classid_ = 'Windows.Devices.Input.Preview.GazeExitedPreviewEventArgs'
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.Devices.Input.Preview.IGazeExitedPreviewEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.Devices.Input.Preview.IGazeExitedPreviewEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CurrentPoint(self: win32more.Windows.Devices.Input.Preview.IGazeExitedPreviewEventArgs) -> win32more.Windows.Devices.Input.Preview.GazePointPreview: ...
    Handled = property(get_Handled, put_Handled)
    CurrentPoint = property(get_CurrentPoint, None)
class GazeInputSourcePreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Input.Preview.IGazeInputSourcePreview
    _classid_ = 'Windows.Devices.Input.Preview.GazeInputSourcePreview'
    @winrt_mixinmethod
    def add_GazeMoved(self: win32more.Windows.Devices.Input.Preview.IGazeInputSourcePreview, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.Preview.GazeInputSourcePreview, win32more.Windows.Devices.Input.Preview.GazeMovedPreviewEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GazeMoved(self: win32more.Windows.Devices.Input.Preview.IGazeInputSourcePreview, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_GazeEntered(self: win32more.Windows.Devices.Input.Preview.IGazeInputSourcePreview, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.Preview.GazeInputSourcePreview, win32more.Windows.Devices.Input.Preview.GazeEnteredPreviewEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GazeEntered(self: win32more.Windows.Devices.Input.Preview.IGazeInputSourcePreview, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_GazeExited(self: win32more.Windows.Devices.Input.Preview.IGazeInputSourcePreview, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.Preview.GazeInputSourcePreview, win32more.Windows.Devices.Input.Preview.GazeExitedPreviewEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GazeExited(self: win32more.Windows.Devices.Input.Preview.IGazeInputSourcePreview, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.Devices.Input.Preview.IGazeInputSourcePreviewStatics) -> win32more.Windows.Devices.Input.Preview.GazeInputSourcePreview: ...
    @winrt_classmethod
    def CreateWatcher(cls: win32more.Windows.Devices.Input.Preview.IGazeInputSourcePreviewStatics) -> win32more.Windows.Devices.Input.Preview.GazeDeviceWatcherPreview: ...
class GazeMovedPreviewEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Input.Preview.IGazeMovedPreviewEventArgs
    _classid_ = 'Windows.Devices.Input.Preview.GazeMovedPreviewEventArgs'
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.Devices.Input.Preview.IGazeMovedPreviewEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.Devices.Input.Preview.IGazeMovedPreviewEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CurrentPoint(self: win32more.Windows.Devices.Input.Preview.IGazeMovedPreviewEventArgs) -> win32more.Windows.Devices.Input.Preview.GazePointPreview: ...
    @winrt_mixinmethod
    def GetIntermediatePoints(self: win32more.Windows.Devices.Input.Preview.IGazeMovedPreviewEventArgs) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.Input.Preview.GazePointPreview]: ...
    Handled = property(get_Handled, put_Handled)
    CurrentPoint = property(get_CurrentPoint, None)
class GazePointPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Input.Preview.IGazePointPreview
    _classid_ = 'Windows.Devices.Input.Preview.GazePointPreview'
    @winrt_mixinmethod
    def get_SourceDevice(self: win32more.Windows.Devices.Input.Preview.IGazePointPreview) -> win32more.Windows.Devices.Input.Preview.GazeDevicePreview: ...
    @winrt_mixinmethod
    def get_EyeGazePosition(self: win32more.Windows.Devices.Input.Preview.IGazePointPreview) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def get_HeadGazePosition(self: win32more.Windows.Devices.Input.Preview.IGazePointPreview) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Input.Preview.IGazePointPreview) -> UInt64: ...
    @winrt_mixinmethod
    def get_HidInputReport(self: win32more.Windows.Devices.Input.Preview.IGazePointPreview) -> win32more.Windows.Devices.HumanInterfaceDevice.HidInputReport: ...
    SourceDevice = property(get_SourceDevice, None)
    EyeGazePosition = property(get_EyeGazePosition, None)
    HeadGazePosition = property(get_HeadGazePosition, None)
    Timestamp = property(get_Timestamp, None)
    HidInputReport = property(get_HidInputReport, None)
class IGazeDevicePreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.Preview.IGazeDevicePreview'
    _iid_ = Guid('{e79e7ee9-b389-11e7-b201-c8d3ffb75721}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_CanTrackEyes(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_CanTrackHead(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_ConfigurationState(self) -> win32more.Windows.Devices.Input.Preview.GazeDeviceConfigurationStatePreview: ...
    @winrt_commethod(10)
    def RequestCalibrationAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(11)
    def GetNumericControlDescriptions(self, usagePage: UInt16, usageId: UInt16) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.HumanInterfaceDevice.HidNumericControlDescription]: ...
    @winrt_commethod(12)
    def GetBooleanControlDescriptions(self, usagePage: UInt16, usageId: UInt16) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.HumanInterfaceDevice.HidBooleanControlDescription]: ...
    Id = property(get_Id, None)
    CanTrackEyes = property(get_CanTrackEyes, None)
    CanTrackHead = property(get_CanTrackHead, None)
    ConfigurationState = property(get_ConfigurationState, None)
class IGazeDeviceWatcherAddedPreviewEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.Preview.IGazeDeviceWatcherAddedPreviewEventArgs'
    _iid_ = Guid('{e79e7eed-b389-11e7-b201-c8d3ffb75721}')
    @winrt_commethod(6)
    def get_Device(self) -> win32more.Windows.Devices.Input.Preview.GazeDevicePreview: ...
    Device = property(get_Device, None)
class IGazeDeviceWatcherPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.Preview.IGazeDeviceWatcherPreview'
    _iid_ = Guid('{e79e7ee7-b389-11e7-b201-c8d3ffb75721}')
    @winrt_commethod(6)
    def add_Added(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.Preview.GazeDeviceWatcherPreview, win32more.Windows.Devices.Input.Preview.GazeDeviceWatcherAddedPreviewEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Added(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Removed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.Preview.GazeDeviceWatcherPreview, win32more.Windows.Devices.Input.Preview.GazeDeviceWatcherRemovedPreviewEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Removed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Updated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.Preview.GazeDeviceWatcherPreview, win32more.Windows.Devices.Input.Preview.GazeDeviceWatcherUpdatedPreviewEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Updated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_EnumerationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.Preview.GazeDeviceWatcherPreview, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_EnumerationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def Start(self) -> Void: ...
    @winrt_commethod(15)
    def Stop(self) -> Void: ...
class IGazeDeviceWatcherRemovedPreviewEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.Preview.IGazeDeviceWatcherRemovedPreviewEventArgs'
    _iid_ = Guid('{f2631f08-0e3f-431f-a606-50b35af94a1c}')
    @winrt_commethod(6)
    def get_Device(self) -> win32more.Windows.Devices.Input.Preview.GazeDevicePreview: ...
    Device = property(get_Device, None)
class IGazeDeviceWatcherUpdatedPreviewEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.Preview.IGazeDeviceWatcherUpdatedPreviewEventArgs'
    _iid_ = Guid('{7fe830ef-7f08-4737-88e1-4a83ae4e4885}')
    @winrt_commethod(6)
    def get_Device(self) -> win32more.Windows.Devices.Input.Preview.GazeDevicePreview: ...
    Device = property(get_Device, None)
class IGazeEnteredPreviewEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.Preview.IGazeEnteredPreviewEventArgs'
    _iid_ = Guid('{2567bf43-1225-489f-9dd1-daa7c50fbf4b}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_CurrentPoint(self) -> win32more.Windows.Devices.Input.Preview.GazePointPreview: ...
    Handled = property(get_Handled, put_Handled)
    CurrentPoint = property(get_CurrentPoint, None)
class IGazeExitedPreviewEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.Preview.IGazeExitedPreviewEventArgs'
    _iid_ = Guid('{5d0af07e-7d83-40ef-9f0a-fbc1bbdcc5ac}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_CurrentPoint(self) -> win32more.Windows.Devices.Input.Preview.GazePointPreview: ...
    Handled = property(get_Handled, put_Handled)
    CurrentPoint = property(get_CurrentPoint, None)
class IGazeInputSourcePreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.Preview.IGazeInputSourcePreview'
    _iid_ = Guid('{e79e7ee8-b389-11e7-b201-c8d3ffb75721}')
    @winrt_commethod(6)
    def add_GazeMoved(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.Preview.GazeInputSourcePreview, win32more.Windows.Devices.Input.Preview.GazeMovedPreviewEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_GazeMoved(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_GazeEntered(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.Preview.GazeInputSourcePreview, win32more.Windows.Devices.Input.Preview.GazeEnteredPreviewEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_GazeEntered(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_GazeExited(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.Preview.GazeInputSourcePreview, win32more.Windows.Devices.Input.Preview.GazeExitedPreviewEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_GazeExited(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IGazeInputSourcePreviewStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.Preview.IGazeInputSourcePreviewStatics'
    _iid_ = Guid('{e79e7ee6-b389-11e7-b201-c8d3ffb75721}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.Devices.Input.Preview.GazeInputSourcePreview: ...
    @winrt_commethod(7)
    def CreateWatcher(self) -> win32more.Windows.Devices.Input.Preview.GazeDeviceWatcherPreview: ...
class IGazeMovedPreviewEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.Preview.IGazeMovedPreviewEventArgs'
    _iid_ = Guid('{e79e7eeb-b389-11e7-b201-c8d3ffb75721}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_CurrentPoint(self) -> win32more.Windows.Devices.Input.Preview.GazePointPreview: ...
    @winrt_commethod(9)
    def GetIntermediatePoints(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.Input.Preview.GazePointPreview]: ...
    Handled = property(get_Handled, put_Handled)
    CurrentPoint = property(get_CurrentPoint, None)
class IGazePointPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.Preview.IGazePointPreview'
    _iid_ = Guid('{e79e7eea-b389-11e7-b201-c8d3ffb75721}')
    @winrt_commethod(6)
    def get_SourceDevice(self) -> win32more.Windows.Devices.Input.Preview.GazeDevicePreview: ...
    @winrt_commethod(7)
    def get_EyeGazePosition(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]: ...
    @winrt_commethod(8)
    def get_HeadGazePosition(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Point]: ...
    @winrt_commethod(9)
    def get_Timestamp(self) -> UInt64: ...
    @winrt_commethod(10)
    def get_HidInputReport(self) -> win32more.Windows.Devices.HumanInterfaceDevice.HidInputReport: ...
    SourceDevice = property(get_SourceDevice, None)
    EyeGazePosition = property(get_EyeGazePosition, None)
    HeadGazePosition = property(get_HeadGazePosition, None)
    Timestamp = property(get_Timestamp, None)
    HidInputReport = property(get_HidInputReport, None)


make_ready(__name__)
