from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Management.Workplace
import win32more.Windows.Win32.System.WinRT
class IMdmAllowPolicyStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Workplace.IMdmAllowPolicyStatics'
    _iid_ = Guid('{c39709e7-741c-41f2-a4b6-314c31502586}')
    @winrt_commethod(6)
    def IsBrowserAllowed(self) -> Boolean: ...
    @winrt_commethod(7)
    def IsCameraAllowed(self) -> Boolean: ...
    @winrt_commethod(8)
    def IsMicrosoftAccountAllowed(self) -> Boolean: ...
    @winrt_commethod(9)
    def IsStoreAllowed(self) -> Boolean: ...
class IMdmPolicyStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Workplace.IMdmPolicyStatics2'
    _iid_ = Guid('{c99c7526-03d4-49f9-a993-43efccd265c4}')
    @winrt_commethod(6)
    def GetMessagingSyncPolicy(self) -> win32more.Windows.Management.Workplace.MessagingSyncPolicy: ...
class IWorkplaceSettingsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Workplace.IWorkplaceSettingsStatics'
    _iid_ = Guid('{e4676ffd-2d92-4c08-bad4-f6590b54a6d3}')
    @winrt_commethod(6)
    def get_IsMicrosoftAccountOptional(self) -> Boolean: ...
    IsMicrosoftAccountOptional = property(get_IsMicrosoftAccountOptional, None)
class MdmPolicy(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Workplace.MdmPolicy'
    @winrt_classmethod
    def GetMessagingSyncPolicy(cls: win32more.Windows.Management.Workplace.IMdmPolicyStatics2) -> win32more.Windows.Management.Workplace.MessagingSyncPolicy: ...
    @winrt_classmethod
    def IsBrowserAllowed(cls: win32more.Windows.Management.Workplace.IMdmAllowPolicyStatics) -> Boolean: ...
    @winrt_classmethod
    def IsCameraAllowed(cls: win32more.Windows.Management.Workplace.IMdmAllowPolicyStatics) -> Boolean: ...
    @winrt_classmethod
    def IsMicrosoftAccountAllowed(cls: win32more.Windows.Management.Workplace.IMdmAllowPolicyStatics) -> Boolean: ...
    @winrt_classmethod
    def IsStoreAllowed(cls: win32more.Windows.Management.Workplace.IMdmAllowPolicyStatics) -> Boolean: ...
class MessagingSyncPolicy(Enum, Int32):
    Disallowed = 0
    Allowed = 1
    Required = 2
class _WorkplaceSettings_Meta_(ComPtr.__class__):
    pass
class WorkplaceSettings(ComPtr, metaclass=_WorkplaceSettings_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Workplace.WorkplaceSettings'
    @winrt_classmethod
    def get_IsMicrosoftAccountOptional(cls: win32more.Windows.Management.Workplace.IWorkplaceSettingsStatics) -> Boolean: ...
    _WorkplaceSettings_Meta_.IsMicrosoftAccountOptional = property(get_IsMicrosoftAccountOptional, None)
WorkplaceSettingsContract: UInt32 = 65536


make_ready(__name__)
