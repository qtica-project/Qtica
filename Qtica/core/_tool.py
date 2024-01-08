#!/usr/bin/python3

from typing import Any, Sequence, Union
from ._declarative import AbstractDec
from ..utils._classes import Func, Args
from ._base import AbstractBase


class AbstractTool:
    '''
    AbstractTool means that the object doesn't contain base methods
    like setObjectName, setProperty ...etc
    '''
    def __init__(self, 
                 *,
                 methods: Sequence[Union[tuple[str, Any], Func]] = None,
                 **kwargs):

        self._set_methods(methods)
        self._set_property_from_kwargs(**kwargs)

    def _getattr(self, name: str, default: object = None) -> object:
        return AbstractBase._getattr(self, name, default)

    def _set_methods(self, methods):
        return AbstractBase._set_methods(self, methods)

    def _set_property_from_kwargs(self, **kwargs):
        for name, value in kwargs.items():
            if hasattr(self, name):
                # handle set callables methods
                if name.lower().startswith("set"):
                    if (func := self._getattr(name)) is not None and callable(func):
                        if isinstance(value, Args):
                            func(*value.args(), **value.kwargs())
                        else:
                            func(value)


class ToolDec(AbstractTool, AbstractDec):
    pass