from win32more import *
import win32more.Foundation
import win32more.Graphics.DXCore
import win32more.System.Com

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
_FACDXCORE = 2176
DXCORE_ADAPTER_ATTRIBUTE_D3D11_GRAPHICS = '8c47866b-7583-450d-f0f0-6bada895af4b'
DXCORE_ADAPTER_ATTRIBUTE_D3D12_GRAPHICS = '0c9ece4d-2f6e-4f01-8c96-e89e331b47b1'
DXCORE_ADAPTER_ATTRIBUTE_D3D12_CORE_COMPUTE = '248e2800-a793-4724-abaa-23a6de1be090'
DXCoreAdapterProperty = UInt32
DXCoreAdapterProperty_InstanceLuid = 0
DXCoreAdapterProperty_DriverVersion = 1
DXCoreAdapterProperty_DriverDescription = 2
DXCoreAdapterProperty_HardwareID = 3
DXCoreAdapterProperty_KmdModelVersion = 4
DXCoreAdapterProperty_ComputePreemptionGranularity = 5
DXCoreAdapterProperty_GraphicsPreemptionGranularity = 6
DXCoreAdapterProperty_DedicatedAdapterMemory = 7
DXCoreAdapterProperty_DedicatedSystemMemory = 8
DXCoreAdapterProperty_SharedSystemMemory = 9
DXCoreAdapterProperty_AcgCompatible = 10
DXCoreAdapterProperty_IsHardware = 11
DXCoreAdapterProperty_IsIntegrated = 12
DXCoreAdapterProperty_IsDetachable = 13
DXCoreAdapterProperty_HardwareIDParts = 14
DXCoreAdapterState = UInt32
DXCoreAdapterState_IsDriverUpdateInProgress = 0
DXCoreAdapterState_AdapterMemoryBudget = 1
DXCoreSegmentGroup = UInt32
DXCoreSegmentGroup_Local = 0
DXCoreSegmentGroup_NonLocal = 1
DXCoreNotificationType = UInt32
DXCoreNotificationType_AdapterListStale = 0
DXCoreNotificationType_AdapterNoLongerValid = 1
DXCoreNotificationType_AdapterBudgetChange = 2
DXCoreNotificationType_AdapterHardwareContentProtectionTeardown = 3
DXCoreAdapterPreference = UInt32
DXCoreAdapterPreference_Hardware = 0
DXCoreAdapterPreference_MinimumPower = 1
DXCoreAdapterPreference_HighPerformance = 2
def _define_DXCoreHardwareID_head():
    class DXCoreHardwareID(Structure):
        pass
    return DXCoreHardwareID
def _define_DXCoreHardwareID():
    DXCoreHardwareID = win32more.Graphics.DXCore.DXCoreHardwareID_head
    DXCoreHardwareID._fields_ = [
        ("vendorID", UInt32),
        ("deviceID", UInt32),
        ("subSysID", UInt32),
        ("revision", UInt32),
    ]
    return DXCoreHardwareID
def _define_DXCoreHardwareIDParts_head():
    class DXCoreHardwareIDParts(Structure):
        pass
    return DXCoreHardwareIDParts
def _define_DXCoreHardwareIDParts():
    DXCoreHardwareIDParts = win32more.Graphics.DXCore.DXCoreHardwareIDParts_head
    DXCoreHardwareIDParts._fields_ = [
        ("vendorID", UInt32),
        ("deviceID", UInt32),
        ("subSystemID", UInt32),
        ("subVendorID", UInt32),
        ("revisionID", UInt32),
    ]
    return DXCoreHardwareIDParts
def _define_DXCoreAdapterMemoryBudgetNodeSegmentGroup_head():
    class DXCoreAdapterMemoryBudgetNodeSegmentGroup(Structure):
        pass
    return DXCoreAdapterMemoryBudgetNodeSegmentGroup
def _define_DXCoreAdapterMemoryBudgetNodeSegmentGroup():
    DXCoreAdapterMemoryBudgetNodeSegmentGroup = win32more.Graphics.DXCore.DXCoreAdapterMemoryBudgetNodeSegmentGroup_head
    DXCoreAdapterMemoryBudgetNodeSegmentGroup._fields_ = [
        ("nodeIndex", UInt32),
        ("segmentGroup", win32more.Graphics.DXCore.DXCoreSegmentGroup),
    ]
    return DXCoreAdapterMemoryBudgetNodeSegmentGroup
def _define_DXCoreAdapterMemoryBudget_head():
    class DXCoreAdapterMemoryBudget(Structure):
        pass
    return DXCoreAdapterMemoryBudget
def _define_DXCoreAdapterMemoryBudget():
    DXCoreAdapterMemoryBudget = win32more.Graphics.DXCore.DXCoreAdapterMemoryBudget_head
    DXCoreAdapterMemoryBudget._fields_ = [
        ("budget", UInt64),
        ("currentUsage", UInt64),
        ("availableForReservation", UInt64),
        ("currentReservation", UInt64),
    ]
    return DXCoreAdapterMemoryBudget
