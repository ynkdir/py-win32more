from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.AI.Agents.Mcp
class IMcpMessageFilterExperimental(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.Mcp.IMcpMessageFilterExperimental'
    _iid_ = Guid('{c5f8f821-895c-5241-b45a-92e249a7d873}')
    @winrt_commethod(6)
    def Initialize(self, clientAppUserModelId: hstr, clientProcessId: UInt32, serverIdentity: hstr, serverName: hstr, serverProcessId: UInt32) -> Void: ...
    @winrt_commethod(7)
    def OnMessage(self, message: hstr, direction: win32more.Windows.AI.Agents.Mcp.McpMessageDirection, filterResponse: win32more.Windows.AI.Agents.Mcp.McpMessageFilterResponse) -> Void: ...
class IMcpMessageFilterResponse(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.Mcp.IMcpMessageFilterResponse'
    _iid_ = Guid('{363ce02c-7098-5e13-a408-7b43e1f452ac}')
class IMcpMessageFilterResponseExperimental(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.Mcp.IMcpMessageFilterResponseExperimental'
    _iid_ = Guid('{e215b5f2-cb02-56cf-aab0-84aef65d1665}')
    @winrt_commethod(6)
    def get_IsAllowed(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsAllowed(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_MessageIfNotAllowed(self) -> hstr: ...
    @winrt_commethod(9)
    def put_MessageIfNotAllowed(self, value: hstr) -> Void: ...
    IsAllowed = property(get_IsAllowed, put_IsAllowed)
    MessageIfNotAllowed = property(get_MessageIfNotAllowed, put_MessageIfNotAllowed)
class IMcpMessageFilterResponseExperimental2(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Agents.Mcp.IMcpMessageFilterResponseExperimental2'
    _iid_ = Guid('{10f4b099-6632-505a-a638-e704c7e47abf}')
    @winrt_commethod(6)
    def Allow(self) -> Void: ...
    @winrt_commethod(7)
    def Reject(self, reason: hstr) -> Void: ...
class McpMessageDirection(Enum, Int32):
    _name_ = 'Windows.AI.Agents.Mcp.McpMessageDirection'
    ClientToServer = 0
    ServerToClient = 1
class McpMessageFilterResponse(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.AI.Agents.Mcp.IMcpMessageFilterResponse
    _classid_ = 'Windows.AI.Agents.Mcp.McpMessageFilterResponse'


make_ready(__name__)
