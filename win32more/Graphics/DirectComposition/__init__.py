from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Direct2D.Common
import win32more.Graphics.Direct3D
import win32more.Graphics.DirectComposition
import win32more.Graphics.Dxgi
import win32more.Graphics.Dxgi.Common
import win32more.Security
import win32more.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
COMPOSITIONOBJECT_READ = 1
COMPOSITIONOBJECT_WRITE = 2
DCOMPOSITION_MAX_WAITFORCOMPOSITORCLOCK_OBJECTS = 32
COMPOSITION_STATS_MAX_TARGETS = 256
def _define_DCompositionCreateDevice():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGIDevice_head,POINTER(Guid),POINTER(c_void_p))(('DCompositionCreateDevice', windll['dcomp.dll']), ((1, 'dxgiDevice'),(1, 'iid'),(1, 'dcompositionDevice'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DCompositionCreateDevice2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(Guid),POINTER(c_void_p))(('DCompositionCreateDevice2', windll['dcomp.dll']), ((1, 'renderingDevice'),(1, 'iid'),(1, 'dcompositionDevice'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DCompositionCreateDevice3():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(Guid),POINTER(c_void_p))(('DCompositionCreateDevice3', windll['dcomp.dll']), ((1, 'renderingDevice'),(1, 'iid'),(1, 'dcompositionDevice'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DCompositionCreateSurfaceHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),POINTER(win32more.Foundation.HANDLE))(('DCompositionCreateSurfaceHandle', windll['dcomp.dll']), ((1, 'desiredAccess'),(1, 'securityAttributes'),(1, 'surfaceHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DCompositionAttachMouseWheelToHwnd():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionVisual_head,win32more.Foundation.HWND,win32more.Foundation.BOOL)(('DCompositionAttachMouseWheelToHwnd', windll['dcomp.dll']), ((1, 'visual'),(1, 'hwnd'),(1, 'enable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DCompositionAttachMouseDragToHwnd():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionVisual_head,win32more.Foundation.HWND,win32more.Foundation.BOOL)(('DCompositionAttachMouseDragToHwnd', windll['dcomp.dll']), ((1, 'visual'),(1, 'hwnd'),(1, 'enable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DCompositionGetFrameId():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.COMPOSITION_FRAME_ID_TYPE,POINTER(UInt64))(('DCompositionGetFrameId', windll['dcomp.dll']), ((1, 'frameIdType'),(1, 'frameId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DCompositionGetStatistics():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(win32more.Graphics.DirectComposition.COMPOSITION_FRAME_STATS_head),UInt32,POINTER(win32more.Graphics.DirectComposition.COMPOSITION_TARGET_ID_head),POINTER(UInt32))(('DCompositionGetStatistics', windll['dcomp.dll']), ((1, 'frameId'),(1, 'frameStats'),(1, 'targetIdCount'),(1, 'targetIds'),(1, 'actualTargetIdCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DCompositionGetTargetStatistics():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(win32more.Graphics.DirectComposition.COMPOSITION_TARGET_ID_head),POINTER(win32more.Graphics.DirectComposition.COMPOSITION_TARGET_STATS_head))(('DCompositionGetTargetStatistics', windll['dcomp.dll']), ((1, 'frameId'),(1, 'targetId'),(1, 'targetStats'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DCompositionBoostCompositorClock():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(('DCompositionBoostCompositorClock', windll['dcomp.dll']), ((1, 'enable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DCompositionWaitForCompositorClock():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(win32more.Foundation.HANDLE),UInt32)(('DCompositionWaitForCompositorClock', windll['dcomp.dll']), ((1, 'count'),(1, 'handles'),(1, 'timeoutInMs'),))
    except (FileNotFoundError, AttributeError):
        return None
COMPOSITION_FRAME_ID_TYPE = Int32
COMPOSITION_FRAME_ID_CREATED = 0
COMPOSITION_FRAME_ID_CONFIRMED = 1
COMPOSITION_FRAME_ID_COMPLETED = 2
def _define_COMPOSITION_FRAME_STATS_head():
    class COMPOSITION_FRAME_STATS(Structure):
        pass
    return COMPOSITION_FRAME_STATS
def _define_COMPOSITION_FRAME_STATS():
    COMPOSITION_FRAME_STATS = win32more.Graphics.DirectComposition.COMPOSITION_FRAME_STATS_head
    COMPOSITION_FRAME_STATS._fields_ = [
        ('startTime', UInt64),
        ('targetTime', UInt64),
        ('framePeriod', UInt64),
    ]
    return COMPOSITION_FRAME_STATS
def _define_COMPOSITION_STATS_head():
    class COMPOSITION_STATS(Structure):
        pass
    return COMPOSITION_STATS
def _define_COMPOSITION_STATS():
    COMPOSITION_STATS = win32more.Graphics.DirectComposition.COMPOSITION_STATS_head
    COMPOSITION_STATS._fields_ = [
        ('presentCount', UInt32),
        ('refreshCount', UInt32),
        ('virtualRefreshCount', UInt32),
        ('time', UInt64),
    ]
    return COMPOSITION_STATS
def _define_COMPOSITION_TARGET_ID_head():
    class COMPOSITION_TARGET_ID(Structure):
        pass
    return COMPOSITION_TARGET_ID
def _define_COMPOSITION_TARGET_ID():
    COMPOSITION_TARGET_ID = win32more.Graphics.DirectComposition.COMPOSITION_TARGET_ID_head
    COMPOSITION_TARGET_ID._fields_ = [
        ('displayAdapterLuid', win32more.Foundation.LUID),
        ('renderAdapterLuid', win32more.Foundation.LUID),
        ('vidPnSourceId', UInt32),
        ('vidPnTargetId', UInt32),
        ('uniqueId', UInt32),
    ]
    return COMPOSITION_TARGET_ID
def _define_COMPOSITION_TARGET_STATS_head():
    class COMPOSITION_TARGET_STATS(Structure):
        pass
    return COMPOSITION_TARGET_STATS
def _define_COMPOSITION_TARGET_STATS():
    COMPOSITION_TARGET_STATS = win32more.Graphics.DirectComposition.COMPOSITION_TARGET_STATS_head
    COMPOSITION_TARGET_STATS._fields_ = [
        ('outstandingPresents', UInt32),
        ('presentTime', UInt64),
        ('vblankDuration', UInt64),
        ('presentedStats', win32more.Graphics.DirectComposition.COMPOSITION_STATS),
        ('completedStats', win32more.Graphics.DirectComposition.COMPOSITION_STATS),
    ]
    return COMPOSITION_TARGET_STATS
DCOMPOSITION_BACKFACE_VISIBILITY = Int32
DCOMPOSITION_BACKFACE_VISIBILITY_VISIBLE = 0
DCOMPOSITION_BACKFACE_VISIBILITY_HIDDEN = 1
DCOMPOSITION_BACKFACE_VISIBILITY_INHERIT = -1
DCOMPOSITION_BITMAP_INTERPOLATION_MODE = Int32
DCOMPOSITION_BITMAP_INTERPOLATION_MODE_NEAREST_NEIGHBOR = 0
DCOMPOSITION_BITMAP_INTERPOLATION_MODE_LINEAR = 1
DCOMPOSITION_BITMAP_INTERPOLATION_MODE_INHERIT = -1
DCOMPOSITION_BORDER_MODE = Int32
DCOMPOSITION_BORDER_MODE_SOFT = 0
DCOMPOSITION_BORDER_MODE_HARD = 1
DCOMPOSITION_BORDER_MODE_INHERIT = -1
DCOMPOSITION_COMPOSITE_MODE = Int32
DCOMPOSITION_COMPOSITE_MODE_SOURCE_OVER = 0
DCOMPOSITION_COMPOSITE_MODE_DESTINATION_INVERT = 1
DCOMPOSITION_COMPOSITE_MODE_MIN_BLEND = 2
DCOMPOSITION_COMPOSITE_MODE_INHERIT = -1
DCOMPOSITION_DEPTH_MODE = Int32
DCOMPOSITION_DEPTH_MODE_TREE = 0
DCOMPOSITION_DEPTH_MODE_SPATIAL = 1
DCOMPOSITION_DEPTH_MODE_SORTED = 3
DCOMPOSITION_DEPTH_MODE_INHERIT = -1
def _define_DCOMPOSITION_FRAME_STATISTICS_head():
    class DCOMPOSITION_FRAME_STATISTICS(Structure):
        pass
    return DCOMPOSITION_FRAME_STATISTICS
def _define_DCOMPOSITION_FRAME_STATISTICS():
    DCOMPOSITION_FRAME_STATISTICS = win32more.Graphics.DirectComposition.DCOMPOSITION_FRAME_STATISTICS_head
    DCOMPOSITION_FRAME_STATISTICS._fields_ = [
        ('lastFrameTime', win32more.Foundation.LARGE_INTEGER),
        ('currentCompositionRate', win32more.Graphics.Dxgi.Common.DXGI_RATIONAL),
        ('currentTime', win32more.Foundation.LARGE_INTEGER),
        ('timeFrequency', win32more.Foundation.LARGE_INTEGER),
        ('nextEstimatedFrameTime', win32more.Foundation.LARGE_INTEGER),
    ]
    return DCOMPOSITION_FRAME_STATISTICS
DCOMPOSITION_OPACITY_MODE = Int32
DCOMPOSITION_OPACITY_MODE_LAYER = 0
DCOMPOSITION_OPACITY_MODE_MULTIPLY = 1
DCOMPOSITION_OPACITY_MODE_INHERIT = -1
def _define_DCompositionInkTrailPoint_head():
    class DCompositionInkTrailPoint(Structure):
        pass
    return DCompositionInkTrailPoint
def _define_DCompositionInkTrailPoint():
    DCompositionInkTrailPoint = win32more.Graphics.DirectComposition.DCompositionInkTrailPoint_head
    DCompositionInkTrailPoint._fields_ = [
        ('x', Single),
        ('y', Single),
        ('radius', Single),
    ]
    return DCompositionInkTrailPoint
def _define_IDCompositionAffineTransform2DEffect_head():
    class IDCompositionAffineTransform2DEffect(win32more.Graphics.DirectComposition.IDCompositionFilterEffect_head):
        Guid = Guid('0b74b9e8-cdd6-492f-bb-bc-5e-d3-21-57-02-6d')
    return IDCompositionAffineTransform2DEffect
def _define_IDCompositionAffineTransform2DEffect():
    IDCompositionAffineTransform2DEffect = win32more.Graphics.DirectComposition.IDCompositionAffineTransform2DEffect_head
    IDCompositionAffineTransform2DEffect.SetInterpolationMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.Common.D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE)(4, 'SetInterpolationMode', ((1, 'interpolationMode'),)))
    IDCompositionAffineTransform2DEffect.SetBorderMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.Common.D2D1_BORDER_MODE)(5, 'SetBorderMode', ((1, 'borderMode'),)))
    IDCompositionAffineTransform2DEffect.SetTransformMatrix = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head))(6, 'SetTransformMatrix', ((1, 'transformMatrix'),)))
    IDCompositionAffineTransform2DEffect.SetTransformMatrixElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(7, 'SetTransformMatrixElement', ((1, 'row'),(1, 'column'),(1, 'animation'),)))
    IDCompositionAffineTransform2DEffect.SetTransformMatrixElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Single)(8, 'SetTransformMatrixElement', ((1, 'row'),(1, 'column'),(1, 'value'),)))
    IDCompositionAffineTransform2DEffect.SetSharpness = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(9, 'SetSharpness', ((1, 'animation'),)))
    IDCompositionAffineTransform2DEffect.SetSharpness = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(10, 'SetSharpness', ((1, 'sharpness'),)))
    win32more.Graphics.DirectComposition.IDCompositionFilterEffect
    return IDCompositionAffineTransform2DEffect
