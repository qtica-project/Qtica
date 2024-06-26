import re
import json
import os.path

from string import Template
from typing import Mapping, Union
from PySide6.QtCore import QFile
from PySide6.QtGui import QGradient, QColor
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QWidget


INDENT_WIDTH: str = " " * 4
CUSTOM_PROPERTIES = (
    "border-radius",
    "box-shadow",
    "text-shadow"
)

class _QssTemplate(Template):
    delimiter = "--"


class QssProperty:
    @staticmethod
    def init_property(qss: dict[str, str], parent: QWidget = None):
        def _init_shadow(name: str):
            if (shadow := qss.get(name)) is not None:
                qss.pop(name)
                if isinstance(shadow, QGraphicsDropShadowEffect):
                    shadow.setParent(parent)
                    parent.setGraphicsEffect(shadow)
                else:
                    QssProperty.box_shadow(parent, shadow)

        if (br := qss.get("border-radius")) is not None:
            qss.pop("border-radius")
            qss.update(QssProperty.border_radius(br))

        _init_shadow("box-shadow")
        _init_shadow("text-shadow")

    @staticmethod
    def border_radius(value: str) -> dict[str, str]:
        args = value.split()
        _len = len(args)

        if _len == 1:
            return {"border-radius": args[0]}
        elif _len == 2:
            sides = ["top-left", "bottom-right"]
        elif _len == 3:
            args.insert(2, args[1])
            sides = ["top-left", "top-right", "bottom-left", "bottom-right"]
        elif _len == 4:
            sides = ["top-left", "top-right", "bottom-right", "bottom-left"]
        else:
            raise ValueError(f"'border-radius' takes 1-4 positional arguments but '{_len}' were given")

        return {"border-{}-radius".format(k): v for k, v in zip(sides, args)}

    @staticmethod
    def box_shadow(parent: QWidget, value: str):
        """box-shadow: offset-x [offset-y] [blur-radius] [spread-radius] [color] [inset]"""

        # Regular expression for parsing a single box-shadow value with optional px suffix
        box_shadow_re = re.compile(r"""
            (?P<dx>-?\d+)(px)? \s+          # Horizontal offset
            (?P<dy>-?\d+)(px)? \s*          # Vertical offset
            (?P<blur>-?\d+)?(px)? \s*             # Optional blur radius
            (?P<spread>-?\d+)?(px)? \s*           # Optional spread radius
            (?P<color>
                (?:rgba?\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*(?:,\s*\d*\.?\d+\s*)?\))|  # RGB/RGBA color
                (?:hsla?\(\s*\d+\s*,\s*\d+%\s*,\s*\d+%\s*(?:,\s*\d*\.?\d+\s*)?\))| # HSL/HSLA color
                (?:\#[0-9a-fA-F]{3,8})|           # Hex color
                (?:[a-zA-Z]+)                     # Named color
            )?
        """, re.VERBOSE)

        def shadow_color(color) -> QColor:
            if not color:
                return QColor("#000")

            # Match RGB/RGBA color
            rgba_match = re.match(r"rgba?\(([^)]+)\)", color)
            if rgba_match:
                values = rgba_match.group(1).split(',')
                if len(values) == 4:
                    values[-1] = str(int(eval(values[-1]) * 255))
                return QColor.fromRgb(*map(lambda x: int(x.strip()), values))

            # Match HSL/HSLA color
            hsla_match = re.match(r"hsla?\(([^)]+)\)", color)
            if hsla_match:
                values = hsla_match.group(1).split(',')
                if len(values) == 4:
                    values[-1] = str(int(eval(values[-1]) * 255))
                return QColor.fromHsl(*map(lambda x: int(x.strip().removesuffix('%')), values))

            return QColor.fromString(color)

        if (shadow_re := tuple(box_shadow_re.finditer(value.strip()))):
            shadow_re = shadow_re[0]

            dx = int(shadow_re.group("dx") or 0)

            shadow = QGraphicsDropShadowEffect()
            shadow.setXOffset(dx),
            shadow.setYOffset(int(shadow_re.group("dy") or dx)),
            shadow.setBlurRadius(int(shadow_re.group("blur") or 0))
            shadow.setColor(shadow_color(shadow_re.group("color")))

            if (spread := int(shadow_re.group("spread") or 0)):
                shadow.setBlurRadius(max(0, shadow.blurRadius() - spread))

        shadow.setParent(parent)
        parent.setGraphicsEffect(shadow)


