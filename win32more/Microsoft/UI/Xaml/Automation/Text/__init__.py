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
import win32more.Microsoft.UI.Xaml.Automation.Text
TextPatternRangeEndpoint = Int32
TextPatternRangeEndpoint_Start: TextPatternRangeEndpoint = 0
TextPatternRangeEndpoint_End: TextPatternRangeEndpoint = 1
TextUnit = Int32
TextUnit_Character: TextUnit = 0
TextUnit_Format: TextUnit = 1
TextUnit_Word: TextUnit = 2
TextUnit_Line: TextUnit = 3
TextUnit_Paragraph: TextUnit = 4
TextUnit_Page: TextUnit = 5
TextUnit_Document: TextUnit = 6
make_ready(__name__)
