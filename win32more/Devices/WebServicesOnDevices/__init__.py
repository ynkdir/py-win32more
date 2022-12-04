from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Devices.WebServicesOnDevices
import win32more.Foundation
import win32more.Networking.WinSock
import win32more.Security.Cryptography
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
WSD_DEFAULT_HOSTING_ADDRESS = 'http://*:5357/'
WSD_DEFAULT_SECURE_HOSTING_ADDRESS = 'https://*:5358/'
WSD_DEFAULT_EVENTING_ADDRESS = 'http://*:5357/'
WSDAPI_OPTION_MAX_INBOUND_MESSAGE_SIZE = 1
WSDAPI_OPTION_TRACE_XML_TO_DEBUGGER = 2
WSDAPI_OPTION_TRACE_XML_TO_FILE = 3
WSDAPI_SSL_CERT_APPLY_DEFAULT_CHECKS = 0
WSDAPI_SSL_CERT_IGNORE_REVOCATION = 1
WSDAPI_SSL_CERT_IGNORE_EXPIRY = 2
WSDAPI_SSL_CERT_IGNORE_WRONG_USAGE = 4
WSDAPI_SSL_CERT_IGNORE_UNKNOWN_CA = 8
WSDAPI_SSL_CERT_IGNORE_INVALID_CN = 16
WSDAPI_COMPACTSIG_ACCEPT_ALL_MESSAGES = 1
WSD_SECURITY_HTTP_AUTH_SCHEME_NEGOTIATE = 1
WSD_SECURITY_HTTP_AUTH_SCHEME_NTLM = 2
WSDAPI_ADDRESSFAMILY_IPV4 = 1
WSDAPI_ADDRESSFAMILY_IPV6 = 2
def _define_WSDCreateUdpMessageParameters():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.IWSDUdpMessageParameters_head))(('WSDCreateUdpMessageParameters', windll['wsdapi.dll']), ((1, 'ppTxParams'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDCreateUdpAddress():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.IWSDUdpAddress_head))(('WSDCreateUdpAddress', windll['wsdapi.dll']), ((1, 'ppAddress'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDCreateHttpMessageParameters():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.IWSDHttpMessageParameters_head))(('WSDCreateHttpMessageParameters', windll['wsdapi.dll']), ((1, 'ppTxParams'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDCreateHttpAddress():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.IWSDHttpAddress_head))(('WSDCreateHttpAddress', windll['wsdapi.dll']), ((1, 'ppAddress'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDCreateOutboundAttachment():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.IWSDOutboundAttachment_head))(('WSDCreateOutboundAttachment', windll['wsdapi.dll']), ((1, 'ppAttachment'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDXMLGetNameFromBuiltinNamespace():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_NAME_head)))(('WSDXMLGetNameFromBuiltinNamespace', windll['wsdapi.dll']), ((1, 'pszNamespace'),(1, 'pszName'),(1, 'ppName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDXMLCreateContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.IWSDXMLContext_head))(('WSDXMLCreateContext', windll['wsdapi.dll']), ((1, 'ppContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDCreateDiscoveryProvider():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.WebServicesOnDevices.IWSDXMLContext_head,POINTER(win32more.Devices.WebServicesOnDevices.IWSDiscoveryProvider_head))(('WSDCreateDiscoveryProvider', windll['wsdapi.dll']), ((1, 'pContext'),(1, 'ppProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDCreateDiscoveryProvider2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.WebServicesOnDevices.IWSDXMLContext_head,POINTER(win32more.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_head),UInt32,POINTER(win32more.Devices.WebServicesOnDevices.IWSDiscoveryProvider_head))(('WSDCreateDiscoveryProvider2', windll['wsdapi.dll']), ((1, 'pContext'),(1, 'pConfigParams'),(1, 'dwConfigParamCount'),(1, 'ppProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDCreateDiscoveryPublisher():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.WebServicesOnDevices.IWSDXMLContext_head,POINTER(win32more.Devices.WebServicesOnDevices.IWSDiscoveryPublisher_head))(('WSDCreateDiscoveryPublisher', windll['wsdapi.dll']), ((1, 'pContext'),(1, 'ppPublisher'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDCreateDiscoveryPublisher2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.WebServicesOnDevices.IWSDXMLContext_head,POINTER(win32more.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_head),UInt32,POINTER(win32more.Devices.WebServicesOnDevices.IWSDiscoveryPublisher_head))(('WSDCreateDiscoveryPublisher2', windll['wsdapi.dll']), ((1, 'pContext'),(1, 'pConfigParams'),(1, 'dwConfigParamCount'),(1, 'ppPublisher'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDCreateDeviceProxy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Devices.WebServicesOnDevices.IWSDXMLContext_head,POINTER(win32more.Devices.WebServicesOnDevices.IWSDDeviceProxy_head))(('WSDCreateDeviceProxy', windll['wsdapi.dll']), ((1, 'pszDeviceId'),(1, 'pszLocalId'),(1, 'pContext'),(1, 'ppDeviceProxy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDCreateDeviceProxyAdvanced():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.WebServicesOnDevices.IWSDAddress_head,win32more.Foundation.PWSTR,win32more.Devices.WebServicesOnDevices.IWSDXMLContext_head,POINTER(win32more.Devices.WebServicesOnDevices.IWSDDeviceProxy_head))(('WSDCreateDeviceProxyAdvanced', windll['wsdapi.dll']), ((1, 'pszDeviceId'),(1, 'pDeviceAddress'),(1, 'pszLocalId'),(1, 'pContext'),(1, 'ppDeviceProxy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDCreateDeviceProxy2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Devices.WebServicesOnDevices.IWSDXMLContext_head,POINTER(win32more.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_head),UInt32,POINTER(win32more.Devices.WebServicesOnDevices.IWSDDeviceProxy_head))(('WSDCreateDeviceProxy2', windll['wsdapi.dll']), ((1, 'pszDeviceId'),(1, 'pszLocalId'),(1, 'pContext'),(1, 'pConfigParams'),(1, 'dwConfigParamCount'),(1, 'ppDeviceProxy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDCreateDeviceHost():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.WebServicesOnDevices.IWSDXMLContext_head,POINTER(win32more.Devices.WebServicesOnDevices.IWSDDeviceHost_head))(('WSDCreateDeviceHost', windll['wsdapi.dll']), ((1, 'pszLocalId'),(1, 'pContext'),(1, 'ppDeviceHost'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDCreateDeviceHostAdvanced():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.WebServicesOnDevices.IWSDXMLContext_head,POINTER(win32more.Devices.WebServicesOnDevices.IWSDAddress_head),UInt32,POINTER(win32more.Devices.WebServicesOnDevices.IWSDDeviceHost_head))(('WSDCreateDeviceHostAdvanced', windll['wsdapi.dll']), ((1, 'pszLocalId'),(1, 'pContext'),(1, 'ppHostAddresses'),(1, 'dwHostAddressCount'),(1, 'ppDeviceHost'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDCreateDeviceHost2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.WebServicesOnDevices.IWSDXMLContext_head,POINTER(win32more.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_head),UInt32,POINTER(win32more.Devices.WebServicesOnDevices.IWSDDeviceHost_head))(('WSDCreateDeviceHost2', windll['wsdapi.dll']), ((1, 'pszLocalId'),(1, 'pContext'),(1, 'pConfigParams'),(1, 'dwConfigParamCount'),(1, 'ppDeviceHost'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDSetConfigurationOption():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,UInt32)(('WSDSetConfigurationOption', windll['wsdapi.dll']), ((1, 'dwOption'),(1, 'pVoid'),(1, 'cbInBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDGetConfigurationOption():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,UInt32)(('WSDGetConfigurationOption', windll['wsdapi.dll']), ((1, 'dwOption'),(1, 'pVoid'),(1, 'cbOutBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDAllocateLinkedMemory():
    try:
        return WINFUNCTYPE(c_void_p,c_void_p,UIntPtr)(('WSDAllocateLinkedMemory', windll['wsdapi.dll']), ((1, 'pParent'),(1, 'cbSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDFreeLinkedMemory():
    try:
        return WINFUNCTYPE(Void,c_void_p)(('WSDFreeLinkedMemory', windll['wsdapi.dll']), ((1, 'pVoid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDAttachLinkedMemory():
    try:
        return WINFUNCTYPE(Void,c_void_p,c_void_p)(('WSDAttachLinkedMemory', windll['wsdapi.dll']), ((1, 'pParent'),(1, 'pChild'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDDetachLinkedMemory():
    try:
        return WINFUNCTYPE(Void,c_void_p)(('WSDDetachLinkedMemory', windll['wsdapi.dll']), ((1, 'pVoid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDXMLBuildAnyForSingleElement():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_NAME_head),win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)))(('WSDXMLBuildAnyForSingleElement', windll['wsdapi.dll']), ((1, 'pElementName'),(1, 'pszText'),(1, 'ppAny'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDXMLGetValueFromAny():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head),POINTER(win32more.Foundation.PWSTR))(('WSDXMLGetValueFromAny', windll['wsdapi.dll']), ((1, 'pszNamespace'),(1, 'pszName'),(1, 'pAny'),(1, 'ppszValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDXMLAddSibling():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head),POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))(('WSDXMLAddSibling', windll['wsdapi.dll']), ((1, 'pFirst'),(1, 'pSecond'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDXMLAddChild():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head),POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))(('WSDXMLAddChild', windll['wsdapi.dll']), ((1, 'pParent'),(1, 'pChild'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDXMLCleanupElement():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))(('WSDXMLCleanupElement', windll['wsdapi.dll']), ((1, 'pAny'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDGenerateFault():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Devices.WebServicesOnDevices.IWSDXMLContext_head,POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_head)))(('WSDGenerateFault', windll['wsdapi.dll']), ((1, 'pszCode'),(1, 'pszSubCode'),(1, 'pszReason'),(1, 'pszDetail'),(1, 'pContext'),(1, 'ppFault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDGenerateFaultEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_NAME_head),POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_NAME_head),POINTER(win32more.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST_head),win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_head)))(('WSDGenerateFaultEx', windll['wsdapi.dll']), ((1, 'pCode'),(1, 'pSubCode'),(1, 'pReasons'),(1, 'pszDetail'),(1, 'ppFault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDUriEncode():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32))(('WSDUriEncode', windll['wsdapi.dll']), ((1, 'source'),(1, 'cchSource'),(1, 'destOut'),(1, 'cchDestOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WSDUriDecode():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32))(('WSDUriDecode', windll['wsdapi.dll']), ((1, 'source'),(1, 'cchSource'),(1, 'destOut'),(1, 'cchDestOut'),))
    except (FileNotFoundError, AttributeError):
        return None
DeviceDiscoveryMechanism = Int32
DeviceDiscoveryMechanism_MulticastDiscovery = 0
DeviceDiscoveryMechanism_DirectedDiscovery = 1
DeviceDiscoveryMechanism_SecureDirectedDiscovery = 2
def _define_IWSDAddress_head():
    class IWSDAddress(win32more.System.Com.IUnknown_head):
        Guid = Guid('b9574c6c-12a6-4f74-93-a1-33-18-ff-60-57-59')
    return IWSDAddress
def _define_IWSDAddress():
    IWSDAddress = win32more.Devices.WebServicesOnDevices.IWSDAddress_head
    IWSDAddress.Serialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.BOOL)(3, 'Serialize', ((1, 'pszBuffer'),(1, 'cchLength'),(1, 'fSafe'),)))
    IWSDAddress.Deserialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(4, 'Deserialize', ((1, 'pszBuffer'),)))
    win32more.System.Com.IUnknown
    return IWSDAddress
def _define_IWSDAsyncCallback_head():
    class IWSDAsyncCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('a63e109d-ce72-49e2-ba-98-e8-45-f5-ee-16-66')
    return IWSDAsyncCallback
def _define_IWSDAsyncCallback():
    IWSDAsyncCallback = win32more.Devices.WebServicesOnDevices.IWSDAsyncCallback_head
    IWSDAsyncCallback.AsyncOperationComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.WebServicesOnDevices.IWSDAsyncResult_head,win32more.System.Com.IUnknown_head)(3, 'AsyncOperationComplete', ((1, 'pAsyncResult'),(1, 'pAsyncState'),)))
    win32more.System.Com.IUnknown
    return IWSDAsyncCallback
def _define_IWSDAsyncResult_head():
    class IWSDAsyncResult(win32more.System.Com.IUnknown_head):
        Guid = Guid('11a9852a-8dd8-423e-b5-37-93-56-db-4f-bf-b8')
    return IWSDAsyncResult
def _define_IWSDAsyncResult():
    IWSDAsyncResult = win32more.Devices.WebServicesOnDevices.IWSDAsyncResult_head
    IWSDAsyncResult.SetCallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.WebServicesOnDevices.IWSDAsyncCallback_head,win32more.System.Com.IUnknown_head)(3, 'SetCallback', ((1, 'pCallback'),(1, 'pAsyncState'),)))
    IWSDAsyncResult.SetWaitHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE)(4, 'SetWaitHandle', ((1, 'hWaitHandle'),)))
    IWSDAsyncResult.HasCompleted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'HasCompleted', ()))
    IWSDAsyncResult.GetAsyncState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(6, 'GetAsyncState', ((1, 'ppAsyncState'),)))
    IWSDAsyncResult.Abort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'Abort', ()))
    IWSDAsyncResult.GetEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSD_EVENT_head))(8, 'GetEvent', ((1, 'pEvent'),)))
    IWSDAsyncResult.GetEndpointProxy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.IWSDEndpointProxy_head))(9, 'GetEndpointProxy', ((1, 'ppEndpoint'),)))
    win32more.System.Com.IUnknown
    return IWSDAsyncResult
def _define_IWSDAttachment_head():
    class IWSDAttachment(win32more.System.Com.IUnknown_head):
        Guid = Guid('5d55a616-9df8-4b09-b1-56-9b-a3-51-a4-8b-76')
    return IWSDAttachment
def _define_IWSDAttachment():
    IWSDAttachment = win32more.Devices.WebServicesOnDevices.IWSDAttachment_head
    win32more.System.Com.IUnknown
    return IWSDAttachment
def _define_IWSDDeviceHost_head():
    class IWSDDeviceHost(win32more.System.Com.IUnknown_head):
        Guid = Guid('917fe891-3d13-4138-98-09-93-4c-8a-be-b1-2c')
    return IWSDDeviceHost
def _define_IWSDDeviceHost():
    IWSDDeviceHost = win32more.Devices.WebServicesOnDevices.IWSDDeviceHost_head
    IWSDDeviceHost.Init = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.WebServicesOnDevices.IWSDXMLContext_head,POINTER(win32more.Devices.WebServicesOnDevices.IWSDAddress_head),UInt32)(3, 'Init', ((1, 'pszLocalId'),(1, 'pContext'),(1, 'ppHostAddresses'),(1, 'dwHostAddressCount'),)))
    IWSDDeviceHost.Start = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(win32more.Devices.WebServicesOnDevices.WSD_URI_LIST_head),win32more.Devices.WebServicesOnDevices.IWSDDeviceHostNotify_head)(4, 'Start', ((1, 'ullInstanceId'),(1, 'pScopeList'),(1, 'pNotificationSink'),)))
    IWSDDeviceHost.Stop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Stop', ()))
    IWSDDeviceHost.Terminate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'Terminate', ()))
    IWSDDeviceHost.RegisterPortType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSD_PORT_TYPE_head))(7, 'RegisterPortType', ((1, 'pPortType'),)))
    IWSDDeviceHost.SetMetadata = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSD_THIS_MODEL_METADATA_head),POINTER(win32more.Devices.WebServicesOnDevices.WSD_THIS_DEVICE_METADATA_head),POINTER(win32more.Devices.WebServicesOnDevices.WSD_HOST_METADATA_head),POINTER(win32more.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST_head))(8, 'SetMetadata', ((1, 'pThisModelMetadata'),(1, 'pThisDeviceMetadata'),(1, 'pHostMetadata'),(1, 'pCustomMetadata'),)))
    IWSDDeviceHost.RegisterService = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.IUnknown_head)(9, 'RegisterService', ((1, 'pszServiceId'),(1, 'pService'),)))
    IWSDDeviceHost.RetireService = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(10, 'RetireService', ((1, 'pszServiceId'),)))
    IWSDDeviceHost.AddDynamicService = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Devices.WebServicesOnDevices.WSD_PORT_TYPE_head),POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_NAME_head),POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head),win32more.System.Com.IUnknown_head)(11, 'AddDynamicService', ((1, 'pszServiceId'),(1, 'pszEndpointAddress'),(1, 'pPortType'),(1, 'pPortName'),(1, 'pAny'),(1, 'pService'),)))
    IWSDDeviceHost.RemoveDynamicService = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(12, 'RemoveDynamicService', ((1, 'pszServiceId'),)))
    IWSDDeviceHost.SetServiceDiscoverable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.BOOL)(13, 'SetServiceDiscoverable', ((1, 'pszServiceId'),(1, 'fDiscoverable'),)))
    IWSDDeviceHost.SignalEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,c_void_p,POINTER(win32more.Devices.WebServicesOnDevices.WSD_OPERATION_head))(14, 'SignalEvent', ((1, 'pszServiceId'),(1, 'pBody'),(1, 'pOperation'),)))
    win32more.System.Com.IUnknown
    return IWSDDeviceHost
