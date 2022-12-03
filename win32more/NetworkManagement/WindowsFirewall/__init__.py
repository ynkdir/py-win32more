from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.NetworkManagement.WindowsFirewall
import win32more.Security
import win32more.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
NETCON_MAX_NAME_LEN = 256
S_OBJECT_NO_LONGER_VALID = 2
NETISO_GEID_FOR_WDAG = 1
NETISO_GEID_FOR_NEUTRAL_AWARE = 2
def _define_NetworkIsolationSetupAppContainerBinaries():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSID,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,POINTER(win32more.Foundation.PWSTR),UInt32)(('NetworkIsolationSetupAppContainerBinaries', windll['api-ms-win-net-isolation-l1-1-0.dll']), ((1, 'applicationContainerSid'),(1, 'packageFullName'),(1, 'packageFolder'),(1, 'displayName'),(1, 'bBinariesFullyComputed'),(1, 'binaries'),(1, 'binariesCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetworkIsolationRegisterForAppContainerChanges():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.NetworkManagement.WindowsFirewall.PAC_CHANGES_CALLBACK_FN,c_void_p,POINTER(win32more.Foundation.HANDLE))(('NetworkIsolationRegisterForAppContainerChanges', windll['api-ms-win-net-isolation-l1-1-0.dll']), ((1, 'flags'),(1, 'callback'),(1, 'context'),(1, 'registrationObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetworkIsolationUnregisterForAppContainerChanges():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE)(('NetworkIsolationUnregisterForAppContainerChanges', windll['api-ms-win-net-isolation-l1-1-0.dll']), ((1, 'registrationObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetworkIsolationFreeAppContainers():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.WindowsFirewall.INET_FIREWALL_APP_CONTAINER_head))(('NetworkIsolationFreeAppContainers', windll['api-ms-win-net-isolation-l1-1-0.dll']), ((1, 'pPublicAppCs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetworkIsolationEnumAppContainers():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(UInt32),POINTER(POINTER(win32more.NetworkManagement.WindowsFirewall.INET_FIREWALL_APP_CONTAINER_head)))(('NetworkIsolationEnumAppContainers', windll['api-ms-win-net-isolation-l1-1-0.dll']), ((1, 'Flags'),(1, 'pdwNumPublicAppCs'),(1, 'ppPublicAppCs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetworkIsolationGetAppContainerConfig():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),POINTER(POINTER(win32more.Security.SID_AND_ATTRIBUTES_head)))(('NetworkIsolationGetAppContainerConfig', windll['api-ms-win-net-isolation-l1-1-0.dll']), ((1, 'pdwNumPublicAppCs'),(1, 'appContainerSids'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetworkIsolationSetAppContainerConfig():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(win32more.Security.SID_AND_ATTRIBUTES_head))(('NetworkIsolationSetAppContainerConfig', windll['api-ms-win-net-isolation-l1-1-0.dll']), ((1, 'dwNumPublicAppCs'),(1, 'appContainerSids'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetworkIsolationDiagnoseConnectFailureAndGetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.WindowsFirewall.NETISO_ERROR_TYPE))(('NetworkIsolationDiagnoseConnectFailureAndGetInfo', windll['api-ms-win-net-isolation-l1-1-0.dll']), ((1, 'wszServerName'),(1, 'netIsoError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FW_DYNAMIC_KEYWORD_ADDRESS_DATA0_head():
    class FW_DYNAMIC_KEYWORD_ADDRESS_DATA0(Structure):
        pass
    return FW_DYNAMIC_KEYWORD_ADDRESS_DATA0
def _define_FW_DYNAMIC_KEYWORD_ADDRESS_DATA0():
    FW_DYNAMIC_KEYWORD_ADDRESS_DATA0 = win32more.NetworkManagement.WindowsFirewall.FW_DYNAMIC_KEYWORD_ADDRESS_DATA0_head
    FW_DYNAMIC_KEYWORD_ADDRESS_DATA0._fields_ = [
        ('dynamicKeywordAddress', win32more.NetworkManagement.WindowsFirewall.FW_DYNAMIC_KEYWORD_ADDRESS0),
        ('next', POINTER(win32more.NetworkManagement.WindowsFirewall.FW_DYNAMIC_KEYWORD_ADDRESS_DATA0_head)),
        ('schemaVersion', UInt16),
        ('originType', win32more.NetworkManagement.WindowsFirewall.FW_DYNAMIC_KEYWORD_ORIGIN_TYPE),
    ]
    return FW_DYNAMIC_KEYWORD_ADDRESS_DATA0
FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS = UInt32
FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS_AUTO_RESOLVE = 1
FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS_NON_AUTO_RESOLVE = 2
FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS_ALL = 3
FW_DYNAMIC_KEYWORD_ADDRESS_FLAGS = UInt32
FW_DYNAMIC_KEYWORD_ADDRESS_FLAGS_AUTO_RESOLVE = 1
def _define_FW_DYNAMIC_KEYWORD_ADDRESS0_head():
    class FW_DYNAMIC_KEYWORD_ADDRESS0(Structure):
        pass
    return FW_DYNAMIC_KEYWORD_ADDRESS0
def _define_FW_DYNAMIC_KEYWORD_ADDRESS0():
    FW_DYNAMIC_KEYWORD_ADDRESS0 = win32more.NetworkManagement.WindowsFirewall.FW_DYNAMIC_KEYWORD_ADDRESS0_head
    FW_DYNAMIC_KEYWORD_ADDRESS0._fields_ = [
        ('id', Guid),
        ('keyword', win32more.Foundation.PWSTR),
        ('flags', UInt32),
        ('addresses', win32more.Foundation.PWSTR),
    ]
    return FW_DYNAMIC_KEYWORD_ADDRESS0
FW_DYNAMIC_KEYWORD_ORIGIN_TYPE = Int32
FW_DYNAMIC_KEYWORD_ORIGIN_INVALID = 0
FW_DYNAMIC_KEYWORD_ORIGIN_LOCAL = 1
FW_DYNAMIC_KEYWORD_ORIGIN_MDM = 2
ICS_TARGETTYPE = Int32
ICSTT_NAME = 0
ICSTT_IPADDRESS = 1
def _define_IDynamicPortMapping_head():
    class IDynamicPortMapping(win32more.System.Com.IDispatch_head):
        Guid = Guid('4fc80282-23b6-4378-9a-27-cd-8f-17-c9-40-0c')
    return IDynamicPortMapping
def _define_IDynamicPortMapping():
    IDynamicPortMapping = win32more.NetworkManagement.WindowsFirewall.IDynamicPortMapping_head
    IDynamicPortMapping.get_ExternalIPAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_ExternalIPAddress', ((1, 'pVal'),)))
    IDynamicPortMapping.get_RemoteHost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_RemoteHost', ((1, 'pVal'),)))
    IDynamicPortMapping.get_ExternalPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_ExternalPort', ((1, 'pVal'),)))
    IDynamicPortMapping.get_Protocol = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_Protocol', ((1, 'pVal'),)))
    IDynamicPortMapping.get_InternalPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(11, 'get_InternalPort', ((1, 'pVal'),)))
    IDynamicPortMapping.get_InternalClient = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_InternalClient', ((1, 'pVal'),)))
    IDynamicPortMapping.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(13, 'get_Enabled', ((1, 'pVal'),)))
    IDynamicPortMapping.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(14, 'get_Description', ((1, 'pVal'),)))
    IDynamicPortMapping.get_LeaseDuration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(15, 'get_LeaseDuration', ((1, 'pVal'),)))
    IDynamicPortMapping.RenewLease = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32))(16, 'RenewLease', ((1, 'lLeaseDurationDesired'),(1, 'pLeaseDurationReturned'),)))
    IDynamicPortMapping.EditInternalClient = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(17, 'EditInternalClient', ((1, 'bstrInternalClient'),)))
    IDynamicPortMapping.Enable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(18, 'Enable', ((1, 'vb'),)))
    IDynamicPortMapping.EditDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(19, 'EditDescription', ((1, 'bstrDescription'),)))
    IDynamicPortMapping.EditInternalPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(20, 'EditInternalPort', ((1, 'lInternalPort'),)))
    win32more.System.Com.IDispatch
    return IDynamicPortMapping
def _define_IDynamicPortMappingCollection_head():
    class IDynamicPortMappingCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('b60de00f-156e-4e8d-9e-c1-3a-23-42-c1-08-99')
    return IDynamicPortMappingCollection
def _define_IDynamicPortMappingCollection():
    IDynamicPortMappingCollection = win32more.NetworkManagement.WindowsFirewall.IDynamicPortMappingCollection_head
    IDynamicPortMappingCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(7, 'get__NewEnum', ((1, 'pVal'),)))
    IDynamicPortMappingCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.Foundation.BSTR,POINTER(win32more.NetworkManagement.WindowsFirewall.IDynamicPortMapping_head))(8, 'get_Item', ((1, 'bstrRemoteHost'),(1, 'lExternalPort'),(1, 'bstrProtocol'),(1, 'ppDPM'),)))
    IDynamicPortMappingCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_Count', ((1, 'pVal'),)))
    IDynamicPortMappingCollection.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.Foundation.BSTR)(10, 'Remove', ((1, 'bstrRemoteHost'),(1, 'lExternalPort'),(1, 'bstrProtocol'),)))
    IDynamicPortMappingCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.Foundation.BSTR,Int32,win32more.Foundation.BSTR,win32more.Foundation.VARIANT_BOOL,win32more.Foundation.BSTR,Int32,POINTER(win32more.NetworkManagement.WindowsFirewall.IDynamicPortMapping_head))(11, 'Add', ((1, 'bstrRemoteHost'),(1, 'lExternalPort'),(1, 'bstrProtocol'),(1, 'lInternalPort'),(1, 'bstrInternalClient'),(1, 'bEnabled'),(1, 'bstrDescription'),(1, 'lLeaseDuration'),(1, 'ppDPM'),)))
    win32more.System.Com.IDispatch
    return IDynamicPortMappingCollection
def _define_IEnumNetConnection_head():
    class IEnumNetConnection(win32more.System.Com.IUnknown_head):
        Guid = Guid('c08956a0-1cd3-11d1-b1-c5-00-80-5f-c1-27-0e')
    return IEnumNetConnection
def _define_IEnumNetConnection():
    IEnumNetConnection = win32more.NetworkManagement.WindowsFirewall.IEnumNetConnection_head
    IEnumNetConnection.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.NetworkManagement.WindowsFirewall.INetConnection_head),POINTER(UInt32))(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumNetConnection.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'celt'),)))
    IEnumNetConnection.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumNetConnection.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.IEnumNetConnection_head))(6, 'Clone', ((1, 'ppenum'),)))
    win32more.System.Com.IUnknown
    return IEnumNetConnection
