from win32more import *
import win32more.Devices.FunctionDiscovery
import win32more.Foundation
import win32more.System.Com
import win32more.System.Com.StructuredStorage
import win32more.UI.Shell.PropertiesSystem

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.Devices.FunctionDiscovery, name, eval(f"_define_{name}()"))
    return getattr(win32more.Devices.FunctionDiscovery, name)
FD_EVENTID_PRIVATE = 100
FD_EVENTID = 1000
FD_EVENTID_SEARCHCOMPLETE = 1000
FD_EVENTID_ASYNCTHREADEXIT = 1001
FD_EVENTID_SEARCHSTART = 1002
FD_EVENTID_IPADDRESSCHANGE = 1003
FD_EVENTID_QUERYREFRESH = 1004
SID_PnpProvider = '8101368e-cabb-4426-acff-96c410812000'
SID_UPnPActivator = '0d0d66eb-cf74-4164-b52f-08344672dd46'
SID_EnumInterface = '40eab0b9-4d7f-4b53-a334-1581dd9041f4'
SID_PNPXPropertyStore = 'a86530b1-542f-439f-b71c-b0756b13677a'
SID_PNPXAssociation = 'cee8ccc9-4f6b-4469-a235-5a22869eef03'
SID_PNPXServiceCollection = '439e80ee-a217-4712-9fa6-deabd9c2a727'
SID_FDPairingHandler = '383b69fa-5486-49da-91f5-d63c24c8e9d0'
SID_EnumDeviceFunction = '13e0e9e2-c3fa-4e3c-906e-64502fa4dc95'
SID_UnpairProvider = '89a502fc-857b-4698-a0b7-027192002f9e'
SID_DeviceDisplayStatusManager = 'f59aa553-8309-46ca-9736-1ac3c62d6031'
SID_FunctionDiscoveryProviderRefresh = '2b4cbdc9-31c4-40d4-a62d-772aa174ed52'
SID_UninstallDeviceFunction = 'c920566e-5671-4496-8025-bf0b89bd44cd'
FMTID_FD = '904b03a2-471d-423c-a584-f3483238a146'
FD_Visibility_Default = 0
FD_Visibility_Hidden = 1
FMTID_Device = '78c34fc8-104a-4aca-9ea4-524d52996e57'
FMTID_DeviceInterface = '53808008-07bb-4661-bc3c-b5953e708560'
FMTID_Pairing = '8807cae6-7db6-4f10-8ee4-435eaa1392bc'
FMTID_WSD = '92506491-ff95-4724-a05a-5b81885a7c92'
FMTID_PNPX = '656a3bb3-ecc0-43fd-8477-4ae0404a96cd'
FMTID_PNPXDynamicProperty = '4fc5077e-b686-44be-93e3-86cafe368ccd'
PNPX_INSTALLSTATE_NOTINSTALLED = 0
PNPX_INSTALLSTATE_INSTALLED = 1
PNPX_INSTALLSTATE_INSTALLING = 2
PNPX_INSTALLSTATE_FAILED = 3
FD_LONGHORN = 1
MAX_FDCONSTRAINTNAME_LENGTH = 100
MAX_FDCONSTRAINTVALUE_LENGTH = 1000
E_FDPAIRING_NOCONNECTION = -1882193919
E_FDPAIRING_HWFAILURE = -1882193918
E_FDPAIRING_AUTHFAILURE = -1882193917
E_FDPAIRING_CONNECTTIMEOUT = -1882193916
E_FDPAIRING_TOOMANYCONNECTIONS = -1882193915
E_FDPAIRING_AUTHNOTALLOWED = -1882193914
E_FDPAIRING_IPBUSDISABLED = -1882193913
E_FDPAIRING_NOPROFILES = -1882193912
PropertyConstraint = Int32
QC_EQUALS = 0
QC_NOTEQUAL = 1
QC_LESSTHAN = 2
QC_LESSTHANOREQUAL = 3
QC_GREATERTHAN = 4
QC_GREATERTHANOREQUAL = 5
QC_STARTSWITH = 6
QC_EXISTS = 7
QC_DOESNOTEXIST = 8
QC_CONTAINS = 9
SystemVisibilityFlags = Int32
SVF_SYSTEM = 0
SVF_USER = 1
QueryUpdateAction = Int32
QUA_ADD = 0
QUA_REMOVE = 1
QUA_CHANGE = 2
QueryCategoryType = Int32
QCT_PROVIDER = 0
QCT_LAYERED = 1
def _define_IFunctionDiscoveryNotification_head():
    class IFunctionDiscoveryNotification(win32more.System.Com.IUnknown_head):
        Guid = Guid('5f6c1ba8-5330-422e-a368-572b244d3f87')
    return IFunctionDiscoveryNotification
