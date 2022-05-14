from win32more import *
import win32more.System.Com.Events
import win32more.Foundation
import win32more.System.Com

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.System.Com.Events, name, eval(f"_define_{name}()"))
    return getattr(win32more.System.Com.Events, name)
CEventSystem = Guid('4e14fba2-2e22-11d1-9964-00c04fbbb345')
CEventPublisher = Guid('ab944620-79c6-11d1-88f9-0080c7d771bf')
CEventClass = Guid('cdbec9c0-7a68-11d1-88f9-0080c7d771bf')
CEventSubscription = Guid('7542e960-79c7-11d1-88f9-0080c7d771bf')
EventObjectChange = Guid('d0565000-9df4-11d1-a281-00c04fca0aa7')
EventObjectChange2 = Guid('bb07bacd-cd56-4e63-a8ff-cbf0355fb9f4')
def _define_IEventSystem_head():
    class IEventSystem(win32more.System.Com.IDispatch_head):
        Guid = Guid('4e14fb9f-2e22-11d1-9964-00c04fbbb345')
    return IEventSystem
def _define_IEventSystem():
    IEventSystem = win32more.System.Com.Events.IEventSystem_head
    IEventSystem.Query = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(Int32),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'Query', ((1, 'progID'),(1, 'queryCriteria'),(1, 'errorIndex'),(1, 'ppInterface'),)))
    IEventSystem.Store = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.IUnknown_head, use_last_error=False)(8, 'Store', ((1, 'ProgID'),(1, 'pInterface'),)))
    IEventSystem.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(Int32), use_last_error=False)(9, 'Remove', ((1, 'progID'),(1, 'queryCriteria'),(1, 'errorIndex'),)))
    IEventSystem.get_EventObjectChangeEventClassID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_EventObjectChangeEventClassID', ((1, 'pbstrEventClassID'),)))
    IEventSystem.QueryS = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(11, 'QueryS', ((1, 'progID'),(1, 'queryCriteria'),(1, 'ppInterface'),)))
    IEventSystem.RemoveS = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(12, 'RemoveS', ((1, 'progID'),(1, 'queryCriteria'),)))
    return IEventSystem
def _define_IEventPublisher_head():
    class IEventPublisher(win32more.System.Com.IDispatch_head):
        Guid = Guid('e341516b-2e32-11d1-9964-00c04fbbb345')
    return IEventPublisher
def _define_IEventPublisher():
    IEventPublisher = win32more.System.Com.Events.IEventPublisher_head
    IEventPublisher.get_PublisherID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_PublisherID', ((1, 'pbstrPublisherID'),)))
    IEventPublisher.put_PublisherID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_PublisherID', ((1, 'bstrPublisherID'),)))
    IEventPublisher.get_PublisherName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_PublisherName', ((1, 'pbstrPublisherName'),)))
    IEventPublisher.put_PublisherName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_PublisherName', ((1, 'bstrPublisherName'),)))
    IEventPublisher.get_PublisherType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_PublisherType', ((1, 'pbstrPublisherType'),)))
    IEventPublisher.put_PublisherType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(12, 'put_PublisherType', ((1, 'bstrPublisherType'),)))
    IEventPublisher.get_OwnerSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_OwnerSID', ((1, 'pbstrOwnerSID'),)))
    IEventPublisher.put_OwnerSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(14, 'put_OwnerSID', ((1, 'bstrOwnerSID'),)))
    IEventPublisher.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_Description', ((1, 'pbstrDescription'),)))
    IEventPublisher.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(16, 'put_Description', ((1, 'bstrDescription'),)))
    IEventPublisher.GetDefaultProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(17, 'GetDefaultProperty', ((1, 'bstrPropertyName'),(1, 'propertyValue'),)))
    IEventPublisher.PutDefaultProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(18, 'PutDefaultProperty', ((1, 'bstrPropertyName'),(1, 'propertyValue'),)))
    IEventPublisher.RemoveDefaultProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(19, 'RemoveDefaultProperty', ((1, 'bstrPropertyName'),)))
    IEventPublisher.GetDefaultPropertyCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.Events.IEventObjectCollection_head), use_last_error=False)(20, 'GetDefaultPropertyCollection', ((1, 'collection'),)))
    return IEventPublisher
