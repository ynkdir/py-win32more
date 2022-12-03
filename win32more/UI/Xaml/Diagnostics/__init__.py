from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Dxgi.Common
import win32more.System.Com
import win32more.System.WinRT
import win32more.UI.Xaml.Diagnostics
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
E_UNKNOWNTYPE = -2144665560
def _define_InitializeXamlDiagnostic():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Guid)(('InitializeXamlDiagnostic', windll['Windows.UI.Xaml.dll']), ((1, 'endPointName'),(1, 'pid'),(1, 'wszDllXamlDiagnostics'),(1, 'wszTAPDllName'),(1, 'tapClsid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitializeXamlDiagnosticsEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Guid,win32more.Foundation.PWSTR)(('InitializeXamlDiagnosticsEx', windll['Windows.UI.Xaml.dll']), ((1, 'endPointName'),(1, 'pid'),(1, 'wszDllXamlDiagnostics'),(1, 'wszTAPDllName'),(1, 'tapClsid'),(1, 'wszInitializationData'),))
    except (FileNotFoundError, AttributeError):
        return None
BaseValueSource = Int32
BaseValueSource_BaseValueSourceUnknown = 0
BaseValueSource_BaseValueSourceDefault = 1
BaseValueSource_BaseValueSourceBuiltInStyle = 2
BaseValueSource_BaseValueSourceStyle = 3
BaseValueSource_BaseValueSourceLocal = 4
BaseValueSource_Inherited = 5
BaseValueSource_DefaultStyleTrigger = 6
BaseValueSource_TemplateTrigger = 7
BaseValueSource_StyleTrigger = 8
BaseValueSource_ImplicitStyleReference = 9
BaseValueSource_ParentTemplate = 10
BaseValueSource_ParentTemplateTrigger = 11
BaseValueSource_Animation = 12
BaseValueSource_Coercion = 13
BaseValueSource_BaseValueSourceVisualState = 14
def _define_BitmapDescription_head():
    class BitmapDescription(Structure):
        pass
    return BitmapDescription
def _define_BitmapDescription():
    BitmapDescription = win32more.UI.Xaml.Diagnostics.BitmapDescription_head
    BitmapDescription._fields_ = [
        ('Width', UInt32),
        ('Height', UInt32),
        ('Format', win32more.Graphics.Dxgi.Common.DXGI_FORMAT),
        ('AlphaMode', win32more.Graphics.Dxgi.Common.DXGI_ALPHA_MODE),
    ]
    return BitmapDescription
def _define_CollectionElementValue_head():
    class CollectionElementValue(Structure):
        pass
    return CollectionElementValue
def _define_CollectionElementValue():
    CollectionElementValue = win32more.UI.Xaml.Diagnostics.CollectionElementValue_head
    CollectionElementValue._fields_ = [
        ('Index', UInt32),
        ('ValueType', win32more.Foundation.BSTR),
        ('Value', win32more.Foundation.BSTR),
        ('MetadataBits', Int64),
    ]
    return CollectionElementValue
def _define_EnumType_head():
    class EnumType(Structure):
        pass
    return EnumType
def _define_EnumType():
    EnumType = win32more.UI.Xaml.Diagnostics.EnumType_head
    EnumType._fields_ = [
        ('Name', win32more.Foundation.BSTR),
        ('ValueInts', POINTER(win32more.System.Com.SAFEARRAY_head)),
        ('ValueStrings', POINTER(win32more.System.Com.SAFEARRAY_head)),
    ]
    return EnumType
def _define_IBitmapData_head():
    class IBitmapData(win32more.System.Com.IUnknown_head):
        Guid = Guid('d1a34ef2-cad8-4635-a3-d2-fc-da-8d-3f-3c-af')
    return IBitmapData
def _define_IBitmapData():
    IBitmapData = win32more.UI.Xaml.Diagnostics.IBitmapData_head
    IBitmapData.CopyBytesTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,c_char_p_no,POINTER(UInt32))(3, 'CopyBytesTo', ((1, 'sourceOffsetInBytes'),(1, 'maxBytesToCopy'),(1, 'pvBytes'),(1, 'numberOfBytesCopied'),)))
    IBitmapData.GetStride = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(4, 'GetStride', ((1, 'pStride'),)))
    IBitmapData.GetBitmapDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Xaml.Diagnostics.BitmapDescription_head))(5, 'GetBitmapDescription', ((1, 'pBitmapDescription'),)))
    IBitmapData.GetSourceBitmapDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Xaml.Diagnostics.BitmapDescription_head))(6, 'GetSourceBitmapDescription', ((1, 'pBitmapDescription'),)))
    win32more.System.Com.IUnknown
    return IBitmapData
