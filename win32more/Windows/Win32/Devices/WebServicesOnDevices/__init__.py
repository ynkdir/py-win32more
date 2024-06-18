from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Devices.WebServicesOnDevices
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Networking.WinSock
import win32more.Windows.Win32.Security.Cryptography
import win32more.Windows.Win32.System.Com
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
def WSDCreateUdpMessageParameters(ppTxParams: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDUdpMessageParameters)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateUdpAddress(ppAddress: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDUdpAddress)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateHttpMessageParameters(ppTxParams: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDHttpMessageParameters)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateHttpAddress(ppAddress: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDHttpAddress)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateOutboundAttachment(ppAttachment: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDOutboundAttachment)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDXMLGetNameFromBuiltinNamespace(pszNamespace: win32more.Windows.Win32.Foundation.PWSTR, pszName: win32more.Windows.Win32.Foundation.PWSTR, ppName: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDXMLCreateContext(ppContext: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDiscoveryProvider(pContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext, ppProvider: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryProvider)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDiscoveryProvider2(pContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext, pConfigParams: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM), dwConfigParamCount: UInt32, ppProvider: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryProvider)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDiscoveryPublisher(pContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext, ppPublisher: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryPublisher)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDiscoveryPublisher2(pContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext, pConfigParams: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM), dwConfigParamCount: UInt32, ppPublisher: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryPublisher)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDeviceProxy(pszDeviceId: win32more.Windows.Win32.Foundation.PWSTR, pszLocalId: win32more.Windows.Win32.Foundation.PWSTR, pContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext, ppDeviceProxy: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceProxy)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDeviceProxyAdvanced(pszDeviceId: win32more.Windows.Win32.Foundation.PWSTR, pDeviceAddress: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress, pszLocalId: win32more.Windows.Win32.Foundation.PWSTR, pContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext, ppDeviceProxy: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceProxy)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDeviceProxy2(pszDeviceId: win32more.Windows.Win32.Foundation.PWSTR, pszLocalId: win32more.Windows.Win32.Foundation.PWSTR, pContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext, pConfigParams: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM), dwConfigParamCount: UInt32, ppDeviceProxy: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceProxy)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDeviceHost(pszLocalId: win32more.Windows.Win32.Foundation.PWSTR, pContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext, ppDeviceHost: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceHost)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDeviceHostAdvanced(pszLocalId: win32more.Windows.Win32.Foundation.PWSTR, pContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext, ppHostAddresses: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress), dwHostAddressCount: UInt32, ppDeviceHost: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceHost)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDCreateDeviceHost2(pszLocalId: win32more.Windows.Win32.Foundation.PWSTR, pContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext, pConfigParams: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM), dwConfigParamCount: UInt32, ppDeviceHost: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceHost)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
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
def WSDXMLBuildAnyForSingleElement(pElementName: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME), pszText: win32more.Windows.Win32.Foundation.PWSTR, ppAny: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDXMLGetValueFromAny(pszNamespace: win32more.Windows.Win32.Foundation.PWSTR, pszName: win32more.Windows.Win32.Foundation.PWSTR, pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT), ppszValue: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDXMLAddSibling(pFirst: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT), pSecond: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDXMLAddChild(pParent: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT), pChild: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDXMLCleanupElement(pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDGenerateFault(pszCode: win32more.Windows.Win32.Foundation.PWSTR, pszSubCode: win32more.Windows.Win32.Foundation.PWSTR, pszReason: win32more.Windows.Win32.Foundation.PWSTR, pszDetail: win32more.Windows.Win32.Foundation.PWSTR, pContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext, ppFault: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDGenerateFaultEx(pCode: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME), pSubCode: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME), pReasons: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST), pszDetail: win32more.Windows.Win32.Foundation.PWSTR, ppFault: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDUriEncode(source: win32more.Windows.Win32.Foundation.PWSTR, cchSource: UInt32, destOut: POINTER(win32more.Windows.Win32.Foundation.PWSTR), cchDestOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wsdapi.dll')
def WSDUriDecode(source: win32more.Windows.Win32.Foundation.PWSTR, cchSource: UInt32, destOut: POINTER(win32more.Windows.Win32.Foundation.PWSTR), cchDestOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
DeviceDiscoveryMechanism = Int32
MulticastDiscovery: win32more.Windows.Win32.Devices.WebServicesOnDevices.DeviceDiscoveryMechanism = 0
DirectedDiscovery: win32more.Windows.Win32.Devices.WebServicesOnDevices.DeviceDiscoveryMechanism = 1
SecureDirectedDiscovery: win32more.Windows.Win32.Devices.WebServicesOnDevices.DeviceDiscoveryMechanism = 2
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
    def AsyncOperationComplete(self, pAsyncResult: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult, pAsyncState: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDAsyncResult(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{11a9852a-8dd8-423e-b537-9356db4fbfb8}')
    @commethod(3)
    def SetCallback(self, pCallback: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncCallback, pAsyncState: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetWaitHandle(self, hWaitHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def HasCompleted(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAsyncState(self, ppAsyncState: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Abort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetEvent(self, pEvent: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetEndpointProxy(self, ppEndpoint: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDEndpointProxy)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDAttachment(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5d55a616-9df8-4b09-b156-9ba351a48b76}')
class IWSDDeviceHost(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{917fe891-3d13-4138-9809-934c8abeb12c}')
    @commethod(3)
    def Init(self, pszLocalId: win32more.Windows.Win32.Foundation.PWSTR, pContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext, ppHostAddresses: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress), dwHostAddressCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Start(self, ullInstanceId: UInt64, pScopeList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST), pNotificationSink: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceHostNotify) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Stop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Terminate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RegisterPortType(self, pPortType: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_PORT_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetMetadata(self, pThisModelMetadata: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_THIS_MODEL_METADATA), pThisDeviceMetadata: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_THIS_DEVICE_METADATA), pHostMetadata: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_HOST_METADATA), pCustomMetadata: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RegisterService(self, pszServiceId: win32more.Windows.Win32.Foundation.PWSTR, pService: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RetireService(self, pszServiceId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AddDynamicService(self, pszServiceId: win32more.Windows.Win32.Foundation.PWSTR, pszEndpointAddress: win32more.Windows.Win32.Foundation.PWSTR, pPortType: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_PORT_TYPE), pPortName: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME), pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT), pService: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RemoveDynamicService(self, pszServiceId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetServiceDiscoverable(self, pszServiceId: win32more.Windows.Win32.Foundation.PWSTR, fDiscoverable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SignalEvent(self, pszServiceId: win32more.Windows.Win32.Foundation.PWSTR, pBody: VoidPtr, pOperation: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDDeviceHostNotify(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b5bee9f9-eeda-41fe-96f7-f45e14990fb0}')
    @commethod(3)
    def GetService(self, pszServiceId: win32more.Windows.Win32.Foundation.PWSTR, ppService: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDDeviceProxy(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{eee0c031-c578-4c0e-9a3b-973c35f409db}')
    @commethod(3)
    def Init(self, pszDeviceId: win32more.Windows.Win32.Foundation.PWSTR, pDeviceAddress: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress, pszLocalId: win32more.Windows.Win32.Foundation.PWSTR, pContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext, pSponsor: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDDeviceProxy) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginGetMetadata(self, ppResult: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EndGetMetadata(self, pResult: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetHostMetadata(self, ppHostMetadata: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_HOST_METADATA))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetThisModelMetadata(self, ppManufacturerMetadata: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_THIS_MODEL_METADATA))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetThisDeviceMetadata(self, ppThisDeviceMetadata: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_THIS_DEVICE_METADATA))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAllMetadata(self, ppMetadata: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetServiceProxyById(self, pszServiceId: win32more.Windows.Win32.Foundation.PWSTR, ppServiceProxy: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDServiceProxy)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetServiceProxyByType(self, pType: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME), ppServiceProxy: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDServiceProxy)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetEndpointProxy(self, ppProxy: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDEndpointProxy)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDEndpointProxy(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1860d430-b24c-4975-9f90-dbb39baa24ec}')
    @commethod(3)
    def SendOneWayRequest(self, pBody: VoidPtr, pOperation: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SendTwoWayRequest(self, pBody: VoidPtr, pOperation: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION), pResponseContext: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SYNCHRONOUS_RESPONSE_CONTEXT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SendTwoWayRequestAsync(self, pBody: VoidPtr, pOperation: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION), pAsyncState: win32more.Windows.Win32.System.Com.IUnknown, pCallback: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncCallback, pResult: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AbortAsyncOperation(self, pAsyncResult: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ProcessFault(self, pFault: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetErrorInfo(self, ppszErrorInfo: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFaultInfo(self, ppFault: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
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
    def SetContext(self, pContext: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetContext(self, ppContext: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
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
    def GetLocalAddress(self, ppAddress: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetLocalAddress(self, pAddress: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRemoteAddress(self, ppAddress: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetRemoteAddress(self, pAddress: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetLowerParameters(self, ppTxParams: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDMetadataExchange(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{06996d57-1d67-4928-9307-3d7833fdb846}')
    @commethod(3)
    def GetMetadata(self, MetadataOut: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
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
    def GetClientCertificate(self, ppCertContext: POINTER(POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
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
    def SendResponse(self, pBody: VoidPtr, pOperation: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION), pMessageParameters: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FaultRequest(self, pRequestHeader: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_HEADER), pMessageParameters: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters, pFault: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDServiceProxy(ComPtr):
    extends: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDMetadataExchange
    _iid_ = Guid('{d4c7fb9c-03ab-4175-9d67-094fafebf487}')
    @commethod(4)
    def BeginGetMetadata(self, ppResult: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EndGetMetadata(self, pResult: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult, ppMetadata: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetServiceMetadata(self, ppServiceMetadata: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SERVICE_METADATA))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SubscribeToOperation(self, pOperation: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION), pUnknown: win32more.Windows.Win32.System.Com.IUnknown, pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT), ppAny: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UnsubscribeToOperation(self, pOperation: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetEventingStatusCallback(self, pStatus: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDEventingStatus) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetEndpointProxy(self, ppProxy: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDEndpointProxy)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDServiceProxyEventing(ComPtr):
    extends: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDServiceProxy
    _iid_ = Guid('{f9279d6d-1012-4a94-b8cc-fd35d2202bfe}')
    @commethod(11)
    def SubscribeToMultipleOperations(self, pOperations: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION), dwOperationCount: UInt32, pUnknown: win32more.Windows.Win32.System.Com.IUnknown, pExpires: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES), pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT), ppExpires: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES)), ppAny: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def BeginSubscribeToMultipleOperations(self, pOperations: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION), dwOperationCount: UInt32, pUnknown: win32more.Windows.Win32.System.Com.IUnknown, pExpires: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES), pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT), pAsyncState: win32more.Windows.Win32.System.Com.IUnknown, pAsyncCallback: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncCallback, ppResult: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def EndSubscribeToMultipleOperations(self, pOperations: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION), dwOperationCount: UInt32, pResult: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult, ppExpires: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES)), ppAny: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def UnsubscribeToMultipleOperations(self, pOperations: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION), dwOperationCount: UInt32, pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def BeginUnsubscribeToMultipleOperations(self, pOperations: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION), dwOperationCount: UInt32, pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT), pAsyncState: win32more.Windows.Win32.System.Com.IUnknown, pAsyncCallback: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncCallback, ppResult: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def EndUnsubscribeToMultipleOperations(self, pOperations: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION), dwOperationCount: UInt32, pResult: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def RenewMultipleOperations(self, pOperations: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION), dwOperationCount: UInt32, pExpires: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES), pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT), ppExpires: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES)), ppAny: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def BeginRenewMultipleOperations(self, pOperations: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION), dwOperationCount: UInt32, pExpires: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES), pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT), pAsyncState: win32more.Windows.Win32.System.Com.IUnknown, pAsyncCallback: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncCallback, ppResult: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def EndRenewMultipleOperations(self, pOperations: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION), dwOperationCount: UInt32, pResult: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult, ppExpires: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES)), ppAny: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetStatusForMultipleOperations(self, pOperations: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION), dwOperationCount: UInt32, pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT), ppExpires: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES)), ppAny: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def BeginGetStatusForMultipleOperations(self, pOperations: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION), dwOperationCount: UInt32, pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT), pAsyncState: win32more.Windows.Win32.System.Com.IUnknown, pAsyncCallback: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncCallback, ppResult: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def EndGetStatusForMultipleOperations(self, pOperations: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION), dwOperationCount: UInt32, pResult: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAsyncResult, ppExpires: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES)), ppAny: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
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
    def SetSockaddr(self, pSockAddr: POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKADDR_STORAGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetSockaddr(self, pSockAddr: POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKADDR_STORAGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
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
    def SetRetransmitParams(self, pParams: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDUdpRetransmitParams)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRetransmitParams(self, pParams: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDUdpRetransmitParams)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDXMLContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{75d8f3ee-3e5a-43b4-a15a-bcf6887460c0}')
    @commethod(3)
    def AddNamespace(self, pszUri: win32more.Windows.Win32.Foundation.PWSTR, pszSuggestedPrefix: win32more.Windows.Win32.Foundation.PWSTR, ppNamespace: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAMESPACE))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddNameToNamespace(self, pszUri: win32more.Windows.Win32.Foundation.PWSTR, pszName: win32more.Windows.Win32.Foundation.PWSTR, ppName: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetNamespaces(self, pNamespaces: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAMESPACE)), wNamespacesCount: UInt16, bLayerNumber: Byte) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetTypes(self, pTypes: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_TYPE)), dwTypesCount: UInt32, bLayerNumber: Byte) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDiscoveredService(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4bad8a3b-b374-4420-9632-aac945b374aa}')
    @commethod(3)
    def GetEndpointReference(self, ppEndpointReference: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTypes(self, ppTypesList: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetScopes(self, ppScopesList: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetXAddrs(self, ppXAddrsList: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetMetadataVersion(self, pullMetadataVersion: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetExtendedDiscoXML(self, ppHeaderAny: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)), ppBodyAny: POINTER(POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
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
    def Attach(self, pSink: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryProviderNotify) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Detach(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SearchById(self, pszId: win32more.Windows.Win32.Foundation.PWSTR, pszTag: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SearchByAddress(self, pszAddress: win32more.Windows.Win32.Foundation.PWSTR, pszTag: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SearchByType(self, pTypesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST), pScopesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST), pszMatchBy: win32more.Windows.Win32.Foundation.PWSTR, pszTag: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetXMLContext(self, ppContext: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDiscoveryProviderNotify(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{73ee3ced-b6e6-4329-a546-3e8ad46563d2}')
    @commethod(3)
    def Add(self, pService: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveredService) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Remove(self, pService: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveredService) -> win32more.Windows.Win32.Foundation.HRESULT: ...
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
    def RegisterNotificationSink(self, pSink: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryPublisherNotify) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def UnRegisterNotificationSink(self, pSink: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDiscoveryPublisherNotify) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Publish(self, pszId: win32more.Windows.Win32.Foundation.PWSTR, ullMetadataVersion: UInt64, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: win32more.Windows.Win32.Foundation.PWSTR, pTypesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST), pScopesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST), pXAddrsList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UnPublish(self, pszId: win32more.Windows.Win32.Foundation.PWSTR, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: win32more.Windows.Win32.Foundation.PWSTR, pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def MatchProbe(self, pProbeMessage: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE), pMessageParameters: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters, pszId: win32more.Windows.Win32.Foundation.PWSTR, ullMetadataVersion: UInt64, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: win32more.Windows.Win32.Foundation.PWSTR, pTypesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST), pScopesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST), pXAddrsList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def MatchResolve(self, pResolveMessage: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE), pMessageParameters: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters, pszId: win32more.Windows.Win32.Foundation.PWSTR, ullMetadataVersion: UInt64, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: win32more.Windows.Win32.Foundation.PWSTR, pTypesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST), pScopesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST), pXAddrsList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def PublishEx(self, pszId: win32more.Windows.Win32.Foundation.PWSTR, ullMetadataVersion: UInt64, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: win32more.Windows.Win32.Foundation.PWSTR, pTypesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST), pScopesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST), pXAddrsList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST), pHeaderAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT), pReferenceParameterAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT), pPolicyAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT), pEndpointReferenceAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT), pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def MatchProbeEx(self, pProbeMessage: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE), pMessageParameters: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters, pszId: win32more.Windows.Win32.Foundation.PWSTR, ullMetadataVersion: UInt64, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: win32more.Windows.Win32.Foundation.PWSTR, pTypesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST), pScopesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST), pXAddrsList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST), pHeaderAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT), pReferenceParameterAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT), pPolicyAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT), pEndpointReferenceAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT), pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def MatchResolveEx(self, pResolveMessage: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE), pMessageParameters: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters, pszId: win32more.Windows.Win32.Foundation.PWSTR, ullMetadataVersion: UInt64, ullInstanceId: UInt64, ullMessageNumber: UInt64, pszSessionId: win32more.Windows.Win32.Foundation.PWSTR, pTypesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST), pScopesList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST), pXAddrsList: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST), pHeaderAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT), pReferenceParameterAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT), pPolicyAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT), pEndpointReferenceAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT), pAny: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def RegisterScopeMatchingRule(self, pScopeMatchingRule: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDScopeMatchingRule) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def UnRegisterScopeMatchingRule(self, pScopeMatchingRule: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDScopeMatchingRule) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetXMLContext(self, ppContext: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDXMLContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWSDiscoveryPublisherNotify(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e67651b0-337a-4b3c-9758-733388568251}')
    @commethod(3)
    def ProbeHandler(self, pSoap: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE), pMessageParameters: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ResolveHandler(self, pSoap: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE), pMessageParameters: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PWSD_SOAP_MESSAGE_HANDLER(thisUnknown: win32more.Windows.Win32.System.Com.IUnknown, event: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class REQUESTBODY_GetStatus(Structure):
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
class REQUESTBODY_Renew(Structure):
    Expires: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES)
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
class REQUESTBODY_Subscribe(Structure):
    EndTo: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE)
    Delivery: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_DELIVERY_MODE)
    Expires: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES)
    Filter: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_FILTER)
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
class REQUESTBODY_Unsubscribe(Structure):
    any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
