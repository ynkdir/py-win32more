from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Activation
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Networking
import win32more.Windows.Networking.Sockets
import win32more.Windows.Networking.Vpn
import win32more.Windows.Security.Credentials
import win32more.Windows.Security.Cryptography.Certificates
import win32more.Windows.Storage.Streams
import win32more.Windows.System
import win32more.Windows.Win32.System.WinRT
class IVpnAppId(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnAppId'
    _iid_ = Guid('{7b06a635-5c58-41d9-94a7-bfbcf1d8ca54}')
    @winrt_commethod(6)
    def get_Type(self) -> win32more.Windows.Networking.Vpn.VpnAppIdType: ...
    @winrt_commethod(7)
    def put_Type(self, value: win32more.Windows.Networking.Vpn.VpnAppIdType) -> Void: ...
    @winrt_commethod(8)
    def get_Value(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Value(self, value: WinRT_String) -> Void: ...
    Type = property(get_Type, put_Type)
    Value = property(get_Value, put_Value)
class IVpnAppIdFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnAppIdFactory'
    _iid_ = Guid('{46adfd2a-0aab-4fdb-821d-d3ddc919788b}')
    @winrt_commethod(6)
    def Create(self, type: win32more.Windows.Networking.Vpn.VpnAppIdType, value: WinRT_String) -> win32more.Windows.Networking.Vpn.VpnAppId: ...
class IVpnChannel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnChannel'
    _iid_ = Guid('{4ac78d07-d1a8-4303-a091-c8d2e0915bc3}')
    @winrt_commethod(6)
    def AssociateTransport(self, mainOuterTunnelTransport: win32more.Windows.Win32.System.WinRT.IInspectable, optionalOuterTunnelTransport: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(7)
    def Start(self, assignedClientIPv4list: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.HostName], assignedClientIPv6list: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.HostName], vpnInterfaceId: win32more.Windows.Networking.Vpn.VpnInterfaceId, routeScope: win32more.Windows.Networking.Vpn.VpnRouteAssignment, namespaceScope: win32more.Windows.Networking.Vpn.VpnNamespaceAssignment, mtuSize: UInt32, maxFrameSize: UInt32, optimizeForLowCostNetwork: Boolean, mainOuterTunnelTransport: win32more.Windows.Win32.System.WinRT.IInspectable, optionalOuterTunnelTransport: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(8)
    def Stop(self) -> Void: ...
    @winrt_commethod(9)
    def RequestCredentials(self, credType: win32more.Windows.Networking.Vpn.VpnCredentialType, isRetry: Boolean, isSingleSignOnCredential: Boolean, certificate: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> win32more.Windows.Networking.Vpn.VpnPickedCredential: ...
    @winrt_commethod(10)
    def RequestVpnPacketBuffer(self, type: win32more.Windows.Networking.Vpn.VpnDataPathType, vpnPacketBuffer: POINTER(win32more.Windows.Networking.Vpn.VpnPacketBuffer)) -> Void: ...
    @winrt_commethod(11)
    def LogDiagnosticMessage(self, message: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(13)
    def get_Configuration(self) -> win32more.Windows.Networking.Vpn.VpnChannelConfiguration: ...
    @winrt_commethod(14)
    def add_ActivityChange(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.Vpn.VpnChannel, win32more.Windows.Networking.Vpn.VpnChannelActivityEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_ActivityChange(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def put_PlugInContext(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(17)
    def get_PlugInContext(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(18)
    def get_SystemHealth(self) -> win32more.Windows.Networking.Vpn.VpnSystemHealth: ...
    @winrt_commethod(19)
    def RequestCustomPrompt(self, customPrompt: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.Vpn.IVpnCustomPrompt]) -> Void: ...
    @winrt_commethod(20)
    def SetErrorMessage(self, message: WinRT_String) -> Void: ...
    @winrt_commethod(21)
    def SetAllowedSslTlsVersions(self, tunnelTransport: win32more.Windows.Win32.System.WinRT.IInspectable, useTls12: Boolean) -> Void: ...
    Configuration = property(get_Configuration, None)
    Id = property(get_Id, None)
    PlugInContext = property(get_PlugInContext, put_PlugInContext)
    SystemHealth = property(get_SystemHealth, None)
    ActivityChange = event()
class IVpnChannel2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnChannel2'
    _iid_ = Guid('{2255d165-993b-4629-ad60-f1c3f3537f50}')
    @winrt_commethod(6)
    def StartWithMainTransport(self, assignedClientIPv4list: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.HostName], assignedClientIPv6list: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.HostName], vpnInterfaceId: win32more.Windows.Networking.Vpn.VpnInterfaceId, assignedRoutes: win32more.Windows.Networking.Vpn.VpnRouteAssignment, assignedDomainName: win32more.Windows.Networking.Vpn.VpnDomainNameAssignment, mtuSize: UInt32, maxFrameSize: UInt32, Reserved: Boolean, mainOuterTunnelTransport: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(7)
    def StartExistingTransports(self, assignedClientIPv4list: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.HostName], assignedClientIPv6list: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.HostName], vpnInterfaceId: win32more.Windows.Networking.Vpn.VpnInterfaceId, assignedRoutes: win32more.Windows.Networking.Vpn.VpnRouteAssignment, assignedDomainName: win32more.Windows.Networking.Vpn.VpnDomainNameAssignment, mtuSize: UInt32, maxFrameSize: UInt32, Reserved: Boolean) -> Void: ...
    @winrt_commethod(8)
    def add_ActivityStateChange(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.Vpn.VpnChannel, win32more.Windows.Networking.Vpn.VpnChannelActivityStateChangedArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ActivityStateChange(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def GetVpnSendPacketBuffer(self) -> win32more.Windows.Networking.Vpn.VpnPacketBuffer: ...
    @winrt_commethod(11)
    def GetVpnReceivePacketBuffer(self) -> win32more.Windows.Networking.Vpn.VpnPacketBuffer: ...
    @winrt_commethod(12)
    def RequestCustomPromptAsync(self, customPromptElement: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.Vpn.IVpnCustomPromptElement]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def RequestCredentialsWithCertificateAsync(self, credType: win32more.Windows.Networking.Vpn.VpnCredentialType, credOptions: UInt32, certificate: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.Vpn.VpnCredential]: ...
    @winrt_commethod(14)
    def RequestCredentialsWithOptionsAsync(self, credType: win32more.Windows.Networking.Vpn.VpnCredentialType, credOptions: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.Vpn.VpnCredential]: ...
    @winrt_commethod(15)
    def RequestCredentialsSimpleAsync(self, credType: win32more.Windows.Networking.Vpn.VpnCredentialType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.Vpn.VpnCredential]: ...
    @winrt_commethod(16)
    def TerminateConnection(self, message: WinRT_String) -> Void: ...
    @winrt_commethod(17)
    def StartWithTrafficFilter(self, assignedClientIpv4List: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.HostName], assignedClientIpv6List: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.HostName], vpnInterfaceId: win32more.Windows.Networking.Vpn.VpnInterfaceId, assignedRoutes: win32more.Windows.Networking.Vpn.VpnRouteAssignment, assignedNamespace: win32more.Windows.Networking.Vpn.VpnDomainNameAssignment, mtuSize: UInt32, maxFrameSize: UInt32, reserved: Boolean, mainOuterTunnelTransport: win32more.Windows.Win32.System.WinRT.IInspectable, optionalOuterTunnelTransport: win32more.Windows.Win32.System.WinRT.IInspectable, assignedTrafficFilters: win32more.Windows.Networking.Vpn.VpnTrafficFilterAssignment) -> Void: ...
    ActivityStateChange = event()
class IVpnChannel4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnChannel4'
    _iid_ = Guid('{d7266ede-2937-419d-9570-486aebb81803}')
    @winrt_commethod(6)
    def AddAndAssociateTransport(self, transport: win32more.Windows.Win32.System.WinRT.IInspectable, context: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(7)
    def StartWithMultipleTransports(self, assignedClientIpv4Addresses: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Networking.HostName], assignedClientIpv6Addresses: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Networking.HostName], vpninterfaceId: win32more.Windows.Networking.Vpn.VpnInterfaceId, assignedRoutes: win32more.Windows.Networking.Vpn.VpnRouteAssignment, assignedNamespace: win32more.Windows.Networking.Vpn.VpnDomainNameAssignment, mtuSize: UInt32, maxFrameSize: UInt32, reserved: Boolean, transports: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Win32.System.WinRT.IInspectable], assignedTrafficFilters: win32more.Windows.Networking.Vpn.VpnTrafficFilterAssignment) -> Void: ...
    @winrt_commethod(8)
    def ReplaceAndAssociateTransport(self, transport: win32more.Windows.Win32.System.WinRT.IInspectable, context: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(9)
    def StartReconnectingTransport(self, transport: win32more.Windows.Win32.System.WinRT.IInspectable, context: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(10)
    def GetSlotTypeForTransportContext(self, context: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.Networking.Sockets.ControlChannelTriggerStatus: ...
    @winrt_commethod(11)
    def get_CurrentRequestTransportContext(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    CurrentRequestTransportContext = property(get_CurrentRequestTransportContext, None)
class IVpnChannel5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnChannel5'
    _iid_ = Guid('{de7a0992-8384-4fbc-882c-1fd23124cd3b}')
    @winrt_commethod(6)
    def AppendVpnReceivePacketBuffer(self, decapsulatedPacketBuffer: win32more.Windows.Networking.Vpn.VpnPacketBuffer) -> Void: ...
    @winrt_commethod(7)
    def AppendVpnSendPacketBuffer(self, encapsulatedPacketBuffer: win32more.Windows.Networking.Vpn.VpnPacketBuffer) -> Void: ...
    @winrt_commethod(8)
    def FlushVpnReceivePacketBuffers(self) -> Void: ...
    @winrt_commethod(9)
    def FlushVpnSendPacketBuffers(self) -> Void: ...
class IVpnChannel6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnChannel6'
    _iid_ = Guid('{55843696-bd63-49c5-abca-5da77885551a}')
    @winrt_commethod(6)
    def ActivateForeground(self, packageRelativeAppId: WinRT_String, sharedContext: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Foundation.Collections.ValueSet: ...
class IVpnChannelActivityEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnChannelActivityEventArgs'
    _iid_ = Guid('{a36c88f2-afdc-4775-855d-d4ac0a35fc55}')
    @winrt_commethod(6)
    def get_Type(self) -> win32more.Windows.Networking.Vpn.VpnChannelActivityEventType: ...
    Type = property(get_Type, None)
class IVpnChannelActivityStateChangedArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnChannelActivityStateChangedArgs'
    _iid_ = Guid('{3d750565-fdc0-4bbe-a23b-45fffc6d97a1}')
    @winrt_commethod(6)
    def get_ActivityState(self) -> win32more.Windows.Networking.Vpn.VpnChannelActivityEventType: ...
    ActivityState = property(get_ActivityState, None)
class IVpnChannelConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnChannelConfiguration'
    _iid_ = Guid('{0e2ddca2-2012-4fe4-b179-8c652c6d107e}')
    @winrt_commethod(6)
    def get_ServerServiceName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ServerHostNameList(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.HostName]: ...
    @winrt_commethod(8)
    def get_CustomField(self) -> WinRT_String: ...
    CustomField = property(get_CustomField, None)
    ServerHostNameList = property(get_ServerHostNameList, None)
    ServerServiceName = property(get_ServerServiceName, None)
class IVpnChannelConfiguration2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnChannelConfiguration2'
    _iid_ = Guid('{f30b574c-7824-471c-a118-63dbc93ae4c7}')
    @winrt_commethod(6)
    def get_ServerUris(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Uri]: ...
    ServerUris = property(get_ServerUris, None)
class IVpnChannelStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnChannelStatics'
    _iid_ = Guid('{88eb062d-e818-4ffd-98a6-363e3736c95d}')
    @winrt_commethod(6)
    def ProcessEventAsync(self, thirdPartyPlugIn: win32more.Windows.Win32.System.WinRT.IInspectable, event: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
class IVpnCredential(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnCredential'
    _iid_ = Guid('{b7e78af3-a46d-404b-8729-1832522853ac}')
    @winrt_commethod(6)
    def get_PasskeyCredential(self) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(7)
    def get_CertificateCredential(self) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_commethod(8)
    def get_AdditionalPin(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_OldPasswordCredential(self) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    AdditionalPin = property(get_AdditionalPin, None)
    CertificateCredential = property(get_CertificateCredential, None)
    OldPasswordCredential = property(get_OldPasswordCredential, None)
    PasskeyCredential = property(get_PasskeyCredential, None)
class IVpnCustomCheckBox(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnCustomCheckBox'
    _iid_ = Guid('{43878753-03c5-4e61-93d7-a957714c4282}')
    @winrt_commethod(6)
    def put_InitialCheckState(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_InitialCheckState(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_Checked(self) -> Boolean: ...
    Checked = property(get_Checked, None)
    InitialCheckState = property(get_InitialCheckState, put_InitialCheckState)
class IVpnCustomComboBox(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnCustomComboBox'
    _iid_ = Guid('{9a24158e-dba1-4c6f-8270-dcf3c9761c4c}')
    @winrt_commethod(6)
    def put_OptionsText(self, value: win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]) -> Void: ...
    @winrt_commethod(7)
    def get_OptionsText(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(8)
    def get_Selected(self) -> UInt32: ...
    OptionsText = property(get_OptionsText, put_OptionsText)
    Selected = property(get_Selected, None)
class IVpnCustomEditBox(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnCustomEditBox'
    _iid_ = Guid('{3002d9a0-cfbf-4c0b-8f3c-66f503c20b39}')
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnCustomErrorBox'
    _iid_ = Guid('{9ec4efb2-c942-42af-b223-588b48328721}')
class IVpnCustomPrompt(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnCustomPrompt'
    _iid_ = Guid('{9b2ebe7b-87d5-433c-b4f6-eee6aa68a244}')
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
    Bordered = property(get_Bordered, put_Bordered)
    Compulsory = property(get_Compulsory, put_Compulsory)
    Label = property(get_Label, put_Label)
class IVpnCustomPromptBooleanInput(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnCustomPromptBooleanInput'
    _iid_ = Guid('{c4c9a69e-ff47-4527-9f27-a49292019979}')
    @winrt_commethod(6)
    def put_InitialValue(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_InitialValue(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_Value(self) -> Boolean: ...
    InitialValue = property(get_InitialValue, put_InitialValue)
    Value = property(get_Value, None)
class IVpnCustomPromptElement(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnCustomPromptElement'
    _iid_ = Guid('{73bd5638-6f04-404d-93dd-50a44924a38b}')
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
    Compulsory = property(get_Compulsory, put_Compulsory)
    DisplayName = property(get_DisplayName, put_DisplayName)
    Emphasized = property(get_Emphasized, put_Emphasized)
class IVpnCustomPromptOptionSelector(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnCustomPromptOptionSelector'
    _iid_ = Guid('{3b8f34d9-8ec1-4e95-9a4e-7ba64d38f330}')
    @winrt_commethod(6)
    def get_Options(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(7)
    def get_SelectedIndex(self) -> UInt32: ...
    Options = property(get_Options, None)
    SelectedIndex = property(get_SelectedIndex, None)
class IVpnCustomPromptText(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnCustomPromptText'
    _iid_ = Guid('{3bc8bdee-3a42-49a3-abdd-07b2edea752d}')
    @winrt_commethod(6)
    def put_Text(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_Text(self) -> WinRT_String: ...
    Text = property(get_Text, put_Text)
class IVpnCustomPromptTextInput(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnCustomPromptTextInput'
    _iid_ = Guid('{c9da9c75-913c-47d5-88ba-48fc48930235}')
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
    IsTextHidden = property(get_IsTextHidden, put_IsTextHidden)
    PlaceholderText = property(get_PlaceholderText, put_PlaceholderText)
    Text = property(get_Text, None)
class IVpnCustomTextBox(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnCustomTextBox'
    _iid_ = Guid('{daa4c3ca-8f23-4d36-91f1-76d937827942}')
    @winrt_commethod(6)
    def put_DisplayText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_DisplayText(self) -> WinRT_String: ...
    DisplayText = property(get_DisplayText, put_DisplayText)
class IVpnDomainNameAssignment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnDomainNameAssignment'
    _iid_ = Guid('{4135b141-ccdb-49b5-9401-039a8ae767e9}')
    @winrt_commethod(6)
    def get_DomainNameList(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnDomainNameInfo]: ...
    @winrt_commethod(7)
    def put_ProxyAutoConfigurationUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def get_ProxyAutoConfigurationUri(self) -> win32more.Windows.Foundation.Uri: ...
    DomainNameList = property(get_DomainNameList, None)
    ProxyAutoConfigurationUri = property(get_ProxyAutoConfigurationUri, put_ProxyAutoConfigurationUri)
class IVpnDomainNameInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnDomainNameInfo'
    _iid_ = Guid('{ad2eb82f-ea8e-4f7a-843e-1a87e32e1b9a}')
    @winrt_commethod(6)
    def put_DomainName(self, value: win32more.Windows.Networking.HostName) -> Void: ...
    @winrt_commethod(7)
    def get_DomainName(self) -> win32more.Windows.Networking.HostName: ...
    @winrt_commethod(8)
    def put_DomainNameType(self, value: win32more.Windows.Networking.Vpn.VpnDomainNameType) -> Void: ...
    @winrt_commethod(9)
    def get_DomainNameType(self) -> win32more.Windows.Networking.Vpn.VpnDomainNameType: ...
    @winrt_commethod(10)
    def get_DnsServers(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.HostName]: ...
    @winrt_commethod(11)
    def get_WebProxyServers(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.HostName]: ...
    DnsServers = property(get_DnsServers, None)
    DomainName = property(get_DomainName, put_DomainName)
    DomainNameType = property(get_DomainNameType, put_DomainNameType)
    WebProxyServers = property(get_WebProxyServers, None)
class IVpnDomainNameInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnDomainNameInfo2'
    _iid_ = Guid('{ab871151-6c53-4828-9883-d886de104407}')
    @winrt_commethod(6)
    def get_WebProxyUris(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Foundation.Uri]: ...
    WebProxyUris = property(get_WebProxyUris, None)
class IVpnDomainNameInfoFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnDomainNameInfoFactory'
    _iid_ = Guid('{2507bb75-028f-4688-8d3a-c4531df37da8}')
    @winrt_commethod(6)
    def CreateVpnDomainNameInfo(self, name: WinRT_String, nameType: win32more.Windows.Networking.Vpn.VpnDomainNameType, dnsServerList: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Networking.HostName], proxyServerList: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Networking.HostName]) -> win32more.Windows.Networking.Vpn.VpnDomainNameInfo: ...
class IVpnForegroundActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnForegroundActivatedEventArgs'
    _iid_ = Guid('{85b465b0-cadb-4d70-ac92-543a24dc9ebc}')
    @winrt_commethod(6)
    def get_ProfileName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SharedContext(self) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_commethod(8)
    def get_ActivationOperation(self) -> win32more.Windows.Networking.Vpn.VpnForegroundActivationOperation: ...
    ActivationOperation = property(get_ActivationOperation, None)
    ProfileName = property(get_ProfileName, None)
    SharedContext = property(get_SharedContext, None)
class IVpnForegroundActivationOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnForegroundActivationOperation'
    _iid_ = Guid('{9e010d57-f17a-4bd5-9b6d-f984f1297d3c}')
    @winrt_commethod(6)
    def Complete(self, result: win32more.Windows.Foundation.Collections.ValueSet) -> Void: ...
class IVpnInterfaceId(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnInterfaceId'
    _iid_ = Guid('{9e2ddca2-1712-4ce4-b179-8c652c6d1011}')
    @winrt_commethod(6)
    def GetAddressInfo(self, id: ReceiveArray[Byte]) -> Void: ...
class IVpnInterfaceIdFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnInterfaceIdFactory'
    _iid_ = Guid('{9e2ddca2-1712-4ce4-b179-8c652c6d1000}')
    @winrt_commethod(6)
    def CreateVpnInterfaceId(self, address: PassArray[Byte]) -> win32more.Windows.Networking.Vpn.VpnInterfaceId: ...
class IVpnManagementAgent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnManagementAgent'
    _iid_ = Guid('{193696cd-a5c4-4abe-852b-785be4cb3e34}')
    @winrt_commethod(6)
    def AddProfileFromXmlAsync(self, xml: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_commethod(7)
    def AddProfileFromObjectAsync(self, profile: win32more.Windows.Networking.Vpn.IVpnProfile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_commethod(8)
    def UpdateProfileFromXmlAsync(self, xml: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_commethod(9)
    def UpdateProfileFromObjectAsync(self, profile: win32more.Windows.Networking.Vpn.IVpnProfile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_commethod(10)
    def GetProfilesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.Vpn.IVpnProfile]]: ...
    @winrt_commethod(11)
    def DeleteProfileAsync(self, profile: win32more.Windows.Networking.Vpn.IVpnProfile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_commethod(12)
    def ConnectProfileAsync(self, profile: win32more.Windows.Networking.Vpn.IVpnProfile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_commethod(13)
    def ConnectProfileWithPasswordCredentialAsync(self, profile: win32more.Windows.Networking.Vpn.IVpnProfile, passwordCredential: win32more.Windows.Security.Credentials.PasswordCredential) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_commethod(14)
    def DisconnectProfileAsync(self, profile: win32more.Windows.Networking.Vpn.IVpnProfile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
class IVpnNamespaceAssignment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnNamespaceAssignment'
    _iid_ = Guid('{d7f7db18-307d-4c0e-bd62-8fa270bbadd6}')
    @winrt_commethod(6)
    def put_NamespaceList(self, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnNamespaceInfo]) -> Void: ...
    @winrt_commethod(7)
    def get_NamespaceList(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnNamespaceInfo]: ...
    @winrt_commethod(8)
    def put_ProxyAutoConfigUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(9)
    def get_ProxyAutoConfigUri(self) -> win32more.Windows.Foundation.Uri: ...
    NamespaceList = property(get_NamespaceList, put_NamespaceList)
    ProxyAutoConfigUri = property(get_ProxyAutoConfigUri, put_ProxyAutoConfigUri)
class IVpnNamespaceInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnNamespaceInfo'
    _iid_ = Guid('{30edfb43-444f-44c5-8167-a35a91f1af94}')
    @winrt_commethod(6)
    def put_Namespace(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_Namespace(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_DnsServers(self, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.HostName]) -> Void: ...
    @winrt_commethod(9)
    def get_DnsServers(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.HostName]: ...
    @winrt_commethod(10)
    def put_WebProxyServers(self, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.HostName]) -> Void: ...
    @winrt_commethod(11)
    def get_WebProxyServers(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.HostName]: ...
    DnsServers = property(get_DnsServers, put_DnsServers)
    Namespace = property(get_Namespace, put_Namespace)
    WebProxyServers = property(get_WebProxyServers, put_WebProxyServers)
class IVpnNamespaceInfoFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnNamespaceInfoFactory'
    _iid_ = Guid('{cb3e951a-b0ce-442b-acbb-5f99b202c31c}')
    @winrt_commethod(6)
    def CreateVpnNamespaceInfo(self, name: WinRT_String, dnsServerList: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.HostName], proxyServerList: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.HostName]) -> win32more.Windows.Networking.Vpn.VpnNamespaceInfo: ...
class IVpnNativeProfile(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnNativeProfile'
    _iid_ = Guid('{a4aee29e-6417-4333-9842-f0a66db69802}')
    @winrt_commethod(6)
    def get_Servers(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(7)
    def get_RoutingPolicyType(self) -> win32more.Windows.Networking.Vpn.VpnRoutingPolicyType: ...
    @winrt_commethod(8)
    def put_RoutingPolicyType(self, value: win32more.Windows.Networking.Vpn.VpnRoutingPolicyType) -> Void: ...
    @winrt_commethod(9)
    def get_NativeProtocolType(self) -> win32more.Windows.Networking.Vpn.VpnNativeProtocolType: ...
    @winrt_commethod(10)
    def put_NativeProtocolType(self, value: win32more.Windows.Networking.Vpn.VpnNativeProtocolType) -> Void: ...
    @winrt_commethod(11)
    def get_UserAuthenticationMethod(self) -> win32more.Windows.Networking.Vpn.VpnAuthenticationMethod: ...
    @winrt_commethod(12)
    def put_UserAuthenticationMethod(self, value: win32more.Windows.Networking.Vpn.VpnAuthenticationMethod) -> Void: ...
    @winrt_commethod(13)
    def get_TunnelAuthenticationMethod(self) -> win32more.Windows.Networking.Vpn.VpnAuthenticationMethod: ...
    @winrt_commethod(14)
    def put_TunnelAuthenticationMethod(self, value: win32more.Windows.Networking.Vpn.VpnAuthenticationMethod) -> Void: ...
    @winrt_commethod(15)
    def get_EapConfiguration(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def put_EapConfiguration(self, value: WinRT_String) -> Void: ...
    EapConfiguration = property(get_EapConfiguration, put_EapConfiguration)
    NativeProtocolType = property(get_NativeProtocolType, put_NativeProtocolType)
    RoutingPolicyType = property(get_RoutingPolicyType, put_RoutingPolicyType)
    Servers = property(get_Servers, None)
    TunnelAuthenticationMethod = property(get_TunnelAuthenticationMethod, put_TunnelAuthenticationMethod)
    UserAuthenticationMethod = property(get_UserAuthenticationMethod, put_UserAuthenticationMethod)
class IVpnNativeProfile2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnNativeProfile2'
    _iid_ = Guid('{0fec2467-cdb5-4ac7-b5a3-0afb5ec47682}')
    @winrt_commethod(6)
    def get_RequireVpnClientAppUI(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_RequireVpnClientAppUI(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_ConnectionStatus(self) -> win32more.Windows.Networking.Vpn.VpnManagementConnectionStatus: ...
    ConnectionStatus = property(get_ConnectionStatus, None)
    RequireVpnClientAppUI = property(get_RequireVpnClientAppUI, put_RequireVpnClientAppUI)
class IVpnPacketBuffer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnPacketBuffer'
    _iid_ = Guid('{c2f891fc-4d5c-4a63-b70d-4e307eacce55}')
    @winrt_commethod(6)
    def get_Buffer(self) -> win32more.Windows.Storage.Streams.Buffer: ...
    @winrt_commethod(7)
    def put_Status(self, value: win32more.Windows.Networking.Vpn.VpnPacketBufferStatus) -> Void: ...
    @winrt_commethod(8)
    def get_Status(self) -> win32more.Windows.Networking.Vpn.VpnPacketBufferStatus: ...
    @winrt_commethod(9)
    def put_TransportAffinity(self, value: UInt32) -> Void: ...
    @winrt_commethod(10)
    def get_TransportAffinity(self) -> UInt32: ...
    Buffer = property(get_Buffer, None)
    Status = property(get_Status, put_Status)
    TransportAffinity = property(get_TransportAffinity, put_TransportAffinity)
class IVpnPacketBuffer2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnPacketBuffer2'
    _iid_ = Guid('{665e91f0-8805-4bf5-a619-2e84882e6b4f}')
    @winrt_commethod(6)
    def get_AppId(self) -> win32more.Windows.Networking.Vpn.VpnAppId: ...
    AppId = property(get_AppId, None)
class IVpnPacketBuffer3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnPacketBuffer3'
    _iid_ = Guid('{e256072f-107b-4c40-b127-5bc53e0ad960}')
    @winrt_commethod(6)
    def put_TransportContext(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(7)
    def get_TransportContext(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    TransportContext = property(get_TransportContext, put_TransportContext)
class IVpnPacketBufferFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnPacketBufferFactory'
    _iid_ = Guid('{9e2ddca2-1712-4ce4-b179-8c652c6d9999}')
    @winrt_commethod(6)
    def CreateVpnPacketBuffer(self, parentBuffer: win32more.Windows.Networking.Vpn.VpnPacketBuffer, offset: UInt32, length: UInt32) -> win32more.Windows.Networking.Vpn.VpnPacketBuffer: ...
class IVpnPacketBufferList(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[IterableProtocol[win32more.Windows.Networking.Vpn.VpnPacketBuffer]]
    _classid_ = 'Windows.Networking.Vpn.IVpnPacketBufferList'
    _iid_ = Guid('{c2f891fc-4d5c-4a63-b70d-4e307eacce77}')
    @winrt_commethod(6)
    def Append(self, nextVpnPacketBuffer: win32more.Windows.Networking.Vpn.VpnPacketBuffer) -> Void: ...
    @winrt_commethod(7)
    def AddAtBegin(self, nextVpnPacketBuffer: win32more.Windows.Networking.Vpn.VpnPacketBuffer) -> Void: ...
    @winrt_commethod(8)
    def RemoveAtEnd(self) -> win32more.Windows.Networking.Vpn.VpnPacketBuffer: ...
    @winrt_commethod(9)
    def RemoveAtBegin(self) -> win32more.Windows.Networking.Vpn.VpnPacketBuffer: ...
    @winrt_commethod(10)
    def Clear(self) -> Void: ...
    @winrt_commethod(11)
    def put_Status(self, value: win32more.Windows.Networking.Vpn.VpnPacketBufferStatus) -> Void: ...
    @winrt_commethod(12)
    def get_Status(self) -> win32more.Windows.Networking.Vpn.VpnPacketBufferStatus: ...
    @winrt_commethod(13)
    def get_Size(self) -> UInt32: ...
    Size = property(get_Size, None)
    Status = property(get_Status, put_Status)
class IVpnPacketBufferList2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[IterableProtocol[win32more.Windows.Networking.Vpn.VpnPacketBuffer]]
    _classid_ = 'Windows.Networking.Vpn.IVpnPacketBufferList2'
    _iid_ = Guid('{3e7acfe5-ea1e-482a-8d98-c065f57d89ea}')
    @winrt_commethod(6)
    def AddLeadingPacket(self, nextVpnPacketBuffer: win32more.Windows.Networking.Vpn.VpnPacketBuffer) -> Void: ...
    @winrt_commethod(7)
    def RemoveLeadingPacket(self) -> win32more.Windows.Networking.Vpn.VpnPacketBuffer: ...
    @winrt_commethod(8)
    def AddTrailingPacket(self, nextVpnPacketBuffer: win32more.Windows.Networking.Vpn.VpnPacketBuffer) -> Void: ...
    @winrt_commethod(9)
    def RemoveTrailingPacket(self) -> win32more.Windows.Networking.Vpn.VpnPacketBuffer: ...
class IVpnPickedCredential(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnPickedCredential'
    _iid_ = Guid('{9a793ac7-8854-4e52-ad97-24dd9a842bce}')
    @winrt_commethod(6)
    def get_PasskeyCredential(self) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(7)
    def get_AdditionalPin(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_OldPasswordCredential(self) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    AdditionalPin = property(get_AdditionalPin, None)
    OldPasswordCredential = property(get_OldPasswordCredential, None)
    PasskeyCredential = property(get_PasskeyCredential, None)
class IVpnPlugIn(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnPlugIn'
    _iid_ = Guid('{ceb78d07-d0a8-4703-a091-c8c2c0915bc4}')
    @winrt_commethod(6)
    def Connect(self, channel: win32more.Windows.Networking.Vpn.VpnChannel) -> Void: ...
    @winrt_commethod(7)
    def Disconnect(self, channel: win32more.Windows.Networking.Vpn.VpnChannel) -> Void: ...
    @winrt_commethod(8)
    def GetKeepAlivePayload(self, channel: win32more.Windows.Networking.Vpn.VpnChannel, keepAlivePacket: POINTER(win32more.Windows.Networking.Vpn.VpnPacketBuffer)) -> Void: ...
    @winrt_commethod(9)
    def Encapsulate(self, channel: win32more.Windows.Networking.Vpn.VpnChannel, packets: win32more.Windows.Networking.Vpn.VpnPacketBufferList, encapulatedPackets: win32more.Windows.Networking.Vpn.VpnPacketBufferList) -> Void: ...
    @winrt_commethod(10)
    def Decapsulate(self, channel: win32more.Windows.Networking.Vpn.VpnChannel, encapBuffer: win32more.Windows.Networking.Vpn.VpnPacketBuffer, decapsulatedPackets: win32more.Windows.Networking.Vpn.VpnPacketBufferList, controlPacketsToSend: win32more.Windows.Networking.Vpn.VpnPacketBufferList) -> Void: ...
class IVpnPlugInProfile(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnPlugInProfile'
    _iid_ = Guid('{0edf0da4-4f00-4589-8d7b-4bf988f6542c}')
    @winrt_commethod(6)
    def get_ServerUris(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Foundation.Uri]: ...
    @winrt_commethod(7)
    def get_CustomConfiguration(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_CustomConfiguration(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_VpnPluginPackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def put_VpnPluginPackageFamilyName(self, value: WinRT_String) -> Void: ...
    CustomConfiguration = property(get_CustomConfiguration, put_CustomConfiguration)
    ServerUris = property(get_ServerUris, None)
    VpnPluginPackageFamilyName = property(get_VpnPluginPackageFamilyName, put_VpnPluginPackageFamilyName)
class IVpnPlugInProfile2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnPlugInProfile2'
    _iid_ = Guid('{611c4892-cf94-4ad6-ba99-00f4ff34565e}')
    @winrt_commethod(6)
    def get_RequireVpnClientAppUI(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_RequireVpnClientAppUI(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_ConnectionStatus(self) -> win32more.Windows.Networking.Vpn.VpnManagementConnectionStatus: ...
    ConnectionStatus = property(get_ConnectionStatus, None)
    RequireVpnClientAppUI = property(get_RequireVpnClientAppUI, put_RequireVpnClientAppUI)
class IVpnPlugInReconnectTransport(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnPlugInReconnectTransport'
    _iid_ = Guid('{9d5a1092-bb46-4d34-9d88-f217893076f4}')
    @winrt_commethod(6)
    def ReconnectTransport(self, channel: win32more.Windows.Networking.Vpn.VpnChannel, context: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
class IVpnProfile(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnProfile'
    _iid_ = Guid('{7875b751-b0d7-43db-8a93-d3fe2479e56a}')
    @winrt_commethod(6)
    def get_ProfileName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_ProfileName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_AppTriggers(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnAppId]: ...
    @winrt_commethod(9)
    def get_Routes(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnRoute]: ...
    @winrt_commethod(10)
    def get_DomainNameInfoList(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnDomainNameInfo]: ...
    @winrt_commethod(11)
    def get_TrafficFilters(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnTrafficFilter]: ...
    @winrt_commethod(12)
    def get_RememberCredentials(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_RememberCredentials(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_AlwaysOn(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_AlwaysOn(self, value: Boolean) -> Void: ...
    AlwaysOn = property(get_AlwaysOn, put_AlwaysOn)
    AppTriggers = property(get_AppTriggers, None)
    DomainNameInfoList = property(get_DomainNameInfoList, None)
    ProfileName = property(get_ProfileName, put_ProfileName)
    RememberCredentials = property(get_RememberCredentials, put_RememberCredentials)
    Routes = property(get_Routes, None)
    TrafficFilters = property(get_TrafficFilters, None)
class IVpnRoute(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnRoute'
    _iid_ = Guid('{b5731b83-0969-4699-938e-7776db29cfb3}')
    @winrt_commethod(6)
    def put_Address(self, value: win32more.Windows.Networking.HostName) -> Void: ...
    @winrt_commethod(7)
    def get_Address(self) -> win32more.Windows.Networking.HostName: ...
    @winrt_commethod(8)
    def put_PrefixSize(self, value: Byte) -> Void: ...
    @winrt_commethod(9)
    def get_PrefixSize(self) -> Byte: ...
    Address = property(get_Address, put_Address)
    PrefixSize = property(get_PrefixSize, put_PrefixSize)
class IVpnRouteAssignment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnRouteAssignment'
    _iid_ = Guid('{db64de22-ce39-4a76-9550-f61039f80e48}')
    @winrt_commethod(6)
    def put_Ipv4InclusionRoutes(self, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnRoute]) -> Void: ...
    @winrt_commethod(7)
    def put_Ipv6InclusionRoutes(self, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnRoute]) -> Void: ...
    @winrt_commethod(8)
    def get_Ipv4InclusionRoutes(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnRoute]: ...
    @winrt_commethod(9)
    def get_Ipv6InclusionRoutes(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnRoute]: ...
    @winrt_commethod(10)
    def put_Ipv4ExclusionRoutes(self, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnRoute]) -> Void: ...
    @winrt_commethod(11)
    def put_Ipv6ExclusionRoutes(self, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnRoute]) -> Void: ...
    @winrt_commethod(12)
    def get_Ipv4ExclusionRoutes(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnRoute]: ...
    @winrt_commethod(13)
    def get_Ipv6ExclusionRoutes(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnRoute]: ...
    @winrt_commethod(14)
    def put_ExcludeLocalSubnets(self, value: Boolean) -> Void: ...
    @winrt_commethod(15)
    def get_ExcludeLocalSubnets(self) -> Boolean: ...
    ExcludeLocalSubnets = property(get_ExcludeLocalSubnets, put_ExcludeLocalSubnets)
    Ipv4ExclusionRoutes = property(get_Ipv4ExclusionRoutes, put_Ipv4ExclusionRoutes)
    Ipv4InclusionRoutes = property(get_Ipv4InclusionRoutes, put_Ipv4InclusionRoutes)
    Ipv6ExclusionRoutes = property(get_Ipv6ExclusionRoutes, put_Ipv6ExclusionRoutes)
    Ipv6InclusionRoutes = property(get_Ipv6InclusionRoutes, put_Ipv6InclusionRoutes)
class IVpnRouteFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnRouteFactory'
    _iid_ = Guid('{bdeab5ff-45cf-4b99-83fb-db3bc2672b02}')
    @winrt_commethod(6)
    def CreateVpnRoute(self, address: win32more.Windows.Networking.HostName, prefixSize: Byte) -> win32more.Windows.Networking.Vpn.VpnRoute: ...
class IVpnSystemHealth(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnSystemHealth'
    _iid_ = Guid('{99a8f8af-c0ee-4e75-817a-f231aee5123d}')
    @winrt_commethod(6)
    def get_StatementOfHealth(self) -> win32more.Windows.Storage.Streams.Buffer: ...
    StatementOfHealth = property(get_StatementOfHealth, None)
class IVpnTrafficFilter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnTrafficFilter'
    _iid_ = Guid('{2f691b60-6c9f-47f5-ac36-bb1b042e2c50}')
    @winrt_commethod(6)
    def get_AppId(self) -> win32more.Windows.Networking.Vpn.VpnAppId: ...
    @winrt_commethod(7)
    def put_AppId(self, value: win32more.Windows.Networking.Vpn.VpnAppId) -> Void: ...
    @winrt_commethod(8)
    def get_AppClaims(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(9)
    def get_Protocol(self) -> win32more.Windows.Networking.Vpn.VpnIPProtocol: ...
    @winrt_commethod(10)
    def put_Protocol(self, value: win32more.Windows.Networking.Vpn.VpnIPProtocol) -> Void: ...
    @winrt_commethod(11)
    def get_LocalPortRanges(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(12)
    def get_RemotePortRanges(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(13)
    def get_LocalAddressRanges(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(14)
    def get_RemoteAddressRanges(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(15)
    def get_RoutingPolicyType(self) -> win32more.Windows.Networking.Vpn.VpnRoutingPolicyType: ...
    @winrt_commethod(16)
    def put_RoutingPolicyType(self, value: win32more.Windows.Networking.Vpn.VpnRoutingPolicyType) -> Void: ...
    AppClaims = property(get_AppClaims, None)
    AppId = property(get_AppId, put_AppId)
    LocalAddressRanges = property(get_LocalAddressRanges, None)
    LocalPortRanges = property(get_LocalPortRanges, None)
    Protocol = property(get_Protocol, put_Protocol)
    RemoteAddressRanges = property(get_RemoteAddressRanges, None)
    RemotePortRanges = property(get_RemotePortRanges, None)
    RoutingPolicyType = property(get_RoutingPolicyType, put_RoutingPolicyType)
class IVpnTrafficFilterAssignment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnTrafficFilterAssignment'
    _iid_ = Guid('{56ccd45c-e664-471e-89cd-601603b9e0f3}')
    @winrt_commethod(6)
    def get_TrafficFilterList(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnTrafficFilter]: ...
    @winrt_commethod(7)
    def get_AllowOutbound(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_AllowOutbound(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_AllowInbound(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_AllowInbound(self, value: Boolean) -> Void: ...
    AllowInbound = property(get_AllowInbound, put_AllowInbound)
    AllowOutbound = property(get_AllowOutbound, put_AllowOutbound)
    TrafficFilterList = property(get_TrafficFilterList, None)
class IVpnTrafficFilterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Networking.Vpn.IVpnTrafficFilterFactory'
    _iid_ = Guid('{480d41d5-7f99-474c-86ee-96df168318f1}')
    @winrt_commethod(6)
    def Create(self, appId: win32more.Windows.Networking.Vpn.VpnAppId) -> win32more.Windows.Networking.Vpn.VpnTrafficFilter: ...
class VpnAppId(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnAppId
    _classid_ = 'Windows.Networking.Vpn.VpnAppId'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Networking.Vpn.VpnAppId.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Networking.Vpn.IVpnAppIdFactory, type: win32more.Windows.Networking.Vpn.VpnAppIdType, value: WinRT_String) -> win32more.Windows.Networking.Vpn.VpnAppId: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Networking.Vpn.IVpnAppId) -> win32more.Windows.Networking.Vpn.VpnAppIdType: ...
    @winrt_mixinmethod
    def put_Type(self: win32more.Windows.Networking.Vpn.IVpnAppId, value: win32more.Windows.Networking.Vpn.VpnAppIdType) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Networking.Vpn.IVpnAppId) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Windows.Networking.Vpn.IVpnAppId, value: WinRT_String) -> Void: ...
    Type = property(get_Type, put_Type)
    Value = property(get_Value, put_Value)
class VpnAppIdType(Enum, Int32):
    PackageFamilyName = 0
    FullyQualifiedBinaryName = 1
    FilePath = 2
class VpnAuthenticationMethod(Enum, Int32):
    Mschapv2 = 0
    Eap = 1
    Certificate = 2
    PresharedKey = 3
class VpnChannel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnChannel
    _classid_ = 'Windows.Networking.Vpn.VpnChannel'
    @winrt_mixinmethod
    def AssociateTransport(self: win32more.Windows.Networking.Vpn.IVpnChannel, mainOuterTunnelTransport: win32more.Windows.Win32.System.WinRT.IInspectable, optionalOuterTunnelTransport: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Networking.Vpn.IVpnChannel, assignedClientIPv4list: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.HostName], assignedClientIPv6list: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.HostName], vpnInterfaceId: win32more.Windows.Networking.Vpn.VpnInterfaceId, routeScope: win32more.Windows.Networking.Vpn.VpnRouteAssignment, namespaceScope: win32more.Windows.Networking.Vpn.VpnNamespaceAssignment, mtuSize: UInt32, maxFrameSize: UInt32, optimizeForLowCostNetwork: Boolean, mainOuterTunnelTransport: win32more.Windows.Win32.System.WinRT.IInspectable, optionalOuterTunnelTransport: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Networking.Vpn.IVpnChannel) -> Void: ...
    @winrt_mixinmethod
    def RequestCredentials(self: win32more.Windows.Networking.Vpn.IVpnChannel, credType: win32more.Windows.Networking.Vpn.VpnCredentialType, isRetry: Boolean, isSingleSignOnCredential: Boolean, certificate: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> win32more.Windows.Networking.Vpn.VpnPickedCredential: ...
    @winrt_mixinmethod
    def RequestVpnPacketBuffer(self: win32more.Windows.Networking.Vpn.IVpnChannel, type: win32more.Windows.Networking.Vpn.VpnDataPathType, vpnPacketBuffer: POINTER(win32more.Windows.Networking.Vpn.VpnPacketBuffer)) -> Void: ...
    @winrt_mixinmethod
    def LogDiagnosticMessage(self: win32more.Windows.Networking.Vpn.IVpnChannel, message: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Networking.Vpn.IVpnChannel) -> UInt32: ...
    @winrt_mixinmethod
    def get_Configuration(self: win32more.Windows.Networking.Vpn.IVpnChannel) -> win32more.Windows.Networking.Vpn.VpnChannelConfiguration: ...
    @winrt_mixinmethod
    def add_ActivityChange(self: win32more.Windows.Networking.Vpn.IVpnChannel, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.Vpn.VpnChannel, win32more.Windows.Networking.Vpn.VpnChannelActivityEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ActivityChange(self: win32more.Windows.Networking.Vpn.IVpnChannel, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def put_PlugInContext(self: win32more.Windows.Networking.Vpn.IVpnChannel, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_PlugInContext(self: win32more.Windows.Networking.Vpn.IVpnChannel) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_SystemHealth(self: win32more.Windows.Networking.Vpn.IVpnChannel) -> win32more.Windows.Networking.Vpn.VpnSystemHealth: ...
    @winrt_mixinmethod
    def RequestCustomPrompt(self: win32more.Windows.Networking.Vpn.IVpnChannel, customPrompt: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.Vpn.IVpnCustomPrompt]) -> Void: ...
    @winrt_mixinmethod
    def SetErrorMessage(self: win32more.Windows.Networking.Vpn.IVpnChannel, message: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def SetAllowedSslTlsVersions(self: win32more.Windows.Networking.Vpn.IVpnChannel, tunnelTransport: win32more.Windows.Win32.System.WinRT.IInspectable, useTls12: Boolean) -> Void: ...
    @winrt_mixinmethod
    def StartWithMainTransport(self: win32more.Windows.Networking.Vpn.IVpnChannel2, assignedClientIPv4list: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.HostName], assignedClientIPv6list: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.HostName], vpnInterfaceId: win32more.Windows.Networking.Vpn.VpnInterfaceId, assignedRoutes: win32more.Windows.Networking.Vpn.VpnRouteAssignment, assignedDomainName: win32more.Windows.Networking.Vpn.VpnDomainNameAssignment, mtuSize: UInt32, maxFrameSize: UInt32, Reserved: Boolean, mainOuterTunnelTransport: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def StartExistingTransports(self: win32more.Windows.Networking.Vpn.IVpnChannel2, assignedClientIPv4list: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.HostName], assignedClientIPv6list: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.HostName], vpnInterfaceId: win32more.Windows.Networking.Vpn.VpnInterfaceId, assignedRoutes: win32more.Windows.Networking.Vpn.VpnRouteAssignment, assignedDomainName: win32more.Windows.Networking.Vpn.VpnDomainNameAssignment, mtuSize: UInt32, maxFrameSize: UInt32, Reserved: Boolean) -> Void: ...
    @winrt_mixinmethod
    def add_ActivityStateChange(self: win32more.Windows.Networking.Vpn.IVpnChannel2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Networking.Vpn.VpnChannel, win32more.Windows.Networking.Vpn.VpnChannelActivityStateChangedArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ActivityStateChange(self: win32more.Windows.Networking.Vpn.IVpnChannel2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetVpnSendPacketBuffer(self: win32more.Windows.Networking.Vpn.IVpnChannel2) -> win32more.Windows.Networking.Vpn.VpnPacketBuffer: ...
    @winrt_mixinmethod
    def GetVpnReceivePacketBuffer(self: win32more.Windows.Networking.Vpn.IVpnChannel2) -> win32more.Windows.Networking.Vpn.VpnPacketBuffer: ...
    @winrt_mixinmethod
    def RequestCustomPromptAsync(self: win32more.Windows.Networking.Vpn.IVpnChannel2, customPromptElement: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.Vpn.IVpnCustomPromptElement]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RequestCredentialsWithCertificateAsync(self: win32more.Windows.Networking.Vpn.IVpnChannel2, credType: win32more.Windows.Networking.Vpn.VpnCredentialType, credOptions: UInt32, certificate: win32more.Windows.Security.Cryptography.Certificates.Certificate) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.Vpn.VpnCredential]: ...
    @winrt_mixinmethod
    def RequestCredentialsWithOptionsAsync(self: win32more.Windows.Networking.Vpn.IVpnChannel2, credType: win32more.Windows.Networking.Vpn.VpnCredentialType, credOptions: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.Vpn.VpnCredential]: ...
    @winrt_mixinmethod
    def RequestCredentialsSimpleAsync(self: win32more.Windows.Networking.Vpn.IVpnChannel2, credType: win32more.Windows.Networking.Vpn.VpnCredentialType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.Vpn.VpnCredential]: ...
    @winrt_mixinmethod
    def TerminateConnection(self: win32more.Windows.Networking.Vpn.IVpnChannel2, message: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def StartWithTrafficFilter(self: win32more.Windows.Networking.Vpn.IVpnChannel2, assignedClientIpv4List: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.HostName], assignedClientIpv6List: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.HostName], vpnInterfaceId: win32more.Windows.Networking.Vpn.VpnInterfaceId, assignedRoutes: win32more.Windows.Networking.Vpn.VpnRouteAssignment, assignedNamespace: win32more.Windows.Networking.Vpn.VpnDomainNameAssignment, mtuSize: UInt32, maxFrameSize: UInt32, reserved: Boolean, mainOuterTunnelTransport: win32more.Windows.Win32.System.WinRT.IInspectable, optionalOuterTunnelTransport: win32more.Windows.Win32.System.WinRT.IInspectable, assignedTrafficFilters: win32more.Windows.Networking.Vpn.VpnTrafficFilterAssignment) -> Void: ...
    @winrt_mixinmethod
    def AddAndAssociateTransport(self: win32more.Windows.Networking.Vpn.IVpnChannel4, transport: win32more.Windows.Win32.System.WinRT.IInspectable, context: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def StartWithMultipleTransports(self: win32more.Windows.Networking.Vpn.IVpnChannel4, assignedClientIpv4Addresses: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Networking.HostName], assignedClientIpv6Addresses: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Networking.HostName], vpninterfaceId: win32more.Windows.Networking.Vpn.VpnInterfaceId, assignedRoutes: win32more.Windows.Networking.Vpn.VpnRouteAssignment, assignedNamespace: win32more.Windows.Networking.Vpn.VpnDomainNameAssignment, mtuSize: UInt32, maxFrameSize: UInt32, reserved: Boolean, transports: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Win32.System.WinRT.IInspectable], assignedTrafficFilters: win32more.Windows.Networking.Vpn.VpnTrafficFilterAssignment) -> Void: ...
    @winrt_mixinmethod
    def ReplaceAndAssociateTransport(self: win32more.Windows.Networking.Vpn.IVpnChannel4, transport: win32more.Windows.Win32.System.WinRT.IInspectable, context: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def StartReconnectingTransport(self: win32more.Windows.Networking.Vpn.IVpnChannel4, transport: win32more.Windows.Win32.System.WinRT.IInspectable, context: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def GetSlotTypeForTransportContext(self: win32more.Windows.Networking.Vpn.IVpnChannel4, context: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.Networking.Sockets.ControlChannelTriggerStatus: ...
    @winrt_mixinmethod
    def get_CurrentRequestTransportContext(self: win32more.Windows.Networking.Vpn.IVpnChannel4) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def AppendVpnReceivePacketBuffer(self: win32more.Windows.Networking.Vpn.IVpnChannel5, decapsulatedPacketBuffer: win32more.Windows.Networking.Vpn.VpnPacketBuffer) -> Void: ...
    @winrt_mixinmethod
    def AppendVpnSendPacketBuffer(self: win32more.Windows.Networking.Vpn.IVpnChannel5, encapsulatedPacketBuffer: win32more.Windows.Networking.Vpn.VpnPacketBuffer) -> Void: ...
    @winrt_mixinmethod
    def FlushVpnReceivePacketBuffers(self: win32more.Windows.Networking.Vpn.IVpnChannel5) -> Void: ...
    @winrt_mixinmethod
    def FlushVpnSendPacketBuffers(self: win32more.Windows.Networking.Vpn.IVpnChannel5) -> Void: ...
    @winrt_mixinmethod
    def ActivateForeground(self: win32more.Windows.Networking.Vpn.IVpnChannel6, packageRelativeAppId: WinRT_String, sharedContext: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_classmethod
    def ProcessEventAsync(cls: win32more.Windows.Networking.Vpn.IVpnChannelStatics, thirdPartyPlugIn: win32more.Windows.Win32.System.WinRT.IInspectable, event: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    Configuration = property(get_Configuration, None)
    CurrentRequestTransportContext = property(get_CurrentRequestTransportContext, None)
    Id = property(get_Id, None)
    PlugInContext = property(get_PlugInContext, put_PlugInContext)
    SystemHealth = property(get_SystemHealth, None)
    ActivityChange = event()
    ActivityStateChange = event()
class VpnChannelActivityEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnChannelActivityEventArgs
    _classid_ = 'Windows.Networking.Vpn.VpnChannelActivityEventArgs'
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Networking.Vpn.IVpnChannelActivityEventArgs) -> win32more.Windows.Networking.Vpn.VpnChannelActivityEventType: ...
    Type = property(get_Type, None)
class VpnChannelActivityEventType(Enum, Int32):
    Idle = 0
    Active = 1
class VpnChannelActivityStateChangedArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnChannelActivityStateChangedArgs
    _classid_ = 'Windows.Networking.Vpn.VpnChannelActivityStateChangedArgs'
    @winrt_mixinmethod
    def get_ActivityState(self: win32more.Windows.Networking.Vpn.IVpnChannelActivityStateChangedArgs) -> win32more.Windows.Networking.Vpn.VpnChannelActivityEventType: ...
    ActivityState = property(get_ActivityState, None)
class VpnChannelConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnChannelConfiguration
    _classid_ = 'Windows.Networking.Vpn.VpnChannelConfiguration'
    @winrt_mixinmethod
    def get_ServerServiceName(self: win32more.Windows.Networking.Vpn.IVpnChannelConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServerHostNameList(self: win32more.Windows.Networking.Vpn.IVpnChannelConfiguration) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.HostName]: ...
    @winrt_mixinmethod
    def get_CustomField(self: win32more.Windows.Networking.Vpn.IVpnChannelConfiguration) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServerUris(self: win32more.Windows.Networking.Vpn.IVpnChannelConfiguration2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Uri]: ...
    CustomField = property(get_CustomField, None)
    ServerHostNameList = property(get_ServerHostNameList, None)
    ServerServiceName = property(get_ServerServiceName, None)
    ServerUris = property(get_ServerUris, None)
class VpnChannelRequestCredentialsOptions(Enum, UInt32):
    None_ = 0
    Retrying = 1
    UseForSingleSignIn = 2
class VpnCredential(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnCredential
    _classid_ = 'Windows.Networking.Vpn.VpnCredential'
    @winrt_mixinmethod
    def get_PasskeyCredential(self: win32more.Windows.Networking.Vpn.IVpnCredential) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def get_CertificateCredential(self: win32more.Windows.Networking.Vpn.IVpnCredential) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def get_AdditionalPin(self: win32more.Windows.Networking.Vpn.IVpnCredential) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OldPasswordCredential(self: win32more.Windows.Networking.Vpn.IVpnCredential) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    AdditionalPin = property(get_AdditionalPin, None)
    CertificateCredential = property(get_CertificateCredential, None)
    OldPasswordCredential = property(get_OldPasswordCredential, None)
    PasskeyCredential = property(get_PasskeyCredential, None)
class VpnCredentialType(Enum, Int32):
    UsernamePassword = 0
    UsernameOtpPin = 1
    UsernamePasswordAndPin = 2
    UsernamePasswordChange = 3
    SmartCard = 4
    ProtectedCertificate = 5
    UnProtectedCertificate = 6
class VpnCustomCheckBox(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnCustomCheckBox
    _classid_ = 'Windows.Networking.Vpn.VpnCustomCheckBox'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Networking.Vpn.VpnCustomCheckBox.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.Vpn.VpnCustomCheckBox: ...
    @winrt_mixinmethod
    def put_InitialCheckState(self: win32more.Windows.Networking.Vpn.IVpnCustomCheckBox, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_InitialCheckState(self: win32more.Windows.Networking.Vpn.IVpnCustomCheckBox) -> Boolean: ...
    @winrt_mixinmethod
    def get_Checked(self: win32more.Windows.Networking.Vpn.IVpnCustomCheckBox) -> Boolean: ...
    @winrt_mixinmethod
    def put_Label(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Label(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Compulsory(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Compulsory(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt) -> Boolean: ...
    @winrt_mixinmethod
    def put_Bordered(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Bordered(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt) -> Boolean: ...
    Bordered = property(get_Bordered, put_Bordered)
    Checked = property(get_Checked, None)
    Compulsory = property(get_Compulsory, put_Compulsory)
    InitialCheckState = property(get_InitialCheckState, put_InitialCheckState)
    Label = property(get_Label, put_Label)
class VpnCustomComboBox(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnCustomComboBox
    _classid_ = 'Windows.Networking.Vpn.VpnCustomComboBox'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Networking.Vpn.VpnCustomComboBox.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.Vpn.VpnCustomComboBox: ...
    @winrt_mixinmethod
    def put_OptionsText(self: win32more.Windows.Networking.Vpn.IVpnCustomComboBox, value: win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]) -> Void: ...
    @winrt_mixinmethod
    def get_OptionsText(self: win32more.Windows.Networking.Vpn.IVpnCustomComboBox) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Selected(self: win32more.Windows.Networking.Vpn.IVpnCustomComboBox) -> UInt32: ...
    @winrt_mixinmethod
    def put_Label(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Label(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Compulsory(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Compulsory(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt) -> Boolean: ...
    @winrt_mixinmethod
    def put_Bordered(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Bordered(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt) -> Boolean: ...
    Bordered = property(get_Bordered, put_Bordered)
    Compulsory = property(get_Compulsory, put_Compulsory)
    Label = property(get_Label, put_Label)
    OptionsText = property(get_OptionsText, put_OptionsText)
    Selected = property(get_Selected, None)
class VpnCustomEditBox(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnCustomEditBox
    _classid_ = 'Windows.Networking.Vpn.VpnCustomEditBox'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Networking.Vpn.VpnCustomEditBox.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.Vpn.VpnCustomEditBox: ...
    @winrt_mixinmethod
    def put_DefaultText(self: win32more.Windows.Networking.Vpn.IVpnCustomEditBox, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DefaultText(self: win32more.Windows.Networking.Vpn.IVpnCustomEditBox) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_NoEcho(self: win32more.Windows.Networking.Vpn.IVpnCustomEditBox, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_NoEcho(self: win32more.Windows.Networking.Vpn.IVpnCustomEditBox) -> Boolean: ...
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.Networking.Vpn.IVpnCustomEditBox) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Label(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Label(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Compulsory(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Compulsory(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt) -> Boolean: ...
    @winrt_mixinmethod
    def put_Bordered(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Bordered(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt) -> Boolean: ...
    Bordered = property(get_Bordered, put_Bordered)
    Compulsory = property(get_Compulsory, put_Compulsory)
    DefaultText = property(get_DefaultText, put_DefaultText)
    Label = property(get_Label, put_Label)
    NoEcho = property(get_NoEcho, put_NoEcho)
    Text = property(get_Text, None)
class VpnCustomErrorBox(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnCustomErrorBox
    _classid_ = 'Windows.Networking.Vpn.VpnCustomErrorBox'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Networking.Vpn.VpnCustomErrorBox.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.Vpn.VpnCustomErrorBox: ...
    @winrt_mixinmethod
    def put_Label(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Label(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Compulsory(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Compulsory(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt) -> Boolean: ...
    @winrt_mixinmethod
    def put_Bordered(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Bordered(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt) -> Boolean: ...
    Bordered = property(get_Bordered, put_Bordered)
    Compulsory = property(get_Compulsory, put_Compulsory)
    Label = property(get_Label, put_Label)
class VpnCustomPromptBooleanInput(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnCustomPromptBooleanInput
    _classid_ = 'Windows.Networking.Vpn.VpnCustomPromptBooleanInput'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Networking.Vpn.VpnCustomPromptBooleanInput.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.Vpn.VpnCustomPromptBooleanInput: ...
    @winrt_mixinmethod
    def put_InitialValue(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptBooleanInput, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_InitialValue(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptBooleanInput) -> Boolean: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptBooleanInput) -> Boolean: ...
    @winrt_mixinmethod
    def put_DisplayName(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptElement, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptElement) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Compulsory(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Compulsory(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptElement) -> Boolean: ...
    @winrt_mixinmethod
    def put_Emphasized(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Emphasized(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptElement) -> Boolean: ...
    Compulsory = property(get_Compulsory, put_Compulsory)
    DisplayName = property(get_DisplayName, put_DisplayName)
    Emphasized = property(get_Emphasized, put_Emphasized)
    InitialValue = property(get_InitialValue, put_InitialValue)
    Value = property(get_Value, None)
class VpnCustomPromptOptionSelector(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnCustomPromptOptionSelector
    _classid_ = 'Windows.Networking.Vpn.VpnCustomPromptOptionSelector'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Networking.Vpn.VpnCustomPromptOptionSelector.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.Vpn.VpnCustomPromptOptionSelector: ...
    @winrt_mixinmethod
    def get_Options(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptOptionSelector) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_SelectedIndex(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptOptionSelector) -> UInt32: ...
    @winrt_mixinmethod
    def put_DisplayName(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptElement, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptElement) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Compulsory(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Compulsory(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptElement) -> Boolean: ...
    @winrt_mixinmethod
    def put_Emphasized(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Emphasized(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptElement) -> Boolean: ...
    Compulsory = property(get_Compulsory, put_Compulsory)
    DisplayName = property(get_DisplayName, put_DisplayName)
    Emphasized = property(get_Emphasized, put_Emphasized)
    Options = property(get_Options, None)
    SelectedIndex = property(get_SelectedIndex, None)
class VpnCustomPromptText(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnCustomPromptText
    _classid_ = 'Windows.Networking.Vpn.VpnCustomPromptText'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Networking.Vpn.VpnCustomPromptText.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.Vpn.VpnCustomPromptText: ...
    @winrt_mixinmethod
    def put_Text(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptText, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptText) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptElement, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptElement) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Compulsory(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Compulsory(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptElement) -> Boolean: ...
    @winrt_mixinmethod
    def put_Emphasized(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Emphasized(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptElement) -> Boolean: ...
    Compulsory = property(get_Compulsory, put_Compulsory)
    DisplayName = property(get_DisplayName, put_DisplayName)
    Emphasized = property(get_Emphasized, put_Emphasized)
    Text = property(get_Text, put_Text)
class VpnCustomPromptTextInput(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnCustomPromptTextInput
    _classid_ = 'Windows.Networking.Vpn.VpnCustomPromptTextInput'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Networking.Vpn.VpnCustomPromptTextInput.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.Vpn.VpnCustomPromptTextInput: ...
    @winrt_mixinmethod
    def put_PlaceholderText(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptTextInput, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PlaceholderText(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptTextInput) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_IsTextHidden(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptTextInput, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsTextHidden(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptTextInput) -> Boolean: ...
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptTextInput) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptElement, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptElement) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Compulsory(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Compulsory(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptElement) -> Boolean: ...
    @winrt_mixinmethod
    def put_Emphasized(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptElement, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Emphasized(self: win32more.Windows.Networking.Vpn.IVpnCustomPromptElement) -> Boolean: ...
    Compulsory = property(get_Compulsory, put_Compulsory)
    DisplayName = property(get_DisplayName, put_DisplayName)
    Emphasized = property(get_Emphasized, put_Emphasized)
    IsTextHidden = property(get_IsTextHidden, put_IsTextHidden)
    PlaceholderText = property(get_PlaceholderText, put_PlaceholderText)
    Text = property(get_Text, None)
class VpnCustomTextBox(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnCustomTextBox
    _classid_ = 'Windows.Networking.Vpn.VpnCustomTextBox'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Networking.Vpn.VpnCustomTextBox.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.Vpn.VpnCustomTextBox: ...
    @winrt_mixinmethod
    def put_DisplayText(self: win32more.Windows.Networking.Vpn.IVpnCustomTextBox, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayText(self: win32more.Windows.Networking.Vpn.IVpnCustomTextBox) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Label(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Label(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Compulsory(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Compulsory(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt) -> Boolean: ...
    @winrt_mixinmethod
    def put_Bordered(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Bordered(self: win32more.Windows.Networking.Vpn.IVpnCustomPrompt) -> Boolean: ...
    Bordered = property(get_Bordered, put_Bordered)
    Compulsory = property(get_Compulsory, put_Compulsory)
    DisplayText = property(get_DisplayText, put_DisplayText)
    Label = property(get_Label, put_Label)
class VpnDataPathType(Enum, Int32):
    Send = 0
    Receive = 1
class VpnDomainNameAssignment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnDomainNameAssignment
    _classid_ = 'Windows.Networking.Vpn.VpnDomainNameAssignment'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Networking.Vpn.VpnDomainNameAssignment.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.Vpn.VpnDomainNameAssignment: ...
    @winrt_mixinmethod
    def get_DomainNameList(self: win32more.Windows.Networking.Vpn.IVpnDomainNameAssignment) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnDomainNameInfo]: ...
    @winrt_mixinmethod
    def put_ProxyAutoConfigurationUri(self: win32more.Windows.Networking.Vpn.IVpnDomainNameAssignment, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ProxyAutoConfigurationUri(self: win32more.Windows.Networking.Vpn.IVpnDomainNameAssignment) -> win32more.Windows.Foundation.Uri: ...
    DomainNameList = property(get_DomainNameList, None)
    ProxyAutoConfigurationUri = property(get_ProxyAutoConfigurationUri, put_ProxyAutoConfigurationUri)
class VpnDomainNameInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnDomainNameInfo
    _classid_ = 'Windows.Networking.Vpn.VpnDomainNameInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 4:
            super().__init__(move=win32more.Windows.Networking.Vpn.VpnDomainNameInfo.CreateVpnDomainNameInfo(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateVpnDomainNameInfo(cls: win32more.Windows.Networking.Vpn.IVpnDomainNameInfoFactory, name: WinRT_String, nameType: win32more.Windows.Networking.Vpn.VpnDomainNameType, dnsServerList: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Networking.HostName], proxyServerList: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Networking.HostName]) -> win32more.Windows.Networking.Vpn.VpnDomainNameInfo: ...
    @winrt_mixinmethod
    def put_DomainName(self: win32more.Windows.Networking.Vpn.IVpnDomainNameInfo, value: win32more.Windows.Networking.HostName) -> Void: ...
    @winrt_mixinmethod
    def get_DomainName(self: win32more.Windows.Networking.Vpn.IVpnDomainNameInfo) -> win32more.Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def put_DomainNameType(self: win32more.Windows.Networking.Vpn.IVpnDomainNameInfo, value: win32more.Windows.Networking.Vpn.VpnDomainNameType) -> Void: ...
    @winrt_mixinmethod
    def get_DomainNameType(self: win32more.Windows.Networking.Vpn.IVpnDomainNameInfo) -> win32more.Windows.Networking.Vpn.VpnDomainNameType: ...
    @winrt_mixinmethod
    def get_DnsServers(self: win32more.Windows.Networking.Vpn.IVpnDomainNameInfo) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.HostName]: ...
    @winrt_mixinmethod
    def get_WebProxyServers(self: win32more.Windows.Networking.Vpn.IVpnDomainNameInfo) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.HostName]: ...
    @winrt_mixinmethod
    def get_WebProxyUris(self: win32more.Windows.Networking.Vpn.IVpnDomainNameInfo2) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Foundation.Uri]: ...
    DnsServers = property(get_DnsServers, None)
    DomainName = property(get_DomainName, put_DomainName)
    DomainNameType = property(get_DomainNameType, put_DomainNameType)
    WebProxyServers = property(get_WebProxyServers, None)
    WebProxyUris = property(get_WebProxyUris, None)
class VpnDomainNameType(Enum, Int32):
    Suffix = 0
    FullyQualified = 1
    Reserved = 65535
class VpnForegroundActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnForegroundActivatedEventArgs
    _classid_ = 'Windows.Networking.Vpn.VpnForegroundActivatedEventArgs'
    @winrt_mixinmethod
    def get_ProfileName(self: win32more.Windows.Networking.Vpn.IVpnForegroundActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SharedContext(self: win32more.Windows.Networking.Vpn.IVpnForegroundActivatedEventArgs) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_ActivationOperation(self: win32more.Windows.Networking.Vpn.IVpnForegroundActivatedEventArgs) -> win32more.Windows.Networking.Vpn.VpnForegroundActivationOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ActivationOperation = property(get_ActivationOperation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    ProfileName = property(get_ProfileName, None)
    SharedContext = property(get_SharedContext, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class VpnForegroundActivationOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnForegroundActivationOperation
    _classid_ = 'Windows.Networking.Vpn.VpnForegroundActivationOperation'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.Networking.Vpn.IVpnForegroundActivationOperation, result: win32more.Windows.Foundation.Collections.ValueSet) -> Void: ...
class VpnIPProtocol(Enum, Int32):
    None_ = 0
    Tcp = 6
    Udp = 17
    Icmp = 1
    Ipv6Icmp = 58
    Igmp = 2
    Pgm = 113
class VpnInterfaceId(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnInterfaceId
    _classid_ = 'Windows.Networking.Vpn.VpnInterfaceId'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Networking.Vpn.VpnInterfaceId.CreateVpnInterfaceId(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateVpnInterfaceId(cls: win32more.Windows.Networking.Vpn.IVpnInterfaceIdFactory, address: PassArray[Byte]) -> win32more.Windows.Networking.Vpn.VpnInterfaceId: ...
    @winrt_mixinmethod
    def GetAddressInfo(self: win32more.Windows.Networking.Vpn.IVpnInterfaceId, id: ReceiveArray[Byte]) -> Void: ...
class VpnManagementAgent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnManagementAgent
    _classid_ = 'Windows.Networking.Vpn.VpnManagementAgent'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Networking.Vpn.VpnManagementAgent.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.Vpn.VpnManagementAgent: ...
    @winrt_mixinmethod
    def AddProfileFromXmlAsync(self: win32more.Windows.Networking.Vpn.IVpnManagementAgent, xml: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_mixinmethod
    def AddProfileFromObjectAsync(self: win32more.Windows.Networking.Vpn.IVpnManagementAgent, profile: win32more.Windows.Networking.Vpn.IVpnProfile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_mixinmethod
    def UpdateProfileFromXmlAsync(self: win32more.Windows.Networking.Vpn.IVpnManagementAgent, xml: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_mixinmethod
    def UpdateProfileFromObjectAsync(self: win32more.Windows.Networking.Vpn.IVpnManagementAgent, profile: win32more.Windows.Networking.Vpn.IVpnProfile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_mixinmethod
    def GetProfilesAsync(self: win32more.Windows.Networking.Vpn.IVpnManagementAgent) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Networking.Vpn.IVpnProfile]]: ...
    @winrt_mixinmethod
    def DeleteProfileAsync(self: win32more.Windows.Networking.Vpn.IVpnManagementAgent, profile: win32more.Windows.Networking.Vpn.IVpnProfile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_mixinmethod
    def ConnectProfileAsync(self: win32more.Windows.Networking.Vpn.IVpnManagementAgent, profile: win32more.Windows.Networking.Vpn.IVpnProfile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_mixinmethod
    def ConnectProfileWithPasswordCredentialAsync(self: win32more.Windows.Networking.Vpn.IVpnManagementAgent, profile: win32more.Windows.Networking.Vpn.IVpnProfile, passwordCredential: win32more.Windows.Security.Credentials.PasswordCredential) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
    @winrt_mixinmethod
    def DisconnectProfileAsync(self: win32more.Windows.Networking.Vpn.IVpnManagementAgent, profile: win32more.Windows.Networking.Vpn.IVpnProfile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Networking.Vpn.VpnManagementErrorStatus]: ...
class VpnManagementConnectionStatus(Enum, Int32):
    Disconnected = 0
    Disconnecting = 1
    Connected = 2
    Connecting = 3
class VpnManagementErrorStatus(Enum, Int32):
    Ok = 0
    Other = 1
    InvalidXmlSyntax = 2
    ProfileNameTooLong = 3
    ProfileInvalidAppId = 4
    AccessDenied = 5
    CannotFindProfile = 6
    AlreadyDisconnecting = 7
    AlreadyConnected = 8
    GeneralAuthenticationFailure = 9
    EapFailure = 10
    SmartCardFailure = 11
    CertificateFailure = 12
    ServerConfiguration = 13
    NoConnection = 14
    ServerConnection = 15
    UserNamePassword = 16
    DnsNotResolvable = 17
    InvalidIP = 18
class VpnNamespaceAssignment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnNamespaceAssignment
    _classid_ = 'Windows.Networking.Vpn.VpnNamespaceAssignment'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Networking.Vpn.VpnNamespaceAssignment.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.Vpn.VpnNamespaceAssignment: ...
    @winrt_mixinmethod
    def put_NamespaceList(self: win32more.Windows.Networking.Vpn.IVpnNamespaceAssignment, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnNamespaceInfo]) -> Void: ...
    @winrt_mixinmethod
    def get_NamespaceList(self: win32more.Windows.Networking.Vpn.IVpnNamespaceAssignment) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnNamespaceInfo]: ...
    @winrt_mixinmethod
    def put_ProxyAutoConfigUri(self: win32more.Windows.Networking.Vpn.IVpnNamespaceAssignment, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ProxyAutoConfigUri(self: win32more.Windows.Networking.Vpn.IVpnNamespaceAssignment) -> win32more.Windows.Foundation.Uri: ...
    NamespaceList = property(get_NamespaceList, put_NamespaceList)
    ProxyAutoConfigUri = property(get_ProxyAutoConfigUri, put_ProxyAutoConfigUri)
class VpnNamespaceInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnNamespaceInfo
    _classid_ = 'Windows.Networking.Vpn.VpnNamespaceInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Networking.Vpn.VpnNamespaceInfo.CreateVpnNamespaceInfo(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateVpnNamespaceInfo(cls: win32more.Windows.Networking.Vpn.IVpnNamespaceInfoFactory, name: WinRT_String, dnsServerList: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.HostName], proxyServerList: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.HostName]) -> win32more.Windows.Networking.Vpn.VpnNamespaceInfo: ...
    @winrt_mixinmethod
    def put_Namespace(self: win32more.Windows.Networking.Vpn.IVpnNamespaceInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Namespace(self: win32more.Windows.Networking.Vpn.IVpnNamespaceInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DnsServers(self: win32more.Windows.Networking.Vpn.IVpnNamespaceInfo, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.HostName]) -> Void: ...
    @winrt_mixinmethod
    def get_DnsServers(self: win32more.Windows.Networking.Vpn.IVpnNamespaceInfo) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.HostName]: ...
    @winrt_mixinmethod
    def put_WebProxyServers(self: win32more.Windows.Networking.Vpn.IVpnNamespaceInfo, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.HostName]) -> Void: ...
    @winrt_mixinmethod
    def get_WebProxyServers(self: win32more.Windows.Networking.Vpn.IVpnNamespaceInfo) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.HostName]: ...
    DnsServers = property(get_DnsServers, put_DnsServers)
    Namespace = property(get_Namespace, put_Namespace)
    WebProxyServers = property(get_WebProxyServers, put_WebProxyServers)
class VpnNativeProfile(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnNativeProfile
    _classid_ = 'Windows.Networking.Vpn.VpnNativeProfile'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Networking.Vpn.VpnNativeProfile.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.Vpn.VpnNativeProfile: ...
    @winrt_mixinmethod
    def get_Servers(self: win32more.Windows.Networking.Vpn.IVpnNativeProfile) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_RoutingPolicyType(self: win32more.Windows.Networking.Vpn.IVpnNativeProfile) -> win32more.Windows.Networking.Vpn.VpnRoutingPolicyType: ...
    @winrt_mixinmethod
    def put_RoutingPolicyType(self: win32more.Windows.Networking.Vpn.IVpnNativeProfile, value: win32more.Windows.Networking.Vpn.VpnRoutingPolicyType) -> Void: ...
    @winrt_mixinmethod
    def get_NativeProtocolType(self: win32more.Windows.Networking.Vpn.IVpnNativeProfile) -> win32more.Windows.Networking.Vpn.VpnNativeProtocolType: ...
    @winrt_mixinmethod
    def put_NativeProtocolType(self: win32more.Windows.Networking.Vpn.IVpnNativeProfile, value: win32more.Windows.Networking.Vpn.VpnNativeProtocolType) -> Void: ...
    @winrt_mixinmethod
    def get_UserAuthenticationMethod(self: win32more.Windows.Networking.Vpn.IVpnNativeProfile) -> win32more.Windows.Networking.Vpn.VpnAuthenticationMethod: ...
    @winrt_mixinmethod
    def put_UserAuthenticationMethod(self: win32more.Windows.Networking.Vpn.IVpnNativeProfile, value: win32more.Windows.Networking.Vpn.VpnAuthenticationMethod) -> Void: ...
    @winrt_mixinmethod
    def get_TunnelAuthenticationMethod(self: win32more.Windows.Networking.Vpn.IVpnNativeProfile) -> win32more.Windows.Networking.Vpn.VpnAuthenticationMethod: ...
    @winrt_mixinmethod
    def put_TunnelAuthenticationMethod(self: win32more.Windows.Networking.Vpn.IVpnNativeProfile, value: win32more.Windows.Networking.Vpn.VpnAuthenticationMethod) -> Void: ...
    @winrt_mixinmethod
    def get_EapConfiguration(self: win32more.Windows.Networking.Vpn.IVpnNativeProfile) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_EapConfiguration(self: win32more.Windows.Networking.Vpn.IVpnNativeProfile, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ProfileName(self: win32more.Windows.Networking.Vpn.IVpnProfile) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ProfileName(self: win32more.Windows.Networking.Vpn.IVpnProfile, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AppTriggers(self: win32more.Windows.Networking.Vpn.IVpnProfile) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnAppId]: ...
    @winrt_mixinmethod
    def get_Routes(self: win32more.Windows.Networking.Vpn.IVpnProfile) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnRoute]: ...
    @winrt_mixinmethod
    def get_DomainNameInfoList(self: win32more.Windows.Networking.Vpn.IVpnProfile) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnDomainNameInfo]: ...
    @winrt_mixinmethod
    def get_TrafficFilters(self: win32more.Windows.Networking.Vpn.IVpnProfile) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnTrafficFilter]: ...
    @winrt_mixinmethod
    def get_RememberCredentials(self: win32more.Windows.Networking.Vpn.IVpnProfile) -> Boolean: ...
    @winrt_mixinmethod
    def put_RememberCredentials(self: win32more.Windows.Networking.Vpn.IVpnProfile, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AlwaysOn(self: win32more.Windows.Networking.Vpn.IVpnProfile) -> Boolean: ...
    @winrt_mixinmethod
    def put_AlwaysOn(self: win32more.Windows.Networking.Vpn.IVpnProfile, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_RequireVpnClientAppUI(self: win32more.Windows.Networking.Vpn.IVpnNativeProfile2) -> Boolean: ...
    @winrt_mixinmethod
    def put_RequireVpnClientAppUI(self: win32more.Windows.Networking.Vpn.IVpnNativeProfile2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ConnectionStatus(self: win32more.Windows.Networking.Vpn.IVpnNativeProfile2) -> win32more.Windows.Networking.Vpn.VpnManagementConnectionStatus: ...
    AlwaysOn = property(get_AlwaysOn, put_AlwaysOn)
    AppTriggers = property(get_AppTriggers, None)
    ConnectionStatus = property(get_ConnectionStatus, None)
    DomainNameInfoList = property(get_DomainNameInfoList, None)
    EapConfiguration = property(get_EapConfiguration, put_EapConfiguration)
    NativeProtocolType = property(get_NativeProtocolType, put_NativeProtocolType)
    ProfileName = property(get_ProfileName, put_ProfileName)
    RememberCredentials = property(get_RememberCredentials, put_RememberCredentials)
    RequireVpnClientAppUI = property(get_RequireVpnClientAppUI, put_RequireVpnClientAppUI)
    Routes = property(get_Routes, None)
    RoutingPolicyType = property(get_RoutingPolicyType, put_RoutingPolicyType)
    Servers = property(get_Servers, None)
    TrafficFilters = property(get_TrafficFilters, None)
    TunnelAuthenticationMethod = property(get_TunnelAuthenticationMethod, put_TunnelAuthenticationMethod)
    UserAuthenticationMethod = property(get_UserAuthenticationMethod, put_UserAuthenticationMethod)
class VpnNativeProtocolType(Enum, Int32):
    Pptp = 0
    L2tp = 1
    IpsecIkev2 = 2
class VpnPacketBuffer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnPacketBuffer
    _classid_ = 'Windows.Networking.Vpn.VpnPacketBuffer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Networking.Vpn.VpnPacketBuffer.CreateVpnPacketBuffer(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateVpnPacketBuffer(cls: win32more.Windows.Networking.Vpn.IVpnPacketBufferFactory, parentBuffer: win32more.Windows.Networking.Vpn.VpnPacketBuffer, offset: UInt32, length: UInt32) -> win32more.Windows.Networking.Vpn.VpnPacketBuffer: ...
    @winrt_mixinmethod
    def get_Buffer(self: win32more.Windows.Networking.Vpn.IVpnPacketBuffer) -> win32more.Windows.Storage.Streams.Buffer: ...
    @winrt_mixinmethod
    def put_Status(self: win32more.Windows.Networking.Vpn.IVpnPacketBuffer, value: win32more.Windows.Networking.Vpn.VpnPacketBufferStatus) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Networking.Vpn.IVpnPacketBuffer) -> win32more.Windows.Networking.Vpn.VpnPacketBufferStatus: ...
    @winrt_mixinmethod
    def put_TransportAffinity(self: win32more.Windows.Networking.Vpn.IVpnPacketBuffer, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_TransportAffinity(self: win32more.Windows.Networking.Vpn.IVpnPacketBuffer) -> UInt32: ...
    @winrt_mixinmethod
    def get_AppId(self: win32more.Windows.Networking.Vpn.IVpnPacketBuffer2) -> win32more.Windows.Networking.Vpn.VpnAppId: ...
    @winrt_mixinmethod
    def put_TransportContext(self: win32more.Windows.Networking.Vpn.IVpnPacketBuffer3, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_TransportContext(self: win32more.Windows.Networking.Vpn.IVpnPacketBuffer3) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    AppId = property(get_AppId, None)
    Buffer = property(get_Buffer, None)
    Status = property(get_Status, put_Status)
    TransportAffinity = property(get_TransportAffinity, put_TransportAffinity)
    TransportContext = property(get_TransportContext, put_TransportContext)
class VpnPacketBufferList(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[IterableProtocol[win32more.Windows.Networking.Vpn.VpnPacketBuffer]]
    default_interface: win32more.Windows.Networking.Vpn.IVpnPacketBufferList
    _classid_ = 'Windows.Networking.Vpn.VpnPacketBufferList'
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Networking.Vpn.IVpnPacketBufferList, nextVpnPacketBuffer: win32more.Windows.Networking.Vpn.VpnPacketBuffer) -> Void: ...
    @winrt_mixinmethod
    def AddAtBegin(self: win32more.Windows.Networking.Vpn.IVpnPacketBufferList, nextVpnPacketBuffer: win32more.Windows.Networking.Vpn.VpnPacketBuffer) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Networking.Vpn.IVpnPacketBufferList) -> win32more.Windows.Networking.Vpn.VpnPacketBuffer: ...
    @winrt_mixinmethod
    def RemoveAtBegin(self: win32more.Windows.Networking.Vpn.IVpnPacketBufferList) -> win32more.Windows.Networking.Vpn.VpnPacketBuffer: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Networking.Vpn.IVpnPacketBufferList) -> Void: ...
    @winrt_mixinmethod
    def put_Status(self: win32more.Windows.Networking.Vpn.IVpnPacketBufferList, value: win32more.Windows.Networking.Vpn.VpnPacketBufferStatus) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Networking.Vpn.IVpnPacketBufferList) -> win32more.Windows.Networking.Vpn.VpnPacketBufferStatus: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Networking.Vpn.IVpnPacketBufferList) -> UInt32: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Networking.Vpn.VpnPacketBuffer]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Networking.Vpn.VpnPacketBuffer]: ...
    Size = property(get_Size, None)
    Status = property(get_Status, put_Status)
class VpnPacketBufferStatus(Enum, Int32):
    Ok = 0
    InvalidBufferSize = 1
class VpnPickedCredential(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnPickedCredential
    _classid_ = 'Windows.Networking.Vpn.VpnPickedCredential'
    @winrt_mixinmethod
    def get_PasskeyCredential(self: win32more.Windows.Networking.Vpn.IVpnPickedCredential) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def get_AdditionalPin(self: win32more.Windows.Networking.Vpn.IVpnPickedCredential) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OldPasswordCredential(self: win32more.Windows.Networking.Vpn.IVpnPickedCredential) -> win32more.Windows.Security.Credentials.PasswordCredential: ...
    AdditionalPin = property(get_AdditionalPin, None)
    OldPasswordCredential = property(get_OldPasswordCredential, None)
    PasskeyCredential = property(get_PasskeyCredential, None)
class VpnPlugInProfile(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnPlugInProfile
    _classid_ = 'Windows.Networking.Vpn.VpnPlugInProfile'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Networking.Vpn.VpnPlugInProfile.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.Vpn.VpnPlugInProfile: ...
    @winrt_mixinmethod
    def get_ServerUris(self: win32more.Windows.Networking.Vpn.IVpnPlugInProfile) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Foundation.Uri]: ...
    @winrt_mixinmethod
    def get_CustomConfiguration(self: win32more.Windows.Networking.Vpn.IVpnPlugInProfile) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CustomConfiguration(self: win32more.Windows.Networking.Vpn.IVpnPlugInProfile, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_VpnPluginPackageFamilyName(self: win32more.Windows.Networking.Vpn.IVpnPlugInProfile) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_VpnPluginPackageFamilyName(self: win32more.Windows.Networking.Vpn.IVpnPlugInProfile, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ProfileName(self: win32more.Windows.Networking.Vpn.IVpnProfile) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ProfileName(self: win32more.Windows.Networking.Vpn.IVpnProfile, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AppTriggers(self: win32more.Windows.Networking.Vpn.IVpnProfile) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnAppId]: ...
    @winrt_mixinmethod
    def get_Routes(self: win32more.Windows.Networking.Vpn.IVpnProfile) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnRoute]: ...
    @winrt_mixinmethod
    def get_DomainNameInfoList(self: win32more.Windows.Networking.Vpn.IVpnProfile) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnDomainNameInfo]: ...
    @winrt_mixinmethod
    def get_TrafficFilters(self: win32more.Windows.Networking.Vpn.IVpnProfile) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnTrafficFilter]: ...
    @winrt_mixinmethod
    def get_RememberCredentials(self: win32more.Windows.Networking.Vpn.IVpnProfile) -> Boolean: ...
    @winrt_mixinmethod
    def put_RememberCredentials(self: win32more.Windows.Networking.Vpn.IVpnProfile, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AlwaysOn(self: win32more.Windows.Networking.Vpn.IVpnProfile) -> Boolean: ...
    @winrt_mixinmethod
    def put_AlwaysOn(self: win32more.Windows.Networking.Vpn.IVpnProfile, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_RequireVpnClientAppUI(self: win32more.Windows.Networking.Vpn.IVpnPlugInProfile2) -> Boolean: ...
    @winrt_mixinmethod
    def put_RequireVpnClientAppUI(self: win32more.Windows.Networking.Vpn.IVpnPlugInProfile2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ConnectionStatus(self: win32more.Windows.Networking.Vpn.IVpnPlugInProfile2) -> win32more.Windows.Networking.Vpn.VpnManagementConnectionStatus: ...
    AlwaysOn = property(get_AlwaysOn, put_AlwaysOn)
    AppTriggers = property(get_AppTriggers, None)
    ConnectionStatus = property(get_ConnectionStatus, None)
    CustomConfiguration = property(get_CustomConfiguration, put_CustomConfiguration)
    DomainNameInfoList = property(get_DomainNameInfoList, None)
    ProfileName = property(get_ProfileName, put_ProfileName)
    RememberCredentials = property(get_RememberCredentials, put_RememberCredentials)
    RequireVpnClientAppUI = property(get_RequireVpnClientAppUI, put_RequireVpnClientAppUI)
    Routes = property(get_Routes, None)
    ServerUris = property(get_ServerUris, None)
    TrafficFilters = property(get_TrafficFilters, None)
    VpnPluginPackageFamilyName = property(get_VpnPluginPackageFamilyName, put_VpnPluginPackageFamilyName)
class VpnRoute(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnRoute
    _classid_ = 'Windows.Networking.Vpn.VpnRoute'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Networking.Vpn.VpnRoute.CreateVpnRoute(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateVpnRoute(cls: win32more.Windows.Networking.Vpn.IVpnRouteFactory, address: win32more.Windows.Networking.HostName, prefixSize: Byte) -> win32more.Windows.Networking.Vpn.VpnRoute: ...
    @winrt_mixinmethod
    def put_Address(self: win32more.Windows.Networking.Vpn.IVpnRoute, value: win32more.Windows.Networking.HostName) -> Void: ...
    @winrt_mixinmethod
    def get_Address(self: win32more.Windows.Networking.Vpn.IVpnRoute) -> win32more.Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def put_PrefixSize(self: win32more.Windows.Networking.Vpn.IVpnRoute, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_PrefixSize(self: win32more.Windows.Networking.Vpn.IVpnRoute) -> Byte: ...
    Address = property(get_Address, put_Address)
    PrefixSize = property(get_PrefixSize, put_PrefixSize)
class VpnRouteAssignment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnRouteAssignment
    _classid_ = 'Windows.Networking.Vpn.VpnRouteAssignment'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Networking.Vpn.VpnRouteAssignment.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.Vpn.VpnRouteAssignment: ...
    @winrt_mixinmethod
    def put_Ipv4InclusionRoutes(self: win32more.Windows.Networking.Vpn.IVpnRouteAssignment, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnRoute]) -> Void: ...
    @winrt_mixinmethod
    def put_Ipv6InclusionRoutes(self: win32more.Windows.Networking.Vpn.IVpnRouteAssignment, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnRoute]) -> Void: ...
    @winrt_mixinmethod
    def get_Ipv4InclusionRoutes(self: win32more.Windows.Networking.Vpn.IVpnRouteAssignment) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnRoute]: ...
    @winrt_mixinmethod
    def get_Ipv6InclusionRoutes(self: win32more.Windows.Networking.Vpn.IVpnRouteAssignment) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnRoute]: ...
    @winrt_mixinmethod
    def put_Ipv4ExclusionRoutes(self: win32more.Windows.Networking.Vpn.IVpnRouteAssignment, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnRoute]) -> Void: ...
    @winrt_mixinmethod
    def put_Ipv6ExclusionRoutes(self: win32more.Windows.Networking.Vpn.IVpnRouteAssignment, value: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnRoute]) -> Void: ...
    @winrt_mixinmethod
    def get_Ipv4ExclusionRoutes(self: win32more.Windows.Networking.Vpn.IVpnRouteAssignment) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnRoute]: ...
    @winrt_mixinmethod
    def get_Ipv6ExclusionRoutes(self: win32more.Windows.Networking.Vpn.IVpnRouteAssignment) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnRoute]: ...
    @winrt_mixinmethod
    def put_ExcludeLocalSubnets(self: win32more.Windows.Networking.Vpn.IVpnRouteAssignment, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ExcludeLocalSubnets(self: win32more.Windows.Networking.Vpn.IVpnRouteAssignment) -> Boolean: ...
    ExcludeLocalSubnets = property(get_ExcludeLocalSubnets, put_ExcludeLocalSubnets)
    Ipv4ExclusionRoutes = property(get_Ipv4ExclusionRoutes, put_Ipv4ExclusionRoutes)
    Ipv4InclusionRoutes = property(get_Ipv4InclusionRoutes, put_Ipv4InclusionRoutes)
    Ipv6ExclusionRoutes = property(get_Ipv6ExclusionRoutes, put_Ipv6ExclusionRoutes)
    Ipv6InclusionRoutes = property(get_Ipv6InclusionRoutes, put_Ipv6InclusionRoutes)
class VpnRoutingPolicyType(Enum, Int32):
    SplitRouting = 0
    ForceAllTrafficOverVpn = 1
class VpnSystemHealth(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnSystemHealth
    _classid_ = 'Windows.Networking.Vpn.VpnSystemHealth'
    @winrt_mixinmethod
    def get_StatementOfHealth(self: win32more.Windows.Networking.Vpn.IVpnSystemHealth) -> win32more.Windows.Storage.Streams.Buffer: ...
    StatementOfHealth = property(get_StatementOfHealth, None)
class VpnTrafficFilter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnTrafficFilter
    _classid_ = 'Windows.Networking.Vpn.VpnTrafficFilter'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Networking.Vpn.VpnTrafficFilter.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Networking.Vpn.IVpnTrafficFilterFactory, appId: win32more.Windows.Networking.Vpn.VpnAppId) -> win32more.Windows.Networking.Vpn.VpnTrafficFilter: ...
    @winrt_mixinmethod
    def get_AppId(self: win32more.Windows.Networking.Vpn.IVpnTrafficFilter) -> win32more.Windows.Networking.Vpn.VpnAppId: ...
    @winrt_mixinmethod
    def put_AppId(self: win32more.Windows.Networking.Vpn.IVpnTrafficFilter, value: win32more.Windows.Networking.Vpn.VpnAppId) -> Void: ...
    @winrt_mixinmethod
    def get_AppClaims(self: win32more.Windows.Networking.Vpn.IVpnTrafficFilter) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Protocol(self: win32more.Windows.Networking.Vpn.IVpnTrafficFilter) -> win32more.Windows.Networking.Vpn.VpnIPProtocol: ...
    @winrt_mixinmethod
    def put_Protocol(self: win32more.Windows.Networking.Vpn.IVpnTrafficFilter, value: win32more.Windows.Networking.Vpn.VpnIPProtocol) -> Void: ...
    @winrt_mixinmethod
    def get_LocalPortRanges(self: win32more.Windows.Networking.Vpn.IVpnTrafficFilter) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_RemotePortRanges(self: win32more.Windows.Networking.Vpn.IVpnTrafficFilter) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_LocalAddressRanges(self: win32more.Windows.Networking.Vpn.IVpnTrafficFilter) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_RemoteAddressRanges(self: win32more.Windows.Networking.Vpn.IVpnTrafficFilter) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_RoutingPolicyType(self: win32more.Windows.Networking.Vpn.IVpnTrafficFilter) -> win32more.Windows.Networking.Vpn.VpnRoutingPolicyType: ...
    @winrt_mixinmethod
    def put_RoutingPolicyType(self: win32more.Windows.Networking.Vpn.IVpnTrafficFilter, value: win32more.Windows.Networking.Vpn.VpnRoutingPolicyType) -> Void: ...
    AppClaims = property(get_AppClaims, None)
    AppId = property(get_AppId, put_AppId)
    LocalAddressRanges = property(get_LocalAddressRanges, None)
    LocalPortRanges = property(get_LocalPortRanges, None)
    Protocol = property(get_Protocol, put_Protocol)
    RemoteAddressRanges = property(get_RemoteAddressRanges, None)
    RemotePortRanges = property(get_RemotePortRanges, None)
    RoutingPolicyType = property(get_RoutingPolicyType, put_RoutingPolicyType)
class VpnTrafficFilterAssignment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Networking.Vpn.IVpnTrafficFilterAssignment
    _classid_ = 'Windows.Networking.Vpn.VpnTrafficFilterAssignment'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Networking.Vpn.VpnTrafficFilterAssignment.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Networking.Vpn.VpnTrafficFilterAssignment: ...
    @winrt_mixinmethod
    def get_TrafficFilterList(self: win32more.Windows.Networking.Vpn.IVpnTrafficFilterAssignment) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Networking.Vpn.VpnTrafficFilter]: ...
    @winrt_mixinmethod
    def get_AllowOutbound(self: win32more.Windows.Networking.Vpn.IVpnTrafficFilterAssignment) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowOutbound(self: win32more.Windows.Networking.Vpn.IVpnTrafficFilterAssignment, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AllowInbound(self: win32more.Windows.Networking.Vpn.IVpnTrafficFilterAssignment) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowInbound(self: win32more.Windows.Networking.Vpn.IVpnTrafficFilterAssignment, value: Boolean) -> Void: ...
    AllowInbound = property(get_AllowInbound, put_AllowInbound)
    AllowOutbound = property(get_AllowOutbound, put_AllowOutbound)
    TrafficFilterList = property(get_TrafficFilterList, None)


make_ready(__name__)
