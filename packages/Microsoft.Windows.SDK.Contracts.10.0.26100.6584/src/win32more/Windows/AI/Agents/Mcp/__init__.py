from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.AI.Agents.Mcp
import win32more.Windows.ApplicationModel
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.UI
class IMcpHttpConnectionResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.Mcp.IMcpHttpConnectionResult'
    _iid_ = Guid('{d2c3755f-6d3c-5e90-84dd-3e0973049606}')
    @winrt_commethod(6)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_Uri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def get_Headers(self) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    Headers = property(get_Headers, None)
    Uri = property(get_Uri, put_Uri)
class IMcpMessageFilter(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.Mcp.IMcpMessageFilter'
    _iid_ = Guid('{8ee681f8-f858-56f7-a0c7-45f928845f9b}')
    @winrt_commethod(6)
    def Initialize(self, clientAppUserModelId: WinRT_String, serverPackageFamilyName: WinRT_String, serverId: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def OnMessage(self, message: WinRT_String, direction: win32more.Windows.AI.Agents.Mcp.McpMessageDirection, filterResponse: win32more.Windows.AI.Agents.Mcp.McpMessageFilterResponse) -> Void: ...
class IMcpMessageFilterResponse(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.Mcp.IMcpMessageFilterResponse'
    _iid_ = Guid('{bcfc9710-e1d8-5ed4-9dab-03269635d83b}')
    @winrt_commethod(6)
    def get_MessageAction(self) -> win32more.Windows.AI.Agents.Mcp.McpMessageAction: ...
    @winrt_commethod(7)
    def put_MessageAction(self, value: win32more.Windows.AI.Agents.Mcp.McpMessageAction) -> Void: ...
    MessageAction = property(get_MessageAction, put_MessageAction)
class IMcpNamedPipeConnectionResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.Mcp.IMcpNamedPipeConnectionResult'
    _iid_ = Guid('{8a2aef6f-b4dc-5180-a3e1-47b63dbbb70a}')
class IMcpNamedPipeConnectionServer(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.Mcp.IMcpNamedPipeConnectionServer'
    _iid_ = Guid('{52bbbdea-3858-5e4c-91d2-86deebf8ecd0}')
    @winrt_commethod(6)
    def Connect(self, hostContext: win32more.Windows.AI.Agents.Mcp.McpServerContext, pipeName: WinRT_String, connectionResult: win32more.Windows.AI.Agents.Mcp.McpNamedPipeConnectionResult) -> Void: ...
class IMcpResourcesStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.Mcp.IMcpResourcesStatics'
    _iid_ = Guid('{9b9f451c-73f8-59c0-bbea-5ceb60b5f26c}')
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
class IMcpServerContext(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.Mcp.IMcpServerContext'
    _iid_ = Guid('{d92a55b5-5c54-5505-960a-8a1a15180e8b}')
    @winrt_commethod(6)
    def get_AppId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def RequestResourceAccess(self, resource: win32more.Windows.Foundation.Uri, description: WinRT_String, reasonForAsking: WinRT_String) -> win32more.Windows.AI.Agents.Mcp.McpAuthorizationResponse: ...
    AppId = property(get_AppId, None)
class IMcpServerContextStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.Mcp.IMcpServerContextStatics'
    _iid_ = Guid('{1f84b814-9fe8-521d-bf3c-b2f12861b29b}')
    @winrt_commethod(6)
    def GetContextForCaller(self) -> win32more.Windows.AI.Agents.Mcp.McpServerContext: ...
class IMcpServerInfo(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.Mcp.IMcpServerInfo'
    _iid_ = Guid('{96622943-0771-4960-8851-7e3ee690ea7e}')
    @winrt_commethod(6)
    def get_Id(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Package(self) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_commethod(10)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_AppUserModelId(self) -> WinRT_String: ...
    AppUserModelId = property(get_AppUserModelId, None)
    Description = property(get_Description, None)
    DisplayName = property(get_DisplayName, None)
    Id = property(get_Id, None)
    Name = property(get_Name, None)
    Package = property(get_Package, None)
class IMcpServerRegistry(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.Mcp.IMcpServerRegistry'
    _iid_ = Guid('{fece06c6-0aa5-4bd1-8e64-fbc5f328f5dc}')
    @winrt_commethod(6)
    def GetMcpServerInfos(self) -> ReceiveArray[win32more.Windows.AI.Agents.Mcp.McpServerInfo]: ...
    @winrt_commethod(7)
    def GetMcpConnectionInfo(self, mcpServerId: Guid, ownerWindowId: win32more.Windows.UI.WindowId) -> win32more.Windows.AI.Agents.Mcp.McpStdioConnectionInfo: ...
class IMcpServerRegistryStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.Mcp.IMcpServerRegistryStatics'
    _iid_ = Guid('{4acf7fed-d300-55bc-9dde-9f433cdc903d}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.AI.Agents.Mcp.McpServerRegistry: ...
class IMcpSseConnectionServer(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.Mcp.IMcpSseConnectionServer'
    _iid_ = Guid('{c460edda-9200-5ecb-91b3-157ee1d2fdf5}')
    @winrt_commethod(6)
    def Connect(self, hostContext: win32more.Windows.AI.Agents.Mcp.McpServerContext, connectionResult: win32more.Windows.AI.Agents.Mcp.McpHttpConnectionResult) -> Void: ...
class IMcpStdioConnectionInfo(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.Mcp.IMcpStdioConnectionInfo'
    _iid_ = Guid('{fbc54aac-590b-526c-a545-b7c731b18c39}')
    @winrt_commethod(6)
    def get_Command(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetCommandArguments(self) -> ReceiveArray[WinRT_String]: ...
    @winrt_commethod(8)
    def get_Info(self) -> win32more.Windows.AI.Agents.Mcp.McpServerInfo: ...
    Command = property(get_Command, None)
    Info = property(get_Info, None)
class McpAuthorizationResponse(Enum, Int32):
    Denied = 0
    Approved = 1
class McpHttpConnectionResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.AI.Agents.Mcp.IMcpHttpConnectionResult
    _classid_ = 'Windows.AI.Agents.Mcp.McpHttpConnectionResult'
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.AI.Agents.Mcp.IMcpHttpConnectionResult) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Uri(self: win32more.Windows.AI.Agents.Mcp.IMcpHttpConnectionResult, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_Headers(self: win32more.Windows.AI.Agents.Mcp.IMcpHttpConnectionResult) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    Headers = property(get_Headers, None)
    Uri = property(get_Uri, put_Uri)
class McpMessageAction(Enum, Int32):
    Allow = 0
    Block = 1
class McpMessageDirection(Enum, Int32):
    Request = 0
    Response = 1
class McpMessageFilterResponse(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.AI.Agents.Mcp.IMcpMessageFilterResponse
    _classid_ = 'Windows.AI.Agents.Mcp.McpMessageFilterResponse'
    @winrt_mixinmethod
    def get_MessageAction(self: win32more.Windows.AI.Agents.Mcp.IMcpMessageFilterResponse) -> win32more.Windows.AI.Agents.Mcp.McpMessageAction: ...
    @winrt_mixinmethod
    def put_MessageAction(self: win32more.Windows.AI.Agents.Mcp.IMcpMessageFilterResponse, value: win32more.Windows.AI.Agents.Mcp.McpMessageAction) -> Void: ...
    MessageAction = property(get_MessageAction, put_MessageAction)
class McpNamedPipeConnectionResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.AI.Agents.Mcp.IMcpNamedPipeConnectionResult
    _classid_ = 'Windows.AI.Agents.Mcp.McpNamedPipeConnectionResult'
class _McpResources_Meta_(ComPtr.__class__):
    pass
class McpResources(ComPtr, metaclass=_McpResources_Meta_):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.Mcp.McpResources'
    @winrt_classmethod
    def get_FileSystemRead(cls: win32more.Windows.AI.Agents.Mcp.IMcpResourcesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_FileSystemWrite(cls: win32more.Windows.AI.Agents.Mcp.IMcpResourcesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_FileSystemDelete(cls: win32more.Windows.AI.Agents.Mcp.IMcpResourcesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_FileSystemCreate(cls: win32more.Windows.AI.Agents.Mcp.IMcpResourcesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HttpGet(cls: win32more.Windows.AI.Agents.Mcp.IMcpResourcesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HttpPost(cls: win32more.Windows.AI.Agents.Mcp.IMcpResourcesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HttpPut(cls: win32more.Windows.AI.Agents.Mcp.IMcpResourcesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HttpDelete(cls: win32more.Windows.AI.Agents.Mcp.IMcpResourcesStatics) -> WinRT_String: ...
    _McpResources_Meta_.FileSystemCreate = property(get_FileSystemCreate, None)
    _McpResources_Meta_.FileSystemDelete = property(get_FileSystemDelete, None)
    _McpResources_Meta_.FileSystemRead = property(get_FileSystemRead, None)
    _McpResources_Meta_.FileSystemWrite = property(get_FileSystemWrite, None)
    _McpResources_Meta_.HttpDelete = property(get_HttpDelete, None)
    _McpResources_Meta_.HttpGet = property(get_HttpGet, None)
    _McpResources_Meta_.HttpPost = property(get_HttpPost, None)
    _McpResources_Meta_.HttpPut = property(get_HttpPut, None)
class McpServerContext(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.AI.Agents.Mcp.IMcpServerContext
    _classid_ = 'Windows.AI.Agents.Mcp.McpServerContext'
    @winrt_mixinmethod
    def get_AppId(self: win32more.Windows.AI.Agents.Mcp.IMcpServerContext) -> WinRT_String: ...
    @winrt_mixinmethod
    def RequestResourceAccess(self: win32more.Windows.AI.Agents.Mcp.IMcpServerContext, resource: win32more.Windows.Foundation.Uri, description: WinRT_String, reasonForAsking: WinRT_String) -> win32more.Windows.AI.Agents.Mcp.McpAuthorizationResponse: ...
    @winrt_classmethod
    def GetContextForCaller(cls: win32more.Windows.AI.Agents.Mcp.IMcpServerContextStatics) -> win32more.Windows.AI.Agents.Mcp.McpServerContext: ...
    AppId = property(get_AppId, None)
class McpServerInfo(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.AI.Agents.Mcp.IMcpServerInfo
    _classid_ = 'Windows.AI.Agents.Mcp.McpServerInfo'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.AI.Agents.Mcp.IMcpServerInfo) -> Guid: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.AI.Agents.Mcp.IMcpServerInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.AI.Agents.Mcp.IMcpServerInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Package(self: win32more.Windows.AI.Agents.Mcp.IMcpServerInfo) -> win32more.Windows.ApplicationModel.Package: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.AI.Agents.Mcp.IMcpServerInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppUserModelId(self: win32more.Windows.AI.Agents.Mcp.IMcpServerInfo) -> WinRT_String: ...
    AppUserModelId = property(get_AppUserModelId, None)
    Description = property(get_Description, None)
    DisplayName = property(get_DisplayName, None)
    Id = property(get_Id, None)
    Name = property(get_Name, None)
    Package = property(get_Package, None)
class McpServerRegistry(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.AI.Agents.Mcp.IMcpServerRegistry
    _classid_ = 'Windows.AI.Agents.Mcp.McpServerRegistry'
    @winrt_mixinmethod
    def GetMcpServerInfos(self: win32more.Windows.AI.Agents.Mcp.IMcpServerRegistry) -> ReceiveArray[win32more.Windows.AI.Agents.Mcp.McpServerInfo]: ...
    @winrt_mixinmethod
    def GetMcpConnectionInfo(self: win32more.Windows.AI.Agents.Mcp.IMcpServerRegistry, mcpServerId: Guid, ownerWindowId: win32more.Windows.UI.WindowId) -> win32more.Windows.AI.Agents.Mcp.McpStdioConnectionInfo: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.AI.Agents.Mcp.IMcpServerRegistryStatics) -> win32more.Windows.AI.Agents.Mcp.McpServerRegistry: ...
class McpStdioConnectionInfo(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.AI.Agents.Mcp.IMcpStdioConnectionInfo
    _classid_ = 'Windows.AI.Agents.Mcp.McpStdioConnectionInfo'
    @winrt_mixinmethod
    def get_Command(self: win32more.Windows.AI.Agents.Mcp.IMcpStdioConnectionInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetCommandArguments(self: win32more.Windows.AI.Agents.Mcp.IMcpStdioConnectionInfo) -> ReceiveArray[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Info(self: win32more.Windows.AI.Agents.Mcp.IMcpStdioConnectionInfo) -> win32more.Windows.AI.Agents.Mcp.McpServerInfo: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Command = property(get_Command, None)
    Info = property(get_Info, None)


make_ready(__name__)
