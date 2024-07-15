from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Sensors
import win32more.Windows.Foundation
import win32more.Windows.System.Preview
import win32more.Windows.Win32.System.WinRT
class HingeState(Enum, Int32):
    Unknown = 0
    Closed = 1
    Concave = 2
    Flat = 3
    Convex = 4
    Full = 5
class ITwoPanelHingedDevicePosturePreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Preview.ITwoPanelHingedDevicePosturePreview'
    _iid_ = Guid('{72245c31-4b39-42a6-8e73-7235ade16853}')
    @winrt_commethod(6)
    def GetCurrentPostureAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.Preview.TwoPanelHingedDevicePosturePreviewReading]: ...
    @winrt_commethod(7)
    def add_PostureChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.Preview.TwoPanelHingedDevicePosturePreview, win32more.Windows.System.Preview.TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_PostureChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    PostureChanged = event()
class ITwoPanelHingedDevicePosturePreviewReading(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Preview.ITwoPanelHingedDevicePosturePreviewReading'
    _iid_ = Guid('{a0251452-4ad6-4b38-8426-c59a15493a7d}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_HingeState(self) -> win32more.Windows.System.Preview.HingeState: ...
    @winrt_commethod(8)
    def get_Panel1Orientation(self) -> win32more.Windows.Devices.Sensors.SimpleOrientation: ...
    @winrt_commethod(9)
    def get_Panel1Id(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Panel2Orientation(self) -> win32more.Windows.Devices.Sensors.SimpleOrientation: ...
    @winrt_commethod(11)
    def get_Panel2Id(self) -> WinRT_String: ...
    HingeState = property(get_HingeState, None)
    Panel1Id = property(get_Panel1Id, None)
    Panel1Orientation = property(get_Panel1Orientation, None)
    Panel2Id = property(get_Panel2Id, None)
    Panel2Orientation = property(get_Panel2Orientation, None)
    Timestamp = property(get_Timestamp, None)
class ITwoPanelHingedDevicePosturePreviewReadingChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Preview.ITwoPanelHingedDevicePosturePreviewReadingChangedEventArgs'
    _iid_ = Guid('{2d2d1bc6-02ce-474a-a556-a75b1cf93a03}')
    @winrt_commethod(6)
    def get_Reading(self) -> win32more.Windows.System.Preview.TwoPanelHingedDevicePosturePreviewReading: ...
    Reading = property(get_Reading, None)
class ITwoPanelHingedDevicePosturePreviewStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Preview.ITwoPanelHingedDevicePosturePreviewStatics'
    _iid_ = Guid('{0c4733d2-57e0-4180-bd5e-f31a2138423e}')
    @winrt_commethod(6)
    def GetDefaultAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.Preview.TwoPanelHingedDevicePosturePreview]: ...
class TwoPanelHingedDevicePosturePreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.Preview.ITwoPanelHingedDevicePosturePreview
    _classid_ = 'Windows.System.Preview.TwoPanelHingedDevicePosturePreview'
    @winrt_mixinmethod
    def GetCurrentPostureAsync(self: win32more.Windows.System.Preview.ITwoPanelHingedDevicePosturePreview) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.Preview.TwoPanelHingedDevicePosturePreviewReading]: ...
    @winrt_mixinmethod
    def add_PostureChanged(self: win32more.Windows.System.Preview.ITwoPanelHingedDevicePosturePreview, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.Preview.TwoPanelHingedDevicePosturePreview, win32more.Windows.System.Preview.TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PostureChanged(self: win32more.Windows.System.Preview.ITwoPanelHingedDevicePosturePreview, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: win32more.Windows.System.Preview.ITwoPanelHingedDevicePosturePreviewStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.Preview.TwoPanelHingedDevicePosturePreview]: ...
    PostureChanged = event()
class TwoPanelHingedDevicePosturePreviewReading(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.Preview.ITwoPanelHingedDevicePosturePreviewReading
    _classid_ = 'Windows.System.Preview.TwoPanelHingedDevicePosturePreviewReading'
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.System.Preview.ITwoPanelHingedDevicePosturePreviewReading) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_HingeState(self: win32more.Windows.System.Preview.ITwoPanelHingedDevicePosturePreviewReading) -> win32more.Windows.System.Preview.HingeState: ...
    @winrt_mixinmethod
    def get_Panel1Orientation(self: win32more.Windows.System.Preview.ITwoPanelHingedDevicePosturePreviewReading) -> win32more.Windows.Devices.Sensors.SimpleOrientation: ...
    @winrt_mixinmethod
    def get_Panel1Id(self: win32more.Windows.System.Preview.ITwoPanelHingedDevicePosturePreviewReading) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Panel2Orientation(self: win32more.Windows.System.Preview.ITwoPanelHingedDevicePosturePreviewReading) -> win32more.Windows.Devices.Sensors.SimpleOrientation: ...
    @winrt_mixinmethod
    def get_Panel2Id(self: win32more.Windows.System.Preview.ITwoPanelHingedDevicePosturePreviewReading) -> WinRT_String: ...
    HingeState = property(get_HingeState, None)
    Panel1Id = property(get_Panel1Id, None)
    Panel1Orientation = property(get_Panel1Orientation, None)
    Panel2Id = property(get_Panel2Id, None)
    Panel2Orientation = property(get_Panel2Orientation, None)
    Timestamp = property(get_Timestamp, None)
class TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.Preview.ITwoPanelHingedDevicePosturePreviewReadingChangedEventArgs
    _classid_ = 'Windows.System.Preview.TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs'
    @winrt_mixinmethod
    def get_Reading(self: win32more.Windows.System.Preview.ITwoPanelHingedDevicePosturePreviewReadingChangedEventArgs) -> win32more.Windows.System.Preview.TwoPanelHingedDevicePosturePreviewReading: ...
    Reading = property(get_Reading, None)


make_ready(__name__)