def _define_IFunctionDiscoveryNotification():
    IFunctionDiscoveryNotification = win32more.Devices.FunctionDiscovery.IFunctionDiscoveryNotification_head
    IFunctionDiscoveryNotification.OnUpdate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.QueryUpdateAction,UInt64,win32more.Devices.FunctionDiscovery.IFunctionInstance_head, use_last_error=False)(3, 'OnUpdate', ((1, 'enumQueryUpdateAction'),(1, 'fdqcQueryContext'),(1, 'pIFunctionInstance'),)))
    IFunctionDiscoveryNotification.OnError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,UInt64,win32more.Foundation.PWSTR, use_last_error=False)(4, 'OnError', ((1, 'hr'),(1, 'fdqcQueryContext'),(1, 'pszProvider'),)))
    IFunctionDiscoveryNotification.OnEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt64,win32more.Foundation.PWSTR, use_last_error=False)(5, 'OnEvent', ((1, 'dwEventID'),(1, 'fdqcQueryContext'),(1, 'pszProvider'),)))
    return IFunctionDiscoveryNotification
def _define_IFunctionDiscovery_head():
    class IFunctionDiscovery(win32more.System.Com.IUnknown_head):
        Guid = Guid('4df99b70-e148-4432-b004-4c9eeb535a5e')
    return IFunctionDiscovery
def _define_IFunctionDiscovery():
    IFunctionDiscovery = win32more.Devices.FunctionDiscovery.IFunctionDiscovery_head
    IFunctionDiscovery.GetInstanceCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstanceCollection_head), use_last_error=False)(3, 'GetInstanceCollection', ((1, 'pszCategory'),(1, 'pszSubCategory'),(1, 'fIncludeAllSubCategories'),(1, 'ppIFunctionInstanceCollection'),)))
    IFunctionDiscovery.GetInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstance_head), use_last_error=False)(4, 'GetInstance', ((1, 'pszFunctionInstanceIdentity'),(1, 'ppIFunctionInstance'),)))
    IFunctionDiscovery.CreateInstanceCollectionQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,win32more.Devices.FunctionDiscovery.IFunctionDiscoveryNotification_head,POINTER(UInt64),POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstanceCollectionQuery_head), use_last_error=False)(5, 'CreateInstanceCollectionQuery', ((1, 'pszCategory'),(1, 'pszSubCategory'),(1, 'fIncludeAllSubCategories'),(1, 'pIFunctionDiscoveryNotification'),(1, 'pfdqcQueryContext'),(1, 'ppIFunctionInstanceCollectionQuery'),)))
    IFunctionDiscovery.CreateInstanceQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.FunctionDiscovery.IFunctionDiscoveryNotification_head,POINTER(UInt64),POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstanceQuery_head), use_last_error=False)(6, 'CreateInstanceQuery', ((1, 'pszFunctionInstanceIdentity'),(1, 'pIFunctionDiscoveryNotification'),(1, 'pfdqcQueryContext'),(1, 'ppIFunctionInstanceQuery'),)))
    IFunctionDiscovery.AddInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.SystemVisibilityFlags,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstance_head), use_last_error=False)(7, 'AddInstance', ((1, 'enumSystemVisibility'),(1, 'pszCategory'),(1, 'pszSubCategory'),(1, 'pszCategoryIdentity'),(1, 'ppIFunctionInstance'),)))
    IFunctionDiscovery.RemoveInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.SystemVisibilityFlags,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(8, 'RemoveInstance', ((1, 'enumSystemVisibility'),(1, 'pszCategory'),(1, 'pszSubCategory'),(1, 'pszCategoryIdentity'),)))
    return IFunctionDiscovery
