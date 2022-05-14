from win32more import *
import win32more.NetworkManagement.WindowsFirewall
import win32more.Foundation
import win32more.Security
import win32more.System.Com

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.NetworkManagement.WindowsFirewall, name, eval(f"_define_{name}()"))
    return getattr(win32more.NetworkManagement.WindowsFirewall, name)
NETCON_MAX_NAME_LEN = 256
S_OBJECT_NO_LONGER_VALID = 2
NETISO_GEID_FOR_WDAG = 1
NETISO_GEID_FOR_NEUTRAL_AWARE = 2
UPnPNAT = Guid('ae1e00aa-3fd5-403c-8a27-2bbdc30cd0e1')
def _define_IUPnPNAT_head():
    class IUPnPNAT(win32more.System.Com.IDispatch_head):
        Guid = Guid('b171c812-cc76-485a-94d8-b6b3a2794e99')
    return IUPnPNAT
def _define_IUPnPNAT():
    IUPnPNAT = win32more.NetworkManagement.WindowsFirewall.IUPnPNAT_head
    IUPnPNAT.get_StaticPortMappingCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.IStaticPortMappingCollection_head), use_last_error=False)(7, 'get_StaticPortMappingCollection', ((1, 'ppSPMs'),)))
    IUPnPNAT.get_DynamicPortMappingCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.IDynamicPortMappingCollection_head), use_last_error=False)(8, 'get_DynamicPortMappingCollection', ((1, 'ppDPMs'),)))
    IUPnPNAT.get_NATEventManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INATEventManager_head), use_last_error=False)(9, 'get_NATEventManager', ((1, 'ppNEM'),)))
    return IUPnPNAT
def _define_INATEventManager_head():
    class INATEventManager(win32more.System.Com.IDispatch_head):
        Guid = Guid('624bd588-9060-4109-b0b0-1adbbcac32df')
    return INATEventManager
def _define_INATEventManager():
    INATEventManager = win32more.NetworkManagement.WindowsFirewall.INATEventManager_head
    INATEventManager.put_ExternalIPAddressCallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(7, 'put_ExternalIPAddressCallback', ((1, 'pUnk'),)))
    INATEventManager.put_NumberOfEntriesCallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(8, 'put_NumberOfEntriesCallback', ((1, 'pUnk'),)))
    return INATEventManager
def _define_INATExternalIPAddressCallback_head():
    class INATExternalIPAddressCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('9c416740-a34e-446f-ba06-abd04c3149ae')
    return INATExternalIPAddressCallback
def _define_INATExternalIPAddressCallback():
    INATExternalIPAddressCallback = win32more.NetworkManagement.WindowsFirewall.INATExternalIPAddressCallback_head
    INATExternalIPAddressCallback.NewExternalIPAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(3, 'NewExternalIPAddress', ((1, 'bstrNewExternalIPAddress'),)))
    return INATExternalIPAddressCallback
def _define_INATNumberOfEntriesCallback_head():
    class INATNumberOfEntriesCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('c83a0a74-91ee-41b6-b67a-67e0f00bbd78')
    return INATNumberOfEntriesCallback
def _define_INATNumberOfEntriesCallback():
    INATNumberOfEntriesCallback = win32more.NetworkManagement.WindowsFirewall.INATNumberOfEntriesCallback_head
    INATNumberOfEntriesCallback.NewNumberOfEntries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(3, 'NewNumberOfEntries', ((1, 'lNewNumberOfEntries'),)))
    return INATNumberOfEntriesCallback
def _define_IDynamicPortMappingCollection_head():
    class IDynamicPortMappingCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('b60de00f-156e-4e8d-9ec1-3a2342c10899')
    return IDynamicPortMappingCollection
def _define_IDynamicPortMappingCollection():
    IDynamicPortMappingCollection = win32more.NetworkManagement.WindowsFirewall.IDynamicPortMappingCollection_head
    IDynamicPortMappingCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'pVal'),)))
    IDynamicPortMappingCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.Foundation.BSTR,POINTER(win32more.NetworkManagement.WindowsFirewall.IDynamicPortMapping_head), use_last_error=False)(8, 'get_Item', ((1, 'bstrRemoteHost'),(1, 'lExternalPort'),(1, 'bstrProtocol'),(1, 'ppDPM'),)))
    IDynamicPortMappingCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'pVal'),)))
    IDynamicPortMappingCollection.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.Foundation.BSTR, use_last_error=False)(10, 'Remove', ((1, 'bstrRemoteHost'),(1, 'lExternalPort'),(1, 'bstrProtocol'),)))
    IDynamicPortMappingCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.Foundation.BSTR,Int32,win32more.Foundation.BSTR,Int16,win32more.Foundation.BSTR,Int32,POINTER(win32more.NetworkManagement.WindowsFirewall.IDynamicPortMapping_head), use_last_error=False)(11, 'Add', ((1, 'bstrRemoteHost'),(1, 'lExternalPort'),(1, 'bstrProtocol'),(1, 'lInternalPort'),(1, 'bstrInternalClient'),(1, 'bEnabled'),(1, 'bstrDescription'),(1, 'lLeaseDuration'),(1, 'ppDPM'),)))
    return IDynamicPortMappingCollection
def _define_IDynamicPortMapping_head():
    class IDynamicPortMapping(win32more.System.Com.IDispatch_head):
        Guid = Guid('4fc80282-23b6-4378-9a27-cd8f17c9400c')
    return IDynamicPortMapping
def _define_IDynamicPortMapping():
    IDynamicPortMapping = win32more.NetworkManagement.WindowsFirewall.IDynamicPortMapping_head
    IDynamicPortMapping.get_ExternalIPAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_ExternalIPAddress', ((1, 'pVal'),)))
    IDynamicPortMapping.get_RemoteHost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_RemoteHost', ((1, 'pVal'),)))
    IDynamicPortMapping.get_ExternalPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_ExternalPort', ((1, 'pVal'),)))
    IDynamicPortMapping.get_Protocol = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_Protocol', ((1, 'pVal'),)))
    IDynamicPortMapping.get_InternalPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'get_InternalPort', ((1, 'pVal'),)))
    IDynamicPortMapping.get_InternalClient = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_InternalClient', ((1, 'pVal'),)))
    IDynamicPortMapping.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(13, 'get_Enabled', ((1, 'pVal'),)))
    IDynamicPortMapping.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_Description', ((1, 'pVal'),)))
    IDynamicPortMapping.get_LeaseDuration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(15, 'get_LeaseDuration', ((1, 'pVal'),)))
    IDynamicPortMapping.RenewLease = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32), use_last_error=False)(16, 'RenewLease', ((1, 'lLeaseDurationDesired'),(1, 'pLeaseDurationReturned'),)))
    IDynamicPortMapping.EditInternalClient = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(17, 'EditInternalClient', ((1, 'bstrInternalClient'),)))
    IDynamicPortMapping.Enable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(18, 'Enable', ((1, 'vb'),)))
    IDynamicPortMapping.EditDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(19, 'EditDescription', ((1, 'bstrDescription'),)))
    IDynamicPortMapping.EditInternalPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(20, 'EditInternalPort', ((1, 'lInternalPort'),)))
    return IDynamicPortMapping
def _define_IStaticPortMappingCollection_head():
    class IStaticPortMappingCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('cd1f3e77-66d6-4664-82c7-36dbb641d0f1')
    return IStaticPortMappingCollection
def _define_IStaticPortMappingCollection():
    IStaticPortMappingCollection = win32more.NetworkManagement.WindowsFirewall.IStaticPortMappingCollection_head
    IStaticPortMappingCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'pVal'),)))
    IStaticPortMappingCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,POINTER(win32more.NetworkManagement.WindowsFirewall.IStaticPortMapping_head), use_last_error=False)(8, 'get_Item', ((1, 'lExternalPort'),(1, 'bstrProtocol'),(1, 'ppSPM'),)))
    IStaticPortMappingCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'pVal'),)))
    IStaticPortMappingCollection.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR, use_last_error=False)(10, 'Remove', ((1, 'lExternalPort'),(1, 'bstrProtocol'),)))
    IStaticPortMappingCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,Int32,win32more.Foundation.BSTR,Int16,win32more.Foundation.BSTR,POINTER(win32more.NetworkManagement.WindowsFirewall.IStaticPortMapping_head), use_last_error=False)(11, 'Add', ((1, 'lExternalPort'),(1, 'bstrProtocol'),(1, 'lInternalPort'),(1, 'bstrInternalClient'),(1, 'bEnabled'),(1, 'bstrDescription'),(1, 'ppSPM'),)))
    return IStaticPortMappingCollection
def _define_IStaticPortMapping_head():
    class IStaticPortMapping(win32more.System.Com.IDispatch_head):
        Guid = Guid('6f10711f-729b-41e5-93b8-f21d0f818df1')
    return IStaticPortMapping
def _define_IStaticPortMapping():
    IStaticPortMapping = win32more.NetworkManagement.WindowsFirewall.IStaticPortMapping_head
    IStaticPortMapping.get_ExternalIPAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_ExternalIPAddress', ((1, 'pVal'),)))
    IStaticPortMapping.get_ExternalPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_ExternalPort', ((1, 'pVal'),)))
    IStaticPortMapping.get_InternalPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_InternalPort', ((1, 'pVal'),)))
    IStaticPortMapping.get_Protocol = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_Protocol', ((1, 'pVal'),)))
    IStaticPortMapping.get_InternalClient = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_InternalClient', ((1, 'pVal'),)))
    IStaticPortMapping.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(12, 'get_Enabled', ((1, 'pVal'),)))
    IStaticPortMapping.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_Description', ((1, 'pVal'),)))
    IStaticPortMapping.EditInternalClient = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(14, 'EditInternalClient', ((1, 'bstrInternalClient'),)))
    IStaticPortMapping.Enable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(15, 'Enable', ((1, 'vb'),)))
    IStaticPortMapping.EditDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(16, 'EditDescription', ((1, 'bstrDescription'),)))
    IStaticPortMapping.EditInternalPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(17, 'EditInternalPort', ((1, 'lInternalPort'),)))
    return IStaticPortMapping
NetSharingManager = Guid('5c63c1ad-3956-4ff8-8486-40034758315b')
def _define_IEnumNetConnection_head():
    class IEnumNetConnection(win32more.System.Com.IUnknown_head):
        Guid = Guid('c08956a0-1cd3-11d1-b1c5-00805fc1270e')
    return IEnumNetConnection
def _define_IEnumNetConnection():
    IEnumNetConnection = win32more.NetworkManagement.WindowsFirewall.IEnumNetConnection_head
    IEnumNetConnection.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.NetworkManagement.WindowsFirewall.INetConnection_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumNetConnection.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'celt'),)))
    IEnumNetConnection.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumNetConnection.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.IEnumNetConnection_head), use_last_error=False)(6, 'Clone', ((1, 'ppenum'),)))
    return IEnumNetConnection
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
        ("guidId", Guid),
        ("pszwName", win32more.Foundation.PWSTR),
        ("pszwDeviceName", win32more.Foundation.PWSTR),
        ("Status", win32more.NetworkManagement.WindowsFirewall.NETCON_STATUS),
        ("MediaType", win32more.NetworkManagement.WindowsFirewall.NETCON_MEDIATYPE),
        ("dwCharacter", UInt32),
        ("clsidThisObject", Guid),
        ("clsidUiObject", Guid),
    ]
    return NETCON_PROPERTIES
