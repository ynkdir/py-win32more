from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Com
import win32more.System.Contacts
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
CGD_DEFAULT = 0
CGD_UNKNOWN_PROPERTY = 0
CGD_STRING_PROPERTY = 1
CGD_DATE_PROPERTY = 2
CGD_BINARY_PROPERTY = 4
CGD_ARRAY_NODE = 8
def _define_CLSID_ContactAggregationManager():
    return Guid('96c8ad95-c199-44de-b3-4e-ac-33-c4-42-df-39')
CONTACTPROP_PUB_NOTES = 'Notes'
CONTACTPROP_PUB_MAILER = 'Mailer'
CONTACTPROP_PUB_PROGID = 'ProgID'
CONTACTPROP_PUB_GENDER = 'Gender'
CONTACTPROP_PUB_GENDER_UNSPECIFIED = 'Unspecified'
CONTACTPROP_PUB_GENDER_MALE = 'Male'
CONTACTPROP_PUB_GENDER_FEMALE = 'Female'
CONTACTPROP_PUB_CREATIONDATE = 'CreationDate'
CONTACTPROP_PUB_L1_CONTACTIDCOLLECTION = 'ContactIDCollection'
CONTACTPROP_PUB_L2_CONTACTID = '/ContactID'
CONTACTPROP_PUB_L3_VALUE = '/Value'
CONTACTPROP_PUB_L1_NAMECOLLECTION = 'NameCollection'
CONTACTPROP_PUB_L2_NAME = '/Name'
CONTACTPROP_PUB_L3_FORMATTEDNAME = '/FormattedName'
CONTACTPROP_PUB_L3_PHONETIC = '/Phonetic'
CONTACTPROP_PUB_L3_PREFIX = '/Prefix'
CONTACTPROP_PUB_L3_TITLE = '/Title'
CONTACTPROP_PUB_L3_GIVENNAME = '/GivenName'
CONTACTPROP_PUB_L3_FAMILYNAME = '/FamilyName'
CONTACTPROP_PUB_L3_MIDDLENAME = '/MiddleName'
CONTACTPROP_PUB_L3_GENERATION = '/Generation'
CONTACTPROP_PUB_L3_SUFFIX = '/Suffix'
CONTACTPROP_PUB_L3_NICKNAME = '/NickName'
CONTACTPROP_PUB_L1_POSITIONCOLLECTION = 'PositionCollection'
CONTACTPROP_PUB_L2_POSITION = '/Position'
CONTACTPROP_PUB_L3_ORGANIZATION = '/Organization'
CONTACTPROP_PUB_L3_COMPANY = '/Company'
CONTACTPROP_PUB_L3_DEPARTMENT = '/Department'
CONTACTPROP_PUB_L3_OFFICE = '/Office'
CONTACTPROP_PUB_L3_JOB_TITLE = '/JobTitle'
CONTACTPROP_PUB_L3_PROFESSION = '/Profession'
CONTACTPROP_PUB_L3_ROLE = '/Role'
CONTACTPROP_PUB_L1_PERSONCOLLECTION = 'PersonCollection'
CONTACTPROP_PUB_L2_PERSON = '/Person'
CONTACTPROP_PUB_L3_PERSONID = '/PersonID'
CONTACTPROP_PUB_L1_DATECOLLECTION = 'DateCollection'
CONTACTPROP_PUB_L2_DATE = '/Date'
CONTACTPROP_PUB_L1_EMAILADDRESSCOLLECTION = 'EmailAddressCollection'
CONTACTPROP_PUB_L2_EMAILADDRESS = '/EmailAddress'
CONTACTPROP_PUB_L3_ADDRESS = '/Address'
CONTACTPROP_PUB_L3_TYPE = '/Type'
CONTACTPROP_PUB_L1_CERTIFICATECOLLECTION = 'CertificateCollection'
CONTACTPROP_PUB_L2_CERTIFICATE = '/Certificate'
CONTACTPROP_PUB_L3_THUMBPRINT = '/ThumbPrint'
CONTACTPROP_PUB_L1_PHONENUMBERCOLLECTION = 'PhoneNumberCollection'
CONTACTPROP_PUB_L2_PHONENUMBER = '/PhoneNumber'
CONTACTPROP_PUB_L3_NUMBER = '/Number'
CONTACTPROP_PUB_L3_ALTERNATE = '/Alternate'
CONTACTPROP_PUB_L1_PHYSICALADDRESSCOLLECTION = 'PhysicalAddressCollection'
CONTACTPROP_PUB_L2_PHYSICALADDRESS = '/PhysicalAddress'
CONTACTPROP_PUB_L3_ADDRESSLABEL = '/AddressLabel'
CONTACTPROP_PUB_L3_STREET = '/Street'
CONTACTPROP_PUB_L3_LOCALITY = '/Locality'
CONTACTPROP_PUB_L3_REGION = '/Region'
CONTACTPROP_PUB_L3_POSTALCODE = '/PostalCode'
CONTACTPROP_PUB_L3_COUNTRY = '/Country'
CONTACTPROP_PUB_L3_POBOX = '/POBox'
CONTACTPROP_PUB_L3_EXTENDEDADDRESS = '/ExtendedAddress'
CONTACTPROP_PUB_L1_IMADDRESSCOLLECTION = 'IMAddressCollection'
CONTACTPROP_PUB_L2_IMADDRESSENTRY = '/IMAddress'
CONTACTPROP_PUB_L3_PROTOCOL = '/Protocol'
CONTACTPROP_PUB_L1_URLCOLLECTION = 'UrlCollection'
CONTACTPROP_PUB_L2_URL = '/Url'
CONTACTPROP_PUB_L1_PHOTOCOLLECTION = 'PhotoCollection'
CONTACTPROP_PUB_L2_PHOTO = '/Photo'
CONTACTPROP_PUB_L3_URL = '/Url'
CONTACTLABEL_PUB_PREFERRED = 'Preferred'
CONTACTLABEL_PUB_PERSONAL = 'Personal'
CONTACTLABEL_PUB_BUSINESS = 'Business'
CONTACTLABEL_PUB_OTHER = 'Other'
CONTACTLABEL_PUB_VOICE = 'Voice'
CONTACTLABEL_PUB_MOBILE = 'Mobile'
CONTACTLABEL_PUB_PCS = 'PCS'
CONTACTLABEL_PUB_CELLULAR = 'Cellular'
CONTACTLABEL_PUB_CAR = 'Car'
CONTACTLABEL_PUB_PAGER = 'Pager'
CONTACTLABEL_PUB_TTY = 'TTY'
CONTACTLABEL_PUB_FAX = 'Fax'
CONTACTLABEL_PUB_VIDEO = 'Video'
CONTACTLABEL_PUB_MODEM = 'Modem'
CONTACTLABEL_PUB_BBS = 'BBS'
CONTACTLABEL_PUB_ISDN = 'ISDN'
CONTACTLABEL_PUB_AGENT = 'Agent'
CONTACTLABEL_PUB_DOMESTIC = 'Domestic'
CONTACTLABEL_PUB_INTERNATIONAL = 'International'
CONTACTLABEL_PUB_POSTAL = 'Postal'
CONTACTLABEL_PUB_PARCEL = 'Parcel'
CONTACTLABEL_PUB_USERTILE = 'UserTile'
CONTACTLABEL_PUB_LOGO = 'Logo'
CONTACTLABEL_WAB_SPOUSE = 'wab:Spouse'
CONTACTLABEL_WAB_CHILD = 'wab:Child'
CONTACTLABEL_WAB_MANAGER = 'wab:Manager'
CONTACTLABEL_WAB_ASSISTANT = 'wab:Assistant'
CONTACTLABEL_WAB_BIRTHDAY = 'wab:Birthday'
CONTACTLABEL_WAB_ANNIVERSARY = 'wab:Anniversary'
CONTACTLABEL_WAB_SOCIALNETWORK = 'wab:SocialNetwork'
CONTACTLABEL_WAB_SCHOOL = 'wab:School'
CONTACTLABEL_WAB_WISHLIST = 'wab:WishList'
Contact = Guid('61b68808-8eee-4fd1-ac-b8-3d-80-4c-8d-b0-56')
def _define_CONTACT_AGGREGATION_BLOB_head():
    class CONTACT_AGGREGATION_BLOB(Structure):
        pass
    return CONTACT_AGGREGATION_BLOB
