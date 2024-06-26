from ._declarative import AbstractDec
from ._base import AbstractBase, MethodsType


class AbstractTool:
    '''
    AbstractTool means that the object doesn't contain base methods
    like setObjectName, setProperty ...etc
    '''
    def __init__(self, methods: MethodsType = None, **kwargs):
        self._set_methods(methods)
        self._set_property_from_kwargs(**kwargs)

    def _getattr(self, name: str, default: object = None) -> object:
        return AbstractBase._getattr(self, name, default)

    def _set_methods(self, methods) -> None:
        return AbstractBase._set_methods(self, methods)

    def _set_property_from_kwargs(self, **kwargs) -> None:
        for name, value in kwargs.items():
            if hasattr(self, name):
                # handle set callable methods
                if name.startswith("set"):
                    AbstractBase._handle_set_methods(self, name, value)

                # handle add callable methods
                elif name.startswith("add"):
                    AbstractBase._handle_add_methods(self, name, value)


class ToolDec(AbstractTool, AbstractDec):
    pass