def _define_INetConnection_head():
    class INetConnection(win32more.System.Com.IUnknown_head):
        Guid = Guid('c08956a1-1cd3-11d1-b1c5-00805fc1270e')
    return INetConnection
def _define_INetConnection():
    INetConnection = win32more.NetworkManagement.WindowsFirewall.INetConnection_head
    INetConnection.Connect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Connect', ()))
    INetConnection.Disconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Disconnect', ()))
    INetConnection.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Delete', ()))
    INetConnection.Duplicate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.WindowsFirewall.INetConnection_head), use_last_error=False)(6, 'Duplicate', ((1, 'pszwDuplicateName'),(1, 'ppCon'),)))
    INetConnection.GetProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.NetworkManagement.WindowsFirewall.NETCON_PROPERTIES_head)), use_last_error=False)(7, 'GetProperties', ((1, 'ppProps'),)))
    INetConnection.GetUiObjectClassId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(8, 'GetUiObjectClassId', ((1, 'pclsid'),)))
    INetConnection.Rename = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(9, 'Rename', ((1, 'pszwNewName'),)))
    return INetConnection
NETCONMGR_ENUM_FLAGS = Int32
NCME_DEFAULT = 0
NCME_HIDDEN = 1
def _define_INetConnectionManager_head():
    class INetConnectionManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('c08956a2-1cd3-11d1-b1c5-00805fc1270e')
    return INetConnectionManager
def _define_INetConnectionManager():
    INetConnectionManager = win32more.NetworkManagement.WindowsFirewall.INetConnectionManager_head
    INetConnectionManager.EnumConnections = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NETCONMGR_ENUM_FLAGS,POINTER(win32more.NetworkManagement.WindowsFirewall.IEnumNetConnection_head), use_last_error=False)(3, 'EnumConnections', ((1, 'Flags'),(1, 'ppEnum'),)))
    return INetConnectionManager
NETCONUI_CONNECT_FLAGS = Int32
NCUC_DEFAULT = 0
NCUC_NO_UI = 1
NCUC_ENABLE_DISABLE = 2
def _define_INetConnectionConnectUi_head():
    class INetConnectionConnectUi(win32more.System.Com.IUnknown_head):
        Guid = Guid('c08956a3-1cd3-11d1-b1c5-00805fc1270e')
    return INetConnectionConnectUi
def _define_INetConnectionConnectUi():
    INetConnectionConnectUi = win32more.NetworkManagement.WindowsFirewall.INetConnectionConnectUi_head
    INetConnectionConnectUi.SetConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.INetConnection_head, use_last_error=False)(3, 'SetConnection', ((1, 'pCon'),)))
    INetConnectionConnectUi.Connect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32, use_last_error=False)(4, 'Connect', ((1, 'hwndParent'),(1, 'dwFlags'),)))
    INetConnectionConnectUi.Disconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32, use_last_error=False)(5, 'Disconnect', ((1, 'hwndParent'),(1, 'dwFlags'),)))
    return INetConnectionConnectUi
def _define_IEnumNetSharingPortMapping_head():
    class IEnumNetSharingPortMapping(win32more.System.Com.IUnknown_head):
        Guid = Guid('c08956b0-1cd3-11d1-b1c5-00805fc1270e')
    return IEnumNetSharingPortMapping
def _define_IEnumNetSharingPortMapping():
    IEnumNetSharingPortMapping = win32more.NetworkManagement.WindowsFirewall.IEnumNetSharingPortMapping_head
    IEnumNetSharingPortMapping.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.VARIANT),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'rgVar'),(1, 'pceltFetched'),)))
    IEnumNetSharingPortMapping.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'celt'),)))
    IEnumNetSharingPortMapping.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumNetSharingPortMapping.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.IEnumNetSharingPortMapping_head), use_last_error=False)(6, 'Clone', ((1, 'ppenum'),)))
    return IEnumNetSharingPortMapping
def _define_INetSharingPortMappingProps_head():
    class INetSharingPortMappingProps(win32more.System.Com.IDispatch_head):
        Guid = Guid('24b7e9b5-e38f-4685-851b-00892cf5f940')
    return INetSharingPortMappingProps
def _define_INetSharingPortMappingProps():
    INetSharingPortMappingProps = win32more.NetworkManagement.WindowsFirewall.INetSharingPortMappingProps_head
    INetSharingPortMappingProps.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Name', ((1, 'pbstrName'),)))
    INetSharingPortMappingProps.get_IPProtocol = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no, use_last_error=False)(8, 'get_IPProtocol', ((1, 'pucIPProt'),)))
    INetSharingPortMappingProps.get_ExternalPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_ExternalPort', ((1, 'pusPort'),)))
    INetSharingPortMappingProps.get_InternalPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_InternalPort', ((1, 'pusPort'),)))
    INetSharingPortMappingProps.get_Options = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'get_Options', ((1, 'pdwOptions'),)))
    INetSharingPortMappingProps.get_TargetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_TargetName', ((1, 'pbstrTargetName'),)))
    INetSharingPortMappingProps.get_TargetIPAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_TargetIPAddress', ((1, 'pbstrTargetIPAddress'),)))
    INetSharingPortMappingProps.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(14, 'get_Enabled', ((1, 'pbool'),)))
    return INetSharingPortMappingProps
def _define_INetSharingPortMapping_head():
    class INetSharingPortMapping(win32more.System.Com.IDispatch_head):
        Guid = Guid('c08956b1-1cd3-11d1-b1c5-00805fc1270e')
    return INetSharingPortMapping
def _define_INetSharingPortMapping():
    INetSharingPortMapping = win32more.NetworkManagement.WindowsFirewall.INetSharingPortMapping_head
    INetSharingPortMapping.Disable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Disable', ()))
    INetSharingPortMapping.Enable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Enable', ()))
    INetSharingPortMapping.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INetSharingPortMappingProps_head), use_last_error=False)(9, 'get_Properties', ((1, 'ppNSPMP'),)))
    INetSharingPortMapping.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'Delete', ()))
    return INetSharingPortMapping
def _define_IEnumNetSharingEveryConnection_head():
    class IEnumNetSharingEveryConnection(win32more.System.Com.IUnknown_head):
        Guid = Guid('c08956b8-1cd3-11d1-b1c5-00805fc1270e')
    return IEnumNetSharingEveryConnection
def _define_IEnumNetSharingEveryConnection():
    IEnumNetSharingEveryConnection = win32more.NetworkManagement.WindowsFirewall.IEnumNetSharingEveryConnection_head
    IEnumNetSharingEveryConnection.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.VARIANT),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'rgVar'),(1, 'pceltFetched'),)))
    IEnumNetSharingEveryConnection.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'celt'),)))
    IEnumNetSharingEveryConnection.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumNetSharingEveryConnection.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.IEnumNetSharingEveryConnection_head), use_last_error=False)(6, 'Clone', ((1, 'ppenum'),)))
    return IEnumNetSharingEveryConnection
def _define_IEnumNetSharingPublicConnection_head():
    class IEnumNetSharingPublicConnection(win32more.System.Com.IUnknown_head):
        Guid = Guid('c08956b4-1cd3-11d1-b1c5-00805fc1270e')
    return IEnumNetSharingPublicConnection
def _define_IEnumNetSharingPublicConnection():
    IEnumNetSharingPublicConnection = win32more.NetworkManagement.WindowsFirewall.IEnumNetSharingPublicConnection_head
    IEnumNetSharingPublicConnection.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.VARIANT),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'rgVar'),(1, 'pceltFetched'),)))
    IEnumNetSharingPublicConnection.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'celt'),)))
    IEnumNetSharingPublicConnection.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumNetSharingPublicConnection.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.IEnumNetSharingPublicConnection_head), use_last_error=False)(6, 'Clone', ((1, 'ppenum'),)))
    return IEnumNetSharingPublicConnection
def _define_IEnumNetSharingPrivateConnection_head():
    class IEnumNetSharingPrivateConnection(win32more.System.Com.IUnknown_head):
        Guid = Guid('c08956b5-1cd3-11d1-b1c5-00805fc1270e')
    return IEnumNetSharingPrivateConnection
def _define_IEnumNetSharingPrivateConnection():
    IEnumNetSharingPrivateConnection = win32more.NetworkManagement.WindowsFirewall.IEnumNetSharingPrivateConnection_head
    IEnumNetSharingPrivateConnection.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.VARIANT),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'rgVar'),(1, 'pCeltFetched'),)))
    IEnumNetSharingPrivateConnection.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'celt'),)))
    IEnumNetSharingPrivateConnection.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumNetSharingPrivateConnection.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.IEnumNetSharingPrivateConnection_head), use_last_error=False)(6, 'Clone', ((1, 'ppenum'),)))
    return IEnumNetSharingPrivateConnection
def _define_INetSharingPortMappingCollection_head():
    class INetSharingPortMappingCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('02e4a2de-da20-4e34-89c8-ac22275a010b')
    return INetSharingPortMappingCollection
def _define_INetSharingPortMappingCollection():
    INetSharingPortMappingCollection = win32more.NetworkManagement.WindowsFirewall.INetSharingPortMappingCollection_head
    INetSharingPortMappingCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'pVal'),)))
    INetSharingPortMappingCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'pVal'),)))
    return INetSharingPortMappingCollection
def _define_INetConnectionProps_head():
    class INetConnectionProps(win32more.System.Com.IDispatch_head):
        Guid = Guid('f4277c95-ce5b-463d-8167-5662d9bcaa72')
    return INetConnectionProps
def _define_INetConnectionProps():
    INetConnectionProps = win32more.NetworkManagement.WindowsFirewall.INetConnectionProps_head
    INetConnectionProps.get_Guid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Guid', ((1, 'pbstrGuid'),)))
    INetConnectionProps.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_Name', ((1, 'pbstrName'),)))
    INetConnectionProps.get_DeviceName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_DeviceName', ((1, 'pbstrDeviceName'),)))
    INetConnectionProps.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NETCON_STATUS), use_last_error=False)(10, 'get_Status', ((1, 'pStatus'),)))
    INetConnectionProps.get_MediaType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NETCON_MEDIATYPE), use_last_error=False)(11, 'get_MediaType', ((1, 'pMediaType'),)))
    INetConnectionProps.get_Characteristics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(12, 'get_Characteristics', ((1, 'pdwFlags'),)))
    return INetConnectionProps
SHARINGCONNECTIONTYPE = Int32
ICSSHARINGTYPE_PUBLIC = 0
ICSSHARINGTYPE_PRIVATE = 1
SHARINGCONNECTION_ENUM_FLAGS = Int32
ICSSC_DEFAULT = 0
ICSSC_ENABLED = 1
ICS_TARGETTYPE = Int32
ICSTT_NAME = 0
ICSTT_IPADDRESS = 1
def _define_INetSharingConfiguration_head():
    class INetSharingConfiguration(win32more.System.Com.IDispatch_head):
        Guid = Guid('c08956b6-1cd3-11d1-b1c5-00805fc1270e')
    return INetSharingConfiguration