def _define_IEnumNetSharingEveryConnection_head():
    class IEnumNetSharingEveryConnection(win32more.System.Com.IUnknown_head):
        Guid = Guid('c08956b8-1cd3-11d1-b1-c5-00-80-5f-c1-27-0e')
    return IEnumNetSharingEveryConnection
def _define_IEnumNetSharingEveryConnection():
    IEnumNetSharingEveryConnection = win32more.NetworkManagement.WindowsFirewall.IEnumNetSharingEveryConnection_head
    IEnumNetSharingEveryConnection.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.VARIANT_head),POINTER(UInt32))(3, 'Next', ((1, 'celt'),(1, 'rgVar'),(1, 'pceltFetched'),)))
    IEnumNetSharingEveryConnection.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'celt'),)))
    IEnumNetSharingEveryConnection.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumNetSharingEveryConnection.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.IEnumNetSharingEveryConnection_head))(6, 'Clone', ((1, 'ppenum'),)))
    win32more.System.Com.IUnknown
    return IEnumNetSharingEveryConnection
def _define_IEnumNetSharingPortMapping_head():
    class IEnumNetSharingPortMapping(win32more.System.Com.IUnknown_head):
        Guid = Guid('c08956b0-1cd3-11d1-b1-c5-00-80-5f-c1-27-0e')
    return IEnumNetSharingPortMapping
def _define_IEnumNetSharingPortMapping():
    IEnumNetSharingPortMapping = win32more.NetworkManagement.WindowsFirewall.IEnumNetSharingPortMapping_head
    IEnumNetSharingPortMapping.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.VARIANT_head),POINTER(UInt32))(3, 'Next', ((1, 'celt'),(1, 'rgVar'),(1, 'pceltFetched'),)))
    IEnumNetSharingPortMapping.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'celt'),)))
    IEnumNetSharingPortMapping.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumNetSharingPortMapping.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.IEnumNetSharingPortMapping_head))(6, 'Clone', ((1, 'ppenum'),)))
    win32more.System.Com.IUnknown
    return IEnumNetSharingPortMapping
def _define_IEnumNetSharingPrivateConnection_head():
    class IEnumNetSharingPrivateConnection(win32more.System.Com.IUnknown_head):
        Guid = Guid('c08956b5-1cd3-11d1-b1-c5-00-80-5f-c1-27-0e')
    return IEnumNetSharingPrivateConnection
def _define_IEnumNetSharingPrivateConnection():
    IEnumNetSharingPrivateConnection = win32more.NetworkManagement.WindowsFirewall.IEnumNetSharingPrivateConnection_head
    IEnumNetSharingPrivateConnection.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.VARIANT_head),POINTER(UInt32))(3, 'Next', ((1, 'celt'),(1, 'rgVar'),(1, 'pCeltFetched'),)))
    IEnumNetSharingPrivateConnection.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'celt'),)))
    IEnumNetSharingPrivateConnection.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumNetSharingPrivateConnection.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.IEnumNetSharingPrivateConnection_head))(6, 'Clone', ((1, 'ppenum'),)))
    win32more.System.Com.IUnknown
    return IEnumNetSharingPrivateConnection
def _define_IEnumNetSharingPublicConnection_head():
    class IEnumNetSharingPublicConnection(win32more.System.Com.IUnknown_head):
        Guid = Guid('c08956b4-1cd3-11d1-b1-c5-00-80-5f-c1-27-0e')
    return IEnumNetSharingPublicConnection
def _define_IEnumNetSharingPublicConnection():
    IEnumNetSharingPublicConnection = win32more.NetworkManagement.WindowsFirewall.IEnumNetSharingPublicConnection_head
    IEnumNetSharingPublicConnection.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.VARIANT_head),POINTER(UInt32))(3, 'Next', ((1, 'celt'),(1, 'rgVar'),(1, 'pceltFetched'),)))
    IEnumNetSharingPublicConnection.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'celt'),)))
    IEnumNetSharingPublicConnection.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumNetSharingPublicConnection.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.IEnumNetSharingPublicConnection_head))(6, 'Clone', ((1, 'ppenum'),)))
    win32more.System.Com.IUnknown
    return IEnumNetSharingPublicConnection
def _define_INATEventManager_head():
    class INATEventManager(win32more.System.Com.IDispatch_head):
        Guid = Guid('624bd588-9060-4109-b0-b0-1a-db-bc-ac-32-df')
    return INATEventManager
def _define_INATEventManager():
    INATEventManager = win32more.NetworkManagement.WindowsFirewall.INATEventManager_head
    INATEventManager.put_ExternalIPAddressCallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(7, 'put_ExternalIPAddressCallback', ((1, 'pUnk'),)))
    INATEventManager.put_NumberOfEntriesCallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(8, 'put_NumberOfEntriesCallback', ((1, 'pUnk'),)))
    win32more.System.Com.IDispatch
    return INATEventManager
def _define_INATExternalIPAddressCallback_head():
    class INATExternalIPAddressCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('9c416740-a34e-446f-ba-06-ab-d0-4c-31-49-ae')
    return INATExternalIPAddressCallback
def _define_INATExternalIPAddressCallback():
    INATExternalIPAddressCallback = win32more.NetworkManagement.WindowsFirewall.INATExternalIPAddressCallback_head
    INATExternalIPAddressCallback.NewExternalIPAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(3, 'NewExternalIPAddress', ((1, 'bstrNewExternalIPAddress'),)))
    win32more.System.Com.IUnknown
    return INATExternalIPAddressCallback
def _define_INATNumberOfEntriesCallback_head():
    class INATNumberOfEntriesCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('c83a0a74-91ee-41b6-b6-7a-67-e0-f0-0b-bd-78')
    return INATNumberOfEntriesCallback
def _define_INATNumberOfEntriesCallback():
    INATNumberOfEntriesCallback = win32more.NetworkManagement.WindowsFirewall.INATNumberOfEntriesCallback_head
    INATNumberOfEntriesCallback.NewNumberOfEntries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(3, 'NewNumberOfEntries', ((1, 'lNewNumberOfEntries'),)))
    win32more.System.Com.IUnknown
    return INATNumberOfEntriesCallback
def _define_INET_FIREWALL_AC_BINARIES_head():
    class INET_FIREWALL_AC_BINARIES(Structure):
        pass
    return INET_FIREWALL_AC_BINARIES
def _define_INET_FIREWALL_AC_BINARIES():
    INET_FIREWALL_AC_BINARIES = win32more.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_BINARIES_head
    INET_FIREWALL_AC_BINARIES._fields_ = [
        ('count', UInt32),
        ('binaries', POINTER(win32more.Foundation.PWSTR)),
    ]
    return INET_FIREWALL_AC_BINARIES
def _define_INET_FIREWALL_AC_CAPABILITIES_head():
    class INET_FIREWALL_AC_CAPABILITIES(Structure):
        pass
    return INET_FIREWALL_AC_CAPABILITIES
def _define_INET_FIREWALL_AC_CAPABILITIES():
    INET_FIREWALL_AC_CAPABILITIES = win32more.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_CAPABILITIES_head
    INET_FIREWALL_AC_CAPABILITIES._fields_ = [
        ('count', UInt32),
        ('capabilities', POINTER(win32more.Security.SID_AND_ATTRIBUTES_head)),
    ]
    return INET_FIREWALL_AC_CAPABILITIES
def _define_INET_FIREWALL_AC_CHANGE_head():
    class INET_FIREWALL_AC_CHANGE(Structure):
        pass
    return INET_FIREWALL_AC_CHANGE
def _define_INET_FIREWALL_AC_CHANGE():
    INET_FIREWALL_AC_CHANGE = win32more.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_CHANGE_head
    class INET_FIREWALL_AC_CHANGE__Anonymous_e__Union(Union):
        pass
    INET_FIREWALL_AC_CHANGE__Anonymous_e__Union._fields_ = [
        ('capabilities', win32more.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_CAPABILITIES),
        ('binaries', win32more.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_BINARIES),
    ]
    INET_FIREWALL_AC_CHANGE._anonymous_ = [
        'Anonymous',
    ]
    INET_FIREWALL_AC_CHANGE._fields_ = [
        ('changeType', win32more.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_CHANGE_TYPE),
        ('createType', win32more.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_CREATION_TYPE),
        ('appContainerSid', POINTER(win32more.Security.SID_head)),
        ('userSid', POINTER(win32more.Security.SID_head)),
        ('displayName', win32more.Foundation.PWSTR),
        ('Anonymous', INET_FIREWALL_AC_CHANGE__Anonymous_e__Union),
    ]
    return INET_FIREWALL_AC_CHANGE
INET_FIREWALL_AC_CHANGE_TYPE = Int32
INET_FIREWALL_AC_CHANGE_INVALID = 0
INET_FIREWALL_AC_CHANGE_CREATE = 1
INET_FIREWALL_AC_CHANGE_DELETE = 2
INET_FIREWALL_AC_CHANGE_MAX = 3
INET_FIREWALL_AC_CREATION_TYPE = Int32
INET_FIREWALL_AC_NONE = 0
INET_FIREWALL_AC_PACKAGE_ID_ONLY = 1
INET_FIREWALL_AC_BINARY = 2
INET_FIREWALL_AC_MAX = 4
def _define_INET_FIREWALL_APP_CONTAINER_head():
    class INET_FIREWALL_APP_CONTAINER(Structure):
        pass
    return INET_FIREWALL_APP_CONTAINER
def _define_INET_FIREWALL_APP_CONTAINER():
    INET_FIREWALL_APP_CONTAINER = win32more.NetworkManagement.WindowsFirewall.INET_FIREWALL_APP_CONTAINER_head
    INET_FIREWALL_APP_CONTAINER._fields_ = [
        ('appContainerSid', POINTER(win32more.Security.SID_head)),
        ('userSid', POINTER(win32more.Security.SID_head)),
        ('appContainerName', win32more.Foundation.PWSTR),
        ('displayName', win32more.Foundation.PWSTR),
        ('description', win32more.Foundation.PWSTR),
        ('capabilities', win32more.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_CAPABILITIES),
        ('binaries', win32more.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_BINARIES),
        ('workingDirectory', win32more.Foundation.PWSTR),
        ('packageFullName', win32more.Foundation.PWSTR),
    ]
    return INET_FIREWALL_APP_CONTAINER
