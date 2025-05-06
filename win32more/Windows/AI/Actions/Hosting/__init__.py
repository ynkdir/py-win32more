from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, FlexibleArray, Guid, Int16, Int32, Int64, IntPtr, NativeBitfieldAttribute, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.AI.Actions
import win32more.Windows.AI.Actions.Hosting
import win32more.Windows.Foundation
import win32more.Windows.Win32.System.WinRT
class ActionCatalog(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.Actions.Hosting.IActionCatalog
    _classid_ = 'Windows.AI.Actions.Hosting.ActionCatalog'
    @winrt_mixinmethod
    def GetAllActions(self: win32more.Windows.AI.Actions.Hosting.IActionCatalog) -> ReceiveArray[win32more.Windows.AI.Actions.Hosting.ActionDefinition]: ...
    @winrt_mixinmethod
    def add_Changed(self: win32more.Windows.AI.Actions.Hosting.IActionCatalog, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.AI.Actions.Hosting.ActionCatalog, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Changed(self: win32more.Windows.AI.Actions.Hosting.IActionCatalog, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Changed = event()
class ActionDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.Actions.Hosting.IActionDefinition
    _classid_ = 'Windows.AI.Actions.Hosting.ActionDefinition'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.AI.Actions.Hosting.IActionDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.AI.Actions.Hosting.IActionDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IconFullPath(self: win32more.Windows.AI.Actions.Hosting.IActionDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PackageFamilyName(self: win32more.Windows.AI.Actions.Hosting.IActionDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetInputs(self: win32more.Windows.AI.Actions.Hosting.IActionDefinition) -> ReceiveArray[win32more.Windows.AI.Actions.Hosting.ActionEntityRegistrationInfo]: ...
    @winrt_mixinmethod
    def GetOutputs(self: win32more.Windows.AI.Actions.Hosting.IActionDefinition) -> ReceiveArray[win32more.Windows.AI.Actions.Hosting.ActionEntityRegistrationInfo]: ...
    @winrt_mixinmethod
    def GetOverloads(self: win32more.Windows.AI.Actions.Hosting.IActionDefinition) -> ReceiveArray[win32more.Windows.AI.Actions.Hosting.ActionOverload]: ...
    @winrt_mixinmethod
    def get_DisplaysUI(self: win32more.Windows.AI.Actions.Hosting.IActionDefinition2) -> Boolean: ...
    @winrt_mixinmethod
    def get_DisclaimerKind(self: win32more.Windows.AI.Actions.Hosting.IActionDefinition2) -> win32more.Windows.AI.Actions.Hosting.ActionDisclaimerKind: ...
    @winrt_mixinmethod
    def get_SchemaVersion(self: win32more.Windows.AI.Actions.Hosting.IActionDefinition2) -> UInt32: ...
    @winrt_mixinmethod
    def get_PackageRelativeApplicationId(self: win32more.Windows.AI.Actions.Hosting.IActionDefinition2) -> WinRT_String: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Description = property(get_Description, None)
    DisclaimerKind = property(get_DisclaimerKind, None)
    DisplaysUI = property(get_DisplaysUI, None)
    IconFullPath = property(get_IconFullPath, None)
    Id = property(get_Id, None)
    PackageFamilyName = property(get_PackageFamilyName, None)
    PackageRelativeApplicationId = property(get_PackageRelativeApplicationId, None)
    SchemaVersion = property(get_SchemaVersion, None)
class ActionDisclaimerKind(Enum, Int32):
    None_ = 0
    UsesAI = 1
class ActionEntityRegistrationInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.Actions.Hosting.IActionEntityRegistrationInfo
    _classid_ = 'Windows.AI.Actions.Hosting.ActionEntityRegistrationInfo'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.AI.Actions.Hosting.IActionEntityRegistrationInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: win32more.Windows.AI.Actions.Hosting.IActionEntityRegistrationInfo, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.AI.Actions.Hosting.IActionEntityRegistrationInfo) -> win32more.Windows.AI.Actions.ActionEntityKind: ...
    @winrt_mixinmethod
    def put_Kind(self: win32more.Windows.AI.Actions.Hosting.IActionEntityRegistrationInfo, value: win32more.Windows.AI.Actions.ActionEntityKind) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Kind = property(get_Kind, put_Kind)
    Name = property(get_Name, put_Name)
class ActionOverload(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.Actions.Hosting.IActionOverload
    _classid_ = 'Windows.AI.Actions.Hosting.ActionOverload'
    @winrt_mixinmethod
    def get_DescriptionTemplate(self: win32more.Windows.AI.Actions.Hosting.IActionOverload) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetInputs(self: win32more.Windows.AI.Actions.Hosting.IActionOverload) -> ReceiveArray[win32more.Windows.AI.Actions.Hosting.ActionEntityRegistrationInfo]: ...
    @winrt_mixinmethod
    def InvokeAsync(self: win32more.Windows.AI.Actions.Hosting.IActionOverload, context: win32more.Windows.AI.Actions.ActionInvocationContext) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def InvokeFeedbackAsync(self: win32more.Windows.AI.Actions.Hosting.IActionOverload2, context: win32more.Windows.AI.Actions.ActionInvocationContext, feedback: win32more.Windows.AI.Actions.ActionFeedback) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetSupportsFeedback(self: win32more.Windows.AI.Actions.Hosting.IActionOverload2) -> Boolean: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    DescriptionTemplate = property(get_DescriptionTemplate, None)
class IActionCatalog(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.Actions.Hosting.IActionCatalog'
    _iid_ = Guid('{dbe7c537-66ea-5394-9085-4fc19d78375c}')
    @winrt_commethod(6)
    def GetAllActions(self) -> ReceiveArray[win32more.Windows.AI.Actions.Hosting.ActionDefinition]: ...
    @winrt_commethod(7)
    def add_Changed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.AI.Actions.Hosting.ActionCatalog, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Changed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Changed = event()
class IActionDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.Actions.Hosting.IActionDefinition'
    _iid_ = Guid('{fe766add-924d-5231-855e-dac9e82c7e6c}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_IconFullPath(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_PackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def GetInputs(self) -> ReceiveArray[win32more.Windows.AI.Actions.Hosting.ActionEntityRegistrationInfo]: ...
    @winrt_commethod(11)
    def GetOutputs(self) -> ReceiveArray[win32more.Windows.AI.Actions.Hosting.ActionEntityRegistrationInfo]: ...
    @winrt_commethod(12)
    def GetOverloads(self) -> ReceiveArray[win32more.Windows.AI.Actions.Hosting.ActionOverload]: ...
    Description = property(get_Description, None)
    IconFullPath = property(get_IconFullPath, None)
    Id = property(get_Id, None)
    PackageFamilyName = property(get_PackageFamilyName, None)
class IActionDefinition2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.Actions.Hosting.IActionDefinition2'
    _iid_ = Guid('{27283794-8014-5dc5-97e3-be19d3fa1971}')
    @winrt_commethod(6)
    def get_DisplaysUI(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_DisclaimerKind(self) -> win32more.Windows.AI.Actions.Hosting.ActionDisclaimerKind: ...
    @winrt_commethod(8)
    def get_SchemaVersion(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_PackageRelativeApplicationId(self) -> WinRT_String: ...
    DisclaimerKind = property(get_DisclaimerKind, None)
    DisplaysUI = property(get_DisplaysUI, None)
    PackageRelativeApplicationId = property(get_PackageRelativeApplicationId, None)
    SchemaVersion = property(get_SchemaVersion, None)
class IActionEntityRegistrationInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.Actions.Hosting.IActionEntityRegistrationInfo'
    _iid_ = Guid('{c3b92bdb-03c3-5a9e-b049-002fa0405699}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Name(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Kind(self) -> win32more.Windows.AI.Actions.ActionEntityKind: ...
    @winrt_commethod(9)
    def put_Kind(self, value: win32more.Windows.AI.Actions.ActionEntityKind) -> Void: ...
    Kind = property(get_Kind, put_Kind)
    Name = property(get_Name, put_Name)
class IActionOverload(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.Actions.Hosting.IActionOverload'
    _iid_ = Guid('{5d184610-d09d-5375-9849-505c359dca01}')
    @winrt_commethod(6)
    def get_DescriptionTemplate(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetInputs(self) -> ReceiveArray[win32more.Windows.AI.Actions.Hosting.ActionEntityRegistrationInfo]: ...
    @winrt_commethod(8)
    def InvokeAsync(self, context: win32more.Windows.AI.Actions.ActionInvocationContext) -> win32more.Windows.Foundation.IAsyncAction: ...
    DescriptionTemplate = property(get_DescriptionTemplate, None)
class IActionOverload2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.Actions.Hosting.IActionOverload2'
    _iid_ = Guid('{57ec9906-8231-5a9e-929f-bf39e952eb93}')
    @winrt_commethod(6)
    def InvokeFeedbackAsync(self, context: win32more.Windows.AI.Actions.ActionInvocationContext, feedback: win32more.Windows.AI.Actions.ActionFeedback) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def GetSupportsFeedback(self) -> Boolean: ...


make_ready(__name__)