def _define_IFunctionInstance_head():
    class IFunctionInstance(win32more.System.Com.IServiceProvider_head):
        Guid = Guid('33591c10-0bed-4f02-b0ab-1530d5533ee9')
    return IFunctionInstance
def _define_IFunctionInstance():
    IFunctionInstance = win32more.Devices.FunctionDiscovery.IFunctionInstance_head
    IFunctionInstance.GetID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)), use_last_error=False)(4, 'GetID', ((1, 'ppszCoMemIdentity'),)))
    IFunctionInstance.GetProviderInstanceID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)), use_last_error=False)(5, 'GetProviderInstanceID', ((1, 'ppszCoMemProviderInstanceIdentity'),)))
    IFunctionInstance.OpenPropertyStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head), use_last_error=False)(6, 'OpenPropertyStore', ((1, 'dwStgAccess'),(1, 'ppIPropertyStore'),)))
    IFunctionInstance.GetCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)),POINTER(POINTER(UInt16)), use_last_error=False)(7, 'GetCategory', ((1, 'ppszCoMemCategory'),(1, 'ppszCoMemSubCategory'),)))
    return IFunctionInstance
def _define_IFunctionInstanceCollection_head():
    class IFunctionInstanceCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('f0a3d895-855c-42a2-948d-2f97d450ecb1')
    return IFunctionInstanceCollection
def _define_IFunctionInstanceCollection():
    IFunctionInstanceCollection = win32more.Devices.FunctionDiscovery.IFunctionInstanceCollection_head
    IFunctionInstanceCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetCount', ((1, 'pdwCount'),)))
    IFunctionInstanceCollection.Get = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstance_head), use_last_error=False)(4, 'Get', ((1, 'pszInstanceIdentity'),(1, 'pdwIndex'),(1, 'ppIFunctionInstance'),)))
    IFunctionInstanceCollection.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstance_head), use_last_error=False)(5, 'Item', ((1, 'dwIndex'),(1, 'ppIFunctionInstance'),)))
    IFunctionInstanceCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head, use_last_error=False)(6, 'Add', ((1, 'pIFunctionInstance'),)))
    IFunctionInstanceCollection.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstance_head), use_last_error=False)(7, 'Remove', ((1, 'dwIndex'),(1, 'ppIFunctionInstance'),)))
    IFunctionInstanceCollection.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(8, 'Delete', ((1, 'dwIndex'),)))
    IFunctionInstanceCollection.DeleteAll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'DeleteAll', ()))
    return IFunctionInstanceCollection
def _define_IPropertyStoreCollection_head():
    class IPropertyStoreCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('d14d9c30-12d2-42d8-bce4-c60c2bb226fa')
    return IPropertyStoreCollection
def _define_IPropertyStoreCollection():
    IPropertyStoreCollection = win32more.Devices.FunctionDiscovery.IPropertyStoreCollection_head
    IPropertyStoreCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetCount', ((1, 'pdwCount'),)))
    IPropertyStoreCollection.Get = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head), use_last_error=False)(4, 'Get', ((1, 'pszInstanceIdentity'),(1, 'pdwIndex'),(1, 'ppIPropertyStore'),)))
    IPropertyStoreCollection.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head), use_last_error=False)(5, 'Item', ((1, 'dwIndex'),(1, 'ppIPropertyStore'),)))
    IPropertyStoreCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Shell.PropertiesSystem.IPropertyStore_head, use_last_error=False)(6, 'Add', ((1, 'pIPropertyStore'),)))
    IPropertyStoreCollection.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head), use_last_error=False)(7, 'Remove', ((1, 'dwIndex'),(1, 'pIPropertyStore'),)))
    IPropertyStoreCollection.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(8, 'Delete', ((1, 'dwIndex'),)))
    IPropertyStoreCollection.DeleteAll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'DeleteAll', ()))
    return IPropertyStoreCollection