def _define_CONTACT_AGGREGATION_BLOB():
    CONTACT_AGGREGATION_BLOB = win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head
    CONTACT_AGGREGATION_BLOB._fields_ = [
        ('dwCount', UInt32),
        ('lpb', c_char_p_no),
    ]
    return CONTACT_AGGREGATION_BLOB
CONTACT_AGGREGATION_COLLECTION_OPTIONS = Int32
CACO_DEFAULT = 0
CACO_INCLUDE_EXTERNAL = 1
CACO_EXTERNAL_ONLY = 2
CONTACT_AGGREGATION_CREATE_OR_OPEN_OPTIONS = Int32
CA_CREATE_LOCAL = 0
CA_CREATE_EXTERNAL = 1
ContactManager = Guid('7165c8ab-af88-42bd-86-fd-53-10-b4-28-5a-02')
def _define_IContact_head():
    class IContact(win32more.System.Com.IUnknown_head):
        Guid = Guid('f941b671-bda7-4f77-88-4a-f4-64-62-f2-26-a7')
    return IContact
def _define_IContact():
    IContact = win32more.System.Contacts.IContact_head
    IContact.GetContactID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32))(3, 'GetContactID', ((1, 'pszContactID'),(1, 'cchContactID'),(1, 'pdwcchContactIDRequired'),)))
    IContact.GetPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32))(4, 'GetPath', ((1, 'pszPath'),(1, 'cchPath'),(1, 'pdwcchPathRequired'),)))
    IContact.CommitChanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(5, 'CommitChanges', ((1, 'dwCommitFlags'),)))
    win32more.System.Com.IUnknown
    return IContact
def _define_IContactAggregationAggregate_head():
    class IContactAggregationAggregate(win32more.System.Com.IUnknown_head):
        Guid = Guid('7ed1c814-cd30-43c8-9b-8d-2e-48-9e-53-d5-4b')
    return IContactAggregationAggregate
def _define_IContactAggregationAggregate():
    IContactAggregationAggregate = win32more.System.Contacts.IContactAggregationAggregate_head
    IContactAggregationAggregate.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Save', ()))
    IContactAggregationAggregate.GetComponentItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationContactCollection_head))(4, 'GetComponentItems', ((1, 'pComponentItems'),)))
    IContactAggregationAggregate.Link = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(5, 'Link', ((1, 'pAggregateId'),)))
    IContactAggregationAggregate.get_Groups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Contacts.CONTACT_AGGREGATION_COLLECTION_OPTIONS,POINTER(win32more.System.Contacts.IContactAggregationGroupCollection_head))(6, 'get_Groups', ((1, 'options'),(1, 'ppGroups'),)))
    IContactAggregationAggregate.get_AntiLink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(7, 'get_AntiLink', ((1, 'ppAntiLink'),)))
    IContactAggregationAggregate.put_AntiLink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(8, 'put_AntiLink', ((1, 'pAntiLink'),)))
    IContactAggregationAggregate.get_FavoriteOrder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(9, 'get_FavoriteOrder', ((1, 'pFavoriteOrder'),)))
    IContactAggregationAggregate.put_FavoriteOrder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(10, 'put_FavoriteOrder', ((1, 'favoriteOrder'),)))
    IContactAggregationAggregate.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(11, 'get_Id', ((1, 'ppItemId'),)))
    win32more.System.Com.IUnknown
    return IContactAggregationAggregate
