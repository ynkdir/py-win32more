from win32more import *
import win32more.Foundation
import win32more.Graphics.DirectManipulation
import win32more.System.Com
import win32more.UI.WindowsAndMessaging

def __getattr__(name):
    module = globals()
    try:
        f = module[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    module[name] = f()
    return module[name]
def __dir__():
    return __all__
DIRECTMANIPULATION_KEYBOARDFOCUS = 4294967294
DIRECTMANIPULATION_MOUSEFOCUS = 4294967293
CLSID_VerticalIndicatorContent = 'a10b5f17-afe0-4aa2-91e9-3e7001d2e6b4'
CLSID_HorizontalIndicatorContent = 'e7d18cf5-3ec7-44d5-a76b-3770f3cf903d'
CLSID_VirtualViewportContent = '3206a19a-86f0-4cb4-a7f3-16e3b7e2d852'
CLSID_DragDropConfigurationBehavior = '09b01b3e-ba6c-454d-82e8-95e352329f23'
CLSID_AutoScrollBehavior = '26126a51-3c70-4c9a-aec2-948849eeb093'
CLSID_DeferContactService = 'd7b67cf4-84bb-434e-86ae-6592bbc9abd9'
DirectManipulationViewport = Guid('34e211b6-3650-4f75-8334-fa359598e1c5')
DirectManipulationUpdateManager = Guid('9fc1bfd5-1835-441a-b3b1-b6cc74b727d0')
DirectManipulationPrimaryContent = Guid('caa02661-d59e-41c7-8393-3ba3bacb6b57')
DirectManipulationManager = Guid('54e211b6-3650-4f75-8334-fa359598e1c5')
DirectManipulationSharedManager = Guid('99793286-77cc-4b57-96db-3b354f6f9fb5')
DCompManipulationCompositor = Guid('79dea627-a08a-43ac-8ef5-6900b9299126')
DIRECTMANIPULATION_STATUS = Int32
DIRECTMANIPULATION_BUILDING = 0
DIRECTMANIPULATION_ENABLED = 1
DIRECTMANIPULATION_DISABLED = 2
DIRECTMANIPULATION_RUNNING = 3
DIRECTMANIPULATION_INERTIA = 4
DIRECTMANIPULATION_READY = 5
DIRECTMANIPULATION_SUSPENDED = 6
DIRECTMANIPULATION_HITTEST_TYPE = Int32
DIRECTMANIPULATION_HITTEST_TYPE_ASYNCHRONOUS = 0
DIRECTMANIPULATION_HITTEST_TYPE_SYNCHRONOUS = 1
DIRECTMANIPULATION_HITTEST_TYPE_AUTO_SYNCHRONOUS = 2
DIRECTMANIPULATION_CONFIGURATION = Int32
DIRECTMANIPULATION_CONFIGURATION_NONE = 0
DIRECTMANIPULATION_CONFIGURATION_INTERACTION = 1
DIRECTMANIPULATION_CONFIGURATION_TRANSLATION_X = 2
DIRECTMANIPULATION_CONFIGURATION_TRANSLATION_Y = 4
DIRECTMANIPULATION_CONFIGURATION_SCALING = 16
DIRECTMANIPULATION_CONFIGURATION_TRANSLATION_INERTIA = 32
DIRECTMANIPULATION_CONFIGURATION_SCALING_INERTIA = 128
DIRECTMANIPULATION_CONFIGURATION_RAILS_X = 256
DIRECTMANIPULATION_CONFIGURATION_RAILS_Y = 512
DIRECTMANIPULATION_GESTURE_CONFIGURATION = Int32
DIRECTMANIPULATION_GESTURE_NONE = 0
DIRECTMANIPULATION_GESTURE_DEFAULT = 0
DIRECTMANIPULATION_GESTURE_CROSS_SLIDE_VERTICAL = 8
DIRECTMANIPULATION_GESTURE_CROSS_SLIDE_HORIZONTAL = 16
DIRECTMANIPULATION_GESTURE_PINCH_ZOOM = 32
DIRECTMANIPULATION_MOTION_TYPES = Int32
DIRECTMANIPULATION_MOTION_NONE = 0
DIRECTMANIPULATION_MOTION_TRANSLATEX = 1
DIRECTMANIPULATION_MOTION_TRANSLATEY = 2
DIRECTMANIPULATION_MOTION_ZOOM = 4
DIRECTMANIPULATION_MOTION_CENTERX = 16
DIRECTMANIPULATION_MOTION_CENTERY = 32
DIRECTMANIPULATION_MOTION_ALL = 55
DIRECTMANIPULATION_VIEWPORT_OPTIONS = Int32
DIRECTMANIPULATION_VIEWPORT_OPTIONS_DEFAULT = 0
DIRECTMANIPULATION_VIEWPORT_OPTIONS_AUTODISABLE = 1
DIRECTMANIPULATION_VIEWPORT_OPTIONS_MANUALUPDATE = 2
DIRECTMANIPULATION_VIEWPORT_OPTIONS_INPUT = 4
DIRECTMANIPULATION_VIEWPORT_OPTIONS_EXPLICITHITTEST = 8
DIRECTMANIPULATION_VIEWPORT_OPTIONS_DISABLEPIXELSNAPPING = 16
DIRECTMANIPULATION_SNAPPOINT_TYPE = Int32
DIRECTMANIPULATION_SNAPPOINT_MANDATORY = 0
DIRECTMANIPULATION_SNAPPOINT_OPTIONAL = 1
DIRECTMANIPULATION_SNAPPOINT_MANDATORY_SINGLE = 2
DIRECTMANIPULATION_SNAPPOINT_OPTIONAL_SINGLE = 3
DIRECTMANIPULATION_SNAPPOINT_COORDINATE = Int32
DIRECTMANIPULATION_COORDINATE_BOUNDARY = 0
DIRECTMANIPULATION_COORDINATE_ORIGIN = 1
DIRECTMANIPULATION_COORDINATE_MIRRORED = 16
DIRECTMANIPULATION_HORIZONTALALIGNMENT = Int32
DIRECTMANIPULATION_HORIZONTALALIGNMENT_NONE = 0
DIRECTMANIPULATION_HORIZONTALALIGNMENT_LEFT = 1
DIRECTMANIPULATION_HORIZONTALALIGNMENT_CENTER = 2
DIRECTMANIPULATION_HORIZONTALALIGNMENT_RIGHT = 4
DIRECTMANIPULATION_HORIZONTALALIGNMENT_UNLOCKCENTER = 8
DIRECTMANIPULATION_VERTICALALIGNMENT = Int32
DIRECTMANIPULATION_VERTICALALIGNMENT_NONE = 0
DIRECTMANIPULATION_VERTICALALIGNMENT_TOP = 1
DIRECTMANIPULATION_VERTICALALIGNMENT_CENTER = 2
DIRECTMANIPULATION_VERTICALALIGNMENT_BOTTOM = 4
DIRECTMANIPULATION_VERTICALALIGNMENT_UNLOCKCENTER = 8
DIRECTMANIPULATION_INPUT_MODE = Int32
DIRECTMANIPULATION_INPUT_MODE_AUTOMATIC = 0
DIRECTMANIPULATION_INPUT_MODE_MANUAL = 1
def _define_IDirectManipulationManager_head():
    class IDirectManipulationManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('fbf5d3b4-70c7-4163-9322-5a6f660d6fbc')
    return IDirectManipulationManager
def _define_IDirectManipulationManager():
    IDirectManipulationManager = win32more.Graphics.DirectManipulation.IDirectManipulationManager_head
    IDirectManipulationManager.Activate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND, use_last_error=False)(3, 'Activate', ((1, 'window'),)))
    IDirectManipulationManager.Deactivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND, use_last_error=False)(4, 'Deactivate', ((1, 'window'),)))
    IDirectManipulationManager.RegisterHitTestTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.HWND,win32more.Graphics.DirectManipulation.DIRECTMANIPULATION_HITTEST_TYPE, use_last_error=False)(5, 'RegisterHitTestTarget', ((1, 'window'),(1, 'hitTestWindow'),(1, 'type'),)))
    IDirectManipulationManager.ProcessInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.WindowsAndMessaging.MSG_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'ProcessInput', ((1, 'message'),(1, 'handled'),)))
    IDirectManipulationManager.GetUpdateManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(7, 'GetUpdateManager', ((1, 'riid'),(1, 'object'),)))
    IDirectManipulationManager.CreateViewport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.IDirectManipulationFrameInfoProvider_head,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(8, 'CreateViewport', ((1, 'frameInfo'),(1, 'window'),(1, 'riid'),(1, 'object'),)))
    IDirectManipulationManager.CreateContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.IDirectManipulationFrameInfoProvider_head,POINTER(Guid),POINTER(Guid),POINTER(c_void_p), use_last_error=False)(9, 'CreateContent', ((1, 'frameInfo'),(1, 'clsid'),(1, 'riid'),(1, 'object'),)))
    return IDirectManipulationManager
