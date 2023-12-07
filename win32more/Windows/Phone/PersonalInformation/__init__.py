from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Phone.PersonalInformation
import win32more.Windows.Storage.Streams
class ContactAddress(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.PersonalInformation.IContactAddress
    _classid_ = 'Windows.Phone.PersonalInformation.ContactAddress'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.Phone.PersonalInformation.ContactAddress.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Phone.PersonalInformation.ContactAddress: ...
    @winrt_mixinmethod
    def get_Country(self: win32more.Windows.Phone.PersonalInformation.IContactAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Country(self: win32more.Windows.Phone.PersonalInformation.IContactAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Locality(self: win32more.Windows.Phone.PersonalInformation.IContactAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Locality(self: win32more.Windows.Phone.PersonalInformation.IContactAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Region(self: win32more.Windows.Phone.PersonalInformation.IContactAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Region(self: win32more.Windows.Phone.PersonalInformation.IContactAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PostalCode(self: win32more.Windows.Phone.PersonalInformation.IContactAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PostalCode(self: win32more.Windows.Phone.PersonalInformation.IContactAddress, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_StreetAddress(self: win32more.Windows.Phone.PersonalInformation.IContactAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_StreetAddress(self: win32more.Windows.Phone.PersonalInformation.IContactAddress, value: WinRT_String) -> Void: ...
    Country = property(get_Country, put_Country)
    Locality = property(get_Locality, put_Locality)
    Region = property(get_Region, put_Region)
    PostalCode = property(get_PostalCode, put_PostalCode)
    StreetAddress = property(get_StreetAddress, put_StreetAddress)
class ContactChangeRecord(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.PersonalInformation.IContactChangeRecord
    _classid_ = 'Windows.Phone.PersonalInformation.ContactChangeRecord'
    @winrt_mixinmethod
    def get_ChangeType(self: win32more.Windows.Phone.PersonalInformation.IContactChangeRecord) -> win32more.Windows.Phone.PersonalInformation.ContactChangeType: ...
    @winrt_mixinmethod
    def get_RevisionNumber(self: win32more.Windows.Phone.PersonalInformation.IContactChangeRecord) -> UInt64: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Phone.PersonalInformation.IContactChangeRecord) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RemoteId(self: win32more.Windows.Phone.PersonalInformation.IContactChangeRecord) -> WinRT_String: ...
    ChangeType = property(get_ChangeType, None)
    RevisionNumber = property(get_RevisionNumber, None)
    Id = property(get_Id, None)
    RemoteId = property(get_RemoteId, None)
ContactChangeType = Int32
ContactChangeType_Created: ContactChangeType = 0
ContactChangeType_Modified: ContactChangeType = 1
ContactChangeType_Deleted: ContactChangeType = 2
class ContactInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.PersonalInformation.IContactInformation
    _classid_ = 'Windows.Phone.PersonalInformation.ContactInformation'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.Phone.PersonalInformation.ContactInformation.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Phone.PersonalInformation.ContactInformation: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Phone.PersonalInformation.IContactInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: win32more.Windows.Phone.PersonalInformation.IContactInformation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FamilyName(self: win32more.Windows.Phone.PersonalInformation.IContactInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_FamilyName(self: win32more.Windows.Phone.PersonalInformation.IContactInformation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_GivenName(self: win32more.Windows.Phone.PersonalInformation.IContactInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_GivenName(self: win32more.Windows.Phone.PersonalInformation.IContactInformation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_HonorificPrefix(self: win32more.Windows.Phone.PersonalInformation.IContactInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_HonorificPrefix(self: win32more.Windows.Phone.PersonalInformation.IContactInformation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_HonorificSuffix(self: win32more.Windows.Phone.PersonalInformation.IContactInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_HonorificSuffix(self: win32more.Windows.Phone.PersonalInformation.IContactInformation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def GetDisplayPictureAsync(self: win32more.Windows.Phone.PersonalInformation.IContactInformation) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_mixinmethod
    def SetDisplayPictureAsync(self: win32more.Windows.Phone.PersonalInformation.IContactInformation, stream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_DisplayPicture(self: win32more.Windows.Phone.PersonalInformation.IContactInformation) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def GetPropertiesAsync(self: win32more.Windows.Phone.PersonalInformation.IContactInformation) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]]: ...
    @winrt_mixinmethod
    def ToVcardAsync(self: win32more.Windows.Phone.PersonalInformation.IContactInformation) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_mixinmethod
    def ToVcardWithOptionsAsync(self: win32more.Windows.Phone.PersonalInformation.IContactInformation, format: win32more.Windows.Phone.PersonalInformation.VCardFormat) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_classmethod
    def ParseVcardAsync(cls: win32more.Windows.Phone.PersonalInformation.IContactInformationStatics, vcard: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Phone.PersonalInformation.ContactInformation]: ...
    DisplayName = property(get_DisplayName, put_DisplayName)
    FamilyName = property(get_FamilyName, put_FamilyName)
    GivenName = property(get_GivenName, put_GivenName)
    HonorificPrefix = property(get_HonorificPrefix, put_HonorificPrefix)
    HonorificSuffix = property(get_HonorificSuffix, put_HonorificSuffix)
    DisplayPicture = property(get_DisplayPicture, None)
class ContactQueryOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.PersonalInformation.IContactQueryOptions
    _classid_ = 'Windows.Phone.PersonalInformation.ContactQueryOptions'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.Phone.PersonalInformation.ContactQueryOptions.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Phone.PersonalInformation.ContactQueryOptions: ...
    @winrt_mixinmethod
    def get_DesiredFields(self: win32more.Windows.Phone.PersonalInformation.IContactQueryOptions) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_OrderBy(self: win32more.Windows.Phone.PersonalInformation.IContactQueryOptions) -> win32more.Windows.Phone.PersonalInformation.ContactQueryResultOrdering: ...
    @winrt_mixinmethod
    def put_OrderBy(self: win32more.Windows.Phone.PersonalInformation.IContactQueryOptions, value: win32more.Windows.Phone.PersonalInformation.ContactQueryResultOrdering) -> Void: ...
    DesiredFields = property(get_DesiredFields, None)
    OrderBy = property(get_OrderBy, put_OrderBy)
class ContactQueryResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.PersonalInformation.IContactQueryResult
    _classid_ = 'Windows.Phone.PersonalInformation.ContactQueryResult'
    @winrt_mixinmethod
    def GetContactCountAsync(self: win32more.Windows.Phone.PersonalInformation.IContactQueryResult) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def GetContactsAsync(self: win32more.Windows.Phone.PersonalInformation.IContactQueryResult) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Phone.PersonalInformation.StoredContact]]: ...
    @winrt_mixinmethod
    def GetContactsAsyncInRange(self: win32more.Windows.Phone.PersonalInformation.IContactQueryResult, startIndex: UInt32, maxNumberOfItems: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Phone.PersonalInformation.StoredContact]]: ...
    @winrt_mixinmethod
    def GetCurrentQueryOptions(self: win32more.Windows.Phone.PersonalInformation.IContactQueryResult) -> win32more.Windows.Phone.PersonalInformation.ContactQueryOptions: ...
ContactQueryResultOrdering = Int32
ContactQueryResultOrdering_SystemDefault: ContactQueryResultOrdering = 0
ContactQueryResultOrdering_GivenNameFamilyName: ContactQueryResultOrdering = 1
ContactQueryResultOrdering_FamilyNameGivenName: ContactQueryResultOrdering = 2
class ContactStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.PersonalInformation.IContactStore
    _classid_ = 'Windows.Phone.PersonalInformation.ContactStore'
    @winrt_mixinmethod
    def FindContactByRemoteIdAsync(self: win32more.Windows.Phone.PersonalInformation.IContactStore, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Phone.PersonalInformation.StoredContact]: ...
    @winrt_mixinmethod
    def FindContactByIdAsync(self: win32more.Windows.Phone.PersonalInformation.IContactStore, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Phone.PersonalInformation.StoredContact]: ...
    @winrt_mixinmethod
    def DeleteContactAsync(self: win32more.Windows.Phone.PersonalInformation.IContactStore, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CreateContactQueryDefault(self: win32more.Windows.Phone.PersonalInformation.IContactStore) -> win32more.Windows.Phone.PersonalInformation.ContactQueryResult: ...
    @winrt_mixinmethod
    def CreateContactQueryWithOptions(self: win32more.Windows.Phone.PersonalInformation.IContactStore, options: win32more.Windows.Phone.PersonalInformation.ContactQueryOptions) -> win32more.Windows.Phone.PersonalInformation.ContactQueryResult: ...
    @winrt_mixinmethod
    def DeleteAsync(self: win32more.Windows.Phone.PersonalInformation.IContactStore) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_RevisionNumber(self: win32more.Windows.Phone.PersonalInformation.IContactStore) -> UInt64: ...
    @winrt_mixinmethod
    def GetChangesAsync(self: win32more.Windows.Phone.PersonalInformation.IContactStore, baseRevisionNumber: UInt64) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Phone.PersonalInformation.ContactChangeRecord]]: ...
    @winrt_mixinmethod
    def LoadExtendedPropertiesAsync(self: win32more.Windows.Phone.PersonalInformation.IContactStore) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]]: ...
    @winrt_mixinmethod
    def SaveExtendedPropertiesAsync(self: win32more.Windows.Phone.PersonalInformation.IContactStore, data: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CreateMeContactAsync(self: win32more.Windows.Phone.PersonalInformation.IContactStore2, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Phone.PersonalInformation.StoredContact]: ...
    @winrt_classmethod
    def CreateOrOpenAsync(cls: win32more.Windows.Phone.PersonalInformation.IContactStoreStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Phone.PersonalInformation.ContactStore]: ...
    @winrt_classmethod
    def CreateOrOpenWithOptionsAsync(cls: win32more.Windows.Phone.PersonalInformation.IContactStoreStatics, access: win32more.Windows.Phone.PersonalInformation.ContactStoreSystemAccessMode, sharing: win32more.Windows.Phone.PersonalInformation.ContactStoreApplicationAccessMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Phone.PersonalInformation.ContactStore]: ...
    RevisionNumber = property(get_RevisionNumber, None)
ContactStoreApplicationAccessMode = Int32
ContactStoreApplicationAccessMode_LimitedReadOnly: ContactStoreApplicationAccessMode = 0
ContactStoreApplicationAccessMode_ReadOnly: ContactStoreApplicationAccessMode = 1
ContactStoreSystemAccessMode = Int32
ContactStoreSystemAccessMode_ReadOnly: ContactStoreSystemAccessMode = 0
ContactStoreSystemAccessMode_ReadWrite: ContactStoreSystemAccessMode = 1
class IContactAddress(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.PersonalInformation.IContactAddress'
    _iid_ = Guid('{5f24f927-94a9-44a2-a155-2d0b37d1dccd}')
    @winrt_commethod(6)
    def get_Country(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Country(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Locality(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Locality(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Region(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_Region(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_PostalCode(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_PostalCode(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_StreetAddress(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_StreetAddress(self, value: WinRT_String) -> Void: ...
    Country = property(get_Country, put_Country)
    Locality = property(get_Locality, put_Locality)
    Region = property(get_Region, put_Region)
    PostalCode = property(get_PostalCode, put_PostalCode)
    StreetAddress = property(get_StreetAddress, put_StreetAddress)
class IContactChangeRecord(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.PersonalInformation.IContactChangeRecord'
    _iid_ = Guid('{b9d3f78f-513b-4742-be00-cc5c5c236b04}')
    @winrt_commethod(6)
    def get_ChangeType(self) -> win32more.Windows.Phone.PersonalInformation.ContactChangeType: ...
    @winrt_commethod(7)
    def get_RevisionNumber(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_RemoteId(self) -> WinRT_String: ...
    ChangeType = property(get_ChangeType, None)
    RevisionNumber = property(get_RevisionNumber, None)
    Id = property(get_Id, None)
    RemoteId = property(get_RemoteId, None)
class IContactInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.PersonalInformation.IContactInformation'
    _iid_ = Guid('{e2b51ffc-e792-4ab7-b15b-f2e078664dea}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_FamilyName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_FamilyName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_GivenName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_GivenName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_HonorificPrefix(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_HonorificPrefix(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_HonorificSuffix(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_HonorificSuffix(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def GetDisplayPictureAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_commethod(17)
    def SetDisplayPictureAsync(self, stream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(18)
    def get_DisplayPicture(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(19)
    def GetPropertiesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]]: ...
    @winrt_commethod(20)
    def ToVcardAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_commethod(21)
    def ToVcardWithOptionsAsync(self, format: win32more.Windows.Phone.PersonalInformation.VCardFormat) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    DisplayName = property(get_DisplayName, put_DisplayName)
    FamilyName = property(get_FamilyName, put_FamilyName)
    GivenName = property(get_GivenName, put_GivenName)
    HonorificPrefix = property(get_HonorificPrefix, put_HonorificPrefix)
    HonorificSuffix = property(get_HonorificSuffix, put_HonorificSuffix)
    DisplayPicture = property(get_DisplayPicture, None)
class IContactInformation2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.PersonalInformation.IContactInformation2'
    _iid_ = Guid('{3198b20c-621e-4668-ac38-d667b87d06d5}')
    @winrt_commethod(6)
    def get_DisplayPictureDate(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def put_DisplayPictureDate(self, returnValue: win32more.Windows.Foundation.DateTime) -> Void: ...
    DisplayPictureDate = property(get_DisplayPictureDate, put_DisplayPictureDate)
class IContactInformationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.PersonalInformation.IContactInformationStatics'
    _iid_ = Guid('{0f67bb29-03d0-4be6-b2a5-fb13859f1202}')
    @winrt_commethod(6)
    def ParseVcardAsync(self, vcard: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Phone.PersonalInformation.ContactInformation]: ...
class IContactQueryOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.PersonalInformation.IContactQueryOptions'
    _iid_ = Guid('{580cab76-3f31-46c1-9a50-424a53dacae3}')
    @winrt_commethod(6)
    def get_DesiredFields(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(7)
    def get_OrderBy(self) -> win32more.Windows.Phone.PersonalInformation.ContactQueryResultOrdering: ...
    @winrt_commethod(8)
    def put_OrderBy(self, value: win32more.Windows.Phone.PersonalInformation.ContactQueryResultOrdering) -> Void: ...
    DesiredFields = property(get_DesiredFields, None)
    OrderBy = property(get_OrderBy, put_OrderBy)
class IContactQueryResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.PersonalInformation.IContactQueryResult'
    _iid_ = Guid('{c03db722-ecdb-4700-857e-3e786426b04b}')
    @winrt_commethod(6)
    def GetContactCountAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_commethod(7)
    def GetContactsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Phone.PersonalInformation.StoredContact]]: ...
    @winrt_commethod(8)
    def GetContactsAsyncInRange(self, startIndex: UInt32, maxNumberOfItems: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Phone.PersonalInformation.StoredContact]]: ...
    @winrt_commethod(9)
    def GetCurrentQueryOptions(self) -> win32more.Windows.Phone.PersonalInformation.ContactQueryOptions: ...
class IContactStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.PersonalInformation.IContactStore'
    _iid_ = Guid('{b2cd6fef-2bfd-4fad-8552-4e698097e8eb}')
    @winrt_commethod(6)
    def FindContactByRemoteIdAsync(self, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Phone.PersonalInformation.StoredContact]: ...
    @winrt_commethod(7)
    def FindContactByIdAsync(self, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Phone.PersonalInformation.StoredContact]: ...
    @winrt_commethod(8)
    def DeleteContactAsync(self, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def CreateContactQueryDefault(self) -> win32more.Windows.Phone.PersonalInformation.ContactQueryResult: ...
    @winrt_commethod(10)
    def CreateContactQueryWithOptions(self, options: win32more.Windows.Phone.PersonalInformation.ContactQueryOptions) -> win32more.Windows.Phone.PersonalInformation.ContactQueryResult: ...
    @winrt_commethod(11)
    def DeleteAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def get_RevisionNumber(self) -> UInt64: ...
    @winrt_commethod(13)
    def GetChangesAsync(self, baseRevisionNumber: UInt64) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Phone.PersonalInformation.ContactChangeRecord]]: ...
    @winrt_commethod(14)
    def LoadExtendedPropertiesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]]: ...
    @winrt_commethod(15)
    def SaveExtendedPropertiesAsync(self, data: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.IAsyncAction: ...
    RevisionNumber = property(get_RevisionNumber, None)
class IContactStore2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.PersonalInformation.IContactStore2'
    _iid_ = Guid('{65f1b64f-d653-43a7-b236-b30c0f4d7269}')
    @winrt_commethod(6)
    def CreateMeContactAsync(self, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Phone.PersonalInformation.StoredContact]: ...
class IContactStoreStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.PersonalInformation.IContactStoreStatics'
    _iid_ = Guid('{a804fe22-4beb-44cc-a572-67a5b92e8567}')
    @winrt_commethod(6)
    def CreateOrOpenAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Phone.PersonalInformation.ContactStore]: ...
    @winrt_commethod(7)
    def CreateOrOpenWithOptionsAsync(self, access: win32more.Windows.Phone.PersonalInformation.ContactStoreSystemAccessMode, sharing: win32more.Windows.Phone.PersonalInformation.ContactStoreApplicationAccessMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Phone.PersonalInformation.ContactStore]: ...
class IKnownContactPropertiesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics'
    _iid_ = Guid('{d5812b01-2ced-4ee6-b1d6-094bf88ef0b6}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_FamilyName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_GivenName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_HonorificPrefix(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_HonorificSuffix(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_AdditionalName(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_Address(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_OtherAddress(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_Email(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_WorkAddress(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_WorkTelephone(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def get_JobTitle(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def get_Birthdate(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_Anniversary(self) -> WinRT_String: ...
    @winrt_commethod(20)
    def get_Telephone(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def get_MobileTelephone(self) -> WinRT_String: ...
    @winrt_commethod(22)
    def get_Url(self) -> WinRT_String: ...
    @winrt_commethod(23)
    def get_Notes(self) -> WinRT_String: ...
    @winrt_commethod(24)
    def get_WorkFax(self) -> WinRT_String: ...
    @winrt_commethod(25)
    def get_Children(self) -> WinRT_String: ...
    @winrt_commethod(26)
    def get_SignificantOther(self) -> WinRT_String: ...
    @winrt_commethod(27)
    def get_CompanyName(self) -> WinRT_String: ...
    @winrt_commethod(28)
    def get_CompanyTelephone(self) -> WinRT_String: ...
    @winrt_commethod(29)
    def get_HomeFax(self) -> WinRT_String: ...
    @winrt_commethod(30)
    def get_AlternateTelephone(self) -> WinRT_String: ...
    @winrt_commethod(31)
    def get_Manager(self) -> WinRT_String: ...
    @winrt_commethod(32)
    def get_Nickname(self) -> WinRT_String: ...
    @winrt_commethod(33)
    def get_OfficeLocation(self) -> WinRT_String: ...
    @winrt_commethod(34)
    def get_WorkEmail(self) -> WinRT_String: ...
    @winrt_commethod(35)
    def get_YomiGivenName(self) -> WinRT_String: ...
    @winrt_commethod(36)
    def get_YomiFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(37)
    def get_YomiCompanyName(self) -> WinRT_String: ...
    @winrt_commethod(38)
    def get_OtherEmail(self) -> WinRT_String: ...
    @winrt_commethod(39)
    def get_AlternateMobileTelephone(self) -> WinRT_String: ...
    @winrt_commethod(40)
    def get_AlternateWorkTelephone(self) -> WinRT_String: ...
    DisplayName = property(get_DisplayName, None)
    FamilyName = property(get_FamilyName, None)
    GivenName = property(get_GivenName, None)
    HonorificPrefix = property(get_HonorificPrefix, None)
    HonorificSuffix = property(get_HonorificSuffix, None)
    AdditionalName = property(get_AdditionalName, None)
    Address = property(get_Address, None)
    OtherAddress = property(get_OtherAddress, None)
    Email = property(get_Email, None)
    WorkAddress = property(get_WorkAddress, None)
    WorkTelephone = property(get_WorkTelephone, None)
    JobTitle = property(get_JobTitle, None)
    Birthdate = property(get_Birthdate, None)
    Anniversary = property(get_Anniversary, None)
    Telephone = property(get_Telephone, None)
    MobileTelephone = property(get_MobileTelephone, None)
    Url = property(get_Url, None)
    Notes = property(get_Notes, None)
    WorkFax = property(get_WorkFax, None)
    Children = property(get_Children, None)
    SignificantOther = property(get_SignificantOther, None)
    CompanyName = property(get_CompanyName, None)
    CompanyTelephone = property(get_CompanyTelephone, None)
    HomeFax = property(get_HomeFax, None)
    AlternateTelephone = property(get_AlternateTelephone, None)
    Manager = property(get_Manager, None)
    Nickname = property(get_Nickname, None)
    OfficeLocation = property(get_OfficeLocation, None)
    WorkEmail = property(get_WorkEmail, None)
    YomiGivenName = property(get_YomiGivenName, None)
    YomiFamilyName = property(get_YomiFamilyName, None)
    YomiCompanyName = property(get_YomiCompanyName, None)
    OtherEmail = property(get_OtherEmail, None)
    AlternateMobileTelephone = property(get_AlternateMobileTelephone, None)
    AlternateWorkTelephone = property(get_AlternateWorkTelephone, None)
class IStoredContact(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.PersonalInformation.IStoredContact'
    _iid_ = Guid('{b070b7b1-263d-4e71-abe7-591d2466570e}')
    @winrt_commethod(6)
    def get_Store(self) -> win32more.Windows.Phone.PersonalInformation.ContactStore: ...
    @winrt_commethod(7)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_RemoteId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_RemoteId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def GetExtendedPropertiesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]]: ...
    @winrt_commethod(11)
    def SaveAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def ReplaceExistingContactAsync(self, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    Store = property(get_Store, None)
    Id = property(get_Id, None)
    RemoteId = property(get_RemoteId, put_RemoteId)
class IStoredContactFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.PersonalInformation.IStoredContactFactory'
    _iid_ = Guid('{49ede921-c225-4fd9-89c5-cecc2c8a4b79}')
    @winrt_commethod(6)
    def CreateStoredContact(self, store: win32more.Windows.Phone.PersonalInformation.ContactStore) -> win32more.Windows.Phone.PersonalInformation.StoredContact: ...
    @winrt_commethod(7)
    def CreateStoredContactFromInformation(self, store: win32more.Windows.Phone.PersonalInformation.ContactStore, contact: win32more.Windows.Phone.PersonalInformation.ContactInformation) -> win32more.Windows.Phone.PersonalInformation.StoredContact: ...
class _KnownContactProperties_Meta_(ComPtr.__class__):
    pass
class KnownContactProperties(ComPtr, metaclass=_KnownContactProperties_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.PersonalInformation.KnownContactProperties'
    @winrt_classmethod
    def get_DisplayName(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_FamilyName(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_GivenName(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HonorificPrefix(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HonorificSuffix(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AdditionalName(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Address(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_OtherAddress(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Email(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_WorkAddress(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_WorkTelephone(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_JobTitle(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Birthdate(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Anniversary(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Telephone(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_MobileTelephone(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Url(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Notes(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_WorkFax(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Children(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SignificantOther(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_CompanyName(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_CompanyTelephone(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HomeFax(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AlternateTelephone(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Manager(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Nickname(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_OfficeLocation(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_WorkEmail(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_YomiGivenName(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_YomiFamilyName(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_YomiCompanyName(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_OtherEmail(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AlternateMobileTelephone(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AlternateWorkTelephone(cls: win32more.Windows.Phone.PersonalInformation.IKnownContactPropertiesStatics) -> WinRT_String: ...
    _KnownContactProperties_Meta_.DisplayName = property(get_DisplayName.__wrapped__, None)
    _KnownContactProperties_Meta_.FamilyName = property(get_FamilyName.__wrapped__, None)
    _KnownContactProperties_Meta_.GivenName = property(get_GivenName.__wrapped__, None)
    _KnownContactProperties_Meta_.HonorificPrefix = property(get_HonorificPrefix.__wrapped__, None)
    _KnownContactProperties_Meta_.HonorificSuffix = property(get_HonorificSuffix.__wrapped__, None)
    _KnownContactProperties_Meta_.AdditionalName = property(get_AdditionalName.__wrapped__, None)
    _KnownContactProperties_Meta_.Address = property(get_Address.__wrapped__, None)
    _KnownContactProperties_Meta_.OtherAddress = property(get_OtherAddress.__wrapped__, None)
    _KnownContactProperties_Meta_.Email = property(get_Email.__wrapped__, None)
    _KnownContactProperties_Meta_.WorkAddress = property(get_WorkAddress.__wrapped__, None)
    _KnownContactProperties_Meta_.WorkTelephone = property(get_WorkTelephone.__wrapped__, None)
    _KnownContactProperties_Meta_.JobTitle = property(get_JobTitle.__wrapped__, None)
    _KnownContactProperties_Meta_.Birthdate = property(get_Birthdate.__wrapped__, None)
    _KnownContactProperties_Meta_.Anniversary = property(get_Anniversary.__wrapped__, None)
    _KnownContactProperties_Meta_.Telephone = property(get_Telephone.__wrapped__, None)
    _KnownContactProperties_Meta_.MobileTelephone = property(get_MobileTelephone.__wrapped__, None)
    _KnownContactProperties_Meta_.Url = property(get_Url.__wrapped__, None)
    _KnownContactProperties_Meta_.Notes = property(get_Notes.__wrapped__, None)
    _KnownContactProperties_Meta_.WorkFax = property(get_WorkFax.__wrapped__, None)
    _KnownContactProperties_Meta_.Children = property(get_Children.__wrapped__, None)
    _KnownContactProperties_Meta_.SignificantOther = property(get_SignificantOther.__wrapped__, None)
    _KnownContactProperties_Meta_.CompanyName = property(get_CompanyName.__wrapped__, None)
    _KnownContactProperties_Meta_.CompanyTelephone = property(get_CompanyTelephone.__wrapped__, None)
    _KnownContactProperties_Meta_.HomeFax = property(get_HomeFax.__wrapped__, None)
    _KnownContactProperties_Meta_.AlternateTelephone = property(get_AlternateTelephone.__wrapped__, None)
    _KnownContactProperties_Meta_.Manager = property(get_Manager.__wrapped__, None)
    _KnownContactProperties_Meta_.Nickname = property(get_Nickname.__wrapped__, None)
    _KnownContactProperties_Meta_.OfficeLocation = property(get_OfficeLocation.__wrapped__, None)
    _KnownContactProperties_Meta_.WorkEmail = property(get_WorkEmail.__wrapped__, None)
    _KnownContactProperties_Meta_.YomiGivenName = property(get_YomiGivenName.__wrapped__, None)
    _KnownContactProperties_Meta_.YomiFamilyName = property(get_YomiFamilyName.__wrapped__, None)
    _KnownContactProperties_Meta_.YomiCompanyName = property(get_YomiCompanyName.__wrapped__, None)
    _KnownContactProperties_Meta_.OtherEmail = property(get_OtherEmail.__wrapped__, None)
    _KnownContactProperties_Meta_.AlternateMobileTelephone = property(get_AlternateMobileTelephone.__wrapped__, None)
    _KnownContactProperties_Meta_.AlternateWorkTelephone = property(get_AlternateWorkTelephone.__wrapped__, None)
class StoredContact(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.PersonalInformation.IStoredContact
    _classid_ = 'Windows.Phone.PersonalInformation.StoredContact'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 1:
            instance = win32more.Windows.Phone.PersonalInformation.StoredContact.CreateStoredContact(*args)
        elif len(args) == 2:
            instance = win32more.Windows.Phone.PersonalInformation.StoredContact.CreateStoredContactFromInformation(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_factorymethod
    def CreateStoredContact(cls: win32more.Windows.Phone.PersonalInformation.IStoredContactFactory, store: win32more.Windows.Phone.PersonalInformation.ContactStore) -> win32more.Windows.Phone.PersonalInformation.StoredContact: ...
    @winrt_factorymethod
    def CreateStoredContactFromInformation(cls: win32more.Windows.Phone.PersonalInformation.IStoredContactFactory, store: win32more.Windows.Phone.PersonalInformation.ContactStore, contact: win32more.Windows.Phone.PersonalInformation.ContactInformation) -> win32more.Windows.Phone.PersonalInformation.StoredContact: ...
    @winrt_mixinmethod
    def get_Store(self: win32more.Windows.Phone.PersonalInformation.IStoredContact) -> win32more.Windows.Phone.PersonalInformation.ContactStore: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Phone.PersonalInformation.IStoredContact) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RemoteId(self: win32more.Windows.Phone.PersonalInformation.IStoredContact) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_RemoteId(self: win32more.Windows.Phone.PersonalInformation.IStoredContact, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def GetExtendedPropertiesAsync(self: win32more.Windows.Phone.PersonalInformation.IStoredContact) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]]: ...
    @winrt_mixinmethod
    def SaveAsync(self: win32more.Windows.Phone.PersonalInformation.IStoredContact) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReplaceExistingContactAsync(self: win32more.Windows.Phone.PersonalInformation.IStoredContact, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Phone.PersonalInformation.IContactInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: win32more.Windows.Phone.PersonalInformation.IContactInformation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FamilyName(self: win32more.Windows.Phone.PersonalInformation.IContactInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_FamilyName(self: win32more.Windows.Phone.PersonalInformation.IContactInformation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_GivenName(self: win32more.Windows.Phone.PersonalInformation.IContactInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_GivenName(self: win32more.Windows.Phone.PersonalInformation.IContactInformation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_HonorificPrefix(self: win32more.Windows.Phone.PersonalInformation.IContactInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_HonorificPrefix(self: win32more.Windows.Phone.PersonalInformation.IContactInformation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_HonorificSuffix(self: win32more.Windows.Phone.PersonalInformation.IContactInformation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_HonorificSuffix(self: win32more.Windows.Phone.PersonalInformation.IContactInformation, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def GetDisplayPictureAsync(self: win32more.Windows.Phone.PersonalInformation.IContactInformation) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_mixinmethod
    def SetDisplayPictureAsync(self: win32more.Windows.Phone.PersonalInformation.IContactInformation, stream: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_DisplayPicture(self: win32more.Windows.Phone.PersonalInformation.IContactInformation) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def GetPropertiesAsync(self: win32more.Windows.Phone.PersonalInformation.IContactInformation) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]]: ...
    @winrt_mixinmethod
    def ToVcardAsync(self: win32more.Windows.Phone.PersonalInformation.IContactInformation) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_mixinmethod
    def ToVcardWithOptionsAsync(self: win32more.Windows.Phone.PersonalInformation.IContactInformation, format: win32more.Windows.Phone.PersonalInformation.VCardFormat) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_mixinmethod
    def get_DisplayPictureDate(self: win32more.Windows.Phone.PersonalInformation.IContactInformation2) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def put_DisplayPictureDate(self: win32more.Windows.Phone.PersonalInformation.IContactInformation2, returnValue: win32more.Windows.Foundation.DateTime) -> Void: ...
    Store = property(get_Store, None)
    Id = property(get_Id, None)
    RemoteId = property(get_RemoteId, put_RemoteId)
    DisplayName = property(get_DisplayName, put_DisplayName)
    FamilyName = property(get_FamilyName, put_FamilyName)
    GivenName = property(get_GivenName, put_GivenName)
    HonorificPrefix = property(get_HonorificPrefix, put_HonorificPrefix)
    HonorificSuffix = property(get_HonorificSuffix, put_HonorificSuffix)
    DisplayPicture = property(get_DisplayPicture, None)
    DisplayPictureDate = property(get_DisplayPictureDate, put_DisplayPictureDate)
VCardFormat = Int32
VCardFormat_Version2_1: VCardFormat = 0
VCardFormat_Version3: VCardFormat = 1
make_ready(__name__)
