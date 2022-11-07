from win32more import *
import win32more.Devices.Enumeration.Pnp
import win32more.Devices.Properties
import win32more.Foundation
import win32more.Security
import win32more.System.Com

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
UPNP_E_ROOT_ELEMENT_EXPECTED = -2147220992
UPNP_E_DEVICE_ELEMENT_EXPECTED = -2147220991
UPNP_E_SERVICE_ELEMENT_EXPECTED = -2147220990
UPNP_E_SERVICE_NODE_INCOMPLETE = -2147220989
UPNP_E_DEVICE_NODE_INCOMPLETE = -2147220988
UPNP_E_ICON_ELEMENT_EXPECTED = -2147220987
UPNP_E_ICON_NODE_INCOMPLETE = -2147220986
UPNP_E_INVALID_ACTION = -2147220985
UPNP_E_INVALID_ARGUMENTS = -2147220984
UPNP_E_OUT_OF_SYNC = -2147220983
UPNP_E_ACTION_REQUEST_FAILED = -2147220976
UPNP_E_TRANSPORT_ERROR = -2147220975
UPNP_E_VARIABLE_VALUE_UNKNOWN = -2147220974
UPNP_E_INVALID_VARIABLE = -2147220973
UPNP_E_DEVICE_ERROR = -2147220972
UPNP_E_PROTOCOL_ERROR = -2147220971
UPNP_E_ERROR_PROCESSING_RESPONSE = -2147220970
UPNP_E_DEVICE_TIMEOUT = -2147220969
UPNP_E_INVALID_DOCUMENT = -2147220224
UPNP_E_EVENT_SUBSCRIPTION_FAILED = -2147220223
FAULT_INVALID_ACTION = 401
FAULT_INVALID_ARG = 402
FAULT_INVALID_SEQUENCE_NUMBER = 403
FAULT_INVALID_VARIABLE = 404
FAULT_DEVICE_INTERNAL_ERROR = 501
FAULT_ACTION_SPECIFIC_BASE = 600
FAULT_ACTION_SPECIFIC_MAX = 899
UPNP_E_ACTION_SPECIFIC_BASE = -2147220736
UPNP_ADDRESSFAMILY_IPv4 = 1
UPNP_ADDRESSFAMILY_IPv6 = 2
UPNP_ADDRESSFAMILY_BOTH = 3
UPNP_SERVICE_DELAY_SCPD_AND_SUBSCRIPTION = 1
UPNP_E_REQUIRED_ELEMENT_ERROR = -2147180512
UPNP_E_DUPLICATE_NOT_ALLOWED = -2147180511
UPNP_E_DUPLICATE_SERVICE_ID = -2147180510
UPNP_E_INVALID_DESCRIPTION = -2147180509
UPNP_E_INVALID_SERVICE = -2147180508
UPNP_E_INVALID_ICON = -2147180507
UPNP_E_INVALID_XML = -2147180506
UPNP_E_INVALID_ROOT_NAMESPACE = -2147180505
UPNP_E_SUFFIX_TOO_LONG = -2147180504
UPNP_E_URLBASE_PRESENT = -2147180503
UPNP_E_VALUE_TOO_LONG = -2147180496
UPNP_E_DEVICE_RUNNING = -2147180495
UPNP_E_DEVICE_NOTREGISTERED = -2147180494
HSWDEVICE = IntPtr
SW_DEVICE_CAPABILITIES = Int32
SW_DEVICE_CAPABILITIES_SWDeviceCapabilitiesNone = 0
SW_DEVICE_CAPABILITIES_SWDeviceCapabilitiesRemovable = 1
SW_DEVICE_CAPABILITIES_SWDeviceCapabilitiesSilentInstall = 2
SW_DEVICE_CAPABILITIES_SWDeviceCapabilitiesNoDisplayInUI = 4
SW_DEVICE_CAPABILITIES_SWDeviceCapabilitiesDriverRequired = 8
def _define_SW_DEVICE_CREATE_INFO_head():
    class SW_DEVICE_CREATE_INFO(Structure):
        pass
    return SW_DEVICE_CREATE_INFO
def _define_SW_DEVICE_CREATE_INFO():
    SW_DEVICE_CREATE_INFO = win32more.Devices.Enumeration.Pnp.SW_DEVICE_CREATE_INFO_head
    SW_DEVICE_CREATE_INFO._fields_ = [
        ("cbSize", UInt32),
        ("pszInstanceId", win32more.Foundation.PWSTR),
        ("pszzHardwareIds", win32more.Foundation.PWSTR),
        ("pszzCompatibleIds", win32more.Foundation.PWSTR),
        ("pContainerId", POINTER(Guid)),
        ("CapabilityFlags", UInt32),
        ("pszDeviceDescription", win32more.Foundation.PWSTR),
        ("pszDeviceLocation", win32more.Foundation.PWSTR),
        ("pSecurityDescriptor", POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)),
    ]
    return SW_DEVICE_CREATE_INFO
SW_DEVICE_LIFETIME = Int32
SW_DEVICE_LIFETIME_SWDeviceLifetimeHandle = 0
SW_DEVICE_LIFETIME_SWDeviceLifetimeParentPresent = 1
SW_DEVICE_LIFETIME_SWDeviceLifetimeMax = 2
def _define_SW_DEVICE_CREATE_CALLBACK():
    return CFUNCTYPE(Void,win32more.Devices.Enumeration.Pnp.HSWDEVICE,win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR, use_last_error=False)
