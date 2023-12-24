from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer, ConstantLazyLoader
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Media.LibrarySharingServices
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Variant
class IWindowsMediaLibrarySharingDevice(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3dccc293-4fd9-4191-a25b-8e57c5d27bd4}')
    @commethod(7)
    def get_DeviceID(self, deviceID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Authorization(self, authorization: POINTER(win32more.Windows.Win32.Media.LibrarySharingServices.WindowsMediaLibrarySharingDeviceAuthorizationStatus)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_Authorization(self, authorization: win32more.Windows.Win32.Media.LibrarySharingServices.WindowsMediaLibrarySharingDeviceAuthorizationStatus) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Properties(self, deviceProperties: POINTER(win32more.Windows.Win32.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDeviceProperties)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWindowsMediaLibrarySharingDeviceProperties(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c4623214-6b06-40c5-a623-b2ff4c076bfd}')
    @commethod(7)
    def get_Item(self, index: Int32, property: POINTER(win32more.Windows.Win32.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDeviceProperty)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetProperty(self, name: win32more.Windows.Win32.Foundation.BSTR, property: POINTER(win32more.Windows.Win32.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDeviceProperty)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWindowsMediaLibrarySharingDeviceProperty(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{81e26927-7a7d-40a7-81d4-bddc02960e3e}')
    @commethod(7)
    def get_Name(self, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Value(self, value: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWindowsMediaLibrarySharingDevices(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{1803f9d6-fe6d-4546-bf5b-992fe8ec12d1}')
    @commethod(7)
    def get_Item(self, index: Int32, device: POINTER(win32more.Windows.Win32.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDevice(self, deviceID: win32more.Windows.Win32.Foundation.BSTR, device: POINTER(win32more.Windows.Win32.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWindowsMediaLibrarySharingServices(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{01f5f85e-0a81-40da-a7c8-21ef3af8440c}')
    @commethod(7)
    def showShareMediaCPL(self, device: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_userHomeMediaSharingState(self, sharingEnabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_userHomeMediaSharingState(self, sharingEnabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_userHomeMediaSharingLibraryName(self, libraryName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_userHomeMediaSharingLibraryName(self, libraryName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_computerHomeMediaSharingAllowedState(self, sharingAllowed: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_computerHomeMediaSharingAllowedState(self, sharingAllowed: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_userInternetMediaSharingState(self, sharingEnabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_userInternetMediaSharingState(self, sharingEnabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_computerInternetMediaSharingAllowedState(self, sharingAllowed: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_computerInternetMediaSharingAllowedState(self, sharingAllowed: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_internetMediaSharingSecurityGroup(self, securityGroup: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_internetMediaSharingSecurityGroup(self, securityGroup: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_allowSharingToAllDevices(self, sharingEnabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_allowSharingToAllDevices(self, sharingEnabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def setDefaultAuthorization(self, MACAddresses: win32more.Windows.Win32.Foundation.BSTR, friendlyName: win32more.Windows.Win32.Foundation.BSTR, authorization: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def setAuthorizationState(self, MACAddress: win32more.Windows.Win32.Foundation.BSTR, authorizationState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def getAllDevices(self, devices: POINTER(win32more.Windows.Win32.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDevices)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_customSettingsApplied(self, customSettingsApplied: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
WindowsMediaLibrarySharingDeviceAuthorizationStatus = Int32
DEVICE_AUTHORIZATION_UNKNOWN: win32more.Windows.Win32.Media.LibrarySharingServices.WindowsMediaLibrarySharingDeviceAuthorizationStatus = 0
DEVICE_AUTHORIZATION_ALLOWED: win32more.Windows.Win32.Media.LibrarySharingServices.WindowsMediaLibrarySharingDeviceAuthorizationStatus = 1
DEVICE_AUTHORIZATION_DENIED: win32more.Windows.Win32.Media.LibrarySharingServices.WindowsMediaLibrarySharingDeviceAuthorizationStatus = 2
WindowsMediaLibrarySharingServices = Guid('{ad581b00-7b64-4e59-a38d-d2c5bf51ddb3}')


make_ready(__name__)