def _define_INetConnection_head():
    class INetConnection(win32more.System.Com.IUnknown_head):
        Guid = Guid('c08956a1-1cd3-11d1-b1-c5-00-80-5f-c1-27-0e')
    return INetConnection
def _define_INetConnection():
    INetConnection = win32more.NetworkManagement.WindowsFirewall.INetConnection_head
    INetConnection.Connect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Connect', ()))
    INetConnection.Disconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Disconnect', ()))
    INetConnection.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Delete', ()))
    INetConnection.Duplicate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.WindowsFirewall.INetConnection_head))(6, 'Duplicate', ((1, 'pszwDuplicateName'),(1, 'ppCon'),)))
    INetConnection.GetProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.NetworkManagement.WindowsFirewall.NETCON_PROPERTIES_head)))(7, 'GetProperties', ((1, 'ppProps'),)))
    INetConnection.GetUiObjectClassId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(8, 'GetUiObjectClassId', ((1, 'pclsid'),)))
    INetConnection.Rename = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(9, 'Rename', ((1, 'pszwNewName'),)))
    win32more.System.Com.IUnknown
    return INetConnection
def _define_INetConnectionConnectUi_head():
    class INetConnectionConnectUi(win32more.System.Com.IUnknown_head):
        Guid = Guid('c08956a3-1cd3-11d1-b1-c5-00-80-5f-c1-27-0e')
    return INetConnectionConnectUi
def _define_INetConnectionConnectUi():
    INetConnectionConnectUi = win32more.NetworkManagement.WindowsFirewall.INetConnectionConnectUi_head
    INetConnectionConnectUi.SetConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.INetConnection_head)(3, 'SetConnection', ((1, 'pCon'),)))
    INetConnectionConnectUi.Connect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32)(4, 'Connect', ((1, 'hwndParent'),(1, 'dwFlags'),)))
    INetConnectionConnectUi.Disconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32)(5, 'Disconnect', ((1, 'hwndParent'),(1, 'dwFlags'),)))
    win32more.System.Com.IUnknown
    return INetConnectionConnectUi
def _define_INetConnectionManager_head():
    class INetConnectionManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('c08956a2-1cd3-11d1-b1-c5-00-80-5f-c1-27-0e')
    return INetConnectionManager
def _define_INetConnectionManager():
    INetConnectionManager = win32more.NetworkManagement.WindowsFirewall.INetConnectionManager_head
    INetConnectionManager.EnumConnections = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NETCONMGR_ENUM_FLAGS,POINTER(win32more.NetworkManagement.WindowsFirewall.IEnumNetConnection_head))(3, 'EnumConnections', ((1, 'Flags'),(1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return INetConnectionManager
def _define_INetConnectionProps_head():
    class INetConnectionProps(win32more.System.Com.IDispatch_head):
        Guid = Guid('f4277c95-ce5b-463d-81-67-56-62-d9-bc-aa-72')
    return INetConnectionProps
def _define_INetConnectionProps():
    INetConnectionProps = win32more.NetworkManagement.WindowsFirewall.INetConnectionProps_head
    INetConnectionProps.get_Guid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Guid', ((1, 'pbstrGuid'),)))
    INetConnectionProps.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_Name', ((1, 'pbstrName'),)))
    INetConnectionProps.get_DeviceName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_DeviceName', ((1, 'pbstrDeviceName'),)))
    INetConnectionProps.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NETCON_STATUS))(10, 'get_Status', ((1, 'pStatus'),)))
    INetConnectionProps.get_MediaType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NETCON_MEDIATYPE))(11, 'get_MediaType', ((1, 'pMediaType'),)))
    INetConnectionProps.get_Characteristics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(12, 'get_Characteristics', ((1, 'pdwFlags'),)))
    win32more.System.Com.IDispatch
    return INetConnectionProps
def _define_INetFwAuthorizedApplication_head():
    class INetFwAuthorizedApplication(win32more.System.Com.IDispatch_head):
        Guid = Guid('b5e64ffa-c2c5-444e-a3-01-fb-5e-00-01-80-50')
    return INetFwAuthorizedApplication
def _define_INetFwAuthorizedApplication():
    INetFwAuthorizedApplication = win32more.NetworkManagement.WindowsFirewall.INetFwAuthorizedApplication_head
    INetFwAuthorizedApplication.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Name', ((1, 'name'),)))
    INetFwAuthorizedApplication.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(8, 'put_Name', ((1, 'name'),)))
    INetFwAuthorizedApplication.get_ProcessImageFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_ProcessImageFileName', ((1, 'imageFileName'),)))
    INetFwAuthorizedApplication.put_ProcessImageFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(10, 'put_ProcessImageFileName', ((1, 'imageFileName'),)))
    INetFwAuthorizedApplication.get_IpVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION))(11, 'get_IpVersion', ((1, 'ipVersion'),)))
    INetFwAuthorizedApplication.put_IpVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION)(12, 'put_IpVersion', ((1, 'ipVersion'),)))
    INetFwAuthorizedApplication.get_Scope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_SCOPE))(13, 'get_Scope', ((1, 'scope'),)))
    INetFwAuthorizedApplication.put_Scope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_SCOPE)(14, 'put_Scope', ((1, 'scope'),)))
    INetFwAuthorizedApplication.get_RemoteAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(15, 'get_RemoteAddresses', ((1, 'remoteAddrs'),)))
    INetFwAuthorizedApplication.put_RemoteAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(16, 'put_RemoteAddresses', ((1, 'remoteAddrs'),)))
    INetFwAuthorizedApplication.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(17, 'get_Enabled', ((1, 'enabled'),)))
    INetFwAuthorizedApplication.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(18, 'put_Enabled', ((1, 'enabled'),)))
    win32more.System.Com.IDispatch
    return INetFwAuthorizedApplication
def _define_INetFwAuthorizedApplications_head():
    class INetFwAuthorizedApplications(win32more.System.Com.IDispatch_head):
        Guid = Guid('644efd52-ccf9-486c-97-a2-39-f3-52-57-0b-30')
    return INetFwAuthorizedApplications
def _define_INetFwAuthorizedApplications():
    INetFwAuthorizedApplications = win32more.NetworkManagement.WindowsFirewall.INetFwAuthorizedApplications_head
    INetFwAuthorizedApplications.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'count'),)))
    INetFwAuthorizedApplications.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.INetFwAuthorizedApplication_head)(8, 'Add', ((1, 'app'),)))
    INetFwAuthorizedApplications.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(9, 'Remove', ((1, 'imageFileName'),)))
    INetFwAuthorizedApplications.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwAuthorizedApplication_head))(10, 'Item', ((1, 'imageFileName'),(1, 'app'),)))
    INetFwAuthorizedApplications.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(11, 'get__NewEnum', ((1, 'newEnum'),)))
    win32more.System.Com.IDispatch
    return INetFwAuthorizedApplications
def _define_INetFwIcmpSettings_head():
    class INetFwIcmpSettings(win32more.System.Com.IDispatch_head):
        Guid = Guid('a6207b2e-7cdd-426a-95-1e-5e-1c-bc-5a-fe-ad')
    return INetFwIcmpSettings
def _define_INetFwIcmpSettings():
    INetFwIcmpSettings = win32more.NetworkManagement.WindowsFirewall.INetFwIcmpSettings_head
    INetFwIcmpSettings.get_AllowOutboundDestinationUnreachable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(7, 'get_AllowOutboundDestinationUnreachable', ((1, 'allow'),)))
    INetFwIcmpSettings.put_AllowOutboundDestinationUnreachable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(8, 'put_AllowOutboundDestinationUnreachable', ((1, 'allow'),)))
    INetFwIcmpSettings.get_AllowRedirect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(9, 'get_AllowRedirect', ((1, 'allow'),)))
    INetFwIcmpSettings.put_AllowRedirect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(10, 'put_AllowRedirect', ((1, 'allow'),)))
    INetFwIcmpSettings.get_AllowInboundEchoRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(11, 'get_AllowInboundEchoRequest', ((1, 'allow'),)))
    INetFwIcmpSettings.put_AllowInboundEchoRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(12, 'put_AllowInboundEchoRequest', ((1, 'allow'),)))
    INetFwIcmpSettings.get_AllowOutboundTimeExceeded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(13, 'get_AllowOutboundTimeExceeded', ((1, 'allow'),)))
    INetFwIcmpSettings.put_AllowOutboundTimeExceeded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(14, 'put_AllowOutboundTimeExceeded', ((1, 'allow'),)))
    INetFwIcmpSettings.get_AllowOutboundParameterProblem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(15, 'get_AllowOutboundParameterProblem', ((1, 'allow'),)))
    INetFwIcmpSettings.put_AllowOutboundParameterProblem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(16, 'put_AllowOutboundParameterProblem', ((1, 'allow'),)))
    INetFwIcmpSettings.get_AllowOutboundSourceQuench = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(17, 'get_AllowOutboundSourceQuench', ((1, 'allow'),)))
    INetFwIcmpSettings.put_AllowOutboundSourceQuench = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(18, 'put_AllowOutboundSourceQuench', ((1, 'allow'),)))
    INetFwIcmpSettings.get_AllowInboundRouterRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(19, 'get_AllowInboundRouterRequest', ((1, 'allow'),)))
    INetFwIcmpSettings.put_AllowInboundRouterRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(20, 'put_AllowInboundRouterRequest', ((1, 'allow'),)))
    INetFwIcmpSettings.get_AllowInboundTimestampRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(21, 'get_AllowInboundTimestampRequest', ((1, 'allow'),)))
    INetFwIcmpSettings.put_AllowInboundTimestampRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(22, 'put_AllowInboundTimestampRequest', ((1, 'allow'),)))
    INetFwIcmpSettings.get_AllowInboundMaskRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(23, 'get_AllowInboundMaskRequest', ((1, 'allow'),)))
    INetFwIcmpSettings.put_AllowInboundMaskRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(24, 'put_AllowInboundMaskRequest', ((1, 'allow'),)))
    INetFwIcmpSettings.get_AllowOutboundPacketTooBig = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(25, 'get_AllowOutboundPacketTooBig', ((1, 'allow'),)))
    INetFwIcmpSettings.put_AllowOutboundPacketTooBig = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(26, 'put_AllowOutboundPacketTooBig', ((1, 'allow'),)))
    win32more.System.Com.IDispatch
    return INetFwIcmpSettings
def _define_INetFwMgr_head():
    class INetFwMgr(win32more.System.Com.IDispatch_head):
        Guid = Guid('f7898af5-cac4-4632-a2-ec-da-06-e5-11-1a-f2')
    return INetFwMgr
