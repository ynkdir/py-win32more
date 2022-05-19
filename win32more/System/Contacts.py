from win32more import *
import win32more.Foundation
import win32more.System.Com
import win32more.System.Contacts

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
CGD_DEFAULT = 0
CGD_UNKNOWN_PROPERTY = 0
CGD_STRING_PROPERTY = 1
CGD_DATE_PROPERTY = 2
CGD_BINARY_PROPERTY = 4
CGD_ARRAY_NODE = 8
CLSID_ContactAggregationManager = '96c8ad95-c199-44de-b34e-ac33c442df39'
Contact = Guid('61b68808-8eee-4fd1-acb8-3d804c8db056')
ContactManager = Guid('7165c8ab-af88-42bd-86fd-5310b4285a02')
def _define_IContactManager_head():
    class IContactManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('ad553d98-deb1-474a-8e17-fc0c2075b738')
    return IContactManager
def _define_IContactManager():
    IContactManager = win32more.System.Contacts.IContactManager_head
    IContactManager.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(3, 'Initialize', ((1, 'pszAppName'),(1, 'pszAppVersion'),)))
    IContactManager.Load = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Contacts.IContact_head), use_last_error=False)(4, 'Load', ((1, 'pszContactID'),(1, 'ppContact'),)))
    IContactManager.MergeContactIDs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(5, 'MergeContactIDs', ((1, 'pszNewContactID'),(1, 'pszOldContactID'),)))
    IContactManager.GetMeContact = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContact_head), use_last_error=False)(6, 'GetMeContact', ((1, 'ppMeContact'),)))
    IContactManager.SetMeContact = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Contacts.IContact_head, use_last_error=False)(7, 'SetMeContact', ((1, 'pMeContact'),)))
    IContactManager.GetContactCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactCollection_head), use_last_error=False)(8, 'GetContactCollection', ((1, 'ppContactCollection'),)))
    return IContactManager
def _define_IContactCollection_head():
    class IContactCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('b6afa338-d779-11d9-8bde-f66bad1e3f3a')
    return IContactCollection
def _define_IContactCollection():
    IContactCollection = win32more.System.Contacts.IContactCollection_head
    IContactCollection.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Reset', ()))
    IContactCollection.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Next', ()))
    IContactCollection.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContact_head), use_last_error=False)(5, 'GetCurrent', ((1, 'ppContact'),)))
    return IContactCollection
def _define_IContactProperties_head():
    class IContactProperties(win32more.System.Com.IUnknown_head):
        Guid = Guid('70dd27dd-5cbd-46e8-bef0-23b6b346288f')
    return IContactProperties