def _define_IDirectManipulationManager2_head():
    class IDirectManipulationManager2(win32more.Graphics.DirectManipulation.IDirectManipulationManager_head):
        Guid = Guid('fa1005e9-3d16-484c-bfc9-62b61e56ec4e')
    return IDirectManipulationManager2
def _define_IDirectManipulationManager2():
    IDirectManipulationManager2 = win32more.Graphics.DirectManipulation.IDirectManipulationManager2_head
    IDirectManipulationManager2.CreateBehavior = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(c_void_p), use_last_error=False)(10, 'CreateBehavior', ((1, 'clsid'),(1, 'riid'),(1, 'object'),)))
    return IDirectManipulationManager2
def _define_IDirectManipulationManager3_head():
    class IDirectManipulationManager3(win32more.Graphics.DirectManipulation.IDirectManipulationManager2_head):
        Guid = Guid('2cb6b33d-ffe8-488c-b750-fbdfe88dca8c')
    return IDirectManipulationManager3
def _define_IDirectManipulationManager3():
    IDirectManipulationManager3 = win32more.Graphics.DirectManipulation.IDirectManipulationManager3_head
    IDirectManipulationManager3.GetService = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(c_void_p), use_last_error=False)(11, 'GetService', ((1, 'clsid'),(1, 'riid'),(1, 'object'),)))
    return IDirectManipulationManager3
def _define_IDirectManipulationViewport_head():
    class IDirectManipulationViewport(win32more.System.Com.IUnknown_head):
        Guid = Guid('28b85a3d-60a0-48bd-9ba1-5ce8d9ea3a6d')
    return IDirectManipulationViewport