def _define_IEventClass_head():
    class IEventClass(win32more.System.Com.IDispatch_head):
        Guid = Guid('fb2b72a0-7a68-11d1-88f9-0080c7d771bf')
    return IEventClass
def _define_IEventClass():
    IEventClass = win32more.System.Com.Events.IEventClass_head
    IEventClass.get_EventClassID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_EventClassID', ((1, 'pbstrEventClassID'),)))
    IEventClass.put_EventClassID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_EventClassID', ((1, 'bstrEventClassID'),)))
    IEventClass.get_EventClassName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_EventClassName', ((1, 'pbstrEventClassName'),)))
    IEventClass.put_EventClassName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_EventClassName', ((1, 'bstrEventClassName'),)))
    IEventClass.get_OwnerSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_OwnerSID', ((1, 'pbstrOwnerSID'),)))
    IEventClass.put_OwnerSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(12, 'put_OwnerSID', ((1, 'bstrOwnerSID'),)))
    IEventClass.get_FiringInterfaceID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_FiringInterfaceID', ((1, 'pbstrFiringInterfaceID'),)))
    IEventClass.put_FiringInterfaceID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(14, 'put_FiringInterfaceID', ((1, 'bstrFiringInterfaceID'),)))
    IEventClass.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_Description', ((1, 'pbstrDescription'),)))
    IEventClass.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(16, 'put_Description', ((1, 'bstrDescription'),)))
    IEventClass.get_CustomConfigCLSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'get_CustomConfigCLSID', ((1, 'pbstrCustomConfigCLSID'),)))
    IEventClass.put_CustomConfigCLSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(18, 'put_CustomConfigCLSID', ((1, 'bstrCustomConfigCLSID'),)))
    IEventClass.get_TypeLib = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(19, 'get_TypeLib', ((1, 'pbstrTypeLib'),)))
    IEventClass.put_TypeLib = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(20, 'put_TypeLib', ((1, 'bstrTypeLib'),)))
    return IEventClass
def _define_IEventClass2_head():
    class IEventClass2(win32more.System.Com.Events.IEventClass_head):
        Guid = Guid('fb2b72a1-7a68-11d1-88f9-0080c7d771bf')
    return IEventClass2
def _define_IEventClass2():
    IEventClass2 = win32more.System.Com.Events.IEventClass2_head
    IEventClass2.get_PublisherID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(21, 'get_PublisherID', ((1, 'pbstrPublisherID'),)))
    IEventClass2.put_PublisherID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(22, 'put_PublisherID', ((1, 'bstrPublisherID'),)))
    IEventClass2.get_MultiInterfacePublisherFilterCLSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(23, 'get_MultiInterfacePublisherFilterCLSID', ((1, 'pbstrPubFilCLSID'),)))
    IEventClass2.put_MultiInterfacePublisherFilterCLSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(24, 'put_MultiInterfacePublisherFilterCLSID', ((1, 'bstrPubFilCLSID'),)))
    IEventClass2.get_AllowInprocActivation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(25, 'get_AllowInprocActivation', ((1, 'pfAllowInprocActivation'),)))
    IEventClass2.put_AllowInprocActivation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(26, 'put_AllowInprocActivation', ((1, 'fAllowInprocActivation'),)))
    IEventClass2.get_FireInParallel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(27, 'get_FireInParallel', ((1, 'pfFireInParallel'),)))
    IEventClass2.put_FireInParallel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(28, 'put_FireInParallel', ((1, 'fFireInParallel'),)))
    return IEventClass2
def _define_IEventSubscription_head():
    class IEventSubscription(win32more.System.Com.IDispatch_head):
        Guid = Guid('4a6b0e15-2e38-11d1-9965-00c04fbbb345')
    return IEventSubscription