def _define_IContactProperties():
    IContactProperties = win32more.System.Contacts.IContactProperties_head
    IContactProperties.GetString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(Char),UInt32,POINTER(UInt32), use_last_error=False)(3, 'GetString', ((1, 'pszPropertyName'),(1, 'dwFlags'),(1, 'pszValue'),(1, 'cchValue'),(1, 'pdwcchPropertyValueRequired'),)))
    IContactProperties.GetDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(4, 'GetDate', ((1, 'pszPropertyName'),(1, 'dwFlags'),(1, 'pftDateTime'),)))
    IContactProperties.GetBinary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(Char),UInt32,POINTER(UInt32),POINTER(win32more.System.Com.IStream_head), use_last_error=False)(5, 'GetBinary', ((1, 'pszPropertyName'),(1, 'dwFlags'),(1, 'pszContentType'),(1, 'cchContentType'),(1, 'pdwcchContentTypeRequired'),(1, 'ppStream'),)))
    IContactProperties.GetLabels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(Char),UInt32,POINTER(UInt32), use_last_error=False)(6, 'GetLabels', ((1, 'pszArrayElementName'),(1, 'dwFlags'),(1, 'pszLabels'),(1, 'cchLabels'),(1, 'pdwcchLabelsRequired'),)))
    IContactProperties.SetString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(7, 'SetString', ((1, 'pszPropertyName'),(1, 'dwFlags'),(1, 'pszValue'),)))
    IContactProperties.SetDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.FILETIME, use_last_error=False)(8, 'SetDate', ((1, 'pszPropertyName'),(1, 'dwFlags'),(1, 'ftDateTime'),)))
    IContactProperties.SetBinary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,win32more.System.Com.IStream_head, use_last_error=False)(9, 'SetBinary', ((1, 'pszPropertyName'),(1, 'dwFlags'),(1, 'pszContentType'),(1, 'pStream'),)))
    IContactProperties.SetLabels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(10, 'SetLabels', ((1, 'pszArrayElementName'),(1, 'dwFlags'),(1, 'dwLabelCount'),(1, 'ppszLabels'),)))
    IContactProperties.CreateArrayNode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.BOOL,POINTER(Char),UInt32,POINTER(UInt32), use_last_error=False)(11, 'CreateArrayNode', ((1, 'pszArrayName'),(1, 'dwFlags'),(1, 'fAppend'),(1, 'pszNewArrayElementName'),(1, 'cchNewArrayElementName'),(1, 'pdwcchNewArrayElementNameRequired'),)))
    IContactProperties.DeleteProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(12, 'DeleteProperty', ((1, 'pszPropertyName'),(1, 'dwFlags'),)))
    IContactProperties.DeleteArrayNode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(13, 'DeleteArrayNode', ((1, 'pszArrayElementName'),(1, 'dwFlags'),)))
    IContactProperties.DeleteLabels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(14, 'DeleteLabels', ((1, 'pszArrayElementName'),(1, 'dwFlags'),)))
    IContactProperties.GetPropertyCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactPropertyCollection_head),UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Foundation.PWSTR),win32more.Foundation.BOOL, use_last_error=False)(15, 'GetPropertyCollection', ((1, 'ppPropertyCollection'),(1, 'dwFlags'),(1, 'pszMultiValueName'),(1, 'dwLabelCount'),(1, 'ppszLabels'),(1, 'fAnyLabelMatches'),)))
    return IContactProperties
def _define_IContact_head():
    class IContact(win32more.System.Com.IUnknown_head):
        Guid = Guid('f941b671-bda7-4f77-884a-f46462f226a7')
    return IContact
def _define_IContact():
    IContact = win32more.System.Contacts.IContact_head
    IContact.GetContactID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32,POINTER(UInt32), use_last_error=False)(3, 'GetContactID', ((1, 'pszContactID'),(1, 'cchContactID'),(1, 'pdwcchContactIDRequired'),)))
    IContact.GetPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32,POINTER(UInt32), use_last_error=False)(4, 'GetPath', ((1, 'pszPath'),(1, 'cchPath'),(1, 'pdwcchPathRequired'),)))
    IContact.CommitChanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'CommitChanges', ((1, 'dwCommitFlags'),)))
    return IContact
def _define_IContactPropertyCollection_head():
    class IContactPropertyCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('ffd3adf8-fa64-4328-b1b6-2e0db509cb3c')
    return IContactPropertyCollection
def _define_IContactPropertyCollection():
    IContactPropertyCollection = win32more.System.Contacts.IContactPropertyCollection_head
    IContactPropertyCollection.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Reset', ()))
    IContactPropertyCollection.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Next', ()))
    IContactPropertyCollection.GetPropertyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32,POINTER(UInt32), use_last_error=False)(5, 'GetPropertyName', ((1, 'pszPropertyName'),(1, 'cchPropertyName'),(1, 'pdwcchPropertyNameRequired'),)))
    IContactPropertyCollection.GetPropertyType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'GetPropertyType', ((1, 'pdwType'),)))
    IContactPropertyCollection.GetPropertyVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(7, 'GetPropertyVersion', ((1, 'pdwVersion'),)))
    IContactPropertyCollection.GetPropertyModificationDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(8, 'GetPropertyModificationDate', ((1, 'pftModificationDate'),)))
    IContactPropertyCollection.GetPropertyArrayElementID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32,POINTER(UInt32), use_last_error=False)(9, 'GetPropertyArrayElementID', ((1, 'pszArrayElementID'),(1, 'cchArrayElementID'),(1, 'pdwcchArrayElementIDRequired'),)))
    return IContactPropertyCollection