def _define_IContactAggregationAggregateCollection_head():
    class IContactAggregationAggregateCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('2359f3a6-3a68-40af-98-db-0f-9e-b1-43-c3-bb')
    return IContactAggregationAggregateCollection
def _define_IContactAggregationAggregateCollection():
    IContactAggregationAggregateCollection = win32more.System.Contacts.IContactAggregationAggregateCollection_head
    IContactAggregationAggregateCollection.FindFirst = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationAggregate_head))(3, 'FindFirst', ((1, 'ppAggregate'),)))
    IContactAggregationAggregateCollection.FindFirstByAntiLinkId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Contacts.IContactAggregationAggregate_head))(4, 'FindFirstByAntiLinkId', ((1, 'pAntiLinkId'),(1, 'ppAggregate'),)))
    IContactAggregationAggregateCollection.FindNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationAggregate_head))(5, 'FindNext', ((1, 'ppAggregate'),)))
    IContactAggregationAggregateCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(6, 'get_Count', ((1, 'pCount'),)))
    win32more.System.Com.IUnknown
    return IContactAggregationAggregateCollection
def _define_IContactAggregationContact_head():
    class IContactAggregationContact(win32more.System.Com.IUnknown_head):
        Guid = Guid('1eb22e86-4c86-41f0-9f-9f-c2-51-e9-fd-a6-c3')
    return IContactAggregationContact
def _define_IContactAggregationContact():
    IContactAggregationContact = win32more.System.Contacts.IContactAggregationContact_head
    IContactAggregationContact.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Delete', ()))
    IContactAggregationContact.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Save', ()))
    IContactAggregationContact.MoveToAggregate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(5, 'MoveToAggregate', ((1, 'pAggregateId'),)))
    IContactAggregationContact.Unlink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'Unlink', ()))
    IContactAggregationContact.get_AccountId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(7, 'get_AccountId', ((1, 'ppAccountId'),)))
    IContactAggregationContact.put_AccountId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(8, 'put_AccountId', ((1, 'pAccountId'),)))
    IContactAggregationContact.get_AggregateId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(9, 'get_AggregateId', ((1, 'ppAggregateId'),)))
    IContactAggregationContact.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(10, 'get_Id', ((1, 'ppItemId'),)))
    IContactAggregationContact.get_IsMe = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(11, 'get_IsMe', ((1, 'pIsMe'),)))
    IContactAggregationContact.get_IsExternal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(12, 'get_IsExternal', ((1, 'pIsExternal'),)))
    IContactAggregationContact.get_NetworkSourceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(13, 'get_NetworkSourceId', ((1, 'pNetworkSourceId'),)))
    IContactAggregationContact.put_NetworkSourceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(14, 'put_NetworkSourceId', ((1, 'networkSourceId'),)))
    IContactAggregationContact.get_NetworkSourceIdString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(15, 'get_NetworkSourceIdString', ((1, 'ppNetworkSourceId'),)))
    IContactAggregationContact.put_NetworkSourceIdString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(16, 'put_NetworkSourceIdString', ((1, 'pNetworkSourceId'),)))
    IContactAggregationContact.get_RemoteObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head)))(17, 'get_RemoteObjectId', ((1, 'ppRemoteObjectId'),)))
    IContactAggregationContact.put_RemoteObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head))(18, 'put_RemoteObjectId', ((1, 'pRemoteObjectId'),)))
    IContactAggregationContact.get_SyncIdentityHash = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head)))(19, 'get_SyncIdentityHash', ((1, 'ppSyncIdentityHash'),)))
    IContactAggregationContact.put_SyncIdentityHash = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head))(20, 'put_SyncIdentityHash', ((1, 'pSyncIdentityHash'),)))
    win32more.System.Com.IUnknown
    return IContactAggregationContact
def _define_IContactAggregationContactCollection_head():
    class IContactAggregationContactCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('826e66fa-81de-43ca-a6-fb-8c-78-5c-d9-96-c6')
    return IContactAggregationContactCollection
def _define_IContactAggregationContactCollection():
    IContactAggregationContactCollection = win32more.System.Contacts.IContactAggregationContactCollection_head
    IContactAggregationContactCollection.FindFirst = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationContact_head))(3, 'FindFirst', ((1, 'ppItem'),)))
    IContactAggregationContactCollection.FindNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationContact_head))(4, 'FindNext', ((1, 'ppItem'),)))
    IContactAggregationContactCollection.FindFirstByIdentityHash = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head),POINTER(win32more.System.Contacts.IContactAggregationContact_head))(5, 'FindFirstByIdentityHash', ((1, 'pSourceType'),(1, 'pAccountId'),(1, 'pIdentityHash'),(1, 'ppItem'),)))
    IContactAggregationContactCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(6, 'get_Count', ((1, 'pCount'),)))
    IContactAggregationContactCollection.FindFirstByRemoteId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head),POINTER(win32more.System.Contacts.IContactAggregationContact_head))(7, 'FindFirstByRemoteId', ((1, 'pSourceType'),(1, 'pAccountId'),(1, 'pRemoteObjectId'),(1, 'ppItem'),)))
    win32more.System.Com.IUnknown
    return IContactAggregationContactCollection
def _define_IContactAggregationGroup_head():
    class IContactAggregationGroup(win32more.System.Com.IUnknown_head):
        Guid = Guid('c93c545f-1284-499b-96-af-07-37-2a-f4-73-e0')
    return IContactAggregationGroup
