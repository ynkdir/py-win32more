from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Devices.WebServicesOnDevices
import Windows.Win32.Foundation
import Windows.Win32.Networking.WinSock
import Windows.Win32.Security.Cryptography
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
def WSDCreateUdpMessageParameters(ppTxParams: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDUdpMessageParameters_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateUdpAddress(ppAddress: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDUdpAddress_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateHttpMessageParameters(ppTxParams: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDHttpMessageParameters_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateHttpAddress(ppAddress: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDHttpAddress_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateOutboundAttachment(ppAttachment: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDOutboundAttachment_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDXMLGetNameFromBuiltinNamespace(pszNamespace: Windows.Win32.Foundation.PWSTR, pszName: Windows.Win32.Foundation.PWSTR, ppName: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDXMLCreateContext(ppContext: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDiscoveryProvider(pContext: Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, ppProvider: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryProvider_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDiscoveryProvider2(pContext: Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, pConfigParams: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_head), dwConfigParamCount: UInt32, ppProvider: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryProvider_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDiscoveryPublisher(pContext: Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, ppPublisher: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryPublisher_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDiscoveryPublisher2(pContext: Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, pConfigParams: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_head), dwConfigParamCount: UInt32, ppPublisher: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryPublisher_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDeviceProxy(pszDeviceId: Windows.Win32.Foundation.PWSTR, pszLocalId: Windows.Win32.Foundation.PWSTR, pContext: Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, ppDeviceProxy: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceProxy_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDeviceProxyAdvanced(pszDeviceId: Windows.Win32.Foundation.PWSTR, pDeviceAddress: Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress_head, pszLocalId: Windows.Win32.Foundation.PWSTR, pContext: Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, ppDeviceProxy: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceProxy_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDeviceProxy2(pszDeviceId: Windows.Win32.Foundation.PWSTR, pszLocalId: Windows.Win32.Foundation.PWSTR, pContext: Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, pConfigParams: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_head), dwConfigParamCount: UInt32, ppDeviceProxy: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceProxy_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDeviceHost(pszLocalId: Windows.Win32.Foundation.PWSTR, pContext: Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, ppDeviceHost: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceHost_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDeviceHostAdvanced(pszLocalId: Windows.Win32.Foundation.PWSTR, pContext: Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, ppHostAddresses: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress_head), dwHostAddressCount: UInt32, ppDeviceHost: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceHost_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDeviceHost2(pszLocalId: Windows.Win32.Foundation.PWSTR, pContext: Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, pConfigParams: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_head), dwConfigParamCount: UInt32, ppDeviceHost: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceHost_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDSetConfigurationOption(dwOption: UInt32, pVoid: c_void_p, cbInBuffer: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDGetConfigurationOption(dwOption: UInt32, pVoid: c_void_p, cbOutBuffer: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDAllocateLinkedMemory(pParent: c_void_p, cbSize: UIntPtr) -> c_void_p: ...
@winfunctype('wsdapi.dll')
def WSDFreeLinkedMemory(pVoid: c_void_p) -> Void: ...
@winfunctype('wsdapi.dll')
def WSDAttachLinkedMemory(pParent: c_void_p, pChild: c_void_p) -> Void: ...
@winfunctype('wsdapi.dll')
def WSDDetachLinkedMemory(pVoid: c_void_p) -> Void: ...
@winfunctype('wsdapi.dll')
def WSDXMLBuildAnyForSingleElement(pElementName: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head), pszText: Windows.Win32.Foundation.PWSTR, ppAny: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDXMLGetValueFromAny(pszNamespace: Windows.Win32.Foundation.PWSTR, pszName: Windows.Win32.Foundation.PWSTR, pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), ppszValue: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDXMLAddSibling(pFirst: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pSecond: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDXMLAddChild(pParent: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pChild: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDXMLCleanupElement(pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDGenerateFault(pszCode: Windows.Win32.Foundation.PWSTR, pszSubCode: Windows.Win32.Foundation.PWSTR, pszReason: Windows.Win32.Foundation.PWSTR, pszDetail: Windows.Win32.Foundation.PWSTR, pContext: Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, ppFault: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDGenerateFaultEx(pCode: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head), pSubCode: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head), pReasons: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST_head), pszDetail: Windows.Win32.Foundation.PWSTR, ppFault: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDUriEncode(source: Windows.Win32.Foundation.PWSTR, cchSource: UInt32, destOut: POINTER(Windows.Win32.Foundation.PWSTR), cchDestOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDUriDecode(source: Windows.Win32.Foundation.PWSTR, cchSource: UInt32, destOut: POINTER(Windows.Win32.Foundation.PWSTR), cchDestOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
DeviceDiscoveryMechanism = Int32
DeviceDiscoveryMechanism_MulticastDiscovery: DeviceDiscoveryMechanism = 0
DeviceDiscoveryMechanism_DirectedDiscovery: DeviceDiscoveryMechanism = 1
DeviceDiscoveryMechanism_SecureDirectedDiscovery: DeviceDiscoveryMechanism = 2
class IWSDAddress(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b9574c6c-12a6-4f74-93-a1-33-18-ff-60-57-59')
    @commethod(3)
    def Serialize(pszBuffer: Windows.Win32.Foundation.PWSTR, cchLength: UInt32, fSafe: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Deserialize(pszBuffer: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDAsyncCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a63e109d-ce72-49e2-ba-98-e8-45-f5-ee-16-66')
    @commethod(3)
    def AsyncOperationComplete(pAsyncResult: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head, pAsyncState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDAsyncResult(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('11a9852a-8dd8-423e-b5-37-93-56-db-4f-bf-b8')
    @commethod(3)
    def SetCallback(pCallback: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncCallback_head, pAsyncState: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetWaitHandle(hWaitHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def HasCompleted() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAsyncState(ppAsyncState: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Abort() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetEvent(pEvent: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetEndpointProxy(ppEndpoint: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDEndpointProxy_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDAttachment(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5d55a616-9df8-4b09-b1-56-9b-a3-51-a4-8b-76')
class IWSDDeviceHost(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('917fe891-3d13-4138-98-09-93-4c-8a-be-b1-2c')
    @commethod(3)
    def Init(pszLocalId: Windows.Win32.Foundation.PWSTR, pContext: Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, ppHostAddresses: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress_head), dwHostAddressCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Start(ullInstanceId: UInt64, pScopeList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pNotificationSink: Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceHostNotify_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Stop() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Terminate() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RegisterPortType(pPortType: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_PORT_TYPE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetMetadata(pThisModelMetadata: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_THIS_MODEL_METADATA_head), pThisDeviceMetadata: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_THIS_DEVICE_METADATA_head), pHostMetadata: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_HOST_METADATA_head), pCustomMetadata: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RegisterService(pszServiceId: Windows.Win32.Foundation.PWSTR, pService: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RetireService(pszServiceId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AddDynamicService(pszServiceId: Windows.Win32.Foundation.PWSTR, pszEndpointAddress: Windows.Win32.Foundation.PWSTR, pPortType: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_PORT_TYPE_head), pPortName: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head), pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pService: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RemoveDynamicService(pszServiceId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetServiceDiscoverable(pszServiceId: Windows.Win32.Foundation.PWSTR, fDiscoverable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SignalEvent(pszServiceId: Windows.Win32.Foundation.PWSTR, pBody: c_void_p, pOperation: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDDeviceHostNotify(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b5bee9f9-eeda-41fe-96-f7-f4-5e-14-99-0f-b0')
    @commethod(3)
    def GetService(pszServiceId: Windows.Win32.Foundation.PWSTR, ppService: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDDeviceProxy(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('eee0c031-c578-4c0e-9a-3b-97-3c-35-f4-09-db')
    @commethod(3)
    def Init(pszDeviceId: Windows.Win32.Foundation.PWSTR, pDeviceAddress: Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress_head, pszLocalId: Windows.Win32.Foundation.PWSTR, pContext: Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head, pSponsor: Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceProxy_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginGetMetadata(ppResult: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EndGetMetadata(pResult: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetHostMetadata(ppHostMetadata: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_HOST_METADATA_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetThisModelMetadata(ppManufacturerMetadata: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_THIS_MODEL_METADATA_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetThisDeviceMetadata(ppThisDeviceMetadata: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_THIS_DEVICE_METADATA_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAllMetadata(ppMetadata: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetServiceProxyById(pszServiceId: Windows.Win32.Foundation.PWSTR, ppServiceProxy: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDServiceProxy_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetServiceProxyByType(pType: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head), ppServiceProxy: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDServiceProxy_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetEndpointProxy(ppProxy: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDEndpointProxy_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDEndpointProxy(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1860d430-b24c-4975-9f-90-db-b3-9b-aa-24-ec')
    @commethod(3)
    def SendOneWayRequest(pBody: c_void_p, pOperation: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SendTwoWayRequest(pBody: c_void_p, pOperation: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), pResponseContext: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SYNCHRONOUS_RESPONSE_CONTEXT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SendTwoWayRequestAsync(pBody: c_void_p, pOperation: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), pAsyncState: Windows.Win32.System.Com.IUnknown_head, pCallback: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncCallback_head, pResult: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AbortAsyncOperation(pAsyncResult: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ProcessFault(pFault: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetErrorInfo(ppszErrorInfo: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFaultInfo(ppFault: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDEventingStatus(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('49b17f52-637a-407a-ae-99-fb-e8-2a-4d-38-c0')
    @commethod(3)
    def SubscriptionRenewed(pszSubscriptionAction: Windows.Win32.Foundation.PWSTR) -> Void: ...
    @commethod(4)
    def SubscriptionRenewalFailed(pszSubscriptionAction: Windows.Win32.Foundation.PWSTR, hr: Windows.Win32.Foundation.HRESULT) -> Void: ...
    @commethod(5)
    def SubscriptionEnded(pszSubscriptionAction: Windows.Win32.Foundation.PWSTR) -> Void: ...
class IWSDHttpAddress(c_void_p):
    extends: Windows.Win32.Devices.WebServicesOnDevices.IWSDTransportAddress
    Guid = Guid('d09ac7bd-2a3e-4b85-86-05-27-37-ff-3e-4e-a0')
    @commethod(10)
    def GetSecure() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetSecure(fSecure: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetPath(ppszPath: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetPath(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDHttpAuthParameters(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0b476df0-8dac-480d-b0-5c-99-78-1a-58-84-aa')
    @commethod(3)
    def GetClientAccessToken(phToken: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAuthType(pAuthType: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDHttpMessageParameters(c_void_p):
    extends: Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters
    Guid = Guid('540bd122-5c83-4dec-b3-96-ea-62-a2-69-7f-df')
    @commethod(8)
    def SetInboundHttpHeaders(pszHeaders: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetInboundHttpHeaders(ppszHeaders: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetOutboundHttpHeaders(pszHeaders: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetOutboundHttpHeaders(ppszHeaders: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetID(pszId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetID(ppszId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetContext(pContext: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetContext(ppContext: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Clear() -> Windows.Win32.Foundation.HRESULT: ...
class IWSDInboundAttachment(c_void_p):
    extends: Windows.Win32.Devices.WebServicesOnDevices.IWSDAttachment
    Guid = Guid('5bd6ca65-233c-4fb8-9f-7a-26-41-61-96-55-c9')
    @commethod(3)
    def Read(pBuffer: c_char_p_no, dwBytesToRead: UInt32, pdwNumberOfBytesRead: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close() -> Windows.Win32.Foundation.HRESULT: ...
class IWSDMessageParameters(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1fafe8a2-e6fc-4b80-b6-cf-b7-d4-5c-41-6d-7c')
    @commethod(3)
    def GetLocalAddress(ppAddress: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetLocalAddress(pAddress: Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRemoteAddress(ppAddress: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetRemoteAddress(pAddress: Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetLowerParameters(ppTxParams: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDMetadataExchange(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('06996d57-1d67-4928-93-07-3d-78-33-fd-b8-46')
    @commethod(3)
    def GetMetadata(MetadataOut: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDOutboundAttachment(c_void_p):
    extends: Windows.Win32.Devices.WebServicesOnDevices.IWSDAttachment
    Guid = Guid('aa302f8d-5a22-4ba5-b3-92-aa-84-86-f4-c1-5d')
    @commethod(3)
    def Write(pBuffer: c_char_p_no, dwBytesToWrite: UInt32, pdwNumberOfBytesWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Abort() -> Windows.Win32.Foundation.HRESULT: ...
class IWSDSSLClientCertificate(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('de105e87-a0da-418e-98-ad-27-b9-ee-d8-7b-dc')
    @commethod(3)
    def GetClientCertificate(ppCertContext: POINTER(POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMappedAccessToken(phToken: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDScopeMatchingRule(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fcafe424-fef5-481a-bd-9f-33-ce-05-74-25-6f')
    @commethod(3)
    def GetScopeRule(ppszScopeMatchingRule: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MatchScopes(pszScope1: Windows.Win32.Foundation.PWSTR, pszScope2: Windows.Win32.Foundation.PWSTR, pfMatch: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDServiceMessaging(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('94974cf4-0cab-460d-a3-f6-7a-0a-d6-23-c0-e6')
    @commethod(3)
    def SendResponse(pBody: c_void_p, pOperation: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), pMessageParameters: Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FaultRequest(pRequestHeader: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_HEADER_head), pMessageParameters: Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head, pFault: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDServiceProxy(c_void_p):
    extends: Windows.Win32.Devices.WebServicesOnDevices.IWSDMetadataExchange
    Guid = Guid('d4c7fb9c-03ab-4175-9d-67-09-4f-af-eb-f4-87')
    @commethod(4)
    def BeginGetMetadata(ppResult: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EndGetMetadata(pResult: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head, ppMetadata: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetServiceMetadata(ppServiceMetadata: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SERVICE_METADATA_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SubscribeToOperation(pOperation: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), pUnknown: Windows.Win32.System.Com.IUnknown_head, pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), ppAny: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UnsubscribeToOperation(pOperation: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetEventingStatusCallback(pStatus: Windows.Win32.Devices.WebServicesOnDevices.IWSDEventingStatus_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetEndpointProxy(ppProxy: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDEndpointProxy_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDServiceProxyEventing(c_void_p):
    extends: Windows.Win32.Devices.WebServicesOnDevices.IWSDServiceProxy
    Guid = Guid('f9279d6d-1012-4a94-b8-cc-fd-35-d2-20-2b-fe')
    @commethod(11)
    def SubscribeToMultipleOperations(pOperations: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pUnknown: Windows.Win32.System.Com.IUnknown_head, pExpires: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head), pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), ppExpires: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)), ppAny: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def BeginSubscribeToMultipleOperations(pOperations: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pUnknown: Windows.Win32.System.Com.IUnknown_head, pExpires: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head), pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pAsyncState: Windows.Win32.System.Com.IUnknown_head, pAsyncCallback: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncCallback_head, ppResult: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def EndSubscribeToMultipleOperations(pOperations: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pResult: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head, ppExpires: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)), ppAny: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def UnsubscribeToMultipleOperations(pOperations: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def BeginUnsubscribeToMultipleOperations(pOperations: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pAsyncState: Windows.Win32.System.Com.IUnknown_head, pAsyncCallback: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncCallback_head, ppResult: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def EndUnsubscribeToMultipleOperations(pOperations: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pResult: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def RenewMultipleOperations(pOperations: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pExpires: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head), pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), ppExpires: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)), ppAny: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def BeginRenewMultipleOperations(pOperations: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pExpires: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head), pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pAsyncState: Windows.Win32.System.Com.IUnknown_head, pAsyncCallback: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncCallback_head, ppResult: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def EndRenewMultipleOperations(pOperations: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pResult: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head, ppExpires: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)), ppAny: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetStatusForMultipleOperations(pOperations: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), ppExpires: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)), ppAny: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def BeginGetStatusForMultipleOperations(pOperations: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pAsyncState: Windows.Win32.System.Com.IUnknown_head, pAsyncCallback: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncCallback_head, ppResult: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def EndGetStatusForMultipleOperations(pOperations: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head), dwOperationCount: UInt32, pResult: Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult_head, ppExpires: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)), ppAny: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDSignatureProperty(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('03ce20aa-71c4-45e2-b3-2e-37-66-c6-1c-79-0f')
    @commethod(3)
    def IsMessageSigned(pbSigned: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsMessageSignatureTrusted(pbSignatureTrusted: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetKeyInfo(pbKeyInfo: c_char_p_no, pdwKeyInfoSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSignature(pbSignature: c_char_p_no, pdwSignatureSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSignedInfoHash(pbSignedInfoHash: c_char_p_no, pdwHashSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDTransportAddress(c_void_p):
    extends: Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress
    Guid = Guid('70d23498-4ee6-4340-a3-df-d8-45-d2-23-54-67')
    @commethod(5)
    def GetPort(pwPort: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetPort(wPort: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTransportAddress(ppszAddress: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTransportAddressEx(fSafe: Windows.Win32.Foundation.BOOL, ppszAddress: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetTransportAddress(pszAddress: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDUdpAddress(c_void_p):
    extends: Windows.Win32.Devices.WebServicesOnDevices.IWSDTransportAddress
    Guid = Guid('74d6124a-a441-4f78-a1-eb-97-a8-d1-99-68-93')
    @commethod(10)
    def SetSockaddr(pSockAddr: POINTER(Windows.Win32.Networking.WinSock.SOCKADDR_STORAGE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetSockaddr(pSockAddr: POINTER(Windows.Win32.Networking.WinSock.SOCKADDR_STORAGE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetExclusive(fExclusive: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetExclusive() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetMessageType(messageType: Windows.Win32.Devices.WebServicesOnDevices.WSDUdpMessageType) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetMessageType(pMessageType: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDUdpMessageType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetTTL(dwTTL: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetTTL(pdwTTL: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetAlias(pAlias: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetAlias(pAlias: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDUdpMessageParameters(c_void_p):
    extends: Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters
    Guid = Guid('9934149f-8f0c-447b-aa-0b-73-12-4b-0c-a7-f0')
    @commethod(8)
    def SetRetransmitParams(pParams: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDUdpRetransmitParams_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRetransmitParams(pParams: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDUdpRetransmitParams_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDXMLContext(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('75d8f3ee-3e5a-43b4-a1-5a-bc-f6-88-74-60-c0')
    @commethod(3)
    def AddNamespace(pszUri: Windows.Win32.Foundation.PWSTR, pszSuggestedPrefix: Windows.Win32.Foundation.PWSTR, ppNamespace: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAMESPACE_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddNameToNamespace(pszUri: Windows.Win32.Foundation.PWSTR, pszName: Windows.Win32.Foundation.PWSTR, ppName: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetNamespaces(pNamespaces: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAMESPACE_head)), wNamespacesCount: UInt16, bLayerNumber: Byte) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetTypes(pTypes: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_TYPE_head)), dwTypesCount: UInt32, bLayerNumber: Byte) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDiscoveredService(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4bad8a3b-b374-4420-96-32-aa-c9-45-b3-74-aa')
    @commethod(3)
    def GetEndpointReference(ppEndpointReference: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTypes(ppTypesList: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetScopes(ppScopesList: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetXAddrs(ppXAddrsList: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetMetadataVersion(pullMetadataVersion: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetExtendedDiscoXML(ppHeaderAny: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)), ppBodyAny: POINTER(POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetProbeResolveTag(ppszTag: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRemoteTransportAddress(ppszRemoteTransportAddress: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetLocalTransportAddress(ppszLocalTransportAddress: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetLocalInterfaceGUID(pGuid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetInstanceId(pullInstanceId: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDiscoveryProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8ffc8e55-f0eb-480f-88-b7-b4-35-dd-28-1d-45')
    @commethod(3)
    def SetAddressFamily(dwAddressFamily: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Attach(pSink: Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryProviderNotify_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Detach() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SearchById(pszId: Windows.Win32.Foundation.PWSTR, pszTag: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SearchByAddress(pszAddress: Windows.Win32.Foundation.PWSTR, pszTag: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SearchByType(pTypesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head), pScopesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pszMatchBy: Windows.Win32.Foundation.PWSTR, pszTag: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetXMLContext(ppContext: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDiscoveryProviderNotify(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('73ee3ced-b6e6-4329-a5-46-3e-8a-d4-65-63-d2')
    @commethod(3)
    def Add(pService: Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveredService_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Remove(pService: Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveredService_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SearchFailed(hr: Windows.Win32.Foundation.HRESULT, pszTag: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SearchComplete(pszTag: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDiscoveryPublisher(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ae01e1a8-3ff9-4148-81-16-05-7c-c6-16-fe-13')
    @commethod(3)
    def SetAddressFamily(dwAddressFamily: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RegisterNotificationSink(pSink: Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryPublisherNotify_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def UnRegisterNotificationSink(pSink: Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryPublisherNotify_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Publish(pszId: Windows.Win32.Foundation.PWSTR, ullMetadataVersion: UInt64, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: Windows.Win32.Foundation.PWSTR, pTypesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head), pScopesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pXAddrsList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UnPublish(pszId: Windows.Win32.Foundation.PWSTR, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: Windows.Win32.Foundation.PWSTR, pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def MatchProbe(pProbeMessage: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head), pMessageParameters: Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head, pszId: Windows.Win32.Foundation.PWSTR, ullMetadataVersion: UInt64, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: Windows.Win32.Foundation.PWSTR, pTypesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head), pScopesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pXAddrsList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def MatchResolve(pResolveMessage: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head), pMessageParameters: Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head, pszId: Windows.Win32.Foundation.PWSTR, ullMetadataVersion: UInt64, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: Windows.Win32.Foundation.PWSTR, pTypesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head), pScopesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pXAddrsList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def PublishEx(pszId: Windows.Win32.Foundation.PWSTR, ullMetadataVersion: UInt64, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: Windows.Win32.Foundation.PWSTR, pTypesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head), pScopesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pXAddrsList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pHeaderAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pReferenceParameterAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pPolicyAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pEndpointReferenceAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def MatchProbeEx(pProbeMessage: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head), pMessageParameters: Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head, pszId: Windows.Win32.Foundation.PWSTR, ullMetadataVersion: UInt64, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: Windows.Win32.Foundation.PWSTR, pTypesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head), pScopesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pXAddrsList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pHeaderAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pReferenceParameterAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pPolicyAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pEndpointReferenceAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def MatchResolveEx(pResolveMessage: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head), pMessageParameters: Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head, pszId: Windows.Win32.Foundation.PWSTR, ullMetadataVersion: UInt64, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: Windows.Win32.Foundation.PWSTR, pTypesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head), pScopesList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pXAddrsList: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head), pHeaderAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pReferenceParameterAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pPolicyAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pEndpointReferenceAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head), pAny: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def RegisterScopeMatchingRule(pScopeMatchingRule: Windows.Win32.Devices.WebServicesOnDevices.IWSDScopeMatchingRule_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def UnRegisterScopeMatchingRule(pScopeMatchingRule: Windows.Win32.Devices.WebServicesOnDevices.IWSDScopeMatchingRule_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetXMLContext(ppContext: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWSDiscoveryPublisherNotify(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e67651b0-337a-4b3c-97-58-73-33-88-56-82-51')
    @commethod(3)
    def ProbeHandler(pSoap: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head), pMessageParameters: Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ResolveHandler(pSoap: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head), pMessageParameters: Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PWSD_SOAP_MESSAGE_HANDLER(thisUnknown: Windows.Win32.System.Com.IUnknown_head, event: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class REQUESTBODY_GetStatus(Structure):
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class REQUESTBODY_Renew(Structure):
    Expires: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class REQUESTBODY_Subscribe(Structure):
    EndTo: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    Delivery: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_DELIVERY_MODE_head)
    Expires: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)
    Filter: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_FILTER_head)
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class REQUESTBODY_Unsubscribe(Structure):
    any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class RESPONSEBODY_GetMetadata(Structure):
    Metadata: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST_head)
class RESPONSEBODY_GetStatus(Structure):
    expires: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)
    any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class RESPONSEBODY_Renew(Structure):
    expires: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)
    any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class RESPONSEBODY_Subscribe(Structure):
    SubscriptionManager: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    expires: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)
    any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class RESPONSEBODY_SubscriptionEnd(Structure):
    SubscriptionManager: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    Status: Windows.Win32.Foundation.PWSTR
    Reason: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_head)
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
WSDEventType = Int32
WSDET_NONE: WSDEventType = 0
WSDET_INCOMING_MESSAGE: WSDEventType = 1
WSDET_INCOMING_FAULT: WSDEventType = 2
WSDET_TRANSMISSION_FAILURE: WSDEventType = 3
WSDET_RESPONSE_TIMEOUT: WSDEventType = 4
WSDUdpMessageType = Int32
ONE_WAY: WSDUdpMessageType = 0
TWO_WAY: WSDUdpMessageType = 1
class WSDUdpRetransmitParams(Structure):
    ulSendDelay: UInt32
    ulRepeat: UInt32
    ulRepeatMinDelay: UInt32
    ulRepeatMaxDelay: UInt32
    ulRepeatUpperDelay: UInt32
class WSDXML_ATTRIBUTE(Structure):
    Element: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
    Next: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ATTRIBUTE_head)
    Name: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head)
    Value: Windows.Win32.Foundation.PWSTR
class WSDXML_ELEMENT(Structure):
    Node: Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NODE
    Name: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head)
    FirstAttribute: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ATTRIBUTE_head)
    FirstChild: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NODE_head)
    PrefixMappings: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_PREFIX_MAPPING_head)
class WSDXML_ELEMENT_LIST(Structure):
    Next: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_LIST_head)
    Element: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSDXML_NAME(Structure):
    Space: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAMESPACE_head)
    LocalName: Windows.Win32.Foundation.PWSTR
class WSDXML_NAMESPACE(Structure):
    Uri: Windows.Win32.Foundation.PWSTR
    PreferredPrefix: Windows.Win32.Foundation.PWSTR
    Names: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head)
    NamesCount: UInt16
    Encoding: UInt16
class WSDXML_NODE(Structure):
    ElementType = 0
    TextType = 1
    Type: Int32
    Parent: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
    Next: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NODE_head)
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
class WSDXML_PREFIX_MAPPING(Structure):
    Refs: UInt32
    Next: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_PREFIX_MAPPING_head)
    Space: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAMESPACE_head)
    Prefix: Windows.Win32.Foundation.PWSTR
class WSDXML_TEXT(Structure):
    Node: Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NODE
    Text: Windows.Win32.Foundation.PWSTR
class WSDXML_TYPE(Structure):
    Uri: Windows.Win32.Foundation.PWSTR
    Table: c_char_p_no
class WSD_APP_SEQUENCE(Structure):
    InstanceId: UInt64
    SequenceId: Windows.Win32.Foundation.PWSTR
    MessageNumber: UInt64
class WSD_BYE(Structure):
    EndpointReference: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_CONFIG_ADDRESSES(Structure):
    addresses: POINTER(Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress_head)
    dwAddressCount: UInt32
class WSD_CONFIG_PARAM(Structure):
    configParamType: Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_TYPE
    pConfigData: c_void_p
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
class WSD_DATETIME(Structure):
    isPositive: Windows.Win32.Foundation.BOOL
    year: UInt32
    month: Byte
    day: Byte
    hour: Byte
    minute: Byte
    second: Byte
    millisecond: UInt32
    TZIsLocal: Windows.Win32.Foundation.BOOL
    TZIsPositive: Windows.Win32.Foundation.BOOL
    TZHour: Byte
    TZMinute: Byte
class WSD_DURATION(Structure):
    isPositive: Windows.Win32.Foundation.BOOL
    year: UInt32
    month: UInt32
    day: UInt32
    hour: UInt32
    minute: UInt32
    second: UInt32
    millisecond: UInt32
class WSD_ENDPOINT_REFERENCE(Structure):
    Address: Windows.Win32.Foundation.PWSTR
    ReferenceProperties: Windows.Win32.Devices.WebServicesOnDevices.WSD_REFERENCE_PROPERTIES
    ReferenceParameters: Windows.Win32.Devices.WebServicesOnDevices.WSD_REFERENCE_PARAMETERS
    PortType: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head)
    ServiceName: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head)
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_ENDPOINT_REFERENCE_LIST(Structure):
    Next: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_LIST_head)
    Element: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
class WSD_EVENT(Structure):
    Hr: Windows.Win32.Foundation.HRESULT
    EventType: UInt32
    DispatchTag: Windows.Win32.Foundation.PWSTR
    HandlerContext: Windows.Win32.Devices.WebServicesOnDevices.WSD_HANDLER_CONTEXT
    Soap: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head)
    Operation: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head)
    MessageParameters: Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head
class WSD_EVENTING_DELIVERY_MODE(Structure):
    Mode: Windows.Win32.Foundation.PWSTR
    Push: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_DELIVERY_MODE_PUSH_head)
    Data: c_void_p
class WSD_EVENTING_DELIVERY_MODE_PUSH(Structure):
    NotifyTo: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
class WSD_EVENTING_EXPIRES(Structure):
    Duration: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_DURATION_head)
    DateTime: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_DATETIME_head)
class WSD_EVENTING_FILTER(Structure):
    Dialect: Windows.Win32.Foundation.PWSTR
    FilterAction: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_FILTER_ACTION_head)
    Data: c_void_p
class WSD_EVENTING_FILTER_ACTION(Structure):
    Actions: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head)
class WSD_HANDLER_CONTEXT(Structure):
    Handler: Windows.Win32.Devices.WebServicesOnDevices.PWSD_SOAP_MESSAGE_HANDLER
    PVoid: c_void_p
    Unknown: Windows.Win32.System.Com.IUnknown_head
class WSD_HEADER_RELATESTO(Structure):
    RelationshipType: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head)
    MessageID: Windows.Win32.Foundation.PWSTR
class WSD_HELLO(Structure):
    EndpointReference: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    Types: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head)
    Scopes: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SCOPES_head)
    XAddrs: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head)
    MetadataVersion: UInt64
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_HOST_METADATA(Structure):
    Host: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SERVICE_METADATA_head)
    Hosted: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SERVICE_METADATA_LIST_head)
class WSD_LOCALIZED_STRING(Structure):
    lang: Windows.Win32.Foundation.PWSTR
    String: Windows.Win32.Foundation.PWSTR
class WSD_LOCALIZED_STRING_LIST(Structure):
    Next: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST_head)
    Element: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_head)
class WSD_METADATA_SECTION(Structure):
    Dialect: Windows.Win32.Foundation.PWSTR
    Identifier: Windows.Win32.Foundation.PWSTR
    Data: c_void_p
    MetadataReference: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    Location: Windows.Win32.Foundation.PWSTR
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_METADATA_SECTION_LIST(Structure):
    Next: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST_head)
    Element: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_head)
class WSD_NAME_LIST(Structure):
    Next: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head)
    Element: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head)
class WSD_OPERATION(Structure):
    RequestType: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_TYPE_head)
    ResponseType: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_TYPE_head)
    RequestStubFunction: Windows.Win32.Devices.WebServicesOnDevices.WSD_STUB_FUNCTION
class WSD_PORT_TYPE(Structure):
    EncodedName: UInt32
    OperationCount: UInt32
    Operations: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION_head)
    ProtocolType: Windows.Win32.Devices.WebServicesOnDevices.WSD_PROTOCOL_TYPE
class WSD_PROBE(Structure):
    Types: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head)
    Scopes: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SCOPES_head)
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_PROBE_MATCH(Structure):
    EndpointReference: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    Types: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head)
    Scopes: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SCOPES_head)
    XAddrs: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head)
    MetadataVersion: UInt64
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_PROBE_MATCHES(Structure):
    ProbeMatch: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_PROBE_MATCH_LIST_head)
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_PROBE_MATCH_LIST(Structure):
    Next: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_PROBE_MATCH_LIST_head)
    Element: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_PROBE_MATCH_head)
WSD_PROTOCOL_TYPE = Int32
WSD_PT_NONE: WSD_PROTOCOL_TYPE = 0
WSD_PT_UDP: WSD_PROTOCOL_TYPE = 1
WSD_PT_HTTP: WSD_PROTOCOL_TYPE = 2
WSD_PT_HTTPS: WSD_PROTOCOL_TYPE = 4
WSD_PT_ALL: WSD_PROTOCOL_TYPE = 255
class WSD_REFERENCE_PARAMETERS(Structure):
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_REFERENCE_PROPERTIES(Structure):
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_RELATIONSHIP_METADATA(Structure):
    Type: Windows.Win32.Foundation.PWSTR
    Data: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_HOST_METADATA_head)
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_RESOLVE(Structure):
    EndpointReference: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_RESOLVE_MATCH(Structure):
    EndpointReference: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    Types: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head)
    Scopes: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SCOPES_head)
    XAddrs: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head)
    MetadataVersion: UInt64
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_RESOLVE_MATCHES(Structure):
    ResolveMatch: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_RESOLVE_MATCH_head)
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_SCOPES(Structure):
    MatchBy: Windows.Win32.Foundation.PWSTR
    Scopes: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head)
class WSD_SECURITY_CERT_VALIDATION(Structure):
    certMatchArray: POINTER(POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head))
    dwCertMatchArrayCount: UInt32
    hCertMatchStore: Windows.Win32.Security.Cryptography.HCERTSTORE
    hCertIssuerStore: Windows.Win32.Security.Cryptography.HCERTSTORE
    dwCertCheckOptions: UInt32
    pszCNGHashAlgId: Windows.Win32.Foundation.PWSTR
    pbCertHash: c_char_p_no
    dwCertHashSize: UInt32
class WSD_SECURITY_CERT_VALIDATION_V1(Structure):
    certMatchArray: POINTER(POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head))
    dwCertMatchArrayCount: UInt32
    hCertMatchStore: Windows.Win32.Security.Cryptography.HCERTSTORE
    hCertIssuerStore: Windows.Win32.Security.Cryptography.HCERTSTORE
    dwCertCheckOptions: UInt32
class WSD_SECURITY_SIGNATURE_VALIDATION(Structure):
    signingCertArray: POINTER(POINTER(Windows.Win32.Security.Cryptography.CERT_CONTEXT_head))
    dwSigningCertArrayCount: UInt32
    hSigningCertStore: Windows.Win32.Security.Cryptography.HCERTSTORE
    dwFlags: UInt32
class WSD_SERVICE_METADATA(Structure):
    EndpointReference: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_LIST_head)
    Types: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST_head)
    ServiceId: Windows.Win32.Foundation.PWSTR
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_SERVICE_METADATA_LIST(Structure):
    Next: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SERVICE_METADATA_LIST_head)
    Element: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SERVICE_METADATA_head)
class WSD_SOAP_FAULT(Structure):
    Code: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_CODE_head)
    Reason: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_REASON_head)
    Node: Windows.Win32.Foundation.PWSTR
    Role: Windows.Win32.Foundation.PWSTR
    Detail: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_SOAP_FAULT_CODE(Structure):
    Value: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head)
    Subcode: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_SUBCODE_head)
class WSD_SOAP_FAULT_REASON(Structure):
    Text: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST_head)
class WSD_SOAP_FAULT_SUBCODE(Structure):
    Value: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME_head)
    Subcode: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_SUBCODE_head)
class WSD_SOAP_HEADER(Structure):
    To: Windows.Win32.Foundation.PWSTR
    Action: Windows.Win32.Foundation.PWSTR
    MessageID: Windows.Win32.Foundation.PWSTR
    RelatesTo: Windows.Win32.Devices.WebServicesOnDevices.WSD_HEADER_RELATESTO
    ReplyTo: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    From: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    FaultTo: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)
    AppSequence: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_APP_SEQUENCE_head)
    AnyHeaders: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_SOAP_MESSAGE(Structure):
    Header: Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_HEADER
    Body: c_void_p
    BodyType: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_TYPE_head)
@winfunctype_pointer
def WSD_STUB_FUNCTION(server: Windows.Win32.System.Com.IUnknown_head, session: Windows.Win32.Devices.WebServicesOnDevices.IWSDServiceMessaging_head, event: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class WSD_SYNCHRONOUS_RESPONSE_CONTEXT(Structure):
    hr: Windows.Win32.Foundation.HRESULT
    eventHandle: Windows.Win32.Foundation.HANDLE
    messageParameters: Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters_head
    results: c_void_p
class WSD_THIS_DEVICE_METADATA(Structure):
    FriendlyName: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST_head)
    FirmwareVersion: Windows.Win32.Foundation.PWSTR
    SerialNumber: Windows.Win32.Foundation.PWSTR
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_THIS_MODEL_METADATA(Structure):
    Manufacturer: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST_head)
    ManufacturerUrl: Windows.Win32.Foundation.PWSTR
    ModelName: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST_head)
    ModelNumber: Windows.Win32.Foundation.PWSTR
    ModelUrl: Windows.Win32.Foundation.PWSTR
    PresentationUrl: Windows.Win32.Foundation.PWSTR
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_UNKNOWN_LOOKUP(Structure):
    Any: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)
class WSD_URI_LIST(Structure):
    Next: POINTER(Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST_head)
    Element: Windows.Win32.Foundation.PWSTR
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
__all__ = [
    "DeviceDiscoveryMechanism",
    "DeviceDiscoveryMechanism_DirectedDiscovery",
    "DeviceDiscoveryMechanism_MulticastDiscovery",
    "DeviceDiscoveryMechanism_SecureDirectedDiscovery",
    "IWSDAddress",
    "IWSDAsyncCallback",
    "IWSDAsyncResult",
    "IWSDAttachment",
    "IWSDDeviceHost",
    "IWSDDeviceHostNotify",
    "IWSDDeviceProxy",
    "IWSDEndpointProxy",
    "IWSDEventingStatus",
    "IWSDHttpAddress",
    "IWSDHttpAuthParameters",
    "IWSDHttpMessageParameters",
    "IWSDInboundAttachment",
    "IWSDMessageParameters",
    "IWSDMetadataExchange",
    "IWSDOutboundAttachment",
    "IWSDSSLClientCertificate",
    "IWSDScopeMatchingRule",
    "IWSDServiceMessaging",
    "IWSDServiceProxy",
    "IWSDServiceProxyEventing",
    "IWSDSignatureProperty",
    "IWSDTransportAddress",
    "IWSDUdpAddress",
    "IWSDUdpMessageParameters",
    "IWSDXMLContext",
    "IWSDiscoveredService",
    "IWSDiscoveryProvider",
    "IWSDiscoveryProviderNotify",
    "IWSDiscoveryPublisher",
    "IWSDiscoveryPublisherNotify",
    "ONE_WAY",
    "PWSD_SOAP_MESSAGE_HANDLER",
    "REQUESTBODY_GetStatus",
    "REQUESTBODY_Renew",
    "REQUESTBODY_Subscribe",
    "REQUESTBODY_Unsubscribe",
    "RESPONSEBODY_GetMetadata",
    "RESPONSEBODY_GetStatus",
    "RESPONSEBODY_Renew",
    "RESPONSEBODY_Subscribe",
    "RESPONSEBODY_SubscriptionEnd",
    "TWO_WAY",
    "WSDAPI_ADDRESSFAMILY_IPV4",
    "WSDAPI_ADDRESSFAMILY_IPV6",
    "WSDAPI_COMPACTSIG_ACCEPT_ALL_MESSAGES",
    "WSDAPI_OPTION_MAX_INBOUND_MESSAGE_SIZE",
    "WSDAPI_OPTION_TRACE_XML_TO_DEBUGGER",
    "WSDAPI_OPTION_TRACE_XML_TO_FILE",
    "WSDAPI_SSL_CERT_APPLY_DEFAULT_CHECKS",
    "WSDAPI_SSL_CERT_IGNORE_EXPIRY",
    "WSDAPI_SSL_CERT_IGNORE_INVALID_CN",
    "WSDAPI_SSL_CERT_IGNORE_REVOCATION",
    "WSDAPI_SSL_CERT_IGNORE_UNKNOWN_CA",
    "WSDAPI_SSL_CERT_IGNORE_WRONG_USAGE",
    "WSDAllocateLinkedMemory",
    "WSDAttachLinkedMemory",
    "WSDCreateDeviceHost",
    "WSDCreateDeviceHost2",
    "WSDCreateDeviceHostAdvanced",
    "WSDCreateDeviceProxy",
    "WSDCreateDeviceProxy2",
    "WSDCreateDeviceProxyAdvanced",
    "WSDCreateDiscoveryProvider",
    "WSDCreateDiscoveryProvider2",
    "WSDCreateDiscoveryPublisher",
    "WSDCreateDiscoveryPublisher2",
    "WSDCreateHttpAddress",
    "WSDCreateHttpMessageParameters",
    "WSDCreateOutboundAttachment",
    "WSDCreateUdpAddress",
    "WSDCreateUdpMessageParameters",
    "WSDDetachLinkedMemory",
    "WSDET_INCOMING_FAULT",
    "WSDET_INCOMING_MESSAGE",
    "WSDET_NONE",
    "WSDET_RESPONSE_TIMEOUT",
    "WSDET_TRANSMISSION_FAILURE",
    "WSDEventType",
    "WSDFreeLinkedMemory",
    "WSDGenerateFault",
    "WSDGenerateFaultEx",
    "WSDGetConfigurationOption",
    "WSDSetConfigurationOption",
    "WSDUdpMessageType",
    "WSDUdpRetransmitParams",
    "WSDUriDecode",
    "WSDUriEncode",
    "WSDXMLAddChild",
    "WSDXMLAddSibling",
    "WSDXMLBuildAnyForSingleElement",
    "WSDXMLCleanupElement",
    "WSDXMLCreateContext",
    "WSDXMLGetNameFromBuiltinNamespace",
    "WSDXMLGetValueFromAny",
    "WSDXML_ATTRIBUTE",
    "WSDXML_ELEMENT",
    "WSDXML_ELEMENT_LIST",
    "WSDXML_NAME",
    "WSDXML_NAMESPACE",
    "WSDXML_NODE",
    "WSDXML_OP",
    "WSDXML_OP_OpAnyElement",
    "WSDXML_OP_OpAnyElements",
    "WSDXML_OP_OpAnyNumber",
    "WSDXML_OP_OpAnyText",
    "WSDXML_OP_OpAnything",
    "WSDXML_OP_OpAttribute_",
    "WSDXML_OP_OpBeginAll",
    "WSDXML_OP_OpBeginAnyElement",
    "WSDXML_OP_OpBeginChoice",
    "WSDXML_OP_OpBeginElement_",
    "WSDXML_OP_OpBeginSequence",
    "WSDXML_OP_OpElement_",
    "WSDXML_OP_OpEndAll",
    "WSDXML_OP_OpEndChoice",
    "WSDXML_OP_OpEndElement",
    "WSDXML_OP_OpEndOfTable",
    "WSDXML_OP_OpEndSequence",
    "WSDXML_OP_OpFormatBool_",
    "WSDXML_OP_OpFormatDateTime_",
    "WSDXML_OP_OpFormatDom_",
    "WSDXML_OP_OpFormatDouble_",
    "WSDXML_OP_OpFormatDuration_",
    "WSDXML_OP_OpFormatDynamicType_",
    "WSDXML_OP_OpFormatFloat_",
    "WSDXML_OP_OpFormatInt16_",
    "WSDXML_OP_OpFormatInt32_",
    "WSDXML_OP_OpFormatInt64_",
    "WSDXML_OP_OpFormatInt8_",
    "WSDXML_OP_OpFormatListInsertTail_",
    "WSDXML_OP_OpFormatLookupType_",
    "WSDXML_OP_OpFormatMax",
    "WSDXML_OP_OpFormatName_",
    "WSDXML_OP_OpFormatStruct_",
    "WSDXML_OP_OpFormatType_",
    "WSDXML_OP_OpFormatUInt16_",
    "WSDXML_OP_OpFormatUInt32_",
    "WSDXML_OP_OpFormatUInt64_",
    "WSDXML_OP_OpFormatUInt8_",
    "WSDXML_OP_OpFormatUnicodeString_",
    "WSDXML_OP_OpFormatUri_",
    "WSDXML_OP_OpFormatUuidUri_",
    "WSDXML_OP_OpFormatXMLDeclaration_",
    "WSDXML_OP_OpNone",
    "WSDXML_OP_OpOneOrMore",
    "WSDXML_OP_OpOptional",
    "WSDXML_OP_OpProcess_",
    "WSDXML_OP_OpQualifiedAttribute_",
    "WSDXML_PREFIX_MAPPING",
    "WSDXML_TEXT",
    "WSDXML_TYPE",
    "WSD_APP_SEQUENCE",
    "WSD_BYE",
    "WSD_CONFIG_ADDRESSES",
    "WSD_CONFIG_DEVICE_ADDRESSES",
    "WSD_CONFIG_HOSTING_ADDRESSES",
    "WSD_CONFIG_MAX_INBOUND_MESSAGE_SIZE",
    "WSD_CONFIG_MAX_OUTBOUND_MESSAGE_SIZE",
    "WSD_CONFIG_PARAM",
    "WSD_CONFIG_PARAM_TYPE",
    "WSD_DATETIME",
    "WSD_DEFAULT_EVENTING_ADDRESS",
    "WSD_DEFAULT_HOSTING_ADDRESS",
    "WSD_DEFAULT_SECURE_HOSTING_ADDRESS",
    "WSD_DURATION",
    "WSD_ENDPOINT_REFERENCE",
    "WSD_ENDPOINT_REFERENCE_LIST",
    "WSD_EVENT",
    "WSD_EVENTING_DELIVERY_MODE",
    "WSD_EVENTING_DELIVERY_MODE_PUSH",
    "WSD_EVENTING_EXPIRES",
    "WSD_EVENTING_FILTER",
    "WSD_EVENTING_FILTER_ACTION",
    "WSD_HANDLER_CONTEXT",
    "WSD_HEADER_RELATESTO",
    "WSD_HELLO",
    "WSD_HOST_METADATA",
    "WSD_LOCALIZED_STRING",
    "WSD_LOCALIZED_STRING_LIST",
    "WSD_METADATA_SECTION",
    "WSD_METADATA_SECTION_LIST",
    "WSD_NAME_LIST",
    "WSD_OPERATION",
    "WSD_PORT_TYPE",
    "WSD_PROBE",
    "WSD_PROBE_MATCH",
    "WSD_PROBE_MATCHES",
    "WSD_PROBE_MATCH_LIST",
    "WSD_PROTOCOL_TYPE",
    "WSD_PT_ALL",
    "WSD_PT_HTTP",
    "WSD_PT_HTTPS",
    "WSD_PT_NONE",
    "WSD_PT_UDP",
    "WSD_REFERENCE_PARAMETERS",
    "WSD_REFERENCE_PROPERTIES",
    "WSD_RELATIONSHIP_METADATA",
    "WSD_RESOLVE",
    "WSD_RESOLVE_MATCH",
    "WSD_RESOLVE_MATCHES",
    "WSD_SCOPES",
    "WSD_SECURITY_CERT_VALIDATION",
    "WSD_SECURITY_CERT_VALIDATION_V1",
    "WSD_SECURITY_COMPACTSIG_SIGNING_CERT",
    "WSD_SECURITY_COMPACTSIG_VALIDATION",
    "WSD_SECURITY_HTTP_AUTH_SCHEME_NEGOTIATE",
    "WSD_SECURITY_HTTP_AUTH_SCHEME_NTLM",
    "WSD_SECURITY_REQUIRE_CLIENT_CERT_OR_HTTP_CLIENT_AUTH",
    "WSD_SECURITY_REQUIRE_HTTP_CLIENT_AUTH",
    "WSD_SECURITY_SIGNATURE_VALIDATION",
    "WSD_SECURITY_SSL_CERT_FOR_CLIENT_AUTH",
    "WSD_SECURITY_SSL_CLIENT_CERT_VALIDATION",
    "WSD_SECURITY_SSL_NEGOTIATE_CLIENT_CERT",
    "WSD_SECURITY_SSL_SERVER_CERT_VALIDATION",
    "WSD_SECURITY_USE_HTTP_CLIENT_AUTH",
    "WSD_SERVICE_METADATA",
    "WSD_SERVICE_METADATA_LIST",
    "WSD_SOAP_FAULT",
    "WSD_SOAP_FAULT_CODE",
    "WSD_SOAP_FAULT_REASON",
    "WSD_SOAP_FAULT_SUBCODE",
    "WSD_SOAP_HEADER",
    "WSD_SOAP_MESSAGE",
    "WSD_STUB_FUNCTION",
    "WSD_SYNCHRONOUS_RESPONSE_CONTEXT",
    "WSD_THIS_DEVICE_METADATA",
    "WSD_THIS_MODEL_METADATA",
    "WSD_UNKNOWN_LOOKUP",
    "WSD_URI_LIST",
]
_arch_optional = [
]
