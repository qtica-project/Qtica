#!/usr/bin/pythone3

from enum import IntEnum
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget
from PySide6.QtGui import QColor, QIcon, QMouseEvent, QPaintEvent, QPainter
from PySide6.QtCore import QRect, QRectF, Qt
from dataclasses import dataclass
from ..core import WidgetBase
from ..tools import Icon


class ThemeSwitchButton(WidgetBase, QWidget):
    '''
    :param: current_mode: False = Night, True = Light
    '''

    @dataclass
    class NightMode:
        bg_color: QColor = QColor("#303030")
        indicator_color: QColor = QColor("#FEFFFE")
        icon: QIcon = None

        @property
        def mode(self) -> bool:
            return False

    @dataclass
    class LightMode:
        bg_color: QColor = QColor("#FF9400")
        indicator_color: QColor = QColor("#FEFFFE")
        icon: QIcon = None

        @property
        def mode(self) -> bool:
            return True

    class Style(IntEnum):
        outline: int = 0
        inline: int = 1

    def __init__(self,
                 *,
                 night_mode: NightMode = None,
                 light_mode: LightMode = None,
                 style: Style = Style.inline,
                 current_mode: bool = False,
                 radius: int = 12,
                 **kwargs):
        QWidget.__init__(self)
        super().__init__(**kwargs)

        color = (Qt.GlobalColor.white
                 if style == ThemeSwitchButton.Style.inline 
                 else Qt.GlobalColor.black)

        self._night_mode = (night_mode 
                            if night_mode is not None 
                            else ThemeSwitchButton.NightMode(
                                icon=Icon(":/Qtica/icons/night.svg",
                                          color=color)))

        self._light_mode = (light_mode 
                            if light_mode is not None 
                            else ThemeSwitchButton.LightMode(
                                icon=Icon(":/Qtica/icons/light.svg",
                                          color=color)))

        self._current_mode = (self._light_mode
                              if current_mode
                              else self._night_mode)
        self._style = style
        self._radius = radius

        self.setContentsMargins(0, 0, 0, 0)
        self.setMinimumHeight(25)
        self.setMaximumHeight(40)

    @property
    def _is_outline(self) -> bool:
        return self._style == ThemeSwitchButton.Style.outline

    @property
    def _is_inline(self) -> bool:
        return self._style == ThemeSwitchButton.Style.inline

    @property
    def avg_size(self) -> int:
        return self.height() / 2

    def _get_rect(self, state: bool):
        _left = (
            self.width() - (self.avg_size + (self.avg_size / 2))
            if state
            else self.avg_size / 2
        )

        return QRect(_left,
                     self.height() / 2 - (self.avg_size / 2),
                     self.avg_size,
                     self.avg_size)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self._current_mode = (self._night_mode
                              if self._current_mode.mode
                              else self._light_mode)
        self.update()
        return super().mousePressEvent(event)

    def paintEvent(self, event: QPaintEvent) -> None:
        qp = QPainter(self)
        qp.setRenderHint(QPainter.RenderHint.Antialiasing)
        bg_rect = QRect(0,
                        0,
                        self.width() -  1,
                        self.height() - 1)

        if self._is_outline:
            icon_rect = self._get_rect(self._current_mode.mode)
            indicator_rect = QRectF(icon_rect.left() - (7 / 2),
                                   icon_rect.top() - (7 / 2),
                                   icon_rect.width() + 7,
                                   icon_rect.height() + 7)
        else:
            icon_rect = self._get_rect(not self._current_mode.mode)
            indicator_rect = self._get_rect(self._current_mode.mode)
            indicator_rect = QRectF(indicator_rect.left() - 2.5,
                                   indicator_rect.top() - 2.5,
                                   indicator_rect.width() + 5,
                                   indicator_rect.height() + 5)

        ## draw background
        qp.setPen(QColor(Qt.GlobalColor.transparent))
        qp.setBrush(self._current_mode.bg_color)
        qp.drawRoundedRect(bg_rect, 
                           self._radius, 
                           self._radius)

        ## draw indicator
        # draw color
        qp.setPen(Qt.GlobalColor.transparent)
        qp.setBrush(self._current_mode.indicator_color)
        qp.drawEllipse(indicator_rect)

        # draw icon
        self._current_mode.icon.paint(qp, 
                                      icon_rect,
                                      Qt.AlignmentFlag.AlignCenter)

        if self._style == ThemeSwitchButton.Style.outline:
            icon = (
                self._night_mode.icon
                if self._current_mode.mode
                else self._light_mode.icon
            )
            icon.paint(qp,
                       self._get_rect(not self._current_mode.mode),
                       Qt.AlignmentFlag.AlignCenter)



class __Test(QWidget):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self._layout = QVBoxLayout(self)
        self.switch_btn = ThemeSwitchButton(style=ThemeSwitchButton.Style.outline)
        self._layout.addWidget(self.switch_btn)

def main():
    import sys
    app = QApplication(sys.argv)
    window = __Test()
    window.resize(100, 50)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()