def _define_IDirectManipulationViewport():
    IDirectManipulationViewport = win32more.Graphics.DirectManipulation.IDirectManipulationViewport_head
    IDirectManipulationViewport.Enable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Enable', ()))
    IDirectManipulationViewport.Disable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Disable', ()))
    IDirectManipulationViewport.SetContact = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'SetContact', ((1, 'pointerId'),)))
    IDirectManipulationViewport.ReleaseContact = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'ReleaseContact', ((1, 'pointerId'),)))
    IDirectManipulationViewport.ReleaseAllContacts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'ReleaseAllContacts', ()))
    IDirectManipulationViewport.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectManipulation.DIRECTMANIPULATION_STATUS), use_last_error=False)(8, 'GetStatus', ((1, 'status'),)))
    IDirectManipulationViewport.GetTag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p),POINTER(UInt32), use_last_error=False)(9, 'GetTag', ((1, 'riid'),(1, 'object'),(1, 'id'),)))
    IDirectManipulationViewport.SetTag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,UInt32, use_last_error=False)(10, 'SetTag', ((1, 'object'),(1, 'id'),)))
    IDirectManipulationViewport.GetViewportRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(11, 'GetViewportRect', ((1, 'viewport'),)))
    IDirectManipulationViewport.SetViewportRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(12, 'SetViewportRect', ((1, 'viewport'),)))
    IDirectManipulationViewport.ZoomToRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,Single,Single,win32more.Foundation.BOOL, use_last_error=False)(13, 'ZoomToRect', ((1, 'left'),(1, 'top'),(1, 'right'),(1, 'bottom'),(1, 'animate'),)))
    IDirectManipulationViewport.SetViewportTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),UInt32, use_last_error=False)(14, 'SetViewportTransform', ((1, 'matrix'),(1, 'pointCount'),)))
    IDirectManipulationViewport.SyncDisplayTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),UInt32, use_last_error=False)(15, 'SyncDisplayTransform', ((1, 'matrix'),(1, 'pointCount'),)))
    IDirectManipulationViewport.GetPrimaryContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(16, 'GetPrimaryContent', ((1, 'riid'),(1, 'object'),)))
    IDirectManipulationViewport.AddContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.IDirectManipulationContent_head, use_last_error=False)(17, 'AddContent', ((1, 'content'),)))
    IDirectManipulationViewport.RemoveContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.IDirectManipulationContent_head, use_last_error=False)(18, 'RemoveContent', ((1, 'content'),)))
    IDirectManipulationViewport.SetViewportOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.DIRECTMANIPULATION_VIEWPORT_OPTIONS, use_last_error=False)(19, 'SetViewportOptions', ((1, 'options'),)))
    IDirectManipulationViewport.AddConfiguration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.DIRECTMANIPULATION_CONFIGURATION, use_last_error=False)(20, 'AddConfiguration', ((1, 'configuration'),)))
    IDirectManipulationViewport.RemoveConfiguration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.DIRECTMANIPULATION_CONFIGURATION, use_last_error=False)(21, 'RemoveConfiguration', ((1, 'configuration'),)))
    IDirectManipulationViewport.ActivateConfiguration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.DIRECTMANIPULATION_CONFIGURATION, use_last_error=False)(22, 'ActivateConfiguration', ((1, 'configuration'),)))
    IDirectManipulationViewport.SetManualGesture = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.DIRECTMANIPULATION_GESTURE_CONFIGURATION, use_last_error=False)(23, 'SetManualGesture', ((1, 'configuration'),)))
    IDirectManipulationViewport.SetChaining = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.DIRECTMANIPULATION_MOTION_TYPES, use_last_error=False)(24, 'SetChaining', ((1, 'enabledTypes'),)))
    IDirectManipulationViewport.AddEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Graphics.DirectManipulation.IDirectManipulationViewportEventHandler_head,POINTER(UInt32), use_last_error=False)(25, 'AddEventHandler', ((1, 'window'),(1, 'eventHandler'),(1, 'cookie'),)))
    IDirectManipulationViewport.RemoveEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(26, 'RemoveEventHandler', ((1, 'cookie'),)))
    IDirectManipulationViewport.SetInputMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.DIRECTMANIPULATION_INPUT_MODE, use_last_error=False)(27, 'SetInputMode', ((1, 'mode'),)))
    IDirectManipulationViewport.SetUpdateMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.DIRECTMANIPULATION_INPUT_MODE, use_last_error=False)(28, 'SetUpdateMode', ((1, 'mode'),)))
    IDirectManipulationViewport.Stop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(29, 'Stop', ()))
    IDirectManipulationViewport.Abandon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(30, 'Abandon', ()))
    return IDirectManipulationViewport
def _define_IDirectManipulationViewport2_head():
    class IDirectManipulationViewport2(win32more.Graphics.DirectManipulation.IDirectManipulationViewport_head):
        Guid = Guid('923ccaac-61e1-4385-b726-017af189882a')
    return IDirectManipulationViewport2
def _define_IDirectManipulationViewport2():
    IDirectManipulationViewport2 = win32more.Graphics.DirectManipulation.IDirectManipulationViewport2_head
    IDirectManipulationViewport2.AddBehavior = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(UInt32), use_last_error=False)(31, 'AddBehavior', ((1, 'behavior'),(1, 'cookie'),)))
    IDirectManipulationViewport2.RemoveBehavior = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(32, 'RemoveBehavior', ((1, 'cookie'),)))
    IDirectManipulationViewport2.RemoveAllBehaviors = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(33, 'RemoveAllBehaviors', ()))
    return IDirectManipulationViewport2