def _define_IEventSubscription():
    IEventSubscription = win32more.System.Com.Events.IEventSubscription_head
    IEventSubscription.get_SubscriptionID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_SubscriptionID', ((1, 'pbstrSubscriptionID'),)))
    IEventSubscription.put_SubscriptionID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_SubscriptionID', ((1, 'bstrSubscriptionID'),)))
    IEventSubscription.get_SubscriptionName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_SubscriptionName', ((1, 'pbstrSubscriptionName'),)))
    IEventSubscription.put_SubscriptionName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_SubscriptionName', ((1, 'bstrSubscriptionName'),)))
    IEventSubscription.get_PublisherID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_PublisherID', ((1, 'pbstrPublisherID'),)))
    IEventSubscription.put_PublisherID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(12, 'put_PublisherID', ((1, 'bstrPublisherID'),)))
    IEventSubscription.get_EventClassID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_EventClassID', ((1, 'pbstrEventClassID'),)))
    IEventSubscription.put_EventClassID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(14, 'put_EventClassID', ((1, 'bstrEventClassID'),)))
    IEventSubscription.get_MethodName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_MethodName', ((1, 'pbstrMethodName'),)))
    IEventSubscription.put_MethodName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(16, 'put_MethodName', ((1, 'bstrMethodName'),)))
    IEventSubscription.get_SubscriberCLSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'get_SubscriberCLSID', ((1, 'pbstrSubscriberCLSID'),)))
    IEventSubscription.put_SubscriberCLSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(18, 'put_SubscriberCLSID', ((1, 'bstrSubscriberCLSID'),)))
    IEventSubscription.get_SubscriberInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(19, 'get_SubscriberInterface', ((1, 'ppSubscriberInterface'),)))
    IEventSubscription.put_SubscriberInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(20, 'put_SubscriberInterface', ((1, 'pSubscriberInterface'),)))
    IEventSubscription.get_PerUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(21, 'get_PerUser', ((1, 'pfPerUser'),)))
    IEventSubscription.put_PerUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(22, 'put_PerUser', ((1, 'fPerUser'),)))
    IEventSubscription.get_OwnerSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(23, 'get_OwnerSID', ((1, 'pbstrOwnerSID'),)))
    IEventSubscription.put_OwnerSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(24, 'put_OwnerSID', ((1, 'bstrOwnerSID'),)))
    IEventSubscription.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(25, 'get_Enabled', ((1, 'pfEnabled'),)))
    IEventSubscription.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(26, 'put_Enabled', ((1, 'fEnabled'),)))
    IEventSubscription.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(27, 'get_Description', ((1, 'pbstrDescription'),)))
    IEventSubscription.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(28, 'put_Description', ((1, 'bstrDescription'),)))
    IEventSubscription.get_MachineName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(29, 'get_MachineName', ((1, 'pbstrMachineName'),)))
    IEventSubscription.put_MachineName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(30, 'put_MachineName', ((1, 'bstrMachineName'),)))
    IEventSubscription.GetPublisherProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(31, 'GetPublisherProperty', ((1, 'bstrPropertyName'),(1, 'propertyValue'),)))
    IEventSubscription.PutPublisherProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(32, 'PutPublisherProperty', ((1, 'bstrPropertyName'),(1, 'propertyValue'),)))
    IEventSubscription.RemovePublisherProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(33, 'RemovePublisherProperty', ((1, 'bstrPropertyName'),)))
    IEventSubscription.GetPublisherPropertyCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.Events.IEventObjectCollection_head), use_last_error=False)(34, 'GetPublisherPropertyCollection', ((1, 'collection'),)))
    IEventSubscription.GetSubscriberProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(35, 'GetSubscriberProperty', ((1, 'bstrPropertyName'),(1, 'propertyValue'),)))
    IEventSubscription.PutSubscriberProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(36, 'PutSubscriberProperty', ((1, 'bstrPropertyName'),(1, 'propertyValue'),)))
    IEventSubscription.RemoveSubscriberProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(37, 'RemoveSubscriberProperty', ((1, 'bstrPropertyName'),)))
    IEventSubscription.GetSubscriberPropertyCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.Events.IEventObjectCollection_head), use_last_error=False)(38, 'GetSubscriberPropertyCollection', ((1, 'collection'),)))
    IEventSubscription.get_InterfaceID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(39, 'get_InterfaceID', ((1, 'pbstrInterfaceID'),)))
    IEventSubscription.put_InterfaceID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(40, 'put_InterfaceID', ((1, 'bstrInterfaceID'),)))
    return IEventSubscription
