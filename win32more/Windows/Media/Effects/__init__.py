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
class AudioEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Effects.IAudioEffect
    _classid_ = 'Windows.Media.Effects.AudioEffect'
    @winrt_mixinmethod
    def get_AudioEffectType(self: win32more.Windows.Media.Effects.IAudioEffect) -> win32more.Windows.Media.Effects.AudioEffectType: ...
    AudioEffectType = property(get_AudioEffectType, None)
class AudioEffectDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Effects.IAudioEffectDefinition
    _classid_ = 'Windows.Media.Effects.AudioEffectDefinition'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 1:
            instance = win32more.Windows.Media.Effects.AudioEffectDefinition.Create(*args)
        elif len(args) == 2:
            instance = win32more.Windows.Media.Effects.AudioEffectDefinition.CreateWithProperties(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
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
AudioEffectType = Int32
AudioEffectType_Other: AudioEffectType = 0
AudioEffectType_AcousticEchoCancellation: AudioEffectType = 1
AudioEffectType_NoiseSuppression: AudioEffectType = 2
AudioEffectType_AutomaticGainControl: AudioEffectType = 3
AudioEffectType_BeamForming: AudioEffectType = 4
AudioEffectType_ConstantToneRemoval: AudioEffectType = 5
AudioEffectType_Equalizer: AudioEffectType = 6
AudioEffectType_LoudnessEqualizer: AudioEffectType = 7
AudioEffectType_BassBoost: AudioEffectType = 8
AudioEffectType_VirtualSurround: AudioEffectType = 9
AudioEffectType_VirtualHeadphones: AudioEffectType = 10
AudioEffectType_SpeakerFill: AudioEffectType = 11
AudioEffectType_RoomCorrection: AudioEffectType = 12
AudioEffectType_BassManagement: AudioEffectType = 13
AudioEffectType_EnvironmentalEffects: AudioEffectType = 14
AudioEffectType_SpeakerProtection: AudioEffectType = 15
AudioEffectType_SpeakerCompensation: AudioEffectType = 16
AudioEffectType_DynamicRangeCompression: AudioEffectType = 17
AudioEffectType_FarFieldBeamForming: AudioEffectType = 18
AudioEffectType_DeepNoiseSuppression: AudioEffectType = 19
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
    EffectsProviderThumbnail = property(get_EffectsProviderThumbnail, None)
    EffectsProviderSettingsLabel = property(get_EffectsProviderSettingsLabel, None)
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
    SurfacesToOverlay = property(get_SurfacesToOverlay, None)
    BackgroundFrame = property(get_BackgroundFrame, None)
    OutputFrame = property(get_OutputFrame, None)
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
class IAudioEffect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Effects.IAudioEffect'
    _iid_ = Guid('{34aafa51-9207-4055-be93-6e5734a86ae4}')
    @winrt_commethod(6)
    def get_AudioEffectType(self) -> win32more.Windows.Media.Effects.AudioEffectType: ...
    AudioEffectType = property(get_AudioEffectType, None)
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
    EffectsProviderThumbnail = property(get_EffectsProviderThumbnail, None)
    EffectsProviderSettingsLabel = property(get_EffectsProviderSettingsLabel, None)
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
    UseInputFrameForOutput = property(get_UseInputFrameForOutput, None)
    SupportedEncodingProperties = property(get_SupportedEncodingProperties, None)
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
    SupportedMemoryTypes = property(get_SupportedMemoryTypes, None)
    TimeIndependent = property(get_TimeIndependent, None)
    SupportedEncodingProperties = property(get_SupportedEncodingProperties, None)
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
    SurfacesToOverlay = property(get_SurfacesToOverlay, None)
    BackgroundFrame = property(get_BackgroundFrame, None)
    OutputFrame = property(get_OutputFrame, None)
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
    PaddingColor = property(get_PaddingColor, put_PaddingColor)
    OutputSize = property(get_OutputSize, put_OutputSize)
    CropRectangle = property(get_CropRectangle, put_CropRectangle)
    Rotation = property(get_Rotation, put_Rotation)
    Mirror = property(get_Mirror, put_Mirror)
    ProcessingAlgorithm = property(get_ProcessingAlgorithm, put_ProcessingAlgorithm)
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
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    FrameFormat = property(get_FrameFormat, put_FrameFormat)
    ProjectionMode = property(get_ProjectionMode, put_ProjectionMode)
    HorizontalFieldOfViewInDegrees = property(get_HorizontalFieldOfViewInDegrees, put_HorizontalFieldOfViewInDegrees)
    ViewOrientation = property(get_ViewOrientation, put_ViewOrientation)
MediaEffectClosedReason = Int32
MediaEffectClosedReason_Done: MediaEffectClosedReason = 0
MediaEffectClosedReason_UnknownError: MediaEffectClosedReason = 1
MediaEffectClosedReason_UnsupportedEncodingFormat: MediaEffectClosedReason = 2
MediaEffectClosedReason_EffectCurrentlyUnloaded: MediaEffectClosedReason = 3
MediaMemoryTypes = Int32
MediaMemoryTypes_Gpu: MediaMemoryTypes = 0
MediaMemoryTypes_Cpu: MediaMemoryTypes = 1
MediaMemoryTypes_GpuAndCpu: MediaMemoryTypes = 2
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
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.Media.Effects.SlowMotionEffectDefinition.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
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
    TimeStretchRate = property(get_TimeStretchRate, put_TimeStretchRate)
    ActivatableClassId = property(get_ActivatableClassId, None)
    Properties = property(get_Properties, None)
class VideoCompositorDefinition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.Effects.IVideoCompositorDefinition
    _classid_ = 'Windows.Media.Effects.VideoCompositorDefinition'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 1:
            instance = win32more.Windows.Media.Effects.VideoCompositorDefinition.Create(*args)
        elif len(args) == 2:
            instance = win32more.Windows.Media.Effects.VideoCompositorDefinition.CreateWithProperties(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
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
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 1:
            instance = win32more.Windows.Media.Effects.VideoEffectDefinition.Create(*args)
        elif len(args) == 2:
            instance = win32more.Windows.Media.Effects.VideoEffectDefinition.CreateWithProperties(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
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
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.Media.Effects.VideoTransformEffectDefinition.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
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
    Properties = property(get_Properties, None)
    PaddingColor = property(get_PaddingColor, put_PaddingColor)
    OutputSize = property(get_OutputSize, put_OutputSize)
    CropRectangle = property(get_CropRectangle, put_CropRectangle)
    Rotation = property(get_Rotation, put_Rotation)
    Mirror = property(get_Mirror, put_Mirror)
    ProcessingAlgorithm = property(get_ProcessingAlgorithm, put_ProcessingAlgorithm)
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
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    FrameFormat = property(get_FrameFormat, put_FrameFormat)
    ProjectionMode = property(get_ProjectionMode, put_ProjectionMode)
    HorizontalFieldOfViewInDegrees = property(get_HorizontalFieldOfViewInDegrees, put_HorizontalFieldOfViewInDegrees)
    ViewOrientation = property(get_ViewOrientation, put_ViewOrientation)
make_ready(__name__)
