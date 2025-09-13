from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Microsoft.UI.Xaml
import win32more.Microsoft.UI.Xaml.Media.Media3D
class _CompositeTransform3D_Meta_(ComPtr.__class__):
    pass
class CompositeTransform3D(ComPtr, metaclass=_CompositeTransform3D_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Media3D.Transform3D
    default_interface: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3D
    _classid_ = 'Microsoft.UI.Xaml.Media.Media3D.CompositeTransform3D'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Media3D.CompositeTransform3D.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Media3D.CompositeTransform3D: ...
    @winrt_mixinmethod
    def get_CenterX(self: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_CenterX(self: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CenterY(self: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_CenterY(self: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CenterZ(self: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_CenterZ(self: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RotationX(self: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_RotationX(self: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RotationY(self: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_RotationY(self: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RotationZ(self: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_RotationZ(self: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleX(self: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_ScaleX(self: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleY(self: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_ScaleY(self: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleZ(self: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_ScaleZ(self: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_TranslateX(self: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_TranslateX(self: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_TranslateY(self: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_TranslateY(self: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_TranslateZ(self: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_TranslateZ(self: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_classmethod
    def get_CenterXProperty(cls: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterYProperty(cls: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterZProperty(cls: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RotationXProperty(cls: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RotationYProperty(cls: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RotationZProperty(cls: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ScaleXProperty(cls: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ScaleYProperty(cls: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ScaleZProperty(cls: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TranslateXProperty(cls: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TranslateYProperty(cls: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TranslateZProperty(cls: win32more.Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
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
    _CompositeTransform3D_Meta_.CenterXProperty = property(get_CenterXProperty, None)
    _CompositeTransform3D_Meta_.CenterYProperty = property(get_CenterYProperty, None)
    _CompositeTransform3D_Meta_.CenterZProperty = property(get_CenterZProperty, None)
    _CompositeTransform3D_Meta_.RotationXProperty = property(get_RotationXProperty, None)
    _CompositeTransform3D_Meta_.RotationYProperty = property(get_RotationYProperty, None)
    _CompositeTransform3D_Meta_.RotationZProperty = property(get_RotationZProperty, None)
    _CompositeTransform3D_Meta_.ScaleXProperty = property(get_ScaleXProperty, None)
    _CompositeTransform3D_Meta_.ScaleYProperty = property(get_ScaleYProperty, None)
    _CompositeTransform3D_Meta_.ScaleZProperty = property(get_ScaleZProperty, None)
    _CompositeTransform3D_Meta_.TranslateXProperty = property(get_TranslateXProperty, None)
    _CompositeTransform3D_Meta_.TranslateYProperty = property(get_TranslateYProperty, None)
    _CompositeTransform3D_Meta_.TranslateZProperty = property(get_TranslateZProperty, None)
class ICompositeTransform3D(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3D'
    _iid_ = Guid('{cbaf163f-c254-5dcf-8ae4-40e21ce1b4ca}')
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
    extends: IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics'
    _iid_ = Guid('{b64d4181-6988-5d46-858a-224db7089dc4}')
    @winrt_commethod(6)
    def get_CenterXProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_CenterYProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_CenterZProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_RotationXProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_RotationYProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_RotationZProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_ScaleXProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_ScaleYProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_ScaleZProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_TranslateXProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_TranslateYProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(17)
    def get_TranslateZProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
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
    extends: IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Media3D.IMatrix3DHelper'
    _iid_ = Guid('{d2909be1-9c28-5b38-b63c-88e838644533}')
class IMatrix3DHelperStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Media3D.IMatrix3DHelperStatics'
    _iid_ = Guid('{930e447b-265c-5ded-9e64-57b8933c55c3}')
    @winrt_commethod(6)
    def get_Identity(self) -> win32more.Microsoft.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_commethod(7)
    def Multiply(self, matrix1: win32more.Microsoft.UI.Xaml.Media.Media3D.Matrix3D, matrix2: win32more.Microsoft.UI.Xaml.Media.Media3D.Matrix3D) -> win32more.Microsoft.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_commethod(8)
    def FromElements(self, m11: Double, m12: Double, m13: Double, m14: Double, m21: Double, m22: Double, m23: Double, m24: Double, m31: Double, m32: Double, m33: Double, m34: Double, offsetX: Double, offsetY: Double, offsetZ: Double, m44: Double) -> win32more.Microsoft.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_commethod(9)
    def GetHasInverse(self, target: win32more.Microsoft.UI.Xaml.Media.Media3D.Matrix3D) -> Boolean: ...
    @winrt_commethod(10)
    def GetIsIdentity(self, target: win32more.Microsoft.UI.Xaml.Media.Media3D.Matrix3D) -> Boolean: ...
    @winrt_commethod(11)
    def Invert(self, target: win32more.Microsoft.UI.Xaml.Media.Media3D.Matrix3D) -> win32more.Microsoft.UI.Xaml.Media.Media3D.Matrix3D: ...
    Identity = property(get_Identity, None)
class IPerspectiveTransform3D(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Media3D.IPerspectiveTransform3D'
    _iid_ = Guid('{4006cc46-684e-54ea-a421-dae5b0556b85}')
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
    extends: IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Media3D.IPerspectiveTransform3DStatics'
    _iid_ = Guid('{3b16aa8d-0ee2-5d46-a723-dc8e5c1c0b19}')
    @winrt_commethod(6)
    def get_DepthProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_OffsetXProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_OffsetYProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    DepthProperty = property(get_DepthProperty, None)
    OffsetXProperty = property(get_OffsetXProperty, None)
    OffsetYProperty = property(get_OffsetYProperty, None)
class ITransform3D(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Media3D.ITransform3D'
    _iid_ = Guid('{afea4941-2e49-533c-9f8f-2c126ef9893a}')
class ITransform3DFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.Media3D.ITransform3DFactory'
    _iid_ = Guid('{9bcce0a1-10ac-5319-bdf1-548d2e5ae504}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: IInspectable, innerInterface: POINTER(IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Media3D.Transform3D: ...
class Matrix3D(Structure):
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
    extends: IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Media.Media3D.IMatrix3DHelper
    _classid_ = 'Microsoft.UI.Xaml.Media.Media3D.Matrix3DHelper'
    @winrt_classmethod
    def get_Identity(cls: win32more.Microsoft.UI.Xaml.Media.Media3D.IMatrix3DHelperStatics) -> win32more.Microsoft.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_classmethod
    def Multiply(cls: win32more.Microsoft.UI.Xaml.Media.Media3D.IMatrix3DHelperStatics, matrix1: win32more.Microsoft.UI.Xaml.Media.Media3D.Matrix3D, matrix2: win32more.Microsoft.UI.Xaml.Media.Media3D.Matrix3D) -> win32more.Microsoft.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_classmethod
    def FromElements(cls: win32more.Microsoft.UI.Xaml.Media.Media3D.IMatrix3DHelperStatics, m11: Double, m12: Double, m13: Double, m14: Double, m21: Double, m22: Double, m23: Double, m24: Double, m31: Double, m32: Double, m33: Double, m34: Double, offsetX: Double, offsetY: Double, offsetZ: Double, m44: Double) -> win32more.Microsoft.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_classmethod
    def GetHasInverse(cls: win32more.Microsoft.UI.Xaml.Media.Media3D.IMatrix3DHelperStatics, target: win32more.Microsoft.UI.Xaml.Media.Media3D.Matrix3D) -> Boolean: ...
    @winrt_classmethod
    def GetIsIdentity(cls: win32more.Microsoft.UI.Xaml.Media.Media3D.IMatrix3DHelperStatics, target: win32more.Microsoft.UI.Xaml.Media.Media3D.Matrix3D) -> Boolean: ...
    @winrt_classmethod
    def Invert(cls: win32more.Microsoft.UI.Xaml.Media.Media3D.IMatrix3DHelperStatics, target: win32more.Microsoft.UI.Xaml.Media.Media3D.Matrix3D) -> win32more.Microsoft.UI.Xaml.Media.Media3D.Matrix3D: ...
    _Matrix3DHelper_Meta_.Identity = property(get_Identity, None)
class _PerspectiveTransform3D_Meta_(ComPtr.__class__):
    pass
class PerspectiveTransform3D(ComPtr, metaclass=_PerspectiveTransform3D_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Media3D.Transform3D
    default_interface: win32more.Microsoft.UI.Xaml.Media.Media3D.IPerspectiveTransform3D
    _classid_ = 'Microsoft.UI.Xaml.Media.Media3D.PerspectiveTransform3D'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Media3D.PerspectiveTransform3D.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Media3D.PerspectiveTransform3D: ...
    @winrt_mixinmethod
    def get_Depth(self: win32more.Microsoft.UI.Xaml.Media.Media3D.IPerspectiveTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_Depth(self: win32more.Microsoft.UI.Xaml.Media.Media3D.IPerspectiveTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_OffsetX(self: win32more.Microsoft.UI.Xaml.Media.Media3D.IPerspectiveTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_OffsetX(self: win32more.Microsoft.UI.Xaml.Media.Media3D.IPerspectiveTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_OffsetY(self: win32more.Microsoft.UI.Xaml.Media.Media3D.IPerspectiveTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_OffsetY(self: win32more.Microsoft.UI.Xaml.Media.Media3D.IPerspectiveTransform3D, value: Double) -> Void: ...
    @winrt_classmethod
    def get_DepthProperty(cls: win32more.Microsoft.UI.Xaml.Media.Media3D.IPerspectiveTransform3DStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OffsetXProperty(cls: win32more.Microsoft.UI.Xaml.Media.Media3D.IPerspectiveTransform3DStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OffsetYProperty(cls: win32more.Microsoft.UI.Xaml.Media.Media3D.IPerspectiveTransform3DStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Depth = property(get_Depth, put_Depth)
    OffsetX = property(get_OffsetX, put_OffsetX)
    OffsetY = property(get_OffsetY, put_OffsetY)
    _PerspectiveTransform3D_Meta_.DepthProperty = property(get_DepthProperty, None)
    _PerspectiveTransform3D_Meta_.OffsetXProperty = property(get_OffsetXProperty, None)
    _PerspectiveTransform3D_Meta_.OffsetYProperty = property(get_OffsetYProperty, None)
class Transform3D(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Media.Media3D.ITransform3D
    _classid_ = 'Microsoft.UI.Xaml.Media.Media3D.Transform3D'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Media3D.Transform3D.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Media.Media3D.ITransform3DFactory, baseInterface: IInspectable, innerInterface: POINTER(IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Media3D.Transform3D: ...


make_ready(__name__)