CONTACT_AGGREGATION_CREATE_OR_OPEN_OPTIONS = Int32
CA_CREATE_LOCAL = 0
CA_CREATE_EXTERNAL = 1
CONTACT_AGGREGATION_COLLECTION_OPTIONS = Int32
CACO_DEFAULT = 0
CACO_INCLUDE_EXTERNAL = 1
CACO_EXTERNAL_ONLY = 2
def _define_CONTACT_AGGREGATION_BLOB_head():
    class CONTACT_AGGREGATION_BLOB(Structure):
        pass
    return CONTACT_AGGREGATION_BLOB
def _define_CONTACT_AGGREGATION_BLOB():
    CONTACT_AGGREGATION_BLOB = win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head
    CONTACT_AGGREGATION_BLOB._fields_ = [
        ("dwCount", UInt32),
        ("lpb", c_char_p_no),
    ]
    return CONTACT_AGGREGATION_BLOB
def _define_IContactAggregationManager_head():
    class IContactAggregationManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('1d865989-4b1f-4b60-8f34-c2ad468b2b50')
    return IContactAggregationManager
def _define_IContactAggregationManager():
    IContactAggregationManager = win32more.System.Contacts.IContactAggregationManager_head
    IContactAggregationManager.GetVersionInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(Int32), use_last_error=False)(3, 'GetVersionInfo', ((1, 'plMajorVersion'),(1, 'plMinorVersion'),)))
    IContactAggregationManager.CreateOrOpenGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Contacts.CONTACT_AGGREGATION_CREATE_OR_OPEN_OPTIONS,POINTER(win32more.Foundation.BOOL),POINTER(win32more.System.Contacts.IContactAggregationGroup_head), use_last_error=False)(4, 'CreateOrOpenGroup', ((1, 'pGroupName'),(1, 'options'),(1, 'pCreatedGroup'),(1, 'ppGroup'),)))
    IContactAggregationManager.CreateExternalContact = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationContact_head), use_last_error=False)(5, 'CreateExternalContact', ((1, 'ppItem'),)))
    IContactAggregationManager.CreateServerPerson = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationServerPerson_head), use_last_error=False)(6, 'CreateServerPerson', ((1, 'ppServerPerson'),)))
    IContactAggregationManager.CreateServerContactLink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationLink_head), use_last_error=False)(7, 'CreateServerContactLink', ((1, 'ppServerContactLink'),)))
    IContactAggregationManager.Flush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Flush', ()))
    IContactAggregationManager.OpenAggregateContact = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Contacts.IContactAggregationAggregate_head), use_last_error=False)(9, 'OpenAggregateContact', ((1, 'pItemId'),(1, 'ppItem'),)))
    IContactAggregationManager.OpenContact = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Contacts.IContactAggregationContact_head), use_last_error=False)(10, 'OpenContact', ((1, 'pItemId'),(1, 'ppItem'),)))
    IContactAggregationManager.OpenServerContactLink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Contacts.IContactAggregationLink_head), use_last_error=False)(11, 'OpenServerContactLink', ((1, 'pItemId'),(1, 'ppItem'),)))
    IContactAggregationManager.OpenServerPerson = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Contacts.IContactAggregationServerPerson_head), use_last_error=False)(12, 'OpenServerPerson', ((1, 'pItemId'),(1, 'ppItem'),)))
    IContactAggregationManager.get_Contacts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Contacts.CONTACT_AGGREGATION_COLLECTION_OPTIONS,POINTER(win32more.System.Contacts.IContactAggregationContactCollection_head), use_last_error=False)(13, 'get_Contacts', ((1, 'options'),(1, 'ppItems'),)))
    IContactAggregationManager.get_AggregateContacts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Contacts.CONTACT_AGGREGATION_COLLECTION_OPTIONS,POINTER(win32more.System.Contacts.IContactAggregationAggregateCollection_head), use_last_error=False)(14, 'get_AggregateContacts', ((1, 'options'),(1, 'ppAggregates'),)))
    IContactAggregationManager.get_Groups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Contacts.CONTACT_AGGREGATION_COLLECTION_OPTIONS,POINTER(win32more.System.Contacts.IContactAggregationGroupCollection_head), use_last_error=False)(15, 'get_Groups', ((1, 'options'),(1, 'ppGroups'),)))
    IContactAggregationManager.get_ServerPersons = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationServerPersonCollection_head), use_last_error=False)(16, 'get_ServerPersons', ((1, 'ppServerPersonCollection'),)))
    IContactAggregationManager.get_ServerContactLinks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Contacts.IContactAggregationLinkCollection_head), use_last_error=False)(17, 'get_ServerContactLinks', ((1, 'pPersonItemId'),(1, 'ppServerContactLinkCollection'),)))
    return IContactAggregationManager