class QStyleSheet:
    '''
    :param: qss: 
        - dict: {"background-color": "white"}
        - str : "QWidget { background-color: white; }"
        - str : ":/path/to/resoucre/file.qss",
        - str : "/path/to/local/file.qss"
        - str : "/path/to/local/file.json"

    ## e.g
    Label(
        qss=QStyleSheet(
            qss={
                "background-color": "--themeColor",
                "color": "white",
                "font-size": "24px"
            },
            vars={
                "themeColor": "blue"
            }
        )
    )
    :result:
        QLabel {
            background-color: blue;
            color: white;
            font-size: 24px;
        }

    '''

    def __init__(self, qss: Union[dict, str], vars: dict = None):
        self._qss = qss
        self._vars = vars
        self._temp = _QssTemplate("")
        self._parent = None

    def _set_parent(self, parent: object):
        self._parent = parent

    def _get_qss_from_str(self, qss: str) -> str:
        if qss.startswith(":") or os.path.exists(qss):
            file = QFile(qss)
            file.open(QFile.OpenModeFlag.ReadOnly)
            data = str(file.readAll(), "utf-8")

            # add .json support
            if qss.lower().endswith(".json"):
                data = self._get_qss_from_dict(json.loads(data))

            file.close()
            return data
        return qss

    def _get_qss_parent(self) -> str:
        _parent = self._parent.objectName().strip()
        if not _parent:
            _parent = self._parent.__class__.__base__.__name__
            return _parent
        return "#" + _parent

    def _get_qss_from_dict(self, qss: dict) -> str:
        style_sheet = ""
        _obj_style = ""

        QssProperty.init_property(qss, self._parent)

        for k, v in qss.items():
            if isinstance(v, dict) and not k.startswith(":"):
                raise ValueError("Invalid Qss Pseudo-States!")

            if k.startswith(("#", ".", "*")):
                raise ValueError("Invalid Qss property!")

            if isinstance(v, dict):
                QssProperty.init_property(v, self._parent)
                style_sheet += "%s%s {\n" % (self._get_qss_parent(), k)
                for sk, sv in v.items():
                    sv = self._property_value(sv)
                    style_sheet += f"{INDENT_WIDTH}{sk}: {sv};\n"
                style_sheet += "}\n"
            else:
                v = self._property_value(v)
                _obj_style += f"{INDENT_WIDTH}{k}: {v};\n"

        style_sheet += "%s {\n" % self._get_qss_parent()
        style_sheet += _obj_style
        style_sheet += "}\n"

        return style_sheet

    def _set_qss(self, qss: Union[dict, str]) -> None:
        if qss:
            _style = (self._get_qss_from_str(qss)
                    if isinstance(qss, str) 
                    else self._get_qss_from_dict(qss))

            if self._vars:
                self._temp.template = _style
                _style = self._temp.safe_substitute(self._vars)

            self._parent.setStyleSheet(_style)

    def update_vars(self, vars: dict) -> None:
        self._vars = vars
        self._set_qss(self._qss)

    def update_qss(self,
                   qss: Union[dict, str],
                   *,
                   save: bool = False) -> None:

        if self._qss is not None:
            if (isinstance(qss, dict) 
                and isinstance(self._qss, dict)):
                _qss = self._qss.copy()
                _qss.update(qss)
                self._qss = qss if save else self._qss
                _style = self._get_qss_from_dict(_qss)
            else:
                self._qss = qss if save else self._qss
                _style = self._get_qss_from_str(qss)
        else:
            _style = (
                self._get_qss_from_dict(qss)
                if isinstance(qss, dict)
                else
                self._get_qss_from_str(qss)
            )

            if save:
                self._qss = qss

        if self._vars:
            self._temp.template = _style
            self._temp.safe_substitute(_style)
            _style = self._temp.safe_substitute(self._vars)

        self._parent.setStyleSheet(_style)

    def restore_qss(self) -> None:
        if self._qss is not None:
            if isinstance(self._qss, dict):
                _style = self._get_qss_from_dict(self._qss)
            else:
                _style = self._get_qss_from_str(self._qss)

            if self._vars:
                self._temp.template = _style
                self._temp.safe_substitute(_style)
                _style = self._temp.safe_substitute(self._vars)

            self._parent.setStyleSheet(_style)
        else:
            self._parent.setStyleSheet("")

    def update(self, 
               qss: Union[dict, str], 
               vars: dict = None, 
               *,
               save: bool = False) -> None:

        if vars is not None:
            self.update_vars(vars)

        self.update_qss(qss, save=save)

    def restore(self) -> None:
        self.restore_qss()

    def style(cls,
              qss: Union[dict, str],
              vars: Mapping[str, object] = None) -> str:
        '''
        :param: qss: 
            - dict: {"background-color": "white"}
            - str : "QWidget { background-color: white; }"
            - str : ":/path/to/resoucre/file.qss",
            - str : "/path/to/local/file.qss"
            - str : "/path/to/local/file.json"
        '''
        if qss:
            _style = (cls._get_qss_from_str(qss)
                      if isinstance(qss, str) 
                      else cls._get_qss_from_dict(qss))
            if vars:
                _temp = _QssTemplate(_style)
                return _temp.safe_substitute(vars)
            return _style

    def _property_value(self, value: Union[str, QGradient]) -> str:
        if isinstance(value, QGradient):
            return value.to_qss()
        return value


class Qss(QStyleSheet):
    pass