def _define_IDCompositionAnimation_head():
    class IDCompositionAnimation(win32more.System.Com.IUnknown_head):
        Guid = Guid('cbfd91d9-51b2-45e4-b3-de-d1-9c-cf-b8-63-c5')
    return IDCompositionAnimation
def _define_IDCompositionAnimation():
    IDCompositionAnimation = win32more.Graphics.DirectComposition.IDCompositionAnimation_head
    IDCompositionAnimation.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Reset', ()))
    IDCompositionAnimation.SetAbsoluteBeginTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.LARGE_INTEGER)(4, 'SetAbsoluteBeginTime', ((1, 'beginTime'),)))
    IDCompositionAnimation.AddCubic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Single,Single,Single,Single)(5, 'AddCubic', ((1, 'beginOffset'),(1, 'constantCoefficient'),(1, 'linearCoefficient'),(1, 'quadraticCoefficient'),(1, 'cubicCoefficient'),)))
    IDCompositionAnimation.AddSinusoidal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Single,Single,Single,Single)(6, 'AddSinusoidal', ((1, 'beginOffset'),(1, 'bias'),(1, 'amplitude'),(1, 'frequency'),(1, 'phase'),)))
    IDCompositionAnimation.AddRepeat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double)(7, 'AddRepeat', ((1, 'beginOffset'),(1, 'durationToRepeat'),)))
    IDCompositionAnimation.End = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Single)(8, 'End', ((1, 'endOffset'),(1, 'endValue'),)))
    win32more.System.Com.IUnknown
    return IDCompositionAnimation
def _define_IDCompositionArithmeticCompositeEffect_head():
    class IDCompositionArithmeticCompositeEffect(win32more.Graphics.DirectComposition.IDCompositionFilterEffect_head):
        Guid = Guid('3b67dfa8-e3dd-4e61-b6-40-46-c2-f3-d7-39-dc')
    return IDCompositionArithmeticCompositeEffect
def _define_IDCompositionArithmeticCompositeEffect():
    IDCompositionArithmeticCompositeEffect = win32more.Graphics.DirectComposition.IDCompositionArithmeticCompositeEffect_head
    IDCompositionArithmeticCompositeEffect.SetCoefficients = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_VECTOR_4F_head))(4, 'SetCoefficients', ((1, 'coefficients'),)))
    IDCompositionArithmeticCompositeEffect.SetClampOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(5, 'SetClampOutput', ((1, 'clampoutput'),)))
    IDCompositionArithmeticCompositeEffect.SetCoefficient1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(6, 'SetCoefficient1', ((1, 'animation'),)))
    IDCompositionArithmeticCompositeEffect.SetCoefficient1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(7, 'SetCoefficient1', ((1, 'Coeffcient1'),)))
    IDCompositionArithmeticCompositeEffect.SetCoefficient2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(8, 'SetCoefficient2', ((1, 'animation'),)))
    IDCompositionArithmeticCompositeEffect.SetCoefficient2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(9, 'SetCoefficient2', ((1, 'Coefficient2'),)))
    IDCompositionArithmeticCompositeEffect.SetCoefficient3 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(10, 'SetCoefficient3', ((1, 'animation'),)))
    IDCompositionArithmeticCompositeEffect.SetCoefficient3 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(11, 'SetCoefficient3', ((1, 'Coefficient3'),)))
    IDCompositionArithmeticCompositeEffect.SetCoefficient4 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(12, 'SetCoefficient4', ((1, 'animation'),)))
    IDCompositionArithmeticCompositeEffect.SetCoefficient4 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(13, 'SetCoefficient4', ((1, 'Coefficient4'),)))
    win32more.Graphics.DirectComposition.IDCompositionFilterEffect
    return IDCompositionArithmeticCompositeEffect
def _define_IDCompositionBlendEffect_head():
    class IDCompositionBlendEffect(win32more.Graphics.DirectComposition.IDCompositionFilterEffect_head):
        Guid = Guid('33ecdc0a-578a-4a11-9c-14-0c-b9-05-17-f9-c5')
    return IDCompositionBlendEffect
def _define_IDCompositionBlendEffect():
    IDCompositionBlendEffect = win32more.Graphics.DirectComposition.IDCompositionBlendEffect_head
    IDCompositionBlendEffect.SetMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.Common.D2D1_BLEND_MODE)(4, 'SetMode', ((1, 'mode'),)))
    win32more.Graphics.DirectComposition.IDCompositionFilterEffect
    return IDCompositionBlendEffect
def _define_IDCompositionBrightnessEffect_head():
    class IDCompositionBrightnessEffect(win32more.Graphics.DirectComposition.IDCompositionFilterEffect_head):
        Guid = Guid('6027496e-cb3a-49ab-93-4f-d7-98-da-4f-7d-a6')
    return IDCompositionBrightnessEffect
def _define_IDCompositionBrightnessEffect():
    IDCompositionBrightnessEffect = win32more.Graphics.DirectComposition.IDCompositionBrightnessEffect_head
    IDCompositionBrightnessEffect.SetWhitePoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_VECTOR_2F_head))(4, 'SetWhitePoint', ((1, 'whitePoint'),)))
    IDCompositionBrightnessEffect.SetBlackPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_VECTOR_2F_head))(5, 'SetBlackPoint', ((1, 'blackPoint'),)))
    IDCompositionBrightnessEffect.SetWhitePointX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(6, 'SetWhitePointX', ((1, 'animation'),)))
    IDCompositionBrightnessEffect.SetWhitePointX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(7, 'SetWhitePointX', ((1, 'whitePointX'),)))
    IDCompositionBrightnessEffect.SetWhitePointY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(8, 'SetWhitePointY', ((1, 'animation'),)))
    IDCompositionBrightnessEffect.SetWhitePointY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(9, 'SetWhitePointY', ((1, 'whitePointY'),)))
    IDCompositionBrightnessEffect.SetBlackPointX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(10, 'SetBlackPointX', ((1, 'animation'),)))
    IDCompositionBrightnessEffect.SetBlackPointX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(11, 'SetBlackPointX', ((1, 'blackPointX'),)))
    IDCompositionBrightnessEffect.SetBlackPointY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(12, 'SetBlackPointY', ((1, 'animation'),)))
    IDCompositionBrightnessEffect.SetBlackPointY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(13, 'SetBlackPointY', ((1, 'blackPointY'),)))
    win32more.Graphics.DirectComposition.IDCompositionFilterEffect
    return IDCompositionBrightnessEffect
def _define_IDCompositionClip_head():
    class IDCompositionClip(win32more.System.Com.IUnknown_head):
        Guid = Guid('64ac3703-9d3f-45ec-a1-09-7c-ac-0e-7a-13-a7')
    return IDCompositionClip
def _define_IDCompositionClip():
    IDCompositionClip = win32more.Graphics.DirectComposition.IDCompositionClip_head
    win32more.System.Com.IUnknown
    return IDCompositionClip
def _define_IDCompositionColorMatrixEffect_head():
    class IDCompositionColorMatrixEffect(win32more.Graphics.DirectComposition.IDCompositionFilterEffect_head):
        Guid = Guid('c1170a22-3ce2-4966-90-d4-55-40-8b-fc-84-c4')
    return IDCompositionColorMatrixEffect
def _define_IDCompositionColorMatrixEffect():
    IDCompositionColorMatrixEffect = win32more.Graphics.DirectComposition.IDCompositionColorMatrixEffect_head
    IDCompositionColorMatrixEffect.SetMatrix = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_5X4_F_head))(4, 'SetMatrix', ((1, 'matrix'),)))
    IDCompositionColorMatrixEffect.SetMatrixElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(5, 'SetMatrixElement', ((1, 'row'),(1, 'column'),(1, 'animation'),)))
    IDCompositionColorMatrixEffect.SetMatrixElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Single)(6, 'SetMatrixElement', ((1, 'row'),(1, 'column'),(1, 'value'),)))
    IDCompositionColorMatrixEffect.SetAlphaMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.Common.D2D1_COLORMATRIX_ALPHA_MODE)(7, 'SetAlphaMode', ((1, 'mode'),)))
    IDCompositionColorMatrixEffect.SetClampOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(8, 'SetClampOutput', ((1, 'clamp'),)))
    win32more.Graphics.DirectComposition.IDCompositionFilterEffect
    return IDCompositionColorMatrixEffect
def _define_IDCompositionCompositeEffect_head():
    class IDCompositionCompositeEffect(win32more.Graphics.DirectComposition.IDCompositionFilterEffect_head):
        Guid = Guid('576616c0-a231-494d-a3-8d-00-fd-5e-c4-db-46')
    return IDCompositionCompositeEffect
def _define_IDCompositionCompositeEffect():
    IDCompositionCompositeEffect = win32more.Graphics.DirectComposition.IDCompositionCompositeEffect_head
    IDCompositionCompositeEffect.SetMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.Common.D2D1_COMPOSITE_MODE)(4, 'SetMode', ((1, 'mode'),)))
    win32more.Graphics.DirectComposition.IDCompositionFilterEffect
    return IDCompositionCompositeEffect
def _define_IDCompositionDelegatedInkTrail_head():
    class IDCompositionDelegatedInkTrail(win32more.System.Com.IUnknown_head):
        Guid = Guid('c2448e9b-547d-4057-8c-f5-81-44-ed-e1-c2-da')
    return IDCompositionDelegatedInkTrail
