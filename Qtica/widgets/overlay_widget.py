from typing import Union
from ..core import AbstractContainer, ContainerChildType

from qtpy.QtCore import Qt
from qtpy import QtCore, QtGui, QtWidgets


class OverlayWidget(AbstractContainer, QtWidgets.QWidget):
	"""
	Container-like widget which allows the user to overlay another widget on top of it. Switching on/off the overlay
	widget is done by setting the overlayHidden property.
	"""

	def __init__(self,
			  *,
			  overlay: Union[QtWidgets.QWidget, QtWidgets.QLayout],
			  child: ContainerChildType = None,
			  mouse_block: bool = True,
			  background: QtGui.QColor = QtGui.QColor(0, 0, 0, 200),
			  **kwargs) -> None:
		QtWidgets.QWidget.__init__(self)
		super().__init__(child, **kwargs)

		self._display_overlay = False
		self._overlay_widget = None
		self._overlay_widget_container: QtWidgets.QWidget = QtWidgets.QWidget(self)
		self._overlay_widget_container.setParent(self)
		self._overlay_widget_container.setWindowFlags(Qt.WindowType.Widget | Qt.WindowType.FramelessWindowHint)
		self._overlay_widget_container.setAutoFillBackground(True)
		self._overlay_widget_container.setContentsMargins(0, 0, 0, 0)
		self._overlay_widget_container.raise_()

		self._cur_background_color = None

		self.set_overlay_mouse_block(mouse_block)
		self.set_background_color(background)
		self.set_overlay_widget(overlay)

	def set_overlay_mouse_block(self, block: bool) -> None:
		"""Sets whether the overlay widget should block mouse events from reaching the underlying widget."""
		self._overlay_widget_container.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, not block)

	def get_overlay_mouse_block(self) -> bool:
		"""Returns whether the overlay widget blocks mouse events from reaching the underlying widget."""
		return self._overlay_widget_container.testAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

	def showEvent(self, event: QtGui.QShowEvent) -> None:
		"""On show, raise the overlay widget to make sure it is on top."""
		self._overlay_widget_container.raise_() #Make sure the overlay widget is on top
		return super().showEvent(event)

	def set_overlay_widget(self, overlay_widget: QtWidgets.QWidget) -> None:
		"""
		Sets the overlay widget to display on top of this widget.
		"""
		self._overlay_widget = overlay_widget
		self._overlay_widget_container.setLayout(QtWidgets.QVBoxLayout()) #Reset the layout to remove any previous

		if isinstance(overlay_widget, QtWidgets.QLayout):
			self._overlay_widget_container.layout().addLayout(overlay_widget)
		else:
			self._overlay_widget_container.layout().addWidget(overlay_widget)

		self._overlay_widget_container.resize(self.size())
		self._overlay_widget_container.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
		self._overlay_widget_container.raise_()

	def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
		"""
		#On resize, update the overlay widget size
		"""
		super().resizeEvent(event)
		self._overlay_widget_container.resize(self.size())

	def set_overlay_hidden(self, hidden: bool) -> None:
		"""
		Sets the overlay widget to be hidden or visible.
		"""
		self._overlay_widget_container.setHidden(hidden)

	def get_overlay_hidden(self) -> bool:
		"""
		Returns whether the overlay widget is hidden or visible.
		"""
		return self._overlay_widget_container.isHidden()

	def overlay_hide(self) -> None:
		self.set_overlay_hidden(True)

	def overlay_show(self) -> None:
		self.set_overlay_hidden(False)

	def set_background_color(self, color: QtGui.QColor) -> None:
		"""
		Sets the background color of the overlay widget.
		"""
		self._cur_background_color = color
		style = QtWidgets.QApplication.style()
		palette = style.standardPalette()
		palette.setColor(QtGui.QPalette.ColorRole.Window, color) #Background color
		self._overlay_widget_container.setPalette(palette)

	def get_background_color(self) -> QtGui.QColor | None:
		"""
		Returns the background color of the overlay widget.
		"""
		return self._cur_background_color

	overlayHidden = QtCore.Property(bool, get_overlay_hidden, set_overlay_hidden)
	overlayBlocksMouse = QtCore.Property(bool, get_overlay_mouse_block, set_overlay_mouse_block)
	overlayBackgroundColor = QtCore.Property(QtGui.QColor, get_background_color, set_background_color)