def _define_INetSharingConfiguration():
    INetSharingConfiguration = win32more.NetworkManagement.WindowsFirewall.INetSharingConfiguration_head
    INetSharingConfiguration.get_SharingEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(7, 'get_SharingEnabled', ((1, 'pbEnabled'),)))
    INetSharingConfiguration.get_SharingConnectionType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.SHARINGCONNECTIONTYPE), use_last_error=False)(8, 'get_SharingConnectionType', ((1, 'pType'),)))
    INetSharingConfiguration.DisableSharing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'DisableSharing', ()))
    INetSharingConfiguration.EnableSharing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.SHARINGCONNECTIONTYPE, use_last_error=False)(10, 'EnableSharing', ((1, 'Type'),)))
    INetSharingConfiguration.get_InternetFirewallEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(11, 'get_InternetFirewallEnabled', ((1, 'pbEnabled'),)))
    INetSharingConfiguration.DisableInternetFirewall = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'DisableInternetFirewall', ()))
    INetSharingConfiguration.EnableInternetFirewall = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(13, 'EnableInternetFirewall', ()))
    INetSharingConfiguration.get_EnumPortMappings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.SHARINGCONNECTION_ENUM_FLAGS,POINTER(win32more.NetworkManagement.WindowsFirewall.INetSharingPortMappingCollection_head), use_last_error=False)(14, 'get_EnumPortMappings', ((1, 'Flags'),(1, 'ppColl'),)))
    INetSharingConfiguration.AddPortMapping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Byte,UInt16,UInt16,UInt32,win32more.Foundation.BSTR,win32more.NetworkManagement.WindowsFirewall.ICS_TARGETTYPE,POINTER(win32more.NetworkManagement.WindowsFirewall.INetSharingPortMapping_head), use_last_error=False)(15, 'AddPortMapping', ((1, 'bstrName'),(1, 'ucIPProtocol'),(1, 'usExternalPort'),(1, 'usInternalPort'),(1, 'dwOptions'),(1, 'bstrTargetNameOrIPAddress'),(1, 'eTargetType'),(1, 'ppMapping'),)))
    INetSharingConfiguration.RemovePortMapping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.INetSharingPortMapping_head, use_last_error=False)(16, 'RemovePortMapping', ((1, 'pMapping'),)))
    return INetSharingConfiguration
def _define_INetSharingEveryConnectionCollection_head():
    class INetSharingEveryConnectionCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('33c4643c-7811-46fa-a89a-768597bd7223')
    return INetSharingEveryConnectionCollection
def _define_INetSharingEveryConnectionCollection():
    INetSharingEveryConnectionCollection = win32more.NetworkManagement.WindowsFirewall.INetSharingEveryConnectionCollection_head
    INetSharingEveryConnectionCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'pVal'),)))
    INetSharingEveryConnectionCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'pVal'),)))
    return INetSharingEveryConnectionCollection
def _define_INetSharingPublicConnectionCollection_head():
    class INetSharingPublicConnectionCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('7d7a6355-f372-4971-a149-bfc927be762a')
    return INetSharingPublicConnectionCollection
def _define_INetSharingPublicConnectionCollection():
    INetSharingPublicConnectionCollection = win32more.NetworkManagement.WindowsFirewall.INetSharingPublicConnectionCollection_head
    INetSharingPublicConnectionCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'pVal'),)))
    INetSharingPublicConnectionCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'pVal'),)))
    return INetSharingPublicConnectionCollection
def _define_INetSharingPrivateConnectionCollection_head():
    class INetSharingPrivateConnectionCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('38ae69e0-4409-402a-a2cb-e965c727f840')
    return INetSharingPrivateConnectionCollection
def _define_INetSharingPrivateConnectionCollection():
    INetSharingPrivateConnectionCollection = win32more.NetworkManagement.WindowsFirewall.INetSharingPrivateConnectionCollection_head
    INetSharingPrivateConnectionCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'pVal'),)))
    INetSharingPrivateConnectionCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'pVal'),)))
    return INetSharingPrivateConnectionCollection
def _define_INetSharingManager_head():
    class INetSharingManager(win32more.System.Com.IDispatch_head):
        Guid = Guid('c08956b7-1cd3-11d1-b1c5-00805fc1270e')
    return INetSharingManager
def _define_INetSharingManager():
    INetSharingManager = win32more.NetworkManagement.WindowsFirewall.INetSharingManager_head
    INetSharingManager.get_SharingInstalled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(7, 'get_SharingInstalled', ((1, 'pbInstalled'),)))
    INetSharingManager.get_EnumPublicConnections = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.SHARINGCONNECTION_ENUM_FLAGS,POINTER(win32more.NetworkManagement.WindowsFirewall.INetSharingPublicConnectionCollection_head), use_last_error=False)(8, 'get_EnumPublicConnections', ((1, 'Flags'),(1, 'ppColl'),)))
    INetSharingManager.get_EnumPrivateConnections = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.SHARINGCONNECTION_ENUM_FLAGS,POINTER(win32more.NetworkManagement.WindowsFirewall.INetSharingPrivateConnectionCollection_head), use_last_error=False)(9, 'get_EnumPrivateConnections', ((1, 'Flags'),(1, 'ppColl'),)))
    INetSharingManager.get_INetSharingConfigurationForINetConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.INetConnection_head,POINTER(win32more.NetworkManagement.WindowsFirewall.INetSharingConfiguration_head), use_last_error=False)(10, 'get_INetSharingConfigurationForINetConnection', ((1, 'pNetConnection'),(1, 'ppNetSharingConfiguration'),)))
    INetSharingManager.get_EnumEveryConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INetSharingEveryConnectionCollection_head), use_last_error=False)(11, 'get_EnumEveryConnection', ((1, 'ppColl'),)))
    INetSharingManager.get_NetConnectionProps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.INetConnection_head,POINTER(win32more.NetworkManagement.WindowsFirewall.INetConnectionProps_head), use_last_error=False)(12, 'get_NetConnectionProps', ((1, 'pNetConnection'),(1, 'ppProps'),)))
    return INetSharingManager
NetFwRule = Guid('2c5bc43e-3369-4c33-ab0c-be9469677af4')
NetFwOpenPort = Guid('0ca545c6-37ad-4a6c-bf92-9f7610067ef5')
NetFwAuthorizedApplication = Guid('ec9846b3-2762-4a6b-a214-6acb603462d2')
NetFwPolicy2 = Guid('e2b3c97f-6ae1-41ac-817a-f6f92166d7dd')
NetFwProduct = Guid('9d745ed8-c514-4d1d-bf42-751fed2d5ac7')
NetFwProducts = Guid('cc19079b-8272-4d73-bb70-cdb533527b61')
NetFwMgr = Guid('304ce942-6e39-40d8-943a-b913c40c9cd4')
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
NET_FW_IP_VERSION = Int32
NET_FW_IP_VERSION_V4 = 0
NET_FW_IP_VERSION_V6 = 1
NET_FW_IP_VERSION_ANY = 2
NET_FW_IP_VERSION_MAX = 3
NET_FW_SCOPE = Int32
NET_FW_SCOPE_ALL = 0
NET_FW_SCOPE_LOCAL_SUBNET = 1
NET_FW_SCOPE_CUSTOM = 2
NET_FW_SCOPE_MAX = 3
NET_FW_IP_PROTOCOL = Int32
NET_FW_IP_PROTOCOL_TCP = 6
NET_FW_IP_PROTOCOL_UDP = 17
NET_FW_IP_PROTOCOL_ANY = 256
NET_FW_SERVICE_TYPE = Int32
NET_FW_SERVICE_FILE_AND_PRINT = 0
NET_FW_SERVICE_UPNP = 1
NET_FW_SERVICE_REMOTE_DESKTOP = 2
NET_FW_SERVICE_NONE = 3
NET_FW_SERVICE_TYPE_MAX = 4
NET_FW_RULE_DIRECTION = Int32
NET_FW_RULE_DIR_IN = 1
NET_FW_RULE_DIR_OUT = 2
NET_FW_RULE_DIR_MAX = 3
NET_FW_ACTION = Int32
NET_FW_ACTION_BLOCK = 0
NET_FW_ACTION_ALLOW = 1
NET_FW_ACTION_MAX = 2
NET_FW_MODIFY_STATE = Int32
NET_FW_MODIFY_STATE_OK = 0
NET_FW_MODIFY_STATE_GP_OVERRIDE = 1
NET_FW_MODIFY_STATE_INBOUND_BLOCKED = 2
NET_FW_RULE_CATEGORY = Int32
NET_FW_RULE_CATEGORY_BOOT = 0
NET_FW_RULE_CATEGORY_STEALTH = 1
NET_FW_RULE_CATEGORY_FIREWALL = 2
NET_FW_RULE_CATEGORY_CONSEC = 3
NET_FW_RULE_CATEGORY_MAX = 4
NET_FW_EDGE_TRAVERSAL_TYPE = Int32
NET_FW_EDGE_TRAVERSAL_TYPE_DENY = 0
NET_FW_EDGE_TRAVERSAL_TYPE_ALLOW = 1
NET_FW_EDGE_TRAVERSAL_TYPE_DEFER_TO_APP = 2
NET_FW_EDGE_TRAVERSAL_TYPE_DEFER_TO_USER = 3
NET_FW_AUTHENTICATE_TYPE = Int32
NET_FW_AUTHENTICATE_NONE = 0
NET_FW_AUTHENTICATE_NO_ENCAPSULATION = 1
NET_FW_AUTHENTICATE_WITH_INTEGRITY = 2
NET_FW_AUTHENTICATE_AND_NEGOTIATE_ENCRYPTION = 3
NET_FW_AUTHENTICATE_AND_ENCRYPT = 4
NETISO_FLAG = Int32
NETISO_FLAG_FORCE_COMPUTE_BINARIES = 1
NETISO_FLAG_MAX = 2
INET_FIREWALL_AC_CREATION_TYPE = Int32
INET_FIREWALL_AC_NONE = 0
INET_FIREWALL_AC_PACKAGE_ID_ONLY = 1
INET_FIREWALL_AC_BINARY = 2
INET_FIREWALL_AC_MAX = 4
INET_FIREWALL_AC_CHANGE_TYPE = Int32
INET_FIREWALL_AC_CHANGE_INVALID = 0
INET_FIREWALL_AC_CHANGE_CREATE = 1
INET_FIREWALL_AC_CHANGE_DELETE = 2
INET_FIREWALL_AC_CHANGE_MAX = 3
def _define_INET_FIREWALL_AC_CAPABILITIES_head():
    class INET_FIREWALL_AC_CAPABILITIES(Structure):
        pass
    return INET_FIREWALL_AC_CAPABILITIES
def _define_INET_FIREWALL_AC_CAPABILITIES():
    INET_FIREWALL_AC_CAPABILITIES = win32more.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_CAPABILITIES_head
    INET_FIREWALL_AC_CAPABILITIES._fields_ = [
        ("count", UInt32),
        ("capabilities", POINTER(win32more.Security.SID_AND_ATTRIBUTES_head)),
    ]
    return INET_FIREWALL_AC_CAPABILITIES
def _define_INET_FIREWALL_AC_BINARIES_head():
    class INET_FIREWALL_AC_BINARIES(Structure):
        pass
    return INET_FIREWALL_AC_BINARIES
def _define_INET_FIREWALL_AC_BINARIES():
    INET_FIREWALL_AC_BINARIES = win32more.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_BINARIES_head
    INET_FIREWALL_AC_BINARIES._fields_ = [
        ("count", UInt32),
        ("binaries", POINTER(win32more.Foundation.PWSTR)),
    ]
    return INET_FIREWALL_AC_BINARIES