def _define_IWSDDeviceHostNotify_head():
    class IWSDDeviceHostNotify(win32more.System.Com.IUnknown_head):
        Guid = Guid('b5bee9f9-eeda-41fe-96-f7-f4-5e-14-99-0f-b0')
    return IWSDDeviceHostNotify
def _define_IWSDDeviceHostNotify():
    IWSDDeviceHostNotify = win32more.Devices.WebServicesOnDevices.IWSDDeviceHostNotify_head
    IWSDDeviceHostNotify.GetService = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.IUnknown_head))(3, 'GetService', ((1, 'pszServiceId'),(1, 'ppService'),)))
    win32more.System.Com.IUnknown
    return IWSDDeviceHostNotify
def _define_IWSDDeviceProxy_head():
    class IWSDDeviceProxy(win32more.System.Com.IUnknown_head):
        Guid = Guid('eee0c031-c578-4c0e-9a-3b-97-3c-35-f4-09-db')
    return IWSDDeviceProxy
def _define_IWSDDeviceProxy():
    IWSDDeviceProxy = win32more.Devices.WebServicesOnDevices.IWSDDeviceProxy_head
    IWSDDeviceProxy.Init = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.WebServicesOnDevices.IWSDAddress_head,win32more.Foundation.PWSTR,win32more.Devices.WebServicesOnDevices.IWSDXMLContext_head,win32more.Devices.WebServicesOnDevices.IWSDDeviceProxy_head)(3, 'Init', ((1, 'pszDeviceId'),(1, 'pDeviceAddress'),(1, 'pszLocalId'),(1, 'pContext'),(1, 'pSponsor'),)))
    IWSDDeviceProxy.BeginGetMetadata = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.IWSDAsyncResult_head))(4, 'BeginGetMetadata', ((1, 'ppResult'),)))
    IWSDDeviceProxy.EndGetMetadata = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.WebServicesOnDevices.IWSDAsyncResult_head)(5, 'EndGetMetadata', ((1, 'pResult'),)))
    IWSDDeviceProxy.GetHostMetadata = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSD_HOST_METADATA_head)))(6, 'GetHostMetadata', ((1, 'ppHostMetadata'),)))
    IWSDDeviceProxy.GetThisModelMetadata = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSD_THIS_MODEL_METADATA_head)))(7, 'GetThisModelMetadata', ((1, 'ppManufacturerMetadata'),)))
    IWSDDeviceProxy.GetThisDeviceMetadata = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSD_THIS_DEVICE_METADATA_head)))(8, 'GetThisDeviceMetadata', ((1, 'ppThisDeviceMetadata'),)))
    IWSDDeviceProxy.GetAllMetadata = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST_head)))(9, 'GetAllMetadata', ((1, 'ppMetadata'),)))
    IWSDDeviceProxy.GetServiceProxyById = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Devices.WebServicesOnDevices.IWSDServiceProxy_head))(10, 'GetServiceProxyById', ((1, 'pszServiceId'),(1, 'ppServiceProxy'),)))
    IWSDDeviceProxy.GetServiceProxyByType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_NAME_head),POINTER(win32more.Devices.WebServicesOnDevices.IWSDServiceProxy_head))(11, 'GetServiceProxyByType', ((1, 'pType'),(1, 'ppServiceProxy'),)))
    IWSDDeviceProxy.GetEndpointProxy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.IWSDEndpointProxy_head))(12, 'GetEndpointProxy', ((1, 'ppProxy'),)))
    win32more.System.Com.IUnknown
    return IWSDDeviceProxy
def _define_IWSDEndpointProxy_head():
    class IWSDEndpointProxy(win32more.System.Com.IUnknown_head):
        Guid = Guid('1860d430-b24c-4975-9f-90-db-b3-9b-aa-24-ec')
    return IWSDEndpointProxy
def _define_IWSDEndpointProxy():
    IWSDEndpointProxy = win32more.Devices.WebServicesOnDevices.IWSDEndpointProxy_head
    IWSDEndpointProxy.SendOneWayRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Devices.WebServicesOnDevices.WSD_OPERATION_head))(3, 'SendOneWayRequest', ((1, 'pBody'),(1, 'pOperation'),)))
    IWSDEndpointProxy.SendTwoWayRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Devices.WebServicesOnDevices.WSD_OPERATION_head),POINTER(win32more.Devices.WebServicesOnDevices.WSD_SYNCHRONOUS_RESPONSE_CONTEXT_head))(4, 'SendTwoWayRequest', ((1, 'pBody'),(1, 'pOperation'),(1, 'pResponseContext'),)))
    IWSDEndpointProxy.SendTwoWayRequestAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Devices.WebServicesOnDevices.WSD_OPERATION_head),win32more.System.Com.IUnknown_head,win32more.Devices.WebServicesOnDevices.IWSDAsyncCallback_head,POINTER(win32more.Devices.WebServicesOnDevices.IWSDAsyncResult_head))(5, 'SendTwoWayRequestAsync', ((1, 'pBody'),(1, 'pOperation'),(1, 'pAsyncState'),(1, 'pCallback'),(1, 'pResult'),)))
    IWSDEndpointProxy.AbortAsyncOperation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.WebServicesOnDevices.IWSDAsyncResult_head)(6, 'AbortAsyncOperation', ((1, 'pAsyncResult'),)))
    IWSDEndpointProxy.ProcessFault = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_head))(7, 'ProcessFault', ((1, 'pFault'),)))
    IWSDEndpointProxy.GetErrorInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(8, 'GetErrorInfo', ((1, 'ppszErrorInfo'),)))
    IWSDEndpointProxy.GetFaultInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_head)))(9, 'GetFaultInfo', ((1, 'ppFault'),)))
    win32more.System.Com.IUnknown
    return IWSDEndpointProxy
def _define_IWSDEventingStatus_head():
    class IWSDEventingStatus(win32more.System.Com.IUnknown_head):
        Guid = Guid('49b17f52-637a-407a-ae-99-fb-e8-2a-4d-38-c0')
    return IWSDEventingStatus
def _define_IWSDEventingStatus():
    IWSDEventingStatus = win32more.Devices.WebServicesOnDevices.IWSDEventingStatus_head
    IWSDEventingStatus.SubscriptionRenewed = COMMETHOD(WINFUNCTYPE(Void,win32more.Foundation.PWSTR)(3, 'SubscriptionRenewed', ((1, 'pszSubscriptionAction'),)))
    IWSDEventingStatus.SubscriptionRenewalFailed = COMMETHOD(WINFUNCTYPE(Void,win32more.Foundation.PWSTR,win32more.Foundation.HRESULT)(4, 'SubscriptionRenewalFailed', ((1, 'pszSubscriptionAction'),(1, 'hr'),)))
    IWSDEventingStatus.SubscriptionEnded = COMMETHOD(WINFUNCTYPE(Void,win32more.Foundation.PWSTR)(5, 'SubscriptionEnded', ((1, 'pszSubscriptionAction'),)))
    win32more.System.Com.IUnknown
    return IWSDEventingStatus
def _define_IWSDHttpAddress_head():
    class IWSDHttpAddress(win32more.Devices.WebServicesOnDevices.IWSDTransportAddress_head):
        Guid = Guid('d09ac7bd-2a3e-4b85-86-05-27-37-ff-3e-4e-a0')
    return IWSDHttpAddress
def _define_IWSDHttpAddress():
    IWSDHttpAddress = win32more.Devices.WebServicesOnDevices.IWSDHttpAddress_head
    IWSDHttpAddress.GetSecure = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(10, 'GetSecure', ()))
    IWSDHttpAddress.SetSecure = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(11, 'SetSecure', ((1, 'fSecure'),)))
    IWSDHttpAddress.GetPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(12, 'GetPath', ((1, 'ppszPath'),)))
    IWSDHttpAddress.SetPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(13, 'SetPath', ((1, 'pszPath'),)))
    win32more.Devices.WebServicesOnDevices.IWSDTransportAddress
    return IWSDHttpAddress
def _define_IWSDHttpAuthParameters_head():
    class IWSDHttpAuthParameters(win32more.System.Com.IUnknown_head):
        Guid = Guid('0b476df0-8dac-480d-b0-5c-99-78-1a-58-84-aa')
    return IWSDHttpAuthParameters
def _define_IWSDHttpAuthParameters():
    IWSDHttpAuthParameters = win32more.Devices.WebServicesOnDevices.IWSDHttpAuthParameters_head
    IWSDHttpAuthParameters.GetClientAccessToken = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HANDLE))(3, 'GetClientAccessToken', ((1, 'phToken'),)))
    IWSDHttpAuthParameters.GetAuthType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(4, 'GetAuthType', ((1, 'pAuthType'),)))
    win32more.System.Com.IUnknown
    return IWSDHttpAuthParameters
def _define_IWSDHttpMessageParameters_head():
    class IWSDHttpMessageParameters(win32more.Devices.WebServicesOnDevices.IWSDMessageParameters_head):
        Guid = Guid('540bd122-5c83-4dec-b3-96-ea-62-a2-69-7f-df')
    return IWSDHttpMessageParameters
def _define_IWSDHttpMessageParameters():
    IWSDHttpMessageParameters = win32more.Devices.WebServicesOnDevices.IWSDHttpMessageParameters_head
    IWSDHttpMessageParameters.SetInboundHttpHeaders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(8, 'SetInboundHttpHeaders', ((1, 'pszHeaders'),)))
    IWSDHttpMessageParameters.GetInboundHttpHeaders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(9, 'GetInboundHttpHeaders', ((1, 'ppszHeaders'),)))
    IWSDHttpMessageParameters.SetOutboundHttpHeaders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(10, 'SetOutboundHttpHeaders', ((1, 'pszHeaders'),)))
    IWSDHttpMessageParameters.GetOutboundHttpHeaders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(11, 'GetOutboundHttpHeaders', ((1, 'ppszHeaders'),)))
    IWSDHttpMessageParameters.SetID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(12, 'SetID', ((1, 'pszId'),)))
    IWSDHttpMessageParameters.GetID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(13, 'GetID', ((1, 'ppszId'),)))
    IWSDHttpMessageParameters.SetContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(14, 'SetContext', ((1, 'pContext'),)))
    IWSDHttpMessageParameters.GetContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(15, 'GetContext', ((1, 'ppContext'),)))
    IWSDHttpMessageParameters.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(16, 'Clear', ()))
    win32more.Devices.WebServicesOnDevices.IWSDMessageParameters
    return IWSDHttpMessageParameters
def _define_IWSDInboundAttachment_head():
    class IWSDInboundAttachment(win32more.Devices.WebServicesOnDevices.IWSDAttachment_head):
        Guid = Guid('5bd6ca65-233c-4fb8-9f-7a-26-41-61-96-55-c9')
    return IWSDInboundAttachment
def _define_IWSDInboundAttachment():
    IWSDInboundAttachment = win32more.Devices.WebServicesOnDevices.IWSDInboundAttachment_head
    IWSDInboundAttachment.Read = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,POINTER(UInt32))(3, 'Read', ((1, 'pBuffer'),(1, 'dwBytesToRead'),(1, 'pdwNumberOfBytesRead'),)))
    IWSDInboundAttachment.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Close', ()))
    win32more.Devices.WebServicesOnDevices.IWSDAttachment
    return IWSDInboundAttachment
