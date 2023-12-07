from typing import List, Optional
from PySide6.QtGui import QColor, QResizeEvent
from PySide6.QtWidgets import QFrame, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget
from .side_bar_button import SideBarButton


_BG_FRAME_STYLESHEET = """\
QFrame#_side_bar_bg_frame {{
    background-color: {bg_color};
    border: none;
    border-radius: 8px;
}}
"""


class SideBar(QWidget):
    def __init__(self, 
                 parent: Optional[QWidget] = None,
                 bg_color: QColor = QColor("#191E23")) -> None:
        super().__init__(parent)

        # Define attributes
        self._first_button = True
        self._top_buttons: List[SideBarButton] = []
        self._bottom_buttons: List[SideBarButton] = []

        # Layout for this widget
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        # Background frame and its layout
        self._bg_frame = QFrame(self)
        self._bg_frame.setObjectName("_side_bar_bg_frame")
        self._bg_layout = QVBoxLayout(self._bg_frame)
        self._bg_layout.setContentsMargins(0, 15, 0, 15)
        self._bg_layout.setSpacing(0)
        self._layout.addWidget(self._bg_frame)

        # Top side bar buttons frame and its layout
        self._top_frame = QFrame(self._bg_frame)
        self._top_frame_layout = QVBoxLayout(self._top_frame)
        self._top_frame_layout.setContentsMargins(0, 0, 0, 0)
        self._top_frame_layout.setSpacing(0)
        self._bg_layout.addWidget(self._top_frame)

        # Vertical spacer between top and bottom bar
        self._vertical_spacer = QSpacerItem(0, 0, 
                                            QSizePolicy.Policy.Minimum, 
                                            QSizePolicy.Policy.Expanding)
        self._bg_layout.addItem(self._vertical_spacer)

        # Bottom side bar buttons frame and its layout
        self._bottom_frame = QFrame(self._bg_frame)
        self._bottom_frame_layout = QVBoxLayout(self._bottom_frame)
        self._bottom_frame_layout.setContentsMargins(0, 0, 0, 0)
        self._bottom_frame_layout.setSpacing(0)
        self._bg_layout.addWidget(self._bottom_frame)

        self.setBackgroundColor(bg_color)

    def setBackgroundColor(self, color: QColor("#191E23")) -> None:
        self._bg_frame.setStyleSheet(_BG_FRAME_STYLESHEET.format(bg_color=color.name()))

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)

        buttons: List[SideBarButton] = self.findChildren(SideBarButton)
        for button in buttons:
            button.setFixedSize(self.width(), 
                                self.width())

    def addButton(self, 
                  button: SideBarButton, 
                  alignment: SideBarButton.Alignment = SideBarButton.Alignment.top) -> None:

        button.setParent(self)
        button.clicked.connect(self._buttonCallback)  # type: ignore[attr-defined]

        if alignment == SideBarButton.Alignment.top:
            self._top_buttons.append(button)
            self._top_frame_layout.addWidget(button)
        elif alignment == SideBarButton.Alignment.bottom:
            self._bottom_buttons.append(button)
            self._bottom_frame_layout.addWidget(button)
        else:
            raise ValueError(
                "Invalid value for 'alignment'!"
                "Supported values are 'SideBarButton.Alignment.top' and 'SideBarButton.Alignment.bottom'."
            )

        # Select the first button as default
        if self._first_button:
            button.click()
            self._first_button = False

    def _buttonCallback(self):
        buttons: List[SideBarButton] = self.findChildren(SideBarButton)
        for button in buttons:
            if button == self.sender():
                button.setChecked(True)
            else:
                button.setChecked(False)