def _define_IFunctionInstanceQuery_head():
    class IFunctionInstanceQuery(win32more.System.Com.IUnknown_head):
        Guid = Guid('6242bc6b-90ec-4b37-bb46-e229fd84ed95')
    return IFunctionInstanceQuery
def _define_IFunctionInstanceQuery():
    IFunctionInstanceQuery = win32more.Devices.FunctionDiscovery.IFunctionInstanceQuery_head
    IFunctionInstanceQuery.Execute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstance_head), use_last_error=False)(3, 'Execute', ((1, 'ppIFunctionInstance'),)))
    return IFunctionInstanceQuery
def _define_IFunctionInstanceCollectionQuery_head():
    class IFunctionInstanceCollectionQuery(win32more.System.Com.IUnknown_head):
        Guid = Guid('57cc6fd2-c09a-4289-bb72-25f04142058e')
    return IFunctionInstanceCollectionQuery
def _define_IFunctionInstanceCollectionQuery():
    IFunctionInstanceCollectionQuery = win32more.Devices.FunctionDiscovery.IFunctionInstanceCollectionQuery_head
    IFunctionInstanceCollectionQuery.AddQueryConstraint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(3, 'AddQueryConstraint', ((1, 'pszConstraintName'),(1, 'pszConstraintValue'),)))
    IFunctionInstanceCollectionQuery.AddPropertyConstraint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.Devices.FunctionDiscovery.PropertyConstraint, use_last_error=False)(4, 'AddPropertyConstraint', ((1, 'Key'),(1, 'pv'),(1, 'enumPropertyConstraint'),)))
    IFunctionInstanceCollectionQuery.Execute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstanceCollection_head), use_last_error=False)(5, 'Execute', ((1, 'ppIFunctionInstanceCollection'),)))
    return IFunctionInstanceCollectionQuery
def _define_IFunctionDiscoveryProvider_head():
    class IFunctionDiscoveryProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcde394f-1478-4813-a402-f6fb10657222')
    return IFunctionDiscoveryProvider
def _define_IFunctionDiscoveryProvider():
    IFunctionDiscoveryProvider = win32more.Devices.FunctionDiscovery.IFunctionDiscoveryProvider_head
    IFunctionDiscoveryProvider.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionDiscoveryProviderFactory_head,win32more.Devices.FunctionDiscovery.IFunctionDiscoveryNotification_head,UInt32,POINTER(UInt32), use_last_error=False)(3, 'Initialize', ((1, 'pIFunctionDiscoveryProviderFactory'),(1, 'pIFunctionDiscoveryNotification'),(1, 'lcidUserDefault'),(1, 'pdwStgAccessCapabilities'),)))
    IFunctionDiscoveryProvider.Query = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionDiscoveryProviderQuery_head,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstanceCollection_head), use_last_error=False)(4, 'Query', ((1, 'pIFunctionDiscoveryProviderQuery'),(1, 'ppIFunctionInstanceCollection'),)))
    IFunctionDiscoveryProvider.EndQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'EndQuery', ()))
    IFunctionDiscoveryProvider.InstancePropertyStoreValidateAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,IntPtr,UInt32, use_last_error=False)(6, 'InstancePropertyStoreValidateAccess', ((1, 'pIFunctionInstance'),(1, 'iProviderInstanceContext'),(1, 'dwStgAccess'),)))
    IFunctionDiscoveryProvider.InstancePropertyStoreOpen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,IntPtr,UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head), use_last_error=False)(7, 'InstancePropertyStoreOpen', ((1, 'pIFunctionInstance'),(1, 'iProviderInstanceContext'),(1, 'dwStgAccess'),(1, 'ppIPropertyStore'),)))
    IFunctionDiscoveryProvider.InstancePropertyStoreFlush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,IntPtr, use_last_error=False)(8, 'InstancePropertyStoreFlush', ((1, 'pIFunctionInstance'),(1, 'iProviderInstanceContext'),)))
    IFunctionDiscoveryProvider.InstanceQueryService = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,IntPtr,POINTER(Guid),POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'InstanceQueryService', ((1, 'pIFunctionInstance'),(1, 'iProviderInstanceContext'),(1, 'guidService'),(1, 'riid'),(1, 'ppIUnknown'),)))
    IFunctionDiscoveryProvider.InstanceReleased = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,IntPtr, use_last_error=False)(10, 'InstanceReleased', ((1, 'pIFunctionInstance'),(1, 'iProviderInstanceContext'),)))
    return IFunctionDiscoveryProvider