def _define_IDirectManipulationViewportEventHandler_head():
    class IDirectManipulationViewportEventHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('952121da-d69f-45f9-b0f9-f23944321a6d')
    return IDirectManipulationViewportEventHandler
def _define_IDirectManipulationViewportEventHandler():
    IDirectManipulationViewportEventHandler = win32more.Graphics.DirectManipulation.IDirectManipulationViewportEventHandler_head
    IDirectManipulationViewportEventHandler.OnViewportStatusChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.IDirectManipulationViewport_head,win32more.Graphics.DirectManipulation.DIRECTMANIPULATION_STATUS,win32more.Graphics.DirectManipulation.DIRECTMANIPULATION_STATUS, use_last_error=False)(3, 'OnViewportStatusChanged', ((1, 'viewport'),(1, 'current'),(1, 'previous'),)))
    IDirectManipulationViewportEventHandler.OnViewportUpdated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.IDirectManipulationViewport_head, use_last_error=False)(4, 'OnViewportUpdated', ((1, 'viewport'),)))
    IDirectManipulationViewportEventHandler.OnContentUpdated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.IDirectManipulationViewport_head,win32more.Graphics.DirectManipulation.IDirectManipulationContent_head, use_last_error=False)(5, 'OnContentUpdated', ((1, 'viewport'),(1, 'content'),)))
    return IDirectManipulationViewportEventHandler
def _define_IDirectManipulationContent_head():
    class IDirectManipulationContent(win32more.System.Com.IUnknown_head):
        Guid = Guid('b89962cb-3d89-442b-bb58-5098fa0f9f16')
    return IDirectManipulationContent
def _define_IDirectManipulationContent():
    IDirectManipulationContent = win32more.Graphics.DirectManipulation.IDirectManipulationContent_head
    IDirectManipulationContent.GetContentRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(3, 'GetContentRect', ((1, 'contentSize'),)))
    IDirectManipulationContent.SetContentRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(4, 'SetContentRect', ((1, 'contentSize'),)))
    IDirectManipulationContent.GetViewport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(5, 'GetViewport', ((1, 'riid'),(1, 'object'),)))
    IDirectManipulationContent.GetTag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p),POINTER(UInt32), use_last_error=False)(6, 'GetTag', ((1, 'riid'),(1, 'object'),(1, 'id'),)))
    IDirectManipulationContent.SetTag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,UInt32, use_last_error=False)(7, 'SetTag', ((1, 'object'),(1, 'id'),)))
    IDirectManipulationContent.GetOutputTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),UInt32, use_last_error=False)(8, 'GetOutputTransform', ((1, 'matrix'),(1, 'pointCount'),)))
    IDirectManipulationContent.GetContentTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),UInt32, use_last_error=False)(9, 'GetContentTransform', ((1, 'matrix'),(1, 'pointCount'),)))
    IDirectManipulationContent.SyncContentTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),UInt32, use_last_error=False)(10, 'SyncContentTransform', ((1, 'matrix'),(1, 'pointCount'),)))
    return IDirectManipulationContent
def _define_IDirectManipulationPrimaryContent_head():
    class IDirectManipulationPrimaryContent(win32more.System.Com.IUnknown_head):
        Guid = Guid('c12851e4-1698-4625-b9b1-7ca3ec18630b')
    return IDirectManipulationPrimaryContent
def _define_IDirectManipulationPrimaryContent():
    IDirectManipulationPrimaryContent = win32more.Graphics.DirectManipulation.IDirectManipulationPrimaryContent_head
    IDirectManipulationPrimaryContent.SetSnapInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.DIRECTMANIPULATION_MOTION_TYPES,Single,Single, use_last_error=False)(3, 'SetSnapInterval', ((1, 'motion'),(1, 'interval'),(1, 'offset'),)))
    IDirectManipulationPrimaryContent.SetSnapPoints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.DIRECTMANIPULATION_MOTION_TYPES,POINTER(Single),UInt32, use_last_error=False)(4, 'SetSnapPoints', ((1, 'motion'),(1, 'points'),(1, 'pointCount'),)))
    IDirectManipulationPrimaryContent.SetSnapType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.DIRECTMANIPULATION_MOTION_TYPES,win32more.Graphics.DirectManipulation.DIRECTMANIPULATION_SNAPPOINT_TYPE, use_last_error=False)(5, 'SetSnapType', ((1, 'motion'),(1, 'type'),)))
    IDirectManipulationPrimaryContent.SetSnapCoordinate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.DIRECTMANIPULATION_MOTION_TYPES,win32more.Graphics.DirectManipulation.DIRECTMANIPULATION_SNAPPOINT_COORDINATE,Single, use_last_error=False)(6, 'SetSnapCoordinate', ((1, 'motion'),(1, 'coordinate'),(1, 'origin'),)))
    IDirectManipulationPrimaryContent.SetZoomBoundaries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single, use_last_error=False)(7, 'SetZoomBoundaries', ((1, 'zoomMinimum'),(1, 'zoomMaximum'),)))
    IDirectManipulationPrimaryContent.SetHorizontalAlignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.DIRECTMANIPULATION_HORIZONTALALIGNMENT, use_last_error=False)(8, 'SetHorizontalAlignment', ((1, 'alignment'),)))
    IDirectManipulationPrimaryContent.SetVerticalAlignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.DIRECTMANIPULATION_VERTICALALIGNMENT, use_last_error=False)(9, 'SetVerticalAlignment', ((1, 'alignment'),)))
    IDirectManipulationPrimaryContent.GetInertiaEndTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),UInt32, use_last_error=False)(10, 'GetInertiaEndTransform', ((1, 'matrix'),(1, 'pointCount'),)))
    IDirectManipulationPrimaryContent.GetCenterPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),POINTER(Single), use_last_error=False)(11, 'GetCenterPoint', ((1, 'centerX'),(1, 'centerY'),)))
    return IDirectManipulationPrimaryContent