def _define_IDCompositionDelegatedInkTrail():
    IDCompositionDelegatedInkTrail = win32more.Graphics.DirectComposition.IDCompositionDelegatedInkTrail_head
    IDCompositionDelegatedInkTrail.AddTrailPoints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.DCompositionInkTrailPoint_head),UInt32,POINTER(UInt32))(3, 'AddTrailPoints', ((1, 'inkPoints'),(1, 'inkPointsCount'),(1, 'generationId'),)))
    IDCompositionDelegatedInkTrail.AddTrailPointsWithPrediction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.DCompositionInkTrailPoint_head),UInt32,POINTER(win32more.Graphics.DirectComposition.DCompositionInkTrailPoint_head),UInt32,POINTER(UInt32))(4, 'AddTrailPointsWithPrediction', ((1, 'inkPoints'),(1, 'inkPointsCount'),(1, 'predictedInkPoints'),(1, 'predictedInkPointsCount'),(1, 'generationId'),)))
    IDCompositionDelegatedInkTrail.RemoveTrailPoints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(5, 'RemoveTrailPoints', ((1, 'generationId'),)))
    IDCompositionDelegatedInkTrail.StartNewTrail = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D1_COLOR_F_head))(6, 'StartNewTrail', ((1, 'color'),)))
    win32more.System.Com.IUnknown
    return IDCompositionDelegatedInkTrail
def _define_IDCompositionDesktopDevice_head():
    class IDCompositionDesktopDevice(win32more.Graphics.DirectComposition.IDCompositionDevice2_head):
        Guid = Guid('5f4633fe-1e08-4cb8-8c-75-ce-24-33-3f-56-02')
    return IDCompositionDesktopDevice
def _define_IDCompositionDesktopDevice():
    IDCompositionDesktopDevice = win32more.Graphics.DirectComposition.IDCompositionDesktopDevice_head
    IDCompositionDesktopDevice.CreateTargetForHwnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.BOOL,POINTER(win32more.Graphics.DirectComposition.IDCompositionTarget_head))(24, 'CreateTargetForHwnd', ((1, 'hwnd'),(1, 'topmost'),(1, 'target'),)))
    IDCompositionDesktopDevice.CreateSurfaceFromHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.System.Com.IUnknown_head))(25, 'CreateSurfaceFromHandle', ((1, 'handle'),(1, 'surface'),)))
    IDCompositionDesktopDevice.CreateSurfaceFromHwnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.System.Com.IUnknown_head))(26, 'CreateSurfaceFromHwnd', ((1, 'hwnd'),(1, 'surface'),)))
    win32more.Graphics.DirectComposition.IDCompositionDevice2
    return IDCompositionDesktopDevice
def _define_IDCompositionDevice_head():
    class IDCompositionDevice(win32more.System.Com.IUnknown_head):
        Guid = Guid('c37ea93a-e7aa-450d-b1-6f-97-46-cb-04-07-f3')
    return IDCompositionDevice
def _define_IDCompositionDevice():
    IDCompositionDevice = win32more.Graphics.DirectComposition.IDCompositionDevice_head
    IDCompositionDevice.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Commit', ()))
    IDCompositionDevice.WaitForCommitCompletion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'WaitForCommitCompletion', ()))
    IDCompositionDevice.GetFrameStatistics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.DCOMPOSITION_FRAME_STATISTICS_head))(5, 'GetFrameStatistics', ((1, 'statistics'),)))
    IDCompositionDevice.CreateTargetForHwnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.BOOL,POINTER(win32more.Graphics.DirectComposition.IDCompositionTarget_head))(6, 'CreateTargetForHwnd', ((1, 'hwnd'),(1, 'topmost'),(1, 'target'),)))
    IDCompositionDevice.CreateVisual = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionVisual_head))(7, 'CreateVisual', ((1, 'visual'),)))
    IDCompositionDevice.CreateSurface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Graphics.Dxgi.Common.DXGI_FORMAT,win32more.Graphics.Dxgi.Common.DXGI_ALPHA_MODE,POINTER(win32more.Graphics.DirectComposition.IDCompositionSurface_head))(8, 'CreateSurface', ((1, 'width'),(1, 'height'),(1, 'pixelFormat'),(1, 'alphaMode'),(1, 'surface'),)))
    IDCompositionDevice.CreateVirtualSurface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Graphics.Dxgi.Common.DXGI_FORMAT,win32more.Graphics.Dxgi.Common.DXGI_ALPHA_MODE,POINTER(win32more.Graphics.DirectComposition.IDCompositionVirtualSurface_head))(9, 'CreateVirtualSurface', ((1, 'initialWidth'),(1, 'initialHeight'),(1, 'pixelFormat'),(1, 'alphaMode'),(1, 'virtualSurface'),)))
    IDCompositionDevice.CreateSurfaceFromHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.System.Com.IUnknown_head))(10, 'CreateSurfaceFromHandle', ((1, 'handle'),(1, 'surface'),)))
    IDCompositionDevice.CreateSurfaceFromHwnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.System.Com.IUnknown_head))(11, 'CreateSurfaceFromHwnd', ((1, 'hwnd'),(1, 'surface'),)))
    IDCompositionDevice.CreateTranslateTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionTranslateTransform_head))(12, 'CreateTranslateTransform', ((1, 'translateTransform'),)))
    IDCompositionDevice.CreateScaleTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionScaleTransform_head))(13, 'CreateScaleTransform', ((1, 'scaleTransform'),)))
    IDCompositionDevice.CreateRotateTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionRotateTransform_head))(14, 'CreateRotateTransform', ((1, 'rotateTransform'),)))
    IDCompositionDevice.CreateSkewTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionSkewTransform_head))(15, 'CreateSkewTransform', ((1, 'skewTransform'),)))
    IDCompositionDevice.CreateMatrixTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionMatrixTransform_head))(16, 'CreateMatrixTransform', ((1, 'matrixTransform'),)))
    IDCompositionDevice.CreateTransformGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionTransform_head),UInt32,POINTER(win32more.Graphics.DirectComposition.IDCompositionTransform_head))(17, 'CreateTransformGroup', ((1, 'transforms'),(1, 'elements'),(1, 'transformGroup'),)))
    IDCompositionDevice.CreateTranslateTransform3D = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionTranslateTransform3D_head))(18, 'CreateTranslateTransform3D', ((1, 'translateTransform3D'),)))
    IDCompositionDevice.CreateScaleTransform3D = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionScaleTransform3D_head))(19, 'CreateScaleTransform3D', ((1, 'scaleTransform3D'),)))
    IDCompositionDevice.CreateRotateTransform3D = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionRotateTransform3D_head))(20, 'CreateRotateTransform3D', ((1, 'rotateTransform3D'),)))
    IDCompositionDevice.CreateMatrixTransform3D = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionMatrixTransform3D_head))(21, 'CreateMatrixTransform3D', ((1, 'matrixTransform3D'),)))
    IDCompositionDevice.CreateTransform3DGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionTransform3D_head),UInt32,POINTER(win32more.Graphics.DirectComposition.IDCompositionTransform3D_head))(22, 'CreateTransform3DGroup', ((1, 'transforms3D'),(1, 'elements'),(1, 'transform3DGroup'),)))
    IDCompositionDevice.CreateEffectGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionEffectGroup_head))(23, 'CreateEffectGroup', ((1, 'effectGroup'),)))
    IDCompositionDevice.CreateRectangleClip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionRectangleClip_head))(24, 'CreateRectangleClip', ((1, 'clip'),)))
    IDCompositionDevice.CreateAnimation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionAnimation_head))(25, 'CreateAnimation', ((1, 'animation'),)))
    IDCompositionDevice.CheckDeviceState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(26, 'CheckDeviceState', ((1, 'pfValid'),)))
    win32more.System.Com.IUnknown
    return IDCompositionDevice
def _define_IDCompositionDevice2_head():
    class IDCompositionDevice2(win32more.System.Com.IUnknown_head):
        Guid = Guid('75f6468d-1b8e-447c-9b-c6-75-fe-a8-0b-5b-25')
    return IDCompositionDevice2
def _define_IDCompositionDevice2():
    IDCompositionDevice2 = win32more.Graphics.DirectComposition.IDCompositionDevice2_head
    IDCompositionDevice2.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Commit', ()))
    IDCompositionDevice2.WaitForCommitCompletion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'WaitForCommitCompletion', ()))
    IDCompositionDevice2.GetFrameStatistics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.DCOMPOSITION_FRAME_STATISTICS_head))(5, 'GetFrameStatistics', ((1, 'statistics'),)))
    IDCompositionDevice2.CreateVisual = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionVisual2_head))(6, 'CreateVisual', ((1, 'visual'),)))
    IDCompositionDevice2.CreateSurfaceFactory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(win32more.Graphics.DirectComposition.IDCompositionSurfaceFactory_head))(7, 'CreateSurfaceFactory', ((1, 'renderingDevice'),(1, 'surfaceFactory'),)))
    IDCompositionDevice2.CreateSurface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Graphics.Dxgi.Common.DXGI_FORMAT,win32more.Graphics.Dxgi.Common.DXGI_ALPHA_MODE,POINTER(win32more.Graphics.DirectComposition.IDCompositionSurface_head))(8, 'CreateSurface', ((1, 'width'),(1, 'height'),(1, 'pixelFormat'),(1, 'alphaMode'),(1, 'surface'),)))
    IDCompositionDevice2.CreateVirtualSurface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Graphics.Dxgi.Common.DXGI_FORMAT,win32more.Graphics.Dxgi.Common.DXGI_ALPHA_MODE,POINTER(win32more.Graphics.DirectComposition.IDCompositionVirtualSurface_head))(9, 'CreateVirtualSurface', ((1, 'initialWidth'),(1, 'initialHeight'),(1, 'pixelFormat'),(1, 'alphaMode'),(1, 'virtualSurface'),)))
    IDCompositionDevice2.CreateTranslateTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionTranslateTransform_head))(10, 'CreateTranslateTransform', ((1, 'translateTransform'),)))
    IDCompositionDevice2.CreateScaleTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionScaleTransform_head))(11, 'CreateScaleTransform', ((1, 'scaleTransform'),)))
    IDCompositionDevice2.CreateRotateTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionRotateTransform_head))(12, 'CreateRotateTransform', ((1, 'rotateTransform'),)))
    IDCompositionDevice2.CreateSkewTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionSkewTransform_head))(13, 'CreateSkewTransform', ((1, 'skewTransform'),)))
    IDCompositionDevice2.CreateMatrixTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionMatrixTransform_head))(14, 'CreateMatrixTransform', ((1, 'matrixTransform'),)))
    IDCompositionDevice2.CreateTransformGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionTransform_head),UInt32,POINTER(win32more.Graphics.DirectComposition.IDCompositionTransform_head))(15, 'CreateTransformGroup', ((1, 'transforms'),(1, 'elements'),(1, 'transformGroup'),)))
    IDCompositionDevice2.CreateTranslateTransform3D = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionTranslateTransform3D_head))(16, 'CreateTranslateTransform3D', ((1, 'translateTransform3D'),)))
    IDCompositionDevice2.CreateScaleTransform3D = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionScaleTransform3D_head))(17, 'CreateScaleTransform3D', ((1, 'scaleTransform3D'),)))
    IDCompositionDevice2.CreateRotateTransform3D = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionRotateTransform3D_head))(18, 'CreateRotateTransform3D', ((1, 'rotateTransform3D'),)))
    IDCompositionDevice2.CreateMatrixTransform3D = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionMatrixTransform3D_head))(19, 'CreateMatrixTransform3D', ((1, 'matrixTransform3D'),)))
    IDCompositionDevice2.CreateTransform3DGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionTransform3D_head),UInt32,POINTER(win32more.Graphics.DirectComposition.IDCompositionTransform3D_head))(20, 'CreateTransform3DGroup', ((1, 'transforms3D'),(1, 'elements'),(1, 'transform3DGroup'),)))
    IDCompositionDevice2.CreateEffectGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionEffectGroup_head))(21, 'CreateEffectGroup', ((1, 'effectGroup'),)))
    IDCompositionDevice2.CreateRectangleClip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionRectangleClip_head))(22, 'CreateRectangleClip', ((1, 'clip'),)))
    IDCompositionDevice2.CreateAnimation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionAnimation_head))(23, 'CreateAnimation', ((1, 'animation'),)))
    win32more.System.Com.IUnknown
    return IDCompositionDevice2
