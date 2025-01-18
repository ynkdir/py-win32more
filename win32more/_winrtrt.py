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


class Vector(ComClass, IVector[T], IVectorView[T], IIterable[T], IObservableVector[T]):
    __orig_class__ = GenericInitialize()

    def __init__(self, lst: list[T] | None = None) -> None:
        self._lst = lst
        self._observers = {}
        self._observers_count = 0

    def __init_generic__(self) -> None:
        super().__init__(own=True)

        self._type = get_args(self.__orig_class__)[0]

        if self._lst is None:
            self._lst = []

        if is_com_class(self._type):
            for v in self._lst:
                v.AddRef()

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
            self._lst[index].Release()
            value.AddRef()
        self._lst[index] = value
        self._notify(VectorChangedEventArgs(CollectionChange.ItemChanged, index))

    def InsertAt(self, index: UInt32, value: T) -> Void:
        if is_com_class(self._type):
            value.AddRef()
        self._lst.insert(index, value)
        self._notify(VectorChangedEventArgs(CollectionChange.ItemInserted, index))

    def RemoveAt(self, index: UInt32) -> Void:
        value = self._lst.pop(index)
        if is_com_class(self._type):
            value.Release()
        self._notify(VectorChangedEventArgs(CollectionChange.ItemRemoved, index))

    def Append(self, value: T) -> Void:
        self.InsertAt(len(self._lst), value)

    def RemoveAtEnd(self) -> Void:
        self.RemoveAt(len(self) - 1)

    def Clear(self) -> Void:
        if is_com_class(self._type):
            for v in self._lst:
                v.Release()
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
        if is_com_class(self._type):
            for v in items:
                v.AddRef()
        if is_com_class(self._type):
            for v in self._lst:
                v.Release()
        self._lst[:] = items
        # FIXME: ?
        self._notify(VectorChangedEventArgs(CollectionChange.Reset, 0))

    def First(self) -> IIterator[T]:
        return Iterator[self._type](self._lst)

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


class Iterator(ComClass, IIterator[T]):
    __orig_class__ = GenericInitialize()

    def __init__(self, lst: list[T] | None = None) -> None:
        self._lst = lst
        self._index = 0

    def __init_generic__(self) -> None:
        super().__init__(own=True)

        self._type = get_args(self.__orig_class__)[0]

    def get_Current(self) -> T:
        return self._lst[self._index]

    def get_HasCurrent(self) -> Boolean:
        return self._index < len(self._lst)

    def MoveNext(self) -> Boolean:
        self._index += 1
        return self._index < len(self._lst)

    def GetMany(self, items: FillArray[T]) -> UInt32:
        numcopied = 0
        for i in range(len(items)):
            if i >= len(self._lst):
                break
            items[numcopied] = self._lst[i]
            numcopied += 1
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