def _define_IVisualTreeService_head():
    class IVisualTreeService(win32more.System.Com.IUnknown_head):
        Guid = Guid('a593b11a-d17f-48bb-8f-66-83-91-07-31-c8-a5')
    return IVisualTreeService
def _define_IVisualTreeService():
    IVisualTreeService = win32more.UI.Xaml.Diagnostics.IVisualTreeService_head
    IVisualTreeService.AdviseVisualTreeChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Xaml.Diagnostics.IVisualTreeServiceCallback_head)(3, 'AdviseVisualTreeChange', ((1, 'pCallback'),)))
    IVisualTreeService.UnadviseVisualTreeChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Xaml.Diagnostics.IVisualTreeServiceCallback_head)(4, 'UnadviseVisualTreeChange', ((1, 'pCallback'),)))
    IVisualTreeService.GetEnums = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(win32more.UI.Xaml.Diagnostics.EnumType_head)))(5, 'GetEnums', ((1, 'pCount'),(1, 'ppEnums'),)))
    IVisualTreeService.CreateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(UInt64))(6, 'CreateInstance', ((1, 'typeName'),(1, 'value'),(1, 'pInstanceHandle'),)))
    IVisualTreeService.GetPropertyValuesChain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(UInt32),POINTER(POINTER(win32more.UI.Xaml.Diagnostics.PropertyChainSource_head)),POINTER(UInt32),POINTER(POINTER(win32more.UI.Xaml.Diagnostics.PropertyChainValue_head)))(7, 'GetPropertyValuesChain', ((1, 'instanceHandle'),(1, 'pSourceCount'),(1, 'ppPropertySources'),(1, 'pPropertyCount'),(1, 'ppPropertyValues'),)))
    IVisualTreeService.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,UInt64,UInt32)(8, 'SetProperty', ((1, 'instanceHandle'),(1, 'value'),(1, 'propertyIndex'),)))
    IVisualTreeService.ClearProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,UInt32)(9, 'ClearProperty', ((1, 'instanceHandle'),(1, 'propertyIndex'),)))
    IVisualTreeService.GetCollectionCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(UInt32))(10, 'GetCollectionCount', ((1, 'instanceHandle'),(1, 'pCollectionSize'),)))
    IVisualTreeService.GetCollectionElements = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,UInt32,POINTER(UInt32),POINTER(POINTER(win32more.UI.Xaml.Diagnostics.CollectionElementValue_head)))(11, 'GetCollectionElements', ((1, 'instanceHandle'),(1, 'startIndex'),(1, 'pElementCount'),(1, 'ppElementValues'),)))
    IVisualTreeService.AddChild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,UInt64,UInt32)(12, 'AddChild', ((1, 'parent'),(1, 'child'),(1, 'index'),)))
    IVisualTreeService.RemoveChild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,UInt32)(13, 'RemoveChild', ((1, 'parent'),(1, 'index'),)))
    IVisualTreeService.ClearChildren = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64)(14, 'ClearChildren', ((1, 'parent'),)))
    win32more.System.Com.IUnknown
    return IVisualTreeService
def _define_IVisualTreeService2_head():
    class IVisualTreeService2(win32more.UI.Xaml.Diagnostics.IVisualTreeService_head):
        Guid = Guid('130f5136-ec43-4f61-89-c7-98-01-a3-6d-2e-95')
    return IVisualTreeService2