class RESPONSEBODY_GetMetadata(Structure):
    Metadata: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST)
class RESPONSEBODY_GetStatus(Structure):
    expires: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES)
    any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
class RESPONSEBODY_Renew(Structure):
    expires: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES)
    any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
class RESPONSEBODY_Subscribe(Structure):
    SubscriptionManager: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE)
    expires: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES)
    any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
class RESPONSEBODY_SubscriptionEnd(Structure):
    SubscriptionManager: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE)
    Status: win32more.Windows.Win32.Foundation.PWSTR
    Reason: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING)
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
WSDEventType = Int32
WSDET_NONE: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDEventType = 0
WSDET_INCOMING_MESSAGE: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDEventType = 1
WSDET_INCOMING_FAULT: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDEventType = 2
WSDET_TRANSMISSION_FAILURE: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDEventType = 3
WSDET_RESPONSE_TIMEOUT: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDEventType = 4
WSDUdpMessageType = Int32
ONE_WAY: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDUdpMessageType = 0
TWO_WAY: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDUdpMessageType = 1
class WSDUdpRetransmitParams(Structure):
    ulSendDelay: UInt32
    ulRepeat: UInt32
    ulRepeatMinDelay: UInt32
    ulRepeatMaxDelay: UInt32
    ulRepeatUpperDelay: UInt32
