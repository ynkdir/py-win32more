from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.NetworkManagement.WindowsFirewall
import Windows.Win32.Security
import Windows.Win32.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
NETCON_MAX_NAME_LEN: UInt32 = 256
S_OBJECT_NO_LONGER_VALID: Windows.Win32.Foundation.HRESULT = 2
NETISO_GEID_FOR_WDAG: UInt32 = 1
NETISO_GEID_FOR_NEUTRAL_AWARE: UInt32 = 2
@winfunctype('api-ms-win-net-isolation-l1-1-0.dll')
def NetworkIsolationSetupAppContainerBinaries(applicationContainerSid: Windows.Win32.Foundation.PSID, packageFullName: Windows.Win32.Foundation.PWSTR, packageFolder: Windows.Win32.Foundation.PWSTR, displayName: Windows.Win32.Foundation.PWSTR, bBinariesFullyComputed: Windows.Win32.Foundation.BOOL, binaries: POINTER(Windows.Win32.Foundation.PWSTR), binariesCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-net-isolation-l1-1-0.dll')
def NetworkIsolationRegisterForAppContainerChanges(flags: UInt32, callback: Windows.Win32.NetworkManagement.WindowsFirewall.PAC_CHANGES_CALLBACK_FN, context: c_void_p, registrationObject: POINTER(Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('api-ms-win-net-isolation-l1-1-0.dll')
def NetworkIsolationUnregisterForAppContainerChanges(registrationObject: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('api-ms-win-net-isolation-l1-1-0.dll')
def NetworkIsolationFreeAppContainers(pPublicAppCs: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INET_FIREWALL_APP_CONTAINER_head)) -> UInt32: ...
@winfunctype('api-ms-win-net-isolation-l1-1-0.dll')
def NetworkIsolationEnumAppContainers(Flags: UInt32, pdwNumPublicAppCs: POINTER(UInt32), ppPublicAppCs: POINTER(POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INET_FIREWALL_APP_CONTAINER_head))) -> UInt32: ...
@winfunctype('api-ms-win-net-isolation-l1-1-0.dll')
def NetworkIsolationGetAppContainerConfig(pdwNumPublicAppCs: POINTER(UInt32), appContainerSids: POINTER(POINTER(Windows.Win32.Security.SID_AND_ATTRIBUTES_head))) -> UInt32: ...
@winfunctype('api-ms-win-net-isolation-l1-1-0.dll')
def NetworkIsolationSetAppContainerConfig(dwNumPublicAppCs: UInt32, appContainerSids: POINTER(Windows.Win32.Security.SID_AND_ATTRIBUTES_head)) -> UInt32: ...
@winfunctype('api-ms-win-net-isolation-l1-1-0.dll')
def NetworkIsolationDiagnoseConnectFailureAndGetInfo(wszServerName: Windows.Win32.Foundation.PWSTR, netIsoError: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.NETISO_ERROR_TYPE)) -> UInt32: ...
class FW_DYNAMIC_KEYWORD_ADDRESS0(Structure):
    id: Guid
    keyword: Windows.Win32.Foundation.PWSTR
    flags: UInt32
    addresses: Windows.Win32.Foundation.PWSTR
class FW_DYNAMIC_KEYWORD_ADDRESS_DATA0(Structure):
    dynamicKeywordAddress: Windows.Win32.NetworkManagement.WindowsFirewall.FW_DYNAMIC_KEYWORD_ADDRESS0
    next: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.FW_DYNAMIC_KEYWORD_ADDRESS_DATA0_head)
    schemaVersion: UInt16
    originType: Windows.Win32.NetworkManagement.WindowsFirewall.FW_DYNAMIC_KEYWORD_ORIGIN_TYPE
FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS = UInt32
FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS_AUTO_RESOLVE: FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS = 1
FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS_NON_AUTO_RESOLVE: FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS = 2
FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS_ALL: FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS = 3
FW_DYNAMIC_KEYWORD_ADDRESS_FLAGS = UInt32
FW_DYNAMIC_KEYWORD_ADDRESS_FLAGS_AUTO_RESOLVE: FW_DYNAMIC_KEYWORD_ADDRESS_FLAGS = 1
FW_DYNAMIC_KEYWORD_ORIGIN_TYPE = Int32
FW_DYNAMIC_KEYWORD_ORIGIN_INVALID: FW_DYNAMIC_KEYWORD_ORIGIN_TYPE = 0
FW_DYNAMIC_KEYWORD_ORIGIN_LOCAL: FW_DYNAMIC_KEYWORD_ORIGIN_TYPE = 1
FW_DYNAMIC_KEYWORD_ORIGIN_MDM: FW_DYNAMIC_KEYWORD_ORIGIN_TYPE = 2
ICS_TARGETTYPE = Int32
ICSTT_NAME: ICS_TARGETTYPE = 0
ICSTT_IPADDRESS: ICS_TARGETTYPE = 1
class IDynamicPortMapping(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('4fc80282-23b6-4378-9a-27-cd-8f-17-c9-40-0c')
    @commethod(7)
    def get_ExternalIPAddress(pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_RemoteHost(pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ExternalPort(pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Protocol(pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_InternalPort(pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_InternalClient(pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Enabled(pVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Description(pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_LeaseDuration(pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def RenewLease(lLeaseDurationDesired: Int32, pLeaseDurationReturned: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def EditInternalClient(bstrInternalClient: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Enable(vb: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def EditDescription(bstrDescription: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def EditInternalPort(lInternalPort: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IDynamicPortMappingCollection(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('b60de00f-156e-4e8d-9e-c1-3a-23-42-c1-08-99')
    @commethod(7)
    def get__NewEnum(pVal: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(bstrRemoteHost: Windows.Win32.Foundation.BSTR, lExternalPort: Int32, bstrProtocol: Windows.Win32.Foundation.BSTR, ppDPM: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.IDynamicPortMapping_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Remove(bstrRemoteHost: Windows.Win32.Foundation.BSTR, lExternalPort: Int32, bstrProtocol: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Add(bstrRemoteHost: Windows.Win32.Foundation.BSTR, lExternalPort: Int32, bstrProtocol: Windows.Win32.Foundation.BSTR, lInternalPort: Int32, bstrInternalClient: Windows.Win32.Foundation.BSTR, bEnabled: Windows.Win32.Foundation.VARIANT_BOOL, bstrDescription: Windows.Win32.Foundation.BSTR, lLeaseDuration: Int32, ppDPM: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.IDynamicPortMapping_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumNetConnection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c08956a0-1cd3-11d1-b1-c5-00-80-5f-c1-27-0e')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INetConnection_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.IEnumNetConnection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumNetSharingEveryConnection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c08956b8-1cd3-11d1-b1-c5-00-80-5f-c1-27-0e')
    @commethod(3)
    def Next(celt: UInt32, rgVar: POINTER(Windows.Win32.System.Com.VARIANT_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.IEnumNetSharingEveryConnection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumNetSharingPortMapping(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c08956b0-1cd3-11d1-b1-c5-00-80-5f-c1-27-0e')
    @commethod(3)
    def Next(celt: UInt32, rgVar: POINTER(Windows.Win32.System.Com.VARIANT_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.IEnumNetSharingPortMapping_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumNetSharingPrivateConnection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c08956b5-1cd3-11d1-b1-c5-00-80-5f-c1-27-0e')
    @commethod(3)
    def Next(celt: UInt32, rgVar: POINTER(Windows.Win32.System.Com.VARIANT_head), pCeltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.IEnumNetSharingPrivateConnection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumNetSharingPublicConnection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c08956b4-1cd3-11d1-b1-c5-00-80-5f-c1-27-0e')
    @commethod(3)
    def Next(celt: UInt32, rgVar: POINTER(Windows.Win32.System.Com.VARIANT_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.IEnumNetSharingPublicConnection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class INATEventManager(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('624bd588-9060-4109-b0-b0-1a-db-bc-ac-32-df')
    @commethod(7)
    def put_ExternalIPAddressCallback(pUnk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_NumberOfEntriesCallback(pUnk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class INATExternalIPAddressCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9c416740-a34e-446f-ba-06-ab-d0-4c-31-49-ae')
    @commethod(3)
    def NewExternalIPAddress(bstrNewExternalIPAddress: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class INATNumberOfEntriesCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c83a0a74-91ee-41b6-b6-7a-67-e0-f0-0b-bd-78')
    @commethod(3)
    def NewNumberOfEntries(lNewNumberOfEntries: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class INET_FIREWALL_AC_BINARIES(Structure):
    count: UInt32
    binaries: POINTER(Windows.Win32.Foundation.PWSTR)
class INET_FIREWALL_AC_CAPABILITIES(Structure):
    count: UInt32
    capabilities: POINTER(Windows.Win32.Security.SID_AND_ATTRIBUTES_head)
class INET_FIREWALL_AC_CHANGE(Structure):
    changeType: Windows.Win32.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_CHANGE_TYPE
    createType: Windows.Win32.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_CREATION_TYPE
    appContainerSid: POINTER(Windows.Win32.Security.SID_head)
    userSid: POINTER(Windows.Win32.Security.SID_head)
    displayName: Windows.Win32.Foundation.PWSTR
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        capabilities: Windows.Win32.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_CAPABILITIES
        binaries: Windows.Win32.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_BINARIES
INET_FIREWALL_AC_CHANGE_TYPE = Int32
INET_FIREWALL_AC_CHANGE_INVALID: INET_FIREWALL_AC_CHANGE_TYPE = 0
INET_FIREWALL_AC_CHANGE_CREATE: INET_FIREWALL_AC_CHANGE_TYPE = 1
INET_FIREWALL_AC_CHANGE_DELETE: INET_FIREWALL_AC_CHANGE_TYPE = 2
INET_FIREWALL_AC_CHANGE_MAX: INET_FIREWALL_AC_CHANGE_TYPE = 3
INET_FIREWALL_AC_CREATION_TYPE = Int32
INET_FIREWALL_AC_NONE: INET_FIREWALL_AC_CREATION_TYPE = 0
INET_FIREWALL_AC_PACKAGE_ID_ONLY: INET_FIREWALL_AC_CREATION_TYPE = 1
INET_FIREWALL_AC_BINARY: INET_FIREWALL_AC_CREATION_TYPE = 2
INET_FIREWALL_AC_MAX: INET_FIREWALL_AC_CREATION_TYPE = 4
class INET_FIREWALL_APP_CONTAINER(Structure):
    appContainerSid: POINTER(Windows.Win32.Security.SID_head)
    userSid: POINTER(Windows.Win32.Security.SID_head)
    appContainerName: Windows.Win32.Foundation.PWSTR
    displayName: Windows.Win32.Foundation.PWSTR
    description: Windows.Win32.Foundation.PWSTR
    capabilities: Windows.Win32.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_CAPABILITIES
    binaries: Windows.Win32.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_BINARIES
    workingDirectory: Windows.Win32.Foundation.PWSTR
    packageFullName: Windows.Win32.Foundation.PWSTR
class INetConnection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c08956a1-1cd3-11d1-b1-c5-00-80-5f-c1-27-0e')
    @commethod(3)
    def Connect() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Disconnect() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Delete() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Duplicate(pszwDuplicateName: Windows.Win32.Foundation.PWSTR, ppCon: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INetConnection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetProperties(ppProps: POINTER(POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.NETCON_PROPERTIES_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetUiObjectClassId(pclsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Rename(pszwNewName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class INetConnectionConnectUi(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c08956a3-1cd3-11d1-b1-c5-00-80-5f-c1-27-0e')
    @commethod(3)
    def SetConnection(pCon: Windows.Win32.NetworkManagement.WindowsFirewall.INetConnection_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Connect(hwndParent: Windows.Win32.Foundation.HWND, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Disconnect(hwndParent: Windows.Win32.Foundation.HWND, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class INetConnectionManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c08956a2-1cd3-11d1-b1-c5-00-80-5f-c1-27-0e')
    @commethod(3)
    def EnumConnections(Flags: Windows.Win32.NetworkManagement.WindowsFirewall.NETCONMGR_ENUM_FLAGS, ppEnum: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.IEnumNetConnection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class INetConnectionProps(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('f4277c95-ce5b-463d-81-67-56-62-d9-bc-aa-72')
    @commethod(7)
    def get_Guid(pbstrGuid: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Name(pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_DeviceName(pbstrDeviceName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Status(pStatus: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.NETCON_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_MediaType(pMediaType: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.NETCON_MEDIATYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Characteristics(pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class INetFwAuthorizedApplication(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('b5e64ffa-c2c5-444e-a3-01-fb-5e-00-01-80-50')
    @commethod(7)
    def get_Name(name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Name(name: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ProcessImageFileName(imageFileName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ProcessImageFileName(imageFileName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_IpVersion(ipVersion: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_IpVersion(ipVersion: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Scope(scope: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_SCOPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Scope(scope: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_SCOPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_RemoteAddresses(remoteAddrs: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_RemoteAddresses(remoteAddrs: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Enabled(enabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_Enabled(enabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class INetFwAuthorizedApplications(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('644efd52-ccf9-486c-97-a2-39-f3-52-57-0b-30')
    @commethod(7)
    def get_Count(count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Add(app: Windows.Win32.NetworkManagement.WindowsFirewall.INetFwAuthorizedApplication_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Remove(imageFileName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Item(imageFileName: Windows.Win32.Foundation.BSTR, app: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INetFwAuthorizedApplication_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get__NewEnum(newEnum: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class INetFwIcmpSettings(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('a6207b2e-7cdd-426a-95-1e-5e-1c-bc-5a-fe-ad')
    @commethod(7)
    def get_AllowOutboundDestinationUnreachable(allow: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_AllowOutboundDestinationUnreachable(allow: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_AllowRedirect(allow: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_AllowRedirect(allow: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_AllowInboundEchoRequest(allow: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_AllowInboundEchoRequest(allow: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_AllowOutboundTimeExceeded(allow: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_AllowOutboundTimeExceeded(allow: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_AllowOutboundParameterProblem(allow: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_AllowOutboundParameterProblem(allow: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_AllowOutboundSourceQuench(allow: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_AllowOutboundSourceQuench(allow: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_AllowInboundRouterRequest(allow: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_AllowInboundRouterRequest(allow: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_AllowInboundTimestampRequest(allow: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_AllowInboundTimestampRequest(allow: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_AllowInboundMaskRequest(allow: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_AllowInboundMaskRequest(allow: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_AllowOutboundPacketTooBig(allow: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_AllowOutboundPacketTooBig(allow: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class INetFwMgr(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('f7898af5-cac4-4632-a2-ec-da-06-e5-11-1a-f2')
    @commethod(7)
    def get_LocalPolicy(localPolicy: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INetFwPolicy_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CurrentProfileType(profileType: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RestoreDefaults() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsPortAllowed(imageFileName: Windows.Win32.Foundation.BSTR, ipVersion: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION, portNumber: Int32, localAddress: Windows.Win32.Foundation.BSTR, ipProtocol: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_PROTOCOL, allowed: POINTER(Windows.Win32.System.Com.VARIANT_head), restricted: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def IsIcmpTypeAllowed(ipVersion: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION, localAddress: Windows.Win32.Foundation.BSTR, type: Byte, allowed: POINTER(Windows.Win32.System.Com.VARIANT_head), restricted: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class INetFwOpenPort(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('e0483ba0-47ff-4d9c-a6-d6-77-41-d0-b1-95-f7')
    @commethod(7)
    def get_Name(name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Name(name: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_IpVersion(ipVersion: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_IpVersion(ipVersion: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Protocol(ipProtocol: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_PROTOCOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Protocol(ipProtocol: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_PROTOCOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Port(portNumber: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Port(portNumber: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Scope(scope: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_SCOPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Scope(scope: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_SCOPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_RemoteAddresses(remoteAddrs: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_RemoteAddresses(remoteAddrs: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_Enabled(enabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_Enabled(enabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_BuiltIn(builtIn: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class INetFwOpenPorts(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('c0e9d7fa-e07e-430a-b1-9a-09-0c-e8-2d-92-e2')
    @commethod(7)
    def get_Count(count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Add(port: Windows.Win32.NetworkManagement.WindowsFirewall.INetFwOpenPort_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Remove(portNumber: Int32, ipProtocol: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_PROTOCOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Item(portNumber: Int32, ipProtocol: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_PROTOCOL, openPort: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INetFwOpenPort_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get__NewEnum(newEnum: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class INetFwPolicy(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('d46d2478-9ac9-4008-9d-c7-55-63-ce-55-36-cc')
    @commethod(7)
    def get_CurrentProfile(profile: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INetFwProfile_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetProfileByType(profileType: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE, profile: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INetFwProfile_head)) -> Windows.Win32.Foundation.HRESULT: ...
class INetFwPolicy2(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('98325047-c671-4174-8d-81-de-fc-d3-f0-31-86')
    @commethod(7)
    def get_CurrentProfileTypes(profileTypesBitmask: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_FirewallEnabled(profileType: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, enabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_FirewallEnabled(profileType: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, enabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ExcludedInterfaces(profileType: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, interfaces: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_ExcludedInterfaces(profileType: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, interfaces: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_BlockAllInboundTraffic(profileType: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, Block: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_BlockAllInboundTraffic(profileType: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, Block: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_NotificationsDisabled(profileType: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, disabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_NotificationsDisabled(profileType: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, disabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_UnicastResponsesToMulticastBroadcastDisabled(profileType: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, disabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_UnicastResponsesToMulticastBroadcastDisabled(profileType: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, disabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Rules(rules: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INetFwRules_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_ServiceRestriction(ServiceRestriction: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INetFwServiceRestriction_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def EnableRuleGroup(profileTypesBitmask: Int32, group: Windows.Win32.Foundation.BSTR, enable: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def IsRuleGroupEnabled(profileTypesBitmask: Int32, group: Windows.Win32.Foundation.BSTR, enabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def RestoreLocalFirewallDefaults() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_DefaultInboundAction(profileType: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, action: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_ACTION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_DefaultInboundAction(profileType: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, action: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_ACTION) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_DefaultOutboundAction(profileType: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, action: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_ACTION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_DefaultOutboundAction(profileType: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2, action: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_ACTION) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_IsRuleGroupCurrentlyEnabled(group: Windows.Win32.Foundation.BSTR, enabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_LocalPolicyModifyState(modifyState: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_MODIFY_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
class INetFwProduct(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('71881699-18f4-458b-b8-92-3f-fc-e5-e0-7f-75')
    @commethod(7)
    def get_RuleCategories(ruleCategories: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_RuleCategories(ruleCategories: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_DisplayName(displayName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_DisplayName(displayName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_PathToSignedProductExe(path: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class INetFwProducts(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('39eb36e0-2097-40bd-8a-f2-63-a1-3b-52-53-62')
    @commethod(7)
    def get_Count(count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Register(product: Windows.Win32.NetworkManagement.WindowsFirewall.INetFwProduct_head, registration: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Item(index: Int32, product: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INetFwProduct_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get__NewEnum(newEnum: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class INetFwProfile(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('174a0dda-e9f9-449d-99-3b-21-ab-66-7c-a4-56')
    @commethod(7)
    def get_Type(type: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_FirewallEnabled(enabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_FirewallEnabled(enabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ExceptionsNotAllowed(notAllowed: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_ExceptionsNotAllowed(notAllowed: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_NotificationsDisabled(disabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_NotificationsDisabled(disabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_UnicastResponsesToMulticastBroadcastDisabled(disabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_UnicastResponsesToMulticastBroadcastDisabled(disabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_RemoteAdminSettings(remoteAdminSettings: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INetFwRemoteAdminSettings_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_IcmpSettings(icmpSettings: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INetFwIcmpSettings_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_GloballyOpenPorts(openPorts: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INetFwOpenPorts_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_Services(services: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INetFwServices_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_AuthorizedApplications(apps: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INetFwAuthorizedApplications_head)) -> Windows.Win32.Foundation.HRESULT: ...
class INetFwRemoteAdminSettings(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('d4becddf-6f73-4a83-b8-32-9c-66-87-4c-d2-0e')
    @commethod(7)
    def get_IpVersion(ipVersion: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_IpVersion(ipVersion: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Scope(scope: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_SCOPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Scope(scope: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_SCOPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_RemoteAddresses(remoteAddrs: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_RemoteAddresses(remoteAddrs: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Enabled(enabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Enabled(enabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class INetFwRule(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('af230d27-baba-4e42-ac-ed-f5-24-f2-2c-fc-e2')
    @commethod(7)
    def get_Name(name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Name(name: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Description(desc: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Description(desc: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ApplicationName(imageFileName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_ApplicationName(imageFileName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_ServiceName(serviceName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_ServiceName(serviceName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Protocol(protocol: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Protocol(protocol: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_LocalPorts(portNumbers: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_LocalPorts(portNumbers: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_RemotePorts(portNumbers: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_RemotePorts(portNumbers: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_LocalAddresses(localAddrs: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_LocalAddresses(localAddrs: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_RemoteAddresses(remoteAddrs: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_RemoteAddresses(remoteAddrs: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_IcmpTypesAndCodes(icmpTypesAndCodes: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_IcmpTypesAndCodes(icmpTypesAndCodes: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_Direction(dir: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_RULE_DIRECTION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_Direction(dir: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_RULE_DIRECTION) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_Interfaces(interfaces: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_Interfaces(interfaces: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_InterfaceTypes(interfaceTypes: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_InterfaceTypes(interfaceTypes: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_Enabled(enabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_Enabled(enabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_Grouping(context: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def put_Grouping(context: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_Profiles(profileTypesBitmask: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def put_Profiles(profileTypesBitmask: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_EdgeTraversal(enabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def put_EdgeTraversal(enabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def get_Action(action: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_ACTION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def put_Action(action: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_ACTION) -> Windows.Win32.Foundation.HRESULT: ...
class INetFwRule2(c_void_p):
    extends: Windows.Win32.NetworkManagement.WindowsFirewall.INetFwRule
    Guid = Guid('9c27c8da-189b-4dde-89-f7-8b-39-a3-16-78-2c')
    @commethod(43)
    def get_EdgeTraversalOptions(lOptions: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def put_EdgeTraversalOptions(lOptions: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class INetFwRule3(c_void_p):
    extends: Windows.Win32.NetworkManagement.WindowsFirewall.INetFwRule2
    Guid = Guid('b21563ff-d696-4222-ab-46-4e-89-b7-3a-b3-4a')
    @commethod(45)
    def get_LocalAppPackageId(wszPackageId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def put_LocalAppPackageId(wszPackageId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def get_LocalUserOwner(wszUserOwner: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def put_LocalUserOwner(wszUserOwner: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def get_LocalUserAuthorizedList(wszUserAuthList: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def put_LocalUserAuthorizedList(wszUserAuthList: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def get_RemoteUserAuthorizedList(wszUserAuthList: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def put_RemoteUserAuthorizedList(wszUserAuthList: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def get_RemoteMachineAuthorizedList(wszUserAuthList: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def put_RemoteMachineAuthorizedList(wszUserAuthList: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def get_SecureFlags(lOptions: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def put_SecureFlags(lOptions: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class INetFwRules(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('9c4c6277-5027-441e-af-ae-ca-1f-54-2d-a0-09')
    @commethod(7)
    def get_Count(count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Add(rule: Windows.Win32.NetworkManagement.WindowsFirewall.INetFwRule_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Remove(name: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Item(name: Windows.Win32.Foundation.BSTR, rule: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INetFwRule_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get__NewEnum(newEnum: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class INetFwService(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('79fd57c8-908e-4a36-98-88-d5-b3-f0-a4-44-cf')
    @commethod(7)
    def get_Name(name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Type(type: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_SERVICE_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Customized(customized: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_IpVersion(ipVersion: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_IpVersion(ipVersion: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Scope(scope: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_SCOPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_Scope(scope: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_SCOPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_RemoteAddresses(remoteAddrs: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_RemoteAddresses(remoteAddrs: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Enabled(enabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_Enabled(enabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_GloballyOpenPorts(openPorts: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INetFwOpenPorts_head)) -> Windows.Win32.Foundation.HRESULT: ...
class INetFwServiceRestriction(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('8267bbe3-f890-491c-b7-b6-2d-b1-ef-0e-5d-2b')
    @commethod(7)
    def RestrictService(serviceName: Windows.Win32.Foundation.BSTR, appName: Windows.Win32.Foundation.BSTR, restrictService: Windows.Win32.Foundation.VARIANT_BOOL, serviceSidRestricted: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ServiceRestricted(serviceName: Windows.Win32.Foundation.BSTR, appName: Windows.Win32.Foundation.BSTR, serviceRestricted: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Rules(rules: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INetFwRules_head)) -> Windows.Win32.Foundation.HRESULT: ...
class INetFwServices(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('79649bb4-903e-421b-94-c9-79-84-8e-79-f6-ee')
    @commethod(7)
    def get_Count(count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(svcType: Windows.Win32.NetworkManagement.WindowsFirewall.NET_FW_SERVICE_TYPE, service: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INetFwService_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(newEnum: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class INetSharingConfiguration(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('c08956b6-1cd3-11d1-b1-c5-00-80-5f-c1-27-0e')
    @commethod(7)
    def get_SharingEnabled(pbEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_SharingConnectionType(pType: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.SHARINGCONNECTIONTYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def DisableSharing() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EnableSharing(Type: Windows.Win32.NetworkManagement.WindowsFirewall.SHARINGCONNECTIONTYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_InternetFirewallEnabled(pbEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DisableInternetFirewall() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def EnableInternetFirewall() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_EnumPortMappings(Flags: Windows.Win32.NetworkManagement.WindowsFirewall.SHARINGCONNECTION_ENUM_FLAGS, ppColl: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INetSharingPortMappingCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def AddPortMapping(bstrName: Windows.Win32.Foundation.BSTR, ucIPProtocol: Byte, usExternalPort: UInt16, usInternalPort: UInt16, dwOptions: UInt32, bstrTargetNameOrIPAddress: Windows.Win32.Foundation.BSTR, eTargetType: Windows.Win32.NetworkManagement.WindowsFirewall.ICS_TARGETTYPE, ppMapping: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INetSharingPortMapping_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def RemovePortMapping(pMapping: Windows.Win32.NetworkManagement.WindowsFirewall.INetSharingPortMapping_head) -> Windows.Win32.Foundation.HRESULT: ...
class INetSharingEveryConnectionCollection(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('33c4643c-7811-46fa-a8-9a-76-85-97-bd-72-23')
    @commethod(7)
    def get__NewEnum(pVal: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class INetSharingManager(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('c08956b7-1cd3-11d1-b1-c5-00-80-5f-c1-27-0e')
    @commethod(7)
    def get_SharingInstalled(pbInstalled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_EnumPublicConnections(Flags: Windows.Win32.NetworkManagement.WindowsFirewall.SHARINGCONNECTION_ENUM_FLAGS, ppColl: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INetSharingPublicConnectionCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_EnumPrivateConnections(Flags: Windows.Win32.NetworkManagement.WindowsFirewall.SHARINGCONNECTION_ENUM_FLAGS, ppColl: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INetSharingPrivateConnectionCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_INetSharingConfigurationForINetConnection(pNetConnection: Windows.Win32.NetworkManagement.WindowsFirewall.INetConnection_head, ppNetSharingConfiguration: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INetSharingConfiguration_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_EnumEveryConnection(ppColl: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INetSharingEveryConnectionCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_NetConnectionProps(pNetConnection: Windows.Win32.NetworkManagement.WindowsFirewall.INetConnection_head, ppProps: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INetConnectionProps_head)) -> Windows.Win32.Foundation.HRESULT: ...
class INetSharingPortMapping(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('c08956b1-1cd3-11d1-b1-c5-00-80-5f-c1-27-0e')
    @commethod(7)
    def Disable() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Enable() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Properties(ppNSPMP: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INetSharingPortMappingProps_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Delete() -> Windows.Win32.Foundation.HRESULT: ...
class INetSharingPortMappingCollection(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('02e4a2de-da20-4e34-89-c8-ac-22-27-5a-01-0b')
    @commethod(7)
    def get__NewEnum(pVal: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class INetSharingPortMappingProps(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('24b7e9b5-e38f-4685-85-1b-00-89-2c-f5-f9-40')
    @commethod(7)
    def get_Name(pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_IPProtocol(pucIPProt: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ExternalPort(pusPort: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_InternalPort(pusPort: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Options(pdwOptions: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_TargetName(pbstrTargetName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_TargetIPAddress(pbstrTargetIPAddress: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Enabled(pbool: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class INetSharingPrivateConnectionCollection(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('38ae69e0-4409-402a-a2-cb-e9-65-c7-27-f8-40')
    @commethod(7)
    def get__NewEnum(pVal: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class INetSharingPublicConnectionCollection(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('7d7a6355-f372-4971-a1-49-bf-c9-27-be-76-2a')
    @commethod(7)
    def get__NewEnum(pVal: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IStaticPortMapping(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('6f10711f-729b-41e5-93-b8-f2-1d-0f-81-8d-f1')
    @commethod(7)
    def get_ExternalIPAddress(pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ExternalPort(pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_InternalPort(pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Protocol(pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_InternalClient(pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Enabled(pVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Description(pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def EditInternalClient(bstrInternalClient: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Enable(vb: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def EditDescription(bstrDescription: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def EditInternalPort(lInternalPort: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IStaticPortMappingCollection(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('cd1f3e77-66d6-4664-82-c7-36-db-b6-41-d0-f1')
    @commethod(7)
    def get__NewEnum(pVal: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(lExternalPort: Int32, bstrProtocol: Windows.Win32.Foundation.BSTR, ppSPM: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.IStaticPortMapping_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Remove(lExternalPort: Int32, bstrProtocol: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Add(lExternalPort: Int32, bstrProtocol: Windows.Win32.Foundation.BSTR, lInternalPort: Int32, bstrInternalClient: Windows.Win32.Foundation.BSTR, bEnabled: Windows.Win32.Foundation.VARIANT_BOOL, bstrDescription: Windows.Win32.Foundation.BSTR, ppSPM: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.IStaticPortMapping_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUPnPNAT(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('b171c812-cc76-485a-94-d8-b6-b3-a2-79-4e-99')
    @commethod(7)
    def get_StaticPortMappingCollection(ppSPMs: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.IStaticPortMappingCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_DynamicPortMappingCollection(ppDPMs: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.IDynamicPortMappingCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_NATEventManager(ppNEM: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INATEventManager_head)) -> Windows.Win32.Foundation.HRESULT: ...
NETCONMGR_ENUM_FLAGS = Int32
NCME_DEFAULT: NETCONMGR_ENUM_FLAGS = 0
NCME_HIDDEN: NETCONMGR_ENUM_FLAGS = 1
NETCONUI_CONNECT_FLAGS = Int32
NCUC_DEFAULT: NETCONUI_CONNECT_FLAGS = 0
NCUC_NO_UI: NETCONUI_CONNECT_FLAGS = 1
NCUC_ENABLE_DISABLE: NETCONUI_CONNECT_FLAGS = 2
NETCON_CHARACTERISTIC_FLAGS = Int32
NCCF_NONE: NETCON_CHARACTERISTIC_FLAGS = 0
NCCF_ALL_USERS: NETCON_CHARACTERISTIC_FLAGS = 1
NCCF_ALLOW_DUPLICATION: NETCON_CHARACTERISTIC_FLAGS = 2
NCCF_ALLOW_REMOVAL: NETCON_CHARACTERISTIC_FLAGS = 4
NCCF_ALLOW_RENAME: NETCON_CHARACTERISTIC_FLAGS = 8
NCCF_INCOMING_ONLY: NETCON_CHARACTERISTIC_FLAGS = 32
NCCF_OUTGOING_ONLY: NETCON_CHARACTERISTIC_FLAGS = 64
NCCF_BRANDED: NETCON_CHARACTERISTIC_FLAGS = 128
NCCF_SHARED: NETCON_CHARACTERISTIC_FLAGS = 256
NCCF_BRIDGED: NETCON_CHARACTERISTIC_FLAGS = 512
NCCF_FIREWALLED: NETCON_CHARACTERISTIC_FLAGS = 1024
NCCF_DEFAULT: NETCON_CHARACTERISTIC_FLAGS = 2048
NCCF_HOMENET_CAPABLE: NETCON_CHARACTERISTIC_FLAGS = 4096
NCCF_SHARED_PRIVATE: NETCON_CHARACTERISTIC_FLAGS = 8192
NCCF_QUARANTINED: NETCON_CHARACTERISTIC_FLAGS = 16384
NCCF_RESERVED: NETCON_CHARACTERISTIC_FLAGS = 32768
NCCF_HOSTED_NETWORK: NETCON_CHARACTERISTIC_FLAGS = 65536
NCCF_VIRTUAL_STATION: NETCON_CHARACTERISTIC_FLAGS = 131072
NCCF_WIFI_DIRECT: NETCON_CHARACTERISTIC_FLAGS = 262144
NCCF_BLUETOOTH_MASK: NETCON_CHARACTERISTIC_FLAGS = 983040
NCCF_LAN_MASK: NETCON_CHARACTERISTIC_FLAGS = 15728640
NETCON_MEDIATYPE = Int32
NCM_NONE: NETCON_MEDIATYPE = 0
NCM_DIRECT: NETCON_MEDIATYPE = 1
NCM_ISDN: NETCON_MEDIATYPE = 2
NCM_LAN: NETCON_MEDIATYPE = 3
NCM_PHONE: NETCON_MEDIATYPE = 4
NCM_TUNNEL: NETCON_MEDIATYPE = 5
NCM_PPPOE: NETCON_MEDIATYPE = 6
NCM_BRIDGE: NETCON_MEDIATYPE = 7
NCM_SHAREDACCESSHOST_LAN: NETCON_MEDIATYPE = 8
NCM_SHAREDACCESSHOST_RAS: NETCON_MEDIATYPE = 9
class NETCON_PROPERTIES(Structure):
    guidId: Guid
    pszwName: Windows.Win32.Foundation.PWSTR
    pszwDeviceName: Windows.Win32.Foundation.PWSTR
    Status: Windows.Win32.NetworkManagement.WindowsFirewall.NETCON_STATUS
    MediaType: Windows.Win32.NetworkManagement.WindowsFirewall.NETCON_MEDIATYPE
    dwCharacter: UInt32
    clsidThisObject: Guid
    clsidUiObject: Guid
NETCON_STATUS = Int32
NCS_DISCONNECTED: NETCON_STATUS = 0
NCS_CONNECTING: NETCON_STATUS = 1
NCS_CONNECTED: NETCON_STATUS = 2
NCS_DISCONNECTING: NETCON_STATUS = 3
NCS_HARDWARE_NOT_PRESENT: NETCON_STATUS = 4
NCS_HARDWARE_DISABLED: NETCON_STATUS = 5
NCS_HARDWARE_MALFUNCTION: NETCON_STATUS = 6
NCS_MEDIA_DISCONNECTED: NETCON_STATUS = 7
NCS_AUTHENTICATING: NETCON_STATUS = 8
NCS_AUTHENTICATION_SUCCEEDED: NETCON_STATUS = 9
NCS_AUTHENTICATION_FAILED: NETCON_STATUS = 10
NCS_INVALID_ADDRESS: NETCON_STATUS = 11
NCS_CREDENTIALS_REQUIRED: NETCON_STATUS = 12
NCS_ACTION_REQUIRED: NETCON_STATUS = 13
NCS_ACTION_REQUIRED_RETRY: NETCON_STATUS = 14
NCS_CONNECT_FAILED: NETCON_STATUS = 15
NETCON_TYPE = Int32
NCT_DIRECT_CONNECT: NETCON_TYPE = 0
NCT_INBOUND: NETCON_TYPE = 1
NCT_INTERNET: NETCON_TYPE = 2
NCT_LAN: NETCON_TYPE = 3
NCT_PHONE: NETCON_TYPE = 4
NCT_TUNNEL: NETCON_TYPE = 5
NCT_BRIDGE: NETCON_TYPE = 6
NETISO_ERROR_TYPE = Int32
NETISO_ERROR_TYPE_NONE: NETISO_ERROR_TYPE = 0
NETISO_ERROR_TYPE_PRIVATE_NETWORK: NETISO_ERROR_TYPE = 1
NETISO_ERROR_TYPE_INTERNET_CLIENT: NETISO_ERROR_TYPE = 2
NETISO_ERROR_TYPE_INTERNET_CLIENT_SERVER: NETISO_ERROR_TYPE = 3
NETISO_ERROR_TYPE_MAX: NETISO_ERROR_TYPE = 4
NETISO_FLAG = Int32
NETISO_FLAG_FORCE_COMPUTE_BINARIES: NETISO_FLAG = 1
NETISO_FLAG_MAX: NETISO_FLAG = 2
NET_FW_ACTION = Int32
NET_FW_ACTION_BLOCK: NET_FW_ACTION = 0
NET_FW_ACTION_ALLOW: NET_FW_ACTION = 1
NET_FW_ACTION_MAX: NET_FW_ACTION = 2
NET_FW_AUTHENTICATE_TYPE = Int32
NET_FW_AUTHENTICATE_NONE: NET_FW_AUTHENTICATE_TYPE = 0
NET_FW_AUTHENTICATE_NO_ENCAPSULATION: NET_FW_AUTHENTICATE_TYPE = 1
NET_FW_AUTHENTICATE_WITH_INTEGRITY: NET_FW_AUTHENTICATE_TYPE = 2
NET_FW_AUTHENTICATE_AND_NEGOTIATE_ENCRYPTION: NET_FW_AUTHENTICATE_TYPE = 3
NET_FW_AUTHENTICATE_AND_ENCRYPT: NET_FW_AUTHENTICATE_TYPE = 4
NET_FW_EDGE_TRAVERSAL_TYPE = Int32
NET_FW_EDGE_TRAVERSAL_TYPE_DENY: NET_FW_EDGE_TRAVERSAL_TYPE = 0
NET_FW_EDGE_TRAVERSAL_TYPE_ALLOW: NET_FW_EDGE_TRAVERSAL_TYPE = 1
NET_FW_EDGE_TRAVERSAL_TYPE_DEFER_TO_APP: NET_FW_EDGE_TRAVERSAL_TYPE = 2
NET_FW_EDGE_TRAVERSAL_TYPE_DEFER_TO_USER: NET_FW_EDGE_TRAVERSAL_TYPE = 3
NET_FW_IP_PROTOCOL = Int32
NET_FW_IP_PROTOCOL_TCP: NET_FW_IP_PROTOCOL = 6
NET_FW_IP_PROTOCOL_UDP: NET_FW_IP_PROTOCOL = 17
NET_FW_IP_PROTOCOL_ANY: NET_FW_IP_PROTOCOL = 256
NET_FW_IP_VERSION = Int32
NET_FW_IP_VERSION_V4: NET_FW_IP_VERSION = 0
NET_FW_IP_VERSION_V6: NET_FW_IP_VERSION = 1
NET_FW_IP_VERSION_ANY: NET_FW_IP_VERSION = 2
NET_FW_IP_VERSION_MAX: NET_FW_IP_VERSION = 3
NET_FW_MODIFY_STATE = Int32
NET_FW_MODIFY_STATE_OK: NET_FW_MODIFY_STATE = 0
NET_FW_MODIFY_STATE_GP_OVERRIDE: NET_FW_MODIFY_STATE = 1
NET_FW_MODIFY_STATE_INBOUND_BLOCKED: NET_FW_MODIFY_STATE = 2
NET_FW_POLICY_TYPE = Int32
NET_FW_POLICY_GROUP: NET_FW_POLICY_TYPE = 0
NET_FW_POLICY_LOCAL: NET_FW_POLICY_TYPE = 1
NET_FW_POLICY_EFFECTIVE: NET_FW_POLICY_TYPE = 2
NET_FW_POLICY_TYPE_MAX: NET_FW_POLICY_TYPE = 3
NET_FW_PROFILE_TYPE = Int32
NET_FW_PROFILE_DOMAIN: NET_FW_PROFILE_TYPE = 0
NET_FW_PROFILE_STANDARD: NET_FW_PROFILE_TYPE = 1
NET_FW_PROFILE_CURRENT: NET_FW_PROFILE_TYPE = 2
NET_FW_PROFILE_TYPE_MAX: NET_FW_PROFILE_TYPE = 3
NET_FW_PROFILE_TYPE2 = Int32
NET_FW_PROFILE2_DOMAIN: NET_FW_PROFILE_TYPE2 = 1
NET_FW_PROFILE2_PRIVATE: NET_FW_PROFILE_TYPE2 = 2
NET_FW_PROFILE2_PUBLIC: NET_FW_PROFILE_TYPE2 = 4
NET_FW_PROFILE2_ALL: NET_FW_PROFILE_TYPE2 = 2147483647
NET_FW_RULE_CATEGORY = Int32
NET_FW_RULE_CATEGORY_BOOT: NET_FW_RULE_CATEGORY = 0
NET_FW_RULE_CATEGORY_STEALTH: NET_FW_RULE_CATEGORY = 1
NET_FW_RULE_CATEGORY_FIREWALL: NET_FW_RULE_CATEGORY = 2
NET_FW_RULE_CATEGORY_CONSEC: NET_FW_RULE_CATEGORY = 3
NET_FW_RULE_CATEGORY_MAX: NET_FW_RULE_CATEGORY = 4
NET_FW_RULE_DIRECTION = Int32
NET_FW_RULE_DIR_IN: NET_FW_RULE_DIRECTION = 1
NET_FW_RULE_DIR_OUT: NET_FW_RULE_DIRECTION = 2
NET_FW_RULE_DIR_MAX: NET_FW_RULE_DIRECTION = 3
NET_FW_SCOPE = Int32
NET_FW_SCOPE_ALL: NET_FW_SCOPE = 0
NET_FW_SCOPE_LOCAL_SUBNET: NET_FW_SCOPE = 1
NET_FW_SCOPE_CUSTOM: NET_FW_SCOPE = 2
NET_FW_SCOPE_MAX: NET_FW_SCOPE = 3
NET_FW_SERVICE_TYPE = Int32
NET_FW_SERVICE_FILE_AND_PRINT: NET_FW_SERVICE_TYPE = 0
NET_FW_SERVICE_UPNP: NET_FW_SERVICE_TYPE = 1
NET_FW_SERVICE_REMOTE_DESKTOP: NET_FW_SERVICE_TYPE = 2
NET_FW_SERVICE_NONE: NET_FW_SERVICE_TYPE = 3
NET_FW_SERVICE_TYPE_MAX: NET_FW_SERVICE_TYPE = 4
NetFwAuthorizedApplication = Guid('ec9846b3-2762-4a6b-a2-14-6a-cb-60-34-62-d2')
NetFwMgr = Guid('304ce942-6e39-40d8-94-3a-b9-13-c4-0c-9c-d4')
NetFwOpenPort = Guid('0ca545c6-37ad-4a6c-bf-92-9f-76-10-06-7e-f5')
NetFwPolicy2 = Guid('e2b3c97f-6ae1-41ac-81-7a-f6-f9-21-66-d7-dd')
NetFwProduct = Guid('9d745ed8-c514-4d1d-bf-42-75-1f-ed-2d-5a-c7')
NetFwProducts = Guid('cc19079b-8272-4d73-bb-70-cd-b5-33-52-7b-61')
NetFwRule = Guid('2c5bc43e-3369-4c33-ab-0c-be-94-69-67-7a-f4')
NetSharingManager = Guid('5c63c1ad-3956-4ff8-84-86-40-03-47-58-31-5b')
@winfunctype_pointer
def PAC_CHANGES_CALLBACK_FN(context: c_void_p, pChange: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_CHANGE_head)) -> Void: ...
@winfunctype_pointer
def PFN_FWADDDYNAMICKEYWORDADDRESS0(dynamicKeywordAddress: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.FW_DYNAMIC_KEYWORD_ADDRESS0_head)) -> UInt32: ...
@winfunctype_pointer
def PFN_FWDELETEDYNAMICKEYWORDADDRESS0(dynamicKeywordAddressId: Guid) -> UInt32: ...
@winfunctype_pointer
def PFN_FWENUMDYNAMICKEYWORDADDRESSBYID0(dynamicKeywordAddressId: Guid, dynamicKeywordAddressData: POINTER(POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.FW_DYNAMIC_KEYWORD_ADDRESS_DATA0_head))) -> UInt32: ...
@winfunctype_pointer
def PFN_FWENUMDYNAMICKEYWORDADDRESSESBYTYPE0(flags: UInt32, dynamicKeywordAddressData: POINTER(POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.FW_DYNAMIC_KEYWORD_ADDRESS_DATA0_head))) -> UInt32: ...
@winfunctype_pointer
def PFN_FWFREEDYNAMICKEYWORDADDRESSDATA0(dynamicKeywordAddressData: POINTER(Windows.Win32.NetworkManagement.WindowsFirewall.FW_DYNAMIC_KEYWORD_ADDRESS_DATA0_head)) -> UInt32: ...
@winfunctype_pointer
def PFN_FWUPDATEDYNAMICKEYWORDADDRESS0(dynamicKeywordAddressId: Guid, updatedAddresses: Windows.Win32.Foundation.PWSTR, append: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype_pointer
def PNETISO_EDP_ID_CALLBACK_FN(context: c_void_p, wszEnterpriseId: Windows.Win32.Foundation.PWSTR, dwErr: UInt32) -> Void: ...
SHARINGCONNECTIONTYPE = Int32
ICSSHARINGTYPE_PUBLIC: SHARINGCONNECTIONTYPE = 0
ICSSHARINGTYPE_PRIVATE: SHARINGCONNECTIONTYPE = 1
SHARINGCONNECTION_ENUM_FLAGS = Int32
ICSSC_DEFAULT: SHARINGCONNECTION_ENUM_FLAGS = 0
ICSSC_ENABLED: SHARINGCONNECTION_ENUM_FLAGS = 1
UPnPNAT = Guid('ae1e00aa-3fd5-403c-8a-27-2b-bd-c3-0c-d0-e1')
make_head(_module, 'FW_DYNAMIC_KEYWORD_ADDRESS0')
make_head(_module, 'FW_DYNAMIC_KEYWORD_ADDRESS_DATA0')
make_head(_module, 'IDynamicPortMapping')
make_head(_module, 'IDynamicPortMappingCollection')
make_head(_module, 'IEnumNetConnection')
make_head(_module, 'IEnumNetSharingEveryConnection')
make_head(_module, 'IEnumNetSharingPortMapping')
make_head(_module, 'IEnumNetSharingPrivateConnection')
make_head(_module, 'IEnumNetSharingPublicConnection')
make_head(_module, 'INATEventManager')
make_head(_module, 'INATExternalIPAddressCallback')
make_head(_module, 'INATNumberOfEntriesCallback')
make_head(_module, 'INET_FIREWALL_AC_BINARIES')
make_head(_module, 'INET_FIREWALL_AC_CAPABILITIES')
make_head(_module, 'INET_FIREWALL_AC_CHANGE')
make_head(_module, 'INET_FIREWALL_APP_CONTAINER')
make_head(_module, 'INetConnection')
make_head(_module, 'INetConnectionConnectUi')
make_head(_module, 'INetConnectionManager')
make_head(_module, 'INetConnectionProps')
make_head(_module, 'INetFwAuthorizedApplication')
make_head(_module, 'INetFwAuthorizedApplications')
make_head(_module, 'INetFwIcmpSettings')
make_head(_module, 'INetFwMgr')
make_head(_module, 'INetFwOpenPort')
make_head(_module, 'INetFwOpenPorts')
make_head(_module, 'INetFwPolicy')
make_head(_module, 'INetFwPolicy2')
make_head(_module, 'INetFwProduct')
make_head(_module, 'INetFwProducts')
make_head(_module, 'INetFwProfile')
make_head(_module, 'INetFwRemoteAdminSettings')
make_head(_module, 'INetFwRule')
make_head(_module, 'INetFwRule2')
make_head(_module, 'INetFwRule3')
make_head(_module, 'INetFwRules')
make_head(_module, 'INetFwService')
make_head(_module, 'INetFwServiceRestriction')
make_head(_module, 'INetFwServices')
make_head(_module, 'INetSharingConfiguration')
make_head(_module, 'INetSharingEveryConnectionCollection')
make_head(_module, 'INetSharingManager')
make_head(_module, 'INetSharingPortMapping')
make_head(_module, 'INetSharingPortMappingCollection')
make_head(_module, 'INetSharingPortMappingProps')
make_head(_module, 'INetSharingPrivateConnectionCollection')
make_head(_module, 'INetSharingPublicConnectionCollection')
make_head(_module, 'IStaticPortMapping')
make_head(_module, 'IStaticPortMappingCollection')
make_head(_module, 'IUPnPNAT')
make_head(_module, 'NETCON_PROPERTIES')
make_head(_module, 'PAC_CHANGES_CALLBACK_FN')
make_head(_module, 'PFN_FWADDDYNAMICKEYWORDADDRESS0')
make_head(_module, 'PFN_FWDELETEDYNAMICKEYWORDADDRESS0')
make_head(_module, 'PFN_FWENUMDYNAMICKEYWORDADDRESSBYID0')
make_head(_module, 'PFN_FWENUMDYNAMICKEYWORDADDRESSESBYTYPE0')
make_head(_module, 'PFN_FWFREEDYNAMICKEYWORDADDRESSDATA0')
make_head(_module, 'PFN_FWUPDATEDYNAMICKEYWORDADDRESS0')
make_head(_module, 'PNETISO_EDP_ID_CALLBACK_FN')
__all__ = [
    "FW_DYNAMIC_KEYWORD_ADDRESS0",
    "FW_DYNAMIC_KEYWORD_ADDRESS_DATA0",
    "FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS",
    "FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS_ALL",
    "FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS_AUTO_RESOLVE",
    "FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS_NON_AUTO_RESOLVE",
    "FW_DYNAMIC_KEYWORD_ADDRESS_FLAGS",
    "FW_DYNAMIC_KEYWORD_ADDRESS_FLAGS_AUTO_RESOLVE",
    "FW_DYNAMIC_KEYWORD_ORIGIN_INVALID",
    "FW_DYNAMIC_KEYWORD_ORIGIN_LOCAL",
    "FW_DYNAMIC_KEYWORD_ORIGIN_MDM",
    "FW_DYNAMIC_KEYWORD_ORIGIN_TYPE",
    "ICSSC_DEFAULT",
    "ICSSC_ENABLED",
    "ICSSHARINGTYPE_PRIVATE",
    "ICSSHARINGTYPE_PUBLIC",
    "ICSTT_IPADDRESS",
    "ICSTT_NAME",
    "ICS_TARGETTYPE",
    "IDynamicPortMapping",
    "IDynamicPortMappingCollection",
    "IEnumNetConnection",
    "IEnumNetSharingEveryConnection",
    "IEnumNetSharingPortMapping",
    "IEnumNetSharingPrivateConnection",
    "IEnumNetSharingPublicConnection",
    "INATEventManager",
    "INATExternalIPAddressCallback",
    "INATNumberOfEntriesCallback",
    "INET_FIREWALL_AC_BINARIES",
    "INET_FIREWALL_AC_BINARY",
    "INET_FIREWALL_AC_CAPABILITIES",
    "INET_FIREWALL_AC_CHANGE",
    "INET_FIREWALL_AC_CHANGE_CREATE",
    "INET_FIREWALL_AC_CHANGE_DELETE",
    "INET_FIREWALL_AC_CHANGE_INVALID",
    "INET_FIREWALL_AC_CHANGE_MAX",
    "INET_FIREWALL_AC_CHANGE_TYPE",
    "INET_FIREWALL_AC_CREATION_TYPE",
    "INET_FIREWALL_AC_MAX",
    "INET_FIREWALL_AC_NONE",
    "INET_FIREWALL_AC_PACKAGE_ID_ONLY",
    "INET_FIREWALL_APP_CONTAINER",
    "INetConnection",
    "INetConnectionConnectUi",
    "INetConnectionManager",
    "INetConnectionProps",
    "INetFwAuthorizedApplication",
    "INetFwAuthorizedApplications",
    "INetFwIcmpSettings",
    "INetFwMgr",
    "INetFwOpenPort",
    "INetFwOpenPorts",
    "INetFwPolicy",
    "INetFwPolicy2",
    "INetFwProduct",
    "INetFwProducts",
    "INetFwProfile",
    "INetFwRemoteAdminSettings",
    "INetFwRule",
    "INetFwRule2",
    "INetFwRule3",
    "INetFwRules",
    "INetFwService",
    "INetFwServiceRestriction",
    "INetFwServices",
    "INetSharingConfiguration",
    "INetSharingEveryConnectionCollection",
    "INetSharingManager",
    "INetSharingPortMapping",
    "INetSharingPortMappingCollection",
    "INetSharingPortMappingProps",
    "INetSharingPrivateConnectionCollection",
    "INetSharingPublicConnectionCollection",
    "IStaticPortMapping",
    "IStaticPortMappingCollection",
    "IUPnPNAT",
    "NCCF_ALLOW_DUPLICATION",
    "NCCF_ALLOW_REMOVAL",
    "NCCF_ALLOW_RENAME",
    "NCCF_ALL_USERS",
    "NCCF_BLUETOOTH_MASK",
    "NCCF_BRANDED",
    "NCCF_BRIDGED",
    "NCCF_DEFAULT",
    "NCCF_FIREWALLED",
    "NCCF_HOMENET_CAPABLE",
    "NCCF_HOSTED_NETWORK",
    "NCCF_INCOMING_ONLY",
    "NCCF_LAN_MASK",
    "NCCF_NONE",
    "NCCF_OUTGOING_ONLY",
    "NCCF_QUARANTINED",
    "NCCF_RESERVED",
    "NCCF_SHARED",
    "NCCF_SHARED_PRIVATE",
    "NCCF_VIRTUAL_STATION",
    "NCCF_WIFI_DIRECT",
    "NCME_DEFAULT",
    "NCME_HIDDEN",
    "NCM_BRIDGE",
    "NCM_DIRECT",
    "NCM_ISDN",
    "NCM_LAN",
    "NCM_NONE",
    "NCM_PHONE",
    "NCM_PPPOE",
    "NCM_SHAREDACCESSHOST_LAN",
    "NCM_SHAREDACCESSHOST_RAS",
    "NCM_TUNNEL",
    "NCS_ACTION_REQUIRED",
    "NCS_ACTION_REQUIRED_RETRY",
    "NCS_AUTHENTICATING",
    "NCS_AUTHENTICATION_FAILED",
    "NCS_AUTHENTICATION_SUCCEEDED",
    "NCS_CONNECTED",
    "NCS_CONNECTING",
    "NCS_CONNECT_FAILED",
    "NCS_CREDENTIALS_REQUIRED",
    "NCS_DISCONNECTED",
    "NCS_DISCONNECTING",
    "NCS_HARDWARE_DISABLED",
    "NCS_HARDWARE_MALFUNCTION",
    "NCS_HARDWARE_NOT_PRESENT",
    "NCS_INVALID_ADDRESS",
    "NCS_MEDIA_DISCONNECTED",
    "NCT_BRIDGE",
    "NCT_DIRECT_CONNECT",
    "NCT_INBOUND",
    "NCT_INTERNET",
    "NCT_LAN",
    "NCT_PHONE",
    "NCT_TUNNEL",
    "NCUC_DEFAULT",
    "NCUC_ENABLE_DISABLE",
    "NCUC_NO_UI",
    "NETCONMGR_ENUM_FLAGS",
    "NETCONUI_CONNECT_FLAGS",
    "NETCON_CHARACTERISTIC_FLAGS",
    "NETCON_MAX_NAME_LEN",
    "NETCON_MEDIATYPE",
    "NETCON_PROPERTIES",
    "NETCON_STATUS",
    "NETCON_TYPE",
    "NETISO_ERROR_TYPE",
    "NETISO_ERROR_TYPE_INTERNET_CLIENT",
    "NETISO_ERROR_TYPE_INTERNET_CLIENT_SERVER",
    "NETISO_ERROR_TYPE_MAX",
    "NETISO_ERROR_TYPE_NONE",
    "NETISO_ERROR_TYPE_PRIVATE_NETWORK",
    "NETISO_FLAG",
    "NETISO_FLAG_FORCE_COMPUTE_BINARIES",
    "NETISO_FLAG_MAX",
    "NETISO_GEID_FOR_NEUTRAL_AWARE",
    "NETISO_GEID_FOR_WDAG",
    "NET_FW_ACTION",
    "NET_FW_ACTION_ALLOW",
    "NET_FW_ACTION_BLOCK",
    "NET_FW_ACTION_MAX",
    "NET_FW_AUTHENTICATE_AND_ENCRYPT",
    "NET_FW_AUTHENTICATE_AND_NEGOTIATE_ENCRYPTION",
    "NET_FW_AUTHENTICATE_NONE",
    "NET_FW_AUTHENTICATE_NO_ENCAPSULATION",
    "NET_FW_AUTHENTICATE_TYPE",
    "NET_FW_AUTHENTICATE_WITH_INTEGRITY",
    "NET_FW_EDGE_TRAVERSAL_TYPE",
    "NET_FW_EDGE_TRAVERSAL_TYPE_ALLOW",
    "NET_FW_EDGE_TRAVERSAL_TYPE_DEFER_TO_APP",
    "NET_FW_EDGE_TRAVERSAL_TYPE_DEFER_TO_USER",
    "NET_FW_EDGE_TRAVERSAL_TYPE_DENY",
    "NET_FW_IP_PROTOCOL",
    "NET_FW_IP_PROTOCOL_ANY",
    "NET_FW_IP_PROTOCOL_TCP",
    "NET_FW_IP_PROTOCOL_UDP",
    "NET_FW_IP_VERSION",
    "NET_FW_IP_VERSION_ANY",
    "NET_FW_IP_VERSION_MAX",
    "NET_FW_IP_VERSION_V4",
    "NET_FW_IP_VERSION_V6",
    "NET_FW_MODIFY_STATE",
    "NET_FW_MODIFY_STATE_GP_OVERRIDE",
    "NET_FW_MODIFY_STATE_INBOUND_BLOCKED",
    "NET_FW_MODIFY_STATE_OK",
    "NET_FW_POLICY_EFFECTIVE",
    "NET_FW_POLICY_GROUP",
    "NET_FW_POLICY_LOCAL",
    "NET_FW_POLICY_TYPE",
    "NET_FW_POLICY_TYPE_MAX",
    "NET_FW_PROFILE2_ALL",
    "NET_FW_PROFILE2_DOMAIN",
    "NET_FW_PROFILE2_PRIVATE",
    "NET_FW_PROFILE2_PUBLIC",
    "NET_FW_PROFILE_CURRENT",
    "NET_FW_PROFILE_DOMAIN",
    "NET_FW_PROFILE_STANDARD",
    "NET_FW_PROFILE_TYPE",
    "NET_FW_PROFILE_TYPE2",
    "NET_FW_PROFILE_TYPE_MAX",
    "NET_FW_RULE_CATEGORY",
    "NET_FW_RULE_CATEGORY_BOOT",
    "NET_FW_RULE_CATEGORY_CONSEC",
    "NET_FW_RULE_CATEGORY_FIREWALL",
    "NET_FW_RULE_CATEGORY_MAX",
    "NET_FW_RULE_CATEGORY_STEALTH",
    "NET_FW_RULE_DIRECTION",
    "NET_FW_RULE_DIR_IN",
    "NET_FW_RULE_DIR_MAX",
    "NET_FW_RULE_DIR_OUT",
    "NET_FW_SCOPE",
    "NET_FW_SCOPE_ALL",
    "NET_FW_SCOPE_CUSTOM",
    "NET_FW_SCOPE_LOCAL_SUBNET",
    "NET_FW_SCOPE_MAX",
    "NET_FW_SERVICE_FILE_AND_PRINT",
    "NET_FW_SERVICE_NONE",
    "NET_FW_SERVICE_REMOTE_DESKTOP",
    "NET_FW_SERVICE_TYPE",
    "NET_FW_SERVICE_TYPE_MAX",
    "NET_FW_SERVICE_UPNP",
    "NetFwAuthorizedApplication",
    "NetFwMgr",
    "NetFwOpenPort",
    "NetFwPolicy2",
    "NetFwProduct",
    "NetFwProducts",
    "NetFwRule",
    "NetSharingManager",
    "NetworkIsolationDiagnoseConnectFailureAndGetInfo",
    "NetworkIsolationEnumAppContainers",
    "NetworkIsolationFreeAppContainers",
    "NetworkIsolationGetAppContainerConfig",
    "NetworkIsolationRegisterForAppContainerChanges",
    "NetworkIsolationSetAppContainerConfig",
    "NetworkIsolationSetupAppContainerBinaries",
    "NetworkIsolationUnregisterForAppContainerChanges",
    "PAC_CHANGES_CALLBACK_FN",
    "PFN_FWADDDYNAMICKEYWORDADDRESS0",
    "PFN_FWDELETEDYNAMICKEYWORDADDRESS0",
    "PFN_FWENUMDYNAMICKEYWORDADDRESSBYID0",
    "PFN_FWENUMDYNAMICKEYWORDADDRESSESBYTYPE0",
    "PFN_FWFREEDYNAMICKEYWORDADDRESSDATA0",
    "PFN_FWUPDATEDYNAMICKEYWORDADDRESS0",
    "PNETISO_EDP_ID_CALLBACK_FN",
    "SHARINGCONNECTIONTYPE",
    "SHARINGCONNECTION_ENUM_FLAGS",
    "S_OBJECT_NO_LONGER_VALID",
    "UPnPNAT",
]
_arch_optional = [
]
