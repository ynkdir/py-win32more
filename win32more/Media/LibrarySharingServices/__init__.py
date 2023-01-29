from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Media.LibrarySharingServices
import win32more.System.Com
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
class IWindowsMediaLibrarySharingDevice(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('3dccc293-4fd9-4191-a2-5b-8e-57-c5-d2-7b-d4')
    @commethod(7)
    def get_DeviceID(deviceID: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Authorization(authorization: POINTER(win32more.Media.LibrarySharingServices.WindowsMediaLibrarySharingDeviceAuthorizationStatus)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_Authorization(authorization: win32more.Media.LibrarySharingServices.WindowsMediaLibrarySharingDeviceAuthorizationStatus) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Properties(deviceProperties: POINTER(win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDeviceProperties_head)) -> win32more.Foundation.HRESULT: ...
class IWindowsMediaLibrarySharingDeviceProperties(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('c4623214-6b06-40c5-a6-23-b2-ff-4c-07-6b-fd')
    @commethod(7)
    def get_Item(index: Int32, property: POINTER(win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDeviceProperty_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(count: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetProperty(name: win32more.Foundation.BSTR, property: POINTER(win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDeviceProperty_head)) -> win32more.Foundation.HRESULT: ...
class IWindowsMediaLibrarySharingDeviceProperty(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('81e26927-7a7d-40a7-81-d4-bd-dc-02-96-0e-3e')
    @commethod(7)
    def get_Name(name: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Value(value: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class IWindowsMediaLibrarySharingDevices(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('1803f9d6-fe6d-4546-bf-5b-99-2f-e8-ec-12-d1')
    @commethod(7)
    def get_Item(index: Int32, device: POINTER(win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDevice_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(count: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetDevice(deviceID: win32more.Foundation.BSTR, device: POINTER(win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDevice_head)) -> win32more.Foundation.HRESULT: ...
class IWindowsMediaLibrarySharingServices(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('01f5f85e-0a81-40da-a7-c8-21-ef-3a-f8-44-0c')
    @commethod(7)
    def showShareMediaCPL(device: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_userHomeMediaSharingState(sharingEnabled: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_userHomeMediaSharingState(sharingEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_userHomeMediaSharingLibraryName(libraryName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_userHomeMediaSharingLibraryName(libraryName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_computerHomeMediaSharingAllowedState(sharingAllowed: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_computerHomeMediaSharingAllowedState(sharingAllowed: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_userInternetMediaSharingState(sharingEnabled: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_userInternetMediaSharingState(sharingEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_computerInternetMediaSharingAllowedState(sharingAllowed: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_computerInternetMediaSharingAllowedState(sharingAllowed: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_internetMediaSharingSecurityGroup(securityGroup: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put_internetMediaSharingSecurityGroup(securityGroup: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_allowSharingToAllDevices(sharingEnabled: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def put_allowSharingToAllDevices(sharingEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def setDefaultAuthorization(MACAddresses: win32more.Foundation.BSTR, friendlyName: win32more.Foundation.BSTR, authorization: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def setAuthorizationState(MACAddress: win32more.Foundation.BSTR, authorizationState: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def getAllDevices(devices: POINTER(win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDevices_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_customSettingsApplied(customSettingsApplied: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
WindowsMediaLibrarySharingDeviceAuthorizationStatus = Int32
DEVICE_AUTHORIZATION_UNKNOWN: WindowsMediaLibrarySharingDeviceAuthorizationStatus = 0
DEVICE_AUTHORIZATION_ALLOWED: WindowsMediaLibrarySharingDeviceAuthorizationStatus = 1
DEVICE_AUTHORIZATION_DENIED: WindowsMediaLibrarySharingDeviceAuthorizationStatus = 2
WindowsMediaLibrarySharingServices = Guid('ad581b00-7b64-4e59-a3-8d-d2-c5-bf-51-dd-b3')
make_head(_module, 'IWindowsMediaLibrarySharingDevice')
make_head(_module, 'IWindowsMediaLibrarySharingDeviceProperties')
make_head(_module, 'IWindowsMediaLibrarySharingDeviceProperty')
make_head(_module, 'IWindowsMediaLibrarySharingDevices')
make_head(_module, 'IWindowsMediaLibrarySharingServices')
__all__ = [
    "DEVICE_AUTHORIZATION_ALLOWED",
    "DEVICE_AUTHORIZATION_DENIED",
    "DEVICE_AUTHORIZATION_UNKNOWN",
    "IWindowsMediaLibrarySharingDevice",
    "IWindowsMediaLibrarySharingDeviceProperties",
    "IWindowsMediaLibrarySharingDeviceProperty",
    "IWindowsMediaLibrarySharingDevices",
    "IWindowsMediaLibrarySharingServices",
    "WindowsMediaLibrarySharingDeviceAuthorizationStatus",
    "WindowsMediaLibrarySharingServices",
]
_arch_optional = [
]
