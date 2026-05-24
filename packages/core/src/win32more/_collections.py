from __future__ import annotations

from ctypes import POINTER

from win32more.Windows.Foundation import EventRegistrationToken
from win32more.Windows.Foundation.Collections import (
    CollectionChange,
    IIterable,
    IIterator,
    IKeyValuePair,
    IMap,
    IMapChangedEventArgs,
    IMapView,
    IObservableMap,
    IObservableVector,
    IVector,
    IVectorChangedEventArgs,
    IVectorView,
    MapChangedEventHandler,
    VectorChangedEventHandler,
)

from . import _box
from ._hstr import hstr
from ._win32 import Boolean, UInt32, Void
from ._win32api import IInspectable
from ._winrt import (
    ComClass,
    FillArray,
    K,
    PassArray,
    T,
    V,
    is_com_instance,
)


def _box_any(value):
    if isinstance(value, list):
        return List(value)
    if isinstance(value, dict):
        return Dict(value)
    return _box.box_value(value)


def _unbox_any(value):
    ivector = value.try_as(IVector[IInspectable])
    if ivector is not None:
        return List(ivector)

    imap = value.try_as(IMap[hstr, IInspectable])
    if imap is not None:
        return Dict(imap)

    return _box.unbox_value(value)


class List(IInspectable):
    def __init__(self, inner: list | IVector[IInspectable] | None = None) -> None:
        super().__init__()

        if inner is None:
            self._inner = Vector[IInspectable]().as_(IVector[IInspectable])
        elif isinstance(inner, list):
            self._inner = Vector[IInspectable]([_box_any(v) for v in inner]).as_(IVector[IInspectable])
        else:
            self._inner = inner.as_(IVector[IInspectable])

        self.value = self._inner.value

    def __len__(self):
        return len(self._inner)

    def __getitem__(self, index):
        r = self._inner[index]
        if isinstance(r, list):
            return [_unbox_any(v) for v in r]
        return _unbox_any(r)

    def __setitem__(self, index, value):
        self._inner.__setitem__(index, _box_any(value))

    def __delitem__(self, index):
        self._inner.__delitem__(index)

    def insert(self, index, value):
        self._inner.InsertAt(index, _box_any(value))

    def append(self, value):
        self._inner.Append(_box_any(value))

    def clear(self, value):
        self._inner.Clear()


class Dict(IInspectable):
    def __init__(self, inner: dict | IMap[hstr, IInspectable] | None = None) -> None:
        super().__init__()

        if inner is None:
            self._inner = Map[hstr, IInspectable]().as_(IMap[hstr, IInspectable])
        elif isinstance(inner, dict):
            self._inner = Map[hstr, IInspectable]({k: _box_any(v) for k, v in inner.items()}).as_(
                IMap[hstr, IInspectable]
            )
        else:
            self._inner = inner.as_(IMap[hstr, IInspectable])

        self.value = self._inner.value

    def __iter__(self):
        return self._inner.__iter__()

    def __len__(self):
        return len(self._inner)

    def __getitem__(self, key):
        return _unbox_any(self._inner[key])

    def __setitem__(self, key, value):
        self._inner[key] = _box_any(value)

    def __delitem__(self, key):
        self._inner.__delitem__(key)

    def __contains__(self, key):
        return key in self._inner

    def items(self):
        for k, v in self._inner.items():
            yield k, _unbox_any(v)

    def keys(self):
        for k in self._inner.keys():
            yield k

    def values(self):
        for v in self._inner.values():
            yield _unbox_any(v)

    def get(self, key, default=None):
        return self._inner.get(key, default)

    def __eq__(self, other):
        return dict(self.items()) == dict(other.items())


