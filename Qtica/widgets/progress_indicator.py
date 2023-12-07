from typing import Union
from PySide6.QtGui import QColor, QFont, QIcon, QPaintEvent, QPainter, QPen
from PySide6.QtCore import QRect, QRectF, Qt
from PySide6.QtWidgets import QWidget
from ..core import WidgetBase


class _ProgressIndicator(QWidget):
    def __init__(self,
                 maximum: int,
                 current: int = 1,
                 step_size: int = 35,
                 font_name: str = "Monospace",
                 steps_content: list[tuple[Union[str, QIcon]]] = None,
                 parent: QWidget | None = None) -> None:
        QWidget.__init__(self, parent)

        self._steps_content = steps_content
        self._current_step = current
        self._step_size = step_size
        self._max_step = maximum
        self._font_name = font_name

        self._style_color = QColor("#5AA9FF")
        self._line_color = QColor(Qt.GlobalColor.gray)
        self._text_color = QColor(Qt.GlobalColor.white)
        self._pen_width = 5

        self.setMinimumHeight(70)

    @property
    def current_step(self) -> int:
        return self._current_step

    @property
    def maximum_step(self) -> int:
        return self._max_step

    @property
    def _is_steps(self) -> bool:
        return self._steps_content is not None

    def setPenWidth(self, width: int):
        self._pen_width = width
        self.update()

    def setFontName(self, font: str):
        self._font_name = font
        self.update()

    def setStyleColor(self, color: QColor = QColor("#5AA9FF")):
        self._style_color = color
        self.update()

    def setLineColor(self, color: QColor = QColor(Qt.GlobalColor.gray)):
        self._line_color = color
        self.update()

    def setTextColor(self, color: QColor = QColor(Qt.GlobalColor.white)):
        self._text_color = color
        self.update()

    def setStepSize(self, size: int):
        self._step_size = size
        self.update()

    def setMaximumSteps(self, steps: int):
        if steps < 2:
            raise ValueError("invalid steps count!")

        self._max_step = steps
        self.update()

    def setCurrentStep(self, step: int):
        if (step > self.maximum_step or step < 1):
            return

        self._current_step = step
        self.update()

    def setNext(self):
        self.setCurrentStep(self.current_step + 1)

    def setPrev(self):
        self.setCurrentStep(self.current_step - 1)

    def _is_icon_step_value(self, value: object):
        return isinstance(value, QIcon)

    def _get_step_value(self, step: int):
        value = 0
        if step == self.current_step:
            value = 1
        elif step < self.current_step:
            value = 2

        return self._steps_content[step - 1][value]

    def paintEvent(self, event: QPaintEvent) -> None:
        qp = QPainter(self)
        qp.setRenderHint(
            QPainter.RenderHint.Antialiasing 
            | QPainter.RenderHint.TextAntialiasing
        )

        left = self.rect().left()
        line_width = 5

        for step in range(1, self._max_step + 1):
            left += ((self.width() / self._max_step)
                     if step > 1
                     else (self.width() / self._max_step / 2))

            if step == self._current_step:
                step_rect = QRectF(left,
                                self.height() // 3 - 5,
                                self._step_size + 10,
                                self._step_size + 10)

            else:
                step_rect = QRectF(left,
                                self.height() // 3,
                                self._step_size,
                                self._step_size)

            # draw rounded step
            if (self._is_steps and not 
                self._is_icon_step_value(self._get_step_value(step))):
                if step < self.current_step or step == self.current_step:
                    qp.setPen(QColor(Qt.GlobalColor.transparent))
                    qp.setBrush(self._style_color)
                else:
                    qp.setPen(QPen(self._line_color, self._pen_width))
                    qp.setBrush(QColor(Qt.GlobalColor.transparent))
            else:
                color = (self._style_color 
                         if step < self.current_step 
                         or step == self.current_step 
                         else self._line_color)
                qp.setPen(QPen(color, self._pen_width))
                qp.setBrush(QColor(Qt.GlobalColor.transparent))

            qp.drawEllipse(step_rect)

            if (not self._is_steps 
                or not self._is_icon_step_value(self._get_step_value(step))):
                # draw step number
                qp.setPen(self._text_color
                        if step == self.current_step 
                        or step < self.current_step
                        else self._style_color)
                font = QFont(self._font_name, 
                            (12 
                            if step == self.current_step 
                            else 11))
                font.setBold(step == self.current_step)
                qp.setFont(font)
                qp.drawText(step_rect,
                            Qt.AlignmentFlag.AlignCenter,
                            self._get_step_value(step)
                            if self._is_steps 
                            else str(step))
            else:
                # draw step icon
                qp.setPen(QColor(Qt.GlobalColor.transparent))
                icon_rect = QRect(
                    step_rect.left()   + (5 // 2) + .5,
                    step_rect.top()    + (5 // 2),
                    step_rect.width()  - 5,
                    step_rect.height() - 5
                )

                if step == self.current_step:
                    icon_rect = step_rect
                elif step < self.current_step:
                    icon_rect = QRect(
                        step_rect.left()   + 5,
                        step_rect.top()    + 5,
                        step_rect.width()  - 10,
                        step_rect.height() - 10
                    )

                mode = (QIcon.Mode.Active 
                        if step == self.current_step 
                        or step < self.current_step 
                        else QIcon.Mode.Disabled)

                self._get_step_value(step).paint(qp,
                                                 icon_rect,
                                                 Qt.AlignmentFlag.AlignCenter,
                                                 mode)

            # draw line
            if step < self._max_step:
                qp.setPen(QColor(Qt.GlobalColor.transparent))

                line_left = left + self._step_size
                if step == 1:
                    line_left = left + self._step_size

                if step == self._current_step:
                    line_rect = QRect(
                        line_left + 12,
                        self.height() // 3 + (self._step_size // 2),
                        (self.width() // self._max_step) - self._step_size - 10,
                        line_width
                    )
                else:
                    line_rect = QRect(
                        line_left,
                        self.height() // 3 + (self._step_size // 2),
                        (self.width() // self._max_step) - self._step_size,
                        line_width
                    )

                if step < self._current_step:
                    qp.setBrush(self._style_color)
                else:
                    qp.setBrush(QColor(Qt.GlobalColor.gray))

                qp.drawRect(line_rect)

        # return super().paintEvent(event)


class ProgressIndicator(WidgetBase, _ProgressIndicator):
    '''
    ProgressIndicator(
        maximum=3
        steps_content = [
            (content, current_content, previous_content),
            (content, current_content, previous_content),
            (content, current_content, previous_content)
        ]
    )
    '''

    def __init__(self,
                 *,
                 maximum: int,
                 current: int = 1,
                 step_size: int = 35,
                 font_name: str = "Monospace",
                 steps_content: list[tuple[Union[str, QIcon]]] = None,
                 style_color: QColor = None,
                 line_color: QColor = None,
                 text_color: QColor = None,
                 pen_width: int = None,
                 **kwargs):
        _ProgressIndicator.__init__(self, maximum, current, step_size, font_name, steps_content)
        super().__init__(**kwargs)

        if style_color is not None:
            self._style_color = style_color
        if line_color is not None:
            self._line_color = line_color
        if text_color is not None:
            self._text_color = text_color
        if pen_width is not None:
            self._pen_width = pen_width