from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.AI.Agents
import win32more.Windows.ApplicationModel
import win32more.Windows.Foundation
class AgentAuthorizationResponse(Enum, Int32):
    Denied = 0
    Approved = 1
class AgentContext(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.AI.Agents.IAgentContext
    _classid_ = 'Windows.AI.Agents.AgentContext'
    @winrt_mixinmethod
    def get_AppUserModelId(self: win32more.Windows.AI.Agents.IAgentContext) -> WinRT_String: ...
    @winrt_mixinmethod
    def RequestResourceAccess(self: win32more.Windows.AI.Agents.IAgentContext, resource: win32more.Windows.Foundation.Uri, description: WinRT_String, reasonForAsking: WinRT_String) -> win32more.Windows.AI.Agents.AgentAuthorizationResponse: ...
    @winrt_classmethod
    def GetContextForCaller(cls: win32more.Windows.AI.Agents.IAgentContextStatics) -> win32more.Windows.AI.Agents.AgentContext: ...
    AppUserModelId = property(get_AppUserModelId, None)
class AgentInfo(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.AI.Agents.IAgentInfo
    _classid_ = 'Windows.AI.Agents.AgentInfo'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.AI.Agents.IAgentInfo) -> Guid: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.AI.Agents.IAgentInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.AI.Agents.IAgentInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetPackage(self: win32more.Windows.AI.Agents.IAgentInfo) -> win32more.Windows.ApplicationModel.Package: ...
    Description = property(get_Description, None)
    Id = property(get_Id, None)
    Name = property(get_Name, None)
class _AgentResources_Meta_(ComPtr.__class__):
    pass
class AgentResources(ComPtr, metaclass=_AgentResources_Meta_):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.AgentResources'
    @winrt_classmethod
    def get_FileSystemRead(cls: win32more.Windows.AI.Agents.IAgentResourcesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_FileSystemWrite(cls: win32more.Windows.AI.Agents.IAgentResourcesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_FileSystemDelete(cls: win32more.Windows.AI.Agents.IAgentResourcesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_FileSystemCreate(cls: win32more.Windows.AI.Agents.IAgentResourcesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HttpGet(cls: win32more.Windows.AI.Agents.IAgentResourcesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HttpPost(cls: win32more.Windows.AI.Agents.IAgentResourcesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HttpPut(cls: win32more.Windows.AI.Agents.IAgentResourcesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HttpDelete(cls: win32more.Windows.AI.Agents.IAgentResourcesStatics) -> WinRT_String: ...
    _AgentResources_Meta_.FileSystemCreate = property(get_FileSystemCreate, None)
    _AgentResources_Meta_.FileSystemDelete = property(get_FileSystemDelete, None)
    _AgentResources_Meta_.FileSystemRead = property(get_FileSystemRead, None)
    _AgentResources_Meta_.FileSystemWrite = property(get_FileSystemWrite, None)
    _AgentResources_Meta_.HttpDelete = property(get_HttpDelete, None)
    _AgentResources_Meta_.HttpGet = property(get_HttpGet, None)
    _AgentResources_Meta_.HttpPost = property(get_HttpPost, None)
    _AgentResources_Meta_.HttpPut = property(get_HttpPut, None)
AgentsContract: UInt32 = 65536
class IAgentContext(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.IAgentContext'
    _iid_ = Guid('{67812fd9-f5fc-5431-b282-2fc753b0c2cd}')
    @winrt_commethod(6)
    def get_AppUserModelId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def RequestResourceAccess(self, resource: win32more.Windows.Foundation.Uri, description: WinRT_String, reasonForAsking: WinRT_String) -> win32more.Windows.AI.Agents.AgentAuthorizationResponse: ...
    AppUserModelId = property(get_AppUserModelId, None)
class IAgentContextStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.IAgentContextStatics'
    _iid_ = Guid('{0625abf6-79f6-5116-a14a-91b3967fc214}')
    @winrt_commethod(6)
    def GetContextForCaller(self) -> win32more.Windows.AI.Agents.AgentContext: ...
class IAgentInfo(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.IAgentInfo'
    _iid_ = Guid('{b023d498-59ab-410b-83e7-1ed007ee2f68}')
    @winrt_commethod(6)
    def get_Id(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetPackage(self) -> win32more.Windows.ApplicationModel.Package: ...
    Description = property(get_Description, None)
    Id = property(get_Id, None)
    Name = property(get_Name, None)
class IAgentResourcesStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.IAgentResourcesStatics'
    _iid_ = Guid('{adedaaf8-3487-50b4-ac42-490083642b05}')
    @winrt_commethod(6)
    def get_FileSystemRead(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_FileSystemWrite(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_FileSystemDelete(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_FileSystemCreate(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_HttpGet(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_HttpPost(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_HttpPut(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_HttpDelete(self) -> WinRT_String: ...
    FileSystemCreate = property(get_FileSystemCreate, None)
    FileSystemDelete = property(get_FileSystemDelete, None)
    FileSystemRead = property(get_FileSystemRead, None)
    FileSystemWrite = property(get_FileSystemWrite, None)
    HttpDelete = property(get_HttpDelete, None)
    HttpGet = property(get_HttpGet, None)
    HttpPost = property(get_HttpPost, None)
    HttpPut = property(get_HttpPut, None)


make_ready(__name__)