UPnPDeviceFinder = Guid('e2085f28-feb7-404a-b8e7-e659bdeaaa02')
UPnPDevices = Guid('b9e84ffd-ad3c-40a4-b835-0882ebcbaaa8')
UPnPDevice = Guid('a32552c5-ba61-457a-b59a-a2561e125e33')
UPnPServices = Guid('c0bc4b4a-a406-4efc-932f-b8546b8100cc')
UPnPService = Guid('c624ba95-fbcb-4409-8c03-8cceec533ef1')
UPnPDescriptionDocument = Guid('1d8a9b47-3a28-4ce2-8a4b-bd34e45bceeb')
UPnPDeviceFinderEx = Guid('181b54fc-380b-4a75-b3f1-4ac45e9605b0')
UPnPDescriptionDocumentEx = Guid('33fd0563-d81a-4393-83cc-0195b1da2f91')
def _define_IUPnPDeviceFinder_head():
    class IUPnPDeviceFinder(win32more.System.Com.IDispatch_head):
        Guid = Guid('adda3d55-6f72-4319-bff9-18600a539b10')
    return IUPnPDeviceFinder
def _define_IUPnPDeviceFinder():
    IUPnPDeviceFinder = win32more.Devices.Enumeration.Pnp.IUPnPDeviceFinder_head
    IUPnPDeviceFinder.FindByType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,UInt32,POINTER(win32more.Devices.Enumeration.Pnp.IUPnPDevices_head), use_last_error=False)(7, 'FindByType', ((1, 'bstrTypeURI'),(1, 'dwFlags'),(1, 'pDevices'),)))
    IUPnPDeviceFinder.CreateAsyncFind = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,UInt32,win32more.System.Com.IUnknown_head,POINTER(Int32), use_last_error=False)(8, 'CreateAsyncFind', ((1, 'bstrTypeURI'),(1, 'dwFlags'),(1, 'punkDeviceFinderCallback'),(1, 'plFindData'),)))
    IUPnPDeviceFinder.StartAsyncFind = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(9, 'StartAsyncFind', ((1, 'lFindData'),)))
    IUPnPDeviceFinder.CancelAsyncFind = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(10, 'CancelAsyncFind', ((1, 'lFindData'),)))
    IUPnPDeviceFinder.FindByUDN = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Devices.Enumeration.Pnp.IUPnPDevice_head), use_last_error=False)(11, 'FindByUDN', ((1, 'bstrUDN'),(1, 'pDevice'),)))
    win32more.System.Com.IDispatch
    return IUPnPDeviceFinder
def _define_IUPnPAddressFamilyControl_head():
    class IUPnPAddressFamilyControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('e3bf6178-694e-459f-a5a6-191ea0ffa1c7')
    return IUPnPAddressFamilyControl
def _define_IUPnPAddressFamilyControl():
    IUPnPAddressFamilyControl = win32more.Devices.Enumeration.Pnp.IUPnPAddressFamilyControl_head
    IUPnPAddressFamilyControl.SetAddressFamily = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(3, 'SetAddressFamily', ((1, 'dwFlags'),)))
    IUPnPAddressFamilyControl.GetAddressFamily = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(4, 'GetAddressFamily', ((1, 'pdwFlags'),)))
    win32more.System.Com.IUnknown
    return IUPnPAddressFamilyControl
def _define_IUPnPHttpHeaderControl_head():
    class IUPnPHttpHeaderControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('0405af4f-8b5c-447c-80f2-b75984a31f3c')
    return IUPnPHttpHeaderControl
def _define_IUPnPHttpHeaderControl():
    IUPnPHttpHeaderControl = win32more.Devices.Enumeration.Pnp.IUPnPHttpHeaderControl_head
    IUPnPHttpHeaderControl.AddRequestHeaders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(3, 'AddRequestHeaders', ((1, 'bstrHttpHeaders'),)))
    win32more.System.Com.IUnknown
    return IUPnPHttpHeaderControl
def _define_IUPnPDeviceFinderCallback_head():
    class IUPnPDeviceFinderCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('415a984a-88b3-49f3-92af-0508bedf0d6c')
    return IUPnPDeviceFinderCallback
def _define_IUPnPDeviceFinderCallback():
    IUPnPDeviceFinderCallback = win32more.Devices.Enumeration.Pnp.IUPnPDeviceFinderCallback_head
    IUPnPDeviceFinderCallback.DeviceAdded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Devices.Enumeration.Pnp.IUPnPDevice_head, use_last_error=False)(3, 'DeviceAdded', ((1, 'lFindData'),(1, 'pDevice'),)))
    IUPnPDeviceFinderCallback.DeviceRemoved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR, use_last_error=False)(4, 'DeviceRemoved', ((1, 'lFindData'),(1, 'bstrUDN'),)))
    IUPnPDeviceFinderCallback.SearchComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(5, 'SearchComplete', ((1, 'lFindData'),)))
    win32more.System.Com.IUnknown
    return IUPnPDeviceFinderCallback
def _define_IUPnPServices_head():
    class IUPnPServices(win32more.System.Com.IDispatch_head):
        Guid = Guid('3f8c8e9e-9a7a-4dc8-bc41-ff31fa374956')
    return IUPnPServices
def _define_IUPnPServices():
    IUPnPServices = win32more.Devices.Enumeration.Pnp.IUPnPServices_head
    IUPnPServices.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'plCount'),)))
    IUPnPServices.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(8, 'get__NewEnum', ((1, 'ppunk'),)))
    IUPnPServices.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Devices.Enumeration.Pnp.IUPnPService_head), use_last_error=False)(9, 'get_Item', ((1, 'bstrServiceId'),(1, 'ppService'),)))
    win32more.System.Com.IDispatch
    return IUPnPServices
