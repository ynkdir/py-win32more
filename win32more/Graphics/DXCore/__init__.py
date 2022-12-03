from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.DXCore
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
_FACDXCORE = 2176
def _define_DXCORE_ADAPTER_ATTRIBUTE_D3D11_GRAPHICS():
    return Guid('8c47866b-7583-450d-f0-f0-6b-ad-a8-95-af-4b')
def _define_DXCORE_ADAPTER_ATTRIBUTE_D3D12_GRAPHICS():
    return Guid('0c9ece4d-2f6e-4f01-8c-96-e8-9e-33-1b-47-b1')
def _define_DXCORE_ADAPTER_ATTRIBUTE_D3D12_CORE_COMPUTE():
    return Guid('248e2800-a793-4724-ab-aa-23-a6-de-1b-e0-90')
def _define_DXCoreCreateAdapterFactory():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(('DXCoreCreateAdapterFactory', windll['DXCORE.dll']), ((1, 'riid'),(1, 'ppvFactory'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DXCoreAdapterMemoryBudget_head():
    class DXCoreAdapterMemoryBudget(Structure):
        pass
    return DXCoreAdapterMemoryBudget
def _define_DXCoreAdapterMemoryBudget():
    DXCoreAdapterMemoryBudget = win32more.Graphics.DXCore.DXCoreAdapterMemoryBudget_head
    DXCoreAdapterMemoryBudget._fields_ = [
        ('budget', UInt64),
        ('currentUsage', UInt64),
        ('availableForReservation', UInt64),
        ('currentReservation', UInt64),
    ]
    return DXCoreAdapterMemoryBudget
def _define_DXCoreAdapterMemoryBudgetNodeSegmentGroup_head():
    class DXCoreAdapterMemoryBudgetNodeSegmentGroup(Structure):
        pass
    return DXCoreAdapterMemoryBudgetNodeSegmentGroup
def _define_DXCoreAdapterMemoryBudgetNodeSegmentGroup():
    DXCoreAdapterMemoryBudgetNodeSegmentGroup = win32more.Graphics.DXCore.DXCoreAdapterMemoryBudgetNodeSegmentGroup_head
    DXCoreAdapterMemoryBudgetNodeSegmentGroup._fields_ = [
        ('nodeIndex', UInt32),
        ('segmentGroup', win32more.Graphics.DXCore.DXCoreSegmentGroup),
    ]
    return DXCoreAdapterMemoryBudgetNodeSegmentGroup
DXCoreAdapterPreference = UInt32
DXCoreAdapterPreference_Hardware = 0
DXCoreAdapterPreference_MinimumPower = 1
DXCoreAdapterPreference_HighPerformance = 2
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
def _define_DXCoreHardwareID_head():
    class DXCoreHardwareID(Structure):
        pass
    return DXCoreHardwareID
def _define_DXCoreHardwareID():
    DXCoreHardwareID = win32more.Graphics.DXCore.DXCoreHardwareID_head
    DXCoreHardwareID._fields_ = [
        ('vendorID', UInt32),
        ('deviceID', UInt32),
        ('subSysID', UInt32),
        ('revision', UInt32),
    ]
    return DXCoreHardwareID
def _define_DXCoreHardwareIDParts_head():
    class DXCoreHardwareIDParts(Structure):
        pass
    return DXCoreHardwareIDParts
def _define_DXCoreHardwareIDParts():
    DXCoreHardwareIDParts = win32more.Graphics.DXCore.DXCoreHardwareIDParts_head
    DXCoreHardwareIDParts._fields_ = [
        ('vendorID', UInt32),
        ('deviceID', UInt32),
        ('subSystemID', UInt32),
        ('subVendorID', UInt32),
        ('revisionID', UInt32),
    ]
    return DXCoreHardwareIDParts
DXCoreNotificationType = UInt32
DXCoreNotificationType_AdapterListStale = 0
DXCoreNotificationType_AdapterNoLongerValid = 1
DXCoreNotificationType_AdapterBudgetChange = 2
DXCoreNotificationType_AdapterHardwareContentProtectionTeardown = 3
DXCoreSegmentGroup = UInt32
DXCoreSegmentGroup_Local = 0
DXCoreSegmentGroup_NonLocal = 1
def _define_IDXCoreAdapter_head():
    class IDXCoreAdapter(win32more.System.Com.IUnknown_head):
        Guid = Guid('f0db4c7f-fe5a-42a2-bd-62-f2-a6-cf-6f-c8-3e')
    return IDXCoreAdapter
def _define_IDXCoreAdapter():
    IDXCoreAdapter = win32more.Graphics.DXCore.IDXCoreAdapter_head
    IDXCoreAdapter.IsValid = COMMETHOD(WINFUNCTYPE(Boolean,)(3, 'IsValid', ()))
    IDXCoreAdapter.IsAttributeSupported = COMMETHOD(WINFUNCTYPE(Boolean,POINTER(Guid))(4, 'IsAttributeSupported', ((1, 'attributeGUID'),)))
    IDXCoreAdapter.IsPropertySupported = COMMETHOD(WINFUNCTYPE(Boolean,win32more.Graphics.DXCore.DXCoreAdapterProperty)(5, 'IsPropertySupported', ((1, 'property'),)))
    IDXCoreAdapter.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DXCore.DXCoreAdapterProperty,UIntPtr,c_void_p)(6, 'GetProperty', ((1, 'property'),(1, 'bufferSize'),(1, 'propertyData'),)))
    IDXCoreAdapter.GetPropertySize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DXCore.DXCoreAdapterProperty,POINTER(UIntPtr))(7, 'GetPropertySize', ((1, 'property'),(1, 'bufferSize'),)))
    IDXCoreAdapter.IsQueryStateSupported = COMMETHOD(WINFUNCTYPE(Boolean,win32more.Graphics.DXCore.DXCoreAdapterState)(8, 'IsQueryStateSupported', ((1, 'property'),)))
    IDXCoreAdapter.QueryState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DXCore.DXCoreAdapterState,UIntPtr,c_void_p,UIntPtr,c_void_p)(9, 'QueryState', ((1, 'state'),(1, 'inputStateDetailsSize'),(1, 'inputStateDetails'),(1, 'outputBufferSize'),(1, 'outputBuffer'),)))
    IDXCoreAdapter.IsSetStateSupported = COMMETHOD(WINFUNCTYPE(Boolean,win32more.Graphics.DXCore.DXCoreAdapterState)(10, 'IsSetStateSupported', ((1, 'property'),)))
    IDXCoreAdapter.SetState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DXCore.DXCoreAdapterState,UIntPtr,c_void_p,UIntPtr,c_void_p)(11, 'SetState', ((1, 'state'),(1, 'inputStateDetailsSize'),(1, 'inputStateDetails'),(1, 'inputDataSize'),(1, 'inputData'),)))
    IDXCoreAdapter.GetFactory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(12, 'GetFactory', ((1, 'riid'),(1, 'ppvFactory'),)))
    win32more.System.Com.IUnknown
    return IDXCoreAdapter