def _define_IFiringControl_head():
    class IFiringControl(win32more.System.Com.IDispatch_head):
        Guid = Guid('e0498c93-4efe-11d1-9971-00c04fbbb345')
    return IFiringControl
def _define_IFiringControl():
    IFiringControl = win32more.System.Com.Events.IFiringControl_head
    IFiringControl.FireSubscription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.Events.IEventSubscription_head, use_last_error=False)(7, 'FireSubscription', ((1, 'subscription'),)))
    return IFiringControl
def _define_IPublisherFilter_head():
    class IPublisherFilter(win32more.System.Com.IUnknown_head):
        Guid = Guid('465e5cc0-7b26-11d1-88fb-0080c7d771bf')
    return IPublisherFilter
def _define_IPublisherFilter():
    IPublisherFilter = win32more.System.Com.Events.IPublisherFilter_head
    IPublisherFilter.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.IDispatch_head, use_last_error=False)(3, 'Initialize', ((1, 'methodName'),(1, 'dispUserDefined'),)))
    IPublisherFilter.PrepareToFire = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.Events.IFiringControl_head, use_last_error=False)(4, 'PrepareToFire', ((1, 'methodName'),(1, 'firingControl'),)))
    return IPublisherFilter
def _define_IMultiInterfacePublisherFilter_head():
    class IMultiInterfacePublisherFilter(win32more.System.Com.IUnknown_head):
        Guid = Guid('465e5cc1-7b26-11d1-88fb-0080c7d771bf')
    return IMultiInterfacePublisherFilter
def _define_IMultiInterfacePublisherFilter():
    IMultiInterfacePublisherFilter = win32more.System.Com.Events.IMultiInterfacePublisherFilter_head
    IMultiInterfacePublisherFilter.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.Events.IMultiInterfaceEventControl_head, use_last_error=False)(3, 'Initialize', ((1, 'pEIC'),)))
    IMultiInterfacePublisherFilter.PrepareToFire = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.BSTR,win32more.System.Com.Events.IFiringControl_head, use_last_error=False)(4, 'PrepareToFire', ((1, 'iid'),(1, 'methodName'),(1, 'firingControl'),)))
    return IMultiInterfacePublisherFilter
EOC_ChangeType = Int32
EOC_NewObject = 0
EOC_ModifiedObject = 1
EOC_DeletedObject = 2
def _define_IEventObjectChange_head():
    class IEventObjectChange(win32more.System.Com.IUnknown_head):
        Guid = Guid('f4a07d70-2e25-11d1-9964-00c04fbbb345')
    return IEventObjectChange
def _define_IEventObjectChange():
    IEventObjectChange = win32more.System.Com.Events.IEventObjectChange_head
    IEventObjectChange.ChangedSubscription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.Events.EOC_ChangeType,win32more.Foundation.BSTR, use_last_error=False)(3, 'ChangedSubscription', ((1, 'changeType'),(1, 'bstrSubscriptionID'),)))
    IEventObjectChange.ChangedEventClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.Events.EOC_ChangeType,win32more.Foundation.BSTR, use_last_error=False)(4, 'ChangedEventClass', ((1, 'changeType'),(1, 'bstrEventClassID'),)))
    IEventObjectChange.ChangedPublisher = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.Events.EOC_ChangeType,win32more.Foundation.BSTR, use_last_error=False)(5, 'ChangedPublisher', ((1, 'changeType'),(1, 'bstrPublisherID'),)))
    return IEventObjectChange
def _define_COMEVENTSYSCHANGEINFO_head():
    class COMEVENTSYSCHANGEINFO(Structure):
        pass
    return COMEVENTSYSCHANGEINFO