def _define_IWSDiscoveredService_head():
    class IWSDiscoveredService(win32more.System.Com.IUnknown_head):
        Guid = Guid('4bad8a3b-b374-4420-96-32-aa-c9-45-b3-74-aa')
    return IWSDiscoveredService
def _define_IWSDiscoveredService():
    IWSDiscoveredService = win32more.Devices.WebServicesOnDevices.IWSDiscoveredService_head
    IWSDiscoveredService.GetEndpointReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)))(3, 'GetEndpointReference', ((1, 'ppEndpointReference'),)))
    IWSDiscoveredService.GetTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSD_NAME_LIST_head)))(4, 'GetTypes', ((1, 'ppTypesList'),)))
    IWSDiscoveredService.GetScopes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSD_URI_LIST_head)))(5, 'GetScopes', ((1, 'ppScopesList'),)))
    IWSDiscoveredService.GetXAddrs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSD_URI_LIST_head)))(6, 'GetXAddrs', ((1, 'ppXAddrsList'),)))
    IWSDiscoveredService.GetMetadataVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64))(7, 'GetMetadataVersion', ((1, 'pullMetadataVersion'),)))
    IWSDiscoveredService.GetExtendedDiscoXML = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)))(8, 'GetExtendedDiscoXML', ((1, 'ppHeaderAny'),(1, 'ppBodyAny'),)))
    IWSDiscoveredService.GetProbeResolveTag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(9, 'GetProbeResolveTag', ((1, 'ppszTag'),)))
    IWSDiscoveredService.GetRemoteTransportAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(10, 'GetRemoteTransportAddress', ((1, 'ppszRemoteTransportAddress'),)))
    IWSDiscoveredService.GetLocalTransportAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(11, 'GetLocalTransportAddress', ((1, 'ppszLocalTransportAddress'),)))
    IWSDiscoveredService.GetLocalInterfaceGUID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(12, 'GetLocalInterfaceGUID', ((1, 'pGuid'),)))
    IWSDiscoveredService.GetInstanceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64))(13, 'GetInstanceId', ((1, 'pullInstanceId'),)))
    win32more.System.Com.IUnknown
    return IWSDiscoveredService
def _define_IWSDiscoveryProvider_head():
    class IWSDiscoveryProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('8ffc8e55-f0eb-480f-88-b7-b4-35-dd-28-1d-45')
    return IWSDiscoveryProvider
def _define_IWSDiscoveryProvider():
    IWSDiscoveryProvider = win32more.Devices.WebServicesOnDevices.IWSDiscoveryProvider_head
    IWSDiscoveryProvider.SetAddressFamily = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(3, 'SetAddressFamily', ((1, 'dwAddressFamily'),)))
    IWSDiscoveryProvider.Attach = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.WebServicesOnDevices.IWSDiscoveryProviderNotify_head)(4, 'Attach', ((1, 'pSink'),)))
    IWSDiscoveryProvider.Detach = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Detach', ()))
    IWSDiscoveryProvider.SearchById = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(6, 'SearchById', ((1, 'pszId'),(1, 'pszTag'),)))
    IWSDiscoveryProvider.SearchByAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(7, 'SearchByAddress', ((1, 'pszAddress'),(1, 'pszTag'),)))
    IWSDiscoveryProvider.SearchByType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSD_NAME_LIST_head),POINTER(win32more.Devices.WebServicesOnDevices.WSD_URI_LIST_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(8, 'SearchByType', ((1, 'pTypesList'),(1, 'pScopesList'),(1, 'pszMatchBy'),(1, 'pszTag'),)))
    IWSDiscoveryProvider.GetXMLContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.IWSDXMLContext_head))(9, 'GetXMLContext', ((1, 'ppContext'),)))
    win32more.System.Com.IUnknown
    return IWSDiscoveryProvider
def _define_IWSDiscoveryProviderNotify_head():
    class IWSDiscoveryProviderNotify(win32more.System.Com.IUnknown_head):
        Guid = Guid('73ee3ced-b6e6-4329-a5-46-3e-8a-d4-65-63-d2')
    return IWSDiscoveryProviderNotify
def _define_IWSDiscoveryProviderNotify():
    IWSDiscoveryProviderNotify = win32more.Devices.WebServicesOnDevices.IWSDiscoveryProviderNotify_head
    IWSDiscoveryProviderNotify.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.WebServicesOnDevices.IWSDiscoveredService_head)(3, 'Add', ((1, 'pService'),)))
    IWSDiscoveryProviderNotify.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.WebServicesOnDevices.IWSDiscoveredService_head)(4, 'Remove', ((1, 'pService'),)))
    IWSDiscoveryProviderNotify.SearchFailed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(5, 'SearchFailed', ((1, 'hr'),(1, 'pszTag'),)))
    IWSDiscoveryProviderNotify.SearchComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(6, 'SearchComplete', ((1, 'pszTag'),)))
    win32more.System.Com.IUnknown
    return IWSDiscoveryProviderNotify
def _define_IWSDiscoveryPublisher_head():
    class IWSDiscoveryPublisher(win32more.System.Com.IUnknown_head):
        Guid = Guid('ae01e1a8-3ff9-4148-81-16-05-7c-c6-16-fe-13')
    return IWSDiscoveryPublisher
def _define_IWSDiscoveryPublisher():
    IWSDiscoveryPublisher = win32more.Devices.WebServicesOnDevices.IWSDiscoveryPublisher_head
    IWSDiscoveryPublisher.SetAddressFamily = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(3, 'SetAddressFamily', ((1, 'dwAddressFamily'),)))
    IWSDiscoveryPublisher.RegisterNotificationSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.WebServicesOnDevices.IWSDiscoveryPublisherNotify_head)(4, 'RegisterNotificationSink', ((1, 'pSink'),)))
    IWSDiscoveryPublisher.UnRegisterNotificationSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.WebServicesOnDevices.IWSDiscoveryPublisherNotify_head)(5, 'UnRegisterNotificationSink', ((1, 'pSink'),)))
    IWSDiscoveryPublisher.Publish = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt64,UInt64,UInt64,win32more.Foundation.PWSTR,POINTER(win32more.Devices.WebServicesOnDevices.WSD_NAME_LIST_head),POINTER(win32more.Devices.WebServicesOnDevices.WSD_URI_LIST_head),POINTER(win32more.Devices.WebServicesOnDevices.WSD_URI_LIST_head))(6, 'Publish', ((1, 'pszId'),(1, 'ullMetadataVersion'),(1, 'ullInstanceId'),(1, 'ullMessageNumber'),(1, 'pszSessionId'),(1, 'pTypesList'),(1, 'pScopesList'),(1, 'pXAddrsList'),)))
    IWSDiscoveryPublisher.UnPublish = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt64,UInt64,win32more.Foundation.PWSTR,POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))(7, 'UnPublish', ((1, 'pszId'),(1, 'ullInstanceId'),(1, 'ullMessageNumber'),(1, 'pszSessionId'),(1, 'pAny'),)))
    IWSDiscoveryPublisher.MatchProbe = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head),win32more.Devices.WebServicesOnDevices.IWSDMessageParameters_head,win32more.Foundation.PWSTR,UInt64,UInt64,UInt64,win32more.Foundation.PWSTR,POINTER(win32more.Devices.WebServicesOnDevices.WSD_NAME_LIST_head),POINTER(win32more.Devices.WebServicesOnDevices.WSD_URI_LIST_head),POINTER(win32more.Devices.WebServicesOnDevices.WSD_URI_LIST_head))(8, 'MatchProbe', ((1, 'pProbeMessage'),(1, 'pMessageParameters'),(1, 'pszId'),(1, 'ullMetadataVersion'),(1, 'ullInstanceId'),(1, 'ullMessageNumber'),(1, 'pszSessionId'),(1, 'pTypesList'),(1, 'pScopesList'),(1, 'pXAddrsList'),)))
    IWSDiscoveryPublisher.MatchResolve = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head),win32more.Devices.WebServicesOnDevices.IWSDMessageParameters_head,win32more.Foundation.PWSTR,UInt64,UInt64,UInt64,win32more.Foundation.PWSTR,POINTER(win32more.Devices.WebServicesOnDevices.WSD_NAME_LIST_head),POINTER(win32more.Devices.WebServicesOnDevices.WSD_URI_LIST_head),POINTER(win32more.Devices.WebServicesOnDevices.WSD_URI_LIST_head))(9, 'MatchResolve', ((1, 'pResolveMessage'),(1, 'pMessageParameters'),(1, 'pszId'),(1, 'ullMetadataVersion'),(1, 'ullInstanceId'),(1, 'ullMessageNumber'),(1, 'pszSessionId'),(1, 'pTypesList'),(1, 'pScopesList'),(1, 'pXAddrsList'),)))
    IWSDiscoveryPublisher.PublishEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt64,UInt64,UInt64,win32more.Foundation.PWSTR,POINTER(win32more.Devices.WebServicesOnDevices.WSD_NAME_LIST_head),POINTER(win32more.Devices.WebServicesOnDevices.WSD_URI_LIST_head),POINTER(win32more.Devices.WebServicesOnDevices.WSD_URI_LIST_head),POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head),POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head),POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head),POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head),POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))(10, 'PublishEx', ((1, 'pszId'),(1, 'ullMetadataVersion'),(1, 'ullInstanceId'),(1, 'ullMessageNumber'),(1, 'pszSessionId'),(1, 'pTypesList'),(1, 'pScopesList'),(1, 'pXAddrsList'),(1, 'pHeaderAny'),(1, 'pReferenceParameterAny'),(1, 'pPolicyAny'),(1, 'pEndpointReferenceAny'),(1, 'pAny'),)))
    IWSDiscoveryPublisher.MatchProbeEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head),win32more.Devices.WebServicesOnDevices.IWSDMessageParameters_head,win32more.Foundation.PWSTR,UInt64,UInt64,UInt64,win32more.Foundation.PWSTR,POINTER(win32more.Devices.WebServicesOnDevices.WSD_NAME_LIST_head),POINTER(win32more.Devices.WebServicesOnDevices.WSD_URI_LIST_head),POINTER(win32more.Devices.WebServicesOnDevices.WSD_URI_LIST_head),POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head),POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head),POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head),POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head),POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))(11, 'MatchProbeEx', ((1, 'pProbeMessage'),(1, 'pMessageParameters'),(1, 'pszId'),(1, 'ullMetadataVersion'),(1, 'ullInstanceId'),(1, 'ullMessageNumber'),(1, 'pszSessionId'),(1, 'pTypesList'),(1, 'pScopesList'),(1, 'pXAddrsList'),(1, 'pHeaderAny'),(1, 'pReferenceParameterAny'),(1, 'pPolicyAny'),(1, 'pEndpointReferenceAny'),(1, 'pAny'),)))
    IWSDiscoveryPublisher.MatchResolveEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head),win32more.Devices.WebServicesOnDevices.IWSDMessageParameters_head,win32more.Foundation.PWSTR,UInt64,UInt64,UInt64,win32more.Foundation.PWSTR,POINTER(win32more.Devices.WebServicesOnDevices.WSD_NAME_LIST_head),POINTER(win32more.Devices.WebServicesOnDevices.WSD_URI_LIST_head),POINTER(win32more.Devices.WebServicesOnDevices.WSD_URI_LIST_head),POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head),POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head),POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head),POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head),POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))(12, 'MatchResolveEx', ((1, 'pResolveMessage'),(1, 'pMessageParameters'),(1, 'pszId'),(1, 'ullMetadataVersion'),(1, 'ullInstanceId'),(1, 'ullMessageNumber'),(1, 'pszSessionId'),(1, 'pTypesList'),(1, 'pScopesList'),(1, 'pXAddrsList'),(1, 'pHeaderAny'),(1, 'pReferenceParameterAny'),(1, 'pPolicyAny'),(1, 'pEndpointReferenceAny'),(1, 'pAny'),)))
    IWSDiscoveryPublisher.RegisterScopeMatchingRule = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.WebServicesOnDevices.IWSDScopeMatchingRule_head)(13, 'RegisterScopeMatchingRule', ((1, 'pScopeMatchingRule'),)))
    IWSDiscoveryPublisher.UnRegisterScopeMatchingRule = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.WebServicesOnDevices.IWSDScopeMatchingRule_head)(14, 'UnRegisterScopeMatchingRule', ((1, 'pScopeMatchingRule'),)))
    IWSDiscoveryPublisher.GetXMLContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.IWSDXMLContext_head))(15, 'GetXMLContext', ((1, 'ppContext'),)))
    win32more.System.Com.IUnknown
    return IWSDiscoveryPublisher
def _define_IWSDiscoveryPublisherNotify_head():
    class IWSDiscoveryPublisherNotify(win32more.System.Com.IUnknown_head):
        Guid = Guid('e67651b0-337a-4b3c-97-58-73-33-88-56-82-51')
    return IWSDiscoveryPublisherNotify
def _define_IWSDiscoveryPublisherNotify():
    IWSDiscoveryPublisherNotify = win32more.Devices.WebServicesOnDevices.IWSDiscoveryPublisherNotify_head
    IWSDiscoveryPublisherNotify.ProbeHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head),win32more.Devices.WebServicesOnDevices.IWSDMessageParameters_head)(3, 'ProbeHandler', ((1, 'pSoap'),(1, 'pMessageParameters'),)))
    IWSDiscoveryPublisherNotify.ResolveHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head),win32more.Devices.WebServicesOnDevices.IWSDMessageParameters_head)(4, 'ResolveHandler', ((1, 'pSoap'),(1, 'pMessageParameters'),)))
    win32more.System.Com.IUnknown
    return IWSDiscoveryPublisherNotify
def _define_IWSDMessageParameters_head():
    class IWSDMessageParameters(win32more.System.Com.IUnknown_head):
        Guid = Guid('1fafe8a2-e6fc-4b80-b6-cf-b7-d4-5c-41-6d-7c')
    return IWSDMessageParameters
