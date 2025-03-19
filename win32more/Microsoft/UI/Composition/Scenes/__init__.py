from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.Graphics.DirectX
import win32more.Microsoft.UI.Composition
import win32more.Microsoft.UI.Composition.Scenes
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Foundation.Numerics
import win32more.Windows.Win32.System.WinRT
class ISceneBoundingBox(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Scenes.ISceneBoundingBox'
    _iid_ = Guid('{39fb48e0-216a-5608-9186-6ba9f98b5c67}')
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
    _classid_ = 'Microsoft.UI.Composition.Scenes.ISceneComponent'
    _iid_ = Guid('{f73361cb-8027-50e2-98ee-b2e3ea050a54}')
    @winrt_commethod(6)
    def get_ComponentType(self) -> win32more.Microsoft.UI.Composition.Scenes.SceneComponentType: ...
    ComponentType = property(get_ComponentType, None)
class ISceneComponentCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Scenes.ISceneComponentCollection'
    _iid_ = Guid('{e4b21c71-87e2-5aeb-85be-884e8302273e}')
class ISceneComponentFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Scenes.ISceneComponentFactory'
    _iid_ = Guid('{254088b0-babf-503d-9a66-0d86af5f7303}')
class ISceneMaterial(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Scenes.ISceneMaterial'
    _iid_ = Guid('{042142a7-bf6b-57ad-badc-f581f38edb48}')
class ISceneMaterialFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Scenes.ISceneMaterialFactory'
    _iid_ = Guid('{25747893-8748-5f60-969f-318fa0b735ca}')
class ISceneMaterialInput(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Scenes.ISceneMaterialInput'
    _iid_ = Guid('{446bdade-719b-5db4-b699-f226d0062a2e}')
class ISceneMaterialInputFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Scenes.ISceneMaterialInputFactory'
    _iid_ = Guid('{b4dabd1d-58c0-5710-928a-bc49b0735694}')
class ISceneMesh(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Scenes.ISceneMesh'
    _iid_ = Guid('{5cf846aa-f53f-555e-a3ad-f5bc52ca32fb}')
    @winrt_commethod(6)
    def get_Bounds(self) -> win32more.Microsoft.UI.Composition.Scenes.SceneBoundingBox: ...
    @winrt_commethod(7)
    def get_PrimitiveTopology(self) -> win32more.Microsoft.Graphics.DirectX.DirectXPrimitiveTopology: ...
    @winrt_commethod(8)
    def put_PrimitiveTopology(self, value: win32more.Microsoft.Graphics.DirectX.DirectXPrimitiveTopology) -> Void: ...
    @winrt_commethod(9)
    def FillMeshAttribute(self, semantic: win32more.Microsoft.UI.Composition.Scenes.SceneAttributeSemantic, format: win32more.Microsoft.Graphics.DirectX.DirectXPixelFormat, memory: win32more.Windows.Foundation.MemoryBuffer) -> Void: ...
    Bounds = property(get_Bounds, None)
    PrimitiveTopology = property(get_PrimitiveTopology, put_PrimitiveTopology)
class ISceneMeshMaterialAttributeMap(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Scenes.ISceneMeshMaterialAttributeMap'
    _iid_ = Guid('{2360c457-edae-5660-bedc-89096582ed70}')
class ISceneMeshRendererComponent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Scenes.ISceneMeshRendererComponent'
    _iid_ = Guid('{d2be85a0-70a8-5c62-84d8-8ba55e4c64a9}')
    @winrt_commethod(6)
    def get_Material(self) -> win32more.Microsoft.UI.Composition.Scenes.SceneMaterial: ...
    @winrt_commethod(7)
    def put_Material(self, value: win32more.Microsoft.UI.Composition.Scenes.SceneMaterial) -> Void: ...
    @winrt_commethod(8)
    def get_Mesh(self) -> win32more.Microsoft.UI.Composition.Scenes.SceneMesh: ...
    @winrt_commethod(9)
    def put_Mesh(self, value: win32more.Microsoft.UI.Composition.Scenes.SceneMesh) -> Void: ...
    @winrt_commethod(10)
    def get_UVMappings(self) -> win32more.Microsoft.UI.Composition.Scenes.SceneMeshMaterialAttributeMap: ...
    Material = property(get_Material, put_Material)
    Mesh = property(get_Mesh, put_Mesh)
    UVMappings = property(get_UVMappings, None)
class ISceneMeshRendererComponentStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Scenes.ISceneMeshRendererComponentStatics'
    _iid_ = Guid('{c54f8c5a-a104-5cfa-89dc-13edaa6e3d88}')
    @winrt_commethod(6)
    def Create(self, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Scenes.SceneMeshRendererComponent: ...
class ISceneMeshStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Scenes.ISceneMeshStatics'
    _iid_ = Guid('{29c52125-964b-5315-80f9-3893713290f5}')
    @winrt_commethod(6)
    def Create(self, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Scenes.SceneMesh: ...
class ISceneMetallicRoughnessMaterial(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial'
    _iid_ = Guid('{0a4afcf4-7bae-5702-9b85-8bc849f39987}')
    @winrt_commethod(6)
    def get_BaseColorInput(self) -> win32more.Microsoft.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_commethod(7)
    def put_BaseColorInput(self, value: win32more.Microsoft.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_commethod(8)
    def get_BaseColorFactor(self) -> win32more.Windows.Foundation.Numerics.Vector4: ...
    @winrt_commethod(9)
    def put_BaseColorFactor(self, value: win32more.Windows.Foundation.Numerics.Vector4) -> Void: ...
    @winrt_commethod(10)
    def get_MetallicFactor(self) -> Single: ...
    @winrt_commethod(11)
    def put_MetallicFactor(self, value: Single) -> Void: ...
    @winrt_commethod(12)
    def get_MetallicRoughnessInput(self) -> win32more.Microsoft.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_commethod(13)
    def put_MetallicRoughnessInput(self, value: win32more.Microsoft.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
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
    _classid_ = 'Microsoft.UI.Composition.Scenes.ISceneMetallicRoughnessMaterialStatics'
    _iid_ = Guid('{dffd2043-ab3c-57a0-8e13-6f09725e970f}')
    @winrt_commethod(6)
    def Create(self, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Scenes.SceneMetallicRoughnessMaterial: ...
class ISceneModelTransform(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Scenes.ISceneModelTransform'
    _iid_ = Guid('{3f05555f-0f67-576e-9d8a-93c1f250c29f}')
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
    _classid_ = 'Microsoft.UI.Composition.Scenes.ISceneNode'
    _iid_ = Guid('{a1bce140-79c2-59e6-9b68-63b1bab0e2a6}')
    @winrt_commethod(6)
    def get_Children(self) -> win32more.Microsoft.UI.Composition.Scenes.SceneNodeCollection: ...
    @winrt_commethod(7)
    def get_Components(self) -> win32more.Microsoft.UI.Composition.Scenes.SceneComponentCollection: ...
    @winrt_commethod(8)
    def get_Parent(self) -> win32more.Microsoft.UI.Composition.Scenes.SceneNode: ...
    @winrt_commethod(9)
    def get_Transform(self) -> win32more.Microsoft.UI.Composition.Scenes.SceneModelTransform: ...
    @winrt_commethod(10)
    def FindFirstComponentOfType(self, value: win32more.Microsoft.UI.Composition.Scenes.SceneComponentType) -> win32more.Microsoft.UI.Composition.Scenes.SceneComponent: ...
    Children = property(get_Children, None)
    Components = property(get_Components, None)
    Parent = property(get_Parent, None)
    Transform = property(get_Transform, None)
class ISceneNodeCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Scenes.ISceneNodeCollection'
    _iid_ = Guid('{f219b68e-5666-5c6c-aa4e-08db07fd6bcf}')
class ISceneNodeStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Scenes.ISceneNodeStatics'
    _iid_ = Guid('{801c4394-4198-5da1-ac39-6e8a44b5ce57}')
    @winrt_commethod(6)
    def Create(self, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Scenes.SceneNode: ...
class ISceneObject(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Scenes.ISceneObject'
    _iid_ = Guid('{4333e514-4fc7-521e-8bca-11c51fbcaf1e}')
class ISceneObjectFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Scenes.ISceneObjectFactory'
    _iid_ = Guid('{ee797f7d-77db-5c4c-b6f5-c1930fad85c5}')
class IScenePbrMaterial(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Scenes.IScenePbrMaterial'
    _iid_ = Guid('{295d0725-56fe-5954-8057-3f4ca7515b36}')
    @winrt_commethod(6)
    def get_AlphaCutoff(self) -> Single: ...
    @winrt_commethod(7)
    def put_AlphaCutoff(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_AlphaMode(self) -> win32more.Microsoft.UI.Composition.Scenes.SceneAlphaMode: ...
    @winrt_commethod(9)
    def put_AlphaMode(self, value: win32more.Microsoft.UI.Composition.Scenes.SceneAlphaMode) -> Void: ...
    @winrt_commethod(10)
    def get_EmissiveInput(self) -> win32more.Microsoft.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_commethod(11)
    def put_EmissiveInput(self, value: win32more.Microsoft.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_commethod(12)
    def get_EmissiveFactor(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(13)
    def put_EmissiveFactor(self, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(14)
    def get_IsDoubleSided(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_IsDoubleSided(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_NormalInput(self) -> win32more.Microsoft.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_commethod(17)
    def put_NormalInput(self, value: win32more.Microsoft.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_commethod(18)
    def get_NormalScale(self) -> Single: ...
    @winrt_commethod(19)
    def put_NormalScale(self, value: Single) -> Void: ...
    @winrt_commethod(20)
    def get_OcclusionInput(self) -> win32more.Microsoft.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_commethod(21)
    def put_OcclusionInput(self, value: win32more.Microsoft.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
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
    _classid_ = 'Microsoft.UI.Composition.Scenes.IScenePbrMaterialFactory'
    _iid_ = Guid('{9e34d32a-e30c-51f5-84ac-6467950605ca}')
class ISceneRendererComponent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Scenes.ISceneRendererComponent'
    _iid_ = Guid('{6bab8030-89c1-5dbc-a48e-1805ddf9cdd1}')
class ISceneRendererComponentFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Scenes.ISceneRendererComponentFactory'
    _iid_ = Guid('{3ccac1d6-6a0f-582e-bb1a-10ebc1e405ca}')
class ISceneSurfaceMaterialInput(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Scenes.ISceneSurfaceMaterialInput'
    _iid_ = Guid('{b9854b4f-286c-50cd-a734-491a251d5fd3}')
    @winrt_commethod(6)
    def get_BitmapInterpolationMode(self) -> win32more.Microsoft.UI.Composition.CompositionBitmapInterpolationMode: ...
    @winrt_commethod(7)
    def put_BitmapInterpolationMode(self, value: win32more.Microsoft.UI.Composition.CompositionBitmapInterpolationMode) -> Void: ...
    @winrt_commethod(8)
    def get_Surface(self) -> win32more.Microsoft.UI.Composition.ICompositionSurface: ...
    @winrt_commethod(9)
    def put_Surface(self, value: win32more.Microsoft.UI.Composition.ICompositionSurface) -> Void: ...
    @winrt_commethod(10)
    def get_WrappingUMode(self) -> win32more.Microsoft.UI.Composition.Scenes.SceneWrappingMode: ...
    @winrt_commethod(11)
    def put_WrappingUMode(self, value: win32more.Microsoft.UI.Composition.Scenes.SceneWrappingMode) -> Void: ...
    @winrt_commethod(12)
    def get_WrappingVMode(self) -> win32more.Microsoft.UI.Composition.Scenes.SceneWrappingMode: ...
    @winrt_commethod(13)
    def put_WrappingVMode(self, value: win32more.Microsoft.UI.Composition.Scenes.SceneWrappingMode) -> Void: ...
    BitmapInterpolationMode = property(get_BitmapInterpolationMode, put_BitmapInterpolationMode)
    Surface = property(get_Surface, put_Surface)
    WrappingUMode = property(get_WrappingUMode, put_WrappingUMode)
    WrappingVMode = property(get_WrappingVMode, put_WrappingVMode)
class ISceneSurfaceMaterialInputStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Scenes.ISceneSurfaceMaterialInputStatics'
    _iid_ = Guid('{8e1ba937-ad60-51bc-8256-ca62c4b2ae92}')
    @winrt_commethod(6)
    def Create(self, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Scenes.SceneSurfaceMaterialInput: ...
class ISceneVisual(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Scenes.ISceneVisual'
    _iid_ = Guid('{0144d7ad-6a7d-59cb-a0f9-74a04e85352c}')
    @winrt_commethod(6)
    def get_Root(self) -> win32more.Microsoft.UI.Composition.Scenes.SceneNode: ...
    @winrt_commethod(7)
    def put_Root(self, value: win32more.Microsoft.UI.Composition.Scenes.SceneNode) -> Void: ...
    Root = property(get_Root, put_Root)
class ISceneVisualStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Scenes.ISceneVisualStatics'
    _iid_ = Guid('{7b8da6d1-5bd8-5095-9264-e5572653ea07}')
    @winrt_commethod(6)
    def Create(self, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Scenes.SceneVisual: ...
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
    extends: win32more.Microsoft.UI.Composition.Scenes.SceneObject
    default_interface: win32more.Microsoft.UI.Composition.Scenes.ISceneBoundingBox
    _classid_ = 'Microsoft.UI.Composition.Scenes.SceneBoundingBox'
    @winrt_mixinmethod
    def get_Center(self: win32more.Microsoft.UI.Composition.Scenes.ISceneBoundingBox) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_Extents(self: win32more.Microsoft.UI.Composition.Scenes.ISceneBoundingBox) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_Max(self: win32more.Microsoft.UI.Composition.Scenes.ISceneBoundingBox) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_Min(self: win32more.Microsoft.UI.Composition.Scenes.ISceneBoundingBox) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Microsoft.UI.Composition.Scenes.ISceneBoundingBox) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    Center = property(get_Center, None)
    Extents = property(get_Extents, None)
    Max = property(get_Max, None)
    Min = property(get_Min, None)
    Size = property(get_Size, None)
class SceneComponent(ComPtr):
    extends: win32more.Microsoft.UI.Composition.Scenes.SceneObject
    default_interface: win32more.Microsoft.UI.Composition.Scenes.ISceneComponent
    _classid_ = 'Microsoft.UI.Composition.Scenes.SceneComponent'
    @winrt_mixinmethod
    def get_ComponentType(self: win32more.Microsoft.UI.Composition.Scenes.ISceneComponent) -> win32more.Microsoft.UI.Composition.Scenes.SceneComponentType: ...
    ComponentType = property(get_ComponentType, None)
class SceneComponentCollection(ComPtr):
    extends: win32more.Microsoft.UI.Composition.Scenes.SceneObject
    implements: Tuple[SequenceProtocol[win32more.Microsoft.UI.Composition.Scenes.SceneComponent]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Composition.Scenes.SceneComponent]
    _classid_ = 'Microsoft.UI.Composition.Scenes.SceneComponentCollection'
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Composition.Scenes.SceneComponent]) -> Void: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Composition.Scenes.SceneComponent], index: UInt32, value: win32more.Microsoft.UI.Composition.Scenes.SceneComponent) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Composition.Scenes.SceneComponent], value: win32more.Microsoft.UI.Composition.Scenes.SceneComponent) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Composition.Scenes.SceneComponent], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Composition.Scenes.SceneComponent]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Composition.Scenes.SceneComponent], startIndex: UInt32, items: FillArray[win32more.Microsoft.UI.Composition.Scenes.SceneComponent]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Composition.Scenes.SceneComponent], items: PassArray[win32more.Microsoft.UI.Composition.Scenes.SceneComponent]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Composition.Scenes.SceneComponent]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Microsoft.UI.Composition.Scenes.SceneComponent]: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Composition.Scenes.SceneComponent], index: UInt32, value: win32more.Microsoft.UI.Composition.Scenes.SceneComponent) -> Void: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Composition.Scenes.SceneComponent], value: win32more.Microsoft.UI.Composition.Scenes.SceneComponent, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Composition.Scenes.SceneComponent]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Composition.Scenes.SceneComponent]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.UI.Composition.Scenes.SceneComponent]: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Composition.Scenes.SceneComponent], index: UInt32) -> win32more.Microsoft.UI.Composition.Scenes.SceneComponent: ...
    Size = property(get_Size, None)
class SceneComponentType(Enum, Int32):
    MeshRendererComponent = 0
class SceneMaterial(ComPtr):
    extends: win32more.Microsoft.UI.Composition.Scenes.SceneObject
    default_interface: win32more.Microsoft.UI.Composition.Scenes.ISceneMaterial
    _classid_ = 'Microsoft.UI.Composition.Scenes.SceneMaterial'
class SceneMaterialInput(ComPtr):
    extends: win32more.Microsoft.UI.Composition.Scenes.SceneObject
    default_interface: win32more.Microsoft.UI.Composition.Scenes.ISceneMaterialInput
    _classid_ = 'Microsoft.UI.Composition.Scenes.SceneMaterialInput'
class SceneMesh(ComPtr):
    extends: win32more.Microsoft.UI.Composition.Scenes.SceneObject
    default_interface: win32more.Microsoft.UI.Composition.Scenes.ISceneMesh
    _classid_ = 'Microsoft.UI.Composition.Scenes.SceneMesh'
    @winrt_mixinmethod
    def put_PrimitiveTopology(self: win32more.Microsoft.UI.Composition.Scenes.ISceneMesh, value: win32more.Microsoft.Graphics.DirectX.DirectXPrimitiveTopology) -> Void: ...
    @winrt_mixinmethod
    def FillMeshAttribute(self: win32more.Microsoft.UI.Composition.Scenes.ISceneMesh, semantic: win32more.Microsoft.UI.Composition.Scenes.SceneAttributeSemantic, format: win32more.Microsoft.Graphics.DirectX.DirectXPixelFormat, memory: win32more.Windows.Foundation.MemoryBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_PrimitiveTopology(self: win32more.Microsoft.UI.Composition.Scenes.ISceneMesh) -> win32more.Microsoft.Graphics.DirectX.DirectXPrimitiveTopology: ...
    @winrt_mixinmethod
    def get_Bounds(self: win32more.Microsoft.UI.Composition.Scenes.ISceneMesh) -> win32more.Microsoft.UI.Composition.Scenes.SceneBoundingBox: ...
    @winrt_classmethod
    def Create(cls: win32more.Microsoft.UI.Composition.Scenes.ISceneMeshStatics, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Scenes.SceneMesh: ...
    Bounds = property(get_Bounds, None)
    PrimitiveTopology = property(get_PrimitiveTopology, put_PrimitiveTopology)
class SceneMeshMaterialAttributeMap(ComPtr):
    extends: win32more.Microsoft.UI.Composition.Scenes.SceneObject
    implements: Tuple[MappingProtocol[WinRT_String, win32more.Microsoft.UI.Composition.Scenes.SceneAttributeSemantic]]
    default_interface: win32more.Microsoft.UI.Composition.Scenes.ISceneMeshMaterialAttributeMap
    _classid_ = 'Microsoft.UI.Composition.Scenes.SceneMeshMaterialAttributeMap'
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Microsoft.UI.Composition.Scenes.SceneAttributeSemantic]]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Microsoft.UI.Composition.Scenes.SceneAttributeSemantic]]: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Microsoft.UI.Composition.Scenes.SceneAttributeSemantic]) -> Void: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Microsoft.UI.Composition.Scenes.SceneAttributeSemantic]) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Microsoft.UI.Composition.Scenes.SceneAttributeSemantic]: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Microsoft.UI.Composition.Scenes.SceneAttributeSemantic]) -> UInt32: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Microsoft.UI.Composition.Scenes.SceneAttributeSemantic], key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def HasKey(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Microsoft.UI.Composition.Scenes.SceneAttributeSemantic], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def Insert(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Microsoft.UI.Composition.Scenes.SceneAttributeSemantic], key: WinRT_String, value: win32more.Microsoft.UI.Composition.Scenes.SceneAttributeSemantic) -> Boolean: ...
    @winrt_mixinmethod
    def Lookup(self: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Microsoft.UI.Composition.Scenes.SceneAttributeSemantic], key: WinRT_String) -> win32more.Microsoft.UI.Composition.Scenes.SceneAttributeSemantic: ...
    Size = property(get_Size, None)