def _define_IUPnPService_head():
    class IUPnPService(win32more.System.Com.IDispatch_head):
        Guid = Guid('a295019c-dc65-47dd-90dc-7fe918a1ab44')
    return IUPnPService
def _define_IUPnPService():
    IUPnPService = win32more.Devices.Enumeration.Pnp.IUPnPService_head
    IUPnPService.QueryStateVariable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'QueryStateVariable', ((1, 'bstrVariableName'),(1, 'pValue'),)))
    IUPnPService.InvokeAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'InvokeAction', ((1, 'bstrActionName'),(1, 'vInActionArgs'),(1, 'pvOutActionArgs'),(1, 'pvRetVal'),)))
    IUPnPService.get_ServiceTypeIdentifier = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_ServiceTypeIdentifier', ((1, 'pVal'),)))
    IUPnPService.AddCallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(10, 'AddCallback', ((1, 'pUnkCallback'),)))
    IUPnPService.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_Id', ((1, 'pbstrId'),)))
    IUPnPService.get_LastTransportStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(12, 'get_LastTransportStatus', ((1, 'plValue'),)))
    win32more.System.Com.IDispatch
    return IUPnPService
def _define_IUPnPAsyncResult_head():
    class IUPnPAsyncResult(win32more.System.Com.IUnknown_head):
        Guid = Guid('4d65fd08-d13e-4274-9c8b-dd8d028c8644')
    return IUPnPAsyncResult
def _define_IUPnPAsyncResult():
    IUPnPAsyncResult = win32more.Devices.Enumeration.Pnp.IUPnPAsyncResult_head
    IUPnPAsyncResult.AsyncOperationComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64, use_last_error=False)(3, 'AsyncOperationComplete', ((1, 'ullRequestID'),)))
    win32more.System.Com.IUnknown
    return IUPnPAsyncResult
def _define_IUPnPServiceAsync_head():
    class IUPnPServiceAsync(win32more.System.Com.IUnknown_head):
        Guid = Guid('098bdaf5-5ec1-49e7-a260-b3a11dd8680c')
    return IUPnPServiceAsync
def _define_IUPnPServiceAsync():
    IUPnPServiceAsync = win32more.Devices.Enumeration.Pnp.IUPnPServiceAsync_head
    IUPnPServiceAsync.BeginInvokeAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,win32more.Devices.Enumeration.Pnp.IUPnPAsyncResult_head,POINTER(UInt64), use_last_error=False)(3, 'BeginInvokeAction', ((1, 'bstrActionName'),(1, 'vInActionArgs'),(1, 'pAsyncResult'),(1, 'pullRequestID'),)))
    IUPnPServiceAsync.EndInvokeAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(4, 'EndInvokeAction', ((1, 'ullRequestID'),(1, 'pvOutActionArgs'),(1, 'pvRetVal'),)))
    IUPnPServiceAsync.BeginQueryStateVariable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Devices.Enumeration.Pnp.IUPnPAsyncResult_head,POINTER(UInt64), use_last_error=False)(5, 'BeginQueryStateVariable', ((1, 'bstrVariableName'),(1, 'pAsyncResult'),(1, 'pullRequestID'),)))
    IUPnPServiceAsync.EndQueryStateVariable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(6, 'EndQueryStateVariable', ((1, 'ullRequestID'),(1, 'pValue'),)))
    IUPnPServiceAsync.BeginSubscribeToEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Devices.Enumeration.Pnp.IUPnPAsyncResult_head,POINTER(UInt64), use_last_error=False)(7, 'BeginSubscribeToEvents', ((1, 'pUnkCallback'),(1, 'pAsyncResult'),(1, 'pullRequestID'),)))
    IUPnPServiceAsync.EndSubscribeToEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64, use_last_error=False)(8, 'EndSubscribeToEvents', ((1, 'ullRequestID'),)))
    IUPnPServiceAsync.BeginSCPDDownload = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Enumeration.Pnp.IUPnPAsyncResult_head,POINTER(UInt64), use_last_error=False)(9, 'BeginSCPDDownload', ((1, 'pAsyncResult'),(1, 'pullRequestID'),)))
    IUPnPServiceAsync.EndSCPDDownload = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'EndSCPDDownload', ((1, 'ullRequestID'),(1, 'pbstrSCPDDoc'),)))
    IUPnPServiceAsync.CancelAsyncOperation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64, use_last_error=False)(11, 'CancelAsyncOperation', ((1, 'ullRequestID'),)))
    win32more.System.Com.IUnknown
    return IUPnPServiceAsync
def _define_IUPnPServiceCallback_head():
    class IUPnPServiceCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('31fadca9-ab73-464b-b67d-5c1d0f83c8b8')
    return IUPnPServiceCallback
def _define_IUPnPServiceCallback():
    IUPnPServiceCallback = win32more.Devices.Enumeration.Pnp.IUPnPServiceCallback_head
    IUPnPServiceCallback.StateVariableChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Enumeration.Pnp.IUPnPService_head,win32more.Foundation.PWSTR,win32more.System.Com.VARIANT, use_last_error=False)(3, 'StateVariableChanged', ((1, 'pus'),(1, 'pcwszStateVarName'),(1, 'vaValue'),)))
    IUPnPServiceCallback.ServiceInstanceDied = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Enumeration.Pnp.IUPnPService_head, use_last_error=False)(4, 'ServiceInstanceDied', ((1, 'pus'),)))
    win32more.System.Com.IUnknown
    return IUPnPServiceCallback
