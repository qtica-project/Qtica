#!/usr/bin/python3

from PySide6.QtGui import QPaintEvent
from PySide6.QtWidgets import QWidget
from .base import BehaviorDeclarative


class AbstractPainter(BehaviorDeclarative):
	def __init__(self, child: QWidget) -> QWidget:
		self._parent = child
		self._parent.paintEvent = self._paint

	def update(self):
		self._repaint()

	def _super_paintEvent(self, event: QPaintEvent):
		return self._parent.__class__.paintEvent(self._parent, event)

	def _repaint(self):
		self._parent.update()

	def _paint(self, event: QPaintEvent):
		raise NotImplementedError


class PainterBase(AbstractPainter):
    pass