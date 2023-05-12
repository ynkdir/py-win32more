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
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.UI.Xaml
import Windows.UI.Xaml.Media.Media3D
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class _CompositeTransform3D_Meta_(ComPtr.__class__):
    pass
class CompositeTransform3D(ComPtr, metaclass=_CompositeTransform3D_Meta_):
    extends: Windows.UI.Xaml.Media.Media3D.Transform3D
    default_interface: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D
    _classid_ = 'Windows.UI.Xaml.Media.Media3D.CompositeTransform3D'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Media3D.CompositeTransform3D: ...
    @winrt_mixinmethod
    def get_CenterX(self: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_CenterX(self: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CenterY(self: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_CenterY(self: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CenterZ(self: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_CenterZ(self: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RotationX(self: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_RotationX(self: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RotationY(self: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_RotationY(self: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RotationZ(self: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_RotationZ(self: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleX(self: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_ScaleX(self: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleY(self: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_ScaleY(self: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleZ(self: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_ScaleZ(self: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_TranslateX(self: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_TranslateX(self: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_TranslateY(self: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_TranslateY(self: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_TranslateZ(self: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_TranslateZ(self: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_classmethod
    def get_CenterXProperty(cls: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterYProperty(cls: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterZProperty(cls: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RotationXProperty(cls: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RotationYProperty(cls: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RotationZProperty(cls: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ScaleXProperty(cls: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ScaleYProperty(cls: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ScaleZProperty(cls: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TranslateXProperty(cls: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TranslateYProperty(cls: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TranslateZProperty(cls: Windows.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    CenterX = property(get_CenterX, put_CenterX)
    CenterY = property(get_CenterY, put_CenterY)
    CenterZ = property(get_CenterZ, put_CenterZ)
    RotationX = property(get_RotationX, put_RotationX)
    RotationY = property(get_RotationY, put_RotationY)
    RotationZ = property(get_RotationZ, put_RotationZ)
    ScaleX = property(get_ScaleX, put_ScaleX)
    ScaleY = property(get_ScaleY, put_ScaleY)
    ScaleZ = property(get_ScaleZ, put_ScaleZ)
    TranslateX = property(get_TranslateX, put_TranslateX)
    TranslateY = property(get_TranslateY, put_TranslateY)
    TranslateZ = property(get_TranslateZ, put_TranslateZ)
    _CompositeTransform3D_Meta_.CenterXProperty = property(get_CenterXProperty.__wrapped__, None)
    _CompositeTransform3D_Meta_.CenterYProperty = property(get_CenterYProperty.__wrapped__, None)
    _CompositeTransform3D_Meta_.CenterZProperty = property(get_CenterZProperty.__wrapped__, None)
    _CompositeTransform3D_Meta_.RotationXProperty = property(get_RotationXProperty.__wrapped__, None)
    _CompositeTransform3D_Meta_.RotationYProperty = property(get_RotationYProperty.__wrapped__, None)
    _CompositeTransform3D_Meta_.RotationZProperty = property(get_RotationZProperty.__wrapped__, None)
    _CompositeTransform3D_Meta_.ScaleXProperty = property(get_ScaleXProperty.__wrapped__, None)
    _CompositeTransform3D_Meta_.ScaleYProperty = property(get_ScaleYProperty.__wrapped__, None)
    _CompositeTransform3D_Meta_.ScaleZProperty = property(get_ScaleZProperty.__wrapped__, None)
    _CompositeTransform3D_Meta_.TranslateXProperty = property(get_TranslateXProperty.__wrapped__, None)
    _CompositeTransform3D_Meta_.TranslateYProperty = property(get_TranslateYProperty.__wrapped__, None)
    _CompositeTransform3D_Meta_.TranslateZProperty = property(get_TranslateZProperty.__wrapped__, None)
class ICompositeTransform3D(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D'
    _iid_ = Guid('{8977cb01-af8d-4af5-b084-c08eb9704abe}')
    @winrt_commethod(6)
    def get_CenterX(self) -> Double: ...
    @winrt_commethod(7)
    def put_CenterX(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_CenterY(self) -> Double: ...
    @winrt_commethod(9)
    def put_CenterY(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_CenterZ(self) -> Double: ...
    @winrt_commethod(11)
    def put_CenterZ(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_RotationX(self) -> Double: ...
    @winrt_commethod(13)
    def put_RotationX(self, value: Double) -> Void: ...
    @winrt_commethod(14)
    def get_RotationY(self) -> Double: ...
    @winrt_commethod(15)
    def put_RotationY(self, value: Double) -> Void: ...
    @winrt_commethod(16)
    def get_RotationZ(self) -> Double: ...
    @winrt_commethod(17)
    def put_RotationZ(self, value: Double) -> Void: ...
    @winrt_commethod(18)
    def get_ScaleX(self) -> Double: ...
    @winrt_commethod(19)
    def put_ScaleX(self, value: Double) -> Void: ...
    @winrt_commethod(20)
    def get_ScaleY(self) -> Double: ...
    @winrt_commethod(21)
    def put_ScaleY(self, value: Double) -> Void: ...
    @winrt_commethod(22)
    def get_ScaleZ(self) -> Double: ...
    @winrt_commethod(23)
    def put_ScaleZ(self, value: Double) -> Void: ...
    @winrt_commethod(24)
    def get_TranslateX(self) -> Double: ...
    @winrt_commethod(25)
    def put_TranslateX(self, value: Double) -> Void: ...
    @winrt_commethod(26)
    def get_TranslateY(self) -> Double: ...
    @winrt_commethod(27)
    def put_TranslateY(self, value: Double) -> Void: ...
    @winrt_commethod(28)
    def get_TranslateZ(self) -> Double: ...
    @winrt_commethod(29)
    def put_TranslateZ(self, value: Double) -> Void: ...
    CenterX = property(get_CenterX, put_CenterX)
    CenterY = property(get_CenterY, put_CenterY)
    CenterZ = property(get_CenterZ, put_CenterZ)
    RotationX = property(get_RotationX, put_RotationX)
    RotationY = property(get_RotationY, put_RotationY)
    RotationZ = property(get_RotationZ, put_RotationZ)
    ScaleX = property(get_ScaleX, put_ScaleX)
    ScaleY = property(get_ScaleY, put_ScaleY)
    ScaleZ = property(get_ScaleZ, put_ScaleZ)
    TranslateX = property(get_TranslateX, put_TranslateX)
    TranslateY = property(get_TranslateY, put_TranslateY)
    TranslateZ = property(get_TranslateZ, put_TranslateZ)
class ICompositeTransform3DStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics'
    _iid_ = Guid('{ddbf4d67-2a25-48f3-9808-c51ec3d55bec}')
    @winrt_commethod(6)
    def get_CenterXProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_CenterYProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_CenterZProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_RotationXProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_RotationYProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_RotationZProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_ScaleXProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_ScaleYProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_ScaleZProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_TranslateXProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_TranslateYProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(17)
    def get_TranslateZProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    CenterXProperty = property(get_CenterXProperty, None)
    CenterYProperty = property(get_CenterYProperty, None)
    CenterZProperty = property(get_CenterZProperty, None)
    RotationXProperty = property(get_RotationXProperty, None)
    RotationYProperty = property(get_RotationYProperty, None)
    RotationZProperty = property(get_RotationZProperty, None)
    ScaleXProperty = property(get_ScaleXProperty, None)
    ScaleYProperty = property(get_ScaleYProperty, None)
    ScaleZProperty = property(get_ScaleZProperty, None)
    TranslateXProperty = property(get_TranslateXProperty, None)
    TranslateYProperty = property(get_TranslateYProperty, None)
    TranslateZProperty = property(get_TranslateZProperty, None)
class IMatrix3DHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Media3D.IMatrix3DHelper'
    _iid_ = Guid('{e48c10ef-9927-4c9b-8213-07775512ba04}')
class IMatrix3DHelperStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Media3D.IMatrix3DHelperStatics'
    _iid_ = Guid('{9264545e-e158-4e74-8899-689160bd2f8c}')
    @winrt_commethod(6)
    def get_Identity(self) -> Windows.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_commethod(7)
    def Multiply(self, matrix1: Windows.UI.Xaml.Media.Media3D.Matrix3D, matrix2: Windows.UI.Xaml.Media.Media3D.Matrix3D) -> Windows.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_commethod(8)
    def FromElements(self, m11: Double, m12: Double, m13: Double, m14: Double, m21: Double, m22: Double, m23: Double, m24: Double, m31: Double, m32: Double, m33: Double, m34: Double, offsetX: Double, offsetY: Double, offsetZ: Double, m44: Double) -> Windows.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_commethod(9)
    def GetHasInverse(self, target: Windows.UI.Xaml.Media.Media3D.Matrix3D) -> Boolean: ...
    @winrt_commethod(10)
    def GetIsIdentity(self, target: Windows.UI.Xaml.Media.Media3D.Matrix3D) -> Boolean: ...
    @winrt_commethod(11)
    def Invert(self, target: Windows.UI.Xaml.Media.Media3D.Matrix3D) -> Windows.UI.Xaml.Media.Media3D.Matrix3D: ...
    Identity = property(get_Identity, None)
class IPerspectiveTransform3D(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Media3D.IPerspectiveTransform3D'
    _iid_ = Guid('{9a7b532a-30f9-40a1-96c9-c59d87f95ac3}')
    @winrt_commethod(6)
    def get_Depth(self) -> Double: ...
    @winrt_commethod(7)
    def put_Depth(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_OffsetX(self) -> Double: ...
    @winrt_commethod(9)
    def put_OffsetX(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_OffsetY(self) -> Double: ...
    @winrt_commethod(11)
    def put_OffsetY(self, value: Double) -> Void: ...
    Depth = property(get_Depth, put_Depth)
    OffsetX = property(get_OffsetX, put_OffsetX)
    OffsetY = property(get_OffsetY, put_OffsetY)
class IPerspectiveTransform3DStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Media3D.IPerspectiveTransform3DStatics'
    _iid_ = Guid('{8e6f6400-620c-48c7-844d-3f0984da5b17}')
    @winrt_commethod(6)
    def get_DepthProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_OffsetXProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_OffsetYProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    DepthProperty = property(get_DepthProperty, None)
    OffsetXProperty = property(get_OffsetXProperty, None)
    OffsetYProperty = property(get_OffsetYProperty, None)
class ITransform3D(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Media3D.ITransform3D'
    _iid_ = Guid('{ae3ed43a-a9fc-4c31-86cd-56d9ca251a69}')
class ITransform3DFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Media3D.ITransform3DFactory'
    _iid_ = Guid('{052c1f7a-8d73-48cd-bbb8-d00434caae5d}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Media3D.Transform3D: ...
class Matrix3D(EasyCastStructure):
    M11: Double
    M12: Double
    M13: Double
    M14: Double
    M21: Double
    M22: Double
    M23: Double
    M24: Double
    M31: Double
    M32: Double
    M33: Double
    M34: Double
    OffsetX: Double
    OffsetY: Double
    OffsetZ: Double
    M44: Double
class _Matrix3DHelper_Meta_(ComPtr.__class__):
    pass
class Matrix3DHelper(ComPtr, metaclass=_Matrix3DHelper_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Media.Media3D.IMatrix3DHelper
    _classid_ = 'Windows.UI.Xaml.Media.Media3D.Matrix3DHelper'
    @winrt_classmethod
    def get_Identity(cls: Windows.UI.Xaml.Media.Media3D.IMatrix3DHelperStatics) -> Windows.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_classmethod
    def Multiply(cls: Windows.UI.Xaml.Media.Media3D.IMatrix3DHelperStatics, matrix1: Windows.UI.Xaml.Media.Media3D.Matrix3D, matrix2: Windows.UI.Xaml.Media.Media3D.Matrix3D) -> Windows.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_classmethod
    def FromElements(cls: Windows.UI.Xaml.Media.Media3D.IMatrix3DHelperStatics, m11: Double, m12: Double, m13: Double, m14: Double, m21: Double, m22: Double, m23: Double, m24: Double, m31: Double, m32: Double, m33: Double, m34: Double, offsetX: Double, offsetY: Double, offsetZ: Double, m44: Double) -> Windows.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_classmethod
    def GetHasInverse(cls: Windows.UI.Xaml.Media.Media3D.IMatrix3DHelperStatics, target: Windows.UI.Xaml.Media.Media3D.Matrix3D) -> Boolean: ...
    @winrt_classmethod
    def GetIsIdentity(cls: Windows.UI.Xaml.Media.Media3D.IMatrix3DHelperStatics, target: Windows.UI.Xaml.Media.Media3D.Matrix3D) -> Boolean: ...
    @winrt_classmethod
    def Invert(cls: Windows.UI.Xaml.Media.Media3D.IMatrix3DHelperStatics, target: Windows.UI.Xaml.Media.Media3D.Matrix3D) -> Windows.UI.Xaml.Media.Media3D.Matrix3D: ...
    _Matrix3DHelper_Meta_.Identity = property(get_Identity.__wrapped__, None)
class _PerspectiveTransform3D_Meta_(ComPtr.__class__):
    pass
class PerspectiveTransform3D(ComPtr, metaclass=_PerspectiveTransform3D_Meta_):
    extends: Windows.UI.Xaml.Media.Media3D.Transform3D
    default_interface: Windows.UI.Xaml.Media.Media3D.IPerspectiveTransform3D
    _classid_ = 'Windows.UI.Xaml.Media.Media3D.PerspectiveTransform3D'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Media.Media3D.PerspectiveTransform3D: ...
    @winrt_mixinmethod
    def get_Depth(self: Windows.UI.Xaml.Media.Media3D.IPerspectiveTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_Depth(self: Windows.UI.Xaml.Media.Media3D.IPerspectiveTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_OffsetX(self: Windows.UI.Xaml.Media.Media3D.IPerspectiveTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_OffsetX(self: Windows.UI.Xaml.Media.Media3D.IPerspectiveTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_OffsetY(self: Windows.UI.Xaml.Media.Media3D.IPerspectiveTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_OffsetY(self: Windows.UI.Xaml.Media.Media3D.IPerspectiveTransform3D, value: Double) -> Void: ...
    @winrt_classmethod
    def get_DepthProperty(cls: Windows.UI.Xaml.Media.Media3D.IPerspectiveTransform3DStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OffsetXProperty(cls: Windows.UI.Xaml.Media.Media3D.IPerspectiveTransform3DStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OffsetYProperty(cls: Windows.UI.Xaml.Media.Media3D.IPerspectiveTransform3DStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Depth = property(get_Depth, put_Depth)
    OffsetX = property(get_OffsetX, put_OffsetX)
    OffsetY = property(get_OffsetY, put_OffsetY)
    _PerspectiveTransform3D_Meta_.DepthProperty = property(get_DepthProperty.__wrapped__, None)
    _PerspectiveTransform3D_Meta_.OffsetXProperty = property(get_OffsetXProperty.__wrapped__, None)
    _PerspectiveTransform3D_Meta_.OffsetYProperty = property(get_OffsetYProperty.__wrapped__, None)
class Transform3D(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Media.Media3D.ITransform3D
    _classid_ = 'Windows.UI.Xaml.Media.Media3D.Transform3D'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.Media.Media3D.ITransform3DFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Media3D.Transform3D: ...
make_head(_module, 'CompositeTransform3D')
make_head(_module, 'ICompositeTransform3D')
make_head(_module, 'ICompositeTransform3DStatics')
make_head(_module, 'IMatrix3DHelper')
make_head(_module, 'IMatrix3DHelperStatics')
make_head(_module, 'IPerspectiveTransform3D')
make_head(_module, 'IPerspectiveTransform3DStatics')
make_head(_module, 'ITransform3D')
make_head(_module, 'ITransform3DFactory')
make_head(_module, 'Matrix3D')
make_head(_module, 'Matrix3DHelper')
make_head(_module, 'PerspectiveTransform3D')
make_head(_module, 'Transform3D')