def _define_IUPnPServiceEnumProperty_head():
    class IUPnPServiceEnumProperty(win32more.System.Com.IUnknown_head):
        Guid = Guid('38873b37-91bb-49f4-b249-2e8efbb8a816')
    return IUPnPServiceEnumProperty
def _define_IUPnPServiceEnumProperty():
    IUPnPServiceEnumProperty = win32more.Devices.Enumeration.Pnp.IUPnPServiceEnumProperty_head
    IUPnPServiceEnumProperty.SetServiceEnumProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(3, 'SetServiceEnumProperty', ((1, 'dwMask'),)))
    win32more.System.Com.IUnknown
    return IUPnPServiceEnumProperty
def _define_IUPnPServiceDocumentAccess_head():
    class IUPnPServiceDocumentAccess(win32more.System.Com.IUnknown_head):
        Guid = Guid('21905529-0a5e-4589-825d-7e6d87ea6998')
    return IUPnPServiceDocumentAccess
def _define_IUPnPServiceDocumentAccess():
    IUPnPServiceDocumentAccess = win32more.Devices.Enumeration.Pnp.IUPnPServiceDocumentAccess_head
    IUPnPServiceDocumentAccess.GetDocumentURL = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'GetDocumentURL', ((1, 'pbstrDocUrl'),)))
    IUPnPServiceDocumentAccess.GetDocument = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'GetDocument', ((1, 'pbstrDoc'),)))
    win32more.System.Com.IUnknown
    return IUPnPServiceDocumentAccess
def _define_IUPnPDevices_head():
    class IUPnPDevices(win32more.System.Com.IDispatch_head):
        Guid = Guid('fdbc0c73-bda3-4c66-ac4f-f2d96fdad68c')
    return IUPnPDevices
def _define_IUPnPDevices():
    IUPnPDevices = win32more.Devices.Enumeration.Pnp.IUPnPDevices_head
    IUPnPDevices.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'plCount'),)))
    IUPnPDevices.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(8, 'get__NewEnum', ((1, 'ppunk'),)))
    IUPnPDevices.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Devices.Enumeration.Pnp.IUPnPDevice_head), use_last_error=False)(9, 'get_Item', ((1, 'bstrUDN'),(1, 'ppDevice'),)))
    win32more.System.Com.IDispatch
    return IUPnPDevices
def _define_IUPnPDevice_head():
    class IUPnPDevice(win32more.System.Com.IDispatch_head):
        Guid = Guid('3d44d0d1-98c9-4889-acd1-f9d674bf2221')
    return IUPnPDevice
def _define_IUPnPDevice():
    IUPnPDevice = win32more.Devices.Enumeration.Pnp.IUPnPDevice_head
    IUPnPDevice.get_IsRootDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(7, 'get_IsRootDevice', ((1, 'pvarb'),)))
    IUPnPDevice.get_RootDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Enumeration.Pnp.IUPnPDevice_head), use_last_error=False)(8, 'get_RootDevice', ((1, 'ppudRootDevice'),)))
    IUPnPDevice.get_ParentDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Enumeration.Pnp.IUPnPDevice_head), use_last_error=False)(9, 'get_ParentDevice', ((1, 'ppudDeviceParent'),)))
    IUPnPDevice.get_HasChildren = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(10, 'get_HasChildren', ((1, 'pvarb'),)))
    IUPnPDevice.get_Children = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Enumeration.Pnp.IUPnPDevices_head), use_last_error=False)(11, 'get_Children', ((1, 'ppudChildren'),)))
    IUPnPDevice.get_UniqueDeviceName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_UniqueDeviceName', ((1, 'pbstr'),)))
    IUPnPDevice.get_FriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_FriendlyName', ((1, 'pbstr'),)))
    IUPnPDevice.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_Type', ((1, 'pbstr'),)))
    IUPnPDevice.get_PresentationURL = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_PresentationURL', ((1, 'pbstr'),)))
    IUPnPDevice.get_ManufacturerName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(16, 'get_ManufacturerName', ((1, 'pbstr'),)))
    IUPnPDevice.get_ManufacturerURL = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'get_ManufacturerURL', ((1, 'pbstr'),)))
    IUPnPDevice.get_ModelName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(18, 'get_ModelName', ((1, 'pbstr'),)))
    IUPnPDevice.get_ModelNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(19, 'get_ModelNumber', ((1, 'pbstr'),)))
    IUPnPDevice.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(20, 'get_Description', ((1, 'pbstr'),)))
    IUPnPDevice.get_ModelURL = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(21, 'get_ModelURL', ((1, 'pbstr'),)))
    IUPnPDevice.get_UPC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(22, 'get_UPC', ((1, 'pbstr'),)))
    IUPnPDevice.get_SerialNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(23, 'get_SerialNumber', ((1, 'pbstr'),)))
    IUPnPDevice.IconURL = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,Int32,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(24, 'IconURL', ((1, 'bstrEncodingFormat'),(1, 'lSizeX'),(1, 'lSizeY'),(1, 'lBitDepth'),(1, 'pbstrIconURL'),)))
    IUPnPDevice.get_Services = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Enumeration.Pnp.IUPnPServices_head), use_last_error=False)(25, 'get_Services', ((1, 'ppusServices'),)))
    win32more.System.Com.IDispatch
    return IUPnPDevice