def _define_IDCompositionDevice3_head():
    class IDCompositionDevice3(win32more.Graphics.DirectComposition.IDCompositionDevice2_head):
        Guid = Guid('0987cb06-f916-48bf-8d-35-ce-76-41-78-1b-d9')
    return IDCompositionDevice3
def _define_IDCompositionDevice3():
    IDCompositionDevice3 = win32more.Graphics.DirectComposition.IDCompositionDevice3_head
    IDCompositionDevice3.CreateGaussianBlurEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionGaussianBlurEffect_head))(24, 'CreateGaussianBlurEffect', ((1, 'gaussianBlurEffect'),)))
    IDCompositionDevice3.CreateBrightnessEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionBrightnessEffect_head))(25, 'CreateBrightnessEffect', ((1, 'brightnessEffect'),)))
    IDCompositionDevice3.CreateColorMatrixEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionColorMatrixEffect_head))(26, 'CreateColorMatrixEffect', ((1, 'colorMatrixEffect'),)))
    IDCompositionDevice3.CreateShadowEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionShadowEffect_head))(27, 'CreateShadowEffect', ((1, 'shadowEffect'),)))
    IDCompositionDevice3.CreateHueRotationEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionHueRotationEffect_head))(28, 'CreateHueRotationEffect', ((1, 'hueRotationEffect'),)))
    IDCompositionDevice3.CreateSaturationEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionSaturationEffect_head))(29, 'CreateSaturationEffect', ((1, 'saturationEffect'),)))
    IDCompositionDevice3.CreateTurbulenceEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionTurbulenceEffect_head))(30, 'CreateTurbulenceEffect', ((1, 'turbulenceEffect'),)))
    IDCompositionDevice3.CreateLinearTransferEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionLinearTransferEffect_head))(31, 'CreateLinearTransferEffect', ((1, 'linearTransferEffect'),)))
    IDCompositionDevice3.CreateTableTransferEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionTableTransferEffect_head))(32, 'CreateTableTransferEffect', ((1, 'tableTransferEffect'),)))
    IDCompositionDevice3.CreateCompositeEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionCompositeEffect_head))(33, 'CreateCompositeEffect', ((1, 'compositeEffect'),)))
    IDCompositionDevice3.CreateBlendEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionBlendEffect_head))(34, 'CreateBlendEffect', ((1, 'blendEffect'),)))
    IDCompositionDevice3.CreateArithmeticCompositeEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionArithmeticCompositeEffect_head))(35, 'CreateArithmeticCompositeEffect', ((1, 'arithmeticCompositeEffect'),)))
    IDCompositionDevice3.CreateAffineTransform2DEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionAffineTransform2DEffect_head))(36, 'CreateAffineTransform2DEffect', ((1, 'affineTransform2dEffect'),)))
    win32more.Graphics.DirectComposition.IDCompositionDevice2
    return IDCompositionDevice3
def _define_IDCompositionDeviceDebug_head():
    class IDCompositionDeviceDebug(win32more.System.Com.IUnknown_head):
        Guid = Guid('a1a3c64a-224f-4a81-97-73-4f-03-a8-9d-3c-6c')
    return IDCompositionDeviceDebug
def _define_IDCompositionDeviceDebug():
    IDCompositionDeviceDebug = win32more.Graphics.DirectComposition.IDCompositionDeviceDebug_head
    IDCompositionDeviceDebug.EnableDebugCounters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'EnableDebugCounters', ()))
    IDCompositionDeviceDebug.DisableDebugCounters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'DisableDebugCounters', ()))
    win32more.System.Com.IUnknown
    return IDCompositionDeviceDebug
def _define_IDCompositionEffect_head():
    class IDCompositionEffect(win32more.System.Com.IUnknown_head):
        Guid = Guid('ec81b08f-bfcb-4e8d-b1-93-a9-15-58-79-99-e8')
    return IDCompositionEffect
def _define_IDCompositionEffect():
    IDCompositionEffect = win32more.Graphics.DirectComposition.IDCompositionEffect_head
    win32more.System.Com.IUnknown
    return IDCompositionEffect
def _define_IDCompositionEffectGroup_head():
    class IDCompositionEffectGroup(win32more.Graphics.DirectComposition.IDCompositionEffect_head):
        Guid = Guid('a7929a74-e6b2-4bd6-8b-95-40-40-11-9c-a3-4d')
    return IDCompositionEffectGroup
def _define_IDCompositionEffectGroup():
    IDCompositionEffectGroup = win32more.Graphics.DirectComposition.IDCompositionEffectGroup_head
    IDCompositionEffectGroup.SetOpacity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(3, 'SetOpacity', ((1, 'animation'),)))
    IDCompositionEffectGroup.SetOpacity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(4, 'SetOpacity', ((1, 'opacity'),)))
    IDCompositionEffectGroup.SetTransform3D = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionTransform3D_head)(5, 'SetTransform3D', ((1, 'transform3D'),)))
    win32more.Graphics.DirectComposition.IDCompositionEffect
    return IDCompositionEffectGroup
def _define_IDCompositionFilterEffect_head():
    class IDCompositionFilterEffect(win32more.Graphics.DirectComposition.IDCompositionEffect_head):
        Guid = Guid('30c421d5-8cb2-4e9f-b1-33-37-be-27-0d-4a-c2')
    return IDCompositionFilterEffect
def _define_IDCompositionFilterEffect():
    IDCompositionFilterEffect = win32more.Graphics.DirectComposition.IDCompositionFilterEffect_head
    IDCompositionFilterEffect.SetInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.Com.IUnknown_head,UInt32)(3, 'SetInput', ((1, 'index'),(1, 'input'),(1, 'flags'),)))
    win32more.Graphics.DirectComposition.IDCompositionEffect
    return IDCompositionFilterEffect
def _define_IDCompositionGaussianBlurEffect_head():
    class IDCompositionGaussianBlurEffect(win32more.Graphics.DirectComposition.IDCompositionFilterEffect_head):
        Guid = Guid('45d4d0b7-1bd4-454e-88-94-2b-fa-68-44-30-33')
    return IDCompositionGaussianBlurEffect
def _define_IDCompositionGaussianBlurEffect():
    IDCompositionGaussianBlurEffect = win32more.Graphics.DirectComposition.IDCompositionGaussianBlurEffect_head
    IDCompositionGaussianBlurEffect.SetStandardDeviation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(4, 'SetStandardDeviation', ((1, 'animation'),)))
    IDCompositionGaussianBlurEffect.SetStandardDeviation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(5, 'SetStandardDeviation', ((1, 'amount'),)))
    IDCompositionGaussianBlurEffect.SetBorderMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.Common.D2D1_BORDER_MODE)(6, 'SetBorderMode', ((1, 'mode'),)))
    win32more.Graphics.DirectComposition.IDCompositionFilterEffect
    return IDCompositionGaussianBlurEffect
def _define_IDCompositionHueRotationEffect_head():
    class IDCompositionHueRotationEffect(win32more.Graphics.DirectComposition.IDCompositionFilterEffect_head):
        Guid = Guid('6db9f920-0770-4781-b0-c6-38-19-12-f9-d1-67')
    return IDCompositionHueRotationEffect
def _define_IDCompositionHueRotationEffect():
    IDCompositionHueRotationEffect = win32more.Graphics.DirectComposition.IDCompositionHueRotationEffect_head
    IDCompositionHueRotationEffect.SetAngle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(4, 'SetAngle', ((1, 'animation'),)))
    IDCompositionHueRotationEffect.SetAngle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(5, 'SetAngle', ((1, 'amountDegrees'),)))
    win32more.Graphics.DirectComposition.IDCompositionFilterEffect
    return IDCompositionHueRotationEffect
def _define_IDCompositionInkTrailDevice_head():
    class IDCompositionInkTrailDevice(win32more.System.Com.IUnknown_head):
        Guid = Guid('df0c7cec-cdeb-4d4a-b9-1c-72-1b-f2-2f-4e-6c')
    return IDCompositionInkTrailDevice
def _define_IDCompositionInkTrailDevice():
    IDCompositionInkTrailDevice = win32more.Graphics.DirectComposition.IDCompositionInkTrailDevice_head
    IDCompositionInkTrailDevice.CreateDelegatedInkTrail = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionDelegatedInkTrail_head))(3, 'CreateDelegatedInkTrail', ((1, 'inkTrail'),)))
    IDCompositionInkTrailDevice.CreateDelegatedInkTrailForSwapChain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(win32more.Graphics.DirectComposition.IDCompositionDelegatedInkTrail_head))(4, 'CreateDelegatedInkTrailForSwapChain', ((1, 'swapChain'),(1, 'inkTrail'),)))
    win32more.System.Com.IUnknown
    return IDCompositionInkTrailDevice
def _define_IDCompositionLinearTransferEffect_head():
    class IDCompositionLinearTransferEffect(win32more.Graphics.DirectComposition.IDCompositionFilterEffect_head):
        Guid = Guid('4305ee5b-c4a0-4c88-93-85-67-12-4e-01-76-83')
    return IDCompositionLinearTransferEffect
