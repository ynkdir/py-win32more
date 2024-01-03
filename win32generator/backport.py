import sys

__all__ = ["TypeAlias", "removeprefix"]

if sys.version_info < (3, 11):
    from typing_extensions import TypeAlias
else:
    from typing import TypeAlias

if sys.version_info < (3, 9):

    def removeprefix(s, prefix):
        if s.startswith(prefix):
            return s[len(prefix) :]
        else:
            return s
else:
    removeprefix = str.removeprefix
