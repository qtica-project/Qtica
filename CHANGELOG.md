# Changelog

## Unreleased - (Soon!)

### Added

- parent_child_widgets.py example

## 0.1.1 - (2023-11-05)

### Added

- #### PySide6 Built-in Widgets

  - QApplication
  - QPushButton
  - QLabel
  - QFrame
  - QMainWindow
  - QSystemTrayIcon
  - QGraphicsView
  - QWidget
  - QQuickWidget
  - QQuickView
  - QGraphicsOpacityEffect
  - QGraphicsDropShadowEffect
  - QGraphicsColorizeEffect
  - QGraphicsBlurEffect
  - QFormLayout
  - QGridLayout
  - QHBoxLayout
  - QStackedLayout
  - QVBoxLayout

- #### PySide6 Additional Widgets

  - WigglyWidget
  - WaterRippleProgressBar
  - WaterProgressBar
  - ProgressIndicator
  - MovieView
  - MetroCircleProgress
  - ElidingLabel
  - FramelessWindow
  - RoutingWindow
  - TeachingTip
  - SlidingStackedWidget
  - SideBarWidget
  - TerminalWidget
  - NavBarWidget
  - SilentTextDialog
  - LargTextDialog
  - ColourfulProgressBar
  - OutsideNeumorphismEffect
  - InsideNeumorphismEffect
  - FlowLayout
  - ExpandLayout

- #### PySide6 Built-in Core

  - QPropertyAnimation

- #### PySide6 Additional Core
  - StyleAnimation
  - ProgressStyleAnimation
  - Animation

## 0.1.2 - (2023-11-07)

### Added

- Qtica `logo.png`
- version_generator.py example
- status_edge.py example
- resources, and fonts into the `Application` class.
- `tools.Painter class`
- `tools.PaintStatusEdge`
- `widgets.FramelessWindowSizeGrip`

### Changed

- `enums.Sizes.size_hint` -> `enums.Sizes.hint`

### Fixed

- `core.BehaviorDeclarative`, no uid in `__init__` parameters

## 0.1.3 - (2023-11-12)

### Added

- `widgets.ThemeSwitchButton`
- `enums.AbstractIcons` to make enum icons that work with Qtica tools
- `tools.Icon`
- `utils.color.DetectImageColors`, using to get an image colors map.
- `utils.color.get_image_average_color`, get an image rgb color
- `widgets.LineEdit`
- `core.WidgetBase` effect argument.
- `core.AbstractBase` \*\*kwargs, can now accept set value for method.
- `widgets.ScrollArea`
- get_start.py example

### Changed

- `Theme.system_theme` to static method type.
- `effects.*` from ObjectDeclarative class type to `ObjectBase`
- `utils.color.get_hex_from_color` color arg to \*rgb arg

### Fixed

- pixmap error when you try to add `QIcon` to `tools.Icon` with color value.

## 0.1.4 (2023-11-24)

### Added

- extras `icons` modules `elusive` `feather` `fluent` `fontawesome` `material`
- `widgets.FramelessWindowSizeGrip` edge option.
- `utils.methods.qt_corner_to_edge` convert Qt.Corner inputs to Qt.Edge values.
- `widgets.StackedWidget` QStackedWidget built-in PySide6 class
- `widgets.IconWidget`
- `widgets.MaskDialog`

### Fixed

- `widgets.FramelessWindow` window geometry changed when move window.
- `widgets.FramelessWindowSizeGrip` cursor shape for SizeGrip hover.
- `tools.Icon` list index out of range, when used colored icon

### Updated

- `widgets.NavBarButton` it's now subclass from `core.WidgetBase`