def _define_INetFwMgr():
    INetFwMgr = win32more.NetworkManagement.WindowsFirewall.INetFwMgr_head
    INetFwMgr.get_LocalPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwPolicy_head))(7, 'get_LocalPolicy', ((1, 'localPolicy'),)))
    INetFwMgr.get_CurrentProfileType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE))(8, 'get_CurrentProfileType', ((1, 'profileType'),)))
    INetFwMgr.RestoreDefaults = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(9, 'RestoreDefaults', ()))
    INetFwMgr.IsPortAllowed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION,Int32,win32more.Foundation.BSTR,win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_PROTOCOL,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head))(10, 'IsPortAllowed', ((1, 'imageFileName'),(1, 'ipVersion'),(1, 'portNumber'),(1, 'localAddress'),(1, 'ipProtocol'),(1, 'allowed'),(1, 'restricted'),)))
    INetFwMgr.IsIcmpTypeAllowed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION,win32more.Foundation.BSTR,Byte,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head))(11, 'IsIcmpTypeAllowed', ((1, 'ipVersion'),(1, 'localAddress'),(1, 'type'),(1, 'allowed'),(1, 'restricted'),)))
    win32more.System.Com.IDispatch
    return INetFwMgr
def _define_INetFwOpenPort_head():
    class INetFwOpenPort(win32more.System.Com.IDispatch_head):
        Guid = Guid('e0483ba0-47ff-4d9c-a6-d6-77-41-d0-b1-95-f7')
    return INetFwOpenPort
def _define_INetFwOpenPort():
    INetFwOpenPort = win32more.NetworkManagement.WindowsFirewall.INetFwOpenPort_head
    INetFwOpenPort.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Name', ((1, 'name'),)))
    INetFwOpenPort.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(8, 'put_Name', ((1, 'name'),)))
    INetFwOpenPort.get_IpVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION))(9, 'get_IpVersion', ((1, 'ipVersion'),)))
    INetFwOpenPort.put_IpVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION)(10, 'put_IpVersion', ((1, 'ipVersion'),)))
    INetFwOpenPort.get_Protocol = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_PROTOCOL))(11, 'get_Protocol', ((1, 'ipProtocol'),)))
    INetFwOpenPort.put_Protocol = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_PROTOCOL)(12, 'put_Protocol', ((1, 'ipProtocol'),)))
    INetFwOpenPort.get_Port = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(13, 'get_Port', ((1, 'portNumber'),)))
    INetFwOpenPort.put_Port = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(14, 'put_Port', ((1, 'portNumber'),)))
    INetFwOpenPort.get_Scope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_SCOPE))(15, 'get_Scope', ((1, 'scope'),)))
    INetFwOpenPort.put_Scope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_SCOPE)(16, 'put_Scope', ((1, 'scope'),)))
    INetFwOpenPort.get_RemoteAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(17, 'get_RemoteAddresses', ((1, 'remoteAddrs'),)))
    INetFwOpenPort.put_RemoteAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(18, 'put_RemoteAddresses', ((1, 'remoteAddrs'),)))
    INetFwOpenPort.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(19, 'get_Enabled', ((1, 'enabled'),)))
    INetFwOpenPort.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(20, 'put_Enabled', ((1, 'enabled'),)))
    INetFwOpenPort.get_BuiltIn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(21, 'get_BuiltIn', ((1, 'builtIn'),)))
    win32more.System.Com.IDispatch
    return INetFwOpenPort
def _define_INetFwOpenPorts_head():
    class INetFwOpenPorts(win32more.System.Com.IDispatch_head):
        Guid = Guid('c0e9d7fa-e07e-430a-b1-9a-09-0c-e8-2d-92-e2')
    return INetFwOpenPorts
def _define_INetFwOpenPorts():
    INetFwOpenPorts = win32more.NetworkManagement.WindowsFirewall.INetFwOpenPorts_head
    INetFwOpenPorts.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'count'),)))
    INetFwOpenPorts.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.INetFwOpenPort_head)(8, 'Add', ((1, 'port'),)))
    INetFwOpenPorts.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_PROTOCOL)(9, 'Remove', ((1, 'portNumber'),(1, 'ipProtocol'),)))
    INetFwOpenPorts.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_PROTOCOL,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwOpenPort_head))(10, 'Item', ((1, 'portNumber'),(1, 'ipProtocol'),(1, 'openPort'),)))
    INetFwOpenPorts.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(11, 'get__NewEnum', ((1, 'newEnum'),)))
    win32more.System.Com.IDispatch
    return INetFwOpenPorts
def _define_INetFwPolicy_head():
    class INetFwPolicy(win32more.System.Com.IDispatch_head):
        Guid = Guid('d46d2478-9ac9-4008-9d-c7-55-63-ce-55-36-cc')
    return INetFwPolicy
def _define_INetFwPolicy():
    INetFwPolicy = win32more.NetworkManagement.WindowsFirewall.INetFwPolicy_head
    INetFwPolicy.get_CurrentProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwProfile_head))(7, 'get_CurrentProfile', ((1, 'profile'),)))
    INetFwPolicy.GetProfileByType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwProfile_head))(8, 'GetProfileByType', ((1, 'profileType'),(1, 'profile'),)))
    win32more.System.Com.IDispatch
    return INetFwPolicy
def _define_INetFwPolicy2_head():
    class INetFwPolicy2(win32more.System.Com.IDispatch_head):
        Guid = Guid('98325047-c671-4174-8d-81-de-fc-d3-f0-31-86')
    return INetFwPolicy2
def _define_INetFwPolicy2():
    INetFwPolicy2 = win32more.NetworkManagement.WindowsFirewall.INetFwPolicy2_head
    INetFwPolicy2.get_CurrentProfileTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_CurrentProfileTypes', ((1, 'profileTypesBitmask'),)))
    INetFwPolicy2.get_FirewallEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,POINTER(win32more.Foundation.VARIANT_BOOL))(8, 'get_FirewallEnabled', ((1, 'profileType'),(1, 'enabled'),)))
    INetFwPolicy2.put_FirewallEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,win32more.Foundation.VARIANT_BOOL)(9, 'put_FirewallEnabled', ((1, 'profileType'),(1, 'enabled'),)))
    INetFwPolicy2.get_ExcludedInterfaces = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,POINTER(win32more.System.Com.VARIANT_head))(10, 'get_ExcludedInterfaces', ((1, 'profileType'),(1, 'interfaces'),)))
    INetFwPolicy2.put_ExcludedInterfaces = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,win32more.System.Com.VARIANT)(11, 'put_ExcludedInterfaces', ((1, 'profileType'),(1, 'interfaces'),)))
    INetFwPolicy2.get_BlockAllInboundTraffic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,POINTER(win32more.Foundation.VARIANT_BOOL))(12, 'get_BlockAllInboundTraffic', ((1, 'profileType'),(1, 'Block'),)))
    INetFwPolicy2.put_BlockAllInboundTraffic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,win32more.Foundation.VARIANT_BOOL)(13, 'put_BlockAllInboundTraffic', ((1, 'profileType'),(1, 'Block'),)))
    INetFwPolicy2.get_NotificationsDisabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,POINTER(win32more.Foundation.VARIANT_BOOL))(14, 'get_NotificationsDisabled', ((1, 'profileType'),(1, 'disabled'),)))
    INetFwPolicy2.put_NotificationsDisabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,win32more.Foundation.VARIANT_BOOL)(15, 'put_NotificationsDisabled', ((1, 'profileType'),(1, 'disabled'),)))
    INetFwPolicy2.get_UnicastResponsesToMulticastBroadcastDisabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,POINTER(win32more.Foundation.VARIANT_BOOL))(16, 'get_UnicastResponsesToMulticastBroadcastDisabled', ((1, 'profileType'),(1, 'disabled'),)))
    INetFwPolicy2.put_UnicastResponsesToMulticastBroadcastDisabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,win32more.Foundation.VARIANT_BOOL)(17, 'put_UnicastResponsesToMulticastBroadcastDisabled', ((1, 'profileType'),(1, 'disabled'),)))
    INetFwPolicy2.get_Rules = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwRules_head))(18, 'get_Rules', ((1, 'rules'),)))
    INetFwPolicy2.get_ServiceRestriction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwServiceRestriction_head))(19, 'get_ServiceRestriction', ((1, 'ServiceRestriction'),)))
    INetFwPolicy2.EnableRuleGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,win32more.Foundation.VARIANT_BOOL)(20, 'EnableRuleGroup', ((1, 'profileTypesBitmask'),(1, 'group'),(1, 'enable'),)))
    INetFwPolicy2.IsRuleGroupEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,POINTER(win32more.Foundation.VARIANT_BOOL))(21, 'IsRuleGroupEnabled', ((1, 'profileTypesBitmask'),(1, 'group'),(1, 'enabled'),)))
    INetFwPolicy2.RestoreLocalFirewallDefaults = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(22, 'RestoreLocalFirewallDefaults', ()))
    INetFwPolicy2.get_DefaultInboundAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_ACTION))(23, 'get_DefaultInboundAction', ((1, 'profileType'),(1, 'action'),)))
    INetFwPolicy2.put_DefaultInboundAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,win32more.NetworkManagement.WindowsFirewall.NET_FW_ACTION)(24, 'put_DefaultInboundAction', ((1, 'profileType'),(1, 'action'),)))
    INetFwPolicy2.get_DefaultOutboundAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_ACTION))(25, 'get_DefaultOutboundAction', ((1, 'profileType'),(1, 'action'),)))
    INetFwPolicy2.put_DefaultOutboundAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,win32more.NetworkManagement.WindowsFirewall.NET_FW_ACTION)(26, 'put_DefaultOutboundAction', ((1, 'profileType'),(1, 'action'),)))
    INetFwPolicy2.get_IsRuleGroupCurrentlyEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.VARIANT_BOOL))(27, 'get_IsRuleGroupCurrentlyEnabled', ((1, 'group'),(1, 'enabled'),)))
    INetFwPolicy2.get_LocalPolicyModifyState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_MODIFY_STATE))(28, 'get_LocalPolicyModifyState', ((1, 'modifyState'),)))
    win32more.System.Com.IDispatch
    return INetFwPolicy2
def _define_INetFwProduct_head():
    class INetFwProduct(win32more.System.Com.IDispatch_head):
        Guid = Guid('71881699-18f4-458b-b8-92-3f-fc-e5-e0-7f-75')
    return INetFwProduct
