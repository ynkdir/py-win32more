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


class Module(Protocol):
    @property
    def namespace(self) -> str:
        ...

    def __getitem__(self, name: str) -> ApiItem:
        ...

    def __contains__(self, name: str) -> bool:
        ...

    def items(self) -> Iterable[ApiItem]:
        ...

    def add(self, item: ApiItem) -> None:
        ...

    def emit_header(self) -> str:
        ...

    def enumerate_dependencies(self) -> Iterable[str]:
        ...


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
