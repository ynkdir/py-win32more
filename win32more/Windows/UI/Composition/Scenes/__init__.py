from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Foundation.Numerics
import win32more.Windows.Graphics.DirectX
import win32more.Windows.UI.Composition
import win32more.Windows.UI.Composition.Scenes
import win32more.Windows.Win32.System.WinRT
class ISceneBoundingBox(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.ISceneBoundingBox'
    _iid_ = Guid('{5d8ffc70-c618-4083-8251-9962593114aa}')
    @winrt_commethod(6)
    def get_Center(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(7)
    def get_Extents(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(8)
    def get_Max(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(9)
    def get_Min(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(10)
    def get_Size(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    Center = property(get_Center, None)
    Extents = property(get_Extents, None)
    Max = property(get_Max, None)
    Min = property(get_Min, None)
    Size = property(get_Size, None)
class ISceneComponent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.ISceneComponent'
    _iid_ = Guid('{ae20fc96-226c-44bd-95cb-dd5ed9ebe9a5}')
    @winrt_commethod(6)
    def get_ComponentType(self) -> win32more.Windows.UI.Composition.Scenes.SceneComponentType: ...
    ComponentType = property(get_ComponentType, None)
class ISceneComponentCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.ISceneComponentCollection'
    _iid_ = Guid('{c483791c-5f46-45e4-b666-a3d2259f9b2e}')
class ISceneComponentFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.ISceneComponentFactory'
    _iid_ = Guid('{5fbc5574-ddd8-5889-ab5b-d8fa716e7c9e}')
class ISceneMaterial(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.ISceneMaterial'
    _iid_ = Guid('{8ca74b7c-30df-4e07-9490-37875af1a123}')
class ISceneMaterialFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.ISceneMaterialFactory'
    _iid_ = Guid('{67536c19-a707-5254-a495-7fdc799893b9}')
class ISceneMaterialInput(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.ISceneMaterialInput'
    _iid_ = Guid('{422a1642-1ef1-485c-97e9-ae6f95ad812f}')
class ISceneMaterialInputFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.ISceneMaterialInputFactory'
    _iid_ = Guid('{a88feb74-7d0a-5e4c-a748-1015af9ca74f}')
class ISceneMesh(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.ISceneMesh'
    _iid_ = Guid('{ee9a1530-1155-4c0c-92bd-40020cf78347}')
    @winrt_commethod(6)
    def get_Bounds(self) -> win32more.Windows.UI.Composition.Scenes.SceneBoundingBox: ...
    @winrt_commethod(7)
    def get_PrimitiveTopology(self) -> win32more.Windows.Graphics.DirectX.DirectXPrimitiveTopology: ...
    @winrt_commethod(8)
    def put_PrimitiveTopology(self, value: win32more.Windows.Graphics.DirectX.DirectXPrimitiveTopology) -> Void: ...
    @winrt_commethod(9)
    def FillMeshAttribute(self, semantic: win32more.Windows.UI.Composition.Scenes.SceneAttributeSemantic, format: win32more.Windows.Graphics.DirectX.DirectXPixelFormat, memory: win32more.Windows.Foundation.MemoryBuffer) -> Void: ...
    Bounds = property(get_Bounds, None)
    PrimitiveTopology = property(get_PrimitiveTopology, put_PrimitiveTopology)
class ISceneMeshMaterialAttributeMap(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.ISceneMeshMaterialAttributeMap'
    _iid_ = Guid('{ce843171-3d43-4855-aa69-31ff988d049d}')
class ISceneMeshRendererComponent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.ISceneMeshRendererComponent'
    _iid_ = Guid('{9929f7e3-6364-477e-98fe-74ed9fd4c2de}')
    @winrt_commethod(6)
    def get_Material(self) -> win32more.Windows.UI.Composition.Scenes.SceneMaterial: ...
    @winrt_commethod(7)
    def put_Material(self, value: win32more.Windows.UI.Composition.Scenes.SceneMaterial) -> Void: ...
    @winrt_commethod(8)
    def get_Mesh(self) -> win32more.Windows.UI.Composition.Scenes.SceneMesh: ...
    @winrt_commethod(9)
    def put_Mesh(self, value: win32more.Windows.UI.Composition.Scenes.SceneMesh) -> Void: ...
    @winrt_commethod(10)
    def get_UVMappings(self) -> win32more.Windows.UI.Composition.Scenes.SceneMeshMaterialAttributeMap: ...
    Material = property(get_Material, put_Material)
    Mesh = property(get_Mesh, put_Mesh)
    UVMappings = property(get_UVMappings, None)
class ISceneMeshRendererComponentStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.ISceneMeshRendererComponentStatics'
    _iid_ = Guid('{4954f37a-4459-4521-bd6e-2b38b8d711ea}')
    @winrt_commethod(6)
    def Create(self, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.Scenes.SceneMeshRendererComponent: ...
class ISceneMeshStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.ISceneMeshStatics'
    _iid_ = Guid('{8412316c-7b57-473f-966b-81dc277b1751}')
    @winrt_commethod(6)
    def Create(self, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.Scenes.SceneMesh: ...
class ISceneMetallicRoughnessMaterial(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial'
    _iid_ = Guid('{c1d91446-799c-429e-a4e4-5da645f18e61}')
    @winrt_commethod(6)
    def get_BaseColorInput(self) -> win32more.Windows.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_commethod(7)
    def put_BaseColorInput(self, value: win32more.Windows.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_commethod(8)
    def get_BaseColorFactor(self) -> win32more.Windows.Foundation.Numerics.Vector4: ...
    @winrt_commethod(9)
    def put_BaseColorFactor(self, value: win32more.Windows.Foundation.Numerics.Vector4) -> Void: ...
    @winrt_commethod(10)
    def get_MetallicFactor(self) -> Single: ...
    @winrt_commethod(11)
    def put_MetallicFactor(self, value: Single) -> Void: ...
    @winrt_commethod(12)
    def get_MetallicRoughnessInput(self) -> win32more.Windows.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_commethod(13)
    def put_MetallicRoughnessInput(self, value: win32more.Windows.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_commethod(14)
    def get_RoughnessFactor(self) -> Single: ...
    @winrt_commethod(15)
    def put_RoughnessFactor(self, value: Single) -> Void: ...
    BaseColorFactor = property(get_BaseColorFactor, put_BaseColorFactor)
    BaseColorInput = property(get_BaseColorInput, put_BaseColorInput)
    MetallicFactor = property(get_MetallicFactor, put_MetallicFactor)
    MetallicRoughnessInput = property(get_MetallicRoughnessInput, put_MetallicRoughnessInput)
    RoughnessFactor = property(get_RoughnessFactor, put_RoughnessFactor)
class ISceneMetallicRoughnessMaterialStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.ISceneMetallicRoughnessMaterialStatics'
    _iid_ = Guid('{3bddca50-6d9d-4531-8dc4-b27e3e49b7ab}')
    @winrt_commethod(6)
    def Create(self, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.Scenes.SceneMetallicRoughnessMaterial: ...
class ISceneModelTransform(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.ISceneModelTransform'
    _iid_ = Guid('{c05576c2-32b1-4269-980d-b98537100ae4}')
    @winrt_commethod(6)
    def get_Orientation(self) -> win32more.Windows.Foundation.Numerics.Quaternion: ...
    @winrt_commethod(7)
    def put_Orientation(self, value: win32more.Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_commethod(8)
    def get_RotationAngle(self) -> Single: ...
    @winrt_commethod(9)
    def put_RotationAngle(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def get_RotationAngleInDegrees(self) -> Single: ...
    @winrt_commethod(11)
    def put_RotationAngleInDegrees(self, value: Single) -> Void: ...
    @winrt_commethod(12)
    def get_RotationAxis(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(13)
    def put_RotationAxis(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(14)
    def get_Scale(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(15)
    def put_Scale(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(16)
    def get_Translation(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(17)
    def put_Translation(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    Orientation = property(get_Orientation, put_Orientation)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    RotationAngleInDegrees = property(get_RotationAngleInDegrees, put_RotationAngleInDegrees)
    RotationAxis = property(get_RotationAxis, put_RotationAxis)
    Scale = property(get_Scale, put_Scale)
    Translation = property(get_Translation, put_Translation)
class ISceneNode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.ISceneNode'
    _iid_ = Guid('{acf2c247-f307-4581-9c41-af2e29c3b016}')
    @winrt_commethod(6)
    def get_Children(self) -> win32more.Windows.UI.Composition.Scenes.SceneNodeCollection: ...
    @winrt_commethod(7)
    def get_Components(self) -> win32more.Windows.UI.Composition.Scenes.SceneComponentCollection: ...
    @winrt_commethod(8)
    def get_Parent(self) -> win32more.Windows.UI.Composition.Scenes.SceneNode: ...
    @winrt_commethod(9)
    def get_Transform(self) -> win32more.Windows.UI.Composition.Scenes.SceneModelTransform: ...
    @winrt_commethod(10)
    def FindFirstComponentOfType(self, value: win32more.Windows.UI.Composition.Scenes.SceneComponentType) -> win32more.Windows.UI.Composition.Scenes.SceneComponent: ...
    Children = property(get_Children, None)
    Components = property(get_Components, None)
    Parent = property(get_Parent, None)
    Transform = property(get_Transform, None)
class ISceneNodeCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.ISceneNodeCollection'
    _iid_ = Guid('{29ada101-2dd9-4332-be63-60d2cf4269f2}')
class ISceneNodeStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.ISceneNodeStatics'
    _iid_ = Guid('{579a0faa-be9d-4210-908c-93d15feed0b7}')
    @winrt_commethod(6)
    def Create(self, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.Scenes.SceneNode: ...
class ISceneObject(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.ISceneObject'
    _iid_ = Guid('{1e94249b-0f1b-49eb-a819-877d8450005b}')
class ISceneObjectFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.ISceneObjectFactory'
    _iid_ = Guid('{14fe799a-33e4-52ef-956c-44229d21f2c1}')
class IScenePbrMaterial(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.IScenePbrMaterial'
    _iid_ = Guid('{aab6ebbe-d680-46df-8294-b6800a9f95e7}')
    @winrt_commethod(6)
    def get_AlphaCutoff(self) -> Single: ...
    @winrt_commethod(7)
    def put_AlphaCutoff(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_AlphaMode(self) -> win32more.Windows.UI.Composition.Scenes.SceneAlphaMode: ...
    @winrt_commethod(9)
    def put_AlphaMode(self, value: win32more.Windows.UI.Composition.Scenes.SceneAlphaMode) -> Void: ...
    @winrt_commethod(10)
    def get_EmissiveInput(self) -> win32more.Windows.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_commethod(11)
    def put_EmissiveInput(self, value: win32more.Windows.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_commethod(12)
    def get_EmissiveFactor(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(13)
    def put_EmissiveFactor(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(14)
    def get_IsDoubleSided(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_IsDoubleSided(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_NormalInput(self) -> win32more.Windows.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_commethod(17)
    def put_NormalInput(self, value: win32more.Windows.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_commethod(18)
    def get_NormalScale(self) -> Single: ...
    @winrt_commethod(19)
    def put_NormalScale(self, value: Single) -> Void: ...
    @winrt_commethod(20)
    def get_OcclusionInput(self) -> win32more.Windows.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_commethod(21)
    def put_OcclusionInput(self, value: win32more.Windows.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_commethod(22)
    def get_OcclusionStrength(self) -> Single: ...
    @winrt_commethod(23)
    def put_OcclusionStrength(self, value: Single) -> Void: ...
    AlphaCutoff = property(get_AlphaCutoff, put_AlphaCutoff)
    AlphaMode = property(get_AlphaMode, put_AlphaMode)
    EmissiveFactor = property(get_EmissiveFactor, put_EmissiveFactor)
    EmissiveInput = property(get_EmissiveInput, put_EmissiveInput)
    IsDoubleSided = property(get_IsDoubleSided, put_IsDoubleSided)
    NormalInput = property(get_NormalInput, put_NormalInput)
    NormalScale = property(get_NormalScale, put_NormalScale)
    OcclusionInput = property(get_OcclusionInput, put_OcclusionInput)
    OcclusionStrength = property(get_OcclusionStrength, put_OcclusionStrength)
class IScenePbrMaterialFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.IScenePbrMaterialFactory'
    _iid_ = Guid('{2e3f3dfe-0b85-5727-b5be-b7d3cbac37fa}')
class ISceneRendererComponent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.ISceneRendererComponent'
    _iid_ = Guid('{f1acb857-cf4f-4025-9b25-a2d1944cf507}')
class ISceneRendererComponentFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.ISceneRendererComponentFactory'
    _iid_ = Guid('{1db6ed6c-aa2c-5967-9035-56352dc69658}')
class ISceneSurfaceMaterialInput(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.ISceneSurfaceMaterialInput'
    _iid_ = Guid('{9937da5c-a9ca-4cfc-b3aa-088356518742}')
    @winrt_commethod(6)
    def get_BitmapInterpolationMode(self) -> win32more.Windows.UI.Composition.CompositionBitmapInterpolationMode: ...
    @winrt_commethod(7)
    def put_BitmapInterpolationMode(self, value: win32more.Windows.UI.Composition.CompositionBitmapInterpolationMode) -> Void: ...
    @winrt_commethod(8)
    def get_Surface(self) -> win32more.Windows.UI.Composition.ICompositionSurface: ...
    @winrt_commethod(9)
    def put_Surface(self, value: win32more.Windows.UI.Composition.ICompositionSurface) -> Void: ...
    @winrt_commethod(10)
    def get_WrappingUMode(self) -> win32more.Windows.UI.Composition.Scenes.SceneWrappingMode: ...
    @winrt_commethod(11)
    def put_WrappingUMode(self, value: win32more.Windows.UI.Composition.Scenes.SceneWrappingMode) -> Void: ...
    @winrt_commethod(12)
    def get_WrappingVMode(self) -> win32more.Windows.UI.Composition.Scenes.SceneWrappingMode: ...
    @winrt_commethod(13)
    def put_WrappingVMode(self, value: win32more.Windows.UI.Composition.Scenes.SceneWrappingMode) -> Void: ...
    BitmapInterpolationMode = property(get_BitmapInterpolationMode, put_BitmapInterpolationMode)
    Surface = property(get_Surface, put_Surface)
    WrappingUMode = property(get_WrappingUMode, put_WrappingUMode)
    WrappingVMode = property(get_WrappingVMode, put_WrappingVMode)
class ISceneSurfaceMaterialInputStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.ISceneSurfaceMaterialInputStatics'
    _iid_ = Guid('{5a2394d3-6429-4589-bbcf-b84f4f3cfbfe}')
    @winrt_commethod(6)
    def Create(self, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.Scenes.SceneSurfaceMaterialInput: ...
class ISceneVisual(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.ISceneVisual'
    _iid_ = Guid('{8e672c1e-d734-47b1-be14-3d694ffa4301}')
    @winrt_commethod(6)
    def get_Root(self) -> win32more.Windows.UI.Composition.Scenes.SceneNode: ...
    @winrt_commethod(7)
    def put_Root(self, value: win32more.Windows.UI.Composition.Scenes.SceneNode) -> Void: ...
    Root = property(get_Root, put_Root)
class ISceneVisualStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Scenes.ISceneVisualStatics'
    _iid_ = Guid('{b8347e9a-50aa-4527-8d34-de4cb8ea88b4}')
    @winrt_commethod(6)
    def Create(self, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.Scenes.SceneVisual: ...
class SceneAlphaMode(Enum, Int32):
    Opaque = 0
    AlphaTest = 1
    Blend = 2
class SceneAttributeSemantic(Enum, Int32):
    Index = 0
    Vertex = 1
    Normal = 2
    TexCoord0 = 3
    TexCoord1 = 4
    Color = 5
    Tangent = 6
class SceneBoundingBox(ComPtr):
    extends: win32more.Windows.UI.Composition.Scenes.SceneObject
    default_interface: win32more.Windows.UI.Composition.Scenes.ISceneBoundingBox
    _classid_ = 'Windows.UI.Composition.Scenes.SceneBoundingBox'
    @winrt_mixinmethod
    def get_Center(self: win32more.Windows.UI.Composition.Scenes.ISceneBoundingBox) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_Extents(self: win32more.Windows.UI.Composition.Scenes.ISceneBoundingBox) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_Max(self: win32more.Windows.UI.Composition.Scenes.ISceneBoundingBox) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_Min(self: win32more.Windows.UI.Composition.Scenes.ISceneBoundingBox) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.UI.Composition.Scenes.ISceneBoundingBox) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    Center = property(get_Center, None)
    Extents = property(get_Extents, None)
    Max = property(get_Max, None)
    Min = property(get_Min, None)
    Size = property(get_Size, None)
class SceneComponent(ComPtr):
    extends: win32more.Windows.UI.Composition.Scenes.SceneObject
    default_interface: win32more.Windows.UI.Composition.Scenes.ISceneComponent
    _classid_ = 'Windows.UI.Composition.Scenes.SceneComponent'
    @winrt_mixinmethod
    def get_ComponentType(self: win32more.Windows.UI.Composition.Scenes.ISceneComponent) -> win32more.Windows.UI.Composition.Scenes.SceneComponentType: ...
    ComponentType = property(get_ComponentType, None)
class SceneComponentCollection(ComPtr):
    extends: win32more.Windows.UI.Composition.Scenes.SceneObject
    implements: Tuple[SequenceProtocol[win32more.Windows.UI.Composition.Scenes.SceneComponent]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.Scenes.SceneComponent]
    _classid_ = 'Windows.UI.Composition.Scenes.SceneComponentCollection'
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.Scenes.SceneComponent], index: UInt32) -> win32more.Windows.UI.Composition.Scenes.SceneComponent: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.Scenes.SceneComponent]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.Scenes.SceneComponent]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Composition.Scenes.SceneComponent]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.Scenes.SceneComponent], value: win32more.Windows.UI.Composition.Scenes.SceneComponent, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.Scenes.SceneComponent], index: UInt32, value: win32more.Windows.UI.Composition.Scenes.SceneComponent) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.Scenes.SceneComponent], index: UInt32, value: win32more.Windows.UI.Composition.Scenes.SceneComponent) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.Scenes.SceneComponent], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.Scenes.SceneComponent], value: win32more.Windows.UI.Composition.Scenes.SceneComponent) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.Scenes.SceneComponent]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.Scenes.SceneComponent]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.Scenes.SceneComponent], startIndex: UInt32, items: FillArray[win32more.Windows.UI.Composition.Scenes.SceneComponent]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.Scenes.SceneComponent], items: PassArray[win32more.Windows.UI.Composition.Scenes.SceneComponent]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.Scenes.SceneComponent]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Composition.Scenes.SceneComponent]: ...
    Size = property(get_Size, None)
class SceneComponentType(Enum, Int32):
    MeshRendererComponent = 0
class SceneMaterial(ComPtr):
    extends: win32more.Windows.UI.Composition.Scenes.SceneObject
    default_interface: win32more.Windows.UI.Composition.Scenes.ISceneMaterial
    _classid_ = 'Windows.UI.Composition.Scenes.SceneMaterial'
class SceneMaterialInput(ComPtr):
    extends: win32more.Windows.UI.Composition.Scenes.SceneObject
    default_interface: win32more.Windows.UI.Composition.Scenes.ISceneMaterialInput
    _classid_ = 'Windows.UI.Composition.Scenes.SceneMaterialInput'
class SceneMesh(ComPtr):
    extends: win32more.Windows.UI.Composition.Scenes.SceneObject
    default_interface: win32more.Windows.UI.Composition.Scenes.ISceneMesh
    _classid_ = 'Windows.UI.Composition.Scenes.SceneMesh'
    @winrt_mixinmethod
    def get_Bounds(self: win32more.Windows.UI.Composition.Scenes.ISceneMesh) -> win32more.Windows.UI.Composition.Scenes.SceneBoundingBox: ...
    @winrt_mixinmethod
    def get_PrimitiveTopology(self: win32more.Windows.UI.Composition.Scenes.ISceneMesh) -> win32more.Windows.Graphics.DirectX.DirectXPrimitiveTopology: ...
    @winrt_mixinmethod
    def put_PrimitiveTopology(self: win32more.Windows.UI.Composition.Scenes.ISceneMesh, value: win32more.Windows.Graphics.DirectX.DirectXPrimitiveTopology) -> Void: ...
    @winrt_mixinmethod
    def FillMeshAttribute(self: win32more.Windows.UI.Composition.Scenes.ISceneMesh, semantic: win32more.Windows.UI.Composition.Scenes.SceneAttributeSemantic, format: win32more.Windows.Graphics.DirectX.DirectXPixelFormat, memory: win32more.Windows.Foundation.MemoryBuffer) -> Void: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.UI.Composition.Scenes.ISceneMeshStatics, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.Scenes.SceneMesh: ...
    Bounds = property(get_Bounds, None)
    PrimitiveTopology = property(get_PrimitiveTopology, put_PrimitiveTopology)
class SceneMeshMaterialAttributeMap(ComPtr):
    extends: win32more.Windows.UI.Composition.Scenes.SceneObject
    implements: Tuple[MappingProtocol[WinRT_String, win32more.Windows.UI.Composition.Scenes.SceneAttributeSemantic]]
    default_interface: win32more.Windows.UI.Composition.Scenes.ISceneMeshMaterialAttributeMap
    _classid_ = 'Windows.UI.Composition.Scenes.SceneMeshMaterialAttributeMap'
    @winrt_mixinmethod
    def Lookup(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.UI.Composition.Scenes.SceneAttributeSemantic], key: WinRT_String) -> win32more.Windows.UI.Composition.Scenes.SceneAttributeSemantic: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.UI.Composition.Scenes.SceneAttributeSemantic]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.UI.Composition.Scenes.SceneAttributeSemantic], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.UI.Composition.Scenes.SceneAttributeSemantic]) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.UI.Composition.Scenes.SceneAttributeSemantic]: ...
    @winrt_mixinmethod
    def Insert(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.UI.Composition.Scenes.SceneAttributeSemantic], key: WinRT_String, value: win32more.Windows.UI.Composition.Scenes.SceneAttributeSemantic) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.UI.Composition.Scenes.SceneAttributeSemantic], key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.UI.Composition.Scenes.SceneAttributeSemantic]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.UI.Composition.Scenes.SceneAttributeSemantic]]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.UI.Composition.Scenes.SceneAttributeSemantic]]: ...
    Size = property(get_Size, None)
class SceneMeshRendererComponent(ComPtr):
    extends: win32more.Windows.UI.Composition.Scenes.SceneRendererComponent
    default_interface: win32more.Windows.UI.Composition.Scenes.ISceneMeshRendererComponent
    _classid_ = 'Windows.UI.Composition.Scenes.SceneMeshRendererComponent'
    @winrt_mixinmethod
    def get_Material(self: win32more.Windows.UI.Composition.Scenes.ISceneMeshRendererComponent) -> win32more.Windows.UI.Composition.Scenes.SceneMaterial: ...
    @winrt_mixinmethod
    def put_Material(self: win32more.Windows.UI.Composition.Scenes.ISceneMeshRendererComponent, value: win32more.Windows.UI.Composition.Scenes.SceneMaterial) -> Void: ...
    @winrt_mixinmethod
    def get_Mesh(self: win32more.Windows.UI.Composition.Scenes.ISceneMeshRendererComponent) -> win32more.Windows.UI.Composition.Scenes.SceneMesh: ...
    @winrt_mixinmethod
    def put_Mesh(self: win32more.Windows.UI.Composition.Scenes.ISceneMeshRendererComponent, value: win32more.Windows.UI.Composition.Scenes.SceneMesh) -> Void: ...
    @winrt_mixinmethod
    def get_UVMappings(self: win32more.Windows.UI.Composition.Scenes.ISceneMeshRendererComponent) -> win32more.Windows.UI.Composition.Scenes.SceneMeshMaterialAttributeMap: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.UI.Composition.Scenes.ISceneMeshRendererComponentStatics, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.Scenes.SceneMeshRendererComponent: ...
    Material = property(get_Material, put_Material)
    Mesh = property(get_Mesh, put_Mesh)
    UVMappings = property(get_UVMappings, None)
class SceneMetallicRoughnessMaterial(ComPtr):
    extends: win32more.Windows.UI.Composition.Scenes.ScenePbrMaterial
    default_interface: win32more.Windows.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial
    _classid_ = 'Windows.UI.Composition.Scenes.SceneMetallicRoughnessMaterial'
    @winrt_mixinmethod
    def get_BaseColorInput(self: win32more.Windows.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial) -> win32more.Windows.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_mixinmethod
    def put_BaseColorInput(self: win32more.Windows.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial, value: win32more.Windows.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_mixinmethod
    def get_BaseColorFactor(self: win32more.Windows.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial) -> win32more.Windows.Foundation.Numerics.Vector4: ...
    @winrt_mixinmethod
    def put_BaseColorFactor(self: win32more.Windows.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial, value: win32more.Windows.Foundation.Numerics.Vector4) -> Void: ...
    @winrt_mixinmethod
    def get_MetallicFactor(self: win32more.Windows.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial) -> Single: ...
    @winrt_mixinmethod
    def put_MetallicFactor(self: win32more.Windows.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_MetallicRoughnessInput(self: win32more.Windows.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial) -> win32more.Windows.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_mixinmethod
    def put_MetallicRoughnessInput(self: win32more.Windows.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial, value: win32more.Windows.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_mixinmethod
    def get_RoughnessFactor(self: win32more.Windows.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial) -> Single: ...
    @winrt_mixinmethod
    def put_RoughnessFactor(self: win32more.Windows.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial, value: Single) -> Void: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.UI.Composition.Scenes.ISceneMetallicRoughnessMaterialStatics, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.Scenes.SceneMetallicRoughnessMaterial: ...
    BaseColorFactor = property(get_BaseColorFactor, put_BaseColorFactor)
    BaseColorInput = property(get_BaseColorInput, put_BaseColorInput)
    MetallicFactor = property(get_MetallicFactor, put_MetallicFactor)
    MetallicRoughnessInput = property(get_MetallicRoughnessInput, put_MetallicRoughnessInput)
    RoughnessFactor = property(get_RoughnessFactor, put_RoughnessFactor)
class SceneModelTransform(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionTransform
    default_interface: win32more.Windows.UI.Composition.Scenes.ISceneModelTransform
    _classid_ = 'Windows.UI.Composition.Scenes.SceneModelTransform'
    @winrt_mixinmethod
    def get_Orientation(self: win32more.Windows.UI.Composition.Scenes.ISceneModelTransform) -> win32more.Windows.Foundation.Numerics.Quaternion: ...
    @winrt_mixinmethod
    def put_Orientation(self: win32more.Windows.UI.Composition.Scenes.ISceneModelTransform, value: win32more.Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAngle(self: win32more.Windows.UI.Composition.Scenes.ISceneModelTransform) -> Single: ...
    @winrt_mixinmethod
    def put_RotationAngle(self: win32more.Windows.UI.Composition.Scenes.ISceneModelTransform, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAngleInDegrees(self: win32more.Windows.UI.Composition.Scenes.ISceneModelTransform) -> Single: ...
    @winrt_mixinmethod
    def put_RotationAngleInDegrees(self: win32more.Windows.UI.Composition.Scenes.ISceneModelTransform, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAxis(self: win32more.Windows.UI.Composition.Scenes.ISceneModelTransform) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_RotationAxis(self: win32more.Windows.UI.Composition.Scenes.ISceneModelTransform, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_Scale(self: win32more.Windows.UI.Composition.Scenes.ISceneModelTransform) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Scale(self: win32more.Windows.UI.Composition.Scenes.ISceneModelTransform, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_Translation(self: win32more.Windows.UI.Composition.Scenes.ISceneModelTransform) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Translation(self: win32more.Windows.UI.Composition.Scenes.ISceneModelTransform, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    Orientation = property(get_Orientation, put_Orientation)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    RotationAngleInDegrees = property(get_RotationAngleInDegrees, put_RotationAngleInDegrees)
    RotationAxis = property(get_RotationAxis, put_RotationAxis)
    Scale = property(get_Scale, put_Scale)
    Translation = property(get_Translation, put_Translation)
class SceneNode(ComPtr):
    extends: win32more.Windows.UI.Composition.Scenes.SceneObject
    default_interface: win32more.Windows.UI.Composition.Scenes.ISceneNode
    _classid_ = 'Windows.UI.Composition.Scenes.SceneNode'
    @winrt_mixinmethod
    def get_Children(self: win32more.Windows.UI.Composition.Scenes.ISceneNode) -> win32more.Windows.UI.Composition.Scenes.SceneNodeCollection: ...
    @winrt_mixinmethod
    def get_Components(self: win32more.Windows.UI.Composition.Scenes.ISceneNode) -> win32more.Windows.UI.Composition.Scenes.SceneComponentCollection: ...
    @winrt_mixinmethod
    def get_Parent(self: win32more.Windows.UI.Composition.Scenes.ISceneNode) -> win32more.Windows.UI.Composition.Scenes.SceneNode: ...
    @winrt_mixinmethod
    def get_Transform(self: win32more.Windows.UI.Composition.Scenes.ISceneNode) -> win32more.Windows.UI.Composition.Scenes.SceneModelTransform: ...
    @winrt_mixinmethod
    def FindFirstComponentOfType(self: win32more.Windows.UI.Composition.Scenes.ISceneNode, value: win32more.Windows.UI.Composition.Scenes.SceneComponentType) -> win32more.Windows.UI.Composition.Scenes.SceneComponent: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.UI.Composition.Scenes.ISceneNodeStatics, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.Scenes.SceneNode: ...
    Children = property(get_Children, None)
    Components = property(get_Components, None)
    Parent = property(get_Parent, None)
    Transform = property(get_Transform, None)
class SceneNodeCollection(ComPtr):
    extends: win32more.Windows.UI.Composition.Scenes.SceneObject
    implements: Tuple[SequenceProtocol[win32more.Windows.UI.Composition.Scenes.SceneNode]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.Scenes.SceneNode]
    _classid_ = 'Windows.UI.Composition.Scenes.SceneNodeCollection'
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.Scenes.SceneNode], index: UInt32) -> win32more.Windows.UI.Composition.Scenes.SceneNode: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.Scenes.SceneNode]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.Scenes.SceneNode]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Composition.Scenes.SceneNode]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.Scenes.SceneNode], value: win32more.Windows.UI.Composition.Scenes.SceneNode, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.Scenes.SceneNode], index: UInt32, value: win32more.Windows.UI.Composition.Scenes.SceneNode) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.Scenes.SceneNode], index: UInt32, value: win32more.Windows.UI.Composition.Scenes.SceneNode) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.Scenes.SceneNode], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.Scenes.SceneNode], value: win32more.Windows.UI.Composition.Scenes.SceneNode) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.Scenes.SceneNode]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.Scenes.SceneNode]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.Scenes.SceneNode], startIndex: UInt32, items: FillArray[win32more.Windows.UI.Composition.Scenes.SceneNode]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Composition.Scenes.SceneNode], items: PassArray[win32more.Windows.UI.Composition.Scenes.SceneNode]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Composition.Scenes.SceneNode]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Composition.Scenes.SceneNode]: ...
    Size = property(get_Size, None)