def _define_IContactAggregationGroup():
    IContactAggregationGroup = win32more.System.Contacts.IContactAggregationGroup_head
    IContactAggregationGroup.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Delete', ()))
    IContactAggregationGroup.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Save', ()))
    IContactAggregationGroup.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(5, 'Add', ((1, 'pAggregateId'),)))
    IContactAggregationGroup.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(6, 'Remove', ((1, 'pAggregateId'),)))
    IContactAggregationGroup.get_Members = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationAggregateCollection_head))(7, 'get_Members', ((1, 'ppAggregateContactCollection'),)))
    IContactAggregationGroup.get_GlobalObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(8, 'get_GlobalObjectId', ((1, 'pGlobalObjectId'),)))
    IContactAggregationGroup.put_GlobalObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(9, 'put_GlobalObjectId', ((1, 'pGlobalObjectId'),)))
    IContactAggregationGroup.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(10, 'get_Id', ((1, 'ppItemId'),)))
    IContactAggregationGroup.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(11, 'get_Name', ((1, 'ppName'),)))
    IContactAggregationGroup.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(12, 'put_Name', ((1, 'pName'),)))
    win32more.System.Com.IUnknown
    return IContactAggregationGroup
def _define_IContactAggregationGroupCollection_head():
    class IContactAggregationGroupCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('20a19a9c-d2f3-4b83-91-43-be-ff-d2-cc-22-6d')
    return IContactAggregationGroupCollection
def _define_IContactAggregationGroupCollection():
    IContactAggregationGroupCollection = win32more.System.Contacts.IContactAggregationGroupCollection_head
    IContactAggregationGroupCollection.FindFirst = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationGroup_head))(3, 'FindFirst', ((1, 'ppGroup'),)))
    IContactAggregationGroupCollection.FindFirstByGlobalObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Contacts.IContactAggregationGroup_head))(4, 'FindFirstByGlobalObjectId', ((1, 'pGlobalObjectId'),(1, 'ppGroup'),)))
    IContactAggregationGroupCollection.FindNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationGroup_head))(5, 'FindNext', ((1, 'ppGroup'),)))
    IContactAggregationGroupCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(6, 'get_Count', ((1, 'pCount'),)))
    win32more.System.Com.IUnknown
    return IContactAggregationGroupCollection
def _define_IContactAggregationLink_head():
    class IContactAggregationLink(win32more.System.Com.IUnknown_head):
        Guid = Guid('b6813323-a183-4654-86-27-79-b3-0d-e3-a0-ec')
    return IContactAggregationLink
def _define_IContactAggregationLink():
    IContactAggregationLink = win32more.System.Contacts.IContactAggregationLink_head
    IContactAggregationLink.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Delete', ()))
    IContactAggregationLink.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Save', ()))
    IContactAggregationLink.get_AccountId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(5, 'get_AccountId', ((1, 'ppAccountId'),)))
    IContactAggregationLink.put_AccountId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(6, 'put_AccountId', ((1, 'pAccountId'),)))
    IContactAggregationLink.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(7, 'get_Id', ((1, 'ppItemId'),)))
    IContactAggregationLink.get_IsLinkResolved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(8, 'get_IsLinkResolved', ((1, 'pIsLinkResolved'),)))
    IContactAggregationLink.put_IsLinkResolved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(9, 'put_IsLinkResolved', ((1, 'isLinkResolved'),)))
    IContactAggregationLink.get_NetworkSourceIdString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(10, 'get_NetworkSourceIdString', ((1, 'ppNetworkSourceId'),)))
    IContactAggregationLink.put_NetworkSourceIdString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(11, 'put_NetworkSourceIdString', ((1, 'pNetworkSourceId'),)))
    IContactAggregationLink.get_RemoteObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head)))(12, 'get_RemoteObjectId', ((1, 'ppRemoteObjectId'),)))
    IContactAggregationLink.put_RemoteObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head))(13, 'put_RemoteObjectId', ((1, 'pRemoteObjectId'),)))
    IContactAggregationLink.get_ServerPerson = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(14, 'get_ServerPerson', ((1, 'ppServerPersonId'),)))
    IContactAggregationLink.put_ServerPerson = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(15, 'put_ServerPerson', ((1, 'pServerPersonId'),)))
    IContactAggregationLink.get_ServerPersonBaseline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(16, 'get_ServerPersonBaseline', ((1, 'ppServerPersonId'),)))
    IContactAggregationLink.put_ServerPersonBaseline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(17, 'put_ServerPersonBaseline', ((1, 'pServerPersonId'),)))
    IContactAggregationLink.get_SyncIdentityHash = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head)))(18, 'get_SyncIdentityHash', ((1, 'ppSyncIdentityHash'),)))
    IContactAggregationLink.put_SyncIdentityHash = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head))(19, 'put_SyncIdentityHash', ((1, 'pSyncIdentityHash'),)))
    win32more.System.Com.IUnknown
    return IContactAggregationLink
def _define_IContactAggregationLinkCollection_head():
    class IContactAggregationLinkCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('f8bc0e93-fb55-4f28-b9-fa-b1-c2-74-15-32-92')
    return IContactAggregationLinkCollection
def _define_IContactAggregationLinkCollection():
    IContactAggregationLinkCollection = win32more.System.Contacts.IContactAggregationLinkCollection_head
    IContactAggregationLinkCollection.FindFirst = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationLink_head))(3, 'FindFirst', ((1, 'ppServerContactLink'),)))
    IContactAggregationLinkCollection.FindFirstByRemoteId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head),POINTER(win32more.System.Contacts.IContactAggregationLink_head))(4, 'FindFirstByRemoteId', ((1, 'pSourceType'),(1, 'pAccountId'),(1, 'pRemoteId'),(1, 'ppServerContactLink'),)))
    IContactAggregationLinkCollection.FindNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationLink_head))(5, 'FindNext', ((1, 'ppServerContactLink'),)))
    IContactAggregationLinkCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(6, 'get_Count', ((1, 'pCount'),)))
    win32more.System.Com.IUnknown
    return IContactAggregationLinkCollection
