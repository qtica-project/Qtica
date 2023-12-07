#!/usr/bin/python3

from typing import Any, Sequence
from .base import BehaviorDeclarative


class AbstractTool(BehaviorDeclarative):
    def __init__(self, 
                 *,
                 methods: Sequence[tuple[str, Any]] = None,
                 **kwargs):

        self._set_methods(methods)
        self._set_property_from_kwargs(**kwargs)

    def _set_methods(self, methods):
        if not methods:
            return

        for method in methods:
            if ((func := self._getattr(method[0])) is not None
                and func.__class__.__name__ in (
                "builtin_function_or_method",
                "method_descriptor",
                "function"
                )):
                func(method[1])

    def _set_property_from_kwargs(self, **kwargs):
        for (name, value) in kwargs.items():
            if hasattr(self, name):
                # handle set callables methods
                if name.lower().startswith("set"):
                    if ((func := self._getattr(name)) is not None
                        and func.__class__.__name__ in (
                        "builtin_function_or_method",
                        "method_descriptor",
                        "function"
                      )):
                        func(value)


class ToolBase(AbstractTool):
    pass