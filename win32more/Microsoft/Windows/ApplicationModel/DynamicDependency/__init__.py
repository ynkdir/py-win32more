from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.Windows.ApplicationModel.DynamicDependency
import win32more.Windows.ApplicationModel
import win32more.Windows.Win32.System.WinRT
class AddPackageDependencyOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.IAddPackageDependencyOptions
    _classid_ = 'Microsoft.Windows.ApplicationModel.DynamicDependency.AddPackageDependencyOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.AddPackageDependencyOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.AddPackageDependencyOptions: ...
    @winrt_mixinmethod
    def get_Rank(self: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.IAddPackageDependencyOptions) -> Int32: ...
    @winrt_mixinmethod
    def put_Rank(self: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.IAddPackageDependencyOptions, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_PrependIfRankCollision(self: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.IAddPackageDependencyOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_PrependIfRankCollision(self: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.IAddPackageDependencyOptions, value: Boolean) -> Void: ...
    PrependIfRankCollision = property(get_PrependIfRankCollision, put_PrependIfRankCollision)
    Rank = property(get_Rank, put_Rank)
class CreatePackageDependencyOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.ICreatePackageDependencyOptions
    _classid_ = 'Microsoft.Windows.ApplicationModel.DynamicDependency.CreatePackageDependencyOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.CreatePackageDependencyOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.CreatePackageDependencyOptions: ...
    @winrt_mixinmethod
    def get_Architectures(self: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.ICreatePackageDependencyOptions) -> win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependencyProcessorArchitectures: ...
    @winrt_mixinmethod
    def put_Architectures(self: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.ICreatePackageDependencyOptions, value: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependencyProcessorArchitectures) -> Void: ...
    @winrt_mixinmethod
    def get_VerifyDependencyResolution(self: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.ICreatePackageDependencyOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_VerifyDependencyResolution(self: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.ICreatePackageDependencyOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_LifetimeArtifactKind(self: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.ICreatePackageDependencyOptions) -> win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependencyLifetimeArtifactKind: ...
    @winrt_mixinmethod
    def put_LifetimeArtifactKind(self: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.ICreatePackageDependencyOptions, value: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependencyLifetimeArtifactKind) -> Void: ...
    @winrt_mixinmethod
    def get_LifetimeArtifact(self: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.ICreatePackageDependencyOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_LifetimeArtifact(self: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.ICreatePackageDependencyOptions, value: WinRT_String) -> Void: ...
    Architectures = property(get_Architectures, put_Architectures)
    LifetimeArtifact = property(get_LifetimeArtifact, put_LifetimeArtifact)
    LifetimeArtifactKind = property(get_LifetimeArtifactKind, put_LifetimeArtifactKind)
    VerifyDependencyResolution = property(get_VerifyDependencyResolution, put_VerifyDependencyResolution)
DynamicDependencyContract: UInt32 = 131072
class IAddPackageDependencyOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.DynamicDependency.IAddPackageDependencyOptions'
    _iid_ = Guid('{01b801fd-24e3-5e6b-9f1c-805ab410b604}')
    @winrt_commethod(6)
    def get_Rank(self) -> Int32: ...
    @winrt_commethod(7)
    def put_Rank(self, value: Int32) -> Void: ...
    @winrt_commethod(8)
    def get_PrependIfRankCollision(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_PrependIfRankCollision(self, value: Boolean) -> Void: ...
    PrependIfRankCollision = property(get_PrependIfRankCollision, put_PrependIfRankCollision)
    Rank = property(get_Rank, put_Rank)
class ICreatePackageDependencyOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.DynamicDependency.ICreatePackageDependencyOptions'
    _iid_ = Guid('{cdbb820f-3c69-55dc-a017-b4132574c5d6}')
    @winrt_commethod(6)
    def get_Architectures(self) -> win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependencyProcessorArchitectures: ...
    @winrt_commethod(7)
    def put_Architectures(self, value: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependencyProcessorArchitectures) -> Void: ...
    @winrt_commethod(8)
    def get_VerifyDependencyResolution(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_VerifyDependencyResolution(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_LifetimeArtifactKind(self) -> win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependencyLifetimeArtifactKind: ...
    @winrt_commethod(11)
    def put_LifetimeArtifactKind(self, value: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependencyLifetimeArtifactKind) -> Void: ...
    @winrt_commethod(12)
    def get_LifetimeArtifact(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_LifetimeArtifact(self, value: WinRT_String) -> Void: ...
    Architectures = property(get_Architectures, put_Architectures)
    LifetimeArtifact = property(get_LifetimeArtifact, put_LifetimeArtifact)
    LifetimeArtifactKind = property(get_LifetimeArtifactKind, put_LifetimeArtifactKind)
    VerifyDependencyResolution = property(get_VerifyDependencyResolution, put_VerifyDependencyResolution)
class IPackageDependency(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.DynamicDependency.IPackageDependency'
    _iid_ = Guid('{32ae7b95-e358-5a48-9669-c97d85ad6556}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def Delete(self) -> Void: ...
    @winrt_commethod(8)
    def Add(self) -> win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependencyContext: ...
    @winrt_commethod(9)
    def Add2(self, options: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.AddPackageDependencyOptions) -> win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependencyContext: ...
    Id = property(get_Id, None)
class IPackageDependencyContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.DynamicDependency.IPackageDependencyContext'
    _iid_ = Guid('{9902c35a-a3f5-5645-af0f-cdf9fca00d5e}')
    @winrt_commethod(6)
    def get_ContextId(self) -> win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependencyContextId: ...
    @winrt_commethod(7)
    def get_PackageDependencyId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_PackageFullName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def Remove(self) -> Void: ...
    ContextId = property(get_ContextId, None)
    PackageDependencyId = property(get_PackageDependencyId, None)
    PackageFullName = property(get_PackageFullName, None)
class IPackageDependencyContextFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.DynamicDependency.IPackageDependencyContextFactory'
    _iid_ = Guid('{9914f24f-bebf-516b-adab-5c3e8bf323f8}')
    @winrt_commethod(6)
    def CreateInstance(self, contextId: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependencyContextId) -> win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependencyContext: ...
class IPackageDependencyRankStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.DynamicDependency.IPackageDependencyRankStatics'
    _iid_ = Guid('{260583bd-a4ab-53fd-a190-c446bfdb5384}')
    @winrt_commethod(6)
    def get_Default(self) -> Int32: ...
    Default = property(get_Default, None)
class IPackageDependencyStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.DynamicDependency.IPackageDependencyStatics'
    _iid_ = Guid('{17b656e1-1a58-5f3c-84a8-4430f6e749c2}')
    @winrt_commethod(6)
    def GetFromId(self, id: WinRT_String) -> win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependency: ...
    @winrt_commethod(7)
    def GetFromIdForSystem(self, id: WinRT_String) -> win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependency: ...
    @winrt_commethod(8)
    def Create(self, packageFamilyName: WinRT_String, minVersion: win32more.Windows.ApplicationModel.PackageVersion) -> win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependency: ...
    @winrt_commethod(9)
    def Create2(self, packageFamilyName: WinRT_String, minVersion: win32more.Windows.ApplicationModel.PackageVersion, options: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.CreatePackageDependencyOptions) -> win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependency: ...
    @winrt_commethod(10)
    def CreateForSystem(self, packageFamilyName: WinRT_String, minVersion: win32more.Windows.ApplicationModel.PackageVersion, options: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.CreatePackageDependencyOptions) -> win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependency: ...
    @winrt_commethod(11)
    def get_GenerationId(self) -> UInt32: ...
    GenerationId = property(get_GenerationId, None)
class IPackageDependencyStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.DynamicDependency.IPackageDependencyStatics2'
    _iid_ = Guid('{c7c6e4f3-c0ca-5fdb-bef2-57e6020ffe4e}')
    @winrt_commethod(6)
    def get_PackageGraphRevisionId(self) -> UInt32: ...
    PackageGraphRevisionId = property(get_PackageGraphRevisionId, None)
class _PackageDependency_Meta_(ComPtr.__class__):
    pass
class PackageDependency(ComPtr, metaclass=_PackageDependency_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.IPackageDependency
    _classid_ = 'Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependency'
    @winrt_mixinmethod
    def get_Id(self: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.IPackageDependency) -> WinRT_String: ...
    @winrt_mixinmethod
    def Delete(self: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.IPackageDependency) -> Void: ...
    @winrt_mixinmethod
    def Add(self: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.IPackageDependency) -> win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependencyContext: ...
    @winrt_mixinmethod
    def Add2(self: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.IPackageDependency, options: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.AddPackageDependencyOptions) -> win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependencyContext: ...
    @winrt_classmethod
    def get_PackageGraphRevisionId(cls: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.IPackageDependencyStatics2) -> UInt32: ...
    @winrt_classmethod
    def GetFromId(cls: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.IPackageDependencyStatics, id: WinRT_String) -> win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependency: ...
    @winrt_classmethod
    def GetFromIdForSystem(cls: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.IPackageDependencyStatics, id: WinRT_String) -> win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependency: ...
    @winrt_classmethod
    def Create(cls: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.IPackageDependencyStatics, packageFamilyName: WinRT_String, minVersion: win32more.Windows.ApplicationModel.PackageVersion) -> win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependency: ...
    @winrt_classmethod
    def Create2(cls: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.IPackageDependencyStatics, packageFamilyName: WinRT_String, minVersion: win32more.Windows.ApplicationModel.PackageVersion, options: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.CreatePackageDependencyOptions) -> win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependency: ...
    @winrt_classmethod
    def CreateForSystem(cls: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.IPackageDependencyStatics, packageFamilyName: WinRT_String, minVersion: win32more.Windows.ApplicationModel.PackageVersion, options: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.CreatePackageDependencyOptions) -> win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependency: ...
    @winrt_classmethod
    def get_GenerationId(cls: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.IPackageDependencyStatics) -> UInt32: ...
    Id = property(get_Id, None)
    _PackageDependency_Meta_.GenerationId = property(get_GenerationId, None)
    _PackageDependency_Meta_.PackageGraphRevisionId = property(get_PackageGraphRevisionId, None)
class PackageDependencyContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.IPackageDependencyContext
    _classid_ = 'Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependencyContext'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependencyContext.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.IPackageDependencyContextFactory, contextId: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependencyContextId) -> win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependencyContext: ...
    @winrt_mixinmethod
    def get_ContextId(self: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.IPackageDependencyContext) -> win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependencyContextId: ...
    @winrt_mixinmethod
    def get_PackageDependencyId(self: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.IPackageDependencyContext) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PackageFullName(self: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.IPackageDependencyContext) -> WinRT_String: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.IPackageDependencyContext) -> Void: ...
    ContextId = property(get_ContextId, None)
    PackageDependencyId = property(get_PackageDependencyId, None)
    PackageFullName = property(get_PackageFullName, None)
class PackageDependencyContextId(Structure):
    Id: UInt64
class PackageDependencyLifetimeArtifactKind(Enum, Int32):
    Process = 0
    FilePath = 1
    RegistryKey = 2
class PackageDependencyProcessorArchitectures(Enum, UInt32):
    None_ = 0
    Neutral = 1
    X86 = 2
    X64 = 4
    Arm = 8
    Arm64 = 16
    X86OnArm64 = 32
class _PackageDependencyRank_Meta_(ComPtr.__class__):
    pass
class PackageDependencyRank(ComPtr, metaclass=_PackageDependencyRank_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependencyRank'
    @winrt_classmethod
    def get_Default(cls: win32more.Microsoft.Windows.ApplicationModel.DynamicDependency.IPackageDependencyRankStatics) -> Int32: ...
    _PackageDependencyRank_Meta_.Default = property(get_Default, None)


make_ready(__name__)