def _define_INET_FIREWALL_AC_CHANGE_head():
    class INET_FIREWALL_AC_CHANGE(Structure):
        pass
    return INET_FIREWALL_AC_CHANGE
def _define_INET_FIREWALL_AC_CHANGE():
    INET_FIREWALL_AC_CHANGE = win32more.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_CHANGE_head
    class INET_FIREWALL_AC_CHANGE__Anonymous_e__Union(Union):
        pass
    INET_FIREWALL_AC_CHANGE__Anonymous_e__Union._fields_ = [
        ("capabilities", win32more.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_CAPABILITIES),
        ("binaries", win32more.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_BINARIES),
    ]
    INET_FIREWALL_AC_CHANGE._anonymous_ = [
        'Anonymous',
    ]
    INET_FIREWALL_AC_CHANGE._fields_ = [
        ("changeType", win32more.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_CHANGE_TYPE),
        ("createType", win32more.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_CREATION_TYPE),
        ("appContainerSid", POINTER(win32more.Security.SID_head)),
        ("userSid", POINTER(win32more.Security.SID_head)),
        ("displayName", win32more.Foundation.PWSTR),
        ("Anonymous", INET_FIREWALL_AC_CHANGE__Anonymous_e__Union),
    ]
    return INET_FIREWALL_AC_CHANGE
def _define_INET_FIREWALL_APP_CONTAINER_head():
    class INET_FIREWALL_APP_CONTAINER(Structure):
        pass
    return INET_FIREWALL_APP_CONTAINER
def _define_INET_FIREWALL_APP_CONTAINER():
    INET_FIREWALL_APP_CONTAINER = win32more.NetworkManagement.WindowsFirewall.INET_FIREWALL_APP_CONTAINER_head
    INET_FIREWALL_APP_CONTAINER._fields_ = [
        ("appContainerSid", POINTER(win32more.Security.SID_head)),
        ("userSid", POINTER(win32more.Security.SID_head)),
        ("appContainerName", win32more.Foundation.PWSTR),
        ("displayName", win32more.Foundation.PWSTR),
        ("description", win32more.Foundation.PWSTR),
        ("capabilities", win32more.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_CAPABILITIES),
        ("binaries", win32more.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_BINARIES),
        ("workingDirectory", win32more.Foundation.PWSTR),
        ("packageFullName", win32more.Foundation.PWSTR),
    ]
    return INET_FIREWALL_APP_CONTAINER
def _define_PAC_CHANGES_CALLBACK_FN():
    return CFUNCTYPE(Void,c_void_p,POINTER(win32more.NetworkManagement.WindowsFirewall.INET_FIREWALL_AC_CHANGE_head), use_last_error=False)
NETISO_ERROR_TYPE = Int32
NETISO_ERROR_TYPE_NONE = 0
NETISO_ERROR_TYPE_PRIVATE_NETWORK = 1
NETISO_ERROR_TYPE_INTERNET_CLIENT = 2
NETISO_ERROR_TYPE_INTERNET_CLIENT_SERVER = 3
NETISO_ERROR_TYPE_MAX = 4
def _define_PNETISO_EDP_ID_CALLBACK_FN():
    return CFUNCTYPE(Void,c_void_p,win32more.Foundation.PWSTR,UInt32, use_last_error=False)
_tag_FW_DYNAMIC_KEYWORD_ORIGIN_TYPE = Int32
FW_DYNAMIC_KEYWORD_ORIGIN_INVALID = 0
FW_DYNAMIC_KEYWORD_ORIGIN_LOCAL = 1
FW_DYNAMIC_KEYWORD_ORIGIN_MDM = 2
def _define__tag_FW_DYNAMIC_KEYWORD_ADDRESS0_head():
    class _tag_FW_DYNAMIC_KEYWORD_ADDRESS0(Structure):
        pass
    return _tag_FW_DYNAMIC_KEYWORD_ADDRESS0
def _define__tag_FW_DYNAMIC_KEYWORD_ADDRESS0():
    _tag_FW_DYNAMIC_KEYWORD_ADDRESS0 = win32more.NetworkManagement.WindowsFirewall._tag_FW_DYNAMIC_KEYWORD_ADDRESS0_head
    _tag_FW_DYNAMIC_KEYWORD_ADDRESS0._fields_ = [
        ("id", Guid),
        ("keyword", win32more.Foundation.PWSTR),
        ("flags", UInt32),
        ("addresses", win32more.Foundation.PWSTR),
    ]
    return _tag_FW_DYNAMIC_KEYWORD_ADDRESS0
def _define__tag_FW_DYNAMIC_KEYWORD_ADDRESS_DATA0_head():
    class _tag_FW_DYNAMIC_KEYWORD_ADDRESS_DATA0(Structure):
        pass
    return _tag_FW_DYNAMIC_KEYWORD_ADDRESS_DATA0
def _define__tag_FW_DYNAMIC_KEYWORD_ADDRESS_DATA0():
    _tag_FW_DYNAMIC_KEYWORD_ADDRESS_DATA0 = win32more.NetworkManagement.WindowsFirewall._tag_FW_DYNAMIC_KEYWORD_ADDRESS_DATA0_head
    _tag_FW_DYNAMIC_KEYWORD_ADDRESS_DATA0._fields_ = [
        ("dynamicKeywordAddress", win32more.NetworkManagement.WindowsFirewall._tag_FW_DYNAMIC_KEYWORD_ADDRESS0),
        ("next", POINTER(win32more.NetworkManagement.WindowsFirewall._tag_FW_DYNAMIC_KEYWORD_ADDRESS_DATA0_head)),
        ("schemaVersion", UInt16),
        ("originType", win32more.NetworkManagement.WindowsFirewall._tag_FW_DYNAMIC_KEYWORD_ORIGIN_TYPE),
    ]
    return _tag_FW_DYNAMIC_KEYWORD_ADDRESS_DATA0
_tag_FW_DYNAMIC_KEYWORD_ADDRESS_FLAGS = Int32
FW_DYNAMIC_KEYWORD_ADDRESS_FLAGS_AUTO_RESOLVE = 1
_tag_FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS = Int32
FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS_AUTO_RESOLVE = 1
FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS_NON_AUTO_RESOLVE = 2
FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS_ALL = 3
def _define_PFN_FWADDDYNAMICKEYWORDADDRESS0():
    return CFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.WindowsFirewall._tag_FW_DYNAMIC_KEYWORD_ADDRESS0_head), use_last_error=False)
def _define_PFN_FWDELETEDYNAMICKEYWORDADDRESS0():
    return CFUNCTYPE(UInt32,Guid, use_last_error=False)
def _define_PFN_FWENUMDYNAMICKEYWORDADDRESSESBYTYPE0():
    return CFUNCTYPE(UInt32,UInt32,POINTER(POINTER(win32more.NetworkManagement.WindowsFirewall._tag_FW_DYNAMIC_KEYWORD_ADDRESS_DATA0_head)), use_last_error=False)
def _define_PFN_FWENUMDYNAMICKEYWORDADDRESSBYID0():
    return CFUNCTYPE(UInt32,Guid,POINTER(POINTER(win32more.NetworkManagement.WindowsFirewall._tag_FW_DYNAMIC_KEYWORD_ADDRESS_DATA0_head)), use_last_error=False)
def _define_PFN_FWFREEDYNAMICKEYWORDADDRESSDATA0():
    return CFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.WindowsFirewall._tag_FW_DYNAMIC_KEYWORD_ADDRESS_DATA0_head), use_last_error=False)
def _define_PFN_FWUPDATEDYNAMICKEYWORDADDRESS0():
    return CFUNCTYPE(UInt32,Guid,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=False)
def _define_INetFwRemoteAdminSettings_head():
    class INetFwRemoteAdminSettings(win32more.System.Com.IDispatch_head):
        Guid = Guid('d4becddf-6f73-4a83-b832-9c66874cd20e')
    return INetFwRemoteAdminSettings
def _define_INetFwRemoteAdminSettings():
    INetFwRemoteAdminSettings = win32more.NetworkManagement.WindowsFirewall.INetFwRemoteAdminSettings_head
    INetFwRemoteAdminSettings.get_IpVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION), use_last_error=False)(7, 'get_IpVersion', ((1, 'ipVersion'),)))
    INetFwRemoteAdminSettings.put_IpVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION, use_last_error=False)(8, 'put_IpVersion', ((1, 'ipVersion'),)))
    INetFwRemoteAdminSettings.get_Scope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_SCOPE), use_last_error=False)(9, 'get_Scope', ((1, 'scope'),)))
    INetFwRemoteAdminSettings.put_Scope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_SCOPE, use_last_error=False)(10, 'put_Scope', ((1, 'scope'),)))
    INetFwRemoteAdminSettings.get_RemoteAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_RemoteAddresses', ((1, 'remoteAddrs'),)))
    INetFwRemoteAdminSettings.put_RemoteAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(12, 'put_RemoteAddresses', ((1, 'remoteAddrs'),)))
    INetFwRemoteAdminSettings.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(13, 'get_Enabled', ((1, 'enabled'),)))
    INetFwRemoteAdminSettings.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(14, 'put_Enabled', ((1, 'enabled'),)))
    return INetFwRemoteAdminSettings
def _define_INetFwIcmpSettings_head():
    class INetFwIcmpSettings(win32more.System.Com.IDispatch_head):
        Guid = Guid('a6207b2e-7cdd-426a-951e-5e1cbc5afead')
    return INetFwIcmpSettings
def _define_INetFwIcmpSettings():
    INetFwIcmpSettings = win32more.NetworkManagement.WindowsFirewall.INetFwIcmpSettings_head
    INetFwIcmpSettings.get_AllowOutboundDestinationUnreachable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(7, 'get_AllowOutboundDestinationUnreachable', ((1, 'allow'),)))
    INetFwIcmpSettings.put_AllowOutboundDestinationUnreachable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(8, 'put_AllowOutboundDestinationUnreachable', ((1, 'allow'),)))
    INetFwIcmpSettings.get_AllowRedirect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(9, 'get_AllowRedirect', ((1, 'allow'),)))
    INetFwIcmpSettings.put_AllowRedirect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(10, 'put_AllowRedirect', ((1, 'allow'),)))
    INetFwIcmpSettings.get_AllowInboundEchoRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(11, 'get_AllowInboundEchoRequest', ((1, 'allow'),)))
    INetFwIcmpSettings.put_AllowInboundEchoRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(12, 'put_AllowInboundEchoRequest', ((1, 'allow'),)))
    INetFwIcmpSettings.get_AllowOutboundTimeExceeded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(13, 'get_AllowOutboundTimeExceeded', ((1, 'allow'),)))
    INetFwIcmpSettings.put_AllowOutboundTimeExceeded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(14, 'put_AllowOutboundTimeExceeded', ((1, 'allow'),)))
    INetFwIcmpSettings.get_AllowOutboundParameterProblem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(15, 'get_AllowOutboundParameterProblem', ((1, 'allow'),)))
    INetFwIcmpSettings.put_AllowOutboundParameterProblem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(16, 'put_AllowOutboundParameterProblem', ((1, 'allow'),)))
    INetFwIcmpSettings.get_AllowOutboundSourceQuench = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(17, 'get_AllowOutboundSourceQuench', ((1, 'allow'),)))
    INetFwIcmpSettings.put_AllowOutboundSourceQuench = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(18, 'put_AllowOutboundSourceQuench', ((1, 'allow'),)))
    INetFwIcmpSettings.get_AllowInboundRouterRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(19, 'get_AllowInboundRouterRequest', ((1, 'allow'),)))
    INetFwIcmpSettings.put_AllowInboundRouterRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(20, 'put_AllowInboundRouterRequest', ((1, 'allow'),)))
    INetFwIcmpSettings.get_AllowInboundTimestampRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(21, 'get_AllowInboundTimestampRequest', ((1, 'allow'),)))
    INetFwIcmpSettings.put_AllowInboundTimestampRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(22, 'put_AllowInboundTimestampRequest', ((1, 'allow'),)))
    INetFwIcmpSettings.get_AllowInboundMaskRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(23, 'get_AllowInboundMaskRequest', ((1, 'allow'),)))
    INetFwIcmpSettings.put_AllowInboundMaskRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(24, 'put_AllowInboundMaskRequest', ((1, 'allow'),)))
    INetFwIcmpSettings.get_AllowOutboundPacketTooBig = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(25, 'get_AllowOutboundPacketTooBig', ((1, 'allow'),)))
    INetFwIcmpSettings.put_AllowOutboundPacketTooBig = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(26, 'put_AllowOutboundPacketTooBig', ((1, 'allow'),)))
    return INetFwIcmpSettings
