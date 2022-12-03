from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Media.LibrarySharingServices
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
def _define_IWindowsMediaLibrarySharingDevice_head():
    class IWindowsMediaLibrarySharingDevice(win32more.System.Com.IDispatch_head):
        Guid = Guid('3dccc293-4fd9-4191-a2-5b-8e-57-c5-d2-7b-d4')
    return IWindowsMediaLibrarySharingDevice
def _define_IWindowsMediaLibrarySharingDevice():
    IWindowsMediaLibrarySharingDevice = win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDevice_head
    IWindowsMediaLibrarySharingDevice.get_DeviceID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_DeviceID', ((1, 'deviceID'),)))
    IWindowsMediaLibrarySharingDevice.get_Authorization = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.LibrarySharingServices.WindowsMediaLibrarySharingDeviceAuthorizationStatus))(8, 'get_Authorization', ((1, 'authorization'),)))
    IWindowsMediaLibrarySharingDevice.put_Authorization = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.LibrarySharingServices.WindowsMediaLibrarySharingDeviceAuthorizationStatus)(9, 'put_Authorization', ((1, 'authorization'),)))
    IWindowsMediaLibrarySharingDevice.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDeviceProperties_head))(10, 'get_Properties', ((1, 'deviceProperties'),)))
    win32more.System.Com.IDispatch
    return IWindowsMediaLibrarySharingDevice
def _define_IWindowsMediaLibrarySharingDeviceProperties_head():
    class IWindowsMediaLibrarySharingDeviceProperties(win32more.System.Com.IDispatch_head):
        Guid = Guid('c4623214-6b06-40c5-a6-23-b2-ff-4c-07-6b-fd')
    return IWindowsMediaLibrarySharingDeviceProperties
def _define_IWindowsMediaLibrarySharingDeviceProperties():
    IWindowsMediaLibrarySharingDeviceProperties = win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDeviceProperties_head
    IWindowsMediaLibrarySharingDeviceProperties.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDeviceProperty_head))(7, 'get_Item', ((1, 'index'),(1, 'property'),)))
    IWindowsMediaLibrarySharingDeviceProperties.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(8, 'get_Count', ((1, 'count'),)))
    IWindowsMediaLibrarySharingDeviceProperties.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDeviceProperty_head))(9, 'GetProperty', ((1, 'name'),(1, 'property'),)))
    win32more.System.Com.IDispatch
    return IWindowsMediaLibrarySharingDeviceProperties
def _define_IWindowsMediaLibrarySharingDeviceProperty_head():
    class IWindowsMediaLibrarySharingDeviceProperty(win32more.System.Com.IDispatch_head):
        Guid = Guid('81e26927-7a7d-40a7-81-d4-bd-dc-02-96-0e-3e')
    return IWindowsMediaLibrarySharingDeviceProperty
def _define_IWindowsMediaLibrarySharingDeviceProperty():
    IWindowsMediaLibrarySharingDeviceProperty = win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDeviceProperty_head
    IWindowsMediaLibrarySharingDeviceProperty.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Name', ((1, 'name'),)))
    IWindowsMediaLibrarySharingDeviceProperty.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(8, 'get_Value', ((1, 'value'),)))
    win32more.System.Com.IDispatch
    return IWindowsMediaLibrarySharingDeviceProperty
def _define_IWindowsMediaLibrarySharingDevices_head():
    class IWindowsMediaLibrarySharingDevices(win32more.System.Com.IDispatch_head):
        Guid = Guid('1803f9d6-fe6d-4546-bf-5b-99-2f-e8-ec-12-d1')
    return IWindowsMediaLibrarySharingDevices
def _define_IWindowsMediaLibrarySharingDevices():
    IWindowsMediaLibrarySharingDevices = win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDevices_head
    IWindowsMediaLibrarySharingDevices.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDevice_head))(7, 'get_Item', ((1, 'index'),(1, 'device'),)))
    IWindowsMediaLibrarySharingDevices.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(8, 'get_Count', ((1, 'count'),)))
    IWindowsMediaLibrarySharingDevices.GetDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDevice_head))(9, 'GetDevice', ((1, 'deviceID'),(1, 'device'),)))
    win32more.System.Com.IDispatch
    return IWindowsMediaLibrarySharingDevices
