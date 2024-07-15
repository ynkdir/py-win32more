from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Graphics.Effects
import win32more.Windows.UI.Composition.Effects
import win32more.Windows.Win32.System.WinRT
class ISceneLightingEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Effects.ISceneLightingEffect'
    _iid_ = Guid('{91bb5e52-95d1-4f8b-9a5a-6408b24b8c6a}')
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
    _classid_ = 'Windows.UI.Composition.Effects.ISceneLightingEffect2'
    _iid_ = Guid('{9e270e81-72f0-4c5c-95f8-8a6e0024f409}')
    @winrt_commethod(6)
    def get_ReflectanceModel(self) -> win32more.Windows.UI.Composition.Effects.SceneLightingEffectReflectanceModel: ...
    @winrt_commethod(7)
    def put_ReflectanceModel(self, value: win32more.Windows.UI.Composition.Effects.SceneLightingEffectReflectanceModel) -> Void: ...
    ReflectanceModel = property(get_ReflectanceModel, put_ReflectanceModel)
class SceneLightingEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Composition.Effects.ISceneLightingEffect
    _classid_ = 'Windows.UI.Composition.Effects.SceneLightingEffect'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Composition.Effects.SceneLightingEffect.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Composition.Effects.SceneLightingEffect: ...
    @winrt_mixinmethod
    def get_AmbientAmount(self: win32more.Windows.UI.Composition.Effects.ISceneLightingEffect) -> Single: ...
    @winrt_mixinmethod
    def put_AmbientAmount(self: win32more.Windows.UI.Composition.Effects.ISceneLightingEffect, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_DiffuseAmount(self: win32more.Windows.UI.Composition.Effects.ISceneLightingEffect) -> Single: ...
    @winrt_mixinmethod
    def put_DiffuseAmount(self: win32more.Windows.UI.Composition.Effects.ISceneLightingEffect, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_NormalMapSource(self: win32more.Windows.UI.Composition.Effects.ISceneLightingEffect) -> win32more.Windows.Graphics.Effects.IGraphicsEffectSource: ...
    @winrt_mixinmethod
    def put_NormalMapSource(self: win32more.Windows.UI.Composition.Effects.ISceneLightingEffect, value: win32more.Windows.Graphics.Effects.IGraphicsEffectSource) -> Void: ...
    @winrt_mixinmethod
    def get_SpecularAmount(self: win32more.Windows.UI.Composition.Effects.ISceneLightingEffect) -> Single: ...
    @winrt_mixinmethod
    def put_SpecularAmount(self: win32more.Windows.UI.Composition.Effects.ISceneLightingEffect, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_SpecularShine(self: win32more.Windows.UI.Composition.Effects.ISceneLightingEffect) -> Single: ...
    @winrt_mixinmethod
    def put_SpecularShine(self: win32more.Windows.UI.Composition.Effects.ISceneLightingEffect, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_ReflectanceModel(self: win32more.Windows.UI.Composition.Effects.ISceneLightingEffect2) -> win32more.Windows.UI.Composition.Effects.SceneLightingEffectReflectanceModel: ...
    @winrt_mixinmethod
    def put_ReflectanceModel(self: win32more.Windows.UI.Composition.Effects.ISceneLightingEffect2, value: win32more.Windows.UI.Composition.Effects.SceneLightingEffectReflectanceModel) -> Void: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Graphics.Effects.IGraphicsEffect) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: win32more.Windows.Graphics.Effects.IGraphicsEffect, name: WinRT_String) -> Void: ...
    AmbientAmount = property(get_AmbientAmount, put_AmbientAmount)
    DiffuseAmount = property(get_DiffuseAmount, put_DiffuseAmount)
    Name = property(get_Name, put_Name)
    NormalMapSource = property(get_NormalMapSource, put_NormalMapSource)
    ReflectanceModel = property(get_ReflectanceModel, put_ReflectanceModel)
    SpecularAmount = property(get_SpecularAmount, put_SpecularAmount)
    SpecularShine = property(get_SpecularShine, put_SpecularShine)
class SceneLightingEffectReflectanceModel(Enum, Int32):
    BlinnPhong = 0
    PhysicallyBasedBlinnPhong = 1


make_ready(__name__)