def _define_INetFwOpenPort_head():
    class INetFwOpenPort(win32more.System.Com.IDispatch_head):
        Guid = Guid('e0483ba0-47ff-4d9c-a6d6-7741d0b195f7')
    return INetFwOpenPort
def _define_INetFwOpenPort():
    INetFwOpenPort = win32more.NetworkManagement.WindowsFirewall.INetFwOpenPort_head
    INetFwOpenPort.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Name', ((1, 'name'),)))
    INetFwOpenPort.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_Name', ((1, 'name'),)))
    INetFwOpenPort.get_IpVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION), use_last_error=False)(9, 'get_IpVersion', ((1, 'ipVersion'),)))
    INetFwOpenPort.put_IpVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION, use_last_error=False)(10, 'put_IpVersion', ((1, 'ipVersion'),)))
    INetFwOpenPort.get_Protocol = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_PROTOCOL), use_last_error=False)(11, 'get_Protocol', ((1, 'ipProtocol'),)))
    INetFwOpenPort.put_Protocol = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_PROTOCOL, use_last_error=False)(12, 'put_Protocol', ((1, 'ipProtocol'),)))
    INetFwOpenPort.get_Port = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'get_Port', ((1, 'portNumber'),)))
    INetFwOpenPort.put_Port = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(14, 'put_Port', ((1, 'portNumber'),)))
    INetFwOpenPort.get_Scope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_SCOPE), use_last_error=False)(15, 'get_Scope', ((1, 'scope'),)))
    INetFwOpenPort.put_Scope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_SCOPE, use_last_error=False)(16, 'put_Scope', ((1, 'scope'),)))
    INetFwOpenPort.get_RemoteAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'get_RemoteAddresses', ((1, 'remoteAddrs'),)))
    INetFwOpenPort.put_RemoteAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(18, 'put_RemoteAddresses', ((1, 'remoteAddrs'),)))
    INetFwOpenPort.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(19, 'get_Enabled', ((1, 'enabled'),)))
    INetFwOpenPort.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(20, 'put_Enabled', ((1, 'enabled'),)))
    INetFwOpenPort.get_BuiltIn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(21, 'get_BuiltIn', ((1, 'builtIn'),)))
    return INetFwOpenPort
def _define_INetFwOpenPorts_head():
    class INetFwOpenPorts(win32more.System.Com.IDispatch_head):
        Guid = Guid('c0e9d7fa-e07e-430a-b19a-090ce82d92e2')
    return INetFwOpenPorts
def _define_INetFwOpenPorts():
    INetFwOpenPorts = win32more.NetworkManagement.WindowsFirewall.INetFwOpenPorts_head
    INetFwOpenPorts.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'count'),)))
    INetFwOpenPorts.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.INetFwOpenPort_head, use_last_error=False)(8, 'Add', ((1, 'port'),)))
    INetFwOpenPorts.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_PROTOCOL, use_last_error=False)(9, 'Remove', ((1, 'portNumber'),(1, 'ipProtocol'),)))
    INetFwOpenPorts.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_PROTOCOL,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwOpenPort_head), use_last_error=False)(10, 'Item', ((1, 'portNumber'),(1, 'ipProtocol'),(1, 'openPort'),)))
    INetFwOpenPorts.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(11, 'get__NewEnum', ((1, 'newEnum'),)))
    return INetFwOpenPorts
def _define_INetFwService_head():
    class INetFwService(win32more.System.Com.IDispatch_head):
        Guid = Guid('79fd57c8-908e-4a36-9888-d5b3f0a444cf')
    return INetFwService
def _define_INetFwService():
    INetFwService = win32more.NetworkManagement.WindowsFirewall.INetFwService_head
    INetFwService.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Name', ((1, 'name'),)))
    INetFwService.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_SERVICE_TYPE), use_last_error=False)(8, 'get_Type', ((1, 'type'),)))
    INetFwService.get_Customized = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(9, 'get_Customized', ((1, 'customized'),)))
    INetFwService.get_IpVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION), use_last_error=False)(10, 'get_IpVersion', ((1, 'ipVersion'),)))
    INetFwService.put_IpVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION, use_last_error=False)(11, 'put_IpVersion', ((1, 'ipVersion'),)))
    INetFwService.get_Scope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_SCOPE), use_last_error=False)(12, 'get_Scope', ((1, 'scope'),)))
    INetFwService.put_Scope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_SCOPE, use_last_error=False)(13, 'put_Scope', ((1, 'scope'),)))
    INetFwService.get_RemoteAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_RemoteAddresses', ((1, 'remoteAddrs'),)))
    INetFwService.put_RemoteAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(15, 'put_RemoteAddresses', ((1, 'remoteAddrs'),)))
    INetFwService.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(16, 'get_Enabled', ((1, 'enabled'),)))
    INetFwService.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(17, 'put_Enabled', ((1, 'enabled'),)))
    INetFwService.get_GloballyOpenPorts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwOpenPorts_head), use_last_error=False)(18, 'get_GloballyOpenPorts', ((1, 'openPorts'),)))
    return INetFwService
def _define_INetFwServices_head():
    class INetFwServices(win32more.System.Com.IDispatch_head):
        Guid = Guid('79649bb4-903e-421b-94c9-79848e79f6ee')
    return INetFwServices
def _define_INetFwServices():
    INetFwServices = win32more.NetworkManagement.WindowsFirewall.INetFwServices_head
    INetFwServices.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'count'),)))
    INetFwServices.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_SERVICE_TYPE,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwService_head), use_last_error=False)(8, 'Item', ((1, 'svcType'),(1, 'service'),)))
    INetFwServices.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'newEnum'),)))
    return INetFwServices
def _define_INetFwAuthorizedApplication_head():
    class INetFwAuthorizedApplication(win32more.System.Com.IDispatch_head):
        Guid = Guid('b5e64ffa-c2c5-444e-a301-fb5e00018050')
    return INetFwAuthorizedApplication
def _define_INetFwAuthorizedApplication():
    INetFwAuthorizedApplication = win32more.NetworkManagement.WindowsFirewall.INetFwAuthorizedApplication_head
    INetFwAuthorizedApplication.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Name', ((1, 'name'),)))
    INetFwAuthorizedApplication.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_Name', ((1, 'name'),)))
    INetFwAuthorizedApplication.get_ProcessImageFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_ProcessImageFileName', ((1, 'imageFileName'),)))
    INetFwAuthorizedApplication.put_ProcessImageFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_ProcessImageFileName', ((1, 'imageFileName'),)))
    INetFwAuthorizedApplication.get_IpVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION), use_last_error=False)(11, 'get_IpVersion', ((1, 'ipVersion'),)))
    INetFwAuthorizedApplication.put_IpVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION, use_last_error=False)(12, 'put_IpVersion', ((1, 'ipVersion'),)))
    INetFwAuthorizedApplication.get_Scope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_SCOPE), use_last_error=False)(13, 'get_Scope', ((1, 'scope'),)))
    INetFwAuthorizedApplication.put_Scope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_SCOPE, use_last_error=False)(14, 'put_Scope', ((1, 'scope'),)))
    INetFwAuthorizedApplication.get_RemoteAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_RemoteAddresses', ((1, 'remoteAddrs'),)))
    INetFwAuthorizedApplication.put_RemoteAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(16, 'put_RemoteAddresses', ((1, 'remoteAddrs'),)))
    INetFwAuthorizedApplication.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(17, 'get_Enabled', ((1, 'enabled'),)))
    INetFwAuthorizedApplication.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(18, 'put_Enabled', ((1, 'enabled'),)))
    return INetFwAuthorizedApplication
def _define_INetFwAuthorizedApplications_head():
    class INetFwAuthorizedApplications(win32more.System.Com.IDispatch_head):
        Guid = Guid('644efd52-ccf9-486c-97a2-39f352570b30')
    return INetFwAuthorizedApplications
def _define_INetFwAuthorizedApplications():
    INetFwAuthorizedApplications = win32more.NetworkManagement.WindowsFirewall.INetFwAuthorizedApplications_head
    INetFwAuthorizedApplications.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'count'),)))
    INetFwAuthorizedApplications.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.INetFwAuthorizedApplication_head, use_last_error=False)(8, 'Add', ((1, 'app'),)))
    INetFwAuthorizedApplications.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(9, 'Remove', ((1, 'imageFileName'),)))
    INetFwAuthorizedApplications.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwAuthorizedApplication_head), use_last_error=False)(10, 'Item', ((1, 'imageFileName'),(1, 'app'),)))
    INetFwAuthorizedApplications.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(11, 'get__NewEnum', ((1, 'newEnum'),)))
    return INetFwAuthorizedApplications
def _define_INetFwRule_head():
    class INetFwRule(win32more.System.Com.IDispatch_head):
        Guid = Guid('af230d27-baba-4e42-aced-f524f22cfce2')
    return INetFwRule