DIRECTMANIPULATION_DRAG_DROP_STATUS = Int32
DIRECTMANIPULATION_DRAG_DROP_READY = 0
DIRECTMANIPULATION_DRAG_DROP_PRESELECT = 1
DIRECTMANIPULATION_DRAG_DROP_SELECTING = 2
DIRECTMANIPULATION_DRAG_DROP_DRAGGING = 3
DIRECTMANIPULATION_DRAG_DROP_CANCELLED = 4
DIRECTMANIPULATION_DRAG_DROP_COMMITTED = 5
def _define_IDirectManipulationDragDropEventHandler_head():
    class IDirectManipulationDragDropEventHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('1fa11b10-701b-41ae-b5f2-49e36bd595aa')
    return IDirectManipulationDragDropEventHandler
def _define_IDirectManipulationDragDropEventHandler():
    IDirectManipulationDragDropEventHandler = win32more.Graphics.DirectManipulation.IDirectManipulationDragDropEventHandler_head
    IDirectManipulationDragDropEventHandler.OnDragDropStatusChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.IDirectManipulationViewport2_head,win32more.Graphics.DirectManipulation.DIRECTMANIPULATION_DRAG_DROP_STATUS,win32more.Graphics.DirectManipulation.DIRECTMANIPULATION_DRAG_DROP_STATUS, use_last_error=False)(3, 'OnDragDropStatusChange', ((1, 'viewport'),(1, 'current'),(1, 'previous'),)))
    return IDirectManipulationDragDropEventHandler
DIRECTMANIPULATION_DRAG_DROP_CONFIGURATION = Int32
DIRECTMANIPULATION_DRAG_DROP_CONFIGURATION_VERTICAL = 1
DIRECTMANIPULATION_DRAG_DROP_CONFIGURATION_HORIZONTAL = 2
DIRECTMANIPULATION_DRAG_DROP_CONFIGURATION_SELECT_ONLY = 16
DIRECTMANIPULATION_DRAG_DROP_CONFIGURATION_SELECT_DRAG = 32
DIRECTMANIPULATION_DRAG_DROP_CONFIGURATION_HOLD_DRAG = 64
def _define_IDirectManipulationDragDropBehavior_head():
    class IDirectManipulationDragDropBehavior(win32more.System.Com.IUnknown_head):
        Guid = Guid('814b5af5-c2c8-4270-a9b7-a198ce8d02fa')
    return IDirectManipulationDragDropBehavior
def _define_IDirectManipulationDragDropBehavior():
    IDirectManipulationDragDropBehavior = win32more.Graphics.DirectManipulation.IDirectManipulationDragDropBehavior_head
    IDirectManipulationDragDropBehavior.SetConfiguration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.DIRECTMANIPULATION_DRAG_DROP_CONFIGURATION, use_last_error=False)(3, 'SetConfiguration', ((1, 'configuration'),)))
    IDirectManipulationDragDropBehavior.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectManipulation.DIRECTMANIPULATION_DRAG_DROP_STATUS), use_last_error=False)(4, 'GetStatus', ((1, 'status'),)))
    return IDirectManipulationDragDropBehavior
DIRECTMANIPULATION_INTERACTION_TYPE = Int32
DIRECTMANIPULATION_INTERACTION_BEGIN = 0
DIRECTMANIPULATION_INTERACTION_TYPE_MANIPULATION = 1
DIRECTMANIPULATION_INTERACTION_TYPE_GESTURE_TAP = 2
DIRECTMANIPULATION_INTERACTION_TYPE_GESTURE_HOLD = 3
DIRECTMANIPULATION_INTERACTION_TYPE_GESTURE_CROSS_SLIDE = 4
DIRECTMANIPULATION_INTERACTION_TYPE_GESTURE_PINCH_ZOOM = 5
DIRECTMANIPULATION_INTERACTION_END = 100
def _define_IDirectManipulationInteractionEventHandler_head():
    class IDirectManipulationInteractionEventHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('e43f45b8-42b4-403e-b1f2-273b8f510830')
    return IDirectManipulationInteractionEventHandler
def _define_IDirectManipulationInteractionEventHandler():
    IDirectManipulationInteractionEventHandler = win32more.Graphics.DirectManipulation.IDirectManipulationInteractionEventHandler_head
    IDirectManipulationInteractionEventHandler.OnInteraction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.IDirectManipulationViewport2_head,win32more.Graphics.DirectManipulation.DIRECTMANIPULATION_INTERACTION_TYPE, use_last_error=False)(3, 'OnInteraction', ((1, 'viewport'),(1, 'interaction'),)))
    return IDirectManipulationInteractionEventHandler