def _define_IContactAggregationManager_head():
    class IContactAggregationManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('1d865989-4b1f-4b60-8f-34-c2-ad-46-8b-2b-50')
    return IContactAggregationManager
def _define_IContactAggregationManager():
    IContactAggregationManager = win32more.System.Contacts.IContactAggregationManager_head
    IContactAggregationManager.GetVersionInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(Int32))(3, 'GetVersionInfo', ((1, 'plMajorVersion'),(1, 'plMinorVersion'),)))
    IContactAggregationManager.CreateOrOpenGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Contacts.CONTACT_AGGREGATION_CREATE_OR_OPEN_OPTIONS,POINTER(win32more.Foundation.BOOL),POINTER(win32more.System.Contacts.IContactAggregationGroup_head))(4, 'CreateOrOpenGroup', ((1, 'pGroupName'),(1, 'options'),(1, 'pCreatedGroup'),(1, 'ppGroup'),)))
    IContactAggregationManager.CreateExternalContact = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationContact_head))(5, 'CreateExternalContact', ((1, 'ppItem'),)))
    IContactAggregationManager.CreateServerPerson = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationServerPerson_head))(6, 'CreateServerPerson', ((1, 'ppServerPerson'),)))
    IContactAggregationManager.CreateServerContactLink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationLink_head))(7, 'CreateServerContactLink', ((1, 'ppServerContactLink'),)))
    IContactAggregationManager.Flush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'Flush', ()))
    IContactAggregationManager.OpenAggregateContact = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Contacts.IContactAggregationAggregate_head))(9, 'OpenAggregateContact', ((1, 'pItemId'),(1, 'ppItem'),)))
    IContactAggregationManager.OpenContact = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Contacts.IContactAggregationContact_head))(10, 'OpenContact', ((1, 'pItemId'),(1, 'ppItem'),)))
    IContactAggregationManager.OpenServerContactLink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Contacts.IContactAggregationLink_head))(11, 'OpenServerContactLink', ((1, 'pItemId'),(1, 'ppItem'),)))
    IContactAggregationManager.OpenServerPerson = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Contacts.IContactAggregationServerPerson_head))(12, 'OpenServerPerson', ((1, 'pItemId'),(1, 'ppItem'),)))
    IContactAggregationManager.get_Contacts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Contacts.CONTACT_AGGREGATION_COLLECTION_OPTIONS,POINTER(win32more.System.Contacts.IContactAggregationContactCollection_head))(13, 'get_Contacts', ((1, 'options'),(1, 'ppItems'),)))
    IContactAggregationManager.get_AggregateContacts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Contacts.CONTACT_AGGREGATION_COLLECTION_OPTIONS,POINTER(win32more.System.Contacts.IContactAggregationAggregateCollection_head))(14, 'get_AggregateContacts', ((1, 'options'),(1, 'ppAggregates'),)))
    IContactAggregationManager.get_Groups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Contacts.CONTACT_AGGREGATION_COLLECTION_OPTIONS,POINTER(win32more.System.Contacts.IContactAggregationGroupCollection_head))(15, 'get_Groups', ((1, 'options'),(1, 'ppGroups'),)))
    IContactAggregationManager.get_ServerPersons = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationServerPersonCollection_head))(16, 'get_ServerPersons', ((1, 'ppServerPersonCollection'),)))
    IContactAggregationManager.get_ServerContactLinks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Contacts.IContactAggregationLinkCollection_head))(17, 'get_ServerContactLinks', ((1, 'pPersonItemId'),(1, 'ppServerContactLinkCollection'),)))
    win32more.System.Com.IUnknown
    return IContactAggregationManager
def _define_IContactAggregationServerPerson_head():
    class IContactAggregationServerPerson(win32more.System.Com.IUnknown_head):
        Guid = Guid('7fdc3d4b-1b82-4334-85-c5-25-18-4e-e5-a5-f2')
    return IContactAggregationServerPerson
def _define_IContactAggregationServerPerson():
    IContactAggregationServerPerson = win32more.System.Contacts.IContactAggregationServerPerson_head
    IContactAggregationServerPerson.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Delete', ()))
    IContactAggregationServerPerson.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Save', ()))
    IContactAggregationServerPerson.get_AggregateId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(5, 'get_AggregateId', ((1, 'ppAggregateId'),)))
    IContactAggregationServerPerson.put_AggregateId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(6, 'put_AggregateId', ((1, 'pAggregateId'),)))
    IContactAggregationServerPerson.get_AntiLink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(7, 'get_AntiLink', ((1, 'ppAntiLink'),)))
    IContactAggregationServerPerson.put_AntiLink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(8, 'put_AntiLink', ((1, 'pAntiLink'),)))
    IContactAggregationServerPerson.get_AntiLinkBaseline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(9, 'get_AntiLinkBaseline', ((1, 'ppAntiLink'),)))
    IContactAggregationServerPerson.put_AntiLinkBaseline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(10, 'put_AntiLinkBaseline', ((1, 'pAntiLink'),)))
    IContactAggregationServerPerson.get_FavoriteOrder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(11, 'get_FavoriteOrder', ((1, 'pFavoriteOrder'),)))
    IContactAggregationServerPerson.put_FavoriteOrder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(12, 'put_FavoriteOrder', ((1, 'favoriteOrder'),)))
    IContactAggregationServerPerson.get_FavoriteOrderBaseline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(13, 'get_FavoriteOrderBaseline', ((1, 'pFavoriteOrder'),)))
    IContactAggregationServerPerson.put_FavoriteOrderBaseline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(14, 'put_FavoriteOrderBaseline', ((1, 'favoriteOrder'),)))
    IContactAggregationServerPerson.get_Groups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head)))(15, 'get_Groups', ((1, 'pGroups'),)))
    IContactAggregationServerPerson.put_Groups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head))(16, 'put_Groups', ((1, 'pGroups'),)))
    IContactAggregationServerPerson.get_GroupsBaseline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head)))(17, 'get_GroupsBaseline', ((1, 'ppGroups'),)))
    IContactAggregationServerPerson.put_GroupsBaseline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head))(18, 'put_GroupsBaseline', ((1, 'pGroups'),)))
    IContactAggregationServerPerson.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(19, 'get_Id', ((1, 'ppId'),)))
    IContactAggregationServerPerson.get_IsTombstone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(20, 'get_IsTombstone', ((1, 'pIsTombstone'),)))
    IContactAggregationServerPerson.put_IsTombstone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(21, 'put_IsTombstone', ((1, 'isTombstone'),)))
    IContactAggregationServerPerson.get_LinkedAggregateId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(22, 'get_LinkedAggregateId', ((1, 'ppLinkedAggregateId'),)))
    IContactAggregationServerPerson.put_LinkedAggregateId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(23, 'put_LinkedAggregateId', ((1, 'pLinkedAggregateId'),)))
    IContactAggregationServerPerson.get_ObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(24, 'get_ObjectId', ((1, 'ppObjectId'),)))
    IContactAggregationServerPerson.put_ObjectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(25, 'put_ObjectId', ((1, 'pObjectId'),)))
    win32more.System.Com.IUnknown
    return IContactAggregationServerPerson