def _define_IVisualTreeService2():
    IVisualTreeService2 = win32more.UI.Xaml.Diagnostics.IVisualTreeService2_head
    IVisualTreeService2.GetPropertyIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,win32more.Foundation.PWSTR,POINTER(UInt32))(15, 'GetPropertyIndex', ((1, 'object'),(1, 'propertyName'),(1, 'pPropertyIndex'),)))
    IVisualTreeService2.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,UInt32,POINTER(UInt64))(16, 'GetProperty', ((1, 'object'),(1, 'propertyIndex'),(1, 'pValue'),)))
    IVisualTreeService2.ReplaceResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,UInt64,UInt64)(17, 'ReplaceResource', ((1, 'resourceDictionary'),(1, 'key'),(1, 'newValue'),)))
    IVisualTreeService2.RenderTargetBitmap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,win32more.UI.Xaml.Diagnostics.RenderTargetBitmapOptions,UInt32,UInt32,POINTER(win32more.UI.Xaml.Diagnostics.IBitmapData_head))(18, 'RenderTargetBitmap', ((1, 'handle'),(1, 'options'),(1, 'maxPixelWidth'),(1, 'maxPixelHeight'),(1, 'ppBitmapData'),)))
    win32more.UI.Xaml.Diagnostics.IVisualTreeService
    return IVisualTreeService2
def _define_IVisualTreeService3_head():
    class IVisualTreeService3(win32more.UI.Xaml.Diagnostics.IVisualTreeService2_head):
        Guid = Guid('0e79c6e0-85a0-4be8-b4-1a-65-5c-f1-fd-19-bd')
    return IVisualTreeService3
def _define_IVisualTreeService3():
    IVisualTreeService3 = win32more.UI.Xaml.Diagnostics.IVisualTreeService3_head
    IVisualTreeService3.ResolveResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,win32more.Foundation.PWSTR,win32more.UI.Xaml.Diagnostics.ResourceType,UInt32)(19, 'ResolveResource', ((1, 'resourceContext'),(1, 'resourceName'),(1, 'resourceType'),(1, 'propertyIndex'),)))
    IVisualTreeService3.GetDictionaryItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,POINTER(UInt64))(20, 'GetDictionaryItem', ((1, 'dictionaryHandle'),(1, 'resourceName'),(1, 'resourceIsImplicitStyle'),(1, 'resourceHandle'),)))
    IVisualTreeService3.AddDictionaryItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,UInt64,UInt64)(21, 'AddDictionaryItem', ((1, 'dictionaryHandle'),(1, 'resourceKey'),(1, 'resourceHandle'),)))
    IVisualTreeService3.RemoveDictionaryItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,UInt64)(22, 'RemoveDictionaryItem', ((1, 'dictionaryHandle'),(1, 'resourceKey'),)))
    win32more.UI.Xaml.Diagnostics.IVisualTreeService2
    return IVisualTreeService3
def _define_IVisualTreeServiceCallback_head():
    class IVisualTreeServiceCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa7a8931-80e4-4fec-8f-3b-55-3f-87-b4-96-6e')
    return IVisualTreeServiceCallback
def _define_IVisualTreeServiceCallback():
    IVisualTreeServiceCallback = win32more.UI.Xaml.Diagnostics.IVisualTreeServiceCallback_head
    IVisualTreeServiceCallback.OnVisualTreeChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Xaml.Diagnostics.ParentChildRelation,win32more.UI.Xaml.Diagnostics.VisualElement,win32more.UI.Xaml.Diagnostics.VisualMutationType)(3, 'OnVisualTreeChange', ((1, 'relation'),(1, 'element'),(1, 'mutationType'),)))
    win32more.System.Com.IUnknown
    return IVisualTreeServiceCallback
def _define_IVisualTreeServiceCallback2_head():
    class IVisualTreeServiceCallback2(win32more.UI.Xaml.Diagnostics.IVisualTreeServiceCallback_head):
        Guid = Guid('bad9eb88-ae77-4397-b9-48-5f-a2-db-0a-19-ea')
    return IVisualTreeServiceCallback2
def _define_IVisualTreeServiceCallback2():
    IVisualTreeServiceCallback2 = win32more.UI.Xaml.Diagnostics.IVisualTreeServiceCallback2_head
    IVisualTreeServiceCallback2.OnElementStateChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,win32more.UI.Xaml.Diagnostics.VisualElementState,win32more.Foundation.PWSTR)(4, 'OnElementStateChanged', ((1, 'element'),(1, 'elementState'),(1, 'context'),)))
    win32more.UI.Xaml.Diagnostics.IVisualTreeServiceCallback
    return IVisualTreeServiceCallback2