def _define_INetFwProduct():
    INetFwProduct = win32more.NetworkManagement.WindowsFirewall.INetFwProduct_head
    INetFwProduct.get_RuleCategories = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(7, 'get_RuleCategories', ((1, 'ruleCategories'),)))
    INetFwProduct.put_RuleCategories = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(8, 'put_RuleCategories', ((1, 'ruleCategories'),)))
    INetFwProduct.get_DisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_DisplayName', ((1, 'displayName'),)))
    INetFwProduct.put_DisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(10, 'put_DisplayName', ((1, 'displayName'),)))
    INetFwProduct.get_PathToSignedProductExe = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_PathToSignedProductExe', ((1, 'path'),)))
    win32more.System.Com.IDispatch
    return INetFwProduct
def _define_INetFwProducts_head():
    class INetFwProducts(win32more.System.Com.IDispatch_head):
        Guid = Guid('39eb36e0-2097-40bd-8a-f2-63-a1-3b-52-53-62')
    return INetFwProducts
def _define_INetFwProducts():
    INetFwProducts = win32more.NetworkManagement.WindowsFirewall.INetFwProducts_head
    INetFwProducts.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'count'),)))
    INetFwProducts.Register = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.INetFwProduct_head,POINTER(win32more.System.Com.IUnknown_head))(8, 'Register', ((1, 'product'),(1, 'registration'),)))
    INetFwProducts.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwProduct_head))(9, 'Item', ((1, 'index'),(1, 'product'),)))
    INetFwProducts.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(10, 'get__NewEnum', ((1, 'newEnum'),)))
    win32more.System.Com.IDispatch
    return INetFwProducts
def _define_INetFwProfile_head():
    class INetFwProfile(win32more.System.Com.IDispatch_head):
        Guid = Guid('174a0dda-e9f9-449d-99-3b-21-ab-66-7c-a4-56')
    return INetFwProfile
def _define_INetFwProfile():
    INetFwProfile = win32more.NetworkManagement.WindowsFirewall.INetFwProfile_head
    INetFwProfile.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE))(7, 'get_Type', ((1, 'type'),)))
    INetFwProfile.get_FirewallEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(8, 'get_FirewallEnabled', ((1, 'enabled'),)))
    INetFwProfile.put_FirewallEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(9, 'put_FirewallEnabled', ((1, 'enabled'),)))
    INetFwProfile.get_ExceptionsNotAllowed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(10, 'get_ExceptionsNotAllowed', ((1, 'notAllowed'),)))
    INetFwProfile.put_ExceptionsNotAllowed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(11, 'put_ExceptionsNotAllowed', ((1, 'notAllowed'),)))
    INetFwProfile.get_NotificationsDisabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(12, 'get_NotificationsDisabled', ((1, 'disabled'),)))
    INetFwProfile.put_NotificationsDisabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(13, 'put_NotificationsDisabled', ((1, 'disabled'),)))
    INetFwProfile.get_UnicastResponsesToMulticastBroadcastDisabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(14, 'get_UnicastResponsesToMulticastBroadcastDisabled', ((1, 'disabled'),)))
    INetFwProfile.put_UnicastResponsesToMulticastBroadcastDisabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(15, 'put_UnicastResponsesToMulticastBroadcastDisabled', ((1, 'disabled'),)))
    INetFwProfile.get_RemoteAdminSettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwRemoteAdminSettings_head))(16, 'get_RemoteAdminSettings', ((1, 'remoteAdminSettings'),)))
    INetFwProfile.get_IcmpSettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwIcmpSettings_head))(17, 'get_IcmpSettings', ((1, 'icmpSettings'),)))
    INetFwProfile.get_GloballyOpenPorts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwOpenPorts_head))(18, 'get_GloballyOpenPorts', ((1, 'openPorts'),)))
    INetFwProfile.get_Services = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwServices_head))(19, 'get_Services', ((1, 'services'),)))
    INetFwProfile.get_AuthorizedApplications = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwAuthorizedApplications_head))(20, 'get_AuthorizedApplications', ((1, 'apps'),)))
    win32more.System.Com.IDispatch
    return INetFwProfile
def _define_INetFwRemoteAdminSettings_head():
    class INetFwRemoteAdminSettings(win32more.System.Com.IDispatch_head):
        Guid = Guid('d4becddf-6f73-4a83-b8-32-9c-66-87-4c-d2-0e')
    return INetFwRemoteAdminSettings
def _define_INetFwRemoteAdminSettings():
    INetFwRemoteAdminSettings = win32more.NetworkManagement.WindowsFirewall.INetFwRemoteAdminSettings_head
    INetFwRemoteAdminSettings.get_IpVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION))(7, 'get_IpVersion', ((1, 'ipVersion'),)))
    INetFwRemoteAdminSettings.put_IpVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION)(8, 'put_IpVersion', ((1, 'ipVersion'),)))
    INetFwRemoteAdminSettings.get_Scope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_SCOPE))(9, 'get_Scope', ((1, 'scope'),)))
    INetFwRemoteAdminSettings.put_Scope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_SCOPE)(10, 'put_Scope', ((1, 'scope'),)))
    INetFwRemoteAdminSettings.get_RemoteAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_RemoteAddresses', ((1, 'remoteAddrs'),)))
    INetFwRemoteAdminSettings.put_RemoteAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(12, 'put_RemoteAddresses', ((1, 'remoteAddrs'),)))
    INetFwRemoteAdminSettings.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(13, 'get_Enabled', ((1, 'enabled'),)))
    INetFwRemoteAdminSettings.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(14, 'put_Enabled', ((1, 'enabled'),)))
    win32more.System.Com.IDispatch
    return INetFwRemoteAdminSettings
def _define_INetFwRule_head():
    class INetFwRule(win32more.System.Com.IDispatch_head):
        Guid = Guid('af230d27-baba-4e42-ac-ed-f5-24-f2-2c-fc-e2')
    return INetFwRule
def _define_INetFwRule():
    INetFwRule = win32more.NetworkManagement.WindowsFirewall.INetFwRule_head
    INetFwRule.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Name', ((1, 'name'),)))
    INetFwRule.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(8, 'put_Name', ((1, 'name'),)))
    INetFwRule.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_Description', ((1, 'desc'),)))
    INetFwRule.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(10, 'put_Description', ((1, 'desc'),)))
    INetFwRule.get_ApplicationName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_ApplicationName', ((1, 'imageFileName'),)))
    INetFwRule.put_ApplicationName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(12, 'put_ApplicationName', ((1, 'imageFileName'),)))
    INetFwRule.get_ServiceName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(13, 'get_ServiceName', ((1, 'serviceName'),)))
    INetFwRule.put_ServiceName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(14, 'put_ServiceName', ((1, 'serviceName'),)))
    INetFwRule.get_Protocol = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(15, 'get_Protocol', ((1, 'protocol'),)))
    INetFwRule.put_Protocol = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(16, 'put_Protocol', ((1, 'protocol'),)))
    INetFwRule.get_LocalPorts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(17, 'get_LocalPorts', ((1, 'portNumbers'),)))
    INetFwRule.put_LocalPorts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(18, 'put_LocalPorts', ((1, 'portNumbers'),)))
    INetFwRule.get_RemotePorts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(19, 'get_RemotePorts', ((1, 'portNumbers'),)))
    INetFwRule.put_RemotePorts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(20, 'put_RemotePorts', ((1, 'portNumbers'),)))
    INetFwRule.get_LocalAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(21, 'get_LocalAddresses', ((1, 'localAddrs'),)))
    INetFwRule.put_LocalAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(22, 'put_LocalAddresses', ((1, 'localAddrs'),)))
    INetFwRule.get_RemoteAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(23, 'get_RemoteAddresses', ((1, 'remoteAddrs'),)))
    INetFwRule.put_RemoteAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(24, 'put_RemoteAddresses', ((1, 'remoteAddrs'),)))
    INetFwRule.get_IcmpTypesAndCodes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(25, 'get_IcmpTypesAndCodes', ((1, 'icmpTypesAndCodes'),)))
    INetFwRule.put_IcmpTypesAndCodes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(26, 'put_IcmpTypesAndCodes', ((1, 'icmpTypesAndCodes'),)))
    INetFwRule.get_Direction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_RULE_DIRECTION))(27, 'get_Direction', ((1, 'dir'),)))
    INetFwRule.put_Direction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_RULE_DIRECTION)(28, 'put_Direction', ((1, 'dir'),)))
    INetFwRule.get_Interfaces = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(29, 'get_Interfaces', ((1, 'interfaces'),)))
    INetFwRule.put_Interfaces = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(30, 'put_Interfaces', ((1, 'interfaces'),)))
    INetFwRule.get_InterfaceTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(31, 'get_InterfaceTypes', ((1, 'interfaceTypes'),)))
    INetFwRule.put_InterfaceTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(32, 'put_InterfaceTypes', ((1, 'interfaceTypes'),)))
    INetFwRule.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(33, 'get_Enabled', ((1, 'enabled'),)))
    INetFwRule.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(34, 'put_Enabled', ((1, 'enabled'),)))
    INetFwRule.get_Grouping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(35, 'get_Grouping', ((1, 'context'),)))
    INetFwRule.put_Grouping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(36, 'put_Grouping', ((1, 'context'),)))
    INetFwRule.get_Profiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(37, 'get_Profiles', ((1, 'profileTypesBitmask'),)))
    INetFwRule.put_Profiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(38, 'put_Profiles', ((1, 'profileTypesBitmask'),)))
    INetFwRule.get_EdgeTraversal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(39, 'get_EdgeTraversal', ((1, 'enabled'),)))
    INetFwRule.put_EdgeTraversal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(40, 'put_EdgeTraversal', ((1, 'enabled'),)))
    INetFwRule.get_Action = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_ACTION))(41, 'get_Action', ((1, 'action'),)))
    INetFwRule.put_Action = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_ACTION)(42, 'put_Action', ((1, 'action'),)))
    win32more.System.Com.IDispatch
    return INetFwRule
def _define_INetFwRule2_head():
    class INetFwRule2(win32more.NetworkManagement.WindowsFirewall.INetFwRule_head):
        Guid = Guid('9c27c8da-189b-4dde-89-f7-8b-39-a3-16-78-2c')
    return INetFwRule2
def _define_INetFwRule2():
    INetFwRule2 = win32more.NetworkManagement.WindowsFirewall.INetFwRule2_head
    INetFwRule2.get_EdgeTraversalOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(43, 'get_EdgeTraversalOptions', ((1, 'lOptions'),)))
    INetFwRule2.put_EdgeTraversalOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(44, 'put_EdgeTraversalOptions', ((1, 'lOptions'),)))
    win32more.NetworkManagement.WindowsFirewall.INetFwRule
    return INetFwRule2
