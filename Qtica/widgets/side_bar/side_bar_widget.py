from typing import Optional
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QHBoxLayout, QStackedWidget, QWidget
from .side_bar import SideBar
from .side_bar_button import SideBarButton
from ...core import WidgetBase


class _SideBarWidget(QWidget):
    def __init__(self, 
                 parent: Optional[QWidget] = None,
                 stacked_widget: QStackedWidget = None) -> None:
        super().__init__(parent)

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        # Layout for this widget
        self._layout = QHBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        # Background frame and its layout
        self._bg_frame = QFrame(self)

        self._bg_frame_layout = QHBoxLayout(self._bg_frame)
        self._bg_frame_layout.setContentsMargins(5, 5, 5, 5)
        self._bg_frame_layout.setSpacing(10)
        self._layout.addWidget(self._bg_frame)

        # Menu bar
        self._side_bar = SideBar(self)
        self._side_bar.setFixedWidth(60)
        self._bg_frame_layout.addWidget(self._side_bar)

        # Stacked widget and its layout
        if stacked_widget is not None:
            self._stacked_widget = stacked_widget
            self._stacked_widget.setParent(self)
        else:
            self._stacked_widget = QStackedWidget(self)

        self._bg_frame_layout.addWidget(self._stacked_widget)

    def addPage(self, 
                page: QWidget,
                button: SideBarButton, 
                button_alignment: SideBarButton.Alignment = SideBarButton.Alignment.top) -> None:

        if not hasattr(button, "clicked"):
            raise ValueError("invalid button value!")

        self._side_bar.addButton(button, button_alignment)
        self._stacked_widget.addWidget(page)
        button.clicked.connect(lambda: self._stacked_widget.setCurrentWidget(page))  # type: ignore[attr-defined]


class SideBarItemWrapper:
    def __init__(self,
                 *,
                 page: QWidget,
                 button: SideBarButton | QWidget,
                 alignment: SideBarButton.Alignment = SideBarButton.Alignment.top):
        self.page = page
        self.button = button
        self.alignment = alignment


class SideBarWidget(WidgetBase, _SideBarWidget):
    def __init__(self, 
                 *,
                 children: list[SideBarItemWrapper] = None,
                 stacked_widget: QStackedWidget = None,
                 **kwargs):
        _SideBarWidget.__init__(self, None, stacked_widget)
        super().__init__(**kwargs)

        if children is not None:
            for child in children:
                self.addPage(
                    child.page,
                    child.button,
                    child.alignment
                )