class WSDXML_ATTRIBUTE(Structure):
    Element: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
    Next: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ATTRIBUTE)
    Name: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME)
    Value: win32more.Windows.Win32.Foundation.PWSTR
class WSDXML_ELEMENT(Structure):
    Node: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NODE
    Name: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME)
    FirstAttribute: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ATTRIBUTE)
    FirstChild: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NODE)
    PrefixMappings: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_PREFIX_MAPPING)
class WSDXML_ELEMENT_LIST(Structure):
    Next: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT_LIST)
    Element: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
class WSDXML_NAME(Structure):
    Space: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAMESPACE)
    LocalName: win32more.Windows.Win32.Foundation.PWSTR
class WSDXML_NAMESPACE(Structure):
    Uri: win32more.Windows.Win32.Foundation.PWSTR
    PreferredPrefix: win32more.Windows.Win32.Foundation.PWSTR
    Names: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME)
    NamesCount: UInt16
    Encoding: UInt16
class WSDXML_NODE(Structure):
    ElementType = 0
    TextType = 1
    Type: Int32
    Parent: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
    Next: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NODE)
WSDXML_OP = Int32
OpNone: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 0
OpEndOfTable: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 1
OpBeginElement_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 2
OpBeginAnyElement: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 3
OpEndElement: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 4
OpElement_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 5
OpAnyElement: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 6
OpAnyElements: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 7
OpAnyText: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 8
OpAttribute_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 9
OpBeginChoice: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 10
OpEndChoice: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 11
OpBeginSequence: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 12
OpEndSequence: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 13
OpBeginAll: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 14
OpEndAll: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 15
OpAnything: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 16
OpAnyNumber: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 17
OpOneOrMore: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 18
OpOptional: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 19
OpFormatBool_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 20
OpFormatInt8_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 21
OpFormatInt16_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 22
OpFormatInt32_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 23
OpFormatInt64_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 24
OpFormatUInt8_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 25
OpFormatUInt16_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 26
OpFormatUInt32_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 27
OpFormatUInt64_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 28
OpFormatUnicodeString_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 29
OpFormatDom_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 30
OpFormatStruct_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 31
OpFormatUri_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 32
OpFormatUuidUri_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 33
OpFormatName_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 34
OpFormatListInsertTail_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 35
OpFormatType_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 36
OpFormatDynamicType_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 37
OpFormatLookupType_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 38
OpFormatDuration_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 39
OpFormatDateTime_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 40
OpFormatFloat_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 41
OpFormatDouble_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 42
OpProcess_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 43
OpQualifiedAttribute_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 44
OpFormatXMLDeclaration_: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 45
OpFormatMax: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_OP = 46
class WSDXML_PREFIX_MAPPING(Structure):
    Refs: UInt32
    Next: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_PREFIX_MAPPING)
    Space: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAMESPACE)
    Prefix: win32more.Windows.Win32.Foundation.PWSTR