def _define_IContactAggregationContact_head():
    class IContactAggregationContact(win32more.System.Com.IUnknown_head):
        Guid = Guid('1eb22e86-4c86-41f0-9f9f-c251e9fda6c3')
    return IContactAggregationContact
def _define_IContactAggregationContact():
    IContactAggregationContact = win32more.System.Contacts.IContactAggregationContact_head
    IContactAggregationContact.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Delete', ()))
    IContactAggregationContact.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Save', ()))
    IContactAggregationContact.MoveToAggregate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(5, 'MoveToAggregate', ((1, 'pAggregateId'),)))
    IContactAggregationContact.Unlink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'Unlink', ()))
    IContactAggregationContact.get_AccountId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(7, 'get_AccountId', ((1, 'ppAccountId'),)))
    IContactAggregationContact.put_AccountId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(8, 'put_AccountId', ((1, 'pAccountId'),)))
    IContactAggregationContact.get_AggregateId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(9, 'get_AggregateId', ((1, 'ppAggregateId'),)))
    IContactAggregationContact.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(10, 'get_Id', ((1, 'ppItemId'),)))
    IContactAggregationContact.get_IsMe = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(11, 'get_IsMe', ((1, 'pIsMe'),)))
    IContactAggregationContact.get_IsExternal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(12, 'get_IsExternal', ((1, 'pIsExternal'),)))
    IContactAggregationContact.get_NetworkSourceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(13, 'get_NetworkSourceId', ((1, 'pNetworkSourceId'),)))
    IContactAggregationContact.put_NetworkSourceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(14, 'put_NetworkSourceId', ((1, 'networkSourceId'),)))
    IContactAggregationContact.get_NetworkSourceIdString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(15, 'get_NetworkSourceIdString', ((1, 'ppNetworkSourceId'),)))
    IContactAggregationContact.put_NetworkSourceIdString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(16, 'put_NetworkSourceIdString', ((1, 'pNetworkSourceId'),)))
    IContactAggregationContact.get_RemoteObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head)), use_last_error=False)(17, 'get_RemoteObjectId', ((1, 'ppRemoteObjectId'),)))
    IContactAggregationContact.put_RemoteObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head), use_last_error=False)(18, 'put_RemoteObjectId', ((1, 'pRemoteObjectId'),)))
    IContactAggregationContact.get_SyncIdentityHash = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head)), use_last_error=False)(19, 'get_SyncIdentityHash', ((1, 'ppSyncIdentityHash'),)))
    IContactAggregationContact.put_SyncIdentityHash = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head), use_last_error=False)(20, 'put_SyncIdentityHash', ((1, 'pSyncIdentityHash'),)))
    return IContactAggregationContact
def _define_IContactAggregationContactCollection_head():
    class IContactAggregationContactCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('826e66fa-81de-43ca-a6fb-8c785cd996c6')
    return IContactAggregationContactCollection
