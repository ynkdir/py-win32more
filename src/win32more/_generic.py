from __future__ import annotations

from typing import Generic, TypeVar, _GenericAlias, get_args, get_origin

from ._win32 import get_type_hints


# Cls[T]?
def is_generic_alias(cls):
    return isinstance(cls, _GenericAlias)


# Cls[T]()?
def is_generic_instance(obj):
    return isinstance(obj, Generic)


# types.get_original_bases >= 3.12
def get_original_bases(cls):
    return cls.__dict__.get("__orig_bases__", cls.__bases__)


def get_original_class(instance):
    return instance.__dict__.get("__orig_class__", instance.__class__)


def get_origin_or_itself(cls):
    return get_origin(cls) or cls


def generic_get_type_hints(prototype, cls):
    hints = get_type_hints(prototype)
    if is_generic_alias(cls):
        gs = GenericSpecializer.from_generic_alias(cls)
        hints = {key: gs.specialize_parameter(parameter) for key, parameter in hints.items()}
    return hints


class GenericSpecializer:
    def __init__(self, parameter_to_type_map: dict[TypeVar, type]) -> None:
        self._parameter_to_type_map = parameter_to_type_map

    @classmethod
    def from_generic_alias(cls, specialized_generic_alias: _GenericAlias) -> GenericSpecializer:
        parameters = get_origin(specialized_generic_alias).__parameters__
        args = get_args(specialized_generic_alias)
        return GenericSpecializer(dict(zip(parameters, args)))

    def specialize_generic_alias(self, parameterized_generic_alias: _GenericAlias) -> _GenericAlias:
        parameters = get_args(parameterized_generic_alias)
        args = self.specialize_parameters(parameters)
        return get_origin(parameterized_generic_alias)[tuple(args)]

    def specialize_parameters(self, parameters: list[_GenericAlias | TypeVar | type]) -> list[_GenericAlias | type]:
        return [self.specialize_parameter(parameter) for parameter in parameters]

    def specialize_parameter(self, parameter: _GenericAlias | TypeVar | type) -> _GenericAlias | type:
        if is_generic_alias(parameter):
            return self.specialize_generic_alias(parameter)
        elif isinstance(parameter, TypeVar):
            return self._parameter_to_type_map[parameter]
        else:
            return parameter


def get_specialized_bases(cls):
    if not is_generic_alias(cls):
        return get_original_bases(cls)
    gs = GenericSpecializer.from_generic_alias(cls)
    bases = []
    for base in get_original_bases(get_origin_or_itself(cls)):
        if get_origin(base) is Generic:
            continue
        bases.append(gs.specialize_parameter(base))
    return bases
