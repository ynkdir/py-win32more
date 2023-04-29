from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.Contacts
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
class CONTACT_AGGREGATION_BLOB(EasyCastStructure):
    dwCount: UInt32
    lpb: POINTER(Byte)
CONTACT_AGGREGATION_COLLECTION_OPTIONS = Int32
CACO_DEFAULT: CONTACT_AGGREGATION_COLLECTION_OPTIONS = 0
CACO_INCLUDE_EXTERNAL: CONTACT_AGGREGATION_COLLECTION_OPTIONS = 1
CACO_EXTERNAL_ONLY: CONTACT_AGGREGATION_COLLECTION_OPTIONS = 2
CONTACT_AGGREGATION_CREATE_OR_OPEN_OPTIONS = Int32
CA_CREATE_LOCAL: CONTACT_AGGREGATION_CREATE_OR_OPEN_OPTIONS = 0
CA_CREATE_EXTERNAL: CONTACT_AGGREGATION_CREATE_OR_OPEN_OPTIONS = 1
Contact = Guid('61b68808-8eee-4fd1-ac-b8-3d-80-4c-8d-b0-56')
ContactManager = Guid('7165c8ab-af88-42bd-86-fd-53-10-b4-28-5a-02')
class IContact(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f941b671-bda7-4f77-88-4a-f4-64-62-f2-26-a7')
    @commethod(3)
    def GetContactID(self, pszContactID: Windows.Win32.Foundation.PWSTR, cchContactID: UInt32, pdwcchContactIDRequired: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPath(self, pszPath: Windows.Win32.Foundation.PWSTR, cchPath: UInt32, pdwcchPathRequired: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CommitChanges(self, dwCommitFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IContactAggregationAggregate(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7ed1c814-cd30-43c8-9b-8d-2e-48-9e-53-d5-4b')
    @commethod(3)
    def Save(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetComponentItems(self, pComponentItems: POINTER(Windows.Win32.System.Contacts.IContactAggregationContactCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Link(self, pAggregateId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Groups(self, options: Windows.Win32.System.Contacts.CONTACT_AGGREGATION_COLLECTION_OPTIONS, ppGroups: POINTER(Windows.Win32.System.Contacts.IContactAggregationGroupCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_AntiLink(self, ppAntiLink: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_AntiLink(self, pAntiLink: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_FavoriteOrder(self, pFavoriteOrder: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_FavoriteOrder(self, favoriteOrder: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Id(self, ppItemId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IContactAggregationAggregateCollection(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2359f3a6-3a68-40af-98-db-0f-9e-b1-43-c3-bb')
    @commethod(3)
    def FindFirst(self, ppAggregate: POINTER(Windows.Win32.System.Contacts.IContactAggregationAggregate_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FindFirstByAntiLinkId(self, pAntiLinkId: Windows.Win32.Foundation.PWSTR, ppAggregate: POINTER(Windows.Win32.System.Contacts.IContactAggregationAggregate_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FindNext(self, ppAggregate: POINTER(Windows.Win32.System.Contacts.IContactAggregationAggregate_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Count(self, pCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IContactAggregationContact(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1eb22e86-4c86-41f0-9f-9f-c2-51-e9-fd-a6-c3')
    @commethod(3)
    def Delete(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Save(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveToAggregate(self, pAggregateId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Unlink(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_AccountId(self, ppAccountId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_AccountId(self, pAccountId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_AggregateId(self, ppAggregateId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Id(self, ppItemId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_IsMe(self, pIsMe: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_IsExternal(self, pIsExternal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_NetworkSourceId(self, pNetworkSourceId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_NetworkSourceId(self, networkSourceId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_NetworkSourceIdString(self, ppNetworkSourceId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_NetworkSourceIdString(self, pNetworkSourceId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_RemoteObjectId(self, ppRemoteObjectId: POINTER(POINTER(Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_RemoteObjectId(self, pRemoteObjectId: POINTER(Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_SyncIdentityHash(self, ppSyncIdentityHash: POINTER(POINTER(Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_SyncIdentityHash(self, pSyncIdentityHash: POINTER(Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IContactAggregationContactCollection(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('826e66fa-81de-43ca-a6-fb-8c-78-5c-d9-96-c6')
    @commethod(3)
    def FindFirst(self, ppItem: POINTER(Windows.Win32.System.Contacts.IContactAggregationContact_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FindNext(self, ppItem: POINTER(Windows.Win32.System.Contacts.IContactAggregationContact_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FindFirstByIdentityHash(self, pSourceType: Windows.Win32.Foundation.PWSTR, pAccountId: Windows.Win32.Foundation.PWSTR, pIdentityHash: POINTER(Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB_head), ppItem: POINTER(Windows.Win32.System.Contacts.IContactAggregationContact_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Count(self, pCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FindFirstByRemoteId(self, pSourceType: Windows.Win32.Foundation.PWSTR, pAccountId: Windows.Win32.Foundation.PWSTR, pRemoteObjectId: POINTER(Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB_head), ppItem: POINTER(Windows.Win32.System.Contacts.IContactAggregationContact_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IContactAggregationGroup(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c93c545f-1284-499b-96-af-07-37-2a-f4-73-e0')
    @commethod(3)
    def Delete(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Save(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Add(self, pAggregateId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Remove(self, pAggregateId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Members(self, ppAggregateContactCollection: POINTER(Windows.Win32.System.Contacts.IContactAggregationAggregateCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_GlobalObjectId(self, pGlobalObjectId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_GlobalObjectId(self, pGlobalObjectId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Id(self, ppItemId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Name(self, ppName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Name(self, pName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IContactAggregationGroupCollection(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('20a19a9c-d2f3-4b83-91-43-be-ff-d2-cc-22-6d')
    @commethod(3)
    def FindFirst(self, ppGroup: POINTER(Windows.Win32.System.Contacts.IContactAggregationGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FindFirstByGlobalObjectId(self, pGlobalObjectId: POINTER(Guid), ppGroup: POINTER(Windows.Win32.System.Contacts.IContactAggregationGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FindNext(self, ppGroup: POINTER(Windows.Win32.System.Contacts.IContactAggregationGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Count(self, pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IContactAggregationLink(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b6813323-a183-4654-86-27-79-b3-0d-e3-a0-ec')
    @commethod(3)
    def Delete(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Save(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_AccountId(self, ppAccountId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_AccountId(self, pAccountId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Id(self, ppItemId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_IsLinkResolved(self, pIsLinkResolved: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_IsLinkResolved(self, isLinkResolved: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_NetworkSourceIdString(self, ppNetworkSourceId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_NetworkSourceIdString(self, pNetworkSourceId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_RemoteObjectId(self, ppRemoteObjectId: POINTER(POINTER(Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_RemoteObjectId(self, pRemoteObjectId: POINTER(Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_ServerPerson(self, ppServerPersonId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_ServerPerson(self, pServerPersonId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_ServerPersonBaseline(self, ppServerPersonId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_ServerPersonBaseline(self, pServerPersonId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_SyncIdentityHash(self, ppSyncIdentityHash: POINTER(POINTER(Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_SyncIdentityHash(self, pSyncIdentityHash: POINTER(Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IContactAggregationLinkCollection(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f8bc0e93-fb55-4f28-b9-fa-b1-c2-74-15-32-92')
    @commethod(3)
    def FindFirst(self, ppServerContactLink: POINTER(Windows.Win32.System.Contacts.IContactAggregationLink_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FindFirstByRemoteId(self, pSourceType: Windows.Win32.Foundation.PWSTR, pAccountId: Windows.Win32.Foundation.PWSTR, pRemoteId: POINTER(Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB_head), ppServerContactLink: POINTER(Windows.Win32.System.Contacts.IContactAggregationLink_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FindNext(self, ppServerContactLink: POINTER(Windows.Win32.System.Contacts.IContactAggregationLink_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Count(self, pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IContactAggregationManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1d865989-4b1f-4b60-8f-34-c2-ad-46-8b-2b-50')
    @commethod(3)
    def GetVersionInfo(self, plMajorVersion: POINTER(Int32), plMinorVersion: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateOrOpenGroup(self, pGroupName: Windows.Win32.Foundation.PWSTR, options: Windows.Win32.System.Contacts.CONTACT_AGGREGATION_CREATE_OR_OPEN_OPTIONS, pCreatedGroup: POINTER(Windows.Win32.Foundation.BOOL), ppGroup: POINTER(Windows.Win32.System.Contacts.IContactAggregationGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateExternalContact(self, ppItem: POINTER(Windows.Win32.System.Contacts.IContactAggregationContact_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateServerPerson(self, ppServerPerson: POINTER(Windows.Win32.System.Contacts.IContactAggregationServerPerson_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateServerContactLink(self, ppServerContactLink: POINTER(Windows.Win32.System.Contacts.IContactAggregationLink_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Flush(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OpenAggregateContact(self, pItemId: Windows.Win32.Foundation.PWSTR, ppItem: POINTER(Windows.Win32.System.Contacts.IContactAggregationAggregate_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OpenContact(self, pItemId: Windows.Win32.Foundation.PWSTR, ppItem: POINTER(Windows.Win32.System.Contacts.IContactAggregationContact_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def OpenServerContactLink(self, pItemId: Windows.Win32.Foundation.PWSTR, ppItem: POINTER(Windows.Win32.System.Contacts.IContactAggregationLink_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OpenServerPerson(self, pItemId: Windows.Win32.Foundation.PWSTR, ppItem: POINTER(Windows.Win32.System.Contacts.IContactAggregationServerPerson_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Contacts(self, options: Windows.Win32.System.Contacts.CONTACT_AGGREGATION_COLLECTION_OPTIONS, ppItems: POINTER(Windows.Win32.System.Contacts.IContactAggregationContactCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_AggregateContacts(self, options: Windows.Win32.System.Contacts.CONTACT_AGGREGATION_COLLECTION_OPTIONS, ppAggregates: POINTER(Windows.Win32.System.Contacts.IContactAggregationAggregateCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Groups(self, options: Windows.Win32.System.Contacts.CONTACT_AGGREGATION_COLLECTION_OPTIONS, ppGroups: POINTER(Windows.Win32.System.Contacts.IContactAggregationGroupCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_ServerPersons(self, ppServerPersonCollection: POINTER(Windows.Win32.System.Contacts.IContactAggregationServerPersonCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_ServerContactLinks(self, pPersonItemId: Windows.Win32.Foundation.PWSTR, ppServerContactLinkCollection: POINTER(Windows.Win32.System.Contacts.IContactAggregationLinkCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IContactAggregationServerPerson(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7fdc3d4b-1b82-4334-85-c5-25-18-4e-e5-a5-f2')
    @commethod(3)
    def Delete(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Save(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_AggregateId(self, ppAggregateId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_AggregateId(self, pAggregateId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_AntiLink(self, ppAntiLink: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_AntiLink(self, pAntiLink: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_AntiLinkBaseline(self, ppAntiLink: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_AntiLinkBaseline(self, pAntiLink: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_FavoriteOrder(self, pFavoriteOrder: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_FavoriteOrder(self, favoriteOrder: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_FavoriteOrderBaseline(self, pFavoriteOrder: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_FavoriteOrderBaseline(self, favoriteOrder: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Groups(self, pGroups: POINTER(POINTER(Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Groups(self, pGroups: POINTER(Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_GroupsBaseline(self, ppGroups: POINTER(POINTER(Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_GroupsBaseline(self, pGroups: POINTER(Windows.Win32.System.Contacts.CONTACT_AGGREGATION_BLOB_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_Id(self, ppId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_IsTombstone(self, pIsTombstone: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_IsTombstone(self, isTombstone: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_LinkedAggregateId(self, ppLinkedAggregateId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_LinkedAggregateId(self, pLinkedAggregateId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_ObjectId(self, ppObjectId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_ObjectId(self, pObjectId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IContactAggregationServerPersonCollection(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4f730a4a-6604-47b6-a9-87-66-9e-cf-1e-57-51')
    @commethod(3)
    def FindFirst(self, ppServerPerson: POINTER(Windows.Win32.System.Contacts.IContactAggregationServerPerson_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FindFirstByServerId(self, pServerId: Windows.Win32.Foundation.PWSTR, ppServerPerson: POINTER(Windows.Win32.System.Contacts.IContactAggregationServerPerson_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FindFirstByAggregateId(self, pAggregateId: Windows.Win32.Foundation.PWSTR, ppServerPerson: POINTER(Windows.Win32.System.Contacts.IContactAggregationServerPerson_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FindFirstByLinkedAggregateId(self, pAggregateId: Windows.Win32.Foundation.PWSTR, ppServerPerson: POINTER(Windows.Win32.System.Contacts.IContactAggregationServerPerson_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FindNext(self, ppServerPerson: POINTER(Windows.Win32.System.Contacts.IContactAggregationServerPerson_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IContactCollection(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b6afa338-d779-11d9-8b-de-f6-6b-ad-1e-3f-3a')
    @commethod(3)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrent(self, ppContact: POINTER(Windows.Win32.System.Contacts.IContact_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IContactManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ad553d98-deb1-474a-8e-17-fc-0c-20-75-b7-38')
    @commethod(3)
    def Initialize(self, pszAppName: Windows.Win32.Foundation.PWSTR, pszAppVersion: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Load(self, pszContactID: Windows.Win32.Foundation.PWSTR, ppContact: POINTER(Windows.Win32.System.Contacts.IContact_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MergeContactIDs(self, pszNewContactID: Windows.Win32.Foundation.PWSTR, pszOldContactID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMeContact(self, ppMeContact: POINTER(Windows.Win32.System.Contacts.IContact_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetMeContact(self, pMeContact: Windows.Win32.System.Contacts.IContact_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetContactCollection(self, ppContactCollection: POINTER(Windows.Win32.System.Contacts.IContactCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IContactProperties(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('70dd27dd-5cbd-46e8-be-f0-23-b6-b3-46-28-8f')
    @commethod(3)
    def GetString(self, pszPropertyName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pszValue: Windows.Win32.Foundation.PWSTR, cchValue: UInt32, pdwcchPropertyValueRequired: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDate(self, pszPropertyName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pftDateTime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetBinary(self, pszPropertyName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pszContentType: Windows.Win32.Foundation.PWSTR, cchContentType: UInt32, pdwcchContentTypeRequired: POINTER(UInt32), ppStream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetLabels(self, pszArrayElementName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pszLabels: Windows.Win32.Foundation.PWSTR, cchLabels: UInt32, pdwcchLabelsRequired: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetString(self, pszPropertyName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pszValue: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDate(self, pszPropertyName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, ftDateTime: Windows.Win32.Foundation.FILETIME) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetBinary(self, pszPropertyName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pszContentType: Windows.Win32.Foundation.PWSTR, pStream: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetLabels(self, pszArrayElementName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, dwLabelCount: UInt32, ppszLabels: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CreateArrayNode(self, pszArrayName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, fAppend: Windows.Win32.Foundation.BOOL, pszNewArrayElementName: Windows.Win32.Foundation.PWSTR, cchNewArrayElementName: UInt32, pdwcchNewArrayElementNameRequired: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DeleteProperty(self, pszPropertyName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def DeleteArrayNode(self, pszArrayElementName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def DeleteLabels(self, pszArrayElementName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetPropertyCollection(self, ppPropertyCollection: POINTER(Windows.Win32.System.Contacts.IContactPropertyCollection_head), dwFlags: UInt32, pszMultiValueName: Windows.Win32.Foundation.PWSTR, dwLabelCount: UInt32, ppszLabels: POINTER(Windows.Win32.Foundation.PWSTR), fAnyLabelMatches: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IContactPropertyCollection(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ffd3adf8-fa64-4328-b1-b6-2e-0d-b5-09-cb-3c')
    @commethod(3)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPropertyName(self, pszPropertyName: Windows.Win32.Foundation.PWSTR, cchPropertyName: UInt32, pdwcchPropertyNameRequired: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPropertyType(self, pdwType: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPropertyVersion(self, pdwVersion: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetPropertyModificationDate(self, pftModificationDate: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPropertyArrayElementID(self, pszArrayElementID: Windows.Win32.Foundation.PWSTR, cchArrayElementID: UInt32, pdwcchArrayElementIDRequired: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
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
