from typing import Union
from ..tools.icon import Icon
from ..enums.colors import Colors
from ..core import (
    AbstractIcons, 
    AbstractWidget, 
    AbstractContainer, 
    ContainerChildType
)

from qtpy.QtWidgets import QFrame
from qtpy.QtSvg import QSvgRenderer
from qtpy.QtSvgWidgets import QSvgWidget
from qtpy.QtCore import QByteArray, QSize, Qt
from qtpy.QtGui import (
    QColor, 
    QIcon, 
    QIconEngine, 
    QImage, 
    QMovie, 
    QPaintEvent, 
    QPainter, 
    QPixmap
)


class IconWidget(AbstractContainer, QFrame):
    def __init__(self,
                 *,
                 icon: Union[str,
                            QIcon,
                            QIconEngine,
                            QPixmap,
                            QImage,
                            AbstractIcons,
                            QMovie],
                 child: ContainerChildType = None,
                 alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter,
                 mode: QIcon.Mode = QIcon.Mode.Active,
                 state: QIcon.State = QIcon.State.On,
                 color: Union[QColor, Colors] = None,
                 size: Union[QSize, tuple, int] = None,
                 **kwargs):
        QFrame.__init__(self)
        super().__init__(child, **kwargs)

        if isinstance(icon, QMovie):
            self._icon = icon
            self._icon.setParent(self)
            icon.frameChanged.connect(self.update)
        else:
            self._icon = Icon(icon, color, size)
            self._alignment = alignment
            self._mode = mode
            self._state = state

    @property
    def icon(self) -> QIcon:
        return self._icon

    @icon.setter
    def icon(self, icon) -> None:
        self._icon = Icon(icon) if not isinstance(icon, QIcon) else icon

    def paintEvent(self, event: QPaintEvent) -> None:
        super().paintEvent(event)

        painter = QPainter(self)
        painter.setRenderHints(QPainter.RenderHint.Antialiasing 
                               | QPainter.RenderHint.SmoothPixmapTransform
                               | QPainter.RenderHint.TextAntialiasing)

        if isinstance(self.icon, QMovie):
            painter.drawPixmap(self.rect(),
                               self.icon.currentPixmap())
        else:
            painter.drawPixmap(self.rect(),
                               self._icon.pixmap(self.rect().size(),
                                                 self._mode,
                                                 self._state))

    def setIcon(self, icon) -> None:
        self._icon = Icon(icon)
        self.update()


class SvgWidget(AbstractWidget, QSvgWidget):
    def __init__(self, icon: Union[QByteArray, bytes, str] = None, **kwargs):
        QSvgWidget.__init__(self)

        if icon is not None:
            self.load(icon)

        super().__init__(**kwargs)

    @property
    def _renderer(self) -> QSvgRenderer:
        return self.renderer()