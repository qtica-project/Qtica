#!/usr/bin/python3
# coding:utf-8

from PySide6.QtWidgets import QDialog, QGraphicsOpacityEffect, QGridLayout, QWidget
from PySide6.QtCore import QEasingCurve, QPropertyAnimation, Qt, QEvent
from PySide6.QtGui import QColor, QResizeEvent
from darkdetect import isDark
from ...core.base import WidgetBase


class MaskDialog:
    @classmethod
    def display(cls,
                parent: QWidget,
                child: QWidget,
                mask: QWidget = None,
                auto_close: bool = False,
                **kwargs):
        mask_dialog = _MaskDialog(parent, child, mask, auto_close, **kwargs)
        mask_dialog.show()


class _MaskDialog(WidgetBase, QDialog):
    """ Dialog box base class with a mask """

    def __init__(self, 
                 parent: QWidget,
                 child: QWidget,
                 mask: QWidget = None,
                 auto_close: bool = False,
                 **kwargs):
        QDialog.__init__(self, parent)
        super().__init__(**kwargs)

        self._grid_layout = QGridLayout(self)

        self._auto_close = auto_close

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
        self._mask.setStyleSheet(f'background:rgba({c}, {c}, {c}, 0.6)')
        self._mask.resize(self.size())

        self._grid_layout.addWidget(self.child)

        self.window().installEventFilter(self)

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
        self._mask.resize(self.size())

    def eventFilter(self, obj, e: QEvent):
        if obj is self.window():
            if e.type() == QEvent.Type.Resize:
                re = QResizeEvent(e)
                self.resize(re.size())

            if e.type() == QEvent.Type.MouseButtonPress and self._auto_close:
                self.close()

        return super().eventFilter(obj, e)