def _define_IWSDMessageParameters():
    IWSDMessageParameters = win32more.Devices.WebServicesOnDevices.IWSDMessageParameters_head
    IWSDMessageParameters.GetLocalAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.IWSDAddress_head))(3, 'GetLocalAddress', ((1, 'ppAddress'),)))
    IWSDMessageParameters.SetLocalAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.WebServicesOnDevices.IWSDAddress_head)(4, 'SetLocalAddress', ((1, 'pAddress'),)))
    IWSDMessageParameters.GetRemoteAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.IWSDAddress_head))(5, 'GetRemoteAddress', ((1, 'ppAddress'),)))
    IWSDMessageParameters.SetRemoteAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.WebServicesOnDevices.IWSDAddress_head)(6, 'SetRemoteAddress', ((1, 'pAddress'),)))
    IWSDMessageParameters.GetLowerParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.IWSDMessageParameters_head))(7, 'GetLowerParameters', ((1, 'ppTxParams'),)))
    win32more.System.Com.IUnknown
    return IWSDMessageParameters
def _define_IWSDMetadataExchange_head():
    class IWSDMetadataExchange(win32more.System.Com.IUnknown_head):
        Guid = Guid('06996d57-1d67-4928-93-07-3d-78-33-fd-b8-46')
    return IWSDMetadataExchange
def _define_IWSDMetadataExchange():
    IWSDMetadataExchange = win32more.Devices.WebServicesOnDevices.IWSDMetadataExchange_head
    IWSDMetadataExchange.GetMetadata = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST_head)))(3, 'GetMetadata', ((1, 'MetadataOut'),)))
    win32more.System.Com.IUnknown
    return IWSDMetadataExchange
def _define_IWSDOutboundAttachment_head():
    class IWSDOutboundAttachment(win32more.Devices.WebServicesOnDevices.IWSDAttachment_head):
        Guid = Guid('aa302f8d-5a22-4ba5-b3-92-aa-84-86-f4-c1-5d')
    return IWSDOutboundAttachment
def _define_IWSDOutboundAttachment():
    IWSDOutboundAttachment = win32more.Devices.WebServicesOnDevices.IWSDOutboundAttachment_head
    IWSDOutboundAttachment.Write = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,POINTER(UInt32))(3, 'Write', ((1, 'pBuffer'),(1, 'dwBytesToWrite'),(1, 'pdwNumberOfBytesWritten'),)))
    IWSDOutboundAttachment.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Close', ()))
    IWSDOutboundAttachment.Abort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Abort', ()))
    win32more.Devices.WebServicesOnDevices.IWSDAttachment
    return IWSDOutboundAttachment
def _define_IWSDScopeMatchingRule_head():
    class IWSDScopeMatchingRule(win32more.System.Com.IUnknown_head):
        Guid = Guid('fcafe424-fef5-481a-bd-9f-33-ce-05-74-25-6f')
    return IWSDScopeMatchingRule
def _define_IWSDScopeMatchingRule():
    IWSDScopeMatchingRule = win32more.Devices.WebServicesOnDevices.IWSDScopeMatchingRule_head
    IWSDScopeMatchingRule.GetScopeRule = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(3, 'GetScopeRule', ((1, 'ppszScopeMatchingRule'),)))
    IWSDScopeMatchingRule.MatchScopes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BOOL))(4, 'MatchScopes', ((1, 'pszScope1'),(1, 'pszScope2'),(1, 'pfMatch'),)))
    win32more.System.Com.IUnknown
    return IWSDScopeMatchingRule
def _define_IWSDServiceMessaging_head():
    class IWSDServiceMessaging(win32more.System.Com.IUnknown_head):
        Guid = Guid('94974cf4-0cab-460d-a3-f6-7a-0a-d6-23-c0-e6')
    return IWSDServiceMessaging
def _define_IWSDServiceMessaging():
    IWSDServiceMessaging = win32more.Devices.WebServicesOnDevices.IWSDServiceMessaging_head
    IWSDServiceMessaging.SendResponse = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Devices.WebServicesOnDevices.WSD_OPERATION_head),win32more.Devices.WebServicesOnDevices.IWSDMessageParameters_head)(3, 'SendResponse', ((1, 'pBody'),(1, 'pOperation'),(1, 'pMessageParameters'),)))
    IWSDServiceMessaging.FaultRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSD_SOAP_HEADER_head),win32more.Devices.WebServicesOnDevices.IWSDMessageParameters_head,POINTER(win32more.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_head))(4, 'FaultRequest', ((1, 'pRequestHeader'),(1, 'pMessageParameters'),(1, 'pFault'),)))
    win32more.System.Com.IUnknown
    return IWSDServiceMessaging
def _define_IWSDServiceProxy_head():
    class IWSDServiceProxy(win32more.Devices.WebServicesOnDevices.IWSDMetadataExchange_head):
        Guid = Guid('d4c7fb9c-03ab-4175-9d-67-09-4f-af-eb-f4-87')
    return IWSDServiceProxy
def _define_IWSDServiceProxy():
    IWSDServiceProxy = win32more.Devices.WebServicesOnDevices.IWSDServiceProxy_head
    IWSDServiceProxy.BeginGetMetadata = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.IWSDAsyncResult_head))(4, 'BeginGetMetadata', ((1, 'ppResult'),)))
    IWSDServiceProxy.EndGetMetadata = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.WebServicesOnDevices.IWSDAsyncResult_head,POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST_head)))(5, 'EndGetMetadata', ((1, 'pResult'),(1, 'ppMetadata'),)))
    IWSDServiceProxy.GetServiceMetadata = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSD_SERVICE_METADATA_head)))(6, 'GetServiceMetadata', ((1, 'ppServiceMetadata'),)))
    IWSDServiceProxy.SubscribeToOperation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSD_OPERATION_head),win32more.System.Com.IUnknown_head,POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head),POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)))(7, 'SubscribeToOperation', ((1, 'pOperation'),(1, 'pUnknown'),(1, 'pAny'),(1, 'ppAny'),)))
    IWSDServiceProxy.UnsubscribeToOperation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSD_OPERATION_head))(8, 'UnsubscribeToOperation', ((1, 'pOperation'),)))
    IWSDServiceProxy.SetEventingStatusCallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.WebServicesOnDevices.IWSDEventingStatus_head)(9, 'SetEventingStatusCallback', ((1, 'pStatus'),)))
    IWSDServiceProxy.GetEndpointProxy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.IWSDEndpointProxy_head))(10, 'GetEndpointProxy', ((1, 'ppProxy'),)))
    win32more.Devices.WebServicesOnDevices.IWSDMetadataExchange
    return IWSDServiceProxy
def _define_IWSDServiceProxyEventing_head():
    class IWSDServiceProxyEventing(win32more.Devices.WebServicesOnDevices.IWSDServiceProxy_head):
        Guid = Guid('f9279d6d-1012-4a94-b8-cc-fd-35-d2-20-2b-fe')
    return IWSDServiceProxyEventing
def _define_IWSDServiceProxyEventing():
    IWSDServiceProxyEventing = win32more.Devices.WebServicesOnDevices.IWSDServiceProxyEventing_head
    IWSDServiceProxyEventing.SubscribeToMultipleOperations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSD_OPERATION_head),UInt32,win32more.System.Com.IUnknown_head,POINTER(win32more.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head),POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head),POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)),POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)))(11, 'SubscribeToMultipleOperations', ((1, 'pOperations'),(1, 'dwOperationCount'),(1, 'pUnknown'),(1, 'pExpires'),(1, 'pAny'),(1, 'ppExpires'),(1, 'ppAny'),)))
    IWSDServiceProxyEventing.BeginSubscribeToMultipleOperations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSD_OPERATION_head),UInt32,win32more.System.Com.IUnknown_head,POINTER(win32more.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head),POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head),win32more.System.Com.IUnknown_head,win32more.Devices.WebServicesOnDevices.IWSDAsyncCallback_head,POINTER(win32more.Devices.WebServicesOnDevices.IWSDAsyncResult_head))(12, 'BeginSubscribeToMultipleOperations', ((1, 'pOperations'),(1, 'dwOperationCount'),(1, 'pUnknown'),(1, 'pExpires'),(1, 'pAny'),(1, 'pAsyncState'),(1, 'pAsyncCallback'),(1, 'ppResult'),)))
    IWSDServiceProxyEventing.EndSubscribeToMultipleOperations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSD_OPERATION_head),UInt32,win32more.Devices.WebServicesOnDevices.IWSDAsyncResult_head,POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)),POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)))(13, 'EndSubscribeToMultipleOperations', ((1, 'pOperations'),(1, 'dwOperationCount'),(1, 'pResult'),(1, 'ppExpires'),(1, 'ppAny'),)))
    IWSDServiceProxyEventing.UnsubscribeToMultipleOperations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSD_OPERATION_head),UInt32,POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head))(14, 'UnsubscribeToMultipleOperations', ((1, 'pOperations'),(1, 'dwOperationCount'),(1, 'pAny'),)))
    IWSDServiceProxyEventing.BeginUnsubscribeToMultipleOperations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSD_OPERATION_head),UInt32,POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head),win32more.System.Com.IUnknown_head,win32more.Devices.WebServicesOnDevices.IWSDAsyncCallback_head,POINTER(win32more.Devices.WebServicesOnDevices.IWSDAsyncResult_head))(15, 'BeginUnsubscribeToMultipleOperations', ((1, 'pOperations'),(1, 'dwOperationCount'),(1, 'pAny'),(1, 'pAsyncState'),(1, 'pAsyncCallback'),(1, 'ppResult'),)))
    IWSDServiceProxyEventing.EndUnsubscribeToMultipleOperations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSD_OPERATION_head),UInt32,win32more.Devices.WebServicesOnDevices.IWSDAsyncResult_head)(16, 'EndUnsubscribeToMultipleOperations', ((1, 'pOperations'),(1, 'dwOperationCount'),(1, 'pResult'),)))
    IWSDServiceProxyEventing.RenewMultipleOperations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSD_OPERATION_head),UInt32,POINTER(win32more.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head),POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head),POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)),POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)))(17, 'RenewMultipleOperations', ((1, 'pOperations'),(1, 'dwOperationCount'),(1, 'pExpires'),(1, 'pAny'),(1, 'ppExpires'),(1, 'ppAny'),)))
    IWSDServiceProxyEventing.BeginRenewMultipleOperations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSD_OPERATION_head),UInt32,POINTER(win32more.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head),POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head),win32more.System.Com.IUnknown_head,win32more.Devices.WebServicesOnDevices.IWSDAsyncCallback_head,POINTER(win32more.Devices.WebServicesOnDevices.IWSDAsyncResult_head))(18, 'BeginRenewMultipleOperations', ((1, 'pOperations'),(1, 'dwOperationCount'),(1, 'pExpires'),(1, 'pAny'),(1, 'pAsyncState'),(1, 'pAsyncCallback'),(1, 'ppResult'),)))
    IWSDServiceProxyEventing.EndRenewMultipleOperations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSD_OPERATION_head),UInt32,win32more.Devices.WebServicesOnDevices.IWSDAsyncResult_head,POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)),POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)))(19, 'EndRenewMultipleOperations', ((1, 'pOperations'),(1, 'dwOperationCount'),(1, 'pResult'),(1, 'ppExpires'),(1, 'ppAny'),)))
    IWSDServiceProxyEventing.GetStatusForMultipleOperations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSD_OPERATION_head),UInt32,POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head),POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)),POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)))(20, 'GetStatusForMultipleOperations', ((1, 'pOperations'),(1, 'dwOperationCount'),(1, 'pAny'),(1, 'ppExpires'),(1, 'ppAny'),)))
    IWSDServiceProxyEventing.BeginGetStatusForMultipleOperations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSD_OPERATION_head),UInt32,POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head),win32more.System.Com.IUnknown_head,win32more.Devices.WebServicesOnDevices.IWSDAsyncCallback_head,POINTER(win32more.Devices.WebServicesOnDevices.IWSDAsyncResult_head))(21, 'BeginGetStatusForMultipleOperations', ((1, 'pOperations'),(1, 'dwOperationCount'),(1, 'pAny'),(1, 'pAsyncState'),(1, 'pAsyncCallback'),(1, 'ppResult'),)))
    IWSDServiceProxyEventing.EndGetStatusForMultipleOperations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSD_OPERATION_head),UInt32,win32more.Devices.WebServicesOnDevices.IWSDAsyncResult_head,POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)),POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)))(22, 'EndGetStatusForMultipleOperations', ((1, 'pOperations'),(1, 'dwOperationCount'),(1, 'pResult'),(1, 'ppExpires'),(1, 'ppAny'),)))
    win32more.Devices.WebServicesOnDevices.IWSDServiceProxy
    return IWSDServiceProxyEventing
def _define_IWSDSignatureProperty_head():
    class IWSDSignatureProperty(win32more.System.Com.IUnknown_head):
        Guid = Guid('03ce20aa-71c4-45e2-b3-2e-37-66-c6-1c-79-0f')
    return IWSDSignatureProperty
def _define_IWSDSignatureProperty():
    IWSDSignatureProperty = win32more.Devices.WebServicesOnDevices.IWSDSignatureProperty_head
    IWSDSignatureProperty.IsMessageSigned = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(3, 'IsMessageSigned', ((1, 'pbSigned'),)))
    IWSDSignatureProperty.IsMessageSignatureTrusted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(4, 'IsMessageSignatureTrusted', ((1, 'pbSignatureTrusted'),)))
    IWSDSignatureProperty.GetKeyInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32))(5, 'GetKeyInfo', ((1, 'pbKeyInfo'),(1, 'pdwKeyInfoSize'),)))
    IWSDSignatureProperty.GetSignature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32))(6, 'GetSignature', ((1, 'pbSignature'),(1, 'pdwSignatureSize'),)))
    IWSDSignatureProperty.GetSignedInfoHash = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32))(7, 'GetSignedInfoHash', ((1, 'pbSignedInfoHash'),(1, 'pdwHashSize'),)))
    win32more.System.Com.IUnknown
    return IWSDSignatureProperty
def _define_IWSDSSLClientCertificate_head():
    class IWSDSSLClientCertificate(win32more.System.Com.IUnknown_head):
        Guid = Guid('de105e87-a0da-418e-98-ad-27-b9-ee-d8-7b-dc')
    return IWSDSSLClientCertificate