class Vector(ComClass, IVector[T], IVectorView[T], IIterable[T], IObservableVector[T]):
    # FIXME: dirty hack
    # Return IVector for normal usage.
    # Implemented methods are expected to be called from com interface, not from python code directory.
    def __new__(cls, lst: list[T] | None = None) -> Vector[T] | IVector[T]:
        self = super().__new__(cls)
        self.__init__(lst)
        return self.as_(IVector[self._T])

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
        if value and is_com_instance(value):
            value.AddRef()

    def _release(self, value: T) -> None:
        if value and is_com_instance(value):
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


class Map(ComClass, IMap[K, V], IMapView[K, V], IIterable[IKeyValuePair[K, V]], IObservableMap[K, V]):
    # FIXME: dirty hack
    def __new__(cls, dct: dict[K, V] | None = None) -> Map[K, V] | IMap[K, V]:
        self = super().__new__(cls)
        self.__init__(dct)
        return self.as_(IMap[self._K, self._V])

    def __init__(self, dct: dict[K, V] | None = None) -> None:
        super().__init__(own=True)

        self._K, self._V = self.__args

        self._observers = {}
        self._observers_count = 0

        if dct is None:
            self._dict = {}
        else:
            self._dict = dict(dct)

        for k, v in self._dict.items():
            self._addref(k, v)

    def Lookup(self, key: K) -> V:
        return self._dict[key]

    def get_Size(self) -> UInt32:
        return len(self._dict)

    def HasKey(self, key: K) -> Boolean:
        return key in self._dict

    def GetView(self) -> IMapView[K, V]:
        return self.as_(IMapView[K, V])

    def Insert(self, key: K, value: V) -> Boolean:
        self._addref(key, value)
        r = key in self._dict
        self._dict[key] = value
        self._notify(MapChangedEventArgs[self._K](CollectionChange.ItemChanged, key))
        return r

    def Remove(self, key: K) -> Void:
        self._release(key, self._dict.pop(key))
        self._notify(MapChangedEventArgs[self._K](CollectionChange.ItemRemoved, key))

    def Clear(self) -> Void:
        for k, v in self._dict.items():
            self._release(k, v)
        self._dict.clear()
        self._notify(MapChangedEventArgs(CollectionChange.Reset, None))

    def Split(self, first: POINTER(IMapView[K, V]), second: POINTER(IMapView[K, V])) -> Void:
        raise NotImplementedError("Split")

    def First(self) -> IIterator[T]:
        return Iterator[IKeyValuePair[self._K, self._V]](
            KeyValuePair[self._K, self._V]((k, v)) for k, v in self._dict.items()
        )

    def add_MapChanged(self, vhnd: MapChangedEventHandler[K, V]) -> EventRegistrationToken:
        self._observers_count += 1
        self._observers[self._observers_count] = vhnd
        vhnd.AddRef()
        return EventRegistrationToken(self._observers_count)

    def remove_MapChanged(self, token: EventRegistrationToken) -> Void:
        vhnd = self._observers.pop(token.Value)
        vhnd.Release()

    def _notify(self, args: MapChangedEventArgs) -> None:
        for observer in self._observers.values():
            observer.Invoke(self, args)

    def _addref(self, key: K, value: V) -> None:
        if key and is_com_instance(key):
            key.AddRef()
        if value and is_com_instance(value):
            value.AddRef()

    def _release(self, key: K, value: V) -> None:
        if key and is_com_instance(key):
            key.Release()
        if value and is_com_instance(value):
            value.Release()


class KeyValuePair(ComClass, IKeyValuePair[K, V]):
    def __init__(self, item) -> None:
        super().__init__(own=True)
        self._key = item[0]
        self._value = item[1]

    def get_Key(self) -> K:
        return self._key

    def get_Value(self) -> V:
        return self._value


class MapChangedEventArgs(ComClass, IMapChangedEventArgs[K]):
    def __init__(self, collection_change: CollectionChange, key: K) -> None:
        super().__init__(own=True)
        self._collection_change = collection_change
        self._key = key

    def get_CollectionChange(self) -> CollectionChange:
        return self._collection_change

    def get_Key(self) -> K:
        return self._key
