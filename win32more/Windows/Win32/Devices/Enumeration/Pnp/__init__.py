from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Devices.Enumeration.Pnp
import win32more.Windows.Win32.Devices.Properties
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Variant
UPNP_E_ROOT_ELEMENT_EXPECTED: win32more.Windows.Win32.Foundation.HRESULT = -2147220992
UPNP_E_DEVICE_ELEMENT_EXPECTED: win32more.Windows.Win32.Foundation.HRESULT = -2147220991
UPNP_E_SERVICE_ELEMENT_EXPECTED: win32more.Windows.Win32.Foundation.HRESULT = -2147220990
UPNP_E_SERVICE_NODE_INCOMPLETE: win32more.Windows.Win32.Foundation.HRESULT = -2147220989
UPNP_E_DEVICE_NODE_INCOMPLETE: win32more.Windows.Win32.Foundation.HRESULT = -2147220988
UPNP_E_ICON_ELEMENT_EXPECTED: win32more.Windows.Win32.Foundation.HRESULT = -2147220987
UPNP_E_ICON_NODE_INCOMPLETE: win32more.Windows.Win32.Foundation.HRESULT = -2147220986
UPNP_E_INVALID_ACTION: win32more.Windows.Win32.Foundation.HRESULT = -2147220985
UPNP_E_INVALID_ARGUMENTS: win32more.Windows.Win32.Foundation.HRESULT = -2147220984
UPNP_E_OUT_OF_SYNC: win32more.Windows.Win32.Foundation.HRESULT = -2147220983
UPNP_E_ACTION_REQUEST_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2147220976
UPNP_E_TRANSPORT_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2147220975
UPNP_E_VARIABLE_VALUE_UNKNOWN: win32more.Windows.Win32.Foundation.HRESULT = -2147220974
UPNP_E_INVALID_VARIABLE: win32more.Windows.Win32.Foundation.HRESULT = -2147220973
UPNP_E_DEVICE_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2147220972
UPNP_E_PROTOCOL_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2147220971
UPNP_E_ERROR_PROCESSING_RESPONSE: win32more.Windows.Win32.Foundation.HRESULT = -2147220970
UPNP_E_DEVICE_TIMEOUT: win32more.Windows.Win32.Foundation.HRESULT = -2147220969
UPNP_E_INVALID_DOCUMENT: win32more.Windows.Win32.Foundation.HRESULT = -2147220224
UPNP_E_EVENT_SUBSCRIPTION_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2147220223
FAULT_INVALID_ACTION: UInt32 = 401
FAULT_INVALID_ARG: UInt32 = 402
FAULT_INVALID_SEQUENCE_NUMBER: UInt32 = 403
FAULT_INVALID_VARIABLE: UInt32 = 404
FAULT_DEVICE_INTERNAL_ERROR: UInt32 = 501
FAULT_ACTION_SPECIFIC_BASE: UInt32 = 600
FAULT_ACTION_SPECIFIC_MAX: UInt32 = 899
UPNP_E_ACTION_SPECIFIC_BASE: win32more.Windows.Win32.Foundation.HRESULT = -2147220736
UPNP_ADDRESSFAMILY_IPv4: UInt32 = 1
UPNP_ADDRESSFAMILY_IPv6: UInt32 = 2
UPNP_ADDRESSFAMILY_BOTH: UInt32 = 3
UPNP_SERVICE_DELAY_SCPD_AND_SUBSCRIPTION: UInt32 = 1
UPNP_E_REQUIRED_ELEMENT_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2147180512
UPNP_E_DUPLICATE_NOT_ALLOWED: win32more.Windows.Win32.Foundation.HRESULT = -2147180511
UPNP_E_DUPLICATE_SERVICE_ID: win32more.Windows.Win32.Foundation.HRESULT = -2147180510
UPNP_E_INVALID_DESCRIPTION: win32more.Windows.Win32.Foundation.HRESULT = -2147180509
UPNP_E_INVALID_SERVICE: win32more.Windows.Win32.Foundation.HRESULT = -2147180508
UPNP_E_INVALID_ICON: win32more.Windows.Win32.Foundation.HRESULT = -2147180507
UPNP_E_INVALID_XML: win32more.Windows.Win32.Foundation.HRESULT = -2147180506
UPNP_E_INVALID_ROOT_NAMESPACE: win32more.Windows.Win32.Foundation.HRESULT = -2147180505
UPNP_E_SUFFIX_TOO_LONG: win32more.Windows.Win32.Foundation.HRESULT = -2147180504
UPNP_E_URLBASE_PRESENT: win32more.Windows.Win32.Foundation.HRESULT = -2147180503
UPNP_E_VALUE_TOO_LONG: win32more.Windows.Win32.Foundation.HRESULT = -2147180496
UPNP_E_DEVICE_RUNNING: win32more.Windows.Win32.Foundation.HRESULT = -2147180495
UPNP_E_DEVICE_NOTREGISTERED: win32more.Windows.Win32.Foundation.HRESULT = -2147180494
REMOTE_ADDRESS_VALUE_NAME: String = 'RemoteAddress'
ADDRESS_FAMILY_VALUE_NAME: String = 'AddressFamily'
@winfunctype('CFGMGR32.dll')
def SwDeviceCreate(pszEnumeratorName: win32more.Windows.Win32.Foundation.PWSTR, pszParentDeviceInstance: win32more.Windows.Win32.Foundation.PWSTR, pCreateInfo: POINTER(win32more.Windows.Win32.Devices.Enumeration.Pnp.SW_DEVICE_CREATE_INFO), cPropertyCount: UInt32, pProperties: POINTER(win32more.Windows.Win32.Devices.Properties.DEVPROPERTY), pCallback: win32more.Windows.Win32.Devices.Enumeration.Pnp.SW_DEVICE_CREATE_CALLBACK, pContext: VoidPtr, phSwDevice: POINTER(win32more.Windows.Win32.Devices.Enumeration.Pnp.HSWDEVICE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('CFGMGR32.dll')
def SwDeviceClose(hSwDevice: win32more.Windows.Win32.Devices.Enumeration.Pnp.HSWDEVICE) -> Void: ...
@winfunctype('CFGMGR32.dll')
def SwDeviceSetLifetime(hSwDevice: win32more.Windows.Win32.Devices.Enumeration.Pnp.HSWDEVICE, Lifetime: win32more.Windows.Win32.Devices.Enumeration.Pnp.SW_DEVICE_LIFETIME) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('CFGMGR32.dll')
def SwDeviceGetLifetime(hSwDevice: win32more.Windows.Win32.Devices.Enumeration.Pnp.HSWDEVICE, pLifetime: POINTER(win32more.Windows.Win32.Devices.Enumeration.Pnp.SW_DEVICE_LIFETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('CFGMGR32.dll')
def SwDevicePropertySet(hSwDevice: win32more.Windows.Win32.Devices.Enumeration.Pnp.HSWDEVICE, cPropertyCount: UInt32, pProperties: POINTER(win32more.Windows.Win32.Devices.Properties.DEVPROPERTY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('CFGMGR32.dll')
def SwDeviceInterfaceRegister(hSwDevice: win32more.Windows.Win32.Devices.Enumeration.Pnp.HSWDEVICE, pInterfaceClassGuid: POINTER(Guid), pszReferenceString: win32more.Windows.Win32.Foundation.PWSTR, cPropertyCount: UInt32, pProperties: POINTER(win32more.Windows.Win32.Devices.Properties.DEVPROPERTY), fEnabled: win32more.Windows.Win32.Foundation.BOOL, ppszDeviceInterfaceId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('CFGMGR32.dll')
def SwMemFree(pMem: VoidPtr) -> Void: ...
@winfunctype('CFGMGR32.dll')
def SwDeviceInterfaceSetState(hSwDevice: win32more.Windows.Win32.Devices.Enumeration.Pnp.HSWDEVICE, pszDeviceInterfaceId: win32more.Windows.Win32.Foundation.PWSTR, fEnabled: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('CFGMGR32.dll')
def SwDeviceInterfacePropertySet(hSwDevice: win32more.Windows.Win32.Devices.Enumeration.Pnp.HSWDEVICE, pszDeviceInterfaceId: win32more.Windows.Win32.Foundation.PWSTR, cPropertyCount: UInt32, pProperties: POINTER(win32more.Windows.Win32.Devices.Properties.DEVPROPERTY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
HSWDEVICE = VoidPtr
class IUPnPAddressFamilyControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e3bf6178-694e-459f-a5a6-191ea0ffa1c7}')
    @commethod(3)
    def SetAddressFamily(self, dwFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAddressFamily(self, pdwFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUPnPAsyncResult(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4d65fd08-d13e-4274-9c8b-dd8d028c8644}')
    @commethod(3)
    def AsyncOperationComplete(self, ullRequestID: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUPnPDescriptionDocument(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{11d1c1b2-7daa-4c9e-9595-7f82ed206d1e}')
    @commethod(7)
    def get_ReadyState(self, plReadyState: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Load(self, bstrUrl: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def LoadAsync(self, bstrUrl: win32more.Windows.Win32.Foundation.BSTR, punkCallback: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_LoadResult(self, phrError: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Abort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RootDevice(self, ppudRootDevice: POINTER(win32more.Windows.Win32.Devices.Enumeration.Pnp.IUPnPDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def DeviceByUDN(self, bstrUDN: win32more.Windows.Win32.Foundation.BSTR, ppudDevice: POINTER(win32more.Windows.Win32.Devices.Enumeration.Pnp.IUPnPDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUPnPDescriptionDocumentCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{77394c69-5486-40d6-9bc3-4991983e02da}')
    @commethod(3)
    def LoadComplete(self, hrLoadResult: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUPnPDevice(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3d44d0d1-98c9-4889-acd1-f9d674bf2221}')
    @commethod(7)
    def get_IsRootDevice(self, pvarb: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_RootDevice(self, ppudRootDevice: POINTER(win32more.Windows.Win32.Devices.Enumeration.Pnp.IUPnPDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ParentDevice(self, ppudDeviceParent: POINTER(win32more.Windows.Win32.Devices.Enumeration.Pnp.IUPnPDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_HasChildren(self, pvarb: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Children(self, ppudChildren: POINTER(win32more.Windows.Win32.Devices.Enumeration.Pnp.IUPnPDevices)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_UniqueDeviceName(self, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_FriendlyName(self, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Type(self, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_PresentationURL(self, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_ManufacturerName(self, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_ManufacturerURL(self, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_ModelName(self, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_ModelNumber(self, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_Description(self, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_ModelURL(self, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_UPC(self, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_SerialNumber(self, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def IconURL(self, bstrEncodingFormat: win32more.Windows.Win32.Foundation.BSTR, lSizeX: Int32, lSizeY: Int32, lBitDepth: Int32, pbstrIconURL: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_Services(self, ppusServices: POINTER(win32more.Windows.Win32.Devices.Enumeration.Pnp.IUPnPServices)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUPnPDeviceControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{204810ba-73b2-11d4-bf42-00b0d0118b56}')
    @commethod(3)
    def Initialize(self, bstrXMLDesc: win32more.Windows.Win32.Foundation.BSTR, bstrDeviceIdentifier: win32more.Windows.Win32.Foundation.BSTR, bstrInitString: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetServiceObject(self, bstrUDN: win32more.Windows.Win32.Foundation.BSTR, bstrServiceId: win32more.Windows.Win32.Foundation.BSTR, ppdispService: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUPnPDeviceControlHttpHeaders(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{204810bb-73b2-11d4-bf42-00b0d0118b56}')
    @commethod(3)
    def GetAdditionalResponseHeaders(self, bstrHttpResponseHeaders: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUPnPDeviceDocumentAccess(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e7772804-3287-418e-9072-cf2b47238981}')
    @commethod(3)
    def GetDocumentURL(self, pbstrDocument: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUPnPDeviceDocumentAccessEx(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c4bc4050-6178-4bd1-a4b8-6398321f3247}')
    @commethod(3)
    def GetDocument(self, pbstrDocument: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUPnPDeviceFinder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{adda3d55-6f72-4319-bff9-18600a539b10}')
    @commethod(7)
    def FindByType(self, bstrTypeURI: win32more.Windows.Win32.Foundation.BSTR, dwFlags: UInt32, pDevices: POINTER(win32more.Windows.Win32.Devices.Enumeration.Pnp.IUPnPDevices)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateAsyncFind(self, bstrTypeURI: win32more.Windows.Win32.Foundation.BSTR, dwFlags: UInt32, punkDeviceFinderCallback: win32more.Windows.Win32.System.Com.IUnknown, plFindData: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def StartAsyncFind(self, lFindData: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CancelAsyncFind(self, lFindData: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def FindByUDN(self, bstrUDN: win32more.Windows.Win32.Foundation.BSTR, pDevice: POINTER(win32more.Windows.Win32.Devices.Enumeration.Pnp.IUPnPDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUPnPDeviceFinderAddCallbackWithInterface(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{983dfc0b-1796-44df-8975-ca545b620ee5}')
    @commethod(3)
    def DeviceAddedWithInterface(self, lFindData: Int32, pDevice: win32more.Windows.Win32.Devices.Enumeration.Pnp.IUPnPDevice, pguidInterface: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUPnPDeviceFinderCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{415a984a-88b3-49f3-92af-0508bedf0d6c}')
    @commethod(3)
    def DeviceAdded(self, lFindData: Int32, pDevice: win32more.Windows.Win32.Devices.Enumeration.Pnp.IUPnPDevice) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DeviceRemoved(self, lFindData: Int32, bstrUDN: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SearchComplete(self, lFindData: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUPnPDeviceProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{204810b8-73b2-11d4-bf42-00b0d0118b56}')
    @commethod(3)
    def Start(self, bstrInitString: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Stop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUPnPDevices(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{fdbc0c73-bda3-4c66-ac4f-f2d96fdad68c}')
    @commethod(7)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Item(self, bstrUDN: win32more.Windows.Win32.Foundation.BSTR, ppDevice: POINTER(win32more.Windows.Win32.Devices.Enumeration.Pnp.IUPnPDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUPnPEventSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{204810b4-73b2-11d4-bf42-00b0d0118b56}')
    @commethod(3)
    def OnStateChanged(self, cChanges: UInt32, rgdispidChanges: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnStateChangedSafe(self, varsadispidChanges: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUPnPEventSource(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{204810b5-73b2-11d4-bf42-00b0d0118b56}')
    @commethod(3)
    def Advise(self, pesSubscriber: win32more.Windows.Win32.Devices.Enumeration.Pnp.IUPnPEventSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unadvise(self, pesSubscriber: win32more.Windows.Win32.Devices.Enumeration.Pnp.IUPnPEventSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUPnPHttpHeaderControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0405af4f-8b5c-447c-80f2-b75984a31f3c}')
    @commethod(3)
    def AddRequestHeaders(self, bstrHttpHeaders: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUPnPRegistrar(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{204810b6-73b2-11d4-bf42-00b0d0118b56}')
    @commethod(3)
    def RegisterDevice(self, bstrXMLDesc: win32more.Windows.Win32.Foundation.BSTR, bstrProgIDDeviceControlClass: win32more.Windows.Win32.Foundation.BSTR, bstrInitString: win32more.Windows.Win32.Foundation.BSTR, bstrContainerId: win32more.Windows.Win32.Foundation.BSTR, bstrResourcePath: win32more.Windows.Win32.Foundation.BSTR, nLifeTime: Int32, pbstrDeviceIdentifier: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RegisterRunningDevice(self, bstrXMLDesc: win32more.Windows.Win32.Foundation.BSTR, punkDeviceControl: win32more.Windows.Win32.System.Com.IUnknown, bstrInitString: win32more.Windows.Win32.Foundation.BSTR, bstrResourcePath: win32more.Windows.Win32.Foundation.BSTR, nLifeTime: Int32, pbstrDeviceIdentifier: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RegisterDeviceProvider(self, bstrProviderName: win32more.Windows.Win32.Foundation.BSTR, bstrProgIDProviderClass: win32more.Windows.Win32.Foundation.BSTR, bstrInitString: win32more.Windows.Win32.Foundation.BSTR, bstrContainerId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetUniqueDeviceName(self, bstrDeviceIdentifier: win32more.Windows.Win32.Foundation.BSTR, bstrTemplateUDN: win32more.Windows.Win32.Foundation.BSTR, pbstrUDN: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UnregisterDevice(self, bstrDeviceIdentifier: win32more.Windows.Win32.Foundation.BSTR, fPermanent: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UnregisterDeviceProvider(self, bstrProviderName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUPnPRemoteEndpointInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c92eb863-0269-4aff-9c72-75321bba2952}')
    @commethod(3)
    def GetDwordValue(self, bstrValueName: win32more.Windows.Win32.Foundation.BSTR, pdwValue: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetStringValue(self, bstrValueName: win32more.Windows.Win32.Foundation.BSTR, pbstrValue: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetGuidValue(self, bstrValueName: win32more.Windows.Win32.Foundation.BSTR, pguidValue: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUPnPReregistrar(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{204810b7-73b2-11d4-bf42-00b0d0118b56}')
    @commethod(3)
    def ReregisterDevice(self, bstrDeviceIdentifier: win32more.Windows.Win32.Foundation.BSTR, bstrXMLDesc: win32more.Windows.Win32.Foundation.BSTR, bstrProgIDDeviceControlClass: win32more.Windows.Win32.Foundation.BSTR, bstrInitString: win32more.Windows.Win32.Foundation.BSTR, bstrContainerId: win32more.Windows.Win32.Foundation.BSTR, bstrResourcePath: win32more.Windows.Win32.Foundation.BSTR, nLifeTime: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReregisterRunningDevice(self, bstrDeviceIdentifier: win32more.Windows.Win32.Foundation.BSTR, bstrXMLDesc: win32more.Windows.Win32.Foundation.BSTR, punkDeviceControl: win32more.Windows.Win32.System.Com.IUnknown, bstrInitString: win32more.Windows.Win32.Foundation.BSTR, bstrResourcePath: win32more.Windows.Win32.Foundation.BSTR, nLifeTime: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUPnPService(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{a295019c-dc65-47dd-90dc-7fe918a1ab44}')
    @commethod(7)
    def QueryStateVariable(self, bstrVariableName: win32more.Windows.Win32.Foundation.BSTR, pValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def InvokeAction(self, bstrActionName: win32more.Windows.Win32.Foundation.BSTR, vInActionArgs: win32more.Windows.Win32.System.Variant.VARIANT, pvOutActionArgs: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvRetVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ServiceTypeIdentifier(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def AddCallback(self, pUnkCallback: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Id(self, pbstrId: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_LastTransportStatus(self, plValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUPnPServiceAsync(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{098bdaf5-5ec1-49e7-a260-b3a11dd8680c}')
    @commethod(3)
    def BeginInvokeAction(self, bstrActionName: win32more.Windows.Win32.Foundation.BSTR, vInActionArgs: win32more.Windows.Win32.System.Variant.VARIANT, pAsyncResult: win32more.Windows.Win32.Devices.Enumeration.Pnp.IUPnPAsyncResult, pullRequestID: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EndInvokeAction(self, ullRequestID: UInt64, pvOutActionArgs: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvRetVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def BeginQueryStateVariable(self, bstrVariableName: win32more.Windows.Win32.Foundation.BSTR, pAsyncResult: win32more.Windows.Win32.Devices.Enumeration.Pnp.IUPnPAsyncResult, pullRequestID: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EndQueryStateVariable(self, ullRequestID: UInt64, pValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def BeginSubscribeToEvents(self, pUnkCallback: win32more.Windows.Win32.System.Com.IUnknown, pAsyncResult: win32more.Windows.Win32.Devices.Enumeration.Pnp.IUPnPAsyncResult, pullRequestID: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def EndSubscribeToEvents(self, ullRequestID: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def BeginSCPDDownload(self, pAsyncResult: win32more.Windows.Win32.Devices.Enumeration.Pnp.IUPnPAsyncResult, pullRequestID: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EndSCPDDownload(self, ullRequestID: UInt64, pbstrSCPDDoc: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CancelAsyncOperation(self, ullRequestID: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUPnPServiceCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{31fadca9-ab73-464b-b67d-5c1d0f83c8b8}')
    @commethod(3)
    def StateVariableChanged(self, pus: win32more.Windows.Win32.Devices.Enumeration.Pnp.IUPnPService, pcwszStateVarName: win32more.Windows.Win32.Foundation.PWSTR, vaValue: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ServiceInstanceDied(self, pus: win32more.Windows.Win32.Devices.Enumeration.Pnp.IUPnPService) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUPnPServiceDocumentAccess(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{21905529-0a5e-4589-825d-7e6d87ea6998}')
    @commethod(3)
    def GetDocumentURL(self, pbstrDocUrl: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDocument(self, pbstrDoc: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUPnPServiceEnumProperty(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{38873b37-91bb-49f4-b249-2e8efbb8a816}')
    @commethod(3)
    def SetServiceEnumProperty(self, dwMask: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUPnPServices(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3f8c8e9e-9a7a-4dc8-bc41-ff31fa374956}')
    @commethod(7)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Item(self, bstrServiceId: win32more.Windows.Win32.Foundation.BSTR, ppService: POINTER(win32more.Windows.Win32.Devices.Enumeration.Pnp.IUPnPService)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
SW_DEVICE_CAPABILITIES = Int32
SWDeviceCapabilitiesNone: win32more.Windows.Win32.Devices.Enumeration.Pnp.SW_DEVICE_CAPABILITIES = 0
SWDeviceCapabilitiesRemovable: win32more.Windows.Win32.Devices.Enumeration.Pnp.SW_DEVICE_CAPABILITIES = 1
SWDeviceCapabilitiesSilentInstall: win32more.Windows.Win32.Devices.Enumeration.Pnp.SW_DEVICE_CAPABILITIES = 2
SWDeviceCapabilitiesNoDisplayInUI: win32more.Windows.Win32.Devices.Enumeration.Pnp.SW_DEVICE_CAPABILITIES = 4
SWDeviceCapabilitiesDriverRequired: win32more.Windows.Win32.Devices.Enumeration.Pnp.SW_DEVICE_CAPABILITIES = 8
@winfunctype_pointer
def SW_DEVICE_CREATE_CALLBACK(hSwDevice: win32more.Windows.Win32.Devices.Enumeration.Pnp.HSWDEVICE, CreateResult: win32more.Windows.Win32.Foundation.HRESULT, pContext: VoidPtr, pszDeviceInstanceId: win32more.Windows.Win32.Foundation.PWSTR) -> Void: ...
class SW_DEVICE_CREATE_INFO(Structure):
    cbSize: UInt32
    pszInstanceId: win32more.Windows.Win32.Foundation.PWSTR
    pszzHardwareIds: win32more.Windows.Win32.Foundation.PWSTR
    pszzCompatibleIds: win32more.Windows.Win32.Foundation.PWSTR
    pContainerId: POINTER(Guid)
    CapabilityFlags: UInt32
    pszDeviceDescription: win32more.Windows.Win32.Foundation.PWSTR
    pszDeviceLocation: win32more.Windows.Win32.Foundation.PWSTR
    pSecurityDescriptor: POINTER(win32more.Windows.Win32.Security.SECURITY_DESCRIPTOR)
SW_DEVICE_LIFETIME = Int32
SWDeviceLifetimeHandle: win32more.Windows.Win32.Devices.Enumeration.Pnp.SW_DEVICE_LIFETIME = 0
SWDeviceLifetimeParentPresent: win32more.Windows.Win32.Devices.Enumeration.Pnp.SW_DEVICE_LIFETIME = 1
SWDeviceLifetimeMax: win32more.Windows.Win32.Devices.Enumeration.Pnp.SW_DEVICE_LIFETIME = 2
UPnPDescriptionDocument = Guid('{1d8a9b47-3a28-4ce2-8a4b-bd34e45bceeb}')
UPnPDescriptionDocumentEx = Guid('{33fd0563-d81a-4393-83cc-0195b1da2f91}')
UPnPDevice = Guid('{a32552c5-ba61-457a-b59a-a2561e125e33}')
UPnPDeviceFinder = Guid('{e2085f28-feb7-404a-b8e7-e659bdeaaa02}')
UPnPDeviceFinderEx = Guid('{181b54fc-380b-4a75-b3f1-4ac45e9605b0}')
UPnPDevices = Guid('{b9e84ffd-ad3c-40a4-b835-0882ebcbaaa8}')
UPnPRegistrar = Guid('{204810b9-73b2-11d4-bf42-00b0d0118b56}')
UPnPRemoteEndpointInfo = Guid('{2e5e84e9-4049-4244-b728-2d24227157c7}')
UPnPService = Guid('{c624ba95-fbcb-4409-8c03-8cceec533ef1}')
UPnPServices = Guid('{c0bc4b4a-a406-4efc-932f-b8546b8100cc}')


make_ready(__name__)