def _define_IUPnPDeviceDocumentAccess_head():
    class IUPnPDeviceDocumentAccess(win32more.System.Com.IUnknown_head):
        Guid = Guid('e7772804-3287-418e-9072-cf2b47238981')
    return IUPnPDeviceDocumentAccess
def _define_IUPnPDeviceDocumentAccess():
    IUPnPDeviceDocumentAccess = win32more.Devices.Enumeration.Pnp.IUPnPDeviceDocumentAccess_head
    IUPnPDeviceDocumentAccess.GetDocumentURL = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'GetDocumentURL', ((1, 'pbstrDocument'),)))
    win32more.System.Com.IUnknown
    return IUPnPDeviceDocumentAccess
def _define_IUPnPDeviceDocumentAccessEx_head():
    class IUPnPDeviceDocumentAccessEx(win32more.System.Com.IUnknown_head):
        Guid = Guid('c4bc4050-6178-4bd1-a4b8-6398321f3247')
    return IUPnPDeviceDocumentAccessEx
def _define_IUPnPDeviceDocumentAccessEx():
    IUPnPDeviceDocumentAccessEx = win32more.Devices.Enumeration.Pnp.IUPnPDeviceDocumentAccessEx_head
    IUPnPDeviceDocumentAccessEx.GetDocument = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'GetDocument', ((1, 'pbstrDocument'),)))
    win32more.System.Com.IUnknown
    return IUPnPDeviceDocumentAccessEx
def _define_IUPnPDescriptionDocument_head():
    class IUPnPDescriptionDocument(win32more.System.Com.IDispatch_head):
        Guid = Guid('11d1c1b2-7daa-4c9e-9595-7f82ed206d1e')
    return IUPnPDescriptionDocument
def _define_IUPnPDescriptionDocument():
    IUPnPDescriptionDocument = win32more.Devices.Enumeration.Pnp.IUPnPDescriptionDocument_head
    IUPnPDescriptionDocument.get_ReadyState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_ReadyState', ((1, 'plReadyState'),)))
    IUPnPDescriptionDocument.Load = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'Load', ((1, 'bstrUrl'),)))
    IUPnPDescriptionDocument.LoadAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.IUnknown_head, use_last_error=False)(9, 'LoadAsync', ((1, 'bstrUrl'),(1, 'punkCallback'),)))
    IUPnPDescriptionDocument.get_LoadResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_LoadResult', ((1, 'phrError'),)))
    IUPnPDescriptionDocument.Abort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'Abort', ()))
    IUPnPDescriptionDocument.RootDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Enumeration.Pnp.IUPnPDevice_head), use_last_error=False)(12, 'RootDevice', ((1, 'ppudRootDevice'),)))
    IUPnPDescriptionDocument.DeviceByUDN = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Devices.Enumeration.Pnp.IUPnPDevice_head), use_last_error=False)(13, 'DeviceByUDN', ((1, 'bstrUDN'),(1, 'ppudDevice'),)))
    win32more.System.Com.IDispatch
    return IUPnPDescriptionDocument
def _define_IUPnPDeviceFinderAddCallbackWithInterface_head():
    class IUPnPDeviceFinderAddCallbackWithInterface(win32more.System.Com.IUnknown_head):
        Guid = Guid('983dfc0b-1796-44df-8975-ca545b620ee5')
    return IUPnPDeviceFinderAddCallbackWithInterface
def _define_IUPnPDeviceFinderAddCallbackWithInterface():
    IUPnPDeviceFinderAddCallbackWithInterface = win32more.Devices.Enumeration.Pnp.IUPnPDeviceFinderAddCallbackWithInterface_head
    IUPnPDeviceFinderAddCallbackWithInterface.DeviceAddedWithInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Devices.Enumeration.Pnp.IUPnPDevice_head,POINTER(Guid), use_last_error=False)(3, 'DeviceAddedWithInterface', ((1, 'lFindData'),(1, 'pDevice'),(1, 'pguidInterface'),)))
    win32more.System.Com.IUnknown
    return IUPnPDeviceFinderAddCallbackWithInterface
def _define_IUPnPDescriptionDocumentCallback_head():
    class IUPnPDescriptionDocumentCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('77394c69-5486-40d6-9bc3-4991983e02da')
    return IUPnPDescriptionDocumentCallback
def _define_IUPnPDescriptionDocumentCallback():
    IUPnPDescriptionDocumentCallback = win32more.Devices.Enumeration.Pnp.IUPnPDescriptionDocumentCallback_head
    IUPnPDescriptionDocumentCallback.LoadComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT, use_last_error=False)(3, 'LoadComplete', ((1, 'hrLoadResult'),)))
    win32more.System.Com.IUnknown
    return IUPnPDescriptionDocumentCallback
UPnPRegistrar = Guid('204810b9-73b2-11d4-bf42-00b0d0118b56')
UPnPRemoteEndpointInfo = Guid('2e5e84e9-4049-4244-b728-2d24227157c7')
def _define_IUPnPEventSink_head():
    class IUPnPEventSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('204810b4-73b2-11d4-bf42-00b0d0118b56')
    return IUPnPEventSink
def _define_IUPnPEventSink():
    IUPnPEventSink = win32more.Devices.Enumeration.Pnp.IUPnPEventSink_head
    IUPnPEventSink.OnStateChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Int32), use_last_error=False)(3, 'OnStateChanged', ((1, 'cChanges'),(1, 'rgdispidChanges'),)))
    IUPnPEventSink.OnStateChangedSafe = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(4, 'OnStateChangedSafe', ((1, 'varsadispidChanges'),)))
    win32more.System.Com.IUnknown
    return IUPnPEventSink
