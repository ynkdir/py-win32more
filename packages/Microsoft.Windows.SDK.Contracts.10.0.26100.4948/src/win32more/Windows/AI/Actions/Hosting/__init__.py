from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.AI.Actions
import win32more.Windows.AI.Actions.Hosting
import win32more.Windows.Foundation
import win32more.Windows.UI
class ActionCatalog(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.Actions.Hosting.IActionCatalog
    _classid_ = 'Windows.AI.Actions.Hosting.ActionCatalog'
    @winrt_mixinmethod
    def GetAllActions(self: win32more.Windows.AI.Actions.Hosting.IActionCatalog) -> ReceiveArray[win32more.Windows.AI.Actions.Hosting.ActionDefinition]: ...
    @winrt_mixinmethod
    def add_Changed(self: win32more.Windows.AI.Actions.Hosting.IActionCatalog, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.AI.Actions.Hosting.ActionCatalog, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Changed(self: win32more.Windows.AI.Actions.Hosting.IActionCatalog, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetActionsForInputs(self: win32more.Windows.AI.Actions.Hosting.IActionCatalog2, inputEntities: PassArray[win32more.Windows.AI.Actions.ActionEntity]) -> ReceiveArray[win32more.Windows.AI.Actions.Hosting.ActionInstance]: ...
    @winrt_mixinmethod
    def GetActionsForInputs2(self: win32more.Windows.AI.Actions.Hosting.IActionCatalog2, inputEntities: PassArray[win32more.Windows.AI.Actions.ActionEntity], invokerWindowId: win32more.Windows.UI.WindowId) -> ReceiveArray[win32more.Windows.AI.Actions.Hosting.ActionInstance]: ...
    @winrt_mixinmethod
    def GetActionsForCurrentApp(self: win32more.Windows.AI.Actions.Hosting.IActionCatalog3) -> ReceiveArray[win32more.Windows.AI.Actions.Hosting.ActionDefinition]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Changed = event()
class ActionDefinition(ComPtr):
    extends: IInspectable
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
    def get_UsesGenerativeAI(self: win32more.Windows.AI.Actions.Hosting.IActionDefinition2) -> Boolean: ...
    @winrt_mixinmethod
    def get_SchemaVersion(self: win32more.Windows.AI.Actions.Hosting.IActionDefinition2) -> UInt32: ...
    @winrt_mixinmethod
    def get_PackageRelativeApplicationId(self: win32more.Windows.AI.Actions.Hosting.IActionDefinition3) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsCurrentlyAvailable(self: win32more.Windows.AI.Actions.Hosting.IActionDefinition4) -> Boolean: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Description = property(get_Description, None)
    DisplaysUI = property(get_DisplaysUI, None)
    IconFullPath = property(get_IconFullPath, None)
    Id = property(get_Id, None)
    IsCurrentlyAvailable = property(get_IsCurrentlyAvailable, None)
    PackageFamilyName = property(get_PackageFamilyName, None)
    PackageRelativeApplicationId = property(get_PackageRelativeApplicationId, None)
    SchemaVersion = property(get_SchemaVersion, None)
    UsesGenerativeAI = property(get_UsesGenerativeAI, None)
class ActionEntityRegistrationInfo(ComPtr):
    extends: IInspectable
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
class ActionInstance(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.AI.Actions.Hosting.IActionInstance
    _classid_ = 'Windows.AI.Actions.Hosting.ActionInstance'
    @winrt_mixinmethod
    def get_DisplayInfo(self: win32more.Windows.AI.Actions.Hosting.IActionInstance) -> win32more.Windows.AI.Actions.Hosting.ActionInstanceDisplayInfo: ...
    @winrt_mixinmethod
    def get_Definition(self: win32more.Windows.AI.Actions.Hosting.IActionInstance) -> win32more.Windows.AI.Actions.Hosting.ActionDefinition: ...
    @winrt_mixinmethod
    def get_Context(self: win32more.Windows.AI.Actions.Hosting.IActionInstance) -> win32more.Windows.AI.Actions.ActionInvocationContext: ...
    @winrt_mixinmethod
    def InvokeAsync(self: win32more.Windows.AI.Actions.Hosting.IActionInstance) -> win32more.Windows.Foundation.IAsyncAction: ...
    Context = property(get_Context, None)
    Definition = property(get_Definition, None)
    DisplayInfo = property(get_DisplayInfo, None)
class ActionInstanceDisplayInfo(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.AI.Actions.Hosting.IActionInstanceDisplayInfo
    _classid_ = 'Windows.AI.Actions.Hosting.ActionInstanceDisplayInfo'
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.AI.Actions.Hosting.IActionInstanceDisplayInfo) -> WinRT_String: ...
    Description = property(get_Description, None)
class ActionOverload(ComPtr):
    extends: IInspectable
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
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.Hosting.IActionCatalog'
    _iid_ = Guid('{dbe7c537-66ea-5394-9085-4fc19d78375c}')
    @winrt_commethod(6)
    def GetAllActions(self) -> ReceiveArray[win32more.Windows.AI.Actions.Hosting.ActionDefinition]: ...
    @winrt_commethod(7)
    def add_Changed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.AI.Actions.Hosting.ActionCatalog, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Changed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Changed = event()
class IActionCatalog2(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.Hosting.IActionCatalog2'
    _iid_ = Guid('{370360b1-a14b-5ea8-b611-b5f70342ba44}')
    @winrt_commethod(6)
    def GetActionsForInputs(self, inputEntities: PassArray[win32more.Windows.AI.Actions.ActionEntity]) -> ReceiveArray[win32more.Windows.AI.Actions.Hosting.ActionInstance]: ...
    @winrt_commethod(7)
    def GetActionsForInputs2(self, inputEntities: PassArray[win32more.Windows.AI.Actions.ActionEntity], invokerWindowId: win32more.Windows.UI.WindowId) -> ReceiveArray[win32more.Windows.AI.Actions.Hosting.ActionInstance]: ...
class IActionCatalog3(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.Hosting.IActionCatalog3'
    _iid_ = Guid('{2e05d518-8680-55d3-820d-2605adb7d62d}')
    @winrt_commethod(6)
    def GetActionsForCurrentApp(self) -> ReceiveArray[win32more.Windows.AI.Actions.Hosting.ActionDefinition]: ...
class IActionDefinition(ComPtr):
    extends: IInspectable
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
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.Hosting.IActionDefinition2'
    _iid_ = Guid('{c1f44733-f563-54e2-bd2b-dc4c732054cf}')
    @winrt_commethod(6)
    def get_DisplaysUI(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_UsesGenerativeAI(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_SchemaVersion(self) -> UInt32: ...
    DisplaysUI = property(get_DisplaysUI, None)
    SchemaVersion = property(get_SchemaVersion, None)
    UsesGenerativeAI = property(get_UsesGenerativeAI, None)
class IActionDefinition3(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.Hosting.IActionDefinition3'
    _iid_ = Guid('{89c9a7e0-4bfd-55f4-9eed-dce2250114fa}')
    @winrt_commethod(6)
    def get_PackageRelativeApplicationId(self) -> WinRT_String: ...
    PackageRelativeApplicationId = property(get_PackageRelativeApplicationId, None)
class IActionDefinition4(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.Hosting.IActionDefinition4'
    _iid_ = Guid('{6dd91071-8847-55b6-9518-9ff8de421eb7}')
    @winrt_commethod(6)
    def get_IsCurrentlyAvailable(self) -> Boolean: ...
    IsCurrentlyAvailable = property(get_IsCurrentlyAvailable, None)
class IActionEntityRegistrationInfo(ComPtr):
    extends: IInspectable
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
class IActionInstance(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.Hosting.IActionInstance'
    _iid_ = Guid('{809bcb6e-e6ef-5f16-b89a-06b8893df20e}')
    @winrt_commethod(6)
    def get_DisplayInfo(self) -> win32more.Windows.AI.Actions.Hosting.ActionInstanceDisplayInfo: ...
    @winrt_commethod(7)
    def get_Definition(self) -> win32more.Windows.AI.Actions.Hosting.ActionDefinition: ...
    @winrt_commethod(8)
    def get_Context(self) -> win32more.Windows.AI.Actions.ActionInvocationContext: ...
    @winrt_commethod(9)
    def InvokeAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    Context = property(get_Context, None)
    Definition = property(get_Definition, None)
    DisplayInfo = property(get_DisplayInfo, None)
class IActionInstanceDisplayInfo(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.Hosting.IActionInstanceDisplayInfo'
    _iid_ = Guid('{fcfdce21-678b-5602-b9dc-2f4533a6f4b2}')
    @winrt_commethod(6)
    def get_Description(self) -> WinRT_String: ...
    Description = property(get_Description, None)
class IActionOverload(ComPtr):
    extends: IInspectable
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
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.Hosting.IActionOverload2'
    _iid_ = Guid('{57ec9906-8231-5a9e-929f-bf39e952eb93}')
    @winrt_commethod(6)
    def InvokeFeedbackAsync(self, context: win32more.Windows.AI.Actions.ActionInvocationContext, feedback: win32more.Windows.AI.Actions.ActionFeedback) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def GetSupportsFeedback(self) -> Boolean: ...


make_ready(__name__)
