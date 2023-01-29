from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Com
import win32more.System.Contacts
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
CGD_DEFAULT: UInt32 = 0
CGD_UNKNOWN_PROPERTY: UInt32 = 0
CGD_STRING_PROPERTY: UInt32 = 1
CGD_DATE_PROPERTY: UInt32 = 2
CGD_BINARY_PROPERTY: UInt32 = 4
CGD_ARRAY_NODE: UInt32 = 8
CLSID_ContactAggregationManager: Guid = Guid('96c8ad95-c199-44de-b3-4e-ac-33-c4-42-df-39')
CONTACTPROP_PUB_NOTES: String = 'Notes'
CONTACTPROP_PUB_MAILER: String = 'Mailer'
CONTACTPROP_PUB_PROGID: String = 'ProgID'
CONTACTPROP_PUB_GENDER: String = 'Gender'
CONTACTPROP_PUB_GENDER_UNSPECIFIED: String = 'Unspecified'
CONTACTPROP_PUB_GENDER_MALE: String = 'Male'
CONTACTPROP_PUB_GENDER_FEMALE: String = 'Female'
CONTACTPROP_PUB_CREATIONDATE: String = 'CreationDate'
CONTACTPROP_PUB_L1_CONTACTIDCOLLECTION: String = 'ContactIDCollection'
CONTACTPROP_PUB_L2_CONTACTID: String = '/ContactID'
CONTACTPROP_PUB_L3_VALUE: String = '/Value'
CONTACTPROP_PUB_L1_NAMECOLLECTION: String = 'NameCollection'
CONTACTPROP_PUB_L2_NAME: String = '/Name'
CONTACTPROP_PUB_L3_FORMATTEDNAME: String = '/FormattedName'
CONTACTPROP_PUB_L3_PHONETIC: String = '/Phonetic'
CONTACTPROP_PUB_L3_PREFIX: String = '/Prefix'
CONTACTPROP_PUB_L3_TITLE: String = '/Title'
CONTACTPROP_PUB_L3_GIVENNAME: String = '/GivenName'
CONTACTPROP_PUB_L3_FAMILYNAME: String = '/FamilyName'
CONTACTPROP_PUB_L3_MIDDLENAME: String = '/MiddleName'
CONTACTPROP_PUB_L3_GENERATION: String = '/Generation'
CONTACTPROP_PUB_L3_SUFFIX: String = '/Suffix'
CONTACTPROP_PUB_L3_NICKNAME: String = '/NickName'
CONTACTPROP_PUB_L1_POSITIONCOLLECTION: String = 'PositionCollection'
CONTACTPROP_PUB_L2_POSITION: String = '/Position'
CONTACTPROP_PUB_L3_ORGANIZATION: String = '/Organization'
CONTACTPROP_PUB_L3_COMPANY: String = '/Company'
CONTACTPROP_PUB_L3_DEPARTMENT: String = '/Department'
CONTACTPROP_PUB_L3_OFFICE: String = '/Office'
CONTACTPROP_PUB_L3_JOB_TITLE: String = '/JobTitle'
CONTACTPROP_PUB_L3_PROFESSION: String = '/Profession'
CONTACTPROP_PUB_L3_ROLE: String = '/Role'
CONTACTPROP_PUB_L1_PERSONCOLLECTION: String = 'PersonCollection'
CONTACTPROP_PUB_L2_PERSON: String = '/Person'
CONTACTPROP_PUB_L3_PERSONID: String = '/PersonID'
CONTACTPROP_PUB_L1_DATECOLLECTION: String = 'DateCollection'
CONTACTPROP_PUB_L2_DATE: String = '/Date'
CONTACTPROP_PUB_L1_EMAILADDRESSCOLLECTION: String = 'EmailAddressCollection'
CONTACTPROP_PUB_L2_EMAILADDRESS: String = '/EmailAddress'
CONTACTPROP_PUB_L3_ADDRESS: String = '/Address'
CONTACTPROP_PUB_L3_TYPE: String = '/Type'
CONTACTPROP_PUB_L1_CERTIFICATECOLLECTION: String = 'CertificateCollection'
CONTACTPROP_PUB_L2_CERTIFICATE: String = '/Certificate'
CONTACTPROP_PUB_L3_THUMBPRINT: String = '/ThumbPrint'
CONTACTPROP_PUB_L1_PHONENUMBERCOLLECTION: String = 'PhoneNumberCollection'
CONTACTPROP_PUB_L2_PHONENUMBER: String = '/PhoneNumber'
CONTACTPROP_PUB_L3_NUMBER: String = '/Number'
CONTACTPROP_PUB_L3_ALTERNATE: String = '/Alternate'
CONTACTPROP_PUB_L1_PHYSICALADDRESSCOLLECTION: String = 'PhysicalAddressCollection'
CONTACTPROP_PUB_L2_PHYSICALADDRESS: String = '/PhysicalAddress'
CONTACTPROP_PUB_L3_ADDRESSLABEL: String = '/AddressLabel'
CONTACTPROP_PUB_L3_STREET: String = '/Street'
CONTACTPROP_PUB_L3_LOCALITY: String = '/Locality'
CONTACTPROP_PUB_L3_REGION: String = '/Region'
CONTACTPROP_PUB_L3_POSTALCODE: String = '/PostalCode'
CONTACTPROP_PUB_L3_COUNTRY: String = '/Country'
CONTACTPROP_PUB_L3_POBOX: String = '/POBox'
CONTACTPROP_PUB_L3_EXTENDEDADDRESS: String = '/ExtendedAddress'
CONTACTPROP_PUB_L1_IMADDRESSCOLLECTION: String = 'IMAddressCollection'
CONTACTPROP_PUB_L2_IMADDRESSENTRY: String = '/IMAddress'
CONTACTPROP_PUB_L3_PROTOCOL: String = '/Protocol'
CONTACTPROP_PUB_L1_URLCOLLECTION: String = 'UrlCollection'
CONTACTPROP_PUB_L2_URL: String = '/Url'
CONTACTPROP_PUB_L1_PHOTOCOLLECTION: String = 'PhotoCollection'
CONTACTPROP_PUB_L2_PHOTO: String = '/Photo'
CONTACTPROP_PUB_L3_URL: String = '/Url'
CONTACTLABEL_PUB_PREFERRED: String = 'Preferred'
CONTACTLABEL_PUB_PERSONAL: String = 'Personal'
CONTACTLABEL_PUB_BUSINESS: String = 'Business'
CONTACTLABEL_PUB_OTHER: String = 'Other'
CONTACTLABEL_PUB_VOICE: String = 'Voice'
CONTACTLABEL_PUB_MOBILE: String = 'Mobile'
CONTACTLABEL_PUB_PCS: String = 'PCS'
CONTACTLABEL_PUB_CELLULAR: String = 'Cellular'
CONTACTLABEL_PUB_CAR: String = 'Car'
CONTACTLABEL_PUB_PAGER: String = 'Pager'
CONTACTLABEL_PUB_TTY: String = 'TTY'
CONTACTLABEL_PUB_FAX: String = 'Fax'
CONTACTLABEL_PUB_VIDEO: String = 'Video'
CONTACTLABEL_PUB_MODEM: String = 'Modem'
CONTACTLABEL_PUB_BBS: String = 'BBS'
CONTACTLABEL_PUB_ISDN: String = 'ISDN'
CONTACTLABEL_PUB_AGENT: String = 'Agent'
CONTACTLABEL_PUB_DOMESTIC: String = 'Domestic'
CONTACTLABEL_PUB_INTERNATIONAL: String = 'International'
CONTACTLABEL_PUB_POSTAL: String = 'Postal'
CONTACTLABEL_PUB_PARCEL: String = 'Parcel'
CONTACTLABEL_PUB_USERTILE: String = 'UserTile'
CONTACTLABEL_PUB_LOGO: String = 'Logo'
CONTACTLABEL_WAB_SPOUSE: String = 'wab:Spouse'
CONTACTLABEL_WAB_CHILD: String = 'wab:Child'
CONTACTLABEL_WAB_MANAGER: String = 'wab:Manager'
CONTACTLABEL_WAB_ASSISTANT: String = 'wab:Assistant'
CONTACTLABEL_WAB_BIRTHDAY: String = 'wab:Birthday'
CONTACTLABEL_WAB_ANNIVERSARY: String = 'wab:Anniversary'
CONTACTLABEL_WAB_SOCIALNETWORK: String = 'wab:SocialNetwork'
CONTACTLABEL_WAB_SCHOOL: String = 'wab:School'
CONTACTLABEL_WAB_WISHLIST: String = 'wab:WishList'
Contact = Guid('61b68808-8eee-4fd1-ac-b8-3d-80-4c-8d-b0-56')
class CONTACT_AGGREGATION_BLOB(Structure):
    dwCount: UInt32
    lpb: c_char_p_no