class WSDXML_TEXT(Structure):
    Node: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NODE
    Text: win32more.Windows.Win32.Foundation.PWSTR
class WSDXML_TYPE(Structure):
    Uri: win32more.Windows.Win32.Foundation.PWSTR
    Table: POINTER(Byte)
class WSD_APP_SEQUENCE(Structure):
    InstanceId: UInt64
    SequenceId: win32more.Windows.Win32.Foundation.PWSTR
    MessageNumber: UInt64
class WSD_BYE(Structure):
    EndpointReference: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE)
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
class WSD_CONFIG_ADDRESSES(Structure):
    addresses: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDAddress)
    dwAddressCount: UInt32
class WSD_CONFIG_PARAM(Structure):
    configParamType: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_TYPE
    pConfigData: VoidPtr
    dwConfigDataSize: UInt32
WSD_CONFIG_PARAM_TYPE = Int32
WSD_CONFIG_MAX_INBOUND_MESSAGE_SIZE: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_TYPE = 1
WSD_CONFIG_MAX_OUTBOUND_MESSAGE_SIZE: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_TYPE = 2
WSD_SECURITY_SSL_CERT_FOR_CLIENT_AUTH: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_TYPE = 3
WSD_SECURITY_SSL_SERVER_CERT_VALIDATION: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_TYPE = 4
WSD_SECURITY_SSL_CLIENT_CERT_VALIDATION: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_TYPE = 5
WSD_SECURITY_SSL_NEGOTIATE_CLIENT_CERT: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_TYPE = 6
WSD_SECURITY_COMPACTSIG_SIGNING_CERT: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_TYPE = 7
WSD_SECURITY_COMPACTSIG_VALIDATION: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_TYPE = 8
WSD_CONFIG_HOSTING_ADDRESSES: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_TYPE = 9
WSD_CONFIG_DEVICE_ADDRESSES: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_TYPE = 10
WSD_SECURITY_REQUIRE_HTTP_CLIENT_AUTH: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_TYPE = 11
WSD_SECURITY_REQUIRE_CLIENT_CERT_OR_HTTP_CLIENT_AUTH: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_TYPE = 12
WSD_SECURITY_USE_HTTP_CLIENT_AUTH: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_TYPE = 13
class WSD_DATETIME(Structure):
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
class WSD_DURATION(Structure):
    isPositive: win32more.Windows.Win32.Foundation.BOOL
    year: UInt32
    month: UInt32
    day: UInt32
    hour: UInt32
    minute: UInt32
    second: UInt32
    millisecond: UInt32