def _define_IProviderProperties_head():
    class IProviderProperties(win32more.System.Com.IUnknown_head):
        Guid = Guid('cf986ea6-3b5f-4c5f-b88a-2f8b20ceef17')
    return IProviderProperties
def _define_IProviderProperties():
    IProviderProperties = win32more.Devices.FunctionDiscovery.IProviderProperties_head
    IProviderProperties.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,IntPtr,POINTER(UInt32), use_last_error=False)(3, 'GetCount', ((1, 'pIFunctionInstance'),(1, 'iProviderInstanceContext'),(1, 'pdwCount'),)))
    IProviderProperties.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,IntPtr,UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), use_last_error=False)(4, 'GetAt', ((1, 'pIFunctionInstance'),(1, 'iProviderInstanceContext'),(1, 'dwIndex'),(1, 'pKey'),)))
    IProviderProperties.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,IntPtr,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(5, 'GetValue', ((1, 'pIFunctionInstance'),(1, 'iProviderInstanceContext'),(1, 'Key'),(1, 'ppropVar'),)))
    IProviderProperties.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,IntPtr,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(6, 'SetValue', ((1, 'pIFunctionInstance'),(1, 'iProviderInstanceContext'),(1, 'Key'),(1, 'ppropVar'),)))
    return IProviderProperties
def _define_IProviderPublishing_head():
    class IProviderPublishing(win32more.System.Com.IUnknown_head):
        Guid = Guid('cd1b9a04-206c-4a05-a0c8-1635a21a2b7c')
    return IProviderPublishing
def _define_IProviderPublishing():
    IProviderPublishing = win32more.Devices.FunctionDiscovery.IProviderPublishing_head
    IProviderPublishing.CreateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.SystemVisibilityFlags,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstance_head), use_last_error=False)(3, 'CreateInstance', ((1, 'enumVisibilityFlags'),(1, 'pszSubCategory'),(1, 'pszProviderInstanceIdentity'),(1, 'ppIFunctionInstance'),)))
    IProviderPublishing.RemoveInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.SystemVisibilityFlags,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(4, 'RemoveInstance', ((1, 'enumVisibilityFlags'),(1, 'pszSubCategory'),(1, 'pszProviderInstanceIdentity'),)))
    return IProviderPublishing
def _define_IFunctionDiscoveryProviderFactory_head():
    class IFunctionDiscoveryProviderFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('86443ff0-1ad5-4e68-a45a-40c2c329de3b')
    return IFunctionDiscoveryProviderFactory
def _define_IFunctionDiscoveryProviderFactory():
    IFunctionDiscoveryProviderFactory = win32more.Devices.FunctionDiscovery.IFunctionDiscoveryProviderFactory_head
    IFunctionDiscoveryProviderFactory.CreatePropertyStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.IPropertyStore_head), use_last_error=False)(3, 'CreatePropertyStore', ((1, 'ppIPropertyStore'),)))
    IFunctionDiscoveryProviderFactory.CreateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,IntPtr,win32more.UI.Shell.PropertiesSystem.IPropertyStore_head,win32more.Devices.FunctionDiscovery.IFunctionDiscoveryProvider_head,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstance_head), use_last_error=False)(4, 'CreateInstance', ((1, 'pszSubCategory'),(1, 'pszProviderInstanceIdentity'),(1, 'iProviderInstanceContext'),(1, 'pIPropertyStore'),(1, 'pIFunctionDiscoveryProvider'),(1, 'ppIFunctionInstance'),)))
    IFunctionDiscoveryProviderFactory.CreateFunctionInstanceCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.FunctionDiscovery.IFunctionInstanceCollection_head), use_last_error=False)(5, 'CreateFunctionInstanceCollection', ((1, 'ppIFunctionInstanceCollection'),)))
    return IFunctionDiscoveryProviderFactory