def _define_IContactAggregationContactCollection():
    IContactAggregationContactCollection = win32more.System.Contacts.IContactAggregationContactCollection_head
    IContactAggregationContactCollection.FindFirst = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationContact_head), use_last_error=False)(3, 'FindFirst', ((1, 'ppItem'),)))
    IContactAggregationContactCollection.FindNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationContact_head), use_last_error=False)(4, 'FindNext', ((1, 'ppItem'),)))
    IContactAggregationContactCollection.FindFirstByIdentityHash = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head),POINTER(win32more.System.Contacts.IContactAggregationContact_head), use_last_error=False)(5, 'FindFirstByIdentityHash', ((1, 'pSourceType'),(1, 'pAccountId'),(1, 'pIdentityHash'),(1, 'ppItem'),)))
    IContactAggregationContactCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(6, 'get_Count', ((1, 'pCount'),)))
    IContactAggregationContactCollection.FindFirstByRemoteId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head),POINTER(win32more.System.Contacts.IContactAggregationContact_head), use_last_error=False)(7, 'FindFirstByRemoteId', ((1, 'pSourceType'),(1, 'pAccountId'),(1, 'pRemoteObjectId'),(1, 'ppItem'),)))
    return IContactAggregationContactCollection
def _define_IContactAggregationAggregate_head():
    class IContactAggregationAggregate(win32more.System.Com.IUnknown_head):
        Guid = Guid('7ed1c814-cd30-43c8-9b8d-2e489e53d54b')
    return IContactAggregationAggregate
def _define_IContactAggregationAggregate():
    IContactAggregationAggregate = win32more.System.Contacts.IContactAggregationAggregate_head
    IContactAggregationAggregate.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Save', ()))
    IContactAggregationAggregate.GetComponentItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationContactCollection_head), use_last_error=False)(4, 'GetComponentItems', ((1, 'pComponentItems'),)))
    IContactAggregationAggregate.Link = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(5, 'Link', ((1, 'pAggregateId'),)))
    IContactAggregationAggregate.get_Groups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Contacts.CONTACT_AGGREGATION_COLLECTION_OPTIONS,POINTER(win32more.System.Contacts.IContactAggregationGroupCollection_head), use_last_error=False)(6, 'get_Groups', ((1, 'options'),(1, 'ppGroups'),)))
    IContactAggregationAggregate.get_AntiLink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(7, 'get_AntiLink', ((1, 'ppAntiLink'),)))
    IContactAggregationAggregate.put_AntiLink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(8, 'put_AntiLink', ((1, 'pAntiLink'),)))
    IContactAggregationAggregate.get_FavoriteOrder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'get_FavoriteOrder', ((1, 'pFavoriteOrder'),)))
    IContactAggregationAggregate.put_FavoriteOrder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(10, 'put_FavoriteOrder', ((1, 'favoriteOrder'),)))
    IContactAggregationAggregate.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(11, 'get_Id', ((1, 'ppItemId'),)))
    return IContactAggregationAggregate
def _define_IContactAggregationAggregateCollection_head():
    class IContactAggregationAggregateCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('2359f3a6-3a68-40af-98db-0f9eb143c3bb')
    return IContactAggregationAggregateCollection
def _define_IContactAggregationAggregateCollection():
    IContactAggregationAggregateCollection = win32more.System.Contacts.IContactAggregationAggregateCollection_head
    IContactAggregationAggregateCollection.FindFirst = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationAggregate_head), use_last_error=False)(3, 'FindFirst', ((1, 'ppAggregate'),)))
    IContactAggregationAggregateCollection.FindFirstByAntiLinkId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Contacts.IContactAggregationAggregate_head), use_last_error=False)(4, 'FindFirstByAntiLinkId', ((1, 'pAntiLinkId'),(1, 'ppAggregate'),)))
    IContactAggregationAggregateCollection.FindNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationAggregate_head), use_last_error=False)(5, 'FindNext', ((1, 'ppAggregate'),)))
    IContactAggregationAggregateCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(6, 'get_Count', ((1, 'pCount'),)))
    return IContactAggregationAggregateCollection
def _define_IContactAggregationGroup_head():
    class IContactAggregationGroup(win32more.System.Com.IUnknown_head):
        Guid = Guid('c93c545f-1284-499b-96af-07372af473e0')
    return IContactAggregationGroup
