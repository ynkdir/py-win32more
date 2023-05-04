from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.UI.UIAutomation
import Windows.UI.UIAutomation.Core
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AutomationAnnotationTypeRegistration(EasyCastStructure):
    LocalId: Int32
class AutomationRemoteOperationOperandId(EasyCastStructure):
    Value: Int32
class AutomationRemoteOperationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.UIAutomation.Core.AutomationRemoteOperationResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.UI.UIAutomation.Core.IAutomationRemoteOperationResult) -> Windows.UI.UIAutomation.Core.AutomationRemoteOperationStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.UI.UIAutomation.Core.IAutomationRemoteOperationResult) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_ErrorLocation(self: Windows.UI.UIAutomation.Core.IAutomationRemoteOperationResult) -> Int32: ...
    @winrt_mixinmethod
    def HasOperand(self: Windows.UI.UIAutomation.Core.IAutomationRemoteOperationResult, operandId: Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId) -> Boolean: ...
    @winrt_mixinmethod
    def GetOperand(self: Windows.UI.UIAutomation.Core.IAutomationRemoteOperationResult, operandId: Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
    ErrorLocation = property(get_ErrorLocation, None)
AutomationRemoteOperationStatus = Int32
AutomationRemoteOperationStatus_Success: AutomationRemoteOperationStatus = 0
AutomationRemoteOperationStatus_MalformedBytecode: AutomationRemoteOperationStatus = 1
AutomationRemoteOperationStatus_InstructionLimitExceeded: AutomationRemoteOperationStatus = 2
AutomationRemoteOperationStatus_UnhandledException: AutomationRemoteOperationStatus = 3
AutomationRemoteOperationStatus_ExecutionFailure: AutomationRemoteOperationStatus = 4
class CoreAutomationRegistrar(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.UIAutomation.Core.CoreAutomationRegistrar'
    @winrt_classmethod
    def RegisterAnnotationType(cls: Windows.UI.UIAutomation.Core.ICoreAutomationRegistrarStatics, guid: Guid) -> Windows.UI.UIAutomation.Core.AutomationAnnotationTypeRegistration: ...
    @winrt_classmethod
    def UnregisterAnnotationType(cls: Windows.UI.UIAutomation.Core.ICoreAutomationRegistrarStatics, registration: Windows.UI.UIAutomation.Core.AutomationAnnotationTypeRegistration) -> Void: ...
class CoreAutomationRemoteOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.UIAutomation.Core.CoreAutomationRemoteOperation'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.UIAutomation.Core.CoreAutomationRemoteOperation: ...
    @winrt_mixinmethod
    def IsOpcodeSupported(self: Windows.UI.UIAutomation.Core.ICoreAutomationRemoteOperation, opcode: UInt32) -> Boolean: ...
    @winrt_mixinmethod
    def ImportElement(self: Windows.UI.UIAutomation.Core.ICoreAutomationRemoteOperation, operandId: Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId, element: Windows.UI.UIAutomation.AutomationElement) -> Void: ...
    @winrt_mixinmethod
    def ImportTextRange(self: Windows.UI.UIAutomation.Core.ICoreAutomationRemoteOperation, operandId: Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId, textRange: Windows.UI.UIAutomation.AutomationTextRange) -> Void: ...
    @winrt_mixinmethod
    def AddToResults(self: Windows.UI.UIAutomation.Core.ICoreAutomationRemoteOperation, operandId: Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId) -> Void: ...
    @winrt_mixinmethod
    def Execute(self: Windows.UI.UIAutomation.Core.ICoreAutomationRemoteOperation, bytecodeBuffer: c_char_p_no) -> Windows.UI.UIAutomation.Core.AutomationRemoteOperationResult: ...
    @winrt_mixinmethod
    def ImportConnectionBoundObject(self: Windows.UI.UIAutomation.Core.ICoreAutomationRemoteOperation2, operandId: Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId, connectionBoundObject: Windows.UI.UIAutomation.AutomationConnectionBoundObject) -> Void: ...
class CoreAutomationRemoteOperationContext(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.UIAutomation.Core.CoreAutomationRemoteOperationContext'
    @winrt_mixinmethod
    def GetOperand(self: Windows.UI.UIAutomation.Core.ICoreAutomationRemoteOperationContext, id: Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def SetOperand(self: Windows.UI.UIAutomation.Core.ICoreAutomationRemoteOperationContext, id: Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId, operand: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def SetOperand2(self: Windows.UI.UIAutomation.Core.ICoreAutomationRemoteOperationContext, id: Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId, operand: Windows.Win32.System.WinRT.IInspectable_head, operandInterfaceId: Guid) -> Void: ...
class IAutomationRemoteOperationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e0f80c42-4a67-5534-bf5a-09e8a99b36b1}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.UI.UIAutomation.Core.AutomationRemoteOperationStatus: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(8)
    def get_ErrorLocation(self) -> Int32: ...
    @winrt_commethod(9)
    def HasOperand(self, operandId: Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId) -> Boolean: ...
    @winrt_commethod(10)
    def GetOperand(self, operandId: Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
    ErrorLocation = property(get_ErrorLocation, None)
class ICoreAutomationConnectionBoundObjectProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0620bb64-9616-5593-be3a-eb8e6daeb3fa}')
    @winrt_commethod(6)
    def get_IsComThreadingRequired(self) -> Boolean: ...
    IsComThreadingRequired = property(get_IsComThreadingRequired, None)
class ICoreAutomationRegistrarStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{3e50129b-d6dc-5680-b580-ffff78300304}')
    @winrt_commethod(6)
    def RegisterAnnotationType(self, guid: Guid) -> Windows.UI.UIAutomation.Core.AutomationAnnotationTypeRegistration: ...
    @winrt_commethod(7)
    def UnregisterAnnotationType(self, registration: Windows.UI.UIAutomation.Core.AutomationAnnotationTypeRegistration) -> Void: ...
class ICoreAutomationRemoteOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{3ac656f4-e2bc-5c6e-b8e7-b224fb74b060}')
    @winrt_commethod(6)
    def IsOpcodeSupported(self, opcode: UInt32) -> Boolean: ...
    @winrt_commethod(7)
    def ImportElement(self, operandId: Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId, element: Windows.UI.UIAutomation.AutomationElement) -> Void: ...
    @winrt_commethod(8)
    def ImportTextRange(self, operandId: Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId, textRange: Windows.UI.UIAutomation.AutomationTextRange) -> Void: ...
    @winrt_commethod(9)
    def AddToResults(self, operandId: Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId) -> Void: ...
    @winrt_commethod(10)
    def Execute(self, bytecodeBuffer: c_char_p_no) -> Windows.UI.UIAutomation.Core.AutomationRemoteOperationResult: ...
class ICoreAutomationRemoteOperation2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{eefaf86f-e953-5099-8ce9-dca813482ba0}')
    @winrt_commethod(6)
    def ImportConnectionBoundObject(self, operandId: Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId, connectionBoundObject: Windows.UI.UIAutomation.AutomationConnectionBoundObject) -> Void: ...
class ICoreAutomationRemoteOperationContext(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b9af9cbb-3d3e-5918-a16b-7861626a3aeb}')
    @winrt_commethod(6)
    def GetOperand(self, id: Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def SetOperand(self, id: Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId, operand: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(8)
    def SetOperand2(self, id: Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId, operand: Windows.Win32.System.WinRT.IInspectable_head, operandInterfaceId: Guid) -> Void: ...
class ICoreAutomationRemoteOperationExtensionProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{88f53e67-dc69-553b-a0aa-70477e724da8}')
    @winrt_commethod(6)
    def CallExtension(self, extensionId: Guid, context: Windows.UI.UIAutomation.Core.CoreAutomationRemoteOperationContext, operandIds: POINTER(Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId_head)) -> Void: ...
    @winrt_commethod(7)
    def IsExtensionSupported(self, extensionId: Guid) -> Boolean: ...
class IRemoteAutomationClientSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{5c8a091d-94cc-5b33-afdb-678cded2bd54}')
    @winrt_commethod(6)
    def Start(self) -> Void: ...
    @winrt_commethod(7)
    def Stop(self) -> Void: ...
    @winrt_commethod(8)
    def CreateWindowAsync(self, remoteWindowId: UInt64, remoteProcessId: UInt32, parentAutomationElement: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.Foundation.IAsyncOperation[Windows.UI.UIAutomation.Core.RemoteAutomationWindow]: ...
    @winrt_commethod(9)
    def get_SessionId(self) -> Guid: ...
    @winrt_commethod(10)
    def add_ConnectionRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.UIAutomation.Core.RemoteAutomationClientSession, Windows.UI.UIAutomation.Core.RemoteAutomationConnectionRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ConnectionRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_Disconnected(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.UIAutomation.Core.RemoteAutomationClientSession, Windows.UI.UIAutomation.Core.RemoteAutomationDisconnectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_Disconnected(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    SessionId = property(get_SessionId, None)
class IRemoteAutomationClientSessionFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f250263d-6057-5373-a5a5-ed7265fe0376}')
    @winrt_commethod(6)
    def CreateInstance(self, name: WinRT_String) -> Windows.UI.UIAutomation.Core.RemoteAutomationClientSession: ...
    @winrt_commethod(7)
    def CreateInstance2(self, name: WinRT_String, sessionId: Guid) -> Windows.UI.UIAutomation.Core.RemoteAutomationClientSession: ...
class IRemoteAutomationConnectionRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{ea3319a8-e3a8-5dc6-adf8-044e46b14af5}')
    @winrt_commethod(6)
    def get_LocalPipeName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_RemoteProcessId(self) -> UInt32: ...
    LocalPipeName = property(get_LocalPipeName, None)
    RemoteProcessId = property(get_RemoteProcessId, None)
class IRemoteAutomationDisconnectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{bbb33a3d-5d90-5c38-9eb2-dd9dcc1b2e3f}')
    @winrt_commethod(6)
    def get_LocalPipeName(self) -> WinRT_String: ...
    LocalPipeName = property(get_LocalPipeName, None)
class IRemoteAutomationServerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e6e8945e-0c11-5028-9ae3-c2771288b6b7}')
    @winrt_commethod(6)
    def ReportSession(self, sessionId: Guid) -> Void: ...
class IRemoteAutomationWindow(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{7c607689-496d-512a-9bd5-c050cfaf1428}')
    @winrt_commethod(6)
    def get_AutomationProvider(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def UnregisterAsync(self) -> Windows.Foundation.IAsyncAction: ...
    AutomationProvider = property(get_AutomationProvider, None)
class RemoteAutomationClientSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.UIAutomation.Core.RemoteAutomationClientSession'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.UIAutomation.Core.IRemoteAutomationClientSessionFactory, name: WinRT_String) -> Windows.UI.UIAutomation.Core.RemoteAutomationClientSession: ...
    @winrt_factorymethod
    def CreateInstance2(cls: Windows.UI.UIAutomation.Core.IRemoteAutomationClientSessionFactory, name: WinRT_String, sessionId: Guid) -> Windows.UI.UIAutomation.Core.RemoteAutomationClientSession: ...
    @winrt_mixinmethod
    def Start(self: Windows.UI.UIAutomation.Core.IRemoteAutomationClientSession) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.UI.UIAutomation.Core.IRemoteAutomationClientSession) -> Void: ...
    @winrt_mixinmethod
    def CreateWindowAsync(self: Windows.UI.UIAutomation.Core.IRemoteAutomationClientSession, remoteWindowId: UInt64, remoteProcessId: UInt32, parentAutomationElement: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.Foundation.IAsyncOperation[Windows.UI.UIAutomation.Core.RemoteAutomationWindow]: ...
    @winrt_mixinmethod
    def get_SessionId(self: Windows.UI.UIAutomation.Core.IRemoteAutomationClientSession) -> Guid: ...
    @winrt_mixinmethod
    def add_ConnectionRequested(self: Windows.UI.UIAutomation.Core.IRemoteAutomationClientSession, handler: Windows.Foundation.TypedEventHandler[Windows.UI.UIAutomation.Core.RemoteAutomationClientSession, Windows.UI.UIAutomation.Core.RemoteAutomationConnectionRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ConnectionRequested(self: Windows.UI.UIAutomation.Core.IRemoteAutomationClientSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Disconnected(self: Windows.UI.UIAutomation.Core.IRemoteAutomationClientSession, handler: Windows.Foundation.TypedEventHandler[Windows.UI.UIAutomation.Core.RemoteAutomationClientSession, Windows.UI.UIAutomation.Core.RemoteAutomationDisconnectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Disconnected(self: Windows.UI.UIAutomation.Core.IRemoteAutomationClientSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    SessionId = property(get_SessionId, None)
class RemoteAutomationConnectionRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.UIAutomation.Core.RemoteAutomationConnectionRequestedEventArgs'
    @winrt_mixinmethod
    def get_LocalPipeName(self: Windows.UI.UIAutomation.Core.IRemoteAutomationConnectionRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RemoteProcessId(self: Windows.UI.UIAutomation.Core.IRemoteAutomationConnectionRequestedEventArgs) -> UInt32: ...
    LocalPipeName = property(get_LocalPipeName, None)
    RemoteProcessId = property(get_RemoteProcessId, None)
class RemoteAutomationDisconnectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.UIAutomation.Core.RemoteAutomationDisconnectedEventArgs'
    @winrt_mixinmethod
    def get_LocalPipeName(self: Windows.UI.UIAutomation.Core.IRemoteAutomationDisconnectedEventArgs) -> WinRT_String: ...
    LocalPipeName = property(get_LocalPipeName, None)
class RemoteAutomationServer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.UIAutomation.Core.RemoteAutomationServer'
    @winrt_classmethod
    def ReportSession(cls: Windows.UI.UIAutomation.Core.IRemoteAutomationServerStatics, sessionId: Guid) -> Void: ...
class RemoteAutomationWindow(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.UIAutomation.Core.RemoteAutomationWindow'
    @winrt_mixinmethod
    def get_AutomationProvider(self: Windows.UI.UIAutomation.Core.IRemoteAutomationWindow) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def UnregisterAsync(self: Windows.UI.UIAutomation.Core.IRemoteAutomationWindow) -> Windows.Foundation.IAsyncAction: ...
    AutomationProvider = property(get_AutomationProvider, None)
make_head(_module, 'AutomationAnnotationTypeRegistration')
make_head(_module, 'AutomationRemoteOperationOperandId')
make_head(_module, 'AutomationRemoteOperationResult')
make_head(_module, 'CoreAutomationRegistrar')
make_head(_module, 'CoreAutomationRemoteOperation')
make_head(_module, 'CoreAutomationRemoteOperationContext')
make_head(_module, 'IAutomationRemoteOperationResult')
make_head(_module, 'ICoreAutomationConnectionBoundObjectProvider')
make_head(_module, 'ICoreAutomationRegistrarStatics')
make_head(_module, 'ICoreAutomationRemoteOperation')
make_head(_module, 'ICoreAutomationRemoteOperation2')
make_head(_module, 'ICoreAutomationRemoteOperationContext')
make_head(_module, 'ICoreAutomationRemoteOperationExtensionProvider')
make_head(_module, 'IRemoteAutomationClientSession')
make_head(_module, 'IRemoteAutomationClientSessionFactory')
make_head(_module, 'IRemoteAutomationConnectionRequestedEventArgs')
make_head(_module, 'IRemoteAutomationDisconnectedEventArgs')
make_head(_module, 'IRemoteAutomationServerStatics')
make_head(_module, 'IRemoteAutomationWindow')
make_head(_module, 'RemoteAutomationClientSession')
make_head(_module, 'RemoteAutomationConnectionRequestedEventArgs')
make_head(_module, 'RemoteAutomationDisconnectedEventArgs')
make_head(_module, 'RemoteAutomationServer')
make_head(_module, 'RemoteAutomationWindow')