def _define_IFunctionDiscoveryProviderQuery_head():
    class IFunctionDiscoveryProviderQuery(win32more.System.Com.IUnknown_head):
        Guid = Guid('6876ea98-baec-46db-bc20-75a76e267a3a')
    return IFunctionDiscoveryProviderQuery
def _define_IFunctionDiscoveryProviderQuery():
    IFunctionDiscoveryProviderQuery = win32more.Devices.FunctionDiscovery.IFunctionDiscoveryProviderQuery_head
    IFunctionDiscoveryProviderQuery.IsInstanceQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),POINTER(POINTER(UInt16)), use_last_error=False)(3, 'IsInstanceQuery', ((1, 'pisInstanceQuery'),(1, 'ppszConstraintValue'),)))
    IFunctionDiscoveryProviderQuery.IsSubcategoryQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),POINTER(POINTER(UInt16)), use_last_error=False)(4, 'IsSubcategoryQuery', ((1, 'pisSubcategoryQuery'),(1, 'ppszConstraintValue'),)))
    IFunctionDiscoveryProviderQuery.GetQueryConstraints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.FunctionDiscovery.IProviderQueryConstraintCollection_head), use_last_error=False)(5, 'GetQueryConstraints', ((1, 'ppIProviderQueryConstraints'),)))
    IFunctionDiscoveryProviderQuery.GetPropertyConstraints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.FunctionDiscovery.IProviderPropertyConstraintCollection_head), use_last_error=False)(6, 'GetPropertyConstraints', ((1, 'ppIProviderPropertyConstraints'),)))
    return IFunctionDiscoveryProviderQuery
def _define_IProviderQueryConstraintCollection_head():
    class IProviderQueryConstraintCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('9c243e11-3261-4bcd-b922-84a873d460ae')
    return IProviderQueryConstraintCollection
def _define_IProviderQueryConstraintCollection():
    IProviderQueryConstraintCollection = win32more.Devices.FunctionDiscovery.IProviderQueryConstraintCollection_head
    IProviderQueryConstraintCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetCount', ((1, 'pdwCount'),)))
    IProviderQueryConstraintCollection.Get = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(POINTER(UInt16)), use_last_error=False)(4, 'Get', ((1, 'pszConstraintName'),(1, 'ppszConstraintValue'),)))
    IProviderQueryConstraintCollection.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(UInt16)),POINTER(POINTER(UInt16)), use_last_error=False)(5, 'Item', ((1, 'dwIndex'),(1, 'ppszConstraintName'),(1, 'ppszConstraintValue'),)))
    IProviderQueryConstraintCollection.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)),POINTER(POINTER(UInt16)), use_last_error=False)(6, 'Next', ((1, 'ppszConstraintName'),(1, 'ppszConstraintValue'),)))
    IProviderQueryConstraintCollection.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Skip', ()))
    IProviderQueryConstraintCollection.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Reset', ()))
    return IProviderQueryConstraintCollection
def _define_IProviderPropertyConstraintCollection_head():
    class IProviderPropertyConstraintCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('f4fae42f-5778-4a13-8540-b5fd8c1398dd')
    return IProviderPropertyConstraintCollection
