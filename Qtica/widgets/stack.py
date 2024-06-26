from enum import Enum
from typing import Union
from ..core import AbstractWidget
from ..utils.alignment import Alignment
from ..core.objects.routes import Routes

from qtpy.QtWidgets import QFrame, QWidget, QLayout, QLayoutItem, QStackedLayout


class Stack(AbstractWidget, QFrame):
    StackingMode: Enum = QStackedLayout.StackingMode
    SizeConstraint: Enum = QStackedLayout.SizeConstraint

    def __init__(self, 
                 *,
                 children: Union[list[Union[QWidget, QLayout, QLayoutItem, Alignment]], Routes] = None,
                 stacking_mode: QStackedLayout.StackingMode = QStackedLayout.StackingMode.StackAll,
                 size_constraint: QStackedLayout.SizeConstraint = None,
                 spacing: int = None,
                 index: Union[int, str] = None,
                 menu_bar: QWidget = None,
                 **kwargs):
        QFrame.__init__(self)
        super().__init__(**kwargs)

        self._layout = QStackedLayout()

        if menu_bar is not None:
            self._layout.setMenuBar(menu_bar)

        if index is not None and isinstance(index, int):
            self._layout.setCurrentIndex(index)

        if spacing is not None:
            self._layout.setSpacing(spacing)

        if size_constraint is not None:
            self._layout.setSizeConstraint(size_constraint)

        if stacking_mode is not None:
            self._layout.setStackingMode(stacking_mode)

        self._set_children(children)
        self.setLayout(self._layout)

    def _set_children_from_list(self, children):
        for child in children:
            if isinstance(child, Alignment):
                _widget = child.child

                if isinstance(_widget, QWidget):
                    _func = self._layout.addWidget
                elif isinstance(_widget, QLayoutItem):
                    _func = self._layout.addItem
                elif isinstance(_widget, QLayout):
                    self.childLayoutWidget = QWidget(self)
                    _widget.setProperty("parent", self.childLayoutWidget)
                    self.childLayoutWidget.setLayout(_widget)
                    _func = self._layout.addWidget

                _func(_widget)
                self.setAlignment(_widget, child.alignment)

            elif isinstance(child, QLayoutItem):
                self._layout.addItem(child)

            elif isinstance(child, QWidget):
                self._layout.addWidget(child)

            elif isinstance(child, QLayout):
                self.childLayoutWidget = QWidget(self)
                child.setProperty("parent", self.childLayoutWidget)
                self.childLayoutWidget.setLayout(child)
                self._layout.addWidget(self.childLayoutWidget)

    def _set_children_from_dict(self, children):
        self.routes = Routes(**children.items()) if isinstance(children, dict) else children
        self.routes._set_stacked(self)

        for route, child in self.routes.widgets:
            if isinstance(child, Alignment):
                _widget = child.child

                if isinstance(_widget, QLayout):
                    _widget = QWidget(self)
                    _widget.setProperty("parent", _widget)
                    _widget.setLayout(_widget)

                self.routes.add(route, _widget)
                self.setAlignment(_widget, child.alignment)
            else:
                self.routes.add(route, child)

    def _set_children(self, children):
        if not children:
            return

        if isinstance(children, (Routes, dict)):
            return self._set_children_from_dict(children)
        return self._set_children_from_list(children)

    @property
    def stacked(self) -> QStackedLayout:
        return self._layout