def _define_IDCompositionLinearTransferEffect():
    IDCompositionLinearTransferEffect = win32more.Graphics.DirectComposition.IDCompositionLinearTransferEffect_head
    IDCompositionLinearTransferEffect.SetRedYIntercept = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(4, 'SetRedYIntercept', ((1, 'animation'),)))
    IDCompositionLinearTransferEffect.SetRedYIntercept = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(5, 'SetRedYIntercept', ((1, 'redYIntercept'),)))
    IDCompositionLinearTransferEffect.SetRedSlope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(6, 'SetRedSlope', ((1, 'animation'),)))
    IDCompositionLinearTransferEffect.SetRedSlope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(7, 'SetRedSlope', ((1, 'redSlope'),)))
    IDCompositionLinearTransferEffect.SetRedDisable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(8, 'SetRedDisable', ((1, 'redDisable'),)))
    IDCompositionLinearTransferEffect.SetGreenYIntercept = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(9, 'SetGreenYIntercept', ((1, 'animation'),)))
    IDCompositionLinearTransferEffect.SetGreenYIntercept = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(10, 'SetGreenYIntercept', ((1, 'greenYIntercept'),)))
    IDCompositionLinearTransferEffect.SetGreenSlope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(11, 'SetGreenSlope', ((1, 'animation'),)))
    IDCompositionLinearTransferEffect.SetGreenSlope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(12, 'SetGreenSlope', ((1, 'greenSlope'),)))
    IDCompositionLinearTransferEffect.SetGreenDisable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(13, 'SetGreenDisable', ((1, 'greenDisable'),)))
    IDCompositionLinearTransferEffect.SetBlueYIntercept = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(14, 'SetBlueYIntercept', ((1, 'animation'),)))
    IDCompositionLinearTransferEffect.SetBlueYIntercept = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(15, 'SetBlueYIntercept', ((1, 'blueYIntercept'),)))
    IDCompositionLinearTransferEffect.SetBlueSlope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(16, 'SetBlueSlope', ((1, 'animation'),)))
    IDCompositionLinearTransferEffect.SetBlueSlope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(17, 'SetBlueSlope', ((1, 'blueSlope'),)))
    IDCompositionLinearTransferEffect.SetBlueDisable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(18, 'SetBlueDisable', ((1, 'blueDisable'),)))
    IDCompositionLinearTransferEffect.SetAlphaYIntercept = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(19, 'SetAlphaYIntercept', ((1, 'animation'),)))
    IDCompositionLinearTransferEffect.SetAlphaYIntercept = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(20, 'SetAlphaYIntercept', ((1, 'alphaYIntercept'),)))
    IDCompositionLinearTransferEffect.SetAlphaSlope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(21, 'SetAlphaSlope', ((1, 'animation'),)))
    IDCompositionLinearTransferEffect.SetAlphaSlope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(22, 'SetAlphaSlope', ((1, 'alphaSlope'),)))
    IDCompositionLinearTransferEffect.SetAlphaDisable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(23, 'SetAlphaDisable', ((1, 'alphaDisable'),)))
    IDCompositionLinearTransferEffect.SetClampOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(24, 'SetClampOutput', ((1, 'clampOutput'),)))
    win32more.Graphics.DirectComposition.IDCompositionFilterEffect
    return IDCompositionLinearTransferEffect
def _define_IDCompositionMatrixTransform_head():
    class IDCompositionMatrixTransform(win32more.Graphics.DirectComposition.IDCompositionTransform_head):
        Guid = Guid('16cdff07-c503-419c-83-f2-09-65-c7-af-1f-a6')
    return IDCompositionMatrixTransform
def _define_IDCompositionMatrixTransform():
    IDCompositionMatrixTransform = win32more.Graphics.DirectComposition.IDCompositionMatrixTransform_head
    IDCompositionMatrixTransform.SetMatrix = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head))(3, 'SetMatrix', ((1, 'matrix'),)))
    IDCompositionMatrixTransform.SetMatrixElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(4, 'SetMatrixElement', ((1, 'row'),(1, 'column'),(1, 'animation'),)))
    IDCompositionMatrixTransform.SetMatrixElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Single)(5, 'SetMatrixElement', ((1, 'row'),(1, 'column'),(1, 'value'),)))
    win32more.Graphics.DirectComposition.IDCompositionTransform
    return IDCompositionMatrixTransform
def _define_IDCompositionMatrixTransform3D_head():
    class IDCompositionMatrixTransform3D(win32more.Graphics.DirectComposition.IDCompositionTransform3D_head):
        Guid = Guid('4b3363f0-643b-41b7-b6-e0-cc-f2-2d-34-46-7c')
    return IDCompositionMatrixTransform3D
def _define_IDCompositionMatrixTransform3D():
    IDCompositionMatrixTransform3D = win32more.Graphics.DirectComposition.IDCompositionMatrixTransform3D_head
    IDCompositionMatrixTransform3D.SetMatrix = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D.D3DMATRIX_head))(3, 'SetMatrix', ((1, 'matrix'),)))
    IDCompositionMatrixTransform3D.SetMatrixElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(4, 'SetMatrixElement', ((1, 'row'),(1, 'column'),(1, 'animation'),)))
    IDCompositionMatrixTransform3D.SetMatrixElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Single)(5, 'SetMatrixElement', ((1, 'row'),(1, 'column'),(1, 'value'),)))
    win32more.Graphics.DirectComposition.IDCompositionTransform3D
    return IDCompositionMatrixTransform3D
def _define_IDCompositionRectangleClip_head():
    class IDCompositionRectangleClip(win32more.Graphics.DirectComposition.IDCompositionClip_head):
        Guid = Guid('9842ad7d-d9cf-4908-ae-d7-48-b5-1d-a5-e7-c2')
    return IDCompositionRectangleClip
def _define_IDCompositionRectangleClip():
    IDCompositionRectangleClip = win32more.Graphics.DirectComposition.IDCompositionRectangleClip_head
    IDCompositionRectangleClip.SetLeft = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(3, 'SetLeft', ((1, 'animation'),)))
    IDCompositionRectangleClip.SetLeft = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(4, 'SetLeft', ((1, 'left'),)))
    IDCompositionRectangleClip.SetTop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(5, 'SetTop', ((1, 'animation'),)))
    IDCompositionRectangleClip.SetTop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(6, 'SetTop', ((1, 'top'),)))
    IDCompositionRectangleClip.SetRight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(7, 'SetRight', ((1, 'animation'),)))
    IDCompositionRectangleClip.SetRight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(8, 'SetRight', ((1, 'right'),)))
    IDCompositionRectangleClip.SetBottom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(9, 'SetBottom', ((1, 'animation'),)))
    IDCompositionRectangleClip.SetBottom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(10, 'SetBottom', ((1, 'bottom'),)))
    IDCompositionRectangleClip.SetTopLeftRadiusX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(11, 'SetTopLeftRadiusX', ((1, 'animation'),)))
    IDCompositionRectangleClip.SetTopLeftRadiusX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(12, 'SetTopLeftRadiusX', ((1, 'radius'),)))
    IDCompositionRectangleClip.SetTopLeftRadiusY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(13, 'SetTopLeftRadiusY', ((1, 'animation'),)))
    IDCompositionRectangleClip.SetTopLeftRadiusY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(14, 'SetTopLeftRadiusY', ((1, 'radius'),)))
    IDCompositionRectangleClip.SetTopRightRadiusX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(15, 'SetTopRightRadiusX', ((1, 'animation'),)))
    IDCompositionRectangleClip.SetTopRightRadiusX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(16, 'SetTopRightRadiusX', ((1, 'radius'),)))
    IDCompositionRectangleClip.SetTopRightRadiusY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(17, 'SetTopRightRadiusY', ((1, 'animation'),)))
    IDCompositionRectangleClip.SetTopRightRadiusY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(18, 'SetTopRightRadiusY', ((1, 'radius'),)))
    IDCompositionRectangleClip.SetBottomLeftRadiusX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(19, 'SetBottomLeftRadiusX', ((1, 'animation'),)))
    IDCompositionRectangleClip.SetBottomLeftRadiusX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(20, 'SetBottomLeftRadiusX', ((1, 'radius'),)))
    IDCompositionRectangleClip.SetBottomLeftRadiusY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(21, 'SetBottomLeftRadiusY', ((1, 'animation'),)))
    IDCompositionRectangleClip.SetBottomLeftRadiusY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(22, 'SetBottomLeftRadiusY', ((1, 'radius'),)))
    IDCompositionRectangleClip.SetBottomRightRadiusX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(23, 'SetBottomRightRadiusX', ((1, 'animation'),)))
    IDCompositionRectangleClip.SetBottomRightRadiusX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(24, 'SetBottomRightRadiusX', ((1, 'radius'),)))
    IDCompositionRectangleClip.SetBottomRightRadiusY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(25, 'SetBottomRightRadiusY', ((1, 'animation'),)))
    IDCompositionRectangleClip.SetBottomRightRadiusY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(26, 'SetBottomRightRadiusY', ((1, 'radius'),)))
    win32more.Graphics.DirectComposition.IDCompositionClip
    return IDCompositionRectangleClip
def _define_IDCompositionRotateTransform_head():
    class IDCompositionRotateTransform(win32more.Graphics.DirectComposition.IDCompositionTransform_head):
        Guid = Guid('641ed83c-ae96-46c5-90-dc-32-77-4c-c5-c6-d5')
    return IDCompositionRotateTransform
def _define_IDCompositionRotateTransform():
    IDCompositionRotateTransform = win32more.Graphics.DirectComposition.IDCompositionRotateTransform_head
    IDCompositionRotateTransform.SetAngle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(3, 'SetAngle', ((1, 'animation'),)))
    IDCompositionRotateTransform.SetAngle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(4, 'SetAngle', ((1, 'angle'),)))
    IDCompositionRotateTransform.SetCenterX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(5, 'SetCenterX', ((1, 'animation'),)))
    IDCompositionRotateTransform.SetCenterX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(6, 'SetCenterX', ((1, 'centerX'),)))
    IDCompositionRotateTransform.SetCenterY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(7, 'SetCenterY', ((1, 'animation'),)))
    IDCompositionRotateTransform.SetCenterY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(8, 'SetCenterY', ((1, 'centerY'),)))
    win32more.Graphics.DirectComposition.IDCompositionTransform
    return IDCompositionRotateTransform
def _define_IDCompositionRotateTransform3D_head():
    class IDCompositionRotateTransform3D(win32more.Graphics.DirectComposition.IDCompositionTransform3D_head):
        Guid = Guid('d8f5b23f-d429-4a91-b5-5a-d2-f4-5f-d7-5b-18')
    return IDCompositionRotateTransform3D
