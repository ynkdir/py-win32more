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
from ._comclass import ComClass, is_com_class
from ._hstr import hstr
from ._win32 import Boolean, UInt32, Void
from ._win32api import IInspectable
from ._winrt import (
    FillArray,
    K,
    PassArray,
    T,
    V,
)

_sentinel = object()


def _box_any(value):
    if isinstance(value, list):
        return List(value)
    if isinstance(value, dict):
        return Dict(value)
    return _box.box_value(value)


def _unbox_any(value):
    if value is None:
        return None

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

    def __contains__(self, value):
        for v in self:
            if v == value:
                return True
        return False

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def __reversed__(self):
        for i in reversed(range(len(self))):
            yield self[i]

    def __setitem__(self, index, value):
        self._inner.__setitem__(index, _box_any(value))

    def __delitem__(self, index):
        self._inner.__delitem__(index)

    def __iadd__(self, iterable):
        self.extend(iterable)
        return self

    def count(self, value):
        counter = 0
        for v in self:
            if v == value:
                counter += 1
        return counter

    def index(self, value):
        for i, v in enumerate(self):
            if v == value:
                return i
        raise ValueError(f"{value} is not in List")

    def insert(self, index, value):
        self._inner.InsertAt(index, _box_any(value))

    def append(self, value):
        self._inner.Append(_box_any(value))

    def clear(self):
        self._inner.Clear()

    def reverse(self):
        self._inner.ReplaceAll([_box_any(v) for v in reversed(self)])

    def extend(self, iterable):
        for v in iterable:
            self.append(v)

    def pop(self, index=-1):
        r = self[index]
        del self[index]
        return r

    def remove(self, value):
        del self[self.index(value)]


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

    def __eq__(self, other):
        return dict(self.items()) == dict(other.items())

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

    def clear(self):
        self._inner.Clear()

    def pop(self, key, default=_sentinel):
        if key in self:
            r = self[key]
            del self[key]
            return r
        if default is not _sentinel:
            return default
        raise KeyError(f"{key}")

    # NOTE: LIFO order is not guaranteed.  It depends on _inner object.
    def popitem(self):
        if len(self) == 0:
            raise KeyError("dictionary is empty")
        for k in self.keys():
            pass
        return (k, self.pop(k))

    def update(self, *args, **kwargs):
        if len(args) > 2:
            raise TypeError(f"update expected at most 1 argument, got {len(args)}")

        if len(args) == 1:
            if hasattr(args[0], "items"):
                # mapping
                for k, v in args[0].items():
                    self[k] = v
            else:
                # iterable
                for k, v in args[0]:
                    self[k] = v

        for k, v in kwargs.items():
            self[k] = v

    def setdefault(self, key, default=None):
        if key in self:
            return self[key]
        self[key] = default
        return default


class Vector(ComClass, IVector[T], IVectorView[T], IIterable[T], IObservableVector[T]):
    def __init__(self, lst: list[T] | None = None) -> None:
        super().__init__()

        self._T = self.__args[0]

        self._observers = {}
        self._observers_count = 0

        if lst is None:
            self._data = []
        else:
            self._data = [self._addref(v) for v in lst]

    def GetAt(self, index: UInt32) -> T:
        return self._data[index]

    def get_Size(self) -> UInt32:
        return len(self._data)

    def GetView(self) -> IVectorView[T]:
        return self.as_(IVector[self._T])

    def IndexOf(self, value: T, index: POINTER(UInt32)) -> Boolean:
        for i, v in enumerate(self._data):
            if v == value:
                index[0] = i
                return True
        return False

    def SetAt(self, index: UInt32, value: T) -> Void:
        self._data[index] = self._addref(value)
        self._notify(VectorChangedEventArgs(CollectionChange.ItemChanged, index))

    def InsertAt(self, index: UInt32, value: T) -> Void:
        self._data.insert(index, self._addref(value))
        self._notify(VectorChangedEventArgs(CollectionChange.ItemInserted, index))

    def RemoveAt(self, index: UInt32) -> Void:
        self._data.pop(index)
        self._notify(VectorChangedEventArgs(CollectionChange.ItemRemoved, index))

    def Append(self, value: T) -> Void:
        self.InsertAt(len(self._data), value)

    def RemoveAtEnd(self) -> Void:
        self.RemoveAt(len(self) - 1)

    def Clear(self) -> Void:
        self._data.clear()
        self._notify(VectorChangedEventArgs(CollectionChange.Reset, 0))

    def GetMany(self, startIndex: UInt32, items: FillArray[T]) -> UInt32:
        numcopied = 0
        for i in range(startIndex, startIndex + len(items)):
            if i >= len(self._data):
                break
            items[numcopied] = self._data[i]
            numcopied += 1
        return numcopied

    def ReplaceAll(self, items: PassArray[T]) -> Void:
        self._data = [self._addref(v) for v in items]
        self._notify(VectorChangedEventArgs(CollectionChange.Reset, 0))

    def First(self) -> IIterator[T]:
        return Iterator[self._T](self._T(v) for v in self._data)

    def add_VectorChanged(self, vhnd: VectorChangedEventHandler[T]) -> EventRegistrationToken:
        self._observers_count += 1
        self._observers[self._observers_count] = self._addref_vhnd(vhnd)
        return EventRegistrationToken(self._observers_count)

    def remove_VectorChanged(self, token: EventRegistrationToken) -> Void:
        self._observers.pop(token.Value)

    def _notify(self, args):
        for observer in self._observers.values():
            observer.Invoke(self, args)

    def _addref(self, value: T) -> T:
        if is_com_class(self._T) and value:
            value = self._T(value.value, own=True)
            value.AddRef()
        return value

    def _addref_vhnd(self, vhnd: VectorChangedEventHandler[T]) -> VectorChangedEventHandler[T]:
        vhnd = VectorChangedEventHandler[self._T](vhnd.value, own=True)
        vhnd.AddRef()
        return vhnd


