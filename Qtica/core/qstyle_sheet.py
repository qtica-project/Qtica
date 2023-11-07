#!/usr/bin/python3

from PySide6.QtCore import QFile
from typing import Union
from string import Template

import os


class _QssTemplate(Template):
    delimiter = "--"


class QStyleSheet:
    '''
    Label(
        uid="label",
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
    
    :param: qss: 
        - {"background-color": "white"}
        - ":/path/to/resoucre"
        - "/path/to/local/file"
        - QWidget { background-color: white;}
    '''

    def __init__(self, 
                 qss: Union[str, dict],
                 vars: dict = None):

        self._qss = qss
        self._vars = vars
        self._temp = _QssTemplate("")
        self._parent = None

    def _set_parent(self, parent: object):
        self._parent = parent

    def _get_qss_from_str(self, qss: str) -> str:
        if qss.startswith(":"):
            file = QFile(qss)
            file.open(QFile.OpenModeFlag.ReadOnly)
            data = str(file.readAll(), "utf-8")
            file.close()
            return data

        elif os.path.exists(qss):
            with open(qss, "r") as fr:
                return fr.read()

        return qss

    def _get_qss_from_dict(self, qss: dict) -> str:
        style_sheet = ""
        _obj_style = ""

        for k, v in qss.items():
            if isinstance(v, dict):
                style_sheet += "%s {\n" % k
                for sk, sv in v.items():
                    style_sheet += f"{sk}: {sv};\n"
                style_sheet += "}\n"
            else:
                _obj_style += f"{k}: {v};\n"

        if (obj_name := self._parent.objectName()):
            style_sheet += "#%s {\n" % obj_name
            style_sheet += _obj_style
            style_sheet += "}"

        elif not style_sheet:
            style_sheet = _obj_style

        return style_sheet

    def _set_qss(self, qss: Union[str, dict]) -> None:
        _style = (self._get_qss_from_str(qss)
                  if isinstance(qss, str) 
                  else self._get_qss_from_dict(qss))

        if self._vars:
            self._temp.template = _style
            self._temp.safe_substitute(_style)
            _style = self._temp.safe_substitute(self._vars)

        self._parent.setStyleSheet(_style)

    def update_vars(self, vars: dict) -> None:
        self._vars = vars
        self._set_qss(self._qss)

    def update_qss(self,
                   qss: Union[str, dict],
                   *,
                   save: bool = False) -> None:

        if (isinstance(qss, dict) 
            and isinstance(self._qss, dict)):
            _qss = self._qss.copy()
            _qss.update(qss)
            self._qss = qss if save else self._qss
            _style = self._get_qss_from_dict(_qss)
        else:
            _style = self._get_qss_from_str(qss)
            self._qss = qss if save else self._qss

        if self._vars:
            self._temp.template = _style
            self._temp.safe_substitute(_style)
            _style = self._temp.safe_substitute(self._vars)

        self._parent.setStyleSheet(_style)