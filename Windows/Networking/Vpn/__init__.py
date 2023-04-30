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
import Windows.ApplicationModel.Activation
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Networking
import Windows.Networking.Sockets
import Windows.Networking.Vpn
import Windows.Security.Credentials
import Windows.Security.Cryptography.Certificates
import Windows.Storage.Streams
import Windows.System
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IVpnAppId(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('7b06a635-5c58-41d9-94-a7-bf-bc-f1-d8-ca-54')
    @winrt_commethod(6)
    def get_Type(self) -> Windows.Networking.Vpn.VpnAppIdType: ...
    @winrt_commethod(7)
    def put_Type(self, value: Windows.Networking.Vpn.VpnAppIdType) -> Void: ...
    @winrt_commethod(8)
    def get_Value(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Value(self, value: WinRT_String) -> Void: ...
    Type = property(get_Type, put_Type)
    Value = property(get_Value, put_Value)
class IVpnAppIdFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('46adfd2a-0aab-4fdb-82-1d-d3-dd-c9-19-78-8b')
    @winrt_commethod(6)
    def Create(self, type: Windows.Networking.Vpn.VpnAppIdType, value: WinRT_String) -> Windows.Networking.Vpn.VpnAppId: ...
class IVpnChannel(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('4ac78d07-d1a8-4303-a0-91-c8-d2-e0-91-5b-c3')
    @winrt_commethod(6)
    def AssociateTransport(self, mainOuterTunnelTransport: Windows.Win32.System.WinRT.IInspectable_head, optionalOuterTunnelTransport: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(7)
    def Start(self, assignedClientIPv4list: Windows.Foundation.Collections.IVectorView[Windows.Networking.HostName], assignedClientIPv6list: Windows.Foundation.Collections.IVectorView[Windows.Networking.HostName], vpnInterfaceId: Windows.Networking.Vpn.VpnInterfaceId, routeScope: Windows.Networking.Vpn.VpnRouteAssignment, namespaceScope: Windows.Networking.Vpn.VpnNamespaceAssignment, mtuSize: UInt32, maxFrameSize: UInt32, optimizeForLowCostNetwork: Boolean, mainOuterTunnelTransport: Windows.Win32.System.WinRT.IInspectable_head, optionalOuterTunnelTransport: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(8)
    def Stop(self) -> Void: ...
    @winrt_commethod(9)
    def RequestCredentials(self, credType: Windows.Networking.Vpn.VpnCredentialType, isRetry: Boolean, isSingleSignOnCredential: Boolean, certificate: Windows.Security.Cryptography.Certificates.Certificate) -> Windows.Networking.Vpn.VpnPickedCredential: ...
    @winrt_commethod(10)
    def RequestVpnPacketBuffer(self, type: Windows.Networking.Vpn.VpnDataPathType, vpnPacketBuffer: POINTER(Windows.Networking.Vpn.VpnPacketBuffer)) -> Void: ...
    @winrt_commethod(11)
    def LogDiagnosticMessage(self, message: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(13)
    def get_Configuration(self) -> Windows.Networking.Vpn.VpnChannelConfiguration: ...
    @winrt_commethod(14)
    def add_ActivityChange(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.Vpn.VpnChannel, Windows.Networking.Vpn.VpnChannelActivityEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_ActivityChange(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def put_PlugInContext(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(17)
    def get_PlugInContext(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(18)
    def get_SystemHealth(self) -> Windows.Networking.Vpn.VpnSystemHealth: ...
    @winrt_commethod(19)
    def RequestCustomPrompt(self, customPrompt: Windows.Foundation.Collections.IVectorView[Windows.Networking.Vpn.IVpnCustomPrompt]) -> Void: ...
    @winrt_commethod(20)
    def SetErrorMessage(self, message: WinRT_String) -> Void: ...
    @winrt_commethod(21)
    def SetAllowedSslTlsVersions(self, tunnelTransport: Windows.Win32.System.WinRT.IInspectable_head, useTls12: Boolean) -> Void: ...
    Id = property(get_Id, None)
    Configuration = property(get_Configuration, None)
    PlugInContext = property(get_PlugInContext, put_PlugInContext)
    SystemHealth = property(get_SystemHealth, None)
class IVpnChannel2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2255d165-993b-4629-ad-60-f1-c3-f3-53-7f-50')
    @winrt_commethod(6)
    def StartWithMainTransport(self, assignedClientIPv4list: Windows.Foundation.Collections.IVectorView[Windows.Networking.HostName], assignedClientIPv6list: Windows.Foundation.Collections.IVectorView[Windows.Networking.HostName], vpnInterfaceId: Windows.Networking.Vpn.VpnInterfaceId, assignedRoutes: Windows.Networking.Vpn.VpnRouteAssignment, assignedDomainName: Windows.Networking.Vpn.VpnDomainNameAssignment, mtuSize: UInt32, maxFrameSize: UInt32, Reserved: Boolean, mainOuterTunnelTransport: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(7)
    def StartExistingTransports(self, assignedClientIPv4list: Windows.Foundation.Collections.IVectorView[Windows.Networking.HostName], assignedClientIPv6list: Windows.Foundation.Collections.IVectorView[Windows.Networking.HostName], vpnInterfaceId: Windows.Networking.Vpn.VpnInterfaceId, assignedRoutes: Windows.Networking.Vpn.VpnRouteAssignment, assignedDomainName: Windows.Networking.Vpn.VpnDomainNameAssignment, mtuSize: UInt32, maxFrameSize: UInt32, Reserved: Boolean) -> Void: ...
    @winrt_commethod(8)
    def add_ActivityStateChange(self, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.Vpn.VpnChannel, Windows.Networking.Vpn.VpnChannelActivityStateChangedArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ActivityStateChange(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def GetVpnSendPacketBuffer(self) -> Windows.Networking.Vpn.VpnPacketBuffer: ...
    @winrt_commethod(11)
    def GetVpnReceivePacketBuffer(self) -> Windows.Networking.Vpn.VpnPacketBuffer: ...
    @winrt_commethod(12)
    def RequestCustomPromptAsync(self, customPromptElement: Windows.Foundation.Collections.IVectorView[Windows.Networking.Vpn.IVpnCustomPromptElement]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def RequestCredentialsWithCertificateAsync(self, credType: Windows.Networking.Vpn.VpnCredentialType, credOptions: UInt32, certificate: Windows.Security.Cryptography.Certificates.Certificate) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Vpn.VpnCredential]: ...
    @winrt_commethod(14)
    def RequestCredentialsWithOptionsAsync(self, credType: Windows.Networking.Vpn.VpnCredentialType, credOptions: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Vpn.VpnCredential]: ...
    @winrt_commethod(15)
    def RequestCredentialsSimpleAsync(self, credType: Windows.Networking.Vpn.VpnCredentialType) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Vpn.VpnCredential]: ...
    @winrt_commethod(16)
    def TerminateConnection(self, message: WinRT_String) -> Void: ...
    @winrt_commethod(17)
    def StartWithTrafficFilter(self, assignedClientIpv4List: Windows.Foundation.Collections.IVectorView[Windows.Networking.HostName], assignedClientIpv6List: Windows.Foundation.Collections.IVectorView[Windows.Networking.HostName], vpnInterfaceId: Windows.Networking.Vpn.VpnInterfaceId, assignedRoutes: Windows.Networking.Vpn.VpnRouteAssignment, assignedNamespace: Windows.Networking.Vpn.VpnDomainNameAssignment, mtuSize: UInt32, maxFrameSize: UInt32, reserved: Boolean, mainOuterTunnelTransport: Windows.Win32.System.WinRT.IInspectable_head, optionalOuterTunnelTransport: Windows.Win32.System.WinRT.IInspectable_head, assignedTrafficFilters: Windows.Networking.Vpn.VpnTrafficFilterAssignment) -> Void: ...
class IVpnChannel4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d7266ede-2937-419d-95-70-48-6a-eb-b8-18-03')
    @winrt_commethod(6)
    def AddAndAssociateTransport(self, transport: Windows.Win32.System.WinRT.IInspectable_head, context: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(7)
    def StartWithMultipleTransports(self, assignedClientIpv4Addresses: Windows.Foundation.Collections.IIterable[Windows.Networking.HostName], assignedClientIpv6Addresses: Windows.Foundation.Collections.IIterable[Windows.Networking.HostName], vpninterfaceId: Windows.Networking.Vpn.VpnInterfaceId, assignedRoutes: Windows.Networking.Vpn.VpnRouteAssignment, assignedNamespace: Windows.Networking.Vpn.VpnDomainNameAssignment, mtuSize: UInt32, maxFrameSize: UInt32, reserved: Boolean, transports: Windows.Foundation.Collections.IIterable[Windows.Win32.System.WinRT.IInspectable_head], assignedTrafficFilters: Windows.Networking.Vpn.VpnTrafficFilterAssignment) -> Void: ...
    @winrt_commethod(8)
    def ReplaceAndAssociateTransport(self, transport: Windows.Win32.System.WinRT.IInspectable_head, context: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(9)
    def StartReconnectingTransport(self, transport: Windows.Win32.System.WinRT.IInspectable_head, context: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(10)
    def GetSlotTypeForTransportContext(self, context: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.Networking.Sockets.ControlChannelTriggerStatus: ...
    @winrt_commethod(11)
    def get_CurrentRequestTransportContext(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    CurrentRequestTransportContext = property(get_CurrentRequestTransportContext, None)
class IVpnChannel5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('de7a0992-8384-4fbc-88-2c-1f-d2-31-24-cd-3b')
    @winrt_commethod(6)
    def AppendVpnReceivePacketBuffer(self, decapsulatedPacketBuffer: Windows.Networking.Vpn.VpnPacketBuffer) -> Void: ...
    @winrt_commethod(7)
    def AppendVpnSendPacketBuffer(self, encapsulatedPacketBuffer: Windows.Networking.Vpn.VpnPacketBuffer) -> Void: ...
    @winrt_commethod(8)
    def FlushVpnReceivePacketBuffers(self) -> Void: ...
    @winrt_commethod(9)
    def FlushVpnSendPacketBuffers(self) -> Void: ...
class IVpnChannel6(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('55843696-bd63-49c5-ab-ca-5d-a7-78-85-55-1a')
    @winrt_commethod(6)
    def ActivateForeground(self, packageRelativeAppId: WinRT_String, sharedContext: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.Collections.ValueSet: ...
class IVpnChannelActivityEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a36c88f2-afdc-4775-85-5d-d4-ac-0a-35-fc-55')
    @winrt_commethod(6)
    def get_Type(self) -> Windows.Networking.Vpn.VpnChannelActivityEventType: ...
    Type = property(get_Type, None)
class IVpnChannelActivityStateChangedArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3d750565-fdc0-4bbe-a2-3b-45-ff-fc-6d-97-a1')
    @winrt_commethod(6)
    def get_ActivityState(self) -> Windows.Networking.Vpn.VpnChannelActivityEventType: ...
    ActivityState = property(get_ActivityState, None)
class IVpnChannelConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0e2ddca2-2012-4fe4-b1-79-8c-65-2c-6d-10-7e')
    @winrt_commethod(6)
    def get_ServerServiceName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ServerHostNameList(self) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.HostName]: ...
    @winrt_commethod(8)
    def get_CustomField(self) -> WinRT_String: ...
    ServerServiceName = property(get_ServerServiceName, None)
    ServerHostNameList = property(get_ServerHostNameList, None)
    CustomField = property(get_CustomField, None)
class IVpnChannelConfiguration2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('f30b574c-7824-471c-a1-18-63-db-c9-3a-e4-c7')
    @winrt_commethod(6)
    def get_ServerUris(self) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Uri]: ...
    ServerUris = property(get_ServerUris, None)
class IVpnChannelStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('88eb062d-e818-4ffd-98-a6-36-3e-37-36-c9-5d')
    @winrt_commethod(6)
    def ProcessEventAsync(self, thirdPartyPlugIn: Windows.Win32.System.WinRT.IInspectable_head, event: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
class IVpnCredential(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b7e78af3-a46d-404b-87-29-18-32-52-28-53-ac')
    @winrt_commethod(6)
    def get_PasskeyCredential(self) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(7)
    def get_CertificateCredential(self) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(8)
    def get_AdditionalPin(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_OldPasswordCredential(self) -> Windows.Security.Credentials.PasswordCredential: ...
    PasskeyCredential = property(get_PasskeyCredential, None)
    CertificateCredential = property(get_CertificateCredential, None)
    AdditionalPin = property(get_AdditionalPin, None)
    OldPasswordCredential = property(get_OldPasswordCredential, None)
class IVpnCustomCheckBox(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('43878753-03c5-4e61-93-d7-a9-57-71-4c-42-82')
    @winrt_commethod(6)
    def put_InitialCheckState(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_InitialCheckState(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_Checked(self) -> Boolean: ...
    InitialCheckState = property(get_InitialCheckState, put_InitialCheckState)
    Checked = property(get_Checked, None)
class IVpnCustomComboBox(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('9a24158e-dba1-4c6f-82-70-dc-f3-c9-76-1c-4c')
    @winrt_commethod(6)
    def put_OptionsText(self, value: Windows.Foundation.Collections.IVectorView[WinRT_String]) -> Void: ...
    @winrt_commethod(7)
    def get_OptionsText(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(8)
    def get_Selected(self) -> UInt32: ...
    OptionsText = property(get_OptionsText, put_OptionsText)
    Selected = property(get_Selected, None)
class IVpnCustomEditBox(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3002d9a0-cfbf-4c0b-8f-3c-66-f5-03-c2-0b-39')
    @winrt_commethod(6)
    def put_DefaultText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_DefaultText(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_NoEcho(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_NoEcho(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_Text(self) -> WinRT_String: ...
    DefaultText = property(get_DefaultText, put_DefaultText)
    NoEcho = property(get_NoEcho, put_NoEcho)
    Text = property(get_Text, None)
class IVpnCustomErrorBox(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('9ec4efb2-c942-42af-b2-23-58-8b-48-32-87-21')
class IVpnCustomPrompt(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('9b2ebe7b-87d5-433c-b4-f6-ee-e6-aa-68-a2-44')
    @winrt_commethod(6)
    def put_Label(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_Label(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Compulsory(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_Compulsory(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_Bordered(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_Bordered(self) -> Boolean: ...
    Label = property(get_Label, put_Label)
    Compulsory = property(get_Compulsory, put_Compulsory)
    Bordered = property(get_Bordered, put_Bordered)
class IVpnCustomPromptBooleanInput(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c4c9a69e-ff47-4527-9f-27-a4-92-92-01-99-79')
    @winrt_commethod(6)
    def put_InitialValue(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_InitialValue(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_Value(self) -> Boolean: ...
    InitialValue = property(get_InitialValue, put_InitialValue)
    Value = property(get_Value, None)
class IVpnCustomPromptElement(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('73bd5638-6f04-404d-93-dd-50-a4-49-24-a3-8b')
    @winrt_commethod(6)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Compulsory(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_Compulsory(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_Emphasized(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_Emphasized(self) -> Boolean: ...
    DisplayName = property(get_DisplayName, put_DisplayName)
    Compulsory = property(get_Compulsory, put_Compulsory)
    Emphasized = property(get_Emphasized, put_Emphasized)
class IVpnCustomPromptOptionSelector(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3b8f34d9-8ec1-4e95-9a-4e-7b-a6-4d-38-f3-30')
    @winrt_commethod(6)
    def get_Options(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(7)
    def get_SelectedIndex(self) -> UInt32: ...
    Options = property(get_Options, None)
    SelectedIndex = property(get_SelectedIndex, None)
class IVpnCustomPromptText(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3bc8bdee-3a42-49a3-ab-dd-07-b2-ed-ea-75-2d')
    @winrt_commethod(6)
    def put_Text(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_Text(self) -> WinRT_String: ...
    Text = property(get_Text, put_Text)
class IVpnCustomPromptTextInput(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c9da9c75-913c-47d5-88-ba-48-fc-48-93-02-35')
    @winrt_commethod(6)
    def put_PlaceholderText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_PlaceholderText(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_IsTextHidden(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_IsTextHidden(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_Text(self) -> WinRT_String: ...
    PlaceholderText = property(get_PlaceholderText, put_PlaceholderText)
    IsTextHidden = property(get_IsTextHidden, put_IsTextHidden)
    Text = property(get_Text, None)
class IVpnCustomTextBox(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('daa4c3ca-8f23-4d36-91-f1-76-d9-37-82-79-42')
    @winrt_commethod(6)
    def put_DisplayText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_DisplayText(self) -> WinRT_String: ...
    DisplayText = property(get_DisplayText, put_DisplayText)
class IVpnDomainNameAssignment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('4135b141-ccdb-49b5-94-01-03-9a-8a-e7-67-e9')
    @winrt_commethod(6)
    def get_DomainNameList(self) -> Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnDomainNameInfo]: ...
    @winrt_commethod(7)
    def put_ProxyAutoConfigurationUri(self, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def get_ProxyAutoConfigurationUri(self) -> Windows.Foundation.Uri: ...
    DomainNameList = property(get_DomainNameList, None)
    ProxyAutoConfigurationUri = property(get_ProxyAutoConfigurationUri, put_ProxyAutoConfigurationUri)
class IVpnDomainNameInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ad2eb82f-ea8e-4f7a-84-3e-1a-87-e3-2e-1b-9a')
    @winrt_commethod(6)
    def put_DomainName(self, value: Windows.Networking.HostName) -> Void: ...
    @winrt_commethod(7)
    def get_DomainName(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(8)
    def put_DomainNameType(self, value: Windows.Networking.Vpn.VpnDomainNameType) -> Void: ...
    @winrt_commethod(9)
    def get_DomainNameType(self) -> Windows.Networking.Vpn.VpnDomainNameType: ...
    @winrt_commethod(10)
    def get_DnsServers(self) -> Windows.Foundation.Collections.IVector[Windows.Networking.HostName]: ...
    @winrt_commethod(11)
    def get_WebProxyServers(self) -> Windows.Foundation.Collections.IVector[Windows.Networking.HostName]: ...
    DomainName = property(get_DomainName, put_DomainName)
    DomainNameType = property(get_DomainNameType, put_DomainNameType)
    DnsServers = property(get_DnsServers, None)
    WebProxyServers = property(get_WebProxyServers, None)
class IVpnDomainNameInfo2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ab871151-6c53-4828-98-83-d8-86-de-10-44-07')
    @winrt_commethod(6)
    def get_WebProxyUris(self) -> Windows.Foundation.Collections.IVector[Windows.Foundation.Uri]: ...
    WebProxyUris = property(get_WebProxyUris, None)
class IVpnDomainNameInfoFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2507bb75-028f-4688-8d-3a-c4-53-1d-f3-7d-a8')
    @winrt_commethod(6)
    def CreateVpnDomainNameInfo(self, name: WinRT_String, nameType: Windows.Networking.Vpn.VpnDomainNameType, dnsServerList: Windows.Foundation.Collections.IIterable[Windows.Networking.HostName], proxyServerList: Windows.Foundation.Collections.IIterable[Windows.Networking.HostName]) -> Windows.Networking.Vpn.VpnDomainNameInfo: ...
class IVpnForegroundActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('85b465b0-cadb-4d70-ac-92-54-3a-24-dc-9e-bc')
    @winrt_commethod(6)
    def get_ProfileName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SharedContext(self) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_commethod(8)
    def get_ActivationOperation(self) -> Windows.Networking.Vpn.VpnForegroundActivationOperation: ...
    ProfileName = property(get_ProfileName, None)
    SharedContext = property(get_SharedContext, None)
    ActivationOperation = property(get_ActivationOperation, None)
class IVpnForegroundActivationOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('9e010d57-f17a-4bd5-9b-6d-f9-84-f1-29-7d-3c')
    @winrt_commethod(6)
    def Complete(self, result: Windows.Foundation.Collections.ValueSet) -> Void: ...
class IVpnInterfaceId(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('9e2ddca2-1712-4ce4-b1-79-8c-65-2c-6d-10-11')
    @winrt_commethod(6)
    def GetAddressInfo(self, id: POINTER(c_char_p_no)) -> Void: ...
class IVpnInterfaceIdFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('9e2ddca2-1712-4ce4-b1-79-8c-65-2c-6d-10-00')
    @winrt_commethod(6)
    def CreateVpnInterfaceId(self, address: c_char_p_no) -> Windows.Networking.Vpn.VpnInterfaceId: ...
class IVpnManagementAgent(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('193696cd-a5c4-4abe-85-2b-78-5b-e4-cb-3e-34')
    @winrt_commethod(6)
    def AddProfileFromXmlAsync(self, xml: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_commethod(7)
    def AddProfileFromObjectAsync(self, profile: Windows.Networking.Vpn.IVpnProfile) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_commethod(8)
    def UpdateProfileFromXmlAsync(self, xml: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_commethod(9)
    def UpdateProfileFromObjectAsync(self, profile: Windows.Networking.Vpn.IVpnProfile) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_commethod(10)
    def GetProfilesAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.Vpn.IVpnProfile]]: ...
    @winrt_commethod(11)
    def DeleteProfileAsync(self, profile: Windows.Networking.Vpn.IVpnProfile) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_commethod(12)
    def ConnectProfileAsync(self, profile: Windows.Networking.Vpn.IVpnProfile) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_commethod(13)
    def ConnectProfileWithPasswordCredentialAsync(self, profile: Windows.Networking.Vpn.IVpnProfile, passwordCredential: Windows.Security.Credentials.PasswordCredential) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_commethod(14)
    def DisconnectProfileAsync(self, profile: Windows.Networking.Vpn.IVpnProfile) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
class IVpnNamespaceAssignment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d7f7db18-307d-4c0e-bd-62-8f-a2-70-bb-ad-d6')
    @winrt_commethod(6)
    def put_NamespaceList(self, value: Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnNamespaceInfo]) -> Void: ...
    @winrt_commethod(7)
    def get_NamespaceList(self) -> Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnNamespaceInfo]: ...
    @winrt_commethod(8)
    def put_ProxyAutoConfigUri(self, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(9)
    def get_ProxyAutoConfigUri(self) -> Windows.Foundation.Uri: ...
    NamespaceList = property(get_NamespaceList, put_NamespaceList)
    ProxyAutoConfigUri = property(get_ProxyAutoConfigUri, put_ProxyAutoConfigUri)
class IVpnNamespaceInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('30edfb43-444f-44c5-81-67-a3-5a-91-f1-af-94')
    @winrt_commethod(6)
    def put_Namespace(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_Namespace(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_DnsServers(self, value: Windows.Foundation.Collections.IVector[Windows.Networking.HostName]) -> Void: ...
    @winrt_commethod(9)
    def get_DnsServers(self) -> Windows.Foundation.Collections.IVector[Windows.Networking.HostName]: ...
    @winrt_commethod(10)
    def put_WebProxyServers(self, value: Windows.Foundation.Collections.IVector[Windows.Networking.HostName]) -> Void: ...
    @winrt_commethod(11)
    def get_WebProxyServers(self) -> Windows.Foundation.Collections.IVector[Windows.Networking.HostName]: ...
    Namespace = property(get_Namespace, put_Namespace)
    DnsServers = property(get_DnsServers, put_DnsServers)
    WebProxyServers = property(get_WebProxyServers, put_WebProxyServers)
class IVpnNamespaceInfoFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('cb3e951a-b0ce-442b-ac-bb-5f-99-b2-02-c3-1c')
    @winrt_commethod(6)
    def CreateVpnNamespaceInfo(self, name: WinRT_String, dnsServerList: Windows.Foundation.Collections.IVector[Windows.Networking.HostName], proxyServerList: Windows.Foundation.Collections.IVector[Windows.Networking.HostName]) -> Windows.Networking.Vpn.VpnNamespaceInfo: ...
class IVpnNativeProfile(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a4aee29e-6417-4333-98-42-f0-a6-6d-b6-98-02')
    @winrt_commethod(6)
    def get_Servers(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(7)
    def get_RoutingPolicyType(self) -> Windows.Networking.Vpn.VpnRoutingPolicyType: ...
    @winrt_commethod(8)
    def put_RoutingPolicyType(self, value: Windows.Networking.Vpn.VpnRoutingPolicyType) -> Void: ...
    @winrt_commethod(9)
    def get_NativeProtocolType(self) -> Windows.Networking.Vpn.VpnNativeProtocolType: ...
    @winrt_commethod(10)
    def put_NativeProtocolType(self, value: Windows.Networking.Vpn.VpnNativeProtocolType) -> Void: ...
    @winrt_commethod(11)
    def get_UserAuthenticationMethod(self) -> Windows.Networking.Vpn.VpnAuthenticationMethod: ...
    @winrt_commethod(12)
    def put_UserAuthenticationMethod(self, value: Windows.Networking.Vpn.VpnAuthenticationMethod) -> Void: ...
    @winrt_commethod(13)
    def get_TunnelAuthenticationMethod(self) -> Windows.Networking.Vpn.VpnAuthenticationMethod: ...
    @winrt_commethod(14)
    def put_TunnelAuthenticationMethod(self, value: Windows.Networking.Vpn.VpnAuthenticationMethod) -> Void: ...
    @winrt_commethod(15)
    def get_EapConfiguration(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def put_EapConfiguration(self, value: WinRT_String) -> Void: ...
    Servers = property(get_Servers, None)
    RoutingPolicyType = property(get_RoutingPolicyType, put_RoutingPolicyType)
    NativeProtocolType = property(get_NativeProtocolType, put_NativeProtocolType)
    UserAuthenticationMethod = property(get_UserAuthenticationMethod, put_UserAuthenticationMethod)
    TunnelAuthenticationMethod = property(get_TunnelAuthenticationMethod, put_TunnelAuthenticationMethod)
    EapConfiguration = property(get_EapConfiguration, put_EapConfiguration)
class IVpnNativeProfile2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0fec2467-cdb5-4ac7-b5-a3-0a-fb-5e-c4-76-82')
    @winrt_commethod(6)
    def get_RequireVpnClientAppUI(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_RequireVpnClientAppUI(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_ConnectionStatus(self) -> Windows.Networking.Vpn.VpnManagementConnectionStatus: ...
    RequireVpnClientAppUI = property(get_RequireVpnClientAppUI, put_RequireVpnClientAppUI)
    ConnectionStatus = property(get_ConnectionStatus, None)
class IVpnPacketBuffer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c2f891fc-4d5c-4a63-b7-0d-4e-30-7e-ac-ce-55')
    @winrt_commethod(6)
    def get_Buffer(self) -> Windows.Storage.Streams.Buffer: ...
    @winrt_commethod(7)
    def put_Status(self, value: Windows.Networking.Vpn.VpnPacketBufferStatus) -> Void: ...
    @winrt_commethod(8)
    def get_Status(self) -> Windows.Networking.Vpn.VpnPacketBufferStatus: ...
    @winrt_commethod(9)
    def put_TransportAffinity(self, value: UInt32) -> Void: ...
    @winrt_commethod(10)
    def get_TransportAffinity(self) -> UInt32: ...
    Buffer = property(get_Buffer, None)
    Status = property(get_Status, put_Status)
    TransportAffinity = property(get_TransportAffinity, put_TransportAffinity)
class IVpnPacketBuffer2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('665e91f0-8805-4bf5-a6-19-2e-84-88-2e-6b-4f')
    @winrt_commethod(6)
    def get_AppId(self) -> Windows.Networking.Vpn.VpnAppId: ...
    AppId = property(get_AppId, None)
class IVpnPacketBuffer3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e256072f-107b-4c40-b1-27-5b-c5-3e-0a-d9-60')
    @winrt_commethod(6)
    def put_TransportContext(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(7)
    def get_TransportContext(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    TransportContext = property(get_TransportContext, put_TransportContext)
class IVpnPacketBufferFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('9e2ddca2-1712-4ce4-b1-79-8c-65-2c-6d-99-99')
    @winrt_commethod(6)
    def CreateVpnPacketBuffer(self, parentBuffer: Windows.Networking.Vpn.VpnPacketBuffer, offset: UInt32, length: UInt32) -> Windows.Networking.Vpn.VpnPacketBuffer: ...
class IVpnPacketBufferList(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c2f891fc-4d5c-4a63-b7-0d-4e-30-7e-ac-ce-77')
    @winrt_commethod(6)
    def Append(self, nextVpnPacketBuffer: Windows.Networking.Vpn.VpnPacketBuffer) -> Void: ...
    @winrt_commethod(7)
    def AddAtBegin(self, nextVpnPacketBuffer: Windows.Networking.Vpn.VpnPacketBuffer) -> Void: ...
    @winrt_commethod(8)
    def RemoveAtEnd(self) -> Windows.Networking.Vpn.VpnPacketBuffer: ...
    @winrt_commethod(9)
    def RemoveAtBegin(self) -> Windows.Networking.Vpn.VpnPacketBuffer: ...
    @winrt_commethod(10)
    def Clear(self) -> Void: ...
    @winrt_commethod(11)
    def put_Status(self, value: Windows.Networking.Vpn.VpnPacketBufferStatus) -> Void: ...
    @winrt_commethod(12)
    def get_Status(self) -> Windows.Networking.Vpn.VpnPacketBufferStatus: ...
    @winrt_commethod(13)
    def get_Size(self) -> UInt32: ...
    Status = property(get_Status, put_Status)
    Size = property(get_Size, None)
class IVpnPacketBufferList2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3e7acfe5-ea1e-482a-8d-98-c0-65-f5-7d-89-ea')
    @winrt_commethod(6)
    def AddLeadingPacket(self, nextVpnPacketBuffer: Windows.Networking.Vpn.VpnPacketBuffer) -> Void: ...
    @winrt_commethod(7)
    def RemoveLeadingPacket(self) -> Windows.Networking.Vpn.VpnPacketBuffer: ...
    @winrt_commethod(8)
    def AddTrailingPacket(self, nextVpnPacketBuffer: Windows.Networking.Vpn.VpnPacketBuffer) -> Void: ...
    @winrt_commethod(9)
    def RemoveTrailingPacket(self) -> Windows.Networking.Vpn.VpnPacketBuffer: ...
class IVpnPickedCredential(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('9a793ac7-8854-4e52-ad-97-24-dd-9a-84-2b-ce')
    @winrt_commethod(6)
    def get_PasskeyCredential(self) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(7)
    def get_AdditionalPin(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_OldPasswordCredential(self) -> Windows.Security.Credentials.PasswordCredential: ...
    PasskeyCredential = property(get_PasskeyCredential, None)
    AdditionalPin = property(get_AdditionalPin, None)
    OldPasswordCredential = property(get_OldPasswordCredential, None)
class IVpnPlugIn(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ceb78d07-d0a8-4703-a0-91-c8-c2-c0-91-5b-c4')
    @winrt_commethod(6)
    def Connect(self, channel: Windows.Networking.Vpn.VpnChannel) -> Void: ...
    @winrt_commethod(7)
    def Disconnect(self, channel: Windows.Networking.Vpn.VpnChannel) -> Void: ...
    @winrt_commethod(8)
    def GetKeepAlivePayload(self, channel: Windows.Networking.Vpn.VpnChannel, keepAlivePacket: POINTER(Windows.Networking.Vpn.VpnPacketBuffer)) -> Void: ...
    @winrt_commethod(9)
    def Encapsulate(self, channel: Windows.Networking.Vpn.VpnChannel, packets: Windows.Networking.Vpn.VpnPacketBufferList, encapulatedPackets: Windows.Networking.Vpn.VpnPacketBufferList) -> Void: ...
    @winrt_commethod(10)
    def Decapsulate(self, channel: Windows.Networking.Vpn.VpnChannel, encapBuffer: Windows.Networking.Vpn.VpnPacketBuffer, decapsulatedPackets: Windows.Networking.Vpn.VpnPacketBufferList, controlPacketsToSend: Windows.Networking.Vpn.VpnPacketBufferList) -> Void: ...
class IVpnPlugInProfile(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0edf0da4-4f00-4589-8d-7b-4b-f9-88-f6-54-2c')
    @winrt_commethod(6)
    def get_ServerUris(self) -> Windows.Foundation.Collections.IVector[Windows.Foundation.Uri]: ...
    @winrt_commethod(7)
    def get_CustomConfiguration(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_CustomConfiguration(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_VpnPluginPackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def put_VpnPluginPackageFamilyName(self, value: WinRT_String) -> Void: ...
    ServerUris = property(get_ServerUris, None)
    CustomConfiguration = property(get_CustomConfiguration, put_CustomConfiguration)
    VpnPluginPackageFamilyName = property(get_VpnPluginPackageFamilyName, put_VpnPluginPackageFamilyName)
class IVpnPlugInProfile2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('611c4892-cf94-4ad6-ba-99-00-f4-ff-34-56-5e')
    @winrt_commethod(6)
    def get_RequireVpnClientAppUI(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_RequireVpnClientAppUI(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_ConnectionStatus(self) -> Windows.Networking.Vpn.VpnManagementConnectionStatus: ...
    RequireVpnClientAppUI = property(get_RequireVpnClientAppUI, put_RequireVpnClientAppUI)
    ConnectionStatus = property(get_ConnectionStatus, None)
class IVpnProfile(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('7875b751-b0d7-43db-8a-93-d3-fe-24-79-e5-6a')
    @winrt_commethod(6)
    def get_ProfileName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_ProfileName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_AppTriggers(self) -> Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnAppId]: ...
    @winrt_commethod(9)
    def get_Routes(self) -> Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnRoute]: ...
    @winrt_commethod(10)
    def get_DomainNameInfoList(self) -> Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnDomainNameInfo]: ...
    @winrt_commethod(11)
    def get_TrafficFilters(self) -> Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnTrafficFilter]: ...
    @winrt_commethod(12)
    def get_RememberCredentials(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_RememberCredentials(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_AlwaysOn(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_AlwaysOn(self, value: Boolean) -> Void: ...
    ProfileName = property(get_ProfileName, put_ProfileName)
    AppTriggers = property(get_AppTriggers, None)
    Routes = property(get_Routes, None)
    DomainNameInfoList = property(get_DomainNameInfoList, None)
    TrafficFilters = property(get_TrafficFilters, None)
    RememberCredentials = property(get_RememberCredentials, put_RememberCredentials)
    AlwaysOn = property(get_AlwaysOn, put_AlwaysOn)
class IVpnRoute(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b5731b83-0969-4699-93-8e-77-76-db-29-cf-b3')
    @winrt_commethod(6)
    def put_Address(self, value: Windows.Networking.HostName) -> Void: ...
    @winrt_commethod(7)
    def get_Address(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(8)
    def put_PrefixSize(self, value: Byte) -> Void: ...
    @winrt_commethod(9)
    def get_PrefixSize(self) -> Byte: ...
    Address = property(get_Address, put_Address)
    PrefixSize = property(get_PrefixSize, put_PrefixSize)
class IVpnRouteAssignment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('db64de22-ce39-4a76-95-50-f6-10-39-f8-0e-48')
    @winrt_commethod(6)
    def put_Ipv4InclusionRoutes(self, value: Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnRoute]) -> Void: ...
    @winrt_commethod(7)
    def put_Ipv6InclusionRoutes(self, value: Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnRoute]) -> Void: ...
    @winrt_commethod(8)
    def get_Ipv4InclusionRoutes(self) -> Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnRoute]: ...
    @winrt_commethod(9)
    def get_Ipv6InclusionRoutes(self) -> Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnRoute]: ...
    @winrt_commethod(10)
    def put_Ipv4ExclusionRoutes(self, value: Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnRoute]) -> Void: ...
    @winrt_commethod(11)
    def put_Ipv6ExclusionRoutes(self, value: Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnRoute]) -> Void: ...
    @winrt_commethod(12)
    def get_Ipv4ExclusionRoutes(self) -> Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnRoute]: ...
    @winrt_commethod(13)
    def get_Ipv6ExclusionRoutes(self) -> Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnRoute]: ...
    @winrt_commethod(14)
    def put_ExcludeLocalSubnets(self, value: Boolean) -> Void: ...
    @winrt_commethod(15)
    def get_ExcludeLocalSubnets(self) -> Boolean: ...
    Ipv4InclusionRoutes = property(get_Ipv4InclusionRoutes, put_Ipv4InclusionRoutes)
    Ipv6InclusionRoutes = property(get_Ipv6InclusionRoutes, put_Ipv6InclusionRoutes)
    Ipv4ExclusionRoutes = property(get_Ipv4ExclusionRoutes, put_Ipv4ExclusionRoutes)
    Ipv6ExclusionRoutes = property(get_Ipv6ExclusionRoutes, put_Ipv6ExclusionRoutes)
    ExcludeLocalSubnets = property(get_ExcludeLocalSubnets, put_ExcludeLocalSubnets)
class IVpnRouteFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('bdeab5ff-45cf-4b99-83-fb-db-3b-c2-67-2b-02')
    @winrt_commethod(6)
    def CreateVpnRoute(self, address: Windows.Networking.HostName, prefixSize: Byte) -> Windows.Networking.Vpn.VpnRoute: ...
class IVpnSystemHealth(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('99a8f8af-c0ee-4e75-81-7a-f2-31-ae-e5-12-3d')
    @winrt_commethod(6)
    def get_StatementOfHealth(self) -> Windows.Storage.Streams.Buffer: ...
    StatementOfHealth = property(get_StatementOfHealth, None)
class IVpnTrafficFilter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2f691b60-6c9f-47f5-ac-36-bb-1b-04-2e-2c-50')
    @winrt_commethod(6)
    def get_AppId(self) -> Windows.Networking.Vpn.VpnAppId: ...
    @winrt_commethod(7)
    def put_AppId(self, value: Windows.Networking.Vpn.VpnAppId) -> Void: ...
    @winrt_commethod(8)
    def get_AppClaims(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(9)
    def get_Protocol(self) -> Windows.Networking.Vpn.VpnIPProtocol: ...
    @winrt_commethod(10)
    def put_Protocol(self, value: Windows.Networking.Vpn.VpnIPProtocol) -> Void: ...
    @winrt_commethod(11)
    def get_LocalPortRanges(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(12)
    def get_RemotePortRanges(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(13)
    def get_LocalAddressRanges(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(14)
    def get_RemoteAddressRanges(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(15)
    def get_RoutingPolicyType(self) -> Windows.Networking.Vpn.VpnRoutingPolicyType: ...
    @winrt_commethod(16)
    def put_RoutingPolicyType(self, value: Windows.Networking.Vpn.VpnRoutingPolicyType) -> Void: ...
    AppId = property(get_AppId, put_AppId)
    AppClaims = property(get_AppClaims, None)
    Protocol = property(get_Protocol, put_Protocol)
    LocalPortRanges = property(get_LocalPortRanges, None)
    RemotePortRanges = property(get_RemotePortRanges, None)
    LocalAddressRanges = property(get_LocalAddressRanges, None)
    RemoteAddressRanges = property(get_RemoteAddressRanges, None)
    RoutingPolicyType = property(get_RoutingPolicyType, put_RoutingPolicyType)
class IVpnTrafficFilterAssignment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('56ccd45c-e664-471e-89-cd-60-16-03-b9-e0-f3')
    @winrt_commethod(6)
    def get_TrafficFilterList(self) -> Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnTrafficFilter]: ...
    @winrt_commethod(7)
    def get_AllowOutbound(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_AllowOutbound(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_AllowInbound(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_AllowInbound(self, value: Boolean) -> Void: ...
    TrafficFilterList = property(get_TrafficFilterList, None)
    AllowOutbound = property(get_AllowOutbound, put_AllowOutbound)
    AllowInbound = property(get_AllowInbound, put_AllowInbound)
class IVpnTrafficFilterFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('480d41d5-7f99-474c-86-ee-96-df-16-83-18-f1')
    @winrt_commethod(6)
    def Create(self, appId: Windows.Networking.Vpn.VpnAppId) -> Windows.Networking.Vpn.VpnTrafficFilter: ...
class VpnAppId(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnAppId'
    @winrt_factorymethod
    def Create(cls: Windows.Networking.Vpn.IVpnAppIdFactory, type: Windows.Networking.Vpn.VpnAppIdType, value: WinRT_String) -> Windows.Networking.Vpn.VpnAppId: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Networking.Vpn.IVpnAppId) -> Windows.Networking.Vpn.VpnAppIdType: ...
    @winrt_mixinmethod
    def put_Type(self: Windows.Networking.Vpn.IVpnAppId, value: Windows.Networking.Vpn.VpnAppIdType) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Networking.Vpn.IVpnAppId) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Value(self: Windows.Networking.Vpn.IVpnAppId, value: WinRT_String) -> Void: ...
    Type = property(get_Type, put_Type)
    Value = property(get_Value, put_Value)
VpnAppIdType = Int32
VpnAppIdType_PackageFamilyName: VpnAppIdType = 0
VpnAppIdType_FullyQualifiedBinaryName: VpnAppIdType = 1
VpnAppIdType_FilePath: VpnAppIdType = 2
VpnAuthenticationMethod = Int32
VpnAuthenticationMethod_Mschapv2: VpnAuthenticationMethod = 0
VpnAuthenticationMethod_Eap: VpnAuthenticationMethod = 1
VpnAuthenticationMethod_Certificate: VpnAuthenticationMethod = 2
VpnAuthenticationMethod_PresharedKey: VpnAuthenticationMethod = 3
class VpnChannel(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnChannel'
    @winrt_mixinmethod
    def AssociateTransport(self: Windows.Networking.Vpn.IVpnChannel, mainOuterTunnelTransport: Windows.Win32.System.WinRT.IInspectable_head, optionalOuterTunnelTransport: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def Start(self: Windows.Networking.Vpn.IVpnChannel, assignedClientIPv4list: Windows.Foundation.Collections.IVectorView[Windows.Networking.HostName], assignedClientIPv6list: Windows.Foundation.Collections.IVectorView[Windows.Networking.HostName], vpnInterfaceId: Windows.Networking.Vpn.VpnInterfaceId, routeScope: Windows.Networking.Vpn.VpnRouteAssignment, namespaceScope: Windows.Networking.Vpn.VpnNamespaceAssignment, mtuSize: UInt32, maxFrameSize: UInt32, optimizeForLowCostNetwork: Boolean, mainOuterTunnelTransport: Windows.Win32.System.WinRT.IInspectable_head, optionalOuterTunnelTransport: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Networking.Vpn.IVpnChannel) -> Void: ...
    @winrt_mixinmethod
    def RequestCredentials(self: Windows.Networking.Vpn.IVpnChannel, credType: Windows.Networking.Vpn.VpnCredentialType, isRetry: Boolean, isSingleSignOnCredential: Boolean, certificate: Windows.Security.Cryptography.Certificates.Certificate) -> Windows.Networking.Vpn.VpnPickedCredential: ...
    @winrt_mixinmethod
    def RequestVpnPacketBuffer(self: Windows.Networking.Vpn.IVpnChannel, type: Windows.Networking.Vpn.VpnDataPathType, vpnPacketBuffer: POINTER(Windows.Networking.Vpn.VpnPacketBuffer)) -> Void: ...
    @winrt_mixinmethod
    def LogDiagnosticMessage(self: Windows.Networking.Vpn.IVpnChannel, message: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Networking.Vpn.IVpnChannel) -> UInt32: ...
    @winrt_mixinmethod
    def get_Configuration(self: Windows.Networking.Vpn.IVpnChannel) -> Windows.Networking.Vpn.VpnChannelConfiguration: ...
    @winrt_mixinmethod
    def add_ActivityChange(self: Windows.Networking.Vpn.IVpnChannel, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.Vpn.VpnChannel, Windows.Networking.Vpn.VpnChannelActivityEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ActivityChange(self: Windows.Networking.Vpn.IVpnChannel, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def put_PlugInContext(self: Windows.Networking.Vpn.IVpnChannel, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def get_PlugInContext(self: Windows.Networking.Vpn.IVpnChannel) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_SystemHealth(self: Windows.Networking.Vpn.IVpnChannel) -> Windows.Networking.Vpn.VpnSystemHealth: ...
    @winrt_mixinmethod
    def RequestCustomPrompt(self: Windows.Networking.Vpn.IVpnChannel, customPrompt: Windows.Foundation.Collections.IVectorView[Windows.Networking.Vpn.IVpnCustomPrompt]) -> Void: ...
    @winrt_mixinmethod
    def SetErrorMessage(self: Windows.Networking.Vpn.IVpnChannel, message: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def SetAllowedSslTlsVersions(self: Windows.Networking.Vpn.IVpnChannel, tunnelTransport: Windows.Win32.System.WinRT.IInspectable_head, useTls12: Boolean) -> Void: ...
    @winrt_mixinmethod
    def StartWithMainTransport(self: Windows.Networking.Vpn.IVpnChannel2, assignedClientIPv4list: Windows.Foundation.Collections.IVectorView[Windows.Networking.HostName], assignedClientIPv6list: Windows.Foundation.Collections.IVectorView[Windows.Networking.HostName], vpnInterfaceId: Windows.Networking.Vpn.VpnInterfaceId, assignedRoutes: Windows.Networking.Vpn.VpnRouteAssignment, assignedDomainName: Windows.Networking.Vpn.VpnDomainNameAssignment, mtuSize: UInt32, maxFrameSize: UInt32, Reserved: Boolean, mainOuterTunnelTransport: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def StartExistingTransports(self: Windows.Networking.Vpn.IVpnChannel2, assignedClientIPv4list: Windows.Foundation.Collections.IVectorView[Windows.Networking.HostName], assignedClientIPv6list: Windows.Foundation.Collections.IVectorView[Windows.Networking.HostName], vpnInterfaceId: Windows.Networking.Vpn.VpnInterfaceId, assignedRoutes: Windows.Networking.Vpn.VpnRouteAssignment, assignedDomainName: Windows.Networking.Vpn.VpnDomainNameAssignment, mtuSize: UInt32, maxFrameSize: UInt32, Reserved: Boolean) -> Void: ...
    @winrt_mixinmethod
    def add_ActivityStateChange(self: Windows.Networking.Vpn.IVpnChannel2, handler: Windows.Foundation.TypedEventHandler[Windows.Networking.Vpn.VpnChannel, Windows.Networking.Vpn.VpnChannelActivityStateChangedArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ActivityStateChange(self: Windows.Networking.Vpn.IVpnChannel2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetVpnSendPacketBuffer(self: Windows.Networking.Vpn.IVpnChannel2) -> Windows.Networking.Vpn.VpnPacketBuffer: ...
    @winrt_mixinmethod
    def GetVpnReceivePacketBuffer(self: Windows.Networking.Vpn.IVpnChannel2) -> Windows.Networking.Vpn.VpnPacketBuffer: ...
    @winrt_mixinmethod
    def RequestCustomPromptAsync(self: Windows.Networking.Vpn.IVpnChannel2, customPromptElement: Windows.Foundation.Collections.IVectorView[Windows.Networking.Vpn.IVpnCustomPromptElement]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RequestCredentialsWithCertificateAsync(self: Windows.Networking.Vpn.IVpnChannel2, credType: Windows.Networking.Vpn.VpnCredentialType, credOptions: UInt32, certificate: Windows.Security.Cryptography.Certificates.Certificate) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Vpn.VpnCredential]: ...
    @winrt_mixinmethod
    def RequestCredentialsWithOptionsAsync(self: Windows.Networking.Vpn.IVpnChannel2, credType: Windows.Networking.Vpn.VpnCredentialType, credOptions: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Vpn.VpnCredential]: ...
    @winrt_mixinmethod
    def RequestCredentialsSimpleAsync(self: Windows.Networking.Vpn.IVpnChannel2, credType: Windows.Networking.Vpn.VpnCredentialType) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Vpn.VpnCredential]: ...
    @winrt_mixinmethod
    def TerminateConnection(self: Windows.Networking.Vpn.IVpnChannel2, message: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def StartWithTrafficFilter(self: Windows.Networking.Vpn.IVpnChannel2, assignedClientIpv4List: Windows.Foundation.Collections.IVectorView[Windows.Networking.HostName], assignedClientIpv6List: Windows.Foundation.Collections.IVectorView[Windows.Networking.HostName], vpnInterfaceId: Windows.Networking.Vpn.VpnInterfaceId, assignedRoutes: Windows.Networking.Vpn.VpnRouteAssignment, assignedNamespace: Windows.Networking.Vpn.VpnDomainNameAssignment, mtuSize: UInt32, maxFrameSize: UInt32, reserved: Boolean, mainOuterTunnelTransport: Windows.Win32.System.WinRT.IInspectable_head, optionalOuterTunnelTransport: Windows.Win32.System.WinRT.IInspectable_head, assignedTrafficFilters: Windows.Networking.Vpn.VpnTrafficFilterAssignment) -> Void: ...
    @winrt_mixinmethod
    def AddAndAssociateTransport(self: Windows.Networking.Vpn.IVpnChannel4, transport: Windows.Win32.System.WinRT.IInspectable_head, context: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def StartWithMultipleTransports(self: Windows.Networking.Vpn.IVpnChannel4, assignedClientIpv4Addresses: Windows.Foundation.Collections.IIterable[Windows.Networking.HostName], assignedClientIpv6Addresses: Windows.Foundation.Collections.IIterable[Windows.Networking.HostName], vpninterfaceId: Windows.Networking.Vpn.VpnInterfaceId, assignedRoutes: Windows.Networking.Vpn.VpnRouteAssignment, assignedNamespace: Windows.Networking.Vpn.VpnDomainNameAssignment, mtuSize: UInt32, maxFrameSize: UInt32, reserved: Boolean, transports: Windows.Foundation.Collections.IIterable[Windows.Win32.System.WinRT.IInspectable_head], assignedTrafficFilters: Windows.Networking.Vpn.VpnTrafficFilterAssignment) -> Void: ...
    @winrt_mixinmethod
    def ReplaceAndAssociateTransport(self: Windows.Networking.Vpn.IVpnChannel4, transport: Windows.Win32.System.WinRT.IInspectable_head, context: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def StartReconnectingTransport(self: Windows.Networking.Vpn.IVpnChannel4, transport: Windows.Win32.System.WinRT.IInspectable_head, context: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def GetSlotTypeForTransportContext(self: Windows.Networking.Vpn.IVpnChannel4, context: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.Networking.Sockets.ControlChannelTriggerStatus: ...
    @winrt_mixinmethod
    def get_CurrentRequestTransportContext(self: Windows.Networking.Vpn.IVpnChannel4) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def AppendVpnReceivePacketBuffer(self: Windows.Networking.Vpn.IVpnChannel5, decapsulatedPacketBuffer: Windows.Networking.Vpn.VpnPacketBuffer) -> Void: ...
    @winrt_mixinmethod
    def AppendVpnSendPacketBuffer(self: Windows.Networking.Vpn.IVpnChannel5, encapsulatedPacketBuffer: Windows.Networking.Vpn.VpnPacketBuffer) -> Void: ...
    @winrt_mixinmethod
    def FlushVpnReceivePacketBuffers(self: Windows.Networking.Vpn.IVpnChannel5) -> Void: ...
    @winrt_mixinmethod
    def FlushVpnSendPacketBuffers(self: Windows.Networking.Vpn.IVpnChannel5) -> Void: ...
    @winrt_mixinmethod
    def ActivateForeground(self: Windows.Networking.Vpn.IVpnChannel6, packageRelativeAppId: WinRT_String, sharedContext: Windows.Foundation.Collections.ValueSet) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_classmethod
    def ProcessEventAsync(cls: Windows.Networking.Vpn.IVpnChannelStatics, thirdPartyPlugIn: Windows.Win32.System.WinRT.IInspectable_head, event: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    Id = property(get_Id, None)
    Configuration = property(get_Configuration, None)
    PlugInContext = property(get_PlugInContext, put_PlugInContext)
    SystemHealth = property(get_SystemHealth, None)
    CurrentRequestTransportContext = property(get_CurrentRequestTransportContext, None)
class VpnChannelActivityEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnChannelActivityEventArgs'
    @winrt_mixinmethod
    def get_Type(self: Windows.Networking.Vpn.IVpnChannelActivityEventArgs) -> Windows.Networking.Vpn.VpnChannelActivityEventType: ...
    Type = property(get_Type, None)
VpnChannelActivityEventType = Int32
VpnChannelActivityEventType_Idle: VpnChannelActivityEventType = 0
VpnChannelActivityEventType_Active: VpnChannelActivityEventType = 1
class VpnChannelActivityStateChangedArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnChannelActivityStateChangedArgs'
    @winrt_mixinmethod
    def get_ActivityState(self: Windows.Networking.Vpn.IVpnChannelActivityStateChangedArgs) -> Windows.Networking.Vpn.VpnChannelActivityEventType: ...
    ActivityState = property(get_ActivityState, None)
class VpnChannelConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnChannelConfiguration'
    @winrt_mixinmethod
    def get_ServerServiceName(self: Windows.Networking.Vpn.IVpnChannelConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServerHostNameList(self: Windows.Networking.Vpn.IVpnChannelConfiguration) -> Windows.Foundation.Collections.IVectorView[Windows.Networking.HostName]: ...
    @winrt_mixinmethod
    def get_CustomField(self: Windows.Networking.Vpn.IVpnChannelConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServerUris(self: Windows.Networking.Vpn.IVpnChannelConfiguration2) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Uri]: ...
    ServerServiceName = property(get_ServerServiceName, None)
    ServerHostNameList = property(get_ServerHostNameList, None)
    CustomField = property(get_CustomField, None)
    ServerUris = property(get_ServerUris, None)
VpnChannelRequestCredentialsOptions = UInt32
VpnChannelRequestCredentialsOptions_None: VpnChannelRequestCredentialsOptions = 0
VpnChannelRequestCredentialsOptions_Retrying: VpnChannelRequestCredentialsOptions = 1
VpnChannelRequestCredentialsOptions_UseForSingleSignIn: VpnChannelRequestCredentialsOptions = 2
class VpnCredential(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnCredential'
    @winrt_mixinmethod
    def get_PasskeyCredential(self: Windows.Networking.Vpn.IVpnCredential) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def get_CertificateCredential(self: Windows.Networking.Vpn.IVpnCredential) -> Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def get_AdditionalPin(self: Windows.Networking.Vpn.IVpnCredential) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OldPasswordCredential(self: Windows.Networking.Vpn.IVpnCredential) -> Windows.Security.Credentials.PasswordCredential: ...
    PasskeyCredential = property(get_PasskeyCredential, None)
    CertificateCredential = property(get_CertificateCredential, None)
    AdditionalPin = property(get_AdditionalPin, None)
    OldPasswordCredential = property(get_OldPasswordCredential, None)
VpnCredentialType = Int32
VpnCredentialType_UsernamePassword: VpnCredentialType = 0
VpnCredentialType_UsernameOtpPin: VpnCredentialType = 1
VpnCredentialType_UsernamePasswordAndPin: VpnCredentialType = 2
VpnCredentialType_UsernamePasswordChange: VpnCredentialType = 3
VpnCredentialType_SmartCard: VpnCredentialType = 4
VpnCredentialType_ProtectedCertificate: VpnCredentialType = 5
VpnCredentialType_UnProtectedCertificate: VpnCredentialType = 6
class VpnCustomCheckBox(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnCustomCheckBox'
    @winrt_activatemethod
    def New(cls) -> Windows.Networking.Vpn.VpnCustomCheckBox: ...
    @winrt_mixinmethod
    def put_InitialCheckState(self: Windows.Networking.Vpn.IVpnCustomCheckBox, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_InitialCheckState(self: Windows.Networking.Vpn.IVpnCustomCheckBox) -> Boolean: ...
    @winrt_mixinmethod
    def get_Checked(self: Windows.Networking.Vpn.IVpnCustomCheckBox) -> Boolean: ...
    @winrt_mixinmethod
    def put_Label(self: Windows.Networking.Vpn.IVpnCustomPrompt, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Label(self: Windows.Networking.Vpn.IVpnCustomPrompt) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Compulsory(self: Windows.Networking.Vpn.IVpnCustomPrompt, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Compulsory(self: Windows.Networking.Vpn.IVpnCustomPrompt) -> Boolean: ...
    @winrt_mixinmethod
    def put_Bordered(self: Windows.Networking.Vpn.IVpnCustomPrompt, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Bordered(self: Windows.Networking.Vpn.IVpnCustomPrompt) -> Boolean: ...
    InitialCheckState = property(get_InitialCheckState, put_InitialCheckState)
    Checked = property(get_Checked, None)
    Label = property(get_Label, put_Label)
    Compulsory = property(get_Compulsory, put_Compulsory)
    Bordered = property(get_Bordered, put_Bordered)
class VpnCustomComboBox(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnCustomComboBox'
    @winrt_activatemethod
    def New(cls) -> Windows.Networking.Vpn.VpnCustomComboBox: ...
    @winrt_mixinmethod
    def put_OptionsText(self: Windows.Networking.Vpn.IVpnCustomComboBox, value: Windows.Foundation.Collections.IVectorView[WinRT_String]) -> Void: ...
    @winrt_mixinmethod
    def get_OptionsText(self: Windows.Networking.Vpn.IVpnCustomComboBox) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Selected(self: Windows.Networking.Vpn.IVpnCustomComboBox) -> UInt32: ...
    @winrt_mixinmethod
    def put_Label(self: Windows.Networking.Vpn.IVpnCustomPrompt, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Label(self: Windows.Networking.Vpn.IVpnCustomPrompt) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Compulsory(self: Windows.Networking.Vpn.IVpnCustomPrompt, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Compulsory(self: Windows.Networking.Vpn.IVpnCustomPrompt) -> Boolean: ...
    @winrt_mixinmethod
    def put_Bordered(self: Windows.Networking.Vpn.IVpnCustomPrompt, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Bordered(self: Windows.Networking.Vpn.IVpnCustomPrompt) -> Boolean: ...
    OptionsText = property(get_OptionsText, put_OptionsText)
    Selected = property(get_Selected, None)
    Label = property(get_Label, put_Label)
    Compulsory = property(get_Compulsory, put_Compulsory)
    Bordered = property(get_Bordered, put_Bordered)
class VpnCustomEditBox(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnCustomEditBox'
    @winrt_activatemethod
    def New(cls) -> Windows.Networking.Vpn.VpnCustomEditBox: ...
    @winrt_mixinmethod
    def put_DefaultText(self: Windows.Networking.Vpn.IVpnCustomEditBox, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DefaultText(self: Windows.Networking.Vpn.IVpnCustomEditBox) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NoEcho(self: Windows.Networking.Vpn.IVpnCustomEditBox, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_NoEcho(self: Windows.Networking.Vpn.IVpnCustomEditBox) -> Boolean: ...
    @winrt_mixinmethod
    def get_Text(self: Windows.Networking.Vpn.IVpnCustomEditBox) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Label(self: Windows.Networking.Vpn.IVpnCustomPrompt, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Label(self: Windows.Networking.Vpn.IVpnCustomPrompt) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Compulsory(self: Windows.Networking.Vpn.IVpnCustomPrompt, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Compulsory(self: Windows.Networking.Vpn.IVpnCustomPrompt) -> Boolean: ...
    @winrt_mixinmethod
    def put_Bordered(self: Windows.Networking.Vpn.IVpnCustomPrompt, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Bordered(self: Windows.Networking.Vpn.IVpnCustomPrompt) -> Boolean: ...
    DefaultText = property(get_DefaultText, put_DefaultText)
    NoEcho = property(get_NoEcho, put_NoEcho)
    Text = property(get_Text, None)
    Label = property(get_Label, put_Label)
    Compulsory = property(get_Compulsory, put_Compulsory)
    Bordered = property(get_Bordered, put_Bordered)
class VpnCustomErrorBox(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnCustomErrorBox'
    @winrt_activatemethod
    def New(cls) -> Windows.Networking.Vpn.VpnCustomErrorBox: ...
    @winrt_mixinmethod
    def put_Label(self: Windows.Networking.Vpn.IVpnCustomPrompt, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Label(self: Windows.Networking.Vpn.IVpnCustomPrompt) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Compulsory(self: Windows.Networking.Vpn.IVpnCustomPrompt, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Compulsory(self: Windows.Networking.Vpn.IVpnCustomPrompt) -> Boolean: ...
    @winrt_mixinmethod
    def put_Bordered(self: Windows.Networking.Vpn.IVpnCustomPrompt, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Bordered(self: Windows.Networking.Vpn.IVpnCustomPrompt) -> Boolean: ...
    Label = property(get_Label, put_Label)
    Compulsory = property(get_Compulsory, put_Compulsory)
    Bordered = property(get_Bordered, put_Bordered)
class VpnCustomPromptBooleanInput(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnCustomPromptBooleanInput'
    @winrt_activatemethod
    def New(cls) -> Windows.Networking.Vpn.VpnCustomPromptBooleanInput: ...
    @winrt_mixinmethod
    def put_InitialValue(self: Windows.Networking.Vpn.IVpnCustomPromptBooleanInput, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_InitialValue(self: Windows.Networking.Vpn.IVpnCustomPromptBooleanInput) -> Boolean: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Networking.Vpn.IVpnCustomPromptBooleanInput) -> Boolean: ...
    @winrt_mixinmethod
    def put_DisplayName(self: Windows.Networking.Vpn.IVpnCustomPromptElement, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Networking.Vpn.IVpnCustomPromptElement) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Compulsory(self: Windows.Networking.Vpn.IVpnCustomPromptElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Compulsory(self: Windows.Networking.Vpn.IVpnCustomPromptElement) -> Boolean: ...
    @winrt_mixinmethod
    def put_Emphasized(self: Windows.Networking.Vpn.IVpnCustomPromptElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Emphasized(self: Windows.Networking.Vpn.IVpnCustomPromptElement) -> Boolean: ...
    InitialValue = property(get_InitialValue, put_InitialValue)
    Value = property(get_Value, None)
    DisplayName = property(get_DisplayName, put_DisplayName)
    Compulsory = property(get_Compulsory, put_Compulsory)
    Emphasized = property(get_Emphasized, put_Emphasized)
class VpnCustomPromptOptionSelector(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnCustomPromptOptionSelector'
    @winrt_activatemethod
    def New(cls) -> Windows.Networking.Vpn.VpnCustomPromptOptionSelector: ...
    @winrt_mixinmethod
    def get_Options(self: Windows.Networking.Vpn.IVpnCustomPromptOptionSelector) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_SelectedIndex(self: Windows.Networking.Vpn.IVpnCustomPromptOptionSelector) -> UInt32: ...
    @winrt_mixinmethod
    def put_DisplayName(self: Windows.Networking.Vpn.IVpnCustomPromptElement, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Networking.Vpn.IVpnCustomPromptElement) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Compulsory(self: Windows.Networking.Vpn.IVpnCustomPromptElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Compulsory(self: Windows.Networking.Vpn.IVpnCustomPromptElement) -> Boolean: ...
    @winrt_mixinmethod
    def put_Emphasized(self: Windows.Networking.Vpn.IVpnCustomPromptElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Emphasized(self: Windows.Networking.Vpn.IVpnCustomPromptElement) -> Boolean: ...
    Options = property(get_Options, None)
    SelectedIndex = property(get_SelectedIndex, None)
    DisplayName = property(get_DisplayName, put_DisplayName)
    Compulsory = property(get_Compulsory, put_Compulsory)
    Emphasized = property(get_Emphasized, put_Emphasized)
class VpnCustomPromptText(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnCustomPromptText'
    @winrt_activatemethod
    def New(cls) -> Windows.Networking.Vpn.VpnCustomPromptText: ...
    @winrt_mixinmethod
    def put_Text(self: Windows.Networking.Vpn.IVpnCustomPromptText, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Text(self: Windows.Networking.Vpn.IVpnCustomPromptText) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: Windows.Networking.Vpn.IVpnCustomPromptElement, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Networking.Vpn.IVpnCustomPromptElement) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Compulsory(self: Windows.Networking.Vpn.IVpnCustomPromptElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Compulsory(self: Windows.Networking.Vpn.IVpnCustomPromptElement) -> Boolean: ...
    @winrt_mixinmethod
    def put_Emphasized(self: Windows.Networking.Vpn.IVpnCustomPromptElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Emphasized(self: Windows.Networking.Vpn.IVpnCustomPromptElement) -> Boolean: ...
    Text = property(get_Text, put_Text)
    DisplayName = property(get_DisplayName, put_DisplayName)
    Compulsory = property(get_Compulsory, put_Compulsory)
    Emphasized = property(get_Emphasized, put_Emphasized)
class VpnCustomPromptTextInput(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnCustomPromptTextInput'
    @winrt_activatemethod
    def New(cls) -> Windows.Networking.Vpn.VpnCustomPromptTextInput: ...
    @winrt_mixinmethod
    def put_PlaceholderText(self: Windows.Networking.Vpn.IVpnCustomPromptTextInput, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PlaceholderText(self: Windows.Networking.Vpn.IVpnCustomPromptTextInput) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_IsTextHidden(self: Windows.Networking.Vpn.IVpnCustomPromptTextInput, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsTextHidden(self: Windows.Networking.Vpn.IVpnCustomPromptTextInput) -> Boolean: ...
    @winrt_mixinmethod
    def get_Text(self: Windows.Networking.Vpn.IVpnCustomPromptTextInput) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: Windows.Networking.Vpn.IVpnCustomPromptElement, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Networking.Vpn.IVpnCustomPromptElement) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Compulsory(self: Windows.Networking.Vpn.IVpnCustomPromptElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Compulsory(self: Windows.Networking.Vpn.IVpnCustomPromptElement) -> Boolean: ...
    @winrt_mixinmethod
    def put_Emphasized(self: Windows.Networking.Vpn.IVpnCustomPromptElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Emphasized(self: Windows.Networking.Vpn.IVpnCustomPromptElement) -> Boolean: ...
    PlaceholderText = property(get_PlaceholderText, put_PlaceholderText)
    IsTextHidden = property(get_IsTextHidden, put_IsTextHidden)
    Text = property(get_Text, None)
    DisplayName = property(get_DisplayName, put_DisplayName)
    Compulsory = property(get_Compulsory, put_Compulsory)
    Emphasized = property(get_Emphasized, put_Emphasized)
class VpnCustomTextBox(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnCustomTextBox'
    @winrt_activatemethod
    def New(cls) -> Windows.Networking.Vpn.VpnCustomTextBox: ...
    @winrt_mixinmethod
    def put_DisplayText(self: Windows.Networking.Vpn.IVpnCustomTextBox, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayText(self: Windows.Networking.Vpn.IVpnCustomTextBox) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Label(self: Windows.Networking.Vpn.IVpnCustomPrompt, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Label(self: Windows.Networking.Vpn.IVpnCustomPrompt) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Compulsory(self: Windows.Networking.Vpn.IVpnCustomPrompt, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Compulsory(self: Windows.Networking.Vpn.IVpnCustomPrompt) -> Boolean: ...
    @winrt_mixinmethod
    def put_Bordered(self: Windows.Networking.Vpn.IVpnCustomPrompt, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Bordered(self: Windows.Networking.Vpn.IVpnCustomPrompt) -> Boolean: ...
    DisplayText = property(get_DisplayText, put_DisplayText)
    Label = property(get_Label, put_Label)
    Compulsory = property(get_Compulsory, put_Compulsory)
    Bordered = property(get_Bordered, put_Bordered)
VpnDataPathType = Int32
VpnDataPathType_Send: VpnDataPathType = 0
VpnDataPathType_Receive: VpnDataPathType = 1
class VpnDomainNameAssignment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnDomainNameAssignment'
    @winrt_activatemethod
    def New(cls) -> Windows.Networking.Vpn.VpnDomainNameAssignment: ...
    @winrt_mixinmethod
    def get_DomainNameList(self: Windows.Networking.Vpn.IVpnDomainNameAssignment) -> Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnDomainNameInfo]: ...
    @winrt_mixinmethod
    def put_ProxyAutoConfigurationUri(self: Windows.Networking.Vpn.IVpnDomainNameAssignment, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ProxyAutoConfigurationUri(self: Windows.Networking.Vpn.IVpnDomainNameAssignment) -> Windows.Foundation.Uri: ...
    DomainNameList = property(get_DomainNameList, None)
    ProxyAutoConfigurationUri = property(get_ProxyAutoConfigurationUri, put_ProxyAutoConfigurationUri)
class VpnDomainNameInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnDomainNameInfo'
    @winrt_factorymethod
    def CreateVpnDomainNameInfo(cls: Windows.Networking.Vpn.IVpnDomainNameInfoFactory, name: WinRT_String, nameType: Windows.Networking.Vpn.VpnDomainNameType, dnsServerList: Windows.Foundation.Collections.IIterable[Windows.Networking.HostName], proxyServerList: Windows.Foundation.Collections.IIterable[Windows.Networking.HostName]) -> Windows.Networking.Vpn.VpnDomainNameInfo: ...
    @winrt_mixinmethod
    def put_DomainName(self: Windows.Networking.Vpn.IVpnDomainNameInfo, value: Windows.Networking.HostName) -> Void: ...
    @winrt_mixinmethod
    def get_DomainName(self: Windows.Networking.Vpn.IVpnDomainNameInfo) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def put_DomainNameType(self: Windows.Networking.Vpn.IVpnDomainNameInfo, value: Windows.Networking.Vpn.VpnDomainNameType) -> Void: ...
    @winrt_mixinmethod
    def get_DomainNameType(self: Windows.Networking.Vpn.IVpnDomainNameInfo) -> Windows.Networking.Vpn.VpnDomainNameType: ...
    @winrt_mixinmethod
    def get_DnsServers(self: Windows.Networking.Vpn.IVpnDomainNameInfo) -> Windows.Foundation.Collections.IVector[Windows.Networking.HostName]: ...
    @winrt_mixinmethod
    def get_WebProxyServers(self: Windows.Networking.Vpn.IVpnDomainNameInfo) -> Windows.Foundation.Collections.IVector[Windows.Networking.HostName]: ...
    @winrt_mixinmethod
    def get_WebProxyUris(self: Windows.Networking.Vpn.IVpnDomainNameInfo2) -> Windows.Foundation.Collections.IVector[Windows.Foundation.Uri]: ...
    DomainName = property(get_DomainName, put_DomainName)
    DomainNameType = property(get_DomainNameType, put_DomainNameType)
    DnsServers = property(get_DnsServers, None)
    WebProxyServers = property(get_WebProxyServers, None)
    WebProxyUris = property(get_WebProxyUris, None)
VpnDomainNameType = Int32
VpnDomainNameType_Suffix: VpnDomainNameType = 0
VpnDomainNameType_FullyQualified: VpnDomainNameType = 1
VpnDomainNameType_Reserved: VpnDomainNameType = 65535
class VpnForegroundActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnForegroundActivatedEventArgs'
    @winrt_mixinmethod
    def get_ProfileName(self: Windows.Networking.Vpn.IVpnForegroundActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SharedContext(self: Windows.Networking.Vpn.IVpnForegroundActivatedEventArgs) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_ActivationOperation(self: Windows.Networking.Vpn.IVpnForegroundActivatedEventArgs) -> Windows.Networking.Vpn.VpnForegroundActivationOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    ProfileName = property(get_ProfileName, None)
    SharedContext = property(get_SharedContext, None)
    ActivationOperation = property(get_ActivationOperation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class VpnForegroundActivationOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnForegroundActivationOperation'
    @winrt_mixinmethod
    def Complete(self: Windows.Networking.Vpn.IVpnForegroundActivationOperation, result: Windows.Foundation.Collections.ValueSet) -> Void: ...
VpnIPProtocol = Int32
VpnIPProtocol_None: VpnIPProtocol = 0
VpnIPProtocol_Tcp: VpnIPProtocol = 6
VpnIPProtocol_Udp: VpnIPProtocol = 17
VpnIPProtocol_Icmp: VpnIPProtocol = 1
VpnIPProtocol_Ipv6Icmp: VpnIPProtocol = 58
VpnIPProtocol_Igmp: VpnIPProtocol = 2
VpnIPProtocol_Pgm: VpnIPProtocol = 113
class VpnInterfaceId(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnInterfaceId'
    @winrt_factorymethod
    def CreateVpnInterfaceId(cls: Windows.Networking.Vpn.IVpnInterfaceIdFactory, address: c_char_p_no) -> Windows.Networking.Vpn.VpnInterfaceId: ...
    @winrt_mixinmethod
    def GetAddressInfo(self: Windows.Networking.Vpn.IVpnInterfaceId, id: POINTER(c_char_p_no)) -> Void: ...
class VpnManagementAgent(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnManagementAgent'
    @winrt_activatemethod
    def New(cls) -> Windows.Networking.Vpn.VpnManagementAgent: ...
    @winrt_mixinmethod
    def AddProfileFromXmlAsync(self: Windows.Networking.Vpn.IVpnManagementAgent, xml: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_mixinmethod
    def AddProfileFromObjectAsync(self: Windows.Networking.Vpn.IVpnManagementAgent, profile: Windows.Networking.Vpn.IVpnProfile) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_mixinmethod
    def UpdateProfileFromXmlAsync(self: Windows.Networking.Vpn.IVpnManagementAgent, xml: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_mixinmethod
    def UpdateProfileFromObjectAsync(self: Windows.Networking.Vpn.IVpnManagementAgent, profile: Windows.Networking.Vpn.IVpnProfile) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_mixinmethod
    def GetProfilesAsync(self: Windows.Networking.Vpn.IVpnManagementAgent) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Networking.Vpn.IVpnProfile]]: ...
    @winrt_mixinmethod
    def DeleteProfileAsync(self: Windows.Networking.Vpn.IVpnManagementAgent, profile: Windows.Networking.Vpn.IVpnProfile) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_mixinmethod
    def ConnectProfileAsync(self: Windows.Networking.Vpn.IVpnManagementAgent, profile: Windows.Networking.Vpn.IVpnProfile) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_mixinmethod
    def ConnectProfileWithPasswordCredentialAsync(self: Windows.Networking.Vpn.IVpnManagementAgent, profile: Windows.Networking.Vpn.IVpnProfile, passwordCredential: Windows.Security.Credentials.PasswordCredential) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_mixinmethod
    def DisconnectProfileAsync(self: Windows.Networking.Vpn.IVpnManagementAgent, profile: Windows.Networking.Vpn.IVpnProfile) -> Windows.Foundation.IAsyncOperation[Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
VpnManagementConnectionStatus = Int32
VpnManagementConnectionStatus_Disconnected: VpnManagementConnectionStatus = 0
VpnManagementConnectionStatus_Disconnecting: VpnManagementConnectionStatus = 1
VpnManagementConnectionStatus_Connected: VpnManagementConnectionStatus = 2
VpnManagementConnectionStatus_Connecting: VpnManagementConnectionStatus = 3
VpnManagementErrorStatus = Int32
VpnManagementErrorStatus_Ok: VpnManagementErrorStatus = 0
VpnManagementErrorStatus_Other: VpnManagementErrorStatus = 1
VpnManagementErrorStatus_InvalidXmlSyntax: VpnManagementErrorStatus = 2
VpnManagementErrorStatus_ProfileNameTooLong: VpnManagementErrorStatus = 3
VpnManagementErrorStatus_ProfileInvalidAppId: VpnManagementErrorStatus = 4
VpnManagementErrorStatus_AccessDenied: VpnManagementErrorStatus = 5
VpnManagementErrorStatus_CannotFindProfile: VpnManagementErrorStatus = 6
VpnManagementErrorStatus_AlreadyDisconnecting: VpnManagementErrorStatus = 7
VpnManagementErrorStatus_AlreadyConnected: VpnManagementErrorStatus = 8
VpnManagementErrorStatus_GeneralAuthenticationFailure: VpnManagementErrorStatus = 9
VpnManagementErrorStatus_EapFailure: VpnManagementErrorStatus = 10
VpnManagementErrorStatus_SmartCardFailure: VpnManagementErrorStatus = 11
VpnManagementErrorStatus_CertificateFailure: VpnManagementErrorStatus = 12
VpnManagementErrorStatus_ServerConfiguration: VpnManagementErrorStatus = 13
VpnManagementErrorStatus_NoConnection: VpnManagementErrorStatus = 14
VpnManagementErrorStatus_ServerConnection: VpnManagementErrorStatus = 15
VpnManagementErrorStatus_UserNamePassword: VpnManagementErrorStatus = 16
VpnManagementErrorStatus_DnsNotResolvable: VpnManagementErrorStatus = 17
VpnManagementErrorStatus_InvalidIP: VpnManagementErrorStatus = 18
class VpnNamespaceAssignment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnNamespaceAssignment'
    @winrt_activatemethod
    def New(cls) -> Windows.Networking.Vpn.VpnNamespaceAssignment: ...
    @winrt_mixinmethod
    def put_NamespaceList(self: Windows.Networking.Vpn.IVpnNamespaceAssignment, value: Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnNamespaceInfo]) -> Void: ...
    @winrt_mixinmethod
    def get_NamespaceList(self: Windows.Networking.Vpn.IVpnNamespaceAssignment) -> Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnNamespaceInfo]: ...
    @winrt_mixinmethod
    def put_ProxyAutoConfigUri(self: Windows.Networking.Vpn.IVpnNamespaceAssignment, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ProxyAutoConfigUri(self: Windows.Networking.Vpn.IVpnNamespaceAssignment) -> Windows.Foundation.Uri: ...
    NamespaceList = property(get_NamespaceList, put_NamespaceList)
    ProxyAutoConfigUri = property(get_ProxyAutoConfigUri, put_ProxyAutoConfigUri)
class VpnNamespaceInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnNamespaceInfo'
    @winrt_factorymethod
    def CreateVpnNamespaceInfo(cls: Windows.Networking.Vpn.IVpnNamespaceInfoFactory, name: WinRT_String, dnsServerList: Windows.Foundation.Collections.IVector[Windows.Networking.HostName], proxyServerList: Windows.Foundation.Collections.IVector[Windows.Networking.HostName]) -> Windows.Networking.Vpn.VpnNamespaceInfo: ...
    @winrt_mixinmethod
    def put_Namespace(self: Windows.Networking.Vpn.IVpnNamespaceInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Namespace(self: Windows.Networking.Vpn.IVpnNamespaceInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DnsServers(self: Windows.Networking.Vpn.IVpnNamespaceInfo, value: Windows.Foundation.Collections.IVector[Windows.Networking.HostName]) -> Void: ...
    @winrt_mixinmethod
    def get_DnsServers(self: Windows.Networking.Vpn.IVpnNamespaceInfo) -> Windows.Foundation.Collections.IVector[Windows.Networking.HostName]: ...
    @winrt_mixinmethod
    def put_WebProxyServers(self: Windows.Networking.Vpn.IVpnNamespaceInfo, value: Windows.Foundation.Collections.IVector[Windows.Networking.HostName]) -> Void: ...
    @winrt_mixinmethod
    def get_WebProxyServers(self: Windows.Networking.Vpn.IVpnNamespaceInfo) -> Windows.Foundation.Collections.IVector[Windows.Networking.HostName]: ...
    Namespace = property(get_Namespace, put_Namespace)
    DnsServers = property(get_DnsServers, put_DnsServers)
    WebProxyServers = property(get_WebProxyServers, put_WebProxyServers)
class VpnNativeProfile(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnNativeProfile'
    @winrt_activatemethod
    def New(cls) -> Windows.Networking.Vpn.VpnNativeProfile: ...
    @winrt_mixinmethod
    def get_Servers(self: Windows.Networking.Vpn.IVpnNativeProfile) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_RoutingPolicyType(self: Windows.Networking.Vpn.IVpnNativeProfile) -> Windows.Networking.Vpn.VpnRoutingPolicyType: ...
    @winrt_mixinmethod
    def put_RoutingPolicyType(self: Windows.Networking.Vpn.IVpnNativeProfile, value: Windows.Networking.Vpn.VpnRoutingPolicyType) -> Void: ...
    @winrt_mixinmethod
    def get_NativeProtocolType(self: Windows.Networking.Vpn.IVpnNativeProfile) -> Windows.Networking.Vpn.VpnNativeProtocolType: ...
    @winrt_mixinmethod
    def put_NativeProtocolType(self: Windows.Networking.Vpn.IVpnNativeProfile, value: Windows.Networking.Vpn.VpnNativeProtocolType) -> Void: ...
    @winrt_mixinmethod
    def get_UserAuthenticationMethod(self: Windows.Networking.Vpn.IVpnNativeProfile) -> Windows.Networking.Vpn.VpnAuthenticationMethod: ...
    @winrt_mixinmethod
    def put_UserAuthenticationMethod(self: Windows.Networking.Vpn.IVpnNativeProfile, value: Windows.Networking.Vpn.VpnAuthenticationMethod) -> Void: ...
    @winrt_mixinmethod
    def get_TunnelAuthenticationMethod(self: Windows.Networking.Vpn.IVpnNativeProfile) -> Windows.Networking.Vpn.VpnAuthenticationMethod: ...
    @winrt_mixinmethod
    def put_TunnelAuthenticationMethod(self: Windows.Networking.Vpn.IVpnNativeProfile, value: Windows.Networking.Vpn.VpnAuthenticationMethod) -> Void: ...
    @winrt_mixinmethod
    def get_EapConfiguration(self: Windows.Networking.Vpn.IVpnNativeProfile) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_EapConfiguration(self: Windows.Networking.Vpn.IVpnNativeProfile, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ProfileName(self: Windows.Networking.Vpn.IVpnProfile) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ProfileName(self: Windows.Networking.Vpn.IVpnProfile, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AppTriggers(self: Windows.Networking.Vpn.IVpnProfile) -> Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnAppId]: ...
    @winrt_mixinmethod
    def get_Routes(self: Windows.Networking.Vpn.IVpnProfile) -> Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnRoute]: ...
    @winrt_mixinmethod
    def get_DomainNameInfoList(self: Windows.Networking.Vpn.IVpnProfile) -> Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnDomainNameInfo]: ...
    @winrt_mixinmethod
    def get_TrafficFilters(self: Windows.Networking.Vpn.IVpnProfile) -> Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnTrafficFilter]: ...
    @winrt_mixinmethod
    def get_RememberCredentials(self: Windows.Networking.Vpn.IVpnProfile) -> Boolean: ...
    @winrt_mixinmethod
    def put_RememberCredentials(self: Windows.Networking.Vpn.IVpnProfile, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AlwaysOn(self: Windows.Networking.Vpn.IVpnProfile) -> Boolean: ...
    @winrt_mixinmethod
    def put_AlwaysOn(self: Windows.Networking.Vpn.IVpnProfile, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_RequireVpnClientAppUI(self: Windows.Networking.Vpn.IVpnNativeProfile2) -> Boolean: ...
    @winrt_mixinmethod
    def put_RequireVpnClientAppUI(self: Windows.Networking.Vpn.IVpnNativeProfile2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ConnectionStatus(self: Windows.Networking.Vpn.IVpnNativeProfile2) -> Windows.Networking.Vpn.VpnManagementConnectionStatus: ...
    Servers = property(get_Servers, None)
    RoutingPolicyType = property(get_RoutingPolicyType, put_RoutingPolicyType)
    NativeProtocolType = property(get_NativeProtocolType, put_NativeProtocolType)
    UserAuthenticationMethod = property(get_UserAuthenticationMethod, put_UserAuthenticationMethod)
    TunnelAuthenticationMethod = property(get_TunnelAuthenticationMethod, put_TunnelAuthenticationMethod)
    EapConfiguration = property(get_EapConfiguration, put_EapConfiguration)
    ProfileName = property(get_ProfileName, put_ProfileName)
    AppTriggers = property(get_AppTriggers, None)
    Routes = property(get_Routes, None)
    DomainNameInfoList = property(get_DomainNameInfoList, None)
    TrafficFilters = property(get_TrafficFilters, None)
    RememberCredentials = property(get_RememberCredentials, put_RememberCredentials)
    AlwaysOn = property(get_AlwaysOn, put_AlwaysOn)
    RequireVpnClientAppUI = property(get_RequireVpnClientAppUI, put_RequireVpnClientAppUI)
    ConnectionStatus = property(get_ConnectionStatus, None)
VpnNativeProtocolType = Int32
VpnNativeProtocolType_Pptp: VpnNativeProtocolType = 0
VpnNativeProtocolType_L2tp: VpnNativeProtocolType = 1
VpnNativeProtocolType_IpsecIkev2: VpnNativeProtocolType = 2
class VpnPacketBuffer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnPacketBuffer'
    @winrt_factorymethod
    def CreateVpnPacketBuffer(cls: Windows.Networking.Vpn.IVpnPacketBufferFactory, parentBuffer: Windows.Networking.Vpn.VpnPacketBuffer, offset: UInt32, length: UInt32) -> Windows.Networking.Vpn.VpnPacketBuffer: ...
    @winrt_mixinmethod
    def get_Buffer(self: Windows.Networking.Vpn.IVpnPacketBuffer) -> Windows.Storage.Streams.Buffer: ...
    @winrt_mixinmethod
    def put_Status(self: Windows.Networking.Vpn.IVpnPacketBuffer, value: Windows.Networking.Vpn.VpnPacketBufferStatus) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Networking.Vpn.IVpnPacketBuffer) -> Windows.Networking.Vpn.VpnPacketBufferStatus: ...
    @winrt_mixinmethod
    def put_TransportAffinity(self: Windows.Networking.Vpn.IVpnPacketBuffer, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_TransportAffinity(self: Windows.Networking.Vpn.IVpnPacketBuffer) -> UInt32: ...
    @winrt_mixinmethod
    def get_AppId(self: Windows.Networking.Vpn.IVpnPacketBuffer2) -> Windows.Networking.Vpn.VpnAppId: ...
    @winrt_mixinmethod
    def put_TransportContext(self: Windows.Networking.Vpn.IVpnPacketBuffer3, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def get_TransportContext(self: Windows.Networking.Vpn.IVpnPacketBuffer3) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    Buffer = property(get_Buffer, None)
    Status = property(get_Status, put_Status)
    TransportAffinity = property(get_TransportAffinity, put_TransportAffinity)
    AppId = property(get_AppId, None)
    TransportContext = property(get_TransportContext, put_TransportContext)
class VpnPacketBufferList(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnPacketBufferList'
    @winrt_mixinmethod
    def Append(self: Windows.Networking.Vpn.IVpnPacketBufferList, nextVpnPacketBuffer: Windows.Networking.Vpn.VpnPacketBuffer) -> Void: ...
    @winrt_mixinmethod
    def AddAtBegin(self: Windows.Networking.Vpn.IVpnPacketBufferList, nextVpnPacketBuffer: Windows.Networking.Vpn.VpnPacketBuffer) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Networking.Vpn.IVpnPacketBufferList) -> Windows.Networking.Vpn.VpnPacketBuffer: ...
    @winrt_mixinmethod
    def RemoveAtBegin(self: Windows.Networking.Vpn.IVpnPacketBufferList) -> Windows.Networking.Vpn.VpnPacketBuffer: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Networking.Vpn.IVpnPacketBufferList) -> Void: ...
    @winrt_mixinmethod
    def put_Status(self: Windows.Networking.Vpn.IVpnPacketBufferList, value: Windows.Networking.Vpn.VpnPacketBufferStatus) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Networking.Vpn.IVpnPacketBufferList) -> Windows.Networking.Vpn.VpnPacketBufferStatus: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Networking.Vpn.IVpnPacketBufferList) -> UInt32: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Networking.Vpn.VpnPacketBuffer]) -> Windows.Foundation.Collections.IIterator[Windows.Networking.Vpn.VpnPacketBuffer]: ...
    Status = property(get_Status, put_Status)
    Size = property(get_Size, None)
VpnPacketBufferStatus = Int32
VpnPacketBufferStatus_Ok: VpnPacketBufferStatus = 0
VpnPacketBufferStatus_InvalidBufferSize: VpnPacketBufferStatus = 1
class VpnPickedCredential(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnPickedCredential'
    @winrt_mixinmethod
    def get_PasskeyCredential(self: Windows.Networking.Vpn.IVpnPickedCredential) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def get_AdditionalPin(self: Windows.Networking.Vpn.IVpnPickedCredential) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OldPasswordCredential(self: Windows.Networking.Vpn.IVpnPickedCredential) -> Windows.Security.Credentials.PasswordCredential: ...
    PasskeyCredential = property(get_PasskeyCredential, None)
    AdditionalPin = property(get_AdditionalPin, None)
    OldPasswordCredential = property(get_OldPasswordCredential, None)
class VpnPlugInProfile(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnPlugInProfile'
    @winrt_activatemethod
    def New(cls) -> Windows.Networking.Vpn.VpnPlugInProfile: ...
    @winrt_mixinmethod
    def get_ServerUris(self: Windows.Networking.Vpn.IVpnPlugInProfile) -> Windows.Foundation.Collections.IVector[Windows.Foundation.Uri]: ...
    @winrt_mixinmethod
    def get_CustomConfiguration(self: Windows.Networking.Vpn.IVpnPlugInProfile) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CustomConfiguration(self: Windows.Networking.Vpn.IVpnPlugInProfile, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_VpnPluginPackageFamilyName(self: Windows.Networking.Vpn.IVpnPlugInProfile) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_VpnPluginPackageFamilyName(self: Windows.Networking.Vpn.IVpnPlugInProfile, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ProfileName(self: Windows.Networking.Vpn.IVpnProfile) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ProfileName(self: Windows.Networking.Vpn.IVpnProfile, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AppTriggers(self: Windows.Networking.Vpn.IVpnProfile) -> Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnAppId]: ...
    @winrt_mixinmethod
    def get_Routes(self: Windows.Networking.Vpn.IVpnProfile) -> Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnRoute]: ...
    @winrt_mixinmethod
    def get_DomainNameInfoList(self: Windows.Networking.Vpn.IVpnProfile) -> Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnDomainNameInfo]: ...
    @winrt_mixinmethod
    def get_TrafficFilters(self: Windows.Networking.Vpn.IVpnProfile) -> Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnTrafficFilter]: ...
    @winrt_mixinmethod
    def get_RememberCredentials(self: Windows.Networking.Vpn.IVpnProfile) -> Boolean: ...
    @winrt_mixinmethod
    def put_RememberCredentials(self: Windows.Networking.Vpn.IVpnProfile, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AlwaysOn(self: Windows.Networking.Vpn.IVpnProfile) -> Boolean: ...
    @winrt_mixinmethod
    def put_AlwaysOn(self: Windows.Networking.Vpn.IVpnProfile, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_RequireVpnClientAppUI(self: Windows.Networking.Vpn.IVpnPlugInProfile2) -> Boolean: ...
    @winrt_mixinmethod
    def put_RequireVpnClientAppUI(self: Windows.Networking.Vpn.IVpnPlugInProfile2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ConnectionStatus(self: Windows.Networking.Vpn.IVpnPlugInProfile2) -> Windows.Networking.Vpn.VpnManagementConnectionStatus: ...
    ServerUris = property(get_ServerUris, None)
    CustomConfiguration = property(get_CustomConfiguration, put_CustomConfiguration)
    VpnPluginPackageFamilyName = property(get_VpnPluginPackageFamilyName, put_VpnPluginPackageFamilyName)
    ProfileName = property(get_ProfileName, put_ProfileName)
    AppTriggers = property(get_AppTriggers, None)
    Routes = property(get_Routes, None)
    DomainNameInfoList = property(get_DomainNameInfoList, None)
    TrafficFilters = property(get_TrafficFilters, None)
    RememberCredentials = property(get_RememberCredentials, put_RememberCredentials)
    AlwaysOn = property(get_AlwaysOn, put_AlwaysOn)
    RequireVpnClientAppUI = property(get_RequireVpnClientAppUI, put_RequireVpnClientAppUI)
    ConnectionStatus = property(get_ConnectionStatus, None)
class VpnRoute(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnRoute'
    @winrt_factorymethod
    def CreateVpnRoute(cls: Windows.Networking.Vpn.IVpnRouteFactory, address: Windows.Networking.HostName, prefixSize: Byte) -> Windows.Networking.Vpn.VpnRoute: ...
    @winrt_mixinmethod
    def put_Address(self: Windows.Networking.Vpn.IVpnRoute, value: Windows.Networking.HostName) -> Void: ...
    @winrt_mixinmethod
    def get_Address(self: Windows.Networking.Vpn.IVpnRoute) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def put_PrefixSize(self: Windows.Networking.Vpn.IVpnRoute, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_PrefixSize(self: Windows.Networking.Vpn.IVpnRoute) -> Byte: ...
    Address = property(get_Address, put_Address)
    PrefixSize = property(get_PrefixSize, put_PrefixSize)
class VpnRouteAssignment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnRouteAssignment'
    @winrt_activatemethod
    def New(cls) -> Windows.Networking.Vpn.VpnRouteAssignment: ...
    @winrt_mixinmethod
    def put_Ipv4InclusionRoutes(self: Windows.Networking.Vpn.IVpnRouteAssignment, value: Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnRoute]) -> Void: ...
    @winrt_mixinmethod
    def put_Ipv6InclusionRoutes(self: Windows.Networking.Vpn.IVpnRouteAssignment, value: Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnRoute]) -> Void: ...
    @winrt_mixinmethod
    def get_Ipv4InclusionRoutes(self: Windows.Networking.Vpn.IVpnRouteAssignment) -> Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnRoute]: ...
    @winrt_mixinmethod
    def get_Ipv6InclusionRoutes(self: Windows.Networking.Vpn.IVpnRouteAssignment) -> Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnRoute]: ...
    @winrt_mixinmethod
    def put_Ipv4ExclusionRoutes(self: Windows.Networking.Vpn.IVpnRouteAssignment, value: Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnRoute]) -> Void: ...
    @winrt_mixinmethod
    def put_Ipv6ExclusionRoutes(self: Windows.Networking.Vpn.IVpnRouteAssignment, value: Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnRoute]) -> Void: ...
    @winrt_mixinmethod
    def get_Ipv4ExclusionRoutes(self: Windows.Networking.Vpn.IVpnRouteAssignment) -> Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnRoute]: ...
    @winrt_mixinmethod
    def get_Ipv6ExclusionRoutes(self: Windows.Networking.Vpn.IVpnRouteAssignment) -> Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnRoute]: ...
    @winrt_mixinmethod
    def put_ExcludeLocalSubnets(self: Windows.Networking.Vpn.IVpnRouteAssignment, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ExcludeLocalSubnets(self: Windows.Networking.Vpn.IVpnRouteAssignment) -> Boolean: ...
    Ipv4InclusionRoutes = property(get_Ipv4InclusionRoutes, put_Ipv4InclusionRoutes)
    Ipv6InclusionRoutes = property(get_Ipv6InclusionRoutes, put_Ipv6InclusionRoutes)
    Ipv4ExclusionRoutes = property(get_Ipv4ExclusionRoutes, put_Ipv4ExclusionRoutes)
    Ipv6ExclusionRoutes = property(get_Ipv6ExclusionRoutes, put_Ipv6ExclusionRoutes)
    ExcludeLocalSubnets = property(get_ExcludeLocalSubnets, put_ExcludeLocalSubnets)
VpnRoutingPolicyType = Int32
VpnRoutingPolicyType_SplitRouting: VpnRoutingPolicyType = 0
VpnRoutingPolicyType_ForceAllTrafficOverVpn: VpnRoutingPolicyType = 1
class VpnSystemHealth(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnSystemHealth'
    @winrt_mixinmethod
    def get_StatementOfHealth(self: Windows.Networking.Vpn.IVpnSystemHealth) -> Windows.Storage.Streams.Buffer: ...
    StatementOfHealth = property(get_StatementOfHealth, None)
class VpnTrafficFilter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnTrafficFilter'
    @winrt_factorymethod
    def Create(cls: Windows.Networking.Vpn.IVpnTrafficFilterFactory, appId: Windows.Networking.Vpn.VpnAppId) -> Windows.Networking.Vpn.VpnTrafficFilter: ...
    @winrt_mixinmethod
    def get_AppId(self: Windows.Networking.Vpn.IVpnTrafficFilter) -> Windows.Networking.Vpn.VpnAppId: ...
    @winrt_mixinmethod
    def put_AppId(self: Windows.Networking.Vpn.IVpnTrafficFilter, value: Windows.Networking.Vpn.VpnAppId) -> Void: ...
    @winrt_mixinmethod
    def get_AppClaims(self: Windows.Networking.Vpn.IVpnTrafficFilter) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Protocol(self: Windows.Networking.Vpn.IVpnTrafficFilter) -> Windows.Networking.Vpn.VpnIPProtocol: ...
    @winrt_mixinmethod
    def put_Protocol(self: Windows.Networking.Vpn.IVpnTrafficFilter, value: Windows.Networking.Vpn.VpnIPProtocol) -> Void: ...
    @winrt_mixinmethod
    def get_LocalPortRanges(self: Windows.Networking.Vpn.IVpnTrafficFilter) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_RemotePortRanges(self: Windows.Networking.Vpn.IVpnTrafficFilter) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_LocalAddressRanges(self: Windows.Networking.Vpn.IVpnTrafficFilter) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_RemoteAddressRanges(self: Windows.Networking.Vpn.IVpnTrafficFilter) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_RoutingPolicyType(self: Windows.Networking.Vpn.IVpnTrafficFilter) -> Windows.Networking.Vpn.VpnRoutingPolicyType: ...
    @winrt_mixinmethod
    def put_RoutingPolicyType(self: Windows.Networking.Vpn.IVpnTrafficFilter, value: Windows.Networking.Vpn.VpnRoutingPolicyType) -> Void: ...
    AppId = property(get_AppId, put_AppId)
    AppClaims = property(get_AppClaims, None)
    Protocol = property(get_Protocol, put_Protocol)
    LocalPortRanges = property(get_LocalPortRanges, None)
    RemotePortRanges = property(get_RemotePortRanges, None)
    LocalAddressRanges = property(get_LocalAddressRanges, None)
    RemoteAddressRanges = property(get_RemoteAddressRanges, None)
    RoutingPolicyType = property(get_RoutingPolicyType, put_RoutingPolicyType)
class VpnTrafficFilterAssignment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.VpnTrafficFilterAssignment'
    @winrt_activatemethod
    def New(cls) -> Windows.Networking.Vpn.VpnTrafficFilterAssignment: ...
    @winrt_mixinmethod
    def get_TrafficFilterList(self: Windows.Networking.Vpn.IVpnTrafficFilterAssignment) -> Windows.Foundation.Collections.IVector[Windows.Networking.Vpn.VpnTrafficFilter]: ...
    @winrt_mixinmethod
    def get_AllowOutbound(self: Windows.Networking.Vpn.IVpnTrafficFilterAssignment) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowOutbound(self: Windows.Networking.Vpn.IVpnTrafficFilterAssignment, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AllowInbound(self: Windows.Networking.Vpn.IVpnTrafficFilterAssignment) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowInbound(self: Windows.Networking.Vpn.IVpnTrafficFilterAssignment, value: Boolean) -> Void: ...
    TrafficFilterList = property(get_TrafficFilterList, None)
    AllowOutbound = property(get_AllowOutbound, put_AllowOutbound)
    AllowInbound = property(get_AllowInbound, put_AllowInbound)
make_head(_module, 'IVpnAppId')
make_head(_module, 'IVpnAppIdFactory')
make_head(_module, 'IVpnChannel')
make_head(_module, 'IVpnChannel2')
make_head(_module, 'IVpnChannel4')
make_head(_module, 'IVpnChannel5')
make_head(_module, 'IVpnChannel6')
make_head(_module, 'IVpnChannelActivityEventArgs')
make_head(_module, 'IVpnChannelActivityStateChangedArgs')
make_head(_module, 'IVpnChannelConfiguration')
make_head(_module, 'IVpnChannelConfiguration2')
make_head(_module, 'IVpnChannelStatics')
make_head(_module, 'IVpnCredential')
make_head(_module, 'IVpnCustomCheckBox')
make_head(_module, 'IVpnCustomComboBox')
make_head(_module, 'IVpnCustomEditBox')
make_head(_module, 'IVpnCustomErrorBox')
make_head(_module, 'IVpnCustomPrompt')
make_head(_module, 'IVpnCustomPromptBooleanInput')
make_head(_module, 'IVpnCustomPromptElement')
make_head(_module, 'IVpnCustomPromptOptionSelector')
make_head(_module, 'IVpnCustomPromptText')
make_head(_module, 'IVpnCustomPromptTextInput')
make_head(_module, 'IVpnCustomTextBox')
make_head(_module, 'IVpnDomainNameAssignment')
make_head(_module, 'IVpnDomainNameInfo')
make_head(_module, 'IVpnDomainNameInfo2')
make_head(_module, 'IVpnDomainNameInfoFactory')
make_head(_module, 'IVpnForegroundActivatedEventArgs')
make_head(_module, 'IVpnForegroundActivationOperation')
make_head(_module, 'IVpnInterfaceId')
make_head(_module, 'IVpnInterfaceIdFactory')
make_head(_module, 'IVpnManagementAgent')
make_head(_module, 'IVpnNamespaceAssignment')
make_head(_module, 'IVpnNamespaceInfo')
make_head(_module, 'IVpnNamespaceInfoFactory')
make_head(_module, 'IVpnNativeProfile')
make_head(_module, 'IVpnNativeProfile2')
make_head(_module, 'IVpnPacketBuffer')
make_head(_module, 'IVpnPacketBuffer2')
make_head(_module, 'IVpnPacketBuffer3')
make_head(_module, 'IVpnPacketBufferFactory')
make_head(_module, 'IVpnPacketBufferList')
make_head(_module, 'IVpnPacketBufferList2')
make_head(_module, 'IVpnPickedCredential')
make_head(_module, 'IVpnPlugIn')
make_head(_module, 'IVpnPlugInProfile')
make_head(_module, 'IVpnPlugInProfile2')
make_head(_module, 'IVpnProfile')
make_head(_module, 'IVpnRoute')
make_head(_module, 'IVpnRouteAssignment')
make_head(_module, 'IVpnRouteFactory')
make_head(_module, 'IVpnSystemHealth')
make_head(_module, 'IVpnTrafficFilter')
make_head(_module, 'IVpnTrafficFilterAssignment')
make_head(_module, 'IVpnTrafficFilterFactory')
make_head(_module, 'VpnAppId')
make_head(_module, 'VpnChannel')
make_head(_module, 'VpnChannelActivityEventArgs')
make_head(_module, 'VpnChannelActivityStateChangedArgs')
make_head(_module, 'VpnChannelConfiguration')
make_head(_module, 'VpnCredential')
make_head(_module, 'VpnCustomCheckBox')
make_head(_module, 'VpnCustomComboBox')
make_head(_module, 'VpnCustomEditBox')
make_head(_module, 'VpnCustomErrorBox')
make_head(_module, 'VpnCustomPromptBooleanInput')
make_head(_module, 'VpnCustomPromptOptionSelector')
make_head(_module, 'VpnCustomPromptText')
make_head(_module, 'VpnCustomPromptTextInput')
make_head(_module, 'VpnCustomTextBox')
make_head(_module, 'VpnDomainNameAssignment')
make_head(_module, 'VpnDomainNameInfo')
make_head(_module, 'VpnForegroundActivatedEventArgs')
make_head(_module, 'VpnForegroundActivationOperation')
make_head(_module, 'VpnInterfaceId')
make_head(_module, 'VpnManagementAgent')
make_head(_module, 'VpnNamespaceAssignment')
make_head(_module, 'VpnNamespaceInfo')
make_head(_module, 'VpnNativeProfile')
make_head(_module, 'VpnPacketBuffer')
make_head(_module, 'VpnPacketBufferList')
make_head(_module, 'VpnPickedCredential')
make_head(_module, 'VpnPlugInProfile')
make_head(_module, 'VpnRoute')
make_head(_module, 'VpnRouteAssignment')
make_head(_module, 'VpnSystemHealth')
make_head(_module, 'VpnTrafficFilter')
make_head(_module, 'VpnTrafficFilterAssignment')
