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
    MapChangedEventHandler,
)

from ._vector import Iterator
from ._win32 import Boolean, UInt32, Void
from ._winrt import ComClass, K, T, V, is_com_instance


class Map(ComClass, IMap[K, V], IMapView[K, V], IIterable[IKeyValuePair[K, V]], IObservableMap[K, V]):
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
        if key and is_com_instance(self._K):
            key.AddRef()
        if value and is_com_instance(self._V):
            value.AddRef()

    def _release(self, key: K, value: V) -> None:
        if key and is_com_instance(self._K):
            key.Release()
        if value and is_com_instance(self._V):
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