def _define_IWSDSSLClientCertificate():
    IWSDSSLClientCertificate = win32more.Devices.WebServicesOnDevices.IWSDSSLClientCertificate_head
    IWSDSSLClientCertificate.GetClientCertificate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)))(3, 'GetClientCertificate', ((1, 'ppCertContext'),)))
    IWSDSSLClientCertificate.GetMappedAccessToken = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HANDLE))(4, 'GetMappedAccessToken', ((1, 'phToken'),)))
    win32more.System.Com.IUnknown
    return IWSDSSLClientCertificate
def _define_IWSDTransportAddress_head():
    class IWSDTransportAddress(win32more.Devices.WebServicesOnDevices.IWSDAddress_head):
        Guid = Guid('70d23498-4ee6-4340-a3-df-d8-45-d2-23-54-67')
    return IWSDTransportAddress
def _define_IWSDTransportAddress():
    IWSDTransportAddress = win32more.Devices.WebServicesOnDevices.IWSDTransportAddress_head
    IWSDTransportAddress.GetPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16))(5, 'GetPort', ((1, 'pwPort'),)))
    IWSDTransportAddress.SetPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16)(6, 'SetPort', ((1, 'wPort'),)))
    IWSDTransportAddress.GetTransportAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(7, 'GetTransportAddress', ((1, 'ppszAddress'),)))
    IWSDTransportAddress.GetTransportAddressEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,POINTER(win32more.Foundation.PWSTR))(8, 'GetTransportAddressEx', ((1, 'fSafe'),(1, 'ppszAddress'),)))
    IWSDTransportAddress.SetTransportAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(9, 'SetTransportAddress', ((1, 'pszAddress'),)))
    win32more.Devices.WebServicesOnDevices.IWSDAddress
    return IWSDTransportAddress
def _define_IWSDUdpAddress_head():
    class IWSDUdpAddress(win32more.Devices.WebServicesOnDevices.IWSDTransportAddress_head):
        Guid = Guid('74d6124a-a441-4f78-a1-eb-97-a8-d1-99-68-93')
    return IWSDUdpAddress
def _define_IWSDUdpAddress():
    IWSDUdpAddress = win32more.Devices.WebServicesOnDevices.IWSDUdpAddress_head
    IWSDUdpAddress.SetSockaddr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WinSock.SOCKADDR_STORAGE_head))(10, 'SetSockaddr', ((1, 'pSockAddr'),)))
    IWSDUdpAddress.GetSockaddr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WinSock.SOCKADDR_STORAGE_head))(11, 'GetSockaddr', ((1, 'pSockAddr'),)))
    IWSDUdpAddress.SetExclusive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(12, 'SetExclusive', ((1, 'fExclusive'),)))
    IWSDUdpAddress.GetExclusive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(13, 'GetExclusive', ()))
    IWSDUdpAddress.SetMessageType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.WebServicesOnDevices.WSDUdpMessageType)(14, 'SetMessageType', ((1, 'messageType'),)))
    IWSDUdpAddress.GetMessageType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSDUdpMessageType))(15, 'GetMessageType', ((1, 'pMessageType'),)))
    IWSDUdpAddress.SetTTL = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(16, 'SetTTL', ((1, 'dwTTL'),)))
    IWSDUdpAddress.GetTTL = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(17, 'GetTTL', ((1, 'pdwTTL'),)))
    IWSDUdpAddress.SetAlias = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(18, 'SetAlias', ((1, 'pAlias'),)))
    IWSDUdpAddress.GetAlias = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(19, 'GetAlias', ((1, 'pAlias'),)))
    win32more.Devices.WebServicesOnDevices.IWSDTransportAddress
    return IWSDUdpAddress
def _define_IWSDUdpMessageParameters_head():
    class IWSDUdpMessageParameters(win32more.Devices.WebServicesOnDevices.IWSDMessageParameters_head):
        Guid = Guid('9934149f-8f0c-447b-aa-0b-73-12-4b-0c-a7-f0')
    return IWSDUdpMessageParameters
def _define_IWSDUdpMessageParameters():
    IWSDUdpMessageParameters = win32more.Devices.WebServicesOnDevices.IWSDUdpMessageParameters_head
    IWSDUdpMessageParameters.SetRetransmitParams = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSDUdpRetransmitParams_head))(8, 'SetRetransmitParams', ((1, 'pParams'),)))
    IWSDUdpMessageParameters.GetRetransmitParams = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.WebServicesOnDevices.WSDUdpRetransmitParams_head))(9, 'GetRetransmitParams', ((1, 'pParams'),)))
    win32more.Devices.WebServicesOnDevices.IWSDMessageParameters
    return IWSDUdpMessageParameters
def _define_IWSDXMLContext_head():
    class IWSDXMLContext(win32more.System.Com.IUnknown_head):
        Guid = Guid('75d8f3ee-3e5a-43b4-a1-5a-bc-f6-88-74-60-c0')
    return IWSDXMLContext
def _define_IWSDXMLContext():
    IWSDXMLContext = win32more.Devices.WebServicesOnDevices.IWSDXMLContext_head
    IWSDXMLContext.AddNamespace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_NAMESPACE_head)))(3, 'AddNamespace', ((1, 'pszUri'),(1, 'pszSuggestedPrefix'),(1, 'ppNamespace'),)))
    IWSDXMLContext.AddNameToNamespace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_NAME_head)))(4, 'AddNameToNamespace', ((1, 'pszUri'),(1, 'pszName'),(1, 'ppName'),)))
    IWSDXMLContext.SetNamespaces = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_NAMESPACE_head)),UInt16,Byte)(5, 'SetNamespaces', ((1, 'pNamespaces'),(1, 'wNamespacesCount'),(1, 'bLayerNumber'),)))
    IWSDXMLContext.SetTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_TYPE_head)),UInt32,Byte)(6, 'SetTypes', ((1, 'pTypes'),(1, 'dwTypesCount'),(1, 'bLayerNumber'),)))
    win32more.System.Com.IUnknown
    return IWSDXMLContext
def _define_PWSD_SOAP_MESSAGE_HANDLER():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(win32more.Devices.WebServicesOnDevices.WSD_EVENT_head))
def _define_REQUESTBODY_GetStatus_head():
    class REQUESTBODY_GetStatus(Structure):
        pass
    return REQUESTBODY_GetStatus
