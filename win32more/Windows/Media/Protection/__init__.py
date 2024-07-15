from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Media.Playback
import win32more.Windows.Media.Protection
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class ComponentLoadFailedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.IComponentLoadFailedEventArgs
    _classid_ = 'Windows.Media.Protection.ComponentLoadFailedEventArgs'
    @winrt_mixinmethod
    def get_Information(self: win32more.Windows.Media.Protection.IComponentLoadFailedEventArgs) -> win32more.Windows.Media.Protection.RevocationAndRenewalInformation: ...
    @winrt_mixinmethod
    def get_Completion(self: win32more.Windows.Media.Protection.IComponentLoadFailedEventArgs) -> win32more.Windows.Media.Protection.MediaProtectionServiceCompletion: ...
    Completion = property(get_Completion, None)
    Information = property(get_Information, None)
class ComponentLoadFailedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{95da643c-6db9-424b-86ca-091af432081c}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Media.Protection.MediaProtectionManager, e: win32more.Windows.Media.Protection.ComponentLoadFailedEventArgs) -> Void: ...
class ComponentRenewal(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.ComponentRenewal'
    @winrt_classmethod
    def RenewSystemComponentsAsync(cls: win32more.Windows.Media.Protection.IComponentRenewalStatics, information: win32more.Windows.Media.Protection.RevocationAndRenewalInformation) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Protection.RenewalStatus, UInt32]: ...
class GraphicsTrustStatus(Enum, Int32):
    TrustNotRequired = 0
    TrustEstablished = 1
    EnvironmentNotSupported = 2
    DriverNotSupported = 3
    DriverSigningFailure = 4
    UnknownFailure = 5
class HdcpProtection(Enum, Int32):
    Off = 0
    On = 1
    OnWithTypeEnforcement = 2
class HdcpSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Media.Protection.IHdcpSession
    _classid_ = 'Windows.Media.Protection.HdcpSession'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Protection.HdcpSession.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Protection.HdcpSession: ...
    @winrt_mixinmethod
    def IsEffectiveProtectionAtLeast(self: win32more.Windows.Media.Protection.IHdcpSession, protection: win32more.Windows.Media.Protection.HdcpProtection) -> Boolean: ...
    @winrt_mixinmethod
    def GetEffectiveProtection(self: win32more.Windows.Media.Protection.IHdcpSession) -> win32more.Windows.Foundation.IReference[win32more.Windows.Media.Protection.HdcpProtection]: ...
    @winrt_mixinmethod
    def SetDesiredMinProtectionAsync(self: win32more.Windows.Media.Protection.IHdcpSession, protection: win32more.Windows.Media.Protection.HdcpProtection) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Protection.HdcpSetProtectionResult]: ...
    @winrt_mixinmethod
    def add_ProtectionChanged(self: win32more.Windows.Media.Protection.IHdcpSession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Protection.HdcpSession, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ProtectionChanged(self: win32more.Windows.Media.Protection.IHdcpSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    ProtectionChanged = event()
class HdcpSetProtectionResult(Enum, Int32):
    Success = 0
    TimedOut = 1
    NotSupported = 2
    UnknownFailure = 3
class IComponentLoadFailedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.IComponentLoadFailedEventArgs'
    _iid_ = Guid('{95972e93-7746-417e-8495-f031bbc5862c}')
    @winrt_commethod(6)
    def get_Information(self) -> win32more.Windows.Media.Protection.RevocationAndRenewalInformation: ...
    @winrt_commethod(7)
    def get_Completion(self) -> win32more.Windows.Media.Protection.MediaProtectionServiceCompletion: ...
    Completion = property(get_Completion, None)
    Information = property(get_Information, None)
class IComponentRenewalStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.IComponentRenewalStatics'
    _iid_ = Guid('{6ffbcd67-b795-48c5-8b7b-a7c4efe202e3}')
    @winrt_commethod(6)
    def RenewSystemComponentsAsync(self, information: win32more.Windows.Media.Protection.RevocationAndRenewalInformation) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Media.Protection.RenewalStatus, UInt32]: ...
class IHdcpSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Media.Protection.IHdcpSession'
    _iid_ = Guid('{718845e9-64d7-426d-809b-1be461941a2a}')
    @winrt_commethod(6)
    def IsEffectiveProtectionAtLeast(self, protection: win32more.Windows.Media.Protection.HdcpProtection) -> Boolean: ...
    @winrt_commethod(7)
    def GetEffectiveProtection(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Media.Protection.HdcpProtection]: ...
    @winrt_commethod(8)
    def SetDesiredMinProtectionAsync(self, protection: win32more.Windows.Media.Protection.HdcpProtection) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.Protection.HdcpSetProtectionResult]: ...
    @winrt_commethod(9)
    def add_ProtectionChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Protection.HdcpSession, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_ProtectionChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ProtectionChanged = event()
class IMediaProtectionManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.IMediaProtectionManager'
    _iid_ = Guid('{45694947-c741-434b-a79e-474c12d93d2f}')
    @winrt_commethod(6)
    def add_ServiceRequested(self, handler: win32more.Windows.Media.Protection.ServiceRequestedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ServiceRequested(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_RebootNeeded(self, handler: win32more.Windows.Media.Protection.RebootNeededEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_RebootNeeded(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_ComponentLoadFailed(self, handler: win32more.Windows.Media.Protection.ComponentLoadFailedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ComponentLoadFailed(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    Properties = property(get_Properties, None)
    ServiceRequested = event()
    RebootNeeded = event()
    ComponentLoadFailed = event()
class IMediaProtectionPMPServer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.IMediaProtectionPMPServer'
    _iid_ = Guid('{0c111226-7b26-4d31-95bb-9c1b08ef7fc0}')
    @winrt_commethod(6)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    Properties = property(get_Properties, None)
class IMediaProtectionPMPServerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.IMediaProtectionPMPServerFactory'
    _iid_ = Guid('{602c8e5e-f7d2-487e-af91-dbc4252b2182}')
    @winrt_commethod(6)
    def CreatePMPServer(self, pProperties: win32more.Windows.Foundation.Collections.IPropertySet) -> win32more.Windows.Media.Protection.MediaProtectionPMPServer: ...
class IMediaProtectionServiceCompletion(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.IMediaProtectionServiceCompletion'
    _iid_ = Guid('{8b5cca18-cfd5-44ee-a2ed-df76010c14b5}')
    @winrt_commethod(6)
    def Complete(self, success: Boolean) -> Void: ...
class IMediaProtectionServiceRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.IMediaProtectionServiceRequest'
    _iid_ = Guid('{b1de0ea6-2094-478d-87a4-8b95200f85c6}')
    @winrt_commethod(6)
    def get_ProtectionSystem(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Type(self) -> Guid: ...
    ProtectionSystem = property(get_ProtectionSystem, None)
    Type = property(get_Type, None)
class IProtectionCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.IProtectionCapabilities'
    _iid_ = Guid('{c7ac5d7e-7480-4d29-a464-7bcd913dd8e4}')
    @winrt_commethod(6)
    def IsTypeSupported(self, type: WinRT_String, keySystem: WinRT_String) -> win32more.Windows.Media.Protection.ProtectionCapabilityResult: ...
class IRevocationAndRenewalInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.IRevocationAndRenewalInformation'
    _iid_ = Guid('{f3a1937b-2501-439e-a6e7-6fc95e175fcf}')
    @winrt_commethod(6)
    def get_Items(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Protection.RevocationAndRenewalItem]: ...
    Items = property(get_Items, None)
class IRevocationAndRenewalItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.IRevocationAndRenewalItem'
    _iid_ = Guid('{3099c20c-3cf0-49ea-902d-caf32d2dde2c}')
    @winrt_commethod(6)
    def get_Reasons(self) -> win32more.Windows.Media.Protection.RevocationAndRenewalReasons: ...
    @winrt_commethod(7)
    def get_HeaderHash(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_PublicKeyHash(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_RenewalId(self) -> WinRT_String: ...
    HeaderHash = property(get_HeaderHash, None)
    Name = property(get_Name, None)
    PublicKeyHash = property(get_PublicKeyHash, None)
    Reasons = property(get_Reasons, None)
    RenewalId = property(get_RenewalId, None)
class IServiceRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.IServiceRequestedEventArgs'
    _iid_ = Guid('{34283baf-abb4-4fc1-bd89-93f106573a49}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.Media.Protection.IMediaProtectionServiceRequest: ...
    @winrt_commethod(7)
    def get_Completion(self) -> win32more.Windows.Media.Protection.MediaProtectionServiceCompletion: ...
    Completion = property(get_Completion, None)
    Request = property(get_Request, None)
class IServiceRequestedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Protection.IServiceRequestedEventArgs2'
    _iid_ = Guid('{553c69d6-fafe-4128-8dfa-130e398a13a7}')
    @winrt_commethod(6)
    def get_MediaPlaybackItem(self) -> win32more.Windows.Media.Playback.MediaPlaybackItem: ...
    MediaPlaybackItem = property(get_MediaPlaybackItem, None)
class MediaProtectionManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.IMediaProtectionManager
    _classid_ = 'Windows.Media.Protection.MediaProtectionManager'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Protection.MediaProtectionManager.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Protection.MediaProtectionManager: ...
    @winrt_mixinmethod
    def add_ServiceRequested(self: win32more.Windows.Media.Protection.IMediaProtectionManager, handler: win32more.Windows.Media.Protection.ServiceRequestedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ServiceRequested(self: win32more.Windows.Media.Protection.IMediaProtectionManager, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_RebootNeeded(self: win32more.Windows.Media.Protection.IMediaProtectionManager, handler: win32more.Windows.Media.Protection.RebootNeededEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RebootNeeded(self: win32more.Windows.Media.Protection.IMediaProtectionManager, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ComponentLoadFailed(self: win32more.Windows.Media.Protection.IMediaProtectionManager, handler: win32more.Windows.Media.Protection.ComponentLoadFailedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ComponentLoadFailed(self: win32more.Windows.Media.Protection.IMediaProtectionManager, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Media.Protection.IMediaProtectionManager) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    Properties = property(get_Properties, None)
    ServiceRequested = event()
    RebootNeeded = event()
    ComponentLoadFailed = event()
class MediaProtectionPMPServer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.IMediaProtectionPMPServer
    _classid_ = 'Windows.Media.Protection.MediaProtectionPMPServer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Media.Protection.MediaProtectionPMPServer.CreatePMPServer(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreatePMPServer(cls: win32more.Windows.Media.Protection.IMediaProtectionPMPServerFactory, pProperties: win32more.Windows.Foundation.Collections.IPropertySet) -> win32more.Windows.Media.Protection.MediaProtectionPMPServer: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Media.Protection.IMediaProtectionPMPServer) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    Properties = property(get_Properties, None)
class MediaProtectionServiceCompletion(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.IMediaProtectionServiceCompletion
    _classid_ = 'Windows.Media.Protection.MediaProtectionServiceCompletion'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.Media.Protection.IMediaProtectionServiceCompletion, success: Boolean) -> Void: ...
class ProtectionCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.IProtectionCapabilities
    _classid_ = 'Windows.Media.Protection.ProtectionCapabilities'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Protection.ProtectionCapabilities.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Protection.ProtectionCapabilities: ...
    @winrt_mixinmethod
    def IsTypeSupported(self: win32more.Windows.Media.Protection.IProtectionCapabilities, type: WinRT_String, keySystem: WinRT_String) -> win32more.Windows.Media.Protection.ProtectionCapabilityResult: ...
class ProtectionCapabilityResult(Enum, Int32):
    NotSupported = 0
    Maybe = 1
    Probably = 2
ProtectionRenewalContract: UInt32 = 65536
class RebootNeededEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{64e12a45-973b-4a3a-b260-91898a49a82c}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Media.Protection.MediaProtectionManager) -> Void: ...
class RenewalStatus(Enum, Int32):
    NotStarted = 0
    UpdatesInProgress = 1
    UserCancelled = 2
    AppComponentsMayNeedUpdating = 3
    NoComponentsFound = 4
class RevocationAndRenewalInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.IRevocationAndRenewalInformation
    _classid_ = 'Windows.Media.Protection.RevocationAndRenewalInformation'
    @winrt_mixinmethod
    def get_Items(self: win32more.Windows.Media.Protection.IRevocationAndRenewalInformation) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Media.Protection.RevocationAndRenewalItem]: ...
    Items = property(get_Items, None)
class RevocationAndRenewalItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.IRevocationAndRenewalItem
    _classid_ = 'Windows.Media.Protection.RevocationAndRenewalItem'
    @winrt_mixinmethod
    def get_Reasons(self: win32more.Windows.Media.Protection.IRevocationAndRenewalItem) -> win32more.Windows.Media.Protection.RevocationAndRenewalReasons: ...
    @winrt_mixinmethod
    def get_HeaderHash(self: win32more.Windows.Media.Protection.IRevocationAndRenewalItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PublicKeyHash(self: win32more.Windows.Media.Protection.IRevocationAndRenewalItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Media.Protection.IRevocationAndRenewalItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RenewalId(self: win32more.Windows.Media.Protection.IRevocationAndRenewalItem) -> WinRT_String: ...
    HeaderHash = property(get_HeaderHash, None)
    Name = property(get_Name, None)
    PublicKeyHash = property(get_PublicKeyHash, None)
    Reasons = property(get_Reasons, None)
    RenewalId = property(get_RenewalId, None)
class RevocationAndRenewalReasons(Enum, UInt32):
    UserModeComponentLoad = 1
    KernelModeComponentLoad = 2
    AppComponent = 4
    GlobalRevocationListLoadFailed = 16
    InvalidGlobalRevocationListSignature = 32
    GlobalRevocationListAbsent = 4096
    ComponentRevoked = 8192
    InvalidComponentCertificateExtendedKeyUse = 16384
    ComponentCertificateRevoked = 32768
    InvalidComponentCertificateRoot = 65536
    ComponentHighSecurityCertificateRevoked = 131072
    ComponentLowSecurityCertificateRevoked = 262144
    BootDriverVerificationFailed = 1048576
    ComponentSignedWithTestCertificate = 16777216
    EncryptionFailure = 268435456
class ServiceRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Protection.IServiceRequestedEventArgs
    _classid_ = 'Windows.Media.Protection.ServiceRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.Media.Protection.IServiceRequestedEventArgs) -> win32more.Windows.Media.Protection.IMediaProtectionServiceRequest: ...
    @winrt_mixinmethod
    def get_Completion(self: win32more.Windows.Media.Protection.IServiceRequestedEventArgs) -> win32more.Windows.Media.Protection.MediaProtectionServiceCompletion: ...
    @winrt_mixinmethod
    def get_MediaPlaybackItem(self: win32more.Windows.Media.Protection.IServiceRequestedEventArgs2) -> win32more.Windows.Media.Playback.MediaPlaybackItem: ...
    Completion = property(get_Completion, None)
    MediaPlaybackItem = property(get_MediaPlaybackItem, None)
    Request = property(get_Request, None)
class ServiceRequestedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d2d690ba-cac9-48e1-95c0-d38495a84055}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Media.Protection.MediaProtectionManager, e: win32more.Windows.Media.Protection.ServiceRequestedEventArgs) -> Void: ...


make_ready(__name__)
