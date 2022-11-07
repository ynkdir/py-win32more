from win32more import *
import win32more.Foundation
import win32more.Media.LibrarySharingServices
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
WindowsMediaLibrarySharingServices = Guid('ad581b00-7b64-4e59-a38d-d2c5bf51ddb3')
WindowsMediaLibrarySharingDeviceAuthorizationStatus = Int32
DEVICE_AUTHORIZATION_UNKNOWN = 0
DEVICE_AUTHORIZATION_ALLOWED = 1
DEVICE_AUTHORIZATION_DENIED = 2
def _define_IWindowsMediaLibrarySharingDeviceProperty_head():
    class IWindowsMediaLibrarySharingDeviceProperty(win32more.System.Com.IDispatch_head):
        Guid = Guid('81e26927-7a7d-40a7-81d4-bddc02960e3e')
    return IWindowsMediaLibrarySharingDeviceProperty
def _define_IWindowsMediaLibrarySharingDeviceProperty():
    IWindowsMediaLibrarySharingDeviceProperty = win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDeviceProperty_head
    IWindowsMediaLibrarySharingDeviceProperty.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Name', ((1, 'name'),)))
    IWindowsMediaLibrarySharingDeviceProperty.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'get_Value', ((1, 'value'),)))
    win32more.System.Com.IDispatch
    return IWindowsMediaLibrarySharingDeviceProperty
def _define_IWindowsMediaLibrarySharingDeviceProperties_head():
    class IWindowsMediaLibrarySharingDeviceProperties(win32more.System.Com.IDispatch_head):
        Guid = Guid('c4623214-6b06-40c5-a623-b2ff4c076bfd')
    return IWindowsMediaLibrarySharingDeviceProperties
def _define_IWindowsMediaLibrarySharingDeviceProperties():
    IWindowsMediaLibrarySharingDeviceProperties = win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDeviceProperties_head
    IWindowsMediaLibrarySharingDeviceProperties.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDeviceProperty_head), use_last_error=False)(7, 'get_Item', ((1, 'index'),(1, 'property'),)))
    IWindowsMediaLibrarySharingDeviceProperties.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'count'),)))
    IWindowsMediaLibrarySharingDeviceProperties.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDeviceProperty_head), use_last_error=False)(9, 'GetProperty', ((1, 'name'),(1, 'property'),)))
    win32more.System.Com.IDispatch
    return IWindowsMediaLibrarySharingDeviceProperties
def _define_IWindowsMediaLibrarySharingDevice_head():
    class IWindowsMediaLibrarySharingDevice(win32more.System.Com.IDispatch_head):
        Guid = Guid('3dccc293-4fd9-4191-a25b-8e57c5d27bd4')
    return IWindowsMediaLibrarySharingDevice
def _define_IWindowsMediaLibrarySharingDevice():
    IWindowsMediaLibrarySharingDevice = win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDevice_head
    IWindowsMediaLibrarySharingDevice.get_DeviceID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_DeviceID', ((1, 'deviceID'),)))
    IWindowsMediaLibrarySharingDevice.get_Authorization = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.LibrarySharingServices.WindowsMediaLibrarySharingDeviceAuthorizationStatus), use_last_error=False)(8, 'get_Authorization', ((1, 'authorization'),)))
    IWindowsMediaLibrarySharingDevice.put_Authorization = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.LibrarySharingServices.WindowsMediaLibrarySharingDeviceAuthorizationStatus, use_last_error=False)(9, 'put_Authorization', ((1, 'authorization'),)))
    IWindowsMediaLibrarySharingDevice.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDeviceProperties_head), use_last_error=False)(10, 'get_Properties', ((1, 'deviceProperties'),)))
    win32more.System.Com.IDispatch
    return IWindowsMediaLibrarySharingDevice
def _define_IWindowsMediaLibrarySharingDevices_head():
    class IWindowsMediaLibrarySharingDevices(win32more.System.Com.IDispatch_head):
        Guid = Guid('1803f9d6-fe6d-4546-bf5b-992fe8ec12d1')
    return IWindowsMediaLibrarySharingDevices
def _define_IWindowsMediaLibrarySharingDevices():
    IWindowsMediaLibrarySharingDevices = win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDevices_head
    IWindowsMediaLibrarySharingDevices.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDevice_head), use_last_error=False)(7, 'get_Item', ((1, 'index'),(1, 'device'),)))
    IWindowsMediaLibrarySharingDevices.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'count'),)))
    IWindowsMediaLibrarySharingDevices.GetDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDevice_head), use_last_error=False)(9, 'GetDevice', ((1, 'deviceID'),(1, 'device'),)))
    win32more.System.Com.IDispatch
    return IWindowsMediaLibrarySharingDevices
