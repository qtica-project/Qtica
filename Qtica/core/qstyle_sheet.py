#!/usr/bin/python3

from PySide6.QtCore import QFile
from string import Template
from typing import Union
import json
import os


class _QssTemplate(Template):
    delimiter = "--"


class QStyleSheet:
    '''
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
    
    :param: qss: 
        - dict: {"background-color": "white"}
        - str: "QWidget { background-color: white;}"
        - str: ":/path/to/resoucre/file.ext", 
                and "/path/to/local/file.ext",
                and "/path/to/local/file.json"

    :Qss result
        QLabel {
            background-color: blue;
            color: white;
            font-size: 24px;
        }
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

        for k, v in qss.items():
            if isinstance(v, dict) and not k.startswith(":"):
                raise ValueError("Invalid Qss parent!")

            if k.startswith(("#", ".", "*")):
                raise ValueError("Invalid Qss key value!")

            if isinstance(v, dict):
                style_sheet += "%s%s {\n" % (self._get_qss_parent(), k)
                for sk, sv in v.items():
                    style_sheet += f"\t{sk}: {sv};\n"
                style_sheet += "}\n"
            else:
                _obj_style += f"\t{k}: {v};\n"

        style_sheet += "%s {\n" % self._get_qss_parent()
        style_sheet += _obj_style
        style_sheet += "}\n"

        return style_sheet

    def _set_qss(self, qss: Union[str, dict]) -> None:
        if qss:
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
               qss: Union[str, dict], 
               vars: dict = None, 
               *,
               save: bool = False) -> None:

        if vars is not None:
            self.update_vars(vars)

        self.update_qss(qss, save=save)

    def restore(self) -> None:
        self.restore_qss()