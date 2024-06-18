from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.System.Search.Common
CONDITION_OPERATION = Int32
COP_IMPLICIT: win32more.Windows.Win32.System.Search.Common.CONDITION_OPERATION = 0
COP_EQUAL: win32more.Windows.Win32.System.Search.Common.CONDITION_OPERATION = 1
COP_NOTEQUAL: win32more.Windows.Win32.System.Search.Common.CONDITION_OPERATION = 2
COP_LESSTHAN: win32more.Windows.Win32.System.Search.Common.CONDITION_OPERATION = 3
COP_GREATERTHAN: win32more.Windows.Win32.System.Search.Common.CONDITION_OPERATION = 4
COP_LESSTHANOREQUAL: win32more.Windows.Win32.System.Search.Common.CONDITION_OPERATION = 5
COP_GREATERTHANOREQUAL: win32more.Windows.Win32.System.Search.Common.CONDITION_OPERATION = 6
COP_VALUE_STARTSWITH: win32more.Windows.Win32.System.Search.Common.CONDITION_OPERATION = 7
COP_VALUE_ENDSWITH: win32more.Windows.Win32.System.Search.Common.CONDITION_OPERATION = 8
COP_VALUE_CONTAINS: win32more.Windows.Win32.System.Search.Common.CONDITION_OPERATION = 9
COP_VALUE_NOTCONTAINS: win32more.Windows.Win32.System.Search.Common.CONDITION_OPERATION = 10
COP_DOSWILDCARDS: win32more.Windows.Win32.System.Search.Common.CONDITION_OPERATION = 11
COP_WORD_EQUAL: win32more.Windows.Win32.System.Search.Common.CONDITION_OPERATION = 12
COP_WORD_STARTSWITH: win32more.Windows.Win32.System.Search.Common.CONDITION_OPERATION = 13
COP_APPLICATION_SPECIFIC: win32more.Windows.Win32.System.Search.Common.CONDITION_OPERATION = 14
CONDITION_TYPE = Int32
CT_AND_CONDITION: win32more.Windows.Win32.System.Search.Common.CONDITION_TYPE = 0
CT_OR_CONDITION: win32more.Windows.Win32.System.Search.Common.CONDITION_TYPE = 1
CT_NOT_CONDITION: win32more.Windows.Win32.System.Search.Common.CONDITION_TYPE = 2
CT_LEAF_CONDITION: win32more.Windows.Win32.System.Search.Common.CONDITION_TYPE = 3


make_ready(__name__)
