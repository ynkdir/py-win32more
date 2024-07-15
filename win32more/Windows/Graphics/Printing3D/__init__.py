from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Foundation.Numerics
import win32more.Windows.Graphics.Printing3D
import win32more.Windows.Storage.Streams
import win32more.Windows.UI
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class IPrint3DManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrint3DManager'
    _iid_ = Guid('{4d2fcb0a-7366-4971-8bd5-17c4e3e8c6c0}')
    @winrt_commethod(6)
    def add_TaskRequested(self, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing3D.Print3DManager, win32more.Windows.Graphics.Printing3D.Print3DTaskRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_TaskRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    TaskRequested = event()
class IPrint3DManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrint3DManagerStatics'
    _iid_ = Guid('{0ef1cafe-a9ad-4c08-a917-1d1f863eabcb}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.Graphics.Printing3D.Print3DManager: ...
    @winrt_commethod(7)
    def ShowPrintUIAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class IPrint3DTask(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrint3DTask'
    _iid_ = Guid('{8ce3d080-2118-4c28-80de-f426d70191ae}')
    @winrt_commethod(6)
    def get_Source(self) -> win32more.Windows.Graphics.Printing3D.Printing3D3MFPackage: ...
    @winrt_commethod(7)
    def add_Submitting(self, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing3D.Print3DTask, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Submitting(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_Completed(self, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing3D.Print3DTask, win32more.Windows.Graphics.Printing3D.Print3DTaskCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Completed(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_SourceChanged(self, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing3D.Print3DTask, win32more.Windows.Graphics.Printing3D.Print3DTaskSourceChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_SourceChanged(self, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Source = property(get_Source, None)
    Submitting = event()
    Completed = event()
    SourceChanged = event()
class IPrint3DTaskCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrint3DTaskCompletedEventArgs'
    _iid_ = Guid('{cc1914af-2614-4f1d-accc-d6fc4fda5455}')
    @winrt_commethod(6)
    def get_Completion(self) -> win32more.Windows.Graphics.Printing3D.Print3DTaskCompletion: ...
    @winrt_commethod(7)
    def get_ExtendedStatus(self) -> win32more.Windows.Graphics.Printing3D.Print3DTaskDetail: ...
    Completion = property(get_Completion, None)
    ExtendedStatus = property(get_ExtendedStatus, None)
class IPrint3DTaskRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrint3DTaskRequest'
    _iid_ = Guid('{2595c46f-2245-4c5a-8731-0d604dc6bc3c}')
    @winrt_commethod(6)
    def CreateTask(self, title: WinRT_String, printerId: WinRT_String, handler: win32more.Windows.Graphics.Printing3D.Print3DTaskSourceRequestedHandler) -> win32more.Windows.Graphics.Printing3D.Print3DTask: ...
class IPrint3DTaskRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrint3DTaskRequestedEventArgs'
    _iid_ = Guid('{150cb77f-18c5-40d7-9f40-fab3096e05a9}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.Graphics.Printing3D.Print3DTaskRequest: ...
    Request = property(get_Request, None)
class IPrint3DTaskSourceChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrint3DTaskSourceChangedEventArgs'
    _iid_ = Guid('{5bcd34af-24e9-4c10-8d07-14c346ba3fcf}')
    @winrt_commethod(6)
    def get_Source(self) -> win32more.Windows.Graphics.Printing3D.Printing3D3MFPackage: ...
    Source = property(get_Source, None)
class IPrint3DTaskSourceRequestedArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrint3DTaskSourceRequestedArgs'
    _iid_ = Guid('{c77c9aba-24af-424d-a3bf-92250c355602}')
    @winrt_commethod(6)
    def SetSource(self, source: win32more.Windows.Graphics.Printing3D.Printing3D3MFPackage) -> Void: ...
class IPrinting3D3MFPackage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3D3MFPackage'
    _iid_ = Guid('{f64dd5c8-2ab7-45a9-a1b7-267e948d5b18}')
    @winrt_commethod(6)
    def SaveAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_commethod(7)
    def get_PrintTicket(self) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_commethod(8)
    def put_PrintTicket(self, value: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Void: ...
    @winrt_commethod(9)
    def get_ModelPart(self) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_commethod(10)
    def put_ModelPart(self, value: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Void: ...
    @winrt_commethod(11)
    def get_Thumbnail(self) -> win32more.Windows.Graphics.Printing3D.Printing3DTextureResource: ...
    @winrt_commethod(12)
    def put_Thumbnail(self, value: win32more.Windows.Graphics.Printing3D.Printing3DTextureResource) -> Void: ...
    @winrt_commethod(13)
    def get_Textures(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DTextureResource]: ...
    @winrt_commethod(14)
    def LoadModelFromPackageAsync(self, value: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Printing3D.Printing3DModel]: ...
    @winrt_commethod(15)
    def SaveModelToPackageAsync(self, value: win32more.Windows.Graphics.Printing3D.Printing3DModel) -> win32more.Windows.Foundation.IAsyncAction: ...
    ModelPart = property(get_ModelPart, put_ModelPart)
    PrintTicket = property(get_PrintTicket, put_PrintTicket)
    Textures = property(get_Textures, None)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
class IPrinting3D3MFPackage2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3D3MFPackage2'
    _iid_ = Guid('{965c7ac4-93cb-4430-92b8-789cd454f883}')
    @winrt_commethod(6)
    def get_Compression(self) -> win32more.Windows.Graphics.Printing3D.Printing3DPackageCompression: ...
    @winrt_commethod(7)
    def put_Compression(self, value: win32more.Windows.Graphics.Printing3D.Printing3DPackageCompression) -> Void: ...
    Compression = property(get_Compression, put_Compression)
class IPrinting3D3MFPackageStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3D3MFPackageStatics'
    _iid_ = Guid('{7058d9af-7a9a-4787-b817-f6f459214823}')
    @winrt_commethod(6)
    def LoadAsync(self, value: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Printing3D.Printing3D3MFPackage]: ...
class IPrinting3DBaseMaterial(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DBaseMaterial'
    _iid_ = Guid('{d0f0e743-c50c-4bcb-9d04-fc16adcea2c9}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Name(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Color(self) -> win32more.Windows.Graphics.Printing3D.Printing3DColorMaterial: ...
    @winrt_commethod(9)
    def put_Color(self, value: win32more.Windows.Graphics.Printing3D.Printing3DColorMaterial) -> Void: ...
    Color = property(get_Color, put_Color)
    Name = property(get_Name, put_Name)
class IPrinting3DBaseMaterialGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DBaseMaterialGroup'
    _iid_ = Guid('{94f070b8-2515-4a8d-a1f0-d0fc13d06021}')
    @winrt_commethod(6)
    def get_Bases(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DBaseMaterial]: ...
    @winrt_commethod(7)
    def get_MaterialGroupId(self) -> UInt32: ...
    Bases = property(get_Bases, None)
    MaterialGroupId = property(get_MaterialGroupId, None)
class IPrinting3DBaseMaterialGroupFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DBaseMaterialGroupFactory'
    _iid_ = Guid('{5c1546dc-8697-4193-976b-84bb4116e5bf}')
    @winrt_commethod(6)
    def Create(self, MaterialGroupId: UInt32) -> win32more.Windows.Graphics.Printing3D.Printing3DBaseMaterialGroup: ...
class IPrinting3DBaseMaterialStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DBaseMaterialStatics'
    _iid_ = Guid('{815a47bc-374a-476d-be92-3ecfd1cb9776}')
    @winrt_commethod(6)
    def get_Abs(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Pla(self) -> WinRT_String: ...
    Abs = property(get_Abs, None)
    Pla = property(get_Pla, None)
class IPrinting3DColorMaterial(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DColorMaterial'
    _iid_ = Guid('{e1899928-7ce7-4285-a35d-f145c9510c7b}')
    @winrt_commethod(6)
    def get_Value(self) -> UInt32: ...
    @winrt_commethod(7)
    def put_Value(self, value: UInt32) -> Void: ...
    Value = property(get_Value, put_Value)
class IPrinting3DColorMaterial2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DColorMaterial2'
    _iid_ = Guid('{fab0e852-0aef-44e9-9ddd-36eeea5acd44}')
    @winrt_commethod(6)
    def get_Color(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Color(self, value: win32more.Windows.UI.Color) -> Void: ...
    Color = property(get_Color, put_Color)
class IPrinting3DColorMaterialGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DColorMaterialGroup'
    _iid_ = Guid('{001a6bd0-aadf-4226-afe9-f369a0b45004}')
    @winrt_commethod(6)
    def get_Colors(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DColorMaterial]: ...
    @winrt_commethod(7)
    def get_MaterialGroupId(self) -> UInt32: ...
    Colors = property(get_Colors, None)
    MaterialGroupId = property(get_MaterialGroupId, None)
class IPrinting3DColorMaterialGroupFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DColorMaterialGroupFactory'
    _iid_ = Guid('{71d38d6d-b1ea-4a5b-bc54-19c65f3df044}')
    @winrt_commethod(6)
    def Create(self, MaterialGroupId: UInt32) -> win32more.Windows.Graphics.Printing3D.Printing3DColorMaterialGroup: ...
class IPrinting3DComponent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DComponent'
    _iid_ = Guid('{7e287845-bf7f-4cdb-a27f-30a01437fede}')
    @winrt_commethod(6)
    def get_Mesh(self) -> win32more.Windows.Graphics.Printing3D.Printing3DMesh: ...
    @winrt_commethod(7)
    def put_Mesh(self, value: win32more.Windows.Graphics.Printing3D.Printing3DMesh) -> Void: ...
    @winrt_commethod(8)
    def get_Components(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DComponentWithMatrix]: ...
    @winrt_commethod(9)
    def get_Thumbnail(self) -> win32more.Windows.Graphics.Printing3D.Printing3DTextureResource: ...
    @winrt_commethod(10)
    def put_Thumbnail(self, value: win32more.Windows.Graphics.Printing3D.Printing3DTextureResource) -> Void: ...
    @winrt_commethod(11)
    def get_Type(self) -> win32more.Windows.Graphics.Printing3D.Printing3DObjectType: ...
    @winrt_commethod(12)
    def put_Type(self, value: win32more.Windows.Graphics.Printing3D.Printing3DObjectType) -> Void: ...
    @winrt_commethod(13)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_Name(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_PartNumber(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def put_PartNumber(self, value: WinRT_String) -> Void: ...
    Components = property(get_Components, None)
    Mesh = property(get_Mesh, put_Mesh)
    Name = property(get_Name, put_Name)
    PartNumber = property(get_PartNumber, put_PartNumber)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
    Type = property(get_Type, put_Type)
class IPrinting3DComponentWithMatrix(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DComponentWithMatrix'
    _iid_ = Guid('{3279f335-0ef0-456b-9a21-49bebe8b51c2}')
    @winrt_commethod(6)
    def get_Component(self) -> win32more.Windows.Graphics.Printing3D.Printing3DComponent: ...
    @winrt_commethod(7)
    def put_Component(self, value: win32more.Windows.Graphics.Printing3D.Printing3DComponent) -> Void: ...
    @winrt_commethod(8)
    def get_Matrix(self) -> win32more.Windows.Foundation.Numerics.Matrix4x4: ...
    @winrt_commethod(9)
    def put_Matrix(self, value: win32more.Windows.Foundation.Numerics.Matrix4x4) -> Void: ...
    Component = property(get_Component, put_Component)
    Matrix = property(get_Matrix, put_Matrix)
class IPrinting3DCompositeMaterial(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DCompositeMaterial'
    _iid_ = Guid('{462238dd-562e-4f6c-882d-f4d841fd63c7}')
    @winrt_commethod(6)
    def get_Values(self) -> win32more.Windows.Foundation.Collections.IVector[Double]: ...
    Values = property(get_Values, None)
class IPrinting3DCompositeMaterialGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DCompositeMaterialGroup'
    _iid_ = Guid('{8d946a5b-40f1-496d-a5fb-340a5a678e30}')
    @winrt_commethod(6)
    def get_Composites(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DCompositeMaterial]: ...
    @winrt_commethod(7)
    def get_MaterialGroupId(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_MaterialIndices(self) -> win32more.Windows.Foundation.Collections.IVector[UInt32]: ...
    Composites = property(get_Composites, None)
    MaterialGroupId = property(get_MaterialGroupId, None)
    MaterialIndices = property(get_MaterialIndices, None)
class IPrinting3DCompositeMaterialGroup2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DCompositeMaterialGroup2'
    _iid_ = Guid('{06e86d62-7d3b-41e1-944c-bafde4555483}')
    @winrt_commethod(6)
    def get_BaseMaterialGroup(self) -> win32more.Windows.Graphics.Printing3D.Printing3DBaseMaterialGroup: ...
    @winrt_commethod(7)
    def put_BaseMaterialGroup(self, value: win32more.Windows.Graphics.Printing3D.Printing3DBaseMaterialGroup) -> Void: ...
    BaseMaterialGroup = property(get_BaseMaterialGroup, put_BaseMaterialGroup)
class IPrinting3DCompositeMaterialGroupFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DCompositeMaterialGroupFactory'
    _iid_ = Guid('{d08ecd13-92ff-43aa-a627-8d43c22c817e}')
    @winrt_commethod(6)
    def Create(self, MaterialGroupId: UInt32) -> win32more.Windows.Graphics.Printing3D.Printing3DCompositeMaterialGroup: ...
class IPrinting3DFaceReductionOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DFaceReductionOptions'
    _iid_ = Guid('{bbfed397-2d74-46f7-be85-99a67bbb6629}')
    @winrt_commethod(6)
    def get_MaxReductionArea(self) -> Double: ...
    @winrt_commethod(7)
    def put_MaxReductionArea(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_TargetTriangleCount(self) -> UInt32: ...
    @winrt_commethod(9)
    def put_TargetTriangleCount(self, value: UInt32) -> Void: ...
    @winrt_commethod(10)
    def get_MaxEdgeLength(self) -> Double: ...
    @winrt_commethod(11)
    def put_MaxEdgeLength(self, value: Double) -> Void: ...
    MaxEdgeLength = property(get_MaxEdgeLength, put_MaxEdgeLength)
    MaxReductionArea = property(get_MaxReductionArea, put_MaxReductionArea)
    TargetTriangleCount = property(get_TargetTriangleCount, put_TargetTriangleCount)
class IPrinting3DMaterial(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DMaterial'
    _iid_ = Guid('{378db256-ed62-4952-b85b-03567d7c465e}')
    @winrt_commethod(6)
    def get_BaseGroups(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DBaseMaterialGroup]: ...
    @winrt_commethod(7)
    def get_ColorGroups(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DColorMaterialGroup]: ...
    @winrt_commethod(8)
    def get_Texture2CoordGroups(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DTexture2CoordMaterialGroup]: ...
    @winrt_commethod(9)
    def get_CompositeGroups(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DCompositeMaterialGroup]: ...
    @winrt_commethod(10)
    def get_MultiplePropertyGroups(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DMultiplePropertyMaterialGroup]: ...
    BaseGroups = property(get_BaseGroups, None)
    ColorGroups = property(get_ColorGroups, None)
    CompositeGroups = property(get_CompositeGroups, None)
    MultiplePropertyGroups = property(get_MultiplePropertyGroups, None)
    Texture2CoordGroups = property(get_Texture2CoordGroups, None)
class IPrinting3DMesh(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DMesh'
    _iid_ = Guid('{192e90dc-0228-2e01-bc20-c5290cbf32c4}')
    @winrt_commethod(6)
    def get_VertexCount(self) -> UInt32: ...
    @winrt_commethod(7)
    def put_VertexCount(self, value: UInt32) -> Void: ...
    @winrt_commethod(8)
    def get_IndexCount(self) -> UInt32: ...
    @winrt_commethod(9)
    def put_IndexCount(self, value: UInt32) -> Void: ...
    @winrt_commethod(10)
    def get_VertexPositionsDescription(self) -> win32more.Windows.Graphics.Printing3D.Printing3DBufferDescription: ...
    @winrt_commethod(11)
    def put_VertexPositionsDescription(self, value: win32more.Windows.Graphics.Printing3D.Printing3DBufferDescription) -> Void: ...
    @winrt_commethod(12)
    def get_VertexNormalsDescription(self) -> win32more.Windows.Graphics.Printing3D.Printing3DBufferDescription: ...
    @winrt_commethod(13)
    def put_VertexNormalsDescription(self, value: win32more.Windows.Graphics.Printing3D.Printing3DBufferDescription) -> Void: ...
    @winrt_commethod(14)
    def get_TriangleIndicesDescription(self) -> win32more.Windows.Graphics.Printing3D.Printing3DBufferDescription: ...
    @winrt_commethod(15)
    def put_TriangleIndicesDescription(self, value: win32more.Windows.Graphics.Printing3D.Printing3DBufferDescription) -> Void: ...
    @winrt_commethod(16)
    def get_TriangleMaterialIndicesDescription(self) -> win32more.Windows.Graphics.Printing3D.Printing3DBufferDescription: ...
    @winrt_commethod(17)
    def put_TriangleMaterialIndicesDescription(self, value: win32more.Windows.Graphics.Printing3D.Printing3DBufferDescription) -> Void: ...
    @winrt_commethod(18)
    def GetVertexPositions(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(19)
    def CreateVertexPositions(self, value: UInt32) -> Void: ...
    @winrt_commethod(20)
    def GetVertexNormals(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(21)
    def CreateVertexNormals(self, value: UInt32) -> Void: ...
    @winrt_commethod(22)
    def GetTriangleIndices(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(23)
    def CreateTriangleIndices(self, value: UInt32) -> Void: ...
    @winrt_commethod(24)
    def GetTriangleMaterialIndices(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(25)
    def CreateTriangleMaterialIndices(self, value: UInt32) -> Void: ...
    @winrt_commethod(26)
    def get_BufferDescriptionSet(self) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_commethod(27)
    def get_BufferSet(self) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_commethod(28)
    def VerifyAsync(self, value: win32more.Windows.Graphics.Printing3D.Printing3DMeshVerificationMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Printing3D.Printing3DMeshVerificationResult]: ...
    BufferDescriptionSet = property(get_BufferDescriptionSet, None)
    BufferSet = property(get_BufferSet, None)
    IndexCount = property(get_IndexCount, put_IndexCount)
    TriangleIndicesDescription = property(get_TriangleIndicesDescription, put_TriangleIndicesDescription)
    TriangleMaterialIndicesDescription = property(get_TriangleMaterialIndicesDescription, put_TriangleMaterialIndicesDescription)
    VertexCount = property(get_VertexCount, put_VertexCount)
    VertexNormalsDescription = property(get_VertexNormalsDescription, put_VertexNormalsDescription)
    VertexPositionsDescription = property(get_VertexPositionsDescription, put_VertexPositionsDescription)
class IPrinting3DMeshVerificationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DMeshVerificationResult'
    _iid_ = Guid('{195671ba-e93a-4e8a-a46f-dea8e852197e}')
    @winrt_commethod(6)
    def get_IsValid(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_NonmanifoldTriangles(self) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(8)
    def get_ReversedNormalTriangles(self) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    IsValid = property(get_IsValid, None)
    NonmanifoldTriangles = property(get_NonmanifoldTriangles, None)
    ReversedNormalTriangles = property(get_ReversedNormalTriangles, None)
class IPrinting3DModel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DModel'
    _iid_ = Guid('{2d012ef0-52fb-919a-77b0-4b1a3b80324f}')
    @winrt_commethod(6)
    def get_Unit(self) -> win32more.Windows.Graphics.Printing3D.Printing3DModelUnit: ...
    @winrt_commethod(7)
    def put_Unit(self, value: win32more.Windows.Graphics.Printing3D.Printing3DModelUnit) -> Void: ...
    @winrt_commethod(8)
    def get_Textures(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DModelTexture]: ...
    @winrt_commethod(9)
    def get_Meshes(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DMesh]: ...
    @winrt_commethod(10)
    def get_Components(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DComponent]: ...
    @winrt_commethod(11)
    def get_Material(self) -> win32more.Windows.Graphics.Printing3D.Printing3DMaterial: ...
    @winrt_commethod(12)
    def put_Material(self, value: win32more.Windows.Graphics.Printing3D.Printing3DMaterial) -> Void: ...
    @winrt_commethod(13)
    def get_Build(self) -> win32more.Windows.Graphics.Printing3D.Printing3DComponent: ...
    @winrt_commethod(14)
    def put_Build(self, value: win32more.Windows.Graphics.Printing3D.Printing3DComponent) -> Void: ...
    @winrt_commethod(15)
    def get_Version(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def put_Version(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(17)
    def get_RequiredExtensions(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(18)
    def get_Metadata(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_commethod(19)
    def RepairAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(20)
    def Clone(self) -> win32more.Windows.Graphics.Printing3D.Printing3DModel: ...
    Build = property(get_Build, put_Build)
    Components = property(get_Components, None)
    Material = property(get_Material, put_Material)
    Meshes = property(get_Meshes, None)
    Metadata = property(get_Metadata, None)
    RequiredExtensions = property(get_RequiredExtensions, None)
    Textures = property(get_Textures, None)
    Unit = property(get_Unit, put_Unit)
    Version = property(get_Version, put_Version)
class IPrinting3DModel2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DModel2'
    _iid_ = Guid('{c92069c7-c841-47f3-a84e-a149fd08b657}')
    @winrt_commethod(6)
    def TryPartialRepairAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def TryPartialRepairWithTimeAsync(self, maxWaitTime: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def TryReduceFacesAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[Boolean, Double]: ...
    @winrt_commethod(9)
    def TryReduceFacesWithOptionsAsync(self, printing3DFaceReductionOptions: win32more.Windows.Graphics.Printing3D.Printing3DFaceReductionOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[Boolean, Double]: ...
    @winrt_commethod(10)
    def TryReduceFacesWithOptionsAndTimeAsync(self, printing3DFaceReductionOptions: win32more.Windows.Graphics.Printing3D.Printing3DFaceReductionOptions, maxWait: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[Boolean, Double]: ...
    @winrt_commethod(11)
    def RepairWithProgressAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[Boolean, Double]: ...
class IPrinting3DModelTexture(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DModelTexture'
    _iid_ = Guid('{5dafcf01-b59d-483c-97bb-a4d546d1c75c}')
    @winrt_commethod(6)
    def get_TextureResource(self) -> win32more.Windows.Graphics.Printing3D.Printing3DTextureResource: ...
    @winrt_commethod(7)
    def put_TextureResource(self, value: win32more.Windows.Graphics.Printing3D.Printing3DTextureResource) -> Void: ...
    @winrt_commethod(8)
    def get_TileStyleU(self) -> win32more.Windows.Graphics.Printing3D.Printing3DTextureEdgeBehavior: ...
    @winrt_commethod(9)
    def put_TileStyleU(self, value: win32more.Windows.Graphics.Printing3D.Printing3DTextureEdgeBehavior) -> Void: ...
    @winrt_commethod(10)
    def get_TileStyleV(self) -> win32more.Windows.Graphics.Printing3D.Printing3DTextureEdgeBehavior: ...
    @winrt_commethod(11)
    def put_TileStyleV(self, value: win32more.Windows.Graphics.Printing3D.Printing3DTextureEdgeBehavior) -> Void: ...
    TextureResource = property(get_TextureResource, put_TextureResource)
    TileStyleU = property(get_TileStyleU, put_TileStyleU)
    TileStyleV = property(get_TileStyleV, put_TileStyleV)
class IPrinting3DMultiplePropertyMaterial(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DMultiplePropertyMaterial'
    _iid_ = Guid('{25a6254b-c6e9-484d-a214-a25e5776ba62}')
    @winrt_commethod(6)
    def get_MaterialIndices(self) -> win32more.Windows.Foundation.Collections.IVector[UInt32]: ...
    MaterialIndices = property(get_MaterialIndices, None)
class IPrinting3DMultiplePropertyMaterialGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DMultiplePropertyMaterialGroup'
    _iid_ = Guid('{f0950519-aeb9-4515-a39b-a088fbbb277c}')
    @winrt_commethod(6)
    def get_MultipleProperties(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DMultiplePropertyMaterial]: ...
    @winrt_commethod(7)
    def get_MaterialGroupIndices(self) -> win32more.Windows.Foundation.Collections.IVector[UInt32]: ...
    @winrt_commethod(8)
    def get_MaterialGroupId(self) -> UInt32: ...
    MaterialGroupId = property(get_MaterialGroupId, None)
    MaterialGroupIndices = property(get_MaterialGroupIndices, None)
    MultipleProperties = property(get_MultipleProperties, None)
class IPrinting3DMultiplePropertyMaterialGroupFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DMultiplePropertyMaterialGroupFactory'
    _iid_ = Guid('{323e196e-d4c6-451e-a814-4d78a210fe53}')
    @winrt_commethod(6)
    def Create(self, MaterialGroupId: UInt32) -> win32more.Windows.Graphics.Printing3D.Printing3DMultiplePropertyMaterialGroup: ...
class IPrinting3DTexture2CoordMaterial(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DTexture2CoordMaterial'
    _iid_ = Guid('{8d844bfb-07e9-4986-9833-8dd3d48c6859}')
    @winrt_commethod(6)
    def get_Texture(self) -> win32more.Windows.Graphics.Printing3D.Printing3DModelTexture: ...
    @winrt_commethod(7)
    def put_Texture(self, value: win32more.Windows.Graphics.Printing3D.Printing3DModelTexture) -> Void: ...
    @winrt_commethod(8)
    def get_U(self) -> Double: ...
    @winrt_commethod(9)
    def put_U(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_V(self) -> Double: ...
    @winrt_commethod(11)
    def put_V(self, value: Double) -> Void: ...
    Texture = property(get_Texture, put_Texture)
    U = property(get_U, put_U)
    V = property(get_V, put_V)
class IPrinting3DTexture2CoordMaterialGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DTexture2CoordMaterialGroup'
    _iid_ = Guid('{627d7ca7-6d90-4fb9-9fc4-9feff3dfa892}')
    @winrt_commethod(6)
    def get_Texture2Coords(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DTexture2CoordMaterial]: ...
    @winrt_commethod(7)
    def get_MaterialGroupId(self) -> UInt32: ...
    MaterialGroupId = property(get_MaterialGroupId, None)
    Texture2Coords = property(get_Texture2Coords, None)
class IPrinting3DTexture2CoordMaterialGroup2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DTexture2CoordMaterialGroup2'
    _iid_ = Guid('{69fbdbba-b12e-429b-8386-df5284f6e80f}')
    @winrt_commethod(6)
    def get_Texture(self) -> win32more.Windows.Graphics.Printing3D.Printing3DModelTexture: ...
    @winrt_commethod(7)
    def put_Texture(self, value: win32more.Windows.Graphics.Printing3D.Printing3DModelTexture) -> Void: ...
    Texture = property(get_Texture, put_Texture)
class IPrinting3DTexture2CoordMaterialGroupFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DTexture2CoordMaterialGroupFactory'
    _iid_ = Guid('{cbb049b0-468a-4c6f-b2a2-8eb8ba8dea48}')
    @winrt_commethod(6)
    def Create(self, MaterialGroupId: UInt32) -> win32more.Windows.Graphics.Printing3D.Printing3DTexture2CoordMaterialGroup: ...
class IPrinting3DTextureResource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing3D.IPrinting3DTextureResource'
    _iid_ = Guid('{a70df32d-6ab1-44ae-bc45-a27382c0d38c}')
    @winrt_commethod(6)
    def get_TextureData(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamWithContentType: ...
    @winrt_commethod(7)
    def put_TextureData(self, value: win32more.Windows.Storage.Streams.IRandomAccessStreamWithContentType) -> Void: ...
    @winrt_commethod(8)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Name(self, value: WinRT_String) -> Void: ...
    Name = property(get_Name, put_Name)
    TextureData = property(get_TextureData, put_TextureData)
class Print3DManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing3D.IPrint3DManager
    _classid_ = 'Windows.Graphics.Printing3D.Print3DManager'
    @winrt_mixinmethod
    def add_TaskRequested(self: win32more.Windows.Graphics.Printing3D.IPrint3DManager, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing3D.Print3DManager, win32more.Windows.Graphics.Printing3D.Print3DTaskRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TaskRequested(self: win32more.Windows.Graphics.Printing3D.IPrint3DManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.Graphics.Printing3D.IPrint3DManagerStatics) -> win32more.Windows.Graphics.Printing3D.Print3DManager: ...
    @winrt_classmethod
    def ShowPrintUIAsync(cls: win32more.Windows.Graphics.Printing3D.IPrint3DManagerStatics) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    TaskRequested = event()
class Print3DTask(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing3D.IPrint3DTask
    _classid_ = 'Windows.Graphics.Printing3D.Print3DTask'
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.Graphics.Printing3D.IPrint3DTask) -> win32more.Windows.Graphics.Printing3D.Printing3D3MFPackage: ...
    @winrt_mixinmethod
    def add_Submitting(self: win32more.Windows.Graphics.Printing3D.IPrint3DTask, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing3D.Print3DTask, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Submitting(self: win32more.Windows.Graphics.Printing3D.IPrint3DTask, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Completed(self: win32more.Windows.Graphics.Printing3D.IPrint3DTask, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing3D.Print3DTask, win32more.Windows.Graphics.Printing3D.Print3DTaskCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Completed(self: win32more.Windows.Graphics.Printing3D.IPrint3DTask, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SourceChanged(self: win32more.Windows.Graphics.Printing3D.IPrint3DTask, eventHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Printing3D.Print3DTask, win32more.Windows.Graphics.Printing3D.Print3DTaskSourceChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceChanged(self: win32more.Windows.Graphics.Printing3D.IPrint3DTask, eventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Source = property(get_Source, None)
    Submitting = event()
    Completed = event()
    SourceChanged = event()
class Print3DTaskCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing3D.IPrint3DTaskCompletedEventArgs
    _classid_ = 'Windows.Graphics.Printing3D.Print3DTaskCompletedEventArgs'
    @winrt_mixinmethod
    def get_Completion(self: win32more.Windows.Graphics.Printing3D.IPrint3DTaskCompletedEventArgs) -> win32more.Windows.Graphics.Printing3D.Print3DTaskCompletion: ...
    @winrt_mixinmethod
    def get_ExtendedStatus(self: win32more.Windows.Graphics.Printing3D.IPrint3DTaskCompletedEventArgs) -> win32more.Windows.Graphics.Printing3D.Print3DTaskDetail: ...
    Completion = property(get_Completion, None)
    ExtendedStatus = property(get_ExtendedStatus, None)
class Print3DTaskCompletion(Enum, Int32):
    Abandoned = 0
    Canceled = 1
    Failed = 2
    Slicing = 3
    Submitted = 4
class Print3DTaskDetail(Enum, Int32):
    Unknown = 0
    ModelExceedsPrintBed = 1
    UploadFailed = 2
    InvalidMaterialSelection = 3
    InvalidModel = 4
    ModelNotManifold = 5
    InvalidPrintTicket = 6
class Print3DTaskRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing3D.IPrint3DTaskRequest
    _classid_ = 'Windows.Graphics.Printing3D.Print3DTaskRequest'
    @winrt_mixinmethod
    def CreateTask(self: win32more.Windows.Graphics.Printing3D.IPrint3DTaskRequest, title: WinRT_String, printerId: WinRT_String, handler: win32more.Windows.Graphics.Printing3D.Print3DTaskSourceRequestedHandler) -> win32more.Windows.Graphics.Printing3D.Print3DTask: ...
class Print3DTaskRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing3D.IPrint3DTaskRequestedEventArgs
    _classid_ = 'Windows.Graphics.Printing3D.Print3DTaskRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.Graphics.Printing3D.IPrint3DTaskRequestedEventArgs) -> win32more.Windows.Graphics.Printing3D.Print3DTaskRequest: ...
    Request = property(get_Request, None)
class Print3DTaskSourceChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing3D.IPrint3DTaskSourceChangedEventArgs
    _classid_ = 'Windows.Graphics.Printing3D.Print3DTaskSourceChangedEventArgs'
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.Graphics.Printing3D.IPrint3DTaskSourceChangedEventArgs) -> win32more.Windows.Graphics.Printing3D.Printing3D3MFPackage: ...
    Source = property(get_Source, None)
class Print3DTaskSourceRequestedArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing3D.IPrint3DTaskSourceRequestedArgs
    _classid_ = 'Windows.Graphics.Printing3D.Print3DTaskSourceRequestedArgs'
    @winrt_mixinmethod
    def SetSource(self: win32more.Windows.Graphics.Printing3D.IPrint3DTaskSourceRequestedArgs, source: win32more.Windows.Graphics.Printing3D.Printing3D3MFPackage) -> Void: ...
class Print3DTaskSourceRequestedHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e9175e70-c917-46de-bb51-d9a94db3711f}')
    @winrt_commethod(3)
    def Invoke(self, args: win32more.Windows.Graphics.Printing3D.Print3DTaskSourceRequestedArgs) -> Void: ...
class Printing3D3MFPackage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing3D.IPrinting3D3MFPackage
    _classid_ = 'Windows.Graphics.Printing3D.Printing3D3MFPackage'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Graphics.Printing3D.Printing3D3MFPackage.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Graphics.Printing3D.Printing3D3MFPackage: ...
    @winrt_mixinmethod
    def SaveAsync(self: win32more.Windows.Graphics.Printing3D.IPrinting3D3MFPackage) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_mixinmethod
    def get_PrintTicket(self: win32more.Windows.Graphics.Printing3D.IPrinting3D3MFPackage) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def put_PrintTicket(self: win32more.Windows.Graphics.Printing3D.IPrinting3D3MFPackage, value: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Void: ...
    @winrt_mixinmethod
    def get_ModelPart(self: win32more.Windows.Graphics.Printing3D.IPrinting3D3MFPackage) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def put_ModelPart(self: win32more.Windows.Graphics.Printing3D.IPrinting3D3MFPackage, value: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Void: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: win32more.Windows.Graphics.Printing3D.IPrinting3D3MFPackage) -> win32more.Windows.Graphics.Printing3D.Printing3DTextureResource: ...
    @winrt_mixinmethod
    def put_Thumbnail(self: win32more.Windows.Graphics.Printing3D.IPrinting3D3MFPackage, value: win32more.Windows.Graphics.Printing3D.Printing3DTextureResource) -> Void: ...
    @winrt_mixinmethod
    def get_Textures(self: win32more.Windows.Graphics.Printing3D.IPrinting3D3MFPackage) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DTextureResource]: ...
    @winrt_mixinmethod
    def LoadModelFromPackageAsync(self: win32more.Windows.Graphics.Printing3D.IPrinting3D3MFPackage, value: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Printing3D.Printing3DModel]: ...
    @winrt_mixinmethod
    def SaveModelToPackageAsync(self: win32more.Windows.Graphics.Printing3D.IPrinting3D3MFPackage, value: win32more.Windows.Graphics.Printing3D.Printing3DModel) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_Compression(self: win32more.Windows.Graphics.Printing3D.IPrinting3D3MFPackage2) -> win32more.Windows.Graphics.Printing3D.Printing3DPackageCompression: ...
    @winrt_mixinmethod
    def put_Compression(self: win32more.Windows.Graphics.Printing3D.IPrinting3D3MFPackage2, value: win32more.Windows.Graphics.Printing3D.Printing3DPackageCompression) -> Void: ...
    @winrt_classmethod
    def LoadAsync(cls: win32more.Windows.Graphics.Printing3D.IPrinting3D3MFPackageStatics, value: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Printing3D.Printing3D3MFPackage]: ...
    Compression = property(get_Compression, put_Compression)
    ModelPart = property(get_ModelPart, put_ModelPart)
    PrintTicket = property(get_PrintTicket, put_PrintTicket)
    Textures = property(get_Textures, None)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
class _Printing3DBaseMaterial_Meta_(ComPtr.__class__):
    pass
class Printing3DBaseMaterial(ComPtr, metaclass=_Printing3DBaseMaterial_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing3D.IPrinting3DBaseMaterial
    _classid_ = 'Windows.Graphics.Printing3D.Printing3DBaseMaterial'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Graphics.Printing3D.Printing3DBaseMaterial.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Graphics.Printing3D.Printing3DBaseMaterial: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Graphics.Printing3D.IPrinting3DBaseMaterial) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: win32more.Windows.Graphics.Printing3D.IPrinting3DBaseMaterial, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Color(self: win32more.Windows.Graphics.Printing3D.IPrinting3DBaseMaterial) -> win32more.Windows.Graphics.Printing3D.Printing3DColorMaterial: ...
    @winrt_mixinmethod
    def put_Color(self: win32more.Windows.Graphics.Printing3D.IPrinting3DBaseMaterial, value: win32more.Windows.Graphics.Printing3D.Printing3DColorMaterial) -> Void: ...
    @winrt_classmethod
    def get_Abs(cls: win32more.Windows.Graphics.Printing3D.IPrinting3DBaseMaterialStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Pla(cls: win32more.Windows.Graphics.Printing3D.IPrinting3DBaseMaterialStatics) -> WinRT_String: ...
    Color = property(get_Color, put_Color)
    Name = property(get_Name, put_Name)
    _Printing3DBaseMaterial_Meta_.Abs = property(get_Abs, None)
    _Printing3DBaseMaterial_Meta_.Pla = property(get_Pla, None)
class Printing3DBaseMaterialGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing3D.IPrinting3DBaseMaterialGroup
    _classid_ = 'Windows.Graphics.Printing3D.Printing3DBaseMaterialGroup'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Graphics.Printing3D.Printing3DBaseMaterialGroup.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Graphics.Printing3D.IPrinting3DBaseMaterialGroupFactory, MaterialGroupId: UInt32) -> win32more.Windows.Graphics.Printing3D.Printing3DBaseMaterialGroup: ...
    @winrt_mixinmethod
    def get_Bases(self: win32more.Windows.Graphics.Printing3D.IPrinting3DBaseMaterialGroup) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DBaseMaterial]: ...
    @winrt_mixinmethod
    def get_MaterialGroupId(self: win32more.Windows.Graphics.Printing3D.IPrinting3DBaseMaterialGroup) -> UInt32: ...
    Bases = property(get_Bases, None)
    MaterialGroupId = property(get_MaterialGroupId, None)
class Printing3DBufferDescription(Structure):
    Format: win32more.Windows.Graphics.Printing3D.Printing3DBufferFormat
    Stride: UInt32
class Printing3DBufferFormat(Enum, Int32):
    Unknown = 0
    R32G32B32A32Float = 2
    R32G32B32A32UInt = 3
    R32G32B32Float = 6
    R32G32B32UInt = 7
    Printing3DDouble = 500
    Printing3DUInt = 501
class Printing3DColorMaterial(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing3D.IPrinting3DColorMaterial
    _classid_ = 'Windows.Graphics.Printing3D.Printing3DColorMaterial'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Graphics.Printing3D.Printing3DColorMaterial.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Graphics.Printing3D.Printing3DColorMaterial: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Graphics.Printing3D.IPrinting3DColorMaterial) -> UInt32: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Windows.Graphics.Printing3D.IPrinting3DColorMaterial, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Color(self: win32more.Windows.Graphics.Printing3D.IPrinting3DColorMaterial2) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: win32more.Windows.Graphics.Printing3D.IPrinting3DColorMaterial2, value: win32more.Windows.UI.Color) -> Void: ...
    Color = property(get_Color, put_Color)
    Value = property(get_Value, put_Value)
class Printing3DColorMaterialGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing3D.IPrinting3DColorMaterialGroup
    _classid_ = 'Windows.Graphics.Printing3D.Printing3DColorMaterialGroup'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Graphics.Printing3D.Printing3DColorMaterialGroup.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Graphics.Printing3D.IPrinting3DColorMaterialGroupFactory, MaterialGroupId: UInt32) -> win32more.Windows.Graphics.Printing3D.Printing3DColorMaterialGroup: ...
    @winrt_mixinmethod
    def get_Colors(self: win32more.Windows.Graphics.Printing3D.IPrinting3DColorMaterialGroup) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DColorMaterial]: ...
    @winrt_mixinmethod
    def get_MaterialGroupId(self: win32more.Windows.Graphics.Printing3D.IPrinting3DColorMaterialGroup) -> UInt32: ...
    Colors = property(get_Colors, None)
    MaterialGroupId = property(get_MaterialGroupId, None)
class Printing3DComponent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing3D.IPrinting3DComponent
    _classid_ = 'Windows.Graphics.Printing3D.Printing3DComponent'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Graphics.Printing3D.Printing3DComponent.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Graphics.Printing3D.Printing3DComponent: ...
    @winrt_mixinmethod
    def get_Mesh(self: win32more.Windows.Graphics.Printing3D.IPrinting3DComponent) -> win32more.Windows.Graphics.Printing3D.Printing3DMesh: ...
    @winrt_mixinmethod
    def put_Mesh(self: win32more.Windows.Graphics.Printing3D.IPrinting3DComponent, value: win32more.Windows.Graphics.Printing3D.Printing3DMesh) -> Void: ...
    @winrt_mixinmethod
    def get_Components(self: win32more.Windows.Graphics.Printing3D.IPrinting3DComponent) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DComponentWithMatrix]: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: win32more.Windows.Graphics.Printing3D.IPrinting3DComponent) -> win32more.Windows.Graphics.Printing3D.Printing3DTextureResource: ...
    @winrt_mixinmethod
    def put_Thumbnail(self: win32more.Windows.Graphics.Printing3D.IPrinting3DComponent, value: win32more.Windows.Graphics.Printing3D.Printing3DTextureResource) -> Void: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Graphics.Printing3D.IPrinting3DComponent) -> win32more.Windows.Graphics.Printing3D.Printing3DObjectType: ...
    @winrt_mixinmethod
    def put_Type(self: win32more.Windows.Graphics.Printing3D.IPrinting3DComponent, value: win32more.Windows.Graphics.Printing3D.Printing3DObjectType) -> Void: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Graphics.Printing3D.IPrinting3DComponent) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: win32more.Windows.Graphics.Printing3D.IPrinting3DComponent, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PartNumber(self: win32more.Windows.Graphics.Printing3D.IPrinting3DComponent) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PartNumber(self: win32more.Windows.Graphics.Printing3D.IPrinting3DComponent, value: WinRT_String) -> Void: ...
    Components = property(get_Components, None)
    Mesh = property(get_Mesh, put_Mesh)
    Name = property(get_Name, put_Name)
    PartNumber = property(get_PartNumber, put_PartNumber)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
    Type = property(get_Type, put_Type)
class Printing3DComponentWithMatrix(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing3D.IPrinting3DComponentWithMatrix
    _classid_ = 'Windows.Graphics.Printing3D.Printing3DComponentWithMatrix'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Graphics.Printing3D.Printing3DComponentWithMatrix.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Graphics.Printing3D.Printing3DComponentWithMatrix: ...
    @winrt_mixinmethod
    def get_Component(self: win32more.Windows.Graphics.Printing3D.IPrinting3DComponentWithMatrix) -> win32more.Windows.Graphics.Printing3D.Printing3DComponent: ...
    @winrt_mixinmethod
    def put_Component(self: win32more.Windows.Graphics.Printing3D.IPrinting3DComponentWithMatrix, value: win32more.Windows.Graphics.Printing3D.Printing3DComponent) -> Void: ...
    @winrt_mixinmethod
    def get_Matrix(self: win32more.Windows.Graphics.Printing3D.IPrinting3DComponentWithMatrix) -> win32more.Windows.Foundation.Numerics.Matrix4x4: ...
    @winrt_mixinmethod
    def put_Matrix(self: win32more.Windows.Graphics.Printing3D.IPrinting3DComponentWithMatrix, value: win32more.Windows.Foundation.Numerics.Matrix4x4) -> Void: ...
    Component = property(get_Component, put_Component)
    Matrix = property(get_Matrix, put_Matrix)
class Printing3DCompositeMaterial(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing3D.IPrinting3DCompositeMaterial
    _classid_ = 'Windows.Graphics.Printing3D.Printing3DCompositeMaterial'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Graphics.Printing3D.Printing3DCompositeMaterial.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Graphics.Printing3D.Printing3DCompositeMaterial: ...
    @winrt_mixinmethod
    def get_Values(self: win32more.Windows.Graphics.Printing3D.IPrinting3DCompositeMaterial) -> win32more.Windows.Foundation.Collections.IVector[Double]: ...
    Values = property(get_Values, None)
class Printing3DCompositeMaterialGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing3D.IPrinting3DCompositeMaterialGroup
    _classid_ = 'Windows.Graphics.Printing3D.Printing3DCompositeMaterialGroup'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Graphics.Printing3D.Printing3DCompositeMaterialGroup.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Graphics.Printing3D.IPrinting3DCompositeMaterialGroupFactory, MaterialGroupId: UInt32) -> win32more.Windows.Graphics.Printing3D.Printing3DCompositeMaterialGroup: ...
    @winrt_mixinmethod
    def get_Composites(self: win32more.Windows.Graphics.Printing3D.IPrinting3DCompositeMaterialGroup) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DCompositeMaterial]: ...
    @winrt_mixinmethod
    def get_MaterialGroupId(self: win32more.Windows.Graphics.Printing3D.IPrinting3DCompositeMaterialGroup) -> UInt32: ...
    @winrt_mixinmethod
    def get_MaterialIndices(self: win32more.Windows.Graphics.Printing3D.IPrinting3DCompositeMaterialGroup) -> win32more.Windows.Foundation.Collections.IVector[UInt32]: ...
    @winrt_mixinmethod
    def get_BaseMaterialGroup(self: win32more.Windows.Graphics.Printing3D.IPrinting3DCompositeMaterialGroup2) -> win32more.Windows.Graphics.Printing3D.Printing3DBaseMaterialGroup: ...
    @winrt_mixinmethod
    def put_BaseMaterialGroup(self: win32more.Windows.Graphics.Printing3D.IPrinting3DCompositeMaterialGroup2, value: win32more.Windows.Graphics.Printing3D.Printing3DBaseMaterialGroup) -> Void: ...
    BaseMaterialGroup = property(get_BaseMaterialGroup, put_BaseMaterialGroup)
    Composites = property(get_Composites, None)
    MaterialGroupId = property(get_MaterialGroupId, None)
    MaterialIndices = property(get_MaterialIndices, None)
Printing3DContract: UInt32 = 262144
class Printing3DFaceReductionOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing3D.IPrinting3DFaceReductionOptions
    _classid_ = 'Windows.Graphics.Printing3D.Printing3DFaceReductionOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Graphics.Printing3D.Printing3DFaceReductionOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Graphics.Printing3D.Printing3DFaceReductionOptions: ...
    @winrt_mixinmethod
    def get_MaxReductionArea(self: win32more.Windows.Graphics.Printing3D.IPrinting3DFaceReductionOptions) -> Double: ...
    @winrt_mixinmethod
    def put_MaxReductionArea(self: win32more.Windows.Graphics.Printing3D.IPrinting3DFaceReductionOptions, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_TargetTriangleCount(self: win32more.Windows.Graphics.Printing3D.IPrinting3DFaceReductionOptions) -> UInt32: ...
    @winrt_mixinmethod
    def put_TargetTriangleCount(self: win32more.Windows.Graphics.Printing3D.IPrinting3DFaceReductionOptions, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_MaxEdgeLength(self: win32more.Windows.Graphics.Printing3D.IPrinting3DFaceReductionOptions) -> Double: ...
    @winrt_mixinmethod
    def put_MaxEdgeLength(self: win32more.Windows.Graphics.Printing3D.IPrinting3DFaceReductionOptions, value: Double) -> Void: ...
    MaxEdgeLength = property(get_MaxEdgeLength, put_MaxEdgeLength)
    MaxReductionArea = property(get_MaxReductionArea, put_MaxReductionArea)
    TargetTriangleCount = property(get_TargetTriangleCount, put_TargetTriangleCount)
class Printing3DMaterial(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing3D.IPrinting3DMaterial
    _classid_ = 'Windows.Graphics.Printing3D.Printing3DMaterial'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Graphics.Printing3D.Printing3DMaterial.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Graphics.Printing3D.Printing3DMaterial: ...
    @winrt_mixinmethod
    def get_BaseGroups(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMaterial) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DBaseMaterialGroup]: ...
    @winrt_mixinmethod
    def get_ColorGroups(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMaterial) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DColorMaterialGroup]: ...
    @winrt_mixinmethod
    def get_Texture2CoordGroups(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMaterial) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DTexture2CoordMaterialGroup]: ...
    @winrt_mixinmethod
    def get_CompositeGroups(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMaterial) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DCompositeMaterialGroup]: ...
    @winrt_mixinmethod
    def get_MultiplePropertyGroups(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMaterial) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DMultiplePropertyMaterialGroup]: ...
    BaseGroups = property(get_BaseGroups, None)
    ColorGroups = property(get_ColorGroups, None)
    CompositeGroups = property(get_CompositeGroups, None)
    MultiplePropertyGroups = property(get_MultiplePropertyGroups, None)
    Texture2CoordGroups = property(get_Texture2CoordGroups, None)
class Printing3DMesh(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing3D.IPrinting3DMesh
    _classid_ = 'Windows.Graphics.Printing3D.Printing3DMesh'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Graphics.Printing3D.Printing3DMesh.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Graphics.Printing3D.Printing3DMesh: ...
    @winrt_mixinmethod
    def get_VertexCount(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMesh) -> UInt32: ...
    @winrt_mixinmethod
    def put_VertexCount(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMesh, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_IndexCount(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMesh) -> UInt32: ...
    @winrt_mixinmethod
    def put_IndexCount(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMesh, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_VertexPositionsDescription(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMesh) -> win32more.Windows.Graphics.Printing3D.Printing3DBufferDescription: ...
    @winrt_mixinmethod
    def put_VertexPositionsDescription(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMesh, value: win32more.Windows.Graphics.Printing3D.Printing3DBufferDescription) -> Void: ...
    @winrt_mixinmethod
    def get_VertexNormalsDescription(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMesh) -> win32more.Windows.Graphics.Printing3D.Printing3DBufferDescription: ...
    @winrt_mixinmethod
    def put_VertexNormalsDescription(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMesh, value: win32more.Windows.Graphics.Printing3D.Printing3DBufferDescription) -> Void: ...
    @winrt_mixinmethod
    def get_TriangleIndicesDescription(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMesh) -> win32more.Windows.Graphics.Printing3D.Printing3DBufferDescription: ...
    @winrt_mixinmethod
    def put_TriangleIndicesDescription(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMesh, value: win32more.Windows.Graphics.Printing3D.Printing3DBufferDescription) -> Void: ...
    @winrt_mixinmethod
    def get_TriangleMaterialIndicesDescription(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMesh) -> win32more.Windows.Graphics.Printing3D.Printing3DBufferDescription: ...
    @winrt_mixinmethod
    def put_TriangleMaterialIndicesDescription(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMesh, value: win32more.Windows.Graphics.Printing3D.Printing3DBufferDescription) -> Void: ...
    @winrt_mixinmethod
    def GetVertexPositions(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMesh) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def CreateVertexPositions(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMesh, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def GetVertexNormals(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMesh) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def CreateVertexNormals(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMesh, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def GetTriangleIndices(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMesh) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def CreateTriangleIndices(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMesh, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def GetTriangleMaterialIndices(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMesh) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def CreateTriangleMaterialIndices(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMesh, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_BufferDescriptionSet(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMesh) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_mixinmethod
    def get_BufferSet(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMesh) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_mixinmethod
    def VerifyAsync(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMesh, value: win32more.Windows.Graphics.Printing3D.Printing3DMeshVerificationMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Graphics.Printing3D.Printing3DMeshVerificationResult]: ...
    BufferDescriptionSet = property(get_BufferDescriptionSet, None)
    BufferSet = property(get_BufferSet, None)
    IndexCount = property(get_IndexCount, put_IndexCount)
    TriangleIndicesDescription = property(get_TriangleIndicesDescription, put_TriangleIndicesDescription)
    TriangleMaterialIndicesDescription = property(get_TriangleMaterialIndicesDescription, put_TriangleMaterialIndicesDescription)
    VertexCount = property(get_VertexCount, put_VertexCount)
    VertexNormalsDescription = property(get_VertexNormalsDescription, put_VertexNormalsDescription)
    VertexPositionsDescription = property(get_VertexPositionsDescription, put_VertexPositionsDescription)
class Printing3DMeshVerificationMode(Enum, Int32):
    FindFirstError = 0
    FindAllErrors = 1
class Printing3DMeshVerificationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing3D.IPrinting3DMeshVerificationResult
    _classid_ = 'Windows.Graphics.Printing3D.Printing3DMeshVerificationResult'
    @winrt_mixinmethod
    def get_IsValid(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMeshVerificationResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_NonmanifoldTriangles(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMeshVerificationResult) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_mixinmethod
    def get_ReversedNormalTriangles(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMeshVerificationResult) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    IsValid = property(get_IsValid, None)
    NonmanifoldTriangles = property(get_NonmanifoldTriangles, None)
    ReversedNormalTriangles = property(get_ReversedNormalTriangles, None)
class Printing3DModel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing3D.IPrinting3DModel
    _classid_ = 'Windows.Graphics.Printing3D.Printing3DModel'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Graphics.Printing3D.Printing3DModel.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Graphics.Printing3D.Printing3DModel: ...
    @winrt_mixinmethod
    def get_Unit(self: win32more.Windows.Graphics.Printing3D.IPrinting3DModel) -> win32more.Windows.Graphics.Printing3D.Printing3DModelUnit: ...
    @winrt_mixinmethod
    def put_Unit(self: win32more.Windows.Graphics.Printing3D.IPrinting3DModel, value: win32more.Windows.Graphics.Printing3D.Printing3DModelUnit) -> Void: ...
    @winrt_mixinmethod
    def get_Textures(self: win32more.Windows.Graphics.Printing3D.IPrinting3DModel) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DModelTexture]: ...
    @winrt_mixinmethod
    def get_Meshes(self: win32more.Windows.Graphics.Printing3D.IPrinting3DModel) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DMesh]: ...
    @winrt_mixinmethod
    def get_Components(self: win32more.Windows.Graphics.Printing3D.IPrinting3DModel) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DComponent]: ...
    @winrt_mixinmethod
    def get_Material(self: win32more.Windows.Graphics.Printing3D.IPrinting3DModel) -> win32more.Windows.Graphics.Printing3D.Printing3DMaterial: ...
    @winrt_mixinmethod
    def put_Material(self: win32more.Windows.Graphics.Printing3D.IPrinting3DModel, value: win32more.Windows.Graphics.Printing3D.Printing3DMaterial) -> Void: ...
    @winrt_mixinmethod
    def get_Build(self: win32more.Windows.Graphics.Printing3D.IPrinting3DModel) -> win32more.Windows.Graphics.Printing3D.Printing3DComponent: ...
    @winrt_mixinmethod
    def put_Build(self: win32more.Windows.Graphics.Printing3D.IPrinting3DModel, value: win32more.Windows.Graphics.Printing3D.Printing3DComponent) -> Void: ...
    @winrt_mixinmethod
    def get_Version(self: win32more.Windows.Graphics.Printing3D.IPrinting3DModel) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Version(self: win32more.Windows.Graphics.Printing3D.IPrinting3DModel, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_RequiredExtensions(self: win32more.Windows.Graphics.Printing3D.IPrinting3DModel) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Metadata(self: win32more.Windows.Graphics.Printing3D.IPrinting3DModel) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def RepairAsync(self: win32more.Windows.Graphics.Printing3D.IPrinting3DModel) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Clone(self: win32more.Windows.Graphics.Printing3D.IPrinting3DModel) -> win32more.Windows.Graphics.Printing3D.Printing3DModel: ...
    @winrt_mixinmethod
    def TryPartialRepairAsync(self: win32more.Windows.Graphics.Printing3D.IPrinting3DModel2) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryPartialRepairWithTimeAsync(self: win32more.Windows.Graphics.Printing3D.IPrinting3DModel2, maxWaitTime: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryReduceFacesAsync(self: win32more.Windows.Graphics.Printing3D.IPrinting3DModel2) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[Boolean, Double]: ...
    @winrt_mixinmethod
    def TryReduceFacesWithOptionsAsync(self: win32more.Windows.Graphics.Printing3D.IPrinting3DModel2, printing3DFaceReductionOptions: win32more.Windows.Graphics.Printing3D.Printing3DFaceReductionOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[Boolean, Double]: ...
    @winrt_mixinmethod
    def TryReduceFacesWithOptionsAndTimeAsync(self: win32more.Windows.Graphics.Printing3D.IPrinting3DModel2, printing3DFaceReductionOptions: win32more.Windows.Graphics.Printing3D.Printing3DFaceReductionOptions, maxWait: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[Boolean, Double]: ...
    @winrt_mixinmethod
    def RepairWithProgressAsync(self: win32more.Windows.Graphics.Printing3D.IPrinting3DModel2) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[Boolean, Double]: ...
    Build = property(get_Build, put_Build)
    Components = property(get_Components, None)
    Material = property(get_Material, put_Material)
    Meshes = property(get_Meshes, None)
    Metadata = property(get_Metadata, None)
    RequiredExtensions = property(get_RequiredExtensions, None)
    Textures = property(get_Textures, None)
    Unit = property(get_Unit, put_Unit)
    Version = property(get_Version, put_Version)
class Printing3DModelTexture(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing3D.IPrinting3DModelTexture
    _classid_ = 'Windows.Graphics.Printing3D.Printing3DModelTexture'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Graphics.Printing3D.Printing3DModelTexture.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Graphics.Printing3D.Printing3DModelTexture: ...
    @winrt_mixinmethod
    def get_TextureResource(self: win32more.Windows.Graphics.Printing3D.IPrinting3DModelTexture) -> win32more.Windows.Graphics.Printing3D.Printing3DTextureResource: ...
    @winrt_mixinmethod
    def put_TextureResource(self: win32more.Windows.Graphics.Printing3D.IPrinting3DModelTexture, value: win32more.Windows.Graphics.Printing3D.Printing3DTextureResource) -> Void: ...
    @winrt_mixinmethod
    def get_TileStyleU(self: win32more.Windows.Graphics.Printing3D.IPrinting3DModelTexture) -> win32more.Windows.Graphics.Printing3D.Printing3DTextureEdgeBehavior: ...
    @winrt_mixinmethod
    def put_TileStyleU(self: win32more.Windows.Graphics.Printing3D.IPrinting3DModelTexture, value: win32more.Windows.Graphics.Printing3D.Printing3DTextureEdgeBehavior) -> Void: ...
    @winrt_mixinmethod
    def get_TileStyleV(self: win32more.Windows.Graphics.Printing3D.IPrinting3DModelTexture) -> win32more.Windows.Graphics.Printing3D.Printing3DTextureEdgeBehavior: ...
    @winrt_mixinmethod
    def put_TileStyleV(self: win32more.Windows.Graphics.Printing3D.IPrinting3DModelTexture, value: win32more.Windows.Graphics.Printing3D.Printing3DTextureEdgeBehavior) -> Void: ...
    TextureResource = property(get_TextureResource, put_TextureResource)
    TileStyleU = property(get_TileStyleU, put_TileStyleU)
    TileStyleV = property(get_TileStyleV, put_TileStyleV)
class Printing3DModelUnit(Enum, Int32):
    Meter = 0
    Micron = 1
    Millimeter = 2
    Centimeter = 3
    Inch = 4
    Foot = 5
class Printing3DMultiplePropertyMaterial(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing3D.IPrinting3DMultiplePropertyMaterial
    _classid_ = 'Windows.Graphics.Printing3D.Printing3DMultiplePropertyMaterial'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Graphics.Printing3D.Printing3DMultiplePropertyMaterial.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Graphics.Printing3D.Printing3DMultiplePropertyMaterial: ...
    @winrt_mixinmethod
    def get_MaterialIndices(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMultiplePropertyMaterial) -> win32more.Windows.Foundation.Collections.IVector[UInt32]: ...
    MaterialIndices = property(get_MaterialIndices, None)
class Printing3DMultiplePropertyMaterialGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing3D.IPrinting3DMultiplePropertyMaterialGroup
    _classid_ = 'Windows.Graphics.Printing3D.Printing3DMultiplePropertyMaterialGroup'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Graphics.Printing3D.Printing3DMultiplePropertyMaterialGroup.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Graphics.Printing3D.IPrinting3DMultiplePropertyMaterialGroupFactory, MaterialGroupId: UInt32) -> win32more.Windows.Graphics.Printing3D.Printing3DMultiplePropertyMaterialGroup: ...
    @winrt_mixinmethod
    def get_MultipleProperties(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMultiplePropertyMaterialGroup) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DMultiplePropertyMaterial]: ...
    @winrt_mixinmethod
    def get_MaterialGroupIndices(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMultiplePropertyMaterialGroup) -> win32more.Windows.Foundation.Collections.IVector[UInt32]: ...
    @winrt_mixinmethod
    def get_MaterialGroupId(self: win32more.Windows.Graphics.Printing3D.IPrinting3DMultiplePropertyMaterialGroup) -> UInt32: ...
    MaterialGroupId = property(get_MaterialGroupId, None)
    MaterialGroupIndices = property(get_MaterialGroupIndices, None)
    MultipleProperties = property(get_MultipleProperties, None)
class Printing3DObjectType(Enum, Int32):
    Model = 0
    Support = 1
    Others = 2
class Printing3DPackageCompression(Enum, Int32):
    Low = 0
    Medium = 1
    High = 2
class Printing3DTexture2CoordMaterial(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing3D.IPrinting3DTexture2CoordMaterial
    _classid_ = 'Windows.Graphics.Printing3D.Printing3DTexture2CoordMaterial'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Graphics.Printing3D.Printing3DTexture2CoordMaterial.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Graphics.Printing3D.Printing3DTexture2CoordMaterial: ...
    @winrt_mixinmethod
    def get_Texture(self: win32more.Windows.Graphics.Printing3D.IPrinting3DTexture2CoordMaterial) -> win32more.Windows.Graphics.Printing3D.Printing3DModelTexture: ...
    @winrt_mixinmethod
    def put_Texture(self: win32more.Windows.Graphics.Printing3D.IPrinting3DTexture2CoordMaterial, value: win32more.Windows.Graphics.Printing3D.Printing3DModelTexture) -> Void: ...
    @winrt_mixinmethod
    def get_U(self: win32more.Windows.Graphics.Printing3D.IPrinting3DTexture2CoordMaterial) -> Double: ...
    @winrt_mixinmethod
    def put_U(self: win32more.Windows.Graphics.Printing3D.IPrinting3DTexture2CoordMaterial, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_V(self: win32more.Windows.Graphics.Printing3D.IPrinting3DTexture2CoordMaterial) -> Double: ...
    @winrt_mixinmethod
    def put_V(self: win32more.Windows.Graphics.Printing3D.IPrinting3DTexture2CoordMaterial, value: Double) -> Void: ...
    Texture = property(get_Texture, put_Texture)
    U = property(get_U, put_U)
    V = property(get_V, put_V)
class Printing3DTexture2CoordMaterialGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing3D.IPrinting3DTexture2CoordMaterialGroup
    _classid_ = 'Windows.Graphics.Printing3D.Printing3DTexture2CoordMaterialGroup'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Graphics.Printing3D.Printing3DTexture2CoordMaterialGroup.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Graphics.Printing3D.IPrinting3DTexture2CoordMaterialGroupFactory, MaterialGroupId: UInt32) -> win32more.Windows.Graphics.Printing3D.Printing3DTexture2CoordMaterialGroup: ...
    @winrt_mixinmethod
    def get_Texture2Coords(self: win32more.Windows.Graphics.Printing3D.IPrinting3DTexture2CoordMaterialGroup) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Graphics.Printing3D.Printing3DTexture2CoordMaterial]: ...
    @winrt_mixinmethod
    def get_MaterialGroupId(self: win32more.Windows.Graphics.Printing3D.IPrinting3DTexture2CoordMaterialGroup) -> UInt32: ...
    @winrt_mixinmethod
    def get_Texture(self: win32more.Windows.Graphics.Printing3D.IPrinting3DTexture2CoordMaterialGroup2) -> win32more.Windows.Graphics.Printing3D.Printing3DModelTexture: ...
    @winrt_mixinmethod
    def put_Texture(self: win32more.Windows.Graphics.Printing3D.IPrinting3DTexture2CoordMaterialGroup2, value: win32more.Windows.Graphics.Printing3D.Printing3DModelTexture) -> Void: ...
    MaterialGroupId = property(get_MaterialGroupId, None)
    Texture = property(get_Texture, put_Texture)
    Texture2Coords = property(get_Texture2Coords, None)
class Printing3DTextureEdgeBehavior(Enum, Int32):
    None_ = 0
    Wrap = 1
    Mirror = 2
    Clamp = 3
class Printing3DTextureResource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Printing3D.IPrinting3DTextureResource
    _classid_ = 'Windows.Graphics.Printing3D.Printing3DTextureResource'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Graphics.Printing3D.Printing3DTextureResource.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Graphics.Printing3D.Printing3DTextureResource: ...
    @winrt_mixinmethod
    def get_TextureData(self: win32more.Windows.Graphics.Printing3D.IPrinting3DTextureResource) -> win32more.Windows.Storage.Streams.IRandomAccessStreamWithContentType: ...
    @winrt_mixinmethod
    def put_TextureData(self: win32more.Windows.Graphics.Printing3D.IPrinting3DTextureResource, value: win32more.Windows.Storage.Streams.IRandomAccessStreamWithContentType) -> Void: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Graphics.Printing3D.IPrinting3DTextureResource) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: win32more.Windows.Graphics.Printing3D.IPrinting3DTextureResource, value: WinRT_String) -> Void: ...
    Name = property(get_Name, put_Name)
    TextureData = property(get_TextureData, put_TextureData)


make_ready(__name__)
