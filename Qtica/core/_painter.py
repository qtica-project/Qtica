from ._declarative import AbstractDec

from qtpy.QtGui import QPaintEvent
from qtpy.QtWidgets import QWidget


class AbstractPainter(AbstractDec):
	def __init__(self, child: QWidget, **kwargs) -> QWidget:
		self._parent = child
		self._parent.paintEvent = self.paint

		return self._parent

	@property
	def _super(self) -> object:
		return self._parent.__class__

	def super_paintEvent(self, event: QPaintEvent) -> None:
		self._super.paintEvent(self._parent, event)

	def _paintEvent(self, event: QPaintEvent) -> None:
		self.super_paintEvent(event)

	def update(self) -> None:
		self.repaint()

	def repaint(self) -> None:
		self._parent.update()

	def paint(self, event: QPaintEvent) -> None:
		raise NotImplementedError