def _define_IContactAggregationServerPersonCollection_head():
    class IContactAggregationServerPersonCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('4f730a4a-6604-47b6-a9-87-66-9e-cf-1e-57-51')
    return IContactAggregationServerPersonCollection
def _define_IContactAggregationServerPersonCollection():
    IContactAggregationServerPersonCollection = win32more.System.Contacts.IContactAggregationServerPersonCollection_head
    IContactAggregationServerPersonCollection.FindFirst = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationServerPerson_head))(3, 'FindFirst', ((1, 'ppServerPerson'),)))
    IContactAggregationServerPersonCollection.FindFirstByServerId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Contacts.IContactAggregationServerPerson_head))(4, 'FindFirstByServerId', ((1, 'pServerId'),(1, 'ppServerPerson'),)))
    IContactAggregationServerPersonCollection.FindFirstByAggregateId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Contacts.IContactAggregationServerPerson_head))(5, 'FindFirstByAggregateId', ((1, 'pAggregateId'),(1, 'ppServerPerson'),)))
    IContactAggregationServerPersonCollection.FindFirstByLinkedAggregateId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Contacts.IContactAggregationServerPerson_head))(6, 'FindFirstByLinkedAggregateId', ((1, 'pAggregateId'),(1, 'ppServerPerson'),)))
    IContactAggregationServerPersonCollection.FindNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactAggregationServerPerson_head))(7, 'FindNext', ((1, 'ppServerPerson'),)))
    IContactAggregationServerPersonCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(8, 'get_Count', ((1, 'pCount'),)))
    win32more.System.Com.IUnknown
    return IContactAggregationServerPersonCollection
def _define_IContactCollection_head():
    class IContactCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('b6afa338-d779-11d9-8b-de-f6-6b-ad-1e-3f-3a')
    return IContactCollection
def _define_IContactCollection():
    IContactCollection = win32more.System.Contacts.IContactCollection_head
    IContactCollection.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Reset', ()))
    IContactCollection.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Next', ()))
    IContactCollection.GetCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContact_head))(5, 'GetCurrent', ((1, 'ppContact'),)))
    win32more.System.Com.IUnknown
    return IContactCollection
def _define_IContactManager_head():
    class IContactManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('ad553d98-deb1-474a-8e-17-fc-0c-20-75-b7-38')
    return IContactManager
def _define_IContactManager():
    IContactManager = win32more.System.Contacts.IContactManager_head
    IContactManager.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(3, 'Initialize', ((1, 'pszAppName'),(1, 'pszAppVersion'),)))
    IContactManager.Load = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Contacts.IContact_head))(4, 'Load', ((1, 'pszContactID'),(1, 'ppContact'),)))
    IContactManager.MergeContactIDs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(5, 'MergeContactIDs', ((1, 'pszNewContactID'),(1, 'pszOldContactID'),)))
    IContactManager.GetMeContact = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContact_head))(6, 'GetMeContact', ((1, 'ppMeContact'),)))
    IContactManager.SetMeContact = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Contacts.IContact_head)(7, 'SetMeContact', ((1, 'pMeContact'),)))
    IContactManager.GetContactCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactCollection_head))(8, 'GetContactCollection', ((1, 'ppContactCollection'),)))
    win32more.System.Com.IUnknown
    return IContactManager
def _define_IContactProperties_head():
    class IContactProperties(win32more.System.Com.IUnknown_head):
        Guid = Guid('70dd27dd-5cbd-46e8-be-f0-23-b6-b3-46-28-8f')
    return IContactProperties