def _define_IDirectManipulationFrameInfoProvider_head():
    class IDirectManipulationFrameInfoProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('fb759dba-6f4c-4c01-874e-19c8a05907f9')
    return IDirectManipulationFrameInfoProvider
def _define_IDirectManipulationFrameInfoProvider():
    IDirectManipulationFrameInfoProvider = win32more.Graphics.DirectManipulation.IDirectManipulationFrameInfoProvider_head
    IDirectManipulationFrameInfoProvider.GetNextFrameInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64),POINTER(UInt64),POINTER(UInt64), use_last_error=False)(3, 'GetNextFrameInfo', ((1, 'time'),(1, 'processTime'),(1, 'compositionTime'),)))
    return IDirectManipulationFrameInfoProvider
def _define_IDirectManipulationCompositor_head():
    class IDirectManipulationCompositor(win32more.System.Com.IUnknown_head):
        Guid = Guid('537a0825-0387-4efa-b62f-71eb1f085a7e')
    return IDirectManipulationCompositor
def _define_IDirectManipulationCompositor():
    IDirectManipulationCompositor = win32more.Graphics.DirectManipulation.IDirectManipulationCompositor_head
    IDirectManipulationCompositor.AddContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.IDirectManipulationContent_head,win32more.System.Com.IUnknown_head,win32more.System.Com.IUnknown_head,win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'AddContent', ((1, 'content'),(1, 'device'),(1, 'parentVisual'),(1, 'childVisual'),)))
    IDirectManipulationCompositor.RemoveContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.IDirectManipulationContent_head, use_last_error=False)(4, 'RemoveContent', ((1, 'content'),)))
    IDirectManipulationCompositor.SetUpdateManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.IDirectManipulationUpdateManager_head, use_last_error=False)(5, 'SetUpdateManager', ((1, 'updateManager'),)))
    IDirectManipulationCompositor.Flush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'Flush', ()))
    return IDirectManipulationCompositor
def _define_IDirectManipulationCompositor2_head():
    class IDirectManipulationCompositor2(win32more.Graphics.DirectManipulation.IDirectManipulationCompositor_head):
        Guid = Guid('d38c7822-f1cb-43cb-b4b9-ac0c767a412e')
    return IDirectManipulationCompositor2
def _define_IDirectManipulationCompositor2():
    IDirectManipulationCompositor2 = win32more.Graphics.DirectManipulation.IDirectManipulationCompositor2_head
    IDirectManipulationCompositor2.AddContentWithCrossProcessChaining = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.IDirectManipulationPrimaryContent_head,win32more.System.Com.IUnknown_head,win32more.System.Com.IUnknown_head,win32more.System.Com.IUnknown_head, use_last_error=False)(7, 'AddContentWithCrossProcessChaining', ((1, 'content'),(1, 'device'),(1, 'parentVisual'),(1, 'childVisual'),)))
    return IDirectManipulationCompositor2
def _define_IDirectManipulationUpdateHandler_head():
    class IDirectManipulationUpdateHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('790b6337-64f8-4ff5-a269-b32bc2af27a7')
    return IDirectManipulationUpdateHandler
def _define_IDirectManipulationUpdateHandler():
    IDirectManipulationUpdateHandler = win32more.Graphics.DirectManipulation.IDirectManipulationUpdateHandler_head
    IDirectManipulationUpdateHandler.Update = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Update', ()))
    return IDirectManipulationUpdateHandler
def _define_IDirectManipulationUpdateManager_head():
    class IDirectManipulationUpdateManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('b0ae62fd-be34-46e7-9caa-d361facbb9cc')
    return IDirectManipulationUpdateManager
def _define_IDirectManipulationUpdateManager():
    IDirectManipulationUpdateManager = win32more.Graphics.DirectManipulation.IDirectManipulationUpdateManager_head
    IDirectManipulationUpdateManager.RegisterWaitHandleCallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,win32more.Graphics.DirectManipulation.IDirectManipulationUpdateHandler_head,POINTER(UInt32), use_last_error=False)(3, 'RegisterWaitHandleCallback', ((1, 'handle'),(1, 'eventHandler'),(1, 'cookie'),)))
    IDirectManipulationUpdateManager.UnregisterWaitHandleCallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'UnregisterWaitHandleCallback', ((1, 'cookie'),)))
    IDirectManipulationUpdateManager.Update = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.IDirectManipulationFrameInfoProvider_head, use_last_error=False)(5, 'Update', ((1, 'frameInfo'),)))
    return IDirectManipulationUpdateManager
DIRECTMANIPULATION_AUTOSCROLL_CONFIGURATION = Int32
DIRECTMANIPULATION_AUTOSCROLL_CONFIGURATION_STOP = 0
DIRECTMANIPULATION_AUTOSCROLL_CONFIGURATION_FORWARD = 1
DIRECTMANIPULATION_AUTOSCROLL_CONFIGURATION_REVERSE = 2
def _define_IDirectManipulationAutoScrollBehavior_head():
    class IDirectManipulationAutoScrollBehavior(win32more.System.Com.IUnknown_head):
        Guid = Guid('6d5954d4-2003-4356-9b31-d051c9ff0af7')
    return IDirectManipulationAutoScrollBehavior
