#!/usr/bin/python3
# coding:utf-8

from typing import Union
from PySide6.QtWidgets import QDialog, QGraphicsOpacityEffect, QGridLayout, QWidget, QApplication
from PySide6.QtCore import QEasingCurve, QPropertyAnimation, QSize, QTimer, Qt, QEvent
from PySide6.QtGui import QColor, QResizeEvent
from ...utils.theme_detect import isDark
from ...core import WidgetBase


class _MaskDialog(WidgetBase, QDialog):
    """ Dialog box base class with a mask """

    def __init__(self, 
                 parent: QWidget,
                 child: QWidget,
                 mask: QWidget = None,
                 auto_close: bool = False,
                 padding: Union[QSize, tuple, int] = 90,
                 timeout: int = None,
                 **kwargs):
        QDialog.__init__(self, parent)
        super().__init__(**kwargs)

        self._grid_layout = QGridLayout(self)
        self._auto_close = auto_close
        self._timeout = timeout
        self._padding = padding

        child.closeEvent = self._child_close_event

        if isinstance(padding, int):
            self._padding = QSize(padding, padding)

        if isinstance(padding, (tuple, list)):
            self._padding = QSize(*padding[:2])

        if child is not None:
            self.child = child

        if mask is not None:
            self._mask = mask
            self._mask.setParent(self)
        else:
            self._mask = QWidget(self)
            color = QColor(0, 0, 0, 76)
            self._mask.setStyleSheet(f"""
                background: rgba({color.red()}, \
                    {color.blue()}, \
                        {color.green()}, \
                            {color.alpha()})
                            """)

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setGeometry(0, 0, parent.width(), parent.height())

        c = 0 if isDark() else 255
        self._mask.setStyleSheet(f'background: rgba({c}, {c}, {c}, 0.6)')
        self._mask.resize(self.size())

        self._grid_layout.addWidget(self.child)

        self.window().installEventFilter(self)

    def _child_close_event(self, e):
        self.close()

    def showEvent(self, e):
        """ fade in """
        opacityEffect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(opacityEffect)

        opacityAni = QPropertyAnimation(opacityEffect, b'opacity', self)
        opacityAni.setStartValue(0)
        opacityAni.setEndValue(1)
        opacityAni.setDuration(200)
        opacityAni.setEasingCurve(QEasingCurve.Type.InSine)
        opacityAni.finished.connect(opacityEffect.deleteLater)
        opacityAni.start()

        super().showEvent(e)

        if self._timeout is not None:
            QTimer.singleShot(self._timeout, self.close)

    def closeEvent(self, e):
        """ fade out """
        self.child.setGraphicsEffect(None)

        opacityEffect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(opacityEffect)

        opacityAni = QPropertyAnimation(opacityEffect, b'opacity', self)
        opacityAni.setStartValue(1)
        opacityAni.setEndValue(0)
        opacityAni.setDuration(100)
        opacityAni.setEasingCurve(QEasingCurve.Type.OutCubic)
        opacityAni.finished.connect(self.deleteLater)
        opacityAni.start()

        super().closeEvent(e)

    def resizeEvent(self, e):
        self.child.blockSignals(True)
        self.child.setFixedSize(self.width() -  self._padding.width(),
                                self.height() - self._padding.height())
        self.child.blockSignals(False)
        self._mask.resize(self.size())

    def eventFilter(self, obj, e: QEvent):
        if obj is self.window():
            if e.type() == QEvent.Type.Resize:
                re = QResizeEvent(e)
                self.resize(re.size())

            if e.type() == QEvent.Type.MouseButtonPress and self._auto_close:
                self.close()

        return super().eventFilter(obj, e)


class MaskDialog:
    @classmethod
    def display(cls,
                *,
                child: QWidget,
                parent: QWidget = None,
                mask: QWidget = None,
                auto_close: bool = False,
                padding: Union[QSize, tuple, int] = 90,
                timeout: int = None,
                **kwargs):

        if not parent:
            parent = QApplication.activeWindow()

        mask_dialog = _MaskDialog(parent, 
                                  child, 
                                  mask, 
                                  auto_close,
                                  padding,
                                  timeout,
                                  **kwargs)
        mask_dialog.show()