class SceneObject(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionObject
    default_interface: win32more.Windows.UI.Composition.Scenes.ISceneObject
    _classid_ = 'Windows.UI.Composition.Scenes.SceneObject'
class ScenePbrMaterial(ComPtr):
    extends: win32more.Windows.UI.Composition.Scenes.SceneMaterial
    default_interface: win32more.Windows.UI.Composition.Scenes.IScenePbrMaterial
    _classid_ = 'Windows.UI.Composition.Scenes.ScenePbrMaterial'
    @winrt_mixinmethod
    def get_AlphaCutoff(self: win32more.Windows.UI.Composition.Scenes.IScenePbrMaterial) -> Single: ...
    @winrt_mixinmethod
    def put_AlphaCutoff(self: win32more.Windows.UI.Composition.Scenes.IScenePbrMaterial, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_AlphaMode(self: win32more.Windows.UI.Composition.Scenes.IScenePbrMaterial) -> win32more.Windows.UI.Composition.Scenes.SceneAlphaMode: ...
    @winrt_mixinmethod
    def put_AlphaMode(self: win32more.Windows.UI.Composition.Scenes.IScenePbrMaterial, value: win32more.Windows.UI.Composition.Scenes.SceneAlphaMode) -> Void: ...
    @winrt_mixinmethod
    def get_EmissiveInput(self: win32more.Windows.UI.Composition.Scenes.IScenePbrMaterial) -> win32more.Windows.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_mixinmethod
    def put_EmissiveInput(self: win32more.Windows.UI.Composition.Scenes.IScenePbrMaterial, value: win32more.Windows.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_mixinmethod
    def get_EmissiveFactor(self: win32more.Windows.UI.Composition.Scenes.IScenePbrMaterial) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_EmissiveFactor(self: win32more.Windows.UI.Composition.Scenes.IScenePbrMaterial, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_IsDoubleSided(self: win32more.Windows.UI.Composition.Scenes.IScenePbrMaterial) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsDoubleSided(self: win32more.Windows.UI.Composition.Scenes.IScenePbrMaterial, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_NormalInput(self: win32more.Windows.UI.Composition.Scenes.IScenePbrMaterial) -> win32more.Windows.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_mixinmethod
    def put_NormalInput(self: win32more.Windows.UI.Composition.Scenes.IScenePbrMaterial, value: win32more.Windows.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_mixinmethod
    def get_NormalScale(self: win32more.Windows.UI.Composition.Scenes.IScenePbrMaterial) -> Single: ...
    @winrt_mixinmethod
    def put_NormalScale(self: win32more.Windows.UI.Composition.Scenes.IScenePbrMaterial, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_OcclusionInput(self: win32more.Windows.UI.Composition.Scenes.IScenePbrMaterial) -> win32more.Windows.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_mixinmethod
    def put_OcclusionInput(self: win32more.Windows.UI.Composition.Scenes.IScenePbrMaterial, value: win32more.Windows.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_mixinmethod
    def get_OcclusionStrength(self: win32more.Windows.UI.Composition.Scenes.IScenePbrMaterial) -> Single: ...
    @winrt_mixinmethod
    def put_OcclusionStrength(self: win32more.Windows.UI.Composition.Scenes.IScenePbrMaterial, value: Single) -> Void: ...
    AlphaCutoff = property(get_AlphaCutoff, put_AlphaCutoff)
    AlphaMode = property(get_AlphaMode, put_AlphaMode)
    EmissiveFactor = property(get_EmissiveFactor, put_EmissiveFactor)
    EmissiveInput = property(get_EmissiveInput, put_EmissiveInput)
    IsDoubleSided = property(get_IsDoubleSided, put_IsDoubleSided)
    NormalInput = property(get_NormalInput, put_NormalInput)
    NormalScale = property(get_NormalScale, put_NormalScale)
    OcclusionInput = property(get_OcclusionInput, put_OcclusionInput)
    OcclusionStrength = property(get_OcclusionStrength, put_OcclusionStrength)
class SceneRendererComponent(ComPtr):
    extends: win32more.Windows.UI.Composition.Scenes.SceneComponent
    default_interface: win32more.Windows.UI.Composition.Scenes.ISceneRendererComponent
    _classid_ = 'Windows.UI.Composition.Scenes.SceneRendererComponent'
class SceneSurfaceMaterialInput(ComPtr):
    extends: win32more.Windows.UI.Composition.Scenes.SceneMaterialInput
    default_interface: win32more.Windows.UI.Composition.Scenes.ISceneSurfaceMaterialInput
    _classid_ = 'Windows.UI.Composition.Scenes.SceneSurfaceMaterialInput'
    @winrt_mixinmethod
    def get_BitmapInterpolationMode(self: win32more.Windows.UI.Composition.Scenes.ISceneSurfaceMaterialInput) -> win32more.Windows.UI.Composition.CompositionBitmapInterpolationMode: ...
    @winrt_mixinmethod
    def put_BitmapInterpolationMode(self: win32more.Windows.UI.Composition.Scenes.ISceneSurfaceMaterialInput, value: win32more.Windows.UI.Composition.CompositionBitmapInterpolationMode) -> Void: ...
    @winrt_mixinmethod
    def get_Surface(self: win32more.Windows.UI.Composition.Scenes.ISceneSurfaceMaterialInput) -> win32more.Windows.UI.Composition.ICompositionSurface: ...
    @winrt_mixinmethod
    def put_Surface(self: win32more.Windows.UI.Composition.Scenes.ISceneSurfaceMaterialInput, value: win32more.Windows.UI.Composition.ICompositionSurface) -> Void: ...
    @winrt_mixinmethod
    def get_WrappingUMode(self: win32more.Windows.UI.Composition.Scenes.ISceneSurfaceMaterialInput) -> win32more.Windows.UI.Composition.Scenes.SceneWrappingMode: ...
    @winrt_mixinmethod
    def put_WrappingUMode(self: win32more.Windows.UI.Composition.Scenes.ISceneSurfaceMaterialInput, value: win32more.Windows.UI.Composition.Scenes.SceneWrappingMode) -> Void: ...
    @winrt_mixinmethod
    def get_WrappingVMode(self: win32more.Windows.UI.Composition.Scenes.ISceneSurfaceMaterialInput) -> win32more.Windows.UI.Composition.Scenes.SceneWrappingMode: ...
    @winrt_mixinmethod
    def put_WrappingVMode(self: win32more.Windows.UI.Composition.Scenes.ISceneSurfaceMaterialInput, value: win32more.Windows.UI.Composition.Scenes.SceneWrappingMode) -> Void: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.UI.Composition.Scenes.ISceneSurfaceMaterialInputStatics, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.Scenes.SceneSurfaceMaterialInput: ...
    BitmapInterpolationMode = property(get_BitmapInterpolationMode, put_BitmapInterpolationMode)
    Surface = property(get_Surface, put_Surface)
    WrappingUMode = property(get_WrappingUMode, put_WrappingUMode)
    WrappingVMode = property(get_WrappingVMode, put_WrappingVMode)
class SceneVisual(ComPtr):
    extends: win32more.Windows.UI.Composition.ContainerVisual
    default_interface: win32more.Windows.UI.Composition.Scenes.ISceneVisual
    _classid_ = 'Windows.UI.Composition.Scenes.SceneVisual'
    @winrt_mixinmethod
    def get_Root(self: win32more.Windows.UI.Composition.Scenes.ISceneVisual) -> win32more.Windows.UI.Composition.Scenes.SceneNode: ...
    @winrt_mixinmethod
    def put_Root(self: win32more.Windows.UI.Composition.Scenes.ISceneVisual, value: win32more.Windows.UI.Composition.Scenes.SceneNode) -> Void: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.UI.Composition.Scenes.ISceneVisualStatics, compositor: win32more.Windows.UI.Composition.Compositor) -> win32more.Windows.UI.Composition.Scenes.SceneVisual: ...
    Root = property(get_Root, put_Root)
class SceneWrappingMode(Enum, Int32):
    ClampToEdge = 0
    MirroredRepeat = 1
    Repeat = 2


make_ready(__name__)