def _define_INetFwRule():
    INetFwRule = win32more.NetworkManagement.WindowsFirewall.INetFwRule_head
    INetFwRule.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Name', ((1, 'name'),)))
    INetFwRule.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_Name', ((1, 'name'),)))
    INetFwRule.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_Description', ((1, 'desc'),)))
    INetFwRule.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_Description', ((1, 'desc'),)))
    INetFwRule.get_ApplicationName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_ApplicationName', ((1, 'imageFileName'),)))
    INetFwRule.put_ApplicationName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(12, 'put_ApplicationName', ((1, 'imageFileName'),)))
    INetFwRule.get_ServiceName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_ServiceName', ((1, 'serviceName'),)))
    INetFwRule.put_ServiceName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(14, 'put_ServiceName', ((1, 'serviceName'),)))
    INetFwRule.get_Protocol = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(15, 'get_Protocol', ((1, 'protocol'),)))
    INetFwRule.put_Protocol = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(16, 'put_Protocol', ((1, 'protocol'),)))
    INetFwRule.get_LocalPorts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'get_LocalPorts', ((1, 'portNumbers'),)))
    INetFwRule.put_LocalPorts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(18, 'put_LocalPorts', ((1, 'portNumbers'),)))
    INetFwRule.get_RemotePorts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(19, 'get_RemotePorts', ((1, 'portNumbers'),)))
    INetFwRule.put_RemotePorts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(20, 'put_RemotePorts', ((1, 'portNumbers'),)))
    INetFwRule.get_LocalAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(21, 'get_LocalAddresses', ((1, 'localAddrs'),)))
    INetFwRule.put_LocalAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(22, 'put_LocalAddresses', ((1, 'localAddrs'),)))
    INetFwRule.get_RemoteAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(23, 'get_RemoteAddresses', ((1, 'remoteAddrs'),)))
    INetFwRule.put_RemoteAddresses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(24, 'put_RemoteAddresses', ((1, 'remoteAddrs'),)))
    INetFwRule.get_IcmpTypesAndCodes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(25, 'get_IcmpTypesAndCodes', ((1, 'icmpTypesAndCodes'),)))
    INetFwRule.put_IcmpTypesAndCodes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(26, 'put_IcmpTypesAndCodes', ((1, 'icmpTypesAndCodes'),)))
    INetFwRule.get_Direction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_RULE_DIRECTION), use_last_error=False)(27, 'get_Direction', ((1, 'dir'),)))
    INetFwRule.put_Direction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_RULE_DIRECTION, use_last_error=False)(28, 'put_Direction', ((1, 'dir'),)))
    INetFwRule.get_Interfaces = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(29, 'get_Interfaces', ((1, 'interfaces'),)))
    INetFwRule.put_Interfaces = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(30, 'put_Interfaces', ((1, 'interfaces'),)))
    INetFwRule.get_InterfaceTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(31, 'get_InterfaceTypes', ((1, 'interfaceTypes'),)))
    INetFwRule.put_InterfaceTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(32, 'put_InterfaceTypes', ((1, 'interfaceTypes'),)))
    INetFwRule.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(33, 'get_Enabled', ((1, 'enabled'),)))
    INetFwRule.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(34, 'put_Enabled', ((1, 'enabled'),)))
    INetFwRule.get_Grouping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(35, 'get_Grouping', ((1, 'context'),)))
    INetFwRule.put_Grouping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(36, 'put_Grouping', ((1, 'context'),)))
    INetFwRule.get_Profiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(37, 'get_Profiles', ((1, 'profileTypesBitmask'),)))
    INetFwRule.put_Profiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(38, 'put_Profiles', ((1, 'profileTypesBitmask'),)))
    INetFwRule.get_EdgeTraversal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(39, 'get_EdgeTraversal', ((1, 'enabled'),)))
    INetFwRule.put_EdgeTraversal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(40, 'put_EdgeTraversal', ((1, 'enabled'),)))
    INetFwRule.get_Action = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_ACTION), use_last_error=False)(41, 'get_Action', ((1, 'action'),)))
    INetFwRule.put_Action = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_ACTION, use_last_error=False)(42, 'put_Action', ((1, 'action'),)))
    return INetFwRule
def _define_INetFwRule2_head():
    class INetFwRule2(win32more.NetworkManagement.WindowsFirewall.INetFwRule_head):
        Guid = Guid('9c27c8da-189b-4dde-89f7-8b39a316782c')
    return INetFwRule2
def _define_INetFwRule2():
    INetFwRule2 = win32more.NetworkManagement.WindowsFirewall.INetFwRule2_head
    INetFwRule2.get_EdgeTraversalOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(43, 'get_EdgeTraversalOptions', ((1, 'lOptions'),)))
    INetFwRule2.put_EdgeTraversalOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(44, 'put_EdgeTraversalOptions', ((1, 'lOptions'),)))
    return INetFwRule2
def _define_INetFwRule3_head():
    class INetFwRule3(win32more.NetworkManagement.WindowsFirewall.INetFwRule2_head):
        Guid = Guid('b21563ff-d696-4222-ab46-4e89b73ab34a')
    return INetFwRule3
def _define_INetFwRule3():
    INetFwRule3 = win32more.NetworkManagement.WindowsFirewall.INetFwRule3_head
    INetFwRule3.get_LocalAppPackageId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(45, 'get_LocalAppPackageId', ((1, 'wszPackageId'),)))
    INetFwRule3.put_LocalAppPackageId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(46, 'put_LocalAppPackageId', ((1, 'wszPackageId'),)))
    INetFwRule3.get_LocalUserOwner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(47, 'get_LocalUserOwner', ((1, 'wszUserOwner'),)))
    INetFwRule3.put_LocalUserOwner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(48, 'put_LocalUserOwner', ((1, 'wszUserOwner'),)))
    INetFwRule3.get_LocalUserAuthorizedList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(49, 'get_LocalUserAuthorizedList', ((1, 'wszUserAuthList'),)))
    INetFwRule3.put_LocalUserAuthorizedList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(50, 'put_LocalUserAuthorizedList', ((1, 'wszUserAuthList'),)))
    INetFwRule3.get_RemoteUserAuthorizedList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(51, 'get_RemoteUserAuthorizedList', ((1, 'wszUserAuthList'),)))
    INetFwRule3.put_RemoteUserAuthorizedList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(52, 'put_RemoteUserAuthorizedList', ((1, 'wszUserAuthList'),)))
    INetFwRule3.get_RemoteMachineAuthorizedList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(53, 'get_RemoteMachineAuthorizedList', ((1, 'wszUserAuthList'),)))
    INetFwRule3.put_RemoteMachineAuthorizedList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(54, 'put_RemoteMachineAuthorizedList', ((1, 'wszUserAuthList'),)))
    INetFwRule3.get_SecureFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(55, 'get_SecureFlags', ((1, 'lOptions'),)))
    INetFwRule3.put_SecureFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(56, 'put_SecureFlags', ((1, 'lOptions'),)))
    return INetFwRule3
def _define_INetFwRules_head():
    class INetFwRules(win32more.System.Com.IDispatch_head):
        Guid = Guid('9c4c6277-5027-441e-afae-ca1f542da009')
    return INetFwRules
def _define_INetFwRules():
    INetFwRules = win32more.NetworkManagement.WindowsFirewall.INetFwRules_head
    INetFwRules.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'count'),)))
    INetFwRules.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.INetFwRule_head, use_last_error=False)(8, 'Add', ((1, 'rule'),)))
    INetFwRules.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(9, 'Remove', ((1, 'name'),)))
    INetFwRules.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwRule_head), use_last_error=False)(10, 'Item', ((1, 'name'),(1, 'rule'),)))
    INetFwRules.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(11, 'get__NewEnum', ((1, 'newEnum'),)))
    return INetFwRules
def _define_INetFwServiceRestriction_head():
    class INetFwServiceRestriction(win32more.System.Com.IDispatch_head):
        Guid = Guid('8267bbe3-f890-491c-b7b6-2db1ef0e5d2b')
    return INetFwServiceRestriction
def _define_INetFwServiceRestriction():
    INetFwServiceRestriction = win32more.NetworkManagement.WindowsFirewall.INetFwServiceRestriction_head
    INetFwServiceRestriction.RestrictService = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int16,Int16, use_last_error=False)(7, 'RestrictService', ((1, 'serviceName'),(1, 'appName'),(1, 'restrictService'),(1, 'serviceSidRestricted'),)))
    INetFwServiceRestriction.ServiceRestricted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(Int16), use_last_error=False)(8, 'ServiceRestricted', ((1, 'serviceName'),(1, 'appName'),(1, 'serviceRestricted'),)))
    INetFwServiceRestriction.get_Rules = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwRules_head), use_last_error=False)(9, 'get_Rules', ((1, 'rules'),)))
    return INetFwServiceRestriction
def _define_INetFwProfile_head():
    class INetFwProfile(win32more.System.Com.IDispatch_head):
        Guid = Guid('174a0dda-e9f9-449d-993b-21ab667ca456')
    return INetFwProfile
def _define_INetFwProfile():
    INetFwProfile = win32more.NetworkManagement.WindowsFirewall.INetFwProfile_head
    INetFwProfile.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE), use_last_error=False)(7, 'get_Type', ((1, 'type'),)))
    INetFwProfile.get_FirewallEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(8, 'get_FirewallEnabled', ((1, 'enabled'),)))
    INetFwProfile.put_FirewallEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(9, 'put_FirewallEnabled', ((1, 'enabled'),)))
    INetFwProfile.get_ExceptionsNotAllowed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(10, 'get_ExceptionsNotAllowed', ((1, 'notAllowed'),)))
    INetFwProfile.put_ExceptionsNotAllowed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(11, 'put_ExceptionsNotAllowed', ((1, 'notAllowed'),)))
    INetFwProfile.get_NotificationsDisabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(12, 'get_NotificationsDisabled', ((1, 'disabled'),)))
    INetFwProfile.put_NotificationsDisabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(13, 'put_NotificationsDisabled', ((1, 'disabled'),)))
    INetFwProfile.get_UnicastResponsesToMulticastBroadcastDisabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(14, 'get_UnicastResponsesToMulticastBroadcastDisabled', ((1, 'disabled'),)))
    INetFwProfile.put_UnicastResponsesToMulticastBroadcastDisabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(15, 'put_UnicastResponsesToMulticastBroadcastDisabled', ((1, 'disabled'),)))
    INetFwProfile.get_RemoteAdminSettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwRemoteAdminSettings_head), use_last_error=False)(16, 'get_RemoteAdminSettings', ((1, 'remoteAdminSettings'),)))
    INetFwProfile.get_IcmpSettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwIcmpSettings_head), use_last_error=False)(17, 'get_IcmpSettings', ((1, 'icmpSettings'),)))
    INetFwProfile.get_GloballyOpenPorts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwOpenPorts_head), use_last_error=False)(18, 'get_GloballyOpenPorts', ((1, 'openPorts'),)))
    INetFwProfile.get_Services = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwServices_head), use_last_error=False)(19, 'get_Services', ((1, 'services'),)))
    INetFwProfile.get_AuthorizedApplications = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwAuthorizedApplications_head), use_last_error=False)(20, 'get_AuthorizedApplications', ((1, 'apps'),)))
    return INetFwProfile
def _define_INetFwPolicy_head():
    class INetFwPolicy(win32more.System.Com.IDispatch_head):
        Guid = Guid('d46d2478-9ac9-4008-9dc7-5563ce5536cc')
    return INetFwPolicy
def _define_INetFwPolicy():
    INetFwPolicy = win32more.NetworkManagement.WindowsFirewall.INetFwPolicy_head
    INetFwPolicy.get_CurrentProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwProfile_head), use_last_error=False)(7, 'get_CurrentProfile', ((1, 'profile'),)))
    INetFwPolicy.GetProfileByType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwProfile_head), use_last_error=False)(8, 'GetProfileByType', ((1, 'profileType'),(1, 'profile'),)))
    return INetFwPolicy
def _define_INetFwPolicy2_head():
    class INetFwPolicy2(win32more.System.Com.IDispatch_head):
        Guid = Guid('98325047-c671-4174-8d81-defcd3f03186')
    return INetFwPolicy2