def _define_IWindowsMediaLibrarySharingServices_head():
    class IWindowsMediaLibrarySharingServices(win32more.System.Com.IDispatch_head):
        Guid = Guid('01f5f85e-0a81-40da-a7c8-21ef3af8440c')
    return IWindowsMediaLibrarySharingServices
def _define_IWindowsMediaLibrarySharingServices():
    IWindowsMediaLibrarySharingServices = win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingServices_head
    IWindowsMediaLibrarySharingServices.showShareMediaCPL = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(7, 'showShareMediaCPL', ((1, 'device'),)))
    IWindowsMediaLibrarySharingServices.get_userHomeMediaSharingState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(8, 'get_userHomeMediaSharingState', ((1, 'sharingEnabled'),)))
    IWindowsMediaLibrarySharingServices.put_userHomeMediaSharingState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(9, 'put_userHomeMediaSharingState', ((1, 'sharingEnabled'),)))
    IWindowsMediaLibrarySharingServices.get_userHomeMediaSharingLibraryName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_userHomeMediaSharingLibraryName', ((1, 'libraryName'),)))
    IWindowsMediaLibrarySharingServices.put_userHomeMediaSharingLibraryName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(11, 'put_userHomeMediaSharingLibraryName', ((1, 'libraryName'),)))
    IWindowsMediaLibrarySharingServices.get_computerHomeMediaSharingAllowedState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(12, 'get_computerHomeMediaSharingAllowedState', ((1, 'sharingAllowed'),)))
    IWindowsMediaLibrarySharingServices.put_computerHomeMediaSharingAllowedState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(13, 'put_computerHomeMediaSharingAllowedState', ((1, 'sharingAllowed'),)))
    IWindowsMediaLibrarySharingServices.get_userInternetMediaSharingState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(14, 'get_userInternetMediaSharingState', ((1, 'sharingEnabled'),)))
    IWindowsMediaLibrarySharingServices.put_userInternetMediaSharingState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(15, 'put_userInternetMediaSharingState', ((1, 'sharingEnabled'),)))
    IWindowsMediaLibrarySharingServices.get_computerInternetMediaSharingAllowedState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(16, 'get_computerInternetMediaSharingAllowedState', ((1, 'sharingAllowed'),)))
    IWindowsMediaLibrarySharingServices.put_computerInternetMediaSharingAllowedState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(17, 'put_computerInternetMediaSharingAllowedState', ((1, 'sharingAllowed'),)))
    IWindowsMediaLibrarySharingServices.get_internetMediaSharingSecurityGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(18, 'get_internetMediaSharingSecurityGroup', ((1, 'securityGroup'),)))
    IWindowsMediaLibrarySharingServices.put_internetMediaSharingSecurityGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(19, 'put_internetMediaSharingSecurityGroup', ((1, 'securityGroup'),)))
    IWindowsMediaLibrarySharingServices.get_allowSharingToAllDevices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(20, 'get_allowSharingToAllDevices', ((1, 'sharingEnabled'),)))
    IWindowsMediaLibrarySharingServices.put_allowSharingToAllDevices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(21, 'put_allowSharingToAllDevices', ((1, 'sharingEnabled'),)))
    IWindowsMediaLibrarySharingServices.setDefaultAuthorization = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int16, use_last_error=False)(22, 'setDefaultAuthorization', ((1, 'MACAddresses'),(1, 'friendlyName'),(1, 'authorization'),)))
    IWindowsMediaLibrarySharingServices.setAuthorizationState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int16, use_last_error=False)(23, 'setAuthorizationState', ((1, 'MACAddress'),(1, 'authorizationState'),)))
    IWindowsMediaLibrarySharingServices.getAllDevices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Media.LibrarySharingServices.IWindowsMediaLibrarySharingDevices_head), use_last_error=False)(24, 'getAllDevices', ((1, 'devices'),)))
    IWindowsMediaLibrarySharingServices.get_customSettingsApplied = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(25, 'get_customSettingsApplied', ((1, 'customSettingsApplied'),)))
    win32more.System.Com.IDispatch
    return IWindowsMediaLibrarySharingServices
__all__ = [
    "WindowsMediaLibrarySharingServices",
    "WindowsMediaLibrarySharingDeviceAuthorizationStatus",
    "DEVICE_AUTHORIZATION_UNKNOWN",
    "DEVICE_AUTHORIZATION_ALLOWED",
    "DEVICE_AUTHORIZATION_DENIED",
    "IWindowsMediaLibrarySharingDeviceProperty",
    "IWindowsMediaLibrarySharingDeviceProperties",
    "IWindowsMediaLibrarySharingDevice",
    "IWindowsMediaLibrarySharingDevices",
    "IWindowsMediaLibrarySharingServices",
]