def _define_IDCompositionRotateTransform3D():
    IDCompositionRotateTransform3D = win32more.Graphics.DirectComposition.IDCompositionRotateTransform3D_head
    IDCompositionRotateTransform3D.SetAngle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(3, 'SetAngle', ((1, 'animation'),)))
    IDCompositionRotateTransform3D.SetAngle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(4, 'SetAngle', ((1, 'angle'),)))
    IDCompositionRotateTransform3D.SetAxisX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(5, 'SetAxisX', ((1, 'animation'),)))
    IDCompositionRotateTransform3D.SetAxisX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(6, 'SetAxisX', ((1, 'axisX'),)))
    IDCompositionRotateTransform3D.SetAxisY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(7, 'SetAxisY', ((1, 'animation'),)))
    IDCompositionRotateTransform3D.SetAxisY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(8, 'SetAxisY', ((1, 'axisY'),)))
    IDCompositionRotateTransform3D.SetAxisZ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(9, 'SetAxisZ', ((1, 'animation'),)))
    IDCompositionRotateTransform3D.SetAxisZ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(10, 'SetAxisZ', ((1, 'axisZ'),)))
    IDCompositionRotateTransform3D.SetCenterX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(11, 'SetCenterX', ((1, 'animation'),)))
    IDCompositionRotateTransform3D.SetCenterX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(12, 'SetCenterX', ((1, 'centerX'),)))
    IDCompositionRotateTransform3D.SetCenterY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(13, 'SetCenterY', ((1, 'animation'),)))
    IDCompositionRotateTransform3D.SetCenterY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(14, 'SetCenterY', ((1, 'centerY'),)))
    IDCompositionRotateTransform3D.SetCenterZ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(15, 'SetCenterZ', ((1, 'animation'),)))
    IDCompositionRotateTransform3D.SetCenterZ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(16, 'SetCenterZ', ((1, 'centerZ'),)))
    win32more.Graphics.DirectComposition.IDCompositionTransform3D
    return IDCompositionRotateTransform3D
def _define_IDCompositionSaturationEffect_head():
    class IDCompositionSaturationEffect(win32more.Graphics.DirectComposition.IDCompositionFilterEffect_head):
        Guid = Guid('a08debda-3258-4fa4-9f-16-91-74-d3-fe-93-b1')
    return IDCompositionSaturationEffect
def _define_IDCompositionSaturationEffect():
    IDCompositionSaturationEffect = win32more.Graphics.DirectComposition.IDCompositionSaturationEffect_head
    IDCompositionSaturationEffect.SetSaturation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(4, 'SetSaturation', ((1, 'animation'),)))
    IDCompositionSaturationEffect.SetSaturation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(5, 'SetSaturation', ((1, 'ratio'),)))
    win32more.Graphics.DirectComposition.IDCompositionFilterEffect
    return IDCompositionSaturationEffect
def _define_IDCompositionScaleTransform_head():
    class IDCompositionScaleTransform(win32more.Graphics.DirectComposition.IDCompositionTransform_head):
        Guid = Guid('71fde914-40ef-45ef-bd-51-68-b0-37-c3-39-f9')
    return IDCompositionScaleTransform
def _define_IDCompositionScaleTransform():
    IDCompositionScaleTransform = win32more.Graphics.DirectComposition.IDCompositionScaleTransform_head
    IDCompositionScaleTransform.SetScaleX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(3, 'SetScaleX', ((1, 'animation'),)))
    IDCompositionScaleTransform.SetScaleX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(4, 'SetScaleX', ((1, 'scaleX'),)))
    IDCompositionScaleTransform.SetScaleY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(5, 'SetScaleY', ((1, 'animation'),)))
    IDCompositionScaleTransform.SetScaleY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(6, 'SetScaleY', ((1, 'scaleY'),)))
    IDCompositionScaleTransform.SetCenterX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(7, 'SetCenterX', ((1, 'animation'),)))
    IDCompositionScaleTransform.SetCenterX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(8, 'SetCenterX', ((1, 'centerX'),)))
    IDCompositionScaleTransform.SetCenterY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(9, 'SetCenterY', ((1, 'animation'),)))
    IDCompositionScaleTransform.SetCenterY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(10, 'SetCenterY', ((1, 'centerY'),)))
    win32more.Graphics.DirectComposition.IDCompositionTransform
    return IDCompositionScaleTransform
def _define_IDCompositionScaleTransform3D_head():
    class IDCompositionScaleTransform3D(win32more.Graphics.DirectComposition.IDCompositionTransform3D_head):
        Guid = Guid('2a9e9ead-364b-4b15-a7-c4-a1-99-7f-78-b3-89')
    return IDCompositionScaleTransform3D
def _define_IDCompositionScaleTransform3D():
    IDCompositionScaleTransform3D = win32more.Graphics.DirectComposition.IDCompositionScaleTransform3D_head
    IDCompositionScaleTransform3D.SetScaleX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(3, 'SetScaleX', ((1, 'animation'),)))
    IDCompositionScaleTransform3D.SetScaleX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(4, 'SetScaleX', ((1, 'scaleX'),)))
    IDCompositionScaleTransform3D.SetScaleY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(5, 'SetScaleY', ((1, 'animation'),)))
    IDCompositionScaleTransform3D.SetScaleY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(6, 'SetScaleY', ((1, 'scaleY'),)))
    IDCompositionScaleTransform3D.SetScaleZ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(7, 'SetScaleZ', ((1, 'animation'),)))
    IDCompositionScaleTransform3D.SetScaleZ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(8, 'SetScaleZ', ((1, 'scaleZ'),)))
    IDCompositionScaleTransform3D.SetCenterX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(9, 'SetCenterX', ((1, 'animation'),)))
    IDCompositionScaleTransform3D.SetCenterX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(10, 'SetCenterX', ((1, 'centerX'),)))
    IDCompositionScaleTransform3D.SetCenterY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(11, 'SetCenterY', ((1, 'animation'),)))
    IDCompositionScaleTransform3D.SetCenterY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(12, 'SetCenterY', ((1, 'centerY'),)))
    IDCompositionScaleTransform3D.SetCenterZ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(13, 'SetCenterZ', ((1, 'animation'),)))
    IDCompositionScaleTransform3D.SetCenterZ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(14, 'SetCenterZ', ((1, 'centerZ'),)))
    win32more.Graphics.DirectComposition.IDCompositionTransform3D
    return IDCompositionScaleTransform3D
def _define_IDCompositionShadowEffect_head():
    class IDCompositionShadowEffect(win32more.Graphics.DirectComposition.IDCompositionFilterEffect_head):
        Guid = Guid('4ad18ac0-cfd2-4c2f-bb-62-96-e5-4f-db-68-79')
    return IDCompositionShadowEffect
def _define_IDCompositionShadowEffect():
    IDCompositionShadowEffect = win32more.Graphics.DirectComposition.IDCompositionShadowEffect_head
    IDCompositionShadowEffect.SetStandardDeviation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(4, 'SetStandardDeviation', ((1, 'animation'),)))
    IDCompositionShadowEffect.SetStandardDeviation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(5, 'SetStandardDeviation', ((1, 'amount'),)))
    IDCompositionShadowEffect.SetColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_VECTOR_4F_head))(6, 'SetColor', ((1, 'color'),)))
    IDCompositionShadowEffect.SetRed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(7, 'SetRed', ((1, 'animation'),)))
    IDCompositionShadowEffect.SetRed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(8, 'SetRed', ((1, 'amount'),)))
    IDCompositionShadowEffect.SetGreen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(9, 'SetGreen', ((1, 'animation'),)))
    IDCompositionShadowEffect.SetGreen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(10, 'SetGreen', ((1, 'amount'),)))
    IDCompositionShadowEffect.SetBlue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(11, 'SetBlue', ((1, 'animation'),)))
    IDCompositionShadowEffect.SetBlue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(12, 'SetBlue', ((1, 'amount'),)))
    IDCompositionShadowEffect.SetAlpha = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(13, 'SetAlpha', ((1, 'animation'),)))
    IDCompositionShadowEffect.SetAlpha = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(14, 'SetAlpha', ((1, 'amount'),)))
    win32more.Graphics.DirectComposition.IDCompositionFilterEffect
    return IDCompositionShadowEffect
def _define_IDCompositionSkewTransform_head():
    class IDCompositionSkewTransform(win32more.Graphics.DirectComposition.IDCompositionTransform_head):
        Guid = Guid('e57aa735-dcdb-4c72-9c-61-05-91-f5-88-89-ee')
    return IDCompositionSkewTransform
def _define_IDCompositionSkewTransform():
    IDCompositionSkewTransform = win32more.Graphics.DirectComposition.IDCompositionSkewTransform_head
    IDCompositionSkewTransform.SetAngleX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(3, 'SetAngleX', ((1, 'animation'),)))
    IDCompositionSkewTransform.SetAngleX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(4, 'SetAngleX', ((1, 'angleX'),)))
    IDCompositionSkewTransform.SetAngleY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(5, 'SetAngleY', ((1, 'animation'),)))
    IDCompositionSkewTransform.SetAngleY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(6, 'SetAngleY', ((1, 'angleY'),)))
    IDCompositionSkewTransform.SetCenterX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(7, 'SetCenterX', ((1, 'animation'),)))
    IDCompositionSkewTransform.SetCenterX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(8, 'SetCenterX', ((1, 'centerX'),)))
    IDCompositionSkewTransform.SetCenterY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(9, 'SetCenterY', ((1, 'animation'),)))
    IDCompositionSkewTransform.SetCenterY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(10, 'SetCenterY', ((1, 'centerY'),)))
    win32more.Graphics.DirectComposition.IDCompositionTransform
    return IDCompositionSkewTransform
def _define_IDCompositionSurface_head():
    class IDCompositionSurface(win32more.System.Com.IUnknown_head):
        Guid = Guid('bb8a4953-2c99-4f5a-96-f5-48-19-02-7f-a3-ac')
    return IDCompositionSurface
def _define_IDCompositionSurface():
    IDCompositionSurface = win32more.Graphics.DirectComposition.IDCompositionSurface_head
    IDCompositionSurface.BeginDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head),POINTER(Guid),POINTER(c_void_p),POINTER(win32more.Foundation.POINT_head))(3, 'BeginDraw', ((1, 'updateRect'),(1, 'iid'),(1, 'updateObject'),(1, 'updateOffset'),)))
    IDCompositionSurface.EndDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'EndDraw', ()))
    IDCompositionSurface.SuspendDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'SuspendDraw', ()))
    IDCompositionSurface.ResumeDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'ResumeDraw', ()))
    IDCompositionSurface.Scroll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head),Int32,Int32)(7, 'Scroll', ((1, 'scrollRect'),(1, 'clipRect'),(1, 'offsetX'),(1, 'offsetY'),)))
    win32more.System.Com.IUnknown
    return IDCompositionSurface
def _define_IDCompositionSurfaceFactory_head():
    class IDCompositionSurfaceFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('e334bc12-3937-4e02-85-eb-fc-f4-eb-30-d2-c8')
    return IDCompositionSurfaceFactory
def _define_IDCompositionSurfaceFactory():
    IDCompositionSurfaceFactory = win32more.Graphics.DirectComposition.IDCompositionSurfaceFactory_head
    IDCompositionSurfaceFactory.CreateSurface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Graphics.Dxgi.Common.DXGI_FORMAT,win32more.Graphics.Dxgi.Common.DXGI_ALPHA_MODE,POINTER(win32more.Graphics.DirectComposition.IDCompositionSurface_head))(3, 'CreateSurface', ((1, 'width'),(1, 'height'),(1, 'pixelFormat'),(1, 'alphaMode'),(1, 'surface'),)))
    IDCompositionSurfaceFactory.CreateVirtualSurface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Graphics.Dxgi.Common.DXGI_FORMAT,win32more.Graphics.Dxgi.Common.DXGI_ALPHA_MODE,POINTER(win32more.Graphics.DirectComposition.IDCompositionVirtualSurface_head))(4, 'CreateVirtualSurface', ((1, 'initialWidth'),(1, 'initialHeight'),(1, 'pixelFormat'),(1, 'alphaMode'),(1, 'virtualSurface'),)))
    win32more.System.Com.IUnknown
    return IDCompositionSurfaceFactory