def _define_IDXCoreAdapterFactory_head():
    class IDXCoreAdapterFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('78ee5945-c36e-4b13-a6-69-00-5d-d1-1c-0f-06')
    return IDXCoreAdapterFactory
def _define_IDXCoreAdapterFactory():
    IDXCoreAdapterFactory = win32more.Graphics.DXCore.IDXCoreAdapterFactory_head
    IDXCoreAdapterFactory.CreateAdapterList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(Guid),POINTER(c_void_p))(3, 'CreateAdapterList', ((1, 'numAttributes'),(1, 'filterAttributes'),(1, 'riid'),(1, 'ppvAdapterList'),)))
    IDXCoreAdapterFactory.GetAdapterByLuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.LUID_head),POINTER(Guid),POINTER(c_void_p))(4, 'GetAdapterByLuid', ((1, 'adapterLUID'),(1, 'riid'),(1, 'ppvAdapter'),)))
    IDXCoreAdapterFactory.IsNotificationTypeSupported = COMMETHOD(WINFUNCTYPE(Boolean,win32more.Graphics.DXCore.DXCoreNotificationType)(5, 'IsNotificationTypeSupported', ((1, 'notificationType'),)))
    IDXCoreAdapterFactory.RegisterEventNotification = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Graphics.DXCore.DXCoreNotificationType,win32more.Graphics.DXCore.PFN_DXCORE_NOTIFICATION_CALLBACK,c_void_p,POINTER(UInt32))(6, 'RegisterEventNotification', ((1, 'dxCoreObject'),(1, 'notificationType'),(1, 'callbackFunction'),(1, 'callbackContext'),(1, 'eventCookie'),)))
    IDXCoreAdapterFactory.UnregisterEventNotification = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(7, 'UnregisterEventNotification', ((1, 'eventCookie'),)))
    win32more.System.Com.IUnknown
    return IDXCoreAdapterFactory