def _define_IUPnPEventSource_head():
    class IUPnPEventSource(win32more.System.Com.IUnknown_head):
        Guid = Guid('204810b5-73b2-11d4-bf42-00b0d0118b56')
    return IUPnPEventSource
def _define_IUPnPEventSource():
    IUPnPEventSource = win32more.Devices.Enumeration.Pnp.IUPnPEventSource_head
    IUPnPEventSource.Advise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Enumeration.Pnp.IUPnPEventSink_head, use_last_error=False)(3, 'Advise', ((1, 'pesSubscriber'),)))
    IUPnPEventSource.Unadvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Enumeration.Pnp.IUPnPEventSink_head, use_last_error=False)(4, 'Unadvise', ((1, 'pesSubscriber'),)))
    win32more.System.Com.IUnknown
    return IUPnPEventSource
def _define_IUPnPRegistrar_head():
    class IUPnPRegistrar(win32more.System.Com.IUnknown_head):
        Guid = Guid('204810b6-73b2-11d4-bf42-00b0d0118b56')
    return IUPnPRegistrar
def _define_IUPnPRegistrar():
    IUPnPRegistrar = win32more.Devices.Enumeration.Pnp.IUPnPRegistrar_head
    IUPnPRegistrar.RegisterDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'RegisterDevice', ((1, 'bstrXMLDesc'),(1, 'bstrProgIDDeviceControlClass'),(1, 'bstrInitString'),(1, 'bstrContainerId'),(1, 'bstrResourcePath'),(1, 'nLifeTime'),(1, 'pbstrDeviceIdentifier'),)))
    IUPnPRegistrar.RegisterRunningDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.IUnknown_head,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'RegisterRunningDevice', ((1, 'bstrXMLDesc'),(1, 'punkDeviceControl'),(1, 'bstrInitString'),(1, 'bstrResourcePath'),(1, 'nLifeTime'),(1, 'pbstrDeviceIdentifier'),)))
    IUPnPRegistrar.RegisterDeviceProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(5, 'RegisterDeviceProvider', ((1, 'bstrProviderName'),(1, 'bstrProgIDProviderClass'),(1, 'bstrInitString'),(1, 'bstrContainerId'),)))
    IUPnPRegistrar.GetUniqueDeviceName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(6, 'GetUniqueDeviceName', ((1, 'bstrDeviceIdentifier'),(1, 'bstrTemplateUDN'),(1, 'pbstrUDN'),)))
    IUPnPRegistrar.UnregisterDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BOOL, use_last_error=False)(7, 'UnregisterDevice', ((1, 'bstrDeviceIdentifier'),(1, 'fPermanent'),)))
    IUPnPRegistrar.UnregisterDeviceProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'UnregisterDeviceProvider', ((1, 'bstrProviderName'),)))
    win32more.System.Com.IUnknown
    return IUPnPRegistrar
def _define_IUPnPReregistrar_head():
    class IUPnPReregistrar(win32more.System.Com.IUnknown_head):
        Guid = Guid('204810b7-73b2-11d4-bf42-00b0d0118b56')
    return IUPnPReregistrar
def _define_IUPnPReregistrar():
    IUPnPReregistrar = win32more.Devices.Enumeration.Pnp.IUPnPReregistrar_head
    IUPnPReregistrar.ReregisterDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32, use_last_error=False)(3, 'ReregisterDevice', ((1, 'bstrDeviceIdentifier'),(1, 'bstrXMLDesc'),(1, 'bstrProgIDDeviceControlClass'),(1, 'bstrInitString'),(1, 'bstrContainerId'),(1, 'bstrResourcePath'),(1, 'nLifeTime'),)))
    IUPnPReregistrar.ReregisterRunningDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.System.Com.IUnknown_head,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32, use_last_error=False)(4, 'ReregisterRunningDevice', ((1, 'bstrDeviceIdentifier'),(1, 'bstrXMLDesc'),(1, 'punkDeviceControl'),(1, 'bstrInitString'),(1, 'bstrResourcePath'),(1, 'nLifeTime'),)))
    win32more.System.Com.IUnknown
    return IUPnPReregistrar
def _define_IUPnPDeviceControl_head():
    class IUPnPDeviceControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('204810ba-73b2-11d4-bf42-00b0d0118b56')
    return IUPnPDeviceControl
def _define_IUPnPDeviceControl():
    IUPnPDeviceControl = win32more.Devices.Enumeration.Pnp.IUPnPDeviceControl_head
    IUPnPDeviceControl.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(3, 'Initialize', ((1, 'bstrXMLDesc'),(1, 'bstrDeviceIdentifier'),(1, 'bstrInitString'),)))
    IUPnPDeviceControl.GetServiceObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(4, 'GetServiceObject', ((1, 'bstrUDN'),(1, 'bstrServiceId'),(1, 'ppdispService'),)))
    win32more.System.Com.IUnknown
    return IUPnPDeviceControl
def _define_IUPnPDeviceControlHttpHeaders_head():
    class IUPnPDeviceControlHttpHeaders(win32more.System.Com.IUnknown_head):
        Guid = Guid('204810bb-73b2-11d4-bf42-00b0d0118b56')
    return IUPnPDeviceControlHttpHeaders
