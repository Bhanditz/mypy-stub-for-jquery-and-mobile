from typing import (Any, Callable, Dict, List, Text, Union,
                    overload, )

from d3 import D3Chart


if False:
    Any, Callable, Dict, List, Text
    D3Chart


# Primitive Values
JsPrims = Union[bool, int, float, Text]


class utils(object):  # {{{1
    @classmethod
    def windowResize(cls, fn):  # {{{1
        # type: (Callable[[], bool]) -> Any
        ...


class Models(object):  # {{{1
    def discreteBarChart(self):  # {{{1
        # type: () -> D3Chart
        ...

    def multiBarChart(self):  # {{{1
        # type: () -> D3Chart
        ...


models = Models()

# end of file {{{1
# vi: ft=python:ts=4:et:fdm=marker:nowrap