def _define_IDirectManipulationAutoScrollBehavior():
    IDirectManipulationAutoScrollBehavior = win32more.Graphics.DirectManipulation.IDirectManipulationAutoScrollBehavior_head
    IDirectManipulationAutoScrollBehavior.SetConfiguration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectManipulation.DIRECTMANIPULATION_MOTION_TYPES,win32more.Graphics.DirectManipulation.DIRECTMANIPULATION_AUTOSCROLL_CONFIGURATION, use_last_error=False)(3, 'SetConfiguration', ((1, 'motionTypes'),(1, 'scrollMotion'),)))
    return IDirectManipulationAutoScrollBehavior
def _define_IDirectManipulationDeferContactService_head():
    class IDirectManipulationDeferContactService(win32more.System.Com.IUnknown_head):
        Guid = Guid('652d5c71-fe60-4a98-be70-e5f21291e7f1')
    return IDirectManipulationDeferContactService
def _define_IDirectManipulationDeferContactService():
    IDirectManipulationDeferContactService = win32more.Graphics.DirectManipulation.IDirectManipulationDeferContactService_head
    IDirectManipulationDeferContactService.DeferContact = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(3, 'DeferContact', ((1, 'pointerId'),(1, 'timeout'),)))
    IDirectManipulationDeferContactService.CancelContact = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'CancelContact', ((1, 'pointerId'),)))
    IDirectManipulationDeferContactService.CancelDeferral = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'CancelDeferral', ((1, 'pointerId'),)))
    return IDirectManipulationDeferContactService
