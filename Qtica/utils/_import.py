import os.path
from imp import load_package


class Imports:
    @staticmethod
    def import_(path: str) -> object:
        """python function for import module from files"""
        return load_package(os.path.basename(path).split(".", 1)[0], path)

    @staticmethod
    def include(path: str) -> object:
        """python function for import module from files"""
        return Imports.import_(path)

    @staticmethod
    def import_plugin(path: str) -> object:
        """python function for import module from plugins"""
        return load_package(os.path.basename(path).split(".")[-1], path)

    @staticmethod
    def method(path: str) -> object:
        """
        >>> py = method("/path/to/script.py")
        >>> py("attribute")
        ...
        """

        def get(name: str, default: object = None) -> object:
            return getattr(Imports.import_(path), name, default)

        return get