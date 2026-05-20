from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.Wdk.Foundation
import win32more.Windows.Wdk.System.Registry
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.IO
@winfunctype('ntdll.dll')
def NtNotifyChangeMultipleKeys(MasterKeyHandle: win32more.Windows.Win32.Foundation.HANDLE, Count: UInt32, SubordinateObjects: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES), Event: win32more.Windows.Win32.Foundation.HANDLE, ApcRoutine: win32more.Windows.Win32.System.IO.PIO_APC_ROUTINE, ApcContext: VoidPtr, IoStatusBlock: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), CompletionFilter: UInt32, WatchTree: win32more.Windows.Win32.Foundation.BOOLEAN, Buffer: VoidPtr, BufferSize: UInt32, Asynchronous: win32more.Windows.Win32.Foundation.BOOLEAN) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwNotifyChangeMultipleKeys(MasterKeyHandle: win32more.Windows.Win32.Foundation.HANDLE, Count: UInt32, SubordinateObjects: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES), Event: win32more.Windows.Win32.Foundation.HANDLE, ApcRoutine: win32more.Windows.Win32.System.IO.PIO_APC_ROUTINE, ApcContext: VoidPtr, IoStatusBlock: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), CompletionFilter: UInt32, WatchTree: win32more.Windows.Win32.Foundation.BOOLEAN, Buffer: VoidPtr, BufferSize: UInt32, Asynchronous: win32more.Windows.Win32.Foundation.BOOLEAN) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtQueryMultipleValueKey(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE, ValueEntries: POINTER(win32more.Windows.Wdk.System.Registry.KEY_VALUE_ENTRY), EntryCount: UInt32, ValueBuffer: VoidPtr, BufferLength: POINTER(UInt32), RequiredBufferLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwQueryMultipleValueKey(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE, ValueEntries: POINTER(win32more.Windows.Wdk.System.Registry.KEY_VALUE_ENTRY), EntryCount: UInt32, ValueBuffer: VoidPtr, BufferLength: POINTER(UInt32), RequiredBufferLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtRenameKey(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE, NewName: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtSetInformationKey(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE, KeySetInformationClass: win32more.Windows.Wdk.System.Registry.KEY_SET_INFORMATION_CLASS, KeySetInformation: VoidPtr, KeySetInformationLength: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtCreateKey(KeyHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES), TitleIndex: UInt32, Class: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING), CreateOptions: UInt32, Disposition: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtCreateKeyTransacted(KeyHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES), TitleIndex: UInt32, Class: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING), CreateOptions: UInt32, TransactionHandle: win32more.Windows.Win32.Foundation.HANDLE, Disposition: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtCreateRegistryTransaction(TransactionHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES), CreateOptions: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtCommitRegistryTransaction(TransactionHandle: win32more.Windows.Win32.Foundation.HANDLE, Flags: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtOpenKey(KeyHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtOpenKeyEx(KeyHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES), OpenOptions: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtOpenKeyTransacted(KeyHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES), TransactionHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtOpenKeyTransactedEx(KeyHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES), OpenOptions: UInt32, TransactionHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtDeleteKey(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtDeleteValueKey(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE, ValueName: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtEnumerateKey(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE, Index: UInt32, KeyInformationClass: win32more.Windows.Wdk.System.Registry.KEY_INFORMATION_CLASS, KeyInformation: VoidPtr, Length: UInt32, ResultLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtEnumerateValueKey(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE, Index: UInt32, KeyValueInformationClass: win32more.Windows.Wdk.System.Registry.KEY_VALUE_INFORMATION_CLASS, KeyValueInformation: VoidPtr, Length: UInt32, ResultLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtFlushKey(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtQueryKey(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE, KeyInformationClass: win32more.Windows.Wdk.System.Registry.KEY_INFORMATION_CLASS, KeyInformation: VoidPtr, Length: UInt32, ResultLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtQueryValueKey(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE, ValueName: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING), KeyValueInformationClass: win32more.Windows.Wdk.System.Registry.KEY_VALUE_INFORMATION_CLASS, KeyValueInformation: VoidPtr, Length: UInt32, ResultLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtSaveKey(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE, FileHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtSaveKeyEx(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE, FileHandle: win32more.Windows.Win32.Foundation.HANDLE, Format: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtRestoreKey(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE, FileHandle: win32more.Windows.Win32.Foundation.HANDLE, Flags: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtSetValueKey(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE, ValueName: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING), TitleIndex: UInt32, Type: UInt32, Data: VoidPtr, DataSize: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwOpenRegistryTransaction(TransactionHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwRollbackRegistryTransaction(TransactionHandle: win32more.Windows.Win32.Foundation.HANDLE, Flags: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwCreateKey(KeyHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES), TitleIndex: UInt32, Class: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING), CreateOptions: UInt32, Disposition: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwCreateKeyTransacted(KeyHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES), TitleIndex: UInt32, Class: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING), CreateOptions: UInt32, TransactionHandle: win32more.Windows.Win32.Foundation.HANDLE, Disposition: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwCreateRegistryTransaction(TransactionHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES), CreateOptions: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtOpenRegistryTransaction(TransactionHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwCommitRegistryTransaction(TransactionHandle: win32more.Windows.Win32.Foundation.HANDLE, Flags: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtRollbackRegistryTransaction(TransactionHandle: win32more.Windows.Win32.Foundation.HANDLE, Flags: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwOpenKey(KeyHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwOpenKeyEx(KeyHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES), OpenOptions: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwOpenKeyTransacted(KeyHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES), TransactionHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwOpenKeyTransactedEx(KeyHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), DesiredAccess: UInt32, ObjectAttributes: POINTER(win32more.Windows.Wdk.Foundation.OBJECT_ATTRIBUTES), OpenOptions: UInt32, TransactionHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwDeleteKey(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwDeleteValueKey(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE, ValueName: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwEnumerateKey(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE, Index: UInt32, KeyInformationClass: win32more.Windows.Wdk.System.Registry.KEY_INFORMATION_CLASS, KeyInformation: VoidPtr, Length: UInt32, ResultLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwEnumerateValueKey(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE, Index: UInt32, KeyValueInformationClass: win32more.Windows.Wdk.System.Registry.KEY_VALUE_INFORMATION_CLASS, KeyValueInformation: VoidPtr, Length: UInt32, ResultLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwFlushKey(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwQueryKey(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE, KeyInformationClass: win32more.Windows.Wdk.System.Registry.KEY_INFORMATION_CLASS, KeyInformation: VoidPtr, Length: UInt32, ResultLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwQueryValueKey(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE, ValueName: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING), KeyValueInformationClass: win32more.Windows.Wdk.System.Registry.KEY_VALUE_INFORMATION_CLASS, KeyValueInformation: VoidPtr, Length: UInt32, ResultLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwRenameKey(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE, NewName: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwSaveKey(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE, FileHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwSaveKeyEx(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE, FileHandle: win32more.Windows.Win32.Foundation.HANDLE, Format: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwRestoreKey(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE, FileHandle: win32more.Windows.Win32.Foundation.HANDLE, Flags: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwSetInformationKey(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE, KeySetInformationClass: win32more.Windows.Wdk.System.Registry.KEY_SET_INFORMATION_CLASS, KeySetInformation: VoidPtr, KeySetInformationLength: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def ZwSetValueKey(KeyHandle: win32more.Windows.Win32.Foundation.HANDLE, ValueName: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING), TitleIndex: UInt32, Type: UInt32, Data: VoidPtr, DataSize: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
KEY_INFORMATION_CLASS = Int32
KeyBasicInformation: win32more.Windows.Wdk.System.Registry.KEY_INFORMATION_CLASS = 0
KeyNodeInformation: win32more.Windows.Wdk.System.Registry.KEY_INFORMATION_CLASS = 1
KeyFullInformation: win32more.Windows.Wdk.System.Registry.KEY_INFORMATION_CLASS = 2
KeyNameInformation: win32more.Windows.Wdk.System.Registry.KEY_INFORMATION_CLASS = 3
KeyCachedInformation: win32more.Windows.Wdk.System.Registry.KEY_INFORMATION_CLASS = 4
KeyFlagsInformation: win32more.Windows.Wdk.System.Registry.KEY_INFORMATION_CLASS = 5
KeyVirtualizationInformation: win32more.Windows.Wdk.System.Registry.KEY_INFORMATION_CLASS = 6
KeyHandleTagsInformation: win32more.Windows.Wdk.System.Registry.KEY_INFORMATION_CLASS = 7
KeyTrustInformation: win32more.Windows.Wdk.System.Registry.KEY_INFORMATION_CLASS = 8
KeyLayerInformation: win32more.Windows.Wdk.System.Registry.KEY_INFORMATION_CLASS = 9
MaxKeyInfoClass: win32more.Windows.Wdk.System.Registry.KEY_INFORMATION_CLASS = 10
KEY_SET_INFORMATION_CLASS = Int32
KeyWriteTimeInformation: win32more.Windows.Wdk.System.Registry.KEY_SET_INFORMATION_CLASS = 0
KeyWow64FlagsInformation: win32more.Windows.Wdk.System.Registry.KEY_SET_INFORMATION_CLASS = 1
KeyControlFlagsInformation: win32more.Windows.Wdk.System.Registry.KEY_SET_INFORMATION_CLASS = 2
KeySetVirtualizationInformation: win32more.Windows.Wdk.System.Registry.KEY_SET_INFORMATION_CLASS = 3
KeySetDebugInformation: win32more.Windows.Wdk.System.Registry.KEY_SET_INFORMATION_CLASS = 4
KeySetHandleTagsInformation: win32more.Windows.Wdk.System.Registry.KEY_SET_INFORMATION_CLASS = 5
KeySetLayerInformation: win32more.Windows.Wdk.System.Registry.KEY_SET_INFORMATION_CLASS = 6
MaxKeySetInfoClass: win32more.Windows.Wdk.System.Registry.KEY_SET_INFORMATION_CLASS = 7
class KEY_VALUE_ENTRY(Structure):
    ValueName: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING)
    DataLength: UInt32
    DataOffset: UInt32
    Type: UInt32
KEY_VALUE_INFORMATION_CLASS = Int32
KeyValueBasicInformation: win32more.Windows.Wdk.System.Registry.KEY_VALUE_INFORMATION_CLASS = 0
KeyValueFullInformation: win32more.Windows.Wdk.System.Registry.KEY_VALUE_INFORMATION_CLASS = 1
KeyValuePartialInformation: win32more.Windows.Wdk.System.Registry.KEY_VALUE_INFORMATION_CLASS = 2
KeyValueFullInformationAlign64: win32more.Windows.Wdk.System.Registry.KEY_VALUE_INFORMATION_CLASS = 3
KeyValuePartialInformationAlign64: win32more.Windows.Wdk.System.Registry.KEY_VALUE_INFORMATION_CLASS = 4
KeyValueLayerInformation: win32more.Windows.Wdk.System.Registry.KEY_VALUE_INFORMATION_CLASS = 5
MaxKeyValueInfoClass: win32more.Windows.Wdk.System.Registry.KEY_VALUE_INFORMATION_CLASS = 6
class REG_ENUMERATE_KEY_INFORMATION(Structure):
    Object: VoidPtr
    Index: UInt32
    KeyInformationClass: win32more.Windows.Wdk.System.Registry.KEY_INFORMATION_CLASS
    KeyInformation: VoidPtr
    Length: UInt32
    ResultLength: POINTER(UInt32)
    CallContext: VoidPtr
    ObjectContext: VoidPtr
    Reserved: VoidPtr
class REG_ENUMERATE_VALUE_KEY_INFORMATION(Structure):
    Object: VoidPtr
    Index: UInt32
    KeyValueInformationClass: win32more.Windows.Wdk.System.Registry.KEY_VALUE_INFORMATION_CLASS
    KeyValueInformation: VoidPtr
    Length: UInt32
    ResultLength: POINTER(UInt32)
    CallContext: VoidPtr
    ObjectContext: VoidPtr
    Reserved: VoidPtr
class REG_QUERY_KEY_INFORMATION(Structure):
    Object: VoidPtr
    KeyInformationClass: win32more.Windows.Wdk.System.Registry.KEY_INFORMATION_CLASS
    KeyInformation: VoidPtr
    Length: UInt32
    ResultLength: POINTER(UInt32)
    CallContext: VoidPtr
    ObjectContext: VoidPtr
    Reserved: VoidPtr
class REG_QUERY_MULTIPLE_VALUE_KEY_INFORMATION(Structure):
    Object: VoidPtr
    ValueEntries: POINTER(win32more.Windows.Wdk.System.Registry.KEY_VALUE_ENTRY)
    EntryCount: UInt32
    ValueBuffer: VoidPtr
    BufferLength: POINTER(UInt32)
    RequiredBufferLength: POINTER(UInt32)
    CallContext: VoidPtr
    ObjectContext: VoidPtr
    Reserved: VoidPtr
class REG_QUERY_VALUE_KEY_INFORMATION(Structure):
    Object: VoidPtr
    ValueName: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING)
    KeyValueInformationClass: win32more.Windows.Wdk.System.Registry.KEY_VALUE_INFORMATION_CLASS
    KeyValueInformation: VoidPtr
    Length: UInt32
    ResultLength: POINTER(UInt32)
    CallContext: VoidPtr
    ObjectContext: VoidPtr
    Reserved: VoidPtr
class REG_SET_INFORMATION_KEY_INFORMATION(Structure):
    Object: VoidPtr
    KeySetInformationClass: win32more.Windows.Wdk.System.Registry.KEY_SET_INFORMATION_CLASS
    KeySetInformation: VoidPtr
    KeySetInformationLength: UInt32
    CallContext: VoidPtr
    ObjectContext: VoidPtr
    Reserved: VoidPtr


make_ready(__name__)