__all__ = [
    "DIRECTMANIPULATION_KEYBOARDFOCUS",
    "DIRECTMANIPULATION_MOUSEFOCUS",
    "CLSID_VerticalIndicatorContent",
    "CLSID_HorizontalIndicatorContent",
    "CLSID_VirtualViewportContent",
    "CLSID_DragDropConfigurationBehavior",
    "CLSID_AutoScrollBehavior",
    "CLSID_DeferContactService",
    "DirectManipulationViewport",
    "DirectManipulationUpdateManager",
    "DirectManipulationPrimaryContent",
    "DirectManipulationManager",
    "DirectManipulationSharedManager",
    "DCompManipulationCompositor",
    "DIRECTMANIPULATION_STATUS",
    "DIRECTMANIPULATION_BUILDING",
    "DIRECTMANIPULATION_ENABLED",
    "DIRECTMANIPULATION_DISABLED",
    "DIRECTMANIPULATION_RUNNING",
    "DIRECTMANIPULATION_INERTIA",
    "DIRECTMANIPULATION_READY",
    "DIRECTMANIPULATION_SUSPENDED",
    "DIRECTMANIPULATION_HITTEST_TYPE",
    "DIRECTMANIPULATION_HITTEST_TYPE_ASYNCHRONOUS",
    "DIRECTMANIPULATION_HITTEST_TYPE_SYNCHRONOUS",
    "DIRECTMANIPULATION_HITTEST_TYPE_AUTO_SYNCHRONOUS",
    "DIRECTMANIPULATION_CONFIGURATION",
    "DIRECTMANIPULATION_CONFIGURATION_NONE",
    "DIRECTMANIPULATION_CONFIGURATION_INTERACTION",
    "DIRECTMANIPULATION_CONFIGURATION_TRANSLATION_X",
    "DIRECTMANIPULATION_CONFIGURATION_TRANSLATION_Y",
    "DIRECTMANIPULATION_CONFIGURATION_SCALING",
    "DIRECTMANIPULATION_CONFIGURATION_TRANSLATION_INERTIA",
    "DIRECTMANIPULATION_CONFIGURATION_SCALING_INERTIA",
    "DIRECTMANIPULATION_CONFIGURATION_RAILS_X",
    "DIRECTMANIPULATION_CONFIGURATION_RAILS_Y",
    "DIRECTMANIPULATION_GESTURE_CONFIGURATION",
    "DIRECTMANIPULATION_GESTURE_NONE",
    "DIRECTMANIPULATION_GESTURE_DEFAULT",
    "DIRECTMANIPULATION_GESTURE_CROSS_SLIDE_VERTICAL",
    "DIRECTMANIPULATION_GESTURE_CROSS_SLIDE_HORIZONTAL",
    "DIRECTMANIPULATION_GESTURE_PINCH_ZOOM",
    "DIRECTMANIPULATION_MOTION_TYPES",
    "DIRECTMANIPULATION_MOTION_NONE",
    "DIRECTMANIPULATION_MOTION_TRANSLATEX",
    "DIRECTMANIPULATION_MOTION_TRANSLATEY",
    "DIRECTMANIPULATION_MOTION_ZOOM",
    "DIRECTMANIPULATION_MOTION_CENTERX",
    "DIRECTMANIPULATION_MOTION_CENTERY",
    "DIRECTMANIPULATION_MOTION_ALL",
    "DIRECTMANIPULATION_VIEWPORT_OPTIONS",
    "DIRECTMANIPULATION_VIEWPORT_OPTIONS_DEFAULT",
    "DIRECTMANIPULATION_VIEWPORT_OPTIONS_AUTODISABLE",
    "DIRECTMANIPULATION_VIEWPORT_OPTIONS_MANUALUPDATE",
    "DIRECTMANIPULATION_VIEWPORT_OPTIONS_INPUT",
    "DIRECTMANIPULATION_VIEWPORT_OPTIONS_EXPLICITHITTEST",
    "DIRECTMANIPULATION_VIEWPORT_OPTIONS_DISABLEPIXELSNAPPING",
    "DIRECTMANIPULATION_SNAPPOINT_TYPE",
    "DIRECTMANIPULATION_SNAPPOINT_MANDATORY",
    "DIRECTMANIPULATION_SNAPPOINT_OPTIONAL",
    "DIRECTMANIPULATION_SNAPPOINT_MANDATORY_SINGLE",
    "DIRECTMANIPULATION_SNAPPOINT_OPTIONAL_SINGLE",
    "DIRECTMANIPULATION_SNAPPOINT_COORDINATE",
    "DIRECTMANIPULATION_COORDINATE_BOUNDARY",
    "DIRECTMANIPULATION_COORDINATE_ORIGIN",
    "DIRECTMANIPULATION_COORDINATE_MIRRORED",
    "DIRECTMANIPULATION_HORIZONTALALIGNMENT",
    "DIRECTMANIPULATION_HORIZONTALALIGNMENT_NONE",
    "DIRECTMANIPULATION_HORIZONTALALIGNMENT_LEFT",
    "DIRECTMANIPULATION_HORIZONTALALIGNMENT_CENTER",
    "DIRECTMANIPULATION_HORIZONTALALIGNMENT_RIGHT",
    "DIRECTMANIPULATION_HORIZONTALALIGNMENT_UNLOCKCENTER",
    "DIRECTMANIPULATION_VERTICALALIGNMENT",
    "DIRECTMANIPULATION_VERTICALALIGNMENT_NONE",
    "DIRECTMANIPULATION_VERTICALALIGNMENT_TOP",
    "DIRECTMANIPULATION_VERTICALALIGNMENT_CENTER",
    "DIRECTMANIPULATION_VERTICALALIGNMENT_BOTTOM",
    "DIRECTMANIPULATION_VERTICALALIGNMENT_UNLOCKCENTER",
    "DIRECTMANIPULATION_INPUT_MODE",
    "DIRECTMANIPULATION_INPUT_MODE_AUTOMATIC",
    "DIRECTMANIPULATION_INPUT_MODE_MANUAL",
    "IDirectManipulationManager",
    "IDirectManipulationManager2",
    "IDirectManipulationManager3",
    "IDirectManipulationViewport",
    "IDirectManipulationViewport2",
    "IDirectManipulationViewportEventHandler",
    "IDirectManipulationContent",
    "IDirectManipulationPrimaryContent",
    "DIRECTMANIPULATION_DRAG_DROP_STATUS",
    "DIRECTMANIPULATION_DRAG_DROP_READY",
    "DIRECTMANIPULATION_DRAG_DROP_PRESELECT",
    "DIRECTMANIPULATION_DRAG_DROP_SELECTING",
    "DIRECTMANIPULATION_DRAG_DROP_DRAGGING",
    "DIRECTMANIPULATION_DRAG_DROP_CANCELLED",
    "DIRECTMANIPULATION_DRAG_DROP_COMMITTED",
    "IDirectManipulationDragDropEventHandler",
    "DIRECTMANIPULATION_DRAG_DROP_CONFIGURATION",
    "DIRECTMANIPULATION_DRAG_DROP_CONFIGURATION_VERTICAL",
    "DIRECTMANIPULATION_DRAG_DROP_CONFIGURATION_HORIZONTAL",
    "DIRECTMANIPULATION_DRAG_DROP_CONFIGURATION_SELECT_ONLY",
    "DIRECTMANIPULATION_DRAG_DROP_CONFIGURATION_SELECT_DRAG",
    "DIRECTMANIPULATION_DRAG_DROP_CONFIGURATION_HOLD_DRAG",
    "IDirectManipulationDragDropBehavior",
    "DIRECTMANIPULATION_INTERACTION_TYPE",
    "DIRECTMANIPULATION_INTERACTION_BEGIN",
    "DIRECTMANIPULATION_INTERACTION_TYPE_MANIPULATION",
    "DIRECTMANIPULATION_INTERACTION_TYPE_GESTURE_TAP",
    "DIRECTMANIPULATION_INTERACTION_TYPE_GESTURE_HOLD",
    "DIRECTMANIPULATION_INTERACTION_TYPE_GESTURE_CROSS_SLIDE",
    "DIRECTMANIPULATION_INTERACTION_TYPE_GESTURE_PINCH_ZOOM",
    "DIRECTMANIPULATION_INTERACTION_END",
    "IDirectManipulationInteractionEventHandler",
    "IDirectManipulationFrameInfoProvider",
    "IDirectManipulationCompositor",
    "IDirectManipulationCompositor2",
    "IDirectManipulationUpdateHandler",
    "IDirectManipulationUpdateManager",
    "DIRECTMANIPULATION_AUTOSCROLL_CONFIGURATION",
    "DIRECTMANIPULATION_AUTOSCROLL_CONFIGURATION_STOP",
    "DIRECTMANIPULATION_AUTOSCROLL_CONFIGURATION_FORWARD",
    "DIRECTMANIPULATION_AUTOSCROLL_CONFIGURATION_REVERSE",
    "IDirectManipulationAutoScrollBehavior",
    "IDirectManipulationDeferContactService",
]