def _define_IDCompositionTableTransferEffect_head():
    class IDCompositionTableTransferEffect(win32more.Graphics.DirectComposition.IDCompositionFilterEffect_head):
        Guid = Guid('9b7e82e2-69c5-4eb4-a5-f5-a7-03-3f-51-32-cd')
    return IDCompositionTableTransferEffect
def _define_IDCompositionTableTransferEffect():
    IDCompositionTableTransferEffect = win32more.Graphics.DirectComposition.IDCompositionTableTransferEffect_head
    IDCompositionTableTransferEffect.SetRedTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),UInt32)(4, 'SetRedTable', ((1, 'tableValues'),(1, 'count'),)))
    IDCompositionTableTransferEffect.SetGreenTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),UInt32)(5, 'SetGreenTable', ((1, 'tableValues'),(1, 'count'),)))
    IDCompositionTableTransferEffect.SetBlueTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),UInt32)(6, 'SetBlueTable', ((1, 'tableValues'),(1, 'count'),)))
    IDCompositionTableTransferEffect.SetAlphaTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),UInt32)(7, 'SetAlphaTable', ((1, 'tableValues'),(1, 'count'),)))
    IDCompositionTableTransferEffect.SetRedDisable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(8, 'SetRedDisable', ((1, 'redDisable'),)))
    IDCompositionTableTransferEffect.SetGreenDisable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(9, 'SetGreenDisable', ((1, 'greenDisable'),)))
    IDCompositionTableTransferEffect.SetBlueDisable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(10, 'SetBlueDisable', ((1, 'blueDisable'),)))
    IDCompositionTableTransferEffect.SetAlphaDisable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(11, 'SetAlphaDisable', ((1, 'alphaDisable'),)))
    IDCompositionTableTransferEffect.SetClampOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(12, 'SetClampOutput', ((1, 'clampOutput'),)))
    IDCompositionTableTransferEffect.SetRedTableValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(13, 'SetRedTableValue', ((1, 'index'),(1, 'animation'),)))
    IDCompositionTableTransferEffect.SetRedTableValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Single)(14, 'SetRedTableValue', ((1, 'index'),(1, 'value'),)))
    IDCompositionTableTransferEffect.SetGreenTableValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(15, 'SetGreenTableValue', ((1, 'index'),(1, 'animation'),)))
    IDCompositionTableTransferEffect.SetGreenTableValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Single)(16, 'SetGreenTableValue', ((1, 'index'),(1, 'value'),)))
    IDCompositionTableTransferEffect.SetBlueTableValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(17, 'SetBlueTableValue', ((1, 'index'),(1, 'animation'),)))
    IDCompositionTableTransferEffect.SetBlueTableValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Single)(18, 'SetBlueTableValue', ((1, 'index'),(1, 'value'),)))
    IDCompositionTableTransferEffect.SetAlphaTableValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(19, 'SetAlphaTableValue', ((1, 'index'),(1, 'animation'),)))
    IDCompositionTableTransferEffect.SetAlphaTableValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Single)(20, 'SetAlphaTableValue', ((1, 'index'),(1, 'value'),)))
    win32more.Graphics.DirectComposition.IDCompositionFilterEffect
    return IDCompositionTableTransferEffect
def _define_IDCompositionTarget_head():
    class IDCompositionTarget(win32more.System.Com.IUnknown_head):
        Guid = Guid('eacdd04c-117e-4e17-88-f4-d1-b1-2b-0e-3d-89')
    return IDCompositionTarget
def _define_IDCompositionTarget():
    IDCompositionTarget = win32more.Graphics.DirectComposition.IDCompositionTarget_head
    IDCompositionTarget.SetRoot = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionVisual_head)(3, 'SetRoot', ((1, 'visual'),)))
    win32more.System.Com.IUnknown
    return IDCompositionTarget
def _define_IDCompositionTransform_head():
    class IDCompositionTransform(win32more.Graphics.DirectComposition.IDCompositionTransform3D_head):
        Guid = Guid('fd55faa7-37e0-4c20-95-d2-9b-e4-5b-c3-3f-55')
    return IDCompositionTransform
def _define_IDCompositionTransform():
    IDCompositionTransform = win32more.Graphics.DirectComposition.IDCompositionTransform_head
    win32more.Graphics.DirectComposition.IDCompositionTransform3D
    return IDCompositionTransform
def _define_IDCompositionTransform3D_head():
    class IDCompositionTransform3D(win32more.Graphics.DirectComposition.IDCompositionEffect_head):
        Guid = Guid('71185722-246b-41f2-aa-d1-04-43-f7-f4-bf-c2')
    return IDCompositionTransform3D
def _define_IDCompositionTransform3D():
    IDCompositionTransform3D = win32more.Graphics.DirectComposition.IDCompositionTransform3D_head
    win32more.Graphics.DirectComposition.IDCompositionEffect
    return IDCompositionTransform3D
def _define_IDCompositionTranslateTransform_head():
    class IDCompositionTranslateTransform(win32more.Graphics.DirectComposition.IDCompositionTransform_head):
        Guid = Guid('06791122-c6f0-417d-83-23-26-9e-98-7f-59-54')
    return IDCompositionTranslateTransform
def _define_IDCompositionTranslateTransform():
    IDCompositionTranslateTransform = win32more.Graphics.DirectComposition.IDCompositionTranslateTransform_head
    IDCompositionTranslateTransform.SetOffsetX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(3, 'SetOffsetX', ((1, 'animation'),)))
    IDCompositionTranslateTransform.SetOffsetX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(4, 'SetOffsetX', ((1, 'offsetX'),)))
    IDCompositionTranslateTransform.SetOffsetY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(5, 'SetOffsetY', ((1, 'animation'),)))
    IDCompositionTranslateTransform.SetOffsetY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(6, 'SetOffsetY', ((1, 'offsetY'),)))
    win32more.Graphics.DirectComposition.IDCompositionTransform
    return IDCompositionTranslateTransform
def _define_IDCompositionTranslateTransform3D_head():
    class IDCompositionTranslateTransform3D(win32more.Graphics.DirectComposition.IDCompositionTransform3D_head):
        Guid = Guid('91636d4b-9ba1-4532-aa-f7-e3-34-49-94-d7-88')
    return IDCompositionTranslateTransform3D
def _define_IDCompositionTranslateTransform3D():
    IDCompositionTranslateTransform3D = win32more.Graphics.DirectComposition.IDCompositionTranslateTransform3D_head
    IDCompositionTranslateTransform3D.SetOffsetX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(3, 'SetOffsetX', ((1, 'animation'),)))
    IDCompositionTranslateTransform3D.SetOffsetX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(4, 'SetOffsetX', ((1, 'offsetX'),)))
    IDCompositionTranslateTransform3D.SetOffsetY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(5, 'SetOffsetY', ((1, 'animation'),)))
    IDCompositionTranslateTransform3D.SetOffsetY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(6, 'SetOffsetY', ((1, 'offsetY'),)))
    IDCompositionTranslateTransform3D.SetOffsetZ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(7, 'SetOffsetZ', ((1, 'animation'),)))
    IDCompositionTranslateTransform3D.SetOffsetZ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(8, 'SetOffsetZ', ((1, 'offsetZ'),)))
    win32more.Graphics.DirectComposition.IDCompositionTransform3D
    return IDCompositionTranslateTransform3D
def _define_IDCompositionTurbulenceEffect_head():
    class IDCompositionTurbulenceEffect(win32more.Graphics.DirectComposition.IDCompositionFilterEffect_head):
        Guid = Guid('a6a55bda-c09c-49f3-91-93-a4-19-22-c8-97-15')
    return IDCompositionTurbulenceEffect
def _define_IDCompositionTurbulenceEffect():
    IDCompositionTurbulenceEffect = win32more.Graphics.DirectComposition.IDCompositionTurbulenceEffect_head
    IDCompositionTurbulenceEffect.SetOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_VECTOR_2F_head))(4, 'SetOffset', ((1, 'offset'),)))
    IDCompositionTurbulenceEffect.SetBaseFrequency = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_VECTOR_2F_head))(5, 'SetBaseFrequency', ((1, 'frequency'),)))
    IDCompositionTurbulenceEffect.SetSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_VECTOR_2F_head))(6, 'SetSize', ((1, 'size'),)))
    IDCompositionTurbulenceEffect.SetNumOctaves = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(7, 'SetNumOctaves', ((1, 'numOctaves'),)))
    IDCompositionTurbulenceEffect.SetSeed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(8, 'SetSeed', ((1, 'seed'),)))
    IDCompositionTurbulenceEffect.SetNoise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.Common.D2D1_TURBULENCE_NOISE)(9, 'SetNoise', ((1, 'noise'),)))
    IDCompositionTurbulenceEffect.SetStitchable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(10, 'SetStitchable', ((1, 'stitchable'),)))
    win32more.Graphics.DirectComposition.IDCompositionFilterEffect
    return IDCompositionTurbulenceEffect
def _define_IDCompositionVirtualSurface_head():
    class IDCompositionVirtualSurface(win32more.Graphics.DirectComposition.IDCompositionSurface_head):
        Guid = Guid('ae471c51-5f53-4a24-8d-3e-d0-c3-9c-30-b3-f0')
    return IDCompositionVirtualSurface
def _define_IDCompositionVirtualSurface():
    IDCompositionVirtualSurface = win32more.Graphics.DirectComposition.IDCompositionVirtualSurface_head
    IDCompositionVirtualSurface.Resize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32)(8, 'Resize', ((1, 'width'),(1, 'height'),)))
    IDCompositionVirtualSurface.Trim = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head),UInt32)(9, 'Trim', ((1, 'rectangles'),(1, 'count'),)))
    win32more.Graphics.DirectComposition.IDCompositionSurface
    return IDCompositionVirtualSurface
def _define_IDCompositionVisual_head():
    class IDCompositionVisual(win32more.System.Com.IUnknown_head):
        Guid = Guid('4d93059d-097b-4651-9a-60-f0-f2-51-16-e2-f3')
    return IDCompositionVisual
