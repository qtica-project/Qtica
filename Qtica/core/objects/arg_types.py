from typing import Any, Callable, Union


class Func:
    def __init__(self, func: Union[Callable, str], *args, **kwargs):
        self._func = func
        self._args = args
        self._kwargs = kwargs

    def func(self) -> Union[Callable, str]:
        return self._func

    def args(self) -> tuple[Any]:
        return self._args

    def kwargs(self) -> dict[str, Any]:
        return self._kwargs


class Args:
    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs

    def args(self) -> list[Any]:
        return self._args

    def kwargs(self) -> dict[str, Any]:
        return self._kwargs


class MArgs:
    def __init__(self, *args: Union[Args, Any]):
        self._args = args

    def args(self) -> list[Union[Args, Any]]:
        return self._args