def _define_IContactAggregationGroup():
    IContactAggregationGroup = win32more.System.Contacts.IContactAggregationGroup_head
    IContactAggregationGroup.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Delete', ()))
    IContactAggregationGroup.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Save', ()))
    IContactAggregationGroup.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(5, 'Add', ((1, 'pAggregateId'),)))
    IContactAggregationGroup.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(6, 'Remove', ((1, 'pAggregateId'),)))
    IContactAggregationGroup.get_Members = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationAggregateCollection_head), use_last_error=False)(7, 'get_Members', ((1, 'ppAggregateContactCollection'),)))
    IContactAggregationGroup.get_GlobalObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(8, 'get_GlobalObjectId', ((1, 'pGlobalObjectId'),)))
    IContactAggregationGroup.put_GlobalObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(9, 'put_GlobalObjectId', ((1, 'pGlobalObjectId'),)))
    IContactAggregationGroup.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(10, 'get_Id', ((1, 'ppItemId'),)))
    IContactAggregationGroup.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(11, 'get_Name', ((1, 'ppName'),)))
    IContactAggregationGroup.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(12, 'put_Name', ((1, 'pName'),)))
    return IContactAggregationGroup
def _define_IContactAggregationGroupCollection_head():
    class IContactAggregationGroupCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('20a19a9c-d2f3-4b83-9143-beffd2cc226d')
    return IContactAggregationGroupCollection
def _define_IContactAggregationGroupCollection():
    IContactAggregationGroupCollection = win32more.System.Contacts.IContactAggregationGroupCollection_head
    IContactAggregationGroupCollection.FindFirst = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationGroup_head), use_last_error=False)(3, 'FindFirst', ((1, 'ppGroup'),)))
    IContactAggregationGroupCollection.FindFirstByGlobalObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Contacts.IContactAggregationGroup_head), use_last_error=False)(4, 'FindFirstByGlobalObjectId', ((1, 'pGlobalObjectId'),(1, 'ppGroup'),)))
    IContactAggregationGroupCollection.FindNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationGroup_head), use_last_error=False)(5, 'FindNext', ((1, 'ppGroup'),)))
    IContactAggregationGroupCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'get_Count', ((1, 'pCount'),)))
    return IContactAggregationGroupCollection
def _define_IContactAggregationLink_head():
    class IContactAggregationLink(win32more.System.Com.IUnknown_head):
        Guid = Guid('b6813323-a183-4654-8627-79b30de3a0ec')
    return IContactAggregationLink
def _define_IContactAggregationLink():
    IContactAggregationLink = win32more.System.Contacts.IContactAggregationLink_head
    IContactAggregationLink.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Delete', ()))
    IContactAggregationLink.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Save', ()))
    IContactAggregationLink.get_AccountId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(5, 'get_AccountId', ((1, 'ppAccountId'),)))
    IContactAggregationLink.put_AccountId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(6, 'put_AccountId', ((1, 'pAccountId'),)))
    IContactAggregationLink.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(7, 'get_Id', ((1, 'ppItemId'),)))
    IContactAggregationLink.get_IsLinkResolved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(8, 'get_IsLinkResolved', ((1, 'pIsLinkResolved'),)))
    IContactAggregationLink.put_IsLinkResolved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(9, 'put_IsLinkResolved', ((1, 'isLinkResolved'),)))
    IContactAggregationLink.get_NetworkSourceIdString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(10, 'get_NetworkSourceIdString', ((1, 'ppNetworkSourceId'),)))
    IContactAggregationLink.put_NetworkSourceIdString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(11, 'put_NetworkSourceIdString', ((1, 'pNetworkSourceId'),)))
    IContactAggregationLink.get_RemoteObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head)), use_last_error=False)(12, 'get_RemoteObjectId', ((1, 'ppRemoteObjectId'),)))
    IContactAggregationLink.put_RemoteObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head), use_last_error=False)(13, 'put_RemoteObjectId', ((1, 'pRemoteObjectId'),)))
    IContactAggregationLink.get_ServerPerson = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(14, 'get_ServerPerson', ((1, 'ppServerPersonId'),)))
    IContactAggregationLink.put_ServerPerson = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(15, 'put_ServerPerson', ((1, 'pServerPersonId'),)))
    IContactAggregationLink.get_ServerPersonBaseline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(16, 'get_ServerPersonBaseline', ((1, 'ppServerPersonId'),)))
    IContactAggregationLink.put_ServerPersonBaseline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(17, 'put_ServerPersonBaseline', ((1, 'pServerPersonId'),)))
    IContactAggregationLink.get_SyncIdentityHash = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head)), use_last_error=False)(18, 'get_SyncIdentityHash', ((1, 'ppSyncIdentityHash'),)))
    IContactAggregationLink.put_SyncIdentityHash = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head), use_last_error=False)(19, 'put_SyncIdentityHash', ((1, 'pSyncIdentityHash'),)))
    return IContactAggregationLink