def _define_INetFwPolicy2():
    INetFwPolicy2 = win32more.NetworkManagement.WindowsFirewall.INetFwPolicy2_head
    INetFwPolicy2.get_CurrentProfileTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_CurrentProfileTypes', ((1, 'profileTypesBitmask'),)))
    INetFwPolicy2.get_FirewallEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,POINTER(Int16), use_last_error=False)(8, 'get_FirewallEnabled', ((1, 'profileType'),(1, 'enabled'),)))
    INetFwPolicy2.put_FirewallEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,Int16, use_last_error=False)(9, 'put_FirewallEnabled', ((1, 'profileType'),(1, 'enabled'),)))
    INetFwPolicy2.get_ExcludedInterfaces = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(10, 'get_ExcludedInterfaces', ((1, 'profileType'),(1, 'interfaces'),)))
    INetFwPolicy2.put_ExcludedInterfaces = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,win32more.System.Com.VARIANT, use_last_error=False)(11, 'put_ExcludedInterfaces', ((1, 'profileType'),(1, 'interfaces'),)))
    INetFwPolicy2.get_BlockAllInboundTraffic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,POINTER(Int16), use_last_error=False)(12, 'get_BlockAllInboundTraffic', ((1, 'profileType'),(1, 'Block'),)))
    INetFwPolicy2.put_BlockAllInboundTraffic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,Int16, use_last_error=False)(13, 'put_BlockAllInboundTraffic', ((1, 'profileType'),(1, 'Block'),)))
    INetFwPolicy2.get_NotificationsDisabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,POINTER(Int16), use_last_error=False)(14, 'get_NotificationsDisabled', ((1, 'profileType'),(1, 'disabled'),)))
    INetFwPolicy2.put_NotificationsDisabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,Int16, use_last_error=False)(15, 'put_NotificationsDisabled', ((1, 'profileType'),(1, 'disabled'),)))
    INetFwPolicy2.get_UnicastResponsesToMulticastBroadcastDisabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,POINTER(Int16), use_last_error=False)(16, 'get_UnicastResponsesToMulticastBroadcastDisabled', ((1, 'profileType'),(1, 'disabled'),)))
    INetFwPolicy2.put_UnicastResponsesToMulticastBroadcastDisabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,Int16, use_last_error=False)(17, 'put_UnicastResponsesToMulticastBroadcastDisabled', ((1, 'profileType'),(1, 'disabled'),)))
    INetFwPolicy2.get_Rules = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwRules_head), use_last_error=False)(18, 'get_Rules', ((1, 'rules'),)))
    INetFwPolicy2.get_ServiceRestriction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwServiceRestriction_head), use_last_error=False)(19, 'get_ServiceRestriction', ((1, 'ServiceRestriction'),)))
    INetFwPolicy2.EnableRuleGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,Int16, use_last_error=False)(20, 'EnableRuleGroup', ((1, 'profileTypesBitmask'),(1, 'group'),(1, 'enable'),)))
    INetFwPolicy2.IsRuleGroupEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,POINTER(Int16), use_last_error=False)(21, 'IsRuleGroupEnabled', ((1, 'profileTypesBitmask'),(1, 'group'),(1, 'enabled'),)))
    INetFwPolicy2.RestoreLocalFirewallDefaults = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(22, 'RestoreLocalFirewallDefaults', ()))
    INetFwPolicy2.get_DefaultInboundAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_ACTION), use_last_error=False)(23, 'get_DefaultInboundAction', ((1, 'profileType'),(1, 'action'),)))
    INetFwPolicy2.put_DefaultInboundAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,win32more.NetworkManagement.WindowsFirewall.NET_FW_ACTION, use_last_error=False)(24, 'put_DefaultInboundAction', ((1, 'profileType'),(1, 'action'),)))
    INetFwPolicy2.get_DefaultOutboundAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_ACTION), use_last_error=False)(25, 'get_DefaultOutboundAction', ((1, 'profileType'),(1, 'action'),)))
    INetFwPolicy2.put_DefaultOutboundAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE2,win32more.NetworkManagement.WindowsFirewall.NET_FW_ACTION, use_last_error=False)(26, 'put_DefaultOutboundAction', ((1, 'profileType'),(1, 'action'),)))
    INetFwPolicy2.get_IsRuleGroupCurrentlyEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(Int16), use_last_error=False)(27, 'get_IsRuleGroupCurrentlyEnabled', ((1, 'group'),(1, 'enabled'),)))
    INetFwPolicy2.get_LocalPolicyModifyState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_MODIFY_STATE), use_last_error=False)(28, 'get_LocalPolicyModifyState', ((1, 'modifyState'),)))
    return INetFwPolicy2
def _define_INetFwMgr_head():
    class INetFwMgr(win32more.System.Com.IDispatch_head):
        Guid = Guid('f7898af5-cac4-4632-a2ec-da06e5111af2')
    return INetFwMgr
def _define_INetFwMgr():
    INetFwMgr = win32more.NetworkManagement.WindowsFirewall.INetFwMgr_head
    INetFwMgr.get_LocalPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwPolicy_head), use_last_error=False)(7, 'get_LocalPolicy', ((1, 'localPolicy'),)))
    INetFwMgr.get_CurrentProfileType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.NetworkManagement.WindowsFirewall.NET_FW_PROFILE_TYPE), use_last_error=False)(8, 'get_CurrentProfileType', ((1, 'profileType'),)))
    INetFwMgr.RestoreDefaults = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'RestoreDefaults', ()))
    INetFwMgr.IsPortAllowed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION,Int32,win32more.Foundation.BSTR,win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_PROTOCOL,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(10, 'IsPortAllowed', ((1, 'imageFileName'),(1, 'ipVersion'),(1, 'portNumber'),(1, 'localAddress'),(1, 'ipProtocol'),(1, 'allowed'),(1, 'restricted'),)))
    INetFwMgr.IsIcmpTypeAllowed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.NET_FW_IP_VERSION,win32more.Foundation.BSTR,Byte,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(11, 'IsIcmpTypeAllowed', ((1, 'ipVersion'),(1, 'localAddress'),(1, 'type'),(1, 'allowed'),(1, 'restricted'),)))
    return INetFwMgr
def _define_INetFwProduct_head():
    class INetFwProduct(win32more.System.Com.IDispatch_head):
        Guid = Guid('71881699-18f4-458b-b892-3ffce5e07f75')
    return INetFwProduct
def _define_INetFwProduct():
    INetFwProduct = win32more.NetworkManagement.WindowsFirewall.INetFwProduct_head
    INetFwProduct.get_RuleCategories = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_RuleCategories', ((1, 'ruleCategories'),)))
    INetFwProduct.put_RuleCategories = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(8, 'put_RuleCategories', ((1, 'ruleCategories'),)))
    INetFwProduct.get_DisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_DisplayName', ((1, 'displayName'),)))
    INetFwProduct.put_DisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_DisplayName', ((1, 'displayName'),)))
    INetFwProduct.get_PathToSignedProductExe = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_PathToSignedProductExe', ((1, 'path'),)))
    return INetFwProduct
def _define_INetFwProducts_head():
    class INetFwProducts(win32more.System.Com.IDispatch_head):
        Guid = Guid('39eb36e0-2097-40bd-8af2-63a13b525362')
    return INetFwProducts
def _define_INetFwProducts():
    INetFwProducts = win32more.NetworkManagement.WindowsFirewall.INetFwProducts_head
    INetFwProducts.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'count'),)))
    INetFwProducts.Register = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.NetworkManagement.WindowsFirewall.INetFwProduct_head,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(8, 'Register', ((1, 'product'),(1, 'registration'),)))
    INetFwProducts.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.NetworkManagement.WindowsFirewall.INetFwProduct_head), use_last_error=False)(9, 'Item', ((1, 'index'),(1, 'product'),)))
    INetFwProducts.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(10, 'get__NewEnum', ((1, 'newEnum'),)))
    return INetFwProducts
