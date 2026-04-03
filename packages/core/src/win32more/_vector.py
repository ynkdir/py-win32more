from __future__ import annotations

import logging
from ctypes import POINTER

from win32more.Windows.Foundation import EventRegistrationToken
from win32more.Windows.Foundation.Collections import (
    CollectionChange,
    IIterable,
    IIterator,
    IObservableVector,
    IVector,
    IVectorChangedEventArgs,
    IVectorView,
    VectorChangedEventHandler,
)

from ._win32 import Boolean, UInt32, Void
from ._winrt import (
    ComClass,
    FillArray,
    PassArray,
    T,
    is_com_instance,
)

logger = logging.getLogger(__name__)


class Vector(ComClass, IVector[T], IVectorView[T], IIterable[T], IObservableVector[T]):
    def __init__(self, lst: list[T] | None = None) -> None:
        super().__init__(own=True)

        self._T = self.__args[0]

        self._observers = {}
        self._observers_count = 0

        if lst is None:
            self._lst = []
        else:
            self._lst = list(lst)

        for v in self._lst:
            self._addref(v)

    def GetAt(self, index: UInt32) -> T:
        return self._lst[index]

    def get_Size(self) -> UInt32:
        return len(self._lst)

    def GetView(self) -> IVectorView[T]:
        return self.as_(IVector[self._T])

    def IndexOf(self, value: T, index: POINTER(UInt32)) -> Boolean:
        for i, v in enumerate(self._lst):
            if v == value:
                index[0] = i
                return True
        return False

    def SetAt(self, index: UInt32, value: T) -> Void:
        self._release(self._lst[index])
        self._addref(value)
        self._lst[index] = value
        self._notify(VectorChangedEventArgs(CollectionChange.ItemChanged, index))

    def InsertAt(self, index: UInt32, value: T) -> Void:
        self._addref(value)
        self._lst.insert(index, value)
        self._notify(VectorChangedEventArgs(CollectionChange.ItemInserted, index))

    def RemoveAt(self, index: UInt32) -> Void:
        value = self._lst.pop(index)
        self._release(value)
        self._notify(VectorChangedEventArgs(CollectionChange.ItemRemoved, index))

    def Append(self, value: T) -> Void:
        self.InsertAt(len(self._lst), value)

    def RemoveAtEnd(self) -> Void:
        self.RemoveAt(len(self) - 1)

    def Clear(self) -> Void:
        for v in self._lst:
            self._release(v)
        self._lst[:] = []
        self._notify(VectorChangedEventArgs(CollectionChange.Reset, 0))

    def GetMany(self, startIndex: UInt32, items: FillArray[T]) -> UInt32:
        numcopied = 0
        for i in range(startIndex, startIndex + len(items)):
            if i >= len(self._lst):
                break
            items[numcopied] = self._lst[i]
            numcopied += 1
        return numcopied

    def ReplaceAll(self, items: PassArray[T]) -> Void:
        for v in items:
            self._addref(v)
        for v in self._lst:
            self._addref(v)
        self._lst[:] = items
        # FIXME: ?
        self._notify(VectorChangedEventArgs(CollectionChange.Reset, 0))

    def First(self) -> IIterator[T]:
        return Iterator[self._T](self._T(v) for v in self._lst)

    def add_VectorChanged(self, vhnd: VectorChangedEventHandler[T]) -> EventRegistrationToken:
        self._observers_count += 1
        self._observers[self._observers_count] = vhnd
        vhnd.AddRef()
        return EventRegistrationToken(self._observers_count)

    def remove_VectorChanged(self, token: EventRegistrationToken) -> Void:
        vhnd = self._observers.pop(token.Value)
        vhnd.Release()

    def _notify(self, args):
        for observer in self._observers.values():
            observer.Invoke(self, args)

    def _addref(self, value: T) -> None:
        if value and is_com_instance(self._T):
            value.AddRef()

    def _release(self, value: T) -> None:
        if value and is_com_instance(self._T):
            value.Release()


class Iterator(ComClass, IIterator[T]):
    def __init__(self, it) -> None:
        super().__init__(own=True)

        self._it = it
        try:
            self._current = next(self._it)
        except StopIteration:
            self._current = None

    def get_Current(self) -> T:
        if self._current is None:
            return None
        return self._current

    def get_HasCurrent(self) -> Boolean:
        return self._current is not None

    def MoveNext(self) -> Boolean:
        try:
            self._current = next(self._it)
            return True
        except StopIteration:
            self._current = None
            return False

    def GetMany(self, items: FillArray[T]) -> UInt32:
        numcopied = 0
        for i in range(len(items)):
            if self._current is None:
                break
            items[numcopied] = self._current
            numcopied += 1
            try:
                self._current = next(self._it)
            except StopIteration:
                self._current = None
        return numcopied


class VectorChangedEventArgs(ComClass, IVectorChangedEventArgs):
    def __init__(self, collection_change: CollectionChange, index: int) -> None:
        super().__init__(own=True)
        self._collection_change = collection_change
        self._index = index

    def get_CollectionChange(self) -> CollectionChange:
        return self._collection_change

    def get_Index(self) -> UInt32:
        return self._index