def _define_IProviderPropertyConstraintCollection():
    IProviderPropertyConstraintCollection = win32more.Devices.FunctionDiscovery.IProviderPropertyConstraintCollection_head
    IProviderPropertyConstraintCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetCount', ((1, 'pdwCount'),)))
    IProviderPropertyConstraintCollection.Get = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(UInt32), use_last_error=False)(4, 'Get', ((1, 'Key'),(1, 'pPropVar'),(1, 'pdwPropertyConstraint'),)))
    IProviderPropertyConstraintCollection.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(UInt32), use_last_error=False)(5, 'Item', ((1, 'dwIndex'),(1, 'pKey'),(1, 'pPropVar'),(1, 'pdwPropertyConstraint'),)))
    IProviderPropertyConstraintCollection.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(UInt32), use_last_error=False)(6, 'Next', ((1, 'pKey'),(1, 'pPropVar'),(1, 'pdwPropertyConstraint'),)))
    IProviderPropertyConstraintCollection.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Skip', ()))
    IProviderPropertyConstraintCollection.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Reset', ()))
    return IProviderPropertyConstraintCollection
def _define_IFunctionDiscoveryServiceProvider_head():
    class IFunctionDiscoveryServiceProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('4c81ed02-1b04-43f2-a451-69966cbcd1c2')
    return IFunctionDiscoveryServiceProvider
def _define_IFunctionDiscoveryServiceProvider():
    IFunctionDiscoveryServiceProvider = win32more.Devices.FunctionDiscovery.IFunctionDiscoveryServiceProvider_head
    IFunctionDiscoveryServiceProvider.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.FunctionDiscovery.IFunctionInstance_head,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(3, 'Initialize', ((1, 'pIFunctionInstance'),(1, 'riid'),(1, 'ppv'),)))
    return IFunctionDiscoveryServiceProvider
PNPXAssociation = Guid('cee8ccc9-4f6b-4469-a235-5a22869eef03')
PNPXPairingHandler = Guid('b8a27942-ade7-4085-aa6e-4fadc7ada1ef')
def _define_IPNPXAssociation_head():
    class IPNPXAssociation(win32more.System.Com.IUnknown_head):
        Guid = Guid('0bd7e521-4da6-42d5-81ba-1981b6b94075')
    return IPNPXAssociation
def _define_IPNPXAssociation():
    IPNPXAssociation = win32more.Devices.FunctionDiscovery.IPNPXAssociation_head
    IPNPXAssociation.Associate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(3, 'Associate', ((1, 'pszSubcategory'),)))
    IPNPXAssociation.Unassociate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(4, 'Unassociate', ((1, 'pszSubcategory'),)))
    IPNPXAssociation.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(5, 'Delete', ((1, 'pszSubcategory'),)))
    return IPNPXAssociation
def _define_IPNPXDeviceAssociation_head():
    class IPNPXDeviceAssociation(win32more.System.Com.IUnknown_head):
        Guid = Guid('eed366d0-35b8-4fc5-8d20-7e5bd31f6ded')
    return IPNPXDeviceAssociation
def _define_IPNPXDeviceAssociation():
    IPNPXDeviceAssociation = win32more.Devices.FunctionDiscovery.IPNPXDeviceAssociation_head
    IPNPXDeviceAssociation.Associate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.FunctionDiscovery.IFunctionDiscoveryNotification_head, use_last_error=False)(3, 'Associate', ((1, 'pszSubCategory'),(1, 'pIFunctionDiscoveryNotification'),)))
    IPNPXDeviceAssociation.Unassociate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.FunctionDiscovery.IFunctionDiscoveryNotification_head, use_last_error=False)(4, 'Unassociate', ((1, 'pszSubCategory'),(1, 'pIFunctionDiscoveryNotification'),)))
    IPNPXDeviceAssociation.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Devices.FunctionDiscovery.IFunctionDiscoveryNotification_head, use_last_error=False)(5, 'Delete', ((1, 'pszSubcategory'),(1, 'pIFunctionDiscoveryNotification'),)))
    return IPNPXDeviceAssociation