def _define_NetworkIsolationSetupAppContainerBinaries():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSID,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,POINTER(win32more.Foundation.PWSTR),UInt32, use_last_error=False)(("NetworkIsolationSetupAppContainerBinaries", windll["api-ms-win-net-isolation-l1-1-0"]), ((1, 'applicationContainerSid'),(1, 'packageFullName'),(1, 'packageFolder'),(1, 'displayName'),(1, 'bBinariesFullyComputed'),(1, 'binaries'),(1, 'binariesCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetworkIsolationRegisterForAppContainerChanges():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.NetworkManagement.WindowsFirewall.PAC_CHANGES_CALLBACK_FN,c_void_p,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("NetworkIsolationRegisterForAppContainerChanges", windll["api-ms-win-net-isolation-l1-1-0"]), ((1, 'flags'),(1, 'callback'),(1, 'context'),(1, 'registrationObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetworkIsolationUnregisterForAppContainerChanges():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE, use_last_error=False)(("NetworkIsolationUnregisterForAppContainerChanges", windll["api-ms-win-net-isolation-l1-1-0"]), ((1, 'registrationObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetworkIsolationFreeAppContainers():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.WindowsFirewall.INET_FIREWALL_APP_CONTAINER_head), use_last_error=False)(("NetworkIsolationFreeAppContainers", windll["api-ms-win-net-isolation-l1-1-0"]), ((1, 'pPublicAppCs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetworkIsolationEnumAppContainers():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(UInt32),POINTER(POINTER(win32more.NetworkManagement.WindowsFirewall.INET_FIREWALL_APP_CONTAINER_head)), use_last_error=False)(("NetworkIsolationEnumAppContainers", windll["api-ms-win-net-isolation-l1-1-0"]), ((1, 'Flags'),(1, 'pdwNumPublicAppCs'),(1, 'ppPublicAppCs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetworkIsolationGetAppContainerConfig():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),POINTER(POINTER(win32more.Security.SID_AND_ATTRIBUTES_head)), use_last_error=False)(("NetworkIsolationGetAppContainerConfig", windll["api-ms-win-net-isolation-l1-1-0"]), ((1, 'pdwNumPublicAppCs'),(1, 'appContainerSids'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetworkIsolationSetAppContainerConfig():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(win32more.Security.SID_AND_ATTRIBUTES), use_last_error=False)(("NetworkIsolationSetAppContainerConfig", windll["api-ms-win-net-isolation-l1-1-0"]), ((1, 'dwNumPublicAppCs'),(1, 'appContainerSids'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetworkIsolationDiagnoseConnectFailureAndGetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.WindowsFirewall.NETISO_ERROR_TYPE), use_last_error=False)(("NetworkIsolationDiagnoseConnectFailureAndGetInfo", windll["api-ms-win-net-isolation-l1-1-0"]), ((1, 'wszServerName'),(1, 'netIsoError'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "NETCON_MAX_NAME_LEN",
    "S_OBJECT_NO_LONGER_VALID",
    "NETISO_GEID_FOR_WDAG",
    "NETISO_GEID_FOR_NEUTRAL_AWARE",
    "UPnPNAT",
    "IUPnPNAT",
    "INATEventManager",
    "INATExternalIPAddressCallback",
    "INATNumberOfEntriesCallback",
    "IDynamicPortMappingCollection",
    "IDynamicPortMapping",
    "IStaticPortMappingCollection",
    "IStaticPortMapping",
    "NetSharingManager",
    "IEnumNetConnection",
    "NETCON_CHARACTERISTIC_FLAGS",
    "NCCF_NONE",
    "NCCF_ALL_USERS",
    "NCCF_ALLOW_DUPLICATION",
    "NCCF_ALLOW_REMOVAL",
    "NCCF_ALLOW_RENAME",
    "NCCF_INCOMING_ONLY",
    "NCCF_OUTGOING_ONLY",
    "NCCF_BRANDED",
    "NCCF_SHARED",
    "NCCF_BRIDGED",
    "NCCF_FIREWALLED",
    "NCCF_DEFAULT",
    "NCCF_HOMENET_CAPABLE",
    "NCCF_SHARED_PRIVATE",
    "NCCF_QUARANTINED",
    "NCCF_RESERVED",
    "NCCF_HOSTED_NETWORK",
    "NCCF_VIRTUAL_STATION",
    "NCCF_WIFI_DIRECT",
    "NCCF_BLUETOOTH_MASK",
    "NCCF_LAN_MASK",
    "NETCON_STATUS",
    "NCS_DISCONNECTED",
    "NCS_CONNECTING",
    "NCS_CONNECTED",
    "NCS_DISCONNECTING",
    "NCS_HARDWARE_NOT_PRESENT",
    "NCS_HARDWARE_DISABLED",
    "NCS_HARDWARE_MALFUNCTION",
    "NCS_MEDIA_DISCONNECTED",
    "NCS_AUTHENTICATING",
    "NCS_AUTHENTICATION_SUCCEEDED",
    "NCS_AUTHENTICATION_FAILED",
    "NCS_INVALID_ADDRESS",
    "NCS_CREDENTIALS_REQUIRED",
    "NCS_ACTION_REQUIRED",
    "NCS_ACTION_REQUIRED_RETRY",
    "NCS_CONNECT_FAILED",
    "NETCON_TYPE",
    "NCT_DIRECT_CONNECT",
    "NCT_INBOUND",
    "NCT_INTERNET",
    "NCT_LAN",
    "NCT_PHONE",
    "NCT_TUNNEL",
    "NCT_BRIDGE",
    "NETCON_MEDIATYPE",
    "NCM_NONE",
    "NCM_DIRECT",
    "NCM_ISDN",
    "NCM_LAN",
    "NCM_PHONE",
    "NCM_TUNNEL",
    "NCM_PPPOE",
    "NCM_BRIDGE",
    "NCM_SHAREDACCESSHOST_LAN",
    "NCM_SHAREDACCESSHOST_RAS",
    "NETCON_PROPERTIES",
    "INetConnection",
    "NETCONMGR_ENUM_FLAGS",
    "NCME_DEFAULT",
    "NCME_HIDDEN",
    "INetConnectionManager",
    "NETCONUI_CONNECT_FLAGS",
    "NCUC_DEFAULT",
    "NCUC_NO_UI",
    "NCUC_ENABLE_DISABLE",
    "INetConnectionConnectUi",
    "IEnumNetSharingPortMapping",
    "INetSharingPortMappingProps",
    "INetSharingPortMapping",
    "IEnumNetSharingEveryConnection",
    "IEnumNetSharingPublicConnection",
    "IEnumNetSharingPrivateConnection",
    "INetSharingPortMappingCollection",
    "INetConnectionProps",
    "SHARINGCONNECTIONTYPE",
    "ICSSHARINGTYPE_PUBLIC",
    "ICSSHARINGTYPE_PRIVATE",
    "SHARINGCONNECTION_ENUM_FLAGS",
    "ICSSC_DEFAULT",
    "ICSSC_ENABLED",
    "ICS_TARGETTYPE",
    "ICSTT_NAME",
    "ICSTT_IPADDRESS",
    "INetSharingConfiguration",
    "INetSharingEveryConnectionCollection",
    "INetSharingPublicConnectionCollection",
    "INetSharingPrivateConnectionCollection",
    "INetSharingManager",
    "NetFwRule",
    "NetFwOpenPort",
    "NetFwAuthorizedApplication",
    "NetFwPolicy2",
    "NetFwProduct",
    "NetFwProducts",
    "NetFwMgr",
    "NET_FW_POLICY_TYPE",
    "NET_FW_POLICY_GROUP",
    "NET_FW_POLICY_LOCAL",
    "NET_FW_POLICY_EFFECTIVE",
    "NET_FW_POLICY_TYPE_MAX",
    "NET_FW_PROFILE_TYPE",
    "NET_FW_PROFILE_DOMAIN",
    "NET_FW_PROFILE_STANDARD",
    "NET_FW_PROFILE_CURRENT",
    "NET_FW_PROFILE_TYPE_MAX",
    "NET_FW_PROFILE_TYPE2",
    "NET_FW_PROFILE2_DOMAIN",
    "NET_FW_PROFILE2_PRIVATE",
    "NET_FW_PROFILE2_PUBLIC",
    "NET_FW_PROFILE2_ALL",
    "NET_FW_IP_VERSION",
    "NET_FW_IP_VERSION_V4",
    "NET_FW_IP_VERSION_V6",
    "NET_FW_IP_VERSION_ANY",
    "NET_FW_IP_VERSION_MAX",
    "NET_FW_SCOPE",
    "NET_FW_SCOPE_ALL",
    "NET_FW_SCOPE_LOCAL_SUBNET",
    "NET_FW_SCOPE_CUSTOM",
    "NET_FW_SCOPE_MAX",
    "NET_FW_IP_PROTOCOL",
    "NET_FW_IP_PROTOCOL_TCP",
    "NET_FW_IP_PROTOCOL_UDP",
    "NET_FW_IP_PROTOCOL_ANY",
    "NET_FW_SERVICE_TYPE",
    "NET_FW_SERVICE_FILE_AND_PRINT",
    "NET_FW_SERVICE_UPNP",
    "NET_FW_SERVICE_REMOTE_DESKTOP",
    "NET_FW_SERVICE_NONE",
    "NET_FW_SERVICE_TYPE_MAX",
    "NET_FW_RULE_DIRECTION",
    "NET_FW_RULE_DIR_IN",
    "NET_FW_RULE_DIR_OUT",
    "NET_FW_RULE_DIR_MAX",
    "NET_FW_ACTION",
    "NET_FW_ACTION_BLOCK",
    "NET_FW_ACTION_ALLOW",
    "NET_FW_ACTION_MAX",
    "NET_FW_MODIFY_STATE",
    "NET_FW_MODIFY_STATE_OK",
    "NET_FW_MODIFY_STATE_GP_OVERRIDE",
    "NET_FW_MODIFY_STATE_INBOUND_BLOCKED",
    "NET_FW_RULE_CATEGORY",
    "NET_FW_RULE_CATEGORY_BOOT",
    "NET_FW_RULE_CATEGORY_STEALTH",
    "NET_FW_RULE_CATEGORY_FIREWALL",
    "NET_FW_RULE_CATEGORY_CONSEC",
    "NET_FW_RULE_CATEGORY_MAX",
    "NET_FW_EDGE_TRAVERSAL_TYPE",
    "NET_FW_EDGE_TRAVERSAL_TYPE_DENY",
    "NET_FW_EDGE_TRAVERSAL_TYPE_ALLOW",
    "NET_FW_EDGE_TRAVERSAL_TYPE_DEFER_TO_APP",
    "NET_FW_EDGE_TRAVERSAL_TYPE_DEFER_TO_USER",
    "NET_FW_AUTHENTICATE_TYPE",
    "NET_FW_AUTHENTICATE_NONE",
    "NET_FW_AUTHENTICATE_NO_ENCAPSULATION",
    "NET_FW_AUTHENTICATE_WITH_INTEGRITY",
    "NET_FW_AUTHENTICATE_AND_NEGOTIATE_ENCRYPTION",
    "NET_FW_AUTHENTICATE_AND_ENCRYPT",
    "NETISO_FLAG",
    "NETISO_FLAG_FORCE_COMPUTE_BINARIES",
    "NETISO_FLAG_MAX",
    "INET_FIREWALL_AC_CREATION_TYPE",
    "INET_FIREWALL_AC_NONE",
    "INET_FIREWALL_AC_PACKAGE_ID_ONLY",
    "INET_FIREWALL_AC_BINARY",
    "INET_FIREWALL_AC_MAX",
    "INET_FIREWALL_AC_CHANGE_TYPE",
    "INET_FIREWALL_AC_CHANGE_INVALID",
    "INET_FIREWALL_AC_CHANGE_CREATE",
    "INET_FIREWALL_AC_CHANGE_DELETE",
    "INET_FIREWALL_AC_CHANGE_MAX",
    "INET_FIREWALL_AC_CAPABILITIES",
    "INET_FIREWALL_AC_BINARIES",
    "INET_FIREWALL_AC_CHANGE",
    "INET_FIREWALL_APP_CONTAINER",
    "PAC_CHANGES_CALLBACK_FN",
    "NETISO_ERROR_TYPE",
    "NETISO_ERROR_TYPE_NONE",
    "NETISO_ERROR_TYPE_PRIVATE_NETWORK",
    "NETISO_ERROR_TYPE_INTERNET_CLIENT",
    "NETISO_ERROR_TYPE_INTERNET_CLIENT_SERVER",
    "NETISO_ERROR_TYPE_MAX",
    "PNETISO_EDP_ID_CALLBACK_FN",
    "_tag_FW_DYNAMIC_KEYWORD_ORIGIN_TYPE",
    "FW_DYNAMIC_KEYWORD_ORIGIN_INVALID",
    "FW_DYNAMIC_KEYWORD_ORIGIN_LOCAL",
    "FW_DYNAMIC_KEYWORD_ORIGIN_MDM",
    "_tag_FW_DYNAMIC_KEYWORD_ADDRESS0",
    "_tag_FW_DYNAMIC_KEYWORD_ADDRESS_DATA0",
    "_tag_FW_DYNAMIC_KEYWORD_ADDRESS_FLAGS",
    "FW_DYNAMIC_KEYWORD_ADDRESS_FLAGS_AUTO_RESOLVE",
    "_tag_FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS",
    "FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS_AUTO_RESOLVE",
    "FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS_NON_AUTO_RESOLVE",
    "FW_DYNAMIC_KEYWORD_ADDRESS_ENUM_FLAGS_ALL",
    "PFN_FWADDDYNAMICKEYWORDADDRESS0",
    "PFN_FWDELETEDYNAMICKEYWORDADDRESS0",
    "PFN_FWENUMDYNAMICKEYWORDADDRESSESBYTYPE0",
    "PFN_FWENUMDYNAMICKEYWORDADDRESSBYID0",
    "PFN_FWFREEDYNAMICKEYWORDADDRESSDATA0",
    "PFN_FWUPDATEDYNAMICKEYWORDADDRESS0",
    "INetFwRemoteAdminSettings",
    "INetFwIcmpSettings",
    "INetFwOpenPort",
    "INetFwOpenPorts",
    "INetFwService",
    "INetFwServices",
    "INetFwAuthorizedApplication",
    "INetFwAuthorizedApplications",
    "INetFwRule",
    "INetFwRule2",
    "INetFwRule3",
    "INetFwRules",
    "INetFwServiceRestriction",
    "INetFwProfile",
    "INetFwPolicy",
    "INetFwPolicy2",
    "INetFwMgr",
    "INetFwProduct",
    "INetFwProducts",
    "NetworkIsolationSetupAppContainerBinaries",
    "NetworkIsolationRegisterForAppContainerChanges",
    "NetworkIsolationUnregisterForAppContainerChanges",
    "NetworkIsolationFreeAppContainers",
    "NetworkIsolationEnumAppContainers",
    "NetworkIsolationGetAppContainerConfig",
    "NetworkIsolationSetAppContainerConfig",
    "NetworkIsolationDiagnoseConnectFailureAndGetInfo",
]
