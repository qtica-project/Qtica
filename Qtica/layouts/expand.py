# coding:utf-8
from typing import Union
from ..core import AbstractQObject
from ..utils.alignment import Alignment

from qtpy.QtCore import QSize, QPoint, Qt, QEvent, QRect
from qtpy.QtWidgets import QLayout, QWidget, QLayoutItem


class _ExpandLayout(QLayout):
    """ Expand layout """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__items = []
        self.__widgets = []

    def addWidget(self, widget: QWidget):
        super().addWidget(widget)

        if widget in self.__widgets:
            return

        self.__widgets.append(widget)
        widget.installEventFilter(self)

    def addItem(self, item):
        self.__items.append(item)

    def count(self):
        return len(self.__items)

    def itemAt(self, index):
        if 0 <= index < len(self.__items):
            return self.__items[index]

        return None

    def takeAt(self, index):
        if 0 <= index < len(self.__items):
            self.__widgets.pop(index)
            return self.__items.pop(index)

        return None

    def expandingDirections(self):
        return Qt.Orientation.Vertical | Qt.Orientation.Horizontal

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        """ get the minimal height according to width """
        return self.__doLayout(QRect(0, 0, width, 0), False)

    def setGeometry(self, rect):
        super().setGeometry(rect)
        self.__doLayout(rect, True)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QSize()

        for w in self.__widgets:
            size = size.expandedTo(w.minimumSize())

        m = self.contentsMargins()
        size += QSize(m.left()+m.right(), m.top()+m.bottom())

        return size

    def __doLayout(self, rect, move):
        """ adjust widgets position according to the window size """
        margin = self.contentsMargins()
        x = rect.x() + margin.left()
        y = rect.y() + margin.top() + margin.bottom()
        width = rect.width() - margin.left() - margin.right()

        for i, w in enumerate(self.__widgets):
            y += ( i > 0) * self.spacing()
            if move:
                w.setGeometry(QRect(QPoint(x, y), QSize(width, w.height())))

            y += w.height()

        return y - rect.y()

    def eventFilter(self, obj, e):
        if obj in self.__widgets:
            if e.type() == QEvent.Type.Resize:
                ds = e.size() - e.oldSize()  # type:QSize
                if ds.height() != 0 and ds.width() == 0:
                    w = self.parentWidget()
                    w.resize(w.width(), w.height() + ds.height())

        return super().eventFilter(obj, e)


class ExpandLayout(AbstractQObject, _ExpandLayout):
    def __init__(self, 
                 *,
                 children: list[Union[QWidget, QLayoutItem, Alignment]] = None, 
                 **kwargs) -> None:
        _ExpandLayout.__init__(self)
        super().__init__(**kwargs)

        if not children:
            return

        for child in children:
            if isinstance(child, Alignment):
                _widget = child.child
                if isinstance(_widget, QWidget):
                    self.addWidget(_widget)
                elif isinstance(_widget, QLayoutItem):
                    self.addItem(_widget)

                self.setAlignment(_widget, child.alignment)

            elif isinstance(child, QLayoutItem):
                self.addItem(child)

            elif isinstance(child, QWidget):
                self.addWidget(child)