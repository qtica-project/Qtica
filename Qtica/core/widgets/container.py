from typing import TypeAlias, Union
from PySide6.QtWidgets import QLayout, QWidget
from .widget import AbstractWidget


ContainerChildType: TypeAlias = Union[QWidget, QLayout, list[QWidget]]


class AbstractContainer(AbstractWidget):
    def __init__(self, child: ContainerChildType = None, **kwargs):
        super().__init__(**kwargs)

        if not child:
            return

        if isinstance(child, QWidget):
            child.setParent(self)
        elif isinstance(child, QLayout):
            child.setProperty("parent", self)
            self.setLayout(child)
        elif isinstance(child, (list, tuple, set)):
            for sub in child:
                if isinstance(sub, QLayout):
                    self._throw_exception(sub)
                sub.setParent(self)
        else:
            self._throw_exception(child)

    def _throw_exception(self, cls) -> None:
        raise ValueError(f"invalid child value '{cls.__class__.__name__}', the 'QWidget' instance is the only supported value.")