def _define_IWindowsMediaLibrarySharingServices_head():
    class IWindowsMediaLibrarySharingServices(win32more.System.Com.IDispatch_head):
        Guid = Guid('01f5f85e-0a81-40da-a7-c8-21-ef-3a-f8-44-0c')
    return IWindowsMediaLibrarySharingServices
def _define_IWindowsMediaLibrarySharingServices():
    IWindowsMediaLibrarySharingServices = win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingServices_head
    IWindowsMediaLibrarySharingServices.showShareMediaCPL = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(7, 'showShareMediaCPL', ((1, 'device'),)))
    IWindowsMediaLibrarySharingServices.get_userHomeMediaSharingState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(8, 'get_userHomeMediaSharingState', ((1, 'sharingEnabled'),)))
    IWindowsMediaLibrarySharingServices.put_userHomeMediaSharingState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(9, 'put_userHomeMediaSharingState', ((1, 'sharingEnabled'),)))
    IWindowsMediaLibrarySharingServices.get_userHomeMediaSharingLibraryName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_userHomeMediaSharingLibraryName', ((1, 'libraryName'),)))
    IWindowsMediaLibrarySharingServices.put_userHomeMediaSharingLibraryName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(11, 'put_userHomeMediaSharingLibraryName', ((1, 'libraryName'),)))
    IWindowsMediaLibrarySharingServices.get_computerHomeMediaSharingAllowedState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(12, 'get_computerHomeMediaSharingAllowedState', ((1, 'sharingAllowed'),)))
    IWindowsMediaLibrarySharingServices.put_computerHomeMediaSharingAllowedState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(13, 'put_computerHomeMediaSharingAllowedState', ((1, 'sharingAllowed'),)))
    IWindowsMediaLibrarySharingServices.get_userInternetMediaSharingState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(14, 'get_userInternetMediaSharingState', ((1, 'sharingEnabled'),)))
    IWindowsMediaLibrarySharingServices.put_userInternetMediaSharingState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(15, 'put_userInternetMediaSharingState', ((1, 'sharingEnabled'),)))
    IWindowsMediaLibrarySharingServices.get_computerInternetMediaSharingAllowedState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(16, 'get_computerInternetMediaSharingAllowedState', ((1, 'sharingAllowed'),)))
    IWindowsMediaLibrarySharingServices.put_computerInternetMediaSharingAllowedState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(17, 'put_computerInternetMediaSharingAllowedState', ((1, 'sharingAllowed'),)))
    IWindowsMediaLibrarySharingServices.get_internetMediaSharingSecurityGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(18, 'get_internetMediaSharingSecurityGroup', ((1, 'securityGroup'),)))
    IWindowsMediaLibrarySharingServices.put_internetMediaSharingSecurityGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(19, 'put_internetMediaSharingSecurityGroup', ((1, 'securityGroup'),)))
    IWindowsMediaLibrarySharingServices.get_allowSharingToAllDevices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(20, 'get_allowSharingToAllDevices', ((1, 'sharingEnabled'),)))
    IWindowsMediaLibrarySharingServices.put_allowSharingToAllDevices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(21, 'put_allowSharingToAllDevices', ((1, 'sharingEnabled'),)))
    IWindowsMediaLibrarySharingServices.setDefaultAuthorization = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.VARIANT_BOOL)(22, 'setDefaultAuthorization', ((1, 'MACAddresses'),(1, 'friendlyName'),(1, 'authorization'),)))
    IWindowsMediaLibrarySharingServices.setAuthorizationState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.VARIANT_BOOL)(23, 'setAuthorizationState', ((1, 'MACAddress'),(1, 'authorizationState'),)))
    IWindowsMediaLibrarySharingServices.getAllDevices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDevices_head))(24, 'getAllDevices', ((1, 'devices'),)))
    IWindowsMediaLibrarySharingServices.get_customSettingsApplied = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(25, 'get_customSettingsApplied', ((1, 'customSettingsApplied'),)))
    win32more.System.Com.IDispatch
    return IWindowsMediaLibrarySharingServices
WindowsMediaLibrarySharingDeviceAuthorizationStatus = Int32
DEVICE_AUTHORIZATION_UNKNOWN = 0
DEVICE_AUTHORIZATION_ALLOWED = 1
DEVICE_AUTHORIZATION_DENIED = 2
WindowsMediaLibrarySharingServices = Guid('ad581b00-7b64-4e59-a3-8d-d2-c5-bf-51-dd-b3')
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