class WSD_ENDPOINT_REFERENCE(Structure):
    Address: win32more.Windows.Win32.Foundation.PWSTR
    ReferenceProperties: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_REFERENCE_PROPERTIES
    ReferenceParameters: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_REFERENCE_PARAMETERS
    PortType: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME)
    ServiceName: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME)
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
class WSD_ENDPOINT_REFERENCE_LIST(Structure):
    Next: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_LIST)
    Element: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE)
class WSD_EVENT(Structure):
    Hr: win32more.Windows.Win32.Foundation.HRESULT
    EventType: UInt32
    DispatchTag: win32more.Windows.Win32.Foundation.PWSTR
    HandlerContext: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_HANDLER_CONTEXT
    Soap: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE)
    Operation: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION)
    MessageParameters: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters
class WSD_EVENTING_DELIVERY_MODE(Structure):
    Mode: win32more.Windows.Win32.Foundation.PWSTR
    Push: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_DELIVERY_MODE_PUSH)
    Data: VoidPtr
class WSD_EVENTING_DELIVERY_MODE_PUSH(Structure):
    NotifyTo: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE)
class WSD_EVENTING_EXPIRES(Structure):
    Duration: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_DURATION)
    DateTime: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_DATETIME)
class WSD_EVENTING_FILTER(Structure):
    Dialect: win32more.Windows.Win32.Foundation.PWSTR
    FilterAction: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENTING_FILTER_ACTION)
    Data: VoidPtr