def _define_IUPnPDeviceControlHttpHeaders():
    IUPnPDeviceControlHttpHeaders = win32more.Devices.Enumeration.Pnp.IUPnPDeviceControlHttpHeaders_head
    IUPnPDeviceControlHttpHeaders.GetAdditionalResponseHeaders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'GetAdditionalResponseHeaders', ((1, 'bstrHttpResponseHeaders'),)))
    win32more.System.Com.IUnknown
    return IUPnPDeviceControlHttpHeaders
def _define_IUPnPDeviceProvider_head():
    class IUPnPDeviceProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('204810b8-73b2-11d4-bf42-00b0d0118b56')
    return IUPnPDeviceProvider
def _define_IUPnPDeviceProvider():
    IUPnPDeviceProvider = win32more.Devices.Enumeration.Pnp.IUPnPDeviceProvider_head
    IUPnPDeviceProvider.Start = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(3, 'Start', ((1, 'bstrInitString'),)))
    IUPnPDeviceProvider.Stop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Stop', ()))
    win32more.System.Com.IUnknown
    return IUPnPDeviceProvider
def _define_IUPnPRemoteEndpointInfo_head():
    class IUPnPRemoteEndpointInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('c92eb863-0269-4aff-9c72-75321bba2952')
    return IUPnPRemoteEndpointInfo
def _define_IUPnPRemoteEndpointInfo():
    IUPnPRemoteEndpointInfo = win32more.Devices.Enumeration.Pnp.IUPnPRemoteEndpointInfo_head
    IUPnPRemoteEndpointInfo.GetDwordValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(UInt32), use_last_error=False)(3, 'GetDwordValue', ((1, 'bstrValueName'),(1, 'pdwValue'),)))
    IUPnPRemoteEndpointInfo.GetStringValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'GetStringValue', ((1, 'bstrValueName'),(1, 'pbstrValue'),)))
    IUPnPRemoteEndpointInfo.GetGuidValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(Guid), use_last_error=False)(5, 'GetGuidValue', ((1, 'bstrValueName'),(1, 'pguidValue'),)))
    win32more.System.Com.IUnknown
    return IUPnPRemoteEndpointInfo