def _define_IContactProperties():
    IContactProperties = win32more.System.Contacts.IContactProperties_head
    IContactProperties.GetString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32))(3, 'GetString', ((1, 'pszPropertyName'),(1, 'dwFlags'),(1, 'pszValue'),(1, 'cchValue'),(1, 'pdwcchPropertyValueRequired'),)))
    IContactProperties.GetDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Foundation.FILETIME_head))(4, 'GetDate', ((1, 'pszPropertyName'),(1, 'dwFlags'),(1, 'pftDateTime'),)))
    IContactProperties.GetBinary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),POINTER(win32more.System.Com.IStream_head))(5, 'GetBinary', ((1, 'pszPropertyName'),(1, 'dwFlags'),(1, 'pszContentType'),(1, 'cchContentType'),(1, 'pdwcchContentTypeRequired'),(1, 'ppStream'),)))
    IContactProperties.GetLabels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32))(6, 'GetLabels', ((1, 'pszArrayElementName'),(1, 'dwFlags'),(1, 'pszLabels'),(1, 'cchLabels'),(1, 'pdwcchLabelsRequired'),)))
    IContactProperties.SetString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR)(7, 'SetString', ((1, 'pszPropertyName'),(1, 'dwFlags'),(1, 'pszValue'),)))
    IContactProperties.SetDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.FILETIME)(8, 'SetDate', ((1, 'pszPropertyName'),(1, 'dwFlags'),(1, 'ftDateTime'),)))
    IContactProperties.SetBinary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,win32more.System.Com.IStream_head)(9, 'SetBinary', ((1, 'pszPropertyName'),(1, 'dwFlags'),(1, 'pszContentType'),(1, 'pStream'),)))
    IContactProperties.SetLabels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.Foundation.PWSTR))(10, 'SetLabels', ((1, 'pszArrayElementName'),(1, 'dwFlags'),(1, 'dwLabelCount'),(1, 'ppszLabels'),)))
    IContactProperties.CreateArrayNode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32))(11, 'CreateArrayNode', ((1, 'pszArrayName'),(1, 'dwFlags'),(1, 'fAppend'),(1, 'pszNewArrayElementName'),(1, 'cchNewArrayElementName'),(1, 'pdwcchNewArrayElementNameRequired'),)))
    IContactProperties.DeleteProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32)(12, 'DeleteProperty', ((1, 'pszPropertyName'),(1, 'dwFlags'),)))
    IContactProperties.DeleteArrayNode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32)(13, 'DeleteArrayNode', ((1, 'pszArrayElementName'),(1, 'dwFlags'),)))
    IContactProperties.DeleteLabels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32)(14, 'DeleteLabels', ((1, 'pszArrayElementName'),(1, 'dwFlags'),)))
    IContactProperties.GetPropertyCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Contacts.IContactPropertyCollection_head),UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Foundation.PWSTR),win32more.Foundation.BOOL)(15, 'GetPropertyCollection', ((1, 'ppPropertyCollection'),(1, 'dwFlags'),(1, 'pszMultiValueName'),(1, 'dwLabelCount'),(1, 'ppszLabels'),(1, 'fAnyLabelMatches'),)))
    win32more.System.Com.IUnknown
    return IContactProperties
def _define_IContactPropertyCollection_head():
    class IContactPropertyCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('ffd3adf8-fa64-4328-b1-b6-2e-0d-b5-09-cb-3c')
    return IContactPropertyCollection
def _define_IContactPropertyCollection():
    IContactPropertyCollection = win32more.System.Contacts.IContactPropertyCollection_head
    IContactPropertyCollection.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Reset', ()))
    IContactPropertyCollection.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Next', ()))
    IContactPropertyCollection.GetPropertyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32))(5, 'GetPropertyName', ((1, 'pszPropertyName'),(1, 'cchPropertyName'),(1, 'pdwcchPropertyNameRequired'),)))
    IContactPropertyCollection.GetPropertyType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(6, 'GetPropertyType', ((1, 'pdwType'),)))
    IContactPropertyCollection.GetPropertyVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(7, 'GetPropertyVersion', ((1, 'pdwVersion'),)))
    IContactPropertyCollection.GetPropertyModificationDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head))(8, 'GetPropertyModificationDate', ((1, 'pftModificationDate'),)))
    IContactPropertyCollection.GetPropertyArrayElementID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32))(9, 'GetPropertyArrayElementID', ((1, 'pszArrayElementID'),(1, 'cchArrayElementID'),(1, 'pdwcchArrayElementIDRequired'),)))
    win32more.System.Com.IUnknown
    return IContactPropertyCollection