class WSD_EVENTING_FILTER_ACTION(Structure):
    Actions: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST)
class WSD_HANDLER_CONTEXT(Structure):
    Handler: win32more.Windows.Win32.Devices.WebServicesOnDevices.PWSD_SOAP_MESSAGE_HANDLER
    PVoid: VoidPtr
    Unknown: win32more.Windows.Win32.System.Com.IUnknown
class WSD_HEADER_RELATESTO(Structure):
    RelationshipType: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME)
    MessageID: win32more.Windows.Win32.Foundation.PWSTR
class WSD_HELLO(Structure):
    EndpointReference: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE)
    Types: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST)
    Scopes: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SCOPES)
    XAddrs: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST)
    MetadataVersion: UInt64
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
class WSD_HOST_METADATA(Structure):
    Host: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SERVICE_METADATA)
    Hosted: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SERVICE_METADATA_LIST)
class WSD_LOCALIZED_STRING(Structure):
    lang: win32more.Windows.Win32.Foundation.PWSTR
    String: win32more.Windows.Win32.Foundation.PWSTR
class WSD_LOCALIZED_STRING_LIST(Structure):
    Next: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST)
    Element: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING)
class WSD_METADATA_SECTION(Structure):
    Dialect: win32more.Windows.Win32.Foundation.PWSTR
    Identifier: win32more.Windows.Win32.Foundation.PWSTR
    Data: VoidPtr
    MetadataReference: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE)
    Location: win32more.Windows.Win32.Foundation.PWSTR
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
class WSD_METADATA_SECTION_LIST(Structure):
    Next: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST)
    Element: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_METADATA_SECTION)
