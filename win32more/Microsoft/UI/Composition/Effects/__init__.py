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
import win32more.Microsoft.UI.Composition.Effects
import win32more.Windows.Graphics.Effects
class ISceneLightingEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Effects.ISceneLightingEffect'
    _iid_ = Guid('{eb1e7316-114c-5950-8480-20a29a3bb1ee}')
    @winrt_commethod(6)
    def get_AmbientAmount(self) -> Single: ...
    @winrt_commethod(7)
    def put_AmbientAmount(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_DiffuseAmount(self) -> Single: ...
    @winrt_commethod(9)
    def put_DiffuseAmount(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def get_NormalMapSource(self) -> win32more.Windows.Graphics.Effects.IGraphicsEffectSource: ...
    @winrt_commethod(11)
    def put_NormalMapSource(self, value: win32more.Windows.Graphics.Effects.IGraphicsEffectSource) -> Void: ...
    @winrt_commethod(12)
    def get_SpecularAmount(self) -> Single: ...
    @winrt_commethod(13)
    def put_SpecularAmount(self, value: Single) -> Void: ...
    @winrt_commethod(14)
    def get_SpecularShine(self) -> Single: ...
    @winrt_commethod(15)
    def put_SpecularShine(self, value: Single) -> Void: ...
    AmbientAmount = property(get_AmbientAmount, put_AmbientAmount)
    DiffuseAmount = property(get_DiffuseAmount, put_DiffuseAmount)
    NormalMapSource = property(get_NormalMapSource, put_NormalMapSource)
    SpecularAmount = property(get_SpecularAmount, put_SpecularAmount)
    SpecularShine = property(get_SpecularShine, put_SpecularShine)
class ISceneLightingEffect2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Effects.ISceneLightingEffect2'
    _iid_ = Guid('{6b6496b2-468d-50d1-bbe9-593b8263ad80}')
    @winrt_commethod(6)
    def get_ReflectanceModel(self) -> win32more.Microsoft.UI.Composition.Effects.SceneLightingEffectReflectanceModel: ...
    @winrt_commethod(7)
    def put_ReflectanceModel(self, value: win32more.Microsoft.UI.Composition.Effects.SceneLightingEffectReflectanceModel) -> Void: ...
    ReflectanceModel = property(get_ReflectanceModel, put_ReflectanceModel)
class SceneLightingEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Composition.Effects.ISceneLightingEffect
    _classid_ = 'Microsoft.UI.Composition.Effects.SceneLightingEffect'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Composition.Effects.SceneLightingEffect: ...
    @winrt_mixinmethod
    def put_Name(self: win32more.Windows.Graphics.Effects.IGraphicsEffect, name: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def put_SpecularAmount(self: win32more.Microsoft.UI.Composition.Effects.ISceneLightingEffect, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_SpecularShine(self: win32more.Microsoft.UI.Composition.Effects.ISceneLightingEffect) -> Single: ...
    @winrt_mixinmethod
    def put_SpecularShine(self: win32more.Microsoft.UI.Composition.Effects.ISceneLightingEffect, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_ReflectanceModel(self: win32more.Microsoft.UI.Composition.Effects.ISceneLightingEffect2) -> win32more.Microsoft.UI.Composition.Effects.SceneLightingEffectReflectanceModel: ...
    @winrt_mixinmethod
    def put_ReflectanceModel(self: win32more.Microsoft.UI.Composition.Effects.ISceneLightingEffect2, value: win32more.Microsoft.UI.Composition.Effects.SceneLightingEffectReflectanceModel) -> Void: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Graphics.Effects.IGraphicsEffect) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AmbientAmount(self: win32more.Microsoft.UI.Composition.Effects.ISceneLightingEffect) -> Single: ...
    @winrt_mixinmethod
    def put_AmbientAmount(self: win32more.Microsoft.UI.Composition.Effects.ISceneLightingEffect, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_DiffuseAmount(self: win32more.Microsoft.UI.Composition.Effects.ISceneLightingEffect) -> Single: ...
    @winrt_mixinmethod
    def put_DiffuseAmount(self: win32more.Microsoft.UI.Composition.Effects.ISceneLightingEffect, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_NormalMapSource(self: win32more.Microsoft.UI.Composition.Effects.ISceneLightingEffect) -> win32more.Windows.Graphics.Effects.IGraphicsEffectSource: ...
    @winrt_mixinmethod
    def put_NormalMapSource(self: win32more.Microsoft.UI.Composition.Effects.ISceneLightingEffect, value: win32more.Windows.Graphics.Effects.IGraphicsEffectSource) -> Void: ...
    @winrt_mixinmethod
    def get_SpecularAmount(self: win32more.Microsoft.UI.Composition.Effects.ISceneLightingEffect) -> Single: ...
    Name = property(get_Name, put_Name)
    SpecularAmount = property(get_SpecularAmount, put_SpecularAmount)
    SpecularShine = property(get_SpecularShine, put_SpecularShine)
    ReflectanceModel = property(get_ReflectanceModel, put_ReflectanceModel)
    AmbientAmount = property(get_AmbientAmount, put_AmbientAmount)
    DiffuseAmount = property(get_DiffuseAmount, put_DiffuseAmount)
    NormalMapSource = property(get_NormalMapSource, put_NormalMapSource)
SceneLightingEffectReflectanceModel = Int32
SceneLightingEffectReflectanceModel_BlinnPhong: SceneLightingEffectReflectanceModel = 0
SceneLightingEffectReflectanceModel_PhysicallyBasedBlinnPhong: SceneLightingEffectReflectanceModel = 1
make_ready(__name__)
