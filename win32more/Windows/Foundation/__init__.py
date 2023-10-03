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
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AsyncActionCompletedHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a4ed5c81-76c9-40bd-8be6-b1d90fb20ae7}')
    def Invoke(self, asyncInfo: win32more.Windows.Foundation.IAsyncAction, asyncStatus: win32more.Windows.Foundation.AsyncStatus) -> Void: ...
class AsyncActionProgressHandler(Generic[TProgress], MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6d844858-0cff-4590-ae89-95a5a5c8b4b8}')
    def Invoke(self, asyncInfo: win32more.Windows.Foundation.IAsyncActionWithProgress[TProgress], progressInfo: TProgress) -> Void: ...
class AsyncActionWithProgressCompletedHandler(Generic[TProgress], MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9c029f91-cc84-44fd-ac26-0a6c4e555281}')
    def Invoke(self, asyncInfo: win32more.Windows.Foundation.IAsyncActionWithProgress[TProgress], asyncStatus: win32more.Windows.Foundation.AsyncStatus) -> Void: ...
class AsyncOperationCompletedHandler(Generic[TResult], MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fcdcf02c-e5d8-4478-915a-4d90b74b83a5}')
    def Invoke(self, asyncInfo: win32more.Windows.Foundation.IAsyncOperation[TResult], asyncStatus: win32more.Windows.Foundation.AsyncStatus) -> Void: ...
class AsyncOperationProgressHandler(Generic[TResult, TProgress], MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{55690902-0aab-421a-8778-f8ce5026d758}')
    def Invoke(self, asyncInfo: win32more.Windows.Foundation.IAsyncOperationWithProgress[TResult, TProgress], progressInfo: TProgress) -> Void: ...
class AsyncOperationWithProgressCompletedHandler(Generic[TResult, TProgress], MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e85df41d-6aa7-46e3-a8e2-f009d840c627}')
    def Invoke(self, asyncInfo: win32more.Windows.Foundation.IAsyncOperationWithProgress[TResult, TProgress], asyncStatus: win32more.Windows.Foundation.AsyncStatus) -> Void: ...
AsyncStatus = Int32
AsyncStatus_Canceled: AsyncStatus = 2
AsyncStatus_Completed: AsyncStatus = 1
AsyncStatus_Error: AsyncStatus = 3
AsyncStatus_Started: AsyncStatus = 0
class DateTime(EasyCastStructure):
    UniversalTime: Int64
class Deferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Foundation.IDeferral
    _classid_ = 'Windows.Foundation.Deferral'
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Foundation.IDeferralFactory, handler: win32more.Windows.Foundation.DeferralCompletedHandler) -> win32more.Windows.Foundation.Deferral: ...
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.Foundation.IDeferral) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
class DeferralCompletedHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ed32a372-f3c8-4faa-9cfb-470148da3888}')
    def Invoke(self) -> Void: ...
class EventHandler(Generic[T], MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9de1c535-6ae1-11e0-84e1-18a905bcc53f}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable_head, args: T) -> Void: ...
class EventRegistrationToken(EasyCastStructure):
    Value: Int64
FoundationContract: UInt32 = 262144
class _GuidHelper_Meta_(ComPtr.__class__):
    pass