def _define_IContactAggregationLinkCollection_head():
    class IContactAggregationLinkCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('f8bc0e93-fb55-4f28-b9fa-b1c274153292')
    return IContactAggregationLinkCollection
def _define_IContactAggregationLinkCollection():
    IContactAggregationLinkCollection = win32more.System.Contacts.IContactAggregationLinkCollection_head
    IContactAggregationLinkCollection.FindFirst = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationLink_head), use_last_error=False)(3, 'FindFirst', ((1, 'ppServerContactLink'),)))
    IContactAggregationLinkCollection.FindFirstByRemoteId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head),POINTER(win32more.System.Contacts.IContactAggregationLink_head), use_last_error=False)(4, 'FindFirstByRemoteId', ((1, 'pSourceType'),(1, 'pAccountId'),(1, 'pRemoteId'),(1, 'ppServerContactLink'),)))
    IContactAggregationLinkCollection.FindNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationLink_head), use_last_error=False)(5, 'FindNext', ((1, 'ppServerContactLink'),)))
    IContactAggregationLinkCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'get_Count', ((1, 'pCount'),)))
    return IContactAggregationLinkCollection
def _define_IContactAggregationServerPerson_head():
    class IContactAggregationServerPerson(win32more.System.Com.IUnknown_head):
        Guid = Guid('7fdc3d4b-1b82-4334-85c5-25184ee5a5f2')
    return IContactAggregationServerPerson
def _define_IContactAggregationServerPerson():
    IContactAggregationServerPerson = win32more.System.Contacts.IContactAggregationServerPerson_head
    IContactAggregationServerPerson.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Delete', ()))
    IContactAggregationServerPerson.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Save', ()))
    IContactAggregationServerPerson.get_AggregateId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(5, 'get_AggregateId', ((1, 'ppAggregateId'),)))
    IContactAggregationServerPerson.put_AggregateId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(6, 'put_AggregateId', ((1, 'pAggregateId'),)))
    IContactAggregationServerPerson.get_AntiLink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(7, 'get_AntiLink', ((1, 'ppAntiLink'),)))
    IContactAggregationServerPerson.put_AntiLink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(8, 'put_AntiLink', ((1, 'pAntiLink'),)))
    IContactAggregationServerPerson.get_AntiLinkBaseline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(9, 'get_AntiLinkBaseline', ((1, 'ppAntiLink'),)))
    IContactAggregationServerPerson.put_AntiLinkBaseline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(10, 'put_AntiLinkBaseline', ((1, 'pAntiLink'),)))
    IContactAggregationServerPerson.get_FavoriteOrder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(11, 'get_FavoriteOrder', ((1, 'pFavoriteOrder'),)))
    IContactAggregationServerPerson.put_FavoriteOrder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(12, 'put_FavoriteOrder', ((1, 'favoriteOrder'),)))
    IContactAggregationServerPerson.get_FavoriteOrderBaseline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(13, 'get_FavoriteOrderBaseline', ((1, 'pFavoriteOrder'),)))
    IContactAggregationServerPerson.put_FavoriteOrderBaseline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(14, 'put_FavoriteOrderBaseline', ((1, 'favoriteOrder'),)))
    IContactAggregationServerPerson.get_Groups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head)), use_last_error=False)(15, 'get_Groups', ((1, 'pGroups'),)))
    IContactAggregationServerPerson.put_Groups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head), use_last_error=False)(16, 'put_Groups', ((1, 'pGroups'),)))
    IContactAggregationServerPerson.get_GroupsBaseline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head)), use_last_error=False)(17, 'get_GroupsBaseline', ((1, 'ppGroups'),)))
    IContactAggregationServerPerson.put_GroupsBaseline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head), use_last_error=False)(18, 'put_GroupsBaseline', ((1, 'pGroups'),)))
    IContactAggregationServerPerson.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(19, 'get_Id', ((1, 'ppId'),)))
    IContactAggregationServerPerson.get_IsTombstone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(20, 'get_IsTombstone', ((1, 'pIsTombstone'),)))
    IContactAggregationServerPerson.put_IsTombstone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(21, 'put_IsTombstone', ((1, 'isTombstone'),)))
    IContactAggregationServerPerson.get_LinkedAggregateId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(22, 'get_LinkedAggregateId', ((1, 'ppLinkedAggregateId'),)))
    IContactAggregationServerPerson.put_LinkedAggregateId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(23, 'put_LinkedAggregateId', ((1, 'pLinkedAggregateId'),)))
    IContactAggregationServerPerson.get_ObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(24, 'get_ObjectId', ((1, 'ppObjectId'),)))
    IContactAggregationServerPerson.put_ObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(25, 'put_ObjectId', ((1, 'pObjectId'),)))
    return IContactAggregationServerPerson
