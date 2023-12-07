<p align="center">
  <a href="https://omamkaz.gitbook.io/qtica/">
    <img alt="Qtica" src="./logo.png">
  </a>
</p>

<p align="center">
  A Fast Way to Done Your Idea!
</p>

Qtica is a Python library that provides a lightweight API around native PySide6, allowing for lightning-fast GUI prototyping using modern declarative UI techniques entirely within Python.

# Documention

[Learn More About](https://omamkaz.gitbook.io/qtica/)

# Qtica Get Start

```python
#!/usr/bin/python3

import os
import sys
from PySide6.QtCore import QSize
from Qtica import BehaviorDeclarative, Api
from Qtica.tools import Alignment, Color
from Qtica.utils.colors import get_random_color, get_hex_from_color
from Qtica.widgets import (
  MainWindow,
  Container,
  Label,
  Application
)


class Window(BehaviorDeclarative):
  def update_background(self):
    bg_color = get_hex_from_color(*get_random_color())
    fg_color = get_hex_from_color(*get_random_color())
    Api.fetch("window").qss.update({"background-color": bg_color})
    Api.fetch("label").qss.update({"color": fg_color})

  def __init__(self):
    return MainWindow(
      uid="window",
      setWindowTitle="Qtica Get Start",
      methods = [
        ("resize", QSize(400, 200))
      ],
      events = [
        ("mousePressEvent", lambda event: self.update_background())
      ],
      home=Alignment(
          child=Label(
            uid="label",
            text=f"Hello {os.environ.get('USER', '')}, Welcome to Qtica!",
            qss={"font-size": "24px"}
          )
        ),
      qss={
        "background-color": get_hex_from_color(*get_random_color())
        },
      )

app = Application(
  arg=sys.argv
)
window = Window()
window.show()
sys.exit(app.exec())
```
