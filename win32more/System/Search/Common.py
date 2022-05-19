from win32more import *
import win32more.System.Search.Common

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
CONDITION_TYPE = Int32
CT_AND_CONDITION = 0
CT_OR_CONDITION = 1
CT_NOT_CONDITION = 2
CT_LEAF_CONDITION = 3
CONDITION_OPERATION = Int32
COP_IMPLICIT = 0
COP_EQUAL = 1
COP_NOTEQUAL = 2
COP_LESSTHAN = 3
COP_GREATERTHAN = 4
COP_LESSTHANOREQUAL = 5
COP_GREATERTHANOREQUAL = 6
COP_VALUE_STARTSWITH = 7
COP_VALUE_ENDSWITH = 8
COP_VALUE_CONTAINS = 9
COP_VALUE_NOTCONTAINS = 10
COP_DOSWILDCARDS = 11
COP_WORD_EQUAL = 12
COP_WORD_STARTSWITH = 13
COP_APPLICATION_SPECIFIC = 14
__all__ = [
    "CONDITION_TYPE",
    "CT_AND_CONDITION",
    "CT_OR_CONDITION",
    "CT_NOT_CONDITION",
    "CT_LEAF_CONDITION",
    "CONDITION_OPERATION",
    "COP_IMPLICIT",
    "COP_EQUAL",
    "COP_NOTEQUAL",
    "COP_LESSTHAN",
    "COP_GREATERTHAN",
    "COP_LESSTHANOREQUAL",
    "COP_GREATERTHANOREQUAL",
    "COP_VALUE_STARTSWITH",
    "COP_VALUE_ENDSWITH",
    "COP_VALUE_CONTAINS",
    "COP_VALUE_NOTCONTAINS",
    "COP_DOSWILDCARDS",
    "COP_WORD_EQUAL",
    "COP_WORD_STARTSWITH",
    "COP_APPLICATION_SPECIFIC",
]