class GuidHelper(ComPtr, metaclass=_GuidHelper_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.GuidHelper'
    @winrt_classmethod
    def CreateNewGuid(cls: win32more.Windows.Foundation.IGuidHelperStatics) -> Guid: ...
    @winrt_classmethod
    def get_Empty(cls: win32more.Windows.Foundation.IGuidHelperStatics) -> Guid: ...
    @winrt_classmethod
    def Equals(cls: win32more.Windows.Foundation.IGuidHelperStatics, target: POINTER(Guid), value: POINTER(Guid)) -> Boolean: ...
    _GuidHelper_Meta_.Empty = property(get_Empty.__wrapped__, None)
class HResult(EasyCastStructure):
    Value: Int32
class IAsyncAction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.IAsyncAction'
    _iid_ = Guid('{5a648006-843a-4da9-865b-9d26e5dfad7b}')
    @winrt_commethod(6)
    def put_Completed(self, handler: win32more.Windows.Foundation.AsyncActionCompletedHandler) -> Void: ...
    @winrt_commethod(7)
    def get_Completed(self) -> win32more.Windows.Foundation.AsyncActionCompletedHandler: ...
    @winrt_commethod(8)
    def GetResults(self) -> Void: ...
    Completed = property(get_Completed, put_Completed)
    def __await__(self):
        from win32more._winrt import IAsyncAction___await__
        return IAsyncAction___await__(self)
class IAsyncActionWithProgress(Generic[TProgress], ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.IAsyncActionWithProgress'
    _iid_ = Guid('{1f6db258-e803-48a1-9546-eb7353398884}')
    @winrt_commethod(6)
    def put_Progress(self, handler: win32more.Windows.Foundation.AsyncActionProgressHandler[TProgress]) -> Void: ...
    @winrt_commethod(7)
    def get_Progress(self) -> win32more.Windows.Foundation.AsyncActionProgressHandler[TProgress]: ...
    @winrt_commethod(8)
    def put_Completed(self, handler: win32more.Windows.Foundation.AsyncActionWithProgressCompletedHandler[TProgress]) -> Void: ...
    @winrt_commethod(9)
    def get_Completed(self) -> win32more.Windows.Foundation.AsyncActionWithProgressCompletedHandler[TProgress]: ...
    @winrt_commethod(10)
    def GetResults(self) -> Void: ...
    Progress = property(get_Progress, put_Progress)
    Completed = property(get_Completed, put_Completed)
    def __await__(self):
        from win32more._winrt import IAsyncAction___await__
        return IAsyncAction___await__(self)
class IAsyncInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.IAsyncInfo'
    _iid_ = Guid('{00000036-0000-0000-c000-000000000046}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Windows.Foundation.AsyncStatus: ...
    @winrt_commethod(8)
    def get_ErrorCode(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(9)
    def Cancel(self) -> Void: ...
    @winrt_commethod(10)
    def Close(self) -> Void: ...
    Id = property(get_Id, None)
    Status = property(get_Status, None)
    ErrorCode = property(get_ErrorCode, None)
class IAsyncOperationWithProgress(Generic[TResult, TProgress], ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.IAsyncOperationWithProgress'
    _iid_ = Guid('{b5d036d7-e297-498f-ba60-0289e76e23dd}')
    @winrt_commethod(6)
    def put_Progress(self, handler: win32more.Windows.Foundation.AsyncOperationProgressHandler[TResult, TProgress]) -> Void: ...
    @winrt_commethod(7)
    def get_Progress(self) -> win32more.Windows.Foundation.AsyncOperationProgressHandler[TResult, TProgress]: ...
    @winrt_commethod(8)
    def put_Completed(self, handler: win32more.Windows.Foundation.AsyncOperationWithProgressCompletedHandler[TResult, TProgress]) -> Void: ...
    @winrt_commethod(9)
    def get_Completed(self) -> win32more.Windows.Foundation.AsyncOperationWithProgressCompletedHandler[TResult, TProgress]: ...
    @winrt_commethod(10)
    def GetResults(self) -> TResult: ...
    Progress = property(get_Progress, put_Progress)
    Completed = property(get_Completed, put_Completed)
    def __await__(self):
        from win32more._winrt import IAsyncOperation___await__
        return IAsyncOperation___await__(self)
class IAsyncOperation(Generic[TResult], ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.IAsyncOperation'
    _iid_ = Guid('{9fc2b0bb-e446-44e2-aa61-9cab8f636af2}')
    @winrt_commethod(6)
    def put_Completed(self, handler: win32more.Windows.Foundation.AsyncOperationCompletedHandler[TResult]) -> Void: ...
    @winrt_commethod(7)
    def get_Completed(self) -> win32more.Windows.Foundation.AsyncOperationCompletedHandler[TResult]: ...
    @winrt_commethod(8)
    def GetResults(self) -> TResult: ...
    Completed = property(get_Completed, put_Completed)
    def __await__(self):
        from win32more._winrt import IAsyncOperation___await__
        return IAsyncOperation___await__(self)
class IClosable(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.IClosable'
    _iid_ = Guid('{30d5a829-7fa4-4026-83bb-d75bae4ea99e}')
    @winrt_commethod(6)
    def Close(self) -> Void: ...
class IDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.IDeferral'
    _iid_ = Guid('{d6269732-3b7f-46a7-b40b-4fdca2a2c693}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IDeferralFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.IDeferralFactory'
    _iid_ = Guid('{65a1ecc5-3fb5-4832-8ca9-f061b281d13a}')
    @winrt_commethod(6)
    def Create(self, handler: win32more.Windows.Foundation.DeferralCompletedHandler) -> win32more.Windows.Foundation.Deferral: ...
class IGetActivationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.IGetActivationFactory'
    _iid_ = Guid('{4edb8ee2-96dd-49a7-94f7-4607ddab8e3c}')
    @winrt_commethod(6)
    def GetActivationFactory(self, activatableClassId: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
class IGuidHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.IGuidHelperStatics'
    _iid_ = Guid('{59c7966b-ae52-5283-ad7f-a1b9e9678add}')
    @winrt_commethod(6)
    def CreateNewGuid(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Empty(self) -> Guid: ...
    @winrt_commethod(8)
    def Equals(self, target: POINTER(Guid), value: POINTER(Guid)) -> Boolean: ...
    Empty = property(get_Empty, None)
class IMemoryBuffer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.IMemoryBuffer'
    _iid_ = Guid('{fbc4dd2a-245b-11e4-af98-689423260cf8}')
    @winrt_commethod(6)
    def CreateReference(self) -> win32more.Windows.Foundation.IMemoryBufferReference: ...
class IMemoryBufferFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.IMemoryBufferFactory'
    _iid_ = Guid('{fbc4dd2b-245b-11e4-af98-689423260cf8}')
    @winrt_commethod(6)
    def Create(self, capacity: UInt32) -> win32more.Windows.Foundation.MemoryBuffer: ...
class IMemoryBufferReference(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.IMemoryBufferReference'
    _iid_ = Guid('{fbc4dd29-245b-11e4-af98-689423260cf8}')
    @winrt_commethod(6)
    def get_Capacity(self) -> UInt32: ...
    @winrt_commethod(7)
    def add_Closed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Foundation.IMemoryBufferReference, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Closed(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Capacity = property(get_Capacity, None)
class IPropertyValue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.IPropertyValue'
    _iid_ = Guid('{4bd682dd-7554-40e9-9a9b-82654ede7e62}')
    @winrt_commethod(6)
    def get_Type(self) -> win32more.Windows.Foundation.PropertyType: ...
    @winrt_commethod(7)
    def get_IsNumericScalar(self) -> Boolean: ...
    @winrt_commethod(8)
    def GetUInt8(self) -> Byte: ...
    @winrt_commethod(9)
    def GetInt16(self) -> Int16: ...
    @winrt_commethod(10)
    def GetUInt16(self) -> UInt16: ...
    @winrt_commethod(11)
    def GetInt32(self) -> Int32: ...
    @winrt_commethod(12)
    def GetUInt32(self) -> UInt32: ...
    @winrt_commethod(13)
    def GetInt64(self) -> Int64: ...
    @winrt_commethod(14)
    def GetUInt64(self) -> UInt64: ...
    @winrt_commethod(15)
    def GetSingle(self) -> Single: ...
    @winrt_commethod(16)
    def GetDouble(self) -> Double: ...
    @winrt_commethod(17)
    def GetChar16(self) -> Char: ...
    @winrt_commethod(18)
    def GetBoolean(self) -> Boolean: ...
    @winrt_commethod(19)
    def GetString(self) -> WinRT_String: ...
    @winrt_commethod(20)
    def GetGuid(self) -> Guid: ...
    @winrt_commethod(21)
    def GetDateTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(22)
    def GetTimeSpan(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(23)
    def GetPoint(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(24)
    def GetSize(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(25)
    def GetRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(26)
    def GetUInt8Array(self, value: POINTER(SZArray[Byte])) -> Void: ...
    @winrt_commethod(27)
    def GetInt16Array(self, value: POINTER(SZArray[Int16])) -> Void: ...
    @winrt_commethod(28)
    def GetUInt16Array(self, value: POINTER(SZArray[UInt16])) -> Void: ...
    @winrt_commethod(29)
    def GetInt32Array(self, value: POINTER(SZArray[Int32])) -> Void: ...
    @winrt_commethod(30)
    def GetUInt32Array(self, value: POINTER(SZArray[UInt32])) -> Void: ...
    @winrt_commethod(31)
    def GetInt64Array(self, value: POINTER(SZArray[Int64])) -> Void: ...
    @winrt_commethod(32)
    def GetUInt64Array(self, value: POINTER(SZArray[UInt64])) -> Void: ...
    @winrt_commethod(33)
    def GetSingleArray(self, value: POINTER(SZArray[Single])) -> Void: ...
    @winrt_commethod(34)
    def GetDoubleArray(self, value: POINTER(SZArray[Double])) -> Void: ...
    @winrt_commethod(35)
    def GetChar16Array(self, value: POINTER(SZArray[Char])) -> Void: ...
    @winrt_commethod(36)
    def GetBooleanArray(self, value: POINTER(SZArray[Boolean])) -> Void: ...
    @winrt_commethod(37)
    def GetStringArray(self, value: POINTER(SZArray[WinRT_String])) -> Void: ...
    @winrt_commethod(38)
    def GetInspectableArray(self, value: POINTER(SZArray[win32more.Windows.Win32.System.WinRT.IInspectable_head])) -> Void: ...
    @winrt_commethod(39)
    def GetGuidArray(self, value: POINTER(SZArray[Guid])) -> Void: ...
    @winrt_commethod(40)
    def GetDateTimeArray(self, value: POINTER(SZArray[win32more.Windows.Foundation.DateTime])) -> Void: ...
    @winrt_commethod(41)
    def GetTimeSpanArray(self, value: POINTER(SZArray[win32more.Windows.Foundation.TimeSpan])) -> Void: ...
    @winrt_commethod(42)
    def GetPointArray(self, value: POINTER(SZArray[win32more.Windows.Foundation.Point])) -> Void: ...
    @winrt_commethod(43)
    def GetSizeArray(self, value: POINTER(SZArray[win32more.Windows.Foundation.Size])) -> Void: ...
    @winrt_commethod(44)
    def GetRectArray(self, value: POINTER(SZArray[win32more.Windows.Foundation.Rect])) -> Void: ...
    Type = property(get_Type, None)
    IsNumericScalar = property(get_IsNumericScalar, None)
class IPropertyValueStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.IPropertyValueStatics'
    _iid_ = Guid('{629bdbc8-d932-4ff4-96b9-8d96c5c1e858}')
    @winrt_commethod(6)
    def CreateEmpty(self) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def CreateUInt8(self, value: Byte) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(8)
    def CreateInt16(self, value: Int16) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(9)
    def CreateUInt16(self, value: UInt16) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(10)
    def CreateInt32(self, value: Int32) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(11)
    def CreateUInt32(self, value: UInt32) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(12)
    def CreateInt64(self, value: Int64) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(13)
    def CreateUInt64(self, value: UInt64) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(14)
    def CreateSingle(self, value: Single) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(15)
    def CreateDouble(self, value: Double) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(16)
    def CreateChar16(self, value: Char) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(17)
    def CreateBoolean(self, value: Boolean) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(18)
    def CreateString(self, value: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(19)
    def CreateInspectable(self, value: win32more.Windows.Win32.System.WinRT.IInspectable_head) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(20)
    def CreateGuid(self, value: Guid) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(21)
    def CreateDateTime(self, value: win32more.Windows.Foundation.DateTime) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(22)
    def CreateTimeSpan(self, value: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(23)
    def CreatePoint(self, value: win32more.Windows.Foundation.Point) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(24)
    def CreateSize(self, value: win32more.Windows.Foundation.Size) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(25)
    def CreateRect(self, value: win32more.Windows.Foundation.Rect) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(26)
    def CreateUInt8Array(self, value: Annotated[SZArray[Byte], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(27)
    def CreateInt16Array(self, value: Annotated[SZArray[Int16], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(28)
    def CreateUInt16Array(self, value: Annotated[SZArray[UInt16], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(29)
    def CreateInt32Array(self, value: Annotated[SZArray[Int32], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(30)
    def CreateUInt32Array(self, value: Annotated[SZArray[UInt32], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(31)
    def CreateInt64Array(self, value: Annotated[SZArray[Int64], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(32)
    def CreateUInt64Array(self, value: Annotated[SZArray[UInt64], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(33)
    def CreateSingleArray(self, value: Annotated[SZArray[Single], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(34)
    def CreateDoubleArray(self, value: Annotated[SZArray[Double], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(35)
    def CreateChar16Array(self, value: Annotated[SZArray[Char], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(36)
    def CreateBooleanArray(self, value: Annotated[SZArray[Boolean], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(37)
    def CreateStringArray(self, value: Annotated[SZArray[WinRT_String], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(38)
    def CreateInspectableArray(self, value: Annotated[SZArray[win32more.Windows.Win32.System.WinRT.IInspectable_head], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(39)
    def CreateGuidArray(self, value: Annotated[SZArray[Guid], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(40)
    def CreateDateTimeArray(self, value: Annotated[SZArray[win32more.Windows.Foundation.DateTime], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(41)
    def CreateTimeSpanArray(self, value: Annotated[SZArray[win32more.Windows.Foundation.TimeSpan], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(42)
    def CreatePointArray(self, value: Annotated[SZArray[win32more.Windows.Foundation.Point], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(43)
    def CreateSizeArray(self, value: Annotated[SZArray[win32more.Windows.Foundation.Size], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(44)
    def CreateRectArray(self, value: Annotated[SZArray[win32more.Windows.Foundation.Rect], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
class IReferenceArray(Generic[T], ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.IReferenceArray'
    _iid_ = Guid('{61c17707-2d65-11e0-9ae8-d48564015472}')
    @winrt_commethod(6)
    def get_Value(self) -> SZArray[T]: ...
    Value = property(get_Value, None)
class IReference(Generic[T], ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.IReference'
    _iid_ = Guid('{61c17706-2d65-11e0-9ae8-d48564015472}')
    @winrt_commethod(6)
    def get_Value(self) -> T: ...
    Value = property(get_Value, None)
class IStringable(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.IStringable'
    _iid_ = Guid('{96369f54-8eb6-48f0-abce-c1b211e627c3}')
    @winrt_commethod(6)
    def ToString(self) -> WinRT_String: ...
class IUriEscapeStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.IUriEscapeStatics'
    _iid_ = Guid('{c1d432ba-c824-4452-a7fd-512bc3bbe9a1}')
    @winrt_commethod(6)
    def UnescapeComponent(self, toUnescape: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(7)
    def EscapeComponent(self, toEscape: WinRT_String) -> WinRT_String: ...
class IUriRuntimeClass(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.IUriRuntimeClass'
    _iid_ = Guid('{9e365e57-48b2-4160-956f-c7385120bbfc}')
    @winrt_commethod(6)
    def get_AbsoluteUri(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayUri(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Domain(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Extension(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Fragment(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Host(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_Password(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_Path(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_Query(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_QueryParsed(self) -> win32more.Windows.Foundation.WwwFormUrlDecoder: ...
    @winrt_commethod(16)
    def get_RawUri(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def get_SchemeName(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def get_UserName(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_Port(self) -> Int32: ...
    @winrt_commethod(20)
    def get_Suspicious(self) -> Boolean: ...
    @winrt_commethod(21)
    def Equals(self, pUri: win32more.Windows.Foundation.Uri) -> Boolean: ...
    @winrt_commethod(22)
    def CombineUri(self, relativeUri: WinRT_String) -> win32more.Windows.Foundation.Uri: ...
    AbsoluteUri = property(get_AbsoluteUri, None)
    DisplayUri = property(get_DisplayUri, None)
    Domain = property(get_Domain, None)
    Extension = property(get_Extension, None)
    Fragment = property(get_Fragment, None)
    Host = property(get_Host, None)
    Password = property(get_Password, None)
    Path = property(get_Path, None)
    Query = property(get_Query, None)
    QueryParsed = property(get_QueryParsed, None)
    RawUri = property(get_RawUri, None)
    SchemeName = property(get_SchemeName, None)
    UserName = property(get_UserName, None)
    Port = property(get_Port, None)
    Suspicious = property(get_Suspicious, None)
class IUriRuntimeClassFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.IUriRuntimeClassFactory'
    _iid_ = Guid('{44a9796f-723e-4fdf-a218-033e75b0c084}')
    @winrt_commethod(6)
    def CreateUri(self, uri: WinRT_String) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def CreateWithRelativeUri(self, baseUri: WinRT_String, relativeUri: WinRT_String) -> win32more.Windows.Foundation.Uri: ...
class IUriRuntimeClassWithAbsoluteCanonicalUri(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.IUriRuntimeClassWithAbsoluteCanonicalUri'
    _iid_ = Guid('{758d9661-221c-480f-a339-50656673f46f}')
    @winrt_commethod(6)
    def get_AbsoluteCanonicalUri(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayIri(self) -> WinRT_String: ...
    AbsoluteCanonicalUri = property(get_AbsoluteCanonicalUri, None)
    DisplayIri = property(get_DisplayIri, None)
class IWwwFormUrlDecoderEntry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.IWwwFormUrlDecoderEntry'
    _iid_ = Guid('{125e7431-f678-4e8e-b670-20a9b06c512d}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Value(self) -> WinRT_String: ...
    Name = property(get_Name, None)
    Value = property(get_Value, None)
class IWwwFormUrlDecoderRuntimeClass(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.IWwwFormUrlDecoderRuntimeClass'
    _iid_ = Guid('{d45a0451-f225-4542-9296-0e1df5d254df}')
    @winrt_commethod(6)
    def GetFirstValueByName(self, name: WinRT_String) -> WinRT_String: ...
class IWwwFormUrlDecoderRuntimeClassFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.IWwwFormUrlDecoderRuntimeClassFactory'
    _iid_ = Guid('{5b8c6b3d-24ae-41b5-a1bf-f0c3d544845b}')
    @winrt_commethod(6)
    def CreateWwwFormUrlDecoder(self, query: WinRT_String) -> win32more.Windows.Foundation.WwwFormUrlDecoder: ...
class MemoryBuffer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Foundation.IMemoryBuffer
    _classid_ = 'Windows.Foundation.MemoryBuffer'
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Foundation.IMemoryBufferFactory, capacity: UInt32) -> win32more.Windows.Foundation.MemoryBuffer: ...
    @winrt_mixinmethod
    def CreateReference(self: win32more.Windows.Foundation.IMemoryBuffer) -> win32more.Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
class Point(EasyCastStructure):
    X: Single
    Y: Single
PropertyType = Int32
PropertyType_Empty: PropertyType = 0
PropertyType_UInt8: PropertyType = 1
PropertyType_Int16: PropertyType = 2
PropertyType_UInt16: PropertyType = 3
PropertyType_Int32: PropertyType = 4
PropertyType_UInt32: PropertyType = 5
PropertyType_Int64: PropertyType = 6
PropertyType_UInt64: PropertyType = 7
PropertyType_Single: PropertyType = 8
PropertyType_Double: PropertyType = 9
PropertyType_Char16: PropertyType = 10
PropertyType_Boolean: PropertyType = 11
PropertyType_String: PropertyType = 12
PropertyType_Inspectable: PropertyType = 13
PropertyType_DateTime: PropertyType = 14
PropertyType_TimeSpan: PropertyType = 15
PropertyType_Guid: PropertyType = 16
PropertyType_Point: PropertyType = 17
PropertyType_Size: PropertyType = 18
PropertyType_Rect: PropertyType = 19
PropertyType_OtherType: PropertyType = 20
PropertyType_UInt8Array: PropertyType = 1025
PropertyType_Int16Array: PropertyType = 1026
PropertyType_UInt16Array: PropertyType = 1027
PropertyType_Int32Array: PropertyType = 1028
PropertyType_UInt32Array: PropertyType = 1029
PropertyType_Int64Array: PropertyType = 1030
PropertyType_UInt64Array: PropertyType = 1031
PropertyType_SingleArray: PropertyType = 1032
PropertyType_DoubleArray: PropertyType = 1033
PropertyType_Char16Array: PropertyType = 1034
PropertyType_BooleanArray: PropertyType = 1035
PropertyType_StringArray: PropertyType = 1036
PropertyType_InspectableArray: PropertyType = 1037
PropertyType_DateTimeArray: PropertyType = 1038
PropertyType_TimeSpanArray: PropertyType = 1039
PropertyType_GuidArray: PropertyType = 1040
PropertyType_PointArray: PropertyType = 1041
PropertyType_SizeArray: PropertyType = 1042
PropertyType_RectArray: PropertyType = 1043
PropertyType_OtherTypeArray: PropertyType = 1044
class PropertyValue(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Foundation.PropertyValue'
    @winrt_classmethod
    def CreateEmpty(cls: win32more.Windows.Foundation.IPropertyValueStatics) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateUInt8(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Byte) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateInt16(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Int16) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateUInt16(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: UInt16) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateInt32(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Int32) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateUInt32(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: UInt32) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateInt64(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Int64) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateUInt64(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: UInt64) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateSingle(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Single) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateDouble(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Double) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateChar16(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Char) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateBoolean(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Boolean) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateString(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateInspectable(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: win32more.Windows.Win32.System.WinRT.IInspectable_head) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateGuid(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Guid) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateDateTime(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: win32more.Windows.Foundation.DateTime) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateTimeSpan(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreatePoint(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: win32more.Windows.Foundation.Point) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateSize(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: win32more.Windows.Foundation.Size) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateRect(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: win32more.Windows.Foundation.Rect) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateUInt8Array(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Annotated[SZArray[Byte], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateInt16Array(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Annotated[SZArray[Int16], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateUInt16Array(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Annotated[SZArray[UInt16], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateInt32Array(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Annotated[SZArray[Int32], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateUInt32Array(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Annotated[SZArray[UInt32], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateInt64Array(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Annotated[SZArray[Int64], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateUInt64Array(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Annotated[SZArray[UInt64], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateSingleArray(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Annotated[SZArray[Single], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateDoubleArray(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Annotated[SZArray[Double], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateChar16Array(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Annotated[SZArray[Char], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateBooleanArray(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Annotated[SZArray[Boolean], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateStringArray(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Annotated[SZArray[WinRT_String], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateInspectableArray(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Annotated[SZArray[win32more.Windows.Win32.System.WinRT.IInspectable_head], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateGuidArray(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Annotated[SZArray[Guid], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateDateTimeArray(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Annotated[SZArray[win32more.Windows.Foundation.DateTime], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateTimeSpanArray(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Annotated[SZArray[win32more.Windows.Foundation.TimeSpan], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreatePointArray(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Annotated[SZArray[win32more.Windows.Foundation.Point], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateSizeArray(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Annotated[SZArray[win32more.Windows.Foundation.Size], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def CreateRectArray(cls: win32more.Windows.Foundation.IPropertyValueStatics, value: Annotated[SZArray[win32more.Windows.Foundation.Rect], 'In']) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
class Rect(EasyCastStructure):
    X: Single
    Y: Single
    Width: Single
    Height: Single
class Size(EasyCastStructure):
    Width: Single
    Height: Single
class TimeSpan(EasyCastStructure):
    Duration: Int64
class TypedEventHandler(Generic[TSender, TResult], MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9de1c534-6ae1-11e0-84e1-18a905bcc53f}')
    def Invoke(self, sender: TSender, args: TResult) -> Void: ...
UniversalApiContract: UInt32 = 983040
class Uri(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Foundation.IUriRuntimeClass
    _classid_ = 'Windows.Foundation.Uri'
    @winrt_factorymethod
    def CreateUri(cls: win32more.Windows.Foundation.IUriRuntimeClassFactory, uri: WinRT_String) -> win32more.Windows.Foundation.Uri: ...
    @winrt_factorymethod
    def CreateWithRelativeUri(cls: win32more.Windows.Foundation.IUriRuntimeClassFactory, baseUri: WinRT_String, relativeUri: WinRT_String) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_AbsoluteUri(self: win32more.Windows.Foundation.IUriRuntimeClass) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayUri(self: win32more.Windows.Foundation.IUriRuntimeClass) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Domain(self: win32more.Windows.Foundation.IUriRuntimeClass) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Extension(self: win32more.Windows.Foundation.IUriRuntimeClass) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Fragment(self: win32more.Windows.Foundation.IUriRuntimeClass) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Host(self: win32more.Windows.Foundation.IUriRuntimeClass) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Password(self: win32more.Windows.Foundation.IUriRuntimeClass) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Path(self: win32more.Windows.Foundation.IUriRuntimeClass) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Query(self: win32more.Windows.Foundation.IUriRuntimeClass) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_QueryParsed(self: win32more.Windows.Foundation.IUriRuntimeClass) -> win32more.Windows.Foundation.WwwFormUrlDecoder: ...
    @winrt_mixinmethod
    def get_RawUri(self: win32more.Windows.Foundation.IUriRuntimeClass) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SchemeName(self: win32more.Windows.Foundation.IUriRuntimeClass) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UserName(self: win32more.Windows.Foundation.IUriRuntimeClass) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Port(self: win32more.Windows.Foundation.IUriRuntimeClass) -> Int32: ...
    @winrt_mixinmethod
    def get_Suspicious(self: win32more.Windows.Foundation.IUriRuntimeClass) -> Boolean: ...
    @winrt_mixinmethod
    def Equals(self: win32more.Windows.Foundation.IUriRuntimeClass, pUri: win32more.Windows.Foundation.Uri) -> Boolean: ...
    @winrt_mixinmethod
    def CombineUri(self: win32more.Windows.Foundation.IUriRuntimeClass, relativeUri: WinRT_String) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_AbsoluteCanonicalUri(self: win32more.Windows.Foundation.IUriRuntimeClassWithAbsoluteCanonicalUri) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayIri(self: win32more.Windows.Foundation.IUriRuntimeClassWithAbsoluteCanonicalUri) -> WinRT_String: ...
    @winrt_mixinmethod
    def ToString(self: win32more.Windows.Foundation.IStringable) -> WinRT_String: ...
    @winrt_classmethod
    def UnescapeComponent(cls: win32more.Windows.Foundation.IUriEscapeStatics, toUnescape: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def EscapeComponent(cls: win32more.Windows.Foundation.IUriEscapeStatics, toEscape: WinRT_String) -> WinRT_String: ...
    AbsoluteUri = property(get_AbsoluteUri, None)
    DisplayUri = property(get_DisplayUri, None)
    Domain = property(get_Domain, None)
    Extension = property(get_Extension, None)
    Fragment = property(get_Fragment, None)
    Host = property(get_Host, None)
    Password = property(get_Password, None)
    Path = property(get_Path, None)
    Query = property(get_Query, None)
    QueryParsed = property(get_QueryParsed, None)
    RawUri = property(get_RawUri, None)
    SchemeName = property(get_SchemeName, None)
    UserName = property(get_UserName, None)
    Port = property(get_Port, None)
    Suspicious = property(get_Suspicious, None)
    AbsoluteCanonicalUri = property(get_AbsoluteCanonicalUri, None)
    DisplayIri = property(get_DisplayIri, None)
class WwwFormUrlDecoder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Foundation.IWwwFormUrlDecoderRuntimeClass
    _classid_ = 'Windows.Foundation.WwwFormUrlDecoder'
    @winrt_factorymethod
    def CreateWwwFormUrlDecoder(cls: win32more.Windows.Foundation.IWwwFormUrlDecoderRuntimeClassFactory, query: WinRT_String) -> win32more.Windows.Foundation.WwwFormUrlDecoder: ...
    @winrt_mixinmethod
    def GetFirstValueByName(self: win32more.Windows.Foundation.IWwwFormUrlDecoderRuntimeClass, name: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.IWwwFormUrlDecoderEntry]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.IWwwFormUrlDecoderEntry]: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.IWwwFormUrlDecoderEntry], index: UInt32) -> win32more.Windows.Foundation.IWwwFormUrlDecoderEntry: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.IWwwFormUrlDecoderEntry]) -> UInt32: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.IWwwFormUrlDecoderEntry], value: win32more.Windows.Foundation.IWwwFormUrlDecoderEntry, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.IWwwFormUrlDecoderEntry], startIndex: UInt32, items: Annotated[SZArray[win32more.Windows.Foundation.IWwwFormUrlDecoderEntry], 'Out']) -> UInt32: ...
    Size = property(get_Size, None)
class WwwFormUrlDecoderEntry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Foundation.IWwwFormUrlDecoderEntry
    _classid_ = 'Windows.Foundation.WwwFormUrlDecoderEntry'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Foundation.IWwwFormUrlDecoderEntry) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Foundation.IWwwFormUrlDecoderEntry) -> WinRT_String: ...
    Name = property(get_Name, None)
    Value = property(get_Value, None)
make_head(_module, 'DateTime')
make_head(_module, 'Deferral')
make_head(_module, 'EventRegistrationToken')
make_head(_module, 'GuidHelper')
make_head(_module, 'HResult')
make_head(_module, 'IAsyncAction')
make_head(_module, 'IAsyncActionWithProgress')
make_head(_module, 'IAsyncInfo')
make_head(_module, 'IAsyncOperationWithProgress')
make_head(_module, 'IAsyncOperation')
make_head(_module, 'IClosable')
make_head(_module, 'IDeferral')
make_head(_module, 'IDeferralFactory')
make_head(_module, 'IGetActivationFactory')
make_head(_module, 'IGuidHelperStatics')
make_head(_module, 'IMemoryBuffer')
make_head(_module, 'IMemoryBufferFactory')
make_head(_module, 'IMemoryBufferReference')
make_head(_module, 'IPropertyValue')
make_head(_module, 'IPropertyValueStatics')
make_head(_module, 'IReferenceArray')
make_head(_module, 'IReference')
make_head(_module, 'IStringable')
make_head(_module, 'IUriEscapeStatics')
make_head(_module, 'IUriRuntimeClass')
make_head(_module, 'IUriRuntimeClassFactory')
make_head(_module, 'IUriRuntimeClassWithAbsoluteCanonicalUri')
make_head(_module, 'IWwwFormUrlDecoderEntry')
make_head(_module, 'IWwwFormUrlDecoderRuntimeClass')
make_head(_module, 'IWwwFormUrlDecoderRuntimeClassFactory')
make_head(_module, 'MemoryBuffer')
make_head(_module, 'Point')
make_head(_module, 'PropertyValue')
make_head(_module, 'Rect')
make_head(_module, 'Size')
make_head(_module, 'TimeSpan')
make_head(_module, 'Uri')
make_head(_module, 'WwwFormUrlDecoder')
make_head(_module, 'WwwFormUrlDecoderEntry')