def _define_REQUESTBODY_GetStatus():
    REQUESTBODY_GetStatus = win32more.Devices.WebServicesOnDevices.REQUESTBODY_GetStatus_head
    REQUESTBODY_GetStatus._fields_ = [
        ('Any', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return REQUESTBODY_GetStatus
def _define_REQUESTBODY_Renew_head():
    class REQUESTBODY_Renew(Structure):
        pass
    return REQUESTBODY_Renew
def _define_REQUESTBODY_Renew():
    REQUESTBODY_Renew = win32more.Devices.WebServicesOnDevices.REQUESTBODY_Renew_head
    REQUESTBODY_Renew._fields_ = [
        ('Expires', POINTER(win32more.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)),
        ('Any', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return REQUESTBODY_Renew
def _define_REQUESTBODY_Subscribe_head():
    class REQUESTBODY_Subscribe(Structure):
        pass
    return REQUESTBODY_Subscribe
def _define_REQUESTBODY_Subscribe():
    REQUESTBODY_Subscribe = win32more.Devices.WebServicesOnDevices.REQUESTBODY_Subscribe_head
    REQUESTBODY_Subscribe._fields_ = [
        ('EndTo', POINTER(win32more.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)),
        ('Delivery', POINTER(win32more.Devices.WebServicesOnDevices.WSD_EVENTING_DELIVERY_MODE_head)),
        ('Expires', POINTER(win32more.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)),
        ('Filter', POINTER(win32more.Devices.WebServicesOnDevices.WSD_EVENTING_FILTER_head)),
        ('Any', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return REQUESTBODY_Subscribe
def _define_REQUESTBODY_Unsubscribe_head():
    class REQUESTBODY_Unsubscribe(Structure):
        pass
    return REQUESTBODY_Unsubscribe
def _define_REQUESTBODY_Unsubscribe():
    REQUESTBODY_Unsubscribe = win32more.Devices.WebServicesOnDevices.REQUESTBODY_Unsubscribe_head
    REQUESTBODY_Unsubscribe._fields_ = [
        ('any', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return REQUESTBODY_Unsubscribe
def _define_RESPONSEBODY_GetMetadata_head():
    class RESPONSEBODY_GetMetadata(Structure):
        pass
    return RESPONSEBODY_GetMetadata
def _define_RESPONSEBODY_GetMetadata():
    RESPONSEBODY_GetMetadata = win32more.Devices.WebServicesOnDevices.RESPONSEBODY_GetMetadata_head
    RESPONSEBODY_GetMetadata._fields_ = [
        ('Metadata', POINTER(win32more.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST_head)),
    ]
    return RESPONSEBODY_GetMetadata
def _define_RESPONSEBODY_GetStatus_head():
    class RESPONSEBODY_GetStatus(Structure):
        pass
    return RESPONSEBODY_GetStatus
def _define_RESPONSEBODY_GetStatus():
    RESPONSEBODY_GetStatus = win32more.Devices.WebServicesOnDevices.RESPONSEBODY_GetStatus_head
    RESPONSEBODY_GetStatus._fields_ = [
        ('expires', POINTER(win32more.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)),
        ('any', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return RESPONSEBODY_GetStatus
def _define_RESPONSEBODY_Renew_head():
    class RESPONSEBODY_Renew(Structure):
        pass
    return RESPONSEBODY_Renew
def _define_RESPONSEBODY_Renew():
    RESPONSEBODY_Renew = win32more.Devices.WebServicesOnDevices.RESPONSEBODY_Renew_head
    RESPONSEBODY_Renew._fields_ = [
        ('expires', POINTER(win32more.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)),
        ('any', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return RESPONSEBODY_Renew
def _define_RESPONSEBODY_Subscribe_head():
    class RESPONSEBODY_Subscribe(Structure):
        pass
    return RESPONSEBODY_Subscribe
def _define_RESPONSEBODY_Subscribe():
    RESPONSEBODY_Subscribe = win32more.Devices.WebServicesOnDevices.RESPONSEBODY_Subscribe_head
    RESPONSEBODY_Subscribe._fields_ = [
        ('SubscriptionManager', POINTER(win32more.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)),
        ('expires', POINTER(win32more.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head)),
        ('any', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return RESPONSEBODY_Subscribe
def _define_RESPONSEBODY_SubscriptionEnd_head():
    class RESPONSEBODY_SubscriptionEnd(Structure):
        pass
    return RESPONSEBODY_SubscriptionEnd
def _define_RESPONSEBODY_SubscriptionEnd():
    RESPONSEBODY_SubscriptionEnd = win32more.Devices.WebServicesOnDevices.RESPONSEBODY_SubscriptionEnd_head
    RESPONSEBODY_SubscriptionEnd._fields_ = [
        ('SubscriptionManager', POINTER(win32more.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)),
        ('Status', win32more.Foundation.PWSTR),
        ('Reason', POINTER(win32more.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_head)),
        ('Any', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return RESPONSEBODY_SubscriptionEnd
def _define_WSD_APP_SEQUENCE_head():
    class WSD_APP_SEQUENCE(Structure):
        pass
    return WSD_APP_SEQUENCE
def _define_WSD_APP_SEQUENCE():
    WSD_APP_SEQUENCE = win32more.Devices.WebServicesOnDevices.WSD_APP_SEQUENCE_head
    WSD_APP_SEQUENCE._fields_ = [
        ('InstanceId', UInt64),
        ('SequenceId', win32more.Foundation.PWSTR),
        ('MessageNumber', UInt64),
    ]
    return WSD_APP_SEQUENCE
def _define_WSD_BYE_head():
    class WSD_BYE(Structure):
        pass
    return WSD_BYE
def _define_WSD_BYE():
    WSD_BYE = win32more.Devices.WebServicesOnDevices.WSD_BYE_head
    WSD_BYE._fields_ = [
        ('EndpointReference', POINTER(win32more.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)),
        ('Any', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return WSD_BYE
def _define_WSD_CONFIG_ADDRESSES_head():
    class WSD_CONFIG_ADDRESSES(Structure):
        pass
    return WSD_CONFIG_ADDRESSES
def _define_WSD_CONFIG_ADDRESSES():
    WSD_CONFIG_ADDRESSES = win32more.Devices.WebServicesOnDevices.WSD_CONFIG_ADDRESSES_head
    WSD_CONFIG_ADDRESSES._fields_ = [
        ('addresses', POINTER(win32more.Devices.WebServicesOnDevices.IWSDAddress_head)),
        ('dwAddressCount', UInt32),
    ]
    return WSD_CONFIG_ADDRESSES
def _define_WSD_CONFIG_PARAM_head():
    class WSD_CONFIG_PARAM(Structure):
        pass
    return WSD_CONFIG_PARAM
def _define_WSD_CONFIG_PARAM():
    WSD_CONFIG_PARAM = win32more.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_head
    WSD_CONFIG_PARAM._fields_ = [
        ('configParamType', win32more.Devices.WebServicesOnDevices.WSD_CONFIG_PARAM_TYPE),
        ('pConfigData', c_void_p),
        ('dwConfigDataSize', UInt32),
    ]
    return WSD_CONFIG_PARAM
WSD_CONFIG_PARAM_TYPE = Int32
WSD_CONFIG_MAX_INBOUND_MESSAGE_SIZE = 1
WSD_CONFIG_MAX_OUTBOUND_MESSAGE_SIZE = 2
WSD_SECURITY_SSL_CERT_FOR_CLIENT_AUTH = 3
WSD_SECURITY_SSL_SERVER_CERT_VALIDATION = 4
WSD_SECURITY_SSL_CLIENT_CERT_VALIDATION = 5
WSD_SECURITY_SSL_NEGOTIATE_CLIENT_CERT = 6
WSD_SECURITY_COMPACTSIG_SIGNING_CERT = 7
WSD_SECURITY_COMPACTSIG_VALIDATION = 8
WSD_CONFIG_HOSTING_ADDRESSES = 9
WSD_CONFIG_DEVICE_ADDRESSES = 10
WSD_SECURITY_REQUIRE_HTTP_CLIENT_AUTH = 11
WSD_SECURITY_REQUIRE_CLIENT_CERT_OR_HTTP_CLIENT_AUTH = 12
WSD_SECURITY_USE_HTTP_CLIENT_AUTH = 13
def _define_WSD_DATETIME_head():
    class WSD_DATETIME(Structure):
        pass
    return WSD_DATETIME
def _define_WSD_DATETIME():
    WSD_DATETIME = win32more.Devices.WebServicesOnDevices.WSD_DATETIME_head
    WSD_DATETIME._fields_ = [
        ('isPositive', win32more.Foundation.BOOL),
        ('year', UInt32),
        ('month', Byte),
        ('day', Byte),
        ('hour', Byte),
        ('minute', Byte),
        ('second', Byte),
        ('millisecond', UInt32),
        ('TZIsLocal', win32more.Foundation.BOOL),
        ('TZIsPositive', win32more.Foundation.BOOL),
        ('TZHour', Byte),
        ('TZMinute', Byte),
    ]
    return WSD_DATETIME
def _define_WSD_DURATION_head():
    class WSD_DURATION(Structure):
        pass
    return WSD_DURATION
def _define_WSD_DURATION():
    WSD_DURATION = win32more.Devices.WebServicesOnDevices.WSD_DURATION_head
    WSD_DURATION._fields_ = [
        ('isPositive', win32more.Foundation.BOOL),
        ('year', UInt32),
        ('month', UInt32),
        ('day', UInt32),
        ('hour', UInt32),
        ('minute', UInt32),
        ('second', UInt32),
        ('millisecond', UInt32),
    ]
    return WSD_DURATION
def _define_WSD_ENDPOINT_REFERENCE_head():
    class WSD_ENDPOINT_REFERENCE(Structure):
        pass
    return WSD_ENDPOINT_REFERENCE
def _define_WSD_ENDPOINT_REFERENCE():
    WSD_ENDPOINT_REFERENCE = win32more.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head
    WSD_ENDPOINT_REFERENCE._fields_ = [
        ('Address', win32more.Foundation.PWSTR),
        ('ReferenceProperties', win32more.Devices.WebServicesOnDevices.WSD_REFERENCE_PROPERTIES),
        ('ReferenceParameters', win32more.Devices.WebServicesOnDevices.WSD_REFERENCE_PARAMETERS),
        ('PortType', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_NAME_head)),
        ('ServiceName', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_NAME_head)),
        ('Any', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return WSD_ENDPOINT_REFERENCE
def _define_WSD_ENDPOINT_REFERENCE_LIST_head():
    class WSD_ENDPOINT_REFERENCE_LIST(Structure):
        pass
    return WSD_ENDPOINT_REFERENCE_LIST
def _define_WSD_ENDPOINT_REFERENCE_LIST():
    WSD_ENDPOINT_REFERENCE_LIST = win32more.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_LIST_head
    WSD_ENDPOINT_REFERENCE_LIST._fields_ = [
        ('Next', POINTER(win32more.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_LIST_head)),
        ('Element', POINTER(win32more.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)),
    ]
    return WSD_ENDPOINT_REFERENCE_LIST
def _define_WSD_EVENT_head():
    class WSD_EVENT(Structure):
        pass
    return WSD_EVENT
def _define_WSD_EVENT():
    WSD_EVENT = win32more.Devices.WebServicesOnDevices.WSD_EVENT_head
    WSD_EVENT._fields_ = [
        ('Hr', win32more.Foundation.HRESULT),
        ('EventType', UInt32),
        ('DispatchTag', win32more.Foundation.PWSTR),
        ('HandlerContext', win32more.Devices.WebServicesOnDevices.WSD_HANDLER_CONTEXT),
        ('Soap', POINTER(win32more.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head)),
        ('Operation', POINTER(win32more.Devices.WebServicesOnDevices.WSD_OPERATION_head)),
        ('MessageParameters', win32more.Devices.WebServicesOnDevices.IWSDMessageParameters_head),
    ]
    return WSD_EVENT
def _define_WSD_EVENTING_DELIVERY_MODE_head():
    class WSD_EVENTING_DELIVERY_MODE(Structure):
        pass
    return WSD_EVENTING_DELIVERY_MODE
def _define_WSD_EVENTING_DELIVERY_MODE():
    WSD_EVENTING_DELIVERY_MODE = win32more.Devices.WebServicesOnDevices.WSD_EVENTING_DELIVERY_MODE_head
    WSD_EVENTING_DELIVERY_MODE._fields_ = [
        ('Mode', win32more.Foundation.PWSTR),
        ('Push', POINTER(win32more.Devices.WebServicesOnDevices.WSD_EVENTING_DELIVERY_MODE_PUSH_head)),
        ('Data', c_void_p),
    ]
    return WSD_EVENTING_DELIVERY_MODE
def _define_WSD_EVENTING_DELIVERY_MODE_PUSH_head():
    class WSD_EVENTING_DELIVERY_MODE_PUSH(Structure):
        pass
    return WSD_EVENTING_DELIVERY_MODE_PUSH
def _define_WSD_EVENTING_DELIVERY_MODE_PUSH():
    WSD_EVENTING_DELIVERY_MODE_PUSH = win32more.Devices.WebServicesOnDevices.WSD_EVENTING_DELIVERY_MODE_PUSH_head
    WSD_EVENTING_DELIVERY_MODE_PUSH._fields_ = [
        ('NotifyTo', POINTER(win32more.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)),
    ]
    return WSD_EVENTING_DELIVERY_MODE_PUSH
def _define_WSD_EVENTING_EXPIRES_head():
    class WSD_EVENTING_EXPIRES(Structure):
        pass
    return WSD_EVENTING_EXPIRES
def _define_WSD_EVENTING_EXPIRES():
    WSD_EVENTING_EXPIRES = win32more.Devices.WebServicesOnDevices.WSD_EVENTING_EXPIRES_head
    WSD_EVENTING_EXPIRES._fields_ = [
        ('Duration', POINTER(win32more.Devices.WebServicesOnDevices.WSD_DURATION_head)),
        ('DateTime', POINTER(win32more.Devices.WebServicesOnDevices.WSD_DATETIME_head)),
    ]
    return WSD_EVENTING_EXPIRES
def _define_WSD_EVENTING_FILTER_head():
    class WSD_EVENTING_FILTER(Structure):
        pass
    return WSD_EVENTING_FILTER
def _define_WSD_EVENTING_FILTER():
    WSD_EVENTING_FILTER = win32more.Devices.WebServicesOnDevices.WSD_EVENTING_FILTER_head
    WSD_EVENTING_FILTER._fields_ = [
        ('Dialect', win32more.Foundation.PWSTR),
        ('FilterAction', POINTER(win32more.Devices.WebServicesOnDevices.WSD_EVENTING_FILTER_ACTION_head)),
        ('Data', c_void_p),
    ]
    return WSD_EVENTING_FILTER
def _define_WSD_EVENTING_FILTER_ACTION_head():
    class WSD_EVENTING_FILTER_ACTION(Structure):
        pass
    return WSD_EVENTING_FILTER_ACTION
def _define_WSD_EVENTING_FILTER_ACTION():
    WSD_EVENTING_FILTER_ACTION = win32more.Devices.WebServicesOnDevices.WSD_EVENTING_FILTER_ACTION_head
    WSD_EVENTING_FILTER_ACTION._fields_ = [
        ('Actions', POINTER(win32more.Devices.WebServicesOnDevices.WSD_URI_LIST_head)),
    ]
    return WSD_EVENTING_FILTER_ACTION
def _define_WSD_HANDLER_CONTEXT_head():
    class WSD_HANDLER_CONTEXT(Structure):
        pass
    return WSD_HANDLER_CONTEXT
def _define_WSD_HANDLER_CONTEXT():
    WSD_HANDLER_CONTEXT = win32more.Devices.WebServicesOnDevices.WSD_HANDLER_CONTEXT_head
    WSD_HANDLER_CONTEXT._fields_ = [
        ('Handler', win32more.Devices.WebServicesOnDevices.PWSD_SOAP_MESSAGE_HANDLER),
        ('PVoid', c_void_p),
        ('Unknown', win32more.System.Com.IUnknown_head),
    ]
    return WSD_HANDLER_CONTEXT
def _define_WSD_HEADER_RELATESTO_head():
    class WSD_HEADER_RELATESTO(Structure):
        pass
    return WSD_HEADER_RELATESTO
def _define_WSD_HEADER_RELATESTO():
    WSD_HEADER_RELATESTO = win32more.Devices.WebServicesOnDevices.WSD_HEADER_RELATESTO_head
    WSD_HEADER_RELATESTO._fields_ = [
        ('RelationshipType', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_NAME_head)),
        ('MessageID', win32more.Foundation.PWSTR),
    ]
    return WSD_HEADER_RELATESTO
def _define_WSD_HELLO_head():
    class WSD_HELLO(Structure):
        pass
    return WSD_HELLO
def _define_WSD_HELLO():
    WSD_HELLO = win32more.Devices.WebServicesOnDevices.WSD_HELLO_head
    WSD_HELLO._fields_ = [
        ('EndpointReference', POINTER(win32more.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)),
        ('Types', POINTER(win32more.Devices.WebServicesOnDevices.WSD_NAME_LIST_head)),
        ('Scopes', POINTER(win32more.Devices.WebServicesOnDevices.WSD_SCOPES_head)),
        ('XAddrs', POINTER(win32more.Devices.WebServicesOnDevices.WSD_URI_LIST_head)),
        ('MetadataVersion', UInt64),
        ('Any', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return WSD_HELLO
def _define_WSD_HOST_METADATA_head():
    class WSD_HOST_METADATA(Structure):
        pass
    return WSD_HOST_METADATA
def _define_WSD_HOST_METADATA():
    WSD_HOST_METADATA = win32more.Devices.WebServicesOnDevices.WSD_HOST_METADATA_head
    WSD_HOST_METADATA._fields_ = [
        ('Host', POINTER(win32more.Devices.WebServicesOnDevices.WSD_SERVICE_METADATA_head)),
        ('Hosted', POINTER(win32more.Devices.WebServicesOnDevices.WSD_SERVICE_METADATA_LIST_head)),
    ]
    return WSD_HOST_METADATA
def _define_WSD_LOCALIZED_STRING_head():
    class WSD_LOCALIZED_STRING(Structure):
        pass
    return WSD_LOCALIZED_STRING
def _define_WSD_LOCALIZED_STRING():
    WSD_LOCALIZED_STRING = win32more.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_head
    WSD_LOCALIZED_STRING._fields_ = [
        ('lang', win32more.Foundation.PWSTR),
        ('String', win32more.Foundation.PWSTR),
    ]
    return WSD_LOCALIZED_STRING
def _define_WSD_LOCALIZED_STRING_LIST_head():
    class WSD_LOCALIZED_STRING_LIST(Structure):
        pass
    return WSD_LOCALIZED_STRING_LIST
def _define_WSD_LOCALIZED_STRING_LIST():
    WSD_LOCALIZED_STRING_LIST = win32more.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST_head
    WSD_LOCALIZED_STRING_LIST._fields_ = [
        ('Next', POINTER(win32more.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST_head)),
        ('Element', POINTER(win32more.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_head)),
    ]
    return WSD_LOCALIZED_STRING_LIST
def _define_WSD_METADATA_SECTION_head():
    class WSD_METADATA_SECTION(Structure):
        pass
    return WSD_METADATA_SECTION
def _define_WSD_METADATA_SECTION():
    WSD_METADATA_SECTION = win32more.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_head
    WSD_METADATA_SECTION._fields_ = [
        ('Dialect', win32more.Foundation.PWSTR),
        ('Identifier', win32more.Foundation.PWSTR),
        ('Data', c_void_p),
        ('MetadataReference', POINTER(win32more.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)),
        ('Location', win32more.Foundation.PWSTR),
        ('Any', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return WSD_METADATA_SECTION
def _define_WSD_METADATA_SECTION_LIST_head():
    class WSD_METADATA_SECTION_LIST(Structure):
        pass
    return WSD_METADATA_SECTION_LIST
def _define_WSD_METADATA_SECTION_LIST():
    WSD_METADATA_SECTION_LIST = win32more.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST_head
    WSD_METADATA_SECTION_LIST._fields_ = [
        ('Next', POINTER(win32more.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_LIST_head)),
        ('Element', POINTER(win32more.Devices.WebServicesOnDevices.WSD_METADATA_SECTION_head)),
    ]
    return WSD_METADATA_SECTION_LIST
def _define_WSD_NAME_LIST_head():
    class WSD_NAME_LIST(Structure):
        pass
    return WSD_NAME_LIST
def _define_WSD_NAME_LIST():
    WSD_NAME_LIST = win32more.Devices.WebServicesOnDevices.WSD_NAME_LIST_head
    WSD_NAME_LIST._fields_ = [
        ('Next', POINTER(win32more.Devices.WebServicesOnDevices.WSD_NAME_LIST_head)),
        ('Element', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_NAME_head)),
    ]
    return WSD_NAME_LIST
def _define_WSD_OPERATION_head():
    class WSD_OPERATION(Structure):
        pass
    return WSD_OPERATION
def _define_WSD_OPERATION():
    WSD_OPERATION = win32more.Devices.WebServicesOnDevices.WSD_OPERATION_head
    WSD_OPERATION._fields_ = [
        ('RequestType', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_TYPE_head)),
        ('ResponseType', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_TYPE_head)),
        ('RequestStubFunction', win32more.Devices.WebServicesOnDevices.WSD_STUB_FUNCTION),
    ]
    return WSD_OPERATION
def _define_WSD_PORT_TYPE_head():
    class WSD_PORT_TYPE(Structure):
        pass
    return WSD_PORT_TYPE
def _define_WSD_PORT_TYPE():
    WSD_PORT_TYPE = win32more.Devices.WebServicesOnDevices.WSD_PORT_TYPE_head
    WSD_PORT_TYPE._fields_ = [
        ('EncodedName', UInt32),
        ('OperationCount', UInt32),
        ('Operations', POINTER(win32more.Devices.WebServicesOnDevices.WSD_OPERATION_head)),
        ('ProtocolType', win32more.Devices.WebServicesOnDevices.WSD_PROTOCOL_TYPE),
    ]
    return WSD_PORT_TYPE
def _define_WSD_PROBE_head():
    class WSD_PROBE(Structure):
        pass
    return WSD_PROBE
def _define_WSD_PROBE():
    WSD_PROBE = win32more.Devices.WebServicesOnDevices.WSD_PROBE_head
    WSD_PROBE._fields_ = [
        ('Types', POINTER(win32more.Devices.WebServicesOnDevices.WSD_NAME_LIST_head)),
        ('Scopes', POINTER(win32more.Devices.WebServicesOnDevices.WSD_SCOPES_head)),
        ('Any', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return WSD_PROBE
def _define_WSD_PROBE_MATCH_head():
    class WSD_PROBE_MATCH(Structure):
        pass
    return WSD_PROBE_MATCH
def _define_WSD_PROBE_MATCH():
    WSD_PROBE_MATCH = win32more.Devices.WebServicesOnDevices.WSD_PROBE_MATCH_head
    WSD_PROBE_MATCH._fields_ = [
        ('EndpointReference', POINTER(win32more.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)),
        ('Types', POINTER(win32more.Devices.WebServicesOnDevices.WSD_NAME_LIST_head)),
        ('Scopes', POINTER(win32more.Devices.WebServicesOnDevices.WSD_SCOPES_head)),
        ('XAddrs', POINTER(win32more.Devices.WebServicesOnDevices.WSD_URI_LIST_head)),
        ('MetadataVersion', UInt64),
        ('Any', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return WSD_PROBE_MATCH
def _define_WSD_PROBE_MATCH_LIST_head():
    class WSD_PROBE_MATCH_LIST(Structure):
        pass
    return WSD_PROBE_MATCH_LIST
def _define_WSD_PROBE_MATCH_LIST():
    WSD_PROBE_MATCH_LIST = win32more.Devices.WebServicesOnDevices.WSD_PROBE_MATCH_LIST_head
    WSD_PROBE_MATCH_LIST._fields_ = [
        ('Next', POINTER(win32more.Devices.WebServicesOnDevices.WSD_PROBE_MATCH_LIST_head)),
        ('Element', POINTER(win32more.Devices.WebServicesOnDevices.WSD_PROBE_MATCH_head)),
    ]
    return WSD_PROBE_MATCH_LIST
def _define_WSD_PROBE_MATCHES_head():
    class WSD_PROBE_MATCHES(Structure):
        pass
    return WSD_PROBE_MATCHES
def _define_WSD_PROBE_MATCHES():
    WSD_PROBE_MATCHES = win32more.Devices.WebServicesOnDevices.WSD_PROBE_MATCHES_head
    WSD_PROBE_MATCHES._fields_ = [
        ('ProbeMatch', POINTER(win32more.Devices.WebServicesOnDevices.WSD_PROBE_MATCH_LIST_head)),
        ('Any', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return WSD_PROBE_MATCHES
WSD_PROTOCOL_TYPE = Int32
WSD_PT_NONE = 0
WSD_PT_UDP = 1
WSD_PT_HTTP = 2
WSD_PT_HTTPS = 4
WSD_PT_ALL = 255
def _define_WSD_REFERENCE_PARAMETERS_head():
    class WSD_REFERENCE_PARAMETERS(Structure):
        pass
    return WSD_REFERENCE_PARAMETERS
def _define_WSD_REFERENCE_PARAMETERS():
    WSD_REFERENCE_PARAMETERS = win32more.Devices.WebServicesOnDevices.WSD_REFERENCE_PARAMETERS_head
    WSD_REFERENCE_PARAMETERS._fields_ = [
        ('Any', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return WSD_REFERENCE_PARAMETERS
def _define_WSD_REFERENCE_PROPERTIES_head():
    class WSD_REFERENCE_PROPERTIES(Structure):
        pass
    return WSD_REFERENCE_PROPERTIES
def _define_WSD_REFERENCE_PROPERTIES():
    WSD_REFERENCE_PROPERTIES = win32more.Devices.WebServicesOnDevices.WSD_REFERENCE_PROPERTIES_head
    WSD_REFERENCE_PROPERTIES._fields_ = [
        ('Any', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return WSD_REFERENCE_PROPERTIES
def _define_WSD_RELATIONSHIP_METADATA_head():
    class WSD_RELATIONSHIP_METADATA(Structure):
        pass
    return WSD_RELATIONSHIP_METADATA
def _define_WSD_RELATIONSHIP_METADATA():
    WSD_RELATIONSHIP_METADATA = win32more.Devices.WebServicesOnDevices.WSD_RELATIONSHIP_METADATA_head
    WSD_RELATIONSHIP_METADATA._fields_ = [
        ('Type', win32more.Foundation.PWSTR),
        ('Data', POINTER(win32more.Devices.WebServicesOnDevices.WSD_HOST_METADATA_head)),
        ('Any', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return WSD_RELATIONSHIP_METADATA
def _define_WSD_RESOLVE_head():
    class WSD_RESOLVE(Structure):
        pass
    return WSD_RESOLVE
def _define_WSD_RESOLVE():
    WSD_RESOLVE = win32more.Devices.WebServicesOnDevices.WSD_RESOLVE_head
    WSD_RESOLVE._fields_ = [
        ('EndpointReference', POINTER(win32more.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)),
        ('Any', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return WSD_RESOLVE
def _define_WSD_RESOLVE_MATCH_head():
    class WSD_RESOLVE_MATCH(Structure):
        pass
    return WSD_RESOLVE_MATCH
def _define_WSD_RESOLVE_MATCH():
    WSD_RESOLVE_MATCH = win32more.Devices.WebServicesOnDevices.WSD_RESOLVE_MATCH_head
    WSD_RESOLVE_MATCH._fields_ = [
        ('EndpointReference', POINTER(win32more.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)),
        ('Types', POINTER(win32more.Devices.WebServicesOnDevices.WSD_NAME_LIST_head)),
        ('Scopes', POINTER(win32more.Devices.WebServicesOnDevices.WSD_SCOPES_head)),
        ('XAddrs', POINTER(win32more.Devices.WebServicesOnDevices.WSD_URI_LIST_head)),
        ('MetadataVersion', UInt64),
        ('Any', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return WSD_RESOLVE_MATCH
def _define_WSD_RESOLVE_MATCHES_head():
    class WSD_RESOLVE_MATCHES(Structure):
        pass
    return WSD_RESOLVE_MATCHES
def _define_WSD_RESOLVE_MATCHES():
    WSD_RESOLVE_MATCHES = win32more.Devices.WebServicesOnDevices.WSD_RESOLVE_MATCHES_head
    WSD_RESOLVE_MATCHES._fields_ = [
        ('ResolveMatch', POINTER(win32more.Devices.WebServicesOnDevices.WSD_RESOLVE_MATCH_head)),
        ('Any', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return WSD_RESOLVE_MATCHES
def _define_WSD_SCOPES_head():
    class WSD_SCOPES(Structure):
        pass
    return WSD_SCOPES
def _define_WSD_SCOPES():
    WSD_SCOPES = win32more.Devices.WebServicesOnDevices.WSD_SCOPES_head
    WSD_SCOPES._fields_ = [
        ('MatchBy', win32more.Foundation.PWSTR),
        ('Scopes', POINTER(win32more.Devices.WebServicesOnDevices.WSD_URI_LIST_head)),
    ]
    return WSD_SCOPES
def _define_WSD_SECURITY_CERT_VALIDATION_head():
    class WSD_SECURITY_CERT_VALIDATION(Structure):
        pass
    return WSD_SECURITY_CERT_VALIDATION
def _define_WSD_SECURITY_CERT_VALIDATION():
    WSD_SECURITY_CERT_VALIDATION = win32more.Devices.WebServicesOnDevices.WSD_SECURITY_CERT_VALIDATION_head
    WSD_SECURITY_CERT_VALIDATION._fields_ = [
        ('certMatchArray', POINTER(POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head))),
        ('dwCertMatchArrayCount', UInt32),
        ('hCertMatchStore', win32more.Security.Cryptography.HCERTSTORE),
        ('hCertIssuerStore', win32more.Security.Cryptography.HCERTSTORE),
        ('dwCertCheckOptions', UInt32),
        ('pszCNGHashAlgId', win32more.Foundation.PWSTR),
        ('pbCertHash', c_char_p_no),
        ('dwCertHashSize', UInt32),
    ]
    return WSD_SECURITY_CERT_VALIDATION
def _define_WSD_SECURITY_CERT_VALIDATION_V1_head():
    class WSD_SECURITY_CERT_VALIDATION_V1(Structure):
        pass
    return WSD_SECURITY_CERT_VALIDATION_V1
def _define_WSD_SECURITY_CERT_VALIDATION_V1():
    WSD_SECURITY_CERT_VALIDATION_V1 = win32more.Devices.WebServicesOnDevices.WSD_SECURITY_CERT_VALIDATION_V1_head
    WSD_SECURITY_CERT_VALIDATION_V1._fields_ = [
        ('certMatchArray', POINTER(POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head))),
        ('dwCertMatchArrayCount', UInt32),
        ('hCertMatchStore', win32more.Security.Cryptography.HCERTSTORE),
        ('hCertIssuerStore', win32more.Security.Cryptography.HCERTSTORE),
        ('dwCertCheckOptions', UInt32),
    ]
    return WSD_SECURITY_CERT_VALIDATION_V1
def _define_WSD_SECURITY_SIGNATURE_VALIDATION_head():
    class WSD_SECURITY_SIGNATURE_VALIDATION(Structure):
        pass
    return WSD_SECURITY_SIGNATURE_VALIDATION
def _define_WSD_SECURITY_SIGNATURE_VALIDATION():
    WSD_SECURITY_SIGNATURE_VALIDATION = win32more.Devices.WebServicesOnDevices.WSD_SECURITY_SIGNATURE_VALIDATION_head
    WSD_SECURITY_SIGNATURE_VALIDATION._fields_ = [
        ('signingCertArray', POINTER(POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head))),
        ('dwSigningCertArrayCount', UInt32),
        ('hSigningCertStore', win32more.Security.Cryptography.HCERTSTORE),
        ('dwFlags', UInt32),
    ]
    return WSD_SECURITY_SIGNATURE_VALIDATION
def _define_WSD_SERVICE_METADATA_head():
    class WSD_SERVICE_METADATA(Structure):
        pass
    return WSD_SERVICE_METADATA
def _define_WSD_SERVICE_METADATA():
    WSD_SERVICE_METADATA = win32more.Devices.WebServicesOnDevices.WSD_SERVICE_METADATA_head
    WSD_SERVICE_METADATA._fields_ = [
        ('EndpointReference', POINTER(win32more.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_LIST_head)),
        ('Types', POINTER(win32more.Devices.WebServicesOnDevices.WSD_NAME_LIST_head)),
        ('ServiceId', win32more.Foundation.PWSTR),
        ('Any', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return WSD_SERVICE_METADATA
def _define_WSD_SERVICE_METADATA_LIST_head():
    class WSD_SERVICE_METADATA_LIST(Structure):
        pass
    return WSD_SERVICE_METADATA_LIST
def _define_WSD_SERVICE_METADATA_LIST():
    WSD_SERVICE_METADATA_LIST = win32more.Devices.WebServicesOnDevices.WSD_SERVICE_METADATA_LIST_head
    WSD_SERVICE_METADATA_LIST._fields_ = [
        ('Next', POINTER(win32more.Devices.WebServicesOnDevices.WSD_SERVICE_METADATA_LIST_head)),
        ('Element', POINTER(win32more.Devices.WebServicesOnDevices.WSD_SERVICE_METADATA_head)),
    ]
    return WSD_SERVICE_METADATA_LIST
def _define_WSD_SOAP_FAULT_head():
    class WSD_SOAP_FAULT(Structure):
        pass
    return WSD_SOAP_FAULT
def _define_WSD_SOAP_FAULT():
    WSD_SOAP_FAULT = win32more.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_head
    WSD_SOAP_FAULT._fields_ = [
        ('Code', POINTER(win32more.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_CODE_head)),
        ('Reason', POINTER(win32more.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_REASON_head)),
        ('Node', win32more.Foundation.PWSTR),
        ('Role', win32more.Foundation.PWSTR),
        ('Detail', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return WSD_SOAP_FAULT
def _define_WSD_SOAP_FAULT_CODE_head():
    class WSD_SOAP_FAULT_CODE(Structure):
        pass
    return WSD_SOAP_FAULT_CODE
def _define_WSD_SOAP_FAULT_CODE():
    WSD_SOAP_FAULT_CODE = win32more.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_CODE_head
    WSD_SOAP_FAULT_CODE._fields_ = [
        ('Value', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_NAME_head)),
        ('Subcode', POINTER(win32more.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_SUBCODE_head)),
    ]
    return WSD_SOAP_FAULT_CODE
def _define_WSD_SOAP_FAULT_REASON_head():
    class WSD_SOAP_FAULT_REASON(Structure):
        pass
    return WSD_SOAP_FAULT_REASON
def _define_WSD_SOAP_FAULT_REASON():
    WSD_SOAP_FAULT_REASON = win32more.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_REASON_head
    WSD_SOAP_FAULT_REASON._fields_ = [
        ('Text', POINTER(win32more.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST_head)),
    ]
    return WSD_SOAP_FAULT_REASON
def _define_WSD_SOAP_FAULT_SUBCODE_head():
    class WSD_SOAP_FAULT_SUBCODE(Structure):
        pass
    return WSD_SOAP_FAULT_SUBCODE
def _define_WSD_SOAP_FAULT_SUBCODE():
    WSD_SOAP_FAULT_SUBCODE = win32more.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_SUBCODE_head
    WSD_SOAP_FAULT_SUBCODE._fields_ = [
        ('Value', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_NAME_head)),
        ('Subcode', POINTER(win32more.Devices.WebServicesOnDevices.WSD_SOAP_FAULT_SUBCODE_head)),
    ]
    return WSD_SOAP_FAULT_SUBCODE
def _define_WSD_SOAP_HEADER_head():
    class WSD_SOAP_HEADER(Structure):
        pass
    return WSD_SOAP_HEADER
def _define_WSD_SOAP_HEADER():
    WSD_SOAP_HEADER = win32more.Devices.WebServicesOnDevices.WSD_SOAP_HEADER_head
    WSD_SOAP_HEADER._fields_ = [
        ('To', win32more.Foundation.PWSTR),
        ('Action', win32more.Foundation.PWSTR),
        ('MessageID', win32more.Foundation.PWSTR),
        ('RelatesTo', win32more.Devices.WebServicesOnDevices.WSD_HEADER_RELATESTO),
        ('ReplyTo', POINTER(win32more.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)),
        ('From', POINTER(win32more.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)),
        ('FaultTo', POINTER(win32more.Devices.WebServicesOnDevices.WSD_ENDPOINT_REFERENCE_head)),
        ('AppSequence', POINTER(win32more.Devices.WebServicesOnDevices.WSD_APP_SEQUENCE_head)),
        ('AnyHeaders', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return WSD_SOAP_HEADER
def _define_WSD_SOAP_MESSAGE_head():
    class WSD_SOAP_MESSAGE(Structure):
        pass
    return WSD_SOAP_MESSAGE
def _define_WSD_SOAP_MESSAGE():
    WSD_SOAP_MESSAGE = win32more.Devices.WebServicesOnDevices.WSD_SOAP_MESSAGE_head
    WSD_SOAP_MESSAGE._fields_ = [
        ('Header', win32more.Devices.WebServicesOnDevices.WSD_SOAP_HEADER),
        ('Body', c_void_p),
        ('BodyType', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_TYPE_head)),
    ]
    return WSD_SOAP_MESSAGE
def _define_WSD_STUB_FUNCTION():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Devices.WebServicesOnDevices.IWSDServiceMessaging_head,POINTER(win32more.Devices.WebServicesOnDevices.WSD_EVENT_head))
def _define_WSD_SYNCHRONOUS_RESPONSE_CONTEXT_head():
    class WSD_SYNCHRONOUS_RESPONSE_CONTEXT(Structure):
        pass
    return WSD_SYNCHRONOUS_RESPONSE_CONTEXT
def _define_WSD_SYNCHRONOUS_RESPONSE_CONTEXT():
    WSD_SYNCHRONOUS_RESPONSE_CONTEXT = win32more.Devices.WebServicesOnDevices.WSD_SYNCHRONOUS_RESPONSE_CONTEXT_head
    WSD_SYNCHRONOUS_RESPONSE_CONTEXT._fields_ = [
        ('hr', win32more.Foundation.HRESULT),
        ('eventHandle', win32more.Foundation.HANDLE),
        ('messageParameters', win32more.Devices.WebServicesOnDevices.IWSDMessageParameters_head),
        ('results', c_void_p),
    ]
    return WSD_SYNCHRONOUS_RESPONSE_CONTEXT
def _define_WSD_THIS_DEVICE_METADATA_head():
    class WSD_THIS_DEVICE_METADATA(Structure):
        pass
    return WSD_THIS_DEVICE_METADATA
def _define_WSD_THIS_DEVICE_METADATA():
    WSD_THIS_DEVICE_METADATA = win32more.Devices.WebServicesOnDevices.WSD_THIS_DEVICE_METADATA_head
    WSD_THIS_DEVICE_METADATA._fields_ = [
        ('FriendlyName', POINTER(win32more.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST_head)),
        ('FirmwareVersion', win32more.Foundation.PWSTR),
        ('SerialNumber', win32more.Foundation.PWSTR),
        ('Any', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return WSD_THIS_DEVICE_METADATA
def _define_WSD_THIS_MODEL_METADATA_head():
    class WSD_THIS_MODEL_METADATA(Structure):
        pass
    return WSD_THIS_MODEL_METADATA
def _define_WSD_THIS_MODEL_METADATA():
    WSD_THIS_MODEL_METADATA = win32more.Devices.WebServicesOnDevices.WSD_THIS_MODEL_METADATA_head
    WSD_THIS_MODEL_METADATA._fields_ = [
        ('Manufacturer', POINTER(win32more.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST_head)),
        ('ManufacturerUrl', win32more.Foundation.PWSTR),
        ('ModelName', POINTER(win32more.Devices.WebServicesOnDevices.WSD_LOCALIZED_STRING_LIST_head)),
        ('ModelNumber', win32more.Foundation.PWSTR),
        ('ModelUrl', win32more.Foundation.PWSTR),
        ('PresentationUrl', win32more.Foundation.PWSTR),
        ('Any', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return WSD_THIS_MODEL_METADATA
def _define_WSD_UNKNOWN_LOOKUP_head():
    class WSD_UNKNOWN_LOOKUP(Structure):
        pass
    return WSD_UNKNOWN_LOOKUP
def _define_WSD_UNKNOWN_LOOKUP():
    WSD_UNKNOWN_LOOKUP = win32more.Devices.WebServicesOnDevices.WSD_UNKNOWN_LOOKUP_head
    WSD_UNKNOWN_LOOKUP._fields_ = [
        ('Any', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return WSD_UNKNOWN_LOOKUP
def _define_WSD_URI_LIST_head():
    class WSD_URI_LIST(Structure):
        pass
    return WSD_URI_LIST
def _define_WSD_URI_LIST():
    WSD_URI_LIST = win32more.Devices.WebServicesOnDevices.WSD_URI_LIST_head
    WSD_URI_LIST._fields_ = [
        ('Next', POINTER(win32more.Devices.WebServicesOnDevices.WSD_URI_LIST_head)),
        ('Element', win32more.Foundation.PWSTR),
    ]
    return WSD_URI_LIST
WSDEventType = Int32
WSDET_NONE = 0
WSDET_INCOMING_MESSAGE = 1
WSDET_INCOMING_FAULT = 2
WSDET_TRANSMISSION_FAILURE = 3
WSDET_RESPONSE_TIMEOUT = 4
WSDUdpMessageType = Int32
ONE_WAY = 0
TWO_WAY = 1
def _define_WSDUdpRetransmitParams_head():
    class WSDUdpRetransmitParams(Structure):
        pass
    return WSDUdpRetransmitParams
def _define_WSDUdpRetransmitParams():
    WSDUdpRetransmitParams = win32more.Devices.WebServicesOnDevices.WSDUdpRetransmitParams_head
    WSDUdpRetransmitParams._fields_ = [
        ('ulSendDelay', UInt32),
        ('ulRepeat', UInt32),
        ('ulRepeatMinDelay', UInt32),
        ('ulRepeatMaxDelay', UInt32),
        ('ulRepeatUpperDelay', UInt32),
    ]
    return WSDUdpRetransmitParams
def _define_WSDXML_ATTRIBUTE_head():
    class WSDXML_ATTRIBUTE(Structure):
        pass
    return WSDXML_ATTRIBUTE
def _define_WSDXML_ATTRIBUTE():
    WSDXML_ATTRIBUTE = win32more.Devices.WebServicesOnDevices.WSDXML_ATTRIBUTE_head
    WSDXML_ATTRIBUTE._fields_ = [
        ('Element', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
        ('Next', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ATTRIBUTE_head)),
        ('Name', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_NAME_head)),
        ('Value', win32more.Foundation.PWSTR),
    ]
    return WSDXML_ATTRIBUTE
def _define_WSDXML_ELEMENT_head():
    class WSDXML_ELEMENT(Structure):
        pass
    return WSDXML_ELEMENT
def _define_WSDXML_ELEMENT():
    WSDXML_ELEMENT = win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head
    WSDXML_ELEMENT._fields_ = [
        ('Node', win32more.Devices.WebServicesOnDevices.WSDXML_NODE),
        ('Name', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_NAME_head)),
        ('FirstAttribute', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ATTRIBUTE_head)),
        ('FirstChild', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_NODE_head)),
        ('PrefixMappings', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_PREFIX_MAPPING_head)),
    ]
    return WSDXML_ELEMENT
def _define_WSDXML_ELEMENT_LIST_head():
    class WSDXML_ELEMENT_LIST(Structure):
        pass
    return WSDXML_ELEMENT_LIST
def _define_WSDXML_ELEMENT_LIST():
    WSDXML_ELEMENT_LIST = win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_LIST_head
    WSDXML_ELEMENT_LIST._fields_ = [
        ('Next', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_LIST_head)),
        ('Element', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
    ]
    return WSDXML_ELEMENT_LIST
def _define_WSDXML_NAME_head():
    class WSDXML_NAME(Structure):
        pass
    return WSDXML_NAME
def _define_WSDXML_NAME():
    WSDXML_NAME = win32more.Devices.WebServicesOnDevices.WSDXML_NAME_head
    WSDXML_NAME._fields_ = [
        ('Space', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_NAMESPACE_head)),
        ('LocalName', win32more.Foundation.PWSTR),
    ]
    return WSDXML_NAME
def _define_WSDXML_NAMESPACE_head():
    class WSDXML_NAMESPACE(Structure):
        pass
    return WSDXML_NAMESPACE
def _define_WSDXML_NAMESPACE():
    WSDXML_NAMESPACE = win32more.Devices.WebServicesOnDevices.WSDXML_NAMESPACE_head
    WSDXML_NAMESPACE._fields_ = [
        ('Uri', win32more.Foundation.PWSTR),
        ('PreferredPrefix', win32more.Foundation.PWSTR),
        ('Names', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_NAME_head)),
        ('NamesCount', UInt16),
        ('Encoding', UInt16),
    ]
    return WSDXML_NAMESPACE
def _define_WSDXML_NODE_head():
    class WSDXML_NODE(Structure):
        pass
    return WSDXML_NODE
def _define_WSDXML_NODE():
    WSDXML_NODE = win32more.Devices.WebServicesOnDevices.WSDXML_NODE_head
    WSDXML_NODE.ElementType = 0
    WSDXML_NODE.TextType = 1
    WSDXML_NODE._fields_ = [
        ('Type', Int32),
        ('Parent', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_ELEMENT_head)),
        ('Next', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_NODE_head)),
    ]
    return WSDXML_NODE
WSDXML_OP = Int32
WSDXML_OP_OpNone = 0
WSDXML_OP_OpEndOfTable = 1
WSDXML_OP_OpBeginElement_ = 2
WSDXML_OP_OpBeginAnyElement = 3
WSDXML_OP_OpEndElement = 4
WSDXML_OP_OpElement_ = 5
WSDXML_OP_OpAnyElement = 6
WSDXML_OP_OpAnyElements = 7
WSDXML_OP_OpAnyText = 8
WSDXML_OP_OpAttribute_ = 9
WSDXML_OP_OpBeginChoice = 10
WSDXML_OP_OpEndChoice = 11
WSDXML_OP_OpBeginSequence = 12
WSDXML_OP_OpEndSequence = 13
WSDXML_OP_OpBeginAll = 14
WSDXML_OP_OpEndAll = 15
WSDXML_OP_OpAnything = 16
WSDXML_OP_OpAnyNumber = 17
WSDXML_OP_OpOneOrMore = 18
WSDXML_OP_OpOptional = 19
WSDXML_OP_OpFormatBool_ = 20
WSDXML_OP_OpFormatInt8_ = 21
WSDXML_OP_OpFormatInt16_ = 22
WSDXML_OP_OpFormatInt32_ = 23
WSDXML_OP_OpFormatInt64_ = 24
WSDXML_OP_OpFormatUInt8_ = 25
WSDXML_OP_OpFormatUInt16_ = 26
WSDXML_OP_OpFormatUInt32_ = 27
WSDXML_OP_OpFormatUInt64_ = 28
WSDXML_OP_OpFormatUnicodeString_ = 29
WSDXML_OP_OpFormatDom_ = 30
WSDXML_OP_OpFormatStruct_ = 31
WSDXML_OP_OpFormatUri_ = 32
WSDXML_OP_OpFormatUuidUri_ = 33
WSDXML_OP_OpFormatName_ = 34
WSDXML_OP_OpFormatListInsertTail_ = 35
WSDXML_OP_OpFormatType_ = 36
WSDXML_OP_OpFormatDynamicType_ = 37
WSDXML_OP_OpFormatLookupType_ = 38
WSDXML_OP_OpFormatDuration_ = 39
WSDXML_OP_OpFormatDateTime_ = 40
WSDXML_OP_OpFormatFloat_ = 41
WSDXML_OP_OpFormatDouble_ = 42
WSDXML_OP_OpProcess_ = 43
WSDXML_OP_OpQualifiedAttribute_ = 44
WSDXML_OP_OpFormatXMLDeclaration_ = 45
WSDXML_OP_OpFormatMax = 46
def _define_WSDXML_PREFIX_MAPPING_head():
    class WSDXML_PREFIX_MAPPING(Structure):
        pass
    return WSDXML_PREFIX_MAPPING
def _define_WSDXML_PREFIX_MAPPING():
    WSDXML_PREFIX_MAPPING = win32more.Devices.WebServicesOnDevices.WSDXML_PREFIX_MAPPING_head
    WSDXML_PREFIX_MAPPING._fields_ = [
        ('Refs', UInt32),
        ('Next', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_PREFIX_MAPPING_head)),
        ('Space', POINTER(win32more.Devices.WebServicesOnDevices.WSDXML_NAMESPACE_head)),
        ('Prefix', win32more.Foundation.PWSTR),
    ]
    return WSDXML_PREFIX_MAPPING
def _define_WSDXML_TEXT_head():
    class WSDXML_TEXT(Structure):
        pass
    return WSDXML_TEXT
def _define_WSDXML_TEXT():
    WSDXML_TEXT = win32more.Devices.WebServicesOnDevices.WSDXML_TEXT_head
    WSDXML_TEXT._fields_ = [
        ('Node', win32more.Devices.WebServicesOnDevices.WSDXML_NODE),
        ('Text', win32more.Foundation.PWSTR),
    ]
    return WSDXML_TEXT
def _define_WSDXML_TYPE_head():
    class WSDXML_TYPE(Structure):
        pass
    return WSDXML_TYPE
def _define_WSDXML_TYPE():
    WSDXML_TYPE = win32more.Devices.WebServicesOnDevices.WSDXML_TYPE_head
    WSDXML_TYPE._fields_ = [
        ('Uri', win32more.Foundation.PWSTR),
        ('Table', c_char_p_no),
    ]
    return WSDXML_TYPE
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
