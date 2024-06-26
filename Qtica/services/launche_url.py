from typing import Iterable, Union

from qtpy.QtGui import QDesktopServices
from qtpy.QtCore import QUrl


class LauncheURL:
    @classmethod
    def open_url(cls, *urls: list[Union[str, QUrl]]) -> Iterable[bool]:
        '''
        Web URL      : http, https, ftp, etc...
        File URL     : file:///[file path]
        Map Location : geo:[...],[...]
        Phone Number : tel:[phone number]
        Any URL      : [URL...]
        '''
        for url in urls:
            yield QDesktopServices.openUrl(
                QUrl.fromUserInput(url)
                if isinstance(url, str)
                else url
            )

    ## work on!
    # @classmethod
    # def open_app(cls):
    #     '''
    #     Linux: [.desktop, .AppImage, .boundle, .bin, .sh]
    #     MacOS: [.dmg]
    #     Windows: [.msi, .exe]
    #     '''
    #     ...


class UrlOpen:
    def _open(self, url: Union[str, QUrl]) -> bool:
        return QDesktopServices.openUrl(
            QUrl.fromUserInput(url)
            if isinstance(url, str)
            else url
        )

    @classmethod
    def phone(cls, phone: Union[str, int]) -> bool:
        cls._open(f"tel:{QUrl.fromUserInput(str(phone))}")

    @classmethod
    def tel(cls, tel: Union[str, int]) -> bool:
        cls.phone(tel)

    @classmethod
    def geo(cls, x: Union[str, float], y: Union[str, float]) -> bool:
        cls._open(f"geo:{x},{y}")

    @classmethod
    def url(cls, url: Union[QUrl, str]) -> bool:
        cls._open(url)

    ## work on!
    # @classmethod
    # def app(cls, app: str) -> bool:
    #     ...