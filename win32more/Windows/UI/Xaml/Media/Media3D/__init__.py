from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.UI.Xaml
import win32more.Windows.UI.Xaml.Media.Media3D
import win32more.Windows.Win32.System.WinRT
class _CompositeTransform3D_Meta_(ComPtr.__class__):
    pass
class CompositeTransform3D(ComPtr, metaclass=_CompositeTransform3D_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Media3D.Transform3D
    default_interface: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D
    _classid_ = 'Windows.UI.Xaml.Media.Media3D.CompositeTransform3D'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Media3D.CompositeTransform3D.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Media3D.CompositeTransform3D: ...
    @winrt_mixinmethod
    def get_CenterX(self: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_CenterX(self: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CenterY(self: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_CenterY(self: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CenterZ(self: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_CenterZ(self: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RotationX(self: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_RotationX(self: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RotationY(self: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_RotationY(self: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RotationZ(self: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_RotationZ(self: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleX(self: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_ScaleX(self: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleY(self: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_ScaleY(self: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleZ(self: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_ScaleZ(self: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_TranslateX(self: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_TranslateX(self: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_TranslateY(self: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_TranslateY(self: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_TranslateZ(self: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_TranslateZ(self: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3D, value: Double) -> Void: ...
    @winrt_classmethod
    def get_CenterXProperty(cls: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterYProperty(cls: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterZProperty(cls: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RotationXProperty(cls: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RotationYProperty(cls: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RotationZProperty(cls: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ScaleXProperty(cls: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ScaleYProperty(cls: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ScaleZProperty(cls: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TranslateXProperty(cls: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TranslateYProperty(cls: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TranslateZProperty(cls: win32more.Windows.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Media3D.ICompositeTransform3DStatics'
    _iid_ = Guid('{ddbf4d67-2a25-48f3-9808-c51ec3d55bec}')
    @winrt_commethod(6)
    def get_CenterXProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_CenterYProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_CenterZProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_RotationXProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_RotationYProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_RotationZProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_ScaleXProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_ScaleYProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_ScaleZProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_TranslateXProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_TranslateYProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(17)
    def get_TranslateZProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Media3D.IMatrix3DHelper'
    _iid_ = Guid('{e48c10ef-9927-4c9b-8213-07775512ba04}')
class IMatrix3DHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Media3D.IMatrix3DHelperStatics'
    _iid_ = Guid('{9264545e-e158-4e74-8899-689160bd2f8c}')
    @winrt_commethod(6)
    def get_Identity(self) -> win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_commethod(7)
    def Multiply(self, matrix1: win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D, matrix2: win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D) -> win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_commethod(8)
    def FromElements(self, m11: Double, m12: Double, m13: Double, m14: Double, m21: Double, m22: Double, m23: Double, m24: Double, m31: Double, m32: Double, m33: Double, m34: Double, offsetX: Double, offsetY: Double, offsetZ: Double, m44: Double) -> win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_commethod(9)
    def GetHasInverse(self, target: win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D) -> Boolean: ...
    @winrt_commethod(10)
    def GetIsIdentity(self, target: win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D) -> Boolean: ...
    @winrt_commethod(11)
    def Invert(self, target: win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D) -> win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D: ...
    Identity = property(get_Identity, None)
class IPerspectiveTransform3D(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Media3D.IPerspectiveTransform3DStatics'
    _iid_ = Guid('{8e6f6400-620c-48c7-844d-3f0984da5b17}')
    @winrt_commethod(6)
    def get_DepthProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_OffsetXProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_OffsetYProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    DepthProperty = property(get_DepthProperty, None)
    OffsetXProperty = property(get_OffsetXProperty, None)
    OffsetYProperty = property(get_OffsetYProperty, None)
class ITransform3D(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Media3D.ITransform3D'
    _iid_ = Guid('{ae3ed43a-a9fc-4c31-86cd-56d9ca251a69}')
class ITransform3DFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.Media3D.ITransform3DFactory'
    _iid_ = Guid('{052c1f7a-8d73-48cd-bbb8-d00434caae5d}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Media3D.Transform3D: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Media.Media3D.IMatrix3DHelper
    _classid_ = 'Windows.UI.Xaml.Media.Media3D.Matrix3DHelper'
    @winrt_classmethod
    def get_Identity(cls: win32more.Windows.UI.Xaml.Media.Media3D.IMatrix3DHelperStatics) -> win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_classmethod
    def Multiply(cls: win32more.Windows.UI.Xaml.Media.Media3D.IMatrix3DHelperStatics, matrix1: win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D, matrix2: win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D) -> win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_classmethod
    def FromElements(cls: win32more.Windows.UI.Xaml.Media.Media3D.IMatrix3DHelperStatics, m11: Double, m12: Double, m13: Double, m14: Double, m21: Double, m22: Double, m23: Double, m24: Double, m31: Double, m32: Double, m33: Double, m34: Double, offsetX: Double, offsetY: Double, offsetZ: Double, m44: Double) -> win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_classmethod
    def GetHasInverse(cls: win32more.Windows.UI.Xaml.Media.Media3D.IMatrix3DHelperStatics, target: win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D) -> Boolean: ...
    @winrt_classmethod
    def GetIsIdentity(cls: win32more.Windows.UI.Xaml.Media.Media3D.IMatrix3DHelperStatics, target: win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D) -> Boolean: ...
    @winrt_classmethod
    def Invert(cls: win32more.Windows.UI.Xaml.Media.Media3D.IMatrix3DHelperStatics, target: win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D) -> win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D: ...
    _Matrix3DHelper_Meta_.Identity = property(get_Identity, None)
class _PerspectiveTransform3D_Meta_(ComPtr.__class__):
    pass
class PerspectiveTransform3D(ComPtr, metaclass=_PerspectiveTransform3D_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Media3D.Transform3D
    default_interface: win32more.Windows.UI.Xaml.Media.Media3D.IPerspectiveTransform3D
    _classid_ = 'Windows.UI.Xaml.Media.Media3D.PerspectiveTransform3D'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Media3D.PerspectiveTransform3D.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Media3D.PerspectiveTransform3D: ...
    @winrt_mixinmethod
    def get_Depth(self: win32more.Windows.UI.Xaml.Media.Media3D.IPerspectiveTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_Depth(self: win32more.Windows.UI.Xaml.Media.Media3D.IPerspectiveTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_OffsetX(self: win32more.Windows.UI.Xaml.Media.Media3D.IPerspectiveTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_OffsetX(self: win32more.Windows.UI.Xaml.Media.Media3D.IPerspectiveTransform3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_OffsetY(self: win32more.Windows.UI.Xaml.Media.Media3D.IPerspectiveTransform3D) -> Double: ...
    @winrt_mixinmethod
    def put_OffsetY(self: win32more.Windows.UI.Xaml.Media.Media3D.IPerspectiveTransform3D, value: Double) -> Void: ...
    @winrt_classmethod
    def get_DepthProperty(cls: win32more.Windows.UI.Xaml.Media.Media3D.IPerspectiveTransform3DStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OffsetXProperty(cls: win32more.Windows.UI.Xaml.Media.Media3D.IPerspectiveTransform3DStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OffsetYProperty(cls: win32more.Windows.UI.Xaml.Media.Media3D.IPerspectiveTransform3DStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Depth = property(get_Depth, put_Depth)
    OffsetX = property(get_OffsetX, put_OffsetX)
    OffsetY = property(get_OffsetY, put_OffsetY)
    _PerspectiveTransform3D_Meta_.DepthProperty = property(get_DepthProperty, None)
    _PerspectiveTransform3D_Meta_.OffsetXProperty = property(get_OffsetXProperty, None)
    _PerspectiveTransform3D_Meta_.OffsetYProperty = property(get_OffsetYProperty, None)
class Transform3D(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Media.Media3D.ITransform3D
    _classid_ = 'Windows.UI.Xaml.Media.Media3D.Transform3D'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Media3D.Transform3D.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Media.Media3D.ITransform3DFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Media3D.Transform3D: ...


make_ready(__name__)
