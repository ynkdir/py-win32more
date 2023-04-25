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
import Windows.Devices.Perception
import Windows.Devices.Perception.Provider
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Foundation.Numerics
import Windows.Graphics.Imaging
import Windows.Media
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IKnownPerceptionFrameKindStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3ae651d6-9669-4106-9f-ae-48-35-c1-b9-61-04')
    @winrt_commethod(6)
    def get_Color(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Depth(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Infrared(self) -> WinRT_String: ...
    Color = property(get_Color, None)
    Depth = property(get_Depth, None)
    Infrared = property(get_Infrared, None)
class IPerceptionControlGroup(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('172c4882-2fd9-4c4e-ba-34-fd-f2-0a-73-dd-e5')
    @winrt_commethod(6)
    def get_FrameProviderIds(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    FrameProviderIds = property(get_FrameProviderIds, None)
class IPerceptionControlGroupFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2f1af2e0-baf1-453b-be-d4-cd-9d-46-19-15-4c')
    @winrt_commethod(6)
    def Create(self, ids: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Devices.Perception.Provider.PerceptionControlGroup: ...
class IPerceptionCorrelation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b4131a82-dff5-4047-8a-19-3b-4d-80-5f-71-76')
    @winrt_commethod(6)
    def get_TargetId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Position(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(8)
    def get_Orientation(self) -> Windows.Foundation.Numerics.Quaternion: ...
    TargetId = property(get_TargetId, None)
    Position = property(get_Position, None)
    Orientation = property(get_Orientation, None)
class IPerceptionCorrelationFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d4a6c425-2884-4a8f-81-34-28-35-d7-28-6c-bf')
    @winrt_commethod(6)
    def Create(self, targetId: WinRT_String, position: Windows.Foundation.Numerics.Vector3, orientation: Windows.Foundation.Numerics.Quaternion) -> Windows.Devices.Perception.Provider.PerceptionCorrelation: ...
class IPerceptionCorrelationGroup(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('752a0906-36a7-47bb-9b-79-56-cc-6b-74-67-70')
    @winrt_commethod(6)
    def get_RelativeLocations(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Perception.Provider.PerceptionCorrelation]: ...
    RelativeLocations = property(get_RelativeLocations, None)
class IPerceptionCorrelationGroupFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7dfe2088-63df-48ed-83-b1-4a-b8-29-13-29-95')
    @winrt_commethod(6)
    def Create(self, relativeLocations: Windows.Foundation.Collections.IIterable[Windows.Devices.Perception.Provider.PerceptionCorrelation]) -> Windows.Devices.Perception.Provider.PerceptionCorrelationGroup: ...
class IPerceptionFaceAuthenticationGroup(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e8019814-4a91-41b0-83-a6-88-1a-17-75-35-3e')
    @winrt_commethod(6)
    def get_FrameProviderIds(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    FrameProviderIds = property(get_FrameProviderIds, None)
class IPerceptionFaceAuthenticationGroupFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e68a05d4-b60c-40f4-bc-b9-f2-4d-46-46-73-20')
    @winrt_commethod(6)
    def Create(self, ids: Windows.Foundation.Collections.IIterable[WinRT_String], startHandler: Windows.Devices.Perception.Provider.PerceptionStartFaceAuthenticationHandler, stopHandler: Windows.Devices.Perception.Provider.PerceptionStopFaceAuthenticationHandler) -> Windows.Devices.Perception.Provider.PerceptionFaceAuthenticationGroup: ...
class IPerceptionFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7cfe7825-54bb-4d9d-be-c5-8e-f6-61-51-d2-ac')
    @winrt_commethod(6)
    def get_RelativeTime(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_RelativeTime(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_Properties(self) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_commethod(9)
    def get_FrameData(self) -> Windows.Foundation.IMemoryBuffer: ...
    RelativeTime = property(get_RelativeTime, put_RelativeTime)
    Properties = property(get_Properties, None)
    FrameData = property(get_FrameData, None)
class IPerceptionFrameProvider(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('794f7ab9-b37d-3b33-a1-0d-30-62-64-19-ce-65')
    @winrt_commethod(6)
    def get_FrameProviderInfo(self) -> Windows.Devices.Perception.Provider.PerceptionFrameProviderInfo: ...
    @winrt_commethod(7)
    def get_Available(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_Properties(self) -> Windows.Foundation.Collections.IPropertySet: ...
    @winrt_commethod(9)
    def Start(self) -> Void: ...
    @winrt_commethod(10)
    def Stop(self) -> Void: ...
    @winrt_commethod(11)
    def SetProperty(self, value: Windows.Devices.Perception.Provider.PerceptionPropertyChangeRequest) -> Void: ...
    FrameProviderInfo = property(get_FrameProviderInfo, None)
    Available = property(get_Available, None)
    Properties = property(get_Properties, None)
class IPerceptionFrameProviderInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cca959e8-797e-4e83-9b-87-03-6a-74-14-2f-c4')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Id(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_DeviceKind(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_DeviceKind(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_FrameKind(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_FrameKind(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_Hidden(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_Hidden(self, value: Boolean) -> Void: ...
    Id = property(get_Id, put_Id)
    DisplayName = property(get_DisplayName, put_DisplayName)
    DeviceKind = property(get_DeviceKind, put_DeviceKind)
    FrameKind = property(get_FrameKind, put_FrameKind)
    Hidden = property(get_Hidden, put_Hidden)
class IPerceptionFrameProviderManager(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a959ce07-ead3-33df-8e-c1-b9-24-ab-e0-19-c4')
    @winrt_commethod(6)
    def GetFrameProvider(self, frameProviderInfo: Windows.Devices.Perception.Provider.PerceptionFrameProviderInfo) -> Windows.Devices.Perception.Provider.IPerceptionFrameProvider: ...
class IPerceptionFrameProviderManagerServiceStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ae8386e6-cad9-4359-8f-96-8e-ae-51-81-05-26')
    @winrt_commethod(6)
    def RegisterFrameProviderInfo(self, manager: Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, frameProviderInfo: Windows.Devices.Perception.Provider.PerceptionFrameProviderInfo) -> Void: ...
    @winrt_commethod(7)
    def UnregisterFrameProviderInfo(self, manager: Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, frameProviderInfo: Windows.Devices.Perception.Provider.PerceptionFrameProviderInfo) -> Void: ...
    @winrt_commethod(8)
    def RegisterFaceAuthenticationGroup(self, manager: Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, faceAuthenticationGroup: Windows.Devices.Perception.Provider.PerceptionFaceAuthenticationGroup) -> Void: ...
    @winrt_commethod(9)
    def UnregisterFaceAuthenticationGroup(self, manager: Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, faceAuthenticationGroup: Windows.Devices.Perception.Provider.PerceptionFaceAuthenticationGroup) -> Void: ...
    @winrt_commethod(10)
    def RegisterControlGroup(self, manager: Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, controlGroup: Windows.Devices.Perception.Provider.PerceptionControlGroup) -> Void: ...
    @winrt_commethod(11)
    def UnregisterControlGroup(self, manager: Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, controlGroup: Windows.Devices.Perception.Provider.PerceptionControlGroup) -> Void: ...
    @winrt_commethod(12)
    def RegisterCorrelationGroup(self, manager: Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, correlationGroup: Windows.Devices.Perception.Provider.PerceptionCorrelationGroup) -> Void: ...
    @winrt_commethod(13)
    def UnregisterCorrelationGroup(self, manager: Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, correlationGroup: Windows.Devices.Perception.Provider.PerceptionCorrelationGroup) -> Void: ...
    @winrt_commethod(14)
    def UpdateAvailabilityForProvider(self, provider: Windows.Devices.Perception.Provider.IPerceptionFrameProvider, available: Boolean) -> Void: ...
    @winrt_commethod(15)
    def PublishFrameForProvider(self, provider: Windows.Devices.Perception.Provider.IPerceptionFrameProvider, frame: Windows.Devices.Perception.Provider.PerceptionFrame) -> Void: ...
class IPerceptionPropertyChangeRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3c5aeb51-350b-4df8-94-14-59-e0-98-15-51-0b')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Value(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(8)
    def get_Status(self) -> Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeStatus: ...
    @winrt_commethod(9)
    def put_Status(self, value: Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeStatus) -> Void: ...
    @winrt_commethod(10)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Name = property(get_Name, None)
    Value = property(get_Value, None)
    Status = property(get_Status, put_Status)
class IPerceptionVideoFrameAllocator(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4c38a7da-fdd8-4ed4-a0-39-2a-6f-9b-23-50-38')
    @winrt_commethod(6)
    def AllocateFrame(self) -> Windows.Devices.Perception.Provider.PerceptionFrame: ...
    @winrt_commethod(7)
    def CopyFromVideoFrame(self, frame: Windows.Media.VideoFrame) -> Windows.Devices.Perception.Provider.PerceptionFrame: ...
class IPerceptionVideoFrameAllocatorFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1a58b0e1-e91a-481e-b8-76-a8-9e-2b-bc-6b-33')
    @winrt_commethod(6)
    def Create(self, maxOutstandingFrameCountForWrite: UInt32, format: Windows.Graphics.Imaging.BitmapPixelFormat, resolution: Windows.Foundation.Size, alpha: Windows.Graphics.Imaging.BitmapAlphaMode) -> Windows.Devices.Perception.Provider.PerceptionVideoFrameAllocator: ...
class KnownPerceptionFrameKind(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Perception.Provider.KnownPerceptionFrameKind'
    @winrt_classmethod
    def get_Color(cls: Windows.Devices.Perception.Provider.IKnownPerceptionFrameKindStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Depth(cls: Windows.Devices.Perception.Provider.IKnownPerceptionFrameKindStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Infrared(cls: Windows.Devices.Perception.Provider.IKnownPerceptionFrameKindStatics) -> WinRT_String: ...
    Color = property(get_Color, None)
    Depth = property(get_Depth, None)
    Infrared = property(get_Infrared, None)
class PerceptionControlGroup(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Perception.Provider.PerceptionControlGroup'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.Perception.Provider.IPerceptionControlGroupFactory, ids: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Devices.Perception.Provider.PerceptionControlGroup: ...
    @winrt_mixinmethod
    def get_FrameProviderIds(self: Windows.Devices.Perception.Provider.IPerceptionControlGroup) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    FrameProviderIds = property(get_FrameProviderIds, None)
class PerceptionCorrelation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Perception.Provider.PerceptionCorrelation'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.Perception.Provider.IPerceptionCorrelationFactory, targetId: WinRT_String, position: Windows.Foundation.Numerics.Vector3, orientation: Windows.Foundation.Numerics.Quaternion) -> Windows.Devices.Perception.Provider.PerceptionCorrelation: ...
    @winrt_mixinmethod
    def get_TargetId(self: Windows.Devices.Perception.Provider.IPerceptionCorrelation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.Devices.Perception.Provider.IPerceptionCorrelation) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_Orientation(self: Windows.Devices.Perception.Provider.IPerceptionCorrelation) -> Windows.Foundation.Numerics.Quaternion: ...
    TargetId = property(get_TargetId, None)
    Position = property(get_Position, None)
    Orientation = property(get_Orientation, None)
class PerceptionCorrelationGroup(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Perception.Provider.PerceptionCorrelationGroup'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.Perception.Provider.IPerceptionCorrelationGroupFactory, relativeLocations: Windows.Foundation.Collections.IIterable[Windows.Devices.Perception.Provider.PerceptionCorrelation]) -> Windows.Devices.Perception.Provider.PerceptionCorrelationGroup: ...
    @winrt_mixinmethod
    def get_RelativeLocations(self: Windows.Devices.Perception.Provider.IPerceptionCorrelationGroup) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Perception.Provider.PerceptionCorrelation]: ...
    RelativeLocations = property(get_RelativeLocations, None)
class PerceptionFaceAuthenticationGroup(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Perception.Provider.PerceptionFaceAuthenticationGroup'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.Perception.Provider.IPerceptionFaceAuthenticationGroupFactory, ids: Windows.Foundation.Collections.IIterable[WinRT_String], startHandler: Windows.Devices.Perception.Provider.PerceptionStartFaceAuthenticationHandler, stopHandler: Windows.Devices.Perception.Provider.PerceptionStopFaceAuthenticationHandler) -> Windows.Devices.Perception.Provider.PerceptionFaceAuthenticationGroup: ...
    @winrt_mixinmethod
    def get_FrameProviderIds(self: Windows.Devices.Perception.Provider.IPerceptionFaceAuthenticationGroup) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    FrameProviderIds = property(get_FrameProviderIds, None)
class PerceptionFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Perception.Provider.PerceptionFrame'
    @winrt_mixinmethod
    def get_RelativeTime(self: Windows.Devices.Perception.Provider.IPerceptionFrame) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_RelativeTime(self: Windows.Devices.Perception.Provider.IPerceptionFrame, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.Perception.Provider.IPerceptionFrame) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_FrameData(self: Windows.Devices.Perception.Provider.IPerceptionFrame) -> Windows.Foundation.IMemoryBuffer: ...
    RelativeTime = property(get_RelativeTime, put_RelativeTime)
    Properties = property(get_Properties, None)
    FrameData = property(get_FrameData, None)
class PerceptionFrameProviderInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Perception.Provider.PerceptionFrameProviderInfo'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Perception.Provider.PerceptionFrameProviderInfo: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.Perception.Provider.IPerceptionFrameProviderInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Id(self: Windows.Devices.Perception.Provider.IPerceptionFrameProviderInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Devices.Perception.Provider.IPerceptionFrameProviderInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: Windows.Devices.Perception.Provider.IPerceptionFrameProviderInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceKind(self: Windows.Devices.Perception.Provider.IPerceptionFrameProviderInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DeviceKind(self: Windows.Devices.Perception.Provider.IPerceptionFrameProviderInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FrameKind(self: Windows.Devices.Perception.Provider.IPerceptionFrameProviderInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_FrameKind(self: Windows.Devices.Perception.Provider.IPerceptionFrameProviderInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Hidden(self: Windows.Devices.Perception.Provider.IPerceptionFrameProviderInfo) -> Boolean: ...
    @winrt_mixinmethod
    def put_Hidden(self: Windows.Devices.Perception.Provider.IPerceptionFrameProviderInfo, value: Boolean) -> Void: ...
    Id = property(get_Id, put_Id)
    DisplayName = property(get_DisplayName, put_DisplayName)
    DeviceKind = property(get_DeviceKind, put_DeviceKind)
    FrameKind = property(get_FrameKind, put_FrameKind)
    Hidden = property(get_Hidden, put_Hidden)
class PerceptionFrameProviderManagerService(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Perception.Provider.PerceptionFrameProviderManagerService'
    @winrt_classmethod
    def RegisterFrameProviderInfo(cls: Windows.Devices.Perception.Provider.IPerceptionFrameProviderManagerServiceStatics, manager: Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, frameProviderInfo: Windows.Devices.Perception.Provider.PerceptionFrameProviderInfo) -> Void: ...
    @winrt_classmethod
    def UnregisterFrameProviderInfo(cls: Windows.Devices.Perception.Provider.IPerceptionFrameProviderManagerServiceStatics, manager: Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, frameProviderInfo: Windows.Devices.Perception.Provider.PerceptionFrameProviderInfo) -> Void: ...
    @winrt_classmethod
    def RegisterFaceAuthenticationGroup(cls: Windows.Devices.Perception.Provider.IPerceptionFrameProviderManagerServiceStatics, manager: Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, faceAuthenticationGroup: Windows.Devices.Perception.Provider.PerceptionFaceAuthenticationGroup) -> Void: ...
    @winrt_classmethod
    def UnregisterFaceAuthenticationGroup(cls: Windows.Devices.Perception.Provider.IPerceptionFrameProviderManagerServiceStatics, manager: Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, faceAuthenticationGroup: Windows.Devices.Perception.Provider.PerceptionFaceAuthenticationGroup) -> Void: ...
    @winrt_classmethod
    def RegisterControlGroup(cls: Windows.Devices.Perception.Provider.IPerceptionFrameProviderManagerServiceStatics, manager: Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, controlGroup: Windows.Devices.Perception.Provider.PerceptionControlGroup) -> Void: ...
    @winrt_classmethod
    def UnregisterControlGroup(cls: Windows.Devices.Perception.Provider.IPerceptionFrameProviderManagerServiceStatics, manager: Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, controlGroup: Windows.Devices.Perception.Provider.PerceptionControlGroup) -> Void: ...
    @winrt_classmethod
    def RegisterCorrelationGroup(cls: Windows.Devices.Perception.Provider.IPerceptionFrameProviderManagerServiceStatics, manager: Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, correlationGroup: Windows.Devices.Perception.Provider.PerceptionCorrelationGroup) -> Void: ...
    @winrt_classmethod
    def UnregisterCorrelationGroup(cls: Windows.Devices.Perception.Provider.IPerceptionFrameProviderManagerServiceStatics, manager: Windows.Devices.Perception.Provider.IPerceptionFrameProviderManager, correlationGroup: Windows.Devices.Perception.Provider.PerceptionCorrelationGroup) -> Void: ...
    @winrt_classmethod
    def UpdateAvailabilityForProvider(cls: Windows.Devices.Perception.Provider.IPerceptionFrameProviderManagerServiceStatics, provider: Windows.Devices.Perception.Provider.IPerceptionFrameProvider, available: Boolean) -> Void: ...
    @winrt_classmethod
    def PublishFrameForProvider(cls: Windows.Devices.Perception.Provider.IPerceptionFrameProviderManagerServiceStatics, provider: Windows.Devices.Perception.Provider.IPerceptionFrameProvider, frame: Windows.Devices.Perception.Provider.PerceptionFrame) -> Void: ...
class PerceptionPropertyChangeRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Perception.Provider.PerceptionPropertyChangeRequest'
    @winrt_mixinmethod
    def get_Name(self: Windows.Devices.Perception.Provider.IPerceptionPropertyChangeRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Devices.Perception.Provider.IPerceptionPropertyChangeRequest) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Perception.Provider.IPerceptionPropertyChangeRequest) -> Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeStatus: ...
    @winrt_mixinmethod
    def put_Status(self: Windows.Devices.Perception.Provider.IPerceptionPropertyChangeRequest, value: Windows.Devices.Perception.PerceptionFrameSourcePropertyChangeStatus) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Devices.Perception.Provider.IPerceptionPropertyChangeRequest) -> Windows.Foundation.Deferral: ...
    Name = property(get_Name, None)
    Value = property(get_Value, None)
    Status = property(get_Status, put_Status)
class PerceptionStartFaceAuthenticationHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('74816d2a-2090-4670-8c-48-ef-39-e7-ff-7c-26')
    ClassId = 'Windows.Devices.Perception.Provider.PerceptionStartFaceAuthenticationHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Devices.Perception.Provider.PerceptionFaceAuthenticationGroup) -> Boolean: ...
class PerceptionStopFaceAuthenticationHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('387ee6aa-89cd-481e-aa-de-dd-92-f7-0b-2a-d7')
    ClassId = 'Windows.Devices.Perception.Provider.PerceptionStopFaceAuthenticationHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Devices.Perception.Provider.PerceptionFaceAuthenticationGroup) -> Void: ...
class PerceptionVideoFrameAllocator(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Perception.Provider.PerceptionVideoFrameAllocator'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.Perception.Provider.IPerceptionVideoFrameAllocatorFactory, maxOutstandingFrameCountForWrite: UInt32, format: Windows.Graphics.Imaging.BitmapPixelFormat, resolution: Windows.Foundation.Size, alpha: Windows.Graphics.Imaging.BitmapAlphaMode) -> Windows.Devices.Perception.Provider.PerceptionVideoFrameAllocator: ...
    @winrt_mixinmethod
    def AllocateFrame(self: Windows.Devices.Perception.Provider.IPerceptionVideoFrameAllocator) -> Windows.Devices.Perception.Provider.PerceptionFrame: ...
    @winrt_mixinmethod
    def CopyFromVideoFrame(self: Windows.Devices.Perception.Provider.IPerceptionVideoFrameAllocator, frame: Windows.Media.VideoFrame) -> Windows.Devices.Perception.Provider.PerceptionFrame: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
make_head(_module, 'IKnownPerceptionFrameKindStatics')
make_head(_module, 'IPerceptionControlGroup')
make_head(_module, 'IPerceptionControlGroupFactory')
make_head(_module, 'IPerceptionCorrelation')
make_head(_module, 'IPerceptionCorrelationFactory')
make_head(_module, 'IPerceptionCorrelationGroup')
make_head(_module, 'IPerceptionCorrelationGroupFactory')
make_head(_module, 'IPerceptionFaceAuthenticationGroup')
make_head(_module, 'IPerceptionFaceAuthenticationGroupFactory')
make_head(_module, 'IPerceptionFrame')
make_head(_module, 'IPerceptionFrameProvider')
make_head(_module, 'IPerceptionFrameProviderInfo')
make_head(_module, 'IPerceptionFrameProviderManager')
make_head(_module, 'IPerceptionFrameProviderManagerServiceStatics')
make_head(_module, 'IPerceptionPropertyChangeRequest')
make_head(_module, 'IPerceptionVideoFrameAllocator')
make_head(_module, 'IPerceptionVideoFrameAllocatorFactory')
make_head(_module, 'KnownPerceptionFrameKind')
make_head(_module, 'PerceptionControlGroup')
make_head(_module, 'PerceptionCorrelation')
make_head(_module, 'PerceptionCorrelationGroup')
make_head(_module, 'PerceptionFaceAuthenticationGroup')
make_head(_module, 'PerceptionFrame')
make_head(_module, 'PerceptionFrameProviderInfo')
make_head(_module, 'PerceptionFrameProviderManagerService')
make_head(_module, 'PerceptionPropertyChangeRequest')
make_head(_module, 'PerceptionStartFaceAuthenticationHandler')
make_head(_module, 'PerceptionStopFaceAuthenticationHandler')
make_head(_module, 'PerceptionVideoFrameAllocator')
