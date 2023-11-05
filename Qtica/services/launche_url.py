from typing import Iterable, Union
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices


class LauncheURL:
    @staticmethod
    def open_url(*urls: list[Union[str, QUrl]]) -> Iterable[bool]:
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
    # @staticmethod
    # def open_app(self):
    #     """
    #     Linux: [.desktop, .AppImage, .boundle, .bin, .sh]
    #     MacOS: [.dmg]
    #     Windows: [.msi, .exe]            
    #     """
    #     ...