class Iterator(ComClass, IIterator[T]):
    def __init__(self, it) -> None:
        super().__init__()

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
        super().__init__()
        self._collection_change = collection_change
        self._index = index

    def get_CollectionChange(self) -> CollectionChange:
        return self._collection_change

    def get_Index(self) -> UInt32:
        return self._index


class Map(ComClass, IMap[K, V], IMapView[K, V], IIterable[IKeyValuePair[K, V]], IObservableMap[K, V]):
    def __init__(self, dct: dict[K, V] | None = None) -> None:
        super().__init__()

        self._K, self._V = self.__args

        self._observers = {}
        self._observers_count = 0

        if dct is None:
            self._data = {}
        else:
            self._data = dict(self._addref(k, v) for k, v in dct.items())

    def Lookup(self, key: K) -> V:
        return self._data[key]

    def get_Size(self) -> UInt32:
        return len(self._data)

    def HasKey(self, key: K) -> Boolean:
        return key in self._data

    def GetView(self) -> IMapView[K, V]:
        return self.as_(IMapView[K, V])

    def Insert(self, key: K, value: V) -> Boolean:
        key, value = self._addref(key, value)
        r = key in self._data
        self._data[key] = value
        self._notify(MapChangedEventArgs[self._K](CollectionChange.ItemChanged, key))
        return r

    def Remove(self, key: K) -> Void:
        self._data.pop(key)
        self._notify(MapChangedEventArgs[self._K](CollectionChange.ItemRemoved, key))

    def Clear(self) -> Void:
        self._data.clear()
        self._notify(MapChangedEventArgs[self._K](CollectionChange.Reset, None))

    def Split(self, first: POINTER(IMapView[K, V]), second: POINTER(IMapView[K, V])) -> Void:
        raise NotImplementedError("Split")

    def First(self) -> IIterator[T]:
        return Iterator[IKeyValuePair[self._K, self._V]](
            KeyValuePair[self._K, self._V](k, v) for k, v in self._data.items()
        )

    def add_MapChanged(self, vhnd: MapChangedEventHandler[K, V]) -> EventRegistrationToken:
        self._observers_count += 1
        self._observers[self._observers_count] = self._addref_vhnd(vhnd)
        return EventRegistrationToken(self._observers_count)

    def remove_MapChanged(self, token: EventRegistrationToken) -> Void:
        self._observers.pop(token.Value)

    def _notify(self, args: MapChangedEventArgs) -> None:
        for observer in self._observers.values():
            observer.Invoke(self, args)

    def _addref(self, key: K, value: V) -> tuple[K, V]:
        if is_com_class(self._K) and key:
            key = self._K(key.value, own=True)
            key.AddRef()
        if is_com_class(self._V) and value:
            value = self._V(value.value, own=True)
            value.AddRef()
        return key, value

    def _addref_vhnd(self, vhnd: MapChangedEventHandler[K, V]) -> MapChangedEventHandler[K, V]:
        vhnd = MapChangedEventHandler[self._K, self._V](vhnd.value, own=True)
        vhnd.AddRef()
        return vhnd


class KeyValuePair(ComClass, IKeyValuePair[K, V]):
    def __init__(self, key: K, value: V) -> None:
        super().__init__()

        self._K, self._V = self.__args

        self._key, self._value = self._addref(key, value)

    def get_Key(self) -> K:
        return self._key

    def get_Value(self) -> V:
        return self._value

    def _addref(self, key: K, value: V) -> tuple[K, V]:
        if is_com_class(self._K) and key:
            key = self._K(key.value, own=True)
            key.AddRef()
        if is_com_class(self._V) and value:
            value = self._V(value.value, own=True)
            value.AddRef()
        return key, value


class MapChangedEventArgs(ComClass, IMapChangedEventArgs[K]):
    def __init__(self, collection_change: CollectionChange, key: K) -> None:
        super().__init__()

        self._K = self.__args[0]

        self._collection_change = collection_change
        self._key = self._addref(key)

    def get_CollectionChange(self) -> CollectionChange:
        return self._collection_change

    def get_Key(self) -> K:
        return self._key

    def _addref(self, key: K) -> K:
        if is_com_class(self._K) and key:
            key = self._K(key.value, own=True)
            key.AddRef()
        return key