class SceneMeshRendererComponent(ComPtr):
    extends: win32more.Microsoft.UI.Composition.Scenes.SceneRendererComponent
    default_interface: win32more.Microsoft.UI.Composition.Scenes.ISceneMeshRendererComponent
    _classid_ = 'Microsoft.UI.Composition.Scenes.SceneMeshRendererComponent'
    @winrt_mixinmethod
    def get_Mesh(self: win32more.Microsoft.UI.Composition.Scenes.ISceneMeshRendererComponent) -> win32more.Microsoft.UI.Composition.Scenes.SceneMesh: ...
    @winrt_mixinmethod
    def put_Mesh(self: win32more.Microsoft.UI.Composition.Scenes.ISceneMeshRendererComponent, value: win32more.Microsoft.UI.Composition.Scenes.SceneMesh) -> Void: ...
    @winrt_mixinmethod
    def get_UVMappings(self: win32more.Microsoft.UI.Composition.Scenes.ISceneMeshRendererComponent) -> win32more.Microsoft.UI.Composition.Scenes.SceneMeshMaterialAttributeMap: ...
    @winrt_mixinmethod
    def get_Material(self: win32more.Microsoft.UI.Composition.Scenes.ISceneMeshRendererComponent) -> win32more.Microsoft.UI.Composition.Scenes.SceneMaterial: ...
    @winrt_mixinmethod
    def put_Material(self: win32more.Microsoft.UI.Composition.Scenes.ISceneMeshRendererComponent, value: win32more.Microsoft.UI.Composition.Scenes.SceneMaterial) -> Void: ...
    @winrt_classmethod
    def Create(cls: win32more.Microsoft.UI.Composition.Scenes.ISceneMeshRendererComponentStatics, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Scenes.SceneMeshRendererComponent: ...
    Material = property(get_Material, put_Material)
    Mesh = property(get_Mesh, put_Mesh)
    UVMappings = property(get_UVMappings, None)
class SceneMetallicRoughnessMaterial(ComPtr):
    extends: win32more.Microsoft.UI.Composition.Scenes.ScenePbrMaterial
    default_interface: win32more.Microsoft.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial
    _classid_ = 'Microsoft.UI.Composition.Scenes.SceneMetallicRoughnessMaterial'
    @winrt_mixinmethod
    def get_BaseColorFactor(self: win32more.Microsoft.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial) -> win32more.Windows.Foundation.Numerics.Vector4: ...
    @winrt_mixinmethod
    def put_RoughnessFactor(self: win32more.Microsoft.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial, value: Single) -> Void: ...
    @winrt_mixinmethod
    def put_BaseColorFactor(self: win32more.Microsoft.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial, value: win32more.Windows.Foundation.Numerics.Vector4) -> Void: ...
    @winrt_mixinmethod
    def get_MetallicFactor(self: win32more.Microsoft.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial) -> Single: ...
    @winrt_mixinmethod
    def put_MetallicFactor(self: win32more.Microsoft.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial, value: Single) -> Void: ...
    @winrt_mixinmethod
    def put_BaseColorInput(self: win32more.Microsoft.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial, value: win32more.Microsoft.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_mixinmethod
    def get_BaseColorInput(self: win32more.Microsoft.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial) -> win32more.Microsoft.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_mixinmethod
    def get_MetallicRoughnessInput(self: win32more.Microsoft.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial) -> win32more.Microsoft.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_mixinmethod
    def put_MetallicRoughnessInput(self: win32more.Microsoft.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial, value: win32more.Microsoft.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_mixinmethod
    def get_RoughnessFactor(self: win32more.Microsoft.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial) -> Single: ...
    @winrt_classmethod
    def Create(cls: win32more.Microsoft.UI.Composition.Scenes.ISceneMetallicRoughnessMaterialStatics, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Scenes.SceneMetallicRoughnessMaterial: ...
    BaseColorFactor = property(get_BaseColorFactor, put_BaseColorFactor)
    BaseColorInput = property(get_BaseColorInput, put_BaseColorInput)
    MetallicFactor = property(get_MetallicFactor, put_MetallicFactor)
    MetallicRoughnessInput = property(get_MetallicRoughnessInput, put_MetallicRoughnessInput)
    RoughnessFactor = property(get_RoughnessFactor, put_RoughnessFactor)
class SceneModelTransform(ComPtr):
    extends: win32more.Microsoft.UI.Composition.CompositionTransform
    default_interface: win32more.Microsoft.UI.Composition.Scenes.ISceneModelTransform
    _classid_ = 'Microsoft.UI.Composition.Scenes.SceneModelTransform'
    @winrt_mixinmethod
    def get_Translation(self: win32more.Microsoft.UI.Composition.Scenes.ISceneModelTransform) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_RotationAngle(self: win32more.Microsoft.UI.Composition.Scenes.ISceneModelTransform) -> Single: ...
    @winrt_mixinmethod
    def put_Orientation(self: win32more.Microsoft.UI.Composition.Scenes.ISceneModelTransform, value: win32more.Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_mixinmethod
    def put_RotationAngleInDegrees(self: win32more.Microsoft.UI.Composition.Scenes.ISceneModelTransform, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAxis(self: win32more.Microsoft.UI.Composition.Scenes.ISceneModelTransform) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_RotationAxis(self: win32more.Microsoft.UI.Composition.Scenes.ISceneModelTransform, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_Scale(self: win32more.Microsoft.UI.Composition.Scenes.ISceneModelTransform) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Scale(self: win32more.Microsoft.UI.Composition.Scenes.ISceneModelTransform, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def put_Translation(self: win32more.Microsoft.UI.Composition.Scenes.ISceneModelTransform, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_Orientation(self: win32more.Microsoft.UI.Composition.Scenes.ISceneModelTransform) -> win32more.Windows.Foundation.Numerics.Quaternion: ...
    @winrt_mixinmethod
    def put_RotationAngle(self: win32more.Microsoft.UI.Composition.Scenes.ISceneModelTransform, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAngleInDegrees(self: win32more.Microsoft.UI.Composition.Scenes.ISceneModelTransform) -> Single: ...
    Orientation = property(get_Orientation, put_Orientation)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    RotationAngleInDegrees = property(get_RotationAngleInDegrees, put_RotationAngleInDegrees)
    RotationAxis = property(get_RotationAxis, put_RotationAxis)
    Scale = property(get_Scale, put_Scale)
    Translation = property(get_Translation, put_Translation)
class SceneNode(ComPtr):
    extends: win32more.Microsoft.UI.Composition.Scenes.SceneObject
    default_interface: win32more.Microsoft.UI.Composition.Scenes.ISceneNode
    _classid_ = 'Microsoft.UI.Composition.Scenes.SceneNode'
    @winrt_mixinmethod
    def get_Transform(self: win32more.Microsoft.UI.Composition.Scenes.ISceneNode) -> win32more.Microsoft.UI.Composition.Scenes.SceneModelTransform: ...
    @winrt_mixinmethod
    def FindFirstComponentOfType(self: win32more.Microsoft.UI.Composition.Scenes.ISceneNode, value: win32more.Microsoft.UI.Composition.Scenes.SceneComponentType) -> win32more.Microsoft.UI.Composition.Scenes.SceneComponent: ...
    @winrt_mixinmethod
    def get_Components(self: win32more.Microsoft.UI.Composition.Scenes.ISceneNode) -> win32more.Microsoft.UI.Composition.Scenes.SceneComponentCollection: ...
    @winrt_mixinmethod
    def get_Parent(self: win32more.Microsoft.UI.Composition.Scenes.ISceneNode) -> win32more.Microsoft.UI.Composition.Scenes.SceneNode: ...
    @winrt_mixinmethod
    def get_Children(self: win32more.Microsoft.UI.Composition.Scenes.ISceneNode) -> win32more.Microsoft.UI.Composition.Scenes.SceneNodeCollection: ...
    @winrt_classmethod
    def Create(cls: win32more.Microsoft.UI.Composition.Scenes.ISceneNodeStatics, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Scenes.SceneNode: ...
    Children = property(get_Children, None)
    Components = property(get_Components, None)
    Parent = property(get_Parent, None)
    Transform = property(get_Transform, None)
class SceneNodeCollection(ComPtr):
    extends: win32more.Microsoft.UI.Composition.Scenes.SceneObject
    implements: Tuple[SequenceProtocol[win32more.Microsoft.UI.Composition.Scenes.SceneNode]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Composition.Scenes.SceneNode]
    _classid_ = 'Microsoft.UI.Composition.Scenes.SceneNodeCollection'
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Composition.Scenes.SceneNode], value: win32more.Microsoft.UI.Composition.Scenes.SceneNode) -> Void: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Composition.Scenes.SceneNode]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.UI.Composition.Scenes.SceneNode]: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Composition.Scenes.SceneNode]) -> UInt32: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Composition.Scenes.SceneNode], index: UInt32, value: win32more.Microsoft.UI.Composition.Scenes.SceneNode) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Composition.Scenes.SceneNode], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Composition.Scenes.SceneNode]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Composition.Scenes.SceneNode]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Composition.Scenes.SceneNode], startIndex: UInt32, items: FillArray[win32more.Microsoft.UI.Composition.Scenes.SceneNode]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Composition.Scenes.SceneNode], items: PassArray[win32more.Microsoft.UI.Composition.Scenes.SceneNode]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Composition.Scenes.SceneNode]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Microsoft.UI.Composition.Scenes.SceneNode]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Composition.Scenes.SceneNode], value: win32more.Microsoft.UI.Composition.Scenes.SceneNode, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Composition.Scenes.SceneNode], index: UInt32, value: win32more.Microsoft.UI.Composition.Scenes.SceneNode) -> Void: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Composition.Scenes.SceneNode], index: UInt32) -> win32more.Microsoft.UI.Composition.Scenes.SceneNode: ...
    Size = property(get_Size, None)