def _define_COMEVENTSYSCHANGEINFO():
    COMEVENTSYSCHANGEINFO = win32more.System.Com.Events.COMEVENTSYSCHANGEINFO_head
    COMEVENTSYSCHANGEINFO._fields_ = [
        ("cbSize", UInt32),
        ("changeType", win32more.System.Com.Events.EOC_ChangeType),
        ("objectId", win32more.Foundation.BSTR),
        ("partitionId", win32more.Foundation.BSTR),
        ("applicationId", win32more.Foundation.BSTR),
        ("reserved", Guid * 10),
    ]
    return COMEVENTSYSCHANGEINFO
def _define_IEventObjectChange2_head():
    class IEventObjectChange2(win32more.System.Com.IUnknown_head):
        Guid = Guid('7701a9c3-bd68-438f-83e0-67bf4f53a422')
    return IEventObjectChange2
def _define_IEventObjectChange2():
    IEventObjectChange2 = win32more.System.Com.Events.IEventObjectChange2_head
    IEventObjectChange2.ChangedSubscription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.Events.COMEVENTSYSCHANGEINFO_head), use_last_error=False)(3, 'ChangedSubscription', ((1, 'pInfo'),)))
    IEventObjectChange2.ChangedEventClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.Events.COMEVENTSYSCHANGEINFO_head), use_last_error=False)(4, 'ChangedEventClass', ((1, 'pInfo'),)))
    return IEventObjectChange2
def _define_IEnumEventObject_head():
    class IEnumEventObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('f4a07d63-2e25-11d1-9964-00c04fbbb345')
    return IEnumEventObject
def _define_IEnumEventObject():
    IEnumEventObject = win32more.System.Com.Events.IEnumEventObject_head
    IEnumEventObject.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.Events.IEnumEventObject_head), use_last_error=False)(3, 'Clone', ((1, 'ppInterface'),)))
    IEnumEventObject.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.IUnknown_head),POINTER(UInt32), use_last_error=False)(4, 'Next', ((1, 'cReqElem'),(1, 'ppInterface'),(1, 'cRetElem'),)))
    IEnumEventObject.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumEventObject.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'Skip', ((1, 'cSkipElem'),)))
    return IEnumEventObject
def _define_IEventObjectCollection_head():
    class IEventObjectCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('f89ac270-d4eb-11d1-b682-00805fc79216')
    return IEventObjectCollection
def _define_IEventObjectCollection():
    IEventObjectCollection = win32more.System.Com.Events.IEventObjectCollection_head
    IEventObjectCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'ppUnkEnum'),)))
    IEventObjectCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'get_Item', ((1, 'objectID'),(1, 'pItem'),)))
    IEventObjectCollection.get_NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.Events.IEnumEventObject_head), use_last_error=False)(9, 'get_NewEnum', ((1, 'ppEnum'),)))
    IEventObjectCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_Count', ((1, 'pCount'),)))
    IEventObjectCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),win32more.Foundation.BSTR, use_last_error=False)(11, 'Add', ((1, 'item'),(1, 'objectID'),)))
    IEventObjectCollection.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(12, 'Remove', ((1, 'objectID'),)))
    return IEventObjectCollection
def _define_IEventProperty_head():
    class IEventProperty(win32more.System.Com.IDispatch_head):
        Guid = Guid('da538ee2-f4de-11d1-b6bb-00805fc79216')
    return IEventProperty
def _define_IEventProperty():
    IEventProperty = win32more.System.Com.Events.IEventProperty_head
    IEventProperty.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Name', ((1, 'propertyName'),)))
    IEventProperty.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_Name', ((1, 'propertyName'),)))
    IEventProperty.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(9, 'get_Value', ((1, 'propertyValue'),)))
    IEventProperty.put_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(10, 'put_Value', ((1, 'propertyValue'),)))
    return IEventProperty
def _define_IEventControl_head():
    class IEventControl(win32more.System.Com.IDispatch_head):
        Guid = Guid('0343e2f4-86f6-11d1-b760-00c04fb926af')
    return IEventControl
