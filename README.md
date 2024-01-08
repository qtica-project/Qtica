<p align="center">
  <a href="https://qticaproject.gitbook.io/qtica/">
    <img alt="Qtica" src="https://github.com/qtica-project/Qtica/blob/main/logo.png">
  </a>
</p>

<p align="center">
  A Fast Way to Done Your Idea!
</p>

<h2 align="center">
  v0.3.1
</h2>

# Qtica

Qtica is a Python library that offers a lightweight API built around native PySide6. It enables swift GUI prototyping utilizing contemporary declarative UI methods, all within Python.

## Features

- **Lightweight API:** Built around PySide6, Qtica offers a streamlined interface for GUI development.
- **Declarative UI Techniques:** Facilitates the use of modern UI techniques directly within Python.
- **Swift Prototyping:** Enables rapid GUI prototyping for efficient development.

## Installation

You can install Qtica via pip:

```bash
pip install qtica
```

## Usage

```python
import os
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QColor
from Qtica import BehaviorDec, Api
from Qtica.services import randomColor, colorToHex
from Qtica.widgets import MainWindow, Label, Application


class Window(BehaviorDec):
    def get_text_color(self, color: QColor) -> QColor:
        luma = ((0.299 * color.red()) + (0.587 * color.green()) + (0.114 * color.blue())) / 255
        return QColor(0, 0, 0) if luma > 0.5 else QColor(255, 255, 255)

    def update_background(self):
        bg_color = randomColor()
        fg_color = self.get_text_color(bg_color)

        Api.fetch("window").qss.update({"background-color": bg_color.name()})
        Api.fetch("label").qss.update({"color": fg_color.name()})

    def __init__(self):
        return MainWindow(
            uid="window",
            windowTitle="Welcome Qtica!",
            methods = [
              ("resize", QSize(400, 200))
            ],
            events = [
              ("mousePress", lambda _: self.update_background())
            ],
            home=Label(
                uid="label",
                setText=f"Hello {os.environ.get('USER', '')}, Welcome to Qtica.<br>Click me!",
                setTextFormat=Qt.TextFormat.RichText,
                setAlignment=Qt.AlignmentFlag.AlignCenter,
                qss={"font-size": "24px"}
            ),
            qss={"background-color": colorToHex(randomColor())},
        )

app = Application(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
```

## Documentation
For more information and detailed usage examples, refer to the [documentation](https://omamkaz.gitbook.io/qtica/).

## License

This project is licensed under the [GPL3 License](https://github.com/qtica-project/Qtica/blob/main/LICENSE).

## NOTE
Welcome to Qtica!

Thank you for choosing Qtica! Please be aware that this library is continuously evolving and is not yet considered stable as it's actively under development. We encourage you to use it for experimentation and kindly ask for your feedback, bug reports, suggestions, or improvements that align with your preferences. Your input is invaluable! 😊

Thank you for being a part of Qtica's development journey!