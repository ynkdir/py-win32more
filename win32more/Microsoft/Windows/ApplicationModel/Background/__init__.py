from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.Windows.ApplicationModel.Background
import win32more.Windows.ApplicationModel.Background
import win32more.Windows.Win32.System.WinRT
class BackgroundTaskBuilder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.ApplicationModel.Background.IBackgroundTaskBuilder
    _classid_ = 'Microsoft.Windows.ApplicationModel.Background.BackgroundTaskBuilder'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.Windows.ApplicationModel.Background.BackgroundTaskBuilder.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.Windows.ApplicationModel.Background.BackgroundTaskBuilder: ...
    @winrt_mixinmethod
    def SetTrigger(self: win32more.Microsoft.Windows.ApplicationModel.Background.IBackgroundTaskBuilder, trigger: win32more.Windows.ApplicationModel.Background.IBackgroundTrigger) -> Void: ...
    @winrt_mixinmethod
    def SetTaskEntryPointClsid(self: win32more.Microsoft.Windows.ApplicationModel.Background.IBackgroundTaskBuilder, clsId: Guid) -> Void: ...
    @winrt_mixinmethod
    def AddCondition(self: win32more.Microsoft.Windows.ApplicationModel.Background.IBackgroundTaskBuilder, condition: win32more.Windows.ApplicationModel.Background.IBackgroundCondition) -> Void: ...
    @winrt_mixinmethod
    def put_Name(self: win32more.Microsoft.Windows.ApplicationModel.Background.IBackgroundTaskBuilder, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Microsoft.Windows.ApplicationModel.Background.IBackgroundTaskBuilder) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TaskGroup(self: win32more.Microsoft.Windows.ApplicationModel.Background.IBackgroundTaskBuilder, value: win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup) -> Void: ...
    @winrt_mixinmethod
    def get_TaskGroup(self: win32more.Microsoft.Windows.ApplicationModel.Background.IBackgroundTaskBuilder) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup: ...
    @winrt_mixinmethod
    def Register(self: win32more.Microsoft.Windows.ApplicationModel.Background.IBackgroundTaskBuilder) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistration: ...
    @winrt_mixinmethod
    def Register2(self: win32more.Microsoft.Windows.ApplicationModel.Background.IBackgroundTaskBuilder, name: WinRT_String) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistration: ...
    Name = property(get_Name, put_Name)
    TaskGroup = property(get_TaskGroup, put_TaskGroup)
BackgroundTaskContract: UInt32 = 65536
class IBackgroundTaskBuilder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.Background.IBackgroundTaskBuilder'
    _iid_ = Guid('{32a355a0-75ca-5cb8-9f8e-2c4ea62d1ee3}')
    @winrt_commethod(6)
    def SetTrigger(self, trigger: win32more.Windows.ApplicationModel.Background.IBackgroundTrigger) -> Void: ...
    @winrt_commethod(7)
    def SetTaskEntryPointClsid(self, clsId: Guid) -> Void: ...
    @winrt_commethod(8)
    def AddCondition(self, condition: win32more.Windows.ApplicationModel.Background.IBackgroundCondition) -> Void: ...
    @winrt_commethod(9)
    def put_Name(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_TaskGroup(self, value: win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup) -> Void: ...
    @winrt_commethod(12)
    def get_TaskGroup(self) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistrationGroup: ...
    @winrt_commethod(13)
    def Register(self) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistration: ...
    @winrt_commethod(14)
    def Register2(self, name: WinRT_String) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistration: ...
    Name = property(get_Name, put_Name)
    TaskGroup = property(get_TaskGroup, put_TaskGroup)


make_ready(__name__)