def _define_INetFwRule3_head():
    class INetFwRule3(win32more.NetworkManagement.WindowsFirewall.INetFwRule2_head):
        Guid = Guid('b21563ff-d696-4222-ab-46-4e-89-b7-3a-b3-4a')
    return INetFwRule3
def _define_INetFwRule3():
    INetFwRule3 = win32more.NetworkManagement.WindowsFirewall.INetFwRule3_head
    INetFwRule3.get_LocalAppPackageId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(45, 'get_LocalAppPackageId', ((1, 'wszPackageId'),)))
    INetFwRule3.put_LocalAppPackageId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(46, 'put_LocalAppPackageId', ((1, 'wszPackageId'),)))
    INetFwRule3.get_LocalUserOwner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(47, 'get_LocalUserOwner', ((1, 'wszUserOwner'),)))
    INetFwRule3.put_LocalUserOwner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(48, 'put_LocalUserOwner', ((1, 'wszUserOwner'),)))
    INetFwRule3.get_LocalUserAuthorizedList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(49, 'get_LocalUserAuthorizedList', ((1, 'wszUserAuthList'),)))
    INetFwRule3.put_LocalUserAuthorizedList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(50, 'put_LocalUserAuthorizedList', ((1, 'wszUserAuthList'),)))
    INetFwRule3.get_RemoteUserAuthorizedList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(51, 'get_RemoteUserAuthorizedList', ((1, 'wszUserAuthList'),)))
    INetFwRule3.put_RemoteUserAuthorizedList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(52, 'put_RemoteUserAuthorizedList', ((1, 'wszUserAuthList'),)))
    INetFwRule3.get_RemoteMachineAuthorizedList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(53, 'get_RemoteMachineAuthorizedList', ((1, 'wszUserAuthList'),)))
    INetFwRule3.put_RemoteMachineAuthorizedList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(54, 'put_RemoteMachineAuthorizedList', ((1, 'wszUserAuthList'),)))
    INetFwRule3.get_SecureFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(55, 'get_SecureFlags', ((1, 'lOptions'),)))
    INetFwRule3.put_SecureFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(56, 'put_SecureFlags', ((1, 'lOptions'),)))
    win32more.NetworkManagement.WindowsFirewall.INetFwRule2
    return INetFwRule3
def _define_INetFwRules_head():
    class INetFwRules(win32more.System.Com.IDispatch_head):
        Guid = Guid('9c4c6277-5027-441e-af-ae-ca-1f-54-2d-a0-09')
    return INetFwRules
def _define_INetFwRules():
    INetFwRules = win32more.NetworkManagement.WindowsFirewall.INetFwRules_head
    INetFwRules.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'count'),)))
    INetFwRules.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.INetFwRule_head)(8, 'Add', ((1, 'rule'),)))
    INetFwRules.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(9, 'Remove', ((1, 'name'),)))
    INetFwRules.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwRule_head))(10, 'Item', ((1, 'name'),(1, 'rule'),)))
    INetFwRules.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(11, 'get__NewEnum', ((1, 'newEnum'),)))
    win32more.System.Com.IDispatch
    return INetFwRules
def _define_INetFwService_head():
    class INetFwService(win32more.System.Com.IDispatch_head):
        Guid = Guid('79fd57c8-908e-4a36-98-88-d5-b3-f0-a4-44-cf')
    return INetFwService
def _define_INetFwService():
    INetFwService = win32more.NetworkManagement.WindowsFirewall.INetFwService_head
    INetFwService.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Name', ((1, 'name'),)))
    INetFwService.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_SERVICE_TYPE))(8, 'get_Type', ((1, 'type'),)))
    INetFwService.get_Customized = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(9, 'get_Customized', ((1, 'customized'),)))
    INetFwService.get_IpVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION))(10, 'get_IpVersion', ((1, 'ipVersion'),)))
    INetFwService.put_IpVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION)(11, 'put_IpVersion', ((1, 'ipVersion'),)))
    INetFwService.get_Scope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_SCOPE))(12, 'get_Scope', ((1, 'scope'),)))
    INetFwService.put_Scope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_SCOPE)(13, 'put_Scope', ((1, 'scope'),)))
    INetFwService.get_RemoteAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(14, 'get_RemoteAddresses', ((1, 'remoteAddrs'),)))
    INetFwService.put_RemoteAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(15, 'put_RemoteAddresses', ((1, 'remoteAddrs'),)))
    INetFwService.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(16, 'get_Enabled', ((1, 'enabled'),)))
    INetFwService.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(17, 'put_Enabled', ((1, 'enabled'),)))
    INetFwService.get_GloballyOpenPorts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwOpenPorts_head))(18, 'get_GloballyOpenPorts', ((1, 'openPorts'),)))
    win32more.System.Com.IDispatch
    return INetFwService
def _define_INetFwServiceRestriction_head():
    class INetFwServiceRestriction(win32more.System.Com.IDispatch_head):
        Guid = Guid('8267bbe3-f890-491c-b7-b6-2d-b1-ef-0e-5d-2b')
    return INetFwServiceRestriction
def _define_INetFwServiceRestriction():
    INetFwServiceRestriction = win32more.NetworkManagement.WindowsFirewall.INetFwServiceRestriction_head
    INetFwServiceRestriction.RestrictService = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.VARIANT_BOOL,win32more.Foundation.VARIANT_BOOL)(7, 'RestrictService', ((1, 'serviceName'),(1, 'appName'),(1, 'restrictService'),(1, 'serviceSidRestricted'),)))
    INetFwServiceRestriction.ServiceRestricted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.Foundation.VARIANT_BOOL))(8, 'ServiceRestricted', ((1, 'serviceName'),(1, 'appName'),(1, 'serviceRestricted'),)))
    INetFwServiceRestriction.get_Rules = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwRules_head))(9, 'get_Rules', ((1, 'rules'),)))
    win32more.System.Com.IDispatch
    return INetFwServiceRestriction
def _define_INetFwServices_head():
    class INetFwServices(win32more.System.Com.IDispatch_head):
        Guid = Guid('79649bb4-903e-421b-94-c9-79-84-8e-79-f6-ee')
    return INetFwServices
def _define_INetFwServices():
    INetFwServices = win32more.NetworkManagement.WindowsFirewall.INetFwServices_head
    INetFwServices.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'count'),)))
    INetFwServices.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_SERVICE_TYPE,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwService_head))(8, 'Item', ((1, 'svcType'),(1, 'service'),)))
    INetFwServices.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(9, 'get__NewEnum', ((1, 'newEnum'),)))
    win32more.System.Com.IDispatch
    return INetFwServices
def _define_INetSharingConfiguration_head():
    class INetSharingConfiguration(win32more.System.Com.IDispatch_head):
        Guid = Guid('c08956b6-1cd3-11d1-b1-c5-00-80-5f-c1-27-0e')
    return INetSharingConfiguration
def _define_INetSharingConfiguration():
    INetSharingConfiguration = win32more.NetworkManagement.WindowsFirewall.INetSharingConfiguration_head
    INetSharingConfiguration.get_SharingEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(7, 'get_SharingEnabled', ((1, 'pbEnabled'),)))
    INetSharingConfiguration.get_SharingConnectionType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.SHARINGCONNECTIONTYPE))(8, 'get_SharingConnectionType', ((1, 'pType'),)))
    INetSharingConfiguration.DisableSharing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(9, 'DisableSharing', ()))
    INetSharingConfiguration.EnableSharing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.SHARINGCONNECTIONTYPE)(10, 'EnableSharing', ((1, 'Type'),)))
    INetSharingConfiguration.get_InternetFirewallEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(11, 'get_InternetFirewallEnabled', ((1, 'pbEnabled'),)))
    INetSharingConfiguration.DisableInternetFirewall = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(12, 'DisableInternetFirewall', ()))
    INetSharingConfiguration.EnableInternetFirewall = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(13, 'EnableInternetFirewall', ()))
    INetSharingConfiguration.get_EnumPortMappings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.SHARINGCONNECTION_ENUM_FLAGS,POINTER(win32more.NetworkManagement.WindowsFirewall.INetSharingPortMappingCollection_head))(14, 'get_EnumPortMappings', ((1, 'Flags'),(1, 'ppColl'),)))
    INetSharingConfiguration.AddPortMapping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Byte,UInt16,UInt16,UInt32,win32more.Foundation.BSTR,win32more.NetworkManagement.WindowsFirewall.ICS_TARGETTYPE,POINTER(win32more.NetworkManagement.WindowsFirewall.INetSharingPortMapping_head))(15, 'AddPortMapping', ((1, 'bstrName'),(1, 'ucIPProtocol'),(1, 'usExternalPort'),(1, 'usInternalPort'),(1, 'dwOptions'),(1, 'bstrTargetNameOrIPAddress'),(1, 'eTargetType'),(1, 'ppMapping'),)))
    INetSharingConfiguration.RemovePortMapping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.INetSharingPortMapping_head)(16, 'RemovePortMapping', ((1, 'pMapping'),)))
    win32more.System.Com.IDispatch
    return INetSharingConfiguration
def _define_INetSharingEveryConnectionCollection_head():
    class INetSharingEveryConnectionCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('33c4643c-7811-46fa-a8-9a-76-85-97-bd-72-23')
    return INetSharingEveryConnectionCollection
def _define_INetSharingEveryConnectionCollection():
    INetSharingEveryConnectionCollection = win32more.NetworkManagement.WindowsFirewall.INetSharingEveryConnectionCollection_head
    INetSharingEveryConnectionCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(7, 'get__NewEnum', ((1, 'pVal'),)))
    INetSharingEveryConnectionCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(8, 'get_Count', ((1, 'pVal'),)))
    win32more.System.Com.IDispatch
    return INetSharingEveryConnectionCollection
def _define_INetSharingManager_head():
    class INetSharingManager(win32more.System.Com.IDispatch_head):
        Guid = Guid('c08956b7-1cd3-11d1-b1-c5-00-80-5f-c1-27-0e')
    return INetSharingManager
