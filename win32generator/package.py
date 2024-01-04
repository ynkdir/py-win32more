from __future__ import annotations

from collections.abc import Iterable
from typing import Protocol


class Package:
    current: Package
    name: str
    directory: str
    is_onefile = False

    def __init__(self) -> None:
        Package.current = self

        self._modules: dict[str, Module] = {}

    def __getitem__(self, namespace: str) -> Module:
        return self._modules[namespace]

    def __setitem__(self, namespace: str, module: Module) -> None:
        self._modules[namespace] = module

    def __contains__(self, namespace: str) -> bool:
        return namespace in self._modules

    def modules(self) -> Iterable[Module]:
        return self._modules.values()

    @staticmethod
    def abs_pkg(name: str) -> str:
        return name.split(".")[-1] if Package.is_onefile else f"{Package.name}.{name}"


class Module:
    def __init__(self, namespace: str) -> None:
        self._namespace = namespace
        self._items: dict[str, ApiItem] = {}

    @property
    def namespace(self) -> str:
        return self._namespace

    def __getitem__(self, name: str) -> ApiItem:
        return self._items[name]

    def __contains__(self, name: str) -> bool:
        return name in self._items

    def items(self) -> Iterable[ApiItem]:
        return self._items.values()

    def add(self, item: ApiItem) -> None:
        raise NotImplementedError()

    def emit_header(self, import_namespaces: set[str]) -> str:
        raise NotImplementedError()

    def enumerate_imported_namespaces(self) -> Iterable[str]:
        for item in self._items.values():
            for fullname in item.enumerate_dependencies():
                namespace, name = fullname.rsplit(".", 1)
                yield namespace


class ApiItem(Protocol):
    @property
    def namespace(self) -> str:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def supported_architecture(self) -> list[str]:
        ...

    def enumerate_dependencies(self) -> Iterable[str]:
        ...

    def emit(self) -> str:
        ...