__all__ = [
    "CACO_DEFAULT",
    "CACO_EXTERNAL_ONLY",
    "CACO_INCLUDE_EXTERNAL",
    "CA_CREATE_EXTERNAL",
    "CA_CREATE_LOCAL",
    "CGD_ARRAY_NODE",
    "CGD_BINARY_PROPERTY",
    "CGD_DATE_PROPERTY",
    "CGD_DEFAULT",
    "CGD_STRING_PROPERTY",
    "CGD_UNKNOWN_PROPERTY",
    "CLSID_ContactAggregationManager",
    "CONTACTLABEL_PUB_AGENT",
    "CONTACTLABEL_PUB_BBS",
    "CONTACTLABEL_PUB_BUSINESS",
    "CONTACTLABEL_PUB_CAR",
    "CONTACTLABEL_PUB_CELLULAR",
    "CONTACTLABEL_PUB_DOMESTIC",
    "CONTACTLABEL_PUB_FAX",
    "CONTACTLABEL_PUB_INTERNATIONAL",
    "CONTACTLABEL_PUB_ISDN",
    "CONTACTLABEL_PUB_LOGO",
    "CONTACTLABEL_PUB_MOBILE",
    "CONTACTLABEL_PUB_MODEM",
    "CONTACTLABEL_PUB_OTHER",
    "CONTACTLABEL_PUB_PAGER",
    "CONTACTLABEL_PUB_PARCEL",
    "CONTACTLABEL_PUB_PCS",
    "CONTACTLABEL_PUB_PERSONAL",
    "CONTACTLABEL_PUB_POSTAL",
    "CONTACTLABEL_PUB_PREFERRED",
    "CONTACTLABEL_PUB_TTY",
    "CONTACTLABEL_PUB_USERTILE",
    "CONTACTLABEL_PUB_VIDEO",
    "CONTACTLABEL_PUB_VOICE",
    "CONTACTLABEL_WAB_ANNIVERSARY",
    "CONTACTLABEL_WAB_ASSISTANT",
    "CONTACTLABEL_WAB_BIRTHDAY",
    "CONTACTLABEL_WAB_CHILD",
    "CONTACTLABEL_WAB_MANAGER",
    "CONTACTLABEL_WAB_SCHOOL",
    "CONTACTLABEL_WAB_SOCIALNETWORK",
    "CONTACTLABEL_WAB_SPOUSE",
    "CONTACTLABEL_WAB_WISHLIST",
    "CONTACTPROP_PUB_CREATIONDATE",
    "CONTACTPROP_PUB_GENDER",
    "CONTACTPROP_PUB_GENDER_FEMALE",
    "CONTACTPROP_PUB_GENDER_MALE",
    "CONTACTPROP_PUB_GENDER_UNSPECIFIED",
    "CONTACTPROP_PUB_L1_CERTIFICATECOLLECTION",
    "CONTACTPROP_PUB_L1_CONTACTIDCOLLECTION",
    "CONTACTPROP_PUB_L1_DATECOLLECTION",
    "CONTACTPROP_PUB_L1_EMAILADDRESSCOLLECTION",
    "CONTACTPROP_PUB_L1_IMADDRESSCOLLECTION",
    "CONTACTPROP_PUB_L1_NAMECOLLECTION",
    "CONTACTPROP_PUB_L1_PERSONCOLLECTION",
    "CONTACTPROP_PUB_L1_PHONENUMBERCOLLECTION",
    "CONTACTPROP_PUB_L1_PHOTOCOLLECTION",
    "CONTACTPROP_PUB_L1_PHYSICALADDRESSCOLLECTION",
    "CONTACTPROP_PUB_L1_POSITIONCOLLECTION",
    "CONTACTPROP_PUB_L1_URLCOLLECTION",
    "CONTACTPROP_PUB_L2_CERTIFICATE",
    "CONTACTPROP_PUB_L2_CONTACTID",
    "CONTACTPROP_PUB_L2_DATE",
    "CONTACTPROP_PUB_L2_EMAILADDRESS",
    "CONTACTPROP_PUB_L2_IMADDRESSENTRY",
    "CONTACTPROP_PUB_L2_NAME",
    "CONTACTPROP_PUB_L2_PERSON",
    "CONTACTPROP_PUB_L2_PHONENUMBER",
    "CONTACTPROP_PUB_L2_PHOTO",
    "CONTACTPROP_PUB_L2_PHYSICALADDRESS",
    "CONTACTPROP_PUB_L2_POSITION",
    "CONTACTPROP_PUB_L2_URL",
    "CONTACTPROP_PUB_L3_ADDRESS",
    "CONTACTPROP_PUB_L3_ADDRESSLABEL",
    "CONTACTPROP_PUB_L3_ALTERNATE",
    "CONTACTPROP_PUB_L3_COMPANY",
    "CONTACTPROP_PUB_L3_COUNTRY",
    "CONTACTPROP_PUB_L3_DEPARTMENT",
    "CONTACTPROP_PUB_L3_EXTENDEDADDRESS",
    "CONTACTPROP_PUB_L3_FAMILYNAME",
    "CONTACTPROP_PUB_L3_FORMATTEDNAME",
    "CONTACTPROP_PUB_L3_GENERATION",
    "CONTACTPROP_PUB_L3_GIVENNAME",
    "CONTACTPROP_PUB_L3_JOB_TITLE",
    "CONTACTPROP_PUB_L3_LOCALITY",
    "CONTACTPROP_PUB_L3_MIDDLENAME",
    "CONTACTPROP_PUB_L3_NICKNAME",
    "CONTACTPROP_PUB_L3_NUMBER",
    "CONTACTPROP_PUB_L3_OFFICE",
    "CONTACTPROP_PUB_L3_ORGANIZATION",
    "CONTACTPROP_PUB_L3_PERSONID",
    "CONTACTPROP_PUB_L3_PHONETIC",
    "CONTACTPROP_PUB_L3_POBOX",
    "CONTACTPROP_PUB_L3_POSTALCODE",
    "CONTACTPROP_PUB_L3_PREFIX",
    "CONTACTPROP_PUB_L3_PROFESSION",
    "CONTACTPROP_PUB_L3_PROTOCOL",
    "CONTACTPROP_PUB_L3_REGION",
    "CONTACTPROP_PUB_L3_ROLE",
    "CONTACTPROP_PUB_L3_STREET",
    "CONTACTPROP_PUB_L3_SUFFIX",
    "CONTACTPROP_PUB_L3_THUMBPRINT",
    "CONTACTPROP_PUB_L3_TITLE",
    "CONTACTPROP_PUB_L3_TYPE",
    "CONTACTPROP_PUB_L3_URL",
    "CONTACTPROP_PUB_L3_VALUE",
    "CONTACTPROP_PUB_MAILER",
    "CONTACTPROP_PUB_NOTES",
    "CONTACTPROP_PUB_PROGID",
    "CONTACT_AGGREGATION_BLOB",
    "CONTACT_AGGREGATION_COLLECTION_OPTIONS",
    "CONTACT_AGGREGATION_CREATE_OR_OPEN_OPTIONS",
    "Contact",
    "ContactManager",
    "IContact",
    "IContactAggregationAggregate",
    "IContactAggregationAggregateCollection",
    "IContactAggregationContact",
    "IContactAggregationContactCollection",
    "IContactAggregationGroup",
    "IContactAggregationGroupCollection",
    "IContactAggregationLink",
    "IContactAggregationLinkCollection",
    "IContactAggregationManager",
    "IContactAggregationServerPerson",
    "IContactAggregationServerPersonCollection",
    "IContactCollection",
    "IContactManager",
    "IContactProperties",
    "IContactPropertyCollection",
]