class SceneObject(ComPtr):
    extends: win32more.Microsoft.UI.Composition.CompositionObject
    default_interface: win32more.Microsoft.UI.Composition.Scenes.ISceneObject
    _classid_ = 'Microsoft.UI.Composition.Scenes.SceneObject'
class ScenePbrMaterial(ComPtr):
    extends: win32more.Microsoft.UI.Composition.Scenes.SceneMaterial
    default_interface: win32more.Microsoft.UI.Composition.Scenes.IScenePbrMaterial
    _classid_ = 'Microsoft.UI.Composition.Scenes.ScenePbrMaterial'
    @winrt_mixinmethod
    def put_NormalInput(self: win32more.Microsoft.UI.Composition.Scenes.IScenePbrMaterial, value: win32more.Microsoft.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_mixinmethod
    def put_OcclusionInput(self: win32more.Microsoft.UI.Composition.Scenes.IScenePbrMaterial, value: win32more.Microsoft.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_mixinmethod
    def put_OcclusionStrength(self: win32more.Microsoft.UI.Composition.Scenes.IScenePbrMaterial, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_AlphaMode(self: win32more.Microsoft.UI.Composition.Scenes.IScenePbrMaterial) -> win32more.Microsoft.UI.Composition.Scenes.SceneAlphaMode: ...
    @winrt_mixinmethod
    def get_OcclusionInput(self: win32more.Microsoft.UI.Composition.Scenes.IScenePbrMaterial) -> win32more.Microsoft.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_mixinmethod
    def get_OcclusionStrength(self: win32more.Microsoft.UI.Composition.Scenes.IScenePbrMaterial) -> Single: ...
    @winrt_mixinmethod
    def get_EmissiveInput(self: win32more.Microsoft.UI.Composition.Scenes.IScenePbrMaterial) -> win32more.Microsoft.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_mixinmethod
    def put_AlphaCutoff(self: win32more.Microsoft.UI.Composition.Scenes.IScenePbrMaterial, value: Single) -> Void: ...
    @winrt_mixinmethod
    def put_AlphaMode(self: win32more.Microsoft.UI.Composition.Scenes.IScenePbrMaterial, value: win32more.Microsoft.UI.Composition.Scenes.SceneAlphaMode) -> Void: ...
    @winrt_mixinmethod
    def get_AlphaCutoff(self: win32more.Microsoft.UI.Composition.Scenes.IScenePbrMaterial) -> Single: ...
    @winrt_mixinmethod
    def put_EmissiveInput(self: win32more.Microsoft.UI.Composition.Scenes.IScenePbrMaterial, value: win32more.Microsoft.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_mixinmethod
    def get_EmissiveFactor(self: win32more.Microsoft.UI.Composition.Scenes.IScenePbrMaterial) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_EmissiveFactor(self: win32more.Microsoft.UI.Composition.Scenes.IScenePbrMaterial, value: win32more.Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_IsDoubleSided(self: win32more.Microsoft.UI.Composition.Scenes.IScenePbrMaterial) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsDoubleSided(self: win32more.Microsoft.UI.Composition.Scenes.IScenePbrMaterial, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_NormalInput(self: win32more.Microsoft.UI.Composition.Scenes.IScenePbrMaterial) -> win32more.Microsoft.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_mixinmethod
    def get_NormalScale(self: win32more.Microsoft.UI.Composition.Scenes.IScenePbrMaterial) -> Single: ...
    @winrt_mixinmethod
    def put_NormalScale(self: win32more.Microsoft.UI.Composition.Scenes.IScenePbrMaterial, value: Single) -> Void: ...
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
    extends: win32more.Microsoft.UI.Composition.Scenes.SceneComponent
    default_interface: win32more.Microsoft.UI.Composition.Scenes.ISceneRendererComponent
    _classid_ = 'Microsoft.UI.Composition.Scenes.SceneRendererComponent'
class SceneSurfaceMaterialInput(ComPtr):
    extends: win32more.Microsoft.UI.Composition.Scenes.SceneMaterialInput
    default_interface: win32more.Microsoft.UI.Composition.Scenes.ISceneSurfaceMaterialInput
    _classid_ = 'Microsoft.UI.Composition.Scenes.SceneSurfaceMaterialInput'
    @winrt_mixinmethod
    def get_Surface(self: win32more.Microsoft.UI.Composition.Scenes.ISceneSurfaceMaterialInput) -> win32more.Microsoft.UI.Composition.ICompositionSurface: ...
    @winrt_mixinmethod
    def get_BitmapInterpolationMode(self: win32more.Microsoft.UI.Composition.Scenes.ISceneSurfaceMaterialInput) -> win32more.Microsoft.UI.Composition.CompositionBitmapInterpolationMode: ...
    @winrt_mixinmethod
    def put_Surface(self: win32more.Microsoft.UI.Composition.Scenes.ISceneSurfaceMaterialInput, value: win32more.Microsoft.UI.Composition.ICompositionSurface) -> Void: ...
    @winrt_mixinmethod
    def get_WrappingUMode(self: win32more.Microsoft.UI.Composition.Scenes.ISceneSurfaceMaterialInput) -> win32more.Microsoft.UI.Composition.Scenes.SceneWrappingMode: ...
    @winrt_mixinmethod
    def put_WrappingUMode(self: win32more.Microsoft.UI.Composition.Scenes.ISceneSurfaceMaterialInput, value: win32more.Microsoft.UI.Composition.Scenes.SceneWrappingMode) -> Void: ...
    @winrt_mixinmethod
    def put_BitmapInterpolationMode(self: win32more.Microsoft.UI.Composition.Scenes.ISceneSurfaceMaterialInput, value: win32more.Microsoft.UI.Composition.CompositionBitmapInterpolationMode) -> Void: ...
    @winrt_mixinmethod
    def put_WrappingVMode(self: win32more.Microsoft.UI.Composition.Scenes.ISceneSurfaceMaterialInput, value: win32more.Microsoft.UI.Composition.Scenes.SceneWrappingMode) -> Void: ...
    @winrt_mixinmethod
    def get_WrappingVMode(self: win32more.Microsoft.UI.Composition.Scenes.ISceneSurfaceMaterialInput) -> win32more.Microsoft.UI.Composition.Scenes.SceneWrappingMode: ...
    @winrt_classmethod
    def Create(cls: win32more.Microsoft.UI.Composition.Scenes.ISceneSurfaceMaterialInputStatics, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Scenes.SceneSurfaceMaterialInput: ...
    BitmapInterpolationMode = property(get_BitmapInterpolationMode, put_BitmapInterpolationMode)
    Surface = property(get_Surface, put_Surface)
    WrappingUMode = property(get_WrappingUMode, put_WrappingUMode)
    WrappingVMode = property(get_WrappingVMode, put_WrappingVMode)
class SceneVisual(ComPtr):
    extends: win32more.Microsoft.UI.Composition.ContainerVisual
    default_interface: win32more.Microsoft.UI.Composition.Scenes.ISceneVisual
    _classid_ = 'Microsoft.UI.Composition.Scenes.SceneVisual'
    @winrt_mixinmethod
    def get_Root(self: win32more.Microsoft.UI.Composition.Scenes.ISceneVisual) -> win32more.Microsoft.UI.Composition.Scenes.SceneNode: ...
    @winrt_mixinmethod
    def put_Root(self: win32more.Microsoft.UI.Composition.Scenes.ISceneVisual, value: win32more.Microsoft.UI.Composition.Scenes.SceneNode) -> Void: ...
    @winrt_classmethod
    def Create(cls: win32more.Microsoft.UI.Composition.Scenes.ISceneVisualStatics, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Scenes.SceneVisual: ...
    Root = property(get_Root, put_Root)
class SceneWrappingMode(Enum, Int32):
    ClampToEdge = 0
    MirroredRepeat = 1
    Repeat = 2


make_ready(__name__)