def _define_INetSharingManager():
    INetSharingManager = win32more.NetworkManagement.WindowsFirewall.INetSharingManager_head
    INetSharingManager.get_SharingInstalled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(7, 'get_SharingInstalled', ((1, 'pbInstalled'),)))
    INetSharingManager.get_EnumPublicConnections = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.SHARINGCONNECTION_ENUM_FLAGS,POINTER(win32more.NetworkManagement.WindowsFirewall.INetSharingPublicConnectionCollection_head))(8, 'get_EnumPublicConnections', ((1, 'Flags'),(1, 'ppColl'),)))
    INetSharingManager.get_EnumPrivateConnections = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.SHARINGCONNECTION_ENUM_FLAGS,POINTER(win32more.NetworkManagement.WindowsFirewall.INetSharingPrivateConnectionCollection_head))(9, 'get_EnumPrivateConnections', ((1, 'Flags'),(1, 'ppColl'),)))
    INetSharingManager.get_INetSharingConfigurationForINetConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.INetConnection_head,POINTER(win32more.NetworkManagement.WindowsFirewall.INetSharingConfiguration_head))(10, 'get_INetSharingConfigurationForINetConnection', ((1, 'pNetConnection'),(1, 'ppNetSharingConfiguration'),)))
    INetSharingManager.get_EnumEveryConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INetSharingEveryConnectionCollection_head))(11, 'get_EnumEveryConnection', ((1, 'ppColl'),)))
    INetSharingManager.get_NetConnectionProps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.INetConnection_head,POINTER(win32more.NetworkManagement.WindowsFirewall.INetConnectionProps_head))(12, 'get_NetConnectionProps', ((1, 'pNetConnection'),(1, 'ppProps'),)))
    win32more.System.Com.IDispatch
    return INetSharingManager
def _define_INetSharingPortMapping_head():
    class INetSharingPortMapping(win32more.System.Com.IDispatch_head):
        Guid = Guid('c08956b1-1cd3-11d1-b1-c5-00-80-5f-c1-27-0e')
    return INetSharingPortMapping
def _define_INetSharingPortMapping():
    INetSharingPortMapping = win32more.NetworkManagement.WindowsFirewall.INetSharingPortMapping_head
    INetSharingPortMapping.Disable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'Disable', ()))
    INetSharingPortMapping.Enable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'Enable', ()))
    INetSharingPortMapping.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INetSharingPortMappingProps_head))(9, 'get_Properties', ((1, 'ppNSPMP'),)))
    INetSharingPortMapping.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(10, 'Delete', ()))
    win32more.System.Com.IDispatch
    return INetSharingPortMapping
def _define_INetSharingPortMappingCollection_head():
    class INetSharingPortMappingCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('02e4a2de-da20-4e34-89-c8-ac-22-27-5a-01-0b')
    return INetSharingPortMappingCollection
def _define_INetSharingPortMappingCollection():
    INetSharingPortMappingCollection = win32more.NetworkManagement.WindowsFirewall.INetSharingPortMappingCollection_head
    INetSharingPortMappingCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(7, 'get__NewEnum', ((1, 'pVal'),)))
    INetSharingPortMappingCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(8, 'get_Count', ((1, 'pVal'),)))
    win32more.System.Com.IDispatch
    return INetSharingPortMappingCollection
def _define_INetSharingPortMappingProps_head():
    class INetSharingPortMappingProps(win32more.System.Com.IDispatch_head):
        Guid = Guid('24b7e9b5-e38f-4685-85-1b-00-89-2c-f5-f9-40')
    return INetSharingPortMappingProps
def _define_INetSharingPortMappingProps():
    INetSharingPortMappingProps = win32more.NetworkManagement.WindowsFirewall.INetSharingPortMappingProps_head
    INetSharingPortMappingProps.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Name', ((1, 'pbstrName'),)))
    INetSharingPortMappingProps.get_IPProtocol = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no)(8, 'get_IPProtocol', ((1, 'pucIPProt'),)))
    INetSharingPortMappingProps.get_ExternalPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_ExternalPort', ((1, 'pusPort'),)))
    INetSharingPortMappingProps.get_InternalPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(10, 'get_InternalPort', ((1, 'pusPort'),)))
    INetSharingPortMappingProps.get_Options = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(11, 'get_Options', ((1, 'pdwOptions'),)))
    INetSharingPortMappingProps.get_TargetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_TargetName', ((1, 'pbstrTargetName'),)))
    INetSharingPortMappingProps.get_TargetIPAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(13, 'get_TargetIPAddress', ((1, 'pbstrTargetIPAddress'),)))
    INetSharingPortMappingProps.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(14, 'get_Enabled', ((1, 'pbool'),)))
    win32more.System.Com.IDispatch
    return INetSharingPortMappingProps
def _define_INetSharingPrivateConnectionCollection_head():
    class INetSharingPrivateConnectionCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('38ae69e0-4409-402a-a2-cb-e9-65-c7-27-f8-40')
    return INetSharingPrivateConnectionCollection
def _define_INetSharingPrivateConnectionCollection():
    INetSharingPrivateConnectionCollection = win32more.NetworkManagement.WindowsFirewall.INetSharingPrivateConnectionCollection_head
    INetSharingPrivateConnectionCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(7, 'get__NewEnum', ((1, 'pVal'),)))
    INetSharingPrivateConnectionCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(8, 'get_Count', ((1, 'pVal'),)))
    win32more.System.Com.IDispatch
    return INetSharingPrivateConnectionCollection
def _define_INetSharingPublicConnectionCollection_head():
    class INetSharingPublicConnectionCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('7d7a6355-f372-4971-a1-49-bf-c9-27-be-76-2a')
    return INetSharingPublicConnectionCollection
def _define_INetSharingPublicConnectionCollection():
    INetSharingPublicConnectionCollection = win32more.NetworkManagement.WindowsFirewall.INetSharingPublicConnectionCollection_head
    INetSharingPublicConnectionCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(7, 'get__NewEnum', ((1, 'pVal'),)))
    INetSharingPublicConnectionCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(8, 'get_Count', ((1, 'pVal'),)))
    win32more.System.Com.IDispatch
    return INetSharingPublicConnectionCollection
def _define_IStaticPortMapping_head():
    class IStaticPortMapping(win32more.System.Com.IDispatch_head):
        Guid = Guid('6f10711f-729b-41e5-93-b8-f2-1d-0f-81-8d-f1')
    return IStaticPortMapping
def _define_IStaticPortMapping():
    IStaticPortMapping = win32more.NetworkManagement.WindowsFirewall.IStaticPortMapping_head
    IStaticPortMapping.get_ExternalIPAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_ExternalIPAddress', ((1, 'pVal'),)))
    IStaticPortMapping.get_ExternalPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(8, 'get_ExternalPort', ((1, 'pVal'),)))
    IStaticPortMapping.get_InternalPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_InternalPort', ((1, 'pVal'),)))
    IStaticPortMapping.get_Protocol = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_Protocol', ((1, 'pVal'),)))
    IStaticPortMapping.get_InternalClient = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_InternalClient', ((1, 'pVal'),)))
    IStaticPortMapping.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(12, 'get_Enabled', ((1, 'pVal'),)))
    IStaticPortMapping.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(13, 'get_Description', ((1, 'pVal'),)))
    IStaticPortMapping.EditInternalClient = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(14, 'EditInternalClient', ((1, 'bstrInternalClient'),)))
    IStaticPortMapping.Enable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(15, 'Enable', ((1, 'vb'),)))
    IStaticPortMapping.EditDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(16, 'EditDescription', ((1, 'bstrDescription'),)))
    IStaticPortMapping.EditInternalPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(17, 'EditInternalPort', ((1, 'lInternalPort'),)))
    win32more.System.Com.IDispatch
    return IStaticPortMapping
def _define_IStaticPortMappingCollection_head():
    class IStaticPortMappingCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('cd1f3e77-66d6-4664-82-c7-36-db-b6-41-d0-f1')
    return IStaticPortMappingCollection
def _define_IStaticPortMappingCollection():
    IStaticPortMappingCollection = win32more.NetworkManagement.WindowsFirewall.IStaticPortMappingCollection_head
    IStaticPortMappingCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(7, 'get__NewEnum', ((1, 'pVal'),)))
    IStaticPortMappingCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,POINTER(win32more.NetworkManagement.WindowsFirewall.IStaticPortMapping_head))(8, 'get_Item', ((1, 'lExternalPort'),(1, 'bstrProtocol'),(1, 'ppSPM'),)))
    IStaticPortMappingCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_Count', ((1, 'pVal'),)))
    IStaticPortMappingCollection.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR)(10, 'Remove', ((1, 'lExternalPort'),(1, 'bstrProtocol'),)))
    IStaticPortMappingCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,Int32,win32more.Foundation.BSTR,win32more.Foundation.VARIANT_BOOL,win32more.Foundation.BSTR,POINTER(win32more.NetworkManagement.WindowsFirewall.IStaticPortMapping_head))(11, 'Add', ((1, 'lExternalPort'),(1, 'bstrProtocol'),(1, 'lInternalPort'),(1, 'bstrInternalClient'),(1, 'bEnabled'),(1, 'bstrDescription'),(1, 'ppSPM'),)))
    win32more.System.Com.IDispatch
    return IStaticPortMappingCollection
def _define_IUPnPNAT_head():
    class IUPnPNAT(win32more.System.Com.IDispatch_head):
        Guid = Guid('b171c812-cc76-485a-94-d8-b6-b3-a2-79-4e-99')
    return IUPnPNAT
def _define_IUPnPNAT():
    IUPnPNAT = win32more.NetworkManagement.WindowsFirewall.IUPnPNAT_head
    IUPnPNAT.get_StaticPortMappingCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.IStaticPortMappingCollection_head))(7, 'get_StaticPortMappingCollection', ((1, 'ppSPMs'),)))
    IUPnPNAT.get_DynamicPortMappingCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.IDynamicPortMappingCollection_head))(8, 'get_DynamicPortMappingCollection', ((1, 'ppDPMs'),)))
    IUPnPNAT.get_NATEventManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INATEventManager_head))(9, 'get_NATEventManager', ((1, 'ppNEM'),)))
    win32more.System.Com.IDispatch
    return IUPnPNAT
