from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Foundation.Numerics
import win32more.Windows.Graphics.DirectX.Direct3D11
import win32more.Windows.Media
import win32more.Windows.Media.Capture
import win32more.Windows.Media.Editing
import win32more.Windows.Media.Effects
import win32more.Windows.Media.MediaProperties
import win32more.Windows.Media.Playback
import win32more.Windows.Media.Render
import win32more.Windows.Media.Transcoding
import win32more.Windows.Storage.Streams
import win32more.Windows.UI
import win32more.Windows.Win32.System.WinRT
class AcousticEchoCancellationConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Effects.IAcousticEchoCancellationConfiguration
    _classid_ = 'Windows.Media.Effects.AcousticEchoCancellationConfiguration'
    @winrt_mixinmethod
    def SetEchoCancellationRenderEndpoint(self: win32more.Windows.Media.Effects.IAcousticEchoCancellationConfiguration, deviceId: WinRT_String) -> Void: ...
class AudioCaptureEffectsManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Effects.IAudioCaptureEffectsManager
    _classid_ = 'Windows.Media.Effects.AudioCaptureEffectsManager'
    @winrt_mixinmethod
    def add_AudioCaptureEffectsChanged(self: win32more.Windows.Media.Effects.IAudioCaptureEffectsManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Effects.AudioCaptureEffectsManager, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AudioCaptureEffectsChanged(self: win32more.Windows.Media.Effects.IAudioCaptureEffectsManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetAudioCaptureEffects(self: win32more.Windows.Media.Effects.IAudioCaptureEffectsManager) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Effects.AudioEffect]: ...
    AudioCaptureEffectsChanged = event()
class AudioEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Effects.IAudioEffect
    _classid_ = 'Windows.Media.Effects.AudioEffect'
    @winrt_mixinmethod
    def get_AudioEffectType(self: win32more.Windows.Media.Effects.IAudioEffect) -> win32more.Windows.Media.Effects.AudioEffectType: ...
    @winrt_mixinmethod
    def get_AcousticEchoCancellationConfiguration(self: win32more.Windows.Media.Effects.IAudioEffect2) -> win32more.Windows.Media.Effects.AcousticEchoCancellationConfiguration: ...
    @winrt_mixinmethod
    def get_CanSetState(self: win32more.Windows.Media.Effects.IAudioEffect2) -> Boolean: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Media.Effects.IAudioEffect2) -> win32more.Windows.Media.Effects.AudioEffectState: ...
    @winrt_mixinmethod
    def SetState(self: win32more.Windows.Media.Effects.IAudioEffect2, newState: win32more.Windows.Media.Effects.AudioEffectState) -> Void: ...
    AcousticEchoCancellationConfiguration = property(get_AcousticEchoCancellationConfiguration, None)
    AudioEffectType = property(get_AudioEffectType, None)
    CanSetState = property(get_CanSetState, None)
    State = property(get_State, None)
class AudioEffectDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Effects.IAudioEffectDefinition
    _classid_ = 'Windows.Media.Effects.AudioEffectDefinition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Media.Effects.AudioEffectDefinition.Create(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Media.Effects.AudioEffectDefinition.CreateWithProperties(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Media.Effects.IAudioEffectDefinitionFactory, activatableClassId: WinRT_String) -> win32more.Windows.Media.Effects.AudioEffectDefinition: ...
    @winrt_factorymethod
    def CreateWithProperties(cls: win32more.Windows.Media.Effects.IAudioEffectDefinitionFactory, activatableClassId: WinRT_String, props: win32more.Windows.Foundation.Collections.IPropertySet) -> win32more.Windows.Media.Effects.AudioEffectDefinition: ...
    @winrt_mixinmethod
    def get_ActivatableClassId(self: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Media.Effects.IAudioEffectDefinition) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    ActivatableClassId = property(get_ActivatableClassId, None)
    Properties = property(get_Properties, None)
class AudioEffectState(Enum, Int32):
    Off = 0
    On = 1
class AudioEffectType(Enum, Int32):
    Other = 0
    AcousticEchoCancellation = 1
    NoiseSuppression = 2
    AutomaticGainControl = 3
    BeamForming = 4
    ConstantToneRemoval = 5
    Equalizer = 6
    LoudnessEqualizer = 7
    BassBoost = 8
    VirtualSurround = 9
    VirtualHeadphones = 10
    SpeakerFill = 11
    RoomCorrection = 12
    BassManagement = 13
    EnvironmentalEffects = 14
    SpeakerProtection = 15
    SpeakerCompensation = 16
    DynamicRangeCompression = 17
    FarFieldBeamForming = 18
    DeepNoiseSuppression = 19
class AudioEffectsManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Effects.AudioEffectsManager'
    @winrt_classmethod
    def CreateAudioRenderEffectsManager(cls: win32more.Windows.Media.Effects.IAudioEffectsManagerStatics, deviceId: WinRT_String, category: win32more.Windows.Media.Render.AudioRenderCategory) -> win32more.Windows.Media.Effects.AudioRenderEffectsManager: ...
    @winrt_classmethod
    def CreateAudioRenderEffectsManagerWithMode(cls: win32more.Windows.Media.Effects.IAudioEffectsManagerStatics, deviceId: WinRT_String, category: win32more.Windows.Media.Render.AudioRenderCategory, mode: win32more.Windows.Media.AudioProcessing) -> win32more.Windows.Media.Effects.AudioRenderEffectsManager: ...
    @winrt_classmethod
    def CreateAudioCaptureEffectsManager(cls: win32more.Windows.Media.Effects.IAudioEffectsManagerStatics, deviceId: WinRT_String, category: win32more.Windows.Media.Capture.MediaCategory) -> win32more.Windows.Media.Effects.AudioCaptureEffectsManager: ...
    @winrt_classmethod
    def CreateAudioCaptureEffectsManagerWithMode(cls: win32more.Windows.Media.Effects.IAudioEffectsManagerStatics, deviceId: WinRT_String, category: win32more.Windows.Media.Capture.MediaCategory, mode: win32more.Windows.Media.AudioProcessing) -> win32more.Windows.Media.Effects.AudioCaptureEffectsManager: ...
class AudioRenderEffectsManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Effects.IAudioRenderEffectsManager
    _classid_ = 'Windows.Media.Effects.AudioRenderEffectsManager'
    @winrt_mixinmethod
    def add_AudioRenderEffectsChanged(self: win32more.Windows.Media.Effects.IAudioRenderEffectsManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Effects.AudioRenderEffectsManager, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AudioRenderEffectsChanged(self: win32more.Windows.Media.Effects.IAudioRenderEffectsManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetAudioRenderEffects(self: win32more.Windows.Media.Effects.IAudioRenderEffectsManager) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Effects.AudioEffect]: ...
    @winrt_mixinmethod
    def get_EffectsProviderThumbnail(self: win32more.Windows.Media.Effects.IAudioRenderEffectsManager2) -> win32more.Windows.Storage.Streams.IRandomAccessStreamWithContentType: ...
    @winrt_mixinmethod
    def get_EffectsProviderSettingsLabel(self: win32more.Windows.Media.Effects.IAudioRenderEffectsManager2) -> WinRT_String: ...
    @winrt_mixinmethod
    def ShowSettingsUI(self: win32more.Windows.Media.Effects.IAudioRenderEffectsManager2) -> Void: ...
    EffectsProviderSettingsLabel = property(get_EffectsProviderSettingsLabel, None)
    EffectsProviderThumbnail = property(get_EffectsProviderThumbnail, None)
    AudioRenderEffectsChanged = event()
class CompositeVideoFrameContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Effects.ICompositeVideoFrameContext
    _classid_ = 'Windows.Media.Effects.CompositeVideoFrameContext'
    @winrt_mixinmethod
    def get_SurfacesToOverlay(self: win32more.Windows.Media.Effects.ICompositeVideoFrameContext) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface]: ...
    @winrt_mixinmethod
    def get_BackgroundFrame(self: win32more.Windows.Media.Effects.ICompositeVideoFrameContext) -> win32more.Windows.Media.VideoFrame: ...
    @winrt_mixinmethod
    def get_OutputFrame(self: win32more.Windows.Media.Effects.ICompositeVideoFrameContext) -> win32more.Windows.Media.VideoFrame: ...
    @winrt_mixinmethod
    def GetOverlayForSurface(self: win32more.Windows.Media.Effects.ICompositeVideoFrameContext, surfaceToOverlay: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface) -> win32more.Windows.Media.Editing.MediaOverlay: ...
    BackgroundFrame = property(get_BackgroundFrame, None)
    OutputFrame = property(get_OutputFrame, None)
    SurfacesToOverlay = property(get_SurfacesToOverlay, None)
class IAcousticEchoCancellationConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Effects.IAcousticEchoCancellationConfiguration'
    _iid_ = Guid('{587e735b-175b-5177-a407-2e33bafe33a5}')
    @winrt_commethod(6)
    def SetEchoCancellationRenderEndpoint(self, deviceId: WinRT_String) -> Void: ...
class IAudioCaptureEffectsManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Effects.IAudioCaptureEffectsManager'
    _iid_ = Guid('{8f85c271-038d-4393-8298-540110608eef}')
    @winrt_commethod(6)
    def add_AudioCaptureEffectsChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Effects.AudioCaptureEffectsManager, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_AudioCaptureEffectsChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def GetAudioCaptureEffects(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Effects.AudioEffect]: ...
    AudioCaptureEffectsChanged = event()
class IAudioEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Effects.IAudioEffect'
    _iid_ = Guid('{34aafa51-9207-4055-be93-6e5734a86ae4}')
    @winrt_commethod(6)
    def get_AudioEffectType(self) -> win32more.Windows.Media.Effects.AudioEffectType: ...
    AudioEffectType = property(get_AudioEffectType, None)
class IAudioEffect2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Effects.IAudioEffect2'
    _iid_ = Guid('{06703cb0-757e-5757-8af0-6ba58a8b2990}')
    @winrt_commethod(6)
    def get_AcousticEchoCancellationConfiguration(self) -> win32more.Windows.Media.Effects.AcousticEchoCancellationConfiguration: ...
    @winrt_commethod(7)
    def get_CanSetState(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_State(self) -> win32more.Windows.Media.Effects.AudioEffectState: ...
    @winrt_commethod(9)
    def SetState(self, newState: win32more.Windows.Media.Effects.AudioEffectState) -> Void: ...
    AcousticEchoCancellationConfiguration = property(get_AcousticEchoCancellationConfiguration, None)
    CanSetState = property(get_CanSetState, None)
    State = property(get_State, None)
class IAudioEffectDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Effects.IAudioEffectDefinition'
    _iid_ = Guid('{e4d7f974-7d80-4f73-9089-e31c9db9c294}')
    @winrt_commethod(6)
    def get_ActivatableClassId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    ActivatableClassId = property(get_ActivatableClassId, None)
    Properties = property(get_Properties, None)
class IAudioEffectDefinitionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Effects.IAudioEffectDefinitionFactory'
    _iid_ = Guid('{8e1da646-e705-45ed-8a2b-fc4e4f405a97}')
    @winrt_commethod(6)
    def Create(self, activatableClassId: WinRT_String) -> win32more.Windows.Media.Effects.AudioEffectDefinition: ...
    @winrt_commethod(7)
    def CreateWithProperties(self, activatableClassId: WinRT_String, props: win32more.Windows.Foundation.Collections.IPropertySet) -> win32more.Windows.Media.Effects.AudioEffectDefinition: ...
class IAudioEffectsManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Effects.IAudioEffectsManagerStatics'
    _iid_ = Guid('{66406c04-86fa-47cc-a315-f489d8c3fe10}')
    @winrt_commethod(6)
    def CreateAudioRenderEffectsManager(self, deviceId: WinRT_String, category: win32more.Windows.Media.Render.AudioRenderCategory) -> win32more.Windows.Media.Effects.AudioRenderEffectsManager: ...
    @winrt_commethod(7)
    def CreateAudioRenderEffectsManagerWithMode(self, deviceId: WinRT_String, category: win32more.Windows.Media.Render.AudioRenderCategory, mode: win32more.Windows.Media.AudioProcessing) -> win32more.Windows.Media.Effects.AudioRenderEffectsManager: ...
    @winrt_commethod(8)
    def CreateAudioCaptureEffectsManager(self, deviceId: WinRT_String, category: win32more.Windows.Media.Capture.MediaCategory) -> win32more.Windows.Media.Effects.AudioCaptureEffectsManager: ...
    @winrt_commethod(9)
    def CreateAudioCaptureEffectsManagerWithMode(self, deviceId: WinRT_String, category: win32more.Windows.Media.Capture.MediaCategory, mode: win32more.Windows.Media.AudioProcessing) -> win32more.Windows.Media.Effects.AudioCaptureEffectsManager: ...
class IAudioRenderEffectsManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Effects.IAudioRenderEffectsManager'
    _iid_ = Guid('{4dc98966-8751-42b2-bfcb-39ca7864bd47}')
    @winrt_commethod(6)
    def add_AudioRenderEffectsChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.Effects.AudioRenderEffectsManager, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_AudioRenderEffectsChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def GetAudioRenderEffects(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.Effects.AudioEffect]: ...
    AudioRenderEffectsChanged = event()
class IAudioRenderEffectsManager2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Effects.IAudioRenderEffectsManager2'
    _iid_ = Guid('{a844cd09-5ecc-44b3-bb4e-1db07287139c}')
    @winrt_commethod(6)
    def get_EffectsProviderThumbnail(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamWithContentType: ...
    @winrt_commethod(7)
    def get_EffectsProviderSettingsLabel(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def ShowSettingsUI(self) -> Void: ...
    EffectsProviderSettingsLabel = property(get_EffectsProviderSettingsLabel, None)
    EffectsProviderThumbnail = property(get_EffectsProviderThumbnail, None)
class IBasicAudioEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Effects.IBasicAudioEffect'
    _iid_ = Guid('{8c062c53-6bc0-48b8-a99a-4b41550f1359}')
    @winrt_commethod(6)
    def get_UseInputFrameForOutput(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SupportedEncodingProperties(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.MediaProperties.AudioEncodingProperties]: ...
    @winrt_commethod(8)
    def SetEncodingProperties(self, encodingProperties: win32more.Windows.Media.MediaProperties.AudioEncodingProperties) -> Void: ...
    @winrt_commethod(9)
    def ProcessFrame(self, context: win32more.Windows.Media.Effects.ProcessAudioFrameContext) -> Void: ...
    @winrt_commethod(10)
    def Close(self, reason: win32more.Windows.Media.Effects.MediaEffectClosedReason) -> Void: ...
    @winrt_commethod(11)
    def DiscardQueuedFrames(self) -> Void: ...
    SupportedEncodingProperties = property(get_SupportedEncodingProperties, None)
    UseInputFrameForOutput = property(get_UseInputFrameForOutput, None)
class IBasicVideoEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Effects.IBasicVideoEffect'
    _iid_ = Guid('{8262c7ef-b360-40be-949b-2ff42ff35693}')
    @winrt_commethod(6)
    def get_IsReadOnly(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SupportedMemoryTypes(self) -> win32more.Windows.Media.Effects.MediaMemoryTypes: ...
    @winrt_commethod(8)
    def get_TimeIndependent(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_SupportedEncodingProperties(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.MediaProperties.VideoEncodingProperties]: ...
    @winrt_commethod(10)
    def SetEncodingProperties(self, encodingProperties: win32more.Windows.Media.MediaProperties.VideoEncodingProperties, device: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice) -> Void: ...
    @winrt_commethod(11)
    def ProcessFrame(self, context: win32more.Windows.Media.Effects.ProcessVideoFrameContext) -> Void: ...
    @winrt_commethod(12)
    def Close(self, reason: win32more.Windows.Media.Effects.MediaEffectClosedReason) -> Void: ...
    @winrt_commethod(13)
    def DiscardQueuedFrames(self) -> Void: ...
    IsReadOnly = property(get_IsReadOnly, None)
    SupportedEncodingProperties = property(get_SupportedEncodingProperties, None)
    SupportedMemoryTypes = property(get_SupportedMemoryTypes, None)
    TimeIndependent = property(get_TimeIndependent, None)
class ICompositeVideoFrameContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Effects.ICompositeVideoFrameContext'
    _iid_ = Guid('{6c30024b-f514-4278-a5f7-b9188049d110}')
    @winrt_commethod(6)
    def get_SurfacesToOverlay(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface]: ...
    @winrt_commethod(7)
    def get_BackgroundFrame(self) -> win32more.Windows.Media.VideoFrame: ...
    @winrt_commethod(8)
    def get_OutputFrame(self) -> win32more.Windows.Media.VideoFrame: ...
    @winrt_commethod(9)
    def GetOverlayForSurface(self, surfaceToOverlay: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DSurface) -> win32more.Windows.Media.Editing.MediaOverlay: ...
    BackgroundFrame = property(get_BackgroundFrame, None)
    OutputFrame = property(get_OutputFrame, None)
    SurfacesToOverlay = property(get_SurfacesToOverlay, None)
class IProcessAudioFrameContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Effects.IProcessAudioFrameContext'
    _iid_ = Guid('{4cd92946-1222-4a27-a586-fb3e20273255}')
    @winrt_commethod(6)
    def get_InputFrame(self) -> win32more.Windows.Media.AudioFrame: ...
    @winrt_commethod(7)
    def get_OutputFrame(self) -> win32more.Windows.Media.AudioFrame: ...
    InputFrame = property(get_InputFrame, None)
    OutputFrame = property(get_OutputFrame, None)
class IProcessVideoFrameContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Effects.IProcessVideoFrameContext'
    _iid_ = Guid('{276f0e2b-6461-401e-ba78-0fdad6114eec}')
    @winrt_commethod(6)
    def get_InputFrame(self) -> win32more.Windows.Media.VideoFrame: ...
    @winrt_commethod(7)
    def get_OutputFrame(self) -> win32more.Windows.Media.VideoFrame: ...
    InputFrame = property(get_InputFrame, None)
    OutputFrame = property(get_OutputFrame, None)
class ISlowMotionEffectDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Effects.ISlowMotionEffectDefinition'
    _iid_ = Guid('{35053cd0-176c-4763-82c4-1b02dbe31737}')
    @winrt_commethod(6)
    def get_TimeStretchRate(self) -> Double: ...
    @winrt_commethod(7)
    def put_TimeStretchRate(self, value: Double) -> Void: ...
    TimeStretchRate = property(get_TimeStretchRate, put_TimeStretchRate)
class IVideoCompositor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Effects.IVideoCompositor'
    _iid_ = Guid('{8510b43e-420c-420f-96c7-7c98bba1fc55}')
    @winrt_commethod(6)
    def get_TimeIndependent(self) -> Boolean: ...
    @winrt_commethod(7)
    def SetEncodingProperties(self, backgroundProperties: win32more.Windows.Media.MediaProperties.VideoEncodingProperties, device: win32more.Windows.Graphics.DirectX.Direct3D11.IDirect3DDevice) -> Void: ...
    @winrt_commethod(8)
    def CompositeFrame(self, context: win32more.Windows.Media.Effects.CompositeVideoFrameContext) -> Void: ...
    @winrt_commethod(9)
    def Close(self, reason: win32more.Windows.Media.Effects.MediaEffectClosedReason) -> Void: ...
    @winrt_commethod(10)
    def DiscardQueuedFrames(self) -> Void: ...
    TimeIndependent = property(get_TimeIndependent, None)
class IVideoCompositorDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Effects.IVideoCompositorDefinition'
    _iid_ = Guid('{7946b8d0-2010-4ae3-9ab2-2cef42edd4d2}')
    @winrt_commethod(6)
    def get_ActivatableClassId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    ActivatableClassId = property(get_ActivatableClassId, None)
    Properties = property(get_Properties, None)
class IVideoCompositorDefinitionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Effects.IVideoCompositorDefinitionFactory'
    _iid_ = Guid('{4366fd10-68b8-4d52-89b6-02a968cca899}')
    @winrt_commethod(6)
    def Create(self, activatableClassId: WinRT_String) -> win32more.Windows.Media.Effects.VideoCompositorDefinition: ...
    @winrt_commethod(7)
    def CreateWithProperties(self, activatableClassId: WinRT_String, props: win32more.Windows.Foundation.Collections.IPropertySet) -> win32more.Windows.Media.Effects.VideoCompositorDefinition: ...
class IVideoEffectDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Effects.IVideoEffectDefinition'
    _iid_ = Guid('{39f38cf0-8d0f-4f3e-84fc-2d46a5297943}')
    @winrt_commethod(6)
    def get_ActivatableClassId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    ActivatableClassId = property(get_ActivatableClassId, None)
    Properties = property(get_Properties, None)
class IVideoEffectDefinitionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Effects.IVideoEffectDefinitionFactory'
    _iid_ = Guid('{81439b4e-6e33-428f-9d21-b5aafef7617c}')
    @winrt_commethod(6)
    def Create(self, activatableClassId: WinRT_String) -> win32more.Windows.Media.Effects.VideoEffectDefinition: ...
    @winrt_commethod(7)
    def CreateWithProperties(self, activatableClassId: WinRT_String, props: win32more.Windows.Foundation.Collections.IPropertySet) -> win32more.Windows.Media.Effects.VideoEffectDefinition: ...
class IVideoTransformEffectDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Effects.IVideoTransformEffectDefinition'
    _iid_ = Guid('{9664bb6a-1ea6-4aa6-8074-abe8851ecae2}')
    @winrt_commethod(6)
    def get_PaddingColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_PaddingColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_OutputSize(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(9)
    def put_OutputSize(self, value: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_commethod(10)
    def get_CropRectangle(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(11)
    def put_CropRectangle(self, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(12)
    def get_Rotation(self) -> win32more.Windows.Media.MediaProperties.MediaRotation: ...
    @winrt_commethod(13)
    def put_Rotation(self, value: win32more.Windows.Media.MediaProperties.MediaRotation) -> Void: ...
    @winrt_commethod(14)
    def get_Mirror(self) -> win32more.Windows.Media.MediaProperties.MediaMirroringOptions: ...
    @winrt_commethod(15)
    def put_Mirror(self, value: win32more.Windows.Media.MediaProperties.MediaMirroringOptions) -> Void: ...
    @winrt_commethod(16)
    def put_ProcessingAlgorithm(self, value: win32more.Windows.Media.Transcoding.MediaVideoProcessingAlgorithm) -> Void: ...
    @winrt_commethod(17)
    def get_ProcessingAlgorithm(self) -> win32more.Windows.Media.Transcoding.MediaVideoProcessingAlgorithm: ...
    CropRectangle = property(get_CropRectangle, put_CropRectangle)
    Mirror = property(get_Mirror, put_Mirror)
    OutputSize = property(get_OutputSize, put_OutputSize)
    PaddingColor = property(get_PaddingColor, put_PaddingColor)
    ProcessingAlgorithm = property(get_ProcessingAlgorithm, put_ProcessingAlgorithm)
    Rotation = property(get_Rotation, put_Rotation)
class IVideoTransformEffectDefinition2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Effects.IVideoTransformEffectDefinition2'
    _iid_ = Guid('{f0a8089f-66c8-4694-9fd9-1136abf7444a}')
    @winrt_commethod(6)
    def get_SphericalProjection(self) -> win32more.Windows.Media.Effects.VideoTransformSphericalProjection: ...
    SphericalProjection = property(get_SphericalProjection, None)
class IVideoTransformSphericalProjection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Effects.IVideoTransformSphericalProjection'
    _iid_ = Guid('{cf4401f0-9bf2-4c39-9f41-e022514a8468}')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_FrameFormat(self) -> win32more.Windows.Media.MediaProperties.SphericalVideoFrameFormat: ...
    @winrt_commethod(9)
    def put_FrameFormat(self, value: win32more.Windows.Media.MediaProperties.SphericalVideoFrameFormat) -> Void: ...
    @winrt_commethod(10)
    def get_ProjectionMode(self) -> win32more.Windows.Media.Playback.SphericalVideoProjectionMode: ...
    @winrt_commethod(11)
    def put_ProjectionMode(self, value: win32more.Windows.Media.Playback.SphericalVideoProjectionMode) -> Void: ...
    @winrt_commethod(12)
    def get_HorizontalFieldOfViewInDegrees(self) -> Double: ...
    @winrt_commethod(13)
    def put_HorizontalFieldOfViewInDegrees(self, value: Double) -> Void: ...
    @winrt_commethod(14)
    def get_ViewOrientation(self) -> win32more.Windows.Foundation.Numerics.Quaternion: ...
    @winrt_commethod(15)
    def put_ViewOrientation(self, value: win32more.Windows.Foundation.Numerics.Quaternion) -> Void: ...
    FrameFormat = property(get_FrameFormat, put_FrameFormat)
    HorizontalFieldOfViewInDegrees = property(get_HorizontalFieldOfViewInDegrees, put_HorizontalFieldOfViewInDegrees)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    ProjectionMode = property(get_ProjectionMode, put_ProjectionMode)
    ViewOrientation = property(get_ViewOrientation, put_ViewOrientation)
class MediaEffectClosedReason(Enum, Int32):
    Done = 0
    UnknownError = 1
    UnsupportedEncodingFormat = 2
    EffectCurrentlyUnloaded = 3
class MediaMemoryTypes(Enum, Int32):
    Gpu = 0
    Cpu = 1
    GpuAndCpu = 2
class ProcessAudioFrameContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Effects.IProcessAudioFrameContext
    _classid_ = 'Windows.Media.Effects.ProcessAudioFrameContext'
    @winrt_mixinmethod
    def get_InputFrame(self: win32more.Windows.Media.Effects.IProcessAudioFrameContext) -> win32more.Windows.Media.AudioFrame: ...
    @winrt_mixinmethod
    def get_OutputFrame(self: win32more.Windows.Media.Effects.IProcessAudioFrameContext) -> win32more.Windows.Media.AudioFrame: ...
    InputFrame = property(get_InputFrame, None)
    OutputFrame = property(get_OutputFrame, None)
class ProcessVideoFrameContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Effects.IProcessVideoFrameContext
    _classid_ = 'Windows.Media.Effects.ProcessVideoFrameContext'
    @winrt_mixinmethod
    def get_InputFrame(self: win32more.Windows.Media.Effects.IProcessVideoFrameContext) -> win32more.Windows.Media.VideoFrame: ...
    @winrt_mixinmethod
    def get_OutputFrame(self: win32more.Windows.Media.Effects.IProcessVideoFrameContext) -> win32more.Windows.Media.VideoFrame: ...
    InputFrame = property(get_InputFrame, None)
    OutputFrame = property(get_OutputFrame, None)
class SlowMotionEffectDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Effects.ISlowMotionEffectDefinition
    _classid_ = 'Windows.Media.Effects.SlowMotionEffectDefinition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Effects.SlowMotionEffectDefinition.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Effects.SlowMotionEffectDefinition: ...
    @winrt_mixinmethod
    def get_TimeStretchRate(self: win32more.Windows.Media.Effects.ISlowMotionEffectDefinition) -> Double: ...
    @winrt_mixinmethod
    def put_TimeStretchRate(self: win32more.Windows.Media.Effects.ISlowMotionEffectDefinition, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ActivatableClassId(self: win32more.Windows.Media.Effects.IVideoEffectDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Media.Effects.IVideoEffectDefinition) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    ActivatableClassId = property(get_ActivatableClassId, None)
    Properties = property(get_Properties, None)
    TimeStretchRate = property(get_TimeStretchRate, put_TimeStretchRate)
class VideoCompositorDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Effects.IVideoCompositorDefinition
    _classid_ = 'Windows.Media.Effects.VideoCompositorDefinition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Media.Effects.VideoCompositorDefinition.Create(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Media.Effects.VideoCompositorDefinition.CreateWithProperties(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Media.Effects.IVideoCompositorDefinitionFactory, activatableClassId: WinRT_String) -> win32more.Windows.Media.Effects.VideoCompositorDefinition: ...
    @winrt_factorymethod
    def CreateWithProperties(cls: win32more.Windows.Media.Effects.IVideoCompositorDefinitionFactory, activatableClassId: WinRT_String, props: win32more.Windows.Foundation.Collections.IPropertySet) -> win32more.Windows.Media.Effects.VideoCompositorDefinition: ...
    @winrt_mixinmethod
    def get_ActivatableClassId(self: win32more.Windows.Media.Effects.IVideoCompositorDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Media.Effects.IVideoCompositorDefinition) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    ActivatableClassId = property(get_ActivatableClassId, None)
    Properties = property(get_Properties, None)
class VideoEffectDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Effects.IVideoEffectDefinition
    _classid_ = 'Windows.Media.Effects.VideoEffectDefinition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Media.Effects.VideoEffectDefinition.Create(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Media.Effects.VideoEffectDefinition.CreateWithProperties(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Media.Effects.IVideoEffectDefinitionFactory, activatableClassId: WinRT_String) -> win32more.Windows.Media.Effects.VideoEffectDefinition: ...
    @winrt_factorymethod
    def CreateWithProperties(cls: win32more.Windows.Media.Effects.IVideoEffectDefinitionFactory, activatableClassId: WinRT_String, props: win32more.Windows.Foundation.Collections.IPropertySet) -> win32more.Windows.Media.Effects.VideoEffectDefinition: ...
    @winrt_mixinmethod
    def get_ActivatableClassId(self: win32more.Windows.Media.Effects.IVideoEffectDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Media.Effects.IVideoEffectDefinition) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    ActivatableClassId = property(get_ActivatableClassId, None)
    Properties = property(get_Properties, None)
class VideoTransformEffectDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Effects.IVideoEffectDefinition
    _classid_ = 'Windows.Media.Effects.VideoTransformEffectDefinition'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.Effects.VideoTransformEffectDefinition.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.Effects.VideoTransformEffectDefinition: ...
    @winrt_mixinmethod
    def get_ActivatableClassId(self: win32more.Windows.Media.Effects.IVideoEffectDefinition) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Media.Effects.IVideoEffectDefinition) -> win32more.Windows.Foundation.Collections.IPropertySet: ...
    @winrt_mixinmethod
    def get_PaddingColor(self: win32more.Windows.Media.Effects.IVideoTransformEffectDefinition) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_PaddingColor(self: win32more.Windows.Media.Effects.IVideoTransformEffectDefinition, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_OutputSize(self: win32more.Windows.Media.Effects.IVideoTransformEffectDefinition) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def put_OutputSize(self: win32more.Windows.Media.Effects.IVideoTransformEffectDefinition, value: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_mixinmethod
    def get_CropRectangle(self: win32more.Windows.Media.Effects.IVideoTransformEffectDefinition) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_CropRectangle(self: win32more.Windows.Media.Effects.IVideoTransformEffectDefinition, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def get_Rotation(self: win32more.Windows.Media.Effects.IVideoTransformEffectDefinition) -> win32more.Windows.Media.MediaProperties.MediaRotation: ...
    @winrt_mixinmethod
    def put_Rotation(self: win32more.Windows.Media.Effects.IVideoTransformEffectDefinition, value: win32more.Windows.Media.MediaProperties.MediaRotation) -> Void: ...
    @winrt_mixinmethod
    def get_Mirror(self: win32more.Windows.Media.Effects.IVideoTransformEffectDefinition) -> win32more.Windows.Media.MediaProperties.MediaMirroringOptions: ...
    @winrt_mixinmethod
    def put_Mirror(self: win32more.Windows.Media.Effects.IVideoTransformEffectDefinition, value: win32more.Windows.Media.MediaProperties.MediaMirroringOptions) -> Void: ...
    @winrt_mixinmethod
    def put_ProcessingAlgorithm(self: win32more.Windows.Media.Effects.IVideoTransformEffectDefinition, value: win32more.Windows.Media.Transcoding.MediaVideoProcessingAlgorithm) -> Void: ...
    @winrt_mixinmethod
    def get_ProcessingAlgorithm(self: win32more.Windows.Media.Effects.IVideoTransformEffectDefinition) -> win32more.Windows.Media.Transcoding.MediaVideoProcessingAlgorithm: ...
    @winrt_mixinmethod
    def get_SphericalProjection(self: win32more.Windows.Media.Effects.IVideoTransformEffectDefinition2) -> win32more.Windows.Media.Effects.VideoTransformSphericalProjection: ...
    ActivatableClassId = property(get_ActivatableClassId, None)
    CropRectangle = property(get_CropRectangle, put_CropRectangle)
    Mirror = property(get_Mirror, put_Mirror)
    OutputSize = property(get_OutputSize, put_OutputSize)
    PaddingColor = property(get_PaddingColor, put_PaddingColor)
    ProcessingAlgorithm = property(get_ProcessingAlgorithm, put_ProcessingAlgorithm)
    Properties = property(get_Properties, None)
    Rotation = property(get_Rotation, put_Rotation)
    SphericalProjection = property(get_SphericalProjection, None)
class VideoTransformSphericalProjection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Effects.IVideoTransformSphericalProjection
    _classid_ = 'Windows.Media.Effects.VideoTransformSphericalProjection'
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.Media.Effects.IVideoTransformSphericalProjection) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: win32more.Windows.Media.Effects.IVideoTransformSphericalProjection, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_FrameFormat(self: win32more.Windows.Media.Effects.IVideoTransformSphericalProjection) -> win32more.Windows.Media.MediaProperties.SphericalVideoFrameFormat: ...
    @winrt_mixinmethod
    def put_FrameFormat(self: win32more.Windows.Media.Effects.IVideoTransformSphericalProjection, value: win32more.Windows.Media.MediaProperties.SphericalVideoFrameFormat) -> Void: ...
    @winrt_mixinmethod
    def get_ProjectionMode(self: win32more.Windows.Media.Effects.IVideoTransformSphericalProjection) -> win32more.Windows.Media.Playback.SphericalVideoProjectionMode: ...
    @winrt_mixinmethod
    def put_ProjectionMode(self: win32more.Windows.Media.Effects.IVideoTransformSphericalProjection, value: win32more.Windows.Media.Playback.SphericalVideoProjectionMode) -> Void: ...
    @winrt_mixinmethod
    def get_HorizontalFieldOfViewInDegrees(self: win32more.Windows.Media.Effects.IVideoTransformSphericalProjection) -> Double: ...
    @winrt_mixinmethod
    def put_HorizontalFieldOfViewInDegrees(self: win32more.Windows.Media.Effects.IVideoTransformSphericalProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ViewOrientation(self: win32more.Windows.Media.Effects.IVideoTransformSphericalProjection) -> win32more.Windows.Foundation.Numerics.Quaternion: ...
    @winrt_mixinmethod
    def put_ViewOrientation(self: win32more.Windows.Media.Effects.IVideoTransformSphericalProjection, value: win32more.Windows.Foundation.Numerics.Quaternion) -> Void: ...
    FrameFormat = property(get_FrameFormat, put_FrameFormat)
    HorizontalFieldOfViewInDegrees = property(get_HorizontalFieldOfViewInDegrees, put_HorizontalFieldOfViewInDegrees)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    ProjectionMode = property(get_ProjectionMode, put_ProjectionMode)
    ViewOrientation = property(get_ViewOrientation, put_ViewOrientation)


make_ready(__name__)