def _define_PFN_DXCORE_NOTIFICATION_CALLBACK():
    return CFUNCTYPE(Void,win32more.Graphics.DXCore.DXCoreNotificationType,win32more.System.Com.IUnknown_head,c_void_p, use_last_error=False)
def _define_IDXCoreAdapter_head():
    class IDXCoreAdapter(win32more.System.Com.IUnknown_head):
        Guid = Guid('f0db4c7f-fe5a-42a2-bd62-f2a6cf6fc83e')
    return IDXCoreAdapter
def _define_IDXCoreAdapter():
    IDXCoreAdapter = win32more.Graphics.DXCore.IDXCoreAdapter_head
    IDXCoreAdapter.IsValid = COMMETHOD(WINFUNCTYPE(Boolean, use_last_error=False)(3, 'IsValid', ()))
    IDXCoreAdapter.IsAttributeSupported = COMMETHOD(WINFUNCTYPE(Boolean,POINTER(Guid), use_last_error=False)(4, 'IsAttributeSupported', ((1, 'attributeGUID'),)))
    IDXCoreAdapter.IsPropertySupported = COMMETHOD(WINFUNCTYPE(Boolean,win32more.Graphics.DXCore.DXCoreAdapterProperty, use_last_error=False)(5, 'IsPropertySupported', ((1, 'property'),)))
    IDXCoreAdapter.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DXCore.DXCoreAdapterProperty,UIntPtr,c_void_p, use_last_error=False)(6, 'GetProperty', ((1, 'property'),(1, 'bufferSize'),(1, 'propertyData'),)))
    IDXCoreAdapter.GetPropertySize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DXCore.DXCoreAdapterProperty,POINTER(UIntPtr), use_last_error=False)(7, 'GetPropertySize', ((1, 'property'),(1, 'bufferSize'),)))
    IDXCoreAdapter.IsQueryStateSupported = COMMETHOD(WINFUNCTYPE(Boolean,win32more.Graphics.DXCore.DXCoreAdapterState, use_last_error=False)(8, 'IsQueryStateSupported', ((1, 'property'),)))
    IDXCoreAdapter.QueryState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DXCore.DXCoreAdapterState,UIntPtr,c_void_p,UIntPtr,c_void_p, use_last_error=False)(9, 'QueryState', ((1, 'state'),(1, 'inputStateDetailsSize'),(1, 'inputStateDetails'),(1, 'outputBufferSize'),(1, 'outputBuffer'),)))
    IDXCoreAdapter.IsSetStateSupported = COMMETHOD(WINFUNCTYPE(Boolean,win32more.Graphics.DXCore.DXCoreAdapterState, use_last_error=False)(10, 'IsSetStateSupported', ((1, 'property'),)))
    IDXCoreAdapter.SetState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DXCore.DXCoreAdapterState,UIntPtr,c_void_p,UIntPtr,c_void_p, use_last_error=False)(11, 'SetState', ((1, 'state'),(1, 'inputStateDetailsSize'),(1, 'inputStateDetails'),(1, 'inputDataSize'),(1, 'inputData'),)))
    IDXCoreAdapter.GetFactory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(12, 'GetFactory', ((1, 'riid'),(1, 'ppvFactory'),)))
    return IDXCoreAdapter
def _define_IDXCoreAdapterList_head():
    class IDXCoreAdapterList(win32more.System.Com.IUnknown_head):
        Guid = Guid('526c7776-40e9-459b-b711-f32ad76dfc28')
    return IDXCoreAdapterList
def _define_IDXCoreAdapterList():
    IDXCoreAdapterList = win32more.Graphics.DXCore.IDXCoreAdapterList_head
    IDXCoreAdapterList.GetAdapter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(3, 'GetAdapter', ((1, 'index'),(1, 'riid'),(1, 'ppvAdapter'),)))
    IDXCoreAdapterList.GetAdapterCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(4, 'GetAdapterCount', ()))
    IDXCoreAdapterList.IsStale = COMMETHOD(WINFUNCTYPE(Boolean, use_last_error=False)(5, 'IsStale', ()))
    IDXCoreAdapterList.GetFactory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(6, 'GetFactory', ((1, 'riid'),(1, 'ppvFactory'),)))
    IDXCoreAdapterList.Sort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.DXCore.DXCoreAdapterPreference), use_last_error=False)(7, 'Sort', ((1, 'numPreferences'),(1, 'preferences'),)))
    IDXCoreAdapterList.IsAdapterPreferenceSupported = COMMETHOD(WINFUNCTYPE(Boolean,win32more.Graphics.DXCore.DXCoreAdapterPreference, use_last_error=False)(8, 'IsAdapterPreferenceSupported', ((1, 'preference'),)))
    return IDXCoreAdapterList
