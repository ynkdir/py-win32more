from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, FlexibleArray, Guid, Int16, Int32, Int64, IntPtr, NativeBitfieldAttribute, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IInspectable, IUnknown, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.AI.ModelContextProtocol
import win32more.Windows.ApplicationModel
import win32more.Windows.Foundation
import win32more.Windows.UI
class IModelContextProtocolClientContext(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.ModelContextProtocol.IModelContextProtocolClientContext'
    _iid_ = Guid('{5bd93f10-c0aa-4963-b4c5-ac4a69bdbb33}')
    @winrt_commethod(6)
    def put_OwnerWindowId(self, value: win32more.Windows.UI.WindowId) -> Void: ...
    @winrt_commethod(7)
    def get_OwnerWindowId(self) -> win32more.Windows.UI.WindowId: ...
    OwnerWindowId = property(get_OwnerWindowId, put_OwnerWindowId)
class IModelContextProtocolClientContextFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.ModelContextProtocol.IModelContextProtocolClientContextFactory'
    _iid_ = Guid('{efb2ba31-148c-5ad7-ab8f-4f0e6154fedb}')
class IModelContextProtocolServer(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.AI.ModelContextProtocol.IModelContextProtocolServer'
    _iid_ = Guid('{9d78431d-533f-55dd-9692-dc1462f0bb39}')
    @winrt_commethod(6)
    def get_Command(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetCommandArguments(self) -> ReceiveArray[WinRT_String]: ...
    @winrt_commethod(8)
    def get_Info(self) -> win32more.Windows.AI.ModelContextProtocol.ModelContextProtocolServerInfo: ...
    Command = property(get_Command, None)
    Info = property(get_Info, None)
class IModelContextProtocolServerCatalog(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.ModelContextProtocol.IModelContextProtocolServerCatalog'
    _iid_ = Guid('{062b8a5e-b124-4490-a1ba-4692875df83e}')
    @winrt_commethod(6)
    def GetServerInfos(self) -> ReceiveArray[win32more.Windows.AI.ModelContextProtocol.ModelContextProtocolServerInfo]: ...
    @winrt_commethod(7)
    def ActivateServer(self, serverId: Guid, client: win32more.Windows.AI.ModelContextProtocol.ModelContextProtocolClientContext) -> win32more.Windows.AI.ModelContextProtocol.IModelContextProtocolServer: ...
    @winrt_commethod(8)
    def CreateClientContext(self) -> win32more.Windows.AI.ModelContextProtocol.ModelContextProtocolClientContext: ...
class IModelContextProtocolServerCatalogFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.ModelContextProtocol.IModelContextProtocolServerCatalogFactory'
    _iid_ = Guid('{6e5d0e8f-77e1-5a9d-b980-0779b3b128ba}')
class IModelContextProtocolServerInfo(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.ModelContextProtocol.IModelContextProtocolServerInfo'
    _iid_ = Guid('{503102ba-831b-47e5-b97b-e7b06209dd8b}')
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
class IModelContextProtocolServerInfoFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.ModelContextProtocol.IModelContextProtocolServerInfoFactory'
    _iid_ = Guid('{c93ee14e-e477-5a65-bd80-2a7860de7ead}')
class ModelContextProtocolClientContext(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.AI.ModelContextProtocol.IModelContextProtocolClientContext
    _classid_ = 'Windows.AI.ModelContextProtocol.ModelContextProtocolClientContext'
    @winrt_mixinmethod
    def put_OwnerWindowId(self: win32more.Windows.AI.ModelContextProtocol.IModelContextProtocolClientContext, value: win32more.Windows.UI.WindowId) -> Void: ...
    @winrt_mixinmethod
    def get_OwnerWindowId(self: win32more.Windows.AI.ModelContextProtocol.IModelContextProtocolClientContext) -> win32more.Windows.UI.WindowId: ...
    OwnerWindowId = property(get_OwnerWindowId, put_OwnerWindowId)
ModelContextProtocolContract: UInt32 = 65536
class ModelContextProtocolServerCatalog(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.AI.ModelContextProtocol.IModelContextProtocolServerCatalog
    _classid_ = 'Windows.AI.ModelContextProtocol.ModelContextProtocolServerCatalog'
    @winrt_mixinmethod
    def GetServerInfos(self: win32more.Windows.AI.ModelContextProtocol.IModelContextProtocolServerCatalog) -> ReceiveArray[win32more.Windows.AI.ModelContextProtocol.ModelContextProtocolServerInfo]: ...
    @winrt_mixinmethod
    def ActivateServer(self: win32more.Windows.AI.ModelContextProtocol.IModelContextProtocolServerCatalog, serverId: Guid, client: win32more.Windows.AI.ModelContextProtocol.ModelContextProtocolClientContext) -> win32more.Windows.AI.ModelContextProtocol.IModelContextProtocolServer: ...
    @winrt_mixinmethod
    def CreateClientContext(self: win32more.Windows.AI.ModelContextProtocol.IModelContextProtocolServerCatalog) -> win32more.Windows.AI.ModelContextProtocol.ModelContextProtocolClientContext: ...
class ModelContextProtocolServerInfo(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.AI.ModelContextProtocol.IModelContextProtocolServerInfo
    _classid_ = 'Windows.AI.ModelContextProtocol.ModelContextProtocolServerInfo'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.AI.ModelContextProtocol.IModelContextProtocolServerInfo) -> Guid: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.AI.ModelContextProtocol.IModelContextProtocolServerInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.AI.ModelContextProtocol.IModelContextProtocolServerInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetPackage(self: win32more.Windows.AI.ModelContextProtocol.IModelContextProtocolServerInfo) -> win32more.Windows.ApplicationModel.Package: ...
    Description = property(get_Description, None)
    Id = property(get_Id, None)
    Name = property(get_Name, None)


make_ready(__name__)
