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
import Windows.Devices.Sensors
import Windows.Foundation
import Windows.System.Preview
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
HingeState = Int32
HingeState_Unknown: HingeState = 0
HingeState_Closed: HingeState = 1
HingeState_Concave: HingeState = 2
HingeState_Flat: HingeState = 3
HingeState_Convex: HingeState = 4
HingeState_Full: HingeState = 5
class ITwoPanelHingedDevicePosturePreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('72245c31-4b39-42a6-8e-73-72-35-ad-e1-68-53')
    @winrt_commethod(6)
    def GetCurrentPostureAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.System.Preview.TwoPanelHingedDevicePosturePreviewReading]: ...
    @winrt_commethod(7)
    def add_PostureChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.Preview.TwoPanelHingedDevicePosturePreview, Windows.System.Preview.TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_PostureChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ITwoPanelHingedDevicePosturePreviewReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a0251452-4ad6-4b38-84-26-c5-9a-15-49-3a-7d')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_HingeState(self) -> Windows.System.Preview.HingeState: ...
    @winrt_commethod(8)
    def get_Panel1Orientation(self) -> Windows.Devices.Sensors.SimpleOrientation: ...
    @winrt_commethod(9)
    def get_Panel1Id(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Panel2Orientation(self) -> Windows.Devices.Sensors.SimpleOrientation: ...
    @winrt_commethod(11)
    def get_Panel2Id(self) -> WinRT_String: ...
    Timestamp = property(get_Timestamp, None)
    HingeState = property(get_HingeState, None)
    Panel1Orientation = property(get_Panel1Orientation, None)
    Panel1Id = property(get_Panel1Id, None)
    Panel2Orientation = property(get_Panel2Orientation, None)
    Panel2Id = property(get_Panel2Id, None)
class ITwoPanelHingedDevicePosturePreviewReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2d2d1bc6-02ce-474a-a5-56-a7-5b-1c-f9-3a-03')
    @winrt_commethod(6)
    def get_Reading(self) -> Windows.System.Preview.TwoPanelHingedDevicePosturePreviewReading: ...
    Reading = property(get_Reading, None)
class ITwoPanelHingedDevicePosturePreviewStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0c4733d2-57e0-4180-bd-5e-f3-1a-21-38-42-3e')
    @winrt_commethod(6)
    def GetDefaultAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.System.Preview.TwoPanelHingedDevicePosturePreview]: ...
class TwoPanelHingedDevicePosturePreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Preview.TwoPanelHingedDevicePosturePreview'
    @winrt_mixinmethod
    def GetCurrentPostureAsync(self: Windows.System.Preview.ITwoPanelHingedDevicePosturePreview) -> Windows.Foundation.IAsyncOperation[Windows.System.Preview.TwoPanelHingedDevicePosturePreviewReading]: ...
    @winrt_mixinmethod
    def add_PostureChanged(self: Windows.System.Preview.ITwoPanelHingedDevicePosturePreview, handler: Windows.Foundation.TypedEventHandler[Windows.System.Preview.TwoPanelHingedDevicePosturePreview, Windows.System.Preview.TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PostureChanged(self: Windows.System.Preview.ITwoPanelHingedDevicePosturePreview, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: Windows.System.Preview.ITwoPanelHingedDevicePosturePreviewStatics) -> Windows.Foundation.IAsyncOperation[Windows.System.Preview.TwoPanelHingedDevicePosturePreview]: ...
class TwoPanelHingedDevicePosturePreviewReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Preview.TwoPanelHingedDevicePosturePreviewReading'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.System.Preview.ITwoPanelHingedDevicePosturePreviewReading) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_HingeState(self: Windows.System.Preview.ITwoPanelHingedDevicePosturePreviewReading) -> Windows.System.Preview.HingeState: ...
    @winrt_mixinmethod
    def get_Panel1Orientation(self: Windows.System.Preview.ITwoPanelHingedDevicePosturePreviewReading) -> Windows.Devices.Sensors.SimpleOrientation: ...
    @winrt_mixinmethod
    def get_Panel1Id(self: Windows.System.Preview.ITwoPanelHingedDevicePosturePreviewReading) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Panel2Orientation(self: Windows.System.Preview.ITwoPanelHingedDevicePosturePreviewReading) -> Windows.Devices.Sensors.SimpleOrientation: ...
    @winrt_mixinmethod
    def get_Panel2Id(self: Windows.System.Preview.ITwoPanelHingedDevicePosturePreviewReading) -> WinRT_String: ...
    Timestamp = property(get_Timestamp, None)
    HingeState = property(get_HingeState, None)
    Panel1Orientation = property(get_Panel1Orientation, None)
    Panel1Id = property(get_Panel1Id, None)
    Panel2Orientation = property(get_Panel2Orientation, None)
    Panel2Id = property(get_Panel2Id, None)
class TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Preview.TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs'
    @winrt_mixinmethod
    def get_Reading(self: Windows.System.Preview.ITwoPanelHingedDevicePosturePreviewReadingChangedEventArgs) -> Windows.System.Preview.TwoPanelHingedDevicePosturePreviewReading: ...
    Reading = property(get_Reading, None)
make_head(_module, 'ITwoPanelHingedDevicePosturePreview')
make_head(_module, 'ITwoPanelHingedDevicePosturePreviewReading')
make_head(_module, 'ITwoPanelHingedDevicePosturePreviewReadingChangedEventArgs')
make_head(_module, 'ITwoPanelHingedDevicePosturePreviewStatics')
make_head(_module, 'TwoPanelHingedDevicePosturePreview')
make_head(_module, 'TwoPanelHingedDevicePosturePreviewReading')
make_head(_module, 'TwoPanelHingedDevicePosturePreviewReadingChangedEventArgs')
