from __future__ import annotations

import logging

from win32more import POINTER, Boolean, UInt32, Void
from win32more._winrt import (
    ComClass,
    FillArray,
    PassArray,
    T,
    get_args,
    is_com_class,
)
from win32more.Windows.Foundation.Collections import IVector, IVectorView

logger = logging.getLogger(__name__)


class GenericInitialize:
    def __set__(self, instance, value):
        instance.__dict__["__orig_class__"] = value
        try:
            instance.__init_generic__()
        except Exception:
            # _BaseGenericAlias.__call__() ignore error
            logger.exception("Unhandled exception caught")
            raise


class Vector(ComClass, IVector[T], IVectorView[T]):
    __orig_class__ = GenericInitialize()

    def __init__(self, lst: list[T] | None = None) -> None:
        self._lst = lst

    def __init_generic__(self) -> None:
        super().__init__(own=True)

        self._type = get_args(self.__orig_class__)[0]

        if self._lst is None:
            self._lst = []

    def GetAt(self, index: UInt32) -> T:
        return self._lst[index]

    def get_Size(self) -> UInt32:
        return len(self._lst)

    def GetView(self) -> IVectorView[T]:
        return self.as_(IVector[self._type])

    def IndexOf(self, value: T, index: POINTER(UInt32)) -> Boolean:
        for i, v in enumerate(self._lst):
            if v == value:
                index[0] = i
                return True
        return False

    def SetAt(self, index: UInt32, value: T) -> Void:
        if is_com_class(self._type):
            value.AddRef()
        self._lst[index] = value

    def InsertAt(self, index: UInt32, value: T) -> Void:
        if is_com_class(self._type):
            value.AddRef()
        self._lst.insert(index, value)

    def RemoveAt(self, index: UInt32) -> Void:
        del self._lst[index]

    def Append(self, value: T) -> Void:
        if is_com_class(self._type):
            value.AddRef()
        self._lst.append(value)

    def RemoveAtEnd(self) -> Void:
        del self._lst[-1]

    def Clear(self) -> Void:
        self._lst[:] = []

    def GetMany(self, startIndex: UInt32, items: FillArray[T]) -> UInt32:
        numcopied = 0
        for i in range(startIndex, startIndex + len(items)):
            if i >= len(self._lst):
                break
            items[numcopied] = self._lst[i]
            numcopied += 1
        return numcopied

    def ReplaceAll(self, items: PassArray[T]) -> Void:
        self._lst[:] = items
        if is_com_class(self._type):
            for v in self._lst:
                v.AddRef()
