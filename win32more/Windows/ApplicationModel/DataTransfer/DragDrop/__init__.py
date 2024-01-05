from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import Annotated, Generic, K, MulticastDelegate, SZArray, T, TProgress, TResult, TSender, V, WinRT_String, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.DataTransfer.DragDrop
DragDropModifiers = UInt32
DragDropModifiers_None: DragDropModifiers = 0
DragDropModifiers_Shift: DragDropModifiers = 1
DragDropModifiers_Control: DragDropModifiers = 2
DragDropModifiers_Alt: DragDropModifiers = 4
DragDropModifiers_LeftButton: DragDropModifiers = 8
DragDropModifiers_MiddleButton: DragDropModifiers = 16
DragDropModifiers_RightButton: DragDropModifiers = 32


make_ready(__name__)