def _define_IXamlDiagnostics_head():
    class IXamlDiagnostics(win32more.System.Com.IUnknown_head):
        Guid = Guid('18c9e2b6-3f43-4116-9f-2b-ff-93-5d-77-70-d2')
    return IXamlDiagnostics
def _define_IXamlDiagnostics():
    IXamlDiagnostics = win32more.UI.Xaml.Diagnostics.IXamlDiagnostics_head
    IXamlDiagnostics.GetDispatcher = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WinRT.IInspectable_head))(3, 'GetDispatcher', ((1, 'ppDispatcher'),)))
    IXamlDiagnostics.GetUiLayer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WinRT.IInspectable_head))(4, 'GetUiLayer', ((1, 'ppLayer'),)))
    IXamlDiagnostics.GetApplication = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WinRT.IInspectable_head))(5, 'GetApplication', ((1, 'ppApplication'),)))
    IXamlDiagnostics.GetIInspectableFromHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(win32more.System.WinRT.IInspectable_head))(6, 'GetIInspectableFromHandle', ((1, 'instanceHandle'),(1, 'ppInstance'),)))
    IXamlDiagnostics.GetHandleFromIInspectable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,POINTER(UInt64))(7, 'GetHandleFromIInspectable', ((1, 'pInstance'),(1, 'pHandle'),)))
    IXamlDiagnostics.HitTest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.RECT,POINTER(UInt32),POINTER(POINTER(UInt64)))(8, 'HitTest', ((1, 'rect'),(1, 'pCount'),(1, 'ppInstanceHandles'),)))
    IXamlDiagnostics.RegisterInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,POINTER(UInt64))(9, 'RegisterInstance', ((1, 'pInstance'),(1, 'pInstanceHandle'),)))
    IXamlDiagnostics.GetInitializationData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'GetInitializationData', ((1, 'pInitializationData'),)))
    win32more.System.Com.IUnknown
    return IXamlDiagnostics
MetadataBit = Int32
MetadataBit_None = 0
MetadataBit_IsValueHandle = 1
MetadataBit_IsPropertyReadOnly = 2
MetadataBit_IsValueCollection = 4
MetadataBit_IsValueCollectionReadOnly = 8
MetadataBit_IsValueBindingExpression = 16
MetadataBit_IsValueNull = 32
MetadataBit_IsValueHandleAndEvaluatedValue = 64
def _define_ParentChildRelation_head():
    class ParentChildRelation(Structure):
        pass
    return ParentChildRelation
def _define_ParentChildRelation():
    ParentChildRelation = win32more.UI.Xaml.Diagnostics.ParentChildRelation_head
    ParentChildRelation._fields_ = [
        ('Parent', UInt64),
        ('Child', UInt64),
        ('ChildIndex', UInt32),
    ]
    return ParentChildRelation
def _define_PropertyChainSource_head():
    class PropertyChainSource(Structure):
        pass
    return PropertyChainSource
def _define_PropertyChainSource():
    PropertyChainSource = win32more.UI.Xaml.Diagnostics.PropertyChainSource_head
    PropertyChainSource._fields_ = [
        ('Handle', UInt64),
        ('TargetType', win32more.Foundation.BSTR),
        ('Name', win32more.Foundation.BSTR),
        ('Source', win32more.UI.Xaml.Diagnostics.BaseValueSource),
        ('SrcInfo', win32more.UI.Xaml.Diagnostics.SourceInfo),
    ]
    return PropertyChainSource
def _define_PropertyChainValue_head():
    class PropertyChainValue(Structure):
        pass
    return PropertyChainValue
def _define_PropertyChainValue():
    PropertyChainValue = win32more.UI.Xaml.Diagnostics.PropertyChainValue_head
    PropertyChainValue._fields_ = [
        ('Index', UInt32),
        ('Type', win32more.Foundation.BSTR),
        ('DeclaringType', win32more.Foundation.BSTR),
        ('ValueType', win32more.Foundation.BSTR),
        ('ItemType', win32more.Foundation.BSTR),
        ('Value', win32more.Foundation.BSTR),
        ('Overridden', win32more.Foundation.BOOL),
        ('MetadataBits', Int64),
        ('PropertyName', win32more.Foundation.BSTR),
        ('PropertyChainIndex', UInt32),
    ]
    return PropertyChainValue
