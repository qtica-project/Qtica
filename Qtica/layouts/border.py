from typing import Union
from ..enums.position import Positions
from ..enums.size import Sizes
from ..core import AbstractQObject
from ..tools.wrappers.border_layout import BorderLayoutWrapper

from qtpy.QtCore import QRect, QSize, Qt
from qtpy.QtWidgets import (
    QLayout,
    QLayoutItem,
    QWidget,
    QWidgetItem,
)


class _BorderLayout(QLayout):
    def __init__(self):
        super().__init__()

        self._list: list[BorderLayoutWrapper] = []

    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, item: QLayoutItem, position: Positions = Positions.left):
        self.add(item, position)

    def addWidget(self, widget: QWidget, position: Positions = Positions.left):
        super().addWidget(widget)
        self.add(QWidgetItem(widget), position)

    def add_item_wrapper(self, item: BorderLayoutWrapper):
        self._list.append(item)

    def expandingDirections(self) -> Qt.Orientation:
        return Qt.Orientation.Horizontal | Qt.Orientation.Vertical

    def hasHeightForWidth(self) -> bool:
        return False

    def count(self) -> int:
        return len(self._list)

    def itemAt(self, index: int) -> QLayoutItem:
        if index < len(self._list):
            wrapper: BorderLayoutWrapper = self._list[index]
            return wrapper.item
        return None

    def minimumSize(self) -> QSize:
        return self.calculate_size(Sizes.minimum)

    def setGeometry(self, rect: QRect):
        center: BorderLayoutWrapper = None
        east_width = 0
        west_width = 0
        north_height = 0
        south_height = 0

        super().setGeometry(rect)

        for wrapper in self._list:
            item: QLayoutItem = wrapper.item
            position: Positions = wrapper.pos

            if position == Positions.top:
                item.setGeometry(
                    QRect(
                        rect.x(), north_height, rect.width(), item.sizeHint().height()
                    )
                )

                north_height += item.geometry().height() + self.spacing()

            elif position == Positions.bottom:
                item.setGeometry(
                    QRect(
                        item.geometry().x(),
                        item.geometry().y(),
                        rect.width(),
                        item.sizeHint().height(),
                    )
                )

                south_height += item.geometry().height() + self.spacing()

                item.setGeometry(
                    QRect(
                        rect.x(),
                        rect.y() + rect.height() - south_height + self.spacing(),
                        item.geometry().width(),
                        item.geometry().height(),
                    )
                )

            elif position == Positions.center:
                center = wrapper

        center_height = rect.height() - north_height - south_height

        for wrapper in self._list:
            item: QLayoutItem = wrapper.item
            position: Positions = wrapper.pos

            if position == Positions.left:
                item.setGeometry(
                    QRect(
                        rect.x() + west_width,
                        north_height,
                        item.sizeHint().width(),
                        center_height,
                    )
                )

                west_width += item.geometry().width() + self.spacing()

            elif position == Positions.right:
                item.setGeometry(
                    QRect(
                        item.geometry().x(),
                        item.geometry().y(),
                        item.sizeHint().width(),
                        center_height,
                    )
                )

                east_width += item.geometry().width() + self.spacing()

                item.setGeometry(
                    QRect(
                        rect.x() + rect.width() - east_width + self.spacing(),
                        north_height,
                        item.geometry().width(),
                        item.geometry().height(),
                    )
                )

        if center:
            center.item.setGeometry(
                QRect(
                    west_width,
                    north_height,
                    rect.width() - east_width - west_width,
                    center_height,
                )
            )

    def sizeHint(self) -> QSize:
        return self.calculate_size(Sizes.hint)

    def takeAt(self, index: int):
        if 0 <= index < len(self._list):
            layout_struct: BorderLayoutWrapper = self._list.pop(index)
            return layout_struct.item
        return None

    def add(self, item: QLayoutItem, position: Positions):
        self._list.append(BorderLayoutWrapper(item, position))

    def calculate_size(self, size_type: Sizes):
        total_size = QSize()

        for wrapper in self._list:
            position = wrapper.pos

            item_size: QSize
            if size_type == Sizes.minimum:
                item_size = wrapper.item.minimumSize()
            elif size_type == Sizes.maximum:
                item_size = wrapper.item.maximumSize()
            else:
                item_size = wrapper.item.sizeHint()

            if position in (Positions.top, Positions.bottom, Positions.center):
                total_size.setHeight(total_size.height() + item_size.height())

            if position in (Positions.left, Positions.right, Positions.center):
                total_size.setWidth(total_size.width() + item_size.width())

        return total_size

    def wrapper(self, 
                child: QWidget | QLayoutItem, 
                pos: Positions = Positions.left) -> BorderLayoutWrapper:

        return BorderLayoutWrapper(child, pos)


class BorderLayout(AbstractQObject, _BorderLayout):
    def __init__(self,
                 *,
                 children: list[Union[QWidget, 
                                      QLayoutItem, 
                                      BorderLayoutWrapper]] = None,
                 **kwargs):
        _BorderLayout.__init__(self)
        super().__init__(**kwargs)

        if not children:
            return

        for child in children:
            if isinstance(child, BorderLayoutWrapper):
                self.add_item_wrapper(child)

            elif isinstance(child, QLayoutItem):
                self.addItem(child)

            elif isinstance(child, QWidget):
                self.addWidget(child)