FunctionDiscovery = Guid('c72be2ec-8e90-452c-b29a-ab8ff1c071fc')
PropertyStore = Guid('e4796550-df61-448b-9193-13fc1341b163')
FunctionInstanceCollection = Guid('ba818ce5-b55f-443f-ad39-2fe89be6191f')
PropertyStoreCollection = Guid('edd36029-d753-4862-aa5b-5bccad2a4d29')
__all__ = [
    "FD_EVENTID_PRIVATE",
    "FD_EVENTID",
    "FD_EVENTID_SEARCHCOMPLETE",
    "FD_EVENTID_ASYNCTHREADEXIT",
    "FD_EVENTID_SEARCHSTART",
    "FD_EVENTID_IPADDRESSCHANGE",
    "FD_EVENTID_QUERYREFRESH",
    "SID_PnpProvider",
    "SID_UPnPActivator",
    "SID_EnumInterface",
    "SID_PNPXPropertyStore",
    "SID_PNPXAssociation",
    "SID_PNPXServiceCollection",
    "SID_FDPairingHandler",
    "SID_EnumDeviceFunction",
    "SID_UnpairProvider",
    "SID_DeviceDisplayStatusManager",
    "SID_FunctionDiscoveryProviderRefresh",
    "SID_UninstallDeviceFunction",
    "FMTID_FD",
    "FD_Visibility_Default",
    "FD_Visibility_Hidden",
    "FMTID_Device",
    "FMTID_DeviceInterface",
    "FMTID_Pairing",
    "FMTID_WSD",
    "FMTID_PNPX",
    "FMTID_PNPXDynamicProperty",
    "PNPX_INSTALLSTATE_NOTINSTALLED",
    "PNPX_INSTALLSTATE_INSTALLED",
    "PNPX_INSTALLSTATE_INSTALLING",
    "PNPX_INSTALLSTATE_FAILED",
    "FD_LONGHORN",
    "MAX_FDCONSTRAINTNAME_LENGTH",
    "MAX_FDCONSTRAINTVALUE_LENGTH",
    "E_FDPAIRING_NOCONNECTION",
    "E_FDPAIRING_HWFAILURE",
    "E_FDPAIRING_AUTHFAILURE",
    "E_FDPAIRING_CONNECTTIMEOUT",
    "E_FDPAIRING_TOOMANYCONNECTIONS",
    "E_FDPAIRING_AUTHNOTALLOWED",
    "E_FDPAIRING_IPBUSDISABLED",
    "E_FDPAIRING_NOPROFILES",
    "PropertyConstraint",
    "QC_EQUALS",
    "QC_NOTEQUAL",
    "QC_LESSTHAN",
    "QC_LESSTHANOREQUAL",
    "QC_GREATERTHAN",
    "QC_GREATERTHANOREQUAL",
    "QC_STARTSWITH",
    "QC_EXISTS",
    "QC_DOESNOTEXIST",
    "QC_CONTAINS",
    "SystemVisibilityFlags",
    "SVF_SYSTEM",
    "SVF_USER",
    "QueryUpdateAction",
    "QUA_ADD",
    "QUA_REMOVE",
    "QUA_CHANGE",
    "QueryCategoryType",
    "QCT_PROVIDER",
    "QCT_LAYERED",
    "IFunctionDiscoveryNotification",
    "IFunctionDiscovery",
    "IFunctionInstance",
    "IFunctionInstanceCollection",
    "IPropertyStoreCollection",
    "IFunctionInstanceQuery",
    "IFunctionInstanceCollectionQuery",
    "IFunctionDiscoveryProvider",
    "IProviderProperties",
    "IProviderPublishing",
    "IFunctionDiscoveryProviderFactory",
    "IFunctionDiscoveryProviderQuery",
    "IProviderQueryConstraintCollection",
    "IProviderPropertyConstraintCollection",
    "IFunctionDiscoveryServiceProvider",
    "PNPXAssociation",
    "PNPXPairingHandler",
    "IPNPXAssociation",
    "IPNPXDeviceAssociation",
    "FunctionDiscovery",
    "PropertyStore",
    "FunctionInstanceCollection",
    "PropertyStoreCollection",
]
