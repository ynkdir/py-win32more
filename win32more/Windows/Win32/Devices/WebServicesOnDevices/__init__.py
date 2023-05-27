from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Devices.WebServicesOnDevices
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Networking.WinSock
import win32more.Windows.Win32.Security.Cryptography
import win32more.Windows.Win32.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
WSD_DEFAULT_HOSTING_ADDRESS: String = 'http://*:5357/'
WSD_DEFAULT_SECURE_HOSTING_ADDRESS: String = 'https://*:5358/'
WSD_DEFAULT_EVENTING_ADDRESS: String = 'http://*:5357/'
WSDAPI_OPTION_MAX_INBOUND_MESSAGE_SIZE: UInt32 = 1
WSDAPI_OPTION_TRACE_XML_TO_DEBUGGER: UInt32 = 2
WSDAPI_OPTION_TRACE_XML_TO_FILE: UInt32 = 3
WSDAPI_SSL_CERT_APPLY_DEFAULT_CHECKS: UInt32 = 0
WSDAPI_SSL_CERT_IGNORE_REVOCATION: UInt32 = 1
WSDAPI_SSL_CERT_IGNORE_EXPIRY: UInt32 = 2
WSDAPI_SSL_CERT_IGNORE_WRONG_USAGE: UInt32 = 4
WSDAPI_SSL_CERT_IGNORE_UNKNOWN_CA: UInt32 = 8
WSDAPI_SSL_CERT_IGNORE_INVALID_CN: UInt32 = 16
WSDAPI_COMPACTSIG_ACCEPT_ALL_MESSAGES: UInt32 = 1
WSD_SECURITY_HTTP_AUTH_SCHEME_NEGOTIATE: UInt32 = 1
WSD_SECURITY_HTTP_AUTH_SCHEME_NTLM: UInt32 = 2
WSDAPI_ADDRESSFAMILY_IPV4: UInt32 = 1
WSDAPI_ADDRESSFAMILY_IPV6: UInt32 = 2
@winfunctype('wsdapi.dll')
def WSDCreateUdpMessageParameters(ppTxParams: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDUdpMessageParameters_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateUdpAddress(ppAddress: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDUdpAddress_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateHttpMessageParameters(ppTxParams: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDHttpMessageParameters_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateHttpAddress(ppAddress: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDHttpAddress_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateOutboundAttachment(ppAttachment: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDOutboundAttachment_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDXMLGetNameFromBuiltinNamespace(pszNamespace: win32more.Windows.Win32.Foundation.PWSTR, pszName: win32more.Windows.Win32.Foundation.PWSTR, ppName: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDXMLCreateContext(ppContext: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDiscoveryProvider(pContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, ppProvider: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryProvider_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDiscoveryProvider2(pContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, pConfigParams: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_head), dwConfigParamCount: UInt32, ppProvider: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryProvider_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDiscoveryPublisher(pContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, ppPublisher: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryPublisher_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDiscoveryPublisher2(pContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, pConfigParams: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_head), dwConfigParamCount: UInt32, ppPublisher: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryPublisher_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDeviceProxy(pszDeviceId: win32more.Windows.Win32.Foundation.PWSTR, pszLocalId: win32more.Windows.Win32.Foundation.PWSTR, pContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, ppDeviceProxy: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceProxy_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDeviceProxyAdvanced(pszDeviceId: win32more.Windows.Win32.Foundation.PWSTR, pDeviceAddress: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress_head, pszLocalId: win32more.Windows.Win32.Foundation.PWSTR, pContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, ppDeviceProxy: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceProxy_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDeviceProxy2(pszDeviceId: win32more.Windows.Win32.Foundation.PWSTR, pszLocalId: win32more.Windows.Win32.Foundation.PWSTR, pContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, pConfigParams: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_head), dwConfigParamCount: UInt32, ppDeviceProxy: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceProxy_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDeviceHost(pszLocalId: win32more.Windows.Win32.Foundation.PWSTR, pContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, ppDeviceHost: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceHost_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDeviceHostAdvanced(pszLocalId: win32more.Windows.Win32.Foundation.PWSTR, pContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, ppHostAddresses: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress_head), dwHostAddressCount: UInt32, ppDeviceHost: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceHost_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDeviceHost2(pszLocalId: win32more.Windows.Win32.Foundation.PWSTR, pContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, pConfigParams: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_head), dwConfigParamCount: UInt32, ppDeviceHost: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceHost_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDSetConfigurationOption(dwOption: UInt32, pVoid: VoidPtr, cbInBuffer: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDGetConfigurationOption(dwOption: UInt32, pVoid: VoidPtr, cbOutBuffer: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDAllocateLinkedMemory(pParent: VoidPtr, cbSize: UIntPtr) -> VoidPtr: ...
@winfunctype('wsdapi.dll')
def WSDFreeLinkedMemory(pVoid: VoidPtr) -> Void: ...
@winfunctype('wsdapi.dll')
def WSDAttachLinkedMemory(pParent: VoidPtr, pChild: VoidPtr) -> Void: ...
@winfunctype('wsdapi.dll')
def WSDDetachLinkedMemory(pVoid: VoidPtr) -> Void: ...
@winfunctype('wsdapi.dll')
def WSDXMLBuildAnyForSingleElement(pElementName: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head), pszText: win32more.Windows.Win32.Foundation.PWSTR, ppAny: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDXMLGetValueFromAny(pszNamespace: win32more.Windows.Win32.Foundation.PWSTR, pszName: win32more.Windows.Win32.Foundation.PWSTR, pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), ppszValue: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDXMLAddSibling(pFirst: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pSecond: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDXMLAddChild(pParent: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pChild: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDXMLCleanupElement(pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDGenerateFault(pszCode: win32more.Windows.Win32.Foundation.PWSTR, pszSubCode: win32more.Windows.Win32.Foundation.PWSTR, pszReason: win32more.Windows.Win32.Foundation.PWSTR, pszDetail: win32more.Windows.Win32.Foundation.PWSTR, pContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, ppFault: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDGenerateFaultEx(pCode: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head), pSubCode: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head), pReasons: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST_head), pszDetail: win32more.Windows.Win32.Foundation.PWSTR, ppFault: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDUriEncode(source: win32more.Windows.Win32.Foundation.PWSTR, cchSource: UInt32, destOut: POINTER(win32more.Windows.Win32.Foundation.PWSTR), cchDestOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDUriDecode(source: win32more.Windows.Win32.Foundation.PWSTR, cchSource: UInt32, destOut: POINTER(win32more.Windows.Win32.Foundation.PWSTR), cchDestOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
DeviceDiscoveryMechanism = Int32
DeviceDiscoveryMechanism_MulticastDiscovery: DeviceDiscoveryMechanism = 0
DeviceDiscoveryMechanism_DirectedDiscovery: DeviceDiscoveryMechanism = 1
DeviceDiscoveryMechanism_SecureDirectedDiscovery: DeviceDiscoveryMechanism = 2
class IWSDAddress(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b9574c6c-12a6-4f74-93a1-3318ff605759}')
    @commethod(3)
    def Serialize(self, pszBuffer: win32more.Windows.Win32.Foundation.PWSTR, cchLength: UInt32, fSafe: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Deserialize(self, pszBuffer: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDAsyncCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a63e109d-ce72-49e2-ba98-e845f5ee1666}')
    @commethod(3)
    def AsyncOperationComplete(self, pAsyncResult: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head, pAsyncState: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDAsyncResult(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{11a9852a-8dd8-423e-b537-9356db4fbfb8}')
    @commethod(3)
    def SetCallback(self, pCallback: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncCallback_head, pAsyncState: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetWaitHandle(self, hWaitHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def HasCompleted(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAsyncState(self, ppAsyncState: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Abort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetEvent(self, pEvent: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetEndpointProxy(self, ppEndpoint: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDEndpointProxy_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDAttachment(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5d55a616-9df8-4b09-b156-9ba351a48b76}')
class IWSDDeviceHost(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{917fe891-3d13-4138-9809-934c8abeb12c}')
    @commethod(3)
    def Init(self, pszLocalId: win32more.Windows.Win32.Foundation.PWSTR, pContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, ppHostAddresses: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress_head), dwHostAddressCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Start(self, ullInstanceId: UInt64, pScopeList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pNotificationSink: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceHostNotify_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Stop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Terminate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RegisterPortType(self, pPortType: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_PORT_TYPE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetMetadata(self, pThisModelMetadata: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_THIS_MODEL_METADATA_head), pThisDeviceMetadata: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_THIS_DEVICE_METADATA_head), pHostMetadata: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_HOST_METADATA_head), pCustomMetadata: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RegisterService(self, pszServiceId: win32more.Windows.Win32.Foundation.PWSTR, pService: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RetireService(self, pszServiceId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AddDynamicService(self, pszServiceId: win32more.Windows.Win32.Foundation.PWSTR, pszEndpointAddress: win32more.Windows.Win32.Foundation.PWSTR, pPortType: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_PORT_TYPE_head), pPortName: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head), pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pService: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RemoveDynamicService(self, pszServiceId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetServiceDiscoverable(self, pszServiceId: win32more.Windows.Win32.Foundation.PWSTR, fDiscoverable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SignalEvent(self, pszServiceId: win32more.Windows.Win32.Foundation.PWSTR, pBody: VoidPtr, pOperation: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDDeviceHostNotify(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b5bee9f9-eeda-41fe-96f7-f45e14990fb0}')
    @commethod(3)
    def GetService(self, pszServiceId: win32more.Windows.Win32.Foundation.PWSTR, ppService: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDDeviceProxy(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{eee0c031-c578-4c0e-9a3b-973c35f409db}')
    @commethod(3)
    def Init(self, pszDeviceId: win32more.Windows.Win32.Foundation.PWSTR, pDeviceAddress: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress_head, pszLocalId: win32more.Windows.Win32.Foundation.PWSTR, pContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, pSponsor: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceProxy_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginGetMetadata(self, ppResult: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EndGetMetadata(self, pResult: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetHostMetadata(self, ppHostMetadata: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_HOST_METADATA_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetThisModelMetadata(self, ppManufacturerMetadata: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_THIS_MODEL_METADATA_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetThisDeviceMetadata(self, ppThisDeviceMetadata: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_THIS_DEVICE_METADATA_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAllMetadata(self, ppMetadata: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetServiceProxyById(self, pszServiceId: win32more.Windows.Win32.Foundation.PWSTR, ppServiceProxy: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDServiceProxy_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetServiceProxyByType(self, pType: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head), ppServiceProxy: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDServiceProxy_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetEndpointProxy(self, ppProxy: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDEndpointProxy_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDEndpointProxy(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1860d430-b24c-4975-9f90-dbb39baa24ec}')
    @commethod(3)
    def SendOneWayRequest(self, pBody: VoidPtr, pOperation: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SendTwoWayRequest(self, pBody: VoidPtr, pOperation: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), pResponseContext: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SYNCHRONOUS_RESPONSE_CONTEXT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SendTwoWayRequestAsync(self, pBody: VoidPtr, pOperation: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), pAsyncState: win32more.Windows.Win32.System.Com.IUnknown_head, pCallback: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncCallback_head, pResult: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AbortAsyncOperation(self, pAsyncResult: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ProcessFault(self, pFault: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetErrorInfo(self, ppszErrorInfo: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFaultInfo(self, ppFault: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDEventingStatus(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{49b17f52-637a-407a-ae99-fbe82a4d38c0}')
    @commethod(3)
    def SubscriptionRenewed(self, pszSubscriptionAction: win32more.Windows.Win32.Foundation.PWSTR) -> Void: ...
    @commethod(4)
    def SubscriptionRenewalFailed(self, pszSubscriptionAction: win32more.Windows.Win32.Foundation.PWSTR, hr: win32more.Windows.Win32.Foundation.HRESULT) -> Void: ...
    @commethod(5)
    def SubscriptionEnded(self, pszSubscriptionAction: win32more.Windows.Win32.Foundation.PWSTR) -> Void: ...
class IWSDHttpAddress(ComPtr):
    extends: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDTransportAddress
    _iid_ = Guid('{d09ac7bd-2a3e-4b85-8605-2737ff3e4ea0}')
    @commethod(10)
    def GetSecure(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetSecure(self, fSecure: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetPath(self, ppszPath: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetPath(self, pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDHttpAuthParameters(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0b476df0-8dac-480d-b05c-99781a5884aa}')
    @commethod(3)
    def GetClientAccessToken(self, phToken: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAuthType(self, pAuthType: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDHttpMessageParameters(ComPtr):
    extends: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters
    _iid_ = Guid('{540bd122-5c83-4dec-b396-ea62a2697fdf}')
    @commethod(8)
    def SetInboundHttpHeaders(self, pszHeaders: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetInboundHttpHeaders(self, ppszHeaders: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetOutboundHttpHeaders(self, pszHeaders: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetOutboundHttpHeaders(self, ppszHeaders: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetID(self, pszId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetID(self, ppszId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetContext(self, pContext: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetContext(self, ppContext: POINTER(win32more.Windows.Win32.System.Com.IUnknown_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Clear(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDInboundAttachment(ComPtr):
    extends: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAttachment
    _iid_ = Guid('{5bd6ca65-233c-4fb8-9f7a-2641619655c9}')
    @commethod(3)
    def Read(self, pBuffer: POINTER(Byte), dwBytesToRead: UInt32, pdwNumberOfBytesRead: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDMessageParameters(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1fafe8a2-e6fc-4b80-b6cf-b7d45c416d7c}')
    @commethod(3)
    def GetLocalAddress(self, ppAddress: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetLocalAddress(self, pAddress: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRemoteAddress(self, ppAddress: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetRemoteAddress(self, pAddress: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetLowerParameters(self, ppTxParams: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDMetadataExchange(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{06996d57-1d67-4928-9307-3d7833fdb846}')
    @commethod(3)
    def GetMetadata(self, MetadataOut: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDOutboundAttachment(ComPtr):
    extends: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAttachment
    _iid_ = Guid('{aa302f8d-5a22-4ba5-b392-aa8486f4c15d}')
    @commethod(3)
    def Write(self, pBuffer: POINTER(Byte), dwBytesToWrite: UInt32, pdwNumberOfBytesWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Abort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDSSLClientCertificate(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{de105e87-a0da-418e-98ad-27b9eed87bdc}')
    @commethod(3)
    def GetClientCertificate(self, ppCertContext: POINTER(POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMappedAccessToken(self, phToken: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDScopeMatchingRule(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fcafe424-fef5-481a-bd9f-33ce0574256f}')
    @commethod(3)
    def GetScopeRule(self, ppszScopeMatchingRule: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MatchScopes(self, pszScope1: win32more.Windows.Win32.Foundation.PWSTR, pszScope2: win32more.Windows.Win32.Foundation.PWSTR, pfMatch: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDServiceMessaging(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{94974cf4-0cab-460d-a3f6-7a0ad623c0e6}')
    @commethod(3)
    def SendResponse(self, pBody: VoidPtr, pOperation: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), pMessageParameters: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FaultRequest(self, pRequestHeader: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_HEADER_head), pMessageParameters: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head, pFault: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDServiceProxy(ComPtr):
    extends: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDMetadataExchange
    _iid_ = Guid('{d4c7fb9c-03ab-4175-9d67-094fafebf487}')
    @commethod(4)
    def BeginGetMetadata(self, ppResult: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EndGetMetadata(self, pResult: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head, ppMetadata: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetServiceMetadata(self, ppServiceMetadata: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SERVICE_METADATA_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SubscribeToOperation(self, pOperation: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), pUnknown: win32more.Windows.Win32.System.Com.IUnknown_head, pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), ppAny: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UnsubscribeToOperation(self, pOperation: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetEventingStatusCallback(self, pStatus: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDEventingStatus_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetEndpointProxy(self, ppProxy: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDEndpointProxy_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDServiceProxyEventing(ComPtr):
    extends: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDServiceProxy
    _iid_ = Guid('{f9279d6d-1012-4a94-b8cc-fd35d2202bfe}')
    @commethod(11)
    def SubscribeToMultipleOperations(self, pOperations: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pUnknown: win32more.Windows.Win32.System.Com.IUnknown_head, pExpires: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head), pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), ppExpires: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)), ppAny: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def BeginSubscribeToMultipleOperations(self, pOperations: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pUnknown: win32more.Windows.Win32.System.Com.IUnknown_head, pExpires: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head), pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pAsyncState: win32more.Windows.Win32.System.Com.IUnknown_head, pAsyncCallback: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncCallback_head, ppResult: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def EndSubscribeToMultipleOperations(self, pOperations: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pResult: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head, ppExpires: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)), ppAny: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def UnsubscribeToMultipleOperations(self, pOperations: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def BeginUnsubscribeToMultipleOperations(self, pOperations: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pAsyncState: win32more.Windows.Win32.System.Com.IUnknown_head, pAsyncCallback: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncCallback_head, ppResult: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def EndUnsubscribeToMultipleOperations(self, pOperations: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pResult: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def RenewMultipleOperations(self, pOperations: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pExpires: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head), pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), ppExpires: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)), ppAny: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def BeginRenewMultipleOperations(self, pOperations: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pExpires: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head), pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pAsyncState: win32more.Windows.Win32.System.Com.IUnknown_head, pAsyncCallback: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncCallback_head, ppResult: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def EndRenewMultipleOperations(self, pOperations: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pResult: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head, ppExpires: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)), ppAny: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetStatusForMultipleOperations(self, pOperations: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), ppExpires: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)), ppAny: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def BeginGetStatusForMultipleOperations(self, pOperations: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pAsyncState: win32more.Windows.Win32.System.Com.IUnknown_head, pAsyncCallback: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncCallback_head, ppResult: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def EndGetStatusForMultipleOperations(self, pOperations: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pResult: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head, ppExpires: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)), ppAny: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDSignatureProperty(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{03ce20aa-71c4-45e2-b32e-3766c61c790f}')
    @commethod(3)
    def IsMessageSigned(self, pbSigned: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsMessageSignatureTrusted(self, pbSignatureTrusted: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetKeyInfo(self, pbKeyInfo: POINTER(Byte), pdwKeyInfoSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSignature(self, pbSignature: POINTER(Byte), pdwSignatureSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSignedInfoHash(self, pbSignedInfoHash: POINTER(Byte), pdwHashSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDTransportAddress(ComPtr):
    extends: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress
    _iid_ = Guid('{70d23498-4ee6-4340-a3df-d845d2235467}')
    @commethod(5)
    def GetPort(self, pwPort: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetPort(self, wPort: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTransportAddress(self, ppszAddress: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTransportAddressEx(self, fSafe: win32more.Windows.Win32.Foundation.BOOL, ppszAddress: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetTransportAddress(self, pszAddress: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDUdpAddress(ComPtr):
    extends: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDTransportAddress
    _iid_ = Guid('{74d6124a-a441-4f78-a1eb-97a8d1996893}')
    @commethod(10)
    def SetSockaddr(self, pSockAddr: POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKADDR_STORAGE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetSockaddr(self, pSockAddr: POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKADDR_STORAGE_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetExclusive(self, fExclusive: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetExclusive(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetMessageType(self, messageType: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDUdpMessageType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetMessageType(self, pMessageType: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDUdpMessageType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetTTL(self, dwTTL: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetTTL(self, pdwTTL: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetAlias(self, pAlias: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetAlias(self, pAlias: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDUdpMessageParameters(ComPtr):
    extends: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters
    _iid_ = Guid('{9934149f-8f0c-447b-aa0b-73124b0ca7f0}')
    @commethod(8)
    def SetRetransmitParams(self, pParams: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDUdpRetransmitParams_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRetransmitParams(self, pParams: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDUdpRetransmitParams_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDXMLContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{75d8f3ee-3e5a-43b4-a15a-bcf6887460c0}')
    @commethod(3)
    def AddNamespace(self, pszUri: win32more.Windows.Win32.Foundation.PWSTR, pszSuggestedPrefix: win32more.Windows.Win32.Foundation.PWSTR, ppNamespace: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAMESPACE_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddNameToNamespace(self, pszUri: win32more.Windows.Win32.Foundation.PWSTR, pszName: win32more.Windows.Win32.Foundation.PWSTR, ppName: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetNamespaces(self, pNamespaces: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAMESPACE_head)), wNamespacesCount: UInt16, bLayerNumber: Byte) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetTypes(self, pTypes: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_TYPE_head)), dwTypesCount: UInt32, bLayerNumber: Byte) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDiscoveredService(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4bad8a3b-b374-4420-9632-aac945b374aa}')
    @commethod(3)
    def GetEndpointReference(self, ppEndpointReference: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTypes(self, ppTypesList: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetScopes(self, ppScopesList: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetXAddrs(self, ppXAddrsList: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetMetadataVersion(self, pullMetadataVersion: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetExtendedDiscoXML(self, ppHeaderAny: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)), ppBodyAny: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetProbeResolveTag(self, ppszTag: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRemoteTransportAddress(self, ppszRemoteTransportAddress: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetLocalTransportAddress(self, ppszLocalTransportAddress: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetLocalInterfaceGUID(self, pGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetInstanceId(self, pullInstanceId: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDiscoveryProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8ffc8e55-f0eb-480f-88b7-b435dd281d45}')
    @commethod(3)
    def SetAddressFamily(self, dwAddressFamily: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Attach(self, pSink: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryProviderNotify_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Detach(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SearchById(self, pszId: win32more.Windows.Win32.Foundation.PWSTR, pszTag: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SearchByAddress(self, pszAddress: win32more.Windows.Win32.Foundation.PWSTR, pszTag: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SearchByType(self, pTypesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head), pScopesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pszMatchBy: win32more.Windows.Win32.Foundation.PWSTR, pszTag: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetXMLContext(self, ppContext: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDiscoveryProviderNotify(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{73ee3ced-b6e6-4329-a546-3e8ad46563d2}')
    @commethod(3)
    def Add(self, pService: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveredService_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Remove(self, pService: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveredService_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SearchFailed(self, hr: win32more.Windows.Win32.Foundation.HRESULT, pszTag: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SearchComplete(self, pszTag: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDiscoveryPublisher(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ae01e1a8-3ff9-4148-8116-057cc616fe13}')
    @commethod(3)
    def SetAddressFamily(self, dwAddressFamily: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RegisterNotificationSink(self, pSink: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryPublisherNotify_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def UnRegisterNotificationSink(self, pSink: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryPublisherNotify_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Publish(self, pszId: win32more.Windows.Win32.Foundation.PWSTR, ullMetadataVersion: UInt64, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: win32more.Windows.Win32.Foundation.PWSTR, pTypesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head), pScopesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pXAddrsList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UnPublish(self, pszId: win32more.Windows.Win32.Foundation.PWSTR, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: win32more.Windows.Win32.Foundation.PWSTR, pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def MatchProbe(self, pProbeMessage: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head), pMessageParameters: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head, pszId: win32more.Windows.Win32.Foundation.PWSTR, ullMetadataVersion: UInt64, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: win32more.Windows.Win32.Foundation.PWSTR, pTypesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head), pScopesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pXAddrsList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def MatchResolve(self, pResolveMessage: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head), pMessageParameters: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head, pszId: win32more.Windows.Win32.Foundation.PWSTR, ullMetadataVersion: UInt64, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: win32more.Windows.Win32.Foundation.PWSTR, pTypesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head), pScopesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pXAddrsList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def PublishEx(self, pszId: win32more.Windows.Win32.Foundation.PWSTR, ullMetadataVersion: UInt64, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: win32more.Windows.Win32.Foundation.PWSTR, pTypesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head), pScopesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pXAddrsList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pHeaderAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pReferenceParameterAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pPolicyAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pEndpointReferenceAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def MatchProbeEx(self, pProbeMessage: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head), pMessageParameters: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head, pszId: win32more.Windows.Win32.Foundation.PWSTR, ullMetadataVersion: UInt64, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: win32more.Windows.Win32.Foundation.PWSTR, pTypesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head), pScopesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pXAddrsList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pHeaderAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pReferenceParameterAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pPolicyAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pEndpointReferenceAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def MatchResolveEx(self, pResolveMessage: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head), pMessageParameters: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head, pszId: win32more.Windows.Win32.Foundation.PWSTR, ullMetadataVersion: UInt64, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: win32more.Windows.Win32.Foundation.PWSTR, pTypesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head), pScopesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pXAddrsList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pHeaderAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pReferenceParameterAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pPolicyAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pEndpointReferenceAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def RegisterScopeMatchingRule(self, pScopeMatchingRule: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDScopeMatchingRule_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def UnRegisterScopeMatchingRule(self, pScopeMatchingRule: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDScopeMatchingRule_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetXMLContext(self, ppContext: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDiscoveryPublisherNotify(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e67651b0-337a-4b3c-9758-733388568251}')
    @commethod(3)
    def ProbeHandler(self, pSoap: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head), pMessageParameters: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ResolveHandler(self, pSoap: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head), pMessageParameters: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PWSD_SOAP_MESSAGE_HANDLER(thisUnknown: win32more.Windows.Win32.System.Com.IUnknown_head, event: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class REQUESTBODY_GetStatus(EasyCastStructure):
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class REQUESTBODY_Renew(EasyCastStructure):
    Expires: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class REQUESTBODY_Subscribe(EasyCastStructure):
    EndTo: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    Delivery: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_DELIVERY_MODE_head)
    Expires: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)
    Filter: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_FILTER_head)
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class REQUESTBODY_Unsubscribe(EasyCastStructure):
    any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class RESPONSEBODY_GetMetadata(EasyCastStructure):
    Metadata: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST_head)
class RESPONSEBODY_GetStatus(EasyCastStructure):
    expires: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)
    any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class RESPONSEBODY_Renew(EasyCastStructure):
    expires: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)
    any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class RESPONSEBODY_Subscribe(EasyCastStructure):
    SubscriptionManager: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    expires: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)
    any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class RESPONSEBODY_SubscriptionEnd(EasyCastStructure):
    SubscriptionManager: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    Status: win32more.Windows.Win32.Foundation.PWSTR
    Reason: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_head)
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
WSDEventType = Int32
WSDET_NONE: WSDEventType = 0
WSDET_INCOMING_MESSAGE: WSDEventType = 1
WSDET_INCOMING_FAULT: WSDEventType = 2
WSDET_TRANSMISSION_FAILURE: WSDEventType = 3
WSDET_RESPONSE_TIMEOUT: WSDEventType = 4
WSDUdpMessageType = Int32
ONE_WAY: WSDUdpMessageType = 0
TWO_WAY: WSDUdpMessageType = 1
class WSDUdpRetransmitParams(EasyCastStructure):
    ulSendDelay: UInt32
    ulRepeat: UInt32
    ulRepeatMinDelay: UInt32
    ulRepeatMaxDelay: UInt32
    ulRepeatUpperDelay: UInt32
class WSDXML_ATTRIBUTE(EasyCastStructure):
    Element: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
    Next: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ATTRIBUTE_head)
    Name: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head)
    Value: win32more.Windows.Win32.Foundation.PWSTR
class WSDXML_ELEMENT(EasyCastStructure):
    Node: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NODE
    Name: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head)
    FirstAttribute: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ATTRIBUTE_head)
    FirstChild: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NODE_head)
    PrefixMappings: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_PREFIX_MAPPING_head)
class WSDXML_ELEMENT_LIST(EasyCastStructure):
    Next: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_LIST_head)
    Element: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSDXML_NAME(EasyCastStructure):
    Space: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAMESPACE_head)
    LocalName: win32more.Windows.Win32.Foundation.PWSTR
class WSDXML_NAMESPACE(EasyCastStructure):
    Uri: win32more.Windows.Win32.Foundation.PWSTR
    PreferredPrefix: win32more.Windows.Win32.Foundation.PWSTR
    Names: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head)
    NamesCount: UInt16
    Encoding: UInt16
class WSDXML_NODE(EasyCastStructure):
    ElementType = 0
    TextType = 1
    Type: Int32
    Parent: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
    Next: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NODE_head)
WSDXML_OP = Int32
WSDXML_OP_OpNone: WSDXML_OP = 0
WSDXML_OP_OpEndOfTable: WSDXML_OP = 1
WSDXML_OP_OpBeginElement_: WSDXML_OP = 2
WSDXML_OP_OpBeginAnyElement: WSDXML_OP = 3
WSDXML_OP_OpEndElement: WSDXML_OP = 4
WSDXML_OP_OpElement_: WSDXML_OP = 5
WSDXML_OP_OpAnyElement: WSDXML_OP = 6
WSDXML_OP_OpAnyElements: WSDXML_OP = 7
WSDXML_OP_OpAnyText: WSDXML_OP = 8
WSDXML_OP_OpAttribute_: WSDXML_OP = 9
WSDXML_OP_OpBeginChoice: WSDXML_OP = 10
WSDXML_OP_OpEndChoice: WSDXML_OP = 11
WSDXML_OP_OpBeginSequence: WSDXML_OP = 12
WSDXML_OP_OpEndSequence: WSDXML_OP = 13
WSDXML_OP_OpBeginAll: WSDXML_OP = 14
WSDXML_OP_OpEndAll: WSDXML_OP = 15
WSDXML_OP_OpAnything: WSDXML_OP = 16
WSDXML_OP_OpAnyNumber: WSDXML_OP = 17
WSDXML_OP_OpOneOrMore: WSDXML_OP = 18
WSDXML_OP_OpOptional: WSDXML_OP = 19
WSDXML_OP_OpFormatBool_: WSDXML_OP = 20
WSDXML_OP_OpFormatInt8_: WSDXML_OP = 21
WSDXML_OP_OpFormatInt16_: WSDXML_OP = 22
WSDXML_OP_OpFormatInt32_: WSDXML_OP = 23
WSDXML_OP_OpFormatInt64_: WSDXML_OP = 24
WSDXML_OP_OpFormatUInt8_: WSDXML_OP = 25
WSDXML_OP_OpFormatUInt16_: WSDXML_OP = 26
WSDXML_OP_OpFormatUInt32_: WSDXML_OP = 27
WSDXML_OP_OpFormatUInt64_: WSDXML_OP = 28
WSDXML_OP_OpFormatUnicodeString_: WSDXML_OP = 29
WSDXML_OP_OpFormatDom_: WSDXML_OP = 30
WSDXML_OP_OpFormatStruct_: WSDXML_OP = 31
WSDXML_OP_OpFormatUri_: WSDXML_OP = 32
WSDXML_OP_OpFormatUuidUri_: WSDXML_OP = 33
WSDXML_OP_OpFormatName_: WSDXML_OP = 34
WSDXML_OP_OpFormatListInsertTail_: WSDXML_OP = 35
WSDXML_OP_OpFormatType_: WSDXML_OP = 36
WSDXML_OP_OpFormatDynamicType_: WSDXML_OP = 37
WSDXML_OP_OpFormatLookupType_: WSDXML_OP = 38
WSDXML_OP_OpFormatDuration_: WSDXML_OP = 39
WSDXML_OP_OpFormatDateTime_: WSDXML_OP = 40
WSDXML_OP_OpFormatFloat_: WSDXML_OP = 41
WSDXML_OP_OpFormatDouble_: WSDXML_OP = 42
WSDXML_OP_OpProcess_: WSDXML_OP = 43
WSDXML_OP_OpQualifiedAttribute_: WSDXML_OP = 44
WSDXML_OP_OpFormatXMLDeclaration_: WSDXML_OP = 45
WSDXML_OP_OpFormatMax: WSDXML_OP = 46
class WSDXML_PREFIX_MAPPING(EasyCastStructure):
    Refs: UInt32
    Next: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_PREFIX_MAPPING_head)
    Space: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAMESPACE_head)
    Prefix: win32more.Windows.Win32.Foundation.PWSTR
class WSDXML_TEXT(EasyCastStructure):
    Node: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NODE
    Text: win32more.Windows.Win32.Foundation.PWSTR
class WSDXML_TYPE(EasyCastStructure):
    Uri: win32more.Windows.Win32.Foundation.PWSTR
    Table: POINTER(Byte)
class WSD_APP_SEQUENCE(EasyCastStructure):
    InstanceId: UInt64
    SequenceId: win32more.Windows.Win32.Foundation.PWSTR
    MessageNumber: UInt64
class WSD_BYE(EasyCastStructure):
    EndpointReference: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_CONFIG_ADDRESSES(EasyCastStructure):
    addresses: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress_head)
    dwAddressCount: UInt32
class WSD_CONFIG_PARAM(EasyCastStructure):
    configParamType: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_TYPE
    pConfigData: VoidPtr
    dwConfigDataSize: UInt32
WSD_CONFIG_PARAM_TYPE = Int32
WSD_CONFIG_MAX_INBOUND_MESSAGE_SIZE: WSD_CONFIG_PARAM_TYPE = 1
WSD_CONFIG_MAX_OUTBOUND_MESSAGE_SIZE: WSD_CONFIG_PARAM_TYPE = 2
WSD_SECURITY_SSL_CERT_FOR_CLIENT_AUTH: WSD_CONFIG_PARAM_TYPE = 3
WSD_SECURITY_SSL_SERVER_CERT_VALIDATION: WSD_CONFIG_PARAM_TYPE = 4
WSD_SECURITY_SSL_CLIENT_CERT_VALIDATION: WSD_CONFIG_PARAM_TYPE = 5
WSD_SECURITY_SSL_NEGOTIATE_CLIENT_CERT: WSD_CONFIG_PARAM_TYPE = 6
WSD_SECURITY_COMPACTSIG_SIGNING_CERT: WSD_CONFIG_PARAM_TYPE = 7
WSD_SECURITY_COMPACTSIG_VALIDATION: WSD_CONFIG_PARAM_TYPE = 8
WSD_CONFIG_HOSTING_ADDRESSES: WSD_CONFIG_PARAM_TYPE = 9
WSD_CONFIG_DEVICE_ADDRESSES: WSD_CONFIG_PARAM_TYPE = 10
WSD_SECURITY_REQUIRE_HTTP_CLIENT_AUTH: WSD_CONFIG_PARAM_TYPE = 11
WSD_SECURITY_REQUIRE_CLIENT_CERT_OR_HTTP_CLIENT_AUTH: WSD_CONFIG_PARAM_TYPE = 12
WSD_SECURITY_USE_HTTP_CLIENT_AUTH: WSD_CONFIG_PARAM_TYPE = 13
class WSD_DATETIME(EasyCastStructure):
    isPositive: win32more.Windows.Win32.Foundation.BOOL
    year: UInt32
    month: Byte
    day: Byte
    hour: Byte
    minute: Byte
    second: Byte
    millisecond: UInt32
    TZIsLocal: win32more.Windows.Win32.Foundation.BOOL
    TZIsPositive: win32more.Windows.Win32.Foundation.BOOL
    TZHour: Byte
    TZMinute: Byte
class WSD_DURATION(EasyCastStructure):
    isPositive: win32more.Windows.Win32.Foundation.BOOL
    year: UInt32
    month: UInt32
    day: UInt32
    hour: UInt32
    minute: UInt32
    second: UInt32
    millisecond: UInt32
class WSD_ENDPOINT_REFERENCE(EasyCastStructure):
    Address: win32more.Windows.Win32.Foundation.PWSTR
    ReferenceProperties: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_REFERENCE_PROPERTIES
    ReferenceParameters: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_REFERENCE_PARAMETERS
    PortType: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head)
    ServiceName: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head)
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_ENDPOINT_REFERENCE_LIST(EasyCastStructure):
    Next: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_LIST_head)
    Element: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
class WSD_EVENT(EasyCastStructure):
    Hr: win32more.Windows.Win32.Foundation.HRESULT
    EventType: UInt32
    DispatchTag: win32more.Windows.Win32.Foundation.PWSTR
    HandlerContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_HANDLER_CONTEXT
    Soap: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head)
    Operation: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head)
    MessageParameters: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head
class WSD_EVENTING_DELIVERY_MODE(EasyCastStructure):
    Mode: win32more.Windows.Win32.Foundation.PWSTR
    Push: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_DELIVERY_MODE_PUSH_head)
    Data: VoidPtr
class WSD_EVENTING_DELIVERY_MODE_PUSH(EasyCastStructure):
    NotifyTo: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
class WSD_EVENTING_EXPIRES(EasyCastStructure):
    Duration: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_DURATION_head)
    DateTime: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_DATETIME_head)
class WSD_EVENTING_FILTER(EasyCastStructure):
    Dialect: win32more.Windows.Win32.Foundation.PWSTR
    FilterAction: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_FILTER_ACTION_head)
    Data: VoidPtr
class WSD_EVENTING_FILTER_ACTION(EasyCastStructure):
    Actions: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head)
class WSD_HANDLER_CONTEXT(EasyCastStructure):
    Handler: win32more.Windows.Win32.Devices.WebServicesOnDevices.PWSD_SOAP_MESSAGE_HANDLER
    PVoid: VoidPtr
    Unknown: win32more.Windows.Win32.System.Com.IUnknown_head
class WSD_HEADER_RELATESTO(EasyCastStructure):
    RelationshipType: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head)
    MessageID: win32more.Windows.Win32.Foundation.PWSTR
class WSD_HELLO(EasyCastStructure):
    EndpointReference: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    Types: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head)
    Scopes: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SCOPES_head)
    XAddrs: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head)
    MetadataVersion: UInt64
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_HOST_METADATA(EasyCastStructure):
    Host: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SERVICE_METADATA_head)
    Hosted: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SERVICE_METADATA_LIST_head)
class WSD_LOCALIZED_STRING(EasyCastStructure):
    lang: win32more.Windows.Win32.Foundation.PWSTR
    String: win32more.Windows.Win32.Foundation.PWSTR
class WSD_LOCALIZED_STRING_LIST(EasyCastStructure):
    Next: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST_head)
    Element: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_head)
class WSD_METADATA_SECTION(EasyCastStructure):
    Dialect: win32more.Windows.Win32.Foundation.PWSTR
    Identifier: win32more.Windows.Win32.Foundation.PWSTR
    Data: VoidPtr
    MetadataReference: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    Location: win32more.Windows.Win32.Foundation.PWSTR
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_METADATA_SECTION_LIST(EasyCastStructure):
    Next: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST_head)
    Element: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_head)
class WSD_NAME_LIST(EasyCastStructure):
    Next: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head)
    Element: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head)
class WSD_OPERATION(EasyCastStructure):
    RequestType: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_TYPE_head)
    ResponseType: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_TYPE_head)
    RequestStubFunction: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_STUB_FUNCTION
class WSD_PORT_TYPE(EasyCastStructure):
    EncodedName: UInt32
    OperationCount: UInt32
    Operations: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head)
    ProtocolType: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_PROTOCOL_TYPE
class WSD_PROBE(EasyCastStructure):
    Types: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head)
    Scopes: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SCOPES_head)
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_PROBE_MATCH(EasyCastStructure):
    EndpointReference: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    Types: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head)
    Scopes: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SCOPES_head)
    XAddrs: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head)
    MetadataVersion: UInt64
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_PROBE_MATCHES(EasyCastStructure):
    ProbeMatch: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_PROBE_MATCH_LIST_head)
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_PROBE_MATCH_LIST(EasyCastStructure):
    Next: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_PROBE_MATCH_LIST_head)
    Element: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_PROBE_MATCH_head)
WSD_PROTOCOL_TYPE = Int32
WSD_PT_NONE: WSD_PROTOCOL_TYPE = 0
WSD_PT_UDP: WSD_PROTOCOL_TYPE = 1
WSD_PT_HTTP: WSD_PROTOCOL_TYPE = 2
WSD_PT_HTTPS: WSD_PROTOCOL_TYPE = 4
WSD_PT_ALL: WSD_PROTOCOL_TYPE = 255
class WSD_REFERENCE_PARAMETERS(EasyCastStructure):
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_REFERENCE_PROPERTIES(EasyCastStructure):
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_RELATIONSHIP_METADATA(EasyCastStructure):
    Type: win32more.Windows.Win32.Foundation.PWSTR
    Data: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_HOST_METADATA_head)
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_RESOLVE(EasyCastStructure):
    EndpointReference: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_RESOLVE_MATCH(EasyCastStructure):
    EndpointReference: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    Types: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head)
    Scopes: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SCOPES_head)
    XAddrs: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head)
    MetadataVersion: UInt64
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_RESOLVE_MATCHES(EasyCastStructure):
    ResolveMatch: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_RESOLVE_MATCH_head)
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_SCOPES(EasyCastStructure):
    MatchBy: win32more.Windows.Win32.Foundation.PWSTR
    Scopes: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head)
class WSD_SECURITY_CERT_VALIDATION(EasyCastStructure):
    certMatchArray: POINTER(POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT_head))
    dwCertMatchArrayCount: UInt32
    hCertMatchStore: win32more.Windows.Win32.Security.Cryptography.HCERTSTORE
    hCertIssuerStore: win32more.Windows.Win32.Security.Cryptography.HCERTSTORE
    dwCertCheckOptions: UInt32
    pszCNGHashAlgId: win32more.Windows.Win32.Foundation.PWSTR
    pbCertHash: POINTER(Byte)
    dwCertHashSize: UInt32
class WSD_SECURITY_CERT_VALIDATION_V1(EasyCastStructure):
    certMatchArray: POINTER(POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT_head))
    dwCertMatchArrayCount: UInt32
    hCertMatchStore: win32more.Windows.Win32.Security.Cryptography.HCERTSTORE
    hCertIssuerStore: win32more.Windows.Win32.Security.Cryptography.HCERTSTORE
    dwCertCheckOptions: UInt32
class WSD_SECURITY_SIGNATURE_VALIDATION(EasyCastStructure):
    signingCertArray: POINTER(POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT_head))
    dwSigningCertArrayCount: UInt32
    hSigningCertStore: win32more.Windows.Win32.Security.Cryptography.HCERTSTORE
    dwFlags: UInt32
class WSD_SERVICE_METADATA(EasyCastStructure):
    EndpointReference: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_LIST_head)
    Types: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head)
    ServiceId: win32more.Windows.Win32.Foundation.PWSTR
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_SERVICE_METADATA_LIST(EasyCastStructure):
    Next: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SERVICE_METADATA_LIST_head)
    Element: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SERVICE_METADATA_head)
class WSD_SOAP_FAULT(EasyCastStructure):
    Code: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_CODE_head)
    Reason: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_REASON_head)
    Node: win32more.Windows.Win32.Foundation.PWSTR
    Role: win32more.Windows.Win32.Foundation.PWSTR
    Detail: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_SOAP_FAULT_CODE(EasyCastStructure):
    Value: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head)
    Subcode: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_SUBCODE_head)
class WSD_SOAP_FAULT_REASON(EasyCastStructure):
    Text: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST_head)
class WSD_SOAP_FAULT_SUBCODE(EasyCastStructure):
    Value: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head)
    Subcode: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_SUBCODE_head)
class WSD_SOAP_HEADER(EasyCastStructure):
    To: win32more.Windows.Win32.Foundation.PWSTR
    Action: win32more.Windows.Win32.Foundation.PWSTR
    MessageID: win32more.Windows.Win32.Foundation.PWSTR
    RelatesTo: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_HEADER_RELATESTO
    ReplyTo: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    From: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    FaultTo: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    AppSequence: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_APP_SEQUENCE_head)
    AnyHeaders: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_SOAP_MESSAGE(EasyCastStructure):
    Header: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_HEADER
    Body: VoidPtr
    BodyType: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_TYPE_head)
@winfunctype_pointer
def WSD_STUB_FUNCTION(server: win32more.Windows.Win32.System.Com.IUnknown_head, session: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDServiceMessaging_head, event: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class WSD_SYNCHRONOUS_RESPONSE_CONTEXT(EasyCastStructure):
    hr: win32more.Windows.Win32.Foundation.HRESULT
    eventHandle: win32more.Windows.Win32.Foundation.HANDLE
    messageParameters: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head
    results: VoidPtr
class WSD_THIS_DEVICE_METADATA(EasyCastStructure):
    FriendlyName: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST_head)
    FirmwareVersion: win32more.Windows.Win32.Foundation.PWSTR
    SerialNumber: win32more.Windows.Win32.Foundation.PWSTR
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_THIS_MODEL_METADATA(EasyCastStructure):
    Manufacturer: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST_head)
    ManufacturerUrl: win32more.Windows.Win32.Foundation.PWSTR
    ModelName: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST_head)
    ModelNumber: win32more.Windows.Win32.Foundation.PWSTR
    ModelUrl: win32more.Windows.Win32.Foundation.PWSTR
    PresentationUrl: win32more.Windows.Win32.Foundation.PWSTR
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_UNKNOWN_LOOKUP(EasyCastStructure):
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_URI_LIST(EasyCastStructure):
    Next: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head)
    Element: win32more.Windows.Win32.Foundation.PWSTR
make_head(_module, 'IWSDAddress')
make_head(_module, 'IWSDAsyncCallback')
make_head(_module, 'IWSDAsyncResult')
make_head(_module, 'IWSDAttachment')
make_head(_module, 'IWSDDeviceHost')
make_head(_module, 'IWSDDeviceHostNotify')
make_head(_module, 'IWSDDeviceProxy')
make_head(_module, 'IWSDEndpointProxy')
make_head(_module, 'IWSDEventingStatus')
make_head(_module, 'IWSDHttpAddress')
make_head(_module, 'IWSDHttpAuthParameters')
make_head(_module, 'IWSDHttpMessageParameters')
make_head(_module, 'IWSDInboundAttachment')
make_head(_module, 'IWSDMessageParameters')
make_head(_module, 'IWSDMetadataExchange')
make_head(_module, 'IWSDOutboundAttachment')
make_head(_module, 'IWSDSSLClientCertificate')
make_head(_module, 'IWSDScopeMatchingRule')
make_head(_module, 'IWSDServiceMessaging')
make_head(_module, 'IWSDServiceProxy')
make_head(_module, 'IWSDServiceProxyEventing')
make_head(_module, 'IWSDSignatureProperty')
make_head(_module, 'IWSDTransportAddress')
make_head(_module, 'IWSDUdpAddress')
make_head(_module, 'IWSDUdpMessageParameters')
make_head(_module, 'IWSDXMLContext')
make_head(_module, 'IWSDiscoveredService')
make_head(_module, 'IWSDiscoveryProvider')
make_head(_module, 'IWSDiscoveryProviderNotify')
make_head(_module, 'IWSDiscoveryPublisher')
make_head(_module, 'IWSDiscoveryPublisherNotify')
make_head(_module, 'PWSD_SOAP_MESSAGE_HANDLER')
make_head(_module, 'REQUESTBODY_GetStatus')
make_head(_module, 'REQUESTBODY_Renew')
make_head(_module, 'REQUESTBODY_Subscribe')
make_head(_module, 'REQUESTBODY_Unsubscribe')
make_head(_module, 'RESPONSEBODY_GetMetadata')
make_head(_module, 'RESPONSEBODY_GetStatus')
make_head(_module, 'RESPONSEBODY_Renew')
make_head(_module, 'RESPONSEBODY_Subscribe')
make_head(_module, 'RESPONSEBODY_SubscriptionEnd')
make_head(_module, 'WSDUdpRetransmitParams')
make_head(_module, 'WSDXML_ATTRIBUTE')
make_head(_module, 'WSDXML_ELEMENT')
make_head(_module, 'WSDXML_ELEMENT_LIST')
make_head(_module, 'WSDXML_NAME')
make_head(_module, 'WSDXML_NAMESPACE')
make_head(_module, 'WSDXML_NODE')
make_head(_module, 'WSDXML_PREFIX_MAPPING')
make_head(_module, 'WSDXML_TEXT')
make_head(_module, 'WSDXML_TYPE')
make_head(_module, 'WSD_APP_SEQUENCE')
make_head(_module, 'WSD_BYE')
make_head(_module, 'WSD_CONFIG_ADDRESSES')
make_head(_module, 'WSD_CONFIG_PARAM')
make_head(_module, 'WSD_DATETIME')
make_head(_module, 'WSD_DURATION')
make_head(_module, 'WSD_ENDPOINT_REFERENCE')
make_head(_module, 'WSD_ENDPOINT_REFERENCE_LIST')
make_head(_module, 'WSD_EVENT')
make_head(_module, 'WSD_EVENTING_DELIVERY_MODE')
make_head(_module, 'WSD_EVENTING_DELIVERY_MODE_PUSH')
make_head(_module, 'WSD_EVENTING_EXPIRES')
make_head(_module, 'WSD_EVENTING_FILTER')
make_head(_module, 'WSD_EVENTING_FILTER_ACTION')
make_head(_module, 'WSD_HANDLER_CONTEXT')
make_head(_module, 'WSD_HEADER_RELATESTO')
make_head(_module, 'WSD_HELLO')
make_head(_module, 'WSD_HOST_METADATA')
make_head(_module, 'WSD_LOCALIZED_STRING')
make_head(_module, 'WSD_LOCALIZED_STRING_LIST')
make_head(_module, 'WSD_METADATA_SECTION')
make_head(_module, 'WSD_METADATA_SECTION_LIST')
make_head(_module, 'WSD_NAME_LIST')
make_head(_module, 'WSD_OPERATION')
make_head(_module, 'WSD_PORT_TYPE')
make_head(_module, 'WSD_PROBE')
make_head(_module, 'WSD_PROBE_MATCH')
make_head(_module, 'WSD_PROBE_MATCHES')
make_head(_module, 'WSD_PROBE_MATCH_LIST')
make_head(_module, 'WSD_REFERENCE_PARAMETERS')
make_head(_module, 'WSD_REFERENCE_PROPERTIES')
make_head(_module, 'WSD_RELATIONSHIP_METADATA')
make_head(_module, 'WSD_RESOLVE')
make_head(_module, 'WSD_RESOLVE_MATCH')
make_head(_module, 'WSD_RESOLVE_MATCHES')
make_head(_module, 'WSD_SCOPES')
make_head(_module, 'WSD_SECURITY_CERT_VALIDATION')
make_head(_module, 'WSD_SECURITY_CERT_VALIDATION_V1')
make_head(_module, 'WSD_SECURITY_SIGNATURE_VALIDATION')
make_head(_module, 'WSD_SERVICE_METADATA')
make_head(_module, 'WSD_SERVICE_METADATA_LIST')
make_head(_module, 'WSD_SOAP_FAULT')
make_head(_module, 'WSD_SOAP_FAULT_CODE')
make_head(_module, 'WSD_SOAP_FAULT_REASON')
make_head(_module, 'WSD_SOAP_FAULT_SUBCODE')
make_head(_module, 'WSD_SOAP_HEADER')
make_head(_module, 'WSD_SOAP_MESSAGE')
make_head(_module, 'WSD_STUB_FUNCTION')
make_head(_module, 'WSD_SYNCHRONOUS_RESPONSE_CONTEXT')
make_head(_module, 'WSD_THIS_DEVICE_METADATA')
make_head(_module, 'WSD_THIS_MODEL_METADATA')
make_head(_module, 'WSD_UNKNOWN_LOOKUP')
make_head(_module, 'WSD_URI_LIST')