def _define_IDXCoreAdapterList_head():
    class IDXCoreAdapterList(win32more.System.Com.IUnknown_head):
        Guid = Guid('526c7776-40e9-459b-b7-11-f3-2a-d7-6d-fc-28')
    return IDXCoreAdapterList
def _define_IDXCoreAdapterList():
    IDXCoreAdapterList = win32more.Graphics.DXCore.IDXCoreAdapterList_head
    IDXCoreAdapterList.GetAdapter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(c_void_p))(3, 'GetAdapter', ((1, 'index'),(1, 'riid'),(1, 'ppvAdapter'),)))
    IDXCoreAdapterList.GetAdapterCount = COMMETHOD(WINFUNCTYPE(UInt32,)(4, 'GetAdapterCount', ()))
    IDXCoreAdapterList.IsStale = COMMETHOD(WINFUNCTYPE(Boolean,)(5, 'IsStale', ()))
    IDXCoreAdapterList.GetFactory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(6, 'GetFactory', ((1, 'riid'),(1, 'ppvFactory'),)))
    IDXCoreAdapterList.Sort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.DXCore.DXCoreAdapterPreference))(7, 'Sort', ((1, 'numPreferences'),(1, 'preferences'),)))
    IDXCoreAdapterList.IsAdapterPreferenceSupported = COMMETHOD(WINFUNCTYPE(Boolean,win32more.Graphics.DXCore.DXCoreAdapterPreference)(8, 'IsAdapterPreferenceSupported', ((1, 'preference'),)))
    win32more.System.Com.IUnknown
    return IDXCoreAdapterList
def _define_PFN_DXCORE_NOTIFICATION_CALLBACK():
    return WINFUNCTYPE(Void,win32more.Graphics.DXCore.DXCoreNotificationType,win32more.System.Com.IUnknown_head,c_void_p)
__all__ = [
    "DXCORE_ADAPTER_ATTRIBUTE_D3D11_GRAPHICS",
    "DXCORE_ADAPTER_ATTRIBUTE_D3D12_CORE_COMPUTE",
    "DXCORE_ADAPTER_ATTRIBUTE_D3D12_GRAPHICS",
    "DXCoreAdapterMemoryBudget",
    "DXCoreAdapterMemoryBudgetNodeSegmentGroup",
    "DXCoreAdapterPreference",
    "DXCoreAdapterPreference_Hardware",
    "DXCoreAdapterPreference_HighPerformance",
    "DXCoreAdapterPreference_MinimumPower",
    "DXCoreAdapterProperty",
    "DXCoreAdapterProperty_AcgCompatible",
    "DXCoreAdapterProperty_ComputePreemptionGranularity",
    "DXCoreAdapterProperty_DedicatedAdapterMemory",
    "DXCoreAdapterProperty_DedicatedSystemMemory",
    "DXCoreAdapterProperty_DriverDescription",
    "DXCoreAdapterProperty_DriverVersion",
    "DXCoreAdapterProperty_GraphicsPreemptionGranularity",
    "DXCoreAdapterProperty_HardwareID",
    "DXCoreAdapterProperty_HardwareIDParts",
    "DXCoreAdapterProperty_InstanceLuid",
    "DXCoreAdapterProperty_IsDetachable",
    "DXCoreAdapterProperty_IsHardware",
    "DXCoreAdapterProperty_IsIntegrated",
    "DXCoreAdapterProperty_KmdModelVersion",
    "DXCoreAdapterProperty_SharedSystemMemory",
    "DXCoreAdapterState",
    "DXCoreAdapterState_AdapterMemoryBudget",
    "DXCoreAdapterState_IsDriverUpdateInProgress",
    "DXCoreCreateAdapterFactory",
    "DXCoreHardwareID",
    "DXCoreHardwareIDParts",
    "DXCoreNotificationType",
    "DXCoreNotificationType_AdapterBudgetChange",
    "DXCoreNotificationType_AdapterHardwareContentProtectionTeardown",
    "DXCoreNotificationType_AdapterListStale",
    "DXCoreNotificationType_AdapterNoLongerValid",
    "DXCoreSegmentGroup",
    "DXCoreSegmentGroup_Local",
    "DXCoreSegmentGroup_NonLocal",
    "IDXCoreAdapter",
    "IDXCoreAdapterFactory",
    "IDXCoreAdapterList",
    "PFN_DXCORE_NOTIFICATION_CALLBACK",
    "_FACDXCORE",
]