def _define_IEventControl():
    IEventControl = win32more.System.Com.Events.IEventControl_head
    IEventControl.SetPublisherFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.Events.IPublisherFilter_head, use_last_error=False)(7, 'SetPublisherFilter', ((1, 'methodName'),(1, 'pPublisherFilter'),)))
    IEventControl.get_AllowInprocActivation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(8, 'get_AllowInprocActivation', ((1, 'pfAllowInprocActivation'),)))
    IEventControl.put_AllowInprocActivation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(9, 'put_AllowInprocActivation', ((1, 'fAllowInprocActivation'),)))
    IEventControl.GetSubscriptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(Int32),POINTER(win32more.System.Com.Events.IEventObjectCollection_head), use_last_error=False)(10, 'GetSubscriptions', ((1, 'methodName'),(1, 'optionalCriteria'),(1, 'optionalErrorIndex'),(1, 'ppCollection'),)))
    IEventControl.SetDefaultQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(Int32), use_last_error=False)(11, 'SetDefaultQuery', ((1, 'methodName'),(1, 'criteria'),(1, 'errorIndex'),)))
    return IEventControl
def _define_IMultiInterfaceEventControl_head():
    class IMultiInterfaceEventControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('0343e2f5-86f6-11d1-b760-00c04fb926af')
    return IMultiInterfaceEventControl
def _define_IMultiInterfaceEventControl():
    IMultiInterfaceEventControl = win32more.System.Com.Events.IMultiInterfaceEventControl_head
    IMultiInterfaceEventControl.SetMultiInterfacePublisherFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.Events.IMultiInterfacePublisherFilter_head, use_last_error=False)(3, 'SetMultiInterfacePublisherFilter', ((1, 'classFilter'),)))
    IMultiInterfaceEventControl.GetSubscriptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(Int32),POINTER(win32more.System.Com.Events.IEventObjectCollection_head), use_last_error=False)(4, 'GetSubscriptions', ((1, 'eventIID'),(1, 'bstrMethodName'),(1, 'optionalCriteria'),(1, 'optionalErrorIndex'),(1, 'ppCollection'),)))
    IMultiInterfaceEventControl.SetDefaultQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(Int32), use_last_error=False)(5, 'SetDefaultQuery', ((1, 'eventIID'),(1, 'bstrMethodName'),(1, 'bstrCriteria'),(1, 'errorIndex'),)))
    IMultiInterfaceEventControl.get_AllowInprocActivation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'get_AllowInprocActivation', ((1, 'pfAllowInprocActivation'),)))
    IMultiInterfaceEventControl.put_AllowInprocActivation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(7, 'put_AllowInprocActivation', ((1, 'fAllowInprocActivation'),)))
    IMultiInterfaceEventControl.get_FireInParallel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(8, 'get_FireInParallel', ((1, 'pfFireInParallel'),)))
    IMultiInterfaceEventControl.put_FireInParallel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(9, 'put_FireInParallel', ((1, 'fFireInParallel'),)))
    return IMultiInterfaceEventControl
def _define_IDontSupportEventSubscription_head():
    class IDontSupportEventSubscription(win32more.System.Com.IUnknown_head):
        Guid = Guid('784121f1-62a6-4b89-855f-d65f296de83a')
    return IDontSupportEventSubscription
def _define_IDontSupportEventSubscription():
    IDontSupportEventSubscription = win32more.System.Com.Events.IDontSupportEventSubscription_head
    return IDontSupportEventSubscription
__all__ = [
    "CEventSystem",
    "CEventPublisher",
    "CEventClass",
    "CEventSubscription",
    "EventObjectChange",
    "EventObjectChange2",
    "IEventSystem",
    "IEventPublisher",
    "IEventClass",
    "IEventClass2",
    "IEventSubscription",
    "IFiringControl",
    "IPublisherFilter",
    "IMultiInterfacePublisherFilter",
    "EOC_ChangeType",
    "EOC_NewObject",
    "EOC_ModifiedObject",
    "EOC_DeletedObject",
    "IEventObjectChange",
    "COMEVENTSYSCHANGEINFO",
    "IEventObjectChange2",
    "IEnumEventObject",
    "IEventObjectCollection",
    "IEventProperty",
    "IEventControl",
    "IMultiInterfaceEventControl",
    "IDontSupportEventSubscription",
]
