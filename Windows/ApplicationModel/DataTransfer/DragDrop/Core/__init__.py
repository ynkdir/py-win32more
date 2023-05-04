from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.ApplicationModel.DataTransfer
import Windows.ApplicationModel.DataTransfer.DragDrop
import Windows.ApplicationModel.DataTransfer.DragDrop.Core
import Windows.Foundation
import Windows.Graphics.Imaging
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class CoreDragDropManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragDropManager
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragDropManager'
    @winrt_mixinmethod
    def add_TargetRequested(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragDropManager, value: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragDropManager, Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDropOperationTargetRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TargetRequested(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragDropManager, value: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_AreConcurrentOperationsEnabled(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragDropManager) -> Boolean: ...
    @winrt_mixinmethod
    def put_AreConcurrentOperationsEnabled(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragDropManager, value: Boolean) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragDropManagerStatics) -> Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragDropManager: ...
    AreConcurrentOperationsEnabled = property(get_AreConcurrentOperationsEnabled, put_AreConcurrentOperationsEnabled)
class CoreDragInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragInfo
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragInfo'
    @winrt_mixinmethod
    def get_Data(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragInfo) -> Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_mixinmethod
    def get_Modifiers(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragInfo) -> Windows.ApplicationModel.DataTransfer.DragDrop.DragDropModifiers: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragInfo) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_AllowedOperations(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragInfo2) -> Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    Data = property(get_Data, None)
    Modifiers = property(get_Modifiers, None)
    Position = property(get_Position, None)
    AllowedOperations = property(get_AllowedOperations, None)
class CoreDragOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragOperation
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragOperation'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragOperation: ...
    @winrt_mixinmethod
    def get_Data(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragOperation) -> Windows.ApplicationModel.DataTransfer.DataPackage: ...
    @winrt_mixinmethod
    def SetPointerId(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragOperation, pointerId: UInt32) -> Void: ...
    @winrt_mixinmethod
    def SetDragUIContentFromSoftwareBitmap(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragOperation, softwareBitmap: Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    @winrt_mixinmethod
    def SetDragUIContentFromSoftwareBitmapWithAnchorPoint(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragOperation, softwareBitmap: Windows.Graphics.Imaging.SoftwareBitmap, anchorPoint: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_DragUIContentMode(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragOperation) -> Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragUIContentMode: ...
    @winrt_mixinmethod
    def put_DragUIContentMode(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragOperation, value: Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragUIContentMode) -> Void: ...
    @winrt_mixinmethod
    def StartAsync(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragOperation) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.DataTransfer.DataPackageOperation]: ...
    @winrt_mixinmethod
    def get_AllowedOperations(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragOperation2) -> Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    @winrt_mixinmethod
    def put_AllowedOperations(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragOperation2, value: Windows.ApplicationModel.DataTransfer.DataPackageOperation) -> Void: ...
    Data = property(get_Data, None)
    DragUIContentMode = property(get_DragUIContentMode, put_DragUIContentMode)
    AllowedOperations = property(get_AllowedOperations, put_AllowedOperations)
CoreDragUIContentMode = UInt32
CoreDragUIContentMode_Auto: CoreDragUIContentMode = 0
CoreDragUIContentMode_Deferred: CoreDragUIContentMode = 1
class CoreDragUIOverride(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragUIOverride
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragUIOverride'
    @winrt_mixinmethod
    def SetContentFromSoftwareBitmap(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragUIOverride, softwareBitmap: Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    @winrt_mixinmethod
    def SetContentFromSoftwareBitmapWithAnchorPoint(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragUIOverride, softwareBitmap: Windows.Graphics.Imaging.SoftwareBitmap, anchorPoint: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_IsContentVisible(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragUIOverride) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsContentVisible(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragUIOverride, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Caption(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragUIOverride) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Caption(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragUIOverride, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsCaptionVisible(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragUIOverride) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsCaptionVisible(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragUIOverride, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsGlyphVisible(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragUIOverride) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsGlyphVisible(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragUIOverride, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragUIOverride) -> Void: ...
    IsContentVisible = property(get_IsContentVisible, put_IsContentVisible)
    Caption = property(get_Caption, put_Caption)
    IsCaptionVisible = property(get_IsCaptionVisible, put_IsCaptionVisible)
    IsGlyphVisible = property(get_IsGlyphVisible, put_IsGlyphVisible)
class CoreDropOperationTargetRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDropOperationTargetRequestedEventArgs
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDropOperationTargetRequestedEventArgs'
    @winrt_mixinmethod
    def SetTarget(self: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDropOperationTargetRequestedEventArgs, target: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDropOperationTarget) -> Void: ...
class ICoreDragDropManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragDropManager'
    _iid_ = Guid('{7d56d344-8464-4faf-aa49-37ea6e2d7bd1}')
    @winrt_commethod(6)
    def add_TargetRequested(self, value: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragDropManager, Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDropOperationTargetRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_TargetRequested(self, value: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_AreConcurrentOperationsEnabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_AreConcurrentOperationsEnabled(self, value: Boolean) -> Void: ...
    AreConcurrentOperationsEnabled = property(get_AreConcurrentOperationsEnabled, put_AreConcurrentOperationsEnabled)
class ICoreDragDropManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragDropManagerStatics'
    _iid_ = Guid('{9542fdca-da12-4c1c-8d06-041db29733c3}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragDropManager: ...
class ICoreDragInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragInfo'
    _iid_ = Guid('{48353a8b-cb50-464e-9575-cd4e3a7ab028}')
    @winrt_commethod(6)
    def get_Data(self) -> Windows.ApplicationModel.DataTransfer.DataPackageView: ...
    @winrt_commethod(7)
    def get_Modifiers(self) -> Windows.ApplicationModel.DataTransfer.DragDrop.DragDropModifiers: ...
    @winrt_commethod(8)
    def get_Position(self) -> Windows.Foundation.Point: ...
    Data = property(get_Data, None)
    Modifiers = property(get_Modifiers, None)
    Position = property(get_Position, None)
class ICoreDragInfo2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragInfo2'
    _iid_ = Guid('{c54691e5-e6fb-4d74-b4b1-8a3c17f25e9e}')
    @winrt_commethod(6)
    def get_AllowedOperations(self) -> Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    AllowedOperations = property(get_AllowedOperations, None)
class ICoreDragOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragOperation'
    _iid_ = Guid('{cc06de4f-6db0-4e62-ab1b-a74a02dc6d85}')
    @winrt_commethod(6)
    def get_Data(self) -> Windows.ApplicationModel.DataTransfer.DataPackage: ...
    @winrt_commethod(7)
    def SetPointerId(self, pointerId: UInt32) -> Void: ...
    @winrt_commethod(8)
    def SetDragUIContentFromSoftwareBitmap(self, softwareBitmap: Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    @winrt_commethod(9)
    def SetDragUIContentFromSoftwareBitmapWithAnchorPoint(self, softwareBitmap: Windows.Graphics.Imaging.SoftwareBitmap, anchorPoint: Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(10)
    def get_DragUIContentMode(self) -> Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragUIContentMode: ...
    @winrt_commethod(11)
    def put_DragUIContentMode(self, value: Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragUIContentMode) -> Void: ...
    @winrt_commethod(12)
    def StartAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.DataTransfer.DataPackageOperation]: ...
    Data = property(get_Data, None)
    DragUIContentMode = property(get_DragUIContentMode, put_DragUIContentMode)
class ICoreDragOperation2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragOperation2'
    _iid_ = Guid('{824b1e2c-d99a-4fc3-8507-6c182f33b46a}')
    @winrt_commethod(6)
    def get_AllowedOperations(self) -> Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    @winrt_commethod(7)
    def put_AllowedOperations(self, value: Windows.ApplicationModel.DataTransfer.DataPackageOperation) -> Void: ...
    AllowedOperations = property(get_AllowedOperations, put_AllowedOperations)
class ICoreDragUIOverride(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDragUIOverride'
    _iid_ = Guid('{89a85064-3389-4f4f-8897-7e8a3ffb3c93}')
    @winrt_commethod(6)
    def SetContentFromSoftwareBitmap(self, softwareBitmap: Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    @winrt_commethod(7)
    def SetContentFromSoftwareBitmapWithAnchorPoint(self, softwareBitmap: Windows.Graphics.Imaging.SoftwareBitmap, anchorPoint: Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(8)
    def get_IsContentVisible(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsContentVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_Caption(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_Caption(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_IsCaptionVisible(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IsCaptionVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_IsGlyphVisible(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_IsGlyphVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def Clear(self) -> Void: ...
    IsContentVisible = property(get_IsContentVisible, put_IsContentVisible)
    Caption = property(get_Caption, put_Caption)
    IsCaptionVisible = property(get_IsCaptionVisible, put_IsCaptionVisible)
    IsGlyphVisible = property(get_IsGlyphVisible, put_IsGlyphVisible)
class ICoreDropOperationTarget(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDropOperationTarget'
    _iid_ = Guid('{d9126196-4c5b-417d-bb37-76381def8db4}')
    @winrt_commethod(6)
    def EnterAsync(self, dragInfo: Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragInfo, dragUIOverride: Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragUIOverride) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.DataTransfer.DataPackageOperation]: ...
    @winrt_commethod(7)
    def OverAsync(self, dragInfo: Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragInfo, dragUIOverride: Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragUIOverride) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.DataTransfer.DataPackageOperation]: ...
    @winrt_commethod(8)
    def LeaveAsync(self, dragInfo: Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragInfo) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def DropAsync(self, dragInfo: Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragInfo) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.DataTransfer.DataPackageOperation]: ...
class ICoreDropOperationTargetRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDropOperationTargetRequestedEventArgs'
    _iid_ = Guid('{2aca929a-5e28-4ea6-829e-29134e665d6d}')
    @winrt_commethod(6)
    def SetTarget(self, target: Windows.ApplicationModel.DataTransfer.DragDrop.Core.ICoreDropOperationTarget) -> Void: ...
make_head(_module, 'CoreDragDropManager')
make_head(_module, 'CoreDragInfo')
make_head(_module, 'CoreDragOperation')
make_head(_module, 'CoreDragUIOverride')
make_head(_module, 'CoreDropOperationTargetRequestedEventArgs')
make_head(_module, 'ICoreDragDropManager')
make_head(_module, 'ICoreDragDropManagerStatics')
make_head(_module, 'ICoreDragInfo')
make_head(_module, 'ICoreDragInfo2')
make_head(_module, 'ICoreDragOperation')
make_head(_module, 'ICoreDragOperation2')
make_head(_module, 'ICoreDragUIOverride')
make_head(_module, 'ICoreDropOperationTarget')
make_head(_module, 'ICoreDropOperationTargetRequestedEventArgs')
