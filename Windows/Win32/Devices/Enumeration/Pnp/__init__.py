from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Devices.Enumeration.Pnp
import Windows.Win32.Devices.Properties
import Windows.Win32.Foundation
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
UPNP_E_ROOT_ELEMENT_EXPECTED: Windows.Win32.Foundation.HRESULT = -2147220992
UPNP_E_DEVICE_ELEMENT_EXPECTED: Windows.Win32.Foundation.HRESULT = -2147220991
UPNP_E_SERVICE_ELEMENT_EXPECTED: Windows.Win32.Foundation.HRESULT = -2147220990
UPNP_E_SERVICE_NODE_INCOMPLETE: Windows.Win32.Foundation.HRESULT = -2147220989
UPNP_E_DEVICE_NODE_INCOMPLETE: Windows.Win32.Foundation.HRESULT = -2147220988
UPNP_E_ICON_ELEMENT_EXPECTED: Windows.Win32.Foundation.HRESULT = -2147220987
UPNP_E_ICON_NODE_INCOMPLETE: Windows.Win32.Foundation.HRESULT = -2147220986
UPNP_E_INVALID_ACTION: Windows.Win32.Foundation.HRESULT = -2147220985
UPNP_E_INVALID_ARGUMENTS: Windows.Win32.Foundation.HRESULT = -2147220984
UPNP_E_OUT_OF_SYNC: Windows.Win32.Foundation.HRESULT = -2147220983
UPNP_E_ACTION_REQUEST_FAILED: Windows.Win32.Foundation.HRESULT = -2147220976
UPNP_E_TRANSPORT_ERROR: Windows.Win32.Foundation.HRESULT = -2147220975
UPNP_E_VARIABLE_VALUE_UNKNOWN: Windows.Win32.Foundation.HRESULT = -2147220974
UPNP_E_INVALID_VARIABLE: Windows.Win32.Foundation.HRESULT = -2147220973
UPNP_E_DEVICE_ERROR: Windows.Win32.Foundation.HRESULT = -2147220972
UPNP_E_PROTOCOL_ERROR: Windows.Win32.Foundation.HRESULT = -2147220971
UPNP_E_ERROR_PROCESSING_RESPONSE: Windows.Win32.Foundation.HRESULT = -2147220970
UPNP_E_DEVICE_TIMEOUT: Windows.Win32.Foundation.HRESULT = -2147220969
UPNP_E_INVALID_DOCUMENT: Windows.Win32.Foundation.HRESULT = -2147220224
UPNP_E_EVENT_SUBSCRIPTION_FAILED: Windows.Win32.Foundation.HRESULT = -2147220223
FAULT_INVALID_ACTION: UInt32 = 401
FAULT_INVALID_ARG: UInt32 = 402
FAULT_INVALID_SEQUENCE_NUMBER: UInt32 = 403
FAULT_INVALID_VARIABLE: UInt32 = 404
FAULT_DEVICE_INTERNAL_ERROR: UInt32 = 501
FAULT_ACTION_SPECIFIC_BASE: UInt32 = 600
FAULT_ACTION_SPECIFIC_MAX: UInt32 = 899
UPNP_E_ACTION_SPECIFIC_BASE: Windows.Win32.Foundation.HRESULT = -2147220736
UPNP_ADDRESSFAMILY_IPv4: UInt32 = 1
UPNP_ADDRESSFAMILY_IPv6: UInt32 = 2
UPNP_ADDRESSFAMILY_BOTH: UInt32 = 3
UPNP_SERVICE_DELAY_SCPD_AND_SUBSCRIPTION: UInt32 = 1
UPNP_E_REQUIRED_ELEMENT_ERROR: Windows.Win32.Foundation.HRESULT = -2147180512
UPNP_E_DUPLICATE_NOT_ALLOWED: Windows.Win32.Foundation.HRESULT = -2147180511
UPNP_E_DUPLICATE_SERVICE_ID: Windows.Win32.Foundation.HRESULT = -2147180510
UPNP_E_INVALID_DESCRIPTION: Windows.Win32.Foundation.HRESULT = -2147180509
UPNP_E_INVALID_SERVICE: Windows.Win32.Foundation.HRESULT = -2147180508
UPNP_E_INVALID_ICON: Windows.Win32.Foundation.HRESULT = -2147180507
UPNP_E_INVALID_XML: Windows.Win32.Foundation.HRESULT = -2147180506
UPNP_E_INVALID_ROOT_NAMESPACE: Windows.Win32.Foundation.HRESULT = -2147180505
UPNP_E_SUFFIX_TOO_LONG: Windows.Win32.Foundation.HRESULT = -2147180504
UPNP_E_URLBASE_PRESENT: Windows.Win32.Foundation.HRESULT = -2147180503
UPNP_E_VALUE_TOO_LONG: Windows.Win32.Foundation.HRESULT = -2147180496
UPNP_E_DEVICE_RUNNING: Windows.Win32.Foundation.HRESULT = -2147180495
UPNP_E_DEVICE_NOTREGISTERED: Windows.Win32.Foundation.HRESULT = -2147180494
REMOTE_ADDRESS_VALUE_NAME: String = 'RemoteAddress'
ADDRESS_FAMILY_VALUE_NAME: String = 'AddressFamily'
@winfunctype('CFGMGR32.dll')
def SwDeviceCreate(pszEnumeratorName: Windows.Win32.Foundation.PWSTR, pszParentDeviceInstance: Windows.Win32.Foundation.PWSTR, pCreateInfo: POINTER(Windows.Win32.Devices.Enumeration.Pnp.SW_DEVICE_CREATE_INFO_head), cPropertyCount: UInt32, pProperties: POINTER(Windows.Win32.Devices.Properties.DEVPROPERTY_head), pCallback: Windows.Win32.Devices.Enumeration.Pnp.SW_DEVICE_CREATE_CALLBACK, pContext: c_void_p, phSwDevice: POINTER(IntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('CFGMGR32.dll')
def SwDeviceClose(hSwDevice: Windows.Win32.Devices.Enumeration.Pnp.HSWDEVICE) -> Void: ...
@winfunctype('CFGMGR32.dll')
def SwDeviceSetLifetime(hSwDevice: Windows.Win32.Devices.Enumeration.Pnp.HSWDEVICE, Lifetime: Windows.Win32.Devices.Enumeration.Pnp.SW_DEVICE_LIFETIME) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('CFGMGR32.dll')
def SwDeviceGetLifetime(hSwDevice: Windows.Win32.Devices.Enumeration.Pnp.HSWDEVICE, pLifetime: POINTER(Windows.Win32.Devices.Enumeration.Pnp.SW_DEVICE_LIFETIME)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('CFGMGR32.dll')
def SwDevicePropertySet(hSwDevice: Windows.Win32.Devices.Enumeration.Pnp.HSWDEVICE, cPropertyCount: UInt32, pProperties: POINTER(Windows.Win32.Devices.Properties.DEVPROPERTY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('CFGMGR32.dll')
def SwDeviceInterfaceRegister(hSwDevice: Windows.Win32.Devices.Enumeration.Pnp.HSWDEVICE, pInterfaceClassGuid: POINTER(Guid), pszReferenceString: Windows.Win32.Foundation.PWSTR, cPropertyCount: UInt32, pProperties: POINTER(Windows.Win32.Devices.Properties.DEVPROPERTY_head), fEnabled: Windows.Win32.Foundation.BOOL, ppszDeviceInterfaceId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('CFGMGR32.dll')
def SwMemFree(pMem: c_void_p) -> Void: ...
@winfunctype('CFGMGR32.dll')
def SwDeviceInterfaceSetState(hSwDevice: Windows.Win32.Devices.Enumeration.Pnp.HSWDEVICE, pszDeviceInterfaceId: Windows.Win32.Foundation.PWSTR, fEnabled: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('CFGMGR32.dll')
def SwDeviceInterfacePropertySet(hSwDevice: Windows.Win32.Devices.Enumeration.Pnp.HSWDEVICE, pszDeviceInterfaceId: Windows.Win32.Foundation.PWSTR, cPropertyCount: UInt32, pProperties: POINTER(Windows.Win32.Devices.Properties.DEVPROPERTY_head)) -> Windows.Win32.Foundation.HRESULT: ...
HSWDEVICE = IntPtr
class IUPnPAddressFamilyControl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e3bf6178-694e-459f-a5-a6-19-1e-a0-ff-a1-c7')
    @commethod(3)
    def SetAddressFamily(dwFlags: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAddressFamily(pdwFlags: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IUPnPAsyncResult(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4d65fd08-d13e-4274-9c-8b-dd-8d-02-8c-86-44')
    @commethod(3)
    def AsyncOperationComplete(ullRequestID: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
class IUPnPDescriptionDocument(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('11d1c1b2-7daa-4c9e-95-95-7f-82-ed-20-6d-1e')
    @commethod(7)
    def get_ReadyState(plReadyState: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Load(bstrUrl: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def LoadAsync(bstrUrl: Windows.Win32.Foundation.BSTR, punkCallback: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_LoadResult(phrError: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Abort() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RootDevice(ppudRootDevice: POINTER(Windows.Win32.Devices.Enumeration.Pnp.IUPnPDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def DeviceByUDN(bstrUDN: Windows.Win32.Foundation.BSTR, ppudDevice: POINTER(Windows.Win32.Devices.Enumeration.Pnp.IUPnPDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUPnPDescriptionDocumentCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('77394c69-5486-40d6-9b-c3-49-91-98-3e-02-da')
    @commethod(3)
    def LoadComplete(hrLoadResult: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class IUPnPDevice(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('3d44d0d1-98c9-4889-ac-d1-f9-d6-74-bf-22-21')
    @commethod(7)
    def get_IsRootDevice(pvarb: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_RootDevice(ppudRootDevice: POINTER(Windows.Win32.Devices.Enumeration.Pnp.IUPnPDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ParentDevice(ppudDeviceParent: POINTER(Windows.Win32.Devices.Enumeration.Pnp.IUPnPDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_HasChildren(pvarb: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Children(ppudChildren: POINTER(Windows.Win32.Devices.Enumeration.Pnp.IUPnPDevices_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_UniqueDeviceName(pbstr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_FriendlyName(pbstr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Type(pbstr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_PresentationURL(pbstr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_ManufacturerName(pbstr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_ManufacturerURL(pbstr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_ModelName(pbstr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_ModelNumber(pbstr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_Description(pbstr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_ModelURL(pbstr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_UPC(pbstr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_SerialNumber(pbstr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def IconURL(bstrEncodingFormat: Windows.Win32.Foundation.BSTR, lSizeX: Int32, lSizeY: Int32, lBitDepth: Int32, pbstrIconURL: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_Services(ppusServices: POINTER(Windows.Win32.Devices.Enumeration.Pnp.IUPnPServices_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUPnPDeviceControl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('204810ba-73b2-11d4-bf-42-00-b0-d0-11-8b-56')
    @commethod(3)
    def Initialize(bstrXMLDesc: Windows.Win32.Foundation.BSTR, bstrDeviceIdentifier: Windows.Win32.Foundation.BSTR, bstrInitString: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetServiceObject(bstrUDN: Windows.Win32.Foundation.BSTR, bstrServiceId: Windows.Win32.Foundation.BSTR, ppdispService: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUPnPDeviceControlHttpHeaders(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('204810bb-73b2-11d4-bf-42-00-b0-d0-11-8b-56')
    @commethod(3)
    def GetAdditionalResponseHeaders(bstrHttpResponseHeaders: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IUPnPDeviceDocumentAccess(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e7772804-3287-418e-90-72-cf-2b-47-23-89-81')
    @commethod(3)
    def GetDocumentURL(pbstrDocument: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IUPnPDeviceDocumentAccessEx(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c4bc4050-6178-4bd1-a4-b8-63-98-32-1f-32-47')
    @commethod(3)
    def GetDocument(pbstrDocument: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IUPnPDeviceFinder(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('adda3d55-6f72-4319-bf-f9-18-60-0a-53-9b-10')
    @commethod(7)
    def FindByType(bstrTypeURI: Windows.Win32.Foundation.BSTR, dwFlags: UInt32, pDevices: POINTER(Windows.Win32.Devices.Enumeration.Pnp.IUPnPDevices_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateAsyncFind(bstrTypeURI: Windows.Win32.Foundation.BSTR, dwFlags: UInt32, punkDeviceFinderCallback: Windows.Win32.System.Com.IUnknown_head, plFindData: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def StartAsyncFind(lFindData: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CancelAsyncFind(lFindData: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def FindByUDN(bstrUDN: Windows.Win32.Foundation.BSTR, pDevice: POINTER(Windows.Win32.Devices.Enumeration.Pnp.IUPnPDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUPnPDeviceFinderAddCallbackWithInterface(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('983dfc0b-1796-44df-89-75-ca-54-5b-62-0e-e5')
    @commethod(3)
    def DeviceAddedWithInterface(lFindData: Int32, pDevice: Windows.Win32.Devices.Enumeration.Pnp.IUPnPDevice_head, pguidInterface: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IUPnPDeviceFinderCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('415a984a-88b3-49f3-92-af-05-08-be-df-0d-6c')
    @commethod(3)
    def DeviceAdded(lFindData: Int32, pDevice: Windows.Win32.Devices.Enumeration.Pnp.IUPnPDevice_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DeviceRemoved(lFindData: Int32, bstrUDN: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SearchComplete(lFindData: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IUPnPDeviceProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('204810b8-73b2-11d4-bf-42-00-b0-d0-11-8b-56')
    @commethod(3)
    def Start(bstrInitString: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Stop() -> Windows.Win32.Foundation.HRESULT: ...
class IUPnPDevices(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('fdbc0c73-bda3-4c66-ac-4f-f2-d9-6f-da-d6-8c')
    @commethod(7)
    def get_Count(plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(ppunk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Item(bstrUDN: Windows.Win32.Foundation.BSTR, ppDevice: POINTER(Windows.Win32.Devices.Enumeration.Pnp.IUPnPDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUPnPEventSink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('204810b4-73b2-11d4-bf-42-00-b0-d0-11-8b-56')
    @commethod(3)
    def OnStateChanged(cChanges: UInt32, rgdispidChanges: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnStateChangedSafe(varsadispidChanges: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class IUPnPEventSource(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('204810b5-73b2-11d4-bf-42-00-b0-d0-11-8b-56')
    @commethod(3)
    def Advise(pesSubscriber: Windows.Win32.Devices.Enumeration.Pnp.IUPnPEventSink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unadvise(pesSubscriber: Windows.Win32.Devices.Enumeration.Pnp.IUPnPEventSink_head) -> Windows.Win32.Foundation.HRESULT: ...
class IUPnPHttpHeaderControl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0405af4f-8b5c-447c-80-f2-b7-59-84-a3-1f-3c')
    @commethod(3)
    def AddRequestHeaders(bstrHttpHeaders: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IUPnPRegistrar(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('204810b6-73b2-11d4-bf-42-00-b0-d0-11-8b-56')
    @commethod(3)
    def RegisterDevice(bstrXMLDesc: Windows.Win32.Foundation.BSTR, bstrProgIDDeviceControlClass: Windows.Win32.Foundation.BSTR, bstrInitString: Windows.Win32.Foundation.BSTR, bstrContainerId: Windows.Win32.Foundation.BSTR, bstrResourcePath: Windows.Win32.Foundation.BSTR, nLifeTime: Int32, pbstrDeviceIdentifier: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RegisterRunningDevice(bstrXMLDesc: Windows.Win32.Foundation.BSTR, punkDeviceControl: Windows.Win32.System.Com.IUnknown_head, bstrInitString: Windows.Win32.Foundation.BSTR, bstrResourcePath: Windows.Win32.Foundation.BSTR, nLifeTime: Int32, pbstrDeviceIdentifier: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RegisterDeviceProvider(bstrProviderName: Windows.Win32.Foundation.BSTR, bstrProgIDProviderClass: Windows.Win32.Foundation.BSTR, bstrInitString: Windows.Win32.Foundation.BSTR, bstrContainerId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetUniqueDeviceName(bstrDeviceIdentifier: Windows.Win32.Foundation.BSTR, bstrTemplateUDN: Windows.Win32.Foundation.BSTR, pbstrUDN: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UnregisterDevice(bstrDeviceIdentifier: Windows.Win32.Foundation.BSTR, fPermanent: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UnregisterDeviceProvider(bstrProviderName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IUPnPRemoteEndpointInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c92eb863-0269-4aff-9c-72-75-32-1b-ba-29-52')
    @commethod(3)
    def GetDwordValue(bstrValueName: Windows.Win32.Foundation.BSTR, pdwValue: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetStringValue(bstrValueName: Windows.Win32.Foundation.BSTR, pbstrValue: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetGuidValue(bstrValueName: Windows.Win32.Foundation.BSTR, pguidValue: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IUPnPReregistrar(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('204810b7-73b2-11d4-bf-42-00-b0-d0-11-8b-56')
    @commethod(3)
    def ReregisterDevice(bstrDeviceIdentifier: Windows.Win32.Foundation.BSTR, bstrXMLDesc: Windows.Win32.Foundation.BSTR, bstrProgIDDeviceControlClass: Windows.Win32.Foundation.BSTR, bstrInitString: Windows.Win32.Foundation.BSTR, bstrContainerId: Windows.Win32.Foundation.BSTR, bstrResourcePath: Windows.Win32.Foundation.BSTR, nLifeTime: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReregisterRunningDevice(bstrDeviceIdentifier: Windows.Win32.Foundation.BSTR, bstrXMLDesc: Windows.Win32.Foundation.BSTR, punkDeviceControl: Windows.Win32.System.Com.IUnknown_head, bstrInitString: Windows.Win32.Foundation.BSTR, bstrResourcePath: Windows.Win32.Foundation.BSTR, nLifeTime: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IUPnPService(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('a295019c-dc65-47dd-90-dc-7f-e9-18-a1-ab-44')
    @commethod(7)
    def QueryStateVariable(bstrVariableName: Windows.Win32.Foundation.BSTR, pValue: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def InvokeAction(bstrActionName: Windows.Win32.Foundation.BSTR, vInActionArgs: Windows.Win32.System.Com.VARIANT, pvOutActionArgs: POINTER(Windows.Win32.System.Com.VARIANT_head), pvRetVal: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ServiceTypeIdentifier(pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def AddCallback(pUnkCallback: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Id(pbstrId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_LastTransportStatus(plValue: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IUPnPServiceAsync(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('098bdaf5-5ec1-49e7-a2-60-b3-a1-1d-d8-68-0c')
    @commethod(3)
    def BeginInvokeAction(bstrActionName: Windows.Win32.Foundation.BSTR, vInActionArgs: Windows.Win32.System.Com.VARIANT, pAsyncResult: Windows.Win32.Devices.Enumeration.Pnp.IUPnPAsyncResult_head, pullRequestID: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EndInvokeAction(ullRequestID: UInt64, pvOutActionArgs: POINTER(Windows.Win32.System.Com.VARIANT_head), pvRetVal: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def BeginQueryStateVariable(bstrVariableName: Windows.Win32.Foundation.BSTR, pAsyncResult: Windows.Win32.Devices.Enumeration.Pnp.IUPnPAsyncResult_head, pullRequestID: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EndQueryStateVariable(ullRequestID: UInt64, pValue: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def BeginSubscribeToEvents(pUnkCallback: Windows.Win32.System.Com.IUnknown_head, pAsyncResult: Windows.Win32.Devices.Enumeration.Pnp.IUPnPAsyncResult_head, pullRequestID: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def EndSubscribeToEvents(ullRequestID: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def BeginSCPDDownload(pAsyncResult: Windows.Win32.Devices.Enumeration.Pnp.IUPnPAsyncResult_head, pullRequestID: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EndSCPDDownload(ullRequestID: UInt64, pbstrSCPDDoc: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CancelAsyncOperation(ullRequestID: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
class IUPnPServiceCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('31fadca9-ab73-464b-b6-7d-5c-1d-0f-83-c8-b8')
    @commethod(3)
    def StateVariableChanged(pus: Windows.Win32.Devices.Enumeration.Pnp.IUPnPService_head, pcwszStateVarName: Windows.Win32.Foundation.PWSTR, vaValue: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ServiceInstanceDied(pus: Windows.Win32.Devices.Enumeration.Pnp.IUPnPService_head) -> Windows.Win32.Foundation.HRESULT: ...
class IUPnPServiceDocumentAccess(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('21905529-0a5e-4589-82-5d-7e-6d-87-ea-69-98')
    @commethod(3)
    def GetDocumentURL(pbstrDocUrl: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDocument(pbstrDoc: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IUPnPServiceEnumProperty(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('38873b37-91bb-49f4-b2-49-2e-8e-fb-b8-a8-16')
    @commethod(3)
    def SetServiceEnumProperty(dwMask: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IUPnPServices(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('3f8c8e9e-9a7a-4dc8-bc-41-ff-31-fa-37-49-56')
    @commethod(7)
    def get_Count(plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(ppunk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Item(bstrServiceId: Windows.Win32.Foundation.BSTR, ppService: POINTER(Windows.Win32.Devices.Enumeration.Pnp.IUPnPService_head)) -> Windows.Win32.Foundation.HRESULT: ...
SW_DEVICE_CAPABILITIES = Int32
SW_DEVICE_CAPABILITIES_SWDeviceCapabilitiesNone: SW_DEVICE_CAPABILITIES = 0
SW_DEVICE_CAPABILITIES_SWDeviceCapabilitiesRemovable: SW_DEVICE_CAPABILITIES = 1
SW_DEVICE_CAPABILITIES_SWDeviceCapabilitiesSilentInstall: SW_DEVICE_CAPABILITIES = 2
SW_DEVICE_CAPABILITIES_SWDeviceCapabilitiesNoDisplayInUI: SW_DEVICE_CAPABILITIES = 4
SW_DEVICE_CAPABILITIES_SWDeviceCapabilitiesDriverRequired: SW_DEVICE_CAPABILITIES = 8
@winfunctype_pointer
def SW_DEVICE_CREATE_CALLBACK(hSwDevice: Windows.Win32.Devices.Enumeration.Pnp.HSWDEVICE, CreateResult: Windows.Win32.Foundation.HRESULT, pContext: c_void_p, pszDeviceInstanceId: Windows.Win32.Foundation.PWSTR) -> Void: ...
class SW_DEVICE_CREATE_INFO(Structure):
    cbSize: UInt32
    pszInstanceId: Windows.Win32.Foundation.PWSTR
    pszzHardwareIds: Windows.Win32.Foundation.PWSTR
    pszzCompatibleIds: Windows.Win32.Foundation.PWSTR
    pContainerId: POINTER(Guid)
    CapabilityFlags: UInt32
    pszDeviceDescription: Windows.Win32.Foundation.PWSTR
    pszDeviceLocation: Windows.Win32.Foundation.PWSTR
    pSecurityDescriptor: POINTER(Windows.Win32.Security.SECURITY_DESCRIPTOR_head)
SW_DEVICE_LIFETIME = Int32
SW_DEVICE_LIFETIME_SWDeviceLifetimeHandle: SW_DEVICE_LIFETIME = 0
SW_DEVICE_LIFETIME_SWDeviceLifetimeParentPresent: SW_DEVICE_LIFETIME = 1
SW_DEVICE_LIFETIME_SWDeviceLifetimeMax: SW_DEVICE_LIFETIME = 2
UPnPDescriptionDocument = Guid('1d8a9b47-3a28-4ce2-8a-4b-bd-34-e4-5b-ce-eb')
UPnPDescriptionDocumentEx = Guid('33fd0563-d81a-4393-83-cc-01-95-b1-da-2f-91')
UPnPDevice = Guid('a32552c5-ba61-457a-b5-9a-a2-56-1e-12-5e-33')
UPnPDeviceFinder = Guid('e2085f28-feb7-404a-b8-e7-e6-59-bd-ea-aa-02')
UPnPDeviceFinderEx = Guid('181b54fc-380b-4a75-b3-f1-4a-c4-5e-96-05-b0')
UPnPDevices = Guid('b9e84ffd-ad3c-40a4-b8-35-08-82-eb-cb-aa-a8')
UPnPRegistrar = Guid('204810b9-73b2-11d4-bf-42-00-b0-d0-11-8b-56')
UPnPRemoteEndpointInfo = Guid('2e5e84e9-4049-4244-b7-28-2d-24-22-71-57-c7')
UPnPService = Guid('c624ba95-fbcb-4409-8c-03-8c-ce-ec-53-3e-f1')
UPnPServices = Guid('c0bc4b4a-a406-4efc-93-2f-b8-54-6b-81-00-cc')
make_head(_module, 'IUPnPAddressFamilyControl')
make_head(_module, 'IUPnPAsyncResult')
make_head(_module, 'IUPnPDescriptionDocument')
make_head(_module, 'IUPnPDescriptionDocumentCallback')
make_head(_module, 'IUPnPDevice')
make_head(_module, 'IUPnPDeviceControl')
make_head(_module, 'IUPnPDeviceControlHttpHeaders')
make_head(_module, 'IUPnPDeviceDocumentAccess')
make_head(_module, 'IUPnPDeviceDocumentAccessEx')
make_head(_module, 'IUPnPDeviceFinder')
make_head(_module, 'IUPnPDeviceFinderAddCallbackWithInterface')
make_head(_module, 'IUPnPDeviceFinderCallback')
make_head(_module, 'IUPnPDeviceProvider')
make_head(_module, 'IUPnPDevices')
make_head(_module, 'IUPnPEventSink')
make_head(_module, 'IUPnPEventSource')
make_head(_module, 'IUPnPHttpHeaderControl')
make_head(_module, 'IUPnPRegistrar')
make_head(_module, 'IUPnPRemoteEndpointInfo')
make_head(_module, 'IUPnPReregistrar')
make_head(_module, 'IUPnPService')
make_head(_module, 'IUPnPServiceAsync')
make_head(_module, 'IUPnPServiceCallback')
make_head(_module, 'IUPnPServiceDocumentAccess')
make_head(_module, 'IUPnPServiceEnumProperty')
make_head(_module, 'IUPnPServices')
make_head(_module, 'SW_DEVICE_CREATE_CALLBACK')
make_head(_module, 'SW_DEVICE_CREATE_INFO')
__all__ = [
    "ADDRESS_FAMILY_VALUE_NAME",
    "FAULT_ACTION_SPECIFIC_BASE",
    "FAULT_ACTION_SPECIFIC_MAX",
    "FAULT_DEVICE_INTERNAL_ERROR",
    "FAULT_INVALID_ACTION",
    "FAULT_INVALID_ARG",
    "FAULT_INVALID_SEQUENCE_NUMBER",
    "FAULT_INVALID_VARIABLE",
    "HSWDEVICE",
    "IUPnPAddressFamilyControl",
    "IUPnPAsyncResult",
    "IUPnPDescriptionDocument",
    "IUPnPDescriptionDocumentCallback",
    "IUPnPDevice",
    "IUPnPDeviceControl",
    "IUPnPDeviceControlHttpHeaders",
    "IUPnPDeviceDocumentAccess",
    "IUPnPDeviceDocumentAccessEx",
    "IUPnPDeviceFinder",
    "IUPnPDeviceFinderAddCallbackWithInterface",
    "IUPnPDeviceFinderCallback",
    "IUPnPDeviceProvider",
    "IUPnPDevices",
    "IUPnPEventSink",
    "IUPnPEventSource",
    "IUPnPHttpHeaderControl",
    "IUPnPRegistrar",
    "IUPnPRemoteEndpointInfo",
    "IUPnPReregistrar",
    "IUPnPService",
    "IUPnPServiceAsync",
    "IUPnPServiceCallback",
    "IUPnPServiceDocumentAccess",
    "IUPnPServiceEnumProperty",
    "IUPnPServices",
    "REMOTE_ADDRESS_VALUE_NAME",
    "SW_DEVICE_CAPABILITIES",
    "SW_DEVICE_CAPABILITIES_SWDeviceCapabilitiesDriverRequired",
    "SW_DEVICE_CAPABILITIES_SWDeviceCapabilitiesNoDisplayInUI",
    "SW_DEVICE_CAPABILITIES_SWDeviceCapabilitiesNone",
    "SW_DEVICE_CAPABILITIES_SWDeviceCapabilitiesRemovable",
    "SW_DEVICE_CAPABILITIES_SWDeviceCapabilitiesSilentInstall",
    "SW_DEVICE_CREATE_CALLBACK",
    "SW_DEVICE_CREATE_INFO",
    "SW_DEVICE_LIFETIME",
    "SW_DEVICE_LIFETIME_SWDeviceLifetimeHandle",
    "SW_DEVICE_LIFETIME_SWDeviceLifetimeMax",
    "SW_DEVICE_LIFETIME_SWDeviceLifetimeParentPresent",
    "SwDeviceClose",
    "SwDeviceCreate",
    "SwDeviceGetLifetime",
    "SwDeviceInterfacePropertySet",
    "SwDeviceInterfaceRegister",
    "SwDeviceInterfaceSetState",
    "SwDevicePropertySet",
    "SwDeviceSetLifetime",
    "SwMemFree",
    "UPNP_ADDRESSFAMILY_BOTH",
    "UPNP_ADDRESSFAMILY_IPv4",
    "UPNP_ADDRESSFAMILY_IPv6",
    "UPNP_E_ACTION_REQUEST_FAILED",
    "UPNP_E_ACTION_SPECIFIC_BASE",
    "UPNP_E_DEVICE_ELEMENT_EXPECTED",
    "UPNP_E_DEVICE_ERROR",
    "UPNP_E_DEVICE_NODE_INCOMPLETE",
    "UPNP_E_DEVICE_NOTREGISTERED",
    "UPNP_E_DEVICE_RUNNING",
    "UPNP_E_DEVICE_TIMEOUT",
    "UPNP_E_DUPLICATE_NOT_ALLOWED",
    "UPNP_E_DUPLICATE_SERVICE_ID",
    "UPNP_E_ERROR_PROCESSING_RESPONSE",
    "UPNP_E_EVENT_SUBSCRIPTION_FAILED",
    "UPNP_E_ICON_ELEMENT_EXPECTED",
    "UPNP_E_ICON_NODE_INCOMPLETE",
    "UPNP_E_INVALID_ACTION",
    "UPNP_E_INVALID_ARGUMENTS",
    "UPNP_E_INVALID_DESCRIPTION",
    "UPNP_E_INVALID_DOCUMENT",
    "UPNP_E_INVALID_ICON",
    "UPNP_E_INVALID_ROOT_NAMESPACE",
    "UPNP_E_INVALID_SERVICE",
    "UPNP_E_INVALID_VARIABLE",
    "UPNP_E_INVALID_XML",
    "UPNP_E_OUT_OF_SYNC",
    "UPNP_E_PROTOCOL_ERROR",
    "UPNP_E_REQUIRED_ELEMENT_ERROR",
    "UPNP_E_ROOT_ELEMENT_EXPECTED",
    "UPNP_E_SERVICE_ELEMENT_EXPECTED",
    "UPNP_E_SERVICE_NODE_INCOMPLETE",
    "UPNP_E_SUFFIX_TOO_LONG",
    "UPNP_E_TRANSPORT_ERROR",
    "UPNP_E_URLBASE_PRESENT",
    "UPNP_E_VALUE_TOO_LONG",
    "UPNP_E_VARIABLE_VALUE_UNKNOWN",
    "UPNP_SERVICE_DELAY_SCPD_AND_SUBSCRIPTION",
    "UPnPDescriptionDocument",
    "UPnPDescriptionDocumentEx",
    "UPnPDevice",
    "UPnPDeviceFinder",
    "UPnPDeviceFinderEx",
    "UPnPDevices",
    "UPnPRegistrar",
    "UPnPRemoteEndpointInfo",
    "UPnPService",
    "UPnPServices",
]
_arch_optional = [
]