def _define_IDXCoreAdapterFactory_head():
    class IDXCoreAdapterFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('78ee5945-c36e-4b13-a669-005dd11c0f06')
    return IDXCoreAdapterFactory
def _define_IDXCoreAdapterFactory():
    IDXCoreAdapterFactory = win32more.Graphics.DXCore.IDXCoreAdapterFactory_head
    IDXCoreAdapterFactory.CreateAdapterList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(Guid),POINTER(c_void_p), use_last_error=False)(3, 'CreateAdapterList', ((1, 'numAttributes'),(1, 'filterAttributes'),(1, 'riid'),(1, 'ppvAdapterList'),)))
    IDXCoreAdapterFactory.GetAdapterByLuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.LUID_head),POINTER(Guid),POINTER(c_void_p), use_last_error=False)(4, 'GetAdapterByLuid', ((1, 'adapterLUID'),(1, 'riid'),(1, 'ppvAdapter'),)))
    IDXCoreAdapterFactory.IsNotificationTypeSupported = COMMETHOD(WINFUNCTYPE(Boolean,win32more.Graphics.DXCore.DXCoreNotificationType, use_last_error=False)(5, 'IsNotificationTypeSupported', ((1, 'notificationType'),)))
    IDXCoreAdapterFactory.RegisterEventNotification = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Graphics.DXCore.DXCoreNotificationType,win32more.Graphics.DXCore.PFN_DXCORE_NOTIFICATION_CALLBACK,c_void_p,POINTER(UInt32), use_last_error=False)(6, 'RegisterEventNotification', ((1, 'dxCoreObject'),(1, 'notificationType'),(1, 'callbackFunction'),(1, 'callbackContext'),(1, 'eventCookie'),)))
    IDXCoreAdapterFactory.UnregisterEventNotification = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(7, 'UnregisterEventNotification', ((1, 'eventCookie'),)))
    return IDXCoreAdapterFactory
def _define_DXCoreCreateAdapterFactory():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("DXCoreCreateAdapterFactory", windll["DXCORE"]), ((1, 'riid'),(1, 'ppvFactory'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "_FACDXCORE",
    "DXCORE_ADAPTER_ATTRIBUTE_D3D11_GRAPHICS",
    "DXCORE_ADAPTER_ATTRIBUTE_D3D12_GRAPHICS",
    "DXCORE_ADAPTER_ATTRIBUTE_D3D12_CORE_COMPUTE",
    "DXCoreAdapterProperty",
    "DXCoreAdapterProperty_InstanceLuid",
    "DXCoreAdapterProperty_DriverVersion",
    "DXCoreAdapterProperty_DriverDescription",
    "DXCoreAdapterProperty_HardwareID",
    "DXCoreAdapterProperty_KmdModelVersion",
    "DXCoreAdapterProperty_ComputePreemptionGranularity",
    "DXCoreAdapterProperty_GraphicsPreemptionGranularity",
    "DXCoreAdapterProperty_DedicatedAdapterMemory",
    "DXCoreAdapterProperty_DedicatedSystemMemory",
    "DXCoreAdapterProperty_SharedSystemMemory",
    "DXCoreAdapterProperty_AcgCompatible",
    "DXCoreAdapterProperty_IsHardware",
    "DXCoreAdapterProperty_IsIntegrated",
    "DXCoreAdapterProperty_IsDetachable",
    "DXCoreAdapterProperty_HardwareIDParts",
    "DXCoreAdapterState",
    "DXCoreAdapterState_IsDriverUpdateInProgress",
    "DXCoreAdapterState_AdapterMemoryBudget",
    "DXCoreSegmentGroup",
    "DXCoreSegmentGroup_Local",
    "DXCoreSegmentGroup_NonLocal",
    "DXCoreNotificationType",
    "DXCoreNotificationType_AdapterListStale",
    "DXCoreNotificationType_AdapterNoLongerValid",
    "DXCoreNotificationType_AdapterBudgetChange",
    "DXCoreNotificationType_AdapterHardwareContentProtectionTeardown",
    "DXCoreAdapterPreference",
    "DXCoreAdapterPreference_Hardware",
    "DXCoreAdapterPreference_MinimumPower",
    "DXCoreAdapterPreference_HighPerformance",
    "DXCoreHardwareID",
    "DXCoreHardwareIDParts",
    "DXCoreAdapterMemoryBudgetNodeSegmentGroup",
    "DXCoreAdapterMemoryBudget",
    "PFN_DXCORE_NOTIFICATION_CALLBACK",
    "IDXCoreAdapter",
    "IDXCoreAdapterList",
    "IDXCoreAdapterFactory",
    "DXCoreCreateAdapterFactory",
]