def _define_IContactAggregationServerPersonCollection_head():
    class IContactAggregationServerPersonCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('4f730a4a-6604-47b6-a987-669ecf1e5751')
    return IContactAggregationServerPersonCollection
def _define_IContactAggregationServerPersonCollection():
    IContactAggregationServerPersonCollection = win32more.System.Contacts.IContactAggregationServerPersonCollection_head
    IContactAggregationServerPersonCollection.FindFirst = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationServerPerson_head), use_last_error=False)(3, 'FindFirst', ((1, 'ppServerPerson'),)))
    IContactAggregationServerPersonCollection.FindFirstByServerId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Contacts.IContactAggregationServerPerson_head), use_last_error=False)(4, 'FindFirstByServerId', ((1, 'pServerId'),(1, 'ppServerPerson'),)))
    IContactAggregationServerPersonCollection.FindFirstByAggregateId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Contacts.IContactAggregationServerPerson_head), use_last_error=False)(5, 'FindFirstByAggregateId', ((1, 'pAggregateId'),(1, 'ppServerPerson'),)))
    IContactAggregationServerPersonCollection.FindFirstByLinkedAggregateId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Contacts.IContactAggregationServerPerson_head), use_last_error=False)(6, 'FindFirstByLinkedAggregateId', ((1, 'pAggregateId'),(1, 'ppServerPerson'),)))
    IContactAggregationServerPersonCollection.FindNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationServerPerson_head), use_last_error=False)(7, 'FindNext', ((1, 'ppServerPerson'),)))
    IContactAggregationServerPersonCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(8, 'get_Count', ((1, 'pCount'),)))
    return IContactAggregationServerPersonCollection
__all__ = [
    "CGD_DEFAULT",
    "CGD_UNKNOWN_PROPERTY",
    "CGD_STRING_PROPERTY",
    "CGD_DATE_PROPERTY",
    "CGD_BINARY_PROPERTY",
    "CGD_ARRAY_NODE",
    "CLSID_ContactAggregationManager",
    "Contact",
    "ContactManager",
    "IContactManager",
    "IContactCollection",
    "IContactProperties",
    "IContact",
    "IContactPropertyCollection",
    "CONTACT_AGGREGATION_CREATE_OR_OPEN_OPTIONS",
    "CA_CREATE_LOCAL",
    "CA_CREATE_EXTERNAL",
    "CONTACT_AGGREGATION_COLLECTION_OPTIONS",
    "CACO_DEFAULT",
    "CACO_INCLUDE_EXTERNAL",
    "CACO_EXTERNAL_ONLY",
    "CONTACT_AGGREGATION_BLOB",
    "IContactAggregationManager",
    "IContactAggregationContact",
    "IContactAggregationContactCollection",
    "IContactAggregationAggregate",
    "IContactAggregationAggregateCollection",
    "IContactAggregationGroup",
    "IContactAggregationGroupCollection",
    "IContactAggregationLink",
    "IContactAggregationLinkCollection",
    "IContactAggregationServerPerson",
    "IContactAggregationServerPersonCollection",
]