NET_FW_ACTION = Int32
NET_FW_ACTION_BLOCK = 0
NET_FW_ACTION_ALLOW = 1
NET_FW_ACTION_MAX = 2
NET_FW_AUTHENTICATE_TYPE = Int32
NET_FW_AUTHENTICATE_NONE = 0
NET_FW_AUTHENTICATE_NO_ENCAPSULATION = 1
NET_FW_AUTHENTICATE_WITH_INTEGRITY = 2
NET_FW_AUTHENTICATE_AND_NEGOTIATE_ENCRYPTION = 3
NET_FW_AUTHENTICATE_AND_ENCRYPT = 4
NET_FW_EDGE_TRAVERSAL_TYPE = Int32
NET_FW_EDGE_TRAVERSAL_TYPE_DENY = 0
NET_FW_EDGE_TRAVERSAL_TYPE_ALLOW = 1
NET_FW_EDGE_TRAVERSAL_TYPE_DEFER_TO_APP = 2
NET_FW_EDGE_TRAVERSAL_TYPE_DEFER_TO_USER = 3
NET_FW_IP_PROTOCOL = Int32
NET_FW_IP_PROTOCOL_TCP = 6
NET_FW_IP_PROTOCOL_UDP = 17
NET_FW_IP_PROTOCOL_ANY = 256
NET_FW_IP_VERSION = Int32
NET_FW_IP_VERSION_V4 = 0
NET_FW_IP_VERSION_V6 = 1
NET_FW_IP_VERSION_ANY = 2
NET_FW_IP_VERSION_MAX = 3
NET_FW_MODIFY_STATE = Int32
NET_FW_MODIFY_STATE_OK = 0
NET_FW_MODIFY_STATE_GP_OVERRIDE = 1
NET_FW_MODIFY_STATE_INBOUND_BLOCKED = 2
NET_FW_POLICY_TYPE = Int32
NET_FW_POLICY_GROUP = 0
NET_FW_POLICY_LOCAL = 1
NET_FW_POLICY_EFFECTIVE = 2
NET_FW_POLICY_TYPE_MAX = 3
NET_FW_PROFILE_TYPE = Int32
NET_FW_PROFILE_DOMAIN = 0
NET_FW_PROFILE_STANDARD = 1
NET_FW_PROFILE_CURRENT = 2
NET_FW_PROFILE_TYPE_MAX = 3
NET_FW_PROFILE_TYPE2 = Int32
NET_FW_PROFILE2_DOMAIN = 1
NET_FW_PROFILE2_PRIVATE = 2
NET_FW_PROFILE2_PUBLIC = 4
NET_FW_PROFILE2_ALL = 2147483647
NET_FW_RULE_CATEGORY = Int32
NET_FW_RULE_CATEGORY_BOOT = 0
NET_FW_RULE_CATEGORY_STEALTH = 1
NET_FW_RULE_CATEGORY_FIREWALL = 2
NET_FW_RULE_CATEGORY_CONSEC = 3
NET_FW_RULE_CATEGORY_MAX = 4
NET_FW_RULE_DIRECTION = Int32
NET_FW_RULE_DIR_IN = 1
NET_FW_RULE_DIR_OUT = 2
NET_FW_RULE_DIR_MAX = 3
NET_FW_SCOPE = Int32
NET_FW_SCOPE_ALL = 0
NET_FW_SCOPE_LOCAL_SUBNET = 1
NET_FW_SCOPE_CUSTOM = 2
NET_FW_SCOPE_MAX = 3
NET_FW_SERVICE_TYPE = Int32
NET_FW_SERVICE_FILE_AND_PRINT = 0
NET_FW_SERVICE_UPNP = 1
NET_FW_SERVICE_REMOTE_DESKTOP = 2
NET_FW_SERVICE_NONE = 3
NET_FW_SERVICE_TYPE_MAX = 4
NETCON_CHARACTERISTIC_FLAGS = Int32
NCCF_NONE = 0
NCCF_ALL_USERS = 1
NCCF_ALLOW_DUPLICATION = 2
NCCF_ALLOW_REMOVAL = 4
NCCF_ALLOW_RENAME = 8
NCCF_INCOMING_ONLY = 32
NCCF_OUTGOING_ONLY = 64
NCCF_BRANDED = 128
NCCF_SHARED = 256
NCCF_BRIDGED = 512
NCCF_FIREWALLED = 1024
NCCF_DEFAULT = 2048
NCCF_HOMENET_CAPABLE = 4096
NCCF_SHARED_PRIVATE = 8192
NCCF_QUARANTINED = 16384
NCCF_RESERVED = 32768
NCCF_HOSTED_NETWORK = 65536
NCCF_VIRTUAL_STATION = 131072
NCCF_WIFI_DIRECT = 262144
NCCF_BLUETOOTH_MASK = 983040
NCCF_LAN_MASK = 15728640
NETCON_MEDIATYPE = Int32
NCM_NONE = 0
NCM_DIRECT = 1
NCM_ISDN = 2
NCM_LAN = 3
NCM_PHONE = 4
NCM_TUNNEL = 5
NCM_PPPOE = 6
NCM_BRIDGE = 7
NCM_SHAREDACCESSHOST_LAN = 8
NCM_SHAREDACCESSHOST_RAS = 9
def _define_NETCON_PROPERTIES_head():
    class NETCON_PROPERTIES(Structure):
        pass
    return NETCON_PROPERTIES
def _define_NETCON_PROPERTIES():
    NETCON_PROPERTIES = win32more.NetworkManagement.WindowsFirewall.NETCON_PROPERTIES_head
    NETCON_PROPERTIES._fields_ = [
        ('guidId', Guid),
        ('pszwName', win32more.Foundation.PWSTR),
        ('pszwDeviceName', win32more.Foundation.PWSTR),
        ('Status', win32more.NetworkManagement.WindowsFirewall.NETCON_STATUS),
        ('MediaType', win32more.NetworkManagement.WindowsFirewall.NETCON_MEDIATYPE),
        ('dwCharacter', UInt32),
        ('clsidThisObject', Guid),
        ('clsidUiObject', Guid),
    ]
    return NETCON_PROPERTIES
NETCON_STATUS = Int32
NCS_DISCONNECTED = 0
NCS_CONNECTING = 1
NCS_CONNECTED = 2
NCS_DISCONNECTING = 3
NCS_HARDWARE_NOT_PRESENT = 4
NCS_HARDWARE_DISABLED = 5
NCS_HARDWARE_MALFUNCTION = 6
NCS_MEDIA_DISCONNECTED = 7
NCS_AUTHENTICATING = 8
NCS_AUTHENTICATION_SUCCEEDED = 9
NCS_AUTHENTICATION_FAILED = 10
NCS_INVALID_ADDRESS = 11
NCS_CREDENTIALS_REQUIRED = 12
NCS_ACTION_REQUIRED = 13
NCS_ACTION_REQUIRED_RETRY = 14
NCS_CONNECT_FAILED = 15
NETCON_TYPE = Int32
NCT_DIRECT_CONNECT = 0
NCT_INBOUND = 1
NCT_INTERNET = 2
NCT_LAN = 3
NCT_PHONE = 4
NCT_TUNNEL = 5
NCT_BRIDGE = 6
NETCONMGR_ENUM_FLAGS = Int32
NCME_DEFAULT = 0
NCME_HIDDEN = 1
NETCONUI_CONNECT_FLAGS = Int32
NCUC_DEFAULT = 0
NCUC_NO_UI = 1
NCUC_ENABLE_DISABLE = 2
NetFwAuthorizedApplication = Guid('ec9846b3-2762-4a6b-a2-14-6a-cb-60-34-62-d2')
NetFwMgr = Guid('304ce942-6e39-40d8-94-3a-b9-13-c4-0c-9c-d4')
NetFwOpenPort = Guid('0ca545c6-37ad-4a6c-bf-92-9f-76-10-06-7e-f5')
NetFwPolicy2 = Guid('e2b3c97f-6ae1-41ac-81-7a-f6-f9-21-66-d7-dd')
NetFwProduct = Guid('9d745ed8-c514-4d1d-bf-42-75-1f-ed-2d-5a-c7')
NetFwProducts = Guid('cc19079b-8272-4d73-bb-70-cd-b5-33-52-7b-61')
NetFwRule = Guid('2c5bc43e-3369-4c33-ab-0c-be-94-69-67-7a-f4')
NETISO_ERROR_TYPE = Int32
NETISO_ERROR_TYPE_NONE = 0
NETISO_ERROR_TYPE_PRIVATE_NETWORK = 1
NETISO_ERROR_TYPE_INTERNET_CLIENT = 2
NETISO_ERROR_TYPE_INTERNET_CLIENT_SERVER = 3
NETISO_ERROR_TYPE_MAX = 4
NETISO_FLAG = Int32
NETISO_FLAG_FORCE_COMPUTE_BINARIES = 1
NETISO_FLAG_MAX = 2
NetSharingManager = Guid('5c63c1ad-3956-4ff8-84-86-40-03-47-58-31-5b')
def _define_PAC_CHANGES_CALLBACK_FN():
    return WINFUNCTYPE(Void,c_void_p,POINTER(win32more.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_CHANGE_head))
def _define_PFN_FWADDDYNAMICKEYWORDADDRESS0():
    return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.WindowsFirewall.FW_DYNAMIC_KEYWORD_ADDRESS0_head))
def _define_PFN_FWDELETEDYNAMICKEYWORDADDRESS0():
    return WINFUNCTYPE(UInt32,Guid)
def _define_PFN_FWENUMDYNAMICKEYWORDADDRESSBYID0():
    return WINFUNCTYPE(UInt32,Guid,POINTER(POINTER(win32more.NetworkManagement.WindowsFirewall.FW_DYNAMIC_KEYWORD_ADDRESS_DATA0_head)))
def _define_PFN_FWENUMDYNAMICKEYWORDADDRESSESBYTYPE0():
    return WINFUNCTYPE(UInt32,UInt32,POINTER(POINTER(win32more.NetworkManagement.WindowsFirewall.FW_DYNAMIC_KEYWORD_ADDRESS_DATA0_head)))
def _define_PFN_FWFREEDYNAMICKEYWORDADDRESSDATA0():
    return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.WindowsFirewall.FW_DYNAMIC_KEYWORD_ADDRESS_DATA0_head))
def _define_PFN_FWUPDATEDYNAMICKEYWORDADDRESS0():
    return WINFUNCTYPE(UInt32,Guid,win32more.Foundation.PWSTR,win32more.Foundation.BOOL)
def _define_PNETISO_EDP_ID_CALLBACK_FN():
    return WINFUNCTYPE(Void,c_void_p,win32more.Foundation.PWSTR,UInt32)
SHARINGCONNECTION_ENUM_FLAGS = Int32
ICSSC_DEFAULT = 0
ICSSC_ENABLED = 1
SHARINGCONNECTIONTYPE = Int32
ICSSHARINGTYPE_PUBLIC = 0
ICSSHARINGTYPE_PRIVATE = 1
UPnPNAT = Guid('ae1e00aa-3fd5-403c-8a-27-2b-bd-c3-0c-d0-e1')
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
