from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Microsoft.UI.Content
import win32more.Microsoft.UI.Input
import win32more.Microsoft.UI.Input.DragDrop
import win32more.Windows.ApplicationModel.DataTransfer
import win32more.Windows.Foundation
import win32more.Windows.Graphics.Imaging
class DragDropManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.DragDrop.IDragDropManager
    _classid_ = 'Microsoft.UI.Input.DragDrop.DragDropManager'
    @winrt_mixinmethod
    def put_AreConcurrentOperationsEnabled(self: win32more.Microsoft.UI.Input.DragDrop.IDragDropManager, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def add_TargetRequested(self: win32more.Microsoft.UI.Input.DragDrop.IDragDropManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.DragDrop.DragDropManager, win32more.Microsoft.UI.Input.DragDrop.DropOperationTargetRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TargetRequested(self: win32more.Microsoft.UI.Input.DragDrop.IDragDropManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_AreConcurrentOperationsEnabled(self: win32more.Microsoft.UI.Input.DragDrop.IDragDropManager) -> Boolean: ...
    @winrt_classmethod
    def GetForIsland(cls: win32more.Microsoft.UI.Input.DragDrop.IDragDropManagerStatics, content: win32more.Microsoft.UI.Content.ContentIsland) -> win32more.Microsoft.UI.Input.DragDrop.DragDropManager: ...
    AreConcurrentOperationsEnabled = property(get_AreConcurrentOperationsEnabled, put_AreConcurrentOperationsEnabled)
DragDropModifiers = UInt32
DragDropModifiers_None: DragDropModifiers = 0
DragDropModifiers_Shift: DragDropModifiers = 1
DragDropModifiers_Control: DragDropModifiers = 2
DragDropModifiers_Alt: DragDropModifiers = 4
DragDropModifiers_LeftButton: DragDropModifiers = 8
DragDropModifiers_MiddleButton: DragDropModifiers = 16
DragDropModifiers_RightButton: DragDropModifiers = 32
class DragInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.DragDrop.IDragInfo
    _classid_ = 'Microsoft.UI.Input.DragDrop.DragInfo'
    @winrt_mixinmethod
    def get_Modifiers(self: win32more.Microsoft.UI.Input.DragDrop.IDragInfo) -> win32more.Microsoft.UI.Input.DragDrop.DragDropModifiers: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Microsoft.UI.Input.DragDrop.IDragInfo) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Microsoft.UI.Input.DragDrop.IDragInfo) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_AllowedOperations(self: win32more.Microsoft.UI.Input.DragDrop.IDragInfo) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    Modifiers = property(get_Modifiers, None)
    Data = property(get_Data, None)
    Position = property(get_Position, None)
    AllowedOperations = property(get_AllowedOperations, None)
class DragOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.DragDrop.IDragOperation
    _classid_ = 'Microsoft.UI.Input.DragDrop.DragOperation'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Input.DragDrop.DragOperation: ...
    @winrt_mixinmethod
    def get_AllowedOperations(self: win32more.Microsoft.UI.Input.DragDrop.IDragOperation) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    @winrt_mixinmethod
    def put_AllowedOperations(self: win32more.Microsoft.UI.Input.DragDrop.IDragOperation, value: win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation) -> Void: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Microsoft.UI.Input.DragDrop.IDragOperation) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackage: ...
    @winrt_mixinmethod
    def get_DragUIContentMode(self: win32more.Microsoft.UI.Input.DragDrop.IDragOperation) -> win32more.Microsoft.UI.Input.DragDrop.DragUIContentMode: ...
    @winrt_mixinmethod
    def put_DragUIContentMode(self: win32more.Microsoft.UI.Input.DragDrop.IDragOperation, value: win32more.Microsoft.UI.Input.DragDrop.DragUIContentMode) -> Void: ...
    @winrt_mixinmethod
    def SetDragUIContentFromSoftwareBitmap(self: win32more.Microsoft.UI.Input.DragDrop.IDragOperation, bitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    @winrt_mixinmethod
    def SetDragUIContentFromSoftwareBitmap2(self: win32more.Microsoft.UI.Input.DragDrop.IDragOperation, bitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap, anchorPoint: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def StartAsync(self: win32more.Microsoft.UI.Input.DragDrop.IDragOperation, initialTarget: win32more.Microsoft.UI.Input.DragDrop.DragDropManager, initialPointerPoint: win32more.Microsoft.UI.Input.PointerPoint) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    AllowedOperations = property(get_AllowedOperations, put_AllowedOperations)
    Data = property(get_Data, None)
    DragUIContentMode = property(get_DragUIContentMode, put_DragUIContentMode)
DragUIContentMode = Int32
DragUIContentMode_Auto: DragUIContentMode = 0
DragUIContentMode_Deferred: DragUIContentMode = 1
class DragUIOverride(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.DragDrop.IDragUIOverride
    _classid_ = 'Microsoft.UI.Input.DragDrop.DragUIOverride'
    @winrt_mixinmethod
    def get_IsCaptionVisible(self: win32more.Microsoft.UI.Input.DragDrop.IDragUIOverride) -> Boolean: ...
    @winrt_mixinmethod
    def put_Caption(self: win32more.Microsoft.UI.Input.DragDrop.IDragUIOverride, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Caption(self: win32more.Microsoft.UI.Input.DragDrop.IDragUIOverride) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_IsCaptionVisible(self: win32more.Microsoft.UI.Input.DragDrop.IDragUIOverride, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsContentVisible(self: win32more.Microsoft.UI.Input.DragDrop.IDragUIOverride) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsContentVisible(self: win32more.Microsoft.UI.Input.DragDrop.IDragUIOverride, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsGlyphVisible(self: win32more.Microsoft.UI.Input.DragDrop.IDragUIOverride) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsGlyphVisible(self: win32more.Microsoft.UI.Input.DragDrop.IDragUIOverride, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Microsoft.UI.Input.DragDrop.IDragUIOverride) -> Void: ...
    @winrt_mixinmethod
    def SetContentFromSoftwareBitmap(self: win32more.Microsoft.UI.Input.DragDrop.IDragUIOverride, bitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    @winrt_mixinmethod
    def SetContentFromSoftwareBitmap2(self: win32more.Microsoft.UI.Input.DragDrop.IDragUIOverride, bitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap, anchorPoint: win32more.Windows.Foundation.Point) -> Void: ...
    IsCaptionVisible = property(get_IsCaptionVisible, put_IsCaptionVisible)
    Caption = property(get_Caption, put_Caption)
    IsContentVisible = property(get_IsContentVisible, put_IsContentVisible)
    IsGlyphVisible = property(get_IsGlyphVisible, put_IsGlyphVisible)
class DropOperationTargetRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.DragDrop.IDropOperationTargetRequestedEventArgs
    _classid_ = 'Microsoft.UI.Input.DragDrop.DropOperationTargetRequestedEventArgs'
    @winrt_mixinmethod
    def SetTarget(self: win32more.Microsoft.UI.Input.DragDrop.IDropOperationTargetRequestedEventArgs, target: win32more.Microsoft.UI.Input.DragDrop.IDropOperationTarget) -> Void: ...
class IDragDropManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.DragDrop.IDragDropManager'
    _iid_ = Guid('{4fea9efc-b073-5fbe-9c95-a4113ef6393f}')
    @winrt_commethod(6)
    def get_AreConcurrentOperationsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AreConcurrentOperationsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def add_TargetRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.DragDrop.DragDropManager, win32more.Microsoft.UI.Input.DragDrop.DropOperationTargetRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_TargetRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AreConcurrentOperationsEnabled = property(get_AreConcurrentOperationsEnabled, put_AreConcurrentOperationsEnabled)
class IDragDropManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.DragDrop.IDragDropManagerStatics'
    _iid_ = Guid('{5587c863-57d7-5d0f-8ea9-e5dcf06a0f83}')
    @winrt_commethod(6)
    def GetForIsland(self, content: win32more.Microsoft.UI.Content.ContentIsland) -> win32more.Microsoft.UI.Input.DragDrop.DragDropManager: ...
class IDragInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.DragDrop.IDragInfo'
    _iid_ = Guid('{7507d891-62a8-5a79-a880-ac7353d001ec}')
    @winrt_commethod(6)
    def get_AllowedOperations(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    @winrt_commethod(7)
    def get_Data(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_commethod(8)
    def get_Modifiers(self) -> win32more.Microsoft.UI.Input.DragDrop.DragDropModifiers: ...
    @winrt_commethod(9)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    AllowedOperations = property(get_AllowedOperations, None)
    Data = property(get_Data, None)
    Modifiers = property(get_Modifiers, None)
    Position = property(get_Position, None)
class IDragOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.DragDrop.IDragOperation'
    _iid_ = Guid('{ef122288-7984-53d3-8488-133dcd3de793}')
    @winrt_commethod(6)
    def get_AllowedOperations(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    @winrt_commethod(7)
    def put_AllowedOperations(self, value: win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation) -> Void: ...
    @winrt_commethod(8)
    def get_Data(self) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackage: ...
    @winrt_commethod(9)
    def get_DragUIContentMode(self) -> win32more.Microsoft.UI.Input.DragDrop.DragUIContentMode: ...
    @winrt_commethod(10)
    def put_DragUIContentMode(self, value: win32more.Microsoft.UI.Input.DragDrop.DragUIContentMode) -> Void: ...
    @winrt_commethod(11)
    def SetDragUIContentFromSoftwareBitmap(self, bitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    @winrt_commethod(12)
    def SetDragUIContentFromSoftwareBitmap2(self, bitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap, anchorPoint: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(13)
    def StartAsync(self, initialTarget: win32more.Microsoft.UI.Input.DragDrop.DragDropManager, initialPointerPoint: win32more.Microsoft.UI.Input.PointerPoint) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation]: ...
    AllowedOperations = property(get_AllowedOperations, put_AllowedOperations)
    Data = property(get_Data, None)
    DragUIContentMode = property(get_DragUIContentMode, put_DragUIContentMode)
class IDragUIOverride(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.DragDrop.IDragUIOverride'
    _iid_ = Guid('{8432fbac-a17f-5a95-8f56-fb432280b54d}')
    @winrt_commethod(6)
    def get_Caption(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Caption(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_IsCaptionVisible(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsCaptionVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_IsContentVisible(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsContentVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_IsGlyphVisible(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IsGlyphVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def Clear(self) -> Void: ...
    @winrt_commethod(15)
    def SetContentFromSoftwareBitmap(self, bitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    @winrt_commethod(16)
    def SetContentFromSoftwareBitmap2(self, bitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap, anchorPoint: win32more.Windows.Foundation.Point) -> Void: ...
    Caption = property(get_Caption, put_Caption)
    IsCaptionVisible = property(get_IsCaptionVisible, put_IsCaptionVisible)
    IsContentVisible = property(get_IsContentVisible, put_IsContentVisible)
    IsGlyphVisible = property(get_IsGlyphVisible, put_IsGlyphVisible)
class IDropOperationTarget(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.DragDrop.IDropOperationTarget'
    _iid_ = Guid('{1c2707d9-0065-53c7-bbfb-50850378caf3}')
    @winrt_commethod(6)
    def DropAsync(self, dragInfo: win32more.Microsoft.UI.Input.DragDrop.DragInfo) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation]: ...
    @winrt_commethod(7)
    def EnterAsync(self, dragInfo: win32more.Microsoft.UI.Input.DragDrop.DragInfo, dragUIOverride: win32more.Microsoft.UI.Input.DragDrop.DragUIOverride) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation]: ...
    @winrt_commethod(8)
    def LeaveAsync(self, dragInfo: win32more.Microsoft.UI.Input.DragDrop.DragInfo) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def OverAsync(self, dragInfo: win32more.Microsoft.UI.Input.DragDrop.DragInfo, dragUIOverride: win32more.Microsoft.UI.Input.DragDrop.DragUIOverride) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation]: ...
class IDropOperationTargetRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.DragDrop.IDropOperationTargetRequestedEventArgs'
    _iid_ = Guid('{f61c5b62-720e-59ff-ad0b-e77fc5b8a4a3}')
    @winrt_commethod(6)
    def SetTarget(self, target: win32more.Microsoft.UI.Input.DragDrop.IDropOperationTarget) -> Void: ...
make_ready(__name__)