def _define_SwDeviceCreate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Devices.Enumeration.Pnp.SW_DEVICE_CREATE_INFO_head),UInt32,POINTER(win32more.Devices.Properties.DEVPROPERTY),win32more.Devices.Enumeration.Pnp.SW_DEVICE_CREATE_CALLBACK,c_void_p,POINTER(IntPtr), use_last_error=False)(("SwDeviceCreate", windll["CFGMGR32"]), ((1, 'pszEnumeratorName'),(1, 'pszParentDeviceInstance'),(1, 'pCreateInfo'),(1, 'cPropertyCount'),(1, 'pProperties'),(1, 'pCallback'),(1, 'pContext'),(1, 'phSwDevice'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SwDeviceClose():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.Enumeration.Pnp.HSWDEVICE, use_last_error=False)(("SwDeviceClose", windll["CFGMGR32"]), ((1, 'hSwDevice'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SwDeviceSetLifetime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Enumeration.Pnp.HSWDEVICE,win32more.Devices.Enumeration.Pnp.SW_DEVICE_LIFETIME, use_last_error=False)(("SwDeviceSetLifetime", windll["CFGMGR32"]), ((1, 'hSwDevice'),(1, 'Lifetime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SwDeviceGetLifetime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Enumeration.Pnp.HSWDEVICE,POINTER(win32more.Devices.Enumeration.Pnp.SW_DEVICE_LIFETIME), use_last_error=False)(("SwDeviceGetLifetime", windll["CFGMGR32"]), ((1, 'hSwDevice'),(1, 'pLifetime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SwDevicePropertySet():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Enumeration.Pnp.HSWDEVICE,UInt32,POINTER(win32more.Devices.Properties.DEVPROPERTY), use_last_error=False)(("SwDevicePropertySet", windll["CFGMGR32"]), ((1, 'hSwDevice'),(1, 'cPropertyCount'),(1, 'pProperties'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SwDeviceInterfaceRegister():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Enumeration.Pnp.HSWDEVICE,POINTER(Guid),win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Devices.Properties.DEVPROPERTY),win32more.Foundation.BOOL,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("SwDeviceInterfaceRegister", windll["CFGMGR32"]), ((1, 'hSwDevice'),(1, 'pInterfaceClassGuid'),(1, 'pszReferenceString'),(1, 'cPropertyCount'),(1, 'pProperties'),(1, 'fEnabled'),(1, 'ppszDeviceInterfaceId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SwMemFree():
    try:
        return WINFUNCTYPE(Void,c_void_p, use_last_error=False)(("SwMemFree", windll["CFGMGR32"]), ((1, 'pMem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SwDeviceInterfaceSetState():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Enumeration.Pnp.HSWDEVICE,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=False)(("SwDeviceInterfaceSetState", windll["CFGMGR32"]), ((1, 'hSwDevice'),(1, 'pszDeviceInterfaceId'),(1, 'fEnabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SwDeviceInterfacePropertySet():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Enumeration.Pnp.HSWDEVICE,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Devices.Properties.DEVPROPERTY), use_last_error=False)(("SwDeviceInterfacePropertySet", windll["CFGMGR32"]), ((1, 'hSwDevice'),(1, 'pszDeviceInterfaceId'),(1, 'cPropertyCount'),(1, 'pProperties'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "UPNP_E_ROOT_ELEMENT_EXPECTED",
    "UPNP_E_DEVICE_ELEMENT_EXPECTED",
    "UPNP_E_SERVICE_ELEMENT_EXPECTED",
    "UPNP_E_SERVICE_NODE_INCOMPLETE",
    "UPNP_E_DEVICE_NODE_INCOMPLETE",
    "UPNP_E_ICON_ELEMENT_EXPECTED",
    "UPNP_E_ICON_NODE_INCOMPLETE",
    "UPNP_E_INVALID_ACTION",
    "UPNP_E_INVALID_ARGUMENTS",
    "UPNP_E_OUT_OF_SYNC",
    "UPNP_E_ACTION_REQUEST_FAILED",
    "UPNP_E_TRANSPORT_ERROR",
    "UPNP_E_VARIABLE_VALUE_UNKNOWN",
    "UPNP_E_INVALID_VARIABLE",
    "UPNP_E_DEVICE_ERROR",
    "UPNP_E_PROTOCOL_ERROR",
    "UPNP_E_ERROR_PROCESSING_RESPONSE",
    "UPNP_E_DEVICE_TIMEOUT",
    "UPNP_E_INVALID_DOCUMENT",
    "UPNP_E_EVENT_SUBSCRIPTION_FAILED",
    "FAULT_INVALID_ACTION",
    "FAULT_INVALID_ARG",
    "FAULT_INVALID_SEQUENCE_NUMBER",
    "FAULT_INVALID_VARIABLE",
    "FAULT_DEVICE_INTERNAL_ERROR",
    "FAULT_ACTION_SPECIFIC_BASE",
    "FAULT_ACTION_SPECIFIC_MAX",
    "UPNP_E_ACTION_SPECIFIC_BASE",
    "UPNP_ADDRESSFAMILY_IPv4",
    "UPNP_ADDRESSFAMILY_IPv6",
    "UPNP_ADDRESSFAMILY_BOTH",
    "UPNP_SERVICE_DELAY_SCPD_AND_SUBSCRIPTION",
    "UPNP_E_REQUIRED_ELEMENT_ERROR",
    "UPNP_E_DUPLICATE_NOT_ALLOWED",
    "UPNP_E_DUPLICATE_SERVICE_ID",
    "UPNP_E_INVALID_DESCRIPTION",
    "UPNP_E_INVALID_SERVICE",
    "UPNP_E_INVALID_ICON",
    "UPNP_E_INVALID_XML",
    "UPNP_E_INVALID_ROOT_NAMESPACE",
    "UPNP_E_SUFFIX_TOO_LONG",
    "UPNP_E_URLBASE_PRESENT",
    "UPNP_E_VALUE_TOO_LONG",
    "UPNP_E_DEVICE_RUNNING",
    "UPNP_E_DEVICE_NOTREGISTERED",
    "HSWDEVICE",
    "SW_DEVICE_CAPABILITIES",
    "SW_DEVICE_CAPABILITIES_SWDeviceCapabilitiesNone",
    "SW_DEVICE_CAPABILITIES_SWDeviceCapabilitiesRemovable",
    "SW_DEVICE_CAPABILITIES_SWDeviceCapabilitiesSilentInstall",
    "SW_DEVICE_CAPABILITIES_SWDeviceCapabilitiesNoDisplayInUI",
    "SW_DEVICE_CAPABILITIES_SWDeviceCapabilitiesDriverRequired",
    "SW_DEVICE_CREATE_INFO",
    "SW_DEVICE_LIFETIME",
    "SW_DEVICE_LIFETIME_SWDeviceLifetimeHandle",
    "SW_DEVICE_LIFETIME_SWDeviceLifetimeParentPresent",
    "SW_DEVICE_LIFETIME_SWDeviceLifetimeMax",
    "SW_DEVICE_CREATE_CALLBACK",
    "UPnPDeviceFinder",
    "UPnPDevices",
    "UPnPDevice",
    "UPnPServices",
    "UPnPService",
    "UPnPDescriptionDocument",
    "UPnPDeviceFinderEx",
    "UPnPDescriptionDocumentEx",
    "IUPnPDeviceFinder",
    "IUPnPAddressFamilyControl",
    "IUPnPHttpHeaderControl",
    "IUPnPDeviceFinderCallback",
    "IUPnPServices",
    "IUPnPService",
    "IUPnPAsyncResult",
    "IUPnPServiceAsync",
    "IUPnPServiceCallback",
    "IUPnPServiceEnumProperty",
    "IUPnPServiceDocumentAccess",
    "IUPnPDevices",
    "IUPnPDevice",
    "IUPnPDeviceDocumentAccess",
    "IUPnPDeviceDocumentAccessEx",
    "IUPnPDescriptionDocument",
    "IUPnPDeviceFinderAddCallbackWithInterface",
    "IUPnPDescriptionDocumentCallback",
    "UPnPRegistrar",
    "UPnPRemoteEndpointInfo",
    "IUPnPEventSink",
    "IUPnPEventSource",
    "IUPnPRegistrar",
    "IUPnPReregistrar",
    "IUPnPDeviceControl",
    "IUPnPDeviceControlHttpHeaders",
    "IUPnPDeviceProvider",
    "IUPnPRemoteEndpointInfo",
    "SwDeviceCreate",
    "SwDeviceClose",
    "SwDeviceSetLifetime",
    "SwDeviceGetLifetime",
    "SwDevicePropertySet",
    "SwDeviceInterfaceRegister",
    "SwMemFree",
    "SwDeviceInterfaceSetState",
    "SwDeviceInterfacePropertySet",
]
