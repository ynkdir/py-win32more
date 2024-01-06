from __future__ import annotations

from collections.abc import Iterable
from typing import Protocol


class Package:
    def __init__(self, name, is_onefile=False) -> None:
        self.name = name
        self.is_onefile = is_onefile
        self._modules: dict[str, Module] = {}

    def __getitem__(self, namespace: str) -> Module:
        return self._modules[namespace]

    def __setitem__(self, namespace: str, module: Module) -> None:
        self._modules[namespace] = module

    def __contains__(self, namespace: str) -> bool:
        return namespace in self._modules

    def modules(self) -> Iterable[Module]:
        return self._modules.values()

    def abs_pkg(self, name: str) -> str:
        return name.split(".")[-1] if self.is_onefile else f"{self.name}.{name}"


class Module:
    def __init__(self, namespace: str, package: Package) -> None:
        self._namespace = namespace
        self._package = package
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

    def emit_header(self) -> str:
        raise NotImplementedError()

    def enumerate_dependencies(self) -> Iterable[str]:
        for item in self._items.values():
            yield from item.enumerate_dependencies()


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