class WSD_NAME_LIST(Structure):
    Next: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST)
    Element: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME)
class WSD_OPERATION(Structure):
    RequestType: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_TYPE)
    ResponseType: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_TYPE)
    RequestStubFunction: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_STUB_FUNCTION
class WSD_PORT_TYPE(Structure):
    EncodedName: UInt32
    OperationCount: UInt32
    Operations: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_OPERATION)
    ProtocolType: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_PROTOCOL_TYPE
class WSD_PROBE(Structure):
    Types: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST)
    Scopes: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SCOPES)
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
class WSD_PROBE_MATCH(Structure):
    EndpointReference: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE)
    Types: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST)
    Scopes: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SCOPES)
    XAddrs: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST)
    MetadataVersion: UInt64
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
class WSD_PROBE_MATCHES(Structure):
    ProbeMatch: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_PROBE_MATCH_LIST)
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
class WSD_PROBE_MATCH_LIST(Structure):
    Next: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_PROBE_MATCH_LIST)
    Element: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_PROBE_MATCH)
WSD_PROTOCOL_TYPE = Int32
WSD_PT_NONE: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_PROTOCOL_TYPE = 0
WSD_PT_UDP: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_PROTOCOL_TYPE = 1
WSD_PT_HTTP: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_PROTOCOL_TYPE = 2
WSD_PT_HTTPS: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_PROTOCOL_TYPE = 4
WSD_PT_ALL: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_PROTOCOL_TYPE = 255
class WSD_REFERENCE_PARAMETERS(Structure):
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
class WSD_REFERENCE_PROPERTIES(Structure):
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
class WSD_RELATIONSHIP_METADATA(Structure):
    Type: win32more.Windows.Win32.Foundation.PWSTR
    Data: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_HOST_METADATA)
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
class WSD_RESOLVE(Structure):
    EndpointReference: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE)
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
class WSD_RESOLVE_MATCH(Structure):
    EndpointReference: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE)
    Types: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST)
    Scopes: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SCOPES)
    XAddrs: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST)
    MetadataVersion: UInt64
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
class WSD_RESOLVE_MATCHES(Structure):
    ResolveMatch: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_RESOLVE_MATCH)
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
class WSD_SCOPES(Structure):
    MatchBy: win32more.Windows.Win32.Foundation.PWSTR
    Scopes: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST)
