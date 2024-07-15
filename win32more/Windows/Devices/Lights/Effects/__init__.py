from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Lights
import win32more.Windows.Devices.Lights.Effects
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Graphics.Imaging
import win32more.Windows.UI
import win32more.Windows.Win32.System.WinRT
class ILampArrayBitmapEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.Effects.ILampArrayBitmapEffect'
    _iid_ = Guid('{3238e065-d877-4627-89e5-2a88f7052fa6}')
    @winrt_commethod(6)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_Duration(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_StartDelay(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_StartDelay(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(10)
    def get_UpdateInterval(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(11)
    def put_UpdateInterval(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(12)
    def get_SuggestedBitmapSize(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(13)
    def add_BitmapRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Lights.Effects.LampArrayBitmapEffect, win32more.Windows.Devices.Lights.Effects.LampArrayBitmapRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_BitmapRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Duration = property(get_Duration, put_Duration)
    StartDelay = property(get_StartDelay, put_StartDelay)
    SuggestedBitmapSize = property(get_SuggestedBitmapSize, None)
    UpdateInterval = property(get_UpdateInterval, put_UpdateInterval)
    BitmapRequested = event()
class ILampArrayBitmapEffectFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.Effects.ILampArrayBitmapEffectFactory'
    _iid_ = Guid('{13608090-e336-4c8f-9053-a92407ca7b1d}')
    @winrt_commethod(6)
    def CreateInstance(self, lampArray: win32more.Windows.Devices.Lights.LampArray, lampIndexes: PassArray[Int32]) -> win32more.Windows.Devices.Lights.Effects.LampArrayBitmapEffect: ...
class ILampArrayBitmapRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.Effects.ILampArrayBitmapRequestedEventArgs'
    _iid_ = Guid('{c8b4af9e-fe63-4d51-babd-619defb454ba}')
    @winrt_commethod(6)
    def get_SinceStarted(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def UpdateBitmap(self, bitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    SinceStarted = property(get_SinceStarted, None)
class ILampArrayBlinkEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.Effects.ILampArrayBlinkEffect'
    _iid_ = Guid('{ebbf35f6-2fc5-4bb3-b3c3-6221a7680d13}')
    @winrt_commethod(6)
    def get_Color(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Color(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_AttackDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_AttackDuration(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(10)
    def get_SustainDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(11)
    def put_SustainDuration(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(12)
    def get_DecayDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(13)
    def put_DecayDuration(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(14)
    def get_RepetitionDelay(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(15)
    def put_RepetitionDelay(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(16)
    def get_StartDelay(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(17)
    def put_StartDelay(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(18)
    def get_Occurrences(self) -> Int32: ...
    @winrt_commethod(19)
    def put_Occurrences(self, value: Int32) -> Void: ...
    @winrt_commethod(20)
    def get_RepetitionMode(self) -> win32more.Windows.Devices.Lights.Effects.LampArrayRepetitionMode: ...
    @winrt_commethod(21)
    def put_RepetitionMode(self, value: win32more.Windows.Devices.Lights.Effects.LampArrayRepetitionMode) -> Void: ...
    AttackDuration = property(get_AttackDuration, put_AttackDuration)
    Color = property(get_Color, put_Color)
    DecayDuration = property(get_DecayDuration, put_DecayDuration)
    Occurrences = property(get_Occurrences, put_Occurrences)
    RepetitionDelay = property(get_RepetitionDelay, put_RepetitionDelay)
    RepetitionMode = property(get_RepetitionMode, put_RepetitionMode)
    StartDelay = property(get_StartDelay, put_StartDelay)
    SustainDuration = property(get_SustainDuration, put_SustainDuration)
class ILampArrayBlinkEffectFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.Effects.ILampArrayBlinkEffectFactory'
    _iid_ = Guid('{879f1d97-9f50-49b2-a56f-013aa08d55e0}')
    @winrt_commethod(6)
    def CreateInstance(self, lampArray: win32more.Windows.Devices.Lights.LampArray, lampIndexes: PassArray[Int32]) -> win32more.Windows.Devices.Lights.Effects.LampArrayBlinkEffect: ...
class ILampArrayColorRampEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.Effects.ILampArrayColorRampEffect'
    _iid_ = Guid('{2b004437-40a7-432e-a0b9-0d570c2153ff}')
    @winrt_commethod(6)
    def get_Color(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Color(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_RampDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_RampDuration(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(10)
    def get_StartDelay(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(11)
    def put_StartDelay(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(12)
    def get_CompletionBehavior(self) -> win32more.Windows.Devices.Lights.Effects.LampArrayEffectCompletionBehavior: ...
    @winrt_commethod(13)
    def put_CompletionBehavior(self, value: win32more.Windows.Devices.Lights.Effects.LampArrayEffectCompletionBehavior) -> Void: ...
    Color = property(get_Color, put_Color)
    CompletionBehavior = property(get_CompletionBehavior, put_CompletionBehavior)
    RampDuration = property(get_RampDuration, put_RampDuration)
    StartDelay = property(get_StartDelay, put_StartDelay)
class ILampArrayColorRampEffectFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.Effects.ILampArrayColorRampEffectFactory'
    _iid_ = Guid('{520bd133-0c74-4df5-bea7-4899e0266b0f}')
    @winrt_commethod(6)
    def CreateInstance(self, lampArray: win32more.Windows.Devices.Lights.LampArray, lampIndexes: PassArray[Int32]) -> win32more.Windows.Devices.Lights.Effects.LampArrayColorRampEffect: ...
class ILampArrayCustomEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.Effects.ILampArrayCustomEffect'
    _iid_ = Guid('{ec579170-3c34-4876-818b-5765f78b0ee4}')
    @winrt_commethod(6)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_Duration(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_UpdateInterval(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_UpdateInterval(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(10)
    def add_UpdateRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Lights.Effects.LampArrayCustomEffect, win32more.Windows.Devices.Lights.Effects.LampArrayUpdateRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_UpdateRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Duration = property(get_Duration, put_Duration)
    UpdateInterval = property(get_UpdateInterval, put_UpdateInterval)
    UpdateRequested = event()
class ILampArrayCustomEffectFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.Effects.ILampArrayCustomEffectFactory'
    _iid_ = Guid('{68b4774d-63e5-4af0-a58b-3e535b94e8c9}')
    @winrt_commethod(6)
    def CreateInstance(self, lampArray: win32more.Windows.Devices.Lights.LampArray, lampIndexes: PassArray[Int32]) -> win32more.Windows.Devices.Lights.Effects.LampArrayCustomEffect: ...
class ILampArrayEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.Effects.ILampArrayEffect'
    _iid_ = Guid('{11d45590-57fb-4546-b1ce-863107f740df}')
    @winrt_commethod(6)
    def get_ZIndex(self) -> Int32: ...
    @winrt_commethod(7)
    def put_ZIndex(self, value: Int32) -> Void: ...
    ZIndex = property(get_ZIndex, put_ZIndex)
class ILampArrayEffectPlaylist(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.Effects.ILampArrayEffectPlaylist'
    _iid_ = Guid('{7de58bfe-6f61-4103-98c7-d6632f7b9169}')
    @winrt_commethod(6)
    def Append(self, effect: win32more.Windows.Devices.Lights.Effects.ILampArrayEffect) -> Void: ...
    @winrt_commethod(7)
    def OverrideZIndex(self, zIndex: Int32) -> Void: ...
    @winrt_commethod(8)
    def Start(self) -> Void: ...
    @winrt_commethod(9)
    def Stop(self) -> Void: ...
    @winrt_commethod(10)
    def Pause(self) -> Void: ...
    @winrt_commethod(11)
    def get_EffectStartMode(self) -> win32more.Windows.Devices.Lights.Effects.LampArrayEffectStartMode: ...
    @winrt_commethod(12)
    def put_EffectStartMode(self, value: win32more.Windows.Devices.Lights.Effects.LampArrayEffectStartMode) -> Void: ...
    @winrt_commethod(13)
    def get_Occurrences(self) -> Int32: ...
    @winrt_commethod(14)
    def put_Occurrences(self, value: Int32) -> Void: ...
    @winrt_commethod(15)
    def get_RepetitionMode(self) -> win32more.Windows.Devices.Lights.Effects.LampArrayRepetitionMode: ...
    @winrt_commethod(16)
    def put_RepetitionMode(self, value: win32more.Windows.Devices.Lights.Effects.LampArrayRepetitionMode) -> Void: ...
    EffectStartMode = property(get_EffectStartMode, put_EffectStartMode)
    Occurrences = property(get_Occurrences, put_Occurrences)
    RepetitionMode = property(get_RepetitionMode, put_RepetitionMode)
class ILampArrayEffectPlaylistStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.Effects.ILampArrayEffectPlaylistStatics'
    _iid_ = Guid('{fb15235c-ea35-4c7f-a016-f3bfc6a6c47d}')
    @winrt_commethod(6)
    def StartAll(self, value: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Lights.Effects.LampArrayEffectPlaylist]) -> Void: ...
    @winrt_commethod(7)
    def StopAll(self, value: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Lights.Effects.LampArrayEffectPlaylist]) -> Void: ...
    @winrt_commethod(8)
    def PauseAll(self, value: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Lights.Effects.LampArrayEffectPlaylist]) -> Void: ...
class ILampArraySolidEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.Effects.ILampArraySolidEffect'
    _iid_ = Guid('{441f8213-43cc-4b33-80eb-c6ddde7dc8ed}')
    @winrt_commethod(6)
    def get_Color(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Color(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_Duration(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(10)
    def get_StartDelay(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(11)
    def put_StartDelay(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(12)
    def get_CompletionBehavior(self) -> win32more.Windows.Devices.Lights.Effects.LampArrayEffectCompletionBehavior: ...
    @winrt_commethod(13)
    def put_CompletionBehavior(self, value: win32more.Windows.Devices.Lights.Effects.LampArrayEffectCompletionBehavior) -> Void: ...
    Color = property(get_Color, put_Color)
    CompletionBehavior = property(get_CompletionBehavior, put_CompletionBehavior)
    Duration = property(get_Duration, put_Duration)
    StartDelay = property(get_StartDelay, put_StartDelay)
class ILampArraySolidEffectFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.Effects.ILampArraySolidEffectFactory'
    _iid_ = Guid('{f862a32c-5576-4341-961b-aee1f13cf9dd}')
    @winrt_commethod(6)
    def CreateInstance(self, lampArray: win32more.Windows.Devices.Lights.LampArray, lampIndexes: PassArray[Int32]) -> win32more.Windows.Devices.Lights.Effects.LampArraySolidEffect: ...
class ILampArrayUpdateRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Lights.Effects.ILampArrayUpdateRequestedEventArgs'
    _iid_ = Guid('{73560d6a-576a-48af-8539-67ffa0ab3516}')
    @winrt_commethod(6)
    def get_SinceStarted(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def SetColor(self, desiredColor: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def SetColorForIndex(self, lampIndex: Int32, desiredColor: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(9)
    def SetSingleColorForIndices(self, desiredColor: win32more.Windows.UI.Color, lampIndexes: PassArray[Int32]) -> Void: ...
    @winrt_commethod(10)
    def SetColorsForIndices(self, desiredColors: PassArray[win32more.Windows.UI.Color], lampIndexes: PassArray[Int32]) -> Void: ...
    SinceStarted = property(get_SinceStarted, None)
class LampArrayBitmapEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Lights.Effects.ILampArrayBitmapEffect
    _classid_ = 'Windows.Devices.Lights.Effects.LampArrayBitmapEffect'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Devices.Lights.Effects.LampArrayBitmapEffect.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Devices.Lights.Effects.ILampArrayBitmapEffectFactory, lampArray: win32more.Windows.Devices.Lights.LampArray, lampIndexes: PassArray[Int32]) -> win32more.Windows.Devices.Lights.Effects.LampArrayBitmapEffect: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Devices.Lights.Effects.ILampArrayBitmapEffect) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: win32more.Windows.Devices.Lights.Effects.ILampArrayBitmapEffect, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_StartDelay(self: win32more.Windows.Devices.Lights.Effects.ILampArrayBitmapEffect) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_StartDelay(self: win32more.Windows.Devices.Lights.Effects.ILampArrayBitmapEffect, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_UpdateInterval(self: win32more.Windows.Devices.Lights.Effects.ILampArrayBitmapEffect) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_UpdateInterval(self: win32more.Windows.Devices.Lights.Effects.ILampArrayBitmapEffect, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_SuggestedBitmapSize(self: win32more.Windows.Devices.Lights.Effects.ILampArrayBitmapEffect) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def add_BitmapRequested(self: win32more.Windows.Devices.Lights.Effects.ILampArrayBitmapEffect, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Lights.Effects.LampArrayBitmapEffect, win32more.Windows.Devices.Lights.Effects.LampArrayBitmapRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BitmapRequested(self: win32more.Windows.Devices.Lights.Effects.ILampArrayBitmapEffect, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_ZIndex(self: win32more.Windows.Devices.Lights.Effects.ILampArrayEffect) -> Int32: ...
    @winrt_mixinmethod
    def put_ZIndex(self: win32more.Windows.Devices.Lights.Effects.ILampArrayEffect, value: Int32) -> Void: ...
    Duration = property(get_Duration, put_Duration)
    StartDelay = property(get_StartDelay, put_StartDelay)
    SuggestedBitmapSize = property(get_SuggestedBitmapSize, None)
    UpdateInterval = property(get_UpdateInterval, put_UpdateInterval)
    ZIndex = property(get_ZIndex, put_ZIndex)
    BitmapRequested = event()
class LampArrayBitmapRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Lights.Effects.ILampArrayBitmapRequestedEventArgs
    _classid_ = 'Windows.Devices.Lights.Effects.LampArrayBitmapRequestedEventArgs'
    @winrt_mixinmethod
    def get_SinceStarted(self: win32more.Windows.Devices.Lights.Effects.ILampArrayBitmapRequestedEventArgs) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def UpdateBitmap(self: win32more.Windows.Devices.Lights.Effects.ILampArrayBitmapRequestedEventArgs, bitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> Void: ...
    SinceStarted = property(get_SinceStarted, None)
class LampArrayBlinkEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Lights.Effects.ILampArrayBlinkEffect
    _classid_ = 'Windows.Devices.Lights.Effects.LampArrayBlinkEffect'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Devices.Lights.Effects.LampArrayBlinkEffect.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Devices.Lights.Effects.ILampArrayBlinkEffectFactory, lampArray: win32more.Windows.Devices.Lights.LampArray, lampIndexes: PassArray[Int32]) -> win32more.Windows.Devices.Lights.Effects.LampArrayBlinkEffect: ...
    @winrt_mixinmethod
    def get_Color(self: win32more.Windows.Devices.Lights.Effects.ILampArrayBlinkEffect) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: win32more.Windows.Devices.Lights.Effects.ILampArrayBlinkEffect, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_AttackDuration(self: win32more.Windows.Devices.Lights.Effects.ILampArrayBlinkEffect) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_AttackDuration(self: win32more.Windows.Devices.Lights.Effects.ILampArrayBlinkEffect, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_SustainDuration(self: win32more.Windows.Devices.Lights.Effects.ILampArrayBlinkEffect) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_SustainDuration(self: win32more.Windows.Devices.Lights.Effects.ILampArrayBlinkEffect, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_DecayDuration(self: win32more.Windows.Devices.Lights.Effects.ILampArrayBlinkEffect) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_DecayDuration(self: win32more.Windows.Devices.Lights.Effects.ILampArrayBlinkEffect, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_RepetitionDelay(self: win32more.Windows.Devices.Lights.Effects.ILampArrayBlinkEffect) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_RepetitionDelay(self: win32more.Windows.Devices.Lights.Effects.ILampArrayBlinkEffect, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_StartDelay(self: win32more.Windows.Devices.Lights.Effects.ILampArrayBlinkEffect) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_StartDelay(self: win32more.Windows.Devices.Lights.Effects.ILampArrayBlinkEffect, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_Occurrences(self: win32more.Windows.Devices.Lights.Effects.ILampArrayBlinkEffect) -> Int32: ...
    @winrt_mixinmethod
    def put_Occurrences(self: win32more.Windows.Devices.Lights.Effects.ILampArrayBlinkEffect, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_RepetitionMode(self: win32more.Windows.Devices.Lights.Effects.ILampArrayBlinkEffect) -> win32more.Windows.Devices.Lights.Effects.LampArrayRepetitionMode: ...
    @winrt_mixinmethod
    def put_RepetitionMode(self: win32more.Windows.Devices.Lights.Effects.ILampArrayBlinkEffect, value: win32more.Windows.Devices.Lights.Effects.LampArrayRepetitionMode) -> Void: ...
    @winrt_mixinmethod
    def get_ZIndex(self: win32more.Windows.Devices.Lights.Effects.ILampArrayEffect) -> Int32: ...
    @winrt_mixinmethod
    def put_ZIndex(self: win32more.Windows.Devices.Lights.Effects.ILampArrayEffect, value: Int32) -> Void: ...
    AttackDuration = property(get_AttackDuration, put_AttackDuration)
    Color = property(get_Color, put_Color)
    DecayDuration = property(get_DecayDuration, put_DecayDuration)
    Occurrences = property(get_Occurrences, put_Occurrences)
    RepetitionDelay = property(get_RepetitionDelay, put_RepetitionDelay)
    RepetitionMode = property(get_RepetitionMode, put_RepetitionMode)
    StartDelay = property(get_StartDelay, put_StartDelay)
    SustainDuration = property(get_SustainDuration, put_SustainDuration)
    ZIndex = property(get_ZIndex, put_ZIndex)
class LampArrayColorRampEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Lights.Effects.ILampArrayColorRampEffect
    _classid_ = 'Windows.Devices.Lights.Effects.LampArrayColorRampEffect'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Devices.Lights.Effects.LampArrayColorRampEffect.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Devices.Lights.Effects.ILampArrayColorRampEffectFactory, lampArray: win32more.Windows.Devices.Lights.LampArray, lampIndexes: PassArray[Int32]) -> win32more.Windows.Devices.Lights.Effects.LampArrayColorRampEffect: ...
    @winrt_mixinmethod
    def get_Color(self: win32more.Windows.Devices.Lights.Effects.ILampArrayColorRampEffect) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: win32more.Windows.Devices.Lights.Effects.ILampArrayColorRampEffect, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_RampDuration(self: win32more.Windows.Devices.Lights.Effects.ILampArrayColorRampEffect) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_RampDuration(self: win32more.Windows.Devices.Lights.Effects.ILampArrayColorRampEffect, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_StartDelay(self: win32more.Windows.Devices.Lights.Effects.ILampArrayColorRampEffect) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_StartDelay(self: win32more.Windows.Devices.Lights.Effects.ILampArrayColorRampEffect, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_CompletionBehavior(self: win32more.Windows.Devices.Lights.Effects.ILampArrayColorRampEffect) -> win32more.Windows.Devices.Lights.Effects.LampArrayEffectCompletionBehavior: ...
    @winrt_mixinmethod
    def put_CompletionBehavior(self: win32more.Windows.Devices.Lights.Effects.ILampArrayColorRampEffect, value: win32more.Windows.Devices.Lights.Effects.LampArrayEffectCompletionBehavior) -> Void: ...
    @winrt_mixinmethod
    def get_ZIndex(self: win32more.Windows.Devices.Lights.Effects.ILampArrayEffect) -> Int32: ...
    @winrt_mixinmethod
    def put_ZIndex(self: win32more.Windows.Devices.Lights.Effects.ILampArrayEffect, value: Int32) -> Void: ...
    Color = property(get_Color, put_Color)
    CompletionBehavior = property(get_CompletionBehavior, put_CompletionBehavior)
    RampDuration = property(get_RampDuration, put_RampDuration)
    StartDelay = property(get_StartDelay, put_StartDelay)
    ZIndex = property(get_ZIndex, put_ZIndex)
class LampArrayCustomEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Lights.Effects.ILampArrayCustomEffect
    _classid_ = 'Windows.Devices.Lights.Effects.LampArrayCustomEffect'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Devices.Lights.Effects.LampArrayCustomEffect.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Devices.Lights.Effects.ILampArrayCustomEffectFactory, lampArray: win32more.Windows.Devices.Lights.LampArray, lampIndexes: PassArray[Int32]) -> win32more.Windows.Devices.Lights.Effects.LampArrayCustomEffect: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Devices.Lights.Effects.ILampArrayCustomEffect) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: win32more.Windows.Devices.Lights.Effects.ILampArrayCustomEffect, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_UpdateInterval(self: win32more.Windows.Devices.Lights.Effects.ILampArrayCustomEffect) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_UpdateInterval(self: win32more.Windows.Devices.Lights.Effects.ILampArrayCustomEffect, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def add_UpdateRequested(self: win32more.Windows.Devices.Lights.Effects.ILampArrayCustomEffect, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Lights.Effects.LampArrayCustomEffect, win32more.Windows.Devices.Lights.Effects.LampArrayUpdateRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UpdateRequested(self: win32more.Windows.Devices.Lights.Effects.ILampArrayCustomEffect, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_ZIndex(self: win32more.Windows.Devices.Lights.Effects.ILampArrayEffect) -> Int32: ...
    @winrt_mixinmethod
    def put_ZIndex(self: win32more.Windows.Devices.Lights.Effects.ILampArrayEffect, value: Int32) -> Void: ...
    Duration = property(get_Duration, put_Duration)
    UpdateInterval = property(get_UpdateInterval, put_UpdateInterval)
    ZIndex = property(get_ZIndex, put_ZIndex)
    UpdateRequested = event()
class LampArrayEffectCompletionBehavior(Enum, Int32):
    ClearState = 0
    KeepState = 1
class LampArrayEffectPlaylist(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.Devices.Lights.Effects.ILampArrayEffect]]
    default_interface: win32more.Windows.Devices.Lights.Effects.ILampArrayEffectPlaylist
    _classid_ = 'Windows.Devices.Lights.Effects.LampArrayEffectPlaylist'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Lights.Effects.LampArrayEffectPlaylist.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Lights.Effects.LampArrayEffectPlaylist: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Devices.Lights.Effects.ILampArrayEffectPlaylist, effect: win32more.Windows.Devices.Lights.Effects.ILampArrayEffect) -> Void: ...
    @winrt_mixinmethod
    def OverrideZIndex(self: win32more.Windows.Devices.Lights.Effects.ILampArrayEffectPlaylist, zIndex: Int32) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Devices.Lights.Effects.ILampArrayEffectPlaylist) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Devices.Lights.Effects.ILampArrayEffectPlaylist) -> Void: ...
    @winrt_mixinmethod
    def Pause(self: win32more.Windows.Devices.Lights.Effects.ILampArrayEffectPlaylist) -> Void: ...
    @winrt_mixinmethod
    def get_EffectStartMode(self: win32more.Windows.Devices.Lights.Effects.ILampArrayEffectPlaylist) -> win32more.Windows.Devices.Lights.Effects.LampArrayEffectStartMode: ...
    @winrt_mixinmethod
    def put_EffectStartMode(self: win32more.Windows.Devices.Lights.Effects.ILampArrayEffectPlaylist, value: win32more.Windows.Devices.Lights.Effects.LampArrayEffectStartMode) -> Void: ...
    @winrt_mixinmethod
    def get_Occurrences(self: win32more.Windows.Devices.Lights.Effects.ILampArrayEffectPlaylist) -> Int32: ...
    @winrt_mixinmethod
    def put_Occurrences(self: win32more.Windows.Devices.Lights.Effects.ILampArrayEffectPlaylist, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_RepetitionMode(self: win32more.Windows.Devices.Lights.Effects.ILampArrayEffectPlaylist) -> win32more.Windows.Devices.Lights.Effects.LampArrayRepetitionMode: ...
    @winrt_mixinmethod
    def put_RepetitionMode(self: win32more.Windows.Devices.Lights.Effects.ILampArrayEffectPlaylist, value: win32more.Windows.Devices.Lights.Effects.LampArrayRepetitionMode) -> Void: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Lights.Effects.ILampArrayEffect], index: UInt32) -> win32more.Windows.Devices.Lights.Effects.ILampArrayEffect: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Lights.Effects.ILampArrayEffect]) -> UInt32: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Lights.Effects.ILampArrayEffect], value: win32more.Windows.Devices.Lights.Effects.ILampArrayEffect, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Lights.Effects.ILampArrayEffect], startIndex: UInt32, items: FillArray[win32more.Windows.Devices.Lights.Effects.ILampArrayEffect]) -> UInt32: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Lights.Effects.ILampArrayEffect]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Devices.Lights.Effects.ILampArrayEffect]: ...
    @winrt_classmethod
    def StartAll(cls: win32more.Windows.Devices.Lights.Effects.ILampArrayEffectPlaylistStatics, value: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Lights.Effects.LampArrayEffectPlaylist]) -> Void: ...
    @winrt_classmethod
    def StopAll(cls: win32more.Windows.Devices.Lights.Effects.ILampArrayEffectPlaylistStatics, value: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Lights.Effects.LampArrayEffectPlaylist]) -> Void: ...
    @winrt_classmethod
    def PauseAll(cls: win32more.Windows.Devices.Lights.Effects.ILampArrayEffectPlaylistStatics, value: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Lights.Effects.LampArrayEffectPlaylist]) -> Void: ...
    EffectStartMode = property(get_EffectStartMode, put_EffectStartMode)
    Occurrences = property(get_Occurrences, put_Occurrences)
    RepetitionMode = property(get_RepetitionMode, put_RepetitionMode)
    Size = property(get_Size, None)
class LampArrayEffectStartMode(Enum, Int32):
    Sequential = 0
    Simultaneous = 1
class LampArrayRepetitionMode(Enum, Int32):
    Occurrences = 0
    Forever = 1
class LampArraySolidEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Lights.Effects.ILampArraySolidEffect
    _classid_ = 'Windows.Devices.Lights.Effects.LampArraySolidEffect'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Devices.Lights.Effects.LampArraySolidEffect.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.Devices.Lights.Effects.ILampArraySolidEffectFactory, lampArray: win32more.Windows.Devices.Lights.LampArray, lampIndexes: PassArray[Int32]) -> win32more.Windows.Devices.Lights.Effects.LampArraySolidEffect: ...
    @winrt_mixinmethod
    def get_Color(self: win32more.Windows.Devices.Lights.Effects.ILampArraySolidEffect) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: win32more.Windows.Devices.Lights.Effects.ILampArraySolidEffect, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Devices.Lights.Effects.ILampArraySolidEffect) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Duration(self: win32more.Windows.Devices.Lights.Effects.ILampArraySolidEffect, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_StartDelay(self: win32more.Windows.Devices.Lights.Effects.ILampArraySolidEffect) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_StartDelay(self: win32more.Windows.Devices.Lights.Effects.ILampArraySolidEffect, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_CompletionBehavior(self: win32more.Windows.Devices.Lights.Effects.ILampArraySolidEffect) -> win32more.Windows.Devices.Lights.Effects.LampArrayEffectCompletionBehavior: ...
    @winrt_mixinmethod
    def put_CompletionBehavior(self: win32more.Windows.Devices.Lights.Effects.ILampArraySolidEffect, value: win32more.Windows.Devices.Lights.Effects.LampArrayEffectCompletionBehavior) -> Void: ...
    @winrt_mixinmethod
    def get_ZIndex(self: win32more.Windows.Devices.Lights.Effects.ILampArrayEffect) -> Int32: ...
    @winrt_mixinmethod
    def put_ZIndex(self: win32more.Windows.Devices.Lights.Effects.ILampArrayEffect, value: Int32) -> Void: ...
    Color = property(get_Color, put_Color)
    CompletionBehavior = property(get_CompletionBehavior, put_CompletionBehavior)
    Duration = property(get_Duration, put_Duration)
    StartDelay = property(get_StartDelay, put_StartDelay)
    ZIndex = property(get_ZIndex, put_ZIndex)
class LampArrayUpdateRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Lights.Effects.ILampArrayUpdateRequestedEventArgs
    _classid_ = 'Windows.Devices.Lights.Effects.LampArrayUpdateRequestedEventArgs'
    @winrt_mixinmethod
    def get_SinceStarted(self: win32more.Windows.Devices.Lights.Effects.ILampArrayUpdateRequestedEventArgs) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def SetColor(self: win32more.Windows.Devices.Lights.Effects.ILampArrayUpdateRequestedEventArgs, desiredColor: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def SetColorForIndex(self: win32more.Windows.Devices.Lights.Effects.ILampArrayUpdateRequestedEventArgs, lampIndex: Int32, desiredColor: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def SetSingleColorForIndices(self: win32more.Windows.Devices.Lights.Effects.ILampArrayUpdateRequestedEventArgs, desiredColor: win32more.Windows.UI.Color, lampIndexes: PassArray[Int32]) -> Void: ...
    @winrt_mixinmethod
    def SetColorsForIndices(self: win32more.Windows.Devices.Lights.Effects.ILampArrayUpdateRequestedEventArgs, desiredColors: PassArray[win32more.Windows.UI.Color], lampIndexes: PassArray[Int32]) -> Void: ...
    SinceStarted = property(get_SinceStarted, None)


make_ready(__name__)
