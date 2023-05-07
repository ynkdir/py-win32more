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
import Windows.Graphics.Effects
import Windows.UI.Composition.Effects
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ISceneLightingEffect(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Effects.ISceneLightingEffect'
    _iid_ = Guid('{91bb5e52-95d1-4f8b-9a5a-6408b24b8c6a}')
    @winrt_commethod(6)
    def get_AmbientAmount(self: Windows.UI.Composition.Effects.ISceneLightingEffect) -> Single: ...
    @winrt_commethod(7)
    def put_AmbientAmount(self: Windows.UI.Composition.Effects.ISceneLightingEffect, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_DiffuseAmount(self: Windows.UI.Composition.Effects.ISceneLightingEffect) -> Single: ...
    @winrt_commethod(9)
    def put_DiffuseAmount(self: Windows.UI.Composition.Effects.ISceneLightingEffect, value: Single) -> Void: ...
    @winrt_commethod(10)
    def get_NormalMapSource(self: Windows.UI.Composition.Effects.ISceneLightingEffect) -> Windows.Graphics.Effects.IGraphicsEffectSource: ...
    @winrt_commethod(11)
    def put_NormalMapSource(self: Windows.UI.Composition.Effects.ISceneLightingEffect, value: Windows.Graphics.Effects.IGraphicsEffectSource) -> Void: ...
    @winrt_commethod(12)
    def get_SpecularAmount(self: Windows.UI.Composition.Effects.ISceneLightingEffect) -> Single: ...
    @winrt_commethod(13)
    def put_SpecularAmount(self: Windows.UI.Composition.Effects.ISceneLightingEffect, value: Single) -> Void: ...
    @winrt_commethod(14)
    def get_SpecularShine(self: Windows.UI.Composition.Effects.ISceneLightingEffect) -> Single: ...
    @winrt_commethod(15)
    def put_SpecularShine(self: Windows.UI.Composition.Effects.ISceneLightingEffect, value: Single) -> Void: ...
    AmbientAmount = property(get_AmbientAmount, put_AmbientAmount)
    DiffuseAmount = property(get_DiffuseAmount, put_DiffuseAmount)
    NormalMapSource = property(get_NormalMapSource, put_NormalMapSource)
    SpecularAmount = property(get_SpecularAmount, put_SpecularAmount)
    SpecularShine = property(get_SpecularShine, put_SpecularShine)
class ISceneLightingEffect2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Effects.ISceneLightingEffect2'
    _iid_ = Guid('{9e270e81-72f0-4c5c-95f8-8a6e0024f409}')
    @winrt_commethod(6)
    def get_ReflectanceModel(self: Windows.UI.Composition.Effects.ISceneLightingEffect2) -> Windows.UI.Composition.Effects.SceneLightingEffectReflectanceModel: ...
    @winrt_commethod(7)
    def put_ReflectanceModel(self: Windows.UI.Composition.Effects.ISceneLightingEffect2, value: Windows.UI.Composition.Effects.SceneLightingEffectReflectanceModel) -> Void: ...
    ReflectanceModel = property(get_ReflectanceModel, put_ReflectanceModel)
class SceneLightingEffect(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Composition.Effects.ISceneLightingEffect
    _classid_ = 'Windows.UI.Composition.Effects.SceneLightingEffect'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Composition.Effects.SceneLightingEffect: ...
    @winrt_mixinmethod
    def get_AmbientAmount(self: Windows.UI.Composition.Effects.ISceneLightingEffect) -> Single: ...
    @winrt_mixinmethod
    def put_AmbientAmount(self: Windows.UI.Composition.Effects.ISceneLightingEffect, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_DiffuseAmount(self: Windows.UI.Composition.Effects.ISceneLightingEffect) -> Single: ...
    @winrt_mixinmethod
    def put_DiffuseAmount(self: Windows.UI.Composition.Effects.ISceneLightingEffect, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_NormalMapSource(self: Windows.UI.Composition.Effects.ISceneLightingEffect) -> Windows.Graphics.Effects.IGraphicsEffectSource: ...
    @winrt_mixinmethod
    def put_NormalMapSource(self: Windows.UI.Composition.Effects.ISceneLightingEffect, value: Windows.Graphics.Effects.IGraphicsEffectSource) -> Void: ...
    @winrt_mixinmethod
    def get_SpecularAmount(self: Windows.UI.Composition.Effects.ISceneLightingEffect) -> Single: ...
    @winrt_mixinmethod
    def put_SpecularAmount(self: Windows.UI.Composition.Effects.ISceneLightingEffect, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_SpecularShine(self: Windows.UI.Composition.Effects.ISceneLightingEffect) -> Single: ...
    @winrt_mixinmethod
    def put_SpecularShine(self: Windows.UI.Composition.Effects.ISceneLightingEffect, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_ReflectanceModel(self: Windows.UI.Composition.Effects.ISceneLightingEffect2) -> Windows.UI.Composition.Effects.SceneLightingEffectReflectanceModel: ...
    @winrt_mixinmethod
    def put_ReflectanceModel(self: Windows.UI.Composition.Effects.ISceneLightingEffect2, value: Windows.UI.Composition.Effects.SceneLightingEffectReflectanceModel) -> Void: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.Graphics.Effects.IGraphicsEffect) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: Windows.Graphics.Effects.IGraphicsEffect, name: WinRT_String) -> Void: ...
    AmbientAmount = property(get_AmbientAmount, put_AmbientAmount)
    DiffuseAmount = property(get_DiffuseAmount, put_DiffuseAmount)
    NormalMapSource = property(get_NormalMapSource, put_NormalMapSource)
    SpecularAmount = property(get_SpecularAmount, put_SpecularAmount)
    SpecularShine = property(get_SpecularShine, put_SpecularShine)
    ReflectanceModel = property(get_ReflectanceModel, put_ReflectanceModel)
    Name = property(get_Name, put_Name)
SceneLightingEffectReflectanceModel = Int32
SceneLightingEffectReflectanceModel_BlinnPhong: SceneLightingEffectReflectanceModel = 0
SceneLightingEffectReflectanceModel_PhysicallyBasedBlinnPhong: SceneLightingEffectReflectanceModel = 1
make_head(_module, 'ISceneLightingEffect')
make_head(_module, 'ISceneLightingEffect2')
make_head(_module, 'SceneLightingEffect')