class WSD_SECURITY_CERT_VALIDATION(Structure):
    certMatchArray: POINTER(POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT))
    dwCertMatchArrayCount: UInt32
    hCertMatchStore: win32more.Windows.Win32.Security.Cryptography.HCERTSTORE
    hCertIssuerStore: win32more.Windows.Win32.Security.Cryptography.HCERTSTORE
    dwCertCheckOptions: UInt32
    pszCNGHashAlgId: win32more.Windows.Win32.Foundation.PWSTR
    pbCertHash: POINTER(Byte)
    dwCertHashSize: UInt32
class WSD_SECURITY_CERT_VALIDATION_V1(Structure):
    certMatchArray: POINTER(POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT))
    dwCertMatchArrayCount: UInt32
    hCertMatchStore: win32more.Windows.Win32.Security.Cryptography.HCERTSTORE
    hCertIssuerStore: win32more.Windows.Win32.Security.Cryptography.HCERTSTORE
    dwCertCheckOptions: UInt32
class WSD_SECURITY_SIGNATURE_VALIDATION(Structure):
    signingCertArray: POINTER(POINTER(win32more.Windows.Win32.Security.Cryptography.CERT_CONTEXT))
    dwSigningCertArrayCount: UInt32
    hSigningCertStore: win32more.Windows.Win32.Security.Cryptography.HCERTSTORE
    dwFlags: UInt32
class WSD_SERVICE_METADATA(Structure):
    EndpointReference: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_LIST)
    Types: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_NAME_LIST)
    ServiceId: win32more.Windows.Win32.Foundation.PWSTR
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
class WSD_SERVICE_METADATA_LIST(Structure):
    Next: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SERVICE_METADATA_LIST)
    Element: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SERVICE_METADATA)
class WSD_SOAP_FAULT(Structure):
    Code: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_CODE)
    Reason: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_REASON)
    Node: win32more.Windows.Win32.Foundation.PWSTR
    Role: win32more.Windows.Win32.Foundation.PWSTR
    Detail: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
class WSD_SOAP_FAULT_CODE(Structure):
    Value: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME)
    Subcode: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_SUBCODE)
class WSD_SOAP_FAULT_REASON(Structure):
    Text: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST)
class WSD_SOAP_FAULT_SUBCODE(Structure):
    Value: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_NAME)
    Subcode: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_SUBCODE)
class WSD_SOAP_HEADER(Structure):
    To: win32more.Windows.Win32.Foundation.PWSTR
    Action: win32more.Windows.Win32.Foundation.PWSTR
    MessageID: win32more.Windows.Win32.Foundation.PWSTR
    RelatesTo: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_HEADER_RELATESTO
    ReplyTo: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE)
    From: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE)
    FaultTo: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE)
    AppSequence: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_APP_SEQUENCE)
    AnyHeaders: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
class WSD_SOAP_MESSAGE(Structure):
    Header: win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_SOAP_HEADER
    Body: VoidPtr
    BodyType: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_TYPE)
@winfunctype_pointer
def WSD_STUB_FUNCTION(server: win32more.Windows.Win32.System.Com.IUnknown, session: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDServiceMessaging, event: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_EVENT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class WSD_SYNCHRONOUS_RESPONSE_CONTEXT(Structure):
    hr: win32more.Windows.Win32.Foundation.HRESULT
    eventHandle: win32more.Windows.Win32.Foundation.HANDLE
    messageParameters: win32more.Windows.Win32.Devices.WebServicesOnDevices.IWSDMessageParameters
    results: VoidPtr
class WSD_THIS_DEVICE_METADATA(Structure):
    FriendlyName: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST)
    FirmwareVersion: win32more.Windows.Win32.Foundation.PWSTR
    SerialNumber: win32more.Windows.Win32.Foundation.PWSTR
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
class WSD_THIS_MODEL_METADATA(Structure):
    Manufacturer: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST)
    ManufacturerUrl: win32more.Windows.Win32.Foundation.PWSTR
    ModelName: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST)
    ModelNumber: win32more.Windows.Win32.Foundation.PWSTR
    ModelUrl: win32more.Windows.Win32.Foundation.PWSTR
    PresentationUrl: win32more.Windows.Win32.Foundation.PWSTR
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
class WSD_UNKNOWN_LOOKUP(Structure):
    Any: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSDXML_ELEMENT)
class WSD_URI_LIST(Structure):
    Next: POINTER(win32more.Windows.Win32.Devices.WebServicesOnDevices.WSD_URI_LIST)
    Element: win32more.Windows.Win32.Foundation.PWSTR


make_ready(__name__)
