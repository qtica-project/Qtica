#!/usr/bin/python3

from PySide6.QtGui import QPaintEvent
from PySide6.QtWidgets import QWidget
from ..core.base import BehaviorDeclarative


class Painter(BehaviorDeclarative):
	def __init__(self, child: QWidget) -> QWidget:
		self._parent = child
		self._parent.paintEvent = self._paint
		return self._parent

	def update(self):
		self._repaint()

	def _repaint(self):
		self._parent.update()

	def _paint(self, event: QPaintEvent):
		raise NotImplementedError