RenderTargetBitmapOptions = Int32
RenderTargetBitmapOptions_RenderTarget = 0
RenderTargetBitmapOptions_RenderTargetAndChildren = 1
ResourceType = Int32
ResourceType_ResourceTypeStatic = 0
ResourceType_ResourceTypeTheme = 1
def _define_SourceInfo_head():
    class SourceInfo(Structure):
        pass
    return SourceInfo
def _define_SourceInfo():
    SourceInfo = win32more.UI.Xaml.Diagnostics.SourceInfo_head
    SourceInfo._fields_ = [
        ('FileName', win32more.Foundation.BSTR),
        ('LineNumber', UInt32),
        ('ColumnNumber', UInt32),
        ('CharPosition', UInt32),
        ('Hash', win32more.Foundation.BSTR),
    ]
    return SourceInfo
def _define_VisualElement_head():
    class VisualElement(Structure):
        pass
    return VisualElement
def _define_VisualElement():
    VisualElement = win32more.UI.Xaml.Diagnostics.VisualElement_head
    VisualElement._fields_ = [
        ('Handle', UInt64),
        ('SrcInfo', win32more.UI.Xaml.Diagnostics.SourceInfo),
        ('Type', win32more.Foundation.BSTR),
        ('Name', win32more.Foundation.BSTR),
        ('NumChildren', UInt32),
    ]
    return VisualElement
VisualElementState = Int32
VisualElementState_ErrorResolved = 0
VisualElementState_ErrorResourceNotFound = 1
VisualElementState_ErrorInvalidResource = 2
VisualMutationType = Int32
VisualMutationType_Add = 0
VisualMutationType_Remove = 1
__all__ = [
    "BaseValueSource",
    "BaseValueSource_Animation",
    "BaseValueSource_BaseValueSourceBuiltInStyle",
    "BaseValueSource_BaseValueSourceDefault",
    "BaseValueSource_BaseValueSourceLocal",
    "BaseValueSource_BaseValueSourceStyle",
    "BaseValueSource_BaseValueSourceUnknown",
    "BaseValueSource_BaseValueSourceVisualState",
    "BaseValueSource_Coercion",
    "BaseValueSource_DefaultStyleTrigger",
    "BaseValueSource_ImplicitStyleReference",
    "BaseValueSource_Inherited",
    "BaseValueSource_ParentTemplate",
    "BaseValueSource_ParentTemplateTrigger",
    "BaseValueSource_StyleTrigger",
    "BaseValueSource_TemplateTrigger",
    "BitmapDescription",
    "CollectionElementValue",
    "E_UNKNOWNTYPE",
    "EnumType",
    "IBitmapData",
    "IVisualTreeService",
    "IVisualTreeService2",
    "IVisualTreeService3",
    "IVisualTreeServiceCallback",
    "IVisualTreeServiceCallback2",
    "IXamlDiagnostics",
    "InitializeXamlDiagnostic",
    "InitializeXamlDiagnosticsEx",
    "MetadataBit",
    "MetadataBit_IsPropertyReadOnly",
    "MetadataBit_IsValueBindingExpression",
    "MetadataBit_IsValueCollection",
    "MetadataBit_IsValueCollectionReadOnly",
    "MetadataBit_IsValueHandle",
    "MetadataBit_IsValueHandleAndEvaluatedValue",
    "MetadataBit_IsValueNull",
    "MetadataBit_None",
    "ParentChildRelation",
    "PropertyChainSource",
    "PropertyChainValue",
    "RenderTargetBitmapOptions",
    "RenderTargetBitmapOptions_RenderTarget",
    "RenderTargetBitmapOptions_RenderTargetAndChildren",
    "ResourceType",
    "ResourceType_ResourceTypeStatic",
    "ResourceType_ResourceTypeTheme",
    "SourceInfo",
    "VisualElement",
    "VisualElementState",
    "VisualElementState_ErrorInvalidResource",
    "VisualElementState_ErrorResolved",
    "VisualElementState_ErrorResourceNotFound",
    "VisualMutationType",
    "VisualMutationType_Add",
    "VisualMutationType_Remove",
]