def _define_IDCompositionVisual():
    IDCompositionVisual = win32more.Graphics.DirectComposition.IDCompositionVisual_head
    IDCompositionVisual.SetOffsetX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(3, 'SetOffsetX', ((1, 'animation'),)))
    IDCompositionVisual.SetOffsetX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(4, 'SetOffsetX', ((1, 'offsetX'),)))
    IDCompositionVisual.SetOffsetY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(5, 'SetOffsetY', ((1, 'animation'),)))
    IDCompositionVisual.SetOffsetY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(6, 'SetOffsetY', ((1, 'offsetY'),)))
    IDCompositionVisual.SetTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionTransform_head)(7, 'SetTransform', ((1, 'transform'),)))
    IDCompositionVisual.SetTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head))(8, 'SetTransform', ((1, 'matrix'),)))
    IDCompositionVisual.SetTransformParent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionVisual_head)(9, 'SetTransformParent', ((1, 'visual'),)))
    IDCompositionVisual.SetEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionEffect_head)(10, 'SetEffect', ((1, 'effect'),)))
    IDCompositionVisual.SetBitmapInterpolationMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.DCOMPOSITION_BITMAP_INTERPOLATION_MODE)(11, 'SetBitmapInterpolationMode', ((1, 'interpolationMode'),)))
    IDCompositionVisual.SetBorderMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.DCOMPOSITION_BORDER_MODE)(12, 'SetBorderMode', ((1, 'borderMode'),)))
    IDCompositionVisual.SetClip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionClip_head)(13, 'SetClip', ((1, 'clip'),)))
    IDCompositionVisual.SetClip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head))(14, 'SetClip', ((1, 'rect'),)))
    IDCompositionVisual.SetContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(15, 'SetContent', ((1, 'content'),)))
    IDCompositionVisual.AddVisual = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionVisual_head,win32more.Foundation.BOOL,win32more.Graphics.DirectComposition.IDCompositionVisual_head)(16, 'AddVisual', ((1, 'visual'),(1, 'insertAbove'),(1, 'referenceVisual'),)))
    IDCompositionVisual.RemoveVisual = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionVisual_head)(17, 'RemoveVisual', ((1, 'visual'),)))
    IDCompositionVisual.RemoveAllVisuals = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(18, 'RemoveAllVisuals', ()))
    IDCompositionVisual.SetCompositeMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.DCOMPOSITION_COMPOSITE_MODE)(19, 'SetCompositeMode', ((1, 'compositeMode'),)))
    win32more.System.Com.IUnknown
    return IDCompositionVisual
def _define_IDCompositionVisual2_head():
    class IDCompositionVisual2(win32more.Graphics.DirectComposition.IDCompositionVisual_head):
        Guid = Guid('e8de1639-4331-4b26-bc-5f-6a-32-1d-34-7a-85')
    return IDCompositionVisual2
def _define_IDCompositionVisual2():
    IDCompositionVisual2 = win32more.Graphics.DirectComposition.IDCompositionVisual2_head
    IDCompositionVisual2.SetOpacityMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.DCOMPOSITION_OPACITY_MODE)(20, 'SetOpacityMode', ((1, 'mode'),)))
    IDCompositionVisual2.SetBackFaceVisibility = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.DCOMPOSITION_BACKFACE_VISIBILITY)(21, 'SetBackFaceVisibility', ((1, 'visibility'),)))
    win32more.Graphics.DirectComposition.IDCompositionVisual
    return IDCompositionVisual2
def _define_IDCompositionVisual3_head():
    class IDCompositionVisual3(win32more.Graphics.DirectComposition.IDCompositionVisualDebug_head):
        Guid = Guid('2775f462-b6c1-4015-b0-be-b3-e7-d6-a4-97-6d')
    return IDCompositionVisual3
def _define_IDCompositionVisual3():
    IDCompositionVisual3 = win32more.Graphics.DirectComposition.IDCompositionVisual3_head
    IDCompositionVisual3.SetDepthMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.DCOMPOSITION_DEPTH_MODE)(26, 'SetDepthMode', ((1, 'mode'),)))
    IDCompositionVisual3.SetOffsetZ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(27, 'SetOffsetZ', ((1, 'animation'),)))
    IDCompositionVisual3.SetOffsetZ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(28, 'SetOffsetZ', ((1, 'offsetZ'),)))
    IDCompositionVisual3.SetOpacity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head)(29, 'SetOpacity', ((1, 'animation'),)))
    IDCompositionVisual3.SetOpacity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(30, 'SetOpacity', ((1, 'opacity'),)))
    IDCompositionVisual3.SetTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionTransform3D_head)(31, 'SetTransform', ((1, 'transform'),)))
    IDCompositionVisual3.SetTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_4X4_F_head))(32, 'SetTransform', ((1, 'matrix'),)))
    IDCompositionVisual3.SetVisible = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(33, 'SetVisible', ((1, 'visible'),)))
    win32more.Graphics.DirectComposition.IDCompositionVisualDebug
    return IDCompositionVisual3
def _define_IDCompositionVisualDebug_head():
    class IDCompositionVisualDebug(win32more.Graphics.DirectComposition.IDCompositionVisual2_head):
        Guid = Guid('fed2b808-5eb4-43a0-ae-a3-35-f6-52-80-f9-1b')
    return IDCompositionVisualDebug
def _define_IDCompositionVisualDebug():
    IDCompositionVisualDebug = win32more.Graphics.DirectComposition.IDCompositionVisualDebug_head
    IDCompositionVisualDebug.EnableHeatMap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D1_COLOR_F_head))(22, 'EnableHeatMap', ((1, 'color'),)))
    IDCompositionVisualDebug.DisableHeatMap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(23, 'DisableHeatMap', ()))
    IDCompositionVisualDebug.EnableRedrawRegions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(24, 'EnableRedrawRegions', ()))
    IDCompositionVisualDebug.DisableRedrawRegions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(25, 'DisableRedrawRegions', ()))
    win32more.Graphics.DirectComposition.IDCompositionVisual2
    return IDCompositionVisualDebug
__all__ = [
    "COMPOSITIONOBJECT_READ",
    "COMPOSITIONOBJECT_WRITE",
    "COMPOSITION_FRAME_ID_COMPLETED",
    "COMPOSITION_FRAME_ID_CONFIRMED",
    "COMPOSITION_FRAME_ID_CREATED",
    "COMPOSITION_FRAME_ID_TYPE",
    "COMPOSITION_FRAME_STATS",
    "COMPOSITION_STATS",
    "COMPOSITION_STATS_MAX_TARGETS",
    "COMPOSITION_TARGET_ID",
    "COMPOSITION_TARGET_STATS",
    "DCOMPOSITION_BACKFACE_VISIBILITY",
    "DCOMPOSITION_BACKFACE_VISIBILITY_HIDDEN",
    "DCOMPOSITION_BACKFACE_VISIBILITY_INHERIT",
    "DCOMPOSITION_BACKFACE_VISIBILITY_VISIBLE",
    "DCOMPOSITION_BITMAP_INTERPOLATION_MODE",
    "DCOMPOSITION_BITMAP_INTERPOLATION_MODE_INHERIT",
    "DCOMPOSITION_BITMAP_INTERPOLATION_MODE_LINEAR",
    "DCOMPOSITION_BITMAP_INTERPOLATION_MODE_NEAREST_NEIGHBOR",
    "DCOMPOSITION_BORDER_MODE",
    "DCOMPOSITION_BORDER_MODE_HARD",
    "DCOMPOSITION_BORDER_MODE_INHERIT",
    "DCOMPOSITION_BORDER_MODE_SOFT",
    "DCOMPOSITION_COMPOSITE_MODE",
    "DCOMPOSITION_COMPOSITE_MODE_DESTINATION_INVERT",
    "DCOMPOSITION_COMPOSITE_MODE_INHERIT",
    "DCOMPOSITION_COMPOSITE_MODE_MIN_BLEND",
    "DCOMPOSITION_COMPOSITE_MODE_SOURCE_OVER",
    "DCOMPOSITION_DEPTH_MODE",
    "DCOMPOSITION_DEPTH_MODE_INHERIT",
    "DCOMPOSITION_DEPTH_MODE_SORTED",
    "DCOMPOSITION_DEPTH_MODE_SPATIAL",
    "DCOMPOSITION_DEPTH_MODE_TREE",
    "DCOMPOSITION_FRAME_STATISTICS",
    "DCOMPOSITION_MAX_WAITFORCOMPOSITORCLOCK_OBJECTS",
    "DCOMPOSITION_OPACITY_MODE",
    "DCOMPOSITION_OPACITY_MODE_INHERIT",
    "DCOMPOSITION_OPACITY_MODE_LAYER",
    "DCOMPOSITION_OPACITY_MODE_MULTIPLY",
    "DCompositionAttachMouseDragToHwnd",
    "DCompositionAttachMouseWheelToHwnd",
    "DCompositionBoostCompositorClock",
    "DCompositionCreateDevice",
    "DCompositionCreateDevice2",
    "DCompositionCreateDevice3",
    "DCompositionCreateSurfaceHandle",
    "DCompositionGetFrameId",
    "DCompositionGetStatistics",
    "DCompositionGetTargetStatistics",
    "DCompositionInkTrailPoint",
    "DCompositionWaitForCompositorClock",
    "IDCompositionAffineTransform2DEffect",
    "IDCompositionAnimation",
    "IDCompositionArithmeticCompositeEffect",
    "IDCompositionBlendEffect",
    "IDCompositionBrightnessEffect",
    "IDCompositionClip",
    "IDCompositionColorMatrixEffect",
    "IDCompositionCompositeEffect",
    "IDCompositionDelegatedInkTrail",
    "IDCompositionDesktopDevice",
    "IDCompositionDevice",
    "IDCompositionDevice2",
    "IDCompositionDevice3",
    "IDCompositionDeviceDebug",
    "IDCompositionEffect",
    "IDCompositionEffectGroup",
    "IDCompositionFilterEffect",
    "IDCompositionGaussianBlurEffect",
    "IDCompositionHueRotationEffect",
    "IDCompositionInkTrailDevice",
    "IDCompositionLinearTransferEffect",
    "IDCompositionMatrixTransform",
    "IDCompositionMatrixTransform3D",
    "IDCompositionRectangleClip",
    "IDCompositionRotateTransform",
    "IDCompositionRotateTransform3D",
    "IDCompositionSaturationEffect",
    "IDCompositionScaleTransform",
    "IDCompositionScaleTransform3D",
    "IDCompositionShadowEffect",
    "IDCompositionSkewTransform",
    "IDCompositionSurface",
    "IDCompositionSurfaceFactory",
    "IDCompositionTableTransferEffect",
    "IDCompositionTarget",
    "IDCompositionTransform",
    "IDCompositionTransform3D",
    "IDCompositionTranslateTransform",
    "IDCompositionTranslateTransform3D",
    "IDCompositionTurbulenceEffect",
    "IDCompositionVirtualSurface",
    "IDCompositionVisual",
    "IDCompositionVisual2",
    "IDCompositionVisual3",
    "IDCompositionVisualDebug",
]