CONTACT_AGGREGATION_COLLECTION_OPTIONS = Int32
CACO_DEFAULT: CONTACT_AGGREGATION_COLLECTION_OPTIONS = 0
CACO_INCLUDE_EXTERNAL: CONTACT_AGGREGATION_COLLECTION_OPTIONS = 1
CACO_EXTERNAL_ONLY: CONTACT_AGGREGATION_COLLECTION_OPTIONS = 2
CONTACT_AGGREGATION_CREATE_OR_OPEN_OPTIONS = Int32
CA_CREATE_LOCAL: CONTACT_AGGREGATION_CREATE_OR_OPEN_OPTIONS = 0
CA_CREATE_EXTERNAL: CONTACT_AGGREGATION_CREATE_OR_OPEN_OPTIONS = 1
ContactManager = Guid('7165c8ab-af88-42bd-86-fd-53-10-b4-28-5a-02')
class IContact(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f941b671-bda7-4f77-88-4a-f4-64-62-f2-26-a7')
    @commethod(3)
    def GetContactID(pszContactID: win32more.Foundation.PWSTR, cchContactID: UInt32, pdwcchContactIDRequired: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetPath(pszPath: win32more.Foundation.PWSTR, cchPath: UInt32, pdwcchPathRequired: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CommitChanges(dwCommitFlags: UInt32) -> win32more.Foundation.HRESULT: ...
class IContactAggregationAggregate(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('7ed1c814-cd30-43c8-9b-8d-2e-48-9e-53-d5-4b')
    @commethod(3)
    def Save() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetComponentItems(pComponentItems: POINTER(win32more.System.Contacts.IContactAggregationContactCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Link(pAggregateId: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_Groups(options: win32more.System.Contacts.CONTACT_AGGREGATION_COLLECTION_OPTIONS, ppGroups: POINTER(win32more.System.Contacts.IContactAggregationGroupCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_AntiLink(ppAntiLink: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_AntiLink(pAntiLink: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_FavoriteOrder(pFavoriteOrder: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_FavoriteOrder(favoriteOrder: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Id(ppItemId: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
class IContactAggregationAggregateCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('2359f3a6-3a68-40af-98-db-0f-9e-b1-43-c3-bb')
    @commethod(3)
    def FindFirst(ppAggregate: POINTER(win32more.System.Contacts.IContactAggregationAggregate_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def FindFirstByAntiLinkId(pAntiLinkId: win32more.Foundation.PWSTR, ppAggregate: POINTER(win32more.System.Contacts.IContactAggregationAggregate_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def FindNext(ppAggregate: POINTER(win32more.System.Contacts.IContactAggregationAggregate_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_Count(pCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IContactAggregationContact(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1eb22e86-4c86-41f0-9f-9f-c2-51-e9-fd-a6-c3')
    @commethod(3)
    def Delete() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Save() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def MoveToAggregate(pAggregateId: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Unlink() -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_AccountId(ppAccountId: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_AccountId(pAccountId: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_AggregateId(ppAggregateId: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Id(ppItemId: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_IsMe(pIsMe: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_IsExternal(pIsExternal: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_NetworkSourceId(pNetworkSourceId: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_NetworkSourceId(networkSourceId: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_NetworkSourceIdString(ppNetworkSourceId: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_NetworkSourceIdString(pNetworkSourceId: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_RemoteObjectId(ppRemoteObjectId: POINTER(POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_RemoteObjectId(pRemoteObjectId: POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_SyncIdentityHash(ppSyncIdentityHash: POINTER(POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_SyncIdentityHash(pSyncIdentityHash: POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head)) -> win32more.Foundation.HRESULT: ...
class IContactAggregationContactCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('826e66fa-81de-43ca-a6-fb-8c-78-5c-d9-96-c6')
    @commethod(3)
    def FindFirst(ppItem: POINTER(win32more.System.Contacts.IContactAggregationContact_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def FindNext(ppItem: POINTER(win32more.System.Contacts.IContactAggregationContact_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def FindFirstByIdentityHash(pSourceType: win32more.Foundation.PWSTR, pAccountId: win32more.Foundation.PWSTR, pIdentityHash: POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head), ppItem: POINTER(win32more.System.Contacts.IContactAggregationContact_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_Count(pCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def FindFirstByRemoteId(pSourceType: win32more.Foundation.PWSTR, pAccountId: win32more.Foundation.PWSTR, pRemoteObjectId: POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head), ppItem: POINTER(win32more.System.Contacts.IContactAggregationContact_head)) -> win32more.Foundation.HRESULT: ...
class IContactAggregationGroup(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c93c545f-1284-499b-96-af-07-37-2a-f4-73-e0')
    @commethod(3)
    def Delete() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Save() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Add(pAggregateId: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Remove(pAggregateId: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_Members(ppAggregateContactCollection: POINTER(win32more.System.Contacts.IContactAggregationAggregateCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_GlobalObjectId(pGlobalObjectId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_GlobalObjectId(pGlobalObjectId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Id(ppItemId: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Name(ppName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_Name(pName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class IContactAggregationGroupCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('20a19a9c-d2f3-4b83-91-43-be-ff-d2-cc-22-6d')
    @commethod(3)
    def FindFirst(ppGroup: POINTER(win32more.System.Contacts.IContactAggregationGroup_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def FindFirstByGlobalObjectId(pGlobalObjectId: POINTER(Guid), ppGroup: POINTER(win32more.System.Contacts.IContactAggregationGroup_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def FindNext(ppGroup: POINTER(win32more.System.Contacts.IContactAggregationGroup_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_Count(pCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IContactAggregationLink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b6813323-a183-4654-86-27-79-b3-0d-e3-a0-ec')
    @commethod(3)
    def Delete() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Save() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_AccountId(ppAccountId: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def put_AccountId(pAccountId: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_Id(ppItemId: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_IsLinkResolved(pIsLinkResolved: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_IsLinkResolved(isLinkResolved: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_NetworkSourceIdString(ppNetworkSourceId: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_NetworkSourceIdString(pNetworkSourceId: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_RemoteObjectId(ppRemoteObjectId: POINTER(POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_RemoteObjectId(pRemoteObjectId: POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_ServerPerson(ppServerPersonId: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_ServerPerson(pServerPersonId: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_ServerPersonBaseline(ppServerPersonId: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_ServerPersonBaseline(pServerPersonId: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_SyncIdentityHash(ppSyncIdentityHash: POINTER(POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put_SyncIdentityHash(pSyncIdentityHash: POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head)) -> win32more.Foundation.HRESULT: ...
class IContactAggregationLinkCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f8bc0e93-fb55-4f28-b9-fa-b1-c2-74-15-32-92')
    @commethod(3)
    def FindFirst(ppServerContactLink: POINTER(win32more.System.Contacts.IContactAggregationLink_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def FindFirstByRemoteId(pSourceType: win32more.Foundation.PWSTR, pAccountId: win32more.Foundation.PWSTR, pRemoteId: POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head), ppServerContactLink: POINTER(win32more.System.Contacts.IContactAggregationLink_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def FindNext(ppServerContactLink: POINTER(win32more.System.Contacts.IContactAggregationLink_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def get_Count(pCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IContactAggregationManager(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1d865989-4b1f-4b60-8f-34-c2-ad-46-8b-2b-50')
    @commethod(3)
    def GetVersionInfo(plMajorVersion: POINTER(Int32), plMinorVersion: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CreateOrOpenGroup(pGroupName: win32more.Foundation.PWSTR, options: win32more.System.Contacts.CONTACT_AGGREGATION_CREATE_OR_OPEN_OPTIONS, pCreatedGroup: POINTER(win32more.Foundation.BOOL), ppGroup: POINTER(win32more.System.Contacts.IContactAggregationGroup_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CreateExternalContact(ppItem: POINTER(win32more.System.Contacts.IContactAggregationContact_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def CreateServerPerson(ppServerPerson: POINTER(win32more.System.Contacts.IContactAggregationServerPerson_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def CreateServerContactLink(ppServerContactLink: POINTER(win32more.System.Contacts.IContactAggregationLink_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Flush() -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def OpenAggregateContact(pItemId: win32more.Foundation.PWSTR, ppItem: POINTER(win32more.System.Contacts.IContactAggregationAggregate_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def OpenContact(pItemId: win32more.Foundation.PWSTR, ppItem: POINTER(win32more.System.Contacts.IContactAggregationContact_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def OpenServerContactLink(pItemId: win32more.Foundation.PWSTR, ppItem: POINTER(win32more.System.Contacts.IContactAggregationLink_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def OpenServerPerson(pItemId: win32more.Foundation.PWSTR, ppItem: POINTER(win32more.System.Contacts.IContactAggregationServerPerson_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_Contacts(options: win32more.System.Contacts.CONTACT_AGGREGATION_COLLECTION_OPTIONS, ppItems: POINTER(win32more.System.Contacts.IContactAggregationContactCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_AggregateContacts(options: win32more.System.Contacts.CONTACT_AGGREGATION_COLLECTION_OPTIONS, ppAggregates: POINTER(win32more.System.Contacts.IContactAggregationAggregateCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_Groups(options: win32more.System.Contacts.CONTACT_AGGREGATION_COLLECTION_OPTIONS, ppGroups: POINTER(win32more.System.Contacts.IContactAggregationGroupCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_ServerPersons(ppServerPersonCollection: POINTER(win32more.System.Contacts.IContactAggregationServerPersonCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_ServerContactLinks(pPersonItemId: win32more.Foundation.PWSTR, ppServerContactLinkCollection: POINTER(win32more.System.Contacts.IContactAggregationLinkCollection_head)) -> win32more.Foundation.HRESULT: ...
class IContactAggregationServerPerson(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('7fdc3d4b-1b82-4334-85-c5-25-18-4e-e5-a5-f2')
    @commethod(3)
    def Delete() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Save() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_AggregateId(ppAggregateId: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def put_AggregateId(pAggregateId: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_AntiLink(ppAntiLink: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_AntiLink(pAntiLink: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_AntiLinkBaseline(ppAntiLink: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_AntiLinkBaseline(pAntiLink: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_FavoriteOrder(pFavoriteOrder: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_FavoriteOrder(favoriteOrder: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_FavoriteOrderBaseline(pFavoriteOrder: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_FavoriteOrderBaseline(favoriteOrder: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_Groups(pGroups: POINTER(POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_Groups(pGroups: POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_GroupsBaseline(ppGroups: POINTER(POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_GroupsBaseline(pGroups: POINTER(win32more.System.Contacts.CONTACT_AGGREGATION_BLOB_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_Id(ppId: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_IsTombstone(pIsTombstone: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def put_IsTombstone(isTombstone: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_LinkedAggregateId(ppLinkedAggregateId: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_LinkedAggregateId(pLinkedAggregateId: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_ObjectId(ppObjectId: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_ObjectId(pObjectId: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class IContactAggregationServerPersonCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4f730a4a-6604-47b6-a9-87-66-9e-cf-1e-57-51')
    @commethod(3)
    def FindFirst(ppServerPerson: POINTER(win32more.System.Contacts.IContactAggregationServerPerson_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def FindFirstByServerId(pServerId: win32more.Foundation.PWSTR, ppServerPerson: POINTER(win32more.System.Contacts.IContactAggregationServerPerson_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def FindFirstByAggregateId(pAggregateId: win32more.Foundation.PWSTR, ppServerPerson: POINTER(win32more.System.Contacts.IContactAggregationServerPerson_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def FindFirstByLinkedAggregateId(pAggregateId: win32more.Foundation.PWSTR, ppServerPerson: POINTER(win32more.System.Contacts.IContactAggregationServerPerson_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def FindNext(ppServerPerson: POINTER(win32more.System.Contacts.IContactAggregationServerPerson_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(pCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IContactCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b6afa338-d779-11d9-8b-de-f6-6b-ad-1e-3f-3a')
    @commethod(3)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Next() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrent(ppContact: POINTER(win32more.System.Contacts.IContact_head)) -> win32more.Foundation.HRESULT: ...
class IContactManager(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ad553d98-deb1-474a-8e-17-fc-0c-20-75-b7-38')
    @commethod(3)
    def Initialize(pszAppName: win32more.Foundation.PWSTR, pszAppVersion: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Load(pszContactID: win32more.Foundation.PWSTR, ppContact: POINTER(win32more.System.Contacts.IContact_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def MergeContactIDs(pszNewContactID: win32more.Foundation.PWSTR, pszOldContactID: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetMeContact(ppMeContact: POINTER(win32more.System.Contacts.IContact_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetMeContact(pMeContact: win32more.System.Contacts.IContact_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetContactCollection(ppContactCollection: POINTER(win32more.System.Contacts.IContactCollection_head)) -> win32more.Foundation.HRESULT: ...
class IContactProperties(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('70dd27dd-5cbd-46e8-be-f0-23-b6-b3-46-28-8f')
    @commethod(3)
    def GetString(pszPropertyName: win32more.Foundation.PWSTR, dwFlags: UInt32, pszValue: win32more.Foundation.PWSTR, cchValue: UInt32, pdwcchPropertyValueRequired: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetDate(pszPropertyName: win32more.Foundation.PWSTR, dwFlags: UInt32, pftDateTime: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetBinary(pszPropertyName: win32more.Foundation.PWSTR, dwFlags: UInt32, pszContentType: win32more.Foundation.PWSTR, cchContentType: UInt32, pdwcchContentTypeRequired: POINTER(UInt32), ppStream: POINTER(win32more.System.Com.IStream_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetLabels(pszArrayElementName: win32more.Foundation.PWSTR, dwFlags: UInt32, pszLabels: win32more.Foundation.PWSTR, cchLabels: UInt32, pdwcchLabelsRequired: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetString(pszPropertyName: win32more.Foundation.PWSTR, dwFlags: UInt32, pszValue: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetDate(pszPropertyName: win32more.Foundation.PWSTR, dwFlags: UInt32, ftDateTime: win32more.Foundation.FILETIME) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetBinary(pszPropertyName: win32more.Foundation.PWSTR, dwFlags: UInt32, pszContentType: win32more.Foundation.PWSTR, pStream: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetLabels(pszArrayElementName: win32more.Foundation.PWSTR, dwFlags: UInt32, dwLabelCount: UInt32, ppszLabels: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def CreateArrayNode(pszArrayName: win32more.Foundation.PWSTR, dwFlags: UInt32, fAppend: win32more.Foundation.BOOL, pszNewArrayElementName: win32more.Foundation.PWSTR, cchNewArrayElementName: UInt32, pdwcchNewArrayElementNameRequired: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def DeleteProperty(pszPropertyName: win32more.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def DeleteArrayNode(pszArrayElementName: win32more.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def DeleteLabels(pszArrayElementName: win32more.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetPropertyCollection(ppPropertyCollection: POINTER(win32more.System.Contacts.IContactPropertyCollection_head), dwFlags: UInt32, pszMultiValueName: win32more.Foundation.PWSTR, dwLabelCount: UInt32, ppszLabels: POINTER(win32more.Foundation.PWSTR), fAnyLabelMatches: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
class IContactPropertyCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ffd3adf8-fa64-4328-b1-b6-2e-0d-b5-09-cb-3c')
    @commethod(3)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Next() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetPropertyName(pszPropertyName: win32more.Foundation.PWSTR, cchPropertyName: UInt32, pdwcchPropertyNameRequired: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetPropertyType(pdwType: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetPropertyVersion(pdwVersion: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetPropertyModificationDate(pftModificationDate: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetPropertyArrayElementID(pszArrayElementID: win32more.Foundation.PWSTR, cchArrayElementID: UInt32, pdwcchArrayElementIDRequired: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
make_head(_module, 'CONTACT_AGGREGATION_BLOB')
make_head(_module, 'IContact')
make_head(_module, 'IContactAggregationAggregate')
make_head(_module, 'IContactAggregationAggregateCollection')
make_head(_module, 'IContactAggregationContact')
make_head(_module, 'IContactAggregationContactCollection')
make_head(_module, 'IContactAggregationGroup')
make_head(_module, 'IContactAggregationGroupCollection')
make_head(_module, 'IContactAggregationLink')
make_head(_module, 'IContactAggregationLinkCollection')
make_head(_module, 'IContactAggregationManager')
make_head(_module, 'IContactAggregationServerPerson')
make_head(_module, 'IContactAggregationServerPersonCollection')
make_head(_module, 'IContactCollection')
make_head(_module, 'IContactManager')
make_head(_module, 'IContactProperties')
make_head(_module, 'IContactPropertyCollection')
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
_arch_optional = [
]
