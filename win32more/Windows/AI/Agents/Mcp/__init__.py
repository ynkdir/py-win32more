from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.AI.Agents
import win32more.Windows.AI.Agents.Mcp
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
class IMcpNamedPipeConnectionResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.Mcp.IMcpNamedPipeConnectionResult'
    _iid_ = Guid('{8a2aef6f-b4dc-5180-a3e1-47b63dbbb70a}')
class IMcpNamedPipeConnectionServer(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.Mcp.IMcpNamedPipeConnectionServer'
    _iid_ = Guid('{52f204a5-2ad1-5430-96c9-ea7e090be839}')
    @winrt_commethod(6)
    def Connect(self, hostContext: win32more.Windows.AI.Agents.AgentContext, pipeName: WinRT_String, connectionResult: win32more.Windows.AI.Agents.Mcp.McpNamedPipeConnectionResult) -> win32more.Windows.AI.Agents.Mcp.McpNamedPipeConnectionResult: ...
class IMcpServerRegistry(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.Mcp.IMcpServerRegistry'
    _iid_ = Guid('{150f795b-3f93-4493-abc7-48a04fd2d7b6}')
    @winrt_commethod(6)
    def GetAgentInfos(self) -> ReceiveArray[win32more.Windows.AI.Agents.AgentInfo]: ...
    @winrt_commethod(7)
    def GetMcpConnectionInfo(self, agentId: Guid, ownerWindowId: win32more.Windows.UI.WindowId) -> win32more.Windows.AI.Agents.Mcp.McpStdioConnectionInfo: ...
class IMcpServerRegistryStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.Mcp.IMcpServerRegistryStatics'
    _iid_ = Guid('{4acf7fed-d300-55bc-9dde-9f433cdc903d}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.AI.Agents.Mcp.McpServerRegistry: ...
class IMcpSseConnectionServer(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.Mcp.IMcpSseConnectionServer'
    _iid_ = Guid('{6c558671-1b20-5b6b-920d-b8afc2509771}')
    @winrt_commethod(6)
    def Connect(self, hostContext: win32more.Windows.AI.Agents.AgentContext, connectionResult: win32more.Windows.AI.Agents.Mcp.McpHttpConnectionResult) -> win32more.Windows.AI.Agents.Mcp.McpHttpConnectionResult: ...
class IMcpStdioConnectionInfo(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.Mcp.IMcpStdioConnectionInfo'
    _iid_ = Guid('{93d9827b-32a2-5b89-ba8a-05bd2093598e}')
    @winrt_commethod(6)
    def get_Command(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetCommandArguments(self) -> ReceiveArray[WinRT_String]: ...
    @winrt_commethod(8)
    def get_Info(self) -> win32more.Windows.AI.Agents.AgentInfo: ...
    Command = property(get_Command, None)
    Info = property(get_Info, None)
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
class McpNamedPipeConnectionResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.AI.Agents.Mcp.IMcpNamedPipeConnectionResult
    _classid_ = 'Windows.AI.Agents.Mcp.McpNamedPipeConnectionResult'
class McpServerRegistry(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.AI.Agents.Mcp.IMcpServerRegistry
    _classid_ = 'Windows.AI.Agents.Mcp.McpServerRegistry'
    @winrt_mixinmethod
    def GetAgentInfos(self: win32more.Windows.AI.Agents.Mcp.IMcpServerRegistry) -> ReceiveArray[win32more.Windows.AI.Agents.AgentInfo]: ...
    @winrt_mixinmethod
    def GetMcpConnectionInfo(self: win32more.Windows.AI.Agents.Mcp.IMcpServerRegistry, agentId: Guid, ownerWindowId: win32more.Windows.UI.WindowId) -> win32more.Windows.AI.Agents.Mcp.McpStdioConnectionInfo: ...
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
    def get_Info(self: win32more.Windows.AI.Agents.Mcp.IMcpStdioConnectionInfo) -> win32more.Windows.AI.Agents.AgentInfo: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Command = property(get_Command, None)
    Info = property(get_Info, None)


make_ready(__name__)
